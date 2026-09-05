# Phase 4: Discrete Random Variables

## Table of Contents
- [Section 4.1: Discrete Random Variables, PMF/CDF, Expectation & Variance](#section-41-discrete-random-variables-pmfcdf-expectation--variance)
- [Section 4.2: Binomial & Poisson Distributions](#section-42-binomial--poisson-distributions)
- [Section 4.3: Geometric & Hypergeometric Distributions](#section-43-geometric--hypergeometric-distributions)
- [Section 4.4: Moment Generating Functions & Characteristic Functions](#section-44-moment-generating-functions--characteristic-functions)
- [Exam Preparation Guide](#exam-preparation-guide)
- [Phase Summary](#phase-summary)

---

## Section 4.1: Discrete Random Variables, PMF/CDF, Expectation & Variance

### Core Theory & Definitions

A **Random Variable (RV)** $X$ is a formal mathematical function that maps outcomes from a sample space $\Omega$ to real numbers ($X: \Omega \to \mathbb{R}$). A random variable is classified as **discrete** if its support $S_X = \{x \in \mathbb{R} : P(X = x) > 0\}$ is finite or countably infinite (such as the set of non-negative integers $\mathbb{N}_0$).

```
Sample Space $\Omega$ (Outcomes)   Real Line $R$ (Values)
+-----------------------+        +-------------------+
|  Outcome $\omega_1$ (Success) | ------>|  X($\omega_1$) = 1 |
|  Outcome $\omega_2$ (Failure) | ------>|  X($\omega_2$) = 0 |
+-----------------------+        +-------------------+
```

#### Probability Mass Function (PMF)
The probability distribution of a discrete random variable is specified by its **Probability Mass Function (PMF)**, denoted $p(x)$ or $P(X = x)$. The PMF assigns a probability to each possible value in the support and must satisfy two fundamental axiomatic validity conditions:

1. **Non-negativity:** $p(x) \ge 0$ for all $x \in S_X$, and $p(x) = 0$ for all $x \notin S_X$.
2. **Normalization:** $\sum_{x \in S_X} p(x) = 1$.

#### Cumulative Distribution Function (CDF)
The **Cumulative Distribution Function (CDF)**, denoted $F(x)$ or $F_X(x)$, measures the probability that $X$ takes on a value less than or equal to $x$:
$$F(x) = P(X \le x) = \sum_{k \le x} p(k)$$

For a discrete random variable, the CDF is a monotonic, non-decreasing, right-continuous step function. The steps occur precisely at the points in the support $S_X$, and the height of the jump at $x_k$ equals the PMF value $p(x_k) = F(x_k) - \lim_{t \to x_k^-} F(t)$.

#### Expected Value ($E[X]$) and LOTUS
The **Expected Value** (or population mean $\mu$) represents the probability-weighted long-run average of $X$:
$$E[X] = \mu = \sum_{x \in S_X} x \cdot p(x)$$
The expectation exists if and only if the sum converges absolutely ($\sum_{x} |x| p(x) < \infty$).

By the **Law of the Unconscious Statistician (LOTUS)**, the expected value of any real-valued function $g(X)$ of a discrete random variable is computed directly without finding the PMF of $g(X)$:
$$E[g(X)] = \sum_{x \in S_X} g(x) \cdot p(x)$$

#### Variance ($Var(X)$) and Standard Deviation ($\sigma$)
**Variance** measures the expected squared deviation of $X$ from its mean $\mu$, quantifying dispersion:
$$Var(X) = \sigma^2 = E[(X - \mu)^2] = E[X^2] - (E[X])^2$$
where $E[X^2] = \sum_{x \in S_X} x^2 \cdot p(x)$ is the second raw moment. The **Standard Deviation** is $\sigma = \sqrt{Var(X)}$.

#### Linear Properties of Expectation and Variance
For any real constants $a, b, c$ and discrete random variables $X, Y$:
1. **Linearity of Expectation:** $E[aX + bY + c] = a E[X] + b E[Y] + c$ (holds universally, regardless of independence).
2. **Linear Transformation of Variance:** $Var(aX + b) = a^2 Var(X)$ (additive constants do not change spread).
3. **Variance of Sum/Difference:** If $X$ and $Y$ are **statistically independent**, $Var(X \pm Y) = Var(X) + Var(Y)$.

> **Practical / Time-Domain Note:**
> In computer performance engineering and time-series measurement, discrete random variables model quantized latency buckets, discrete clock tick counts, packet retransmission attempts, or queue lengths.
> When scaling time units by a factor $c$ (e.g., converting seconds to milliseconds, $c = 1000$), the random variable transforms as $Y_{[ms]} = c \cdot X_{[s]}$.
> While the expected duration scales linearly ($E[Y_{[ms]}] = c \cdot E[X_{[s]}]$), the duration variance scales quadratically ($Var(Y_{[ms]}^2) = c^2 \cdot Var(X_{[s]}^2)$). This is known as the **$c^2$ variance scaling rule**.

---

### Mathematical Formulas & Derivations

#### 1. Fundamental PMF & CDF Formulas
$$\text{PMF Validity:} \quad p(x) \ge 0 \quad \text{and} \quad \sum_{x \in S_X} p(x) = 1$$
$$\text{Discrete CDF:} \quad F(x) = P(X \le x) = \sum_{k \le x} p(k)$$
$$\text{PMF from CDF:} \quad P(X = x_k) = F(x_k) - F(x_k^-)$$

#### 2. Expectation & Variance Formulas
$$\text{Expected Value (Mean):} \quad E[X] = \mu = \sum_{x \in S_X} x \cdot p(x)$$
$$\text{LOTUS:} \quad E[g(X)] = \sum_{x \in S_X} g(x) \cdot p(x)$$
$$\text{Computational Variance Formula:} \quad Var(X) = \sigma^2 = E[X^2] - (E[X])^2$$
$$\text{where} \quad E[X^2] = \sum_{x \in S_X} x^2 \cdot p(x)$$

#### 3. Linear Operator Derivations
*Proof of $Var(aX + b) = a^2 Var(X)$:*
Let $\mu = E[X]$. Then $E[aX + b] = a\mu + b$.
$$Var(aX + b) = E[\{(aX + b) - (a\mu + b)\}^2] = E[\{a(X - \mu)\}^2] = E[a^2 (X - \mu)^2] = a^2 E[(X - \mu)^2] = a^2 Var(X)$$

#### 4. Time-Domain Adapted Formulas (with Explicit Units)
For a discrete duration variable $T_{[s]}$ in seconds and linear transformation $Y_{[ms]} = c \cdot T_{[s]} + d_{[ms]}$ where $c = 1000\,[ms/s]$:
$$\text{Adapted Mean:} \quad E[Y_{[ms]}] = c_{[ms/s]} \cdot E[T_{[s]}] + d_{[ms]}$$
$$\text{Adapted Variance ($c^2$ rule):} \quad Var(Y_{[ms]}^2) = c_{[ms/s]}^2 \cdot Var(T_{[s]}^2) = 10^6 \cdot Var(T_{[s]}^2)$$
$$\text{Adapted Standard Deviation:} \quad \sigma_{Y,[ms]} = c_{[ms/s]} \cdot \sigma_{T,[s]} = 1000 \cdot \sigma_{T,[s]}$$

---

### Worked Exercises

#### Exercise 1: Discrete PMF Validation & Constant Determination
**Problem:** A discrete random variable $X$ has PMF given by $p(x) = c \cdot x$ for $x \in \{1, 2, 3, 4\}$ and $p(x) = 0$ otherwise.
**a) ** Determine the normalizing constant $c$.
**b) ** Compute the Cumulative Distribution Function $F(x)$ for all $x \in \mathbb{R}$.
**c) ** Compute the expected value $E[X]$ and variance $Var(X)$.

**Solution:**
**Step 1: Determine constant $c$ using normalization condition**
$$\sum_{x=1}^4 p(x) = 1 \implies c(1) + c(2) + c(3) + c(4) = 1 \implies 10c = 1 \implies c = 0.1$$
The valid PMF is $p(1) = 0.1, p(2) = 0.2, p(3) = 0.3, p(4) = 0.4$.

**Step 2: Construct CDF $F(x)$**
$$F(x) = \begin{cases} 0 & \text{if } x < 1 \\ 0.1 & \text{if } 1 \le x < 2 \\ 0.3 & \text{if } 2 \le x < 3 \\ 0.6 & \text{if } 3 \le x < 4 \\ 1.0 & \text{if } x \ge 4 \end{cases}$$

**Step 3: Compute $E[X]$ and $Var(X)$**
$$E[X] = \sum_{x=1}^4 x \cdot p(x) = (1 \cdot 0.1) + (2 \cdot 0.2) + (3 \cdot 0.3) + (4 \cdot 0.4) = 0.1 + 0.4 + 0.9 + 1.6 = 3.0$$
$$E[X^2] = \sum_{x=1}^4 x^2 \cdot p(x) = (1^2 \cdot 0.1) + (2^2 \cdot 0.2) + (3^2 \cdot 0.3) + (4^2 \cdot 0.4) = 0.1 + 0.8 + 2.7 + 6.4 = 10.0$$
$$Var(X) = E[X^2] - (E[X])^2 = 10.0 - (3.0)^2 = 10.0 - 9.0 = 1.0$$

Final Answer:
- **a) ** $c = 0.1$
- **b) ** $F(x)$ step function as defined above
- **c) ** $E[X] = 3.0$, $Var(X) = 1.0$

---

#### Exercise 2: Discrete Latency Bucket PMF & CDF Transformation (Time-Domain)
**Problem:** A cloud load balancer logs network request latencies into discrete time buckets $T \in \{5, 10, 15, 20\}\,[ms]$. The empirical PMF is $p(5) = 0.40, p(10) = 0.30, p(15) = 0.20, p(20) = 0.10$.
**a) ** Construct the CDF table for $T_{[ms]}$.
**b) ** Compute the probability that a request latency exceeds $10\,ms$, $P(T > 10\,ms)$.
**c) ** Calculate the expected latency $E[T_{[ms]}]$ and standard deviation $\sigma_{T,[ms]}$.

**Solution:**
**Step 1: Construct CDF $F_T(t)$**
- $F_T(5) = P(T \le 5) = 0.40$
- $F_T(10) = P(T \le 10) = 0.40 + 0.30 = 0.70$
- $F_T(15) = P(T \le 15) = 0.70 + 0.20 = 0.90$
- $F_T(20) = P(T \le 20) = 0.90 + 0.10 = 1.00$

**Step 2: Compute $P(T > 10\,ms)$**
$$P(T > 10\,ms) = 1 - P(T \le 10\,ms) = 1 - F_T(10) = 1 - 0.70 = 0.30$$

**Step 3: Calculate $E[T]$ and $\sigma_T$**
$$E[T_{[ms]}] = (5 \cdot 0.40) + (10 \cdot 0.30) + (15 \cdot 0.20) + (20 \cdot 0.10) = 2.0 + 3.0 + 3.0 + 2.0 = 10.0\,[ms]$$
$$E[T_{[ms]}^2] = (5^2 \cdot 0.40) + (10^2 \cdot 0.30) + (15^2 \cdot 0.20) + (20^2 \cdot 0.10) = 10.0 + 30.0 + 45.0 + 40.0 = 125.0\,[ms^2]$$
$$Var(T_{[ms]}^2) = 125.0 - (10.0)^2 = 125.0 - 100.0 = 25.0\,[ms^2]$$
$$\sigma_{T,[ms]} = \sqrt{25.0} = 5.0\,[ms]$$

