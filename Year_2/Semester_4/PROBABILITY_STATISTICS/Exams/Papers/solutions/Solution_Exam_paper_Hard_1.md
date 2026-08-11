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

### Solution to Problem 1

**a. Εύρεση αγνώστου $x$**

$$\sum f_i = 100 \Rightarrow 15 + x + 40 + 20 + 5 = 100 \Rightarrow x = \boxed{20}$$

**Table Completion:**

| Ενοίκιο | $x_i$ | $f_i$ | $f_i x_i$ | $F_i$ |
|---|---|---|---|---|
| [300, 400) | 350 | 15 | 5250  | 15  |
| [400, 500) | 450 | 20 | 9000  | 35  |
| [500, 600) | 550 | 40 | 22000 | 75  |
| [600, 700) | 650 | 20 | 13000 | 95  |
| [700, 800) | 750 | 5  | 3750  | 100 |
| Σύνολα     |     | 100| 53000 |     |

**b. Μέση τιμή $\bar{x}$**

$$\bar{x} = \frac{\sum f_i x_i}{n} = \frac{53000}{100} = \boxed{530 \text{ €}}$$

**Standard Deviation $s$**

| $x_i$ | $x_i - \bar{x}$ | $(x_i-\bar{x})^2$ | $f_i(x_i-\bar{x})^2$ |
|---|---|---|---|
| 350 | -180 | 32400 | 486000  |
| 450 | -80  | 6400  | 128000  |
| 550 | 20   | 400   | 16000   |
| 650 | 120  | 14400 | 288000  |
| 750 | 220  | 48400 | 242000  |
| **Σύνολο** | | | **1160000** |

$$s^2 = \frac{1160000}{99} \approx 11717.17, \qquad s = \sqrt{11717.17} \approx \boxed{108.25 \text{ €}}$$

**Median $M_e$**

- $n/2 = 50$. Έχουμε $F_2 = 35 < 50 \le 75 = F_3$, άρα η διάμεσος βρίσκεται στην κλάση $[500, 600)$.

$$M_e = L + \left( \frac{\frac{n}{2} - F_{i-1}}{f_i} \right) \cdot w = 500 + \left( \frac{50 - 35}{40} \right) \cdot 100 = 500 + 37.5 = \boxed{537.50 \text{ €}}$$

**c. Εντολές R για μέση τιμή**

```r
mean(rent)
```

---

**ΘΕΜΑ 2:** Ένα σύστημα ασφαλείας έχει πιθανότητα αποτυχίας $p=0.08$ σε κάθε απόπειρα παραβίασης.
i) Αν πραγματοποιηθούν 15 ανεξάρτητες απόπειρες παραβίασης, ποια είναι η πιθανότητα να αποτύχει το σύστημα σε τουλάχιστον 3 από αυτές;
ii) Πόσες τουλάχιστον ανεξάρτητες απόπειρες παραβίασης πρέπει να γίνουν ώστε η πιθανότητα να εμφανιστεί τουλάχιστον μία αποτυχία του συστήματος να είναι μεγαλύτερη από 99%;
iii) Γράψτε τις R εντολές για τον υπολογισμό των πιθανοτήτων των ερωτημάτων i και ii.

### Solution to Problem 2

**Given Data:** $p = 0.08$

**i. $P(X \ge 3)$ για $n=15$, $X \sim B(15,\ 0.08)$**

$$P(X \ge 3) = 1 - P(X=0) - P(X=1) - P(X=2)$$

$$P(X=0) = (0.92)^{15} = 0.2863$$

$$P(X=1) = \binom{15}{1}(0.08)(0.92)^{14} = 15 \times 0.08 \times 0.3112 = 0.3726$$

$$P(X=2) = \binom{15}{2}(0.08)^2(0.92)^{13} = 105 \times 0.0064 \times 0.3383 = 0.2273$$

$$P(X \ge 3) = 1 - 0.2863 - 0.3726 - 0.2273 = \boxed{0.1138}$$

**ii. Ελάχιστο $n$ ώστε $P(X \ge 1) > 0.99$**

$$P(X \ge 1) = 1 - P(X=0) = 1 - (0.92)^n > 0.99$$

$$(0.92)^n < 0.01$$

Λαμβάνοντας λογαρίθμους:

$$n \cdot \ln(0.92) < \ln(0.01) \Rightarrow n > \frac{\ln(0.01)}{\ln(0.92)} = \frac{-4.6052}{-0.08338} \approx 55.24$$

$$n_{\min} = \boxed{56}$$

- Ο αριθμός στρογγυλοποιείται προς τα πάνω γιατί απαιτείται αυστηρή ανισότητα.

**iii. Εντολές R**

```r
# Ερώτημα i
1 - pbinom(2, size = 15, prob = 0.08)

# Ερώτημα ii
n <- 1
while ((1 - (0.92)^n) <= 0.99) n <- n + 1
n
# ή: ceiling(log(0.01) / log(0.92))
```

---

