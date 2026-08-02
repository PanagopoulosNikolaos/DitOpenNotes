# Phase 5: Continuous Random Variables & Distributions

## Table of Contents
- [Section 5.1: Normal Distribution](#section-51-normal-distribution)
- [Section 5.2: The Empirical Rule](#section-52-the-empirical-rule)
- [Section 5.3: Continuous Uniform Distribution](#section-53-continuous-uniform-distribution)
- [Section 5.4: Exponential Distribution](#section-54-exponential-distribution)
- [Section 5.5: Gamma, Erlang, and Weibull Distributions](#section-55-gamma-erlang-and-weibull-distributions)
- [Section 5.6: Transformations of Continuous Random Variables](#section-56-transformations-of-continuous-random-variables)
- [Exam Preparation Guide](#exam-preparation-guide)
- [Phase Summary](#phase-summary)

---

## Section 5.1: Normal Distribution

### Core Theory & Definitions

The **Normal (Gaussian) Distribution** is the most important continuous probability distribution in statistics. A continuous random variable $X$ follows a Normal distribution with parameters $\mu$ (mean) and $\sigma^2$ (variance), written $X \sim N(\mu, \sigma^2)$, if its probability density function (PDF) has the symmetric, bell-shaped form shown below.

The Normal distribution is parameterized by:
- $\mu \in (-\infty, +\infty)$: the **mean** (also the median and mode for a symmetric distribution)
- $\sigma > 0$: the **standard deviation**; $\sigma^2$ is the variance

The distribution is symmetric around $\mu$, meaning $P(X \le \mu - c) = P(X \ge \mu + c)$ for any $c > 0$.

**Standard Normal Distribution:** The special case $Z \sim N(0, 1)$ (mean 0, variance 1) is called the **standard normal**. Any normal random variable can be converted to standard normal via the Z-score transformation. The CDF of $Z$ is denoted $\Phi(z) = P(Z \le z)$ and is tabulated in Z-tables.

**Support:** $x \in (-\infty, +\infty)$. The Normal domain is the entire real line, which creates practical issues when modeling strictly positive quantities (e.g., durations, weights). For such applications, truncation or log-normal models are preferred when $\mu < 3\sigma$.

> **Practical / Time-Domain Note:**
> Response times, latencies, and system delays are strictly positive quantities. A Normal model $T \sim N(\mu_T, \sigma_T^2)$ assigns a small but nonzero probability to $T < 0$, which is physically impossible. This is acceptable as a working approximation when $\mu_T \gg \sigma_T$ (equivalently, when $\mu_T > 3\sigma_T$). When the coefficient of variation $\sigma_T / \mu_T$ is large (greater than roughly 0.3), prefer a Log-Normal, Gamma, or Exponential model for positive-valued latency data.

### Mathematical Formulas & Derivations

**Probability Density Function (PDF):**
$$f(x) = \frac{1}{\sigma \sqrt{2\pi}} \exp\left( -\frac{(x - \mu)^2}{2\sigma^2} \right), \quad x \in (-\infty, +\infty)$$

**Cumulative Distribution Function (CDF):**
$$F(x) = P(X \le x) = \Phi\left(\frac{x - \mu}{\sigma}\right)$$

where $\Phi(\cdot)$ is the standard normal CDF, tabulated in Z-tables.

**Z-Score (Standardization):**
$$Z = \frac{X - \mu}{\sigma} \sim N(0, 1)$$

This transformation converts any normal probability to a standard normal probability, enabling use of the Z-table.

**Key Probability Calculations:**
$$P(X \le x) = \Phi\left(\frac{x - \mu}{\sigma}\right)$$
$$P(X > x) = 1 - \Phi\left(\frac{x - \mu}{\sigma}\right)$$
$$P(a \le X \le b) = \Phi\left(\frac{b - \mu}{\sigma}\right) - \Phi\left(\frac{a - \mu}{\sigma}\right)$$

**Symmetry of the Standard Normal:**
$$\Phi(-z) = 1 - \Phi(z)$$

This is used to convert negative Z-scores into positive ones available in standard tables.

**Quantile / Inverse CDF (Percentile):**
$$x_p = \mu + z_p \cdot \sigma$$

where $z_p = \Phi^{-1}(p)$ is the $p$-th quantile of the standard normal (e.g., $z_{0.95} = 1.645$, $z_{0.99} = 2.326$).

**Mean and Variance:**
$$E[X] = \mu, \quad V(X) = \sigma^2$$

**Sum of Independent Normals:** If $X_1 \sim N(\mu_1, \sigma_1^2)$ and $X_2 \sim N(\mu_2, \sigma_2^2)$ are independent, then:
$$X_1 + X_2 \sim N(\mu_1 + \mu_2,\ \sigma_1^2 + \sigma_2^2)$$

**Time-Domain Adapted Formula (Latency Percentile SLA):**

When $T \sim N(\mu_T, \sigma_T^2)$ models a latency (in ms, s, etc.), the $p$-th percentile SLA threshold is:
$$t_p = \mu_T + z_p \cdot \sigma_T \quad [\text{same time unit as } \mu_T]$$

**Unit Conversion via the $c^2$ Rule:**

If time measurements are converted from one unit to another by multiplying by $c$ (e.g., seconds to milliseconds: $c = 1000$), then:
$$\mu_{new} = c \cdot \mu_{old}, \quad \sigma_{new} = c \cdot \sigma_{old}, \quad \sigma^2_{new} = c^2 \cdot \sigma^2_{old}$$

The Z-score is unitless and unaffected by the conversion.

> **Practical / Time-Domain Note:**
> The $c^2$ rule is a frequent exam trap. If $T \sim N(50, 100)$ ms and you convert to seconds ($c = 1/1000$), the new distribution is $T \sim N(0.05, 0.0001)$ s. The variance scales by $c^2 = 10^{-6}$, NOT by $c$. Forgetting this is one of the most common unit-conversion mistakes.

**Solving for Unknown Parameters from Percentiles:**

Given two percentile conditions (common in hard exam problems):
- $P(X \le a) = p_1$ implies $\frac{a - \mu}{\sigma} = z_{p_1}$
- $P(X \le b) = p_2$ implies $\frac{b - \mu}{\sigma} = z_{p_2}$

This gives a system of two linear equations in $\mu$ and $\sigma$:
$$a = \mu + z_{p_1} \cdot \sigma$$
$$b = \mu + z_{p_2} \cdot \sigma$$

Solve by subtraction to find $\sigma$, then substitute to find $\mu$.

### Worked Exercises

#### Exercise 1: Normal Tail Probability for Apple Weight
**Problem:** The weight of apples from a specific variety follows a Normal distribution with $\mu = 150$ g and $\sigma = 15$ g. Find:
a) $P(X < 165)$
b) $P(135 \le X \le 165)$

Given: $\Phi(1) = 0.8413$.

**Solution:**

**a) Standardize $x = 165$:
$$Z = \frac{165 - 150}{15} = \frac{15}{15} = 1.00$$
$$P(X < 165) = \Phi(1.00) = \boxed{0.8413}$$

**b) Standardize both bounds:
$$z_1 = \frac{135 - 150}{15} = \frac{-15}{15} = -1.00, \quad z_2 = \frac{165 - 150}{15} = 1.00$$
Use symmetry $\Phi(-1) = 1 - \Phi(1) = 1 - 0.8413 = 0.1587$:
$$P(135 \le X \le 165) = \Phi(1.00) - \Phi(-1.00) = 0.8413 - 0.1587 = \boxed{0.6826}$$

#### Exercise 2: Solving for Unknown Normal Parameters (Hard Exam Type)
**Problem:** A machine fills bottles with a liquid. The volume $X$ follows a Normal distribution with unknown $\mu$ and $\sigma$. It is known that $P(X > 334.8) = 0.10$ and $P(X < 318.5) = 0.05$. Find $\mu$ and $\sigma$.

Given: $\Phi(1.282) = 0.90$, $\Phi(1.645) = 0.95$.

**Solution:**

**Step 1:** Translate the two conditions into Z-score equations.

$P(X > 334.8) = 0.10 \implies P(X \le 334.8) = 0.90 \implies \frac{334.8 - \mu}{\sigma} = 1.282$

$P(X < 318.5) = 0.05 \implies \frac{318.5 - \mu}{\sigma} = -1.645$ (using symmetry: $\Phi^{-1}(0.05) = -1.645$)

**Step 2:** Write the system of equations:
$$334.8 = \mu + 1.282\sigma \quad (1)$$
$$318.5 = \mu - 1.645\sigma \quad (2)$$

**Step 3:** Subtract equation (2) from equation (1):
$$334.8 - 318.5 = 1.282\sigma - (-1.645\sigma) = (1.282 + 1.645)\sigma$$
$$16.3 = 2.927\sigma \implies \sigma = \frac{16.3}{2.927} \approx \mathbf{5.57 \text{ ml}}$$

**Step 4:** Substitute into equation (1):
$$\mu = 334.8 - 1.282 \times 5.57 = 334.8 - 7.14 \approx \boxed{\mu \approx 327.66 \text{ ml}}$$

#### Exercise 3: Sum of Independent Normal Delays (Time-Domain)
**Problem:** A web request passes through two independent processing stages. Stage 1 latency: $T_1 \sim N(30, 9)$ ms. Stage 2 latency: $T_2 \sim N(50, 16)$ ms. Find $P(T_1 + T_2 \le 90)$.

**Solution:**

**Step 1:** Total latency distribution (sum of independent normals):
$$T_{total} = T_1 + T_2 \sim N(\mu_{total}, \sigma^2_{total})$$
$$\mu_{total} = 30 + 50 = 80 \text{ ms}, \quad \sigma^2_{total} = 9 + 16 = 25 \implies \sigma_{total} = 5 \text{ ms}$$

**Step 2:** Standardize:
$$Z = \frac{90 - 80}{5} = \frac{10}{5} = 2.00$$

**Step 3:** Look up:
$$P(T_{total} \le 90) = \Phi(2.00) = \boxed{0.9772 \approx 97.72\%}$$

#### Exercise 4: Finding the 99th Percentile SLA Threshold (Time-Domain)
**Problem:** Microservice processing time $T \sim N(50, 100)$ ms ($\mu_T = 50$ ms, $\sigma_T = 10$ ms). Find the SLA threshold $t_{99}$ such that 99% of requests are served within that time.

**Solution:**

From Z-tables: $z_{0.99} = 2.326$.

$$t_{99} = \mu_T + z_{0.99} \cdot \sigma_T = 50 + (2.326)(10) = 50 + 23.26 = \boxed{73.26 \text{ ms}}$$

#### Exercise 5: Probability of Timeout Failure (Time-Domain)
**Problem:** Network ping latency $T \sim N(45, 25)$ ms ($\mu_T = 45$, $\sigma_T = 5$). A timeout occurs if $T > 60$ ms. Find the probability of a timeout.

**Solution:**

$$Z = \frac{60 - 45}{5} = \frac{15}{5} = 3.00$$
$$P(T > 60) = 1 - \Phi(3.00) = 1 - 0.99865 = \boxed{0.00135 \approx 0.135\%}$$

### R Implementation

```r
# Normal distribution probability: P(X <= x)
pnorm(q = 165, mean = 150, sd = 15)

# P(X > x) using lower.tail = FALSE
pnorm(q = 60, mean = 45, sd = 5, lower.tail = FALSE)

# Interval probability: P(135 <= X <= 165)
pnorm(q = 165, mean = 150, sd = 15) - pnorm(q = 135, mean = 150, sd = 15)

# Inverse CDF (quantile / percentile): find x_p such that P(X <= x_p) = 0.99
qnorm(p = 0.99, mean = 50, sd = 10)

# Standard normal CDF lookup
pnorm(q = 2.326)           # Phi(2.326) approximately 0.99

# Compute PDF value at x
dnorm(x = 150, mean = 150, sd = 15)

# WARNING: pnorm() takes sd (standard deviation), NOT variance.
# If X ~ N(50, 100) where 100 is variance, sigma = sqrt(100) = 10.
pnorm(q = 73.26, mean = 50, sd = sqrt(100))
```

---

## Section 5.2: The Empirical Rule

### Core Theory & Definitions

The **Empirical Rule** (also called the 68-95-99.7 Rule) provides a quick approximation for tail probabilities of any approximately symmetric, bell-shaped distribution, including the Normal distribution. It states that nearly all observations fall within three standard deviations of the mean.

The rule is useful for quick mental estimation without Z-tables, and it appears frequently on exams as a shortcut tool.

> **Practical / Time-Domain Note:**
> The Empirical Rule is a rapid diagnostic for SLA compliance. If a system's mean latency is $\mu_T$ ms with standard deviation $\sigma_T$ ms, then roughly 99.7% of requests complete within $\mu_T \pm 3\sigma_T$ ms. Any request exceeding $\mu_T + 3\sigma_T$ is a statistical outlier. This is the basis of "3-sigma" quality control in manufacturing and performance engineering.

### Mathematical Formulas & Derivations

For $X \sim N(\mu, \sigma^2)$ (or any approximately symmetric distribution):

**68% Rule:**
$$P(\mu - \sigma \le X \le \mu + \sigma) \approx 0.6827$$

**95% Rule:**
$$P(\mu - 2\sigma \le X \le \mu + 2\sigma) \approx 0.9545$$

**99.7% Rule:**
$$P(\mu - 3\sigma \le X \le \mu + 3\sigma) \approx 0.9973$$

**Derived tail probabilities (symmetric about $\mu$):**

$$P(X < \mu - \sigma) \approx \frac{1 - 0.6827}{2} = 0.1587 \quad \text{(left 16th percentile)}$$

$$P(X > \mu + 2\sigma) \approx \frac{1 - 0.9545}{2} = 0.0228 \quad \text{(right 2.28th percentile)}$$

**Asymmetric window (using half-rule):**

For $P(\mu - k_1 \sigma \le X \le \mu + k_2 \sigma)$ with $k_1 \ne k_2$, combine half-rule contributions:
- Area from $\mu - \sigma$ to $\mu$: $68.27\% / 2 = 34.135\%$
- Area from $\mu$ to $\mu + 2\sigma$: $95.45\% / 2 = 47.725\%$
- Total: $34.135\% + 47.725\% = 81.86\%$

> **Practical / Time-Domain Note:**
> The Empirical Rule applies only when the underlying distribution is approximately symmetric and bell-shaped. Do NOT apply it to Exponential, Gamma, or Weibull distributions, which are right-skewed. Applying the 68% rule to skewed latency distributions (e.g., Gamma-distributed queueing delays) will significantly underestimate the probability of tail events.

### Worked Exercises

#### Exercise 6: Number of Outlier Requests using the Empirical Rule (Time-Domain)
**Problem:** Out of $10{,}000$ HTTP requests with processing time $T \sim N(2, 0.09)$ seconds ($\mu_T = 2$ s, $\sigma_T = 0.3$ s), how many requests fall outside the interval $[1.1, 2.9]$ seconds?

**Solution:**

**Step 1:** Identify the interval in terms of standard deviations from the mean:
$$1.1 = 2 - 3(0.3) = \mu_T - 3\sigma_T, \quad 2.9 = 2 + 3(0.3) = \mu_T + 3\sigma_T$$

**Step 2:** Apply the 99.7% rule:
$$P(1.1 \le T \le 2.9) \approx 0.9973$$

**Step 3:** Compute the outside probability:
$$P(T < 1.1 \text{ or } T > 2.9) = 1 - 0.9973 = 0.0027$$

**Step 4:** Expected count:
$$10{,}000 \times 0.0027 = \boxed{27 \text{ requests}}$$

#### Exercise 7: Asymmetric Interval using the Empirical Half-Rule
**Problem:** Batch processing time $T \sim N(12, 4)$ hours ($\sigma_T = 2$). Estimate $P(10 \le T \le 16)$.

**Solution:**

**Step 1:** Express the bounds in terms of $\sigma_T$:
$$10 = 12 - 2 = \mu_T - 1\sigma_T, \quad 16 = 12 + 4 = \mu_T + 2\sigma_T$$

**Step 2:** Apply the asymmetric half-rule:
- From $\mu_T - 1\sigma_T$ to $\mu_T$: half the 68% area = $68.27\% / 2 = 34.135\%$
- From $\mu_T$ to $\mu_T + 2\sigma_T$: half the 95% area = $95.45\% / 2 = 47.725\%$

**Step 3:** Total:
$$P(10 \le T \le 16) \approx 34.135\% + 47.725\% = \boxed{81.86\%}$$

### R Implementation

```r
# Verify 68-95-99.7 rule numerically
mu <- 12; sigma <- 2

rule_68 <- pnorm(mu + sigma, mu, sigma) - pnorm(mu - sigma, mu, sigma)
rule_95 <- pnorm(mu + 2*sigma, mu, sigma) - pnorm(mu - 2*sigma, mu, sigma)
rule_99 <- pnorm(mu + 3*sigma, mu, sigma) - pnorm(mu - 3*sigma, mu, sigma)

rule_68  # ~0.6827
rule_95  # ~0.9545
rule_99  # ~0.9973

# Asymmetric interval example
pnorm(16, mean = 12, sd = 2) - pnorm(10, mean = 12, sd = 2)  # ~0.8186
```

---

## Section 5.3: Continuous Uniform Distribution

### Core Theory & Definitions

A continuous random variable $X$ follows a **Continuous Uniform Distribution** on the interval $[a, b]$, written $X \sim U(a, b)$, if all values in the interval are equally likely. The PDF is flat (constant) over $[a, b]$ and zero outside.

**Common applications:**
- **General statistics:** Modeling rounding errors, random selection from a range, Monte Carlo simulation inputs.
- **Time-domain:** Random backoff intervals in network collision avoidance (CSMA/CD), quantization error in analog-to-digital converters, scheduling jitter, random timestamp offsets.

> **Practical / Time-Domain Note:**
> In network protocols (e.g., Ethernet CSMA/CD), when a collision is detected, each station waits a random backoff time drawn from $U(0, 2^k \cdot T_{slot})$ where $k$ is the retry attempt. The Uniform distribution models this backoff window perfectly. The key property for exam problems is that $P(X \in [c, d]) = (d - c)/(b - a)$ for any sub-interval $[c, d] \subseteq [a, b]$.

### Mathematical Formulas & Derivations

**Probability Density Function (PDF):**
$$f(x) = \frac{1}{b - a}, \quad a \le x \le b \quad (\text{zero otherwise})$$

**Cumulative Distribution Function (CDF):**
$$F(x) = P(X \le x) = \frac{x - a}{b - a}, \quad a \le x \le b$$

**Interval Probability:**
$$P(c \le X \le d) = \frac{d - c}{b - a}, \quad a \le c \le d \le b$$

**Mean (Expected Value):**
$$E[X] = \frac{a + b}{2}$$

**Variance:**
$$V(X) = \frac{(b - a)^2}{12}$$

**Standard Deviation:**
$$\sigma_X = \frac{b - a}{\sqrt{12}} = \frac{b - a}{2\sqrt{3}}$$

**$p$-th Quantile (Inverse CDF):**
$$x_p = a + p \cdot (b - a)$$

For example, the median is $x_{0.5} = (a + b)/2$, and the 75th percentile is $x_{0.75} = a + 0.75(b - a)$.

**Time-Domain Adapted Formula (Backoff Interval):**

For a backoff interval $T \sim U(a_{[ms]}, b_{[ms]})$ in milliseconds:
$$E[T] = \frac{a_{[ms]} + b_{[ms]}}{2} \quad [\text{ms}]$$
$$V(T) = \frac{(b_{[ms]} - a_{[ms]})^2}{12} \quad [\text{ms}^2]$$

If converted to seconds ($c = 1/1000$):
$$E[T_{[s]}] = \frac{1}{1000} \cdot E[T_{[ms]}], \quad V(T_{[s]}) = \frac{1}{10^6} \cdot V(T_{[ms]})$$

### Worked Exercises

#### Exercise 8: Uniform Random Backoff Time (Time-Domain)
**Problem:** A network interface uses random backoff $T \sim U(10, 50)$ ms.
a) Find $P(T > 35)$.
b) Find the mean and variance of $T$.
c) Find the 90th percentile of the backoff time.

**Solution:**

**a) Interval probability:
$$P(T > 35) = \frac{50 - 35}{50 - 10} = \frac{15}{40} = \boxed{0.375}$$

