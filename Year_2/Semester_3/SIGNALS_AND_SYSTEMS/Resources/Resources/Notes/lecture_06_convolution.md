# Lecture 06 - Convolution

The convolution operation is the fundamental mathematical tool for computing the output of a Linear Time-Invariant (LTI) system to any arbitrary input. Building on the impulse response derived in Lecture 05, convolution transforms the superposition of shifted impulse responses into a structured integral operation. This lecture develops the analytical and graphical procedures for evaluating convolution, establishes the algebraic properties that make convolution a well-behaved operation, and provides a reference table of common convolution pairs. Mastery of convolution is essential for time-domain LTI system analysis and forms the conceptual foundation for frequency-domain methods (Fourier and Laplace transforms), where convolution becomes multiplication.

---

## 1. Conceptual Foundation

### 1.1 The Role of Convolution in LTI System Analysis

An LTI system is completely characterized by its impulse response $h(t)$. The convolution integral provides the mechanism for computing the output $y(t)$ for any input $x(t)$:

$$
y(t) = \int_{-\infty}^{\infty} x(\tau) h(t - \tau) \, d\tau = x(t) * h(t)
$$

The operation $*$ denotes convolution. The integral expresses the following idea: the input signal $x(t)$ is decomposed into a continuum of weighted and shifted impulses via the sifting property:

$$
x(t) = \int_{-\infty}^{\infty} x(\tau) \delta(t - \tau) \, d\tau
$$

Each weighted impulse $x(\tau) \delta(t - \tau)$ produces a weighted, shifted impulse response $x(\tau) h(t - \tau)$. By linearity (superposition), the total output is the sum (integral) of these individual contributions.

### 1.2 Why Graphical Convolution Matters

For signals defined piecewise (rectangular pulses, ramps, exponentials with finite support), the convolution integral must be evaluated separately over each interval where the overlap of the two signals has a consistent form. Graphical convolution provides a systematic method for:

- Determining the piecewise intervals of $t$ where the overlap region changes.
- Visualizing the product $x(\tau) h(t - \tau)$ as a function of $\tau$.
- Computing the area under the product for each interval.

This approach is indispensable for exam problems, where signals are almost always piecewise-defined.

### 1.3 The Physical Meaning of Convolution

Convolution describes the spreading and smoothing effect of a system on an input signal:

- A system with a short impulse response (narrow $h(t)$) produces an output that closely resembles the input — the system has short memory.
- A system with a long impulse response (wide $h(t)$) produces an output that is a heavily smoothed version of the input — the system has long memory.
- The width of the output signal is the sum of the widths of the input and the impulse response: $T_y = T_x + T_h$ (the **width property**).

> **[Key Insight]**
>
> Convolution is commutative: $x(t) * h(t) = h(t) * x(t)$. This means the roles of "input" and "system" can be swapped without changing the output. In graphical convolution, you may choose which signal to reverse and shift — choose the one that makes the integration simpler.

---

## 2. Formal Definition or Model

### 2.1 The Convolution Integral

The convolution of two continuous-time signals $x(t)$ and $h(t)$ is defined as:

$$
y(t) = x(t) * h(t) = \int_{-\infty}^{\infty} x(\tau) h(t - \tau) \, d\tau
$$

An equivalent form, obtained by the change of variable $\sigma = t - \tau$, is:

$$
y(t) = \int_{-\infty}^{\infty} x(t - \sigma) h(\sigma) \, d\sigma = h(t) * x(t)
$$

### 2.2 Special Forms for Causal Signals

When both $x(t)$ and $h(t)$ are causal (zero for $t < 0$), the convolution reduces to:

$$
y(t) = \int_{0}^{t} x(\tau) h(t - \tau) \, d\tau = \int_{0}^{t} h(\tau) x(t - \tau) \, d\tau
$$

The finite limits $0$ to $t$ arise because:
- $x(\tau) = 0$ for $\tau < 0$ (causal input) — lower limit becomes $0$.
- $h(t - \tau) = 0$ for $\tau > t$ (causal system) — upper limit becomes $t$.

### 2.3 Convolution for Non-Causal or Non-Causal Systems

If the input is non-causal but the system is causal:

$$
y(t) = \int_{-\infty}^{t} x(\tau) h(t - \tau) \, d\tau
$$

If the system is non-causal (impulse response extends into $t < 0$):

$$
y(t) = \int_{-\infty}^{\infty} x(\tau) h(t - \tau) \, d\tau
$$

with no simplification of the limits.

---

## 3. Key Parameters and Constraints

### 3.1 Convolution Parameters

| Parameter | Symbol | Description | Constraints |
| :--- | :--- | :--- | :--- |
| Input signal | $x(t)$ | Signal to be convolved | Must be integrable over the region of overlap |
| Impulse response | $h(t)$ | System characterization | Must be absolutely integrable for BIBO-stable systems |
| Integration variable | $\tau$ | Dummy variable of integration | Real-valued; disappears after integration |
| Shift parameter | $t$ | Time at which output is evaluated | Determines the position of the reversed/shifted signal |
| Output | $y(t)$ | Convolution result | Duration = $T_x + T_h$ (width property) |

### 3.2 Width Property (Convolution Duration)

If $x(t)$ has finite duration $T_x$ (i.e., $x(t) = 0$ for $t$ outside an interval of length $T_x$) and $h(t)$ has finite duration $T_h$, then $y(t) = x(t) * h(t)$ has finite duration $T_y = T_x + T_h$.

| Input Duration | Impulse Response Duration | Output Duration |
| :--- | :--- | :--- |
| $T_x$ | $T_h$ | $T_x + T_h$ |
| Finite | Finite | Finite |
| Finite | Infinite | Infinite |
| Infinite | Finite | Infinite |
| Infinite | Infinite | Infinite |

> **[Supplementary]**
>
> The width property holds more generally: if $x(t)$ is supported on $[a, b]$ and $h(t)$ on $[c, d]$, then $y(t)$ is supported on $[a + c, b + d]$. For causal signals ($a = c = 0$), the output support is $[0, b + d]$.

### 3.3 Continuity Property

Even if $x(t)$ and $h(t)$ are discontinuous (e.g., rectangular pulses), their convolution $y(t)$ is always a continuous function. Discontinuities in the individual signals produce piecewise-defined outputs, but the boundaries between pieces match continuously.

---

