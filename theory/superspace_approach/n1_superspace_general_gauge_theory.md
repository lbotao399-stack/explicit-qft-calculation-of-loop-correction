---
title: "N=1 superspace general gauge theory"
doc_type: theory
approach: "Superspace"
theory: "N=1 superspace general gauge theory"
status: canonical
source: user_supplied_book_excerpt_ch3_ch4
---

# N=1 superspace general gauge theory

## 1. (N=1) superspace notation / algebra / D-algebra

### 1.1 Spinor / vector conventions

$$
V^{\underline a}\equiv V^{\alpha\dot\alpha},
\qquad
V^{\underline a}=(V^{+\dot +},V^{+\dot -},V^{-\dot +},V^{-\dot -})
\equiv (V^+,V_T,\bar V_T,-V^-). \tag{3.1.1}
$$

$$
V^{\alpha\dot\alpha}=\frac1{\sqrt2}\sigma^{\tilde b,\alpha\dot\alpha}V_{\tilde b},
\qquad
V_{\tilde b}=\frac1{\sqrt2}\sigma_{\tilde b}^{\alpha\dot\alpha}V_{\alpha\dot\alpha}, \tag{3.1.2a}
$$

$$
\partial_{\alpha\dot\alpha}=\sigma_{\tilde b,\alpha\dot\alpha}\partial^{\tilde b},
\qquad
\partial^{\tilde b}=\frac12\sigma^{\tilde b,\alpha\dot\alpha}\partial_{\alpha\dot\alpha},
$$

$$
x^{\alpha\dot\alpha}=\frac12\sigma^{\tilde b,\alpha\dot\alpha}x_{\tilde b},
\qquad
x_{\tilde b}=\sigma_{\tilde b}^{\alpha\dot\alpha}x_{\alpha\dot\alpha}.
$$

$$
\sigma^{\tilde b}{}_{\alpha\dot\alpha}\sigma_{\tilde c}^{\alpha\dot\alpha}=2\delta^{\tilde b}{}_{\tilde c},
\qquad
\sigma^{\tilde b}{}_{\alpha\dot\alpha}\sigma_{\tilde b}^{\beta\dot\beta}
=2\delta_\alpha{}^\beta\delta_{\dot\alpha}{}^{\dot\beta}. \tag{3.1.2b}
$$

### 1.2 Superspace coordinates / graded calculus

$$
z^A=(x^{\underline a},\theta^{\underline\alpha},\bar\theta^{\underline{\dot\alpha}}), \tag{3.1.3a}
$$

$$
\partial_A=(\partial_{\underline a},\partial_{\underline\alpha},\bar\partial_{\underline{\dot\alpha}}),
\qquad
\partial_A z^B\equiv \delta_A{}^B. \tag{3.1.3b}
$$

$$
(\partial_A XY)\equiv [\partial_A,XY}
=[\partial_A,X}Y+(-)^{XA}X[\partial_A,Y}. \tag{3.1.4a}
$$

$$
[A,B}\equiv AB-(-)^{AB}BA,
\qquad
[\partial_A,\partial_B}=0. \tag{3.1.4b}
$$

### 1.3 \(C_{\alpha\beta}\), raising/lowering, contractions

$$
\bar C_{\alpha\beta}=C_{\dot\beta\dot\alpha},
\qquad
C^{\alpha\beta}C_{\gamma\delta}
=\delta^\alpha{}_{[\gamma}\delta^\beta{}_{\delta]}. \tag{3.1.10a}
$$

$$
C_{\alpha\beta}
=
\begin{pmatrix}
0&-i\\
i&0
\end{pmatrix}
=\sigma_2. \tag{3.1.15}
$$

$$
\psi_\alpha=\psi^\beta C_{\beta\alpha},
\qquad
\psi^\alpha=C^{\alpha\beta}\psi_\beta, \tag{3.1.16a}
$$

