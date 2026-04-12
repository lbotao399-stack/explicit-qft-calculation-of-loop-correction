---
title: "N=4 SYM: action and SUSY"
doc_type: theory
theory: "N=4 SYM"
status: canonical
---

# N=4 SYM: action and SUSY

这份文档收录 `N=4 SYM` 的场内容、分量作用量、SUSY 变换以及与 `N=1` 记号的对应。

## $SU(4)_R$-covariant field content

$$
	A_{\alpha\dot\alpha},\qquad
\lambda^A_\alpha,\qquad
\bar\lambda_{A\dot\alpha},\qquad
\phi^{AB}=-\phi^{BA},\qquad
A,B=1,2,3,4.
$$

并记

$$
	\epsilon^{1234}=1,\qquad
\bar\phi_{AB}:=\frac12\epsilon_{ABCD}\phi^{CD}
$$

这在这里是 epsilon-dual notation，不是 complex conjugation。

和你前面的 $\mathcal N=1$ basis 的对应是

$$
	\lambda^A=(\psi^1,\psi^2,\psi^3,\lambda),\qquad
\bar\lambda_A=(\bar\psi_1,\bar\psi_2,\bar\psi_3,\bar\lambda),
$$

$$
	\phi^{i4}=\phi^i,\qquad
\phi^{ij}=\epsilon^{ijk}\bar\phi_k,\qquad
\bar\phi_{i4}=\bar\phi_i,\qquad
\bar\phi_{ij}=\epsilon_{ijk}\phi^k,
\qquad i,j,k=1,2,3.
$$

---

## 1. full component action

### compact $SU(4)_R$-covariant form

$$
	S_{\mathcal N=4} = \frac{1}{g^2}\int d^4x\ \operatorname{tr}\Bigg[
\frac14 F_{\mu\nu}F_{\mu\nu}
+\bar\lambda_{A\dot\alpha}D^{\dot\alpha\alpha}\lambda^A_\alpha
+\frac18 D^{\alpha\dot\alpha}\bar\phi_{AB} D_{\alpha\dot\alpha}\phi^{AB}
$$

$$
	\qquad\qquad\qquad
+\frac{i}{\sqrt2} \lambda^{A\alpha} [\bar\phi_{AB},\lambda^B_\alpha]
+\frac{i}{\sqrt2} \bar\lambda_{A\dot\alpha} [\phi^{AB},\bar\lambda_B^{\dot\alpha}]
+\frac1{16} [\phi^{AB},\phi^{CD}][\bar\phi_{AB},\bar\phi_{CD}]
\Bigg].
$$

若要加 topological term，再加

$$
\Delta \mathcal L_\theta = \frac{i\theta}{32\pi^2}\operatorname{tr}\big(\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}\big),
$$

它单独也是 SUSY-invariant。

### 等价地，写成你前面 $\mathcal N=1$ 的 $(\lambda,\psi^i,\phi^i)$ basis

$$
	\mathcal L_{\mathcal N=4} = \frac{1}{g^2}\operatorname{tr}\Bigg[
\frac14F_{\mu\nu}F_{\mu\nu}
+\bar\lambda_{\dot\alpha}D^{\dot\alpha\alpha}\lambda_\alpha
+\bar\psi_{i\dot\alpha}D^{\dot\alpha\alpha}\psi^i_\alpha
+\frac12 D^{\alpha\dot\alpha}\bar\phi_i D_{\alpha\dot\alpha}\phi^i
$$

$$
	\qquad
+\sqrt2 i \bar\phi_i[\lambda^\alpha,\psi^i_\alpha]
- \sqrt2 i \bar\psi_{i\dot\alpha}[\bar\lambda^{\dot\alpha},\phi^i]
- \frac{i}{\sqrt2}\epsilon_{ijk}\psi^{i\alpha}[\psi^j_\alpha,\phi^k]
- \frac{i}{\sqrt2}\epsilon^{ijk}\bar\psi_{i\dot\alpha}[\bar\psi_j^{\dot\alpha},\bar\phi_k]
$$

$$
	\qquad
- \frac12[\phi^i,\bar\phi_i][\phi^j,\bar\phi_j]
+[\phi^i,\phi^j][\bar\phi_i,\bar\phi_j]
\Bigg].
$$

这里 quartic term 和 compact form 的精确恒等式是

$$
\frac1{16}[\phi^{AB},\phi^{CD}][\bar\phi_{AB},\bar\phi_{CD}] = - \frac12[\phi^i,\bar\phi_i][\phi^j,\bar\phi_j] +[\phi^i,\phi^j][\bar\phi_i,\bar\phi_j].
$$

---

## 2. full SUSY transformations

取 16 个 supercharges 的参数

$$
\delta=\zeta^{A\alpha}Q_{A\alpha}+\widetilde\zeta_A^{\dot\alpha}\widetilde Q^A_{\dot\alpha}.
$$

