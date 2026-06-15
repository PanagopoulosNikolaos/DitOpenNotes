# Lecture 05 - Linear Time-Invariant (LTI) Systems

Continuation of the system classification framework from Lecture 04, introducing the additional properties of memory, causality, and stability that characterize system behavior. This lecture defines the class of Linear Time-Invariant (LTI) systems and establishes the impulse response as a complete characterization of such systems. The convolution integral is derived as the mechanism for computing the output of an LTI system to any arbitrary input, forming the foundation for time-domain system analysis.

---

## 1. Conceptual Foundation

### 1.1 Static (Memoryless) vs. Dynamic Systems

A system is classified as **static** (or **memoryless**) if the output at any time $t$ depends only on the input at that same time $t$, and not on past or future values of the input. Conversely, a **dynamic** system (or system **with memory**) is one where the output depends on past (or future) values of the input.

#### Memoryless Systems

For a memoryless system, the input-output relationship at time $t$ is an instantaneous function:

$$
y(t) = f\big(x(t)\big)
$$

where $f$ is some function (possibly non-linear) that involves no integration, differentiation, or delay elements.

**Resistor example:** An ideal resistor obeys Ohm's law:

$$
v(t) = R \cdot i(t)
$$

At any instant $t$, the voltage depends only on the current at that same instant. There is no integration, no storage of energy, and no dependence on past values. The resistor is memoryless.

Other memoryless systems:
- $y(t) = x^2(t)$ (instantaneous squaring)
- $y(t) = \sin\big(x(t)\big)$ (instantaneous non-linear mapping)
- $y(t) = 2x(t) + 3$ (affine mapping)

#### Systems with Memory

For a system with memory, the output depends on values of the input at times other than the present. This dependence arises whenever the system stores energy (capacitors, inductors) or performs operations that span multiple time instants (integrators, differentiators, delays).

**Capacitor integrator example:** An ideal capacitor obeys:

$$
v(t) = \frac{1}{C} \int_{-\infty}^{t} i(\tau) \, d\tau
$$

At time $t$, the voltage depends on the entire history of the current $i(\tau)$ for $\tau \le t$. The capacitor therefore has **infinite memory** — the output depends on all past inputs.

**Differentiator example:**

$$
y(t) = \frac{dx}{dt}
$$

Although a derivative is a local operation, it implicitly depends on values in an arbitrarily small neighborhood around $t$, making it a dynamic system.

#### Memory Length

| Memory Type | Description | Example |
| :--- | :--- | :--- |
| **Zero memory** (static) | Output depends only on current input | $y(t) = R \cdot x(t)$ |
| **Finite memory** | Output depends on inputs over a finite window | $y(t) = \frac{1}{T} \int_{t-T}^{t} x(\tau) d\tau$ (moving average) |
| **Infinite memory** | Output depends on all past inputs | $y(t) = \int_{-\infty}^{t} x(\tau) d\tau$ (ideal integrator) |

---

### 1.2 Causal vs. Non-causal Systems

#### Definition of Causality

A system is **causal** if the output at any time $t$ depends only on values of the input at the present time and past times ($\tau \le t$). A causal system cannot "look into the future" — there is no dependence on $x(\tau)$ for $\tau > t$.

Formally, a system $S$ is causal if for any two inputs $x_1(t)$ and $x_2(t)$ that are identical for all $\tau \le t$:

$$
x_1(\tau) = x_2(\tau), \quad \forall \tau \le t
$$

the corresponding outputs are also identical at time $t$:

$$
S\{x_1\}(t) = S\{x_2\}(t)
$$

**Causal physical real-time systems:** Every physical system that operates in real time must be causal. When you speak into a microphone, the electrical output cannot depend on words you have not yet spoken. A causal system processes the input as it arrives, without access to future values.

**Non-causal systems in non-real-time processing:** A system that processes recorded data can be non-causal because the entire signal is available in memory. For example:

- A smoothing filter that computes $y(t) = \frac{1}{3}\big(x(t-1) + x(t) + x(t+1)\big)$ is non-causal because $y(t)$ depends on $x(t+1)$, a future value.
- Image processing (where the independent variable is spatial position, not time) routinely uses non-causal filters, since the entire image is available simultaneously.

> **[Supplementary]**
>
> In digital signal processing, a non-causal filter can be made causal by introducing a sufficient delay. For the three-point moving average above, defining $y_{\text{causal}}(t) = y(t-1)$ yields a causal output that is simply a delayed version of the non-causal result. This approach is standard when processing pre-recorded data offline.

---

### 1.3 System Stability — Bounded-Input Bounded-Output (BIBO) Stability

A system is **BIBO stable** if every bounded input produces a bounded output. Formally:

$$
\forall x(t) \text{ such that } |x(t)| \le M_x < \infty \quad \Rightarrow \quad |y(t)| \le M_y < \infty
$$

for some finite constants $M_x$ and $M_y$ (which may differ).

#### Physical Analogy

**Stable system (marble in a bowl):** A marble placed at the bottom of a bowl, when perturbed, rolls around but eventually settles back to the bottom. Perturbations produce bounded excursions. This is analogous to a stable system: a bounded input (the perturbation) produces a bounded output (the marble stays within the bowl).

**Unstable system (marble on a dome):** A marble placed at the top of a dome, when perturbed, rolls away and never returns. The smallest perturbation produces an unbounded excursion. This is analogous to an unstable system: a bounded input can produce an output that grows without bound.

#### Stability Proofs and Testing

For LTI systems characterized by an impulse response $h(t)$, BIBO stability is equivalent to the **absolute integrability** of the impulse response:

$$
\int_{-\infty}^{\infty} |h(\tau)| \, d\tau < \infty
$$

This condition can be tested directly. For systems described by differential equations, stability can be assessed by examining the locations of the system's poles (the roots of the characteristic equation). If all poles have negative real parts, the system is stable.

> **[Key Insight]**
>
> BIBO stability is an input-output property — it addresses whether the system's output remains bounded for all possible bounded inputs. A system that appears stable for a particular bounded input may still be BIBO unstable if there exists any bounded input that drives the output to infinity. The impulse response test (absolute integrability) is definitive for LTI systems.

---

### 1.4 Importance of Linear Time-Invariant (LTI) Systems

LTI systems occupy a central position in signals and systems because they satisfy both **linearity** (superposition) and **time-invariance** (shift invariance). These two properties together produce the following powerful consequences:

1. **Complete characterization by impulse response:** The system's behavior is fully described by its response to a single test signal — the Dirac delta $\delta(t)$. No other system class has this property.

2. **Convolution integral:** The output for any input is given by $y(t) = x(t) * h(t)$. This is a closed-form, deterministic operation.

3. **Eigenfunction property:** Complex exponentials $e^{st}$ are eigenfunctions of LTI systems. The output is $H(s)e^{st}$ where $H(s)$ is the (possibly complex) eigenvalue. This property is the foundation of Fourier and Laplace analysis.

4. **Frequency-domain analysis:** The frequency response $H(j\omega)$ (the Fourier transform of $h(t)$) describes the system's effect on sinusoidal inputs: amplitude scaling and phase shift as functions of frequency.

5. **Cascade and parallel combinations:** LTI systems in series have an overall impulse response $h_1(t) * h_2(t)$. In parallel, the overall impulse response is $h_1(t) + h_2(t)$. These simple combination rules do not hold for non-linear or time-varying systems.

6. **Predictable behavior:** The superposition principle means the system's response to complex inputs can be decomposed into responses to simpler components and recombined. This makes analysis, design, and optimization tractable.

---

## 2. Formal Definition or Model

### 2.1 Impulse Response

#### Definition for LTI Systems

For an LTI system $S$, the **impulse response** $h(t)$ is defined as the output when the input is the Dirac delta function $\delta(t)$, with the system initially at rest:

$$
h(t) = S\{\delta(t)\}
$$

Because the system is time-invariant, the response to a shifted impulse $\delta(t - \tau)$ is the shifted impulse response:

$$
S\{\delta(t - \tau)\} = h(t - \tau)
$$

Because the system is linear, the response to a weighted impulse $\alpha \delta(t - \tau)$ is:

$$
S\{\alpha \delta(t - \tau)\} = \alpha h(t - \tau)
$$

The impulse response $h(t)$ completely characterizes the LTI system. Once $h(t)$ is known, the output to any input $x(t)$ can be computed via convolution.

#### Definition for Linear Time-Varying (LTV) Systems

For a linear but **time-varying** system, the response to a shifted impulse depends on both the observation time $t$ and the impulse application time $\tau$. The impulse response is therefore a function of two variables:

$$
h(t, \tau) = S\{\delta(t - \tau)\}
$$

where $t$ is the time at which the output is observed, and $\tau$ is the time at which the impulse was applied. In this case, the output is:

$$
y(t) = \int_{-\infty}^{\infty} x(\tau) h(t, \tau) \, d\tau
$$

This is the **superposition integral** (also called the time-varying convolution). For time-invariant systems, $h(t, \tau)$ reduces to $h(t - \tau)$, a function of only one variable (the difference between observation time and impulse application time).

---

### 2.2 The Convolution Integral

#### Derivation and Formulation

The convolution integral is derived from the impulse response and the superposition of impulse responses. Starting from the sifting property:

$$
x(t) = \int_{-\infty}^{\infty} x(\tau) \delta(t - \tau) \, d\tau
$$

Apply the system operator $S$ to both sides. If $S$ is **linear**, the operator passes through the integral:

$$
y(t) = S\{x(t)\} = S\left\{\int_{-\infty}^{\infty} x(\tau) \delta(t - \tau) \, d\tau\right\} = \int_{-\infty}^{\infty} x(\tau) \, S\{\delta(t - \tau)\} \, d\tau
$$

If $S$ is also **time-invariant**, then $S\{\delta(t - \tau)\} = h(t - \tau)$, giving:

$$
y(t) = \int_{-\infty}^{\infty} x(\tau) h(t - \tau) \, d\tau
$$

This is the **convolution integral**, denoted by the convolution operator $*$:

$$
y(t) = x(t) * h(t) = \int_{-\infty}^{\infty} x(\tau) h(t - \tau) \, d\tau
$$

An equivalent form (obtained by the change of variable $\sigma = t - \tau$) is:

$$
y(t) = \int_{-\infty}^{\infty} x(t - \sigma) h(\sigma) \, d\sigma = h(t) * x(t)
$$

#### Output Representation for Causal LTI Systems

For a **causal** LTI system, the impulse response satisfies $h(t) = 0$ for $t < 0$ (a causal system cannot respond before the impulse is applied). This modifies the convolution limits:

$$
y(t) = \int_{-\infty}^{t} x(\tau) h(t - \tau) \, d\tau = \int_{0}^{\infty} x(t - \sigma) h(\sigma) \, d\sigma
$$

#### Output Representation for Causal Inputs

If the input is also causal ($x(t) = 0$ for $t < 0$), the lower limit of integration becomes $0$:

$$
y(t) = \int_{0}^{t} x(\tau) h(t - \tau) \, d\tau = \int_{0}^{t} h(\tau) x(t - \tau) \, d\tau
$$

This is the most common form encountered in practice: the convolution of two causal signals has finite, time-dependent limits from $0$ to $t$.

> **[Key Insight]**
>
> The upper limit $t$ (rather than $\infty$) is the consequence of causality: the integrand $x(\tau)h(t - \tau)$ is zero for $\tau > t$ because $h(t - \tau) = 0$ when $t - \tau < 0$ (i.e., $\tau > t$). Similarly, the lower limit $0$ arises from the causal input: $x(\tau) = 0$ for $\tau < 0$.

---

## 3. Key Parameters and Constraints

### 3.1 System Memory and Memory Length

| Parameter | Description | Classification | Example |
| :--- | :--- | :--- | :--- |
| Memory type | Dependence on past input values | Static (memoryless) / Dynamic (with memory) | Resistor (static), Capacitor (dynamic) |
| Memory length | Duration of input history affecting output | Zero / Finite / Infinite | Moving average (finite), Integrator (infinite) |
| Memory indicator | Presence of energy-storage elements | Absence / Presence of $L$, $C$, integration, delay | No $C$ in circuit implies memoryless |

### 3.2 Causality

| Property | Description | Testing Method |
| :--- | :--- | :--- |
| Causal system | Output depends only on present and past inputs | $h(t) = 0$ for $t < 0$ (for LTI systems) |
| Anti-causal system | Output depends only on future inputs | $h(t) = 0$ for $t > 0$ |
| Non-causal system | Output depends on both past and future inputs | $h(t) \neq 0$ for some $t < 0$ |

### 3.3 BIBO Stability Condition

