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


# Phase 6: Inferential Statistics - Confidence Intervals

## 1. Theoretical Foundation

A **Confidence Interval (CI)** provides a range of plausible values for an unknown population parameter (like the mean $\mu$ or proportion $p$). Instead of a single point estimate (like $\bar{X}$ or $\hat{p}$), a confidence interval gives a margin of error around the point estimate, along with a specified level of confidence that the true parameter lies within that interval.

### 1.1 Core Concept

The general formula for a confidence interval is:
$$ \text{Point Estimate} \pm \text{Margin of Error} $$
$$ \text{Point Estimate} \pm (\text{Critical Value}) \times (\text{Standard Error}) $$

The **Confidence Level** is denoted by $(1 - \alpha) \times 100\%$, where $\alpha$ is the significance level. For example, a 95% confidence level means $\alpha = 0.05$. The critical value separates the tail area $\alpha/2$ from the central area.

### 1.2 Confidence Interval for Population Mean ($\mu$)

#### Case A: Population Standard Deviation ($\sigma$) is KNOWN
When $\sigma$ is known and either the population is normal or $n \ge 30$, we use the Standard Normal (Z) distribution.
$$ CI = \bar{X} \pm Z_{\alpha/2} \left( \frac{\sigma}{\sqrt{n}} \right) $$
*   $\bar{X}$ = Sample mean
*   $Z_{\alpha/2}$ = Z critical value (e.g., 1.96 for 95% confidence)
*   $\frac{\sigma}{\sqrt{n}}$ = Standard Error

#### Case B: Population Standard Deviation ($\sigma$) is UNKNOWN
When $\sigma$ is unknown, we estimate it using the sample standard deviation $s$. We must use the Student's t-distribution with $n - 1$ degrees of freedom ($df$).
$$ CI = \bar{X} \pm t_{\alpha/2, n-1} \left( \frac{s}{\sqrt{n}} \right) $$
*   $s$ = Sample standard deviation
*   $t_{\alpha/2, n-1}$ = t critical value with $df = n - 1$

### 1.3 Confidence Interval for Population Proportion ($p$)

When dealing with proportions (e.g., "what percentage of voters favor candidate A?"), we use the sample proportion $\hat{p} = \frac{x}{n}$ (where $x$ is the number of successes).
Assuming large sample sizes ($n\hat{p} \ge 10$ and $n(1-\hat{p}) \ge 10$), we use the Z-distribution:
$$ CI = \hat{p} \pm Z_{\alpha/2} \sqrt{ \frac{\hat{p}(1-\hat{p})}{n} } $$

### 1.4 Sample Size Determination
To achieve a specific Margin of Error ($E$) at a given confidence level:
**For Mean:**
$$ n = \left( \frac{Z_{\alpha/2} \cdot \sigma}{E} \right)^2 $$
**For Proportion:**
$$ n = \hat{p}(1-\hat{p}) \left( \frac{Z_{\alpha/2}}{E} \right)^2 $$
*(If $\hat{p}$ is completely unknown, use $\hat{p} = 0.5$ for the most conservative (largest) sample size).*

---

## 2. Step-by-Step Examples

### Example 1: CI for Mean ($\sigma$ known)
A random sample of 50 apples has a mean weight of 150g. The population standard deviation is known to be 10g. Construct a 95% confidence interval for the true mean weight of all apples.

**Step 1: Identify Given Information**
*   $n = 50$, $\bar{X} = 150$, $\sigma = 10$
*   Confidence level = 95%, so $\alpha = 0.05$ and $\alpha/2 = 0.025$

**Step 2: Find Critical Value**
For a 95% CI, $Z_{0.025} = 1.96$ (from standard normal table).

**Step 3: Calculate Margin of Error (E)**
$$ E = Z_{\alpha/2} \left( \frac{\sigma}{\sqrt{n}} \right) = 1.96 \left( \frac{10}{\sqrt{50}} \right) = 1.96 \times 1.414 \approx 2.77 $$

**Step 4: Construct Interval**
$$ CI = 150 \pm 2.77 = [147.23, 152.77] $$

### Example 2: CI for Mean ($\sigma$ unknown)
A sample of 16 laptop batteries has a mean life of 4.5 hours with a sample standard deviation of 0.8 hours. Assume the population is normally distributed. Find a 99% CI for the true mean battery life.

**Step 1: Identify Given Information**
*   $n = 16$, $\bar{X} = 4.5$, $s = 0.8$
*   Since $\sigma$ is unknown, use t-distribution. $df = n - 1 = 15$.
*   Confidence level = 99%, $\alpha = 0.01$, $\alpha/2 = 0.005$.

**Step 2: Find Critical Value**
From t-table for $df=15$ and tail area 0.005: $t_{0.005, 15} = 2.947$.

