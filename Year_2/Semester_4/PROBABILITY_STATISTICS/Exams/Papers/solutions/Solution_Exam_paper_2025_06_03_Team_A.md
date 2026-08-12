# Exam Paper 2025 06 03 (Team A)

**Team A**
**UNIVERSITY OF IOANNINA**                   Full Name:_______________________
**Department of Computer Science & Telecommunications**    Seat Code:_______________________
**COURSE: Probability & Statistics**       Tuesday 03/06/2025

Instructions:
1. All problems carry equal weight
2. Hand in the question sheet along with your answer booklet.
3. Use of pocket calculators is permitted; mobile phones are prohibited

**PROBLEM 1:** In a manufacturing industry, 2% of a product is non-compliant (defective). We randomly select 6 units of this product for inspection. What is the probability that:
a. exactly one product unit is defective
b. 2 or more units are defective
c. What command should we give in R to calculate the probability of question a)?

**PROBLEM 2:** In a survey conducted in a region regarding readership of various Sunday newspapers, 40% stated they read "Ta Nea", 25% "To Vima", and 10% stated they read both newspapers. A person is selected at random. Calculate the probability that they:
A. read at least one of the two newspapers
B. read neither of the two newspapers
C. read only "Ta Nea"
D. read "Ta Nea", given that they read "To Vima"

**PROBLEM 3:** The service time required for bank customers at the teller follows a Normal distribution with mean $\mu=12$ min and standard deviation $\sigma=2$ min. What is the probability that a customer waits:
i) more than 9 min
ii) between 11 and 15 min
iii) what command should we give in R to calculate the probability of question ii)?

Given: $\Phi(0.5) = P(Z \le 0.5) = 0.69146$, $\Phi(1.5) = P(Z \le 1.5) = 0.93319$

**PROBLEM 4:** The monthly salary of employees in a company is given in the following table:

| Monthly Salary | Number of Employees $f_i$ | $f_i x_i$ | $f_i(x_i - \bar{x})^2$ | $F_i$ |
| --- | --- | --- | --- | --- |
| 1250 | 25 | | 2673225 | |
| 1300 | 40 | | 3069160 | |
| 1550 | 65 | | 47385 | |
| 1800 | 43 | | 2138347 | |
| 2000 | 27 | | 4831083 | |
| Total | 200 | | 12759200 | |

A. Calculate the mean monthly salary, the first quartile, and the standard deviation.
B. What percentage of employees have a salary of at most 1550 €?
C. Company management decided to grant an allowance to the 25% of employees with the lowest monthly salary. What maximum salary must an employee have to receive the allowance?
D. What commands should we give in R to calculate the mode of our data?

### Solution to Problem 1

**Given Data:** $X \sim B(n=6,\ p=0.02)$

$$P(X=k) = \binom{6}{k}(0.02)^k(0.98)^{6-k}$$

**a. $P(X=1)$**

$$P(X=1) = \binom{6}{1}(0.02)^1(0.98)^5 = 6 \times 0.02 \times 0.9039 = \boxed{0.1085}$$

- $0.98^5 = 0.9039$ (successive multiplication).

**b. $P(X \ge 2)$**

$$P(X \ge 2) = 1 - P(X=0) - P(X=1)$$

$$P(X=0) = (0.98)^6 = 0.8858$$

$$P(X \ge 2) = 1 - 0.8858 - 0.1085 = \boxed{0.0057}$$

**c. R command for question a**

```r
dbinom(1, size = 6, prob = 0.02)
```

---

**PROBLEM 2:** In a survey conducted in a region regarding readership of various Sunday newspapers, 40% stated they read "Ta Nea", 25% "To Vima", and 10% stated they read both newspapers. We select a person at random. Calculate the probability that:
A. they read at least one of the two newspapers
B. they read neither of the two newspapers
C. they read only "Ta Nea"
D. they read "Ta Nea", given that they read "To Vima"

### Solution to Problem 2

**Given Data:**
- $P(N) = 0.40$ (Ta Nea)
- $P(B) = 0.25$ (To Vima)
- $P(N \cap B) = 0.10$

**A. $P(N \cup B)$ — at least one newspaper**

$$P(N \cup B) = P(N) + P(B) - P(N \cap B) = 0.40 + 0.25 - 0.10 = \boxed{0.55}$$

