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