$$
\bar\psi_{\dot\alpha}=\bar\psi^{\dot\beta}C_{\dot\beta\dot\alpha},
\qquad
\bar\psi^{\dot\alpha}=C^{\dot\alpha\dot\beta}\bar\psi_{\dot\beta}. \tag{3.1.16c}
$$

$$
\psi\cdot\chi\equiv \psi^\alpha\chi_\alpha=\chi\cdot\psi,
\qquad
\psi^2\equiv \frac12 C_{\beta\alpha}\psi^\alpha\psi^\beta
=\frac12\psi^\alpha\psi_\alpha=i\psi^+\psi^-, \tag{3.1.16b}
$$

$$
\bar\psi\cdot\bar\chi\equiv \bar\psi^{\dot\alpha}\bar\chi_{\dot\alpha}=\bar\chi\cdot\bar\psi,
\qquad
\bar\psi^2
=\frac12 C_{\dot\beta\dot\alpha}\bar\psi^{\dot\alpha}\bar\psi^{\dot\beta}
=\frac12\bar\psi^{\dot\alpha}\bar\psi_{\dot\alpha}
=i\bar\psi^{\dot +}\bar\psi^{\dot -}. \tag{3.1.16d}
$$

$$
V_{\underline a}
=
V^{\underline b}C_{\beta\alpha}C_{\dot\beta\dot\alpha}
\equiv V^{\underline b}\eta_{\underline{ba}},
\qquad
V^{\underline a}
=
C^{\alpha\beta}C^{\dot\alpha\dot\beta}V_{\underline b}
\equiv \eta^{\underline{ab}}V_{\underline b}. \tag{3.1.16e}
$$

$$
V^2\equiv \frac12\eta_{\underline{ba}}V^{\underline a}V^{\underline b}
=\frac12V^{\underline a}V_{\underline a}
=V^+V^-+V_T\bar V_T
=-\det V^{\alpha\dot\beta}. \tag{3.1.16f}
$$

$$
\Box\equiv \frac12\partial^{\underline a}\partial_{\underline a}.
$$

$$
\partial^{\alpha\dot\gamma}\partial_{\beta\dot\gamma}
=\delta_\beta{}^\alpha\,\Box. \tag{3.1.18}
$$

$$
\psi_{[\alpha}\chi_{\beta]}
=
C_{\beta\alpha}(C^{\delta\gamma}\psi_\gamma\chi_\delta)
=
C_{\beta\alpha}(\psi^\delta\chi_\delta). \tag{3.1.19}
$$

$$
(\psi_\alpha)^\dagger=-\bar\psi_{\dot\alpha}. \tag{3.1.20}
$$

### 1.4 Super-Poincaré algebra / superconformal algebra

#### Super-Poincaré

$$
\{Q^a_\alpha,\bar Q^b_{\dot\beta}\}=\delta^b_a P_{\alpha\dot\beta}, \tag{3.2.8a}
$$

$$
\{Q_a{}_\alpha,Q_b{}_\beta\}=C_{\alpha\beta}Z^{ab}, \tag{3.2.8b}
$$

$$
[Q_a{}_\alpha,P_{\beta\dot\beta}]
=
[P_{\alpha\dot\alpha},P_{\beta\dot\beta}]
=
[J_{\dot\alpha\dot\beta},Q_c{}_\gamma]
=0, \tag{3.2.8c}
$$

$$
[J_{\alpha\beta},Q_c{}_\gamma]
=
\frac12 i\,C_{\gamma(\alpha}Q_c{}_{\beta)}, \tag{3.2.8d}
$$

$$
[J_{\alpha\beta},P_{\gamma\dot\gamma}]
=
\frac12 i\,C_{\gamma(\alpha}P_{\beta)\dot\gamma}, \tag{3.2.8e}
$$

$$
[J_{\alpha\beta},J^{\gamma\delta}]
=
-\frac12 i\,\delta^{(\gamma}{}_{(\alpha}J^{\delta)}{}_{\beta)}, \tag{3.2.8f}
$$

