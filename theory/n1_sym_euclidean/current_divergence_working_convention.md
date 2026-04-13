---
title: "N=1 SYM (Euclidean): current-divergence working convention"
doc_type: theory
theory: "N=1 SYM (Euclidean)"
status: working
---

# N=1 SYM (Euclidean): current-divergence working convention

## Current choice

对 `n1_sym_euclidean`，工作中统一采用 gauge-invariant FZ / Belinfante supercurrent。

Dirac 形式：

$$
S_\mu
=
-\frac{1}{2g_0}\,\sigma_{\rho\sigma}\gamma_\mu \psi^a F_{\rho\sigma}^a.
$$

Euclidean two-spinor 形式：

$$
J_{\mu\alpha}
=
-\frac{1}{2g_0}\,
F_{\rho\sigma}^a
\big(\sigma^{\rho\sigma}\sigma_\mu \bar\lambda^a\big)_\alpha.
$$

若 `conventions_and_rules.md` 中采用

$$
\delta \lambda_\alpha
=
c_f\,f_{\alpha\beta}\,\varepsilon^\beta+\cdots,
$$

则工作 current 的 relevant piece 固定为

$$
J_{\mu\alpha}^{(f\bar\lambda)}
=
c_f\,f_{\alpha\beta}^a(\sigma_\mu)^{\beta\dot\beta}\bar\lambda^a_{\dot\beta}.
$$

## \(Q_1\) projection

定义

$$
J^\mu_{Q_1}:=v_{Q_1}^\alpha J^\mu_\alpha,
$$

其中 \(v_{Q_1}^\alpha\) 取自 `conventions_and_rules.md` 中定义该 supercharge 时所用的同一 basis spinor。

工作插入统一取

$$
\boxed{
\partial_\mu J^\mu_{Q_1}
}.
$$

若只写 relevant piece，则

$$
\partial_\mu J^\mu_{Q_1}
=
-c_f\,\partial_\mu\!\left[
f_{Q_1,\beta}^a(\sigma^\mu)^{\beta\dot\beta}\bar\lambda^a_{\dot\beta}
\right].
$$

## Diagrammatic expansion

在 Wick contraction 前不代 EOM。

$$
F_{\rho\sigma}
=
\partial_\rho A_\sigma-\partial_\sigma A_\rho+[A_\rho,A_\sigma].
$$

因此必须同时保留

$$
J^{(2)}\sim (\partial A)\,\bar\lambda,
\qquad
J^{(3)}\sim [A,A]\,\bar\lambda.
$$

对 `Q_1(f_{++}f_{++})` 及其同族页面，1-loop 工作图统一来自：

$$
\text{(a) }J^{(2)}+\text{ ordinary SYM interaction vertex},
\qquad
\text{(b) }J^{(3)}+\text{ free contractions}.
$$

## Excluded insertions

以下对象不作为独立 anomaly-channel insertion：

$$
X_{\rm gf}+X_{c\bar c},
\qquad
X_{\rm Fierz},
\qquad
\partial^\nu U_{\nu\mu\alpha},
\qquad
\bar J_{\mu\dot\alpha}.
$$

对 `Q_1(f_{++}f_{++})` 这一族页面，off-shell auxiliary \(D\)-completion 也不作为独立 insertion 保留。

## Local extraction

局域 anomaly 统一按

$$
\text{local}
=
t^0(\cdots)-\Gamma_{\rm cl}
$$

抽取。

只有在 local part 写完之后，才对结果再做

$$
\text{EOM quotient},
\qquad
\text{BRST-exact quotient},
\qquad
\text{total-derivative quotient}.
$$

目标局域基底统一限制为：

$$
\text{gauge-invariant local operators built from }
f^{(+)}\text{ and }\bar\lambda,
$$

并匹配同一个 \(Q_1\) projection；含 ghost、\(D\)、或 anti-self-dual \(\bar f\) 的项丢弃。
