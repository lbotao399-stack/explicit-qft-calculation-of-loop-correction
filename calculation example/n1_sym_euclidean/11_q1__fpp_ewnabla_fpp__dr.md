---
title: 'Q_1(O)（f_{++}e^{w\nabla}f_{++}） / DR'
doc_type: calculation
theory: 'N=1 SYM (Euclidean)'
regularization: DR
supercharge: Q_-
loop_order: 1
operator: 'f_{++}e^{w\nabla}f_{++}'
status: working
---

## Step 1: Operator / current / vertex

$$
\mathcal O_w^{AB}(p)
:=
\int_{p_1,p_2}
f_{++}^A(p_1)\,
\big(e^{w\cdot\nabla_+}f_{++}^B\big)(p_2)\,
\delta_{p-p_1-p_2}.
$$

$$
p=p_1+p_2.
$$

## Step 2: Wick contraction

![](../../assets/step4/calculation_triangles/n1_q1_fpp_expw_fpp_triangle_pair.png)

$$
\mathcal I\!\left[Q_1\mathcal O_w^{AB}(p)\right]_{\rm DR,\,1\text{-}loop,\,loc}
=
\Gamma_{12}^{AB}(w)
+
\Gamma_{21}^{AB}(w).
$$

$$
N_{\rm raw}^{[A,\widetilde\lambda]}=20,
\qquad
N_{\rm top}^{[A,\widetilde\lambda]}=6.
$$

$$
N_{\rm raw}^{[A,A,\widetilde\lambda]}=348,
\qquad
N_{\rm top}^{[A,A,\widetilde\lambda]}=20.
$$

$$
N_{\rm raw}^{[A,A,A,\widetilde\lambda]}=9152,
\qquad
N_{\rm top}^{[A,A,A,\widetilde\lambda]}=66.
$$

## Step 3: Local part

$$
\Gamma_{12}^{AB}(w)
=
-2g^2
\int_{p_1,p_2}\delta_{p-p_1-p_2}
\int_q^d
e^{\,i w\cdot(p_2-q)}
\frac{\widehat q^2\,(q-p_2)_{+\dot\beta}}
{q^2(q+p_1)^2(q-p_2)^2}\,
f^{CE}{}_{A}f^{DE}{}_{B}\,
f_{++}^C(p_1)\widetilde\lambda^{D\dot\beta}(p_2).
$$

$$
\Gamma_{21}^{AB}(w)
=
-2g^2
\int_{p_1,p_2}\delta_{p-p_1-p_2}
\int_q^d
e^{\,i w\cdot(p_1-q)}
\frac{\widehat q^2\,(q-p_1)_{+\dot\beta}}
{q^2(q+p_2)^2(q-p_1)^2}\,
f^{CE}{}_{A}f^{DE}{}_{B}\,
f_{++}^C(p_2)\widetilde\lambda^{D\dot\beta}(p_1).
$$

## Step 4: Regularization and final local anomaly

$$
\frac{1}{q^2(q+p_1)^2(q-p_2)^2}
=
2\int_\Delta
\frac{1}{\big[(q+y p_1-z p_2)^2+\Delta\big]^3}.
$$

$$
\ell=q+y p_1-z p_2.
$$

$$
p_2-q=-\ell+y p_1+(x+y)p_2,
\qquad
q-p_2=\ell-y p_1-(x+y)p_2.
$$

$$
e^{\,i w\cdot(p_2-q)}
=
e^{\,i w\cdot\big(y p_1+(x+y)p_2\big)}\,e^{-i w\cdot\ell}.
$$

$$
\Gamma_{12}^{AB}(w)\Big|_{\rm DR,\,loc}
=
-\frac{g^2}{8\pi^2}
\int_{p_1,p_2}\delta_{p-p_1-p_2}
\int_\Delta
e^{\,i w\cdot\big(y p_1+(x+y)p_2\big)}
\big(y p_1+(x+y)p_2\big)_{+\dot\beta}
f^{CE}{}_{A}f^{DE}{}_{B}\,
f_{++}^C(p_1)\widetilde\lambda^{D\dot\beta}(p_2).
$$

$$
\frac{1}{q^2(q+p_2)^2(q-p_1)^2}
=
2\int_\Delta
\frac{1}{\big[(q+y p_2-z p_1)^2+\Delta\big]^3}.
$$

$$
\ell=q+y p_2-z p_1.
$$

$$
p_1-q=-\ell+(x+y)p_1+y p_2,
\qquad
q-p_1=\ell-(x+y)p_1-y p_2.
$$

$$
e^{\,i w\cdot(p_1-q)}
=
e^{\,i w\cdot\big((x+y)p_1+y p_2\big)}\,e^{-i w\cdot\ell}.
$$

$$
\Gamma_{21}^{AB}(w)\Big|_{\rm DR,\,loc}
=
-\frac{g^2}{8\pi^2}
\int_{p_1,p_2}\delta_{p-p_1-p_2}
\int_\Delta
e^{\,i w\cdot\big((x+y)p_1+y p_2\big)}
\big((x+y)p_1+y p_2\big)_{+\dot\beta}
f^{CE}{}_{A}f^{DE}{}_{B}\,
f_{++}^C(p_2)\widetilde\lambda^{D\dot\beta}(p_1).
$$

