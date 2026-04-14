---
title: "Q_1 triangle seed: F_raw F_raw"
doc_type: calculation
theory: "N=4 SYM ordinary-space"
loop_order: 1
supercharge: "Q_-^4"
regularization: DR
status: momentum_space_rewrite
---

# Q_1 triangle seed: \(F_{\rm raw}F_{\rm raw}\)

## Step 1: Operator / classical target / one-loop basis

$$
\mathcal O_{FF}^{AB}(p)
:=
\int_{p_1,p_2}
F_{\rm raw}^A(p_1)\,
F_{\rm raw}^B(p_2)\,
\delta_{p-p_1-p_2}.
$$

$$
Q_1F_{\rm raw}
=
i\,\nabla_{+\dot\alpha}\bar\Lambda^{\dot\alpha}.
$$

$$
\boxed{
Q_1^{\rm cl}\mathcal O_{FF}^{AB}(p)
=
\int_{p_1,p_2}\delta_{p-p_1-p_2}
\Big[
i\,p_{1,+\dot\alpha}\,\bar\Lambda^{A\dot\alpha}(p_1)\,F_{\rm raw}^B(p_2)
+
F_{\rm raw}^A(p_1)\,i\,p_{2,+\dot\alpha}\,\bar\Lambda^{B\dot\alpha}(p_2)
\Big]
}
$$

$$
\mathcal K_{F\bar\Lambda,12}^{AB,\dot\alpha}(p_1,p_2)
:=
f^{CE}{}_{A}f^{DE}{}_{B}\,
F_{\rm raw}^C(p_1)\,\bar\Lambda^{D\dot\alpha}(p_2),
\qquad
\mathcal K_{F\bar\Lambda,21}^{AB,\dot\alpha}(p_1,p_2)
:=
\mathcal K_{F\bar\Lambda,12}^{AB,\dot\alpha}(p_2,p_1),
$$

$$
\mathcal K_{\Psi X,12}^{AB}(p_1,p_2)
:=
f^{CE}{}_{A}f^{DE}{}_{B}\,
X_i^C(p_1)\,\Psi_+^{iD}(p_2),
\qquad
\mathcal K_{\Psi X,21}^{AB}(p_1,p_2)
:=
\mathcal K_{\Psi X,12}^{AB}(p_2,p_1).
$$

## Step 2: Two genuine Wick-contraction classes

在当前 \(Q_1\) projection 下，与
$$
Q_1(F^A_{\rm raw}F^B_{\rm raw})
$$
有关的 genuine one-loop triangle contractions 只有两大类：

$$
\boxed{
\text{Class I: }
J_F^{(2)} \times S_{A\Lambda\bar\Lambda}^{(3)}
\quad\Longrightarrow\quad
(\nabla F)\bar\Lambda
}
$$

$$
\boxed{
\text{Class II: }
J_F^{(3)} \times S_{X\Lambda\Psi}^{(3)}
\quad\Longrightarrow\quad
(\nabla\Psi)(\nabla X)
}
$$

每一类都要保留两种 ordered routings：
$$
[1|2],\ [2|1]
\qquad\text{or}\qquad
[1,2],\ [2,1].
$$

## Step 3: Three-propagator triangle integrals

总体起点统一写成
$$
\boxed{
\left\langle
\mathcal O_{FF}^{AB}(p)\,
\int_k i\,k_\mu J_F^\mu(-k)\,
\int d^dz\,\big(-\mathcal L_{\rm int}^{(3)}(z)\big)
\right\rangle_0.
}
$$

### Step 3.1: Class I

定义
$$
\Gamma_{F\bar\Lambda}^{AB}(p)
:=
\Gamma_{F\bar\Lambda,12}^{AB}(p)
+
\Gamma_{F\bar\Lambda,21}^{AB}(p).
$$

