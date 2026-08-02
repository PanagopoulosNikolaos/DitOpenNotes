# Phase 5.6 (Time): Multivariate Random Variable Fundamentals for Time Data

In complex systems, performance depends on multiple continuous time metrics simultaneously (e.g., database query time $T_1$ and network transmission time $T_2$). Multivariate continuous random variables model the joint behavior, dependencies, and joint probabilities of multiple continuous time durations.

---

## 1. Joint Probability Density Function (Joint PDF)

For two continuous time random variables $T_1$ and $T_2$, the joint PDF $f_{T_1, T_2}(t_1, t_2)$ satisfies:

1. **Non-negativity:** $f_{T_1, T_2}(t_1, t_2) \ge 0$ for all $(t_1, t_2) \in \mathbb{R}^2$.
2. **Total Probability Normalization:**
   $$\boxed{\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f_{T_1, T_2}(t_1, t_2) \, dt_1 \, dt_2 = 1}$$
3. **Region Probability:** The probability that $(T_1, T_2)$ falls within time region $R$ is:
   $$P((T_1, T_2) \in R) = \iint_R f_{T_1, T_2}(t_1, t_2) \, dt_1 \, dt_2$$

---

## 2. Marginal Densities and Independence of Time Metrics

### 2.1 Marginal PDFs
The individual (marginal) density of $T_1$ is obtained by integrating out $T_2$ over its entire domain:

$$\boxed{f_{T_1}(t_1) = \int_{-\infty}^{\infty} f_{T_1, T_2}(t_1, t_2) \, dt_2}, \quad \boxed{f_{T_2}(t_2) = \int_{-\infty}^{\infty} f_{T_1, T_2}(t_1, t_2) \, dt_1}$$

### 2.2 Independence Criterion for Time Variables
Time random variables $T_1$ and $T_2$ are **stochastically independent** if and only if their joint PDF factors into the product of their marginal PDFs for all $(t_1, t_2)$:

$$\boxed{f_{T_1, T_2}(t_1, t_2) = f_{T_1}(t_1) \cdot f_{T_2}(t_2)}$$

---

## 3. Conditional Probability Density Functions

The conditional density of stage 2 time $T_2$ given that stage 1 time was observed to be $T_1 = t_1$ is:

$$\boxed{f_{T_2 \mid T_1}(t_2 \mid t_1) = \frac{f_{T_1, T_2}(t_1, t_2)}{f_{T_1}(t_1)}, \quad \text{for } f_{T_1}(t_1) > 0}$$

The conditional probability of duration $T_2$ taking a value in $[a, b]$ given $T_1 = t_1$ is:

$$P(a \le T_2 \le b \mid T_1 = t_1) = \int_a^b f_{T_2 \mid T_1}(t_2 \mid t_1) \, dt_2$$

---

## 4. Time-Specific Gotchas

### Gotcha 1: Dependent Support Boundaries (e.g., $0 \le t_1 \le t_2 \le 1$)
Even if the joint density formula looks factorable (e.g., $f(t_1, t_2) = k$), if the support bounds couple the variables (such as $0 \le t_1 \le t_2 \le c$), $T_1$ and $T_2$ are **DEPENDENT**. Always inspect support limits!

### Gotcha 2: Integrating Over Rectangular vs Non-Rectangular Regions
When calculating joint probability bounds like $P(T_1 + T_2 \le 10)$, the integration limits are coupled ($0 \le t_2 \le 10 - t_1$). Do not integrate both limits independently from $0$ to $10$.

---

## 5. Solved Exercises (10 Examples)

### Exercise 1: Finding Normalizing Constant $k$ for Joint Processing Times
**Problem:** Dual processing times $(T_1, T_2)$ have joint PDF $f(t_1, t_2) = k \cdot t_1 t_2$ for $0 \le t_1 \le 2$ and $0 \le t_2 \le 3$ (in seconds), and $0$ elsewhere. Find $k$.

**Solution:**
- **Step 1: Set double integral equal to 1.**
  $$\int_{0}^{2} \int_{0}^{3} k t_1 t_2 \, dt_2 \, dt_1 = 1$$
- **Step 2: WIP State.**
  $$k \left( \int_{0}^{2} t_1 dt_1 \right) \left( \int_{0}^{3} t_2 dt_2 \right) = k \left[ \frac{t_1^2}{2} \right]_0^2 \left[ \frac{t_2^2}{2} \right]_0^3$$
  $$k (2) (4.5) = 9k = 1$$
- **Step 3: Final Result.**
  $$k = 1/9$$

---

### Exercise 2: Computing Marginal PDFs
**Problem:** For joint PDF $f(t_1, t_2) = \frac{1}{9} t_1 t_2$ on $[0, 2] \times [0, 3]$, find marginal PDFs $f_{T_1}(t_1)$ and $f_{T_2}(t_2)$.