### basic fields

$$
\delta A_{\alpha\dot\alpha} = i \zeta^A_\alpha \bar\lambda_{A\dot\alpha} + i \widetilde\zeta_{A\dot\alpha} \lambda^A_\alpha.
$$

$$
\delta\phi^{AB} = \sqrt2\big(\zeta^{B\alpha}\lambda^A_\alpha-\zeta^{A\alpha}\lambda^B_\alpha\big) - \sqrt2 \epsilon^{ABCD}\widetilde\zeta_{C\dot\alpha}\bar\lambda_D^{\dot\alpha}.
$$

$$
\delta\bar\phi_{AB} = \sqrt2\big(\widetilde\zeta_{B\dot\alpha}\bar\lambda_A^{\dot\alpha} - \widetilde\zeta_{A\dot\alpha}\bar\lambda_B^{\dot\alpha}\big) - \sqrt2 \epsilon_{ABCD}\zeta^{C\alpha}\lambda^D_\alpha.
$$

$$
\delta\lambda^A_\alpha = f_{\alpha\beta}\zeta^{A\beta} + i\sqrt2 D_{\alpha\dot\alpha}\phi^{AB} \widetilde\zeta_B^{\dot\alpha} + i [\phi^{AB},\bar\phi_{BC}] \zeta^C_\alpha.
$$

$$
\delta\bar\lambda_{A\dot\alpha} = \bar f_{\dot\alpha\dot\beta}\widetilde\zeta_A^{\dot\beta} - i\sqrt2 D_{\alpha\dot\alpha}\bar\phi_{AB} \zeta^{B\alpha} + i [\bar\phi_{AB},\phi^{BC}] \widetilde\zeta_{C\dot\alpha}.
$$

### induced variation of field strengths

$$
\delta f_{\alpha\beta} = i \zeta^A_{(\alpha}D_{\beta)\dot\gamma}\bar\lambda_A^{\dot\gamma} + i \widetilde\zeta_A^{\dot\gamma}D_{(\alpha|\dot\gamma|}\lambda^A_{\beta)}.
$$

$$
\delta\bar f_{\dot\alpha\dot\beta} = i \widetilde\zeta_{A(\dot\alpha}D_{\gamma\dot\beta)}\lambda^{A\gamma} + i \zeta^{A\gamma}D_{\gamma(\dot\alpha}\bar\lambda_{A\dot\beta)}.
$$

---

## 3. 和你前面的 $\mathcal N=1$ 公式对一下

若只开

$$
	\zeta^4_\alpha=\zeta_\alpha,\qquad
\widetilde\zeta_{4\dot\alpha}=\widetilde\zeta_{\dot\alpha},
\qquad
\zeta^i=\widetilde\zeta_i=0,
$$

则正好得到你之前那套 $\mathcal N=1$ 变换、并且已经把 $(D,F)$ 积分掉：

$$
\delta\lambda_\alpha = f_{\alpha\beta}\zeta^\beta - i[\phi^i,\bar\phi_i]\zeta_\alpha,
$$

$$
\delta\psi^i_\alpha = i\sqrt2 D_{\alpha\dot\alpha}\phi^i \widetilde\zeta^{\dot\alpha} - i \epsilon^{ijk}[\bar\phi_j,\bar\phi_k]\zeta_\alpha,
$$

$$
\delta\bar\psi_{i\dot\alpha} = - i\sqrt2 D_{\alpha\dot\alpha}\bar\phi_i \zeta^\alpha - i \epsilon_{ijk}[\phi^j,\phi^k]\widetilde\zeta_{\dot\alpha}.
$$

---

## 4. closure

因为这里没有 auxiliary fields，closure 是 on-shell：

$$
[\delta_1,\delta_2] = v^{\alpha\dot\alpha}D_{\alpha\dot\alpha} +\delta_{\rm gauge}(\omega),
$$

$$
	v_{\alpha\dot\alpha} = 2i\big(
\zeta^A_{2\alpha}\widetilde\zeta_{1A\dot\alpha}
- \zeta^A_{1\alpha}\widetilde\zeta_{2A\dot\alpha}
\big),
\qquad
\omega=-v^{\beta\dot\beta}A_{\beta\dot\beta},
$$

并且在 fermion / scalar EOM 上闭合。

我已经按两条 route 检过一次：

一条是 先还原到 $A=4$ 的 manifest $\mathcal N=1$ off-shell system，再把 $(D,F)$ 消掉；

另一条是 利用整个 action 的 $SU(4)_R$-covariance，把这个 manifest supercharge 旋转成全部 16 个 supercharges。

两条 route 给出的系数完全一致，所以这套 $\delta$ 的确使上面的 action 不变。

如果你下一步要，我可以直接在这套记号下继续做 $Q_-\subset \mathcal N=4$ 的 BPS letters / cohomology。
