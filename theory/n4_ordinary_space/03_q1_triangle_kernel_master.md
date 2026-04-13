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
\Psi_{\rm raw}^i=-2i\,\Psi^i,
\qquad
F_{\rm raw}=-2\sqrt2\,i\,F,
$$
所以 normalized coefficients 为
$$
a=-2i\,a_{\rm raw},
$$

$$
b_L=-2\sqrt2\,i\,b_{L,{\rm raw}},
\qquad
b_R=-2\sqrt2\,i\,b_{R,{\rm raw}}.
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

## 4. Ordered probe-amputated extraction

seed coefficient 不从裸的
$$
\langle \partial\!\cdot\!J,\Tr(LM)\rangle
$$
读取。

先把输入写成 ordered open product
$$
\mathcal O_{LM}(y_1,y_2):=L(y_1)M(y_2),
\qquad
y_1\to y,\ y_2\to y\ \text{only at the end}.
$$

定义 probe-amputated correlator
$$
\mathcal G_{LM\to N}(x;y_1,y_2;z)
:=
\left\langle
\big[\partial_\mu J^\mu_{Q_1}(x)\,\mathcal O_{LM}(y_1,y_2)\big]^{1\text{-loop}}_{\rm conn,loc}
\,
\mathbb P_N(z)
\right\rangle_0.
$$

其中 \(\mathbb P_N\) 满足
$$
\boxed{
\langle N(y)\,\mathbb P_M(z)\rangle_0
=
\delta_{N,M}\,\delta^{(4)}(y-z).
}
$$

## 5. Amputated probes

对 \(\Psi_{\rm raw}^k=\Psi^k_+\) 输出：
$$
\boxed{
\mathbb P_{\Psi,k}(z)
:=
-\frac{i}{g_{\rm YM}^2}\,
\partial_z^{+\dot\alpha}\bar\Psi_{k\dot\alpha}(z).
}
$$

$$
\boxed{
\langle \Psi_+^{i\,a}(y)\,\mathbb P_{\Psi,k}^{\,b}(z)\rangle_0
=
\delta^i_k\,\delta^{ab}\,\delta^{(4)}(y-z).
}
$$

对 \(F_{\rm raw}=f^{\rm raw}_{++}\) 输出：
$$
\boxed{
\mathbb P_F(z):=
\frac{1}{2g_{\rm YM}^2}\,f^{\rm raw}_{--}(z).
}
$$

$$
\langle f^{\rm raw\,a}_{\alpha\beta}(y)\,
f^{\rm raw\,b}_{\gamma\delta}(z)\rangle_0
=
g_{\rm YM}^2\,\delta^{ab}\,
\big(
\epsilon_{\alpha\gamma}\epsilon_{\beta\delta}
+
\epsilon_{\alpha\delta}\epsilon_{\beta\gamma}
\big)\,
\delta^{(4)}(y-z),
$$

从而
$$
\boxed{
\langle F_{\rm raw}^a(y)\,\mathbb P_F^{\,b}(z)\rangle_0
=
\delta^{ab}\,\delta^{(4)}(y-z).
}
$$

bare-probe language 与 inverse 2-point amputation 等价：
$$
\mathcal A_{\Psi_+}^{\dot\alpha}
=
-\frac{i}{g_{\rm YM}^2}\,\partial_z^{+\dot\alpha}
\quad \text{acting on } \bar\Psi_{k\dot\alpha}(z),
$$

$$
\mathcal A_F
=
\frac{1}{2g_{\rm YM}^2}
\quad \text{acting on } f^{\rm raw}_{--}(z).
$$

$$
\boxed{
\text{Use probe-amputated legs from the start.}
}
$$

## 6. Coefficient extraction equations

`XX -> Psi_raw`:
$$
\mathcal G_{ij|k}(x;y_1,y_2;z)
:=
\left\langle
\big[\partial_\mu J^\mu_{Q_1}(x)\,X_i(y_1)X_j(y_2)\big]^{1\text{-loop}}_{\rm conn,loc}
\,
\mathbb P_{\Psi,k}(z)
\right\rangle_0.
$$

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

`X Psi_raw -> F_raw`:
$$
\mathcal G^{L}_{i}{}^{j}(x;y_1,y_2;z)
:=
\left\langle
\big[\partial_\mu J^\mu_{Q_1}(x)\,X_i(y_1)\Psi^j_+(y_2)\big]^{1\text{-loop}}_{\rm conn,loc}
\,
\mathbb P_F(z)
\right\rangle_0.
$$

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

`Psi_raw X -> F_raw`:
$$
\mathcal G^{R}_{i}{}^{j}(x;y_1,y_2;z)
:=
\left\langle
\big[\partial_\mu J^\mu_{Q_1}(x)\,\Psi^j_+(y_1)X_i(y_2)\big]^{1\text{-loop}}_{\rm conn,loc}
\,
\mathbb P_F(z)
\right\rangle_0.
$$

$$
\boxed{
\mathcal G^{R}_{i}{}^{j}(x;y,z)
=
-\frac{g_{\rm YM}^2}{8\pi^2}\,
b_{R,{\rm raw}}\,
\delta_i^{\,j}\,
\delta^{(4)}(x-y)\,
\delta^{(4)}(y-z).
}
$$

## 7. Universal local triangle integral

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

## 8. Planar lift after seed stage

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
