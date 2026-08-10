$$
\textbf{Group A}
$$
\textbf{PROBLEM 1}
The function is given:
$$
f(x)=\begin{cases}sin(\pi x)+ae^{x-2},&x\le2\\ \frac{x^{3}-x^{2}-2x}{x^{2}-4},&x>2\end{cases}
$$
For which values of $a$ is $f$ continuous on $\mathbb{R}$?

**Solution**

For the function $f$ to be continuous on $\mathbb{R}$, it must be continuous at every point of its domain. The two branches of the function are continuous on their respective intervals. The only point we need to examine is $x=2$.

For $f$ to be continuous at $x=2$, the following must hold:
$$
\lim_{x\to2^{-}}f(x) = \lim_{x\to2^{+}}f(x) = f(2)
$$

1.  **Computing $f(2)$ and the left-hand limit:**
    $$
    f(2) = \sin(2\pi) + ae^{2-2} = 0 + a \cdot e^0 = a
    $$
    $$
    \lim_{x\to2^{-}}f(x) = \lim_{x\to2^{-}}(\sin(\pi x)+ae^{x-2}) = \sin(2\pi) + ae^{2-2} = a
    $$

2.  **Computing the right-hand limit:**
    $$
    \lim_{x\to2^{+}}f(x) = \lim_{x\to2^{+}}\frac{x^{3}-x^{2}-2x}{x^{2}-4}
    $$
    Substituting $x=2$ yields the indeterminate form $\frac{0}{0}$. Therefore, we factor the numerator and the denominator:
    *   $x^{3}-x^{2}-2x = x(x^{2}-x-2) = x(x-2)(x+1)$
    *   $x^{2}-4 = (x-2)(x+2)$

    The limit becomes:
    $$
    \lim_{x\to2^{+}}\frac{x(x-2)(x+1)}{(x-2)(x+2)} = \lim_{x\to2^{+}}\frac{x(x+1)}{x+2} = \frac{2(2+1)}{2+2} = \frac{6}{4} = \frac{3}{2}
    $$

3.  **Equating the limits:**
    For the function to be continuous, the limits must be equal:
    $$
    a = \frac{3}{2}
    $$

Therefore, $f$ is continuous on $\mathbb{R}$ for $a = \frac{3}{2}$.

---
$$
\textbf{PROBLEM 2}
$$
What commands must be given to Octave in order to find the roots of the equation:
$$
x^{4}-8x^{3}-70x=19.
$$
**Solution**

1.  **Converting the equation:**
    First, we bring the equation to the polynomial form $p(x)=0$:
    $$
    x^{4}-8x^{3}+0x^{2}-70x-19 = 0
    $$

2.  **Creating the coefficient vector:**
    In Octave, a polynomial is represented by a vector containing its coefficients, starting from the highest power. The coefficients are: $1, -8, 0, -70, -19$.
    ```octave
    p = [1, -8, 0, -70, -19];
    ```

3.  **Finding the roots:**
    We use the built-in function `roots()` to compute the roots of the polynomial.
    ```octave
    roots(p)
    ```

In summary, the commands in Octave are:
```octave
% Definition of the polynomial coefficient vector
p = [1, -8, 0, -70, -19];

% Finding the roots using the roots() function
roots(p)
```
---
$$
\textbf{PROBLEM 3}
$$
Compute the limit:
$$
\lim_{x\to-\infty}(\frac{2x^{4}+x-1}{4x^{3}-x^{2}+2})
$$
**Solution**

To compute the limit of a rational function as $x$ tends to $\pm\infty$, we keep only the terms with the highest power of $x$ in the numerator and the denominator.

1.  **Rule of highest-degree terms:**
    $$
    \lim_{x\to-\infty}\frac{2x^{4}+x-1}{4x^{3}-x^{2}+2} = \lim_{x\to-\infty}\frac{2x^{4}}{4x^{3}}
    $$

2.  **Simplification:**
    $$
    \lim_{x\to-\infty}\frac{2x^{4}}{4x^{3}} = \lim_{x\to-\infty}\frac{x}{2}
    $$

