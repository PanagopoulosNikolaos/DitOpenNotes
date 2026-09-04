# Assignment 02: Diode Rectifier and BJT Biasing Network Design

## Objective
Design and simulate two core analog building blocks: (1) an AC-to-DC full-wave bridge rectifier with capacitive filtering and Zener diode regulation, and (2) a thermally stable voltage-divider biased BJT small-signal amplifier.

---

## Technical Specifications

### Part 1: Regulated DC Power Supply Stage
Design an unregulated and regulated DC stage powered by secondary AC input:
* Input: $V_{\text{in}}(t) = 15 \sin(2\pi \cdot 50 \cdot t)\text{ V}$ ($V_{p} = 15\text{ V}, f = 50\text{ Hz}$).
* Full-Wave Bridge Rectifier: 4 silicon diodes ($V_\gamma = 0.7\text{ V}$).
* Smoothing Filter: Filter capacitor $C$ designed to maintain peak-to-peak ripple voltage $V_r \le 1.0\text{ V}$ when delivering $I_{\text{load}} = 100\text{ mA}$ to load $R_L$.
* Zener Regulator: Select standard Zener diode ($V_Z = 9.1\text{ V}, P_{Z,\text{max}} = 1.0\text{ W}, I_{Z,\text{min}} = 5\text{ mA}$) and compute current-limiting series resistance $R_S$.

### Part 2: BJT Voltage-Divider Amplifier Design
Design a common-emitter NPN transistor amplifier stage:
* Transistor: Silicon NPN BJT with nominal $\beta = 120$, $V_{BE} = 0.7\text{ V}$.
* Supply Voltage: $V_{CC} = 15\text{ V}$.
* Quiescent Operating Point ($Q$-point):
  - Target collector current: $I_{CQ} = 2.0\text{ mA}$.
  - Target collector-emitter voltage: $V_{CEQ} = 7.5\text{ V}$ (midpoint bias for maximum symmetric dynamic range).
* Design Constraints:
  - Allocate $V_E \approx 1.5\text{ V}$ across emitter resistor $R_E$ for negative feedback thermal stability.
  - Apply the $\beta$-independent bias rule: $I_{\text{divider}} \ge 10 I_B$.
  - Calculate standard E24 resistor values for $R_1, R_2, R_C, R_E$.
  - Calculate small-signal voltage gain $A_v$ assuming fully bypassed emitter capacitor ($C_E$).

---

## Deliverables
* Complete analytical design report containing all formulas, component selections, and tolerance calculations.
* SPICE circuit files (`rectifier.cir` and `bjt_amplifier.cir`).
* Transient response waveforms showing input voltage, rectified voltage, ripple filter, and amplified output AC voltage.

---

## Evaluation Rubric

| Criterion | Evaluation Target | Points |
|:---|:---|:---:|
| Rectifier & Filter Calculation | Correct $C$ value, ripple voltage, and diode PIV rating | 25 |
| Zener Regulator Sizing | Valid $R_S$ range satisfying minimum and maximum Zener currents | 25 |
| BJT Bias Network Design | Robust resistor selections meeting $Q$-point criteria and thermal stability | 30 |
| SPICE Simulation Validation | Transient simulation logs confirming ripple specs and voltage gain | 20 |
| **Total** | | **100** |

