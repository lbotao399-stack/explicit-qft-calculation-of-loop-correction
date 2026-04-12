# 直接1-loop level计算

# Fundamental definition

<aside>

## 取 **flat Euclidean** $\mathbb R^4$，$\mathrm{Spin}(4)=SU(2)_+\times SU(2)_-$，**WZ gauge, off-shell**。

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

</aside>

<aside>

### $Q_-$ 的取法

$$
																																																Q_-:\quad \zeta^-=1,\ \zeta^+=0,\ \widetilde\zeta^{\dot\alpha}=0,\qquad
\zeta_+=1,\ \zeta_-=0,\qquad g=0.
$$

取 $H_{\rm BRST}^0$ 的 gauge-covariant letters；$A_{\alpha\dot\alpha}$ 不算 basic letter。在 raw basis 下，

$$
Q_-A_{+\dot\alpha}=i\bar\lambda_{\dot\alpha}.
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

</aside>

<aside>

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

</aside>

# With matter

### 1. Matter + superpotential, component action

取一组 chiral multiplets

$$
\Phi^i=(\phi^i,\psi^i_\alpha,F^i),\qquad
\widetilde\Phi_i=(\widetilde\phi_i,\widetilde\psi_{i\dot\alpha},\widetilde F_i).
$$

$(i,j,\ldots)$ 是 flavor/species index。gauge index 全部 suppress。$(phi,psi,F)$ 在某个 representation $(R)$。$(widetildephi,widetildepsi,widetilde F)$ 在 dual rep $(R^*)$。

协变导数写成

$$
D_{\alpha\dot\alpha}\phi=\partial_{\alpha\dot\alpha}\phi+A_{\alpha\dot\alpha}\phi,\qquad
D_{\alpha\dot\alpha}\psi_\beta=\partial_{\alpha\dot\alpha}\psi_\beta+A_{\alpha\dot\alpha}\psi_\beta,
$$

$$
D_{\alpha\dot\alpha}F=\partial_{\alpha\dot\alpha}F+A_{\alpha\dot\alpha}F,
$$

$$
D_{\alpha\dot\alpha}\widetilde\phi=\partial_{\alpha\dot\alpha}\widetilde\phi-\widetilde\phi A_{\alpha\dot\alpha},\qquad
D_{\alpha\dot\alpha}\widetilde\psi_{\dot\beta}=\partial_{\alpha\dot\alpha}\widetilde\psi_{\dot\beta}-\widetilde\psi_{\dot\beta}A_{\alpha\dot\alpha},
$$

$$
D_{\alpha\dot\alpha}\widetilde F=\partial_{\alpha\dot\alpha}\widetilde F-\widetilde F A_{\alpha\dot\alpha}.
$$

定义

$$
W_i:=\frac{\partial W}{\partial \phi^i},\qquad
W_{ij}:=\frac{\partial^2 W}{\partial \phi^i\partial \phi^j}=W_{ji},
$$

$$
\widetilde W^i:=\frac{\partial \widetilde W}{\partial \widetilde\phi_i},\qquad
\widetilde W^{ij}:=\frac{\partial^2 \widetilde W}{\partial \widetilde\phi_i\partial \widetilde\phi_j}
=\widetilde W^{ji}.
$$

并记

$$
\psi^i\psi^j:=\psi^{i\alpha}\psi^j_\alpha,\qquad
\widetilde\psi_i\widetilde\psi_j:=\widetilde\psi_{i\dot\alpha}\widetilde\psi_j^{\dot\alpha}.
$$

则 canonical Kähler 的 matter + superpotential component Lagrangian 是

$$
\mathcal L_{\rm matt}
=\frac12 D^{\alpha\dot\alpha}\widetilde\phi_i\,D_{\alpha\dot\alpha}\phi^i
+\widetilde\psi_{i\dot\alpha}D^{\dot\alpha\alpha}\psi^i_\alpha
-\widetilde F_i F^i
+\sqrt2\,i\,\widetilde\phi_i\lambda^\alpha\psi^i_\alpha
-\sqrt2\,i\,\widetilde\psi_{i\dot\alpha}\widetilde\lambda^{\dot\alpha}\phi^i
+\widetilde\phi_i\mathcal D\phi^i.
$$

$$
\mathcal L_W
=F^iW_i(\phi)-\frac12 W_{ij}(\phi)\,\psi^i\psi^j
+\widetilde F_i\widetilde W^i(\widetilde\phi)
-\frac12 \widetilde W^{ij}(\widetilde\phi)\,\widetilde\psi_i\widetilde\psi_j.
$$

$$
\boxed{\mathcal L_{\rm tot}^{\rm new}
=\mathcal L_{\rm SYM}
+\mathcal L_{\rm gf+gh}
+\mathcal L_{\rm matt}
+\mathcal L_W }.
$$

其中 $(W,\widetilde W)$ 要满足 gauge invariance：

$$
W_i(\phi)(T^a\phi)^i=0,\qquad
(\widetilde\phi T^a)_i\,\widetilde W^i(\widetilde\phi)=0.
$$

若你最后要改回 $(\bar\lambda)$ 记号，只需

$$
\widetilde\lambda_{\dot\alpha}\mapsto \bar\lambda_{\dot\alpha}.
$$

### 2. SUSY 作用在 matter components 上（off-shell，不除 EOM）

$$
\delta\phi^i=\sqrt2\,\zeta^\alpha\psi^i_\alpha.
$$

$$
\delta\psi^i_\alpha
=\sqrt2\,\zeta_\alpha F^i
+i\sqrt2\,\widetilde\zeta^{\dot\alpha}D_{\alpha\dot\alpha}\phi^i.
$$

$$
\delta F^i
=i\sqrt2\,\widetilde\zeta^{\dot\alpha}D_{\alpha\dot\alpha}\psi^{i\alpha}
-2\,\widetilde\zeta_{\dot\alpha}\widetilde\lambda^{\dot\alpha}\phi^i.
$$

$$
\delta\widetilde\phi_i
=\sqrt2\,\widetilde\zeta_{\dot\alpha}\widetilde\psi_i^{\dot\alpha}.
$$

$$
\delta\widetilde\psi_{i\dot\alpha}
=\sqrt2\,\widetilde\zeta_{\dot\alpha}\widetilde F_i
-i\sqrt2\,\zeta^\alpha D_{\alpha\dot\alpha}\widetilde\phi_i.
$$

$$
\delta\widetilde F_i
=-i\sqrt2\,\zeta^\alpha D_{\alpha\dot\alpha}\widetilde\psi_i^{\dot\alpha}
+2\,\widetilde\phi_i\zeta^\alpha\lambda_\alpha.
$$

closure 仍然是同一个

$$
[\delta_1,\delta_2]
= v^{\alpha\dot\alpha}D_{\alpha\dot\alpha}+\delta_{\rm gauge}(\omega),
$$

$$
v_{\alpha\dot\alpha}=2i(\zeta_{2\alpha}\widetilde\zeta_{1\dot\alpha}-\zeta_{1\alpha}\widetilde\zeta_{2\dot\alpha}),
\qquad
\omega=-v^{\beta\dot\beta}A_{\beta\dot\beta}.
$$

### 3. 单独抽 $Q_-$

仍按你文档里的定义

$$
Q_-:\qquad
\zeta^-=1,\quad \zeta^+=0,\quad \widetilde\zeta^{\dot\alpha}=0,
\qquad
\zeta_+=1,\quad \zeta_-=0.
$$

**chiral multiplet**

$$
Q_-\phi^i=\sqrt2\,\psi^i_-.
$$

$$
Q_-\psi^i_+=\sqrt2\,F^i,\qquad
Q_-\psi^i_-=0.
$$

$$
Q_-F^i=0.
$$

**anti-chiral multiplet**

$$
Q_-\widetilde\phi_i=0.
$$

$$
Q_-\widetilde\psi_{i\dot\alpha}
=-i\sqrt2\,D_{-\dot\alpha}\widetilde\phi_i.
$$

即

$$
Q_-\widetilde\psi_{i\dot+}=-i\sqrt2\,D_{-\dot+}\widetilde\phi_i,\qquad
Q_-\widetilde\psi_{i\dot-}=-i\sqrt2\,D_{-\dot-}\widetilde\phi_i.
$$

$$
Q_-\widetilde F_i
=-i\sqrt2\,D_{-\dot\alpha}\widetilde\psi_i^{\dot\alpha}
+2\,\widetilde\phi_i\lambda_-.
$$

对 $(W,\widetilde W)$ 的直接作用

$$
Q_-W(\phi)=\sqrt2\,W_i\psi^i_-,\qquad
Q_-W_i=\sqrt2\,W_{ij}\psi^j_-,\qquad
Q_-\widetilde W(\widetilde\phi)=0,\qquad
Q_-\widetilde W^i=0.
$$

于是

$$
Q_-\left(F^iW_i-\frac12 W_{ij}\psi^i\psi^j\right)=0.
$$

free limit $(g=0)$ 时只需

$$
D_{\alpha\dot\alpha}\to \partial_{\alpha\dot\alpha},\qquad
Q_-\widetilde F_i=-i\sqrt2\,\partial_{-\dot\alpha}\widetilde\psi_i^{\dot\alpha}.
$$

# Add matter : susy transformation and BPS

继续用你 note 的 flat Euclidean / WZ gauge / spinor conventions；并记

$$
\bar\lambda_{\dot\alpha}:=\widetilde\lambda_{\dot\alpha},\qquad
\bar\phi_i:=\widetilde\phi_i,\qquad
\bar\psi_{i\dot\alpha}:=\widetilde\psi_{i\dot\alpha},\qquad
\bar F_i:=\widetilde F_i,
$$

bar 在这里都只是记号，不是 complex conjugation。gauge-sector 的 conventions 与你 note 完全一致。

定义

$$
W_i:=\frac{\partial W}{\partial \phi^i},\qquad
\bar W^i:=\frac{\partial \widetilde W}{\partial \bar\phi_i},\qquad
\mu^a:=\bar\phi_i (T^a\phi)^i.
$$

---

## 1. 先只 integrate out $(mathcal D,F,bar F)$，不再用别的 EOM

### auxiliary equations

由

$$
\mathcal L_{\rm aux} = \frac1{2g^2}\mathcal D^a\mathcal D^a+\mathcal D^a\mu^a-\bar F_iF^i+F^iW_i+\bar F_i\bar W^i
$$

得

$$
\frac{\partial \mathcal L}{\partial \mathcal D^a}= \frac1{g^2}\mathcal D^a+\mu^a=0
\quad\Longrightarrow\quad
\boxed{\mathcal D^a=-g^2\mu^a},
$$

$$
\frac{\partial \mathcal L}{\partial F^i}=-\bar F_i+W_i=0
\quad\Longrightarrow\quad
\boxed{\bar F_i=W_i},
$$

$$
\frac{\partial \mathcal L}{\partial \bar F_i}=-F^i+\bar W^i=0
\quad\Longrightarrow\quad
\boxed{F^i=\bar W^i}.
$$

### general SUSY after substitution

这里只是把 auxiliary EOM 直接代回 off-shell rules；**不**再用 $(\lambda,\psi,\phi,f)$ 的 dynamical EOM。

gauge multiplet:

$$
\delta A_{\alpha\dot\alpha}^a = i\zeta_\alpha\bar\lambda_{\dot\alpha}^a+i\widetilde\zeta_{\dot\alpha}\lambda_\alpha^a,
$$

$$
\delta\lambda_\alpha^a = f_{\alpha\beta}^a\zeta^\beta + i g^2\mu^a\zeta_\alpha,
$$

$$
\delta\bar\lambda_{\dot\alpha}^a = \bar f_{\dot\alpha\dot\beta}^a\widetilde\zeta^{\dot\beta}+i g^2\mu^a\widetilde\zeta_{\dot\alpha},
$$

$$
\delta f_{\alpha\beta}^a = i\zeta_{(\alpha}D_{\beta)\dot\gamma}\bar\lambda^{a\dot\gamma}+i\widetilde\zeta^{\dot\gamma}D_{(\alpha|\dot\gamma|}\lambda_{\beta)}^a,
$$

$$
\delta \bar f_{\dot\alpha\dot\beta}^a = i\widetilde\zeta_{(\dot\alpha}D_{\gamma\dot\beta)}\lambda^{a\gamma} +i\zeta^\gamma D_{\gamma(\dot\alpha}\bar\lambda_{\dot\beta)}^a.
$$

matter multiplet:

$$
\delta\phi^i=\sqrt2\zeta^\alpha\psi_\alpha^i,
$$

$$
\delta\psi_\alpha^i = \sqrt2\zeta_\alpha\bar W^i+i\sqrt2\widetilde\zeta^{\dot\alpha}D_{\alpha\dot\alpha}\phi^i,
$$

$$
\delta\bar\phi_i=\sqrt2\widetilde\zeta_{\dot\alpha}\bar\psi_i^{\dot\alpha},
$$

$$
\delta\bar\psi_{i\dot\alpha} = \sqrt2\widetilde\zeta_{\dot\alpha}W_i - i\sqrt2\zeta^\alpha D_{\alpha\dot\alpha}\bar\phi_i.
$$

composite auxiliaries 现在变成

$$
Q_-\mathcal D^a=-g^2Q_-\mu^a,\qquad
Q_-F^i=Q_-\bar W^i,\qquad
Q_-\bar F_i=Q_-W_i.
$$

并且

$$
\delta\mu^a = \sqrt2\zeta^\alpha\bar\phi_i(T^a\psi_\alpha)^i +\sqrt2\widetilde\zeta_{\dot\alpha}(\bar\psi^{\dot\alpha}T^a\phi),
$$

$$
\delta W_i=\sqrt2 W_{ij}\zeta^\alpha\psi_\alpha^j,\qquad
\delta\bar W^i=\sqrt2\bar W^{ij}\widetilde\zeta_{\dot\alpha}\bar\psi_j^{\dot\alpha}.
$$

### raw $Q_-$ action

取

$$
Q_-:\qquad \zeta^-=1,\ \zeta^+=0,\ \widetilde\zeta^{\dot\alpha}=0,
\qquad \zeta_+=1,\ \zeta_-=0.
$$

先写 basic letters。gauge 部分与你 note 一致，只是 $(mathcal Dto -g^2mu)$。

### gauge multiplet

$$
Q_-A_{+\dot\alpha}^a=i\bar\lambda_{\dot\alpha}^a,\qquad
Q_-A_{-\dot\alpha}^a=0.
$$

$$
Q_-\lambda_+^a=f_{+-}^a-i g^2\mu^a,\qquad
Q_-\lambda_-^a=f_{--}^a,
$$

$$
Q_-\bar\lambda_{\dot\alpha}^a=0.
$$

$$
Q_-f_{++}^a=iD_{+\dot\alpha}\bar\lambda^{a\dot\alpha},
$$

$$
Q_-f_{+-}^a=\frac{i}{2}D_{-\dot\alpha}\bar\lambda^{a\dot\alpha},
$$

$$
Q_-f_{--}^a=0.
$$

$$
Q_-\bar f_{\dot\alpha\dot\beta}^a = iD_{-(\dot\alpha}\bar\lambda_{\dot\beta)}^a,
$$

即

$$
Q_-\bar f_{\dot+\dot+}^a=iD_{-\dot+}\bar\lambda_{\dot+}^a,
$$

$$
Q_-\bar f_{\dot+\dot-}^a=\frac{i}{2} \Big(D_{-\dot+}\bar\lambda_{\dot-}^a+D_{-\dot-}\bar\lambda_{\dot+}^a\Big),
$$

$$
Q_-\bar f_{\dot-\dot-}^a=iD_{-\dot-}\bar\lambda_{\dot-}^a.
$$

并且

$$
Q_-\mu^a=\sqrt2\bar\phi_i(T^a\psi_- )^i,
\qquad
Q_-\mathcal D^a=-\sqrt2 g^2\bar\phi_i(T^a\psi_-)^i.
$$

### matter multiplet

$$
Q_-\phi^i=\sqrt2\psi_-^i,
$$

$$
Q_-\psi_+^i=\sqrt2\bar W^i,\qquad Q_-\psi_-^i=0,
$$

$$
Q_-\bar\phi_i=0,
$$

$$
Q_-\bar\psi_{i\dot\alpha} = - i\sqrt2 D_{-\dot\alpha}\bar\phi_i,
$$

即

$$
Q_-\bar\psi_{i\dot+}=-i\sqrt2 D_{-\dot+}\bar\phi_i,
\qquad
Q_-\bar\psi_{i\dot-}=-i\sqrt2 D_{-\dot-}\bar\phi_i.
$$

以及

$$
Q_-W_i=\sqrt2 W_{ij}\psi_-^j,\qquad
Q_-\bar W^i=0,
$$

$$
Q_-F^i=Q_-\bar W^i=0,\qquad
Q_-\bar F_i=Q_-W_i=\sqrt2 W_{ij}\psi_-^j.
$$

### descendants 的统一公式

对 adjoint-valued $X$:

$$
Q_-\big(D_{\alpha\dot\alpha}X\big) = D_{\alpha\dot\alpha}(Q_-X) +i\delta_{\alpha+}[\bar\lambda_{\dot\alpha},X].
$$

对 $R$-representation 的 $Y$:

$$
Q_-\big(D_{\alpha\dot\alpha}Y\big) = D_{\alpha\dot\alpha}(Q_-Y) +i\delta_{\alpha+}\bar\lambda_{\dot\alpha}Y.
$$

对 dual representation 的 $bar Y$:

$$
Q_-\big(D_{\alpha\dot\alpha}\bar Y\big) = D_{\alpha\dot\alpha}(Q_-\bar Y) - i\delta_{\alpha+}\bar Y\bar\lambda_{\dot\alpha}.
$$

free limit 时直接

$$
D_{\alpha\dot\alpha}\to \partial_{\alpha\dot\alpha}.
$$

---

## 2. free level 的 $Q_-$ BPS letters

现在取

$$
g=0,\qquad W=0,\qquad \widetilde W=0,
$$

所以

$$
\mathcal D=0,\qquad F=0,\qquad \bar F=0.
$$

### free raw $Q_-$

gauge:

$$
Q_-\bar\lambda_{\dot\alpha}=0,\qquad
Q_-\lambda_+=f_{+-},\qquad
Q_-\lambda_-=f_{--},
$$

$$
Q_-f_{++}=i\partial_{+\dot\alpha}\bar\lambda^{\dot\alpha},\qquad
Q_-f_{+-}=\frac{i}{2}\partial_{-\dot\alpha}\bar\lambda^{\dot\alpha},\qquad
Q_-f_{--}=0,
$$

$$
Q_-\bar f_{\dot\alpha\dot\beta}=i\partial_{-(\dot\alpha}\bar\lambda_{\dot\beta)}.
$$

matter:

$$
Q_-\phi^i=\sqrt2\psi_-^i,
\qquad
Q_-\psi_+^i=0,
\qquad
Q_-\psi_-^i=0,
$$

$$
Q_-\bar\phi_i=0,
\qquad
Q_-\bar\psi_{i\dot\alpha}=-i\sqrt2\partial_{-\dot\alpha}\bar\phi_i.
$$

### free EOM

gauge-sector:

$$
\partial_{+\dot\alpha}\bar\lambda^{\dot\alpha}=0,\qquad
\partial_{-\dot\alpha}\bar\lambda^{\dot\alpha}=0.
$$

这正是你 note 里前面已经用过的 free gaugino EOM。

matter-sector:

$$
\partial^{\alpha\dot\alpha}\partial_{\alpha\dot\alpha}\phi^i=0,\qquad
\partial^{\alpha\dot\alpha}\partial_{\alpha\dot\alpha}\bar\phi_i=0,
$$

$$
\partial^{\dot\alpha\alpha}\psi_\alpha^i=0,\qquad
\partial_{\alpha\dot\alpha}\bar\psi_i^{\dot\alpha}=0.
$$

把 $\partial^{\dot\alpha\alpha}\psi_\alpha^i=0$ 写成分量：

$$
\partial_{-\dot-}\psi_+^i-\partial_{+\dot-}\psi_-^i=0,
$$

$$
- \partial_{-\dot+}\psi_+^i+\partial_{+\dot+}\psi_-^i=0.
$$

即

$$
\partial_{+\dot-}\psi_-^i=\partial_{-\dot-}\psi_+^i,
\qquad
\partial_{+\dot+}\psi_-^i=\partial_{-\dot+}\psi_+^i.
$$

## closed / exact / cohomology

先看 **basic letters**。

### $Q_-$-closed set

$$
\ker Q_-\cap\{\bar\lambda,f,\bar\phi,\psi,\bar\psi\} = \{\bar\lambda_{\dot+},\bar\lambda_{\dot-},f_{++},f_{+-},f_{--},\bar\phi_i,\psi_+^i,\psi_-^i\}.
$$

这里

$$
Q_-f_{++}=0,\qquad Q_-f_{+-}=0
$$

是用了 free gaugino EOM；

而

$$
Q_-\bar\phi_i=0,\qquad Q_-\psi_\pm^i=0
$$

不需要别的 EOM。

### $Q_-$-exact set

$$
f_{+-}=Q_-\lambda_+,\qquad
f_{--}=Q_-\lambda_-,
$$

$$
\psi_-^i=\frac1{\sqrt2}Q_-\phi^i.
$$

所以

$$
\operatorname{Im}Q_-\cap\{\bar\lambda,f,\bar\phi,\psi,\bar\psi\} = \{f_{+-},f_{--},\psi_-^i\}.
$$

### cohomology

因此真正 surviving 的 free $Q_-$-BPS basic letters 是

$$
\boxed{H^0(Q_-;\{\rm letters\})_{\rm basic}^{\rm free} = \{\bar\lambda_{\dot+},\ \bar\lambda_{\dot-},\ f_{++},\ \bar\phi_i,\ \psi_+^i\}. }
$$

所以你猜的

$$
f_{++},\ \bar\lambda,\ \bar\phi_i,\ \psi_{+或-}
$$

里，**strict cohomology** 结果是

$$
\boxed{\psi_+^i\ \text{survives},\qquad \psi_-^i\ \text{closed but exact}.}
$$

---

## descendants

由 free SUSY algebra

$$
\{Q_-,\widetilde Q_{\dot\alpha}\}=2i\partial_{-\dot\alpha}
$$

得

$$
\partial_{-\dot\alpha}\mathcal O\in \operatorname{Im}Q_-.
$$

因此只保留 $partial_{+dotalpha}$-descendants：

$$
\partial_{+\dot+}^m\partial_{+\dot-}^n\bar\lambda_{\dot\beta},
\qquad
\partial_{+\dot+}^m\partial_{+\dot-}^n f_{++},
\qquad
\partial_{+\dot+}^m\partial_{+\dot-}^n \bar\phi_i,
\qquad
\partial_{+\dot+}^m\partial_{+\dot-}^n \psi_+^i.
$$

gauge-sector 仍有 relation

$$
\partial_{+\dot-}\bar\lambda_{\dot+} = \partial_{+\dot+}\bar\lambda_{\dot-}.
$$

matter-sector 则

$$
\partial_{-\dot\alpha}\bar\phi_i = \frac{i}{\sqrt2}Q_-\bar\psi_{i\dot\alpha},
$$

$$
\psi_-^i=\frac1{\sqrt2}Q_-\phi^i,
$$

$$
\partial_{+\dot-}\psi_-^i=\partial_{-\dot-}\psi_+^i\in \operatorname{Im}Q_-,
\qquad
\partial_{+\dot+}\psi_-^i=\partial_{-\dot+}\psi_+^i\in \operatorname{Im}Q_-.
$$

因此 full free $Q_-$-BPS descendant letters 就是

$$
\boxed{
\partial_{+\dot+}^m\partial_{+\dot-}^n\bar\lambda_{\dot\beta},\quad
\partial_{+\dot+}^m\partial_{+\dot-}^n f_{++},\quad
\partial_{+\dot+}^m\partial_{+\dot-}^n\bar\phi_i,\quad
\partial_{+\dot+}^m\partial_{+\dot-}^n\psi_+^i
\qquad (m,n\ge 0).
}
$$

如果下一步你要，我可以继续把这套 letters 的 quantum numbers $(E,j_+,j_-,r)$ 和 single-letter index 也直接算出来。

# N=4 SYM : Action and susy transformation

### 0. $SU(4)_R$-covariant field content

$$
	A_{\alpha\dot\alpha},\qquad
\lambda^A_\alpha,\qquad
\bar\lambda_{A\dot\alpha},\qquad
\phi^{AB}=-\phi^{BA},\qquad
A,B=1,2,3,4.
$$

并记

$$
	\epsilon^{1234}=1,\qquad
\bar\phi_{AB}:=\frac12\epsilon_{ABCD}\phi^{CD}
$$

这在这里是 epsilon-dual notation，不是 complex conjugation。

和你前面的 $\mathcal N=1$ basis 的对应是

$$
	\lambda^A=(\psi^1,\psi^2,\psi^3,\lambda),\qquad
\bar\lambda_A=(\bar\psi_1,\bar\psi_2,\bar\psi_3,\bar\lambda),
$$

$$
	\phi^{i4}=\phi^i,\qquad
\phi^{ij}=\epsilon^{ijk}\bar\phi_k,\qquad
\bar\phi_{i4}=\bar\phi_i,\qquad
\bar\phi_{ij}=\epsilon_{ijk}\phi^k,
\qquad i,j,k=1,2,3.
$$

---

## 1. full component action

### compact $SU(4)_R$-covariant form

$$
	S_{\mathcal N=4} = \frac{1}{g^2}\int d^4x\ \operatorname{tr}\Bigg[
\frac14 F_{\mu\nu}F_{\mu\nu}
+\bar\lambda_{A\dot\alpha}D^{\dot\alpha\alpha}\lambda^A_\alpha
+\frac18 D^{\alpha\dot\alpha}\bar\phi_{AB} D_{\alpha\dot\alpha}\phi^{AB}
$$

$$
	\qquad\qquad\qquad
+\frac{i}{\sqrt2} \lambda^{A\alpha} [\bar\phi_{AB},\lambda^B_\alpha]
+\frac{i}{\sqrt2} \bar\lambda_{A\dot\alpha} [\phi^{AB},\bar\lambda_B^{\dot\alpha}]
+\frac1{16} [\phi^{AB},\phi^{CD}][\bar\phi_{AB},\bar\phi_{CD}]
\Bigg].
$$

若要加 topological term，再加

$$
\Delta \mathcal L_\theta = \frac{i\theta}{32\pi^2}\operatorname{tr}\big(\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}\big),
$$

它单独也是 SUSY-invariant。

### 等价地，写成你前面 $\mathcal N=1$ 的 $(\lambda,\psi^i,\phi^i)$ basis

