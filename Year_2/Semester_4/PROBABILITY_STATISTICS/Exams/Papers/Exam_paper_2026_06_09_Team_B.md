# Exam Paper 2026 06 09 (Team B)

**Team B**
**UNIVERSITY OF IOANNINA**                   Full Name:_______________________
**Department of Computer Science & Telecommunications**    Seat Code:_______________________
**COURSE: Probability & Statistics**       Tuesday 09/06/2026

Instructions:
1. All problems carry equal weight
2. Hand in the question sheet along with your answer booklet.
3. Use of pocket calculators is permitted; mobile phones are prohibited.

**PROBLEM 1:** The following table shows the time (in minutes) taken by 200 users to complete an online purchase.

| Time (minutes) | Class Marks $x_i$ | Number of Users $f_i$ | $f_i x_i$ | $f_i (x_i - \bar{x})^2$ | $F_i$ |
| --- | --- | --- | --- | --- | --- |
| [0,4) | | 30 | | 1228.8 | |
| [4,8) | | 60 | | 345.6 | |
| [8,12) | | 70 | | 179.2 | |
| [12,16) | | 40 | | 1254.4 | |
| Total | | 200 | | 3008 | |

i. Using the table, calculate the mean ($\bar{x}$), third quartile ($Q_3$), and standard deviation of completion time.
ii. If the company wants to improve its platform for the 25% of users with the longest delays, what is the minimum threshold time (in minutes) above which a user is considered part of this group?
iii. Within what interval of values is the completion time expected to lie for 95% of users, assuming the distribution of times is approximately symmetric/bell-shaped?
iv. If the original raw un-grouped data are stored in an R vector named `times`, write the command to calculate the standard deviation.

**PROBLEM 2:** A survey among department students revealed that: 20% use R software, 15% use Python, and 5% use both.
A student is selected at random. Calculate the probabilities:
a) that they use at least one of the two software packages.
b) that they use only Python.
c) that they use Python given that they do not use R.
d) that they use neither of the two.

**PROBLEM 3:** In a telecommunications company, daily quality checks are performed on 20 randomly selected connections. A connection is classified as faulty or non-faulty. From prior measurements it is known that the probability a connection is faulty is 0.08.
Let $X$ be the number of faulty connections found in 20 daily checks.
a) Describe the type of random variable $X$. Which theoretical distribution do you consider most suitable for modeling $X$? Justify your choice.
b) Calculate the probability of finding at most 2 faulty connections.
c) Calculate the probability of finding at least one faulty connection.
d) Calculate the expected value and standard deviation of $X$.
e) What command should we give in R to calculate the probability of question c)?

**PROBLEM 4:** The lifespan of a specific electronic tube manufactured in a factory follows a Normal distribution with mean 800 hours and standard deviation 40 hours. We randomly select a tube.
i. What is the probability that the tube lifespan is between 740 and 860 hours?
ii. What is the probability that the tube operates for more than 720 hours?
iii. Write the appropriate command in R that calculates the probability of question i).
Given: $P(Z \le 1.5) = 0.9332$, $P(Z \le 2) = 0.9772$

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
