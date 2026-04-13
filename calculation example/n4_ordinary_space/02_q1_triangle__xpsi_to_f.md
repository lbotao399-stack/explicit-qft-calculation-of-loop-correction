---
title: "Q_1 triangle seed: X_i Psi^j -> F"
doc_type: calculation
theory: "N=4 SYM ordinary-space"
loop_order: 1
supercharge: "Q_-^4"
status: seed_setup
---

# Q_1 triangle seed: \(X_i\Psi^j\to F\)

## Step 1: Operator / current / vertex

$$
\mathcal O_{i,{\rm raw}}{}^j(y):=\operatorname{Tr}(X_i\Psi_{\rm raw}^j)(y).
$$

$$
\mathfrak q_{1,\triangle}^{\rm raw}(X_i,\Psi_{\rm raw}^j)
=
b_{L,{\rm raw}}\,\delta_i^{\,j}F_{\rm raw}.
$$

$$
Q_1^{[1\to2]}\mathcal O_{i,{\rm raw}}{}^j(y)
=
\operatorname{Tr}\!\big(X_i\,Q_1\Psi_{\rm raw}^j\big)(y).
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
\langle \Lambda_+^a(z)\,\bar\Lambda_{\dot\beta}^{\,b}(x)\rangle_0
=
i\,g_{\rm YM}^2\,\delta^{ab}\,\partial_{+\dot\beta}\Delta(z-x).
$$

$$
V_{X\Lambda\Psi}.
$$

## Step 2: Triangle local remainder

$$
\partial_\mu J^\mu_{Q_1}(x)\cdot \mathcal O_{i,{\rm raw}}{}^j(y)
\quad\leadsto\quad
\text{connected one-loop triangle local remainder}.
$$

$$
\big[\partial_\mu J^\mu_{Q_1}(x),\mathcal O_{i,{\rm raw}}{}^j(y)\big]^{1\text{-loop}}_{\rm tri,loc}
=
-\delta^{(4)}(x-y)\,
\frac{g_{\rm YM}^2}{8\pi^2}\,
b_{L,{\rm raw}}\,\delta_i^{\,j}\operatorname{Tr}(F_{\rm raw})(y).
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
b_{L,{\rm raw}}
=
(\text{spinor factor})_{X\Psi\to F}
\times
(\text{color factor})_{X\Psi\to F}
\times
I_\triangle^{\rm loc}(x-y).
$$

$$
\Psi_{\rm raw}^j=-2i\,\Psi^j,
\qquad
F_{\rm raw}=-2\sqrt2 i\,F
\qquad\Longrightarrow\qquad
b_L=\frac{c_f}{c_\psi}\,b_{L,{\rm raw}}=\sqrt2\,b_{L,{\rm raw}}.
$$

## Step 4: To compute

$$
\boxed{
\text{remaining task: use the collapse }
\partial_\mu J_{F{\rm -branch},+}^{\mu,{\rm raw}}\to iF_{\rm raw}\delta^{(4)}
\text{ and evaluate the ordered raw Wick contraction with }V_{X\Lambda\Psi}
\text{ in the amputated correlator that uses a conjugate probe to receive }F_{\rm raw},
\text{ to read off }b_{L,{\rm raw}}.
}
$$
