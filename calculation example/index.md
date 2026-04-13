# calculation example index

当前目录采用“先按理论分桶，再在桶内按一个具体计算一个文件组织”的方式。

## 标题规范

每个具体计算文件的页内标题统一采用：

`Q_1(O)（算符内容） / DR`

或

`Q_1(O)（算符内容） / PV`

文件名本身为了兼容路径与检索，使用 ASCII 简写；真正的标准标题写在文件首行。每个文件同时带有 front matter 属性，其中最关键的是 `theory`。

## 理论分桶

- `n1_sym_euclidean/`
  - 当前全部显式算例都在这里。
- `n1_general/`
  - 一般 `N=1` 理论的显式算例，当前已加入 Konishi anomaly 的 DR current-diagram 版本。
- `n4_sym/`
  - 已加入 `N=4 SYM` 的 `Q_1(f_{++}f_{++})` 及其 generating-kernel PV / DR 笔记。
- `archive/grouped_archive/`
  - 旧的主题打包稿，只作归档与对照。

## 当前算例

### N=1 General

1. `n1_general/01_q1__psi_plus_phidag__dr.md`
   - `Q_1(O)（\frac{1}{\sqrt2}\psi_+\phi^\dagger） / DR`

### N=1 SYM (Euclidean)

1. `n1_sym_euclidean/01_q1__fpp_barlambda__dr.md`
   - `Q_1(O)（f_{++}\bar\lambda_{\dot\alpha}） / DR`
2. `n1_sym_euclidean/02_q1__fpp_barlambda__pv.md`
   - `Q_1(O)（f_{++}\bar\lambda_{\dot\alpha}） / PV`
3. `n1_sym_euclidean/03_q1__fpp_fpp__dr.md`
   - `Q_1(O)（f_{++}f_{++}） / DR`
4. `n1_sym_euclidean/04_q1__fpp_nabla_barlambda__pv.md`
   - `Q_1(O)（f_{++}\nabla_{+\dot\gamma}\bar\lambda_{\dot\alpha}） / PV`
5. `n1_sym_euclidean/05_q1__nabla_fpp__fpp__pv.md`
   - `Q_1(O)（(\nabla_{+\dot\alpha}f_{++})f_{++}） / PV`
6. `n1_sym_euclidean/06_q1__nabla_fpp__barlambda__pv.md`
   - `Q_1(O)（(\nabla_{+\dot\alpha}f_{++})\bar\lambda_{\dot\beta}） / PV`
7. `n1_sym_euclidean/07_q1__nabla_fpp__nabla_barlambda__pv.md`
   - `Q_1(O)（(\nabla_{+\dot\alpha}f_{++})\nabla_{+\dot\beta}\bar\lambda_{\dot\gamma}） / PV`
8. `n1_sym_euclidean/08_q1__fpp_ewnabla_fpp__pv.md`
   - `Q_1(O)（f_{++}e^{w\nabla}f_{++}） / PV`
9. `n1_sym_euclidean/09_q1__ewnabla_fpp__fpp__pv.md`
   - `Q_1(O)（e^{w\nabla}f_{++}f_{++}） / PV`
10. `n1_sym_euclidean/10_q1__fpp_ewnabla_barlambda__pv.md`
    - `Q_1(O)（f_{++}e^{w\nabla}\bar\lambda_{\dot\beta}） / PV`

### N=4 SYM

1. `n4_sym/01_q1__fpp_fpp__pv.md`
   - `Q_1(O)（f_{++}f_{++}） / PV`
2. `n4_sym/02_q1__fpp_ewnabla_fpp__pv.md`
   - `Q_1(O)（f_{++}e^{w\nabla}f_{++}） / PV`
3. `n4_sym/03_q1__fpp_ewnabla_fpp__dr.md`
   - `Q_1(O)（f_{++}e^{w\nabla}f_{++}） / DR`

## 归档

此前按主题打包的三份合集稿保留在 `archive/grouped_archive/`，只作为归档与对照，不再作为主入口。
