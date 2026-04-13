---
title: "N=4 ordinary-space: Q_1 current relevant branches"
doc_type: theory
theory: "N=4 SYM ordinary-space"
status: working
---

# N=4 ordinary-space: Q_1 current relevant branches

## 1. Raw off-shell layer

$$
\Lambda_\alpha:=\lambda^4_\alpha,
\qquad
\bar\Lambda_{\dot\alpha}:=\bar\lambda_{4\dot\alpha},
$$

$$
X_i:=\phi_{i4},
\qquad
\bar X^i:=\phi^{i4},
\qquad
\Psi^i_\alpha:=\lambda^i_\alpha,
\qquad
\bar\Psi_{i\dot\alpha}:=\bar\lambda_{i\dot\alpha},
$$

$$
D,\qquad G^i,\qquad \bar G_i.
$$

## 2. Off-shell ordinary-space action

$$
\mathcal L
=
\frac1{g_{\rm YM}^2}\Tr\Big[
-\frac14 F_{\mu\nu}F^{\mu\nu}
-i\,\Lambda\sigma^\mu\nabla_\mu\bar\Lambda
+\frac12 D^2
-\nabla_\mu X_i\,\nabla^\mu \bar X^i
-i\,\Psi^i\sigma^\mu\nabla_\mu\bar\Psi_i
+\bar G_i G^i
\Big]
+\mathcal L_{\rm int}.
$$

$$
\mathcal L_{\rm int}
=
\frac1{g_{\rm YM}^2}\Tr\Big[
D[X_i,\bar X^i]
+\sqrt2\,i\,\Lambda^\alpha[X_i,\Psi^i_\alpha]
-\sqrt2\,i\,\bar\Lambda_{\dot\alpha}[\bar X^i,\bar\Psi_i^{\dot\alpha}]
+G^i\,\mathcal W_i
+\bar G_i\,\bar{\mathcal W}^i
\Big].
$$

$$
\mathcal W_i\propto \epsilon_{ijk}[\bar X^j,\bar X^k],
\qquad
\bar{\mathcal W}^i\propto \epsilon^{ijk}[X_j,X_k].
$$

## 3. Localized Noether identity

$$
\eta^\alpha_A(x)=\eta^\alpha_4(x)\,\delta_A^{\,4},
\qquad
\eta^\alpha_4(x)\ \text{kept general until the final }\alpha=-\text{ projection}.
$$

$$
\delta_{\eta(x)}\mathcal L
=
(\partial_\mu \eta^\alpha_4)\,J^\mu_{4\alpha}
+\eta^\alpha_4 \sum_\Phi \frac{\delta S}{\delta \Phi}\,\delta_{4\alpha}\Phi
+\partial_\mu\!\big(\eta^\alpha_4\,B^\mu_{4\alpha}\big).
$$

$$
J^\mu_{4\alpha}
=
\sum_\Phi
\frac{\partial \mathcal L}{\partial(\partial_\mu\Phi)}\,\Delta_{4\alpha}\Phi
-B^\mu_{4\alpha},
\qquad
\delta\Phi=\eta^\alpha_4\,\Delta_{4\alpha}\Phi.
$$

工作上直接从 localized variation 读取 \((\partial_\mu\eta^\alpha_4)\)-coefficient。

## 4. Raw SUSY transformations needed for current derivation

$$
\Delta_{4\alpha}A_{\beta\dot\beta}
=
i\,\epsilon_{\alpha\beta}\,\bar\Lambda_{\dot\beta},
$$

$$
\Delta_{4\alpha}\Lambda_\beta
=
F_{\alpha\beta}
+i\,\epsilon_{\alpha\beta}D,
$$

$$
\delta_\eta X_i=0,
$$

$$
\Delta_{4\alpha}\Psi^i_\beta
=
\epsilon_{\alpha\beta}\,\bar G^i,
$$

