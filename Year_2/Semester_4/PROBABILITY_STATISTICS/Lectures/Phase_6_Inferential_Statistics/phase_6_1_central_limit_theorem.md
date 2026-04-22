# Phase 6: Inferential Statistics - Central Limit Theorem (CLT)

## 1. Theoretical Foundation

The Central Limit Theorem (CLT) is one of the most fundamental concepts in probability and statistics. It states that, given certain conditions, the sampling distribution of the sample mean will approach a normal distribution as the sample size gets larger, regardless of the shape of the population distribution.

### 1.1 Core Concept

Let $X_1, X_2, \dots, X_n$ be a random sample of size $n$ drawn from a population with an overall mean $\mu$ and a finite variance $\sigma^2$. Let $\bar{X}$ be the sample mean.

According to the CLT, if $n$ is sufficiently large (typically $n \ge 30$), the distribution of the sample mean $\bar{X}$ is approximately normal:

$$ \bar{X} \sim N\left(\mu, \frac{\sigma^2}{n}\right) $$

**Key parameters of the sampling distribution:**
*   **Mean of the sample means:** $\mu_{\bar{X}} = \mu$
*   **Variance of the sample means:** $\sigma_{\bar{X}}^2 = \frac{\sigma^2}{n}$
*   **Standard Error (Standard deviation of the sample means):** $\sigma_{\bar{X}} = \frac{\sigma}{\sqrt{n}}$

### 1.2 The Standard Normal Transformation (Z-Score)

To calculate probabilities involving $\bar{X}$, we standardize it to the standard normal distribution $Z \sim N(0, 1)$ using the formula:

$$ Z = \frac{\bar{X} - \mu}{\frac{\sigma}{\sqrt{n}}} $$

### 1.3 Sum of Random Variables

The CLT also applies to the sum of the sample observations, $S_n = X_1 + X_2 + \dots + X_n$. As $n$ increases, the distribution of $S_n$ approaches a normal distribution:

$$ S_n \sim N(n\mu, n\sigma^2) $$

Standardizing the sum gives:

$$ Z = \frac{S_n - n\mu}{\sigma\sqrt{n}} $$

### 1.4 Important Caveats and Rules of Thumb
*   **Sample Size:** A general rule of thumb is that $n \ge 30$ is "sufficiently large" for the CLT to apply, even if the underlying population is highly skewed.
*   **Normal Population:** If the underlying population is *already* normally distributed, then the sample mean $\bar{X}$ is exactly normally distributed for *any* sample size $n$.
*   **Independence:** The sampled observations must be independent.

---

## 2. Step-by-Step Examples

### Example 1: Basic Application of CLT
Suppose the average weight of a certain species of fish is $\mu = 40$ kg with a standard deviation of $\sigma = 8$ kg. A sample of $n = 35$ fish is caught. What is the probability that the average weight of the sample is strictly less than $42$ kg?

**Step 1: Identify given information**
*   $\mu = 40$
*   $\sigma = 8$
*   $n = 35$

**Step 2: Calculate Standard Error**
$$ \sigma_{\bar{X}} = \frac{\sigma}{\sqrt{n}} = \frac{8}{\sqrt{35}} \approx 1.352 $$

**Step 3: Calculate Z-score**
We want $P(\bar{X} < 42)$. Let's standardize $42$:
$$ Z = \frac{42 - 40}{1.352} = \frac{2}{1.352} \approx 1.48 $$

**Step 4: Find the probability**
$$ P(\bar{X} < 42) = P(Z < 1.48) = 0.9306 $$

### Example 2: Probability Between Two Values
An elevator has a maximum weight limit. The weights of people using the elevator have a mean $\mu = 75$ kg and a standard deviation $\sigma = 15$ kg. If 40 people enter the elevator, what is the probability that their average weight is between $70$ kg and $78$ kg?

**Step 1: Standard Error**
$$ \sigma_{\bar{X}} = \frac{15}{\sqrt{40}} \approx 2.37 $$

**Step 2: Z-scores for boundaries**
For $70$: $Z_1 = \frac{70 - 75}{2.37} = -2.11$
For $78$: $Z_2 = \frac{78 - 75}{2.37} = 1.27$

**Step 3: Compute Probability**
$$ P(70 < \bar{X} < 78) = P(-2.11 < Z < 1.27) = P(Z < 1.27) - P(Z < -2.11) $$
$$ = 0.8980 - 0.0174 = 0.8806 $$

