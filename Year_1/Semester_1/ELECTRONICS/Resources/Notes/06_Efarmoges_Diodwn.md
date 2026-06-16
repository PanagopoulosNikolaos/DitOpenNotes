# 06_Efarmoges_Diodwn Documentation

This lecture covers diode applications in power supply design: rectification (half-wave, full-wave, bridge), smoothing filters, Zener regulation, voltage multipliers, and fault detection in power supplies.

---

## 1. Conceptual Foundation

Electronic devices require stable DC voltages for operation. While batteries can power low-consumption devices, most equipment requires a power supply that converts AC mains voltage to a regulated DC voltage. The process involves four stages: transformation, rectification, filtering, and regulation.

---

## 2. Formal Definition and Model

### 2.1 Power Supply Block Diagram

$$
\text{AC Mains} \rightarrow \text{Step-down Transformer} \rightarrow \text{Rectifier} \rightarrow \text{Filter} \rightarrow \text{Regulator} \rightarrow \text{DC Output}
$$

### 2.2 Rectifier Types

**Half-wave rectifier:**
- Uses a single diode.
- Only positive half-cycles pass; negative half-cycles are blocked.
- Average output: $V_{dc} = 0.318 \times V_{out(max)}$.
- Frequency: $f_{out} = f_{in}$.

**Full-wave rectifier (center-tapped transformer, 2 diodes):**
- Both half-cycles are rectified.
- Average output: $V_{dc} = 0.636 \times V_{out(max)}$.
- Frequency: $f_{out} = 2 \times f_{in}$.
- PIV (Peak Inverse Voltage) per diode: $2 \times V_{out(max)} + 0.7\,\text{V}$.

**Full-wave bridge rectifier (4 diodes):**
- Both half-cycles rectified without center tap.
- Average output: $V_{dc} = 0.636 \times V_{out(max)}$.
- Frequency: $f_{out} = 2 \times f_{in}$.
- PIV per diode: $V_{out(max)} + 0.7\,\text{V}$ (half of center-tap type).

### 2.3 Comparison of Rectifier Types

| Property | Half-Wave | Full-Wave (2-diode) | Full-Wave (Bridge) |
|:---------|:----------|:--------------------|:-------------------|
| Diodes needed | 1 | 2 | 4 |
| Transformer | Simple | Center-tapped | Simple |
| $V_{dc}$ relative to $V_{peak}$ | $0.318 \times V_p$ | $0.636 \times V_p$ | $0.636 \times V_p$ |
| Output frequency | $f_{in}$ | $2 f_{in}$ | $2 f_{in}$ |
| PIV per diode | $V_p$ | $2V_p + 0.7$ | $V_p + 0.7$ |
| DC voltage | Lower | Higher | Higher |
| Ripple | Higher | Lower | Lower |

### 2.4 Three-Phase Rectification

**Three-phase half-wave:** $V_{dc} = 0.831 \times V_{max}$.

**Three-phase full-wave:** Higher efficiency, lower ripple.

### 2.5 Smoothing Filters

**Capacitor filter:**
- Capacitor charges to peak voltage when diode conducts.
- Discharges through $R_L$ when diode is off.
- Ripple voltage: $\Delta V_{out} \approx \frac{I_{out}}{f_{out} \cdot C}$.

**Inductor filter:**
- Series inductor opposes current changes.
- Smoother output for high-current loads.

**Stabilization coefficient ($\gamma$):**

$$
\gamma = \frac{\Delta v_{out}}{\Delta V}
$$

Where $\Delta v_{out}$ is the change in smoothed voltage and $\Delta V$ is the change in rectified voltage. Lower $\gamma$ means better filtering.

### 2.6 Voltage Multipliers

| Type | Configuration | Output |
|:-----|:--------------|:-------|
| Half-wave doubler | 2 diodes + 2 capacitors | $2 \times V_{peak}$ |
| Full-wave doubler | 2 diodes + 2 capacitors | $2 \times V_{peak}$ |
| Tripler | Doubler + 1 diode + 1 capacitor | $3 \times V_{peak}$ |
| Quadrupler | Doubler + extended stages | $4 \times V_{peak}$ |

---

## 3. Step-by-Step Mechanism

### 3.1 Fault Detection in Power Supplies

**Failure symptoms:**
1. Zero output voltage.
2. Low output voltage.
3. Excessive ripple.
4. High output voltage.

**Diagnostic approach:**
1. Observe physical damage.
2. Analyze possible causes using circuit knowledge.
3. Narrow possibilities through measurements.

**Example fault analysis:**
- Correct transformer secondary ($12.7\,\text{V AC}$) + DC measurement of $10.5\,\text{V}$ after filter = no filtering action $\rightarrow$ open filter capacitor.

---

## 4. Worked Examples

### Exercise 1: Half-Wave Rectifier

**Problem:** A half-wave rectifier has $V_{in(peak)} = 10\,\text{V}$ (after transformer) with a silicon diode. Find $V_{dc}$ and PIV.

**Solution:**

Peak output: $V_{out(max)} = 10 - 0.7 = 9.3\,\text{V}$

Average DC: $V_{dc} = 0.318 \times 9.3 = 2.96\,\text{V}$

PIV: $PIV = V_{in(peak)} = 10\,\text{V}$

