# Explicit Calculation rules

<aside>

## $i\nabla_{+\dot\alpha}\bar\lambda^{\dot\alpha}^i_j\,\bar\lambda_{\dot\beta}^k_l(p)$ 的 perturbative prescription$Q_1 (f_{++}\bar\lambda_{\dot\alpha})$

$$
																																										\mathcal O_{\dot\beta}(x):=iD_{+\dot\alpha}\bar\lambda^{\dot\alpha}(x)\,\bar\lambda_{\dot\beta}(x)
=\mathcal O^{(\partial)}_{\dot\beta}(x)+\mathcal O^{(A)}_{\dot\beta}(x),
$$

$$
																																										\mathcal O^{(\partial)}_{\dot\beta}=i\partial_{+\dot\alpha}\bar\lambda^{\dot\alpha}\,\bar\lambda_{\dot\beta},\qquad
\mathcal O^{(A)}_{\dot\beta}=ig[A_{+\dot\alpha},\bar\lambda^{\dot\alpha}]\,\bar\lambda_{\dot\beta}.
$$

$$
																																										\mathcal I[\mathcal O^{(\partial)}_{\dot\beta}(p)]
=\int_{k,\ell}(2\pi)^4\delta^{(4)}(p-k-\ell)\,(-k_{+\dot\alpha})\,\bar\lambda^{\dot\alpha}(k)\bar\lambda_{\dot\beta}(\ell).
$$

$$
																																										\text{order }g^n:\quad
\text{attach }n\text{ vertices}\ \to\ \text{Wick contract}\ \to\ \text{uncontracted fields become new external legs }\{p_i\},\quad
p=\sum_i p_i.
$$

$$
																																										\text{tree level}:\ \text{no closed cycle};\qquad
\text{loop level}:\ \text{keep every }\int_q\text{ unintegrated until regularization}.
$$

$$
																																										(-k_{+\dot\alpha})\left(-\frac{i\,r_{\gamma}{}^{\dot\alpha}}{r^2}\right)(2\pi)^4\delta^{(4)}(k+r)
=-i\,\delta_{+\gamma}(2\pi)^4\delta^{(4)}(k+r).
$$

$$
\text{所以 }\partial_{+\dot\alpha}\bar\lambda^{\dot\alpha}\text{ 与一条 }\lambda_\gamma\text{ 线收缩时，整条传播子缩成 local contact term.}
$$

### Tree-level (actually All non-anomaly level) cancellation

$$
																																																															\mathcal L_{A\lambda\bar\lambda}
=g\,\bar\lambda_{\dot\gamma}A^{\alpha\dot\gamma}\lambda_\alpha
-g\,\bar\lambda_{\dot\gamma}\lambda_\alpha A^{\alpha\dot\gamma}.
$$

$$
																																																															\mathcal I^{\text{tree}}_{(1)}[\mathcal O^{(\partial)}_{\dot\beta}(p)]
=\int_{k,\ell,q,r,s}(2\pi)^8\delta^{(4)}(p-k-\ell)\delta^{(4)}(q+r+s)
(-k_{+\dot\alpha})\bar\lambda^{\dot\alpha}(k)\bar\lambda_{\dot\beta}(\ell)
\cdot g\,\bar\lambda_{\dot\gamma}(q)A^{\gamma\dot\gamma}(r)\lambda_\gamma(s).
$$

$$
																																																															\bar\lambda^{\dot\alpha}(k)\text{ 与 }\lambda_\gamma(s)\text{ 收缩 }\Longrightarrow
\mathcal I^{\text{tree}}_{(1)}[\mathcal O^{(\partial)}_{\dot\beta}(p)]
=-ig\int_{q,r,\ell}(2\pi)^4\delta^{(4)}(p-q-r-\ell)
A_{+\dot\gamma}(r)\bar\lambda^{\dot\gamma}(q)\bar\lambda_{\dot\beta}(\ell).
$$

$$
																																																															\mathcal I^{\text{tree}}_{(2)}[\mathcal O^{(\partial)}_{\dot\beta}(p)]
=+ig\int_{q,r,\ell}(2\pi)^4\delta^{(4)}(p-q-r-\ell)
\bar\lambda^{\dot\gamma}(q)A_{+\dot\gamma}(r)\bar\lambda_{\dot\beta}(\ell).
$$

$$
																																																															\therefore\quad
\mathcal I^{\text{tree}}[\mathcal O^{(\partial)}_{\dot\beta}(p)]
=-ig\int_{q,r,\ell}(2\pi)^4\delta^{(4)}(p-q-r-\ell)
[A_{+\dot\gamma}(r),\bar\lambda^{\dot\gamma}(q)]\bar\lambda_{\dot\beta}(\ell).
$$

$$
																																																															\mathcal I[\mathcal O^{(A)}_{\dot\beta}(p)]
=+ig\int_{q,r,\ell}(2\pi)^4\delta^{(4)}(p-q-r-\ell)
[A_{+\dot\gamma}(r),\bar\lambda^{\dot\gamma}(q)]\bar\lambda_{\dot\beta}(\ell).
$$

$$
																																																															\boxed{
\mathcal I^{\text{tree}}[\mathcal O_{\dot\beta}(p)]
=\mathcal I^{\text{tree}}[\mathcal O^{(\partial)}_{\dot\beta}(p)]
+\mathcal I[\mathcal O^{(A)}_{\dot\beta}(p)]
=0
}
$$

$$
																																																															\text{故在不含 self-loop 的 tree graphs 上，} \quad iD_{+\dot\alpha}\bar\lambda^{\dot\alpha}=0
\text{ 逐图成立；非零只能来自 loop-level coincident singularity + regulator.}
$$

</aside>

<aside>

## $Q_1 (f_{++}\bar\lambda_{\dot\alpha})$1-loop relevant graphs （first attempt, wrong at group index) (dimensional regularization)

$$
																																								\mathcal O_{\dot\beta}(p)
=
\mathcal O^{(\partial)}_{\dot\beta}(p)
+
\mathcal O^{(A)}_{\dot\beta}(p),
\qquad
\mathcal O^{(\partial)}_{\dot\beta}
=
i\partial_{+\dot\alpha}\bar\lambda^{\dot\alpha}\,\bar\lambda_{\dot\beta},
\qquad
\mathcal O^{(A)}_{\dot\beta}
=
ig\big[A_{+\dot\alpha},\bar\lambda^{\dot\alpha}\big]\,\bar\lambda_{\dot\beta}.
$$

$$
\text{lowest nontrivial loop order}=g^2.
$$

$$
																																								\text{for the external structure }
\bar\lambda_{\dot\gamma}(p_1)\,\bar\lambda_{\dot\beta}(p_2),
\qquad
p=p_1+p_2,
$$

$$
\text{only }V_{A\lambda\bar\lambda}\text{ contributes}.
$$

$$
																																								V_{\bar cAc},\ V_{AAA},\ V_{AAAA}
\quad\text{do not soak up the }\bar\lambda\text{ legs of }\mathcal O_{\dot\beta}.
$$

$$
																																								\Gamma_{\partial}^{(1)}
:\quad
\mathcal O^{(\partial)}_{\dot\beta}
+
V_{A\lambda\bar\lambda}^{(1)}
+
V_{A\lambda\bar\lambda}^{(2)},
$$

$$
																																								(\partial\bar\lambda)_{\mathcal O}\cong \lambda_1,
\qquad
\bar\lambda_1\cong \lambda_2,
\qquad
A_1\cong A_2,
\qquad
\bar\lambda_{\dot\beta,\mathcal O}\ \text{external},
\qquad
\bar\lambda_{\dot\gamma}(p_1)\ \text{external}.
$$

$$
																																								\Gamma_{A}^{(1)}
:\quad
\mathcal O^{(A)}_{\dot\beta}
+
V_{A\lambda\bar\lambda},
$$

$$
																																								A_{\mathcal O}\cong A,
