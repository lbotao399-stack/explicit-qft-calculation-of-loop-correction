from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle
import numpy as np

import feynarts_style_n1sym_generator as gen


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets" / "step4" / "n1_sym_euclidean"


plt.rcParams.update(
    {
        "font.family": "STIXGeneral",
        "mathtext.fontset": "stix",
        "figure.facecolor": "white",
        "axes.facecolor": "white",
    }
)


def vec(xy):
    return np.asarray(xy, dtype=float)


def cubic_points(p0, c0, c1, p1, n=260):
    p0 = vec(p0)
    c0 = vec(c0)
    c1 = vec(c1)
    p1 = vec(p1)
    t = np.linspace(0.0, 1.0, n)
    s = 1.0 - t
    pts = (
        (s**3)[:, None] * p0
        + (3.0 * s**2 * t)[:, None] * c0
        + (3.0 * s * t**2)[:, None] * c1
        + (t**3)[:, None] * p1
    )
    return t, pts


def cubic_tangents(p0, c0, c1, p1, n=260):
    p0 = vec(p0)
    c0 = vec(c0)
    c1 = vec(c1)
    p1 = vec(p1)
    t = np.linspace(0.0, 1.0, n)
    s = 1.0 - t
    tan = (
        (3.0 * s**2)[:, None] * (c0 - p0)
        + (6.0 * s * t)[:, None] * (c1 - c0)
        + (3.0 * t**2)[:, None] * (p1 - c1)
    )
    return t, tan


def unit_normals(tangent):
    length = np.linalg.norm(tangent, axis=1, keepdims=True)
    length[length == 0.0] = 1.0
    tangent = tangent / length
    return np.stack([-tangent[:, 1], tangent[:, 0]], axis=1)


def draw_plain_curve(ax, p0, c0, c1, p1, lw=1.7):
    _, pts = cubic_points(p0, c0, c1, p1)
    ax.plot(pts[:, 0], pts[:, 1], color="black", lw=lw, solid_capstyle="round", zorder=2)
    return pts


def draw_fermion_curve(ax, p0, c0, c1, p1, direction="forward", lw=1.7):
    pts = draw_plain_curve(ax, p0, c0, c1, p1, lw=lw)
    n = len(pts)
    i0 = int(0.53 * (n - 1))
    i1 = int(0.67 * (n - 1))
    start = pts[i0]
    end = pts[i1]
    if direction != "forward":
        start, end = end, start
    arrow = FancyArrowPatch(
        tuple(start),
        tuple(end),
        arrowstyle="-|>",
        mutation_scale=10.5,
        linewidth=1.0,
        color="black",
        shrinkA=0,
        shrinkB=0,
        zorder=4,
    )
    ax.add_patch(arrow)
    return pts


def draw_gauge_curve(ax, p0, c0, c1, p1, lw=1.45, amplitude=0.040, waves=7.0):
    t, pts = cubic_points(p0, c0, c1, p1, n=420)
    _, tan = cubic_tangents(p0, c0, c1, p1, n=420)
    normals = unit_normals(tan)
    envelope = np.sin(np.pi * t) ** 0.85
    phase = amplitude * envelope * np.sin(2.0 * np.pi * waves * t)
    curve = pts + normals * phase[:, None]
    ax.plot(curve[:, 0], curve[:, 1], color="black", lw=lw, solid_capstyle="round", zorder=2)
    return pts


def point_and_normal(points, frac):
    frac = min(max(frac, 0.0), 1.0)
    idx = int(frac * (len(points) - 1))
    idx_prev = max(idx - 1, 0)
    idx_next = min(idx + 1, len(points) - 1)
    tangent = points[idx_next] - points[idx_prev]
    norm = np.linalg.norm(tangent)
    if norm == 0.0:
        tangent = np.asarray([1.0, 0.0])
        norm = 1.0
    tangent = tangent / norm
    normal = np.asarray([-tangent[1], tangent[0]])
    return points[idx], normal


def curve_label(ax, points, frac, text, normal_offset=0.12, tangential_offset=0.0, size=9.2, boxed=True):
    pos, normal = point_and_normal(points, frac)
    tangent = np.asarray([normal[1], -normal[0]])
    xy = pos + normal_offset * normal + tangential_offset * tangent
    bbox = {"boxstyle": "round,pad=0.08", "fc": "white", "ec": "none", "alpha": 0.96} if boxed else None
    ax.text(xy[0], xy[1], rf"${text}$", ha="center", va="center", fontsize=size, bbox=bbox, zorder=7)


