# Phase 7: R Programming Commands - Descriptive Stats

## 1. Theoretical Foundation

R provides a powerful and streamlined suite of functions to calculate descriptive statistics directly from data vectors. Understanding how to use these base R functions is critical for quickly analyzing datasets without manual calculation.

### 1.1 Central Tendency and Dispersion

Given a numeric vector `x`, you can calculate its fundamental descriptive statistics using the following built-in functions:

*   **Mean:** Calculates the arithmetic average ($\bar{X}$).
    `mean(x)`
*   **Median:** Finds the middle value when the data is ordered.
    `median(x)`
*   **Variance:** Calculates the **sample** variance ($s^2$).
    `var(x)`
*   **Standard Deviation:** Calculates the **sample** standard deviation ($s$).
    `sd(x)`

### 1.2 Quantiles and Percentiles

To find specific percentiles or quartiles, R uses the `quantile()` function. It takes the data vector and a vector of probabilities `probs` indicating the desired percentiles.

*   **Syntax:** `quantile(x, probs = c(...))`
*   **Example for Quartiles:** To find $Q_1, Q_2$ (Median), and $Q_3$, use `probs = c(0.25, 0.5, 0.75)`.

### 1.3 Mode in R

Unlike the mean and median, R does **not** have a built-in function to find the mode (the most frequently occurring value). A common implementation requires combining the `table()` function (which creates a frequency count) and the `max()` function.

*   **Implementation pattern:**
    ```R
    get_mode <- function(v) {
      uniqv <- unique(v)
      uniqv[which.max(tabulate(match(v, uniqv)))]
    }
    ```
    Alternatively, for a quick console check:
    ```R
    freq_table <- table(x)
    names(freq_table)[freq_table == max(freq_table)]
    ```

---

## 2. Step-by-Step Examples

### Example 1: Basic Mean and Median
Calculate the mean and median for the dataset: 12, 15, 18, 20, 22, 25.

**Step 1: Create the vector in R**
```R
data_vec <- c(12, 15, 18, 20, 22, 25)
```

**Step 2: Calculate Mean**
```R
avg_val <- mean(data_vec)
# Result: 18.66667
```

**Step 3: Calculate Median**
```R
med_val <- median(data_vec)
# Result: 19
```

### Example 2: Variance and Standard Deviation
Find the sample variance and standard deviation for: 4, 8, 6, 5, 3, 2, 8, 9, 2, 5.

**Step 1: Create the vector**
```R
x <- c(4, 8, 6, 5, 3, 2, 8, 9, 2, 5)
```

**Step 2: Calculate Variance ($s^2$)**
```R
variance_val <- var(x)
# Result: 6.4
```

**Step 3: Calculate Standard Deviation ($s$)**
```R
sd_val <- sd(x)
# Result: 2.529822
```
*(Notice that `sd(x)` is precisely equal to `sqrt(var(x))`)*.

### Example 3: Extracting Specific Quartiles
From a random sample of 100 observations generated from a normal distribution, extract the 25th, 50th, and 75th percentiles.

**Step 1: Generate Data**
```R
set.seed(123)
obs <- rnorm(100, mean = 50, sd = 10)
```

**Step 2: Use quantile function**
```R
target_probs <- c(0.25, 0.5, 0.75)
quartiles <- quantile(obs, probs = target_probs)
print(quartiles)
```
**Output:**
```R
      25%       50%       75% 
45.06014  50.61868  56.55173 
```

### Example 4: Finding the Interquartile Range (IQR)
Using the `quantile()` function, compute the IQR for `x <- c(10, 20, 30, 40, 50, 60, 70, 80, 90)`.

**Step 1: Calculate $Q_1$ and $Q_3$**
```R
x <- c(10, 20, 30, 40, 50, 60, 70, 80, 90)
q_vals <- quantile(x, probs = c(0.25, 0.75))
```

**Step 2: Subtract $Q_1$ from $Q_3$**
```R
iqr_val <- q_vals[2] - q_vals[1]
# Note: R also has a built-in IQR() function that does exactly this: IQR(x)
```