3.  **Computing the limit:**
    As $x$ tends to $-\infty$, the expression $\frac{x}{2}$ also tends to $-\infty$.
    $$
    \lim_{x\to-\infty}\frac{x}{2} = -\infty
    $$

Therefore, the limit is $-\infty$.

---
$$
\textbf{PROBLEM 4}
$$
Find all vertical asymptotes of the function:
$$
f(x)=\frac{1}{(x+2)(x-4)}
$$
**Solution**

The vertical asymptotes of a rational function are found at the values of $x$ that make the denominator zero but not the numerator.

1.  **Finding the roots of the denominator:**
    We set the denominator equal to zero:
    $$
    (x+2)(x-4) = 0
    $$
    The roots are $x = -2$ and $x = 4$.

2.  **Checking the numerator:**
    The numerator is 1, which is constant and non-zero. Therefore, the values $x=-2$ and $x=4$ are candidates for vertical asymptotes.

3.  **Computing the one-sided limits:**
    We check the limits of $f(x)$ as $x$ approaches these values:
    *   For $x=-2$: $\lim_{x\to-2}\frac{1}{(x+2)(x-4)} = \frac{1}{0 \cdot (-6)} = \infty$.
    *   For $x=4$: $\lim_{x\to4}\frac{1}{(x+2)(x-4)} = \frac{1}{6 \cdot 0} = \infty$.

Since the limits tend to infinity, the lines $x=-2$ and $x=4$ are the vertical asymptotes of the function.

---
$$
\textbf{PROBLEM 5}
$$
Compute the derivatives of the functions:
$$
f(x)=\frac{x^{2}-2}{x+1}
$$
$$
h(x)=(3x^{2}+e^{x})\ln(3x)
$$
**Solution**

**For the function $f(x)$:**
We use the quotient rule for differentiation $(\frac{u}{v})' = \frac{u'v - uv'}{v^2}$, where $u(x) = x^2-2$ and $v(x) = x+1$.
*   $u'(x) = 2x$
*   $v'(x) = 1$

$$
f'(x) = \frac{(2x)(x+1) - (x^2-2)(1)}{(x+1)^2} = \frac{2x^2+2x - x^2+2}{(x+1)^2} = \frac{x^2+2x+2}{(x+1)^2}
$$

**For the function $h(x)$:**
We use the product rule for differentiation $(uv)' = u'v + uv'$, where $u(x) = 3x^2+e^x$ and $v(x) = \ln(3x)$.
*   $u'(x) = 6x+e^x$
*   $v'(x) = \frac{1}{3x} \cdot (3x)' = \frac{1}{3x} \cdot 3 = \frac{1}{x}$ (using the chain rule)

$$
h'(x) = (6x+e^x)\ln(3x) + (3x^2+e^x)\frac{1}{x} = (6x+e^x)\ln(3x) + 3x + \frac{e^x}{x}
$$
---
$$
\textbf{PROBLEM 6}
$$
The function $y(x)$ is defined by the equality:
$$
x^{3}y^{5}+3x=8y^{3}+1
$$
Find the equation of the tangent line to the graph of $y(x)$ at the point $(0,-\frac{1}{2})$.
**Solution**

1.  **Implicit differentiation:**
    We differentiate both sides of the equation with respect to $x$, treating $y$ as a function of $x$ ($y(x)$).
    $$
    \frac{d}{dx}(x^3y^5+3x) = \frac{d}{dx}(8y^3+1)
    $$
    $$
    (3x^2 \cdot y^5 + x^3 \cdot 5y^4 \frac{dy}{dx}) + 3 = 24y^2 \frac{dy}{dx} + 0
    $$

2.  **Solving for $\frac{dy}{dx}$:**
    $$
    3x^2y^5 + 3 = 24y^2 \frac{dy}{dx} - 5x^3y^4 \frac{dy}{dx}
    $$
    $$
    3x^2y^5 + 3 = (24y^2 - 5x^3y^4) \frac{dy}{dx}
    $$
    $$
    \frac{dy}{dx} = \frac{3x^2y^5 + 3}{24y^2 - 5x^3y^4}
    $$

