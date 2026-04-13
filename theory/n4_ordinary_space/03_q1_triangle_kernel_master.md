---
title: "N=4 ordinary-space: Q_1 one-loop local basis master"
doc_type: theory
theory: "N=4 SYM ordinary-space"
status: working
---

# N=4 ordinary-space: Q_1 one-loop local basis master

## 1. Correction to the old reduction

$$
\boxed{
\text{the no-derivative bi-letter problem is not a universal }2\to1\text{ kernel problem.}
}
$$

对
$$
\mathcal O_{FF}(y):=\Tr\!\big(F_{\rm raw}F_{\rm raw}\big)(y),
\qquad
\Delta(F_{\rm raw})=2,
\qquad
\Delta(Q_1)=\frac12,
$$
有
$$
\Delta\!\big(Q_1\mathcal O_{FF}\big)=\frac92.
$$

因此一圈修正不能落到单个 no-derivative letter 上，而必须落到导数二字母 sector。

$$
\boxed{
Q_1(\Tr(F_{\rm raw}F_{\rm raw}))\text{ at one loop is a }2\to2\text{ derivative problem.}
}
$$

## 2. Correct general workflow

对任意输入
$$
\mathcal O_{L_1L_2}=\Tr(L_1L_2),
\qquad
L_1,L_2\in\{X_i,\Psi^i,F\},
$$
先做
$$
\mathcal B_{L_1L_2}^{1\text{-loop}}
$$
的局域基底分类，再去算系数。

$$
\boxed{
\text{input bi-letter}
\ \to\
\text{classical }Q_1\text{ target}
\ \to\
\text{1-loop local basis classification}
\ \to\
\text{relevant current branches}
\ \to\
\text{all admissible cubic triangle classes}
\ \to\
\text{local reduction onto the chosen basis}.
}
$$

## 3. First true seed: \(Q_1(FF)\)

raw notation:
$$
\mathcal O_{FF}(y):=\Tr\!\big(F_{\rm raw}F_{\rm raw}\big)(y),
\qquad
F_{\rm raw}=f^{\rm raw}_{++}.
$$

classical target:
$$
Q_1F_{\rm raw}
=
i\,\nabla_{+\dot\alpha}\bar\Lambda^{\dot\alpha},
$$

$$
\boxed{
Q_1^{\rm cl}\mathcal O_{FF}
=
i\,\Tr\!\Big[
(\nabla_{+\dot\alpha}\bar\Lambda^{\dot\alpha})\,F_{\rm raw}
+
F_{\rm raw}\,(\nabla_{+\dot\alpha}\bar\Lambda^{\dot\alpha})
\Big].
}
$$

The corrected AWI ansatz is
$$
\boxed{
\big[\partial_\mu J^\mu_{Q_1}(x)\,\mathcal O_{FF}(y)\big]^{1\text{-loop}}_{\rm loc}
=
-\delta^{(4)}(x-y)\,Q_1^{\rm cl}\mathcal O_{FF}(y)
-\frac{g_{\rm YM}^2}{8\pi^2}\,\delta^{(4)}(x-y)\,
\Big(
c_{F\bar\Lambda}^{\rm raw}\,\mathcal K_{F\bar\Lambda}^{\rm raw}
+
c_{\Psi X}^{\rm raw}\,\mathcal K_{\Psi X}^{\rm raw}
\Big)(y).
}
$$

## 4. Minimal independent raw basis for \(Q_1(FF)\)

$$
\boxed{
\mathcal K_{F\bar\Lambda}^{\rm raw}
:=
\Tr\!\big[
(\nabla_{+\dot\alpha}F_{\rm raw})\,\bar\Lambda^{\dot\alpha}
\big],
}
$$

$$
\boxed{
\mathcal K_{\Psi X}^{\rm raw}
:=
\Tr\!\big[
(\nabla_{+\dot\alpha}\Psi^i_+)\,(\nabla_+^{\dot\alpha}X_i)
\big].
}
$$

$$
\nabla_{+\dot\alpha}\Tr(F_{\rm raw}\bar\Lambda^{\dot\alpha})
=
\Tr\!\big[(\nabla_{+\dot\alpha}F_{\rm raw})\bar\Lambda^{\dot\alpha}\big]
+
\Tr\!\big[F_{\rm raw}\nabla_{+\dot\alpha}\bar\Lambda^{\dot\alpha}\big].
$$

