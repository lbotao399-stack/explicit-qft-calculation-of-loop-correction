# Generating function of derivatives$Q_1(f_{++}e^{w\nabla}f_{++})$(Full One loop result)(Weird)

![image.png](../source_archive/%E7%9B%B4%E6%8E%A51-loop%20level%E8%AE%A1%E7%AE%97/image%204.png)

#### Setup

定义

$$
w\cdot \nabla_+ := w^{+\dot\alpha}\nabla_{+\dot\alpha},
\qquad
w\cdot p_a := w^{+\dot\alpha}p_{a,+\dot\alpha}.
$$

$$
\mathcal O_w{}^i{}_j{}^k{}_l(x):=f_{++}{}^i{}_j(x)e^{w\cdot \nabla_+}f_{++}{}^k{}_l(x).
$$

#### **只保留 loop-focus：**

$$
Q_1\mathcal O_w
\underbrace{
 i\nabla_{+\dot\rho}\bar\lambda^{\dot\rho},e^{,w\cdot \nabla_+}f_{++}
}_{\text{hit first }f_{++}}
+
\underbrace{
 f_{++},e^{,w\cdot \nabla_+}\big(i\nabla_{+\dot\rho}\bar\lambda^{\dot\rho}\big)
}_{\text{hit second }f_{++}}
+
\text{tree from }[Q_-,\nabla_+].
$$

tree pieces 全部丢开；只算 anomaly。沿用前页 propagators、$(V_{A\lambda\bar\lambda}=V_L-V_R)$、matrix-index / double-line、以及 mixed color tensor $(\mathscr F_{12}^{\dot\beta},\mathscr F_{21}^{\dot\beta})$。

$$
\mathscr F_{12}^{\dot\beta}{}^i{}_j{}^k{}_l
$$

$$
\Pi^{mn}{}_{jl},f_{++}{}^i{}_m(p_1)\bar\lambda^{\dot\beta}{}^k{}_n(p_2)-\Pi^{mk}{}_{jn},f_{++}{}^i{}_m(p_1)\bar\lambda^{\dot\beta}{}^n{}_l(p_2)
$$

$$
\qquad-\Pi^{in}{}_{ml},f_{++}{}^m{}_j(p_1)\bar\lambda^{\dot\beta}{}^k{}_n(p_2)+\Pi^{ik}{}_{mn},f_{++}{}^m{}_j(p_1)\bar\lambda^{\dot\beta}{}^n{}_l(p_2),
$$

$$
\mathscr F_{21}^{\dot\beta}(p_1,p_2)=\mathscr F_{12}^{\dot\beta}(p_2,p_1).
$$

#### **Pattern 12**

对应 $(\mathscr F_{12}^{\dot\beta})$ 的 ordered contribution。two-field PV loop 直接写成

$$
\Gamma_{12;M}^{\rm PV\text{-}loop}{}^i{}_j{}^k{}_l(w)
$$

$$
2g^2\int_q
e^{,i w\cdot (p_2-q)}
\frac{(q-p_2)^{+\dot\beta}}{(q^2+M^2)\big((q-p_2)^2+M^2\big)},\mathscr F_{12}^{\dot\beta}{}^i{}_j{}^k{}_l
$$

$$
\qquad-2g^2M^2\int_qe^{,i w\cdot (p_2-q)}\frac{(q-p_2)^{+\dot\beta}}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)},\mathscr F_{12}^{\dot\beta}{}^i{}_j{}^k{}_l.
$$

前一项 (=) contact/EOM。后一项 (=) anomaly：

$$
\Gamma_{12;M}^{(\rm anom)}=-2g^2M^2\int_q
e^{,i w\cdot (p_2-q)}
\frac{(q-p_2)^{+\dot\beta}}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)},\mathscr F_{12}^{\dot\beta}.
$$

Feynman parameter：

$$
\frac{1}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}
$$

$$
2\int_\Delta
\frac{1}{\big[(q+yp_1-zp_2)^2+M^2+\Delta\big]^3},
$$

$$
\int_\Delta := \int_0^1dx\,dy\,dz\,\delta(1-x-y-z),
\qquad
\Delta=xy\,p_1^2+xz\,p_2^2+yz\,p^2.
$$

令

$$
\ell=q+yp_1-zp_2,
\qquad
q-p_2=\ell-Y_{12},
\qquad
Y_{12}:= y\,p_1+(x+y)\,p_2.
$$

