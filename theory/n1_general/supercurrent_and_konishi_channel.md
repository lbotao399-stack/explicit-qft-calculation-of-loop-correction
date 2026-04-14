---
title: "N=1 General: ordinary-space action, supercurrent, and Q_-"
doc_type: theory
theory: "N=1 General"
status: canonical
---

# N=1 General: ordinary-space action, supercurrent, and Q_-

固定 Wess-Zumino gauge、two-component Weyl notation。先写最一般 superspace form；真正做 Noether derivation 时 specialize 到 canonical Kähler + constant gauge kinetic function。

## Conventions

$$
\eta_{\mu\nu}=\mathrm{diag}(1,-1,-1,-1),\qquad
\sigma^\mu=(1,\vec \sigma),\qquad
\bar\sigma^\mu=(1,-\vec \sigma),
$$

$$
\sigma^{\mu\nu}:=\frac14(\sigma^\mu\bar\sigma^\nu-\sigma^\nu\bar\sigma^\mu),\qquad
\bar\sigma^{\mu\nu}:=\frac14(\bar\sigma^\mu\sigma^\nu-\bar\sigma^\nu\sigma^\mu).
$$

Gauge generators 取 Hermitian:
$$
[T^a,T^b]=if^{abc}T^c.
$$

Covariant derivatives:
$$
D_\mu \phi^i=\partial_\mu\phi^i+igA_\mu^a (T^a)^i{}_j\phi^j,
$$

$$
D_\mu \psi^i=\partial_\mu\psi^i+igA_\mu^a (T^a)^i{}_j\psi^j,
$$

$$
D_\mu \lambda^a=\partial_\mu\lambda^a-gf^{abc}A_\mu^b\lambda^c.
$$

Field strength:
$$
F_{\mu\nu}^a=\partial_\mu A_\nu^a-\partial_\nu A_\mu^a-gf^{abc}A_\mu^bA_\nu^c.
$$

## 0. General \(\mathcal N=1\) gauge theory action and \(Q_-\)

### 0.1 Superspace general form

$$
S=\int d^4x\left[
\int d^4\theta\, K(\Phi^\dagger e^{2gV},\Phi)
+\left(
\int d^2\theta\,
\Big(
\frac14 f_{ab}(\Phi)\,W^{a\alpha}W^b_{\alpha}+W(\Phi)
\Big)
+\mathrm{h.c.}
\right)
\right].
$$

后面要做的 \(\mathcal N=4\) SYM 属于
$$
K=\Phi_i^\dagger e^{2gV}\Phi^i,\qquad
f_{ab}=\delta_{ab},
$$
所以 component derivation 只需 canonical case。

### 0.2 Component action, off-shell

Chiral multiplets:
$$
(\phi^i,\psi^i_\alpha,F^i),\qquad i=1,\dots,n_\chi.
$$

Vector multiplet:
$$
(A_\mu^a,\lambda^a_\alpha,\bar\lambda_{\dot\alpha}^a,D^a),\qquad a=1,\dots,\dim G.
$$

Lagrangian:
$$
\boxed{
\begin{aligned}
\mathcal L
&=
-\frac14 F_{\mu\nu}^aF^{a\mu\nu}
-i\,\bar\lambda^a\bar\sigma^\mu D_\mu\lambda^a
+\frac12 D^aD^a
\\[1mm]
&\quad
-D_\mu\phi_i^\dagger D^\mu\phi^i
-i\,\bar\psi_i\bar\sigma^\mu D_\mu\psi^i
+F_i^\dagger F^i
\\[1mm]
&\quad
+i\sqrt2\,g\,\phi_i^\dagger (T^a)^i{}_j\psi^j\lambda^a
-i\sqrt2\,g\,\bar\lambda^a\,\bar\psi_i (T^a)^i{}_j\phi^j
+g\,\phi_i^\dagger (T^a)^i{}_j\phi^j\,D^a
\\[1mm]
&\quad
-\frac12 W_{ij}(\phi)\,\psi^i\psi^j
-\frac12 W^{\dagger ij}(\phi^\dagger)\,\bar\psi_i\bar\psi_j
+F^iW_i(\phi)+F_i^\dagger W^{\dagger i}(\phi^\dagger).
\end{aligned}}
$$

其中
$$
W_i:=\frac{\partial W}{\partial \phi^i},\qquad
W_{ij}:=\frac{\partial^2 W}{\partial\phi^i\partial\phi^j}.
$$

Auxiliary equations:
$$
F^i=-W^{\dagger i},\qquad
F_i^\dagger=-W_i,\qquad
D^a=-g\,\phi_i^\dagger(T^a)^i{}_j\phi^j.
$$

### 0.3 SUSY transformations

写成
$$
\delta_\epsilon=\epsilon^\alpha Q_\alpha+\bar\epsilon_{\dot\alpha}\bar Q^{\dot\alpha}.
$$

#### Chiral multiplet

$$
\delta \phi^i=\sqrt2\,\epsilon\psi^i,
$$

