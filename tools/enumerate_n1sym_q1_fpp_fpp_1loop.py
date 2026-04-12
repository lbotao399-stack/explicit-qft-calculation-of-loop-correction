from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from itertools import count
import json
from pathlib import Path

import networkx as nx


ROOT = Path(__file__).resolve().parents[1]
OUT_JSON = ROOT / "assets" / "step4" / "n1_sym_euclidean" / "q1_fpp_fpp_1loop_graphs.json"
OUT_MD = ROOT / "assets" / "step4" / "n1_sym_euclidean" / "q1_fpp_fpp_1loop_graphs.md"
OUT_SUMMARY_JSON = ROOT / "assets" / "step4" / "n1_sym_euclidean" / "q1_fpp_fpp_1loop_summary.json"
OUT_SUMMARY_MD = ROOT / "assets" / "step4" / "n1_sym_euclidean" / "q1_fpp_fpp_1loop_summary.md"
ALLOW_SAME_VERTEX_CONTRACTIONS = False
TOTAL_G_POWERS = (2, 3, 4)


@dataclass(frozen=True)
class PortDef:
    name: str
    field: str
    canon_label: str
    slot_label: str | None = None


@dataclass(frozen=True)
class VertexTemplate:
    name: str
    category: str
    g_power: int
    ports: tuple[PortDef, ...]


@dataclass(frozen=True)
class PortInstance:
    id: str
    vertex_id: str
    vertex_name: str
    field: str
    canon_label: str
    port_name: str
    is_insertion: bool
    slot_label: str | None


ACTION_TEMPLATES = (
    VertexTemplate(
        name="V_A_lambda_lambdabar",
        category="action",
        g_power=1,
        ports=(
            PortDef("A", "A", "A"),
            PortDef("lambda", "lam", "lam"),
            PortDef("lambdabar", "lbar", "lbar"),
        ),
    ),
    VertexTemplate(
        name="V_AAA",
        category="action",
        g_power=1,
        ports=(
            PortDef("A1", "A", "A"),
            PortDef("A2", "A", "A"),
            PortDef("A3", "A", "A"),
        ),
    ),
    VertexTemplate(
        name="V_cbar_A_c",
        category="action",
        g_power=1,
        ports=(
            PortDef("cbar", "cbar", "cbar"),
            PortDef("A", "A", "A"),
            PortDef("c", "c", "c"),
        ),
    ),
    VertexTemplate(
        name="V_AAAA",
        category="action",
        g_power=2,
        ports=(
            PortDef("A1", "A", "A"),
            PortDef("A2", "A", "A"),
            PortDef("A3", "A", "A"),
            PortDef("A4", "A", "A"),
        ),
    ),
)


INSERTION_TEMPLATES = (
    VertexTemplate(
        name="O12_dlb_A",
        category="insertion",
        g_power=0,
        ports=(
            PortDef("Qf1_lambdabar", "lbar", "Qf1:lbar", "Qf1"),
            PortDef("f2_A", "A", "f2:A", "f2"),
        ),
    ),
    VertexTemplate(
        name="O21_A_dlb",
        category="insertion",
        g_power=0,
        ports=(
            PortDef("f1_A", "A", "f1:A", "f1"),
            PortDef("Qf2_lambdabar", "lbar", "Qf2:lbar", "Qf2"),
        ),
    ),
    VertexTemplate(
        name="O12_dlb_AA",
        category="insertion",
        g_power=1,
        ports=(
            PortDef("Qf1_lambdabar", "lbar", "Qf1:lbar", "Qf1"),
            PortDef("f2_A1", "A", "f2:A", "f2"),
            PortDef("f2_A2", "A", "f2:A", "f2"),
        ),
    ),
    VertexTemplate(
        name="O12_Aldb_A",
        category="insertion",
        g_power=1,
        ports=(
            PortDef("Qf1_A", "A", "Qf1:A", "Qf1"),
            PortDef("Qf1_lambdabar", "lbar", "Qf1:lbar", "Qf1"),
            PortDef("f2_A", "A", "f2:A", "f2"),
        ),
    ),
    VertexTemplate(
        name="O21_AA_dlb",
        category="insertion",
        g_power=1,
        ports=(
            PortDef("f1_A1", "A", "f1:A", "f1"),
            PortDef("f1_A2", "A", "f1:A", "f1"),
            PortDef("Qf2_lambdabar", "lbar", "Qf2:lbar", "Qf2"),
        ),
    ),
    VertexTemplate(
        name="O21_A_Aldb",
        category="insertion",
        g_power=1,
        ports=(
            PortDef("f1_A", "A", "f1:A", "f1"),
            PortDef("Qf2_A", "A", "Qf2:A", "Qf2"),
            PortDef("Qf2_lambdabar", "lbar", "Qf2:lbar", "Qf2"),
        ),
    ),
    VertexTemplate(
        name="O12_Aldb_AA",
        category="insertion",
        g_power=2,
        ports=(
            PortDef("Qf1_A", "A", "Qf1:A", "Qf1"),
            PortDef("Qf1_lambdabar", "lbar", "Qf1:lbar", "Qf1"),
            PortDef("f2_A1", "A", "f2:A", "f2"),
            PortDef("f2_A2", "A", "f2:A", "f2"),
        ),
    ),
    VertexTemplate(
        name="O21_AA_Aldb",
        category="insertion",
        g_power=2,
        ports=(
            PortDef("f1_A1", "A", "f1:A", "f1"),
            PortDef("f1_A2", "A", "f1:A", "f1"),
            PortDef("Qf2_A", "A", "Qf2:A", "Qf2"),
            PortDef("Qf2_lambdabar", "lbar", "Qf2:lbar", "Qf2"),
        ),
    ),
)


