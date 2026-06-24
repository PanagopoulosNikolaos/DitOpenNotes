# Lecture 01 - Introduction to Signals and Systems

Course overview establishing the foundational concepts of signals and systems, their mathematical representations, and their role across electrical and computer engineering disciplines. This lecture introduces the formal definition of a signal, distinguishes continuous-time from discrete-time representations, surveys key application domains, and outlines the course structure and grading policy.

---

## 1. Conceptual Foundation

### 1.1 What is a Signal?

A signal is a physical quantity that varies with one or more independent variables and conveys information about a phenomenon. In this course, the independent variable is almost always time, denoted $t$ (continuous) or $n$ (discrete integer index). The dependent variable — the signal amplitude — may represent voltage, current, pressure, temperature, displacement, or any other measurable quantity.

The fundamental operation of an engineering system is to process an input signal to produce an output signal that serves some purpose: extraction of information, modification of the signal form, control of a physical process, or communication over a channel.

### 1.2 What is a System?

A system is any entity that takes one or more input signals and produces one or more output signals according to a well-defined rule or transformation. Systems are represented generically as:

$$
y(t) = T\{x(t)\}
$$

where $x(t)$ is the input signal, $y(t)$ is the output signal, and $T\{\cdot\}$ denotes the transformation operator applied by the system.

### 1.3 Continuous-Time vs. Discrete-Time Representation

| Aspect | Continuous-Time (CT) | Discrete-Time (DT) |
| :--- | :--- | :--- |
| Independent variable | Real time $t \in \mathbb{R}$ | Integer index $n \in \mathbb{Z}$ |
| Notation | $x(t)$ | $x[n]$ |
| Source | Naturally occurring physical signals | Sampled data, digital computation |
| Amplitude | Continuous range | Continuous or quantized |
| Processing technology | Analog circuits, operational amplifiers | Digital signal processors, software |

### 1.4 Mathematical Properties of Signals

Signals are characterized by several mathematical properties that determine how they can be analyzed and processed:

- **Amplitude:** The magnitude of the signal at any instant.
- **Duration:** The time interval over which the signal is non-zero (finite or infinite).
- **Periodicity:** Whether the signal repeats exactly after a fixed period $T_0$.
- **Symmetry:** Whether the signal is even ($x(t) = x(-t)$), odd ($x(t) = -x(-t)$), or neither.
- **Boundedness:** Whether the signal amplitude remains within finite limits.
- **Determinism:** Whether the signal is exactly predictable (deterministic) or random (stochastic).

### 1.5 Applications and Fields of Engineering

Signals and systems theory underpins virtually every branch of electrical and computer engineering:

| Application Area | Signal Type | System Function |
| :--- | :--- | :--- |
| Audio processing | Acoustic pressure waveform | Filtering, compression, equalization |
| Image processing | 2D intensity function $I(x, y)$ | Edge detection, enhancement, encoding |
| Communications | Modulated electromagnetic wave | Modulation, demodulation, channel equalization |
| Control systems | Sensor voltage, actuator current | Stabilization, tracking, regulation |
| Biomedical engineering | ECG, EEG voltage traces | Diagnosis, artifact removal, feature extraction |
| Radar/sonar | Reflected pulse train | Target detection, ranging, Doppler estimation |

---

## 2. Core Definitions and Signal Representation

### 2.1 Formal Definition of a Signal

> **[Supplementary]**
>
> A signal is formally defined as a function that maps an independent variable (typically time) to a dependent variable (amplitude):
>
> $$
> x: \mathbb{R} \to \mathbb{R} \quad \text{(CT signal)}
> $$
> $$
> x: \mathbb{Z} \to \mathbb{R} \quad \text{(DT signal)}
> $$
>
> The codomain may also be $\mathbb{C}$ for complex-valued signals.

### 2.2 Sinusoidal Signals

The sinusoidal signal is the most important elementary signal in the course because it is an eigenfunction of linear time-invariant (LTI) systems.

$$
x(t) = A \cos(\omega_0 t + \phi)
$$

