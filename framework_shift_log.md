# framework shift log

## 2026-04-12

- repository `lbotao399-stack/explicit-qft-calculation-of-loop-correction` 已切为 public。
- project 主计算口径从 “raw \(Q_{\rm bare}-Q_0\) 逐字母代入” 固定为
  - susy current diagram
  - anomaly Ward identity
  - local-term extraction
- `n1_general` 的 Konishi 页已作为 current-divergence 模板保留。
- `n1_sym_euclidean` 当前工作约定固定为：
  - current 取 gauge-invariant FZ / Belinfante supercurrent；
  - current 的 \(f\bar\lambda\) 系数与 raw SUSY 中 \(\delta\lambda=c_f f\varepsilon+\cdots\) 的 \(c_f\) 做 coefficient matching；
  - 工作插入统一取 \(\partial_\mu J^\mu_{Q_1}\)；
  - current vertex 必须同时展开为 \(J^{(2)}\sim (\partial A)\bar\lambda\) 与 \(J^{(3)}\sim [A,A]\bar\lambda\)；
  - local anomaly 统一按 \(t^0(\cdots)-\Gamma_{\rm cl}\) 提取。
- `n1_sym_euclidean` 暂不把以下对象作为独立 anomaly-channel insertion：
  - \(X_{\rm gf}+X_{c\bar c}\)
  - \(X_{\rm Fierz}\)
  - improvement terms
  - conjugate current \(\bar J\)
  - 对 `Q_1(f_{++}f_{++})` 这一族页面的 auxiliary \(D\)-piece
- 下一步：
  - 先重写 `Q_1(f_{++}f_{++}) / DR`
  - 再把同族 `n1_sym_euclidean` 计算页依次迁成 current-divergence 版 Step 2 / Step 3 / Step 4