3.  **Computing the slope at the point $(0, -\frac{1}{2})$:**
    We substitute $x=0$ and $y=-\frac{1}{2}$ into the derivative expression to find the slope $m$ of the tangent.
    $$
    m = \frac{3(0)^2(-\frac{1}{2})^5 + 3}{24(-\frac{1}{2})^2 - 5(0)^3(-\frac{1}{2})^4} = \frac{0+3}{24(\frac{1}{4}) - 0} = \frac{3}{6} = \frac{1}{2}
    $$

4.  **Equation of the tangent:**
    We use the line equation form $y - y_0 = m(x - x_0)$ with $(x_0, y_0) = (0, -\frac{1}{2})$ and $m = \frac{1}{2}$.
    $$
    y - (-\frac{1}{2}) = \frac{1}{2}(x - 0)
    $$
    $$
    y + \frac{1}{2} = \frac{1}{2}x
    $$
    $$
    y = \frac{1}{2}x - \frac{1}{2}
    $$
---
$$
\textbf{PROBLEM 7}
$$
What commands must be given to Octave in order to plot the function $y=3\sin(2x)$ on the interval $[-\frac{\pi}{2},2\pi]$;

**Solution**

1.  **Defining the x interval:**
    We create a vector of values for $x$ from $-\frac{\pi}{2}$ to $2\pi$. We use the `linspace` function to obtain a large number of points (e.g., 200) for a smooth curve.
    ```octave
    x = linspace(-pi/2, 2*pi, 200);
    ```

2.  **Computing the y values:**
    We compute the corresponding $y$ values for each $x$.
    ```octave
    y = 3 * sin(2*x);
    ```

3.  **Plotting the graph:**
    We use the `plot` function to plot $y$ against $x$.
    ```octave
    plot(x, y);
    ```

4.  **Adding labels and title (optional):**
    For a more complete graph, we can add axis labels and a title.
    ```octave
    xlabel('x');
    ylabel('y');
    title('Graph of y = 3sin(2x)');
    grid on;
    ```

In summary, the basic commands in Octave are:
```octave
% Definition of the x vector
x = linspace(-pi/2, 2*pi, 200);

% Computation of y
y = 3 * sin(2*x);

% Plotting
plot(x, y);
title('Graph of y = 3sin(2x)');
xlabel('x');
ylabel('y');
grid on;
```

$$
\textbf{Group B}
$$
$$\textbf{PROBLEM 1}$$
Compute the derivatives of the functions:
$$
f(x)=\frac{x+2}{x^{2}-1}
$$
$$
h(x)=(5x^{4}+\sin(3x))\ln(x)
$$
**Solution**

**For the function $f(x)$:**
We use the quotient rule for differentiation $(\frac{u}{v})' = \frac{u'v - uv'}{v^2}$, where $u(x) = x+2$ and $v(x) = x^2-1$.
*   $u'(x) = 1$
*   $v'(x) = 2x$

$$
f'(x) = \frac{(1)(x^2-1) - (x+2)(2x)}{(x^2-1)^2} = \frac{x^2-1 - (2x^2+4x)}{(x^2-1)^2} = \frac{-x^2-4x-1}{(x^2-1)^2}
$$

**For the function $h(x)$:**
We use the product rule for differentiation $(uv)' = u'v + uv'$, where $u(x) = 5x^4+\sin(3x)$ and $v(x) = \ln(x)$.
*   $u'(x) = 20x^3 + \cos(3x) \cdot 3 = 20x^3 + 3\cos(3x)$ (using the chain rule)
*   $v'(x) = \frac{1}{x}$

$$
h'(x) = (20x^3 + 3\cos(3x))\ln(x) + (5x^4+\sin(3x))\frac{1}{x} = (20x^3 + 3\cos(3x))\ln(x) + 5x^3 + \frac{\sin(3x)}{x}
$$
---
$$
\textbf{PROBLEM 2}
$$
The function $y(x)$ is defined by the equality:
$$
x^{5}y^{3}+3x=8y^{3}-1
$$
Find the equation of the tangent line to the graph of $y(x)$ at the point $(0,\frac{1}{2})$.
**Solution**

