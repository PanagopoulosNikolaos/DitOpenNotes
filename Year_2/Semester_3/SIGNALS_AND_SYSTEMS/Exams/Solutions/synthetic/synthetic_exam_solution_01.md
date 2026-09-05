# University of Ioannina - Department of Informatics and Telecommunications
## Course: Signals and Systems (Course Code: 303)
### Academic Year: 2025-2026
### Synthetic Final Examination Solutions - Paper 01

---

### Solution 1: Signal Classification, Energy, Power & Periodicity (20 Marks)

#### Part A: Continuous-Time Energy and Power (8 Marks)
Given signal:
$$x_1(t) = 3 e^{-2|t|}$$

1. **Classification:**
   - The signal decays exponentially to zero as $t \to \pm \infty$: $\lim_{t \to \pm \infty} x_1(t) = 0$.
   - A signal with square-integrable amplitude over $(-\infty, \infty)$ has finite total energy and zero average power. Therefore, $x_1(t)$ is an **Energy Signal**.

2. **Energy Calculation:**
   Using the symmetry of $|t|$ ($x_1(t)$ is an even function):
   $$E_\infty = \int_{-\infty}^{\infty} |x_1(t)|^2 \, dt = \int_{-\infty}^{\infty} \left(3 e^{-2|t|}\right)^2 \, dt = \int_{-\infty}^{\infty} 9 e^{-4|t|} \, dt$$
   $$E_\infty = 2 \int_{0}^{\infty} 9 e^{-4t} \, dt = 18 \left[ \frac{e^{-4t}}{-4} \right]_{0}^{\infty} = 18 \left(0 - \left(-\frac{1}{4}\right)\right) = \frac{18}{4} = 4.5 \text{ J}$$
   The average power for any energy signal over infinite time is:
   $$P_\infty = \lim_{T \to \infty} \frac{1}{2T} \int_{-T}^{T} |x_1(t)|^2 \, dt = \lim_{T \to \infty} \frac{E_\infty}{2T} = 0 \text{ W}$$

---

#### Part B: Discrete-Time Periodicity Analysis (6 Marks)
Given:
$$x_2[n] = 5 \cos\left(\frac{3\pi}{7} n + \frac{\pi}{6}\right) - 2 \sin\left(\frac{5\pi}{8} n\right)$$

1. **Individual Component Periodicity:**
   A discrete sinusoidal sequence $\cos(\omega_0 n)$ is periodic if and only if its normalized digital frequency $\frac{\omega_0}{2\pi}$ is a rational number $\frac{m}{N} \in \mathbb{Q}$.
   - First term: $\omega_1 = \frac{3\pi}{7}$.
     $$\frac{\omega_1}{2\pi} = \frac{3\pi / 7}{2\pi} = \frac{3}{14}$$
     Since $\gcd(3, 14) = 1$, the fundamental period is $N_1 = 14$ samples.
   - Second term: $\omega_2 = \frac{5\pi}{8}$.
     $$\frac{\omega_2}{2\pi} = \frac{5\pi / 8}{2\pi} = \frac{5}{16}$$
     Since $\gcd(5, 16) = 1$, the fundamental period is $N_2 = 16$ samples.

2. **Composite Signal Periodicity:**
   Both components are periodic. The composite signal is periodic with overall fundamental period $N_0$ equal to the least common multiple (LCM) of $N_1$ and $N_2$:
   $$N_0 = \text{lcm}(14, 16) = \text{lcm}(2 \times 7, 2^4) = 2^4 \times 7 = 16 \times 7 = 112 \text{ samples}$$

---

#### Part C: Even and Odd Decomposition (6 Marks)
Given:
$$x_3(t) = (t^2 + 4t) u(t)$$
Then:
$$x_3(-t) = \left((-t)^2 + 4(-t)\right) u(-t) = (t^2 - 4t) u(-t)$$

1. **Derivation:**
   - **Even Component:**
     $$x_{3,e}(t) = \frac{x_3(t) + x_3(-t)}{2} = \frac{(t^2 + 4t) u(t) + (t^2 - 4t) u(-t)}{2}$$
     Piecewise representation:
     $$x_{3,e}(t) = \begin{cases} 
     \frac{1}{2} t^2 + 2t, & t > 0 \\ 
     0, & t = 0 \\ 
     \frac{1}{2} t^2 - 2t, & t < 0 
     \end{cases}$$
   - **Odd Component:**
     $$x_{3,o}(t) = \frac{x_3(t) - x_3(-t)}{2} = \frac{(t^2 + 4t) u(t) - (t^2 - 4t) u(-t)}{2}$$
     Piecewise representation:
     $$x_{3,o}(t) = \begin{cases} 
     \frac{1}{2} t^2 + 2t, & t > 0 \\ 
     0, & t = 0 \\ 
     -\frac{1}{2} t^2 + 2t, & t < 0 
     \end{cases}$$

