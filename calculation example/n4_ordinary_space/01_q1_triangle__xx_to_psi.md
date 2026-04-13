---
title: "Q_1 triangle seed: X_i X_j -> Psi^k"
doc_type: calculation
theory: "N=4 SYM ordinary-space"
loop_order: 1
supercharge: "Q_-^4"
status: seed_setup
---

# Q_1 triangle seed: \(X_iX_j\to\Psi^k\)

## Step 1: Operator / current / vertex

$$
\boxed{
Q_1:=Q_-^4.
}
$$

$$
\mathcal O_{ij}(y):=\operatorname{Tr}(X_iX_j)(y).
$$

$$
\mathfrak q_{1,\triangle}^{\rm raw}(X_i,X_j)=a_{\rm raw}\,\epsilon_{ijk}\Psi_{\rm raw}^k.
$$

$$
Q_1^{[1\to2]}\mathcal O_{ij}(y)=0.
$$

$$
J^\mu_{\psi{\rm -branch}}{}^{\rm raw}
=
\frac{\sqrt2}{g_{\rm YM}^2}
\Tr\!\left[
(\nabla_\nu X_i)(\sigma^\nu\bar\sigma^\mu\Psi^i)_-
\right].
$$

$$
J_{\psi{\rm -branch}}^{(2)\mu,\rm raw}
=
\frac{\sqrt2}{g_{\rm YM}^2}
\Tr\!\left[
(\partial_\nu X_i)(\sigma^\nu\bar\sigma^\mu\Psi^i)_-
\right],
$$

$$
J_{\psi{\rm -branch}}^{(3)\mu,\rm raw}
=
-\frac{i\sqrt2}{g_{\rm YM}^2}
\Tr\!\left[
[A_\nu,X_i](\sigma^\nu\bar\sigma^\mu\Psi^i)_-
\right].
$$

$$
V_{A X\bar X}.
$$

## Step 2: Triangle local remainder

$$
\partial_\mu J^\mu_{Q_1}(x)\cdot \mathcal O_{ij}(y)
\quad\leadsto\quad
\text{connected one-loop triangle local remainder}.
$$

$$
\big[\partial_\mu J^\mu_{Q_1}(x),\mathcal O_{ij}(y)\big]^{1\text{-loop}}_{\rm tri,loc}
=
-\delta^{(4)}(x-y)\,
\frac{g_{\rm YM}^2}{8\pi^2}\,
a_{\rm raw}\,\epsilon_{ijk}\operatorname{Tr}(\Psi_{\rm raw}^k)(y).
$$

## Step 3: Reduced coefficient form

$$
a_{\rm raw}
=
(\text{spinor factor})_{XX\to\Psi}
\times
(\text{color factor})_{XX\to\Psi}
\times
I_\triangle^{\rm loc}.
$$

$$
\Psi_{\rm raw}^k=-2i\,\Psi^k
\qquad\Longrightarrow\qquad
a=-2i\,a_{\rm raw}.
$$

## Step 4: To compute

$$
\boxed{
\text{input still needed for the explicit value of }a_{\rm raw}:
\text{ the raw propagator/projector contraction for }J_{\psi{\rm -branch}}^{\rm raw}\text{ with }V_{A X\bar X}.
}
$$
