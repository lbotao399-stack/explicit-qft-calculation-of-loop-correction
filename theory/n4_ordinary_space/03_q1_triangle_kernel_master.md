---
title: "N=4 ordinary-space: Q_1 triangle kernel master"
doc_type: theory
theory: "N=4 SYM ordinary-space"
status: working
---

# N=4 ordinary-space: Q_1 triangle kernel master

## 1. Full \(Q_1\) on the no-derivative sector

$$
Q_1^{\rm full}
=
Q_1^{[1\to 2]}
+
\frac{g_{\rm YM}^2}{8\pi^2}\,Q_{1,\triangle}^{[2\to 1]}
+
O(g_{\rm YM}^4).
$$

$$
\mathfrak q_1^{[1\to2]}:\mathbb B_0\to T^2(\mathbb B_0),
\qquad
\mathfrak q_{1,\triangle}^{[2\to1]}:\mathbb B_0\otimes\mathbb B_0\to \mathbb B_0.
$$

对 ordered bi-letters
$$
Q_{1,\triangle}^{[2\to1]}(LM)=\mathfrak q_{1,\triangle}^{[2\to1]}(L,M),
\qquad
L,M\in\mathbb B_0.
$$

## 2. Raw-to-normalized workflow

$$
\boxed{
\text{raw action}
\ \to\
\text{raw Noether current}
\ \to\
\text{raw triangle remainder}
\ \to\
\text{normalized pair-kernel}.
}
$$

令 raw seed coefficients 为
$$
\mathfrak q_{1,\triangle}^{\rm raw}(X_i,X_j)
=
a_{\rm raw}\,\epsilon_{ijk}\Psi_{\rm raw}^k,
$$

$$
\mathfrak q_{1,\triangle}^{\rm raw}(X_i,\Psi_{\rm raw}^j)
=
b_{L,{\rm raw}}\,\delta_i^{\,j}F_{\rm raw},
$$

$$
\mathfrak q_{1,\triangle}^{\rm raw}(\Psi_{\rm raw}^j,X_i)
=
b_{R,{\rm raw}}\,\delta_i^{\,j}F_{\rm raw}.
$$

又因为
$$
\Psi_{\rm raw}^i=c_\psi\,\Psi^i,
\qquad
F_{\rm raw}=c_f\,F,
\qquad
c_\psi=-2i,
\qquad
c_f=-2\sqrt2 i,
$$
所以 normalized coefficients 为
$$
a=c_\psi\,a_{\rm raw}=-2i\,a_{\rm raw},
$$

$$
b_L=\frac{c_f}{c_\psi}\,b_{L,{\rm raw}}=\sqrt2\,b_{L,{\rm raw}},
\qquad
b_R=\frac{c_f}{c_\psi}\,b_{R,{\rm raw}}=\sqrt2\,b_{R,{\rm raw}}.
$$

## 3. Three-coefficient ansatz

$$
\mathfrak q_{1,\triangle}(X_i,X_j)
=
a\,\epsilon_{ijk}\Psi^k,
$$

$$
\mathfrak q_{1,\triangle}(X_i,\Psi^j)
=
b_L\,\delta_i^{\,j}F,
$$

$$
\mathfrak q_{1,\triangle}(\Psi^j,X_i)
=
b_R\,\delta_i^{\,j}F.
$$

其余全部为零：
$$
\mathfrak q_{1,\triangle}(X_i,F)=0,
\qquad
\mathfrak q_{1,\triangle}(F,X_i)=0,
$$

$$
\mathfrak q_{1,\triangle}(\Psi^i,\Psi^j)=0,
$$

$$
\mathfrak q_{1,\triangle}(\Psi^i,F)=0,
\qquad
\mathfrak q_{1,\triangle}(F,\Psi^i)=0,
\qquad
\mathfrak q_{1,\triangle}(F,F)=0.
$$

$$
\boxed{
\text{all no-derivative bi-letter one-loop data reduce to }\{a,b_L,b_R\}.
}
$$

## 4. AWI master equation

$$
\mathcal O_{LM}(y):=\operatorname{Tr}(LM)(y),
\qquad
L,M\in\mathbb B_0.
$$

$$
\big[\partial_\mu J^\mu_{Q_1}(x),\mathcal O_{LM}(y)\big]_{\rm loc}^{1\text{-loop}}
=
-\delta^{(4)}(x-y)
\Big(
Q_1^{[1\to2]}\mathcal O_{LM}
+
\frac{g_{\rm YM}^2}{8\pi^2}
Q_{1,\triangle}^{[2\to1]}\mathcal O_{LM}
\Big).
$$

在 page 上真正要抽取的是
$$
\text{triangle local remainder}
=
-\delta^{(4)}(x-y)\,
\frac{g_{\rm YM}^2}{8\pi^2}\,
\mathfrak q_{1,\triangle}(L,M).
$$

对 raw seed pages，对应写法是
$$
\text{triangle local remainder}^{\rm raw}
=
-\delta^{(4)}(x-y)\,
\frac{g_{\rm YM}^2}{8\pi^2}\,
\mathfrak q_{1,\triangle}^{\rm raw}(L,M).
$$

## 5. Universal local triangle integral

$$
[\Delta(x)^2]_{\rm R}
=
-\frac{1}{64\pi^4}\,
\square\!\left(\frac{\ln(\mu^2 x^2)}{x^2}\right).
$$

$$
I_{\triangle}^{\rm loc}(x)
:=
\mu\frac{\partial}{\partial\mu}[\Delta(x)^2]_{\rm R}
=
\frac{1}{8\pi^2}\,\delta^{(4)}(x).
$$

$$
\boxed{
\text{all seed channels should be reduced to }
(\text{spinor factor})\times(\text{color factor})\times I_{\triangle}^{\rm loc}(x-y).
}
$$

DR-compatible statement:
$$
\Delta_\epsilon(x)
=
\frac{\Gamma(1-\epsilon)}{4\pi^{2-\epsilon}}\,
\frac{1}{(x^2)^{1-\epsilon}},
$$

$$
\mu^{2\epsilon}\Delta_\epsilon(x)^2
=
-\frac{1}{16\pi^2}\frac{1}{\epsilon}\,\delta^{(4)}(x)
-\frac{1}{64\pi^4}\,
\square\!\left(\frac{\ln(\mu^2 x^2)}{x^2}\right)
+O(\epsilon),
$$

$$
\boxed{
\text{minimal subtraction leaves }
I_{\triangle}^{\rm loc}(x)=\frac{1}{8\pi^2}\delta^{(4)}(x).
}
$$

## 6. Planar lift after seed stage

$$
Q_{1,\triangle}^{[2\to1]}\operatorname{Tr}(L_1L_2\cdots L_n)
=
\frac{g_{\rm YM}^2}{8\pi^2}
\sum_{r=1}^{n-1}
(-1)^{\sum_{s<r}|L_s|}
\operatorname{Tr}\!\big(
L_1\cdots
\mathfrak q_{1,\triangle}(L_r,L_{r+1})
\cdots L_n
\big).
$$

$$
\boxed{
\text{first compute }\mathfrak q_{1,\triangle}(L,M)\text{ on ordered bi-letters, then lift.}
}
$$
