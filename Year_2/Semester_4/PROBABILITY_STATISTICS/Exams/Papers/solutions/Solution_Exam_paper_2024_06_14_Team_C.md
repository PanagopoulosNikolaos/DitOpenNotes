# Exam Paper 2024 06 14 (Team C)

**Team C**
**UNIVERSITY OF IOANNINA**                   Full Name:_______________________
**Department of Computer Science & Telecommunications**    Student ID:________________________________
**COURSE: Probability & Statistics**       Friday 14/06/2024

Instructions:
1. Write your full name on the exam sheet.
2. All problems carry equal weight
3. Hand in the question sheet along with your answer booklet.
4. Use of pocket calculators is permitted; mobile phones are prohibited

**PROBLEM 1:** In a manufacturing industry, 1% of a product is non-compliant (defective). We randomly select 7 units of this product for inspection. What is the probability that:
a. exactly one product unit is defective
b. 2 or more units are defective
c. What command should we give in R to calculate the probability of question a)?

**PROBLEM 2:** In a survey conducted in a region regarding readership of various Sunday newspapers, 25% stated they read "Ta Nea", 35% "To Vima", and 5% stated they read both newspapers. A person is selected at random. Calculate the probability that they:
A. read at least one of the two newspapers
B. read neither of the two newspapers
C. read only "Ta Nea"
D. read "Ta Nea", given that they read "To Vima"

**PROBLEM 3:** The service time required for bank customers at the teller follows a Normal distribution with mean $\mu=10$ min and standard deviation $\sigma=2$ min. What is the probability that a customer waits:
i) more than 7 min
ii) between 9 and 13 min
iii) what command should we give in R to calculate the probability of question ii)?

Given: $\Phi(0.5) = P(Z \le 0.5) = 0.69146$, $\Phi(1.5) = P(Z \le 1.5) = 0.93319$

**PROBLEM 4:** The monthly salary of employees in a company is given in the following table:

| Monthly Salary | Number of Employees | $f_i x_i$ | $f_i(x_i - \bar{x})^2$ | $F_i$ |
| --- | --- | --- | --- | --- |
| 1250 | 22 | | 2217737.5 | |
| 1300 | 35 | | 2504468.75 | |
| 1550 | 65 | | 19906.25 | |
| 1800 | 38 | | 2054137.5 | |
| 2000 | 20 | | 3741125 | |
| Total | 180 | | 10537375 | |

A. Calculate the mean monthly salary, the first quartile, and the standard deviation.
B. What percentage of employees have a salary of at most 1300 €?
C. Company management decided to grant an allowance to the 25% of employees with the lowest monthly salary. What maximum salary must an employee have to receive the allowance?
D. What commands should we give in R to calculate the mode of our data?

### Solution to Problem 1

**Given Data:** $X \sim B(n=7,\ p=0.01)$

$$P(X=k) = \binom{7}{k}(0.01)^k(0.99)^{7-k}$$

**a. $P(X=1)$**

$$P(X=1) = \binom{7}{1}(0.01)^1(0.99)^6 = 7 \times 0.01 \times 0.9415 = \boxed{0.06590}$$

- $0.99^6 = 0.9415$ (calculation).

**b. $P(X \ge 2)$**

$$P(X \ge 2) = 1 - P(X=0) - P(X=1)$$

$$P(X=0) = (0.99)^7 = 0.9321$$

$$P(X \ge 2) = 1 - 0.9321 - 0.0659 = \boxed{0.0020}$$

- Ο συμπληρωματικός κανόνας αποφεύγει την άθροιση πολλών όρων.

**c. Εντολή R για ερώτημα a**

```r
dbinom(1, size = 7, prob = 0.01)
```

---

**ΘΕΜΑ 2:** Σε δημοσκόπηση που έγινε σε μία περιοχή σχετικά με την αναγνωσιμότητα διάφορων κυριακάτικων εντύπων, το 25% δήλωσε ότι διαβάζει "τα Νέα", το 35% "το Βήμα" και ένα 5% δήλωσε ότι διαβάζει και τις δύο εφημερίδες. Επιλέγουμε τυχαία ένα άτομο. Να υπολογισθεί η πιθανότητα:
Α. να διαβάζει τουλάχιστον μία από τις δύο εφημερίδες
Β. να μη διαβάζει καμία από τις δύο εφημερίδες
C. να διαβάζει μόνο " τα Νέα "
D. να διαβάζει "τα Νέα", δοθέντος ότι διαβάζει "το Βήμα"

### Solution to Problem 2

**Given Data:**
- $P(N) = 0.25$ (Νέα)
- $P(B) = 0.35$ (Βήμα)
- $P(N \cap B) = 0.05$

**Α. $P(N \cup B)$ — at least one newspaper**

$$P(N \cup B) = P(N) + P(B) - P(N \cap B) = 0.25 + 0.35 - 0.05 = \boxed{0.55}$$