**b) Mean and variance:
$$E[T] = \frac{10 + 50}{2} = \frac{60}{2} = 30 \text{ ms}$$
$$V(T) = \frac{(50 - 10)^2}{12} = \frac{1600}{12} \approx 133.33 \text{ ms}^2$$

**c) 90th percentile:
$$t_{0.90} = 10 + 0.90 \times (50 - 10) = 10 + 36 = \boxed{46 \text{ ms}}$$

#### Exercise 9: Scheduling Jitter (Time-Domain)
**Problem:** A task scheduler introduces jitter $J \sim U(-5, 5)$ ms. Find the probability that the absolute jitter $|J|$ exceeds 3 ms.

**Solution:**

$|J| > 3$ corresponds to $J < -3$ or $J > 3$.

$$P(J < -3) = \frac{-3 - (-5)}{5 - (-5)} = \frac{2}{10} = 0.20$$
$$P(J > 3) = \frac{5 - 3}{10} = 0.20$$
$$P(|J| > 3) = 0.20 + 0.20 = \boxed{0.40}$$

#### Exercise 10: Quantization Error in ADC
**Problem:** An analog-to-digital converter (ADC) introduces quantization error $E \sim U(-q/2, q/2)$ where $q = 0.01$ V. Find the variance and standard deviation of $E$.

