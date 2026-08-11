# Exam Paper 2026 06 09 (Team A)

**Team A**
**UNIVERSITY OF IOANNINA**                   Full Name:_______________________
**Department of Computer Science & Telecommunications**    Seat Code:_______________________
**COURSE: Probability & Statistics**       Tuesday 09/06/2025

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

Good Luck!

---

## FORMULA SHEET

**Probability and Statistics (405)**

**Mean:**
$ar{X} = rac{1}{n} \sum_{i=1}^n X_i$, $ar{X} = rac{1}{n} \sum_{i=1}^k X_i f_i$

**Variance:**
^2 = rac{1}{n-1} \sum_{i=1}^n (x_i - ar{x})^2$, ^2 = rac{1}{n-1} \sum_{i=1}^k (X_i - ar{X})^2 \cdot f_i$

**Coefficient of variation:**  = s / ar{x}$

If {(i-1)} \le rac{N}{2} \le F_i$ then the **median** (for grouped data):
 = x_{(i-1)} + rac{\delta}{f_i} \left( rac{N}{2} - F_{(i-1)} 
ight)$

If {(i-1)} \le rac{kN}{4} \le F_i$ then  = x_{(i-1)} + rac{\delta}{f_i} \left( rac{kN}{4} - F_{(i-1)} 
ight), \quad k = 1, 2, 3$

**Mode** (for grouped data):
 = x_{(i-1)} + \delta rac{\Delta_1}{\Delta_1 + \Delta_2}$

**Classical definition of probability:**
(A) = rac{N(A)}{N(\Omega)}$,
(A)$: number of favorable outcomes for event A
(\Omega)$: total number of possible outcomes

**Properties:**
I) (A') = 1 - P(A)$, II) (\emptyset) = 0$, III) (A) \le 1$
IV) (A \cup B) = P(A) + P(B) - P(A \cap B)$ .....(Additive Law)
V) If , A_2, \cdots, A_n$ are $ mutually exclusive events of the sample space $\Omega$, then:
(A_1 \cup A_2 \cup \cdots \cup A_n) = P(A_1) + P(A_2) + \cdots + P(A_n)$.
VI) If  \subseteq B$, then a) (B - A) = P(B) - P(A)$ and b) (A) \le P(B)$

**Conditional Probability:**
(A|B) = rac{P(A \cap B)}{P(B)}, \quad P(B) > 0$

**Multiplication Rule:**
(A \cap B) = P(A|B)P(B)$

**Independent Events:**
(A \cap B) = P(A)P(B)$

If  \cap A_j = \emptyset, orall i 
eq j$ and  \cup A_2 \cup \ldots \cup A_n = \Omega$ then:
**Law of Total Probability:**
(B) = P(B \cap A_1) + P(B \cap A_2) + \cdots + P(B \cap A_n)$

**Bayes' Theorem:**
(A_i | B) = rac{P(B \cap A_i)}{P(B)} = rac{P(B|A_i)P(A_i)}{\sum_{k=1}^n P(B|A_k)P(A_k)}$