## 4. Step-by-Step Mechanism

### 4.1 The Graphical Convolution Procedure

The graphical method consists of four operations performed on the functions $x(\tau)$ and $h(t-\tau)$ as functions of $\tau$:

#### Step 1: Time Reversal (Reflection)

Replace $h(\tau)$ with $h(-\tau)$. Graphically, this means reflecting $h$ about the vertical axis ($\tau = 0$). The result is $h(-\tau)$.

#### Step 2: Time Shifting (Sliding)

Shift the reversed signal by $t$ to obtain $h(t - \tau) = h(-(\tau - t))$. Graphically:
- For $t > 0$, the reversed signal slides to the right by $t$.
- For $t < 0$, the reversed signal slides to the left by $|t|$.

#### Step 3: Multiplication (Overlap Product)

For a fixed $t$, compute the product $x(\tau) \cdot h(t - \tau)$ for each $\tau$. Graphically, this is the pointwise product of the two functions plotted on the same $\tau$ axis.

#### Step 4: Integration (Area Calculation)

Compute the area under the product $x(\tau) h(t - \tau)$ with respect to $\tau$. This area is the value of $y(t)$ for the chosen $t$.

Repeat Steps 2-4 for all values of $t$ to obtain $y(t)$ over its entire domain.

### 4.2 Systematic Method for Determining Piecewise Intervals

1. **Identify breakpoints** of $x(\tau)$ and $h(\tau)$ — the points where the functional form changes.
2. **Express the support of $h(t - \tau)$ in $\tau$** — if $h(\tau)$ is supported on $[c, d]$, then $h(t - \tau)$ is supported on $\tau \in [t - d, t - c]$.
3. **Determine the overlap interval** as the intersection of the support of $x(\tau)$ and the support of $h(t - \tau)$.
4. **Find the critical values of $t$** where the overlap region changes. These are the breakpoints of $y(t)$.
5. **Evaluate the integral** over each interval, using the appropriate functional forms.

### 4.3 Number of Piecewise Cases

For two piecewise-defined signals, the number of piecewise intervals for $y(t)$ is at most $N + 1$, where $N$ is the total number of distinct breakpoints contributed by both signals.

---

## 5. Solved Exercises

### Exercise 1: Convolution of Two Rectangular Pulses (Graphical Method)

**Problem:** Compute $y(t) = x(t) * h(t)$ using the graphical method, where:
$$
x(t) =
\begin{cases}
1, & 0 \le t \le 3 \\
0, & \text{otherwise}
\end{cases}
\quad
h(t) =
\begin{cases}
2, & 0 \le t \le 1 \\
0, & \text{otherwise}
\end{cases}
$$

**Solution:**

**Step 1:** Express both signals. $x(t)$ is a rectangle of height 1 over $[0, 3]$. $h(t)$ is a rectangle of height 2 over $[0, 1]$.

**Step 2:** Write the convolution integral:
$$
y(t) = \int_{-\infty}^{\infty} x(\tau) h(t - \tau) \, d\tau
$$

The support of $x(\tau)$ is $[0, 3]$. The support of $h(t - \tau)$ in $\tau$ is found from $h(\tau)$ supported on $[0, 1]$: $h(t - \tau)$ is supported where $0 \le t - \tau \le 1$, i.e., $\tau \in [t - 1, t]$.

**Step 3:** Determine piecewise intervals based on the overlap of $[0, 3]$ and $[t - 1, t]$.

**Case 1:** $t < 0$ — No overlap because $[t - 1, t]$ is entirely to the left of $[0, 3]$. $y(t) = 0$.

**Case 2:** $0 \le t < 1$ — Partial overlap entering. Overlap region: $\tau \in [0, t]$.
$$
y(t) = \int_{0}^{t} 1 \cdot 2 \, d\tau = 2t
$$

**Case 3:** $1 \le t < 3$ — Full overlap. The interval $[t - 1, t]$ is fully within $[0, 3]$. Overlap region: $\tau \in [t - 1, t]$.
$$
y(t) = \int_{t-1}^{t} 1 \cdot 2 \, d\tau = 2[t - (t - 1)] = 2
$$

**Case 4:** $3 \le t < 4$ — Partial overlap exiting. The interval $[t - 1, t]$ extends beyond $3$ on the left (since $t - 1 < 3 < t$). Overlap region: $\tau \in [t - 1, 3]$.
$$
y(t) = \int_{t-1}^{3} 1 \cdot 2 \, d\tau = 2[3 - (t - 1)] = 2(4 - t)
$$

**Case 5:** $t \ge 4$ — No overlap because $[t - 1, t]$ is entirely to the right of $[0, 3]$. $y(t) = 0$.

**Step 4:** The complete result:
$$
y(t) =
\begin{cases}
0, & t < 0 \\
2t, & 0 \le t < 1 \\
2, & 1 \le t < 3 \\
2(4 - t), & 3 \le t < 4 \\
0, & t \ge 4
\end{cases}
$$

*Verification:* Output duration $T_y = 4 = T_x + T_h = 3 + 1 = 4$. The output is a trapezoidal pulse. At $t = 1$, the two pieces give $y(1) = 2(1) = 2$ and $y(1) = 2$, confirming continuity. At $t = 3$, $y(3) = 2$ and $y(3) = 2(4 - 3) = 2$, confirming continuity.

---

### Exercise 2: Convolution of a Rectangle and a Triangle

**Problem:** Compute $y(t) = x(t) * h(t)$ where:
$$
x(t) =
\begin{cases}
1, & 0 \le t \le 2 \\
0, & \text{otherwise}
\end{cases}
\quad
h(t) =
\begin{cases}
t, & 0 \le t \le 2 \\
0, & \text{otherwise}
\end{cases}
$$

**Solution:**

**Step 1:** $x(\tau)$ is supported on $[0, 2]$ with value $1$. $h(t - \tau)$ is supported on $\tau \in [t - 2, t]$ with value $t - \tau$ (since $h(\tau) = \tau$ implies $h(t - \tau) = t - \tau$).

**Step 2:** Determine intervals by considering the overlap of $[0, 2]$ and $[t - 2, t]$.

**Case 1:** $t < 0$ — No overlap. $y(t) = 0$.

