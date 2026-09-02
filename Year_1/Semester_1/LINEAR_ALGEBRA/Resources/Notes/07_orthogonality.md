# Ορθογωνιότητα

Η ορθογωνιότητα επεκτείνει τη γεωμετρική έννοια της καθετότητας σε αυθαίρετα διανύσματα και υποχώρους. Οι ορθογώνιες και ορθοκανονικές βάσεις απλοποιούν σημαντικά τους υπολογισμούς, καθώς οι συντεταγμένες μπορούν να υπολογιστούν μέσω εσωτερικών γινομένων. Η διαδικασία Gram-Schmidt κατασκευάζει μια ορθογώνια βάση από οποιαδήποτε αρχική βάση, και η σχετική παραγοντοποίηση QR αποτελεί θεμελιώδες εργαλείο στην αριθμητική γραμμική άλγεβρα. Οι ορθογώνιες προβολές σε υποχώρους και οι λύσεις ελαχίστων τετραγώνων αντιμετωπίζουν το πρόβλημα της εύρεσης της βέλτιστης προσεγγιστικής λύσης σε υπερορισμένα συστήματα.

---

## 1. Βασικοί Ορισμοί

### 1.1 Ορθογώνια και Ορθοκανονικά Σύνολα

Ένα σύνολο διανυσμάτων $\{\mathbf{u}_1, \ldots, \mathbf{u}_k\}$ είναι **ορθογώνιο** αν $\mathbf{u}_i \cdot \mathbf{u}_j = 0$ για $i \neq j$.

Είναι **ορθοκανονικό** αν, επιπλέον, $\|\mathbf{u}_i\| = 1$ για όλα τα $i$.

### 1.2 Ορθοκανονική Βάση

Μια βάση $B$ του $\mathbb{R}^n$ η οποία είναι ορθοκανονική. Οι συντεταγμένες ως προς μια ορθοκανονική βάση δίνονται από:

$$
\mathbf{v} = \sum_{i=1}^{n} (\mathbf{v} \cdot \mathbf{u}_i) \mathbf{u}_i
$$

### 1.3 Ανάπτυγμα Fourier

Για μια ορθοκανονική βάση $\{\mathbf{u}_1, \ldots, \mathbf{u}_n\}$:

$$
\mathbf{v} = \sum_{i=1}^{n} (\mathbf{v} \cdot \mathbf{u}_i) \mathbf{u}_i
$$

Οι συντελεστές $c_i = \mathbf{v} \cdot \mathbf{u}_i$ ονομάζονται **συντελεστές Fourier**.

---

## 2. Διαδικασία Gram-Schmidt

Δεδομένου ενός γραμμικά ανεξάρτητου συνόλου $\{\mathbf{a}_1, \ldots, \mathbf{a}_k\}$, η διαδικασία παράγει ένα ορθογώνιο σύνολο $\{\mathbf{v}_1, \ldots, \mathbf{v}_k\}$:

$$
\begin{aligned}
\mathbf{v}_1 &= \mathbf{a}_1 \\
\mathbf{v}_2 &= \mathbf{a}_2 - \text{proj}_{\mathbf{v}_1}(\mathbf{a}_2) \\
\mathbf{v}_3 &= \mathbf{a}_3 - \text{proj}_{\mathbf{v}_1}(\mathbf{a}_3) - \text{proj}_{\mathbf{v}_2}(\mathbf{a}_3) \\
&\vdots
\end{aligned}
$$

όπου $\text{proj}_{\mathbf{v}}(\mathbf{u}) = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{v}\|^2} \mathbf{v}$.

Κανονικοποιούμε κάθε $\mathbf{v}_i$ για να λάβουμε ένα ορθοκανονικό σύνολο.

---

## 3. Ορθογώνιοι Πίνακες

### 3.1 Ορισμός

Ένας τετραγωνικός πίνακας $Q$ είναι **ορθογώνιος** αν $Q^\mathsf{T} Q = I$, ισοδύναμα $Q^{-1} = Q^\mathsf{T}$.