Final Answer:
- **a) ** $F_T(5)=0.40, F_T(10)=0.70, F_T(15)=0.90, F_T(20)=1.00$
- **b) ** $P(T > 10\,ms) = 0.30$
- **c) ** $E[T] = 10.0\,[ms]$, $\sigma_T = 5.0\,[ms]$

---

#### Exercise 3: Expectation, LOTUS, and Variance of Dice Roll Winnings
**Problem:** In a carnival game, a player rolls a single fair 6-sided die ($X \in \{1, 2, 3, 4, 5, 6\}$). The payoff in dollars is given by $W = g(X) = X^2 - 3X$.
**a) ** Write out the PMF of $W$.
**b) ** Calculate the expected payoff $E[W]$ using LOTUS.
**c) ** Compute $Var(W)$.

**Solution:**
**Step 1: Compute payoff values $g(x)$ for each die outcome**
- $x = 1 \implies g(1) = 1^2 - 3(1) = -2$
- $x = 2 \implies g(2) = 2^2 - 3(2) = -2$
- $x = 3 \implies g(3) = 3^2 - 3(3) = 0$
- $x = 4 \implies g(4) = 4^2 - 3(4) = 4$
- $x = 5 \implies g(5) = 5^2 - 3(5) = 10$
- $x = 6 \implies g(6) = 6^2 - 3(6) = 18$

Each outcome has probability $p(x) = 1/6$.

**Step 2: Calculate $E[W]$ via LOTUS**
$$E[W] = \sum_{x=1}^6 (x^2 - 3x) \cdot \frac{1}{6} = \frac{-2 + (-2) + 0 + 4 + 10 + 18}{6} = \frac{28}{6} = \frac{14}{3} \approx 4.6667\,\text{dollars}$$

**Step 3: Compute $Var(W) = E[W^2] - (E[W])^2$**
Calculate $E[W^2]$ via LOTUS:
$$E[W^2] = \sum_{x=1}^6 (x^2 - 3x)^2 \cdot \frac{1}{6} = \frac{(-2)^2 + (-2)^2 + 0^2 + 4^2 + 10^2 + 18^2}{6} = \frac{4 + 4 + 0 + 16 + 100 + 324}{6} = \frac{448}{6} = \frac{224}{3} \approx 74.6667$$
$$Var(W) = \frac{224}{3} - \left(\frac{14}{3}\right)^2 = \frac{224}{3} - \frac{196}{9} = \frac{672 - 196}{9} = \frac{476}{9} \approx 52.8889\,\text{dollars}^2$$

Final Answer:
- **a) ** $W \in \{-2, 0, 4, 10, 18\}$ with $P(W=-2)=2/6, P(W=0)=1/6, P(W=4)=1/6, P(W=10)=1/6, P(W=18)=1/6$
- **b) ** $E[W] = 14/3 \approx 4.67\,\text{dollars}$
- **c) ** $Var(W) = 476/9 \approx 52.89\,\text{dollars}^2$

---

#### Exercise 4: Execution Duration Expectation, Variance, & Unit Scaling ($c^2$ rule) (Time-Domain)
**Problem:** An algorithm's execution duration $T_{[s]}$ in seconds has $E[T_{[s]}] = 0.050\,s$ and $Var(T_{[s]}^2) = 0.00040\,s^2$. The total system latency including fixed overhead $250\,\mu s$ converted to microseconds is $Y_{[\mu s]} = 10^6 \cdot T_{[s]} + 250$.
**a) ** Calculate expected latency $E[Y_{[\mu s]}]$.
**b) ** Calculate variance $Var(Y_{[\mu s]}^2)$ using the $c^2$ variance scaling rule.
**c) ** Calculate standard deviation $\sigma_{Y,[\mu s]}$ and convert it back to milliseconds.

**Solution:**
**Step 1: Compute $E[Y_{[\mu s]}]$**
$$E[Y_{[\mu s]}] = 10^6 \cdot E[T_{[s]}] + 250 = 10^6 (0.050) + 250 = 50,000 + 250 = 50,250\,[\mu s]$$

**Step 2: Compute $Var(Y_{[\mu s]}^2)$ using $c^2$ rule**
Here $c = 10^6\,[\mu s / s]$, so $c^2 = (10^6)^2 = 10^{12}$.
$$Var(Y_{[\mu s]}^2) = c^2 \cdot Var(T_{[s]}^2) = 10^{12} \cdot 0.00040 = 4.0 \times 10^8\,[\mu s^2]$$

**Step 3: Compute $\sigma_{Y,[\mu s]}$ and convert to $ms$**
$$\sigma_{Y,[\mu s]} = \sqrt{4.0 \times 10^8} = 20,000\,[\mu s]$$
Converting to milliseconds ($1\,ms = 1000\,\mu s$):
$$\sigma_{Y,[ms]} = \frac{20,000}{1000} = 20.0\,[ms]$$

Final Answer:
- **a) ** $E[Y] = 50,250\,[\mu s]$
- **b) ** $Var(Y) = 4.0 \times 10^8\,[\mu s^2]$
- **c) ** $\sigma_Y = 20,000\,[\mu s] = 20.0\,[ms]$

---

#### Exercise 5: Linear Combination of Independent Discrete Variables
**Problem:** Let $X$ and $Y$ be independent discrete random variables with $E[X] = 4, Var(X) = 2, E[Y] = 3, Var(Y) = 5$. Define $Z = 3X - 2Y + 5$.
**a) ** Compute $E[Z]$.
**b) ** Compute $Var(Z)$.
**c) ** Compute $E[Z^2]$.

**Solution:**
**Step 1: Compute $E[Z]$**
$$E[Z] = E[3X - 2Y + 5] = 3 E[X] - 2 E[Y] + 5 = 3(4) - 2(3) + 5 = 12 - 6 + 5 = 11$$

**Step 2: Compute $Var(Z)$ using independence of $X, Y$**
$$Var(Z) = Var(3X - 2Y + 5) = 3^2 Var(X) + (-2)^2 Var(Y) = 9(2) + 4(5) = 18 + 20 = 38$$

**Step 3: Compute $E[Z^2]$ using $Var(Z) = E[Z^2] - (E[Z])^2$**
$$E[Z^2] = Var(Z) + (E[Z])^2 = 38 + (11)^2 = 38 + 121 = 159$$

Final Answer:
- **a) ** $E[Z] = 11$
- **b) ** $Var(Z) = 38$
- **c) ** $E[Z^2] = 159$

---

#### Exercise 6: Multi-Server Latency Hop Sum & Variance Scaling (Time-Domain)
**Problem:** A database query traverses 3 independent microservice network hops with durations $T_1, T_2, T_3\,[ms]$ having expected values $E[T_1]=12\,ms, E[T_2]=25\,ms, E[T_3]=8\,ms$ and variances $Var(T_1)=9\,ms^2, Var(T_2)=16\,ms^2, Var(T_3)=4\,ms^2$. Total pipeline duration is $T = T_1 + T_2 + T_3$.
**a) ** Calculate expected total pipeline duration $E[T_{[ms]}]$.
**b) ** Calculate total variance $Var(T_{[ms]}^2)$ and standard deviation $\sigma_{T,[ms]}$.
**c) ** If network congestion causes hop 2 latency to scale by factor $1.5$ ($T_2' = 1.5 T_2$), compute new total variance $Var(T_{[ms]}'^{2})$.

**Solution:**
**Step 1: Compute $E[T]$**
$$E[T] = E[T_1] + E[T_2] + E[T_3] = 12 + 25 + 8 = 45\,[ms]$$

**Step 2: Compute $Var(T)$ and $\sigma_T$ using independence**
$$Var(T) = Var(T_1) + Var(T_2) + Var(T_3) = 9 + 16 + 4 = 29\,[ms^2]$$
$$\sigma_T = \sqrt{29} \approx 5.3852\,[ms]$$

**Step 3: Compute $Var(T')$ with scaled hop 2**
$$Var(T_2') = (1.5)^2 Var(T_2) = 2.25 \times 16 = 36\,[ms^2]$$
$$Var(T') = Var(T_1) + Var(T_2') + Var(T_3) = 9 + 36 + 4 = 49\,[ms^2]$$

Final Answer:
- **a) ** $E[T] = 45\,[ms]$
- **b) ** $Var(T) = 29\,[ms^2]$, $\sigma_T \approx 5.39\,[ms]$
- **c) ** New variance $Var(T') = 49\,[ms^2]$

---

#### Exercise 7: Discrete System Downtime Hours Expectation & Standard Deviation (Time-Domain)
**Problem:** Weekly maintenance downtime hours $D$ for a server cluster has PMF:
$p(0) = 0.60, p(1) = 0.25, p(2) = 0.10, p(3) = 0.05$.
**a) ** Compute expected weekly downtime hours $E[D_{[hr]}]$.
**b) ** Compute standard deviation $\sigma_{D,[hr]}$.
**c) ** If downtime costs $150 per hour plus a fixed setup penalty of $200 per week ($C = 150 D + 200$), calculate expected weekly cost $E[C]$ and cost standard deviation $\sigma_C$.

**Solution:**
**Step 1: Compute $E[D]$**
$$E[D_{[hr]}] = (0 \cdot 0.60) + (1 \cdot 0.25) + (2 \cdot 0.10) + (3 \cdot 0.05) = 0 + 0.25 + 0.20 + 0.15 = 0.60\,[hr]$$

**Step 2: Compute $Var(D)$ and $\sigma_D$**
$$E[D^2] = (0^2 \cdot 0.60) + (1^2 \cdot 0.25) + (2^2 \cdot 0.10) + (3^2 \cdot 0.05) = 0 + 0.25 + 0.40 + 0.45 = 1.10\,[hr^2]$$
$$Var(D) = 1.10 - (0.60)^2 = 1.10 - 0.36 = 0.74\,[hr^2]$$
$$\sigma_D = \sqrt{0.74} \approx 0.8602\,[hr]$$

**Step 3: Compute $E[C]$ and $\sigma_C$**
$$E[C] = 150 E[D] + 200 = 150(0.60) + 200 = 90 + 200 = \$290$$
$$\sigma_C = 150 \cdot \sigma_D = 150(0.8602) \approx \$129.03$$

Final Answer:
- **a) ** $E[D] = 0.60\,[hr]$
- **b) ** $\sigma_D \approx 0.86\,[hr]$
- **c) ** $E[C] = \$290$, $\sigma_C \approx \$129.03$

---

### R Implementation