取 ordered representative
$$
\mathcal O_{[1|2]}^{AB}(p)
:=
\int_{p_1,p_2}\delta_{p-p_1-p_2}\,
F_{\rm raw}^{A}(p_1)\,F_{\rm raw}^{(2),B}(p_2),
$$

$$
F_{\rm raw}^{(2),B}(p_2)
=
-i\int_{r,s}\delta_{p_2-r-s}\,
[A_{+\dot\alpha}(r),A_+^{\dot\alpha}(s)]^B.
$$

current quadratic branch 写成
$$
J_F^{(2)\mu}(k)
=
-\frac{1}{g_{\rm YM}^2}
\int_{q_1,q_2}
\delta_{k-q_1-q_2}\,
f_{+-}^{(1)}(q_1)\,
\sigma^{\mu-\dot\alpha}\bar\Lambda_{\dot\alpha}(q_2).
$$

因此
$$
i\,k_\mu J_F^{(2)\mu}(-k)
=
-\frac{i}{g_{\rm YM}^2}
\int_{q_1,q_2}
\delta_{-k-q_1-q_2}\,
k_\mu\,
f_{+-}^{(1)}(q_1)\,
\sigma^{\mu-\dot\alpha}\bar\Lambda_{\dot\alpha}(q_2).
$$

interaction vertex 取
$$
\int d^dz\,\big(-\mathcal L_{A\Lambda\bar\Lambda}^{(3)}(z)\big)
=
\frac{1}{g_{\rm YM}^2}
\int_{u,v,w}
\delta_{u+v+w}\,
A_{-\dot\beta}(u)\Lambda_-(v)\bar\Lambda^{\dot\beta}(w).
$$

于是第一种 routing 的真正 Wick contraction 先写成
$$
\boxed{
\Gamma_{F\bar\Lambda,12}^{AB}(p)
=
\left\langle
\mathcal O_{[1|2]}^{AB}(p)\,
\int_k i\,k_\mu J_F^{(2)\mu}(-k)\,
\int d^dz\,\big(-\mathcal L_{A\Lambda\bar\Lambda}^{(3)}(z)\big)
\right\rangle_0 .
}
$$

把三个插入全部展开后，保留这一个 contraction pattern：
$$
\langle \bar\Lambda(q_2)\Lambda_-(v)\rangle_0,\qquad
\langle f_{+-}^{(1)}(q_1)A_{+\dot\alpha}(r)\rangle_0,\qquad
\langle A_{-\dot\beta}(u)A_+^{\dot\alpha}(s)\rangle_0.
$$

所以
$$
\boxed{
\Gamma_{F\bar\Lambda,12}^{AB}(p)
=
\int_{p_1,p_2}\delta_{p-p_1-p_2}\,F_{\rm raw}^A(p_1)
\int_{r,s}\delta_{p_2-r-s}
\int_{q_1,q_2}\delta_{-k-q_1-q_2}
\int_{u,v,w}\delta_{u+v+w}
}
$$

$$
\boxed{
\qquad\qquad
\times
\langle f_{+-}^{(1)}(q_1)A_{+\dot\alpha}(r)\rangle_0\,
\langle A_{-\dot\beta}(u)A_+^{\dot\alpha}(s)\rangle_0\,
\langle \bar\Lambda^{\dot\beta}(q_2)\Lambda_-(v)\rangle_0\,
\bar\Lambda^{B}(w).
}
$$

用 propagators
$$
\langle f_{+-}^{(1)}(q_1)A_{+\dot\alpha}(r)\rangle_0
=
-i g_{\rm YM}^2\,\frac{q_{1,+\dot\alpha}}{q_1^2}\,\delta_{q_1+r},
$$

$$
\langle A_{-\dot\beta}(u)A_+^{\dot\alpha}(s)\rangle_0
=
-2 g_{\rm YM}^2\,\frac{\delta_{\dot\beta}^{\dot\alpha}}{u^2}\,\delta_{u+s},
$$

