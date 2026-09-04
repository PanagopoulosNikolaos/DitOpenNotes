# Practice Exam 01: Probability and Statistics (Course 405)

This practice examination strictly adheres to the official 4-topic examination structure of Course 405, allocating 2.5 marks to each of the four fundamental pillars.

**Duration:** 2 Hours  
**Total Grade:** 10.0 Marks  

---

## Topic 1: Probability Theory, Event Algebra, and Bayes' Theorem (2.5 Marks)

### Question 1.1 (1.5 Marks)
Let $A$ and $B$ be two events in a common sample space $\Omega$ with given probabilities:
$$P(A) = 0.55, \quad P(B) = 0.40, \quad P(A \cap B') = 0.35$$

1. Calculate the intersection probability $P(A \cap B)$.
2. Calculate the union probability $P(A \cup B)$.
3. Determine whether events $A$ and $B$ are statistically independent.
4. Calculate the conditional probability $P(B \mid A)$.

### Question 1.2 (1.0 Mark)
An autonomous vehicle navigation subsystem uses three independent sensors ($S_1, S_2, S_3$) to detect obstacles:
- Sensor $S_1$ detects an obstacle with probability $0.90$.
- Sensor $S_2$ detects an obstacle with probability $0.85$.
- Sensor $S_3$ detects an obstacle with probability $0.80$.

Assuming the sensors operate independently:
1. What is the probability that an obstacle is detected by **at least one** sensor?
2. What is the probability that an obstacle is detected by **exactly one** sensor?

---

## Topic 2: Descriptive Statistics and Linear Transformations (2.5 Marks)

### Question 2.1 (1.8 Marks)
A software benchmark records compilation times (in seconds) for $n = 40$ test builds, categorized into four equal-width class intervals:

| Interval $[L_i, U_i)$ | Absolute Frequency ($f_i$) |
|---|---|
| $[10, 20)$ | 8 |
| $[20, 30)$ | 16 |
| $[30, 40)$ | 12 |
| $[40, 50)$ | 4 |

1. Complete the frequency table by determining class midpoints $m_i$, relative frequencies $h_i$, and cumulative frequencies ($F_i, H_i$).
2. Compute the grouped arithmetic mean $\bar{x}$.
3. Compute the grouped sample variance $s^2$ and standard deviation $s$.
4. Calculate the grouped median $\tilde{x}$ using the linear interpolation formula.

### Question 2.2 (0.7 Marks)
Suppose every compilation time $X$ is scaled to account for container startup overhead: $Y = 1.5 X + 5$.
1. Calculate the new mean $\bar{y}$.
2. Calculate the new standard deviation $s_y$.
3. State the value of the new variance $s_y^2$.

---

## Topic 3: Discrete Random Variables and Binomial Distribution (2.5 Marks)

### Question 3.1 (1.5 Marks)
A database server receives concurrent write requests. Let $X$ be the number of write conflicts per second, with probability mass function (PMF):

| $x$ | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| $P(X = x)$ | $0.30$ | $0.35$ | $0.20$ | $c$ | $0.05$ |

1. Find the value of constant $c$ that makes $P(X = x)$ a valid probability mass function.
2. Compute the expected value $E[X]$.
3. Compute the variance $\text{Var}(X)$ and standard deviation $\sigma_X$.
4. Evaluate the cumulative distribution value $F(2.5) = P(X \le 2.5)$.

### Question 3.2 (1.0 Mark)
In a communications system, packets are routed across $n = 8$ independent hops. Each hop introduces routing delay with probability $p = 0.25$.
1. What is the probability that exactly 2 hops introduce delay?
2. What is the probability that at least 1 hop introduces delay?

---

## Topic 4: Continuous Distributions and Central Limit Theorem (2.5 Marks)

### Question 4.1 (1.5 Marks)
The battery operating life (in hours) of an IoT monitoring device is normally distributed with mean $\mu = 120 \text{ hours}$ and standard deviation $\sigma = 15 \text{ hours}$ ($X \sim N(120, 225)$).
1. What proportion of devices last longer than $135 \text{ hours}$?
2. What proportion of devices last between $96$ and $138 \text{ hours}$?
3. The manufacturer wishes to guarantee battery life for $T$ hours such that only $5\%$ of devices fail before $T$. Find $T$.

*(Standard normal reference: $\Phi(1.0) = 0.8413$, $\Phi(1.20) = 0.8849$, $\Phi(-1.60) = 0.0548$, $\Phi(-1.645) = 0.0500$)*

### Question 4.2 (1.0 Mark)
A file server processes file download requests whose sizes have mean $\mu = 3.5 \text{ MB}$ and standard deviation $\sigma = 1.2 \text{ MB}$. A sample of $n = 36$ independent download requests is observed.
1. State the distribution of the sample mean $\bar{X}$.
2. Calculate the probability that the sample mean download size exceeds $3.8 \text{ MB}$.

---

## Complete Solution and Marking Guide

### Solution to Topic 1

#### Question 1.1
1. $P(A \cap B') = P(A) - P(A \cap B) \implies 0.35 = 0.55 - P(A \cap B) \implies P(A \cap B) = 0.55 - 0.35 = \mathbf{0.20}$. *(0.4 Marks)*
2. $P(A \cup B) = P(A) + P(B) - P(A \cap B) = 0.55 + 0.40 - 0.20 = \mathbf{0.75}$. *(0.3 Marks)*
3. Independence test: $P(A) \cdot P(B) = 0.55 \times 0.40 = 0.22$. Since $P(A \cap B) = 0.20 \neq 0.22$, $A$ and $B$ are **not independent**. *(0.4 Marks)*
4. $P(B \mid A) = \frac{P(A \cap B)}{P(A)} = \frac{0.20}{0.55} = \frac{4}{11} \approx \mathbf{0.3636}$. *(0.4 Marks)*

#### Question 1.2
1. Complement rule: $P(\text{none detect}) = (1 - 0.90)(1 - 0.85)(1 - 0.80) = 0.10 \times 0.15 \times 0.20 = 0.003$.
   $$P(\text{at least one}) = 1 - 0.003 = \mathbf{0.997} \ (99.7\%)$$ *(0.5 Marks)*
2. $P(\text{only } S_1) = 0.90 \times 0.15 \times 0.20 = 0.027$.
   $P(\text{only } S_2) = 0.10 \times 0.85 \times 0.20 = 0.017$.
   $P(\text{only } S_3) = 0.10 \times 0.15 \times 0.80 = 0.012$.
   $$P(\text{exactly one}) = 0.027 + 0.017 + 0.012 = \mathbf{0.056} \ (5.6\%)$$ *(0.5 Marks)*

---

### Solution to Topic 2

#### Question 2.1
1. **Frequency Table ($n = 40$):**
   - $[10, 20): m_1 = 15, \ f_1 = 8, \ h_1 = 0.20, \ F_1 = 8, \ H_1 = 0.20$
   - $[20, 30): m_2 = 25, \ f_2 = 16, \ h_2 = 0.40, \ F_2 = 24, \ H_2 = 0.60$
   - $[30, 40): m_3 = 35, \ f_3 = 12, \ h_3 = 0.30, \ F_3 = 36, \ H_3 = 0.90$
   - $[40, 50): m_4 = 45, \ f_4 = 4, \ h_4 = 0.10, \ F_4 = 40, \ H_4 = 1.00$
   *(0.5 Marks)*
2. **Mean:**
   $$\bar{x} = \sum h_i m_i = (0.20 \times 15) + (0.40 \times 25) + (0.30 \times 35) + (0.10 \times 45) = 3 + 10 + 10.5 + 4.5 = \mathbf{28.0 \text{ s}}$$
   *(0.4 Marks)*
3. **Variance and Standard Deviation:**
   $\sum f_i m_i^2 = 8(225) + 16(625) + 12(1225) + 4(2025) = 1800 + 10000 + 14700 + 8100 = 34600$.
   $$s^2 = \frac{1}{n-1} \left( \sum f_i m_i^2 - n \bar{x}^2 \right) = \frac{1}{39} (34600 - 40(784)) = \frac{34600 - 31360}{39} = \frac{3240}{39} \approx \mathbf{83.08 \text{ s}^2}$$
   $$s = \sqrt{83.08} \approx \mathbf{9.11 \text{ s}}$$
   *(0.5 Marks)*
4. **Median:**
   $n/2 = 20$. Median class is $[20, 30)$ where $L_m = 20, F_{m-1} = 8, f_m = 16, w = 10$.
   $$\tilde{x} = 20 + \left( \frac{20 - 8}{16} \right) \times 10 = 20 + \left( \frac{12}{16} \right) \times 10 = 20 + 7.5 = \mathbf{27.5 \text{ s}}$$
   *(0.4 Marks)*

#### Question 2.2
1. $\bar{y} = 1.5 \bar{x} + 5 = (1.5 \times 28.0) + 5 = 42.0 + 5 = \mathbf{47.0 \text{ s}}$. *(0.3 Marks)*
2. $s_y = |1.5| \cdot s_x = 1.5 \times 9.11 = \mathbf{13.67 \text{ s}}$. *(0.2 Marks)*
3. $s_y^2 = (1.5)^2 \cdot s_x^2 = 2.25 \times 83.08 = \mathbf{186.93 \text{ s}^2}$. *(0.2 Marks)*

---

### Solution to Topic 3

#### Question 3.1
1. $\sum P(X = x) = 1 \implies 0.30 + 0.35 + 0.20 + c + 0.05 = 1 \implies 0.90 + c = 1 \implies \mathbf{c = 0.10}$. *(0.4 Marks)*
2. $E[X] = (0)(0.30) + (1)(0.35) + (2)(0.20) + (3)(0.10) + (4)(0.05) = 0 + 0.35 + 0.40 + 0.30 + 0.20 = \mathbf{1.25}$. *(0.4 Marks)*
3. $E[X^2] = (0)(0.30) + (1)(0.35) + (4)(0.20) + (9)(0.10) + (16)(0.05) = 0.35 + 0.80 + 0.90 + 0.80 = 2.85$.
   $$\text{Var}(X) = E[X^2] - (E[X])^2 = 2.85 - (1.25)^2 = 2.85 - 1.5625 = \mathbf{1.2875}$$
   $$\sigma_X = \sqrt{1.2875} \approx \mathbf{1.135}$$ *(0.4 Marks)*
4. $F(2.5) = P(X \le 2) = 0.30 + 0.35 + 0.20 = \mathbf{0.85}$. *(0.3 Marks)*

#### Question 3.2
1. $X \sim B(n = 8, p = 0.25)$.
   $$P(X = 2) = \binom{8}{2} (0.25)^2 (0.75)^6 = 28 \times 0.0625 \times 0.17798 \approx \mathbf{0.3115} \ (31.15\%)$$ *(0.5 Marks)*
2. $P(X \ge 1) = 1 - P(X = 0) = 1 - (0.75)^8 = 1 - 0.1001 = \mathbf{0.8999} \ (89.99\%)$. *(0.5 Marks)*

---

### Solution to Topic 4

#### Question 4.1
1. $X \sim N(120, 225) \implies \mu = 120, \sigma = 15$.
   $$Z = \frac{135 - 120}{15} = 1.0 \implies P(X > 135) = 1 - \Phi(1.0) = 1 - 0.8413 = \mathbf{0.1587} \ (15.87\%)$$ *(0.5 Marks)*
2. $Z_1 = \frac{96 - 120}{15} = \frac{-24}{15} = -1.60, \quad Z_2 = \frac{138 - 120}{15} = \frac{18}{15} = 1.20$.
   $$P(96 \le X \le 138) = \Phi(1.20) - \Phi(-1.60) = 0.8849 - 0.0548 = \mathbf{0.8301} \ (83.01\%)$$ *(0.5 Marks)*
3. Find $T$ such that $P(X \le T) = 0.05 \implies \Phi(Z) = 0.05 \implies Z = -1.645$.
   $$T = \mu + Z \cdot \sigma = 120 + (-1.645 \times 15) = 120 - 24.675 = \mathbf{95.33 \text{ hours}}$$ *(0.5 Marks)*

#### Question 4.2
1. By the Central Limit Theorem, since $n = 36 \ge 30$:
   $$\bar{X} \sim N\left(\mu = 3.5, \ \sigma_{\bar{X}}^2 = \frac{\sigma^2}{n} = \frac{1.44}{36} = 0.04\right) \implies \sigma_{\bar{X}} = 0.2 \text{ MB}$$ *(0.5 Marks)*
2. $Z = \frac{3.8 - 3.5}{0.2} = \frac{0.3}{0.2} = 1.50$.
   $$P(\bar{X} > 3.8) = 1 - \Phi(1.50) = 1 - 0.9332 = \mathbf{0.0668} \ (6.68\%)$$ *(0.5 Marks)*

