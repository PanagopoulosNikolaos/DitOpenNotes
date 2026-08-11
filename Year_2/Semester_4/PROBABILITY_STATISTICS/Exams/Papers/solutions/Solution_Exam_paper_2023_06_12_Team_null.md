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

### Solution to Problem 1

**Given Data:**
- $P(K) = 0.35$ (Kathimerini)
- $P(B) = 0.20$ (To Vima)
- $P(K \cap B) = 0.08$ (both)

**A. $P(K \cup B)$ — at least one newspaper**

Using the Additive Law:

$$P(K \cup B) = P(K) + P(B) - P(K \cap B)$$

$$P(K \cup B) = 0.35 + 0.20 - 0.08 = \boxed{0.47}$$

- We add the individual probabilities and subtract the intersection to avoid double counting.

**B. $P(B \cap K')$ — only To Vima**

$$P(B \cap K') = P(B) - P(B \cap K)$$

$$P(B \cap K') = 0.20 - 0.08 = \boxed{0.12}$$

- From the total reading To Vima we subtract those reading both.

**C. $P((K \cup B)')$ — neither newspaper**

$$P((K \cup B)') = 1 - P(K \cup B)$$

$$P((K \cup B)') = 1 - 0.47 = \boxed{0.53}$$

- The complement of the union yields the probability of reading neither.

**D. $P(B | K)$ — To Vima given Kathimerini**

Using the definition of conditional probability:

$$P(B \mid K) = \frac{P(B \cap K)}{P(K)}$$

$$P(B \mid K) = \frac{0.08}{0.35} \approx \boxed{0.2286}$$

- We restrict the sample space to those reading Kathimerini and find the fraction that also read To Vima.

---

**PROBLEM 2:** A factory produces batteries of a specific type for mobile phone devices. According to factory data, the battery lifespan can be assumed to follow a normal distribution with mean $\mu=48$ hours and standard deviation $\sigma=4$ hours. If a battery is selected at random, calculate the probability that:
i) the lifespan is between 39 and 57 hours
ii) the lifespan exceeds 42 hours
iii) what R command should we give to calculate the probability of question i)?
Given: $P(Z \le 2.25) = 0.98778$, $P(Z \le 1.5) = 0.93319$.

### Solution to Problem 2

**Given Data:** $X \sim N(\mu=48,\ \sigma=4)$

Standardization: $Z = \dfrac{X - \mu}{\sigma}$

**i) $P(39 \le X \le 57)$**

$$z_1 = \frac{39 - 48}{4} = \frac{-9}{4} = -2.25, \qquad z_2 = \frac{57 - 48}{4} = \frac{9}{4} = 2.25$$

$$P(39 \le X \le 57) = P(-2.25 \le Z \le 2.25)$$

$$= P(Z \le 2.25) - P(Z \le -2.25)$$

- Utilizing the symmetry of the Normal distribution: $P(Z \le -a) = 1 - P(Z \le a)$.

$$= P(Z \le 2.25) - [1 - P(Z \le 2.25)]$$

$$= 2 \cdot P(Z \le 2.25) - 1 = 2 \times 0.98778 - 1 = \boxed{0.97556}$$

**ii) $P(X > 42)$**

$$z = \frac{42 - 48}{4} = \frac{-6}{4} = -1.5$$

$$P(X > 42) = P(Z > -1.5) = 1 - P(Z \le -1.5) = P(Z \le 1.5)$$

$$= \boxed{0.93319}$$

- Utilizing symmetry: $P(Z > -a) = P(Z \le a)$.

**iii) R command for question i)**

```r
pnorm(57, mean = 48, sd = 4) - pnorm(39, mean = 48, sd = 4)
```

---

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

### Solution to Problem 3

**Table Completion:**

| Score | $x_i$ | $f_i$ | $f_i x_i$ | $F_i$ |
|---|---|---|---|---|
| [0, 20)   | 10 | 26  | 260   | 26  |
| [20, 40)  | 30 | 70  | 2100  | 96  |
| [40, 60)  | 50 | 110 | 5500  | 206 |
| [60, 80)  | 70 | 69  | 4830  | 275 |
| [80, 100] | 90 | 25  | 2250  | 300 |
| TOTAL    |    | 300 | 14940 |     |

**i. Mean score $\bar{x}$**

$$\bar{x} = \frac{1}{n} \sum f_i x_i = \frac{14940}{300} = \boxed{49.8}$$

- The numerator is the sum of $f_i x_i$ and the denominator is the total count.

**Standard deviation $s$**

$$s^2 = \frac{1}{n-1} \sum f_i(x_i - \bar{x})^2 = \frac{137188}{299} \approx 458.82$$

$$s = \sqrt{458.82} \approx \boxed{21.42}$$

**Median $M_e$**

- $n/2 = 150$. The value $F_2 = 96 < 150 \le 206 = F_3$, so the median lies in the 3rd class $[40, 60)$.

$$M_e = L + \left( \frac{\frac{n}{2} - F_{i-1}}{f_i} \right) \cdot w = 40 + \left( \frac{150 - 96}{110} \right) \cdot 20$$

$$M_e = 40 + \left( \frac{54}{110} \right) \cdot 20 \approx 40 + 9.82 = \boxed{49.82}$$

**ii. Cutoff score if half are hired**

Half of 300 candidates is 150; the top 150 with highest scores are hired. The cutoff score is the median:

$$\text{Cutoff Score} \approx \boxed{49.82}$$

- The median divides the 300 candidates into two equal groups of 150.

**iii. Interval for 95% of candidates (Empirical Rule)**

$$[\bar{x} - 2s,\ \bar{x} + 2s] = [49.8 - 2(21.42),\ 49.8 + 2(21.42)]$$

$$= [49.8 - 42.84,\ 49.8 + 42.84] = \boxed{[6.96,\ 92.64]}$$

- For a Normal distribution, approximately 95% of values fall within the interval $\mu \pm 2\sigma$.

**iv. R command for median**

```r
median(data)
```

---

**PROBLEM 4:** In a factory hall, 6 machines are installed. The machines operate independently and the probability that any one machine fails during a day is 0.02.
i. Find the probability that exactly 1 machine fails.
ii. Find the probability that at least 2 machines fail.
iii. What R command should we give to calculate the probability of question ii)?

### Solution to Problem 4

**Given Data:** $X \sim B(n=6,\ p=0.02)$

The Binomial distribution formula:

$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$$

**i. $P(X = 1)$**

$$P(X=1) = \binom{6}{1}(0.02)^1(0.98)^5$$

$$= 6 \times 0.02 \times 0.9039 = \boxed{0.1085}$$

- $0.98^5 = 0.9039$ (calculation).

**ii. $P(X \ge 2)$**

Using the complement rule:

$$P(X \ge 2) = 1 - P(X = 0) - P(X = 1)$$

$$P(X=0) = \binom{6}{0}(0.02)^0(0.98)^6 = 0.98^6 = 0.8858$$

$$P(X \ge 2) = 1 - 0.8858 - 0.1085 = \boxed{0.0057}$$

- The complement rule avoids summing multiple terms.

**iii. R command for question ii)**

```r
1 - pbinom(1, size = 6, prob = 0.02)
```

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
