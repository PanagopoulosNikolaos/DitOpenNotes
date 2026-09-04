# 1. (1 point) The function is given $f(x) = \begin{cases} 7x^2 - 6, & x < 0 \\ 3, & x = 0 \\ 3x - 4, & x > 0 \end{cases}$.
Which of the following propositions hold for the function $f$?

a. The limit $\lim_{x \to 0} f(x)$ exists

b. The value $f(0)$ exists

c. $f$ is continuous at $x=0$

d. $f$ is not differentiable at $x=0$

**Solution:**

To examine the propositions, we will analyze the behavior of the function around $x=0$.

1.  **Examination of the limit (Proposition a):**
    *   We compute the one-sided limit as $x$ tends to 0 from the left (x < 0):
        $\lim_{x \to 0^-} f(x) = \lim_{x \to 0^-} (7x^2 - 6) = 7(0)^2 - 6 = -6$.
    *   We compute the one-sided limit as $x$ tends to 0 from the right (x > 0):
        $\lim_{x \to 0^+} f(x) = \lim_{x \to 0^+} (3x - 4) = 3(0) - 4 = -4$.
    *   Since the two one-sided limits are different ($-6 \neq -4$), the limit $\lim_{x \to 0} f(x)$ **does not exist**. Therefore, proposition (a) is false.

2.  **Examination of the value at x=0 (Proposition b):**
    *   From the definition of the function, for $x=0$, we have $f(0) = 3$.
    *   Therefore, $f(0)$ **exists**. Thus, proposition (b) is true.

3.  **Examination of continuity (Proposition c):**
    *   For a function to be continuous at $x=0$, it must hold that $\lim_{x \to 0} f(x) = f(0)$.
    *   As we saw, $\lim_{x \to 0} f(x)$ does not exist.
    *   Therefore, $f$ **is not continuous** at $x=0$. Thus, proposition (c) is false.

4.  **Examination of differentiability (Proposition d):**
    *   A fundamental property of functions is that if a function is differentiable at a point, then it is also continuous at that point.
    *   Since $f$ is not continuous at $x=0$, it cannot be differentiable either.
    *   Therefore, $f$ **is not differentiable** at $x=0$. Thus, proposition (d) is true.

**Correct propositions: b, d**

# 2. (0.5 points) Let $h(x) = \frac{3x-1}{5x-2}$. Then $h'(x) =$

a. $-\frac{\alpha}{2x}$ 

b. $\frac{6x^2-2x+3}{(3x-1)^2}$ 

c. $\frac{5x^2-2x-9}{(3x-1)^2}$ 

d. $\frac{1}{(5x-2)^2}$

**Solution:**

To find the derivative of $h(x)$, we use the quotient rule for differentiation:
$(\frac{f}{g})' = \frac{f'g - fg'}{g^2}$.

In our case, $f(x) = 3x-1$ and $g(x) = 5x-2$.

1.  **We compute the derivatives of $f(x)$ and $g(x)$:**
    *   $f'(x) = (3x-1)' = 3$
    *   $g'(x) = (5x-2)' = 5$

2.  **We apply the quotient rule:**
    $h'(x) = \frac{(3x-1)'(5x-2) - (3x-1)(5x-2)'}{(5x-2)^2}$
    $h'(x) = \frac{3(5x-2) - (3x-1)5}{(5x-2)^2}$

3.  **We simplify the numerator expression:**
    $h'(x) = \frac{15x - 6 - (15x - 5)}{(5x-2)^2}$
    $h'(x) = \frac{15x - 6 - 15x + 5}{(5x-2)^2}$
    $h'(x) = \frac{-1}{(5x-2)^2}$

None of the options a, b, c, d matches exactly with the result. Option (d) has the correct denominator but wrong numerator. If we assume a typographical error in option (d) and that the numerator should be -1, then this would be the correct answer. Based on the given options, none is correct. The correct result is $h'(x) = -\frac{1}{(5x-2)^2}$.

**Correct answer (outside options):** $h'(x) = -\frac{1}{(5x-2)^2}$

# 3. (1 point) Find the equation of the tangent to the curve $2xy - y^2 = 1$ at the point $(2,1)$. Select the correct answer.

a. $y = x - 1$

b. $y = -x + 1$

c. $y = 1$

d. $x = 1$

**Solution:**

To find the slope of the tangent, we need the value of the derivative $\frac{dy}{dx}$ at the point $(2,1)$. We use implicit differentiation.