COMPATIBILITY = {
    ("A", "A"): "A",
    ("lam", "lbar"): "fermion",
    ("lbar", "lam"): "fermion",
    ("c", "cbar"): "ghost",
    ("cbar", "c"): "ghost",
}


def compatible(p1: PortInstance, p2: PortInstance) -> str | None:
    return COMPATIBILITY.get((p1.field, p2.field))


def can_complete(remaining: list[PortInstance], external_slots_left: int) -> bool:
    counts = Counter(port.field for port in remaining)
    for e_a in range(external_slots_left + 1):
        for e_lam in range(external_slots_left + 1):
            for e_lbar in range(external_slots_left + 1):
                for e_c in range(external_slots_left + 1):
                    for e_cbar in range(external_slots_left + 1):
                        if e_a + e_lam + e_lbar + e_c + e_cbar != external_slots_left:
                            continue
                        if (
                            e_a > counts["A"]
                            or e_lam > counts["lam"]
                            or e_lbar > counts["lbar"]
                            or e_c > counts["c"]
                            or e_cbar > counts["cbar"]
                        ):
                            continue
                        rem_a = counts["A"] - e_a
                        rem_lam = counts["lam"] - e_lam
                        rem_lbar = counts["lbar"] - e_lbar
                        rem_c = counts["c"] - e_c
                        rem_cbar = counts["cbar"] - e_cbar
                        if rem_a % 2 != 0:
                            continue
                        if rem_lam != rem_lbar:
                            continue
                        if rem_c != rem_cbar:
                            continue
                        return True
    return False


def generate_action_multisets(target_g_power: int, start: int = 0):
    if target_g_power == 0:
        yield []
        return
    for idx in range(start, len(ACTION_TEMPLATES)):
        template = ACTION_TEMPLATES[idx]
        if template.g_power > target_g_power:
            continue
        for rest in generate_action_multisets(target_g_power - template.g_power, idx):
            yield [template, *rest]


def instantiate_vertices(insertion: VertexTemplate, actions: list[VertexTemplate]):
    vertices = [("O", insertion)]
    local_counters = defaultdict(lambda: count(1))
    for template in actions:
        k = next(local_counters[template.name])
        vertices.append((f"{template.name}#{k}", template))
    return vertices


def instantiate_ports(vertices):
    ports: list[PortInstance] = []
    for vertex_id, template in vertices:
        for port in template.ports:
            ports.append(
                PortInstance(
                    id=f"{vertex_id}:{port.name}",
                    vertex_id=vertex_id,
                    vertex_name=template.name,
                    field=port.field,
                    canon_label=port.canon_label if template.category == "insertion" else port.field,
                    port_name=port.name,
                    is_insertion=template.category == "insertion",
                    slot_label=port.slot_label if template.category == "insertion" else None,
                )
            )
    return ports