def endpoint_label(ax, xy, text, size=10.8):
    ax.text(xy[0], xy[1], rf"${text}$", ha="center", va="center", fontsize=size, zorder=7)


def operator_box(ax, center, w=0.28, h=0.22):
    x, y = center
    ax.add_patch(Rectangle((x - w / 2, y - h / 2), w, h, facecolor="white", edgecolor="black", lw=1.2, zorder=5))
    ax.text(x, y, "QO", ha="center", va="center", fontsize=11.0, zorder=6)
    return {
        "top": np.asarray([x + w / 2, y + h * 0.25]),
        "bottom": np.asarray([x + w / 2, y - h * 0.25]),
    }


def node(ax, center, r=0.040):
    ax.add_patch(Circle(center, r, facecolor="black", edgecolor="black", zorder=5))


def setup_panel(ax, top_id, orient):
    ax.set_xlim(-2.95, 2.85)
    ax.set_ylim(-1.55, 1.32)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.text(-2.82, 1.17, orient, ha="left", va="center", fontsize=10.6)
    ax.text(0.02, 1.17, top_id, ha="center", va="center", fontsize=13.0)


def slot_labels(template: gen.TypedVertexTemplate):
    by_field = {}
    for slot in template.slots:
        by_field.setdefault(slot.field, slot.display_tex or slot.field)
    return by_field


def draw_triangle_panel(ax, template: gen.TypedVertexTemplate, top_id: str, orient: str):
    setup_panel(ax, top_id, orient)
    labels = slot_labels(template)

    op = operator_box(ax, (-2.28, -0.78))
    v_g = np.asarray([-0.18, -0.15])
    v_f = np.asarray([0.98, 0.23])
    ext_a = np.asarray([2.20, 0.92])
    ext_l = np.asarray([2.22, -0.04])

    p_op_a = draw_gauge_curve(ax, op["bottom"], (-1.60, -1.02), (-0.78, -0.43), v_g, amplitude=0.036, waves=5.9)
    p_op_l = draw_fermion_curve(ax, op["top"], (-1.55, -0.08), (0.08, 0.16), v_f, direction="forward")
    p_mid_a = draw_gauge_curve(ax, v_g, (0.12, 0.24), (0.56, 0.40), v_f, amplitude=0.032, waves=4.9)
    p_ext_a = draw_gauge_curve(ax, v_g, (0.52, 0.12), (1.42, 0.64), ext_a, amplitude=0.028, waves=4.1)
    p_ext_l = draw_fermion_curve(ax, v_f, (1.35, 0.18), (1.82, 0.01), ext_l, direction="forward")

    node(ax, v_g)
    node(ax, v_f)

    curve_label(ax, p_op_l, 0.34, labels["lbar"], normal_offset=0.18, size=8.0)
    curve_label(ax, p_op_a, 0.40, labels["A"], normal_offset=-0.13, size=8.1)
    curve_label(ax, p_op_l, 0.63, r"\lambda", normal_offset=0.12, size=9.2)
    curve_label(ax, p_mid_a, 0.50, r"A(q)", normal_offset=0.16, size=9.2)
    endpoint_label(ax, ext_a + np.asarray([0.03, 0.04]), r"A")
    endpoint_label(ax, ext_l + np.asarray([0.03, -0.04]), r"\widetilde\lambda")


def draw_chain_same_panel(ax, template: gen.TypedVertexTemplate, top_id: str, orient: str):
    setup_panel(ax, top_id, orient)
    labels = slot_labels(template)

    op = operator_box(ax, (-2.28, -0.78))
    v1 = np.asarray([-0.36, -0.03])
    v2 = np.asarray([1.10, 0.18])
    ext_a = np.asarray([2.22, 0.90])
    ext_l = np.asarray([2.24, -0.02])

    p_op_a = draw_gauge_curve(ax, op["bottom"], (-1.62, -1.00), (-0.82, -0.36), v1, amplitude=0.036, waves=5.8)
    p_op_l = draw_fermion_curve(ax, op["top"], (-1.50, -0.16), (-0.86, 0.07), v1, direction="forward")
    p_mid_l = draw_fermion_curve(ax, v1, (0.08, -0.01), (0.62, 0.12), v2, direction="forward")
    p_ext_a = draw_gauge_curve(ax, v2, (1.44, 0.34), (1.88, 0.70), ext_a, amplitude=0.027, waves=4.0)
    p_ext_l = draw_fermion_curve(ax, v2, (1.44, 0.12), (1.86, 0.02), ext_l, direction="forward")

    node(ax, v1)
    node(ax, v2)

    curve_label(ax, p_op_l, 0.33, labels["lbar"], normal_offset=0.17, size=8.0)
    curve_label(ax, p_op_a, 0.40, labels["A"], normal_offset=-0.13, size=8.1)
    curve_label(ax, p_mid_l, 0.54, r"\lambda", normal_offset=0.12, size=9.2)
    endpoint_label(ax, ext_a + np.asarray([0.03, 0.03]), r"A")
    endpoint_label(ax, ext_l + np.asarray([0.04, -0.04]), r"\widetilde\lambda")


