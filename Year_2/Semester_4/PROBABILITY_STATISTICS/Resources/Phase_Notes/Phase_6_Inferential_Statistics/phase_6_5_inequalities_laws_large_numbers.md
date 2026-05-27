# Phase 6.5: Probability Inequalities and Laws of Large Numbers

This file covers fundamental probability bounds (**Markov's Inequality** and **Chebyshev's Inequality**) and the asymptotic behaviors of sample averages (**Weak and Strong Laws of Large Numbers**).

---

## 1. Probability Inequalities

Probability inequalities allow us to bound the probability of tail events when the exact distribution of a random variable is unknown or complex, requiring only its moments (like mean and variance).

### 1.1 Markov's Inequality
Let $X$ be a **non-negative** random variable ($X \ge 0$). For any constant $a > 0$:

$$P(X \ge a) \le \frac{E[X]}{a}$$

### 1.2 Chebyshev's Inequality
Let $X$ be any random variable with mean $\mu$ and variance $\sigma^2 > 0$. For any constant $\epsilon > 0$:

$$P(|X - \mu| \ge \epsilon) \le \frac{Var(X)}{\epsilon^2}$$

Alternatively, setting $\epsilon = k\sigma$ (where $k > 0$ is the number of standard deviations from the mean):

$$P(|X - \mu| \ge k\sigma) \le \frac{1}{k^2}$$

This states that the probability of any random variable falling more than $k$ standard deviations away from its mean is at most $1/k^2$. E.g., for $k=2$, at least $75\%$ of the data must lie within 2 standard deviations of the mean.

---

## 2. Laws of Large Numbers (LLN)

Let $X_1, X_2, \dots$ be a sequence of independent and identically distributed (i.i.d.) random variables, each with mean $E[X_i] = \mu$ and variance $Var(X_i) = \sigma^2$. The sample mean is:

$$\bar{X}_n = \frac{1}{n} \sum_{i=1}^{n} X_i$$

### 2.1 The Weak Law of Large Numbers (WLLN)
As the sample size $n$ approaches infinity, the sample mean converges in **probability** to the population mean $\mu$. That is, for any $\epsilon > 0$:

$$\lim_{n \to \infty} P(|\bar{X}_n - \mu| \ge \epsilon) = 0$$

### 2.2 The Strong Law of Large Numbers (SLLN)
As the sample size $n$ approaches infinity, the sample mean converges **almost surely** (with probability 1) to the population mean $\mu$:

$$P\left( \lim_{n \to \infty} \bar{X}_n = \mu \right) = 1$$

---

## 3. Solved Exercises (9 Examples)

### Exercise 1: Basic Markov's Inequality
**Problem:** A post office handles an average of 10,000 letters per day. What is the maximum probability that it will handle at least 15,000 letters tomorrow?

**Solution:**
- **Step 1: Check conditions and identify parameters.**
  The number of letters $X \ge 0$, and we are given $E[X] = 10,000$.
- **Step 2: WIP State.**
  Apply Markov's Inequality with $a = 15,000$:
  $$P(X \ge 15,000) \le \frac{E[X]}{15,000} = \frac{10,000}{15,000} = ?$$
- **Step 3: Final Calculation.**
  $$P(X \ge 15,000) \le \frac{2}{3} \approx 0.6667.$$

---

### Exercise 2: Basic Chebyshev's Inequality
**Problem:** The height of adults in a city has a mean of 170 cm and a standard deviation of 8 cm. Find the upper bound for the probability that a randomly chosen adult has a height outside the range $(154 \text{ cm}, 186 \text{ cm})$.

**Solution:**
- **Step 1: Map the range to the inequality format $|X - \mu| \ge \epsilon$.**
  - $\mu = 170$
  - $\sigma = 8 \implies Var(X) = 64$.
  - The range $(154, 186)$ is $(170 - 16, 170 + 16)$, which corresponds to $\epsilon = 16$.
- **Step 2: WIP State.**
  Apply Chebyshev's Inequality:
  $$P(|X - 170| \ge 16) \le \frac{Var(X)}{16^2} = \frac{64}{256} = ?$$
- **Step 3: Final Calculation.**
  $$P(|X - 170| \ge 16) \le \frac{1}{4} = 0.25.$$

---

### Exercise 3: Chebyshev's Inequality vs. Normal Distribution
**Problem:** For the height data in Exercise 2 (assuming height is normally distributed), find the exact probability of being outside $(154 \text{ cm}, 186 \text{ cm})$, and compare it to Chebyshev's bound. (Recall $\Phi(2) = 0.9772$).