$$
[J_{\alpha\beta},\bar J_{\dot\alpha\dot\beta}]
=
[Z_{ab},Z_{cd}]
=
[Z_{ab},\bar Z^{cd}]
=0. \tag{3.2.8g}
$$

$$
\{Q_\alpha,\bar Q_{\dot\beta}\}=P_{\alpha\dot\beta},
\qquad
\{Q_\alpha,Q_\beta\}=0.
$$

#### Superconformal

$$
\{Q_a{}_\alpha,\bar Q^b{}_{\dot\beta}\}
=
\delta^a_b P_{\alpha\dot\beta},
\qquad
\{S^a{}^\alpha,\bar S_b{}^{\dot\beta}\}
=
\delta^a_b K^{\alpha\dot\beta}. \tag{3.2.12a}
$$

$$
\{Q_a{}_\alpha,S^b{}^\beta\}
=
-i\delta_a{}^b\Big(J_\alpha{}^\beta+\frac12\delta_\alpha{}^\beta\Delta\Big)
-\frac12\delta_\alpha^\beta\delta_a^b\Big(1-\frac4N\Big)A
+2\delta_\alpha{}^\beta T_a{}^b. \tag{3.2.12b}
$$

$$
[A,S^c{}^\gamma]=\frac12 S^c{}^\gamma,
\qquad
[\Delta,S^c{}^\gamma]=-\frac{i}{2}S^c{}^\gamma, \tag{3.2.12d}
$$

$$
[A,Q_c{}_\gamma]=-\frac12 Q_c{}_\gamma,
\qquad
[\Delta,Q_c{}_\gamma]=\frac{i}{2}Q_c{}_\gamma, \tag{3.2.12g}
$$

$$
[J_\alpha{}^\beta,Q_c{}_\gamma]
=
\frac12 i\,\delta_\gamma^{(\beta}Q_c{}_{\alpha)},
\qquad
[K^{\alpha\dot\alpha},Q_c{}_\gamma]
=
\delta_\gamma^\alpha \bar S_c{}^{\dot\alpha}, \tag{3.2.12h}
$$

$$
[\Delta,K^{\alpha\dot\alpha}]=-iK^{\alpha\dot\alpha},
\qquad
[\Delta,P_{\alpha\dot\alpha}]=iP_{\alpha\dot\alpha}, \tag{3.2.12j}
$$

$$
[J_\alpha{}^\beta,K^{\gamma\dot\gamma}]
=
-\frac12 i\,\delta_{(\alpha}^{|\gamma|}K^{\beta)\dot\gamma},
\qquad
[J_\alpha{}^\beta,P_{\gamma\dot\gamma}]
=
\frac12 i\,\delta_\gamma^{(\beta}P_{\alpha)\dot\gamma}, \tag{3.2.12k}
$$

$$
[P_{\alpha\dot\alpha},K^{\beta\dot\beta}]
=
i\Big(
\delta_{\dot\alpha}^{\dot\beta}J_\alpha{}^\beta
+\delta_\alpha^\beta J_{\dot\alpha}{}^{\dot\beta}
+\delta_\alpha^\beta\delta_{\dot\alpha}^{\dot\beta}\Delta
\Big). \tag{3.2.12m}
$$

### 1.5 Covariant derivatives \(D\)

$$
D_\alpha=-iQ_\alpha+\bar\theta^{\dot\alpha}P_{\alpha\dot\alpha},
\qquad
\bar D_{\dot\alpha}=-i\bar Q_{\dot\alpha}+\theta^\alpha P_{\alpha\dot\alpha}. \tag{3.4.4}
$$

$$
D_\alpha=\partial_\alpha+\frac12\bar\theta^{\dot\alpha}i\partial_{\alpha\dot\alpha},
\qquad
\bar D_{\dot\alpha}=\bar\partial_{\dot\alpha}+\frac12\theta^\alpha i\partial_{\alpha\dot\alpha}. \tag{3.4.5}
$$

$$
\{Q,D\}=\{\bar Q,\bar D\}=[P,D]=0. \tag{3.4.3}
$$

