---
title: "N=1 SYM (Euclidean): current-divergence working convention"
doc_type: theory
theory: "N=1 SYM (Euclidean)"
status: working
---

# N=1 SYM (Euclidean): current-divergence working convention

## Global alias

$$
\boxed{
Q_1\equiv Q_-
}.
$$

$$
\delta_{Q_1}=\delta_{Q_-},
\qquad
J^\mu_{Q_1}=J^\mu_-,
\qquad
\partial_\mu J^\mu_{Q_1}=\partial_\mu J^\mu_-.
$$

$$
Q_-=\left.Q_-^4\right|_{N=4\to N=1\text{ gauge truncation}}.
$$

$$
\delta_{Q_-}\Phi
:=
\delta_{\rm raw}\Phi\Big|_{\varepsilon^-=1,\ \varepsilon^+=0,\ \bar\varepsilon^{\dot\pm}=0}.
$$

$$
Q_-^2=0,
\qquad
\{Q_-,\bar Q_{\dot\alpha}\}=2\,\sigma^\mu_{-\dot\alpha}P_\mu.
$$

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
J^\mu_-:=v_-^\alpha J^\mu_\alpha.
$$

$$
\boxed{
J^\mu_-\equiv \big(J_{\mu\alpha}^{\rm rel}\big)\text{ 对应 }Q_-\text{ 的那一支}
}.
$$

$$
J^\mu_-=
C_J\Big(f_{+-}\Xi^{\mu +}+f_{--}\Xi^{\mu -}\Big).
$$

## Unified coefficient

$$
\nabla_{\alpha\dot\alpha}:=D_{\alpha\dot\alpha}.
$$

$$
\delta_{Q_-}^{\rm cl}A_{+\dot\alpha}=\kappa_A\,\bar\lambda_{\dot\alpha},
\qquad
\delta_{Q_-}^{\rm cl}A_{-\dot\alpha}=0,
\qquad
\delta_{Q_-}^{\rm cl}\bar\lambda_{\dot\alpha}=0.
$$

$$
\delta_{Q_-}^{\rm cl}f_{++}=2\kappa_A\,\nabla_{+\dot\beta}\bar\lambda^{\dot\beta}.
$$

$$
\boxed{
\kappa_A:=\frac12\,\text{coeff}\Big(\delta_{Q_-}^{\rm cl}f_{++},\ \nabla_{+\dot\beta}\bar\lambda^{\dot\beta}\Big)
\qquad\Longrightarrow\qquad
\kappa_A=\frac{i}{2}
}
$$

$$
Q_-\,\operatorname{Tr}(f_{++}f_{++})
=
4\,\kappa_A\,\operatorname{Tr}\!\big(f_{++}\nabla_{+\dot\beta}\bar\lambda^{\dot\beta}\big).
$$

## Exact commutators with \(\nabla\)

$$
[\delta_{Q_-}^{\rm cl},\nabla_{\alpha\dot\alpha}]X
=
\operatorname{ad}_{\delta_{Q_-}^{\rm cl}A_{\alpha\dot\alpha}}X,
\qquad
\operatorname{ad}_Y(X)^a:=f^{abc}Y^bX^c.
$$

$$
[\delta_{Q_-}^{\rm cl},\nabla_{+\dot\alpha}]
=
\kappa_A\,\operatorname{ad}_{\bar\lambda_{\dot\alpha}},
\qquad
[\delta_{Q_-}^{\rm cl},\nabla_{-\dot\alpha}]=0.
$$

$$
\delta_{Q_-}^{\rm cl}(\nabla_{+\dot\alpha}X)
=
\nabla_{+\dot\alpha}(\delta_{Q_-}^{\rm cl}X)
+
\kappa_A\,\operatorname{ad}_{\bar\lambda_{\dot\alpha}}X,
$$

$$
\delta_{Q_-}^{\rm cl}(\nabla_{-\dot\alpha}X)
=
\nabla_{-\dot\alpha}(\delta_{Q_-}^{\rm cl}X).
$$

$$
\delta_{Q_-}^{\rm cl}\!\left(
\nabla_{+\dot\alpha_1}\cdots\nabla_{+\dot\alpha_n}X
\right)
=
\nabla_{+\dot\alpha_1}\cdots\nabla_{+\dot\alpha_n}(\delta_{Q_-}^{\rm cl}X)
+
\kappa_A
\sum_{k=1}^{n}
\nabla_{+\dot\alpha_1}\cdots\nabla_{+\dot\alpha_{k-1}}
\operatorname{ad}_{\bar\lambda_{\dot\alpha_k}}
\nabla_{+\dot\alpha_{k+1}}\cdots\nabla_{+\dot\alpha_n}X.
$$

