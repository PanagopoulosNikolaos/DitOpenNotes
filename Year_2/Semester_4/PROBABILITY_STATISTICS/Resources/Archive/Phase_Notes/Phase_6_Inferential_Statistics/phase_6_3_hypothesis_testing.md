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