2. **Verification:**
   For $t > 0$:
   $$x_{3,e}(t) + x_{3,o}(t) = \left(\frac{1}{2}t^2 + 2t\right) + \left(\frac{1}{2}t^2 + 2t\right) = t^2 + 4t = x_3(t)$$
   At $t = 0$: $x_{3,e}(0) = 0$ and $x_{3,o}(0) = 0$.

---

### Solution 2: Formal Proofs of System Properties (25 Marks)

#### System 1: $y(t) = t \cdot x(t - 2)$ (12 Marks)

1. **Memory:**
   At $t = 3$, $y(3) = 3 x(1)$. Because the output at $t=3$ depends on the input at past time $t=1 \ne 3$, the system is **Dynamic (Has Memory)**.
2. **Causality:**
   For all $t \in \mathbb{R}$, $t - 2 < t$. The output at any time $t$ depends strictly on the past input value at $t - 2$. Therefore, the system is **Causal**.
3. **Linearity:**
   Let $x(t) = a x_1(t) + b x_2(t)$.
   $$y(t) = \mathcal{T}\{a x_1(t) + b x_2(t)\} = t \left[a x_1(t - 2) + b x_2(t - 2)\right] = a \left[t x_1(t - 2)\right] + b \left[t x_2(t - 2)\right] = a y_1(t) + b y_2(t)$$
   The system satisfies the superposition principle $\implies$ **Linear**.
4. **Time-Invariance:**
   - Delay input by $t_0$: let $x_d(t) = x(t - t_0)$.
     $$y_d(t) = \mathcal{T}\{x_d(t)\} = t \cdot x_d(t - 2) = t \cdot x(t - t_0 - 2)$$
   - Delay output by $t_0$:
     $$y(t - t_0) = (t - t_0) x((t - t_0) - 2) = (t - t_0) x(t - t_0 - 2)$$
   - Because $y_d(t) \ne y(t - t_0)$ due to the explicit factor of $t$, the system is **Time-Variant**.
5. **BIBO Stability:**
   Consider the bounded input $x(t) = 1$ for all $t$ (where $|x(t)| \le 1 < \infty$).
   The response is $y(t) = t \cdot 1 = t$.
   As $t \to \infty$, $|y(t)| = |t| \to \infty$. A bounded input produces an unbounded output $\implies$ **BIBO Unstable**.

---

#### System 2: $y[n] = \sum_{k=-\infty}^{n} 2^{-(n - k)} x[k]$ (13 Marks)

1. **Memory:**
   Setting $m = n - k$:
   $$y[n] = \sum_{m=0}^{\infty} 2^{-m} x[n - m] = x[n] + \frac{1}{2} x[n - 1] + \frac{1}{4} x[n - 2] + \dots$$
   The output $y[n]$ depends on past samples $x[n-1], x[n-2], \dots$ $\implies$ **Dynamic (Has Memory)**.
2. **Causality:**
   The summation index $m = n - k \ge 0$, which implies $k \le n$. The output never requires future samples $x[n+1], x[n+2], \dots$ $\implies$ **Causal**.
3. **Linearity:**
   Let $x[n] = a x_1[n] + b x_2[n]$.
   $$\mathcal{T}\{a x_1[n] + b x_2[n]\} = \sum_{k=-\infty}^{n} 2^{-(n-k)} [a x_1[k] + b x_2[k]] = a \sum_{k=-\infty}^{n} 2^{-(n-k)} x_1[k] + b \sum_{k=-\infty}^{n} 2^{-(n-k)} x_2[k] = a y_1[n] + b y_2[n]$$
   $\implies$ **Linear**.
4. **Time-Invariance:**
   The impulse response is obtained by setting $x[n] = \delta[n]$:
   $$h[n] = \sum_{k=-\infty}^{n} 2^{-(n-k)} \delta[k] = 2^{-n} u[n]$$
   The input-output relationship is a discrete convolution with fixed impulse response: $y[n] = x[n] * h[n]$. All convolution operators are strictly **Time-Invariant**.
