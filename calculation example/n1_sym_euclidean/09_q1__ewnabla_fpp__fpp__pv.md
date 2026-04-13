---
title: 'Q_1(O)（e^{w\nabla}f_{++}f_{++}） / PV'
doc_type: calculation
theory: 'N=1 SYM (Euclidean)'
regularization: PV
supercharge: Q_-
loop_order: 1
operator: 'e^{w\nabla}f_{++}f_{++}'
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
\mathcal O_w^{AB}(p)
:=
\int_{p_1,p_2}
\big(e^{w\cdot\nabla_+}f_{++}^A\big)(p_1)\,
f_{++}^B(p_2)\,
\delta_{p-p_1-p_2}.
$$

$$
\delta_{Q_-}^{\rm cl}\!\big(e^{w\cdot\nabla_+}f_{++}^A\big)
=
2\kappa_A\,e^{w\cdot\nabla_+}\nabla_{+\dot\beta}\bar\lambda^{A\dot\beta}
+
\kappa_A
\int_0^1 ds\;
e^{s w\cdot\nabla_+}
\Big(
w^{\dot\alpha}\operatorname{ad}_{\bar\lambda_{\dot\alpha}}
\Big)
e^{(1-s) w\cdot\nabla_+}f_{++}^A,
$$

$$
\delta_{Q_-}^{\rm cl}f_{++}^B
=
2\kappa_A\,\nabla_{+\dot\gamma}\bar\lambda^{B\dot\gamma}.
$$

$$
\delta_{Q_-}^{\rm cl}\mathcal O_w^{AB}
=
\delta_{Q_-}^{\rm cl}\!\big(e^{w\cdot\nabla_+}f_{++}^A\big)\,f_{++}^B
+
\big(e^{w\cdot\nabla_+}f_{++}^A\big)\,
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

![](../../assets/step4/calculation_triangles/n1_q1_expw_fpp_fpp_triangle_pair.png)

$$
\big\langle \partial_\mu J^\mu_-(x)\,\mathcal O_w^{AB}(y)\big\rangle_{\rm conn,loc}
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
T_{R,\rm lin-lin}^{AB}(w)
+
T_{R,\rm lin-quad}^{AB}(w)
+
T_{R,\rm quad-lin}^{AB}(w).
$$

$$
T_L^{AB}(w;x,y)
\Longrightarrow
-\delta^{(4)}(x-y)\,
\delta_{Q_-}^{\rm cl}\!\big(e^{w\cdot\nabla_+}f_{++}^A\big)\,f_{++}^B(y).
$$

$$
T_R^{AB}(w;x,y)
\Longrightarrow
\delta^{(4)}(x-y)\,
\big(e^{w\cdot\nabla_+}f_{++}^A\big)\,
\big(2\kappa_A\,\nabla_{+\dot\gamma}\bar\lambda^{B\dot\gamma}\big)(y).
$$

### Target-matching regrouping

$$
T_L^{AB}(w)
+
T_R^{AB}(w)
\Longrightarrow
-\delta^{(4)}(x-y)\,
\delta_{Q_-}^{\rm cl}\mathcal O_w^{AB}(y).
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
\mathcal O_{w=0}^{AB}=\mathcal O_{ff}^{AB}.
$$

$$
\delta_{Q_-}^{\rm cl}\!\big(e^{0\cdot\nabla_+}f_{++}^A\big)
=
2\kappa_A\,\nabla_{+\dot\beta}\bar\lambda^{A\dot\beta}.
$$

$$
t^0(\cdots)-\Gamma_{\rm cl}=0.
$$
