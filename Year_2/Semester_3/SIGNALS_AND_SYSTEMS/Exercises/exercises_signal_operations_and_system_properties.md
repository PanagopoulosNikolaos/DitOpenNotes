# Exercises: Signal Operations, Energy/Power, and System Properties

This practice problem set provides step-by-step solutions for signal transformations, even/odd decomposition, energy/power integrals, and formal system property proofs.

---

## Problem 1: Even and Odd Signal Decomposition

Given the continuous-time signal:
$$
x(t) = (1 + 2t + 3t^2) \cdot u(t)
$$

### Questions:
1. Find the analytical expression for the even part $x_e(t)$.
2. Find the analytical expression for the odd part $x_o(t)$.
3. Verify that $x_e(t) + x_o(t) = x(t)$.

---

### Solution to Problem 1

Recall that:
$$
x_e(t) = \frac{x(t) + x(-t)}{2}, \quad x_o(t) = \frac{x(t) - x(-t)}{2}
$$

Substitute $x(-t)$:
$$
x(-t) = [1 + 2(-t) + 3(-t)^2] u(-t) = (1 - 2t + 3t^2) u(-t)
$$

#### 1. Even Component $x_e(t)$:
$$
x_e(t) = \frac{1}{2} \left[ (1 + 2t + 3t^2) u(t) + (1 - 2t + 3t^2) u(-t) \right]
$$
- For $t > 0$ ($u(t) = 1, u(-t) = 0$):
  $$x_e(t) = \frac{1}{2} (1 + 2t + 3t^2)$$
- For $t < 0$ ($u(t) = 0, u(-t) = 1$):
  $$x_e(t) = \frac{1}{2} (1 - 2t + 3t^2) = \frac{1}{2} [1 + 2(-t) + 3(-t)^2]$$
Notice $x_e(t) = x_e(-t)$ for all $t$.

#### 2. Odd Component $x_o(t)$:
$$
x_o(t) = \frac{1}{2} \left[ (1 + 2t + 3t^2) u(t) - (1 - 2t + 3t^2) u(-t) \right]
$$
- For $t > 0$:
  $$x_o(t) = \frac{1}{2} (1 + 2t + 3t^2)$$
- For $t < 0$:
  $$x_o(t) = -\frac{1}{2} (1 - 2t + 3t^2)$$
Notice $x_o(-t) = -x_o(t)$ for all $t$.

#### 3. Verification:
For $t > 0$:
$$x_e(t) + x_o(t) = \frac{1 + 2t + 3t^2}{2} + \frac{1 + 2t + 3t^2}{2} = 1 + 2t + 3t^2 = x(t)$$
For $t < 0$:
$$x_e(t) + x_o(t) = \frac{1 - 2t + 3t^2}{2} - \frac{1 - 2t + 3t^2}{2} = 0 = x(t)$$
Verified.

---

## Problem 2: Formal Proof of System Properties

Consider the system:
$$
y(t) = \mathcal{T}\{x(t)\} = x\left(\frac{t}{2}\right)
$$

### Questions:
Determine whether the system is:
1. Memoryless or Dynamic
2. Invertible
3. Causal
4. Linear
5. Time-Invariant
6. BIBO Stable

---

### Solution to Problem 2

1. **Memory:** At $t = 2$, $y(2) = x(1)$ (depends on past input). At $t = -2$, $y(-2) = x(-1)$ (depends on future input). The system depends on values other than the current instant. $\implies$ **System has Memory (Dynamic)**.
2. **Invertibility:** If $w(t) = y(2t) = x\left(\frac{2t}{2}\right) = x(t)$, an inverse system exists ($\mathcal{T}^{-1}\{y(t)\} = y(2t)$). $\implies$ **Invertible**.
3. **Causality:** For $t < 0$ (e.g., $t = -2$), $y(-2) = x(-1)$. Since $-1 > -2$, the current output requires a future input value. $\implies$ **Non-Causal**.
4. **Linearity:**
   $$\mathcal{T}\{a x_1(t) + b x_2(t)\} = a x_1\left(\frac{t}{2}\right) + b x_2\left(\frac{t}{2}\right) = a y_1(t) + b y_2(t)$$
   Superposition holds. $\implies$ **Linear**.
5. **Time-Invariance:**
   - Delayed input: $x_1(t) = x(t - t_0)$.
   - Response to delayed input: $y_1(t) = \mathcal{T}\{x_1(t)\} = x_1\left(\frac{t}{2}\right) = x\left(\frac{t}{2} - t_0\right)$.
   - Delayed output: $y(t - t_0) = x\left(\frac{t - t_0}{2}\right) = x\left(\frac{t}{2} - \frac{t_0}{2}\right)$.
   - Since $x\left(\frac{t}{2} - t_0\right) \ne x\left(\frac{t}{2} - \frac{t_0}{2}\right)$, $y_1(t) \ne y(t - t_0)$. $\implies$ **Time-Variant**.
6. **BIBO Stability:** If $|x(t)| \le M_x < \infty$ for all $t$, then $|y(t)| = |x(t/2)| \le M_x < \infty$ for all $t$. Every bounded input yields a bounded output. $\implies$ **BIBO Stable**.

