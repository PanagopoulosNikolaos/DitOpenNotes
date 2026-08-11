# Exam Paper Intermediate 2

**Level: Intermediate 2**
**UNIVERSITY OF IOANNINA**                   Full Name:_______________________
**Department of Computer Science & Telecommunications**    Student ID:________________________________
**COURSE: Probability & Statistics**          

Instructions:
1. Write your full name on the exam sheet.
2. All problems carry equal weight.
3. Hand in the question sheet along with your answer booklet.
4. Use of pocket calculators is permitted; mobile phones are prohibited.

**PROBLEM 1:** Progress test scores of 12 students are:
4, 5, 5, 6, 7, 7, 8, 8, 8, 9, 9, 10.
a. Calculate the mean ($\bar{x}$), 3rd quartile ($Q_3$), and mode ($T$).
b. Calculate the variance ($s^2$) and coefficient of variation ($CV$).
c. Which commands do we give in R to calculate the variance and mean of these data?

**PROBLEM 2:** A software has a 10% probability of encountering an error upon startup. We execute 10 independent software startups.
i) What is the probability an error occurs in exactly 2 startups?
ii) What is the probability an error occurs in at least 2 startups?
iii) Which R command calculates the probability of question ii)?

**PROBLEM 3:** For two events $A$ and $B$ of a sample space $\Omega$, given $P(A) = 0.6$, $P(B) = 0.5$, and $P(A \cap B) = 0.3$.
A. Calculate $P(A \cup B)$ and $P(A \cap B')$.
B. Calculate the conditional probability $P(A' | B')$.
C. Are events $A$ and $B$ independent? Justify your answer.

**PROBLEM 4:** Supermarket queue waiting time follows a Normal distribution with mean $\mu = 8$ minutes and standard deviation $\sigma = 2.5$ minutes.
i. What is the probability a customer waits more than 13 minutes?
ii. What is the probability a customer waits between 5.5 and 10.5 minutes?
iii. Which R command calculates the probability a customer waits at most 6 minutes?
Given: $\Phi(1) = P(Z \le 1) = 0.84134$, $\Phi(2) = P(Z \le 2) = 0.97725$.

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
