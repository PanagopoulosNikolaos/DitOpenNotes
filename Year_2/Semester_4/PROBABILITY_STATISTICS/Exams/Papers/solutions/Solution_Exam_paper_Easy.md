# Exam Paper Easy

**Level: Easy**
**UNIVERSITY OF IOANNINA**                   Full Name:_______________________
**Department of Computer Science & Telecommunications**    Student ID:________________________________
**COURSE: Probability & Statistics**          

Instructions:
1. Write your full name on the exam sheet.
2. All problems carry equal weight.
3. Hand in the question sheet along with your answer booklet.
4. Use of pocket calculators is permitted; mobile phones are prohibited.

**PROBLEM 1:** The exam scores of 10 students in a course are: 5, 6, 7, 7, 8, 8, 8, 9, 9, 10.
a. Calculate the mean ($\bar{x}$), median ($M$), mode ($T$), and first quartile ($Q_1$).
b. Calculate the range of scores and the standard deviation ($s$).
c. What command do we give in R to input these data into a vector named `grades` and what command to calculate the median?

**PROBLEM 2:** A diagnostic test for a disease has a 0.10 probability of giving a false positive result in healthy people. We randomly select 5 healthy people and test them.
i) What is the probability that none of them shows a false positive result?
ii) What is the probability that at least one shows a false positive result?
iii) What command should we give in R to calculate the probability of question i)?

**PROBLEM 3:** Let $A$ and $B$ be two events of a sample space $\Omega$ with $P(A) = 0.5$ and $P(B) = 0.4$.
A. If $A$ and $B$ are mutually exclusive (disjoint), calculate the probability $P(A \cup B)$ and $P(A \cap B)$.
B. If $A$ and $B$ are independent events, calculate the probability $P(A \cap B)$, $P(A \cup B)$, and $P(A | B)$.
C. Find $P(A' \cap B')$ in the case where $A$ and $B$ are independent.

**PROBLEM 4:** The weight of apples of a certain variety follows a Normal distribution with mean $\mu = 150$ grams and standard deviation $\sigma = 15$ grams. What is the probability that a randomly selected apple:
i. Weighs less than 165 grams?
ii. Weighs between 135 and 165 grams?
iii. What command should we give in R to calculate the probability of question i)?
Given: $\Phi(1) = P(Z \le 1) = 0.8413$.

### Solution to Problem 1

**Data (sorted):** 5, 6, 7, 7, 8, 8, 8, 9, 9, 10 — $n=10$

**a. Mean $\bar{x}$**

$$\bar{x} = \frac{5+6+7+7+8+8+8+9+9+10}{10} = \frac{77}{10} = \boxed{7.7}$$

**Median $M_e$**

- $n=10$ (even), the median is the average of the values in positions 5 and 6.

$$M_e = \frac{x_{(5)} + x_{(6)}}{2} = \frac{8 + 8}{2} = \boxed{8}$$

**Mode $T$**

- The grade 8 appears 3 times (more than any other).

$$T = \boxed{8}$$

**First quartile $Q_1$**

- Position of $Q_1$: $\frac{n+1}{4} = \frac{11}{4} = 2.75$, i.e., between the 2nd and 3rd values.

$$Q_1 = x_{(2)} + 0.75 \cdot (x_{(3)} - x_{(2)}) = 6 + 0.75(7-6) = 6 + 0.75 = \boxed{6.75}$$

**b. Range**

$$\text{Range} = x_{\max} - x_{\min} = 10 - 5 = \boxed{5}$$

**Standard Deviation $s$**

| $x_i$ | $x_i - \bar{x}$ | $(x_i - \bar{x})^2$ |
|---|---|---|
| 5  | -2.7 | 7.29 |
| 6  | -1.7 | 2.89 |
| 7  | -0.7 | 0.49 |
| 7  | -0.7 | 0.49 |
| 8  | 0.3  | 0.09 |
| 8  | 0.3  | 0.09 |
| 8  | 0.3  | 0.09 |
| 9  | 1.3  | 1.69 |
| 9  | 1.3  | 1.69 |
| 10 | 2.3  | 5.29 |
| **Total** | | **20.10** |

$$s^2 = \frac{20.10}{9} \approx 2.233, \qquad s = \sqrt{2.233} \approx \boxed{1.494}$$

