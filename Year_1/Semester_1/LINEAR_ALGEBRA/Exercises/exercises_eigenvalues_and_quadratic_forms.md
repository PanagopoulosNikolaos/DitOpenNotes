# Ασκήσεις Εξάσκησης: Ιδιοτιμές, Διαγωνιοποίηση και Τετραγωνικές Μορφές

## Άσκηση 1: Διαγωνιοποίηση Πίνακα $2 \times 2$

### Εκφώνηση
Δίνεται ο συμμετρικός πίνακας:
$$A = \begin{pmatrix} 3 & 2 \\ 2 & 6 \end{pmatrix}$$
1. Βρείτε τις ιδιοτιμές και τα αντίστοιχα ιδιοδιανύσματα του $A$.
2. Κατασκευάστε τον ορθογώνιο πίνακα $P$ και τον διαγώνιο $D$ τέτοιους ώστε $A = P D P^T$.

### Λύση
1. **Χαρακτηριστική Εξίσωση:**
   $$\det(A - \lambda I) = \begin{vmatrix} 3 - \lambda & 2 \\ 2 & 6 - \lambda \end{vmatrix} = (3 - \lambda)(6 - \lambda) - 4 = \lambda^2 - 9\lambda + 14 = 0$$
   Οι ρίζες είναι: $\lambda_1 = 7, \quad \lambda_2 = 2$.

2. **Ιδιοδιανύσματα:**
   * Για $\lambda_1 = 7$:
     $$(A - 7I)\mathbf{x} = \begin{pmatrix} -4 & 2 \\ 2 & -1 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \implies 2x_1 = x_2$$
     Ιδιοδιάνυσμα $\mathbf{v}_1 = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$, κανονικοποιημένο $\mathbf{q}_1 = \frac{1}{\sqrt{5}} \begin{pmatrix} 1 \\ 2 \end{pmatrix}$.
   * Για $\lambda_2 = 2$:
     $$(A - 2I)\mathbf{x} = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \implies x_1 = -2x_2$$
     Ιδιοδιάνυσμα $\mathbf{v}_2 = \begin{pmatrix} -2 \\ 1 \end{pmatrix}$, κανονικοποιημένο $\mathbf{q}_2 = \frac{1}{\sqrt{5}} \begin{pmatrix} -2 \\ 1 \end{pmatrix}$.

3. **Ορθογώνια Διαγωνιοποίηση:**
   $$P = \frac{1}{\sqrt{5}} \begin{pmatrix} 1 & -2 \\ 2 & 1 \end{pmatrix}, \quad D = \begin{pmatrix} 7 & 0 \\ 0 & 2 \end{pmatrix}$$
   όπου $P^T P = I_2$ και $A = P D P^T$.