### 3.2 Ιδιότητες

- Οι στήλες του $Q$ αποτελούν ένα ορθοκανονικό σύνολο.
- $\|Q\mathbf{x}\| = \|\mathbf{x}\|$ (διατηρεί το μήκος / τη νόρμα).
- $(Q\mathbf{x}) \cdot (Q\mathbf{y}) = \mathbf{x} \cdot \mathbf{y}$ (διατηρεί τις γωνίες και τα εσωτερικά γινόμενα).
- $\det(Q) = \pm 1$.

---

## 4. Ορθογώνιες Προβολές

### 4.1 Προβολή σε Υποχώρο

Έστω $W$ ένας υποχώρος του $\mathbb{R}^n$ με ορθοκανονική βάση $\{\mathbf{u}_1, \ldots, \mathbf{u}_k\}$. Η ορθογώνια προβολή του $\mathbf{v}$ πάνω στον $W$ είναι:

$$
\text{proj}_W(\mathbf{v}) = \sum_{i=1}^{k} (\mathbf{v} \cdot \mathbf{u}_i) \mathbf{u}_i
$$

Αν ο $A$ είναι ένας πίνακας του οποίου οι στήλες αποτελούν βάση του $W$, τότε:

$$
P = A(A^\mathsf{T} A)^{-1} A^\mathsf{T}
$$

είναι ο πίνακας προβολής στον $\text{Col}(A)$.

### 4.2 Ορθογώνια Αποσύνθεση

Κάθε $\mathbf{v} \in \mathbb{R}^n$ μπορεί να αποσυντεθεί μοναδικά ως:

$$
\mathbf{v} = \text{proj}_W(\mathbf{v}) + (\mathbf{v} - \text{proj}_W(\mathbf{v}))
$$

όπου η πρώτη συνιστώσα ανήκει στον $W$ και η δεύτερη ανήκει στον $W^\perp$ (το ορθογώνιο συμπλήρωμα).

---

## 5. Ελάχιστα Τετράγωνα (Least Squares)

### 5.1 Διατύπωση Προβλήματος

Για ένα υπερορισμένο σύστημα $A\mathbf{x} = \mathbf{b}$ ($m > n$), γενικά δεν υπάρχει ακριβής λύση. Η **λύση ελαχίστων τετραγώνων** $\hat{\mathbf{x}}$ ελαχιστοποιεί το $\|A\mathbf{x} - \mathbf{b}\|^2$.

### 5.2 Κανονικές Εξισώσεις

Η λύση ελαχίστων τετραγώνων ικανοποιεί:

$$
A^\mathsf{T} A \hat{\mathbf{x}} = A^\mathsf{T} \mathbf{b}
$$

### 5.3 Εφαρμογή: Γραμμική Παλινδρόμηση

Δεδομένων των σημείων $(x_i, y_i)$, η ευθεία $y = \beta_0 + \beta_1 x$ που ελαχιστοποιεί το άθροισμα των τετραγώνων των υπολοίπων βρίσκεται επιλύοντας τις κανονικές εξισώσεις.

---

## Λυμένες Ασκήσεις

### Άσκηση 1: Επαλήθευση Ορθογώνιου Συνόλου

**Πρόβλημα:**
Εξετάστε αν το σύνολο $\{(1, 2, -1), (2, 1, 4)\}$ είναι ορθογώνιο.

**Λύση:**
$$
(1, 2, -1) \cdot (2, 1, 4) = 1 \cdot 2 + 2 \cdot 1 + (-1) \cdot 4 = 2 + 2 - 4 = 0
$$

Το εσωτερικό γινόμενο είναι μηδέν, άρα το σύνολο είναι ορθογώνιο.

---

### Άσκηση 2: Διαδικασία Gram-Schmidt

**Πρόβλημα:**
Εφαρμόστε τη διαδικασία Gram-Schmidt στο $\{(1, 1, 0), (1, 0, 1), (0, 1, 1)\}$ για να λάβετε μια ορθογώνια βάση.

