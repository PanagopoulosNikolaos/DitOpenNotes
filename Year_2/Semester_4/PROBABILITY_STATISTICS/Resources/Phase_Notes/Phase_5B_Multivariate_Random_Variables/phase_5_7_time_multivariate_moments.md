# Phase 5.7 (Time): Multivariate Moments, Covariance, and Conditional Expectation

When tracking interconnected execution steps (e.g., frontend load time $T_1$ and backend query time $T_2$), measuring expected joint metrics, co-movement (covariance/correlation), and conditional expected durations becomes essential for system bottleneck analysis.

---

## 1. Covariance and Correlation Between Time Metrics

### 1.1 Covariance Definition
The covariance $\text{Cov}(T_1, T_2)$ measures the linear dependence and joint variability of two continuous time random variables $T_1$ and $T_2$:

$$\boxed{\text{Cov}(T_1, T_2) = E[(T_1 - \mu_1)(T_2 - \mu_2)] = E[T_1 T_2] - E[T_1] E[T_2]}$$

Where:
$$E[T_1 T_2] = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} t_1 t_2 \cdot f_{T_1, T_2}(t_1, t_2) \, dt_1 \, dt_2$$

### 1.2 Pearson Correlation Coefficient $\rho_{T_1, T_2}$
The scale-invariant correlation coefficient ranges between $-1$ and $+1$:

$$\boxed{\rho_{T_1, T_2} = \frac{\text{Cov}(T_1, T_2)}{\sigma_{T_1} \sigma_{T_2}} = \frac{\text{Cov}(T_1, T_2)}{\sqrt{V(T_1) V(T_2)}}}$$

* **$\rho = 0$:** Linear independence (note: independent time RVs always have $\text{Cov} = 0$, but zero covariance does not guarantee independence unless normal).
* **$\rho > 0$:** High $T_1$ latency tends to coincide with high $T_2$ latency.
* **$\rho < 0$:** High $T_1$ latency tends to coincide with low $T_2$ latency.

---

## 2. Variance of Linear Combinations of Time Variables

For constants $a, b$:

$$\boxed{V(a T_1 + b T_2) = a^2 V(T_1) + b^2 V(T_2) + 2 a b \text{Cov}(T_1, T_2)}$$

Specifically for total processing duration $T_{\text{total}} = T_1 + T_2$:

$$V(T_1 + T_2) = V(T_1) + V(T_2) + 2\text{Cov}(T_1, T_2)$$

If $T_1$ and $T_2$ are independent, $\text{Cov}(T_1, T_2) = 0 \implies V(T_1 + T_2) = V(T_1) + V(T_2)$.

---

## 3. Conditional Expectation and Law of Total Expectation

### 3.1 Conditional Expectation Function
The expected value of $T_1$ given that $T_2 = t_2$ is a function of $t_2$:

$$\boxed{E[T_1 \mid T_2 = t_2] = \int_{-\infty}^{\infty} t_1 \cdot f_{T_1 \mid T_2}(t_1 \mid t_2) \, dt_1}$$

### 3.2 Law of Iterated Expectations (Law of Total Expectation)
$$\boxed{E[T_1] = E_{T_2} \left[ E_{T_1 \mid T_2}(T_1 \mid T_2) \right]}$$

---

## 4. Time-Specific Gotchas

### Gotcha 1: Uncorrelated Does Not Mean Independent for Non-Gaussian Time RVs
If $\text{Cov}(T_1, T_2) = 0$, you CANNOT automatically conclude that $T_1$ and $T_2$ are independent unless $(T_1, T_2)$ is jointly Bivariate Normal. Quadratic or non-linear time dependencies can yield $\text{Cov}(T_1, T_2) = 0$ while being strongly dependent.

### Gotcha 2: Ignoring Covariance in Total Processing Variance
When computing the variance of total pipeline time $T_{\text{total}} = T_1 + T_2 + T_3$, summing individual variances $V(T_1) + V(T_2) + V(T_3)$ without checking for non-zero cross-covariances undercounts jitter if stages share server resources (positive correlation).

---

## 5. Solved Exercises (10 Examples)

### Exercise 1: Joint Product Moment $E[T_1 T_2]$
**Problem:** Joint PDF of stage times is $f(t_1, t_2) = \frac{1}{9} t_1 t_2$ on $[0, 2] \times [0, 3]$. Calculate $E[T_1 T_2]$.

**Solution:**
- **Step 1: Set up double integral.**
  $$E[T_1 T_2] = \int_0^2 \int_0^3 t_1 t_2 \left( \frac{1}{9} t_1 t_2 \right) dt_2 dt_1 = \frac{1}{9} \int_0^2 t_1^2 dt_1 \int_0^3 t_2^2 dt_2$$
