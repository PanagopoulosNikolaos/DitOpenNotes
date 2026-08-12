# Exam Paper 2024 09 06 (Team A)

**Team A**
**UNIVERSITY OF IOANNINA**                   Full Name:_______________________
**Department of Computer Science & Telecommunications**    Student ID:________________________________
**COURSE: Probability & Statistics**       Friday 06/09/2024

Instructions:
1. Write your full name on the exam sheet.
2. All problems carry equal weight
3. Hand in the question sheet along with your answer booklet.
4. Use of pocket calculators is permitted; mobile phones are prohibited

**PROBLEM 1:** If $P(A) = a, P(B) = 0.4$, and $P(A \cup B) = 0.6$, find $\alpha$ if:
i. events A and B are mutually exclusive (disjoint)
ii. events A and B are independent
iii. $B \subset A$

**PROBLEM 2:** The time required for a student to prepare for the Statistics exam in September was found to approximately follow a Normal distribution with mean $\mu=25$ hours and standard deviation $\sigma=5$ hours.
A. Calculate the percentage of students who spend more than 15 hours on review.
B. Calculate the percentage of students who spend between 20 and 25 hours on review.
C. What command should we give in R to calculate the probability of question B)?
Given: $P(Z \le 1) = 0.8413$, $P(Z \le 2) = 0.9772$.

**PROBLEM 3:** The heights of 11 students in a class are (in cm):
160, 162, 168, 168, 170, 173, 175, 178, 182, 185, 186.
i. Calculate: the mean height ($\bar{x}$) of students, the 3rd quartile ($Q_3$), and standard deviation ($s$).
ii. School management decided that the top 25% of students in the class with the greatest height will participate in the parade. What minimum height must a student have to participate in the parade?
iii. What commands should we give in R to calculate the mode of our data?

**PROBLEM 4:** A pharmaceutical laboratory reports that a medication causes adverse side effects in 3 out of 100 patients. To verify this hypothesis, another laboratory randomly selects 5 individuals who consumed the drug.
i. Find the probability that at least two patients experienced side effects.
ii. What is the expected number of patients the laboratory should expect to experience side effects if 100 patients are selected at random?
iii. What command should we give in R to calculate the probability of question i)?

### Solution to Problem 1

The Additive Law in general: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$

**i. A, B disjoint ($A \cap B = \emptyset$)**

$$P(A \cap B) = 0$$

$$P(A \cup B) = P(A) + P(B) \Rightarrow 0.6 = a + 0.4$$

$$a = \boxed{0.2}$$

- For disjoint events the intersection is empty, so the additive law is simplified.

**ii. A, B independent**

$$P(A \cap B) = P(A) \cdot P(B) = a \cdot 0.4$$

$$0.6 = a + 0.4 - 0.4a \Rightarrow 0.6 - 0.4 = a - 0.4a$$

$$0.2 = 0.6a \Rightarrow a = \frac{0.2}{0.6} = \boxed{\frac{1}{3} \approx 0.333}$$

- We substitute $P(A \cap B) = 0.4a$ into the additive law and solve for $a$.

**iii. $B \subset A$ (B is contained in A)**

When $B \subseteq A$: $A \cup B = A$ and $A \cap B = B$.

$$P(A \cup B) = P(A) \Rightarrow 0.6 = a$$

$$a = \boxed{0.6}$$

- Since B is a subset of A, their union coincides with A.

---

**PROBLEM 2:** The time required for a student to prepare for the Statistics course for the September exams was found to approximately follow the normal distribution with mean $\mu=25$ hours and standard deviation $\sigma=5$ hours.
A. Calculate the percentage of students who spend more than 15 hours on review.
B. Calculate the percentage of students who spend between 20 and 25 hours on review.
C. What command should we give in R to calculate the probability of question B)?
Given: $P(Z \le 1) = 0.8413$, $P(Z \le 2) = 0.9772$.

### Solution to Problem 2

**Given Data:** $X \sim N(\mu=25,\ \sigma=5)$

**A. $P(X > 15)$**

$$z = \frac{15 - 25}{5} = \frac{-10}{5} = -2$$

$$P(X > 15) = P(Z > -2) = P(Z \le 2) = 0.9772 = \boxed{97.72\%}$$

**B. $P(20 \le X \le 25)$**

