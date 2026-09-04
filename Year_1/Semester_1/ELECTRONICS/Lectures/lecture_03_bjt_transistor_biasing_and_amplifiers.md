# Lecture 03: Bipolar Junction Transistors (BJT) and Small-Signal Amplifiers

## Context and Grounding
This lecture analyzes the three-terminal Bipolar Junction Transistor (BJT). It covers physical transport phenomena, operating regions, DC load-line analysis, bias stabilization techniques (particularly four-resistor voltage-divider biasing), and small-signal AC modeling for common-emitter (CE) voltage amplifiers.

---

## 1. BJT Architecture and Operational Regimes

A BJT consists of two back-to-back PN junctions sharing a thin central base region. The dominant configurations are NPN and PNP.

### 1.1 Operating Modes and Junction Biasing
| Operating Mode | Base-Emitter Junction (BEJ) | Base-Collector Junction (BCJ) | Functional Application |
|:---|:---:|:---:|:---|
| **Cutoff** | Reverse Biased ($V_{BE} < 0.7\text{ V}$) | Reverse Biased | Digital switch "OFF" ($I_C \approx 0$) |
| **Forward Active** | Forward Biased ($V_{BE} \approx 0.7\text{ V}$) | Reverse Biased | Linear analog signal amplification |
| **Saturation** | Forward Biased ($V_{BE} \approx 0.7\text{ V}$) | Forward Biased | Digital switch "ON" ($V_{CE,\text{sat}} \approx 0.2\text{ V}$) |
| **Reverse Active** | Reverse Biased | Forward Biased | Inefficient inverted operation (low gain) |

### 1.2 Fundamental Current Relationships
Kirchhoff's Current Law applied to the transistor body yields:
$$I_E = I_C + I_B$$

In the forward active mode:
* Common-emitter DC current gain ($\beta$ or $h_{FE}$):
  $$I_C = \beta \cdot I_B \quad (\text{typical values: } 50 \le \beta \le 400)$$
* Common-base DC current gain ($\alpha$):
  $$\alpha = \frac{I_C}{I_E} = \frac{\beta}{\beta + 1} \approx 0.980 - 0.998$$
* Emitter current expressed via base current:
  $$I_E = (\beta + 1) I_B$$

---

## 2. DC Biasing Networks and Q-Point Stability

To amplify AC signals without non-linear clipping, the transistor must be biased at a stable quiescent operating point ($Q$-point: $I_{CQ}, V_{CEQ}$) in the active region.

### 2.1 Voltage-Divider Biasing (Four-Resistor Topology)
Voltage-divider biasing provides excellent immunity against variations in transistor $\beta$ and operating temperature.

```text
       +V_CC
         │
    ┌────┴────┐
    │         │
   [R1]      [RC]
    │         │
    ├─── B ───┤ C  (NPN Transistor)
    │         │
   [R2]      [RE]
    │         │
   GND       GND
```

#### Exact Thevenin Analysis:
1. Equivalent base circuit parameters:
   $$V_{\text{th}} = V_{CC} \cdot \frac{R_2}{R_1 + R_2}, \quad R_{\text{th}} = R_1 \parallel R_2 = \frac{R_1 R_2}{R_1 + R_2}$$
2. KVL around Base-Emitter loop:
   $$V_{\text{th}} - I_B R_{\text{th}} - V_{BE} - I_E R_E = 0$$
   Substituting $I_E = (\beta + 1) I_B$:
   $$I_B = \frac{V_{\text{th}} - V_{BE}}{R_{\text{th}} + (\beta + 1) R_E}$$
3. Collector current and operating collector-emitter voltage:
   $$I_C = \beta I_B$$
   $$V_{CE} = V_{CC} - I_C R_C - I_E R_E \approx V_{CC} - I_C (R_C + R_E)$$

#### Approximate Rule of Thumb ($\beta$-Independent Condition):
If the divider current satisfies $\beta R_E \ge 10 R_2$, base loading can be neglected:
$$V_B \approx V_{\text{th}} = V_{CC} \frac{R_2}{R_1 + R_2}$$
$$V_E = V_B - V_{BE} \approx V_B - 0.7\text{ V}$$
$$I_C \approx I_E = \frac{V_E}{R_E}$$

---

## 3. The DC Load Line and Dynamic Range

Writing KVL across the collector-emitter loop:
$$V_{CE} = V_{CC} - I_C (R_C + R_E) \implies I_C = -\frac{1}{R_C + R_E} V_{CE} + \frac{V_{CC}}{R_C + R_E}$$

* **Cutoff Point ($I_C = 0$)**: $V_{CE,\text{cutoff}} = V_{CC}$.
* **Saturation Point ($V_{CE} \approx 0$)**: $I_{C,\text{sat}} = \frac{V_{CC}}{R_C + R_E}$.
* Optimal linear dynamic range is achieved when the $Q$-point sits near the center of the active region:
  $$V_{CEQ} \approx \frac{V_{CC}}{2}$$

---

## 4. Small-Signal Common-Emitter (CE) Amplifier

### 4.1 Dynamic Emitter Resistance ($r_e$)
At DC operating current $I_C$:
$$r_e = \frac{V_T}{I_E} \approx \frac{26\text{ mV}}{I_{CQ}}$$

### 4.2 Key AC Amplifier Metrics (Bypassed Emitter Resistor $C_E$)
1. **Input Impedance ($Z_{\text{in}}$)**:
   $$Z_{\text{in}} = R_1 \parallel R_2 \parallel (\beta \cdot r_e)$$
2. **Output Impedance ($Z_{\text{out}}$)**:
   $$Z_{\text{out}} \approx R_C$$
3. **Small-Signal Voltage Gain ($A_v$)**:
   $$A_v = \frac{v_{\text{out}}}{v_{\text{in}}} = -\frac{R_C \parallel R_L}{r_e}$$
   The negative sign denotes an intrinsic $180^\circ$ phase inversion between input and output waveforms.

