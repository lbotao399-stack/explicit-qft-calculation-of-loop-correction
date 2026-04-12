---
title: 'Q_1(O)（f_{++}f_{++}） / DR'
doc_type: calculation
theory: 'N=1 SYM (Euclidean)'
regularization: DR
supercharge: Q_-
loop_order: 1
operator: 'f_{++}f_{++}'
status: canonical
---

## Step 1: Operator set up

$$
\mathcal O_{ff}^{AB}(p):=\int_{p_1,p_2}f_{++}^A(p_1)f_{++}^B(p_2)\,\delta_{p-p_1-p_2},
\qquad
p=p_1+p_2.
$$

## Step 2: Act supercharge Q on O (off-shell)

$$
Q\equiv Q_-,\qquad
Qf_{++}^A=i\nabla_{+\dot\alpha}\widetilde\lambda^{A\dot\alpha}.
$$

$$
Q\mathcal O_{ff}^{AB}(p)
=
\int_{p_1,p_2}\delta_{p-p_1-p_2}
\Big[
\big(i\nabla_{+\dot\alpha}\widetilde\lambda^{A\dot\alpha}\big)(p_1)f_{++}^B(p_2)
+
f_{++}^A(p_1)\big(i\nabla_{+\dot\alpha}\widetilde\lambda^{B\dot\alpha}\big)(p_2)
\Big].
$$

## Step 3: Subtracting tree level Q

$$
Q_0\mathcal O_{ff}^{AB}(p)=0.
$$

$$
Q_1\mathcal O_{ff}^{AB}(p)
=
\int_{p_1,p_2}\delta_{p-p_1-p_2}
\Big[
\big(i\nabla_{+\dot\alpha}\widetilde\lambda^{A\dot\alpha}\big)(p_1)f_{++}^B(p_2)
+
f_{++}^A(p_1)\big(i\nabla_{+\dot\alpha}\widetilde\lambda^{B\dot\alpha}\big)(p_2)
\Big].
$$

## Step 4: All related Feynman Diagrams (Wick contractions) at this order

![](../../assets/step4/calculation_triangles/n1_q1_fpp_fpp_triangle_pair.png)

$$
\mathcal I\!\left[Q_1\mathcal O_{ff}^{AB}\right]_{\rm 1\text{-}loop,\,conn}
=
\mathcal I\!\left[Q_1\mathcal O_{ff}^{AB}\right]^{[A,\widetilde\lambda]}
+
\mathcal I\!\left[Q_1\mathcal O_{ff}^{AB}\right]^{[A,A,\widetilde\lambda]}
+
\mathcal I\!\left[Q_1\mathcal O_{ff}^{AB}\right]^{[A,A,A,\widetilde\lambda]}.
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

$$
N_{\rm top}^{[A,A,\widetilde\lambda]}
=
2\times 10,
\qquad
10=4+2+1+3.
$$

$$
\mathcal C_1=V_{AAA}\big(V_{A\lambda\widetilde\lambda}\big)^2,
\qquad
\mathcal C_2=\big(V_{AAA}\big)^2V_{A\lambda\widetilde\lambda}.
$$

$$
\mathcal C_3=V_{AAAA}V_{A\lambda\widetilde\lambda},
\qquad
\mathcal C_4=\big(V_{A\lambda\widetilde\lambda}\big)^3.
$$

$$
Q_1\mathcal O_{ff}^{AB}(x)\Big|_{\rm DR,\,loc}^{[A,A,\widetilde\lambda]\oplus[A,A,A,\widetilde\lambda]}_{\rm conn}
\stackrel{?}{=}
\frac{g^2}{16\pi^2}\,
i\big(\nabla_{+\dot\beta}-\partial_{+\dot\beta}\big)
\Big(
f^{CE}{}_{A}f^{DE}{}_{B}\,
f_{++}^C\widetilde\lambda^{D\dot\beta}
\Big)(x).
$$

## Step 5: Estimate the Feynman Diagrams

$$
\mathcal I\!\left[Q_1\mathcal O_{ff}^{AB}(p)\right]^{[A,\widetilde\lambda]}
=
\Gamma_{12}^{AB}(p)+\Gamma_{21}^{AB}(p).
$$

$$
\Gamma_{12}^{AB}(p)
=
2g^2
\int_{p_1,p_2}\delta_{p-p_1-p_2}
\int_q^d
D(q)\,D(q-p_2)\,
\Big[-(q+p_1)_{+\dot\alpha}\big(S(q+p_1)P_L\big)_\rho{}^{\dot\alpha}\Big]
(q-p_2)_{+\dot\beta}
$$

$$
\qquad\qquad\times\,
f^{CE}{}_{A}f^{DE}{}_{B}\,
f_{++}^C(p_1)\widetilde\lambda^{D\dot\beta}(p_2).
$$

$$
\Gamma_{21}^{AB}(p)
=
2g^2
\int_{p_1,p_2}\delta_{p-p_1-p_2}
\int_q^d
D(q)\,D(q-p_1)\,
\Big[-(q+p_2)_{+\dot\alpha}\big(S(q+p_2)P_L\big)_\rho{}^{\dot\alpha}\Big]
(q-p_1)_{+\dot\beta}
$$