```r
# Section 4.1: Discrete RV PMF, CDF, Expectation & Variance Calculations

# Define Support and PMF
x_vals <- c(1, 2, 3, 4)
pmf_vals <- c(0.1, 0.2, 0.3, 0.4)

# 1. PMF Validation Check
stopifnot(all(pmf_vals >= 0), abs(sum(pmf_vals) - 1.0) < 1e-9)

# 2. Cumulative Distribution Function (CDF)
cdf_vals <- cumsum(pmf_vals)
names(cdf_vals) <- paste0("P(X<=", x_vals, ")")
print(cdf_vals)

# 3. Expected Value E[X]
mean_X <- sum(x_vals * pmf_vals)

# 4. Variance Var(X) via LOTUS
mean_X2 <- sum((x_vals^2) * pmf_vals)
var_X <- mean_X2 - (mean_X^2)
sd_X <- sqrt(var_X)

cat(sprintf("E[X] = %.4f | Var(X) = %.4f | SD(X) = %.4f\n", mean_X, var_X, sd_X))

# 5. Linear Transformation & Unit Scaling (c^2 rule)
# Converting duration X (in seconds) to Y (in ms): Y = 1000*X + 250
c_scale <- 1000
mean_Y <- c_scale * mean_X + 250
var_Y <- (c_scale^2) * var_X
sd_Y <- c_scale * sd_X

cat(sprintf("E[Y_ms] = %.2f | Var(Y_ms) = %.2f | SD(Y_ms) = %.2f\n", mean_Y, var_Y, sd_Y))
```

---

## Section 4.2: Binomial & Poisson Distributions

### Core Theory & Definitions

#### 1. The Binomial Distribution ($Bin(n, p)$)
The **Binomial distribution** models the number of successes $X$ in a sequence of $n$ independent trials. It relies strictly on the **FINS** criteria:

1. **F**ixed number of trials $n$.
2. **I**ndependent trials.
3. **N**umber of outcomes per trial is binary (Success / Failure).
4. **S**ame probability of success $p$ across all trials ($q = 1 - p$).

The support is $S_X = \{0, 1, 2, \dots, n\}$. Its PMF is:
$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k \in \{0, 1, \dots, n\}$$
where $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ is the binomial coefficient.

**Mean and Variance:**
$$E[X] = n \cdot p, \quad Var(X) = n \cdot p \cdot (1-p)$$

**Additivity of Independent Binomials:**
If $X \sim Bin(n_1, p)$ and $Y \sim Bin(n_2, p)$ are independent with the *same* success probability $p$, then $X + Y \sim Bin(n_1 + n_2, p)$.

#### 2. The Poisson Distribution ($Poisson(\lambda)$)
The **Poisson distribution** models the count of rare events occurring within a specified continuous window (time or space) at a constant average rate $\lambda > 0$.

**Poisson Process Assumptions:**
- Events occur independently of each other.
- The average rate $\lambda$ is constant throughout the window.
- Two events cannot occur simultaneously at the exact same instant.

The support is countably infinite: $S_X = \{0, 1, 2, \dots\}$. Its PMF is:
$$P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}, \quad k = 0, 1, 2, \dots$$

**Mean and Variance (Equidispersion):**
$$E[X] = \lambda, \quad Var(X) = \lambda$$
In a true Poisson process, the mean always equals the variance.

#### Rate Scaling in Time Windows
If events occur at an hourly rate $\lambda_0$, then over a time window of duration $t$ hours, the Poisson parameter scales linearly:
$$\lambda_t = \lambda_0 \cdot t$$
The PMF for count $X_t$ in window $t$ becomes:
$$P(X_t = k) = \frac{(\lambda_0 t)^k e^{-\lambda_0 t}}{k!}$$

#### 3. Poisson Approximation to the Binomial Distribution
When the number of trials $n$ is very large and the success probability $p$ is very small, calculating binomial coefficients becomes computationally expensive. The Binomial distribution converges mathematically to a Poisson distribution with rate parameter $\lambda = n \cdot p$:
$$\lim_{n \to \infty, p \to 0, np = \lambda} \binom{n}{k} p^k (1-p)^{n-k} = \frac{\lambda^k e^{-\lambda}}{k!}$$

> **Standard Rule of Thumb for Approximation:**
> The Poisson approximation $Bin(n, p) \approx Poisson(\lambda = np)$ is valid when:
> $$n \ge 20 \quad \text{(or } n \ge 100\text{)} \quad \text{and} \quad p \le 0.05 \quad \text{(or } np \le 10\text{)}$$

---

### Mathematical Formulas & Derivations

#### 1. Binomial Expectation & Variance Derivation
Using the linear combination of $n$ independent Bernoulli indicator variables $X = \sum_{i=1}^n I_i$ where $P(I_i = 1) = p, P(I_i = 0) = 1-p$:
$$E[I_i] = 1(p) + 0(1-p) = p \implies E[X] = \sum_{i=1}^n E[I_i] = n \cdot p$$
$$Var(I_i) = E[I_i^2] - (E[I_i])^2 = p - p^2 = p(1-p)$$
$$Var(X) = \sum_{i=1}^n Var(I_i) = n \cdot p \cdot (1-p) \quad \text{(by independence)}$$

#### 2. Poisson Limit Proof from Binomial
Substitute $p = \frac{\lambda}{n}$ into the Binomial PMF:
$$P(X = k) = \frac{n!}{k!(n-k)!} \left(\frac{\lambda}{n}\right)^k \left(1 - \frac{\lambda}{n}\right)^{n-k} = \frac{\lambda^k}{k!} \cdot \left[ \frac{n(n-1)\cdots(n-k+1)}{n^k} \right] \cdot \left(1 - \frac{\lambda}{n}\right)^n \cdot \left(1 - \frac{\lambda}{n}\right)^{-k}$$
Taking the limit as $n \to \infty$:
- $\lim_{n \to \infty} \frac{n(n-1)\cdots(n-k+1)}{n^k} = 1$
- $\lim_{n \to \infty} \left(1 - \frac{\lambda}{n}\right)^n = e^{-\lambda}$
- $\lim_{n \to \infty} \left(1 - \frac{\lambda}{n}\right)^{-k} = 1$

Thus, $\lim_{n \to \infty} P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$.

#### 3. Time-Domain Adapted Formulas
For request arrival rate $\lambda_0\,[\text{events}/s]$ and measurement window $t_{[s]}$:
$$\lambda_{t,[s]} = \lambda_0 \cdot t_{[s]}$$
$$P(X_{t,[s]} = k) = \frac{(\lambda_0 t)^k e^{-\lambda_0 t}}{k!}$$
$$E[X_{t,[s]}] = Var(X_{t,[s]}) = \lambda_0 \cdot t_{[s]}$$

---

### Worked Exercises

#### Exercise 8: Manufacturing Defect Inspection Binomial Probability
**Problem:** A component manufacturing line produces items with a defect probability $p = 0.05$. An inspector draws a random sample of $n = 10$ components. Let $X \sim Bin(10, 0.05)$.
**a) ** Calculate the probability that zero components are defective.
**b) ** Calculate the probability that at least 2 components are defective.
**c) ** Compute the mean $E[X]$ and variance $Var(X)$.

**Solution:**
**Step 1: Compute $P(X = 0)$**
$$P(X = 0) = \binom{10}{0} (0.05)^0 (0.95)^{10} = 1 \cdot 1 \cdot (0.95)^{10} \approx 0.598737$$

**Step 2: Compute $P(X \ge 2)$ via complement rule**
$$P(X \ge 2) = 1 - P(X = 0) - P(X = 1)$$
$$P(X = 1) = \binom{10}{1} (0.05)^1 (0.95)^9 = 10 \cdot 0.05 \cdot 0.630249 = 0.315125$$
$$P(X \ge 2) = 1 - 0.598737 - 0.315125 = 0.086138 \approx 0.0861$$

**Step 3: Compute $E[X]$ and $Var(X)$**
$$E[X] = n \cdot p = 10 \cdot 0.05 = 0.50$$
$$Var(X) = n \cdot p \cdot (1-p) = 10 \cdot 0.05 \cdot 0.95 = 0.475$$

Final Answer:
- **a) ** $P(X = 0) \approx 0.5987$
- **b) ** $P(X \ge 2) \approx 0.0861$
- **c) ** $E[X] = 0.50$, $Var(X) = 0.475$

---

#### Exercise 9: API Request Retry Limit & SLA Binomial Compliance (Time-Domain)
**Problem:** An application issues $n = 20$ independent network requests to a microservice. Each request has a success probability $p = 0.90$.
**a) ** Compute the probability that all 20 requests succeed.
**b) ** Compute the probability that at least 18 requests succeed ($P(X \ge 18)$).
**c) ** Provide the R command to calculate $P(X \ge 18)$.

**Solution:**
**Step 1: Compute $P(X = 20)$**
$$P(X = 20) = \binom{20}{20} (0.90)^{20} (0.10)^0 = (0.90)^{20} \approx 0.121577 \approx 0.1216$$

**Step 2: Compute $P(X \ge 18) = P(X=18) + P(X=19) + P(X=20)$**
$$P(X = 19) = \binom{20}{19} (0.90)^{19} (0.10)^1 = 20 \cdot 0.135085 \cdot 0.10 = 0.270170$$
$$P(X = 18) = \binom{20}{18} (0.90)^{18} (0.10)^2 = 190 \cdot 0.150095 \cdot 0.01 = 0.285180$$
$$P(X \ge 18) = 0.285180 + 0.270170 + 0.121577 = 0.676927 \approx 0.6769$$

**Step 3: R command**
`pbinom(17, size = 20, prob = 0.90, lower.tail = FALSE)` or `1 - pbinom(17, 20, 0.90)` or `sum(dbinom(18:20, 20, 0.90))`.

Final Answer:
- **a) ** $P(X = 20) \approx 0.1216$
- **b) ** $P(X \ge 18) \approx 0.6769$
- **c) ** `pbinom(17, size = 20, prob = 0.90, lower.tail = FALSE)`

---

#### Exercise 10: Minimum Sample Size Binomial Logarithm Inequality
**Problem:** In a semiconductor batch, component defect probability is $p = 0.02$. How many items $n$ must be sampled so that the probability of detecting at least one defect is at least $95\%$ ($0.95$)?

**Solution:**
**Step 1: Set up the inequality**
$$P(X \ge 1) = 1 - P(X = 0) = 1 - (1 - p)^n \ge 0.95$$
$$1 - (0.98)^n \ge 0.95 \implies (0.98)^n \le 0.05$$

**Step 2: Apply natural logarithms**
$$n \cdot \ln(0.98) \le \ln(0.05)$$
Since $\ln(0.98) \approx -0.0202027 < 0$, dividing by $\ln(0.98)$ reverses the inequality:
$$n \ge \frac{\ln(0.05)}{\ln(0.98)} = \frac{-2.995732}{-0.0202027} \approx 148.284$$

**Step 3: Round up to nearest integer**
$n = 149$ components.

Final Answer:
Minimum sample size $n = 149$ components.

---

#### Exercise 11: High-Throughput Web Request Failure Binomial Trial Size (Time-Domain)
**Problem:** A telemetry system experiences packet drop probability $p_{\text{drop}} = 0.08$ per transmission attempt. Find the minimum number of attempts $n$ required so that the probability of at least one successful delivery is at least $99.9\%$ ($0.999$).

