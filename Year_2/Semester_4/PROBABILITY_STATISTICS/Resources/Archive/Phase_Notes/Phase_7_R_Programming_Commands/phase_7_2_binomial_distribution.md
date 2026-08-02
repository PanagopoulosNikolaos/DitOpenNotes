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
