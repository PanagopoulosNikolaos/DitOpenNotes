# Signals and Systems: Interactive Simulators & Visualizers

A collection of standalone, browser-based interactive web applications engineered to visualize continuous-time and discrete-time signal operations, system classifications, and LTI convolution mechanics for **Signals and Systems (Course Code: 303)**.

---

## Interactive Application Directory

| File Name | Topic Covered | Key Interactive Features |
|:---|:---|:---|
| [`01_InteractiveLearning.html`](01_InteractiveLearning.html) | Fundamental Signals & Harmonic Synthesis | Real-time generation of sinusoids, square waves, and sawtooth waves with adjustable frequency, phase, and amplitude. Live harmonic decomposition and frequency spectrum plotting. |
| [`02_InteractiveLearning.html`](02_InteractiveLearning.html) | Continuous-Time Signal Transformations | Interactive graphical transformation explorer: time shifting $x(t - t_0)$, time reversal $x(-t)$, and time scaling $x(at)$. Displays original and transformed waveforms simultaneously with order-of-operations controls. |
| [`03_InteractiveLearning.html`](03_InteractiveLearning.html) | Elementary Waveforms & Energy/Power Metrics | Interactive synthesis of elementary functions: unit step $u(t)$, Dirac delta approximation $\delta_\epsilon(t)$, complex exponential $e^{(\sigma + j\omega)t}$, and rectangular/triangular pulses. Automated analytical integration of total signal energy $E$ and average power $P$. |
| [`04_InteractiveLearning.html`](04_InteractiveLearning.html) | Continuous-Time System Property Verification | Visual sandbox verifying mathematical system properties: Linearity (Superposition & Homogeneity), Time-Invariance, Memory (Static vs. Dynamic), Causality, and BIBO Stability under user-defined stimulus signals. |
| [`05_InteractiveLearning.html`](05_InteractiveLearning.html) | LTI Systems & Graphical Convolution Simulator | Cycle-by-cycle continuous convolution animator: $y(t) = \int_{-\infty}^\infty x(\tau) h(t - \tau) d\tau$. Visualizes the four classical stages: folding $h(-\tau)$, shifting $h(t - \tau)$, point-by-point multiplying $x(\tau)h(t-\tau)$, and surface integrating under the product curve. |

---

## How to Launch and Use

All interactive applications are built using client-side JavaScript, Tailwind CSS, Chart.js, and MathJax. They run locally without requiring an active web server or internet connection (aside from initial CDN caching).

### Opening in Linux / Ubuntu:
```bash
# Open a specific simulator in default browser
xdg-open Examples/01_InteractiveLearning.html

# Or open the convolution animator directly
xdg-open Examples/05_InteractiveLearning.html
```

### Opening in Web Browser Directly:
Navigate to the repository folder and double-click any `.html` file, or drag and drop the file into Google Chrome, Mozilla Firefox, or Microsoft Edge.

---

## Alignment with Course Syllabus

- **Lectures 01 - 02:** Supported by `01_InteractiveLearning.html` and `02_InteractiveLearning.html` for signal representations and independent variable operations.
- **Lectures 03 - 04:** Supported by `03_InteractiveLearning.html` and `04_InteractiveLearning.html` for energy/power classifications and formal system property proofs.
- **Lectures 05 - 06:** Supported by `05_InteractiveLearning.html` for continuous-time convolution, impulse responses, and LTI stability analysis.

