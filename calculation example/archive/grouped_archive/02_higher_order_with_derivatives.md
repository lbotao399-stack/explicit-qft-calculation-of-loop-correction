# Higher order( with derivatives)

<aside>

## $Q_1(f_{++}f_{++})$

![image.png](../source_archive/%E7%9B%B4%E6%8E%A51-loop%20level%E8%AE%A1%E7%AE%97/image%201.png)

### **Setup**

沿用当前页的 propagators、$V_{A\lambda\bar\lambda}=V_L-V_R$、matrix-index / double-line conventions，以及上一页已经算完的 PV master integral。

取

$$
\mathcal O(x):=i\nabla_{+\dot\alpha}\bar\lambda^{\dot\alpha}(x),\qquad f_{++}(x).
$$

抽出决定 universal 1-loop coefficient 的 two-field triangle piece：

$$
																														\mathcal O^{(\partial\partial)}(x)=i\partial_{+\dot\alpha}\bar\lambda^{\dot\alpha}(x),\qquad
f_{++}^{(\partial)}(x)=i\partial_{+\dot\gamma}A_{+}{}^{\dot\gamma}(x).
$$

其余带显式 $g$ 的 pieces 只做 covariant completion，不改这个 triangle 的 PV coefficient。

### **Color-flow tensor**

定义 mixed tensor

$$
																														\mathscr F_{12}^{\dot\beta}
=\mathscr F_{12}^{(LL)\dot\beta}+\mathscr F_{12}^{(LR)\dot\beta}+\mathscr F_{12}^{(RL)\dot\beta}+\mathscr F_{12}^{(RR)\dot\beta},
$$

其中

$$
																														\mathscr F_{12}^{(LL)\dot\beta}{}^i{}_j{}^k{}_l
=\Pi^{mn}{}_{jl}\,f_{++}{}^i{}_m(p_1)\,\bar\lambda^{\dot\beta}{}^k{}_n(p_2),
$$

$$
																														\mathscr F_{12}^{(LR)\dot\beta}{}^i{}_j{}^k{}_l
=-\Pi^{mk}{}_{jn}\,f_{++}{}^i{}_m(p_1)\,\bar\lambda^{\dot\beta}{}^n{}_l(p_2),
$$

$$
																														\mathscr F_{12}^{(RL)\dot\beta}{}^i{}_j{}^k{}_l
=-\Pi^{in}{}_{ml}\,f_{++}{}^m{}_j(p_1)\,\bar\lambda^{\dot\beta}{}^k{}_n(p_2),
$$

$$
																														\mathscr F_{12}^{(RR)\dot\beta}{}^i{}_j{}^k{}_l
=\Pi^{ik}{}_{mn}\,f_{++}{}^m{}_j(p_1)\,\bar\lambda^{\dot\beta}{}^n{}_l(p_2).
$$

在 $U(N)$ 下

$$
																														\mathscr F_{12}^{\dot\beta}{}^i{}_j{}^k{}_l
=f_{++}{}^i{}_l(p_1)\bar\lambda^{\dot\beta}{}^k{}_j(p_2)
-\delta^k{}_j f_{++}{}^i{}_m(p_1)\bar\lambda^{\dot\beta}{}^m{}_l(p_2)
-\delta^i{}_l f_{++}{}^m{}_j(p_1)\bar\lambda^{\dot\beta}{}^k{}_m(p_2)
+f_{++}{}^k{}_j(p_1)\bar\lambda^{\dot\beta}{}^i{}_l(p_2).
$$

并取

$$
\mathscr F_{21}^{\dot\beta}(p_1,p_2)=\mathscr F_{12}^{\dot\beta}(p_2,p_1).
$$

### **Pattern 12**

routing 取成和图一致：

$$
u_1=q,\qquad v_1=p_1,\qquad w_1=-(q+p_1),
$$

$$
u_2=p_2,\qquad v_2=q-p_2,\qquad w_2=-q,
$$

$$
r=q+p_1,\qquad s=p-r=p_2-q,\qquad p=p_1+p_2.
$$

PV propagators：

$$
																														\langle \Lambda_\alpha(p)\bar\Lambda_{\dot\beta}(-p)\rangle_{\rm PV}
=-\frac{i\,p_{\alpha\dot\beta}}{p^2+M^2},\qquad
\langle B_{\alpha\dot\alpha}(p)B_{\beta\dot\beta}(-p)\rangle_{\rm PV}
=\frac{2\epsilon_{\alpha\beta}\epsilon_{\dot\alpha\dot\beta}}{p^2+M^2}.
$$

massive collapse identity：

$$
																														-k_{+\dot\alpha}\big(S_M(k)P_L\big)_\alpha{}^{\dot\alpha}
=i\epsilon_{+\alpha}-i\frac{M^2}{k^2+M^2}\epsilon_{+\alpha}.
$$

因此 12 图的 PV loop 直接写成

$$
																														\Gamma_{12;M}^{\rm PV\text{-}loop}{}^i{}_j{}^k{}_l
=2g^2\int_q\frac{(q-p_2)_{+\dot\beta}}{(q^2+M^2)\big((q-p_2)^2+M^2\big)}\,\mathscr F_{12}^{\dot\beta}{}^i{}_j{}^k{}_l
$$

$$
																														\qquad
-2g^2M^2\int_q
\frac{(q-p_2)_{+\dot\beta}}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}\,\mathscr F_{12}^{\dot\beta}{}^i{}_j{}^k{}_l.
$$

前一项是 contact/EOM sector，后一项是 anomaly sector。

### **Feynman parameter**

$$
																													\frac{1}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}
=2\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
\frac{1}{\big[(q+yp_1-zp_2)^2+M^2+\Delta\big]^3},
$$

$$
\Delta=xy\,p_1^2+xz\,p_2^2+yz\,p^2.
$$

令

$$
\ell=q+yp_1-zp_2,\qquad q-p_2=\ell-yp-xp_2.
$$

则 odd part 消失：

$$
																													\Gamma_{12;M}^{(\rm anom)}
=-4g^2M^2\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
(yp+xp_2)_{+\dot\beta}\int_\ell\frac{1}{(\ell^2+M^2+\Delta)^3}\,\mathscr F_{12}^{\dot\beta}.
$$

再用

$$
\int_\ell\frac{1}{(\ell^2+\Omega)^3}=\frac{1}{32\pi^2}\frac{1}{\Omega},
$$

得 local part

$$
																													\Gamma_{12;M}^{(\rm anom,loc)}
=-\frac{g^2}{8\pi^2}
\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
\frac{M^2}{M^2+\Delta}\,(yp+xp_2)_{+\dot\beta}\,\mathscr F_{12}^{\dot\beta}.
$$

取 $M\to\infty$ 的 local part，并用 simplex integrals

$$
																													\int dx\,dy\,dz\,\delta(1-x-y-z)
\,x=\int dx\,dy\,dz\,\delta(1-x-y-z)\,y=\frac16,
$$

得到

$$
																													\boxed{\Gamma_{12}^{(\rm anom,loc)}{}^i{}_j{}^k{}_l
=-\frac{g^2}{48\pi^2}(p_1+2p_2)_{+\dot\beta}\,\mathscr F_{12}^{\dot\beta}{}^i{}_j{}^k{}_l}.
$$

### **Pattern 21**

完全平行：

$$
																													\boxed{\Gamma_{21}^{(\rm anom,loc)}{}^i{}_j{}^k{}_l
=-\frac{g^2}{48\pi^2}(2p_1+p_2)_{+\dot\beta}\,\mathscr F_{21}^{\dot\beta}{}^i{}_j{}^k{}_l}.
$$

### **Open-index final result**

$$
																														\boxed{\mathcal I\!\left[Q_1\big(f_{++}f_{++}\big){}^i{}_j{}^k{}_l(p)\right]
=-\frac{g^2}{48\pi^2}
\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)
\Big[(p_1+2p_2)_{+\dot\beta}\,\mathscr F_{12}^{\dot\beta}{}^i{}_j{}^k{}_l
+(2p_1+p_2)_{+\dot\beta}\,\mathscr F_{21}^{\dot\beta}{}^i{}_j{}^k{}_l\Big]}.
$$

### **Single-trace simplification**

若真正要的是 gauge-invariant $operatorname{Tr}(f_{++}f_{++})$，则 cyclicity 给出

$$
																														\Gamma_{12}^{(\rm anom,loc)}+\Gamma_{21}^{(\rm anom,loc)}
=-\frac{g^2}{16\pi^2}
p_{+\dot\beta}\operatorname{Tr}\big(f_{++}(p_1)\bar\lambda^{\dot\beta}(p_2)\big).
$$

所以

