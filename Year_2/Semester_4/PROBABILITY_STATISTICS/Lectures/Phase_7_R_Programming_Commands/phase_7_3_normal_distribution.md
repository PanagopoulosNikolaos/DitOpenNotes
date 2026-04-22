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
