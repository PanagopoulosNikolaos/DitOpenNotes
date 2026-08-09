# Παραγοντοποιήσεις Πινάκων

Οι παραγοντοποιήσεις (αποσυνθέσεις) πινάκων εκφράζουν έναν πίνακα ως γινόμενο απλούστερων πινάκων, καθένας από τους οποίους διαθέτει ειδική δομή. Η παραγοντοποίηση LU επιλύει γραμμικά συστήματα αποδοτικά για πολλαπλά δεξιά μέλη. Η παραγοντοποίηση QR παρέχει μια αριθμητικά σταθερή προσέγγιση σε προβλήματα ελαχίστων τετραγώνων και αλγορίθμους ιδιοτιμών. Η Ανάλυση Ιδιάζουσων Τιμών (Singular Value Decomposition - SVD) είναι η πιο γενική παραγοντοποίηση, εφαρμόσιμη σε οποιονδήποτε πίνακα, και αποκαλύπτει τη θεμελιώδη γεωμετρική δομή. Η παραγοντοποίηση Cholesky, εξειδικευμένη για συμμετρικούς θετικά ορισμένους πίνακες, είναι η υπολογιστικά πιο αποδοτική.

---

## 1. Παραγοντοποίηση LU

### 1.1 Ορισμός

Για έναν τετραγωνικό πίνακα $A$, αν δεν απαιτούνται εναλλαγές γραμμών κατά την απαλοιφή Gauss:

$$
A = LU
$$

όπου ο $L$ είναι κάτω τριγωνικός με μονάδες στη διαγώνιο (unit lower triangular) και ο $U$ είναι άνω τριγωνικός.

### 1.2 Επίλυση Γραμμικών Συστημάτων

Επίλυση του $A\mathbf{x} = \mathbf{b}$ σε δύο βήματα:

1. **Εμπρός αντικατάσταση:** $L\mathbf{y} = \mathbf{b}$
2. **Πίσω αντικατάσταση:** $U\mathbf{x} = \mathbf{y}$

### 1.3 PA = LU

Αν απαιτούνται εναλλαγές γραμμών (pivoting):

$$
PA = LU
$$

όπου ο $P$ είναι ένας πίνακας μετάθεσης (permutation matrix) που κωδικοποιεί τις εναλλαγές γραμμών.

---

## 2. Παραγοντοποίηση QR

### 2.1 Ορισμός

Για έναν πίνακα $A$ μεγέθους $m \times n$ με πλήρη τάξη στηλών:

$$
A = QR
$$

όπου ο $Q$ είναι $m \times n$ με ορθοκανονικές στήλες και ο $R$ είναι $n \times n$ άνω τριγωνικός.

### 2.2 Κατασκευή μέσω Gram-Schmidt

Ο $Q$ προκύπτει από την ορθοκανονικοποίηση των στηλών του $A$. Ο $R = Q^\mathsf{T} A$ περιέχει τους συντελεστές.

### 2.3 Εφαρμογές

- Αριθμητικά σταθερά ελάχιστα τετράγωνα: επίλυση του $R\mathbf{x} = Q^\mathsf{T}\mathbf{b}$.
- Αλγόριθμος QR για τον υπολογισμό ιδιοτιμών.

---

## 3. Ανάλυση Ιδιάζουσων Τιμών (SVD)

### 3.1 Ορισμός

Για οποιονδήποτε $m \times n$ πίνακα $A$ (πραγματικό ή μιγαδικό):

$$
A = U \Sigma V^\mathsf{T}
$$

όπου:
- Ο $U$ είναι $m \times m$ ορθογώνιος πίνακας (αριστερά ιδιάζοντα διανύσματα / left singular vectors)
- Ο $V$ είναι $n \times n$ ορθογώνιος πίνακας (δεξιά ιδιάζοντα διανύσματα / right singular vectors)
- Ο $\Sigma$ είναι $m \times n$ διαγώνιος πίνακας με ιδιάζουσες τιμές $\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_r \geq 0$, όπου $r = \text{rank}(A)$.

### 3.2 Σχέση με τις Ιδιοτιμές

Οι ιδιάζουσες τιμές ικανοποιούν:

$$
\sigma_i = \sqrt{\lambda_i(A^\mathsf{T} A)} = \sqrt{\lambda_i(A A^\mathsf{T})}
$$

