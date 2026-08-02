# Phase 5.4 (Time): Gamma, Weibull, and Erlang Distributions for Time Metrics

While the Exponential distribution models the waiting time until the *first* Poisson event ($k=1$), the Gamma and Erlang distributions generalize this to model the total waiting time elapsed until the $k$-th event. The Weibull distribution further extends reliability modeling by accommodating non-constant hazard rates (aging or burn-in effects over time).

---

## 1. The Gamma and Erlang Distributions for Waiting Times

### 1.1 Mathematical Definition
A continuous random variable $T$ representing cumulative waiting time follows a Gamma distribution with shape parameter $\alpha > 0$ and rate parameter $\beta > 0$ (denoted $T \sim \text{Gamma}(\alpha, \beta)$) if its PDF is:

$$\boxed{f_T(t) = \frac{\beta^\alpha}{\Gamma(\alpha)} t^{\alpha - 1} e^{-\beta t}, \quad t \ge 0}$$

Where $\Gamma(\alpha) = \int_0^\infty u^{\alpha - 1} e^{-u} du$ is the Gamma function. When $\alpha = k$ is a positive integer, the distribution is called the **Erlang distribution**, representing the sum of $k$ independent Exponential random variables each with rate $\beta$:

$$T = \sum_{i=1}^{k} X_i, \quad X_i \sim \text{Exp}(\beta) \implies T \sim \text{Erlang}(k, \beta)$$

For integer shape $\alpha = k$, $\Gamma(k) = (k - 1)!$.

### 1.2 Mean, Variance, and Mode
$$\boxed{E[T] = \frac{\alpha}{\beta}}, \quad \boxed{V(T) = \frac{\alpha}{\beta^2}}, \quad SD(T) = \frac{\sqrt{\alpha}}{\beta}$$

---

## 2. The Weibull Distribution for System Reliability and Aging

In real-world hardware, failure rates change over time due to infant mortality (burn-in) or wear-out. The Weibull distribution parameterized by shape parameter $k > 0$ (or $\alpha$) and scale parameter $\lambda > 0$ (or $\beta$) models time-to-failure $T$:

### 2.1 PDF and Reliability Function
$$\text{PDF: } f_T(t) = \frac{k}{\lambda} \left(\frac{t}{\lambda}\right)^{k-1} e^{-(t/\lambda)^k}, \quad t \ge 0$$

$$\text{Reliability / Survival: } S_T(t) = P(T > t) = \boxed{e^{-(t/\lambda)^k}}$$

* **$k < 1$:** Decreasing failure rate (infant mortality / defective components fail early).
* **$k = 1$:** Constant failure rate (reduces exactly to Exponential distribution $\text{Exp}(1/\lambda)$).
* **$k > 1$:** Increasing failure rate (wear-out / component aging over time).

---

## 3. Time-Specific Gotchas

### Gotcha 1: Rate Parameter $\beta$ vs Scale Parameter $\theta = 1/\beta$ in R and Formulas
Some textbooks and R functions define the Gamma distribution using the scale parameter $\theta$ ($f(t) = \frac{1}{\theta^\alpha \Gamma(\alpha)} t^{\alpha-1} e^{-t/\theta}$).
* With rate parameter $\beta$: $E[T] = \alpha / \beta$
* With scale parameter $\theta$: $E[T] = \alpha \cdot \theta$
Always confirm whether a formula or R function uses `rate` ($\beta$) or `scale` ($\theta = 1/\beta$). In R, `pgamma(t, shape = alpha, rate = beta)` vs `pgamma(t, shape = alpha, scale = 1/beta)`.

### Gotcha 2: Erlang Sum Property Requires Identical Rates
The rule $T = \sum_{i=1}^k X_i \sim \text{Gamma}(k, \beta)$ holds ONLY if all $k$ stage durations $X_i$ are **independent** AND share the **exact same rate parameter $\beta$**. If stage rates differ, the sum does not follow a simple Gamma distribution.

---

## 4. Solved Exercises (10 Examples)

### Exercise 1: Waiting Time for $k = 3$ API Requests (Erlang)
**Problem:** Requests arrive at a server according to a Poisson process with rate $\beta = 2$ requests per second. Let $T$ be the waiting time in seconds until the 3rd request arrives ($T \sim \text{Gamma}(\alpha=3, \beta=2)$). Find the mean and variance of $T$.

**Solution:**
- **Step 1: Compute Mean and Variance.**
  $$E[T] = \frac{\alpha}{\beta} = \frac{3}{2} = 1.5\text{ seconds}$$
  $$V(T) = \frac{\alpha}{\beta^2} = \frac{3}{2^2} = \frac{3}{4} = 0.75\text{ seconds}^2$$