$$
	\mathcal L_{\mathcal N=4} = \frac{1}{g^2}\operatorname{tr}\Bigg[
\frac14F_{\mu\nu}F_{\mu\nu}
+\bar\lambda_{\dot\alpha}D^{\dot\alpha\alpha}\lambda_\alpha
+\bar\psi_{i\dot\alpha}D^{\dot\alpha\alpha}\psi^i_\alpha
+\frac12 D^{\alpha\dot\alpha}\bar\phi_i D_{\alpha\dot\alpha}\phi^i
$$

$$
	\qquad
+\sqrt2 i \bar\phi_i[\lambda^\alpha,\psi^i_\alpha]
- \sqrt2 i \bar\psi_{i\dot\alpha}[\bar\lambda^{\dot\alpha},\phi^i]
- \frac{i}{\sqrt2}\epsilon_{ijk}\psi^{i\alpha}[\psi^j_\alpha,\phi^k]
- \frac{i}{\sqrt2}\epsilon^{ijk}\bar\psi_{i\dot\alpha}[\bar\psi_j^{\dot\alpha},\bar\phi_k]
$$

$$
	\qquad
- \frac12[\phi^i,\bar\phi_i][\phi^j,\bar\phi_j]
+[\phi^i,\phi^j][\bar\phi_i,\bar\phi_j]
\Bigg].
$$

这里 quartic term 和 compact form 的精确恒等式是

$$
\frac1{16}[\phi^{AB},\phi^{CD}][\bar\phi_{AB},\bar\phi_{CD}] = - \frac12[\phi^i,\bar\phi_i][\phi^j,\bar\phi_j] +[\phi^i,\phi^j][\bar\phi_i,\bar\phi_j].
$$

---

## 2. full SUSY transformations

取 16 个 supercharges 的参数

$$
\delta=\zeta^{A\alpha}Q_{A\alpha}+\widetilde\zeta_A^{\dot\alpha}\widetilde Q^A_{\dot\alpha}.
$$

### basic fields

$$
\delta A_{\alpha\dot\alpha} = i \zeta^A_\alpha \bar\lambda_{A\dot\alpha} + i \widetilde\zeta_{A\dot\alpha} \lambda^A_\alpha.
$$

$$
\delta\phi^{AB} = \sqrt2\big(\zeta^{B\alpha}\lambda^A_\alpha-\zeta^{A\alpha}\lambda^B_\alpha\big) - \sqrt2 \epsilon^{ABCD}\widetilde\zeta_{C\dot\alpha}\bar\lambda_D^{\dot\alpha}.
$$

$$
\delta\bar\phi_{AB} = \sqrt2\big(\widetilde\zeta_{B\dot\alpha}\bar\lambda_A^{\dot\alpha} - \widetilde\zeta_{A\dot\alpha}\bar\lambda_B^{\dot\alpha}\big) - \sqrt2 \epsilon_{ABCD}\zeta^{C\alpha}\lambda^D_\alpha.
$$

$$
\delta\lambda^A_\alpha = f_{\alpha\beta}\zeta^{A\beta} + i\sqrt2 D_{\alpha\dot\alpha}\phi^{AB} \widetilde\zeta_B^{\dot\alpha} + i [\phi^{AB},\bar\phi_{BC}] \zeta^C_\alpha.
$$

$$
\delta\bar\lambda_{A\dot\alpha} = \bar f_{\dot\alpha\dot\beta}\widetilde\zeta_A^{\dot\beta} - i\sqrt2 D_{\alpha\dot\alpha}\bar\phi_{AB} \zeta^{B\alpha} + i [\bar\phi_{AB},\phi^{BC}] \widetilde\zeta_{C\dot\alpha}.
$$

### induced variation of field strengths

$$
\delta f_{\alpha\beta} = i \zeta^A_{(\alpha}D_{\beta)\dot\gamma}\bar\lambda_A^{\dot\gamma} + i \widetilde\zeta_A^{\dot\gamma}D_{(\alpha|\dot\gamma|}\lambda^A_{\beta)}.
$$

$$
\delta\bar f_{\dot\alpha\dot\beta} = i \widetilde\zeta_{A(\dot\alpha}D_{\gamma\dot\beta)}\lambda^{A\gamma} + i \zeta^{A\gamma}D_{\gamma(\dot\alpha}\bar\lambda_{A\dot\beta)}.
$$

---

## 3. 和你前面的 $\mathcal N=1$ 公式对一下

若只开

$$
	\zeta^4_\alpha=\zeta_\alpha,\qquad
\widetilde\zeta_{4\dot\alpha}=\widetilde\zeta_{\dot\alpha},
\qquad
\zeta^i=\widetilde\zeta_i=0,
$$

则正好得到你之前那套 $\mathcal N=1$ 变换、并且已经把 $(D,F)$ 积分掉：

$$
\delta\lambda_\alpha = f_{\alpha\beta}\zeta^\beta - i[\phi^i,\bar\phi_i]\zeta_\alpha,
$$

$$
\delta\psi^i_\alpha = i\sqrt2 D_{\alpha\dot\alpha}\phi^i \widetilde\zeta^{\dot\alpha} - i \epsilon^{ijk}[\bar\phi_j,\bar\phi_k]\zeta_\alpha,
$$

$$
\delta\bar\psi_{i\dot\alpha} = - i\sqrt2 D_{\alpha\dot\alpha}\bar\phi_i \zeta^\alpha - i \epsilon_{ijk}[\phi^j,\phi^k]\widetilde\zeta_{\dot\alpha}.
$$

---

## 4. closure

因为这里没有 auxiliary fields，closure 是 on-shell：

$$
[\delta_1,\delta_2] = v^{\alpha\dot\alpha}D_{\alpha\dot\alpha} +\delta_{\rm gauge}(\omega),
$$

$$
	v_{\alpha\dot\alpha} = 2i\big(
\zeta^A_{2\alpha}\widetilde\zeta_{1A\dot\alpha}
- \zeta^A_{1\alpha}\widetilde\zeta_{2A\dot\alpha}
\big),
\qquad
\omega=-v^{\beta\dot\beta}A_{\beta\dot\beta},
$$

并且在 fermion / scalar EOM 上闭合。

我已经按两条 route 检过一次：

一条是 先还原到 $A=4$ 的 manifest $\mathcal N=1$ off-shell system，再把 $(D,F)$ 消掉；

另一条是 利用整个 action 的 $SU(4)_R$-covariance，把这个 manifest supercharge 旋转成全部 16 个 supercharges。

两条 route 给出的系数完全一致，所以这套 $\delta$ 的确使上面的 action 不变。

如果你下一步要，我可以直接在这套记号下继续做 $Q_-\subset \mathcal N=4$ 的 BPS letters / cohomology。

# N=4 SYM : BPS letters and Feynman rules

下面固定

$$
	Q\equiv Q_-^4:\qquad \zeta^{4-}=1,\ \zeta^{4+}=0,\ \widetilde\zeta_{A\dot\alpha}=0,
\qquad
\zeta^4_+=1,\ \zeta^4_-=0,
$$

其余 SUSY parameter 全部为 $0$。这正好对应你旧记号里的 $Q_-$，因为你原来取的是 $\zeta^-=1 \iff \zeta_+=1$。并且

$$
	\phi^{i4}=\phi^i,\qquad
\phi^{ij}=\epsilon^{ijk}\bar\phi_k,\qquad
\bar\phi_{i4}=\frac12\epsilon_{ijk}\phi^{jk},
$$

$$
	\lambda^4=\lambda,\qquad
\lambda^i=\psi^i,\qquad
\bar\lambda_4=\bar\lambda,\qquad
\bar\lambda_i=\bar\psi_i,
\qquad \epsilon_{123}=1.
$$

所以这套 $Q_-^4$ 与你之前的 $Q_-$ 记号完全适配。

### 1. $Q_-^4$ 在 $SU(4)_R$-covariant base 下的 raw 作用

先给全套 basic fields：

**gauge**

$$
	Q A_{+\dot\alpha}= i\bar\lambda_{4\dot\alpha},\qquad
Q A_{-\dot\alpha}=0.
$$

$$
	Q f_{++}= iD_{+\dot\alpha}\bar\lambda_4^{\dot\alpha},
\qquad
Q f_{+-}= \frac{i}{2}D_{-\dot\alpha}\bar\lambda_4^{\dot\alpha},
\qquad
Q f_{--}=0.
$$

$$
Q \bar f_{\dot\alpha\dot\beta} = iD_{-(\dot\alpha}\bar\lambda_{4\dot\beta)}.
$$

**scalars**

$$
	Q\phi^{ij}=0,
\qquad
Q\phi^{i4}=\sqrt2\lambda^i_-.
$$

等价地

$$
	Q\bar\phi_{i4}=0,
\qquad
Q\bar\phi_{ij}= \sqrt2\epsilon_{ijk}\lambda^k_-.
$$

**fermions**

$$
	Q\lambda^4_+=f_{+-}-i[\phi^{i4},\bar\phi_{i4}],
\qquad
Q\lambda^4_-=f_{--}.
$$

$$
	Q\lambda^i_+= i[\phi^{ij},\bar\phi_{j4}],
\qquad
Q\lambda^i_-=0.
$$

$$
Q\bar\lambda_{4\dot\alpha}=0.
$$

$$
Q\bar\lambda_{i\dot\alpha} = -i\sqrt2D_{-\dot\alpha}\bar\phi_{i4} -\frac{i}{\sqrt2}\epsilon_{ijk}D_{-\dot\alpha}\phi^{jk}.
$$

这正好退化回你前面那套 $\mathcal N=1$ 公式：

$$
	Q\bar\phi_i=0,\qquad
Q\psi^i_+=-i\epsilon^{ijk}[\bar\phi_j,\bar\phi_k],\qquad
Q\bar\lambda_{\dot\alpha}=0,\qquad
Qf_{++}=iD_{+\dot\alpha}\bar\lambda^{\dot\alpha}.
$$

### 2. $Q_-^4$-complex：basic letters

### 2.1 真正用来做 $Q$-complex 的 generating letters

我建议把 basic generating set 取成

$$
	\boxed{
\phi^{ij},\qquad
\lambda^i_+,\qquad
\bar\lambda_{4\dot+},\ \bar\lambda_{4\dot-},\qquad
f_{++}.
}
$$

因为其余都落在 exact / partner sector 里：

$$
Q\phi^{i4}=\sqrt2\lambda^i_-,\qquad Q\lambda^4_-=f_{--},\qquad Q\lambda^4_+=f_{+-}-i[\phi^{i4},\bar\phi_{i4}],
$$

$$
Q\bar\lambda_{i\dot\alpha} = -\frac{i}{\sqrt2}\epsilon_{ijk}D_{-\dot\alpha}\phi^{jk}.
$$

所以

$$
	\lambda^i_-,\qquad
f_{--},\qquad
f_{+-} \text{ (free 时)},\qquad
D_{-\dot\alpha}\phi^{ij}
$$

都不是 independent cohomology generators。

### 3. 这些 BPS letters 的 SUSY 变换

下面分成两版：

#### 3.1 raw version（不代 dynamical EOM）

$$
Q\phi^{ij}=0.
$$

$$
Q\lambda^i_+= i[\phi^{ij},\bar\phi_{j4}] = \frac{i}{2}\epsilon_{jkl}[\phi^{ij},\phi^{kl}].
$$

$$
Q\bar\lambda_{4\dot\alpha}=0.
$$

$$
Qf_{++}= iD_{+\dot\alpha}\bar\lambda_4^{\dot\alpha}.
$$

这就是你要的 保留运动方程 version。

#### 3.2 simple EOM-substituted version

这里仅把最直接会用到的 fermion EOM 代进去。在 原始 normalization（即还没为 perturbation 做 canonical rescaling）下，

$$
D_{\alpha\dot\alpha}\bar\lambda_A^{\dot\alpha} = -\sqrt2i[\bar\phi_{AB},\lambda^B_\alpha].
$$

特别对 $A=4$：

$$
D_{\alpha\dot\alpha}\bar\lambda_4^{\dot\alpha} = -\sqrt2i[\bar\phi_{i4},\lambda^i_\alpha].
$$

因此

$$
Qf_{++} = iD_{+\dot\alpha}\bar\lambda_4^{\dot\alpha} = \sqrt2[\bar\phi_{i4},\lambda^i_+] = \frac1{\sqrt2}\epsilon_{ijk}[\phi^{jk},\lambda^i_+].
$$

于是生成元上的 $Q$ 变成

$$
	\boxed{
Q\phi^{ij}=0,\qquad
Q\lambda^i_+= i[\phi^{ij},\bar\phi_{j4}],\qquad
Q\bar\lambda_{4\dot\alpha}=0,\qquad
Qf_{++}= \sqrt2[\bar\phi_{i4},\lambda^i_+].
}
$$

这已经是你后面做 cohomological algebra / perturbation 最常用的一版。

### 4. free limit 的 $Q_-^4$ cohomology letters

$$
	\boxed{H^0(Q_-^4;{\rm letters})_{\rm basic}^{\rm free} = \{\phi^{ij}, \lambda^i_+, \bar\lambda_{4\dot+}, \bar\lambda_{4\dot-}, f_{++}\}.
}
$$

### 5. derivative letters

$$
Q(D_{\alpha\dot\alpha}X) = D_{\alpha\dot\alpha}(QX) +i\delta_{\alpha+}[\bar\lambda_{4\dot\alpha},X]
$$

### 6. full $\mathcal N=4$ SYM Feynman rules（同记号；这里切换到 canonical normalization）

下面 为了 perturbation theory，先做标准 rescaling

$$
	A\to gA,\qquad
\lambda\to g\lambda,\qquad
\phi\to g\phi,\qquad
c\to gc,
$$

取 Feynman gauge $\xi=1$，all incoming，定义

$$
	\int_q:=\int\frac{d^4q}{(2\pi)^4},
\qquad
[T^a,T^b]=f^{abc}T^c,\qquad
\operatorname{tr}(T^aT^b)=\delta^{ab}.
$$

#### 6.1 gauge-fixed canonical Lagrangian

$$
	\mathcal L_E^{\rm can} = \frac14F_{\mu\nu}^aF_{\mu\nu}^a
+\bar\lambda_{A\dot\alpha}^a\bar\sigma^{\mu,\dot\alpha\alpha}(D_\mu\lambda^A_\alpha)^a
+\frac18(D_\mu\bar\phi_{AB})^a(D_\mu\phi^{AB})^a
$$

$$
	\qquad
+\frac{i g}{\sqrt2}f^{abc}\lambda^{Aa\alpha}\bar\phi_{AB}^b\lambda^B_{\alpha}{}^c
+\frac{i g}{\sqrt2}f^{abc}\bar\lambda_{A\dot\alpha}^a\phi^{AB b}\bar\lambda_B^{c\dot\alpha}
+\frac{g^2}{16}f^{abe}f^{cde}\phi^{AB a}\phi^{CD b}\bar\phi_{AB}^c\bar\phi_{CD}^d
$$

$$
	\qquad
+(\partial_\mu\bar c^a)(D_\mu c)^a
+\frac12(\partial_\mu A_\mu^a)^2.
$$

#### 6.2 propagators

gauge

$$
\langle A_\mu^a(p)A_\nu^b(-p)\rangle = \frac{\delta^{ab}\delta_{\mu\nu}}{p^2}.
$$

$$
\langle A_{\alpha\dot\alpha}^a(p)A_{\beta\dot\beta}^b(-p)\rangle = \frac{2\delta^{ab}\epsilon_{\alpha\beta}\epsilon_{\dot\alpha\dot\beta}}{p^2}.
$$

fermions

$$
\langle \lambda_\alpha^{A a}(p)\bar\lambda_{B\dot\beta}^b(-p)\rangle = -\frac{i\delta^{ab}\delta^A{}_B p_{\alpha\dot\beta}}{p^2}.
$$

$$
\langle \lambda\lambda\rangle=\langle\bar\lambda\bar\lambda\rangle=0.
$$

scalars

定义 antisymmetric projector

$$
\delta^{AB}_{CD}:=\delta^A_C\delta^B_D-\delta^A_D\delta^B_C.
$$

mixed form:

$$
\langle \phi^{AB a}(p)\bar\phi_{CD}^b(-p)\rangle = \frac{\delta^{ab}\delta^{AB}_{CD}}{p^2}.
$$

pure-$\phi$ form:

$$
\langle \phi^{AB a}(p)\phi^{CD b}(-p)\rangle = \frac{\delta^{ab}\epsilon^{ABCD}}{p^2}.
$$

特别地

$$
\langle \phi^{i4 a}(p)\phi^{jk b}(-p)\rangle = \frac{\delta^{ab}\epsilon^{ijk}}{p^2}.
$$

ghosts

$$
\langle c^a(p)\bar c^b(-p)\rangle = \frac{\delta^{ab}}{p^2}.
$$

#### 6.3 standard gauge vertices

ghost-gauge

$$
V^{abc}_{\bar cAc,\mu}(p_{\bar c}) = g f^{abc}p_{\bar c,\mu}.
$$

(AAA)

$$
	V^{abc}_{AAA,\mu\nu\rho}(p,q,r) = g f^{abc}\Big[
\delta_{\mu\nu}(p-q)_\rho+\delta_{\nu\rho}(q-r)_\mu+\delta_{\rho\mu}(r-p)_\nu\Big].
$$

(AAAA)

$$
	\begin{aligned}V^{abcd}_{AAAA,\mu\nu\rho\sigma} = g^2\Big[
&f^{abe}f^{cde}(\delta_{\mu\rho}\delta_{\nu\sigma}-\delta_{\mu\sigma}\delta_{\nu\rho})\\
&+f^{ace}f^{bde}(\delta_{\mu\nu}\delta_{\rho\sigma}-\delta_{\mu\sigma}\delta_{\nu\rho})\\
&+f^{ade}f^{bce}(\delta_{\mu\nu}\delta_{\rho\sigma}-\delta_{\mu\rho}\delta_{\nu\sigma})
\Big].
\end{aligned}
$$

#### 6.4 matter-gauge vertices

($A\lambda\bar\lambda$)

$$
V^{abc;A}_{\ B,\mu} = g f^{abc}\delta^A{}_B\bar\sigma_\mu.
$$

即 component monomial

$$
\mathcal L_{A\lambda\bar\lambda} = g f^{abc} \bar\lambda_{A\dot\alpha}^a A_\mu^b \bar\sigma^{\mu,\dot\alpha\alpha} \lambda_\alpha^{A c}.
$$

($A\phi\bar\phi$)

$$
V^{abc;AB}{}_{CD,\mu}(p_{\bar\phi},p_\phi) = g f^{abc}\delta^{AB}_{CD}(p_{\bar\phi}-p_\phi)_\mu.
$$

等价 monomial

$$
\mathcal L_{A\phi\bar\phi} = g f^{abc}A_\mu^b \Big( (\partial_\mu\bar\phi_{AB}^a)\phi^{AB c} -\bar\phi_{AB}^a(\partial_\mu\phi^{AB c}) \Big).
$$

($AA\phi\bar\phi$)

$$
V^{ab;cd;AB}{}_{CD,\mu\nu} = g^2\delta_{\mu\nu}\delta^{AB}_{CD} \big( f^{ace}f^{bde}+f^{ade}f^{bce} \big).
$$

等价 monomial

$$
\mathcal L_{AA\phi\bar\phi} = g^2 f^{abe}f^{cde} A_\mu^a A_\mu^c \bar\phi_{AB}^b\phi^{AB d}.
$$

#### 6.5 Yukawa + scalar self-interaction vertices

直接按 ordered monomial 读 vertex：

$$
(\lambda\lambda\bar\phi) = \frac{i g}{\sqrt2} f^{abc} \lambda^{Aa\alpha}\bar\phi_{AB}^b\lambda^B_{\alpha}{}^c.
$$

$$
(\bar\lambda\bar\lambda\phi) = \frac{i g}{\sqrt2} f^{abc} \bar\lambda_{A\dot\alpha}^a\phi^{AB b}\bar\lambda_B^{c\dot\alpha}.
$$

$$
(\phi^4) = \frac{g^2}{16} f^{abe}f^{cde} \phi^{AB a}\phi^{CD b}\bar\phi_{AB}^c\bar\phi_{CD}^d.
$$

直接把上面三条按 fields written in order 当作 vertex source 即可。

#### 6.6 $Q_-^4$-BPS letters 的 insertion rules

trivial insertions

$$
	\mathcal I[\phi^{ij a}(p)] = \phi^{ij a}(p),
\qquad
\mathcal I[\lambda^{i a}_+(p)] = \lambda^{i a}_+(p),
\qquad
\mathcal I[\bar\lambda_{4\dot\alpha}^a(p)] = \bar\lambda_{4\dot\alpha}^a(p).
$$

$f_{++}$

$$
\mathcal I[f_{++}^a(p)] = \frac{i}{2}\Big( p_{+\dot+}A_{+\dot-}^a -p_{+\dot-}A_{+\dot+}^a \Big) +\frac{g}{2}f^{abc}\int_q A_{+\dot+}^b(q)A_{+\dot-}^c(p-q).
$$

并且

$$
\langle f_{++}^a(p)A_{-\dot\alpha}^b(-p)\rangle = -\frac{i\delta^{ab}p_{+\dot\alpha}}{p^2},\qquad \langle f_{++}^a(p)f_{++}^b(-p)\rangle = \langle f_{++}^a(p)\bar\lambda_{4\dot\alpha}^b(-p)\rangle = 0.
$$

derivative insertion（adjoint-valued $X$）

$$
\mathcal I[D_{\alpha\dot\alpha}X^a(p)] = i p_{\alpha\dot\alpha}X^a(p) +g f^{abc}\int_q A_{\alpha\dot\alpha}^b(q)X^c(p-q).
$$

free level 则简化为

$$
\mathcal I[\partial_{\alpha\dot\alpha}X(p)] = i p_{\alpha\dot\alpha}\mathcal I[X(p)].
$$

# Explicit Calculation rules

<aside>

## $i\nabla_{+\dot\alpha}\bar\lambda^{\dot\alpha}^i_j\,\bar\lambda_{\dot\beta}^k_l(p)$ 的 perturbative prescription$Q_1 (f_{++}\bar\lambda_{\dot\alpha})$

$$
																																										\mathcal O_{\dot\beta}(x):=iD_{+\dot\alpha}\bar\lambda^{\dot\alpha}(x)\,\bar\lambda_{\dot\beta}(x)
=\mathcal O^{(\partial)}_{\dot\beta}(x)+\mathcal O^{(A)}_{\dot\beta}(x),
$$

$$
																																										\mathcal O^{(\partial)}_{\dot\beta}=i\partial_{+\dot\alpha}\bar\lambda^{\dot\alpha}\,\bar\lambda_{\dot\beta},\qquad
\mathcal O^{(A)}_{\dot\beta}=ig[A_{+\dot\alpha},\bar\lambda^{\dot\alpha}]\,\bar\lambda_{\dot\beta}.
$$

$$
																																										\mathcal I[\mathcal O^{(\partial)}_{\dot\beta}(p)]
=\int_{k,\ell}(2\pi)^4\delta^{(4)}(p-k-\ell)\,(-k_{+\dot\alpha})\,\bar\lambda^{\dot\alpha}(k)\bar\lambda_{\dot\beta}(\ell).
$$

$$
																																										\text{order }g^n:\quad
\text{attach }n\text{ vertices}\ \to\ \text{Wick contract}\ \to\ \text{uncontracted fields become new external legs }\{p_i\},\quad
p=\sum_i p_i.
$$

$$
																																										\text{tree level}:\ \text{no closed cycle};\qquad
\text{loop level}:\ \text{keep every }\int_q\text{ unintegrated until regularization}.
$$

$$
																																										(-k_{+\dot\alpha})\left(-\frac{i\,r_{\gamma}{}^{\dot\alpha}}{r^2}\right)(2\pi)^4\delta^{(4)}(k+r)
=-i\,\delta_{+\gamma}(2\pi)^4\delta^{(4)}(k+r).
$$

$$
\text{所以 }\partial_{+\dot\alpha}\bar\lambda^{\dot\alpha}\text{ 与一条 }\lambda_\gamma\text{ 线收缩时，整条传播子缩成 local contact term.}
$$

### Tree-level (actually All non-anomaly level) cancellation

$$
																																																															\mathcal L_{A\lambda\bar\lambda}
=g\,\bar\lambda_{\dot\gamma}A^{\alpha\dot\gamma}\lambda_\alpha
-g\,\bar\lambda_{\dot\gamma}\lambda_\alpha A^{\alpha\dot\gamma}.
$$

$$
																																																															\mathcal I^{\text{tree}}_{(1)}[\mathcal O^{(\partial)}_{\dot\beta}(p)]
=\int_{k,\ell,q,r,s}(2\pi)^8\delta^{(4)}(p-k-\ell)\delta^{(4)}(q+r+s)
(-k_{+\dot\alpha})\bar\lambda^{\dot\alpha}(k)\bar\lambda_{\dot\beta}(\ell)
\cdot g\,\bar\lambda_{\dot\gamma}(q)A^{\gamma\dot\gamma}(r)\lambda_\gamma(s).
$$

$$
																																																															\bar\lambda^{\dot\alpha}(k)\text{ 与 }\lambda_\gamma(s)\text{ 收缩 }\Longrightarrow
\mathcal I^{\text{tree}}_{(1)}[\mathcal O^{(\partial)}_{\dot\beta}(p)]
=-ig\int_{q,r,\ell}(2\pi)^4\delta^{(4)}(p-q-r-\ell)
A_{+\dot\gamma}(r)\bar\lambda^{\dot\gamma}(q)\bar\lambda_{\dot\beta}(\ell).
$$

$$
																																																															\mathcal I^{\text{tree}}_{(2)}[\mathcal O^{(\partial)}_{\dot\beta}(p)]
=+ig\int_{q,r,\ell}(2\pi)^4\delta^{(4)}(p-q-r-\ell)
\bar\lambda^{\dot\gamma}(q)A_{+\dot\gamma}(r)\bar\lambda_{\dot\beta}(\ell).
$$

$$
																																																															\therefore\quad
\mathcal I^{\text{tree}}[\mathcal O^{(\partial)}_{\dot\beta}(p)]
=-ig\int_{q,r,\ell}(2\pi)^4\delta^{(4)}(p-q-r-\ell)
[A_{+\dot\gamma}(r),\bar\lambda^{\dot\gamma}(q)]\bar\lambda_{\dot\beta}(\ell).
$$

$$
																																																															\mathcal I[\mathcal O^{(A)}_{\dot\beta}(p)]