**Case 2:** $0 \le t < 2$ — Overlap region: $\tau \in [0, t]$.
$$
y(t) = \int_{0}^{t} 1 \cdot (t - \tau) \, d\tau = \left[t\tau - \frac{\tau^2}{2}\right]_{0}^{t} = t^2 - \frac{t^2}{2} = \frac{t^2}{2}
$$

**Case 3:** $2 \le t < 4$ — Overlap region: $\tau \in [t - 2, 2]$.
$$
y(t) = \int_{t-2}^{2} 1 \cdot (t - \tau) \, d\tau = \left[t\tau - \frac{\tau^2}{2}\right]_{t-2}^{2}
$$

Evaluate at $\tau = 2$: $2t - 2$.
Evaluate at $\tau = t - 2$: $t(t - 2) - \frac{(t - 2)^2}{2} = t^2 - 2t - \frac{t^2 - 4t + 4}{2} = t^2 - 2t - \frac{t^2}{2} + 2t - 2 = \frac{t^2}{2} - 2$.

Subtract:
$$
y(t) = (2t - 2) - \left(\frac{t^2}{2} - 2\right) = 2t - 2 - \frac{t^2}{2} + 2 = 2t - \frac{t^2}{2}
$$

**Case 4:** $t \ge 4$ — No overlap. $y(t) = 0$.

**Step 3:** The complete result:
$$
y(t) =
\begin{cases}
0, & t < 0 \\
\frac{t^2}{2}, & 0 \le t < 2 \\
2t - \frac{t^2}{2}, & 2 \le t < 4 \\
0, & t \ge 4
\end{cases}
$$

*Verification:* At $t = 2$, both pieces give $y(2) = 2^2/2 = 2$ and $y(2) = 2(2) - 2^2/2 = 4 - 2 = 2$. Output duration $T_y = 4 = 2 + 2 = T_x + T_h$.

---

### Exercise 3: Convolution of an Exponential and a Rectangular Pulse

**Problem:** Compute $y(t) = x(t) * h(t)$ where $x(t) = e^{-2t} u(t)$ and $h(t) = u(t) - u(t - 3)$.

**Solution:**

**Step 1:** $x(t) = e^{-2t} u(t)$ is a causal exponential. $h(t)$ is a rectangular pulse of height 1 over $[0, 3]$.

**Step 2:** The support of $h(t - \tau)$ in $\tau$ is $\tau \in [t - 3, t]$. Since both signals are causal, the lower integration limit cannot be less than 0.

**Case 1:** $t < 0$ — No overlap. $y(t) = 0$.

**Case 2:** $0 \le t < 3$ — Overlap region: $\tau \in [0, t]$.
$$
y(t) = \int_{0}^{t} e^{-2\tau} \cdot 1 \, d\tau = \left[-\frac{e^{-2\tau}}{2}\right]_{0}^{t} = \frac{1}{2}(1 - e^{-2t})
$$

**Case 3:** $t \ge 3$ — Overlap region: $\tau \in [t - 3, t]$, but since $x(\tau) = 0$ for $\tau < 0$, and for $t \ge 3$, we have $t - 3 \ge 0$, so the overlap is $\tau \in [t - 3, t]$. However, $h(t - \tau) = 1$ only when $0 \le t - \tau \le 3$, i.e., $\tau \in [t - 3, t]$. For $\tau > t$, $h(t - \tau) = 0$. So the overlap is $\tau \in [t - 3, t]$, and the upper limit is actually $t$, but $x(\tau)$ is nonzero for all $\tau \ge 0$.
$$
y(t) = \int_{t-3}^{t} e^{-2\tau} \cdot 1 \, d\tau = \left[-\frac{e^{-2\tau}}{2}\right]_{t-3}^{t} = -\frac{e^{-2t}}{2} + \frac{e^{-2(t-3)}}{2}
$$
$$
y(t) = \frac{1}{2}\left(e^{-2t + 6} - e^{-2t}\right) = \frac{1}{2}e^{-2t}(e^{6} - 1)
$$

**Step 4:** The complete result:
$$
y(t) =
\begin{cases}
0, & t < 0 \\
\frac{1}{2}(1 - e^{-2t}), & 0 \le t < 3 \\
\frac{1}{2}e^{-2t}(e^{6} - 1), & t \ge 3
\end{cases}
$$

*Verification:* At $t = 3$, both pieces give $y(3) = \frac{1}{2}(1 - e^{-6})$ and $y(3) = \frac{1}{2}e^{-6}(e^{6} - 1) = \frac{1}{2}(1 - e^{-6})$, confirming continuity.

---

### Exercise 4: Convolution with a Unit Step Function

**Problem:** Compute $y(t) = u(t) * u(t)$ where $u(t)$ is the unit step function.

**Solution:**

**Step 1:** Write the convolution integral. Both signals are causal:
$$
y(t) = \int_{0}^{t} u(\tau) u(t - \tau) \, d\tau
$$

**Step 2:** For $\tau \in [0, t]$, $u(\tau) = 1$ and $u(t - \tau) = 1$ (since $t - \tau \ge 0$).
$$
y(t) = \int_{0}^{t} 1 \cdot 1 \, d\tau = t, \quad t \ge 0
$$

**Step 3:** For $t < 0$, the convolution is zero. The complete result:
$$
y(t) = t \cdot u(t) = r(t)
$$

where $r(t)$ is the unit ramp function.

*Interpretation:* The convolution of two unit steps produces a unit ramp. This is a fundamental result: integrating twice (the step is the integral of the impulse) produces a ramp (the double integral of the impulse).

> **[Key Insight]**
>
> The pattern generalizes: $\underbrace{u(t) * u(t) * \cdots * u(t)}_{n \text{ times}} = \frac{t^{n-1}}{(n-1)!} u(t)$. This is the convolution equivalent of repeated integration.

---

### Exercise 5: Convolution of a Sine Wave and an Exponential (Steady-State and Transient)

**Problem:** Compute $y(t) = x(t) * h(t)$ where $x(t) = \sin(\omega_0 t) u(t)$ and $h(t) = e^{-at} u(t)$ with $a > 0$.

**Solution:**

**Step 1:** Both signals are causal. Write the convolution integral:
$$
y(t) = \int_{0}^{t} \sin(\omega_0 \tau) e^{-a(t - \tau)} \, d\tau = e^{-at} \int_{0}^{t} \sin(\omega_0 \tau) e^{a\tau} \, d\tau
$$