$$
																														\boxed{\mathcal I\!\left[Q_1,\operatorname{Tr}(f_{++}f_{++})(p)\right]
=-\frac{g^2}{16\pi^2}
p_{+\dot\beta}\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)
\operatorname{Tr}\big(f_{++}(p_1)\bar\lambda^{\dot\beta}(p_2)\big)}.
$$

position space：

$$
																														\boxed{Q_1,\operatorname{Tr}(f_{++}f_{++})(x)
=\frac{g^2}{16\pi^2}\,i\partial_{+\dot\beta}\operatorname{Tr}\big(f_{++}\bar\lambda^{\dot\beta}\big)(x)}.
$$

在 1-loop order 写成 covariantized form 也成立：

$$
																														Q_1,\operatorname{Tr}(f_{++}f_{++})(x)
=\frac{g^2}{16\pi^2}\,i\nabla_{+\dot\beta}\operatorname{Tr}\big(f_{++}\bar\lambda^{\dot\beta}\big)(x),
$$

因为 $\partial\to\nabla$ 的差别从更高阶开始。

### Lie-algebra-index rewrite of the open-index final result

$$
[T^A,T^B]=f^{AB}{}_C\,T^C,\qquad \operatorname{Tr}(T^AT^B)=\delta^{AB}.
$$

$$
																		(f_{++}f_{++}){}^i{}_j{}^k{}_l=(T^A)^i{}_j(T^B)^k{}_l\,\mathcal O_{ff}^{AB},
\qquad
\mathcal O_{ff}^{AB}:=f_{++}^A f_{++}^B.
$$

$$
																		\mathscr F_{12}^{\dot\beta}{}^i{}_j{}^k{}_l=(T^A)^i{}_j(T^B)^k{}_l\,\mathscr F_{12}^{AB,\dot\beta},
\qquad
\mathscr F_{21}^{\dot\beta}{}^i{}_j{}^k{}_l=(T^A)^i{}_j(T^B)^k{}_l\,\mathscr F_{21}^{AB,\dot\beta}.
$$

$$
																		\mathscr F_{12}^{AB,\dot\beta}
=f^{CE}{}_A f^{DE}{}_B\,f_{++}^C(p_1)\bar\lambda^{\dot\beta D}(p_2),
\qquad
\mathscr F_{21}^{AB,\dot\beta}
=f^{CE}{}_A f^{DE}{}_B\,f_{++}^C(p_2)\bar\lambda^{\dot\beta D}(p_1).
$$

$$
																		\boxed{\mathcal I\!\left[Q_1\mathcal O_{ff}^{AB}(p)\right]
=-\frac{g^2}{48\pi^2}
\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)
\Big[(p_1+2p_2)_{+\dot\beta}\,\mathscr F_{12}^{AB,\dot\beta}
+(2p_1+p_2)_{+\dot\beta}\,\mathscr F_{21}^{AB,\dot\beta}\Big]}.
$$

$$
																		=-\frac{g^2}{16\pi^2}\,p_{+\dot\beta}
\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)
\,f^{CE}{}_A f^{DE}{}_B\,f_{++}^C(p_1)\bar\lambda^{\dot\beta D}(p_2).
$$

$$
\mathcal O_{f\bar\lambda}^{AB,\dot\beta}(x):=f^{CE}{}_A f^{DE}{}_B\,f_{++}^C(x)\bar\lambda^{\dot\beta D}(x).
$$

$$
Q_1\mathcal O_{ff}^{AB}(x)=\frac{g^2}{16\pi^2}\,i\partial_{+\dot\beta}\mathcal O_{f\bar\lambda}^{AB,\dot\beta}(x).
$$

$$
																		(\nabla_{\alpha\dot\alpha}\mathcal O)^{AB}
:=\partial_{\alpha\dot\alpha}\mathcal O^{AB}
+f^{AC}{}_D A_{\alpha\dot\alpha}^C\mathcal O^{DB}
+f^{BC}{}_D A_{\alpha\dot\alpha}^C\mathcal O^{AD}.
$$

$$
																		\boxed{
Q_1\mathcal O_{ff}^{AB}(x)
=\frac{g^2}{16\pi^2}\,i\nabla_{+\dot\beta}\mathcal O_{f\bar\lambda}^{AB,\dot\beta}(x)
}.
$$

</aside>

<aside>

### $Q_1(f_{++}\nabla_{+\dot\gamma}\bar\lambda_{\dot\alpha})$

![image.png](../source_archive/%E7%9B%B4%E6%8E%A51-loop%20level%E8%AE%A1%E7%AE%97/image%202.png)

### **Setup**

沿用前页全部 conventions：propagators、$(V_{Alambdabarlambda}=V_L-V_R)$、matrix-index / double-line、同一个 $(mathscr C_{12},mathscr C_{21})$，以及 PV collapse identity。

取

$$
\mathcal O_{\dot\theta\dot\beta}{}^i{}_j{}^k{}_l(x):=i\nabla_{+\dot\alpha}\bar\lambda^{\dot\alpha}{}^i{}_j(x),\nabla_{+\dot\theta}\bar\lambda_{\dot\beta}{}^k{}_l(x).
$$

抽出决定 universal 1-loop coefficient 的 two-field triangle piece：

$$
														\mathcal O_{\dot\theta\dot\beta}^{(\partial\partial)}{}^i{}_j{}^k{}_l
:= i\partial_{+\dot\alpha}\bar\lambda^{\dot\alpha}{}^i{}_j\, i\partial_{+\dot\theta}\bar\lambda_{\dot\beta}{}^k{}_l.
$$

其余显式 $g$ 的 $(partial A)$、$(Apartial)$、$(AA)$ pieces 只做 covariant completion，不改 triangle 的 PV coefficient。anomaly 仍只来自 triangle pair。

动量空间 insertion：

$$
														\mathcal I\!\left[\mathcal O_{\dot\theta\dot\beta}^{(\partial\partial)}(p)\right]
=
\int_{r,s}(2\pi)^4\delta^{(4)}(p-r-s)
(-r_{+\dot\alpha})(i s_{+\dot\theta})
\bar\lambda^{\dot\alpha}(r)\bar\lambda_{\dot\beta}(s).
$$

color tensor 直接沿用前页：

$$
														\mathscr C_{21}{}^i{}_j{}^k{}_l(p_1,p_2),
\qquad
\mathscr C_{12}{}^i{}_j{}^k{}_l(p_2,p_1).
$$

### Pattern 12

routing 取

$$
r=q+p_1,\qquad s=p_2-q,\qquad p=p_1+p_2.
$$

PV propagators：

$$
														\langle \Lambda_\alpha(p)\bar\Lambda_{\dot\beta}(-p)\rangle_{\rm PV}
=-\frac{i p_{\alpha\dot\beta}}{p^2+M^2},
\qquad
\langle B_{\alpha\dot\alpha}(p)B_{\beta\dot\beta}(-p)\rangle_{\rm PV}
=\frac{2\epsilon_{\alpha\beta}\epsilon_{\dot\alpha\dot\beta}}{p^2+M^2}.
$$

写成

$$
\big(S_M(k)P_L\big)_{\alpha\dot\alpha}=-\frac{i k_{\alpha\dot\alpha}}{k^2+M^2}.
$$

于是

$$
														-r_{+\dot\alpha}\big(S_M(r)P_L\big)_\alpha{}^{\dot\alpha}
=i\epsilon_{+\alpha}
-i\frac{M^2}{r^2+M^2}\epsilon_{+\alpha},
$$

$$
														i s_{+\dot\theta}\big(S_M(s)P_L\big)_{\rho\dot\beta}
=\frac{s_{+\dot\theta}s_{\rho\dot\beta}}{s^2+M^2}.
$$

故 12 图的 PV loop 为

$$
														\Gamma_{12;M}^{\rm PV\text{-}loop}{}_{\dot\theta\dot\beta}{}^i{}_j{}^k{}_l
=2i g^2\int_q
\frac{(q-p_2)_{+\dot\theta}(q-p_2)_{+\dot\beta}}{(q^2+M^2)\big((q-p_2)^2+M^2\big)}\,\mathscr C_{12}{}^i{}_j{}^k{}_l
$$

$$
														\qquad
-2i g^2M^2\int_q
\frac{(q-p_2)_{+\dot\theta}(q-p_2)_{+\dot\beta}}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}\,\mathscr C_{12}{}^i{}_j{}^k{}_l.
$$

前一项是 contact/EOM sector，后一项是 anomaly sector：

$$
														\Gamma_{12;M}^{(\rm anom)}{}_{\dot\theta\dot\beta}
=-2i g^2M^2\int_q
\frac{(q-p_2)_{+\dot\theta}(q-p_2)_{+\dot\beta}}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}\,\mathscr C_{12}.
$$

Feynman parameter：

$$
														\frac{1}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}
=2\int_0^1 dx\,dy\,dz\,\delta(1-x-y-z)
\frac{1}{\big[(q+yp_1-zp_2)^2+M^2+\Delta\big]^3},
$$