**Step 3: Calculate Margin of Error (E)**
$$ E = 2.947 \left( \frac{0.8}{\sqrt{16}} \right) = 2.947 \times 0.2 = 0.5894 $$

**Step 4: Construct Interval**
$$ CI = 4.5 \pm 0.5894 = [3.91, 5.09] $$

### Example 3: CI for Proportion
In a survey of 400 randomly selected adults, 250 said they drink coffee daily. Construct a 90% confidence interval for the true proportion of adults who drink coffee daily.

**Step 1: Calculate Sample Proportion**
$$ \hat{p} = \frac{x}{n} = \frac{250}{400} = 0.625 $$

**Step 2: Find Critical Value**
For 90% confidence, $\alpha = 0.10$, $\alpha/2 = 0.05$. $Z_{0.05} = 1.645$.

**Step 3: Calculate Margin of Error (E)**
$$ E = 1.645 \sqrt{ \frac{0.625(1-0.625)}{400} } = 1.645 \sqrt{\frac{0.234375}{400}} \approx 1.645 \times 0.0242 \approx 0.0398 $$

**Step 4: Construct Interval**
$$ CI = 0.625 \pm 0.0398 = [0.5852, 0.6648] $$

### Example 4: Finding Required Sample Size (Mean)
We want to estimate the mean height of students in a university to within 2 cm with 95% confidence. The population standard deviation is estimated to be 8 cm. How large of a sample is required?

**Step 1: Identify Given Information**
*   $E = 2$ (Margin of error)
*   $\sigma = 8$
*   $Z_{\alpha/2}$ for 95% is $1.96$

**Step 2: Apply Sample Size Formula**
$$ n = \left( \frac{1.96 \times 8}{2} \right)^2 = (1.96 \times 4)^2 = (7.84)^2 = 61.4656 $$

**Step 3: Round Up**
Always round sample size *up* to the next whole number. $n = 62$.

### Example 5: Changing Confidence Levels
Using the data from Example 1 ($n=50, \bar{X}=150, \sigma=10$), what happens to the confidence interval if we increase the confidence level to 99%?

**Step 1: New Critical Value**
For 99%, $Z_{0.005} = 2.576$.

**Step 2: New Margin of Error**
$$ E = 2.576 \left( \frac{10}{\sqrt{50}} \right) \approx 3.64 $$

**Step 3: New Interval**
$$ CI = 150 \pm 3.64 = [146.36, 153.64] $$
*Observation: Higher confidence requires a wider interval.*

### Example 6: Extracting Information from an Interval
A 95% confidence interval for a population mean is given as $[45, 55]$. What was the sample mean and the margin of error?

**Step 1: Find the Sample Mean**
The sample mean is exactly in the middle of the interval.
$$ \bar{X} = \frac{\text{Upper} + \text{Lower}}{2} = \frac{55 + 45}{2} = 50 $$

**Step 2: Find the Margin of Error**
The margin of error is half the width of the interval.
$$ E = \frac{\text{Upper} - \text{Lower}}{2} = \frac{55 - 45}{2} = 5 $$

---

### Example 7: The "Z vs. t" Trap and Degrees of Freedom (Gotcha Moment)
A researcher measures the lifespan of 25 fruit flies. The sample mean is 14 days and the *sample variance* is 16 days squared. Construct a 95% confidence interval for the population mean lifespan.

#### Gotcha Section Analysis
There are three common traps here:
1. **Variance vs. Standard Deviation:** The problem gives the sample *variance* ($s^2 = 16$), not standard deviation. You must take the square root ($s = 4$).
2. **t vs Z:** Many students automatically use $Z=1.96$ because it is a 95% interval. However, because we only have the *sample* variance (and $n < 30$), we MUST use the t-distribution.
3. **Degrees of Freedom:** For $n=25$, degrees of freedom is $df = 24$, not 25.

**Step 1: Extract Correct Values**
*   $n = 25 \implies df = 24$
*   $\bar{X} = 14$
*   $s^2 = 16 \implies s = 4$

**Step 2: Find the correct Critical Value (t-distribution)**
For 95% confidence ($\alpha = 0.05, \alpha/2 = 0.025$) and $df = 24$:
$t_{0.025, 24} = 2.064$ (NOT 1.96!)

**Step 3: Calculate Margin of Error and CI**
$$ E = 2.064 \left( \frac{4}{\sqrt{25}} \right) = 2.064 \left( \frac{4}{5} \right) = 2.064 \times 0.8 = 1.6512 $$
$$ CI = 14 \pm 1.6512 = [12.3488, 15.6512] $$

---

### Example 8: Worst-Case Proportion Sample Size Trap (Gotcha Moment)
You are planning a survey to estimate the proportion of students who prefer online exams. You want the estimate to be accurate within 4 percentage points with 95% confidence. Previous studies suggest the proportion is somewhere between 20% and 30%. What sample size should you use?

