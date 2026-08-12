# Exam Paper Hard 1

**Level: Hard 1**
**UNIVERSITY OF IOANNINA**                   Full Name:_______________________
**Department of Computer Science & Telecommunications**    Student ID:________________________________
**COURSE: Probability & Statistics**          

Instructions:
1. Write your full name on the exam sheet.
2. All problems carry equal weight.
3. Hand in the question sheet along with your answer booklet.
4. Use of pocket calculators is permitted; mobile phones are prohibited.

**PROBLEM 1:** The following table shows monthly rent values (in €) for 100 apartments in an area. The frequency $f_2$ of the second class is unknown (let it be $x$).

| Rent (€) | Class Marks $x_i$ | Number of Apts $f_i$ | $f_i x_i$ | $f_i(x_i - \bar{x})^2$ | $F_i$ |
| --- | --- | --- | --- | --- | --- |
| [300, 400) | | 15 | | | |
| [400, 500) | | $x$ | | | |
| [500, 600) | | 40 | | | |
| [600, 700) | | 20 | | | |
| [700, 800) | | 5 | | | |
| Total | | 100 | | | |

a. Find the unknown frequency $x$ and complete the table columns.
b. Calculate the mean rent ($\bar{x}$), median ($M$), and standard deviation ($s$).
c. Which R commands are required to calculate the mean of these data if we had the original raw un-grouped data in a vector `rent`?

**PROBLEM 2:** A security system has a failure probability of $p=0.08$ on each breach attempt.
i) If 15 independent breach attempts occur, what is the probability that the system fails in at least 3 of them?
ii) How many independent breach attempts must take place at minimum so that the probability of at least one system failure is greater than 99%?
iii) Write the R commands for calculating the probabilities of questions i and ii.

**PROBLEM 3:** In a medical center, 2% of patients examined have a rare condition. A diagnostic test detects the condition with 98% probability (sensitivity), but yields a false positive result in 3% of healthy individuals (specificity of 97%).
A. What is the probability that a random individual tests positive?
B. If an individual tests positive, what is the probability that they actually have the condition?
C. If an individual tests negative, what is the probability that they are healthy?
D. Are the events "individual has condition" and "test is positive" independent? Justify your answer.

**PROBLEM 4:** The weight of coffee packages produced by a machine follows a Normal distribution with mean $\mu = 250$ grams and standard deviation $\sigma$ grams.
i. If it is known that 5% of packages weigh less than 241.8 grams, calculate the standard deviation $\sigma$.
ii. With the standard deviation found, what is the probability that a package weighs between 245 and 255 grams?
iii. Which R command finds the weight below which 10% of packages fall?
Given: For the standard normal variable $Z$, $\Phi(1.645) = P(Z \le 1.645) = 0.95$ and $\Phi(1.2) = 0.8849$.

### Solution to Problem 1

**a. Finding the unknown $x$**

$$\sum f_i = 100 \Rightarrow 15 + x + 40 + 20 + 5 = 100 \Rightarrow x = \boxed{20}$$

**Table Completion:**

| Rent | $x_i$ | $f_i$ | $f_i x_i$ | $F_i$ |
|---|---|---|---|---|
| [300, 400) | 350 | 15 | 5250  | 15  |
| [400, 500) | 450 | 20 | 9000  | 35  |
| [500, 600) | 550 | 40 | 22000 | 75  |
| [600, 700) | 650 | 20 | 13000 | 95  |
| [700, 800) | 750 | 5  | 3750  | 100 |
| Totals     |     | 100| 53000 |     |

**b. Mean $\bar{x}$**

$$\bar{x} = \frac{\sum f_i x_i}{n} = \frac{53000}{100} = \boxed{530 \text{ €}}$$

**Standard Deviation $s$**

| $x_i$ | $x_i - \bar{x}$ | $(x_i-\bar{x})^2$ | $f_i(x_i-\bar{x})^2$ |
|---|---|---|---|
| 350 | -180 | 32400 | 486000  |
| 450 | -80  | 6400  | 128000  |
| 550 | 20   | 400   | 16000   |
| 650 | 120  | 14400 | 288000  |
| 750 | 220  | 48400 | 242000  |
| **Total** | | | **1160000** |

$$s^2 = \frac{1160000}{99} \approx 11717.17, \qquad s = \sqrt{11717.17} \approx \boxed{108.25 \text{ €}}$$

**Median $M_e$**

- $n/2 = 50$. We have $F_2 = 35 < 50 \le 75 = F_3$, so the median lies in the class $[500, 600)$.

$$M_e = L + \left( \frac{\frac{n}{2} - F_{i-1}}{f_i} \right) \cdot w = 500 + \left( \frac{50 - 35}{40} \right) \cdot 100 = 500 + 37.5 = \boxed{537.50 \text{ €}}$$