**Solution:**

$$V(E) = \frac{(q/2 - (-q/2))^2}{12} = \frac{q^2}{12} = \frac{(0.01)^2}{12} = \frac{0.0001}{12} \approx 8.33 \times 10^{-6} \text{ V}^2$$
$$\sigma_E = \frac{q}{\sqrt{12}} = \frac{0.01}{2\sqrt{3}} \approx \boxed{2.89 \times 10^{-3} \text{ V}}$$

### R Implementation

```r
# Continuous Uniform U(10, 50): P(T > 35) = 1 - F(35)
punif(q = 35, min = 10, max = 50, lower.tail = FALSE)   # 0.375

# Interval probability: P(20 <= T <= 40)
punif(q = 40, min = 10, max = 50) - punif(q = 20, min = 10, max = 50)

# Mean and variance (manual calculation)
a <- 10; b <- 50
mean_u <- (a + b) / 2              # 30
var_u  <- (b - a)^2 / 12           # 133.33

# 90th percentile
qunif(p = 0.90, min = 10, max = 50)   # 46

# Random sample from U(10, 50)
set.seed(42)
runif(n = 1000, min = 10, max = 50)
```

---

## Section 5.4: Exponential Distribution

### Core Theory & Definitions

The **Exponential Distribution** $X \sim Exp(\lambda)$ models the waiting time until the first event in a Poisson process with rate $\lambda$. It is the **only memoryless continuous distribution**, a property with profound implications for modeling component lifetimes and inter-arrival times.

**Definition of the memoryless property:** A distribution is memoryless if:
$$P(X > s + t \mid X > s) = P(X > t) \quad \text{for all } s, t \ge 0$$

Intuitively: given that a component has already survived $s$ units of time, the probability of surviving an additional $t$ units is the same as the probability of surviving $t$ units from the start. The component "has no memory" of its age.

**Rate vs. Scale parameterization:** Some textbooks and software parameterize the Exponential by its mean (scale $\theta = 1/\lambda$) rather than its rate $\lambda$. R uses the rate parameterization by default. Always verify which parameterization is used before applying formulas.

**Relationship to Poisson:** If events occur as a Poisson process with rate $\lambda$ (events per unit time), then the inter-event time $X \sim Exp(\lambda)$.

> **Practical / Time-Domain Note:**
> The Exponential distribution is the default model for component failure times in reliability engineering (under the assumption of constant failure rate, i.e., no aging). However, most real hardware exhibits a bathtub-shaped hazard rate: high infant mortality (decreasing hazard, $k < 1$ Weibull), then a low flat rate (Exponential), then wear-out (increasing hazard, $k > 1$ Weibull). Blindly applying the Exponential model to aged hardware significantly underestimates failure probability.

### Mathematical Formulas & Derivations

**Probability Density Function (PDF):**
$$f(x) = \lambda e^{-\lambda x}, \quad x \ge 0 \quad (\text{zero for } x < 0)$$

**Cumulative Distribution Function (CDF):**
$$F(x) = P(X \le x) = 1 - e^{-\lambda x}, \quad x \ge 0$$

**Survival / Reliability Function:**
$$S(x) = P(X > x) = e^{-\lambda x}$$

**Mean and Variance:**
$$E[X] = \frac{1}{\lambda}, \quad V(X) = \frac{1}{\lambda^2}, \quad \sigma_X = \frac{1}{\lambda}$$

Note: for the Exponential distribution, the mean equals the standard deviation.

**Memoryless Property:**
$$P(X > s + t \mid X > s) = \frac{P(X > s + t)}{P(X > s)} = \frac{e^{-\lambda(s+t)}}{e^{-\lambda s}} = e^{-\lambda t} = P(X > t)$$

**Conditional Survival (Time-Domain Adapted):**

For a system component with lifetime $T \sim Exp(\lambda)$, the probability of surviving an additional $t$ hours given it has already survived $s$ hours:
$$P(T > s + t \mid T > s) = e^{-\lambda t} = P(T > t)$$

This ONLY equals $P(T > t)$ because the Exponential is memoryless. For Gamma or Weibull ($k \ne 1$), the conditional survival probability depends on the current age $s$ and must be computed as $S(s+t)/S(s)$.

**Minimum of Independent Exponentials:**

If $X_1 \sim Exp(\lambda_1), X_2 \sim Exp(\lambda_2), \ldots, X_n \sim Exp(\lambda_n)$ are independent, then:
$$X_{min} = \min(X_1, \ldots, X_n) \sim Exp(\lambda_1 + \lambda_2 + \cdots + \lambda_n)$$

**$p$-th Quantile:**
$$x_p = -\frac{\ln(1 - p)}{\lambda}$$

For example, the median is $x_{0.5} = \ln(2)/\lambda$.

### Worked Exercises

#### Exercise 11: Hard Drive Survival Probability
**Problem:** A hard drive has failure rate $\lambda = 0.0001$ h$^{-1}$ (mean lifetime of 10,000 hours). Find:
a) The probability that the drive survives beyond 5,000 hours.
b) The median lifetime of the drive.

**Solution:**

**a) Survival function:
$$P(T > 5000) = e^{-\lambda \cdot 5000} = e^{-(0.0001)(5000)} = e^{-0.5} \approx \boxed{0.6065}$$

**b) Median lifetime $t_{0.5} = \ln(2) / \lambda$:
$$t_{0.5} = \frac{\ln 2}{0.0001} = \frac{0.6931}{0.0001} \approx \boxed{6{,}931 \text{ hours}}$$

#### Exercise 12: Minimum of Independent Failure Times (Time-Domain)
**Problem:** A system has two critical components: $T_1 \sim Exp(0.02)$ h$^{-1}$ and $T_2 \sim Exp(0.03)$ h$^{-1}$. The system fails when the FIRST component fails. Find:
a) The distribution and mean of $T_{sys} = \min(T_1, T_2)$.
b) $P(T_{sys} > 10)$.

**Solution:**

**a) Minimum of independent Exponentials:
$$T_{sys} \sim Exp(\lambda_1 + \lambda_2) = Exp(0.02 + 0.03) = Exp(0.05)$$
$$E[T_{sys}] = \frac{1}{0.05} = \boxed{20 \text{ hours}}$$

**b) Survival probability:
$$P(T_{sys} > 10) = e^{-0.05 \times 10} = e^{-0.5} \approx \boxed{0.6065}$$

#### Exercise 13: Memoryless Property in a Network Router (Time-Domain)
**Problem:** A network router's time between packet drops $T \sim Exp(0.1)$ minutes. Given no packet has been dropped in the last 5 minutes, find the probability of surviving another 3 minutes without a drop.

**Solution:**

By the memoryless property:
$$P(T > 5 + 3 \mid T > 5) = P(T > 3) = e^{-0.1 \times 3} = e^{-0.3} \approx \boxed{0.7408}$$

The 5 minutes of observed uptime are irrelevant due to the memoryless property.

#### Exercise 14: Conditional Survival for a Non-Memoryless Component (Time-Domain)
**Problem:** A pump's lifetime $T$ has survival function $S(t) = e^{-(t/1000)^2}$ (Weibull with $k=2$). Given the pump has survived 800 hours, find $P(T > 1000 \mid T > 800)$.

**Solution:**

This is NOT memoryless (Weibull with $k = 2 \ne 1$):

$$P(T > 1000 \mid T > 800) = \frac{S(1000)}{S(800)} = \frac{e^{-(1000/1000)^2}}{e^{-(800/1000)^2}} = \frac{e^{-1}}{e^{-0.64}} = e^{-0.36} \approx \boxed{0.6977}$$

> **Gotcha:** If the memoryless property were incorrectly applied here (valid only for Exponential), one would compute $P(T > 200) = e^{-(200/1000)^2} = e^{-0.04} \approx 0.9608$, which is dramatically wrong.

### R Implementation