=+ig\int_{q,r,\ell}(2\pi)^4\delta^{(4)}(p-q-r-\ell)
[A_{+\dot\gamma}(r),\bar\lambda^{\dot\gamma}(q)]\bar\lambda_{\dot\beta}(\ell).
$$

$$
																																																															\boxed{
\mathcal I^{\text{tree}}[\mathcal O_{\dot\beta}(p)]
=\mathcal I^{\text{tree}}[\mathcal O^{(\partial)}_{\dot\beta}(p)]
+\mathcal I[\mathcal O^{(A)}_{\dot\beta}(p)]
=0
}
$$

$$
																																																															\text{故在不含 self-loop 的 tree graphs 上，} \quad iD_{+\dot\alpha}\bar\lambda^{\dot\alpha}=0
\text{ 逐图成立；非零只能来自 loop-level coincident singularity + regulator.}
$$

</aside>

<aside>

## $Q_1 (f_{++}\bar\lambda_{\dot\alpha})$1-loop relevant graphs （first attempt, wrong at group index) (dimensional regularization)

$$
																																								\mathcal O_{\dot\beta}(p)
=
\mathcal O^{(\partial)}_{\dot\beta}(p)
+
\mathcal O^{(A)}_{\dot\beta}(p),
\qquad
\mathcal O^{(\partial)}_{\dot\beta}
=
i\partial_{+\dot\alpha}\bar\lambda^{\dot\alpha}\,\bar\lambda_{\dot\beta},
\qquad
\mathcal O^{(A)}_{\dot\beta}
=
ig\big[A_{+\dot\alpha},\bar\lambda^{\dot\alpha}\big]\,\bar\lambda_{\dot\beta}.
$$

$$
\text{lowest nontrivial loop order}=g^2.
$$

$$
																																								\text{for the external structure }
\bar\lambda_{\dot\gamma}(p_1)\,\bar\lambda_{\dot\beta}(p_2),
\qquad
p=p_1+p_2,
$$

$$
\text{only }V_{A\lambda\bar\lambda}\text{ contributes}.
$$

$$
																																								V_{\bar cAc},\ V_{AAA},\ V_{AAAA}
\quad\text{do not soak up the }\bar\lambda\text{ legs of }\mathcal O_{\dot\beta}.
$$

$$
																																								\Gamma_{\partial}^{(1)}
:\quad
\mathcal O^{(\partial)}_{\dot\beta}
+
V_{A\lambda\bar\lambda}^{(1)}
+
V_{A\lambda\bar\lambda}^{(2)},
$$

$$
																																								(\partial\bar\lambda)_{\mathcal O}\cong \lambda_1,
\qquad
\bar\lambda_1\cong \lambda_2,
\qquad
A_1\cong A_2,
\qquad
\bar\lambda_{\dot\beta,\mathcal O}\ \text{external},
\qquad
\bar\lambda_{\dot\gamma}(p_1)\ \text{external}.
$$

$$
																																								\Gamma_{A}^{(1)}
:\quad
\mathcal O^{(A)}_{\dot\beta}
+
V_{A\lambda\bar\lambda},
$$

$$
																																								A_{\mathcal O}\cong A,
\qquad
\bar\lambda_{\mathcal O}\cong \lambda,
\qquad
\bar\lambda_{\dot\beta,\mathcal O}\ \text{external},
\qquad
\bar\lambda_{\dot\gamma}(p_1)\ \text{external}.
$$

$$
\text{both graphs have exactly one self-loop.}
$$

### Momentum routing

$$
																																																												\int_{p_1,p_2,q}
:=
\int\frac{d^4p_1}{(2\pi)^4}
\int\frac{d^4p_2}{(2\pi)^4}
\int\frac{d^4q}{(2\pi)^4}.
$$

$$
																																																												\text{all incoming},\qquad
p=p_1+p_2,
\qquad
q\ \text{is the loop momentum on the internal }A\text{-line}.
$$

$$
																																																												\text{Weyl propagator }\to\text{ Dirac propagator}:
\qquad
S_D(k):=\frac{-i\not k}{k^2},
\qquad
P_L=\frac{1+\gamma_5}{2},
$$

$$
																																																												-\frac{i\,k_{\alpha\dot\alpha}}{k^2}
=
\big(S_D(k)P_L\big)_{\alpha\dot\alpha}.
$$

### Honest 1-loop integral from $\mathcal O^{(\partial)}$

$$
																																																												\Gamma_{\partial,\dot\beta}^{(1)}(p)
=
g^2
\int_{p_1,p_2,q}
(2\pi)^4\delta^{(4)}(p-p_1-p_2)\,
(-p_{1,+\dot\eta})
\left(
-\frac{i\,p_{1,\gamma_1}{}^{\dot\eta}}{p_1^2}
\right)
\frac{2\,\epsilon^{\gamma_1\gamma_2}\epsilon^{\dot\rho\dot\gamma}}{q^2}
\left(
-\frac{i\,(q-p_1)_{\gamma_2\dot\rho}}{(q-p_1)^2}
\right)
\big[\bar\lambda_{\dot\gamma}(p_1),\bar\lambda_{\dot\beta}(p_2)\big].
$$

$$
																																																												\text{Dirac form}:
\qquad
\Gamma_{\partial,\dot\beta}^{(1)}(p)
=
g^2
\int_{p_1,p_2,q}
(2\pi)^4\delta^{(4)}(p-p_1-p_2)\,
(-p_{1,+\dot\eta})
\big(S_D(p_1)P_L\big)_{\gamma_1}{}^{\dot\eta}
\frac{2\,\epsilon^{\gamma_1\gamma_2}\epsilon^{\dot\rho\dot\gamma}}{q^2}
\big(S_D(q-p_1)P_L\big)_{\gamma_2\dot\rho}
\big[\bar\lambda_{\dot\gamma}(p_1),\bar\lambda_{\dot\beta}(p_2)\big].
$$

### Honest 1-loop integral from $\mathcal O^{(A)}$

$$
																																																												\Gamma_{A,\dot\beta}^{(1)}(p)
=
ig^2
\int_{p_1,p_2,q}
(2\pi)^4\delta^{(4)}(p-p_1-p_2)\,
\frac{2\,\epsilon_{+\gamma}\epsilon_{\dot\eta\dot\gamma}}{q^2}
\left(
-\frac{i\,(q-p_1)^{\gamma\dot\eta}}{(q-p_1)^2}
\right)
\big[\bar\lambda^{\dot\gamma}(p_1),\bar\lambda_{\dot\beta}(p_2)\big].
$$

$$
																																																												\text{Dirac form}:
\qquad
\Gamma_{A,\dot\beta}^{(1)}(p)
=
ig^2
\int_{p_1,p_2,q}
(2\pi)^4\delta^{(4)}(p-p_1-p_2)\,
\frac{2\,\epsilon_{+\gamma}\epsilon_{\dot\eta\dot\gamma}}{q^2}
\big(S_D(q-p_1)P_L\big)^{\gamma\dot\eta}
\big[\bar\lambda^{\dot\gamma}(p_1),\bar\lambda_{\dot\beta}(p_2)\big].
$$

### Formal collapse

$$
																																																												(-p_{1,+\dot\eta})
\left(
-\frac{i\,p_{1,\gamma_1}{}^{\dot\eta}}{p_1^2}
\right)
=
-i\,\delta_{+\gamma_1}.
$$

$$
																																																												\Gamma_{\partial,\dot\beta}^{(1)\,\mathrm{formal}}(p)
=
-2g^2
\int_{p_1,p_2,q}
(2\pi)^4\delta^{(4)}(p-p_1-p_2)\,
\frac{(q-p_1)_{-\dot\gamma}}{q^2(q-p_1)^2}
\big[\bar\lambda^{\dot\gamma}(p_1),\bar\lambda_{\dot\beta}(p_2)\big].
$$

$$
																																																												\Gamma_{A,\dot\beta}^{(1)}(p)
=
+2g^2
\int_{p_1,p_2,q}
(2\pi)^4\delta^{(4)}(p-p_1-p_2)\,
\frac{(q-p_1)_{-\dot\gamma}}{q^2(q-p_1)^2}
\big[\bar\lambda^{\dot\gamma}(p_1),\bar\lambda_{\dot\beta}(p_2)\big].
$$

$$
\text{所以 1-loop anomaly 的关键点不是 formal cancellation，}
$$

$$
\text{而是 }\Gamma_{\partial}^{(1)}\text{ 必须先保持为 honest UV-divergent integral，再上 regulator；}
$$

$$
\text{不能先把 }(-p_1)_{+\dot\eta}S_W(p_1)\text{ 直接缩成 }-i\delta_{+}.
$$

</aside>

<aside>

## $Q_1 (f_{++}\bar\lambda_{\dot\alpha})$1-loop relevant graphs (second attempt, wrong at group index)(dimensional regularization)

![image.png](%E7%9B%B4%E6%8E%A51-loop%20level%E8%AE%A1%E7%AE%97/image.png)

### 1-loop perturbative prescription

$$
																																																									\mathcal O_{\dot\beta}(p)
=
\mathcal O^{(\partial)}_{\dot\beta}(p)
+
\mathcal O^{(A)}_{\dot\beta}(p),
\qquad
\mathcal O^{(\partial)}_{\dot\beta}
=
i\partial_{+\dot\alpha}\bar\lambda^{\dot\alpha}\,\bar\lambda_{\dot\beta},
\qquad
\mathcal O^{(A)}_{\dot\beta}
=
ig\big[A_{+\dot\alpha},\bar\lambda^{\dot\alpha}\big]\,\bar\lambda_{\dot\beta}.
$$

$$
																																																									d=4-2\epsilon,
\qquad
\int_q^d:=\mu^{2\epsilon}\int\frac{d^dq}{(2\pi)^d},
\qquad
S_D(k):=\frac{-i\not k}{k^2},
\qquad
P_L=\frac{1+\gamma_5}{2}.
$$

$$
																																																									\big[S_D(k)P_L\big]_{\alpha\dot\alpha}
=
-\frac{i\,k_{\alpha\dot\alpha}}{k^2}.
$$

$$
																																																								t(\bar\lambda\bar\lambda)(p)
:=
\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)\,\epsilon^{\dot\gamma\dot\delta}\bar\lambda_{\dot\gamma}(p_1)\bar\lambda_{\dot\delta}(p_2).
$$

$$
																																																									\mathcal I\!\left[\partial_{+\dot\beta}(\bar\lambda\bar\lambda)(p)\right]
=
i\,p_{+\dot\beta}\,(\bar\lambda\bar\lambda)(p).
$$

### Relevant 1-loop graphs

真正 relevant 的 one-self-loop sector 分成两类：

$$
																																																									\Gamma_{\rm EOM}^{(1)}
=
\Gamma_{\partial,{\rm chain}}^{(1)}
+
\Gamma_{A,{\rm bubble}}^{(1)},
\qquad
\Gamma_{\rm anom}^{(1)}
=
\Gamma_{\partial,12}^{(1)}
+
\Gamma_{\partial,21}^{(1)}.
$$

其中

$$
																																																									\Gamma_{\partial,{\rm chain}}^{(1)}:\qquad
(\partial\bar\lambda)_{\mathcal O}\cong\lambda_1,
\qquad
\bar\lambda_1\cong\lambda_2,
\qquad
A_1\cong A_2,
$$

$$
																																																									\bar\lambda_{\dot\beta,\mathcal O}\ \text{external},
\qquad
\bar\lambda_{\dot\gamma}(p_1)\ \text{external}.
$$

$$
																																																									\Gamma_{A,{\rm bubble}}^{(1)}:\qquad
A_{\mathcal O}\cong A,
\qquad
\bar\lambda_{\mathcal O}\cong\lambda,
$$

$$
																																																									\bar\lambda_{\dot\beta,\mathcal O}\ \text{external},
\qquad
\bar\lambda_{\dot\gamma}(p_1)\ \text{external}.
$$

这两张图属于 EOM sector；formal 4d reduction 后彼此抵消。

真正给 $\partial_{+\dot\beta}(\bar\lambda\bar\lambda)$ 的是 triangle pair：

$$
																																																									\Gamma_{\partial,12}^{(1)}:\qquad
(\partial\bar\lambda)_{\mathcal O}\cong\lambda_1,
\qquad
(\bar\lambda_{\dot\beta})_{\mathcal O}\cong\lambda_2,
\qquad
A_1\cong A_2,
$$

$$
																																																									\bar\lambda_{\dot\gamma}(p_1)\ \text{external},
\qquad
\bar\lambda_{\dot\delta}(p_2)\ \text{external}.
$$

$$
																																																									\Gamma_{\partial,21}^{(1)}:\qquad
(\partial\bar\lambda)_{\mathcal O}\cong\lambda_2,
\qquad
(\bar\lambda_{\dot\beta})_{\mathcal O}\cong\lambda_1,
\qquad
A_1\cong A_2,
$$

$$
																																																									\bar\lambda_{\dot\delta}(p_2)\ \text{external},
\qquad
\bar\lambda_{\dot\gamma}(p_1)\ \text{external}.
$$

### Honest momentum integrals: EOM sector

$$
																																																									\Gamma_{\partial,{\rm chain},\dot\beta}^{(1)}(p_1,p_2)
=
g^2 C_A
\int_q^d
\Big[
-p_{1,+\dot\alpha}\,
\big[S_D(p_1)P_L\big]_{\alpha}{}^{\dot\alpha}
\Big]
\frac{2\,\epsilon^{\alpha\rho}\epsilon^{\dot\eta\dot\gamma}}{q^2}
\big[S_D(q-p_1)P_L\big]_{\rho\dot\eta}\,
\bar\lambda_{\dot\gamma}(p_1)\bar\lambda_{\dot\beta}(p_2).
$$

$$
																																																									\Gamma_{A,{\rm bubble},\dot\beta}^{(1)}(p_1,p_2)
=
i g^2 C_A
\int_q^d
\frac{2\,\epsilon_{+\rho}\epsilon_{\dot\eta\dot\gamma}}{q^2}\,
\big[S_D(q-p_1)P_L\big]^{\rho\dot\eta}\,
\bar\lambda^{\dot\gamma}(p_1)\bar\lambda_{\dot\beta}(p_2).
$$

formal 4d identity:

$$
																																																									-p_{1,+\dot\alpha}\,\big[S_D(p_1)P_L\big]_{\alpha}{}^{\dot\alpha}
=
i\,\epsilon_{+\alpha},
$$

所以

$$
\Gamma_{\partial,{\rm chain}}^{(1)}+\Gamma_{A,{\rm bubble}}^{(1)}=0.
$$

### Honest momentum integrals: anomalous triangle sector

取 routing

$$
																																																									k_1=q+p_1,
\qquad
k_2=p_2-q,
\qquad
p=p_1+p_2.
$$

则

$$
																																																									\Gamma_{\partial,12,\dot\beta}^{(1)}(p_1,p_2)
=
g^2 C_A
\int_q^d
\Big[
-(q+p_1)_{+\dot\alpha}\,
\big[S_D(q+p_1)P_L\big]_{\alpha}{}^{\dot\alpha}
\Big]
\frac{2\,\epsilon^{\alpha\rho}\epsilon^{\dot\gamma\dot\delta}}{q^2}
\big[S_D(q-p_2)P_L\big]_{\rho\dot\beta}\,
\bar\lambda_{\dot\gamma}(p_1)\bar\lambda_{\dot\delta}(p_2).
$$

$$
																																																									\Gamma_{\partial,21,\dot\beta}^{(1)}(p_1,p_2)
=
g^2 C_A
\int_q^d
\Big[
-(q+p_2)_{+\dot\alpha}\,
\big[S_D(q+p_2)P_L\big]_{\alpha}{}^{\dot\alpha}
\Big]
\frac{2\,\epsilon^{\alpha\rho}\epsilon^{\dot\delta\dot\gamma}}{q^2}
\big[S_D(q-p_1)P_L\big]_{\rho\dot\beta}\,
\bar\lambda_{\dot\delta}(p_2)\bar\lambda_{\dot\gamma}(p_1).
$$

### d-dimensional reduction of the triangle numerator

把 $q=\tilde q+\hat q$ 分成 4d part 与 $(d-4)$-dim part，则

$$
																																																									(\tilde q+p_1)_{+\dot\alpha}(\tilde q+p_1)_{\alpha}{}^{\dot\alpha}
=
\big((q+p_1)^2-\hat q^2\big)\epsilon_{+\alpha}.
$$

故

$$
																																																									-(q+p_1)_{+\dot\alpha}\,\big[S_D(q+p_1)P_L\big]_{\alpha}{}^{\dot\alpha}
=
i\left(1-\frac{\hat q^2}{(q+p_1)^2}\right)\epsilon_{+\alpha}.
$$

于是

$$
																																																									\Gamma_{\partial,12,\dot\beta}^{(1)}
=
2C_A g^2
\int_q^d
\frac{(q-p_2)_{+\dot\beta}}{q^2(q-p_2)^2}\,
\epsilon^{\dot\gamma\dot\delta}\bar\lambda_{\dot\gamma}(p_1)\bar\lambda_{\dot\delta}(p_2)
-
2C_A g^2
\int_q^d
\frac{\hat q^2\,(q-p_2)_{+\dot\beta}}{q^2(q+p_1)^2(q-p_2)^2}\,
\epsilon^{\dot\gamma\dot\delta}\bar\lambda_{\dot\gamma}(p_1)\bar\lambda_{\dot\delta}(p_2).
$$

同理

$$
																																																									\Gamma_{\partial,21,\dot\beta}^{(1)}
=
2C_A g^2
\int_q^d
\frac{(q-p_1)_{+\dot\beta}}{q^2(q-p_1)^2}\,
\epsilon^{\dot\gamma\dot\delta}\bar\lambda_{\dot\gamma}(p_1)\bar\lambda_{\dot\delta}(p_2)
-
2C_A g^2
\int_q^d
\frac{\hat q^2\,(q-p_1)_{+\dot\beta}}{q^2(q+p_2)^2(q-p_1)^2}\,
\epsilon^{\dot\gamma\dot\delta}\bar\lambda_{\dot\gamma}(p_1)\bar\lambda_{\dot\delta}(p_2).
$$

### UV-divergent local piece

定义标准 two-point integral

$$
																																																									I_0(s)
:=
\int_q^d\frac{1}{q^2(q-p)^2}\Big\|_{p^2=s}
=
\frac{\mu^{2\epsilon}}{(4\pi)^{2-\epsilon}}
\Gamma(\epsilon)\,
\frac{\Gamma(1-\epsilon)^2}{\Gamma(2-2\epsilon)}\,
s^{-\epsilon}.
$$

其 UV pole 为

$$
																																																									\big[I_0(s)\big]_{\rm UV}
=
\frac{1}{16\pi^2}\frac{1}{\epsilon}.
$$

并且

$$
																																																									\int_q^d\frac{(q-p)_{+\dot\beta}}{q^2(q-p)^2}
=
-\frac12\,p_{+\dot\beta}\,I_0(p^2).
$$

故 triangle pair 的 local UV part 为

$$
																																																									\Gamma_{{\rm anom},\dot\beta}^{(1)}(p_1,p_2)\Big\|_{\rm UV}
=
-C_A g^2\,
\Big[
p_{2,+\dot\beta}I_0(p_2^2)
+
p_{1,+\dot\beta}I_0(p_1^2)
\Big]_{\rm UV}
\epsilon^{\dot\gamma\dot\delta}\bar\lambda_{\dot\gamma}(p_1)\bar\lambda_{\dot\delta}(p_2).
$$

即

$$
																																																									\Gamma_{{\rm anom},\dot\beta}^{(1)}(p_1,p_2)\Big\|_{\rm UV}
=
-\frac{C_A g^2}{16\pi^2}\frac{1}{\epsilon}\,
(p_1+p_2)_{+\dot\beta}\,
\epsilon^{\dot\gamma\dot\delta}\bar\lambda_{\dot\gamma}(p_1)\bar\lambda_{\dot\delta}(p_2).
$$

由于 $p=p_1+p_2$,

$$
																																																									\boxed{
\Gamma_{{\rm anom},\dot\beta}^{(1)}(p)\Big\|_{\rm UV}
=
-\frac{C_A g^2}{16\pi^2}\frac{1}{\epsilon}\,
p_{+\dot\beta}\,
(\bar\lambda\bar\lambda)(p)
}.
$$

于是，作为 local operator mixing，

$$
																																																									\boxed{
i\nabla_{+\dot\alpha}\bar\lambda^{\dot\alpha}\,\bar\lambda_{\dot\beta}(p)
\ \leadsto\
-\frac{C_A g^2}{16\pi^2}\frac{1}{\epsilon}\,
\partial_{+\dot\beta}(\bar\lambda\bar\lambda)(p)
}.
$$

$$
																																								\text{(省略群指标；EOM-sector cancel，nonzero piece 只来自 anomalous triangle UV divergence).
Python schematic Feynman graphs： q1_fpp_nablafpp_diagrams.png**<br>Setup**<br>沿用同页 conventions：<br>\[
Q_- f_{++}= i\nabla_{+\dot\alpha}\bar\lambda^{\dot\alpha},\qquad<br>Q_-A_{+\dot\theta}= i\bar\lambda_{\dot\theta},\qquad<br>\[Q_-,\nabla_{+\dot\theta}\]X=i[\bar\lambda_{\dot\theta},X],<br>\]<br>\[
\mathcal I[\partial_{+\dot\theta}f_{++}(p)]<br>= i,p_{+\dot\theta},\mathcal I[f_{++}(p)],<br>\qquad<br>V_{A\lambda\bar\lambda}=V_L-V_R,<br>\]<br>\[
\langle \Lambda_\alpha(p)\bar\Lambda_{\dot\beta}(-p)\rangle_{\rm PV}<br>=-\frac{i,p_{\alpha\dot\beta}}{p^2+M^2},<br>\qquad<br>\langle B_{\alpha\dot\alpha}(p)B_{\beta\dot\beta}(-p)\rangle_{\rm PV}<br>=\frac{2\epsilon_{\alpha\beta}\epsilon_{\dot\alpha\dot\beta}}{p^2+M^2}.<br>\]
并且继续用前页 mixed color tensor (\mathscr F_{12}^{\dot\beta},\mathscr F_{21}^{\dot\beta})。
定义
\[
\mathcal O_{f\nabla f,\dot\theta}{}^i{}_j{}^k{}_l(x):=f_{++}{}^i{}_j(x),\nabla_{+\dot\theta}f_{++}{}^k{}_l(x).\]
**<br>严格写\[Q_-\mathcal O_{f\nabla f,\dot\theta}**<br>\underbrace{<br>\big(i\nabla_{+\dot\alpha}\bar\lambda^{\dot\alpha}\big),\nabla_{+\dot\theta}f_{++}<br>}*{\text{loop-focus 1}}+\underbrace{f*{++},\nabla_{+\dot\theta}\big(i\nabla_{+\dot\alpha}\bar\lambda^{\dot\alpha}\big)}*{\text{loop-focus 2}}+\underbrace{i,f*{++},[\bar\lambda_{\dot\theta},f_{++}]}_{\text{tree level}}.\]<br>下面只算 loop-focus；最后一项不进 1-loop anomaly。**<br>Ordered pair 先算**<br>\[
\mathcal O_{\dot\theta}^{\rm mix}{}^i{}_j{}^k{}_l(x):=i\nabla_{+\dot\alpha}\bar\lambda^{\dot\alpha}{}^i{}_j(x),\nabla_{+\dot\theta}f_{++}{}^k{}_l(x).\]**<br>取决定 universal coefficient 的 two-field triangle piece：\[\mathcal O_{\dot\theta}^{(\partial\partial)}{}^i{}_j{}^k{}_l**<br>i\partial_{+\dot\alpha}\bar\lambda^{\dot\alpha}{}^i{}_j;i\partial_{+\dot\theta}f_{++}^{(\partial)}{}^k{}_l.\]**<br>动量空间 insertion：\[\mathcal I!\left[\mathcal O_{\dot\theta}^{(\partial\partial)}(p)\right]**<br>\int_{r,s}(2\pi)^4\delta^{(4)}(p-r-s),<br>(-r_{+\dot\alpha})(i s_{+\dot\theta}),<br>\bar\lambda^{\dot\alpha}(r),\mathcal I[f_{++}(s)].<br>\]**<br>同前页定义\[\mathscr F_{12}^{\dot\beta}**<br>\mathscr F_{12}^{(LL)\dot\beta}<br>+\mathscr F_{12}^{(LR)\dot\beta}<br>+\mathscr F_{12}^{(RL)\dot\beta}<br>+\mathscr F_{12}^{(RR)\dot\beta},<br>\]<br>\[
\mathscr F_{12}^{(LL)\dot\beta}{}^i{}_j{}^k{}_l=\Pi^{mn}{}_{jl},f_{++}{}^i{}_m(p_1),\bar\lambda^{\dot\beta}{}^k{}_n(p_2),\]
\[\mathscr F_{12}^{(LR)\dot\beta}{}^i{}_j{}^k{}_l=-\Pi^{mk}{}_{jn},f_{++}{}^i{}_m(p_1),\bar\lambda^{\dot\beta}{}^n{}_l(p_2),\]
\[\mathscr F_{12}^{(RL)\dot\beta}{}^i{}_j{}^k{}_l=-\Pi^{in}{}_{ml},f_{++}{}^m{}_j(p_1),\bar\lambda^{\dot\beta}{}^k{}_n(p_2),\]
\[\mathscr F_{12}^{(RR)\dot\beta}{}^i{}_j{}^k{}_l=\Pi^{ik}{}_{mn},f_{++}{}^m{}_j(p_1),\bar\lambda^{\dot\beta}{}^n{}_l(p_2),\]
\[\mathscr F_{21}^{\dot\beta}(p_1,p_2)=\mathscr F_{12}^{\dot\beta}(p_2,p_1).\]**<br>Pattern 12**<br>routing 取<br>\[
r=q+p_1,\qquad s=p_2-q,\qquad p=p_1+p_2.<br>\]
写<br>\[
\big(S_M(k)P_L\big)_{\alpha\dot\alpha}=-\frac{i,k_{\alpha\dot\alpha}}{k^2+M^2}.\]**<br>则\[-r_{+\dot\alpha}\big(S_M(r)P_L\big)_\alpha{}^{\dot\alpha}**<br>i\epsilon_{+\alpha}<br>-i\frac{M^2}{r^2+M^2}\epsilon_{+\alpha}.<br>\]**<br>又\[\langle f_{++}(s),B_{-\dot\beta}(-s)\rangle_{\rm PV}<br>-\frac{i,s_{+\dot\beta}}{s^2+M^2},\]故\[i s_{+\dot\theta},\langle f_{++}(s),B_{-\dot\beta}(-s)\rangle_{\rm PV}**<br>\frac{s_{+\dot\theta}s_{+\dot\beta}}{s^2+M^2}.<br>\]**<br>于是\[\Gamma_{12;M}^{\rm PV\text{-}loop}{}_{\dot\theta}{}^i{}_j{}^k{}_l**<br>2i g^2\int_q<br>\frac{(q-p_2)_{+\dot\theta}(q-p_2)_{+\dot\beta}}<br>\{(q^2+M^2)\big((q-p_2)^2+M^2\big)\}<br>,<br>\mathscr F_{12}^{\dot\beta}{}^i{}_j{}^k{}_l\]
\[\qquad-2i g^2 M^2\int_q\frac{(q-p_2)_{+\dot\theta}(q-p_2)_{+\dot\beta}}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)},\mathscr F_{12}^{\dot\beta}{}^i{}_j{}^k{}_l.\]**<br>前一项是 contact/EOM sector；后一项是 anomaly sector：\[\Gamma_{12;M}^{(\rm anom)}{}_{\dot\theta}**<br>-2i g^2 M^2\int_q<br>\frac{(q-p_2)_{+\dot\theta}(q-p_2)_{+\dot\beta}}<br>\{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)\}<br>,<br>\mathscr F_{12}^{\dot\beta}.<br>\]**<br>Feynman parameter：\[\frac{1}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}**<br>2\int_0^1dx,dy,dz,\delta(1-x-y-z)<br>\frac{1}{\big[(q+yp_1-zp_2)^2+M^2+\Delta\big]^3},<br>\]<br>\[
\Delta=xy,p_1^2+xz,p_2^2+yz,p^2.<br>\]
令<br>\[
\ell=q+yp_1-zp_2,\qquad q-p_2=\ell-yp-xp_2.<br>\]
**<br>则\[\Gamma_{12;M}^{(\rm anom)}**<br>-4i g^2 M^2\int_0^1dx,dy,dz,\delta(1-x-y-z)<br>\int_\ell<br>\frac{(\ell-yp-xp_2)_{+\dot\theta}(\ell-yp-xp_2)_{+\dot\beta}}<br>\{(\ell^2+M^2+\Delta)^3\}<br>,<br>\mathscr F_{12}^{\dot\beta}.<br>\]**<br>\[\int_\ell \ell_{+\dot\theta}\ell_{+\dot\beta},F(\ell^2)=0,\qquad\int_\ell \ell_{+\dot\theta},F(\ell^2)=0,\]故只剩 shift piece：\[\Gamma_{12;M}^{(\rm anom)}**<br>-4i g^2 M^2\int_0^1dx,dy,dz,\delta(1-x-y-z)<br>(yp+xp_2)_{+\dot\theta}(yp+xp_2)_{+\dot\beta}<br>\int_\ell\frac{1}{(\ell^2+M^2+\Delta)^3}<br>,<br>\mathscr F_{12}^{\dot\beta}.<br>\]**<br>再用\[\int_\ell\frac{1}{(\ell^2+\Omega)^3}<br>\frac{1}{32\pi^2}\frac{1}{\Omega},\]得\[\Gamma_{12;M}^{(\rm anom)}**<br>-\frac{i g^2}{8\pi^2}<br>\int_0^1dx,dy,dz,\delta(1-x-y-z)<br>\frac{M^2}{M^2+\Delta}<br>(yp+xp_2)_{+\dot\theta}(yp+xp_2)_{+\dot\beta}<br>,<br>\mathscr F_{12}^{\dot\beta}.<br>\]**<br>取 (M\to\infty) 的 local part：\[\Gamma_{12}^{(\rm anom,loc)}\]...
$$