#### Gotcha Section Analysis
There are two traps here:
1. **"Within 4 percentage points":** This means the Margin of Error $E = 0.04$. Do not use $E=4$.
2. **Which $\hat{p}$ to use?** The sample size formula for proportions is $n = \hat{p}(1-\hat{p}) \left( \frac{Z}{E} \right)^2$. If no proportion is known, you use $\hat{p} = 0.5$ because it maximizes $\hat{p}(1-\hat{p})$ to $0.25$, yielding the safest (largest) sample size. However, here you are given a *range* (20% to 30%). You must pick the value in the range that is *closest to 50%* because that will maximize the variance and ensure your sample is large enough.

**Step 1: Determine the conservative $\hat{p}$**
The range is $0.20$ to $0.30$. The value closest to $0.50$ is $0.30$.
Let's check the product $\hat{p}(1-\hat{p})$:
*   If $p=0.20 \implies 0.20 \times 0.80 = 0.16$
*   If $p=0.30 \implies 0.30 \times 0.70 = 0.21$
Since $0.21 > 0.16$, using $p=0.30$ guarantees a large enough sample.

**Step 2: Calculate Sample Size**
*   $Z_{0.025} = 1.96$
*   $E = 0.04$
*   $\hat{p} = 0.30$

$$ n = 0.30(1 - 0.30) \left( \frac{1.96}{0.04} \right)^2 $$
$$ n = 0.30(0.70) \left( 49 \right)^2 $$
$$ n = 0.21 \times 2401 = 504.21 $$

**Step 3: Round Up**
You must always round *up* to the nearest integer to ensure the margin of error is *strictly within* 4%.
$n = 505$.
*(If you used $p=0.5$ blindly without looking at the known range, you would get $n=601$, meaning you would waste time and money surveying 96 extra people unnecessarily!)*


# Phase 6: Inferential Statistics - Hypothesis Testing

## 1. Theoretical Foundation

Hypothesis testing is a formal procedure used to evaluate a claim about a population parameter based on sample data. We compare two competing hypotheses and determine if there is enough statistical evidence to reject the default assumption.

### 1.1 The Hypotheses
*   **Null Hypothesis ($H_0$):** The default assumption, representing "no effect," "no difference," or "status quo." It always contains an equality sign ($=, \le, \ge$).
*   **Alternative Hypothesis ($H_1$ or $H_A$):** The claim we are trying to prove. It contains an inequality sign ($\ne, <, >$). The direction of the inequality determines the type of test:
    *   $\ne$ : Two-tailed test
    *   $<$ : Left-tailed test
    *   $>$ : Right-tailed test

### 1.2 Errors in Hypothesis Testing
*   **Type I Error ($\alpha$):** Rejecting $H_0$ when it is actually true (False Positive). $\alpha$ is the significance level of the test.
*   **Type II Error ($\beta$):** Failing to reject $H_0$ when $H_1$ is actually true (False Negative).
*   **Power of the Test ($1 - \beta$):** The probability of correctly rejecting a false $H_0$.

### 1.3 Test Statistics

The test statistic measures how far our sample statistic is from the hypothesized population parameter, standardized by the standard error.

**1. Test for Mean ($\mu$) with KNOWN Population Variance ($\sigma^2$):**
$$ Z_{stat} = \frac{\bar{X} - \mu_0}{\frac{\sigma}{\sqrt{n}}} $$

**2. Test for Mean ($\mu$) with UNKNOWN Population Variance — Large Sample ($n \ge 30$):**
By the CLT, the sample standard deviation $s$ is a reliable estimate of $\sigma$, so $s$ is substituted into the Z-formula:
$$ Z_{stat} = \frac{\bar{X} - \mu_0}{\frac{s}{\sqrt{n}}} $$
> **Note:** Most courses accept using the t-statistic here as well (with $df = n-1$). Because $t_{n-1} \approx Z$ for large $n$, both approaches give virtually identical results. Confirm which convention your course prefers.

**3. Test for Mean ($\mu$) with UNKNOWN Population Variance — Small Sample ($n < 30$):**
Must use the t-distribution with $df = n - 1$ degrees of freedom:
$$ t_{stat} = \frac{\bar{X} - \mu_0}{\frac{s}{\sqrt{n}}} $$
*(This requires the population to be approximately normally distributed.)*

**4. Test for Proportion ($p$):**
$$ Z_{stat} = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}} $$

### 1.4 Decision Rules

There are two equivalent ways to make a decision:

**1. Critical Value Approach:**
*   Determine the critical value(s) ($Z_{crit}$ or $t_{crit}$) based on $\alpha$ and the tail(s) of the test.
*   If the test statistic falls into the **rejection region** (beyond the critical value), reject $H_0$.

