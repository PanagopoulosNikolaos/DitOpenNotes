# Lecture 02 - Basic Signal Concepts

Formal definitions and comprehensive classifications of signals and systems, including signal dimensionality, energy and power analysis, time-domain and amplitude transformations, and fundamental signal properties. This lecture establishes the mathematical framework for characterizing signals by their domain, duration, symmetry, periodicity, determinism, and causality, and introduces the critical distinction between energy signals and power signals.

---

## 1. Conceptual Foundation

### 1.1 The Purpose of Signal Classification

Before any signal can be processed by a system, its fundamental nature must be understood. Classification answers essential questions: Is the signal defined at every instant or only at discrete points? Is its amplitude one of infinitely many values or a finite set? Does it repeat? Does it have finite or infinite energy? Each classification determines which mathematical tools — Fourier analysis, convolution, statistical methods — are applicable.

### 1.2 Signal Dimensionality

A signal is defined by its number of independent variables:

| Dimensionality | Notation | Example | Domain |
| :--- | :--- | :--- | :--- |
| One-dimensional (1D) | $x(t)$ or $x[n]$ | Audio voltage waveform | Time |
| Two-dimensional (2D) | $I(x, y)$ | Grayscale image | Spatial coordinates |
| Three-dimensional (3D) | $V(x, y, z)$ | Volumetric MRI scan | Spatial coordinates |
| Multidimensional | $s(x_1, x_2, \ldots, x_M)$ | Video $I(x, y, t)$ | Space-time |

In this course, the emphasis is on **one-dimensional** signals where the independent variable is time.

### 1.3 Formal Definition of a Signal and System

A **signal** is formally defined as a function that maps an independent variable (typically time) to a dependent variable (amplitude):

$$
x: \mathbb{R} \to \mathbb{R} \quad \text{(real-valued CT signal)}
$$

$$
x: \mathbb{Z} \to \mathbb{R} \quad \text{(real-valued DT signal)}
$$

The codomain may also be $\mathbb{C}$ for complex-valued signals.

A **system** is an operator $T\{\cdot\}$ that maps an input signal $x(t)$ to an output signal $y(t)$:

$$
y(t) = T\{x(t)\}
$$

The system is defined by the rule that determines $y(t)$ from $x(t)$.

---

## 2. Formal Definitions and Classification Models

### 2.1 Continuous-Time vs. Discrete-Time

| Aspect | Continuous-Time (CT) | Discrete-Time (DT) |
| :--- | :--- | :--- |
| Independent variable | Real time $t \in \mathbb{R}$ | Integer index $n \in \mathbb{Z}$ |
| Notation | $x(t)$ — parentheses | $x[n]$ — square brackets |
| Signal value between samples | Defined for all $t$ | Not defined; only at integer $n$ |
| Origin | Physical phenomena | Sampling of CT signals or computation |

### 2.2 Analog vs. Digital

| Property | Analog Signal | Digital Signal |
| :--- | :--- | :--- |
| Time variable | Continuous ($t$) or discrete ($n$) | Discrete ($n$) |
| Amplitude | Continuous range | Finite set of quantized levels |
| Notation | $x(t)$ or $x[n]$ (real-valued) | $x[n]$ with values from a codebook |
| Noise susceptibility | High (continuous amplitude) | Low (discrete levels are distinguishable) |

> **[Key Insight]**
>
> "Discrete-time" and "digital" are not synonyms. A **discrete-time analog** signal (e.g., sampled but unquantized voltage) has discrete time but continuous amplitude. A **digital** signal has both discrete time and discrete amplitude. Always check both axes independently.

### 2.3 Analog-to-Digital Conversion Process

The conversion of a real-world analog signal to a digital representation proceeds through three sequential stages:

1. **Sampling:** The continuous-time signal $x(t)$ is measured at uniformly spaced time instants $t = nT_s$, where $T_s$ is the sampling period and $f_s = 1/T_s$ is the sampling frequency. The output is a discrete-time signal $x[n] = x(nT_s)$.

