from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
from itertools import product
import json
from pathlib import Path

import networkx as nx
from networkx.algorithms.graph_hashing import weisfeiler_lehman_graph_hash


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets" / "step4" / "n1_sym_euclidean"


@dataclass(frozen=True)
class SlotDef:
    name: str
    field: str
    display_tex: str | None = None


@dataclass(frozen=True)
class TypedVertexTemplate:
    name: str
    kind: str
    g_power: int
    ordered_slots: bool
    slots: tuple[SlotDef, ...]

    @property
    def valence(self) -> int:
        return len(self.slots)


@dataclass(frozen=True)
class VertexInstance:
    id: str
    template: TypedVertexTemplate


@dataclass(frozen=True)
class SlotInstance:
    id: str
    vertex_id: str
    template_name: str
    kind: str
    slot_index: int
    ordered_slot: bool
    field: str
    display_tex: str


@dataclass(frozen=True)
class ProbeConstraint:
    allowed_fields: tuple[str, ...]
    exact_counts: tuple[tuple[str, int], ...] = ()
    min_counts: tuple[tuple[str, int], ...] = ()

    def matches(self, fields: list[str]) -> bool:
        counts = Counter(fields)
        if set(counts) - set(self.allowed_fields):
            return False
        for field, value in self.exact_counts:
            if counts[field] != value:
                return False
        for field, value in self.min_counts:
            if counts[field] < value:
                return False
        return True


@dataclass(frozen=True)
class RawTopology:
    total_g_power: int
    loop_number: int
    vertices: tuple[VertexInstance, ...]
    internal_pairs: tuple[tuple[str, str], ...]
    probe_slots: tuple[str, ...]


@dataclass(frozen=True)
class WickGraph:
    total_g_power: int
    loop_number: int
    vertex_templates: tuple[tuple[str, str], ...]
    internal_pairs: tuple[tuple[str, str, str], ...]
    probe_legs: tuple[tuple[str, str], ...]


COMPATIBILITY = {
    ("A", "A"): "A",
    ("lam", "lbar"): "fermion",
    ("lbar", "lam"): "fermion",
    ("c", "cbar"): "ghost",
    ("cbar", "c"): "ghost",
}


O12_DLB_A = TypedVertexTemplate(
    name="O12_dlb_A",
    kind="operator",
    g_power=0,
    ordered_slots=True,
    slots=(
        SlotDef("Qf1_lambdabar", "lbar", r"i\nabla_{+\dot\alpha}\widetilde\lambda^{\dot\alpha}"),
        SlotDef("f2_A", "A", r"f_{++}"),
    ),
)

O21_A_DLB = TypedVertexTemplate(
    name="O21_A_dlb",
    kind="operator",
    g_power=0,
    ordered_slots=True,
    slots=(
        SlotDef("f1_A", "A", r"f_{++}"),
        SlotDef("Qf2_lambdabar", "lbar", r"i\nabla_{+\dot\alpha}\widetilde\lambda^{\dot\alpha}"),
    ),
)

O12_DLB_AEXPW = TypedVertexTemplate(
    name="O12_dlb_Aexpw",
    kind="operator",
    g_power=0,
    ordered_slots=True,
    slots=(
        SlotDef("Qf1_lambdabar", "lbar", r"i\nabla_{+\dot\alpha}\widetilde\lambda^{\dot\alpha}"),
        SlotDef("f2_Aexpw", "A", r"e^{w\cdot\nabla_+}f_{++}"),
    ),
)

O21_A_DLB_EXPW = TypedVertexTemplate(
    name="O21_A_dlb_expw",
    kind="operator",
    g_power=0,
    ordered_slots=True,
    slots=(
        SlotDef("f1_A", "A", r"f_{++}"),
        SlotDef("Qf2_lambdabar_expw", "lbar", r"e^{w\cdot\nabla_+}\!\left(i\nabla_{+\dot\alpha}\widetilde\lambda^{\dot\alpha}\right)"),
    ),
)

V_AAA = TypedVertexTemplate(
    name="V_AAA",
    kind="interaction",
    g_power=1,
    ordered_slots=False,
    slots=(
        SlotDef("A1", "A"),
        SlotDef("A2", "A"),
        SlotDef("A3", "A"),
    ),
)

