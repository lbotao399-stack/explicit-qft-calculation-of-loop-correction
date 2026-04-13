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

$$
x_{\alpha\dot\alpha}=(\sigma^\mu)_{\alpha\dot\alpha}x_\mu,
\qquad
\partial_{\alpha\dot\alpha}=(\sigma^\mu)_{\alpha\dot\alpha}\partial_\mu,
\qquad
\sigma^{\mu\nu}
=
\frac14\left(\sigma^\mu\bar\sigma^\nu-\sigma^\nu\bar\sigma^\mu\right).
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
k^\mu=\bar k^\mu+\widehat k^\mu,\qquad
k_{\alpha\dot\alpha}=\bar k_{\alpha\dot\alpha},\qquad
\bar k^2=k^2-\widehat k^2.
$$

$$
\bar g^\mu{}_\mu=4,
\qquad
\widehat g^\mu{}_\mu=-2\epsilon.
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
\widehat k^2\ \longrightarrow\ \frac{d-4}{d}\,k^2
=-\frac{2\epsilon}{4-2\epsilon}\,k^2.
$$

$$
\int\frac{d^d\ell}{(2\pi)^d}
\frac{\widehat\ell^2\,\ell_{+\dot\beta}}{(\ell^2+\Delta)^3}
=0.
$$

## Gauge-covariant derivatives

$$
\nabla_\mu\phi^i=\partial_\mu\phi^i-igA_\mu^a(T^a)^i{}_j\phi^j,
\qquad
\nabla_\mu\psi^i=\partial_\mu\psi^i-igA_\mu^a(T^a)^i{}_j\psi^j.
$$

$$
(D_\mu\lambda)^a=\partial_\mu\lambda^a+gf^{abc}A_\mu^b\lambda^c.
$$

## Fourier conventions

$$
\Phi(x)=\int_p e^{ip\cdot x}\Phi(p),\qquad
\Phi(p)=\int d^dx\,e^{-ip\cdot x}\Phi(x).
$$

$$
\partial_{\alpha\dot\alpha}\Phi(x)\ \longleftrightarrow\ i\,p_{\alpha\dot\alpha}\Phi(p).
$$
