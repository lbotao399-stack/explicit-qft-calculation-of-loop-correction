---
title: "N=1 SYM (Euclidean): conventions and rules"
doc_type: theory
theory: "N=1 SYM (Euclidean)"
status: canonical
---

# N=1 SYM (Euclidean): conventions and rules

这份文档只收录当前 `N=1 SYM (Euclidean)` 显式计算真正调用的记号、raw SUSY、free EOM、`Q_-`-BPS letters 和 Feynman rules。

## Background and field content

取 **flat Euclidean** $\mathbb R^4$，$\mathrm{Spin}(4)=SU(2)_+\times SU(2)_-$，**WZ gauge, off-shell**。

**Vector multiplet**

$$
																																																		(A_{\alpha\dot\alpha},\,\lambda_\alpha,\,\widetilde\lambda_{\dot\alpha},\,\mathcal D),\qquad
\widetilde\lambda_{\dot\alpha}\equiv \bar\lambda_{\dot\alpha}\ \text{只是记号，不是 complex conjugate}.
$$

所有场均为 adjoint-valued。$D_{\alpha\dot\alpha}$ 是 covariant derivative，$\mathcal D$ 是 auxiliary scalar。

### 1. Spinor / vector conventions

$$
\alpha,\beta=\pm,\qquad \dot\alpha,\dot\beta=\dot\pm.
$$

$$
																																																																											\epsilon_{+-}=\epsilon_{\dot+\dot-}=1,\qquad
\epsilon_{-+}=\epsilon_{\dot-\dot+}=-1.
$$

$$
																																																																											\epsilon^{-+}=\epsilon^{\dot-\dot+}=1,\qquad
\epsilon^{+-}=\epsilon^{\dot+\dot-}=-1.
$$

$$
																																																																											\psi^\alpha=\epsilon^{\alpha\beta}\psi_\beta,\qquad
\psi_\alpha=\epsilon_{\alpha\beta}\psi^\beta,\qquad
\widetilde\psi^{\dot\alpha}=\epsilon^{\dot\alpha\dot\beta}\widetilde\psi_{\dot\beta},\qquad
\widetilde\psi_{\dot\alpha}=\epsilon_{\dot\alpha\dot\beta}\widetilde\psi^{\dot\beta}.
$$

NW-SE contraction:

$$
																																																																											\psi\chi:=\psi^\alpha\chi_\alpha,\qquad
\widetilde\psi\widetilde\chi:=\widetilde\psi_{\dot\alpha}\widetilde\chi^{\dot\alpha}.
$$

对 Grassmann-odd spinors:

$$
																																																																											\psi\chi=\chi\psi,\qquad
\widetilde\psi\widetilde\chi=\widetilde\chi\widetilde\psi,\qquad
\psi\sigma^\mu\widetilde\chi=-\,\widetilde\chi\bar\sigma^\mu\psi.
$$

取

$$
																																																																											\sigma^\mu_{\alpha\dot\alpha}=(i\tau^1,\ i\tau^2,\ i\tau^3,\ \mathbf 1),\qquad
\bar\sigma^{\mu,\dot\alpha\alpha}=(-i\tau^1,\ -i\tau^2,\ -i\tau^3,\ \mathbf 1).
$$

$$
\bar\sigma^{\mu,\dot\alpha\alpha}=\epsilon^{\dot\alpha\dot\beta}\epsilon^{\alpha\beta}\sigma^\mu_{\beta\dot\beta}.
$$

$$
																																																																											\sigma^\mu_{\alpha\dot\alpha}\bar\sigma^{\nu,\dot\alpha\beta}
+\sigma^\nu_{\alpha\dot\alpha}\bar\sigma^{\mu,\dot\alpha\beta}
=2\delta^{\mu\nu}\delta_\alpha{}^\beta.
$$

$$
																																																																											\bar\sigma^{\mu,\dot\alpha\alpha}\sigma^\nu_{\alpha\dot\beta}
+\bar\sigma^{\nu,\dot\alpha\alpha}\sigma^\mu_{\alpha\dot\beta}
=2\delta^{\mu\nu}\delta^{\dot\alpha}{}_{\dot\beta}.
$$

