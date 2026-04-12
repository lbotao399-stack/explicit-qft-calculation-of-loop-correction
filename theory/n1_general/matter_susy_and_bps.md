---
title: "N=1 General: matter, SUSY, and BPS data"
doc_type: theory
theory: "N=1 General"
status: canonical
---

# N=1 General: matter, SUSY, and BPS data

这份文档记录带一般 chiral matter 与 superpotential 的 `N=1` 理论输入，作为超出纯 `N=1 SYM` 时的通用背景。

## Matter multiplets and superpotential

取一组 chiral multiplets

$$
\Phi^i=(\phi^i,\psi^i_\alpha,F^i),\qquad
\widetilde\Phi_i=(\widetilde\phi_i,\widetilde\psi_{i\dot\alpha},\widetilde F_i).
$$

$(i,j,\ldots)$ 是 flavor/species index。gauge index 全部 suppress。$(phi,psi,F)$ 在某个 representation $(R)$。$(widetildephi,widetildepsi,widetilde F)$ 在 dual rep $(R^*)$。

协变导数写成

$$
D_{\alpha\dot\alpha}\phi=\partial_{\alpha\dot\alpha}\phi+A_{\alpha\dot\alpha}\phi,\qquad
D_{\alpha\dot\alpha}\psi_\beta=\partial_{\alpha\dot\alpha}\psi_\beta+A_{\alpha\dot\alpha}\psi_\beta,
$$

$$
D_{\alpha\dot\alpha}F=\partial_{\alpha\dot\alpha}F+A_{\alpha\dot\alpha}F,
$$

$$
D_{\alpha\dot\alpha}\widetilde\phi=\partial_{\alpha\dot\alpha}\widetilde\phi-\widetilde\phi A_{\alpha\dot\alpha},\qquad
D_{\alpha\dot\alpha}\widetilde\psi_{\dot\beta}=\partial_{\alpha\dot\alpha}\widetilde\psi_{\dot\beta}-\widetilde\psi_{\dot\beta}A_{\alpha\dot\alpha},
$$

$$
D_{\alpha\dot\alpha}\widetilde F=\partial_{\alpha\dot\alpha}\widetilde F-\widetilde F A_{\alpha\dot\alpha}.
$$

定义

$$
W_i:=\frac{\partial W}{\partial \phi^i},\qquad
W_{ij}:=\frac{\partial^2 W}{\partial \phi^i\partial \phi^j}=W_{ji},
$$

$$
\widetilde W^i:=\frac{\partial \widetilde W}{\partial \widetilde\phi_i},\qquad
\widetilde W^{ij}:=\frac{\partial^2 \widetilde W}{\partial \widetilde\phi_i\partial \widetilde\phi_j}
=\widetilde W^{ji}.
$$

并记

$$
\psi^i\psi^j:=\psi^{i\alpha}\psi^j_\alpha,\qquad
\widetilde\psi_i\widetilde\psi_j:=\widetilde\psi_{i\dot\alpha}\widetilde\psi_j^{\dot\alpha}.
$$

则 canonical Kähler 的 matter + superpotential component Lagrangian 是

$$
\mathcal L_{\rm matt}
=\frac12 D^{\alpha\dot\alpha}\widetilde\phi_i\,D_{\alpha\dot\alpha}\phi^i
+\widetilde\psi_{i\dot\alpha}D^{\dot\alpha\alpha}\psi^i_\alpha
-\widetilde F_i F^i
+\sqrt2\,i\,\widetilde\phi_i\lambda^\alpha\psi^i_\alpha
-\sqrt2\,i\,\widetilde\psi_{i\dot\alpha}\widetilde\lambda^{\dot\alpha}\phi^i
+\widetilde\phi_i\mathcal D\phi^i.
$$

$$
\mathcal L_W
=F^iW_i(\phi)-\frac12 W_{ij}(\phi)\,\psi^i\psi^j
+\widetilde F_i\widetilde W^i(\widetilde\phi)
-\frac12 \widetilde W^{ij}(\widetilde\phi)\,\widetilde\psi_i\widetilde\psi_j.
$$