**Λύση:**
Έστω $\mathbf{a}_1 = (1, 1, 0)$, $\mathbf{a}_2 = (1, 0, 1)$, $\mathbf{a}_3 = (0, 1, 1)$.

**Βήμα 1:** $\mathbf{v}_1 = \mathbf{a}_1 = (1, 1, 0)$.

**Βήμα 2:**
$$
\text{proj}_{\mathbf{v}_1}(\mathbf{a}_2) = \frac{(1, 0, 1) \cdot (1, 1, 0)}{\|(1, 1, 0)\|^2} (1, 1, 0)
= \frac{1 + 0 + 0}{1 + 1 + 0} (1, 1, 0) = \frac{1}{2}(1, 1, 0) = \left(\frac{1}{2}, \frac{1}{2}, 0\right)
$$

$$
\mathbf{v}_2 = \mathbf{a}_2 - \text{proj}_{\mathbf{v}_1}(\mathbf{a}_2) = \left(1 - \frac{1}{2}, 0 - \frac{1}{2}, 1 - 0\right) = \left(\frac{1}{2}, -\frac{1}{2}, 1\right)
$$

**Βήμα 3:**
$$
\text{proj}_{\mathbf{v}_1}(\mathbf{a}_3) = \frac{(0, 1, 1) \cdot (1, 1, 0)}{2} (1, 1, 0) = \frac{1}{2}(1, 1, 0) = \left(\frac{1}{2}, \frac{1}{2}, 0\right)
$$

$$
\text{proj}_{\mathbf{v}_2}(\mathbf{a}_3) = \frac{(0, 1, 1) \cdot \left(\frac{1}{2}, -\frac{1}{2}, 1\right)}{\|\mathbf{v}_2\|^2} \mathbf{v}_2
$$

Υπολογισμός εσωτερικού γινομένου: $0 \cdot \frac{1}{2} + 1 \cdot \left(-\frac{1}{2}\right) + 1 \cdot 1 = -\frac{1}{2} + 1 = \frac{1}{2}$.

$$\|\mathbf{v}_2\|^2 = \left(\frac{1}{2}\right)^2 + \left(-\frac{1}{2}\right)^2 + 1^2 = \frac{1}{4} + \frac{1}{4} + 1 = \frac{3}{2}.$$

$$
\text{proj}_{\mathbf{v}_2}(\mathbf{a}_3) = \frac{1/2}{3/2} \mathbf{v}_2 = \frac{1}{3} \left(\frac{1}{2}, -\frac{1}{2}, 1\right) = \left(\frac{1}{6}, -\frac{1}{6}, \frac{1}{3}\right)
$$

$$
\mathbf{v}_3 = \mathbf{a}_3 - \text{proj}_{\mathbf{v}_1}(\mathbf{a}_3) - \text{proj}_{\mathbf{v}_2}(\mathbf{a}_3)
$$

$$
= (0, 1, 1) - \left(\frac{1}{2}, \frac{1}{2}, 0\right) - \left(\frac{1}{6}, -\frac{1}{6}, \frac{1}{3}\right)
$$

$$
= \left(-\frac{2}{3}, \frac{2}{3}, \frac{2}{3}\right)
$$

Ορθογώνια βάση: $\left\{(1, 1, 0), \left(\frac{1}{2}, -\frac{1}{2}, 1\right), \left(-\frac{2}{3}, \frac{2}{3}, \frac{2}{3}\right)\right\}$.

---

### Άσκηση 3: Συντελεστές Fourier

**Πρόβλημα:**
Βρείτε τις συντεταγμένες του $\mathbf{v} = (3, 1, 2)$ ως προς την ορθοκανονική βάση $\{\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3\}$ όπου:

$$
\mathbf{u}_1 = \left(\frac{1}{\sqrt{2}}, 0, \frac{1}{\sqrt{2}}\right),\;
\mathbf{u}_2 = (0, 1, 0),\;
\mathbf{u}_3 = \left(\frac{1}{\sqrt{2}}, 0, -\frac{1}{\sqrt{2}}\right)
$$

**Λύση:**
Καθώς η βάση είναι ορθοκανονική, υπολογίζουμε τους συντελεστές Fourier:

$$
c_1 = \mathbf{v} \cdot \mathbf{u}_1 = 3 \cdot \frac{1}{\sqrt{2}} + 1 \cdot 0 + 2 \cdot \frac{1}{\sqrt{2}} = \frac{5}{\sqrt{2}}
$$

$$
c_2 = \mathbf{v} \cdot \mathbf{u}_2 = 3 \cdot 0 + 1 \cdot 1 + 2 \cdot 0 = 1
$$

$$
c_3 = \mathbf{v} \cdot \mathbf{u}_3 = 3 \cdot \frac{1}{\sqrt{2}} + 1 \cdot 0 + 2 \cdot \left(-\frac{1}{\sqrt{2}}\right) = \frac{1}{\sqrt{2}}
$$

Συντεταγμένες: $[\mathbf{v}]_B = \left(\frac{5}{\sqrt{2}}, 1, \frac{1}{\sqrt{2}}\right)$.

Επαλήθευση: $\frac{5}{\sqrt{2}} \mathbf{u}_1 + 1 \cdot \mathbf{u}_2 + \frac{1}{\sqrt{2}} \mathbf{u}_3 = \left(\frac{5}{2} + 0 + \frac{1}{2}, 0 + 1 + 0, \frac{5}{2} + 0 - \frac{1}{2}\right) = (3, 1, 2)$.

---

### Άσκηση 4: Επαλήθευση Ορθογώνιου Πίνακα

**Πρόβλημα:**
Δείξτε ότι ο $Q = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$ είναι ορθογώνιος.

**Λύση:**
Υπολογίζουμε $Q^\mathsf{T} Q$:

$$
Q^\mathsf{T} Q = \begin{bmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{bmatrix}
\begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}
$$

$$
= \begin{bmatrix}
\cos^2\theta + \sin^2\theta & -\cos\theta\sin\theta + \sin\theta\cos\theta \\
-\sin\theta\cos\theta + \cos\theta\sin\theta & \sin^2\theta + \cos^2\theta
\end{bmatrix}
= \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}
$$

$\det(Q) = \cos^2\theta + \sin^2\theta = 1$, επιβεβαιώνοντας ότι $\det(Q) = \pm 1$ (συγκεκριμένα $+1$ για στροφή).

---

### Άσκηση 5: Προβολή σε Υποχώρο

**Πρόβλημα:**
Βρείτε την προβολή του $\mathbf{v} = (1, 0, 2)$ στον υποχώρο που παράγεται από τα $\{(1, 1, 0), (0, 1, 1)\}$.

**Λύση:**
Έστω $A = \begin{bmatrix} 1 & 0 \\ 1 & 1 \\ 0 & 1 \end{bmatrix}$.

Υπολογίζουμε:
$$
A^\mathsf{T} A = \begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{bmatrix}
\begin{bmatrix} 1 & 0 \\ 1 & 1 \\ 0 & 1 \end{bmatrix}
= \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}
$$

$$
(A^\mathsf{T} A)^{-1} = \frac{1}{4 - 1} \begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix}
= \frac{1}{3} \begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix}
$$

$$
A^\mathsf{T} \mathbf{b} = \begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{bmatrix}
\begin{pmatrix} 1 \\ 0 \\ 2 \end{pmatrix}
= \begin{pmatrix} 1 \\ 2 \end{pmatrix}
$$

Συντελεστές ελαχίστων τετραγώνων:
$$
\hat{\mathbf{x}} = (A^\mathsf{T} A)^{-1} A^\mathsf{T} \mathbf{b}
= \frac{1}{3} \begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix}
\begin{pmatrix} 1 \\ 2 \end{pmatrix}
= \frac{1}{3} \begin{pmatrix} 0 \\ 3 \end{pmatrix} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}
$$