**ΘΕΜΑ 3:** Σε ένα ιατρικό κέντρο, το 2% των εξεταζόμενων έχει μια σπάνια πάθηση. Ένα διαγνωστικό τεστ ανιχνεύει την πάθηση με πιθανότητα 98% (ευαισθησία), αλλά δίνει ψευδώς θετικό αποτέλεσμα στο 3% των υγιών ατόμων (δηλαδή η ειδικότητα είναι 97%).
A. Ποια είναι η πιθανότητα ένα τυχαίο άτομο να βρεθεί θετικό στο τεστ;
B. Αν ένα άτομο βρεθεί θετικό στο τεστ, ποια είναι η πιθανότητα να πάσχει πράγματι;
C. Αν ένα άτομο βρεθεί αρνητικό στο τεστ, ποια είναι η πιθανότητα να είναι υγιές;
D. Είναι τα ενδεχόμενα «το άτομο πάσχει» και «το τεστ είναι θετικό» ανεξάρτητα; Δικαιολογήστε την απάντησή σας.

### Solution to Problem 3

**Ορισμός ενδεχομένων:**
- $P$ = άτομο πάσχει: $P(P) = 0.02$, $P(P') = 0.98$
- $T^+$ = τεστ θετικό: $P(T^+ | P) = 0.98$, $P(T^+ | P') = 0.03$

**A. Ολική πιθανότητα $P(T^+)$**

$$P(T^+) = P(T^+|P) \cdot P(P) + P(T^+|P') \cdot P(P')$$

$$= 0.98 \times 0.02 + 0.03 \times 0.98 = 0.0196 + 0.0294 = \boxed{0.0490}$$

**B. $P(P | T^+)$ — Bayes**

$$P(P \mid T^+) = \frac{P(T^+|P) \cdot P(P)}{P(T^+)} = \frac{0.98 \times 0.02}{0.0490} = \frac{0.0196}{0.0490} = \boxed{0.40}$$

- Παρόλο που η ευαισθησία είναι υψηλή (98%), η χαμηλή επιπολασμός (2%) οδηγεί σε μόλις 40% θετική προγνωστική αξία.

**C. $P(P' | T^-)$ — αρνητική προγνωστική αξία**

$$P(T^-) = 1 - P(T^+) = 1 - 0.0490 = 0.9510$$

$$P(T^- | P) = 1 - 0.98 = 0.02, \qquad P(T^- | P') = 1 - 0.03 = 0.97$$

$$P(P' \mid T^-) = \frac{P(T^-|P') \cdot P(P')}{P(T^-)} = \frac{0.97 \times 0.98}{0.9510} = \frac{0.9506}{0.9510} \approx \boxed{0.9996}$$

**D. Ανεξαρτησία;**

Για ανεξαρτησία απαιτείται: $P(P \cap T^+) = P(P) \cdot P(T^+)$

$$P(P \cap T^+) = P(T^+|P) \cdot P(P) = 0.98 \times 0.02 = 0.0196$$

$$P(P) \cdot P(T^+) = 0.02 \times 0.049 = 0.00098$$

$$0.0196 \ne 0.00098 \Rightarrow \text{τα ενδεχόμενα } \textbf{δεν είναι ανεξάρτητα.}$$

---

**ΘΕΜΑ 4:** Το βάρος των συσκευασιών καφέ που παράγει μια μηχανή ακολουθεί την Κανονική Κατανομή με μέση τιμή $\mu = 250$ γραμμάρια και τυπική απόκλιση $\sigma$ γραμμάρια.
i. Αν είναι γνωστό ότι το 5% των συσκευασιών ζυγίζει λιγότερο από 241.8 γραμμάρια, υπολογίστε την τυπική απόκλιση $\sigma$.
ii. Με την τυπική απόκλιση που βρήκατε, ποια είναι η πιθανότητα μια συσκευασία να ζυγίζει μεταξύ 245 και 255 γραμμάρια;
iii. Ποια εντολή R βρίσκει το βάρος κάτω από το οποίο βρίσκεται το 10% των συσκευασιών;
Δίνονται: Για τη standard κανονική μεταβλητή $Z$, ισχύει $\Phi(1.645) = P(Z \le 1.645) = 0.95$ και $\Phi(1.2) = 0.8849$.

### Solution to Problem 4

**Given Data:** $X \sim N(\mu=250,\ \sigma=?)$

**i. Εύρεση $\sigma$**

$$P(X < 241.8) = 0.05 \Rightarrow P\!\left(Z < \frac{241.8 - 250}{\sigma}\right) = 0.05$$

- Το 5ο εκατοστημόριο της τυπικής κανονικής αντιστοιχεί σε $z_{0.05} = -1.645$ (λόγω συμμετρίας: $\Phi(-1.645) = 0.05$).

$$\frac{241.8 - 250}{\sigma} = -1.645 \Rightarrow \frac{-8.2}{\sigma} = -1.645$$

$$\sigma = \frac{8.2}{1.645} = \boxed{5 \text{ γρ.}}$$

**ii. $P(245 \le X \le 255)$ με $\sigma = 5$**

$$z_1 = \frac{245 - 250}{5} = -1, \qquad z_2 = \frac{255 - 250}{5} = 1$$

$$P(245 \le X \le 255) = P(-1 \le Z \le 1) = 2\Phi(1) - 1$$

- Χρησιμοποιούμε $\Phi(1.2) = 0.8849$; ωστόσο εδώ χρειαζόμαστε $\Phi(1)$. Το $z=1$ δεν δίνεται άμεσα, οπότε σημειώνουμε ότι από τον εμπειρικό κανόνα $P(\mu \pm \sigma) \approx 0.6826$.

$$P(245 \le X \le 255) \approx \boxed{0.6826}$$

**iii. Εντολή R για 10ο εκατοστημόριο**

```r
qnorm(0.10, mean = 250, sd = 5)
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