**Solution:**
**Step 1: Set up inequality for success**
$P(\text{at least 1 success}) = 1 - P(\text{all } n \text{ dropped}) = 1 - (p_{\text{drop}})^n \ge 0.999$
$$1 - (0.08)^n \ge 0.999 \implies (0.08)^n \le 0.001$$

**Step 2: Solve using logarithms**
$$n \cdot \ln(0.08) \le \ln(0.001)$$
Since $\ln(0.08) \approx -2.525729 < 0$:
$$n \ge \frac{\ln(0.001)}{\ln(0.08)} = \frac{-6.907755}{-2.525729} \approx 2.73496$$

**Step 3: Round up to integer**
$n = 3$ attempts.

Final Answer:
Minimum attempts required $n = 3$.

---

#### Exercise 12: Conditional Binomial Probability given Minimum Successes
**Problem:** Let $X \sim Bin(n=5, p=0.40)$. Calculate the conditional probability $P(X = 3 \mid X \ge 2)$.

**Solution:**
**Step 1: Use conditional probability definition**
$$P(X = 3 \mid X \ge 2) = \frac{P(\{X = 3\} \cap \{X \ge 2\})}{P(X \ge 2)} = \frac{P(X = 3)}{P(X \ge 2)}$$

**Step 2: Compute $P(X = 3)$**
$$P(X = 3) = \binom{5}{3} (0.40)^3 (0.60)^2 = 10 \cdot 0.064 \cdot 0.36 = 0.2304$$

**Step 3: Compute $P(X \ge 2)$ via complement**
$$P(X = 0) = (0.60)^5 = 0.07776$$
$$P(X = 1) = \binom{5}{1} (0.40)^1 (0.60)^4 = 5 \cdot 0.40 \cdot 0.1296 = 0.2592$$
$$P(X \ge 2) = 1 - 0.07776 - 0.2592 = 0.66304$$

**Step 4: Compute conditional probability**
$$P(X = 3 \mid X \ge 2) = \frac{0.2304}{0.66304} \approx 0.34749 \approx 0.3475$$

Final Answer:
$P(X = 3 \mid X \ge 2) \approx 0.3475$ (or $34.75\%$).

---

#### Exercise 13: Microservice Cluster Packet Loss Conditional Binomial (Time-Domain)
**Problem:** A microservice transmits a batch of $n = 6$ packets with drop probability $p = 0.15$. Let $X$ be the count of dropped packets. Find $P(X = 1 \mid X \le 2)$.

**Solution:**
**Step 1: Compute PMF values for $X = 0, 1, 2$**
$$P(X = 0) = (0.85)^6 \approx 0.377150$$
$$P(X = 1) = \binom{6}{1} (0.15)^1 (0.85)^5 = 6 \cdot 0.15 \cdot 0.443705 = 0.399335$$
$$P(X = 2) = \binom{6}{2} (0.15)^2 (0.85)^4 = 15 \cdot 0.0225 \cdot 0.522006 = 0.176177$$

**Step 2: Compute denominator $P(X \le 2)$**
$$P(X \le 2) = 0.377150 + 0.399335 + 0.176177 = 0.952662$$

**Step 3: Compute conditional probability**
$$P(X = 1 \mid X \le 2) = \frac{P(X = 1)}{P(X \le 2)} = \frac{0.399335}{0.952662} \approx 0.419178 \approx 0.4192$$

Final Answer:
$P(X = 1 \mid X \le 2) \approx 0.4192$.

---

#### Exercise 14: Call Center Hourly Arrivals Poisson Distribution
**Problem:** Calls arrive at a support desk at a Poisson rate $\lambda = 6$ calls per hour.
**a) ** Calculate the probability of receiving exactly 4 calls in a 1-hour window.
**b) ** Calculate the probability of receiving zero calls in a 30-minute window ($t = 0.5\,hr$).

**Solution:**
**Step 1: Compute $P(X = 4)$ for $\lambda = 6$**
$$P(X = 4) = \frac{6^4 e^{-6}}{4!} = \frac{1296 \cdot e^{-6}}{24} = 54 e^{-6} \approx 54(0.00247875) \approx 0.133853 \approx 0.1339$$

**Step 2: Scale rate for 30-minute window ($t = 0.5\,hr$)**
$$\lambda_{30m} = \lambda_0 \cdot t = 6 \times 0.5 = 3.0$$
$$P(X_{30m} = 0) = \frac{3^0 e^{-3}}{0!} = e^{-3} \approx 0.049787 \approx 0.0498$$

Final Answer:
- **a) ** $P(X = 4) \approx 0.1339$
- **b) ** $P(X_{30m} = 0) \approx 0.0498$

---

#### Exercise 15: Server Log Anomaly Rate Scaling across Time Windows (Time-Domain)
**Problem:** Error anomalies are logged at a rate of $\lambda_0 = 120$ errors per hour.
**a) ** Determine the scaled Poisson rate $\lambda_{5m}$ for a 5-minute window.
**b) ** Compute the probability of logging exactly 10 errors in a 5-minute window.
**c) ** State the mean and standard deviation of errors in a 5-minute window.

**Solution:**
**Step 1: Scale rate for 5 minutes ($t = 5/60 = 1/12\,hr$)**
$$\lambda_{5m} = 120 \cdot \frac{5}{60} = 10.0\,\text{errors}$$

**Step 2: Compute $P(X_{5m} = 10)$**
$$P(X_{5m} = 10) = \frac{10^{10} e^{-10}}{10!} = \frac{10,000,000,000 \cdot e^{-10}}{3,628,800} \approx 2755.7319 \cdot (0.00004540) \approx 0.125110$$

**Step 3: Mean and Standard Deviation**
$$E[X_{5m}] = \lambda_{5m} = 10.0, \quad Var(X_{5m}) = 10.0 \implies \sigma = \sqrt{10} \approx 3.1623\,\text{errors}$$

Final Answer:
- **a) ** $\lambda_{5m} = 10.0$
- **b) ** $P(X_{5m} = 10) \approx 0.1251$
- **c) ** Mean $= 10.0$, $\sigma \approx 3.16\,\text{errors}$

---

#### Exercise 16: Rare Disease Prevalence Binomial-to-Poisson Approximation
**Problem:** A medical test screens $n = 1000$ individuals for a rare condition with prevalence $p = 0.003$.
**a) ** Verify that the Poisson approximation is justified.
**b) ** Calculate the approximate probability that exactly 2 individuals test positive.
**c) ** Compute the approximate probability that at least 1 individual tests positive.

**Solution:**
**Step 1: Verify approximation criteria**
$n = 1000 \ge 100$ and $p = 0.003 \le 0.05$. $np = 1000(0.003) = 3.0 \le 10$. Criteria satisfied! Use $Poisson(\lambda = 3.0)$.

**Step 2: Compute $P(X = 2)$ via Poisson**
$$P(X = 2) \approx \frac{3^2 e^{-3}}{2!} = \frac{9 e^{-3}}{2} = 4.5 e^{-3} \approx 4.5(0.049787) \approx 0.224042 \approx 0.2240$$

**Step 3: Compute $P(X \ge 1)$**
$$P(X \ge 1) = 1 - P(X = 0) \approx 1 - e^{-3} = 1 - 0.049787 = 0.950213 \approx 0.9502$$

Final Answer:
- **a) ** Approximation valid ($n=1000 \ge 100, p=0.003 \le 0.05, \lambda=3.0$)
- **b) ** $P(X = 2) \approx 0.2240$
- **c) ** $P(X \ge 1) \approx 0.9502$

---

#### Exercise 17: Memory Leak Fault Occurrences via Poisson Approximation (Time-Domain)
**Problem:** A cloud deployment runs $n = 500$ container instances. Each instance has an hourly crash probability $p = 0.004$ due to memory leaks.
**a) ** Using Poisson approximation, calculate the probability of exactly 3 container crashes in a 1-hour window.
**b) ** Calculate the probability of at most 1 crash in a 2-hour window ($t = 2\,hr$).

**Solution:**
**Step 1: Hourly Poisson rate**
$\lambda_1 = n \cdot p = 500 \cdot 0.004 = 2.0$ crashes/hour.

**Step 2: Compute $P(X_1 = 3)$ for 1 hour**
$$P(X_1 = 3) = \frac{2^3 e^{-2}}{3!} = \frac{8 e^{-2}}{6} = \frac{4}{3} e^{-2} \approx 1.33333 \cdot 0.135335 \approx 0.180447 \approx 0.1804$$

**Step 3: Compute $P(X_2 \le 1)$ for 2 hours ($\lambda_2 = 2.0 \times 2 = 4.0$)**
$$P(X_2 \le 1) = P(X_2 = 0) + P(X_2 = 1) = \frac{4^0 e^{-4}}{0!} + \frac{4^1 e^{-4}}{1!} = e^{-4} + 4e^{-4} = 5e^{-4}$$
$$5e^{-4} \approx 5(0.0183156) = 0.091578 \approx 0.0916$$

Final Answer:
- **a) ** $P(X_1 = 3) \approx 0.1804$
- **b) ** $P(X_2 \le 1) \approx 0.0916$

---

### R Implementation

```r
# Section 4.2: Binomial & Poisson Distribution R Commands

# 1. Binomial Distribution: B(n=20, p=0.90)
n_bin <- 20; p_bin <- 0.90
dbinom_exact <- dbinom(18, size = n_bin, prob = p_bin)   # P(X = 18)
pbinom_tail <- pbinom(17, size = n_bin, prob = p_bin, lower.tail = FALSE) # P(X >= 18)

cat(sprintf("Binomial P(X=18) = %.4f | P(X>=18) = %.4f\n", dbinom_exact, pbinom_tail))

# 2. Poisson Distribution & Rate Scaling: Poisson(lambda_hourly = 120)
lambda_hr <- 120
lambda_5m <- lambda_hr * (5 / 60) # Scaled to 10

dpois_exact <- dpois(10, lambda = lambda_5m)             # P(X = 10 in 5m)
ppois_cum <- ppois(10, lambda = lambda_5m)               # P(X <= 10 in 5m)

cat(sprintf("Poisson P(X_5m = 10) = %.4f | P(X_5m <= 10) = %.4f\n", dpois_exact, ppois_cum))

# 3. Poisson Approximation to Binomial: B(n=1000, p=0.003) vs Poisson(lambda=3)
exact_binom <- dbinom(2, size = 1000, prob = 0.003)
approx_pois  <- dpois(2, lambda = 3.0)

cat(sprintf("Exact Binomial: %.6f | Poisson Approx: %.6f | Diff: %.6f\n",
            exact_binom, approx_pois, abs(exact_binom - approx_pois)))
```

---

## Section 4.3: Geometric & Hypergeometric Distributions

### Core Theory & Definitions

#### 1. The Geometric Distribution ($Geo(p)$)
The **Geometric distribution** models the number of independent Bernoulli trials required until observing the **first success**, where each trial has success probability $p \in (0, 1]$.

There are two standard textbook definitions of the Geometric distribution:

```
Definition A (Trials Count X):     [ F ] [ F ] [ F ] [ S ]   --> X = 4 trials
Definition B (Failures Count Y):   [ F ] [ F ] [ F ]         --> Y = 3 failures
```

