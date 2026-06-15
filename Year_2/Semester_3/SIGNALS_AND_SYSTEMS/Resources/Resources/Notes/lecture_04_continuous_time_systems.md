# Lecture 04 - Continuous-Time Systems

Foundations of continuous-time system analysis, covering the representation of signals as superpositions of shifted impulses, the definition and classification of systems, and the core concepts of linearity and time-invariance. This lecture establishes the theoretical groundwork for Linear Time-Invariant (LTI) system analysis, which is the central framework of signals and systems. System classification by input-output count, signal nature, and state behavior is introduced, followed by rigorous definitions and testing procedures for linearity and time-invariance.

---

## 1. Conceptual Foundation

### 1.1 Why System Classification Matters

Real-world systems — electronic circuits, communication channels, control systems, biological signal processors — can be modeled mathematically as mappings from input signals to output signals. The mathematical properties of this mapping determine which analytical tools can be applied. Linear Time-Invariant (LTI) systems, in particular, admit the powerful convolution integral representation and enable frequency-domain analysis via Fourier and Laplace transforms.

Before applying these tools, one must determine whether a given system satisfies the properties of linearity and time-invariance. Misclassifying a non-linear or time-varying system as LTI leads to incorrect predictions. The classification framework introduced in this lecture provides the systematic testing procedures needed to make this determination.

### 1.2 Representing Arbitrary Signals as Integrals of Shifted Impulses

The Dirac delta function introduced in Lecture 03 enables a fundamental representation: any continuous-time signal $x(t)$ can be expressed as a superposition (integral) of weighted, shifted impulses. This is the **sifting property** expressed as a synthesis equation:

$$
x(t) = \int_{-\infty}^{\infty} x(\tau) \delta(t - \tau) \, d\tau
$$

This identity states that the signal $x(t)$ at time $t$ is the sum of all impulse contributions $x(\tau)\delta(t - \tau)$ across all times $\tau$. While it appears tautological, this representation is the foundation for deriving the convolution integral: the output of a linear system to an arbitrary input can be computed by superimposing the system's responses to each individual impulse component.

> **[Key Insight]**
>
> The expression $x(t) = \int x(\tau) \delta(t - \tau) d\tau$ is not a mathematical trick — it is the conceptual bridge between the impulse response of a system and its response to any arbitrary input. If a system is linear, its response to the weighted integral of impulses equals the weighted integral of its responses to each impulse.

---

## 2. Formal Definition or Model

### 2.1 Definition of a System

A **system** is a mathematical abstraction that maps an input signal $x(t)$ to an output signal $y(t)$. This mapping is denoted by the operator $S$:

$$
y(t) = S\{x(t)\}
$$

A system may have multiple inputs and multiple outputs. The general representation for a system with $M$ inputs and $N$ outputs is:

$$
y_i(t) = S_i\{x_1(t), x_2(t), \ldots, x_M(t)\}, \quad i = 1, 2, \ldots, N
$$

### 2.2 Block Diagram Representation

Systems are represented graphically using block diagrams. A basic block diagram for a Single-Input Single-Output (SISO) system:

```text
        +---------+
x(t) -->| System  |--> y(t)
        |   S     |
        +---------+
```

For multi-variable systems, multiple input and output arrows are used:

```text
                +---------+
x1(t) -------->|         |--> y1(t)
x2(t) -------->| System  |--> y2(t)
                |   S     |
xM(t) -------->|         |--> yN(t)
                +---------+
```

### 2.3 System Classification by Input-Output Count

| Classification | Inputs | Outputs | Example |
| :--- | :--- | :--- | :--- |
| **SISO** (Single-Input Single-Output) | 1 | 1 | A simple RC low-pass filter |
| **MISO** (Multiple-Input Single-Output) | $M \ge 2$ | 1 | Audio mixer combining multiple channels |
| **SIMO** (Single-Input Multiple-Output) | 1 | $N \ge 2$ | A filter with two outputs (e.g., low-pass and high-pass branches) |
| **MIMO** (Multiple-Input Multiple-Output) | $M \ge 2$ | $N \ge 2$ | MIMO wireless communication channel, multi-variable control system |

### 2.4 System Classification by Signal Nature

| Classification | Input Signal | Output Signal |
| :--- | :--- | :--- |
| **Continuous-Time System** | $x(t)$, continuous-time | $y(t)$, continuous-time |
| **Discrete-Time System** | $x[n]$, discrete-time | $y[n]$, discrete-time |
| **Deterministic System** | $x(t)$ is deterministic | $y(t)$ is deterministic |
| **Stochastic System** | $x(t)$ is random | $y(t)$ is random |

A continuous-time system processes signals defined on a continuum of time values $t \in \mathbb{R}$. A discrete-time system processes signals defined only at integer instants $n \in \mathbb{Z}$. The same physical plant may be modeled as either type depending on whether the input is analog or sampled.