$$
\Delta=xy\,p_1^2+xz\,p_2^2+yz\,p^2.
$$

令

$$
\ell=q+yp_1-zp_2,\qquad q-p_2=\ell-yp-xp_2.
$$

则

$$
														\Gamma_{12;M}^{(\rm anom)}
=-4i g^2M^2\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
\int_\ell
\frac{(\ell-yp-xp_2)_{+\dot\theta}(\ell-yp-xp_2)_{+\dot\beta}}{(\ell^2+M^2+\Delta)^3}\,\mathscr C_{12}.
$$

只剩 shift piece：

$$
														\Gamma_{12;M}^{(\rm anom)}
=-4i g^2M^2\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
(yp+xp_2)_{+\dot\theta}(yp+xp_2)_{+\dot\beta}
\int_\ell\frac{1}{(\ell^2+M^2+\Delta)^3}\,\mathscr C_{12}.
$$

再用

$$
\int_\ell\frac{1}{(\ell^2+\Omega)^3}=\frac{1}{32\pi^2}\frac{1}{\Omega},
$$

得

$$
														\Gamma_{12;M}^{(\rm anom)}
=-\frac{i g^2}{8\pi^2}
\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
\frac{M^2}{M^2+\Delta}
(yp+xp_2)_{+\dot\theta}(yp+xp_2)_{+\dot\beta}\,\mathscr C_{12}.
$$

取 local part：

$$
														\Gamma_{12}^{(\rm anom,loc)}{}_{\dot\theta\dot\beta}
=-\frac{i g^2}{8\pi^2}
\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
(yp+xp_2)_{+\dot\theta}(yp+xp_2)_{+\dot\beta}\,\mathscr C_{12}.
$$

simplex 积分：

$$
														\int y^2=\frac{1}{12},\qquad
\int y(x+y)=\frac{1}{8},\qquad
\int (x+y)^2=\frac{1}{4}.
$$

于是

$$
														\boxed{
\Gamma_{12}^{(\rm anom,loc)}{}_{\dot\theta\dot\beta}{}^i{}_j{}^k{}_l
=-\frac{i g^2}{96\pi^2}
\Big[
 p_{1,+\dot\theta}p_{1,+\dot\beta}
+3p_{1,+ (\dot\theta}p_{2,+\dot\beta)}
+3p_{2,+\dot\theta}p_{2,+\dot\beta}
\Big]
\mathscr C_{12}{}^i{}_j{}^k{}_l
}.
$$

### Pattern 21

完全平行：

$$
														\boxed{
\Gamma_{21}^{(\rm anom,loc)}{}_{\dot\theta\dot\beta}{}^i{}_j{}^k{}_l
=-\frac{i g^2}{96\pi^2}
\Big[
3p_{1,+\dot\theta}p_{1,+\dot\beta}
+3p_{1,+ (\dot\theta}p_{2,+\dot\beta)}
+p_{2,+\dot\theta}p_{2,+\dot\beta}
\Big]
\mathscr C_{21}{}^i{}_j{}^k{}_l
}.
$$

### Open-index final result

定义

$$
														\Xi_{12,+\dot\theta,+\dot\beta}(p_1,p_2)
:=
 p_{1,+\dot\theta}p_{1,+\dot\beta}
+3p_{1,+ (\dot\theta}p_{2,+\dot\beta)}
+3p_{2,+\dot\theta}p_{2,+\dot\beta},
$$

$$
														\Xi_{21,+\dot\theta,+\dot\beta}(p_1,p_2)
:=
3p_{1,+\dot\theta}p_{1,+\dot\beta}
+3p_{1,+ (\dot\theta}p_{2,+\dot\beta)}
+p_{2,+\dot\theta}p_{2,+\dot\beta}.
$$

则严格的 open-index 1-loop local anomaly 为

$$
														\boxed{
\mathcal I\!\left[
\big(i\nabla_{+\dot\alpha}\bar\lambda^{\dot\alpha},\nabla_{+\dot\theta}\bar\lambda_{\dot\beta}\big)^{(1),\rm loc}{}^i{}_j{}^k{}_l(p)
\right]
=-\frac{i g^2}{96\pi^2}
\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)
\Big[
\Xi_{12,+\dot\theta,+\dot\beta}\,\mathscr C_{12}{}^i{}_j{}^k{}_l
+\Xi_{21,+\dot\theta,+\dot\beta}\,\mathscr C_{21}{}^i{}_j{}^k{}_l
\Big]
}.
$$

并且

$$
														\Gamma_{\dot\theta\dot\beta}^{(\rm anom,loc)}
=\Gamma_{(\dot\theta\dot\beta)}^{(\rm anom,loc)},
$$

即只有 symmetric dotted part survives。

Position-space / covariantized form：

$$
\partial\rightarrow \nabla
$$

在 1-loop order 可直接做 covariantization，因为差别从更高阶开始。

<aside>
💡

### Lie-algebra-index / local-operator rewrite

定义

$$
												\mathcal O_{\dot\theta\dot\beta}^{AB}(x):=
i\nabla_{+\dot\alpha}\bar\lambda^{\dot\alpha A}(x)\,
\nabla_{+\dot\theta}\bar\lambda_{\dot\beta}^{B}(x).
$$

$$
[T^A,T^B]=f^{AB}{}_C\,T^C,\qquad \operatorname{Tr}(T^AT^B)=\delta^{AB}.
$$

$$
												\mathcal O_{\dot\theta\dot\beta}{}^i{}_j{}^k{}_l
=(T^A)^i{}_j(T^B)^k{}_l\,\mathcal O_{\dot\theta\dot\beta}^{AB}.
$$

则

$$
												\mathscr C_{12}{}^i{}_j{}^k{}_l
=(T^A)^i{}_j(T^B)^k{}_l\,\mathscr C_{12}^{AB},
\qquad
\mathscr C_{21}{}^i{}_j{}^k{}_l
=(T^A)^i{}_j(T^B)^k{}_l\,\mathscr C_{21}^{AB},
$$

$$
												\mathscr C_{12}^{AB}(p_1,p_2)
=
\epsilon^{\dot\gamma\dot\delta}
f^{CA}{}_E f^{DB}{}_E\,
\bar\lambda_{\dot\gamma}^{C}(p_1)\bar\lambda_{\dot\delta}^{D}(p_2),
\qquad
\mathscr C_{21}^{AB}(p_1,p_2)=\mathscr C_{12}^{AB}(p_2,p_1).
$$

于是 momentum-space 写成

$$
												\boxed{
\mathcal I\!\left[
\mathcal O_{\dot\theta\dot\beta}^{AB\,(1),\rm loc}(p)
\right]
=
-\frac{i g^2}{96\pi^2}
\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)
\Big[
\Xi_{12,+\dot\theta,+\dot\beta}\,\mathscr C_{12}^{AB}
+
\Xi_{21,+\dot\theta,+\dot\beta}\,\mathscr C_{21}^{AB}
\Big]
}.
$$

合并 $\mathscr C_{21}^{AB}(p_1,p_2)=\mathscr C_{12}^{AB}(p_2,p_1)$ 后，

$$
												\boxed{
\mathcal I\!\left[
\mathcal O_{\dot\theta\dot\beta}^{AB\,(1),\rm loc}(p)
\right]
=
-\frac{i g^2}{48\pi^2}
\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)\,
\Xi_{12,+\dot\theta,+\dot\beta}(p_1,p_2)\,
\epsilon^{\dot\gamma\dot\delta}
f^{CA}{}_E f^{DB}{}_E\,
\bar\lambda_{\dot\gamma}^{C}(p_1)\bar\lambda_{\dot\delta}^{D}(p_2)
}.
$$

记

$$
												\mathcal B_{\dot\theta\dot\beta}^{AB}(x):=
\epsilon^{\dot\gamma\dot\delta}
f^{CA}{}_E f^{DB}{}_E
\Big[
(\nabla_{+(\dot\theta}\nabla_{+\dot\beta)}\bar\lambda_{\dot\gamma}^{C})\bar\lambda_{\dot\delta}^{D}
+3(\nabla_{+(\dot\theta}\bar\lambda_{\dot\gamma}^{C})(\nabla_{+\dot\beta)}\bar\lambda_{\dot\delta}^{D})
+3\bar\lambda_{\dot\gamma}^{C}(\nabla_{+(\dot\theta}\nabla_{+\dot\beta)}\bar\lambda_{\dot\delta}^{D})
\Big].
$$

则 local operator 形式为

$$
												\boxed{
\mathcal O_{\dot\theta\dot\beta}^{AB\,(1),\rm loc}(x)
=
\frac{i g^2}{48\pi^2}\,
\mathcal B_{\dot\theta\dot\beta}^{AB}(x)
},
\qquad
\mathcal O_{\dot\theta\dot\beta}^{AB\,(1),\rm loc}
=
\mathcal O_{(\dot\theta\dot\beta)}^{AB\,(1),\rm loc}.
$$

