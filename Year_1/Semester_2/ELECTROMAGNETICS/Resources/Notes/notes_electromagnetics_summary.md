# Σύνοψη Θεωρίας και Τυπολόγιο: Ηλεκτρομαγνητισμός και Τηλεπικοινωνίες

## 1. Διανυσματικός Λογισμός και Διαφορικοί Τελεστές

### Τελεστής Ανάδελτα ($\nabla$) σε Καρτεσιανές Συντεταγμένες
$$\nabla = \hat{x}\frac{\partial}{\partial x} + \hat{y}\frac{\partial}{\partial y} + \hat{z}\frac{\partial}{\partial z}$$

- **Κλίση Βαθμωτού Πεδίου (Gradient):**
  $$\nabla V = \frac{\partial V}{\partial x}\hat{x} + \frac{\partial V}{\partial y}\hat{y} + \frac{\partial V}{\partial z}\hat{z}$$
- **Απόκλιση Διανυσματικού Πεδίου (Divergence):**
  $$\nabla \cdot \vec{A} = \frac{\partial A_x}{\partial x} + \frac{\partial A_y}{\partial y} + \frac{\partial A_z}{\partial z}$$
- **Στροβιλισμός (Curl):**
  $$\nabla \times \vec{A} = \begin{vmatrix} \hat{x} & \hat{y} & \hat{z} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ A_x & A_y & A_z \end{vmatrix}$$
- **Θεώρημα Gauss (Απόκλισης):**
  $$\iiint_V (\nabla \cdot \vec{A}) \, dV = \oiint_S \vec{A} \cdot d\vec{S}$$
- **Θεώρημα Stokes:**
  $$\iint_S (\nabla \times \vec{A}) \cdot d\vec{S} = \oint_C \vec{A} \cdot d\vec{l}$$

---

## 2. Εξισώσεις του Maxwell

| Νόμος | Διαφορική Μορφή | Ολοκληρωτική Μορφή | Φυσική Ερμηνεία |
|---|---|---|---|
| **Gauss (Ηλεκτρισμός)** | $\nabla \cdot \vec{D} = \rho_v$ | $\oint_S \vec{D} \cdot d\vec{S} = Q_{\text{enc}}$ | Πηγές ηλεκτρικού πεδίου είναι τα φορτία |
| **Gauss (Μαγνητισμός)** | $\nabla \cdot \vec{B} = 0$ | $\oint_S \vec{B} \cdot d\vec{S} = 0$ | Απουσία μαγνητικών μονοπόλων |
| **Faraday (Επαγωγή)** | $\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}$ | $\oint_C \vec{E} \cdot d\vec{l} = -\frac{d\Phi_B}{dt}$ | Χρονικά μεταβαλλόμενο $\vec{B}$ παράγει $\vec{E}$ |
| **Ampère-Maxwell** | $\nabla \times \vec{H} = \vec{J} + \frac{\partial \vec{D}}{\partial t}$ | $\oint_C \vec{H} \cdot d\vec{l} = I_{\text{enc}} + \frac{d\Phi_D}{dt}$ | Ρεύματα αγωγιμότητας & μετατόπισης παράγουν $\vec{H}$ |

### Καταστατικές Σχέσεις Γραμμικών Ισότροπων Μέσων
$$\vec{D} = \epsilon \vec{E} = \epsilon_0 \epsilon_r \vec{E}$$
$$\vec{B} = \mu \vec{H} = \mu_0 \mu_r \vec{H}$$
$$\vec{J} = \sigma \vec{E} \quad \text{(Νόμος του Ohm)}$$

---

## 3. Επίπεδα Ηλεκτρομαγνητικά Κύματα στο Κενό
Για κύμα πολωμένο κατά $\hat{x}$ που διαδίδεται προς τη θετική κατεύθυνση $+z$:
$$\vec{E}(z, t) = E_0 \cos(kz - \omega t) \hat{x}$$
$$\vec{B}(z, t) = B_0 \cos(kz - \omega t) \hat{y}$$

- **Σχέση Πλατών:** $E_0 = c B_0$, όπου $c = \frac{1}{\sqrt{\mu_0 \epsilon_0}} \approx 3 \times 10^8 \text{ m/s}$.
- **Κυματάριθμος & Συχνότητα:** $k = \frac{2\pi}{\lambda}$, $\omega = 2\pi f$, $c = \lambda f = \frac{\omega}{k}$.
- **Κυματική Εμπέδηση Κενού:**
  $$\eta_0 = \sqrt{\frac{\mu_0}{\epsilon_0}} \approx 120\pi \ \Omega \approx 377\ \Omega$$
- **Διάνυσμα Poynting:**
  $$\vec{S} = \vec{E} \times \vec{H} = \frac{1}{\mu_0} (\vec{E} \times \vec{B})$$
- **Μέση Ένταση Κύματος:**
  $$I = \langle |\vec{S}| \rangle = \frac{E_0^2}{2\eta_0} = \frac{1}{2} c \epsilon_0 E_0^2$$
