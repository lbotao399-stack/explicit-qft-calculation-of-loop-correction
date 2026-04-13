---
title: "N=1 SYM (Euclidean): component diagram master targets"
doc_type: theory
theory: "N=1 SYM (Euclidean)"
track: component_current_diagram
status: working
source: user_supplied_freeze_2026_04_12
---

# N=1 SYM (Euclidean): component diagram master targets

## 1. Freeze of component algebra

$$
\boxed{
Q_1\equiv Q_-,\qquad
\kappa_A=\frac{i}{2},\qquad
\partial_\mu J_-^\mu \text{ is WT-only},\qquad
\gamma_\mu S^\mu \text{ anomaly stays separate}.
}
$$

$$
f:=f_{++},
\qquad
\nabla_+\!\cdot\!\bar\lambda:=\nabla_{+\dot\beta}\bar\lambda^{\dot\beta},
\qquad
B:=w^{\dot\alpha}\nabla_{+\dot\alpha}.
$$

$$
Q_- A_{+\dot\alpha}=\frac{i}{2}\bar\lambda_{\dot\alpha},
\qquad
Q_- A_{-\dot\alpha}=0,
\qquad
Q_- \bar\lambda_{\dot\alpha}=0.
$$

$$
Q_- f = i\,\nabla_+\!\cdot\!\bar\lambda.
$$

$$
[Q_-,\nabla_{+\dot\alpha}]
=
\frac{i}{2}\operatorname{ad}_{\bar\lambda_{\dot\alpha}},
\qquad
[Q_-,\nabla_{-\dot\alpha}]=0.
$$

$$
Q_-(\nabla_{+\dot\alpha}X)
=
\nabla_{+\dot\alpha}(Q_-X)
+\frac{i}{2}\operatorname{ad}_{\bar\lambda_{\dot\alpha}}X,
$$

$$
Q_-(\nabla_{-\dot\alpha}X)
=
\nabla_{-\dot\alpha}(Q_-X).
$$

$$
\operatorname{ad}_Y(X)^a:=f^{abc}Y^bX^c.
$$

$$
Q_-(e^B X)
=
e^B(Q_-X)
+\frac{i}{2}\int_0^1 ds\;
e^{sB}\big(w^{\dot\alpha}\operatorname{ad}_{\bar\lambda_{\dot\alpha}}\big)e^{(1-s)B}X.
$$

$$
Q_-(e^B X)
=
Q_-X
+w^{\dot\alpha}\Big(\nabla_{+\dot\alpha}Q_-X+\frac{i}{2}\operatorname{ad}_{\bar\lambda_{\dot\alpha}}X\Big)
+\mathcal O(w^2).
$$

$$
Q_-^2=0,
\qquad
Q_-^2\nabla_{+\dot\alpha}=0,
\qquad
Q_-^2(e^B X)=0.
$$

## 2. Diagram-page master target formula

$$
\mathcal O=\operatorname{Tr}(X_1X_2\cdots X_n).
$$

$$
Q_-\mathcal O
=
\sum_{k=1}^n
(-1)^{\sum_{j<k}|X_j|}
\operatorname{Tr}(X_1\cdots (Q_-X_k)\cdots X_n).
$$

$$
\sum_{\rm diagrams}\Big[\partial_\mu J_-^\mu(x)\cdot \mathcal O(y)\Big]_{\rm local}
=
-\delta^{(4)}(x-y)\,Q_-^{\rm cl}\mathcal O(y),
$$

$$
t^0(\cdots)-\Gamma_{\rm cl}=0.
$$

$$
\text{nonlocal pieces: discard},
\qquad
\text{improvement pieces: discard},
\qquad
\gamma_\mu S^\mu\text{ channel: separate}.
$$

## 3. Common classical targets

### 3.1 \(\operatorname{Tr}(f\,\bar\lambda_{\dot\alpha})\)

$$
Q_-\operatorname{Tr}(f\,\bar\lambda_{\dot\alpha})
=
i\,\operatorname{Tr}\!\big((\nabla_+\!\cdot\!\bar\lambda)\,\bar\lambda_{\dot\alpha}\big).
$$

### 3.2 \(\operatorname{Tr}(f\,f)\)

$$
Q_-\operatorname{Tr}(f\,f)
=
2i\,\operatorname{Tr}\!\big(f\,\nabla_+\!\cdot\!\bar\lambda\big).
$$

### 3.3 \(\operatorname{Tr}\!\big(f\,\nabla_{+\dot\alpha}\bar\lambda_{\dot\beta}\big)\)

$$
Q_-\operatorname{Tr}\!\big(f\,\nabla_{+\dot\alpha}\bar\lambda_{\dot\beta}\big)
=
i\,\operatorname{Tr}\!\big((\nabla_+\!\cdot\!\bar\lambda)\,\nabla_{+\dot\alpha}\bar\lambda_{\dot\beta}\big)
+\frac{i}{2}\operatorname{Tr}\!\big(f\,\operatorname{ad}_{\bar\lambda_{\dot\alpha}}\bar\lambda_{\dot\beta}\big).
$$