\qquad
\bar\lambda_{\mathcal O}\cong \lambda,
\qquad
\bar\lambda_{\dot\beta,\mathcal O}\ \text{external},
\qquad
\bar\lambda_{\dot\gamma}(p_1)\ \text{external}.
$$

$$
\text{both graphs have exactly one self-loop.}
$$

### Momentum routing

$$
																																																												\int_{p_1,p_2,q}
:=
\int\frac{d^4p_1}{(2\pi)^4}
\int\frac{d^4p_2}{(2\pi)^4}
\int\frac{d^4q}{(2\pi)^4}.
$$

$$
																																																												\text{all incoming},\qquad
p=p_1+p_2,
\qquad
q\ \text{is the loop momentum on the internal }A\text{-line}.
$$

$$
																																																												\text{Weyl propagator }\to\text{ Dirac propagator}:
\qquad
S_D(k):=\frac{-i\not k}{k^2},
\qquad
P_L=\frac{1+\gamma_5}{2},
$$

$$
																																																												-\frac{i\,k_{\alpha\dot\alpha}}{k^2}
=
\big(S_D(k)P_L\big)_{\alpha\dot\alpha}.
$$

### Honest 1-loop integral from $\mathcal O^{(\partial)}$

$$
																																																												\Gamma_{\partial,\dot\beta}^{(1)}(p)
=
g^2
\int_{p_1,p_2,q}
(2\pi)^4\delta^{(4)}(p-p_1-p_2)\,
(-p_{1,+\dot\eta})
\left(
-\frac{i\,p_{1,\gamma_1}{}^{\dot\eta}}{p_1^2}
\right)
\frac{2\,\epsilon^{\gamma_1\gamma_2}\epsilon^{\dot\rho\dot\gamma}}{q^2}
\left(
-\frac{i\,(q-p_1)_{\gamma_2\dot\rho}}{(q-p_1)^2}
\right)
\big[\bar\lambda_{\dot\gamma}(p_1),\bar\lambda_{\dot\beta}(p_2)\big].
$$

$$
																																																												\text{Dirac form}:
\qquad
\Gamma_{\partial,\dot\beta}^{(1)}(p)
=
g^2
\int_{p_1,p_2,q}
(2\pi)^4\delta^{(4)}(p-p_1-p_2)\,
(-p_{1,+\dot\eta})
\big(S_D(p_1)P_L\big)_{\gamma_1}{}^{\dot\eta}
\frac{2\,\epsilon^{\gamma_1\gamma_2}\epsilon^{\dot\rho\dot\gamma}}{q^2}
\big(S_D(q-p_1)P_L\big)_{\gamma_2\dot\rho}
\big[\bar\lambda_{\dot\gamma}(p_1),\bar\lambda_{\dot\beta}(p_2)\big].
$$

### Honest 1-loop integral from $\mathcal O^{(A)}$

$$
																																																												\Gamma_{A,\dot\beta}^{(1)}(p)
=
ig^2
\int_{p_1,p_2,q}
(2\pi)^4\delta^{(4)}(p-p_1-p_2)\,
\frac{2\,\epsilon_{+\gamma}\epsilon_{\dot\eta\dot\gamma}}{q^2}
\left(
-\frac{i\,(q-p_1)^{\gamma\dot\eta}}{(q-p_1)^2}
\right)
\big[\bar\lambda^{\dot\gamma}(p_1),\bar\lambda_{\dot\beta}(p_2)\big].
$$

$$
																																																												\text{Dirac form}:
\qquad
\Gamma_{A,\dot\beta}^{(1)}(p)
=
ig^2
\int_{p_1,p_2,q}
(2\pi)^4\delta^{(4)}(p-p_1-p_2)\,
\frac{2\,\epsilon_{+\gamma}\epsilon_{\dot\eta\dot\gamma}}{q^2}
\big(S_D(q-p_1)P_L\big)^{\gamma\dot\eta}
\big[\bar\lambda^{\dot\gamma}(p_1),\bar\lambda_{\dot\beta}(p_2)\big].
$$

### Formal collapse

$$
																																																												(-p_{1,+\dot\eta})
\left(
-\frac{i\,p_{1,\gamma_1}{}^{\dot\eta}}{p_1^2}
\right)
=
-i\,\delta_{+\gamma_1}.
$$

$$
																																																												\Gamma_{\partial,\dot\beta}^{(1)\,\mathrm{formal}}(p)
=
-2g^2
\int_{p_1,p_2,q}
(2\pi)^4\delta^{(4)}(p-p_1-p_2)\,
\frac{(q-p_1)_{-\dot\gamma}}{q^2(q-p_1)^2}
\big[\bar\lambda^{\dot\gamma}(p_1),\bar\lambda_{\dot\beta}(p_2)\big].
$$

$$
																																																												\Gamma_{A,\dot\beta}^{(1)}(p)
=
+2g^2
\int_{p_1,p_2,q}
(2\pi)^4\delta^{(4)}(p-p_1-p_2)\,
\frac{(q-p_1)_{-\dot\gamma}}{q^2(q-p_1)^2}
\big[\bar\lambda^{\dot\gamma}(p_1),\bar\lambda_{\dot\beta}(p_2)\big].
$$

$$
\text{所以 1-loop anomaly 的关键点不是 formal cancellation，}
$$

$$
\text{而是 }\Gamma_{\partial}^{(1)}\text{ 必须先保持为 honest UV-divergent integral，再上 regulator；}
$$

$$
\text{不能先把 }(-p_1)_{+\dot\eta}S_W(p_1)\text{ 直接缩成 }-i\delta_{+}.
$$

</aside>

<aside>

## $Q_1 (f_{++}\bar\lambda_{\dot\alpha})$1-loop relevant graphs (second attempt, wrong at group index)(dimensional regularization)

![image.png](../source_archive/%E7%9B%B4%E6%8E%A51-loop%20level%E8%AE%A1%E7%AE%97/image.png)

### 1-loop perturbative prescription

$$
																																																									\mathcal O_{\dot\beta}(p)
=
\mathcal O^{(\partial)}_{\dot\beta}(p)
+
\mathcal O^{(A)}_{\dot\beta}(p),
\qquad
\mathcal O^{(\partial)}_{\dot\beta}
=
i\partial_{+\dot\alpha}\bar\lambda^{\dot\alpha}\,\bar\lambda_{\dot\beta},
\qquad
\mathcal O^{(A)}_{\dot\beta}
=
ig\big[A_{+\dot\alpha},\bar\lambda^{\dot\alpha}\big]\,\bar\lambda_{\dot\beta}.
$$

$$
																																																									d=4-2\epsilon,
\qquad
\int_q^d:=\mu^{2\epsilon}\int\frac{d^dq}{(2\pi)^d},
\qquad
S_D(k):=\frac{-i\not k}{k^2},
\qquad
P_L=\frac{1+\gamma_5}{2}.
$$

$$
																																																									\big[S_D(k)P_L\big]_{\alpha\dot\alpha}
=
-\frac{i\,k_{\alpha\dot\alpha}}{k^2}.
$$

$$
																																																								t(\bar\lambda\bar\lambda)(p)
:=
\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)\,\epsilon^{\dot\gamma\dot\delta}\bar\lambda_{\dot\gamma}(p_1)\bar\lambda_{\dot\delta}(p_2).
$$

$$
																																																									\mathcal I\!\left[\partial_{+\dot\beta}(\bar\lambda\bar\lambda)(p)\right]
=
i\,p_{+\dot\beta}\,(\bar\lambda\bar\lambda)(p).
$$

### Relevant 1-loop graphs

真正 relevant 的 one-self-loop sector 分成两类：

$$
																																																									\Gamma_{\rm EOM}^{(1)}
=
\Gamma_{\partial,{\rm chain}}^{(1)}
+
\Gamma_{A,{\rm bubble}}^{(1)},
\qquad
\Gamma_{\rm anom}^{(1)}
=
\Gamma_{\partial,12}^{(1)}
+
\Gamma_{\partial,21}^{(1)}.
$$