$$z_1 = \frac{20 - 25}{5} = -1, \qquad z_2 = \frac{25 - 25}{5} = 0$$

$$P(20 \le X \le 25) = P(-1 \le Z \le 0) = P(Z \le 0) - P(Z \le -1)$$

$$= 0.5 - [1 - P(Z \le 1)] = 0.5 - (1 - 0.8413) = 0.5 - 0.1587 = \boxed{0.3413 = 34.13\%}$$

- It is used that $P(Z \le 0) = 0.5$ due to symmetry and $P(Z \le -1) = 1 - P(Z \le 1)$.

**C. R command for question B**

```r
pnorm(25, mean = 25, sd = 5) - pnorm(20, mean = 25, sd = 5)
```

---

**PROBLEM 3:** The heights of 11 students in a class are (in cm):
160, 162, 168, 168, 170, 173, 175, 178, 182, 185, 186.
i. Calculate: the mean height ($\bar{x}$) of the students, the 3rd quartile ($Q_3$), and the standard deviation ($s$).
ii. The management decided that the 25% of the students of the class with the greatest height will take part in the parade. What height must a student have to take part in the parade?
iii. What commands should we give in R to calculate the mode of our data?

### Solution to Problem 3

**Data (sorted):** 160, 162, 168, 168, 170, 173, 175, 178, 182, 185, 186 — $n=11$

**i. Mean $\bar{x}$**

$$\bar{x} = \frac{160+162+168+168+170+173+175+178+182+185+186}{11} = \frac{1907}{11} = \boxed{173.36 \text{ cm}}$$

**3rd quartile $Q_3$**

Position of $Q_3$: $\frac{3(n+1)}{4} = \frac{3 \times 12}{4} = 9$th position.

$$Q_3 = x_{(9)} = \boxed{182 \text{ cm}}$$

**Standard Deviation $s$**

$$s^2 = \frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2$$

| $x_i$ | $x_i - \bar{x}$ | $(x_i-\bar{x})^2$ |
|---|---|---|
| 160 | -13.36 | 178.49 |
| 162 | -11.36 | 129.05 |
| 168 | -5.36  | 28.73  |
| 168 | -5.36  | 28.73  |
| 170 | -3.36  | 11.29  |
| 173 | -0.36  | 0.13   |
| 175 | 1.64   | 2.69   |
| 178 | 4.64   | 21.53  |
| 182 | 8.64   | 74.65  |
| 185 | 11.64  | 135.49 |
| 186 | 12.64  | 159.77 |
| **Total** | | **770.55** |

$$s^2 = \frac{770.55}{10} = 77.055, \qquad s = \sqrt{77.055} \approx \boxed{8.78 \text{ cm}}$$

**ii. Height for participation in the parade**

The top 25% corresponds to heights above $Q_3$:

$$\text{Cutoff} = Q_3 = \boxed{182 \text{ cm}}$$

**iii. R commands for the mode**

```r
heights <- c(160, 162, 168, 168, 170, 173, 175, 178, 182, 185, 186)
names(which.max(table(heights)))
```

---

**PROBLEM 4:** A pharmaceutical laboratory reports that a medication causes adverse side effects in 3 out of 100 patients. To verify this hypothesis, another laboratory randomly selects 5 individuals who have consumed the medication.
i. Find the probability that at least two patients experienced side effects.
ii. What is the expected number of patients that the laboratory should expect to experience side effects if it selects 100 patients at random?
iii. What command should we give in R to calculate the probability of question i)?

### Solution to Problem 4

**Given Data:** $X \sim B(n=5,\ p=0.03)$

**i. $P(X \ge 2)$**

$$P(X \ge 2) = 1 - P(X=0) - P(X=1)$$

$$P(X=0) = (0.97)^5 = 0.8587$$

$$P(X=1) = \binom{5}{1}(0.03)(0.97)^4 = 5 \times 0.03 \times 0.8853 = 0.1328$$

$$P(X \ge 2) = 1 - 0.8587 - 0.1328 = \boxed{0.0085}$$

**ii. Expected number for $n = 100$**

$$E[X] = n \cdot p = 100 \times 0.03 = \boxed{3 \text{ patients}}$$

- The mean of the binomial distribution is given by the formula $\mu = np$.

**iii. R command for question i**

```r
1 - pbinom(1, size = 5, prob = 0.03)
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
