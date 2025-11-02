# Mathematical Analysis: Calculus 1 Exercises (Part 1)

This file contains introductory exercises on limits, derivatives, and basic applications.

---

### Section 1: Limits of Functions

**Exercise 1:** Find the limit: $\lim_{x \to 2} (3x^2 - 5x + 1)$
**Solution:**
Substitute $x=2$ into the expression:
$$3(2)^2 - 5(2) + 1 = 3(4) - 10 + 1 = 12 - 10 + 1 = 3$$

**Exercise 2:** Find the limit: $\lim_{x \to -1} \frac{x^2 + 2x + 1}{x + 1}$
**Solution:**
Factor the numerator: $x^2 + 2x + 1 = (x+1)^2$.
$$\lim_{x \to -1} \frac{(x+1)^2}{x + 1} = \lim_{x \to -1} (x+1) = -1 + 1 = 0$$

**Exercise 3:** Find the limit: $\lim_{x \to 3} \frac{x^2 - 9}{x - 3}$
**Solution:**
Factor the numerator: $x^2 - 9 = (x-3)(x+3)$.
$$\lim_{x \to 3} \frac{(x-3)(x+3)}{x - 3} = \lim_{x \to 3} (x+3) = 3 + 3 = 6$$

**Exercise 4:** Find the limit: $\lim_{x \to 0} \frac{\sin(x)}{x}$
**Solution:**
This is a standard trigonometric limit.
$$\lim_{x \to 0} \frac{\sin(x)}{x} = 1$$

**Exercise 5:** Find the limit: $\lim_{x \to \infty} \frac{2x^2 - 1}{3x^2 + x}$
**Solution:**
Divide the numerator and denominator by the highest power of $x$, which is $x^2$.
$$\lim_{x \to \infty} \frac{2 - 1/x^2}{3 + 1/x} = \frac{2 - 0}{3 + 0} = \frac{2}{3}$$

---

### Section 2: Continuity

**Exercise 6:** Determine if the function $f(x) = x^2 + 1$ is continuous at $x=1$.
**Solution:**
The function is a polynomial, which is continuous everywhere.
$f(1) = 1^2 + 1 = 2$.
$\lim_{x \to 1} (x^2 + 1) = 1^2 + 1 = 2$.
Since $f(1) = \lim_{x \to 1} f(x)$, the function is continuous at $x=1$.

**Exercise 7:** Find the value of $c$ that makes the function continuous at $x=2$.
$f(x) = \begin{cases} x^2 & \text{if } x \leq 2 \\ cx + 3 & \text{if } x > 2 \end{cases}$
**Solution:**
For continuity, the left-hand limit must equal the right-hand limit at $x=2$.
$\lim_{x \to 2^-} f(x) = 2^2 = 4$.
$\lim_{x \to 2^+} f(x) = c(2) + 3 = 2c + 3$.
Set them equal: $4 = 2c + 3 \implies 2c = 1 \implies c = 1/2$.

---

### Section 3: Derivatives using the Limit Definition

**Exercise 8:** Find the derivative of $f(x) = 3x + 2$ using the limit definition.
**Solution:**
$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h} = \lim_{h \to 0} \frac{(3(x+h) + 2) - (3x+2)}{h}$$
$$= \lim_{h \to 0} \frac{3x + 3h + 2 - 3x - 2}{h} = \lim_{h \to 0} \frac{3h}{h} = 3$$

**Exercise 9:** Find the derivative of $f(x) = x^2$ using the limit definition.
**Solution:**
$$f'(x) = \lim_{h \to 0} \frac{(x+h)^2 - x^2}{h} = \lim_{h \to 0} \frac{x^2 + 2xh + h^2 - x^2}{h}$$
$$= \lim_{h \to 0} \frac{2xh + h^2}{h} = \lim_{h \to 0} (2x + h) = 2x$$

---

### Section 4: Basic Differentiation Rules

**Exercise 10:** Find the derivative of $f(x) = 5x^4 - 2x^3 + x - 7$.
**Solution:**
Using the power rule:
$$f'(x) = 5(4x^3) - 2(3x^2) + 1 - 0 = 20x^3 - 6x^2 + 1$$

**Exercise 11:** Find the derivative of $f(x) = \sqrt{x}$.
**Solution:**
Rewrite as $f(x) = x^{1/2}$.
$$f'(x) = \frac{1}{2}x^{-1/2} = \frac{1}{2\sqrt{x}}$$

**Exercise 12:** Find the derivative of $f(x) = \sin(x) + \cos(x)$.
**Solution:**
$$f'(x) = \cos(x) - \sin(x)$$

**Exercise 13:** Find the derivative of $f(x) = e^x \ln(x)$.
**Solution:**
Using the product rule: $(uv)' = u'v + uv'$.
$$f'(x) = (e^x)'\ln(x) + e^x(\ln(x))' = e^x\ln(x) + e^x\frac{1}{x}$$

**Exercise 14:** Find the derivative of $g(t) = \frac{t^2}{t+1}$.
**Solution:**
Using the quotient rule: $(\frac{u}{v})' = \frac{u'v - uv'}{v^2}$.
$$g'(t) = \frac{(2t)(t+1) - (t^2)(1)}{(t+1)^2} = \frac{2t^2 + 2t - t^2}{(t+1)^2} = \frac{t^2 + 2t}{(t+1)^2}$$

**Exercise 15:** Find the derivative of $h(x) = (x^2 + 1)^5$.
**Solution:**
Using the chain rule:
$$h'(x) = 5(x^2 + 1)^4 \cdot (2x) = 10x(x^2 + 1)^4$$

**Exercise 16:** Find the derivative of $f(x) = \cos(3x^2)$.
**Solution:**
Using the chain rule:
$$f'(x) = -\sin(3x^2) \cdot (6x) = -6x\sin(3x^2)$$

