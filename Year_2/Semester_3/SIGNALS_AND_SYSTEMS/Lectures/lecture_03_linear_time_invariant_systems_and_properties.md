# Lecture 03: Linear Time-Invariant Systems and Properties

This lecture examines Linear Time-Invariant (LTI) systems, establishing the derivation of the convolution integral from the sifting property, defining the impulse response $h(t)$, and deriving the necessary and sufficient conditions for causality and BIBO stability.

---

## 1. The Significance of LTI Systems

When a system satisfies both **Linearity** (superposition) and **Time-Invariance**, its response to any arbitrary input signal $x(t)$ is entirely determined by its response to a single elementary signal: the **Unit Impulse $\delta(t)$**.

---

## 2. Derivation of the Convolution Integral

Using the sifting property of the Dirac delta function:
$$
x(t) = \int_{-\infty}^{\infty} x(\tau) \delta(t - \tau) \, d\tau
$$

We apply the system operator $\mathcal{T}$ to both sides:
$$
y(t) = \mathcal{T}\{x(t)\} = \mathcal{T}\left\{ \int_{-\infty}^{\infty} x(\tau) \delta(t - \tau) \, d\tau \right\}
$$

By **Linearity** (treating integration as the limiting sum of scaled inputs):
$$
y(t) = \int_{-\infty}^{\infty} x(\tau) \mathcal{T}\{\delta(t - \tau)\} \, d\tau
$$

By **Time-Invariance**, if the response to $\delta(t)$ is the **Impulse Response** $h(t) \equiv \mathcal{T}\{\delta(t)\}$, then:
$$
\mathcal{T}\{\delta(t - \tau)\} = h(t - \tau)
$$

Substituting yields the fundamental **Convolution Integral**:
$$
y(t) = \int_{-\infty}^{\infty} x(\tau) h(t - \tau) \, d\tau \equiv x(t) * h(t)
$$

---

## 3. Algebraic Properties of Convolution

1. **Commutativity:**
   $$x(t) * h(t) = h(t) * x(t)$$
2. **Associativity:**
   $$\big(x(t) * h_1(t)\big) * h_2(t) = x(t) * \big(h_1(t) * h_2(t)\big)$$
   *(Represents the cascade/series connection of two LTI subsystems).*
3. **Distributivity:**
   $$x(t) * \big(h_1(t) + h_2(t)\big) = x(t) * h_1(t) + x(t) * h_2(t)$$
   *(Represents the parallel connection of two LTI subsystems).*

---

## 4. Characterizing LTI System Properties via $h(t)$

Because $h(t)$ completely describes an LTI system, system properties translate directly into mathematical conditions on $h(t)$:

### 4.1 Memoryless LTI Systems
An LTI system is memoryless if and only if:
$$
h(t) = K \delta(t)
$$
for some constant $K$. If $h(t)$ has non-zero values for any $t \ne 0$, the system possesses memory.

### 4.2 Causal LTI Systems
An LTI system is causal if and only if its impulse response is zero for all negative time:
$$
h(t) = 0 \quad \forall t < 0
$$
For a causal LTI system, the convolution integral simplifies to:
$$
y(t) = \int_{0}^{\infty} h(\tau) x(t - \tau) \, d\tau = \int_{-\infty}^{t} x(\tau) h(t - \tau) \, d\tau
$$

### 4.3 BIBO Stable LTI Systems
An LTI system is BIBO stable if and only if its impulse response is **absolutely integrable**:
$$
\int_{-\infty}^{\infty} |h(t)| \, dt < \infty
$$

#### Proof:
Let input $x(t)$ be bounded: $|x(t)| \le M_x < \infty$ for all $t$.
$$
|y(t)| = \left| \int_{-\infty}^{\infty} h(\tau) x(t - \tau) \, d\tau \right| \le \int_{-\infty}^{\infty} |h(\tau)| \cdot |x(t - \tau)| \, d\tau \le M_x \int_{-\infty}^{\infty} |h(\tau)| \, d\tau
$$
If $\int_{-\infty}^{\infty} |h(\tau)| \, d\tau = I < \infty$, then $|y(t)| \le M_x \cdot I < \infty$, guaranteeing stability.

---

## 5. Summary

- LTI systems are completely and uniquely defined by their impulse response $h(t)$.
- System output is computed via the continuous convolution integral $x(t) * h(t)$.
- Causality requires $h(t) = 0$ for $t < 0$.
- Stability requires absolute integrability: $\int_{-\infty}^{\infty} |h(t)| dt < \infty$.