| Property | Condition for LTI Systems | Implications |
| :--- | :--- | :--- |
| BIBO stable | $\int_{-\infty}^{\infty} \|h(t)\| dt < \infty$ | All poles have negative real parts (for rational systems) |
| BIBO unstable | $\int_{-\infty}^{\infty} \|h(t)\| dt = \infty$ | At least one pole has non-negative real part |
| Marginally stable | $\int_{-\infty}^{\infty} \|h(t)\| dt = \infty$ but output remains bounded for some inputs | Poles on imaginary axis (oscillator) |

### 3.4 Convolution Parameters

| Parameter | Symbol | Role | Constraints |
| :--- | :--- | :--- | :--- |
| Input signal | $x(t)$ | Signal to be processed | Must be integrable for convolution to be defined |
| Impulse response | $h(t)$ | System characterization | Must be absolutely integrable for BIBO stability |
| Convolution output | $y(t) = x(t) * h(t)$ | System response | Duration = $T_x + T_h$ (width property) |
| Integration variable | $\tau$ | Dummy variable of integration | Real-valued |

---

## 4. Step-by-Step Mechanisms

### 4.1 Procedure for Determining if a System is Memoryless

1. **Inspect the input-output relationship.** If the output $y(t)$ can be expressed as a function $f(x(t))$ involving only the instantaneous value $x(t)$ (no integrals, derivatives, differences, or delays), the system is memoryless.
2. **Check for energy storage elements.** In circuit systems, check for the presence of capacitors ($C$) or inductors ($L$). Their presence indicates memory.
3. **Check for integration or summation.** Any operation of the form $\int_{a}^{t} x(\tau) d\tau$ or $\sum_{k=-\infty}^{n} x[k]$ indicates memory.
4. **Check for delay operations.** Any $x(t - t_0)$ with $t_0 \neq 0$ indicates memory (the output depends on a past value).

### 4.2 Procedure for Determining Causality

1. **Inspect the input-output relationship.** If the output $y(t)$ depends on $x(\tau)$ for $\tau > t$, the system is non-causal.
2. **For LTI systems, examine $h(t)$.** If $h(t) \neq 0$ for any $t < 0$, the system is non-causal.
3. **For systems defined by differential equations:** If the equation involves future values (advance operators), the system is non-causal.
4. **Check the integration limits.** An integral with upper limit $t$ (e.g., $\int_{-\infty}^{t}$) is causal. An integral with upper limit $t+1$ (e.g., $\int_{t}^{t+1}$) is non-causal.

### 4.3 Procedure for Testing BIBO Stability

1. **For LTI systems with known $h(t)$:** Compute $\int_{-\infty}^{\infty} |h(t)| dt$. If the integral is finite, the system is BIBO stable.
2. **For systems described by differential equations:** Compute the system's poles (roots of the characteristic equation). If all poles have strictly negative real parts, the system is stable.
3. **For feedback systems:** Check the closed-loop transfer function for any poles in the right-half plane (RHP) or on the imaginary axis (repeated poles).
4. **For non-linear systems:** BIBO stability must be tested case-by-case. A common approach is to check whether the system function $f(x)$ is bounded for all bounded $x$.

### 4.4 Procedure for Computing Convolution of Two Functions

1. **Express the convolution integral:** $y(t) = \int_{-\infty}^{\infty} x(\tau) h(t - \tau) d\tau$.
2. **Time-reverse $h(\tau)$:** Define $h_{\text{rev}}(\tau) = h(-\tau)$. Graphically, flip $h$ about the vertical axis.
3. **Shift by $t$:** $h_{\text{rev}}(\tau - t) = h(t - \tau)$. Graphically, slide the reversed $h$ to position $t$.
4. **Multiply:** Compute $x(\tau) \cdot h(t - \tau)$ for each $\tau$. This is the pointwise product of the two signals.
5. **Integrate:** Compute the area under the product $x(\tau)h(t-\tau)$ with respect to $\tau$. This gives $y(t)$.
6. **Repeat for all $t$:** The result is $y(t)$ defined piecewise over different intervals of $t$, depending on the overlap region.

---

## 5. Solved Exercises

### Exercise 1: Classifying Memory and Causality of a Simple System

**Problem:** Classify each system as (i) memoryless or with memory, and (ii) causal or non-causal:

(a) $y(t) = 5x(t) + 2$

(b) $y(t) = \int_{0}^{t} x(\tau) d\tau$

(c) $y(t) = x(t-2) + x(t+2)$

(d) $y(t) = \frac{1}{T} \int_{t-T}^{t} x(\tau) d\tau$ (moving average over window $T$)

(e) $y(t) = \frac{dx}{dt}$

**Solution:**

**(a)** $y(t) = 5x(t) + 2$
- **Memoryless** — The output depends only on $x(t)$ at the same instant.
- **Causal** — No dependence on future values.

**(b)** $y(t) = \int_{0}^{t} x(\tau) d\tau$
- **With memory** — The output depends on all values $x(\tau)$ from $0$ to $t$, which includes past inputs.
- **Causal** — The upper limit is $t$ (present time), not beyond.
- *Note:* If $t < 0$, the integral runs from $0$ to a negative $t$, which effectively goes backward. For $t < 0$, the integration limits would be reversed, introducing a non-causal dependency. Typically, the system is defined with $t \ge 0$ and $x(t) = 0$ for $t < 0$.

**(c)** $y(t) = x(t-2) + x(t+2)$
- **With memory** — Depends on $x(t-2)$ (past) and $x(t+2)$ (future).
- **Non-causal** — The term $x(t+2)$ depends on a future value.

**(d)** $y(t) = \frac{1}{T} \int_{t-T}^{t} x(\tau) d\tau$
- **With memory (finite memory of length $T$)** — The output depends on inputs over the window $[t-T, t]$.
- **Causal** — The integration upper limit is $t$, so it uses only past and present values.

**(e)** $y(t) = \frac{dx}{dt}$
- **With memory** — The derivative depends on values in an arbitrarily small neighborhood around $t$, which includes information about the immediate past (and future in the mathematical sense). In practice, the derivative is treated as a system with infinitesimal memory.
- **Causal** — If defined as a right-sided derivative, it depends only on past and present values. The symmetric derivative $dx/dt = \lim_{h \to 0} (x(t+h) - x(t-h))/(2h)$ is technically non-causal, but the standard causal definition uses a backward difference.

---

### Exercise 2: Testing BIBO Stability of an Integrator

**Problem:** Determine whether the ideal integrator $y(t) = \int_{-\infty}^{t} x(\tau) d\tau$ is BIBO stable.

**Solution:**

