# Ευκλείδιοι Διανυσματικοί Χώροι

Τα διανύσματα στον $\mathbb{R}^n$ παρέχουν τη γεωμετρική θεμελίωση της γραμμικής άλγεβρας. Πράξεις όπως η πρόσθεση, ο βαθμωτός πολλαπλασιασμός, το εσωτερικό (βαθμωτό) γινόμενο και το εξωτερικό γινόμενο (γινόμενο σταυρού) επιτρέπουν τη μέτρηση μηκών, γωνιών και εμβαδών. Οι γραμμικοί μετασχηματισμοί μεταξύ Ευκλείδιων χώρων αναπαρίστανται από πίνακες, συνδέοντας αλγεβρικές πράξεις με τη γεωμετρική διαίσθηση. Αυτή η ενότητα καλύπτει τις βασικές ιδιότητες του $\mathbb{R}^n$, συμπεριλαμβανομένων των νορμών (μέτρων), της ορθογωνιότητας, των προβολών και των γεωμετρικών μετασχηματισμών όπως η στροφή, η ανάκλαση και η διάτμηση.

---

## 1. Βασικοί Ορισμοί

### 1.1 Διανύσματα στον $\mathbb{R}^n$

Ένα **διάνυσμα** στον $\mathbb{R}^n$ είναι μια διατεταγμένη $n$-άδα πραγματικών αριθμών:

$$
\mathbf{v} = \begin{pmatrix} v_1 & v_2 & \cdots & v_n \end{pmatrix}^\mathsf{T}
$$

Τα **κανονικά (τυπικά) διανύσματα βάσης** στον $\mathbb{R}^n$ είναι:

$$
\mathbf{e}_1 = \begin{pmatrix}1&0&\cdots&0\end{pmatrix}^\mathsf{T},\;
\mathbf{e}_2 = \begin{pmatrix}0&1&\cdots&0\end{pmatrix}^\mathsf{T},\;
\ldots,\;
\mathbf{e}_n = \begin{pmatrix}0&0&\cdots&1\end{pmatrix}^\mathsf{T}
$$

### 1.2 Πράξεις Διανυσμάτων

- **Πρόσθεση:** $\mathbf{u} + \mathbf{v} = (u_1+v_1,\; u_2+v_2,\; \ldots,\; u_n+v_n)^\mathsf{T}$
- **Βαθμωτός πολλαπλασιασμός:** $c\mathbf{v} = (c v_1,\; c v_2,\; \ldots,\; c v_n)^\mathsf{T}$

### 1.3 Νόρμα (Μέτρο)

Η **Ευκλείδια νόρμα** (μήκος / μέτρο) του $\mathbf{v} \in \mathbb{R}^n$ είναι:

$$
\|\mathbf{v}\| = \sqrt{v_1^2 + v_2^2 + \cdots + v_n^2}
$$

Ένα **μοναδιαίο διάνυσμα** ικανοποιεί $\|\mathbf{v}\| = 1$. Κάθε μη-μηδενικό διάνυσμα μπορεί να κανονικοποιηθεί:

$$
\hat{\mathbf{v}} = \frac{\mathbf{v}}{\|\mathbf{v}\|}
$$

---

## 2. Εσωτερικό Γινόμενο (Dot Product)

### 2.1 Ορισμός

Το **εσωτερικό γινόμενο** των $\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$ είναι:

$$
\mathbf{u} \cdot \mathbf{v} = \sum_{i=1}^{n} u_i v_i = \|\mathbf{u}\| \|\mathbf{v}\| \cos\theta
$$

όπου $\theta$ είναι η γωνία μεταξύ των $\mathbf{u}$ και $\mathbf{v}$.

### 2.2 Ιδιότητες

- $\mathbf{u} \cdot \mathbf{v} = \mathbf{v} \cdot \mathbf{u}$ (αντιμεταθετική)
- $\mathbf{u} \cdot (\mathbf{v} + \mathbf{w}) = \mathbf{u} \cdot \mathbf{v} + \mathbf{u} \cdot \mathbf{w}$ (επιμεριστική)
- $c(\mathbf{u} \cdot \mathbf{v}) = (c\mathbf{u}) \cdot \mathbf{v} = \mathbf{u} \cdot (c\mathbf{v})$
- $\mathbf{v} \cdot \mathbf{v} = \|\mathbf{v}\|^2$

### 2.3 Ορθογωνιότητα

Δύο διανύσματα είναι **ορθογώνια** (κάθετα) αν $\mathbf{u} \cdot \mathbf{v} = 0$.

### 2.4 Προβολή