1.  **Implicit differentiation:**
    We differentiate both sides of the equation with respect to $x$.
    $$
    \frac{d}{dx}(x^5y^3+3x) = \frac{d}{dx}(8y^3-1)
    $$
    $$
    (5x^4 \cdot y^3 + x^5 \cdot 3y^2 \frac{dy}{dx}) + 3 = 24y^2 \frac{dy}{dx} - 0
    $$

2.  **Solving for $\frac{dy}{dx}$:**
    $$
    5x^4y^3 + 3 = 24y^2 \frac{dy}{dx} - 3x^5y^2 \frac{dy}{dx}
    $$
    $$
    5x^4y^3 + 3 = (24y^2 - 3x^5y^2) \frac{dy}{dx}
    $$
    $$
    \frac{dy}{dx} = \frac{5x^4y^3 + 3}{24y^2 - 3x^5y^2}
    $$

3.  **Computing the slope at the point $(0, \frac{1}{2})$:**
    We substitute $x=0$ and $y=\frac{1}{2}$ to find the slope $m$.
    $$
    m = \frac{5(0)^4(\frac{1}{2})^3 + 3}{24(\frac{1}{2})^2 - 3(0)^5(\frac{1}{2})^2} = \frac{0+3}{24(\frac{1}{4}) - 0} = \frac{3}{6} = \frac{1}{2}
    $$

4.  **Equation of the tangent:**
    We use the form $y - y_0 = m(x - x_0)$ with $(x_0, y_0) = (0, \frac{1}{2})$ and $m = \frac{1}{2}$.
    $$
    y - \frac{1}{2} = \frac{1}{2}(x - 0)
    $$
    $$
    y = \frac{1}{2}x + \frac{1}{2}
    $$
---
$$
\textbf{PROBLEM 3}
$$
The function is given:
$$
f(x)=\begin{cases}ae^{x-1}+\sin(\pi x),&x\le1\\ \frac{x^{3}+2x^{2}-3x}{x^{2}-1},&x>1\end{cases}
$$
Find the real number $a$ such that $f$ is continuous on its domain.
**Solution**

For $f$ to be continuous, it must be continuous at the point $x=1$. Therefore, we need $\lim_{x\to1^{-}}f(x) = \lim_{x\to1^{+}}f(x) = f(1)$.

1.  **Computing $f(1)$ and the left-hand limit:**
    $$
    f(1) = ae^{1-1} + \sin(\pi \cdot 1) = a \cdot e^0 + 0 = a
    $$
    $$
    \lim_{x\to1^{-}}f(x) = \lim_{x\to1^{-}}(ae^{x-1}+\sin(\pi x)) = a
    $$

2.  **Computing the right-hand limit:**
    $$
    \lim_{x\to1^{+}}f(x) = \lim_{x\to1^{+}}\frac{x^{3}+2x^{2}-3x}{x^{2}-1}
    $$
    Substituting $x=1$ yields the indeterminate form $\frac{0}{0}$. We factor:
    *   $x^{3}+2x^{2}-3x = x(x^2+2x-3) = x(x-1)(x+3)$
    *   $x^{2}-1 = (x-1)(x+1)$

    The limit becomes:
    $$
    \lim_{x\to1^{+}}\frac{x(x-1)(x+3)}{(x-1)(x+1)} = \lim_{x\to1^{+}}\frac{x(x+3)}{x+1} = \frac{1(1+3)}{1+1} = \frac{4}{2} = 2
    $$

3.  **Equating the limits:**
    $$
    a = 2
    $$

Therefore, $f$ is continuous for $a = 2$.

---
$$
\textbf{PROBLEM 4}
$$
What commands must be given to Octave in order to plot the function $y=2\cos(2x)$ on the interval $[-\pi, \pi]$;
**Solution**