### 3.4 \(\operatorname{Tr}\!\big((\nabla_{+\dot\alpha}f)\,f\big)\)

$$
Q_-(\nabla_{+\dot\alpha}f)
=
i\,\nabla_{+\dot\alpha}\nabla_+\!\cdot\!\bar\lambda
+\frac{i}{2}\operatorname{ad}_{\bar\lambda_{\dot\alpha}}f.
$$

$$
Q_-\operatorname{Tr}\!\big((\nabla_{+\dot\alpha}f)\,f\big)
=
i\,\operatorname{Tr}\!\big((\nabla_{+\dot\alpha}\nabla_+\!\cdot\!\bar\lambda)\,f\big)
+\frac{i}{2}\operatorname{Tr}\!\big((\operatorname{ad}_{\bar\lambda_{\dot\alpha}}f)\,f\big)
+i\,\operatorname{Tr}\!\big((\nabla_{+\dot\alpha}f)\,\nabla_+\!\cdot\!\bar\lambda\big).
$$

$$
\operatorname{Tr}\!\big((\operatorname{ad}_{\bar\lambda_{\dot\alpha}}f)\,f\big)=0.
$$

$$
Q_-\operatorname{Tr}\!\big((\nabla_{+\dot\alpha}f)\,f\big)
=
i\,\operatorname{Tr}\!\big((\nabla_{+\dot\alpha}\nabla_+\!\cdot\!\bar\lambda)\,f\big)
+i\,\operatorname{Tr}\!\big((\nabla_{+\dot\alpha}f)\,\nabla_+\!\cdot\!\bar\lambda\big).
$$

### 3.5 \(\operatorname{Tr}\!\big((\nabla_{+\dot\alpha}f)\,\bar\lambda_{\dot\beta}\big)\)

$$
Q_-\operatorname{Tr}\!\big((\nabla_{+\dot\alpha}f)\,\bar\lambda_{\dot\beta}\big)
=
i\,\operatorname{Tr}\!\big((\nabla_{+\dot\alpha}\nabla_+\!\cdot\!\bar\lambda)\,\bar\lambda_{\dot\beta}\big)
+\frac{i}{2}\operatorname{Tr}\!\big((\operatorname{ad}_{\bar\lambda_{\dot\alpha}}f)\,\bar\lambda_{\dot\beta}\big).
$$

### 3.6 \(\operatorname{Tr}\!\big((\nabla_{+\dot\alpha}f)\,(\nabla_{+\dot\beta}\bar\lambda_{\dot\gamma})\big)\)

$$
Q_-\operatorname{Tr}\!\big((\nabla_{+\dot\alpha}f)\,(\nabla_{+\dot\beta}\bar\lambda_{\dot\gamma})\big)
=
i\,\operatorname{Tr}\!\big((\nabla_{+\dot\alpha}\nabla_+\!\cdot\!\bar\lambda)\,\nabla_{+\dot\beta}\bar\lambda_{\dot\gamma}\big)
$$

$$
\qquad
+\frac{i}{2}\operatorname{Tr}\!\big((\operatorname{ad}_{\bar\lambda_{\dot\alpha}}f)\,\nabla_{+\dot\beta}\bar\lambda_{\dot\gamma}\big)
+\frac{i}{2}\operatorname{Tr}\!\big((\nabla_{+\dot\alpha}f)\,\operatorname{ad}_{\bar\lambda_{\dot\beta}}\bar\lambda_{\dot\gamma}\big).
$$

## 4. Decorated \(e^{w\cdot\nabla_+}\) targets

### 4.1 \(\operatorname{Tr}\!\big(f,e^B f\big)\)

$$
Q_-\operatorname{Tr}\!\big(f,e^B f\big)
=
i\,\operatorname{Tr}\!\big((\nabla_+\!\cdot\!\bar\lambda),e^B f\big)
+i\,\operatorname{Tr}\!\big(f,e^B(\nabla_+\!\cdot\!\bar\lambda)\big)
$$

$$
\qquad
+\frac{i}{2}\int_0^1 ds\;
\operatorname{Tr}\!\big(
f,e^{sB}(w^{\dot\alpha}\operatorname{ad}_{\bar\lambda_{\dot\alpha}})e^{(1-s)B}f
\big).
$$

### 4.2 \(\operatorname{Tr}\!\big((e^B f),f\big)\)

$$
Q_-\operatorname{Tr}\!\big((e^B f),f\big)
=
i\,\operatorname{Tr}\!\big(e^B(\nabla_+\!\cdot\!\bar\lambda),f\big)
+i\,\operatorname{Tr}\!\big((e^B f),\nabla_+\!\cdot\!\bar\lambda\big)
$$

$$
\qquad
+\frac{i}{2}\int_0^1 ds\;
\operatorname{Tr}\!\big(
e^{sB}(w^{\dot\alpha}\operatorname{ad}_{\bar\lambda_{\dot\alpha}})e^{(1-s)B}f,\ f
\big).
$$

