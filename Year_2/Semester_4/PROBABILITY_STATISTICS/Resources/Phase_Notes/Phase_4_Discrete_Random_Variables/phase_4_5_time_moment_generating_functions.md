# Phase 4.5 (Time): Moment Generating Functions for Time-Based Random Variables

Moment Generating Functions (MGFs) and Characteristic Functions provide a powerful mathematical framework for deriving higher-order moments (mean latency, duration variance, skewness) and proving the distribution of **sums of independent processing durations**.

---

## 1. Theoretical Foundation (Time Context)

### Definition of the Time MGF
The Moment Generating Function $M_T(t)$ of a non-negative time random variable $T$ is defined for all real numbers $t$ in an open neighborhood around $t = 0$:

$$M_T(t) = E\left[e^{tT}\right]$$

* **Discrete Time RV:** $M_T(t) = \sum_{t_i} e^{t \cdot t_i} \cdot P(T = t_i)$
* **Continuous Time RV:** $M_T(t) = \int_{0}^{\infty} e^{t \cdot \tau} \cdot f(\tau) \, d\tau$

### Finding Duration Moments via Differentiation
The $n$-th raw moment of duration $E[T^n]$ is obtained by evaluating the $n$-th derivative of $M_T(t)$ at $t = 0$:

$$\boxed{E[T^n] = \left. \frac{d^n}{dt^n} M_T(t) \right|_{t=0} = M_T^{(n)}(0)}$$

