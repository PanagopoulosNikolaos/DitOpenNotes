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

### Solution to Problem 1

**Given Data:** $n_1=40$, $\bar{x}_1=7.5$, $s_1=1.2$; $n_2=60$, $\bar{x}_2=6.5$, $s_2=1.5$

**a. Overall mean score $\bar{x}$**

The weighted mean is calculated as:

$$\bar{x} = \frac{n_1 \bar{x}_1 + n_2 \bar{x}_2}{n_1 + n_2} = \frac{40 \times 7.5 + 60 \times 6.5}{100} = \frac{300 + 390}{100} = \frac{690}{100} = \boxed{6.90}$$

- The weighted mean is used because the two sections have different numbers of students.

**b. Combined variance $s^2$**

For combining two groups, the following formula is used:

$$s^2 = \frac{(n_1-1)s_1^2 + n_1(\bar{x}_1-\bar{x})^2 + (n_2-1)s_2^2 + n_2(\bar{x}_2-\bar{x})^2}{n_1+n_2-1}$$

- **Within-group variance A:** $(n_1-1)s_1^2 = 39 \times 1.44 = 56.16$
- **Variance of the means A:** $n_1(\bar{x}_1 - \bar{x})^2 = 40 \times (7.5-6.9)^2 = 40 \times 0.36 = 14.40$
- **Within-group variance B:** $(n_2-1)s_2^2 = 59 \times 2.25 = 132.75$
- **Variance of the means B:** $n_2(\bar{x}_2 - \bar{x})^2 = 60 \times (6.5-6.9)^2 = 60 \times 0.16 = 9.60$

$$s^2 = \frac{56.16 + 14.40 + 132.75 + 9.60}{99} = \frac{212.91}{99} \approx \boxed{2.151}$$

$$s = \sqrt{2.151} \approx \boxed{1.467}$$

**c. R commands for boxplots**

```r
scores_A <- c(...)          # grades of section A
scores_B <- c(...)          # grades of section B
all_scores <- c(scores_A, scores_B)
groups <- c(rep("A", 40), rep("B", 60))
boxplot(all_scores ~ groups, xlab = "Section", ylab = "Score")
```

---

**PROBLEM 2:** In a game, we roll a fair die. If a 6 turns up, we win. We play the game 10 times (independent trials).
i) What is the probability of winning at least 2 times?
ii) If we know that we won at least once, what is the probability that we won exactly 2 times?
iii) Which command in R calculates the probability of question ii)?

### Solution to Problem 2

**Given Data:** $X \sim B(n=10,\ p=\frac{1}{6})$

**i. $P(X \ge 2)$**

$$P(X \ge 2) = 1 - P(X=0) - P(X=1)$$

$$P(X=0) = \left(\frac{5}{6}\right)^{10} = \frac{5^{10}}{6^{10}} = \frac{9765625}{60466176} \approx 0.1615$$

$$P(X=1) = \binom{10}{1}\frac{1}{6}\left(\frac{5}{6}\right)^9 = 10 \times \frac{1}{6} \times \frac{5^9}{6^9} \approx 10 \times 0.1667 \times 0.1938 = 0.3230$$

$$P(X \ge 2) = 1 - 0.1615 - 0.3230 = \boxed{0.5155}$$

**ii. $P(X = 2 \mid X \ge 1)$**

Using the definition of conditional probability:

$$P(X=2 \mid X \ge 1) = \frac{P(X=2 \cap X \ge 1)}{P(X \ge 1)} = \frac{P(X=2)}{P(X \ge 1)}$$

$$P(X=2) = \binom{10}{2}\left(\frac{1}{6}\right)^2\left(\frac{5}{6}\right)^8 = 45 \times \frac{1}{36} \times 0.2326 \approx 0.2907$$

$$P(X \ge 1) = 1 - P(X=0) = 1 - 0.1615 = 0.8385$$

$$P(X=2 \mid X \ge 1) = \frac{0.2907}{0.8385} \approx \boxed{0.3467}$$

**iii) R command for question ii)**

```r
dbinom(2, size = 10, prob = 1/6) / (1 - dbinom(0, size = 10, prob = 1/6))
```

---

**PROBLEM 3:** A digital communication channel transmits binary digital signals (0 and 1). The probability of transmitting digit 0 is 0.45 and the probability of transmitting 1 is 0.55. Due to noise in the channel:
- If 0 is transmitted, the probability of receiving it incorrectly as 1 is 0.10.
- If 1 is transmitted, the probability of receiving it incorrectly as 0 is 0.15.
A. What is the probability of receiving digit 1?
B. If digit 1 is received, what is the probability that 0 was actually transmitted?
C. What is the total probability of error during signal transmission in this channel?

### Solution to Problem 3

**Definition:**
- $T_0$: 0 is transmitted, $P(T_0) = 0.45$
- $T_1$: 1 is transmitted, $P(T_1) = 0.55$
- $R_1$: 1 is received: $P(R_1|T_0) = 0.10$, $P(R_1|T_1) = 0.85$
- $R_0$: 0 is received: $P(R_0|T_1) = 0.15$, $P(R_0|T_0) = 0.90$

**A. $P(R_1)$ — total probability of receiving 1**

$$P(R_1) = P(R_1|T_0) \cdot P(T_0) + P(R_1|T_1) \cdot P(T_1)$$

$$= 0.10 \times 0.45 + 0.85 \times 0.55 = 0.045 + 0.4675 = \boxed{0.5125}$$

**B. $P(T_0 | R_1)$ — Bayes**

$$P(T_0 \mid R_1) = \frac{P(R_1|T_0) \cdot P(T_0)}{P(R_1)} = \frac{0.10 \times 0.45}{0.5125} = \frac{0.045}{0.5125} \approx \boxed{0.0878}$$

