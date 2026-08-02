# Phase 4.1 (Time): Discrete Random Variables -- Fundamentals in Time Context

A **Discrete Random Variable in Time** maps time-based outcomes (such as clock tick counts, discrete delay steps, retry attempt numbers, or time slot indices) to numerical values $t \in \mathbb{R}$.

---

## 1. Theoretical Foundation (Time Context)

### Probability Mass Function (PMF) of Duration
The PMF of a discrete time random variable $T$ is a function $p(t)$ that assigns a probability to each discrete time value $t$:

$$p(t) = P(T = t)$$

#### Validity Conditions
1. **Non-negativity:** $p(t) \ge 0$ for all discrete time values $t$.
2. **Normalization:** $\sum_{\text{all } t} p(t) = 1$.

### Expected Duration $E[T]$
The **Expected Duration** (or mean latency) represents the long-run average time taken per operation:

$$\boxed{E[T] = \mu_T = \sum_{\text{all } t} t \cdot p(t)}$$

#### Linearity of Expectation for Time Transformations
If time $T$ is linearly transformed (e.g., converting units or adding a fixed latency overhead $b$):

$$E[aT + b] = a \cdot E[T] + b$$

### Variance of Duration $V(T)$
The **Variance of Duration** measures the dispersion of processing times around the mean latency:

$$V(T) = E\left[(T - \mu_T)^2\right] = \sum_{\text{all } t} (t - \mu_T)^2 \cdot p(t)$$

#### Computational Shortcut Formula
$$\boxed{V(T) = E[T^2] - (E[T])^2}$$

where $E[T^2] = \sum_{\text{all } t} t^2 \cdot p(t)$. Standard Deviation of Duration: $\sigma_T = SD(T) = \sqrt{V(T)}$.

#### Variance Properties Under Time Unit Changes
When converting units (e.g., multiplying time $T$ by scaling factor $a$) or adding constant setup overhead $b$:

$$\boxed{V(aT + b) = a^2 \cdot V(T)}$$

---

## 2. Time-Specific Gotchas

### Gotcha 1: Unit Scaling Multiplier on Variance ($a^2$)
When converting execution times from seconds to milliseconds ($a = 1000$), the expected time scales by 1000 ($E[1000T] = 1000 E[T]$), but the variance scales by $1000^2 = 1,000,000$ ($V(1000T) = 10^6 V(T)$). Forgetting to square $a$ leads to massive calculation errors!

### Gotcha 2: Constant Overhead $b$ Does Not Affect Spread
Adding a fixed network handshake delay of $b = 50\text{ ms}$ to every transaction increases the expected duration by 50 ms ($E[T + 50] = E[T] + 50$), but has **zero impact on variance**: $V(T + 50) = V(T)$.

### Gotcha 3: Variance of Time Difference Is Additive
For independent processing stages with durations $T_1$ and $T_2$, the variance of the delay difference $T_1 - T_2$ is **additive**:

$$V(T_1 - T_2) = V(T_1) + (-1)^2 V(T_2) = V(T_1) + V(T_2)$$

Variance can **never** be negative, and subtracting durations does not reduce variance.

---

## 3. Solved Exercises (10 Examples)

### Exercise 1: Verifying a Discrete Duration PMF
**Problem:** A task completes in $T \in \{1, 2, 3, 4\}\text{ seconds}$ with probabilities given in the table:

| Duration $t$ (sec) | 1 | 2 | 3 | 4 |
| :--- | :---: | :---: | :---: | :---: |
| $P(T = t)$ | 0.15 | 0.35 | 0.30 | 0.20 |

Verify if this is a valid PMF for duration $T$.

**Solution:**
- **Step 1: Check non-negativity.** All values $\ge 0$. Passed.
- **Step 2: Check normalization.**
  $$\sum p(t) = 0.15 + 0.35 + 0.30 + 0.20 = 1.00$$
- **Conclusion:** It is a valid PMF.

---