**Solution:**
- **Step 1: Compute $f_{T_1}(t_1)$.**
  $$f_{T_1}(t_1) = \int_{0}^{3} \frac{1}{9} t_1 t_2 \, dt_2 = \frac{t_1}{9} \left[ \frac{t_2^2}{2} \right]_0^3 = \frac{t_1}{9} (4.5) = \frac{t_1}{2}, \quad 0 \le t_1 \le 2$$
- **Step 2: Compute $f_{T_2}(t_2)$.**
  $$f_{T_2}(t_2) = \int_{0}^{2} \frac{1}{9} t_1 t_2 \, dt_1 = \frac{t_2}{9} \left[ \frac{t_1^2}{2} \right]_0^2 = \frac{2 t_2}{9}, \quad 0 \le t_2 \le 3$$
- **Step 3: Final Result.**
  $f_{T_1}(t_1) = \frac{t_1}{2}$ for $0 \le t_1 \le 2$; $f_{T_2}(t_2) = \frac{2 t_2}{9}$ for $0 \le t_2 \le 3$.

---

### Exercise 3: Testing Independence of Time Variables
**Problem:** Test whether $T_1$ and $T_2$ from Exercises 1 and 2 are independent.

**Solution:**
- **Step 1: Check $f_{T_1}(t_1) \cdot f_{T_2}(t_2)$.**
  $$f_{T_1}(t_1) \cdot f_{T_2}(t_2) = \left(\frac{t_1}{2}\right) \left(\frac{2 t_2}{9}\right) = \frac{t_1 t_2}{9}$$
- **Step 2: Compare with joint PDF $f(t_1, t_2)$.**
  $$\frac{t_1 t_2}{9} = f_{T_1, T_2}(t_1, t_2)$$
- **Step 3: Final Result.**
  Since product of marginals equals joint PDF and support is rectangular, $T_1$ and $T_2$ are independent.

---

### Exercise 4: Joint Probability Over a Region $P(T_1 \le 1, T_2 \le 2)$
**Problem:** Using joint PDF $f(t_1, t_2) = \frac{1}{9} t_1 t_2$ on $[0, 2] \times [0, 3]$, find $P(T_1 \le 1 \text{ and } T_2 \le 2)$.

**Solution:**
- **Step 1: Set up double integral.**
  $$P(T_1 \le 1, T_2 \le 2) = \int_{0}^{1} \int_{0}^{2} \frac{1}{9} t_1 t_2 \, dt_2 \, dt_1$$
- **Step 2: WIP State.**
  $$\int_0^1 \frac{t_1}{9} dt_1 \times \int_0^2 t_2 dt_2 = \left[ \frac{t_1^2}{18} \right]_0^1 \times \left[ \frac{t_2^2}{2} \right]_0^2 = \frac{1}{18} \times 2$$
- **Step 3: Final Result.**
  $$P(T_1 \le 1, T_2 \le 2) = \frac{1}{9} \approx 0.1111 \text{ (11.11\%)}$$

---

### Exercise 5: Dependent Support Region ($0 \le t_1 \le t_2 \le 1$)
**Problem:** Sequential stage durations $(T_1, T_2)$ have joint PDF $f(t_1, t_2) = 8 t_1 t_2$ for $0 \le t_1 \le t_2 \le 1$. Find marginal PDF $f_{T_2}(t_2)$ and test for independence.

**Solution:**
- **Step 1: Compute $f_{T_2}(t_2)$ by integrating over $t_1 \in [0, t_2]$.**
  $$f_{T_2}(t_2) = \int_{0}^{t_2} 8 t_1 t_2 \, dt_1 = 8 t_2 \left[ \frac{t_1^2}{2} \right]_0^{t_2} = 4 t_2^3, \quad 0 \le t_2 \le 1$$
- **Step 2: WIP State for independence.**
  Support is $0 \le t_1 \le t_2 \le 1$, which is triangular (non-rectangular).
- **Step 3: Final Result.**
  $f_{T_2}(t_2) = 4 t_2^3$. $T_1$ and $T_2$ are dependent due to triangular support.

---

### Exercise 6: Conditional PDF $f_{T_1 \mid T_2}(t_1 \mid t_2)$
**Problem:** For joint PDF $f(t_1, t_2) = 8 t_1 t_2$ on $0 \le t_1 \le t_2 \le 1$, find the conditional density $f_{T_1 \mid T_2}(t_1 \mid t_2 = 0.5)$.

**Solution:**
- **Step 1: Formula for conditional density.**
  $$f_{T_1 \mid T_2}(t_1 \mid t_2) = \frac{f(t_1, t_2)}{f_{T_2}(t_2)} = \frac{8 t_1 t_2}{4 t_2^3} = \frac{2 t_1}{t_2^2}, \quad 0 \le t_1 \le t_2$$
