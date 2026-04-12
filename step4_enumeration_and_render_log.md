# Step 4 Enumeration and Render Log

## Scope

- theory: `N=1 SYM (Euclidean)`
- operator: `Q_1(f_{++}f_{++})`
- target: `Step 4` diagram generation, topology compression, representative rendering

## 1-loop render method

- script: `tools/render_n1sym_q1_fpp_fpp_step4.py`
- backend: `matplotlib`
- style:
  - gallery content: the `g^2` strictly fully connected topological representatives arranged as `3` row families times `12/21` mirror columns
  - operator insertion: square box `O`
  - insertion legs: the `A` and `\widetilde\lambda` legs now start at the operator box and attach explicitly to the graph
  - interaction vertices: black filled dots
  - gauge propagator: wavy line
  - fermion propagator: solid line with arrow
  - labels: `STIX` math font with white background patch
- output:
  - `assets/step4/n1_sym_euclidean/q1_fpp_fpp_1loop.png`
  - `assets/step4/n1_sym_euclidean/q1_fpp_fpp_1loop.pdf`

## 1-loop full enumeration method

- script: `tools/enumerate_n1sym_q1_fpp_fpp_1loop.py`
- enumeration level: raw Wick contractions
- action vertex templates:
  - `V_A_lambda_lambdabar`
  - `V_AAA`
  - `V_AAAA`
  - `V_cbar_A_c`
- insertion templates:
  - explicit field-level expansion of `Q_1(f_{++}f_{++})` through insertion order `g^2`
- propagator compatibility:
  - `A-A`
  - `lam-lbar`
  - `c-cbar`
- connectedness criterion:
  - do **not** use the whole operator box `O` as an artificial connector
  - every insertion letter of `O` is disconnected by default
  - remove the artificial `O`-core incidence and require the entire remaining graph to be connected
- fixed constraints:
  - loop number: `L=1`
  - total explicit coupling order scanned over `g^2`, `g^3`, `g^4`
  - self-contractions inside insertion: excluded
  - same-vertex contractions: excluded
  - external sector: only `{A,\bar\lambda}`-type outputs, exactly one `lbar`, any number of `A`
- raw output:
  - `g^2`: `20`
  - `g^3`: `348`
  - `g^4`: `9152`
  - total: `9520`
- raw files:
  - `assets/step4/n1_sym_euclidean/q1_fpp_fpp_1loop_graphs.json`
  - `assets/step4/n1_sym_euclidean/q1_fpp_fpp_1loop_graphs.md`
  - `assets/step4/n1_sym_euclidean/q1_fpp_fpp_1loop_summary.json`
  - `assets/step4/n1_sym_euclidean/q1_fpp_fpp_1loop_summary.md`

## 1-loop topology compression

- script: `tools/compress_n1sym_q1_fpp_fpp_1loop_topologies.py`
- graph model:
  - insertion core node with insertion-term label
  - action-vertex core nodes with vertex-type labels
  - insertion/action port nodes
  - propagator-species edges
  - external-leg edges
- compressed counts:
  - `g^2`: `6` topological classes
  - `g^3`: `20` topological classes
  - `g^4`: `66` topological classes
  - total: `92`
- topology files:
  - `assets/step4/n1_sym_euclidean/q1_fpp_fpp_1loop_topologies.json`
  - `assets/step4/n1_sym_euclidean/q1_fpp_fpp_1loop_topologies.md`
  - `assets/step4/n1_sym_euclidean/q1_fpp_fpp_1loop_topologies_summary.md`

## `g^3` analytic-family extraction

- file:
  - `assets/step4/n1_sym_euclidean/q1_fpp_fpp_1loop_g3_families.md`
- strict fully connected `g^3` counts:
  - raw Wick contractions: `348`
  - topological classes: `20`
  - `12/21` mirror-reduced families: `10`
- surviving analytic families for the candidate `(\nabla-\partial)(f_{++}\widetilde\lambda)` completion:
  - `C_1 = V_AAA (V_{A\lambda\widetilde\lambda})^2`
  - `C_2 = (V_AAA)^2 V_{A\lambda\widetilde\lambda}`
  - `C_3 = V_AAAA V_{A\lambda\widetilde\lambda}`
  - `C_4 = (V_{A\lambda\widetilde\lambda})^3`
- channels removed by the stricter full-connected filter:
  - disconnected ghost pair sector
  - disconnected `AAA-AAA` spectator bubble sector

## 2-loop raw enumeration method

- script: `tools/enumerate_n1sym_q1_fpp_fpp_2loop.py`
- enumeration level: raw Wick contractions
- action vertex templates:
  - `V_A_lambda_lambdabar`
  - `V_AAA`
  - `V_AAAA`
  - `V_cbar_A_c`
- insertion templates:
  - explicit field-level expansion of `Q_1(f_{++}f_{++})` through insertion order `g^2`
- propagator compatibility:
  - `A-A`
  - `lam-lbar`
  - `c-cbar`
- fixed constraints:
  - total explicit coupling order: `g^4`
  - loop number: `L=2`
  - connected Wick contractions only at the raw vertex-incidence level
  - self-contractions inside insertion: excluded
  - same-vertex contractions: excluded
  - external slots: one `A`, one `lbar`
- raw output:
  - `graph_count = 134924`
- raw files:
  - `assets/step4/n1_sym_euclidean/q1_fpp_fpp_2loop_graphs.json`
  - `assets/step4/n1_sym_euclidean/q1_fpp_fpp_2loop_graphs.md`
  - `assets/step4/n1_sym_euclidean/q1_fpp_fpp_2loop_summary.json`
  - `assets/step4/n1_sym_euclidean/q1_fpp_fpp_2loop_summary.md`