### Exercise 2: Finding Missing Probability in Retry Durations
**Problem:** Connection retry counts $T \in \{0, 1, 2, 3\}\text{ seconds}$ have PMF $P(T=t) = c \cdot (t + 1)$. Find $c$ and the completed table.

**Solution:**
- **Step 1: Apply normalization condition.**
  $$\sum p(t) = c(0+1) + c(1+1) + c(2+1) + c(3+1) = 1$$
  $$c(1 + 2 + 3 + 4) = 10c = 1 \implies c = 0.1$$
- **Step 2: WIP State.**
  $p(0) = 0.1$, $p(1) = 0.2$, $p(2) = 0.3$, $p(3) = 0.4$.
  Check sum: $0.1 + 0.2 + 0.3 + 0.4 = ?$
- **Step 3: Final Calculation.**
  Sum = 1.0. Table is complete.

---

### Exercise 3: Computing Expected Processing Duration $E[T]$
**Problem:** Using the PMF from Exercise 2 ($p(t) = [0.1, 0.2, 0.3, 0.4]$ for $t \in \{0, 1, 2, 3\}\text{ seconds}$), find the expected duration $E[T]$.

**Solution:**
- **Step 1: Apply expected value formula.**
  $$E[T] = \sum t \cdot p(t) = (0 \cdot 0.1) + (1 \cdot 0.2) + (2 \cdot 0.3) + (3 \cdot 0.4)$$
- **Step 2: WIP State.**
  $$E[T] = 0 + 0.2 + 0.6 + ?$$
- **Step 3: Final Calculation.**
  $$E[T] = 0 + 0.2 + 0.6 + 1.2 = 2.0\text{ seconds}$$

---

### Exercise 4: Computing Duration Variance $V(T)$
**Problem:** Using the PMF from Exercise 2 ($E[T] = 2.0$), compute $E[T^2]$, $V(T)$, and $SD(T)$.

**Solution:**
- **Step 1: Compute second raw moment $E[T^2]$.**
  $$E[T^2] = (0^2 \cdot 0.1) + (1^2 \cdot 0.2) + (2^2 \cdot 0.3) + (3^2 \cdot 0.4) = 0 + 0.2 + 1.2 + 3.6 = 5.0$$
- **Step 2: WIP State.**
  Apply shortcut formula:
  $$V(T) = E[T^2] - (E[T])^2 = 5.0 - (2.0)^2 = 5.0 - ?$$
- **Step 3: Final Calculation.**
  $$V(T) = 5.0 - 4.0 = 1.0\text{ sec}^2$$
  $$SD(T) = \sqrt{1.0} = 1.0\text{ second}$$

---

### Exercise 5: Unit Scaling and Constant Overhead
**Problem:** A task duration $T$ in seconds has $E[T] = 2.5\text{ s}$ and $V(T) = 1.44\text{ s}^2$. Total response time in milliseconds is defined as $Y = 1000T + 40$ (where 40 ms is fixed network setup delay). Find $E[Y]$ and $V[Y]$.

**Solution:**
- **Step 1: Compute $E[Y]$.**
  $$E[Y] = 1000 \cdot E[T] + 40 = 1000(2.5) + 40 = 2500 + 40 = 2540\text{ ms}$$
- **Step 2: WIP State.**
  Compute $V[Y]$ using scaling property $a^2$:
  $$V[Y] = 1000^2 \cdot V(T) = 1,000,000 \cdot 1.44 = ?$$
- **Step 3: Final Calculation.**
  $$V[Y] = 1,440,000\text{ ms}^2$$
  $$SD(Y) = \sqrt{1,440,000} = 1200\text{ ms}$$

---

### Exercise 6: Cumulative Latency Probability Bounds
**Problem:** For discrete execution time $T \in \{10, 20, 30, 40, 50\}\text{ ms}$ with PMF $p(t) = [0.10, 0.25, 0.35, 0.20, 0.10]$, compute $P(T \le 30\text{ ms})$ and $P(T > 20\text{ ms})$.

