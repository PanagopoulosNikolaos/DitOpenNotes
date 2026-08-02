# Phase 5B: Multivariate Random Variables

## Table of Contents
1. [Multivariate Random Variables - Fundamentals](#1-multivariate-random-variables---fundamentals)
2. [Multivariate Moments, Covariance, and Conditional Expectation](#2-multivariate-moments-covariance-and-conditional-expectation)
3. [Functions of Multiple Random Variables & Order Statistics](#3-functions-of-multiple-random-variables--order-statistics)
4. [Time-Specific Gotchas](#4-time-specific-gotchas)
5. [Solved Exercises](#5-solved-exercises)
6. [Phase Summary](#phase-summary)

---

## 1. Multivariate Random Variables - Fundamentals

Multivariate variables model the joint behavior of multiple execution metrics (e.g., $T_1$ and $T_2$).

### Joint PDF and Normalization
$$\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f_{T_1, T_2}(t_1, t_2) \, dt_1 \, dt_2 = 1$$
Probability over a region $R$: $P((T_1, T_2) \in R) = \iint_R f(t_1, t_2) \, dt_1 \, dt_2$.

### Marginal and Conditional PDFs
**Marginal:** $f_{T_1}(t_1) = \int_{-\infty}^{\infty} f_{T_1, T_2}(t_1, t_2) \, dt_2$.
**Conditional:** $f_{T_2 \mid T_1}(t_2 \mid t_1) = \frac{f_{T_1, T_2}(t_1, t_2)}{f_{T_1}(t_1)}$.

### Independence
$T_1$ and $T_2$ are independent iff $f(t_1, t_2) = f_{T_1}(t_1) \cdot f_{T_2}(t_2)$ for all regions.

---

## 2. Multivariate Moments, Covariance, and Conditional Expectation

### Covariance and Correlation
**Covariance** measures linear dependence:
$$\text{Cov}(T_1, T_2) = E[T_1 T_2] - E[T_1] E[T_2]$$
**Correlation ($\rho$):**
$$\rho_{T_1, T_2} = \frac{\text{Cov}(T_1, T_2)}{\sigma_{T_1} \sigma_{T_2}}$$

### Variance of Sums
For constants $a, b$:
$$V(a T_1 + b T_2) = a^2 V(T_1) + b^2 V(T_2) + 2 a b \text{Cov}(T_1, T_2)$$
If $T_1, T_2$ are independent, $\text{Cov} = 0$, so $V(T_1 + T_2) = V(T_1) + V(T_2)$.

### Conditional Expectation
Law of Total Expectation: $E[T_1] = E_{T_2} \left[ E_{T_1 \mid T_2}(T_1 \mid T_2) \right]$.

---

## 3. Functions of Multiple Random Variables & Order Statistics

### Convolution (Sums)
For independent $T_1, T_2$, the PDF of $Y = T_1 + T_2$ is:
$$f_Y(y) = \int_{-\infty}^{\infty} f_{T_1}(t) \, f_{T_2}(y - t) \, dt$$

### Order Statistics (Min and Max)
For $n$ i.i.d. variables with CDF $F(t)$ and PDF $f(t)$:
*   **Max (Parallel Bottleneck):** $F_{\max}(t) = [F(t)]^n$, $f_{\max}(t) = n[F(t)]^{n-1}f(t)$
*   **Min (First to Finish):** $F_{\min}(t) = 1 - [1 - F(t)]^n$

---

## 4. Time-Specific Gotchas

1. **Dependent Support Regions:** If integration bounds for $T_1$ depend on $T_2$ (e.g., $0 \le t_1 \le t_2 \le 1$), the variables are **dependent**, even if the PDF is constant.
2. **Uncorrelated $\neq$ Independent:** For non-Gaussian variables, zero covariance does not guarantee independence.
3. **Variance of Total Processing:** Always include $2\text{Cov}(T_1, T_2)$ when computing $V(T_1 + T_2)$ if components share resources.
4. **Underestimating Parallel Latency:** Average parallel execution time $E[\max(T_1, \dots, T_n)]$ is strictly greater than the single-task average $E[T]$.
5. **Sum of Exponentials with Different Rates:** It is a Hypoexponential distribution, not a Gamma distribution.

---

## 5. Solved Exercises

#### Exercise 1: Finding Normalizing Constant $k$ for Joint Processing Times
**Problem:** $f(t_1, t_2) = k \cdot t_1 t_2$ for $0 \le t_1 \le 2$ and $0 \le t_2 \le 3$. Find $k$.
**Solution:**
$$\int_{0}^{2} \int_{0}^{3} k t_1 t_2 \, dt_2 \, dt_1 = k \left[ \frac{t_1^2}{2} \right]_0^2 \left[ \frac{t_2^2}{2} \right]_0^3 = k (2) (4.5) = 9k = 1 \implies k = 1/9$$

#### Exercise 2: Computing Marginal PDFs
**Problem:** Find $f_{T_1}(t_1)$ for $f(t_1, t_2) = \frac{1}{9} t_1 t_2$ on $[0, 2] \times [0, 3]$.
**Solution:**
$$f_{T_1}(t_1) = \int_{0}^{3} \frac{1}{9} t_1 t_2 \, dt_2 = \frac{t_1}{9} \left[ \frac{t_2^2}{2} \right]_0^3 = \frac{4.5 t_1}{9} = \frac{t_1}{2}, \quad 0 \le t_1 \le 2$$

#### Exercise 3: Testing Independence of Time Variables
**Problem:** Are $T_1$ and $T_2$ from Exercise 2 independent?
**Solution:**
$f_{T_2}(t_2) = \frac{2t_2}{9}$. Product $= (\frac{t_1}{2})(\frac{2t_2}{9}) = \frac{t_1 t_2}{9} = f(t_1, t_2)$. Yes, independent.

#### Exercise 4: Conditional PDF $f_{T_1 \mid T_2}(t_1 \mid t_2)$
**Problem:** $f(t_1, t_2) = 8 t_1 t_2$ on $0 \le t_1 \le t_2 \le 1$. Find $f_{T_1 \mid T_2}(t_1 \mid 0.5)$.
**Solution:**
$f_{T_2}(t_2) = \int_0^{t_2} 8 t_1 t_2 dt_1 = 4 t_2^3$.
$$f_{T_1 \mid T_2}(t_1 \mid t_2) = \frac{8 t_1 t_2}{4 t_2^3} = \frac{2 t_1}{t_2^2}$$
For $t_2 = 0.5$, $f(t_1 \mid 0.5) = \frac{2 t_1}{0.25} = 8 t_1$ for $0 \le t_1 \le 0.5$.

#### Exercise 5: Joint Product Moment $E[T_1 T_2]$
**Problem:** $f(t_1, t_2) = \frac{1}{9} t_1 t_2$ on $[0, 2] \times [0, 3]$. Calculate $E[T_1 T_2]$.
**Solution:**
$$E[T_1 T_2] = \int_0^2 \int_0^3 t_1 t_2 \left( \frac{1}{9} t_1 t_2 \right) dt_2 dt_1 = \frac{1}{9} \left[\frac{t_1^3}{3}\right]_0^2 \left[\frac{t_2^3}{3}\right]_0^3 = \frac{1}{9} \times \frac{8}{3} \times 9 = \frac{8}{3}$$

#### Exercise 6: Pearson Correlation Coefficient $\rho$
**Problem:** $V(T_1) = 11/225$, $V(T_2) = 2/75$, $\text{Cov} = 11/300$. Find $\rho$.
**Solution:**
$$\sigma_1 \sigma_2 = \sqrt{\frac{11}{225} \cdot \frac{2}{75}} \approx 0.036055$$
$$\rho = \frac{11/300}{0.036055} \approx \frac{0.036667}{0.036055} \approx 0.9574$$

#### Exercise 7: Variance of Sum with Positive Correlation
**Problem:** $V(T_1) = 25$, $V(T_2) = 36$, $\text{Cov}(T_1, T_2) = 10$. Find $V(T_1 + T_2)$.
**Solution:**
$$V(T_1 + T_2) = 25 + 36 + 2(10) = 81$$

#### Exercise 8: Conditional Expectation for Bivariate Normal Latency
**Problem:** $T_1 \sim N(100, 100), T_2 \sim N(150, 400), \rho = 0.8$. Find $E[T_1 \mid T_2 = 170]$.
**Solution:**
$$E[T_1 \mid T_2 = 170] = 100 + 0.8 \left(\frac{10}{20}\right) (170 - 150) = 100 + 8 = 108$$

#### Exercise 9: Convolution of Two Independent Uniform Stage Times
**Problem:** $T_1, T_2 \sim U(0, 1)$. Find PDF of $Y = T_1 + T_2$.
**Solution:**
$f_Y(y) = \int_0^1 f_{T_1}(t) f_{T_2}(y - t) dt$.
$f_Y(y) = y$ for $0 \le y \le 1$, and $f_Y(y) = 2 - y$ for $1 < y \le 2$.

#### Exercise 10: Parallel Task Bottleneck (Maximum of 3 Uniform RVs)
**Problem:** 3 tasks $T_i \sim U(0, 10)$. Find PDF of $Y_{\max}$.
**Solution:**
$F(t) = t/10$. $F_{(3)}(t) = (t/10)^3 = t^3/1000$.
$f_{(3)}(t) = 3t^2/1000$ for $0 \le t \le 10$.

#### Exercise 11: Expected Parallel Completion Time
**Problem:** Find $E[Y_{\max}]$ from Exercise 10.
**Solution:**
$$E[Y_{\max}] = \int_0^{10} t \left(\frac{3t^2}{1000}\right) dt = \frac{3}{1000} \left[ \frac{t^4}{4} \right]_0^{10} = \frac{30}{4} = 7.5\text{ s}$$

#### Exercise 12: Difference Between Two Normal Execution Times
**Problem:** $T_1 \sim N(100, 25)$ and $T_2 \sim N(90, 16)$, independent. $P(T_1 < T_2)$?
**Solution:**
$D = T_1 - T_2 \sim N(10, 41)$. $z = (0 - 10) / \sqrt{41} = -1.56$.
$P(D < 0) = \Phi(-1.56) = 0.0594 \text{ (5.94\%)}$.

#### Exercise 13: R Code Verification of Order Statistics for Parallel Tasks
**Problem:** Calculate empirical mean of max of 3 uniform $U(0, 10)$ variables.
**Solution:**
```r
t1 <- runif(1000000, 0, 10)
t2 <- runif(1000000, 0, 10)
t3 <- runif(1000000, 0, 10)
t_max <- pmax(t1, t2, t3)
cat("Empirical E:", mean(t_max), "\n") # approx 7.5
```

---

## Phase Summary
Phase 5B extends the statistical toolkit to Multivariate Random Variables, focusing heavily on the interdependencies between operational metrics like sequential phase delays or parallel completion times. Key tools include the Joint PDF for regional probability, and Marginal/Conditional densities to isolate variable behavior. The Covariance and Pearson Correlation ($\rho$) definitively quantify linear co-movement, directly affecting the Variance of Sums (total system jitter increases if stages are positively correlated). Order statistics explicitly model the critical paths: the Maximum ($Y_{\max}$) maps to parallel execution bottlenecks, demonstrating that average system completion time scales strictly worse than single-task averages. Finally, convolution seamlessly provides the probability density of sequential processing times.