**Exercise 17:** Find the derivative of $f(x) = \ln(x^2 + 4)$.
**Solution:**
Using the chain rule:
$$f'(x) = \frac{1}{x^2+4} \cdot (2x) = \frac{2x}{x^2+4}$$

---

### Section 5: Applications of Derivatives

**Exercise 18:** Find the equation of the tangent line to $f(x) = x^3 - 2x$ at $x=2$.
**Solution:**
First, find the slope by calculating the derivative: $f'(x) = 3x^2 - 2$.
The slope at $x=2$ is $m = f'(2) = 3(2)^2 - 2 = 12 - 2 = 10$.
The point on the curve is $(2, f(2))$. $f(2) = 2^3 - 2(2) = 8 - 4 = 4$.
Using the point-slope form $y - y_1 = m(x - x_1)$:
$$y - 4 = 10(x - 2) \implies y = 10x - 20 + 4 \implies y = 10x - 16$$

**Exercise 19:** Find the critical points of $f(x) = x^3 - 6x^2 + 5$.
**Solution:**
Find the derivative and set it to zero: $f'(x) = 3x^2 - 12x$.
$$3x^2 - 12x = 0 \implies 3x(x - 4) = 0$$
The critical points are $x=0$ and $x=4$.

**Exercise 20:** Determine the intervals where $f(x) = x^3 - 3x$ is increasing or decreasing.
**Solution:**
Find the derivative: $f'(x) = 3x^2 - 3 = 3(x^2 - 1) = 3(x-1)(x+1)$.
The critical points are $x=-1$ and $x=1$.
Test intervals:
- $(-\infty, -1)$: $f'(-2) = 3(3) > 0$ (increasing)
- $(-1, 1)$: $f'(0) = -3 < 0$ (decreasing)
- $(1, \infty)$: $f'(2) = 3(3) > 0$ (increasing)

**Exercise 21:** Find the local maximum and minimum values of $f(x) = 2x^3 - 3x^2 - 12x + 1$.
**Solution:**
$f'(x) = 6x^2 - 6x - 12 = 6(x^2 - x - 2) = 6(x-2)(x+1)$.
Critical points are $x=2$ and $x=-1$.
Use the second derivative test: $f''(x) = 12x - 6$.
- $f''(-1) = -12 - 6 = -18 < 0$, so there is a local maximum at $x=-1$.
- $f''(2) = 24 - 6 = 18 > 0$, so there is a local minimum at $x=2$.

**Exercise 22:** A particle moves along a line with position function $s(t) = t^3 - 6t^2 + 9t$. Find its velocity at time $t$.
**Solution:**
Velocity is the derivative of position:
$$v(t) = s'(t) = 3t^2 - 12t + 9$$

**Exercise 23:** For the particle in the previous exercise, when is the particle at rest?
**Solution:**
The particle is at rest when $v(t) = 0$.
$$3t^2 - 12t + 9 = 0 \implies 3(t^2 - 4t + 3) = 0 \implies 3(t-1)(t-3) = 0$$
The particle is at rest at $t=1$ and $t=3$.

---

### Section 6: L'Hôpital's Rule

**Exercise 24:** Use L'Hôpital's Rule to find the limit: $\lim_{x \to 0} \frac{e^x - 1}{x}$
**Solution:**
This is an indeterminate form $\frac{0}{0}$.
$$\lim_{x \to 0} \frac{\frac{d}{dx}(e^x - 1)}{\frac{d}{dx}(x)} = \lim_{x \to 0} \frac{e^x}{1} = e^0 = 1$$

**Exercise 25:** Use L'Hôpital's Rule to find the limit: $\lim_{x \to \infty} \frac{\ln(x)}{x}$
**Solution:**
This is an indeterminate form $\frac{\infty}{\infty}$.
$$\lim_{x \to \infty} \frac{\frac{d}{dx}(\ln x)}{\frac{d}{dx}(x)} = \lim_{x \to \infty} \frac{1/x}{1} = 0$$

**Exercise 26:** Find the limit: $\lim_{x \to 0} \frac{1 - \cos(x)}{x^2}$
**Solution:**
This is a $\frac{0}{0}$ form. Apply L'Hôpital's Rule.
$$\lim_{x \to 0} \frac{\sin(x)}{2x}$$
This is still $\frac{0}{0}$. Apply the rule again.
$$\lim_{x \to 0} \frac{\cos(x)}{2} = \frac{1}{2}$$

---

### Section 7: Basic Integration

**Exercise 27:** Find the indefinite integral: $\int (3x^2 + 4x - 5) dx$
**Solution:**
$$\int (3x^2 + 4x - 5) dx = 3\frac{x^3}{3} + 4\frac{x^2}{2} - 5x + C = x^3 + 2x^2 - 5x + C$$

**Exercise 28:** Find the indefinite integral: $\int \frac{1}{x} dx$
**Solution:**
$$\int \frac{1}{x} dx = \ln|x| + C$$

**Exercise 29:** Evaluate the definite integral: $\int_0^1 (x^2 + 1) dx$
**Solution:**
$$\int_0^1 (x^2 + 1) dx = \left[ \frac{x^3}{3} + x \right]_0^1 = \left(\frac{1^3}{3} + 1\right) - (0) = \frac{1}{3} + 1 = \frac{4}{3}$$

**Exercise 30:** Evaluate the definite integral: $\int_0^{\pi} \sin(x) dx$
**Solution:**
$$\int_0^{\pi} \sin(x) dx = [-\cos(x)]_0^{\pi} = (-\cos(\pi)) - (-\cos(0)) = -(-1) - (-1) = 1 + 1 = 2$$
