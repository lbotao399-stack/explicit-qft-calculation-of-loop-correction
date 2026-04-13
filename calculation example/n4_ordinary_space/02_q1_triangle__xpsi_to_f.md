---
title: "Q_1 triangle seed: X_i Psi^j -> F"
doc_type: calculation
theory: "N=4 SYM ordinary-space"
loop_order: 1
supercharge: "Q_-^4"
status: seed_setup
---

# Q_1 triangle seed: \(X_i\Psi^j\to F\)

## Step 1: Ordered input / current / vertex / probe

$$
\mathcal O_{i,{\rm raw}}{}^j(y_1,y_2):=X_i(y_1)\Psi^j_+(y_2),
\qquad
y_1\to y,\ y_2\to y\ \text{only at the end}.
$$

$$
\mathfrak q_{1,\triangle}^{\rm raw}(X_i,\Psi_{\rm raw}^j)
=
b_{L,{\rm raw}}\,\delta_i^{\,j}F_{\rm raw}.
$$

$$
Q_1^{[1\to2]}(X_i\Psi_+^j)\sim X_iXX.
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
V_{X\Lambda\Psi}.
$$

$$
\mathbb P_F(z):=
\frac{1}{2g_{\rm YM}^2}\,f^{\rm raw}_{--}(z),
\qquad
\langle F_{\rm raw}^a(y)\,\mathbb P_F^{\,b}(z)\rangle_0
=
\delta^{ab}\,\delta^{(4)}(y-z).
$$

## Step 2: Probe-amputated local correlator

$$
\mathcal G^{L}_{i}{}^{j}(x;y_1,y_2;z)
:=
\left\langle
\big[\partial_\mu J^\mu_{Q_1}(x)\,X_i(y_1)\Psi^j_+(y_2)\big]^{1\text{-loop}}_{\rm conn,loc}
\,
\mathbb P_F(z)
\right\rangle_0.
$$

ordered limit \(y_1,y_2\to y\):
$$
\boxed{
\mathcal G^{L}_{i}{}^{j}(x;y,z)
=
-\frac{g_{\rm YM}^2}{8\pi^2}\,
b_{L,{\rm raw}}\,
\delta_i^{\,j}\,
\delta^{(4)}(x-y)\,
\delta^{(4)}(y-z).
}
$$

Operational collapse used inside this seed:
$$
\partial_\mu^x
J_{F{\rm -branch},+}^{\mu,{\rm raw}}(x)
\quad
\xrightarrow[\langle \bar\Lambda\,\Lambda_+\rangle_0]{{\rm local}}
\quad
i\,F_{\rm raw}(x)\,\delta^{(4)}(x-z).
$$

$$
Q_1^{[1\to2]}(X_i\Psi_+^j)\sim X_iXX
\qquad\Longrightarrow\qquad
\text{the single-letter probe }\mathbb P_F\text{ kills tree contamination.}
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
b_L=-2\sqrt2\,i\,b_{L,{\rm raw}}.
$$

## Step 4: To compute

$$
\boxed{
\text{remaining task: evaluate }
\mathcal G^{L}_{i}{}^{j}
\text{ by the ordered raw Wick contraction of }
J_{F{\rm -branch}}^{(2,3)\mu,\rm raw}
\text{ with }V_{X\Lambda\Psi}
\text{ and the amputated probe }\mathbb P_F,
\text{ then read off }b_{L,{\rm raw}}.
}
$$
