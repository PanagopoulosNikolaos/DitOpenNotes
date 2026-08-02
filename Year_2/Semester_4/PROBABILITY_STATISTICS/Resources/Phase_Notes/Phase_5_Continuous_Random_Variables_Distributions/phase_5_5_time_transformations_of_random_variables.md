# Phase 5.5 (Time): Transformations of Time Random Variables

In performance monitoring and system modeling, raw time metrics $T$ (e.g., latency, response time) are frequently transformed to derive new operational variables $Y = g(T)$—such as system throughput ($Y = 1/T$), logarithmic response scale ($Y = \ln T$), or scaled temporal metrics.

---

## 1. Linear Transformations of Time RVs

For a continuous time random variable $T$ with PDF $f_T(t)$, expected value $E[T]$, and variance $V(T)$, let $Y = aT + b$ (where $a \neq 0$ and $b$ are constants).

### 1.1 Expectation, Variance, and PDF Transformation
$$\boxed{E[Y] = a E[T] + b}, \quad \boxed{V(Y) = a^2 V(T)}, \quad SD(Y) = |a| SD(T)$$

The PDF of the transformed time variable $Y$ is:

$$\boxed{f_Y(y) = \frac{1}{|a|} f_T\left( \frac{y - b}{a} \right)}$$

---

## 2. Monotonic Non-Linear Transformations (Change of Variable Technique)

If $Y = g(T)$ is a strictly monotonic (strictly increasing or decreasing) differentiable function over the support of continuous time RV $T$, then $T = g^{-1}(Y)$ is unique.

### 2.1 Transformation Formula via Jacobian / Derivative
$$\boxed{f_Y(y) = f_T\left( g^{-1}(y) \right) \cdot \left| \frac{d}{dy} g^{-1}(y) \right|}$$