**Step 2:** Evaluate $I = \int_{0}^{t} e^{a\tau} \sin(\omega_0 \tau) \, d\tau$ using the standard formula:
$$
\int e^{a\tau} \sin(b\tau) \, d\tau = \frac{e^{a\tau}}{a^2 + b^2} \big(a \sin(b\tau) - b \cos(b\tau)\big)
$$

With $a$ (the exponential rate) and $b = \omega_0$:
$$
I = \left[\frac{e^{a\tau}}{a^2 + \omega_0^2} \big(a \sin(\omega_0 \tau) - \omega_0 \cos(\omega_0 \tau)\big)\right]_{0}^{t}
$$

**Step 3:** Evaluate the limits:
At $\tau = t$:
$$
\frac{e^{at}}{a^2 + \omega_0^2} \big(a \sin(\omega_0 t) - \omega_0 \cos(\omega_0 t)\big)
$$

At $\tau = 0$:
$$
\frac{1}{a^2 + \omega_0^2} (0 - \omega_0) = -\frac{\omega_0}{a^2 + \omega_0^2}
$$

Therefore:
$$
I = \frac{e^{at}}{a^2 + \omega_0^2} \big(a \sin(\omega_0 t) - \omega_0 \cos(\omega_0 t)\big) + \frac{\omega_0}{a^2 + \omega_0^2}
$$

**Step 4:** Multiply by $e^{-at}$:
$$
y(t) = \frac{1}{a^2 + \omega_0^2} \big(a \sin(\omega_0 t) - \omega_0 \cos(\omega_0 t)\big) + \frac{\omega_0}{a^2 + \omega_0^2} e^{-at}
$$

**Step 5:** Combine the sinusoidal terms. Let $\phi = \tan^{-1}(\omega_0 / a)$. Then:
$$
a \sin(\omega_0 t) - \omega_0 \cos(\omega_0 t) = \sqrt{a^2 + \omega_0^2} \, \sin(\omega_0 t - \phi)
$$

where $\phi = \tan^{-1}(\omega_0 / a)$.

**Step 6:** The complete result:
$$
y(t) = \left[\frac{1}{\sqrt{a^2 + \omega_0^2}} \sin(\omega_0 t - \phi) + \frac{\omega_0}{a^2 + \omega_0^2} e^{-at}\right] u(t)
$$

*Interpretation:* The output consists of two parts:
- **Steady-state response:** A sinusoid at the input frequency $\omega_0$, with amplitude $1/\sqrt{a^2 + \omega_0^2}$ and phase shift $-\phi$ (lag).
- **Transient response:** An exponential term $\frac{\omega_0}{a^2 + \omega_0^2} e^{-at}$ that decays to zero as $t \to \infty$.

As $a \to 0^+$ (the system approaches a pure integrator), the amplitude becomes $1/\omega_0$ and the phase shift approaches $-\pi/2$, consistent with $\int \sin(\omega_0 t) \, dt = -\frac{1}{\omega_0} \cos(\omega_0 t)$.

---

### Exercise 6: Convolution Using the Commutative Property to Simplify

**Problem:** Compute $y(t) = x(t) * h(t)$ where:
$$
x(t) = e^{-t} u(t), \quad h(t) = t e^{-2t} u(t)
$$

Use the commutative property to choose the easier order.

**Solution:**

**Step 1:** By commutativity, $x(t) * h(t) = h(t) * x(t)$. The convolution $h(t) * x(t)$ requires integrating $h(\tau) x(t - \tau) = \tau e^{-2\tau} \cdot e^{-(t-\tau)} = \tau e^{-2\tau} e^{-t} e^{\tau} = \tau e^{-t} e^{-\tau}$.

**Step 2:** Compute $y(t) = e^{-t} \int_{0}^{t} \tau e^{-\tau} \, d\tau$ for $t \ge 0$.

**Step 3:** Evaluate $\int_{0}^{t} \tau e^{-\tau} \, d\tau$ using integration by parts:
Let $u = \tau$, $dv = e^{-\tau} d\tau$. Then $du = d\tau$, $v = -e^{-\tau}$.
$$
\int_{0}^{t} \tau e^{-\tau} \, d\tau = \left[-\tau e^{-\tau}\right]_{0}^{t} + \int_{0}^{t} e^{-\tau} \, d\tau
$$
$$
= (-t e^{-t} - 0) + \left[-e^{-\tau}\right]_{0}^{t} = -t e^{-t} + (-e^{-t} + 1) = 1 - e^{-t}(t + 1)
$$

**Step 4:** The result:
$$
y(t) = \left[e^{-t} \big(1 - e^{-t}(t + 1)\big)\right] u(t) = \left[e^{-t} - (t + 1) e^{-2t}\right] u(t)
$$

*Verification:* At $t = 0$, $y(0) = 1 - 1 = 0$, which is correct since both signals are zero at $t = 0$ (the exponential starts at $1$, but the product $x(\tau) h(t - \tau)$ at $t = 0$ has zero integration interval).

---

### Exercise 7: Convolution of Two Causal Exponentials

**Problem:** Compute $y(t) = h_1(t) * h_2(t)$ where $h_1(t) = e^{-\alpha t} u(t)$ and $h_2(t) = e^{-\beta t} u(t)$, with $\alpha \neq \beta$.

**Solution:**

**Step 1:** Both are causal. Write the convolution integral:
$$
y(t) = \int_{0}^{t} e^{-\alpha \tau} e^{-\beta (t - \tau)} \, d\tau = e^{-\beta t} \int_{0}^{t} e^{-(\alpha - \beta)\tau} \, d\tau
$$

**Step 2:** Evaluate the integral. Since $\alpha \neq \beta$:
$$
\int_{0}^{t} e^{-(\alpha - \beta)\tau} \, d\tau = \left[-\frac{e^{-(\alpha - \beta)\tau}}{\alpha - \beta}\right]_{0}^{t} = \frac{1 - e^{-(\alpha - \beta)t}}{\alpha - \beta}
$$

**Step 3:** The result:
$$
y(t) = \frac{e^{-\beta t} - e^{-\alpha t}}{\alpha - \beta} \, u(t)
$$

*Special case:* When $\alpha = \beta$, apply L'Hopital's rule or compute directly:
$$
y(t) = \int_{0}^{t} e^{-\alpha \tau} e^{-\alpha (t - \tau)} \, d\tau = e^{-\alpha t} \int_{0}^{t} 1 \, d\tau = t e^{-\alpha t} u(t)
$$