V_A_LAM_LBAR = TypedVertexTemplate(
    name="V_A_lambda_lambdabar",
    kind="interaction",
    g_power=1,
    ordered_slots=False,
    slots=(
        SlotDef("A", "A"),
        SlotDef("lambda", "lam"),
        SlotDef("lambdabar", "lbar"),
    ),
)

V_CBAR_A_C = TypedVertexTemplate(
    name="V_cbar_A_c",
    kind="interaction",
    g_power=1,
    ordered_slots=False,
    slots=(
        SlotDef("cbar", "cbar"),
        SlotDef("A", "A"),
        SlotDef("c", "c"),
    ),
)

V_AAAA = TypedVertexTemplate(
    name="V_AAAA",
    kind="interaction",
    g_power=2,
    ordered_slots=False,
    slots=(
        SlotDef("A1", "A"),
        SlotDef("A2", "A"),
        SlotDef("A3", "A"),
        SlotDef("A4", "A"),
    ),
)


def instantiate_vertices(operator_template: TypedVertexTemplate, action_templates: list[TypedVertexTemplate]) -> tuple[VertexInstance, ...]:
    vertices = [VertexInstance(id="O1", template=operator_template)]
    counters = defaultdict(int)
    for template in action_templates:
        counters[template.name] += 1
        vertices.append(VertexInstance(id=f"{template.name}#{counters[template.name]}", template=template))
    return tuple(vertices)


def instantiate_slots(vertices: tuple[VertexInstance, ...]) -> tuple[SlotInstance, ...]:
    slots = []
    for vertex in vertices:
        for slot_index, slot_def in enumerate(vertex.template.slots):
            slots.append(
                SlotInstance(
                    id=f"{vertex.id}:{slot_index}",
                    vertex_id=vertex.id,
                    template_name=vertex.template.name,
                    kind=vertex.template.kind,
                    slot_index=slot_index,
                    ordered_slot=vertex.template.ordered_slots,
                    field=slot_def.field,
                    display_tex=slot_def.display_tex or slot_def.field,
                )
            )
    return tuple(slots)


def generate_action_template_multisets(target_g_power: int, templates: tuple[TypedVertexTemplate, ...], start: int = 0):
    if target_g_power == 0:
        yield []
        return
    for idx in range(start, len(templates)):
        template = templates[idx]
        if template.g_power > target_g_power:
            continue
        for tail in generate_action_template_multisets(target_g_power - template.g_power, templates, idx):
            yield [template, *tail]


def probe_number(vertices: tuple[VertexInstance, ...], slots: tuple[SlotInstance, ...], loop_number: int) -> int:
    internal_edges = loop_number + len(vertices) - 1
    return len(slots) - 2 * internal_edges


def strict_connected_after_operator_split(
    vertices: tuple[VertexInstance, ...],
    slots: tuple[SlotInstance, ...],
    internal_pairs: list[tuple[SlotInstance, SlotInstance]],
    probes: list[SlotInstance],
) -> bool:
    graph = nx.Graph()
    for vertex in vertices:
        if vertex.template.kind == "interaction":
            graph.add_node(f"core::{vertex.id}")
    for slot in slots:
        slot_node = f"slot::{slot.id}"
        graph.add_node(slot_node)
        if slot.kind == "interaction":
            graph.add_edge(f"core::{slot.vertex_id}", slot_node, label="inc")
    for left, right in internal_pairs:
        graph.add_edge(f"slot::{left.id}", f"slot::{right.id}", label="prop")
    for slot in probes:
        probe_node = f"probe::{slot.id}"
        graph.add_node(probe_node)
        graph.add_edge(f"slot::{slot.id}", probe_node, label="probe")
    if graph.number_of_nodes() == 0:
        return False
    return nx.is_connected(graph)


def raw_signature(internal_pairs: list[tuple[SlotInstance, SlotInstance]], probes: list[SlotInstance]) -> tuple:
    pair_sig = tuple(sorted(tuple(sorted((left.id, right.id))) for left, right in internal_pairs))
    probe_sig = tuple(sorted(slot.id for slot in probes))
    return pair_sig, probe_sig


