# Term Project: Numerical Quadrature and Root-Finding Algorithms

## Project Overview
This computational project synthesizes the analytical theorems of differential and integral calculus with scientific computing algorithms. Students design, implement, error-bound, and benchmark numerical root-finding and quadrature algorithms in GNU Octave, comparing their empirical convergence against theoretical error theorems.

---

## 1. Module 1: Non-Linear Root Finding

### 1.1 Target Benchmark Equations
Implement solvers for the following transcendental equations:
1. $f_1(x) = x e^x - 2 = 0$ on interval $[0, 2]$.
2. $f_2(x) = \cos(x) - x^3 = 0$ on interval $[0, 1]$.

### 1.2 Algorithms to Implement
1. **Bisection Method**:
   - Requires $f(a) \cdot f(b) < 0$ (guaranteed convergence by Bolzano's Theorem).
   - Linear convergence rate with error bound $\varepsilon_k \le \frac{b - a}{2^k}$.
2. **Newton-Raphson Method**:
   - Iteration scheme:
     $$x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}$$
   - Quadratic convergence rate near simple roots.
3. **Secant Method**:
   - Quasi-Newton scheme eliminating the analytical derivative evaluation:
     $$x_{k+1} = x_k - f(x_k) \frac{x_k - x_{k-1}}{f(x_k) - f(x_{k-1})}$$
   - Superlinear convergence rate ($\alpha \approx 1.618$).

---

## 2. Module 2: Composite Numerical Quadrature

Evaluate non-elementary integrals where no closed-form elementary antiderivative exists:
$$I = \int_0^1 e^{-x^2} \, dx \quad (\text{Gaussian Error Function})$$

### 2.1 Quadrature Rules
1. **Composite Trapezoidal Rule**:
   Subdivide $[a, b]$ into $N$ equal panels of width $h = \frac{b - a}{N}$:
   $$T(h) = \frac{h}{2} \left[ f(x_0) + 2 \sum_{i=1}^{N-1} f(x_i) + f(x_N) \right]$$
   Theoretical global error: $E_T = -\frac{(b - a)}{12} h^2 f''(\xi), \quad \xi \in (a, b)$.
2. **Composite Simpson's 1/3 Rule** ($N$ even):
   $$S(h) = \frac{h}{3} \left[ f(x_0) + 4 \sum_{i=1,3,\dots}^{N-1} f(x_i) + 2 \sum_{i=2,4,\dots}^{N-2} f(x_i) + f(x_N) \right]$$
   Theoretical global error: $E_S = -\frac{(b - a)}{180} h^4 f^{(4)}(\xi), \quad \xi \in (a, b)$.

---

## 3. Implementation Requirements (GNU Octave)

* `bisection.m`: General bisection solver accepting function handle, bounds, tolerance ($10^{-10}$), and maximum iterations.
* `newton_raphson.m`: Newton solver accepting function and derivative handles.
* `secant.m`: Two-point secant solver.
* `composite_trapezoid.m`: Vectorized composite trapezoid evaluator.
* `composite_simpson.m`: Vectorized composite Simpson evaluator.
* `convergence_analysis.m`: Generates log-log error plots ($\log(\text{error})$ vs. $\log(h)$) demonstrating the slope of $2$ for the trapezoid rule and slope of $4$ for Simpson's rule.

---

## 4. Evaluation Rubric

| Component | Target Metric | Points |
|:---|:---|:---:|
| Root Finding Implementation | Flawless execution and iteration stopping criteria across Bisection, Newton, Secant | 25 |
| Quadrature Implementation | Accurate vectorized Trapezoidal and Simpson's 1/3 routines | 25 |
| Empirical vs. Theoretical Convergence | Correct verification of $O(h^2)$ and $O(h^4)$ asymptotic rates via log-log plots | 25 |
| Error Bound Analysis | Analytical calculation of maximum derivative values and strict error bounds | 15 |
| Code Standards & Formatting | Clean Octave code, documentation, and reproducibility | 10 |
| **Total** | | **100** |

