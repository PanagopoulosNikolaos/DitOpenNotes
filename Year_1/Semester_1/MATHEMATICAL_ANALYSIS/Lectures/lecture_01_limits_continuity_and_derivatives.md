# Lecture 01: Real Functions, Limits, Continuity, and the Derivative

## Context and Grounding
This lecture establishes the foundational concepts of single-variable real analysis. It formalizes real-valued functions, domain and range constraints, the rigorous $(\varepsilon, \delta)$-definition of limits, one-sided limits, continuity theorems, and the limit definition of the derivative.

---

## 1. Real Functions of a Real Variable

### 1.1 Definitions and Mappings
A real function of a real variable is a mapping $f: D(f) \to \mathbb{R}$, where $D(f) \subseteq \mathbb{R}$ is the domain.
* **Domain ($D(f)$)**: The set of all real values $x$ for which the mathematical expression $f(x)$ produces a well-defined real number:
  - Rational functions $\frac{P(x)}{Q(x)} \implies Q(x) \neq 0$.
  - Even roots $\sqrt[2k]{g(x)} \implies g(x) \ge 0$.
  - Logarithms $\ln(g(x)) \implies g(x) > 0$.
* **Range ($R(f)$)**: The image set $\{f(x) \mid x \in D(f)\}$.

### 1.2 Invertibility
A function $f$ is **injective (one-to-one)** if $f(x_1) = f(x_2) \implies x_1 = x_2$.
An injective function possesses a unique inverse function $f^{-1}: R(f) \to D(f)$ satisfying:
$$f^{-1}(f(x)) = x \quad \text{and} \quad f(f^{-1}(y)) = y$$
The graph of $y = f^{-1}(x)$ is the reflection of the graph of $y = f(x)$ across the line $y = x$.

---

## 2. Limits of Functions

### 2.1 The Formal $(\varepsilon, \delta)$-Definition
Let $f$ be defined on an open interval containing $x_0$, except possibly at $x_0$ itself. We write:
$$\lim_{x \to x_0} f(x) = L$$
if and only if for every $\varepsilon > 0$, there exists a corresponding $\delta > 0$ such that:
$$0 < |x - x_0| < \delta \implies |f(x) - L| < \varepsilon$$

### 2.2 One-Sided Limits and Existence
* **Left-hand limit**: $\lim_{x \to x_0^-} f(x) = L_1$ (values $x < x_0$).
* **Right-hand limit**: $\lim_{x \to x_0^+} f(x) = L_2$ (values $x > x_0$).
* **Limit Existence Criterion**:
  $$\lim_{x \to x_0} f(x) = L \iff \lim_{x \to x_0^-} f(x) = \lim_{x \to x_0^+} f(x) = L$$

### 2.3 The Squeeze (Sandwich) Theorem
If $g(x) \le f(x) \le h(x)$ for all $x$ in an open neighborhood around $x_0$ (except possibly at $x_0$), and:
$$\lim_{x \to x_0} g(x) = \lim_{x \to x_0} h(x) = L$$
then:
$$\lim_{x \to x_0} f(x) = L$$

* Application: $\lim_{x \to 0} \frac{\sin(x)}{x} = 1$ and $\lim_{x \to 0} \frac{1 - \cos(x)}{x} = 0$.

---

## 3. Continuity of Functions

### 3.1 Continuity at a Point
A function $f$ is **continuous at $x_0 \in D(f)$** if and only if three conditions are satisfied:
1. $f(x_0)$ exists ($x_0 \in D(f)$).
2. $\lim_{x \to x_0} f(x)$ exists.
3. $\lim_{x \to x_0} f(x) = f(x_0)$.

### 3.2 Fundamental Theorems of Continuous Functions
1. **Intermediate Value Theorem (IVT)**: If $f$ is continuous on the closed interval $[a, b]$ and $u$ is any number between $f(a)$ and $f(b)$, there exists at least one $c \in (a, b)$ such that $f(c) = u$.
2. **Bolzano's Theorem (Root Existence)**: If $f$ is continuous on $[a, b]$ and $f(a) \cdot f(b) < 0$, then there exists at least one root $c \in (a, b)$ such that $f(c) = 0$.
3. **Extreme Value Theorem (EVT)**: If $f$ is continuous on a closed and bounded interval $[a, b]$, then $f$ attains both an absolute maximum and an absolute minimum on $[a, b]$.

---

## 4. The Derivative as an Instantaneous Rate of Change

### 4.1 Limit Definition of the Derivative
The derivative of $f$ at $x_0$ is the limit of the difference quotient as the increment $h \to 0$:
$$f'(x_0) = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h} = \lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0}$$
Geometrically, $f'(x_0)$ represents the exact slope of the tangent line to the curve $y = f(x)$ at $(x_0, f(x_0))$.

### 4.2 Differentiability Implies Continuity
If $f$ is differentiable at $x_0$, then $f$ is necessarily continuous at $x_0$:
$$\lim_{x \to x_0} [f(x) - f(x_0)] = \lim_{x \to x_0} \left[ \frac{f(x) - f(x_0)}{x - x_0} (x - x_0) \right] = f'(x_0) \cdot 0 = 0$$
* The converse does not hold: $f(x) = |x|$ is continuous at $x = 0$ but fails to be differentiable at $x = 0$.