**Solution:**
- **Step 1: Convert the range to Z-scores.**
  - Lower bound Z-score: $z_1 = \frac{154 - 170}{8} = -2$
  - Upper bound Z-score: $z_2 = \frac{186 - 170}{8} = 2$
- **Step 2: WIP State.**
  Calculate the exact probability:
  $$P(|Z| \ge 2) = 2 \cdot P(Z < -2) = 2(1 - \Phi(2)) = 2(1 - 0.9772) = 2 \cdot ?$$
- **Step 3: Final Calculation.**
  - $2 \cdot 0.0228 = 0.0456$.
  **Comparison:** Chebyshev's bound is $0.25$, which is much wider than the exact probability $0.0456$. This illustrates that while Chebyshev's inequality is guaranteed to hold for *any* distribution, it can be very conservative for specific distributions like the normal distribution.

---

### Exercise 4: Sample Size Determination using Chebyshev
**Problem:** A coin is flipped $n$ times. We want to estimate the probability of heads $p$ using the sample proportion $\hat{p}_n$. Use Chebyshev's inequality to find the minimum number of flips $n$ required to be at least $95\%$ confident that $\hat{p}_n$ is within $0.05$ of the true probability $p$.

**Solution:**
- **Step 1: Identify mean and variance of $\hat{p}_n$.**
  Let $X_i \sim Bernoulli(p)$ for $i=1,\dots,n$.
  - $E[\hat{p}_n] = p$
  - $Var(\hat{p}_n) = \frac{p(1-p)}{n}$.
- **Step 2: WIP State.**
  We want to find $n$ such that:
  $$P(|\hat{p}_n - p| < 0.05) \ge 0.95 \implies P(|\hat{p}_n - p| \ge 0.05) \le 0.05$$
  Apply Chebyshev's Inequality:
  $$P(|\hat{p}_n - p| \ge 0.05) \le \frac{Var(\hat{p}_n)}{0.05^2} = \frac{p(1-p)}{n \cdot 0.0025}$$
  Since we don't know $p$, we use the worst-case variance value, which occurs at $p = 0.5 \implies p(1-p) = 0.25$.
  $$P(|\hat{p}_n - p| \ge 0.05) \le \frac{0.25}{n \cdot 0.0025} = \frac{100}{n}$$
  We set this upper bound $\le 0.05$:
  $$\frac{100}{n} \le 0.05 \implies n \ge ?$$
- **Step 3: Final Calculation.**
  $$n \ge \frac{100}{0.05} = 2000 \text{ flips}.$$

---

### Exercise 5: Bound for Exponential Variable (Markov vs Chebyshev)
**Problem:** Let $X \sim Exp(1)$. Compare the upper bounds of $P(X \ge 3)$ given by Markov's and Chebyshev's inequalities with the exact probability.

**Solution:**
- **Step 1: Identify moments and exact value.**
  - Mean $E[X] = 1$, Variance $Var(X) = 1$.
  - Exact probability: $P(X \ge 3) = e^{-3} \approx 0.0498$.
- **Step 2: WIP State.**
  - **Markov's Bound:**
    $$P(X \ge 3) \le \frac{E[X]}{3} = \frac{1}{3} \approx 0.3333$$
  - **Chebyshev's Bound:**
    Note that $P(X \ge 3) = P(X - 1 \ge 2)$. Since $X \ge 0$:
    $$P(X \ge 3) \le P(|X - 1| \ge 2) \le \frac{Var(X)}{2^2} = \frac{1}{4} = ?$$
- **Step 3: Final Calculation.**
  - Chebyshev's bound $= 0.25$.
  - **Comparison:** The exact value is $0.0498$. Chebyshev's bound ($0.25$) is tighter than Markov's bound ($0.3333$), but both are much larger than the true value.

---

### Exercise 6: One-Sided Chebyshev Inequality (Cantelli's Inequality)
**Problem:** Let $X$ have mean $\mu$ and variance $\sigma^2$. Cantelli's inequality states that for any $a > 0$:
$$P(X - \mu \ge a) \le \frac{\sigma^2}{\sigma^2 + a^2}$$
If the test scores have a mean of 70 and variance of 25, find the upper bound for the probability that a student scores at least 85.

