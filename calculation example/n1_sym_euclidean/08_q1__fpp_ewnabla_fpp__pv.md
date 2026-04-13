---
title: 'Q_1(O)（f_{++}e^{w\nabla}f_{++}） / PV'
doc_type: calculation
theory: 'N=1 SYM (Euclidean)'
regularization: PV
supercharge: Q_-
loop_order: 1
operator: 'f_{++}e^{w\nabla}f_{++}'
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
w\cdot\nabla_+ := w^{+\dot\alpha}\nabla_{+\dot\alpha}.
$$

$$
\mathcal O_w^{AB}(p)
:=
\int_{p_1,p_2}
f_{++}^A(p_1)\,
\big(e^{w\cdot\nabla_+}f_{++}^B\big)(p_2)\,
\delta_{p-p_1-p_2}.
$$

$$
Q_- f_{++}^A=iD_{+\dot\gamma}\bar\lambda^{A\dot\gamma}.
$$

$$
\big[\delta_{Q_-}^{\rm cl}\mathcal O_w^{AB}\big]_{L}
:=
\big(iD_{+\dot\gamma}\bar\lambda^{A\dot\gamma}\big)\,
\big(e^{w\cdot\nabla_+}f_{++}^B\big).
$$

$$
\big[\delta_{Q_-}^{\rm cl}\mathcal O_w^{AB}\big]_{R}
:=
f_{++}^A\,
\delta_{Q_-}^{\rm cl}\big(e^{w\cdot\nabla_+}f_{++}^B\big).
$$

$$
\delta_{Q_-}^{\rm cl}\mathcal O_w^{AB}
=
\big[\delta_{Q_-}^{\rm cl}\mathcal O_w^{AB}\big]_{L}
+
\big[\delta_{Q_-}^{\rm cl}\mathcal O_w^{AB}\big]_{R}.
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

![](../../assets/step4/calculation_triangles/n1_q1_fpp_expw_fpp_triangle_pair.png)

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
\delta^{(4)}(x-y)\,
\big[\delta_{Q_-}^{\rm cl}\mathcal O_w^{AB}(y)\big]_{L}.
$$

$$
T_R^{AB}(w;x,y)
\Longrightarrow
\delta^{(4)}(x-y)\,
\big[\delta_{Q_-}^{\rm cl}\mathcal O_w^{AB}(y)\big]_{R}.
$$

## Step 3: WT contact reconstruction

$$
T_L^{AB}(w)
+
T_R^{AB}(w)
\Longrightarrow
\delta^{(4)}(x-y)\,
\delta_{Q_-}^{\rm cl}\mathcal O_w^{AB}(y).
$$

$$
t^0(\cdots)=\Gamma_{\rm cl}.
$$

## Step 4: Regularization and consistency condition

$$
\big\langle \partial_\mu J^\mu_-(x)\,\mathcal O_w^{AB}(y)\big\rangle_{\rm PV,loc}
=
\delta^{(4)}(x-y)\,
\delta_{Q_-}^{\rm cl}\mathcal O_w^{AB}(y).
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
\mathcal O_{w=0}^{AB}=\mathcal O_{ff}^{AB}.
$$

$$
\big\langle \partial_\mu J^\mu_-(x)\,\mathcal O_{w=0}^{AB}(y)\big\rangle_{\rm conn,loc}
\Longrightarrow
\delta^{(4)}(x-y)\,
\delta_{Q_-}^{\rm cl}\mathcal O_{ff}^{AB}(y).
$$

$$
t^0(\cdots)-\Gamma_{\rm cl}=0.
$$
