---
title: "N=1 superspace BRST and supergraph rules"
doc_type: theory
approach: "Superspace"
theory: "N=1 superspace general gauge theory"
status: canonical
source: user_supplied_book_excerpt_ch4_ch6
---

# N=1 superspace BRST and supergraph rules

## 0. Superspace gauge-covariant derivative \(\nabla\) algebra

$$
\nabla_A=(\nabla_\alpha,\bar\nabla_{\dot\alpha},\nabla_{\alpha\dot\alpha})
=
\bigl(e^{-V}D_\alpha e^V,\ \bar D_{\dot\alpha},\ -i\{\nabla_\alpha,\bar\nabla_{\dot\alpha}\}\bigr). \tag{4.2.35}
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
W_\alpha \equiv i\bar D^2(e^{-V}D_\alpha e^V),
\qquad
W_{\dot\alpha}\equiv e^{-V}\bar W_{\dot\alpha}e^V. \tag{4.2.45}
$$

$$
\nabla^\alpha W_\alpha=-\bar\nabla^{\dot\alpha}W_{\dot\alpha}. \tag{4.2.46}
$$

$$
F_{\alpha,\beta\dot\beta}
=
-iC_{\beta\alpha}\bar W_{\dot\beta}, \tag{4.2.81}
$$

$$
\nabla_\alpha \bar W_{\dot\beta}=0, \tag{4.2.83}
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
C_{\dot\alpha\dot\beta}f_{\alpha\beta}. \tag{4.2.85}
$$

$$
\nabla^\alpha W_\alpha+\bar\nabla^{\dot\alpha}\bar W_{\dot\alpha}=0, \tag{4.2.86}
$$

$$
\nabla_\alpha W_\beta
=
iC_{\beta\alpha}D'
+
f_{\alpha\beta},
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
[\bar\nabla_{\dot\alpha},\,i\nabla_{\beta\dot\beta}]
=
-iC_{\dot\beta\dot\alpha}W_\beta,
$$

$$
[i\nabla_{\underline a},\,i\nabla_{\underline b}]
=
i\bigl(
C_{\dot\alpha\dot\beta}f_{\alpha\beta}
+
C_{\alpha\beta}\bar f_{\dot\alpha\dot\beta}
\bigr). \tag{4.2.90}
$$

## 1. Superspace BRST quantization

### 1.1 Starting point

$$
Z=\int \mathcal D V\, e^{S_{\rm inv}(V)}. \tag{6.2.11}
$$

$$
S_{\rm inv}
=
-\frac{1}{2g^2}\,\operatorname{tr}\int d^4x\,d^4\theta\,
(e^{-V}D^\alpha e^V)\bar D^2(e^{-V}D_\alpha e^V). \tag{6.2.12}
$$

