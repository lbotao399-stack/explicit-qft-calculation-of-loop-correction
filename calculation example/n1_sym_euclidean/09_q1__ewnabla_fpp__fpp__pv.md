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
w\cdot\nabla_+ := w^{+\dot\alpha}\nabla_{+\dot\alpha},
\qquad
w\cdot p_a := w^{+\dot\alpha}p_{a,+\dot\alpha}.
$$

$$
\mathcal O_w^{AB}(p)
:=
\int_{p_1,p_2}
\big(e^{w\cdot\nabla_+}f_{++}^A\big)(p_1)\,
f_{++}^B(p_2)\,
\delta_{p-p_1-p_2}.
$$

## Step 2: Wick contraction

![](../../assets/step4/calculation_triangles/n1_q1_expw_fpp_fpp_triangle_pair.png)

$$
\mathcal I\!\left[Q_1\mathcal O_w^{AB}(p)\right]_{\rm PV,\,1\text{-}loop,\,loc}
=
\widehat\Gamma_{12}^{AB}(w)
+
\widehat\Gamma_{21}^{AB}(w).
$$

## Step 3: Local part

$$
X_{12}:=(x+z)p_1+z p_2,
\qquad
Y_{12}:=y p_1+(x+y)p_2,
$$

$$
X_{21}:=z p_1+(x+z)p_2,
\qquad
Y_{21}:=(x+y)p_1+y p_2.
$$

## Step 4: Regularization and final local anomaly

$$
\widehat{\mathcal G}_{12,+\dot\beta}(w;p_1,p_2)
:=
\int_\Delta e^{\,i w\cdot X_{12}}\,Y_{12,+\dot\beta},
\qquad
\widehat{\mathcal G}_{21,+\dot\beta}(w;p_1,p_2)
:=
\int_\Delta e^{\,i w\cdot X_{21}}\,Y_{21,+\dot\beta}.
$$

$$
\boxed{
\mathcal I\!\left[Q_1\mathcal O_w^{AB}(p)\right]_{\rm PV,\,1\text{-}loop,\,loc}
=
-\frac{g^2}{8\pi^2}
\int_{p_1,p_2}\delta_{p-p_1-p_2}
\Big[
\widehat{\mathcal G}_{12,+\dot\beta}(w;p_1,p_2)\,\mathscr F_{12}^{AB,\dot\beta}
+
\widehat{\mathcal G}_{21,+\dot\beta}(w;p_1,p_2)\,\mathscr F_{21}^{AB,\dot\beta}
\Big].
}
$$

$$
\widehat{\mathbb D}_{12,+\dot\beta}(w)
:=
\int_\Delta
e^{\,w\cdot\big((x+z)\nabla_+^{(1)}+z\nabla_+^{(2)}\big)}
\Big(y\nabla_{+\dot\beta}^{(1)}+(x+y)\nabla_{+\dot\beta}^{(2)}\Big),
$$

$$
\widehat{\mathbb D}_{21,+\dot\beta}(w)
:=
\int_\Delta
e^{\,w\cdot\big(z\nabla_+^{(1)}+(x+z)\nabla_+^{(2)}\big)}
\Big((x+y)\nabla_{+\dot\beta}^{(1)}+y\nabla_{+\dot\beta}^{(2)}\Big).
$$

## Step 5: Simplification examples

$$
\widehat{\mathcal G}_{12,+\dot\beta}(0)=\frac16(p_1+2p_2)_{+\dot\beta},
\qquad
\widehat{\mathcal G}_{21,+\dot\beta}(0)=\frac16(2p_1+p_2)_{+\dot\beta}.
$$