</aside>

<aside>

## $Q_1 (f_{++}\bar\lambda_{\dot\alpha})$ (third attempt, DR. right answer)

### corrected matrix-index setup

$$
\Pi^{ik}{}_{jl}:=\sum_a (T^a)^i{}_j(T^a)^k{}_l.
$$

$$
																										\Pi^{ik}{}_{jl}
=
\delta^i{}_l\delta^k{}_j
\quad (U(N)),
\qquad
\Pi^{ik}{}_{jl}
=
\delta^i{}_l\delta^k{}_j-\frac1N\delta^i{}_j\delta^k{}_l
\quad (SU(N)).
$$

$$
																										\langle \lambda_\alpha{}^i{}_j(p)\,\bar\lambda_{\dot\beta}{}^k{}_l(-p)\rangle
=
-\frac{i\,p_{\alpha\dot\beta}}{p^2}\,\Pi^{ik}{}_{jl},
$$

$$
																										\langle A_{\alpha\dot\alpha}{}^i{}_j(p)\,A_{\beta\dot\beta}{}^k{}_l(-p)\rangle
=
\frac{2\,\epsilon_{\alpha\beta}\epsilon_{\dot\alpha\dot\beta}}{p^2}\,\Pi^{ik}{}_{jl}.
$$

$$
V_{A\lambda\bar\lambda}=V_L-V_R,
$$

$$
																										V_L
=
g\,\bar\lambda_{\dot\gamma}{}^a{}_b\,A^{\gamma\dot\gamma}{}^b{}_c\,\lambda_\gamma{}^c{}_a,
\qquad
V_R
=
g\,\bar\lambda_{\dot\gamma}{}^a{}_b\,\lambda_\gamma{}^b{}_c\,A^{\gamma\dot\gamma}{}^c{}_a.
$$

$$
																										\mathcal O_{\dot\beta}{}^i{}_j{}^k{}_l
=
i\nabla_{+\dot\alpha}\bar\lambda^{\dot\alpha}{}^i{}_j\,\bar\lambda_{\dot\beta}{}^k{}_l
=
\mathcal O_{\dot\beta}^{(\partial)}{}^i{}_j{}^k{}_l
+
\mathcal O_{\dot\beta}^{(A)}{}^i{}_j{}^k{}_l,
$$

$$
																										\mathcal O_{\dot\beta}^{(\partial)}{}^i{}_j{}^k{}_l
=
i\partial_{+\dot\alpha}\bar\lambda^{\dot\alpha}{}^i{}_j\,\bar\lambda_{\dot\beta}{}^k{}_l,
$$

$$
																										\mathcal O_{\dot\beta}^{(A)}{}^i{}_j{}^k{}_l
=
ig\Big(
A_{+\dot\alpha}{}^i{}_m\,\bar\lambda^{\dot\alpha}{}^m{}_j
-
\bar\lambda^{\dot\alpha}{}^i{}_m\,A_{+\dot\alpha}{}^m{}_j
\Big)\bar\lambda_{\dot\beta}{}^k{}_l.
$$

$$
																										\mathcal I[\mathcal O_{\dot\beta}^{(\partial)}{}^i{}_j{}^k{}_l(p)]
=
\int_{r,s}(2\pi)^4\delta^{(4)}(p-r-s)\,
(-r_{+\dot\alpha})\,
\bar\lambda^{\dot\alpha}{}^i{}_j(r)\,
\bar\lambda_{\dot\beta}{}^k{}_l(s).
$$

### order $g^2$ before Wick contraction

$$
																										\Gamma_{\triangle,\dot\beta}^{(1)}{}^i{}_j{}^k{}_l(p)
=
\frac12\,
\Big\langle
\mathcal I[\mathcal O_{\dot\beta}^{(\partial)}{}^i{}_j{}^k{}_l(p)]
\,
(V_L-V_R)_1
\,
(V_L-V_R)_2
\Big\rangle_{0,\text{1-loop}}.
$$

$$
																										(V_L-V_R)_a
=
\int_{u_a,v_a,w_a}(2\pi)^4\delta^{(4)}(u_a+v_a+w_a)
\Big[
\bar\lambda_{\dot\gamma_a}{}^{a_a}{}_{b_a}(u_a)\,
A^{\gamma_a\dot\gamma_a}{}^{b_a}{}_{c_a}(v_a)\,
\lambda_{\gamma_a}{}^{c_a}{}_{a_a}(w_a)
-
\bar\lambda_{\dot\gamma_a}{}^{a_a}{}_{b_a}(u_a)\,
\lambda_{\gamma_a}{}^{b_a}{}_{c_a}(w_a)\,
A^{\gamma_a\dot\gamma_a}{}^{c_a}{}_{a_a}(v_a)
\Big].
$$

### Wick pattern 12

$$
																										\bar\lambda^{\dot\alpha}{}^i{}_j(r)\cong \lambda_{1,\alpha}(w_1),
\qquad
\bar\lambda_{\dot\beta}{}^k{}_l(s)\cong \lambda_{2,\rho}(w_2),
\qquad
A_1(v_1)\cong A_2(v_2),
$$

$$
																										\bar\lambda_{\dot\gamma}(u_1)\ \text{external with momentum }p_1,
\qquad
\bar\lambda_{\dot\delta}(u_2)\ \text{external with momentum }p_2,
\qquad
p=p_1+p_2.
$$

取 routing

$$
																										v_1=q,\qquad v_2=-q,\qquad
w_1=-(q+p_1),\qquad
w_2=q-p_2.
$$

于是

$$
																										r=q+p_1,
\qquad
s=p-r=p_2-q.
$$

### after Wick contraction: graph 12

$$
																									\Gamma_{12,\dot\beta}^{(1)}{}^i{}_j{}^k{}_l(p_1,p_2)
=
g^2\int_q^d
\Big[
-(q+p_1)_{+\dot\alpha}\,
\big(S_D(q+p_1)P_L\big)_{\alpha}{}^{\dot\alpha}
\Big]
\frac{2\,\epsilon^{\alpha\rho}}{q^2}\,
\big(S_D(q-p_2)P_L\big)_{\rho\dot\beta}\,
\mathscr C_{12}{}^i{}_j{}^k{}_l(p_1,p_2),
$$

$$
																									S_D(k)=\frac{-i\not k}{k^2},
\qquad
\big(S_D(k)P_L\big)_{\alpha\dot\alpha}
=
-\frac{i\,\tilde k_{\alpha\dot\alpha}}{k^2}.
$$

其中 color-flow tensor 分成四项：

$$
																									\mathscr C_{12}
=
\mathscr C_{12}^{(LL)}
+
\mathscr C_{12}^{(LR)}
+
\mathscr C_{12}^{(RL)}
+
\mathscr C_{12}^{(RR)},
$$

$$
																									\mathscr C_{12}^{(LL)}{}^i{}_j{}^k{}_l
=
\epsilon^{\dot\gamma\dot\delta}\,
\Pi^{mn}{}_{jl}\,
\bar\lambda_{\dot\gamma}{}^i{}_m(p_1)\,
\bar\lambda_{\dot\delta}{}^k{}_n(p_2),
$$

$$
																									\mathscr C_{12}^{(LR)}{}^i{}_j{}^k{}_l
=
-\epsilon^{\dot\gamma\dot\delta}\,
\Pi^{mk}{}_{jn}\,
\bar\lambda_{\dot\gamma}{}^i{}_m(p_1)\,
\bar\lambda_{\dot\delta}{}^n{}_l(p_2),
$$

$$
																									\mathscr C_{12}^{(RL)}{}^i{}_j{}^k{}_l
=
-\epsilon^{\dot\gamma\dot\delta}\,
\Pi^{in}{}_{ml}\,
\bar\lambda_{\dot\gamma}{}^m{}_j(p_1)\,
\bar\lambda_{\dot\delta}{}^k{}_n(p_2),
$$

$$
																									\mathscr C_{12}^{(RR)}{}^i{}_j{}^k{}_l
=
\epsilon^{\dot\gamma\dot\delta}\,
\Pi^{ik}{}_{mn}\,
\bar\lambda_{\dot\gamma}{}^m{}_j(p_1)\,
\bar\lambda_{\dot\delta}{}^n{}_l(p_2).
$$

在 (U(N)) double-line 下：

$$
																									\mathscr C_{12}{}^i{}_j{}^k{}_l
=
\epsilon^{\dot\gamma\dot\delta}\Big[
\bar\lambda_{\dot\gamma}{}^i{}_l(p_1)\bar\lambda_{\dot\delta}{}^k{}_j(p_2)
-\delta^k{}_j\,\bar\lambda_{\dot\gamma}{}^i{}_m(p_1)\bar\lambda_{\dot\delta}{}^m{}_l(p_2)
-\delta^i{}_l\,\bar\lambda_{\dot\gamma}{}^m{}_j(p_1)\bar\lambda_{\dot\delta}{}^k{}_m(p_2)
+\bar\lambda_{\dot\gamma}{}^k{}_j(p_1)\bar\lambda_{\dot\delta}{}^i{}_l(p_2)
\Big].
$$

### Wick pattern 21

$$
																									\Gamma_{21,\dot\beta}^{(1)}{}^i{}_j{}^k{}_l(p_1,p_2)
=
g^2\int_q^d
\Big[
-(q+p_2)_{+\dot\alpha}\,
\big(S_D(q+p_2)P_L\big)_{\alpha}{}^{\dot\alpha}
\Big]
\frac{2\,\epsilon^{\alpha\rho}}{q^2}\,
\big(S_D(q-p_1)P_L\big)_{\rho\dot\beta}\,
\mathscr C_{21}{}^i{}_j{}^k{}_l(p_1,p_2),
$$

$$
																									\mathscr C_{21}{}^i{}_j{}^k{}_l(p_1,p_2)
=
\mathscr C_{12}{}^i{}_j{}^k{}_l(p_2,p_1).
$$

### 4d part + evanescent part

把 (q=tilde q+hat q), external momenta 全在 4d 子空间：

$$
																									-(q+p_1)_{+\dot\alpha}
\big(S_D(q+p_1)P_L\big)_{\alpha}{}^{\dot\alpha}
=
i\left(
1-\frac{\hat q^2}{(q+p_1)^2}
\right)\epsilon_{+\alpha}.
$$

故

$$
																									\Gamma_{12,\dot\beta}^{(1)}
=
\Gamma_{12,\dot\beta}^{(0)}
+
\Gamma_{12,\dot\beta}^{(\mathrm{ev})},
$$

$$
																									\Gamma_{12,\dot\beta}^{(0)}{}^i{}_j{}^k{}_l
=
2g^2\int_q^d
\frac{(q-p_2)_{+\dot\beta}}{q^2(q-p_2)^2}\,
\mathscr C_{12}{}^i{}_j{}^k{}_l,
$$

$$
																									\Gamma_{12,\dot\beta}^{(\mathrm{ev})}{}^i{}_j{}^k{}_l
=
-2g^2\int_q^d
\frac{\hat q^2\,(q-p_2)_{+\dot\beta}}{q^2(q+p_1)^2(q-p_2)^2}\,
\mathscr C_{12}{}^i{}_j{}^k{}_l.
$$

同理

$$
																									\Gamma_{21,\dot\beta}^{(0)}{}^i{}_j{}^k{}_l
=
2g^2\int_q^d
\frac{(q-p_1)_{+\dot\beta}}{q^2(q-p_1)^2}\,
\mathscr C_{21}{}^i{}_j{}^k{}_l,
$$

$$
																									\Gamma_{21,\dot\beta}^{(\mathrm{ev})}{}^i{}_j{}^k{}_l
=
-2g^2\int_q^d
\frac{\hat q^2\,(q-p_1)_{+\dot\beta}}{q^2(q+p_2)^2(q-p_1)^2}\,
\mathscr C_{21}{}^i{}_j{}^k{}_l.
$$

$$
																									\Gamma^{(0)}
\ \text{是 naive 4d collapse 的 contact/EOM 部分；}
\qquad
\Gamma^{(\mathrm{ev})}
\ \text{才是 anomaly 部分。}
$$

### Feynman parameter evaluation of the anomalous term

$$
																								\frac{1}{q^2(q+p_1)^2(q-p_2)^2}
=
2\int_0^1 dx\,dy\,dz\,
\delta(1-x-y-z)\,
\frac{1}{\big[(q+y p_1-z p_2)^2+\Delta\big]^3},
$$

$$
																								\Delta
=
xy\,p_1^2+xz\,p_2^2+yz\,p^2,
\qquad
p=p_1+p_2.
$$

令

$$
\ell=q+y p_1-z p_2.
$$

则

$$
																								q-p_2
=
\ell-y p_1-(1-z)p_2
=
\ell-y p-x p_2.
$$

故 odd part 消失：

$$
																								\Gamma_{12,\dot\beta}^{(\mathrm{ev})}{}^i{}_j{}^k{}_l
=
4g^2
\int_0^1 dx\,dy\,dz\,
\delta(1-x-y-z)\,
(y p+x p_2)_{+\dot\beta}\,
I_{\hat2}(\Delta)\,
\mathscr C_{12}{}^i{}_j{}^k{}_l,
$$

$$
																								I_{\hat2}(\Delta)
:=
\mu^{2\epsilon}
\int\frac{d^d\ell}{(2\pi)^d}\,
\frac{\hat\ell^2}{(\ell^2+\Delta)^3}.
$$

由于分母只依赖 (ell^2),

$$
																								I_{\hat2}(\Delta)
=
\frac{d-4}{d}\,
\mu^{2\epsilon}
\int\frac{d^d\ell}{(2\pi)^d}\,
\frac{\ell^2}{(\ell^2+\Delta)^3}
=
\frac{d-4}{4}\,
\frac{\mu^{2\epsilon}}{(4\pi)^{2-\epsilon}}\,
\Gamma(\epsilon)\,
\Delta^{-\epsilon}.
$$

于是

$$
																								I_{\hat2}^{\mathrm{loc}}
=
-\frac{1}{32\pi^2}.
$$

从而

$$
																								\Gamma_{12,\dot\beta}^{(\mathrm{ev,loc})}{}^i{}_j{}^k{}_l
=
-\frac{g^2}{48\pi^2}\,
(p_1+2p_2)_{+\dot\beta}\,
\mathscr C_{12}{}^i{}_j{}^k{}_l,
$$

$$
																								\Gamma_{21,\dot\beta}^{(\mathrm{ev,loc})}{}^i{}_j{}^k{}_l
=
-\frac{g^2}{48\pi^2}\,
(2p_1+p_2)_{+\dot\beta}\,
\mathscr C_{21}{}^i{}_j{}^k{}_l.
$$

### final local anomaly

因为

$$
\mathscr C_{21}(p_1,p_2)=\mathscr C_{12}(p_2,p_1),
$$

且

$$
																								\epsilon^{\dot\gamma\dot\delta}
\bar\lambda_{\dot\gamma}(p_1)\bar\lambda_{\dot\delta}(p_2)
=
\epsilon^{\dot\gamma\dot\delta}
\bar\lambda_{\dot\gamma}(p_2)\bar\lambda_{\dot\delta}(p_1),
$$

故

$$
																								\Gamma_{\mathrm{anom},\dot\beta}^{(1)}{}^i{}_j{}^k{}_l(p)
=
-\frac{g^2}{16\pi^2}\,
p_{+\dot\beta}\,
\mathscr B{}^i{}_j{}^k{}_l(p),
$$

其中

$$
																								\mathscr B{}^i{}_j{}^k{}_l(p)
:=
\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)\,
\mathscr C_{12}{}^i{}_j{}^k{}_l(p_1,p_2).
$$

在 (U(N)) double-line 下，

$$
																								\mathscr B{}^i{}_j{}^k{}_l(p)
=
\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)\,
\epsilon^{\dot\gamma\dot\delta}
\Big[
2\,\bar\lambda_{\dot\gamma}{}^i{}_l(p_1)\bar\lambda_{\dot\delta}{}^k{}_j(p_2)
-\delta^k{}_j\,\bar\lambda_{\dot\gamma}{}^i{}_m(p_1)\bar\lambda_{\dot\delta}{}^m{}_l(p_2)
-\delta^i{}_l\,\bar\lambda_{\dot\gamma}{}^m{}_j(p_1)\bar\lambda_{\dot\delta}{}^k{}_m(p_2)
\Big].
$$

因此 momentum-space insertion 是

$$
																								\boxed{
\mathcal I\!\left[
\mathcal O_{\dot\beta}^{(1)\,\mathrm{loc}}{}^i{}_j{}^k{}_l(p)
\right]
=
-\frac{g^2}{16\pi^2}\,
p_{+\dot\beta}\,
\mathscr B{}^i{}_j{}^k{}_l(p)
}.
$$

等价地，position-space operator 是

$$
																								\boxed{
\mathcal O_{\dot\beta}^{(1)\,\mathrm{loc}}{}^i{}_j{}^k{}_l(x)
=
\frac{g^2}{16\pi^2}\,
i\partial_{+\dot\beta}\,
\mathscr B{}^i{}_j{}^k{}_l(x)
}.
$$

### one-line summary

$$
																								\Gamma^{(0)}\ \text{不是 anomaly；}
\qquad
\Gamma^{(\mathrm{ev})}\propto \hat q^2
\ \text{若无 UV pole 则严格为 }0;
\qquad
(d-4)\times \Gamma(\epsilon)
\ \text{给出上面的 finite local term。}
$$

</aside>

<aside>
💡

## $Q_1 (f_{++}\bar\lambda_{\dot\alpha})$  fourth attempt PV   (right answer, the same)

**anomaly 来自 PV mass term 在** $M\to\infty$ **之后留下的 finite local term**。

### PV setup

取一个 adjoint PV copy：fermion $(\Lambda_\alpha,\bar\Lambda_{\dot\alpha})$ 与 vector $B_{\alpha\dot\alpha}$，并取相同的 color projector

$$
\Pi^{ik}{}_{jl}:=\sum_a (T^a)^i{}_j(T^a)^k{}_l.
$$

relevant propagators（PV）：

$$
																																	\left\langle \Lambda_\alpha{}^i{}_j(p)\,\bar\Lambda_{\dot\beta}{}^k{}_l(-p)\right\rangle_{\rm PV}
=
-\frac{i\,p_{\alpha\dot\beta}}{p^2+M^2}\,\Pi^{ik}{}_{jl},
$$

$$
																																	\left\langle B_{\alpha\dot\alpha}{}^i{}_j(p)\,B_{\beta\dot\beta}{}^k{}_l(-p)\right\rangle_{\rm PV}
=
\frac{2\,\epsilon_{\alpha\beta}\epsilon_{\dot\alpha\dot\beta}}{p^2+M^2}\,\Pi^{ik}{}_{jl}.
$$

并记

$$
\int_q:=\int\frac{d^4q}{(2\pi)^4}.
$$

massive mixed fermion propagator（仍只取 $P_L$ 部分）：

$$
\big(S_M(k)P_L\big)_{\alpha\dot\alpha}=-\frac{i\,\tilde k_{\alpha\dot\alpha}}{k^2+M^2}.
$$

于是

$$
																																	-k_{+\dot\alpha}\,\big(S_M(k)P_L\big)_{\alpha}{}^{\dot\alpha}
=
i\,\frac{k_{+\dot\alpha}k_{\alpha}{}^{\dot\alpha}}{k^2+M^2}
=
i\,\epsilon_{+\alpha}-i\,\frac{M^2}{k^2+M^2}\,\epsilon_{+\alpha}.
$$

### Graph 12：PV loop 与 regulated splitting

先写 PV loop：

$$
																																	\Gamma_{12,\dot\beta}^{{\rm PV\text{-}loop}}{}^i{}_j{}^k{}_l
=
g^2\int_q
\Big[
-(q+p_1)_{+\dot\alpha}\,\big(S_M(q+p_1)P_L\big)_{\alpha}{}^{\dot\alpha}
\Big]
\frac{2\epsilon^{\alpha\rho}}{q^2+M^2}
\big(S_M(q-p_2)P_L\big)_{\rho\dot\beta}
\,\mathscr C_{12}{}^i{}_j{}^k{}_l.
$$

代入上一恒等式，得到两项分解：

$$
																																	\Gamma_{12,\dot\beta}^{{\rm PV\text{-}loop}}
=
2g^2\int_q\frac{(q-p_2)_{+\dot\beta}}{(q^2+M^2)\big((q-p_2)^2+M^2\big)}\,\mathscr C_{12}
-
2g^2M^2\int_q\frac{(q-p_2)_{+\dot\beta}}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}\,\mathscr C_{12}.
$$

因此把 **regulated amplitude** 写成

$$
																																	\Gamma_{12,\dot\beta}^{\rm reg}
=
\Big(\Gamma_{12,\dot\beta}^{(0)}-\Gamma_{12,\dot\beta;M}^{(0)}\Big)
+
\Gamma_{12,\dot\beta;M}^{({\rm anom})},
$$

其中（与本页 DRED 部分逐项对照）

$$
																																	\Gamma_{12,\dot\beta}^{(0)}
=
2g^2\int_q\frac{(q-p_2)_{+\dot\beta}}{q^2(q-p_2)^2}\,\mathscr C_{12},
$$

$$
																																	\Gamma_{12,\dot\beta;M}^{(0)}
=
2g^2\int_q\frac{(q-p_2)_{+\dot\beta}}{(q^2+M^2)\big((q-p_2)^2+M^2\big)}\,\mathscr C_{12},
$$

$$
																																	\Gamma_{12,\dot\beta;M}^{({\rm anom})}
=
2g^2M^2\int_q\frac{(q-p_2)_{+\dot\beta}}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}\,\mathscr C_{12}.
$$

前两项是 contact/EOM sector；最后一项由 **PV mass term** 产生，是 anomalous sector。

### Feynman parameter：提取 finite local term

对 $\Gamma_{12;M}^{({\rm anom})}$ 用参数化：

$$
																																	\frac{1}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}
=
2\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
\frac{1}{\big[(q+yp_1-zp_2)^2+M^2+\Delta\big]^3},
$$

$$
\Delta=xy\,p_1^2+xz\,p_2^2+yz\,p^2,\qquad p=p_1+p_2.
$$

令

$$
\ell=q+yp_1-zp_2,
$$

则

$$
q-p_2=\ell-yp_1-(1-z)p_2=\ell-yp-xp_2.
$$

于是

$$
																																	\Gamma_{12,\dot\beta;M}^{({\rm anom})}
=
4g^2M^2\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
\int_\ell\frac{(\ell-yp-xp_2)_{+\dot\beta}}{(\ell^2+M^2+\Delta)^3}\,\mathscr C_{12}.
$$

odd part 消失，得到

$$
																																	\Gamma_{12,\dot\beta;M}^{({\rm anom})}
=
-4g^2M^2\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
(yp+xp_2)_{+\dot\beta}
\int_\ell\frac{1}{(\ell^2+M^2+\Delta)^3}\,\mathscr C_{12}.
$$

并用 4d Euclidean 标量积分

$$
																																	\int_\ell\frac{1}{(\ell^2+\Omega)^3}