### Example 3: Finding a Threshold Value (Inverse Normal)
The mean time to complete a test is 50 minutes with a standard deviation of 10 minutes. For a class of 36 students, what is the average time $x$ such that there is only a 5% chance the class mean exceeds $x$?

**Step 1: Set up the problem**
We want $P(\bar{X} > x) = 0.05$. This implies $P(\bar{X} < x) = 0.95$.

**Step 2: Find corresponding Z-score**
Using a standard normal table, the Z-score for an area of $0.95$ is approximately $1.645$.

**Step 3: Solve for $x$**
$$ 1.645 = \frac{x - 50}{\frac{10}{\sqrt{36}}} $$
$$ 1.645 = \frac{x - 50}{1.667} $$
$$ x - 50 = 2.74 $$
$$ x = 52.74 \text{ minutes} $$

### Example 4: Applying CLT to a Sum
A shipping company loads 50 boxes onto a truck. The weight of each box has a mean of 20 kg and a standard deviation of 4 kg. What is the probability that the total weight of the boxes exceeds 1050 kg?

**Step 1: Identify Sum parameters**
*   $n = 50$, $\mu = 20$, $\sigma = 4$
*   Mean of sum: $n\mu = 50 \times 20 = 1000$
*   Standard deviation of sum: $\sigma\sqrt{n} = 4\sqrt{50} \approx 28.28$

**Step 2: Calculate Z-score**
We want $P(S_n > 1050)$.
$$ Z = \frac{1050 - 1000}{28.28} = \frac{50}{28.28} \approx 1.77 $$

**Step 3: Compute Probability**
$$ P(S_n > 1050) = P(Z > 1.77) = 1 - P(Z \le 1.77) = 1 - 0.9616 = 0.0384 $$

### Example 5: CLT with Unknown Underlying Distribution (Uniform)
A random variable $X$ follows a continuous uniform distribution between 0 and 10. A sample of $n = 45$ is drawn. Find the probability that the sample mean is less than 4.5.

**Step 1: Find Population Mean and Variance**
For a uniform distribution $U(a,b)$:
$$ \mu = \frac{a+b}{2} = \frac{0+10}{2} = 5 $$
$$ \sigma^2 = \frac{(b-a)^2}{12} = \frac{100}{12} = 8.33 $$
$$ \sigma = \sqrt{8.33} \approx 2.89 $$

**Step 2: Calculate Standard Error**
$$ \sigma_{\bar{X}} = \frac{2.89}{\sqrt{45}} \approx 0.43 $$

**Step 3: Z-score and Probability**
$$ Z = \frac{4.5 - 5}{0.43} = -1.16 $$
$$ P(\bar{X} < 4.5) = P(Z < -1.16) = 0.1230 $$

### Example 6: Determining Minimum Sample Size
A lightbulb manufacturer knows that the lifespan of its bulbs has a standard deviation of $\sigma = 50$ hours. How large of a sample is needed to ensure that there is at least a 99% probability that the sample mean is within 15 hours of the true population mean?

**Step 1: Set up the probability statement**
We want $P(|\bar{X} - \mu| \le 15) \ge 0.99$.
This is equivalent to $P(-15 \le \bar{X} - \mu \le 15) \ge 0.99$.

**Step 2: Convert to Z-scores**
Divide the inequality by $\sigma_{\bar{X}} = \frac{50}{\sqrt{n}}$:
$$ P\left(\frac{-15}{50/\sqrt{n}} \le Z \le \frac{15}{50/\sqrt{n}}\right) \ge 0.99 $$
Let $Z_c = \frac{15\sqrt{n}}{50}$. We want the area between $-Z_c$ and $Z_c$ to be 0.99.

**Step 3: Find critical Z-value**
For a central area of 0.99, the tails have $0.005$ each. The $Z$-score for an area of $0.995$ to the left is approximately $2.576$.
So, $Z_c = 2.576$.

**Step 4: Solve for $n$**
$$ \frac{15\sqrt{n}}{50} \ge 2.576 $$
$$ \sqrt{n} \ge \frac{50 \times 2.576}{15} \approx 8.587 $$
$$ n \ge (8.587)^2 \approx 73.7 $$
Since sample size must be an integer, we round up to $n = 74$.

---

