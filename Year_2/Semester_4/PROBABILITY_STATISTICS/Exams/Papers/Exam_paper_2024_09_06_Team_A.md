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