=\int\frac{d^4\ell}{(2\pi)^4}\frac{1}{(\ell^2+\Omega)^3}
=\frac{1}{32\pi^2}\frac{1}{\Omega}.
$$

故

$$
																																	\Gamma_{12,\dot\beta;M}^{({\rm anom})}
=
-\frac{g^2}{8\pi^2}
\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
\frac{M^2}{M^2+\Delta}
(yp+xp_2)_{+\dot\beta}\,\mathscr C_{12}.
$$

将

$$
\frac{M^2}{M^2+\Delta}=1-\frac{\Delta}{M^2+\Delta}
$$

分解为 local + decoupling：

$$
																																	\Gamma_{12,\dot\beta;M}^{({\rm anom})}
=
\Gamma_{12,\dot\beta}^{({\rm anom,loc})}+\Gamma_{12,\dot\beta;M}^{({\rm anom,dec})},
\qquad
\lim_{M\to\infty}\Gamma_{12,\dot\beta;M}^{({\rm anom,dec})}=0.
$$

其中 local piece 为

$$
																																	\Gamma_{12,\dot\beta}^{({\rm anom,loc})}
=
-\frac{g^2}{8\pi^2}
\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
(yp+xp_2)_{+\dot\beta}\,\mathscr C_{12}.
$$

simplex 积分

$$
																																	\int dx\,dy\,dz\,\delta(1-x-y-z)\,x=\frac16,
\qquad
\int dx\,dy\,dz\,\delta(1-x-y-z)\,y=\frac16,
$$

因此

$$
																																	\Gamma_{12,\dot\beta}^{({\rm anom,loc})}{}^i{}_j{}^k{}_l
=
-\frac{g^2}{48\pi^2}
(p_1+2p_2)_{+\dot\beta}\,\mathscr C_{12}{}^i{}_j{}^k{}_l.
$$

### Graph 21 与求和

同理

$$
																																	\Gamma_{21,\dot\beta}^{({\rm anom,loc})}{}^i{}_j{}^k{}_l
=
-\frac{g^2}{48\pi^2}
(2p_1+p_2)_{+\dot\beta}\,\mathscr C_{21}{}^i{}_j{}^k{}_l.
$$

定义

$$
																																	\mathscr B{}^i{}_j{}^k{}_l(p)
:=
\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)\,\mathscr C_{12}{}^i{}_j{}^k{}_l(p_1,p_2).
$$

用 $\mathscr C_{21}(p_1,p_2)=\mathscr C_{12}(p_2,p_1)$ 以及

$$
																																	\epsilon^{\dot\gamma\dot\delta}\bar\lambda_{\dot\gamma}(p_1)\bar\lambda_{\dot\delta}(p_2)
=
\epsilon^{\dot\gamma\dot\delta}\bar\lambda_{\dot\gamma}(p_2)\bar\lambda_{\dot\delta}(p_1),
$$

得到最终 anomalous local term

$$
																																	\Gamma_{\rm anom,\dot\beta}^{(1)}{}^i{}_j{}^k{}_l(p)
=
-\frac{g^2}{16\pi^2}\,p_{+\dot\beta}\,\mathscr B{}^i{}_j{}^k{}_l(p).
$$

对应的 insertion / operator mixing：

$$
																																	\boxed{\ 
\mathcal I\!\left[\mathcal O_{\dot\beta}^{(1),\rm loc}{}^i{}_j{}^k{}_l(p)\right]
=
-\frac{g^2}{16\pi^2}\,p_{+\dot\beta}\,\mathscr B{}^i{}_j{}^k{}_l(p)
\ }
$$

$$
																																	\boxed{\ 
\mathcal O_{\dot\beta}^{(1),\rm loc}{}^i{}_j{}^k{}_l(x)
=
\frac{g^2}{16\pi^2}\,i\partial_{+\dot\beta}\,\mathscr B{}^i{}_j{}^k{}_l(x)
\ }
$$

这与本页 DRED 的结论完全一致：EOM/contact sector 被 $\Gamma^{(0)}-\Gamma_M^{(0)}$ 吸收，anomaly 来自 PV mass term 留下的 finite local term。

</aside>

# Higher order( with derivatives)

<aside>

## $Q_1(f_{++}f_{++})$

![image.png](%E7%9B%B4%E6%8E%A51-loop%20level%E8%AE%A1%E7%AE%97/image%201.png)

### **Setup**

沿用当前页的 propagators、$V_{A\lambda\bar\lambda}=V_L-V_R$、matrix-index / double-line conventions，以及上一页已经算完的 PV master integral。

取

$$
\mathcal O(x):=i\nabla_{+\dot\alpha}\bar\lambda^{\dot\alpha}(x),\qquad f_{++}(x).
$$

抽出决定 universal 1-loop coefficient 的 two-field triangle piece：

$$
																														\mathcal O^{(\partial\partial)}(x)=i\partial_{+\dot\alpha}\bar\lambda^{\dot\alpha}(x),\qquad
f_{++}^{(\partial)}(x)=i\partial_{+\dot\gamma}A_{+}{}^{\dot\gamma}(x).
$$

其余带显式 $g$ 的 pieces 只做 covariant completion，不改这个 triangle 的 PV coefficient。

### **Color-flow tensor**

定义 mixed tensor

$$
																														\mathscr F_{12}^{\dot\beta}
=\mathscr F_{12}^{(LL)\dot\beta}+\mathscr F_{12}^{(LR)\dot\beta}+\mathscr F_{12}^{(RL)\dot\beta}+\mathscr F_{12}^{(RR)\dot\beta},
$$

其中

$$
																														\mathscr F_{12}^{(LL)\dot\beta}{}^i{}_j{}^k{}_l
=\Pi^{mn}{}_{jl}\,f_{++}{}^i{}_m(p_1)\,\bar\lambda^{\dot\beta}{}^k{}_n(p_2),
$$

$$
																														\mathscr F_{12}^{(LR)\dot\beta}{}^i{}_j{}^k{}_l
=-\Pi^{mk}{}_{jn}\,f_{++}{}^i{}_m(p_1)\,\bar\lambda^{\dot\beta}{}^n{}_l(p_2),
$$

$$
																														\mathscr F_{12}^{(RL)\dot\beta}{}^i{}_j{}^k{}_l
=-\Pi^{in}{}_{ml}\,f_{++}{}^m{}_j(p_1)\,\bar\lambda^{\dot\beta}{}^k{}_n(p_2),
$$

$$
																														\mathscr F_{12}^{(RR)\dot\beta}{}^i{}_j{}^k{}_l
=\Pi^{ik}{}_{mn}\,f_{++}{}^m{}_j(p_1)\,\bar\lambda^{\dot\beta}{}^n{}_l(p_2).
$$

在 $U(N)$ 下

$$
																														\mathscr F_{12}^{\dot\beta}{}^i{}_j{}^k{}_l
=f_{++}{}^i{}_l(p_1)\bar\lambda^{\dot\beta}{}^k{}_j(p_2)
-\delta^k{}_j f_{++}{}^i{}_m(p_1)\bar\lambda^{\dot\beta}{}^m{}_l(p_2)
-\delta^i{}_l f_{++}{}^m{}_j(p_1)\bar\lambda^{\dot\beta}{}^k{}_m(p_2)
+f_{++}{}^k{}_j(p_1)\bar\lambda^{\dot\beta}{}^i{}_l(p_2).
$$

并取

$$
\mathscr F_{21}^{\dot\beta}(p_1,p_2)=\mathscr F_{12}^{\dot\beta}(p_2,p_1).
$$

### **Pattern 12**

routing 取成和图一致：

$$
u_1=q,\qquad v_1=p_1,\qquad w_1=-(q+p_1),
$$

$$
u_2=p_2,\qquad v_2=q-p_2,\qquad w_2=-q,
$$

$$
r=q+p_1,\qquad s=p-r=p_2-q,\qquad p=p_1+p_2.
$$

PV propagators：

$$
																														\langle \Lambda_\alpha(p)\bar\Lambda_{\dot\beta}(-p)\rangle_{\rm PV}
=-\frac{i\,p_{\alpha\dot\beta}}{p^2+M^2},\qquad
\langle B_{\alpha\dot\alpha}(p)B_{\beta\dot\beta}(-p)\rangle_{\rm PV}
=\frac{2\epsilon_{\alpha\beta}\epsilon_{\dot\alpha\dot\beta}}{p^2+M^2}.
$$

massive collapse identity：

$$
																														-k_{+\dot\alpha}\big(S_M(k)P_L\big)_\alpha{}^{\dot\alpha}
=i\epsilon_{+\alpha}-i\frac{M^2}{k^2+M^2}\epsilon_{+\alpha}.
$$

因此 12 图的 PV loop 直接写成

$$
																														\Gamma_{12;M}^{\rm PV\text{-}loop}{}^i{}_j{}^k{}_l
=2g^2\int_q\frac{(q-p_2)_{+\dot\beta}}{(q^2+M^2)\big((q-p_2)^2+M^2\big)}\,\mathscr F_{12}^{\dot\beta}{}^i{}_j{}^k{}_l
$$

$$
																														\qquad
-2g^2M^2\int_q
\frac{(q-p_2)_{+\dot\beta}}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}\,\mathscr F_{12}^{\dot\beta}{}^i{}_j{}^k{}_l.
$$

前一项是 contact/EOM sector，后一项是 anomaly sector。

### **Feynman parameter**

$$
																													\frac{1}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}
=2\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
\frac{1}{\big[(q+yp_1-zp_2)^2+M^2+\Delta\big]^3},
$$

$$
\Delta=xy\,p_1^2+xz\,p_2^2+yz\,p^2.
$$

令

$$
\ell=q+yp_1-zp_2,\qquad q-p_2=\ell-yp-xp_2.
$$

则 odd part 消失：

$$
																													\Gamma_{12;M}^{(\rm anom)}
=-4g^2M^2\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
(yp+xp_2)_{+\dot\beta}\int_\ell\frac{1}{(\ell^2+M^2+\Delta)^3}\,\mathscr F_{12}^{\dot\beta}.
$$

再用

$$
\int_\ell\frac{1}{(\ell^2+\Omega)^3}=\frac{1}{32\pi^2}\frac{1}{\Omega},
$$

得 local part

$$
																													\Gamma_{12;M}^{(\rm anom,loc)}
=-\frac{g^2}{8\pi^2}
\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
\frac{M^2}{M^2+\Delta}\,(yp+xp_2)_{+\dot\beta}\,\mathscr F_{12}^{\dot\beta}.
$$

取 $M\to\infty$ 的 local part，并用 simplex integrals

$$
																													\int dx\,dy\,dz\,\delta(1-x-y-z)
\,x=\int dx\,dy\,dz\,\delta(1-x-y-z)\,y=\frac16,
$$

得到

$$
																													\boxed{\Gamma_{12}^{(\rm anom,loc)}{}^i{}_j{}^k{}_l
=-\frac{g^2}{48\pi^2}(p_1+2p_2)_{+\dot\beta}\,\mathscr F_{12}^{\dot\beta}{}^i{}_j{}^k{}_l}.
$$

### **Pattern 21**

完全平行：

$$
																													\boxed{\Gamma_{21}^{(\rm anom,loc)}{}^i{}_j{}^k{}_l
=-\frac{g^2}{48\pi^2}(2p_1+p_2)_{+\dot\beta}\,\mathscr F_{21}^{\dot\beta}{}^i{}_j{}^k{}_l}.
$$

### **Open-index final result**

$$
																														\boxed{\mathcal I\!\left[Q_1\big(f_{++}f_{++}\big){}^i{}_j{}^k{}_l(p)\right]
=-\frac{g^2}{48\pi^2}
\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)
\Big[(p_1+2p_2)_{+\dot\beta}\,\mathscr F_{12}^{\dot\beta}{}^i{}_j{}^k{}_l
+(2p_1+p_2)_{+\dot\beta}\,\mathscr F_{21}^{\dot\beta}{}^i{}_j{}^k{}_l\Big]}.
$$

### **Single-trace simplification**

若真正要的是 gauge-invariant $operatorname{Tr}(f_{++}f_{++})$，则 cyclicity 给出

$$
																														\Gamma_{12}^{(\rm anom,loc)}+\Gamma_{21}^{(\rm anom,loc)}
=-\frac{g^2}{16\pi^2}
p_{+\dot\beta}\operatorname{Tr}\big(f_{++}(p_1)\bar\lambda^{\dot\beta}(p_2)\big).
$$

所以

$$
																														\boxed{\mathcal I\!\left[Q_1,\operatorname{Tr}(f_{++}f_{++})(p)\right]
=-\frac{g^2}{16\pi^2}
p_{+\dot\beta}\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)
\operatorname{Tr}\big(f_{++}(p_1)\bar\lambda^{\dot\beta}(p_2)\big)}.
$$

position space：

$$
																														\boxed{Q_1,\operatorname{Tr}(f_{++}f_{++})(x)
=\frac{g^2}{16\pi^2}\,i\partial_{+\dot\beta}\operatorname{Tr}\big(f_{++}\bar\lambda^{\dot\beta}\big)(x)}.
$$

在 1-loop order 写成 covariantized form 也成立：

$$
																														Q_1,\operatorname{Tr}(f_{++}f_{++})(x)
=\frac{g^2}{16\pi^2}\,i\nabla_{+\dot\beta}\operatorname{Tr}\big(f_{++}\bar\lambda^{\dot\beta}\big)(x),
$$

因为 $\partial\to\nabla$ 的差别从更高阶开始。

### Lie-algebra-index rewrite of the open-index final result

$$
[T^A,T^B]=f^{AB}{}_C\,T^C,\qquad \operatorname{Tr}(T^AT^B)=\delta^{AB}.
$$

$$
																		(f_{++}f_{++}){}^i{}_j{}^k{}_l=(T^A)^i{}_j(T^B)^k{}_l\,\mathcal O_{ff}^{AB},
\qquad
\mathcal O_{ff}^{AB}:=f_{++}^A f_{++}^B.
$$

$$
																		\mathscr F_{12}^{\dot\beta}{}^i{}_j{}^k{}_l=(T^A)^i{}_j(T^B)^k{}_l\,\mathscr F_{12}^{AB,\dot\beta},
\qquad
\mathscr F_{21}^{\dot\beta}{}^i{}_j{}^k{}_l=(T^A)^i{}_j(T^B)^k{}_l\,\mathscr F_{21}^{AB,\dot\beta}.
$$

$$
																		\mathscr F_{12}^{AB,\dot\beta}
=f^{CE}{}_A f^{DE}{}_B\,f_{++}^C(p_1)\bar\lambda^{\dot\beta D}(p_2),
\qquad
\mathscr F_{21}^{AB,\dot\beta}
=f^{CE}{}_A f^{DE}{}_B\,f_{++}^C(p_2)\bar\lambda^{\dot\beta D}(p_1).
$$

$$
																		\boxed{\mathcal I\!\left[Q_1\mathcal O_{ff}^{AB}(p)\right]
=-\frac{g^2}{48\pi^2}
\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)
\Big[(p_1+2p_2)_{+\dot\beta}\,\mathscr F_{12}^{AB,\dot\beta}
+(2p_1+p_2)_{+\dot\beta}\,\mathscr F_{21}^{AB,\dot\beta}\Big]}.
$$

$$
																		=-\frac{g^2}{16\pi^2}\,p_{+\dot\beta}
\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)
\,f^{CE}{}_A f^{DE}{}_B\,f_{++}^C(p_1)\bar\lambda^{\dot\beta D}(p_2).
$$

$$
\mathcal O_{f\bar\lambda}^{AB,\dot\beta}(x):=f^{CE}{}_A f^{DE}{}_B\,f_{++}^C(x)\bar\lambda^{\dot\beta D}(x).
$$

$$
Q_1\mathcal O_{ff}^{AB}(x)=\frac{g^2}{16\pi^2}\,i\partial_{+\dot\beta}\mathcal O_{f\bar\lambda}^{AB,\dot\beta}(x).
$$

$$
																		(\nabla_{\alpha\dot\alpha}\mathcal O)^{AB}
:=\partial_{\alpha\dot\alpha}\mathcal O^{AB}
+f^{AC}{}_D A_{\alpha\dot\alpha}^C\mathcal O^{DB}
+f^{BC}{}_D A_{\alpha\dot\alpha}^C\mathcal O^{AD}.
$$

$$
																		\boxed{
Q_1\mathcal O_{ff}^{AB}(x)
=\frac{g^2}{16\pi^2}\,i\nabla_{+\dot\beta}\mathcal O_{f\bar\lambda}^{AB,\dot\beta}(x)
}.
$$

</aside>

<aside>

### $Q_1(f_{++}\nabla_{+\dot\gamma}\bar\lambda_{\dot\alpha})$

![image.png](%E7%9B%B4%E6%8E%A51-loop%20level%E8%AE%A1%E7%AE%97/image%202.png)

### **Setup**

沿用前页全部 conventions：propagators、$(V_{Alambdabarlambda}=V_L-V_R)$、matrix-index / double-line、同一个 $(mathscr C_{12},mathscr C_{21})$，以及 PV collapse identity。

取

$$
\mathcal O_{\dot\theta\dot\beta}{}^i{}_j{}^k{}_l(x):=i\nabla_{+\dot\alpha}\bar\lambda^{\dot\alpha}{}^i{}_j(x),\nabla_{+\dot\theta}\bar\lambda_{\dot\beta}{}^k{}_l(x).
$$

抽出决定 universal 1-loop coefficient 的 two-field triangle piece：

$$
														\mathcal O_{\dot\theta\dot\beta}^{(\partial\partial)}{}^i{}_j{}^k{}_l
:= i\partial_{+\dot\alpha}\bar\lambda^{\dot\alpha}{}^i{}_j\, i\partial_{+\dot\theta}\bar\lambda_{\dot\beta}{}^k{}_l.
$$

其余显式 $g$ 的 $(partial A)$、$(Apartial)$、$(AA)$ pieces 只做 covariant completion，不改 triangle 的 PV coefficient。anomaly 仍只来自 triangle pair。

动量空间 insertion：

$$
														\mathcal I\!\left[\mathcal O_{\dot\theta\dot\beta}^{(\partial\partial)}(p)\right]
=
\int_{r,s}(2\pi)^4\delta^{(4)}(p-r-s)
(-r_{+\dot\alpha})(i s_{+\dot\theta})
\bar\lambda^{\dot\alpha}(r)\bar\lambda_{\dot\beta}(s).
$$

color tensor 直接沿用前页：

$$
														\mathscr C_{21}{}^i{}_j{}^k{}_l(p_1,p_2),
\qquad
\mathscr C_{12}{}^i{}_j{}^k{}_l(p_2,p_1).
$$

### Pattern 12

routing 取

$$
r=q+p_1,\qquad s=p_2-q,\qquad p=p_1+p_2.
$$

PV propagators：

$$
														\langle \Lambda_\alpha(p)\bar\Lambda_{\dot\beta}(-p)\rangle_{\rm PV}
=-\frac{i p_{\alpha\dot\beta}}{p^2+M^2},
\qquad
\langle B_{\alpha\dot\alpha}(p)B_{\beta\dot\beta}(-p)\rangle_{\rm PV}
=\frac{2\epsilon_{\alpha\beta}\epsilon_{\dot\alpha\dot\beta}}{p^2+M^2}.
$$

写成

$$
\big(S_M(k)P_L\big)_{\alpha\dot\alpha}=-\frac{i k_{\alpha\dot\alpha}}{k^2+M^2}.
$$

于是

$$
														-r_{+\dot\alpha}\big(S_M(r)P_L\big)_\alpha{}^{\dot\alpha}
=i\epsilon_{+\alpha}
-i\frac{M^2}{r^2+M^2}\epsilon_{+\alpha},
$$

$$
														i s_{+\dot\theta}\big(S_M(s)P_L\big)_{\rho\dot\beta}
=\frac{s_{+\dot\theta}s_{\rho\dot\beta}}{s^2+M^2}.
$$

故 12 图的 PV loop 为

$$
														\Gamma_{12;M}^{\rm PV\text{-}loop}{}_{\dot\theta\dot\beta}{}^i{}_j{}^k{}_l
=2i g^2\int_q
\frac{(q-p_2)_{+\dot\theta}(q-p_2)_{+\dot\beta}}{(q^2+M^2)\big((q-p_2)^2+M^2\big)}\,\mathscr C_{12}{}^i{}_j{}^k{}_l
$$

$$
														\qquad
-2i g^2M^2\int_q
\frac{(q-p_2)_{+\dot\theta}(q-p_2)_{+\dot\beta}}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}\,\mathscr C_{12}{}^i{}_j{}^k{}_l.
$$

前一项是 contact/EOM sector，后一项是 anomaly sector：

$$
														\Gamma_{12;M}^{(\rm anom)}{}_{\dot\theta\dot\beta}
=-2i g^2M^2\int_q
\frac{(q-p_2)_{+\dot\theta}(q-p_2)_{+\dot\beta}}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}\,\mathscr C_{12}.
$$

Feynman parameter：

$$
														\frac{1}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}
=2\int_0^1 dx\,dy\,dz\,\delta(1-x-y-z)
\frac{1}{\big[(q+yp_1-zp_2)^2+M^2+\Delta\big]^3},
$$

$$
\Delta=xy\,p_1^2+xz\,p_2^2+yz\,p^2.
$$

令

$$
\ell=q+yp_1-zp_2,\qquad q-p_2=\ell-yp-xp_2.
$$

则

$$
														\Gamma_{12;M}^{(\rm anom)}
=-4i g^2M^2\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
\int_\ell
\frac{(\ell-yp-xp_2)_{+\dot\theta}(\ell-yp-xp_2)_{+\dot\beta}}{(\ell^2+M^2+\Delta)^3}\,\mathscr C_{12}.
$$

只剩 shift piece：

$$
														\Gamma_{12;M}^{(\rm anom)}
=-4i g^2M^2\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
(yp+xp_2)_{+\dot\theta}(yp+xp_2)_{+\dot\beta}
\int_\ell\frac{1}{(\ell^2+M^2+\Delta)^3}\,\mathscr C_{12}.
$$

再用

$$
\int_\ell\frac{1}{(\ell^2+\Omega)^3}=\frac{1}{32\pi^2}\frac{1}{\Omega},
$$

得

$$
														\Gamma_{12;M}^{(\rm anom)}
=-\frac{i g^2}{8\pi^2}
\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
\frac{M^2}{M^2+\Delta}
(yp+xp_2)_{+\dot\theta}(yp+xp_2)_{+\dot\beta}\,\mathscr C_{12}.
$$

取 local part：

$$
														\Gamma_{12}^{(\rm anom,loc)}{}_{\dot\theta\dot\beta}
=-\frac{i g^2}{8\pi^2}
\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
(yp+xp_2)_{+\dot\theta}(yp+xp_2)_{+\dot\beta}\,\mathscr C_{12}.
$$

simplex 积分：

$$
														\int y^2=\frac{1}{12},\qquad
\int y(x+y)=\frac{1}{8},\qquad
\int (x+y)^2=\frac{1}{4}.
$$

于是

$$
														\boxed{
\Gamma_{12}^{(\rm anom,loc)}{}_{\dot\theta\dot\beta}{}^i{}_j{}^k{}_l
=-\frac{i g^2}{96\pi^2}
\Big[
 p_{1,+\dot\theta}p_{1,+\dot\beta}
+3p_{1,+ (\dot\theta}p_{2,+\dot\beta)}
+3p_{2,+\dot\theta}p_{2,+\dot\beta}
\Big]
\mathscr C_{12}{}^i{}_j{}^k{}_l
}.
$$

### Pattern 21

完全平行：

$$
														\boxed{
\Gamma_{21}^{(\rm anom,loc)}{}_{\dot\theta\dot\beta}{}^i{}_j{}^k{}_l
=-\frac{i g^2}{96\pi^2}
\Big[
3p_{1,+\dot\theta}p_{1,+\dot\beta}
+3p_{1,+ (\dot\theta}p_{2,+\dot\beta)}
+p_{2,+\dot\theta}p_{2,+\dot\beta}
\Big]
\mathscr C_{21}{}^i{}_j{}^k{}_l
}.
$$

### Open-index final result

定义

$$
														\Xi_{12,+\dot\theta,+\dot\beta}(p_1,p_2)
:=
 p_{1,+\dot\theta}p_{1,+\dot\beta}
+3p_{1,+ (\dot\theta}p_{2,+\dot\beta)}
+3p_{2,+\dot\theta}p_{2,+\dot\beta},
$$

$$
														\Xi_{21,+\dot\theta,+\dot\beta}(p_1,p_2)
:=
3p_{1,+\dot\theta}p_{1,+\dot\beta}
+3p_{1,+ (\dot\theta}p_{2,+\dot\beta)}
+p_{2,+\dot\theta}p_{2,+\dot\beta}.
$$

则严格的 open-index 1-loop local anomaly 为

$$
														\boxed{
\mathcal I\!\left[
\big(i\nabla_{+\dot\alpha}\bar\lambda^{\dot\alpha},\nabla_{+\dot\theta}\bar\lambda_{\dot\beta}\big)^{(1),\rm loc}{}^i{}_j{}^k{}_l(p)
\right]
=-\frac{i g^2}{96\pi^2}
\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)
\Big[
\Xi_{12,+\dot\theta,+\dot\beta}\,\mathscr C_{12}{}^i{}_j{}^k{}_l
+\Xi_{21,+\dot\theta,+\dot\beta}\,\mathscr C_{21}{}^i{}_j{}^k{}_l
\Big]
}.
$$

并且

$$
														\Gamma_{\dot\theta\dot\beta}^{(\rm anom,loc)}
=\Gamma_{(\dot\theta\dot\beta)}^{(\rm anom,loc)},
$$

即只有 symmetric dotted part survives。

Position-space / covariantized form：

$$
\partial\rightarrow \nabla
$$

在 1-loop order 可直接做 covariantization，因为差别从更高阶开始。

<aside>
💡

### Lie-algebra-index / local-operator rewrite

定义

$$
												\mathcal O_{\dot\theta\dot\beta}^{AB}(x):=
i\nabla_{+\dot\alpha}\bar\lambda^{\dot\alpha A}(x)\,
\nabla_{+\dot\theta}\bar\lambda_{\dot\beta}^{B}(x).
$$

$$
[T^A,T^B]=f^{AB}{}_C\,T^C,\qquad \operatorname{Tr}(T^AT^B)=\delta^{AB}.
$$

$$
												\mathcal O_{\dot\theta\dot\beta}{}^i{}_j{}^k{}_l
=(T^A)^i{}_j(T^B)^k{}_l\,\mathcal O_{\dot\theta\dot\beta}^{AB}.
$$

则

$$
												\mathscr C_{12}{}^i{}_j{}^k{}_l