**c. R commands**

```r
grades <- c(5, 6, 7, 7, 8, 8, 8, 9, 9, 10)
median(grades)
```

---

**PROBLEM 2:** A diagnostic test for a disease has a 0.10 probability of giving a false positive result in healthy people. We randomly select 5 healthy people and subject them to the test.
i) What is the probability that none of them shows a false positive result?
ii) What is the probability that at least one shows a false positive result?
iii) What command should we give in R to calculate the probability of question i)?

### Solution to Problem 2

**Given Data:** $X \sim B(n=5,\ p=0.10)$

$$P(X=k) = \binom{5}{k}(0.10)^k(0.90)^{5-k}$$

**i. $P(X=0)$**

$$P(X=0) = (0.90)^5 = \boxed{0.5905}$$

**ii. $P(X \ge 1)$**

$$P(X \ge 1) = 1 - P(X=0) = 1 - 0.5905 = \boxed{0.4095}$$

- The complement rule avoids summing multiple terms.

**iii. R command for question i**

```r
dbinom(0, size = 5, prob = 0.10)
```

---

**PROBLEM 3:** Let $A$ and $B$ be two events of a sample space $\Omega$ with $P(A) = 0.5$ and $P(B) = 0.4$.
A. If $A$ and $B$ are mutually exclusive (disjoint), calculate the probability $P(A \cup B)$ and $P(A \cap B)$.
B. If $A$ and $B$ are independent events, calculate the probability $P(A \cap B)$, $P(A \cup B)$, and $P(A | B)$.
C. Find $P(A' \cap B')$ in the case where $A$ and $B$ are independent.

### Solution to Problem 3

**A. Disjoint events ($A \cap B = \emptyset$)**

$$P(A \cap B) = \boxed{0}$$

$$P(A \cup B) = P(A) + P(B) = 0.5 + 0.4 = \boxed{0.9}$$

- Disjoint events have no common elements, so their intersection is empty.

**B. Independent events**

$$P(A \cap B) = P(A) \cdot P(B) = 0.5 \times 0.4 = \boxed{0.20}$$

$$P(A \cup B) = 0.5 + 0.4 - 0.20 = \boxed{0.70}$$

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)} = \frac{0.20}{0.4} = \boxed{0.50}$$

- For independent events it holds that $P(A|B) = P(A)$, which is confirmed here.

**C. $P(A' \cap B')$ — neither A nor B (independent)**

De Morgan's law is used: $A' \cap B' = (A \cup B)'$

$$P(A' \cap B') = 1 - P(A \cup B) = 1 - 0.70 = \boxed{0.30}$$

Alternatively, since $A$ and $B$ are independent, $A'$ and $B'$ are also independent:

$$P(A' \cap B') = P(A') \cdot P(B') = 0.5 \times 0.6 = 0.30 \checkmark$$

---

**PROBLEM 4:** The weight of apples of a certain variety follows the Normal distribution with mean $\mu = 150$ grams and standard deviation $\sigma = 15$ grams. What is the probability that a randomly selected apple:
i. Weighs less than 165 grams?
ii. Weighs between 135 and 165 grams?
iii. What command should we give in R to calculate the probability of question i)?
Given: $\Phi(1) = P(Z \le 1) = 0.8413$.

### Solution to Problem 4

**Given Data:** $X \sim N(\mu=150,\ \sigma=15)$

**i. $P(X < 165)$**

$$z = \frac{165 - 150}{15} = 1$$

$$P(X < 165) = P(Z \le 1) = \boxed{0.8413}$$

**ii. $P(135 \le X \le 165)$**

$$z_1 = \frac{135 - 150}{15} = -1, \qquad z_2 = \frac{165 - 150}{15} = 1$$

$$P(135 \le X \le 165) = P(-1 \le Z \le 1) = P(Z \le 1) - P(Z \le -1)$$

$$= \Phi(1) - [1 - \Phi(1)] = 2\Phi(1) - 1 = 2(0.8413) - 1 = \boxed{0.6826}$$

- The distribution is symmetric about zero, so $P(Z \le -1) = 1 - \Phi(1)$.

**iii. R command for question i**

```r
pnorm(165, mean = 150, sd = 15)
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