> **[Supplementary]**
>
> The formula $\frac{e^{-\beta t} - e^{-\alpha t}}{\alpha - \beta}$ for $\alpha \neq \beta$ and $t e^{-\alpha t}$ for $\alpha = \beta$ is a standard result worth memorizing. It appears frequently in the analysis of cascaded first-order systems: the impulse response of two first-order systems in series is the convolution of their individual impulse responses.

---

### Exercise 8: Convolution with the Delta Function (Identity and Shifting)

**Problem:** Compute:
(a) $x(t) * \delta(t)$
(b) $x(t) * \delta(t - t_0)$
(c) $\delta(t - t_1) * \delta(t - t_2)$
(d) $[x(t) * \delta'(t)]$

**Solution:**

**(a)** $x(t) * \delta(t)$:
$$
x(t) * \delta(t) = \int_{-\infty}^{\infty} x(\tau) \delta(t - \tau) \, d\tau = x(t)
$$

The delta function is the **identity element** for convolution: convolving any signal with $\delta(t)$ leaves it unchanged.

**(b)** $x(t) * \delta(t - t_0)$:
$$
x(t) * \delta(t - t_0) = \int_{-\infty}^{\infty} x(\tau) \delta(t - \tau - t_0) \, d\tau
$$
Let $\sigma = t - \tau - t_0$, then $d\sigma = -d\tau$, but it is easier to use the sifting property directly: the delta selects $\tau$ such that $t - \tau - t_0 = 0$, i.e., $\tau = t - t_0$.
$$
x(t) * \delta(t - t_0) = x(t - t_0)
$$

Convolution with a shifted delta produces a shifted version of the signal.

**(c)** $\delta(t - t_1) * \delta(t - t_2)$:
$$
\delta(t - t_1) * \delta(t - t_2) = \int_{-\infty}^{\infty} \delta(\tau - t_1) \delta(t - \tau - t_2) \, d\tau = \delta(t - (t_1 + t_2))
$$

The convolution of two shifted deltas is a delta at the sum of the shifts.

**(d)** $x(t) * \delta'(t)$:
$$
x(t) * \delta'(t) = \int_{-\infty}^{\infty} x(\tau) \delta'(t - \tau) \, d\tau = \frac{dx}{dt}
$$

Convolution with the derivative of the delta function produces the derivative of the signal.

---

### Exercise 9: Convolution of Two Piecewise-Defined Signals with Different Supports

**Problem:** Compute $y(t) = x(t) * h(t)$ where:
$$
x(t) =
\begin{cases}
t, & 0 \le t \le 1 \\
2 - t, & 1 \le t \le 2 \\
0, & \text{otherwise}
\end{cases}
\quad
h(t) =
\begin{cases}
1, & 0 \le t \le 1 \\
0, & \text{otherwise}
\end{cases}
$$

**Solution:**

**Step 1:** $x(t)$ is a triangular pulse (height 1 at $t = 1$, zero at $t = 0$ and $t = 2$) supported on $[0, 2]$. $h(t)$ is a rectangular pulse supported on $[0, 1]$.

**Step 2:** The support of $h(t - \tau)$ in $\tau$ is $\tau \in [t - 1, t]$. The support of $x(\tau)$ is $[0, 2]$. The output support will be $[0, 3]$.

**Step 3:** Determine the piecewise intervals. The critical points come from the breakpoints of $x$ ($0, 1, 2$) and the edges of the sliding window ($t - 1$ and $t$).

**Case 1:** $t < 0$ — No overlap. $y(t) = 0$.

**Case 2:** $0 \le t < 1$ — Overlap on $\tau \in [0, t]$. On this interval, $x(\tau) = \tau$.
$$
y(t) = \int_{0}^{t} \tau \cdot 1 \, d\tau = \frac{t^2}{2}
$$

**Case 3:** $1 \le t < 2$ — Overlap on $\tau \in [t - 1, t]$. This interval spans the point $\tau = 1$ where $x(\tau)$ changes form. Split the integral:
For $\tau \in [t - 1, 1]$, $x(\tau) = \tau$. For $\tau \in [1, t]$, $x(\tau) = 2 - \tau$.

$$
y(t) = \int_{t-1}^{1} \tau \, d\tau + \int_{1}^{t} (2 - \tau) \, d\tau
$$

First integral:
$$
\int_{t-1}^{1} \tau \, d\tau = \left[\frac{\tau^2}{2}\right]_{t-1}^{1} = \frac{1}{2} - \frac{(t-1)^2}{2} = \frac{1 - (t^2 - 2t + 1)}{2} = \frac{2t - t^2}{2}
$$

Second integral:
$$
\int_{1}^{t} (2 - \tau) \, d\tau = \left[2\tau - \frac{\tau^2}{2}\right]_{1}^{t} = \left(2t - \frac{t^2}{2}\right) - \left(2 - \frac{1}{2}\right) = 2t - \frac{t^2}{2} - \frac{3}{2}
$$

Sum:
$$
y(t) = \frac{2t - t^2}{2} + 2t - \frac{t^2}{2} - \frac{3}{2} = \frac{2t - t^2}{2} + \frac{4t - t^2 - 3}{2} = \frac{6t - 2t^2 - 3}{2}
$$

**Case 4:** $2 \le t < 3$ — Overlap on $\tau \in [t - 1, 2]$. For all $\tau$ in this interval, $x(\tau) = 2 - \tau$.
$$
y(t) = \int_{t-1}^{2} (2 - \tau) \cdot 1 \, d\tau = \left[2\tau - \frac{\tau^2}{2}\right]_{t-1}^{2}
$$

At $\tau = 2$: $4 - 2 = 2$.
At $\tau = t - 1$: $2(t - 1) - \frac{(t - 1)^2}{2} = 2t - 2 - \frac{t^2 - 2t + 1}{2} = 2t - 2 - \frac{t^2}{2} + t - \frac{1}{2} = 3t - \frac{t^2}{2} - \frac{5}{2}$.

$$
y(t) = 2 - \left(3t - \frac{t^2}{2} - \frac{5}{2}\right) = 2 - 3t + \frac{t^2}{2} + \frac{5}{2} = \frac{t^2}{2} - 3t + \frac{9}{2}
$$

**Case 5:** $t \ge 3$ — No overlap. $y(t) = 0$.

**Step 4:** The complete result:
$$
y(t) =
\begin{cases}
0, & t < 0 \\
\frac{t^2}{2}, & 0 \le t < 1 \\
\frac{6t - 2t^2 - 3}{2}, & 1 \le t < 2 \\
\frac{t^2}{2} - 3t + \frac{9}{2}, & 2 \le t < 3 \\
0, & t \ge 3
\end{cases}
$$

*Verification:* At $t = 1$: Case 2 gives $1/2$. Case 3 gives $(6 - 2 - 3)/2 = 1/2$. At $t = 2$: Case 3 gives $(12 - 8 - 3)/2 = 1/2$. Case 4 gives $(4/2 - 6 + 9/2) = 2 - 6 + 4.5 = 0.5 = 1/2$. Continuity confirmed. Output duration $T_y = 3 = 2 + 1 = T_x + T_h$.

---

### Exercise 10: Verifying the Associative Property

**Problem:** Let $x(t) = u(t)$, $h_1(t) = e^{-t} u(t)$, and $h_2(t) = e^{-2t} u(t)$. Verify that $(x * h_1) * h_2 = x * (h_1 * h_2)$.

**Solution:**

**Step 1:** Compute $x * h_1$ first:
$$
(x * h_1)(t) = \int_{0}^{t} 1 \cdot e^{-(t - \tau)} \, d\tau = e^{-t} \int_{0}^{t} e^{\tau} \, d\tau = e^{-t}(e^{t} - 1) = 1 - e^{-t}, \quad t \ge 0
$$

**Step 2:** Compute $(x * h_1) * h_2$:
$$
((x * h_1) * h_2)(t) = \int_{0}^{t} (1 - e^{-\tau}) e^{-2(t - \tau)} \, d\tau = e^{-2t} \int_{0}^{t} (e^{2\tau} - e^{\tau}) \, d\tau
$$

Evaluate:
$$
e^{-2t} \left[ \frac{e^{2\tau}}{2} - e^{\tau} \right]_{0}^{t} = e^{-2t} \left[ \left(\frac{e^{2t}}{2} - e^{t}\right) - \left(\frac{1}{2} - 1\right) \right]
$$
$$
= e^{-2t} \left( \frac{e^{2t}}{2} - e^{t} + \frac{1}{2} \right) = \frac{1}{2} - e^{-t} + \frac{1}{2} e^{-2t}
$$

**Step 3:** Compute $h_1 * h_2$ first (using the result from Exercise 7 with $\alpha = 1$, $\beta = 2$):
$$
(h_1 * h_2)(t) = \frac{e^{-t} - e^{-2t}}{1} = e^{-t} - e^{-2t}, \quad t \ge 0
$$

**Step 4:** Compute $x * (h_1 * h_2)$:
$$
(x * (h_1 * h_2))(t) = \int_{0}^{t} 1 \cdot (e^{-(t - \tau)} - e^{-2(t - \tau)}) \, d\tau = \int_{0}^{t} e^{-(t - \tau)} \, d\tau - \int_{0}^{t} e^{-2(t - \tau)} \, d\tau
$$

First integral: $\int_{0}^{t} e^{-(t - \tau)} \, d\tau = 1 - e^{-t}$ (from Step 1).
Second integral: $\int_{0}^{t} e^{-2(t - \tau)} \, d\tau = e^{-2t} \int_{0}^{t} e^{2\tau} \, d\tau = e^{-2t} \cdot \frac{e^{2t} - 1}{2} = \frac{1 - e^{-2t}}{2}$.

Therefore:
$$
(x * (h_1 * h_2))(t) = (1 - e^{-t}) - \frac{1 - e^{-2t}}{2} = 1 - e^{-t} - \frac{1}{2} + \frac{e^{-2t}}{2} = \frac{1}{2} - e^{-t} + \frac{1}{2} e^{-2t}
$$

**Step 5:** Both orders give the same result, verifying the associative property.

---

### Exercise 11: Convolution of Even and Odd Signal Decompositions

**Problem:** Let $x(t)$ be an arbitrary signal and $h(t)$ be an even function ($h(-t) = h(t)$). Show that $y(t) = x(t) * h(t)$ can be expressed as $y(t) = x_e(t) * h(t)$ where $x_e(t)$ is the even part of $x(t)$.

**Solution:**

**Step 1:** Decompose $x(t)$ into even and odd parts:
$$
x(t) = x_e(t) + x_o(t)
$$
where
$$
x_e(t) = \frac{x(t) + x(-t)}{2}, \quad x_o(t) = \frac{x(t) - x(-t)}{2}
$$

**Step 2:** By the distributive property:
$$
y(t) = x_e(t) * h(t) + x_o(t) * h(t)
$$

**Step 3:** Consider $x_o(t) * h(t)$. Since $h$ is even, show that the odd part contributes zero. Write:
$$
(x_o * h)(t) = \int_{-\infty}^{\infty} x_o(\tau) h(t - \tau) \, d\tau
$$

Change variable $\sigma = -\tau$:
$$
(x_o * h)(t) = \int_{-\infty}^{\infty} x_o(-\sigma) h(t + \sigma) \, d\sigma
$$

Since $x_o$ is odd, $x_o(-\sigma) = -x_o(\sigma)$. Since $h$ is even, $h(t + \sigma) = h(-(t + \sigma)) = h(-t - \sigma)$.

But we need a more direct approach. Consider $y(-t)$:
$$
y(-t) = \int_{-\infty}^{\infty} x(\tau) h(-t - \tau) \, d\tau
$$

Change variable $\sigma = -\tau$:
$$
y(-t) = \int_{-\infty}^{\infty} x(-\sigma) h(-t + \sigma) \, d\sigma
$$

Since $h$ is even, $h(-t + \sigma) = h(t - \sigma)$. So:
$$
y(-t) = \int_{-\infty}^{\infty} x(-\sigma) h(t - \sigma) \, d\sigma
$$

Now decompose $x(-\sigma) = x_e(\sigma) - x_o(\sigma)$. Then:
$$
y(-t) = \int_{-\infty}^{\infty} (x_e(\sigma) - x_o(\sigma)) h(t - \sigma) \, d\sigma = (x_e * h)(t) - (x_o * h)(t)
$$

But $y(t) = (x_e * h)(t) + (x_o * h)(t)$. For $y(t) = y(-t)$ (i.e., $y$ is even), we need $(x_o * h)(t) = 0$.

**Step 4:** For an even $h$, the convolution of an odd $x_o$ with $h$ is always zero. Proof:
$$
(x_o * h)(t) = \int_{-\infty}^{\infty} x_o(\tau) h(t - \tau) \, d\tau
$$

Split the integral at $\tau = 0$ and change variable $\sigma = -\tau$ in the negative part:
$$
(x_o * h)(t) = \int_{0}^{\infty} x_o(\tau) h(t - \tau) \, d\tau + \int_{0}^{\infty} x_o(-\sigma) h(t + \sigma) \, d\sigma
$$

Since $x_o$ is odd, $x_o(-\sigma) = -x_o(\sigma)$:
$$
(x_o * h)(t) = \int_{0}^{\infty} x_o(\tau) h(t - \tau) \, d\tau - \int_{0}^{\infty} x_o(\sigma) h(t + \sigma) \, d\sigma
$$

For $h$ even, $h(t + \sigma) = h(-(t + \sigma))$. This does not generally equal $h(t - \sigma)$. The result that $x_o * h = 0$ for even $h$ requires an additional symmetry. In fact, the correct statement is: if $h$ is even, then $y(t) = x(t) * h(t)$ is even if and only if $x$ is even.

The claim in the problem statement is therefore only true in general if $x$ itself is even. The more precise result is:

> **[Supplementary]**
>
> For an even impulse response $h(t)$, the system output $y(t) = x(t) * h(t)$ preserves the even/odd decomposition property: the even part of $x$ contributes to the even part of $y$, and the odd part of $x$ contributes to the odd part of $y$. This follows from the fact that convolution with an even function is an even operator: if $x$ is even, $x * h$ is even; if $x$ is odd, $x * h$ is odd.

---

### Exercise 12: Convolution Using the Distributive Property

**Problem:** Use the distributive property to compute $y(t) = x(t) * h(t)$ where $x(t) = u(t) - u(t-1)$ and $h(t) = e^{-t} u(t) + \delta(t-2)$.

**Solution:**

**Step 1:** By the distributive property, convolution distributes over addition:
$$
x(t) * (h_1(t) + h_2(t)) = x(t) * h_1(t) + x(t) * h_2(t)
$$

So decompose $h(t) = h_1(t) + h_2(t)$ where $h_1(t) = e^{-t} u(t)$ and $h_2(t) = \delta(t-2)$.

**Step 2:** Compute $y_1(t) = x(t) * e^{-t} u(t)$ (convolution of a unit rectangle with a causal exponential).

$x(t)$ is supported on $[0, 1]$. For $t < 0$, $y_1(t) = 0$.

For $0 \le t < 1$:
$$
y_1(t) = \int_{0}^{t} 1 \cdot e^{-(t - \tau)} \, d\tau = e^{-t} \int_{0}^{t} e^{\tau} \, d\tau = e^{-t}(e^{t} - 1) = 1 - e^{-t}
$$

For $t \ge 1$:
$$
y_1(t) = \int_{0}^{1} 1 \cdot e^{-(t - \tau)} \, d\tau = e^{-t} \int_{0}^{1} e^{\tau} \, d\tau = e^{-t}(e - 1)
$$

Thus:
$$
y_1(t) =
\begin{cases}
0, & t < 0 \\
1 - e^{-t}, & 0 \le t < 1 \\
(e - 1) e^{-t}, & t \ge 1
\end{cases}
$$

**Step 3:** Compute $y_2(t) = x(t) * \delta(t-2) = x(t-2)$ (shifting property). Since $x(t) = u(t) - u(t-1)$:
$$
y_2(t) = x(t-2) = u(t-2) - u(t-3)
$$

This is a unit rectangle over $[2, 3]$.

**Step 4:** The total output is $y(t) = y_1(t) + y_2(t)$:
$$
y(t) =
\begin{cases}
0, & t < 0 \\
1 - e^{-t}, & 0 \le t < 1 \\
(e - 1) e^{-t}, & 1 \le t < 2 \\
(e - 1) e^{-t} + 1, & 2 \le t < 3 \\
(e - 1) e^{-t}, & t \ge 3
\end{cases}
$$

*Verification:* At $t = 2$: $y(2) = (e - 1)e^{-2}$ from the first piece and $y(2) = (e - 1)e^{-2} + 1$ from the second piece. Since $y_2(2) = x(0) = 1$, the jump at $t = 2$ is correct — $y_2$ contributes $1$ starting at $t = 2$.

---

## 6. Properties of Convolution

### 6.1 Algebraic Properties

| Property | Definition | Implication |
| :--- | :--- | :--- |
| **Commutative** | $x(t) * h(t) = h(t) * x(t)$ | The roles of input and system are interchangeable |
| **Associative** | $x * (h_1 * h_2) = (x * h_1) * h_2$ | Cascaded LTI systems have an equivalent impulse response $h_{\text{eq}} = h_1 * h_2$ |
| **Distributive** | $x * (h_1 + h_2) = x * h_1 + x * h_2$ | Parallel LTI systems have an equivalent impulse response $h_{\text{eq}} = h_1 + h_2$ |

### 6.2 Identity and Shifting Properties

| Operation | Result |
| :--- | :--- |
| $x(t) * \delta(t)$ | $x(t)$ |
| $x(t) * \delta(t - t_0)$ | $x(t - t_0)$ |
| $\delta(t - t_1) * \delta(t - t_2)$ | $\delta(t - (t_1 + t_2))$ |
| $x(t) * \delta'(t)$ | $\frac{dx}{dt}$ |
| $x(t) * \delta^{(n)}(t)$ | $\frac{d^n x}{dt^n}$ |
| $\frac{dx}{dt} * h(t)$ | $\frac{d}{dt}(x(t) * h(t))$ |

### 6.3 Homogeneity Property

For any scalar $\alpha$:
$$
(\alpha x(t)) * h(t) = \alpha (x(t) * h(t)) = x(t) * (\alpha h(t))
$$

### 6.4 Width Property

If $x(t)$ is supported on $[a, b]$ and $h(t)$ is supported on $[c, d]$, then $y(t) = x(t) * h(t)$ is supported on $[a + c, b + d]$.

### 6.5 Differentiation Property

$$
\frac{d}{dt}\big(x(t) * h(t)\big) = \frac{dx}{dt} * h(t) = x(t) * \frac{dh}{dt}
$$

This property allows convolution to be simplified by differentiating one signal and integrating the other (a form of integration by parts applied to convolution).

### 6.6 Convolution Table of Common Pairs

| $x(t)$ | $h(t)$ | $x(t) * h(t)$ |
| :--- | :--- | :--- |
| $x(t)$ | $\delta(t)$ | $x(t)$ |
| $x(t)$ | $\delta(t - t_0)$ | $x(t - t_0)$ |
| $e^{at} u(t)$ | $e^{bt} u(t)$ | $\frac{e^{at} - e^{bt}}{a - b} u(t)$, $a \neq b$ |
| $e^{at} u(t)$ | $e^{at} u(t)$ | $t e^{at} u(t)$ |
| $u(t)$ | $u(t)$ | $t u(t) = r(t)$ |
| $u(t)$ | $t u(t)$ | $\frac{t^2}{2} u(t)$ |
| $u(t)$ | $e^{at} u(t)$ | $\frac{e^{at} - 1}{a} u(t)$ |
| $t u(t)$ | $e^{at} u(t)$ | $\frac{e^{at} - at - 1}{a^2} u(t)$ |
| $e^{at} u(t)$ | $\sin(\omega_0 t) u(t)$ | $\frac{e^{at} - \cos(\omega_0 t) + \frac{a}{\omega_0} \sin(\omega_0 t)}{a^2 + \omega_0^2} u(t)$ |

---

## 7. Connections and Cross-References

- **Lecture 05 (LTI Systems):** The convolution integral is derived from the impulse response and the superposition principle established in Lecture 05. The properties of convolution (commutativity, associativity, distributivity) are essential for analyzing cascaded and parallel LTI system configurations.
- **Lecture 04 (Continuous-Time Systems):** The linearity and time-invariance properties are prerequisites for the convolution representation to be valid. A system that is not LTI cannot be fully characterized by its impulse response alone.
- **Lecture 03 (Continuous-Time Signals):** The Dirac delta function's sifting property is the mathematical starting point for the convolution derivation. The unit step, ramp, exponential, and sinusoidal signals used in the examples are all introduced in Lecture 03.
- **Fourier Transform (upcoming):** The convolution theorem states that $\mathcal{F}\{x(t) * h(t)\} = X(j\omega) H(j\omega)$. This property is the foundation of frequency-domain system analysis: convolution in time becomes multiplication in frequency.
- **Laplace Transform (upcoming):** Similarly, $\mathcal{L}\{x(t) * h(t)\} = X(s) H(s)$. The transfer function $H(s) = \mathcal{L}\{h(t)\}$ is the Laplace transform of the impulse response.
- **Digital Signal Processing (future course):** Discrete-time convolution $y[n] = x[n] * h[n] = \sum_{k=-\infty}^{\infty} x[k] h[n-k]$ is the direct counterpart, with the same algebraic properties. The graphical method for discrete-time convolution uses summation instead of integration.

---

## 8. Exam Tip: Systematic Convolution Strategy

### The Five-Step Procedure for Exam Problems

1. **Sketch both signals** as functions of $\tau$. Mark all breakpoints clearly.
2. **Choose which signal to reverse** — pick the one with fewer pieces or simpler functional form to make integration easier (commutativity gives you this freedom).
3. **Determine the piecewise intervals.** The critical values of $t$ are:
   - The start and end of each signal's support.
   - For each breakpoint $b$ in $h(\tau)$, add/subtract breakpoints from $x(\tau)$ to find $t$ values where overlap changes.
   - More systematically: if $x$ has breakpoints $\{a_i\}$ and $h$ has breakpoints $\{b_j\}$, then $y$ has candidate breakpoints at $\{a_i + b_j\}$.
4. **For each interval, write the integral with correct limits and functional forms.**
5. **Verify continuity** at each interval boundary — the output of convolution is always continuous.

### Common Mistakes to Avoid

| Mistake | Correction |
| :--- | :--- |
| Forgetting to reverse one signal before shifting | The operation is $h(t - \tau)$, not $h(\tau - t)$ |
| Confusing the shift direction | For $t > 0$, the reversed signal moves right; for $t < 0$, it moves left |
| Using the wrong integration variable | The integration is over $\tau$, not over $t$ |
| Forgetting the width property as a sanity check | $T_y = T_x + T_h$ must always hold for finite-duration signals |
| Assuming the output is discontinuous at interval boundaries | Convolution always produces a continuous output |
| Not checking the commutative choice | Reversing $x$ instead of $h$ can dramatically simplify integration |
| Using $\infty$ as upper limit when both signals are causal | Use $\int_{0}^{t}$, not $\int_{0}^{\infty}$ |

### Convolution Shortcut for Exam Problems

For piecewise-constant signals, the integral at each $t$ is simply the area of the overlap region multiplied by the overlapping values:

$$
y(t) = (\text{overlap length}) \times (\text{product of signal values in overlap})
$$

This shortcut applies when both signals are constant over the overlap interval. For piecewise-linear signals, the overlap product is a polynomial, and integration follows standard polynomial integration rules.

### Quick Reference: Convolution Properties for Problem Solving

When faced with a complex convolution, simplify using:

1. **Decompose signals** using the distributive property: break $x$ or $h$ into simpler pieces.
2. **Use the identity property**: convolving with $\delta(t - t_0)$ is just a shift.
3. **Use the differentiation property**: $\frac{d}{dt}(x * h) = \frac{dx}{dt} * h$ — differentiating one signal may produce impulses that simplify the convolution.
4. **Use the convolution table** for standard pairs: exponentials, steps, ramps, and sines have known results.
5. **Verify with the width property**: if your output duration does not match $T_x + T_h$, recheck your intervals.

> **[Key Insight]**
>
> The most common exam error: using $\int_{0}^{\infty}$ instead of $\int_{0}^{t}$ when both signals are causal. The upper limit of the convolution integral for causal signals is $t$, not $\infty$, because $h(t - \tau) = 0$ for $\tau > t$ (the system cannot respond to future inputs). Using $\infty$ as the upper limit will produce an incorrect result unless the signals naturally decay to zero at infinity in a way that makes the contribution beyond $t$ vanish, which only happens for special cases (e.g., exponentials).