```r
# Exponential distribution: P(T <= t), rate = lambda
pexp(q = 5000, rate = 0.0001)            # P(T <= 5000)
pexp(q = 5000, rate = 0.0001, lower.tail = FALSE)  # P(T > 5000) = survival

# Survival probability P(T > 10) for system with combined rate
pexp(q = 10, rate = 0.05, lower.tail = FALSE)

# Median lifetime
qexp(p = 0.5, rate = 0.0001)             # = log(2)/lambda

# PDF value at t
dexp(x = 1000, rate = 0.0001)

# Simulate 500 component lifetimes
set.seed(42)
lifetimes <- rexp(n = 500, rate = 0.0001)
mean(lifetimes)   # Should be approximately 1/lambda = 10000
```

---

## Section 5.5: Gamma, Erlang, and Weibull Distributions

### Core Theory & Definitions

**Gamma Distribution:** The Gamma distribution generalizes the Exponential. It models the time until the $\alpha$-th event in a Poisson process, or equivalently, the sum of $\alpha$ independent $Exp(\beta)$ random variables. The shape parameter $\alpha > 0$ and rate parameter $\beta > 0$ (or scale $\theta = 1/\beta > 0$).

**Erlang Distribution:** A special case of the Gamma distribution where $\alpha = k$ is a positive integer. It is used in queueing theory to model multi-stage processes (e.g., time for $k$ service completions).

**Gamma Function:** The generalization of the factorial to non-integer values:
$$\Gamma(\alpha) = \int_0^\infty t^{\alpha-1} e^{-t} \, dt$$

Key properties: $\Gamma(1) = 1$, $\Gamma(1/2) = \sqrt{\pi}$, $\Gamma(\alpha + 1) = \alpha \cdot \Gamma(\alpha)$, and for positive integers: $\Gamma(n) = (n-1)!$.

**Weibull Distribution:** Models time-to-failure with a non-constant hazard rate. Parameterized by shape $k > 0$ and scale $\lambda > 0$. The Exponential is a special case ($k = 1$). The hazard rate is monotonically increasing for $k > 1$ (wear-out), constant for $k = 1$ (memoryless), and decreasing for $k < 1$ (infant mortality).

**Chi-Square Relationship:** $\chi^2(\nu) = Gamma(\nu/2, 1/2)$, i.e., the Chi-Square distribution with $\nu$ degrees of freedom is a Gamma distribution with shape $\alpha = \nu/2$ and rate $\beta = 1/2$.

> **Practical / Time-Domain Note:**
> The Gamma and Weibull distributions are essential for modeling real-world system reliability. The Erlang distribution arises naturally in queueing systems: the service time for a customer requiring $k$ sequential service stages (each exponentially distributed with rate $\beta$) follows $Erlang(k, \beta)$. The Weibull distribution is the standard model for hardware lifetime analysis because its flexible hazard rate captures the three phases of the bathtub curve.

### Mathematical Formulas & Derivations

**Gamma Distribution $Gamma(\alpha, \beta)$ (rate parameterization):**

$$f(x) = \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha - 1} e^{-\beta x}, \quad x > 0$$

$$E[X] = \frac{\alpha}{\beta}, \quad V(X) = \frac{\alpha}{\beta^2}$$

**Erlang Distribution $Erlang(k, \beta)$:**

Same as $Gamma(k, \beta)$ where $k$ is a positive integer. It is the sum of $k$ independent $Exp(\beta)$ random variables:
$$T = X_1 + X_2 + \cdots + X_k, \quad X_i \stackrel{iid}{\sim} Exp(\beta) \implies T \sim Erlang(k, \beta)$$

**Erlang Sum Property (Critical Requirement):** The $k$ Exponential components must have the EXACT same rate $\beta$. If rates differ, the sum is NOT Erlang.

$$E[T] = \frac{k}{\beta}, \quad V(T) = \frac{k}{\beta^2}$$

**Weibull Distribution $Weibull(k, \lambda)$:**

$$f(t) = \frac{k}{\lambda} \left(\frac{t}{\lambda}\right)^{k-1} e^{-(t/\lambda)^k}, \quad t \ge 0$$

**Survival (Reliability) Function:**
$$S(t) = P(T > t) = e^{-(t/\lambda)^k}$$

**CDF:**
$$F(t) = P(T \le t) = 1 - e^{-(t/\lambda)^k}$$

**Hazard Rate:**
$$h(t) = \frac{f(t)}{S(t)} = \frac{k}{\lambda}\left(\frac{t}{\lambda}\right)^{k-1}$$

- $k < 1$: Decreasing hazard (infant mortality / early failures)
- $k = 1$: Constant hazard (reduces to $Exp(1/\lambda)$, memoryless)
- $k > 1$: Increasing hazard (wear-out / aging failures)

**Weibull Mean and Variance:**
$$E[T] = \lambda \cdot \Gamma\left(1 + \frac{1}{k}\right)$$
$$V(T) = \lambda^2 \left[ \Gamma\left(1 + \frac{2}{k}\right) - \left(\Gamma\left(1 + \frac{1}{k}\right)\right)^2 \right]$$

**Rate vs. Scale Parameterization Alert:**

R's `pgamma()` uses the rate parameterization by default: $\beta$ = rate. Some textbooks use the scale $\theta = 1/\beta$. Always verify:
- Rate parameterization: `pgamma(x, shape = alpha, rate = beta)`
- Scale parameterization: `pgamma(x, shape = alpha, scale = theta)` where `theta = 1/rate`

### Worked Exercises

#### Exercise 15: Waiting Time for 3rd API Request (Erlang)
**Problem:** Requests arrive as a Poisson process at rate $\beta = 2$ requests/second. Find the mean, variance, and $P(T \le 2)$ for the waiting time $T$ until the 3rd request.

**Solution:**

$T \sim Erlang(k=3, \beta=2)$, equivalently $Gamma(3, 2)$.

**Mean and variance:**
$$E[T] = \frac{k}{\beta} = \frac{3}{2} = 1.5 \text{ s}$$
$$V(T) = \frac{k}{\beta^2} = \frac{3}{4} = 0.75 \text{ s}^2$$

**CDF:** Using R: `pgamma(2, shape = 3, rate = 2)` $\approx \boxed{0.7619}$.

#### Exercise 16: Weibull Survival Probability with Wear-Out
**Problem:** A pump's failure time $T \sim Weibull(k=2, \lambda=1000 \text{ h})$. Find:
a) $P(T > 1500)$.
b) The median lifetime.

**Solution:**

**a) Survival function:
$$P(T > 1500) = e^{-(1500/1000)^2} = e^{-(1.5)^2} = e^{-2.25} \approx \boxed{0.1054}$$

**b) Set $S(t_{0.5}) = 0.5$:
$$e^{-(t_{0.5}/1000)^2} = 0.5 \implies \left(\frac{t_{0.5}}{1000}\right)^2 = \ln 2 \implies t_{0.5} = 1000\sqrt{\ln 2} \approx \boxed{832.6 \text{ h}}$$

#### Exercise 17: Sum of Independent Exponential Stage Times (Time-Domain)
**Problem:** A process has 4 sequential stages, each independently $Exp(0.5)$ s$^{-1}$ (mean 2 s per stage). Find the distribution and mean of the total time $T$.

**Solution:**

Since all 4 stages have the **same rate** $\beta = 0.5$:
$$T = X_1 + X_2 + X_3 + X_4 \sim Gamma(4, 0.5) = Erlang(4, 0.5)$$
$$E[T] = \frac{4}{0.5} = 8 \text{ s}, \quad V(T) = \frac{4}{0.25} = 16 \text{ s}^2$$

> If the stages had different rates, the sum would NOT be an Erlang/Gamma distribution and would require convolution to find exactly.

#### Exercise 18: Chi-Square as a Special Gamma (Time-Domain)
**Problem:** The squared normalized timing error $Z^2$ where $Z \sim N(0,1)$ follows a Chi-Square distribution $\chi^2(1)$. Express this as a Gamma distribution and find its mean and variance.

**Solution:**

$$\chi^2(1) = Gamma\left(\frac{1}{2}, \frac{1}{2}\right)$$

$$E[\chi^2(1)] = \frac{\alpha}{\beta} = \frac{1/2}{1/2} = 1, \quad V(\chi^2(1)) = \frac{\alpha}{\beta^2} = \frac{1/2}{1/4} = 2$$

This matches the known result: $E[\chi^2(\nu)] = \nu$, $V(\chi^2(\nu)) = 2\nu$ with $\nu = 1$. $\boxed{E = 1, V = 2}$.

### R Implementation

```r
# Gamma distribution (rate parameterization)
# P(T <= 2) for T ~ Gamma(alpha=3, beta=2)
pgamma(q = 2, shape = 3, rate = 2)       # ~0.7619

# P(T > 1500) for Weibull(k=2, lambda=1000)
pweibull(q = 1500, shape = 2, scale = 1000, lower.tail = FALSE)  # ~0.1054

# Weibull median
qweibull(p = 0.5, shape = 2, scale = 1000)  # ~832.6

# Gamma PDF at x = 1.5
dgamma(x = 1.5, shape = 3, rate = 2)

# Chi-square: same as Gamma(nu/2, 1/2)
pgamma(q = 3.84, shape = 0.5, rate = 0.5)
pchisq(q = 3.84, df = 1)               # These should be identical

# WARNING: R's pgamma uses rate by default.
# If your textbook uses scale (theta = 1/rate), use:
pgamma(q = 2, shape = 3, scale = 0.5)  # scale = 1/rate = 1/2
```

---

## Section 5.6: Transformations of Continuous Random Variables

### Core Theory & Definitions

When a continuous random variable $X$ is passed through a deterministic function $Y = g(X)$, the resulting $Y$ is also a random variable. The goal is to find the PDF of $Y$ from the PDF of $X$. Two main methods are used:

1. **CDF Method (Change-of-Variable via CDF):** Find $F_Y(y) = P(Y \le y)$ directly from $F_X$, then differentiate: $f_Y(y) = dF_Y(y)/dy$.