$$
\boxed{\mathcal L_{\rm tot}^{\rm new}
=\mathcal L_{\rm SYM}
+\mathcal L_{\rm gf+gh}
+\mathcal L_{\rm matt}
+\mathcal L_W }.
$$

其中 $(W,\widetilde W)$ 要满足 gauge invariance：

$$
W_i(\phi)(T^a\phi)^i=0,\qquad
(\widetilde\phi T^a)_i\,\widetilde W^i(\widetilde\phi)=0.
$$

若你最后要改回 $(\bar\lambda)$ 记号，只需

$$
\widetilde\lambda_{\dot\alpha}\mapsto \bar\lambda_{\dot\alpha}.
$$

### 2. SUSY 作用在 matter components 上（off-shell，不除 EOM）

$$
\delta\phi^i=\sqrt2\,\zeta^\alpha\psi^i_\alpha.
$$

$$
\delta\psi^i_\alpha
=\sqrt2\,\zeta_\alpha F^i
+i\sqrt2\,\widetilde\zeta^{\dot\alpha}D_{\alpha\dot\alpha}\phi^i.
$$

$$
\delta F^i
=i\sqrt2\,\widetilde\zeta^{\dot\alpha}D_{\alpha\dot\alpha}\psi^{i\alpha}
-2\,\widetilde\zeta_{\dot\alpha}\widetilde\lambda^{\dot\alpha}\phi^i.
$$

$$
\delta\widetilde\phi_i
=\sqrt2\,\widetilde\zeta_{\dot\alpha}\widetilde\psi_i^{\dot\alpha}.
$$

$$
\delta\widetilde\psi_{i\dot\alpha}
=\sqrt2\,\widetilde\zeta_{\dot\alpha}\widetilde F_i
-i\sqrt2\,\zeta^\alpha D_{\alpha\dot\alpha}\widetilde\phi_i.
$$

$$
\delta\widetilde F_i
=-i\sqrt2\,\zeta^\alpha D_{\alpha\dot\alpha}\widetilde\psi_i^{\dot\alpha}
+2\,\widetilde\phi_i\zeta^\alpha\lambda_\alpha.
$$

closure 仍然是同一个

$$
[\delta_1,\delta_2]
= v^{\alpha\dot\alpha}D_{\alpha\dot\alpha}+\delta_{\rm gauge}(\omega),
$$

$$
v_{\alpha\dot\alpha}=2i(\zeta_{2\alpha}\widetilde\zeta_{1\dot\alpha}-\zeta_{1\alpha}\widetilde\zeta_{2\dot\alpha}),
\qquad
\omega=-v^{\beta\dot\beta}A_{\beta\dot\beta}.
$$

### 3. 单独抽 $Q_-$

仍按你文档里的定义

$$
Q_-:\qquad
\zeta^-=1,\quad \zeta^+=0,\quad \widetilde\zeta^{\dot\alpha}=0,
\qquad
\zeta_+=1,\quad \zeta_-=0.
$$

**chiral multiplet**

$$
Q_-\phi^i=\sqrt2\,\psi^i_-.
$$

$$
Q_-\psi^i_+=\sqrt2\,F^i,\qquad
Q_-\psi^i_-=0.
$$

$$
Q_-F^i=0.
$$

**anti-chiral multiplet**

$$
Q_-\widetilde\phi_i=0.
$$

$$
Q_-\widetilde\psi_{i\dot\alpha}
=-i\sqrt2\,D_{-\dot\alpha}\widetilde\phi_i.
$$

即

$$
Q_-\widetilde\psi_{i\dot+}=-i\sqrt2\,D_{-\dot+}\widetilde\phi_i,\qquad
Q_-\widetilde\psi_{i\dot-}=-i\sqrt2\,D_{-\dot-}\widetilde\phi_i.
$$

$$
Q_-\widetilde F_i
=-i\sqrt2\,D_{-\dot\alpha}\widetilde\psi_i^{\dot\alpha}
+2\,\widetilde\phi_i\lambda_-.
$$

对 $(W,\widetilde W)$ 的直接作用