### 4.3 \(\operatorname{Tr}\!\big(f,e^B\bar\lambda_{\dot\beta}\big)\)

$$
Q_-\operatorname{Tr}\!\big(f,e^B\bar\lambda_{\dot\beta}\big)
=
i\,\operatorname{Tr}\!\big((\nabla_+\!\cdot\!\bar\lambda),e^B\bar\lambda_{\dot\beta}\big)
+\frac{i}{2}\int_0^1 ds\;
\operatorname{Tr}\!\big(
f,e^{sB}(w^{\dot\alpha}\operatorname{ad}_{\bar\lambda_{\dot\alpha}})e^{(1-s)B}\bar\lambda_{\dot\beta}
\big).
$$

### 4.4 Small-\(w\) expansion for \(\operatorname{Tr}(f,e^B f)\)

$$
Q_-\operatorname{Tr}\!\big(f,e^B f\big)
=
2i\,\operatorname{Tr}\!\big(f,\nabla_+\!\cdot\!\bar\lambda\big)
+w^{\dot\alpha}\Big[
i\,\operatorname{Tr}\!\big((\nabla_+\!\cdot\!\bar\lambda),\nabla_{+\dot\alpha}f\big)
+i\,\operatorname{Tr}\!\big(f,\nabla_{+\dot\alpha}\nabla_+\!\cdot\!\bar\lambda\big)
+\frac{i}{2}\operatorname{Tr}\!\big(f,\operatorname{ad}_{\bar\lambda_{\dot\alpha}}f\big)
\Big]
+\mathcal O(w^2).
$$

$$
\operatorname{Tr}\!\big(f,\operatorname{ad}_{\bar\lambda_{\dot\alpha}}f\big)=0.
$$

$$
Q_-\operatorname{Tr}\!\big(f,e^B f\big)
=
2i\,\operatorname{Tr}\!\big(f,\nabla_+\!\cdot\!\bar\lambda\big)
+w^{\dot\alpha}\Big[
i\,\operatorname{Tr}\!\big((\nabla_+\!\cdot\!\bar\lambda),\nabla_{+\dot\alpha}f\big)
+i\,\operatorname{Tr}\!\big(f,\nabla_{+\dot\alpha}\nabla_+\!\cdot\!\bar\lambda\big)
\Big]
+\mathcal O(w^2).
$$

## 5. Diagram-page local selection rule

$$
\langle f_{\alpha\beta}(x)f_{\gamma\delta}(y)\rangle
\propto
\epsilon_{\alpha\gamma}\epsilon_{\beta\delta}
+\epsilon_{\alpha\delta}\epsilon_{\beta\gamma}.
$$

$$
\langle f_{++}(x)f_{++}(y)\rangle=0,
\qquad
\langle f_{+-}(x)f_{++}(y)\rangle=0,
\qquad
\langle f_{--}(x)f_{++}(y)\rangle\neq 0.
$$

$$
\boxed{
\text{if the current }f\text{-leg contracts locally to external }f_{++},\text{ keep only the }f_{--}\text{-branch}.
}
$$

$$
\text{for external }\nabla_{+\dot\alpha}X:
\quad
\nabla_{+\dot\alpha}(Q_-X)
\quad\text{and}\quad
\frac{i}{2}\operatorname{ad}_{\bar\lambda_{\dot\alpha}}X
\text{ must both be kept.}
$$

$$
\text{for external }e^B X:
\quad
e^B(Q_-X)
\quad\text{and}\quad
\frac{i}{2}\int_0^1 ds\;e^{sB}(w\cdot\operatorname{ad}_{\bar\lambda})e^{(1-s)B}X
\text{ must both be kept.}
$$

## 6. Superspace track boundary condition

$$
\boxed{
\text{component track source of truth}
=
\{Q_1\equiv Q_-,\ \kappa_A=i/2,\ \partial_\mu J_-^\mu\text{ WT-only}\}.
}
$$

$$
\boxed{
\text{superspace track is only for }
\text{(a) operator dictionary}
\quad\text{and}\quad
\text{(b) anomaly multiplet bookkeeping}.
}
$$

$$
\boxed{
\text{do not feed superspace anomaly equations back into component divergence pages.}
}
$$

## 7. Execution order

$$
\boxed{
\text{Step A: fix all component diagram-page headers to the same freeze conventions.}
}
$$

$$
\boxed{
\text{Step B: write }Q_-^{\rm cl}\mathcal O\text{ explicitly for each page.}
}
$$

$$
\boxed{
\text{Step C: keep only local diagram pieces that reconstruct that target.}
}
$$

$$
\boxed{
\text{Step D: close each page with }
\sum_{\rm local}=-\delta^{(4)}(x-y)Q_-^{\rm cl}\mathcal O,\quad
t^0(\cdots)-\Gamma_{\rm cl}=0.
}
$$

$$
\boxed{
\text{Step E: after the component pages are sealed, continue only on the separate superspace track.}
}
$$