则

$$
e^{,i w\cdot(p_2-q)}=e^{,i w\cdot Y_{12}}e^{-i w\cdot \ell}.
$$

而

$$
\int_\ell e^{-i w\cdot \ell},\ell_{+\dot\alpha_1}\cdots \ell_{+\dot\alpha_n}F(\ell^2)=0,
\qquad n\ge 1,
$$

因为 tensor reduction 必含 $(\epsilon_{\alpha\beta})$，而这里所有 undotted index 都是 $(+)$，故 $(\epsilon_{++}=0)$。

于是只剩 shift piece：

$$
\Gamma_{12;M}^{(\rm anom)}
$$

$$
4g^2M^2\int_\Delta
 e^{,i w\cdot Y_{12}},
 Y_{12,+\dot\beta}
\int_\ell\frac{1}{(\ell^2+M^2+\Delta)^3}
,
\mathscr F_{12}^{\dot\beta}.
$$

$$
\int_\ell\frac{1}{(\ell^2+\Omega)^3}=\frac{1}{32\pi^2}\frac{1}{\Omega}.
$$

故 local part：

$$
\boxed{\Gamma_{12}^{(\rm anom,loc)}{}^i{}_j{}^k{}_l(w)
-
\frac{g^2}{8\pi^2}
\int_\Delta
 e^{,i w\cdot Y_{12}},
 Y_{12,+\dot\beta},
 \mathscr F_{12}^{\dot\beta}{}^i{}_j{}^k{}_l
}.
$$

#### **Pattern 21**

完全平行：

$$
Y_{21}:=(x+y)\,p_1+y\,p_2.
$$

$$
\boxed{\Gamma_{21}^{(\rm anom,loc)}{}^i{}_j{}^k{}_l(w)
-
\frac{g^2}{8\pi^2}
\int_\Delta
 e^{,i w\cdot Y_{21}},
 Y_{21,+\dot\beta},
 \mathscr F_{21}^{\dot\beta}{}^i{}_j{}^k{}_l
}.
$$

#### **Open-index final result**

$$
\boxed{\mathcal I![Q_1!\Big(f_{++},e^{,w\cdot \nabla_+}f_{++}\Big)_{\rm loop}^{(1),\rm loc}{}^i{}_j{}^k{}_l(p)
-
\frac{g^2}{8\pi^2}
\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)
\Big[
\mathcal G_{12,+\dot\beta}(w;p_1,p_2),\mathscr F_{12}^{\dot\beta}{}^i{}_j{}^k{}_l+\mathcal G_{21,+\dot\beta}(w;p_1,p_2),\mathscr F_{21}^{\dot\beta}{}^i{}_j{}^k{}_l
\Big].
}
$$

其中

$$
\mathcal G_{12,+\dot\beta}(w;p_1,p_2):=\int_\Delta e^{,i w\cdot Y_{12}},Y_{12,+\dot\beta},\qquad\mathcal G_{21,+\dot\beta}(w;p_1,p_2):=\int_\Delta e^{,i w\cdot Y_{21}},Y_{21,+\dot\beta}.
$$

这已经是 exact compact form。(w=0) 立即回到已知

$$
\mathcal G_{12,+\dot\beta}(0)=\frac16(p_1+2p_2)^{+\dot\beta},\qquad \mathcal G_{21,+\dot\beta}(0)=\frac16(2p_1+p_2)^{+\dot\beta},
$$

所以

$$
\mathcal I[Q_1(f_{++}f_{++})]
-
\frac{g^2}{48\pi^2}
\int_{p_1,p_2}\delta^{(4)}(p-p_1-p_2)
\Big[
(p_1+2p_2)^{+\dot\beta}\mathscr F_{12}^{\dot\beta}
+
(2p_1+p_2)^{+\dot\beta}\mathscr F_{21}^{\dot\beta}
\Big].
$$

#### **closed form for the generating kernel**

记

$$
u_1:= i\,w\cdot p_1,\qquad \nu_2:= i\,w\cdot p_2.
$$

定义 scalar kernels

$$
\mathcal K_{12}(\nu_1,\nu_2):=\int_\Delta e^{,y \nu_1+(x+y)\nu_2}
\frac{\nu_1+\nu_2 e^{\nu_1+\nu_2}-(\nu_1+\nu_2)e^{\nu_2}}{\nu_1\nu_2(\nu_1+\nu_2)},
$$