5. **BIBO Stability:**
   A discrete LTI system is BIBO stable if and only if its impulse response is absolutely summable:
   $$\sum_{n=-\infty}^{\infty} |h[n]| = \sum_{n=0}^{\infty} \left(\frac{1}{2}\right)^n = \frac{1}{1 - 1/2} = 2 < \infty$$
   Since the sum is finite, the system is strictly **BIBO Stable**.

---

### Solution 3: Continuous-Time Convolution Integral (30 Marks)

Given:
- $h(t) = (2 - t) [u(t) - u(t - 2)]$ (support: $[0, 2]$)
- $x(t) = u(t - 1) - u(t - 3)$ (support: $[1, 3]$)

1. **Support Calculation:**
   $$\text{Start of } y(t) = t_{x,\text{start}} + t_{h,\text{start}} = 1 + 0 = 1$$
   $$\text{End of } y(t) = t_{x,\text{end}} + t_{h,\text{end}} = 3 + 2 = 5$$
   The output $y(t)$ is non-zero strictly on the closed interval $[1, 5]$.

2. **Analytical Evaluation:**
   $$y(t) = \int_{-\infty}^{\infty} x(\tau) h(t - \tau) \, d\tau = \int_{1}^{3} h(t - \tau) \, d\tau$$
   The integrand $h(t - \tau) = 2 - (t - \tau)$ is non-zero when $0 \le t - \tau \le 2 \iff t - 2 \le \tau \le t$.
   Substituting $u = t - \tau \implies d\tau = -du$:
   When $\tau = \tau_{\text{lower}} \implies u_{\text{upper}} = t - \tau_{\text{lower}}$.
   When $\tau = \tau_{\text{upper}} \implies u_{\text{lower}} = t - \tau_{\text{upper}}$.
   $$y(t) = \int_{t - \tau_{\text{upper}}}^{t - \tau_{\text{lower}}} (2 - u) \, du = \left[ 2u - \frac{u^2}{2} \right]_{t - \tau_{\text{upper}}}^{t - \tau_{\text{lower}}}$$

   - **Interval 1: $t < 1$**  
     $t < 1 \implies$ No overlap between $[1, 3]$ and $[t - 2, t]$.
     $$y(t) = 0$$

   - **Interval 2: $1 \le t < 3$**  
     Overlap interval for $\tau$: $[\,1, t\,]$.
     $u$-limits: from $t - t = 0$ to $t - 1$.
     $$y(t) = \int_{0}^{t - 1} (2 - u) \, du = \left[ 2u - \frac{u^2}{2} \right]_{0}^{t - 1} = 2(t - 1) - \frac{(t - 1)^2}{2} = -\frac{1}{2} t^2 + 3t - \frac{5}{2}$$

   - **Interval 3: $3 \le t < 5$**  
     Overlap interval for $\tau$: $[\,t - 2, 3\,]$.
     $u$-limits: from $t - 3$ to $t - (t - 2) = 2$.
     $$y(t) = \int_{t - 3}^{2} (2 - u) \, du = \left[ 2u - \frac{u^2}{2} \right]_{t - 3}^{2} = \left(2(2) - \frac{4}{2}\right) - \left(2(t - 3) - \frac{(t - 3)^2}{2}\right)$$
     $$y(t) = 2 - \left(2t - 6 - \frac{t^2 - 6t + 9}{2}\right) = \frac{1}{2} (t - 5)^2 = \frac{1}{2} t^2 - 5t + \frac{25}{2}$$

   - **Interval 4: $t \ge 5$**  
     $t - 2 \ge 3 \implies$ No overlap.
     $$y(t) = 0$$

3. **Boundary Continuity Verification:**
   - At $t = 1$:
     $$y(1^-) = 0, \quad y(1^+) = -\frac{1}{2}(1)^2 + 3(1) - \frac{5}{2} = -0.5 + 3 - 2.5 = 0 \quad (\text{Continuous})$$
   - At $t = 3$:
     $$y(3^-) = -\frac{1}{2}(9) + 3(3) - \frac{5}{2} = -4.5 + 9 - 2.5 = 2.0$$
     $$y(3^+) = \frac{1}{2}(3 - 5)^2 = \frac{1}{2}(-2)^2 = 2.0 \quad (\text{Continuous})$$
   - At $t = 5$:
     $$y(5^-) = \frac{1}{2}(5 - 5)^2 = 0, \quad y(5^+) = 0 \quad (\text{Continuous})$$

---