2. **Quantization:** Each sample $x[n]$ (which has continuous amplitude) is rounded to the nearest value from a finite set of $2^B$ discrete levels, where $B$ is the number of bits per sample. The error introduced is called **quantization error** or **quantization noise**.

3. **Coding:** Each quantized level is assigned a unique binary codeword of $B$ bits. The resulting bitstream is the digital representation of the original analog signal.

![ADC Block Diagram]
$$
x(t) \xrightarrow{\text{Sampling}} x[n] \xrightarrow{\text{Quantization}} x_q[n] \xrightarrow{\text{Coding}} \text{Bitstream}
$$

### 2.4 Signal Energy and Power

#### Energy Over a Finite Interval

The energy of a CT signal $x(t)$ over the interval $[t_1, t_2]$ is:

$$
E_{[t_1,t_2]} = \int_{t_1}^{t_2} |x(t)|^2 dt
$$

For a DT signal $x[n]$ over $N_1 \le n \le N_2$:

$$
E_{[N_1,N_2]} = \sum_{n=N_1}^{N_2} |x[n]|^2
$$

#### Average Power Over a Finite Interval

The average power of a CT signal over $[t_1, t_2]$ is:

$$
P_{[t_1,t_2]} = \frac{1}{t_2 - t_1} \int_{t_1}^{t_2} |x(t)|^2 dt
$$

For DT:

$$
P_{[N_1,N_2]} = \frac{1}{N_2 - N_1 + 1} \sum_{n=N_1}^{N_2} |x[n]|^2
$$

#### Total Energy and Average Power Over Infinite Horizon

**Total energy:**

$$
E_\infty = \lim_{T \to \infty} \int_{-T}^{T} |x(t)|^2 dt = \int_{-\infty}^{\infty} |x(t)|^2 dt
$$

**Average power:**

$$
P_\infty = \lim_{T \to \infty} \frac{1}{2T} \int_{-T}^{T} |x(t)|^2 dt
$$

#### Energy Signals vs. Power Signals

| Signal Type | Condition | Example |
| :--- | :--- | :--- |
| **Energy signal** | $0 < E_\infty < \infty$ (finite total energy) | $e^{-t}u(t)$ |
| **Power signal** | $0 < P_\infty < \infty$ (finite non-zero average power) | $\cos(\omega_0 t)$ |
| **Neither** | Both $E_\infty$ and $P_\infty$ are infinite | $e^{t}u(t)$ (growing exponential) |

> **[Key Insight]**
>
> A signal **cannot** be both an energy signal and a power signal. If total energy is finite, average power over infinite time is zero. If average power is finite and non-zero, total energy is infinite. However, a signal can be **neither** if neither quantity is finite (e.g., a growing exponential).

---

## 3. Key Parameters and Constraints

### 3.1 Characteristic Parameters of CT Signals

| Parameter | Definition | Formula | Units |
| :--- | :--- | :--- | :--- |
| Mean value (DC component) | Average value over a period or interval | $\bar{x} = \frac{1}{T} \int_0^T x(t) dt$ | Same as signal |
| Mean square value | Average of squared amplitude | $\overline{x^2} = \frac{1}{T} \int_0^T x^2(t) dt$ | (Signal units)$^2$ |
| RMS value | Root of mean square | $X_{\text{RMS}} = \sqrt{\overline{x^2}}$ | Same as signal |
| Instantaneous power | Power at a single instant | $p(t) = x^2(t)$ (across $1\Omega$) | W |
| Average power | Power averaged over time | $P = \overline{x^2}$ | W |

### 3.2 Signal Duration Classification