**c. R commands for the mean**

```r
mean(rent)
```

---

**PROBLEM 2:** A security system has a failure probability of $p=0.08$ on each breach attempt.
i) If 15 independent breach attempts occur, what is the probability that the system fails in at least 3 of them?
ii) How many independent breach attempts must take place at minimum so that the probability of at least one system failure is greater than 99%?
iii) Write the R commands for calculating the probabilities of questions i and ii.

### Solution to Problem 2

**Given Data:** $p = 0.08$

**i. $P(X \ge 3)$ for $n=15$, $X \sim B(15,\ 0.08)$**

$$P(X \ge 3) = 1 - P(X=0) - P(X=1) - P(X=2)$$

$$P(X=0) = (0.92)^{15} = 0.2863$$

$$P(X=1) = \binom{15}{1}(0.08)(0.92)^{14} = 15 \times 0.08 \times 0.3112 = 0.3726$$

$$P(X=2) = \binom{15}{2}(0.08)^2(0.92)^{13} = 105 \times 0.0064 \times 0.3383 = 0.2273$$

$$P(X \ge 3) = 1 - 0.2863 - 0.3726 - 0.2273 = \boxed{0.1138}$$

**ii. Minimum $n$ such that $P(X \ge 1) > 0.99$**

$$P(X \ge 1) = 1 - P(X=0) = 1 - (0.92)^n > 0.99$$

$$(0.92)^n < 0.01$$

Taking logarithms:

$$n \cdot \ln(0.92) < \ln(0.01) \Rightarrow n > \frac{\ln(0.01)}{\ln(0.92)} = \frac{-4.6052}{-0.08338} \approx 55.24$$

$$n_{\min} = \boxed{56}$$

- The number is rounded up because a strict inequality is required.

**iii. R commands**

```r
# Question i
1 - pbinom(2, size = 15, prob = 0.08)

# Question ii
n <- 1
while ((1 - (0.92)^n) <= 0.99) n <- n + 1
n
# or: ceiling(log(0.01) / log(0.92))
```

---

**PROBLEM 3:** In a medical center, 2% of patients examined have a rare condition. A diagnostic test detects the condition with 98% probability (sensitivity), but yields a false positive result in 3% of healthy individuals (i.e., specificity of 97%).
A. What is the probability that a random individual tests positive?
B. If an individual tests positive, what is the probability that they actually have the condition?
C. If an individual tests negative, what is the probability that they are healthy?
D. Are the events "the individual has the condition" and "the test is positive" independent? Justify your answer.

### Solution to Problem 3

