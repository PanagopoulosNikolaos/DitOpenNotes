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