=(T^A)^i{}_j(T^B)^k{}_l\,\mathscr C_{12}^{AB},
\qquad
\mathscr C_{21}{}^i{}_j{}^k{}_l
=(T^A)^i{}_j(T^B)^k{}_l\,\mathscr C_{21}^{AB},
$$

$$
												\mathscr C_{12}^{AB}(p_1,p_2)
=
\epsilon^{\dot\gamma\dot\delta}
f^{CA}{}_E f^{DB}{}_E\,
\bar\lambda_{\dot\gamma}^{C}(p_1)\bar\lambda_{\dot\delta}^{D}(p_2),
\qquad
\mathscr C_{21}^{AB}(p_1,p_2)=\mathscr C_{12}^{AB}(p_2,p_1).
$$

于是 momentum-space 写成

$$
												\boxed{
\mathcal I\!\left[
\mathcal O_{\dot\theta\dot\beta}^{AB\,(1),\rm loc}(p)
\right]
=
-\frac{i g^2}{96\pi^2}
\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)
\Big[
\Xi_{12,+\dot\theta,+\dot\beta}\,\mathscr C_{12}^{AB}
+
\Xi_{21,+\dot\theta,+\dot\beta}\,\mathscr C_{21}^{AB}
\Big]
}.
$$

合并 $\mathscr C_{21}^{AB}(p_1,p_2)=\mathscr C_{12}^{AB}(p_2,p_1)$ 后，

$$
												\boxed{
\mathcal I\!\left[
\mathcal O_{\dot\theta\dot\beta}^{AB\,(1),\rm loc}(p)
\right]
=
-\frac{i g^2}{48\pi^2}
\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)\,
\Xi_{12,+\dot\theta,+\dot\beta}(p_1,p_2)\,
\epsilon^{\dot\gamma\dot\delta}
f^{CA}{}_E f^{DB}{}_E\,
\bar\lambda_{\dot\gamma}^{C}(p_1)\bar\lambda_{\dot\delta}^{D}(p_2)
}.
$$

记

$$
												\mathcal B_{\dot\theta\dot\beta}^{AB}(x):=
\epsilon^{\dot\gamma\dot\delta}
f^{CA}{}_E f^{DB}{}_E
\Big[
(\nabla_{+(\dot\theta}\nabla_{+\dot\beta)}\bar\lambda_{\dot\gamma}^{C})\bar\lambda_{\dot\delta}^{D}
+3(\nabla_{+(\dot\theta}\bar\lambda_{\dot\gamma}^{C})(\nabla_{+\dot\beta)}\bar\lambda_{\dot\delta}^{D})
+3\bar\lambda_{\dot\gamma}^{C}(\nabla_{+(\dot\theta}\nabla_{+\dot\beta)}\bar\lambda_{\dot\delta}^{D})
\Big].
$$

则 local operator 形式为

$$
												\boxed{
\mathcal O_{\dot\theta\dot\beta}^{AB\,(1),\rm loc}(x)
=
\frac{i g^2}{48\pi^2}\,
\mathcal B_{\dot\theta\dot\beta}^{AB}(x)
},
\qquad
\mathcal O_{\dot\theta\dot\beta}^{AB\,(1),\rm loc}
=
\mathcal O_{(\dot\theta\dot\beta)}^{AB\,(1),\rm loc}.
$$

</aside>

</aside>

<aside>

## $Q_1((\nabla_{+\dot\alpha} f_{++}) f_{++})$

### Setup

沿用同页 conventions：

$$
															Q_- f_{++}= i\nabla_{+\dot\alpha}\bar\lambda^{\dot\alpha},\qquad
Q_-A_{+\dot\theta}= i\bar\lambda_{\dot\theta},\qquad
[Q_-,\nabla_{+\dot\theta}]X=i[\bar\lambda_{\dot\theta},X].
$$

$$
															\mathcal I[\partial_{+\dot\theta}f_{++}(p)]
= i\,p_{+\dot\theta}\,\mathcal I[f_{++}(p)],\qquad
V_{A\lambda\bar\lambda}=V_L-V_R.
$$

PV propagators：

$$
															\langle \Lambda_\alpha(p)\bar\Lambda_{\dot\beta}(-p)\rangle_{\rm PV}
=-\frac{i\,p_{\alpha\dot\beta}}{p^2+M^2},\qquad
\langle B_{\alpha\dot\alpha}(p)B_{\beta\dot\beta}(-p)\rangle_{\rm PV}
=\frac{2\epsilon_{\alpha\beta}\epsilon_{\dot\alpha\dot\beta}}{p^2+M^2}.
$$

并且继续用前页 mixed color tensor $(mathscr F_{12}^{dotbeta},mathscr F_{21}^{dotbeta})$。

定义

$$
\mathcal O_{f\nabla f,\dot\theta}{}^i{}_j{}^k{}_l(x):=f_{++}{}^i{}_j(x)\,\nabla_{+\dot\theta}f_{++}{}^k{}_l(x).
$$

严格写

$$
															Q_-\mathcal O_{f\nabla f,\dot\theta}
=
\underbrace{\big(i\nabla_{+\dot\alpha}\bar\lambda^{\dot\alpha}\big)\,\nabla_{+\dot\theta}f_{++}}_{\text{loop-focus 1}}
+
\underbrace{f_{++}\,\nabla_{+\dot\theta}\big(i\nabla_{+\dot\alpha}\bar\lambda^{\dot\alpha}\big)}_{\text{loop-focus 2}}
+
\underbrace{i\,f_{++}\,[\bar\lambda_{\dot\theta},f_{++}]}_{\text{tree level}}.
$$

下面只算 loop-focus；最后一项不进 1-loop anomaly。

### Ordered pair 先算

定义

$$
															\mathcal O_{\dot\theta}^{\rm mix}{}^i{}_j{}^k{}_l(x):=
i\nabla_{+\dot\alpha}\bar\lambda^{\dot\alpha}{}^i{}_j(x)\,\nabla_{+\dot\theta}f_{++}{}^k{}_l(x).
$$

取决定 universal coefficient 的 two-field triangle piece：

$$
															\mathcal O_{\dot\theta}^{(\partial\partial)}{}^i{}_j{}^k{}_l
:=i\partial_{+\dot\alpha}\bar\lambda^{\dot\alpha}{}^i{}_j\;i\partial_{+\dot\theta}f_{++}^{(\partial)}{}^k{}_l.
$$

动量空间 insertion：

$$
															\mathcal I\!\left[\mathcal O_{\dot\theta}^{(\partial\partial)}(p)\right]
=
\int_{r,s}(2\pi)^4\delta^{(4)}(p-r-s)
(-r_{+\dot\alpha})(i s_{+\dot\theta})
\bar\lambda^{\dot\alpha}(r)\,\mathcal I[f_{++}(s)].
$$

同前页定义

$$
															\mathscr F_{12}^{\dot\beta}
=
\mathscr F_{12}^{(LL)\dot\beta}
+\mathscr F_{12}^{(LR)\dot\beta}
+\mathscr F_{12}^{(RL)\dot\beta}
+\mathscr F_{12}^{(RR)\dot\beta},
\qquad
\mathscr F_{21}^{\dot\beta}(p_1,p_2)=\mathscr F_{12}^{\dot\beta}(p_2,p_1).
$$

其中

$$
															\mathscr F_{12}^{(LL)\dot\beta}{}^i{}_j{}^k{}_l
=\Pi^{mn}{}_{jl}\,f_{++}{}^i{}_m(p_1)\,\bar\lambda^{\dot\beta}{}^k{}_n(p_2),
$$

$$
															\mathscr F_{12}^{(LR)\dot\beta}{}^i{}_j{}^k{}_l
=-\Pi^{mk}{}_{jn}\,f_{++}{}^i{}_m(p_1)\,\bar\lambda^{\dot\beta}{}^n{}_l(p_2),
$$

$$
															\mathscr F_{12}^{(RL)\dot\beta}{}^i{}_j{}^k{}_l
=-\Pi^{in}{}_{ml}\,f_{++}{}^m{}_j(p_1)\,\bar\lambda^{\dot\beta}{}^k{}_n(p_2),
$$

$$
															\mathscr F_{12}^{(RR)\dot\beta}{}^i{}_j{}^k{}_l
=\Pi^{ik}{}_{mn}\,f_{++}{}^m{}_j(p_1)\,\bar\lambda^{\dot\beta}{}^n{}_l(p_2).
$$

### Pattern 12

routing 取

$$
r=q+p_1,\qquad s=p_2-q,\qquad p=p_1+p_2.
$$

写

$$
\big(S_M(k)P_L\big)_{\alpha\dot\alpha}=-\frac{i\,k_{\alpha\dot\alpha}}{k^2+M^2}.
$$

则

$$
															-r_{+\dot\alpha}\big(S_M(r)P_L\big)_\alpha{}^{\dot\alpha}
=
i\epsilon_{+\alpha}-i\frac{M^2}{r^2+M^2}\epsilon_{+\alpha}.
$$

又

$$
															\langle f_{++}(s)\,B_{-\dot\beta}(-s)\rangle_{\rm PV}
=-\frac{i\,s_{+\dot\beta}}{s^2+M^2},
$$

故

$$
															i s_{+\dot\theta}\,\langle f_{++}(s)\,B_{-\dot\beta}(-s)\rangle_{\rm PV}
=\frac{s_{+\dot\theta}s_{+\dot\beta}}{s^2+M^2}.
$$

于是

$$
															\Gamma_{12;M}^{\rm PV\text{-}loop}{}_{\dot\theta}{}^i{}_j{}^k{}_l
=
2i g^2\int_q
\frac{(q-p_2)_{+\dot\theta}(q-p_2)_{+\dot\beta}}{(q^2+M^2)\big((q-p_2)^2+M^2\big)}\,
\mathscr F_{12}^{\dot\beta}{}^i{}_j{}^k{}_l
$$

$$
															\qquad
-2i g^2 M^2\int_q
\frac{(q-p_2)_{+\dot\theta}(q-p_2)_{+\dot\beta}}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}\,
\mathscr F_{12}^{\dot\beta}{}^i{}_j{}^k{}_l.
$$

前一项是 contact/EOM sector；后一项是 anomaly sector。

记

$$
															\Gamma_{12;M}^{({\rm anom})}{}_{\dot\theta}
=
-2i g^2 M^2\int_q
\frac{(q-p_2)_{+\dot\theta}(q-p_2)_{+\dot\beta}}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}\,\mathscr F_{12}^{\dot\beta}.
$$

Feynman parameter：

$$
															\frac{1}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}
=
2\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
\frac{1}{\big[(q+yp_1-zp_2)^2+M^2+\Delta\big]^3},
$$

$$
\Delta=xy\,p_1^2+xz\,p_2^2+yz\,p^2.
$$

令

$$
\ell=q+yp_1-zp_2,\qquad q-p_2=\ell-yp-xp_2.
$$

则只剩 shift piece：

$$
															\Gamma_{12;M}^{({\rm anom})}
=
-4i g^2 M^2\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
(yp+xp_2)_{+\dot\theta}(yp+xp_2)_{+\dot\beta}
\int_\ell\frac{1}{(\ell^2+M^2+\Delta)^3}\,\mathscr F_{12}^{\dot\beta}.
$$

再用

$$
\int_\ell\frac{1}{(\ell^2+\Omega)^3}=\frac{1}{32\pi^2}\frac{1}{\Omega},
$$

得

$$
															\Gamma_{12;M}^{({\rm anom})}
=
-\frac{i g^2}{8\pi^2}
\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
\frac{M^2}{M^2+\Delta}
(yp+xp_2)_{+\dot\theta}(yp+xp_2)_{+\dot\beta}\,\mathscr F_{12}^{\dot\beta}.
$$

取 $(M\to\infty)$ 的 local part：

$$
															\Gamma_{12}^{({\rm anom,loc})}{}_{\dot\theta}
=
-\frac{i g^2}{8\pi^2}
\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
(yp+xp_2)_{+\dot\theta}(yp+xp_2)_{+\dot\beta}\,\mathscr F_{12}^{\dot\beta}.
$$

simplex integrals：

$$
															\int y^2=\frac{1}{12},\qquad
\int y(x+y)=\frac{1}{8},\qquad
\int (x+y)^2=\frac{1}{4}.
$$

定义

$$
															\Xi_{12,+\dot\theta,+\dot\beta}(p_1,p_2)
:=
p_{1,+\dot\theta}p_{1,+\dot\beta}
+3p_{1,+(\dot\theta}p_{2,+\dot\beta)}
+3p_{2,+\dot\theta}p_{2,+\dot\beta},
$$

则

$$
															\boxed{
\Gamma_{12}^{({\rm anom,loc})}{}_{\dot\theta}{}^i{}_j{}^k{}_l
=
-\frac{i g^2}{96\pi^2}
\,\Xi_{12,+\dot\theta,+\dot\beta}(p_1,p_2)
\,\mathscr F_{12}^{\dot\beta}{}^i{}_j{}^k{}_l
}.
$$

### Pattern 21

完全平行。定义

$$
															\Xi_{21,+\dot\theta,+\dot\beta}(p_1,p_2)
:=
3p_{1,+\dot\theta}p_{1,+\dot\beta}
+3p_{1,+(\dot\theta}p_{2,+\dot\beta)}
+p_{2,+\dot\theta}p_{2,+\dot\beta},
$$

则

$$
															\boxed{
\Gamma_{21}^{({\rm anom,loc})}{}_{\dot\theta}{}^i{}_j{}^k{}_l
=
-\frac{i g^2}{96\pi^2}
\,\Xi_{21,+\dot\theta,+\dot\beta}(p_1,p_2)
\,\mathscr F_{21}^{\dot\beta}{}^i{}_j{}^k{}_l
}.
$$

所以 ordered-pair 的 1-loop local anomaly 是

$$
															\boxed{
\mathcal I\!\left[\big(i\nabla_{+\dot\alpha}\bar\lambda^{\dot\alpha},\nabla_{+\dot\theta}f_{++}\big)^{(1),{\rm loc}}{}^i{}_j{}^k{}_l(p)\right]
=
-\frac{i g^2}{96\pi^2}
\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)
\Big[
\Xi_{12,+\dot\theta,+\dot\beta}\,\mathscr F_{12}^{\dot\beta}{}^i{}_j{}^k{}_l
+\Xi_{21,+\dot\theta,+\dot\beta}\,\mathscr F_{21}^{\dot\beta}{}^i{}_j{}^k{}_l
\Big]
}.
$$

### Full $Q_1(f_{++}\nabla_{+\dot\theta}f_{++})$：loop-focus final result

去掉 $[Q_-,\nabla_{+\dot\theta}]$ 的 tree term 后，

$$
															(Q_-f_{++})\,\nabla_{+\dot\theta}f_{++}
+
f_{++}\,\nabla_{+\dot\theta}(Q_-f_{++})
=
\nabla_{+\dot\theta}\big(f_{++}\,Q_-f_{++}\big),
$$

因为 $f_{++}$ 是 bosonic。

因此

$$
															\mathcal I\!\left[Q_1\big(f_{++}\nabla_{+\dot\theta}f_{++}\big){}^i{}_j{}^k{}_l(p)\right]_{\rm loop}
=
i\,p_{+\dot\theta}\,\mathcal I\!\left[Q_1\big(f_{++}f_{++}\big){}^i{}_j{}^k{}_l(p)\right].
$$

代入前页已经得到的

$$
															\mathcal I\!\left[Q_1\big(f_{++}f_{++}\big){}^i{}_j{}^k{}_l(p)\right]
=
-\frac{g^2}{48\pi^2}
\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)
\Big[
(p_1+2p_2)_{+\dot\beta}\,\mathscr F_{12}^{\dot\beta}
+
(2p_1+p_2)_{+\dot\beta}\,\mathscr F_{21}^{\dot\beta}
\Big]{}^i{}_j{}^k{}_l,
$$

得最终 total loop piece：

$$
															\boxed{
\mathcal I\!\left[Q_1\big(f_{++}\nabla_{+\dot\theta}f_{++}\big){}^i{}_j{}^k{}_l(p)\right]_{\rm loop}
=
-\frac{i g^2}{48\pi^2}
\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)\,p_{+\dot\theta}
\Big[
(p_1+2p_2)_{+\dot\beta}\,\mathscr F_{12}^{\dot\beta}
+
(2p_1+p_2)_{+\dot\beta}\,\mathscr F_{21}^{\dot\beta}
\Big]{}^i{}_j{}^k{}_l
}.
$$

</aside>

<aside>

## $Q_1((\nabla_{+\dot\alpha}f_{++})\bar\lambda_{\dot\beta})$

#### Setup

沿用本页 conventions。取 $mathcal O_{dotalphadotbeta}{}^i{}*j{}^k{}_l(x):=(nabla*{+dotalpha}f_{++}){}^i{}*j(x),barlambda*{dotbeta}{}^k{}_l(x)$。

$Q_-f_{++}=inabla_{+dotrho}barlambda^{dotrho},quad Q_-barlambda_{dotbeta}=0,quad [Q_-,nabla_{+dotalpha}]X=i[barlambda_{dotalpha},X]$。

故

$$
Q_1\mathcal O_{\dot\alpha\dot\beta}
=
\underbrace{(i\nabla_{+\dot\alpha}\nabla_{+\dot\rho}\bar\lambda^{\dot\rho})\,\bar\lambda_{\dot\beta}}_{\text{loop-focus}}
+
\underbrace{i[\bar\lambda_{\dot\alpha},f_{++}]\,\bar\lambda_{\dot\beta}}_{\text{tree level}}.
$$

只算 loop/anomaly 部分。沿用前页 propagators、$V_{Alambdabarlambda}=V_L-V_R$、matrix-index / double-line、同一个 $(mathscr C_{12},mathscr C_{21})$、PV collapse identity。

two-field triangle piece：

$$
\mathcal O^{(\partial\partial)}_{\dot\alpha\dot\beta}{}^i{}_j{}^k{}_l
:=
\partial_{+\dot\alpha}\big(i\partial_{+\dot\rho}\bar\lambda^{\dot\rho}{}^i{}_j\big)\,\bar\lambda_{\dot\beta}{}^k{}_l.
$$

动量空间 insertion：

$$
\mathcal I\!\left[\mathcal O^{(\partial\partial)}_{\dot\alpha\dot\beta}(p)\right]
=
\int_{r,s}(2\pi)^4\delta^{(4)}(p-r-s)
(i r_{+\dot\alpha})(-r_{+\dot\rho})
\bar\lambda^{\dot\rho}(r)\bar\lambda_{\dot\beta}(s).
$$

#### Pattern 12

routing：

$$
r=q+p_1,\qquad s=p_2-q,\qquad p=p_1+p_2.
$$

PV propagators：

$$
\langle \Lambda_\alpha(p)\bar\Lambda_{\dot\beta}(-p)\rangle_{\rm PV}
=-\frac{i p_{\alpha\dot\beta}}{p^2+M^2},
\qquad
\langle B_{\alpha\dot\alpha}(p)B_{\beta\dot\beta}(-p)\rangle_{\rm PV}
=\frac{2\epsilon_{\alpha\beta}\epsilon_{\dot\alpha\dot\beta}}{p^2+M^2}.
$$

$$
\big(S_M(k)P_L\big)_{\alpha\dot\alpha}
=-\frac{i k_{\alpha\dot\alpha}}{k^2+M^2}.
$$

collapse：

$$
-r_{+\dot\rho}\big(S_M(r)P_L\big)_\alpha{}^{\dot\rho}
=i\epsilon_{+\alpha}-i\frac{M^2}{r^2+M^2}\epsilon_{+\alpha}.
$$

second fermion line：

$$
\big(S_M(q-p_2)P_L\big)_{\rho\dot\beta}
=-\frac{i (q-p_2)_{\rho\dot\beta}}{(q-p_2)^2+M^2}.
$$

故

$$
\Gamma_{12;M}^{\rm PV\text{-}loop}{}_{\dot\alpha\dot\beta}{}^i{}_j{}^k{}_l
=
-2i g^2\int_q
\frac{(q+p_1)_{+\dot\alpha}(q-p_2)_{+\dot\beta}}
{(q^2+M^2)\big((q-p_2)^2+M^2\big)}
\,\mathscr C_{12}{}^i{}_j{}^k{}_l
$$

$$
\qquad
+
2i g^2M^2\int_q
\frac{(q+p_1)_{+\dot\alpha}(q-p_2)_{+\dot\beta}}
{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}
\,\mathscr C_{12}{}^i{}_j{}^k{}_l.
$$

第一项是 contact/EOM sector。第二项是 anomaly sector：

$$
\Gamma_{12;M}^{(\rm anom)}{}_{\dot\alpha\dot\beta}
=
2i g^2M^2\int_q
\frac{(q+p_1)_{+\dot\alpha}(q-p_2)_{+\dot\beta}}
{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}
\,\mathscr C_{12}.
$$

Feynman parameter：

$$
\frac{1}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}
=
2\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
\frac{1}{\big[(q+yp_1-zp_2)^2+M^2+\Delta\big]^3},
$$

$$
\Delta=xy\,p_1^2+xz\,p_2^2+yz\,p^2.
$$

令

$$
\ell=q+yp_1-zp_2,
$$

则

$$
q+p_1=\ell+zp+xp_1=\ell+(x+z)p_1+z p_2,
$$

$$
q-p_2=\ell-yp-xp_2=\ell-y p_1-(x+y)p_2.
$$

写

$$
X:=(x+z)p_1+z p_2,\qquad Y:=y p_1+(x+y)p_2.
$$

于是

$$
\Gamma_{12;M}^{(\rm anom)}
=
4i g^2M^2\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
\int_\ell
\frac{(\ell+X)_{+\dot\alpha}(\ell-Y)_{+\dot\beta}}
{(\ell^2+M^2+\Delta)^3}
\,\mathscr C_{12}.
$$

$$
\int_\ell \ell_{+\dot\alpha}F(\ell^2)=0,\qquad
\int_\ell \ell_{+\dot\alpha}\ell_{+\dot\beta}F(\ell^2)=0,
$$

故只剩 shift piece：

$$
\Gamma_{12;M}^{(\rm anom)}
=
-4i g^2M^2\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
X_{+\dot\alpha}Y_{+\dot\beta}
\int_\ell\frac{1}{(\ell^2+M^2+\Delta)^3}
\,\mathscr C_{12}.
$$

$$
\int_\ell\frac{1}{(\ell^2+\Omega)^3}
=
\frac{1}{32\pi^2}\frac{1}{\Omega}.
$$

故

$$
\Gamma_{12;M}^{(\rm anom)}
=
-\frac{i g^2}{8\pi^2}
\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
\frac{M^2}{M^2+\Delta}
X_{+\dot\alpha}Y_{+\dot\beta}
\,\mathscr C_{12}.
$$

取 local part：

$$
\Gamma_{12}^{(\rm anom,loc)}{}_{\dot\alpha\dot\beta}
=
-\frac{i g^2}{8\pi^2}
\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
X_{+\dot\alpha}Y_{+\dot\beta}
\,\mathscr C_{12}.
$$

simplex integrals：

$$
\int (x+z)y=\frac{1}{12},\qquad
\int (x+z)(x+y)=\frac{5}{24},\qquad
\int zy=\frac{1}{24},\qquad
\int z(x+y)=\frac{1}{12}.
$$

定义

$$
\Upsilon_{12,+\dot\alpha,+\dot\beta}(p_1,p_2)
:=
2p_{1,+\dot\alpha}p_{1,+\dot\beta}
+5p_{1,+\dot\alpha}p_{2,+\dot\beta}
+p_{2,+\dot\alpha}p_{1,+\dot\beta}
+2p_{2,+\dot\alpha}p_{2,+\dot\beta}.
$$

则

$$
\boxed{
\Gamma_{12}^{(\rm anom,loc)}{}_{\dot\alpha\dot\beta}{}^i{}_j{}^k{}_l
=
-\frac{i g^2}{192\pi^2}
\,\Upsilon_{12,+\dot\alpha,+\dot\beta}(p_1,p_2)
\,\mathscr C_{12}{}^i{}_j{}^k{}_l
}.
$$

#### Pattern 21

完全平行：

$$
\Upsilon_{21,+\dot\alpha,+\dot\beta}(p_1,p_2)
:=
2p_{1,+\dot\alpha}p_{1,+\dot\beta}
+p_{1,+\dot\alpha}p_{2,+\dot\beta}
+5p_{2,+\dot\alpha}p_{1,+\dot\beta}
+2p_{2,+\dot\alpha}p_{2,+\dot\beta}.
$$

$$
\boxed{
\Gamma_{21}^{(\rm anom,loc)}{}_{\dot\alpha\dot\beta}{}^i{}_j{}^k{}_l
=
-\frac{i g^2}{192\pi^2}
\,\Upsilon_{21,+\dot\alpha,+\dot\beta}(p_1,p_2)
\,\mathscr C_{21}{}^i{}_j{}^k{}_l
}.
$$

#### Open-index final result

$$
\boxed{
\mathcal I\!\left[
Q_1\!\Big((\nabla_{+\dot\alpha}f_{++})\,\bar\lambda_{\dot\beta}\Big)_{\rm loop}^{(1),\rm loc}
{}^i{}_j{}^k{}_l(p)
\right]
=
-\frac{i g^2}{192\pi^2}
\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)
\Big[
\Upsilon_{12,+\dot\alpha,+\dot\beta}\,\mathscr C_{12}{}^i{}_j{}^k{}_l
+
\Upsilon_{21,+\dot\alpha,+\dot\beta}\,\mathscr C_{21}{}^i{}_j{}^k{}_l
\Big]
}.
$$

这里 $(\mathscr C_{12},\mathscr C_{21})$ 就是前页已经定义好的 open-index $(\bar\lambda\bar\lambda)$ color-flow tensor。

#### Lie-algebra indices $(A,B,\dots)$

$$
\mathcal O_{\dot\alpha\dot\beta}^{AB}(x)
:=(\nabla_{+\dot\alpha}f_{++}^A)(x)\,\bar\lambda_{\dot\beta}^B(x),
\qquad
[T^A,T^B]=f^{AB}{}_C T^C,
\qquad
\operatorname{Tr}(T^AT^B)=\delta^{AB}.
$$

$$
\mathscr C_{12}^{AB}(p_1,p_2)
=
\epsilon^{\dot\gamma\dot\delta}
f^{CA}{}_E f^{DB}{}_E
\bar\lambda_{\dot\gamma}^{C}(p_1)\bar\lambda_{\dot\delta}^{D}(p_2),
\qquad
\mathscr C_{21}^{AB}(p_1,p_2)=\mathscr C_{12}^{AB}(p_2,p_1).
$$

于是