**Definition of events:**
- $P$ = the individual has the condition: $P(P) = 0.02$, $P(P') = 0.98$
- $T^+$ = test positive: $P(T^+ | P) = 0.98$, $P(T^+ | P') = 0.03$

**A. Total probability $P(T^+)$**

$$P(T^+) = P(T^+|P) \cdot P(P) + P(T^+|P') \cdot P(P')$$

$$= 0.98 \times 0.02 + 0.03 \times 0.98 = 0.0196 + 0.0294 = \boxed{0.0490}$$

**B. $P(P | T^+)$ — Bayes**

$$P(P \mid T^+) = \frac{P(T^+|P) \cdot P(P)}{P(T^+)} = \frac{0.98 \times 0.02}{0.0490} = \frac{0.0196}{0.0490} = \boxed{0.40}$$

- Although the sensitivity is high (98%), the low prevalence (2%) leads to a positive predictive value of only 40%.

**C. $P(P' | T^-)$ — negative predictive value**

$$P(T^-) = 1 - P(T^+) = 1 - 0.0490 = 0.9510$$

$$P(T^- | P) = 1 - 0.98 = 0.02, \qquad P(T^- | P') = 1 - 0.03 = 0.97$$

$$P(P' \mid T^-) = \frac{P(T^-|P') \cdot P(P')}{P(T^-)} = \frac{0.97 \times 0.98}{0.9510} = \frac{0.9506}{0.9510} \approx \boxed{0.9996}$$

**D. Independence?**

For independence it is required that: $P(P \cap T^+) = P(P) \cdot P(T^+)$

$$P(P \cap T^+) = P(T^+|P) \cdot P(P) = 0.98 \times 0.02 = 0.0196$$

$$P(P) \cdot P(T^+) = 0.02 \times 0.049 = 0.00098$$

$$0.0196 \ne 0.00098 \Rightarrow \text{the events } \textbf{are not independent.}$$

---

**PROBLEM 4:** The weight of coffee packages produced by a machine follows the Normal distribution with mean $\mu = 250$ grams and standard deviation $\sigma$ grams.
i. If it is known that 5% of packages weigh less than 241.8 grams, calculate the standard deviation $\sigma$.
ii. With the standard deviation found, what is the probability that a package weighs between 245 and 255 grams?
iii. Which R command finds the weight below which 10% of packages fall?
Given: For the standard normal variable $Z$, $\Phi(1.645) = P(Z \le 1.645) = 0.95$ and $\Phi(1.2) = 0.8849$.

### Solution to Problem 4

**Given Data:** $X \sim N(\mu=250,\ \sigma=?)$

**i. Finding $\sigma$**

$$P(X < 241.8) = 0.05 \Rightarrow P\!\left(Z < \frac{241.8 - 250}{\sigma}\right) = 0.05$$

- The 5th percentile of the standard normal corresponds to $z_{0.05} = -1.645$ (by symmetry: $\Phi(-1.645) = 0.05$).

$$\frac{241.8 - 250}{\sigma} = -1.645 \Rightarrow \frac{-8.2}{\sigma} = -1.645$$

$$\sigma = \frac{8.2}{1.645} = \boxed{5 \text{ g.}}$$

**ii. $P(245 \le X \le 255)$ with $\sigma = 5$**

$$z_1 = \frac{245 - 250}{5} = -1, \qquad z_2 = \frac{255 - 250}{5} = 1$$

$$P(245 \le X \le 255) = P(-1 \le Z \le 1) = 2\Phi(1) - 1$$

- We use $\Phi(1.2) = 0.8849$; however, here we need $\Phi(1)$. The value $z=1$ is not given directly, so we note that from the empirical rule $P(\mu \pm \sigma) \approx 0.6826$.

$$P(245 \le X \le 255) \approx \boxed{0.6826}$$

**iii. R command for the 10th percentile**

```r
qnorm(0.10, mean = 250, sd = 5)
```

---

---

## FORMULA SHEET

**Probability and Statistics (405)**

**Mean:**
$\bar{X} = \frac{1}{n} \sum_{i=1}^n X_i$, $\bar{X} = \frac{1}{n} \sum_{i=1}^k X_i f_i$

**Variance:**
$s^2 = \frac{1}{n-1} \sum_{i=1}^n (x_i - \bar{x})^2$, $s^2 = \frac{1}{n-1} \sum_{i=1}^k (X_i - \bar{X})^2 \cdot f_i$

**Coefficient of variation:** $CV = s / \bar{x}$

If $F_{(i-1)} \le \frac{N}{2} \le F_i$ then the **median** (for grouped data):
$M = x_{(i-1)} + \frac{\delta}{f_i} \left( \frac{N}{2} - F_{(i-1)} \right)$

If $F_{(i-1)} \le \frac{kN}{4} \le F_i$ then $Q_k = x_{(i-1)} + \frac{\delta}{f_i} \left( \frac{kN}{4} - F_{(i-1)} \right), \quad k = 1, 2, 3$

**Mode** (for grouped data):
$T = x_{(i-1)} + \delta \frac{\Delta_1}{\Delta_1 + \Delta_2}$

**Classical definition of probability:**
$P(A) = \frac{N(A)}{N(\Omega)}$,
$N(A)$: number of favorable outcomes for event A
$N(\Omega)$: total number of possible outcomes

**Properties:**
I) $P(A') = 1 - P(A)$, II) $P(\emptyset) = 0$, III) $P(A) \le 1$
IV) $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ .....(Additive Law)
V) If $A_1, A_2, \cdots, A_n$ are $n$ mutually exclusive events of the sample space $\Omega$, then:
$P(A_1 \cup A_2 \cup \cdots \cup A_n) = P(A_1) + P(A_2) + \cdots + P(A_n)$.
VI) If $A \subseteq B$, then a) $P(B - A) = P(B) - P(A)$ and b) $P(A) \le P(B)$

**Conditional Probability:**
$P(A|B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) > 0$

**Multiplication Rule:**
$P(A \cap B) = P(A|B)P(B)$

**Independent Events:**
$P(A \cap B) = P(A)P(B)$

If $A_i \cap A_j = \emptyset, \forall i \neq j$ and $A_1 \cup A_2 \cup \ldots \cup A_n = \Omega$ then:
**Law of Total Probability:**
$P(B) = P(B \cap A_1) + P(B \cap A_2) + \cdots + P(B \cap A_n)$

**Bayes' Theorem:**
$P(A_i | B) = \frac{P(B \cap A_i)}{P(B)} = \frac{P(B|A_i)P(A_i)}{\sum_{k=1}^n P(B|A_k)P(A_k)}$