Η **βαθμωτή προβολή** του $\mathbf{u}$ πάνω στο $\mathbf{v}$ είναι:

$$
\text{comp}_{\mathbf{v}}(\mathbf{u}) = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{v}\|}
$$

Η **διανυσματική προβολή** του $\mathbf{u}$ πάνω στο $\mathbf{v}$ είναι:

$$
\text{proj}_{\mathbf{v}}(\mathbf{u}) = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{v}\|^2}\, \mathbf{v}
$$

---

## 3. Εξωτερικό Γινόμενο (Cross Product στον $\mathbb{R}^3$)

### 3.1 Ορισμός

Για $\mathbf{u}, \mathbf{v} \in \mathbb{R}^3$:

$$
\mathbf{u} \times \mathbf{v} = \begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
u_1 & u_2 & u_3 \\
v_1 & v_2 & v_3
\end{vmatrix}
= \begin{pmatrix}
u_2 v_3 - u_3 v_2 \\
u_3 v_1 - u_1 v_3 \\
u_1 v_2 - u_2 v_1
\end{pmatrix}
$$

### 3.2 Ιδιότητες

- Το $\mathbf{u} \times \mathbf{v}$ είναι ορθογώνιο και στο $\mathbf{u}$ και στο $\mathbf{v}$.
- $\|\mathbf{u} \times \mathbf{v}\| = \|\mathbf{u}\| \|\mathbf{v}\| \sin\theta$
- $\mathbf{u} \times \mathbf{v} = -(\mathbf{v} \times \mathbf{u})$ (αντι-αντιμεταθετική)
- Το μέτρο ισούται με το εμβαδόν του παραλληλογράμμου που σχηματίζεται από τα $\mathbf{u}$ και $\mathbf{v}$.

### 3.3 Εφαρμογές

- Υπολογισμός **κάθετου (κανονικού) διανύσματος** σε ένα επίπεδο.
- Υπολογισμός του **εμβαδού** παραλληλογράμμου: $\text{Εμβαδόν} = \|\mathbf{u} \times \mathbf{v}\|$.
- Υπολογισμός του **όγκου** παραλληλεπιπέδου: $V = |\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w})|$ (μικτό/βαθμωτό τριπλό γινόμενο).

---

## 4. Γραμμικοί Μετασχηματισμοί $\mathbb{R}^n \to \mathbb{R}^m$

### 4.1 Ορισμός

Μια απεικόνιση $T: \mathbb{R}^n \to \mathbb{R}^m$ είναι **γραμμική** αν για όλα τα $\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$ και βαθμωτά $c$:

1. $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$
2. $T(c\mathbf{u}) = c\,T(\mathbf{u})$

### 4.2 Αναπαράσταση με Πίνακα

Κάθε γραμμικός μετασχηματισμός $T$ αναπαρίσταται από έναν πίνακα $A$ μεγέθους $m \times n$ τέτοιον ώστε $T(\mathbf{x}) = A\mathbf{x}$. Η στήλη $j$ του $A$ είναι το $T(\mathbf{e}_j)$.

### 4.3 Πυρήνας και Εικόνα

- **Πυρήνας (Kernel):** $\ker(T) = \{\mathbf{x} \in \mathbb{R}^n \mid T(\mathbf{x}) = \mathbf{0}\}$
- **Εικόνα (Image):** $\text{Im}(T) = \{T(\mathbf{x}) \mid \mathbf{x} \in \mathbb{R}^n\}$
- $\dim(\ker(T)) + \dim(\text{Im}(T)) = n$

---

## Λυμένες Ασκήσεις

### Άσκηση 1: Νόρμα και Μοναδιαίο Διάνυσμα

**Πρόβλημα:**
Δίνεται το $\mathbf{v} = (3, -1, 2)$. Βρείτε το $\|\mathbf{v}\|$ και το μοναδιαίο διάνυσμα στην κατεύθυνση του $\mathbf{v}$.

**Λύση:**
$$
\|\mathbf{v}\| = \sqrt{3^2 + (-1)^2 + 2^2} = \sqrt{9 + 1 + 4} = \sqrt{14}
$$

$$
\hat{\mathbf{v}} = \frac{1}{\sqrt{14}} (3, -1, 2) = \left(\frac{3}{\sqrt{14}}, -\frac{1}{\sqrt{14}}, \frac{2}{\sqrt{14}}\right)
$$

---

### Άσκηση 2: Εσωτερικό Γινόμενο και Γωνία

**Πρόβλημα:**
Βρείτε τη γωνία μεταξύ των $\mathbf{u} = (1, 2, -1)$ και $\mathbf{v} = (2, 0, 3)$.