The commands in Octave for plotting the graph are as follows:
```octave
% 1. Definition of the value interval for x
x = linspace(-pi, pi, 200);

% 2. Computation of the corresponding y values
y = 2 * cos(2*x);

% 3. Plotting the graph
plot(x, y);

% 4. Adding title and labels (optional)
title('Graph of y = 2cos(2x)');
xlabel('x');
ylabel('y');
grid on;
```
---
$$
\textbf{PROBLEM 5}
$$
What commands must be given to Octave in order to find the roots of the equation:
$$
x^{5}-8x^{4}-70x^{2}+6x=19
$$
**Solution**

1.  **Converting the equation:**
    We bring the equation to the polynomial form $p(x)=0$:
    $$
    x^{5}-8x^{4}+0x^3-70x^{2}+6x-19 = 0
    $$

2.  **Creating the coefficient vector:**
    The coefficients of the polynomial are: $1, -8, 0, -70, 6, -19$.
    ```octave
    p = [1, -8, 0, -70, 6, -19];
    ```

3.  **Finding the roots:**
    We use the `roots()` function.
    ```octave
    roots(p)
    ```

In summary, the commands in Octave are:
```octave
p = [1, -8, 0, -70, 6, -19];
roots(p)
```
---
$$
\textbf{PROBLEM 6}
$$
Compute the limit:
$$
\lim_{x\to-\infty}(\frac{3x^{4}+x^{3}-2}{2x^{3}+x^{2}-10x})
$$
**Solution**

We use the rule of highest-degree terms for limits of rational functions at infinity.

1.  **Rule of highest-degree terms:**
    $$
    \lim_{x\to-\infty}\frac{3x^{4}+x^{3}-2}{2x^{3}+x^{2}-10x} = \lim_{x\to-\infty}\frac{3x^{4}}{2x^{3}}
    $$

2.  **Simplification:**
    $$
    \lim_{x\to-\infty}\frac{3x}{2}
    $$

3.  **Computing the limit:**
    As $x \to -\infty$, the expression $\frac{3x}{2}$ also tends to $-\infty$.
    $$
    \lim_{x\to-\infty}\frac{3x}{2} = -\infty
    $$
---
$$
\textbf{PROBLEM 7}
$$
Find all vertical asymptotes of the function:
$$
f(x)=\frac{1}{(x-5)(x+4)}
$$
**Solution**

The vertical asymptotes are found at the roots of the denominator that are not roots of the numerator.

1.  **Finding the roots of the denominator:**
    $$
    (x-5)(x+4) = 0
    $$
    The roots are $x = 5$ and $x = -4$.

2.  **Checking the numerator:**
    The numerator is 1, so the roots of the denominator lead to vertical asymptotes.

3.  **Conclusion:**
    The vertical asymptotes of the function are the lines $x=5$ and $x=-4$.

$$
\textbf{Group C}
$$
$$
\textbf{PROBLEM 1}
$$
What commands must be given to Octave in order to plot the function $y=2\sin(2x)$ on the interval $[-\pi, \pi]$;
**Solution**

The commands in Octave are:
```octave
% Definition of the x vector
x = linspace(-pi, pi, 200);

% Computation of y
y = 2 * sin(2*x);

% Plotting
plot(x, y);
title('Graph of y = 2sin(2x)');
xlabel('x');
ylabel('y');
grid on;
```
---
$$
\textbf{PROBLEM 2}
$$
Compute the derivatives of the functions:
$$
f(x)=\frac{x^{3}-1}{x+1}
$$
$$
h(x)=(2x^{5}+e^{2x})\ln(x)
$$
**Solution**

**For the function $f(x)$:**
We use the quotient rule $(\frac{u}{v})' = \frac{u'v - uv'}{v^2}$ with $u=x^3-1$ and $v=x+1$.
*   $u' = 3x^2$
*   $v' = 1$

$$
f'(x) = \frac{(3x^2)(x+1) - (x^3-1)(1)}{(x+1)^2} = \frac{3x^3+3x^2 - x^3+1}{(x+1)^2} = \frac{2x^3+3x^2+1}{(x+1)^2}
$$

