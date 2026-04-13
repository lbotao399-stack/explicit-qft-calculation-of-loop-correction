---
title: "N=4 ordinary-space: BPS alphabet and Q_1"
doc_type: theory
theory: "N=4 SYM ordinary-space"
status: working
---

# N=4 ordinary-space: BPS alphabet and Q_1

## 1. Freeze

$$
\boxed{
\text{ordinary-space only},\qquad
Q_1:=Q_-^4,\qquad
\text{no }N=1\text{ superspace},\qquad
\text{no derivative letters}.
}
$$

$$
A,B,C,D=1,2,3,4,
\qquad
i,j,k=1,2,3.
$$

## 2. Raw off-shell field notation

$$
A_{\alpha\dot\alpha},\quad
f_{\alpha\beta},\ \bar f_{\dot\alpha\dot\beta},\quad
\lambda^A_\alpha,\ \bar\lambda_{A\dot\alpha},\quad
\phi^{AB}=-\phi^{BA},\quad
\bar\phi_{AB}=\frac12\epsilon_{ABCD}\phi^{CD}.
$$

$$
\Lambda_\alpha:=\lambda^4_\alpha,
\qquad
\bar\Lambda_{\dot\alpha}:=\bar\lambda_{4\dot\alpha},
$$

$$
X_i:=\phi_{i4}=\frac12\epsilon_{ijk}\phi^{jk},
\qquad
\bar X^i:=\phi^{i4},
$$

$$
\Psi^i_\alpha:=\lambda^i_\alpha,
\qquad
\bar\Psi_{i\dot\alpha}:=\bar\lambda_{i\dot\alpha},
$$

$$
D,
\qquad
G^i,
\qquad
\bar G_i.
$$

$$
Q_1=Q_-^4
\qquad
\text{is kept as the }A=4\text{ supercharge and projected to }\alpha=-\text{ only at the end.}
$$

## 3. Raw no-derivative letter alphabet

$$
\Psi_{\rm raw}^i:=\Psi^i_{+}=\lambda^i_{+},
\qquad
F_{\rm raw}:=f_{++}.
$$

$$
\mathbb B_0^{\rm raw}:=\{X_i,\Psi_{\rm raw}^i,F_{\rm raw}\}.
$$

由
$$
Q_1\phi^{ij}=0,
\qquad
Q_1\Psi^i_+=i[\phi^{ij},\bar\phi_{j4}],
\qquad
Q_1F_{\rm raw}=iD_{+\dot\alpha}\bar\Lambda^{\dot\alpha},
$$
以及
$$
\phi^{ij}=\epsilon^{ijk}X_k,
\qquad
\bar\phi_{j4}=X_j,
$$
得
$$
Q_1 X_i=0,
$$

$$
Q_1\Psi_{\rm raw}^i
=
i\epsilon^{ijk}[X_k,X_j]
=
-2i\,\epsilon^{ijk}X_jX_k,
$$

$$
\boxed{
Q_1F_{\rm raw}=iD_{+\dot\alpha}\bar\Lambda^{\dot\alpha}
}
$$

## 4. Normalized cohomological alphabet

raw current / triangle remainder 先在
$$
\{X_i,\Psi_{\rm raw}^i,F_{\rm raw}\}
$$
上做；只在最后归一到
$$
\mathbb B_0=\{X_i,\Psi^i,F\}.
$$

取
$$
c_\psi:=-2i,
\qquad
c_f:=\sqrt2\,c_\psi=-2\sqrt2 i.
$$

定义
$$
\Psi^i:=\frac{1}{c_\psi}\Psi_{\rm raw}^i,
\qquad
F:=\frac{1}{c_f}F_{\rm raw}.
$$

于是
$$
\mathbb B_0:=\{X_i,\Psi^i,F\}.
$$

于是
$$
Q_1 X_i=0,
$$

$$
Q_1 \Psi^i=\epsilon^{ijk}X_jX_k,
$$

$$
Q_1 F=[X_i,\Psi^i].
$$

这层 normalized cohomological rule 只用于最终 pair-kernel 记号，不用于 raw Noether current derivation。

## 5. Statistics and dimensions

$$
|X_i|=0,
\qquad
|\Psi^i|=1,
\qquad
|F|=0.
$$

$$
\Delta(X)=1,
\qquad
\Delta(\Psi)=\frac32,
\qquad
\Delta(F)=2,
\qquad
\Delta(Q_1)=\frac12.
$$

## 6. Classical operator map

$$
\mathfrak q_1^{[1\to2]}:\mathbb B_0\to T^2(\mathbb B_0).
$$

$$
\mathfrak q_1^{[1\to2]}(X_i)=0,
\qquad
\mathfrak q_1^{[1\to2]}(\Psi^i)=\epsilon^{ijk}X_jX_k,
\qquad
\mathfrak q_1^{[1\to2]}(F)=[X_i,\Psi^i].
$$

## 7. Scope of current stage

$$
\boxed{
\text{current stage: compute the one-loop ordered bi-letter kernel on }\mathbb B_0\otimes\mathbb B_0.
}
$$
