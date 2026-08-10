# Differentiation Rules

A concise guide to the basic rules of differentiation for real-valued functions, including the sum, product, quotient, and power rules.

---

## 1. Fundamental Differentiation Rules

These rules allow us to compute the derivative of composite expressions without using the limit definition.

### Basic Rules
1. **Constant Rule:**
   $$
   \frac{d}{dx}[c] = 0
   $$
2. **Constant Multiple Rule:**
   $$
   \frac{d}{dx}[c f(x)] = c f'(x)
   $$
3. **Sum Rule:**
   $$
   \frac{d}{dx}[f(x) + g(x)] = f'(x) + g'(x)
   $$
4. **Difference Rule:**
   $$
   \frac{d}{dx}[f(x) - g(x)] = f'(x) - g'(x)
   $$

---

## 2. Product and Quotient Rules

### Product Rule
The derivative of the product of two functions equals the derivative of the first times the second, plus the first times the derivative of the second:
$$
\frac{d}{dx}[f(x)g(x)] = f'(x)g(x) + f(x)g'(x)
$$

### Quotient Rule
The derivative of the quotient of two functions is computed as:
$$
\frac{d}{dx}\left[\frac{f(x)}{g(x)}\right] = \frac{f'(x)g(x) - f(x)g'(x)}{[g(x)]^2}
$$
for every $x$ where $g(x) \neq 0$.

### Power Rule
For any real number $n$:
$$
\frac{d}{dx}[x^n] = n x^{n-1}
$$

---

## Solved Exercises

### Exercise 1: Derivative of a Polynomial Function
**Problem:**
Find the derivative of the function:
$$
f(x) = 5x^4 - 3x^2 + 7
$$

**Solution:**
1. Apply the sum/difference and constant multiple rules:
   $$
   f'(x) = 5 \cdot \frac{d}{dx}[x^4] - 3 \cdot \frac{d}{dx}[x^2] + \frac{d}{dx}[7]
   $$
2. Apply the power and constant rules:
   $$
   f'(x) = 5(4x^3) - 3(2x) + 0
   $$
3. Simplify:
   $$
   f'(x) = 20x^3 - 6x
   $$

### Exercise 2: Application of the Product Rule
**Problem:**
Differentiate the function:
$$
f(x) = x^2 \cos(x)
$$

**Solution:**
1. Apply the product rule:
   $$
   f'(x) = \frac{d}{dx}[x^2] \cdot \cos(x) + x^2 \cdot \frac{d}{dx}[\cos(x)]
   $$
