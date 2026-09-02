# Ασκήσεις Εμπέδωσης: Εξισώσεις Maxwell και Διάδοση Επιπέδων Κυμάτων

## Άσκηση 1: Επίπεδο Ηλεκτρομαγνητικό Κύμα στο Κενό

### Εκφώνηση
Ένα ομοιόμορφο επίπεδο ηλεκτρομαγνητικό κύμα διαδίδεται στο κενό κατά μήκος του άξονα $+z$. Το ηλεκτρικό πεδίο δίνεται από:
$$\mathbf{E}(z, t) = 100 \cos(\omega t - kz) \hat{\mathbf{x}} \quad [\text{V/m}]$$
με συχνότητα $f = 300\text{ MHz}$.
1. Υπολογίστε το μήκος κύματος $\lambda$, τον κυματαριθμό $k$ και την κυκλική συχνότητα $\omega$.
2. Βρείτε την έκφραση του μαγνητικού πεδίου $\mathbf{H}(z, t)$.
3. Υπολογίστε το διάνυσμα Poynting $\mathbf{S}(z, t)$ και τη μέση χρονική πυκνότητα ισχύος $\mathbf{S}_{avg}$.

### Λύση
1. **Παράμετροι Κύματος:**
   - $\omega = 2\pi f = 2\pi \cdot 300 \cdot 10^6 = 6\pi \cdot 10^8\text{ rad/s}$
   - $\lambda = \frac{c}{f} = \frac{3 \cdot 10^8}{300 \cdot 10^6} = 1\text{ m}$
   - $k = \frac{2\pi}{\lambda} = 2\pi\text{ rad/m}$

2. **Μαγνητικό Πεδίο:**
   - Εγγενής αντίσταση κενού: $\eta_0 = \sqrt{\frac{\mu_0}{\epsilon_0}} \approx 120\pi \approx 377 \, \Omega$.
   - $\mathbf{H} = \frac{1}{\eta_0} (\hat{\mathbf{k}} \times \mathbf{E}) = \frac{1}{\eta_0} (\hat{\mathbf{z}} \times \hat{\mathbf{x}}) E_x = \frac{E_x}{\eta_0} \hat{\mathbf{y}}$
   - $\mathbf{H}(z, t) = \frac{100}{377} \cos(6\pi \cdot 10^8 t - 2\pi z) \hat{\mathbf{y}} \approx 0.265 \cos(6\pi \cdot 10^8 t - 2\pi z) \hat{\mathbf{y}} \quad [\text{A/m}]$

3. **Διάνυσμα Poynting:**
   $$\mathbf{S}(z, t) = \mathbf{E} \times \mathbf{H} = 26.5 \cos^2(\omega t - kz) \hat{\mathbf{z}} \quad [\text{W/m}^2]$$
   $$\mathbf{S}_{avg} = \frac{1}{2} \text{Re}\{\mathbf{E} \times \mathbf{H}^*\} = \frac{E_0^2}{2\eta_0} \hat{\mathbf{z}} = \frac{100^2}{2 \cdot 377} \hat{\mathbf{z}} \approx 13.26 \hat{\mathbf{z}} \quad [\text{W/m}^2]$$

---

## Άσκηση 2: Ρεύμα Μετατόπισης σε Επίπεδο Πυκνωτή

### Εκφώνηση
Επίπεδος πυκνωτής με πλάκες εμβαδού $A$ και απόσταση $d$ τροφοδοτείται με αρμονική τάση $V(t) = V_0 \sin(\omega t)$. Δείξτε ότι το ρεύμα αγωγιμότητας $I_c$ στα καλώδια τροφοδοσίας ισούται με το ρεύμα μετατόπισης $I_d$ εντός του διηλεκτρικού μεταξύ των οπλισμών.

### Λύση
- Χωρητικότητα: $C = \frac{\epsilon A}{d}$.
- Ρεύμα αγωγιμότητας:
  $$I_c = C \frac{dV}{dt} = \frac{\epsilon A}{d} \omega V_0 \cos(\omega t)$$
- Ηλεκτρικό πεδίο: $E(t) = \frac{V(t)}{d} = \frac{V_0}{d} \sin(\omega t)$.
- Πυκνότητα ρεύματος μετατόπισης:
  $$J_d = \frac{\partial D}{\partial t} = \epsilon \frac{\partial E}{\partial t} = \epsilon \frac{\omega V_0}{d} \cos(\omega t)$$
- Συνολικό ρεύμα μετατόπισης:
  $$I_d = \iint_A J_d \, dA = J_d \cdot A = \frac{\epsilon A}{d} \omega V_0 \cos(\omega t) = I_c$$
  Αποδείχθηκε ότι $I_d = I_c$, διασφαλίζοντας τη συνέχεια του ρεύματος.

