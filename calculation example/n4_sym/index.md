# N=4 SYM calculation index

当前这一桶下已经放入三份 `N=4 SYM` 的显式算例，全部来自你最新补充的 working notes。

它们都带有：

- `theory: N=4 SYM`
- `loop_order: 1`

再按 `regularization`、`operator`、以及是否是 generating-kernel 版本区分。

## Current files

1. `01_q1__fpp_fpp__pv.md`
   - `Q_1(O)（f_{++}f_{++}） / PV`
   - corrected `w=0` 结果，明确保留 gauge / matter triangles 两部分。
2. `02_q1__fpp_ewnabla_fpp__pv.md`
   - `Q_1(O)（f_{++}e^{w\nabla}f_{++}） / PV`
   - exact $(w)$-generating one-loop local anomaly。
3. `03_q1__fpp_ewnabla_fpp__dr.md`
   - `Q_1(O)（f_{++}e^{w\nabla}f_{++}） / DR`
   - DR / DRED-style 重算版本。