$$
\boxed{
\mathcal I\!\left[
Q_1\mathcal O_{\dot\alpha\dot\beta}^{AB}(p)
\right]_{\rm loop}^{(1),\rm loc}
=
-\frac{i g^2}{192\pi^2}
\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)
\Big[
\Upsilon_{12,+\dot\alpha,+\dot\beta}\,\mathscr C_{12}^{AB}
+
\Upsilon_{21,+\dot\alpha,+\dot\beta}\,\mathscr C_{21}^{AB}
\Big]
}.
$$

把第二项 rename $(p_1\leftrightarrow p_2)$ 后，

$$
\boxed{
\mathcal I\!\left[
Q_1\mathcal O_{\dot\alpha\dot\beta}^{AB}(p)
\right]_{\rm loop}^{(1),\rm loc}
=
-\frac{i g^2}{96\pi^2}
\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)
\,\Upsilon_{12,+\dot\alpha,+\dot\beta}(p_1,p_2)
\,\mathscr C_{12}^{AB}(p_1,p_2).
$$

#### local operator rewrite

定义

$$
\mathcal K_{\dot\alpha\dot\beta}^{AB}(x)
:=
\epsilon^{\dot\gamma\dot\delta}
f^{CA}{}_E f^{DB}{}_E
\Big[
2(\nabla_{+\dot\alpha}\nabla_{+\dot\beta}\bar\lambda_{\dot\gamma}^{C})\bar\lambda_{\dot\delta}^{D}
+5(\nabla_{+\dot\alpha}\bar\lambda_{\dot\gamma}^{C})(\nabla_{+\dot\beta}\bar\lambda_{\dot\delta}^{D})
$$

$$
\qquad\qquad\qquad\qquad
+(\nabla_{+\dot\beta}\bar\lambda_{\dot\gamma}^{C})(\nabla_{+\dot\alpha}\bar\lambda_{\dot\delta}^{D})
+2\bar\lambda_{\dot\gamma}^{C}(\nabla_{+\dot\alpha}\nabla_{+\dot\beta}\bar\lambda_{\dot\delta}^{D})
\Big].
$$

则

$$
\boxed{
Q_1\mathcal O_{\dot\alpha\dot\beta}^{AB}(x)\Big|_{\rm loop}^{(1),\rm loc}
=
\frac{i g^2}{96\pi^2}
\,\mathcal K_{\dot\alpha\dot\beta}^{AB}(x).
}.
$$

在 1-loop order，

$$
\partial\rightarrow\nabla
$$

的 covariantization 直接成立。

#### consistency check

由

$$
\nabla_{+\dot\alpha}\Big(i\nabla_{+\dot\rho}\bar\lambda^{\dot\rho}\,\bar\lambda_{\dot\beta}\Big)
=
\Big(i\nabla_{+\dot\alpha}\nabla_{+\dot\rho}\bar\lambda^{\dot\rho}\Big)\bar\lambda_{\dot\beta}
+
\Big(i\nabla_{+\dot\rho}\bar\lambda^{\dot\rho}\Big)\nabla_{+\dot\alpha}\bar\lambda_{\dot\beta},
$$

得

$$
Q_1\!\Big((\nabla_{+\dot\alpha}f_{++})\bar\lambda_{\dot\beta}\Big)_{\rm loop}
=
\nabla_{+\dot\alpha}Q_1\!\Big(f_{++}\bar\lambda_{\dot\beta}\Big)_{\rm loop}
-
Q_1\!\Big(f_{++}\nabla_{+\dot\alpha}\bar\lambda_{\dot\beta}\Big)_{\rm loop},
$$

代入前页两个已算结果，正好给出上面的 $(Upsilon_{12},Upsilon_{21})$。

![image.png](%E7%9B%B4%E6%8E%A51-loop%20level%E8%AE%A1%E7%AE%97/image%203.png)

</aside>

<aside>

## $Q_1((\nabla_{+\dot\alpha}f_{++})\nabla_{+\dot\beta} \bar\lambda_{\dot \gamma})$

### 2. $Q_1$ 的 split

取

$$
\mathcal O_{\dot\alpha\dot\beta\dot\gamma}{}^i{}_j{}^k{}_l(x):=\nabla_{+\dot\alpha}f_{++}{}^i{}_j(x)\,\nabla_{+\dot\beta}\bar\lambda_{\dot\gamma}{}^k{}_l(x).
$$

沿用本页 propagators, $V_{Alambdabarlambda}=V_L-V_R$, $Q_-f_{++}=inabla_{+dotrho}barlambda^{dotrho}$, $Q_-barlambda_{dotgamma}=0$, 同一个 $mathscr C_{12},mathscr C_{21}$, 以及 PV collapse identity.

完整地

$$
	Q_1\mathcal O_{\dot\alpha\dot\beta\dot\gamma}
=
\underbrace{\big(i\nabla_{+\dot\alpha}\nabla_{+\dot\rho}\bar\lambda^{\dot\rho}\big)\,\nabla_{+\dot\beta}\bar\lambda_{\dot\gamma}}_{\text{loop-focus}}+\underbrace{i[\bar\lambda_{\dot\alpha},f_{++}]\,\nabla_{+\dot\beta}\bar\lambda_{\dot\gamma}+i\nabla_{+\dot\alpha}f_{++}\,[\bar\lambda_{\dot\beta},\bar\lambda_{\dot\gamma}]}_{\text{tree level}}.
$$

只算 loop/anomaly 部分：

$$
\mathcal O^{\rm loop}_{\dot\alpha\dot\beta\dot\gamma}{}^i{}_j{}^k{}_l:=i\nabla_{+\dot\alpha}\nabla_{+\dot\rho}\bar\lambda^{\dot\rho}{}^i{}_j\,\nabla_{+\dot\beta}\bar\lambda_{\dot\gamma}{}^k{}_l.
$$

其 two-field triangle piece：

$$
\mathcal O^{(\partial\partial\partial)}_{\dot\alpha\dot\beta\dot\gamma}{}^i{}_j{}^k{}_l:=i\partial_{+\dot\alpha}\partial_{+\dot\rho}\bar\lambda^{\dot\rho}{}^i{}_j\,i\partial_{+\dot\beta}\bar\lambda_{\dot\gamma}{}^k{}_l.
$$

动量空间 insertion：

$$
\mathcal I\!\left[\mathcal O^{(\partial\partial\partial)}_{\dot\alpha\dot\beta\dot\gamma}(p)\right]=\int_{r,s}(2\pi)^4\delta^{(4)}(p-r-s)\,(i r_{+\dot\alpha})(-r_{+\dot\rho})(i s_{+\dot\beta})\,\bar\lambda^{\dot\rho}(r)\bar\lambda_{\dot\gamma}(s).
$$

并记

$$
\mathscr C_{21}{}^i{}_j{}^k{}_l(p_1,p_2)=\mathscr C_{12}{}^i{}_j{}^k{}_l(p_2,p_1).
$$

### 3. Pattern 12

routing：

$$
r=q+p_1,\qquad s=p_2-q,\qquad p=p_1+p_2.
$$

PV propagators：

$$
\langle \Lambda_\alpha(p)\bar\Lambda_{\dot\beta}(-p)\rangle_{\rm PV}=-\frac{i p_{\alpha\dot\beta}}{p^2+M^2},\qquad \langle B_{\alpha\dot\alpha}(p)B_{\beta\dot\beta}(-p)\rangle_{\rm PV}=\frac{2\epsilon_{\alpha\beta}\epsilon_{\dot\alpha\dot\beta}}{p^2+M^2}.
$$

$$
\big(S_M(k)P_L\big)_{\alpha\dot\alpha}=-\frac{i k_{\alpha\dot\alpha}}{k^2+M^2}.
$$

collapse:

$$
-r_{+\dot\rho}\big(S_M(r)P_L\big)_\alpha{}^{\dot\rho}=i\epsilon_{+\alpha}-i\frac{M^2}{r^2+M^2}\epsilon_{+\alpha},
$$

$$
i s_{+\dot\beta}\big(S_M(s)P_L\big)_{\rho\dot\gamma}=\frac{s_{+\dot\beta}s_{\rho\dot\gamma}}{s^2+M^2}.
$$

故

$$
\Gamma_{12;M}^{\rm PV\text{-}loop}{}_{\dot\alpha\dot\beta\dot\gamma}{}^i{}_j{}^k{}_l=-2 g^2\int_q\frac{(q+p_1)_{+\dot\alpha}(q-p_2)_{+\dot\beta}(q-p_2)_{+\dot\gamma}}{(q^2+M^2)\big((q-p_2)^2+M^2\big)}\,\mathscr C_{12}{}^i{}_j{}^k{}_l
$$

$$
\qquad+2 g^2 M^2\int_q\frac{(q+p_1)_{+\dot\alpha}(q-p_2)_{+\dot\beta}(q-p_2)_{+\dot\gamma}}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}\,\mathscr C_{12}{}^i{}_j{}^k{}_l.
$$

前一项是 contact/EOM sector，后一项是 anomaly sector：

$$
\Gamma_{12;M}^{(\rm anom)}{}_{\dot\alpha\dot\beta\dot\gamma}=2 g^2 M^2\int_q\frac{(q+p_1)_{+\dot\alpha}(q-p_2)_{+\dot\beta}(q-p_2)_{+\dot\gamma}}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}\,\mathscr C_{12}.
$$

Feynman parameter：

$$
\frac{1}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}=2\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)\,\frac{1}{\big[(q+yp_1-zp_2)^2+M^2+\Delta\big]^3},
$$

$$
\Delta=xy\,p_1^2+xz\,p_2^2+yz\,p^2.
$$

令

$$
\ell=q+yp_1-zp_2.
$$

则

$$
q+p_1=\ell+z p+x p_1,\qquad q-p_2=\ell-y p-x p_2.
$$

故

$$
\Gamma_{12;M}^{(\rm anom)}=4 g^2 M^2\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)\int_\ell\frac{(\ell+z p+x p_1)_{+\dot\alpha}(\ell-y p-x p_2)_{+\dot\beta}(\ell-y p-x p_2)_{+\dot\gamma}}{(\ell^2+M^2+\Delta)^3}\,\mathscr C_{12}.
$$

$$
\int_\ell \ell_{+\dot\mu}F(\ell^2)=0,\qquad \int_\ell \ell_{+\dot\mu}\ell_{+\dot\nu}F(\ell^2)=0,\qquad \int_\ell \ell_{+\dot\mu}\ell_{+\dot\nu}\ell_{+\dot\rho}F(\ell^2)=0.
$$

只剩 shift piece：

$$
\Gamma_{12;M}^{(\rm anom)}=4 g^2 M^2\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)\,(z p+x p_1)_{+\dot\alpha}(y p+x p_2)_{+\dot\beta}(y p+x p_2)_{+\dot\gamma}\int_\ell\frac{1}{(\ell^2+M^2+\Delta)^3}\,\mathscr C_{12}.
$$

$$
\int_\ell\frac{1}{(\ell^2+\Omega)^3}=\frac{1}{32\pi^2}\frac{1}{\Omega}.
$$

于是 local part：

$$
\Gamma_{12}^{(\rm anom,loc)}{}_{\dot\alpha\dot\beta\dot\gamma}=\frac{g^2}{8\pi^2}\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)\,(z p+x p_1)_{+\dot\alpha}(y p+x p_2)_{+\dot\beta}(y p+x p_2)_{+\dot\gamma}\,\mathscr C_{12}.
$$

写成

$$
z p+x p_1=(x+z)p_1+z p_2,\qquad y p+x p_2=y p_1+(x+y)p_2.
$$

simplex 积分：

$$
\int (x+z)y^2=\frac{1}{30},\qquad \int (x+z)y(x+y)=\frac{7}{120},\qquad \int (x+z)(x+y)^2=\frac{3}{20},
$$

$$
\int z y^2=\frac{1}{60},\qquad \int z y(x+y)=\frac{1}{40},\qquad \int z(x+y)^2=\frac{1}{20}.
$$

定义

$$
\Omega_{12,+\dot\alpha,+\dot\beta,+\dot\gamma}(p_1,p_2):=2\,p_{1,+\dot\alpha}p_{1,+\dot\beta}p_{1,+\dot\gamma}+7\,p_{1,+\dot\alpha}p_{1,+(\dot\beta}p_{2,+\dot\gamma)}+9\,p_{1,+\dot\alpha}p_{2,+\dot\beta}p_{2,+\dot\gamma}
$$

$$
\qquad\qquad+p_{2,+\dot\alpha}p_{1,+\dot\beta}p_{1,+\dot\gamma}+3\,p_{2,+\dot\alpha}p_{1,+(\dot\beta}p_{2,+\dot\gamma)}+3\,p_{2,+\dot\alpha}p_{2,+\dot\beta}p_{2,+\dot\gamma}.
$$

则

$$
\boxed{\Gamma_{12}^{(\rm anom,loc)}{}_{\dot\alpha\dot\beta\dot\gamma}{}^i{}_j{}^k{}_l=\frac{g^2}{480\pi^2}\,\Omega_{12,+\dot\alpha,+\dot\beta,+\dot\gamma}(p_1,p_2)\,\mathscr C_{12}{}^i{}_j{}^k{}_l}.
$$

并且

$$
\Gamma_{12}^{(\rm anom,loc)}{}_{\dot\alpha\dot\beta\dot\gamma}=\Gamma_{12}^{(\rm anom,loc)}{}_{\dot\alpha(\dot\beta\dot\gamma)}.
$$

### 4. Pattern 21

完全平行：

$$
\Omega_{21,+\dot\alpha,+\dot\beta,+\dot\gamma}(p_1,p_2):=\Omega_{12,+\dot\alpha,+\dot\beta,+\dot\gamma}(p_2,p_1),
$$

即

$$
\Omega_{21,+\dot\alpha,+\dot\beta,+\dot\gamma}=3\,p_{1,+\dot\alpha}p_{1,+\dot\beta}p_{1,+\dot\gamma}+3\,p_{1,+\dot\alpha}p_{1,+(\dot\beta}p_{2,+\dot\gamma)}+p_{1,+\dot\alpha}p_{2,+\dot\beta}p_{2,+\dot\gamma}
$$

$$
\qquad\qquad+9\,p_{2,+\dot\alpha}p_{1,+\dot\beta}p_{1,+\dot\gamma}+7\,p_{2,+\dot\alpha}p_{1,+(\dot\beta}p_{2,+\dot\gamma)}+2\,p_{2,+\dot\alpha}p_{2,+\dot\beta}p_{2,+\dot\gamma}.
$$

$$
\boxed{\Gamma_{21}^{(\rm anom,loc)}{}_{\dot\alpha\dot\beta\dot\gamma}{}^i{}_j{}^k{}_l=\frac{g^2}{480\pi^2}\,\Omega_{21,+\dot\alpha,+\dot\beta,+\dot\gamma}(p_1,p_2)\,\mathscr C_{21}{}^i{}_j{}^k{}_l}.
$$

### 5. Open-index final result

$$
\boxed{\mathcal I\!\left[Q_1\!\left(\nabla_{+\dot\alpha}f_{++}\,\nabla_{+\dot\beta}\bar\lambda_{\dot\gamma}\right)_{\rm loop}^{(1),\rm loc}{}^i{}_j{}^k{}_l(p)\right]=\frac{g^2}{480\pi^2}\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)\Big[\Omega_{12,+\dot\alpha,+\dot\beta,+\dot\gamma}\,\mathscr C_{12}{}^i{}_j{}^k{}_l+\Omega_{21,+\dot\alpha,+\dot\beta,+\dot\gamma}\,\mathscr C_{21}{}^i{}_j{}^k{}_l\Big]}.
$$

只对 $(\dot\beta\dot\gamma)$ symmetric。

$$
Q_1(\cdots)=Q_1(\cdots)_{\rm tree}+Q_1(\cdots)_{\rm loop},
$$

上框是 loop/anomaly 部分。

### 6. Lie-algebra indices $(A,B,\dots)$

定义

$$
\mathcal O_{\dot\alpha\dot\beta\dot\gamma}^{AB}(x):=\nabla_{+\dot\alpha}f_{++}^A(x)\,\nabla_{+\dot\beta}\bar\lambda_{\dot\gamma}^B(x),\qquad [T^A,T^B]=f^{AB}{}_C T^C,\qquad \operatorname{Tr}(T^AT^B)=\delta^{AB}.
$$

$$
\mathscr C_{12}^{AB}(p_1,p_2)=\epsilon^{\dot\delta\dot\epsilon}f^{CA}{}_E f^{DB}{}_E\,\bar\lambda_{\dot\delta}^C(p_1)\bar\lambda_{\dot\epsilon}^D(p_2),\qquad \mathscr C_{21}^{AB}(p_1,p_2)=\mathscr C_{12}^{AB}(p_2,p_1).
$$

这正是前页 $\mathscr C_{12},\mathscr C_{21}$ 的 Lie-algebra rewrite。把第二项 $p_1\leftrightarrow p_2$ 重命名后，

$$
\boxed{\mathcal I\!\left[Q_1\mathcal O_{\dot\alpha\dot\beta\dot\gamma}^{AB}(p)\right]_{\rm loop}^{(1),\rm loc}=\frac{g^2}{240\pi^2}\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)\,\Omega_{12,+\dot\alpha,+\dot\beta,+\dot\gamma}(p_1,p_2)\,\mathscr C_{12}^{AB}(p_1,p_2)}.
$$

### 7. Local operator rewrite

定义

$$
\mathcal K_{\dot\alpha\dot\beta\dot\gamma}^{AB}(x):=\epsilon^{\dot\delta\dot\epsilon}f^{CA}{}_E f^{DB}{}_E\Big[2\,(\nabla_{+\dot\alpha}\nabla_{+\dot\beta}\nabla_{+\dot\gamma}\bar\lambda_{\dot\delta}^C)\,\bar\lambda_{\dot\epsilon}^D+7\,(\nabla_{+\dot\alpha}\nabla_{+(\dot\beta}\bar\lambda_{\dot\delta}^C)(\nabla_{+\dot\gamma)}\bar\lambda_{\dot\epsilon}^D)+9\,(\nabla_{+\dot\alpha}\bar\lambda_{\dot\delta}^C)(\nabla_{+\dot\beta}\nabla_{+\dot\gamma}\bar\lambda_{\dot\epsilon}^D)
$$

$$
\qquad\qquad+(\nabla_{+\dot\beta}\nabla_{+\dot\gamma}\bar\lambda_{\dot\delta}^C)(\nabla_{+\dot\alpha}\bar\lambda_{\dot\epsilon}^D)+3\,(\nabla_{+(\dot\beta}\bar\lambda_{\dot\delta}^C)(\nabla_{+\dot\alpha}\nabla_{+\dot\gamma)}\bar\lambda_{\dot\epsilon}^D)+3\,\bar\lambda_{\dot\delta}^C(\nabla_{+\dot\alpha}\nabla_{+\dot\beta}\nabla_{+\dot\gamma}\bar\lambda_{\dot\epsilon}^D)\Big].
$$

则

$$
\boxed{Q_1\mathcal O_{\dot\alpha\dot\beta\dot\gamma}^{AB}(x)\Big\|_{\rm loop}^{(1),\rm loc}=\frac{i g^2}{240\pi^2}\,\mathcal K_{\dot\alpha\dot\beta\dot\gamma}^{AB}(x)},\qquad \mathcal K_{\dot\alpha\dot\beta\dot\gamma}^{AB}=\mathcal K_{\dot\alpha(\dot\beta\dot\gamma)}^{AB}.
$$

同样地，在 1-loop order 可直接取 $\partial\to\nabla$ 做 covariantization。

</aside>

# Generating function of derivatives$Q_1(f_{++}e^{w\nabla}f_{++})$(Full One loop result)(Weird)

![image.png](%E7%9B%B4%E6%8E%A51-loop%20level%E8%AE%A1%E7%AE%97/image%204.png)

#### Setup

定义

$$
w\cdot \nabla_+ := w^{+\dot\alpha}\nabla_{+\dot\alpha},
\qquad
w\cdot p_a := w^{+\dot\alpha}p_{a,+\dot\alpha}.
$$

$$
\mathcal O_w{}^i{}_j{}^k{}_l(x):=f_{++}{}^i{}_j(x)e^{w\cdot \nabla_+}f_{++}{}^k{}_l(x).
$$

#### **只保留 loop-focus：**

$$
Q_1\mathcal O_w
\underbrace{
 i\nabla_{+\dot\rho}\bar\lambda^{\dot\rho},e^{,w\cdot \nabla_+}f_{++}
}_{\text{hit first }f_{++}}
+
\underbrace{
 f_{++},e^{,w\cdot \nabla_+}\big(i\nabla_{+\dot\rho}\bar\lambda^{\dot\rho}\big)
}_{\text{hit second }f_{++}}
+
\text{tree from }[Q_-,\nabla_+].
$$

tree pieces 全部丢开；只算 anomaly。沿用前页 propagators、$(V_{A\lambda\bar\lambda}=V_L-V_R)$、matrix-index / double-line、以及 mixed color tensor $(\mathscr F_{12}^{\dot\beta},\mathscr F_{21}^{\dot\beta})$。

$$
\mathscr F_{12}^{\dot\beta}{}^i{}_j{}^k{}_l
$$

$$
\Pi^{mn}{}_{jl},f_{++}{}^i{}_m(p_1)\bar\lambda^{\dot\beta}{}^k{}_n(p_2)-\Pi^{mk}{}_{jn},f_{++}{}^i{}_m(p_1)\bar\lambda^{\dot\beta}{}^n{}_l(p_2)
$$

$$
\qquad-\Pi^{in}{}_{ml},f_{++}{}^m{}_j(p_1)\bar\lambda^{\dot\beta}{}^k{}_n(p_2)+\Pi^{ik}{}_{mn},f_{++}{}^m{}_j(p_1)\bar\lambda^{\dot\beta}{}^n{}_l(p_2),
$$

$$
\mathscr F_{21}^{\dot\beta}(p_1,p_2)=\mathscr F_{12}^{\dot\beta}(p_2,p_1).
$$

#### **Pattern 12**

对应 $(\mathscr F_{12}^{\dot\beta})$ 的 ordered contribution。two-field PV loop 直接写成

$$
\Gamma_{12;M}^{\rm PV\text{-}loop}{}^i{}_j{}^k{}_l(w)
$$

$$
2g^2\int_q
e^{,i w\cdot (p_2-q)}
\frac{(q-p_2)^{+\dot\beta}}{(q^2+M^2)\big((q-p_2)^2+M^2\big)},\mathscr F_{12}^{\dot\beta}{}^i{}_j{}^k{}_l
$$

$$
\qquad-2g^2M^2\int_qe^{,i w\cdot (p_2-q)}\frac{(q-p_2)^{+\dot\beta}}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)},\mathscr F_{12}^{\dot\beta}{}^i{}_j{}^k{}_l.
$$

前一项 (=) contact/EOM。后一项 (=) anomaly：

$$
\Gamma_{12;M}^{(\rm anom)}=-2g^2M^2\int_q
e^{,i w\cdot (p_2-q)}
\frac{(q-p_2)^{+\dot\beta}}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)},\mathscr F_{12}^{\dot\beta}.
$$

Feynman parameter：

$$
\frac{1}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}
$$

$$
2\int_\Delta
\frac{1}{\big[(q+yp_1-zp_2)^2+M^2+\Delta\big]^3},
$$

$$
\int_\Delta := \int_0^1dx\,dy\,dz\,\delta(1-x-y-z),
\qquad
\Delta=xy\,p_1^2+xz\,p_2^2+yz\,p^2.
$$

令

$$
\ell=q+yp_1-zp_2,
\qquad
q-p_2=\ell-Y_{12},
\qquad
Y_{12}:= y\,p_1+(x+y)\,p_2.
$$

则

$$
e^{,i w\cdot(p_2-q)}=e^{,i w\cdot Y_{12}}e^{-i w\cdot \ell}.
$$

而

$$
\int_\ell e^{-i w\cdot \ell},\ell_{+\dot\alpha_1}\cdots \ell_{+\dot\alpha_n}F(\ell^2)=0,
\qquad n\ge 1,
$$

因为 tensor reduction 必含 $(\epsilon_{\alpha\beta})$，而这里所有 undotted index 都是 $(+)$，故 $(\epsilon_{++}=0)$。

于是只剩 shift piece：

$$
\Gamma_{12;M}^{(\rm anom)}
$$

$$
4g^2M^2\int_\Delta
 e^{,i w\cdot Y_{12}},
 Y_{12,+\dot\beta}
\int_\ell\frac{1}{(\ell^2+M^2+\Delta)^3}
,
\mathscr F_{12}^{\dot\beta}.
$$

$$
\int_\ell\frac{1}{(\ell^2+\Omega)^3}=\frac{1}{32\pi^2}\frac{1}{\Omega}.
$$

故 local part：

$$
\boxed{\Gamma_{12}^{(\rm anom,loc)}{}^i{}_j{}^k{}_l(w)
-
\frac{g^2}{8\pi^2}
\int_\Delta
 e^{,i w\cdot Y_{12}},
 Y_{12,+\dot\beta},
 \mathscr F_{12}^{\dot\beta}{}^i{}_j{}^k{}_l
}.
$$

#### **Pattern 21**

完全平行：

$$
Y_{21}:=(x+y)\,p_1+y\,p_2.
$$

$$
\boxed{\Gamma_{21}^{(\rm anom,loc)}{}^i{}_j{}^k{}_l(w)
-
\frac{g^2}{8\pi^2}
\int_\Delta
 e^{,i w\cdot Y_{21}},
 Y_{21,+\dot\beta},
 \mathscr F_{21}^{\dot\beta}{}^i{}_j{}^k{}_l
}.
$$

#### **Open-index final result**

$$
\boxed{\mathcal I![Q_1!\Big(f_{++},e^{,w\cdot \nabla_+}f_{++}\Big)_{\rm loop}^{(1),\rm loc}{}^i{}_j{}^k{}_l(p)
-
\frac{g^2}{8\pi^2}
\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)
\Big[
\mathcal G_{12,+\dot\beta}(w;p_1,p_2),\mathscr F_{12}^{\dot\beta}{}^i{}_j{}^k{}_l+\mathcal G_{21,+\dot\beta}(w;p_1,p_2),\mathscr F_{21}^{\dot\beta}{}^i{}_j{}^k{}_l
\Big].
}
$$

其中

$$
\mathcal G_{12,+\dot\beta}(w;p_1,p_2):=\int_\Delta e^{,i w\cdot Y_{12}},Y_{12,+\dot\beta},\qquad\mathcal G_{21,+\dot\beta}(w;p_1,p_2):=\int_\Delta e^{,i w\cdot Y_{21}},Y_{21,+\dot\beta}.
$$