**Λύση:**
$$
\mathbf{u} \cdot \mathbf{v} = 1 \cdot 2 + 2 \cdot 0 + (-1) \cdot 3 = 2 + 0 - 3 = -1
$$

$$
\|\mathbf{u}\| = \sqrt{1 + 4 + 1} = \sqrt{6},\quad
\|\mathbf{v}\| = \sqrt{4 + 0 + 9} = \sqrt{13}
$$

$$
\cos\theta = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\| \|\mathbf{v}\|} = \frac{-1}{\sqrt{6} \cdot \sqrt{13}} = -\frac{1}{\sqrt{78}}
$$

$$
\theta = \arccos\left(-\frac{1}{\sqrt{78}}\right) \approx 96.5^\circ
$$

Καθώς $\theta > 90^\circ$, τα διανύσματα δείχνουν σε γενικά αντίθετες κατευθύνσεις.

---

### Άσκηση 3: Διανυσματική Προβολή

**Πρόβλημα:**
Βρείτε την προβολή του $\mathbf{u} = (4, 1)$ πάνω στο $\mathbf{v} = (2, 3)$.

**Λύση:**
$$
\mathbf{u} \cdot \mathbf{v} = 4 \cdot 2 + 1 \cdot 3 = 8 + 3 = 11
$$

$$
\|\mathbf{v}\|^2 = 2^2 + 3^2 = 4 + 9 = 13
$$

$$
\text{proj}_{\mathbf{v}}(\mathbf{u}) = \frac{11}{13} (2, 3) = \left(\frac{22}{13}, \frac{33}{13}\right)
$$

Το συνιστών διάνυσμα του $\mathbf{u}$ που είναι ορθογώνιο στο $\mathbf{v}$ είναι:

$$
\mathbf{u} - \text{proj}_{\mathbf{v}}(\mathbf{u}) = \left(4 - \frac{22}{13}, \; 1 - \frac{33}{13}\right) = \left(\frac{30}{13}, -\frac{20}{13}\right)
$$

Επαλήθευση: το εσωτερικό γινόμενο της ορθογώνιας συνιστώσας με το $\mathbf{v}$ πρέπει να είναι μηδέν:

$$
\frac{30}{13} \cdot 2 + \left(-\frac{20}{13}\right) \cdot 3 = \frac{60}{13} - \frac{60}{13} = 0
$$

---

### Άσκηση 4: Εξωτερικό Γινόμενο

**Πρόβλημα:**
Υπολογίστε το $\mathbf{u} \times \mathbf{v}$ για $\mathbf{u} = (1, 2, 3)$ και $\mathbf{v} = (4, 5, 6)$.

**Λύση:**

$$
\mathbf{u} \times \mathbf{v} = \begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
1 & 2 & 3 \\
4 & 5 & 6
\end{vmatrix}
= \mathbf{i}(2 \cdot 6 - 3 \cdot 5) - \mathbf{j}(1 \cdot 6 - 3 \cdot 4) + \mathbf{k}(1 \cdot 5 - 2 \cdot 4)
$$

$$
= \mathbf{i}(12 - 15) - \mathbf{j}(6 - 12) + \mathbf{k}(5 - 8)
= (-3, 6, -3)
$$

Το εμβαδόν του παραλληλογράμμου που σχηματίζεται από τα $\mathbf{u}$ και $\mathbf{v}$ είναι:

$$
\|\mathbf{u} \times \mathbf{v}\| = \sqrt{(-3)^2 + 6^2 + (-3)^2} = \sqrt{9 + 36 + 9} = \sqrt{54} = 3\sqrt{6}
$$

---

### Άσκηση 5: Έλεγχος Ορθογωνιότητας

**Πρόβλημα:**
Determina αν τα $\mathbf{u} = (2, -1, 3)$ και $\mathbf{v} = (1, 5, 1)$ είναι ορθογώνια.

**Λύση:**
$$
\mathbf{u} \cdot \mathbf{v} = 2 \cdot 1 + (-1) \cdot 5 + 3 \cdot 1 = 2 - 5 + 3 = 0
$$

Αφού το εσωτερικό γινόμενο είναι μηδέν, τα $\mathbf{u}$ και $\mathbf{v}$ είναι ορθογώνια.

---

### Άσκηση 6: Πίνακας Γραμμικού Μετασχηματισμού

**Πρόβλημα:**
Βρείτε τον πίνακα $A$ του γραμμικού μετασχηματισμού $T: \mathbb{R}^2 \to \mathbb{R}^3$ που ορίζεται από:

$$
T(x_1, x_2) = (2x_1 - x_2,\; x_1 + 3x_2,\; -x_1 + 4x_2)
$$