$$
\mathcal K_{21}(\nu_1,\nu_2):=\int_\Delta e^{,(x+y)\nu_1+y \nu_2}
\frac{\nu_2+\nu_1 e^{\nu_1+\nu_2}-(\nu_1+\nu_2)e^{\nu_1}}{\nu_1\nu_2(\nu_1+\nu_2)}.
$$

则

$$
\mathcal G_{12,+\dot\beta}
\frac1{i},\frac{\partial \mathcal K_{12}}{\partial w^{+\dot\beta}},\qquad\mathcal G_{21,+\dot\beta}
\frac1{i},\frac{\partial \mathcal K_{21}}{\partial w^{+\dot\beta}}.
$$

#### **(w)-power expansion**

$$
\mathcal G_{12,+\dot\beta}
\sum_{n\ge0}\frac{i^n}{n!},w^{+\dot\alpha_1}\cdots w^{+\dot\alpha_n}\int_\Delta Y_{12,+\dot\alpha_1}\cdots Y_{12,+\dot\alpha_n}Y_{12,+\dot\beta},
$$

$$
\mathcal G_{21,+\dot\beta}
\sum_{n\ge0}\frac{i^n}{n!},
 w^{+\dot\alpha_1}\cdots w^{+\dot\alpha_n}
\int_\Delta
Y_{21,+\dot\alpha_1}\cdots Y_{21,+\dot\alpha_n}Y_{21,+\dot\beta}.
$$

前两阶：

$$
\mathcal G_{12,+\dot\beta}
\frac16(p_1+2p_2)^{+\dot\beta}+\frac{i}{12},w^{+\dot\theta},\Xi_{12,+\dot\theta,+\dot\beta}+O(w^2),
$$

$$
\mathcal G_{21,+\dot\beta}
\frac16(2p_1+p_2)^{+\dot\beta}+\frac{i}{12},w^{+\dot\theta},\Xi_{21,+\dot\theta,+\dot\beta}+O(w^2),
$$

其中

$$
\Xi_{12,+\dot\theta,+\dot\beta}
 p_{1,+\dot\theta}p_{1,+\dot\beta}+3p_{1,+(\dot\theta}p_{2,+\dot\beta)}+3p_{2,+\dot\theta}p_{2,+\dot\beta},
$$

$$
\Xi_{21,+\dot\theta,+\dot\beta}
3p_{1,+\dot\theta}p_{1,+\dot\beta}+3p_{1,+(\dot\theta}p_{2,+\dot\beta)}+p_{2,+\dot\theta}p_{2,+\dot\beta}.
$$

所以

$$
\mathcal I![Q_1!\Big(f_{++}e^{,w\cdot \nabla_+}f_{++}\Big)_{\rm loop}^{(1),\rm loc}]
-
\frac{g^2}{48\pi^2}\Big[(p_1+2p_2)^{+\dot\beta}\mathscr F_{12}^{\dot\beta}
+(2p_1+p_2)^{+\dot\beta}\mathscr F_{21}^{\dot\beta}\Big]
$$

$$
\qquad
-\frac{i g^2}{96\pi^2},
 w^{+\dot\theta}
\Big[
\Xi_{12,+\dot\theta,+\dot\beta}\mathscr F_{12}^{\dot\beta}
+
\Xi_{21,+\dot\theta,+\dot\beta}\mathscr F_{21}^{\dot\beta}
\Big]
+O(w^2).
$$

#### **Lie-algebra indices (A,B,dots)**

$$
[T^A,T^B]=f^{AB}{}_C,T^C,
\qquad
\operatorname{Tr}(T^AT^B)=\delta^{AB}.
$$

$$
\mathcal O_w^{AB}(x):=
 f_{++}^A(x),e^{,w\cdot \nabla_+}f_{++}^B(x).
$$

$$
\mathscr F_{12}^{AB,\dot\beta}
 f^{CE}{}_A f^{DE}{}_B,f_{++}^C(p_1)\bar\lambda^{\dot\beta D}(p_2),\qquad\mathscr F_{21}^{AB,\dot\beta}
 f^{CE}{}_A f^{DE}{}_B,f_{++}^C(p_2)\bar\lambda^{\dot\beta D}(p_1).
$$

于是

