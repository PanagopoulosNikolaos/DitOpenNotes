# Complete Theoretical & Methodological Exam Guide: Probability and Statistics (Course 405)

---

## Table of Contents
1. [Course Overview & Exam Structure](#1-course-overview--exam-structure)
2. [Unit 1: Probability Theory & Event Operations](#2-unit-1-probability-theory--event-operations)
3. [Unit 2: Descriptive Statistics (Ungrouped & Grouped Data)](#3-unit-2-descriptive-statistics-ungrouped--grouped-data)
4. [Unit 3: Discrete Random Variables & Binomial Distribution](#4-unit-3-discrete-random-variables--binomial-distribution)
5. [Unit 4: Continuous Random Variables & Normal Distribution](#5-unit-4-continuous-random-variables--normal-distribution)
6. [Unit 5: Advanced Topics & Sampling Distributions (CLT & Bivariate)](#6-unit-5-advanced-topics--sampling-distributions-clt--bivariate)
7. [Unit 6: Complete Reference Guide for R Language Commands](#7-unit-6-complete-reference-guide-for-r-language-commands)
8. [Unit 7: Step-by-Step Methodological Algorithms & Solution Recipes](#8-unit-7-step-by-step-methodological-algorithms--solution-recipes)
9. [Unit 8: Official Formula Sheet & Extended Relations](#9-unit-8-official-formula-sheet--extended-relations)
10. [Unit 9: Critical Exam Traps & Checklist of Common Mistakes](#10-unit-9-critical-exam-traps--checklist-of-common-mistakes)

---

## 1. Course Overview & Exam Structure

The examination for the course **Probability and Statistics (Course 405)** in the Department of Informatics & Telecommunications consists of **4 equivalent exam topics (2.5 marks each)**. Across all previous exam papers (2023–2026), the questions map consistently onto four core pillars:

| Exam Topic Category | Main Focus | Recurring Question Types | Mark Weight |
|---|---|---|---|
| **Topic 1** | Probability Theory & Events | Event operations ($A \cup B$, $A \cap B'$, $A' \cap B'$), Parametric probabilities, Conditional probability $P(A\|B)$, Independence vs. Mutually Exclusive (Disjoint), Total Probability & Bayes | 2.5 / 10 |
| **Topic 2** | Descriptive Statistics | Frequency tables for grouped data ($f_i, h_i, F_i, H_i$), Mean $\bar{x}$, Median $M$, Mode $T$, Quartiles ($Q_1, Q_3$), Variance $s^2$, Standard deviation $s$, Coefficient of variation $CV$, Quantile boundaries, R commands | 2.5 / 10 |
| **Topic 3** | Discrete Distributions | Binomial distribution $X \sim \text{Bin}(n, p)$, Probability function computations, "at least", "at most", $E[X]$, $\text{Var}(X)$, Selection & justification of a theoretical distribution model, R commands | 2.5 / 10 |
| **Topic 4** | Continuous Distributions | Normal distribution $X \sim N(\mu, \sigma^2)$, Z-standardization, Interval probabilities $P(a \le X \le b)$, Tail probabilities $P(X > a)$, Empirical Rule intervals ($\bar{x} \pm ks$), R commands | 2.5 / 10 |

---

## 2. Unit 1: Probability Theory & Event Operations

### 2.1 Set Theory & Axioms of Probability

Let $\Omega$ be the sample space of a random experiment, and let $A, B \subseteq \Omega$ be events.

#### Classical Definition of Probability
$$P(A) = \frac{N(A)}{N(\Omega)} = \frac{\text{Πλήθος ευνοϊκών περιπτώσεων}}{\text{Συνολικό πλήθος δυνατών περιπτώσεων}}$$

#### Kolmogorov Axioms
1. $0 \le P(A) \le 1$ for every event $A$.
2. $P(\Omega) = 1$.
3. If $A_1, A_2, \dots, A_n$ are mutually exclusive (pairwise disjoint) events ($A_i \cap A_j = \emptyset$ for $i \neq j$), then:
   $$P\left(\bigcup_{i=1}^n A_i\right) = \sum_{i=1}^n P(A_i)$$

---

### 2.2 Fundamental Identities & Event Operations

| Event Description | Set Notation | Probability Formula | Venn Diagram Relation |
|---|---|---|---|
| Complement of A | $A'$ or $A^c$ | $P(A') = 1 - P(A)$ | All elements outside the set $A$ |
| Empty Set | $\emptyset$ | $P(\emptyset) = 0$ | Impossible event |
| Union (At least one of A or B) | $A \cup B$ | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ | General addition rule |
| Intersection (Both A and B) | $A \cap B$ | $P(A \cap B) = P(A) + P(B) - P(A \cup B)$ | Common (overlapping) region |
| Only A (A but not B) | $A \setminus B = A \cap B'$ | $P(A \cap B') = P(A) - P(A \cap B)$ | Set $A$ minus the intersection |
| Only B (B but not A) | $B \setminus A = B \cap A'$ | $P(B \cap A') = P(B) - P(A \cap B)$ | Set $B$ minus the intersection |
| Neither A nor B | $A' \cap B'$ | $P(A' \cap B') = 1 - P(A \cup B)$ | De Morgan's law: $(A \cup B)'$ |
| Exactly one of A or B | $(A \cap B') \cup (B \cap A')$ | $P(A \cup B) - P(A \cap B) = P(A) + P(B) - 2P(A \cap B)$ | Union minus the intersection |
| Subset Property | $A \subseteq B$ | $P(B \setminus A) = P(B) - P(A)$, and $P(A) \le P(B)$ | The event $A$ is entirely contained in $B$ |

---

### 2.3 Conditional Probability & Independence

#### Conditional Probability
The probability of event $A$ occurring given that event $B$ has already occurred ($P(B) > 0$):
$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$

Correspondingly, the conditional probability of $B$ given $A'$ is:
$$P(B \mid A') = \frac{P(B \cap A')}{P(A')} = \frac{P(B) - P(A \cap B)}{1 - P(A)}$$

#### Multiplication Rule
$$P(A \cap B) = P(A \mid B) P(B) = P(B \mid A) P(A)$$

#### Independent Events vs. Mutually Exclusive (Disjoint) Events

| Property | Mutually Exclusive (Disjoint) | Independent |
|---|---|---|
| Definition | They cannot occur simultaneously: $A \cap B = \emptyset$ | The occurrence of $B$ does not affect $A$ |
| Intersection | $P(A \cap B) = 0$ | $P(A \cap B) = P(A) \cdot P(B)$ |
| Conditional Probability | $P(A \mid B) = 0$ | $P(A \mid B) = P(A)$ |
| Union Formula | $P(A \cup B) = P(A) + P(B)$ | $P(A \cup B) = P(A) + P(B) - P(A)P(B)$ |

> **Caution:** Mutually exclusive (disjoint) events with $P(A) > 0$ and $P(B) > 0$ are **never** independent, because $P(A \cap B) = 0 \neq P(A)P(B)$.

---

### 2.4 Law of Total Probability & Bayes' Theorem

#### Partition of the Sample Space
A set of events $\{A_1, A_2, \dots, A_n\}$ forms a partition of $\Omega$ if:
1. $A_i \cap A_j = \emptyset$ for every $i \neq j$ (pairwise disjoint).
2. $\bigcup_{i=1}^n A_i = \Omega$ (exhaustive).
3. $P(A_i) > 0$ for all $i$.

#### Law of Total Probability
For any event $B \subseteq \Omega$:
$$P(B) = \sum_{k=1}^n P(B \cap A_k) = \sum_{k=1}^n P(B \mid A_k) P(A_k)$$

#### Bayes' Theorem (A Posteriori / Posterior Probability)
$$P(A_i \mid B) = \frac{P(B \cap A_i)}{P(B)} = \frac{P(B \mid A_i) P(A_i)}{\sum_{k=1}^n P(B \mid A_k) P(A_k)}$$

---

### 2.5 Methodological Recipes for Parametric Probability Problems (Exam Topic 1)

Given $P(A) = a$, $P(B) = b$, and $P(A \cup B) = u$:

1. **If A and B are Mutually Exclusive (Disjoint):**
   $$P(A \cap B) = 0 \implies u = a + b \implies a = u - b$$

2. **If A and B are Independent:**
   $$P(A \cap B) = a \cdot b \implies u = a + b - a \cdot b \implies u - b = a(1 - b) \implies a = \frac{u - b}{1 - b}$$

3. **If B is a subset of A ($B \subseteq A$):**
   $$P(A \cap B) = P(B) = b \implies P(A \cup B) = P(A) = a \implies a = u$$

---

## 3. Unit 2: Descriptive Statistics (Ungrouped & Grouped Data)

### 3.1 Data Organization & Frequency Tables

When raw data are grouped into $k$ class intervals $[L_i, U_i)$ ($i = 1, 2, \dots, k$):

*   **Class Limits:** Lower limit $L_i$, Upper limit $U_i$.
*   **Class Width ($\delta$):** $\delta = U_i - L_i$ (assumed equal across all classes).
*   **Class Midpoint ($x_i$):**
    $$x_i = \frac{L_i + U_i}{2}$$
*   **Absolute Frequency ($f_i$):** Number of observations in class $i$. Total number of observations: $N = \sum_{i=1}^k f_i$.
*   **Relative Frequency ($h_i$):** Proportion of observations in class $i$:
    $$h_i = \frac{f_i}{N}, \quad \sum_{i=1}^k h_i = 1$$
*   **Cumulative Absolute Frequency ($F_i$):**
    $$F_i = \sum_{j=1}^i f_j = F_{i-1} + f_i, \quad F_k = N$$
*   **Cumulative Relative Frequency ($H_i$):**
    $$H_i = \frac{F_i}{N} = \sum_{j=1}^i h_j, \quad H_k = 1.00$$

#### Rules for Grouping Raw Data
1. **Range ($R$):** $R = x_{\max} - x_{\min}$
2. **Number of Classes ($k$):** (Sturges' rule) $k = 1 + 3.322 \cdot \log_{10}(N)$
3. **Class Width ($w$):** $w = \frac{R}{k}$ (rounded up to a suitable integer/decimal).

---

### 3.2 Measures of Central Tendency

#### Arithmetic Mean / Average ($\bar{x}$)
*   **Ungrouped Data:**
    $$\bar{x} = \frac{1}{n} \sum_{i=1}^n x_i$$
*   **Grouped Data:**
    $$\bar{x} = \frac{1}{N} \sum_{i=1}^k f_i x_i$$

#### Median ($M$)
*   **Ungrouped Data:** Middle value of the ordered data. If $n$ is odd, $M = x_{\left(\frac{n+1}{2}\right)}$. If $n$ is even, $M = \frac{x_{\left(\frac{n}{2}\right)} + x_{\left(\frac{n}{2}+1\right)}}{2}$.
*   **Grouped Data (Linear Interpolation):**
    First, locate the median class $i$ such that $F_{i-1} < \frac{N}{2} \le F_i$. Then:
    $$M = L_i + \frac{\delta}{f_i} \left( \frac{N}{2} - F_{i-1} \right)$$
    where $L_i$ is the lower limit of the median class, $\delta$ the class width, $f_i$ the absolute frequency of the median class, and $F_{i-1}$ the cumulative frequency of the preceding class.

#### Quartiles ($Q_1, Q_2, Q_3$)
*   $Q_2 = M$ (The Median).
*   **Grouped Data Formula:**
    To find $Q_k$ ($k=1, 2, 3$), locate the class where $F_{i-1} < \frac{k N}{4} \le F_i$:
    $$Q_k = L_i + \frac{\delta}{f_i} \left( \frac{k N}{4} - F_{i-1} \right)$$

#### Mode ($T$)
*   **Ungrouped Data:** The value with the highest frequency of occurrence.
*   **Grouped Data:**
    Locate the modal class (the class with the maximum absolute frequency $f_i$). Then:
    $$T = L_i + \delta \frac{\Delta_1}{\Delta_1 + \Delta_2}$$
    where $\Delta_1 = f_i - f_{i-1}$ (difference from the frequency of the preceding class) and $\Delta_2 = f_i - f_{i+1}$ (difference from the frequency of the following class).

---

### 3.3 Measures of Dispersion

#### Sample Variance ($s^2$)
*   **Ungrouped Data:**
    $$s^2 = \frac{1}{n-1} \sum_{i=1}^n (x_i - \bar{x})^2 = \frac{1}{n-1} \left[ \sum_{i=1}^n x_i^2 - n \bar{x}^2 \right]$$
*   **Grouped Data:**
    $$s^2 = \frac{1}{N-1} \sum_{i=1}^k f_i (x_i - \bar{x})^2$$

#### Sample Standard Deviation ($s$)
$$s = \sqrt{s^2}$$

#### Coefficient of Variation ($CV$)
A relative measure of dispersion, independent of the units of measurement:
$$CV = \frac{s}{\bar{x}}$$
It is multiplied by 100 to be expressed as a percentage: $CV\% = \left(\frac{s}{\bar{x}}\right) \times 100\%$.

---

### 3.4 The Empirical Rule (68-95-99.7 Rule)

For symmetric, bell-shaped (approximately normal) distributions:

```
                  +-----------------------+  68.26%  (--> x_bar +/- 1s)
          +-------+-----------------------+-------+  95.44%  (--> x_bar +/- 2s)
  +-------+-------+-----------------------+-------+-------+  99.73%  (--> x_bar +/- 3s)
  |       |       |                       |       |       |
--+-------+-------+-----------+-----------+-------+-------+--
x_bar-3s x_bar-2s x_bar-1s  x_bar      x_bar+1s x_bar+2s x_bar+3s
```

*   **68% of the data** lies in the interval $[\bar{x} - s, \; \bar{x} + s]$.
*   **95% of the data** lies in the interval $[\bar{x} - 2s, \; \bar{x} + 2s]$.
*   **99.7% of the data** lies in the interval $[\bar{x} - 3s, \; \bar{x} + 3s]$.

---

## 4. Unit 3: Discrete Random Variables & Binomial Distribution

### 4.1 Fundamentals of Discrete Random Variables

A discrete random variable $X$ takes countably many discrete values $x_1, x_2, \dots, x_k$.

*   **Probability Mass Function (PMF):** $p(x_i) = P(X = x_i)$, which satisfies the conditions:
    $$\sum_{i=1}^k p(x_i) = 1, \quad 0 \le p(x_i) \le 1$$
*   **Cumulative Distribution Function (CDF):** $F(x) = P(X \le x) = \sum_{x_i \le x} p(x_i)$.
*   **Expected Value (Mean):**
    $$E[X] = \mu = \sum_{i=1}^k x_i \cdot P(X = x_i)$$
*   **Variance:**
    $$\text{Var}(X) = \sigma^2 = E[(X - \mu)^2] = E[X^2] - (E[X])^2 = \sum_{i=1}^k x_i^2 \cdot P(X = x_i) - \mu^2$$
*   **Standard Deviation:** $\sigma = \sqrt{\text{Var}(X)}$.

---

### 4.2 Binomial Distribution $X \sim \text{Bin}(n, p)$

#### Required Assumptions & Conditions (Crucial for Theory Questions!)
For a random variable $X$ to be modeled with the Binomial distribution, the following 4 conditions must hold:
1. **Fixed Number of Trials:** The experiment consists of $n$ fixed, identical trials.
2. **Binary Outcomes:** Each trial has only two possible outcomes: "Success" or "Failure".
3. **Constant Probability:** The probability of success $p$ is constant in each trial ($P(\text{Αποτυχία}) = q = 1 - p$).
4. **Independence:** All trials are mutually independent of one another.

#### Probability Mass Function (PMF)
$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k = 0, 1, 2, \dots, n$$
where the binomial coefficient is:
$$\binom{n}{k} = \frac{n!}{k!(n-k)!}$$

#### Cumulative Probabilities & Tail Probabilities

| Verbal Statement | Mathematical Expression | Computation Formula |
|---|---|---|
| Exactly $k$ successes | $P(X = k)$ | $\binom{n}{k} p^k (1-p)^{n-k}$ |
| At most $k$ successes | $P(X \le k)$ | $\sum_{j=0}^k \binom{n}{j} p^j (1-p)^{n-j}$ |
| Strictly fewer than $k$ | $P(X < k)$ | $P(X \le k - 1)$ |
| At least $k$ successes | $P(X \ge k)$ | $1 - P(X \le k - 1) = \sum_{j=k}^n \binom{n}{j} p^j (1-p)^{n-j}$ |
| Strictly more than $k$ | $P(X > k)$ | $1 - P(X \le k)$ |
| At least 1 success | $P(X \ge 1)$ | $1 - P(X = 0) = 1 - (1-p)^n$ |

#### Basic Theoretical Moments
*   **Expected Value:** $E[X] = \mu = n \cdot p$
*   **Variance:** $\text{Var}(X) = \sigma^2 = n \cdot p \cdot (1 - p)$
*   **Standard Deviation:** $\sigma = \sqrt{n \cdot p \cdot (1 - p)}$

---

## 5. Unit 4: Continuous Random Variables & Normal Distribution

### 5.1 Continuous Random Variables & Probability Density Function (PDF)

A continuous random variable $X$ takes uncountably infinitely many values over an interval of real numbers.

*   **Probability Density Function (PDF) $f(x)$:**
    $$P(a \le X \le b) = \int_{a}^{b} f(x) \, dx, \quad \int_{-\infty}^{+\infty} f(x) \, dx = 1$$
*   **Point Probability Rule:** For every continuous random variable and a specific value $c$:
    $$P(X = c) = 0 \implies P(a \le X \le b) = P(a < X < b) = P(a \le X < b) = P(a < X \le b)$$

---

### 5.2 The Normal Distribution $X \sim N(\mu, \sigma^2)$

A normal random variable $X$ has the probability density function (PDF):
$$f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}, \quad -\infty < x < +\infty$$

#### Basic Characteristics
1. A symmetric bell-shaped curve centered at the mean $\mu$.
2. The mean, median, and mode are all equal: $\bar{x} = M = T = \mu$.
3. The total area under the curve equals 1.0.

---

### 5.3 Z-Standardization & the Standard Normal Distribution $Z \sim N(0, 1)$

To compute probabilities for any $X \sim N(\mu, \sigma^2)$, we transform the variable $X$ into the Standard Normal variable $Z$:
$$Z = \frac{X - \mu}{\sigma} \sim N(0, 1)$$

#### Cumulative Distribution Function $\Phi(z)$
$$\Phi(z) = P(Z \le z)$$

#### Symmetry Properties of $\Phi(z)$
*   $\Phi(0) = 0.5000$
*   $\Phi(-z) = 1 - \Phi(z)$
*   $P(Z > z) = 1 - \Phi(z) = \Phi(-z)$
*   $P(z_1 \le Z \le z_2) = \Phi(z_2) - \Phi(z_1)$

```
   P(a <= X <= b) = P(z1 <= Z <= z2) = Phi(z2) - Phi(z1)

            z1 = (a - mu)/sigma      z2 = (b - mu)/sigma
                     |                    |
                     v                    v
              +--------------+------------+--
             /|              |            |\
            / |              |            | \
           /  |              |            |  \
   -------+---+--------------+------------+---+-------
             z1              0            z2
```

---

### 5.4 Quantile Boundary / Inverse Quantile Problems

When an exam question asks: *"Find the boundary value $x_0$ such that the top $p\%$ of observations exceeds $x_0$"*:

1. Convert the percentage into an upper-tail probability: $P(X > x_0) = \alpha = \frac{p}{100}$.
2. Convert to the lower tail: $P(X \le x_0) = 1 - \alpha$.
3. Find the corresponding standard normal $Z$-score value $z_\alpha$ from the table: $\Phi(z_\alpha) = 1 - \alpha$.
4. De-standardize to solve for $x_0$:
   $$z_\alpha = \frac{x_0 - \mu}{\sigma} \implies x_0 = \mu + z_\alpha \cdot \sigma$$

---

## 6. Unit 5: Advanced Topics & Sampling Distributions (CLT & Bivariate)

### 6.1 Central Limit Theorem (CLT)

Let $X_1, X_2, \dots, X_n$ be an independent and identically distributed (i.i.d.) random sample from any population with mean $\mu$ and finite variance $\sigma^2$.

#### Sampling Distribution of the Sample Mean
For a sample size $n \ge 30$, the sample mean $\bar{X} = \frac{1}{n}\sum_{i=1}^n X_i$ approximately follows the normal distribution:
$$\bar{X} \sim N\left(\mu, \frac{\sigma^2}{n}\right)$$

Standardized $Z$-score value for the sample mean:
$$Z = \frac{\bar{X} - \mu}{\frac{\sigma}{\sqrt{n}}} \sim N(0, 1)$$

#### Sampling Distribution of the Sum
The total sum $S_n = \sum_{i=1}^n X_i$ approximately follows the normal distribution:
$$S_n \sim N(n\mu, n\sigma^2)$$

Standardized $Z$-score value for the sum:
$$Z = \frac{S_n - n\mu}{\sigma\sqrt{n}} \sim N(0, 1)$$

---

### 6.2 Bivariate Distributions & Linear Relationship

For two random variables $X$ and $Y$:

*   **Covariance:**
    $$\text{Cov}(X, Y) = \sigma_{XY} = E[(X - \mu_X)(Y - \mu_Y)] = E[XY] - E[X]E[Y]$$
*   **Pearson Correlation Coefficient ($\rho_{XY}$):**
    $$\rho_{XY} = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y}, \quad -1 \le \rho_{XY} \le 1$$
*   **Independence Property:** If $X$ and $Y$ are independent, then $\text{Cov}(X, Y) = 0$ and $\rho_{XY} = 0$. (Note: The converse does not hold in general, except for the bivariate normal distribution).
*   **Variance of Linear Combinations:**
    $$\text{Var}(aX + bY) = a^2 \text{Var}(X) + b^2 \text{Var}(Y) + 2ab \text{Cov}(X, Y)$$
    If $X$ and $Y$ are independent:
    $$\text{Var}(aX + bY) = a^2 \text{Var}(X) + b^2 \text{Var}(Y)$$

---

## 7. Unit 6: Complete Reference Guide for R Language Commands

Every exam topic explicitly includes R command questions (worth ~0.5 to 1.0 marks per question). The complete syntax dictionary required for full marks is presented below.

### 7.1 R Commands for Descriptive Statistics

```r
# Δημιουργία διανύσματος
x <- c(12, 15, 18, 20, 22, 25, 30)

# Αριθμητικός Μέσος (Μέση Τιμή)
mean(x)

# Διάμεσος (50ό Ποσοστημόριο)
median(x)

# Δειγματική Τυπική Απόκλιση (s)
sd(x)

# Δειγματική Διακύμανση (s^2)
var(x)

# Ποσοστημόρια / Τεταρτημόρια
quantile(x, probs = 0.25)                # Q1 (1ο Τεταρτημόριο / 25ό ποσοστημόριο)
quantile(x, probs = 0.75)                # Q3 (3ο Τεταρτημόριο / 75ό ποσοστημόριο)
quantile(x, probs = c(0.25, 0.50, 0.75)) # Όλα τα τεταρτημόρια ταυτόχρονα

# Συνοπτικά στατιστικά μέτρα (Min, Q1, Διάμεσος, Μέση Τιμή, Q3, Max)
summary(x)

# Υπολογισμός Δεσπόζουσας/Τροπικής Τιμής στην R (Προσαρμοσμένη αναζήτηση πίνακα)
names(which.max(table(x)))
# Ή επιστροφή ως αριθμητική τιμή:
as.numeric(names(which.max(table(x))))
```

---

### 7.2 R Commands for the Binomial Distribution $X \sim \text{Bin}(n, p)$

```r
# 1. Ακριβής Πιθανότητα P(X = k)
dbinom(k, size = n, prob = p)
# Παράδειγμα: P(X = 1) για n = 6, p = 0.02
dbinom(1, size = 6, prob = 0.02)

# 2. Αθροιστική Πιθανότητα P(X <= k)
pbinom(k, size = n, prob = p)

# 3. Πιθανότητα Άνω Ουράς P(X >= k) = 1 - P(X <= k - 1)
# Παράδειγμα: P(X >= 2) για n = 6, p = 0.02
1 - pbinom(1, size = 6, prob = 0.02)
# Εναλλακτικά με χρήση lower.tail = FALSE:
pbinom(1, size = 6, prob = 0.02, lower.tail = FALSE)

# 4. Αυστηρά Μεγαλύτερο P(X > k)
1 - pbinom(k, size = n, prob = p)
pbinom(k, size = n, prob = p, lower.tail = FALSE)

# 5. Αντίστροφο Ποσοστημόριο (Εύρεση του k ώστε P(X <= k) >= prob)
qbinom(p_prob, size = n, prob = p)
```

---

### 7.3 R Commands for the Normal Distribution $X \sim N(\mu, \sigma)$

```r
# 1. Πιθανότητα Κάτω Ουράς P(X <= x)
pnorm(x, mean = mu, sd = sigma)

# 2. Πιθανότητα Άνω Ουράς P(X > a)
1 - pnorm(a, mean = mu, sd = sigma)
# Εναλλακτικά:
pnorm(a, mean = mu, sd = sigma, lower.tail = FALSE)

# 3. Πιθανότητα Διαστήματος P(a <= X <= b)
pnorm(b, mean = mu, sd = sigma) - pnorm(a, mean = mu, sd = sigma)
# Παράδειγμα: P(39 <= X <= 57) για mu = 48, sigma = 4
pnorm(57, mean = 48, sd = 4) - pnorm(39, mean = 48, sd = 4)

# 4. Όριο Ποσοστημορίου / Αντίστροφο Κανονικό Ποσοστημόριο
# Εύρεση της τιμής x0 ώστε P(X <= x0) = p
qnorm(p, mean = mu, sd = sigma)
# Παράδειγμα: Όριο ανώτερου 25% (η κάτω ουρά είναι 0.75)
qnorm(0.75, mean = mu, sd = sigma)
```

---

## 8. Unit 7: Step-by-Step Methodological Algorithms & Solution Recipes

### 8.1 Recipe 1: Solving Exam Topic 1 (Set, Probability & Venn Diagram Problems)

1. **Define the Events Explicitly:** Let $A = \{\text{διαβάζει Εφημερίδα A}\}$, $B = \{\text{διαβάζει Εφημερίδα B}\}$.
2. **Extract the Given Values:** Record $P(A)$, $P(B)$, and $P(A \cap B)$ or $P(A \cup B)$ from the percentages in the problem statement.
3. **Carry Out the Sub-Questions:**
   - *At least one:* Apply $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.
   - *Only A:* Apply $P(A \cap B') = P(A) - P(A \cap B)$.
   - *Neither one nor the other:* Apply $P(A' \cap B') = 1 - P(A \cup B)$.
   - *Conditional $P(A \mid B)$:* Apply $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$.
   - *Conditional $P(A \mid B')$:* Apply $P(A \mid B') = \frac{P(A) - P(A \cap B)}{1 - P(B)}$.

---

### 8.2 Recipe 2: Completing Frequency Tables & Statistical Measures (Exam Topic 2)

1. **Compute the Class Midpoints ($x_i$):** $x_i = \frac{L_i + U_i}{2}$ for each row.
2. **Fill in the $f_i x_i$ Column:** Multiply the frequency $f_i$ by the midpoint $x_i$. Sum to obtain $\sum f_i x_i$.
3. **Compute the Mean ($\bar{x}$):** $\bar{x} = \frac{\sum f_i x_i}{N}$, where $N = \sum f_i$.
4. **Fill in the $(x_i - \bar{x})^2$ and $f_i(x_i - \bar{x})^2$ Columns:** Compute the squared deviation for each row, multiply by $f_i$, and sum to obtain $\sum f_i(x_i - \bar{x})^2$.
5. **Compute the Variance ($s^2$) & Standard Deviation ($s$):**
   $$s^2 = \frac{\sum f_i(x_i - \bar{x})^2}{N - 1}, \quad s = \sqrt{s^2}$$
6. **Compute the Cumulative Frequencies ($F_i$):** Running total of the $f_i$.
7. **Interpolate the Median ($M$) / Quartiles ($Q_k$):**
   - Locate the class where $F_{i-1} < \frac{k N}{4} \le F_i$.
   - Apply the formula: $Q_k = L_i + \frac{\delta}{f_i}\left(\frac{k N}{4} - F_{i-1}\right)$.
8. **Determine Boundary Criteria (Bonus / Upper Percentage):**
   - The boundary for the "top 25%" corresponds to $Q_3$ ($k=3$).
   - The bonus boundary for the "lowest 25% time" corresponds to $Q_1$ ($k=1$).

---

### 8.3 Recipe 3: Solving Binomial Distribution Exercises (Exam Topic 3)

1. **State the Distribution & Its Parameters:** State explicitly: "Let $X$ be the number of defective units. $X \sim \text{Bin}(n, p)$ where $n = \text{μέγεθος δείγματος}$ and $p = \text{πιθανότητα επιτυχίας}$."
2. **Justify the Model Choice (if asked):** State the 4 conditions (fixed $n$, binary outcomes, constant $p$, independent trials).
3. **Apply PMF / Cumulative Formulas:**
   - Exactly 1: $P(X = 1) = \binom{n}{1} p^1 (1-p)^{n-1}$.
   - At least 2: $P(X \ge 2) = 1 - P(X = 0) - P(X = 1) = 1 - (1-p)^n - n p (1-p)^{n-1}$.
4. **Compute the Expected Value & Standard Deviation:** $E[X] = n p$, $\sigma = \sqrt{n p (1-p)}$.
5. **Write the R Command:** State the exact R command: `dbinom(1, n, p)` or `1 - pbinom(1, n, p)`.

---

### 8.4 Recipe 4: Solving Normal Distribution Exercises (Exam Topic 4)

1. **Identify the Parameters:** $X \sim N(\mu, \sigma^2)$ with $\mu$ and $\sigma$ given.
2. **Standardize the Boundaries:** Convert $x$ to $Z = \frac{x - \mu}{\sigma}$.
3. **Compute the Probabilities Using $\Phi(z)$:**
   - $P(X > a) = P\left(Z > \frac{a-\mu}{\sigma}\right) = 1 - \Phi(z_a) = \Phi(-z_a)$.
   - $P(a < X < b) = \Phi\left(\frac{b-\mu}{\sigma}\right) - \Phi\left(\frac{a-\mu}{\sigma}\right) = \Phi(z_b) - \Phi(z_a)$.
4. **Write the R Command:** State `pnorm(b, mu, sigma) - pnorm(a, mu, sigma)`.

---

## 9. Unit 8: Official Formula Sheet & Extended Relations

Below is the complete set of formulas provided on the official exam formula sheet, together with key extended relations:

### Official Exam Formula Sheet (Formula Sheet 405)

$$\bar{X} = \frac{1}{n} \sum_{i=1}^n X_i, \quad \bar{X} = \frac{1}{n} \sum_{i=1}^k X_i f_i$$

$$s^2 = \frac{1}{n-1} \sum_{i=1}^n (x_i - \bar{x})^2, \quad s^2 = \frac{1}{n-1} \sum_{i=1}^k (X_i - \bar{X})^2 \cdot f_i$$

$$CV = \frac{s}{\bar{x}}$$

$$\text{Αν } F_{(i-1)} \le \frac{N}{2} \le F_i \implies M = x_{(i-1)} + \frac{\delta}{f_i} \left( \frac{N}{2} - F_{(i-1)} \right)$$

$$\text{Αν } F_{(i-1)} \le \frac{kN}{4} \le F_i \implies Q_k = x_{(i-1)} + \frac{\delta}{f_i} \left( \frac{kN}{4} - F_{(i-1)} \right), \quad k = 1, 2, 3$$

$$T = x_{(i-1)} + \delta \frac{\Delta_1}{\Delta_1 + \Delta_2}$$

$$P(A) = \frac{N(A)}{N(\Omega)}$$

$$P(A') = 1 - P(A), \quad P(\emptyset) = 0, \quad P(A) \le 1$$

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

$$\text{Αν τα } A_1, \dots, A_n \text{ είναι ξένα: } P(A_1 \cup \dots \cup A_n) = \sum_{i=1}^n P(A_i)$$

$$\text{Αν } A \subseteq B \implies P(B - A) = P(B) - P(A) \text{ και } P(A) \le P(B)$$

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) > 0$$

$$P(A \cap B) = P(A \mid B) P(B)$$

$$\text{Ανεξάρτητα: } P(A \cap B) = P(A) P(B)$$

$$P(B) = \sum_{k=1}^n P(B \cap A_k) = \sum_{k=1}^n P(B \mid A_k) P(A_k)$$

$$P(A_i \mid B) = \frac{P(B \cap A_i)}{P(B)} = \frac{P(B \mid A_i) P(A_i)}{\sum_{k=1}^n P(B \mid A_k) P(A_k)}$$

---

## 10. Unit 9: Critical Exam Traps & Checklist of Common Mistakes

| # | Common Exam Trap | Correct Rule / Avoidance Strategy |
|---|---|---|
| 1 | **Confusing Mutually Exclusive (Disjoint) with Independent** | Mutually exclusive means $P(A \cap B) = 0$. Independent means $P(A \cap B) = P(A)P(B)$. Never set $P(A \cap B) = 0$ for independent events! |
| 2 | **Dividing by $N$ instead of $N-1$ in the sample variance** | In statistics exams, the sample variance always uses $N-1$ in the denominator: $s^2 = \frac{\sum f_i(x_i - \bar{x})^2}{N-1}$. |
| 3 | **Wrong index shift in R for the Binomial $P(X \ge k)$** | In R, $P(X \ge 2)$ is `1 - pbinom(1, size, prob)` or `pbinom(1, size, prob, lower.tail = FALSE)`. Writing `1 - pbinom(2, ...)` also subtracts $k=2$, which is wrong! |
| 4 | **Failing to standardize the variable $X$ before using $\Phi(z)$** | Always compute the value $Z = \frac{X - \mu}{\sigma}$ first. Do not enter the raw values of $X$ directly into the function $\Phi()$. |
| 5 | **Using the variance instead of the standard deviation in R** | R's `pnorm()` and `qnorm()` functions take the standard deviation $\sigma$ as the `sd` argument, **not** the variance $\sigma^2$. |
| 6 | **Confusing $Q_1$ and $Q_3$ for upper/lower percentages** | The boundary for the "top 25% of larger values" is $Q_3$ (75th percentile). The boundary for the "top 25% of faster/smaller times" is $Q_1$ (25th percentile). |
| 7 | **Forgetting to multiply relative frequencies by 100 for percentages** | $h_i = 0.25$ means $25\%$. Always state the percentage clearly when proportions/percentages are requested. |
| 8 | **Writing $P(A \cap B) = P(A) + P(B)$** | The sum $P(A) + P(B)$ equals $P(A \cup B)$ only if $A, B$ are disjoint. For the intersection, $P(A \cap B) = P(A)P(B)$ only if they are independent. |
| 9 | **Incorrectly identifying the modal class in grouped data** | The modal class is the interval with the highest absolute frequency $f_i$, NOT the highest $x_i$ or the highest $f_i x_i$. |
| 10 | **Omitting the lower limit when interpolating grouped $M$ or $Q_k$** | Always add the lower limit $L_i$ of the median/quartile class: $M = L_i + \text{κλάσμα} \cdot \delta$. |
| 11 | **Confusing the Expected Value of the Binomial with the sample size** | The expected value is $E[X] = n p$. If a sample of $N=100$ products is drawn with $p=0.03$, the expected count is $100 \times 0.03 = 3$. |
| 12 | **Omitting the syntax for computing the mode in R** | R has no built-in `mode()` function for the statistical mode (`mode(x)` returns the storage type of the vector!). Use `names(which.max(table(x)))`. |

---
*End of the Complete Theoretical Exam Guide — Study this document to score 10/10 in Probability & Statistics (405).*
