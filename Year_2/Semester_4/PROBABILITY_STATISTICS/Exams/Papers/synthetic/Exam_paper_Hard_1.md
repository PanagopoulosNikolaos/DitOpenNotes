# Exam Paper Hard 1

**Level: Hard 1**
**UNIVERSITY OF IOANNINA**                   Full Name:_______________________
**Department of Computer Science & Telecommunications**    Student ID:________________________________
**COURSE: Probability & Statistics**          

Instructions:
1. Write your full name on the exam sheet.
2. All problems carry equal weight.
3. Hand in the question sheet along with your answer booklet.
4. Use of pocket calculators is permitted; mobile phones are prohibited.

**PROBLEM 1:** The following table shows monthly rent values (in €) for 100 apartments in an area. The frequency $f_2$ of the second class is unknown (let it be $x$).

| Rent (€) | Class Marks $x_i$ | Number of Apts $f_i$ | $f_i x_i$ | $f_i(x_i - \bar{x})^2$ | $F_i$ |
| --- | --- | --- | --- | --- | --- |
| [300, 400) | | 15 | | | |
| [400, 500) | | $x$ | | | |
| [500, 600) | | 40 | | | |
| [600, 700) | | 20 | | | |
| [700, 800) | | 5 | | | |
| Total | | 100 | | | |

a. Find the unknown frequency $x$ and complete the table columns.
b. Calculate the mean rent ($\bar{x}$), median ($M$), and standard deviation ($s$).
c. Which R commands are required to calculate the mean of these data if we had the original raw un-grouped data in a vector `rent`?

**PROBLEM 2:** A security system has a failure probability of $p=0.08$ on each breach attempt.
i) If 15 independent breach attempts occur, what is the probability that the system fails in at least 3 of them?
ii) How many independent breach attempts must take place at minimum so that the probability of at least one system failure is greater than 99%?
iii) Write the R commands for calculating the probabilities of questions i and ii.

**PROBLEM 3:** In a medical center, 2% of patients examined have a rare condition. A diagnostic test detects the condition with 98% probability (sensitivity), but yields a false positive result in 3% of healthy individuals (specificity of 97%).
A. What is the probability that a random individual tests positive?
B. If an individual tests positive, what is the probability that they actually have the condition?
C. If an individual tests negative, what is the probability that they are healthy?
D. Are the events "individual has condition" and "test is positive" independent? Justify your answer.

**PROBLEM 4:** The weight of coffee packages produced by a machine follows a Normal distribution with mean $\mu = 250$ grams and standard deviation $\sigma$ grams.
i. If it is known that 5% of packages weigh less than 241.8 grams, calculate the standard deviation $\sigma$.
ii. With the standard deviation found, what is the probability that a package weighs between 245 and 255 grams?
iii. Which R command finds the weight below which 10% of packages fall?
Given: For the standard normal variable $Z$, $\Phi(1.645) = P(Z \le 1.645) = 0.95$ and $\Phi(1.2) = 0.8849$.

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