$$
\boxed{\mathcal I![Q_1\mathcal O_w^{AB}(p)]_{\rm loop}^{(1),\rm loc}
-
\frac{g^2}{8\pi^2}
\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)
\Big[
\mathcal G_{12,+\dot\beta}(w;p_1,p_2),\mathscr F_{12}^{AB,\dot\beta}
+
\mathcal G_{21,+\dot\beta}(w;p_1,p_2),\mathscr F_{21}^{AB,\dot\beta}
\Big].
}
$$

#### **local-operator rewrite**

formal two-slot derivatives：

$$
\nabla_{+\dot\beta}^{(1)}\big(X(x_1)Y(x_2)\big)
:=
(\nabla_{+\dot\beta}X)(x_1),Y(x_2),
\qquad
\nabla_{+\dot\beta}^{(2)}\big(X(x_1)Y(x_2)\big)
:=
X(x_1),(\nabla_{+\dot\beta}Y)(x_2).
$$

定义

$$
\mathbb D_{12,+\dot\beta}(w)
:=
\int_\Delta
 e^{,w\cdot\big(y\nabla_+^{(1)}+(x+y)\nabla_+^{(2)}\big)}
\Big(y\nabla_{+\dot\beta}^{(1)}+(x+y)\nabla_{+\dot\beta}^{(2)}\Big),
$$

$$
\mathbb D_{21,+\dot\beta}(w)
:=
\int_\Delta
 e^{,w\cdot\big((x+y)\nabla_+^{(1)}+y\nabla_+^{(2)}\big)}
\Big((x+y)\nabla_{+\dot\beta}^{(1)}+y\nabla_{+\dot\beta}^{(2)}\Big).
$$

则 exact local-operator form 可写成

$$
\boxed{Q_1\mathcal O_w^{AB}(x)\Big\|_{\rm loop}^{(1),\rm loc}
\frac{i g^2}{8\pi^2},
 f^{CE}{}_A f^{DE}{}_B\Big[\mathbb D_{12,+\dot\beta}(w),f_{++}^C(x_1)\bar\lambda^{\dot\beta D}(x_2)+\mathbb D_{21,+\dot\beta}(w),f_{++}^C(x_2)\bar\lambda^{\dot\beta D}(x_1)\Big]_{x_1=x_2=x}.
}
$$

这就是 compact generating-function form。

# $Q_1(e^{w\nabla}f_{++} f_{++})$

这次只比上一条多一件事：指数放在 **第一 slot**。

$$
w\cdot\nabla_+ := w^{+\dot\alpha}\nabla_{+\dot\alpha},\qquad
w\cdot p_a := w^{+\dot\alpha}p_{a,+\dot\alpha}.
$$

$$
\mathcal O_w{}^i{}_j{}^k{}_l(x):=\big(e^{w\cdot\nabla_+}f_{++}\big)^i{}_j(x),f_{++}^k{}_l(x).
$$

只保留 loop-focus：

$$
Q_1\mathcal O_w
$$

tree pieces 全部略去。

$$
\mathscr F_{21}^{\dot\beta}(p_1,p_2)=\mathscr F_{12}^{\dot\beta}(p_2,p_1).
$$

**Pattern 12**

对应的 PV triangle 只是在 $(Q_1(f_{++}f_{++}))$ 的 12 图上多了第一 slot 的 phase

$$
e^{i w\cdot r},\qquad r=q+p_1.
$$

所以

$$
\Gamma_{12;M}^{\rm PV\text{-}loop}{}^i{}_j{}^k{}_l(w)
$$

前一项 $(=)$ contact/EOM。

后一项 $(=)$ anomaly。

**Pattern 21**

完全平行。

$$
X_{21}:=z p_1+(x+z)p_2,\qquad
Y_{21}:=(x+y)p_1+y p_2.
$$

$$
\boxed{\Gamma_{21}^{(\rm anom,loc)}{}^i{}_j{}^k{}_l(w)}
$$

**Open-index final result**

定义

$$
\widehat{\mathcal G}_{12,+\dot\beta}(w;p_1,p_2):=\int_\Delta e^{i w\cdot X_{12}},Y_{12,+\dot\beta},\qquad\widehat{\mathcal G}_{21,+\dot\beta}(w;p_1,p_2):=\int_\Delta e^{i w\cdot X_{21}},Y_{21,+\dot\beta}.
$$

这已经是 exact compact form。

**(w=0) check**

