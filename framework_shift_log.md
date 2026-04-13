# framework shift log

## 2026-04-12

- repository `lbotao399-stack/explicit-qft-calculation-of-loop-correction` 已切为 public。
- project 主计算口径从 “raw \(Q_{\rm bare}-Q_0\) 逐字母代入” 固定为
  - susy current diagram
  - anomaly Ward identity
  - local-term extraction
- `n1_general` 的 Konishi 页已作为 current-divergence 模板保留。
- `n1_sym_euclidean` 当前工作约定固定为：
  - `Q_1 \equiv Q_-`，不做新的 basis / rescaling / phase；
  - current 取 properly-normalized canonical / WZ-gauge supercurrent；
  - current 的 \(f\bar\lambda\) 系数与 raw SUSY 中 \(\delta\lambda=c_f f\varepsilon+\cdots\) 的 \(c_f\) 做 coefficient matching；
  - 工作插入统一取 \(\partial_\mu J^\mu_-\)；
  - current vertex 必须同时展开为 \(J^{(2)}\sim (\partial A)\bar\lambda\) 与 \(J^{(3)}\sim [A,A]\bar\lambda\)；
  - `f` propagator 的 spinor selection rule 固定为只有 `f_{--}` 支能直接 contract 到 external `f_{++}`；
  - pure SYM 的这组页面不再把 \(\partial_\mu J^\mu\) 读成独立 anomaly channel；
  - `Q_1(f_{++}f_{++})` 页面只要求短程 contraction 重建 classical covariant variation；
  - 在该 channel 中一致性条件固定为 \(t^0(\cdots)-\Gamma_{\rm cl}=0\)。
- `n1_sym_euclidean` 暂不把以下对象作为独立 anomaly-channel insertion：
  - \(X_{\rm gf}+X_{c\bar c}\)
  - \(X_{\rm Fierz}\)
  - improvement terms
  - conjugate current \(\bar J\)
  - 对 `Q_1(f_{++}f_{++})` 这一族页面的 auxiliary \(D\)-piece
- 下一步：
  - `Q_1(f_{++}f_{++}) / DR` 已改成 pure-SYM divergence consistency page
  - 下一步继续把同族 `n1_sym_euclidean` 计算页依次迁成 current-divergence 版 Step 2 / Step 3 / Step 4
- 同日补充完成：
  - `01/02/04/05/06/07/08/09/10/11` 已全部迁成 `Q_-` 显式投影 + current-piece selection + WT contact reconstruction 版；
  - 对带 `\nabla` 与 `e^{w\cdot\nabla_+}` 的 slot，当前页面统一保留 `\delta_{Q_-}^{\rm cl}` 的 active-slot 记法，不在页面内额外展开 `[\delta_{Q_-},\nabla]` 的树项；
  - `03_q1__fpp_fpp__dr.md` 继续作为 pure-SYM divergence consistency 的基准页。
