# Phase 5: Continuous Random Variables & Distributions

## Table of Contents
1. [Normal Distribution](#1-normal-distribution)
2. [The Empirical Rule](#2-the-empirical-rule)
3. [Continuous Uniform and Exponential Distributions](#3-continuous-uniform-and-exponential-distributions)
4. [Gamma, Weibull, and Erlang Distributions](#4-gamma-weibull-and-erlang-distributions)
5. [Transformations of Random Variables](#5-transformations-of-random-variables)
6. [Time-Specific Gotchas](#6-time-specific-gotchas)
7. [Solved Exercises](#7-solved-exercises)
8. [Phase Summary](#phase-summary)

---

## 1. Normal Distribution

The Normal (Gaussian) Distribution $N(\mu, \sigma^2)$ is characterized by a symmetric, bell-shaped probability density function (PDF).

### Probability Density Function (PDF)
$$f_T(t) = \frac{1}{\sigma_T \sqrt{2\pi}} \exp\left( -\frac{(t - \mu_T)^2}{2\sigma_T^2} \right), \quad -\infty < t < \infty$$

### Standard Normal Transformation
We standardise any normal random variable to $Z \sim N(0, 1)$ using the $Z$-score:
$$Z = \frac{T - \mu_T}{\sigma_T}$$
Then $P(T \le t) = \Phi(Z)$.

---

## 2. The Empirical Rule

For any symmetric, bell-shaped distribution (like the Normal distribution):
1. **68% Rule:** $\sim 68.27\%$ of values fall within $\mu_T \pm 1\sigma_T$.
2. **95% Rule:** $\sim 95.45\%$ of values fall within $\mu_T \pm 2\sigma_T$.
3. **99.7% Rule:** $\sim 99.73\%$ of values fall within $\mu_T \pm 3\sigma_T$.

---

## 3. Continuous Uniform and Exponential Distributions

### Continuous Uniform Distribution $U(a, b)$
Models equal probability over an interval.
*   **PDF:** $f_T(t) = \frac{1}{b - a}$ for $a \le t \le b$
*   **Mean:** $E[T] = \frac{a + b}{2}$, **Variance:** $V(T) = \frac{(b - a)^2}{12}$

### Exponential Distribution $Exp(\lambda)$
Models time between Poisson events. It is the **only memoryless** continuous distribution.
*   **PDF:** $f_T(t) = \lambda e^{-\lambda t}$ for $t \ge 0$
*   **Reliability / Survival:** $P(T > t) = e^{-\lambda t}$
*   **Mean:** $E[T] = 1/\lambda$, **Variance:** $V(T) = 1/\lambda^2$
*   **Memoryless Property:** $P(T > s + t \mid T > s) = P(T > t) = e^{-\lambda t}$

---

## 4. Gamma, Weibull, and Erlang Distributions

### Gamma Distribution $Gamma(\alpha, \beta)$
Models the time until $\alpha$ events occur in a Poisson process. If $\alpha = k$ (integer), it's the **Erlang** distribution.
*   **PDF:** $f_T(t) = \frac{\beta^\alpha}{\Gamma(\alpha)} t^{\alpha - 1} e^{-\beta t}$
*   **Mean:** $E[T] = \frac{\alpha}{\beta}$, **Variance:** $V(T) = \frac{\alpha}{\beta^2}$

### Weibull Distribution
Models time-to-failure with changing hazard rates.
*   **Reliability / Survival:** $S_T(t) = P(T > t) = e^{-(t/\lambda)^k}$
*   **$k < 1$**: Infant mortality. **$k = 1$**: Constant rate (Exponential). **$k > 1$**: Wear-out.

---

## 5. Transformations of Random Variables

For a continuous RV $T$ and transformation $Y = g(T)$:

### Linear Transformation ($Y = aT + b$)
*   $E[Y] = aE[T] + b$, $V(Y) = a^2 V(T)$
*   $f_Y(y) = \frac{1}{|a|} f_T\left(\frac{y-b}{a}\right)$

### Monotonic Non-Linear Transformation
Using the Jacobian derivative:
$$f_Y(y) = f_T\left( g^{-1}(y) \right) \cdot \left| \frac{d}{dy} g^{-1}(y) \right|$$

---

## 6. Time-Specific Gotchas

1. **Negative Time in Normal Models:** The Normal domain is $(-\infty, \infty)$. If $\mu_T < 3\sigma_T$, the model predicts negative time. Use Log-Normal or truncated normal in high-precision cases.
2. **Scaling Variance:** Converting seconds to ms multiplies values by 1000, but **variance** by $1{,}000{,}000$.
3. **Throughput Fallacy:** Average throughput $E[1/T]$ is strictly greater than $1/E[T]$ due to Jensen's Inequality.
4. **Memoryless Assumption:** Only the Exponential distribution is memoryless. Gamma and Weibull (with $k \ne 1$) are memoryful.
5. **Erlang Sum Property:** Adding Exponentials gives an Erlang ONLY if all stages have the EXACT same rate $\beta$.

---

## 7. Solved Exercises

#### Exercise 1: Finding the 99th Percentile SLA Benchmark ($p_{99}$)
**Problem:** Microservice processing time $T \sim N(50, 100)$ in ms ($\mu_T = 50$, $\sigma_T = 10$). Find $t_{99}$.
**Solution:**
From z-tables, $\Phi(2.326) = 0.99$.
$$t_{99} = \mu_T + z_{0.99} \cdot \sigma_T = 50 + (2.326)(10) = 50 + 23.26 = 73.26\text{ ms}$$

#### Exercise 2: Probability of Timeout Failure ($T > t_{\text{timeout}}$)
**Problem:** Network ping $T \sim N(45, 25)$ in ms. Times out if $T > 60\text{ ms}$. Find timeout prob.
**Solution:**
$z = (60 - 45) / 5 = 3.00$.
$$P(T > 60) = 1 - \Phi(3.00) = 1 - 0.99865 = 0.00135 \text{ (0.135\%)}$$

#### Exercise 3: Sum of Two Independent Normal Delay Stages
**Problem:** Stage 1 $T_1 \sim N(30, 9)$ ms and Stage 2 $T_2 \sim N(50, 16)$ ms. Find $P(T_1 + T_2 \le 90)$.
**Solution:**
$\mu_{tot} = 30 + 50 = 80$, $\sigma_{tot}^2 = 9 + 16 = 25 \implies \sigma_{tot} = 5$.
$z = (90 - 80) / 5 = 2.00$.
$P \le 90 = \Phi(2.00) = 0.9772 \text{ (97.72\%)}$.

#### Exercise 4: Number of Outlier Requests out of 10,000 (Empirical Rule)
**Problem:** Out of $10{,}000$ requests with $T \sim N(2, 0.09)$ (in s), how many fall outside $[1.1, 2.9]$?
**Solution:**
$1.1$ and $2.9$ are $\mu_T \pm 3\sigma_T$.
Outside area $= 100\% - 99.73\% = 0.27\% = 0.0027$.
$10{,}000 \times 0.0027 = 27 \text{ requests}$.

#### Exercise 5: Asymmetric Duration Window
**Problem:** Batch processing $T \sim N(12, 4)$ in hours. Estimate $P(10 \le T \le 16)$.
**Solution:**
$10$ is $\mu_T - 1\sigma_T$. $16$ is $\mu_T + 2\sigma_T$.
Left half (0 to -1) $= 34.135\%$. Right half (0 to 2) $= 47.725\%$.
Total $= 81.86\%$.

#### Exercise 6: Uniform Random Backoff Time
**Problem:** $T \sim U(10, 50)$ ms. Find $P(T > 35)$.
**Solution:**
$$P(T > 35) = \frac{50 - 35}{50 - 10} = \frac{15}{40} = 0.375 \text{ (37.5\%)}$$

#### Exercise 7: Exponential Component Survival
**Problem:** Hard drive $\lambda = 0.0001\text{ h}^{-1}$. Prob it survives beyond $5{,}000$ hours?
**Solution:**
$$P(T > 5000) = e^{-(0.0001)(5000)} = e^{-0.5} \approx 0.6065$$

#### Exercise 8: Minimum of Independent Exponential Durations
**Problem:** Components fail at $T_1 \sim Exp(0.02)$, $T_2 \sim Exp(0.03)$. System fails when FIRST component fails. Expected time to failure?
**Solution:**
$T_{min} \sim Exp(0.02 + 0.03) = Exp(0.05)$.
$E[T_{min}] = 1 / 0.05 = 20\text{ hours}$.

#### Exercise 9: Waiting Time for $k = 3$ API Requests (Erlang)
**Problem:** Poisson requests at $\beta = 2\text{ s}^{-1}$. Waiting time $T$ until 3rd request. Find mean and variance.
**Solution:**
$T \sim Gamma(\alpha=3, \beta=2)$.
$E[T] = 3/2 = 1.5\text{ s}$. $V(T) = 3/2^2 = 0.75\text{ s}^2$.

#### Exercise 10: Weibull Survival Probability with Wear-Out
**Problem:** Pump failure $T \sim Weibull(k=2, \lambda=1000\text{ h})$. Prob of survival beyond 1500 hours.
**Solution:**
$$P(T > 1500) = e^{-(1500/1000)^2} = e^{-2.25} \approx 0.1054$$

#### Exercise 11: Sum of Independent Exponential Stage Times
**Problem:** 4 stages, each $X_i \sim Exp(0.5\text{ ms}^{-1})$. Distribution of total $T$?
**Solution:**
Since they share the same rate, sum is Erlang/Gamma: $T \sim Gamma(4, 0.5)$.

#### Exercise 12: Reciprocal Transformation ($Y = 1/T$) for Throughput
**Problem:** Time $T \sim U(0.5, 2.0)$. Find PDF of throughput $Y = 1/T$.
**Solution:**
$y = 1/t \implies t = 1/y$. $|dt/dy| = 1/y^2$.
$f_T(t) = 1/(2.0 - 0.5) = 2/3$.
$$f_Y(y) = \frac{2}{3} \cdot \frac{1}{y^2} = \frac{2}{3y^2} \quad \text{for } 0.5 \le y \le 2.0$$

#### Exercise 13: Log-Normal Mean Calculation
**Problem:** $Y = \ln T \sim N(3, 0.25)$. Find $E[T]$.
**Solution:**
$E[T] = \exp(\mu + \sigma^2/2) = \exp(3 + 0.125) = e^{3.125} \approx 22.76$.

#### Exercise 14: Non-Monotonic Transformation Symmetry ($Y = T^2$)
**Problem:** Latency error $T \sim N(0, \sigma^2)$. PDF of $Y = T^2$?
**Solution:**
$F_Y(y) = P(-\sqrt{y} \le T \le \sqrt{y}) = F_T(\sqrt{y}) - F_T(-\sqrt{y})$.
$f_Y(y) = f_T(\sqrt{y}) \frac{1}{2\sqrt{y}} + f_T(-\sqrt{y}) \frac{1}{2\sqrt{y}} = \frac{1}{\sqrt{y}} f_T(\sqrt{y})$.
$$f_Y(y) = \frac{1}{\sigma \sqrt{2\pi y}} e^{-y / 2\sigma^2} \quad (y > 0)$$

#### Exercise 15: R Code Verification of Latency Quantiles
**Problem:** Compute $P(T \le 115)$ and $p_{95}$ for $T \sim N(100, 64)$.
**Solution:**
```r
mean_t <- 100; sd_t <- 8
p_115 <- pnorm(q = 115, mean = mean_t, sd = sd_t)
p95_limit <- qnorm(p = 0.95, mean = mean_t, sd = sd_t)
```

#### Exercise 16: R Code Verification for Exponential and Uniform
**Problem:** Calc prob for $U(10, 50)$ and $Exp(0.0001)$.
**Solution:**
```r
p_unif <- punif(q = 35, min = 10, max = 50, lower.tail = FALSE)
p_exp_fail <- pexp(q = 2000, rate = 0.0001)
p_exp_surv <- pexp(q = 5000, rate = 0.0001, lower.tail = FALSE)
```

---

## Phase Summary
Phase 5 introduces continuous probability distributions and the critical methodology of random variable transformations. The Normal distribution $N(\mu, \sigma^2)$ is foundational, accompanied by the Empirical Rule (68-95-99.7) for quick tail probability estimates. In the time domain, Uniform $U(a,b)$ models random jitter/backoff, while the Exponential distribution uniquely offers memoryless inter-arrival times. To model complex cumulative delays or changing hazard rates (aging), the Gamma, Erlang, and Weibull distributions are utilized. Transformations, evaluated via the Jacobian derivative $|g'(t)|^{-1}$, allow translation between latency and throughput ($1/T$) or derivation of skewed Log-Normal metrics ($e^Y$). Critical real-world gotchas include the expectation reciprocal fallacy ($E[1/T] > 1/E[T]$) and tracking rate vs. scale parameterizations in Gamma implementations.
