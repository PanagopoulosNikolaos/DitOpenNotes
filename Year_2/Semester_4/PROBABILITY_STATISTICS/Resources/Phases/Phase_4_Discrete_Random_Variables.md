# Phase 4: Discrete Random Variables

## Table of Contents
1. [Discrete RV Fundamentals](#1-discrete-rv-fundamentals)
2. [Binomial Distribution](#2-binomial-distribution)
3. [Poisson Distribution](#3-poisson-distribution)
4. [Geometric and Hypergeometric Distributions](#4-geometric-and-hypergeometric-distributions)
5. [Moment Generating Functions](#5-moment-generating-functions)
6. [Time-Specific Gotchas](#6-time-specific-gotchas)
7. [Solved Exercises](#7-solved-exercises)
8. [Phase Summary](#phase-summary)

---

## 1. Discrete RV Fundamentals

A **Discrete Random Variable** takes on a finite or countably infinite set of values. In a time context, it maps time-based outcomes (clock tick counts, discrete delay steps) to numerical values.

### Probability Mass Function (PMF)
The PMF is $p(x) = P(X = x)$. It must satisfy:
1. $p(x) \geq 0$
2. $\sum p(x) = 1$

### Expected Value $E[X]$
The Expected Value (mean) is the probability-weighted average:
$$E[X] = \mu = \sum x \cdot p(x)$$
Linearity: $E[aX + b] = a \cdot E[X] + b$

### Variance $V(X)$
Variance measures spread:
$$V(X) = E[X^2] - (E[X])^2$$
where $E[X^2] = \sum x^2 \cdot p(x)$.
Properties: $V(aX + b) = a^2 \cdot V(X)$

---

## 2. Binomial Distribution

Models the number of successes in a fixed sequence of independent trials.

### The Four Conditions (FINS)
1. **F**ixed number of trials $n$.
2. **I**ndependence between trials.
3. **N**o more than two outcomes (success/failure).
4. **S**ame probability of success $p$ for all trials.

### Formulae
*   **PMF:** $P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$
*   **Mean:** $E[X] = n \cdot p$
*   **Variance:** $V(X) = n \cdot p \cdot (1-p)$

---

## 3. Poisson Distribution

Models the count of rare, independent events occurring within a fixed time window at a constant average rate $\lambda$.

### Formulae
*   **PMF:** $P(X_t = k) = \frac{(\lambda \cdot t)^k \cdot e^{-\lambda \cdot t}}{k!}$
*   **Mean:** $E[X_t] = \lambda \cdot t$
*   **Variance:** $V(X_t) = \lambda \cdot t$

Note: To change the time interval, scale $\lambda$ proportionally ($\lambda_t = \lambda \cdot t$).

---

## 4. Geometric and Hypergeometric Distributions

### Geometric Distribution
Models the number of discrete time slots until the first success.
*   **Definition A (Counting total slots):** $P(T = k) = (1-p)^{k-1} p$, $E[T] = 1/p$, $V(T) = (1-p)/p^2$
*   **Definition B (Counting failures before success):** $P(Y = k) = (1-p)^k p$, $E[Y] = (1-p)/p$, $V(Y) = (1-p)/p^2$
*   **Memoryless Property:** $P(T > k + s \mid T > k) = P(T > s)$

### Hypergeometric Distribution
Models sampling **without replacement** from a finite population.
*   **PMF:** $P(X = k) = \frac{\binom{K}{k} \binom{N-K}{n-k}}{\binom{N}{n}}$
*   **Mean:** $E[X] = n \cdot \frac{K}{N}$
*   **Variance:** $V(X) = n \cdot \frac{K}{N} \cdot (1 - \frac{K}{N}) \cdot \frac{N - n}{N - 1}$

---

## 5. Moment Generating Functions

The Moment Generating Function $M_X(t)$ is:
$$M_X(t) = E\left[e^{tX}\right]$$
Moments can be found by differentiating:
$E[X^n] = M_X^{(n)}(0)$
*   $E[X] = M'_X(0)$
*   $V(X) = M''_X(0) - (M'_X(0))^2$

**Linear Transformation:** $M_{aX+b}(t) = e^{bt} \cdot M_X(at)$
**Sums of Independent RVs:** $M_{X+Y}(t) = M_X(t) \cdot M_Y(t)$

---

## 6. Time-Specific Gotchas

1. **Unit Scaling Multiplier on Variance:** If you convert seconds to ms ($a=1000$), $V(1000T) = 1,000,000 \cdot V(T)$. Don't forget to square $a$.
2. **Variance of Difference:** $V(T_1 - T_2) = V(T_1) + V(T_2)$. Variance is never subtracted.
3. **Binomial Time Slots vs Duration:** $n$ in Binomial is the number of time slots, not the total elapsed time.
4. **Poisson Rate Scaling:** If rate is 120/hr, and window is 1 min, you must scale $\lambda$ to 2/min before calculating.
5. **Memorylessness:** Geometric and Exponential are the only memoryless distributions.
6. **MGF Linear Scaling:** $M_{aT+b}(t) = e^{bt} M_T(at)$. Note that $a$ multiplies $t$ inside $M_T(\cdot)$, and $b$ becomes an exponential term $e^{bt}$.

---

## 7. Solved Exercises

#### Exercise 1: Computing Expected Processing Duration $E[T]$
**Problem:** Connection retry counts $T \in \{0, 1, 2, 3\}\text{ s}$ have PMF $p(t) = [0.1, 0.2, 0.3, 0.4]$. Find $E[T]$.
**Solution:**
$$E[T] = \sum t \cdot p(t) = (0 \cdot 0.1) + (1 \cdot 0.2) + (2 \cdot 0.3) + (3 \cdot 0.4) = 0 + 0.2 + 0.6 + 1.2 = 2.0\text{ s}$$

#### Exercise 2: Computing Duration Variance $V(T)$
**Problem:** Using PMF from Ex 1 ($E[T] = 2.0$), compute $V(T)$.
**Solution:**
$$E[T^2] = (0^2 \cdot 0.1) + (1^2 \cdot 0.2) + (2^2 \cdot 0.3) + (3^2 \cdot 0.4) = 0 + 0.2 + 1.2 + 3.6 = 5.0$$
$$V(T) = E[T^2] - (E[T])^2 = 5.0 - (2.0)^2 = 1.0\text{ s}^2$$

#### Exercise 3: Unit Scaling and Constant Overhead
**Problem:** $T$ in seconds has $E[T] = 2.5\text{ s}$ and $V(T) = 1.44\text{ s}^2$. Total response time in ms is $Y = 1000T + 40$. Find $E[Y]$ and $V[Y]$.
**Solution:**
$$E[Y] = 1000 \cdot E[T] + 40 = 2500 + 40 = 2540\text{ ms}$$
$$V[Y] = 1000^2 \cdot V(T) = 1,000,000 \cdot 1.44 = 1,440,000\text{ ms}^2$$

#### Exercise 4: Computing PMF for Exact Number of Time Slots
**Problem:** Inspect 5 slots. Prob of bottleneck per slot is $p = 0.20$. Prob of exactly 2 bottlenecks?
**Solution:**
$$P(X=2) = \binom{5}{2} (0.20)^2 (0.80)^3 = 10 \cdot 0.04 \cdot 0.512 = 0.2048$$

#### Exercise 5: "At Least One" Failed Time Slot
**Problem:** Server checks health for $n=6$ slots. Prob of outage is $p=0.05$. Find prob of at least 1 outage.
**Solution:**
$$P(X \ge 1) = 1 - P(X=0) = 1 - \binom{6}{0} (0.05)^0 (0.95)^6 = 1 - (0.95)^6 = 1 - 0.7351 = 0.2649$$

#### Exercise 6: Basic Arrival Count in 1 Hour Window (Poisson)
**Problem:** API calls arrive at $\lambda = 4$ per hour. Find prob of exactly 3 requests in a 1-hour window.
**Solution:**
$$P(X=3) = \frac{4^3 \cdot e^{-4}}{3!} = \frac{64 \cdot e^{-4}}{6} \approx \frac{1.1722}{6} \approx 0.1954$$

#### Exercise 7: Scaling Rate from Hours to Minutes
**Problem:** Queries arrive at $\lambda = 6$ per hour. Find prob of exactly 2 queries in a 30-minute window.
**Solution:**
$\lambda_{30\min} = 6 \times 0.5 = 3$.
$$P(X=2) = \frac{3^2 \cdot e^{-3}}{2!} = \frac{9 \cdot e^{-3}}{2} \approx 0.2240$$

#### Exercise 8: First Connection Success on 4th Time Slot (Geometric)
**Problem:** A modem connects in discrete 1-second slots with $p = 0.70$. Find prob that first success is on 4th slot.
**Solution:**
Using Definition A:
$$P(T = 4) = (1 - 0.70)^{4-1} (0.70) = (0.30)^3 \cdot 0.70 = 0.027 \cdot 0.70 = 0.0189$$

#### Exercise 9: Memoryless Property of Time Slots
**Problem:** Defect probability $p = 0.10$. Given first 5 slots were error-free, find prob that first defect is on 8th slot.
**Solution:**
$$P(T = 8 \mid T > 5) = P(T = 8 - 5) = P(T = 3) = (0.90)^2 \cdot 0.10 = 0.081$$

#### Exercise 10: Time Log Audit (Hypergeometric)
**Problem:** Batch of $N = 52$ logs, $K = 4$ contain alerts. Sample $n = 5$ without replacement. Prob of exactly 3 alerts?
**Solution:**
$$P(X = 3) = \frac{\binom{4}{3} \binom{48}{2}}{\binom{52}{5}} = \frac{4 \cdot 1128}{2598960} \approx 0.001736$$

#### Exercise 11: Finding Mean and Variance from a Duration MGF
**Problem:** Response time $T$ has $M_T(t) = (1 - 2t)^{-1}$. Find $E[T]$ and $V(T)$.
**Solution:**
$M'_T(t) = 2(1 - 2t)^{-2}$. Evaluate at $t=0$: $E[T] = 2$.
$M''_T(t) = 8(1 - 2t)^{-3}$. Evaluate at $t=0$: $E[T^2] = 8$.
$V(T) = 8 - 2^2 = 4$.

#### Exercise 12: MGF Linear Transformation of Latency
**Problem:** Execution time $T$ has $M_T(t) = e^{2t + 8t^2}$. Find MGF of $Y = 3T - 5$.
**Solution:**
$$M_Y(t) = e^{-5t} M_T(3t) = e^{-5t} e^{2(3t) + 8(3t)^2} = e^{-5t + 6t + 72t^2} = e^{t + 72t^2}$$

#### Exercise 13: Sum of Independent Binomial Time Slots
**Problem:** $X \sim B(n, p)$ and $Y \sim B(m, p)$ are independent. Find $M_{X+Y}(t)$.
**Solution:**
$$M_{X+Y}(t) = M_X(t) \cdot M_Y(t) = (q + p e^t)^n \cdot (q + p e^t)^m = (q + p e^t)^{n+m}$$

#### Exercise 14: R Code Snippet -- Empirical Discrete Duration Analysis
**Problem:** R code to compute PMF table, expected value, and variance.
**Solution:**
```r
durations <- c(1, 2, 2, 3, 1, 4, 2, 3, 3, 2)
val_counts <- table(durations)
pmf <- val_counts / length(durations)
t_vals <- as.numeric(names(pmf))

e_T <- sum(t_vals * pmf)
e_T2 <- sum((t_vals^2) * pmf)
var_T <- e_T2 - (e_T^2)
```

#### Exercise 15: R Code Snippet -- Time Slot Reliability (Binomial)
**Problem:** R code for cumulative and exact Binomial prob.
**Solution:**
```r
n_slots <- 20; p_fail <- 0.15
p_exact_3 <- dbinom(3, size = n_slots, prob = p_fail)
p_at_most_3 <- pbinom(3, size = n_slots, prob = p_fail)
```

#### Exercise 16: R Code Snippet -- Poisson Time Window Rate Analysis
**Problem:** Scale rate and compute Poisson prob in R.
**Solution:**
```r
lambda_hourly <- 12
lambda_15min <- lambda_hourly * (15 / 60)
p_2_in_15min <- dpois(2, lambda = lambda_15min)
p_atmost_20_in_2hr <- ppois(20, lambda = lambda_hourly * 2)
```

#### Exercise 17: R Code Snippet -- Geometric & Hypergeometric
**Problem:** Calculate probabilities for Geometric (Def A) and Hypergeometric.
**Solution:**
```r
p_success <- 0.20; k_trial <- 4
# R uses failures before success (Def B)
p_geom_defA <- dgeom(k_trial - 1, prob = p_success)

N_pop <- 52; K_succ <- 4; n_sample <- 5; k_target <- 3
p_hyper <- dhyper(k_target, m = K_succ, n = N_pop - K_succ, k = n_sample)
```

---

## Phase Summary
- Discrete Random Variables map outcomes to numerical values. Expected value is $\sum x p(x)$ and Variance is $E[X^2] - (E[X])^2$.
- The Binomial Distribution $B(n, p)$ models the number of successes in $n$ fixed, independent trials. Mean is $np$, variance is $np(1-p)$.
- The Poisson Distribution $Po(\lambda)$ models counts over an interval with constant rate $\lambda$. Mean and variance both equal $\lambda$.
- The Geometric Distribution models trials until first success. Hypergeometric models sampling without replacement.
- Moment Generating Functions $M_X(t) = E[e^{tX}]$ generate raw moments via derivatives at $t=0$. They uniquely identify distributions and are useful for linear transformations and sums of independent variables.
- Time context introduces gotchas like scaling unit multipliers on variance, ensuring time interval scaling in Poisson, and understanding memoryless properties of Geometric variables.