def fully_connected_after_insertion_split(vertices, pairs, externals):
    g = nx.Graph()
    insertion_ports = set()

    for vertex_id, template in vertices:
        if template.category == "action":
            g.add_node(f"core::{vertex_id}")
        else:
            for port in template.ports:
                insertion_ports.add(f"port::{vertex_id}:{port.name}")

    def ensure_port_node(port: PortInstance):
        node_id = f"port::{port.id}"
        if node_id not in g:
            g.add_node(node_id)
            if not port.is_insertion:
                g.add_edge(f"core::{port.vertex_id}", node_id)
        return node_id

    for left, right, _kind in pairs:
        if not ALLOW_SAME_VERTEX_CONTRACTIONS and left.vertex_id == right.vertex_id:
            return False
        if left.vertex_id == "O" and right.vertex_id == "O":
            return False
        n_left = ensure_port_node(left)
        n_right = ensure_port_node(right)
        g.add_edge(n_left, n_right)

    for port in externals:
        ensure_port_node(port)

    if not insertion_ports:
        return False
    if not nx.is_connected(g):
        return False
    return all(port in g for port in insertion_ports)


def external_sector_ok(externals: list[PortInstance]) -> bool:
    counts = Counter(port.field for port in externals)
    if set(counts) - {"A", "lbar"}:
        return False
    if counts["lbar"] != 1:
        return False
    if counts["A"] < 1:
        return False
    return True


def exact_signature(pairs, externals):
    pair_sig = tuple(
        sorted(
            (
                tuple(sorted((left.id, right.id))),
                kind,
            )
            for left, right, kind in pairs
        )
    )
    ext_sig = tuple(sorted((ext.id, ext.field) for ext in externals))
    return pair_sig, ext_sig


def summarize_graph(total_g_power: int, insertion: VertexTemplate, actions, pairs, externals):
    action_counter = Counter(template.name for template in actions)
    external_fields = [port.field for port in externals]
    pair_lines = []
    for left, right, kind in sorted(
        pairs,
        key=lambda item: (
            item[0].vertex_id,
            item[0].port_name,
            item[1].vertex_id,
            item[1].port_name,
            item[2],
        ),
    ):
        pair_lines.append(
            {
                "from": f"{left.vertex_id}:{left.port_name}",
                "to": f"{right.vertex_id}:{right.port_name}",
                "kind": kind,
            }
        )
    external_lines = [
        {
            "port": f"{port.vertex_id}:{port.port_name}",
            "field": port.field,
            "slot": port.slot_label,
        }
        for port in sorted(externals, key=lambda p: (p.vertex_id, p.port_name))
    ]
    return {
        "total_g_power": total_g_power,
        "insertion_term": insertion.name,
        "action_vertices": dict(sorted(action_counter.items())),
        "external_fields": sorted(external_fields),
        "internal_contractions": pair_lines,
        "external_ports": external_lines,
    }


def enumerate_pairings(total_g_power: int, vertices, insertion: VertexTemplate, actions, ports, external_target, seen_signatures, entries):
    ports_sorted = sorted(ports, key=lambda p: p.id)

    def rec(remaining: list[PortInstance], externals: list[PortInstance], pairs):
        if not can_complete(remaining, 0):
            return

        if not remaining:
            if not external_sector_ok(externals):
                return
            if not fully_connected_after_insertion_split(vertices, pairs, externals):
                return
            signature = exact_signature(pairs, externals)
            if signature in seen_signatures:
                return
            seen_signatures.add(signature)
            entries.append(summarize_graph(total_g_power, insertion, actions, pairs, externals))
            return

        first = remaining[0]
        tail = remaining[1:]
        for idx, second in enumerate(tail):
            kind = compatible(first, second)
            if kind is None:
                continue
            if not ALLOW_SAME_VERTEX_CONTRACTIONS and first.vertex_id == second.vertex_id:
                continue
            if first.vertex_id == "O" and second.vertex_id == "O":
                continue
            new_remaining = tail[:idx] + tail[idx + 1 :]
            rec(new_remaining, externals, [*pairs, (first, second, kind)])

    if external_target < 0:
        return
    if external_target > len(ports_sorted):
        return

    def choose_externals(start: int, need: int, chosen: list[PortInstance]):
        if need == 0:
            if not external_sector_ok(chosen):
                return
            remaining = [port for port in ports_sorted if port.id not in {ext.id for ext in chosen}]
            if not can_complete(remaining, 0):
                return
            rec(remaining, chosen, [])
            return
        for idx in range(start, len(ports_sorted) - need + 1):
            choose_externals(idx + 1, need - 1, [*chosen, ports_sorted[idx]])

    choose_externals(0, external_target, [])


