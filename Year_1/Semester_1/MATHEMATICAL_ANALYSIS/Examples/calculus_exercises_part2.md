# Mathematical Analysis: Calculus 1 Exercises (Part 2)

This file contains advanced exercises on integration techniques, series, and other challenging topics.

---

### Section 1: Advanced Integration Techniques

**Exercise 1:** Find the integral: $\int x \cos(x) dx$
**Solution:**
Use integration by parts: $\int u dv = uv - \int v du$.
Let $u = x$ and $dv = \cos(x) dx$. Then $du = dx$ and $v = \sin(x)$.
$$\int x \cos(x) dx = x \sin(x) - \int \sin(x) dx = x \sin(x) + \cos(x) + C$$

**Exercise 2:** Find the integral: $\int \ln(x) dx$
**Solution:**
Use integration by parts. Let $u = \ln(x)$ and $dv = dx$. Then $du = \frac{1}{x} dx$ and $v = x$.
$$\int \ln(x) dx = x \ln(x) - \int x \cdot \frac{1}{x} dx = x \ln(x) - \int 1 dx = x \ln(x) - x + C$$

**Exercise 3:** Evaluate the integral: $\int_0^1 x e^x dx$
**Solution:**
Use integration by parts. Let $u = x$ and $dv = e^x dx$. Then $du = dx$ and $v = e^x$.
$$\int x e^x dx = x e^x - \int e^x dx = x e^x - e^x$$
$$\int_0^1 x e^x dx = [x e^x - e^x]_0^1 = (1e^1 - e^1) - (0 - e^0) = 0 - (-1) = 1$$

**Exercise 4:** Find the integral: $\int \sin^2(x) dx$
**Solution:**
Use the half-angle identity: $\sin^2(x) = \frac{1 - \cos(2x)}{2}$.
$$\int \frac{1 - \cos(2x)}{2} dx = \frac{1}{2} \int (1 - \cos(2x)) dx = \frac{1}{2} (x - \frac{1}{2}\sin(2x)) + C = \frac{x}{2} - \frac{\sin(2x)}{4} + C$$

**Exercise 5:** Find the integral: $\int \frac{1}{x^2 + a^2} dx$
**Solution:**
This is a standard integral form related to arctangent.
$$\int \frac{1}{x^2 + a^2} dx = \frac{1}{a} \arctan\left(\frac{x}{a}\right) + C$$

**Exercise 6:** Find the integral: $\int \frac{dx}{\sqrt{a^2 - x^2}}$
**Solution:**
This is a standard integral form related to arcsin.
$$\int \frac{dx}{\sqrt{a^2 - x^2}} = \arcsin\left(\frac{x}{a}\right) + C$$

**Exercise 7:** Use trigonometric substitution to find $\int \frac{dx}{x^2\sqrt{4 - x^2}}$.
**Solution:**
Let $x = 2\sin(\theta)$, so $dx = 2\cos(\theta)d\theta$.
$$\int \frac{2\cos(\theta)d\theta}{(2\sin\theta)^2\sqrt{4 - 4\sin^2\theta}} = \int \frac{2\cos(\theta)}{4\sin^2\theta \cdot 2\cos\theta} d\theta = \frac{1}{4} \int \csc^2(\theta) d\theta$$
$$= -\frac{1}{4}\cot(\theta) + C = -\frac{1}{4} \frac{\sqrt{4-x^2}}{x} + C$$

**Exercise 8:** Use partial fractions to find $\int \frac{5x-3}{x^2-2x-3} dx$.
**Solution:**
Factor the denominator: $x^2-2x-3 = (x-3)(x+1)$.
$$\frac{5x-3}{(x-3)(x+1)} = \frac{A}{x-3} + \frac{B}{x+1}$$
$5x-3 = A(x+1) + B(x-3)$.
If $x=3$, $12 = 4A \implies A=3$.
If $x=-1$, $-8 = -4B \implies B=2$.
$$\int \left(\frac{3}{x-3} + \frac{2}{x+1}\right) dx = 3\ln|x-3| + 2\ln|x+1| + C$$

