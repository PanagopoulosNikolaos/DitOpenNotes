# Lecture 03: Discrete and Continuous Probability Distributions

This lecture covers random variables, Probability Mass Functions (PMF), Probability Density Functions (PDF), Cumulative Distribution Functions (CDF), expected value and variance properties, the Binomial distribution, and the continuous Normal (Gaussian) distribution.

---

## 1. Random Variables and Distribution Functions

A random variable $X: \Omega \to \mathbb{R}$ is a measurable function mapping experimental sample space outcomes to real numbers.

### 1.1 Cumulative Distribution Function (CDF)
For any random variable $X$, the CDF $F(x)$ is defined as:

$$
F(x) = P(X \le x) \quad \text{for } -\infty < x < \infty
$$

Properties:
- Non-decreasing: $x_1 < x_2 \implies F(x_1) \le F(x_2)$.
- Asymptotes: $\lim_{x \to -\infty} F(x) = 0$, $\lim_{x \to \infty} F(x) = 1$.
- Interval probability: $P(a < X \le b) = F(b) - F(a)$.

---

## 2. Discrete Random Variables and the Binomial Distribution

A discrete random variable takes values in a countable set $\{x_1, x_2, \dots\}$ with Probability Mass Function (PMF) $p(x) = P(X = x)$:

$$
\sum_{i} p(x_i) = 1.0, \quad p(x_i) \ge 0
$$

### 2.1 Expected Value and Variance
- **Expected Value:**
  $$E[X] = \mu = \sum_i x_i \cdot p(x_i)$$
- **Variance:**
  $$\text{Var}(X) = \sigma^2 = E[(X - \mu)^2] = E[X^2] - (E[X])^2 = \sum_i x_i^2 p(x_i) - \mu^2$$

### 2.2 The Binomial Distribution: $B(n, p)$
Models the number of successes $k$ in $n$ independent Bernoulli trials with constant success probability $p$:

$$
P(X = k) = \binom{n}{k} p^k (1 - p)^{n - k} \quad \text{for } k = 0, 1, 2, \dots, n
$$

Where the binomial coefficient is:

$$
\binom{n}{k} = \frac{n!}{k!(n - k)!}
$$

- **Expected Value:** $E[X] = n \cdot p$.
- **Variance:** $\text{Var}(X) = n \cdot p \cdot (1 - p)$.
- **Standard Deviation:** $\sigma = \sqrt{n p (1 - p)}$.

---

## 3. Continuous Random Variables and the Normal Distribution

A continuous random variable takes values over continuous intervals with Probability Density Function (PDF) $f(x) \ge 0$:

$$
\int_{-\infty}^{\infty} f(x) \, dx = 1.0, \quad P(a \le X \le b) = \int_{a}^{b} f(x) \, dx
$$

Note that for any individual exact point $c$, $P(X = c) = 0$.

### 3.1 The Normal (Gaussian) Distribution: $N(\mu, \sigma^2)$
The probability density function is bell-shaped and symmetric about mean $\mu$:

$$
f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2\sigma^2}} \quad \text{for } -\infty < x < \infty
$$

### 3.2 Standard Normal Distribution: $Z \sim N(0, 1)$
Any normal random variable $X \sim N(\mu, \sigma^2)$ transforms into standard normal $Z$ via **$Z$-score standardization**:

$$
Z = \frac{X - \mu}{\sigma}
$$

The standard normal CDF is tabulated as $\Phi(z)$:

$$
\Phi(z) = P(Z \le z) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{z} e^{-\frac{u^2}{2}} \, du
$$

Symmetry identities for standard normal table lookups:
- $\Phi(-z) = 1 - \Phi(z)$.
- $P(a \le X \le b) = \Phi\left(\frac{b - \mu}{\sigma}\right) - \Phi\left(\frac{a - \mu}{\sigma}\right)$.
- $P(X > c) = 1 - \Phi\left(\frac{c - \mu}{\sigma}\right)$.

