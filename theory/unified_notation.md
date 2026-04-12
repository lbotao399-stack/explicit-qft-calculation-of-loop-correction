---
title: "Unified notation"
doc_type: theory
scope: cross-theory
status: canonical
---

# Unified notation

## Spinor indices

$$
\alpha,\beta=\pm,\qquad \dot\alpha,\dot\beta=\dot\pm.
$$

$$
\epsilon_{+-}=\epsilon_{\dot+\dot-}=1,\qquad
\epsilon_{-+}=\epsilon_{\dot-\dot+}=-1.
$$

$$
\epsilon^{-+}=\epsilon^{\dot-\dot+}=1,\qquad
\epsilon^{+-}=\epsilon^{\dot+\dot-}=-1.
$$

$$
\psi^\alpha=\epsilon^{\alpha\beta}\psi_\beta,\qquad
\psi_\alpha=\epsilon_{\alpha\beta}\psi^\beta,\qquad
\widetilde\psi^{\dot\alpha}=\epsilon^{\dot\alpha\dot\beta}\widetilde\psi_{\dot\beta},\qquad
\widetilde\psi_{\dot\alpha}=\epsilon_{\dot\alpha\dot\beta}\widetilde\psi^{\dot\beta}.
$$

$$
\psi\chi:=\psi^\alpha\chi_\alpha,\qquad
\widetilde\psi\widetilde\chi:=\widetilde\psi_{\dot\alpha}\widetilde\chi^{\dot\alpha}.
$$

## Vector / bispinor

$$
v_{\alpha\dot\alpha}=\sigma^\mu_{\alpha\dot\alpha}v_\mu,\qquad
v_\mu=\frac12\bar\sigma_\mu^{\dot\alpha\alpha}v_{\alpha\dot\alpha},\qquad
u\cdot v=\frac12u^{\alpha\dot\alpha}v_{\alpha\dot\alpha}.
$$

$$
v_{+\dot\alpha}:=v_{\alpha\dot\alpha}\big|_{\alpha=+},\qquad
v_{-\dot\alpha}:=v_{\alpha\dot\alpha}\big|_{\alpha=-}.
$$

## Momentum-space measure

$$
\int_p:=\int\frac{d^dp}{(2\pi)^d},\qquad
\int_{p_1,\ldots,p_n}:=\int_{p_1}\cdots\int_{p_n}.
$$

$$
\delta_p:=(2\pi)^d\delta^{(d)}(p),\qquad
\delta_{p-p_1-\cdots-p_n}:=(2\pi)^d\delta^{(d)}(p-p_1-\cdots-p_n).
$$

$$
d=4-2\epsilon,\qquad
\int_q^d:=\mu^{2\epsilon}\int\frac{d^dq}{(2\pi)^d}.
$$

$$
\int_\Delta:=\int_0^1dx\,dy\,dz\,\delta(1-x-y-z).
$$

$$
\mu^{2\epsilon}\int\frac{d^d\ell}{(2\pi)^d}
\frac{\widehat\ell^2}{(\ell^2+\Delta)^3}\Big|_{\rm loc}
=
-\frac{1}{32\pi^2}.
$$

$$
\int\frac{d^d\ell}{(2\pi)^d}
\frac{\widehat\ell^2\,\ell_{+\dot\beta}}{(\ell^2+\Delta)^3}
=0.
$$

## Fourier conventions

$$
\Phi(x)=\int_p e^{ip\cdot x}\Phi(p),\qquad
\Phi(p)=\int d^dx\,e^{-ip\cdot x}\Phi(x).
$$

$$
\partial_{\alpha\dot\alpha}\Phi(x)\ \longleftrightarrow\ i\,p_{\alpha\dot\alpha}\Phi(p).
$$
