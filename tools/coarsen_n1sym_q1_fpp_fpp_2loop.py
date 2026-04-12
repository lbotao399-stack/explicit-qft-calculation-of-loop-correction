from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
import json
from pathlib import Path

import networkx as nx
from networkx.algorithms.graph_hashing import weisfeiler_lehman_graph_hash


ROOT = Path(__file__).resolve().parents[1]
FINE_JSON = ROOT / "assets" / "step4" / "n1_sym_euclidean" / "q1_fpp_fpp_2loop_topologies.json"
OUT_JSON = ROOT / "assets" / "step4" / "n1_sym_euclidean" / "q1_fpp_fpp_2loop_coarse_classes.json"
OUT_MD = ROOT / "assets" / "step4" / "n1_sym_euclidean" / "q1_fpp_fpp_2loop_coarse_summary.md"


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


def fine_graph(entry):
    g = nx.Graph()
    g.add_node("core::O", label="core_ins")
    action_vertex_types = {}

    for contraction in entry["representative_internal_contractions"]:
        for endpoint in (contraction["from"], contraction["to"]):
            vertex_id, _ = parse_endpoint(endpoint)
            if vertex_id == "O":
                continue
            action_vertex_types[vertex_id] = vertex_id.split("#", 1)[0]

    for ext in entry["representative_external_ports"]:
        vertex_id, _ = parse_endpoint(ext["port"])
        if vertex_id == "O":
            continue
        action_vertex_types[vertex_id] = vertex_id.split("#", 1)[0]

    for vertex_id, vertex_type in sorted(action_vertex_types.items()):
        g.add_node(f"core::{vertex_id}", label=f"core_act:{vertex_type}")

    port_nodes = {}

    def ensure_port_node(vertex_id: str, port_name: str):
        key = (vertex_id, port_name)
        if key in port_nodes:
            return port_nodes[key]
        node_id = f"port::{vertex_id}:{port_name}"
        node_label = f"port:{field_from_endpoint(vertex_id, port_name)}"
        core_id = "core::O" if vertex_id == "O" else f"core::{vertex_id}"
        g.add_node(node_id, label=node_label)
        g.add_edge(core_id, node_id, label="inc")
        port_nodes[key] = node_id
        return node_id

    for contraction in entry["representative_internal_contractions"]:
        v1, p1 = parse_endpoint(contraction["from"])
        v2, p2 = parse_endpoint(contraction["to"])
        n1 = ensure_port_node(v1, p1)
        n2 = ensure_port_node(v2, p2)
        g.add_edge(n1, n2, label=f"prop:{contraction['kind']}")

    for ext in entry["representative_external_ports"]:
        v, p = parse_endpoint(ext["port"])
        n = ensure_port_node(v, p)
        ext_id = f"ext::{ext['port']}::{ext['field']}"
        g.add_node(ext_id, label=f"ext:{ext['field']}")
        g.add_edge(n, ext_id, label="ext")

    return g


def bare_graph(entry):
    g = nx.Graph()
    g.add_node("core::O", label="core_ins")
    action_vertices = set()

    for contraction in entry["representative_internal_contractions"]:
        for endpoint in (contraction["from"], contraction["to"]):
            vertex_id, _ = parse_endpoint(endpoint)
            if vertex_id != "O":
                action_vertices.add(vertex_id)

    for ext in entry["representative_external_ports"]:
        vertex_id, _ = parse_endpoint(ext["port"])
        if vertex_id != "O":
            action_vertices.add(vertex_id)

    for vertex_id in sorted(action_vertices):
        g.add_node(f"core::{vertex_id}", label="core_act")

    port_nodes = {}

    def ensure_port_node(vertex_id: str, port_name: str):
        key = (vertex_id, port_name)
        if key in port_nodes:
            return port_nodes[key]
        node_id = f"port::{vertex_id}:{port_name}"
        core_id = "core::O" if vertex_id == "O" else f"core::{vertex_id}"
        g.add_node(node_id, label="port")
        g.add_edge(core_id, node_id, label="inc")
        port_nodes[key] = node_id
        return node_id

    for contraction in entry["representative_internal_contractions"]:
        v1, p1 = parse_endpoint(contraction["from"])
        v2, p2 = parse_endpoint(contraction["to"])
        n1 = ensure_port_node(v1, p1)
        n2 = ensure_port_node(v2, p2)
        g.add_edge(n1, n2, label="prop")

    for ext in entry["representative_external_ports"]:
        v, p = parse_endpoint(ext["port"])
        n = ensure_port_node(v, p)
        ext_id = f"ext::{ext['port']}::{ext['field']}"
        g.add_node(ext_id, label="ext")
        g.add_edge(n, ext_id, label="ext")

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


