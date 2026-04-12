from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
import json
from pathlib import Path

import networkx as nx
from networkx.algorithms.graph_hashing import weisfeiler_lehman_graph_hash


ROOT = Path(__file__).resolve().parents[1]
RAW_JSON = ROOT / "assets" / "step4" / "n1_sym_euclidean" / "q1_fpp_fpp_2loop_graphs.json"
OUT_JSON = ROOT / "assets" / "step4" / "n1_sym_euclidean" / "q1_fpp_fpp_2loop_topologies.json"
OUT_MD = ROOT / "assets" / "step4" / "n1_sym_euclidean" / "q1_fpp_fpp_2loop_topologies.md"
OUT_SUMMARY_MD = ROOT / "assets" / "step4" / "n1_sym_euclidean" / "q1_fpp_fpp_2loop_topologies_summary.md"


def parse_endpoint(text: str):
    vertex_id, port_name = text.split(":", 1)
    return vertex_id, port_name


def action_port_label(vertex_type: str, port_name: str):
    if vertex_type in {"V_AAA", "V_AAAA"}:
        return "A"
    if vertex_type == "V_A_lambda_lambdabar":
        if port_name == "A":
            return "A"
        if port_name == "lambda":
            return "lam"
        if port_name == "lambdabar":
            return "lbar"
    if vertex_type == "V_cbar_A_c":
        if port_name == "A":
            return "A"
        if port_name == "c":
            return "c"
        if port_name == "cbar":
            return "cbar"
    raise ValueError(f"unknown action port: {vertex_type}:{port_name}")


def build_topology_graph(entry):
    g = nx.Graph()

    insertion_term = entry["insertion_term"]
    g.add_node("core::O", label=f"core_ins:{insertion_term}")

    action_vertex_types = {}
    for contraction in entry["internal_contractions"]:
        for endpoint in (contraction["from"], contraction["to"]):
            vertex_id, _port_name = parse_endpoint(endpoint)
            if vertex_id == "O":
                continue
            vertex_type = vertex_id.split("#", 1)[0]
            action_vertex_types[vertex_id] = vertex_type
    for ext in entry["external_ports"]:
        vertex_id, _port_name = parse_endpoint(ext["port"])
        if vertex_id == "O":
            continue
        vertex_type = vertex_id.split("#", 1)[0]
        action_vertex_types[vertex_id] = vertex_type

    for vertex_id, vertex_type in sorted(action_vertex_types.items()):
        g.add_node(f"core::{vertex_id}", label=f"core_act:{vertex_type}")

    port_nodes = {}

    def ensure_port_node(vertex_id: str, port_name: str):
        key = (vertex_id, port_name)
        if key in port_nodes:
            return port_nodes[key]
        node_id = f"port::{vertex_id}:{port_name}"
        if vertex_id == "O":
            node_label = f"port_ins:{port_name}"
            core_id = "core::O"
        else:
            vertex_type = action_vertex_types[vertex_id]
            node_label = f"port_act:{action_port_label(vertex_type, port_name)}"
            core_id = f"core::{vertex_id}"
        g.add_node(node_id, label=node_label)
        g.add_edge(core_id, node_id, label="inc")
        port_nodes[key] = node_id
        return node_id

    for contraction in entry["internal_contractions"]:
        v1, p1 = parse_endpoint(contraction["from"])
        v2, p2 = parse_endpoint(contraction["to"])
        n1 = ensure_port_node(v1, p1)
        n2 = ensure_port_node(v2, p2)
        g.add_edge(n1, n2, label=f"prop:{contraction['kind']}")

    for ext in entry["external_ports"]:
        v, p = parse_endpoint(ext["port"])
        n = ensure_port_node(v, p)
        ext_node = f"ext::{v}:{p}"
        g.add_node(ext_node, label=f"ext:{ext['field']}")
        g.add_edge(n, ext_node, label="ext")

    return g


def node_match(a, b):
    return a["label"] == b["label"]


def edge_match(a, b):
    return a["label"] == b["label"]


def automorphism_order(graph: nx.Graph):
    matcher = nx.isomorphism.GraphMatcher(graph, graph, node_match=node_match, edge_match=edge_match)
    return sum(1 for _ in matcher.isomorphisms_iter())


def symmetry_factor_string(order: int):
    frac = Fraction(1, order)
    if frac.denominator == 1:
        return str(frac.numerator)
    return f"{frac.numerator}/{frac.denominator}"


def representative_markdown(class_id, item):
    lines = []
    lines.append(f"### T{class_id:03d}")
    lines.append("")
    lines.append(f"- insertion term: `{item['insertion_term']}`")
    action_string = ", ".join(f"`{k}` x {v}" for k, v in item["action_vertices"].items()) or "`none`"
    lines.append(f"- action vertices: {action_string}")
    lines.append(f"- external fields: `{item['external_fields']}`")
    lines.append(f"- raw Wick contraction multiplicity: `{item['wick_multiplicity']}`")
    lines.append(f"- automorphism order: `{item['automorphism_order']}`")
    lines.append(f"- graph symmetry factor: `{item['symmetry_factor']}`")
    lines.append("- representative internal contractions:")
    for contraction in item["representative_internal_contractions"]:
        lines.append(f"  - `{contraction['from']}` --[{contraction['kind']}]-- `{contraction['to']}`")
    lines.append("- representative external ports:")
    for ext in item["representative_external_ports"]:
        lines.append(f"  - `{ext['port']}` : `{ext['field']}`")
    lines.append("")
    return lines


