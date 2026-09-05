# University of Ioannina - Department of Informatics and Telecommunications
## Course: Signals and Systems (Course Code: 303)
### Academic Year: 2025-2026
### Synthetic Final Examination - Paper 01

**Time Allowed:** 3 Hours  
**Total Marks:** 100 Points  
**Instructions:**
- Answer all questions with rigorous mathematical derivations and full working.
- State all integration limits, transformation properties, and region of convergence (ROC) definitions explicitly.
- Verify boundary continuity for all piecewise convolution results.

---

### Question 1: Signal Classification, Energy, Power & Periodicity (20 Marks)

#### Part A: Continuous-Time Energy and Power (8 Marks)
Consider the continuous-time signal:
$$x_1(t) = 3 e^{-2|t|}$$

1. Classify $x_1(t)$ as an energy signal, a power signal, or neither.
2. If it is an energy signal, compute its total energy $E_\infty = \int_{-\infty}^{\infty} |x_1(t)|^2 \, dt$. If it is a power signal, compute its average power $P_\infty$.

#### Part B: Discrete-Time Periodicity Analysis (6 Marks)
Consider the discrete-time signal:
$$x_2[n] = 5 \cos\left(\frac{3\pi}{7} n + \frac{\pi}{6}\right) - 2 \sin\left(\frac{5\pi}{8} n\right)$$

1. Determine whether each constituent sinusoidal component is periodic in discrete time. If so, determine their fundamental periods $N_1$ and $N_2$.
2. Determine whether the composite sum $x_2[n]$ is periodic. If periodic, calculate its overall fundamental period $N_0$; if not, justify mathematically.

#### Part C: Even and Odd Decomposition (6 Marks)
Given the causal signal:
$$x_3(t) = (t^2 + 4t) u(t)$$

1. Derive closed-form expressions for the even component $x_{3,e}(t)$ and odd component $x_{3,o}(t)$ for all $t \in \mathbb{R}$.
2. Verify that $x_3(t) = x_{3,e}(t) + x_{3,o}(t)$ for $t > 0$ and evaluate both components at $t = 0$.

---

### Question 2: Formal Proofs of System Properties (25 Marks)

Evaluate the fundamental operational properties of each of the following systems:
- (i) Memoryless vs. Dynamic (Memory)
- (ii) Causality (Causal vs. Non-Causal)
- (iii) Linearity (Linear vs. Non-Linear)
- (iv) Time-Invariance (Time-Invariant vs. Time-Variant)
- (v) Stability (BIBO Stable vs. Unstable)

Provide rigorous mathematical proofs or explicit counterexamples for each property.

#### System 1 (Continuous-Time) (12 Marks)
The system input-output relationship is given by:
$$y(t) = \mathcal{T}\{x(t)\} = t \cdot x(t - 2)$$

#### System 2 (Discrete-Time) (13 Marks)
The discrete-time accumulator system with exponential weighting is defined by:
$$y[n] = \mathcal{T}\{x[n]\} = \sum_{k=-\infty}^{n} 2^{-(n - k)} x[k]$$

---

### Question 3: Continuous-Time Convolution Integral (30 Marks)

An analog Linear Time-Invariant (LTI) filter has the impulse response:
$$h(t) = (2 - t) [u(t) - u(t - 2)]$$

The input excitation signal applied to the filter is:
$$x(t) = u(t - 1) - u(t - 3)$$

1. *(5 Marks)* Determine the support intervals of $x(t)$ and $h(t)$, and determine the exact start and end points of the output signal $y(t) = x(t) * h(t)$.
2. *(20 Marks)* Compute the convolution integral $y(t) = \int_{-\infty}^{\infty} x(\tau) h(t - \tau) \, d\tau$ analytically across all piecewise time intervals:
   - Interval 1: $t < 1$
   - Interval 2: $1 \le t < 3$
   - Interval 3: $3 \le t < 5$
   - Interval 4: $t \ge 5$
3. *(5 Marks)* Verify the mathematical continuity of $y(t)$ at the boundary transition points $t = 1$, $t = 3$, and $t = 5$, and sketch the resulting waveform.

---

### Question 4: Differential Equations, Transfer Functions & Frequency Response (25 Marks)

A continuous-time LTI system is described by the second-order linear constant-coefficient differential equation:
$$\frac{d^2 y(t)}{dt^2} + 5 \frac{dy(t)}{dt} + 6 y(t) = 2 \frac{dx(t)}{dt} + 8 x(t)$$

1. *(6 Marks)* Taking the bilateral Laplace transform under zero initial conditions, derive the system transfer function:
   $$H(s) = \frac{Y(s)}{X(s)}$$
   Identify all pole and zero locations in the complex $s$-plane.
2. *(7 Marks)* Assuming the system is **causal**:
   - Specify the corresponding Region of Convergence (ROC).
   - Compute the impulse response $h(t)$ using partial fraction expansion and the inverse Laplace transform.
3. *(5 Marks)* Prove whether this causal system is Bounded-Input Bounded-Output (BIBO) stable using both pole-location criteria and impulse response integrability.
4. *(7 Marks)* Determine the steady-state frequency response $H(j\omega)$ of the system. Calculate the steady-state output $y_{ss}(t)$ when the input is:
   $$x(t) = 10 \cos(2t + \frac{\pi}{4})$$

