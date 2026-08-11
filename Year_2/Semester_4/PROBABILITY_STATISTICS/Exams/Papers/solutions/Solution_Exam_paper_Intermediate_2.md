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

### Solution to Problem 1

**Δεδομένα (ταξινομημένα):** 4, 5, 5, 6, 7, 7, 8, 8, 8, 9, 9, 10 — $n=12$

**a. Μέση τιμή $\bar{x}$**

$$\bar{x} = \frac{4+5+5+6+7+7+8+8+8+9+9+10}{12} = \frac{86}{12} \approx \boxed{7.167}$$

**3ο Τεταρτημόριο $Q_3$**

- Θέση $Q_3$: $\frac{3(n+1)}{4} = \frac{3 \times 13}{4} = 9.75$, δηλαδή μεταξύ 9ης και 10ης τιμής.

$$Q_3 = x_{(9)} + 0.75 \cdot (x_{(10)} - x_{(9)}) = 8 + 0.75(9-8) = 8 + 0.75 = \boxed{8.75}$$

**Mode $T$**

- Ο βαθμός 8 εμφανίζεται 3 φορές (περισσότερο από κάθε άλλο).

$$T = \boxed{8}$$

**b. Διακύμανση $s^2$**

| $x_i$ | $x_i - \bar{x}$ | $(x_i - \bar{x})^2$ |
|---|---|---|
| 4  | -3.167 | 10.03 |
| 5  | -2.167 | 4.70  |
| 5  | -2.167 | 4.70  |
| 6  | -1.167 | 1.36  |
| 7  | -0.167 | 0.03  |
| 7  | -0.167 | 0.03  |
| 8  | 0.833  | 0.69  |
| 8  | 0.833  | 0.69  |
| 8  | 0.833  | 0.69  |
| 9  | 1.833  | 3.36  |
| 9  | 1.833  | 3.36  |
| 10 | 2.833  | 8.03  |
| **Σύνολο** | | **37.67** |

$$s^2 = \frac{37.67}{11} \approx \boxed{3.424}$$

**Coefficient of Variation $CV$**

$$CV = \frac{s}{\bar{x}} = \frac{\sqrt{3.424}}{7.167} = \frac{1.851}{7.167} \approx \boxed{0.258 = 25.8\%}$$

- Ο CV εκφράζει τη διασπορά ως ποσοστό του μέσου, επιτρέπει σύγκριση μεταξύ διαφορετικών συνόλων δεδομένων.

**c. Εντολές R**

```r
scores <- c(4, 5, 5, 6, 7, 7, 8, 8, 8, 9, 9, 10)
var(scores)      # διακύμανση
mean(scores)     # μέση τιμή
```

---

**ΘΕΜΑ 2:** Ένα λογισμικό έχει πιθανότητα 10% να παρουσιάσει σφάλμα κατά την εκκίνησή του. Εκτελούμε 10 ανεξάρτητες εκκινήσεις του λογισμικού.
i) Ποια είναι η πιθανότητα να παρουσιαστεί σφάλμα σε ακριβώς 2 εκκινήσεις;
ii) Ποια είναι η πιθανότητα να παρουσιαστεί σφάλμα σε τουλάχιστον 2 εκκινήσεις;
iii) Ποια εντολή R υπολογίζει την πιθανότητα του ερωτήματος ii;

### Solution to Problem 2

**Given Data:** $X \sim B(n=10,\ p=0.10)$

$$P(X=k) = \binom{10}{k}(0.10)^k(0.90)^{10-k}$$

**i. $P(X=2)$**

$$P(X=2) = \binom{10}{2}(0.10)^2(0.90)^8 = 45 \times 0.01 \times 0.4305 = \boxed{0.1937}$$

- $0.90^8 = 0.4305$ (calculation).

**ii. $P(X \ge 2)$**

$$P(X \ge 2) = 1 - P(X=0) - P(X=1)$$

$$P(X=0) = (0.90)^{10} = 0.3487$$

$$P(X=1) = 10 \times 0.10 \times (0.90)^9 = 10 \times 0.10 \times 0.3874 = 0.3874$$

$$P(X \ge 2) = 1 - 0.3487 - 0.3874 = \boxed{0.2639}$$

**iii) R command for question ii)**

