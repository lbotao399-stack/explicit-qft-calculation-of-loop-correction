---
title: "N=1 General: supercurrent and Konishi channel"
doc_type: theory
theory: "N=1 General"
status: canonical
---

# N=1 General: supercurrent and Konishi channel

## Canonical \(N=1\) action

Chiral multiplets

$$
(\phi^i,\psi^i_\alpha,F^i),
$$

vector multiplets

$$
(A_\mu^a,\lambda_\alpha^a,\bar\lambda_{\dot\alpha}^a,D^a),
$$

superpotential

$$
W(\phi),
\qquad
W_i:=\frac{\partial W}{\partial\phi^i},
\qquad
W_{ij}:=\frac{\partial^2 W}{\partial\phi^i\partial\phi^j}.
$$

$$
\begin{aligned}
\mathcal L
={}&
\nabla_\mu\phi_i^\dagger\nabla^\mu\phi^i
+i\bar\psi_i\bar\sigma^\mu\nabla_\mu\psi^i
+F_i^\dagger F^i
+\frac14 F_{\mu\nu}^aF_{\mu\nu}^a
+i\bar\lambda^a\bar\sigma^\mu D_\mu\lambda^a
+\frac12 D^aD^a
\\
&-\sqrt2 g\Big(
\phi_i^\dagger(T^a)^i{}_j\lambda^a\psi^j
+\bar\psi_i\bar\lambda^a(T^a)^i{}_j\phi^j
\Big)
+gD^a\phi_i^\dagger(T^a)^i{}_j\phi^j
\\
&+F^iW_i+F_i^\dagger\bar W^i
-\frac12 W_{ij}\psi^i\psi^j
-\frac12\bar W^{ij}\bar\psi_i\bar\psi_j.
\end{aligned}
$$

## Off-shell SUSY transformations

$$
\delta\phi^i=\sqrt2\,\eta\psi^i,
\qquad
\delta\phi_i^\dagger=\sqrt2\,\bar\eta\bar\psi_i,
$$

$$
\delta\psi_\alpha^i
=
i\sqrt2\,(\sigma^\mu\bar\eta)_\alpha\nabla_\mu\phi^i
+\sqrt2\,\eta_\alpha F^i,
$$

$$
\delta\bar\psi_i^{\dot\alpha}
=
-i\sqrt2\,(\eta\sigma^\mu)^{\dot\alpha}\nabla_\mu\phi_i^\dagger
+\sqrt2\,\bar\eta^{\dot\alpha}F_i^\dagger,
$$

$$
\delta A_\mu^a=i\eta\sigma_\mu\bar\lambda^a-i\lambda^a\sigma_\mu\bar\eta,
$$

$$
\delta\lambda_\alpha^a=(\sigma^{\mu\nu}\eta)_\alpha F_{\mu\nu}^a+i\eta_\alpha D^a,
\qquad
\delta\bar\lambda^{a\dot\alpha}=(\bar\sigma^{\mu\nu}\bar\eta)^{\dot\alpha}F_{\mu\nu}^a-i\bar\eta^{\dot\alpha}D^a.
$$

## Canonical Noether supercurrent

$$
\boxed{
J^\mu_\alpha
=
\sqrt2\,(\sigma^\nu\bar\sigma^\mu\psi_i)_\alpha\nabla_\nu\phi_i^\dagger
+i\sqrt2\,(\sigma^\mu\bar\psi_i)_\alpha F_i^\dagger
-iF_{\rho\nu}^a(\sigma^{\rho\nu}\sigma^\mu\bar\lambda^a)_\alpha
+iD^a(\sigma^\mu\bar\lambda^a)_\alpha
}
$$

$$
F_i^\dagger=-\bar W_i,
\qquad
D^a=-g\phi_i^\dagger(T^a)^i{}_j\phi^j.
$$

## \(Q_-\) component and Konishi channel

$$
Q_-:=Q_\alpha\big|_{\alpha=-},
\qquad
K_+(x):=\frac1{\sqrt2}\,\psi_+(x)\phi^\dagger(x).
$$

$$
Q_-\phi^i=\sqrt2\,\psi_-^i,
\qquad
Q_-\phi_i^\dagger=0,
$$

$$
Q_-\psi_+^i=\sqrt2\,F^i,
\qquad
Q_-\bar\psi_{i\dot\alpha}=i\sqrt2\,\nabla_{-\dot\alpha}\phi_i^\dagger,
$$

$$
Q_-A_{\alpha\dot\alpha}=i\delta_{\alpha-}\bar\lambda_{\dot\alpha},
\qquad
Q_-\bar\lambda_{\dot\alpha}=0,
$$

$$
Q_-\lambda_\alpha=(\sigma^{\mu\nu})_\alpha{}^-F_{\mu\nu}+i\delta_{\alpha-}D.
$$

## \(U(1)\), one-chiral, \(W=0\) Konishi route

$$
D=-g\phi^\dagger\phi,
\qquad
J_-^\mu\supset iD(\sigma^\mu\bar\lambda)_-
=-ig\,\phi^\dagger\phi\,(\sigma^\mu\bar\lambda)_-.
$$

$$
\partial_\mu J_-^\mu
\supset
-ig\,(\partial_{-\dot\alpha}\phi^\dagger)\phi\,\bar\lambda^{\dot\alpha}
-ig\,\phi^\dagger(\partial_{-\dot\alpha}\phi)\bar\lambda^{\dot\alpha}
-ig\,\phi^\dagger\phi\,\partial_{-\dot\alpha}\bar\lambda^{\dot\alpha}.
$$

$$
V_{\bar\lambda}
=
-\sqrt2 g\int d^d z\,\bar\psi_{\dot\beta}(z)\bar\lambda^{\dot\beta}(z)\phi(z).
$$

$$
\langle\phi(k)\phi^\dagger(-k)\rangle=\frac1{k^2},
\qquad
\langle\psi_\alpha(k)\bar\psi_{\dot\beta}(-k)\rangle=\frac{k_{\alpha\dot\beta}}{k^2}.
$$

$$
\int d^d y\,e^{-iq\cdot y}\,\partial_\mu J_-^\mu(y)\,K_+(p)
\quad\Longrightarrow\quad
\text{local contact term at }q\to0.
$$
