# Tutorial 02: Signal Processing and Convolution Simulation with Python

This tutorial demonstrates how to simulate continuous-time signals, numerically evaluate convolution integrals, and analyze LTI system responses using Python (`numpy`, `scipy.signal`, and `matplotlib`).

---

## 1. Environment Setup

Required Python packages:
```bash
pip install numpy scipy matplotlib
```

---

## 2. Numerical Convolution of Continuous Signals

When computing continuous convolution numerically using discrete samples with step size $\Delta t$:
$$
y(t) = \int x(\tau) h(t - \tau) \, d\tau \approx \sum_{k} x[k] h[n - k] \cdot \Delta t
$$
Crucially, the result of `np.convolve(x, h)` must be multiplied by $\Delta t$ to preserve physical amplitude and unit scaling.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Define simulation time grid
dt = 0.001
t = np.arange(0.0, 5.0, dt)

# Define input signal x(t): Unit pulse of width 2 seconds
x = np.where((t >= 0) & (t <= 2.0), 1.0, 0.0)

# Define impulse response h(t): Exponential decay e^(-t)
h = np.exp(-t)

# Perform numerical convolution
y = np.convolve(x, h, mode='full') * dt

# Compute convolution time axis
t_y = np.arange(0.0, len(y) * dt, dt)

# Analytical solution for validation:
# y(t) = 1 - e^(-t) for 0 <= t < 2
# y(t) = (e^2 - 1) * e^(-t) for t >= 2
y_exact = np.zeros_like(t_y)
mask1 = (t_y >= 0) & (t_y < 2.0)
mask2 = (t_y >= 2.0) & (t_y <= 5.0)
y_exact[mask1] = 1.0 - np.exp(-t_y[mask1])
y_exact[mask2] = (np.exp(2.0) - 1.0) * np.exp(-t_y[mask2])

# Plotting verification
plt.figure(figsize=(10, 6))
plt.plot(t_y, y, 'b-', label='Numerical np.convolve * dt')
plt.plot(t_y, y_exact, 'r--', label='Analytical Exact Solution')
plt.title('Continuous Convolution Validation')
plt.xlabel('Time t (seconds)')
plt.ylabel('Amplitude y(t)')
plt.xlim(0, 5)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('convolution_verification.png')
print("Simulation complete. Saved plot to convolution_verification.png")
```

---

## 3. LTI Transfer Function Simulation with `scipy.signal`

For an LTI system described by the differential equation:
$$
\frac{d^2 y(t)}{dt^2} + 2\zeta \omega_n \frac{dy(t)}{dt} + \omega_n^2 y(t) = \omega_n^2 x(t)
$$

```python
# Second-order system parameters: omega_n = 10 rad/s, zeta = 0.2 (underdamped)
omega_n = 10.0
zeta = 0.2

num = [omega_n**2]
den = [1.0, 2.0 * zeta * omega_n, omega_n**2]

sys = signal.TransferFunction(num, den)

# Step response
t_step, y_step = signal.step(sys)

# Impulse response
t_imp, y_imp = signal.impulse(sys)

print(f"Computed step response across {len(t_step)} points.")
```