**For the function $h(x)$:**
We use the product rule $(uv)' = u'v + uv'$ with $u=2x^5+e^{2x}$ and $v=\ln(x)$.
*   $u' = 10x^4 + e^{2x} \cdot 2 = 10x^4 + 2e^{2x}$
*   $v' = \frac{1}{x}$

$$
h'(x) = (10x^4 + 2e^{2x})\ln(x) + (2x^5+e^{2x})\frac{1}{x} = (10x^4 + 2e^{2x})\ln(x) + 2x^4 + \frac{e^{2x}}{x}
$$
---
$$
\textbf{PROBLEM 3}
$$
The function $y(x)$ is defined by the equality:
$$
x^{2}y=y^{2}-6x
$$
Find the equation of the tangent line to the graph of $y(x)$ at the point $(2, 6)$.
**Solution**

1.  **Implicit differentiation:**
    $$
    \frac{d}{dx}(x^2y) = \frac{d}{dx}(y^2-6x)
    $$
    $$
    2xy + x^2 \frac{dy}{dx} = 2y \frac{dy}{dx} - 6
    $$

2.  **Solving for $\frac{dy}{dx}$:**
    $$
    2xy + 6 = 2y \frac{dy}{dx} - x^2 \frac{dy}{dx}
    $$
    $$
    2xy + 6 = (2y - x^2) \frac{dy}{dx}
    $$
    $$
    \frac{dy}{dx} = \frac{2xy + 6}{2y - x^2}
    $$

3.  **Computing the slope at the point $(2, 6)$:**
    $$
    m = \frac{2(2)(6) + 6}{2(6) - (2)^2} = \frac{24+6}{12-4} = \frac{30}{8} = \frac{15}{4}
    $$

4.  **Equation of the tangent:**
    $$
    y - 6 = \frac{15}{4}(x - 2)
    $$
    $$
    y = \frac{15}{4}x - \frac{30}{4} + 6 = \frac{15}{4}x - \frac{15}{2} + \frac{12}{2}
    $$
    $$
    y = \frac{15}{4}x - \frac{3}{2}
    $$
---
$$
\textbf{PROBLEM 4}
$$
What commands must be given to Octave in order to find the roots of the equation:
$$
7x^{5}-x^{4}+2x^{3}+5x=15
$$
**Solution**

1.  **Converting the equation:**
    $$
    7x^{5}-x^{4}+2x^{3}+0x^2+5x-15 = 0
    $$

2.  **Octave commands:**
    ```octave
    p = [7, -1, 2, 0, 5, -15];
    roots(p)
    ```
---
$$
\textbf{PROBLEM 5}
$$
Compute the limit:
$$
\lim_{x\to-\infty}(\frac{2x^{3}+x-1}{4x^{4}-x^{2}+2})
$$
**Solution**

We use the rule of highest-degree terms.
$$
\lim_{x\to-\infty}\frac{2x^{3}+x-1}{4x^{4}-x^{2}+2} = \lim_{x\to-\infty}\frac{2x^{3}}{4x^{4}} = \lim_{x\to-\infty}\frac{1}{2x}
$$
As $x \to -\infty$, the denominator $2x$ tends to $-\infty$, so the fraction $\frac{1}{2x}$ tends to 0.
$$
\lim_{x\to-\infty}\frac{1}{2x} = 0
$$
---
$$
\textbf{PROBLEM 6}
$$
Find all vertical asymptotes of the function:
$$
f(x)=\frac{1}{(x-2)(x+4)}
$$
**Solution**

The vertical asymptotes are found at the roots of the denominator.
$$
(x-2)(x+4) = 0 \implies x=2 \text{ and } x=-4
$$
The numerator is 1, so the lines $x=2$ and $x=-4$ are the vertical asymptotes.

---
$$
\textbf{PROBLEM 7}
$$
The function is given:
$$
f(x)=\begin{cases}e^{x-2}+a\cos(\pi x),&x\le2\\ \frac{x^{3}-x^{2}-6x}{x^{2}-4},&x>2\end{cases}
$$
For which values of $a$ is $f$ continuous on $\mathbb{R}$;
**Solution**