| Property | Definition A (Total Trials $X$) | Definition B (Failures $Y = X - 1$) |
| :--- | :--- | :--- |
| **Support $S$** | $S_X = \{1, 2, 3, \dots\}$ | $S_Y = \{0, 1, 2, \dots\}$ |
| **PMF** | $P(X = k) = (1-p)^{k-1} p$ | $P(Y = k) = (1-p)^k p$ |
| **CDF** | $F_X(k) = 1 - (1-p)^k$ | $F_Y(k) = 1 - (1-p)^{k+1}$ |
| **Mean $E[\cdot]$** | $E[X] = \frac{1}{p}$ | $E[Y] = \frac{1-p}{p}$ |
| **Variance $Var(\cdot)$** | $Var(X) = \frac{1-p}{p^2}$ | $Var(Y) = \frac{1-p}{p^2}$ |

> **Critical R Parameterization Gotcha:**
> R's built-in functions (`dgeom`, `pgeom`, `qgeom`, `rgeom`) strictly implement **Definition B** (counting failures $Y$ before first success).
> To evaluate $P(X = k)$ under Definition A (trials), you must pass `x = k - 1` to `dgeom`!

#### The Memoryless Property
The Geometric distribution is the **only** discrete distribution possessing the **Memoryless Property**. Given that no success has occurred in the first $k$ trials, the conditional probability of requiring more than $k + s$ trials depends only on $s$, completely forgetting the past $k$ failures:
$$P(X > k + s \mid X > k) = P(X > s) = (1-p)^s$$

#### 2. The Hypergeometric Distribution ($HG(N, K, n)$)
The **Hypergeometric distribution** models sampling **without replacement** from a finite population of size $N$ containing $K$ success items and $N - K$ failure items, drawing a sample of size $n$.

Because draws are without replacement, trials are **dependent**, violating the Binomial assumptions.

The support is $\max(0, n - (N - K)) \le k \le \min(n, K)$. Its PMF is:
$$P(X = k) = \frac{\binom{K}{k} \binom{N - K}{n - k}}{\binom{N}{n}}$$

**Mean and Variance:**
$$E[X] = n \cdot \frac{K}{N}$$
$$Var(X) = n \cdot \frac{K}{N} \cdot \left(1 - \frac{K}{N}\right) \cdot \left( \frac{N - n}{N - 1} \right)$$
The term $\frac{N - n}{N - 1}$ is the **Finite Population Correction (FPC)** factor, which reduces variance compared to Binomial sampling.

#### Binomial Approximation to Hypergeometric
When the sample size $n$ is small relative to the population $N$ ($n/N \le 0.05$ or $N \ge 10n$), the effect of sampling without replacement is negligible. The Hypergeometric distribution can be accurately approximated by $Bin(n, p = K/N)$, and the FPC factor $\frac{N-n}{N-1} \approx 1$.

---

### Mathematical Formulas & Derivations

#### 1. Geometric CDF & Survival Derivation (Def A)
$$P(X > k) = \sum_{j=k+1}^{\infty} (1-p)^{j-1} p = p (1-p)^k \sum_{m=0}^{\infty} (1-p)^m = p (1-p)^k \cdot \frac{1}{1 - (1-p)} = (1-p)^k$$
$$F_X(k) = P(X \le k) = 1 - P(X > k) = 1 - (1-p)^k$$

#### 2. Proof of Memoryless Property
$$P(X > k + s \mid X > k) = \frac{P(X > k + s \cap X > k)}{P(X > k)} = \frac{P(X > k + s)}{P(X > k)} = \frac{(1-p)^{k+s}}{(1-p)^k} = (1-p)^s = P(X > s)$$

#### 3. Hypergeometric Mean Derivation
Let $X = \sum_{i=1}^n I_i$ where $I_i = 1$ if the $i$-th drawn item is a success. By symmetry, $P(I_i = 1) = K/N$ for all $i$:
$$E[X] = \sum_{i=1}^n E[I_i] = \sum_{i=1}^n \frac{K}{N} = n \cdot \frac{K}{N}$$

---

### Worked Exercises

#### Exercise 18: Quality Control Inspection Geometric Trial Count
**Problem:** In a quality control process, component inspection has a defect probability $p = 0.12$ per item. Let $X \sim Geo(0.12)$ under Definition A (total trials).
**a) ** Calculate the probability that the first defect occurs on the 5th inspection.
**b) ** Calculate expected trials $E[X]$ and variance $Var(X)$.
**c) ** Compute $P(X > 4)$.

**Solution:**
**Step 1: Compute $P(X = 5)$**
$$P(X = 5) = (1 - 0.12)^{5-1} (0.12) = (0.88)^4 (0.12) = (0.599695) (0.12) \approx 0.071963 \approx 0.0720$$

**Step 2: Compute $E[X]$ and $Var(X)$**
$$E[X] = \frac{1}{p} = \frac{1}{0.12} \approx 8.3333\,\text{inspections}$$
$$Var(X) = \frac{1 - p}{p^2} = \frac{0.88}{(0.12)^2} = \frac{0.88}{0.0144} \approx 61.1111$$

**Step 3: Compute $P(X > 4)$**
$$P(X > 4) = (1 - p)^4 = (0.88)^4 \approx 0.5997$$

Final Answer:
- **a) ** $P(X = 5) \approx 0.0720$
- **b) ** $E[X] \approx 8.33$, $Var(X) \approx 61.11$
- **c) ** $P(X > 4) \approx 0.5997$

---

#### Exercise 19: Discrete Time-Slot Buffer Polling & Memoryless Property (Time-Domain)
**Problem:** A network buffer polls for incoming packets every $10\,ms$ time slot. Success probability per slot is $p = 0.25$.
**a) ** Calculate the probability that polling takes more than 4 slots ($T > 4$).
**b) ** Given that no packet arrived in the first 6 slots ($T > 6$), compute the conditional probability that the first packet arrives on the 9th slot ($P(T = 9 \mid T > 6)$).

**Solution:**
**Step 1: Compute $P(T > 4)$**
$$P(T > 4) = (1 - 0.25)^4 = (0.75)^4 = 0.316406 \approx 0.3164$$

**Step 2: Apply Memoryless Property for $P(T = 9 \mid T > 6)$**
By memorylessness, conditioning on $T > 6$ resets the trial counter by 6:
$$P(T = 9 \mid T > 6) = P(T = 9 - 6) = P(T = 3)$$
$$P(T = 3) = (1 - 0.25)^{3-1} (0.25) = (0.75)^2 (0.25) = 0.5625 \cdot 0.25 = 0.140625 \approx 0.1406$$

Final Answer:
- **a) ** $P(T > 4) \approx 0.3164$
- **b) ** $P(T = 9 \mid T > 6) \approx 0.1406$

---

#### Exercise 20: Comparison of Geometric Definition A (Trials) vs Definition B (Failures)
**Problem:** A hardware probe retries connection attempts with success probability $p = 0.20$.
**a) ** Under Def A ($X$ = total attempts), state $E[X]$ and $Var(X)$.
**b) ** Under Def B ($Y$ = failures before first success), state $E[Y]$ and $Var(Y)$.
**c) ** Verify that $Var(X) = Var(Y)$ and explain why expectations differ by 1.

**Solution:**
**Step 1: Def A parameters**
$$E[X] = \frac{1}{0.20} = 5.0, \quad Var(X) = \frac{1 - 0.20}{(0.20)^2} = \frac{0.80}{0.04} = 20.0$$

**Step 2: Def B parameters**
$$E[Y] = \frac{1 - 0.20}{0.20} = \frac{0.80}{0.20} = 4.0, \quad Var(Y) = \frac{1 - 0.20}{(0.20)^2} = 20.0$$

**Step 3: Verification**
Since $Y = X - 1$, by linear operator rules $E[Y] = E[X] - 1 = 5.0 - 1 = 4.0$.
For variance, subtracting a constant $1$ does not change dispersion: $Var(Y) = Var(X - 1) = 1^2 Var(X) = 20.0$.

Final Answer:
- **a) ** Def A: $E[X] = 5.0, Var(X) = 20.0$
- **b) ** Def B: $E[Y] = 4.0, Var(Y) = 20.0$
- **c) ** Expectations differ by 1 because $X = Y + 1$; variances are identical because shift is constant.

---

#### Exercise 21: Network Packet Transmission Attempts with Maximum Retry Threshold (Time-Domain)
**Problem:** A wireless sender retries sending a frame with per-slot success probability $p = 0.40$. The system gives up after a maximum of $n = 4$ slots (attempts $1, 2, 3, 4$).
**a) ** Calculate the probability that transmission is aborted ($T > 4$).
**b) ** Calculate the probability of successful transmission within the threshold ($T \le 4$).
**c) ** Write the R command to calculate $P(T \le 4)$.

**Solution:**
**Step 1: Compute abortion probability $P(T > 4)$**
$$P(T > 4) = (1 - 0.40)^4 = (0.60)^4 = 0.1296$$

**Step 2: Compute success probability $P(T \le 4)$**
$$P(T \le 4) = 1 - P(T > 4) = 1 - 0.1296 = 0.8704$$

**Step 3: R command**
Since R uses Def B ($Y = X - 1$), $T \le 4$ corresponds to $Y \le 3$ failures:
`pgeom(3, prob = 0.40)`

Final Answer:
- **a) ** $P(T > 4) = 0.1296$
- **b) ** $P(T \le 4) = 0.8704$
- **c) ** `pgeom(3, prob = 0.40)`

---

#### Exercise 22: Lottery Ticket Sampling Without Replacement Hypergeometric
**Problem:** An urn contains $N = 40$ lottery tickets, of which $K = 8$ are winning tickets. A participant draws $n = 5$ tickets without replacement. Let $X \sim HG(N=40, K=8, n=5)$.
**a) ** Calculate the probability of drawing exactly 2 winning tickets.
**b) ** Calculate expected winning tickets $E[X]$.
**c) ** Compute variance $Var(X)$.

**Solution:**
**Step 1: Compute $P(X = 2)$**
$$P(X = 2) = \frac{\binom{8}{2} \binom{32}{3}}{\binom{40}{5}} = \frac{28 \cdot 4960}{658008} = \frac{138880}{658008} \approx 0.211061 \approx 0.2111$$

**Step 2: Compute $E[X]$**
$$E[X] = n \cdot \frac{K}{N} = 5 \cdot \frac{8}{40} = 5 \cdot 0.20 = 1.0\,\text{ticket}$$

**Step 3: Compute $Var(X)$**
$$Var(X) = n \cdot \frac{K}{N} \cdot \left(1 - \frac{K}{N}\right) \cdot \left(\frac{N-n}{N-1}\right) = 5 \cdot 0.20 \cdot 0.80 \cdot \left(\frac{35}{39}\right) = 0.80 \cdot 0.897436 \approx 0.717949 \approx 0.7179$$

Final Answer:
- **a) ** $P(X = 2) \approx 0.2111$
- **b) ** $E[X] = 1.0$
- **c) ** $Var(X) \approx 0.7179$

---

#### Exercise 23: Hardware Server Faulty Module Audit via Hypergeometric (Time-Domain)
**Problem:** A server rack contains $N = 50$ blades, of which $K = 6$ have failing memory modules. An auditor inspects $n = 10$ blades without replacement.
**a) ** Calculate the probability of finding exactly 1 faulty blade.
**b) ** Provide the R command to calculate this exact probability.