| Duration Type | Definition | Example |
| :--- | :--- | :--- |
| Finite duration (time-limited) | $x(t) = 0$ for $|t| > T_c$ for some finite $T_c$ | Rectangular pulse |
| Infinite duration | $x(t) \neq 0$ for arbitrarily large $|t|$ | Sinusoid |
| Right-sided | $x(t) = 0$ for $t < t_0$ | $e^{-t}u(t)$ |
| Left-sided | $x(t) = 0$ for $t > t_0$ | $e^{t}u(-t)$ |

### 3.3 Periodic Signal Parameters

For a periodic signal $x(t)$ with fundamental period $T_0$:

| Parameter | Formula | Units |
| :--- | :--- | :--- |
| Fundamental period ($T_0$) | Smallest $T > 0$ such that $x(t+T) = x(t)$ | s |
| Fundamental frequency ($f_0$) | $f_0 = 1/T_0$ | Hz |
| Angular frequency ($\omega_0$) | $\omega_0 = 2\pi f_0 = 2\pi/T_0$ | rad/s |

---

## 4. Step-by-Step Mechanisms

### 4.1 Time-Domain Transformations

Time-domain transformations modify the independent variable $t$ and change the signal's temporal characteristics.

#### Time Shifting

$$
y(t) = x(t - t_0)
$$

- If $t_0 > 0$: signal is **delayed** (shifted right)
- If $t_0 < 0$: signal is **advanced** (shifted left)

**Procedure:** Replace every occurrence of $t$ in $x(t)$ with $(t - t_0)$. The shape of the signal is unchanged; only its position on the time axis changes.

#### Time Reversal (Reflection)

$$
y(t) = x(-t)
$$

**Procedure:** Replace every $t$ with $-t$. The signal is flipped about the vertical axis ($t = 0$). What happened at $t = 2$ now happens at $t = -2$.

#### Time Scaling

$$
y(t) = x(at)
$$

- If $|a| > 1$: signal is **compressed** in time
- If $0 < |a| < 1$: signal is **expanded** (stretched) in time
- If $a < 0$: time reversal is combined with scaling

**Procedure:** Replace every $t$ with $at$. The signal's duration is divided by $|a|$.

#### Combined Transformation: $x(at + b)$

The general linear transformation $x(at + b)$ should be applied in the correct order:

1. **Rewrite** as $x\left(a\left(t + \frac{b}{a}\right)\right)$
2. **Apply time shifting** first (shift by $-b/a$)
3. **Apply time scaling/reversal** second (scale by $a$)

Alternatively, use the direct substitution method: replace $t$ with $at + b$ in the original expression.

### 4.2 Amplitude Transformations

Amplitude transformations modify the dependent variable (signal amplitude).

#### Amplitude Scaling

$$
y(t) = A \cdot x(t)
$$

Multiplies every amplitude value by $A$. If $A > 1$, the signal is amplified; if $0 < A < 1$, it is attenuated. If $A < 0$, the signal is also inverted.

#### Amplitude Shifting (DC Offset)

$$
y(t) = x(t) + C
$$

Adds a constant $C$ to every amplitude value, shifting the signal vertically. This is equivalent to adding a DC component.

### 4.3 Signal Arithmetic

#### Addition

$$
y(t) = x_1(t) + x_2(t)
$$

The amplitude of $y(t)$ at each time $t$ is the sum of the amplitudes of $x_1(t)$ and $x_2(t)$ at that same instant.

#### Multiplication

$$
y(t) = x_1(t) \cdot x_2(t)
$$

The amplitude of $y(t)$ at each time $t$ is the product of the amplitudes. Multiplication is used extensively in modulation (amplitude modulation).

### 4.4 Procedure for Classifying a Signal

When classifying any signal, follow this deterministic sequence:

1. **Domain:** Parentheses $x(t)$ $\to$ CT; square brackets $x[n]$ $\to$ DT.
2. **Amplitude:** Continuous range $\to$ analog; finite set $\to$ digital.
3. **Duration:** Non-zero only on finite interval $\to$ finite duration; otherwise infinite.
4. **Periodicity:** Find smallest $T_0$ such that $x(t+T_0) = x(t)$ for all $t$. If none exists, signal is aperiodic.
5. **Symmetry:** $x(t) = x(-t)$ $\to$ even; $x(t) = -x(-t)$ $\to$ odd; otherwise neither.
6. **Determinism:** Exactly predictable $\to$ deterministic; random $\to$ stochastic.
7. **Causality:** $x(t) = 0$ for $t < 0$ $\to$ causal; otherwise non-causal.
8. **Boundedness:** $|x(t)| \le M$ for all $t$ and some finite $M$ $\to$ bounded.
9. **Energy/Power:** Compute $E_\infty$ and $P_\infty$; classify accordingly.

---

## 5. Signal Properties

### 5.1 Deterministic vs. Stochastic (Random) Signals

| Property | Deterministic | Stochastic |
| :--- | :--- | :--- |
| Definition | Exactly predictable; no uncertainty | Described by probability distributions |
| Value at any $t$ | Known exactly | A random variable |
| Analysis tools | Algebraic formulas, transforms | Correlation, spectral density, statistics |
| Example | $x(t) = 5\cos(2\pi t)$ | Thermal noise voltage, speech |

### 5.2 Causal vs. Non-causal Signals

A signal is **causal** if $x(t) = 0$ for all $t < 0$. It is **anti-causal** if $x(t) = 0$ for all $t > 0$. It is **non-causal** if it has non-zero values for both $t < 0$ and $t > 0$.

> **[Key Insight]**
>
> In real-time physical systems, only causal signals exist — no system can respond to an input before it has been applied. However, in recorded (offline) processing, non-causal signals can be analyzed because the entire time history is available.

### 5.3 Bounded Signals

A signal is **bounded** if its magnitude never exceeds some finite limit $M$:

$$
|x(t)| \le M < \infty \quad \text{for all } t
$$

If no such $M$ exists, the signal is **unbounded** (e.g., $x(t) = t$).

### 5.4 Even and Odd Signals

#### Definition

A signal is **even** if $x(t) = x(-t)$ (symmetric about the vertical axis).

A signal is **odd** if $x(t) = -x(-t)$ (anti-symmetric about the vertical axis).

#### Even-Odd Decomposition

Any signal $x(t)$ can be uniquely decomposed into an even component $x_e(t)$ and an odd component $x_o(t)$:

$$
x_e(t) = \frac{x(t) + x(-t)}{2}, \qquad x_o(t) = \frac{x(t) - x(-t)}{2}
$$

Properties:
- $x_e(t) + x_o(t) = x(t)$
- $x_e(t)$ is even: $x_e(-t) = x_e(t)$
- $x_o(t)$ is odd: $x_o(-t) = -x_o(t)$

#### Multiplication Properties

| Signal 1 | Signal 2 | Product |
| :--- | :--- | :--- |
| Even | Even | Even |
| Odd | Odd | Even |
| Even | Odd | Odd |
| Odd | Even | Odd |

### 5.5 Periodic Signals

A CT signal $x(t)$ is **periodic** with period $T_0$ if:

$$
x(t + T_0) = x(t) \quad \text{for all } t \in \mathbb{R}
$$

The **fundamental period** $T_0$ is the smallest positive value for which this holds.

For a DT signal $x[n]$, periodicity requires an integer period $N_0$:

$$
x[n + N_0] = x[n] \quad \text{for all } n \in \mathbb{Z}
$$

> **[Key Insight]**
>
> A DT sinusoid $\cos(\omega_0 n)$ is periodic **only if** $\omega_0 / 2\pi$ is a rational number. This is because $\cos(\omega_0 (n + N_0)) = \cos(\omega_0 n)$ requires $\omega_0 N_0 = 2\pi k$ for integers $k, N_0$.

---

## 6. Solved Exercises

### Exercise 1: Classifying a Signal by All Criteria