---

### Exercise 2: Full-Wave Center-Tapped Rectifier

**Problem:** A center-tapped transformer provides $12\,\text{V RMS}$ on each half-secondary. Find $V_{dc}$ and PIV per diode. ($V_{peak} = V_{RMS} \times \sqrt{2}$)

**Solution:**

$V_{peak} = 12 \times 1.414 = 16.97\,\text{V}$

$V_{out(max)} = 16.97 - 0.7 = 16.27\,\text{V}$

$V_{dc} = 0.636 \times 16.27 = 10.34\,\text{V}$

$PIV = 2 \times 16.27 + 0.7 = 33.24\,\text{V}$

---

### Exercise 3: Bridge Rectifier

**Problem:** A bridge rectifier has $V_{in(RMS)} = 12\,\text{V}$. Find $V_{dc}$ and PIV per diode.

**Solution:**

$V_{peak} = 12 \times 1.414 = 16.97\,\text{V}$

Two diode drops: $V_{out(max)} = 16.97 - 1.4 = 15.57\,\text{V}$

$V_{dc} = 0.636 \times 15.57 = 9.90\,\text{V}$

$PIV = 15.57 + 0.7 = 16.27\,\text{V}$

---

### Exercise 4: Capacitor Filter Ripple

**Problem:** A full-wave bridge rectifier supplies $100\,\text{mA}$ to a load. The filter capacitor is $1000\,\mu\text{F}$ and line frequency is $50\,\text{Hz}$. Estimate the ripple voltage.

**Solution:**

Full-wave output frequency: $f_{out} = 2 \times 50 = 100\,\text{Hz}$

Ripple voltage:

$$
\Delta V = \frac{I_{out}}{f_{out} \cdot C} = \frac{0.1}{100 \times 1000 \times 10^{-6}} = \frac{0.1}{0.1} = 1\,\text{V}_{pp}
$$

---

### Exercise 5: Half-Wave Voltage Doubler

**Problem:** Explain the operation of a half-wave voltage doubler with input peak $10\,\text{V}$.

**Solution:**

1. During negative half-cycle: $D_1$ conducts, $C_1$ charges to $V_{peak} = 10\,\text{V}$.
2. During positive half-cycle: $D_2$ conducts, the input ($+10\,\text{V}$) adds to $C_1$'s stored voltage ($+10\,\text{V}$).
3. $C_2$ charges to $10 + 10 = 20\,\text{V}$.
4. Output: $V_{out} \approx 2 \times V_{peak} = 20\,\text{V}$.

---

### Exercise 6: Zener Regulator in Power Supply

**Problem:** A bridge rectifier produces $15\,\text{V}$ DC with $2\,\text{V}$ ripple. A Zener regulator with $V_Z = 5.1\,\text{V}$, $R_S = 100\,\Omega$, drives a $50\,\text{mA}$ load. Determine if regulation is maintained through the ripple cycle.

**Solution:**

$I_L = 50\,\text{mA}$ (constant).

At $V_{in(max)} = 15 + 1 = 16\,\text{V}$:

$$
I_1 = \frac{16 - 5.1}{100} = 109\,\text{mA}, \quad I_Z = 109 - 50 = 59\,\text{mA}
$$

At $V_{in(min)} = 15 - 1 = 14\,\text{V}$:

$$
I_1 = \frac{14 - 5.1}{100} = 89\,\text{mA}, \quad I_Z = 89 - 50 = 39\,\text{mA}
$$

Regulation maintained if $I_Z$ stays within limits.

---

### Exercise 7: Power Supply Fault Diagnosis

**Problem:** A bridge rectifier power supply outputs $0\,\text{V}$. The transformer secondary measures $12\,\text{V AC}$. Where is the fault?

**Solution:**

Since the transformer is working, the fault is after the secondary. Possible causes:
- Open circuit in the bridge rectifier (all four diodes open).
- Blown fuse after the rectifier.
- Shorted filter capacitor (blows fuse or shorts output to ground).
- Open filter inductor/choke.

Check the rectifier output with a DC voltmeter first. If $0\,\text{V}$, test each diode with an ohmmeter.

---

### Exercise 8: Three-Phase Rectifier

**Problem:** A three-phase half-wave rectifier has a phase voltage peak of $20\,\text{V}$. Find the DC output voltage.

**Solution:**

For three-phase half-wave rectification:

$$
V_{dc} = 0.831 \times V_{max} = 0.831 \times 20 = 16.62\,\text{V}
$$

---

## 5. Connections and Cross-References

- Diode models (Lecture 04) determine the $0.7\,\text{V}$ drop used in rectifier calculations.
- Zener regulation (Lecture 05) completes the power supply chain.
- Capacitor charging behavior and time constants (Lecture 01) explain filter operation.
- Transformer theory and mutual induction (Lecture 01) underlie the step-down stage.

---

## Exam Tip: PIV Calculation

The most common mistake in rectifier problems is incorrect PIV calculation. For half-wave: PIV = $V_{peak}$. For center-tapped full-wave: PIV = $2V_{out(max)} + 0.7\,\text{V}$. For bridge: PIV = $V_{out(max)} + 0.7\,\text{V}$. The bridge requires diodes with half the PIV rating compared to the center-tapped design.