**B. $P((N \cup B)')$ — neither newspaper**

$$P((N \cup B)') = 1 - 0.55 = \boxed{0.45}$$

**C. $P(N \cap B')$ — only Ta Nea**

$$P(N \cap B') = P(N) - P(N \cap B) = 0.40 - 0.10 = \boxed{0.30}$$

**D. $P(N | B)$ — Ta Nea given To Vima**

$$P(N \mid B) = \frac{P(N \cap B)}{P(B)} = \frac{0.10}{0.25} = \boxed{0.40}$$

---

**PROBLEM 3:** The time required for bank customers to be served at the teller follows the Normal distribution with mean $\mu=12$ min and standard deviation $\sigma=2$ min. What is the probability that a customer waits:
i) more than 9 min
ii) between 11 and 15 min
iii) what command should we give in R to calculate the probability of question ii)?

Given: $\Phi(0.5) = P(Z \le 0.5) = 0.69146$, $\Phi(1.5) = P(Z \le 1.5) = 0.93319$

### Solution to Problem 3

**Given Data:** $X \sim N(\mu=12,\ \sigma=2)$

**i. $P(X > 9)$**

$$z = \frac{9 - 12}{2} = -1.5$$

$$P(X > 9) = P(Z > -1.5) = P(Z \le 1.5) = \boxed{0.93319}$$

**ii. $P(11 \le X \le 15)$**

$$z_1 = \frac{11 - 12}{2} = -0.5, \qquad z_2 = \frac{15 - 12}{2} = 1.5$$

$$P(11 \le X \le 15) = P(-0.5 \le Z \le 1.5) = \Phi(1.5) - [1 - \Phi(0.5)]$$

$$= 0.93319 - (1 - 0.69146) = 0.93319 - 0.30854 = \boxed{0.62465}$$

- We subtract the left tail $P(Z \le -0.5)$, which equals $1 - \Phi(0.5)$ due to symmetry.

**iii) R command for question ii)**

```r
pnorm(15, mean = 12, sd = 2) - pnorm(11, mean = 12, sd = 2)
```

---

**PROBLEM 4:** The monthly salary of employees in a company is given in the following table:

| Monthly Salary | Number of Employees $f_i$ | $f_i x_i$ | $f_i(x_i - \bar{x})^2$ | $F_i$ |
| --- | --- | --- | --- | --- |
| 1250 | 25 | | 2673225 | |
| 1300 | 40 | | 3069160 | |
| 1550 | 65 | | 47385 | |
| 1800 | 43 | | 2138347 | |
| 2000 | 27 | | 4831083 | |
| Total | 200 | | 12759200 | |

A. Calculate the mean monthly salary, the first quartile, and the standard deviation.
B. What percentage of employees have a salary of at most 1550 €?
C. The company management decided to grant an allowance to the 25% of employees with the lowest monthly salary. What salary must an employee have to receive the allowance?
D. What commands should we give in R to calculate the mode of our data?

### Solution to Problem 4

**Table Completion:**

| $x_i$ | $f_i$ | $f_i x_i$ | $F_i$ |
|---|---|---|---|
| 1250 | 25  | 31250  | 25  |
| 1300 | 40  | 52000  | 65  |
| 1550 | 65  | 100750 | 130 |
| 1800 | 43  | 77400  | 173 |
| 2000 | 27  | 54000  | 200 |
| Tot. | 200 | 315400 |     |

**A. Mean $\bar{x}$**

$$\bar{x} = \frac{\sum f_i x_i}{n} = \frac{315400}{200} = \boxed{1577 \text{ €}}$$

**Standard Deviation $s$**

$$s^2 = \frac{\sum f_i(x_i - \bar{x})^2}{n-1} = \frac{12759200}{199} \approx 64116.08$$

$$s = \sqrt{64116.08} \approx \boxed{253.21 \text{ €}}$$

**First quartile $Q_1$**

- $\frac{n}{4} = 50$. We have $F_1 = 25 < 50 \le 65 = F_2$, so $Q_1$ lies in the second category with $x=1300$ €.

$$Q_1 = \boxed{1300 \text{ €}}$$

**B. Percentage with salary $\le 1550$ €**

$$\text{Percentage} = \frac{F_3}{n} = \frac{130}{200} = 0.65 = \boxed{65\%}$$

**C. Allowance cutoff**

The 25% with the lowest salary lie below $Q_1$:

$$\text{Cutoff} = Q_1 = \boxed{1300 \text{ €}}$$

**D. R commands for the mode**

```r
salaries <- c(...)
names(which.max(table(salaries)))
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
