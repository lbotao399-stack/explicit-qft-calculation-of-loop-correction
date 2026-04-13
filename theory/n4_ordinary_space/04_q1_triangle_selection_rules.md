---
title: "N=4 ordinary-space: Q_1 triangle selection rules"
doc_type: theory
theory: "N=4 SYM ordinary-space"
status: working
---

# N=4 ordinary-space: Q_1 triangle selection rules

## 1. Channel reduction

由 dimension / Lorentz / \(SU(3)\)：
$$
X_iX_j\to \Psi^k,
\qquad
X_i\Psi^j\to F,
\qquad
\Psi^jX_i\to F
$$
是唯一 nonzero channels。

## 2. Seed pages

$$
\boxed{
\text{Seed 1: }(X_iX_j\to\Psi^k),
\qquad
\text{Seed 2: }(X_i\Psi^j\to F),
\qquad
\text{Seed 3: }(\Psi^jX_i\to F).
}
$$

## 3. Zero channels

$$
X_iF,\qquad FX_i,\qquad \Psi^i\Psi^j,\qquad \Psi^iF,\qquad F\Psi^i,\qquad FF
$$

$$
\boxed{
\text{all zero by quantum numbers in the no-derivative }2\to1\text{ sector}.
}
$$

## 4. Seed-channel assignment

$$
X_iX_j\to\Psi^k
\quad\Longleftrightarrow\quad
J^\mu_{\psi\text{-branch}}{}^{\rm raw}
\ \text{and the honest bare vertex }\ V_{A X\bar X}.
$$

$$
X_i\Psi^j\to F
\quad\Longleftrightarrow\quad
J^\mu_{F\text{-branch}}{}^{\rm raw}
\ \text{and the honest bare vertex }\ V_{X\Lambda\Psi}.
$$

$$
\Psi^jX_i\to F
\quad\Longleftrightarrow\quad
J^\mu_{F\text{-branch}}{}^{\rm raw}
\ \text{and}\ V_{X\Lambda\Psi},
\ \text{with reversed external ordering}.
$$

## 5. Nilpotency check set

算完 \(\{a,b_L,b_R\}\) 后，先检查
$$
Q_1^2(X_iX_jX_k)=0,
$$

$$
Q_1^2(X_iX_j\Psi^k)=0,
$$

$$
Q_1^2(X_i\Psi^jX_k)=0,
$$

$$
Q_1^2(\Psi^iX_jX_k)=0.
$$

$$
\boxed{
\text{this step checks }a,b_L,b_R\text{ and left/right signs before any long-word lift.}
}
$$