2. **Jacobian Method (Change-of-Variable via PDF):** Valid for strictly monotonic $g$. Use the formula:
$$f_Y(y) = f_X\left(g^{-1}(y)\right) \cdot \left|\frac{d}{dy} g^{-1}(y)\right|$$

where $|d g^{-1}(y)/dy|$ is the absolute value of the Jacobian (derivative of the inverse transformation).

**Common Time-Domain Transformations:**
- $Y = 1/X$: Converts inter-arrival time $X$ to throughput $Y$ (requests per second).
- $Y = cX$: Unit conversion (e.g., seconds to milliseconds, $c = 1000$).
- $Y = \ln X$: Log-Normal transformation; if $Y \sim N(\mu, \sigma^2)$, then $X = e^Y$ is Log-Normal.

> **Practical / Time-Domain Note:**
> **Jensen's Inequality and the Throughput Fallacy:** For a convex function $g$ and a random variable $X$, $E[g(X)] \ge g(E[X])$. In particular, since $g(x) = 1/x$ is convex for $x > 0$:
> $$E\left[\frac{1}{T}\right] \ge \frac{1}{E[T]}$$
> This means the **average throughput** (average of $1/T$) is strictly greater than the reciprocal of the average processing time. Average throughput cannot be estimated as $1/\bar{T}$.

### Mathematical Formulas & Derivations

**Linear Transformation $Y = aX + b$:**
$$f_Y(y) = \frac{1}{|a|} f_X\left(\frac{y - b}{a}\right)$$
$$E[Y] = a \cdot E[X] + b, \quad V(Y) = a^2 \cdot V(X)$$

**Monotonic Non-Linear Transformation (Jacobian Method):**
$$f_Y(y) = f_X\left(g^{-1}(y)\right) \cdot \left|\frac{dg^{-1}}{dy}\right|$$

**Non-Monotonic Transformation (CDF Method required):**

For $Y = X^2$ with $X \sim N(0, \sigma^2)$ (which is symmetric about 0, so $g$ is not monotonic):
$$F_Y(y) = P(X^2 \le y) = P(-\sqrt{y} \le X \le \sqrt{y}) = F_X(\sqrt{y}) - F_X(-\sqrt{y})$$
Differentiating:
$$f_Y(y) = \frac{1}{2\sqrt{y}} f_X(\sqrt{y}) + \frac{1}{2\sqrt{y}} f_X(-\sqrt{y}) = \frac{1}{\sqrt{y}} f_X(\sqrt{y})$$

Substituting the Normal PDF:
$$f_Y(y) = \frac{1}{\sigma\sqrt{2\pi y}} e^{-y/(2\sigma^2)}, \quad y > 0$$

This is a $Gamma(1/2, 1/(2\sigma^2))$ distribution, equivalent to $\chi^2(1)$ when $\sigma = 1$.

**Log-Normal Distribution:**

If $X \sim N(\mu, \sigma^2)$ and $Y = e^X$, then $Y$ is **Log-Normal** with:
$$E[Y] = e^{\mu + \sigma^2/2}, \quad V(Y) = e^{2\mu + \sigma^2}(e^{\sigma^2} - 1)$$

Conversely, if $Y$ is Log-Normal such that $\ln Y \sim N(\mu, \sigma^2)$, then:
$$P(Y \le y) = \Phi\left(\frac{\ln y - \mu}{\sigma}\right)$$

**Reciprocal Transformation $Y = 1/X$ for $X \sim U(a, b)$ with $0 < a < b$:**

$g(x) = 1/x$ is monotonically decreasing on $(a, b)$. Inverse: $x = 1/y$, Jacobian: $|dx/dy| = 1/y^2$.
$$f_Y(y) = f_X\left(\frac{1}{y}\right) \cdot \frac{1}{y^2} = \frac{1}{b-a} \cdot \frac{1}{y^2}, \quad \frac{1}{b} \le y \le \frac{1}{a}$$

**Time-Domain Adapted Formula (Unit Conversion):**

Converting time units from seconds to milliseconds ($c = 1000$): if $T \sim N(\mu_{[s]}, \sigma^2_{[s]})$, then $T_{ms} = 1000 \cdot T \sim N(1000\mu_{[s]}, 10^6 \sigma^2_{[s]})$.

### Worked Exercises

#### Exercise 19: Reciprocal Transformation for Throughput (Time-Domain)
**Problem:** Service time $T \sim U(0.5, 2.0)$ seconds per request. Find the PDF of throughput $Y = 1/T$ (requests per second).

**Solution:**

$g(t) = 1/t$ is monotonically decreasing on $(0.5, 2.0)$.

**Step 1:** Inverse transformation: $t = 1/y$, Jacobian: $|dt/dy| = 1/y^2$.

**Step 2:** Range of $Y$: when $t = 2.0$, $y = 0.5$; when $t = 0.5$, $y = 2.0$. So $y \in [0.5, 2.0]$.

**Step 3:** $f_T(t) = 1/(2.0 - 0.5) = 2/3$ for $t \in [0.5, 2.0]$.

**Step 4:** Apply the Jacobian formula:
$$f_Y(y) = f_T\left(\frac{1}{y}\right) \cdot \frac{1}{y^2} = \frac{2}{3} \cdot \frac{1}{y^2} = \frac{2}{3y^2}, \quad 0.5 \le y \le 2.0$$

**Step 5:** Verify Jensen's inequality for $E[Y]$:
$$E[Y] = \int_{0.5}^{2.0} y \cdot \frac{2}{3y^2} \, dy = \frac{2}{3} \ln\left(\frac{2.0}{0.5}\right) = \frac{2}{3} \ln 4 \approx 0.924$$

Indeed $E[Y] \approx 0.924 > 1/E[T] = 1/1.25 = 0.8$, confirming Jensen's inequality. $\boxed{f_Y(y) = 2/(3y^2),\ y \in [0.5, 2.0]}$

#### Exercise 20: Log-Normal Mean for Salary Data
**Problem:** Log-salaries follow $Y = \ln(X) \sim N(10, 0.25)$ (in ln-dollars). Find the expected salary $E[X]$.

**Solution:**

$X = e^Y$ where $Y \sim N(\mu = 10, \sigma^2 = 0.25)$.

$$E[X] = e^{\mu + \sigma^2/2} = e^{10 + 0.125} = e^{10.125} \approx \boxed{24{,}905 \text{ dollars}}$$

#### Exercise 21: Non-Monotonic Transformation -- Squared Latency Error (Time-Domain)
**Problem:** A timing error $T \sim N(0, \sigma^2)$ with $\sigma = 5$ ms. Find the PDF of the squared error $Y = T^2$.

**Solution:**

Since $T$ is symmetric about 0, $g(t) = t^2$ is not monotonic. Use the CDF method:

$$F_Y(y) = P(T^2 \le y) = P(-\sqrt{y} \le T \le \sqrt{y}) = \Phi\left(\frac{\sqrt{y}}{\sigma}\right) - \Phi\left(\frac{-\sqrt{y}}{\sigma}\right)$$

Differentiating with respect to $y$:
$$f_Y(y) = \frac{1}{\sigma\sqrt{2\pi y}} e^{-y/(2\sigma^2)} = \frac{1}{5\sqrt{2\pi y}} e^{-y/50}, \quad y > 0$$

This is a $Gamma(1/2, 1/50)$ distribution. $\boxed{f_Y(y) = \frac{1}{5\sqrt{2\pi y}} e^{-y/50}}$

#### Exercise 22: Unit Conversion with the $c^2$ Rule (Time-Domain)
**Problem:** Network round-trip time $T \sim N(50, 100)$ ms. Convert to seconds and state the distribution of $T_{[s]} = T/1000$.

**Solution:**

Using the linear transformation with $c = 1/1000$:
$$\mu_{[s]} = \frac{50}{1000} = 0.05 \text{ s}$$
$$\sigma^2_{[s]} = \left(\frac{1}{1000}\right)^2 \times 100 = \frac{100}{10^6} = 10^{-4} \text{ s}^2$$

$$T_{[s]} \sim N(0.05,\ 10^{-4}) \quad \text{i.e., } N(0.05, \sigma = 0.01) \text{ seconds}$$

> **Critical:** The variance scaled by $c^2 = 10^{-6}$, not by $c = 10^{-3}$. A common error is to report $\sigma^2_{[s]} = 100/1000 = 0.1$, which is wrong by a factor of 1000. $\boxed{T_{[s]} \sim N(0.05,\, 10^{-4})}$

### R Implementation

```r
# Log-Normal: mean of X = exp(Y) where Y ~ N(mu, sigma^2)
mu_y <- 10; sigma_y <- 0.5
E_X <- exp(mu_y + sigma_y^2 / 2)

# CDF of Log-Normal: P(X <= x) = Phi((ln(x) - mu) / sigma)
plnorm(q = exp(10.5), meanlog = 10, sdlog = 0.5)  # Should be ~0.8413

# Built-in log-normal functions
plnorm(q = 24905, meanlog = 10, sdlog = 0.5)

# Chi-square distribution (squared standard normal)
pchisq(q = 25, df = 1)

# Linear transformation: if X ~ N(50, 100) ms, convert to seconds
mean_s <- 50 / 1000            # 0.05 s
var_s  <- 100 / (1000^2)       # 0.0001 s^2 (NOT 100/1000!)
sd_s   <- sqrt(var_s)          # 0.01 s

# R code does not change for the distribution, just the parameters
pnorm(q = 0.06, mean = mean_s, sd = sd_s)  # P(T_s <= 0.06 s) = P(T <= 60 ms)
```

---

## Exam Preparation Guide

### Formula Quick-Reference