Προβολή: $\text{proj}_W(\mathbf{v}) = A\hat{\mathbf{x}} = 0 \cdot (1, 1, 0) + 1 \cdot (0, 1, 1) = (0, 1, 1)$.

---

### Άσκηση 6: Ευθεία Ελαχίστων Τετραγώνων

**Πρόβλημα:**
Βρείτε την ευθεία ελαχίστων τετραγώνων $y = \beta_0 + \beta_1 x$ που διέρχεται από τα σημεία $(1, 2)$, $(2, 3)$, $(3, 5)$.

**Λύση:**
Στήνουμε το σύστημα $A\hat{\mathbf{x}} \approx \mathbf{b}$:

$$
A = \begin{bmatrix} 1 & 1 \\ 1 & 2 \\ 1 & 3 \end{bmatrix},\quad
\mathbf{b} = \begin{pmatrix} 2 \\ 3 \\ 5 \end{pmatrix},\quad
\hat{\mathbf{x}} = \begin{pmatrix} \beta_0 \\ \beta_1 \end{pmatrix}
$$

$$
A^\mathsf{T} A = \begin{bmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \end{bmatrix}
\begin{bmatrix} 1 & 1 \\ 1 & 2 \\ 1 & 3 \end{bmatrix}
= \begin{bmatrix} 3 & 6 \\ 6 & 14 \end{bmatrix}
$$

$$
A^\mathsf{T} \mathbf{b} = \begin{bmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \end{bmatrix}
\begin{pmatrix} 2 \\ 3 \\ 5 \end{pmatrix}
= \begin{pmatrix} 10 \\ 23 \end{pmatrix}
$$

Λύνουμε τις κανονικές εξισώσεις:

$$
\begin{bmatrix} 3 & 6 \\ 6 & 14 \end{bmatrix}
\begin{pmatrix} \beta_0 \\ \beta_1 \end{pmatrix}
= \begin{pmatrix} 10 \\ 23 \end{pmatrix}
$$

Από την πρώτη εξίσωση: $3\beta_0 + 6\beta_1 = 10$.
Από τη δεύτερη: $6\beta_0 + 14\beta_1 = 23$.

Πολλαπλασιάζουμε την πρώτη με το 2: $6\beta_0 + 12\beta_1 = 20$. Αφαιρούμε από τη δεύτερη:

$$
(6\beta_0 + 14\beta_1) - (6\beta_0 + 12\beta_1) = 23 - 20 \Rightarrow 2\beta_1 = 3 \Rightarrow \beta_1 = \frac{3}{2}
$$

Τότε $3\beta_0 + 6 \cdot \frac{3}{2} = 10 \Rightarrow 3\beta_0 + 9 = 10 \Rightarrow \beta_0 = \frac{1}{3}$.

**Ευθεία ελαχίστων τετραγώνων:** $y = \frac{1}{3} + \frac{3}{2}x$.

---

### Άσκηση 7: Παραγοντοποίηση QR

**Πρόβλημα:**
Βρείτε την παραγοντοποίηση QR του $A = \begin{bmatrix} 1 & 1 \\ 1 & 0 \\ 0 & 1 \end{bmatrix}$.

**Λύση:**
Εφαρμόζουμε Gram-Schmidt στις στήλες $\mathbf{a}_1 = (1, 1, 0)$, $\mathbf{a}_2 = (1, 0, 1)$.

$\mathbf{v}_1 = \mathbf{a}_1 = (1, 1, 0)$. $\|\mathbf{v}_1\| = \sqrt{2}$.
$\mathbf{q}_1 = \left(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}, 0\right)$.

$\text{proj}_{\mathbf{v}_1}(\mathbf{a}_2) = \frac{(1, 0, 1) \cdot (1, 1, 0)}{2} (1, 1, 0) = \frac{1}{2} (1, 1, 0)$.

$\mathbf{v}_2 = (1, 0, 1) - \left(\frac{1}{2}, \frac{1}{2}, 0\right) = \left(\frac{1}{2}, -\frac{1}{2}, 1\right)$.

$\|\mathbf{v}_2\| = \sqrt{\frac{1}{4} + \frac{1}{4} + 1} = \sqrt{\frac{3}{2}} = \frac{\sqrt{6}}{2}$.

$\mathbf{q}_2 = \frac{1}{\sqrt{6}/2} \left(\frac{1}{2}, -\frac{1}{2}, 1\right) = \left(\frac{1}{\sqrt{6}}, -\frac{1}{\sqrt{6}}, \frac{2}{\sqrt{6}}\right)$.

Τότε $Q = \begin{bmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{6}} \\ \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{6}} \\ 0 & \frac{2}{\sqrt{6}} \end{bmatrix}$.