### Example 5: Creating a Mode Function
You are given a categorical numeric vector `votes <- c(1, 2, 2, 3, 1, 2, 4, 5, 2, 1)`. Find the mode.

**Step 1: Create frequency table**
```R
votes <- c(1, 2, 2, 3, 1, 2, 4, 5, 2, 1)
freq <- table(votes)
print(freq)
# votes
# 1 2 3 4 5 
# 3 4 1 1 1 
```

**Step 2: Extract the mode**
```R
# Find the maximum frequency
max_freq <- max(freq)

# Identify the name (the actual value) that corresponds to max frequency
mode_val <- names(freq)[freq == max_freq]
print(mode_val) 
# Result: "2"
```

### Example 6: Coefficient of Variation (CV)
Calculate the Coefficient of Variation ($CV = \frac{SD}{Mean}$) for a given sample `y <- c(100, 110, 95, 105, 120, 90)`.

**Step 1: Assign variable**
```R
y <- c(100, 110, 95, 105, 120, 90)
```

**Step 2: Calculate Mean and SD**
```R
m_y <- mean(y)
sd_y <- sd(y)
```

**Step 3: Compute CV**
```R
cv_y <- sd_y / m_y
# Result: 0.1045261 (or roughly 10.45%)
```

---

### Example 7: The "NA" Trap (Gotcha Moment)
You receive a dataset of student test scores, but one student was absent, resulting in an `NA` (Not Available) value in the data vector: `scores <- c(85, 90, 78, NA, 92, 88)`. Calculate the mean.

#### Gotcha Section Analysis
A very common trap in R is forgetting how statistical functions handle missing values. By default, if there is even a single `NA` in a vector, functions like `mean()`, `median()`, `sd()`, and `var()` will return `NA` for the entire dataset, because mathematically, the average of a known set plus an unknown value is unknown.

**Step 1: The Incorrect Approach**
```R
scores <- c(85, 90, 78, NA, 92, 88)
mean(scores)
# Result: NA
```

**Step 2: The Correct Approach (Using na.rm)**
You must explicitly tell R to remove the `NA` values before performing the calculation by using the `na.rm = TRUE` argument.
```R
mean(scores, na.rm = TRUE)
# Result: 86.6
```
*(Always check your datasets for NAs or preemptively use `na.rm = TRUE` during exploratory analysis!)*

---

### Example 8: Population vs. Sample Variance Trap (Gotcha Moment)
A problem explicitly asks you to calculate the **population** variance ($\sigma^2$) for the dataset `population_ages <- c(25, 30, 35, 40, 45)`. You use the `var()` function.

#### Gotcha Section Analysis
The R `var()` and `sd()` functions are strictly designed for **sample** statistics. They divide the sum of squared differences by $n - 1$ (degrees of freedom). If you are working with an entire population, dividing by $n - 1$ is statistically incorrect; you must divide by $n$. R does not have a built-in `pop.var()` function.

**Step 1: The Incorrect Approach (Sample Variance)**
```R
pop_ages <- c(25, 30, 35, 40, 45)
var(pop_ages)
# R computes: sum((x - mean)^2) / 4
# Result: 62.5
```

**Step 2: The Correct Approach (Manual Adjustment)**
To get the population variance, you must either calculate it manually, or multiply the sample variance by $\frac{n-1}{n}$.

*Manual Calculation:*
```R
n <- length(pop_ages)
mu <- mean(pop_ages)
pop_var_manual <- sum((pop_ages - mu)^2) / n
# Result: 50
```

*Adjustment Method:*
```R
n <- length(pop_ages)
pop_var_adjusted <- var(pop_ages) * ((n - 1) / n)
# Result: 62.5 * (4 / 5) = 50
```
*(Whenever a question specifies "Population Variance" or "Population Standard Deviation", never use `var()` or `sd()` directly without making this adjustment!)*


# Phase 7: R Programming Commands - Binomial Distribution

## 1. Theoretical Foundation

The binomial distribution measures the number of successes in a sequence of $n$ independent experiments (trials), each asking a yes-no question, with a fixed probability of success $p$.