$$
\sigma^\mu_{\alpha\dot\alpha}\sigma_{\mu,\beta\dot\beta}=2\epsilon_{\alpha\beta}\epsilon_{\dot\alpha\dot\beta}.
$$

vector $\leftrightarrow$ bispinor:

$$
																																																																											v_{\alpha\dot\alpha}=\sigma^\mu_{\alpha\dot\alpha}v_\mu,\qquad
v_\mu=\frac12\bar\sigma_\mu^{\dot\alpha\alpha}v_{\alpha\dot\alpha},\qquad
u\cdot v=\frac12 u^{\alpha\dot\alpha}v_{\alpha\dot\alpha}.
$$

显式矩阵：

$$
																																																																											v_{\alpha\dot\alpha}=
\begin{pmatrix}
v_4+i v_3 & i v_1+v_2\\[2mm]
i v_1-v_2 & v_4-i v_3
\end{pmatrix}.
$$

特别地

$$
																																																																											A_{\alpha\dot\alpha}=
\begin{pmatrix}
A_4+iA_3 & iA_1+A_2\\[2mm]
iA_1-A_2 & A_4-iA_3
\end{pmatrix},\qquad
\partial_{\alpha\dot\alpha}=
\begin{pmatrix}
\partial_4+i\partial_3 & i\partial_1+\partial_2\\[2mm]
i\partial_1-\partial_2 & \partial_4-i\partial_3
\end{pmatrix}.
$$

$$
																																																																											(\sigma^{\mu\nu})_\alpha{}^\beta:=\frac14(\sigma^\mu\bar\sigma^\nu-\sigma^\nu\bar\sigma^\mu)_\alpha{}^\beta,\qquad
(\bar\sigma^{\mu\nu})^{\dot\alpha}{}_{\dot\beta}:=\frac14(\bar\sigma^\mu\sigma^\nu-\bar\sigma^\nu\sigma^\mu)^{\dot\alpha}{}_{\dot\beta}.
$$

$$
																																																																											(\sigma^{\mu\nu})_{\alpha\beta}:=(\sigma^{\mu\nu})_\alpha{}^\gamma\epsilon_{\gamma\beta}=(\sigma^{\mu\nu})_{\beta\alpha},\qquad
(\bar\sigma^{\mu\nu})_{\dot\alpha\dot\beta}:=\epsilon_{\dot\alpha\dot\gamma}(\bar\sigma^{\mu\nu})^{\dot\gamma}{}_{\dot\beta}=(\bar\sigma^{\mu\nu})_{\dot\beta\dot\alpha}.
$$

$$
																																																																											\frac12\epsilon^{\mu\nu\rho\sigma}\sigma_{\rho\sigma}=+\sigma^{\mu\nu},\qquad
\frac12\epsilon^{\mu\nu\rho\sigma}\bar\sigma_{\rho\sigma}=-\bar\sigma^{\mu\nu},\qquad
\epsilon^{1234}=1.
$$

symmetrization:

$$
																																																																											X_{(\alpha\beta)}:=\frac12(X_{\alpha\beta}+X_{\beta\alpha}),\qquad
X_{(\alpha|\dot\gamma|\beta)}:=\frac12(X_{\alpha\dot\gamma\beta}+X_{\beta\dot\gamma\alpha}).
$$

### 2. Gauge field, field strength, self-dual / anti-self-dual split

$$
																																																																											D_\mu=\partial_\mu+[A_\mu,\ \cdot\ ],\qquad
D_{\alpha\dot\alpha}=\sigma^\mu_{\alpha\dot\alpha}D_\mu.
$$

$$
F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu+[A_\mu,A_\nu].
$$

$$
																																																																											F_{\alpha\dot\alpha,\beta\dot\beta}:=[D_{\alpha\dot\alpha},D_{\beta\dot\beta}]
=\epsilon_{\dot\alpha\dot\beta}f_{\alpha\beta}+\epsilon_{\alpha\beta}\bar f_{\dot\alpha\dot\beta}.
$$

