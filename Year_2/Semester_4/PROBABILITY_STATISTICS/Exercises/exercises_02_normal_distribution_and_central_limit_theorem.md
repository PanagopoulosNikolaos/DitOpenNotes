# Exercises 02: Continuous Normal Distributions and Central Limit Theorem

This practice problem set provides step-by-step solutions for standard normal $Z$-score transformations, cumulative probability lookups, and applying the Central Limit Theorem to sample means.

---

## Problem 1: Normal Distribution and Standard Scores

### Question
The execution time of a database transaction query follows a Normal distribution with mean $\mu = 80 \text{ ms}$ and standard deviation $\sigma = 12 \text{ ms}$ ($X \sim N(80, 144)$).
1. Calculate the probability that a randomly chosen query executes in under $65 \text{ ms}$ ($P(X \le 65)$).
2. Calculate the probability that a query executes between $74 \text{ ms}$ and $95 \text{ ms}$ ($P(74 \le X \le 95)$).
3. Determine the 90th percentile execution time $x_{0.90}$ (the execution time below which $90\%$ of queries complete).

*(Standard normal reference values: $\Phi(-1.25) = 0.1056$, $\Phi(-0.50) = 0.3085$, $\Phi(1.25) = 0.8944$, $\Phi(1.282) = 0.9000$)*

---

### Solution

#### Part 1: Probability of Execution Under 65 ms
Transform $X = 65$ into standard normal score $Z$:
$$Z = \frac{X - \mu}{\sigma} = \frac{65 - 80}{12} = \frac{-15}{12} = -1.25$$

$$
P(X \le 65) = P(Z \le -1.25) = \Phi(-1.25) = \mathbf{0.1056} \ (10.56\%)
$$

#### Part 2: Probability Between 74 ms and 95 ms
Compute $Z$-scores for both bounds:
$$Z_1 = \frac{74 - 80}{12} = \frac{-6}{12} = -0.50$$
$$Z_2 = \frac{95 - 80}{12} = \frac{15}{12} = 1.25$$

$$
P(74 \le X \le 95) = \Phi(Z_2) - \Phi(Z_1) = \Phi(1.25) - \Phi(-0.50) = 0.8944 - 0.3085 = \mathbf{0.5859} \ (58.59\%)
$$

#### Part 3: 90th Percentile
We seek $x$ such that $\Phi\left(\frac{x - 80}{12}\right) = 0.90$.
From the standard normal table, $\Phi(1.282) = 0.9000$.
$$Z_{0.90} = 1.282 \implies \frac{x - 80}{12} = 1.282$$
$$x = 80 + (1.282 \times 12) = 80 + 15.384 = \mathbf{95.38 \text{ ms}}$$

---

## Problem 2: Central Limit Theorem for Sample Means

### Question
A large web service experiences request payload sizes with population mean $\mu = 4.2 \text{ KB}$ and population standard deviation $\sigma = 1.8 \text{ KB}$. The underlying distribution of payload sizes is heavily right-skewed. An engineer observes a random sample of $n = 36$ independent requests.

1. State the sampling distribution of the sample mean payload size $\bar{X}$.
2. Calculate the probability that the sample mean $\bar{X}$ exceeds $4.6 \text{ KB}$.

---

### Solution

#### Part 1: Sampling Distribution of $\bar{X}$
Since $n = 36 \ge 30$, by the **Central Limit Theorem**, the sample mean $\bar{X}$ is approximately normally distributed regardless of the skewness of the underlying population:
- Expected value: $E[\bar{X}] = \mu = 4.2 \text{ KB}$.
- Standard Error:
  $$\sigma_{\bar{X}} = \frac{\sigma}{\sqrt{n}} = \frac{1.8}{\sqrt{36}} = \frac{1.8}{6} = 0.3 \text{ KB}$$
Thus:
$$\bar{X} \approx N(\mu_{\bar{X}} = 4.2, \ \sigma_{\bar{X}}^2 = 0.09)$$

#### Part 2: Probability That $\bar{X} > 4.6 \text{ KB}$
Standardize $\bar{X} = 4.6$:
$$Z = \frac{\bar{X} - \mu_{\bar{X}}}{\sigma_{\bar{X}}} = \frac{4.6 - 4.2}{0.3} = \frac{0.4}{0.3} \approx 1.33$$

$$
P(\bar{X} > 4.6) = 1 - \Phi(1.33) = 1 - 0.9082 = \mathbf{0.0918} \ (9.18\%)
$$
*(Using $\Phi(1.33) = 0.9082$)*

