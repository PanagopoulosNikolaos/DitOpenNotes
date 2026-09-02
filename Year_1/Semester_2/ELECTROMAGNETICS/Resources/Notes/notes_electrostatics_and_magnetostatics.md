# Σημειώσεις Μελέτης: Ηλεκτροστατική και Μαγνητοστατική

## 1. Θεμελιώδεις Νόμοι Ηλεκτροστατικής

### Νόμος Coulomb και Ένταση Ηλεκτρικού Πεδίου
$$\mathbf{F} = \frac{1}{4\pi\epsilon_0} \frac{q_1 q_2}{R^2} \hat{\mathbf{R}}, \quad \mathbf{E} = \frac{\mathbf{F}}{q} = \frac{1}{4\pi\epsilon_0} \int_V \frac{\rho(\mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|^2} \hat{\mathbf{R}} \, dV'$$

### Ηλεκτρικό Δυναμικό και Εξίσωση Poisson
Το ηλεκτροστατικό πεδίο είναι αστρόβιλο ($\nabla \times \mathbf{E} = 0$), συνεπώς εκφράζεται ως κλίση βαθμωτού δυναμικού:
$$\mathbf{E} = -\nabla V$$
Συνδυάζοντας με τον νόμο του Gauss ($\nabla \cdot \mathbf{D} = \rho_v$, $\mathbf{D} = \epsilon \mathbf{E}$):
$$\nabla^2 V = -\frac{\rho_v}{\epsilon} \quad \text{(Εξίσωση Poisson)}$$
Σε περιοχή χωρίς ελεύθερα φορτία ($\rho_v = 0$), προκύπτει η **Εξίσωση Laplace**:
$$\nabla^2 V = 0$$

---

## 2. Θεμελιώδεις Νόμοι Μαγνητοστατικής

### Νόμος Biot-Savart
$$d\mathbf{B} = \frac{\mu_0 I}{4\pi} \frac{d\mathbf{l} \times \hat{\mathbf{R}}}{R^2}$$

### Νόμος Ampère
$$\oint_C \mathbf{B} \cdot d\mathbf{l} = \mu_0 I_{enc} \iff \nabla \times \mathbf{H} = \mathbf{J}$$

### Απουσία Μαγνητικών Μονοπόλων
$$\nabla \cdot \mathbf{B} = 0 \iff \oiint_S \mathbf{B} \cdot d\mathbf{S} = 0$$
Επειδή η απόκλιση είναι μηδέν, το μαγνητικό πεδίο εκφράζεται μέσω του διανυσματικού δυναμικού $\mathbf{A}$:
$$\mathbf{B} = \nabla \times \mathbf{A}$$