Οι στήλες του $V$ είναι ιδιοδιανύσματα του $A^\mathsf{T} A$. Οι στήλες του $U$ είναι ιδιοδιανύσματα του $A A^\mathsf{T}$.

### 3.3 Ψευδοαντίστροφος Πίνακας (Pseudoinverse)

Ο ψευδοαντίστροφος κατά Moore-Penrose είναι:

$$
A^+ = V \Sigma^+ U^\mathsf{T}
$$

όπου ο $\Sigma^+$ αντικαθιστά κάθε μη-μηδενική ιδιάζουσα τιμή $\sigma_i$ με το $\sigma_i^{-1}$.

### 3.4 Εφαρμογές

- **Βέλτιστη προσέγγιση τάξης-$k$ (Best rank-$k$ approximation):** Το θεώρημα Eckart-Young ορίζει ότι διατηρώντας τις $k$ μεγαλύτερες ιδιάζουσες τιμές λαμβάνουμε τη βέλτιστη προσέγγιση τάξης $k$.
- **Συμπίεση εικόνας:** αποθήκευση μόνο των μεγαλύτερων ιδιαζουσών τιμών και των διανυσμάτων τους.
- **Ανάλυση Κύριων Συνιστωσών (PCA):** ο κεντραρισμένος πίνακας δεδομένων αποσυντίθεται μέσω SVD.
- **Μείωση θορύβου (Noise reduction):** απόρριψη των μικρών ιδιαζουσών τιμών ως θόρυβο.

---

## 4. Παραγοντοποίηση Cholesky

### 4.1 Ορισμός

Για έναν συμμετρικό θετικά ορισμένο πίνακα $A$:

$$
A = LL^\mathsf{T}
$$

όπου ο $L$ είναι κάτω τριγωνικός με θετικά στοιχεία στη διαγώνιο.

### 4.2 Υπολογιστικό Πλεονέκτημα

Η μέθοδος Cholesky είναι περίπου δύο φορές πιο αποδοτική από την LU για συμμετρικούς θετικά ορισμένους πίνακες, απαιτώντας περίπου $\frac{n^3}{3}$ πράξεις κινητής υποδιαστολής (flops) έναντι $\frac{2n^3}{3}$ για την LU.

### 4.3 Ύπαρξη

Ο $A$ είναι συμμετρικός θετικά ορισμένος αν και μόνο αν υπάρχει η παραγοντοποίηση $A = LL^\mathsf{T}$ με τον $L$ να έχει θετικά διαγώνια στοιχεία.

---

## Λυμένες Ασκήσεις

### Άσκηση 1: Παραγοντοποίηση LU (2x2)

**Πρόβλημα:**
Βρείτε την παραγοντοποίηση LU του $A = \begin{bmatrix} 3 & 1 \\ 6 & 5 \end{bmatrix}$ και λύστε το $A\mathbf{x} = \begin{pmatrix} 4 \\ 14 \end{pmatrix}$.

**Λύση:**
Απαλοιφή: αφαιρούμε $2 \times$ τη 1η γραμμή από τη 2η γραμμή (πολλαπλασιαστής $\ell_{21} = 2$):

$$
U = \begin{bmatrix} 3 & 1 \\ 0 & 3 \end{bmatrix},\quad
L = \begin{bmatrix} 1 & 0 \\ 2 & 1 \end{bmatrix}
$$

Εμπρός αντικατάσταση $L\mathbf{y} = \mathbf{b}$:

$$
\begin{bmatrix} 1 & 0 \\ 2 & 1 \end{bmatrix}
\begin{pmatrix} y_1 \\ y_2 \end{pmatrix}
= \begin{pmatrix} 4 \\ 14 \end{pmatrix}
\Rightarrow y_1 = 4,\; 2\cdot4 + y_2 = 14 \Rightarrow y_2 = 6
$$

Πίσω αντικατάσταση $U\mathbf{x} = \mathbf{y}$:

$$
\begin{bmatrix} 3 & 1 \\ 0 & 3 \end{bmatrix}
\begin{pmatrix} x_1 \\ x_2 \end{pmatrix}
= \begin{pmatrix} 4 \\ 6 \end{pmatrix}
\Rightarrow x_2 = 2,\; 3x_1 + 2 = 4 \Rightarrow x_1 = \frac{2}{3}
$$

**Λύση:** $\mathbf{x} = \left(\frac{2}{3}, 2\right)$.

---

### Άσκηση 2: LU με Πολλαπλά Δεξιά Μέλη