$$
																																																																											f_{\alpha\beta}=f_{\beta\alpha}
=\frac12\epsilon^{\dot\alpha\dot\beta}F_{\alpha\dot\alpha,\beta\dot\beta}
=(\sigma^{\mu\nu})_{\alpha\beta}F_{\mu\nu}.
$$

$$
																																																																											\bar f_{\dot\alpha\dot\beta}=\bar f_{\dot\beta\dot\alpha}
=\frac12\epsilon^{\alpha\beta}F_{\alpha\dot\alpha,\beta\dot\beta}
=(\bar\sigma^{\mu\nu})_{\dot\alpha\dot\beta}F_{\mu\nu}.
$$

$$
																																																																											F^{(+)}_{\alpha\dot\alpha,\beta\dot\beta}=\epsilon_{\dot\alpha\dot\beta}f_{\alpha\beta},\qquad
F^{(-)}_{\alpha\dot\alpha,\beta\dot\beta}=\epsilon_{\alpha\beta}\bar f_{\dot\alpha\dot\beta}.
$$

分量写开：

$$
																																																																											f_{\alpha\beta}=
\begin{pmatrix}
f_{++} & f_{+-}\\
f_{+-} & f_{--}
\end{pmatrix},\qquad
\bar f_{\dot\alpha\dot\beta}=
\begin{pmatrix}
\bar f_{\dot+\dot+} & \bar f_{\dot+\dot-}\\
\bar f_{\dot+\dot-} & \bar f_{\dot-\dot-}
\end{pmatrix}.
$$

用上面 $\sigma^\mu$ 约定，显式有

$$
f_{++}=\frac12(F_{13}-F_{24}-iF_{14}-iF_{23}).
$$

$$
f_{+-}=\frac{i}{2}(F_{12}+F_{34}).
$$

$$
f_{--}=\frac12(F_{13}-F_{24}+iF_{14}+iF_{23}).
$$

$$
\bar f_{\dot+\dot+}=\frac12(F_{13}+F_{24}-iF_{14}+iF_{23}).
$$

$$
\bar f_{\dot+\dot-}=\frac{i}{2}(-F_{12}+F_{34}).
$$

$$
\bar f_{\dot-\dot-}=\frac12(F_{13}+F_{24}+iF_{14}-iF_{23}).
$$

### 3. Euclidean $\mathcal N=1$ SUSY, off-shell, 不代 EOM

SUSY parameter:

$$
																																																																											(\zeta_\alpha,\widetilde\zeta_{\dot\alpha}),\qquad
\delta=\zeta^\alpha Q_\alpha+\widetilde\zeta^{\dot\alpha}\widetilde Q_{\dot\alpha}.
$$

基本变换：

$$
\delta A_{\alpha\dot\alpha}= i\zeta_\alpha\widetilde\lambda_{\dot\alpha}+i\widetilde\zeta_{\dot\alpha}\lambda_\alpha.
$$

$$
\delta\lambda_\alpha=f_{\alpha\beta}\zeta^\beta+i\zeta_\alpha\mathcal D.
$$

$$
\delta\widetilde\lambda_{\dot\alpha}=\bar f_{\dot\alpha\dot\beta}\widetilde\zeta^{\dot\beta}-i\widetilde\zeta_{\dot\alpha}\mathcal D.
$$

$$
\delta\mathcal D=-\zeta^\alpha D_{\alpha\dot\alpha}\widetilde\lambda^{\dot\alpha}+\widetilde\zeta^{\dot\alpha}D_{\alpha\dot\alpha}\lambda^\alpha.
$$

对 field strength 的变换（由 $\delta A$ 推出，不代 EOM）：

$$
																																																																											\delta f_{\alpha\beta}
=i\zeta_{(\alpha}D_{\beta)\dot\gamma}\widetilde\lambda^{\dot\gamma}
+i\widetilde\zeta^{\dot\gamma}D_{(\alpha|\dot\gamma|}\lambda_{\beta)}.
$$

$$
																																																																											\delta \bar f_{\dot\alpha\dot\beta}