def create_topologies(
    total_g_power: int,
    loop_number: int,
    operator_template: TypedVertexTemplate,
    action_templates: list[TypedVertexTemplate],
    allow_same_vertex_contractions: bool = False,
) -> list[RawTopology]:
    vertices = instantiate_vertices(operator_template, action_templates)
    slots = tuple(sorted(instantiate_slots(vertices), key=lambda item: item.id))
    n_probes = probe_number(vertices, slots, loop_number)
    if n_probes < 0:
        return []

    seen = set()
    out: list[RawTopology] = []

    def rec(remaining: list[SlotInstance], probes: list[SlotInstance], internal_pairs: list[tuple[SlotInstance, SlotInstance]]):
        if not remaining:
            if len(probes) != n_probes:
                return
            if not strict_connected_after_operator_split(vertices, slots, internal_pairs, probes):
                return
            signature = raw_signature(internal_pairs, probes)
            if signature in seen:
                return
            seen.add(signature)
            out.append(
                RawTopology(
                    total_g_power=total_g_power,
                    loop_number=loop_number,
                    vertices=vertices,
                    internal_pairs=tuple(sorted(tuple(sorted((left.id, right.id))) for left, right in internal_pairs)),
                    probe_slots=tuple(sorted(slot.id for slot in probes)),
                )
            )
            return

        first = remaining[0]
        tail = remaining[1:]

        if len(probes) < n_probes:
            rec(tail, [*probes, first], internal_pairs)

        for idx, second in enumerate(tail):
            if not allow_same_vertex_contractions and first.vertex_id == second.vertex_id:
                continue
            new_remaining = tail[:idx] + tail[idx + 1 :]
            rec(new_remaining, probes, [*internal_pairs, (first, second)])

    rec(list(slots), [], [])
    return out


def slot_lookup(topology: RawTopology) -> dict[str, SlotInstance]:
    return {slot.id: slot for slot in instantiate_slots(topology.vertices)}


def insert_fields(topologies: list[RawTopology], probe_constraint: ProbeConstraint) -> list[WickGraph]:
    out = []
    for topology in topologies:
        slots = slot_lookup(topology)
        pair_payload = []
        ok = True
        for left_id, right_id in topology.internal_pairs:
            left = slots[left_id]
            right = slots[right_id]
            kind = COMPATIBILITY.get((left.field, right.field))
            if kind is None:
                ok = False
                break
            pair_payload.append((left_id, right_id, kind))
        if not ok:
            continue
        probe_payload = tuple(sorted((slot_id, slots[slot_id].field) for slot_id in topology.probe_slots))
        if not probe_constraint.matches([field for _slot_id, field in probe_payload]):
            continue
        vertex_templates = tuple(sorted((vertex.id, vertex.template.name) for vertex in topology.vertices))
        out.append(
            WickGraph(
                total_g_power=topology.total_g_power,
                loop_number=topology.loop_number,
                vertex_templates=vertex_templates,
                internal_pairs=tuple(sorted(pair_payload)),
                probe_legs=probe_payload,
            )
        )
    return out


def graph_signature(graph: WickGraph) -> tuple:
    return (
        graph.total_g_power,
        graph.loop_number,
        graph.vertex_templates,
        graph.internal_pairs,
        graph.probe_legs,
    )


