---
title: "N=1 SYM (Euclidean): current-divergence working convention"
doc_type: theory
theory: "N=1 SYM (Euclidean)"
status: working
---

# N=1 SYM (Euclidean): current-divergence working convention

## Current choice

$$
S_\mu^{\rm adopt}
=
-\frac{1}{2g_0}\,\sigma_{\rho\sigma}\gamma_\mu\,\psi^a\,F_{\rho\sigma}^a.
$$

$$
J_{\alpha\dot\alpha}^{\rm FZ}
=
-\frac{4}{g^2}\,\operatorname{Tr}\!\big(e^V W_\alpha e^{-V}\bar W_{\dot\alpha}\big).
$$

$$
W_\alpha
=
-i\Big(
\lambda_\alpha+i\theta_\alpha D+\theta^\beta f_{\alpha\beta}
+i\theta^2 D_{\alpha\dot\alpha}\bar\lambda^{\dot\alpha}
\Big).
$$

## Euclidean / Weyl decomposition

$$
J_{\mu\alpha}
=
-\frac{1}{2g_0}\,
\big(\sigma^{\rho\sigma}\sigma_\mu\bar\lambda^a\big)_\alpha
F_{\rho\sigma}^a,
\qquad
\bar J_{\mu\dot\alpha}
=
-\frac{1}{2g_0}\,
\big(\bar\sigma^{\rho\sigma}\bar\sigma_\mu\lambda^a\big)_{\dot\alpha}
F_{\rho\sigma}^a.
$$

$$
F_{\mu\nu}(\sigma^{\mu\nu})_{\alpha\beta}=c_f\,f_{\alpha\beta},
\qquad
F_{\mu\nu}(\bar\sigma^{\mu\nu})_{\dot\alpha\dot\beta}=c_{\bar f}\,\bar f_{\dot\alpha\dot\beta}.
$$

$$
J_{\mu\alpha}^{\rm rel}
=
-\frac{c_f}{2g_0}\,
f_{\alpha\beta}^a\,\sigma_\mu^{\beta\dot\beta}\bar\lambda_{\dot\beta}^a,
\qquad
\bar J_{\mu\dot\alpha}^{\rm rel}
=
-\frac{c_{\bar f}}{2g_0}\,
\bar f_{\dot\alpha\dot\beta}^a\,\bar\sigma_\mu^{\dot\beta\beta}\lambda_\beta^a.
$$

$$
\delta\lambda_\alpha
=
c_f\,f_{\alpha\beta}\,\varepsilon^\beta+\cdots
\quad\Longrightarrow\quad
J_{\mu\alpha}^{\rm rel}\ \text{取同一个 }c_f.
$$

## \(Q_1\) projection

$$
J^\mu_{Q_1}:=v_{Q_1}^\alpha J^\mu_\alpha.
$$

$$
\boxed{
J^\mu_{Q_1}\equiv \big(J_{\mu\alpha}^{\rm rel}\big)\text{ 对应 }Q_1\text{ 的那一支}
}.
$$

## Divergence rule

$$
\big\langle \partial_\mu J^\mu_{Q_1}(x),\mathcal O(y_1)\cdots \mathcal O(y_n)\big\rangle
=
-\sum_i \delta(x-y_i)\,
\big\langle \delta_{Q_1}^{\rm cl}\mathcal O_i(y_i)\prod_{j\neq i}\mathcal O_j(y_j)\big\rangle.
$$

$$
\boxed{
\partial_\mu J^\mu_{Q_1}\ \text{acts only by WT contact terms}
}.
$$

$$
\boxed{
\text{no separate pure-SYM divergence anomaly insertion}
}.
$$

## Diagrammatic prescription

$$
F_{\rho\sigma}
=
\partial_\rho A_\sigma-\partial_\sigma A_\rho+[A_\rho,A_\sigma].
$$

$$
J^{(2)}\sim (\partial A)\bar\lambda,
\qquad
J^{(3)}\sim [A,A]\bar\lambda.
$$

$$
\partial_\mu J^\mu_{Q_1}(x)\cdot f_{++}(y).
$$

$$
F_{\mu\nu}(x)\big|_{\rm lin}\ \text{with}\ f_{++}(y)\big|_{\rm lin}
\Longrightarrow
\partial\bar\lambda\ \text{contact term},
$$

$$
F_{\mu\nu}(x)\big|_{\rm lin}\ \text{with}\ f_{++}(y)\big|_{\rm quad}
\Longrightarrow
[A,\bar\lambda]\ \text{contact term},
$$

$$
F_{\mu\nu}(x)\big|_{\rm quad}\ \text{with}\ f_{++}(y)\big|_{\rm lin}
\Longrightarrow
[A,\bar\lambda]\ \text{contact term}.
$$

$$
\partial\bar\lambda+[A,\bar\lambda]=D\bar\lambda.
$$

## Local consistency condition

$$
t^0(\cdots)-\Gamma_{\rm cl}=0.
$$

$$
\boxed{
\text{the short-distance contraction only reconstructs }
\delta_{Q_1}^{\rm cl}f_{++}
}.
$$

## Excluded insertions

$$
X_{\rm gf},
\qquad
X_{c\bar c},
\qquad
X_{\rm Fierz},
\qquad
\partial_\nu U^{[\mu\nu]},
\qquad
\bar J_{\mu\dot\alpha}.
$$

$$
\text{auxiliary }D\text{-piece after }D\text{ elimination}
$$

## Relevant anomaly channel

$$
\gamma_\mu S^\mu_{\rm R}(x)
=
-\frac{3\,C_2(G)\,g}{(4\pi)^2}\,
\sigma_{\mu\nu}\psi^a(x)F_{\nu\mu}^a(x)
+\mathcal O(g^3).
$$

$$
\boxed{
\text{gamma-trace anomaly is not inserted into the }\partial_\mu J^\mu\text{ pages}
}.
$$