R handles distributions systematically using a consistent prefix notation. For the Binomial distribution, the root is `binom`.
*   **`d` prefix (Density/Mass):** Returns the exact probability $P(X = k)$.
*   **`p` prefix (Probability/Cumulative):** Returns the cumulative probability $P(X \le k)$.
*   **`q` prefix (Quantile):** The inverse of `pbinom`. Returns the value $k$ for a given cumulative probability.
*   **`r` prefix (Random):** Generates random observations from the distribution.

### 1.1 Exact Probabilities: `dbinom()`
Calculates the Probability Mass Function (PMF), $P(X = k)$.
*   **Syntax:** `dbinom(x = k, size = n, prob = p)`
*   **Arguments:**
    *   `x`: The target number of successes ($k$). Can also be a vector (e.g., `0:5`).
    *   `size`: The total number of trials ($n$).
    *   `prob`: The probability of success on each trial ($p$).

### 1.2 Cumulative Probabilities: `pbinom()`
Calculates the Cumulative Distribution Function (CDF), $P(X \le k)$.
*   **Syntax:** `pbinom(q = k, size = n, prob = p, lower.tail = TRUE)`
*   **Arguments:**
    *   `q`: The quantile or upper bound of successes ($k$).
    *   `lower.tail`: If `TRUE` (default), calculates $P(X \le k)$. If `FALSE`, calculates $P(X > k)$.

---

## 2. Step-by-Step Examples

### Example 1: Exact Probability ($P(X = k)$)
A biased coin has a 60% chance of landing on Heads. If you flip it 10 times, what is the exact probability of getting exactly 7 Heads?

**Step 1: Identify Parameters**
*   $k = 7$ (Target successes)
*   $n = 10$ (Total trials)
*   $p = 0.60$ (Probability of success)

**Step 2: Use `dbinom`**
```R
ans <- dbinom(x = 7, size = 10, prob = 0.6)
# Result: 0.2149908
```

### Example 2: Cumulative Probability ($P(X \le k)$)
Using the same coin ($n=10, p=0.6$), what is the probability of getting 4 or fewer Heads?

**Step 1: Identify Parameters**
We want $P(X \le 4)$.

**Step 2: Use `pbinom`**
```R
ans <- pbinom(q = 4, size = 10, prob = 0.6)
# Result: 0.1662386
```

### Example 3: Probability of a Range ($P(a \le X \le b)$)
A pharmaceutical drug has an 80% success rate. If given to 20 patients, what is the probability that between 12 and 16 patients (inclusive) recover?