- **Step 2: WIP State.**
  $$\int_0^2 t_1^2 dt_1 = \left[ \frac{t_1^3}{3} \right]_0^2 = \frac{8}{3}$$
  $$\int_0^3 t_2^2 dt_2 = \left[ \frac{t_2^3}{3} \right]_0^3 = \frac{27}{3} = 9$$
  $$E[T_1 T_2] = \frac{1}{9} \times \frac{8}{3} \times 9 = \frac{8}{3}$$
- **Step 3: Final Result.**
  $$E[T_1 T_2] = \frac{8}{3} \approx 2.6667$$

---

### Exercise 2: Covariance Calculation for Independent Time RVs
**Problem:** For the independent variables in Exercise 1, $E[T_1] = 4/3$ and $E[T_2] = 2$. Verify that $\text{Cov}(T_1, T_2) = 0$.

**Solution:**
- **Step 1: Compute product of individual expectations.**
  $$E[T_1] E[T_2] = \left(\frac{4}{3}\right) (2) = \frac{8}{3}$$
- **Step 2: WIP State.**
  $$\text{Cov}(T_1, T_2) = E[T_1 T_2] - E[T_1] E[T_2] = \frac{8}{3} - \frac{8}{3} = 0$$
- **Step 3: Final Result.**
  $\text{Cov}(T_1, T_2) = 0$, confirming independence.

---

### Exercise 3: Covariance Calculation for Dependent Time RVs
**Problem:** Joint PDF $f(t_1, t_2) = 8 t_1 t_2$ for $0 \le t_1 \le t_2 \le 1$. Given $E[T_1] = 4/15$, $E[T_2] = 4/5$, and $E[T_1 T_2] = 1/4$, calculate $\text{Cov}(T_1, T_2)$.

**Solution:**
- **Step 1: Compute $E[T_1] E[T_2]$.**
  $$E[T_1] E[T_2] = \left(\frac{4}{15}\right) \left(\frac{4}{5}\right) = \frac{16}{75}$$
- **Step 2: WIP State.**
  $$\text{Cov}(T_1, T_2) = \frac{1}{4} - \frac{16}{75} = \frac{75 - 64}{300} = \frac{11}{300}$$
- **Step 3: Final Result.**
  $$\text{Cov}(T_1, T_2) = \frac{11}{300} \approx 0.0367$$

---

### Exercise 4: Pearson Correlation Coefficient $\rho$
**Problem:** For the variables in Exercise 3, $V(T_1) = 11/225$ and $V(T_2) = 2/75$. Calculate correlation $\rho_{T_1, T_2}$.

**Solution:**
- **Step 1: Compute product of standard deviations.**
  $$\sigma_1 \sigma_2 = \sqrt{\frac{11}{225} \cdot \frac{2}{75}} = \sqrt{\frac{22}{16875}} = \frac{\sqrt{22/3}}{75} \approx 0.036055$$
- **Step 2: WIP State.**
  $$\rho = \frac{11/300}{\sqrt{22}/(15 \sqrt{75})} = \frac{0.036667}{0.036055}$$
- **Step 3: Final Result.**
  $$\rho \approx 11 / \sqrt{132} \approx 0.9574$$
  Strong positive correlation between stage times $T_1$ and $T_2$.

---

### Exercise 5: Variance of Sum with Positive Correlation
**Problem:** Stage 1 duration $T_1$ has $V(T_1) = 25\text{ ms}^2$, Stage 2 duration $T_2$ has $V(T_2) = 36\text{ ms}^2$, and $\text{Cov}(T_1, T_2) = 10\text{ ms}^2$. Calculate $V(T_1 + T_2)$.

**Solution:**
- **Step 1: Apply variance of sum formula.**
  $$V(T_1 + T_2) = V(T_1) + V(T_2) + 2\text{Cov}(T_1, T_2)$$
- **Step 2: WIP State.**
  $$V(T_1 + T_2) = 25 + 36 + 2(10) = 61 + 20 = 81\text{ ms}^2$$
- **Step 3: Final Result.**
  $$V(T_1 + T_2) = 81\text{ ms}^2 \implies SD(T_{\text{total}}) = 9\text{ ms}$$

---

### Exercise 6: Variance of Difference $V(T_1 - T_2)$
**Problem:** Using the metrics from Exercise 5, calculate the variance of the delay difference $V(T_1 - T_2)$.

**Solution:**
- **Step 1: Apply formula for variance of difference.**
  $$V(T_1 - T_2) = V(T_1) + V(T_2) - 2\text{Cov}(T_1, T_2)$$
