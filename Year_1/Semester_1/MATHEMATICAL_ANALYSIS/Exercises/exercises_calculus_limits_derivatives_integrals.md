# Practice Exercises: Limits, Derivatives, and Integrals

This drill document provides comprehensive worked problems covering analytical limits, differentiability proofs, curve sketching, and integration techniques.

---

## Section 1: Limits and Indeterminate Forms

### Problem 1: Factoring and Rationalization
**Problem:** Evaluate the limits:
1. $\displaystyle L_1 = \lim_{x \to 3} \frac{x^3 - 27}{x^2 - 9}$
2. $\displaystyle L_2 = \lim_{x \to 0} \frac{\sqrt{1 + x + x^2} - 1}{x}$

**Step-by-Step Solution:**
1. Direct substitution yields $\frac{0}{0}$. Factor numerator as difference of cubes and denominator as difference of squares:
   $$x^3 - 27 = (x - 3)(x^2 + 3x + 9)$$
   $$x^2 - 9 = (x - 3)(x + 3)$$
   Cancel the common factor $(x - 3) \neq 0$:
   $$L_1 = \lim_{x \to 3} \frac{(x - 3)(x^2 + 3x + 9)}{(x - 3)(x + 3)} = \lim_{x \to 3} \frac{x^2 + 3x + 9}{x + 3} = \frac{3^2 + 3(3) + 9}{3 + 3} = \frac{27}{6} = \frac{9}{2}$$
2. Multiply numerator and denominator by conjugate $\sqrt{1 + x + x^2} + 1$:
   $$\frac{(\sqrt{1 + x + x^2} - 1)(\sqrt{1 + x + x^2} + 1)}{x(\sqrt{1 + x + x^2} + 1)} = \frac{(1 + x + x^2) - 1}{x(\sqrt{1 + x + x^2} + 1)} = \frac{x(1 + x)}{x(\sqrt{1 + x + x^2} + 1)}$$
   Cancel $x \neq 0$:
   $$L_2 = \lim_{x \to 0} \frac{1 + x}{\sqrt{1 + x + x^2} + 1} = \frac{1 + 0}{\sqrt{1 + 0 + 0} + 1} = \frac{1}{2}$$

---

## Section 2: Differentiation and Applications

### Problem 2: Logarithmic Differentiation
**Problem:** Find the derivative of $y = x^{\sin x}$ for $x > 0$.

**Step-by-Step Solution:**
1. Take the natural logarithm of both sides:
   $$\ln y = \ln(x^{\sin x}) = \sin(x) \ln(x)$$
2. Differentiate both sides with respect to $x$ using chain rule on the left and product rule on the right:
   $$\frac{1}{y} \frac{dy}{dx} = \frac{d}{dx}[\sin x] \ln x + \sin x \frac{d}{dx}[\ln x] = \cos(x) \ln(x) + \frac{\sin(x)}{x}$$
3. Multiply both sides by $y = x^{\sin x}$:
   $$\frac{dy}{dx} = x^{\sin x} \left( \cos(x) \ln(x) + \frac{\sin(x)}{x} \right)$$

---

### Problem 3: Complete Curve Sketching
**Problem:** Analyze the rational function $f(x) = \frac{x^2 - 4}{x^2 - 1}$. Determine domain, symmetry, asymptotes, intervals of increase/decrease, and local extrema.

**Step-by-Step Solution:**
1. **Domain**: $x^2 - 1 \neq 0 \implies x \neq \pm 1$. Domain: $\mathbb{R} \setminus \{-1, 1\}$.
2. **Symmetry**: $f(-x) = \frac{(-x)^2 - 4}{(-x)^2 - 1} = \frac{x^2 - 4}{x^2 - 1} = f(x)$ (Even function, symmetric about $y$-axis).
3. **Asymptotes**:
   - Vertical asymptotes: $x = -1$ and $x = 1$ (since numerator is $-3 \neq 0$).
   - Horizontal asymptote: $\lim_{x \to \pm\infty} \frac{x^2 - 4}{x^2 - 1} = \lim_{x \to \pm\infty} \frac{1 - 4/x^2}{1 - 1/x^2} = 1 \implies y = 1$.