**Step 1:** Recall that for an LTI system, BIBO stability requires $\int_{-\infty}^{\infty} |h(t)| dt < \infty$. First, find the impulse response of the integrator.

**Step 2:** The impulse response is the output when $x(t) = \delta(t)$:
$$
h(t) = \int_{-\infty}^{t} \delta(\tau) d\tau = u(t)
$$

**Step 3:** Test the absolute integrability of $h(t)$:
$$
\int_{-\infty}^{\infty} |h(t)| dt = \int_{-\infty}^{\infty} |u(t)| dt = \int_{0}^{\infty} 1 \, dt = \infty
$$

**Step 4:** Since the integral diverges, the ideal integrator is **not BIBO stable**.

*Verification with a specific bounded input:* Consider $x(t) = u(t)$, which is bounded ($|x(t)| \le 1$). The output is:
$$
y(t) = \int_{-\infty}^{t} u(\tau) d\tau = r(t) = t \cdot u(t)
$$
The output grows without bound as $t \to \infty$, confirming instability.

> **[Key Insight]**
>
> The ideal integrator is unstable because a constant bounded input produces a ramp output that tends to infinity. This is the defining characteristic of an unstable system: there exists at least one bounded input that drives the output to infinity.

---

### Exercise 3: Testing BIBO Stability of an Exponential Decay System

**Problem:** Determine whether the system $y(t) = \int_{-\infty}^{\infty} e^{-|\tau|} x(t - \tau) d\tau$ is BIBO stable.

**Solution:**

**Step 1:** Identify the impulse response. The system is described by $y(t) = x(t) * h(t)$ with $h(t) = e^{-|t|}$.

**Step 2:** Test absolute integrability:
$$
\int_{-\infty}^{\infty} |h(t)| dt = \int_{-\infty}^{\infty} e^{-|t|} dt
$$

**Step 3:** Split the integral at $t = 0$:
$$
\int_{-\infty}^{0} e^{t} dt + \int_{0}^{\infty} e^{-t} dt = \left[e^{t}\right]_{-\infty}^{0} + \left[-e^{-t}\right]_{0}^{\infty}
$$

**Step 4:** Evaluate each part:
$$
(1 - 0) + (0 - (-1)) = 1 + 1 = 2
$$

**Step 5:** The integral is finite ($2 < \infty$). The system is **BIBO stable**.

*Physical interpretation:* The impulse response $e^{-|t|}$ decays rapidly as $|t| \to \infty$, meaning the system has finite "memory" of past and future inputs. Any bounded input produces a bounded output because the weighting function $e^{-|\tau|}$ "forgets" old inputs exponentially fast.

---

### Exercise 4: Computing Impulse Response from a Differential Equation

**Problem:** Find the impulse response $h(t)$ of the LTI system described by:
$$
\frac{dy}{dt} + 3y(t) = x(t)
$$
Assume the system is initially at rest.

**Solution:**

**Step 1:** For the impulse response, set $x(t) = \delta(t)$. The equation becomes:
$$
\frac{dh}{dt} + 3h(t) = \delta(t)
$$
with $h(0^-) = 0$ (initial rest).

**Step 2:** For $t > 0$, the input $\delta(t) = 0$, so the equation reduces to the homogeneous form:
$$
\frac{dh}{dt} + 3h(t) = 0, \quad t > 0
$$

**Step 3:** The solution for $t > 0$ is $h(t) = A e^{-3t} u(t)$.

**Step 4:** Determine $A$ by integrating the differential equation from $t = 0^-$ to $t = 0^+$:
$$
\int_{0^-}^{0^+} \frac{dh}{dt} dt + 3 \int_{0^-}^{0^+} h(t) dt = \int_{0^-}^{0^+} \delta(t) dt
$$

**Step 5:** The leftmost term is $h(0^+) - h(0^-) = h(0^+)$ (since $h(0^-) = 0$). The middle term integrates to zero because $h(t)$ is finite over an infinitesimal interval. The right side is $1$. Thus:
$$
h(0^+) = 1
$$

**Step 6:** Using $h(0^+) = A e^{0} = A = 1$, we have:
$$
h(t) = e^{-3t} u(t)
$$

*Verification:* The response to $\delta(t)$ is an exponential decay starting from $1$ at $t = 0^+$ and decaying to $0$ as $t \to \infty$.

---

### Exercise 5: Convolution of Two Rectangular Pulses

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
1, & 0 \le t \le 1 \\
0, & \text{otherwise}
\end{cases}
$$

**Solution:**

**Step 1:** Write the convolution integral:
$$
y(t) = \int_{-\infty}^{\infty} x(\tau) h(t - \tau) d\tau
$$

**Step 2:** Both signals are rectangular pulses. Convolution of two rectangles produces a trapezoidal (or triangular, when the pulses have equal width) output.

**Step 3:** Determine the piecewise intervals by considering the overlap of $x(\tau)$ (supported on $[0, 2]$) and $h(t-\tau)$ (supported on $\tau \in [t-1, t]$).

**Case 1:** $t < 0$ — No overlap. $y(t) = 0$.

**Case 2:** $0 \le t < 1$ — Partial overlap entering. The overlap region is $\tau \in [0, t]$.
$$
y(t) = \int_{0}^{t} 1 \cdot 1 \, d\tau = t
$$

**Case 3:** $1 \le t < 2$ — Full overlap. The overlap region is $\tau \in [t-1, t]$, entirely within $[0, 2]$.
$$
y(t) = \int_{t-1}^{t} 1 \cdot 1 \, d\tau = 1
$$

**Case 4:** $2 \le t < 3$ — Partial overlap exiting. The overlap region is $\tau \in [t-1, 2]$.
$$
y(t) = \int_{t-1}^{2} 1 \cdot 1 \, d\tau = 2 - (t - 1) = 3 - t
$$

**Case 5:** $t \ge 3$ — No overlap. $y(t) = 0$.

**Step 4:** The complete result:
$$
y(t) =
\begin{cases}
0, & t < 0 \\
t, & 0 \le t < 1 \\
1, & 1 \le t < 2 \\
3 - t, & 2 \le t < 3 \\
0, & t \ge 3
\end{cases}
$$

The convolution is a trapezoidal pulse with total duration $T_y = T_x + T_h = 2 + 1 = 3$, verifying the width property.

---

### Exercise 6: Convolution of a Rectangular Pulse and an Exponential

**Problem:** Compute $y(t) = x(t) * h(t)$ where $x(t) = e^{-t} u(t)$ and $h(t) = u(t) - u(t - 2)$ (a rectangular pulse of width 2).

