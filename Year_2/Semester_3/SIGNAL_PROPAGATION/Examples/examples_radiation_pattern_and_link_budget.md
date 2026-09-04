# Worked Examples: Antenna Pattern and Link Budget Synthesis Walkthrough

This document analyzes the computational algorithms implemented in [`examples_radiation_pattern_and_link_budget.py`](file:///home/ice/Documents/CodeHub/GitHub-Projects/Public/DitOpenNotes/Year_2/Semester_3/SIGNAL_PROPAGATION/Examples/examples_radiation_pattern_and_link_budget.py).

---

## 1. Algorithmic Overview

### 1.1 Numerical Evaluation of the Dipole Field
The function `compute_dipole_field` calculates the normalized far-field magnitude of a half-wave dipole:
$$
F(\theta) = \left| \frac{\cos\left(\frac{\pi}{2}\cos\theta\right)}{\sin\theta} \right|
$$
At the poles ($\theta = 0, \pi$), division by zero is avoided using floating-point threshold clamping.

### 1.2 Array Factor with Indeterminate Handling
At $\psi = 0$, the formula $\frac{\sin(N\psi/2)}{N\sin(\psi/2)}$ yields an indeterminate form $\frac{0}{0}$. By L'Hôpital's rule:
$$
\lim_{\psi \to 0} \frac{\sin(N\psi/2)}{N\sin(\psi/2)} = \frac{\frac{N}{2}\cos(0)}{N \cdot \frac{1}{2}\cos(0)} = 1.0
$$
The script evaluates this limit conditionally using `np.where`.

---

## 2. Execution and Terminal Output

Run the example script:
```bash
python3 examples_radiation_pattern_and_link_budget.py
```

### Expected Terminal Output:
```text
--- RF Link Budget Analysis ---
Carrier Frequency:     2400.0 MHz
Path Distance:         3.50 km
Free Space Path Loss:  110.92 dB
Transmit Power:        23.0 dBm
Antenna Gains (Tx/Rx): 12.0 dBi / 6.0 dBi
Received Power (Pr):   -71.92 dBm (64.2688 pW)
```
The link budget confirms a received power of $-71.92\text{ dBm}$, which is comfortably above typical receiver sensitivity levels (around $-90\text{ dBm}$ for standard Wi-Fi / LTE reception).