- **Step 2: WIP State.**
  $$V(T_1 - T_2) = 25 + 36 - 2(10) = 61 - 20 = 41\text{ ms}^2$$
- **Step 3: Final Result.**
  $$V(T_1 - T_2) = 41\text{ ms}^2$$

---

### Exercise 7: Conditional Expectation Function $E[T_1 \mid T_2 = t_2]$
**Problem:** Given conditional PDF $f_{T_1 \mid T_2}(t_1 \mid t_2) = \frac{2 t_1}{t_2^2}$ for $0 \le t_1 \le t_2$, find $E[T_1 \mid T_2 = t_2]$.

**Solution:**
- **Step 1: Integrate $t_1 \cdot f(t_1 \mid t_2)$ over $[0, t_2]$.**
  $$E[T_1 \mid T_2 = t_2] = \int_{0}^{t_2} t_1 \left( \frac{2 t_1}{t_2^2} \right) dt_1 = \frac{2}{t_2^2} \int_0^{t_2} t_1^2 dt_1$$
- **Step 2: WIP State.**
  $$E[T_1 \mid T_2 = t_2] = \frac{2}{t_2^2} \left[ \frac{t_1^3}{3} \right]_0^{t_2} = \frac{2}{t_2^2} \left( \frac{t_2^3}{3} \right) = \frac{2}{3} t_2$$
- **Step 3: Final Result.**
  $$E[T_1 \mid T_2 = t_2] = \frac{2}{3} t_2$$

---

### Exercise 8: Verification of Law of Iterated Expectations
**Problem:** Use $E[T_1 \mid T_2] = \frac{2}{3} T_2$ and $f_{T_2}(t_2) = 4 t_2^3$ ($0 \le t_2 \le 1$) to compute $E[T_1]$ via total expectation.

**Solution:**
- **Step 1: Compute $E[T_2]$.**
  $$E[T_2] = \int_0^1 t_2 (4 t_2^3) dt_2 = \int_0^1 4 t_2^4 dt_2 = \frac{4}{5}$$
- **Step 2: Apply Law of Total Expectation.**
  $$E[T_1] = E_{T_2}\left[ \frac{2}{3} T_2 \right] = \frac{2}{3} E[T_2] = \frac{2}{3} \times \frac{4}{5} = \frac{8}{15}$$
- **Step 3: Final Result.**
  $$E[T_1] = \frac{8}{15} \approx 0.5333$$

---

### Exercise 9: Conditional Expectation for Bivariate Normal Latency
**Problem:** Joint normal latencies have $\mu_1 = 100\text{ ms}, \mu_2 = 150\text{ ms}, \sigma_1 = 10\text{ ms}, \sigma_2 = 20\text{ ms}$, and $\rho = 0.8$. Calculate expected latency $E[T_1 \mid T_2 = 170\text{ ms}]$.

**Solution:**
- **Step 1: Apply linear regression expectation formula.**
  $$E[T_1 \mid T_2 = t_2] = \mu_1 + \rho \frac{\sigma_1}{\sigma_2} (t_2 - \mu_2)$$
- **Step 2: WIP State.**
  $$E[T_1 \mid T_2 = 170] = 100 + 0.8 \left(\frac{10}{20}\right) (170 - 150) = 100 + 0.8 (0.5) (20)$$
  $$E[T_1 \mid T_2 = 170] = 100 + 8 = 108\text{ ms}$$
- **Step 3: Final Result.**
  $$E[T_1 \mid T_2 = 170\text{ ms}] = 108\text{ ms}$$

---

### Exercise 10: R Code Verification of Covariance and Correlation
**Problem:** Write R code to generate correlated continuous latency samples ($T_1, T_2$) and verify empirical covariance and correlation.

**Solution:**
- **Step 1: R Script Setup.**
```r
library(MASS)
set.seed(123)

# Parameters
mu <- c(100, 150)
sigma1 <- 10
sigma2 <- 20
rho <- 0.8
cov_12 <- rho * sigma1 * sigma2 # 160

cov_matrix <- matrix(c(sigma1^2, cov_12, cov_12, sigma2^2), nrow = 2)

# Generate 500,000 bivariate normal samples
samples <- mvrnorm(n = 500000, mu = mu, Sigma = cov_matrix)
t1 <- samples[, 1]
t2 <- samples[, 2]

cat("Sample Covariance:", round(cov(t1, t2), 2), "\n")
cat("Sample Correlation:", round(cor(t1, t2), 4), "\n")
cat("Sample V(T1 + T2):", round(var(t1 + t2), 2), "\n")
```
- **Step 2: Execution Output.**
  `Sample Covariance: 160.03`
  `Sample Correlation: 0.8001`
  `Sample V(T1 + T2): 820.21`