1.  **We differentiate both sides of the equation $2xy - y^2 = 1$ with respect to $x$:**
    $\frac{d}{dx}(2xy - y^2) = \frac{d}{dx}(1)$
    $\frac{d}{dx}(2xy) - \frac{d}{dx}(y^2) = 0$

2.  **We apply the product rule for the term $2xy$ and the chain rule for the term $y^2$ (where $y$ is a function of $x$):**
    $[(\frac{d}{dx}(2x))y + 2x(\frac{d}{dx}(y))] - [2y \cdot \frac{dy}{dx}] = 0$
    $[2y + 2x \frac{dy}{dx}] - 2y \frac{dy}{dx} = 0$

3.  **We solve the equation for $\frac{dy}{dx}$:**
    $2y + (2x - 2y) \frac{dy}{dx} = 0$
    $(2x - 2y) \frac{dy}{dx} = -2y$
    $\frac{dy}{dx} = \frac{-2y}{2x - 2y} = \frac{-y}{x - y}$

4.  **We compute the slope (m) at the point $(x, y) = (2, 1)$:**
    $m = \frac{-1}{2 - 1} = \frac{-1}{1} = -1$

5.  **We find the equation of the tangent using the form $y - y_1 = m(x - x_1)$ with point $(x_1, y_1) = (2, 1)$ and slope $m = -1$:**
    $y - 1 = -1(x - 2)$
    $y - 1 = -x + 2$
    $y = -x + 3$

None of the given options matches the result $y = -x + 3$. Checking the calculations again, it appears there is an error in the options.

**Correct answer (outside options):** $y = -x + 3$

# 4. (1 point) Which of the following propositions is correct?

a. If $f(x)$ is continuous at a then the limit $\lim_{x \to a} f'(x)$ also exists

b. The indefinite integral is a function

c. If $f'(x)$ is continuous at a then it is also differentiable at a

d. If $v(t)$ is the velocity of a particle moving in a straight line, then $\int_a^b v(t) dt$ equals the difference in the particle's position 
between $t=a$ and $t=b$.

e. The definite integral is a number

**Solution:**

*   **a:** False. A function can be continuous but not differentiable (e.g., $f(x)=|x|$ at $x=0$). If it is not differentiable, the limit of its derivative cannot exist.
*   **b:** False. The indefinite integral $\int f(x)dx$ represents a *family of functions* (the antiderivatives of $f$), which differ by a constant C.
*   **c:** False. The continuity of $f'(x)$ does not guarantee the differentiability of $f'(x)$ (i.e., the existence of $f''(x)$).
*   **d:** True. If $s(t)$ is the position function, then $s'(t) = v(t)$. By the Fundamental Theorem of Calculus, $\int_a^b v(t) dt = \int_a^b s'(t) dt = s(b) - s(a)$, which is the displacement (change in position) of the particle.
*   **e:** True. The definite integral $\int_a^b f(x) dx$, provided it exists, is a specific real number that represents (geometrically) the area between the curve and the x-axis.

Both propositions (d) and (e) are correct. (d) is an application of the definite integral, while (e) is a fundamental definition of it.

**Correct propositions: d, e**

# 5. (1 point) Solve the equation $z^2 - 2z + 5 = 0$ in the set of complex numbers.

**Solution:**

We use the formula for solving the quadratic equation $az^2+bz+c=0$, which is $z = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$.

1.  **We determine the coefficients:**
    $a=1$, $b=-2$, $c=5$.

2.  **We compute the discriminant $\Delta$:**
    $\Delta = b^2 - 4ac = (-2)^2 - 4(1)(5) = 4 - 20 = -16$.

3.  **We find the roots:**
    Since the discriminant is negative, the roots will be complex conjugate numbers.
    $z = \frac{-(-2) \pm \sqrt{-16}}{2(1)}$
    $z = \frac{2 \pm \sqrt{16 \cdot (-1)}}{2}$
    $z = \frac{2 \pm \sqrt{16} \sqrt{-1}}{2}$
    Using the imaginary unit $i = \sqrt{-1}$:
    $z = \frac{2 \pm 4i}{2}$

4.  **We simplify to find the two solutions:**
    $z_1 = \frac{2 + 4i}{2} = 1 + 2i$
    $z_2 = \frac{2 - 4i}{2} = 1 - 2i$

**The solutions are $z = 1 + 2i$ and $z = 1 - 2i$.**

# 6. (1 point) Write in the form $x + yi$ the complex number $\frac{i^5+3}{(i^{21}+i^8+5)}$.

**Solution:**

