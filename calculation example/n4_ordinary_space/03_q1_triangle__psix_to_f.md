---
title: "Q_1 triangle seed: Psi^j X_i -> F"
doc_type: calculation
theory: "N=4 SYM ordinary-space"
loop_order: 1
supercharge: "Q_-^4"
status: seed_setup
---

# Q_1 triangle seed: \(\Psi^jX_i\to F\)

## Step 1: Operator / current / vertex

$$
\widetilde{\mathcal O}_{\rm raw}^j{}_i(y):=\operatorname{Tr}(\Psi_{\rm raw}^jX_i)(y).
$$

$$
\mathfrak q_{1,\triangle}^{\rm raw}(\Psi_{\rm raw}^j,X_i)
=
b_{R,{\rm raw}}\,\delta_i^{\,j}F_{\rm raw}.
$$

$$
J^\mu_{F{\rm -branch},+}{}^{\rm raw}
=
-\frac1{g_{\rm YM}^2}
\Tr\!\left[
f^{\rm raw}_{+\beta}\,
\sigma^{\mu\,\beta\dot\beta}\bar\Lambda_{\dot\beta}
\right].
$$

$$
V_{X\Lambda\Psi},
\qquad
\text{external ordering reversed relative to }X_i\Psi^j\to F.
$$

## Step 2: Triangle local remainder

$$
\partial_\mu J^\mu_{Q_1}(x)\cdot \widetilde{\mathcal O}_{\rm raw}^j{}_i(y)
\quad\leadsto\quad
\text{connected one-loop triangle local remainder}.
$$

$$
\big[\partial_\mu J^\mu_{Q_1}(x),\widetilde{\mathcal O}_{\rm raw}^j{}_i(y)\big]^{1\text{-loop}}_{\rm tri,loc}
=
-\delta^{(4)}(x-y)\,
\frac{g_{\rm YM}^2}{8\pi^2}\,
b_{R,{\rm raw}}\,\delta_i^{\,j}\operatorname{Tr}(F_{\rm raw})(y).
$$

Operational local collapse:
$$
\partial_\mu^x
J_{F{\rm -branch},+}^{\mu,{\rm raw}}(x)
\quad
\xrightarrow[\langle \bar\Lambda\,\Lambda_+\rangle_0]{{\rm local}}
\quad
i\,F_{\rm raw}(x)\,\delta^{(4)}(x-z).
$$

## Step 3: Reduced coefficient form

$$
b_{R,{\rm raw}}
=
(\text{spinor factor})_{\Psi X\to F}
\times
(\text{color factor})_{\Psi X\to F}
\times
I_\triangle^{\rm loc}(x-y).
$$

$$
b_R=\frac{c_f}{c_\psi}\,b_{R,{\rm raw}}=\sqrt2\,b_{R,{\rm raw}}.
$$

## Step 4: To compute

$$
\boxed{
\text{remaining task: use the collapse }
\partial_\mu J_{F{\rm -branch},+}^{\mu,{\rm raw}}\to iF_{\rm raw}\delta^{(4)}
\text{ and evaluate the reversed ordered raw Wick contraction with }V_{X\Lambda\Psi}
\text{ in the amputated correlator that uses a conjugate probe to receive }F_{\rm raw},
\text{ to read off }b_{R,{\rm raw}}.
}
$$