- **Step 2: WIP State.**
  $$SD(T) = \sqrt{0.75} \approx 0.866\text{ seconds}$$
- **Step 3: Final Result.**
  $E[T] = 1.5\text{ s}$, $V(T) = 0.75\text{ s}^2$.

---

### Exercise 2: CDF of Erlang Distribution via Poisson Cumulative Sum
**Problem:** For $T \sim \text{Gamma}(k=2, \beta=3\text{ min}^{-1})$, find $P(T \le 1\text{ min})$ using the equivalence $P(T_{k} \le t) = P(N_t \ge k)$ where $N_t \sim \text{Poisson}(\beta t)$.

**Solution:**
- **Step 1: Calculate Poisson parameter $\lambda_t$.**
  $$\lambda_t = \beta \cdot t = 3 \times 1 = 3$$
- **Step 2: Set up complementary Poisson sum ($N_t \ge 2$).**
  $$P(N_1 \ge 2) = 1 - P(N_1 = 0) - P(N_1 = 1)$$
  $$P(N_1 = 0) = \frac{3^0 e^{-3}}{0!} = e^{-3} \approx 0.04979$$
  $$P(N_1 = 1) = \frac{3^1 e^{-3}}{1!} = 3 e^{-3} \approx 0.14936$$
- **Step 3: WIP State and Final Calculation.**
  $$P(N_1 \ge 2) = 1 - (0.04979 + 0.14936) = 1 - 0.19915 = 0.80085$$
  $$P(T \le 1\text{ min}) \approx 0.8009 \text{ (80.09\%)}$$

---

### Exercise 3: Weibull Survival Probability with Wear-Out ($k > 1$)
**Problem:** Industrial pump time-to-failure $T$ follows a Weibull distribution with shape $k = 2$ and scale $\lambda = 1000\text{ hours}$. Find the probability that a pump operates without failure beyond $1500\text{ hours}$.

**Solution:**
- **Step 1: Apply Weibull reliability function.**
  $$P(T > 1500) = e^{-(t/\lambda)^k} = e^{-(1500/1000)^2}$$
- **Step 2: WIP State.**
  $$\left(\frac{1500}{1000}\right)^2 = (1.5)^2 = 2.25$$
  $$P(T > 1500) = e^{-2.25} \approx 0.1054$$
- **Step 3: Final Result.**
  $$P(T > 1500) = 0.1054 \text{ (10.54\%)}$$

---

### Exercise 4: Weibull Component Failure with Infant Mortality ($k = 0.5$)
**Problem:** Microchip time-to-failure $T$ follows a Weibull distribution with shape $k = 0.5$ and scale $\lambda = 400\text{ hours}$. Find the probability of chip failure within the first $100\text{ hours}$.

**Solution:**
- **Step 1: Apply Weibull CDF $F_T(t) = 1 - e^{-(t/\lambda)^k}$.**
  $$F_T(100) = 1 - e^{-(100/400)^{0.5}} = 1 - e^{-(0.25)^{0.5}}$$
- **Step 2: WIP State.**
  $$\sqrt{0.25} = 0.5, \quad e^{-0.5} \approx 0.60653$$
  $$F_T(100) = 1 - 0.60653 = ?$$
- **Step 3: Final Result.**
  $$P(T \le 100) = 0.3935 \text{ (39.35\%)}$$

---

### Exercise 5: Sum of Independent Exponential Stage Times
**Problem:** A multi-stage pipeline consists of 4 sequential processing steps. Each step execution time is independently distributed as $X_i \sim \text{Exp}(\beta = 0.5\text{ ms}^{-1})$. Find the distribution and expected total execution duration $T = \sum_{i=1}^4 X_i$.

**Solution:**
- **Step 1: Identify distribution of the sum.**
  Since all 4 steps are independent and have rate $\beta = 0.5$,
  $$T \sim \text{Gamma}(\alpha = 4, \beta = 0.5)$$
- **Step 2: WIP State.**
  $$E[T] = \frac{\alpha}{\beta} = \frac{4}{0.5} = 8\text{ ms}$$
  $$V(T) = \frac{\alpha}{\beta^2} = \frac{4}{0.25} = 16\text{ ms}^2$$
- **Step 3: Final Result.**
  Total time $T \sim \text{Gamma}(4, 0.5)$ with mean $8\text{ ms}$ and standard deviation $4\text{ ms}$.

---

### Exercise 6: Connection Between Gamma and Chi-Square Distribution
**Problem:** Prove that if $T \sim \text{Gamma}(\alpha = v/2, \beta = 1/2)$, then $T$ is equivalent to a Chi-Square distribution with $v$ degrees of freedom ($\chi_v^2$). Calculate the mean time for $\chi_{10}^2$.