1.  **We simplify the powers of $i$:**
    The powers of $i$ repeat every 4: $i^1=i, i^2=-1, i^3=-i, i^4=1$. To find a power, we divide the exponent by 4 and keep the remainder.
    *   $i^5 = i^{4 \cdot 1 + 1} = i^1 = i$
    *   $i^{21} = i^{4 \cdot 5 + 1} = i^1 = i$
    *   $i^8 = i^{4 \cdot 2 + 0} = i^0 = 1$

2.  **We substitute the simplified powers into the original expression:**
    $\frac{i^5+3}{i^{21}+i^8+5} = \frac{i+3}{i+1+5} = \frac{3+i}{6+i}$

3.  **We multiply numerator and denominator by the conjugate of the denominator ($6-i$) to convert the denominator to a real number:**
    $\frac{3+i}{6+i} \cdot \frac{6-i}{6-i} = \frac{(3+i)(6-i)}{(6+i)(6-i)}$

4.  **We perform the multiplications:**
    *   Numerator: $(3+i)(6-i) = 18 - 3i + 6i - i^2 = 18 + 3i - (-1) = 19 + 3i$
    *   Denominator: $(6+i)(6-i) = 6^2 - i^2 = 36 - (-1) = 37$

5.  **We combine and write in the final form $x+yi$:**
    $\frac{19+3i}{37} = \frac{19}{37} + \frac{3}{37}i$

**The form $x+yi$ of the complex number is $\frac{19}{37} + \frac{3}{37}i$.**

# 7. (1.5 points) Find the intervals of monotonicity and the local extrema of $f(x) = 2x^3 e^x$.

**Solution:**

1.  **We find the first derivative $f'(x)$ using the product rule $(uv)' = u'v + uv'$:**
    $f'(x) = (2x^3)'e^x + 2x^3(e^x)'$
    $f'(x) = (6x^2)e^x + 2x^3e^x$

2.  **We find the critical points by solving the equation $f'(x)=0$:**
    $6x^2e^x + 2x^3e^x = 0$
    We factor out $2x^2e^x$:
    $2x^2e^x(3 + x) = 0$
    Since $e^x > 0$ for every $x$, the solutions come from:
    $2x^2 = 0 \implies x = 0$
    $3 + x = 0 \implies x = -3$
    The critical points are $x=0$ and $x=-3$.

3.  **We construct a sign table for $f'(x)$ to find the intervals of monotonicity:**
    $f'(x) = 2x^2e^x(3+x)$. The sign depends on the factor $(3+x)$, since $2x^2e^x \ge 0$ for every $x$.
    *   For $x < -3$, the term $(3+x)$ is negative, so $f'(x) < 0$. $f$ is **strictly decreasing** on $(-\infty, -3]$.
    *   For $-3 < x < 0$, the term $(3+x)$ is positive, so $f'(x) > 0$. $f$ is **strictly increasing** on $[-3, 0]$.
    *   For $x > 0$, the term $(3+x)$ is positive, so $f'(x) > 0$. $f$ is **strictly increasing** on $[0, \infty)$.

| Interval | $(-\infty, -3)$ | $(-3, 0)$ | $(0, \infty)$ |
| :--- | :---: | :---: | :---: |
| Sign of $f'(x)$ | - | + | + |
| Monotonicity of $f(x)$ |  |  |  |

4.  **We determine the local extrema:**
    *   At $x=-3$, $f'(x)$ changes sign from negative to positive, so $f$ has a **local minimum**.
        $f(-3) = 2(-3)^3 e^{-3} = 2(-27)e^{-3} = -54e^{-3} = -\frac{54}{e^3}$.
    *   At $x=0$, $f'(x)$ does not change sign (it is positive on both sides). Therefore, at $x=0$ **there is no local extremum** (it is an inflection point).

**Conclusion:**
*   **Intervals of monotonicity:**
    *   Strictly decreasing on $(-\infty, -3]$.
    *   Strictly increasing on $[-3, \infty)$.
*   **Local extrema:**
    *   Local minimum at the point $(-3, -54e^{-3})$.

# 8. (1 point) Compute the integral $I_1 = \int_0^2 x^2(4x + \frac{1}{x^2}) dx$.

**Solution:**

1.  **We simplify the integrand:**
    $x^2(4x + \frac{1}{x^2}) = x^2 \cdot 4x + x^2 \cdot \frac{1}{x^2} = 4x^3 + 1$

2.  **We substitute the simplified expression into the integral:**
    $I_1 = \int_0^2 (4x^3 + 1) dx$

