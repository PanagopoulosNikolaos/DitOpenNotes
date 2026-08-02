# Phase 5.3 (Time): Continuous Uniform and Exponential Distributions

Continuous Uniform and Exponential distributions are fundamental continuous models for time metrics. The Uniform distribution models random wait or backoff times over a bounded interval $[a, b]$, while the Exponential distribution models waiting time between consecutive Poisson events and device time-to-failure.

---

## 1. Continuous Uniform Distribution for Time Intervals

A random variable $T$ follows a Continuous Uniform distribution on time interval $[a, b]$ (denoted $T \sim U(a, b)$) if all equal-length sub-intervals have equal probability.

### 1.1 PDF, CDF, Mean, and Variance
$$\text{PDF: } f_T(t) = \begin{cases} \frac{1}{b - a}, & a \le t \le b \\ 0, & \text{otherwise} \end{cases}$$

$$\text{CDF: } F_T(t) = P(T \le t) = \begin{cases} 0, & t < a \\ \frac{t - a}{b - a}, & a \le t \le b \\ 1, & t > b \end{cases}$$

$$\boxed{E[T] = \frac{a + b}{2}}, \quad \boxed{V(T) = \frac{(b - a)^2}{12}}, \quad SD(T) = \frac{b - a}{\sqrt{12}}$$

---

## 2. Exponential Distribution for Time-to-Event

A random variable $T$ follows an Exponential distribution with rate parameter $\lambda > 0$ (denoted $T \sim \text{Exp}(\lambda)$) if it models the time elapsed until the first event of a Poisson process with rate $\lambda$.

### 2.1 PDF, CDF, Mean, and Variance
$$\text{PDF: } f_T(t) = \begin{cases} \lambda e^{-\lambda t}, & t \ge 0 \\ 0, & t < 0 \end{cases}$$

$$\text{CDF: } F_T(t) = P(T \le t) = \begin{cases} 1 - e^{-\lambda t}, & t \ge 0 \\ 0, & t < 0 \end{cases}$$

$$\text{Survival / Reliability Function: } S_T(t) = P(T > t) = \boxed{e^{-\lambda t}}$$

$$\boxed{E[T] = \frac{1}{\lambda}}, \quad \boxed{V(T) = \frac{1}{\lambda^2}}, \quad SD(T) = \frac{1}{\lambda}$$

---

## 3. The Memoryless Property of Exponential Time

The Exponential distribution is the **only** continuous distribution possessing the memoryless property. For any past elapsed time $s > 0$ and additional future time $t > 0$:

$$\boxed{P(T > s + t \mid T > s) = P(T > t) = e^{-\lambda t}}$$

*Physical Meaning:* A component that has survived $s$ hours without failing is as good as new; its remaining lifespan probability distribution does NOT depend on $s$.

---

## 4. Time-Specific Gotchas

### Gotcha 1: Confusing Rate $\lambda$ with Mean Time Between Events $\theta = 1/\lambda$
If mean time to failure is $\theta = 500\text{ hours}$, then rate $\lambda = 1/500 = 0.002\text{ failures/hour}$. Substituting $\lambda = 500$ directly into $f_T(t) = \lambda e^{-\lambda t}$ yields disastrous errors.

### Gotcha 2: Misinterpreting $P(T > t)$ vs $P(T \le t)$
The CDF calculates $P(T \le t) = 1 - e^{-\lambda t}$ (probability component HAS failed by time $t$). The reliability function calculates $P(T > t) = e^{-\lambda t}$ (probability component STILL functions at time $t$). Always check whether the question asks for failure or survival.

---

## 5. Solved Exercises (10 Examples)

### Exercise 1: Uniform Random Backoff Time
**Problem:** Network retransmission backoff delay $T$ is uniformly distributed between $10\text{ ms}$ and $50\text{ ms}$ ($T \sim U(10, 50)$). Find $P(T > 35\text{ ms})$, mean, and variance.

**Solution:**
- **Step 1: Compute Mean and Variance.**
  $$E[T] = \frac{10 + 50}{2} = 30\text{ ms}$$
  $$V(T) = \frac{(50 - 10)^2}{12} = \frac{1600}{12} = 133.33\text{ ms}^2$$