$$
\delta \psi^i_\alpha
=
i\sqrt2\,(\sigma^\mu\bar\epsilon)_\alpha D_\mu\phi^i
+\sqrt2\,\epsilon_\alpha F^i,
$$

$$
\delta F^i
=
i\sqrt2\,\bar\epsilon\bar\sigma^\mu D_\mu\psi^i
+2g\,\bar\epsilon\bar\lambda^a (T^a\phi)^i.
$$

其共轭为
$$
\delta \phi_i^\dagger=\sqrt2\,\bar\epsilon\bar\psi_i,
$$

$$
\delta \bar\psi_{i\dot\alpha}
=
i\sqrt2\,(\bar\sigma^\mu\epsilon)_{\dot\alpha}D_\mu\phi_i^\dagger
+\sqrt2\,\bar\epsilon_{\dot\alpha}F_i^\dagger,
$$

$$
\delta F_i^\dagger
=
i\sqrt2\,\epsilon\sigma^\mu D_\mu\bar\psi_i
+2g\,(\phi^\dagger T^a)_i\,\epsilon\lambda^a.
$$

#### Vector multiplet

$$
\delta A_\mu^a
=
i\,\epsilon\sigma_\mu\bar\lambda^a
-i\,\lambda^a\sigma_\mu\bar\epsilon,
$$

$$
\delta \lambda^a_\alpha
=
(\sigma^{\mu\nu}\epsilon)_\alpha F_{\mu\nu}^a
+i\,\epsilon_\alpha D^a,
$$

$$
\delta \bar\lambda^a_{\dot\alpha}
=
(\bar\sigma^{\mu\nu}\bar\epsilon)_{\dot\alpha}F_{\mu\nu}^a
-i\,\bar\epsilon_{\dot\alpha}D^a,
$$

$$
\delta D^a
=
-\epsilon\sigma^\mu D_\mu\bar\lambda^a
+D_\mu\lambda^a\sigma^\mu\bar\epsilon.
$$

### 0.4 Define \(Q_-\)

取
$$
\epsilon^\alpha=\eta\,\delta^\alpha{}_{-},\qquad
\bar\epsilon_{\dot\alpha}=0.
$$

则
$$
\delta_-=\eta\,Q_-.
$$

所以 \(Q_-\) 就是上面所有变换中只保留 \(\epsilon^-\) 的那一支。后面要用的 self-dual field strength \(F_{\alpha\beta}^a\) 满足
$$
\boxed{
Q_-\,F_{++}^a=i\,D_{+\dot\alpha}\bar\lambda^{a\dot\alpha}.
}
$$

## 1. Noether theorem: derive \(J^\mu_-\) in general \(\mathcal N=1\) gauge theory

把 global SUSY parameter 局域化：
$$
\epsilon_\alpha\to \epsilon_\alpha(x),\qquad
\bar\epsilon_{\dot\alpha}\to \bar\epsilon_{\dot\alpha}(x).
$$

定义 supercurrent by
$$
\delta \mathcal L
=
(\partial_\mu\epsilon^\alpha)J^\mu_\alpha
+
(\partial_\mu\bar\epsilon_{\dot\alpha})\bar J^{\mu\dot\alpha}
+\partial_\mu(\cdots)
+\text{EOM terms}.
$$

supercurrent 有 improvement ambiguity:
$$
J^\mu_\alpha\to J^\mu_\alpha+\partial_\nu U^{[\nu\mu]}{}_\alpha.
$$

下面直接取 standard gauge-invariant improved current。

### 1.1 Chiral-multiplet contribution

把
$$
\delta \phi^i=\sqrt2\,\epsilon\psi^i,\qquad
\delta \psi^i_\alpha=\sqrt2\,\epsilon_\alpha F^i,\qquad
\delta \bar\psi_{i\dot\alpha}
=
i\sqrt2\,(\bar\sigma^\nu\epsilon)_{\dot\alpha}D_\nu\phi_i^\dagger
$$
代入
$$
\mathcal L_{\rm ch}
=
-D_\mu\phi_i^\dagger D^\mu\phi^i
-i\bar\psi_i\bar\sigma^\mu D_\mu\psi^i
+F_i^\dagger F^i
+F^iW_i+F_i^\dagger W^{\dagger i}
-\frac12W_{ij}\psi^i\psi^j
-\frac12W^{\dagger ij}\bar\psi_i\bar\psi_j,
$$
局域化 \(\epsilon(x)\) 后得到
$$
\boxed{
J^\mu_{{\rm ch},\alpha}
=
\sqrt2\,D_\nu\phi_i^\dagger\,(\sigma^\nu\bar\sigma^\mu\psi^i)_\alpha
+i\sqrt2\,F^i\,(\sigma^\mu\bar\psi_i)_\alpha.
}
$$

### 1.2 Vector-multiplet contribution