---

### Section 2: Improper Integrals

**Exercise 9:** Evaluate $\int_1^\infty \frac{1}{x^2} dx$.
**Solution:**
$$\int_1^\infty \frac{1}{x^2} dx = \lim_{b \to \infty} \int_1^b x^{-2} dx = \lim_{b \to \infty} [-x^{-1}]_1^b = \lim_{b \to \infty} (-\frac{1}{b} + 1) = 1$$

**Exercise 10:** Evaluate $\int_0^1 \frac{1}{\sqrt{x}} dx$.
**Solution:**
$$\int_0^1 x^{-1/2} dx = \lim_{a \to 0^+} \int_a^1 x^{-1/2} dx = \lim_{a \to 0^+} [2\sqrt{x}]_a^1 = \lim_{a \to 0^+} (2 - 2\sqrt{a}) = 2$$

**Exercise 11:** Determine if $\int_1^\infty \frac{1}{x} dx$ converges or diverges.
**Solution:**
$$\int_1^\infty \frac{1}{x} dx = \lim_{b \to \infty} [\ln|x|]_1^b = \lim_{b \to \infty} (\ln(b) - 0) = \infty$$
The integral diverges.

---

### Section 3: Sequences and Series

**Exercise 12:** Determine if the sequence $a_n = \frac{n}{n+1}$ converges.
**Solution:**
$$\lim_{n \to \infty} \frac{n}{n+1} = \lim_{n \to \infty} \frac{1}{1+1/n} = 1$$
The sequence converges to 1.

**Exercise 13:** Determine if the geometric series $\sum_{n=0}^\infty (\frac{1}{2})^n$ converges.
**Solution:**
This is a geometric series with ratio $r = 1/2$. Since $|r| < 1$, the series converges.
The sum is $S = \frac{a}{1-r} = \frac{1}{1 - 1/2} = 2$.

**Exercise 14:** Use the integral test to determine if $\sum_{n=1}^\infty \frac{1}{n^2}$ converges.
**Solution:**
Consider the integral $\int_1^\infty \frac{1}{x^2} dx$. From Exercise 9, this integral converges to 1.
Therefore, by the integral test, the series $\sum_{n=1}^\infty \frac{1}{n^2}$ also converges.

**Exercise 15:** Use the ratio test to determine if $\sum_{n=1}^\infty \frac{n}{2^n}$ converges.
**Solution:**
$$L = \lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| = \lim_{n \to \infty} \frac{n+1}{2^{n+1}} \cdot \frac{2^n}{n} = \lim_{n \to \infty} \frac{n+1}{2n} = \frac{1}{2}$$
Since $L < 1$, the series converges.

**Exercise 16:** Determine if the alternating series $\sum_{n=1}^\infty \frac{(-1)^{n-1}}{n}$ converges.
**Solution:**
This is the alternating harmonic series.
1. $b_n = 1/n > 0$.
2. $\lim_{n \to \infty} b_n = 0$.
3. $b_{n+1} = \frac{1}{n+1} \leq \frac{1}{n} = b_n$.
By the Alternating Series Test, the series converges.

---

### Section 4: Taylor and Maclaurin Series

**Exercise 17:** Find the Maclaurin series for $f(x) = e^x$.
**Solution:**
$f^{(n)}(x) = e^x$ for all $n$, so $f^{(n)}(0) = 1$.
$$e^x = \sum_{n=0}^\infty \frac{f^{(n)}(0)}{n!}x^n = \sum_{n=0}^\infty \frac{1}{n!}x^n = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots$$