**Πρόβλημα:**
Χρησιμοποιώντας τον $LU$ από την Άσκηση 1, λύστε το $A\mathbf{x} = \begin{pmatrix} 1 \\ 5 \end{pmatrix}$.

**Λύση:**
Εμπρός: $y_1 = 1$, $2\cdot1 + y_2 = 5 \Rightarrow y_2 = 3$.

Πίσω: $x_2 = 1$, $3x_1 + 1 = 1 \Rightarrow x_1 = 0$.

**Λύση:** $\mathbf{x} = (0, 1)$.

---

### Άσκηση 3: Παραγοντοποίηση QR (2x2)

**Πρόβλημα:**
Βρείτε την παραγοντοποίηση QR του $A = \begin{bmatrix} 1 & 2 \\ 2 & 1 \end{bmatrix}$.

**Λύση:**
Στήλες: $\mathbf{a}_1 = (1, 2)$, $\mathbf{a}_2 = (2, 1)$.

Gram-Schmidt: $\mathbf{v}_1 = \mathbf{a}_1 = (1, 2)$. $\|\mathbf{v}_1\| = \sqrt{1^2 + 2^2} = \sqrt{5}$.

$\mathbf{q}_1 = \left(\frac{1}{\sqrt{5}}, \frac{2}{\sqrt{5}}\right)$.

$\text{proj}_{\mathbf{v}_1}(\mathbf{a}_2) = \frac{(2, 1) \cdot (1, 2)}{5} (1, 2) = \frac{4}{5}(1, 2) = \left(\frac{4}{5}, \frac{8}{5}\right)$.

$\mathbf{v}_2 = (2, 1) - \left(\frac{4}{5}, \frac{8}{5}\right) = \left(\frac{6}{5}, -\frac{3}{5}\right)$.

$\|\mathbf{v}_2\| = \sqrt{\frac{36}{25} + \frac{9}{25}} = \sqrt{\frac{45}{25}} = \frac{3\sqrt{5}}{5}$.

$\mathbf{q}_2 = \frac{1}{3\sqrt{5}/5} \left(\frac{6}{5}, -\frac{3}{5}\right) = \left(\frac{2}{\sqrt{5}}, -\frac{1}{\sqrt{5}}\right)$.

$Q = \begin{bmatrix} \frac{1}{\sqrt{5}} & \frac{2}{\sqrt{5}} \\ \frac{2}{\sqrt{5}} & -\frac{1}{\sqrt{5}} \end{bmatrix}$.

$R = Q^\mathsf{T} A = \begin{bmatrix} \|v_1\| & \mathbf{q}_1 \cdot \mathbf{a}_2 \\ 0 & \|v_2\| \end{bmatrix}
= \begin{bmatrix} \sqrt{5} & \frac{4}{\sqrt{5}} \\ 0 & \frac{3\sqrt{5}}{5} \end{bmatrix}$.

---

### Άσκηση 4: SVD Πίνακα 2x2

**Πρόβλημα:**
Βρείτε την SVD του $A = \begin{bmatrix} 3 & 0 \\ 0 & 1 \end{bmatrix}$.

**Λύση:**
Ο $A$ είναι ήδη διαγώνιος. Υπολογίζουμε $A^\mathsf{T} A = \begin{bmatrix} 9 & 0 \\ 0 & 1 \end{bmatrix}$.

Ιδιοτιμές του $A^\mathsf{T} A$: $\lambda_1 = 9$, $\lambda_2 = 1$.

Ιδιάζουσες τιμές: $\sigma_1 = 3$, $\sigma_2 = 1$.

$V = I$ (τα ιδιοδιανύσματα του $A^\mathsf{T} A$ είναι τα κανονικά διανύσματα βάσης).

$U = I$ (τα ιδιοδιανύσματα του $A A^\mathsf{T} = A^2$ είναι επίσης τα κανονικά διανύσματα βάσης).

$\Sigma = \begin{bmatrix} 3 & 0 \\ 0 & 1 \end{bmatrix}$.

SVD: $A = I \cdot \Sigma \cdot I^\mathsf{T}$, που είναι τετριμμένα $A = \begin{bmatrix} 3 & 0 \\ 0 & 1 \end{bmatrix}$.

---

### Άσκηση 5: SVD Μη-Τετραγωνικού Πίνακα

**Πρόβλημα:**
Βρείτε την SVD του $A = \begin{bmatrix} 1 & 0 \\ 0 & 1 \\ 1 & 1 \end{bmatrix}$.