$$
\{D_\alpha,D_\beta\}=0,
\qquad
\{D_\alpha,\bar D_{\dot\beta}\}=i\partial_{\alpha\dot\beta}. \tag{3.4.9}
$$

$$
[D^\alpha,\bar D^2]=i\partial^{\alpha\dot\alpha}\bar D_{\dot\alpha},
\qquad
\bar D^2 D^2 D^2=\Box D^2,
\qquad
D^\alpha D_\beta=\delta_\beta{}^\alpha D^2,
\qquad
D^2\theta^2=-1. \tag{3.4.10}
$$

$$
[D_A,D_B}
=
T_{AB}{}^C D_C + R_{AB}^{(M)} + F_{AB}^{(T)} + F_{AB}^{(Z)}, \tag{3.4.18}
$$

$$
T_{\alpha\dot\beta}{}^c
=
i\delta_a{}^b\delta_\alpha{}^\gamma\delta_{\dot\beta}{}^{\dot\gamma}. \tag{3.4.19}
$$

## 2. Chiral multiplet / vector multiplet / \(W_\alpha\)

### 2.1 Chiral multiplet

$$
\Phi^{(+)}=A+\theta^\alpha\psi_\alpha-\theta^2 F. \tag{4.1\ \text{text};\ 3.6.2\ \text{context}}
$$

$$
\Phi
=
e^{\frac12 U}(A+\theta^\alpha\psi_\alpha-\theta^2 F)e^{-\frac12 U}
$$

$$
=
A+\theta^\alpha\psi_\alpha-\theta^2 F
+i\frac12\theta^\alpha\bar\theta^{\dot\alpha}\partial_a A
+i\frac12\theta^2\bar\theta^{\dot\alpha}\partial_a\psi^\alpha
+\frac14\theta^2\bar\theta^2\Box A. \tag{3.6.2}
$$

$$
A=\Phi|, \tag{3.6.7a}
$$

$$
\psi_\alpha=D_\alpha\Phi|, \tag{3.6.7b}
$$

$$
F=D^2\Phi|. \tag{3.6.7c}
$$

$$
\delta A=-\epsilon^\alpha\psi_\alpha, \tag{3.6.6a}
$$

$$
\delta\psi_\alpha
=
-\bar\epsilon^{\dot\alpha}i\partial_{\alpha\dot\alpha}A
+\epsilon_\alpha F, \tag{3.6.6b}
$$

$$
\delta F
=
\bar\epsilon^{\dot\alpha}i\partial_{\alpha\dot\alpha}\psi^\alpha. \tag{3.6.6c}
$$

$$
S
=
\int d^4x\,d^4\theta\,\bar\Phi_i\Phi^i
+
\int d^4x\,d^2\theta\,P(\Phi^i)
+h.c. \tag{4.1.11}
$$

$$
P_i=\frac{\partial P}{\partial A^i},
\qquad
P_{ij}=\frac{\partial^2P}{\partial A^i\partial A^j}. \tag{4.1.13}
$$

### 2.2 Vector multiplet

$$
V
=
C+\theta^\alpha\chi_\alpha+\bar\theta^{\dot\alpha}\bar\chi_{\dot\alpha}
-\theta^2 M-\bar\theta^2\bar M
+\theta^\alpha\bar\theta^{\dot\alpha}A_a
-\bar\theta^2\theta^\alpha\lambda_\alpha
-\theta^2\bar\theta^{\dot\alpha}\bar\lambda_{\dot\alpha}
+\theta^2\bar\theta^2 D. \tag{3.6.1}
$$

$$
C=V|,
\qquad
\chi_\alpha=iD_\alpha V|,
\qquad
\bar\chi_{\dot\alpha}=-i\bar D_{\dot\alpha}V|,
$$

$$
M=D^2V|,
\qquad
\bar M=\bar D^2V|,
\qquad
A_{\alpha\dot\alpha}=\frac12[\bar D_{\dot\alpha},D_\alpha]V|,
$$

