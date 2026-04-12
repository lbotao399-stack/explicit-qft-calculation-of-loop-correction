from __future__ import annotations

from collections import defaultdict
import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle
import networkx as nx
import numpy as np


plt.rcParams.update(
    {
        "font.family": "STIXGeneral",
        "mathtext.fontset": "stix",
        "figure.facecolor": "white",
        "axes.facecolor": "white",
    }
)


ROOT = Path(__file__).resolve().parents[1]
COARSE_JSON = ROOT / "assets" / "step4" / "n1_sym_euclidean" / "q1_fpp_fpp_2loop_coarse_classes.json"
OUT = ROOT / "assets" / "step4" / "n1_sym_euclidean" / "q1_fpp_fpp_2loop_top10.png"
OUT_PDF = ROOT / "assets" / "step4" / "n1_sym_euclidean" / "q1_fpp_fpp_2loop_top10.pdf"


def parse_endpoint(text: str):
    return text.split(":", 1)


def field_from_endpoint(vertex_id: str, port_name: str):
    if vertex_id == "O":
        if "lambdabar" in port_name:
            return "lbar"
        return "A"
    vertex_type = vertex_id.split("#", 1)[0]
    if vertex_type in {"V_AAA", "V_AAAA"}:
        return "A"
    if vertex_type == "V_A_lambda_lambdabar":
        return {"A": "A", "lambda": "lam", "lambdabar": "lbar"}[port_name]
    if vertex_type == "V_cbar_A_c":
        return {"A": "A", "c": "c", "cbar": "cbar"}[port_name]
    raise ValueError(f"unknown endpoint: {vertex_id}:{port_name}")


def species_label(kind: str):
    if kind == "A":
        return r"$A$"
    if kind == "fermion":
        return r"$(\lambda,\widetilde{\lambda})$"
    if kind == "ghost":
        return r"$(c,\bar c)$"
    raise ValueError(kind)


def external_label(field: str):
    if field == "A":
        return r"$A$"
    if field == "lbar":
        return r"$\widetilde{\lambda}$"
    if field == "lam":
        return r"$\lambda$"
    if field == "c":
        return r"$c$"
    if field == "cbar":
        return r"$\bar c$"
    return field


def build_skeleton(entry):
    g = nx.MultiGraph()
    g.add_node("O", kind="operator")
    action_types = {}

    for contraction in entry["representative_internal_contractions"]:
        for endpoint in (contraction["from"], contraction["to"]):
            vertex_id, _ = parse_endpoint(endpoint)
            if vertex_id == "O":
                continue
            action_types[vertex_id] = vertex_id.split("#", 1)[0]

    for ext in entry["representative_external_ports"]:
        vertex_id, _ = parse_endpoint(ext["port"])
        if vertex_id == "O":
            continue
        action_types[vertex_id] = vertex_id.split("#", 1)[0]

    for vertex_id in sorted(action_types):
        g.add_node(vertex_id, kind="vertex", vertex_type=action_types[vertex_id])

    for edge_id, contraction in enumerate(entry["representative_internal_contractions"], start=1):
        v1, p1 = parse_endpoint(contraction["from"])
        v2, p2 = parse_endpoint(contraction["to"])
        f1 = field_from_endpoint(v1, p1)
        f2 = field_from_endpoint(v2, p2)
        arrow = None
        if contraction["kind"] == "fermion":
            arrow = (v1, v2) if (f1, f2) == ("lam", "lbar") else (v2, v1)
        elif contraction["kind"] == "ghost":
            arrow = (v1, v2) if (f1, f2) == ("c", "cbar") else (v2, v1)
        g.add_edge(
            v1,
            v2,
            key=f"int{edge_id}",
            role="internal",
            kind=contraction["kind"],
            arrow=arrow,
        )

    for edge_id, ext in enumerate(entry["representative_external_ports"], start=1):
        v, _ = parse_endpoint(ext["port"])
        ext_id = f"ext{edge_id}"
        g.add_node(ext_id, kind="external", field=ext["field"])
        arrow = None
        if ext["field"] in {"lam", "lbar", "c", "cbar"}:
            arrow = (v, ext_id)
        g.add_edge(
            v,
            ext_id,
            key=f"ext{edge_id}",
            role="external",
            kind=ext["field"],
            arrow=arrow,
        )

    return g


def bezier_points(p0, p1, rad=0.0, n=200):
    p0 = np.array(p0, dtype=float)
    p1 = np.array(p1, dtype=float)
    mid = 0.5 * (p0 + p1)
    d = p1 - p0
    length = np.linalg.norm(d)
    if length == 0:
        return np.repeat(p0[None, :], n, axis=0)
    normal = np.array([-d[1], d[0]]) / length
    control = mid + rad * length * normal
    t = np.linspace(0.0, 1.0, n)
    pts = ((1 - t) ** 2)[:, None] * p0 + (2 * (1 - t) * t)[:, None] * control + (t**2)[:, None] * p1
    return pts