**Β. $P((N \cup B)')$ — neither newspaper**

$$P((N \cup B)') = 1 - P(N \cup B) = 1 - 0.55 = \boxed{0.45}$$

**C. $P(N \cap B')$ — μόνο Νέα**

$$P(N \cap B') = P(N) - P(N \cap B) = 0.25 - 0.05 = \boxed{0.20}$$

**D. $P(N | B)$ — Νέα δοθέντος Βήματος**

$$P(N \mid B) = \frac{P(N \cap B)}{P(B)} = \frac{0.05}{0.35} \approx \boxed{0.1429}$$

---

**ΘΕΜΑ 3:** Ο χρόνος που απαιτείται από τους πελάτες μιας τράπεζας για να εξυπηρετηθούν από το ταμείο, ακολουθεί την Κανονική Κατανομή με μέση τιμή μ=10 min και απόκλιση σ=2 min. Ποια η πιθανότητα κάποιος πελάτης να περιμένει
i) περισσότερο από 7 min
ii) μεταξύ 9 και 13 min
iii) ποια εντολή πρέπει να δώσουμε στην R για να υπολογίσει την πιθανότητα του ερωτήματος ii ;

Δίνονται: $\Phi(0.5) = P(Z \le 0.5) = 0.69146$, $\Phi(1.5) = P(Z \le 1.5) = 0.93319$

### Solution to Problem 3

**Given Data:** $X \sim N(\mu=10,\ \sigma=2)$

**i. $P(X > 7)$**

$$z = \frac{7 - 10}{2} = -1.5$$

$$P(X > 7) = P(Z > -1.5) = P(Z \le 1.5) = \boxed{0.93319}$$

- Συμμετρία κανονικής: $P(Z > -a) = P(Z \le a)$.

**ii. $P(9 \le X \le 13)$**

$$z_1 = \frac{9 - 10}{2} = -0.5, \qquad z_2 = \frac{13 - 10}{2} = 1.5$$

$$P(9 \le X \le 13) = P(-0.5 \le Z \le 1.5) = P(Z \le 1.5) - P(Z \le -0.5)$$

$$= \Phi(1.5) - [1 - \Phi(0.5)] = 0.93319 - (1 - 0.69146)$$

$$= 0.93319 - 0.30854 = \boxed{0.62465}$$

**iii) R command for question ii)**

```r
pnorm(13, mean = 10, sd = 2) - pnorm(9, mean = 10, sd = 2)
```

---

**ΘΕΜΑ 4:** Ο μηνιαίος μισθός των υπαλλήλων μιας εταιρείας δίνεται στον παρακάτω πίνακα

| Monthly Salary | Number of Employees | $f_i x_i$ | $f_i(x_i - \bar{x})^2$ | $F_i$ |
| --- | --- | --- | --- | --- |
| 1250 | 22 | | 2217737.5 | |
| 1300 | 35 | | 2504468.75 | |
| 1550 | 65 | | 19906.25 | |
| 1800 | 38 | | 2054137.5 | |
| 2000 | 20 | | 3741125 | |
| Total | 180 | | 10537375 | |

A. Να υπολογίσετε τον μέσο μηνιαίο μισθό, το πρώτο τεταρτημόριο και τη τυπική απόκλιση.
B. Τι ποσοστό των εργαζομένων έχουν μισθό το πολύ 1300 €;
C. Η διεύθυνση της εταιρείας αποφάσισε τη χορήγηση ενός επιδόματος στο 25% των υπαλλήλων της με τον μικρότερο μηνιαίο μισθό. Τι μισθό πρέπει να έχει κάποιος υπάλληλος για να πάρει το επίδομα;
D. Ποιες εντολές πρέπει να δώσουμε στην R για να υπολογίσει την επικρατούσα τιμή των δεδομένων μας;

### Solution to Problem 4

**Σημείωση:** Τα δεδομένα είναι μη-ομαδοποιημένα (διακριτές τιμές μισθού).

**Table Completion:**

| $x_i$ | $f_i$ | $f_i x_i$ | $F_i$ |
|---|---|---|---|
| 1250 | 22  | 27500  | 22  |
| 1300 | 35  | 45500  | 57  |
| 1550 | 65  | 100750 | 122 |
| 1800 | 38  | 68400  | 160 |
| 2000 | 20  | 40000  | 180 |
| Σύν. | 180 | 282150 |     |

**A. Μέση τιμή $\bar{x}$**

$$\bar{x} = \frac{\sum f_i x_i}{n} = \frac{282150}{180} = \boxed{1567.50 \text{ €}}$$

**Standard Deviation $s$**

$$s^2 = \frac{\sum f_i(x_i - \bar{x})^2}{n-1} = \frac{10537375}{179} \approx 58869.47$$

$$s = \sqrt{58869.47} \approx \boxed{242.63 \text{ €}}$$

**Πρώτο τεταρτημόριο $Q_1$**

- $\frac{N}{4} = 45$. Έχουμε $F_1 = 22 < 45 \le 57 = F_2$, άρα $Q_1$ βρίσκεται στην κατηγορία με μισθό 1300 €.

$$Q_1 = \boxed{1300 \text{ €}}$$

- Καθώς τα δεδομένα είναι διακριτά, το $Q_1$ είναι η τιμή που αντιστοιχεί στην κλάση που περιέχει το 25ο εκατοστημόριο.

**B. Ποσοστό με μισθό $\le 1300$ €**

$$\text{Ποσοστό} = \frac{F_2}{n} = \frac{57}{180} \approx 0.3167 = \boxed{31.67\%}$$

**C. Όριο για επίδομα (κατώτερο 25% → $Q_1$)**

$$\text{Όριο} = Q_1 = \boxed{1300 \text{ €}}$$

- Οι 25% με τον μικρότερο μισθό αντιστοιχούν στο 1ο τεταρτημόριο.

**D. Εντολές R για επικρατούσα τιμή**

```r
salaries <- c(...)        # data input
# Η R δεν έχει ενσωματωμένη συνάρτηση mode· χρησιμοποιούμε:
table(salaries)           # εμφάνιση συχνοτήτων
names(which.max(table(salaries)))  # επικρατούσα τιμή
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