**Solution:**
**Step 1: Compute $P(X = 1)$**
$$P(X = 1) = \frac{\binom{6}{1} \binom{44}{9}}{\binom{50}{10}} = \frac{6 \cdot 707234040}{10272278170} = \frac{4243404240}{10272278170} \approx 0.413093 \approx 0.4131$$

**Step 2: R command**
In R `dhyper(x, m, n, k)` uses:
- `x`: target count $= 1$
- `m`: total successes $K = 6$
- `n`: total failures $N - K = 44$
- `k`: sample size $n = 10$

Command: `dhyper(1, m = 6, n = 44, k = 10)`

Final Answer:
- **a) ** $P(X = 1) \approx 0.4131$
- **b) ** `dhyper(1, m = 6, n = 44, k = 10)`

---

#### Exercise 24: Large Population Binomial Approximation to Hypergeometric
**Problem:** A warehouse contains $N = 2000$ components, $K = 100$ of which are defective ($p = K/N = 0.05$). An engineer samples $n = 20$ components without replacement.
**a) ** Check if the Binomial approximation is justified.
**b) ** Compute $P(X = 0)$ using the Binomial approximation and compare with exact Hypergeometric.

**Solution:**
**Step 1: Check ratio $n/N$**
$$\frac{n}{N} = \frac{20}{2000} = 0.01 \le 0.05$$
Since $0.01 \le 0.05$, the Binomial approximation $Bin(20, 0.05)$ is valid!

**Step 2: Compute approximate $P(X = 0)$ via Binomial**
$$P(X = 0)_{\text{Bin}} = \binom{20}{0} (0.05)^0 (0.95)^{20} = (0.95)^{20} \approx 0.358486 \approx 0.3585$$

**Step 3: Exact Hypergeometric comparison**
$$P(X = 0)_{\text{HG}} = \frac{\binom{100}{0} \binom{1900}{20}}{\binom{2000}{20}} \approx 0.357989$$
Difference is only $0.000497$ ($< 0.05\%$).

Final Answer:
- **a) ** Approximation justified ($n/N = 0.01 \le 0.05$)
- **b) ** Binomial $P(X=0) \approx 0.3585$ (Exact HG $\approx 0.3580$)

---

#### Exercise 25: Large Data Cluster Log Inspection HG vs Binomial (Time-Domain)
**Problem:** A database cluster generates $N = 10,000$ log files per day, $K = 500$ of which record query timeout errors ($p = 0.05$). An automated parser inspects $n = 50$ logs without replacement.
**a) ** Is Binomial approximation justified?
**b) ** Compare expected values and variances under exact Hypergeometric versus Binomial approximation.

**Solution:**
**Step 1: Check $n/N$**
$$\frac{n}{N} = \frac{50}{10000} = 0.005 \le 0.05 \quad \text{(Justified!)}$$

**Step 2: Compare Expectations**
$$E[X]_{\text{Bin}} = n \cdot p = 50 \times 0.05 = 2.50\,\text{logs}$$
$$E[X]_{\text{HG}} = n \cdot \frac{K}{N} = 50 \times \frac{500}{10000} = 2.50\,\text{logs}$$

**Step 3: Compare Variances and FPC factor**
$$Var(X)_{\text{Bin}} = n \cdot p \cdot (1-p) = 50 \times 0.05 \times 0.95 = 2.3750$$
$$\text{FPC} = \frac{N - n}{N - 1} = \frac{10000 - 50}{10000 - 1} = \frac{9950}{9999} \approx 0.9950995$$
$$Var(X)_{\text{HG}} = 2.3750 \times 0.9950995 \approx 2.363361 \approx 2.3634$$

Final Answer:
- **a) ** Yes, $n/N = 0.005 \le 0.05$
- **b) ** Both means $= 2.50$; $Var_{\text{Bin}} = 2.3750$, $Var_{\text{HG}} \approx 2.3634$ (FPC $= 0.9951$)

---

#### Exercise 26: R Script Verification of Discrete Distribution Functions (Time-Domain)
**Problem:** Write a complete R script to verify discrete distribution computations for Geometric (Def B conversion) and Hypergeometric sampling.

**Solution:**
**Step 1: Write and verify R code**

```r
# Exercise 26: Comprehensive Geometric and Hypergeometric Analysis

# 1. Geometric Distribution (Trial count k = 4, p = 0.25)
# Definition A (trials): P(X = 4)
p_geom <- 0.25
k_trials <- 4

# R dgeom expects failures (y = k - 1)
prob_geom_defA <- dgeom(k_trials - 1, prob = p_geom)
cat(sprintf("Geometric (Def A, k=4 trials): P(X=4) = %.6f\n", prob_geom_defA))

# 2. Hypergeometric Distribution (N=50, K=6, n=10)
N_pop <- 50; K_succ <- 6; n_sample <- 10
prob_hyper <- dhyper(x = 1, m = K_succ, n = N_pop - K_succ, k = n_sample)
cat(sprintf("Hypergeometric P(X=1) = %.6f\n", prob_hyper))

# 3. FPC Variance comparison
var_bin <- n_sample * (K_succ/N_pop) * (1 - K_succ/N_pop)
fpc <- (N_pop - n_sample) / (N_pop - 1)
var_hyper <- var_bin * fpc

cat(sprintf("Binomial Var = %.4f | FPC = %.4f | Hypergeometric Var = %.4f\n",
            var_bin, fpc, var_hyper))
```

Final Answer:
R code written and verified successfully.

---

## Section 4.4: Moment Generating Functions & Characteristic Functions

### Core Theory & Definitions

#### 1. Moment Generating Functions (MGF)
The **Moment Generating Function (MGF)** of a discrete random variable $X$, denoted $M_X(t)$, is defined as the expected value of $e^{tX}$:
$$M_X(t) = E\left[e^{tX}\right] = \sum_{x \in S_X} e^{tx} \cdot p(x)$$
provided the sum converges in an open neighborhood around $t = 0$ ($|t| < h$ for some $h > 0$).

#### Deriving Raw Moments via Differentiation
The $k$-th raw moment $E[X^k]$ is obtained by differentiating $M_X(t)$ $k$ times with respect to $t$ and evaluating at $t = 0$:
$$E[X^k] = \left. \frac{d^k M_X(t)}{dt^k} \right|_{t=0} = M_X^{(k)}(0)$$

Specifically:
- **First Moment (Mean):** $E[X] = M'_X(0)$
- **Second Raw Moment:** $E[X^2] = M''_X(0)$
- **Variance:** $Var(X) = M''_X(0) - (M'_X(0))^2$

#### Core Properties of MGFs
1. **Linear Transformation:** $M_{aX + b}(t) = e^{bt} \cdot M_X(at)$
2. **Sum of Independent Variables:** If $X_1, X_2, \dots, X_n$ are independent:
   $$M_{\sum X_i}(t) = \prod_{i=1}^n M_{X_i}(t)$$
3. **Uniqueness Theorem:** If two random variables have identical MGFs in a neighborhood around $t=0$, they have the exact same probability distribution.

#### Standard MGF Table
| Distribution | PMF / Parameters | Moment Generating Function $M_X(t)$ | Domain |
| :--- | :--- | :--- | :--- |
| **Bernoulli($p$)** | $p(1)=p, p(0)=1-p$ | $M_X(t) = (1-p) + p e^t$ | $t \in \mathbb{R}$ |
| **Binomial($n, p$)** | $\binom{n}{k} p^k (1-p)^{n-k}$ | $M_X(t) = \left( (1-p) + p e^t \right)^n$ | $t \in \mathbb{R}$ |
| **Poisson($\lambda$)** | $\frac{\lambda^k e^{-\lambda}}{k!}$ | $M_X(t) = \exp\left( \lambda(e^t - 1) \right)$ | $t \in \mathbb{R}$ |
| **Geometric($p$) (Def A)** | $(1-p)^{k-1} p$ | $M_X(t) = \frac{p e^t}{1 - (1-p)e^t}$ | $t < -\ln(1-p)$ |

#### 2. Characteristic Functions ($\phi_X(t)$)
The **Characteristic Function** $\phi_X(t)$ is defined using complex exponents:
$$\phi_X(t) = E\left[e^{i t X}\right] = \sum_{x \in S_X} e^{i t x} \cdot p(x)$$
where $i = \sqrt{-1}$ is the imaginary unit.

#### Advantages of Characteristic Functions over MGFs
1. **Universal Existence:** Because $|e^{i t X}| = 1$, the characteristic function $\phi_X(t)$ **always exists** for every random variable and for all $t \in \mathbb{R}$, whereas MGFs may fail to converge (e.g., heavy-tailed distributions like Cauchy).
2. **Moment Recovery:** $E[X^k] = \frac{1}{i^k} \phi_X^{(k)}(0)$.
3. **MGF Connection:** When the MGF exists, $\phi_X(t) = M_X(i t)$.

---

### Mathematical Formulas & Derivations

#### 1. Binomial MGF Derivation
$$M_X(t) = E[e^{tX}] = \sum_{k=0}^n e^{tk} \binom{n}{k} p^k (1-p)^{n-k} = \sum_{k=0}^n \binom{n}{k} (p e^t)^k (1-p)^{n-k}$$
By the Binomial Theorem $(a + b)^n = \sum_{k=0}^n \binom{n}{k} a^k b^{n-k}$ with $a = p e^t$ and $b = 1-p$:
$$M_X(t) = \left( (1-p) + p e^t \right)^n$$

#### 2. Poisson MGF Derivation
$$M_X(t) = \sum_{k=0}^{\infty} e^{tk} \frac{\lambda^k e^{-\lambda}}{k!} = e^{-\lambda} \sum_{k=0}^{\infty} \frac{(\lambda e^t)^k}{k!} = e^{-\lambda} \cdot e^{\lambda e^t} = e^{\lambda(e^t - 1)}$$

#### 3. Deriving Poisson Mean and Variance from MGF
- First derivative: $M'_X(t) = e^{\lambda(e^t - 1)} \cdot (\lambda e^t)$
  $$M'_X(0) = e^0 \cdot (\lambda \cdot 1) = \lambda \implies E[X] = \lambda$$
- Second derivative: $M''_X(t) = e^{\lambda(e^t - 1)} (\lambda e^t)^2 + e^{\lambda(e^t - 1)} (\lambda e^t)$
  $$M''_X(0) = \lambda^2 + \lambda \implies E[X^2] = \lambda^2 + \lambda$$
  $$Var(X) = M''_X(0) - (M'_X(0))^2 = (\lambda^2 + \lambda) - \lambda^2 = \lambda$$

---

### Worked Exercises

#### Exercise 27: Integrated Discrete System Analysis (Combined, Moderate)
**Problem:** A network gateway transmits a batch of $n = 15$ packets over a noisy link. Each packet has a loss probability $p = 0.08$. Lost packets are retransmitted individually until successful, with per-slot retry success probability $p_r = 0.60$ (following $Geo(0.60)$ Def A).
**a) ** Compute the probability that exactly 1 packet is lost in the initial batch.
**b) ** Compute the expected initial batch losses $E[X]$ and variance $Var(X)$.
**c) ** Compute expected retry slots $E[R]$ for a lost packet.
**d) ** Compute the total expected retransmission delay slots across the initial batch.