</aside>

</aside>

<aside>

## $Q_1((\nabla_{+\dot\alpha} f_{++}) f_{++})$

### Setup

沿用同页 conventions：

$$
															Q_- f_{++}= i\nabla_{+\dot\alpha}\bar\lambda^{\dot\alpha},\qquad
Q_-A_{+\dot\theta}= i\bar\lambda_{\dot\theta},\qquad
[Q_-,\nabla_{+\dot\theta}]X=i[\bar\lambda_{\dot\theta},X].
$$

$$
															\mathcal I[\partial_{+\dot\theta}f_{++}(p)]
= i\,p_{+\dot\theta}\,\mathcal I[f_{++}(p)],\qquad
V_{A\lambda\bar\lambda}=V_L-V_R.
$$

PV propagators：

$$
															\langle \Lambda_\alpha(p)\bar\Lambda_{\dot\beta}(-p)\rangle_{\rm PV}
=-\frac{i\,p_{\alpha\dot\beta}}{p^2+M^2},\qquad
\langle B_{\alpha\dot\alpha}(p)B_{\beta\dot\beta}(-p)\rangle_{\rm PV}
=\frac{2\epsilon_{\alpha\beta}\epsilon_{\dot\alpha\dot\beta}}{p^2+M^2}.
$$

并且继续用前页 mixed color tensor $(mathscr F_{12}^{dotbeta},mathscr F_{21}^{dotbeta})$。

定义

$$
\mathcal O_{f\nabla f,\dot\theta}{}^i{}_j{}^k{}_l(x):=f_{++}{}^i{}_j(x)\,\nabla_{+\dot\theta}f_{++}{}^k{}_l(x).
$$

严格写

$$
															Q_-\mathcal O_{f\nabla f,\dot\theta}
=
\underbrace{\big(i\nabla_{+\dot\alpha}\bar\lambda^{\dot\alpha}\big)\,\nabla_{+\dot\theta}f_{++}}_{\text{loop-focus 1}}
+
\underbrace{f_{++}\,\nabla_{+\dot\theta}\big(i\nabla_{+\dot\alpha}\bar\lambda^{\dot\alpha}\big)}_{\text{loop-focus 2}}
+
\underbrace{i\,f_{++}\,[\bar\lambda_{\dot\theta},f_{++}]}_{\text{tree level}}.
$$

下面只算 loop-focus；最后一项不进 1-loop anomaly。

### Ordered pair 先算

定义

$$
															\mathcal O_{\dot\theta}^{\rm mix}{}^i{}_j{}^k{}_l(x):=
i\nabla_{+\dot\alpha}\bar\lambda^{\dot\alpha}{}^i{}_j(x)\,\nabla_{+\dot\theta}f_{++}{}^k{}_l(x).
$$

取决定 universal coefficient 的 two-field triangle piece：

$$
															\mathcal O_{\dot\theta}^{(\partial\partial)}{}^i{}_j{}^k{}_l
:=i\partial_{+\dot\alpha}\bar\lambda^{\dot\alpha}{}^i{}_j\;i\partial_{+\dot\theta}f_{++}^{(\partial)}{}^k{}_l.
$$

动量空间 insertion：

$$
															\mathcal I\!\left[\mathcal O_{\dot\theta}^{(\partial\partial)}(p)\right]
=
\int_{r,s}(2\pi)^4\delta^{(4)}(p-r-s)
(-r_{+\dot\alpha})(i s_{+\dot\theta})
\bar\lambda^{\dot\alpha}(r)\,\mathcal I[f_{++}(s)].
$$

同前页定义

$$
															\mathscr F_{12}^{\dot\beta}
=
\mathscr F_{12}^{(LL)\dot\beta}
+\mathscr F_{12}^{(LR)\dot\beta}
+\mathscr F_{12}^{(RL)\dot\beta}
+\mathscr F_{12}^{(RR)\dot\beta},
\qquad
\mathscr F_{21}^{\dot\beta}(p_1,p_2)=\mathscr F_{12}^{\dot\beta}(p_2,p_1).
$$

其中

$$
															\mathscr F_{12}^{(LL)\dot\beta}{}^i{}_j{}^k{}_l
=\Pi^{mn}{}_{jl}\,f_{++}{}^i{}_m(p_1)\,\bar\lambda^{\dot\beta}{}^k{}_n(p_2),
$$

$$
															\mathscr F_{12}^{(LR)\dot\beta}{}^i{}_j{}^k{}_l
=-\Pi^{mk}{}_{jn}\,f_{++}{}^i{}_m(p_1)\,\bar\lambda^{\dot\beta}{}^n{}_l(p_2),
$$

$$
															\mathscr F_{12}^{(RL)\dot\beta}{}^i{}_j{}^k{}_l
=-\Pi^{in}{}_{ml}\,f_{++}{}^m{}_j(p_1)\,\bar\lambda^{\dot\beta}{}^k{}_n(p_2),
$$

$$
															\mathscr F_{12}^{(RR)\dot\beta}{}^i{}_j{}^k{}_l
=\Pi^{ik}{}_{mn}\,f_{++}{}^m{}_j(p_1)\,\bar\lambda^{\dot\beta}{}^n{}_l(p_2).
$$

### Pattern 12

routing 取

$$
r=q+p_1,\qquad s=p_2-q,\qquad p=p_1+p_2.
$$

写

$$
\big(S_M(k)P_L\big)_{\alpha\dot\alpha}=-\frac{i\,k_{\alpha\dot\alpha}}{k^2+M^2}.
$$

则

$$
															-r_{+\dot\alpha}\big(S_M(r)P_L\big)_\alpha{}^{\dot\alpha}
=
i\epsilon_{+\alpha}-i\frac{M^2}{r^2+M^2}\epsilon_{+\alpha}.
$$

又

$$
															\langle f_{++}(s)\,B_{-\dot\beta}(-s)\rangle_{\rm PV}
=-\frac{i\,s_{+\dot\beta}}{s^2+M^2},
$$

故

$$
															i s_{+\dot\theta}\,\langle f_{++}(s)\,B_{-\dot\beta}(-s)\rangle_{\rm PV}
=\frac{s_{+\dot\theta}s_{+\dot\beta}}{s^2+M^2}.
$$

于是

$$
															\Gamma_{12;M}^{\rm PV\text{-}loop}{}_{\dot\theta}{}^i{}_j{}^k{}_l
=
2i g^2\int_q
\frac{(q-p_2)_{+\dot\theta}(q-p_2)_{+\dot\beta}}{(q^2+M^2)\big((q-p_2)^2+M^2\big)}\,
\mathscr F_{12}^{\dot\beta}{}^i{}_j{}^k{}_l
$$

$$
															\qquad
-2i g^2 M^2\int_q
\frac{(q-p_2)_{+\dot\theta}(q-p_2)_{+\dot\beta}}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}\,
\mathscr F_{12}^{\dot\beta}{}^i{}_j{}^k{}_l.
$$

前一项是 contact/EOM sector；后一项是 anomaly sector。

记

$$
															\Gamma_{12;M}^{({\rm anom})}{}_{\dot\theta}
=
-2i g^2 M^2\int_q
\frac{(q-p_2)_{+\dot\theta}(q-p_2)_{+\dot\beta}}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}\,\mathscr F_{12}^{\dot\beta}.
$$

Feynman parameter：

$$
															\frac{1}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}
=
2\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
\frac{1}{\big[(q+yp_1-zp_2)^2+M^2+\Delta\big]^3},
$$

$$
\Delta=xy\,p_1^2+xz\,p_2^2+yz\,p^2.
$$

令

$$
\ell=q+yp_1-zp_2,\qquad q-p_2=\ell-yp-xp_2.
$$

则只剩 shift piece：

$$
															\Gamma_{12;M}^{({\rm anom})}
=
-4i g^2 M^2\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
(yp+xp_2)_{+\dot\theta}(yp+xp_2)_{+\dot\beta}
\int_\ell\frac{1}{(\ell^2+M^2+\Delta)^3}\,\mathscr F_{12}^{\dot\beta}.
$$

再用

$$
\int_\ell\frac{1}{(\ell^2+\Omega)^3}=\frac{1}{32\pi^2}\frac{1}{\Omega},
$$

得

$$
															\Gamma_{12;M}^{({\rm anom})}
=
-\frac{i g^2}{8\pi^2}
\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
\frac{M^2}{M^2+\Delta}
(yp+xp_2)_{+\dot\theta}(yp+xp_2)_{+\dot\beta}\,\mathscr F_{12}^{\dot\beta}.
$$

取 $(M\to\infty)$ 的 local part：

