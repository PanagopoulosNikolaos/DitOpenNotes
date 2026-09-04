# Exercises: Continuous-Time Convolution and LTI System Analysis

This practice problem set provides complete step-by-step solutions for continuous-time convolution integrals and stability/causality tests on LTI impulse responses.

---

## Problem 1: Piecewise Graphical Convolution

Calculate the convolution $y(t) = x(t) * h(t)$ where:
$$
x(t) = u(t) - u(t - 3)
$$
$$
h(t) = 2[u(t) - u(t - 1)]
$$

### Questions:
1. Identify all critical time transition points.
2. Formulate the integral for each distinct time region.
3. Write down the complete closed-form piecewise definition of $y(t)$ and sketch the resulting waveform.

---

### Solution to Problem 1

$x(\tau)$ is a rectangular pulse of height 1 on $[0, 3]$.  
$h(\tau)$ is a rectangular pulse of height 2 on $[0, 1]$.  
$h(t - \tau)$ is a rectangular pulse of height 2 on $\tau \in [t - 1, t]$.

#### Interval Analysis:
- **Region 1: $t < 0$**  
  The leading edge $t$ has not reached $\tau = 0$. Zero overlap.
  $$y(t) = 0$$

- **Region 2: $0 \le t < 1$**  
  The leading edge enters $[0, 3]$. The trailing edge $t - 1 < 0$. Overlap is $\tau \in [0, t]$.
  $$y(t) = \int_{0}^{t} (1 \cdot 2) \, d\tau = 2t$$

- **Region 3: $1 \le t < 3$**  
  The entire pulse $h(t - \tau)$ of width 1 is fully inside $[0, 3]$. Overlap is $\tau \in [t - 1, t]$.
  $$y(t) = \int_{t - 1}^{t} (1 \cdot 2) \, d\tau = 2 [t - (t - 1)] = 2 \cdot 1 = 2$$

- **Region 4: $3 \le t < 4$**  
  The leading edge has passed $\tau = 3$, but the trailing edge $t - 1$ is still within $[0, 3]$. Overlap is $\tau \in [t - 1, 3]$.
  $$y(t) = \int_{t - 1}^{3} 2 \, d\tau = 2 [3 - (t - 1)] = 2 [4 - t] = 8 - 2t$$

- **Region 5: $t \ge 4$**  
  The trailing edge $t - 1 \ge 3 \implies t \ge 4$. Zero overlap.
  $$y(t) = 0$$

#### Summary Equation:
$$
y(t) = \begin{cases}
0, & t < 0 \\
2t, & 0 \le t < 1 \\
2, & 1 \le t < 3 \\
8 - 2t, & 3 \le t < 4 \\
0, & t \ge 4
\end{cases}
$$
The output is a continuous trapezoid of height 2, base width 4 ($3 + 1 = 4$), and flat top width 2 ($3 - 1 = 2$).

---

## Problem 2: LTI Impulse Response Characterization

An LTI system has impulse response:
$$
h(t) = e^{-3t} u(t - 2)
$$

### Questions:
1. Is the system causal? Justify.
2. Is the system memoryless? Justify.
3. Is the system BIBO stable? Prove mathematically.
4. Find the output $y(t)$ when the input is $x(t) = \delta(t - 4)$.

---

### Solution to Problem 2

1. **Causality:**  
   An LTI system is causal if and only if $h(t) = 0$ for all $t < 0$.  
   Since $u(t - 2) = 0$ for $t < 2$, $h(t) = 0$ for all $t < 2$ (which includes all $t < 0$).  
   $\implies$ **The system is Causal** (specifically, it features a 2-second initial transport delay).

2. **Memory:**  
   An LTI system is memoryless if and only if $h(t) = K \delta(t)$.  
   Here, $h(t)$ is non-zero over a continuous interval $t \ge 2$.  
   $\implies$ **The system has Memory (Dynamic)**.

3. **BIBO Stability:**  
   We test whether $h(t)$ is absolutely integrable:
   $$
   I = \int_{-\infty}^{\infty} |h(t)| \, dt = \int_{2}^{\infty} e^{-3t} \, dt = \left[ -\frac{e^{-3t}}{3} \right]_2^\infty = 0 - \left( -\frac{e^{-6}}{3} \right) = \frac{e^{-6}}{3} \approx 0.000826 < \infty
   $$
   Since the integral converges to a finite positive constant, **the system is strictly BIBO Stable**.

4. **Response to Shifted Impulse $x(t) = \delta(t - 4)$:**  
   By time-invariance:
   $$y(t) = x(t) * h(t) = \delta(t - 4) * h(t) = h(t - 4)$$
   Substituting $t - 4$ into $h$:
   $$
   y(t) = e^{-3(t - 4)} u((t - 4) - 2) = e^{-3t + 12} u(t - 6)
   $$

