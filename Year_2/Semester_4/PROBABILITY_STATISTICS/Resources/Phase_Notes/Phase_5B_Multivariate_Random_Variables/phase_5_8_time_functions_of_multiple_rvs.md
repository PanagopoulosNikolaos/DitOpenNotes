# Phase 5.8 (Time): Functions of Multiple Random Variables & Order Statistics

In systems architecture, total completion time is determined by combinations of stage execution times. For sequential execution, overall latency is the sum $Y = T_1 + T_2$ (convolution). For parallel execution, latency is bounded by the slowest task $Y_{\max} = \max(T_1, T_2)$ or fastest task $Y_{\min} = \min(T_1, T_2)$ (Order Statistics).

---

## 1. Distribution of Sums of Independent Time RVs (Convolution)

If continuous stage times $T_1$ and $T_2$ are independent with PDFs $f_{T_1}$ and $f_{T_2}$, the PDF of total time $Y = T_1 + T_2$ is given by the continuous convolution integral:

$$\boxed{f_Y(y) = \int_{-\infty}^{\infty} f_{T_1}(t) \, f_{T_2}(y - t) \, dt = (f_{T_1} * f_{T_2})(y)}$$

---

## 2. Order Statistics for Parallel System Latency

Let $T_1, T_2, \dots, T_n$ be $n$ independent, identically distributed (i.i.d.) continuous task execution times with common PDF $f(t)$ and CDF $F(t)$.

### 2.1 Minimum Execution Time $T_{(1)} = \min(T_1, T_2, \dots, T_n)$ (First Completion)
The time until the **first** of $n$ parallel tasks finishes:

$$\text{Survival Function: } P(T_{(1)} > t) = [1 - F(t)]^n$$

$$\boxed{\text{CDF: } F_{(1)}(t) = 1 - [1 - F(t)]^n}, \quad \boxed{\text{PDF: } f_{(1)}(t) = n [1 - F(t)]^{n-1} f(t)}$$

### 2.2 Maximum Execution Time $T_{(n)} = \max(T_1, T_2, \dots, T_n)$ (Parallel Bottleneck)
The time until **all** $n$ parallel tasks complete:

$$\boxed{\text{CDF: } F_{(n)}(t) = [F(t)]^n}, \quad \boxed{\text{PDF: } f_{(n)}(t) = n [F(t)]^{n-1} f(t)}$$

---

## 3. Time-Specific Gotchas

### Gotcha 1: Convolving Exponential RVs with DIFFERENT Rates
When $T_1 \sim \text{Exp}(\lambda_1)$ and $T_2 \sim \text{Exp}(\lambda_2)$ with $\lambda_1 \neq \lambda_2$, $T_1 + T_2$ is NOT a Gamma distribution! The PDF of the sum is a Hypoexponential distribution:
$$\boxed{f_Y(y) = \frac{\lambda_1 \lambda_2}{\lambda_2 - \lambda_1} \left( e^{-\lambda_1 y} - e^{-\lambda_2 y} \right), \quad y \ge 0}$$

### Gotcha 2: Underestimating Parallel Latency Bottlenecks
For $n$ parallel tasks each taking average duration $\mu$, the average total time $\mu_{\text{parallel}} = E[\max(T_1, \dots, T_n)]$ is strictly GREATER than $\mu$. Assuming parallel execution completes in average single-task time $\mu$ ignores variance in individual tail latencies.

---

## 4. Solved Exercises (10 Examples)

### Exercise 1: Convolution of Two Independent Uniform Stage Times
**Problem:** $T_1 \sim U(0, 1)$ and $T_2 \sim U(0, 1)$ represent independent stage times in seconds. Find the PDF of total time $Y = T_1 + T_2$.

**Solution:**
- **Step 1: Set up convolution integral over non-zero overlap.**
  $$f_Y(y) = \int_0^1 f_{T_1}(t) f_{T_2}(y - t) dt$$
- **Step 2: WIP State for $0 \le y \le 1$ and $1 < y \le 2$.**
  For $0 \le y \le 1$: $0 \le t \le y \implies f_Y(y) = \int_0^y (1)(1) dt = y$.
  For $1 < y \le 2$: $y - 1 \le t \le 1 \implies f_Y(y) = \int_{y-1}^1 (1)(1) dt = 1 - (y - 1) = 2 - y$.
- **Step 3: Final Result.**
  $$f_Y(y) = \begin{cases} y, & 0 \le y \le 1 \\ 2 - y, & 1 < y \le 2 \\ 0, & \text{otherwise} \end{cases} \quad (\text{Triangular Distribution})$$

---

### Exercise 2: Parallel Task Bottleneck (Maximum of 3 Uniform RVs)
**Problem:** 3 parallel threads execute independent tasks with duration $T_i \sim U(0, 10)$ seconds. Find the CDF and PDF of overall completion time $Y_{\max} = \max(T_1, T_2, T_3)$.