$$
															\Gamma_{12}^{({\rm anom,loc})}{}_{\dot\theta}
=
-\frac{i g^2}{8\pi^2}
\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
(yp+xp_2)_{+\dot\theta}(yp+xp_2)_{+\dot\beta}\,\mathscr F_{12}^{\dot\beta}.
$$

simplex integrals：

$$
															\int y^2=\frac{1}{12},\qquad
\int y(x+y)=\frac{1}{8},\qquad
\int (x+y)^2=\frac{1}{4}.
$$

定义

$$
															\Xi_{12,+\dot\theta,+\dot\beta}(p_1,p_2)
:=
p_{1,+\dot\theta}p_{1,+\dot\beta}
+3p_{1,+(\dot\theta}p_{2,+\dot\beta)}
+3p_{2,+\dot\theta}p_{2,+\dot\beta},
$$

则

$$
															\boxed{
\Gamma_{12}^{({\rm anom,loc})}{}_{\dot\theta}{}^i{}_j{}^k{}_l
=
-\frac{i g^2}{96\pi^2}
\,\Xi_{12,+\dot\theta,+\dot\beta}(p_1,p_2)
\,\mathscr F_{12}^{\dot\beta}{}^i{}_j{}^k{}_l
}.
$$

### Pattern 21

完全平行。定义

$$
															\Xi_{21,+\dot\theta,+\dot\beta}(p_1,p_2)
:=
3p_{1,+\dot\theta}p_{1,+\dot\beta}
+3p_{1,+(\dot\theta}p_{2,+\dot\beta)}
+p_{2,+\dot\theta}p_{2,+\dot\beta},
$$

则

$$
															\boxed{
\Gamma_{21}^{({\rm anom,loc})}{}_{\dot\theta}{}^i{}_j{}^k{}_l
=
-\frac{i g^2}{96\pi^2}
\,\Xi_{21,+\dot\theta,+\dot\beta}(p_1,p_2)
\,\mathscr F_{21}^{\dot\beta}{}^i{}_j{}^k{}_l
}.
$$

所以 ordered-pair 的 1-loop local anomaly 是

$$
															\boxed{
\mathcal I\!\left[\big(i\nabla_{+\dot\alpha}\bar\lambda^{\dot\alpha},\nabla_{+\dot\theta}f_{++}\big)^{(1),{\rm loc}}{}^i{}_j{}^k{}_l(p)\right]
=
-\frac{i g^2}{96\pi^2}
\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)
\Big[
\Xi_{12,+\dot\theta,+\dot\beta}\,\mathscr F_{12}^{\dot\beta}{}^i{}_j{}^k{}_l
+\Xi_{21,+\dot\theta,+\dot\beta}\,\mathscr F_{21}^{\dot\beta}{}^i{}_j{}^k{}_l
\Big]
}.
$$

### Full $Q_1(f_{++}\nabla_{+\dot\theta}f_{++})$：loop-focus final result

去掉 $[Q_-,\nabla_{+\dot\theta}]$ 的 tree term 后，

$$
															(Q_-f_{++})\,\nabla_{+\dot\theta}f_{++}
+
f_{++}\,\nabla_{+\dot\theta}(Q_-f_{++})
=
\nabla_{+\dot\theta}\big(f_{++}\,Q_-f_{++}\big),
$$

因为 $f_{++}$ 是 bosonic。

因此

$$
															\mathcal I\!\left[Q_1\big(f_{++}\nabla_{+\dot\theta}f_{++}\big){}^i{}_j{}^k{}_l(p)\right]_{\rm loop}
=
i\,p_{+\dot\theta}\,\mathcal I\!\left[Q_1\big(f_{++}f_{++}\big){}^i{}_j{}^k{}_l(p)\right].
$$

代入前页已经得到的

$$
															\mathcal I\!\left[Q_1\big(f_{++}f_{++}\big){}^i{}_j{}^k{}_l(p)\right]
=
-\frac{g^2}{48\pi^2}
\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)
\Big[
(p_1+2p_2)_{+\dot\beta}\,\mathscr F_{12}^{\dot\beta}
+
(2p_1+p_2)_{+\dot\beta}\,\mathscr F_{21}^{\dot\beta}
\Big]{}^i{}_j{}^k{}_l,
$$

得最终 total loop piece：

$$
															\boxed{
\mathcal I\!\left[Q_1\big(f_{++}\nabla_{+\dot\theta}f_{++}\big){}^i{}_j{}^k{}_l(p)\right]_{\rm loop}
=
-\frac{i g^2}{48\pi^2}
\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)\,p_{+\dot\theta}
\Big[
(p_1+2p_2)_{+\dot\beta}\,\mathscr F_{12}^{\dot\beta}
+
(2p_1+p_2)_{+\dot\beta}\,\mathscr F_{21}^{\dot\beta}
\Big]{}^i{}_j{}^k{}_l
}.
$$

</aside>

<aside>

## $Q_1((\nabla_{+\dot\alpha}f_{++})\bar\lambda_{\dot\beta})$

#### Setup

沿用本页 conventions。取 $mathcal O_{dotalphadotbeta}{}^i{}*j{}^k{}_l(x):=(nabla*{+dotalpha}f_{++}){}^i{}*j(x),barlambda*{dotbeta}{}^k{}_l(x)$。

$Q_-f_{++}=inabla_{+dotrho}barlambda^{dotrho},quad Q_-barlambda_{dotbeta}=0,quad [Q_-,nabla_{+dotalpha}]X=i[barlambda_{dotalpha},X]$。

故

$$
Q_1\mathcal O_{\dot\alpha\dot\beta}
=
\underbrace{(i\nabla_{+\dot\alpha}\nabla_{+\dot\rho}\bar\lambda^{\dot\rho})\,\bar\lambda_{\dot\beta}}_{\text{loop-focus}}
+
\underbrace{i[\bar\lambda_{\dot\alpha},f_{++}]\,\bar\lambda_{\dot\beta}}_{\text{tree level}}.
$$

只算 loop/anomaly 部分。沿用前页 propagators、$V_{Alambdabarlambda}=V_L-V_R$、matrix-index / double-line、同一个 $(mathscr C_{12},mathscr C_{21})$、PV collapse identity。

two-field triangle piece：

$$
\mathcal O^{(\partial\partial)}_{\dot\alpha\dot\beta}{}^i{}_j{}^k{}_l
:=
\partial_{+\dot\alpha}\big(i\partial_{+\dot\rho}\bar\lambda^{\dot\rho}{}^i{}_j\big)\,\bar\lambda_{\dot\beta}{}^k{}_l.
$$

动量空间 insertion：

$$
\mathcal I\!\left[\mathcal O^{(\partial\partial)}_{\dot\alpha\dot\beta}(p)\right]
=
\int_{r,s}(2\pi)^4\delta^{(4)}(p-r-s)
(i r_{+\dot\alpha})(-r_{+\dot\rho})
\bar\lambda^{\dot\rho}(r)\bar\lambda_{\dot\beta}(s).
$$

#### Pattern 12

routing：

$$
r=q+p_1,\qquad s=p_2-q,\qquad p=p_1+p_2.
$$

PV propagators：

$$
\langle \Lambda_\alpha(p)\bar\Lambda_{\dot\beta}(-p)\rangle_{\rm PV}
=-\frac{i p_{\alpha\dot\beta}}{p^2+M^2},
\qquad
\langle B_{\alpha\dot\alpha}(p)B_{\beta\dot\beta}(-p)\rangle_{\rm PV}
=\frac{2\epsilon_{\alpha\beta}\epsilon_{\dot\alpha\dot\beta}}{p^2+M^2}.
$$

$$
\big(S_M(k)P_L\big)_{\alpha\dot\alpha}
=-\frac{i k_{\alpha\dot\alpha}}{k^2+M^2}.
$$

collapse：

$$
-r_{+\dot\rho}\big(S_M(r)P_L\big)_\alpha{}^{\dot\rho}
=i\epsilon_{+\alpha}-i\frac{M^2}{r^2+M^2}\epsilon_{+\alpha}.
$$

second fermion line：

$$
\big(S_M(q-p_2)P_L\big)_{\rho\dot\beta}
=-\frac{i (q-p_2)_{\rho\dot\beta}}{(q-p_2)^2+M^2}.
$$

故

$$
\Gamma_{12;M}^{\rm PV\text{-}loop}{}_{\dot\alpha\dot\beta}{}^i{}_j{}^k{}_l
=
-2i g^2\int_q
\frac{(q+p_1)_{+\dot\alpha}(q-p_2)_{+\dot\beta}}
{(q^2+M^2)\big((q-p_2)^2+M^2\big)}
\,\mathscr C_{12}{}^i{}_j{}^k{}_l
$$