> **[Supplementary]**
>
> Systems can also be classified as **analog** or **digital** based on whether the amplitude values are continuous or quantized. An analog system processes signals with continuous amplitude; a digital system processes signals with quantized (discrete) amplitude. All four combinations are possible: a digital computer processing sampled sensor data is a discrete-time digital system; an analog filter processing a continuous voltage is a continuous-time analog system.

### 2.5 System State and State of Rest

The **state** of a system at time $t_0$ is a set of quantities that, together with the input for $t \ge t_0$, determines the output for $t \ge t_0$. The state encapsulates all past history of the system that is relevant to its future behavior.

A system is said to be at **state of rest** (or **initial rest**) at $t = t_0$ if the output for $t \ge t_0$ is zero when the input for $t \ge t_0$ is zero. In other words, no energy is stored in the system at $t = t_0$.

For LTI systems, the state of rest at $t = -\infty$ is typically assumed so that the system's response is entirely determined by the input — there is no initial stored energy. Under this assumption, the system is **causal** and **linear** with respect to the input applied for all time.

### 2.6 Linear Systems

A system $S$ is **linear** if it satisfies the **superposition principle**: the response to a weighted sum of inputs equals the weighted sum of the responses to each individual input.

Formally, a system is linear if for any two inputs $x_1(t)$ and $x_2(t)$ and any scalars $\alpha, \beta \in \mathbb{R}$ (or $\mathbb{C}$):

$$
S\{\alpha x_1(t) + \beta x_2(t)\} = \alpha S\{x_1(t)\} + \beta S\{x_2(t)\}
$$

Linearity comprises two sub-properties that must both hold:

#### Homogeneity (Scaling)

If the input is scaled by a constant factor $\alpha$, the output is scaled by the same factor:

$$
S\{\alpha x(t)\} = \alpha S\{x(t)\}, \quad \forall \alpha \in \mathbb{R}
$$

#### Additivity

The response to the sum of two inputs equals the sum of the responses to each input individually:

$$
S\{x_1(t) + x_2(t)\} = S\{x_1(t)\} + S\{x_2(t)\}
$$

#### Superposition Principle

Combining homogeneity and additivity gives the full superposition principle as stated above. This is the single condition that must be tested.

#### Methods for Linearity Testing

To test whether a system defined by $y(t) = T\{x(t)\}$ is linear:

1. Compute $y_1(t) = T\{x_1(t)\}$ and $y_2(t) = T\{x_2(t)\}$.
2. Form the weighted combination: $y_{\text{sum}}(t) = T\{\alpha x_1(t) + \beta x_2(t)\}$.
3. Form the weighted combination of individual responses: $y_{\text{expected}}(t) = \alpha y_1(t) + \beta y_2(t)$.
4. If $y_{\text{sum}}(t) = y_{\text{expected}}(t)$ for all $t$, all $\alpha, \beta$, and all $x_1(t), x_2(t)$, the system is linear.

If any single counter-example violates the equality, the system is **non-linear**.

> **[Key Insight]**
>
> A common mistake is to check only additivity or only homogeneity. A system may satisfy one but not the other. For example, a system $y(t) = \sqrt{x(t)}$ is homogeneous for $\alpha \ge 0$ but not additive. Both conditions are required for full linearity.

### 2.7 Time-Invariant Systems

A system is **time-invariant** (or **shift-invariant**) if a time shift in the input produces an identical time shift in the output, with no change in the output's shape.

Formally, a system $S$ is time-invariant if for any input $x(t)$ and any time shift $t_0 \in \mathbb{R}$:

$$
y(t - t_0) = S\{x(t - t_0)\}
$$

where $y(t) = S\{x(t)\}$.

#### Methods for Time-Invariance Testing

To test whether a system is time-invariant:

1. Compute the response to the original input: $y(t) = T\{x(t)\}$.
2. Shift the input by $t_0$: $x_{\text{shifted}}(t) = x(t - t_0)$.
3. Compute the response to the shifted input: $y_{\text{delayed}}(t) = T\{x(t - t_0)\}$.
4. Compute the shifted version of the original output: $y(t - t_0)$.
5. If $y_{\text{delayed}}(t) = y(t - t_0)$ for all $t$ and all $t_0$, the system is time-invariant.

If the system's behavior depends explicitly on time (e.g., the coefficients of a differential equation are functions of $t$), the system is **time-varying**.

---

## 3. Key Parameters and Constraints

### 3.1 System Classification Parameters