def markdown_report(entries, total_count):
    lines = []
    lines.append("# N=1 SYM Q_1(f_{++}f_{++}) 1-loop graph enumeration")
    lines.append("")
    lines.append("## Assumptions")
    lines.append("")
    lines.append("- theory: `N=1 SYM (Euclidean)`")
    lines.append("- insertion: full elementary-field expansion of `Q_1(f_{++}f_{++})` through explicit insertion order `g^2`")
    lines.append("- action vertices: `A\\lambda\\bar\\lambda`, `AAA`, `AAAA`, `\\bar c A c`")
    lines.append("- propagators: `A-A`, `\\lambda-\\bar\\lambda`, `c-\\bar c`")
    lines.append("- total explicit coupling order scanned over `g^2`, `g^3`, `g^4`")
    lines.append("- loop number fixed to `L=1`")
    lines.append("- self-contractions inside insertion: excluded")
    lines.append(f"- same-vertex contractions in general: `{ALLOW_SAME_VERTEX_CONTRACTIONS}`")
    lines.append("- valid sector: strictly fully connected graphs after splitting the insertion letters; external fields only in `{A,lbar}` and exactly one `lbar`")
    lines.append("")
    lines.append("## Total unique graphs")
    lines.append("")
    lines.append(f"- `{total_count}`")
    lines.append("")

    grouped = defaultdict(list)
    for entry in entries:
        grouped[(entry["total_g_power"], entry["insertion_term"], tuple(entry["external_fields"]))].append(entry)

    lines.append("## Summary by explicit order, insertion term and external sector")
    lines.append("")
    for (total_g_power, insertion_term, external_fields), group in sorted(grouped.items()):
        lines.append(f"- `g^{total_g_power}` `{insertion_term}` `{list(external_fields)}`: `{len(group)}`")
    lines.append("")

    lines.append("## Graph list")
    lines.append("")
    for idx, entry in enumerate(entries, start=1):
        lines.append(f"### G{idx:03d}")
        lines.append("")
        lines.append(f"- total explicit order: `g^{entry['total_g_power']}`")
        lines.append(f"- insertion term: `{entry['insertion_term']}`")
        action_string = ", ".join(f"`{k}` x {v}" for k, v in entry["action_vertices"].items()) or "`none`"
        lines.append(f"- action vertices: {action_string}")
        lines.append(f"- external fields: `{entry['external_fields']}`")
        lines.append("- internal contractions:")
        for contraction in entry["internal_contractions"]:
            lines.append(f"  - `{contraction['from']}` --[{contraction['kind']}]-- `{contraction['to']}`")
        lines.append("- external ports:")
        for ext in entry["external_ports"]:
            slot = f" ({ext['slot']})" if ext["slot"] else ""
            lines.append(f"  - `{ext['port']}` : `{ext['field']}`{slot}")
        lines.append("")
    return "\n".join(lines)


def summary_payload(entries):
    by_total_g_power = Counter(entry["total_g_power"] for entry in entries)
    by_insertion = Counter(entry["insertion_term"] for entry in entries)
    by_external_fields = Counter(tuple(entry["external_fields"]) for entry in entries)
    by_action_multiset = Counter(tuple(sorted(entry["action_vertices"].items())) for entry in entries)
    by_sector = Counter(
        (
            entry["total_g_power"],
            entry["insertion_term"],
            tuple(entry["external_fields"]),
            tuple(sorted(entry["action_vertices"].items())),
        )
        for entry in entries
    )
    sector_examples = []
    for (total_g_power, insertion_term, external_fields, action_multiset), count_value in sorted(
        by_sector.items(),
        key=lambda item: (-item[1], item[0][0], item[0][1], list(item[0][2]), list(item[0][3])),
    ):
        sector_examples.append(
            {
                "total_g_power": total_g_power,
                "insertion_term": insertion_term,
                "external_fields": list(external_fields),
                "action_vertices": dict(action_multiset),
                "count": count_value,
            }
        )
    return {
        "graph_count": len(entries),
        "by_total_g_power": dict(sorted(by_total_g_power.items())),
        "by_insertion_term": dict(sorted(by_insertion.items())),
        "by_external_fields": {str(list(k)): v for k, v in sorted(by_external_fields.items())},
        "by_action_multiset": [
            {
                "action_vertices": dict(multiset),
                "count": count_value,
            }
            for multiset, count_value in by_action_multiset.most_common(20)
        ],
        "by_sector": sector_examples,
    }