def point_and_tangent(p0, p1, rad=0.0, t=0.55):
    p0 = np.array(p0, dtype=float)
    p1 = np.array(p1, dtype=float)
    mid = 0.5 * (p0 + p1)
    d = p1 - p0
    length = np.linalg.norm(d)
    if length == 0:
        return p0, np.array([1.0, 0.0])
    normal = np.array([-d[1], d[0]]) / length
    control = mid + rad * length * normal
    pos = ((1 - t) ** 2) * p0 + 2 * (1 - t) * t * control + (t**2) * p1
    tan = 2 * (1 - t) * (control - p0) + 2 * t * (p1 - control)
    return pos, tan


def draw_plain_curve(ax, p0, p1, rad=0.0, lw=2.2, ls="-"):
    pts = bezier_points(p0, p1, rad=rad)
    ax.plot(pts[:, 0], pts[:, 1], color="black", lw=lw, ls=ls, solid_capstyle="round", zorder=2)


def draw_wavy_curve(ax, p0, p1, rad=0.0, amplitude=0.035, waves=6.5, lw=2.0):
    pts = bezier_points(p0, p1, rad=rad, n=240)
    tangents = np.gradient(pts, axis=0)
    lengths = np.linalg.norm(tangents, axis=1)
    lengths[lengths == 0] = 1.0
    normals = np.stack([-tangents[:, 1] / lengths, tangents[:, 0] / lengths], axis=1)
    t = np.linspace(0.0, 1.0, len(pts))
    phase = amplitude * np.sin(2 * np.pi * waves * t)
    pts = pts + normals * phase[:, None]
    ax.plot(pts[:, 0], pts[:, 1], color="black", lw=lw, solid_capstyle="round", zorder=2)


def draw_arrow_on_curve(ax, p0, p1, rad=0.0, t0=0.42, t1=0.62, scale=13):
    pos0, _ = point_and_tangent(p0, p1, rad=rad, t=t0)
    pos1, _ = point_and_tangent(p0, p1, rad=rad, t=t1)
    patch = FancyArrowPatch(
        pos0,
        pos1,
        arrowstyle="-|>",
        mutation_scale=scale,
        linewidth=1.5,
        color="black",
        shrinkA=0,
        shrinkB=0,
        zorder=4,
    )
    ax.add_patch(patch)


def edge_offsets(count):
    if count == 1:
        return [0.0]
    if count == 2:
        return [-0.18, 0.18]
    if count == 3:
        return [-0.28, 0.0, 0.28]
    if count == 4:
        return [-0.36, -0.12, 0.12, 0.36]
    return np.linspace(-0.42, 0.42, count).tolist()


def layout_positions(g):
    core_nodes = [node for node, data in g.nodes(data=True) if data["kind"] in {"operator", "vertex"}]
    simple = nx.Graph()
    for node in core_nodes:
        simple.add_node(node)
    for u, v, _k, data in g.edges(keys=True, data=True):
        if data["role"] != "internal":
            continue
        if simple.has_edge(u, v):
            simple[u][v]["weight"] += 1.0
        else:
            simple.add_edge(u, v, weight=1.0)

    pos = nx.spring_layout(simple, seed=7, weight="weight", iterations=300)
    pos["O"] = np.array([-1.5, 0.0])

    others = [node for node in core_nodes if node != "O"]
    if others:
        sub = np.array([pos[node] for node in others], dtype=float)
        sub[:, 0] = 1.8 * sub[:, 0] + 0.35
        sub[:, 1] = 1.6 * sub[:, 1]
        for node, coords in zip(others, sub):
            pos[node] = coords

    centroid = np.mean(np.array([pos[node] for node in core_nodes]), axis=0)
    ext_counts = {}
    for node, data in g.nodes(data=True):
        if data["kind"] != "external":
            continue
        neighbor = next(iter(g.neighbors(node)))
        idx = ext_counts.get(neighbor, 0)
        ext_counts[neighbor] = idx + 1
        base = np.array(pos[neighbor], dtype=float)
        direction = base - centroid
        norm = np.linalg.norm(direction)
        if norm < 1e-6:
            direction = np.array([1.0, 0.0])
            norm = 1.0
        direction = direction / norm
        normal = np.array([-direction[1], direction[0]])
        spread = (-0.18 + 0.36 * idx)
        pos[node] = base + 0.95 * direction + spread * normal

    return pos


