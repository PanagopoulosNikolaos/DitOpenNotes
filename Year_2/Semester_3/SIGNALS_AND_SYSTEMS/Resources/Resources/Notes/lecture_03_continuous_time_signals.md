# Lecture 03 - Continuous-Time Signals (Basic and Elementary Signals)

Foundational elementary signals used to construct and analyze more complex continuous-time signals in signals and systems. This lecture introduces the unit step, signum, Dirac delta impulse, unit ramp, exponential, sinusoidal, damped sinusoidal, rectangular pulse, triangular pulse, sinc, and impulse train functions. These elementary signals serve as the building blocks for representing arbitrary signals and for characterizing the response of linear time-invariant (LTI) systems.

---

## 1. Conceptual Foundation

### 1.1 Why Elementary Signals Matter

Elementary signals are the "primitives" of signal processing. Just as vectors in $\mathbb{R}^n$ can be expressed as linear combinations of basis vectors, arbitrary continuous-time signals can be expressed as combinations of elementary signals. The Dirac delta function, in particular, enables the representation of any signal as a superposition of shifted impulses, which is the foundation of the convolution integral and LTI system analysis.

The unit step function provides a mathematical mechanism for turning signals "on" at a specific time. Exponential and sinusoidal signals are eigenfunctions of LTI systems — when an exponential passes through an LTI system, the output is the same exponential scaled by a complex factor (the frequency response). This property is the basis for Fourier analysis.

### 1.2 Periodicity of the Sum of Periodic Signals

Before introducing the elementary signals, the condition for the sum of periodic signals to be periodic is established. This condition is essential for determining whether combinations of sinusoids or periodic pulses remain periodic.

Given two periodic signals $x_1(t)$ with fundamental period $T_1$ and $x_2(t)$ with fundamental period $T_2$, their sum $x(t) = x_1(t) + x_2(t)$ is periodic **if and only if** the ratio $T_1 / T_2$ is a rational number (i.e., can be expressed as a ratio of integers).

$$
\frac{T_1}{T_2} = \frac{p}{q}, \quad p, q \in \mathbb{Z}^+
$$

When this holds, the fundamental period of the sum is:

$$
T_0 = p T_2 = q T_1 = \text{lcm}(T_1, T_2)
$$

where lcm denotes the least common multiple in the rational sense.

> **[Key Insight]**
>
> For the sum of $N$ periodic signals $x(t) = \sum_{k=1}^N x_k(t)$ with periods $T_k$, the sum is periodic if and only if $T_i / T_j$ is rational for **every pair** $(i, j)$. A common mistake is to check only one pair; all ratios must be rational.

---

## 2. Formal Definitions and Models

### 2.1 Unit Step Function (Heaviside Function)

The unit step function $u(t)$ is defined as:

$$
u(t) =
\begin{cases}
0, & t < 0 \\
1, & t > 0
\end{cases}
$$

**Discontinuity at $t = 0$:** The value at $t = 0$ is ambiguous. Common conventions set $u(0) = 1$, $u(0) = 1/2$, or leave it undefined. The precise value at $t = 0$ is immaterial for most signal processing applications because integrals over a set of measure zero do not affect the result.

**Alternative limit definition:**

$$
u(t) = \lim_{\epsilon \to 0^+} \frac{1}{2} + \frac{1}{\pi} \arctan\left(\frac{t}{\epsilon}\right)
$$

**Amplitude scaling and shifting:**

A shifted and scaled step is:

$$
A \cdot u(t - t_0) =
\begin{cases}
0, & t < t_0 \\
A, & t > t_0
\end{cases}
$$

The step function is used to **gate** signals — it truncates a signal to be non-zero only for $t \ge t_0$:

$$
x(t) u(t - t_0) =
\begin{cases}
0, & t < t_0 \\
x(t), & t > t_0
\end{cases}
$$

### 2.2 Signum Function

The signum function $\operatorname{sgn}(t)$ is defined as:

$$
\operatorname{sgn}(t) =
\begin{cases}
-1, & t < 0 \\
0, & t = 0 \\
1, & t > 0
\end{cases}
$$

**Relationship to the unit step:**

$$
\operatorname{sgn}(t) = 2u(t) - 1
$$

$$
u(t) = \frac{1}{2} + \frac{1}{2} \operatorname{sgn}(t)
$$

The signum function extracts the polarity of its argument while discarding magnitude information.

### 2.3 Unit Impulse Function (Dirac Delta Function)

The Dirac delta function $\delta(t)$ is a **generalized function** (distribution) defined by its sifting property rather than by pointwise values:

$$
\int_{-\infty}^{\infty} \delta(t) \, dt = 1
$$

$$
\delta(t) = 0 \quad \text{for } t \neq 0
$$

At $t = 0$, $\delta(0)$ is not defined as a finite number; it is represented graphically as an arrow (impulse) of height proportional to its area.

> **[Supplementary]**
>
> The Dirac delta is not a function in the ordinary sense. It is a distribution — a linear functional that maps test functions to real numbers via $\langle \delta, \phi \rangle = \phi(0)$. Engineers treat it operationally through its integral properties, which is sufficient for LTI system analysis.

#### Amplitude Scaling and Time Shifting

A scaled, shifted impulse $\alpha \delta(t - t_0)$ has area $\alpha$ concentrated at $t = t_0$:

$$
\int_{-\infty}^{\infty} \alpha \delta(t - t_0) \, dt = \alpha
$$

#### Approximation Limits

The delta function can be visualized as the limit of a sequence of unit-area pulses:

$$
\delta(t) = \lim_{\epsilon \to 0} \frac{1}{\epsilon} \operatorname{rect}\left(\frac{t}{\epsilon}\right)
$$

where $\operatorname{rect}(t)$ is the rectangular pulse of unit width and unit height.

### 2.4 Mathematical Relations Between Step and Impulse Functions

The unit step is the integral of the unit impulse:

$$
u(t) = \int_{-\infty}^{t} \delta(\tau) \, d\tau
$$

The unit impulse is the derivative (in the distributional sense) of the unit step:

$$
\delta(t) = \frac{d}{dt} u(t)
$$

This relationship is fundamental: the derivative of a discontinuous jump at $t = 0$ produces an impulse whose area equals the height of the jump.

### 2.5 Fundamental Properties of the Dirac Delta Function

#### Sifting Property

The sifting property extracts the value of a continuous function $x(t)$ at the location of the impulse:

$$
\int_{-\infty}^{\infty} x(t) \delta(t - t_0) \, dt = x(t_0)
$$

More generally:

$$
\int_{-\infty}^{\infty} x(t) \delta^{(n)}(t - t_0) \, dt = (-1)^n x^{(n)}(t_0)
$$

where $\delta^{(n)}(t)$ is the $n$-th derivative of the delta function.

#### Time Scaling Property

For any non-zero real $a$:

$$
\delta(at) = \frac{1}{|a|} \delta(t)
$$

This can be derived from the area property:

$$
\int_{-\infty}^{\infty} \delta(at) \, dt = \int_{-\infty}^{\infty} \delta(\tau) \frac{d\tau}{|a|} = \frac{1}{|a|}
$$

#### Evenness Property

The Dirac delta is an even function in the distributional sense:

$$
\delta(-t) = \delta(t)
$$

### 2.6 Unit Ramp Function

The unit ramp function $r(t)$ is defined as:

$$
r(t) =
\begin{cases}
0, & t \le 0 \\
t, & t \ge 0
\end{cases}
$$

**Relationship to step and impulse:**

$$
r(t) = \int_{-\infty}^{t} u(\tau) \, d\tau = t \cdot u(t)
$$

$$
\frac{d}{dt} r(t) = u(t)
$$

$$
\frac{d^2}{dt^2} r(t) = \delta(t)
$$

The ramp increases linearly with unit slope for $t > 0$ and its second derivative produces an impulse at $t = 0$.

### 2.7 Exponential Signals

#### Real Exponential Signals

A real exponential signal has the form:

$$
x(t) = A e^{\sigma t}
$$

where $A$ and $\sigma$ are real constants.

| Condition | Behavior | Example |
| :--- | :--- | :--- |
| $\sigma > 0$ | Growing exponential | $e^{2t}$ |
| $\sigma < 0$ | Decaying exponential | $e^{-3t}$ |
| $\sigma = 0$ | Constant (DC) | $A$ |

The **time constant** $\tau = 1/|\sigma|$ characterizes the rate of decay or growth. After one time constant, $e^{-t/\tau}$ decays to $e^{-1} \approx 0.368$ of its initial value.

#### Complex Exponential Signals

A complex exponential has the form:

$$
x(t) = A e^{(\sigma + j\omega_0)t} = A e^{\sigma t} e^{j\omega_0 t}
$$

Using Euler's identity:

$$
e^{j\omega_0 t} = \cos(\omega_0 t) + j \sin(\omega_0 t)
$$

The complex exponential can therefore be expressed in terms of sinusoids:

**Euler's Formulas:**

$$
\cos(\theta) = \frac{e^{j\theta} + e^{-j\theta}}{2}
$$

$$
\sin(\theta) = \frac{e^{j\theta} - e^{-j\theta}}{2j}
$$

### 2.8 Sinusoidal Signals and Phase Relationships

A general sinusoid is written as:

$$
x(t) = A \cos(\omega_0 t + \phi)
$$

where:
- $A$ is the amplitude (peak value)
- $\omega_0$ is the angular frequency (rad/s)
- $\phi$ is the phase (radians)
- $T_0 = 2\pi/\omega_0$ is the fundamental period

**Phase relationships:**

| Phase $\phi$ | Relationship to $\cos(\omega_0 t)$ |
| :--- | :--- |
| $\phi = 0$ | In-phase |
| $\phi = -\pi/2$ | Quadrature lag (sine) |
| $\phi = \pi/2$ | Quadrature lead |
| $\phi = \pi$ | Phase opposition (inverted) |

A sine is a cosine shifted by $-\pi/2$:

$$
\sin(\omega_0 t) = \cos\left(\omega_0 t - \frac{\pi}{2}\right)
$$

### 2.9 Damped Sinusoids

A damped sinusoid combines an exponential envelope with a sinusoidal oscillation:

$$
x(t) = A e^{\sigma t} \cos(\omega_0 t + \phi) u(t)
$$

For $\sigma < 0$, the amplitude decays exponentially over time. The envelope is $\pm A e^{\sigma t}$. The time constant $\tau = 1/|\sigma|$ determines how quickly the oscillation decays.

Damped sinusoids model many physical phenomena: RLC circuit transient responses, mechanical vibrations with friction, and electromagnetic wave attenuation.

### 2.10 Rectangular Pulse Function

The rectangular pulse function $\operatorname{rect}(t)$ is defined as:

$$
\operatorname{rect}(t) =
\begin{cases}
1, & |t| \le 1/2 \\
0, & |t| > 1/2
\end{cases}
$$

A scaled and shifted rectangular pulse:

$$
\operatorname{rect}\left(\frac{t - t_0}{T}\right) =
\begin{cases}
1, & |t - t_0| \le T/2 \\
0, & |t - t_0| > T/2
\end{cases}
$$

This pulse has:
- Center at $t = t_0$
- Width $T$
- Amplitude $1$

**Relationship to the unit step:**

A rectangular pulse can be expressed as the difference of two step functions:

$$
\operatorname{rect}\left(\frac{t - t_0}{T}\right) = u\left(t - t_0 + \frac{T}{2}\right) - u\left(t - t_0 - \frac{T}{2}\right)
$$

### 2.11 Periodic Rectangular Pulses (Pulse Trains)

A periodic rectangular pulse train with period $T_0$, pulse width $\tau$, and amplitude $A$ is defined as:

$$
x(t) = \sum_{k=-\infty}^{\infty} A \cdot \operatorname{rect}\left(\frac{t - kT_0}{\tau}\right)
$$

The **duty cycle** is the ratio $\tau / T_0$.

### 2.12 Triangular Pulse Function

The triangular pulse function $\operatorname{tri}(t)$ is defined as:

$$
\operatorname{tri}(t) =
\begin{cases}
1 - |t|, & |t| \le 1 \\
0, & |t| > 1
\end{cases}
$$

A scaled and shifted triangular pulse:

$$
\operatorname{tri}\left(\frac{t - t_0}{T}\right) =
\begin{cases}
1 - \frac{|t - t_0|}{T}, & |t - t_0| \le T \\
0, & |t - t_0| > T
\end{cases}
$$

This pulse has:
- Peak $1$ at $t = t_0$
- Base width $2T$
- Triangular shape (linearly rising and falling)

The triangular pulse can be obtained by convolving two rectangular pulses:

$$
\operatorname{tri}(t) = \operatorname{rect}(t) * \operatorname{rect}(t)
$$

### 2.13 Sampling Function (Sinc Function)

The sinc function is defined in two common forms:

**Normalized form (most common in signal processing):**

$$
\operatorname{sinc}(t) = \frac{\sin(\pi t)}{\pi t}
$$

**Unnormalized form (common in mathematics):**

$$
\operatorname{sinc}(t) = \frac{\sin(t)}{t}
$$

In this course, the **normalized form** is used unless otherwise specified.

**Key properties:**

| Property | Expression |
| :--- | :--- |
| Value at $t = 0$ | $\operatorname{sinc}(0) = 1$ (by limit) |
| Zero crossings | $t = n$ for integer $n \neq 0$ |
| Evenness | $\operatorname{sinc}(-t) = \operatorname{sinc}(t)$ |
| Area | $\int_{-\infty}^{\infty} \operatorname{sinc}(t) \, dt = 1$ |
| Energy | $\int_{-\infty}^{\infty} \operatorname{sinc}^2(t) \, dt = 1$ |

The sinc function plays a central role in sampling theory (Nyquist-Shannon sampling theorem) and in the Fourier transform of rectangular pulses.

### 2.14 Impulse Train (Comb Function)

The impulse train (or comb function) is a periodic sequence of Dirac delta impulses:

$$
\operatorname{III}_{T_0}(t) = \sum_{k=-\infty}^{\infty} \delta(t - kT_0)
$$

where $T_0$ is the spacing between impulses (the period).

**Key properties:**

- The impulse train is periodic with period $T_0$.
- Its Fourier series representation is also an impulse train in the frequency domain.
- It is used extensively in sampling theory: multiplying a signal $x(t)$ by $\operatorname{III}_{T_0}(t)$ produces a sampled version:

$$
x_s(t) = x(t) \cdot \operatorname{III}_{T_0}(t) = \sum_{k=-\infty}^{\infty} x(kT_0) \delta(t - kT_0)
$$

---

## 3. Key Parameters and Constraints

### 3.1 Elementary Signal Parameters

| Signal | Parameters | Units | Typical Range |
| :--- | :--- | :--- | :--- |
| Unit step $u(t - t_0)$ | Shift $t_0$ | s | $-\infty < t_0 < \infty$ |
| Signum $\operatorname{sgn}(t)$ | None | — | — |
| Impulse $\alpha \delta(t - t_0)$ | Area $\alpha$, shift $t_0$ | Signal$\cdot$s, s | $\alpha \in \mathbb{R}$ |
| Ramp $A \cdot r(t - t_0)$ | Slope $A$, shift $t_0$ | Signal/s, s | $A \in \mathbb{R}$ |
| Real exponential $A e^{\sigma t}$ | Amplitude $A$, exponent $\sigma$ | Signal, 1/s | $\sigma \in \mathbb{R}$, $A \in \mathbb{R}$ |
| Complex exponential $A e^{(\sigma + j\omega_0)t}$ | $A$, $\sigma$, $\omega_0$ | Signal, 1/s, rad/s | $\sigma \in \mathbb{R}$, $\omega_0 > 0$ |
| Sinusoid $A\cos(\omega_0 t + \phi)$ | $A$, $\omega_0$, $\phi$ | Signal, rad/s, rad | $A > 0$, $\omega_0 > 0$, $0 \le \phi < 2\pi$ |
| Damped sinusoid $A e^{\sigma t}\cos(\omega_0 t + \phi) u(t)$ | $A$, $\sigma$, $\omega_0$, $\phi$ | Signal, 1/s, rad/s, rad | $\sigma < 0$ for decay |
| Rectangular pulse $\operatorname{rect}((t - t_0)/T)$ | Center $t_0$, width $T$ | s, s | $T > 0$ |
| Triangular pulse $\operatorname{tri}((t - t_0)/T)$ | Center $t_0$, half-width $T$ | s, s | $T > 0$ |
| Sinc $\operatorname{sinc}(t)$ | None (scaled by argument) | — | — |
| Impulse train $\operatorname{III}_{T_0}(t)$ | Spacing $T_0$ | s | $T_0 > 0$ |