| Distribution | PDF $f(x)$ | Mean $E[X]$ | Variance $V(X)$ | Survival $P(X > x)$ |
|---|---|---|---|---|
| $N(\mu, \sigma^2)$ | $\frac{1}{\sigma\sqrt{2\pi}}e^{-(x-\mu)^2/(2\sigma^2)}$ | $\mu$ | $\sigma^2$ | $1 - \Phi\!\left(\frac{x-\mu}{\sigma}\right)$ |
| $U(a,b)$ | $\frac{1}{b-a}$ for $x \in [a,b]$ | $\frac{a+b}{2}$ | $\frac{(b-a)^2}{12}$ | $\frac{b-x}{b-a}$ |
| $Exp(\lambda)$ | $\lambda e^{-\lambda x}$ for $x \ge 0$ | $\frac{1}{\lambda}$ | $\frac{1}{\lambda^2}$ | $e^{-\lambda x}$ |
| $Gamma(\alpha,\beta)$ | $\frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\beta x}$ | $\frac{\alpha}{\beta}$ | $\frac{\alpha}{\beta^2}$ | (no closed form) |
| $Weibull(k,\lambda)$ | $\frac{k}{\lambda}(\frac{x}{\lambda})^{k-1}e^{-(x/\lambda)^k}$ | $\lambda\,\Gamma(1+\frac{1}{k})$ | (complex) | $e^{-(x/\lambda)^k}$ |

**Standardization (Z-score):**
$$Z = \frac{X - \mu}{\sigma} \sim N(0,1)$$

**Percentile / Quantile (Normal):**
$$x_p = \mu + z_p \cdot \sigma$$

**System of equations for unknown $\mu, \sigma$ (from two percentiles):**
$$a = \mu + z_{p_1} \sigma, \quad b = \mu + z_{p_2} \sigma \implies \sigma = \frac{a - b}{z_{p_1} - z_{p_2}}$$

**Uniform quantile:**
$$x_p = a + p(b-a)$$

**Exponential memoryless property:**
$$P(X > s+t \mid X > s) = e^{-\lambda t} = P(X > t)$$

**Minimum of independent Exponentials:**
$$\min(X_1,\ldots,X_n) \sim Exp(\lambda_1 + \cdots + \lambda_n)$$

**Erlang (sum of identical Exponentials, $k$ integer):**
$$X_1 + \cdots + X_k \sim Erlang(k,\beta) = Gamma(k,\beta), \quad E = k/\beta, \quad V = k/\beta^2$$

**Weibull survival:**
$$S(t) = e^{-(t/\lambda)^k}$$

**Jacobian transformation (monotonic $g$):**
$$f_Y(y) = f_X(g^{-1}(y)) \cdot \left|\frac{dg^{-1}}{dy}\right|$$

**Log-Normal mean:**
$$E[e^X] = e^{\mu + \sigma^2/2} \quad \text{where } X \sim N(\mu,\sigma^2)$$

**$c^2$ rule (unit conversion):**
$$Y = cX \implies E[Y] = c\,E[X], \quad V(Y) = c^2\,V(X)$$

**Jensen's inequality (convex $g$, e.g., $g(x)=1/x$):**
$$E[g(X)] \ge g(E[X]) \implies E[1/T] \ge 1/E[T]$$

**Symmetry of standard normal:**
$$\Phi(-z) = 1 - \Phi(z)$$

**Sum of independent normals:**
$$X_1 + X_2 \sim N(\mu_1+\mu_2,\; \sigma_1^2 + \sigma_2^2)$$

**Empirical Rule:**
$$P(\mu \pm \sigma) \approx 68.27\%, \quad P(\mu \pm 2\sigma) \approx 95.45\%, \quad P(\mu \pm 3\sigma) \approx 99.73\%$$

---

### Exam Checklist

| Category | Items |
|----------|-------|
| **Must Memorize** | Normal PDF and CDF; Z-score formula $Z = (X-\mu)/\sigma$; Z-table symmetry $\Phi(-z) = 1 - \Phi(z)$; Empirical 68-95-99.7 rule; Exponential PDF, CDF, survival, and mean; Memoryless property of Exponential; Uniform mean and variance; $c^2$ rule for unit conversions; Weibull survival function $e^{-(t/\lambda)^k}$; Erlang = Gamma with integer shape |
| **Must Understand** | Why the Normal domain $(-\infty, +\infty)$ is problematic for strictly positive quantities; System of two equations to solve for unknown $\mu$ and $\sigma$ from two percentiles; When memoryless property applies vs. not (Exponential only); How to identify the correct distribution for a given scenario; Why $E[1/T] \ne 1/E[T]$ (Jensen's inequality); CDF method vs. Jacobian method for transformations; Why Erlang requires identical rates; Weibull hazard interpretation ($k < 1$, $k = 1$, $k > 1$) |
| **Book-Only (Professor May Test)** | Log-Normal distribution and its mean formula $e^{\mu + \sigma^2/2}$; Chi-square as a special Gamma ($\chi^2(\nu) = Gamma(\nu/2, 1/2)$); Non-monotonic transformations via the CDF method (e.g., $Y = X^2$); Gamma function properties: $\Gamma(1) = 1$, $\Gamma(1/2) = \sqrt{\pi}$, $\Gamma(n) = (n-1)!$; Weibull mean formula using the Gamma function; Minimum of independent Exponentials distribution; Quantization error as Uniform; Full derivation of Jacobian for reciprocal transformation |

---

### Common Exam Traps

1. **Variance vs. Standard Deviation in R:** `pnorm()` requires `sd` (standard deviation), not variance. If $X \sim N(50, 100)$ where 100 is the variance, use `sd = sqrt(100) = 10`, not `sd = 100`. This mistake produces wildly wrong results.

2. **Legacy Z-table sign error:** $\Phi(-z)$ for negative Z-scores is not in all tables. Always use $\Phi(-z) = 1 - \Phi(z)$ to convert to a positive Z-score before looking up.

3. **$c^2$ rule violation (unit conversion):** When converting $T$ from ms to s with $c = 1/1000$, the variance scales by $c^2 = 10^{-6}$, not $c = 10^{-3}$. The standard deviation scales by $c = 10^{-3}$. This is the single most common arithmetic error in time-domain problems.

4. **Applying memoryless property to Weibull or Gamma:** Only the Exponential distribution ($k=1$ Weibull) is memoryless. For $Weibull(k=2, \lambda)$, the conditional survival $P(T > s+t \mid T > s) = S(s+t)/S(s) \ne P(T > t)$ and depends on the current age $s$.

5. **Erlang requires identical rates:** The sum $X_1 + \cdots + X_k$ is Erlang only if all $X_i$ have the same rate $\beta$. If rates differ, the sum is not Gamma-distributed.

6. **Throughput fallacy (Jensen):** $E[1/T] \ne 1/E[T]$. The average throughput is strictly greater than the reciprocal of the average service time. Do not substitute $1/\bar{T}$ for $\overline{1/T}$.

7. **Normal model with negative values:** $N(\mu, \sigma^2)$ assigns probability to $(-\infty, 0)$. If $\mu < 3\sigma$, this probability is non-negligible and the Normal model may be inappropriate for strictly positive data.

8. **Rate vs. scale parameterization:** R's `pgamma(x, shape, rate)` vs. textbook $Gamma(\alpha, \theta)$ where $\theta = 1/\text{rate}$. Always confirm which parameterization is in use before plugging numbers.

9. **Weibull hazard interpretation:** The question "is failure rate increasing or decreasing?" is answered directly from $k$: $k < 1$ means decreasing (early failures), $k > 1$ means increasing (aging), $k = 1$ means constant (Exponential).

10. **Empirical rule misapplied to skewed distributions:** The 68-95-99.7 rule applies to approximately symmetric, bell-shaped distributions. Never apply it to Exponential, Gamma ($\alpha < 4$), or Weibull distributions without verifying approximate symmetry.

---

### Exam Paper Cross-References

| Exam Paper | Relevant Questions | Phase 5 Topics Tested | Difficulty |
|---|---|---|---|
| [Exam_paper_Easy.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/PROBABILITY_STATISTICS/Exams/Papers/Exam_paper_Easy.md) | ΘΕΜΑ 4 (parts i, ii, iii) | Normal distribution, Z-score, $P(X < x)$, $P(a \le X \le b)$, R `pnorm()` | 1/5 |
| [Exam_paper_2024_09_06_Team_A.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/PROBABILITY_STATISTICS/Exams/Papers/Exam_paper_2024_09_06_Team_A.md) | ΘΕΜΑ 4 | Normal distribution probability, Z-score standardization | 1/5 |
| [Exam_paper_Intermediate_1.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/PROBABILITY_STATISTICS/Exams/Papers/Exam_paper_Intermediate_1.md) | ΘΕΜΑ 4 | Normal distribution, interval probability, R command | 2/5 |
| [Exam_paper_2023_06_12_Team_null.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/PROBABILITY_STATISTICS/Exams/Papers/Exam_paper_2023_06_12_Team_null.md) | ΘΕΜΑ 3 | Normal distribution, standardization, Z-table | 2/5 |
| [Exam_paper_2024_06_14_Team_B.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/PROBABILITY_STATISTICS/Exams/Papers/Exam_paper_2024_06_14_Team_B.md) | ΘΕΜΑ 4 | Normal probability calculations | 2/5 |
| [Exam_paper_2024_06_14_Team_C.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/PROBABILITY_STATISTICS/Exams/Papers/Exam_paper_2024_06_14_Team_C.md) | ΘΕΜΑ 1 | Normal distribution, Z-score, one-tail probability | 2/5 |
| [Exam_paper_2025_06_03_Team_A.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/PROBABILITY_STATISTICS/Exams/Papers/Exam_paper_2025_06_03_Team_A.md) | ΘΕΜΑ 4 | Normal distribution, R `pnorm()` | 2/5 |
| [Exam_paper_2026_06_09_Team_A.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/PROBABILITY_STATISTICS/Exams/Papers/Exam_paper_2026_06_09_Team_A.md) | ΘΕΜΑ 4 | Normal distribution, probability, R `pnorm()` | 2/5 |
| [Exam_paper_2026_06_09_Team_B.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/PROBABILITY_STATISTICS/Exams/Papers/Exam_paper_2026_06_09_Team_B.md) | ΘΕΜΑ 4 | Normal distribution probability, standardization | 2/5 |
| [Exam_paper_Hard_1.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/PROBABILITY_STATISTICS/Exams/Papers/Exam_paper_Hard_1.md) | ΘΕΜΑ 4 | Normal distribution with one unknown parameter (solve for $\sigma$ from percentile) | 4/5 |
| [Exam_paper_Hard_2.md](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_4/PROBABILITY_STATISTICS/Exams/Papers/Exam_paper_Hard_2.md) | ΘΕΜΑ 4 | Normal with two unknown parameters (solve system of equations for $\mu$ and $\sigma$) | 5/5 |

---

## Combined Exercises

#### Exercise 23: Normal Distribution and Empirical Rule -- Grade Analysis
**Problem:** Final exam scores $X \sim N(65, 225)$ (mean 65, $\sigma = 15$).
a) Find $P(X > 80)$.
b) Find the 90th percentile score.
c) Using the Empirical Rule, estimate the proportion of students scoring between 50 and 95.
d) How many students out of 1,000 score below 35?

