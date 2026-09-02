# Διάλεξη 1: Θεμελιώδεις Αρχές Διάδοσης Ηλεκτρομαγνητικών Κυμάτων

## 1. Εξισώσεις Maxwell και Κυματική Εξίσωση
Η διάδοση ηλεκτρομαγνητικών (Η/Μ) κυμάτων σε ομογενές, ισότροπο και γραμμικό μέσο διέπεται από τις εξισώσεις του Maxwell:
$$\nabla \cdot \vec{E} = \frac{\rho}{\varepsilon}, \quad \nabla \cdot \vec{H} = 0$$
$$\nabla \times \vec{E} = -\mu \frac{\partial \vec{H}}{\partial t}, \quad \nabla \times \vec{H} = \vec{J} + \varepsilon \frac{\partial \vec{E}}{\partial t}$$

### 1.1 Κυματική Εξίσωση Helmholtz
Σε περιοχή χωρίς ελεύθερα φορτία και ρεύματα, για αρμονικά μεταβαλλόμενα πεδία συχνότητας $\omega$:
$$\nabla^2 \vec{E} + k^2 \vec{E} = 0$$
Όπου $k = \omega \sqrt{\mu \varepsilon} = \frac{2\pi}{\lambda}$ είναι ο **κυματαριθμός (Wave Number)** ή σταθερά φάσης $\beta$.

---

## 2. Επίπεδα Κύματα (Uniform Plane Waves)
Για ένα επίπεδο κύμα που διαδίδεται κατά τον άξονα $+z$ με ηλεκτρικό πεδίο πολωμένο κατά τον άξονα $x$:
$$\vec{E}(z, t) = E_0 \cos(\omega t - k z) \hat{a}_x$$
$$\vec{H}(z, t) = \frac{E_0}{\eta} \cos(\omega t - k z) \hat{a}_y$$

### 2.1 Χαρακτηριστική Εμπέδηση Μέσου (Wave Impedance $\eta$):
$$\eta = \sqrt{\frac{\mu}{\varepsilon}}$$
Στον ελεύθερο χώρο (κενό):
$$\eta_0 = \sqrt{\frac{\mu_0}{\varepsilon_0}} \approx 120\pi \approx 377 \, \Omega$$

### 2.2 Ταχύτητα Διάδοσης Φάσης ($v_p$):
$$v_p = \frac{1}{\sqrt{\mu \varepsilon}} = \frac{c}{\sqrt{\varepsilon_r \mu_r}}$$

---

## 3. Διάνυσμα Poynting και Πυκνότητα Ισχύος
Το διάνυσμα Poynting εκφράζει την κατεύθυνση και την πυκνότητα ροής ισχύος (σε $\text{W/m}^2$):
$$\vec{S} = \vec{E} \times \vec{H}$$
Η χρονικά μέση πυκνότητα ισχύος για επίπεδο κύμα είναι:
$$\vec{S}_{avg} = \frac{1}{2} \text{Re}\{\vec{E} \times \vec{H}^*\} = \frac{|E_0|^2}{2\eta} \hat{a}_z \, [\text{W/m}^2]$$

---

## 4. Πόλωση Ηλεκτρομαγνητικών Κυμάτων (Wave Polarization)
Η πόλωση περιγράφει τον προσανατολισμό του διανύσματος του ηλεκτρικού πεδίου $\vec{E}$ στον χώρο συναρτήσει του χρόνου:
1. **Γραμμική Πόλωση (Linear):** Το $\vec{E}$ ταλαντώνεται σε σταθερή ευθεία γραμμή.
2. **Κυκλική Πόλωση (Circular):** Οι συνιστώσες $E_x, E_y$ έχουν ίσο πλάτος και διαφορά φάσης $\Delta\phi = \pm 90^\circ$ ($\pm \pi/2$).
3. **Ελλειπτική Πόλωση (Elliptical):** Η γενική περίπτωση διαφορετικών πλατών ή αυθαίρετης διαφοράς φάσης.

