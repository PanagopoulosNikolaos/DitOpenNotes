# Lecture 02: Continuous-Time and Discrete-Time Systems

This lecture formalizes systems as mathematical transformations on signals and details the definitions and rigorous proof methodologies for testing fundamental system properties: memory, invertibility, causality, BIBO stability, time-invariance, and linearity.

---

## 1. System Formalism

A system is an interconnection of components that accepts an input excitation $x(t)$ and produces an output response $y(t)$ via an operator $\mathcal{T}$:

$$
y(t) = \mathcal{T}\{x(t)\}
$$

---

## 2. Six Fundamental System Properties

### 2.1 Memory (Memoryless vs. Dynamic)
- **Memoryless (Static):** The output $y(t)$ at any time $t$ depends strictly on the input $x(t)$ at that same instant:
  $$y(t) = 3 x(t) + x^2(t)$$
- **With Memory (Dynamic):** The output depends on past or future input values:
  $$y(t) = \int_{-\infty}^{t} x(\tau) \, d\tau$$

### 2.2 Invertibility
A system is **invertible** if distinct inputs always produce distinct outputs. An inverse system $\mathcal{T}^{-1}$ exists such that:
$$
w(t) = \mathcal{T}^{-1}\{\mathcal{T}\{x(t)\}\} = x(t)
$$
- Example: $y(t) = 2x(t)$ is invertible with $w(t) = \frac{1}{2}y(t)$.
- Non-invertible: $y(t) = x^2(t)$ (loss of sign information).

### 2.3 Causality
A system is **causal** (non-anticipative) if the output $y(t)$ at any time $t_0$ depends only on input values $x(t)$ for $t \le t_0$.
- All real-time physical systems are causal.
- Non-causal: $y(t) = x(t + 1)$ or $y[n] = x[n] + x[n+1]$.

### 2.4 Bounded-Input Bounded-Output (BIBO) Stability
A system is BIBO stable if every bounded input produces a bounded output:
$$
|x(t)| \le M_x < \infty \implies |y(t)| \le M_y < \infty \quad \forall t
$$
- Stable: $y(t) = \cos(x(t))$ because $|y(t)| \le 1$ for all inputs.
- Unstable: $y(t) = \int_{-\infty}^{t} x(\tau) \, d\tau$ (for bounded input $x(t) = u(t)$, $y(t) = t \cdot u(t) \to \infty$).

### 2.5 Time-Invariance (Shift-Invariance)
A system is **time-invariant** if a time shift in the input signal results in an identical time shift in the output signal:

Let $y(t) = \mathcal{T}\{x(t)\}$. The system is time-invariant if:
$$
\mathcal{T}\{x(t - t_0)\} = y(t - t_0) \quad \forall t_0 \in \mathbb{R}
$$

#### Proof Methodology:
1. Define delayed input: $x_1(t) = x(t - t_0)$.
2. Compute system response to $x_1(t)$: $y_1(t) = \mathcal{T}\{x_1(t)\}$.
3. Shift original output by $t_0$: $y(t - t_0)$.
4. If $y_1(t) \equiv y(t - t_0)$, the system is time-invariant.

### 2.6 Linearity (The Principle of Superposition)
A system is **linear** if it satisfies both:
1. **Additivity:** $\mathcal{T}\{x_1(t) + x_2(t)\} = \mathcal{T}\{x_1(t)\} + \mathcal{T}\{x_2(t)\}$
2. **Homogeneity (Scaling):** $\mathcal{T}\{a \cdot x(t)\} = a \cdot \mathcal{T}\{x(t)\}$ for any scalar $a \in \mathbb{C}$.

Combined Linear Superposition Condition:
$$
\mathcal{T}\{a x_1(t) + b x_2(t)\} = a y_1(t) + b y_2(t)
$$

---

## 3. Worked Verification Example

Consider the system described by:
$$
y(t) = t \cdot x(t)
$$

1. **Memory:** Output depends only on $x(t)$ at the current instant $t$. **Memoryless**.
2. **Causality:** Does not depend on future inputs. **Causal**.
3. **Linearity:**
   $$\mathcal{T}\{a x_1(t) + b x_2(t)\} = t [a x_1(t) + b x_2(t)] = a [t x_1(t)] + b [t x_2(t)] = a y_1(t) + b y_2(t)$$
   **Linear**.
4. **Time-Invariance:**
   - Input shifted: $x_1(t) = x(t - t_0) \implies y_1(t) = t \cdot x_1(t) = t \cdot x(t - t_0)$.
   - Output shifted: $y(t - t_0) = (t - t_0) \cdot x(t - t_0)$.
   - Since $y_1(t) \ne y(t - t_0)$ (due to explicit multiplier $t$), the system is **Time-Variant**.
5. **Stability:** For bounded input $x(t) = 1$, $y(t) = t \to \infty$ as $t \to \infty$. **Unstable**.