def draw_panel(ax, cls):
    entry = cls["representative_entry"]
    g = build_skeleton(entry)
    pos = layout_positions(g)

    ax.set_xlim(-2.35, 2.95)
    ax.set_ylim(-2.1, 2.1)
    ax.set_aspect("equal")
    ax.axis("off")

    title = (
        f"F{cls['field_topology_id']:03d} / B{cls['bare_topology_id']:03d}\n"
        f"$S={cls['symmetry_factor']}$, raw={cls['raw_wick_multiplicity']}"
    )
    ax.text(0.0, 1.92, title, ha="center", va="top", fontsize=13)

    grouped = defaultdict(list)
    for u, v, k, data in g.edges(keys=True, data=True):
        if data["role"] != "internal":
            continue
        key = tuple(sorted((u, v)))
        grouped[key].append((u, v, k, data))

    for key, edges in grouped.items():
        offsets = edge_offsets(len(edges))
        for offset, (u, v, _k, data) in zip(offsets, edges):
            p0 = pos[u]
            p1 = pos[v]
            if data["kind"] == "A":
                draw_wavy_curve(ax, p0, p1, rad=offset)
            elif data["kind"] == "fermion":
                draw_plain_curve(ax, p0, p1, rad=offset)
                tail, head = data["arrow"]
                if (tail, head) != (u, v):
                    draw_arrow_on_curve(ax, p1, p0, rad=-offset)
                else:
                    draw_arrow_on_curve(ax, p0, p1, rad=offset)
            elif data["kind"] == "ghost":
                draw_plain_curve(ax, p0, p1, rad=offset, ls=(0, (4.0, 3.0)))
                tail, head = data["arrow"]
                if (tail, head) != (u, v):
                    draw_arrow_on_curve(ax, p1, p0, rad=-offset, scale=11)
                else:
                    draw_arrow_on_curve(ax, p0, p1, rad=offset, scale=11)

    for u, v, _k, data in g.edges(keys=True, data=True):
        if data["role"] != "external":
            continue
        p0 = pos[u]
        p1 = pos[v]
        field = g.nodes[v]["field"] if g.nodes[v]["kind"] == "external" else g.nodes[u]["field"]
        if field == "A":
            draw_wavy_curve(ax, p0, p1, rad=0.0, waves=4.5, amplitude=0.03)
        elif field in {"lbar", "lam"}:
            draw_plain_curve(ax, p0, p1, rad=0.0)
            if data["arrow"] is not None:
                draw_arrow_on_curve(ax, p0, p1, rad=0.0, scale=11)
        elif field in {"c", "cbar"}:
            draw_plain_curve(ax, p0, p1, rad=0.0, ls=(0, (4.0, 3.0)))
            if data["arrow"] is not None:
                draw_arrow_on_curve(ax, p0, p1, rad=0.0, scale=10)
        label = external_label(field)
        ax.text(
            p1[0] + 0.06 * np.sign(p1[0] - p0[0]),
            p1[1] + 0.05 * np.sign(p1[1] - p0[1] + 1e-9),
            label,
            fontsize=13,
            ha="left" if p1[0] >= p0[0] else "right",
            va="center",
            bbox={"boxstyle": "round,pad=0.12", "fc": "white", "ec": "none", "alpha": 0.94},
            zorder=6,
        )

    for node, data in g.nodes(data=True):
        x, y = pos[node]
        if data["kind"] == "operator":
            ax.add_patch(Rectangle((x - 0.16, y - 0.14), 0.32, 0.28, facecolor="white", edgecolor="black", lw=1.7, zorder=5))
            ax.text(x, y, "O", ha="center", va="center", fontsize=15, zorder=6)
        elif data["kind"] == "vertex":
            ax.add_patch(Circle((x, y), 0.05, facecolor="black", edgecolor="black", zorder=5))

    multiset_label = ", ".join(f"{k.replace('V_', '')} x {v}" for k, v in entry["action_vertices"].items())
    ax.text(0.0, -1.96, multiset_label, ha="center", va="bottom", fontsize=11)


def main():
    payload = json.loads(COARSE_JSON.read_text())
    selected = payload["selected_gallery_classes"]
    OUT.parent.mkdir(parents=True, exist_ok=True)

    fig, axes = plt.subplots(2, 5, figsize=(21, 9))
    fig.subplots_adjust(left=0.02, right=0.98, top=0.97, bottom=0.04, wspace=0.12, hspace=0.18)

    for ax, cls in zip(axes.flat, selected):
        draw_panel(ax, cls)

    for ax in axes.flat[len(selected):]:
        ax.axis("off")

    fig.savefig(OUT, dpi=260, bbox_inches="tight")
    fig.savefig(OUT_PDF, bbox_inches="tight")
    print(OUT)
    print(OUT_PDF)


if __name__ == "__main__":
    main()
