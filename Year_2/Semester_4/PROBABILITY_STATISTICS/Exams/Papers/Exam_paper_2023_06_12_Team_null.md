# Exam Paper 2023 06 12 (Team Null)

Instructions:
1. Write your full name on the exam sheet.
2. All problems carry equal weight.
3. Hand in the question sheet along with your answer booklet.
4. Use of pocket calculators is permitted; mobile phones are prohibited.

**PROBLEM 1:** In a survey conducted in a region regarding readership of various Sunday newspapers, 35% stated they read "Kathimerini", 20% "To Vima", and 8% stated they read both newspapers. A person is selected at random. Calculate the probability that they:
A. read at least one of the two newspapers.
B. read only "To Vima"
C. read neither of the two newspapers
D. read "To Vima", given that they read "Kathimerini"

**PROBLEM 2:** A factory produces batteries of a specific type for mobile phone devices. According to factory data, the battery lifespan can be assumed to follow a normal distribution with mean $\mu=48$ hours and standard deviation $\sigma=4$ hours. If a battery is selected at random, calculate the probability that:
i) the lifespan is between 39 and 57 hours
ii) the lifespan exceeds 42 hours
iii) what R command should we give to calculate the probability of question i)?
Given: $P(Z \le 2.25) = 0.98778$, $P(Z \le 1.5) = 0.93319$.

**PROBLEM 3:** The scores (on a scale of 0-100) of 300 candidates participating in a recruitment exam are given in the following table:

| Score | Class Marks $x_i$ | Number of Candidates $f_i$ | $f_i x_i$ | $(x_i - \bar{x})$ | $(x_i - \bar{x})^2$ | $f_i(x_i - \bar{x})^2$ | $F_i$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [0, 20) | | 26 | | -39.8 | 1584.04 | 41185.04 | |
| [20, 40) | | 70 | | -19.8 | 392.04 | 27442.8 | |
| [40, 60) | | 110 | | 0.2 | 0.04 | 4.4 | |
| [60, 80) | | 69 | | 20.2 | 408.04 | 28154.76 | |
| [80, 100] | | 25 | | 40.2 | 1616.04 | 40401 | |
| TOTAL | | 300 | | | | 137188 | |

i. Using the table, calculate the mean score ($\bar{x}$), median, and standard deviation.
ii. What will be the passing threshold if half of the candidates are hired?
iii. Within what interval does the score range for 95% of candidates?
iv. What R command should we give to calculate the median of our data?

**PROBLEM 4:** In a factory hall, 6 machines are installed. The machines operate independently and the probability that any one machine fails during a day is 0.02.
i. Find the probability that exactly 1 machine fails.
ii. Find the probability that at least 2 machines fail.
iii. What R command should we give to calculate the probability of question ii)?

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
