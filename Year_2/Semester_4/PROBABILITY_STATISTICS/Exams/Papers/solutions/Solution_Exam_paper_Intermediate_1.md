# Exam Paper Intermediate 1

**Level: Intermediate 1**
**UNIVERSITY OF IOANNINA**                   Full Name:_______________________
**Department of Computer Science & Telecommunications**    Student ID:________________________________
**COURSE: Probability & Statistics**          

Instructions:
1. Write your full name on the exam sheet.
2. All problems carry equal weight.
3. Hand in the question sheet along with your answer booklet.
4. Use of pocket calculators is permitted; mobile phones are prohibited.

**PROBLEM 1:** The weekly study hours of 80 students for a difficult course are given in the following table after grouping:

| Study Hours | Class Marks $x_i$ | Number of Students $f_i$ | $f_i x_i$ | $f_i(x_i - \bar{x})^2$ | $F_i$ |
| --- | --- | --- | --- | --- | --- |
| [5, 10) | | 12 | | | |
| [10, 15) | | 20 | | | |
| [15, 20) | | 30 | | | |
| [20, 25) | | 18 | | | |
| Total | | 80 | | | |

a. Fill in the blanks of the table and calculate the mean ($\bar{x}$) of study hours and the median ($M$).
b. Calculate the standard deviation ($s$).
c. Which commands should we give in R to calculate the first quartile ($Q_1$)?

**PROBLEM 2:** In a production line, 5% of components are defective. We randomly select 8 components. What is the probability:
i) Exactly 2 components are defective?
ii) At most 1 component is defective?
iii) What R command calculates the probability of question ii)?

**PROBLEM 3:** In a factory, three machines $M_1, M_2, M_3$ produce 40%, 35%, and 25% of total production respectively. Defect rates for each machine are 2%, 3%, and 4% respectively. We randomly select a product from the warehouse.
A. What is the probability that the product is defective?
B. If the selected product is defective, what is the probability it was produced by machine $M_1$?

**PROBLEM 4:** Patient waiting time in a hospital emergency room follows a Normal distribution with mean $\mu = 45$ minutes and standard deviation $\sigma = 10$ minutes.
i. What is the probability a patient waits more than 55 minutes?
ii. What is the probability a patient waits between 35 and 65 minutes?
iii. What R command do we give to find the probability a patient waits less than 30 minutes?
Given: $\Phi(1) = P(Z \le 1) = 0.8413$, $\Phi(2) = P(Z \le 2) = 0.9772$.

### Solution to Problem 1

**Table Completion:**

| Hours | $x_i$ | $f_i$ | $f_i x_i$ | $F_i$ |
|---|---|---|---|---|
| [5, 10)  | 7.5  | 12 | 90   | 12 |
| [10, 15) | 12.5 | 20 | 250  | 32 |
| [15, 20) | 17.5 | 30 | 525  | 62 |
| [20, 25) | 22.5 | 18 | 405  | 80 |
| Total    |      | 80 | 1270 |    |

**a. Mean $\bar{x}$**

$$\bar{x} = \frac{\sum f_i x_i}{n} = \frac{1270}{80} = \boxed{15.875 \text{ hours}}$$

**Standard deviation — completing the column $f_i(x_i-\bar{x})^2$:**

| $x_i$ | $x_i - \bar{x}$ | $(x_i-\bar{x})^2$ | $f_i(x_i-\bar{x})^2$ |
|---|---|---|---|
| 7.5  | -8.375 | 70.14 | 841.68 |
| 12.5 | -3.375 | 11.39 | 227.81 |
| 17.5 | 1.625  | 2.64  | 79.22  |
| 22.5 | 6.625  | 43.89 | 790.03 |
| **Total** | | | **1938.74** |

**b. Standard deviation $s$**

$$s^2 = \frac{\sum f_i(x_i-\bar{x})^2}{n-1} = \frac{1938.74}{79} \approx 24.54$$

$$s = \sqrt{24.54} \approx \boxed{4.95 \text{ hours}}$$

**Median $M_e$**

- $n/2 = 40$. We have $F_2 = 32 < 40 \le 62 = F_3$, so the median lies in the class $[15, 20)$.

$$M_e = L + \left( \frac{\frac{n}{2} - F_{i-1}}{f_i} \right) \cdot w = 15 + \left( \frac{40 - 32}{30} \right) \cdot 5 = 15 + 1.333 \approx \boxed{16.33 \text{ hours}}$$