$$
\widehat{\mathcal G}_{12,+\dot\beta}(0)=\frac16(p_1+2p_2)_{+\dot\beta},\qquad
\widehat{\mathcal G}_{21,+\dot\beta}(0)=\frac16(2p_1+p_2)_{+\dot\beta}.
$$

**closed scalar kernel**

$$
u_1:=i w\cdot p_1,\qquad u_2:=i w\cdot p_2.
$$

$$
\widehat{\mathcal K}_{12}(u_1,u_2):=\int_\Delta e^{(x+z)u_1+z u_2}
\frac{u_2+u_1 e^{u_1+u_2}-(u_1+u_2)e^{u_1}}{u_1u_2(u_1+u_2)},
$$

$$
\widehat{\mathcal K}_{21}(u_1,u_2):=\int_\Delta e^{z u_1+(x+z)u_2}
\frac{u_1+u_2 e^{u_1+u_2}-(u_1+u_2)e^{u_2}}{u_1u_2(u_1+u_2)}.
$$

**Lie-algebra indices** $(A,B,\dots)$

$$
[T^A,T^B]=f^{AB}{}_C T^C,\qquad
\operatorname{Tr}(T^A T^B)=\delta^{AB}.
$$

$$
\boxed{\mathcal I\big[Q_1\mathcal O_w^{AB}(p)\big]_{\rm loop}^{(1),\rm loc}}
$$

**local operator rewrite**

$$
\widehat{\mathbb D}_{12,+\dot\beta}(w):=\int_\Delta e^{w\cdot\big((x+z)\nabla_+^{(1)}+z\nabla_+^{(2)}\big)}\Big(y\nabla_{+\dot\beta}^{(1)}+(x+y)\nabla_{+\dot\beta}^{(2)}\Big),
$$

$$
\widehat{\mathbb D}_{21,+\dot\beta}(w):=\int_\Delta e^{w\cdot\big(z\nabla_+^{(1)}+(x+z)\nabla_+^{(2)}\big)}\Big((x+y)\nabla_{+\dot\beta}^{(1)}+y\nabla_{+\dot\beta}^{(2)}\Big).
$$

这就是最紧凑的 generating-function 形式。

# $Q_1（f_{++} e^{w\nabla}\bar\lambda_{\dot\beta}）$（Exactly same with HT)

把第二个 factor 的自由 dotted index 记成 $dotbeta$，并取

$$
w\cdot\nabla_+ := w^{+\dot\alpha}\nabla_{+\dot\alpha},
\qquad
w\cdot p_a := w^{+\dot\alpha}p_{a,+\dot\alpha}.
$$

$$
\mathcal O_{w,\dot\beta}{}^{i}{}_{j}{}^{k}{}_{l}(x)
:= f_{++}{}^{i}{}_{j}(x)\,\Big( e^{\,w\cdot\nabla_+}\bar\lambda_{\dot\beta}\Big){}^{k}{}_{l}(x).
$$

沿用当前页的 $(Q_-)$、propagators、$(V_{Alambdabarlambda}=V_L-V_R)$、PV collapse identity、以及同一个 $(mathscr C_{12},mathscr C_{21})$。

这里只保留 loop-focus：

$$
Q_1\mathcal O_{w,\dot\beta}
\;\underbrace{\big\{ i\nabla_{+\dot\rho}\bar\lambda^{\dot\rho},\; e^{\,w\cdot\nabla_+}\bar\lambda_{\dot\beta}\big\}}_{\text{loop/anomaly}}
+\underbrace{\big\{ f_{++},\; Q_-\!\big(e^{\,w\cdot\nabla_+}\bar\lambda_{\dot\beta}\big)\big\}}_{\text{tree from }[Q_-,\nabla_+] }.
$$

因为

$$
Q_-\bar\lambda_{\dot\beta}=0,
$$

第二项在你关心的 sector 里只给 tree-level commutator pieces，不给 loop anomaly。

## two-field triangle insertion

$$
\mathcal O_{w,\dot\beta}^{(\partial)}{}^{i}{}_{j}{}^{k}{}_{l}
:= i\partial_{+\dot\rho}\bar\lambda^{\dot\rho}{}^{i}{}_{j}\; e^{\,w\cdot\partial_+}\bar\lambda_{\dot\beta}{}^{k}{}_{l}.
$$

动量空间：