=i\widetilde\zeta_{(\dot\alpha}D_{\gamma\dot\beta)}\lambda^\gamma
+i\zeta^\gamma D_{\gamma(\dot\alpha}\widetilde\lambda_{\dot\beta)}.
$$

写成 $(++,+- ,--)$ 分量：

$$
\delta f_{++}= i\zeta_+ D_{+\dot\alpha}\widetilde\lambda^{\dot\alpha}+i\widetilde\zeta^{\dot\alpha}D_{+\dot\alpha}\lambda_+.
$$

$$
																																																																											\delta f_{+-}=\frac{i}{2}\Big(
\zeta_+ D_{-\dot\alpha}\widetilde\lambda^{\dot\alpha}
+\zeta_- D_{+\dot\alpha}\widetilde\lambda^{\dot\alpha}
+\widetilde\zeta^{\dot\alpha}D_{+\dot\alpha}\lambda_-
+\widetilde\zeta^{\dot\alpha}D_{-\dot\alpha}\lambda_+
\Big).
$$

$$
\delta f_{--}= i\zeta_- D_{-\dot\alpha}\widetilde\lambda^{\dot\alpha}+i\widetilde\zeta^{\dot\alpha}D_{-\dot\alpha}\lambda_-.
$$

$$
\delta \bar f_{\dot+\dot+}= i\widetilde\zeta_{\dot+}D_{\alpha\dot+}\lambda^\alpha+i\zeta^\alpha D_{\alpha\dot+}\widetilde\lambda_{\dot+}.
$$

$$
																																																																											\delta \bar f_{\dot+\dot-}=\frac{i}{2}\Big(
\widetilde\zeta_{\dot+}D_{\alpha\dot-}\lambda^\alpha
+\widetilde\zeta_{\dot-}D_{\alpha\dot+}\lambda^\alpha
+\zeta^\alpha D_{\alpha\dot+}\widetilde\lambda_{\dot-}
+\zeta^\alpha D_{\alpha\dot-}\widetilde\lambda_{\dot+}
\Big).
$$

$$
\delta \bar f_{\dot-\dot-}= i\widetilde\zeta_{\dot-}D_{\alpha\dot-}\lambda^\alpha+i\zeta^\alpha D_{\alpha\dot-}\widetilde\lambda_{\dot-}.
$$

若要 compact 的 closure 公式：

$$
[\delta_1,\delta_2]=v^{\alpha\dot\alpha}D_{\alpha\dot\alpha}+\delta_{\rm gauge}(\omega),
$$

$$
																																																																											v_{\alpha\dot\alpha}=2i(\zeta_{2\alpha}\widetilde\zeta_{1\dot\alpha}-\zeta_{1\alpha}\widetilde\zeta_{2\dot\alpha}),\qquad
\omega=-v^{\beta\dot\beta}A_{\beta\dot\beta}.
$$

### 4. Gauge transformation 与 BRST gauge fixing

ordinary gauge transformation, parameter $\omega$:

$$
\delta_\omega A_{\alpha\dot\alpha}=D_{\alpha\dot\alpha}\omega.
$$

$$
																																																																											\delta_\omega \lambda_\alpha=[\lambda_\alpha,\omega],\qquad
\delta_\omega \widetilde\lambda_{\dot\alpha}=[\widetilde\lambda_{\dot\alpha},\omega],\qquad
\delta_\omega \mathcal D=[\mathcal D,\omega].
$$

$$
																																																																											\delta_\omega f_{\alpha\beta}=[f_{\alpha\beta},\omega],\qquad
\delta_\omega \bar f_{\dot\alpha\dot\beta}=[\bar f_{\dot\alpha\dot\beta},\omega].
$$

引入 ghost / antighost / Nakanishi–Lautrup:

$$
c,\ \bar c\ \text{Grassmann-odd},\qquad b\ \text{Grassmann-even}.
$$

BRST operator $s$:

$$
sA_{\alpha\dot\alpha}=D_{\alpha\dot\alpha}c.
$$

$$
																																																																											s\lambda_\alpha=[\lambda_\alpha,c],\qquad
