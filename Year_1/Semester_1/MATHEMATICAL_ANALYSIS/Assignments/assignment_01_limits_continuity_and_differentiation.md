# Assignment 01: Limits, Continuity Analysis, and Analytical Differentiation

## Objective
Evaluate limits with indeterminate forms, determine parameters for piecewise continuity and differentiability, apply derivative theorems, and conduct analytical curve sketching.

---

## Technical Specifications

### Problem 1: Indeterminate Limit Evaluation
Evaluate the following limits analytically without employing L'Hopital's rule:
1. $\displaystyle \lim_{x \to 4} \frac{\sqrt{2x + 1} - 3}{x - 4}$
2. $\displaystyle \lim_{x \to 0} \frac{1 - \cos(4x)}{x \sin(3x)}$
3. $\displaystyle \lim_{x \to \infty} \left( \sqrt{x^2 + 6x - 2} - x \right)$

### Problem 2: Piecewise Continuity and Differentiability
Consider the piecewise parametric function $f: \mathbb{R} \to \mathbb{R}$:

$$f(x) = \begin{cases}
a x^2 + b x + 1, & x \le 1 \\
\displaystyle \frac{\sin(\pi x)}{x - 1} + 2, & x > 1
\end{cases}$$

1. Compute the right-hand limit $\lim_{x \to 1^+} f(x)$ using standard trigonometric limits.
2. Determine the exact relationship between constants $a$ and $b$ that guarantees $f$ is **continuous** at $x = 1$.
3. Compute the left-hand derivative $f'_-(1)$ and right-hand derivative $f'_+(1)$.
4. Determine the unique values of $a$ and $b$ such that $f$ is **differentiable** at $x = 1$.

### Problem 3: Tangent Lines and Implicit Differentiation
Consider the Folium of Descartes curve:
$$x^3 + y^3 - 6xy = 0$$
1. Compute the derivative $\frac{dy}{dx}$ via implicit differentiation.
2. Find the equation of the tangent line to the curve at the point $(3, 3)$.
3. Determine the coordinates of all points on the curve where the tangent line is strictly horizontal ($\frac{dy}{dx} = 0$).

---

## Deliverables & Evaluation Rubric

| Criterion | Target Metric | Points |
|:---|:---|:---:|
| Analytical Limit Derivations | Rigorous algebraic conjugate expansion and trigonometric limit laws | 30 |
| Continuity Parameter Solvers | Exact right-hand limit derivation and continuity condition formulation | 25 |
| Differentiability Equivalence | Accurate limit quotient derivatives and unique $(a, b)$ solution | 25 |
| Implicit Differentiation & Tangents | Flawless derivative expression, tangent equation, and horizontal slopes | 20 |
| **Total** | | **100** |

