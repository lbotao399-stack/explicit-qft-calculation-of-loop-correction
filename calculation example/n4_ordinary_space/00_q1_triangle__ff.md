---
title: "Q_1 triangle seed: F_raw F_raw"
doc_type: calculation
theory: "N=4 SYM ordinary-space"
loop_order: 1
supercharge: "Q_-^4"
status: seed_setup
---

# Q_1 triangle seed: \(F_{\rm raw}F_{\rm raw}\)

## Step 1: Input / classical target / one-loop basis

$$
\mathcal O_{FF}(y):=\Tr\!\big(F_{\rm raw}F_{\rm raw}\big)(y),
\qquad
F_{\rm raw}=f^{\rm raw}_{++}.
$$

$$
Q_1F_{\rm raw}
=
i\,\nabla_{+\dot\alpha}\bar\Lambda^{\dot\alpha}.
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

$$
\mathcal K_{F\bar\Lambda}^{\rm raw}
:=
\Tr\!\big[
(\nabla_{+\dot\alpha}F_{\rm raw})\,\bar\Lambda^{\dot\alpha}
\big],
$$

$$
\mathcal K_{\Psi X}^{\rm raw}
:=
\Tr\!\big[
(\nabla_{+\dot\alpha}\Psi^i_+)\,(\nabla_+^{\dot\alpha}X_i)
\big].
$$

$$
\boxed{
Q_1^{1\text{-loop}}\mathcal O_{FF}
=
\frac{g_{\rm YM}^2}{8\pi^2}
\Big(
c_{F\bar\Lambda}^{\rm raw}\,\mathcal K_{F\bar\Lambda}^{\rm raw}
+
c_{\Psi X}^{\rm raw}\,\mathcal K_{\Psi X}^{\rm raw}
\Big).
}
$$

## Step 2: AWI ansatz

$$
\boxed{
\big[\partial_\mu J^\mu_{Q_1}(x)\,\mathcal O_{FF}(y)\big]^{1\text{-loop}}_{\rm loc}
=
-\delta^{(4)}(x-y)\,
\Big[
Q_1^{\rm cl}\mathcal O_{FF}
+
Q_1^{1\text{-loop}}\mathcal O_{FF}
\Big](y).
}
$$

## Step 3: Relevant current branches and vertices

Only cubic current branches:
$$
J_{F{\rm -branch}}^{(3)\mu,{\rm raw}}
=
\frac{i}{2g_{\rm YM}^2}
\Tr\!\left(
[A_\rho,A_\sigma]\,
(\sigma^{\rho\sigma}\sigma^\mu\bar\Lambda)_-
\right),
$$

$$
J_{\psi{\rm -branch}}^{(3)\mu,{\rm raw}}
=
-\frac{i\sqrt2}{g_{\rm YM}^2}
\Tr\!\left(
[A_\nu,X_i]\,
(\sigma^\nu\bar\sigma^\mu\Psi^i)_-
\right).
$$

Relevant cubic triangle classes:
$$
J_{F{\rm -branch}}^{(3)}\times V_{AAA},
\qquad
J_{F{\rm -branch}}^{(3)}\times V_{A\Lambda\bar\Lambda},
$$

$$
J_{\psi{\rm -branch}}^{(3)}\times V_{AAA},
\qquad
J_{\psi{\rm -branch}}^{(3)}\times V_{AX\bar X},
\qquad
J_{\psi{\rm -branch}}^{(3)}\times V_{A\Psi\bar\Psi}.
$$

with
$$
\mathcal L_{AAA}^{(3)}
=
\frac{i}{g_{\rm YM}^2}\Tr\!\left[
(\partial_\mu A_\nu-\partial_\nu A_\mu)[A^\mu,A^\nu]
\right],
$$

$$
\mathcal L_{A\Lambda\bar\Lambda}^{(3)}
=
-\frac{1}{g_{\rm YM}^2}
\Tr\!\left[
\Lambda^\alpha\sigma^\mu_{\alpha\dot\alpha}[A_\mu,\bar\Lambda^{\dot\alpha}]
\right],
$$

$$
\mathcal L_{AX\bar X}^{(3)}
=
\frac{i}{g_{\rm YM}^2}
\Tr\!\left[
(\partial_\mu X_i)[A^\mu,\bar X^i]
-(\partial_\mu\bar X^i)[A^\mu,X_i]
\right],
$$

$$
\mathcal L_{A\Psi\bar\Psi}^{(3)}
=
-\frac{1}{g_{\rm YM}^2}
\Tr\!\left[
\Psi^{i\alpha}\sigma^\mu_{\alpha\dot\alpha}[A_\mu,\bar\Psi_i^{\dot\alpha}]
\right].
$$

Each class also has the mirror Wick contraction exchanging the two external \(F_{\rm raw}\) legs.

## Step 4: Basis reduction rule

All local pieces proportional to
$$
(\nabla_{+\dot\alpha}F_{\rm raw})\bar\Lambda^{\dot\alpha}
$$
go into \(c_{F\bar\Lambda}^{\rm raw}\).

All local pieces proportional to
$$
(\nabla_{+\dot\alpha}\Psi^i_+)(\nabla_+^{\dot\alpha}X_i)
$$
go into \(c_{\Psi X}^{\rm raw}\).

Modulo total derivatives and EOM, no third independent local structure should remain.

## Step 5: To compute

$$
\boxed{
\text{remaining task: evaluate the five cubic triangle classes, add the two mirror contractions,}
}
$$

$$
\boxed{
\text{and reduce the full local remainder onto }
\mathcal K_{F\bar\Lambda}^{\rm raw}
\text{ and }
\mathcal K_{\Psi X}^{\rm raw}.
}
$$

$$
\boxed{
\text{The first actual coefficients to extract in this track are }
c_{F\bar\Lambda}^{\rm raw}
\text{ and }
c_{\Psi X}^{\rm raw}.
}
$$
