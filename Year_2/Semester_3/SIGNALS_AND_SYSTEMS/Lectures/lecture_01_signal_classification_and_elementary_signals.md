# Lecture 01: Signal Classification and Elementary Signals

This lecture establishes the mathematical taxonomy of continuous-time and discrete-time signals, defines signal energy and power, presents even/odd signal decomposition, and formalizes foundational elementary signals (unit step, Dirac delta impulse, complex exponential).

---

## 1. Mathematical Definitions and Classifications

A **signal** is a mathematical function conveying information about the state or behavior of a physical system.

### 1.1 Continuous-Time vs. Discrete-Time
- **Continuous-Time (CT) Signals:** Defined over a continuum of time $t \in \mathbb{R}$, denoted $x(t)$.
- **Discrete-Time (DT) Signals:** Defined only at integer sample instants $n \in \mathbb{Z}$, denoted $x[n]$.

### 1.2 Deterministic vs. Random Signals
- **Deterministic:** Values are completely described by an explicit mathematical formula with zero uncertainty (e.g., $x(t) = A \cos(\omega_0 t + \theta)$).
- **Random / Stochastic:** Characterized probabilistically via statistical averages (e.g., thermal noise, speech waveforms).

### 1.3 Periodicity
A CT signal $x(t)$ is **periodic** with fundamental period $T_0 > 0$ if:
$$
x(t) = x(t + T_0) \quad \forall t \in \mathbb{R}
$$
The fundamental frequency is:
$$
f_0 = \frac{1}{T_0}, \quad \omega_0 = \frac{2\pi}{T_0}
$$

---

## 2. Signal Energy and Power

To evaluate the strength of a signal over all time:

### 2.1 Continuous-Time Energy and Power
The total energy $E_\infty$ of a signal $x(t)$ is defined as:
$$
E_\infty = \int_{-\infty}^{\infty} |x(t)|^2 \, dt
$$

The time-average power $P_\infty$ is defined as:
$$
P_\infty = \lim_{T \to \infty} \frac{1}{2T} \int_{-T}^{T} |x(t)|^2 \, dt
$$

#### Classification:
1. **Energy Signal:** $0 < E_\infty < \infty \implies P_\infty = 0$.
2. **Power Signal:** $0 < P_\infty < \infty \implies E_\infty = \infty$ (e.g., non-zero periodic signals).
3. **Neither:** Signals where both $E_\infty \to \infty$ and $P_\infty \to \infty$ (e.g., $x(t) = t$).

---

## 3. Even and Odd Signal Symmetry

Any arbitrary signal $x(t)$ can be uniquely decomposed into the sum of an even component $x_e(t)$ and an odd component $x_o(t)$:

$$
x(t) = x_e(t) + x_o(t)
$$

where:
$$
x_e(t) = \frac{x(t) + x(-t)}{2} \quad \text{satisfying } x_e(t) = x_e(-t)
$$
$$
x_o(t) = \frac{x(t) - x(-t)}{2} \quad \text{satisfying } x_o(t) = -x_o(-t)
$$

---

## 4. Foundational Elementary Signals

### 4.1 Unit Step Function $u(t)$
Defined by the Heaviside step:
$$
u(t) = \begin{cases} 1, & t > 0 \\ 0, & t < 0 \end{cases}
$$

### 4.2 Dirac Delta Function $\delta(t)$ (Unit Impulse)
Defined by the sifting (sampling) property:
$$
\delta(t) = 0 \quad \text{for } t \ne 0, \quad \int_{-\infty}^{\infty} \delta(t) \, dt = 1
$$
$$
\int_{-\infty}^{\infty} x(t) \delta(t - t_0) \, dt = x(t_0)
$$
The unit step is the integral of the impulse:
$$
u(t) = \int_{-\infty}^{t} \delta(\tau) \, d\tau \implies \frac{du(t)}{dt} = \delta(t)
$$

### 4.3 Complex Exponential Signal
$$
x(t) = C e^{s t}
$$
where $s = \sigma + j\omega$ is a complex frequency. Using Euler's relation:
$$
e^{j\omega_0 t} = \cos(\omega_0 t) + j\sin(\omega_0 t)
$$
If $\sigma < 0$, the signal represents an exponentially damped oscillation.

---

## 5. Summary

- Signals are classified across time continuity, periodicity, and energy/power bounds.
- Any signal can be decomposed into orthogonal even and odd symmetric parts.
- The Dirac delta $\delta(t)$ serves as the fundamental building block for characterizing continuous systems via its sifting property.

