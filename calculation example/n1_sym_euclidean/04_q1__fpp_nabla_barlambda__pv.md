---
title: 'Q_1(O)（f_{++}\nabla_{+\dot\gamma}\bar\lambda_{\dot\alpha}） / PV'
doc_type: calculation
theory: 'N=1 SYM (Euclidean)'
regularization: PV
supercharge: Q_-
loop_order: 1
operator: 'f_{++}\nabla_{+\dot\gamma}\bar\lambda_{\dot\alpha}'
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
\mathcal O_{\dot\theta\dot\beta}^{AB}(p)
:=
\int_{p_1,p_2}
f_{++}^A(p_1)\,
\nabla_{+\dot\theta}\bar\lambda_{\dot\beta}^B(p_2)\,
\delta_{p-p_1-p_2}.
$$

$$
\delta_{Q_-}^{\rm cl}f_{++}^A
=
2\kappa_A\,\nabla_{+\dot\gamma}\bar\lambda^{A\dot\gamma},
\qquad
\delta_{Q_-}^{\rm cl}(\nabla_{+\dot\theta}\bar\lambda_{\dot\beta}^B)
=
\kappa_A\,\operatorname{ad}_{\bar\lambda_{\dot\theta}}\bar\lambda_{\dot\beta}^B.
$$

$$
\delta_{Q_-}^{\rm cl}\mathcal O_{\dot\theta\dot\beta}^{AB}
=
\big(2\kappa_A\,\nabla_{+\dot\gamma}\bar\lambda^{A\dot\gamma}\big)\,
\nabla_{+\dot\theta}\bar\lambda_{\dot\beta}^B
+
f_{++}^A\,
\kappa_A\,\operatorname{ad}_{\bar\lambda_{\dot\theta}}\bar\lambda_{\dot\beta}^B.
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

## Step C: local WT extraction

$$
\sum_{\rm diagrams}
\big[\partial_\mu J_-^\mu(x)\cdot \mathcal O(y)\big]_{\rm local}
$$

$$
\text{keep only local pieces matching }
-\delta^{(4)}(x-y)\,Q_-^{\rm cl}\mathcal O(y).
$$

$$
\text{discard }
\text{nonlocal},
\qquad
\text{improvement},
\qquad
\gamma_\mu S^\mu\text{-channel},
\qquad
R\text{-current/trace-channel}.
$$

![](../../assets/step4/calculation_triangles/n1_q1_fpp_nabla_barlambda_triangle_pair.png)

$$
\big\langle \partial_\mu J^\mu_-(x)\,\mathcal O_{\dot\theta\dot\beta}^{AB}(y)\big\rangle_{\rm conn,loc}
=
T_{f,\dot\theta\dot\beta}^{AB}(x,y)
+
T_{{\rm dec},\dot\theta\dot\beta}^{AB}(x,y).
$$

$$
T_{f,\dot\theta\dot\beta}^{AB}
=
T_{f,\rm lin-lin,\dot\theta\dot\beta}^{AB}
+
T_{f,\rm lin-quad,\dot\theta\dot\beta}^{AB}
+
T_{f,\rm quad-lin,\dot\theta\dot\beta}^{AB}.
$$

$$
T_{f,\dot\theta\dot\beta}^{AB}(x,y)
\Longrightarrow
\delta^{(4)}(x-y)\,
\big(2\kappa_A\,\nabla_{+\dot\gamma}\bar\lambda^{A\dot\gamma}\big)\,
\nabla_{+\dot\theta}\bar\lambda_{\dot\beta}^B(y).
$$

$$
T_{{\rm dec},\dot\theta\dot\beta}^{AB}(x,y)
\Longrightarrow
\delta^{(4)}(x-y)\,
f_{++}^A\,
\kappa_A\,\operatorname{ad}_{\bar\lambda_{\dot\theta}}\bar\lambda_{\dot\beta}^B(y).
$$

### Target-matching regrouping

$$
T_{f,\dot\theta\dot\beta}^{AB}
+
T_{{\rm dec},\dot\theta\dot\beta}^{AB}
\Longrightarrow
-\delta^{(4)}(x-y)\,
\delta_{Q_-}^{\rm cl}\mathcal O_{\dot\theta\dot\beta}^{AB}(y).
$$

$$
t^0(\cdots)=\Gamma_{\rm cl}.
$$

## Step D: consistency closure

$$
\sum_{\rm diagrams}
\big[\partial_\mu J_-^\mu(x)\cdot \mathcal O(y)\big]_{\rm local}
=
-\delta^{(4)}(x-y)\,Q_-^{\rm cl}\mathcal O(y),
$$

$$
t^0(\cdots)-\Gamma_{\rm cl}=0.
$$

$$
\boxed{
\text{pure }N=1\ \text{SYM divergence channel closes as a WT contact term only.}
}
$$


## Step 5: Simplification examples

$$
\big\langle \partial_\mu J^\mu_-(x)\,\operatorname{Tr}\!\big(f_{++}\nabla_{+\dot\theta}\bar\lambda_{\dot\beta}\big)(y)\big\rangle_{\rm conn,loc}
\Longrightarrow
-\delta^{(4)}(x-y)\,
\delta_{Q_-}^{\rm cl}\operatorname{Tr}\!\big(f_{++}\nabla_{+\dot\theta}\bar\lambda_{\dot\beta}\big)(y).
$$

$$
t^0(\cdots)-\Gamma_{\rm cl}=0.
$$