$$
\langle \bar\Lambda^{\dot\beta}(q_2)\Lambda_-(v)\rangle_0
=
-i g_{\rm YM}^2\,\frac{v_-{}^{\dot\beta}}{v^2}\,\delta_{q_2+v},
$$
得
$$
\boxed{
\Gamma_{F\bar\Lambda,12}^{AB}(p)
=
-2 g_{\rm YM}^2
\int_{p_1,p_2}\delta_{p-p_1-p_2}\,
\mathcal K_{F\bar\Lambda,12}^{AB,\dot\alpha}(p_1,p_2)
\int_q^d
\frac{\widehat q^2\,(q-p_2)_{+\dot\alpha}}
{q^2(q+p_1)^2(q-p_2)^2}.
}
$$

做完三条 propagators 与所有 vertex \(\delta\)-函数后，只剩一个 loop momentum \(q\)，于是得到 evanescent 三角积分
$$
\boxed{
\Gamma_{F\bar\Lambda,12}^{AB,{\rm ev}}(p)
=
-2g_{\rm YM}^2
\int_{p_1,p_2}\delta_{p-p_1-p_2}\,
\mathcal K_{F\bar\Lambda,12}^{AB,\dot\alpha}(p_1,p_2)\,
\int_q^d
\frac{\widehat q^2\,(q-p_2)_{+\dot\alpha}}
{q^2\,(q+p_1)^2\,(q-p_2)^2}.
}
$$

第一种 routing：
$$
\boxed{
\Gamma_{F\bar\Lambda,12}^{AB,{\rm ev}}(p)
=
-2g_{\rm YM}^2
\int_{p_1,p_2}\delta_{p-p_1-p_2}\,
\mathcal K_{F\bar\Lambda,12}^{AB,\dot\alpha}(p_1,p_2)\,
\int_q^d
\frac{\widehat q^2\,(q-p_2)_{+\dot\alpha}}
{q^2\,(q+p_1)^2\,(q-p_2)^2}.
}
$$

第二种 routing：
$$
\boxed{
\Gamma_{F\bar\Lambda,21}^{AB,{\rm ev}}(p)
=
-2g_{\rm YM}^2
\int_{p_1,p_2}\delta_{p-p_1-p_2}\,
\mathcal K_{F\bar\Lambda,21}^{AB,\dot\alpha}(p_1,p_2)\,
\int_q^d
\frac{\widehat q^2\,(q-p_2)_{+\dot\alpha}}
{q^2\,(q+p_1)^2\,(q-p_2)^2}.
}
$$

这里三条 propagators 分别对应
$$
\langle \bar\Lambda\,\Lambda\rangle,\qquad
\langle f^{(1)}_{+-}\,A_+\rangle,\qquad
\langle A_-\,A_+\rangle.
$$

这里的双 color tensor 来自两处：
\[
f^{CE}{}_{B}\ \text{来自}\ F_{\rm raw}^{(2),B}\sim [A,A]^B,
\qquad
f^{DE}{}_{B}\ \text{与 current / vertex contraction 合并后组成}\ 
f^{CE}{}_{A}f^{DE}{}_{B}.
\]

### Step 3.2: Class II

定义
$$
\Gamma_{\Psi X}^{AB}(p)
:=
\Gamma_{\Psi X,12}^{AB}(p)
+
\Gamma_{\Psi X,21}^{AB}(p).
$$

取 ordered representative
$$
\mathcal O_{[1,2]}^{AB}(p)
:=
\int_{p_1,p_2}\delta_{p-p_1-p_2}\,
F_{\rm raw}^{(1),A}(p_1)\,F_{\rm raw}^{(1),B}(p_2),
$$

$$
F_{\rm raw}^{(1)}(p)
=
i\,p_{+\dot\alpha}A_+^{\dot\alpha}(p).
$$