$$
\lambda_\alpha=i\bar D^2 D_\alpha V|,
\qquad
\bar\lambda_{\dot\alpha}=-iD^2\bar D_{\dot\alpha}V|,
\qquad
D'=\frac12 D^\alpha\bar D^2 D_\alpha V|. \tag{4.2.4a}
$$

$$
V'=V+i(\bar\Lambda-\Lambda),
\qquad
\bar D_{\dot\alpha}\Lambda=0,
\qquad
D_\alpha\bar\Lambda=0. \tag{4.2.3}
$$

$$
\delta C=i(\bar\Lambda_1-\Lambda_1),
\qquad
\delta\chi_\alpha=\Lambda_\alpha,
\qquad
\delta M=-i\Lambda_2,
$$

$$
\delta A_{\alpha\dot\alpha}
=
\frac12\partial_{\alpha\dot\alpha}(\Lambda_1+\bar\Lambda_1),
\qquad
\delta\lambda_\alpha=0,
\qquad
\delta D'=0. \tag{4.2.5}
$$

### 2.3 \(W_\alpha\) in vector superspace / chiral superspace

#### Abelian / vector-prepotential form

$$
W_\alpha=i\bar D^2 D_\alpha V,
\qquad
\bar W_{\dot\alpha}=-iD^2\bar D_{\dot\alpha}V,
\qquad
V=\bar V. \tag{4.2.2}
$$

$$
\bar D^{\dot\alpha}W_\alpha=0,
\qquad
D^\alpha W_\alpha=-\bar D^{\dot\alpha}\bar W_{\dot\alpha}. \tag{4.2.1}
$$

$$
\lambda_\alpha=W_\alpha|,
$$

$$
f_{\alpha\beta}=\frac12 D_{(\alpha}W_{\beta)}|,
\qquad
D'=-\frac12 i D^\alpha W_\alpha|,
$$

$$
i\bar\partial_{\dot\alpha}{}^{\dot\beta}\bar\lambda_{\dot\beta}
=
D^2 W_\alpha|. \tag{4.2.6}
$$

#### Nonabelian / gauge-chiral representation

$$
\Phi'=e^{i\Lambda}\Phi,
\qquad
\bar D_{\dot\alpha}\Lambda=0, \tag{4.2.17}
$$

$$
\bar\Phi'=\bar\Phi e^{-i\bar\Lambda},
\qquad
D_\alpha\bar\Lambda=0. \tag{4.2.18}
$$

