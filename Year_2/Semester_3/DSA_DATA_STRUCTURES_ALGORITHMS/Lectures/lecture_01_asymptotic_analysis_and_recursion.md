# Διάλεξη 1: Ασυμπτωτική Ανάλυση Πολυπλοκότητας και Αναδρομή

## 1. Εισαγωγή στην Ανάλυση Αλγορίθμων
Η ανάλυση αλγορίθμων εκτιμά τους υπολογιστικούς πόρους (χρόνο εκτέλεσης και χώρο μνήμης) που απαιτεί ένας αλγόριθμος ως συνάρτηση του μεγέθους της εισόδου $n$.

---

## 2. Ασυμπτωτικοί Συμβολισμοί (Asymptotic Notations)

### 2.1 Συμβολισμός Big-O ($O$) — Άνω Φράγμα
Ορίζει το χειρότερο δυνατό ρυθμό αύξησης (worst-case upper bound):
$$f(n) = O(g(n)) \iff \exists c > 0, n_0 \ge 1 : \forall n \ge n_0, \quad 0 \le f(n) \le c \cdot g(n)$$

### 2.2 Συμβολισμός Big-Omega ($\Omega$) — Κάτω Φράγμα
Ορίζει το καλύτερο δυνατό ρυθμό αύξησης (best-case lower bound):
$$f(n) = \Omega(g(n)) \iff \exists c > 0, n_0 \ge 1 : \forall n \ge n_0, \quad 0 \le c \cdot g(n) \le f(n)$$

### 2.3 Συμβολισμός Big-Theta ($\Theta$) — Ακριβές Φράγμα
Ορίζει ασυμπτωτικά σφιχτό φράγμα (tight bound):
$$f(n) = \Theta(g(n)) \iff f(n) = O(g(n)) \quad \text{και} \quad f(n) = \Omega(g(n))$$

---

## 3. Συνήθεις Τάξεις Πολυπλοκότητας
| Τάξη | Ονομασία | Παράδειγμα Αλγορίθμου |
|---|---|---|
| $O(1)$ | Σταθερός (Constant) | Προσπέλαση στοιχείου πίνακα με δείκτη, Push/Pop σε στοίβα |
| $O(\log n)$ | Λογαριθμικός (Logarithmic) | Δυαδική Αναζήτηση (Binary Search) |
| $O(n)$ | Γραμμικός (Linear) | Γραμμική Αναζήτηση, Διάσχιση λίστας |
| $O(n \log n)$ | Γραμμο-λογαριθμικός (Linearithmic) | Merge Sort, Heap Sort, Quick Sort (μέση περίπτωση) |
| $O(n^2)$ | Τετραγωνικός (Quadratic) | Bubble Sort, Selection Sort, Insertion Sort |
| $O(2^n)$ | Εκθετικός (Exponential) | Αφελής αναδρομικός υπολογισμός Fibonacci, Πρόβλημα Σακιδίου (Brute force) |

---

## 4. Επίλυση Αναδρομικών Σχέσεων (Recurrence Relations)

### 4.1 Θεώρημα Master (Master Theorem)
Για αναδρομές της μορφής:
$$T(n) = a T\left(\frac{n}{b}\right) + f(n), \quad a \ge 1, b > 1$$
Συγκρίνουμε το $f(n)$ με το $n^{\log_b a}$:
1. **Περίπτωση 1:** Αν $f(n) = O(n^{\log_b a - \epsilon})$ για $\epsilon > 0$, τότε $T(n) = \Theta(n^{\log_b a})$.
2. **Περίπτωση 2:** Αν $f(n) = \Theta(n^{\log_b a} \log^k n)$ για $k \ge 0$, τότε $T(n) = \Theta(n^{\log_b a} \log^{k+1} n)$.
3. **Περίπτωση 3:** Αν $f(n) = \Omega(n^{\log_b a + \epsilon})$ για $\epsilon > 0$ και ισχύει η συνθήκη κανονικότητας $a f(n/b) \le c f(n)$ για $c < 1$, τότε $T(n) = \Theta(f(n))$.

### Παράδειγμα (Merge Sort):
$$T(n) = 2 T(n/2) + \Theta(n)$$
- $a = 2, b = 2 \implies n^{\log_2 2} = n^1 = n$.
- Επειδή $f(n) = \Theta(n) = \Theta(n^{\log_2 2})$, ισχύει η **Περίπτωση 2** (με $k=0$):
$$T(n) = \Theta(n \log n)$$

