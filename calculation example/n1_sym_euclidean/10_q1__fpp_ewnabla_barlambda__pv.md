---
title: 'Q_1(O)（f_{++}e^{w\nabla}\bar\lambda_{\dot\beta}） / PV'
doc_type: calculation
theory: 'N=1 SYM (Euclidean)'
regularization: PV
supercharge: Q_-
loop_order: 1
operator: 'f_{++}e^{w\nabla}\bar\lambda_{\dot\beta}'
status: canonical
---

## Step 1: Operator / current / vertex

$$
\boxed{Q_1\equiv Q_-}.
$$

$$
\boxed{\text{same }Q_-\text{ as in }conventions\_and\_rules.md;\ \text{parent }N=4\text{ notation: }Q_-^4.}
$$

$$
\delta_{Q_1}=\delta_{Q_-},
\qquad
J^\mu_{Q_1}=J^\mu_-,
\qquad
\partial_\mu J^\mu_{Q_1}=\partial_\mu J^\mu_-.
$$

$$
\kappa_A=\frac{i}{2},
\qquad
\delta_{Q_-}^{\rm cl}A_{+\dot\alpha}=\kappa_A\,\bar\lambda_{\dot\alpha},
\qquad
\delta_{Q_-}^{\rm cl}\bar\lambda_{\dot\alpha}=0.
$$

$$
w\cdot\nabla_+ := w^{+\dot\alpha}\nabla_{+\dot\alpha}.
$$

$$
\mathcal O_{w,\dot\beta}^{AB}(p)
:=
\int_{p_1,p_2}
f_{++}^A(p_1)\,
\big(e^{w\cdot\nabla_+}\bar\lambda_{\dot\beta}^B\big)(p_2)\,
\delta_{p-p_1-p_2}.
$$

$$
\delta_{Q_-}^{\rm cl}f_{++}^A
=
2\kappa_A\,\nabla_{+\dot\gamma}\bar\lambda^{A\dot\gamma},
$$

$$
\delta_{Q_-}^{\rm cl}\!\big(e^{w\cdot\nabla_+}\bar\lambda_{\dot\beta}^B\big)
=
\kappa_A
\int_0^1 ds\;
e^{s w\cdot\nabla_+}
\Big(
w^{\dot\alpha}\operatorname{ad}_{\bar\lambda_{\dot\alpha}}
\Big)
e^{(1-s) w\cdot\nabla_+}\bar\lambda_{\dot\beta}^B.
$$

$$
\delta_{Q_-}^{\rm cl}\mathcal O_{w,\dot\beta}^{AB}
=
\big(2\kappa_A\,\nabla_{+\dot\gamma}\bar\lambda^{A\dot\gamma}\big)\,
\big(e^{w\cdot\nabla_+}\bar\lambda_{\dot\beta}^B\big)
+
f_{++}^A\,
\delta_{Q_-}^{\rm cl}\!\big(e^{w\cdot\nabla_+}\bar\lambda_{\dot\beta}^B\big).
$$

$$
J^\mu_-=J^{\mu,(2)}_-+J^{\mu,(3)}_-,
\qquad
J^{(2)}_-\sim (\partial A)\bar\lambda,
\qquad
J^{(3)}_-\sim [A,A]\bar\lambda.
$$

$$
\langle f_{++}(x)f_{++}(y)\rangle_0=0,
\qquad
\langle f_{+-}(x)f_{++}(y)\rangle_0=0,
\qquad
\langle f_{--}(x)f_{++}(y)\rangle_0=2K(x-y).
$$

## Step 2: Wick contraction

![](../../assets/step4/calculation_triangles/n1_q1_fpp_expw_barlambda_triangle_pair.png)

$$
\big\langle \partial_\mu J^\mu_-(x)\,\mathcal O_{w,\dot\beta}^{AB}(y)\big\rangle_{\rm conn,loc}
=
T_L^{AB}(w;x,y)
+
T_R^{AB}(w;x,y).
$$

$$
T_L^{AB}(w)
=
T_{L,\rm lin-lin}^{AB}(w)
+
T_{L,\rm lin-quad}^{AB}(w)
+
T_{L,\rm quad-lin}^{AB}(w).
$$

$$
T_R^{AB}(w)
=
T_{R,\rm dec}^{AB}(w).
$$

$$
T_L^{AB}(w;x,y)
\Longrightarrow
\delta^{(4)}(x-y)\,
\big(2\kappa_A\,\nabla_{+\dot\gamma}\bar\lambda^{A\dot\gamma}\big)\,
\big(e^{w\cdot\nabla_+}\bar\lambda_{\dot\beta}^B\big)(y).
$$

$$
T_R^{AB}(w;x,y)
\Longrightarrow
\delta^{(4)}(x-y)\,
f_{++}^A\,
\delta_{Q_-}^{\rm cl}\!\big(e^{w\cdot\nabla_+}\bar\lambda_{\dot\beta}^B\big)(y).
$$

## Step 3: WT contact reconstruction

$$
T_L^{AB}(w)
+
T_R^{AB}(w)
\Longrightarrow
\delta^{(4)}(x-y)\,
\delta_{Q_-}^{\rm cl}\mathcal O_{w,\dot\beta}^{AB}(y).
$$

$$
t^0(\cdots)=\Gamma_{\rm cl}.
$$

## Step 4: Regularization and consistency condition

$$
\big\langle \partial_\mu J^\mu_-(x)\,\mathcal O_{w,\dot\beta}^{AB}(y)\big\rangle_{\rm PV,loc}
=
\delta^{(4)}(x-y)\,
\delta_{Q_-}^{\rm cl}\mathcal O_{w,\dot\beta}^{AB}(y).
$$

$$
t^0(\cdots)-\Gamma_{\rm cl}=0.
$$

$$
\boxed{
\text{no new pure-SYM gauge-invariant local remainder in the }\partial_\mu J^\mu_-\text{ channel}
}.
$$

## Step 5: Simplification examples

$$
\delta_{Q_-}^{\rm cl}\!\big(e^{0\cdot\nabla_+}\bar\lambda_{\dot\beta}^B\big)=0.
$$

$$
\delta_{Q_-}^{\rm cl}\mathcal O_{w=0,\dot\beta}^{AB}
=
\big(2\kappa_A\,\nabla_{+\dot\gamma}\bar\lambda^{A\dot\gamma}\big)\bar\lambda_{\dot\beta}^B.
$$

$$
t^0(\cdots)-\Gamma_{\rm cl}=0.
$$