其中

$$
																																																									\Gamma_{\partial,{\rm chain}}^{(1)}:\qquad
(\partial\bar\lambda)_{\mathcal O}\cong\lambda_1,
\qquad
\bar\lambda_1\cong\lambda_2,
\qquad
A_1\cong A_2,
$$

$$
																																																									\bar\lambda_{\dot\beta,\mathcal O}\ \text{external},
\qquad
\bar\lambda_{\dot\gamma}(p_1)\ \text{external}.
$$

$$
																																																									\Gamma_{A,{\rm bubble}}^{(1)}:\qquad
A_{\mathcal O}\cong A,
\qquad
\bar\lambda_{\mathcal O}\cong\lambda,
$$

$$
																																																									\bar\lambda_{\dot\beta,\mathcal O}\ \text{external},
\qquad
\bar\lambda_{\dot\gamma}(p_1)\ \text{external}.
$$

这两张图属于 EOM sector；formal 4d reduction 后彼此抵消。

真正给 $\partial_{+\dot\beta}(\bar\lambda\bar\lambda)$ 的是 triangle pair：

$$
																																																									\Gamma_{\partial,12}^{(1)}:\qquad
(\partial\bar\lambda)_{\mathcal O}\cong\lambda_1,
\qquad
(\bar\lambda_{\dot\beta})_{\mathcal O}\cong\lambda_2,
\qquad
A_1\cong A_2,
$$

$$
																																																									\bar\lambda_{\dot\gamma}(p_1)\ \text{external},
\qquad
\bar\lambda_{\dot\delta}(p_2)\ \text{external}.
$$

$$
																																																									\Gamma_{\partial,21}^{(1)}:\qquad
(\partial\bar\lambda)_{\mathcal O}\cong\lambda_2,
\qquad
(\bar\lambda_{\dot\beta})_{\mathcal O}\cong\lambda_1,
\qquad
A_1\cong A_2,
$$

$$
																																																									\bar\lambda_{\dot\delta}(p_2)\ \text{external},
\qquad
\bar\lambda_{\dot\gamma}(p_1)\ \text{external}.
$$

### Honest momentum integrals: EOM sector

$$
																																																									\Gamma_{\partial,{\rm chain},\dot\beta}^{(1)}(p_1,p_2)
=
g^2 C_A
\int_q^d
\Big[
-p_{1,+\dot\alpha}\,
\big[S_D(p_1)P_L\big]_{\alpha}{}^{\dot\alpha}
\Big]
\frac{2\,\epsilon^{\alpha\rho}\epsilon^{\dot\eta\dot\gamma}}{q^2}
\big[S_D(q-p_1)P_L\big]_{\rho\dot\eta}\,
\bar\lambda_{\dot\gamma}(p_1)\bar\lambda_{\dot\beta}(p_2).
$$

$$
																																																									\Gamma_{A,{\rm bubble},\dot\beta}^{(1)}(p_1,p_2)
=
i g^2 C_A
\int_q^d
\frac{2\,\epsilon_{+\rho}\epsilon_{\dot\eta\dot\gamma}}{q^2}\,
\big[S_D(q-p_1)P_L\big]^{\rho\dot\eta}\,
\bar\lambda^{\dot\gamma}(p_1)\bar\lambda_{\dot\beta}(p_2).
$$

formal 4d identity:

$$
																																																									-p_{1,+\dot\alpha}\,\big[S_D(p_1)P_L\big]_{\alpha}{}^{\dot\alpha}
=
i\,\epsilon_{+\alpha},
$$

所以

$$
\Gamma_{\partial,{\rm chain}}^{(1)}+\Gamma_{A,{\rm bubble}}^{(1)}=0.
$$

### Honest momentum integrals: anomalous triangle sector

取 routing

$$
																																																									k_1=q+p_1,
\qquad
k_2=p_2-q,
\qquad
p=p_1+p_2.
$$

则

$$
																																																									\Gamma_{\partial,12,\dot\beta}^{(1)}(p_1,p_2)
=
g^2 C_A
\int_q^d
\Big[
-(q+p_1)_{+\dot\alpha}\,
\big[S_D(q+p_1)P_L\big]_{\alpha}{}^{\dot\alpha}
\Big]
\frac{2\,\epsilon^{\alpha\rho}\epsilon^{\dot\gamma\dot\delta}}{q^2}
\big[S_D(q-p_2)P_L\big]_{\rho\dot\beta}\,
\bar\lambda_{\dot\gamma}(p_1)\bar\lambda_{\dot\delta}(p_2).
$$

$$
																																																									\Gamma_{\partial,21,\dot\beta}^{(1)}(p_1,p_2)
=
g^2 C_A
\int_q^d
\Big[
-(q+p_2)_{+\dot\alpha}\,
\big[S_D(q+p_2)P_L\big]_{\alpha}{}^{\dot\alpha}
\Big]
\frac{2\,\epsilon^{\alpha\rho}\epsilon^{\dot\delta\dot\gamma}}{q^2}
\big[S_D(q-p_1)P_L\big]_{\rho\dot\beta}\,
\bar\lambda_{\dot\delta}(p_2)\bar\lambda_{\dot\gamma}(p_1).
$$

### d-dimensional reduction of the triangle numerator

把 $q=\tilde q+\hat q$ 分成 4d part 与 $(d-4)$-dim part，则

$$
																																																									(\tilde q+p_1)_{+\dot\alpha}(\tilde q+p_1)_{\alpha}{}^{\dot\alpha}
=
\big((q+p_1)^2-\hat q^2\big)\epsilon_{+\alpha}.
$$

故

$$
																																																									-(q+p_1)_{+\dot\alpha}\,\big[S_D(q+p_1)P_L\big]_{\alpha}{}^{\dot\alpha}
=
i\left(1-\frac{\hat q^2}{(q+p_1)^2}\right)\epsilon_{+\alpha}.
$$

于是

$$
																																																									\Gamma_{\partial,12,\dot\beta}^{(1)}
=
2C_A g^2
\int_q^d
\frac{(q-p_2)_{+\dot\beta}}{q^2(q-p_2)^2}\,
\epsilon^{\dot\gamma\dot\delta}\bar\lambda_{\dot\gamma}(p_1)\bar\lambda_{\dot\delta}(p_2)
-
2C_A g^2
\int_q^d
\frac{\hat q^2\,(q-p_2)_{+\dot\beta}}{q^2(q+p_1)^2(q-p_2)^2}\,
\epsilon^{\dot\gamma\dot\delta}\bar\lambda_{\dot\gamma}(p_1)\bar\lambda_{\dot\delta}(p_2).
$$

同理

$$
																																																									\Gamma_{\partial,21,\dot\beta}^{(1)}
=
2C_A g^2
\int_q^d
\frac{(q-p_1)_{+\dot\beta}}{q^2(q-p_1)^2}\,
\epsilon^{\dot\gamma\dot\delta}\bar\lambda_{\dot\gamma}(p_1)\bar\lambda_{\dot\delta}(p_2)
-
2C_A g^2
\int_q^d
\frac{\hat q^2\,(q-p_1)_{+\dot\beta}}{q^2(q+p_2)^2(q-p_1)^2}\,
\epsilon^{\dot\gamma\dot\delta}\bar\lambda_{\dot\gamma}(p_1)\bar\lambda_{\dot\delta}(p_2).
$$

### UV-divergent local piece

定义标准 two-point integral

$$
																																																									I_0(s)
:=
\int_q^d\frac{1}{q^2(q-p)^2}\Big\|_{p^2=s}
=
\frac{\mu^{2\epsilon}}{(4\pi)^{2-\epsilon}}
\Gamma(\epsilon)\,
\frac{\Gamma(1-\epsilon)^2}{\Gamma(2-2\epsilon)}\,
s^{-\epsilon}.
$$

其 UV pole 为

$$
																																																									\big[I_0(s)\big]_{\rm UV}