### 3.2 Constraints on Periodicity of Summed Signals

For $x(t) = A_1\cos(\omega_1 t + \phi_1) + A_2\cos(\omega_2 t + \phi_2)$:

| Condition | Result |
| :--- | :--- |
| $\omega_1 / \omega_2$ rational | Sum is periodic |
| $\omega_1 / \omega_2$ irrational | Sum is aperiodic (but may appear nearly periodic over finite intervals) |

> **[Key Insight]**
>
> An irrational ratio $\omega_1 / \omega_2$ (e.g., $\omega_1 = 1$ and $\omega_2 = \sqrt{2}$) means the sum never exactly repeats. However, for practical purposes, if the ratio is approximately rational within measurement precision, the signal may be treated as periodic over sufficiently long observation windows.

---

## 4. Step-by-Step Mechanisms

### 4.1 Procedure for Expressing a Piecewise Signal Using Elementary Signals

When a signal is defined piecewise over multiple intervals, it can be expressed as a sum of gated functions using step functions.

**Algorithm:**

1. Identify each interval where the signal has a distinct functional form.
2. For each interval $[t_a, t_b]$, create a gate using step differences: $u(t - t_a) - u(t - t_b)$.
3. Multiply each functional form by its corresponding gate.
4. Sum all gated components.

$$
x(t) = \sum_{i} f_i(t) \cdot [u(t - t_{a,i}) - u(t - t_{b,i})]
$$

### 4.2 Procedure for Computing Convolution with an Impulse

Convolving any signal $x(t)$ with a shifted impulse produces a shifted copy of $x(t)$:

$$
x(t) * \delta(t - t_0) = x(t - t_0)
$$

This is the **replication property** of the delta function. Combined with the sifting property, it forms the theoretical basis for representing arbitrary signals as impulse trains and for deriving the convolution integral.

### 4.3 Procedure for Computing Derivative Relationships

The derivative of a signal containing a discontinuity produces an impulse whose area equals the size of the discontinuity.

**Algorithm:**

1. Identify all points of discontinuity in $x(t)$.
2. At each discontinuity at $t = t_k$ with jump height $\Delta_k = \lim_{t \to t_k^+} x(t) - \lim_{t \to t_k^-} x(t)$, add $\Delta_k \cdot \delta(t - t_k)$ to the derivative.
3. Differentiate the continuous portions of $x(t)$ normally.

### 4.4 Procedure for Constructing a Pulse Train

A periodic rectangular pulse train with period $T_0$, pulse width $\tau$, and amplitude $A$ can be constructed using either:

**Method 1 (Step functions):**

$$
x(t) = A \sum_{k=-\infty}^{\infty} \left[ u\left(t - kT_0 + \frac{\tau}{2}\right) - u\left(t - kT_0 - \frac{\tau}{2}\right) \right]
$$

**Method 2 (Convolution with impulse train):**

$$
x(t) = \left[ A \cdot \operatorname{rect}\left(\frac{t}{\tau}\right) \right] * \operatorname{III}_{T_0}(t)
$$

Method 2 is more elegant: a single pulse convolved with an impulse train creates a periodic replication of that pulse.

---

## 5. Worked Examples

### Exercise 1: Expressing a Piecewise Signal Using Step Functions

**Problem:** Express the following piecewise signal using unit step functions:

$$
x(t) =
\begin{cases}
0, & t < 0 \\
2, & 0 \le t < 3 \\
-1, & 3 \le t < 5 \\
0, & t \ge 5
\end{cases}
$$

**Solution:**

**Step 1:** Identify the intervals and corresponding functions:

| Interval | Function |
| :--- | :--- |
| $t < 0$ | $0$ |
| $0 \le t < 3$ | $2$ |
| $3 \le t < 5$ | $-1$ |
| $t \ge 5$ | $0$ |

**Step 2:** Create gates for each non-zero interval.

For the first non-zero interval $[0, 3)$:
$$
g_1(t) = u(t) - u(t - 3)
$$

For the second non-zero interval $[3, 5)$:
$$
g_2(t) = u(t - 3) - u(t - 5)
$$

**Step 3:** Multiply each function by its gate and sum:

$$
x(t) = 2 \cdot [u(t) - u(t - 3)] + (-1) \cdot [u(t - 3) - u(t - 5)]
$$

**Step 4:** Simplify:

$$
x(t) = 2u(t) - 2u(t - 3) - u(t - 3) + u(t - 5)
$$

$$
x(t) = 2u(t) - 3u(t - 3) + u(t - 5)
$$

*Verification:* At $t = 2$: $x(2) = 2 - 0 + 0 = 2$ (correct, interval $[0, 3)$). At $t = 4$: $x(4) = 2 - 3 + 0 = -1$ (correct, interval $[3, 5)$). At $t = 6$: $x(6) = 2 - 3 + 1 = 0$ (correct, $t \ge 5$).

---

### Exercise 2: Derivative of a Signal Containing Discontinuities

**Problem:** Given $x(t) = (2t + 1)u(t) - (t - 1)u(t - 2)$, find $\frac{dx}{dt}$ and express it using elementary signals.

**Solution:**

**Step 1:** Identify discontinuities. The signal has potential discontinuities at $t = 0$ and $t = 2$ where the step functions turn on/off.