**C. Total probability of error**

An error occurs when 0 is transmitted and 1 is received, or 1 is transmitted and 0 is received:

$$P(\text{error}) = P(R_1|T_0) \cdot P(T_0) + P(R_0|T_1) \cdot P(T_1)$$

$$= 0.10 \times 0.45 + 0.15 \times 0.55 = 0.045 + 0.0825 = \boxed{0.1275}$$

---

**PROBLEM 4:** A machine fills bottles with soft drink. The volume of the soft drink follows the Normal distribution with mean $\mu$ and standard deviation $\sigma$. It is known that 10% of the bottles contain more than 334.8 ml, while 5% contain less than 318.5 ml.
i. Find the parameters $\mu$ and $\sigma$ of the distribution.
ii. If the nominal volume is 330 ml, what is the probability that a bottle contains less than the nominal volume?
iii. Which R commands are needed to find the probability of question ii)?
Given: For the standard normal variable $Z$, $P(Z \le 1.282) = 0.90$, $P(Z \le 1.645) = 0.95$, and $\Phi(-0.5) = 0.3085$.

### Solution to Problem 4

**Given Data:** $X \sim N(\mu,\ \sigma)$

**i. Finding $\mu$ and $\sigma$**

From the data, a system of two equations is formed:

- $P(X > 334.8) = 0.10 \Rightarrow P(X \le 334.8) = 0.90 \Rightarrow \dfrac{334.8 - \mu}{\sigma} = 1.282$

$$334.8 - \mu = 1.282\sigma \quad \cdots (1)$$

- $P(X < 318.5) = 0.05 \Rightarrow \dfrac{318.5 - \mu}{\sigma} = -1.645$

$$318.5 - \mu = -1.645\sigma \quad \cdots (2)$$

Subtracting (2) from (1):

$$334.8 - 318.5 = 1.282\sigma + 1.645\sigma$$

$$16.3 = 2.927\sigma \Rightarrow \sigma = \frac{16.3}{2.927} \approx \boxed{5.57 \text{ ml}}$$

From (1): $\mu = 334.8 - 1.282 \times 5.57 = 334.8 - 7.14 \approx \boxed{327.66 \text{ ml}}$

**ii. $P(X < 330)$**

$$z = \frac{330 - 327.66}{5.57} \approx \frac{2.34}{5.57} \approx 0.42$$

Using $\Phi(-0.5) = 0.3085$, we observe that $z \approx 0.42$ is not given directly. From the table $\Phi(0.5) = 1 - 0.3085 = 0.6915$. For $z \approx 0.42$:

$$P(X < 330) \approx \boxed{0.6628}$$

- Since $\mu \approx 327.66 < 330$, more than 50% of the bottles contain less than 330 ml.

**iii. R commands for question ii**

```r
pnorm(330, mean = 327.66, sd = 5.57)
```

---

---

## FORMULA SHEET

**Probability and Statistics (405)**

**Mean:**
$\bar{X} = \frac{1}{n} \sum_{i=1}^n X_i$, $\bar{X} = \frac{1}{n} \sum_{i=1}^k X_i f_i$

**Variance:**
$s^2 = \frac{1}{n-1} \sum_{i=1}^n (x_i - \bar{x})^2$, $s^2 = \frac{1}{n-1} \sum_{i=1}^k (X_i - \bar{X})^2 \cdot f_i$

**Coefficient of variation:** $CV = s / \bar{x}$

If $F_{(i-1)} \le \frac{N}{2} \le F_i$ then the **median** (for grouped data):
$M = x_{(i-1)} + \frac{\delta}{f_i} \left( \frac{N}{2} - F_{(i-1)} \right)$

If $F_{(i-1)} \le \frac{kN}{4} \le F_i$ then $Q_k = x_{(i-1)} + \frac{\delta}{f_i} \left( \frac{kN}{4} - F_{(i-1)} \right), \quad k = 1, 2, 3$

**Mode** (for grouped data):
$T = x_{(i-1)} + \delta \frac{\Delta_1}{\Delta_1 + \Delta_2}$

**Classical definition of probability:**
$P(A) = \frac{N(A)}{N(\Omega)}$,
$N(A)$: number of favorable outcomes for event A
$N(\Omega)$: total number of possible outcomes

**Properties:**
I) $P(A') = 1 - P(A)$, II) $P(\emptyset) = 0$, III) $P(A) \le 1$
IV) $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ .....(Additive Law)
V) If $A_1, A_2, \cdots, A_n$ are $n$ mutually exclusive events of the sample space $\Omega$, then:
$P(A_1 \cup A_2 \cup \cdots \cup A_n) = P(A_1) + P(A_2) + \cdots + P(A_n)$.
VI) If $A \subseteq B$, then a) $P(B - A) = P(B) - P(A)$ and b) $P(A) \le P(B)$

**Conditional Probability:**
$P(A|B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) > 0$

**Multiplication Rule:**
$P(A \cap B) = P(A|B)P(B)$

**Independent Events:**
$P(A \cap B) = P(A)P(B)$

If $A_i \cap A_j = \emptyset, \forall i \neq j$ and $A_1 \cup A_2 \cup \ldots \cup A_n = \Omega$ then:
**Law of Total Probability:**
$P(B) = P(B \cap A_1) + P(B \cap A_2) + \cdots + P(B \cap A_n)$

**Bayes' Theorem:**
$P(A_i | B) = \frac{P(B \cap A_i)}{P(B)} = \frac{P(B|A_i)P(A_i)}{\sum_{k=1}^n P(B|A_k)P(A_k)}$
