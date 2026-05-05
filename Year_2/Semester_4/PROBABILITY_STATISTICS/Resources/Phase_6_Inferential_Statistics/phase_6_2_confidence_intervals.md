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