=
\frac{1}{16\pi^2}\frac{1}{\epsilon}.
$$

并且

$$
																																																									\int_q^d\frac{(q-p)_{+\dot\beta}}{q^2(q-p)^2}
=
-\frac12\,p_{+\dot\beta}\,I_0(p^2).
$$

故 triangle pair 的 local UV part 为

$$
																																																									\Gamma_{{\rm anom},\dot\beta}^{(1)}(p_1,p_2)\Big\|_{\rm UV}
=
-C_A g^2\,
\Big[
p_{2,+\dot\beta}I_0(p_2^2)
+
p_{1,+\dot\beta}I_0(p_1^2)
\Big]_{\rm UV}
\epsilon^{\dot\gamma\dot\delta}\bar\lambda_{\dot\gamma}(p_1)\bar\lambda_{\dot\delta}(p_2).
$$

即

$$
																																																									\Gamma_{{\rm anom},\dot\beta}^{(1)}(p_1,p_2)\Big\|_{\rm UV}
=
-\frac{C_A g^2}{16\pi^2}\frac{1}{\epsilon}\,
(p_1+p_2)_{+\dot\beta}\,
\epsilon^{\dot\gamma\dot\delta}\bar\lambda_{\dot\gamma}(p_1)\bar\lambda_{\dot\delta}(p_2).
$$

由于 $p=p_1+p_2$,

$$
																																																									\boxed{
\Gamma_{{\rm anom},\dot\beta}^{(1)}(p)\Big\|_{\rm UV}
=
-\frac{C_A g^2}{16\pi^2}\frac{1}{\epsilon}\,
p_{+\dot\beta}\,
(\bar\lambda\bar\lambda)(p)
}.
$$

于是，作为 local operator mixing，

$$
																																																									\boxed{
i\nabla_{+\dot\alpha}\bar\lambda^{\dot\alpha}\,\bar\lambda_{\dot\beta}(p)
\ \leadsto\
-\frac{C_A g^2}{16\pi^2}\frac{1}{\epsilon}\,
\partial_{+\dot\beta}(\bar\lambda\bar\lambda)(p)
}.
$$

$$
																																								\text{(省略群指标；EOM-sector cancel，nonzero piece 只来自 anomalous triangle UV divergence).
Python schematic Feynman graphs： q1_fpp_nablafpp_diagrams.png**<br>Setup**<br>沿用同页 conventions：<br>\[
Q_- f_{++}= i\nabla_{+\dot\alpha}\bar\lambda^{\dot\alpha},\qquad<br>Q_-A_{+\dot\theta}= i\bar\lambda_{\dot\theta},\qquad<br>\[Q_-,\nabla_{+\dot\theta}\]X=i[\bar\lambda_{\dot\theta},X],<br>\]<br>\[
\mathcal I[\partial_{+\dot\theta}f_{++}(p)]<br>= i,p_{+\dot\theta},\mathcal I[f_{++}(p)],<br>\qquad<br>V_{A\lambda\bar\lambda}=V_L-V_R,<br>\]<br>\[
\langle \Lambda_\alpha(p)\bar\Lambda_{\dot\beta}(-p)\rangle_{\rm PV}<br>=-\frac{i,p_{\alpha\dot\beta}}{p^2+M^2},<br>\qquad<br>\langle B_{\alpha\dot\alpha}(p)B_{\beta\dot\beta}(-p)\rangle_{\rm PV}<br>=\frac{2\epsilon_{\alpha\beta}\epsilon_{\dot\alpha\dot\beta}}{p^2+M^2}.<br>\]
并且继续用前页 mixed color tensor (\mathscr F_{12}^{\dot\beta},\mathscr F_{21}^{\dot\beta})。
定义
\[
\mathcal O_{f\nabla f,\dot\theta}{}^i{}_j{}^k{}_l(x):=f_{++}{}^i{}_j(x),\nabla_{+\dot\theta}f_{++}{}^k{}_l(x).\]
**<br>严格写\[Q_-\mathcal O_{f\nabla f,\dot\theta}**<br>\underbrace{<br>\big(i\nabla_{+\dot\alpha}\bar\lambda^{\dot\alpha}\big),\nabla_{+\dot\theta}f_{++}<br>}*{\text{loop-focus 1}}+\underbrace{f*{++},\nabla_{+\dot\theta}\big(i\nabla_{+\dot\alpha}\bar\lambda^{\dot\alpha}\big)}*{\text{loop-focus 2}}+\underbrace{i,f*{++},[\bar\lambda_{\dot\theta},f_{++}]}_{\text{tree level}}.\]<br>下面只算 loop-focus；最后一项不进 1-loop anomaly。**<br>Ordered pair 先算**<br>\[
\mathcal O_{\dot\theta}^{\rm mix}{}^i{}_j{}^k{}_l(x):=i\nabla_{+\dot\alpha}\bar\lambda^{\dot\alpha}{}^i{}_j(x),\nabla_{+\dot\theta}f_{++}{}^k{}_l(x).\]**<br>取决定 universal coefficient 的 two-field triangle piece：\[\mathcal O_{\dot\theta}^{(\partial\partial)}{}^i{}_j{}^k{}_l**<br>i\partial_{+\dot\alpha}\bar\lambda^{\dot\alpha}{}^i{}_j;i\partial_{+\dot\theta}f_{++}^{(\partial)}{}^k{}_l.\]**<br>动量空间 insertion：\[\mathcal I!\left[\mathcal O_{\dot\theta}^{(\partial\partial)}(p)\right]**<br>\int_{r,s}(2\pi)^4\delta^{(4)}(p-r-s),<br>(-r_{+\dot\alpha})(i s_{+\dot\theta}),<br>\bar\lambda^{\dot\alpha}(r),\mathcal I[f_{++}(s)].<br>\]**<br>同前页定义\[\mathscr F_{12}^{\dot\beta}**<br>\mathscr F_{12}^{(LL)\dot\beta}<br>+\mathscr F_{12}^{(LR)\dot\beta}<br>+\mathscr F_{12}^{(RL)\dot\beta}<br>+\mathscr F_{12}^{(RR)\dot\beta},<br>\]<br>\[
\mathscr F_{12}^{(LL)\dot\beta}{}^i{}_j{}^k{}_l=\Pi^{mn}{}_{jl},f_{++}{}^i{}_m(p_1),\bar\lambda^{\dot\beta}{}^k{}_n(p_2),\]
\[\mathscr F_{12}^{(LR)\dot\beta}{}^i{}_j{}^k{}_l=-\Pi^{mk}{}_{jn},f_{++}{}^i{}_m(p_1),\bar\lambda^{\dot\beta}{}^n{}_l(p_2),\]
\[\mathscr F_{12}^{(RL)\dot\beta}{}^i{}_j{}^k{}_l=-\Pi^{in}{}_{ml},f_{++}{}^m{}_j(p_1),\bar\lambda^{\dot\beta}{}^k{}_n(p_2),\]
\[\mathscr F_{12}^{(RR)\dot\beta}{}^i{}_j{}^k{}_l=\Pi^{ik}{}_{mn},f_{++}{}^m{}_j(p_1),\bar\lambda^{\dot\beta}{}^n{}_l(p_2),\]
\[\mathscr F_{21}^{\dot\beta}(p_1,p_2)=\mathscr F_{12}^{\dot\beta}(p_2,p_1).\]**<br>Pattern 12**<br>routing 取<br>\[
r=q+p_1,\qquad s=p_2-q,\qquad p=p_1+p_2.<br>\]
写<br>\[
\big(S_M(k)P_L\big)_{\alpha\dot\alpha}=-\frac{i,k_{\alpha\dot\alpha}}{k^2+M^2}.\]**<br>则\[-r_{+\dot\alpha}\big(S_M(r)P_L\big)_\alpha{}^{\dot\alpha}**<br>i\epsilon_{+\alpha}<br>-i\frac{M^2}{r^2+M^2}\epsilon_{+\alpha}.<br>\]**<br>又\[\langle f_{++}(s),B_{-\dot\beta}(-s)\rangle_{\rm PV}<br>-\frac{i,s_{+\dot\beta}}{s^2+M^2},\]故\[i s_{+\dot\theta},\langle f_{++}(s),B_{-\dot\beta}(-s)\rangle_{\rm PV}**<br>\frac{s_{+\dot\theta}s_{+\dot\beta}}{s^2+M^2}.<br>\]**<br>于是\[\Gamma_{12;M}^{\rm PV\text{-}loop}{}_{\dot\theta}{}^i{}_j{}^k{}_l**<br>2i g^2\int_q<br>\frac{(q-p_2)_{+\dot\theta}(q-p_2)_{+\dot\beta}}<br>\{(q^2+M^2)\big((q-p_2)^2+M^2\big)\}<br>,<br>\mathscr F_{12}^{\dot\beta}{}^i{}_j{}^k{}_l\]
\[\qquad-2i g^2 M^2\int_q\frac{(q-p_2)_{+\dot\theta}(q-p_2)_{+\dot\beta}}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)},\mathscr F_{12}^{\dot\beta}{}^i{}_j{}^k{}_l.\]**<br>前一项是 contact/EOM sector；后一项是 anomaly sector：\[\Gamma_{12;M}^{(\rm anom)}{}_{\dot\theta}**<br>-2i g^2 M^2\int_q<br>\frac{(q-p_2)_{+\dot\theta}(q-p_2)_{+\dot\beta}}<br>\{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)\}<br>,<br>\mathscr F_{12}^{\dot\beta}.<br>\]**<br>Feynman parameter：\[\frac{1}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}**<br>2\int_0^1dx,dy,dz,\delta(1-x-y-z)<br>\frac{1}{\big[(q+yp_1-zp_2)^2+M^2+\Delta\big]^3},<br>\]<br>\[
\Delta=xy,p_1^2+xz,p_2^2+yz,p^2.<br>\]
令<br>\[
\ell=q+yp_1-zp_2,\qquad q-p_2=\ell-yp-xp_2.<br>\]
**<br>则\[\Gamma_{12;M}^{(\rm anom)}**<br>-4i g^2 M^2\int_0^1dx,dy,dz,\delta(1-x-y-z)<br>\int_\ell<br>\frac{(\ell-yp-xp_2)_{+\dot\theta}(\ell-yp-xp_2)_{+\dot\beta}}<br>\{(\ell^2+M^2+\Delta)^3\}<br>,<br>\mathscr F_{12}^{\dot\beta}.<br>\]**<br>\[\int_\ell \ell_{+\dot\theta}\ell_{+\dot\beta},F(\ell^2)=0,\qquad\int_\ell \ell_{+\dot\theta},F(\ell^2)=0,\]故只剩 shift piece：\[\Gamma_{12;M}^{(\rm anom)}**<br>-4i g^2 M^2\int_0^1dx,dy,dz,\delta(1-x-y-z)<br>(yp+xp_2)_{+\dot\theta}(yp+xp_2)_{+\dot\beta}<br>\int_\ell\frac{1}{(\ell^2+M^2+\Delta)^3}<br>,<br>\mathscr F_{12}^{\dot\beta}.<br>\]**<br>再用\[\int_\ell\frac{1}{(\ell^2+\Omega)^3}<br>\frac{1}{32\pi^2}\frac{1}{\Omega},\]得\[\Gamma_{12;M}^{(\rm anom)}**<br>-\frac{i g^2}{8\pi^2}<br>\int_0^1dx,dy,dz,\delta(1-x-y-z)<br>\frac{M^2}{M^2+\Delta}<br>(yp+xp_2)_{+\dot\theta}(yp+xp_2)_{+\dot\beta}<br>,<br>\mathscr F_{12}^{\dot\beta}.<br>\]**<br>取 (M\to\infty) 的 local part：\[\Gamma_{12}^{(\rm anom,loc)}\]...
$$