**Step 2:** Compute the left-hand and right-hand limits at each discontinuity.

At $t = 0$:
- Left limit: $t \to 0^-$, $u(t) = 0$, $u(t - 2) = 0$, so $x(0^-) = 0$.
- Right limit: $t \to 0^+$, $u(t) = 1$, $u(t - 2) = 0$, so $x(0^+) = 2(0) + 1 = 1$.
- Jump height: $\Delta_0 = 1 - 0 = 1$.

At $t = 2$:
- Left limit: $t \to 2^-$, $u(t) = 1$, $u(t - 2) = 0$, so $x(2^-) = 2(2) + 1 = 5$.
- Right limit: $t \to 2^+$, $u(t) = 1$, $u(t - 2) = 1$, so $x(2^+) = 2(2) + 1 - (2 - 1) = 5 - 1 = 4$.
- Jump height: $\Delta_2 = 4 - 5 = -1$.

**Step 3:** Differentiate the continuous portions.

For the term $(2t + 1)u(t)$, the derivative of the smooth part is $2$, gated by $u(t)$.
For the term $-(t - 1)u(t - 2)$, the derivative of the smooth part is $-1$, gated by $u(t - 2)$.

**Step 4:** Add impulse contributions for each discontinuity:

$$
\frac{dx}{dt} = 2u(t) - u(t - 2) + 1 \cdot \delta(t) + (-1) \cdot \delta(t - 2)
$$

$$
\frac{dx}{dt} = 2u(t) - u(t - 2) + \delta(t) - \delta(t - 2)
$$

*Intermediate state check:* The derivative at $t = 1$ (no impulse): $2 - 0 = 2$, which matches the slope of $2t + 1$ in $(0, 2)$. The derivative at $t = 2.5$: $2 - 1 = 1$, but the signal is actually $(2t + 1) - (t - 1) = t + 2$, whose slope is $1$ — correct.

---

### Exercise 3: Sifting Property of the Dirac Delta

**Problem:** Evaluate the following integrals:

(a) $\int_{-\infty}^{\infty} e^{-2t} \cos(5t) \delta(t - 3) \, dt$

(b) $\int_{-\infty}^{\infty} t^2 \delta(2t) \, dt$

(c) $\int_{-\infty}^{\infty} e^{-|t|} \delta(t + 1) \, dt$

**Solution:**

**(a)** By the sifting property:

$$
\int_{-\infty}^{\infty} x(t) \delta(t - t_0) \, dt = x(t_0)
$$

Here $x(t) = e^{-2t}\cos(5t)$ and $t_0 = 3$:

$$
\int_{-\infty}^{\infty} e^{-2t} \cos(5t) \delta(t - 3) \, dt = e^{-2(3)} \cos(5 \cdot 3) = e^{-6} \cos(15)
$$

$\cos(15) \approx \cos(15 \times 180/\pi) \approx \cos(859.4^\circ) = \cos(859.4^\circ - 2 \times 360^\circ) = \cos(139.4^\circ) \approx -0.759$:

$$
\text{Result} = e^{-6} \cdot (-0.759) \approx 0.00248 \times (-0.759) \approx -0.00188
$$

Exact form: $e^{-6}\cos(15)$.

**(b)** Use the time scaling property: $\delta(2t) = \frac{1}{|2|} \delta(t) = \frac{1}{2} \delta(t)$:

$$
\int_{-\infty}^{\infty} t^2 \delta(2t) \, dt = \int_{-\infty}^{\infty} t^2 \cdot \frac{1}{2} \delta(t) \, dt = \frac{1}{2} \cdot 0^2 = 0
$$

**(c)** Here $x(t) = e^{-|t|}$ and $t_0 = -1$:

$$
\int_{-\infty}^{\infty} e^{-|t|} \delta(t + 1) \, dt = \int_{-\infty}^{\infty} e^{-|t|} \delta(t - (-1)) \, dt = e^{-|-1|} = e^{-1} = \frac{1}{e}
$$

---

### Exercise 4: Periodicity of the Sum of Sinusoids

**Problem:** Determine whether each sum is periodic. If periodic, find the fundamental period.

(a) $x(t) = \cos(2\pi t) + \cos(4\pi t)$

(b) $x(t) = \cos(3t) + \sin(5t)$

(c) $x(t) = \cos(2t) + \cos(2\pi t)$

**Solution:**

**(a)** Compute the individual periods:
- $\cos(2\pi t)$: $\omega_1 = 2\pi$, $T_1 = 2\pi/\omega_1 = 1$ s
- $\cos(4\pi t)$: $\omega_2 = 4\pi$, $T_2 = 2\pi/\omega_2 = 1/2$ s

Check the ratio:
$$
\frac{T_1}{T_2} = \frac{1}{1/2} = 2 = \frac{2}{1}
$$

The ratio $2$ is rational. The sum is periodic.

The fundamental period is the least common multiple: $T_0 = \text{lcm}(1, 1/2) = 1$ s.

*Verification:* $\cos(2\pi(t+1)) + \cos(4\pi(t+1)) = \cos(2\pi t + 2\pi) + \cos(4\pi t + 4\pi) = \cos(2\pi t) + \cos(4\pi t)$.

**(b)** Compute the individual periods:
- $\cos(3t)$: $\omega_1 = 3$, $T_1 = 2\pi/3$ s
- $\sin(5t)$: $\omega_2 = 5$, $T_2 = 2\pi/5$ s

Check the ratio:
$$
\frac{T_1}{T_2} = \frac{2\pi/3}{2\pi/5} = \frac{5}{3}
$$