current cubic branch 写成
$$
J_F^{(3)\mu}(k)
=
\frac{i}{2g_{\rm YM}^2}
\int_{q_1,q_2,q_3}
\delta_{k-q_1-q_2-q_3}\,
[A_\rho(q_1),A_\sigma(q_2)]\,
(\sigma^{\rho\sigma}\sigma^\mu\bar\Lambda(q_3))_-.
$$

因此
$$
i\,k_\mu J_F^{(3)\mu}(-k)
=
\frac{i}{2g_{\rm YM}^2}
\int_{q_1,q_2,q_3}
\delta_{-k-q_1-q_2-q_3}\,
i\,k_\mu\,
[A_\rho(q_1),A_\sigma(q_2)]\,
(\sigma^{\rho\sigma}\sigma^\mu\bar\Lambda(q_3))_-.
$$

把 \(k_\mu\) 按 Leibniz rule 拆成
$$
\boxed{
i\,k_\mu J_F^{(3)\mu}(-k)
=
\frac{i}{2g_{\rm YM}^2}
\int_{q_1,q_2,q_3}
\delta_{-k-q_1-q_2-q_3}
\Big[
i(q_1+q_2)_\mu\,[A_\rho(q_1),A_\sigma(q_2)](\sigma^{\rho\sigma}\sigma^\mu\bar\Lambda(q_3))_-
}
$$

$$
\boxed{
\qquad\qquad
+
[A_\rho(q_1),A_\sigma(q_2)]\,i q_{3\mu}(\sigma^{\rho\sigma}\sigma^\mu\bar\Lambda(q_3))_-
\Big].
}
$$

在当前 triangle channel 里，只保留第二项
$$
[A,A]\nabla_\mu\bar\Lambda
$$
对应的分支；第一项
$$
\nabla_\mu([A,A])\,\bar\Lambda
$$
不进入这里要抽取的 local remainder。

interaction vertex 取
$$
\int d^dz\,\big(-\mathcal L_{X\Lambda\Psi}^{(3)}(z)\big)
=
-\frac{\sqrt2\,i}{g_{\rm YM}^2}
\int_{u,v,w}
\delta_{u+v+w}\,
X_i(u)\Lambda_-(v)\Psi_+^i(w).
$$

所以真正的三角图起点是
$$
\boxed{
\Gamma_{\Psi X,12}^{AB}(p)
=
\left\langle
\mathcal O_{[1,2]}^{AB}(p)\,
\int_k i\,k_\mu J_F^{(3)\mu}(-k)\,
\int d^dz\,\big(-\mathcal L_{X\Lambda\Psi}^{(3)}(z)\big)
\right\rangle_0 .
}
$$

把三个插入展开后，保留这一个 contraction pattern：
$$
\langle \bar\Lambda(q_3)\Lambda_-(v)\rangle_0,\qquad
\langle A_-(q_1)F_{\rm raw}^{(1),A}(p_1)\rangle_0,\qquad
\langle A_-(q_2)F_{\rm raw}^{(1),B}(p_2)\rangle_0.
$$

因此
$$
\boxed{
\Gamma_{\Psi X,12}^{AB}(p)
=
\int_{p_1,p_2}\delta_{p-p_1-p_2}
\int_{q_1,q_2,q_3}\delta_{-k-q_1-q_2-q_3}
\int_{u,v,w}\delta_{u+v+w}
}
$$

$$
\boxed{
\qquad\qquad
\times
\langle A_-(q_1)F_{\rm raw}^{(1),A}(p_1)\rangle_0\,
\langle A_-(q_2)F_{\rm raw}^{(1),B}(p_2)\rangle_0\,
\langle \bar\Lambda(q_3)\Lambda_-(v)\rangle_0\,
X_i(u)\Psi_+^i(w).
}
$$

这里取
$$
ik_\mu J_F^{(3)\mu}(-k)
=
\nabla_\mu([A,A])\,\bar\Lambda_-
+
[A,A]\nabla_\mu\bar\Lambda_-,
$$
只保留第二项
$$
[A,A]\nabla_\mu\bar\Lambda_-.
$$