### Solution 4: Differential Equations, Transfer Functions & Frequency Response (25 Marks)

Given:
$$\frac{d^2 y(t)}{dt^2} + 5 \frac{dy(t)}{dt} + 6 y(t) = 2 \frac{dx(t)}{dt} + 8 x(t)$$

1. **Transfer Function & Pole-Zero Map:**
   Applying the bilateral Laplace transform:
   $$(s^2 + 5s + 6) Y(s) = (2s + 8) X(s)$$
   $$H(s) = \frac{Y(s)}{X(s)} = \frac{2s + 8}{s^2 + 5s + 6} = \frac{2(s + 4)}{(s + 2)(s + 3)}$$
   - **Zeros:** $s = -4$
   - **Poles:** $s = -2$ and $s = -3$

2. **Causal Impulse Response & ROC:**
   - For a causal system, the ROC is the half-plane to the right of the rightmost pole:
     $$\text{ROC}: \text{Re}(s) > -2$$
   - Partial fraction expansion:
     $$H(s) = \frac{A}{s + 2} + \frac{B}{s + 3}$$
     $$A = \left. (s + 2) H(s) \right|_{s = -2} = \frac{2(-2) + 8}{-2 + 3} = \frac{4}{1} = 4$$
     $$B = \left. (s + 3) H(s) \right|_{s = -3} = \frac{2(-3) + 8}{-3 + 2} = \frac{2}{-1} = -2$$
     $$H(s) = \frac{4}{s + 2} - \frac{2}{s + 3}, \quad \text{Re}(s) > -2$$
   - Taking the inverse Laplace transform:
     $$h(t) = \left(4 e^{-2t} - 2 e^{-3t}\right) u(t)$$

3. **BIBO Stability Proof:**
   - **Criterion 1 (Pole Locations):** Both poles lie strictly in the open left-half of the complex $s$-plane ($\text{Re}(p_1) = -2 < 0$, $\text{Re}(p_2) = -3 < 0$), and the $j\omega$ axis ($\text{Re}(s) = 0$) is included within the ROC ($\text{Re}(s) > -2$).
   - **Criterion 2 (Absolute Integrability):**
     $$\int_{-\infty}^{\infty} |h(t)| \, dt = \int_{0}^{\infty} (4 e^{-2t} - 2 e^{-3t}) \, dt = \left[ -2 e^{-2t} + \frac{2}{3} e^{-3t} \right]_{0}^{\infty} = 0 - \left(-2 + \frac{2}{3}\right) = \frac{4}{3} < \infty$$
   - Both criteria confirm the causal system is strictly **BIBO Stable**.

4. **Steady-State Frequency Response & Sinusoidal Response:**
   Setting $s = j\omega$:
   $$H(j\omega) = \frac{8 + j2\omega}{(6 - \omega^2) + j5\omega}$$
   For the input $x(t) = 10 \cos(2t + \pi/4)$, the frequency is $\omega_0 = 2 \text{ rad/s}$.
   Evaluating at $\omega = 2$:
   $$H(j2) = \frac{8 + j4}{(6 - 4) + j10} = \frac{8 + j4}{2 + j10} = \frac{4 + j2}{1 + j5}$$
   Multiply numerator and denominator by $(1 - j5)$:
   $$H(j2) = \frac{(4 + j2)(1 - j5)}{1^2 + 5^2} = \frac{4 - j20 + j2 + 10}{26} = \frac{14 - j18}{26} = \frac{7 - j9}{13}$$
   - **Magnitude:**
     $$|H(j2)| = \frac{\sqrt{7^2 + (-9)^2}}{13} = \frac{\sqrt{49 + 81}}{13} = \frac{\sqrt{130}}{13} = \frac{1}{\sqrt{13}} \sqrt{10} \approx 0.877$$
   - **Phase:**
     $$\angle H(j2) = \arctan\left(-\frac{9}{7}\right) \approx -52.125^\circ \approx -0.9098 \text{ rad}$$
   - **Steady-State Output:**
     $$y_{ss}(t) = 10 |H(j2)| \cos\left(2t + \frac{\pi}{4} + \angle H(j2)\right)$$
     Phase term: $45^\circ - 52.125^\circ = -7.125^\circ \approx -0.1244 \text{ rad}$.
     $$y_{ss}(t) = \frac{10 \sqrt{130}}{13} \cos\left(2t - 0.1244 \text{ rad}\right) \approx 8.77 \cos(2t - 7.125^\circ)$$