</aside>

<aside>

## $Q_1 (f_{++}\bar\lambda_{\dot\alpha})$ (third attempt, DR. right answer)

### corrected matrix-index setup

$$
\Pi^{ik}{}_{jl}:=\sum_a (T^a)^i{}_j(T^a)^k{}_l.
$$

$$
																										\Pi^{ik}{}_{jl}
=
\delta^i{}_l\delta^k{}_j
\quad (U(N)),
\qquad
\Pi^{ik}{}_{jl}
=
\delta^i{}_l\delta^k{}_j-\frac1N\delta^i{}_j\delta^k{}_l
\quad (SU(N)).
$$

$$
																										\langle \lambda_\alpha{}^i{}_j(p)\,\bar\lambda_{\dot\beta}{}^k{}_l(-p)\rangle
=
-\frac{i\,p_{\alpha\dot\beta}}{p^2}\,\Pi^{ik}{}_{jl},
$$

$$
																										\langle A_{\alpha\dot\alpha}{}^i{}_j(p)\,A_{\beta\dot\beta}{}^k{}_l(-p)\rangle
=
\frac{2\,\epsilon_{\alpha\beta}\epsilon_{\dot\alpha\dot\beta}}{p^2}\,\Pi^{ik}{}_{jl}.
$$

$$
V_{A\lambda\bar\lambda}=V_L-V_R,
$$

$$
																										V_L
=
g\,\bar\lambda_{\dot\gamma}{}^a{}_b\,A^{\gamma\dot\gamma}{}^b{}_c\,\lambda_\gamma{}^c{}_a,
\qquad
V_R
=
g\,\bar\lambda_{\dot\gamma}{}^a{}_b\,\lambda_\gamma{}^b{}_c\,A^{\gamma\dot\gamma}{}^c{}_a.
$$

$$
																										\mathcal O_{\dot\beta}{}^i{}_j{}^k{}_l
=
i\nabla_{+\dot\alpha}\bar\lambda^{\dot\alpha}{}^i{}_j\,\bar\lambda_{\dot\beta}{}^k{}_l
=
\mathcal O_{\dot\beta}^{(\partial)}{}^i{}_j{}^k{}_l
+
\mathcal O_{\dot\beta}^{(A)}{}^i{}_j{}^k{}_l,
$$

$$
																										\mathcal O_{\dot\beta}^{(\partial)}{}^i{}_j{}^k{}_l
=
i\partial_{+\dot\alpha}\bar\lambda^{\dot\alpha}{}^i{}_j\,\bar\lambda_{\dot\beta}{}^k{}_l,
$$

$$
																										\mathcal O_{\dot\beta}^{(A)}{}^i{}_j{}^k{}_l
=
ig\Big(
A_{+\dot\alpha}{}^i{}_m\,\bar\lambda^{\dot\alpha}{}^m{}_j
-
\bar\lambda^{\dot\alpha}{}^i{}_m\,A_{+\dot\alpha}{}^m{}_j
\Big)\bar\lambda_{\dot\beta}{}^k{}_l.
$$

$$
																										\mathcal I[\mathcal O_{\dot\beta}^{(\partial)}{}^i{}_j{}^k{}_l(p)]
=
\int_{r,s}(2\pi)^4\delta^{(4)}(p-r-s)\,
(-r_{+\dot\alpha})\,
\bar\lambda^{\dot\alpha}{}^i{}_j(r)\,
\bar\lambda_{\dot\beta}{}^k{}_l(s).
$$

### order $g^2$ before Wick contraction

$$
																										\Gamma_{\triangle,\dot\beta}^{(1)}{}^i{}_j{}^k{}_l(p)
=
\frac12\,
\Big\langle
\mathcal I[\mathcal O_{\dot\beta}^{(\partial)}{}^i{}_j{}^k{}_l(p)]
\,
(V_L-V_R)_1
\,
(V_L-V_R)_2
\Big\rangle_{0,\text{1-loop}}.
$$

$$
																										(V_L-V_R)_a