$$
\delta_{\eta}\bar\Psi_{i\dot\beta}
=
-\,i\,\eta^\alpha_4\,\nabla_{\alpha\dot\beta}X_i,
$$

$$
\delta_{\eta}\bar\Lambda_{\dot\beta}=0.
$$

## 5. Raw current split

$$
J^\mu_{Q_1}{}^{\rm raw}
=
J^\mu_{\psi\text{-branch}}{}^{\rm raw}
+
J^\mu_{F\text{-branch}}{}^{\rm raw}
+
(\text{other raw branches, ignored for no-derivative }2\to1).
$$

### 5.1 \(\psi\)-output branch

从
$$
\mathcal L_{\rm mat,kin}
=
\frac1{g_{\rm YM}^2}\Tr\Big[
-\nabla_\mu X_i\,\nabla^\mu \bar X^i
-i\,\Psi^i\sigma^\mu\nabla_\mu\bar\Psi_i
+\bar G_i G^i
\Big]
$$
localized 之后保留 \((\partial_\mu\eta^\alpha_4)\)-项：
$$
\delta_{\eta(x)}\mathcal L_{\rm mat,kin}
\supset
(\partial_\mu\eta^\alpha_4)\,
\frac{\sqrt2}{g_{\rm YM}^2}
\Tr\!\left[
(\nabla_\nu X_i)(\sigma^\nu\bar\sigma^\mu\Psi^i)_\alpha
-i\,\bar G_i(\sigma^\mu\bar\Psi^i)_\alpha
\right].
$$

因此
$$
J^\mu_{4\alpha}\big|_{\rm matter}
=
\frac{\sqrt2}{g_{\rm YM}^2}
\Tr\!\left[
(\nabla_\nu X_i)(\sigma^\nu\bar\sigma^\mu\Psi^i)_\alpha
-i\,\bar G_i(\sigma^\mu\bar\Psi^i)_\alpha
\right].
$$

对 no-derivative bi-letter \(2\to1\) 的 relevant branch，只保留第一项：
$$
J^\mu_{\psi{\rm -branch},\,\alpha}^{\rm raw}
=
\frac{\sqrt2}{g_{\rm YM}^2}
\Tr\!\left[
(\nabla_\nu X_i)(\sigma^\nu\bar\sigma^\mu\Psi^i)_\alpha
\right].
$$

$$
J^\mu_{\psi{\rm -branch}}^{\rm raw}
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

### 5.2 \(F\)-output branch

从
$$
\mathcal L_{\rm vec,kin}
=
\frac1{g_{\rm YM}^2}\Tr\Big[
-\frac14 F_{\rho\sigma}F^{\rho\sigma}
-i\,\Lambda\sigma^\nu\nabla_\nu\bar\Lambda
+\frac12 D^2
\Big]
$$
localized 之后保留 \((\partial_\mu\eta^\alpha_4)\)-项：

$$
\delta_{\eta(x)}\mathcal L_{\rm vec,kin}
\supset
(\partial_\mu\eta^\alpha_4)\,
\frac1{g_{\rm YM}^2}
\Tr\!\left[
-\frac12 F_{\rho\sigma}(\sigma^{\rho\sigma}\sigma^\mu\bar\Lambda)_\alpha
+iD(\sigma^\mu\bar\Lambda)_\alpha
\right].
$$

因此
$$
J^\mu_{4\alpha}\big|_{\rm vec}
=
\frac1{g_{\rm YM}^2}
\Tr\!\left[
-\frac12 F_{\rho\sigma}(\sigma^{\rho\sigma}\sigma^\mu\bar\Lambda)_\alpha
+iD(\sigma^\mu\bar\Lambda)_\alpha
\right].
$$

对 no-derivative bi-letter \(2\to1\) 的 relevant branch，只保留 \(F\bar\Lambda\) 这一项：
$$
J^\mu_{F{\rm -branch},\,\alpha}^{\rm raw}
=
-\frac1{2g_{\rm YM}^2}
\Tr\!\left[
F_{\rho\sigma}(\sigma^{\rho\sigma}\sigma^\mu\bar\Lambda)_\alpha
\right].
$$