**Solution:**

**a) $Z = (80 - 65)/15 = 1.00 \implies P(X > 80) = 1 - \Phi(1) = 1 - 0.8413 = \boxed{0.1587}$

**b) $z_{0.90} = 1.282 \implies x_{0.90} = 65 + 1.282 \times 15 = 65 + 19.23 = \boxed{84.23}$

**c) $50 = 65 - 1\sigma$, $95 = 65 + 2\sigma$. Asymmetric interval:
$P(50 \le X \le 95) = 68.27\%/2 + 95.45\%/2 = 34.135\% + 47.725\% = \boxed{81.86\%}$

**d) $Z = (35 - 65)/15 = -2.00 \implies P(X < 35) = \Phi(-2) = 1 - \Phi(2) = 0.0228$
$1000 \times 0.0228 = \boxed{23 \text{ students}}$

#### Exercise 24: Multi-Distribution Reliability Analysis (Time-Domain)
**Problem:** A server has three independent subsystems:
- Power supply: $T_1 \sim Exp(\lambda_1 = 0.001 \text{ h}^{-1})$
- CPU: $T_2 \sim Exp(\lambda_2 = 0.002 \text{ h}^{-1})$
- Storage: $T_3 \sim Weibull(k=2, \lambda=500 \text{ h})$

a) Find the probability that all three subsystems survive beyond 100 hours.
b) Find $E[T_1]$.
c) Given the CPU has been running 200 hours without failure, find $P(T_2 > 300 \mid T_2 > 200)$.

**Solution:**

**a) By independence, the joint survival is the product:

$P(T_1 > 100) = e^{-0.001 \times 100} = e^{-0.1} \approx 0.9048$

$P(T_2 > 100) = e^{-0.002 \times 100} = e^{-0.2} \approx 0.8187$

$P(T_3 > 100) = e^{-(100/500)^2} = e^{-0.04} \approx 0.9608$

$$P(\text{all survive}) = 0.9048 \times 0.8187 \times 0.9608 \approx \boxed{0.7120}$$

**b) $E[T_1] = 1/\lambda_1 = 1/0.001 = \boxed{1{,}000 \text{ hours}}$

**c) CPU follows $Exp(0.002)$, which is memoryless:
$$P(T_2 > 300 \mid T_2 > 200) = P(T_2 > 100) = e^{-0.002 \times 100} = e^{-0.2} \approx \boxed{0.8187}$$

#### Exercise 25: Transformation and SLA Analysis (Time-Domain)
**Problem:** An API gateway processes requests with inter-arrival time $T \sim Exp(2 \text{ s}^{-1})$. After processing, each request generates a response of size $Y = 5T$ MB. Find:
a) The distribution and mean of the response size $Y$.
b) $P(Y > 3)$.
c) The 95th percentile of the response size.

**Solution:**

**a) $Y = 5T$ where $T \sim Exp(2)$. Linear transformation of Exponential:

If $T \sim Exp(\lambda)$, then $cT \sim Exp(\lambda/c)$. So $Y = 5T \sim Exp(2/5) = Exp(0.4)$.

$E[Y] = 1/0.4 = \boxed{2.5 \text{ MB}}$

**b) Using the Exponential survival:
$$P(Y > 3) = e^{-0.4 \times 3} = e^{-1.2} \approx \boxed{0.3012}$$

**c) 95th percentile: $y_{0.95} = -\ln(1 - 0.95)/0.4 = -\ln(0.05)/0.4 = 2.996/0.4 \approx \boxed{7.49 \text{ MB}}$

#### Exercise 26: Erlang Queueing Analysis (Time-Domain)
**Problem:** A database server processes queries sequentially. Individual query times $X_i \sim Exp(\mu = 0.5 \text{ s}^{-1})$ (rate 0.5, mean 2 s each). A complex transaction requires 5 sequential queries. Find:
a) The distribution, mean, and variance of the total transaction time $T$.
b) The probability that the transaction completes within 15 seconds.
c) An R command to compute the probability in part b.

**Solution:**

**a) Sum of 5 i.i.d. $Exp(0.5)$ variables:
$$T \sim Erlang(k=5, \beta=0.5) = Gamma(5, 0.5)$$
$$E[T] = \frac{5}{0.5} = \boxed{10 \text{ s}}, \quad V(T) = \frac{5}{0.25} = \boxed{20 \text{ s}^2}$$

**b) CDF of $Gamma(5, 0.5)$ at $t = 15$:

Using R: `pgamma(15, shape = 5, rate = 0.5)` $\approx \boxed{0.7350}$

**c) R command:
```r
pgamma(q = 15, shape = 5, rate = 0.5)   # Probability transaction completes within 15 s
```

---

## Combined Exercises (Exercises 27-30)

#### Exercise 27: Multi-Distribution SLA Compliance Analysis (Combined, Moderate, Time-Domain)
**Problem:** A cloud function receives requests. Processing time per request $T \sim Exp(\lambda = 0.1 \text{ ms}^{-1})$ (rate 0.1, mean 10 ms). For complex requests, the total processing time is the sum of 3 independent identical stages: $T_{complex} = T_1 + T_2 + T_3$, each $\sim Exp(0.1)$.

a) Find the distribution, mean, and variance of $T_{complex}$.
b) Find $P(T_{complex} > 40 \text{ ms})$.
c) Find the 95th percentile $t_{SLA}$ using an R command.
d) If latency is measured in seconds (not ms), state the distribution of $T_{complex,[s]}$ using the $c^2$ rule.

**Solution:**

**a) Sum of 3 i.i.d. $Exp(0.1)$:
$$T_{complex} \sim Gamma(3, 0.1) = Erlang(3, 0.1)$$
$$E[T_{complex}] = \frac{3}{0.1} = 30 \text{ ms}, \quad V(T_{complex}) = \frac{3}{0.01} = 300 \text{ ms}^2$$

**b) Survival function for Gamma:
$$P(T_{complex} > 40) = 1 - P(T_{complex} \le 40)$$

Using the Gamma CDF: `1 - pgamma(40, shape = 3, rate = 0.1)` $\approx 1 - 0.7619 = \boxed{0.2381}$

**c) 95th percentile:
```r
qgamma(p = 0.95, shape = 3, rate = 0.1)  # Approximately 56.4 ms
```
$$t_{SLA} \approx \boxed{56.4 \text{ ms}}$$

**d) Converting to seconds with $c = 1/1000$:
$$\mu_{[s]} = 30/1000 = 0.03 \text{ s}, \quad \sigma^2_{[s]} = 300/10^6 = 3 \times 10^{-4} \text{ s}^2$$

The distribution remains $Gamma(3, \beta_{[s]})$ where the rate in s$^{-1}$ is $\beta_{[s]} = 0.1 \times 1000 = 100$.

$$T_{complex,[s]} \sim Gamma(3, 100) \text{ s}$$

#### Exercise 28: Normal and Exponential Joint System Analysis (Combined, Harder, Time-Domain)
**Problem:** A monitoring system tracks two independent metrics:
- CPU temperature $C \sim N(\mu_C = 60, \sigma^2_C = 25)$ degrees Celsius.
- Uptime between crashes $U \sim Exp(\lambda_U = 0.005 \text{ h}^{-1})$.

a) Find $P(C > 70)$ (thermal throttling threshold).
b) Find the 99th percentile of the CPU temperature.
c) Find $P(U < 24)$ (crashes within first 24 hours).
d) Given the server has been running for 100 hours, find $P(U > 124 \mid U > 100)$.
e) Find $P(C > 70 \text{ and } U < 24)$, assuming independence.
f) Provide the R commands for parts a and c.

**Solution:**

**a) $Z = (70 - 60)/5 = 2.00 \implies P(C > 70) = 1 - \Phi(2) = 1 - 0.9772 = \boxed{0.0228}$

**b) $z_{0.99} = 2.326 \implies c_{0.99} = 60 + 2.326 \times 5 = 60 + 11.63 = \boxed{71.63\text{°C}}$

**c) $P(U < 24) = 1 - e^{-0.005 \times 24} = 1 - e^{-0.12} \approx 1 - 0.8869 = \boxed{0.1131}$

**d) By the memoryless property of the Exponential:
$$P(U > 124 \mid U > 100) = P(U > 24) = e^{-0.12} \approx \boxed{0.8869}$$

**e) By independence:
$$P(C > 70 \text{ and } U < 24) = 0.0228 \times 0.1131 \approx \boxed{0.00258}$$

**f) R commands:
```r
# Part a: P(C > 70) where C ~ N(60, sigma=5)
pnorm(q = 70, mean = 60, sd = 5, lower.tail = FALSE)   # 0.0228

# Part c: P(U < 24) where U ~ Exp(rate = 0.005)
pexp(q = 24, rate = 0.005)                              # 0.1131
```

#### Exercise 29: Multi-Stage System with Transformations (Combined, Hard, Time-Domain)
**Problem:** A distributed computation pipeline has three independent phases:
- Phase A: Completion time $T_A \sim N(100, 400)$ ms ($\sigma_A = 20$ ms).
- Phase B: Completion time $T_B \sim Exp(0.02 \text{ ms}^{-1})$ (mean 50 ms).
- Phase C: Completion time $T_C \sim U(20, 80)$ ms.