The ratio $5/3$ is rational. The sum is periodic.

The fundamental period: $T_0 = 3 T_1 = 5 T_2 = 3 \times 2\pi/3 = 2\pi$ s.

*Verification:* At $t = 2\pi$: $\cos(3 \cdot 2\pi) + \sin(5 \cdot 2\pi) = \cos(6\pi) + \sin(10\pi) = 1 + 0 = 1$. At $t = 0$: $\cos(0) + \sin(0) = 1 + 0 = 1$. The pattern repeats.

**(c)** Compute the individual periods:
- $\cos(2t)$: $\omega_1 = 2$, $T_1 = 2\pi/2 = \pi$ s
- $\cos(2\pi t)$: $\omega_2 = 2\pi$, $T_2 = 2\pi/(2\pi) = 1$ s

Check the ratio:
$$
\frac{T_1}{T_2} = \frac{\pi}{1} = \pi
$$

The ratio $\pi$ is irrational. The sum is **aperiodic**.

> **[Key Insight]**
>
> This is a classic exam trick: $\cos(2t) + \cos(2\pi t)$ looks like it should be periodic because both terms are sinusoids, but the ratio $\pi$ (irrational) means the sum never exactly repeats. Do not confuse $\cos(2\pi t)$ (period 1) with $\cos(2t)$ (period $\pi$).

---

### Exercise 5: Expressing a Damped Sinusoid and Computing its Envelope

**Problem:** A damped sinusoid is given by $x(t) = 5 e^{-0.5t} \cos(3t - \pi/4) u(t)$. Determine:
(a) The amplitude, angular frequency, phase, and damping coefficient.
(b) The time constant.
(c) The value of the signal at $t = 0$ and $t = 2$ s.

**Solution:**

**(a)** From the standard form $A e^{\sigma t} \cos(\omega_0 t + \phi) u(t)$:

| Parameter | Symbol | Value |
| :--- | :--- | :--- |
| Amplitude | $A$ | $5$ |
| Damping coefficient | $\sigma$ | $-0.5$ s$^{-1}$ |
| Angular frequency | $\omega_0$ | $3$ rad/s |
| Phase | $\phi$ | $-\pi/4$ rad |

**(b)** The time constant is:
$$
\tau = \frac{1}{|\sigma|} = \frac{1}{0.5} = 2 \text{ s}
$$

After 2 seconds, the envelope decays to $e^{-1} \approx 0.368$ of its initial value.

**(c)** At $t = 0$:
$$
x(0) = 5 e^{-0.5 \cdot 0} \cos(3 \cdot 0 - \pi/4) u(0) = 5 \cdot 1 \cdot \cos(-\pi/4) \cdot 1 = 5 \cdot \frac{\sqrt{2}}{2} \approx 3.536
$$

At $t = 2$ s:
$$
x(2) = 5 e^{-0.5 \cdot 2} \cos(3 \cdot 2 - \pi/4) u(2) = 5 e^{-1} \cos(6 - \pi/4)
$$

$6 - \pi/4 \approx 6 - 0.785 = 5.215$ rad. Since $5.215 / 3 \approx 1.738$ periods of the $\cos(3t)$ oscillation have occurred. The envelope has decayed to $5e^{-1} \approx 1.839$.

Continuing the calculation:
$$
6 - \pi/4 = \frac{24}{4} - \frac{\pi}{4} \approx 5.215 \text{ rad}
$$

$$
\cos(5.215) \approx 0.468
$$

$$
x(2) \approx 5 \cdot 0.368 \cdot 0.468 \approx 0.861
$$

*Intermediate state check:* The initial amplitude was $3.536$; after one time constant (2 s), the signal has decayed to $0.861$, which is approximately $0.368 \times 3.536 \times (\text{cosine factor})$ — the cosine factor further reduces the value since at $t = 2$ the oscillation is not at a peak.

---

### Exercise 6: Constructing a Rectangular Pulse Train

**Problem:** A periodic rectangular pulse train has amplitude $A = 3$, period $T_0 = 4$ s, and duty cycle $25\%$. Write the mathematical expression using step functions. Determine the pulse width and sketch one period.

**Solution:**

**Step 1:** Compute the pulse width from the duty cycle.
$$
\text{Duty cycle} = \frac{\tau}{T_0} = 0.25 \implies \tau = 0.25 \times 4 = 1 \text{ s}
$$

**Step 2:** Construct one pulse (centered at $t = 0$ for convenience):
$$
p(t) = 3 \cdot \operatorname{rect}\left(\frac{t}{1}\right) = 3 \cdot [u(t + 0.5) - u(t - 0.5)]
$$

**Step 3:** Replicate periodically using the impulse train:
$$
x(t) = p(t) * \operatorname{III}_4(t) = \sum_{k=-\infty}^{\infty} 3 \cdot \left[u(t - 4k + 0.5) - u(t - 4k - 0.5)\right]
$$

**Step 4:** One period $[0, 4]$ using a representative pulse centered at $t = 0.5$:
$$
x_{\text{one period}}(t) = 3 \cdot [u(t) - u(t - 1)], \quad 0 \le t < 4
$$

*Signal values in one period:*

| Interval | $[0, 1)$ | $[1, 4)$ |
| :--- | :--- | :--- |
| $x(t)$ | $3$ | $0$ |

The average (DC) value of this pulse train is:
$$
\bar{x} = \frac{1}{T_0} \int_0^{T_0} x(t) dt = \frac{1}{4} \int_0^1 3 dt = \frac{3}{4}
$$

---