**Problem:** Fully classify the signal $x(t) = 3e^{-2t}u(t)$ according to all applicable criteria.

**Solution:**

1. **Domain:** Parentheses with $t$ → **continuous-time**.
2. **Amplitude:** Continuous range $[0, 3]$ → **analog**.
3. **Duration:** $u(t)$ makes the signal zero for $t < 0$; for $t \ge 0$, the signal decays but never exactly reaches zero. It is **right-sided** and has **infinite duration**.
4. **Periodicity:** The exponential decays without repeating. It is **aperiodic**.
5. **Symmetry:** $x(t) = 0$ for $t < 0$ and $x(t) = 3e^{-2t}$ for $t \ge 0$. Since $x(-t) \neq x(t)$ and $x(-t) \neq -x(t)$, it is **neither even nor odd**.
6. **Determinism:** The signal is given by a precise formula. It is **deterministic**.
7. **Causality:** $x(t) = 0$ for $t < 0$. It is **causal**.
8. **Boundedness:** $|x(t)| \le 3$ for all $t$. It is **bounded**.
9. **Energy/Power:** Compute total energy:
   $$
   E_\infty = \int_{-\infty}^{\infty} |3e^{-2t}u(t)|^2 dt = \int_0^\infty 9e^{-4t} dt = 9\left[\frac{e^{-4t}}{-4}\right]_0^\infty = 9 \times \frac{1}{4} = \frac{9}{4}
   $$
   Finite energy → **energy signal**.

---

### Exercise 2: Energy and Power of a Rectangular Pulse

**Problem:** Compute the total energy and average power of the rectangular pulse:

$$
x(t) = 
\begin{cases}
5, & 0 \le t \le 4 \\
0, & \text{otherwise}
\end{cases}
$$

**Solution:**

Since the signal is non-zero only on $[0, 4]$, the total energy is computed over this finite interval:

$$
E_\infty = \int_{0}^{4} 5^2 dt = \int_{0}^{4} 25 dt = 25 \times 4 = 100
$$

For the average power over infinite time:

$$
P_\infty = \lim_{T \to \infty} \frac{1}{2T} \int_{-T}^{T} |x(t)|^2 dt
$$

The integral over $[-T, T]$ for $T > 4$ includes the interval $[0, 4]$ where the signal is 25, and the rest where it is 0:

$$
P_\infty = \lim_{T \to \infty} \frac{1}{2T} \times 100 = 0
$$

The signal has finite energy ($E_\infty = 100$) and zero average power → **energy signal**.

---

### Exercise 3: Time Shifting and Time Scaling Combined

**Problem:** Given $x(t)$ as shown below (a triangular pulse from $t = -1$ to $t = 1$ with peak $1$ at $t = 0$), sketch $y(t) = x(2t + 1)$.

**Solution:**

Rewrite the transformation to identify the shift and scale:

$$
x(2t + 1) = x\left(2\left(t + \frac{1}{2}\right)\right)
$$

Proceed in steps:

**Step 1:** Write the original signal mathematically:
$$
x(t) = 
\begin{cases}
1 - |t|, & |t| \le 1 \\
0, & \text{otherwise}
\end{cases}
$$

**Step 2:** Apply the transformation directly by substituting $t \to 2t + 1$:

$$
y(t) = x(2t + 1) = 
\begin{cases}
1 - |2t + 1|, & |2t + 1| \le 1 \\
0, & \text{otherwise}
\end{cases}
$$

**Step 3:** Determine the support (where the signal is non-zero):

$$
|2t + 1| \le 1 \implies -1 \le 2t + 1 \le 1 \implies -2 \le 2t \le 0 \implies -1 \le t \le 0
$$

**Step 4:** Write the explicit form on $[-1, 0]$:

$$
y(t) = 1 - |2t + 1|, \quad -1 \le t \le 0
$$