再用 propagators
$$
\langle A_-(q_1)F_{\rm raw}^{(1),A}(p_1)\rangle_0
=
-2i g_{\rm YM}^2\,\frac{p_{1,+\dot\alpha}}{p_1^2}\,\delta_{q_1+p_1},
$$

$$
\langle A_-(q_2)F_{\rm raw}^{(1),B}(p_2)\rangle_0
=
-2i g_{\rm YM}^2\,\frac{p_{2,+\dot\alpha}}{p_2^2}\,\delta_{q_2+p_2},
$$

$$
\langle \bar\Lambda_{\dot\beta}(q_3)\Lambda_-(v)\rangle_0
=
-i g_{\rm YM}^2\,\frac{v_-{}_{\dot\beta}}{v^2}\,\delta_{q_3+v},
$$
得到
$$
\boxed{
\Gamma_{\Psi X,12}^{AB}(p)
=
\sqrt2\,g_{\rm YM}^2
\int_{p_1,p_2}\delta_{p-p_1-p_2}\,
\mathcal K_{\Psi X,12}^{AB}(p_1,p_2)\,
\int_q^d
\frac{\widehat q^2\,q_{+\dot\alpha}(q-p_2)_+{}^{\dot\alpha}}
{q^2(q+p_1)^2(q-p_2)^2}.
}
$$

做完三条 propagators 与所有 \(\delta\)-函数后，只剩一个 loop momentum \(q\)，得到
$$
\boxed{
\Gamma_{\Psi X,12}^{AB,{\rm ev}}(p)
=
\sqrt2\,g_{\rm YM}^2
\int_{p_1,p_2}\delta_{p-p_1-p_2}\,
\mathcal K_{\Psi X,12}^{AB}(p_1,p_2)\,
\int_q^d
\frac{\widehat q^2\,q_{+\dot\alpha}(q-p_2)_+{}^{\dot\alpha}}
{q^2\,(q+p_1)^2\,(q-p_2)^2}.
}
$$

第一种 routing：
$$
\boxed{
\Gamma_{\Psi X,12}^{AB,{\rm ev}}(p)
=
\sqrt2\,g_{\rm YM}^2
\int_{p_1,p_2}\delta_{p-p_1-p_2}\,
\mathcal K_{\Psi X,12}^{AB}(p_1,p_2)\,
\int_q^d
\frac{\widehat q^2\,q_{+\dot\alpha}(q-p_2)_+{}^{\dot\alpha}}
{q^2\,(q+p_1)^2\,(q-p_2)^2}.
}
$$

第二种 routing：
$$
\boxed{
\Gamma_{\Psi X,21}^{AB,{\rm ev}}(p)
=
\sqrt2\,g_{\rm YM}^2
\int_{p_1,p_2}\delta_{p-p_1-p_2}\,
\mathcal K_{\Psi X,21}^{AB}(p_1,p_2)\,
\int_q^d
\frac{\widehat q^2\,q_{+\dot\alpha}(q-p_2)_+{}^{\dot\alpha}}
{q^2\,(q+p_1)^2\,(q-p_2)^2}.
}
$$

这里三条 propagators 分别对应
$$
\langle \bar\Lambda\,\Lambda\rangle,\qquad
\langle A_-\,F_{\rm raw}^{(1),A}\rangle,\qquad
\langle A_-\,F_{\rm raw}^{(1),B}\rangle.
$$

这里的双 color tensor 来自两处：
\[
f^{CE}{}_{A}\ \text{来自}\ J_F^{(3)}\sim [A,A]\bar\Lambda,
\qquad
f^{DE}{}_{B}\ \text{来自}\ \mathcal L_{X\Lambda\Psi}^{(3)}.
\]

## Step 4: DR reduction

两类三角图统一采用
$$
\frac{1}{q^2(q+p_1)^2(q-p_2)^2}
=
2\int_\Delta
\frac{1}{\big[(q+y p_1-z p_2)^2+\Delta\big]^3},
$$