$$
e^{V'}=e^{i\bar\Lambda}e^V e^{-i\Lambda}. \tag{4.2.19}
$$

$$
\nabla_A=D_A-i\Gamma_A=(\nabla_\alpha,\bar\nabla_{\dot\alpha},\nabla_{\alpha\dot\alpha}), \tag{4.2.30}
$$

$$
\nabla'_A=e^{i\Lambda}\nabla_A e^{-i\Lambda}, \tag{4.2.32a}
$$

$$
\nabla_{\dot\alpha}\equiv \bar D_{\dot\alpha}, \tag{4.2.33}
$$

$$
\nabla_\alpha=e^{-V}D_\alpha e^V, \tag{4.2.34}
$$

$$
\nabla_{\alpha\dot\alpha}\equiv -i\{\nabla_\alpha,\bar\nabla_{\dot\alpha}\},
$$

$$
\nabla_A=(e^{-V}D_\alpha e^V,\bar D_{\dot\alpha},-i\{\nabla_\alpha,\bar\nabla_{\dot\alpha}\}). \tag{4.2.35}
$$

$$
[\nabla_A,\nabla_B]
=
T_{AB}{}^C\nabla_C-iF_{AB}. \tag{4.2.43}
$$

$$
F_{\alpha\beta}=F_{\dot\alpha\dot\beta}=F_{\alpha\dot\beta}=0. \tag{4.2.44}
$$

$$
W_\alpha\equiv i\bar D^2(e^{-V}D_\alpha e^V), \tag{4.2.45}
$$

$$
W_{\dot\alpha}\equiv e^{-V}\bar W_{\dot\alpha}e^V
\equiv e^{-V}(-W_\alpha)^\dagger e^V. \tag{4.2.45}
$$

$$
\nabla^\alpha W_\alpha=-\bar\nabla^{\dot\alpha}W_{\dot\alpha}. \tag{4.2.46}
$$

#### Covariant approach / prepotential \(\Omega\)

$$
F_{\alpha\dot\alpha}=0, \tag{4.2.60}
$$

$$
F_{\alpha\beta}=\bar F_{\dot\alpha\dot\beta}=0, \tag{4.2.66}
$$

$$
\{\nabla_\alpha,\nabla_\beta\}=0. \tag{4.2.67}
$$

$$
\nabla_\alpha=e^{-\Omega}D_\alpha e^\Omega, \tag{4.2.68}
$$

$$
\bar\nabla_{\dot\alpha}=e^{\bar\Omega}\bar D_{\dot\alpha}e^{-\bar\Omega}, \tag{4.2.69}
$$

$$
e^V=e^\Omega e^{\bar\Omega}, \tag{4.2.72}
$$

$$
(e^V)'=e^{i\bar\Lambda}e^V e^{-i\Lambda}. \tag{4.2.74}
$$

$$
\bar\nabla_{\dot\alpha}\Phi=0,
\qquad
\Phi'=e^{iK}\Phi, \tag{4.2.64}
$$

$$
\Phi=e^{\bar\Omega}\Phi_0,
\qquad
\bar D_{\dot\alpha}\Phi_0=0. \tag{4.2.75}
$$

### 2.4 Jacobi / Bianchi solved form

$$
[\nabla_{[A}[\nabla_B,\nabla_{C\}}]]=0. \tag{4.2.79a}
$$

$$
\nabla_{[A}F_{BC)}-T_{[AB|}{}^D F_{D|C)}=0. \tag{4.2.79b}
$$

$$
F_{\alpha,\beta\dot\beta}
=
-iC_{\beta\alpha}\bar W_{\dot\beta}, \tag{4.2.81}
$$

$$
\nabla_\alpha\bar W_{\dot\beta}=0, \tag{4.2.83}
$$

$$
F_{\alpha\dot\alpha,\beta\dot\beta}
=
\frac12\Big(
C_{\alpha\beta}\bar\nabla_{(\dot\alpha}\bar W_{\dot\beta)}
+
C_{\dot\alpha\dot\beta}\nabla_{(\alpha}W_{\beta)}
\Big)
\equiv
C_{\alpha\beta}\bar f_{\dot\alpha\dot\beta}
+
C_{\dot\alpha\dot\beta}f_{\alpha\beta}, \tag{4.2.85}
$$

$$
\nabla^\alpha W_\alpha+\bar\nabla^{\dot\alpha}\bar W_{\dot\alpha}=0, \tag{4.2.86}
$$

$$
\nabla_\alpha W_\beta
=
iC_{\beta\alpha}D'+f_{\alpha\beta},
\qquad
D'=\bar D'=-\frac{i}{2}\nabla^\alpha W_\alpha. \tag{4.2.87}
$$

$$
\{\nabla_\alpha,\nabla_\beta\}=0,
$$

$$
\{\nabla_\alpha,\bar\nabla_{\dot\beta}\}=i\nabla_{\alpha\dot\beta},
$$

$$
[\bar\nabla_{\dot\alpha},i\nabla_{\beta\dot\beta}]
=
-iC_{\dot\beta\dot\alpha}W_\beta,
$$

$$
[i\nabla_{\underline a},i\nabla_{\underline b}]
=
i\big(
C_{\dot\alpha\dot\beta}f_{\alpha\beta}
+
C_{\alpha\beta}\bar f_{\dot\alpha\dot\beta}
\big). \tag{4.2.90}
$$

## 3. General \(N=1\) gauge theory with superpotential

### 3.1 Superspace action

$$
S
=
\int d^4x\,d^4\theta\,
\overline{\Phi}_j (e^V)^j{}_i \Phi^i
+
\operatorname{tr}\int d^4x\,d^2\theta\,W^2
+
\left[
\int d^4x\,d^2\theta\,P(\Phi^i)+h.c.
\right]. \tag{4.3.1}
$$

$$
V^i{}_j=V^A(T_A)^i{}_j.
$$

$$
S
=
\int d^4x\,d^4\theta\,\overline{\Phi}_i\Phi^i
+
\operatorname{tr}\int d^4x\,d^2\theta\,W^2
+
\left[
\int d^4x\,d^2\theta\,P(\Phi^i)+h.c.
\right]. \tag{4.3.2}
$$

$$
S_{FI}
=
\operatorname{tr}\int d^4x\,d^4\theta\,\nu V
=
\operatorname{tr}\int d^4x\,\nu D'. \tag{4.3.3}
$$

### 3.2 Covariant component definitions

$$
A=\Phi|,\qquad
\psi_\alpha=\nabla_\alpha\Phi|,\qquad
F=\nabla^2\Phi|. \tag{4.3.4}
$$

$$
\lambda_\alpha=W_\alpha|, \qquad
f_{\alpha\beta}=\frac12\{\nabla_{(\alpha},W_{\beta)}\}| ,
$$

$$
i\nabla_\alpha{}^{\dot\alpha}\bar\lambda_{\dot\alpha}
=
\frac12[\nabla^\beta,\{\nabla_\beta,W_\alpha\}]| ,
\qquad
D'=-\frac{i}{2}\{\nabla^\alpha,W_\alpha\}|. \tag{4.3.5}
$$

### 3.3 Component action

$$
S
=
\int d^4 x \,
\Big[
A^i \square \overline{A}_i
+
\Psi^{\alpha i} i\nabla_{\alpha}{}^{\dot{\alpha}} \overline{\Psi}_{\dot{\alpha}i}
+
i\overline{A}_i (\lambda^{\alpha})^i{}_{j} \Psi_{\alpha}^j
-
i\overline{\Psi}^{\dot{\alpha}}{}_{i}(\overline{\lambda}_{\dot{\alpha}})^i{}_j A^j
\Big.
$$

$$
\Big.
+
\overline{A}_i (D')^i{}_{j} A^j
+
F^i \overline{F}_i
+
\operatorname{tr}\Big(
\lambda^{\alpha} [i\nabla_{\alpha}{}^{\dot{\alpha}}, \bar{\lambda}_{\dot{\alpha}}]
-
\frac{1}{2} f^{\alpha\beta} f_{\alpha\beta}
+
D'^2
\Big)
$$

$$
\Big.
+
\operatorname{tr}\,\nu D'
+
\Big(
P_i F^i
+
\frac{1}{2} P_{ij}\Psi^{\alpha i}\Psi_{\alpha}^j
+
h.c.
\Big)
\Big]. \tag{4.3.6}
$$

$$
\square\equiv \frac12 \nabla^{\underline a}\nabla_{\underline a},
\qquad
P_i=\frac{\partial P}{\partial A^i},
\qquad
P_{ij}=\frac{\partial^2 P}{\partial A^i\partial A^j}. \tag{4.1.13,\ 4.3.6}
$$

$$
-U_F(A^i)=-\sum_i |P_i|^2. \tag{4.1.14}
$$

$$
-U_{D'}
=
-\frac14
\left[
\overline{A}_i (T_A)^i{}_j A^j + \nu\,\operatorname{tr} T_A
\right]^2. \tag{4.3.7}
$$

## 4. Summary

$$
\boxed{
\text{notation from 3.1, 3.2, 3.4;}
\quad
\text{multiplets and }W_\alpha\text{ from 3.6, 4.2;}
\quad
\text{general }N=1\text{ gauge theory with }P(\Phi)\text{ from 4.1, 4.3.}
}
$$