**2. P-Value Approach:**
*   The **p-value** is the probability of observing a test statistic as extreme as, or more extreme than, the one calculated, assuming $H_0$ is true.
*   **Rule:** If $p\text{-value} \le \alpha$, reject $H_0$. If $p\text{-value} > \alpha$, fail to reject $H_0$.

---

## 2. Step-by-Step Examples

### Example 1: Right-Tailed Z-Test for Mean ($\sigma$ known)
A company claims that its new light bulbs last *more than* 1000 hours on average. A sample of 40 bulbs has an average lifespan of 1020 hours. The population standard deviation is known to be 80 hours. Test the claim at a 5% significance level.

**Step 1: State Hypotheses**
*   $H_0: \mu \le 1000$ (Status quo)
*   $H_1: \mu > 1000$ (Claim, right-tailed)

**Step 2: Calculate Test Statistic**
*   $n = 40, \bar{X} = 1020, \mu_0 = 1000, \sigma = 80$
$$ Z_{stat} = \frac{1020 - 1000}{\frac{80}{\sqrt{40}}} = \frac{20}{12.65} \approx 1.58 $$

**Step 3: Determine Critical Value & Decision**
*   $\alpha = 0.05$, right-tailed. $Z_{crit} = 1.645$.
*   Since $1.58 < 1.645$, the statistic is NOT in the rejection region.
*   **Conclusion:** Fail to reject $H_0$. There is not enough evidence to support the claim that the bulbs last more than 1000 hours.

### Example 2: Two-Tailed t-Test for Mean ($\sigma$ unknown)
A machine is supposed to fill bottles with exactly 500ml of water. A random sample of 15 bottles shows a mean of 496ml and a standard deviation of 8ml. Test if the machine is out of calibration at the $\alpha = 0.01$ level.

**Step 1: State Hypotheses**
*   $H_0: \mu = 500$
*   $H_1: \mu \ne 500$ (Two-tailed)

**Step 2: Calculate Test Statistic**
*   $n = 15, \bar{X} = 496, \mu_0 = 500, s = 8$. Use t-test ($df = 14$).
$$ t_{stat} = \frac{496 - 500}{\frac{8}{\sqrt{15}}} = \frac{-4}{2.066} \approx -1.94 $$

**Step 3: Determine Critical Value & Decision**
*   $\alpha = 0.01$, two-tailed. $\alpha/2 = 0.005$.
*   From t-table, $df=14, t_{crit} = \pm 2.977$.
*   Since $-2.977 < -1.94 < 2.977$, it does not fall in the rejection regions.
*   **Conclusion:** Fail to reject $H_0$. No significant evidence the machine is out of calibration.

### Example 3: Left-Tailed Z-Test for Proportion
A politician claims that *less than* 30% of the population opposes a new policy. In a sample of 500 people, 135 oppose the policy. Test the claim at $\alpha = 0.05$.

**Step 1: State Hypotheses**
*   $H_0: p \ge 0.30$
*   $H_1: p < 0.30$ (Claim, left-tailed)

**Step 2: Calculate Test Statistic**
*   $\hat{p} = \frac{135}{500} = 0.27, p_0 = 0.30, n = 500$
$$ Z_{stat} = \frac{0.27 - 0.30}{\sqrt{\frac{0.30(0.70)}{500}}} = \frac{-0.03}{\sqrt{0.00042}} = \frac{-0.03}{0.0205} \approx -1.46 $$

**Step 3: P-Value Approach & Decision**
*   $p\text{-value} = P(Z < -1.46) = 0.0721$
*   Since $0.0721 > 0.05 (\alpha)$, we **Fail to reject $H_0$**.
*   **Conclusion:** Not enough evidence to say less than 30% oppose it.

### Example 4: Calculating Type I Error ($\alpha$)
Given a test where $H_0: \mu = 50$ and we reject $H_0$ if our sample mean $\bar{X} > 52$. We have $n=36, \sigma = 6$. What is the probability of a Type I error?

**Step 1: Define Type I Error**
Type I Error = Rejecting $H_0$ given $H_0$ is true.
$\alpha = P(\bar{X} > 52 \mid \mu = 50)$

**Step 2: Standardize to Z**
$$ Z = \frac{52 - 50}{\frac{6}{\sqrt{36}}} = \frac{2}{1} = 2.0 $$

**Step 3: Find Probability**
$$ \alpha = P(Z > 2.0) = 1 - 0.9772 = 0.0228 $$

### Example 5: Calculating Type II Error ($\beta$)
Following Example 4, what is the probability of a Type II error ($\beta$) if the *true* population mean is actually $\mu_A = 53$?

**Step 1: Define Type II Error**
Type II Error = Failing to reject $H_0$ given $H_1$ is true.
We fail to reject if $\bar{X} \le 52$.
$\beta = P(\bar{X} \le 52 \mid \mu = 53)$