$$
\mathcal I\!\left[\mathcal O_{w,\dot\beta}^{(\partial)}(p)\right]
= \int_{r,s}(2\pi)^4\delta^{(4)}(p-r-s)\,(-r_{+\dot\rho})\,e^{i w\cdot s}\,\bar\lambda^{\dot\rho}(r)\bar\lambda_{\dot\beta}(s).
$$

## Pattern 12

routing：

$$
r=q+p_1,\qquad s=p_2-q,\qquad p=p_1+p_2.
$$

PV-loop 直接写成

$$
\Gamma_{12;M}^{\rm PV\text{-}loop}{}^{i}{}_{j}{}^{k}{}_{l}(w)
=2g^2\int_q
 e^{i w\cdot(p_2-q)}
\frac{(q-p_2)_{+\dot\beta}}{(q^2+M^2)\big((q-p_2)^2+M^2\big)}\,\mathscr C_{12}{}^{i}{}_{j}{}^{k}{}_{l}
$$

$$
\qquad
-2g^2M^2\int_q e^{i w\cdot(p_2-q)}
\frac{(q-p_2)_{+\dot\beta}}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}\,\mathscr C_{12}{}^{i}{}_{j}{}^{k}{}_{l}.
$$

regulated splitting 仍写成

$$
\Gamma_{12}^{\rm reg}(w)
=\Big(\Gamma_{12}^{(0)}(w)-\Gamma_{12;M}^{(0)}(w)\Big)+\Gamma_{12;M}^{(\rm anom)}(w),
$$

其中 anomalous sector 取

$$
\Gamma_{12;M}^{(\rm anom)}(w)
=2g^2M^2\int_q
 e^{i w\cdot(p_2-q)}
\frac{(q-p_2)_{+\dot\beta}}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}\,\mathscr C_{12}.
$$

### Feynman parameter

$$
\frac{1}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}
=2\int_\Delta\frac{1}{\big[(q+y p_1-z p_2)^2+M^2+\Delta\big]^3},
$$

$$
\int_\Delta:=\int_0^1 dx\,dy\,dz\;\delta(1-x-y-z),
\qquad
\Delta=xy\,p_1^2+xz\,p_2^2+yz\,p^2.
$$

令

$$
\ell=q+y p_1-z p_2,
\qquad
q-p_2=\ell-Y_{12},
\qquad
Y_{12}:=y\,p_1+(x+y)\,p_2.
$$

则

$$
e^{i w\cdot(p_2-q)}=e^{i w\cdot Y_{12}}\,e^{-i w\cdot\ell}.
$$

所有含 $\ell$ 的 moments 全部消失：

$$
\int_\ell e^{-i w\cdot\ell}\,\ell_{+\dot\alpha_1}\cdots \ell_{+\dot\alpha_n}\,F(\ell^2)=0,\qquad n\ge 1,
$$

因为 tensor reduction 最终必含 $epsilon_{++}=0$。

于是

$$
\Gamma_{12;M}^{(\rm anom)}(w)
=-4g^2M^2\int_\Delta e^{i w\cdot Y_{12}}\,Y_{12,+\dot\beta}
\int_\ell\frac{1}{(\ell^2+M^2+\Delta)^3}\,\mathscr C_{12}.
$$

再用

$$
\int_\ell\frac{1}{(\ell^2+\Omega)^3}=\frac{1}{32\pi^2}\frac{1}{\Omega},
$$

得 local part

$$
\boxed{\Gamma_{12}^{(\rm anom,loc)}{}^{i}{}_{j}{}^{k}{}_{l}(w)
=-\frac{g^2}{8\pi^2}\int_\Delta e^{i w\cdot Y_{12}}\,Y_{12,+\dot\beta}\,\mathscr C_{12}{}^{i}{}_{j}{}^{k}{}_{l}.}
$$

## Pattern 21

完全平行：

$$
Y_{21}:=(x+y)\,p_1+y\,p_2.
$$

$$
\boxed{\Gamma_{21}^{(\rm anom,loc)}{}^{i}{}_{j}{}^{k}{}_{l}(w)
=-\frac{g^2}{8\pi^2}\int_\Delta e^{i w\cdot Y_{21}}\,Y_{21,+\dot\beta}\,\mathscr C_{21}{}^{i}{}_{j}{}^{k}{}_{l}.}
$$

## Open-index final result

定义 exact kernels