def canonical_graph(graph: WickGraph) -> nx.Graph:
    g = nx.Graph()
    template_map = dict(graph.vertex_templates)
    action_vertices = [vertex_id for vertex_id, template_name in graph.vertex_templates if template_name.startswith("V_")]
    operator_vertices = [vertex_id for vertex_id, template_name in graph.vertex_templates if template_name.startswith("O")]

    action_index = {vertex_id: idx for idx, vertex_id in enumerate(sorted(action_vertices), start=1)}
    operator_index = {vertex_id: idx for idx, vertex_id in enumerate(sorted(operator_vertices), start=1)}

    for vertex_id, template_name in graph.vertex_templates:
        if vertex_id in operator_index:
            g.add_node(f"opcore::{operator_index[vertex_id]}", label=f"opcore:{template_name}")
        else:
            g.add_node(f"actcore::{action_index[vertex_id]}", label=f"actcore:{template_name}")

    slot_field_map = {}
    for left, right, kind in graph.internal_pairs:
        if kind == "A":
            slot_field_map[left] = "A"
            slot_field_map[right] = "A"
        elif kind == "fermion":
            if left.endswith(":1") or "lambda" in template_map[left.split(":")[0]]:
                slot_field_map[left] = "lam"
                slot_field_map[right] = "lbar"
            else:
                slot_field_map[left] = "lbar"
                slot_field_map[right] = "lam"
        else:
            slot_field_map[left] = "c"
            slot_field_map[right] = "cbar"
    for slot_id, field in graph.probe_legs:
        slot_field_map[slot_id] = field

    def ensure_port(slot_id: str):
        vertex_id, slot_index_str = slot_id.split(":")
        slot_index = int(slot_index_str)
        node_id = f"slot::{slot_id}"
        if node_id in g:
            return node_id
        field = slot_field_map.get(slot_id, "?")
        if vertex_id in operator_index:
            core = f"opcore::{operator_index[vertex_id]}"
            label = f"opslot:{slot_index}:{field}"
        else:
            core = f"actcore::{action_index[vertex_id]}"
            label = f"actslot:{field}"
        g.add_node(node_id, label=label)
        g.add_edge(core, node_id, label="inc")
        return node_id

    for left, right, kind in graph.internal_pairs:
        g.add_edge(ensure_port(left), ensure_port(right), label=f"prop:{kind}")
    for slot_id, field in graph.probe_legs:
        probe_id = f"probe::{slot_id}:{field}"
        g.add_node(probe_id, label=f"probe:{field}")
        g.add_edge(ensure_port(slot_id), probe_id, label="probe")
    return g


def node_match(a, b):
    return a["label"] == b["label"]


def edge_match(a, b):
    return a["label"] == b["label"]


def compress_topologies(graphs: list[WickGraph]) -> list[dict]:
    buckets: dict[tuple, list[dict]] = defaultdict(list)
    for graph in graphs:
        topo = canonical_graph(graph)
        topo_hash = weisfeiler_lehman_graph_hash(topo, node_attr="label", edge_attr="label")
        key = (graph.total_g_power, topo_hash)
        placed = False
        for item in buckets[key]:
            if nx.is_isomorphic(topo, item["graph"], node_match=node_match, edge_match=edge_match):
                item["multiplicity"] += 1
                placed = True
                break
        if not placed:
            buckets[key].append(
                {
                    "graph": topo,
                    "total_g_power": graph.total_g_power,
                    "vertex_templates": graph.vertex_templates,
                    "probe_fields": tuple(field for _slot, field in graph.probe_legs),
                    "multiplicity": 1,
                    "representative_pairs": graph.internal_pairs,
                    "representative_probes": graph.probe_legs,
                }
            )
    classes = []
    for items in buckets.values():
        for item in items:
            classes.append(
                {
                    "total_g_power": item["total_g_power"],
                    "vertex_templates": item["vertex_templates"],
                    "probe_fields": item["probe_fields"],
                    "multiplicity": item["multiplicity"],
                    "representative_pairs": item["representative_pairs"],
                    "representative_probes": item["representative_probes"],
                }
            )
    classes.sort(
        key=lambda item: (
            item["total_g_power"],
            item["vertex_templates"],
            item["multiplicity"],
            item["representative_pairs"],
        )
    )
    return classes