**Λύση:**
Ο πίνακας $A$ είναι $3 \times 2$. Η στήλη 1 είναι το $T(\mathbf{e}_1) = T(1, 0) = (2, 1, -1)^\mathsf{T}$.
Η στήλη 2 είναι το $T(\mathbf{e}_2) = T(0, 1) = (-1, 3, 4)^\mathsf{T}$.

$$
A = \begin{bmatrix}
2 & -1 \\
1 & 3 \\
-1 & 4
\end{bmatrix}
$$

Επαλήθευση: $A\mathbf{x} = \begin{bmatrix} 2 & -1 \\ 1 & 3 \\ -1 & 4 \end{bmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} 2x_1 - x_2 \\ x_1 + 3x_2 \\ -x_1 + 4x_2 \end{pmatrix}$, που συμφωνεί με το $T$.

---

### Άσκηση 7: Διαστάσεις Πυρήνα και Εικόνας

**Πρόβλημα:**
Για τον μετασχηματισμό $T: \mathbb{R}^4 \to \mathbb{R}^3$ με πίνακα $A = \begin{bmatrix} 1 & 2 & 1 & 0 \\ 0 & 1 & -1 & 1 \\ 0 & 0 & 0 & 0 \end{bmatrix}$, βρείτε τη $\dim(\ker(T))$ και τη $\dim(\text{Im}(T))$.

**Λύση:**
Αναγωγή του $A$ σε REF (είναι ήδη σε REF). Στήλες pivots: στήλες 1 και 2. Άρα $\text{rank}(A) = 2$.

$\dim(\text{Im}(T)) = \text{rank}(A) = 2$.

Από το θεώρημα rank-nullity: $\dim(\ker(T)) = n - \text{rank}(A) = 4 - 2 = 2$.

Ο πυρήνας έχει διάσταση 2, που σημαίνει ότι ο μηδενοχώρος (null space) περιέχει δύο ελεύθερες μεταβλητές.

---

### Άσκηση 8: Εμβαδόν μέσω Εξωτερικού Γινομένου

**Πρόβλημα:**
Βρείτε το εμβαδόν του τριγώνου με κορυφές $P(1, 0, 1)$, $Q(2, 3, 1)$, $R(0, 1, 4)$.

**Λύση:**
Δύο διανύσματα ακμών:

$$
\mathbf{u} = \overrightarrow{PQ} = (2-1, 3-0, 1-1) = (1, 3, 0)
$$

$$
\mathbf{v} = \overrightarrow{PR} = (0-1, 1-0, 4-1) = (-1, 1, 3)
$$

Εξωτερικό γινόμενο:

$$
\mathbf{u} \times \mathbf{v} = \begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
1 & 3 & 0 \\
-1 & 1 & 3
\end{vmatrix}
= \mathbf{i}(3 \cdot 3 - 0 \cdot 1) - \mathbf{j}(1 \cdot 3 - 0 \cdot (-1)) + \mathbf{k}(1 \cdot 1 - 3 \cdot (-1))
$$

$$
= \mathbf{i}(9 - 0) - \mathbf{j}(3 - 0) + \mathbf{k}(1 + 3) = (9, -3, 4)
$$

Εμβαδόν παραλληλογράμμου: $\|\mathbf{u} \times \mathbf{v}\| = \sqrt{81 + 9 + 16} = \sqrt{106}$.

Εμβαδόν τριγώνου: $\frac{1}{2} \sqrt{106}$.

---

## Συμβουλή Εξετάσεων: Αποσύνθεση Διανύσματος σε Παράλληλη και Ορθογώνια Συνιστώσα

Δεδομένου ενός διανύσματος $\mathbf{u}$ και μιας κατεύθυνσης $\mathbf{v}$, η αποσύνθεση

$$
\mathbf{u} = \text{proj}_{\mathbf{v}}(\mathbf{u}) + (\mathbf{u} - \text{proj}_{\mathbf{v}}(\mathbf{u}))
$$

διαχωρίζει το $\mathbf{u}$ σε ένα τμήμα παράλληλο στο $\mathbf{v}$ και ένα τμήμα ορθογώνιο στο $\mathbf{v}$. Αυτή η αποσύνθεση είναι κεντρικής σημασίας στην ορθογωνιοποίηση Gram-Schmidt και στα προβλήματα ελαχίστων τετραγώνων. Στις εξετάσεις, πάντα να επαληθεύετε την ορθογωνιότητα ελέγχοντας ότι το εσωτερικό γινόμενο του υπολοίπου με το $\mathbf{v}$ είναι μηδέν.

---