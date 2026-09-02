# Εργαστηριακός Οδηγός 1: Προσαρμογή Εμπέδησης με Χάρτη Smith και Python (PySmith / Scikit-RF)

## 1. Σκοπός Εργαστηρίου
Σκοπός είναι ο υπολογισμός συντελεστή ανάκλασης $\Gamma$, λόγου στάσιμου κύματος VSWR, και η σχεδίαση δικτύων προσαρμογής μονής γραμμής συντονισμού (single stub matching) και μετασχηματιστή $\lambda/4$ μέσω του Smith Chart και του υπολογιστικού πακέτου `scikit-rf`.

---

## 2. Εργαστηριακή Άσκηση: Προσαρμογή Φορτίου $Z_L = 100 + j50 \, \Omega$ σε Γραμμή $Z_0 = 50 \, \Omega$

### 2.1 Αναλυτικοί Υπολογισμοί:
1. **Κανονικοποιημένη Εμπέδηση Φορτίου:**
   $$z_L = \frac{Z_L}{Z_0} = \frac{100 + j50}{50} = 2 + j1$$
2. **Συντελεστής Ανάκλασης στο Φορτίο:**
   $$\Gamma_L = \frac{z_L - 1}{z_L + 1} = \frac{1 + j1}{3 + j1} = \frac{\sqrt{2} e^{j 45^\circ}}{\sqrt{10} e^{j 18.43^\circ}} = 0.4472 e^{j 26.57^\circ}$$
3. **Υπολογισμός VSWR:**
   $$\text{VSWR} = \frac{1 + |\Gamma_L|}{1 - |\Gamma_L|} = \frac{1 + 0.4472}{1 - 0.4472} = \frac{1.4472}{0.5528} \approx 2.62$$
4. **Απώλειες Επιστροφής (Return Loss):**
   $$RL = -20 \log_{10}(0.4472) \approx 6.99\text{ dB}$$

---

## 3. Κώδικας Υπολογισμού σε Python

```python
import numpy as np

def analyze_transmission_line(z_load, z0=50.0):
    z_norm = z_load / z0
    gamma = (z_norm - 1) / (z_norm + 1)
    gamma_mag = np.abs(gamma)
    gamma_phase_deg = np.angle(gamma, deg=True)
    
    vswr = (1 + gamma_mag) / (1 - gamma_mag)
    return_loss_db = -20 * np.log10(gamma_mag) if gamma_mag > 0 else float('inf')

    print(f"Fortio Z_L: {z_load} Ohm (Z0 = {z0} Ohm)")
    print(f"Kanonikopoiimeni Empedisi z_L: {z_norm:.4f}")
    print(f"Syntelestis Anaklasis Gamma: {gamma_mag:.4f} /_ {gamma_phase_deg:.2f} deg")
    print(f"Logos Stasimou Kymatos (VSWR): {vswr:.4f}")
    print(f"Apoleies Epistrofis (Return Loss): {return_loss_db:.2f} dB")

if __name__ == "__main__":
    zl = 100 + 50j
    analyze_transmission_line(zl)
```

---

## 4. Εκτέλεση
```bash
python3 smith_chart_calc.py
```

