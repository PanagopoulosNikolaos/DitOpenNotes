# Σημειώσεις Μελέτης: Εξισώσεις Maxwell και Διάδοση Κυμάτων

## 1. Οι Τέσσερις Εξισώσεις Maxwell

| Ονομασία Νόμου | Διαφορική Μορφή | Ολοκληρωτική Μορφή |
|---|---|---|
| **Gauss (Ηλεκτρισμός)** | $\nabla \cdot \mathbf{D} = \rho_v$ | $\oiint_S \mathbf{D} \cdot d\mathbf{S} = Q_{enc}$ |
| **Gauss (Μαγνητισμός)** | $\nabla \cdot \mathbf{B} = 0$ | $\oiint_S \mathbf{B} \cdot d\mathbf{S} = 0$ |
| **Faraday (Επαγωγή)** | $\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$ | $\oint_C \mathbf{E} \cdot d\mathbf{l} = -\frac{d}{dt}\iint_S \mathbf{B} \cdot d\mathbf{S}$ |
| **Ampère-Maxwell** | $\nabla \times \mathbf{H} = \mathbf{J} + \frac{\partial \mathbf{D}}{\partial t}$ | $\oint_C \mathbf{H} \cdot d\mathbf{l} = \iint_S \left(\mathbf{J} + \frac{\partial \mathbf{D}}{\partial t}\right) \cdot d\mathbf{S}$ |

---

## 2. Εξίσωση Κύματος και Εμπέδηση Μέσου

Σε γραμμικό, ισότροπο, ομογενές μέσο χωρίς πηγές ($\rho_v = 0, \mathbf{J} = 0$):
$$\nabla^2 \mathbf{E} - \mu \epsilon \frac{\partial^2 \mathbf{E}}{\partial t^2} = 0$$

- **Ταχύτητα διάδοσης:** $v = \frac{1}{\sqrt{\mu \epsilon}} = \frac{c}{\sqrt{\mu_r \epsilon_r}}$.
- **Εγγενής Εμπέδηση (Intrinsic Impedance):** $\eta = \sqrt{\frac{\mu}{\epsilon}}$.
- **Σε απωλεστικό μέσο (αγωγιμότητα $\sigma > 0$):**
  $$\gamma = \alpha + j\beta = \sqrt{j\omega\mu(\sigma + j\omega\epsilon)}$$
  - $\alpha$: Συντελεστής απόσβεσης (Attenuation constant, $\text{Np/m}$).
  - $\beta$: Συντελεστής φάσης (Phase constant, $\text{rad/m}$).
  - **Βάθος Διείσδυσης (Skin Depth):** $\delta = \frac{1}{\alpha} \approx \sqrt{\frac{2}{\omega \mu \sigma}}$ για καλούς αγωγούς ($\sigma \gg \omega\epsilon$).