For $t$ in $[-1, 0]$, $2t + 1$ goes from $-1$ to $1$. The absolute value makes this piecewise:

- For $t \in [-1, -0.5]$: $2t + 1 \le 0$, so $|2t + 1| = -(2t + 1) = -2t - 1$. Then $y(t) = 1 - (-2t - 1) = 2t + 2$.
- For $t \in [-0.5, 0]$: $2t + 1 \ge 0$, so $|2t + 1| = 2t + 1$. Then $y(t) = 1 - (2t + 1) = -2t$.

**Step 5:** Summarize:

$$
y(t) = 
\begin{cases}
2t + 2, & -1 \le t \le -0.5 \\
-2t, & -0.5 \le t \le 0 \\
0, & \text{otherwise}
\end{cases}
$$

*Intermediate state check:* At $t = -1$: $y(-1) = 2(-1) + 2 = 0$. At $t = -0.5$: $y(-0.5) = 2(-0.5) + 2 = 1$ (from first piece) and $y(-0.5) = -2(-0.5) = 1$ (from second piece) — continuous. At $t = 0$: $y(0) = 0$. The original triangle from $[-1, 1]$ has been compressed by factor 2 (duration halved from 2 to 1) and shifted left by 0.5 units.

---

### Exercise 4: Even-Odd Decomposition of a Sinusoid

**Problem:** Decompose $x(t) = \cos(2t) + \sin(2t)$ into its even and odd components.

**Solution:**

Compute $x(-t)$:

$$
x(-t) = \cos(-2t) + \sin(-2t) = \cos(2t) - \sin(2t)
$$

Using the even/odd formulas:

$$
x_e(t) = \frac{x(t) + x(-t)}{2} = \frac{[\cos(2t) + \sin(2t)] + [\cos(2t) - \sin(2t)]}{2} = \frac{2\cos(2t)}{2} = \cos(2t)
$$

$$
x_o(t) = \frac{x(t) - x(-t)}{2} = \frac{[\cos(2t) + \sin(2t)] - [\cos(2t) - \sin(2t)]}{2} = \frac{2\sin(2t)}{2} = \sin(2t)
$$

Verification:
- $x_e(-t) = \cos(-2t) = \cos(2t) = x_e(t)$ (even)
- $x_o(-t) = \sin(-2t) = -\sin(2t) = -x_o(t)$ (odd)
- $x_e(t) + x_o(t) = \cos(2t) + \sin(2t) = x(t)$

The decomposition shows that $\cos(2t)$ is the even part and $\sin(2t)$ is the odd part of the combined signal.

---

### Exercise 5: Periodicity of a Discrete-Time Sinusoid

**Problem:** Determine whether $x[n] = \cos(0.3\pi n)$ is periodic. If so, find its fundamental period $N_0$.

**Solution:**

A DT sinusoid $\cos(\omega_0 n)$ is periodic if $\omega_0/2\pi$ is rational, i.e., there exist integers $k$ and $N_0$ such that $\omega_0 N_0 = 2\pi k$.

Here $\omega_0 = 0.3\pi$.

$$
\frac{\omega_0}{2\pi} = \frac{0.3\pi}{2\pi} = \frac{0.3}{2} = \frac{3}{20}
$$

The fraction $3/20$ is rational. Therefore the signal is periodic.

The fundamental period $N_0$ is the smallest integer such that $\omega_0 N_0$ is an integer multiple of $2\pi$:

$$
\omega_0 N_0 = 0.3\pi N_0 = 2\pi k \implies N_0 = \frac{2k}{0.3} = \frac{20k}{3}
$$

For $k = 3$: $N_0 = 20$. Since $k = 3$ and $N_0 = 20$ are coprime, the fundamental period is:

$$
N_0 = 20 \text{ samples}
$$

---

### Exercise 6: Energy of a Complex Exponential