**Exercise 18:** Find the Maclaurin series for $f(x) = \sin(x)$.
**Solution:**
$f(0)=0, f'(0)=1, f''(0)=0, f'''(0)=-1, \dots$
$$\sin(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \dots = \sum_{n=0}^\infty \frac{(-1)^n}{(2n+1)!}x^{2n+1}$$

**Exercise 19:** Find the Taylor series for $f(x) = \ln(x)$ centered at $a=1$.
**Solution:**
$f(1)=0, f'(x)=1/x \implies f'(1)=1, f''(x)=-1/x^2 \implies f''(1)=-1, f'''(x)=2/x^3 \implies f'''(1)=2$.
In general, $f^{(n)}(1) = (-1)^{n-1}(n-1)!$ for $n \geq 1$.
$$\ln(x) = \sum_{n=1}^\infty \frac{(-1)^{n-1}(n-1)!}{n!}(x-1)^n = \sum_{n=1}^\infty \frac{(-1)^{n-1}}{n}(x-1)^n$$

**Exercise 20:** Use the Maclaurin series for $e^x$ to find the series for $e^{-x^2}$.
**Solution:**
Substitute $-x^2$ into the series for $e^u$:
$$e^{-x^2} = \sum_{n=0}^\infty \frac{(-x^2)^n}{n!} = \sum_{n=0}^\infty \frac{(-1)^n x^{2n}}{n!} = 1 - x^2 + \frac{x^4}{2!} - \frac{x^6}{3!} + \dots$$

---

### Section 5: Parametric Equations and Polar Coordinates

**Exercise 21:** Find the slope of the tangent line to the parametric curve $x=t^2, y=t^3-3t$ at $t=2$.
**Solution:**
$\frac{dx}{dt} = 2t$, $\frac{dy}{dt} = 3t^2 - 3$.
$$\frac{dy}{dx} = \frac{dy/dt}{dx/dt} = \frac{3t^2-3}{2t}$$
At $t=2$, the slope is $\frac{3(2^2)-3}{2(2)} = \frac{12-3}{4} = \frac{9}{4}$.

**Exercise 22:** Find the arc length of the curve $x=\cos(t), y=\sin(t)$ for $0 \leq t \leq 2\pi$.
**Solution:**
$$L = \int_0^{2\pi} \sqrt{(\frac{dx}{dt})^2 + (\frac{dy}{dt})^2} dt = \int_0^{2\pi} \sqrt{(-\sin t)^2 + (\cos t)^2} dt$$
$$= \int_0^{2\pi} \sqrt{\sin^2 t + \cos^2 t} dt = \int_0^{2\pi} 1 dt = 2\pi$$

**Exercise 23:** Convert the polar equation $r = 2\cos(\theta)$ to Cartesian coordinates.
**Solution:**
Multiply by $r$: $r^2 = 2r\cos(\theta)$.
Since $r^2 = x^2+y^2$ and $x = r\cos(\theta)$, we have $x^2+y^2 = 2x$.
This is the equation of a circle: $(x-1)^2 + y^2 = 1$.

**Exercise 24:** Find the area of the region enclosed by one loop of the polar curve $r = \cos(2\theta)$.
**Solution:**
One loop is traced from $\theta = -\pi/4$ to $\theta = \pi/4$.
$$A = \frac{1}{2} \int_{-\pi/4}^{\pi/4} r^2 d\theta = \frac{1}{2} \int_{-\pi/4}^{\pi/4} \cos^2(2\theta) d\theta$$
Use $\cos^2(u) = \frac{1+\cos(2u)}{2}$:
$$A = \frac{1}{2} \int_{-\pi/4}^{\pi/4} \frac{1+\cos(4\theta)}{2} d\theta = \frac{1}{4} \left[\theta + \frac{1}{4}\sin(4\theta)\right]_{-\pi/4}^{\pi/4}$$
$$= \frac{1}{4} [(\frac{\pi}{4} + 0) - (-\frac{\pi}{4} + 0)] = \frac{1}{4}(\frac{\pi}{2}) = \frac{\pi}{8}$$

---

### Section 6: Further Challenging Problems

**Exercise 25:** Evaluate $\int e^x \sin(x) dx$.
**Solution:**
Use integration by parts twice.
Let $I = \int e^x \sin(x) dx$.
$u = \sin(x), dv = e^x dx \implies du = \cos(x) dx, v = e^x$.
$I = e^x \sin(x) - \int e^x \cos(x) dx$.
For the second integral, $u = \cos(x), dv = e^x dx \implies du = -\sin(x) dx, v = e^x$.
$\int e^x \cos(x) dx = e^x \cos(x) + \int e^x \sin(x) dx = e^x \cos(x) + I$.
Substitute back: $I = e^x \sin(x) - (e^x \cos(x) + I)$.
$2I = e^x(\sin(x) - \cos(x)) \implies I = \frac{e^x}{2}(\sin(x) - \cos(x)) + C$.

**Exercise 26:** Find the sum of the series $\sum_{n=1}^\infty \frac{1}{n(n+1)}$.
**Solution:**
This is a telescoping series. Use partial fractions: $\frac{1}{n(n+1)} = \frac{1}{n} - \frac{1}{n+1}$.
The $k$-th partial sum is $S_k = \sum_{n=1}^k (\frac{1}{n} - \frac{1}{n+1}) = (1 - \frac{1}{2}) + (\frac{1}{2} - \frac{1}{3}) + \dots + (\frac{1}{k} - \frac{1}{k+1}) = 1 - \frac{1}{k+1}$.
$$\lim_{k \to \infty} S_k = \lim_{k \to \infty} (1 - \frac{1}{k+1}) = 1$$

**Exercise 27:** Evaluate the limit $\lim_{x \to 0^+} x^x$.
**Solution:**
This is an indeterminate form $0^0$. Let $y = x^x$, so $\ln(y) = x \ln(x)$.
$$\lim_{x \to 0^+} x \ln(x) = \lim_{x \to 0^+} \frac{\ln(x)}{1/x}$$
This is $\frac{-\infty}{\infty}$, so use L'Hôpital's Rule:
$$\lim_{x \to 0^+} \frac{1/x}{-1/x^2} = \lim_{x \to 0^+} (-x) = 0$$
Since $\ln(y) \to 0$, $y \to e^0 = 1$.

**Exercise 28:** Find the volume of the solid obtained by rotating the region bounded by $y=\sqrt{x}$, $y=0$, and $x=1$ about the x-axis.
**Solution:**
Use the disk method.
$$V = \pi \int_0^1 (\sqrt{x})^2 dx = \pi \int_0^1 x dx = \pi \left[\frac{x^2}{2}\right]_0^1 = \frac{\pi}{2}$$

**Exercise 29:** Find the interval of convergence of the power series $\sum_{n=1}^\infty \frac{(x-3)^n}{n}$.
**Solution:**
Use the ratio test.
$$L = \lim_{n \to \infty} \left| \frac{(x-3)^{n+1}}{n+1} \cdot \frac{n}{(x-3)^n} \right| = \lim_{n \to \infty} \frac{n}{n+1} |x-3| = |x-3|$$
The series converges for $|x-3| < 1$, which is $2 < x < 4$.
Check endpoints:
- $x=2$: $\sum \frac{(-1)^n}{n}$ converges (alternating harmonic).
- $x=4$: $\sum \frac{1}{n}$ diverges (harmonic).
The interval of convergence is $[2, 4)$.

**Exercise 30:** Use a Taylor series to approximate $\int_0^{0.1} e^{-x^2} dx$ to four decimal places.
**Solution:**
From Exercise 20, $e^{-x^2} = 1 - x^2 + \frac{x^4}{2} - \dots$.
$$\int_0^{0.1} e^{-x^2} dx = \int_0^{0.1} (1 - x^2 + \frac{x^4}{2} - \dots) dx = \left[x - \frac{x^3}{3} + \frac{x^5}{10} - \dots\right]_0^{0.1}$$
$$= 0.1 - \frac{(0.1)^3}{3} + \frac{(0.1)^5}{10} - \dots = 0.1 - \frac{0.001}{3} + \frac{0.00001}{10} \approx 0.1 - 0.000333 + 0.000001 \approx 0.09967$$
To four decimal places, the approximation is $0.0997$.