## Direct slot formulas

$$
\delta_{Q_-}^{\rm cl}(\nabla_{+\dot\alpha}f_{++})
=
2\kappa_A\,\nabla_{+\dot\alpha}\nabla_{+\dot\beta}\bar\lambda^{\dot\beta}
+
\kappa_A\,\operatorname{ad}_{\bar\lambda_{\dot\alpha}}f_{++},
$$

$$
\delta_{Q_-}^{\rm cl}(\nabla_{-\dot\alpha}f_{++})
=
2\kappa_A\,\nabla_{-\dot\alpha}\nabla_{+\dot\beta}\bar\lambda^{\dot\beta},
$$

$$
\delta_{Q_-}^{\rm cl}(\nabla_{+\dot\alpha}\bar\lambda_{\dot\beta})
=
\kappa_A\,\operatorname{ad}_{\bar\lambda_{\dot\alpha}}\bar\lambda_{\dot\beta},
\qquad
\delta_{Q_-}^{\rm cl}(\nabla_{-\dot\alpha}\bar\lambda_{\dot\beta})=0.
$$

## Exact rule for \(e^{w\cdot\nabla_+}\)

$$
B_+(w):=w^{\dot\alpha}\nabla_{+\dot\alpha},
\qquad
[\delta_{Q_-}^{\rm cl},B_+(w)]
=
\kappa_A\,w^{\dot\alpha}\operatorname{ad}_{\bar\lambda_{\dot\alpha}}.
$$

$$
\delta_{Q_-}^{\rm cl}e^{B_+}
=
\int_0^1 ds\;
e^{sB_+}\,[\delta_{Q_-}^{\rm cl},B_+]\,e^{(1-s)B_+}.
$$

$$
\delta_{Q_-}^{\rm cl}\!\big(e^{w\cdot\nabla_+}X\big)
=
e^{w\cdot\nabla_+}\big(\delta_{Q_-}^{\rm cl}X\big)
+
\kappa_A
\int_0^1 ds\;
e^{s w\cdot\nabla_+}
\Big(
w^{\dot\alpha}\operatorname{ad}_{\bar\lambda_{\dot\alpha}}
\Big)
e^{(1-s) w\cdot\nabla_+}X.
$$

$$
\delta_{Q_-}^{\rm cl}\!\big(e^{w\cdot\nabla_+}f_{++}\big)
=
2\kappa_A\,e^{w\cdot\nabla_+}\nabla_{+\dot\beta}\bar\lambda^{\dot\beta}
+
\kappa_A
\int_0^1 ds\;
e^{s w\cdot\nabla_+}
\Big(
w^{\dot\alpha}\operatorname{ad}_{\bar\lambda_{\dot\alpha}}
\Big)
e^{(1-s) w\cdot\nabla_+}f_{++},
$$

$$
\delta_{Q_-}^{\rm cl}\!\big(e^{w\cdot\nabla_+}\bar\lambda_{\dot\beta}\big)
=
\kappa_A
\int_0^1 ds\;
e^{s w\cdot\nabla_+}
\Big(
w^{\dot\alpha}\operatorname{ad}_{\bar\lambda_{\dot\alpha}}
\Big)
e^{(1-s) w\cdot\nabla_+}\bar\lambda_{\dot\beta}.
$$

## Divergence rule

$$
\big\langle \partial_\mu J^\mu_-(x),\mathcal O(y_1)\cdots \mathcal O(y_n)\big\rangle
=
-\sum_i \delta(x-y_i)\,
\big\langle \delta_{Q_-}^{\rm cl}\mathcal O_i(y_i)\prod_{j\neq i}\mathcal O_j(y_j)\big\rangle.
$$

$$
\boxed{
\partial_\mu J^\mu_-\ \text{acts only by WT contact terms}
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
\langle f_{\alpha\beta}^a(x)\,f_{\gamma\delta}^b(y)\rangle_0
=
\delta^{ab}\,K(x-y)\,
\Big(\epsilon_{\alpha\gamma}\epsilon_{\beta\delta}
+\epsilon_{\alpha\delta}\epsilon_{\beta\gamma}\Big).
$$

$$
\langle f_{++}(x)f_{++}(y)\rangle_0=0,
\qquad
\langle f_{+-}(x)f_{++}(y)\rangle_0=0,
\qquad
\langle f_{--}(x)f_{++}(y)\rangle_0=2\,K(x-y).
$$

$$
\boxed{
\text{only the }f_{--}\Xi^{\mu -}\text{ branch of }J^\mu_-\text{ can feed into an external }f_{++}
}.
$$

$$
\partial_\mu J^\mu_-(x)\cdot f_{++}(y).
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
\delta_{Q_-}^{\rm cl}f_{++}
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