**Problem:** Compute the total energy and average power of $x(t) = e^{j\omega_0 t}$ over the interval $[0, T_0]$ where $T_0 = 2\pi/\omega_0$, and classify the signal.

**Solution:**

**Step 1:** Compute the magnitude:

$$
|x(t)| = |e^{j\omega_0 t}| = 1
$$

The complex exponential has constant magnitude 1.

**Step 2:** Energy over one period:

$$
E_{[0,T_0]} = \int_0^{T_0} |e^{j\omega_0 t}|^2 dt = \int_0^{T_0} 1^2 dt = T_0
$$

**Step 3:** Average power over one period:

$$
P_{[0,T_0]} = \frac{1}{T_0} \int_0^{T_0} 1 dt = \frac{T_0}{T_0} = 1
$$

**Step 4:** Total energy over infinite horizon:

Since $|x(t)|^2 = 1$ for all $t$, the integral diverges:

$$
E_\infty = \int_{-\infty}^{\infty} 1 dt = \infty
$$

**Step 5:** Average power over infinite horizon:

$$
P_\infty = \lim_{T \to \infty} \frac{1}{2T} \int_{-T}^{T} 1 dt = \lim_{T \to \infty} \frac{2T}{2T} = 1
$$

**Classification:** Finite non-zero average power ($P_\infty = 1$), infinite total energy → **power signal**.

---

### Exercise 7: Combined Amplitude and Time Transformations

**Problem:** Given $x(t) = 2\cos(4\pi t)$, find and sketch $y(t) = -3x(2t - 1) + 2$.

**Solution:**

**Step 1:** Apply time transformation first: $x(2t - 1) = 2\cos(4\pi (2t - 1)) = 2\cos(8\pi t - 4\pi)$.

**Step 2:** Since $\cos(\theta - 4\pi) = \cos(\theta)$ (cosine has period $2\pi$, and $4\pi = 2 \times 2\pi$):

$$
x(2t - 1) = 2\cos(8\pi t)
$$

**Step 3:** Apply amplitude scaling: $-3x(2t - 1) = -3 \times 2\cos(8\pi t) = -6\cos(8\pi t)$.

**Step 4:** Apply vertical shift: $y(t) = -6\cos(8\pi t) + 2$.

**Step 5:** Determine the parameters of the resulting signal:
- Amplitude: $6$ (signal oscillates between $-6 + 2 = -4$ and $6 + 2 = 8$)
- Angular frequency: $\omega = 8\pi$ rad/s
- Frequency: $f = \omega/(2\pi) = 4$ Hz
- Period: $T = 1/f = 0.25$ s
- DC offset: $2$

*Intermediate state comparison:*

| Parameter | $x(t)$ | $y(t)$ |
| :--- | :--- | :--- |
| Amplitude | $2$ | $6$ |
| Frequency | $2$ Hz | $4$ Hz |
| DC offset | $0$ | $2$ |
| Phase | $0$ | $0$ |

---

### Exercise 8: Determining if a Signal is an Energy or Power Signal from a Composite

**Problem:** Classify $x(t) = e^{-t}\cos(10t)u(t)$ as an energy signal, power signal, or neither.

**Solution:**

**Step 1:** Note that $u(t)$ makes the signal zero for $t < 0$.

**Step 2:** Compute total energy:

$$
E_\infty = \int_0^\infty \left|e^{-t}\cos(10t)\right|^2 dt = \int_0^\infty e^{-2t} \cos^2(10t) dt
$$

**Step 3:** Use the identity $\cos^2\theta = \frac{1 + \cos(2\theta)}{2}$:

$$
E_\infty = \int_0^\infty e^{-2t} \cdot \frac{1 + \cos(20t)}{2} dt = \frac{1}{2} \int_0^\infty e^{-2t} dt + \frac{1}{2} \int_0^\infty e^{-2t}\cos(20t) dt
$$

**Step 4:** Evaluate the first integral:

$$
\frac{1}{2} \int_0^\infty e^{-2t} dt = \frac{1}{2} \left[ \frac{e^{-2t}}{-2} \right]_0^\infty = \frac{1}{2} \times \frac{1}{2} = \frac{1}{4}
$$

**Step 5:** Evaluate the second integral using the standard form $\int e^{at}\cos(bt) dt$ or integration by parts. For $a = -2$, $b = 20$:

$$
\int_0^\infty e^{-2t}\cos(20t) dt = \left[ \frac{e^{-2t}(-2\cos(20t) + 20\sin(20t))}{(-2)^2 + 20^2} \right]_0^\infty
$$

At $t = \infty$: the term approaches $0$ due to $e^{-2t}$.
At $t = 0$: $\frac{1(-2\cos(0) + 20\sin(0))}{404} = \frac{-2}{404} = -\frac{1}{202}$.

So the definite integral is $0 - (-\frac{1}{202}) = \frac{1}{202}$.

**Step 6:** Combine:

$$
E_\infty = \frac{1}{4} + \frac{1}{2} \times \frac{1}{202} = \frac{1}{4} + \frac{1}{404} = \frac{101}{404} + \frac{1}{404} = \frac{102}{404} = \frac{51}{202} \approx 0.2525
$$

**Classification:** Total energy is finite ($E_\infty \approx 0.2525$) → **energy signal**.

The decaying exponential envelope $e^{-t}$ ensures the signal decays to zero sufficiently fast for the energy integral to converge, despite the oscillatory $\cos(10t)$ factor.

---

## 7. Connections and Cross-References

This lecture builds directly on Lecture 01 and provides essential prerequisites for subsequent material:

- **Lecture 01** introduced the sinusoidal signal representation and basic CT/DT distinction. This lecture expands classification to all categories.
- **Lecture 03 (Elementary Signals)** uses the unit step $u(t)$ extensively for defining signals; the causal vs. non-causal distinction established here is essential for understanding when the step function is needed.
- **Lectures 05-06 (Convolution)** rely on energy/power classifications to determine whether an LTI system's output has finite energy.
- **Fourier series (Lecture 07+)** require periodicity analysis — the rational ratio test for sum periodicity is used repeatedly.
- **Sampling theorem** builds on the A/D conversion concepts introduced here, specifically sampling and quantization.

---

## 8. Exam Tip: The "Show Your Work" Checklist for Signal Classification

When an exam problem asks you to "classify the signal," examiners expect you to address **all** applicable categories. A partial answer (e.g., stating only CT/DT without energy/power) loses marks even if correct. Use this systematic checklist:

1. **Domain:** CT or DT? (Check parentheses vs. brackets.)
2. **Amplitude:** Analog or digital? (Continuous vs. discrete amplitude.)
3. **Periodicity:** Find $T_0$ or $N_0$, or prove none exists.
4. **Symmetry:** Even, odd, or neither? If decomposition is asked, show both $x_e(t)$ and $x_o(t)$.
5. **Causality:** Zero for $t < 0$?
6. **Boundedness:** Finite maximum magnitude?
7. **Duration:** Finite or infinite? Right-sided, left-sided, or two-sided?
8. **Determinism:** Predictable by formula?
9. **Energy/Power:** Compute $E_\infty$, then $P_\infty$ if $E_\infty = \infty$.

**Common mistake:** Applying the periodic sum condition incorrectly. For $x(t) = \cos(\omega_1 t) + \cos(\omega_2 t)$ to be periodic, $\omega_1/\omega_2$ must be rational — not $\omega_1/\omega_2 = 2\pi$. Always compute periods $T_1$ and $T_2$ first, then check $T_1/T_2$ for rationality.

**Memory aid for even/odd multiplication:** "Even times even = even" (like positive $\times$ positive), "odd times odd = even" (like negative $\times$ negative), "even times odd = odd" (like positive $\times$ negative). The symmetry of the product follows the sign rule.