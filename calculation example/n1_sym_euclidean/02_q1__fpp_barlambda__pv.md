---
title: 'Q_1(O)（f_{++}\bar\lambda_{\dot\alpha}） / PV'
doc_type: calculation
theory: 'N=1 SYM (Euclidean)'
regularization: PV
supercharge: Q_-
loop_order: 1
operator: 'f_{++}\bar\lambda_{\dot\alpha}'
status: canonical
---

## Step 1: Operator / current / vertex

$$
\mathcal O_{\dot\beta}^{AB}(p)
:=
\int_{p_1,p_2}
f_{++}^A(p_1)\,
\bar\lambda_{\dot\beta}^B(p_2)\,
\delta_{p-p_1-p_2}.
$$

$$
p=p_1+p_2.
$$

## Step 2: Wick contraction

![](../../assets/step4/calculation_triangles/n1_q1_fpp_barlambda_triangle_pair.png)

$$
\mathcal I\!\left[Q_1\mathcal O_{\dot\beta}^{AB}(p)\right]_{\rm PV,\,1\text{-}loop,\,loc}
=
\Gamma_{12,\dot\beta}^{AB}(p)
+
\Gamma_{21,\dot\beta}^{AB}(p).
$$

## Step 3: Local part

$$
\Gamma_{12,\dot\beta;M}^{\rm PV\text{-}loop}
=
2g^2\int_q
\frac{(q-p_2)_{+\dot\beta}}{(q^2+M^2)\big((q-p_2)^2+M^2\big)}\,
\mathscr C_{12}
-2g^2M^2\int_q
\frac{(q-p_2)_{+\dot\beta}}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}\,
\mathscr C_{12},
$$

$$
\Gamma_{21,\dot\beta;M}^{\rm PV\text{-}loop}
=
2g^2\int_q
\frac{(q-p_1)_{+\dot\beta}}{(q^2+M^2)\big((q-p_1)^2+M^2\big)}\,
\mathscr C_{21}
-2g^2M^2\int_q
\frac{(q-p_1)_{+\dot\beta}}{(q^2+M^2)\big((q+p_2)^2+M^2\big)\big((q-p_1)^2+M^2\big)}\,
\mathscr C_{21}.
$$

## Step 4: Regularization and final local anomaly

$$
\frac{1}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}
=
2\int_\Delta
\frac{1}{\big[(q+y p_1-z p_2)^2+M^2+\Delta\big]^3}.
$$

$$
\ell=q+y p_1-z p_2,
\qquad
q-p_2=\ell-y p-x p_2.
$$

$$
\Gamma_{12,\dot\beta}^{({\rm anom,loc})}
=
-\frac{g^2}{48\pi^2}
(p_1+2p_2)_{+\dot\beta}\,
\mathscr C_{12},
$$

$$
\Gamma_{21,\dot\beta}^{({\rm anom,loc})}
=
-\frac{g^2}{48\pi^2}
(2p_1+p_2)_{+\dot\beta}\,
\mathscr C_{21}.
$$

$$
\mathscr B^{AB}(p)
:=
\int_{p_1,p_2}\delta_{p-p_1-p_2}\,
\mathscr C_{12}^{AB}(p_1,p_2).
$$

$$
\boxed{
\mathcal I\!\left[Q_1\mathcal O_{\dot\beta}^{AB}(p)\right]_{\rm PV,\,1\text{-}loop,\,loc}
=
-\frac{g^2}{16\pi^2}\,
p_{+\dot\beta}\,
\mathscr B^{AB}(p).
}
$$

$$
\boxed{
Q_1\mathcal O_{\dot\beta}^{AB}(x)\Big|_{\rm PV,\,1\text{-}loop,\,loc}
=
\frac{g^2}{16\pi^2}\,
i\partial_{+\dot\beta}\,
\mathscr B^{AB}(x).
}
$$

## Step 5: Simplification examples

$$
\mathscr C_{12}^{AB}(p_1,p_2)
=
\epsilon^{\dot\gamma\dot\delta}
f^{CA}{}_{E}f^{DB}{}_{E}\,
\bar\lambda_{\dot\gamma}^{C}(p_1)\,
\bar\lambda_{\dot\delta}^{D}(p_2),
\qquad
\mathscr C_{21}^{AB}(p_1,p_2)=\mathscr C_{12}^{AB}(p_2,p_1).
$$