| Property | Description | Values | Impact |
| :--- | :--- | :--- | :--- |
| Input count $M$ | Number of input signals | $M \ge 1$, integer | Determines analysis complexity |
| Output count $N$ | Number of output signals | $N \ge 1$, integer | Determines monitoring complexity |
| Signal domain | Time variable type | Continuous ($t \in \mathbb{R}$) or Discrete ($n \in \mathbb{Z}$) | Determines analysis toolset |
| Signal nature | Deterministic or stochastic | Deterministic / Stochastic | Determines statistical vs. exact analysis |
| State | Initial energy storage at $t_0$ | State vector | Non-zero initial state produces zero-input response |
| Linearity | Superposition validity | Linear / Non-linear | Determines applicability of convolution, Fourier, Laplace |
| Time-invariance | Shift equivalence | Time-invariant / Time-varying | Determines whether impulse response is a function of one variable |

### 3.2 Constraints for Linear Time-Invariant Systems

For a system to be classified as LTI, both conditions must hold simultaneously. The combination of linearity and time-invariance produces uniquely powerful analytical properties:

| Property | LTI Consequence |
| :--- | :--- |
| Impulse response | $h(t) = S\{\delta(t)\}$ fully characterizes the system |
| Convolution | $y(t) = x(t) * h(t) = \int_{-\infty}^{\infty} x(\tau) h(t - \tau) d\tau$ |
| Eigenfunctions | Complex exponentials $e^{st}$ are eigenfunctions: output is $H(s) e^{st}$ |
| Frequency response | $H(j\omega) = \mathcal{F}\{h(t)\}$ describes steady-state sinusoidal behavior |
| Stability | BIBO stability $\iff \int_{-\infty}^{\infty} \|h(t)\| dt < \infty$ |

---

## 4. Step-by-Step Mechanisms

### 4.1 Procedure for Testing Linearity

**Algorithm:**

1. **Select two test inputs** $x_1(t)$ and $x_2(t)$ that are linearly independent (e.g., $x_1(t) = 1$ and $x_2(t) = t$, or $x_1(t) = u(t)$ and $x_2(t) = \delta(t)$).
2. **Compute individual responses:** $y_1(t) = T\{x_1(t)\}$ and $y_2(t) = T\{x_2(t)\}$.
3. **Form a linear combination:** $x_{\text{test}}(t) = \alpha x_1(t) + \beta x_2(t)$.
4. **Compute the response to the combination:** $y_{\text{test}}(t) = T\{x_{\text{test}}(t)\}$.
5. **Form the combination of individual responses:** $y_{\text{comb}}(t) = \alpha y_1(t) + \beta y_2(t)$.
6. **Compare for all $t$:** If $y_{\text{test}}(t) = y_{\text{comb}}(t)$ holds for all $t$, all $\alpha, \beta$, and all choices of $x_1, x_2$, the system is linear. Otherwise, it is non-linear.

### 4.2 Procedure for Testing Time-Invariance

**Algorithm:**

1. **Select a test input** $x(t)$ and **compute the response:** $y(t) = T\{x(t)\}$.
2. **Choose a time shift** $t_0$ (e.g., $t_0 = 1$).
3. **Compute the shifted input:** $x_{\text{shift}}(t) = x(t - t_0)$.
4. **Compute the response to the shifted input:** $y_{\text{shift}}(t) = T\{x(t - t_0)\}$.
5. **Shift the original output:** $y_{\text{delayed}}(t) = y(t - t_0)$.
6. **Compare:** If $y_{\text{shift}}(t) = y_{\text{delayed}}(t)$ for all $t$ and all choices of $t_0$ and $x(t)$, the system is time-invariant.

### 4.3 Procedure for Identifying System Type by Input-Output Count

1. **Count distinct input signals** entering the system block.
2. **Count distinct output signals** leaving the system block.
3. **Classify using the table:**
   - (1, 1) $\to$ SISO
   - ($M \ge 2$, 1) $\to$ MISO
   - (1, $N \ge 2$) $\to$ SIMO
   - ($M \ge 2$, $N \ge 2$) $\to$ MIMO

### 4.4 Procedure for Determining if a System is at State of Rest

1. **Set the input to zero** for $t \ge t_0$: $x(t) = 0$ for $t \ge t_0$.
2. **Observe the output** $y(t)$ for $t \ge t_0$.
3. **If $y(t) = 0$ for all $t \ge t_0$:** the system is at state of rest at $t = t_0$.
4. **If $y(t) \neq 0$:** the system has non-zero initial energy storage and its output includes a **zero-input response** component.

---

## 5. Worked Examples

### Exercise 1: Testing Linearity of a Simple Algebraic System

**Problem:** Determine whether the system $y(t) = 2x(t) + 3$ is linear.

**Solution:**

**Step 1:** Select two test inputs. Let $x_1(t) = 1$ and $x_2(t) = t$.

**Step 2:** Compute individual responses:
$$
y_1(t) = 2(1) + 3 = 5
$$
$$
y_2(t) = 2t + 3
$$