### Exercise 7: Relationship Between Step, Ramp, and Impulse Functions

**Problem:** A signal $x(t)$ has the following derivative:

$$
\frac{dx}{dt} = 2\delta(t) - \delta(t - 2) + u(t - 4)
$$

Given that $x(0^-) = 0$, find $x(t)$ and sketch it.

**Solution:**

**Step 1:** Integrate the derivative from $-\infty$ to $t$.

$$
x(t) = \int_{-\infty}^t \frac{dx}{d\tau} d\tau = \int_{-\infty}^t [2\delta(\tau) - \delta(\tau - 2) + u(\tau - 4)] d\tau
$$

**Step 2:** Integrate each term separately.

The integral of $\delta(\tau)$ produces $u(t)$:
$$
\int_{-\infty}^t 2\delta(\tau) d\tau = 2u(t)
$$

The integral of $-\delta(\tau - 2)$ produces $-u(t - 2)$:
$$
\int_{-\infty}^t -\delta(\tau - 2) d\tau = -u(t - 2)
$$

The integral of $u(\tau - 4)$ from $-\infty$ to $t$:
- For $t < 4$: the integrand is $0$, so the integral is $0$.
- For $t \ge 4$: $\int_4^t 1 d\tau = t - 4$.

This is the ramp function: $r(t - 4) = (t - 4)u(t - 4)$.

**Step 3:** Combine:
$$
x(t) = 2u(t) - u(t - 2) + r(t - 4)
$$

**Step 4:** Write piecewise:

| Interval | $x(t)$ |
| :--- | :--- |
| $t < 0$ | $0$ |
| $0 \le t < 2$ | $2$ |
| $2 \le t < 4$ | $2 - 1 = 1$ |
| $t \ge 4$ | $2 - 1 + (t - 4) = t - 3$ |

*Intermediate state check:* At $t = 0^+$: $x(0^+) = 2$ (jump of 2, consistent with $2\delta(t)$). At $t = 2^+$: $x(2^+) = 1$ (drop of 1, consistent with $-\delta(t - 2)$). At $t = 4$: $x(4) = 1$; for $t > 4$, the signal increases with slope 1 (consistent with $u(t - 4)$ being the derivative of $r(t - 4)$).

---

### Exercise 8: Sinc Function Properties and Zero Crossings

**Problem:** Given the normalized sinc function $x(t) = 5 \operatorname{sinc}(2t)$:

(a) Determine the zero crossings.
(b) Compute the value at $t = 0$.
(c) Compute $\int_{-\infty}^{\infty} x(t) \, dt$.
(d) Find the first non-zero crossing after $t = 0$.

**Solution:**

**(a)** The normalized sinc function $\operatorname{sinc}(2t) = \frac{\sin(\pi \cdot 2t)}{\pi \cdot 2t} = \frac{\sin(2\pi t)}{2\pi t}$.

Zero crossings occur when $\sin(2\pi t) = 0$ and $t \neq 0$:
$$
2\pi t = n\pi \implies t = \frac{n}{2}, \quad n \in \mathbb{Z}, n \neq 0
$$

Zero crossings at $t = \pm 0.5, \pm 1, \pm 1.5, \pm 2, \ldots$

**(b)** At $t = 0$, use the limit:
$$
x(0) = 5 \cdot \lim_{t \to 0} \operatorname{sinc}(2t) = 5 \cdot 1 = 5
$$

**(c)** Use the area property of the sinc function:
$$
\int_{-\infty}^{\infty} \operatorname{sinc}(at) \, dt = \frac{1}{|a|}
$$

For $a = 2$:
$$
\int_{-\infty}^{\infty} x(t) \, dt = 5 \cdot \frac{1}{2} = 2.5
$$

**(d)** The first non-zero crossing after $t = 0$ is at $t = 0.5$.

*Summary of key values:*

| $t$ | $x(t)$ |
| :--- | :--- |
| $0$ | $5$ |
| $\pm 0.5$ | $0$ |
| $\pm 1$ | $0$ |
| $\pm \infty$ | $0$ |

---

### Exercise 9: Expressing a Triangular Pulse Using Step and Ramp Functions

**Problem:** Express the triangular pulse:

$$
x(t) =
\begin{cases}
0, & t < -1 \\
t + 1, & -1 \le t < 0 \\
1 - t, & 0 \le t < 1 \\
0, & t \ge 1
\end{cases}
$$

using only unit step and unit ramp functions.

**Solution:**

**Step 1:** Recognize that the rising edge $t + 1$ on $[-1, 0]$ is a ramp shifted by 1 and the falling edge $1 - t$ on $[0, 1]$ is a negative ramp shifted by 1.

**Step 2:** Express the rising portion: $(t + 1)[u(t + 1) - u(t)]$.
This can be written as $r(t + 1) - r(t) \cdot \text{(something)}$.

Alternatively, express the rising edge directly:
For $t \ge -1$, $t + 1$ looks like $r(t + 1)$ but $r(t + 1)$ continues to grow beyond $t = 0$.

**Step 3:** Use the standard decomposition:

$$
x(t) = r(t + 1) - 2r(t) + r(t - 1)
$$

*Verification:*

| Interval | $r(t + 1)$ | $-2r(t)$ | $r(t - 1)$ | Sum |
| :--- | :--- | :--- | :--- | :--- |
| $t < -1$ | $0$ | $0$ | $0$ | $0$ |
| $-1 \le t < 0$ | $t + 1$ | $0$ | $0$ | $t + 1$ |
| $0 \le t < 1$ | $t + 1$ | $-2t$ | $0$ | $1 - t$ |
| $t \ge 1$ | $t + 1$ | $-2t$ | $t - 1$ | $0$ |