$$
Q_-W(\phi)=\sqrt2\,W_i\psi^i_-,\qquad
Q_-W_i=\sqrt2\,W_{ij}\psi^j_-,\qquad
Q_-\widetilde W(\widetilde\phi)=0,\qquad
Q_-\widetilde W^i=0.
$$

于是

$$
Q_-\left(F^iW_i-\frac12 W_{ij}\psi^i\psi^j\right)=0.
$$

free limit $(g=0)$ 时只需

$$
D_{\alpha\dot\alpha}\to \partial_{\alpha\dot\alpha},\qquad
Q_-\widetilde F_i=-i\sqrt2\,\partial_{-\dot\alpha}\widetilde\psi_i^{\dot\alpha}.
$$

# Add matter : susy transformation and BPS

继续用你 note 的 flat Euclidean / WZ gauge / spinor conventions；并记

$$
\bar\lambda_{\dot\alpha}:=\widetilde\lambda_{\dot\alpha},\qquad
\bar\phi_i:=\widetilde\phi_i,\qquad
\bar\psi_{i\dot\alpha}:=\widetilde\psi_{i\dot\alpha},\qquad
\bar F_i:=\widetilde F_i,
$$

bar 在这里都只是记号，不是 complex conjugation。gauge-sector 的 conventions 与你 note 完全一致。

定义

$$
W_i:=\frac{\partial W}{\partial \phi^i},\qquad
\bar W^i:=\frac{\partial \widetilde W}{\partial \bar\phi_i},\qquad
\mu^a:=\bar\phi_i (T^a\phi)^i.
$$

---

## 1. 先只 integrate out $(mathcal D,F,bar F)$，不再用别的 EOM

### auxiliary equations

由

$$
\mathcal L_{\rm aux} = \frac1{2g^2}\mathcal D^a\mathcal D^a+\mathcal D^a\mu^a-\bar F_iF^i+F^iW_i+\bar F_i\bar W^i
$$

得

$$
\frac{\partial \mathcal L}{\partial \mathcal D^a}= \frac1{g^2}\mathcal D^a+\mu^a=0
\quad\Longrightarrow\quad
\boxed{\mathcal D^a=-g^2\mu^a},
$$

$$
\frac{\partial \mathcal L}{\partial F^i}=-\bar F_i+W_i=0
\quad\Longrightarrow\quad
\boxed{\bar F_i=W_i},
$$

$$
\frac{\partial \mathcal L}{\partial \bar F_i}=-F^i+\bar W^i=0
\quad\Longrightarrow\quad
\boxed{F^i=\bar W^i}.
$$

### general SUSY after substitution

这里只是把 auxiliary EOM 直接代回 off-shell rules；**不**再用 $(\lambda,\psi,\phi,f)$ 的 dynamical EOM。

gauge multiplet:

$$
\delta A_{\alpha\dot\alpha}^a = i\zeta_\alpha\bar\lambda_{\dot\alpha}^a+i\widetilde\zeta_{\dot\alpha}\lambda_\alpha^a,
$$

$$
\delta\lambda_\alpha^a = f_{\alpha\beta}^a\zeta^\beta + i g^2\mu^a\zeta_\alpha,
$$

$$
\delta\bar\lambda_{\dot\alpha}^a = \bar f_{\dot\alpha\dot\beta}^a\widetilde\zeta^{\dot\beta}+i g^2\mu^a\widetilde\zeta_{\dot\alpha},
$$

$$
\delta f_{\alpha\beta}^a = i\zeta_{(\alpha}D_{\beta)\dot\gamma}\bar\lambda^{a\dot\gamma}+i\widetilde\zeta^{\dot\gamma}D_{(\alpha|\dot\gamma|}\lambda_{\beta)}^a,
$$

$$
\delta \bar f_{\dot\alpha\dot\beta}^a = i\widetilde\zeta_{(\dot\alpha}D_{\gamma\dot\beta)}\lambda^{a\gamma} +i\zeta^\gamma D_{\gamma(\dot\alpha}\bar\lambda_{\dot\beta)}^a.
$$

matter multiplet:

$$
\delta\phi^i=\sqrt2\zeta^\alpha\psi_\alpha^i,
$$

$$
\delta\psi_\alpha^i = \sqrt2\zeta_\alpha\bar W^i+i\sqrt2\widetilde\zeta^{\dot\alpha}D_{\alpha\dot\alpha}\phi^i,
$$

$$
\delta\bar\phi_i=\sqrt2\widetilde\zeta_{\dot\alpha}\bar\psi_i^{\dot\alpha},
$$

$$
\delta\bar\psi_{i\dot\alpha} = \sqrt2\widetilde\zeta_{\dot\alpha}W_i - i\sqrt2\zeta^\alpha D_{\alpha\dot\alpha}\bar\phi_i.
$$

composite auxiliaries 现在变成

$$
Q_-\mathcal D^a=-g^2Q_-\mu^a,\qquad
Q_-F^i=Q_-\bar W^i,\qquad
Q_-\bar F_i=Q_-W_i.
$$

并且

$$
\delta\mu^a = \sqrt2\zeta^\alpha\bar\phi_i(T^a\psi_\alpha)^i +\sqrt2\widetilde\zeta_{\dot\alpha}(\bar\psi^{\dot\alpha}T^a\phi),
$$

$$
\delta W_i=\sqrt2 W_{ij}\zeta^\alpha\psi_\alpha^j,\qquad
\delta\bar W^i=\sqrt2\bar W^{ij}\widetilde\zeta_{\dot\alpha}\bar\psi_j^{\dot\alpha}.
$$

### raw $Q_-$ action

取

$$
Q_-:\qquad \zeta^-=1,\ \zeta^+=0,\ \widetilde\zeta^{\dot\alpha}=0,
\qquad \zeta_+=1,\ \zeta_-=0.
$$

先写 basic letters。gauge 部分与你 note 一致，只是 $(mathcal Dto -g^2mu)$。

### gauge multiplet

$$
Q_-A_{+\dot\alpha}^a=i\bar\lambda_{\dot\alpha}^a,\qquad
Q_-A_{-\dot\alpha}^a=0.
$$

$$
Q_-\lambda_+^a=f_{+-}^a-i g^2\mu^a,\qquad
Q_-\lambda_-^a=f_{--}^a,
$$

$$
Q_-\bar\lambda_{\dot\alpha}^a=0.
$$

$$
Q_-f_{++}^a=iD_{+\dot\alpha}\bar\lambda^{a\dot\alpha},
$$

$$
Q_-f_{+-}^a=\frac{i}{2}D_{-\dot\alpha}\bar\lambda^{a\dot\alpha},
$$

$$
Q_-f_{--}^a=0.
$$

$$
Q_-\bar f_{\dot\alpha\dot\beta}^a = iD_{-(\dot\alpha}\bar\lambda_{\dot\beta)}^a,
$$

即

$$
Q_-\bar f_{\dot+\dot+}^a=iD_{-\dot+}\bar\lambda_{\dot+}^a,
$$

$$
Q_-\bar f_{\dot+\dot-}^a=\frac{i}{2} \Big(D_{-\dot+}\bar\lambda_{\dot-}^a+D_{-\dot-}\bar\lambda_{\dot+}^a\Big),
$$

$$
Q_-\bar f_{\dot-\dot-}^a=iD_{-\dot-}\bar\lambda_{\dot-}^a.
$$

并且

$$
Q_-\mu^a=\sqrt2\bar\phi_i(T^a\psi_- )^i,
\qquad
Q_-\mathcal D^a=-\sqrt2 g^2\bar\phi_i(T^a\psi_-)^i.
$$

### matter multiplet

$$
Q_-\phi^i=\sqrt2\psi_-^i,
$$

$$
Q_-\psi_+^i=\sqrt2\bar W^i,\qquad Q_-\psi_-^i=0,
$$

$$
Q_-\bar\phi_i=0,
$$

$$
Q_-\bar\psi_{i\dot\alpha} = - i\sqrt2 D_{-\dot\alpha}\bar\phi_i,
$$

即