s\widetilde\lambda_{\dot\alpha}=[\widetilde\lambda_{\dot\alpha},c],\qquad
s\mathcal D=[\mathcal D,c].
$$

$$
																																																																											sf_{\alpha\beta}=[f_{\alpha\beta},c],\qquad
s\bar f_{\dot\alpha\dot\beta}=[\bar f_{\dot\alpha\dot\beta},c].
$$

$$
																																																																											sc=-\frac12[c,c]=-c^2,\qquad
s\bar c=b,\qquad
sb=0,\qquad
s^2=0.
$$

Lorenz gauge 的 gauge-fixing fermion:

$$
																																																																											\Psi=\int d^4x\ \operatorname{Tr}\,\bar c\Big(\partial^\mu A_\mu+\frac{\xi}{2}b\Big)
=\int d^4x\ \operatorname{Tr}\,\bar c\Big(\frac12\partial^{\alpha\dot\alpha}A_{\alpha\dot\alpha}+\frac{\xi}{2}b\Big).
$$

$$
S_{\rm gf+gh}=s\Psi.
$$

$$
\mathcal L_{\rm gf+gh}=\operatorname{Tr}\Big(b\,\partial^\mu A_\mu+\frac{\xi}{2}b^2-\bar c\,\partial^\mu D_\mu c\Big),
$$

或等价地

$$
																																																																											\mathcal L_{\rm gf+gh}=\operatorname{Tr}\Big(
\frac12 b\,\partial^{\alpha\dot\alpha}A_{\alpha\dot\alpha}
+\frac{\xi}{2}b^2
-\frac12\bar c\,\partial^{\alpha\dot\alpha}D_{\alpha\dot\alpha}c
\Big).
$$

若把 SYM 本体也一并写上，一套常用 normalization 是

$$
\mathcal L_{\rm SYM}=\frac1{g^2}\operatorname{Tr}\Big(\frac14 F_{\mu\nu}F_{\mu\nu}+\widetilde\lambda_{\dot\alpha}D^{\dot\alpha\alpha}\lambda_\alpha+\frac12\mathcal D^2\Big).
$$

$$
\mathcal L_{\rm tot}=\mathcal L_{\rm SYM}+\mathcal L_{\rm gf+gh}.
$$

若你记号里坚持用 $(\bar\lambda,\bar\zeta)$，直接替换

$$
																																																																											\widetilde\lambda_{\dot\alpha}\mapsto \bar\lambda_{\dot\alpha},\qquad
\widetilde\zeta_{\dot\alpha}\mapsto \bar\zeta_{\dot\alpha}
$$

即可，其他公式不变。

### $Q_-$ 的取法

$$
																																																Q_-:\quad \zeta^-=1,\ \zeta^+=0,\ \widetilde\zeta^{\dot\alpha}=0,\qquad
\zeta_+=1,\ \zeta_-=0,\qquad g=0.
$$

取 $H_{\rm BRST}^0$ 的 gauge-covariant letters；$A_{\alpha\dot\alpha}$ 不算 basic letter。在 raw basis 下，

$$
Q_-A_{+\dot\alpha}=i\bar\lambda_{\dot\alpha}=2\kappa_A\,\bar\lambda_{\dot\alpha}.
$$

$$
\nabla_{\alpha\dot\alpha}:=D_{\alpha\dot\alpha}.
$$

### $Q_-$ 的作用( at g=0)

$$
																																																Q_-\bar\lambda_{\dot\alpha}=0,\qquad
Q_-\lambda_+=f_{+-}+i\mathcal D,\qquad
Q_-\lambda_-=f_{--}.
$$

$$
Q_-\mathcal D=-\partial_{-\dot\alpha}\bar\lambda^{\dot\alpha}.
$$

$$
																																																Q_-f_{++}=i\partial_{+\dot\alpha}\bar\lambda^{\dot\alpha},\qquad
Q_-f_{+-}=\frac{i}{2}\partial_{-\dot\alpha}\bar\lambda^{\dot\alpha},\qquad
Q_-f_{--}=0.
$$

$$
Q_-\bar f_{\dot\alpha\dot\beta}=i\partial_{-(\dot\alpha}\bar\lambda_{\dot\beta)}.
$$