Phases run sequentially. Total time $T_{total} = T_A + T_B + T_C$.

a) Find $E[T_{total}]$ and $V(T_{total})$.
b) Approximate $P(T_{total} > 220)$ using the Normal approximation.
c) State the direction of the inequality relating $E[1000/T_{total}]$ and $1000/E[T_{total}]$.
d) Find $V(T_{total,[s]})$ after converting to seconds.
e) Find $P(T_C > 60 \mid T_C > 50)$.

**Solution:**

**a) By linearity of expectation and independence:

$E[T_A] = 100$ ms, $V(T_A) = 400$ ms$^2$

$E[T_B] = 1/0.02 = 50$ ms, $V(T_B) = 1/0.02^2 = 2500$ ms$^2$

$E[T_C] = (20+80)/2 = 50$ ms, $V(T_C) = (80-20)^2/12 = 300$ ms$^2$

$$E[T_{total}] = 100 + 50 + 50 = \boxed{200 \text{ ms}}$$
$$V(T_{total}) = 400 + 2500 + 300 = \boxed{3200 \text{ ms}^2}, \quad \sigma_{total} \approx 56.57 \text{ ms}$$

**b) Approximating $T_{total} \approx N(200, 3200)$:

$$Z = \frac{220 - 200}{56.57} \approx 0.354 \implies P(T_{total} > 220) \approx 1 - \Phi(0.354) \approx 1 - 0.6384 \approx \boxed{0.3616}$$

**c) Since $g(t) = 1000/t$ is convex for $t > 0$, by Jensen's inequality:

$$E\!\left[\frac{1000}{T_{total}}\right] \ge \frac{1000}{E[T_{total}]} = 5 \text{ req/s}$$

The true average throughput is **strictly greater than** 5 requests per second.

**d) Converting to seconds with $c = 1/1000$:

$$V(T_{total,[s]}) = \left(\frac{1}{1000}\right)^2 \times 3200 = \frac{3200}{10^6} = \boxed{3.2 \times 10^{-3} \text{ s}^2}$$

**e) Conditional probability for Uniform (NOT memoryless):
$$P(T_C > 60 \mid T_C > 50) = \frac{P(T_C > 60)}{P(T_C > 50)} = \frac{(80-60)/60}{(80-50)/60} = \frac{20}{30} = \boxed{\frac{2}{3} \approx 0.6667}$$

The Uniform distribution is NOT memoryless, so $P(T_C > 60 \mid T_C > 50) \ne P(T_C > 10) = 10/60$.

#### Exercise 30: Full Phase Integration with Gotcha (Combined, Hardest + Gotcha, Time-Domain)
**Problem:** A network monitoring system records round-trip times (RTT) for packets. Historical data shows:

- RTT follows $T \sim N(\mu, \sigma^2)$.
- From percentile data: 10% of packets have RTT exceeding 75 ms, and 5% have RTT below 45 ms.
- The system samples 3 independent RTT measurements and records the total $S = T_1 + T_2 + T_3$.
- A junior engineer converts RTT to seconds and reports the variance as $\sigma^2 / 1000$.

Answer the following:

a) Solve for $\mu$ and $\sigma$ of the RTT distribution.
b) Find $P(60 \le T \le 75)$.
c) Find the distribution, mean, and variance of $S = T_1 + T_2 + T_3$.
d) Find $P(S > 200)$.
e) Find the 99th percentile of $S$ (for SLA planning).
f) Identify the junior engineer's error in reporting the variance after unit conversion, and provide the correct variance.

Given: $\Phi(1.282) = 0.90$, $\Phi(1.645) = 0.95$, $\Phi(2.326) = 0.99$.

**Solution:**

**a) Setting up the system of equations from the percentile conditions:

$P(T > 75) = 0.10 \implies P(T \le 75) = 0.90 \implies \frac{75 - \mu}{\sigma} = z_{0.90} = 1.282$

$P(T < 45) = 0.05 \implies \frac{45 - \mu}{\sigma} = z_{0.05} = -1.645$

System of equations:
$$75 = \mu + 1.282\sigma \quad (1)$$
$$45 = \mu - 1.645\sigma \quad (2)$$

Subtracting (2) from (1):
$$30 = (1.282 + 1.645)\sigma = 2.927\sigma \implies \sigma = \frac{30}{2.927} \approx \boxed{10.25 \text{ ms}}$$

Substituting into (1):
$$\mu = 75 - 1.282 \times 10.25 = 75 - 13.14 \approx \boxed{61.86 \text{ ms}}$$

**b) Standardize both bounds:
$$z_1 = \frac{60 - 61.86}{10.25} \approx -0.181, \quad z_2 = \frac{75 - 61.86}{10.25} \approx 1.282$$

$$P(60 \le T \le 75) = \Phi(1.282) - \Phi(-0.181) = 0.90 - (1 - \Phi(0.181)) \approx 0.90 - (1 - 0.5719) = \boxed{0.4719}$$

**c) Sum of 3 independent normals:
$$S = T_1 + T_2 + T_3 \sim N(3\mu, 3\sigma^2)$$
$$E[S] = 3 \times 61.86 = \boxed{185.58 \text{ ms}}$$
$$V(S) = 3 \times (10.25)^2 = 3 \times 105.06 = \boxed{315.18 \text{ ms}^2}, \quad \sigma_S \approx 17.75 \text{ ms}$$

**d) $P(S > 200)$:
$$Z = \frac{200 - 185.58}{17.75} \approx 0.812$$
$$P(S > 200) = 1 - \Phi(0.812) \approx 1 - 0.7917 = \boxed{0.2083}$$

**e) 99th percentile of $S$:
$$s_{0.99} = E[S] + z_{0.99} \times \sigma_S = 185.58 + 2.326 \times 17.75 = 185.58 + 41.29 \approx \boxed{226.87 \text{ ms}}$$

**f) Gotcha: The junior engineer's error in unit conversion of variance.**

The engineer reported the variance in seconds as $\sigma^2 / 1000$. This is **wrong**.

When converting from milliseconds to seconds with $c = 1/1000$, the $c^2$ rule states:
$$V(T_{[s]}) = c^2 \cdot V(T_{[ms]}) = \left(\frac{1}{1000}\right)^2 \cdot \sigma^2 = \frac{\sigma^2}{10^6} = \frac{\sigma^2}{1{,}000{,}000}$$

The engineer divided by $1000$ (i.e., applied $c$ scaling to the variance) instead of dividing by $10^6 = 1000^2$ (i.e., applying $c^2$ scaling). The reported variance is off by a factor of 1000.

**Correct variance in seconds:**
$$V(T_{[s]}) = \frac{(10.25)^2}{10^6} = \frac{105.06}{10^6} \approx 1.05 \times 10^{-4} \text{ s}^2$$

**Correct standard deviation in seconds:**
$$\sigma_{T_{[s]}} = \frac{10.25}{1000} = 0.01025 \text{ s}$$

**Gotcha:** The $c^2$ rule applies to variance (a quadratic quantity). The engineer incorrectly treated variance as a linear quantity by dividing by $c = 1000$ rather than $c^2 = 10^6$. This error propagates to all downstream calculations using the variance (confidence intervals, SLA thresholds, hypothesis tests). The standard deviation scales linearly by $c$, but the variance scales by $c^2$.

> **How to avoid this trap:** Always ask "is this a variance or a standard deviation?" before applying a unit conversion factor. Standard deviations scale linearly ($\sigma_{new} = c \cdot \sigma_{old}$), while variances scale quadratically ($\sigma^2_{new} = c^2 \cdot \sigma^2_{old}$). A mnemonic: variance is in squared units, so the conversion factor is also squared.

---

## Phase Summary

Phase 5 develops the complete toolkit for continuous probability distributions and random variable transformations. The **Normal distribution** $N(\mu, \sigma^2)$ is the foundation: the Z-score $Z = (X-\mu)/\sigma$ converts any normal probability to a standard normal lookup, and two percentile conditions yield a linear system that uniquely determines unknown parameters $\mu$ and $\sigma$. The **Empirical Rule** (68-95-99.7%) provides rapid tail probability estimates for symmetric distributions, but must never be applied to skewed distributions.

The **Continuous Uniform** $U(a,b)$ models equal-probability selection over an interval, with exact interval probabilities $(d-c)/(b-a)$. The **Exponential distribution** $Exp(\lambda)$ is the unique memoryless continuous distribution, modeling inter-arrival times in Poisson processes. Its memoryless property -- $P(T > s+t \mid T > s) = P(T > t)$ -- makes conditional survival calculations trivial, but it is a property exclusive to the Exponential (not Gamma, not Weibull with $k \ne 1$). The minimum of $n$ independent Exponentials is itself Exponential with summed rates.

The **Gamma/Erlang** family extends the Exponential to model the time until the $k$-th event. The Erlang requires identical rates across stages; mixing different rates breaks the Gamma structure. The **Weibull** distribution models non-constant failure hazard rates: $k < 1$ (infant mortality), $k = 1$ (memoryless Exponential), $k > 1$ (aging wear-out). The Weibull survival function $e^{-(t/\lambda)^k}$ is closed-form and exam-ready.

**Transformations** are handled by the Jacobian method for monotonic $g$ and the CDF method for non-monotonic $g$. The critical practical gotcha is **Jensen's inequality**: $E[1/T] > 1/E[T]$, so average throughput cannot be estimated as the reciprocal of average service time.

Four key exam traps pervade Phase 5: (1) the **$c^2$ rule** -- variance scales by $c^2$ on unit conversion, not by $c$; (2) the **memoryless exclusivity** -- only Exponential is memoryless; (3) the **R `pnorm()` trap** -- requires `sd`, not variance; and (4) the **Erlang rate requirement** -- all stages must share the same rate $\beta$.