$$
\mathcal H_{12,+\dot\beta}(w;p_1,p_2):=\int_\Delta e^{i w\cdot Y_{12}}\,Y_{12,+\dot\beta},
\qquad
\mathcal H_{21,+\dot\beta}(w;p_1,p_2):=\int_\Delta e^{i w\cdot Y_{21}}\,Y_{21,+\dot\beta}.
$$

则

$$
\boxed{\mathcal I\!\left[Q_1\!\Big(f_{++}\,e^{\,w\cdot\nabla_+}\bar\lambda_{\dot\beta}\Big)_{\rm loop}^{(1),\rm loc}{}^{i}{}_{j}{}^{k}{}_{l}(p)\right]
=-\frac{g^2}{8\pi^2}\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)
\Big[\mathcal H_{12,+\dot\beta}\,\mathscr C_{12}{}^{i}{}_{j}{}^{k}{}_{l}+\mathcal H_{21,+\dot\beta}\,\mathscr C_{21}{}^{i}{}_{j}{}^{k}{}_{l}\Big].}
$$

这里 $(\mathscr C_{12},\mathscr C_{21})$ 就是你当前页已经在用的那一对 color-flow tensors。

## exact scalar kernel

记

$$
u_1:= i\,w\cdot p_1,\qquad \nu_2:= i\,w\cdot p_2.
$$

定义

$$
\mathcal K_{12}(\nu_1,\nu_2):=\int_\Delta e^{y\nu_1+(x+y)\nu_2}
\frac{\nu_1+\nu_2 e^{\nu_1+\nu_2}-(\nu_1+\nu_2)e^{\nu_2}}{\nu_1\nu_2(\nu_1+\nu_2)},
$$

$$
\mathcal K_{21}(\nu_1,\nu_2):=\int_\Delta e^{(x+y)\nu_1+y\nu_2}
\frac{\nu_2+\nu_1 e^{\nu_1+\nu_2}-(\nu_1+\nu_2)e^{\nu_1}}{\nu_1\nu_2(\nu_1+\nu_2)}.
$$

则

$$
\mathcal H_{12,+\dot\beta}=\frac{1}{i}\frac{\partial \mathcal K_{12}}{\partial w^{+\dot\beta}},
\qquad
\mathcal H_{21,+\dot\beta}=\frac{1}{i}\frac{\partial \mathcal K_{21}}{\partial w^{+\dot\beta}}.
$$

这就是最紧凑的 generating-function 形式。

## $(w)$-级数

$$
\mathcal H_{12,+\dot\beta}
=\sum_{n\ge 0}\frac{i^n}{n!}\,w^{+\dot\alpha_1}\cdots w^{+\dot\alpha_n}
\int_\Delta Y_{12,+\dot\alpha_1}\cdots Y_{12,+\dot\alpha_n}Y_{12,+\dot\beta},
$$

$$
\mathcal H_{21,+\dot\beta}
=\sum_{n\ge 0}\frac{i^n}{n!}\,w^{+\dot\alpha_1}\cdots w^{+\dot\alpha_n}
\int_\Delta Y_{21,+\dot\alpha_1}\cdots Y_{21,+\dot\alpha_n}Y_{21,+\dot\beta}.
$$

前两阶：

$$
\mathcal H_{12,+\dot\beta}
=\frac16(p_1+2p_2)_{+\dot\beta}+\frac{i}{12}\,w^{+\dot\theta}\,\Xi_{12,+\dot\theta,+\dot\beta}+O(w^2),
$$

$$
\mathcal H_{21,+\dot\beta}
=\frac16(2p_1+p_2)_{+\dot\beta}+\frac{i}{12}\,w^{+\dot\theta}\,\Xi_{21,+\dot\theta,+\dot\beta}+O(w^2),
$$

其中

$$
\Xi_{12,+\dot\theta,+\dot\beta}
=p_{1,+\dot\theta}p_{1,+\dot\beta}+3p_{1,+(\dot\theta}p_{2,+\dot\beta)}+3p_{2,+\dot\theta}p_{2,+\dot\beta},
$$

$$
\Xi_{21,+\dot\theta,+\dot\beta}
=3p_{1,+\dot\theta}p_{1,+\dot\beta}+3p_{1,+(\dot\theta}p_{2,+\dot\beta)}+p_{2,+\dot\theta}p_{2,+\dot\beta}.
$$

因此