- **Step 2: WIP State for $P(T > 35)$.**
  $$P(T > 35) = 1 - F_T(35) = 1 - \frac{35 - 10}{50 - 10} = 1 - \frac{25}{40}$$
- **Step 3: Final Result.**
  $$P(T > 35) = 1 - 0.625 = 0.375 \text{ (37.5\%)}$$

---

### Exercise 2: Exponential Component Failure Probability
**Problem:** Hard drive failure time $T \sim \text{Exp}(\lambda)$ with rate $\lambda = 0.0001$ failures per hour. Find the probability of failure within the first $2{,}000$ hours.

**Solution:**
- **Step 1: Identify CDF formula.**
  $$P(T \le 2000) = 1 - e^{-\lambda t} = 1 - e^{-(0.0001)(2000)}$$
- **Step 2: WIP State.**
  $$\lambda t = 0.2, \quad e^{-0.2} \approx 0.81873$$
  $$P(T \le 2000) = 1 - 0.81873 = ?$$
- **Step 3: Final Result.**
  $$P(T \le 2000) = 0.1813 \text{ (18.13\%)}$$

---

### Exercise 3: Exponential Component Survival (Reliability)
**Problem:** For the same hard drive ($\lambda = 0.0001\text{ h}^{-1}$), what is the probability it survives beyond $5{,}000$ hours?

**Solution:**
- **Step 1: Apply survival function.**
  $$P(T > 5000) = e^{-\lambda t} = e^{-(0.0001)(5000)} = e^{-0.5}$$
- **Step 2: WIP State.**
  $$e^{-0.5} \approx 0.60653$$
- **Step 3: Final Result.**
  $$P(T > 5000) = 0.6065 \text{ (60.65\%)}$$

---

### Exercise 4: Proof and Application of Memoryless Property
**Problem:** A router session duration $T$ follows an Exponential distribution with mean duration $10\text{ minutes}$. Given that a session has already lasted $15\text{ minutes}$, what is the probability it lasts at least $5$ additional minutes?

**Solution:**
- **Step 1: Determine $\lambda$ and set up conditional probability.**
  $$\text{Mean } E[T] = 1/\lambda = 10 \implies \lambda = 0.1\text{ min}^{-1}$$
  $$P(T > 15 + 5 \mid T > 15) = P(T > 5) \text{ (by Memorylessness)}$$
- **Step 2: WIP State.**
  $$P(T > 5) = e^{-\lambda (5)} = e^{-(0.1)(5)} = e^{-0.5}$$
  $$e^{-0.5} \approx 0.6065$$
- **Step 3: Final Result.**
  $$P(T > 20 \mid T > 15) = 0.6065 \text{ (60.65\%)}$$

---

### Exercise 5: Finding Median Lifespan / Time ($t_{0.5}$)
**Problem:** Server time-to-crash $T \sim \text{Exp}(\lambda)$ with mean $\mu_T = 100\text{ hours}$. Find the median time to crash $t_{0.5}$.

**Solution:**
- **Step 1: Set CDF equal to 0.5.**
  $$F_T(t_{0.5}) = 1 - e^{-\lambda t_{0.5}} = 0.5 \implies e^{-\lambda t_{0.5}} = 0.5$$
- **Step 2: Solve for $t_{0.5}$.**
  $$-\lambda t_{0.5} = \ln(0.5) = -\ln(2) \implies t_{0.5} = \frac{\ln(2)}{\lambda} = \mu_T \cdot \ln(2)$$
- **Step 3: WIP State and Final Calculation.**
  $$t_{0.5} = 100 \times 0.69315 = 69.315\text{ hours}$$

---

### Exercise 6: Uniform Distribution Conditional Probability
**Problem:** A periodic job starts at a random time $T \sim U(0, 60)$ minutes. If the job has not started by minute $20$, what is the probability it starts before minute $40$?

**Solution:**
- **Step 1: Set up conditional probability.**
  $$P(T \le 40 \mid T > 20) = \frac{P(20 < T \le 40)}{P(T > 20)}$$
- **Step 2: WIP State.**
  $$P(20 < T \le 40) = \frac{40 - 20}{60 - 0} = \frac{20}{60} = \frac{1}{3}$$
  $$P(T > 20) = \frac{60 - 20}{60 - 0} = \frac{40}{60} = \frac{2}{3}$$
  $$P(T \le 40 \mid T > 20) = \frac{1/3}{2/3} = ?$$