$$
\qquad
+
2i g^2M^2\int_q
\frac{(q+p_1)_{+\dot\alpha}(q-p_2)_{+\dot\beta}}
{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}
\,\mathscr C_{12}{}^i{}_j{}^k{}_l.
$$

第一项是 contact/EOM sector。第二项是 anomaly sector：

$$
\Gamma_{12;M}^{(\rm anom)}{}_{\dot\alpha\dot\beta}
=
2i g^2M^2\int_q
\frac{(q+p_1)_{+\dot\alpha}(q-p_2)_{+\dot\beta}}
{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}
\,\mathscr C_{12}.
$$

Feynman parameter：

$$
\frac{1}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}
=
2\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
\frac{1}{\big[(q+yp_1-zp_2)^2+M^2+\Delta\big]^3},
$$

$$
\Delta=xy\,p_1^2+xz\,p_2^2+yz\,p^2.
$$

令

$$
\ell=q+yp_1-zp_2,
$$

则

$$
q+p_1=\ell+zp+xp_1=\ell+(x+z)p_1+z p_2,
$$

$$
q-p_2=\ell-yp-xp_2=\ell-y p_1-(x+y)p_2.
$$

写

$$
X:=(x+z)p_1+z p_2,\qquad Y:=y p_1+(x+y)p_2.
$$

于是

$$
\Gamma_{12;M}^{(\rm anom)}
=
4i g^2M^2\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
\int_\ell
\frac{(\ell+X)_{+\dot\alpha}(\ell-Y)_{+\dot\beta}}
{(\ell^2+M^2+\Delta)^3}
\,\mathscr C_{12}.
$$

$$
\int_\ell \ell_{+\dot\alpha}F(\ell^2)=0,\qquad
\int_\ell \ell_{+\dot\alpha}\ell_{+\dot\beta}F(\ell^2)=0,
$$

故只剩 shift piece：

$$
\Gamma_{12;M}^{(\rm anom)}
=
-4i g^2M^2\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
X_{+\dot\alpha}Y_{+\dot\beta}
\int_\ell\frac{1}{(\ell^2+M^2+\Delta)^3}
\,\mathscr C_{12}.
$$

$$
\int_\ell\frac{1}{(\ell^2+\Omega)^3}
=
\frac{1}{32\pi^2}\frac{1}{\Omega}.
$$

故

$$
\Gamma_{12;M}^{(\rm anom)}
=
-\frac{i g^2}{8\pi^2}
\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
\frac{M^2}{M^2+\Delta}
X_{+\dot\alpha}Y_{+\dot\beta}
\,\mathscr C_{12}.
$$

取 local part：

$$
\Gamma_{12}^{(\rm anom,loc)}{}_{\dot\alpha\dot\beta}
=
-\frac{i g^2}{8\pi^2}
\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
X_{+\dot\alpha}Y_{+\dot\beta}
\,\mathscr C_{12}.
$$

simplex integrals：

$$
\int (x+z)y=\frac{1}{12},\qquad
\int (x+z)(x+y)=\frac{5}{24},\qquad
\int zy=\frac{1}{24},\qquad
\int z(x+y)=\frac{1}{12}.
$$

定义

$$
\Upsilon_{12,+\dot\alpha,+\dot\beta}(p_1,p_2)
:=
2p_{1,+\dot\alpha}p_{1,+\dot\beta}
+5p_{1,+\dot\alpha}p_{2,+\dot\beta}
+p_{2,+\dot\alpha}p_{1,+\dot\beta}
+2p_{2,+\dot\alpha}p_{2,+\dot\beta}.
$$

则

$$
\boxed{
\Gamma_{12}^{(\rm anom,loc)}{}_{\dot\alpha\dot\beta}{}^i{}_j{}^k{}_l
=
-\frac{i g^2}{192\pi^2}
\,\Upsilon_{12,+\dot\alpha,+\dot\beta}(p_1,p_2)
\,\mathscr C_{12}{}^i{}_j{}^k{}_l
}.
$$

#### Pattern 21

完全平行：

$$
\Upsilon_{21,+\dot\alpha,+\dot\beta}(p_1,p_2)
:=
2p_{1,+\dot\alpha}p_{1,+\dot\beta}
+p_{1,+\dot\alpha}p_{2,+\dot\beta}
+5p_{2,+\dot\alpha}p_{1,+\dot\beta}
+2p_{2,+\dot\alpha}p_{2,+\dot\beta}.
$$

$$
\boxed{
\Gamma_{21}^{(\rm anom,loc)}{}_{\dot\alpha\dot\beta}{}^i{}_j{}^k{}_l
=
-\frac{i g^2}{192\pi^2}
\,\Upsilon_{21,+\dot\alpha,+\dot\beta}(p_1,p_2)
\,\mathscr C_{21}{}^i{}_j{}^k{}_l
}.
$$

#### Open-index final result

$$
\boxed{
\mathcal I\!\left[
Q_1\!\Big((\nabla_{+\dot\alpha}f_{++})\,\bar\lambda_{\dot\beta}\Big)_{\rm loop}^{(1),\rm loc}
{}^i{}_j{}^k{}_l(p)
\right]
=
-\frac{i g^2}{192\pi^2}
\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)
\Big[
\Upsilon_{12,+\dot\alpha,+\dot\beta}\,\mathscr C_{12}{}^i{}_j{}^k{}_l
+
\Upsilon_{21,+\dot\alpha,+\dot\beta}\,\mathscr C_{21}{}^i{}_j{}^k{}_l
\Big]
}.
$$

这里 $(\mathscr C_{12},\mathscr C_{21})$ 就是前页已经定义好的 open-index $(\bar\lambda\bar\lambda)$ color-flow tensor。

#### Lie-algebra indices $(A,B,\dots)$

$$
\mathcal O_{\dot\alpha\dot\beta}^{AB}(x)
:=(\nabla_{+\dot\alpha}f_{++}^A)(x)\,\bar\lambda_{\dot\beta}^B(x),
\qquad
[T^A,T^B]=f^{AB}{}_C T^C,
\qquad
\operatorname{Tr}(T^AT^B)=\delta^{AB}.
$$

$$
\mathscr C_{12}^{AB}(p_1,p_2)
=
\epsilon^{\dot\gamma\dot\delta}
f^{CA}{}_E f^{DB}{}_E
\bar\lambda_{\dot\gamma}^{C}(p_1)\bar\lambda_{\dot\delta}^{D}(p_2),
\qquad
\mathscr C_{21}^{AB}(p_1,p_2)=\mathscr C_{12}^{AB}(p_2,p_1).
$$

于是

$$
\boxed{
\mathcal I\!\left[
Q_1\mathcal O_{\dot\alpha\dot\beta}^{AB}(p)
\right]_{\rm loop}^{(1),\rm loc}
=
-\frac{i g^2}{192\pi^2}
\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)
\Big[
\Upsilon_{12,+\dot\alpha,+\dot\beta}\,\mathscr C_{12}^{AB}
+
\Upsilon_{21,+\dot\alpha,+\dot\beta}\,\mathscr C_{21}^{AB}
\Big]
}.
$$

把第二项 rename $(p_1\leftrightarrow p_2)$ 后，

$$
\boxed{
\mathcal I\!\left[
Q_1\mathcal O_{\dot\alpha\dot\beta}^{AB}(p)
\right]_{\rm loop}^{(1),\rm loc}
=
-\frac{i g^2}{96\pi^2}
\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)
\,\Upsilon_{12,+\dot\alpha,+\dot\beta}(p_1,p_2)
\,\mathscr C_{12}^{AB}(p_1,p_2).
$$

#### local operator rewrite

定义

$$
\mathcal K_{\dot\alpha\dot\beta}^{AB}(x)
:=
\epsilon^{\dot\gamma\dot\delta}
f^{CA}{}_E f^{DB}{}_E
\Big[
2(\nabla_{+\dot\alpha}\nabla_{+\dot\beta}\bar\lambda_{\dot\gamma}^{C})\bar\lambda_{\dot\delta}^{D}
+5(\nabla_{+\dot\alpha}\bar\lambda_{\dot\gamma}^{C})(\nabla_{+\dot\beta}\bar\lambda_{\dot\delta}^{D})
$$

$$
\qquad\qquad\qquad\qquad
+(\nabla_{+\dot\beta}\bar\lambda_{\dot\gamma}^{C})(\nabla_{+\dot\alpha}\bar\lambda_{\dot\delta}^{D})
+2\bar\lambda_{\dot\gamma}^{C}(\nabla_{+\dot\alpha}\nabla_{+\dot\beta}\bar\lambda_{\dot\delta}^{D})
\Big].
$$

则

$$
\boxed{
Q_1\mathcal O_{\dot\alpha\dot\beta}^{AB}(x)\Big|_{\rm loop}^{(1),\rm loc}
=
\frac{i g^2}{96\pi^2}
\,\mathcal K_{\dot\alpha\dot\beta}^{AB}(x).
}.
$$

