# Lecture 02: Differentiation Rules and Applications of Derivatives

## Context and Grounding
This lecture develops the calculus of differentiation. It details standard operational differentiation rules, derivatives of transcendental functions, implicit differentiation, the Mean Value Theorems, L'Hopital's rule, and geometric curve sketching through extrema and inflection analysis.

---

## 1. Operational Rules of Differentiation

Let $u(x)$ and $v(x)$ be differentiable functions and $c \in \mathbb{R}$ a constant:

| Rule | Formula |
|:---|:---|
| Linearity | $(c \cdot u)' = c \cdot u', \quad (u \pm v)' = u' \pm v'$ |
| Power Rule | $\frac{d}{dx}[x^n] = n x^{n-1} \quad (n \in \mathbb{R})$ |
| Product Rule | $(u \cdot v)' = u' v + u v'$ |
| Quotient Rule | $\left( \frac{u}{v} \right)' = \frac{u' v - u v'}{v^2} \quad (v(x) \neq 0)$ |
| Chain Rule | $\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)$ |

---

## 2. Derivatives of Elementary Functions

* **Trigonometric Functions**:
  $$\frac{d}{dx}[\sin x] = \cos x, \quad \frac{d}{dx}[\cos x] = -\sin x, \quad \frac{d}{dx}[\tan x] = \sec^2 x$$
* **Exponential and Logarithmic Functions**:
  $$\frac{d}{dx}[e^x] = e^x, \quad \frac{d}{dx}[a^x] = a^x \ln a, \quad \frac{d}{dx}[\ln |x|] = \frac{1}{x}$$
* **Inverse Trigonometric Functions**:
  $$\frac{d}{dx}[\arcsin x] = \frac{1}{\sqrt{1 - x^2}}, \quad \frac{d}{dx}[\arctan x] = \frac{1}{1 + x^2}$$

---

## 3. Fundamental Theorems of Differential Calculus

### 3.1 Rolle's Theorem
Let $f$ be continuous on $[a, b]$, differentiable on $(a, b)$, and $f(a) = f(b)$. Then there exists at least one point $c \in (a, b)$ such that:
$$f'(c) = 0$$

### 3.2 Lagrange's Mean Value Theorem (MVT)
Let $f$ be continuous on $[a, b]$ and differentiable on $(a, b)$. Then there exists at least one point $c \in (a, b)$ such that:
$$f'(c) = \frac{f(b) - f(a)}{b - a}$$
Geometrically, the tangent line to the curve at $c$ is parallel to the secant line passing through $(a, f(a))$ and $(b, f(b))$.

### 3.3 L'Hopital's Rule for Indeterminate Forms
Let $\lim_{x \to x_0} f(x) = \lim_{x \to x_0} g(x) = 0$ (or $\pm\infty$). If $f$ and $g$ are differentiable in a punctured neighborhood of $x_0$ with $g'(x) \neq 0$, then:
$$\lim_{x \to x_0} \frac{f(x)}{g(x)} = \lim_{x \to x_0} \frac{f'(x)}{g'(x)}$$
provided the latter limit exists or equals $\pm\infty$.

---

## 4. Geometric Applications & Curve Sketching

### 4.1 Monotonicity and Local Extrema
* **First Derivative Test**:
  - $f'(x) > 0$ on $(a, b) \implies f$ is strictly increasing on $[a, b]$.
  - $f'(x) < 0$ on $(a, b) \implies f$ is strictly decreasing on $[a, b]$.
  - Critical points: Points $x_0 \in D(f)$ where $f'(x_0) = 0$ or $f'(x_0)$ does not exist.
  - If $f'$ transitions from positive to negative across $x_0 \implies$ local maximum.
  - If $f'$ transitions from negative to positive across $x_0 \implies$ local minimum.

### 4.2 Concavity and Inflection Points
* **Second Derivative Test**:
  - $f''(x) > 0$ on $(a, b) \implies f$ is concave upward ($\cup$).
  - $f''(x) < 0$ on $(a, b) \implies f$ is concave downward ($\cap$).
  - An **inflection point** occurs at $(x_0, f(x_0))$ where $f''(x_0) = 0$ (or undefined) and the concavity strictly changes sign across $x_0$.

### 4.3 Asymptotes
1. **Vertical Asymptote ($x = x_0$)**: Occurs if $\lim_{x \to x_0^\pm} f(x) = \pm\infty$.
2. **Horizontal Asymptote ($y = L$)**: Occurs if $\lim_{x \to \pm\infty} f(x) = L$.
3. **Oblique (Slant) Asymptote ($y = \lambda x + \beta$)**:
   $$\lambda = \lim_{x \to \pm\infty} \frac{f(x)}{x}, \quad \beta = \lim_{x \to \pm\infty} [f(x) - \lambda x]$$