**c. R commands for $Q_1$**

```r
hours <- c(...)           # data input
quantile(hours, 0.25)     # 1st quartile
```

---

**PROBLEM 2:** In a production line, 5% of components are defective. We randomly select 8 components. What is the probability:
i) Exactly 2 components are defective?
ii) At most 1 component is defective?
iii) What R command calculates the probability of question ii)?

### Solution to Problem 2

**Given Data:** $X \sim B(n=8,\ p=0.05)$

$$P(X=k) = \binom{8}{k}(0.05)^k(0.95)^{8-k}$$

**i. $P(X=2)$**

$$P(X=2) = \binom{8}{2}(0.05)^2(0.95)^6 = 28 \times 0.0025 \times 0.7351 = \boxed{0.0515}$$

- $0.95^6 = 0.7351$ (successive multiplication).

**ii. $P(X \le 1)$**

$$P(X \le 1) = P(X=0) + P(X=1)$$

$$P(X=0) = (0.95)^8 = 0.6634$$

$$P(X=1) = 8 \times 0.05 \times (0.95)^7 = 8 \times 0.05 \times 0.6983 = 0.2793$$

$$P(X \le 1) = 0.6634 + 0.2793 = \boxed{0.9427}$$

**iii) R command for question ii)**

```r
pbinom(1, size = 8, prob = 0.05)
```

---

**PROBLEM 3:** In a factory, three machines $M_1, M_2, M_3$ produce 40%, 35%, and 25% of total production respectively. The defect rates of the products produced by each machine are 2%, 3%, and 4% respectively. We randomly select a product from the warehouse.
A. What is the probability that the product is defective?
B. If the selected product is defective, what is the probability it was produced by machine $M_1$?

### Solution to Problem 3

**Given Data:**

| Machine | $P(M_i)$ | $P(E \mid M_i)$ |
|---|---|---|
| $M_1$ | 0.40 | 0.02 |
| $M_2$ | 0.35 | 0.03 |
| $M_3$ | 0.25 | 0.04 |

**A. $P(E)$ — Total Probability**

$$P(E) = P(E|M_1)P(M_1) + P(E|M_2)P(M_2) + P(E|M_3)P(M_3)$$

$$= 0.02 \times 0.40 + 0.03 \times 0.35 + 0.04 \times 0.25$$

$$= 0.008 + 0.0105 + 0.01 = \boxed{0.0285}$$

**B. $P(M_1 | E)$ — Bayes' Theorem**

$$P(M_1 \mid E) = \frac{P(E|M_1) \cdot P(M_1)}{P(E)} = \frac{0.02 \times 0.40}{0.0285} = \frac{0.008}{0.0285} \approx \boxed{0.2807}$$

- Bayes' theorem reverses the causal direction: given the effect (defective), it computes the probability of the cause (which machine).

---

**PROBLEM 4:** The waiting time of patients in the emergency room of a hospital follows the Normal distribution with mean $\mu = 45$ minutes and standard deviation $\sigma = 10$ minutes.
i. What is the probability that a patient waits more than 55 minutes?
ii. What is the probability that a patient waits between 35 and 65 minutes?
iii. What command do we give in R to find the probability that a patient waits less than 30 minutes?
Given: $\Phi(1) = P(Z \le 1) = 0.8413$, $\Phi(2) = P(Z \le 2) = 0.9772$.

### Solution to Problem 4

**Given Data:** $X \sim N(\mu=45,\ \sigma=10)$

**i. $P(X > 55)$**

$$z = \frac{55 - 45}{10} = 1$$

$$P(X > 55) = 1 - P(Z \le 1) = 1 - 0.8413 = \boxed{0.1587}$$

**ii. $P(35 \le X \le 65)$**

$$z_1 = \frac{35 - 45}{10} = -1, \qquad z_2 = \frac{65 - 45}{10} = 2$$

$$P(35 \le X \le 65) = P(-1 \le Z \le 2) = P(Z \le 2) - P(Z \le -1)$$

$$= \Phi(2) - [1 - \Phi(1)] = 0.9772 - (1 - 0.8413) = 0.9772 - 0.1587 = \boxed{0.8185}$$

**iii. R command for $P(X < 30)$**

```r
pnorm(30, mean = 45, sd = 10)
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
