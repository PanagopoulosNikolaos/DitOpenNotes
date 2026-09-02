# Εργαστηριακός Οδηγός 1: Πράξεις Σημάτων και Υπολογισμός Συνέλιξης σε Python με NumPy και Matplotlib

## 1. Σκοπός Εργαστηρίου
Σκοπός είναι η δημιουργία σημάτων συνεχούς και διακριτού χρόνου, η εφαρμογή μετασχηματισμών ανεξάρτητης μεταβλητής (ολίσθηση, κλιμάκωση, αναστροφή), ο υπολογισμός διακριτής συνέλιξης με τη μέθοδο `np.convolve`, και η γραφική απεικόνιση σημάτων.

---

## 2. Εργαστηριακός Κώδικας Python

```python
import numpy as np
import matplotlib.pyplot as plt

def generate_signals():
    # 1. Ορισμός χρονικού άξονα διακριτού χρόνου
    n = np.arange(-5, 15)

    # 2. Ορισμός παλμού εισόδου x[n] = u[n] - u[n-5]
    x = np.where((n >= 0) & (n < 5), 1.0, 0.0)

    # 3. Ορισμός κρουστικής απόκρισης h[n] = (0.7)^n * u[n]
    h = np.where(n >= 0, (0.7)**n, 0.0)

    # 4. Υπολογισμός συνέλιξης y[n] = x[n] * h[n]
    y = np.convolve(x, h, mode='full')
    n_y = np.arange(2 * n[0], 2 * n[-1] + 1)

    # 5. Γραφική Απεικόνιση
    plt.figure(figsize=(10, 8))

    plt.subplot(3, 1, 1)
    plt.stem(n, x, basefmt=" ")
    plt.title("Sima Eisodou x[n]")
    plt.xlabel("n")
    plt.ylabel("Platos")
    plt.grid(True)

    plt.subplot(3, 1, 2)
    plt.stem(n, h, basefmt=" ")
    plt.title("Kroustiki Apokrisi Systimatos h[n]")
    plt.xlabel("n")
    plt.ylabel("Platos")
    plt.grid(True)

    plt.subplot(3, 1, 3)
    plt.stem(n_y, y, basefmt=" ")
    plt.title("Eksodos Systimatos y[n] = x[n] * h[n]")
    plt.xlabel("n")
    plt.ylabel("Platos")
    plt.grid(True)

    plt.tight_layout()
    plt.savefig("convolution_output.png")
    print("To grafima apothikeftike sto convolution_output.png")

if __name__ == "__main__":
    generate_signals()
```

---

## 3. Εκτέλεση
```bash
python3 signal_convolution.py
```