把
$$
\delta A_\mu^a=i\epsilon\sigma_\mu\bar\lambda^a,
\qquad
\delta\lambda^a_\alpha=(\sigma^{\rho\sigma}\epsilon)_\alpha F_{\rho\sigma}^a+i\epsilon_\alpha D^a,
\qquad
\delta D^a=-\epsilon\sigma^\mu D_\mu\bar\lambda^a
$$
代入
$$
\mathcal L_{\rm vec}
=
-\frac14F_{\mu\nu}^aF^{a\mu\nu}
-i\bar\lambda^a\bar\sigma^\mu D_\mu\lambda^a
+\frac12D^aD^a,
$$
局域化 \(\epsilon(x)\) 后得到
$$
\boxed{
J^\mu_{{\rm vec},\alpha}
=
-i\,F_{\nu\rho}^a\,(\sigma^{\nu\rho}\sigma^\mu\bar\lambda^a)_\alpha
+D^a\,(\sigma^\mu\bar\lambda^a)_\alpha.
}
$$

### 1.3 Full off-shell supercurrent

$$
\boxed{
J^\mu_\alpha
=
\sqrt2\,D_\nu\phi_i^\dagger\,(\sigma^\nu\bar\sigma^\mu\psi^i)_\alpha
+i\sqrt2\,F^i\,(\sigma^\mu\bar\psi_i)_\alpha
-i\,F_{\nu\rho}^a\,(\sigma^{\nu\rho}\sigma^\mu\bar\lambda^a)_\alpha
+D^a\,(\sigma^\mu\bar\lambda^a)_\alpha.
}
$$

其共轭为
$$
\boxed{
\bar J^{\mu}{}_{\dot\alpha}
=
\sqrt2\,D_\nu\phi^i\,(\bar\sigma^\nu\sigma^\mu\bar\psi_i)_{\dot\alpha}
-i\sqrt2\,F_i^\dagger\,(\psi^i\sigma^\mu)_{\dot\alpha}
+i\,F_{\nu\rho}^a\,(\lambda^a\sigma^\mu\bar\sigma^{\nu\rho})_{\dot\alpha}
+D^a\,(\lambda^a\sigma^\mu)_{\dot\alpha}.
}
$$

supercharge 为
$$
Q_\alpha=\int d^3x\,J^0_\alpha,\qquad
\bar Q_{\dot\alpha}=\int d^3x\,\bar J^0_{\dot\alpha}.
$$

### 1.4 On-shell form

代入
$$
F^i=-W^{\dagger i},\qquad D^a=-g\,\phi_i^\dagger(T^a)^i{}_j\phi^j,
$$
得到 on-shell current
$$
\boxed{
J^\mu_\alpha
=
\sqrt2\,D_\nu\phi_i^\dagger\,(\sigma^\nu\bar\sigma^\mu\psi^i)_\alpha
-i\sqrt2\,W^{\dagger i}\,(\sigma^\mu\bar\psi_i)_\alpha
-i\,F_{\nu\rho}^a\,(\sigma^{\nu\rho}\sigma^\mu\bar\lambda^a)_\alpha
-g\,\phi_i^\dagger(T^a)^i{}_j\phi^j\,(\sigma^\mu\bar\lambda^a)_\alpha.
}
$$

满足
$$
\partial_\mu J^\mu_\alpha=0
$$
在 field equations 成立时严格守恒。

### 1.5 The \(Q_-\) current

取 \(\alpha=-\)：
$$
\boxed{
J^\mu_-
=
\sqrt2\,D_\nu\phi_i^\dagger\,(\sigma^\nu\bar\sigma^\mu\psi^i)_-
+i\sqrt2\,F^i\,(\sigma^\mu\bar\psi_i)_-
-i\,F_{\nu\rho}^a\,(\sigma^{\nu\rho}\sigma^\mu\bar\lambda^a)_-
+D^a\,(\sigma^\mu\bar\lambda^a)_-.
}
$$

on-shell:
$$
\boxed{
J^\mu_-
=
\sqrt2\,D_\nu\phi_i^\dagger\,(\sigma^\nu\bar\sigma^\mu\psi^i)_-
-i\sqrt2\,W^{\dagger i}\,(\sigma^\mu\bar\psi_i)_-
-i\,F_{\nu\rho}^a\,(\sigma^{\nu\rho}\sigma^\mu\bar\lambda^a)_-
-g\,\phi_i^\dagger(T^a)^i{}_j\phi^j\,(\sigma^\mu\bar\lambda^a)_-.
}
$$

## 2. For later \(\mathcal N=4\) SYM

把三个 chiral multiplets 都取 adjoint:
$$
\Phi^I=\Phi^{Ia}T^a,\qquad I=1,2,3,
$$

$$
W=\frac{g}{3!}\,\epsilon_{IJK}f^{abc}\,\Phi^{Ia}\Phi^{Jb}\Phi^{Kc}.
$$

于是上面的 general \(\mathcal N=1\) result 直接 specialize 到 \(\mathcal N=4\) SYM；后面 ordinary-space 的
\[
Q_-(FF),\qquad Q_1(F^A F^B),\qquad \text{triangle diagram}
\]
都从这里出发。
