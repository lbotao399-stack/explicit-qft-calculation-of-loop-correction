---
title: 'Q_1(O)（f_{++}e^{w\nabla}f_{++}） / DR'
doc_type: calculation
theory: 'N=4 SYM'
regularization: DR
supercharge: 'Q_-^4'
loop_order: 1
operator: 'f_{++}e^{w\nabla}f_{++}'
status: canonical
source: user_supplied_chat
---

## Step 1: Operator set up

$$
w\cdot\nabla_+:=w^{+\dot\alpha}\nabla_{+\dot\alpha},
\qquad
\mathcal O_w^{AB}(p)
:=
\int_{p_1,p_2}
f_{++}^A(p_1)\,
\big(e^{w\cdot\nabla_+}f_{++}^B\big)(p_2)\,
\delta_{p-p_1-p_2},
$$

$$
p=p_1+p_2,
$$

$$
\mathscr F_{12}^{AB,\dot\beta}(p_1,p_2)
:=
f^{CE}{}_{A}f^{DE}{}_{B}\,
f_{++}^C(p_1)\bar\lambda^{D\dot\beta}(p_2),
\qquad
\mathscr F_{21}^{AB,\dot\beta}(p_1,p_2):=\mathscr F_{12}^{AB,\dot\beta}(p_2,p_1),
$$

$$
\mathscr M_{12}^{AB}(p_1,p_2)
:=
f^{CE}{}_{A}f^{DE}{}_{B}\,
\bar\phi_i^C(p_1)\psi_+^{\,iD}(p_2),
\qquad
\mathscr M_{21}^{AB}(p_1,p_2):=\mathscr M_{12}^{AB}(p_2,p_1).
$$

## Step 2: Act supercharge Q on O (off-shell)

$$
Q\equiv Q_-^4,
\qquad
Qf_{++}=i\nabla_{+\dot\rho}\bar\lambda^{\dot\rho}.
$$

$$
Q\mathcal O_w^{AB}
=
\big(i\nabla_{+\dot\rho}\bar\lambda^{A\dot\rho}\big)e^{\,w\cdot\nabla_+}f_{++}^B
+
f_{++}^A\,e^{\,w\cdot\nabla_+}\big(i\nabla_{+\dot\rho}\bar\lambda^{B\dot\rho}\big).
$$

## Step 3: Subtracting tree level Q

$$
Q_0\mathcal O_w^{AB}=0,
$$

$$
Q_1\mathcal O_w^{AB}
=
\big(i\nabla_{+\dot\rho}\bar\lambda^{A\dot\rho}\big)e^{\,w\cdot\nabla_+}f_{++}^B
+
f_{++}^A\,e^{\,w\cdot\nabla_+}\big(i\nabla_{+\dot\rho}\bar\lambda^{B\dot\rho}\big).
$$

## Step 4: All related Feynman Diagrams (Wick contractions) at this order

![](../../assets/step4/calculation_triangles/n4_q1_fpp_expw_fpp_triangle_families.png)

$$
\mathcal I\!\left[Q_1\mathcal O_w^{AB}(p)\right]_{\rm DR,\,1\text{-}loop,\,loc}
=
\Gamma_g^{AB}(w)+\Gamma_{\psi}^{AB}(w)+\Gamma_{\phi}^{AB}(w).
$$

## Step 5: Estimate the Feynman Diagrams

$$
\Gamma_{12,g}^{AB,{\rm ev}}(w)
=
-2g^2
\int_q^d
e^{\,i w\cdot(p_2-q)}
\frac{\hat q^2\,(q-p_2)_{+\dot\beta}}
{q^2(q+p_1)^2(q-p_2)^2}\,
\mathscr F_{12}^{AB,\dot\beta},
$$

$$
\Gamma_{21,g}^{AB,{\rm ev}}(w)
=
-2g^2
\int_q^d
e^{\,i w\cdot(p_1-q)}
\frac{\hat q^2\,(q-p_1)_{+\dot\beta}}
{q^2(q+p_2)^2(q-p_1)^2}\,
\mathscr F_{21}^{AB,\dot\beta},
$$

$$
\Gamma_{12,\psi}^{AB,{\rm ev}}(w)
=
\sqrt2\,g^2
\int_q^d
e^{\,i w\cdot(p_2-q)}
\frac{\hat q^2\,q_{+\dot\beta}(q-p_2)_+{}^{\dot\beta}}
{q^2(q+p_1)^2(q-p_2)^2}\,
\mathscr M_{12}^{AB},
$$

