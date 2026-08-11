# Exam Paper Hard 2

**Level: Hard 2**
**UNIVERSITY OF IOANNINA**                   Full Name:_______________________
**Department of Computer Science & Telecommunications**    Student ID:________________________________
**COURSE: Probability & Statistics**          

Instructions:
1. Write your full name on the exam sheet.
2. All problems carry equal weight.
3. Hand in the question sheet along with your answer booklet.
4. Use of pocket calculators is permitted; mobile phones are prohibited.

**PROBLEM 1:** In a survey, the performance of two different class sections A and B of a cohort was studied.
- Section A has $n_1 = 40$ students, with mean score $\bar{x}_1 = 7.5$ and standard deviation $s_1 = 1.2$.
- Section B has $n_2 = 60$ students, with mean score $\bar{x}_2 = 6.5$ and standard deviation $s_2 = 1.5$.
a. Calculate the overall mean score ($\bar{x}$) of all students in both sections combined.
b. Calculate the combined variance ($s^2$) and combined standard deviation ($s$) of the scores for all 100 students.
c. Which R commands are needed to compare the score distributions of the two sections using boxplots?

**PROBLEM 2:** In a game, we roll a fair die. If a 6 turns up, we win. We play the game 10 times (independent trials).
i) What is the probability of winning at least 2 times?
ii) If we know that we won at least once, what is the probability that we won exactly 2 times?
iii) Which command in R calculates the probability of question ii)?

**PROBLEM 3:** A digital communication channel transmits binary digital signals (0 and 1). The probability of transmitting digit 0 is 0.45 and the probability of transmitting 1 is 0.55. Due to noise in the channel:
- If 0 is transmitted, the probability of receiving it incorrectly as 1 is 0.10.
- If 1 is transmitted, the probability of receiving it incorrectly as 0 is 0.15.
A. What is the probability of receiving digit 1?
B. If digit 1 is received, what is the probability that 0 was actually transmitted?
C. What is the total probability of error during signal transmission in this channel?

**PROBLEM 4:** A machine fills beverage bottles. The volume of beverage follows a Normal distribution with mean $\mu$ and standard deviation $\sigma$. It is known that 10% of bottles contain more than 334.8 ml, while 5% contain less than 318.5 ml.
i. Find the parameters $\mu$ and $\sigma$ of the distribution.
ii. If the nominal volume is 330 ml, what is the probability that a bottle contains less than the nominal volume?
iii. Which R commands are needed to find the probability of question ii)?
Given: For the standard normal variable $Z$, $P(Z \le 1.282) = 0.90$, $P(Z \le 1.645) = 0.95$, and $\Phi(-0.5) = 0.3085$.

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