$$
Q_-\bar\psi_{i\dot+}=-i\sqrt2 D_{-\dot+}\bar\phi_i,
\qquad
Q_-\bar\psi_{i\dot-}=-i\sqrt2 D_{-\dot-}\bar\phi_i.
$$

以及

$$
Q_-W_i=\sqrt2 W_{ij}\psi_-^j,\qquad
Q_-\bar W^i=0,
$$

$$
Q_-F^i=Q_-\bar W^i=0,\qquad
Q_-\bar F_i=Q_-W_i=\sqrt2 W_{ij}\psi_-^j.
$$

### descendants 的统一公式

对 adjoint-valued $X$:

$$
Q_-\big(D_{\alpha\dot\alpha}X\big) = D_{\alpha\dot\alpha}(Q_-X) +i\delta_{\alpha+}[\bar\lambda_{\dot\alpha},X].
$$

对 $R$-representation 的 $Y$:

$$
Q_-\big(D_{\alpha\dot\alpha}Y\big) = D_{\alpha\dot\alpha}(Q_-Y) +i\delta_{\alpha+}\bar\lambda_{\dot\alpha}Y.
$$

对 dual representation 的 $bar Y$:

$$
Q_-\big(D_{\alpha\dot\alpha}\bar Y\big) = D_{\alpha\dot\alpha}(Q_-\bar Y) - i\delta_{\alpha+}\bar Y\bar\lambda_{\dot\alpha}.
$$

free limit 时直接

$$
D_{\alpha\dot\alpha}\to \partial_{\alpha\dot\alpha}.
$$

---

## 2. free level 的 $Q_-$ BPS letters

现在取

$$
g=0,\qquad W=0,\qquad \widetilde W=0,
$$

所以

$$
\mathcal D=0,\qquad F=0,\qquad \bar F=0.
$$

### free raw $Q_-$

gauge:

$$
Q_-\bar\lambda_{\dot\alpha}=0,\qquad
Q_-\lambda_+=f_{+-},\qquad
Q_-\lambda_-=f_{--},
$$

$$
Q_-f_{++}=i\partial_{+\dot\alpha}\bar\lambda^{\dot\alpha},\qquad
Q_-f_{+-}=\frac{i}{2}\partial_{-\dot\alpha}\bar\lambda^{\dot\alpha},\qquad
Q_-f_{--}=0,
$$

$$
Q_-\bar f_{\dot\alpha\dot\beta}=i\partial_{-(\dot\alpha}\bar\lambda_{\dot\beta)}.
$$

matter:

$$
Q_-\phi^i=\sqrt2\psi_-^i,
\qquad
Q_-\psi_+^i=0,
\qquad
Q_-\psi_-^i=0,
$$

$$
Q_-\bar\phi_i=0,
\qquad
Q_-\bar\psi_{i\dot\alpha}=-i\sqrt2\partial_{-\dot\alpha}\bar\phi_i.
$$

### free EOM

gauge-sector:

$$
\partial_{+\dot\alpha}\bar\lambda^{\dot\alpha}=0,\qquad
\partial_{-\dot\alpha}\bar\lambda^{\dot\alpha}=0.
$$

这正是你 note 里前面已经用过的 free gaugino EOM。

matter-sector:

$$
\partial^{\alpha\dot\alpha}\partial_{\alpha\dot\alpha}\phi^i=0,\qquad
\partial^{\alpha\dot\alpha}\partial_{\alpha\dot\alpha}\bar\phi_i=0,
$$

$$
\partial^{\dot\alpha\alpha}\psi_\alpha^i=0,\qquad
\partial_{\alpha\dot\alpha}\bar\psi_i^{\dot\alpha}=0.
$$

把 $\partial^{\dot\alpha\alpha}\psi_\alpha^i=0$ 写成分量：

$$
\partial_{-\dot-}\psi_+^i-\partial_{+\dot-}\psi_-^i=0,
$$

$$
- \partial_{-\dot+}\psi_+^i+\partial_{+\dot+}\psi_-^i=0.
$$

即