def is_operator_connected(entry):
    g = nx.Graph()
    insertion_ports = set()
    action_vertices = set()

    for contraction in entry["representative_internal_contractions"]:
        for endpoint in (contraction["from"], contraction["to"]):
            vertex_id, port_name = parse_endpoint(endpoint)
            if vertex_id == "O":
                insertion_ports.add(f"port::{vertex_id}:{port_name}")
            else:
                action_vertices.add(vertex_id)

    for ext in entry["representative_external_ports"]:
        vertex_id, port_name = parse_endpoint(ext["port"])
        if vertex_id == "O":
            insertion_ports.add(f"port::{vertex_id}:{port_name}")
        else:
            action_vertices.add(vertex_id)

    for vertex_id in action_vertices:
        g.add_node(f"core::{vertex_id}")

    def ensure_port_node(vertex_id: str, port_name: str):
        node_id = f"port::{vertex_id}:{port_name}"
        g.add_node(node_id)
        if vertex_id != "O":
            g.add_edge(f"core::{vertex_id}", node_id)
        return node_id

    for contraction in entry["representative_internal_contractions"]:
        v1, p1 = parse_endpoint(contraction["from"])
        v2, p2 = parse_endpoint(contraction["to"])
        n1 = ensure_port_node(v1, p1)
        n2 = ensure_port_node(v2, p2)
        g.add_edge(n1, n2)

    for ext in entry["representative_external_ports"]:
        v, p = parse_endpoint(ext["port"])
        ensure_port_node(v, p)

    if not insertion_ports:
        return False

    touched_components = [component for component in nx.connected_components(g) if component & insertion_ports]
    return len(touched_components) == 1


def coarse_group(entries, graph_builder):
    grouped = defaultdict(list)
    for fine_id, entry in enumerate(entries, start=1):
        graph = graph_builder(entry)
        graph_hash = weisfeiler_lehman_graph_hash(graph, node_attr="label", edge_attr="label")
        bucket = grouped[graph_hash]
        for item in bucket:
            if nx.is_isomorphic(graph, item["graph"], node_match=node_match, edge_match=edge_match):
                item["fine_class_ids"].append(fine_id)
                item["fine_class_count"] += 1
                item["raw_wick_multiplicity"] += entry["wick_multiplicity"]
                break
        else:
            bucket.append(
                {
                    "graph": graph,
                    "representative_fine_class_id": fine_id,
                    "representative_entry": entry,
                    "fine_class_ids": [fine_id],
                    "fine_class_count": 1,
                    "raw_wick_multiplicity": entry["wick_multiplicity"],
                }
            )
    return [item for bucket in grouped.values() for item in bucket]


