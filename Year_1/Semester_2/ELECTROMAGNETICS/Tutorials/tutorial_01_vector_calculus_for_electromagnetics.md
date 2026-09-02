# Εργαστηριακός Οδηγός 1: Διανυσματικός Λογισμός στον Ηλεκτρομαγνητισμό (Gradient, Divergence, Curl, Laplacian)

## 1. Σκοπός Εργαστηρίου
Στο παρόν εργαστήριο θα εξοικειωθείτε με τους βασικούς διαφορικούς τελεστές του διανυσματικού λογισμού σε Καρτεσιανές, Κυλινδρικές και Σφαιρικές συντεταγμένες, οι οποίοι αποτελούν τη μαθηματική γλώσσα των εξισώσεων Maxwell.

---

## 2. Διαφορικοί Τελεστές σε Καρτεσιανές Συντεταγμένες $(x, y, z)$

Έστω βαθμωτό πεδίο $V(x, y, z)$ και διανυσματικό πεδίο $\mathbf{A} = A_x \hat{\mathbf{x}} + A_y \hat{\mathbf{y}} + A_z \hat{\mathbf{z}}$.

### 2.1 Κλίση (Gradient)
$$\nabla V = \frac{\partial V}{\partial x}\hat{\mathbf{x}} + \frac{\partial V}{\partial y}\hat{\mathbf{y}} + \frac{\partial V}{\partial z}\hat{\mathbf{z}}$$
- Φυσική σημασία: Διάνυσμα που δείχνει την κατεύθυνση μέγιστης αύξησης του δυναμικού (π.χ. $\mathbf{E} = -\nabla V$).

### 2.2 Απόκλιση (Divergence)
$$\nabla \cdot \mathbf{A} = \frac{\partial A_x}{\partial x} + \frac{\partial A_y}{\partial y} + \frac{\partial A_z}{\partial z}$$
- Φυσική σημασία: Πυκνότητα πηγής ή καταβόθρας της ροής του διανυσματικού πεδίου ανά μονάδα όγκου.

### 2.3 Στροβιλισμός (Curl)
$$\nabla \times \mathbf{A} = \begin{vmatrix} \hat{\mathbf{x}} & \hat{\mathbf{y}} & \hat{\mathbf{z}} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ A_x & A_y & A_z \end{vmatrix}$$
- Φυσική σημασία: Μέτρο της κυκλοφορίας και στροβιλισμού του πεδίου γύρω από ένα σημείο.

### 2.4 Τελεστής Laplace (Laplacian)
$$\nabla^2 V = \nabla \cdot (\nabla V) = \frac{\partial^2 V}{\partial x^2} + \frac{\partial^2 V}{\partial y^2} + \frac{\partial^2 V}{\partial z^2}$$

---

## 3. Θεωρήματα Ολοκλήρωσης

- **Θεώρημα Απόκλισης (Gauss-Ostrogradsky):**
  $$\iiint_V (\nabla \cdot \mathbf{A}) \, dV = \oiint_S \mathbf{A} \cdot d\mathbf{S}$$
- **Θεώρημα Στροβιλισμού (Stokes):**
  $$\iint_S (\nabla \times \mathbf{A}) \cdot d\mathbf{S} = \oint_C \mathbf{A} \cdot d\mathbf{l}$$