## Fine topology compression

- script: `tools/compress_n1sym_q1_fpp_fpp_2loop_topologies.py`
- graph model:
  - insertion core node
  - action-vertex core nodes
  - port nodes
  - internal propagator edges
  - external-leg edges
- topology preserves:
  - insertion term
  - action vertex type multiset
  - insertion port labels
  - propagator species
  - external field species
- topology forgets:
  - labels of identical action-vertex copies
  - labels of identical `A`-legs inside `AAA` and `AAAA`
- graph symmetry factor convention:
  - `S = 1 / |Aut(topology graph)|`
- fine compressed count:
  - `552` classes

## Operator-connected refinement

- script: `tools/coarsen_n1sym_q1_fpp_fpp_2loop.py`
- motivation:
  - the composite operator box `O` must not be treated as an artificial connector between different operator slots
- connectedness criterion:
  1. remove the artificial `O`-core incidence edges
  2. keep action-vertex incidence edges
  3. require all insertion ports to lie in one connected component
- after this filter:
  - operator-connected fine classes: `172`
  - operator-connected raw Wick contractions: `11696`

## Coarse topology layers

- field-labeled topology:
  - forget insertion term
  - forget insertion port labels
  - forget labels of identical action-vertex copies
  - preserve propagator species
  - preserve external field species
  - count: `64`
- bare skeleton topology:
  - forget action-vertex types
  - forget propagator species
  - forget external field species
  - keep only graph skeleton and operator attachment structure
  - count: `19`
- coarse files:
  - `assets/step4/n1_sym_euclidean/q1_fpp_fpp_2loop_coarse_classes.json`
  - `assets/step4/n1_sym_euclidean/q1_fpp_fpp_2loop_coarse_summary.md`

## 10-diagram gallery selection

- selection rule:
  1. sort coarse field-labeled classes by descending raw multiplicity
  2. first pass: keep one representative for each distinct action-vertex multiset
  3. second pass: if still fewer than `10`, fill from unused bare skeletons
- current selected gallery classes:
  - `F001 / B010`
  - `F005 / B003`
  - `F007 / B014`
  - `F010 / B005`
  - `F017 / B002`
  - `F019 / B004`
  - `F020 / B018`
  - `F021 / B012`
  - `F033 / B001`
  - `F038 / B019`

## 2-loop gallery render method

- script: `tools/render_n1sym_q1_fpp_fpp_2loop_gallery.py`
- input: `selected_gallery_classes` from `q1_fpp_fpp_2loop_coarse_classes.json`
- graph realization:
  - operator node: square box
  - action vertices: black filled dots
  - internal gauge edges: wavy curves
  - internal fermion edges: solid curves with arrows
  - ghost edges: dashed curves with arrows
  - external legs: radial attachment from graph centroid
- layout:
  - spring layout for the core graph
  - operator box fixed near the left
  - external legs placed by outward normal spread
- output:
  - `assets/step4/n1_sym_euclidean/q1_fpp_fpp_2loop_top10.png`
  - `assets/step4/n1_sym_euclidean/q1_fpp_fpp_2loop_top10.pdf`

## Current caution

- the current `symmetry factor` is graph-theoretic `1/|Aut|` only
- if a later step needs the exact perturbative prefactor, the convention must be checked against:
  - Dyson expansion factors
  - identical-field combinatorics
  - normalization of the composite operator insertion

## Decoration-rule status

- file:
  - `calculation example/n1_sym_euclidean/11_q1__fpp_ewnabla_fpp__dr.md`
- exact one-sided generating result:
  - the `f_{++}e^{w\cdot\nabla_+}f_{++}` anomaly is fixed by the same `g^2` anomalous triangle pair as `Q_1(f_{++}f_{++})`
  - the DR local kernel is
    - `\Gamma_{12}(w) \propto \int_\Delta e^{i w\cdot(y p_1+(x+y)p_2)} (y p_1+(x+y)p_2)_{+\dot\beta}`
    - `\Gamma_{21}(w) \propto \int_\Delta e^{i w\cdot((x+y)p_1+y p_2)} ((x+y)p_1+y p_2)_{+\dot\beta}`
- local operator form:
  - the decoration acts by split-slot covariant differential operators
    - `e^{w\cdot(y\nabla^{(1)}+(x+y)\nabla^{(2)})}(y\nabla^{(1)}+(x+y)\nabla^{(2)})`
    - `e^{w\cdot((x+y)\nabla^{(1)}+y\nabla^{(2)})}((x+y)\nabla^{(1)}+y\nabla^{(2)})`
- topology interpretation:
  - the `g^2` six-class sector is the seed anomalous pair
  - the fully connected `g^3` and `g^4` sectors are the first two covariant-completion layers in the expansion of the split-slot operators above
  - no new one-loop anomaly coefficient appears beyond the seed triangle pair
- consistency check:
  - the linear `w` coefficient is
    - `-(i g^2)/(96\pi^2) [ \Xi_{12}\mathscr F_{12} + \Xi_{21}\mathscr F_{21} ]`
  - this is the coefficient extracted directly from the exact generating kernel
  - therefore the old simplification line `Q_1(f_{++}\nabla f_{++}) = i p\,Q_1(f_{++}f_{++})` should not be used as the decoration rule for the anomaly sector without an additional derivation