**Solution:**
- **Step 1: Identify single task CDF $F(t) = t / 10$ for $0 \le t \le 10$.**
- **Step 2: Apply order statistic maximum formula.**
  $$F_{(3)}(t) = [F(t)]^3 = \left(\frac{t}{10}\right)^3 = \frac{t^3}{1000}, \quad 0 \le t \le 10$$
- **Step 3: Differentiate to find PDF.**
  $$f_{(3)}(t) = \frac{d}{dt} \left( \frac{t^3}{1000} \right) = \frac{3 t^2}{1000}, \quad 0 \le t \le 10$$

---

### Exercise 3: Expected Parallel Completion Time $E[\max(T_1, T_2, T_3)]$
**Problem:** For $Y_{\max}$ from Exercise 2, compute the expected parallel completion time $E[Y_{\max}]$. Compare with single task expectation $E[T] = 5\text{ s}$.

**Solution:**
- **Step 1: Integrate $t \cdot f_{(3)}(t)$.**
  $$E[Y_{\max}] = \int_0^{10} t \left( \frac{3 t^2}{1000} \right) dt = \frac{3}{1000} \int_0^{10} t^3 dt$$
- **Step 2: WIP State.**
  $$E[Y_{\max}] = \frac{3}{1000} \left[ \frac{t^4}{4} \right]_0^{10} = \frac{3}{1000} \left( \frac{10000}{4} \right) = \frac{30}{4} = 7.5\text{ s}$$
- **Step 3: Final Result.**
  $E[\max(T_1, T_2, T_3)] = 7.5\text{ s} > 5\text{ s}$ (parallel bottleneck increases average latency by $50\%$).

---

### Exercise 4: Minimum of 4 Independent Exponential Failure Times
**Problem:** 4 independent components have failure times $T_i \sim \text{Exp}(\lambda = 0.05\text{ h}^{-1})$. Find the distribution, mean, and probability of system survival beyond $10\text{ hours}$ for $Y_{\min} = \min(T_1, \dots, T_4)$.

**Solution:**
- **Step 1: Sum rate parameters.**
  $$Y_{\min} \sim \text{Exp}(4 \times 0.05) = \text{Exp}(0.20\text{ h}^{-1})$$
- **Step 2: WIP State.**
  $$E[Y_{\min}] = \frac{1}{0.20} = 5\text{ hours}$$
  $$P(Y_{\min} > 10) = e^{-0.20(10)} = e^{-2} \approx 0.1353$$
- **Step 3: Final Result.**
  $E[Y_{\min}] = 5\text{ h}$, $P(Y_{\min} > 10) = 0.1353 \text{ (13.53\%)}$.

---

### Exercise 5: Convolving Two Exponential RVs with Different Rates
**Problem:** Stage 1 duration $T_1 \sim \text{Exp}(\lambda_1 = 2\text{ s}^{-1})$ and Stage 2 duration $T_2 \sim \text{Exp}(\lambda_2 = 5\text{ s}^{-1})$, independently. Find $P(T_1 + T_2 \le 1\text{ s})$.

**Solution:**
- **Step 1: Write Hypoexponential PDF formula.**
  $$f_Y(y) = \frac{2 \times 5}{5 - 2} (e^{-2y} - e^{-5y}) = \frac{10}{3} (e^{-2y} - e^{-5y}), \quad y \ge 0$$
- **Step 2: Integrate PDF from $0$ to $1$.**
  $$P(Y \le 1) = \frac{10}{3} \int_0^1 (e^{-2y} - e^{-5y}) dy = \frac{10}{3} \left[ -\frac{e^{-2y}}{2} + \frac{e^{-5y}}{5} \right]_0^1$$
  $$P(Y \le 1) = \frac{10}{3} \left[ \left(-\frac{e^{-2}}{2} + \frac{e^{-5}}{5}\right) - \left(-\frac{1}{2} + \frac{1}{5}\right) \right]$$
- **Step 3: WIP State and Final Calculation.**
  $$-\frac{e^{-2}}{2} + \frac{e^{-5}}{5} \approx -0.06767 + 0.00135 = -0.06632$$
  $$-\frac{1}{2} + \frac{1}{5} = -0.30 \implies -0.06632 - (-0.30) = 0.23368$$
  $$P(Y \le 1) = \frac{10}{3} \times 0.23368 \approx 0.7789 \text{ (77.89\%)}$$

---

### Exercise 6: Maximum of 2 Independent Exponential RVs
**Problem:** Two parallel redundant microservices have response times $T_1, T_2 \sim \text{Exp}(\lambda = 1\text{ ms}^{-1})$. Find the CDF and mean of total response time $Y_{\max} = \max(T_1, T_2)$.

**Solution:**
- **Step 1: Calculate CDF $F_{\max}(t)$.**
  $$F(t) = 1 - e^{-\lambda t} \implies F_{\max}(t) = (1 - e^{-\lambda t})^2 = 1 - 2e^{-\lambda t} + e^{-2\lambda t}$$
- **Step 2: Integrate $S_{\max}(t) = 1 - F_{\max}(t)$ to find expectation.**
  $$S_{\max}(t) = 2e^{-\lambda t} - e^{-2\lambda t}$$
  $$E[Y_{\max}] = \int_0^\infty (2e^{-\lambda t} - e^{-2\lambda t}) dt = \frac{2}{\lambda} - \frac{1}{2\lambda} = \frac{3}{2\lambda}$$