### $Q_-$ projected working coefficient

$$
\delta_{Q_-}^{\rm cl}A_{+\dot\alpha}=\kappa_A\,\bar\lambda_{\dot\alpha},
\qquad
\delta_{Q_-}^{\rm cl}A_{-\dot\alpha}=0,
\qquad
\delta_{Q_-}^{\rm cl}\bar\lambda_{\dot\alpha}=0.
$$

$$
\delta_{Q_-}^{\rm cl}f_{++}=2\kappa_A\,\nabla_{+\dot\beta}\bar\lambda^{\dot\beta}.
$$

$$
\boxed{
\kappa_A:=\frac12\,\text{coeff}\Big(\delta_{Q_-}^{\rm cl}f_{++},\ \nabla_{+\dot\beta}\bar\lambda^{\dot\beta}\Big)
\qquad\Longrightarrow\qquad
\kappa_A=\frac{i}{2}
}
$$

$$
[\delta_{Q_-}^{\rm cl},\nabla_{\alpha\dot\alpha}]X
=
\operatorname{ad}_{\delta_{Q_-}^{\rm cl}A_{\alpha\dot\alpha}}X,
\qquad
\operatorname{ad}_Y(X)^a:=f^{abc}Y^bX^c.
$$

$$
[\delta_{Q_-}^{\rm cl},\nabla_{+\dot\alpha}]
=
\kappa_A\,\operatorname{ad}_{\bar\lambda_{\dot\alpha}},
\qquad
[\delta_{Q_-}^{\rm cl},\nabla_{-\dot\alpha}]=0.
$$

$$
\delta_{Q_-}^{\rm cl}(\nabla_{+\dot\alpha}X)
=
\nabla_{+\dot\alpha}(\delta_{Q_-}^{\rm cl}X)
+
\kappa_A\,\operatorname{ad}_{\bar\lambda_{\dot\alpha}}X,
$$

$$
\delta_{Q_-}^{\rm cl}(\nabla_{-\dot\alpha}X)
=
\nabla_{-\dot\alpha}(\delta_{Q_-}^{\rm cl}X).
$$

$$
\delta_{Q_-}^{\rm cl}(\nabla_{+\dot\alpha}f_{++})
=
2\kappa_A\,\nabla_{+\dot\alpha}\nabla_{+\dot\beta}\bar\lambda^{\dot\beta}
+
\kappa_A\,\operatorname{ad}_{\bar\lambda_{\dot\alpha}}f_{++},
$$

$$
\delta_{Q_-}^{\rm cl}(\nabla_{+\dot\alpha}\bar\lambda_{\dot\beta})
=
\kappa_A\,\operatorname{ad}_{\bar\lambda_{\dot\alpha}}\bar\lambda_{\dot\beta}.
$$

$$
\delta_{Q_-}^{\rm cl}(\nabla_{-\dot\alpha}f_{++})
=
2\kappa_A\,\nabla_{-\dot\alpha}\nabla_{+\dot\beta}\bar\lambda^{\dot\beta},
\qquad
\delta_{Q_-}^{\rm cl}(\nabla_{-\dot\alpha}\bar\lambda_{\dot\beta})=0.
$$

$$
\delta_{Q_-}^{\rm cl}\!\big(e^{w\cdot\nabla_+}X\big)
=
e^{w\cdot\nabla_+}\big(\delta_{Q_-}^{\rm cl}X\big)
+
\kappa_A
\int_0^1 ds\;
e^{s w\cdot\nabla_+}
\Big(
w^{\dot\alpha}\operatorname{ad}_{\bar\lambda_{\dot\alpha}}
\Big)
e^{(1-s) w\cdot\nabla_+}X.
$$

$$
\delta_{Q_-}^{\rm cl}\!\big(e^{w\cdot\nabla_+}f_{++}\big)
=
2\kappa_A\,e^{w\cdot\nabla_+}\nabla_{+\dot\beta}\bar\lambda^{\dot\beta}
+
\kappa_A
\int_0^1 ds\;
e^{s w\cdot\nabla_+}
\Big(
w^{\dot\alpha}\operatorname{ad}_{\bar\lambda_{\dot\alpha}}
\Big)
e^{(1-s) w\cdot\nabla_+}f_{++},
$$

