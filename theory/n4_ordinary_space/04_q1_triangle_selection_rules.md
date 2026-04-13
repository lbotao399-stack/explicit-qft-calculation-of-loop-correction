---
title: "N=4 ordinary-space: Q_1 local-basis selection rules"
doc_type: theory
theory: "N=4 SYM ordinary-space"
status: working
---

# N=4 ordinary-space: Q_1 local-basis selection rules

## 1. Global correction

$$
\boxed{
\text{do not classify this track by a universal no-derivative }2\to1\text{ map.}
}
$$

For each ordered input
$$
\mathcal O_{L_1L_2}=\Tr(L_1L_2),
$$
the first task is to determine
$$
\mathcal B_{L_1L_2}^{1\text{-loop}}
$$
modulo total derivatives and EOM.

## 2. First true seed

$$
\boxed{
\text{first seed: }Q_1\big(\Tr(F_{\rm raw}F_{\rm raw})\big).
}
$$

Its raw basis is
$$
\mathcal K_{F\bar\Lambda}^{\rm raw}
=
\Tr\!\big[
(\nabla_{+\dot\alpha}F_{\rm raw})\,\bar\Lambda^{\dot\alpha}
\big],
$$

$$
\mathcal K_{\Psi X}^{\rm raw}
=
\Tr\!\big[
(\nabla_{+\dot\alpha}\Psi^i_+)\,(\nabla_+^{\dot\alpha}X_i)
\big].
$$

$$
\boxed{
\mathcal B_{FF}^{1\text{-loop,raw}}
=
\left\{
\mathcal K_{F\bar\Lambda}^{\rm raw},
\mathcal K_{\Psi X}^{\rm raw}
\right\}.
}
$$

## 3. Relevant current branches for \(FF\)

Only
$$
J_{F{\rm -branch}}^{(3)\mu,\rm raw},
\qquad
J_{\psi{\rm -branch}}^{(3)\mu,\rm raw}
$$
are kept on the \(FF\) page.

Quadratic branches
$$
J_F^{(2)},
\qquad
J_\psi^{(2)}
$$
are not part of the genuine \(FF\) one-loop local correction.

## 4. Admissible cubic triangle classes for \(FF\)

For the \(\mathcal K_{F\bar\Lambda}^{\rm raw}\) channel:
$$
\boxed{
J_{F{\rm -branch}}^{(3)}\times V_{AAA},
\qquad
J_{F{\rm -branch}}^{(3)}\times V_{A\Lambda\bar\Lambda}.
}
$$

For the \(\mathcal K_{\Psi X}^{\rm raw}\) channel:
$$
\boxed{
J_{\psi{\rm -branch}}^{(3)}\times V_{AAA},
\qquad
J_{\psi{\rm -branch}}^{(3)}\times V_{AX\bar X},
\qquad
J_{\psi{\rm -branch}}^{(3)}\times V_{A\Psi\bar\Psi}.
}
$$

Each class has the mirror Wick contraction exchanging the two external \(F_{\rm raw}\) legs.

## 5. Sorting rule on the \(FF\) page

All local pieces proportional to
$$
(\nabla_{+\dot\alpha}F_{\rm raw})\bar\Lambda^{\dot\alpha}
$$
are collected into \(c_{F\bar\Lambda}^{\rm raw}\).

All local pieces proportional to
$$
(\nabla_{+\dot\alpha}\Psi^i_+)(\nabla_+^{\dot\alpha}X_i)
$$
are collected into \(c_{\Psi X}^{\rm raw}\).

No third independent local operator should remain after reduction modulo total derivatives and EOM.

## 6. Deferred legacy pages

The pages
$$
X_iX_j\to\Psi^k,
\qquad
X_i\Psi^j\to F,
\qquad
\Psi^jX_i\to F
$$
are now deferred.

They are no longer the project-wide seed set.

## 7. Next check

Only after the \(FF\) page is explicitly computed should nilpotency and lift pages be reopened in an input-by-input form.