def summary_markdown(summary):
    lines = []
    lines.append("# N=1 SYM Q_1(f_{++}f_{++}) 1-loop summary")
    lines.append("")
    lines.append(f"- total graphs: `{summary['graph_count']}`")
    lines.append("")
    lines.append("## By explicit order")
    lines.append("")
    for key, value in summary["by_total_g_power"].items():
        lines.append(f"- `g^{key}`: `{value}`")
    lines.append("")
    lines.append("## By insertion term")
    lines.append("")
    for key, value in summary["by_insertion_term"].items():
        lines.append(f"- `{key}`: `{value}`")
    lines.append("")
    lines.append("## By external fields")
    lines.append("")
    for key, value in summary["by_external_fields"].items():
        lines.append(f"- `{key}`: `{value}`")
    lines.append("")
    lines.append("## By action multiset")
    lines.append("")
    for item in summary["by_action_multiset"]:
        label = ", ".join(f"`{k}` x {v}" for k, v in item["action_vertices"].items()) or "`none`"
        lines.append(f"- {label}: `{item['count']}`")
    lines.append("")
    lines.append("## By sector")
    lines.append("")
    for item in summary["by_sector"]:
        label = ", ".join(f"`{k}` x {v}" for k, v in item["action_vertices"].items()) or "`none`"
        lines.append(
            f"- `g^{item['total_g_power']}` `{item['insertion_term']}` `{item['external_fields']}` {label}: `{item['count']}`"
        )
    lines.append("")
    return "\n".join(lines)


def main():
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)

    seen_signatures = set()
    entries = []

    for total_g_power in TOTAL_G_POWERS:
        for insertion in INSERTION_TEMPLATES:
            residual_power = total_g_power - insertion.g_power
            if residual_power < 0:
                continue
            for action_multiset in generate_action_multisets(residual_power):
                vertices = instantiate_vertices(insertion, action_multiset)
                ports = instantiate_ports(vertices)
                total_half_edges = len(ports)
                vertex_count = len(vertices)
                internal_edges = vertex_count
                external_target = total_half_edges - 2 * internal_edges
                if external_target < 0:
                    continue
                enumerate_pairings(
                    total_g_power,
                    vertices,
                    insertion,
                    action_multiset,
                    ports,
                    external_target,
                    seen_signatures,
                    entries,
                )

    entries.sort(
        key=lambda entry: (
            entry["insertion_term"],
            json.dumps(entry["action_vertices"], sort_keys=True),
            json.dumps(entry["external_fields"]),
            json.dumps(entry["internal_contractions"]),
        )
    )

    payload = {
        "assumptions": {
            "theory": "N=1 SYM (Euclidean)",
            "operator": "Q_1(f_{++}f_{++})",
            "total_g_power_scan": list(TOTAL_G_POWERS),
            "loop_number": 1,
            "action_vertices": [template.name for template in ACTION_TEMPLATES],
            "self_contraction_inside_insertion": False,
            "allow_same_vertex_contractions": ALLOW_SAME_VERTEX_CONTRACTIONS,
            "connectedness": "all insertion letters are disconnected by default; remove the artificial O-core incidence and require the entire remaining graph to be connected",
            "external_sector": "all external fields in {A,lbar}, exactly one lbar, at least one A",
        },
        "graph_count": len(entries),
        "graphs": entries,
    }
    summary = summary_payload(entries)

    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False))
    OUT_MD.write_text(markdown_report(entries, len(entries)))
    OUT_SUMMARY_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False))
    OUT_SUMMARY_MD.write_text(summary_markdown(summary))

    print(f"graph_count={len(entries)}")
    print(OUT_JSON)


if __name__ == "__main__":
    main()