$$
\partial_{+\dot-}\psi_-^i=\partial_{-\dot-}\psi_+^i,
\qquad
\partial_{+\dot+}\psi_-^i=\partial_{-\dot+}\psi_+^i.
$$

## closed / exact / cohomology

先看 **basic letters**。

### $Q_-$-closed set

$$
\ker Q_-\cap\{\bar\lambda,f,\bar\phi,\psi,\bar\psi\} = \{\bar\lambda_{\dot+},\bar\lambda_{\dot-},f_{++},f_{+-},f_{--},\bar\phi_i,\psi_+^i,\psi_-^i\}.
$$

这里

$$
Q_-f_{++}=0,\qquad Q_-f_{+-}=0
$$

是用了 free gaugino EOM；

而

$$
Q_-\bar\phi_i=0,\qquad Q_-\psi_\pm^i=0
$$

不需要别的 EOM。

### $Q_-$-exact set

$$
f_{+-}=Q_-\lambda_+,\qquad
f_{--}=Q_-\lambda_-,
$$

$$
\psi_-^i=\frac1{\sqrt2}Q_-\phi^i.
$$

所以

$$
\operatorname{Im}Q_-\cap\{\bar\lambda,f,\bar\phi,\psi,\bar\psi\} = \{f_{+-},f_{--},\psi_-^i\}.
$$

### cohomology

因此真正 surviving 的 free $Q_-$-BPS basic letters 是

$$
\boxed{H^0(Q_-;\{\rm letters\})_{\rm basic}^{\rm free} = \{\bar\lambda_{\dot+},\ \bar\lambda_{\dot-},\ f_{++},\ \bar\phi_i,\ \psi_+^i\}. }
$$

所以你猜的

$$
f_{++},\ \bar\lambda,\ \bar\phi_i,\ \psi_{+或-}
$$

里，**strict cohomology** 结果是

$$
\boxed{\psi_+^i\ \text{survives},\qquad \psi_-^i\ \text{closed but exact}.}
$$

---

## descendants

由 free SUSY algebra

$$
\{Q_-,\widetilde Q_{\dot\alpha}\}=2i\partial_{-\dot\alpha}
$$

得

$$
\partial_{-\dot\alpha}\mathcal O\in \operatorname{Im}Q_-.
$$

因此只保留 $partial_{+dotalpha}$-descendants：

$$
\partial_{+\dot+}^m\partial_{+\dot-}^n\bar\lambda_{\dot\beta},
\qquad
\partial_{+\dot+}^m\partial_{+\dot-}^n f_{++},
\qquad
\partial_{+\dot+}^m\partial_{+\dot-}^n \bar\phi_i,
\qquad
\partial_{+\dot+}^m\partial_{+\dot-}^n \psi_+^i.
$$

gauge-sector 仍有 relation

$$
\partial_{+\dot-}\bar\lambda_{\dot+} = \partial_{+\dot+}\bar\lambda_{\dot-}.
$$

matter-sector 则

$$
\partial_{-\dot\alpha}\bar\phi_i = \frac{i}{\sqrt2}Q_-\bar\psi_{i\dot\alpha},
$$

$$
\psi_-^i=\frac1{\sqrt2}Q_-\phi^i,
$$

$$
\partial_{+\dot-}\psi_-^i=\partial_{-\dot-}\psi_+^i\in \operatorname{Im}Q_-,
\qquad
\partial_{+\dot+}\psi_-^i=\partial_{-\dot+}\psi_+^i\in \operatorname{Im}Q_-.
$$

因此 full free $Q_-$-BPS descendant letters 就是

$$
\boxed{
\partial_{+\dot+}^m\partial_{+\dot-}^n\bar\lambda_{\dot\beta},\quad
\partial_{+\dot+}^m\partial_{+\dot-}^n f_{++},\quad
\partial_{+\dot+}^m\partial_{+\dot-}^n\bar\phi_i,\quad
\partial_{+\dot+}^m\partial_{+\dot-}^n\psi_+^i
\qquad (m,n\ge 0).
}
$$

如果下一步你要，我可以继续把这套 letters 的 quantum numbers $(E,j_+,j_-,r)$ 和 single-letter index 也直接算出来。