**Solution:**
- **Step 1: Compare Gamma and Chi-Square PDFs.**
  Gamma PDF: $f(t) = \frac{(1/2)^{v/2}}{\Gamma(v/2)} t^{v/2 - 1} e^{-t/2}$, which matches $\chi_v^2$ PDF identically.
- **Step 2: WIP State.**
  For $\chi_{10}^2$: $\alpha = 10/2 = 5$, $\beta = 1/2 = 0.5$.
  $$E[T] = \frac{\alpha}{\beta} = \frac{5}{0.5} = 10$$
- **Step 3: Final Result.**
  Mean execution time $E[T] = 10$ time units ($E[\chi_v^2] = v$).

---

### Exercise 7: Determining Parameters from Sample Mean and Variance
**Problem:** Sensor calibration time $T$ is modeled as Gamma$(\alpha, \beta)$. Empirical testing yields sample mean $\bar{t} = 12\text{ seconds}$ and sample variance $s^2 = 36\text{ seconds}^2$. Estimate $\alpha$ and $\beta$ via method of moments.

**Solution:**
- **Step 1: Set up moment equations.**
  $$\frac{\alpha}{\beta} = 12, \quad \frac{\alpha}{\beta^2} = 36$$
- **Step 2: Solve system of equations.**
  Divide mean by variance:
  $$\frac{\alpha/\beta}{\alpha/\beta^2} = \beta = \frac{12}{36} = \frac{1}{3} \approx 0.3333\text{ s}^{-1}$$
  Substitute $\beta$ into mean equation:
  $$\alpha = 12 \cdot \beta = 12 \cdot \frac{1}{3} = 4$$
- **Step 3: Final Result.**
  Estimated parameters: $\alpha = 4$, $\beta = 1/3\text{ s}^{-1}$ (or scale $\theta = 3\text{ s}$).

---

### Exercise 8: Mode of the Gamma Waiting Time Distribution
**Problem:** For Gamma$(\alpha = 4, \beta = 0.5\text{ ms}^{-1})$, calculate the mode (the most likely execution time peak).

**Solution:**
- **Step 1: Recall mode formula for Gamma distribution ($\alpha > 1$).**
  $$\text{Mode} = \frac{\alpha - 1}{\beta}$$
- **Step 2: WIP State.**
  $$\text{Mode} = \frac{4 - 1}{0.5} = \frac{3}{0.5} = ?$$
- **Step 3: Final Result.**
  $$\text{Mode} = 6\text{ ms}$$
  (Compare with mean $E[T] = 4 / 0.5 = 8\text{ ms}$; right-skewness pulls mean above mode).

---

### Exercise 9: Weibull Hazard Rate Evaluation
**Problem:** The hazard rate (instantaneous failure rate) of a Weibull time RV is $h(t) = \frac{f(t)}{S(t)} = \frac{k}{\lambda} \left(\frac{t}{\lambda}\right)^{k-1}$. Calculate $h(100)$ for a system with $k = 2$ and $\lambda = 500\text{ hours}$.

**Solution:**
- **Step 1: Substitute parameters into $h(t)$.**
  $$h(100) = \frac{2}{500} \left(\frac{100}{500}\right)^{2-1} = 0.004 \times (0.2)^1$$
- **Step 2: WIP State.**
  $$h(100) = 0.004 \times 0.2 = 0.0008\text{ failures/hour}$$
- **Step 3: Final Result.**
  Instantaneous failure rate at $t = 100\text{ h}$ is $0.0008\text{ failures/hour}$.

---

### Exercise 10: R Code Verification for Gamma and Weibull
**Problem:** Demonstrate how to calculate cumulative probabilities and survival metrics for Gamma and Weibull distributions in R.

**Solution:**
- **Step 1: R Script Setup.**
```r
# Gamma(alpha = 3, beta = 2) waiting time until 3rd event <= 1.5 seconds
p_gamma <- pgamma(q = 1.5, shape = 3, rate = 2)
cat("Gamma P(T <= 1.5 s):", round(p_gamma, 4), "\n")

# Weibull(shape = 2, scale = 1000) survival beyond 1500 hours
p_weibull_surv <- pweibull(q = 1500, shape = 2, scale = 1000, lower.tail = FALSE)
cat("Weibull Survival P(T > 1500 h):", round(p_weibull_surv, 4), "\n")
```
- **Step 2: Execution Output.**
  `Gamma P(T <= 1.5 s): 0.5768`
  `Weibull Survival P(T > 1500 h): 0.1054`