**Step 3:** Form a linear combination with $\alpha = 2$, $\beta = 3$:
$$
x_{\text{test}}(t) = 2 \cdot 1 + 3 \cdot t = 2 + 3t
$$

**Step 4:** Compute the response to the combination:
$$
y_{\text{test}}(t) = 2(2 + 3t) + 3 = 4 + 6t + 3 = 6t + 7
$$

**Step 5:** Form the combination of individual responses:
$$
y_{\text{comb}}(t) = \alpha y_1(t) + \beta y_2(t) = 2 \cdot 5 + 3 \cdot (2t + 3) = 10 + 6t + 9 = 6t + 19
$$

**Step 6:** Compare:
$$
y_{\text{test}}(t) = 6t + 7 \neq 6t + 19 = y_{\text{comb}}(t)
$$

The equality fails. The system is **non-linear**.

*Verification with simpler counter-example:* The term $+3$ is a constant offset that violates homogeneity. For $\alpha = 2$ and $x(t) = 1$:
- $T\{\alpha x(t)\} = T\{2\} = 2(2) + 3 = 7$
- $\alpha T\{x(t)\} = 2 \cdot (2(1) + 3) = 2 \cdot 5 = 10$
Since $7 \neq 10$, homogeneity fails.

---

### Exercise 2: Testing Linearity of an Integrator

**Problem:** Determine whether the system $y(t) = \int_{-\infty}^{t} x(\tau) \, d\tau$ is linear.

**Solution:**

**Step 1:** Select test inputs. Let $x_1(t) = u(t)$ (unit step) and $x_2(t) = \delta(t)$ (impulse).

**Step 2:** Compute individual responses:
$$
y_1(t) = \int_{-\infty}^{t} u(\tau) \, d\tau = r(t) = t \cdot u(t)
$$
$$
y_2(t) = \int_{-\infty}^{t} \delta(\tau) \, d\tau = u(t)
$$

**Step 3:** Form a linear combination with arbitrary $\alpha, \beta$:
$$
x_{\text{test}}(t) = \alpha u(t) + \beta \delta(t)
$$

**Step 4:** Compute the response to the combination:
$$
y_{\text{test}}(t) = \int_{-\infty}^{t} [\alpha u(\tau) + \beta \delta(\tau)] \, d\tau = \alpha \int_{-\infty}^{t} u(\tau) d\tau + \beta \int_{-\infty}^{t} \delta(\tau) d\tau = \alpha r(t) + \beta u(t)
$$

**Step 5:** Form the combination of individual responses:
$$
y_{\text{comb}}(t) = \alpha y_1(t) + \beta y_2(t) = \alpha r(t) + \beta u(t)
$$

**Step 6:** Compare:
$$
y_{\text{test}}(t) = \alpha r(t) + \beta u(t) = y_{\text{comb}}(t)
$$

The equality holds for all $\alpha, \beta$, all $t$, and all inputs. The integrator is **linear**.

> **[Supplementary]**
>
> The integrator is also linear when the lower limit is a finite constant: $y(t) = \int_{t_0}^{t} x(\tau) d\tau + y(t_0)$, provided the initial condition $y(t_0)$ is treated as part of the zero-input response. However, if $y(t_0)$ is non-zero, the system is only linear with respect to the input if the initial condition is considered separately.

---

### Exercise 3: Testing Time-Invariance of a Modulator

**Problem:** Determine whether the system $y(t) = \cos(\omega_0 t) \cdot x(t)$ (a sinusoidal modulator) is time-invariant.

**Solution:**

**Step 1:** Select a test input. Let $x(t) = u(t)$.

**Step 2:** Compute the response to $x(t)$:
$$
y(t) = \cos(\omega_0 t) \cdot u(t) = \cos(\omega_0 t) u(t)
$$

**Step 3:** Choose a time shift $t_0 = 1$ and compute the shifted input:
$$
x_{\text{shift}}(t) = x(t - 1) = u(t - 1)
$$

**Step 4:** Compute the response to the shifted input:
$$
y_{\text{shift}}(t) = T\{u(t - 1)\} = \cos(\omega_0 t) \cdot u(t - 1)
$$

**Step 5:** Shift the original output:
$$
y(t - 1) = \cos(\omega_0 (t - 1)) \cdot u(t - 1) = \cos(\omega_0 t - \omega_0) \cdot u(t - 1)
$$

**Step 6:** Compare for all $t$:
$$
y_{\text{shift}}(t) = \cos(\omega_0 t) u(t - 1)
$$
$$
y(t - 1) = \cos(\omega_0 t - \omega_0) u(t - 1)
$$

