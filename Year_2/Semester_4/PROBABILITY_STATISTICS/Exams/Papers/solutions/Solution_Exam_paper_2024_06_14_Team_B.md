# Exam Paper 2024 06 14 (Team B)

**Team B**
**UNIVERSITY OF IOANNINA**                   Full Name:_______________________
**Department of Computer Science & Telecommunications**    Student ID:________________________________
**COURSE: Probability & Statistics**       Friday 14/06/2024

Instructions:
1. Write your full name on the exam sheet.
2. All problems carry equal weight
3. Hand in the question sheet along with your answer booklet.
4. Use of pocket calculators is permitted; mobile phones are prohibited

**PROBLEM 1:** The times (in minutes) required by 120 workers in a factory to perform a task are given in the following table after grouping:

| Times (in min) | Class Marks $x_i$ | Number of Workers $f_i$ | $f_i x_i$ | $f_i(x_i - \bar{x})^2$ | $F_i$ |
| --- | --- | --- | --- | --- | --- |
| [20, 25) | | 10 | | 1050.625 | |
| [25, 30) | | 22 | | 606.375 | |
| [30, 35) | | 50 | | 3.125 | |
| [35, 40) | | 28 | | 631.75 | |
| [40, 45) | | 10 | | 950.625 | |
| Total | | 120 | | 3242.5 | |

a. Using the table, calculate the mean time ($\bar{x}$) for task completion, the 1st quartile ($Q_1$), and the standard deviation.
b. Within what interval does the task completion time range for 68% of workers?
c. Management decided to give a bonus to the 25% of workers with the shortest completion time. What is the maximum completion time a worker can have to receive the bonus?
d. What commands should we give in R to calculate the mean of our data?

**PROBLEM 2:** In a manufacturing industry, 2% of a product is non-compliant (defective). We randomly select 6 units of this product for inspection. What is the probability that:
i) exactly one product unit is defective
ii) 2 or more units are defective
iii) What command should we give in R to calculate the probability of question i)?

**PROBLEM 3:** A study in a company revealed that 60% of employees know English, while 75% of employees are computer literate (PC). Finally, 55% know both English and PC. We select an employee at random; find the probabilities of the following events:
A. The employee possesses at least one of the above qualifications (English or PC).
B. The employee possesses only PC skills.
C. The employee possesses neither of the two qualifications.
D. Given that the employee knows English, what is the probability that they know PC?

**PROBLEM 4:** A factory manufactures electric refrigerators for which the time until the first failure follows a Normal distribution with mean $\mu=15$ years and standard deviation $\sigma=4$ years. What is the probability for an electric refrigerator that:
i. the first failure occurs after 9 years
ii. the first failure occurs between 13 and 17 years
iii. what command should we give in R to calculate the probability of question ii)?
Given: $\Phi(0.5) = P(Z \le 0.5) = 0.69146$, $\Phi(1.5) = P(Z \le 1.5) = 0.93319$.

### Solution to Problem 1

**Table Completion:**

| Interval | $x_i$ | $f_i$ | $f_i x_i$ | $F_i$ |
|---|---|---|---|---|
| [20, 25) | 22.5 | 10  | 225   | 10  |
| [25, 30) | 27.5 | 22  | 605   | 32  |
| [30, 35) | 32.5 | 50  | 1625  | 82  |
| [35, 40) | 37.5 | 28  | 1050  | 110 |
| [40, 45) | 42.5 | 10  | 425   | 120 |
| Total    |      | 120 | 3930  |     |

**a. Μέση τιμή $\bar{x}$**

$$\bar{x} = \frac{\sum f_i x_i}{n} = \frac{3930}{120} = \boxed{32.75 \text{ min}}$$

**Standard Deviation $s$**

$$s^2 = \frac{\sum f_i(x_i - \bar{x})^2}{n-1} = \frac{3242.5}{119} \approx 27.25$$

$$s = \sqrt{27.25} \approx \boxed{5.22 \text{ min}}$$

**Πρώτο τεταρτημόριο $Q_1$**

- $\frac{n}{4} = 30$. Έχουμε $F_1 = 10 < 30 \le 32 = F_2$, άρα το $Q_1$ βρίσκεται στη 2η κλάση $[25, 30)$.

$$Q_1 = L + \left( \frac{\frac{n}{4} - F_{i-1}}{f_i} \right) \cdot w = 25 + \left( \frac{30 - 10}{22} \right) \cdot 5 = 25 + \frac{100}{22} = 25 + 4.545 \approx \boxed{29.55 \text{ min}}$$

- Ο τύπος παρεμβάλλει γραμμικά μέσα στην κλάση ώστε να περιέχονται ακριβώς $N/4$ παρατηρήσεις.

**b. Interval for 68% (Empirical Rule)**

$$[\bar{x} - s,\ \bar{x} + s] = [32.75 - 5.22,\ 32.75 + 5.22] = \boxed{[27.53,\ 37.97] \text{ min}}$$

- For a distribution approximating the Normal, about 68% of the data fall within $\mu \pm \sigma$.

**c. Χρόνος για μπόνους (κατώτερο 25% → $Q_1$)**

Το μπόνους λαμβάνουν οι 25% με τον **μικρότερο** χρόνο, άρα το όριο είναι το $Q_1$:

$$\text{Όριο} = Q_1 \approx \boxed{29.55 \text{ min}}$$

**d. R commands for mean**

```r
times <- c(...)          # data input
mean(times)              # mean calculation
```

---