def main():
    fine_payload = json.loads(FINE_JSON.read_text())
    fine_entries = [entry for entry in fine_payload["classes"] if is_operator_connected(entry)]

    field_classes = coarse_group(fine_entries, fine_graph)
    bare_classes = coarse_group(fine_entries, bare_graph)

    bare_lookup = {}
    for idx, item in enumerate(bare_classes, start=1):
        for fine_id in item["fine_class_ids"]:
            bare_lookup[fine_id] = idx

    field_classes.sort(
        key=lambda item: (
            -item["raw_wick_multiplicity"],
            -item["fine_class_count"],
            item["representative_fine_class_id"],
        )
    )
    bare_classes.sort(
        key=lambda item: (
            -item["raw_wick_multiplicity"],
            -item["fine_class_count"],
            item["representative_fine_class_id"],
        )
    )

    selected = []
    used_action_multisets = set()
    used_bare = set()
    for item in field_classes:
        bare_id = bare_lookup[item["representative_fine_class_id"]]
        action_key = tuple(sorted(item["representative_entry"]["action_vertices"].items()))
        if action_key in used_action_multisets:
            continue
        used_action_multisets.add(action_key)
        used_bare.add(bare_id)
        selected.append(item)
        if len(selected) == 10:
            break

    if len(selected) < 10:
        for item in field_classes:
            bare_id = bare_lookup[item["representative_fine_class_id"]]
            if bare_id in used_bare:
                continue
            used_bare.add(bare_id)
            selected.append(item)
            if len(selected) == 10:
                break

    field_payload = []
    for idx, item in enumerate(field_classes, start=1):
        aut = automorphism_order(item["graph"])
        field_payload.append(
            {
                "field_topology_id": idx,
                "bare_topology_id": bare_lookup[item["representative_fine_class_id"]],
                "representative_fine_class_id": item["representative_fine_class_id"],
                "fine_class_ids": item["fine_class_ids"],
                "fine_class_count": item["fine_class_count"],
                "raw_wick_multiplicity": item["raw_wick_multiplicity"],
                "automorphism_order": aut,
                "symmetry_factor": symmetry_factor_string(aut),
                "representative_entry": item["representative_entry"],
            }
        )

    bare_payload = []
    for idx, item in enumerate(bare_classes, start=1):
        aut = automorphism_order(item["graph"])
        bare_payload.append(
            {
                "bare_topology_id": idx,
                "representative_fine_class_id": item["representative_fine_class_id"],
                "fine_class_ids": item["fine_class_ids"],
                "fine_class_count": item["fine_class_count"],
                "raw_wick_multiplicity": item["raw_wick_multiplicity"],
                "automorphism_order": aut,
                "symmetry_factor": symmetry_factor_string(aut),
            }
        )

    payload_by_rep = {
        item["representative_fine_class_id"]: item
        for item in field_payload
    }
    selected_payload = [
        payload_by_rep[item["representative_fine_class_id"]]
        for item in selected
    ]

    payload = {
        "source_raw_wick_contractions": fine_payload["source_raw_graph_count"],
        "fine_topology_classes": fine_payload["topology_class_count"],
        "operator_connected_fine_classes": len(fine_entries),
        "operator_connected_raw_wick_contractions": sum(entry["wick_multiplicity"] for entry in fine_entries),
        "field_labeled_topology_classes": len(field_payload),
        "bare_skeleton_classes": len(bare_payload),
        "assumptions": {
            "operator_connected_criterion": [
                "remove the artificial O-core incidence edges",
                "keep action-vertex incidence edges",
                "all insertion ports must lie in a single connected component",
            ],
            "field_labeled_topology": [
                "forgets insertion term",
                "forgets insertion port labels",
                "forgets labels of identical action-vertex copies",
                "preserves propagator species",
                "preserves external field species",
            ],
            "bare_skeleton_topology": [
                "forgets action-vertex types",
                "forgets propagator species",
                "forgets external field species",
                "keeps only graph skeleton and operator node",
            ],
            "graph_symmetry_factor_convention": "1/|Aut(topology graph)|",
        },
        "field_labeled_classes": field_payload,
        "bare_skeletons": bare_payload,
        "selected_gallery_classes": selected_payload,
    }

    lines = []
    lines.append("# N=1 SYM Q_1(f_{++}f_{++}) 2-loop coarse topology summary")
    lines.append("")
    lines.append(f"- source raw Wick contractions: `{fine_payload['source_raw_graph_count']}`")
    lines.append(f"- fine classes used as input: `{fine_payload['topology_class_count']}`")
    lines.append(f"- operator-connected fine classes: `{len(fine_entries)}`")
    lines.append(f"- operator-connected raw Wick contractions: `{sum(entry['wick_multiplicity'] for entry in fine_entries)}`")
    lines.append(f"- field-labeled topological classes: `{len(field_payload)}`")
    lines.append(f"- bare skeleton classes: `{len(bare_payload)}`")
    lines.append("")
    lines.append("## Selected gallery classes")
    lines.append("")
    for item in selected_payload:
        entry = item["representative_entry"]
        lines.append(
            f"- `F{item['field_topology_id']:03d}` / `B{item['bare_topology_id']:03d}` "
            f"`S={item['symmetry_factor']}` `raw={item['raw_wick_multiplicity']}` "
            f"`fine={item['fine_class_count']}` `{entry['action_vertices']}`"
        )

    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False))
    OUT_MD.write_text("\n".join(lines))

    print(f"operator_connected_fine_classes={len(fine_entries)}")
    print(f"field_labeled_topology_classes={len(field_payload)}")
    print(f"bare_skeleton_classes={len(bare_payload)}")
    print(OUT_JSON)
    print(OUT_MD)


if __name__ == "__main__":
    main()