We examine the continuity at $x=2$. We need $\lim_{x\to2^{-}}f(x) = \lim_{x\to2^{+}}f(x) = f(2)$.

1.  **Left-hand limit and $f(2)$:**
    $$
    f(2) = e^{2-2} + a\cos(2\pi) = e^0 + a(1) = 1+a
    $$
    $$
    \lim_{x\to2^{-}}f(x) = 1+a
    $$

2.  **Right-hand limit:**
    $$
    \lim_{x\to2^{+}}\frac{x^{3}-x^{2}-6x}{x^{2}-4} \quad (\text{form } \frac{0}{0})
    $$
    We factor:
    *   $x^3-x^2-6x = x(x^2-x-6) = x(x-3)(x+2)$
    *   $x^2-4 = (x-2)(x+2)$
    The limit becomes:
    $$
    \lim_{x\to2^{+}}\frac{x(x-3)(x+2)}{(x-2)(x+2)} = \lim_{x\to2^{+}}\frac{x(x-3)}{x-2}
    $$
    As $x \to 2^+$, the numerator tends to $2(2-3)=-2$ and the denominator tends to $0^+$. Therefore, the limit is $-\infty$.

3.  **Conclusion:**
    Since the right-hand limit is $-\infty$ and the left-hand limit is $1+a$, there is no value of $a$ for which the limits are equal. Therefore, the function cannot be continuous at $x=2$ for any value of $a$.

$$
\textbf{Group D}
$$
\textbf{PROBLEM 1}
Compute the limit:
$$
\lim_{x\to-\infty}(\frac{3x^{3}+x^{2}-2}{2x^{4}+x^{2}-10x})
$$
**Solution**

We use the rule of highest-degree terms.
$$
\lim_{x\to-\infty}\frac{3x^{3}}{2x^{4}} = \lim_{x\to-\infty}\frac{3}{2x}
$$
As $x \to -\infty$, the denominator $2x \to -\infty$, so the limit is 0.
$$
\lim_{x\to-\infty}\frac{3}{2x} = 0
$$
---
$$
\textbf{PROBLEM 2}
$$
What commands must be given to Octave in order to find the roots of the equation:
$$
2x^{5}-3x^{4}+2x^{2}+8x=11
$$
**Solution**

1.  **Converting the equation:**
    $$
    2x^{5}-3x^{4}+0x^3+2x^{2}+8x-11 = 0
    $$

2.  **Octave commands:**
    ```octave
    p = [2, -3, 0, 2, 8, -11];
    roots(p)
    ```
---
$$
\textbf{PROBLEM 3}
$$
Find all vertical asymptotes of the function:
$$
f(x)=\frac{2}{(x+5)(x-4)}
$$
**Solution**

The vertical asymptotes are found at the roots of the denominator.
$$
(x+5)(x-4) = 0 \implies x=-5 \text{ and } x=4
$$
The numerator is 2, so the lines $x=-5$ and $x=4$ are the vertical asymptotes.

---
$$
\textbf{PROBLEM 4}
$$
What commands must be given to Octave in order to plot the function $y=3\cos(2x)$ on the interval $[-\frac{\pi}{2},2\pi]$;
**Solution**

```octave
x = linspace(-pi/2, 2*pi, 200);
y = 3 * cos(2*x);
plot(x, y);
title('Graph of y = 3cos(2x)');
xlabel('x');
ylabel('y');
grid on;
```
---
$$
\textbf{PROBLEM 5}
$$
The function is given:
$$
f(x)=\begin{cases}e^{1-x}-a\cos(2\pi x),&x\le1\\ \frac{x^{3}-3x^{2}+2x}{x^{2}-1},&x>1\end{cases}
$$
Find the real number $a$ such that $f$ is continuous on its domain.
**Solution**

We examine the continuity at $x=1$. We need $\lim_{x\to1^{-}}f(x) = \lim_{x\to1^{+}}f(x) = f(1)$.