$$
\Gamma_{21,\psi}^{AB,{\rm ev}}(w)
:=
\Gamma_{12,\psi}^{AB,{\rm ev}}(w;p_2,p_1)\Big|_{\mathscr M_{12}^{AB}(p_2,p_1)\to\mathscr M_{21}^{AB}(p_1,p_2)},
$$

$$
\Gamma_{12,\phi}^{AB,{\rm ev}}(w)
=
-\sqrt2\,g^2
\int_q^d
e^{\,i w\cdot(p_1-q)}
\frac{\hat q^2\,(p_1-q)_{+\dot\beta}(p_1+q)_+{}^{\dot\beta}}
{q^2(q+p_2)^2(q-p_1)^2}\,
\mathscr M_{12}^{AB},
$$

$$
\Gamma_{21,\phi}^{AB,{\rm ev}}(w)
:=
\Gamma_{12,\phi}^{AB,{\rm ev}}(w;p_2,p_1)\Big|_{\mathscr M_{12}^{AB}(p_2,p_1)\to\mathscr M_{21}^{AB}(p_1,p_2)}.
$$

## Step 6: Do the regularization and Estimate the ultimate result

$$
\mathcal G_{12,+\dot\beta}(w)
:=
\int_\Delta e^{\,i w\cdot\big(y p_1+(x+y)p_2\big)}\,
\big(y p_1+(x+y)p_2\big)_{+\dot\beta},
\qquad
\mathcal G_{21,+\dot\beta}(w)
:=
\int_\Delta e^{\,i w\cdot\big((x+y)p_1+y p_2\big)}\,
\big((x+y)p_1+y p_2\big)_{+\dot\beta},
$$

$$
\mathcal H_{12}(w)
:=
\int_\Delta y\Big(
e^{\,i w\cdot\big(y p_1+(x+y)p_2\big)}
+
2e^{\,i w\cdot\big((x+y)p_1+y p_2\big)}
\Big),
$$

$$
\mathcal H_{21}(w)
:=
\int_\Delta y\Big(
2e^{\,i w\cdot\big(y p_1+(x+y)p_2\big)}
+
e^{\,i w\cdot\big((x+y)p_1+y p_2\big)}
\Big),
$$

$$
\boxed{
\mathcal I\!\left[
Q_1\big(f_{++}^A e^{\,w\cdot\nabla_+}f_{++}^B\big)(p)
\right]_{\rm DR,\,1\text{-}loop,\,loc}
=
-\frac{g^2}{8\pi^2}
\int_{p_1,p_2}\delta_{p-p_1-p_2}
\Big[
\mathcal G_{12,+\dot\beta}(w)\,\mathscr F_{12}^{AB,\dot\beta}
+
\mathcal G_{21,+\dot\beta}(w)\,\mathscr F_{21}^{AB,\dot\beta}
\Big]
}
$$

$$
\boxed{
\qquad\qquad
-\frac{\sqrt2\,g^2}{16\pi^2}
\int_{p_1,p_2}\delta_{p-p_1-p_2}
\Big[
\mathcal H_{12}(w)\,p_{+\dot\beta}p_{2,+}{}^{\dot\beta}\,\mathscr M_{12}^{AB}
+
\mathcal H_{21}(w)\,p_{+\dot\beta}p_{1,+}{}^{\dot\beta}\,\mathscr M_{21}^{AB}
\Big].
}
$$

## Step 7: Simplification examples

$$
\mathcal G_{12,+\dot\beta}(0)=\frac16(p_1+2p_2)_{+\dot\beta},
\qquad
\mathcal G_{21,+\dot\beta}(0)=\frac16(2p_1+p_2)_{+\dot\beta},
$$

$$
\mathcal H_{12}(0)=\mathcal H_{21}(0)=\frac12,
$$

$$
\boxed{
Q_1\big(f_{++}^A f_{++}^B\big)(x)\Big|_{\rm DR,\,loc}
=
\frac{g^2}{16\pi^2}\,
f^{CE}{}_{A}f^{DE}{}_{B}
\Big[
i\nabla_{+\dot\beta}\big(f_{++}^C\bar\lambda^{D\dot\beta}\big)
+
\sqrt2\,\nabla_{+\dot\beta}\big(\bar\phi_i^C\nabla_+^{\dot\beta}\psi_+^{\,iD}\big)
\Big](x).
}
$$

$$
M^2 \longleftrightarrow \hat q^2,
\qquad
\frac{1}{32\pi^2}\longleftrightarrow -I_{\hat2}^{\rm loc}.
$$