### Example 7: The "Single Observation vs. Sample Mean" Trap (Gotcha Moment)
The resting heart rate of adults is normally distributed with a mean of 72 beats per minute (bpm) and a standard deviation of 8 bpm. 
**Part A:** What is the probability that a *randomly selected individual* has a heart rate above 75 bpm?
**Part B:** What is the probability that a *random sample of 16 adults* has a sample mean heart rate above 75 bpm?

#### Gotcha Section Analysis
A very common mistake in exams is confusing the distribution of the population with the distribution of the sample mean. If the question asks about ONE individual, you do not use the CLT adjustment ($\sqrt{n}$). If it asks about a SAMPLE, you must divide the standard deviation by $\sqrt{n}$. Furthermore, $n=16$ is less than 30, but because the underlying population is explicitly stated to be *normally distributed*, the sampling distribution of the mean is exactly normal regardless of sample size.

**Solution Part A (Single Individual):**
We are looking for $P(X > 75)$. We use the population standard deviation $\sigma = 8$.
$$ Z = \frac{75 - 72}{8} = 0.375 $$
$$ P(X > 75) = P(Z > 0.375) = 1 - P(Z \le 0.375) = 1 - 0.6462 = 0.3538 $$

**Solution Part B (Sample Mean):**
We are looking for $P(\bar{X} > 75)$. We use the standard error $\sigma_{\bar{X}} = \frac{8}{\sqrt{16}} = \frac{8}{4} = 2$.
$$ Z = \frac{75 - 72}{2} = 1.5 $$
$$ P(\bar{X} > 75) = P(Z > 1.5) = 1 - P(Z \le 1.5) = 1 - 0.9332 = 0.0668 $$

Notice how drastically different the probabilities are. It is much harder for a group average to deviate from the true mean than it is for a single individual.

---

### Example 8: Sum vs. Mean Trap combined with Proportions (Gotcha Moment)
A biased coin has a probability $p = 0.6$ of landing heads. You flip the coin 400 times. What is the probability that the number of heads obtained is exactly 240? What is the probability that the *proportion* of heads is greater than 0.65?

#### Gotcha Section Analysis
There are two distinct traps here:
1. **Continuity Correction:** When using the CLT to approximate a discrete distribution (like the Binomial distribution) with a continuous Normal distribution, you MUST apply the continuity correction if you are asking for an exact value or specific bounds.
2. **Proportion vs Sum:** A binomial variable $X$ is a sum of Bernoulli trials. The sample proportion $\hat{p}$ is the sample mean of Bernoulli trials ($\hat{p} = \frac{X}{n}$). You must use the correct parameters for each.

**Solution Part A (Exact Value using Continuity Correction):**
The number of heads $X \sim Binomial(n=400, p=0.6)$.
Using normal approximation:
*   Mean: $\mu = np = 400(0.6) = 240$
*   Standard Deviation: $\sigma = \sqrt{np(1-p)} = \sqrt{400(0.6)(0.4)} = \sqrt{96} \approx 9.798$

To find $P(X = 240)$, we must use the interval $(239.5, 240.5)$ because $X$ is discrete.
$$ Z_1 = \frac{239.5 - 240}{9.798} \approx -0.05 $$
$$ Z_2 = \frac{240.5 - 240}{9.798} \approx 0.05 $$
$$ P(X = 240) \approx P(-0.05 < Z < 0.05) = 0.5199 - 0.4801 = 0.0398 $$
*(Without continuity correction, the probability of an exact value in a continuous distribution is 0, which is a fatal error!)*

**Solution Part B (Proportions):**
We want the probability that the sample proportion $\hat{p} > 0.65$.
According to the CLT for proportions, $\hat{p} \sim N\left(p, \frac{p(1-p)}{n}\right)$.
*   Mean: $\mu_{\hat{p}} = p = 0.6$
*   Standard Error: $\sigma_{\hat{p}} = \sqrt{\frac{p(1-p)}{n}} = \sqrt{\frac{0.6(0.4)}{400}} = \sqrt{\frac{0.24}{400}} = 0.0245$

Without correction (commonly accepted for very large $n$ in proportion tests):
$$ Z = \frac{0.65 - 0.6}{0.0245} \approx 2.04 $$
$$ P(\hat{p} > 0.65) = P(Z > 2.04) = 1 - 0.9793 = 0.0207 $$
*(Always check if your professor requires continuity correction for proportions!)*