| Parameter | Symbol | Units | Description |
| :--- | :--- | :--- | :--- |
| Amplitude | $A$ | Same as signal | Peak deviation from zero |
| Angular frequency | $\omega_0$ | rad/s | Rate of oscillation in radians per second |
| Frequency | $f_0$ | Hz ($\text{s}^{-1}$) | Cycles per second: $\omega_0 = 2\pi f_0$ |
| Period | $T_0$ | s | Time for one complete cycle: $T_0 = 1/f_0$ |
| Phase | $\phi$ | rad | Horizontal shift relative to $t=0$ |

**Euler's formula** relates the sinusoid to complex exponentials:

$$
\cos(\theta) = \frac{e^{j\theta} + e^{-j\theta}}{2}, \qquad \sin(\theta) = \frac{e^{j\theta} - e^{-j\theta}}{2j}
$$

### 2.3 Complex Exponential Signals

The complex exponential is the fundamental building block for representing and analyzing signals:

$$
x(t) = C e^{st}
$$

where $C$ is a complex amplitude and $s = \sigma + j\omega$ is a complex frequency.

**Special cases:**

| $s$ value | Signal type | Behavior |
| :--- | :--- | :--- |
| $s = 0$ | Constant | $x(t) = C$ |
| $s = \sigma$ (real, $\sigma > 0$) | Growing real exponential | $x(t) = C e^{\sigma t}$ |
| $s = \sigma$ (real, $\sigma < 0$) | Decaying real exponential | $x(t) = C e^{\sigma t}$ |
| $s = j\omega$ (purely imaginary) | Complex sinusoid | $x(t) = C e^{j\omega t}$ |
| $s = \sigma \pm j\omega$ | Damped sinusoid | $x(t) = C e^{\sigma t} e^{\pm j\omega t}$ |

### 2.4 Unit Step Function

Defined as:

$$
u(t) = \begin{cases}
0, & t < 0 \\
1, & t > 0
\end{cases}
$$

The value at $t = 0$ is typically left undefined or set to $u(0) = 1/2$ depending on convention. The unit step is used to represent signals that turn on at a specific time.

---

## 3. Key Parameters and Constraints

### 3.1 Signal Dimensionality

Signals can be classified by the number of independent variables:

- **One-dimensional (1D):** $x(t)$ — time-domain signals (audio, voltage)
- **Two-dimensional (2D):** $I(x, y)$ — images, spatial fields
- **Three-dimensional (3D):** $V(x, y, z)$ — volumetric data, video
- **Multidimensional:** $M$ independent variables

### 3.2 Analog vs. Digital Distinction

| Property | Analog Signal | Digital Signal |
| :--- | :--- | :--- |
| Time variable | Continuous ($t$) | Discrete ($n$) |
| Amplitude | Continuous range | Discrete (quantized) levels |
| Notation | $x(t)$ | $x[n]$ with quantized values |
| Example | Microphone voltage | PCM audio bitstream |

### 3.3 Analog-to-Digital Conversion Chain

The process of converting a real-world analog signal into a digital representation involves three steps:

1. **Sampling:** Continuous time $t$ is converted to discrete integer indices $n$ at a sampling rate $f_s$ samples/second.
2. **Quantization:** The continuous amplitude is rounded to one of a finite set of discrete levels.
3. **Coding:** Each quantized level is assigned a binary codeword.

---

## 4. Step-by-Step Mechanism: Signal Analysis Procedure

When analyzing any signal encountered in this course, follow this sequence:

1. **Identify the domain:** Is the signal CT ($t$) or DT ($n$)?
2. **Determine the amplitude range:** What are the minimum and maximum values?
3. **Classify by duration:** Is the signal time-limited or infinite in extent?
4. **Check periodicity:** Does there exist a $T_0 > 0$ such that $x(t + T_0) = x(t)$ for all $t$?
5. **Examine symmetry:** Is the signal even, odd, or neither?
6. **Identify elementary building blocks:** Can the signal be expressed in terms of steps, ramps, impulses, sinusoids, or exponentials?
7. **Compute relevant metrics:** Energy, power, mean value, RMS value as appropriate.