For $t > 1$, $u(t - 1) = 1$, so the comparison reduces to:
$$
\cos(\omega_0 t) \stackrel{?}{=} \cos(\omega_0 t - \omega_0)
$$

These are equal only if $\omega_0 = 2\pi k$ for integer $k$ (i.e., if the modulation frequency is zero, making the system trivial). For a general non-zero $\omega_0$, the two expressions differ. The system is **time-varying**.

*Physical interpretation:* A modulator multiplies the input by a time-dependent function $\cos(\omega_0 t)$. Because the multiplying function itself depends on absolute time, a shift in the input produces an output that is not simply the shifted version of the original output.

---

### Exercise 4: Combined Test for Linearity and Time-Invariance of a Differentiator

**Problem:** Determine whether the system $y(t) = \frac{dx}{dt}$ (the ideal differentiator) is:
(a) Linear
(b) Time-invariant

**Solution:**

**(a) Linearity test:**

**Step 1:** Select test inputs $x_1(t) = t^2$ and $x_2(t) = \sin(t)$.

**Step 2:** Compute individual responses:
$$
y_1(t) = \frac{d}{dt}(t^2) = 2t
$$
$$
y_2(t) = \frac{d}{dt}(\sin(t)) = \cos(t)
$$

**Step 3:** Form a linear combination with arbitrary $\alpha, \beta$:
$$
x_{\text{test}}(t) = \alpha t^2 + \beta \sin(t)
$$

**Step 4:** Compute the response to the combination:
$$
y_{\text{test}}(t) = \frac{d}{dt}[\alpha t^2 + \beta \sin(t)] = \alpha \cdot 2t + \beta \cdot \cos(t)
$$

**Step 5:** Form the combination of individual responses:
$$
y_{\text{comb}}(t) = \alpha \cdot 2t + \beta \cdot \cos(t)
$$

**Step 6:** $y_{\text{test}}(t) = y_{\text{comb}}(t)$ for all $t$, all $\alpha, \beta$, all inputs. The differentiator is **linear**.

**(b) Time-invariance test:**

**Step 1:** Select test input $x(t) = t^2$.

**Step 2:** Compute the response: $y(t) = 2t$.

**Step 3:** Choose $t_0 = 2$ and form $x_{\text{shift}}(t) = (t - 2)^2$.

**Step 4:** Compute response to shifted input:
$$
y_{\text{shift}}(t) = \frac{d}{dt}[(t - 2)^2] = 2(t - 2) = 2t - 4
$$

**Step 5:** Shift the original output:
$$
y(t - 2) = 2(t - 2) = 2t - 4
$$

**Step 6:** $y_{\text{shift}}(t) = 2t - 4 = y(t - 2)$ for all $t$. The differentiator is **time-invariant**.

The ideal differentiator is **LTI** (Linear Time-Invariant).

---

### Exercise 5: Testing Linearity of a Square-Law System

**Problem:** Determine whether the system $y(t) = x^2(t)$ is linear.

**Solution:**

**Step 1:** Select test inputs $x_1(t) = 1$ and $x_2(t) = t$.

**Step 2:** Compute individual responses:
$$
y_1(t) = 1^2 = 1
$$
$$
y_2(t) = t^2
$$

**Step 3:** Form a linear combination with $\alpha = 2$, $\beta = 1$:
$$
x_{\text{test}}(t) = 2 \cdot 1 + 1 \cdot t = t + 2
$$

**Step 4:** Compute the response to the combination:
$$
y_{\text{test}}(t) = (t + 2)^2 = t^2 + 4t + 4
$$

**Step 5:** Form the combination of individual responses:
$$
y_{\text{comb}}(t) = \alpha y_1(t) + \beta y_2(t) = 2 \cdot 1 + 1 \cdot t^2 = t^2 + 2
$$

**Step 6:** Compare:
$$
y_{\text{test}}(t) = t^2 + 4t + 4 \neq t^2 + 2 = y_{\text{comb}}(t)
$$

The equality fails. The square-law system is **non-linear**.

*Geometric interpretation:* The squaring operation produces cross-terms ($2\alpha\beta x_1 x_2$) when applied to a sum, which are absent from the sum of individual squares. This cross-term generation is characteristic of all non-linear systems.

---

### Exercise 6: Testing Time-Invariance of a System with Time-Dependent Coefficients

**Problem:** Determine whether the system $y(t) = t \cdot x(t)$ is time-invariant.

**Solution:**

**Step 1:** Select a test input. Let $x(t) = u(t)$.

**Step 2:** Compute the response:
$$
y(t) = t \cdot u(t) = r(t)
$$

**Step 3:** Choose $t_0 = 3$ and form $x_{\text{shift}}(t) = u(t - 3)$.

**Step 4:** Compute response to shifted input:
$$
y_{\text{shift}}(t) = t \cdot u(t - 3) = t \cdot u(t - 3)
$$