$$
\delta_{Q_-}^{\rm cl}\!\big(e^{w\cdot\nabla_+}\bar\lambda_{\dot\beta}\big)
=
\kappa_A
\int_0^1 ds\;
e^{s w\cdot\nabla_+}
\Big(
w^{\dot\alpha}\operatorname{ad}_{\bar\lambda_{\dot\alpha}}
\Big)
e^{(1-s) w\cdot\nabla_+}\bar\lambda_{\dot\beta}.
$$

### Free EOM

$$
																																																\partial_{+\dot\alpha}\bar\lambda^{\dot\alpha}=0,\qquad
\partial_{-\dot\alpha}\bar\lambda^{\dot\alpha}=0,\qquad
\mathcal D=0.
$$

$$
																																																Q_-f_{++}=0,\qquad
Q_-f_{+-}=0,\qquad
f_{+-}=Q_-\lambda_+,\qquad
f_{--}=Q_-\lambda_-.
$$

$$
																																																\ker Q_-\cap\{\bar\lambda_{\dot\alpha},f_{\alpha\beta}\}
=
\{\bar\lambda_{\dot+},\bar\lambda_{\dot-},f_{++},f_{+-},f_{--}\}.
$$

$$
																																																\operatorname{Im}Q_-\cap\{\bar\lambda_{\dot\alpha},f_{\alpha\beta}\}
=
\{f_{+-},f_{--}\}.
$$

### $Q_-$ BPS letters

$$
																																																\boxed{
H^0(Q_-;H_{\rm BRST}^0)_{\rm letters}
=
\{\bar\lambda_{\dot+},\ \bar\lambda_{\dot-},\ f_{++}\}
}.
$$

### Derivative letters

$$
																																																\{Q_-,\widetilde Q_{\dot\alpha}\}=2i\partial_{-\dot\alpha}
\quad\Longrightarrow\quad
\partial_{-\dot\alpha}\mathcal O\in\operatorname{Im}Q_-.
$$

所以只保留 $\partial_{+\dot\alpha}$ descendants：

$$
																																																\partial_{+\dot+}^m\partial_{+\dot-}^n\bar\lambda_{\dot\beta},\qquad
\partial_{+\dot+}^m\partial_{+\dot-}^n f_{++}.
$$

并且(free level)

$$
																																																\partial_{+\dot-}\bar\lambda_{\dot+}
=
\partial_{+\dot+}\bar\lambda_{\dot-}.
$$

### Feynman rules

按本页记号，rescale 到 canonical，取 $(xi=1)$、all incoming；vertex factor 按 $(S_E)$ 取，定义

$$
\int_q:=\int \frac{d^4q}{(2\pi)^4}.
$$

代数约定：

$$
[T^a,T^b]=f^{abc}T^c,\qquad \operatorname{Tr}(T^aT^b)=\delta^{ab}.
$$

场强与协变导数：

$$
																																														F_{\mu\nu}^a=\partial_\mu A_\nu^a-\partial_\nu A_\mu^a+g f^{abc}A_\mu^bA_\nu^c,\qquad
(D_\mu X)^a=\partial_\mu X^a+g f^{abc}A_\mu^bX^c.
$$

欧式拉氏量：

$$
\mathcal L_E=\frac14F_{\mu\nu}^aF_{\mu\nu}^a+\bar\lambda_{\dot\alpha}^a\bar\sigma^{\mu,\dot\alpha\alpha}(D_\mu\lambda_\alpha)^a+(\partial_\mu\bar c^a)(D_\mu c)^a+\frac12(\partial_\mu A_\mu^a)^2+\frac12\mathcal D^a\mathcal D^a.
$$

Propagators：

$$
																																														\langle A_\mu^a(p)A_\nu^b(-p)\rangle=\frac{\delta^{ab}\delta_{\mu\nu}}{p^2},\qquad