$$
\Delta
=
xy\,p_1^2+xz\,p_2^2+yz\,p^2,
\qquad
\ell=q+y p_1-z p_2.
$$

并使用统一记号文件中的
$$
\mu^{2\epsilon}\int\frac{d^d\ell}{(2\pi)^d}
\frac{\widehat\ell^2}{(\ell^2+\Delta)^3}\Big|_{\rm loc}
=
-\frac{1}{32\pi^2},
$$

$$
\int\frac{d^d\ell}{(2\pi)^d}
\frac{\widehat\ell^2\,\ell_{+\dot\beta}}{(\ell^2+\Delta)^3}=0.
$$

### Step 4.1: Class I

shift 后
$$
q-p_2=\ell-y p_1-(x+y)p_2.
$$

odd part 消失，只剩 shift piece，故
$$
\boxed{
\Gamma_{F\bar\Lambda,12}^{AB,{\rm loc}}(p)
=
-\frac{g_{\rm YM}^2}{8\pi^2}
\int_{p_1,p_2}\delta_{p-p_1-p_2}\,
\mathcal G_{12,+\dot\alpha}(0;p_1,p_2)\,
\mathcal K_{F\bar\Lambda,12}^{AB,\dot\alpha}(p_1,p_2),
}
$$

$$
\boxed{
\Gamma_{F\bar\Lambda,21}^{AB,{\rm loc}}(p)
=
-\frac{g_{\rm YM}^2}{8\pi^2}
\int_{p_1,p_2}\delta_{p-p_1-p_2}\,
\mathcal G_{21,+\dot\alpha}(0;p_1,p_2)\,
\mathcal K_{F\bar\Lambda,21}^{AB,\dot\alpha}(p_1,p_2),
}
$$

其中
$$
\mathcal G_{12,+\dot\alpha}(0;p_1,p_2)=\frac16(p_1+2p_2)_{+\dot\alpha},
\qquad
\mathcal G_{21,+\dot\alpha}(0;p_1,p_2)=\frac16(2p_1+p_2)_{+\dot\alpha}.
$$

按
$$
p=p_1+p_2
$$
并在所选 local basis
\[
\Big\{
\Tr\!\big[(\nabla_{+\dot\alpha}F_{\rm raw}^A)\bar\Lambda^{B\dot\alpha}\big],\,
\Tr\!\big[(\nabla_{+\dot\alpha}F_{\rm raw}^B)\bar\Lambda^{A\dot\alpha}\big]
\Big\}
\]
上直接写成
$$
\boxed{
\Gamma_{F\bar\Lambda}^{AB,{\rm loc}}(p)
=
\frac{g_{\rm YM}^2}{8\pi^2}
\int_{p_1,p_2}\delta_{p-p_1-p_2}
\Big[
+i\,p_{1,+\dot\alpha}\,\mathcal K_{F\bar\Lambda,12}^{AB,\dot\alpha}(p_1,p_2)
+i\,p_{1,+\dot\alpha}\,\mathcal K_{F\bar\Lambda,21}^{AB,\dot\alpha}(p_1,p_2)
\Big].
}
$$

### Step 4.2: Class II

shift 后
$$
q_{+\dot\alpha}(q-p_2)_+{}^{\dot\alpha}
\longrightarrow
y\,p_{1,+\dot\alpha}p_{2,+}{}^{\dot\alpha}.
$$

于是
$$
\boxed{
\Gamma_{\Psi X,12}^{AB,{\rm loc}}(p)
=
-\frac{\sqrt2\,g_{\rm YM}^2}{16\pi^2}
\int_{p_1,p_2}\delta_{p-p_1-p_2}\,
p_{+\dot\alpha}p_{2,+}{}^{\dot\alpha}\,
\mathcal K_{\Psi X,12}^{AB}(p_1,p_2),
}
$$