$$
\mathcal I\!\left[Q_1\!\Big(f_{++}e^{\,w\cdot\nabla_+}\bar\lambda_{\dot\beta}\Big)_{\rm loop}^{(1),\rm loc}\right]
=-\frac{g^2}{48\pi^2}\Big[(p_1+2p_2)_{+\dot\beta}\,\mathscr C_{12}+(2p_1+p_2)_{+\dot\beta}\,\mathscr C_{21}\Big]
$$

$$
\qquad
-\frac{i g^2}{96\pi^2}\,w^{+\dot\theta}
\Big[\Xi_{12,+\dot\theta,+\dot\beta}\,\mathscr C_{12}+\Xi_{21,+\dot\theta,+\dot\beta}\,\mathscr C_{21}\Big]
+O(w^2).
$$

$(w=0)$ 与 $O(w)$ 分别正好退化到当前页已经算过的 $Q_1(f_{++}barlambda_{dotbeta})$、$Q_1(f_{++}nabla_{+dottheta}barlambda_{dotbeta})$ 结果。

## Lie-algebra rewrite

定义

$$
\mathcal O_{w,\dot\beta}^{AB}(x)
:= f_{++}^A(x)\,\Big(e^{\,w\cdot\nabla_+}\bar\lambda_{\dot\beta}^B\Big)(x),
\qquad
[T^A,T^B]=f^{AB}{}_C\,T^C,
\qquad
\operatorname{Tr}(T^A T^B)=\delta^{AB}.
$$

$$
\mathscr C_{12}^{AB}(p_1,p_2)
=\epsilon^{\dot\gamma\dot\delta}\,f^{CA}{}_E f^{DB}{}_E\,\bar\lambda_{\dot\gamma}^C(p_1)\bar\lambda_{\dot\delta}^D(p_2),
\qquad
\mathscr C_{21}^{AB}(p_1,p_2)=\mathscr C_{12}^{AB}(p_2,p_1).
$$

于是

$$
\boxed{\mathcal I\!\left[Q_1\mathcal O_{w,\dot\beta}^{AB}(p)\right]_{\rm loop}^{(1),\rm loc}
=-\frac{g^2}{8\pi^2}\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)
\Big[\mathcal H_{12,+\dot\beta}\,\mathscr C_{12}^{AB}+\mathcal H_{21,+\dot\beta}\,\mathscr C_{21}^{AB}\Big].}
$$

再把第二项重命名 $(p_1leftrightarrow p_2)$，并用 $mathcal H_{21}(w;p_2,p_1)=mathcal H_{12}(w;p_1,p_2)$，得到更紧凑的形式

$$
\boxed{\mathcal I\!\left[Q_1\mathcal O_{w,\dot\beta}^{AB}(p)\right]_{\rm loop}^{(1),\rm loc}
=-\frac{g^2}{4\pi^2}\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)\,\mathcal H_{12,+\dot\beta}(w;p_1,p_2)\,\mathscr C_{12}^{AB}(p_1,p_2).}
$$

## local operator rewrite

定义 bilocal two-slot differential operator

$$
\nabla_{+\dot\beta}^{(1)}\big(X(x_1)Y(x_2)\big):=(\nabla_{+\dot\beta}X)(x_1)\,Y(x_2),
\qquad
\nabla_{+\dot\beta}^{(2)}\big(X(x_1)Y(x_2)\big):=X(x_1)\,(\nabla_{+\dot\beta}Y)(x_2).
$$

再定义

$$
\mathbb H_{+\dot\beta}(w)
:=\int_\Delta
 e^{\,w\cdot\big(y\nabla_+^{(1)}+(x+y)\nabla_+^{(2)}\big)}
\Big(y\nabla_{+\dot\beta}^{(1)}+(x+y)\nabla_{+\dot\beta}^{(2)}\Big).
$$

则 exact local form 可写成

$$
\boxed{Q_1\mathcal O_{w,\dot\beta}^{AB}(x)\Big\|_{\rm loop}^{(1),\rm loc}
=\frac{i g^2}{4\pi^2}\,\mathbb H_{+\dot\beta}(w)\,
\Big[\epsilon^{\dot\gamma\dot\delta}\,f^{CA}{}_E f^{DB}{}_E\,\bar\lambda_{\dot\gamma}^C(x_1)\bar\lambda_{\dot\delta}^D(x_2)\Big]_{x_1=x_2=x}.}
$$