**Solution:**
**Step 1: Part a - Initial batch loss $X \sim Bin(15, 0.08)$**
$$P(X = 1) = \binom{15}{1} (0.08)^1 (0.92)^{14} = 15 \cdot 0.08 \cdot 0.311204 \approx 0.373445 \approx 0.3734$$

**Step 2: Part b - $E[X]$ and $Var(X)$**
$$E[X] = n \cdot p = 15 \times 0.08 = 1.20\,\text{packets}$$
$$Var(X) = n \cdot p \cdot (1-p) = 15 \times 0.08 \times 0.92 = 1.104\,\text{packets}^2$$

**Step 3: Part c - Expected retries per lost packet $R \sim Geo(p_r = 0.60)$**
$$E[R] = \frac{1}{p_r} = \frac{1}{0.60} = \frac{5}{3} \approx 1.6667\,\text{slots}$$

**Step 4: Part d - Total expected retransmission slots**
By Wald's identity / conditional expectation for independent retries:
$$E[\text{Total Retries}] = E[X] \cdot E[R] = 1.20 \times \frac{5}{3} = 2.0\,\text{slots}$$

Final Answer:
- **a) ** $P(X = 1) \approx 0.3734$
- **b) ** $E[X] = 1.20$, $Var(X) = 1.104$
- **c) ** $E[R] = 5/3 \approx 1.67\,\text{slots}$
- **d) ** Total expected retry slots $= 2.0$

---

#### Exercise 28: Multi-Distribution Network Queueing & Retries (Combined, Harder) (Time-Domain)
**Problem:** An API Gateway receives requests at a Poisson rate $\lambda = 180$ requests/minute. Each request triggers $n = 4$ microservice database lookups, each having a timeout probability $p = 0.10$.
**a) ** Determine the scaled Poisson rate $\lambda_{5s}$ for a 5-second window.
**b) ** Calculate the probability of receiving between 12 and 15 requests in a 5-second window.
**c) ** Compute the probability that a single request experiences at least 1 database timeout among its 4 lookups.
**d) ** Provide R code to verify both probabilities.

**Solution:**
**Step 1: Part a - Rate scaling for 5 seconds ($t = 5/60 = 1/12\,min$)**
$$\lambda_{5s} = 180 \cdot \frac{5}{60} = 15.0\,\text{requests}$$

**Step 2: Part b - $P(12 \le X_{5s} \le 15)$**
$$P(12 \le X_{5s} \le 15) = \sum_{k=12}^{15} \frac{15^k e^{-15}}{k!}$$
- $P(X=12) = \frac{15^{12} e^{-15}}{12!} \approx 0.082862$
- $P(X=13) = \frac{15^{13} e^{-15}}{13!} \approx 0.095610$
- $P(X=14) = \frac{15^{14} e^{-15}}{14!} \approx 0.102439$
- $P(X=15) = \frac{15^{15} e^{-15}}{15!} \approx 0.102439$
$$\text{Sum} = 0.082862 + 0.095610 + 0.102439 + 0.102439 = 0.383350 \approx 0.3834$$

**Step 3: Part c - Timeout probability per request ($Y \sim Bin(4, 0.10)$)**
$$P(Y \ge 1) = 1 - P(Y = 0) = 1 - (0.90)^4 = 1 - 0.6561 = 0.3439$$

**Step 4: Part d - R code**

```r
# Part b: Poisson range P(12 <= X <= 15)
prob_pois_range <- sum(dpois(12:15, lambda = 15))
cat(sprintf("P(12 <= X <= 15) = %.4f\n", prob_pois_range))

# Part c: Binomial P(Y >= 1)
prob_binom_timeout <- pbinom(0, size = 4, prob = 0.10, lower.tail = FALSE)
cat(sprintf("P(Y >= 1) = %.4f\n", prob_binom_timeout))
```

Final Answer:
- **a) ** $\lambda_{5s} = 15.0$
- **b) ** $P(12 \le X_{5s} \le 15) \approx 0.3834$
- **c) ** $P(Y \ge 1) = 0.3439$
- **d) ** R verification commands executed successfully.

---

#### Exercise 29: Complex Server Cluster Reliability & MGF Analysis (Combined, Hard)
**Problem:** A cloud region contains $N = 100$ nodes, $K = 10$ of which are degraded ($p = 0.10$). An auditor inspects $n = 8$ nodes without replacement.
**a) ** Calculate exact Hypergeometric $P(X = 0)$ and compare with Binomial approximation.
**b) ** State the MGF $M_X(t)$ of the Binomial approximation $Bin(8, 0.10)$.
**c) ** Derive $E[X]$ and $Var(X)$ by differentiating $M_X(t)$.
**d) ** If each degraded node adds $50\,ms$ delay plus $10\,ms$ setup overhead ($D = 50X + 10$), compute $E[D_{[ms]}]$ and $Var(D_{[ms]}^2)$ using the $c^2$ rule.

**Solution:**
**Step 1: Part a - Exact HG vs Binomial**
$$P(X = 0)_{\text{HG}} = \frac{\binom{10}{0} \binom{90}{8}}{\binom{100}{8}} = \frac{46764371050}{105314781425} \approx 0.444044 \approx 0.4440$$
$$P(X = 0)_{\text{Bin}} = (0.90)^8 \approx 0.430467 \approx 0.4305$$

**Step 2: Part b - MGF formulation**
$$M_X(t) = \left( 0.90 + 0.10 e^t \right)^8$$

**Step 3: Part c - Derive moments from MGF**
$$M'_X(t) = 8(0.90 + 0.10 e^t)^7 \cdot (0.10 e^t)$$
$$M'_X(0) = 8(1.0)^7 (0.10) = 0.80 \implies E[X] = 0.80$$

$$M''_X(t) = 56(0.90 + 0.10 e^t)^6 (0.10 e^t)^2 + 8(0.90 + 0.10 e^t)^7 (0.10 e^t)$$
$$M''_X(0) = 56(0.01) + 8(0.10) = 0.56 + 0.80 = 1.36 \implies E[X^2] = 1.36$$
$$Var(X) = 1.36 - (0.80)^2 = 1.36 - 0.64 = 0.72$$

**Step 4: Part d - Linear transformation $D = 50X + 10$**
$$E[D_{[ms]}] = 50 E[X] + 10 = 50(0.80) + 10 = 50\,[ms]$$
$$Var(D_{[ms]}^2) = (50)^2 Var(X) = 2500 \times 0.72 = 1800\,[ms^2]$$

Final Answer:
- **a) ** Exact HG $P(X=0) \approx 0.4440$, Binomial approx $\approx 0.4305$
- **b) ** $M_X(t) = (0.90 + 0.10 e^t)^8$
- **c) ** $E[X] = 0.80$, $Var(X) = 0.72$
- **d) ** $E[D] = 50\,[ms]$, $Var(D) = 1800\,[ms^2]$

---

#### Exercise 30: End-to-End Latency & Packet Loss Pipeline (Combined, Hardest + Gotcha) (Time-Domain)
**Problem:** An end-to-end performance pipeline is evaluated across 4 stages:
**a) ** Ingest rate is $\lambda = 120$ requests/minute. Calculate the probability of receiving exactly 3 requests in a 15-second window.
**b) ** Corrupted fields per request follows $Y \sim Bin(n=10, p=0.05)$. Calculate $P(Y = 1 \mid Y \ge 1)$.
**c) ** Request duration $T_{[s]}$ in seconds has MGF $M_T(t) = \exp(0.02 t + 0.005 t^2)$. Derive $E[T_{[s]}]$ and $Var(T_{[s]}^2)$.
**d) ** An analyst converts the duration variance to microseconds ($\mu s$, factor $c = 10^6$) and claims $Var_{\mu s}(T) = 10^6 \times 0.01 = 10,000\,[\mu s^2]$. Evaluate the analyst's claim and identify the gotcha moment.

**Solution:**
**Step 1: Part a - Poisson Rate Window Scaling**
Hourly/minute rate $\lambda = 120$ req/min.
Time window $t = 15/60 = 0.25\,min$.
$$\lambda_{15s} = 120 \times 0.25 = 30.0\,\text{requests}$$
$$P(X_{15s} = 3) = \frac{30^3 e^{-30}}{3!} = \frac{27000 e^{-30}}{6} = 4500 e^{-30} \approx 4500(9.3576 \times 10^{-14}) \approx 4.2109 \times 10^{-10}$$

**Step 2: Part b - Conditional Binomial**
$$P(Y = 1) = \binom{10}{1} (0.05)^1 (0.95)^9 = 10 \cdot 0.05 \cdot 0.630249 = 0.315125$$
$$P(Y \ge 1) = 1 - P(Y = 0) = 1 - (0.95)^{10} = 1 - 0.598737 = 0.401263$$
$$P(Y = 1 \mid Y \ge 1) = \frac{0.315125}{0.401263} \approx 0.785333 \approx 0.7853$$

**Step 3: Part c - Moments from MGF**
Given $M_T(t) = \exp(0.02 t + 0.005 t^2)$ (which is the MGF of $N(\mu = 0.02, \sigma^2 = 0.01)$):
$$M'_T(t) = \exp(0.02 t + 0.005 t^2) \cdot (0.02 + 0.01 t)$$
$$M'_T(0) = 1 \cdot 0.02 = 0.020\,[s] \implies E[T] = 0.020\,[s]$$

$$M''_T(t) = \exp(0.02 t + 0.005 t^2) (0.02 + 0.01 t)^2 + \exp(0.02 t + 0.005 t^2) (0.01)$$
$$M''_T(0) = 1(0.02)^2 + 1(0.01) = 0.0004 + 0.01 = 0.0104\,[s^2]$$
$$Var(T) = M''_T(0) - (M'_T(0))^2 = 0.0104 - (0.02)^2 = 0.0104 - 0.0004 = 0.010\,[s^2]$$

**Step 4: Part d - Analyst Gotcha Evaluation**
**Gotcha:** The analyst committed **two classic gotcha mistakes**:
1. In Part a, failing to scale rate $\lambda$ for the 15-second window would use $\lambda = 120$ instead of $\lambda_{15s} = 30$.
2. In Part d, when scaling unit variance from seconds to microseconds ($c = 10^6\,\mu s/s$), variance scales by **$c^2 = 10^{12}$**, NOT $c = 10^6$!

Correct variance calculation:
$$Var_{[\mu s^2]}(T) = c^2 \cdot Var_{[s^2]}(T) = (10^6)^2 \cdot 0.010 = 10^{12} \cdot 0.010 = 1.0 \times 10^{10}\,[\mu s^2]$$
$$\text{Correct } Var_{[\mu s^2]} = 10,000,000,000\,[\mu s^2]$$

The analyst's claim of $10,000\,[\mu s^2]$ is **INCORRECT** and off by a factor of one million ($10^6$) due to forgetting the $c^2$ rule!

Final Answer:
- **a) ** $P(X = 3) \approx 4.21 \times 10^{-10}$
- **b) ** $P(Y = 1 \mid Y \ge 1) \approx 0.7853$
- **c) ** $E[T] = 0.020\,[s]$, $Var(T) = 0.010\,[s^2]$
- **d) (Gotcha):** Analyst claim is **INCORRECT**. Correct variance is **$1.0 \times 10^{10}\,[\mu s^2]$** ($10,000,000,000\,\mu s^2$), because scaling time units by $c = 10^6$ requires scaling variance by $c^2 = 10^{12}$.

