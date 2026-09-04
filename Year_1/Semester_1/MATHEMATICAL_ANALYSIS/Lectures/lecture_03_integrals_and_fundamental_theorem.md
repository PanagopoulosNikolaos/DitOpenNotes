# Lecture 03: Integration Techniques and the Fundamental Theorem of Calculus

## Context and Grounding
This lecture develops the theory of single-variable integral calculus. It formalizes antiderivatives, core integration techniques (substitution, parts, partial fractions), the Riemann integral construct, the Fundamental Theorem of Calculus (FTC), and geometric applications to area and volume computation.

---

## 1. Antiderivatives and Indefinite Integrals

An **antiderivative** of a function $f$ on an interval $I$ is any function $F$ satisfying $F'(x) = f(x)$ for all $x \in I$.
The general indefinite integral introduces an arbitrary constant of integration $C \in \mathbb{R}$:
$$\int f(x) \, dx = F(x) + C$$

### 1.1 Fundamental Integrals Table
| Integrand $f(x)$ | Antiderivative $\int f(x) \, dx$ | Domain Restrictions |
|:---|:---|:---|
| $x^n$ | $\frac{x^{n+1}}{n+1} + C$ | $n \neq -1$ |
| $\frac{1}{x}$ | $\ln |x| + C$ | $x \neq 0$ |
| $e^x$ | $e^x + C$ | $\mathbb{R}$ |
| $\sin x$ | $-\cos x + C$ | $\mathbb{R}$ |
| $\cos x$ | $\sin x + C$ | $\mathbb{R}$ |
| $\frac{1}{1 + x^2}$ | $\arctan x + C$ | $\mathbb{R}$ |
| $\frac{1}{\sqrt{1 - x^2}}$ | $\arcsin x + C$ | $|x| < 1$ |

---

## 2. Integration Techniques

### 2.1 Substitution Method (Change of Variable)
If $u = g(x)$ is a differentiable function whose range is an interval $I$ and $f$ is continuous on $I$:
$$\int f(g(x)) g'(x) \, dx = \int f(u) \, du$$

### 2.2 Integration by Parts
Derived directly from the product rule of differentiation:
$$\int u \, dv = u v - \int v \, du$$
* Strategy (LIATE rule for choosing $u$): **L**ogarithmic, **I**nverse trigonometric, **A**lgebraic, **T**rigonometric, **E**xponential.

### 2.3 Partial Fraction Decomposition
To integrate rational functions $\frac{P(x)}{Q(x)}$ where $\deg(P) < \deg(Q)$:
* **Linear factors $(x - r)$**: Yield $\frac{A}{x - r} \implies A \ln|x - r|$.
* **Repeated linear factors $(x - r)^k$**: Yield $\sum_{j=1}^k \frac{A_j}{(x - r)^j}$.
* **Irreducible quadratic factors $(x^2 + px + q)$**: Yield $\frac{Bx + C}{x^2 + px + q}$, integrating into combinations of logarithms and arctangent functions.

---

## 3. The Definite Integral and Riemann Sums

Let $f$ be bounded on $[a, b]$. A partition $P = \{a = x_0 < x_1 < \cdots < x_n = b\}$ subdivides $[a, b]$ into subintervals with lengths $\Delta x_i = x_i - x_{i-1}$.
The **Riemann integral** of $f$ over $[a, b]$ is the limit:
$$\int_a^b f(x) \, dx = \lim_{\|P\| \to 0} \sum_{i=1}^n f(c_i) \Delta x_i \quad (c_i \in [x_{i-1}, x_i])$$
Every continuous function on a closed interval is guaranteed to be Riemann integrable.

---

## 4. The Fundamental Theorem of Calculus (FTC)

The FTC bridges differential calculus with integral calculus into a unified mathematical discipline.

### 4.1 FTC Part 1 (Differentiation of Integrals)
Let $f$ be continuous on $[a, b]$. The area function:
$$g(x) = \int_a^x f(t) \, dt$$
is continuous on $[a, b]$, differentiable on $(a, b)$, and its derivative is:
$$g'(x) = \frac{d}{dx} \left[ \int_a^x f(t) \, dt \right] = f(x)$$

* **Leibniz Rule for Variable Limits**:
  $$\frac{d}{dx} \left[ \int_{u(x)}^{v(x)} f(t) \, dt \right] = f(v(x)) v'(x) - f(u(x)) u'(x)$$

### 4.2 FTC Part 2 (The Evaluation Theorem)
If $f$ is continuous on $[a, b]$ and $F$ is any antiderivative of $f$ ($F' = f$), then:
$$\int_a^b f(x) \, dx = [F(x)]_a^b = F(b) - F(a)$$

---

## 5. Geometric Applications

### 5.1 Planar Area Between Curves
If $f(x) \ge g(x)$ for all $x \in [a, b]$, the total area enclosed between the curves is:
$$A = \int_a^b [f(x) - g(x)] \, dx$$

### 5.2 Volumes of Solids of Revolution
* **Disk Method** (rotation around $x$-axis):
  $$V = \pi \int_a^b [f(x)]^2 \, dx$$
* **Washer Method** (rotation between two curves $f(x) \ge g(x)$ around $x$-axis):
  $$V = \pi \int_a^b \left( [f(x)]^2 - [g(x)]^2 \right) \, dx$$