3.  **We compute the indefinite integral:**
    $\int (4x^3 + 1) dx = \int 4x^3 dx + \int 1 dx = 4 \frac{x^{3+1}}{3+1} + x = 4 \frac{x^4}{4} + x = x^4 + x$

4.  **We apply the Fundamental Theorem of Calculus to compute the definite integral:**
    $I_1 = [x^4 + x]_0^2 = (2^4 + 2) - (0^4 + 0)$
    $I_1 = (16 + 2) - 0 = 18$

**The result is $I_1 = 18$.**

# 9. (1 point) Find the linear approximation of $f(x) = \ln(2x+1)$ for $x$ near $a=0$. Use the linear approximation to compute the value $\ln(1.2) \approx f(0.1)$.

**Solution:**

1.  **We find the form of the linear approximation (or linearization) $L(x)$:**
    The linear approximation of a function $f(x)$ near $x=a$ is given by the formula:
    $L(x) = f(a) + f'(a)(x-a)$

2.  **We compute $f(a)$ and $f'(a)$ for $a=0$:**
    *   $f(x) = \ln(2x+1) \implies f(0) = \ln(2(0)+1) = \ln(1) = 0$.
    *   For the derivative, we use the chain rule:
        $f'(x) = \frac{1}{2x+1} \cdot (2x+1)' = \frac{2}{2x+1}$.
    *   $f'(0) = \frac{2}{2(0)+1} = \frac{2}{1} = 2$.

3.  **We substitute the values into the linearization formula:**
    $L(x) = 0 + 2(x-0) = 2x$.
    Therefore, the linear approximation of $f(x)$ near $a=0$ is $L(x) = 2x$.
    This means that for $x$ near 0, $\ln(2x+1) \approx 2x$.

4.  **We use the approximation to compute $\ln(1.2)$:**
    We want to find the $x$ for which $2x+1 = 1.2$.
    $2x = 1.2 - 1 \implies 2x = 0.2 \implies x = 0.1$.
    Since $x=0.1$ is near $a=0$, we can use the approximation:
    $\ln(1.2) = f(0.1) \approx L(0.1)$
    $L(0.1) = 2(0.1) = 0.2$.

**The linear approximation is $L(x) = 2x$ and the approximate value is $\ln(1.2) \approx 0.2$.**

# 10. (0.5 points) Compute the limit $\lim_{x \to 2} \frac{x^2-3x+2}{x-2}$.

**Solution:**

1.  **We attempt direct substitution of $x=2$:**
    $\frac{2^2 - 3(2) + 2}{2-2} = \frac{4 - 6 + 2}{0} = \frac{0}{0}$.
    We have the indeterminate form $\frac{0}{0}$, so we must simplify the expression.

2.  **Method 1: Factorization**
    *   We factor the trinomial in the numerator: $x^2 - 3x + 2$. We look for two numbers with sum -3 and product 2. These are -1 and -2.
    *   Therefore, $x^2 - 3x + 2 = (x-1)(x-2)$.
    *   We substitute into the limit:
        $\lim_{x \to 2} \frac{(x-1)(x-2)}{x-2}$
    *   For $x \neq 2$, we can cancel the factor $(x-2)$:
        $\lim_{x \to 2} (x-1)$
    *   Now we substitute:
        $2 - 1 = 1$.

3.  **Method 2: L'Hôpital's Rule**
    *   Since we have the form $\frac{0}{0}$, we can differentiate numerator and denominator:
        $\lim_{x \to 2} \frac{(x^2-3x+2)'}{(x-2)'} = \lim_{x \to 2} \frac{2x-3}{1}$
    *   We substitute $x=2$:
        $\frac{2(2)-3}{1} = \frac{4-3}{1} = 1$.

**The limit is 1.**

# 11. (0.5 points) What commands must be given to Octave to compute the derivative of $f(x) = e^x \cos(x^2)$?

**Solution:**

To perform symbolic computations (such as differentiation) in Octave, we must first load the symbolic computation package (`symbolic`).

1.  **Loading the `symbolic` package:**
    ```octave
    pkg load symbolic
    ```

2.  **Declaring the symbolic variable `x`:**
    ```octave
    syms x
    ```

3.  **Defining the function `f(x)`:**
    ```octave
    f = exp(x) * cos(x^2)
    ```

4.  **Computing the derivative using the `diff` command:**
    ```octave
    df = diff(f, x)
    ```

**The commands in Octave are:**
```octave
pkg load symbolic
syms x
f = exp(x) * cos(x^2);
df = diff(f, x)
```