**Step 5:** Shift the original output:
$$
y(t - 3) = (t - 3) \cdot u(t - 3)
$$

**Step 6:** Compare for $t > 3$ (where $u(t - 3) = 1$):
$$
y_{\text{shift}}(t) = t, \quad y(t - 3) = t - 3
$$

Since $t \neq t - 3$, the system is **time-varying** (and also non-linear if amplitude scaling is applied to the input $t$, but time-variance is the dominant property here).

*Physical interpretation:* The system multiplies the input by the absolute time variable $t$. This is analogous to a potentiometer whose gain is mechanically linked to a clock — the system's behavior changes as time progresses, independent of the input.

---

### Exercise 7: Testing Linearity of a System with Memory (RC Circuit)

**Problem:** A system is described by the differential equation:
$$
\frac{dy}{dt} + 2y(t) = x(t)
$$
Assuming the system is initially at rest ($y(0) = 0$), determine whether it is linear.

**Solution:**

**Step 1:** Solve the differential equation for a generic input. This is a first-order linear ODE with integrating factor $e^{2t}$:
$$
\frac{d}{dt}[e^{2t}y(t)] = e^{2t}x(t)
$$

Integrating from $0$ to $t$ (with $y(0) = 0$):
$$
e^{2t}y(t) = \int_{0}^{t} e^{2\tau} x(\tau) d\tau
$$

$$
y(t) = e^{-2t} \int_{0}^{t} e^{2\tau} x(\tau) d\tau
$$

**Step 2:** Select test inputs $x_1(t) = u(t)$ and $x_2(t) = 1$.

**Step 3:** Compute individual responses:
$$
y_1(t) = e^{-2t} \int_{0}^{t} e^{2\tau} \cdot 1 \, d\tau = e^{-2t} \left[\frac{e^{2\tau}}{2}\right]_{0}^{t} = e^{-2t} \cdot \frac{e^{2t} - 1}{2} = \frac{1}{2}(1 - e^{-2t}) u(t)
$$

$$
y_2(t) = e^{-2t} \int_{0}^{t} e^{2\tau} \cdot 1 \, d\tau = \frac{1}{2}(1 - e^{-2t}) u(t)
$$

**Step 4:** Form a linear combination $x_{\text{test}}(t) = \alpha u(t) + \beta \cdot 1 = (\alpha + \beta) u(t)$ (both are constants for $t > 0$):
$$
y_{\text{test}}(t) = e^{-2t} \int_{0}^{t} e^{2\tau} (\alpha + \beta) \, d\tau = (\alpha + \beta) \cdot \frac{1}{2}(1 - e^{-2t}) u(t)
$$

**Step 5:** Form the combination of individual responses:
$$
y_{\text{comb}}(t) = \alpha \cdot \frac{1}{2}(1 - e^{-2t}) u(t) + \beta \cdot \frac{1}{2}(1 - e^{-2t}) u(t) = (\alpha + \beta) \cdot \frac{1}{2}(1 - e^{-2t}) u(t)
$$

**Step 6:** $y_{\text{test}}(t) = y_{\text{comb}}(t)$ for all $t$, all $\alpha, \beta$, all inputs. The system (at initial rest) is **linear**.

*Key point:* The initial condition $y(0) = 0$ is crucial. If $y(0) \neq 0$, the system would not be linear because the zero-input response would appear as an additive constant independent of the input, violating homogeneity.

---

### Exercise 8: Testing Both Properties on a System with a Threshold

**Problem:** A system is defined by:
$$
y(t) =
\begin{cases}
0, & x(t) < 0 \\
x(t), & x(t) \ge 0
\end{cases}
$$
This is a **half-wave rectifier**. Determine whether it is (a) linear and (b) time-invariant.

**Solution:**

**(a) Linearity test:**

**Step 1:** Select test inputs $x_1(t) = -1$ (negative) and $x_2(t) = 2$ (positive).

**Step 2:** Compute individual responses:
$$
y_1(t) = 0 \quad (\text{since } x_1(t) = -1 < 0)
$$
$$
y_2(t) = 2 \quad (\text{since } x_2(t) = 2 \ge 0)
$$

**Step 3:** Form $x_{\text{test}}(t) = 1 \cdot x_1(t) + 1 \cdot x_2(t) = -1 + 2 = 1$.

**Step 4:** Compute the response to the combination:
$$
y_{\text{test}}(t) = 1 \quad (\text{since } x_{\text{test}}(t) = 1 \ge 0)
$$

**Step 5:** Form the combination of individual responses:
$$
y_{\text{comb}}(t) = 1 \cdot 0 + 1 \cdot 2 = 2
$$

**Step 6:** $y_{\text{test}}(t) = 1 \neq 2 = y_{\text{comb}}(t)$. The half-wave rectifier is **non-linear**.