---

## 5. Solved Exercises

### Exercise 1: Classifying a Given Signal

**Problem:** Determine whether the signal $x(t) = 5 \cos(100\pi t)$ is: (a) continuous-time or discrete-time, (b) analog or digital, (c) periodic or aperiodic. If periodic, find its period.

**Solution:**

1. The independent variable is $t \in \mathbb{R}$, so the signal is **continuous-time**.
2. The amplitude $5 \cos(100\pi t)$ takes on a continuous range of values in $[-5, 5]$, so it is **analog**.
3. A cosine is periodic: $x(t + T_0) = 5 \cos(100\pi (t + T_0))$. For equality, we need $100\pi T_0 = 2\pi k$ for some integer $k$. The fundamental period occurs at $k = 1$:
   $$
   T_0 = \frac{2\pi}{100\pi} = \frac{1}{50} = 0.02 \text{ s}
   $$

The signal is a CT analog periodic sinusoid with period $T_0 = 20$ ms.

---

### Exercise 2: Identifying Domain and Notation

**Problem:** A temperature sensor records a reading every 0.1 seconds. The recorded values are stored in a computer memory. Express the stored signal mathematically. Is it CT or DT?

**Solution:**

The sensor measures temperature $T(t)$ at discrete time instants $t = nT_s$, where $T_s = 0.1$ s is the sampling period and $n$ is an integer index. The stored signal is:

$$
T[n] = T(nT_s), \quad n = 0, 1, 2, \ldots
$$

This is a **discrete-time** signal because the independent variable is the integer index $n$, not continuous time $t$. The square-bracket notation $T[n]$ indicates a DT signal.

---

### Exercise 3: Signal Energy Calculation

**Problem:** Compute the energy of the signal $x(t) = 2$ over the interval $0 \le t \le 5$.

**Solution:**

The energy of a CT signal over a finite interval $[t_1, t_2]$ is:

$$
E = \int_{t_1}^{t_2} |x(t)|^2 dt
$$

Substituting $x(t) = 2$:

$$
E = \int_{0}^{5} 2^2 dt = \int_{0}^{5} 4 dt = 4 \times (5 - 0) = 20
$$

The energy of the signal over the 5-second interval is 20 (energy units, typically Joules if the signal represents voltage across a $1 \Omega$ resistor).

---

### Exercise 4: Average Power of a Periodic Signal

**Problem:** Calculate the average power of $x(t) = A \cos(\omega_0 t + \phi)$ over one period.

**Solution:**

The average power of a periodic signal with period $T_0$ is:

$$
P = \frac{1}{T_0} \int_{0}^{T_0} |x(t)|^2 dt
$$

Substituting $x(t) = A \cos(\omega_0 t + \phi)$:

$$
P = \frac{1}{T_0} \int_{0}^{T_0} A^2 \cos^2(\omega_0 t + \phi) dt
$$

Using the identity $\cos^2\theta = \frac{1 + \cos(2\theta)}{2}$:

$$
P = \frac{A^2}{T_0} \int_{0}^{T_0} \frac{1 + \cos(2\omega_0 t + 2\phi)}{2} dt
$$

$$
P = \frac{A^2}{2T_0} \left[ \int_{0}^{T_0} 1 dt + \int_{0}^{T_0} \cos(2\omega_0 t + 2\phi) dt \right]
$$

The second integral is zero because it integrates a cosine over an integer number of periods. Therefore:

$$
P = \frac{A^2}{2T_0} \times T_0 = \frac{A^2}{2}
$$

The average power of a sinusoidal signal depends only on the amplitude, not on the frequency or phase.

---

### Exercise 5: Signal Arithmetic — Addition

**Problem:** Two signals are defined as $x_1(t) = 3 \cos(2\pi t)$ and $x_2(t) = 1$. Sketch the sum $y(t) = x_1(t) + x_2(t)$ over $0 \le t \le 2$ and describe its behavior.

**Solution:**

The sum is:

$$
y(t) = 3 \cos(2\pi t) + 1
$$