**Step 2: Standardize using the TRUE mean ($\mu_A = 53$)**
$$ Z = \frac{52 - 53}{\frac{6}{\sqrt{36}}} = \frac{-1}{1} = -1.0 $$

**Step 3: Find Probability**
$$ \beta = P(Z \le -1.0) = 0.1587 $$
*(The Power of the test against $\mu_A = 53$ is $1 - \beta = 0.8413$)*

### Example 6: The Connection between CI and Two-Tailed Tests
You have a 95% confidence interval for $\mu$ given as $[12.5, 18.2]$. If you run a two-tailed hypothesis test $H_0: \mu = 19$ vs $H_1: \mu \ne 19$ at $\alpha = 0.05$, what will the conclusion be?

**Step 1: Analyze the Rule**
A two-tailed hypothesis test at significance level $\alpha$ will reject $H_0$ if the hypothesized value $\mu_0$ is *outside* the corresponding $(1-\alpha)\times 100\%$ confidence interval.

**Step 2: Check the Value**
Is 19 inside the interval $[12.5, 18.2]$? No.

**Step 3: Conclusion**
Since 19 is outside the 95% confidence interval, we will **Reject $H_0$** at the 5% significance level.

---

### Example 7: The "P-value Doubling" Trap in Two-Tailed Tests (Gotcha Moment)
A researcher wants to test if a new tutoring method changes exam scores (previously known mean $\mu = 70$, $\sigma = 12$). A sample of 36 students scores an average of 73.5. Calculate the p-value for this test. Is it significant at $\alpha = 0.05$?

#### Gotcha Section Analysis
The key word here is **changes** (not "increases" or "decreases"). This means it is a **two-tailed test** ($H_0: \mu = 70$, $H_1: \mu \ne 70$). A very common mistake is calculating the area in just *one* tail and calling it the p-value. For a two-tailed test, the p-value is the area in BOTH tails combined!

**Step 1: Calculate the Test Statistic**
$$ Z_{stat} = \frac{73.5 - 70}{\frac{12}{\sqrt{36}}} = \frac{3.5}{2} = 1.75 $$

**Step 2: Calculate the Area in One Tail**
Since $Z = 1.75$ is positive, we look at the right tail.
$P(Z > 1.75) = 1 - P(Z \le 1.75) = 1 - 0.9599 = 0.0401$

**Step 3: Calculate the TRUE P-value (The Gotcha)**
Because it is a two-tailed test, we must account for the possibility of extreme results in the other direction.
$$ p\text{-value} = 2 \times P(Z > |Z_{stat}|) $$
$$ p\text{-value} = 2 \times 0.0401 = 0.0802 $$

**Step 4: Decision**
If a student forgot to multiply by 2, they would compare $0.0401 < 0.05$ and incorrectly Reject $H_0$.
Correct comparison: $0.0802 > 0.05$. Therefore, we **Fail to reject $H_0$**. The change is not statistically significant.

---

### Example 8: $H_0$ Phrasing and the Status Quo Trap (Gotcha Moment)
An environmental agency asserts that a local river is polluted, claiming that the average concentration of a toxin is *greater than* the safe limit of 5 ppm. To test this, you take 50 water samples, find a mean of 5.2 ppm, and standard deviation of 0.8 ppm. Formulate the hypotheses and explain what a Type I error means in this specific physical context.

#### Gotcha Section Analysis
There is a massive trap in how the claim is presented. Students often mistakenly put the *researcher's claim* into $H_0$.
**Rule:** $H_0$ MUST contain the equality ($=$ or $\le$ or $\ge$). $H_1$ contains the strictly greater than or less than sign ($>$ or $<$). If the claim is "greater than", the claim itself is $H_1$.
Another trap is contextualizing the error. It's not enough to say "rejecting $H_0$ when true"; you must map it to the physical reality of the river.

**Step 1: Formulate Hypotheses**
*   The claim is $\mu > 5$. This does not contain equality, so it is $H_1$.
*   $H_0: \mu \le 5$ (The river is safe / status quo)
*   $H_1: \mu > 5$ (The river is polluted / agency's claim)

**Step 2: Define Type I Error in Context**
*   **Statistical Definition:** Rejecting $H_0$ when $H_0$ is true.
*   **Physical Translation:** We conclude that $H_1$ is true (the river is polluted) when in reality $H_0$ is true (the river is perfectly safe).
*   **Consequence:** The town might spend millions of dollars cleaning up a river that is not actually polluted, causing a massive waste of resources.

**Step 3: Define Type II Error in Context (Bonus Analysis)**
*   **Statistical Definition:** Failing to reject $H_0$ when $H_1$ is true.
*   **Physical Translation:** We conclude the river is safe ($H_0$), when in reality it IS polluted ($H_1$).
*   **Consequence:** People drink poisoned water, causing a massive public health crisis.
*(In this scenario, a Type II error is far more dangerous to human life than a Type I error, which is why the agency might push for a higher $\alpha$ level to reduce $\beta$!)*


# Phase 6.4: Sampling Distributions, Chi-Square, t, and F Distributions

In inferential statistics, we use sample statistics (like the sample mean $\bar{X}$ or sample variance $S^2$) to estimate population parameters (like $\mu$ or $\sigma^2$). The probability distributions of these statistics are called **sampling distributions**.

---

## 1. Distribution of the Sample Variance ($S^2$)

Let $X_1, X_2, \dots, X_n$ be a random sample of size $n$ from a **Normal population** $N(\mu, \sigma^2)$. The sample variance is defined as:

$$S^2 = \frac{1}{n - 1} \sum_{i=1}^{n} (X_i - \bar{X})^2$$

A fundamental theorem in statistics states that:

$$\frac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1}$$

