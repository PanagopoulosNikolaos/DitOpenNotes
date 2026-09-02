# Διάλεξη 3: Γραμμικοί Μετασχηματισμοί και Ορθογωνιότητα

## 1. Γραμμικές Απεικονίσεις και Αναπαράσταση με Πίνακες

Μια απεικόνιση $T: V \to W$ μεταξύ διανυσματικών χώρων ονομάζεται γραμμικός μετασχηματισμός εάν:
1. $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$ για κάθε $\mathbf{u}, \mathbf{v} \in V$.
2. $T(c\mathbf{u}) = c T(\mathbf{u})$ για κάθε $c \in \mathbb{R}, \mathbf{u} \in V$.

### Πυρήνας και Εικόνα
* **Πυρήνας (Kernel):** $\ker(T) = \{\mathbf{v} \in V \mid T(\mathbf{v}) = \mathbf{0}\}$.
* **Εικόνα (Image / Range):** $\text{Im}(T) = \{T(\mathbf{v}) \mid \mathbf{v} \in V\}$.
* **Θεώρημα Βαθμού και Μηδενικότητας (Rank-Nullity Theorem):**
  $$\dim(\ker(T)) + \dim(\text{Im}(T)) = \dim(V)$$

---

## 2. Εσωτερικό Γινόμενο και Ορθογωνιότητα

Στον ευκλείδειο χώρο $\mathbb{R}^n$, το τυπικό εσωτερικό γινόμενο ορίζεται ως:
$$\langle \mathbf{u}, \mathbf{v} \rangle = \mathbf{u} \cdot \mathbf{v} = \mathbf{u}^T \mathbf{v} = \sum_{i=1}^n u_i v_i$$

* **Μέτρο / Νόρμα:** $\|\mathbf{v}\| = \sqrt{\mathbf{v} \cdot \mathbf{v}}$.
* **Ορθογώνια Διανύσματα:** Δύο διανύσματα είναι ορθογώνια αν $\mathbf{u} \cdot \mathbf{v} = 0$.
* **Ορθοκανονική Βάση:** Βάση αποτελούμενη από διανύσματα μοναδιαίου μέτρου που είναι ανά δύο ορθογώνια ($\mathbf{q}_i \cdot \mathbf{q}_j = \delta_{ij}$).

---

## 3. Διαδικασία Ορθοκανονικοποίησης Gram-Schmidt

Δεδομένης βάσης $\{\mathbf{v}_1, \dots, \mathbf{v}_k\}$, η ορθογώνια βάση $\{\mathbf{u}_1, \dots, \mathbf{u}_k\}$ κατασκευάζεται επαγωγικά:
$$\begin{aligned}
\mathbf{u}_1 &= \mathbf{v}_1 \\
\mathbf{u}_2 &= \mathbf{v}_2 - \frac{\mathbf{v}_2 \cdot \mathbf{u}_1}{\|\mathbf{u}_1\|^2} \mathbf{u}_1 \\
\mathbf{u}_k &= \mathbf{v}_k - \sum_{j=1}^{k-1} \frac{\mathbf{v}_k \cdot \mathbf{u}_j}{\|\mathbf{u}_j\|^2} \mathbf{u}_j
\end{aligned}$$
Η κανονικοποίηση δίνει τα ορθοκανονικά διανύσματα $\mathbf{q}_i = \frac{\mathbf{u}_i}{\|\mathbf{u}_i\|}$.
