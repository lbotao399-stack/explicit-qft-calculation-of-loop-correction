---
title: 'Q_1(O)（(\nabla_{+\dot\alpha}f_{++})f_{++}） / PV'
doc_type: calculation
theory: 'N=1 SYM (Euclidean)'
regularization: PV
supercharge: Q_-
loop_order: 1
operator: '(\nabla_{+\dot\alpha}f_{++})f_{++}'
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
\mathcal O_{\dot\theta}^{AB}(p)
:=
\int_{p_1,p_2}
\big(\nabla_{+\dot\theta}f_{++}^A\big)(p_1)\,
f_{++}^B(p_2)\,
\delta_{p-p_1-p_2}.
$$

$$
\delta_{Q_-}^{\rm cl}(\nabla_{+\dot\theta}f_{++}^A)
=
2\kappa_A\,\nabla_{+\dot\theta}\nabla_{+\dot\gamma}\bar\lambda^{A\dot\gamma}
+
\kappa_A\,\operatorname{ad}_{\bar\lambda_{\dot\theta}}f_{++}^A,
$$

$$
\delta_{Q_-}^{\rm cl}f_{++}^B
=
2\kappa_A\,\nabla_{+\dot\gamma}\bar\lambda^{B\dot\gamma}.
$$

$$
\delta_{Q_-}^{\rm cl}\mathcal O_{\dot\theta}^{AB}
=
\Big(
2\kappa_A\,\nabla_{+\dot\theta}\nabla_{+\dot\gamma}\bar\lambda^{A\dot\gamma}
+
\kappa_A\,\operatorname{ad}_{\bar\lambda_{\dot\theta}}f_{++}^A
\Big)f_{++}^B
+
\big(\nabla_{+\dot\theta}f_{++}^A\big)
\big(2\kappa_A\,\nabla_{+\dot\gamma}\bar\lambda^{B\dot\gamma}\big).
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

![](../../assets/step4/calculation_triangles/n1_q1_nabla_fpp_fpp_triangle_pair.png)

$$
\big\langle \partial_\mu J^\mu_-(x)\,\mathcal O_{\dot\theta}^{AB}(y)\big\rangle_{\rm conn,loc}
=
T_{L,\dot\theta}^{AB}(x,y)
+
T_{R,\dot\theta}^{AB}(x,y).
$$

$$
T_{L,\dot\theta}^{AB}
=
T_{L,\rm lin-lin,\dot\theta}^{AB}
+
T_{L,\rm lin-quad,\dot\theta}^{AB}
+
T_{L,\rm quad-lin,\dot\theta}^{AB}.
$$

$$
T_{R,\dot\theta}^{AB}
=
T_{R,\rm lin-lin,\dot\theta}^{AB}
+
T_{R,\rm lin-quad,\dot\theta}^{AB}
+
T_{R,\rm quad-lin,\dot\theta}^{AB}.
$$

$$
T_{L,\dot\theta}^{AB}(x,y)
\Longrightarrow
\delta^{(4)}(x-y)\,
\Big(
2\kappa_A\,\nabla_{+\dot\theta}\nabla_{+\dot\gamma}\bar\lambda^{A\dot\gamma}
+
\kappa_A\,\operatorname{ad}_{\bar\lambda_{\dot\theta}}f_{++}^A
\Big)f_{++}^B(y).
$$

$$
T_{R,\dot\theta}^{AB}(x,y)
\Longrightarrow
\delta^{(4)}(x-y)\,
\big(\nabla_{+\dot\theta}f_{++}^A\big)\big(2\kappa_A\,\nabla_{+\dot\gamma}\bar\lambda^{B\dot\gamma}\big)(y).
$$

## Step 3: WT contact reconstruction

$$
T_{L,\dot\theta}^{AB}
+
T_{R,\dot\theta}^{AB}
\Longrightarrow
\delta^{(4)}(x-y)\,
\delta_{Q_-}^{\rm cl}\mathcal O_{\dot\theta}^{AB}(y).
$$

$$
t^0(\cdots)=\Gamma_{\rm cl}.
$$

## Step 4: Regularization and consistency condition

$$
\big\langle \partial_\mu J^\mu_-(x)\,\mathcal O_{\dot\theta}^{AB}(y)\big\rangle_{\rm PV,loc}
=
\delta^{(4)}(x-y)\,
\delta_{Q_-}^{\rm cl}\mathcal O_{\dot\theta}^{AB}(y).
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
\big\langle \partial_\mu J^\mu_-(x)\,\operatorname{Tr}\!\big((\nabla_{+\dot\theta}f_{++})f_{++}\big)(y)\big\rangle_{\rm conn,loc}
\Longrightarrow
\delta^{(4)}(x-y)\,
\delta_{Q_-}^{\rm cl}\operatorname{Tr}\!\big((\nabla_{+\dot\theta}f_{++})f_{++}\big)(y).
$$

$$
t^0(\cdots)-\Gamma_{\rm cl}=0.
$$