def draw_chain_split_panel(ax, template: gen.TypedVertexTemplate, top_id: str, orient: str):
    setup_panel(ax, top_id, orient)
    labels = slot_labels(template)

    op = operator_box(ax, (-2.28, -0.78))
    v1 = np.asarray([-0.30, 0.18])
    v2 = np.asarray([1.08, -0.06])
    ext_a = np.asarray([0.55, 1.00])
    ext_l = np.asarray([2.24, -0.04])

    p_op_l = draw_fermion_curve(ax, op["top"], (-1.48, -0.08), (-0.78, 0.28), v1, direction="forward")
    p_op_a = draw_gauge_curve(ax, op["bottom"], (-1.52, -1.06), (0.02, -0.78), v2, amplitude=0.034, waves=6.2)
    p_mid_l = draw_fermion_curve(ax, v1, (0.20, 0.14), (0.66, -0.01), v2, direction="forward")
    p_ext_a = draw_gauge_curve(ax, v1, (-0.02, 0.48), (0.20, 0.84), ext_a, amplitude=0.025, waves=3.5)
    p_ext_l = draw_fermion_curve(ax, v2, (1.44, -0.02), (1.88, -0.02), ext_l, direction="forward")

    node(ax, v1)
    node(ax, v2)

    curve_label(ax, p_op_l, 0.35, labels["lbar"], normal_offset=0.17, size=8.0)
    curve_label(ax, p_op_a, 0.40, labels["A"], normal_offset=-0.13, size=8.1)
    curve_label(ax, p_mid_l, 0.52, r"\lambda", normal_offset=0.12, size=9.2)
    endpoint_label(ax, ext_a + np.asarray([0.03, 0.04]), r"A")
    endpoint_label(ax, ext_l + np.asarray([0.04, -0.04]), r"\widetilde\lambda")


def render_demo(demo: str):
    if demo == "q1_fpp_fpp":
        left_template = gen.O12_DLB_A
        right_template = gen.O21_A_DLB
        stem = "feynarts_style_n1sym_q1_fpp_fpp_g2"
    elif demo == "q1_fpp_expw_fpp":
        left_template = gen.O12_DLB_AEXPW
        right_template = gen.O21_A_DLB_EXPW
        stem = "feynarts_style_n1sym_q1_fpp_expw_fpp_g2"
    else:
        raise ValueError(demo)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_png = OUT_DIR / f"{stem}.png"
    out_pdf = OUT_DIR / f"{stem}.pdf"

    fig, axes = plt.subplots(3, 2, figsize=(13.6, 10.8))
    fig.subplots_adjust(left=0.03, right=0.99, top=0.985, bottom=0.03, hspace=0.16, wspace=0.08)

    draw_triangle_panel(axes[0, 0], left_template, "T001", "12")
    draw_triangle_panel(axes[0, 1], right_template, "T004", "21")
    draw_chain_same_panel(axes[1, 0], left_template, "T002", "12")
    draw_chain_same_panel(axes[1, 1], right_template, "T005", "21")
    draw_chain_split_panel(axes[2, 0], left_template, "T003", "12")
    draw_chain_split_panel(axes[2, 1], right_template, "T006", "21")

    fig.savefig(out_png, dpi=260, bbox_inches="tight")
    fig.savefig(out_pdf, bbox_inches="tight")
    print(out_png)
    print(out_pdf)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", choices=("q1_fpp_fpp", "q1_fpp_expw_fpp"), default="q1_fpp_expw_fpp")
    args = parser.parse_args()
    render_demo(args.demo)


if __name__ == "__main__":
    main()