=
\int_{u_a,v_a,w_a}(2\pi)^4\delta^{(4)}(u_a+v_a+w_a)
\Big[
\bar\lambda_{\dot\gamma_a}{}^{a_a}{}_{b_a}(u_a)\,
A^{\gamma_a\dot\gamma_a}{}^{b_a}{}_{c_a}(v_a)\,
\lambda_{\gamma_a}{}^{c_a}{}_{a_a}(w_a)
-
\bar\lambda_{\dot\gamma_a}{}^{a_a}{}_{b_a}(u_a)\,
\lambda_{\gamma_a}{}^{b_a}{}_{c_a}(w_a)\,
A^{\gamma_a\dot\gamma_a}{}^{c_a}{}_{a_a}(v_a)
\Big].
$$

### Wick pattern 12

$$
																										\bar\lambda^{\dot\alpha}{}^i{}_j(r)\cong \lambda_{1,\alpha}(w_1),
\qquad
\bar\lambda_{\dot\beta}{}^k{}_l(s)\cong \lambda_{2,\rho}(w_2),
\qquad
A_1(v_1)\cong A_2(v_2),
$$

$$
																										\bar\lambda_{\dot\gamma}(u_1)\ \text{external with momentum }p_1,
\qquad
\bar\lambda_{\dot\delta}(u_2)\ \text{external with momentum }p_2,
\qquad
p=p_1+p_2.
$$

取 routing

$$
																										v_1=q,\qquad v_2=-q,\qquad
w_1=-(q+p_1),\qquad
w_2=q-p_2.
$$

于是

$$
																										r=q+p_1,
\qquad
s=p-r=p_2-q.
$$

### after Wick contraction: graph 12

$$
																									\Gamma_{12,\dot\beta}^{(1)}{}^i{}_j{}^k{}_l(p_1,p_2)
=
g^2\int_q^d
\Big[
-(q+p_1)_{+\dot\alpha}\,
\big(S_D(q+p_1)P_L\big)_{\alpha}{}^{\dot\alpha}
\Big]
\frac{2\,\epsilon^{\alpha\rho}}{q^2}\,
\big(S_D(q-p_2)P_L\big)_{\rho\dot\beta}\,
\mathscr C_{12}{}^i{}_j{}^k{}_l(p_1,p_2),
$$

$$
																									S_D(k)=\frac{-i\not k}{k^2},
\qquad
\big(S_D(k)P_L\big)_{\alpha\dot\alpha}
=
-\frac{i\,\tilde k_{\alpha\dot\alpha}}{k^2}.
$$

其中 color-flow tensor 分成四项：

$$
																									\mathscr C_{12}
=
\mathscr C_{12}^{(LL)}
+
\mathscr C_{12}^{(LR)}
+
\mathscr C_{12}^{(RL)}
+
\mathscr C_{12}^{(RR)},
$$

$$
																									\mathscr C_{12}^{(LL)}{}^i{}_j{}^k{}_l
=
\epsilon^{\dot\gamma\dot\delta}\,
\Pi^{mn}{}_{jl}\,
\bar\lambda_{\dot\gamma}{}^i{}_m(p_1)\,
\bar\lambda_{\dot\delta}{}^k{}_n(p_2),
$$

$$
																									\mathscr C_{12}^{(LR)}{}^i{}_j{}^k{}_l
=
-\epsilon^{\dot\gamma\dot\delta}\,
\Pi^{mk}{}_{jn}\,
\bar\lambda_{\dot\gamma}{}^i{}_m(p_1)\,
\bar\lambda_{\dot\delta}{}^n{}_l(p_2),
$$

$$
																									\mathscr C_{12}^{(RL)}{}^i{}_j{}^k{}_l
=
-\epsilon^{\dot\gamma\dot\delta}\,
\Pi^{in}{}_{ml}\,
\bar\lambda_{\dot\gamma}{}^m{}_j(p_1)\,
\bar\lambda_{\dot\delta}{}^k{}_n(p_2),
$$

$$
																									\mathscr C_{12}^{(RR)}{}^i{}_j{}^k{}_l
=
\epsilon^{\dot\gamma\dot\delta}\,
\Pi^{ik}{}_{mn}\,
\bar\lambda_{\dot\gamma}{}^m{}_j(p_1)\,
\bar\lambda_{\dot\delta}{}^n{}_l(p_2).
$$

在 (U(N)) double-line 下：

$$
																									\mathscr C_{12}{}^i{}_j{}^k{}_l
=
\epsilon^{\dot\gamma\dot\delta}\Big[
\bar\lambda_{\dot\gamma}{}^i{}_l(p_1)\bar\lambda_{\dot\delta}{}^k{}_j(p_2)
-\delta^k{}_j\,\bar\lambda_{\dot\gamma}{}^i{}_m(p_1)\bar\lambda_{\dot\delta}{}^m{}_l(p_2)
-\delta^i{}_l\,\bar\lambda_{\dot\gamma}{}^m{}_j(p_1)\bar\lambda_{\dot\delta}{}^k{}_m(p_2)
+\bar\lambda_{\dot\gamma}{}^k{}_j(p_1)\bar\lambda_{\dot\delta}{}^i{}_l(p_2)
\Big].
$$

### Wick pattern 21

$$
																									\Gamma_{21,\dot\beta}^{(1)}{}^i{}_j{}^k{}_l(p_1,p_2)
=
g^2\int_q^d
\Big[
-(q+p_2)_{+\dot\alpha}\,
\big(S_D(q+p_2)P_L\big)_{\alpha}{}^{\dot\alpha}
\Big]
\frac{2\,\epsilon^{\alpha\rho}}{q^2}\,
\big(S_D(q-p_1)P_L\big)_{\rho\dot\beta}\,
\mathscr C_{21}{}^i{}_j{}^k{}_l(p_1,p_2),
$$

$$
																									\mathscr C_{21}{}^i{}_j{}^k{}_l(p_1,p_2)
=
\mathscr C_{12}{}^i{}_j{}^k{}_l(p_2,p_1).
$$

### 4d part + evanescent part

把 (q=tilde q+hat q), external momenta 全在 4d 子空间：

$$
																									-(q+p_1)_{+\dot\alpha}
\big(S_D(q+p_1)P_L\big)_{\alpha}{}^{\dot\alpha}
=
i\left(
1-\frac{\hat q^2}{(q+p_1)^2}
\right)\epsilon_{+\alpha}.
$$

故

$$
																									\Gamma_{12,\dot\beta}^{(1)}
=
\Gamma_{12,\dot\beta}^{(0)}
+
\Gamma_{12,\dot\beta}^{(\mathrm{ev})},
$$

$$
																									\Gamma_{12,\dot\beta}^{(0)}{}^i{}_j{}^k{}_l
=
2g^2\int_q^d
\frac{(q-p_2)_{+\dot\beta}}{q^2(q-p_2)^2}\,
\mathscr C_{12}{}^i{}_j{}^k{}_l,
$$

$$
																									\Gamma_{12,\dot\beta}^{(\mathrm{ev})}{}^i{}_j{}^k{}_l
=
-2g^2\int_q^d
\frac{\hat q^2\,(q-p_2)_{+\dot\beta}}{q^2(q+p_1)^2(q-p_2)^2}\,
\mathscr C_{12}{}^i{}_j{}^k{}_l.
$$

同理

$$
																									\Gamma_{21,\dot\beta}^{(0)}{}^i{}_j{}^k{}_l
=
2g^2\int_q^d
\frac{(q-p_1)_{+\dot\beta}}{q^2(q-p_1)^2}\,
\mathscr C_{21}{}^i{}_j{}^k{}_l,
$$

$$
																									\Gamma_{21,\dot\beta}^{(\mathrm{ev})}{}^i{}_j{}^k{}_l
=
-2g^2\int_q^d
\frac{\hat q^2\,(q-p_1)_{+\dot\beta}}{q^2(q+p_2)^2(q-p_1)^2}\,
\mathscr C_{21}{}^i{}_j{}^k{}_l.
$$