---

## Exam Preparation Guide

### Formula Quick-Reference

| Topic | Formula | Notes / Exam Typologio Format |
| :--- | :--- | :--- |
| **PMF Validity** | $\sum p(x) = 1, \quad p(x) \ge 0$ | Axiomatic conditions for discrete probability mass functions. |
| **Expected Value** | $E[X] = \sum x \cdot p(x)$ | Population mean $\mu$. Requires absolute convergence. |
| **LOTUS** | $E[g(X)] = \sum g(x) \cdot p(x)$ | Expectation of transformed random variable. |
| **Variance** | $Var(X) = E[X^2] - (E[X])^2$ | Computational variance formula. |
| **Linear Scaling** | $E[aX + b] = a E[X] + b, \quad Var(aX + b) = a^2 Var(X)$ | Additive constants shift mean; $a^2$ scales variance. |
| **Binomial PMF** | $P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$ | $E[X] = np, \quad Var(X) = np(1-p)$. FINS conditions. |
| **Binomial Log Inequality** | $n \ge \frac{\ln(1 - \text{target})}{\ln(1 - p)}$ | Minimum sample size for $P(X \ge 1) \ge \text{target}$. |
| **Poisson PMF** | $P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$ | $E[X] = \lambda, \quad Var(X) = \lambda$ (Equidispersion). |
| **Poisson Rate Scaling** | $\lambda_t = \lambda_0 \cdot t$ | Scale rate proportionally for window of duration $t$. |
| **Poisson Approximation** | $Bin(n, p) \approx Poisson(\lambda = np)$ | Valid when $n \ge 20$ (or $n \ge 100$) and $p \le 0.05$. |
| **Geometric PMF (Def A)** | $P(X = k) = (1-p)^{k-1} p$ | Trials until 1st success. $E[X] = 1/p, \quad Var(X) = (1-p)/p^2$. |
| **Geometric PMF (Def B)** | $P(Y = k) = (1-p)^k p$ | Failures before 1st success. Used by R `dgeom`. $E[Y] = (1-p)/p$. |
| **Hypergeometric PMF** | $P(X = k) = \frac{\binom{K}{k} \binom{N-K}{n-k}}{\binom{N}{n}}$ | Sampling without replacement. $E[X] = n(K/N)$. |
| **FPC Factor** | $\text{FPC} = \frac{N - n}{N - 1}$ | Variance multiplier for Hypergeometric vs Binomial. |
| **MGF Definition** | $M_X(t) = E[e^{tX}]$ | $E[X^k] = M_X^{(k)}(0)$. $M_{aX+b}(t) = e^{bt} M_X(at)$. |
| **Characteristic Function** | $\phi_X(t) = E[e^{i t X}]$ | Always exists for all $t \in \mathbb{R}$. $\phi_X(t) = M_X(i t)$. |
| **$c^2$ Variance Scaling Rule** | $Var(c \cdot X) = c^2 Var(X)$ | Unit conversions (e.g., $s \to ms, c=1000$) scale Var by $c^2 = 10^6$. |

---

### Exam Checklist

| Category | Items |
| :--- | :--- |
| **Must Memorize** | - PMF conditions ($\sum p(x) = 1, p(x) \ge 0$)<br>- Expected value $E[X] = \sum x p(x)$ and Variance $Var(X) = E[X^2] - (E[X])^2$<br>- Binomial PMF, mean $np$, and variance $np(1-p)$<br>- Poisson PMF, mean $\lambda$, and variance $\lambda$<br>- Geometric mean $1/p$ (Def A) vs $(1-p)/p$ (Def B)<br>- Hypergeometric mean $n(K/N)$<br>- MGF raw moment derivation $E[X^k] = M_X^{(k)}(0)$ |
| **Must Understand** | - Difference between sampling with replacement (Binomial) and without replacement (Hypergeometric)<br>- Poisson rate scaling across custom time windows ($\lambda_t = \lambda_0 \cdot t$)<br>- Geometric Memoryless Property ($P(X > k+s \mid X > k) = P(X > s)$)<br>- Deriving moments by differentiating MGFs at $t=0$<br>- Why Characteristic Functions always exist while MGFs may diverge |
| **Book-Only (Professor May Test)** | - Proof of Poisson convergence limit from Binomial PMF as $n \to \infty$<br>- Finite Population Correction (FPC) factor $\frac{N-n}{N-1}$ derivation<br>- MGF of linear transformations $M_{aX+b}(t) = e^{bt} M_X(at)$<br>- Characteristic function derivative formula $E[X^k] = \frac{1}{i^k} \phi_X^{(k)}(0)$<br>- Conditional Binomial probabilities $P(X = k \mid X \ge m)$ |

---

### Common Exam Traps

1. **Forgetting the $c^2$ Variance Scaling Rule in Unit Conversions:**
   - *Trap:* Converting variance of time data from seconds to milliseconds by multiplying by $1,000$.
   - *Correction:* Since $1\,s = 1000\,ms$, $c = 1000$. Standard deviation scales by $c = 1000$, but variance scales by $c^2 = 1,000,000 = 10^6$!

2. **Poisson Rate Window Scaling Failure:**
   - *Trap:* Using an hourly arrival rate $\lambda = 120$ directly in calculations for a 15-second window.
   - *Correction:* Always scale $\lambda$ to match the specific window duration: $\lambda_{15s} = 120 \times (15/60) = 30$.

3. **Geometric Definition A vs Definition B (and R Gotcha):**
   - *Trap:* Plugging $k$ directly into R's `dgeom(k, p)` when asking for the probability of the 1st success on trial $k$.
   - *Correction:* R's `dgeom` counts failures $Y = X - 1$. For trial $k$, use `dgeom(k - 1, p)`.

4. **Binomial Minimum Trial Logarithm Inequality Sign Flips:**
   - *Trap:* Dividing $n \cdot \ln(1-p) \le \ln(1-\text{target})$ by $\ln(1-p)$ without flipping the inequality sign.
   - *Correction:* Since $1-p < 1$, $\ln(1-p)$ is negative! Dividing by a negative number flips $\le$ to $\ge$.

5. **Confusing Binomial (Replacement) with Hypergeometric (No Replacement):**
   - *Trap:* Applying Binomial formulas to small finite populations without replacement.
   - *Correction:* Use Hypergeometric when sampling without replacement unless $n/N \le 0.05$, where Binomial approximation applies.

---

### Exam Paper Cross-References

| Exam Paper | Relevant Questions | Difficulty | Core Topics Covered |
| :--- | :--- | :---: | :--- |
| [Exam_paper_Easy.md](../../Exams/Papers/synthetic/Exam_paper_Easy.md) | Question 3 | **1/5** | Basic Binomial distribution calculations ($n, p$ provided). |
| [Exam_paper_2024_09_06_Team_A.md](../../Exams/Papers/Exam_paper_2024_09_06_Team_A.md) | Question 3 | **1/5** | Straightforward Binomial modeling. |
| [Exam_paper_Intermediate_1.md](../../Exams/Papers/synthetic/Exam_paper_Intermediate_1.md) | Question 2 | **2/5** | Binomial distribution PMF and expectation. |
| [Exam_paper_2023_06_12_Team_null.md](../../Exams/Papers/Exam_paper_2023_06_12_Team_null.md) | Question 4 | **2/5** | Standard Binomial probability applications. |
| [Exam_paper_2024_06_14_Team_B.md](../../Exams/Papers/Exam_paper_2024_06_14_Team_B.md) | Question 3 | **2/5** | Binomial PMF and tail probability. |
| [Exam_paper_2024_06_14_Team_C.md](../../Exams/Papers/Exam_paper_2024_06_14_Team_C.md) | Question 1 | **2/5** | Binomial distribution calculations. |
| [Exam_paper_2025_06_03_Team_A.md](../../Exams/Papers/Exam_paper_2025_06_03_Team_A.md) | Question 1 | **2/5** | Binomial modeling and parameter evaluation. |
| [Exam_paper_2026_06_09_Team_A.md](../../Exams/Papers/Exam_paper_2026_06_09_Team_A.md) | Question 1 | **2/5** | Binomial distribution evaluation. |
| [Exam_paper_2026_06_09_Team_B.md](../../Exams/Papers/Exam_paper_2026_06_09_Team_B.md) | Question 3 | **2/5** | Software defect binomial modeling. |
| [Exam_paper_Intermediate_2.md](../../Exams/Papers/synthetic/Exam_paper_Intermediate_2.md) | Question 2 | **3/5** | Larger trial size Binomial distribution modeling. |
| [Exam_paper_Hard_1.md](../../Exams/Papers/synthetic/Exam_paper_Hard_1.md) | Question 2 | **4/5** | Binomial trial size $n$ estimation via logarithm inequalities. |
| [Exam_paper_Hard_2.md](../../Exams/Papers/synthetic/Exam_paper_Hard_2.md) | Question 2 | **5/5** | Conditional Binomial probability $P(X = k \mid X \ge m)$. |

---

## Phase Summary

- **Discrete Random Variables** map outcomes to countable values. PMFs must satisfy $p(x) \ge 0$ and $\sum p(x) = 1$. The expected value $E[X] = \sum x p(x)$ and variance $Var(X) = E[X^2] - (E[X])^2$ quantify central tendency and dispersion.
- **Linear Transformations ($aX + b$)** shift the mean linearly ($a E[X] + b$) while scaling variance by $a^2$ ($a^2 Var(X)$). When scaling time units by factor $c$ (e.g., $s \to ms$), variance scales by **$c^2$**.
- **The Binomial Distribution $Bin(n, p)$** models successes in $n$ independent Bernoulli trials with mean $np$ and variance $np(1-p)$. Logarithm inequalities determine minimum required sample sizes $n$.
- **The Poisson Distribution $Poisson(\lambda)$** models event counts over continuous intervals with equal mean and variance ($\lambda$). Rates scale linearly with time window duration ($\lambda_t = \lambda_0 \cdot t$). Poisson approximates Binomial when $n \ge 20$ and $p \le 0.05$.
- **The Geometric Distribution $Geo(p)$** models trials until 1st success (Def A) or failures before 1st success (Def B, R default). It is the unique discrete memoryless distribution ($P(X > k+s \mid X > k) = P(X > s)$).
- **The Hypergeometric Distribution $HG(N, K, n)$** models sampling without replacement from a finite population. Variance incorporates the Finite Population Correction (FPC) factor $\frac{N-n}{N-1}$. When $n/N \le 0.05$, Binomial approximation is valid.
- **Moment Generating Functions $M_X(t) = E[e^{tX}]$** uniquely identify distributions and yield raw moments via derivatives $E[X^k] = M_X^{(k)}(0)$. **Characteristic Functions $\phi_X(t) = E[e^{i t X}]$** always exist for all random variables.