Specifically:
* **Mean Duration:** $E[T] = M'_T(0)$
* **Duration Variance:** $\boxed{V(T) = E[T^2] - (E[T])^2 = M''_T(0) - (M'_T(0))^2}$

### Key MGF Properties in Time Modeling

1. **Linear Transformation of Time Units:**
   If duration $Y = aT + b$ (where $a$ is a unit scaling factor and $b$ is fixed overhead):
   $$\boxed{M_{aT+b}(t) = e^{bt} \cdot M_T(at)}$$

2. **Sum of Independent Stage Durations:**
   If total system execution time is the sum of $k$ independent sequential stage durations $T_{\text{total}} = T_1 + T_2 + \dots + T_k$:
   $$\boxed{M_{T_{\text{total}}}(t) = M_{T_1}(t) \cdot M_{T_2}(t) \cdots M_{T_k}(t)}$$

3. **Uniqueness Theorem:**
   If two time random variables have identical MGFs in a neighborhood of $t=0$, they possess the exact same probability distribution.

---

## 2. Common MGFs in Time Contexts

| Distribution | Parameters | MGF $M_T(t)$ | Domain Constraint |
| :--- | :--- | :--- | :--- |
| **Bernoulli Slot** | $p$ | $q + p e^t \quad (q = 1-p)$ | All $t \in \mathbb{R}$ |
| **Binomial Slots** | $n, p$ | $(q + p e^t)^n$ | All $t \in \mathbb{R}$ |
| **Poisson Count** | $\lambda_t = \lambda \cdot t$ | $e^{\lambda_t (e^t - 1)}$ | All $t \in \mathbb{R}$ |
| **Geometric Slots** (Def A) | $p$ | $\frac{p e^t}{1 - q e^t}$ | $t < -\ln q$ |
| **Exponential Time** | $\lambda$ | $\frac{\lambda}{\lambda - t}$ | $t < \lambda$ |
| **Normal Latency** | $\mu, \sigma^2$ | $e^{\mu t + \frac{1}{2}\sigma^2 t^2}$ | All $t \in \mathbb{R}$ |

---

## 3. Time-Specific Gotchas

### Gotcha 1: Evaluating Outside the Radius of Convergence
MGF formulas for time distributions like Exponential ($t < \lambda$) or Geometric ($t < -\ln q$) exist **only** within specific domain constraints. Evaluating $M_T(t)$ at $t \ge \lambda$ causes the integral/series to diverge. Always check domain bounds when manipulating MGF expressions.

### Gotcha 2: Incorrect Linear Time Scaling MGF Formula
When converting $T$ to $Y = aT + b$, students often incorrectly write $M_Y(t) = a M_T(t) + b$. The correct relation is $M_Y(t) = e^{bt} M_T(at)$. Note that $a$ multiplies $t$ inside $M_T(\cdot)$, and $b$ becomes an exponential scaling term $e^{bt}$.

### Gotcha 3: Multiplying MGFs for Dependent Processing Stages
The product rule $M_{T_1 + T_2}(t) = M_{T_1}(t) \cdot M_{T_2}(t)$ holds **only if** stage durations $T_1$ and $T_2$ are independent. If Stage 2 latency depends on Stage 1 completion time, the joint expectation $E[e^{t(T_1 + T_2)}]$ cannot be factored into a simple product.

---

## 4. Solved Exercises (10 Examples)

### Exercise 1: Finding Mean and Variance from a Duration MGF
**Problem:** The response time $T$ (seconds) of a service has MGF $M_T(t) = (1 - 2t)^{-1}$ for $t < 0.5$. Find $E[T]$ and $V(T)$.

**Solution:**
- **Step 1: Compute first derivative $M'_T(t)$.**
  $$M_T(t) = (1 - 2t)^{-1}$$
  $$M'_T(t) = -1(1 - 2t)^{-2} (-2) = 2(1 - 2t)^{-2}$$
- **Step 2: WIP State for mean.**
  Evaluate at $t=0$:
  $$E[T] = M'_T(0) = 2(1 - 0)^{-2} = 2\text{ seconds}$$
- **Step 3: Compute second derivative and variance.**
  $$M''_T(t) = 2(-2)(1 - 2t)^{-3}(-2) = 8(1 - 2t)^{-3}$$
  $$E[T^2] = M''_T(0) = 8(1)^{-3} = 8$$
  $$V(T) = E[T^2] - (E[T])^2 = 8 - 2^2 = 8 - 4 = 4\text{ sec}^2$$

---

### Exercise 2: Deriving MGF of a Bernoulli Active Time Slot
**Problem:** A time slot is active ($T = 1$) with probability $p$ and idle ($T = 0$) with probability $q = 1-p$. Derive $M_T(t)$.

**Solution:**
- **Step 1: Write definition sum.**
  $$M_T(t) = E\left[e^{tT}\right] = e^{t(0)} \cdot P(T=0) + e^{t(1)} \cdot P(T=1)$$
- **Step 2: WIP State.**
  $$M_T(t) = 1 \cdot q + e^t \cdot ?$$
- **Step 3: Final Calculation.**
  $$M_T(t) = q + p e^t$$

---

### Exercise 3: Sum of Independent Poisson Arrival Processes
**Problem:** Two independent queue arrival counts over time window $t$ have Poisson distributions $X \sim Po(\lambda_1)$ and $Y \sim Po(\lambda_2)$. Find the MGF of $W = X + Y$ and identify its distribution.

**Solution:**
- **Step 1: Use MGF product rule.**
  $$M_W(t) = M_X(t) \cdot M_Y(t) = e^{\lambda_1 (e^t - 1)} \cdot e^{\lambda_2 (e^t - 1)}$$
- **Step 2: WIP State.**
  $$M_W(t) = e^{\lambda_1(e^t - 1) + \lambda_2(e^t - 1)} = e^{?}$$
- **Step 3: Final Calculation.**
  $$M_W(t) = e^{(\lambda_1 + \lambda_2)(e^t - 1)}$$
  By uniqueness, $W \sim Po(\lambda_1 + \lambda_2)$.

---

### Exercise 4: MGF Linear Transformation of Latency
**Problem:** If execution time $T$ has MGF $M_T(t) = e^{2t + 8t^2}$, find the MGF of scaled time $Y = 3T - 5$.

**Solution:**
- **Step 1: Apply $M_Y(t) = e^{-5t} M_T(3t)$.**
  Substitute $3t$ into $M_T(\cdot)$:
  $$M_T(3t) = e^{2(3t) + 8(3t)^2} = e^{6t + 8(9t^2)} = e^{6t + 72t^2}$$
- **Step 2: WIP State.**
  $$M_Y(t) = e^{-5t} \cdot e^{6t + 72t^2} = e^{-5t + 6t + 72t^2} = e^{?}$$
- **Step 3: Final Calculation.**
  $$M_Y(t) = e^{t + 72t^2}$$
  *(This identifies $Y \sim N(\mu = 1, \sigma^2 = 144)$).*

---

### Exercise 5: Expected Duration from Discrete Empirical MGF
**Problem:** Discrete latency $T \in \{10, 20\}\text{ ms}$ has PMF $P(T=10) = 0.4$, $P(T=20) = 0.6$. Write $M_T(t)$ and compute $E[T]$ by differentiation.

**Solution:**
- **Step 1: Write MGF.**
  $$M_T(t) = 0.4 e^{10t} + 0.6 e^{20t}$$
- **Step 2: WIP State for derivative.**
  $$M'_T(t) = 0.4(10)e^{10t} + 0.6(20)e^{20t} = 4e^{10t} + ?$$
- **Step 3: Final Calculation.**
  $$M'_T(t) = 4e^{10t} + 12e^{20t}$$
  Evaluate at $t=0$:
  $$E[T] = M'_T(0) = 4(1) + 12(1) = 16\text{ ms}$$

---

### Exercise 6: Sum of Independent Binomial Time Slots
**Problem:** Let $X \sim B(n, p)$ and $Y \sim B(m, p)$ be independent active time slot counts. Find $M_{X+Y}(t)$.

**Solution:**
- **Step 1: Multiply MGFs.**
  $$M_{X+Y}(t) = (q + p e^t)^n \cdot (q + p e^t)^m$$
- **Step 2: WIP State.**
  $$M_{X+Y}(t) = (q + p e^t)^{n + ?}$$
- **Step 3: Final Calculation.**
  $$M_{X+Y}(t) = (q + p e^t)^{n + m}$$
  By uniqueness, $X + Y \sim B(n + m, p)$.

---

### Exercise 7: Deriving MGF of Continuous Exponential Duration
**Problem:** Derive the MGF of continuous service time $T \sim Exp(\lambda)$ with PDF $f(\tau) = \lambda e^{-\lambda \tau}$ for $\tau \ge 0$.

**Solution:**
- **Step 1: Set up integral.**
  $$M_T(t) = \int_{0}^{\infty} e^{t\tau} \lambda e^{-\lambda \tau} d\tau = \lambda \int_{0}^{\infty} e^{(t - \lambda)\tau} d\tau$$
- **Step 2: WIP State (for $t < \lambda$).**
  $$\int_{0}^{\infty} e^{(t - \lambda)\tau} d\tau = \left[ \frac{e^{(t - \lambda)\tau}}{t - \lambda} \right]_{0}^{\infty} = 0 - \frac{1}{t - \lambda}$$
- **Step 3: Final Calculation.**
  $$M_T(t) = \lambda \left( \frac{-1}{t - \lambda} \right) = \frac{\lambda}{\lambda - t} \quad (\text{for } t < \lambda)$$

---

### Exercise 8: Taylor Series Expansion of Duration MGF
**Problem:** A duration MGF is given by $M_T(t) = e^{t^2 / 2}$. Find $E[T^4]$ using Taylor expansion.

**Solution:**
- **Step 1: Taylor series for $e^u = \sum \frac{u^k}{k!}$.**
  Substitute $u = t^2 / 2$:
  $$M_T(t) = 1 + \left(\frac{t^2}{2}\right) + \frac{(t^2/2)^2}{2!} + \dots = 1 + \frac{t^2}{2} + \frac{t^4}{8} + \dots$$
- **Step 2: WIP State.**
  Match coefficient with general definition $M_T(t) = \sum \frac{E[T^k]}{k!} t^k$:
  $$\frac{E[T^4]}{4!} = \frac{1}{8}$$
- **Step 3: Final Calculation.**
  $$E[T^4] = \frac{4!}{8} = \frac{24}{8} = 3$$

---

### Exercise 9: Characteristic Function of Symmetric Delay Difference
**Problem:** Show that if delay difference $D = T_1 - T_2$ is symmetric about 0 ($D \sim -D$), its characteristic function $\phi_D(t) = E[e^{itD}]$ is purely real.

**Solution:**
- **Step 1: Relate $\phi_D(t)$ to $\phi_{-D}(t)$.**
  $$\phi_{-D}(t) = E\left[e^{it(-D)}\right] = \phi_D(-t)$$
- **Step 2: WIP State.**
  Symmetry implies $\phi_D(t) = \phi_D(-t)$. Also, complex conjugation gives:
  $$\overline{\phi_D(t)} = \overline{E[\cos(tD) + i\sin(tD)]} = E[\cos(tD)] - i E[\sin(tD)] = \phi_D(-t)$$
- **Step 3: Final Calculation.**
  $$\overline{\phi_D(t)} = \phi_D(t)$$
  A complex quantity equal to its conjugate must be purely real (so $E[\sin(tD)] = 0$).

---

### Exercise 10: Sum of Two Independent Stage Times (Exponential MGFs)
**Problem:** Two independent pipeline stages have exponential durations $T_1 \sim Exp(\lambda)$ and $T_2 \sim Exp(\lambda)$. Find $M_{T_1 + T_2}(t)$ and compute the mean total duration $E[T_1 + T_2]$.

**Solution:**
- **Step 1: Multiply MGFs.**
  $$M_{T_1 + T_2}(t) = M_{T_1}(t) \cdot M_{T_2}(t) = \left(\frac{\lambda}{\lambda - t}\right) \cdot \left(\frac{\lambda}{\lambda - t}\right) = \lambda^2 (\lambda - t)^{-2}$$
- **Step 2: WIP State for derivative.**
  $$M'_{T_1 + T_2}(t) = \lambda^2 (-2)(\lambda - t)^{-3}(-1) = 2\lambda^2 (\lambda - t)^{-3}$$
- **Step 3: Final Calculation.**
  Evaluate at $t=0$:
  $$E[T_1 + T_2] = M'_{T_1 + T_2}(0) = 2\lambda^2 (\lambda)^{-3} = \frac{2}{\lambda}$$
  *(Matches $E[T_1] + E[T_2] = \frac{1}{\lambda} + \frac{1}{\lambda} = \frac{2}{\lambda}$).*