$$
																									\Gamma^{(0)}
\ \text{是 naive 4d collapse 的 contact/EOM 部分；}
\qquad
\Gamma^{(\mathrm{ev})}
\ \text{才是 anomaly 部分。}
$$

### Feynman parameter evaluation of the anomalous term

$$
																								\frac{1}{q^2(q+p_1)^2(q-p_2)^2}
=
2\int_0^1 dx\,dy\,dz\,
\delta(1-x-y-z)\,
\frac{1}{\big[(q+y p_1-z p_2)^2+\Delta\big]^3},
$$

$$
																								\Delta
=
xy\,p_1^2+xz\,p_2^2+yz\,p^2,
\qquad
p=p_1+p_2.
$$

令

$$
\ell=q+y p_1-z p_2.
$$

则

$$
																								q-p_2
=
\ell-y p_1-(1-z)p_2
=
\ell-y p-x p_2.
$$

故 odd part 消失：

$$
																								\Gamma_{12,\dot\beta}^{(\mathrm{ev})}{}^i{}_j{}^k{}_l
=
4g^2
\int_0^1 dx\,dy\,dz\,
\delta(1-x-y-z)\,
(y p+x p_2)_{+\dot\beta}\,
I_{\hat2}(\Delta)\,
\mathscr C_{12}{}^i{}_j{}^k{}_l,
$$

$$
																								I_{\hat2}(\Delta)
:=
\mu^{2\epsilon}
\int\frac{d^d\ell}{(2\pi)^d}\,
\frac{\hat\ell^2}{(\ell^2+\Delta)^3}.
$$

由于分母只依赖 (ell^2),

$$
																								I_{\hat2}(\Delta)
=
\frac{d-4}{d}\,
\mu^{2\epsilon}
\int\frac{d^d\ell}{(2\pi)^d}\,
\frac{\ell^2}{(\ell^2+\Delta)^3}
=
\frac{d-4}{4}\,
\frac{\mu^{2\epsilon}}{(4\pi)^{2-\epsilon}}\,
\Gamma(\epsilon)\,
\Delta^{-\epsilon}.
$$

于是

$$
																								I_{\hat2}^{\mathrm{loc}}
=
-\frac{1}{32\pi^2}.
$$

从而

$$
																								\Gamma_{12,\dot\beta}^{(\mathrm{ev,loc})}{}^i{}_j{}^k{}_l
=
-\frac{g^2}{48\pi^2}\,
(p_1+2p_2)_{+\dot\beta}\,
\mathscr C_{12}{}^i{}_j{}^k{}_l,
$$

$$
																								\Gamma_{21,\dot\beta}^{(\mathrm{ev,loc})}{}^i{}_j{}^k{}_l
=
-\frac{g^2}{48\pi^2}\,
(2p_1+p_2)_{+\dot\beta}\,
\mathscr C_{21}{}^i{}_j{}^k{}_l.
$$

### final local anomaly

因为

$$
\mathscr C_{21}(p_1,p_2)=\mathscr C_{12}(p_2,p_1),
$$

且

$$
																								\epsilon^{\dot\gamma\dot\delta}
\bar\lambda_{\dot\gamma}(p_1)\bar\lambda_{\dot\delta}(p_2)
=
\epsilon^{\dot\gamma\dot\delta}
\bar\lambda_{\dot\gamma}(p_2)\bar\lambda_{\dot\delta}(p_1),
$$

故

$$
																								\Gamma_{\mathrm{anom},\dot\beta}^{(1)}{}^i{}_j{}^k{}_l(p)
=
-\frac{g^2}{16\pi^2}\,
p_{+\dot\beta}\,
\mathscr B{}^i{}_j{}^k{}_l(p),
$$

其中

$$
																								\mathscr B{}^i{}_j{}^k{}_l(p)
:=
\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)\,
\mathscr C_{12}{}^i{}_j{}^k{}_l(p_1,p_2).
$$

在 (U(N)) double-line 下，

$$
																								\mathscr B{}^i{}_j{}^k{}_l(p)
=
\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)\,
\epsilon^{\dot\gamma\dot\delta}
\Big[
2\,\bar\lambda_{\dot\gamma}{}^i{}_l(p_1)\bar\lambda_{\dot\delta}{}^k{}_j(p_2)
-\delta^k{}_j\,\bar\lambda_{\dot\gamma}{}^i{}_m(p_1)\bar\lambda_{\dot\delta}{}^m{}_l(p_2)
-\delta^i{}_l\,\bar\lambda_{\dot\gamma}{}^m{}_j(p_1)\bar\lambda_{\dot\delta}{}^k{}_m(p_2)
\Big].
$$

因此 momentum-space insertion 是

$$
																								\boxed{
\mathcal I\!\left[
\mathcal O_{\dot\beta}^{(1)\,\mathrm{loc}}{}^i{}_j{}^k{}_l(p)
\right]
=
-\frac{g^2}{16\pi^2}\,
p_{+\dot\beta}\,
\mathscr B{}^i{}_j{}^k{}_l(p)
}.
$$

等价地，position-space operator 是

$$
																								\boxed{
\mathcal O_{\dot\beta}^{(1)\,\mathrm{loc}}{}^i{}_j{}^k{}_l(x)
=
\frac{g^2}{16\pi^2}\,
i\partial_{+\dot\beta}\,
\mathscr B{}^i{}_j{}^k{}_l(x)
}.
$$

### one-line summary

$$
																								\Gamma^{(0)}\ \text{不是 anomaly；}
\qquad
\Gamma^{(\mathrm{ev})}\propto \hat q^2
\ \text{若无 UV pole 则严格为 }0;
\qquad
(d-4)\times \Gamma(\epsilon)
\ \text{给出上面的 finite local term。}
$$

</aside>

<aside>
💡

## $Q_1 (f_{++}\bar\lambda_{\dot\alpha})$  fourth attempt PV   (right answer, the same)

**anomaly 来自 PV mass term 在** $M\to\infty$ **之后留下的 finite local term**。

### PV setup

取一个 adjoint PV copy：fermion $(\Lambda_\alpha,\bar\Lambda_{\dot\alpha})$ 与 vector $B_{\alpha\dot\alpha}$，并取相同的 color projector

$$
\Pi^{ik}{}_{jl}:=\sum_a (T^a)^i{}_j(T^a)^k{}_l.
$$

relevant propagators（PV）：

$$
																																	\left\langle \Lambda_\alpha{}^i{}_j(p)\,\bar\Lambda_{\dot\beta}{}^k{}_l(-p)\right\rangle_{\rm PV}
=
-\frac{i\,p_{\alpha\dot\beta}}{p^2+M^2}\,\Pi^{ik}{}_{jl},
$$

$$
																																	\left\langle B_{\alpha\dot\alpha}{}^i{}_j(p)\,B_{\beta\dot\beta}{}^k{}_l(-p)\right\rangle_{\rm PV}
=
\frac{2\,\epsilon_{\alpha\beta}\epsilon_{\dot\alpha\dot\beta}}{p^2+M^2}\,\Pi^{ik}{}_{jl}.
$$

并记

$$
\int_q:=\int\frac{d^4q}{(2\pi)^4}.
$$

massive mixed fermion propagator（仍只取 $P_L$ 部分）：

$$
\big(S_M(k)P_L\big)_{\alpha\dot\alpha}=-\frac{i\,\tilde k_{\alpha\dot\alpha}}{k^2+M^2}.
$$

于是

$$
																																	-k_{+\dot\alpha}\,\big(S_M(k)P_L\big)_{\alpha}{}^{\dot\alpha}
=
i\,\frac{k_{+\dot\alpha}k_{\alpha}{}^{\dot\alpha}}{k^2+M^2}
=
i\,\epsilon_{+\alpha}-i\,\frac{M^2}{k^2+M^2}\,\epsilon_{+\alpha}.
$$

### Graph 12：PV loop 与 regulated splitting

先写 PV loop：