def run_demo(
    operator_templates: tuple[TypedVertexTemplate, TypedVertexTemplate],
    demo_label: str,
    orders: tuple[int, ...] = (2, 3),
) -> tuple[dict, list[dict]]:
    interaction_templates = (V_AAA, V_A_LAM_LBAR, V_CBAR_A_C, V_AAAA)
    topologies = []
    for operator_template in operator_templates:
        for total_g_power in orders:
            for action_multiset in generate_action_template_multisets(total_g_power, interaction_templates):
                topologies.extend(
                    create_topologies(
                        total_g_power=total_g_power,
                        loop_number=1,
                        operator_template=operator_template,
                        action_templates=action_multiset,
                        allow_same_vertex_contractions=False,
                    )
                )

    graphs = insert_fields(
        topologies,
        ProbeConstraint(
            allowed_fields=("A", "lbar"),
            exact_counts=(("lbar", 1),),
            min_counts=(("A", 1),),
        ),
    )
    unique_graphs = sorted({graph_signature(graph): graph for graph in graphs}.values(), key=graph_signature)
    classes = compress_topologies(unique_graphs)
    summary = {
        "demo": demo_label,
        "generator_style": "FeynArts-inspired: typed-template topologies -> compatibility filter -> canonical classes",
        "orders": list(orders),
        "raw_inserted_graph_count": len(unique_graphs),
        "topology_class_count": len(classes),
        "by_total_g_power": dict(sorted(Counter(graph.total_g_power for graph in unique_graphs).items())),
        "topology_by_total_g_power": dict(sorted(Counter(item["total_g_power"] for item in classes).items())),
    }
    return summary, classes


def run_q1_fpp_fpp_demo(orders: tuple[int, ...] = (2, 3)) -> tuple[dict, list[dict]]:
    return run_demo(
        operator_templates=(O12_DLB_A, O21_A_DLB),
        demo_label="Q_1(f_{++}f_{++}) in N=1 SYM (Euclidean)",
        orders=orders,
    )


def run_q1_fpp_expw_fpp_demo(orders: tuple[int, ...] = (2, 3)) -> tuple[dict, list[dict]]:
    return run_demo(
        operator_templates=(O12_DLB_AEXPW, O21_A_DLB_EXPW),
        demo_label="Q_1(f_{++}e^{w\\cdot\\nabla_+}f_{++}) in N=1 SYM (Euclidean)",
        orders=orders,
    )


def write_demo_outputs(summary: dict, classes: list[dict]) -> tuple[Path, Path]:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    order_tag = "g" + "".join(str(order) for order in summary["orders"])
    demo_slug = "q1_fpp_expw_fpp" if "e^{w\\cdot\\nabla_+}" in summary["demo"] else "q1_fpp_fpp"
    json_path = OUT_DIR / f"feynarts_style_n1sym_{demo_slug}_demo_{order_tag}.json"
    md_path = OUT_DIR / f"feynarts_style_n1sym_{demo_slug}_demo_{order_tag}.md"
    json_path.write_text(json.dumps({"summary": summary, "classes": classes}, indent=2, ensure_ascii=False))

    lines = []
    lines.append("# FeynArts-style N=1 SYM graph-generator demo")
    lines.append("")
    lines.append(f"- demo: `{summary['demo']}`")
    lines.append(f"- raw inserted graphs: `{summary['raw_inserted_graph_count']}`")
    lines.append(f"- topological classes: `{summary['topology_class_count']}`")
    lines.append("")
    lines.append("## By explicit order")
    lines.append("")
    for key, value in summary["by_total_g_power"].items():
        lines.append(f"- `g^{key}` raw inserted graphs: `{value}`")
    for key, value in summary["topology_by_total_g_power"].items():
        lines.append(f"- `g^{key}` topological classes: `{value}`")
    lines.append("")
    lines.append("## First classes")
    lines.append("")
    for idx, item in enumerate(classes[:20], start=1):
        lines.append(
            f"- `C{idx:03d}` `g^{item['total_g_power']}` `{item['vertex_templates']}` `{list(item['probe_fields'])}` `mult={item['multiplicity']}`"
        )
    md_path.write_text("\n".join(lines))
    return json_path, md_path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", choices=("q1_fpp_fpp", "q1_fpp_expw_fpp"), default="q1_fpp_fpp")
    parser.add_argument("--orders", nargs="+", type=int, default=[2, 3])
    args = parser.parse_args()

    if args.demo == "q1_fpp_fpp":
        summary, classes = run_q1_fpp_fpp_demo(tuple(args.orders))
    elif args.demo == "q1_fpp_expw_fpp":
        summary, classes = run_q1_fpp_expw_fpp_demo(tuple(args.orders))
    else:
        raise SystemExit(f"unsupported demo: {args.demo}")
    json_path, md_path = write_demo_outputs(summary, classes)
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    print(json_path)
    print(md_path)


if __name__ == "__main__":
    main()
