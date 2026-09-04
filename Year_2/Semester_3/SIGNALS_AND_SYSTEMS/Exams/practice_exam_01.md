# Practice Exam 01: Signals and Systems

**Course:** Signals and Systems (Course Code 303)  
**Format:** Comprehensive Practice Examination with Full Solutions  
**Total Points:** 100 points  
**Time Allowed:** 120 minutes  

---

## Part I: Examination Questions

### Section A: Signal Classification, Energy, and Power (20 Points)

1. *(10 Points)* Determine whether the following continuous-time signal is an energy signal, a power signal, or neither. If it is an energy signal, calculate its total energy $E_\infty$; if it is a power signal, calculate its average power $P_\infty$:
   $$x(t) = 4 \cos\left(10\pi t + \frac{\pi}{4}\right) + 2 \sin(20\pi t)$$
2. *(10 Points)* Given the signal $y(t) = e^{-2t} \sin(4t) u(t)$, determine its odd component $y_o(t)$ and evaluate $y_o(0)$.

---

### Section B: System Property Proofs (30 Points)

For each of the following continuous-time systems where $y(t) = \mathcal{T}\{x(t)\}$, determine whether the system is:
a) Memoryless or Dynamic
b) Causal or Non-Causal
c) Linear or Non-Linear
d) Time-Invariant or Time-Variant
e) BIBO Stable or Unstable

Provide formal mathematical proofs for all five properties for each system:
1. *(15 Points)* **System 1:** $y(t) = \int_{t - 3}^{t + 1} x(\tau) \, d\tau$
2. *(15 Points)* **System 2:** $y(t) = x(2t) + 3$

---

### Section C: The Convolution Integral (30 Points)

An LTI system has impulse response:
$$h(t) = e^{-t} [u(t) - u(t - 2)]$$
The input to the system is:
$$x(t) = u(t) - u(t - 1)$$

1. *(10 Points)* Determine the total time duration over which the output $y(t)$ is non-zero.
2. *(20 Points)* Evaluate the convolution integral $y(t) = x(t) * h(t)$ analytically for all $t \in (-\infty, \infty)$. State the exact closed-form expressions for each piecewise interval.

---

### Section D: Interconnected LTI Systems & Step Response (20 Points)

1. *(10 Points)* The step response of a continuous-time LTI system is given by:
   $$s(t) = \left(2 - 2e^{-4t}\right) u(t)$$
   Determine the system's impulse response $h(t)$.
2. *(10 Points)* Is this system BIBO stable? Prove your answer by testing the absolute integrability of $h(t)$.

---

## Part II: Complete Solutions and Grading Rubric

### Section A Solutions

1. **Energy / Power Calculation (10 Points):**
   - The signal $x(t) = 4 \cos\left(10\pi t + \frac{\pi}{4}\right) + 2 \sin(20\pi t)$ is the sum of two sinusoids.
   - Frequency 1: $f_1 = \frac{10\pi}{2\pi} = 5\text{ Hz} \implies T_1 = \frac{1}{5}\text{ s}$.
   - Frequency 2: $f_2 = \frac{20\pi}{2\pi} = 10\text{ Hz} \implies T_2 = \frac{1}{10}\text{ s}$.
   - The ratio $\frac{T_1}{T_2} = \frac{1/5}{1/10} = 2 \in \mathbb{Q}$, so $x(t)$ is periodic with fundamental period $T_0 = \frac{1}{5}\text{ s}$.
   - Periodic signals that do not vanish have infinite total energy ($E_\infty \to \infty$) and finite average power ($0 < P_\infty < \infty$). Therefore, $x(t)$ is a **Power Signal**. *(4 pts)*
   - For distinct orthogonal harmonic frequencies, total power is the sum of individual component powers:
     $$P_\infty = \frac{A_1^2}{2} + \frac{A_2^2}{2} = \frac{4^2}{2} + \frac{2^2}{2} = \frac{16}{2} + \frac{4}{2} = 8 + 2 = 10\text{ W}$$
     *(6 pts)*

2. **Odd Component Evaluation (10 Points):**
   - $y(t) = e^{-2t} \sin(4t) u(t)$.
   - $y(-t) = e^{2t} \sin(-4t) u(-t) = -e^{2t} \sin(4t) u(-t)$.
   - Odd part:
     $$y_o(t) = \frac{y(t) - y(-t)}{2} = \frac{e^{-2t} \sin(4t) u(t) + e^{2t} \sin(4t) u(-t)}{2}$$
   - At $t = 0$: $\sin(0) = 0 \implies y_o(0) = 0$. (Any valid odd signal must satisfy $y_o(0) = 0$). *(10 pts)*

---

### Section B Solutions

