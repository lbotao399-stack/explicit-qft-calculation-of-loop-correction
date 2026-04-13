---
title: 'Q_1(O)（(\nabla_{+\dot\alpha}f_{++})\nabla_{+\dot\beta}\bar\lambda_{\dot\gamma}） / PV'
doc_type: calculation
theory: 'N=1 SYM (Euclidean)'
regularization: PV
supercharge: Q_-
loop_order: 1
operator: '(\nabla_{+\dot\alpha}f_{++})\nabla_{+\dot\beta}\bar\lambda_{\dot\gamma}'
status: canonical
---

## Step 1: Operator / current / vertex

$$
\mathcal O_{\dot\alpha\dot\beta\dot\gamma}^{AB}(p)
:=
\int_{p_1,p_2}
\big(\nabla_{+\dot\alpha}f_{++}^A\big)(p_1)\,
\big(\nabla_{+\dot\beta}\bar\lambda_{\dot\gamma}^B\big)(p_2)\,
\delta_{p-p_1-p_2}.
$$

$$
p=p_1+p_2.
$$

## Step 2: Wick contraction

![](../../assets/step4/calculation_triangles/n1_q1_nabla_fpp_nabla_barlambda_triangle_pair.png)

$$
\mathcal I\!\left[Q_1\mathcal O_{\dot\alpha\dot\beta\dot\gamma}^{AB}(p)\right]_{\rm PV,\,1\text{-}loop,\,loc}
=
\Gamma_{12,\dot\alpha\dot\beta\dot\gamma}^{AB}(p)
+
\Gamma_{21,\dot\alpha\dot\beta\dot\gamma}^{AB}(p).
$$

## Step 3: Local part

$$
\Gamma_{12;M}^{\rm PV\text{-}loop}{}_{\dot\alpha\dot\beta\dot\gamma}
=
-2g^2\int_q
\frac{(q+p_1)_{+\dot\alpha}(q-p_2)_{+\dot\beta}(q-p_2)_{+\dot\gamma}}
{(q^2+M^2)\big((q-p_2)^2+M^2\big)}\,
\mathscr C_{12}
$$

$$
\qquad
+
2g^2M^2\int_q
\frac{(q+p_1)_{+\dot\alpha}(q-p_2)_{+\dot\beta}(q-p_2)_{+\dot\gamma}}
{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}\,
\mathscr C_{12},
$$

$$
\Gamma_{21;M}^{\rm PV\text{-}loop}{}_{\dot\alpha\dot\beta\dot\gamma}
=
-2g^2\int_q
\frac{(q+p_2)_{+\dot\alpha}(q-p_1)_{+\dot\beta}(q-p_1)_{+\dot\gamma}}
{(q^2+M^2)\big((q-p_1)^2+M^2\big)}\,
\mathscr C_{21}
$$

$$
\qquad
+
2g^2M^2\int_q
\frac{(q+p_2)_{+\dot\alpha}(q-p_1)_{+\dot\beta}(q-p_1)_{+\dot\gamma}}
{(q^2+M^2)\big((q+p_2)^2+M^2\big)\big((q-p_1)^2+M^2\big)}\,
\mathscr C_{21}.
$$

## Step 4: Regularization and final local anomaly

$$
\Omega_{12,+\dot\alpha,+\dot\beta,+\dot\gamma}(p_1,p_2)
:=
2\,p_{1,+\dot\alpha}p_{1,+\dot\beta}p_{1,+\dot\gamma}
+
7\,p_{1,+\dot\alpha}p_{1,+(\dot\beta}p_{2,+\dot\gamma)}
+
9\,p_{1,+\dot\alpha}p_{2,+\dot\beta}p_{2,+\dot\gamma}
$$

$$
\qquad
+
p_{2,+\dot\alpha}p_{1,+\dot\beta}p_{1,+\dot\gamma}
+
3\,p_{2,+\dot\alpha}p_{1,+(\dot\beta}p_{2,+\dot\gamma)}
+
3\,p_{2,+\dot\alpha}p_{2,+\dot\beta}p_{2,+\dot\gamma},
$$

$$
\Omega_{21,+\dot\alpha,+\dot\beta,+\dot\gamma}(p_1,p_2)
:=
\Omega_{12,+\dot\alpha,+\dot\beta,+\dot\gamma}(p_2,p_1).
$$

$$
\Gamma_{12}^{({\rm anom,loc})}{}_{\dot\alpha\dot\beta\dot\gamma}
=
\frac{g^2}{480\pi^2}\,
\Omega_{12,+\dot\alpha,+\dot\beta,+\dot\gamma}(p_1,p_2)\,
\mathscr C_{12},
$$

$$
\Gamma_{21}^{({\rm anom,loc})}{}_{\dot\alpha\dot\beta\dot\gamma}
=
\frac{g^2}{480\pi^2}\,
\Omega_{21,+\dot\alpha,+\dot\beta,+\dot\gamma}(p_1,p_2)\,
\mathscr C_{21}.
$$

$$
\boxed{
\mathcal I\!\left[Q_1\mathcal O_{\dot\alpha\dot\beta\dot\gamma}^{AB}(p)\right]_{\rm PV,\,1\text{-}loop,\,loc}
=
\frac{g^2}{480\pi^2}
\int_{p_1,p_2}\delta_{p-p_1-p_2}
\Big[
\Omega_{12,+\dot\alpha,+\dot\beta,+\dot\gamma}\,\mathscr C_{12}^{AB}
+
\Omega_{21,+\dot\alpha,+\dot\beta,+\dot\gamma}\,\mathscr C_{21}^{AB}
\Big].
}
$$

## Step 5: Simplification examples

$$
\mathscr C_{12}^{AB}(p_1,p_2)
=
\epsilon^{\dot\delta\dot\epsilon}
f^{CA}{}_{E}f^{DB}{}_{E}\,
\bar\lambda_{\dot\delta}^{C}(p_1)\bar\lambda_{\dot\epsilon}^{D}(p_2),
\qquad
\mathscr C_{21}^{AB}(p_1,p_2)=\mathscr C_{12}^{AB}(p_2,p_1).
$$
