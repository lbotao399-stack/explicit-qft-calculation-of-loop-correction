---
title: "Q_1 triangle seed: X_i X_j -> Psi^k"
doc_type: calculation
theory: "N=4 SYM ordinary-space"
loop_order: 1
supercharge: "Q_-^4"
status: seed_setup
---

# Q_1 triangle seed: \(X_iX_j\to\Psi^k\)

## Step 1: Ordered input / current / vertex / probe

$$
\boxed{
Q_1:=Q_-^4.
}
$$

$$
\mathcal O_{ij}(y_1,y_2):=X_i(y_1)X_j(y_2),
\qquad
y_1\to y,\ y_2\to y\ \text{only at the end}.
$$

$$
\mathfrak q_{1,\triangle}^{\rm raw}(X_i,X_j)=a_{\rm raw}\,\epsilon_{ijk}\Psi_{\rm raw}^k.
$$

$$
Q_1^{[1\to2]}(X_iX_j)=0.
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

$$
\mathbb P_{\Psi,k}(z)
:=
-\frac{i}{g_{\rm YM}^2}\,
\partial_z^{+\dot\alpha}\bar\Psi_{k\dot\alpha}(z),
\qquad
\langle \Psi_+^{i\,a}(y)\,\mathbb P_{\Psi,k}^{\,b}(z)\rangle_0
=
\delta^i_k\,\delta^{ab}\,\delta^{(4)}(y-z).
$$

## Step 2: Probe-amputated local correlator

$$
\mathcal G_{ij|k}(x;y_1,y_2;z)
:=
\left\langle
\big[\partial_\mu J^\mu_{Q_1}(x)\,X_i(y_1)X_j(y_2)\big]^{1\text{-loop}}_{\rm conn,loc}
\,
\mathbb P_{\Psi,k}(z)
\right\rangle_0.
$$

ordered limit \(y_1,y_2\to y\):
$$
\boxed{
\mathcal G_{ij|k}(x;y,z)
=
-\frac{g_{\rm YM}^2}{8\pi^2}\,
a_{\rm raw}\,
\epsilon_{ijk}\,
\delta^{(4)}(x-y)\,
\delta^{(4)}(y-z).
}
$$

$$
Q_1^{[1\to2]}(X_iX_j)=0
\qquad\Longrightarrow\qquad
\text{this seed has no tree contamination.}
$$

## Step 3: Reduced coefficient form

$$
a_{\rm raw}
=
(\text{spinor factor})_{XX\to\Psi}
\times
(\text{color factor})_{XX\to\Psi}
\times
I_\triangle^{\rm loc}(x-y).
$$

$$
a=-2i\,a_{\rm raw}.
$$

## Step 4: To compute

$$
\boxed{
\text{remaining task: evaluate }
\mathcal G_{ij|k}
\text{ by the ordered raw Wick contraction of }
J_{\psi{\rm -branch}}^{(2,3)\mu,\rm raw}
\text{ with }V_{A X\bar X}
\text{ and the amputated probe }\mathbb P_{\Psi,k},
\text{ then read off }a_{\rm raw}.
}
$$