**Λύση:**
Ο $A$ είναι $3 \times 2$. Υπολογίζουμε $A^\mathsf{T} A = \begin{bmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \end{bmatrix}
\begin{bmatrix} 1 & 0 \\ 0 & 1 \\ 1 & 1 \end{bmatrix}
= \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$.

Ιδιοτιμές του $A^\mathsf{T} A$: $\lambda_1 = 3$, $\lambda_2 = 1$. Ιδιάζουσες τιμές: $\sigma_1 = \sqrt{3}$, $\sigma_2 = 1$.

Ιδιοδιανύσματα του $A^\mathsf{T} A$: για $\lambda = 3$, $\mathbf{v}_1 = \left(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right)$· για $\lambda = 1$, $\mathbf{v}_2 = \left(\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}\right)$.

$V = \begin{bmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \end{bmatrix}$.

Υπολογίζουμε τον $U$ από τη σχέση $U = A V \Sigma^{-1}$:

$\mathbf{u}_1 = \frac{1}{\sqrt{3}} A \mathbf{v}_1 = \frac{1}{\sqrt{3}} \begin{bmatrix} 1 & 0 \\ 0 & 1 \\ 1 & 1 \end{bmatrix}
\begin{pmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{pmatrix}
= \frac{1}{\sqrt{3}} \begin{pmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \\ \frac{2}{\sqrt{2}} \end{pmatrix}
= \begin{pmatrix} \frac{1}{\sqrt{6}} \\ \frac{1}{\sqrt{6}} \\ \frac{2}{\sqrt{6}} \end{pmatrix}$.

$\mathbf{u}_2 = \frac{1}{1} A \mathbf{v}_2 = \begin{bmatrix} 1 & 0 \\ 0 & 1 \\ 1 & 1 \end{bmatrix}
\begin{pmatrix} \frac{1}{\sqrt{2}} \\ -\frac{1}{\sqrt{2}} \end{pmatrix}
= \begin{pmatrix} \frac{1}{\sqrt{2}} \\ -\frac{1}{\sqrt{2}} \\ 0 \end{pmatrix}$.

Το $\mathbf{u}_3$ είναι ένα οποιοδήποτε μοναδιαίο διάνυσμα ορθογώνιο στα $\mathbf{u}_1$ και $\mathbf{u}_2$· παρατηρούμε ότι $\mathbf{u}_3 = \left(\frac{1}{\sqrt{3}}, \frac{1}{\sqrt{3}}, -\frac{1}{\sqrt{3}}\right)$.

$\Sigma = \begin{bmatrix} \sqrt{3} & 0 \\ 0 & 1 \\ 0 & 0 \end{bmatrix}$.

---

### Άσκηση 6: Ψευδοαντίστροφος Πίνακας

**Πρόβλημα:**
Βρείτε τον ψευδοαντίστροφο του $A = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$.

**Λύση:**
Ο $A$ έχει τάξη 1. $A^\mathsf{T} A = \begin{bmatrix} 2 & 2 \\ 2 & 2 \end{bmatrix}$ με ιδιοτιμές $\lambda_1 = 4$, $\lambda_2 = 0$.

Ιδιάζουσες τιμές: $\sigma_1 = 2$, $\sigma_2 = 0$.

$V$: για $\lambda = 4$, $\mathbf{v}_1 = \left(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right)$· για $\lambda = 0$, $\mathbf{v}_2 = \left(\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}\right)$.

$U$: $\mathbf{u}_1 = \frac{1}{2} A \mathbf{v}_1 = \frac{1}{2} \begin{pmatrix} \sqrt{2} \\ \sqrt{2} \end{pmatrix} = \left(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right)$.
$\mathbf{u}_2 = \left(\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}\right)$.

$\Sigma^+ = \begin{bmatrix} \frac{1}{2} & 0 \\ 0 & 0 \end{bmatrix}$.

$A^+ = V \Sigma^+ U^\mathsf{T} = \begin{bmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \end{bmatrix}
\begin{bmatrix} \frac{1}{2} & 0 \\ 0 & 0 \end{bmatrix}
\begin{bmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \end{bmatrix}
= \frac{1}{4} \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$.

Έλεγχος: $A A^+ A = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}
\frac{1}{4} \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}
\begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}
= \frac{1}{4} \begin{bmatrix} 2 & 2 \\ 2 & 2 \end{bmatrix}
\begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}
= \frac{1}{4} \begin{bmatrix} 4 & 4 \\ 4 & 4 \end{bmatrix}
= \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix} = A$.