def main():
    with RAW_JSON.open() as f:
        raw = json.load(f)

    grouped = defaultdict(list)

    for entry in raw["graphs"]:
        action_key = tuple(sorted(entry["action_vertices"].items()))
        bucket_key = (entry["insertion_term"], action_key)
        topo_graph = build_topology_graph(entry)
        topo_hash = weisfeiler_lehman_graph_hash(topo_graph, node_attr="label", edge_attr="label")
        bucket = grouped[(bucket_key, topo_hash)]

        matched = False
        for item in bucket:
            if nx.is_isomorphic(topo_graph, item["graph"], node_match=node_match, edge_match=edge_match):
                item["wick_multiplicity"] += 1
                matched = True
                break

        if not matched:
            bucket.append(
                {
                    "graph": topo_graph,
                    "insertion_term": entry["insertion_term"],
                    "action_vertices": entry["action_vertices"],
                    "external_fields": entry["external_fields"],
                    "representative_internal_contractions": entry["internal_contractions"],
                    "representative_external_ports": entry["external_ports"],
                    "wick_multiplicity": 1,
                }
            )

    classes = []
    for bucket in grouped.values():
        for item in bucket:
            aut = automorphism_order(item["graph"])
            classes.append(
                {
                    "insertion_term": item["insertion_term"],
                    "action_vertices": item["action_vertices"],
                    "external_fields": item["external_fields"],
                    "wick_multiplicity": item["wick_multiplicity"],
                    "automorphism_order": aut,
                    "symmetry_factor": symmetry_factor_string(aut),
                    "representative_internal_contractions": item["representative_internal_contractions"],
                    "representative_external_ports": item["representative_external_ports"],
                }
            )

    classes.sort(
        key=lambda item: (
            item["insertion_term"],
            json.dumps(item["action_vertices"], sort_keys=True),
            item["wick_multiplicity"],
            json.dumps(item["representative_internal_contractions"]),
        )
    )

    summary_by_insertion = defaultdict(int)
    for item in classes:
        summary_by_insertion[item["insertion_term"]] += 1

    payload = {
        "source_raw_graph_count": raw["graph_count"],
        "topology_class_count": len(classes),
        "assumptions": {
            "topology_preserves": [
                "insertion term",
                "action vertex type multiset",
                "insertion port labels",
                "propagator species",
                "external field species",
            ],
            "topology_forgets": [
                "labels of identical action-vertex copies",
                "labels of identical A-legs inside AAA / AAAA vertices",
            ],
            "graph_symmetry_factor_convention": "1/|Aut(topology graph)|",
        },
        "classes": classes,
    }

    lines = []
    lines.append("# N=1 SYM Q_1(f_{++}f_{++}) 2-loop topological classes")
    lines.append("")
    lines.append(f"- source raw Wick contractions: `{raw['graph_count']}`")
    lines.append(f"- topological classes: `{len(classes)}`")
    lines.append("")
    lines.append("## By insertion term")
    lines.append("")
    for key, value in sorted(summary_by_insertion.items()):
        lines.append(f"- `{key}`: `{value}`")
    lines.append("")
    lines.append("## Classes")
    lines.append("")
    for idx, item in enumerate(classes, start=1):
        lines.extend(representative_markdown(idx, item))

    summary_lines = []
    summary_lines.append("# N=1 SYM Q_1(f_{++}f_{++}) 2-loop topological summary")
    summary_lines.append("")
    summary_lines.append(f"- source raw Wick contractions: `{raw['graph_count']}`")
    summary_lines.append(f"- topological classes: `{len(classes)}`")
    summary_lines.append("")
    summary_lines.append("## By insertion term")
    summary_lines.append("")
    for key, value in sorted(summary_by_insertion.items()):
        summary_lines.append(f"- `{key}`: `{value}`")
    summary_lines.append("")
    summary_lines.append("## First classes")
    summary_lines.append("")
    for idx, item in enumerate(classes[:20], start=1):
        summary_lines.append(
            f"- `T{idx:03d}` `{item['insertion_term']}` {item['action_vertices']} "
            f"`mult={item['wick_multiplicity']}` `|Aut|={item['automorphism_order']}` "
            f"`S={item['symmetry_factor']}`"
        )

    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False))
    OUT_MD.write_text("\n".join(lines))
    OUT_SUMMARY_MD.write_text("\n".join(summary_lines))

    print(f"source_raw_graph_count={raw['graph_count']}")
    print(f"topology_class_count={len(classes)}")
    print(OUT_JSON)
    print(OUT_MD)
    print(OUT_SUMMARY_MD)


if __name__ == "__main__":
    main()
