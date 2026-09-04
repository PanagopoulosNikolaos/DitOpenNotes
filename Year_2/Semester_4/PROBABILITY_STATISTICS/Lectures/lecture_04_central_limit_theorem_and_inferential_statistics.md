# Lecture 04: Central Limit Theorem and Inferential Statistics

This lecture covers sampling distributions, the Central Limit Theorem (CLT), Normal approximation to the Binomial distribution with continuity correction, confidence intervals, and hypothesis testing principles.

---

## 1. Sampling Distributions of the Sample Mean

Let $X_1, X_2, \dots, X_n$ be an independent and identically distributed (i.i.d.) random sample drawn from any arbitrary distribution with finite mean $\mu$ and finite variance $\sigma^2$.

The **Sample Mean** estimator is:

$$
\bar{X} = \frac{1}{n} \sum_{i=1}^{n} X_i
$$

### 1.1 Properties of the Estimator
- **Unbiased Expectation:**
  $$E[\bar{X}] = \frac{1}{n} \sum_{i=1}^{n} E[X_i] = \frac{1}{n} (n\mu) = \mu$$
- **Standard Error of the Mean ($\sigma_{\bar{x}}$):**
  $$\text{Var}(\bar{X}) = \frac{1}{n^2} \sum_{i=1}^{n} \text{Var}(X_i) = \frac{1}{n^2} (n\sigma^2) = \frac{\sigma^2}{n} \implies \sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}$$

---

## 2. The Central Limit Theorem (CLT)

### 2.1 Formal Statement
As the sample size $n \to \infty$, the distribution of the standardized sample mean converges in distribution to the standard normal distribution $N(0, 1)$, regardless of the underlying population distribution:

$$
Z_n = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \xrightarrow{d} N(0, 1) \quad \text{as } n \to \infty
$$

**Practical Rule of Thumb:** When $n \ge 30$, the normal distribution provides an accurate approximation for the distribution of $\bar{X}$ even if the population is non-normal or moderately skewed.

---

## 3. Normal Approximation to the Binomial Distribution

Let $X \sim B(n, p)$. Since $X$ can be expressed as the sum of $n$ independent Bernoulli random variables $X = \sum_{i=1}^{n} Y_i$, the CLT applies:

$$
X \approx N(\mu = np, \ \sigma^2 = np(1 - p))
$$

### 3.1 Applicability Rule
Approximation is valid when:

$$
np \ge 5 \quad \text{and} \quad n(1 - p) \ge 5
$$

### 3.2 Continuity Correction
Because a discrete distribution (integers) is approximated by a continuous distribution, an interval adjustment of $\pm 0.5$ is required:
- $P(X = k) \approx P\left( k - 0.5 \le X_{\text{norm}} \le k + 0.5 \right)$
- $P(X \le k) \approx P\left( X_{\text{norm}} \le k + 0.5 \right)$
- $P(X \ge k) \approx P\left( X_{\text{norm}} \ge k - 0.5 \right)$
- $P(k_1 \le X \le k_2) \approx P\left( k_1 - 0.5 \le X_{\text{norm}} \le k_2 + 0.5 \right)$

---

## 4. Confidence Intervals for the Population Mean ($\mu$)

A $(1 - \alpha) \cdot 100\%$ confidence interval provides an interval estimate $[L, U]$ containing the true population mean with confidence probability $1 - \alpha$.

### 4.1 Known Population Variance ($\sigma$ known)
Using the standard normal critical value $z_{\alpha/2}$:

$$
\text{CI}_{1 - \alpha} = \left[ \bar{x} - z_{\alpha/2} \frac{\sigma}{\sqrt{n}}, \ \bar{x} + z_{\alpha/2} \frac{\sigma}{\sqrt{n}} \right]
$$

Standard critical values:
- $90\%$ Confidence ($\alpha = 0.10$): $z_{0.05} = 1.645$
- $95\%$ Confidence ($\alpha = 0.05$): $z_{0.025} = 1.960$
- $99\%$ Confidence ($\alpha = 0.01$): $z_{0.005} = 2.576$

### 4.2 Unknown Population Variance ($\sigma$ unknown, small sample $n < 30$)
When estimating $\sigma$ by sample standard deviation $s$, use Student's $t$-distribution with $\nu = n - 1$ degrees of freedom:

$$
\text{CI}_{1 - \alpha} = \left[ \bar{x} - t_{\alpha/2, n-1} \frac{s}{\sqrt{n}}, \ \bar{x} + t_{\alpha/2, n-1} \frac{s}{\sqrt{n}} \right]
$$