The decomposition is verified.

---

### Exercise 10: Impulse Train and Sampling

**Problem:** A continuous-time signal $x(t) = \cos(2\pi t)$ is sampled using an impulse train $\operatorname{III}_{0.25}(t)$ with spacing $T_0 = 0.25$ s.

(a) Write the expression for the sampled signal $x_s(t)$.
(b) Evaluate the first four samples ($k = 0, 1, 2, 3$).
(c) Determine if the sampling rate exceeds the Nyquist rate for this signal.

**Solution:**

**(a)** The sampled signal is:

$$
x_s(t) = x(t) \cdot \operatorname{III}_{0.25}(t) = \cos(2\pi t) \cdot \sum_{k=-\infty}^{\infty} \delta(t - 0.25k) = \sum_{k=-\infty}^{\infty} \cos(2\pi \cdot 0.25k) \cdot \delta(t - 0.25k)
$$

$$
x_s(t) = \sum_{k=-\infty}^{\infty} \cos\left(\frac{\pi k}{2}\right) \cdot \delta(t - 0.25k)
$$

**(b)** Evaluate for $k = 0, 1, 2, 3$:

| $k$ | $t = 0.25k$ | $\cos(\pi k / 2)$ | Sample Value |
| :--- | :--- | :--- | :--- |
| $0$ | $0$ | $\cos(0) = 1$ | $1 \cdot \delta(t)$ |
| $1$ | $0.25$ | $\cos(\pi/2) = 0$ | $0$ |
| $2$ | $0.5$ | $\cos(\pi) = -1$ | $-\delta(t - 0.5)$ |
| $3$ | $0.75$ | $\cos(3\pi/2) = 0$ | $0$ |

**(c)** The signal $x(t) = \cos(2\pi t)$ has frequency $f = 1$ Hz. The Nyquist rate is $2f = 2$ Hz.
The sampling frequency is $f_s = 1/T_0 = 1/0.25 = 4$ Hz.
Since $4 > 2$, the sampling rate exceeds the Nyquist rate, so the signal can be perfectly reconstructed from its samples under ideal conditions.

---

## 6. Connections and Cross-References

- **Lecture 01 (Course Introduction):** Introduced the sinusoidal signal representation and fundamental definitions of CT and DT signals. The sinusoid analysis here directly extends those basics.
- **Lecture 02 (Basic Signal Concepts):** The energy/power classification, signal transformations, and symmetry properties established in Lecture 02 apply directly to all elementary signals introduced here. For example, the unit step is a power signal; the rectangular pulse is an energy signal; the sinc function is an even energy signal.
- **Lecture 04 (Continuous-Time Systems):** The impulse response $h(t)$ of an LTI system is defined using the Dirac delta. The sifting property from this lecture is the foundation for deriving the convolution integral.
- **Lectures 05-06 (Convolution and LTI Systems):** The step response of an LTI system is the integral of its impulse response. The ramp response is the double integral. The relationships $u(t) = \int \delta(t) dt$ and $r(t) = \int u(t) dt$ are used to derive system responses to step and ramp inputs from the impulse response.
- **Fourier Series (upcoming):** The impulse train's Fourier series representation is itself an impulse train in the frequency domain. The sinc function is the Fourier transform of the rectangular pulse. The periodicity conditions for sums of sinusoids are applied repeatedly in Fourier analysis.
- **Sampling Theorem (upcoming):** The impulse train is the mathematical model of the ideal sampling process. The sinc function is the ideal reconstruction filter. The rectangular pulse train models practical sampling with a finite-aperture window.

---

## 7. Exam Tip: Elementary Signals in Disguise

Exam problems often embed elementary signals in complex-looking expressions. Recognize these patterns:

**1. The "hidden step" in limits of integration.**
If an integral has variable upper limit $t$, it may be producing a step or ramp:
$$
\int_{-\infty}^t \delta(\tau) d\tau = u(t), \quad \int_{-\infty}^t u(\tau) d\tau = r(t)
$$

**2. The "product of steps" as a pulse gate.**
When you see $u(t - a) - u(t - b)$, recognize this immediately as a pulse on $[a, b]$.

**3. The "derivative test" for impulse content.**
If a signal has a discontinuity, its derivative contains an impulse. The area of the impulse equals the jump height. This is a common exam question: differentiate a piecewise signal with discontinuities.

**4. The "sinc at zero" limit trick.**
When asked for $\operatorname{sinc}(0)$, do not attempt to compute $0/0$. Use L'Hopital's rule or recall that $\lim_{t \to 0} \sin(at)/(at) = 1$.

**5. Checking periodicity — the three-minute rule.**
When asked if a sum of sinusoids is periodic:
1. Compute individual periods from $\omega_k$.
2. Form the ratio $T_1/T_2$ (or $T_i/T_j$ for all pairs).
3. If all ratios are rational, the sum is periodic; the fundamental period is the LCM of the individual periods.
4. If any ratio is irrational, the sum is aperiodic.

**Common mistake:** Forgetting to check that $\omega_1 N_0$ and $\omega_2 N_0$ are simultaneously integer multiples of $2\pi$. Just checking that $\omega_1/\omega_2$ is rational is necessary but students often stop there — always compute the actual fundamental period.

**6. Impulse train as a sampling operator.**
When you see $x(t) \cdot \sum \delta(t - kT_0)$, the result is a train of weighted impulses. The weights are $x(kT_0)$. This appears in sampling theory problems and in Fourier series expansion of periodic signals.