这已经是 exact compact form。(w=0) 立即回到已知

$$
\mathcal G_{12,+\dot\beta}(0)=\frac16(p_1+2p_2)^{+\dot\beta},\qquad \mathcal G_{21,+\dot\beta}(0)=\frac16(2p_1+p_2)^{+\dot\beta},
$$

所以

$$
\mathcal I[Q_1(f_{++}f_{++})]
-
\frac{g^2}{48\pi^2}
\int_{p_1,p_2}\delta^{(4)}(p-p_1-p_2)
\Big[
(p_1+2p_2)^{+\dot\beta}\mathscr F_{12}^{\dot\beta}
+
(2p_1+p_2)^{+\dot\beta}\mathscr F_{21}^{\dot\beta}
\Big].
$$

#### **closed form for the generating kernel**

记

$$
u_1:= i\,w\cdot p_1,\qquad \nu_2:= i\,w\cdot p_2.
$$

定义 scalar kernels

$$
\mathcal K_{12}(\nu_1,\nu_2):=\int_\Delta e^{,y \nu_1+(x+y)\nu_2}
\frac{\nu_1+\nu_2 e^{\nu_1+\nu_2}-(\nu_1+\nu_2)e^{\nu_2}}{\nu_1\nu_2(\nu_1+\nu_2)},
$$

$$
\mathcal K_{21}(\nu_1,\nu_2):=\int_\Delta e^{,(x+y)\nu_1+y \nu_2}
\frac{\nu_2+\nu_1 e^{\nu_1+\nu_2}-(\nu_1+\nu_2)e^{\nu_1}}{\nu_1\nu_2(\nu_1+\nu_2)}.
$$

则

$$
\mathcal G_{12,+\dot\beta}
\frac1{i},\frac{\partial \mathcal K_{12}}{\partial w^{+\dot\beta}},\qquad\mathcal G_{21,+\dot\beta}
\frac1{i},\frac{\partial \mathcal K_{21}}{\partial w^{+\dot\beta}}.
$$

#### **(w)-power expansion**

$$
\mathcal G_{12,+\dot\beta}
\sum_{n\ge0}\frac{i^n}{n!},w^{+\dot\alpha_1}\cdots w^{+\dot\alpha_n}\int_\Delta Y_{12,+\dot\alpha_1}\cdots Y_{12,+\dot\alpha_n}Y_{12,+\dot\beta},
$$

$$
\mathcal G_{21,+\dot\beta}
\sum_{n\ge0}\frac{i^n}{n!},
 w^{+\dot\alpha_1}\cdots w^{+\dot\alpha_n}
\int_\Delta
Y_{21,+\dot\alpha_1}\cdots Y_{21,+\dot\alpha_n}Y_{21,+\dot\beta}.
$$

前两阶：

$$
\mathcal G_{12,+\dot\beta}
\frac16(p_1+2p_2)^{+\dot\beta}+\frac{i}{12},w^{+\dot\theta},\Xi_{12,+\dot\theta,+\dot\beta}+O(w^2),
$$

$$
\mathcal G_{21,+\dot\beta}
\frac16(2p_1+p_2)^{+\dot\beta}+\frac{i}{12},w^{+\dot\theta},\Xi_{21,+\dot\theta,+\dot\beta}+O(w^2),
$$

其中

$$
\Xi_{12,+\dot\theta,+\dot\beta}
 p_{1,+\dot\theta}p_{1,+\dot\beta}+3p_{1,+(\dot\theta}p_{2,+\dot\beta)}+3p_{2,+\dot\theta}p_{2,+\dot\beta},
$$

$$
\Xi_{21,+\dot\theta,+\dot\beta}
3p_{1,+\dot\theta}p_{1,+\dot\beta}+3p_{1,+(\dot\theta}p_{2,+\dot\beta)}+p_{2,+\dot\theta}p_{2,+\dot\beta}.
$$

所以

$$
\mathcal I![Q_1!\Big(f_{++}e^{,w\cdot \nabla_+}f_{++}\Big)_{\rm loop}^{(1),\rm loc}]
-
\frac{g^2}{48\pi^2}\Big[(p_1+2p_2)^{+\dot\beta}\mathscr F_{12}^{\dot\beta}
+(2p_1+p_2)^{+\dot\beta}\mathscr F_{21}^{\dot\beta}\Big]
$$

$$
\qquad
-\frac{i g^2}{96\pi^2},
 w^{+\dot\theta}
\Big[
\Xi_{12,+\dot\theta,+\dot\beta}\mathscr F_{12}^{\dot\beta}
+
\Xi_{21,+\dot\theta,+\dot\beta}\mathscr F_{21}^{\dot\beta}
\Big]
+O(w^2).
$$

#### **Lie-algebra indices (A,B,dots)**

$$
[T^A,T^B]=f^{AB}{}_C,T^C,
\qquad
\operatorname{Tr}(T^AT^B)=\delta^{AB}.
$$

$$
\mathcal O_w^{AB}(x):=
 f_{++}^A(x),e^{,w\cdot \nabla_+}f_{++}^B(x).
$$

$$
\mathscr F_{12}^{AB,\dot\beta}
 f^{CE}{}_A f^{DE}{}_B,f_{++}^C(p_1)\bar\lambda^{\dot\beta D}(p_2),\qquad\mathscr F_{21}^{AB,\dot\beta}
 f^{CE}{}_A f^{DE}{}_B,f_{++}^C(p_2)\bar\lambda^{\dot\beta D}(p_1).
$$

于是

$$
\boxed{\mathcal I![Q_1\mathcal O_w^{AB}(p)]_{\rm loop}^{(1),\rm loc}
-
\frac{g^2}{8\pi^2}
\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)
\Big[
\mathcal G_{12,+\dot\beta}(w;p_1,p_2),\mathscr F_{12}^{AB,\dot\beta}
+
\mathcal G_{21,+\dot\beta}(w;p_1,p_2),\mathscr F_{21}^{AB,\dot\beta}
\Big].
}
$$

#### **local-operator rewrite**

formal two-slot derivatives：

$$
\nabla_{+\dot\beta}^{(1)}\big(X(x_1)Y(x_2)\big)
:=
(\nabla_{+\dot\beta}X)(x_1),Y(x_2),
\qquad
\nabla_{+\dot\beta}^{(2)}\big(X(x_1)Y(x_2)\big)
:=
X(x_1),(\nabla_{+\dot\beta}Y)(x_2).
$$

定义

$$
\mathbb D_{12,+\dot\beta}(w)
:=
\int_\Delta
 e^{,w\cdot\big(y\nabla_+^{(1)}+(x+y)\nabla_+^{(2)}\big)}
\Big(y\nabla_{+\dot\beta}^{(1)}+(x+y)\nabla_{+\dot\beta}^{(2)}\Big),
$$

$$
\mathbb D_{21,+\dot\beta}(w)
:=
\int_\Delta
 e^{,w\cdot\big((x+y)\nabla_+^{(1)}+y\nabla_+^{(2)}\big)}
\Big((x+y)\nabla_{+\dot\beta}^{(1)}+y\nabla_{+\dot\beta}^{(2)}\Big).
$$

则 exact local-operator form 可写成

$$
\boxed{Q_1\mathcal O_w^{AB}(x)\Big\|_{\rm loop}^{(1),\rm loc}
\frac{i g^2}{8\pi^2},
 f^{CE}{}_A f^{DE}{}_B\Big[\mathbb D_{12,+\dot\beta}(w),f_{++}^C(x_1)\bar\lambda^{\dot\beta D}(x_2)+\mathbb D_{21,+\dot\beta}(w),f_{++}^C(x_2)\bar\lambda^{\dot\beta D}(x_1)\Big]_{x_1=x_2=x}.
}
$$

这就是 compact generating-function form。

# $Q_1(e^{w\nabla}f_{++} f_{++})$

这次只比上一条多一件事：指数放在 **第一 slot**。

$$
w\cdot\nabla_+ := w^{+\dot\alpha}\nabla_{+\dot\alpha},\qquad
w\cdot p_a := w^{+\dot\alpha}p_{a,+\dot\alpha}.
$$

$$
\mathcal O_w{}^i{}_j{}^k{}_l(x):=\big(e^{w\cdot\nabla_+}f_{++}\big)^i{}_j(x),f_{++}^k{}_l(x).
$$

只保留 loop-focus：

$$
Q_1\mathcal O_w
$$

tree pieces 全部略去。

$$
\mathscr F_{21}^{\dot\beta}(p_1,p_2)=\mathscr F_{12}^{\dot\beta}(p_2,p_1).
$$

**Pattern 12**

对应的 PV triangle 只是在 $(Q_1(f_{++}f_{++}))$ 的 12 图上多了第一 slot 的 phase

$$
e^{i w\cdot r},\qquad r=q+p_1.
$$

所以

$$
\Gamma_{12;M}^{\rm PV\text{-}loop}{}^i{}_j{}^k{}_l(w)
$$

前一项 $(=)$ contact/EOM。

后一项 $(=)$ anomaly。

**Pattern 21**

完全平行。

$$
X_{21}:=z p_1+(x+z)p_2,\qquad
Y_{21}:=(x+y)p_1+y p_2.
$$

$$
\boxed{\Gamma_{21}^{(\rm anom,loc)}{}^i{}_j{}^k{}_l(w)}
$$

**Open-index final result**

定义

$$
\widehat{\mathcal G}_{12,+\dot\beta}(w;p_1,p_2):=\int_\Delta e^{i w\cdot X_{12}},Y_{12,+\dot\beta},\qquad\widehat{\mathcal G}_{21,+\dot\beta}(w;p_1,p_2):=\int_\Delta e^{i w\cdot X_{21}},Y_{21,+\dot\beta}.
$$

这已经是 exact compact form。

**(w=0) check**

$$
\widehat{\mathcal G}_{12,+\dot\beta}(0)=\frac16(p_1+2p_2)_{+\dot\beta},\qquad
\widehat{\mathcal G}_{21,+\dot\beta}(0)=\frac16(2p_1+p_2)_{+\dot\beta}.
$$

**closed scalar kernel**

$$
u_1:=i w\cdot p_1,\qquad u_2:=i w\cdot p_2.
$$

$$
\widehat{\mathcal K}_{12}(u_1,u_2):=\int_\Delta e^{(x+z)u_1+z u_2}
\frac{u_2+u_1 e^{u_1+u_2}-(u_1+u_2)e^{u_1}}{u_1u_2(u_1+u_2)},
$$

$$
\widehat{\mathcal K}_{21}(u_1,u_2):=\int_\Delta e^{z u_1+(x+z)u_2}
\frac{u_1+u_2 e^{u_1+u_2}-(u_1+u_2)e^{u_2}}{u_1u_2(u_1+u_2)}.
$$

**Lie-algebra indices** $(A,B,\dots)$

$$
[T^A,T^B]=f^{AB}{}_C T^C,\qquad
\operatorname{Tr}(T^A T^B)=\delta^{AB}.
$$

$$
\boxed{\mathcal I\big[Q_1\mathcal O_w^{AB}(p)\big]_{\rm loop}^{(1),\rm loc}}
$$

**local operator rewrite**

$$
\widehat{\mathbb D}_{12,+\dot\beta}(w):=\int_\Delta e^{w\cdot\big((x+z)\nabla_+^{(1)}+z\nabla_+^{(2)}\big)}\Big(y\nabla_{+\dot\beta}^{(1)}+(x+y)\nabla_{+\dot\beta}^{(2)}\Big),
$$

$$
\widehat{\mathbb D}_{21,+\dot\beta}(w):=\int_\Delta e^{w\cdot\big(z\nabla_+^{(1)}+(x+z)\nabla_+^{(2)}\big)}\Big((x+y)\nabla_{+\dot\beta}^{(1)}+y\nabla_{+\dot\beta}^{(2)}\Big).
$$

这就是最紧凑的 generating-function 形式。

# $Q_1（f_{++} e^{w\nabla}\bar\lambda_{\dot\beta}）$（Exactly same with HT)

把第二个 factor 的自由 dotted index 记成 $dotbeta$，并取

$$
w\cdot\nabla_+ := w^{+\dot\alpha}\nabla_{+\dot\alpha},
\qquad
w\cdot p_a := w^{+\dot\alpha}p_{a,+\dot\alpha}.
$$

$$
\mathcal O_{w,\dot\beta}{}^{i}{}_{j}{}^{k}{}_{l}(x)
:= f_{++}{}^{i}{}_{j}(x)\,\Big( e^{\,w\cdot\nabla_+}\bar\lambda_{\dot\beta}\Big){}^{k}{}_{l}(x).
$$

沿用当前页的 $(Q_-)$、propagators、$(V_{Alambdabarlambda}=V_L-V_R)$、PV collapse identity、以及同一个 $(mathscr C_{12},mathscr C_{21})$。

这里只保留 loop-focus：

$$
Q_1\mathcal O_{w,\dot\beta}
\;\underbrace{\big\{ i\nabla_{+\dot\rho}\bar\lambda^{\dot\rho},\; e^{\,w\cdot\nabla_+}\bar\lambda_{\dot\beta}\big\}}_{\text{loop/anomaly}}
+\underbrace{\big\{ f_{++},\; Q_-\!\big(e^{\,w\cdot\nabla_+}\bar\lambda_{\dot\beta}\big)\big\}}_{\text{tree from }[Q_-,\nabla_+] }.
$$

因为

$$
Q_-\bar\lambda_{\dot\beta}=0,
$$

第二项在你关心的 sector 里只给 tree-level commutator pieces，不给 loop anomaly。

## two-field triangle insertion

$$
\mathcal O_{w,\dot\beta}^{(\partial)}{}^{i}{}_{j}{}^{k}{}_{l}
:= i\partial_{+\dot\rho}\bar\lambda^{\dot\rho}{}^{i}{}_{j}\; e^{\,w\cdot\partial_+}\bar\lambda_{\dot\beta}{}^{k}{}_{l}.
$$

动量空间：

$$
\mathcal I\!\left[\mathcal O_{w,\dot\beta}^{(\partial)}(p)\right]
= \int_{r,s}(2\pi)^4\delta^{(4)}(p-r-s)\,(-r_{+\dot\rho})\,e^{i w\cdot s}\,\bar\lambda^{\dot\rho}(r)\bar\lambda_{\dot\beta}(s).
$$

## Pattern 12

routing：

$$
r=q+p_1,\qquad s=p_2-q,\qquad p=p_1+p_2.
$$

PV-loop 直接写成

$$
\Gamma_{12;M}^{\rm PV\text{-}loop}{}^{i}{}_{j}{}^{k}{}_{l}(w)
=2g^2\int_q
 e^{i w\cdot(p_2-q)}
\frac{(q-p_2)_{+\dot\beta}}{(q^2+M^2)\big((q-p_2)^2+M^2\big)}\,\mathscr C_{12}{}^{i}{}_{j}{}^{k}{}_{l}
$$

$$
\qquad
-2g^2M^2\int_q e^{i w\cdot(p_2-q)}
\frac{(q-p_2)_{+\dot\beta}}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}\,\mathscr C_{12}{}^{i}{}_{j}{}^{k}{}_{l}.
$$

regulated splitting 仍写成

$$
\Gamma_{12}^{\rm reg}(w)
=\Big(\Gamma_{12}^{(0)}(w)-\Gamma_{12;M}^{(0)}(w)\Big)+\Gamma_{12;M}^{(\rm anom)}(w),
$$

其中 anomalous sector 取

$$
\Gamma_{12;M}^{(\rm anom)}(w)
=2g^2M^2\int_q
 e^{i w\cdot(p_2-q)}
\frac{(q-p_2)_{+\dot\beta}}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}\,\mathscr C_{12}.
$$

### Feynman parameter

$$
\frac{1}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}
=2\int_\Delta\frac{1}{\big[(q+y p_1-z p_2)^2+M^2+\Delta\big]^3},
$$

$$
\int_\Delta:=\int_0^1 dx\,dy\,dz\;\delta(1-x-y-z),
\qquad
\Delta=xy\,p_1^2+xz\,p_2^2+yz\,p^2.
$$

令

$$
\ell=q+y p_1-z p_2,
\qquad
q-p_2=\ell-Y_{12},
\qquad
Y_{12}:=y\,p_1+(x+y)\,p_2.
$$

则

$$
e^{i w\cdot(p_2-q)}=e^{i w\cdot Y_{12}}\,e^{-i w\cdot\ell}.
$$

所有含 $\ell$ 的 moments 全部消失：

$$
\int_\ell e^{-i w\cdot\ell}\,\ell_{+\dot\alpha_1}\cdots \ell_{+\dot\alpha_n}\,F(\ell^2)=0,\qquad n\ge 1,
$$

因为 tensor reduction 最终必含 $epsilon_{++}=0$。

于是

$$
\Gamma_{12;M}^{(\rm anom)}(w)
=-4g^2M^2\int_\Delta e^{i w\cdot Y_{12}}\,Y_{12,+\dot\beta}
\int_\ell\frac{1}{(\ell^2+M^2+\Delta)^3}\,\mathscr C_{12}.
$$

再用

$$
\int_\ell\frac{1}{(\ell^2+\Omega)^3}=\frac{1}{32\pi^2}\frac{1}{\Omega},
$$

得 local part

$$
\boxed{\Gamma_{12}^{(\rm anom,loc)}{}^{i}{}_{j}{}^{k}{}_{l}(w)
=-\frac{g^2}{8\pi^2}\int_\Delta e^{i w\cdot Y_{12}}\,Y_{12,+\dot\beta}\,\mathscr C_{12}{}^{i}{}_{j}{}^{k}{}_{l}.}
$$

## Pattern 21

完全平行：

$$
Y_{21}:=(x+y)\,p_1+y\,p_2.
$$

$$
\boxed{\Gamma_{21}^{(\rm anom,loc)}{}^{i}{}_{j}{}^{k}{}_{l}(w)
=-\frac{g^2}{8\pi^2}\int_\Delta e^{i w\cdot Y_{21}}\,Y_{21,+\dot\beta}\,\mathscr C_{21}{}^{i}{}_{j}{}^{k}{}_{l}.}
$$

## Open-index final result

定义 exact kernels

$$
\mathcal H_{12,+\dot\beta}(w;p_1,p_2):=\int_\Delta e^{i w\cdot Y_{12}}\,Y_{12,+\dot\beta},
\qquad
\mathcal H_{21,+\dot\beta}(w;p_1,p_2):=\int_\Delta e^{i w\cdot Y_{21}}\,Y_{21,+\dot\beta}.
$$

则

$$
\boxed{\mathcal I\!\left[Q_1\!\Big(f_{++}\,e^{\,w\cdot\nabla_+}\bar\lambda_{\dot\beta}\Big)_{\rm loop}^{(1),\rm loc}{}^{i}{}_{j}{}^{k}{}_{l}(p)\right]
=-\frac{g^2}{8\pi^2}\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)
\Big[\mathcal H_{12,+\dot\beta}\,\mathscr C_{12}{}^{i}{}_{j}{}^{k}{}_{l}+\mathcal H_{21,+\dot\beta}\,\mathscr C_{21}{}^{i}{}_{j}{}^{k}{}_{l}\Big].}
$$

这里 $(\mathscr C_{12},\mathscr C_{21})$ 就是你当前页已经在用的那一对 color-flow tensors。

## exact scalar kernel

记

$$
u_1:= i\,w\cdot p_1,\qquad \nu_2:= i\,w\cdot p_2.
$$

定义

$$
\mathcal K_{12}(\nu_1,\nu_2):=\int_\Delta e^{y\nu_1+(x+y)\nu_2}
\frac{\nu_1+\nu_2 e^{\nu_1+\nu_2}-(\nu_1+\nu_2)e^{\nu_2}}{\nu_1\nu_2(\nu_1+\nu_2)},
$$

$$
\mathcal K_{21}(\nu_1,\nu_2):=\int_\Delta e^{(x+y)\nu_1+y\nu_2}
\frac{\nu_2+\nu_1 e^{\nu_1+\nu_2}-(\nu_1+\nu_2)e^{\nu_1}}{\nu_1\nu_2(\nu_1+\nu_2)}.
$$

则

$$
\mathcal H_{12,+\dot\beta}=\frac{1}{i}\frac{\partial \mathcal K_{12}}{\partial w^{+\dot\beta}},
\qquad
\mathcal H_{21,+\dot\beta}=\frac{1}{i}\frac{\partial \mathcal K_{21}}{\partial w^{+\dot\beta}}.
$$

这就是最紧凑的 generating-function 形式。

## $(w)$-级数

$$
\mathcal H_{12,+\dot\beta}
=\sum_{n\ge 0}\frac{i^n}{n!}\,w^{+\dot\alpha_1}\cdots w^{+\dot\alpha_n}
\int_\Delta Y_{12,+\dot\alpha_1}\cdots Y_{12,+\dot\alpha_n}Y_{12,+\dot\beta},
$$

$$
\mathcal H_{21,+\dot\beta}
=\sum_{n\ge 0}\frac{i^n}{n!}\,w^{+\dot\alpha_1}\cdots w^{+\dot\alpha_n}
\int_\Delta Y_{21,+\dot\alpha_1}\cdots Y_{21,+\dot\alpha_n}Y_{21,+\dot\beta}.
$$

前两阶：

$$
\mathcal H_{12,+\dot\beta}
=\frac16(p_1+2p_2)_{+\dot\beta}+\frac{i}{12}\,w^{+\dot\theta}\,\Xi_{12,+\dot\theta,+\dot\beta}+O(w^2),
$$

$$
\mathcal H_{21,+\dot\beta}
=\frac16(2p_1+p_2)_{+\dot\beta}+\frac{i}{12}\,w^{+\dot\theta}\,\Xi_{21,+\dot\theta,+\dot\beta}+O(w^2),
$$

其中

$$
\Xi_{12,+\dot\theta,+\dot\beta}
=p_{1,+\dot\theta}p_{1,+\dot\beta}+3p_{1,+(\dot\theta}p_{2,+\dot\beta)}+3p_{2,+\dot\theta}p_{2,+\dot\beta},
$$

$$
\Xi_{21,+\dot\theta,+\dot\beta}
=3p_{1,+\dot\theta}p_{1,+\dot\beta}+3p_{1,+(\dot\theta}p_{2,+\dot\beta)}+p_{2,+\dot\theta}p_{2,+\dot\beta}.
$$

因此

$$
\mathcal I\!\left[Q_1\!\Big(f_{++}e^{\,w\cdot\nabla_+}\bar\lambda_{\dot\beta}\Big)_{\rm loop}^{(1),\rm loc}\right]
=-\frac{g^2}{48\pi^2}\Big[(p_1+2p_2)_{+\dot\beta}\,\mathscr C_{12}+(2p_1+p_2)_{+\dot\beta}\,\mathscr C_{21}\Big]
$$

$$
\qquad
-\frac{i g^2}{96\pi^2}\,w^{+\dot\theta}
\Big[\Xi_{12,+\dot\theta,+\dot\beta}\,\mathscr C_{12}+\Xi_{21,+\dot\theta,+\dot\beta}\,\mathscr C_{21}\Big]
+O(w^2).
$$

$(w=0)$ 与 $O(w)$ 分别正好退化到当前页已经算过的 $Q_1(f_{++}barlambda_{dotbeta})$、$Q_1(f_{++}nabla_{+dottheta}barlambda_{dotbeta})$ 结果。

## Lie-algebra rewrite

定义

$$
\mathcal O_{w,\dot\beta}^{AB}(x)
:= f_{++}^A(x)\,\Big(e^{\,w\cdot\nabla_+}\bar\lambda_{\dot\beta}^B\Big)(x),
\qquad
[T^A,T^B]=f^{AB}{}_C\,T^C,
\qquad
\operatorname{Tr}(T^A T^B)=\delta^{AB}.
$$

$$
\mathscr C_{12}^{AB}(p_1,p_2)
=\epsilon^{\dot\gamma\dot\delta}\,f^{CA}{}_E f^{DB}{}_E\,\bar\lambda_{\dot\gamma}^C(p_1)\bar\lambda_{\dot\delta}^D(p_2),
\qquad
\mathscr C_{21}^{AB}(p_1,p_2)=\mathscr C_{12}^{AB}(p_2,p_1).
$$

于是

$$
\boxed{\mathcal I\!\left[Q_1\mathcal O_{w,\dot\beta}^{AB}(p)\right]_{\rm loop}^{(1),\rm loc}
=-\frac{g^2}{8\pi^2}\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)
\Big[\mathcal H_{12,+\dot\beta}\,\mathscr C_{12}^{AB}+\mathcal H_{21,+\dot\beta}\,\mathscr C_{21}^{AB}\Big].}
$$

再把第二项重命名 $(p_1leftrightarrow p_2)$，并用 $mathcal H_{21}(w;p_2,p_1)=mathcal H_{12}(w;p_1,p_2)$，得到更紧凑的形式

$$
\boxed{\mathcal I\!\left[Q_1\mathcal O_{w,\dot\beta}^{AB}(p)\right]_{\rm loop}^{(1),\rm loc}
=-\frac{g^2}{4\pi^2}\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)\,\mathcal H_{12,+\dot\beta}(w;p_1,p_2)\,\mathscr C_{12}^{AB}(p_1,p_2).}
$$

## local operator rewrite

定义 bilocal two-slot differential operator

$$
\nabla_{+\dot\beta}^{(1)}\big(X(x_1)Y(x_2)\big):=(\nabla_{+\dot\beta}X)(x_1)\,Y(x_2),
\qquad
\nabla_{+\dot\beta}^{(2)}\big(X(x_1)Y(x_2)\big):=X(x_1)\,(\nabla_{+\dot\beta}Y)(x_2).
$$

再定义

$$
\mathbb H_{+\dot\beta}(w)
:=\int_\Delta
 e^{\,w\cdot\big(y\nabla_+^{(1)}+(x+y)\nabla_+^{(2)}\big)}
\Big(y\nabla_{+\dot\beta}^{(1)}+(x+y)\nabla_{+\dot\beta}^{(2)}\Big).
$$

则 exact local form 可写成

$$
\boxed{Q_1\mathcal O_{w,\dot\beta}^{AB}(x)\Big\|_{\rm loop}^{(1),\rm loc}
=\frac{i g^2}{4\pi^2}\,\mathbb H_{+\dot\beta}(w)\,
\Big[\epsilon^{\dot\gamma\dot\delta}\,f^{CA}{}_E f^{DB}{}_E\,\bar\lambda_{\dot\gamma}^C(x_1)\bar\lambda_{\dot\delta}^D(x_2)\Big]_{x_1=x_2=x}.}
$$

这就是 compact generating-function local operator.