$$
e^{V'}=e^{i\bar\Lambda}e^V e^{-i\Lambda}, \tag{6.2.13a}
$$

$$
\delta V
=
L_{\frac12 V}
\Bigl[
-i(\Lambda+\bar\Lambda)
+
\coth L_{\frac12 V}\, i(\Lambda-\bar\Lambda)
\Bigr],
\qquad
L_XY=[X,Y]. \tag{6.2.13b}
$$

### 1.2 Gauge-fixing

$$
F=\bar D^2 V,
\qquad
\bar F=D^2 V.
$$

$$
\Delta(V)
=
\int \mathcal D\Lambda\,\mathcal D\bar\Lambda\,
\delta[F(V,\Lambda,\bar\Lambda)-f]\,
\delta[\bar F(V,\Lambda,\bar\Lambda)-\bar f]. \tag{6.2.14}
$$

$$
Z
=
\int \mathcal D V\,
\Delta^{-1}(V)\,
\delta[\bar D^2V-f]\,
\delta[D^2V-\bar f]\,
e^{S_{\rm inv}}. \tag{6.2.15}
$$

$$
\int \mathcal Df\,\mathcal D\bar f\,
\exp\Bigl(
-\frac{1}{g^2\alpha}\,\operatorname{tr}\int d^4x\,d^4\theta\,\bar f f
\Bigr),
$$

$$
Z
=
\int \mathcal D V\,
\Delta^{-1}(V)\,
e^{S_{\rm inv}+S_{GF}}, \tag{6.2.16}
$$

$$
S_{GF}
=
-\frac{1}{\alpha g^2}\,
\operatorname{tr}\int d^4x\,d^4\theta\,
(\bar D^2V)(D^2V). \tag{6.2.17}
$$

### 1.3 Faddeev-Popov ghost superfields

$$
\Delta(V)
=
\int \mathcal D\Lambda\,\mathcal D\bar\Lambda\,
\mathcal D\Lambda'\,\mathcal D\bar\Lambda'\,
e^{\int d^4x\,d^2\theta\,
\bar\Lambda'
\left[
\frac{\delta F}{\delta\Lambda}\Lambda
+
\frac{\delta F}{\delta\bar\Lambda}\bar\Lambda
\right]
+
\int d^4x\,d^2\bar\theta\,
\Lambda'
\left[
\frac{\delta \bar F}{\delta\Lambda}\Lambda
+
\frac{\delta \bar F}{\delta\bar\Lambda}\bar\Lambda
\right]
}. \tag{6.2.18}
$$

$$
Z
=
\int \mathcal D V\,
\mathcal D c\,\mathcal D\bar c\,\mathcal D b\,\mathcal D\bar b\,
e^{S_{\rm inv}+S_{GF}+S_{FP}}. \tag{6.2.19}
$$

$$
S_{FP}
=
i\,\operatorname{tr}\int d^4x\,d^2\theta\, b\,\bar D^2(\delta V)
+
i\,\operatorname{tr}\int d^4x\,d^2\bar\theta\, \bar b\,D^2(\delta V)
$$

$$
=
\operatorname{tr}\int d^4x\,d^4\theta\,
(b+\bar b)\,
L_{\frac12 V}
\Bigl[
(c+\bar c)+\coth L_{\frac12 V}(c-\bar c)
\Bigr]. \tag{6.2.20}
$$

### 1.4 \(\alpha=1\) gauge

$$
V_0=\Pi_0V
=
-\Box^{-1}(D^2\bar D^2+\bar D^2D^2)V,
$$

$$
-\frac12 V(\Pi_{\frac12}+\alpha^{-1}\Pi_0)V
=
-\frac12 V\bigl[1+(\alpha^{-1}-1)\Pi_0\bigr]V. \tag{6.2.21}
$$

$$
\alpha=1.
$$

$$
S_{FP}^{(2)}
=
\operatorname{tr}\int d^4x\,d^4\theta\,
(b+\bar b)(c-\bar c)
=
\operatorname{tr}\int d^4x\,d^4\theta\,
(\bar b c-b\bar c). \tag{6.2.22}
$$

### 1.5 BRST transformations

$$
\delta V
=
\xi\,L_V
\Bigl[
(c+\bar c)
+
\coth L_{\frac12 V}(c-\bar c)
\Bigr],
$$

$$
\delta b
=
\frac{1}{\alpha}\xi\,\bar D^2D^2V,
\qquad
\delta \bar b
=
\frac{1}{\alpha}\xi\,D^2\bar D^2V,
$$

$$
\delta c=-\xi c^2,
\qquad
\delta\bar c=-\xi \bar c^2. \tag{6.2.23}
$$

## 2. Supergraph / Feynman rules

### 2.1 General rules

$$
\frac{\delta j(x,\theta)}{\delta j(x',\theta')}
=
\bar D^2 \delta^4(\theta-\theta')\delta^4(x-x'),
$$

$$
\int \frac{d^4p}{(2\pi)^4},
\qquad
(2\pi)^4\delta^4\!\left(\sum k_{\rm ext}\right).
$$

### 2.2 Vector multiplet \(V\)

$$
S_V
=
\operatorname{tr}\int d^4x\,d^4\theta
\left[
-\frac12 V\Box V
+
\frac12 [V,(D^\alpha V)](\bar D^2D_\alpha V)
+\cdots
\right]. \tag{6.3.5}
$$

$$
e^{-V}D_\alpha e^V
=
D_\alpha V
+\frac12[D_\alpha V,V]
+\frac1{3!}[[D_\alpha V,V],V]
+\cdots . \tag{6.3.15}
$$

$$
VV:\qquad
-\frac1{p^2}\,\delta^4(\theta-\theta'). \tag{6.3.15a}
$$

### 2.3 Chiral multiplet \((\Phi,\bar\Phi)\)

$$
S^{(2)}
=
\int d^4x\,d^4\theta\,\bar\Phi\Phi
-\frac12\int d^4x\,d^2\theta\,m\Phi^2
-\frac12\int d^4x\,d^2\bar\theta\,m\bar\Phi^2
$$

$$
\qquad
+
\int d^4x\,d^2\theta\,j\Phi
+
\int d^4x\,d^2\bar\theta\,\bar j\bar\Phi. \tag{6.3.7}
$$

$$
\Phi\bar\Phi:\qquad
\frac{1}{p^2+m^2}\,\delta^4(\theta-\theta'), \tag{6.3.15b}
$$

$$
\Phi\Phi:\qquad
-\frac{mD^2}{p^2(p^2+m^2)}\,\delta^4(\theta-\theta'), \tag{6.3.15c}
$$

$$
\bar\Phi\bar\Phi:\qquad
-\frac{mD^2}{p^2(p^2+m^2)}\,\delta^4(\theta-\theta'). \tag{6.3.15d}
$$

$$
\text{chiral line leaving a vertex} \Rightarrow \bar D^2,
\qquad
\text{antichiral line leaving a vertex} \Rightarrow D^2.
$$

$$
\text{purely chiral / antichiral vertex} \Rightarrow
\text{omit one corresponding }D^2\text{ or }\bar D^2.
$$

### 2.4 Ghost superfields

$$
S_{FP}
=
\operatorname{tr}\int d^4x\,d^4\theta\,
(b+\bar b)\,
L_{\frac12 V}
\Bigl[
(c+\bar c)+\coth L_{\frac12 V}(c-\bar c)
\Bigr]. \tag{6.2.20}
$$

$$
S_{FP}^{(2)}
=
\operatorname{tr}\int d^4x\,d^4\theta\,
(\bar b c-b\bar c). \tag{6.2.22}
$$

$$
\text{ghosts are chiral superfields and follow the same rules.}
$$
