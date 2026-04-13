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

$$
A_{\alpha\dot\alpha},\quad
f_{\alpha\beta},\ \bar f_{\dot\alpha\dot\beta},\quad
\lambda^A_\alpha,\ \bar\lambda_{A\dot\alpha},\quad
\phi^{AB}=-\phi^{BA},\quad
\bar\phi_{AB}=\frac12\epsilon_{ABCD}\phi^{CD}.
$$

## 2. Raw no-derivative alphabet

$$
X_i^{\rm raw}:=\frac12\epsilon_{ijk}\phi^{jk},
\qquad
\Psi_{\rm raw}^i:=\lambda^i_{+},
\qquad
F_{\rm raw}:=f_{++}.
$$

$$
\mathbb B_0^{\rm raw}:=\{X_i^{\rm raw},\Psi_{\rm raw}^i,F_{\rm raw}\}.
$$

由
$$
Q_1\phi^{ij}=0,
\qquad
Q_1\lambda_+^i=i[\phi^{ij},\bar\phi_{j4}],
\qquad
Q_1 f_{++}=iD_{+\dot\alpha}\bar\lambda_4^{\dot\alpha},
$$
以及
$$
\phi^{ij}=\epsilon^{ijk}X_k^{\rm raw},
\qquad
\bar\phi_{j4}=X_j^{\rm raw},
$$
得
$$
Q_1 X_i^{\rm raw}=0,
$$

$$
Q_1\Psi_{\rm raw}^i
=
i\epsilon^{ijk}[X_k^{\rm raw},X_j^{\rm raw}]
=
-2i\,\epsilon^{ijk}X_j^{\rm raw}X_k^{\rm raw},
$$

$$
Q_1F_{\rm raw}
=
\sqrt2[X_i^{\rm raw},\Psi_{\rm raw}^i].
$$

## 3. Normalized cohomological alphabet

取
$$
c_\psi:=-2i,
\qquad
c_f:=\sqrt2\,c_\psi=-2\sqrt2 i.
$$

定义
$$
X_i:=X_i^{\rm raw},
\qquad
\Psi^i:=\frac{1}{c_\psi}\Psi_{\rm raw}^i,
\qquad
F:=\frac{1}{c_f}F_{\rm raw}.
$$

于是
$$
\mathbb B_0:=\{X_i,\Psi^i,F\}.
$$

并且 classical action of \(Q_1\) 统一成
$$
Q_1 X_i=0,
$$

$$
Q_1 \Psi^i=\epsilon^{ijk}X_jX_k,
$$

$$
Q_1 F=[X_i,\Psi^i].
$$

## 4. Statistics and dimensions

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

## 5. Classical operator map

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

## 6. Scope of current stage

$$
\boxed{
\text{current stage: compute the one-loop ordered bi-letter kernel on }\mathbb B_0\otimes\mathbb B_0.
}
$$