4. **First Derivative**:
   $$f'(x) = \frac{2x(x^2 - 1) - (x^2 - 4)(2x)}{(x^2 - 1)^2} = \frac{2x^3 - 2x - 2x^3 + 8x}{(x^2 - 1)^2} = \frac{6x}{(x^2 - 1)^2}$$
   - Critical point: $f'(x) = 0 \implies 6x = 0 \implies x = 0$.
   - For $x < 0$ ($x \neq -1$): $f'(x) < 0 \implies f$ is strictly decreasing.
   - For $x > 0$ ($x \neq 1$): $f'(x) > 0 \implies f$ is strictly increasing.
   - At $x = 0$: $f(0) = \frac{-4}{-1} = 4$. By the first derivative test, $(0, 4)$ is a strict **local minimum**.

---

## Section 3: Integration Techniques

### Problem 4: Integration by Parts
**Problem:** Evaluate the indefinite integral:
$$I = \int x^2 e^{2x} \, dx$$

**Step-by-Step Solution:**
1. Apply integration by parts ($\int u \, dv = uv - \int v \, du$):
   - Choose $u = x^2 \implies du = 2x \, dx$.
   - Choose $dv = e^{2x} \, dx \implies v = \frac{1}{2} e^{2x}$.
   $$I = x^2 \left( \frac{1}{2} e^{2x} \right) - \int \left( \frac{1}{2} e^{2x} \right) (2x) \, dx = \frac{1}{2} x^2 e^{2x} - \int x e^{2x} \, dx$$
2. Apply integration by parts a second time on $\int x e^{2x} \, dx$:
   - Choose $u_1 = x \implies du_1 = dx$.
   - Choose $dv_1 = e^{2x} \, dx \implies v_1 = \frac{1}{2} e^{2x}$.
   $$\int x e^{2x} \, dx = \frac{1}{2} x e^{2x} - \int \frac{1}{2} e^{2x} \, dx = \frac{1}{2} x e^{2x} - \frac{1}{4} e^{2x}$$
3. Combine results:
   $$I = \frac{1}{2} x^2 e^{2x} - \left( \frac{1}{2} x e^{2x} - \frac{1}{4} e^{2x} \right) + C = e^{2x} \left( \frac{1}{2} x^2 - \frac{1}{2} x + \frac{1}{4} \right) + C$$

---

### Problem 5: Definite Integral Area Calculation
**Problem:** Calculate the area of the finite region enclosed between $y = 2 - x^2$ and $y = x$.

**Step-by-Step Solution:**
1. Find intersection points:
   $$2 - x^2 = x \implies x^2 + x - 2 = 0 \implies (x + 2)(x - 1) = 0$$
   Intersections occur at $x = -2$ and $x = 1$.
2. On interval $[-2, 1]$, test point $x = 0$: $2 - 0^2 = 2 > 0$, so $2 - x^2 \ge x$.
3. Compute area integral:
   $$A = \int_{-2}^1 [(2 - x^2) - x] \, dx = \left[ 2x - \frac{x^3}{3} - \frac{x^2}{2} \right]_{-2}^1$$
4. Evaluate at bounds:
   - At $x = 1$: $2(1) - \frac{1}{3} - \frac{1}{2} = 2 - \frac{5}{6} = \frac{7}{6}$.
   - At $x = -2$: $2(-2) - \frac{(-2)^3}{3} - \frac{(-2)^2}{2} = -4 + \frac{8}{3} - 2 = -6 + \frac{8}{3} = -\frac{10}{3} = -\frac{20}{6}$.
   $$A = \frac{7}{6} - \left( -\frac{20}{6} \right) = \frac{27}{6} = \frac{9}{2} = 4.5$$