$$
\qquad\qquad\times\,
f^{CE}{}_{A}f^{DE}{}_{B}\,
f_{++}^C(p_2)\widetilde\lambda^{D\dot\beta}(p_1).
$$

$$
-(q+p_1)_{+\dot\alpha}\big(S(q+p_1)P_L\big)_\rho{}^{\dot\alpha}
=
i\Big(1-\frac{\widehat q^2}{(q+p_1)^2}\Big)\epsilon_{+\rho},
$$

$$
-(q+p_2)_{+\dot\alpha}\big(S(q+p_2)P_L\big)_\rho{}^{\dot\alpha}
=
i\Big(1-\frac{\widehat q^2}{(q+p_2)^2}\Big)\epsilon_{+\rho}.
$$

$$
\Gamma_{12}^{AB}(p)
=
2g^2
\int_{p_1,p_2}\delta_{p-p_1-p_2}
\int_q^d
\frac{(q-p_2)_{+\dot\beta}}{q^2(q-p_2)^2}\,
f^{CE}{}_{A}f^{DE}{}_{B}\,
f_{++}^C(p_1)\widetilde\lambda^{D\dot\beta}(p_2)
$$

$$
\qquad
-2g^2
\int_{p_1,p_2}\delta_{p-p_1-p_2}
\int_q^d
\frac{\widehat q^2\,(q-p_2)_{+\dot\beta}}{q^2(q+p_1)^2(q-p_2)^2}\,
f^{CE}{}_{A}f^{DE}{}_{B}\,
f_{++}^C(p_1)\widetilde\lambda^{D\dot\beta}(p_2).
$$

$$
\Gamma_{21}^{AB}(p)
=
2g^2
\int_{p_1,p_2}\delta_{p-p_1-p_2}
\int_q^d
\frac{(q-p_1)_{+\dot\beta}}{q^2(q-p_1)^2}\,
f^{CE}{}_{A}f^{DE}{}_{B}\,
f_{++}^C(p_2)\widetilde\lambda^{D\dot\beta}(p_1)
$$

$$
\qquad
-2g^2
\int_{p_1,p_2}\delta_{p-p_1-p_2}
\int_q^d
\frac{\widehat q^2\,(q-p_1)_{+\dot\beta}}{q^2(q+p_2)^2(q-p_1)^2}\,
f^{CE}{}_{A}f^{DE}{}_{B}\,
f_{++}^C(p_2)\widetilde\lambda^{D\dot\beta}(p_1).
$$

## Step 6: Do the regularization and Estimate the ultimate result

$$
\frac{1}{q^2(q+p_1)^2(q-p_2)^2}
=
2\int_\Delta
\frac{1}{\big[(q+yp_1-zp_2)^2+\Delta\big]^3},
$$

$$
\Delta=xy\,p_1^2+xz\,p_2^2+yz\,p^2.
$$

$$
\ell=q+yp_1-zp_2.
$$

$$
\Gamma_{12}^{AB}(p)\Big|_{\rm DR,\,loc}
=
-4g^2
\int_{p_1,p_2}\delta_{p-p_1-p_2}
\int_\Delta
\big(yp_1+(x+y)p_2\big)_{+\dot\beta}
$$

$$
\qquad\qquad\times\,
\mu^{2\epsilon}\int\frac{d^d\ell}{(2\pi)^d}
\frac{\widehat\ell^2}{(\ell^2+\Delta)^3}\,
f^{CE}{}_{A}f^{DE}{}_{B}\,
f_{++}^C(p_1)\widetilde\lambda^{D\dot\beta}(p_2)
$$

$$
\qquad
=
-\frac{g^2}{8\pi^2}
\int_{p_1,p_2}\delta_{p-p_1-p_2}
\int_\Delta
\big(yp_1+(x+y)p_2\big)_{+\dot\beta}\,
f^{CE}{}_{A}f^{DE}{}_{B}\,
f_{++}^C(p_1)\widetilde\lambda^{D\dot\beta}(p_2).
$$

$$
\Gamma_{21}^{AB}(p)\Big|_{\rm DR,\,loc}
=
-4g^2
\int_{p_1,p_2}\delta_{p-p_1-p_2}
\int_\Delta
\big((x+y)p_1+yp_2\big)_{+\dot\beta}
$$

$$
\qquad\qquad\times\,
\mu^{2\epsilon}\int\frac{d^d\ell}{(2\pi)^d}
\frac{\widehat\ell^2}{(\ell^2+\Delta)^3}\,
f^{CE}{}_{A}f^{DE}{}_{B}\,
f_{++}^C(p_2)\widetilde\lambda^{D\dot\beta}(p_1)
$$

$$
\qquad
=
-\frac{g^2}{8\pi^2}
\int_{p_1,p_2}\delta_{p-p_1-p_2}
\int_\Delta
\big((x+y)p_1+yp_2\big)_{+\dot\beta}\,
f^{CE}{}_{A}f^{DE}{}_{B}\,
f_{++}^C(p_2)\widetilde\lambda^{D\dot\beta}(p_1).
$$