- **Step 3: Final Result.**
  $$P(T \le 40 \mid T > 20) = 0.5 \text{ (50\%)}$$

---

### Exercise 7: Minimum of Independent Exponential Durations
**Problem:** A system relies on two parallel redundant components with failure times $T_1 \sim \text{Exp}(\lambda_1 = 0.02\text{ h}^{-1})$ and $T_2 \sim \text{Exp}(\lambda_2 = 0.03\text{ h}^{-1})$. System fails when the FIRST component fails ($T_{\text{min}} = \min(T_1, T_2)$). Find the distribution and mean time to system failure.

**Solution:**
- **Step 1: Combine independent survival functions.**
  $$P(T_{\text{min}} > t) = P(T_1 > t \text{ and } T_2 > t) = e^{-\lambda_1 t} \cdot e^{-\lambda_2 t} = e^{-(\lambda_1 + \lambda_2)t}$$
  $$T_{\text{min}} \sim \text{Exp}(\lambda_1 + \lambda_2) = \text{Exp}(0.02 + 0.03) = \text{Exp}(0.05\text{ h}^{-1})$$
- **Step 2: WIP State.**
  $$E[T_{\text{min}}] = \frac{1}{0.05} = 20\text{ hours}$$
- **Step 3: Final Result.**
  Mean time to first failure is $20\text{ hours}$.

---

### Exercise 8: Inter-Arrival Time from Poisson Rate
**Problem:** Requests arrive at rate $\lambda = 12$ requests per minute. Find the probability that the time between two consecutive requests is less than 5 seconds ($5/60 = 1/12\text{ min}$).

**Solution:**
- **Step 1: Identify Exponential parameter.**
  Inter-arrival time $T \sim \text{Exp}(\lambda = 12\text{ min}^{-1})$.
- **Step 2: WIP State.**
  $$P(T \le 1/12) = 1 - e^{-12 \times (1/12)} = 1 - e^{-1}$$
  $$e^{-1} \approx 0.36788$$
- **Step 3: Final Result.**
  $$P(T \le 5\text{ s}) = 1 - 0.36788 = 0.6321 \text{ (63.21\%)}$$

---

### Exercise 9: Standard Deviation Equal to Mean Property
**Problem:** Execution time $T \sim \text{Exp}(\lambda)$ has standard deviation $SD(T) = 15\text{ seconds}$. Find $P(T > 30\text{ seconds})$.

**Solution:**
- **Step 1: Exploit Exponential property $E[T] = SD(T) = 1/\lambda$.**
  $$SD(T) = 15 \implies \lambda = 1/15\text{ s}^{-1}$$
- **Step 2: WIP State.**
  $$P(T > 30) = e^{-\lambda t} = e^{-(1/15)(30)} = e^{-2}$$
  $$e^{-2} \approx 0.135335$$
- **Step 3: Final Result.**
  $$P(T > 30\text{ s}) = 0.1353 \text{ (13.53\%)}$$

---

### Exercise 10: R Code Verification for Exponential and Uniform
**Problem:** Demonstrate how to calculate probabilities and generate random variates for Uniform and Exponential time metrics in R.

**Solution:**
- **Step 1: R Script Setup.**
```r
# Uniform Backoff T ~ U(10, 50) ms
p_unif <- punif(q = 35, min = 10, max = 50, lower.tail = FALSE)
cat("P(T_unif > 35 ms):", round(p_unif, 4), "\n")

# Exponential Failure T ~ Exp(rate = 0.0001) hours
p_exp_fail <- pexp(q = 2000, rate = 0.0001)
cat("P(T_exp <= 2000 h):", round(p_exp_fail, 4), "\n")

# Exponential Survival P(T > 5000 h)
p_exp_surv <- pexp(q = 5000, rate = 0.0001, lower.tail = FALSE)
cat("P(T_exp > 5000 h):", round(p_exp_surv, 4), "\n")
```
- **Step 2: Execution Output.**
  `P(T_unif > 35 ms): 0.375`
  `P(T_exp <= 2000 h): 0.1813`
  `P(T_exp > 5000 h): 0.6065`