**(b) Time-invariance test:**

**Step 1:** Select $x(t) = \sin(t)$ (which is positive on some intervals and negative on others).

**Step 2:** Compute the response:
$$
y(t) =
\begin{cases}
0, & \sin(t) < 0 \\
\sin(t), & \sin(t) \ge 0
\end{cases}
$$

**Step 3:** Choose $t_0 = \pi/2$ and form $x_{\text{shift}}(t) = \sin(t - \pi/2) = -\cos(t)$.

**Step 4:** Compute response to shifted input:
$$
y_{\text{shift}}(t) =
\begin{cases}
0, & -\cos(t) < 0 \;\;(\cos(t) > 0) \\
-\cos(t), & -\cos(t) \ge 0 \;\;(\cos(t) \le 0)
\end{cases}
$$

**Step 5:** Shift the original output:
$$
y(t - \pi/2) =
\begin{cases}
0, & \sin(t - \pi/2) < 0 \\
\sin(t - \pi/2), & \sin(t - \pi/2) \ge 0
\end{cases}
$$
Since $\sin(t - \pi/2) = -\cos(t)$, this is identical to $y_{\text{shift}}(t)$.

**Step 6:** The comparison holds for all $t$, all $t_0$, and all inputs. The half-wave rectifier is **time-invariant**.

*Summary:* The half-wave rectifier is non-linear but time-invariant — a common classification for many practical electronic systems.

---

### Exercise 9: Classification by Input-Output Count

**Problem:** Classify each of the following systems by its input-output configuration:
(a) A two-channel audio amplifier with left and right inputs and left and right outputs.
(b) A temperature controller with one heater input and one temperature sensor output.
(c) A control system with three sensor inputs and one actuator output.
(d) A robotic arm with four joint motor inputs and four joint angle sensor outputs.

**Solution:**

**(a)** Two inputs (left channel, right channel), two outputs (left speaker, right speaker). This is **MIMO** (specifically $2 \times 2$).

**(b)** One input (heater power), one output (temperature reading). This is **SISO**.

**(c)** Three inputs (sensor signals), one output (actuator command). This is **MISO**.

**(d)** Four inputs (motor commands), four outputs (joint angle measurements). This is **MIMO** (specifically $4 \times 4$).

---

### Exercise 10: State of Rest and Zero-Input Response

**Problem:** A system is described by $y(t) = e^{-t} \int_{0}^{t} e^{\tau} x(\tau) d\tau + y(0)e^{-t}$. The system is initially at rest at $t = 0$ with $y(0) = 2$.

(a) Is the system at state of rest at $t = 0$?
(b) Compute the output for $x(t) = u(t)$.
(c) Compute the zero-input response.

**Solution:**

**(a)** At $t = 0$, the initial condition $y(0) = 2 \neq 0$. The system is **not** at state of rest at $t = 0$ because there is stored energy. If the input were zero for $t \ge 0$, the output would be $y(t) = 2e^{-t} \neq 0$.

**(b)** For $x(t) = u(t)$:
$$
y(t) = e^{-t} \int_{0}^{t} e^{\tau} \cdot 1 \, d\tau + 2e^{-t} = e^{-t} (e^{t} - 1) + 2e^{-t} = 1 - e^{-t} + 2e^{-t} = 1 + e^{-t}
$$

**(c)** The zero-input response is the output when $x(t) = 0$:
$$
y_{zi}(t) = e^{-t} \int_{0}^{t} 0 \, d\tau + 2e^{-t} = 2e^{-t}
$$

The output consists of the **zero-state response** $y_{zs}(t) = 1 - e^{-t}$ (due to the input only) plus the **zero-input response** $y_{zi}(t) = 2e^{-t}$ (due to the initial condition). The total output is $y(t) = y_{zs}(t) + y_{zi}(t) = 1 + e^{-t}$.

---

## 6. Connections and Cross-References

- **Lecture 03 (Continuous-Time Signals):** The Dirac delta function and the sifting property introduced in Lecture 03 are the foundation for representing arbitrary signals as integrals of shifted impulses ($x(t) = \int x(\tau) \delta(t - \tau) d\tau$). This representation is the starting point for Lecture 04's discussion of system classification, as the impulse response concept depends directly on it.
- **Lecture 05 (LTI Systems):** The linearity and time-invariance properties tested in this lecture are the defining conditions for LTI systems. Systems that pass both tests become the subject of Lecture 05's discussion of convolution, impulse response, causality, and stability.
- **Lecture 06 (Convolution):** The convolution integral $y(t) = x(t) * h(t)$ is derived from the superposition of impulse responses. The linearity property (additivity + homogeneity) enables the decomposition of the input into impulses, and time-invariance ensures that each shifted impulse produces a shifted impulse response.
- **Fourier Series and Transform (upcoming):** Linearity ensures that the Fourier series/transform of a sum of signals equals the sum of their individual transforms. Time-invariance ensures that the frequency response $H(j\omega)$ fully characterizes the system's effect on sinusoidal inputs.
- **Laplace Transform (upcoming):** For differential equation descriptions of systems, linearity enables term-by-term transformation using the linearity property of the Laplace transform. The initial conditions (system state) appear as separate terms.
- **Control Systems (future course):** MIMO system analysis, state-space representations, and observability/controllability concepts all build on the definitions of system state and state of rest established here.