\langle A_{\alpha\dot\alpha}^a(p)A_{\beta\dot\beta}^b(-p)\rangle=\frac{2\delta^{ab}\epsilon_{\alpha\beta}\epsilon_{\dot\alpha\dot\beta}}{p^2}.
$$

$$
																																														\langle \lambda_\alpha^a(p)\bar\lambda_{\dot\beta}^b(-p)\rangle=-\frac{i\delta^{ab}p_{\alpha\dot\beta}}{p^2},\qquad
\langle\lambda\lambda\rangle=\langle\bar\lambda\bar\lambda\rangle=0.
$$

$$
																																															\langle c^a(p)\bar c^b(-p)\rangle=\frac{\delta^{ab}}{p^2},\qquad
\langle \mathcal D^a(p)\mathcal D^b(-p)\rangle=\delta^{ab}.
$$

$$
D(q):=\frac{1}{q^2},\qquad
\big[S(q)P_L\big]_{\alpha\dot\alpha}:=-\frac{i\,\widetilde q_{\alpha\dot\alpha}}{q^2}.
$$

$$
D_M(q):=\frac{1}{q^2+M^2},\qquad
\big[S_M(q)P_L\big]_{\alpha\dot\alpha}:=-\frac{i\,q_{\alpha\dot\alpha}}{q^2+M^2}.
$$

Vertices：

$$
																																														V^{abc}_{A\lambda\bar\lambda,\mu}=g f^{abc}\bar\sigma_\mu,\qquad
V^{abc}_{\bar cAc,\mu}(p_{\bar c})=g f^{abc}p_{\bar c,\mu}.
$$

$$
V^{abc}_{AAA,\mu\nu\rho}(p,q,r)=g f^{abc}\big[\delta_{\mu\nu}(p-q)_\rho+\delta_{\nu\rho}(q-r)_\mu+\delta_{\rho\mu}(r-p)_\nu\big].
$$

$$
																																														\begin{aligned}
V^{abcd}_{AAAA,\mu\nu\rho\sigma}=g^2\Big[&f^{abe}f^{cde}(\delta_{\mu\rho}\delta_{\nu\sigma}-\delta_{\mu\sigma}\delta_{\nu\rho})\\
&+f^{ace}f^{bde}(\delta_{\mu\nu}\delta_{\rho\sigma}-\delta_{\mu\sigma}\delta_{\nu\rho})\\
&+f^{ade}f^{bce}(\delta_{\mu\nu}\delta_{\rho\sigma}-\delta_{\mu\rho}\delta_{\nu\sigma})\Big].
\end{aligned}
$$

Insertions：

$$
																																														\mathcal I[f_{\alpha\beta}^a(p)]
=i(\sigma^{\mu\nu})_{\alpha\beta}(p_\mu A_\nu^a-p_\nu A_\mu^a)
+g(\sigma^{\mu\nu})_{\alpha\beta}f^{abc}\int_q A_\mu^b(q)A_\nu^c(p-q).
$$

$$
																																														\mathcal I[f_{++}^a(p)]
=\frac{i}{2}\big(p_{+\dot+}A_{+\dot-}^a-p_{+\dot-}A_{+\dot+}^a\big)
+\frac{g}{2}f^{abc}\int_q A_{+\dot+}^b(q)A_{+\dot-}^c(p-q).
$$

$$
																																														\langle f_{++}^a(p)A_{-\dot\alpha}^b(-p)\rangle=-\frac{i\delta^{ab}p_{+\dot\alpha}}{p^2},\qquad
\langle f_{++}^a(p)f_{++}^b(-p)\rangle=\langle f_{++}^a(p)\bar\lambda_{\dot\alpha}^b(-p)\rangle=0.
$$

$$
																																														\mathcal I[\partial_{+\dot\alpha}\bar\lambda_{\dot\beta}^a(p)]=i p_{+\dot\alpha}\bar\lambda_{\dot\beta}^a(p),\qquad
\mathcal I[\partial_{+\dot\alpha}f_{++}^a(p)]=i p_{+\dot\alpha}\mathcal I[f_{++}^a(p)].
$$