**Solution:**
- **Step 1: $P(T \le 30)$.**
  $$P(T \le 30) = p(10) + p(20) + p(30) = 0.10 + 0.25 + 0.35 = 0.70$$
- **Step 2: WIP State for $P(T > 20)$.**
  $$P(T > 20) = p(30) + p(40) + p(50) = 0.35 + 0.20 + ?$$
- **Step 3: Final Calculation.**
  $$P(T > 20) = 0.35 + 0.20 + 0.10 = 0.65$$

---

### Exercise 7: Discrete Clock Ticks to Event Completion
**Problem:** An algorithm completes in 1 clock tick with probability 0.5, 2 ticks with probability 0.3, and 3 ticks with probability 0.2. Construct the PMF table and compute the mean tick count.

**Solution:**

| $t$ (ticks) | 1 | 2 | 3 |
| :--- | :---: | :---: | :---: |
| $p(t)$ | 0.5 | 0.3 | 0.2 |

$$E[T] = (1 \cdot 0.5) + (2 \cdot 0.3) + (3 \cdot 0.2) = 0.5 + 0.6 + 0.6 = 1.7\text{ ticks}$$

---

### Exercise 8: Gotcha -- Variance of Time Difference
**Problem:** Two independent execution phases have duration variances $V(T_1) = 4\text{ ms}^2$ and $V(T_2) = 9\text{ ms}^2$. A developer computes the variance of the delay difference $V(T_1 - T_2)$ as $4 - 9 = -5\text{ ms}^2$. Correct the error.

**Solution:**
- **The Error:** Variance cannot be negative! Subtraction of variables adds their variances.
- **WIP State:**
  $$V(T_1 - T_2) = V(T_1) + (-1)^2 V(T_2) = V(T_1) + V(T_2) = 4 + ?$$
- **Final Calculation:**
  $$V(T_1 - T_2) = 4 + 9 = 13\text{ ms}^2$$

---

### Exercise 9: Sum of Expected Durations Across Stages
**Problem:** A microservice calls 3 sequential sub-tasks with independent discrete durations $T_1, T_2, T_3$ having means $E[T_1] = 12\text{ ms}$, $E[T_2] = 25\text{ ms}$, $E[T_3] = 8\text{ ms}$. Find the total expected execution time $E[T_{\text{total}}]$.

**Solution:**
- **Step 1: Apply linearity of expectation.**
  $$E[T_{\text{total}}] = E[T_1 + T_2 + T_3] = E[T_1] + E[T_2] + E[T_3]$$
- **Step 2: WIP State.**
  $$E[T_{\text{total}}] = 12 + 25 + ?$$
- **Step 3: Final Calculation.**
  $$E[T_{\text{total}}] = 12 + 25 + 8 = 45\text{ ms}$$

---

### Exercise 10: R Code Snippet -- Empirical Discrete Duration Analysis
**Problem:** Write R code to compute the PMF table, expected value, and variance from a vector of discrete processing times.

**Solution:**

```r
# Vector of observed task durations in seconds
durations <- c(1, 2, 2, 3, 1, 4, 2, 3, 3, 2)

# Build PMF table
val_counts <- table(durations)
pmf <- val_counts / length(durations)
t_vals <- as.numeric(names(pmf))

# Compute Expected Value E[T]
e_T <- sum(t_vals * pmf)

# Compute E[T^2] and Variance V(T)
e_T2 <- sum((t_vals^2) * pmf)
var_T <- e_T2 - (e_T^2)

cat("Discrete Time Values:", t_vals, "\n")
cat("PMF Probabilities:", round(as.numeric(pmf), 4), "\n")
cat("Expected Duration E[T]:", e_T, "sec\n")
cat("Variance V(T):", round(var_T, 4), "sec^2\n")
```

**Interpretation of Output:**
The script computes the discrete PMF using relative frequency, then applies $\sum t \cdot p(t)$ and $E[T^2] - (E[T])^2$ to return exact distribution parameters.
