---
title: "N=4 SYM: BPS letters and Feynman rules"
doc_type: theory
theory: "N=4 SYM"
status: canonical
---

# N=4 SYM: BPS letters and Feynman rules

这份文档固定 `Q\equiv Q_-^4`，并整理 `N=4 SYM` 下与 loop 计算直接相关的 BPS letters、raw action 与 Feynman rules。

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