第二项正是 classical \(Q_1F_{\rm raw}\) channel，所以不是新的 one-loop basis element。

$$
\nabla_{+\dot\alpha}\Tr(\Psi^i_+\nabla_+^{\dot\alpha}X_i)
=
\Tr\!\big[(\nabla_{+\dot\alpha}\Psi^i_+)(\nabla_+^{\dot\alpha}X_i)\big]
+
\Tr\!\big[\Psi^i_+\,\nabla_{+\dot\alpha}\nabla_+^{\dot\alpha}X_i\big].
$$

所以二导数打在 \(X_i\) 上的项可化到 \(\mathcal K_{\Psi X}^{\rm raw}\) 加 total derivative。

$$
\boxed{
\mathcal B_{FF}^{1\text{-loop,raw}}
=
\left\{
\mathcal K_{F\bar\Lambda}^{\rm raw},
\ \mathcal K_{\Psi X}^{\rm raw}
\right\}.
}
$$

## 5. Relevant current branches and admissible cubic triangle classes

对 \(FF\) 输入，quadratic current pieces 不给 genuine \(2\to2\) local correction。

只保留 cubic current branches：
$$
\boxed{
J_{F{\rm -branch}}^{(3)\mu,{\rm raw}}
=
\frac{i}{2g_{\rm YM}^2}
\Tr\!\left(
[A_\rho,A_\sigma]\,
(\sigma^{\rho\sigma}\sigma^\mu\bar\Lambda)_-
\right),
}
$$

$$
\boxed{
J_{\psi{\rm -branch}}^{(3)\mu,{\rm raw}}
=
-\frac{i\sqrt2}{g_{\rm YM}^2}
\Tr\!\left(
[A_\nu,X_i]\,
(\sigma^\nu\bar\sigma^\mu\Psi^i)_-
\right).
}
$$

relevant cubic vertices:
$$
\boxed{
\mathcal L_{AAA}^{(3)}
=
\frac{i}{g_{\rm YM}^2}\Tr\!\left[
(\partial_\mu A_\nu-\partial_\nu A_\mu)[A^\mu,A^\nu]
\right],
}
$$

$$
\boxed{
\mathcal L_{A\Lambda\bar\Lambda}^{(3)}
=
-\frac{1}{g_{\rm YM}^2}
\Tr\!\left[
\Lambda^\alpha\sigma^\mu_{\alpha\dot\alpha}[A_\mu,\bar\Lambda^{\dot\alpha}]
\right],
}
$$

$$
\boxed{
\mathcal L_{AX\bar X}^{(3)}
=
\frac{i}{g_{\rm YM}^2}
\Tr\!\left[
(\partial_\mu X_i)[A^\mu,\bar X^i]
-(\partial_\mu\bar X^i)[A^\mu,X_i]
\right],
}
$$

$$
\boxed{
\mathcal L_{A\Psi\bar\Psi}^{(3)}
=
-\frac{1}{g_{\rm YM}^2}
\Tr\!\left[
\Psi^{i\alpha}\sigma^\mu_{\alpha\dot\alpha}[A_\mu,\bar\Psi_i^{\dot\alpha}]
\right].
}
$$

Hence the five triangle classes are
$$
\boxed{
J_{F{\rm -branch}}^{(3)}\times V_{AAA},
\qquad
J_{F{\rm -branch}}^{(3)}\times V_{A\Lambda\bar\Lambda}.
}
$$

$$
\boxed{
J_{\psi{\rm -branch}}^{(3)}\times V_{AAA},
\qquad
J_{\psi{\rm -branch}}^{(3)}\times V_{AX\bar X},
\qquad
J_{\psi{\rm -branch}}^{(3)}\times V_{A\Psi\bar\Psi}.
}
$$

Each class also has the mirror Wick contraction that exchanges the two external \(F_{\rm raw}\) legs.

## 6. Deferred status of the old \(2\to1\) pages

旧的
$$
X_iX_j\to\Psi^k,
\qquad
X_i\Psi^j\to F,
\qquad
\Psi^jX_i\to F
$$
三页不再作为整个 `n4_ordinary_space` track 的 universal seed reduction。

它们只在 future channel-by-channel basis classification 完成之后，才能重新判定是否作为特定输入的 reduced subproblem 使用。

## 7. Working rule from here

$$
\boxed{
\text{first close the }FF\text{ page, then generalize input by input.}
}
$$