$$
\boxed{
\mathcal I\!\left[Q_1\mathcal O_w^{AB}(p)\right]_{\rm DR,\,1\text{-}loop,\,loc}
=
-\frac{g^2}{8\pi^2}
\int_{p_1,p_2}\delta_{p-p_1-p_2}
\Big[
\int_\Delta
e^{\,i w\cdot\big(y p_1+(x+y)p_2\big)}
\big(y p_1+(x+y)p_2\big)_{+\dot\beta}\,
f^{CE}{}_{A}f^{DE}{}_{B}\,
f_{++}^C(p_1)\widetilde\lambda^{D\dot\beta}(p_2)
}
$$

$$
\boxed{
\qquad\qquad\qquad\qquad
+
\int_\Delta
e^{\,i w\cdot\big((x+y)p_1+y p_2\big)}
\big((x+y)p_1+y p_2\big)_{+\dot\beta}\,
f^{CE}{}_{A}f^{DE}{}_{B}\,
f_{++}^C(p_2)\widetilde\lambda^{D\dot\beta}(p_1)
\Big].
}
$$

$$
\boxed{
Q_1\!\left(f_{++}^A e^{w\cdot\nabla_+}f_{++}^B\right)(x)\Big|_{\rm DR,\,1\text{-}loop,\,loc}
=
\frac{i g^2}{8\pi^2}\,
f^{CE}{}_{A}f^{DE}{}_{B}
\Bigg[
\int_\Delta
e^{\,w\cdot\big(y\nabla_+^{(1)}+(x+y)\nabla_+^{(2)}\big)}
\Big(y\nabla_{+\dot\beta}^{(1)}+(x+y)\nabla_{+\dot\beta}^{(2)}\Big)
f_{++}^C(x_1)\widetilde\lambda^{D\dot\beta}(x_2)
}
$$

$$
\boxed{
\qquad\qquad\qquad\qquad
+
\int_\Delta
e^{\,w\cdot\big((x+y)\nabla_+^{(1)}+y\nabla_+^{(2)}\big)}
\Big((x+y)\nabla_{+\dot\beta}^{(1)}+y\nabla_{+\dot\beta}^{(2)}\Big)
f_{++}^C(x_2)\widetilde\lambda^{D\dot\beta}(x_1)
\Bigg]_{x_1=x_2=x}.
}
$$

## Step 5: Simplification examples

$$
\mathcal I\!\left[Q_1\big(f_{++}^A f_{++}^B\big)(p)\right]_{\rm DR,\,loc}
=
-\frac{g^2}{48\pi^2}
\int_{p_1,p_2}\delta_{p-p_1-p_2}
\Big[
(p_1+2p_2)_{+\dot\beta}\,
f^{CE}{}_{A}f^{DE}{}_{B}\,
f_{++}^C(p_1)\widetilde\lambda^{D\dot\beta}(p_2)
+
(2p_1+p_2)_{+\dot\beta}\,
f^{CE}{}_{A}f^{DE}{}_{B}\,
f_{++}^C(p_2)\widetilde\lambda^{D\dot\beta}(p_1)
\Big].
$$

$$
\mathcal I\!\left[Q_1\!\left(f_{++}^A e^{w\cdot\nabla_+}f_{++}^B\right)(p)\right]_{\rm DR,\,1\text{-}loop,\,loc}
=
\mathcal I\!\left[Q_1\big(f_{++}^A f_{++}^B\big)(p)\right]_{\rm DR,\,loc}
$$

$$
\qquad
-\frac{i g^2}{96\pi^2}\,
w^{+\dot\theta}
\int_{p_1,p_2}\delta_{p-p_1-p_2}
\Big[
\Xi_{12,+\dot\theta,+\dot\beta}(p_1,p_2)\,
f^{CE}{}_{A}f^{DE}{}_{B}\,
f_{++}^C(p_1)\widetilde\lambda^{D\dot\beta}(p_2)
$$

$$
\qquad\qquad\qquad\qquad
+
\Xi_{21,+\dot\theta,+\dot\beta}(p_1,p_2)\,
f^{CE}{}_{A}f^{DE}{}_{B}\,
f_{++}^C(p_2)\widetilde\lambda^{D\dot\beta}(p_1)
\Big]
+
O(w^2),
$$

$$
\Xi_{12,+\dot\theta,+\dot\beta}(p_1,p_2)
:=
p_{1,+\dot\theta}p_{1,+\dot\beta}
+
3p_{1,+(\dot\theta}p_{2,+\dot\beta)}
+
3p_{2,+\dot\theta}p_{2,+\dot\beta},
$$

$$
\Xi_{21,+\dot\theta,+\dot\beta}(p_1,p_2)
:=
3p_{1,+\dot\theta}p_{1,+\dot\beta}
+
3p_{1,+(\dot\theta}p_{2,+\dot\beta)}
+
p_{2,+\dot\theta}p_{2,+\dot\beta}.
$$
