# Assignment 01: Signal Transformations and System Property Proofs

## Objective
Assess analytical proficiency in signal manipulations, even/odd signal decomposition, energy/power calculations, and mathematical proofs of the six fundamental system properties.

---

## Problem Set

### Problem 1: Signal Energy, Power, and Decomposition
Consider the continuous-time signal:
$$
x(t) = e^{-3t} u(t) - e^{-3(t - 2)} u(t - 2)
$$
1. Calculate the total energy $E_\infty$ of $x(t)$.
2. State whether $x(t)$ is an energy signal, power signal, or neither.
3. Compute and sketch closed-form expressions for the even part $x_e(t)$ and odd part $x_o(t)$.

### Problem 2: Independent Variable Transformations
Given the triangular pulse signal:
$$
w(t) = \begin{cases} 1 - |t|, & |t| \le 1 \\ 0, & \text{otherwise} \end{cases}
$$
Provide analytical equations and sketch:
1. $y_1(t) = w(2t + 3)$
2. $y_2(t) = w(4 - 2t)$

### Problem 3: System Property Proofs
For each of the following continuous-time systems, provide formal mathematical proofs determining whether the system is: (a) Memoryless, (b) Causal, (c) Linear, (d) Time-Invariant, and (e) BIBO Stable.
1. **System 1:** $y(t) = \int_{-\infty}^{2t} x(\tau) \, d\tau$
2. **System 2:** $y(t) = x(t) \cdot \cos(100\pi t)$
3. **System 3:** $y(t) = \frac{d}{dt} \left[ e^{-t} x(t) \right]$

---

## Deliverables
A clear, handwritten or LaTeX-typeset PDF report presenting comprehensive mathematical derivations and annotated sketches for all three problems.