$$
\int_\Delta\big(yp_1+(x+y)p_2\big)_{+\dot\beta}
=
\frac16(p_1+2p_2)_{+\dot\beta},
\qquad
\int_\Delta\big((x+y)p_1+yp_2\big)_{+\dot\beta}
=
\frac16(2p_1+p_2)_{+\dot\beta}.
$$

$$
\Gamma_{12}^{AB}(p)\Big|_{\rm DR,\,loc}
=
-\frac{g^2}{48\pi^2}
\int_{p_1,p_2}\delta_{p-p_1-p_2}\,
(p_1+2p_2)_{+\dot\beta}\,
f^{CE}{}_{A}f^{DE}{}_{B}\,
f_{++}^C(p_1)\widetilde\lambda^{D\dot\beta}(p_2),
$$

$$
\Gamma_{21}^{AB}(p)\Big|_{\rm DR,\,loc}
=
-\frac{g^2}{48\pi^2}
\int_{p_1,p_2}\delta_{p-p_1-p_2}\,
(2p_1+p_2)_{+\dot\beta}\,
f^{CE}{}_{A}f^{DE}{}_{B}\,
f_{++}^C(p_2)\widetilde\lambda^{D\dot\beta}(p_1).
$$

$$
\mathcal I\!\left[Q_1\mathcal O_{ff}^{AB}(p)\right]_{\rm DR,\,loc}^{[A,\widetilde\lambda]}
=
-\frac{g^2}{48\pi^2}
\int_{p_1,p_2}\delta_{p-p_1-p_2}
\Big[
(p_1+2p_2)_{+\dot\beta}\,
f^{CE}{}_{A}f^{DE}{}_{B}\,
f_{++}^C(p_1)\widetilde\lambda^{D\dot\beta}(p_2)
$$

$$
\qquad\qquad\qquad\qquad
+
(2p_1+p_2)_{+\dot\beta}\,
f^{CE}{}_{A}f^{DE}{}_{B}\,
f_{++}^C(p_2)\widetilde\lambda^{D\dot\beta}(p_1)
\Big].
$$

$$
\mathcal I\!\left[Q_1\mathcal O_{ff}^{AB}(p)\right]_{\rm DR,\,loc}^{[A,\widetilde\lambda]}
=
-\frac{g^2}{16\pi^2}\,
p_{+\dot\beta}
\int_{p_1,p_2}\delta_{p-p_1-p_2}\,
f^{CE}{}_{A}f^{DE}{}_{B}\,
f_{++}^C(p_1)\widetilde\lambda^{D\dot\beta}(p_2).
$$

$$
Q_1\mathcal O_{ff}^{AB}(x)\Big|_{\rm DR,\,loc}^{[A,\widetilde\lambda]}
=
\frac{g^2}{16\pi^2}\,
i\partial_{+\dot\beta}
\Big(
f^{CE}{}_{A}f^{DE}{}_{B}\,
f_{++}^C\widetilde\lambda^{D\dot\beta}
\Big)(x).
$$

$$
(\nabla_{\alpha\dot\alpha}\mathcal O)^{AB}
:=
\partial_{\alpha\dot\alpha}\mathcal O^{AB}
+f^{AC}{}_{D}A_{\alpha\dot\alpha}^C\mathcal O^{DB}
+f^{BC}{}_{D}A_{\alpha\dot\alpha}^C\mathcal O^{AD}.
$$

$$
Q_1\mathcal O_{ff}^{AB}(x)\Big|_{\rm DR,\,loc}^{\rm letter\text{-}conn}
\stackrel{?}{=}
\frac{g^2}{16\pi^2}\,
i\nabla_{+\dot\beta}
\Big(
f^{CE}{}_{A}f^{DE}{}_{B}\,
f_{++}^C\widetilde\lambda^{D\dot\beta}
\Big)(x).
$$

## Step 7: Simplification examples

$$
Q_1\,\operatorname{Tr}(f_{++}f_{++})(p)\Big|_{\rm DR,\,loc}^{[A,\widetilde\lambda]}
=
-\frac{g^2}{16\pi^2}\,
p_{+\dot\beta}
\int_{p_1,p_2}\delta_{p-p_1-p_2}\,
\operatorname{Tr}\big(f_{++}(p_1)\widetilde\lambda^{\dot\beta}(p_2)\big).
$$

$$
Q_1\,\operatorname{Tr}(f_{++}f_{++})(x)\Big|_{\rm DR,\,loc}^{[A,\widetilde\lambda]}
=
\frac{g^2}{16\pi^2}\,
i\partial_{+\dot\beta}\operatorname{Tr}\big(f_{++}\widetilde\lambda^{\dot\beta}\big)(x).
$$

$$
Q_1\,\operatorname{Tr}(f_{++}f_{++})(x)\Big|_{\rm DR,\,loc}^{\rm letter\text{-}conn}
\stackrel{?}{=}
\frac{g^2}{16\pi^2}\,
i\nabla_{+\dot\beta}\operatorname{Tr}\big(f_{++}\widetilde\lambda^{\dot\beta}\big)(x).
$$
