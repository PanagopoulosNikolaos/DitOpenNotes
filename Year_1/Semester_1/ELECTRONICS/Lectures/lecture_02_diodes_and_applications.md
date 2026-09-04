# Lecture 02: Semiconductor Physics, Diodes, and Applications

## Context and Grounding
This lecture explores the physics and engineering applications of solid-state PN-junction diodes. It details semiconductor doping mechanics, carrier transport, the Shockley diode model, piecewise circuit approximations, rectifier architectures, capacitive smoothing filters, Zener voltage regulation, and waveshaping diode circuits.

---

## 1. Semiconductor Physics and the PN Junction

### 1.1 Intrinsic and Extrinsic Semiconductors
* **Intrinsic Silicon (Si)**: Tetravalent semiconductor with diamond cubic lattice. At $T = 300\text{ K}$, thermal excitation generates equal numbers of free electrons ($n$) and holes ($p$):
  $$n_i = p_i \approx 1.5 \times 10^{10}\text{ cm}^{-3}$$
* **N-Type Doping**: Pentavalent impurities (Phosphorus, Arsenic) introduce donor energy states near the conduction band, increasing electron concentration ($n \approx N_D$).
* **P-Type Doping**: Trivalent impurities (Boron, Gallium) introduce acceptor energy states near the valence band, increasing hole concentration ($p \approx N_A$).

### 1.2 PN Junction Formation & Barrier Potential
Bringing p-type and n-type materials into metallurgical contact causes mobile electrons to diffuse into the p-region and holes into the n-region. Uncompensated ionized donor ($N_D^+$) and acceptor ($N_A^-$) atoms create a space-charge **depletion region**:
* The built-in potential barrier for silicon at room temperature is:
  $$V_0 = V_T \ln\left(\frac{N_A N_D}{n_i^2}\right) \approx 0.6 - 0.7\text{ V}$$
  where $V_T = \frac{k T}{q} \approx 25.86\text{ mV}$ at $300\text{ K}$.

---

## 2. Diode Characteristics and Modeling

### 2.1 The Shockley Diode Equation
The current-voltage relationship of an ideal PN-junction diode is:
$$I_D = I_S \left( e^{\frac{V_D}{\eta V_T}} - 1 \right)$$
* $I_S$: Reverse saturation current (typically $10^{-15}\text{ A}$ to $10^{-12}\text{ A}$).
* $\eta$: Ideality factor ($\eta \approx 1$ for Ge, $\eta \approx 1\text{ to }2$ for Si).
* $V_D$: Voltage across the diode.

### 2.2 Circuit Modeling Approximations
1. **Ideal Diode Model**: Perfect switch. Forward bias $\implies V_D = 0\text{ V}$ (short circuit). Reverse bias $\implies I_D = 0\text{ A}$ (open circuit).
2. **Constant Voltage Drop Model (Practical Model)**:
   - When $I_D > 0$: $V_D = V_\gamma \approx 0.7\text{ V}$ (Silicon).
   - When $V_D < V_\gamma$: $I_D = 0\text{ A}$.
3. **Piecewise Linear Model**: Accounts for internal dynamic forward resistance $r_d$:
   $$V_D = V_\gamma + I_D \cdot r_d$$

---

## 3. Rectification Circuits and DC Power Supplies

### 3.1 Rectifier Topologies
| Metric | Half-Wave Rectifier | Full-Wave Center-Tapped | Full-Wave Bridge Rectifier |
|:---|:---:|:---:|:---:|
| Diodes Count | 1 | 2 | 4 |
| Peak Output Voltage ($V_{p,\text{out}}$) | $V_p - 0.7\text{ V}$ | $V_p - 0.7\text{ V}$ | $V_p - 1.4\text{ V}$ |
| Output Frequency | $f_{\text{in}}$ | $2 f_{\text{in}}$ | $2 f_{\text{in}}$ |
| Peak Inverse Voltage (PIV) | $V_p$ | $2 V_p$ | $V_p$ |
| DC Average Output ($V_{\text{dc}}$) | $\frac{V_{p,\text{out}}}{\pi} \approx 0.318 V_{p,\text{out}}$ | $\frac{2 V_{p,\text{out}}}{\pi} \approx 0.636 V_{p,\text{out}}$ | $\frac{2 V_{p,\text{out}}}{\pi} \approx 0.636 V_{p,\text{out}}$ |

### 3.2 Capacitive Smoothing Filter
Connecting a capacitor $C$ in parallel with load $R_L$ charges the capacitor to peak voltage and discharges through $R_L$ between AC peaks:
* Peak-to-peak ripple voltage:
  $$V_r = \frac{I_{\text{load}}}{f_{\text{rect}} \cdot C} = \frac{V_{\text{dc}}}{f_{\text{rect}} \cdot R_L \cdot C}$$
  where $f_{\text{rect}} = 2 f_{\text{line}} = 100\text{ Hz}$ for full-wave rectifiers on 50 Hz European mains.
* Ripple factor:
  $$r = \frac{V_{r,\text{rms}}}{V_{\text{dc}}} \approx \frac{1}{2 \sqrt{3} f_{\text{rect}} R_L C}$$

---

## 4. Zener Diodes and Wave-Shaping Circuits

### 4.1 Zener Voltage Regulation
Zener diodes operate in controlled reverse breakdown at a stable breakdown voltage $V_Z$.
* Series current limiting resistor:
  $$R_S = \frac{V_{\text{in}} - V_Z}{I_Z + I_L}$$
  subject to $I_{Z,\text{min}} \le I_Z \le I_{Z,\text{max}}$.

### 4.2 Clipping and Clamping Circuits
* **Clippers (Limiters)**: Remove portions of an input signal above or below pre-determined threshold voltages without distorting the remaining waveform.
* **Clampers (DC Restorers)**: Shift an input AC waveform to a different DC voltage level using a capacitor, diode, and resistor without altering signal shape.