**Solution:**

**Step 1:** Write the convolution integral. Since both signals are causal, use the causal limits:
$$
y(t) = \int_{0}^{t} x(\tau) h(t - \tau) d\tau
$$

**Step 2:** The rectangular pulse $h(t)$ is $1$ for $0 \le t \le 2$ and $0$ otherwise. Therefore $h(t - \tau) = 1$ when $0 \le t - \tau \le 2$, i.e., $\tau \in [t-2, t]$.

**Step 3:** Determine piecewise intervals.

**Case 1:** $t < 0$ — No overlap. $y(t) = 0$.

**Case 2:** $0 \le t < 2$ — The $h(t-\tau)$ covers $\tau \in [0, t]$ (since $t-2 < 0$), and $x(\tau)$ is supported on $\tau \ge 0$.
$$
y(t) = \int_{0}^{t} e^{-\tau} \cdot 1 \, d\tau = \left[-e^{-\tau}\right]_{0}^{t} = 1 - e^{-t}
$$

**Case 3:** $t \ge 2$ — The $h(t-\tau)$ covers $\tau \in [t-2, t]$, and since $t-2 \ge 0$, both limits are within $x(\tau)$'s support.
$$
y(t) = \int_{t-2}^{t} e^{-\tau} \cdot 1 \, d\tau = \left[-e^{-\tau}\right]_{t-2}^{t} = e^{-(t-2)} - e^{-t} = e^{-t}(e^{2} - 1)
$$

**Step 4:** The complete result:
$$
y(t) =
\begin{cases}
0, & t < 0 \\
1 - e^{-t}, & 0 \le t < 2 \\
e^{-t}(e^{2} - 1), & t \ge 2
\end{cases}
$$

*Verification:* At $t = 2$, both pieces give $y(2) = 1 - e^{-2} \approx 0.865$, confirming continuity.

---

### Exercise 7: Impulse Response of a Causal LTI System from System Equation

**Problem:** A causal LTI system is described by:
$$
\frac{d^2y}{dt^2} + 4\frac{dy}{dt} + 3y(t) = \frac{dx}{dt} + 2x(t)
$$

Find the impulse response $h(t)$.

**Solution:**

**Step 1:** For the impulse response, set $x(t) = \delta(t)$ and solve:
$$
\frac{d^2h}{dt^2} + 4\frac{dh}{dt} + 3h(t) = \delta'(t) + 2\delta(t)
$$

**Step 2:** The characteristic equation is $s^2 + 4s + 3 = 0$, with roots $s = -1$ and $s = -3$. The natural response for $t > 0$ is:
$$
h(t) = (A e^{-t} + B e^{-3t}) u(t)
$$

**Step 3:** Determine $A$ and $B$ using the initial conditions at $t = 0^+$. Integrate the equation from $t = 0^-$ to $t = 0^+$:

First integration (to capture the $\delta'(t)$ term):
$$
\int_{0^-}^{0^+} \frac{d^2h}{dt^2} dt + 4\int_{0^-}^{0^+} \frac{dh}{dt} dt + 3\int_{0^-}^{0^+} h(t) dt = \int_{0^-}^{0^+} \delta'(t) dt + 2\int_{0^-}^{0^+} \delta(t) dt
$$

The term $\int \delta'(t) dt = 0$ (area of derivative of delta is zero), and $\int \delta(t) dt = 1$. The integrals of $h$ and $dh/dt$ over the infinitesimal interval are zero if these functions are finite. Thus:
$$
h'(0^+) - h'(0^-) = 2 \quad \Rightarrow \quad h'(0^+) = 2
$$

Second integration (to capture the jump in $h$):
$$
\int_{0^-}^{0^+} \frac{dh}{dt} dt + 4\int_{0^-}^{0^+} h(t) dt + 3\int_{0^-}^{0^+} \left(\int h\right) dt = \int_{0^-}^{0^+} \delta(t) dt + 2\int_{0^-}^{0^+} u(t) dt
$$

The first term gives $h(0^+) - h(0^-) = h(0^+)$. The integral of $\delta(t)$ is $1$, and the integral of $u(t)$ over the infinitesimal interval is $0$. Thus:
$$
h(0^+) = 1
$$

**Step 4:** Apply the initial conditions to $h(t) = (A e^{-t} + B e^{-3t}) u(t)$:

At $t = 0^+$:
$$
h(0^+) = A + B = 1
$$

Derivative:
$$
h'(t) = (-A e^{-t} - 3B e^{-3t}) u(t)
$$
$$
h'(0^+) = -A - 3B = 2
$$

**Step 5:** Solve the system:
$$
A + B = 1
$$
$$
-A - 3B = 2
$$

From the first: $A = 1 - B$. Substitute into the second:
$$
-(1 - B) - 3B = 2 \quad \Rightarrow \quad -1 + B - 3B = 2 \quad \Rightarrow \quad -1 - 2B = 2 \quad \Rightarrow \quad -2B = 3 \quad \Rightarrow \quad B = -\frac{3}{2}
$$

Then $A = 1 - (-3/2) = 5/2$.

**Step 6:** The impulse response is:
$$
h(t) = \left(\frac{5}{2} e^{-t} - \frac{3}{2} e^{-3t}\right) u(t)
$$

*Verification:* The system is stable because both poles $p_1 = -1$ and $p_2 = -3$ have negative real parts.

---

### Exercise 8: Convolution Using Graphical Method

**Problem:** Use the graphical convolution method to compute $y(t) = x(t) * h(t)$ where:
$$
x(t) = 
\begin{cases}
t, & 0 \le t \le 1 \\
0, & \text{otherwise}
\end{cases}
\quad
h(t) = e^{-t} u(t)
$$

**Solution:**

**Step 1:** Write $x(t)$ as a triangular-shaped pulse of duration 1, and $h(t)$ as an infinite-duration exponential.

**Step 2:** For graphical convolution, we need to evaluate $y(t) = \int_{-\infty}^{\infty} x(\tau) h(t - \tau) d\tau$ by considering the overlap as $t$ varies.

**Step 3:** The function $h(t-\tau) = e^{-(t-\tau)} u(t-\tau)$ is zero for $\tau > t$. The function $x(\tau)$ is zero for $\tau < 0$ and $\tau > 1$. The overlap is therefore $\tau \in [0, \min(1, t)]$ for $t > 0$.

**Case 1:** $t < 0$ — $h(t-\tau) = 0$ for all $\tau \ge 0$ because $u(t-\tau) = 0$ when $\tau > t$. $y(t) = 0$.

**Case 2:** $0 \le t < 1$ — The overlap region is $\tau \in [0, t]$.
$$
y(t) = \int_{0}^{t} \tau \cdot e^{-(t-\tau)} d\tau = e^{-t} \int_{0}^{t} \tau e^{\tau} d\tau
$$

Integrate $\int \tau e^{\tau} d\tau = e^{\tau}(\tau - 1)$ (integration by parts). Evaluate:
$$
y(t) = e^{-t} \left[e^{\tau}(\tau - 1)\right]_{0}^{t} = e^{-t} \left[e^{t}(t - 1) - (-1)\right] = e^{-t} \left[e^{t}(t - 1) + 1\right]
$$
$$
y(t) = (t - 1) + e^{-t} = t - 1 + e^{-t}
$$

**Case 3:** $t \ge 1$ — The overlap region is $\tau \in [0, 1]$ (the finite support of $x(\tau)$), provided $t \ge 1$ so that $h(t-\tau) > 0$ over all $\tau \in [0, 1]$.
$$
y(t) = \int_{0}^{1} \tau \cdot e^{-(t-\tau)} d\tau = e^{-t} \int_{0}^{1} \tau e^{\tau} d\tau
$$

The integral from $0$ to $1$:
$$
\int_{0}^{1} \tau e^{\tau} d\tau = \left[e^{\tau}(\tau - 1)\right]_{0}^{1} = e^{1}(1 - 1) - (-1) = 1
$$

Thus:
$$
y(t) = e^{-t} \cdot 1 = e^{-t}, \quad t \ge 1
$$

**Step 4:** The complete result:
$$
y(t) =
\begin{cases}
0, & t < 0 \\
t - 1 + e^{-t}, & 0 \le t < 1 \\
e^{-t}, & t \ge 1
\end{cases}
$$

*Verification:* At $t = 1$, both pieces give $y(1) = 1 - 1 + e^{-1} = e^{-1} \approx 0.368$, confirming continuity.

> **[Supplementary]**
>
> The convolution of a finite-duration signal with an infinite-duration exponential produces a response that transitions from a transient phase (during overlap) to an exponential decay that mirrors the impulse response. This is a common pattern: the system's "memory" of the input signal fades exponentially after the input ends.

---

### Exercise 9: Causality and Stability of a Second-Order System

**Problem:** Consider a system with impulse response $h(t) = e^{-2t} u(t) - e^{-4t} u(-t)$.
(a) Is the system causal?
(b) Is the system BIBO stable?

**Solution:**

**(a) Causality test:**

**Step 1:** A causal LTI system has $h(t) = 0$ for $t < 0$.

**Step 2:** Examine $h(t)$ for $t < 0$:
$$
h(t) = e^{-2t} \cdot 0 - e^{-4t} \cdot 1 = -e^{-4t}, \quad t < 0
$$

**Step 3:** For $t < 0$, $-e^{-4t} \neq 0$ (in fact, it grows as $t \to -\infty$). Therefore $h(t) \neq 0$ for negative $t$, and the system is **non-causal**.

*Physical interpretation:* The term $h(t) = -e^{-4t} u(-t)$ represents the response to an impulse before the impulse is applied — a physical impossibility in real-time systems.

**(b) BIBO stability test:**

**Step 1:** Compute $\int_{-\infty}^{\infty} |h(t)| dt$:
$$
\int_{-\infty}^{\infty} |h(t)| dt = \int_{-\infty}^{0} |{-e^{-4t}}| dt + \int_{0}^{\infty} |e^{-2t}| dt
$$

**Step 2:** For $t < 0$, $e^{-4t} = e^{4|t|}$, which grows as $t \to -\infty$:
$$
\int_{-\infty}^{0} e^{-4t} dt = \int_{-\infty}^{0} e^{4|t|} dt = \int_{0}^{\infty} e^{-4u} du = \left[-\frac{e^{-4u}}{4}\right]_{0}^{\infty} = \frac{1}{4}
$$

**Step 3:** For $t > 0$:
$$
\int_{0}^{\infty} e^{-2t} dt = \left[-\frac{e^{-2t}}{2}\right]_{0}^{\infty} = \frac{1}{2}
$$

**Step 4:** Total:
$$
\int_{-\infty}^{\infty} |h(t)| dt = \frac{1}{4} + \frac{1}{2} = \frac{3}{4} < \infty
$$

The system is **BIBO stable**, despite being non-causal.

*Summary:* This system is stable (the impulse response is absolutely integrable) but non-causal (response exists before the impulse is applied). This is characteristic of offline signal processing systems where the entire signal is known in advance.

---

### Exercise 10: Convolution of Two Piecewise-Linear Functions

**Problem:** Let $x(t) = 2[u(t) - u(t-3)]$ and $h(t) = t[u(t) - u(t-2)]$. Compute $y(t) = x(t) * h(t)$.

**Solution:**

**Step 1:** Express $x(t)$ and $h(t)$:
$$
x(t) = 
\begin{cases}
2, & 0 \le t \le 3 \\
0, & \text{otherwise}
\end{cases}
\quad
h(t) = 
\begin{cases}
t, & 0 \le t \le 2 \\
0, & \text{otherwise}
\end{cases}
$$

**Step 2:** Write the convolution integral:
$$
y(t) = \int_{-\infty}^{\infty} x(\tau) h(t - \tau) d\tau
$$

The support of $x(\tau)$ is $[0, 3]$. The support of $h(t-\tau)$ in $\tau$ is $[t-2, t]$

**Step 3:** Determine piecewise intervals based on overlap.

**Case 1:** $t < 0$ — No overlap. $y(t) = 0$.

**Case 2:** $0 \le t < 2$ — Overlap on $\tau \in [0, t]$.
$$
y(t) = \int_{0}^{t} 2 \cdot (t - \tau) d\tau = 2 \int_{0}^{t} (t - \tau) d\tau = 2 \left[t\tau - \frac{\tau^2}{2}\right]_{0}^{t}
$$
$$
y(t) = 2\left[t^2 - \frac{t^2}{2}\right] = 2\left(\frac{t^2}{2}\right) = t^2
$$

**Case 3:** $2 \le t < 3$ — Full height of $h$ overlaps with $x$. Overlap on $\tau \in [t-2, t]$, and $[t-2, t]$ is fully within $[0, 3]$.
$$
y(t) = \int_{t-2}^{t} 2 \cdot (t - \tau) d\tau = 2 \int_{t-2}^{t} (t - \tau) d\tau
$$

Let $u = t - \tau$, then $du = -d\tau$, and when $\tau = t-2$, $u = 2$; when $\tau = t$, $u = 0$:
$$
y(t) = 2 \int_{2}^{0} u (-du) = 2 \int_{0}^{2} u \, du = 2 \left[\frac{u^2}{2}\right]_{0}^{2} = 2 \cdot 2 = 4
$$

Alternatively, directly: $\int_{t-2}^{t} (t-\tau) d\tau = \frac{(2)^2}{2} = 2$, and $2 \cdot 2 = 4$.

**Case 4:** $3 \le t < 5$ — Partial overlap as $x$ ends. Overlap on $\tau \in [t-2, 3]$.
$$
y(t) = \int_{t-2}^{3} 2 \cdot (t - \tau) d\tau = 2 \int_{t-2}^{3} (t - \tau) d\tau
$$
$$
= 2 \left[t\tau - \frac{\tau^2}{2}\right]_{t-2}^{3}
$$
$$
= 2 \left[\left(3t - \frac{9}{2}\right) - \left(t(t-2) - \frac{(t-2)^2}{2}\right)\right]
$$
$$
= 2 \left[3t - \frac{9}{2} - (t^2 - 2t) + \frac{t^2 - 4t + 4}{2}\right]
$$
$$
= 2 \left[3t - \frac{9}{2} - t^2 + 2t + \frac{t^2}{2} - 2t + 2\right]
$$
$$
= 2 \left[-\frac{t^2}{2} + 3t - \frac{5}{2}\right] = -t^2 + 6t - 5
$$

**Case 5:** $t \ge 5$ — No overlap. $y(t) = 0$.

**Step 4:** The complete result:
$$
y(t) =
\begin{cases}
0, & t < 0 \\
t^2, & 0 \le t < 2 \\
4, & 2 \le t < 3 \\
-t^2 + 6t - 5, & 3 \le t < 5 \\
0, & t \ge 5
\end{cases}
$$

*Verification:* At $t = 2$, the first two pieces give $y(2) = 2^2 = 4$, matching the constant region. At $t = 3$, the second and third pieces give $y(3) = 4$ (from constant) and $y(3) = -(3)^2 + 6(3) - 5 = -9 + 18 - 5 = 4$, confirming continuity. Total duration $T_y = T_x + T_h = 3 + 2 = 5$, consistent with the width property.

---

### Exercise 11: Explicitly Computing the Convolution Integral for Causal LTI System

**Problem:** A causal LTI system has impulse response $h(t) = e^{-t} u(t)$. The input is $x(t) = \sin(t) u(t)$. Compute the output $y(t)$ for $t \ge 0$.

**Solution:**

**Step 1:** Both signals are causal, so the convolution limits are $0$ to $t$:
$$
y(t) = \int_{0}^{t} \sin(\tau) e^{-(t-\tau)} d\tau = e^{-t} \int_{0}^{t} \sin(\tau) e^{\tau} d\tau
$$

**Step 2:** Evaluate $I = \int_{0}^{t} e^{\tau} \sin(\tau) d\tau$ using integration by parts or the standard formula:
$$
\int e^{a\tau} \sin(b\tau) d\tau = \frac{e^{a\tau}}{a^2 + b^2} \big(a \sin(b\tau) - b \cos(b\tau)\big)
$$

With $a = 1$, $b = 1$:
$$
I = \left[\frac{e^{\tau}}{2} \big(\sin(\tau) - \cos(\tau)\big)\right]_{0}^{t} = \frac{e^{t}}{2}\big(\sin(t) - \cos(t)\big) - \frac{1}{2}(0 - 1)
$$
$$
I = \frac{e^{t}}{2}\big(\sin(t) - \cos(t)\big) + \frac{1}{2}
$$

**Step 3:** Substitute back:
$$
y(t) = e^{-t} \left[\frac{e^{t}}{2}\big(\sin(t) - \cos(t)\big) + \frac{1}{2}\right]
$$
$$
y(t) = \frac{1}{2}\big(\sin(t) - \cos(t)\big) + \frac{1}{2} e^{-t}, \quad t \ge 0
$$

**Step 4:** With the unit step:
$$
y(t) = \left[\frac{1}{2}\big(\sin(t) - \cos(t)\big) + \frac{1}{2} e^{-t}\right] u(t)
$$

*Interpretation:* The output consists of:
- A **steady-state** sinusoidal component $\frac{1}{2}(\sin(t) - \cos(t)) = \frac{1}{\sqrt{2}} \sin(t - \pi/4)$ — the system's response to the sinusoid after transients decay.
- A **transient** exponential term $\frac{1}{2} e^{-t}$ that decays to zero as $t \to \infty$.

This illustrates the eigenfunction property: for large $t$, the response to a sinusoidal input is a sinusoid of the same frequency, scaled and phase-shifted.

---

### Exercise 12: Determining System Properties from Impulse Response

**Problem:** For each impulse response, determine whether the LTI system is (i) causal, (ii) BIBO stable:
(a) $h(t) = e^{-5t} u(t)$
(b) $h(t) = e^{2t} u(-t)$
(c) $h(t) = u(t)$
(d) $h(t) = \sin(10t) u(t)$

**Solution:**

**(a)** $h(t) = e^{-5t} u(t)$
- **Causality:** $h(t) = 0$ for $t < 0$. The system is **causal**.
- **Stability:** $\int_{0}^{\infty} e^{-5t} dt = \frac{1}{5} < \infty$. The system is **BIBO stable**.

**(b)** $h(t) = e^{2t} u(-t)$
- **Causality:** For $t < 0$, $u(-t) = 1$, so $h(t) = e^{2t} \neq 0$. The system is **non-causal** (response exists before the impulse).
- **Stability:** $\int_{-\infty}^{0} e^{2t} dt = \int_{-\infty}^{0} e^{2t} dt = \left[\frac{e^{2t}}{2}\right]_{-\infty}^{0} = \frac{1}{2} - 0 = \frac{1}{2} < \infty$. The system is **BIBO stable** despite being non-causal.

**(c)** $h(t) = u(t)$
- **Causality:** $h(t) = 0$ for $t < 0$. The system is **causal**.
- **Stability:** $\int_{0}^{\infty} 1 \, dt = \infty$. The system is **not BIBO stable** (this is the ideal integrator).

**(d)** $h(t) = \sin(10t) u(t)$
- **Causality:** $h(t) = 0$ for $t < 0$. The system is **causal**.
- **Stability:** $\int_{0}^{\infty} |\sin(10t)| dt$. Since $|\sin(10t)|$ oscillates between $0$ and $1$ without decaying, the integral diverges. The system is **not BIBO stable**. This is a pure oscillator (undamped second-order system with poles on the imaginary axis).

---

## 6. Connections and Cross-References

- **Lecture 04 (Continuous-Time Systems):** The linearity and time-invariance tests from Lecture 04 are prerequisites for determining whether a system qualifies as LTI. The systems classified in this lecture as LTI are the ones whose impulse response fully characterizes them.
- **Lecture 03 (Continuous-Time Signals):** The Dirac delta function $\delta(t)$ is the test signal used to define the impulse response. The sifting property $x(t) = \int x(\tau) \delta(t-\tau) d\tau$ is the starting point for deriving the convolution integral.
- **Lecture 06 (Convolution):** The convolution integral derived in this lecture is the subject of Lecture 06, which covers the step-by-step graphical convolution procedure, convolution tables, and algebraic properties (commutative, associative, distributive).
- **Fourier Transform (upcoming):** The frequency response $H(j\omega) = \mathcal{F}\{h(t)\}$ is the Fourier transform of the impulse response. LTI system analysis in the frequency domain depends on the convolution property: $\mathcal{F}\{x(t) * h(t)\} = X(j\omega) H(j\omega)$.
- **Laplace Transform (upcoming):** The transfer function $H(s) = \mathcal{L}\{h(t)\}$ is the Laplace transform of the impulse response. Pole locations in the $s$-plane determine stability: poles in the left-half plane (Re$(s) < 0$) indicate stable systems.
- **Control Systems (future course):** BIBO stability, causality, and the impulse response are foundational to control theory. The Routh-Hurwitz criterion, Nyquist stability criterion, and state-space stability analysis all build on these concepts.
- **Digital Signal Processing (future course):** The discrete-time counterparts of these concepts — the unit pulse response, discrete convolution $y[n] = x[n] * h[n]$, and the $z$-transform — parallel the continuous-time results introduced here.

---

## 7. Exam Tip: Systematic Classification of System Properties

### Property Testing Quick Reference

When given a system equation and asked to classify it, test the four properties in this order:

| Step | Property | Key Test | Typical Failure Mode |
| :--- | :--- | :--- | :--- |
| 1 | Memory | Does $y(t)$ depend on $x(\tau)$ for $\tau \neq t$? | Confusing "with memory" with "non-causal" |
| 2 | Causality | Does $y(t)$ depend on $x(\tau)$ for $\tau > t$? | Assuming all dynamic systems are causal |
| 3 | Linearity | Is $T\{\alpha x_1 + \beta x_2\} = \alpha T\{x_1\} + \beta T\{x_2\}$? | Forgetting to check scaling and additivity separately |
| 4 | Time-invariance | Is $T\{x(t-t_0)\} = y(t-t_0)$? | Confusing the function $t$ (time variable) with a constant |

### Common Exam Patterns for LTI Systems

**Pattern 1: Given a differential equation, find the impulse response.**
- Procedure: Solve the ODE with $x(t) = \delta(t)$ and initial rest conditions.
- Use the method of integrating factors or characteristic equation.
- Jump conditions at $t=0$ must be computed by integrating the differential equation.

**Pattern 2: Given $h(t)$ and $x(t)$, compute $y(t)$ via convolution.**
- Sketch both signals to determine the piecewise intervals.
- There are always $N+1$ cases where $N$ is the number of breakpoints in the combined support regions.
- Verify continuity at interval boundaries.

**Pattern 3: Given a description of a system, determine if it is LTI.**
- Test linearity first (faster to disprove).
- Test time-invariance second.
- Systems with explicit $t$ in the equation are always time-varying unless $t$ appears only in the $(t-\tau)$ combination.

**Pattern 4: Given $h(t)$, determine BIBO stability.**
- Compute $\int_{-\infty}^{\infty} |h(t)| dt$. If finite, the system is BIBO stable.
- Key functions and their integrability:

| $h(t)$ | $\int \|h\|$ | Stable? |
| :--- | :--- | :--- |
| $e^{-at} u(t)$, $a > 0$ | $1/a$ | Yes |
| $e^{-a\|t\|}$, $a > 0$ | $2/a$ | Yes |
| $u(t)$ | $\infty$ | No |
| $t^n u(t)$ | $\infty$ | No |
| $\sin(\omega_0 t) u(t)$ | $\infty$ | No |
| $\delta(t)$ | $1$ | Yes |

> **[Key Insight]**
>
> The most common exam error: declaring a system unstable because the impulse response does not decay to zero as $t \to \infty$. While $h(t) = u(t)$ (does not decay) is indeed unstable, $h(t) = 1$ (a constant for all $t$) is also unstable but for a different reason — the integral $\int_{-\infty}^{\infty} |1| dt$ diverges. In contrast, $h(t) = e^{-|t|}$ decays both forward and backward in time and is stable. Always use the absolute integrability test, not just the decay rate for $t \to \infty$.

### Convolution Shortcut for Exam Problems

For piecewise-constant signals, convolution reduces to computing overlapping areas. The key steps:
1. Identify the breakpoints of both signals.
2. Sort the breakpoints to determine the piecewise intervals.
3. For each interval, the overlap region is fixed, and integration is straightforward.
4. The result $y(t)$ is a continuous function (even if the individual signals are discontinuous).

For causal exponential and sinusoidal signals, use the standard convolution table:

| $x(t)$ | $h(t)$ | $x(t) * h(t)$ |
| :--- | :--- | :--- |
| $e^{at} u(t)$ | $e^{bt} u(t)$ | $\frac{e^{at} - e^{bt}}{a - b} u(t)$, $a \neq b$ |
| $e^{at} u(t)$ | $e^{at} u(t)$ | $t e^{at} u(t)$ |
| $e^{at} u(t)$ | $u(t)$ | $\frac{e^{at} - 1}{a} u(t)$ |
| $u(t)$ | $u(t)$ | $t u(t)$ |
| $\sin(\omega_0 t) u(t)$ | $e^{at} u(t)$ | $\frac{\omega_0 e^{at} - \omega_0 \cos(\omega_0 t) - a \sin(\omega_0 t)}{a^2 + \omega_0^2} u(t)$ |