$$
J^\mu_{F{\rm -branch}}^{\rm raw}
=
-\frac1{2g_{\rm YM}^2}
\Tr\!\left[
F_{\rho\sigma}(\sigma^{\rho\sigma}\sigma^\mu\bar\Lambda)_-
\right].
$$

$$
J_{F{\rm -branch}}^{(2)\mu,\rm raw}
=
-\frac1{2g_{\rm YM}^2}
\Tr\!\left[
(\partial_\rho A_\sigma-\partial_\sigma A_\rho)
(\sigma^{\rho\sigma}\sigma^\mu\bar\Lambda)_-
\right],
$$

$$
J_{F{\rm -branch}}^{(3)\mu,\rm raw}
=
\frac{i}{2g_{\rm YM}^2}
\Tr\!\left[
[A_\rho,A_\sigma]
(\sigma^{\rho\sigma}\sigma^\mu\bar\Lambda)_-
\right].
$$

## 6. Honest action-level cubic vertices

$$
\boxed{
\mathcal L_{A X\bar X}^{(3)}
=
\frac{i}{g_{\rm YM}^2}\Tr\!\left[
(\partial_\mu X_i)[A^\mu,\bar X^i]
-(\partial_\mu \bar X^i)[A^\mu,X_i]
\right]
}
$$

$$
\boxed{V_{A X\bar X}}
$$

$$
\boxed{
\mathcal L_{X\Lambda\Psi}^{(3)}
=
\frac{\sqrt2\,i}{g_{\rm YM}^2}
\Tr\!\left[
\Lambda^\alpha[X_i,\Psi^i_\alpha]
\right]
}
$$

$$
\boxed{
\mathcal L_{\bar X\,\bar\Lambda\,\bar\Psi}^{(3)}
=
-\frac{\sqrt2\,i}{g_{\rm YM}^2}
\Tr\!\left[
\bar\Lambda_{\dot\alpha}[\bar X^i,\bar\Psi_i^{\dot\alpha}]
\right]
}
$$

$$
\boxed{V_{X\Lambda\Psi}},
\qquad
\boxed{V_{\bar X\,\bar\Lambda\,\bar\Psi}}.
$$

旧 shorthand 只能作 effective channel label：
$$
V_{A X X}^{\rm eff}
:=
\text{the channel obtained after the current branch fixes which scalar leg is conjugate},
$$

$$
V_{X\Psi\bar\Lambda}^{\rm eff}
:=
\text{the channel where }J_{F{\rm -branch}}^{\rm raw}\text{ supplies }\bar\Lambda
\text{ and the action vertex is }V_{X\Lambda\Psi}.
$$

## 7. Conversion to normalized alphabet

$$
\Psi_{\rm raw}^i=-2i\,\Psi^i,
\qquad
f_{++}^{\rm raw}=-2\sqrt2\,i\,F.
$$

因此 matter branch 可直接改写成
$$
J^\mu_{\psi{\rm -branch}}
=
-\frac{2\sqrt2\,i}{g_{\rm YM}^2}
\Tr\!\left[
(\nabla_\nu X_i)(\sigma^\nu\bar\sigma^\mu\Psi^i)_-
\right].
$$

而 \(F\)-branch 先保持 raw spinor projector：
$$
J^\mu_{F{\rm -branch}}{}^{\rm raw}
=
-\frac1{2g_{\rm YM}^2}
\Tr\!\left[
F_{\rho\sigma}(\sigma^{\rho\sigma}\sigma^\mu\bar\Lambda)_-
\right].
$$

$$
\boxed{
\text{replace }F_{\rho\sigma}\sigma^{\rho\sigma}\text{ by the project-level }f_{++}\text{ decomposition only once, not page-by-page.}
}
$$