This is a sinusoid with amplitude 3, shifted vertically upward by 1 unit. Over $0 \le t \le 2$:

- At $t = 0$: $y(0) = 3 \cos(0) + 1 = 3 + 1 = 4$
- At $t = 0.5$: $y(0.5) = 3 \cos(\pi) + 1 = -3 + 1 = -2$
- At $t = 1$: $y(1) = 3 \cos(2\pi) + 1 = 3 + 1 = 4$
- At $t = 1.5$: $y(1.5) = 3 \cos(3\pi) + 1 = -3 + 1 = -2$
- At $t = 2$: $y(2) = 3 \cos(4\pi) + 1 = 3 + 1 = 4$

The waveform oscillates between $-2$ and $4$, with a period of 1 second and a DC offset of 1.

*Intermediate state before final sketch:*

| $t$ | $x_1(t) = 3 \cos(2\pi t)$ | $x_2(t) = 1$ | $y(t)$ |
| :--- | :--- | :--- | :--- |
| 0.0 | 3.00 | 1 | 4.00 |
| 0.1 | 2.43 | 1 | 3.43 |
| 0.2 | 0.93 | 1 | 1.93 |
| 0.3 | -0.93 | 1 | 0.07 |
| 0.4 | -2.43 | 1 | -1.43 |
| 0.5 | -3.00 | 1 | -2.00 |
| 0.6 | -2.43 | 1 | -1.43 |
| 0.7 | -0.93 | 1 | 0.07 |
| 0.8 | 0.93 | 1 | 1.93 |
| 0.9 | 2.43 | 1 | 3.43 |
| 1.0 | 3.00 | 1 | 4.00 |

The result is a cosine wave vertically shifted upward by 1 unit.

---

### Exercise 6: Distinguishing Energy Signals from Power Signals

**Problem:** Classify each of the following signals as an energy signal, a power signal, or neither.

(a) $x_a(t) = e^{-2t} u(t)$
(b) $x_b(t) = 5 \cos(10t)$
(c) $x_c(t) = 3$ (for all $t$)

**Solution:**

A signal is an **energy signal** if its total energy $E_\infty$ is finite ($0 < E_\infty < \infty$). A signal is a **power signal** if its average power $P_\infty$ is finite and non-zero ($0 < P_\infty < \infty$). A signal cannot be both because finite energy implies zero average power over infinite time.

**(a)** $x_a(t) = e^{-2t} u(t)$:

$$
E_\infty = \int_{-\infty}^{\infty} |e^{-2t} u(t)|^2 dt = \int_{0}^{\infty} e^{-4t} dt = \left[ \frac{e^{-4t}}{-4} \right]_0^\infty = 0 - \left(-\frac{1}{4}\right) = \frac{1}{4}
$$

Energy is finite ($1/4$). Therefore $x_a(t)$ is an **energy signal**.

**(b)** $x_b(t) = 5 \cos(10t)$:

Using the result from Exercise 4, the average power over one period is $P = A^2/2 = 25/2 = 12.5$. Since the power is finite and non-zero, and the energy over infinite time is infinite, this is a **power signal**.

**(c)** $x_c(t) = 3$:

$$
P_\infty = \lim_{T \to \infty} \frac{1}{2T} \int_{-T}^{T} 3^2 dt = \lim_{T \to \infty} \frac{9 \cdot 2T}{2T} = 9
$$

Average power is $9$, finite and non-zero, so it is a **power signal**.

---

### Exercise 7: Even and Odd Decomposition

**Problem:** Decompose $x(t) = e^{-t} u(t)$ into its even part $x_e(t)$ and odd part $x_o(t)$.

**Solution:**

Any signal can be decomposed into even and odd components:

$$
x_e(t) = \frac{x(t) + x(-t)}{2}, \qquad x_o(t) = \frac{x(t) - x(-t)}{2}
$$

First compute $x(-t)$:

$$
x(-t) = e^{-(-t)} u(-t) = e^{t} u(-t)
$$

Now compute the even part:

$$
x_e(t) = \frac{e^{-t} u(t) + e^{t} u(-t)}{2}
$$