**Solution:**
- **Step 1: Map variables.**
  - $\mu = 70$
  - $\sigma^2 = 25$
  - We want $P(X \ge 85) = P(X - 70 \ge 15)$, so $a = 15$.
- **Step 2: WIP State.**
  Apply Cantelli's inequality:
  $$P(X - 70 \ge 15) \le \frac{25}{25 + 15^2} = \frac{25}{25 + 225} = \frac{25}{?}$$
- **Step 3: Final Calculation.**
  - Denominator $= 250$.
  - $P(X - 70 \ge 15) \le \frac{25}{250} = 0.1$.

---

### Exercise 7: Applying WLLN to Sample Variance
**Problem:** Let $X_1, X_2, \dots$ be i.i.d. random variables with mean $\mu$ and finite 4th moment ($E[X^4] < \infty$). Show that the sample variance $S_n^2$ converges in probability to the population variance $\sigma^2$ as $n \to \infty$.

**Solution:**
- **Step 1: Write the expansion of $S_n^2$.**
  $$S_n^2 = \frac{1}{n-1} \sum_{i=1}^{n} (X_i - \bar{X}_n)^2 = \frac{n}{n-1} \left( \frac{1}{n}\sum_{i=1}^{n} X_i^2 - \bar{X}_n^2 \right)$$
- **Step 2: WIP State.**
  - As $n \to \infty$, $\frac{n}{n-1} \to 1$.
  - Let $Y_i = X_i^2$. Since $X_i$ are i.i.d., $Y_i$ are also i.i.d. with mean $E[Y_i] = E[X_i^2]$. By WLLN:
    $$\frac{1}{n}\sum_{i=1}^{n} X_i^2 \xrightarrow{P} E[X^2]$$
  - By WLLN, $\bar{X}_n \xrightarrow{P} \mu$. Since the square function is continuous, $\bar{X}_n^2 \xrightarrow{P} \mu^2$.
- **Step 3: Final Calculation.**
  Using the properties of convergence in probability:
  $$S_n^2 \xrightarrow{P} 1 \cdot \left( E[X^2] - \mu^2 \right) = \sigma^2.$$

---

### Exercise 8: Chebyshev Bound for Sample Mean
**Problem:** Let $X_1, \dots, X_n$ be i.i.d. random variables with mean $\mu$ and variance $\sigma^2$. Show that for any $\epsilon > 0$, WLLN holds by using Chebyshev's inequality on the sample mean $\bar{X}_n$.

**Solution:**
- **Step 1: Find properties of $\bar{X}_n$.**
  - $E[\bar{X}_n] = \mu$
  - $Var(\bar{X}_n) = \frac{\sigma^2}{n}$
- **Step 2: WIP State.**
  Apply Chebyshev's Inequality:
  $$P(|\bar{X}_n - \mu| \ge \epsilon) \le \frac{Var(\bar{X}_n)}{\epsilon^2} = \frac{\sigma^2}{n\epsilon^2}$$
- **Step 3: Final Calculation.**
  Take the limit as $n \to \infty$:
  $$\lim_{n \to \infty} P(|\bar{X}_n - \mu| \ge \epsilon) \le \lim_{n \to \infty} \frac{\sigma^2}{n\epsilon^2} = 0$$
  Since probability is non-negative, the limit must be exactly 0, proving WLLN.

---

### Exercise 9: Monte Carlo Integration (LLN Application)
**Problem:** Explain how the Law of Large Numbers justifies using random numbers to estimate the value of the integral $I = \int_{0}^{1} g(x) \, dx$.

**Solution:**
- **Step 1: Relate the integral to an expectation.**
  Let $U \sim U(0, 1)$. The expected value of $g(U)$ is:
  $$E[g(U)] = \int_{0}^{1} g(x) \cdot f_U(x) \, dx = \int_{0}^{1} g(x) \cdot 1 \, dx = I$$
- **Step 2: WIP State.**
  Generate $n$ independent random variables $U_1, U_2, \dots, U_n$ from $U(0, 1)$.
  Let $Y_i = g(U_i)$. The variables $Y_i$ are i.i.d. with mean $E[Y_i] = I$.
- **Step 3: Final Calculation.**
  By the Law of Large Numbers, the sample mean converges to the expected value:
  $$\frac{1}{n} \sum_{i=1}^{n} g(U_i) \xrightarrow{a.s.} E[g(U)] = I$$
  This justifies approximating the integral by the average value of the function evaluated at random points.