**Step 1: Formulate the Math**
We want $P(12 \le X \le 16)$.
Mathematically, this is $P(X \le 16) - P(X \le 11)$. *(Notice we subtract $P(X \le 11)$, not 12, so we don't accidentally remove 12 from the interval).*

**Step 2: Use `pbinom` difference**
```R
upper_bound <- pbinom(16, size = 20, prob = 0.8)
lower_bound <- pbinom(11, size = 20, prob = 0.8)
ans <- upper_bound - lower_bound
# Result: 0.5785692
```

### Example 4: Range Probability (Alternative method)
Solve Example 3 using `dbinom` and `sum`.

**Step 1: Generate a vector of target successes**
We want exactly 12, 13, 14, 15, and 16 successes.
```R
targets <- 12:16
```

**Step 2: Calculate all exact probabilities and sum them**
```R
probs <- dbinom(targets, size = 20, prob = 0.8)
ans <- sum(probs)
# Result: 0.5785692
```
*(This is often easier to read and less prone to the "off-by-one" error seen in cumulative subtraction).*

### Example 5: Generating Random Binomial Variables
Simulate flipping a fair coin 5 times, and record the number of heads. Repeat this experiment 100 times.

**Step 1: Use `rbinom`**
*   `n = 100` (Number of experiments)
*   `size = 5` (Trials per experiment)
*   `prob = 0.5`
```R
simulations <- rbinom(n = 100, size = 5, prob = 0.5)
```
*(This will output a vector of 100 numbers, where each number is between 0 and 5, representing the number of heads in that specific experiment).*

---

### Example 6: Finding the Minimum Threshold with `qbinom()`
A quality control manager uses $X \sim B(20, 0.15)$ to model the number of defective units in a batch. What is the smallest number $k$ such that the cumulative probability $P(X \leq k) \geq 0.90$? In other words, what is the 90th percentile of the distribution?

**Step 1: Identify Parameters**
*   $n = 20$, $p = 0.15$, target cumulative probability $= 0.90$.

**Step 2: Use `qbinom`**
`qbinom()` is the inverse of `pbinom`. Given a cumulative probability, it returns the smallest integer $k$ satisfying $P(X \leq k) \geq p$.
```R
threshold <- qbinom(p = 0.90, size = 20, prob = 0.15)
# Result: 5
```

**Step 3: Verify the result**
```R
pbinom(4, size = 20, prob = 0.15)  # P(X <= 4)
# Result: 0.8298 (less than 0.90, so k=4 is insufficient)
pbinom(5, size = 20, prob = 0.15)  # P(X <= 5)
# Result: 0.9327 (>= 0.90, so k=5 is the answer)
```
The manager can be 90% confident that no more than **5** units in a batch of 20 will be defective.

---

### Example 7: The "Strictly Less Than" Trap (Gotcha Moment)
A multiple-choice test has 50 questions, each with 4 options (meaning the chance of guessing correctly is 25%). What is the probability of a student guessing *strictly less than* 15 questions correctly? 

#### Gotcha Section Analysis
Students often see "less than 15" and instinctively type `pbinom(15, size=50, prob=0.25)`. However, `pbinom(q)` calculates $P(X \le q)$, meaning it includes 15! Because the binomial distribution is discrete, "strictly less than 15" ($X < 15$) is mathematically equivalent to "less than or equal to 14" ($X \le 14$).

**Step 1: The Incorrect Approach**
```R
wrong_ans <- pbinom(15, size = 50, prob = 0.25)
# This calculates P(X <= 15)
```

**Step 2: The Correct Approach**
Adjust the quantile down by 1.
```R
correct_ans <- pbinom(14, size = 50, prob = 0.25)
# This calculates P(X <= 14), which is P(X < 15).
```

---

### Example 8: The "Greater Than" and `lower.tail` Trap (Gotcha Moment)
A factory produces light bulbs with a 5% defect rate. In a batch of 200 bulbs, what is the probability of finding *at least* 15 defective bulbs?

#### Gotcha Section Analysis
"At least 15" means $P(X \ge 15)$. 
There are two common traps here:
1. **Using Complement Rule Incorrectly:** If you do `1 - pbinom(15, ...)`, you are calculating $1 - P(X \le 15) = P(X > 15) = P(X \ge 16)$. You accidentally excluded 15 from your final answer!
2. **Using `lower.tail = FALSE` Incorrectly:** In R, `lower.tail = FALSE` strictly calculates $P(X > q)$. It does NOT calculate $P(X \ge q)$. 

**Step 1: Formulate the correct Complement**
$P(X \ge 15) = 1 - P(X \le 14)$.
```R
ans_complement <- 1 - pbinom(14, size = 200, prob = 0.05)
```

**Step 2: The `lower.tail` Method**
If you want to use the built-in R feature to avoid subtracting from 1, you must pass 14 as the quantile, because `lower.tail = FALSE` computes $P(X > q)$. So, $P(X > 14)$ is equivalent to $P(X \ge 15)$.
```R
ans_lower_tail <- pbinom(14, size = 200, prob = 0.05, lower.tail = FALSE)
```
*(Both `ans_complement` and `ans_lower_tail` will yield the correct result. Never pass 15 into `pbinom` for an "at least 15" question!)*


# Phase 7: R Programming Commands - Normal Distribution

## 1. Theoretical Foundation

The Normal (Gaussian) distribution is continuous and completely defined by its mean ($\mu$) and standard deviation ($\sigma$). R provides a similar family of functions for the normal distribution as it does for the binomial, using the root `norm`.

Unlike the discrete binomial distribution, the probability of an exact, specific value in a continuous normal distribution is strictly zero ($P(X = x) = 0$). Therefore, we are almost exclusively concerned with cumulative probabilities (ranges) or inverse probabilities.

### 1.1 Cumulative Probabilities: `pnorm()`
Calculates the area under the normal curve up to a given value, $P(X \le x)$.
*   **Syntax:** `pnorm(q = x, mean = \mu, sd = \sigma, lower.tail = TRUE)`
*   **Arguments:**
    *   `q`: The value you are checking ($x$).
    *   `mean`: The population mean ($\mu$). Default is 0.
    *   `sd`: The population standard deviation ($\sigma$). Default is 1.

*(Note: Because the distribution is continuous, $P(X \le x)$ is exactly equal to $P(X < x)$. You do not need to adjust the boundaries like you do in the binomial distribution).*

### 1.2 Inverse Probabilities (Quantiles): `qnorm()`
Finds the value $x$ corresponding to a specific cumulative probability $p$. This answers the question: "What value separates the bottom $p\%$ of the data from the rest?"
*   **Syntax:** `qnorm(p = prob, mean = \mu, sd = \sigma)`

### 1.3 Other Normal Functions
*   **`rnorm(n, mean, sd)`:** Generates $n$ random numbers from the specified normal distribution.
*   **`dnorm(x, mean, sd)`:** Returns the height of the probability density function (PDF) curve at $x$. This does **not** give a probability; it is mostly used for drawing the bell curve.

---

## 2. Step-by-Step Examples

### Example 1: Basic Cumulative Probability ($P(X < x)$)
Human heights are normally distributed with $\mu = 170$ cm and $\sigma = 10$ cm. What is the probability that a randomly selected person is shorter than 185 cm?

**Step 1: Identify Parameters**
*   $q = 185$
*   $\mu = 170$
*   $\sigma = 10$

**Step 2: Use `pnorm`**
```R
ans <- pnorm(q = 185, mean = 170, sd = 10)
# Result: 0.9331928
```

### Example 2: Right-Tail Probability ($P(X > x)$)
Using the same height distribution ($\mu = 170, \sigma = 10$), what is the probability a person is taller than 190 cm?

**Step 1: Formulate the Problem**
We want $P(X > 190)$.

**Step 2: Calculate in R**
You can use the complement rule or `lower.tail = FALSE`.
```R
# Method 1 (Complement)
ans_comp <- 1 - pnorm(190, mean = 170, sd = 10)

# Method 2 (lower.tail)
ans_tail <- pnorm(190, mean = 170, sd = 10, lower.tail = FALSE)
# Result: 0.02275013
```

### Example 3: Probability Between Two Values ($P(a < X < b)$)
What is the probability a person's height is between 160 cm and 180 cm?

**Step 1: Formulate the Math**
$P(160 < X < 180) = P(X < 180) - P(X < 160)$.

**Step 2: Use `pnorm` subtraction**
```R
ans <- pnorm(180, mean = 170, sd = 10) - pnorm(160, mean = 170, sd = 10)
# Result: 0.6826895
```
*(Notice this matches the empirical rule: approximately 68% of data falls within 1 standard deviation of the mean).*

### Example 4: Using the Standard Normal Distribution (Z)
If you have a Z-score of $Z = 1.96$, what is the cumulative probability?

**Step 1: Understand Default Parameters**
For the standard normal distribution, $\mu = 0$ and $\sigma = 1$. R uses these as defaults, so you don't need to explicitly declare them.

**Step 2: Use `pnorm`**
```R
ans <- pnorm(1.96)
# Result: 0.9750021
```

### Example 5: Finding a Percentile with `qnorm()`
Scores on a test are normally distributed with $\mu = 500$ and $\sigma = 100$. What score marks the 90th percentile?

**Step 1: Identify Parameters**
*   We want the bottom 90%, so probability $p = 0.90$.

**Step 2: Use `qnorm`**
```R
ans <- qnorm(p = 0.90, mean = 500, sd = 100)
# Result: 628.1552
```

### Example 6: Generating Random Data
Simulate the grades of a classroom of 30 students, where the class average is 75 with a standard deviation of 8.

**Step 1: Use `rnorm`**
```R
grades <- rnorm(n = 30, mean = 75, sd = 8)
```
*(This returns a vector of 30 randomized grades based on the distribution).*

---

### Example 7: The "Variance vs Standard Deviation" Trap (Gotcha Moment)
A problem states: "The weights of boxes are normally distributed, $X \sim N(50, 16)$. Find $P(X < 55)$."

#### Gotcha Section Analysis
The standard mathematical notation for a normal distribution is $X \sim N(\mu, \sigma^2)$, where the second parameter is the **Variance**. However, the R function `pnorm(q, mean, sd)` strictly requires the **Standard Deviation**. A very common mistake is plugging the number 16 directly into the `sd` argument.

**Step 1: The Incorrect Approach**
```R
wrong_ans <- pnorm(55, mean = 50, sd = 16)
# This calculates based on standard deviation = 16.
```

**Step 2: The Correct Approach**
You must extract the standard deviation by taking the square root of the variance given in the problem statement.
$\sigma = \sqrt{16} = 4$.
```R
correct_ans <- pnorm(55, mean = 50, sd = 4)
# Result: 0.8943502
```

---

### Example 8: The "Top X%" Quantile Trap (Gotcha Moment)
A university accepts only the top 5% of applicants based on an entrance exam ($\mu = 100, \sigma = 15$). What is the minimum score required to be accepted?

#### Gotcha Section Analysis
The phrase "top 5%" naturally leads students to type `qnorm(0.05, ...)`. However, `qnorm(p)` expects the cumulative area from the *left* tail. The "top 5%" corresponds to the upper tail. If you put 0.05 into `qnorm`, you will find the score separating the *bottom* 5% (the worst scores!).

**Step 1: The Incorrect Approach**
```R
wrong_score <- qnorm(0.05, mean = 100, sd = 15)
# Result: 75.32 (This is a terrible score!)
```

**Step 2: The Correct Approach (Using Complement Probability)**
If you are in the top 5%, you scored higher than 95% of people. Therefore, the area to the left is 0.95.
```R
correct_score_1 <- qnorm(0.95, mean = 100, sd = 15)
# Result: 124.6728
```

**Step 3: The Alternative Correct Approach (Using lower.tail)**
You can use the `lower.tail = FALSE` argument to tell `qnorm` you are providing the upper area.
```R
correct_score_2 <- qnorm(0.05, mean = 100, sd = 15, lower.tail = FALSE)
# Result: 124.6728
```
*(Always draw a quick sketch of the bell curve to visually verify if the answer makes logical sense!)*


# Phase 7.4: R Programming Commands - Additional Distributions and Statistical Functions

This file provides the R syntax, parameters, and exam gotchas for the remaining discrete and continuous probability distributions (Geometric, Hypergeometric, Exponential, Uniform, Gamma, Chi-Square, Student's t, and Fisher's F).

---

## 1. Geometric Distribution (`*geom`)

R functions: `dgeom()`, `pgeom()`, `qgeom()`, `rgeom()`.

> **CRITICAL EXAM GOTCHA:** R's geometric functions strictly model **Definition B** (the number of failures *before* the first success). 
> If a problem asks for the probability that the first success is on the 4th trial, this means there were exactly 3 failures. In R, you must use `x = 3`, not `4`!
> *   $P(X = 4 \text{ trials}) = \text{`dgeom(3, prob)`}$
> *   $P(X \le 4 \text{ trials}) = P(\text{failures} \le 3) = \text{`pgeom(3, prob)`}$

---

## 2. Hypergeometric Distribution (`*hyper`)

R functions: `dhyper()`, `phyper()`, `qhyper()`, `rhyper()`.

> **CRITICAL EXAM GOTCHA:** R's naming convention for hypergeometric parameters is completely different from standard textbook notation ($N, K, n$).
> *   R syntax: `dhyper(x, m, n, k)`
> *   Parameter Mapping:
>     *   `x`: Number of successes in the sample ($k$).
>     *   `m`: Number of success items in the population ($K$).
>     *   `n`: Number of **failure** items in the population ($N - K$). *(Do not pass the total population $N$ here!)*
>     *   `k`: The sample size ($n$).

---

## 3. Other Continuous Distributions (`*exp`, `*unif`, `*gamma`)

### 3.1 Exponential: `dexp(x, rate)`, `pexp(q, rate)`
*   `rate` is $\lambda$ (where mean $= 1/\lambda$).

### 3.2 Uniform: `dunif(x, min, max)`, `punif(q, min, max)`
*   `min` and `max` are the lower ($a$) and upper ($b$) boundaries.

### 3.3 Gamma: `dgamma(x, shape, rate, scale = 1/rate)`
*   R accepts both the rate parameter $\beta$ (`rate`) and scale parameter $\theta$ (`scale`). 
*   **Safety Tip:** Always explicitly name the parameter in the function call to avoid using the wrong parameterization: e.g., `dgamma(x, shape = 3, rate = 2)`.

---

## 4. Sampling Distributions (`*chisq`, `*t`, `*f`)

These functions are primarily used to find critical values (using `q*`) and p-values (using `p*`) for hypothesis testing.

*   **Chi-Square:** `pchisq(q, df)`, `qchisq(p, df)`
*   **Student's t:** `pt(q, df)`, `qt(p, df)`
*   **Fisher's F:** `pf(q, df1, df2)`, `qf(p, df1, df2)`

---

## 5. Solved Exercises (9 Examples)

### Example 1: Geometric Probability (Trials vs. Failures)
**Problem:** A machine produces defective parts with probability $p = 0.08$. Write the R command to calculate the probability that the first defective part is found on the 5th test.

**Solution:**
- **Step 1: Translate trials to failures.**
  Finding the first success on the 5th test means the first 4 tests were failures.
- **Step 2: WIP State.**
  We want 4 failures before the first success.
  R function call:
  `dgeom(x = 4, prob = ?)`
- **Step 3: Final Calculation.**
  `dgeom(x = 4, prob = 0.08)`
  *(Result: 0.0573)*

---

### Example 2: Hypergeometric Probability Mapping
**Problem:** A deck of 52 cards contains 4 Aces. If we draw 5 cards without replacement, write the R command to find the probability of getting exactly 2 Aces.

**Solution:**
- **Step 1: Map standard parameters to R parameters.**
  - Successes in sample $x = 2$
  - Successes in population $m = 4$
  - Failures in population $n = 52 - 4 = 48$ *(not 52!)*
  - Sample size $k = 5$
- **Step 2: WIP State.**
  `dhyper(x = 2, m = 4, n = 48, k = ?)`
- **Step 3: Final Calculation.**
  `dhyper(x = 2, m = 4, n = 48, k = 5)`
  *(Result: 0.0399)*

---

### Example 3: Uniform Distribution Wait Time
**Problem:** A bus arrives randomly between 10:00 and 10:30. Write the R command to find the probability that a passenger waiting since 10:00 waits more than 20 minutes.

**Solution:**
- **Step 1: Identify bounds.**
  Let time $X \sim U(0, 30)$. We want $P(X > 20) = 1 - P(X \le 20)$.
- **Step 2: WIP State.**
  Using `punif`:
  `1 - punif(q = 20, min = 0, max = 30)`
  Alternatively, using `lower.tail = FALSE`:
  `punif(q = 20, min = 0, max = 30, lower.tail = ?)`
- **Step 3: Final Calculation.**
  `punif(q = 20, min = 0, max = 30, lower.tail = FALSE)`
  *(Result: 0.3333)*

---

### Example 4: Exponential Wait Time
**Problem:** The lifetime of a light bulb is exponentially distributed with a mean of 1000 hours. Write the R command to find the probability that a bulb lasts less than 800 hours.

**Solution:**
- **Step 1: Calculate rate parameter.**
  Mean $= 1000 \implies \lambda = 1/1000 = 0.001$.
- **Step 2: WIP State.**
  We want $P(X < 800)$.
  `pexp(q = 800, rate = ?)`
- **Step 3: Final Calculation.**
  `pexp(q = 800, rate = 0.001)`
  *(Result: 0.5507)*

---

### Example 5: Gamma Wait Time
**Problem:** A service center receives calls where the wait time between calls is exponentially distributed with a mean of 2 minutes. Write the R command to find the probability that it takes more than 15 minutes to receive 5 calls.

**Solution:**
- **Step 1: Map to Gamma parameters.**
  The sum of 5 independent $Exp(0.5)$ variables follows $Gamma(\alpha = 5, \beta = 0.5)$.
  - `shape` $= 5$
  - `rate` $= 1/2 = 0.5$
- **Step 2: WIP State.**
  We want $P(X > 15)$, so we use `lower.tail = FALSE`:
  `pgamma(q = 15, shape = 5, rate = 0.5, lower.tail = ?)`
- **Step 3: Final Calculation.**
  `pgamma(q = 15, shape = 5, rate = 0.5, lower.tail = FALSE)`
  *(Result: 0.1334)*

---

### Example 6: Finding Chi-Square Critical Values
**Problem:** Find the critical value $\chi^2_{\alpha}$ such that the area in the right tail is $0.05$ for a Chi-square distribution with 14 degrees of freedom.

**Solution:**
- **Step 1: Identify quantile function and area.**
  An upper-tail area of $0.05$ means the cumulative area from the left is $0.95$.
- **Step 2: WIP State.**
  `qchisq(p = 0.95, df = 14)`
  Or, using the upper tail:
  `qchisq(p = 0.05, df = 14, lower.tail = ?)`
- **Step 3: Final Calculation.**
  `qchisq(p = 0.05, df = 14, lower.tail = FALSE)`
  *(Result: 23.68)*

---

### Example 7: Student's t Hypothesis p-value
**Problem:** A researcher computes a t-statistic of $t = -2.15$ with $df = 18$ for a two-tailed test. Write the R command to calculate the p-value.

**Solution:**
- **Step 1: Recall two-tailed p-value formula.**
  $$\text{p-value} = 2 \cdot P(T \le -|t|)$$
- **Step 2: WIP State.**
  Since $t = -2.15$ is negative, the left tail probability is `pt(-2.15, df = 18)`.
  Multiply this by 2 to get both tails:
  `2 * pt(q = -2.15, df = ?)`
- **Step 3: Final Calculation.**
  `2 * pt(q = -2.15, df = 18)`
  *(Result: 0.0454)*

---

### Example 8: F-Distribution Quantiles for ANOVA
**Problem:** In an ANOVA test, the numerator degrees of freedom is 3 and the denominator degrees of freedom is 20. Find the critical F-value for a significance level of $\alpha = 0.01$.

**Solution:**
- **Step 1: Map parameters.**
  We want the 99th percentile of $F_{3, 20}$.
- **Step 2: WIP State.**
  `qf(p = 0.99, df1 = 3, df2 = 20)`
  Or, using the upper tail:
  `qf(p = 0.01, df1 = 3, df2 = 20, lower.tail = ?)`
- **Step 3: Final Calculation.**
  `qf(p = 0.01, df1 = 3, df2 = 20, lower.tail = FALSE)`
  *(Result: 4.938)*

---

### Example 9: Sample Variance Probability Calculation
**Problem:** For a sample of size $n = 16$ from a normal population with $\sigma^2 = 25$, write the R command to find the probability that the sample variance $S^2$ exceeds 35.

**Solution:**
- **Step 1: Relate $S^2$ to the Chi-square distribution.**
  $$P(S^2 > 35) = P\left(\frac{15 S^2}{25} > \frac{15 \cdot 35}{25}\right) = P\left(\chi^2_{15} > 21\right)$$
- **Step 2: WIP State.**
  Compute the right tail of $\chi^2_{15}$ at 21:
  `pchisq(q = 21, df = 15, lower.tail = ?)`
- **Step 3: Final Calculation.**
  `pchisq(q = 21, df = 15, lower.tail = FALSE)`
  *(Result: 0.1369)*