And the odd part:

$$
x_o(t) = \frac{e^{-t} u(t) - e^{t} u(-t)}{2}
$$

Verification that $x_e(t) = x_e(-t)$ and $x_o(-t) = -x_o(t)$:

- For $x_e(-t)$: $\frac{e^{t} u(-t) + e^{-t} u(t)}{2} = x_e(t)$ (even)
- For $x_o(-t)$: $\frac{e^{t} u(-t) - e^{-t} u(t)}{2} = -x_o(t)$ (odd)

And $x_e(t) + x_o(t) = \frac{e^{-t} u(t) + e^{t} u(-t) + e^{-t} u(t) - e^{t} u(-t)}{2} = \frac{2 e^{-t} u(t)}{2} = e^{-t} u(t) = x(t)$.

---

### Exercise 8: Periodicity of Sinusoidal Sums

**Problem:** Determine whether the signal $x(t) = \cos(2\pi t) + \cos(3\pi t)$ is periodic. If so, find its fundamental period.

**Solution:**

A sum of periodic signals is periodic if and only if the ratio of their periods is rational.

For $\cos(2\pi t)$: $\omega_1 = 2\pi$, so $T_1 = \frac{2\pi}{\omega_1} = 1$ s.

For $\cos(3\pi t)$: $\omega_2 = 3\pi$, so $T_2 = \frac{2\pi}{\omega_2} = \frac{2}{3}$ s.

Check the ratio:

$$
\frac{T_1}{T_2} = \frac{1}{2/3} = \frac{3}{2}
$$

The ratio $3/2$ is rational, so the sum is periodic. The fundamental period is the least common multiple of $T_1$ and $T_2$:

$$
T_0 = \text{lcm}(1, 2/3) = \text{lcm}(1, 0.\overline{6})
$$

Convert to fractions with a common denominator: $T_1 = 1 = \frac{3}{3}$, $T_2 = \frac{2}{3}$.

The fundamental period is the smallest $T_0$ such that $T_0 = m T_1 = n T_2$ for integers $m, n$:

$T_0 = 2 \times 1 = 2$ s, and $T_0 = 3 \times \frac{2}{3} = 2$ s.

The signal is periodic with fundamental period $T_0 = 2$ seconds.

---

## 6. Connections and Cross-References

This introductory lecture establishes the language and notation used throughout the entire course:

- **Lecture 02** extends the signal classification (energy/power, even/odd, periodic/aperiodic) and introduces time-domain transformations (shifting, scaling, reversal).
- **Lecture 03** formally defines the elementary signals (unit step, impulse, ramp, exponential, sinusoid, sinc, impulse train) that serve as building blocks for all subsequent system analysis.
- **Convolution (Lectures 05-06)** relies on representing signals as sums of shifted impulses — a concept introduced here through the CT/DT formalism.
- **Fourier series and transforms** reuse the sinusoidal and complex exponential representations introduced in this lecture.
- **Sampling theorem** is built on the analog-to-digital conversion concepts previewed here.

---

## 7. Exam Tip: Understanding the Core Classification Framework

The single most common exam mistake in this course is misidentifying whether a signal is CT or DT based on the notation. Two rules will protect you:

1. **Parentheses $x(t)$ mean continuous-time.** Round parentheses always imply a real-valued independent variable. If you see $x(2t)$ or $x(t-3)$, the argument is a real number — the signal is CT.

2. **Square brackets $x[n]$ mean discrete-time.** Square brackets always imply an integer-valued independent variable. If you see $x[2n]$ or $x[n-3]$, $n$ is an integer — the signal is DT.

A second common error: confusing "analog" with "continuous-time" and "digital" with "discrete-time." A discrete-time signal can still be analog if its amplitude is continuous (e.g., a sampled but unquantized waveform). A signal becomes digital only after quantization. Always check both axes independently.

On any exam, when asked to classify a signal, always provide the full four-part answer: (1) CT or DT, (2) analog or digital, (3) periodic or aperiodic (if applicable), (4) energy or power signal (if applicable). Each classification tests a distinct concept.