1.  **Left-hand limit and $f(1)$:**
    $$
    f(1) = e^{1-1} - a\cos(2\pi) = e^0 - a(1) = 1-a
    $$
    $$
    \lim_{x\to1^{-}}f(x) = 1-a
    $$

2.  **Right-hand limit:**
    $$
    \lim_{x\to1^{+}}\frac{x^{3}-3x^{2}+2x}{x^{2}-1} \quad (\text{form } \frac{0}{0})
    $$
    We factor:
    *   $x^3-3x^2+2x = x(x^2-3x+2) = x(x-1)(x-2)$
    *   $x^2-1 = (x-1)(x+1)$
    The limit becomes:
    $$
    \lim_{x\to1^{+}}\frac{x(x-1)(x-2)}{(x-1)(x+1)} = \lim_{x\to1^{+}}\frac{x(x-2)}{x+1} = \frac{1(1-2)}{1+1} = \frac{-1}{2}
    $$

3.  **Equating the limits:**
    $$
    1-a = -\frac{1}{2} \implies a = 1 + \frac{1}{2} = \frac{3}{2}
    $$
For $a = \frac{3}{2}$, the function is continuous.

---
$$
\textbf{PROBLEM 6}
$$
The function $y(x)$ is defined by the equality:
$$
x^{2}y-6x=-y^{2}
$$
Find the equation of the tangent line to the graph of $y(x)$ at the point $(2,-6)$.
**Solution**

The equation is $x^2y+y^2-6x=0$.
1.  **Implicit differentiation:**
    $$
    \frac{d}{dx}(x^2y+y^2-6x) = \frac{d}{dx}(0)
    $$
    $$
    (2xy + x^2 \frac{dy}{dx}) + 2y \frac{dy}{dx} - 6 = 0
    $$

2.  **Solving for $\frac{dy}{dx}$:**
    $$
    (x^2 + 2y)\frac{dy}{dx} = 6 - 2xy
    $$
    $$
    \frac{dy}{dx} = \frac{6 - 2xy}{x^2 + 2y}
    $$

3.  **Computing the slope at the point $(2, -6)$:**
    $$
    m = \frac{6 - 2(2)(-6)}{(2)^2 + 2(-6)} = \frac{6 + 24}{4 - 12} = \frac{30}{-8} = -\frac{15}{4}
    $$

4.  **Equation of the tangent:**
    $$
    y - (-6) = -\frac{15}{4}(x - 2)
    $$
    $$
    y + 6 = -\frac{15}{4}x + \frac{30}{4}
    $$
    $$
    y = -\frac{15}{4}x + \frac{15}{2} - 6 = -\frac{15}{4}x + \frac{15-12}{2}
    $$
    $$
    y = -\frac{15}{4}x + \frac{3}{2}
    $$
---
$$
\textbf{PROBLEM 7}
$$
Compute the derivatives of the functions:
$$
f(x)=\frac{x+1}{x^{2}+2}
$$
$$
h(x)=(3x^{3}-\cos x)\ln(5x)
$$
**Solution**

**For the function $f(x)$:**
We use the quotient rule $(\frac{u}{v})' = \frac{u'v - uv'}{v^2}$ with $u=x+1$ and $v=x^2+2$.
*   $u' = 1$
*   $v' = 2x$

$$
f'(x) = \frac{(1)(x^2+2) - (x+1)(2x)}{(x^2+2)^2} = \frac{x^2+2 - 2x^2-2x}{(x^2+2)^2} = \frac{-x^2-2x+2}{(x^2+2)^2}
$$

**For the function $h(x)$:**
We use the product rule $(uv)' = u'v + uv'$ with $u=3x^3-\cos x$ and $v=\ln(5x)$.
*   $u' = 9x^2 - (-\sin x) = 9x^2 + \sin x$
*   $v' = \frac{1}{5x} \cdot 5 = \frac{1}{x}$

$$
h'(x) = (9x^2 + \sin x)\ln(5x) + (3x^3-\cos x)\frac{1}{x} = (9x^2 + \sin x)\ln(5x) + 3x^2 - \frac{\cos x}{x}
$$