- **Step 2: Substitute $t_2 = 0.5$.**
  $$f_{T_1 \mid T_2}(t_1 \mid 0.5) = \frac{2 t_1}{(0.5)^2} = \frac{2 t_1}{0.25} = 8 t_1, \quad 0 \le t_1 \le 0.5$$
- **Step 3: Final Result.**
  $$f_{T_1 \mid T_2}(t_1 \mid 0.5) = 8 t_1 \text{ for } 0 \le t_1 \le 0.5$$

---

### Exercise 7: Joint Exponential Service Times
**Problem:** Two independent servers have service times $T_1 \sim \text{Exp}(\lambda_1 = 2)$ and $T_2 \sim \text{Exp}(\lambda_2 = 3)$ in seconds. Write the joint PDF $f(t_1, t_2)$ and find $P(T_1 > 1, T_2 > 1)$.

**Solution:**
- **Step 1: Form joint PDF via independence.**
  $$f(t_1, t_2) = (2 e^{-2 t_1}) (3 e^{-3 t_2}) = 6 e^{-(2 t_1 + 3 t_2)}, \quad t_1, t_2 \ge 0$$
- **Step 2: WIP State.**
  $$P(T_1 > 1, T_2 > 1) = P(T_1 > 1) \cdot P(T_2 > 1) = e^{-2(1)} \cdot e^{-3(1)} = e^{-5}$$
  $$e^{-5} \approx 0.006738$$
- **Step 3: Final Result.**
  $$P(T_1 > 1, T_2 > 1) = 0.0067 \text{ (0.67\%)}$$

---

### Exercise 8: Cumulative Total Time Constraint $P(T_1 + T_2 \le c)$
**Problem:** Independent uniform processing times $T_1 \sim U(0, 1)$ and $T_2 \sim U(0, 1)$. Find $P(T_1 + T_2 \le 1)$.

**Solution:**
- **Step 1: Set up double integral limits.**
  $$P(T_1 + T_2 \le 1) = \int_{0}^{1} \int_{0}^{1 - t_1} (1)(1) \, dt_2 \, dt_1$$
- **Step 2: WIP State.**
  $$\int_{0}^{1} (1 - t_1) dt_1 = \left[ t_1 - \frac{t_1^2}{2} \right]_0^1 = 1 - 0.5 = 0.5$$
- **Step 3: Final Result.**
  $$P(T_1 + T_2 \le 1) = 0.5 \text{ (50\%)}$$

---

### Exercise 9: Joint Bivariate Normal Latency Model
**Problem:** Parallel microservices have joint bivariate normal latency $(T_1, T_2)$ with means $\mu_1 = 50, \mu_2 = 80$, variances $\sigma_1^2 = 25, \sigma_2^2 = 100$, and correlation $\rho = 0.6$. Find the conditional distribution of $T_2 \mid T_1 = 60\text{ ms}$.

**Solution:**
- **Step 1: Apply Bivariate Normal conditional mean and variance formulas.**
  $$\mu_{2 \mid 1} = \mu_2 + \rho \frac{\sigma_2}{\sigma_1} (t_1 - \mu_1) = 80 + 0.6 \left(\frac{10}{5}\right) (60 - 50)$$
  $$\sigma_{2 \mid 1}^2 = \sigma_2^2 (1 - \rho^2) = 100 (1 - 0.36) = 64$$
- **Step 2: WIP State.**
  $$\mu_{2 \mid 1} = 80 + 0.6 (2) (10) = 80 + 12 = 92\text{ ms}$$
  $$\sigma_{2 \mid 1} = \sqrt{64} = 8\text{ ms}$$
- **Step 3: Final Result.**
  $$T_2 \mid (T_1 = 60) \sim N(92\text{ ms}, 64\text{ ms}^2)$$

---

### Exercise 10: R Code Verification of Joint Probability Integration
**Problem:** Demonstrate how to compute joint probabilities over continuous time regions using Monte Carlo integration in R.

**Solution:**
- **Step 1: R Script Setup.**
```r
set.seed(42)
N <- 1000000

# Simulate independent T1 ~ Exp(2), T2 ~ Exp(3)
t1 <- rexp(N, rate = 2)
t2 <- rexp(N, rate = 3)

# Empirical joint probability P(T1 + T2 <= 1.0)
p_sum_le_1 <- mean((t1 + t2) <= 1.0)
cat("P(T1 + T2 <= 1.0 s):", round(p_sum_le_1, 4), "\n")
```
- **Step 2: Execution Output.**
  `P(T1 + T2 <= 1.0 s): 0.6001`
