# Exam Paper 2024 06 14 (Team C)

**Team C**
**UNIVERSITY OF IOANNINA**                   Full Name:_______________________
**Department of Computer Science & Telecommunications**    Student ID:________________________________
**COURSE: Probability & Statistics**       Friday 14/06/2024

Instructions:
1. Write your full name on the exam sheet.
2. All problems carry equal weight
3. Hand in the question sheet along with your answer booklet.
4. Use of pocket calculators is permitted; mobile phones are prohibited

**PROBLEM 1:** In a manufacturing industry, 1% of a product is non-compliant (defective). We randomly select 7 units of this product for inspection. What is the probability that:
a. exactly one product unit is defective
b. 2 or more units are defective
c. What command should we give in R to calculate the probability of question a)?

**PROBLEM 2:** In a survey conducted in a region regarding readership of various Sunday newspapers, 25% stated they read "Ta Nea", 35% "To Vima", and 5% stated they read both newspapers. A person is selected at random. Calculate the probability that they:
A. read at least one of the two newspapers
B. read neither of the two newspapers
C. read only "Ta Nea"
D. read "Ta Nea", given that they read "To Vima"

**PROBLEM 3:** The service time required for bank customers at the teller follows a Normal distribution with mean $\mu=10$ min and standard deviation $\sigma=2$ min. What is the probability that a customer waits:
i) more than 7 min
ii) between 9 and 13 min
iii) what command should we give in R to calculate the probability of question ii)?

Given: $\Phi(0.5) = P(Z \le 0.5) = 0.69146$, $\Phi(1.5) = P(Z \le 1.5) = 0.93319$

**PROBLEM 4:** The monthly salary of employees in a company is given in the following table:

| Monthly Salary | Number of Employees | $f_i x_i$ | $f_i(x_i - \bar{x})^2$ | $F_i$ |
| --- | --- | --- | --- | --- |
| 1250 | 22 | | 2217737.5 | |
| 1300 | 35 | | 2504468.75 | |
| 1550 | 65 | | 19906.25 | |
| 1800 | 38 | | 2054137.5 | |
| 2000 | 20 | | 3741125 | |
| Total | 180 | | 10537375 | |

A. Calculate the mean monthly salary, the first quartile, and the standard deviation.
B. What percentage of employees have a salary of at most 1300 €?
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
