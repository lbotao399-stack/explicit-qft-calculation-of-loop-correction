---
title: "N=4 ordinary-space: Q_1 current relevant branches"
doc_type: theory
theory: "N=4 SYM ordinary-space"
status: working
---

# N=4 ordinary-space: Q_1 current relevant branches

## 0. Global ordinary-space conventions

$$
[T^a,T^b]=i f^{abc}T^c,
\qquad
\Tr(T^aT^b)=\delta^{ab}.
$$

$$
\Delta(x):=\frac{1}{4\pi^2 x^2},
\qquad
-\square\,\Delta(x)=\delta^{(4)}(x).
$$

$$
\partial_{\alpha\dot\alpha}:=\sigma^\mu_{\alpha\dot\alpha}\partial_\mu,
\qquad
\partial^{\alpha\dot\alpha}:=\epsilon^{\alpha\beta}\epsilon^{\dot\alpha\dot\beta}\partial_{\beta\dot\beta}.
$$

$$
\partial^{\beta\dot\beta}\partial_{\alpha\dot\beta}
=
\delta^\beta_{\ \alpha}\,\square.
$$

$$
\mathcal L_{\rm gf}
=
\frac{1}{2g_{\rm YM}^2}\,(\partial_\mu A^\mu)^2.
$$

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

## 3. Raw free propagators

Quadratic action:
$$
S_2
=
\frac{1}{g_{\rm YM}^2}\int d^4x\,
\Tr\Big[
\bar X^i(-\square)X_i
-i\,\Lambda^\alpha\partial_{\alpha\dot\beta}\bar\Lambda^{\dot\beta}
-i\,\Psi^{i\alpha}\partial_{\alpha\dot\beta}\bar\Psi_i^{\dot\beta}
+\frac12 A_\mu(-\square\delta_{\mu\nu})A_\nu
+\frac12 D^2
+\bar G_i G^i
\Big].
$$

$$
\langle X_i^a(x)\,\bar X^{j\,b}(y)\rangle_0
=
g_{\rm YM}^2\,\delta_i^{\ j}\,\delta^{ab}\,\Delta(x-y).
$$

$$
\langle \Lambda_\alpha^a(x)\,\bar\Lambda_{\dot\beta}^{\,b}(y)\rangle_0
=
i\,g_{\rm YM}^2\,\delta^{ab}\,\partial_{\alpha\dot\beta}\Delta(x-y).
$$

$$
\langle \Psi^{i\,a}_\alpha(x)\,\bar\Psi_{j\dot\beta}^{\,b}(y)\rangle_0
=
i\,g_{\rm YM}^2\,\delta^i_{\ j}\,\delta^{ab}\,\partial_{\alpha\dot\beta}\Delta(x-y).
$$

$$
\langle A_\mu^a(x)\,A_\nu^b(y)\rangle_0
=
g_{\rm YM}^2\,\delta^{ab}\,\delta_{\mu\nu}\,\Delta(x-y).
$$

$$
A_{\alpha\dot\alpha}:=\sigma^\mu_{\alpha\dot\alpha}A_\mu
\qquad\Longrightarrow\qquad
\langle A_{\alpha\dot\alpha}^a(x)\,A_{\beta\dot\beta}^b(y)\rangle_0
=
2\,g_{\rm YM}^2\,\delta^{ab}\,\epsilon_{\alpha\beta}\epsilon_{\dot\alpha\dot\beta}\,\Delta(x-y).
$$

$$
\langle D^a(x)D^b(y)\rangle_0
=
g_{\rm YM}^2\,\delta^{ab}\,\delta^{(4)}(x-y),
\qquad
\langle G^{i\,a}(x)\,\bar G_{j}^{\,b}(y)\rangle_0
=
g_{\rm YM}^2\,\delta^i_{\ j}\,\delta^{ab}\,\delta^{(4)}(x-y).
$$

$$
\langle X X\rangle_0
=
\langle \bar X\bar X\rangle_0
=
\langle \Lambda\Lambda\rangle_0
=
\langle \bar\Lambda\bar\Lambda\rangle_0
=
\langle \Psi\Psi\rangle_0
=
\langle \bar\Psi\bar\Psi\rangle_0
=
0.
$$

## 4. Localized Noether identity

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

## 5. Raw SUSY transformations needed for current derivation

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

## 6. Raw current split

$$
J^\mu_{Q_1}{}^{\rm raw}
=
J^\mu_{\psi\text{-branch}}{}^{\rm raw}
+
J^\mu_{F\text{-branch}}{}^{\rm raw}
+
(\text{other raw branches, ignored for no-derivative }2\to1).
$$

### 6.1 \(\psi\)-output branch

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

### 6.2 \(F\)-output branch

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

## 7. Self-dual projector and unified \(F\)-branch formula

$$
f^{\rm raw}_{\alpha\beta}
:=
\nabla_{(\alpha|\dot\gamma|}A_{\beta)}{}^{\dot\gamma},
\qquad
F_{\rho\sigma}(\sigma^{\rho\sigma})_{\alpha\beta}
=
2\,f^{\rm raw}_{\alpha\beta}.
$$