在 1-loop order，

$$
\partial\rightarrow\nabla
$$

的 covariantization 直接成立。

#### consistency check

由

$$
\nabla_{+\dot\alpha}\Big(i\nabla_{+\dot\rho}\bar\lambda^{\dot\rho}\,\bar\lambda_{\dot\beta}\Big)
=
\Big(i\nabla_{+\dot\alpha}\nabla_{+\dot\rho}\bar\lambda^{\dot\rho}\Big)\bar\lambda_{\dot\beta}
+
\Big(i\nabla_{+\dot\rho}\bar\lambda^{\dot\rho}\Big)\nabla_{+\dot\alpha}\bar\lambda_{\dot\beta},
$$

得

$$
Q_1\!\Big((\nabla_{+\dot\alpha}f_{++})\bar\lambda_{\dot\beta}\Big)_{\rm loop}
=
\nabla_{+\dot\alpha}Q_1\!\Big(f_{++}\bar\lambda_{\dot\beta}\Big)_{\rm loop}
-
Q_1\!\Big(f_{++}\nabla_{+\dot\alpha}\bar\lambda_{\dot\beta}\Big)_{\rm loop},
$$

代入前页两个已算结果，正好给出上面的 $(Upsilon_{12},Upsilon_{21})$。

![image.png](../source_archive/%E7%9B%B4%E6%8E%A51-loop%20level%E8%AE%A1%E7%AE%97/image%203.png)

</aside>

<aside>

## $Q_1((\nabla_{+\dot\alpha}f_{++})\nabla_{+\dot\beta} \bar\lambda_{\dot \gamma})$

### 2. $Q_1$ 的 split

取

$$
\mathcal O_{\dot\alpha\dot\beta\dot\gamma}{}^i{}_j{}^k{}_l(x):=\nabla_{+\dot\alpha}f_{++}{}^i{}_j(x)\,\nabla_{+\dot\beta}\bar\lambda_{\dot\gamma}{}^k{}_l(x).
$$

沿用本页 propagators, $V_{Alambdabarlambda}=V_L-V_R$, $Q_-f_{++}=inabla_{+dotrho}barlambda^{dotrho}$, $Q_-barlambda_{dotgamma}=0$, 同一个 $mathscr C_{12},mathscr C_{21}$, 以及 PV collapse identity.

完整地

$$
	Q_1\mathcal O_{\dot\alpha\dot\beta\dot\gamma}
=
\underbrace{\big(i\nabla_{+\dot\alpha}\nabla_{+\dot\rho}\bar\lambda^{\dot\rho}\big)\,\nabla_{+\dot\beta}\bar\lambda_{\dot\gamma}}_{\text{loop-focus}}+\underbrace{i[\bar\lambda_{\dot\alpha},f_{++}]\,\nabla_{+\dot\beta}\bar\lambda_{\dot\gamma}+i\nabla_{+\dot\alpha}f_{++}\,[\bar\lambda_{\dot\beta},\bar\lambda_{\dot\gamma}]}_{\text{tree level}}.
$$

只算 loop/anomaly 部分：

$$
\mathcal O^{\rm loop}_{\dot\alpha\dot\beta\dot\gamma}{}^i{}_j{}^k{}_l:=i\nabla_{+\dot\alpha}\nabla_{+\dot\rho}\bar\lambda^{\dot\rho}{}^i{}_j\,\nabla_{+\dot\beta}\bar\lambda_{\dot\gamma}{}^k{}_l.
$$

其 two-field triangle piece：

$$
\mathcal O^{(\partial\partial\partial)}_{\dot\alpha\dot\beta\dot\gamma}{}^i{}_j{}^k{}_l:=i\partial_{+\dot\alpha}\partial_{+\dot\rho}\bar\lambda^{\dot\rho}{}^i{}_j\,i\partial_{+\dot\beta}\bar\lambda_{\dot\gamma}{}^k{}_l.
$$

动量空间 insertion：

$$
\mathcal I\!\left[\mathcal O^{(\partial\partial\partial)}_{\dot\alpha\dot\beta\dot\gamma}(p)\right]=\int_{r,s}(2\pi)^4\delta^{(4)}(p-r-s)\,(i r_{+\dot\alpha})(-r_{+\dot\rho})(i s_{+\dot\beta})\,\bar\lambda^{\dot\rho}(r)\bar\lambda_{\dot\gamma}(s).
$$

并记

$$
\mathscr C_{21}{}^i{}_j{}^k{}_l(p_1,p_2)=\mathscr C_{12}{}^i{}_j{}^k{}_l(p_2,p_1).
$$

### 3. Pattern 12

routing：

$$
r=q+p_1,\qquad s=p_2-q,\qquad p=p_1+p_2.
$$

PV propagators：

$$
\langle \Lambda_\alpha(p)\bar\Lambda_{\dot\beta}(-p)\rangle_{\rm PV}=-\frac{i p_{\alpha\dot\beta}}{p^2+M^2},\qquad \langle B_{\alpha\dot\alpha}(p)B_{\beta\dot\beta}(-p)\rangle_{\rm PV}=\frac{2\epsilon_{\alpha\beta}\epsilon_{\dot\alpha\dot\beta}}{p^2+M^2}.
$$

$$
\big(S_M(k)P_L\big)_{\alpha\dot\alpha}=-\frac{i k_{\alpha\dot\alpha}}{k^2+M^2}.
$$

collapse:

$$
-r_{+\dot\rho}\big(S_M(r)P_L\big)_\alpha{}^{\dot\rho}=i\epsilon_{+\alpha}-i\frac{M^2}{r^2+M^2}\epsilon_{+\alpha},
$$

$$
i s_{+\dot\beta}\big(S_M(s)P_L\big)_{\rho\dot\gamma}=\frac{s_{+\dot\beta}s_{\rho\dot\gamma}}{s^2+M^2}.
$$

故

$$
\Gamma_{12;M}^{\rm PV\text{-}loop}{}_{\dot\alpha\dot\beta\dot\gamma}{}^i{}_j{}^k{}_l=-2 g^2\int_q\frac{(q+p_1)_{+\dot\alpha}(q-p_2)_{+\dot\beta}(q-p_2)_{+\dot\gamma}}{(q^2+M^2)\big((q-p_2)^2+M^2\big)}\,\mathscr C_{12}{}^i{}_j{}^k{}_l
$$

$$
\qquad+2 g^2 M^2\int_q\frac{(q+p_1)_{+\dot\alpha}(q-p_2)_{+\dot\beta}(q-p_2)_{+\dot\gamma}}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}\,\mathscr C_{12}{}^i{}_j{}^k{}_l.
$$

前一项是 contact/EOM sector，后一项是 anomaly sector：

$$
\Gamma_{12;M}^{(\rm anom)}{}_{\dot\alpha\dot\beta\dot\gamma}=2 g^2 M^2\int_q\frac{(q+p_1)_{+\dot\alpha}(q-p_2)_{+\dot\beta}(q-p_2)_{+\dot\gamma}}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}\,\mathscr C_{12}.
$$

Feynman parameter：

$$
\frac{1}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}=2\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)\,\frac{1}{\big[(q+yp_1-zp_2)^2+M^2+\Delta\big]^3},
$$

$$
\Delta=xy\,p_1^2+xz\,p_2^2+yz\,p^2.
$$

令

$$
\ell=q+yp_1-zp_2.
$$

则

$$
q+p_1=\ell+z p+x p_1,\qquad q-p_2=\ell-y p-x p_2.
$$

故

$$
\Gamma_{12;M}^{(\rm anom)}=4 g^2 M^2\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)\int_\ell\frac{(\ell+z p+x p_1)_{+\dot\alpha}(\ell-y p-x p_2)_{+\dot\beta}(\ell-y p-x p_2)_{+\dot\gamma}}{(\ell^2+M^2+\Delta)^3}\,\mathscr C_{12}.
$$

$$
\int_\ell \ell_{+\dot\mu}F(\ell^2)=0,\qquad \int_\ell \ell_{+\dot\mu}\ell_{+\dot\nu}F(\ell^2)=0,\qquad \int_\ell \ell_{+\dot\mu}\ell_{+\dot\nu}\ell_{+\dot\rho}F(\ell^2)=0.
$$

只剩 shift piece：

$$
\Gamma_{12;M}^{(\rm anom)}=4 g^2 M^2\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)\,(z p+x p_1)_{+\dot\alpha}(y p+x p_2)_{+\dot\beta}(y p+x p_2)_{+\dot\gamma}\int_\ell\frac{1}{(\ell^2+M^2+\Delta)^3}\,\mathscr C_{12}.
$$

$$
\int_\ell\frac{1}{(\ell^2+\Omega)^3}=\frac{1}{32\pi^2}\frac{1}{\Omega}.
$$