This means that the scaled sample variance follows a Chi-square distribution with $\nu = n-1$ degrees of freedom. Furthermore, $\bar{X}$ and $S^2$ are independent random variables when sampling from a normal population.

---

## 2. The Chi-Square ($\chi^2$) Distribution

The Chi-square distribution with $\nu$ degrees of freedom is the distribution of the sum of squares of $\nu$ independent standard normal variables:

$$\chi^2_\nu = \sum_{i=1}^{\nu} Z_i^2, \quad \text{where } Z_i \sim N(0, 1) \text{ i.i.d.}$$

### Properties
*   **Domain:** $x \ge 0$
*   **Mean:** $E[\chi^2_\nu] = \nu$
*   **Variance:** $Var(\chi^2_\nu) = 2\nu$
*   **Additivity:** If $U \sim \chi^2_{\nu_1}$ and $V \sim \chi^2_{\nu_2}$ are independent, then:
    $$U + V \sim \chi^2_{\nu_1 + \nu_2}$$

---

## 3. Student's t-Distribution

The t-distribution arises when estimating the mean of a normally distributed population when the sample size is small ($n < 30$) and the population standard deviation $\sigma$ is unknown.

### Definition
If $Z \sim N(0, 1)$ and $W \sim \chi^2_\nu$ are independent, then the random variable:

$$T = \frac{Z}{\sqrt{W / \nu}} \sim t_\nu$$

follows Student's t-distribution with $\nu$ degrees of freedom.

### Properties
*   Symmetric and bell-shaped around 0 (like the standard normal, but with heavier tails).
*   As $\nu \to \infty$, the t-distribution converges to the standard normal distribution $N(0, 1)$.

---

## 4. Fisher-Snedecor F-Distribution

The F-distribution is used to compare the variances of two independent normal populations (e.g., in ANOVA or two-sample variance tests).

### Definition
If $U \sim \chi^2_{d_1}$ and $V \sim \chi^2_{d_2}$ are independent, then the ratio of their scaled variables:

$$F = \frac{U / d_1}{V / d_2} \sim F_{d_1, d_2}$$

follows the F-distribution with $d_1$ (numerator) and $d_2$ (denominator) degrees of freedom.

### Properties
*   **Domain:** $x > 0$
*   **Reciprocal Property:** If $F \sim F_{d_1, d_2}$, then:
    $$\frac{1}{F} \sim F_{d_2, d_1}$$

---

## 5. Solved Exercises (9 Examples)

### Exercise 1: Probability of Sample Variance
**Problem:** A random sample of size $n = 10$ is taken from a normal population with variance $\sigma^2 = 4$. Find the probability that the sample variance $S^2$ is less than 5.25. (Use the Chi-square table values: $P(\chi^2_9 \le 11.81) = 0.77$, $P(\chi^2_9 \le 16.92) = 0.95$).

**Solution:**
- **Step 1: Set up the Chi-square transformation.**
  We know that $\frac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1}$.
  Substitute $n = 10$ and $\sigma^2 = 4$:
  $$\frac{9 S^2}{4} \sim \chi^2_9$$
- **Step 2: WIP State.**
  We want to find $P(S^2 < 5.25)$:
  $$P(S^2 < 5.25) = P\left(\frac{9 S^2}{4} < \frac{9 \cdot 5.25}{4}\right) = P\left(\chi^2_9 < \frac{47.25}{4}\right)$$
  Compute the fraction:
  $$\frac{47.25}{4} = ?$$
- **Step 3: Final Calculation.**
  - $\frac{47.25}{4} = 11.8125 \approx 11.81$.
  - $P(S^2 < 5.25) \approx P(\chi^2_9 < 11.81) = 0.77$.

---

### Exercise 2: Expected Value and Variance of Sample Variance
**Problem:** A sample of size $n = 25$ is drawn from a normal population with variance $\sigma^2 = 8$. Find the mean and variance of the sample variance $S^2$.