---

### Άσκηση 7: Παραγοντοποίηση Cholesky

**Πρόβλημα:**
Βρείτε την παραγοντοποίηση Cholesky του $A = \begin{bmatrix} 4 & 2 \\ 2 & 5 \end{bmatrix}$.

**Λύση:**
Έστω $L = \begin{bmatrix} \ell_{11} & 0 \\ \ell_{21} & \ell_{22} \end{bmatrix}$ τέτοιος ώστε $LL^\mathsf{T} = A$.

$$
\begin{bmatrix} \ell_{11}^2 & \ell_{11}\ell_{21} \\ \ell_{11}\ell_{21} & \ell_{21}^2 + \ell_{22}^2 \end{bmatrix}
= \begin{bmatrix} 4 & 2 \\ 2 & 5 \end{bmatrix}
$$

$\ell_{11}^2 = 4 \Rightarrow \ell_{11} = 2$ (θετικό).

$\ell_{11}\ell_{21} = 2 \Rightarrow 2\ell_{21} = 2 \Rightarrow \ell_{21} = 1$.

$\ell_{21}^2 + \ell_{22}^2 = 5 \Rightarrow 1 + \ell_{22}^2 = 5 \Rightarrow \ell_{22}^2 = 4 \Rightarrow \ell_{22} = 2$.

$L = \begin{bmatrix} 2 & 0 \\ 1 & 2 \end{bmatrix}$, και $LL^\mathsf{T} = \begin{bmatrix} 2 & 0 \\ 1 & 2 \end{bmatrix}
\begin{bmatrix} 2 & 1 \\ 0 & 2 \end{bmatrix}
= \begin{bmatrix} 4 & 2 \\ 2 & 5 \end{bmatrix} = A$.

---

### Άσκηση 8: Προσέγγιση Τάξης-1 μέσω SVD

**Πρόβλημα:**
Βρείτε τη βέλτιστη προσέγγιση τάξης-1 του $A = \begin{bmatrix} 3 & 0 \\ 0 & 1 \end{bmatrix}$.

**Λύση:**
Από την Άσκηση 4, η SVD είναι $A = U \Sigma V^\mathsf{T}$ με $\sigma_1 = 3$, $\sigma_2 = 1$.

Η βέλτιστη προσέγγιση τάξης-1 χρησιμοποιεί μόνο το $\sigma_1$:

$$
A_1 = \sigma_1 \mathbf{u}_1 \mathbf{v}_1^\mathsf{T}
$$

$U = I$, οπότε $\mathbf{u}_1 = (1, 0)^\mathsf{T}$. $V = I$, οπότε $\mathbf{v}_1 = (1, 0)^\mathsf{T}$.

$$
A_1 = 3 \begin{pmatrix} 1 \\ 0 \end{pmatrix}
\begin{pmatrix} 1 & 0 \end{pmatrix}
= \begin{bmatrix} 3 & 0 \\ 0 & 0 \end{bmatrix}
$$

Αυτή η προσέγγιση συλλαμβάνει την κυρίαρχη κατεύθυνση του μετασχηματισμού.

---

## Συμβουλή Εξετάσεων: Επιλογή της Κατάλληλης Παραγοντοποίησης

Όταν λύνετε ένα πρόβλημα, επιλέξτε την παραγοντοποίηση με βάση τη δομή του πίνακα:

| Τύπος Πίνακα | Βέλτιστη Παραγοντοποίηση | Αιτιολογία |
| :--- | :--- | :--- |
| Γενικός τετραγωνικός | LU | Πιο αποδοτική για μεμονωμένη επίλυση |
| Πολλαπλά δεξιά μέλη | LU | Επαναχρησιμοποίηση $L$ και $U$ |
| Συμμετρικός θετικά ορισμένος | Cholesky | ~2x ταχύτερη από την LU |
| Υπερορισμένος ($m > n$) | QR | Αριθμητικά σταθερά ελάχιστα τετράγωνα |
| Οποιοσδήποτε πίνακας | SVD | Η πιο γενική· αποκαλύπτει τάξη, μηδενοχώρο, χώρο στηλών |
| Ανάλυση δεδομένων | SVD | PCA, προσέγγιση χαμηλής τάξης (low-rank) |

---