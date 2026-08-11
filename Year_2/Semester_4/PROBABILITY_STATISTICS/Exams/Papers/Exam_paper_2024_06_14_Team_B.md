# Exam Paper 2024 06 14 (Team B)

**Team B**
**UNIVERSITY OF IOANNINA**                   Full Name:_______________________
**Department of Computer Science & Telecommunications**    Student ID:________________________________
**COURSE: Probability & Statistics**       Friday 14/06/2024

Instructions:
1. Write your full name on the exam sheet.
2. All problems carry equal weight
3. Hand in the question sheet along with your answer booklet.
4. Use of pocket calculators is permitted; mobile phones are prohibited

**PROBLEM 1:** The times (in minutes) required by 120 workers in a factory to perform a task are given in the following table after grouping:

| Times (in min) | Class Marks $x_i$ | Number of Workers $f_i$ | $f_i x_i$ | $f_i(x_i - \bar{x})^2$ | $F_i$ |
| --- | --- | --- | --- | --- | --- |
| [20, 25) | | 10 | | 1050.625 | |
| [25, 30) | | 22 | | 606.375 | |
| [30, 35) | | 50 | | 3.125 | |
| [35, 40) | | 28 | | 631.75 | |
| [40, 45) | | 10 | | 950.625 | |
| Total | | 120 | | 3242.5 | |

a. Using the table, calculate the mean time ($\bar{x}$) for task completion, the 1st quartile ($Q_1$), and the standard deviation.
b. Within what interval does the task completion time range for 68% of workers?
c. Management decided to give a bonus to the 25% of workers with the shortest completion time. What is the maximum completion time a worker can have to receive the bonus?
d. What commands should we give in R to calculate the mean of our data?

**PROBLEM 2:** In a manufacturing industry, 2% of a product is non-compliant (defective). We randomly select 6 units of this product for inspection. What is the probability that:
i) exactly one product unit is defective
ii) 2 or more units are defective
iii) What command should we give in R to calculate the probability of question i)?

**PROBLEM 3:** A study in a company revealed that 60% of employees know English, while 75% of employees are computer literate (PC). Finally, 55% know both English and PC. We select an employee at random; find the probabilities of the following events:
A. The employee possesses at least one of the above qualifications (English or PC).
B. The employee possesses only PC skills.
C. The employee possesses neither of the two qualifications.
D. Given that the employee knows English, what is the probability that they know PC?

**PROBLEM 4:** A factory manufactures electric refrigerators for which the time until the first failure follows a Normal distribution with mean $\mu=15$ years and standard deviation $\sigma=4$ years. What is the probability for an electric refrigerator that:
i. the first failure occurs after 9 years
ii. the first failure occurs between 13 and 17 years
iii. what command should we give in R to calculate the probability of question ii)?
Given: $\Phi(0.5) = P(Z \le 0.5) = 0.69146$, $\Phi(1.5) = P(Z \le 1.5) = 0.93319$.

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