**Solution:**
- **Step 1: Express $S^2$ in terms of a Chi-square variable.**
  Let $Y = \frac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1}$.
  So, $S^2 = \frac{\sigma^2}{n-1} Y$.
- **Step 2: WIP State.**
  Compute the mean:
  $$E[S^2] = E\left[ \frac{\sigma^2}{n-1} Y \right] = \frac{\sigma^2}{n-1} E[Y]$$
  Since $Y \sim \chi^2_{n-1}$, $E[Y] = n-1 = 24$.
  $$E[S^2] = \frac{8}{24} \cdot 24 = 8$$
  Compute the variance:
  $$Var(S^2) = Var\left( \frac{\sigma^2}{n-1} Y \right) = \left( \frac{\sigma^2}{n-1} \right)^2 Var(Y)$$
  Since $Y \sim \chi^2_{n-1}$, $Var(Y) = 2(n-1) = 48$.
  $$Var(S^2) = \left(\frac{8}{24}\right)^2 \cdot 48 = \left(\frac{1}{3}\right)^2 \cdot 48 = \frac{48}{?}$$
- **Step 3: Final Calculation.**
  - Denominator $= 9$.
  - $Var(S^2) = \frac{48}{9} = \frac{16}{3} \approx 5.3333$.
  *(Important check: Notice that $E[S^2] = \sigma^2$, which proves that the sample variance is an unbiased estimator of the population variance!).*

---

### Exercise 3: Sum of Independent Chi-Squares
**Problem:** Let $U \sim \chi^2_{10}$ and $V \sim \chi^2_{15}$ be independent. What is the distribution of $W = U + V$? Find $E[W]$ and $Var(W)$.

**Solution:**
- **Step 1: Identify the distribution of the sum.**
  By the additivity property of independent Chi-square variables:
  $$W = U + V \sim \chi^2_{10 + 15} \implies W \sim \chi^2_{25}$$
- **Step 2: WIP State.**
  For a Chi-square variable with $\nu = 25$ degrees of freedom:
  - $E[W] = \nu = 25$.
  - $Var(W) = 2\nu = 2 \cdot ?$.
- **Step 3: Final Calculation.**
  - $Var(W) = 50$.

---

### Exercise 4: Constructing a t-Statistic (Gotcha Moment)
**Problem:** Let $Z \sim N(0, 1)$ and $U \sim \chi^2_9$ be independent. Does $T = \frac{Z}{\sqrt{U}}$ follow a t-distribution? If not, modify it so it does.

**Solution:**
- **Step 1: Match the t-distribution definition.**
  The definition of a t-variable is:
  $$T = \frac{Z}{\sqrt{W / \nu}}$$
- **Step 2: WIP State.**
  Looking at $T = \frac{Z}{\sqrt{U}}$, the Chi-square variable $U$ (which has $\nu = 9$) is not divided by its degrees of freedom.
  Therefore, $T$ does **not** follow a t-distribution.
- **Step 3: Final Calculation.**
  To correct it, we must divide $U$ by 9 under the square root:
  $$T_{correct} = \frac{Z}{\sqrt{U / 9}} \sim t_9.$$

---

### Exercise 5: F-Distribution Bounds Transformation
**Problem:** Let $F \sim F_{5, 8}$. Find the value of $c$ such that $P(F > c) = 0.05$, given that for a variable $Y \sim F_{8, 5}$, we have $P(Y \le 4.82) = 0.95$.

**Solution:**
- **Step 1: Use the reciprocal property of the F-distribution.**
  If $F \sim F_{5, 8}$, then $\frac{1}{F} \sim F_{8, 5}$.
- **Step 2: WIP State.**
  We write the probability statement:
  $$P(F > c) = 0.05 \implies P\left(\frac{1}{F} < \frac{1}{c}\right) = 0.05$$
  Since $\frac{1}{F} \sim F_{8, 5}$, this is equivalent to:
  $$P\left(Y < \frac{1}{c}\right) = 0.05 \implies P\left(Y \ge \frac{1}{c}\right) = 0.95$$
  Wait, the problem states $P(Y \le 4.82) = 0.95 \implies P(Y > 4.82) = 0.05$.
  Let's reformulate:
  $$P(F > c) = 0.05 \implies P\left(\frac{1}{F} < \frac{1}{c}\right) = 0.05$$
  This means the left-tail probability of $Y = 1/F$ is 0.05.
  We know that for $Y \sim F_{8, 5}$, $P(Y > 4.82) = 0.05 \implies P(Y \le 4.82) = 0.95$.
  By reciprocal properties of critical values:
  $$c = F_{0.05}(5, 8) = \frac{1}{F_{0.95}(8, 5)} = \frac{1}{?}$$
- **Step 3: Final Calculation.**
  - $F_{0.95}(8, 5) = 4.82$.
  - $c = \frac{1}{4.82} \approx 0.2075$.