---

## 7. Exam Tip: Systematic Linearity and Time-Invariance Testing

Exam problems frequently ask you to test whether a given input-output relationship defines a linear and/or time-invariant system. Use the following structured approach:

### For Linearity Testing — The "Two-Input Check"

1. Write the system equation $y(t) = T\{x(t)\}$.
2. Compute $y_1 = T\{x_1\}$ and $y_2 = T\{x_2\}$ symbolically.
3. Form $T\{\alpha x_1 + \beta x_2\}$ by substituting the sum into the system equation.
4. Form $\alpha y_1 + \beta y_2$ by scaling and summing the individual responses.
5. Compare term by term. Common failure patterns:

| Failure Pattern | Example System | Why It Fails |
| :--- | :--- | :--- |
| Constant offset | $y = x + 1$ | The $+1$ is not scaled by $\alpha, \beta$ |
| Squaring | $y = x^2$ | Cross-term $2\alpha\beta x_1 x_2$ appears |
| Absolute value | $y = \|x\|$ | Sign-dependent cancellation fails |
| Product of input and output | $dy/dt + y^2 = x$ | $y^2$ generates cross-terms |
| Threshold / clipping | $y = \max(0, x)$ | Negative inputs are zeroed |

### For Time-Invariance Testing — The "Shift and Compare" Check

1. Compute the reference output $y(t) = T\{x(t)\}$.
2. Shift the input: $x_{\text{shift}}(t) = x(t - t_0)$.
3. Compute $T\{x(t - t_0)\}$ — this is the **response to the shifted input**.
4. Form $y(t - t_0)$ by substituting $(t - t_0)$ into the expression for $y(t)$ — this is the **shifted output**.
5. Compare. The system is time-varying if:
   - The system equation explicitly contains $t$ (e.g., $y(t) = t x(t)$).
   - The system equation uses $t$ in the limits or coefficients (e.g., $y(t) = \int_{0}^{t} e^{-(t-\tau)} \sin(\tau) x(\tau) d\tau$ is time-invariant because it depends only on $(t-\tau)$, but $y(t) = \int_{0}^{t} \tau x(\tau) d\tau$ is time-varying because $\tau$ appears without the $t-\tau$ shift structure).

### Common Mistake: Checking Linearity by Inspection Only

Do not assume a system is linear just because it "looks" simple. Always test with specific numbers. The quickest counter-example is often:
- Test homogeneity: $T\{2 \cdot x(t)\} \stackrel{?}{=} 2 \cdot T\{x(t)\}$ for a simple $x(t)$.
- If homogeneity holds, test additivity: $T\{x_1 + x_2\} \stackrel{?}{=} T\{x_1\} + T\{x_2\}$.

### Quick Reference: Common Systems and Their Classification

| System Equation | Linear? | Time-Invariant? |
| :--- | :--- | :--- |
| $y(t) = x(t)$ | Yes | Yes |
| $y(t) = ax(t) + b$ ($b \neq 0$) | **No** | Yes |
| $y(t) = x^2(t)$ | **No** | Yes |
| $y(t) = \frac{dx}{dt}$ | Yes | Yes |
| $y(t) = \int_{-\infty}^{t} x(\tau) d\tau$ | Yes | Yes |
| $y(t) = \cos(\omega_0 t) x(t)$ | Yes | **No** |
| $y(t) = t x(t)$ | Yes | **No** |
| $y(t) = \max(0, x(t))$ | **No** | Yes |
| $y(t) = x(t) + x(t-1)$ | Yes | Yes |
| $\frac{dy}{dt} + 2y = x$ (initial rest) | Yes | Yes |
| $y(t) = x(-t)$ | Yes | **No** (reversal changes with shift) |

> **[Key Insight]**
>
> The most common exam pitfall: $y(t) = x(at)$ (time scaling). This system is linear (easy to verify) but **time-varying** unless $a = \pm 1$. For example, if $y(t) = x(2t)$ (time compression), then shifting the input by $t_0$ gives $T\{x(t - t_0)\} = x(2t - t_0)$, but shifting the output gives $y(t - t_0) = x(2t - 2t_0)$. These differ, so the system is time-varying.