2. Compute the individual derivatives (recall that $(\cos(x))' = -\sin(x)$):
   $$
   f'(x) = 2x \cos(x) + x^2(-\sin(x))
   $$
3. Simplify the result:
   $$
   f'(x) = 2x \cos(x) - x^2 \sin(x)
   $$

### Exercise 3: Application of the Quotient Rule
**Problem:**
Differentiate the function:
$$
f(x) = \frac{x^2 + 1}{x - 3}
$$

**Solution:**
1. Apply the quotient rule:
   $$
   f'(x) = \frac{(x^2 + 1)'(x - 3) - (x^2 + 1)(x - 3)'}{(x - 3)^2}
   $$
2. Compute the derivatives of the numerator and denominator:
   $$
   (x^2 + 1)' = 2x, \quad (x - 3)' = 1
   $$
3. Substitute into the formula:
   $$
   f'(x) = \frac{2x(x - 3) - (x^2 + 1)(1)}{(x - 3)^2}
   $$
4. Simplify the numerator:
   $$
   f'(x) = \frac{2x^2 - 6x - x^2 - 1}{(x - 3)^2} = \frac{x^2 - 6x - 1}{(x - 3)^2}
   $$

### Exercise 4: Derivative with Radical and Powers
**Problem:**
Differentiate the function:
$$
f(x) = \sqrt{x} (x^3 - 2x + 1)
$$

**Solution:**
1. Rewrite the radical as a power: $\sqrt{x} = x^{1/2}$.
2. Apply the distributive property before differentiating to avoid the product rule:
   $$
   f(x) = x^{1/2} \cdot x^3 - 2 x^{1/2} \cdot x + x^{1/2} = x^{7/2} - 2x^{3/2} + x^{1/2}
   $$
3. Differentiate each term using the power rule:
   $$
   f'(x) = \frac{7}{2} x^{5/2} - 2\left(\frac{3}{2}\right) x^{1/2} + \frac{1}{2} x^{-1/2}
   $$
4. Simplify the coefficients and rewrite in radical form:
   $$
   f'(x) = \frac{7}{2} x^2 \sqrt{x} - 3 \sqrt{x} + \frac{1}{2\sqrt{x}}
   $$

### Exercise 5: Application of the Chain Rule
**Problem:**
> **[Supplementary]**
> Find the derivative of the function:
> $$
> f(x) = (2x^3 - 5)^4
> $$

**Solution:**
> **[Supplementary]**
> 1. The function is composite of the form $u^4$ with $u(x) = 2x^3 - 5$.
> 2. According to the chain rule:
>    $$
>    f'(x) = 4(2x^3 - 5)^3 \cdot (2x^3 - 5)'
>    $$
> 3. Compute the derivative of the inner function:
>    $$
>    (2x^3 - 5)' = 6x^2
>    $$
> 4. Multiply the terms:
>    $$
>    f'(x) = 4(2x^3 - 5)^3 (6x^2) = 24x^2 (2x^3 - 5)^3
>    $$

### Exercise 6: Tangent Line Equation
**Problem:**
> **[Supplementary]**
> Find the equation of the tangent line to the function $f(x) = \frac{2}{x}$ at the point with abscissa $x_0 = 1$.

**Solution:**
> **[Supplementary]**
> 1. The equation of the tangent line at the point $(x_0, f(x_0))$ is given by the formula:
>    $$
>    y - f(x_0) = f'(x_0)(x - x_0)
>    $$
> 2. Compute the function value:
>    $$
>    f(1) = \frac{2}{1} = 2
>    $$
> 3. Compute the derivative of $f(x) = 2 x^{-1}$:
>    $$
>    f'(x) = 2(-1 x^{-2}) = -\frac{2}{x^2}
>    $$
> 4. Compute the slope of the tangent line at $x_0 = 1$:
>    $$
>    f'(1) = -\frac{2}{1^2} = -2
>    $$
> 5. Substitute the values into the tangent line equation:
>    $$
>    y - 2 = -2(x - 1) \implies y - 2 = -2x + 2 \implies y = -2x + 4
>    $$

### Exercise 7: Derivative of a Quotient with a Trigonometric Term
**Problem:**
> **[Supplementary]**
> Find the derivative of the function:
> $$
> f(x) = \frac{\sin(x)}{x^2}
> $$

**Solution:**
> **[Supplementary]**
> 1. Apply the quotient rule:
>    $$
>    f'(x) = \frac{(\sin(x))'(x^2) - \sin(x)(x^2)'}{(x^2)^2}
>    $$
> 2. Compute the derivatives:
>    $$
>    f'(x) = \frac{\cos(x) \cdot x^2 - \sin(x) \cdot 2x}{x^4}
>    $$
> 3. Simplify by factoring out $x$ from the numerator:
>    $$
>    f'(x) = \frac{x(x \cos(x) - 2 \sin(x))}{x^4} = \frac{x \cos(x) - 2 \sin(x)}{x^3}
>    $$

### Exercise 8: Derivative of a Product with Exponential and Logarithm
**Problem:**
> **[Supplementary]**
> Find the derivative of the function:
> $$
> f(x) = e^x \ln(x)
> $$

**Solution:**
> **[Supplementary]**
> 1. Apply the product rule:
>    $$
>    f'(x) = (e^x)' \ln(x) + e^x (\ln(x))'
>    $$
> 2. Recall that $(e^x)' = e^x$ and $(\ln(x))' = \frac{1}{x}$. Substitute:
>    $$
>    f'(x) = e^x \ln(x) + e^x \cdot \frac{1}{x}
>    $$
> 3. Factor out $e^x$:
>    $$
>    f'(x) = e^x \left(\ln(x) + \frac{1}{x}\right)
>    $$

---

## Exam Tip: Avoiding Errors with the Quotient Rule

The quotient rule is one of the most frequent sources of numerical errors in exams due to the minus sign in the numerator.
- **Mnemonic Rule:** "Derivative of the top times the bottom, MINUS the top times the derivative of the bottom, all over the bottom squared."
- **Common Mistake:** Reversing the order in the numerator (i.e. $f g' - f' g$) will give the opposite result (wrong sign).
- **Tip:** Always keep parentheses around the terms after the minus sign to correctly distribute the minus to all inner terms.