$$
																																	\Gamma_{12,\dot\beta}^{{\rm PV\text{-}loop}}{}^i{}_j{}^k{}_l
=
g^2\int_q
\Big[
-(q+p_1)_{+\dot\alpha}\,\big(S_M(q+p_1)P_L\big)_{\alpha}{}^{\dot\alpha}
\Big]
\frac{2\epsilon^{\alpha\rho}}{q^2+M^2}
\big(S_M(q-p_2)P_L\big)_{\rho\dot\beta}
\,\mathscr C_{12}{}^i{}_j{}^k{}_l.
$$

代入上一恒等式，得到两项分解：

$$
																																	\Gamma_{12,\dot\beta}^{{\rm PV\text{-}loop}}
=
2g^2\int_q\frac{(q-p_2)_{+\dot\beta}}{(q^2+M^2)\big((q-p_2)^2+M^2\big)}\,\mathscr C_{12}
-
2g^2M^2\int_q\frac{(q-p_2)_{+\dot\beta}}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}\,\mathscr C_{12}.
$$

因此把 **regulated amplitude** 写成

$$
																																	\Gamma_{12,\dot\beta}^{\rm reg}
=
\Big(\Gamma_{12,\dot\beta}^{(0)}-\Gamma_{12,\dot\beta;M}^{(0)}\Big)
+
\Gamma_{12,\dot\beta;M}^{({\rm anom})},
$$

其中（与本页 DRED 部分逐项对照）

$$
																																	\Gamma_{12,\dot\beta}^{(0)}
=
2g^2\int_q\frac{(q-p_2)_{+\dot\beta}}{q^2(q-p_2)^2}\,\mathscr C_{12},
$$

$$
																																	\Gamma_{12,\dot\beta;M}^{(0)}
=
2g^2\int_q\frac{(q-p_2)_{+\dot\beta}}{(q^2+M^2)\big((q-p_2)^2+M^2\big)}\,\mathscr C_{12},
$$

$$
																																	\Gamma_{12,\dot\beta;M}^{({\rm anom})}
=
2g^2M^2\int_q\frac{(q-p_2)_{+\dot\beta}}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}\,\mathscr C_{12}.
$$

前两项是 contact/EOM sector；最后一项由 **PV mass term** 产生，是 anomalous sector。

### Feynman parameter：提取 finite local term

对 $\Gamma_{12;M}^{({\rm anom})}$ 用参数化：

$$
																																	\frac{1}{(q^2+M^2)\big((q+p_1)^2+M^2\big)\big((q-p_2)^2+M^2\big)}
=
2\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
\frac{1}{\big[(q+yp_1-zp_2)^2+M^2+\Delta\big]^3},
$$

$$
\Delta=xy\,p_1^2+xz\,p_2^2+yz\,p^2,\qquad p=p_1+p_2.
$$

令

$$
\ell=q+yp_1-zp_2,
$$

则

$$
q-p_2=\ell-yp_1-(1-z)p_2=\ell-yp-xp_2.
$$

于是

$$
																																	\Gamma_{12,\dot\beta;M}^{({\rm anom})}
=
4g^2M^2\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
\int_\ell\frac{(\ell-yp-xp_2)_{+\dot\beta}}{(\ell^2+M^2+\Delta)^3}\,\mathscr C_{12}.
$$

odd part 消失，得到

$$
																																	\Gamma_{12,\dot\beta;M}^{({\rm anom})}
=
-4g^2M^2\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
(yp+xp_2)_{+\dot\beta}
\int_\ell\frac{1}{(\ell^2+M^2+\Delta)^3}\,\mathscr C_{12}.
$$

并用 4d Euclidean 标量积分

$$
																																	\int_\ell\frac{1}{(\ell^2+\Omega)^3}
=\int\frac{d^4\ell}{(2\pi)^4}\frac{1}{(\ell^2+\Omega)^3}
=\frac{1}{32\pi^2}\frac{1}{\Omega}.
$$

故

$$
																																	\Gamma_{12,\dot\beta;M}^{({\rm anom})}
=
-\frac{g^2}{8\pi^2}
\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
\frac{M^2}{M^2+\Delta}
(yp+xp_2)_{+\dot\beta}\,\mathscr C_{12}.
$$

将

$$
\frac{M^2}{M^2+\Delta}=1-\frac{\Delta}{M^2+\Delta}
$$

分解为 local + decoupling：

$$
																																	\Gamma_{12,\dot\beta;M}^{({\rm anom})}
=
\Gamma_{12,\dot\beta}^{({\rm anom,loc})}+\Gamma_{12,\dot\beta;M}^{({\rm anom,dec})},
\qquad
\lim_{M\to\infty}\Gamma_{12,\dot\beta;M}^{({\rm anom,dec})}=0.
$$

其中 local piece 为

$$
																																	\Gamma_{12,\dot\beta}^{({\rm anom,loc})}
=
-\frac{g^2}{8\pi^2}
\int_0^1dx\,dy\,dz\,\delta(1-x-y-z)
(yp+xp_2)_{+\dot\beta}\,\mathscr C_{12}.
$$

simplex 积分

$$
																																	\int dx\,dy\,dz\,\delta(1-x-y-z)\,x=\frac16,
\qquad
\int dx\,dy\,dz\,\delta(1-x-y-z)\,y=\frac16,
$$

因此

$$
																																	\Gamma_{12,\dot\beta}^{({\rm anom,loc})}{}^i{}_j{}^k{}_l
=
-\frac{g^2}{48\pi^2}
(p_1+2p_2)_{+\dot\beta}\,\mathscr C_{12}{}^i{}_j{}^k{}_l.
$$

### Graph 21 与求和

同理

$$
																																	\Gamma_{21,\dot\beta}^{({\rm anom,loc})}{}^i{}_j{}^k{}_l
=
-\frac{g^2}{48\pi^2}
(2p_1+p_2)_{+\dot\beta}\,\mathscr C_{21}{}^i{}_j{}^k{}_l.
$$

定义

$$
																																	\mathscr B{}^i{}_j{}^k{}_l(p)
:=
\int_{p_1,p_2}(2\pi)^4\delta^{(4)}(p-p_1-p_2)\,\mathscr C_{12}{}^i{}_j{}^k{}_l(p_1,p_2).
$$

用 $\mathscr C_{21}(p_1,p_2)=\mathscr C_{12}(p_2,p_1)$ 以及

$$
																																	\epsilon^{\dot\gamma\dot\delta}\bar\lambda_{\dot\gamma}(p_1)\bar\lambda_{\dot\delta}(p_2)
=
\epsilon^{\dot\gamma\dot\delta}\bar\lambda_{\dot\gamma}(p_2)\bar\lambda_{\dot\delta}(p_1),
$$

得到最终 anomalous local term

$$
																																	\Gamma_{\rm anom,\dot\beta}^{(1)}{}^i{}_j{}^k{}_l(p)
=
-\frac{g^2}{16\pi^2}\,p_{+\dot\beta}\,\mathscr B{}^i{}_j{}^k{}_l(p).
$$

对应的 insertion / operator mixing：

$$
																																	\boxed{\ 
\mathcal I\!\left[\mathcal O_{\dot\beta}^{(1),\rm loc}{}^i{}_j{}^k{}_l(p)\right]
=
-\frac{g^2}{16\pi^2}\,p_{+\dot\beta}\,\mathscr B{}^i{}_j{}^k{}_l(p)
\ }
$$

$$
																																	\boxed{\ 
\mathcal O_{\dot\beta}^{(1),\rm loc}{}^i{}_j{}^k{}_l(x)
=
\frac{g^2}{16\pi^2}\,i\partial_{+\dot\beta}\,\mathscr B{}^i{}_j{}^k{}_l(x)
\ }
$$

这与本页 DRED 的结论完全一致：EOM/contact sector 被 $\Gamma^{(0)}-\Gamma_M^{(0)}$ 吸收，anomaly 来自 PV mass term 留下的 finite local term。

</aside>

