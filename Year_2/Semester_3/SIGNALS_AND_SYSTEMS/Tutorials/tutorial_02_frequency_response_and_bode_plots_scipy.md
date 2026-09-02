# Εργαστηριακός Οδηγός 2: Απόκριση Συχνότητας, Διαγράμματα Bode και Σχεδίαση Φίλτρων με SciPy

## 1. Σκοπός Εργαστηρίου
Σκοπός είναι η μοντελοποίηση αναλογικών και ψηφιακών LTI συστημάτων μέσω συναρτήσεων μεταφοράς $H(s)$ και $H(z)$, η παραγωγή διαγραμμάτων Bode (πλάτους και φάσης), και ο υπολογισμός της απόκρισης συχνότητας με τη χρήση της βιβλιοθήκης `scipy.signal`.

---

## 2. Εργαστηριακός Κώδικας Python

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def analyze_lowpass_filter():
    # 1. Ορισμός αναλογικού χαμηλοπερατού φίλτρου Butterworth 2ης τάξης με fc = 100 rad/s
    omega_c = 100.0
    b, a = signal.butter(2, omega_c, 'low', analog=True)

    # 2. Υπολογισμός απόκρισης συχνότητας (Bode plot)
    w, mag, phase = signal.bode((b, a))

    # 3. Σχεδίαση διαγραμμάτων Bode
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7), sharex=True)

    # Διάγραμμα Πλάτους (Magnitude dB)
    ax1.semilogx(w, mag, color='blue', linewidth=2)
    ax1.set_title("Analog Butterworth Low-pass Filter (2nd Order)")
    ax1.set_ylabel("Platos (dB)")
    ax1.grid(True, which="both", ls="-")
    ax1.axvline(omega_c, color='red', linestyle='--', label=f"Cutoff fc = {omega_c} rad/s")
    ax1.legend()

    # Διάγραμμα Φάσης (Phase degrees)
    ax2.semilogx(w, phase, color='green', linewidth=2)
    ax2.set_xlabel("Kykliki Syxnotita omega (rad/s)")
    ax2.set_ylabel("Fasi (moires)")
    ax2.grid(True, which="both", ls="-")

    plt.tight_layout()
    plt.savefig("bode_plot_butterworth.png")
    print("To diagramma Bode apothikeftike sto bode_plot_butterworth.png")

if __name__ == "__main__":
    analyze_lowpass_filter()
```

---

## 3. Εκτέλεση και Παρατηρήσεις
```bash
python3 filter_analysis.py
```
Παρατηρήστε την κλίση εξασθένησης στη ζώνη αποκοπής: για φίλτρο 2ης τάξης η εξασθένηση είναι $-40\text{ dB/decade}$.