于是 local part：

$$
\Gamma_{12}^{(\rm anom,loc)}{}_{\dot\alpha\dot\beta\dot\gamma}=\frac{g^2}{8\pi^2}\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)\,(z p+x p_1)_{+\dot\alpha}(y p+x p_2)_{+\dot\beta}(y p+x p_2)_{+\dot\gamma}\,\mathscr C_{12}.
$$

写成

$$
z p+x p_1=(x+z)p_1+z p_2,\qquad y p+x p_2=y p_1+(x+y)p_2.
$$

simplex 积分：

$$
\int (x+z)y^2=\frac{1}{30},\qquad \int (x+z)y(x+y)=\frac{7}{120},\qquad \int (x+z)(x+y)^2=\frac{3}{20},
$$

$$
\int z y^2=\frac{1}{60},\qquad \int z y(x+y)=\frac{1}{40},\qquad \int z(x+y)^2=\frac{1}{20}.
$$

定义

$$
\Omega_{12,+\dot\alpha,+\dot\beta,+\dot\gamma}(p_1,p_2):=2\,p_{1,+\dot\alpha}p_{1,+\dot\beta}p_{1,+\dot\gamma}+7\,p_{1,+\dot\alpha}p_{1,+(\dot\beta}p_{2,+\dot\gamma)}+9\,p_{1,+\dot\alpha}p_{2,+\dot\beta}p_{2,+\dot\gamma}
$$

$$
\qquad\qquad+p_{2,+\dot\alpha}p_{1,+\dot\beta}p_{1,+\dot\gamma}+3\,p_{2,+\dot\alpha}p_{1,+(\dot\beta}p_{2,+\dot\gamma)}+3\,p_{2,+\dot\alpha}p_{2,+\dot\beta}p_{2,+\dot\gamma}.
$$

则

$$
\boxed{\Gamma_{12}^{(\rm anom,loc)}{}_{\dot\alpha\dot\beta\dot\gamma}{}^i{}_j{}^k{}_l=\frac{g^2}{480\pi^2}\,\Omega_{12,+\dot\alpha,+\dot\beta,+\dot\gamma}(p_1,p_2)\,\mathscr C_{12}{}^i{}_j{}^k{}_l}.
$$

并且

$$
\Gamma_{12}^{(\rm anom,loc)}{}_{\dot\alpha\dot\beta\dot\gamma}=\Gamma_{12}^{(\rm anom,loc)}{}_{\dot\alpha(\dot\beta\dot\gamma)}.
$$

### 4. Pattern 21

完全平行：

$$
\Omega_{21,+\dot\alpha,+\dot\beta,+\dot\gamma}(p_1,p_2):=\Omega_{12,+\dot\alpha,+\dot\beta,+\dot\gamma}(p_2,p_1),
$$

即

$$
\Omega_{21,+\dot\alpha,+\dot\beta,+\dot\gamma}=3\,p_{1,+\dot\alpha}p_{1,+\dot\beta}p_{1,+\dot\gamma}+3\,p_{1,+\dot\alpha}p_{1,+(\dot\beta}p_{2,+\dot\gamma)}+p_{1,+\dot\alpha}p_{2,+\dot\beta}p_{2,+\dot\gamma}
$$

$$
\qquad\qquad+9\,p_{2,+\dot\alpha}p_{1,+\dot\beta}p_{1,+\dot\gamma}+7\,p_{2,+\dot\alpha}p_{1,+(\dot\beta}p_{2,+\dot\gamma)}+2\,p_{2,+\dot\alpha}p_{2,+\dot\beta}p_{2,+\dot\gamma}.
$$

$$
\boxed{\Gamma_{21}^{(\rm anom,loc)}{}_{\dot\alpha\dot\beta\dot\gamma}{}^i{}_j{}^k{}_l=\frac{g^2}{480\pi^2}\,\Omega_{21,+\dot\alpha,+\dot\beta,+\dot\gamma}(p_1,p_2)\,\mathscr C_{21}{}^i{}_j{}^k{}_l}.
$$

### 5. Open-index final result

$$
\boxed{\mathcal I\!\left[Q_1\!\left(\nabla_{+\dot\alpha}f_{++}\,\nabla_{+\dot\beta}\bar\lambda_{\dot\gamma}\right)_{\rm loop}^{(1),\rm loc}{}^i{}_j{}^k{}_l(p)\right]=\frac{g^2}{480\pi^2}\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)\Big[\Omega_{12,+\dot\alpha,+\dot\beta,+\dot\gamma}\,\mathscr C_{12}{}^i{}_j{}^k{}_l+\Omega_{21,+\dot\alpha,+\dot\beta,+\dot\gamma}\,\mathscr C_{21}{}^i{}_j{}^k{}_l\Big]}.
$$

只对 $(\dot\beta\dot\gamma)$ symmetric。

$$
Q_1(\cdots)=Q_1(\cdots)_{\rm tree}+Q_1(\cdots)_{\rm loop},
$$

上框是 loop/anomaly 部分。

### 6. Lie-algebra indices $(A,B,\dots)$

定义

$$
\mathcal O_{\dot\alpha\dot\beta\dot\gamma}^{AB}(x):=\nabla_{+\dot\alpha}f_{++}^A(x)\,\nabla_{+\dot\beta}\bar\lambda_{\dot\gamma}^B(x),\qquad [T^A,T^B]=f^{AB}{}_C T^C,\qquad \operatorname{Tr}(T^AT^B)=\delta^{AB}.
$$

$$
\mathscr C_{12}^{AB}(p_1,p_2)=\epsilon^{\dot\delta\dot\epsilon}f^{CA}{}_E f^{DB}{}_E\,\bar\lambda_{\dot\delta}^C(p_1)\bar\lambda_{\dot\epsilon}^D(p_2),\qquad \mathscr C_{21}^{AB}(p_1,p_2)=\mathscr C_{12}^{AB}(p_2,p_1).
$$

这正是前页 $\mathscr C_{12},\mathscr C_{21}$ 的 Lie-algebra rewrite。把第二项 $p_1\leftrightarrow p_2$ 重命名后，

$$
\boxed{\mathcal I\!\left[Q_1\mathcal O_{\dot\alpha\dot\beta\dot\gamma}^{AB}(p)\right]_{\rm loop}^{(1),\rm loc}=\frac{g^2}{240\pi^2}\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)\,\Omega_{12,+\dot\alpha,+\dot\beta,+\dot\gamma}(p_1,p_2)\,\mathscr C_{12}^{AB}(p_1,p_2)}.
$$

### 7. Local operator rewrite

定义

$$
\mathcal K_{\dot\alpha\dot\beta\dot\gamma}^{AB}(x):=\epsilon^{\dot\delta\dot\epsilon}f^{CA}{}_E f^{DB}{}_E\Big[2\,(\nabla_{+\dot\alpha}\nabla_{+\dot\beta}\nabla_{+\dot\gamma}\bar\lambda_{\dot\delta}^C)\,\bar\lambda_{\dot\epsilon}^D+7\,(\nabla_{+\dot\alpha}\nabla_{+(\dot\beta}\bar\lambda_{\dot\delta}^C)(\nabla_{+\dot\gamma)}\bar\lambda_{\dot\epsilon}^D)+9\,(\nabla_{+\dot\alpha}\bar\lambda_{\dot\delta}^C)(\nabla_{+\dot\beta}\nabla_{+\dot\gamma}\bar\lambda_{\dot\epsilon}^D)
$$

$$
\qquad\qquad+(\nabla_{+\dot\beta}\nabla_{+\dot\gamma}\bar\lambda_{\dot\delta}^C)(\nabla_{+\dot\alpha}\bar\lambda_{\dot\epsilon}^D)+3\,(\nabla_{+(\dot\beta}\bar\lambda_{\dot\delta}^C)(\nabla_{+\dot\alpha}\nabla_{+\dot\gamma)}\bar\lambda_{\dot\epsilon}^D)+3\,\bar\lambda_{\dot\delta}^C(\nabla_{+\dot\alpha}\nabla_{+\dot\beta}\nabla_{+\dot\gamma}\bar\lambda_{\dot\epsilon}^D)\Big].
$$

则

$$
\boxed{Q_1\mathcal O_{\dot\alpha\dot\beta\dot\gamma}^{AB}(x)\Big\|_{\rm loop}^{(1),\rm loc}=\frac{i g^2}{240\pi^2}\,\mathcal K_{\dot\alpha\dot\beta\dot\gamma}^{AB}(x)},\qquad \mathcal K_{\dot\alpha\dot\beta\dot\gamma}^{AB}=\mathcal K_{\dot\alpha(\dot\beta\dot\gamma)}^{AB}.
$$

同样地，在 1-loop order 可直接取 $\partial\to\nabla$ 做 covariantization。

</aside>