```r
1 - pbinom(1, size = 10, prob = 0.10)
```

---

**ΘΕΜΑ 3:** Για δύο ενδεχόμενα $A$ και $B$ ενός δειγματικού χώρου $\Omega$ δίνονται $P(A) = 0.6$, $P(B) = 0.5$ και $P(A \cap B) = 0.3$.
Α. Να υπολογίσετε την $P(A \cup B)$ και την $P(A \cap B')$.
Β. Να υπολογίσετε τη δεσμευμένη πιθανότητα $P(A' | B')$.
C. Είναι τα ενδεχόμενα $A$ και $B$ ανεξάρτητα; Να δικαιολογήσετε την απάντησή σας.

### Solution to Problem 3

**Given Data:** $P(A)=0.6$, $P(B)=0.5$, $P(A \cap B)=0.3$

**Α. $P(A \cup B)$ και $P(A \cap B')$**

$$P(A \cup B) = P(A) + P(B) - P(A \cap B) = 0.6 + 0.5 - 0.3 = \boxed{0.8}$$

$$P(A \cap B') = P(A) - P(A \cap B) = 0.6 - 0.3 = \boxed{0.3}$$

- Η $P(A \cap B')$ αφαιρεί από το Α τον τμήμα που αλληλεπικαλύπτεται με το Β.

**Β. $P(A' | B')$**

$$P(B') = 1 - P(B) = 0.5$$

$$P(A' \cap B') = 1 - P(A \cup B) = 1 - 0.8 = 0.2 \quad \text{(νόμος De Morgan)}$$

$$P(A' \mid B') = \frac{P(A' \cap B')}{P(B')} = \frac{0.2}{0.5} = \boxed{0.4}$$

**C. Ανεξαρτησία;**

Για ανεξαρτησία απαιτείται: $P(A \cap B) = P(A) \cdot P(B)$

$$P(A) \cdot P(B) = 0.6 \times 0.5 = 0.30$$

$$P(A \cap B) = 0.30 = P(A) \cdot P(B) \Rightarrow \textbf{Τα Α και Β είναι ανεξάρτητα.}$$

- Η ισότητα επιβεβαιώνεται αριθμητικά, άρα η γνώση του ενός δεν επηρεάζει την πιθανότητα του άλλου.

---

**ΘΕΜΑ 4:** Ο χρόνος αναμονής σε μια ουρά σούπερ μάρκετ ακολουθεί την Κανονική Κατανομή με μέσο $\mu = 8$ λεπτά και τυπική απόκλιση $\sigma = 2.5$ λεπτά.
i. Ποια είναι η πιθανότητα ένας πελάτης να περιμένει περισσότερο από 13 λεπτά;
ii. Ποια είναι η πιθανότητα ένας πελάτης να περιμένει μεταξύ 5.5 και 10.5 λεπτά;
iii. Ποια εντολή R υπολογίζει την πιθανότητα ένας πελάτης να περιμένει το πολύ 6 λεπτά;
Δίνονται: $\Phi(1) = P(Z \le 1) = 0.84134$, $\Phi(2) = P(Z \le 2) = 0.97725$.

### Solution to Problem 4

**Given Data:** $X \sim N(\mu=8,\ \sigma=2.5)$

**i. $P(X > 13)$**

$$z = \frac{13 - 8}{2.5} = \frac{5}{2.5} = 2$$

$$P(X > 13) = 1 - P(Z \le 2) = 1 - 0.97725 = \boxed{0.02275}$$

**ii. $P(5.5 \le X \le 10.5)$**

$$z_1 = \frac{5.5 - 8}{2.5} = -1, \qquad z_2 = \frac{10.5 - 8}{2.5} = 1$$

$$P(5.5 \le X \le 10.5) = P(-1 \le Z \le 1) = P(Z \le 1) - P(Z \le -1)$$

$$= \Phi(1) - [1 - \Phi(1)] = 2\Phi(1) - 1 = 2(0.84134) - 1 = \boxed{0.68268}$$

- Το διάστημα $[\mu-\sigma, \mu+\sigma]$ περιέχει περίπου 68.3% των παρατηρήσεων (εμπειρικός κανόνας).

**iii. Εντολή R για $P(X \le 6)$**

```r
pnorm(6, mean = 8, sd = 2.5)
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