$$
\boxed{
\Gamma_{\Psi X,21}^{AB,{\rm loc}}(p)
=
-\frac{\sqrt2\,g_{\rm YM}^2}{16\pi^2}
\int_{p_1,p_2}\delta_{p-p_1-p_2}\,
p_{+\dot\alpha}p_{1,+}{}^{\dot\alpha}\,
\mathcal K_{\Psi X,21}^{AB}(p_1,p_2).
}
$$

再用
$$
p=p_1+p_2,
\qquad
p_{1,+\dot\alpha}p_1{}_{+}{}^{\dot\alpha}
=
p_{2,+\dot\alpha}p_2{}_{+}{}^{\dot\alpha}=0,
$$
并在所选 local basis
\[
\Big\{
\Tr\!\big[(\nabla_{+\dot\alpha}\Psi_+^{iA})(\nabla_+^{\dot\alpha}X_i^B)\big],\,
\Tr\!\big[(\nabla_{+\dot\alpha}\Psi_+^{iB})(\nabla_+^{\dot\alpha}X_i^A)\big]
\Big\}
\]
上直接写成
$$
\boxed{
\Gamma_{\Psi X}^{AB,{\rm loc}}(p)
=
-\frac{\sqrt2\,g_{\rm YM}^2}{8\pi^2}
\int_{p_1,p_2}\delta_{p-p_1-p_2}\,
p_{1,+\dot\alpha}p_{2,+}{}^{\dot\alpha}
\Big[
\mathcal K_{\Psi X,12}^{AB}(p_1,p_2)
+
\mathcal K_{\Psi X,21}^{AB}(p_1,p_2)
\Big].
}
$$

## Step 5: Final momentum-space result

$$
\boxed{
Q_1^{(1)}\!\big(F_{\rm raw}^A F_{\rm raw}^B\big)(p)
=
\Gamma_{F\bar\Lambda}^{AB,{\rm loc}}(p)
+
\Gamma_{\Psi X}^{AB,{\rm loc}}(p).
}
$$

即
$$
\boxed{
Q_1^{(1)}\!\big(F_{\rm raw}^A F_{\rm raw}^B\big)(p)
=
\frac{g_{\rm YM}^2}{8\pi^2}
\int_{p_1,p_2}\delta_{p-p_1-p_2}
\Big[
+i\,p_{1,+\dot\alpha}\,f^{CE}{}_{A}f^{DE}{}_{B}\,
F_{\rm raw}^{C}(p_1)\bar\Lambda^{D\dot\alpha}(p_2)
}
$$

$$
\boxed{
\qquad\qquad
+
+i\,p_{1,+\dot\alpha}\,f^{CE}{}_{A}f^{DE}{}_{B}\,
F_{\rm raw}^{C}(p_2)\bar\Lambda^{D\dot\alpha}(p_1)
-\sqrt2\,p_{1,+\dot\alpha}p_{2,+}{}^{\dot\alpha}
\big(
f^{CE}{}_{A}f^{DE}{}_{B}\,
X_i^C(p_1)\Psi_+^{iD}(p_2)
+
f^{CE}{}_{A}f^{DE}{}_{B}\,
X_i^C(p_2)\Psi_+^{iD}(p_1)
\big)
\Big].
}
$$

## Step 6: Equivalent local operator form

$$
\boxed{
Q_1^{(1)}\!\big(F_{\rm raw}^A F_{\rm raw}^B\big)(x)
=
\frac{g_{\rm YM}^2}{8\pi^2}
\,
f^{CE}{}_{A}f^{DE}{}_{B}
\Big[
(\nabla_{+\dot\alpha}F_{\rm raw}^{C})\bar\Lambda^{D\dot\alpha}
-\sqrt2\,
(\nabla_{+\dot\alpha}\Psi_+^{iD})(\nabla_+^{\dot\alpha}X_i^{C})
\Big](x).
}
$$