1. **System 1: $y(t) = \int_{t - 3}^{t + 1} x(\tau) \, d\tau$ (15 Points):**
   - **Memory:** Output depends on an interval of values $[\,t-3, t+1\,]$, not just $x(t)$. $\implies$ **Dynamic (Has Memory)**. *(3 pts)*
   - **Causality:** Upper integration limit is $t + 1 > t$. Computing $y(t)$ requires future input values up to 1 second ahead. $\implies$ **Non-Causal**. *(3 pts)*
   - **Linearity:**
     $$\int_{t-3}^{t+1} [a x_1(\tau) + b x_2(\tau)] \, d\tau = a \int_{t-3}^{t+1} x_1(\tau) \, d\tau + b \int_{t-3}^{t+1} x_2(\tau) \, d\tau = a y_1(t) + b y_2(t)$$
     $\implies$ **Linear**. *(3 pts)*
   - **Time-Invariance:** Let $x_1(t) = x(t - t_0)$.
     $$y_1(t) = \int_{t-3}^{t+1} x(\tau - t_0) \, d\tau$$
     Substitute $\sigma = \tau - t_0$: limits become $t - t_0 - 3$ to $t - t_0 + 1$:
     $$y_1(t) = \int_{(t - t_0) - 3}^{(t - t_0) + 1} x(\sigma) \, d\sigma = y(t - t_0)$$
     $\implies$ **Time-Invariant**. *(3 pts)*
   - **Stability:** If $|x(t)| \le M_x < \infty$:
     $$|y(t)| \le \int_{t-3}^{t+1} |x(\tau)| \, d\tau \le M_x \int_{t-3}^{t+1} 1 \, d\tau = M_x [(t+1) - (t-3)] = 4 M_x < \infty$$
     $\implies$ **BIBO Stable**. *(3 pts)*

2. **System 2: $y(t) = x(2t) + 3$ (15 Points):**
   - **Memory:** At $t = 1$, $y(1) = x(2) + 3$. Depends on $x(2) \ne x(1)$. $\implies$ **Dynamic (Has Memory)**. *(3 pts)*
   - **Causality:** At $t = 1$, requires future input $x(2)$. $\implies$ **Non-Causal**. *(3 pts)*
   - **Linearity:** For zero input $x(t) = 0$, $y(t) = 3 \ne 0$. A linear system must produce zero output for zero input. $\implies$ **Non-Linear**. *(3 pts)*
   - **Time-Invariance:**
     $y_1(t) = x_1(2t) + 3 = x(2t - t_0) + 3$.
     $y(t - t_0) = x(2(t - t_0)) + 3 = x(2t - 2t_0) + 3 \ne y_1(t)$.
     $\implies$ **Time-Variant**. *(3 pts)*
   - **Stability:** If $|x(t)| \le M_x$, then $|y(t)| \le M_x + 3 < \infty$. $\implies$ **BIBO Stable**. *(3 pts)*

---

### Section C Solutions

1. **Duration of Output (10 Points):**
   - $x(t)$ has non-zero duration $L_x = 1 - 0 = 1$ (interval $[0, 1]$).
   - $h(t)$ has non-zero duration $L_h = 2 - 0 = 2$ (interval $[0, 2]$).
   - The convolution of two causal signals of duration $L_x$ and $L_h$ is non-zero over $[0 + 0, 1 + 2] = [0, 3]$.
   - Total non-zero duration: **3 seconds** (from $t = 0$ to $t = 3$). *(10 pts)*

2. **Analytical Evaluation (20 Points):**
   $x(\tau) = 1$ for $0 \le \tau \le 1$.  
   $h(t - \tau) = e^{-(t - \tau)}$ for $0 \le t - \tau \le 2 \iff t - 2 \le \tau \le t$.

   - **Interval 1 ($t < 0$):** No overlap $\implies y(t) = 0$. *(2 pts)*
   - **Interval 2 ($0 \le t < 1$):** Overlap is $\tau \in [0, t]$:
     $$y(t) = \int_{0}^{t} 1 \cdot e^{-(t - \tau)} \, d\tau = e^{-t} \int_{0}^{t} e^\tau \, d\tau = e^{-t} (e^t - 1) = 1 - e^{-t}$$
     *(6 pts)*
   - **Interval 3 ($1 \le t < 2$):** Overlap is $\tau \in [0, 1]$:
     $$y(t) = \int_{0}^{1} 1 \cdot e^{-(t - \tau)} \, d\tau = e^{-t} \left[ e^1 - 1 \right] = (e - 1) e^{-t}$$
     *(6 pts)*
   - **Interval 4 ($2 \le t < 3$):** Overlap is $\tau \in [t - 2, 1]$:
     $$y(t) = \int_{t - 2}^{1} e^{-(t - \tau)} \, d\tau = e^{-t} [e^1 - e^{t - 2}] = e^{1 - t} - e^{-2}$$
     *(5 pts)*
   - **Interval 5 ($t \ge 3$):** Overlap is zero ($t - 2 \ge 1$) $\implies y(t) = 0$. *(1 pt)*

---

### Section D Solutions

1. **Impulse Response from Step Response (10 Points):**
   $$s(t) = (2 - 2e^{-4t}) u(t)$$
   Using $h(t) = \frac{ds(t)}{dt}$ via product rule:
   $$h(t) = \frac{d}{dt}(2 - 2e^{-4t}) \cdot u(t) + (2 - 2e^{-4t}) \cdot \frac{du(t)}{dt}$$
   $$h(t) = (8e^{-4t}) u(t) + (2 - 2e^{-0}) \delta(t) = 8e^{-4t} u(t) + 0 \cdot \delta(t) = 8e^{-4t} u(t)$$
   *(10 pts)*

2. **BIBO Stability Test (10 Points):**
   Integrate absolute impulse response:
   $$
   \int_{-\infty}^{\infty} |h(t)| \, dt = \int_{0}^{\infty} 8e^{-4t} \, dt = 8 \left[ -\frac{e^{-4t}}{4} \right]_0^\infty = 8 \left( 0 - \left(-\frac{1}{4}\right) \right) = \frac{8}{4} = 2 < \infty
   $$
   Since the integral converges to $2 < \infty$, the system is **strictly BIBO Stable**. *(10 pts)*