**ΘΕΜΑ 2:** Σε μια βιομηχανία το 2% ενός προϊόντος είναι εκτός προδιαγραφών (ελαττωματικό). Επιλέγουμε τυχαία για έλεγχο 6 μονάδες του προϊόντος αυτού. Ποια η πιθανότητα
i) ακριβώς μία μονάδα προϊόντος να είναι ελαττωματική
ii) 2 ή περισσότερες μονάδες να είναι ελαττωματικές
iii) Ποια εντολή πρέπει να δώσουμε στην R για να υπολογίσει την πιθανότητα του ερωτήματος i;

### Solution to Problem 2

**Given Data:** $X \sim B(n=6,\ p=0.02)$

$$P(X=k) = \binom{6}{k}(0.02)^k(0.98)^{6-k}$$

**i. $P(X=1)$**

$$P(X=1) = \binom{6}{1}(0.02)^1(0.98)^5 = 6 \times 0.02 \times 0.9039 = \boxed{0.1085}$$

**ii. $P(X \ge 2)$**

$$P(X \ge 2) = 1 - P(X=0) - P(X=1)$$

$$P(X=0) = (0.98)^6 = 0.8858$$

$$P(X \ge 2) = 1 - 0.8858 - 0.1085 = \boxed{0.0057}$$

- Ο συμπληρωματικός κανόνας απλοποιεί τον υπολογισμό.

**iii. Εντολή R για ερώτημα i**

```r
dbinom(1, size = 6, prob = 0.02)
```

---

**ΘΕΜΑ 3:** Από μελέτη σε μια επιχείρηση προέκυψε ότι το 60% των υπαλλήλων γνωρίζει την αγγλική γλώσσα ενώ ένα 75% των υπαλλήλων γνωρίζει ηλεκτρονικό υπολογιστή (Η/Υ). Τέλος, ένα ποσοστό 55% γνωρίζει αγγλική γλώσσα και Η/Υ. Επιλέγουμε στην τύχη έναν υπάλληλο, να βρεθούν οι πιθανότητες των παρακάτω ενδεχομένων
Α. Ο υπάλληλος να διαθέτει τουλάχιστον ένα από τα παραπάνω προσόντα (αγγλική γλώσσα ή Η/Υ).
Β. Ο υπάλληλος να διαθέτει μόνο το προσόν της γνώσης Η/Υ.
C. Ο υπάλληλος να μη διαθέτει κανένα από τα δύο προσόντα.
D. Δοθέντος ότι ο υπάλληλος γνωρίζει αγγλικά, ποια η πιθανότητα να γνωρίζει Η/Υ;

### Solution to Problem 3

**Given Data:**
- $P(A) = 0.60$ (Αγγλικά)
- $P(H) = 0.75$ (Η/Υ)
- $P(A \cap H) = 0.55$

**Α. $P(A \cup H)$ — τουλάχιστον ένα προσόν**

$$P(A \cup H) = P(A) + P(H) - P(A \cap H) = 0.60 + 0.75 - 0.55 = \boxed{0.80}$$

**Β. $P(H \cap A')$ — μόνο Η/Υ**

$$P(H \cap A') = P(H) - P(H \cap A) = 0.75 - 0.55 = \boxed{0.20}$$

**C. $P((A \cup H)')$ — κανένα προσόν**

$$P((A \cup H)') = 1 - P(A \cup H) = 1 - 0.80 = \boxed{0.20}$$

**D. $P(H | A)$ — Η/Υ δοθέντος Αγγλικών**

$$P(H \mid A) = \frac{P(H \cap A)}{P(A)} = \frac{0.55}{0.60} \approx \boxed{0.9167}$$

---

**ΘΕΜΑ 4:** Ένα εργοστάσιο κατασκευάζει ηλεκτρικά ψυγεία για τα οποία, ο χρόνος μέχρι την εμφάνιση της πρώτης βλάβης ακολουθεί την Κανονική Κατανομή με μέσο μ=15 έτη και τυπική απόκλιση σ=4 έτη. Ποια η πιθανότητα για ένα ηλεκτρικό ψυγείο
i. η πρώτη βλάβη να εμφανιστεί μετά από 9 έτη
ii. η πρώτη βλάβη να εμφανιστεί μεταξύ 13 και 17 έτη
iii. ποια εντολή πρέπει να δώσουμε στην R για να υπολογίσει την πιθανότητα του ερωτήματος ii ;
Δίνονται: $\Phi(0.5) = P(Z \le 0.5) = 0.69146$, $\Phi(1.5) = P(Z \le 1.5) = 0.93319$.

### Solution to Problem 4

**Given Data:** $X \sim N(\mu=15,\ \sigma=4)$

**i. $P(X > 9)$**

$$z = \frac{9 - 15}{4} = \frac{-6}{4} = -1.5$$

$$P(X > 9) = P(Z > -1.5) = P(Z \le 1.5) = \boxed{0.93319}$$

- Utilizing symmetry: $P(Z > -a) = P(Z \le a)$.

**ii. $P(13 \le X \le 17)$**

$$z_1 = \frac{13 - 15}{4} = -0.5, \qquad z_2 = \frac{17 - 15}{4} = 0.5$$

$$P(13 \le X \le 17) = P(-0.5 \le Z \le 0.5)$$

$$= P(Z \le 0.5) - P(Z \le -0.5) = \Phi(0.5) - [1 - \Phi(0.5)]$$

$$= 2\Phi(0.5) - 1 = 2(0.69146) - 1 = \boxed{0.38292}$$

**iii) R command for question ii)**

```r
pnorm(17, mean = 15, sd = 4) - pnorm(13, mean = 15, sd = 4)
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