$$
F_{\rm raw}:=f^{\rm raw}_{++}.
$$

$$
F_{\rho\sigma}(\sigma^{\rho\sigma}\sigma^\mu\bar\Lambda)_\alpha
=
2\,f^{\rm raw}_{\alpha\beta}\,
\sigma^{\mu\,\beta\dot\beta}\bar\Lambda_{\dot\beta}.
$$

$$
J^{\mu,{\rm raw}}_{F{\rm -branch},\alpha}
=
-\frac{1}{g_{\rm YM}^2}
\Tr\!\left[
f^{\rm raw}_{\alpha\beta}\,
\sigma^{\mu\,\beta\dot\beta}\bar\Lambda_{\dot\beta}
\right].
$$

$$
J^{\mu,{\rm raw}}_{F{\rm -branch}}
=
-\frac{1}{g_{\rm YM}^2}
\Tr\!\left[
f^{\rm raw}_{-\beta}\,
\sigma^{\mu\,\beta\dot\beta}\bar\Lambda_{\dot\beta}
\right].
$$

$$
J_{F{\rm -branch}}^{(2)\mu,\rm raw}
=
-\frac1{g_{\rm YM}^2}
\Tr\!\left[
f^{(2)\,{\rm raw}}_{-\beta}\,
\sigma^{\mu\,\beta\dot\beta}\bar\Lambda_{\dot\beta}
\right],
\qquad
J_{F{\rm -branch}}^{(3)\mu,\rm raw}
=
-\frac1{g_{\rm YM}^2}
\Tr\!\left[
f^{(3)\,{\rm raw}}_{-\beta}\,
\sigma^{\mu\,\beta\dot\beta}\bar\Lambda_{\dot\beta}
\right].
$$

with
$$
f^{(2)\,{\rm raw}}_{\alpha\beta}
:=
\partial_{(\alpha|\dot\gamma|}A_{\beta)}{}^{\dot\gamma},
\qquad
f^{(3)\,{\rm raw}}_{\alpha\beta}
:=
-i[A_{(\alpha|\dot\gamma|},A_{\beta)}{}^{\dot\gamma}].
$$

For the \(F_{\rm raw}\)-output seed pages the operational collapse uses the \(\Lambda_+\) line:
$$
\langle \Lambda_+^a(z)\,\bar\Lambda_{\dot\beta}^{\,b}(x)\rangle_0
=
i\,g_{\rm YM}^2\,\delta^{ab}\,\partial_{+\dot\beta}\Delta(z-x).
$$

$$
\partial_\mu^x
J_{F{\rm -branch},\alpha}^{\mu,{\rm raw}}(x)
\quad
\xrightarrow{\text{contract }\bar\Lambda(x)\text{ with }\Lambda_+(z)}
\quad
-\frac{i}{g_{\rm YM}^2}\,
f^{\rm raw}_{\alpha\beta}(x)\,
\partial^{\beta\dot\beta}_x\partial_{+\dot\beta}^x\Delta(x-z).
$$

$$
\partial^{\beta\dot\beta}\partial_{+\dot\beta}\Delta(x-z)
=
-\delta^\beta_{\ +}\,\delta^{(4)}(x-z),
$$

$$
\partial_\mu^x
J_{F{\rm -branch},\alpha}^{\mu,{\rm raw}}(x)
\quad
\xrightarrow[\langle \bar\Lambda\,\Lambda_+\rangle_0]{{\rm local}}
\quad
i\,f^{\rm raw}_{\alpha +}(x)\,\delta^{(4)}(x-z).
$$

For the actual \(F_{\rm raw}\)-output channel choose \(\alpha=+\):
$$
\boxed{
\partial_\mu^x
J_{F{\rm -branch},+}^{\mu,{\rm raw}}(x)
\quad
\xrightarrow[\langle \bar\Lambda\,\Lambda_+\rangle_0]{{\rm local}}
\quad
i\,F_{\rm raw}(x)\,\delta^{(4)}(x-z)
}
$$

## 8. Honest action-level cubic vertices

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

## 9. Conversion to normalized alphabet

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

而 \(F\)-output collapse 在 normalized language 中满足
$$
i\,F_{\rm raw}
=
i(-2\sqrt2 i)F
=
2\sqrt2\,F.
$$

$$
\boxed{
\partial_\mu^x
J_{F{\rm -branch},+}^{\mu,{\rm raw}}(x)
\quad
\xrightarrow[\langle \bar\Lambda\,\Lambda_+\rangle_0]{{\rm local}}
\quad
2\sqrt2\,F(x)\,\delta^{(4)}(x-z)
}
$$

$$
\boxed{
\text{do not use the normalized }F\text{-collapse inside raw seed pages; use it only when converting }b_{L,{\rm raw}},b_{R,{\rm raw}}.
}
$$