---

### Exercise 6: Normal Approximation of Chi-Square
**Problem:** For a Chi-square variable $X \sim \chi^2_{100}$, use the Central Limit Theorem to approximate $P(X \le 120)$. (Recall $\Phi(2) = 0.9772$).

**Solution:**
- **Step 1: Find the mean and variance of $X$.**
  - $\mu = \nu = 100$
  - $\sigma^2 = 2\nu = 200 \implies \sigma = \sqrt{200} \approx 14.14$.
- **Step 2: WIP State.**
  Standardize the variable:
  $$P(X \le 120) = P\left(\frac{X - 100}{14.14} \le \frac{120 - 100}{14.14}\right) \approx P\left(Z \le \frac{20}{14.14}\right)$$
  Compute the fraction:
  $$\frac{20}{14.14} = ?$$
- **Step 3: Final Calculation.**
  - $\frac{20}{14.14} \approx 1.414$ (which is exactly $\sqrt{2}$).
  - $P(Z \le 1.41) = \Phi(1.41) \approx 0.9207$.

---

### Exercise 7: Mean of F-Distribution
**Problem:** Calculate the expected value of $F \sim F_{d_1, d_2}$ where $d_2 > 2$. Use the fact that if $V \sim \chi^2_{d_2}$, then $E\left[\frac{1}{V}\right] = \frac{1}{d_2 - 2}$.

**Solution:**
- **Step 1: Write $F$ in terms of $U$ and $V$.**
  $$F = \frac{U / d_1}{V / d_2} = \frac{d_2}{d_1} \cdot U \cdot \frac{1}{V}$$
- **Step 2: WIP State.**
  Since $U \sim \chi^2_{d_1}$ and $V \sim \chi^2_{d_2}$ are independent:
  $$E[F] = \frac{d_2}{d_1} \cdot E[U] \cdot E\left[\frac{1}{V}\right]$$
  We know $E[U] = d_1$ and $E\left[\frac{1}{V}\right] = \frac{1}{d_2 - 2}$.
  $$E[F] = \frac{d_2}{d_1} \cdot d_1 \cdot \frac{1}{?}$$
- **Step 3: Final Calculation.**
  - Denominator $= d_2 - 2$.
  - $E[F] = \frac{d_2}{d_2 - 2}$.
  *(Note: The mean of an F-distribution depends solely on the denominator degrees of freedom $d_2$!).*

---

### Exercise 8: Sample Variance Ratio (ANOVA Precursor)
**Problem:** We draw a sample of size $n_1 = 6$ from population 1 ($N(\mu_1, \sigma^2)$) and a sample of size $n_2 = 11$ from population 2 ($N(\mu_2, \sigma^2)$). Find the distribution of the ratio of their sample variances, $\frac{S_1^2}{S_2^2}$.

**Solution:**
- **Step 2: WIP State.**
  We know that:
  - $U = \frac{(n_1 - 1)S_1^2}{\sigma^2} \sim \chi^2_{n_1 - 1} \implies U \sim \chi^2_5$
  - $V = \frac{(n_2 - 1)S_2^2}{\sigma^2} \sim \chi^2_{n_2 - 1} \implies V \sim \chi^2_{10}$
  By the definition of the F-distribution:
  $$\frac{U / 5}{V / 10} \sim F_{5, 10}$$
  Substitute the expressions for $U$ and $V$:
  $$\frac{\frac{(n_1 - 1)S_1^2}{\sigma^2} \cdot \frac{1}{n_1 - 1}}{\frac{(n_2 - 1)S_2^2}{\sigma^2} \cdot \frac{1}{n_2 - 1}} = \frac{\frac{S_1^2}{\sigma^2}}{\frac{S_2^2}{\sigma^2}} = ?$$
- **Step 3: Final Calculation.**
  - The ratio simplifies to $\frac{S_1^2}{S_2^2}$.
  - Thus, $\frac{S_1^2}{S_2^2} \sim F_{5, 10}$.

---

### Exercise 9: Probability Bounds for t-Distribution
**Problem:** Let $T \sim t_{15}$. If $P(T > 2.131) = 0.025$, find $P(-2.131 < T < 2.131)$.

**Solution:**
- **Step 1: Use symmetry of the t-distribution.**
  Since the t-distribution is symmetric about 0:
  $$P(T < -2.131) = P(T > 2.131) = 0.025$$
- **Step 2: WIP State.**
  The total area under the PDF is 1. The two tails combined contain:
  $$P(T \le -2.131) + P(T \ge 2.131) = 0.025 + 0.025 = 0.05$$
  The area in the middle is the complement:
  $$P(-2.131 < T < 2.131) = 1 - 0.05 = ?$$
- **Step 3: Final Calculation.**
  $$P(-2.131 < T < 2.131) = 0.95.$$


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