- **Step 3: Final Result.**
  For $\lambda = 1$, $E[Y_{\max}] = 1.5\text{ ms}$ (compared to single-service mean $1.0\text{ ms}$).

---

### Exercise 7: Ratio of Two Independent Exponential Time RVs ($Y = T_1 / T_2$)
**Problem:** Let $T_1 \sim \text{Exp}(\lambda_1)$ and $T_2 \sim \text{Exp}(\lambda_2)$ be independent execution times. Prove that $Y = T_1 / T_2$ follows an $F$-like continuous ratio distribution with PDF $f_Y(y) = \frac{\lambda_1 \lambda_2}{(\lambda_1 y + \lambda_2)^2}$ for $y > 0$.

**Solution:**
- **Step 1: Set up joint CDF $P(T_1 / T_2 \le y) = P(T_1 \le y T_2)$.**
  $$F_Y(y) = \int_0^\infty \left( \int_0^{y t_2} \lambda_1 e^{-\lambda_1 t_1} dt_1 \right) \lambda_2 e^{-\lambda_2 t_2} dt_2$$
- **Step 2: Inner integral.**
  $$\int_0^{y t_2} \lambda_1 e^{-\lambda_1 t_1} dt_1 = 1 - e^{-\lambda_1 y t_2}$$
  $$F_Y(y) = \int_0^\infty (1 - e^{-\lambda_1 y t_2}) \lambda_2 e^{-\lambda_2 t_2} dt_2 = 1 - \frac{\lambda_2}{\lambda_1 y + \lambda_2} = \frac{\lambda_1 y}{\lambda_1 y + \lambda_2}$$
- **Step 3: Differentiate to get PDF.**
  $$f_Y(y) = \frac{d}{dy} \left( 1 - \frac{\lambda_2}{\lambda_1 y + \lambda_2} \right) = \frac{\lambda_1 \lambda_2}{(\lambda_1 y + \lambda_2)^2}, \quad y > 0$$

---

### Exercise 8: SLA Compliance for Maximum Latency $P(Y_{\max} \le 15\text{ ms})$
**Problem:** 5 independent nodes return results with latency $T_i \sim N(10, 4)$ in ms ($\mu = 10, \sigma = 2$). Find $P(\max(T_1, \dots, T_5) \le 13\text{ ms})$.

**Solution:**
- **Step 1: Compute single-node probability $P(T_i \le 13)$.**
  $$z = \frac{13 - 10}{2} = 1.50 \implies P(T_i \le 13) = \Phi(1.50) = 0.9332$$
- **Step 2: Raise single-node probability to the 5th power.**
  $$P(\max(T_1, \dots, T_5) \le 13) = (0.9332)^5$$
- **Step 3: WIP State and Final Result.**
  $$(0.9332)^5 \approx 0.7047 \text{ (70.47\%)}$$

---

### Exercise 9: Difference Between Two Normal Execution Times ($Y = T_1 - T_2$)
**Problem:** Server A latency $T_1 \sim N(100, 25)$ ms and Server B latency $T_2 \sim N(90, 16)$ ms, independently. Find the probability that Server A is faster than Server B ($P(T_1 < T_2) \implies P(T_1 - T_2 < 0)$).

**Solution:**
- **Step 1: Find distribution of $D = T_1 - T_2$.**
  $$\mu_D = 100 - 90 = 10\text{ ms}$$
  $$\sigma_D^2 = 25 + 16 = 41 \implies \sigma_D = \sqrt{41} \approx 6.403\text{ ms}$$
  $$D \sim N(10, 41)$$
- **Step 2: WIP State for $P(D < 0)$.**
  $$z = \frac{0 - 10}{6.403} = -1.56$$
  $$P(D < 0) = \Phi(-1.56) = 0.0594$$
- **Step 3: Final Result.**
  $$P(T_1 < T_2) = 0.0594 \text{ (5.94\%)}$$

---

### Exercise 10: R Code Verification of Order Statistics for Parallel Tasks
**Problem:** Demonstrate how to calculate $E[\max(T_1, T_2, T_3)]$ for parallel uniform tasks in R.

**Solution:**
- **Step 1: R Script Setup.**
```r
set.seed(42)
N <- 1000000

# Simulate 3 parallel tasks T ~ U(0, 10)
t1 <- runif(N, 0, 10)
t2 <- runif(N, 0, 10)
t3 <- runif(N, 0, 10)

# Compute max for each trial
t_max <- pmax(t1, t2, t3)

cat("Empirical E[max(T1,T2,T3)]:", round(mean(t_max), 4), "s\n")
cat("Theoretical E[max(T1,T2,T3)]:", 7.5, "s\n")
```
- **Step 2: Execution Output.**
  `Empirical E[max(T1,T2,T3)]: 7.5002 s`
  `Theoretical E[max(T1,T2,T3)]: 7.5 s`