$$
R = Q^\mathsf{T} A = \begin{bmatrix} \|v_1\| & \mathbf{q}_1 \cdot \mathbf{a}_2 \\ 0 & \|v_2\| \end{bmatrix}
= \begin{bmatrix} \sqrt{2} & \frac{1}{\sqrt{2}} \\ 0 & \frac{\sqrt{6}}{2} \end{bmatrix}
$$

---

### Άσκηση 8: Ορθογώνιο Συμπλήρωμα

**Πρόβλημα:**
Βρείτε το $W^\perp$ για το $W = \text{span}\{(1, 2, 1, 0), (0, 1, 2, 1)\} \subseteq \mathbb{R}^4$.

**Λύση:**
Το $W^\perp$ αποτελείται από όλα τα διανύσματα $\mathbf{x}$ που είναι ορθογώνια σε κάθε διάνυσμα του $W$:

$$
(1, 2, 1, 0) \cdot \mathbf{x} = 0,\quad (0, 1, 2, 1) \cdot \mathbf{x} = 0
$$

Αυτό δίνει το σύστημα:

$$
x_1 + 2x_2 + x_3 = 0,\quad x_2 + 2x_3 + x_4 = 0
$$

Εκφράζουμε τις βασικές μεταβλητές ($x_1$, $x_2$) ως προς τις ελεύθερες μεταβλητές ($x_3 = s$, $x_4 = t$):

$x_2 = -2s - t$, $x_1 = -2x_2 - x_3 = -2(-2s - t) - s = 4s + 2t - s = 3s + 2t$.

$$
\mathbf{x} = \begin{pmatrix} 3s + 2t \\ -2s - t \\ s \\ t \end{pmatrix}
= s\begin{pmatrix} 3 \\ -2 \\ 1 \\ 0 \end{pmatrix} + t\begin{pmatrix} 2 \\ -1 \\ 0 \\ 1 \end{pmatrix}
$$

$W^\perp = \text{span}\{(3, -2, 1, 0), (2, -1, 0, 1)\}$, και $\dim(W^\perp) = 4 - 2 = 2$.

---

## Συμβουλή Εξετάσεων: Κανονικές Εξισώσεις για Ελάχιστα Τετράγωνα

Όταν λύνετε προβλήματα ελαχίστων τετραγώνων, διαμορφώνετε πάντα τις κανονικές εξισώσεις $A^\mathsf{T} A \hat{\mathbf{x}} = A^\mathsf{T} \mathbf{b}$. Ο πίνακας $A^\mathsf{T} A$ είναι συμμετρικός και θετικά ορισμένος (αν ο $A$ έχει πλήρη τάξη στηλών), οπότε ο αντίστροφός του υπάρχει. Για τη γραμμική παλινδρόμηση, η πρώτη στήλη του $A$ αποτελείται εξ ολοκλήρου από μονάδες (σταθερός όρος) και η δεύτερη στήλη περιέχει τις τιμές $x_i$. Αποστηθίστε αυτή τη διάταξη.

---