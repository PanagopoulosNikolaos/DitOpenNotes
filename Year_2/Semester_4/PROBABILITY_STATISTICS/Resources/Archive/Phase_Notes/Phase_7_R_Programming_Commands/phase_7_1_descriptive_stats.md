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