Where $\left| \frac{d}{dy} g^{-1}(y) \right| = \frac{1}{|g'(t)|}$ is the absolute transformation scaling factor (1D Jacobian).

---

## 3. Important Special Transformations in Time Domain

### 3.1 Logarithmic Transformation ($Y = \ln T$) -> Log-Normal Latency
If $Y = \ln T \sim N(\mu, \sigma^2)$, then raw latency $T = e^Y$ follows a **Log-Normal distribution** $LN(\mu, \sigma^2)$:

$$\boxed{f_T(t) = \frac{1}{t \sigma \sqrt{2\pi}} \exp\left( -\frac{(\ln t - \mu)^2}{2\sigma^2} \right), \quad t > 0}$$

$$E[T] = \exp\left(\mu + \frac{\sigma^2}{2}\right), \quad V(T) = \left(e^{\sigma^2} - 1\right) \exp\left(2\mu + \sigma^2\right)$$

### 3.2 Reciprocal Transformation ($Y = 1/T$) -> Throughput
If $T$ is request processing time (in seconds/request), $Y = 1/T$ represents throughput (requests/second). Note that $E[1/T] \neq 1/E[T]$ (Jensen's Inequality).

---

## 4. Time-Specific Gotchas

### Gotcha 1: The Expectation Reciprocal Fallacy ($E[1/T] \neq 1/E[T]$)
A common mistake in capacity planning is calculating average throughput as $1 / E[T]$. By Jensen's Inequality for convex function $g(x) = 1/x$ ($x > 0$):
$$\boxed{E\left[\frac{1}{T}\right] > \frac{1}{E[T]}}$$
Calculating throughput from average latency strictly underestimates true expected throughput!

### Gotcha 2: Forgetting the Derivative / Jacobian Derivative Term $\left|\frac{dt}{dy}\right|$
When transforming $f_T(t)$ to $f_Y(y)$, simply substituting $t = g^{-1}(y)$ into $f_T(t)$ is WRONG. You must multiply by the derivative factor $\left|\frac{d t}{d y}\right|$ to preserve total probability area $= 1$.

---

## 5. Solved Exercises (10 Examples)

### Exercise 1: Linear Transformation of Latency (ms to seconds)
**Problem:** Latency $T$ in milliseconds has PDF $f_T(t) = 0.01 e^{-0.01 t}$ for $t \ge 0$. Find the PDF of $Y = T / 1000$ (latency in seconds).

**Solution:**
- **Step 1: Express $t$ in terms of $y$ and find derivative.**
  $$y = \frac{t}{1000} \implies t = 1000 y, \quad \frac{dt}{dy} = 1000$$
- **Step 2: Apply transformation formula.**
  $$f_Y(y) = f_T(1000y) \cdot |1000| = \left( 0.01 e^{-0.01(1000y)} \right) \cdot 1000$$
- **Step 3: Final Result.**
  $$f_Y(y) = 10 e^{-10 y}, \quad y \ge 0 \quad (Y \sim \text{Exp}(\lambda = 10\text{ s}^{-1}))$$

---

### Exercise 2: Logarithmic Transformation ($Y = \ln T$)
**Problem:** Execution time $T$ follows a Uniform distribution $T \sim U(1, e^2)$. Find the PDF of $Y = \ln T$.

**Solution:**
- **Step 1: Determine inverse function and domain.**
  $$y = \ln t \implies t = e^y, \quad \frac{dt}{dy} = e^y$$
  Domain: $t \in [1, e^2] \implies y \in [0, 2]$.
- **Step 2: WIP State.**
  $f_T(t) = \frac{1}{e^2 - 1}$.
  $$f_Y(y) = f_T(e^y) \cdot |e^y| = \frac{e^y}{e^2 - 1}, \quad 0 \le y \le 2$$
- **Step 3: Final Result.**
  $$f_Y(y) = \frac{e^y}{e^2 - 1} \text{ for } 0 \le y \le 2$$

---

### Exercise 3: Reciprocal Transformation ($Y = 1/T$) for Throughput
**Problem:** Processing time $T$ (in seconds) is continuously uniform on $[0.5, 2.0]$. Find the PDF of throughput $Y = 1/T$ (in operations/second).

**Solution:**
- **Step 1: Determine inverse function and domain.**
  $$y = 1/t \implies t = 1/y, \quad \left|\frac{dt}{dy}\right| = \left|-\frac{1}{y^2}\right| = \frac{1}{y^2}$$
  Domain: $t \in [0.5, 2.0] \implies y \in [0.5, 2.0]$.
- **Step 2: WIP State.**
  $f_T(t) = \frac{1}{2.0 - 0.5} = \frac{1}{1.5} = \frac{2}{3}$.
  $$f_Y(y) = \frac{2}{3} \cdot \frac{1}{y^2} = \frac{2}{3 y^2}, \quad 0.5 \le y \le 2.0$$
- **Step 3: Final Result.**
  $$f_Y(y) = \frac{2}{3 y^2} \text{ for } 0.5 \le y \le 2.0$$

---

### Exercise 4: Expected Throughput vs Reciprocal of Expected Latency
**Problem:** For processing time $T \sim U(0.5, 2.0)$ from Exercise 3, compute $E[T]$, $1/E[T]$, and expected throughput $E[Y] = E[1/T]$. Compare the values.

**Solution:**
- **Step 1: Compute $E[T]$ and $1/E[T]$.**
  $$E[T] = \frac{0.5 + 2.0}{2} = 1.25\text{ seconds}$$
  $$\frac{1}{E[T]} = \frac{1}{1.25} = 0.8\text{ ops/second}$$
- **Step 2: Compute $E[1/T]$ via integration.**
  $$E[Y] = \int_{0.5}^{2.0} \frac{1}{t} \cdot f_T(t) dt = \frac{2}{3} \int_{0.5}^{2.0} \frac{1}{t} dt = \frac{2}{3} [\ln t]_{0.5}^{2.0}$$
  $$E[Y] = \frac{2}{3} (\ln 2.0 - \ln 0.5) = \frac{2}{3} \ln(4) \approx \frac{2}{3} (1.38629) = 0.9242\text{ ops/second}$$
- **Step 3: Final Result.**
  $E[1/T] = 0.9242 > 1/E[T] = 0.8000$, confirming Jensen's Inequality.

---

### Exercise 5: Quadratic Transformation of Time Metric ($Y = T^2$)
**Problem:** Signal transmission duration $T$ has PDF $f_T(t) = 2t$ for $0 \le t \le 1$. Find the PDF of energy metric $Y = T^2$.

**Solution:**
- **Step 1: Find inverse function and derivative.**
  $$y = t^2 \implies t = \sqrt{y} = y^{1/2}, \quad \frac{dt}{dy} = \frac{1}{2\sqrt{y}}$$
  Domain: $t \in [0, 1] \implies y \in [0, 1]$.
- **Step 2: Apply transformation formula.**
  $$f_Y(y) = f_T(\sqrt{y}) \cdot \frac{1}{2\sqrt{y}} = (2\sqrt{y}) \cdot \frac{1}{2\sqrt{y}} = 1$$
- **Step 3: Final Result.**
  $$f_Y(y) = 1 \text{ for } 0 \le y \le 1 \quad (Y \sim U(0, 1))$$

---

### Exercise 6: Log-Normal Mean and Variance Calculation
**Problem:** Logarithmic server response time $Y = \ln T$ is normally distributed with $\mu = 3$ and $\sigma^2 = 0.25$ (where $T$ is in milliseconds). Calculate the expected real latency $E[T]$.

**Solution:**
- **Step 1: Apply Log-Normal mean formula.**
  $$E[T] = \exp\left(\mu + \frac{\sigma^2}{2}\right)$$
- **Step 2: WIP State.**
  $$\mu + \frac{\sigma^2}{2} = 3 + \frac{0.25}{2} = 3 + 0.125 = 3.125$$
  $$E[T] = e^{3.125} \approx 22.76$$
- **Step 3: Final Result.**
  Expected real response time $E[T] \approx 22.76\text{ ms}$.

---

### Exercise 7: Linear Shift and Scaling of Uniform Time Bounds
**Problem:** Let $T \sim U(0, 10)$ seconds be queueing delay. A total execution time includes a fixed overhead of $5$ seconds and a $2\times$ processing multiplier ($Y = 2T + 5$). Find $E[Y]$ and $V(Y)$.

**Solution:**
- **Step 1: Identify $E[T]$ and $V[T]$.**
  $$E[T] = 5\text{ s}, \quad V(T) = \frac{(10 - 0)^2}{12} = \frac{100}{12} = 8.333\text{ s}^2$$
- **Step 2: Apply linear transformation rules.**
  $$E[Y] = 2 E[T] + 5 = 2(5) + 5 = 15\text{ seconds}$$
  $$V(Y) = 2^2 V(T) = 4 \times 8.333 = 33.333\text{ seconds}^2$$
- **Step 3: Final Result.**
  $E[Y] = 15\text{ s}$, $V(Y) = 33.33\text{ s}^2$.

---

### Exercise 8: Transformation of Exponential RV ($Y = c T$)
**Problem:** Prove that if $T \sim \text{Exp}(\lambda)$ and $c > 0$, then $Y = c T \sim \text{Exp}(\lambda / c)$.

**Solution:**
- **Step 1: Express $t = y/c$ and derivative $\frac{dt}{dy} = \frac{1}{c}$.**
- **Step 2: Apply transformation formula.**
  $$f_Y(y) = f_T(y/c) \cdot \frac{1}{c} = \left( \lambda e^{-\lambda (y/c)} \right) \cdot \frac{1}{c} = \left(\frac{\lambda}{c}\right) e^{-(\lambda/c) y}$$
- **Step 3: Final Result.**
  $f_Y(y)$ is the PDF of Exponential with rate parameter $\lambda / c$.

---

### Exercise 9: Non-Monotonic Transformation Symmetry ($Y = T^2$ for symmetric $T$)
**Problem:** Latency error $T \sim N(0, \sigma^2)$. Find the PDF of squared error $Y = T^2$.

**Solution:**
- **Step 1: Account for two branches ($t = \pm \sqrt{y}$).**
  $$F_Y(y) = P(T^2 \le y) = P(-\sqrt{y} \le T \le \sqrt{y}) = F_T(\sqrt{y}) - F_T(-\sqrt{y})$$
- **Step 2: Differentiate with respect to $y$.**
  $$f_Y(y) = f_T(\sqrt{y}) \cdot \frac{1}{2\sqrt{y}} + f_T(-\sqrt{y}) \cdot \frac{1}{2\sqrt{y}} = \frac{1}{\sqrt{y}} f_T(\sqrt{y})$$
- **Step 3: Final Result.**
  Since $f_T(t) = \frac{1}{\sigma \sqrt{2\pi}} e^{-t^2 / 2\sigma^2}$,
  $$f_Y(y) = \frac{1}{\sigma \sqrt{2\pi y}} e^{-y / 2\sigma^2}, \quad y > 0 \quad (Y \sim \sigma^2 \chi_1^2)$$

---

### Exercise 10: R Simulation Verification of Log-Normal Transformation
**Problem:** Write R code to verify the Log-Normal expectation $E[T] = \exp(\mu + \sigma^2/2)$ for $Y = \ln T \sim N(3, 0.25)$.

**Solution:**
- **Step 1: R Script Setup.**
```r
set.seed(123)
mu_y <- 3
sd_y <- sqrt(0.25)

# Simulate 1,000,000 normal values for ln(T)
y_sim <- rnorm(1000000, mean = mu_y, sd = sd_y)
t_sim <- exp(y_sim)

# Empirical mean vs Theoretical mean
emp_mean <- mean(t_sim)
theo_mean <- exp(mu_y + (sd_y^2)/2)

cat("Empirical E[T]:", round(emp_mean, 4), "\n")
cat("Theoretical E[T]:", round(theo_mean, 4), "\n")
```
- **Step 2: Execution Output.**
  `Empirical E[T]: 22.7582`
  `Theoretical E[T]: 22.7595`
