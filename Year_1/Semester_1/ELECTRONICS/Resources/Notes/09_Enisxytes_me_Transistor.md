# 09_Enisxytes_me_Transistor Documentation

This lecture covers transistor amplifiers: small-signal amplification principles, the six amplifier variants based on biasing circuits, DC analysis for finding the quiescent emitter current, small-signal parameters ($g_m$, $r_\pi$, $r_e'$), and AC analysis using the Pi and T models.

---

## 1. Conceptual Foundation

Amplifiers use a transistor biased in the active region to increase the amplitude of small input signals. The superposition of a small AC signal on the DC bias causes the collector current to vary proportionally, producing an amplified replica of the input at the output. The ratio of output voltage to input voltage is the voltage gain $A_v$.

---

## 2. Formal Definition and Model

### 2.1 Notation

| Quantity | DC Component | AC Component | Total |
|:---------|:-------------|:-------------|:------|
| Base-emitter voltage | $V_{BE}$ | $v_{be}$ | $v_{BE} = V_{BE} + v_{be}$ |
| Collector current | $I_C$ | $i_c$ | $i_C = I_C + i_c$ |
| Base current | $I_B$ | $i_b$ | $i_B = I_B + i_b$ |
| Emitter current | $I_E$ | $i_e$ | $i_E = I_E + i_e$ |

### 2.2 Small-Signal Parameters

**Transconductance ($g_m$):**

$$
g_m = \frac{i_c}{v_{be}} = \frac{I_C}{V_T}
$$

Where $V_T \approx 25\,\text{mV}$ at room temperature.

**Base-emitter resistance looking from base ($r_\pi'$):**

$$
r_\pi' = \frac{v_{be}}{i_b} = \frac{\beta}{g_m} = \frac{\beta V_T}{I_C}
$$

**Emitter resistance looking from emitter ($r_e'$):**

$$
r_e' = \frac{v_{be}}{i_e} = \frac{V_T}{I_E} \approx \frac{25\,\text{mV}}{I_E}
$$

**Relationship between $r_\pi'$ and $r_e'$:**

$$
r_\pi' = (\beta + 1) r_e' \approx \beta r_e'
$$

---

## 3. Step-by-Step Mechanism: Generalized Amplifier Analysis

### Phase A: DC Analysis

1. Draw the DC equivalent circuit (capacitors = open circuits).
2. Identify the biasing configuration (base, emitter, voltage divider, etc.).
3. Calculate $I_E$ (the quiescent emitter current).
4. Compute $r_e' = 25\,\text{mV} / I_E$.

### Phase B: AC Analysis

1. Ground all DC voltage sources (short to ground). Short all capacitors.
2. Draw the Pi model (or T model) of the transistor.
3. Add all input-side resistors and output-side resistors to the model.
4. For Pi model: resistors in the emitter circuit are multiplied by $\beta$ and placed in the base leg.
5. Determine $v_{in}$ and $v_{out}$ relationships.
6. Calculate voltage gain $A_v = v_{out} / v_{in}$.
7. If $R_g$ is present, apply the voltage divider: $v_{in} = v_g \cdot Z_{inStage} / (R_g + Z_{inStage})$.

### 2.3 Pi Model (Common Emitter)

- Input impedance looking into base: $Z_{inBase} = \beta (r_e' + R_E)$.
- Stage input impedance: $Z_{inStage} = R_1 \parallel R_2 \parallel Z_{inBase}$.
- Output resistance: $r_c = R_C \parallel R_L$.
- Voltage gain:

$$
A_v = \frac{v_{out}}{v_{in}} = \frac{i_c \cdot r_c}{i_b \cdot \beta (r_e' + R_E)} = \frac{r_c}{r_e' + R_E}
$$

### 2.4 Bypass Capacitor Effect

A bypass capacitor placed in parallel with $R_E$ shorts $R_E$ for AC signals, removing it from the gain equation:

$$
A_v = \frac{r_c}{r_e'}
$$

This maximizes the voltage gain.

### 2.5 Input Resistance $R_g$

When $R_g$ is present before the coupling capacitor:

$$
v_{in} = v_g \cdot \frac{Z_{inStage}}{R_g + Z_{inStage}}
$$

The overall gain becomes:

$$
A_v(total) = A_v \cdot \frac{Z_{inStage}}{R_g + Z_{inStage}}
$$

---

## 4. Amplifier Configurations (6 Biasing-Based Variants)

All six biasing circuits from Lecture 08 can form the basis of an amplifier by:
1. Adding a coupling capacitor at the input (to block DC from the signal source).
2. Adding a load resistor $R_L$ at the output after a coupling capacitor.
3. Optionally adding $R_g$ or a bypass capacitor.

---

## 5. Worked Examples

### Exercise 1: DC Analysis -- Finding $r_e'$

**Problem:** An amplifier has $I_E = 2\,\text{mA}$. Find $r_e'$.

**Solution:**

$$
r_e' = \frac{25\,\text{mV}}{2\,\text{mA}} = \frac{0.025}{0.002} = 12.5\,\Omega
$$

---

### Exercise 2: Transconductance

**Problem:** A transistor in an amplifier has $I_C = 1.5\,\text{mA}$. Find $g_m$.

**Solution:**

$$
g_m = \frac{I_C}{V_T} = \frac{0.0015}{0.025} = 0.06\,\text{S} = 60\,\text{mS}
$$

---

### Exercise 3: Voltage Gain (Without Bypass Capacitor)

**Problem:** An amplifier has $R_C = 2.2\,k\Omega$, $R_L = 10\,k\Omega$, $R_E = 470\,\Omega$, $r_e' = 12.5\,\Omega$. The biasing is voltage divider with $R_1 = 10\,k\Omega$, $R_2 = 4.7\,k\Omega$. Find $A_v$ without a bypass capacitor.

**Solution:**

$r_c = R_C \parallel R_L = \frac{2.2 \times 10}{2.2 + 10} = \frac{22}{12.2} = 1.80\,k\Omega$

$$
A_v = \frac{r_c}{r_e' + R_E} = \frac{1800}{12.5 + 470} = \frac{1800}{482.5} = 3.73
$$

---

### Exercise 4: Voltage Gain (With Bypass Capacitor)

**Problem:** Same as Exercise 3 but with a bypass capacitor across $R_E$.

**Solution:**

With $R_E$ bypassed for AC:

$$
A_v = \frac{r_c}{r_e'} = \frac{1800}{12.5} = 144
$$

The gain increases significantly.

---

### Exercise 5: Input Impedance

**Problem:** For the amplifier in Exercise 3, find $Z_{inStage}$ if $\beta = 120$.

**Solution:**

$Z_{inBase} = \beta (r_e' + R_E) = 120 \times (12.5 + 470) = 120 \times 482.5 = 57.9\,k\Omega$

$Z_{inStage} = R_1 \parallel R_2 \parallel Z_{inBase} = 10k \parallel 4.7k \parallel 57.9k$

First: $10k \parallel 4.7k = \frac{10 \times 4.7}{14.7} = 3.20\,k\Omega$

Then: $3.20k \parallel 57.9k = \frac{3.20 \times 57.9}{3.20 + 57.9} = \frac{185.3}{61.1} = 3.03\,k\Omega$

---

### Exercise 6: Effect of $R_g$

**Problem:** The amplifier from Exercise 4 has $R_g = 1\,k\Omega$ and $v_g = 10\,\text{mV}$. Find $v_{out}$.

**Solution:**

$Z_{inStage} = 3.03\,k\Omega$ (from Exercise 5).

$v_{in} = v_g \cdot \frac{Z_{inStage}}{R_g + Z_{inStage}} = 10 \times \frac{3.03}{1 + 3.03} = 10 \times 0.752 = 7.52\,\text{mV}$

$A_v = 144$ (from Exercise 4).

$v_{out} = A_v \cdot v_{in} = 144 \times 7.52 = 1083\,\text{mV} = 1.083\,\text{V}$

---

### Exercise 7: DC Analysis for $I_E$ in Voltage Divider Bias

**Problem:** $V_{CC} = 15\,\text{V}$, $R_1 = 22\,k\Omega$, $R_2 = 10\,k\Omega$, $R_E = 1\,k\Omega$, $\beta = 150$. Find $I_E$ and $r_e'$.

**Solution:**

$V_B = \frac{10}{22 + 10} \times 15 = \frac{10}{32} \times 15 = 4.69\,\text{V}$

$I_E = \frac{4.69 - 0.7}{1000} = \frac{3.99}{1000} = 3.99\,\text{mA}$

$r_e' = \frac{25}{3.99} = 6.27\,\Omega$

---

### Exercise 8: Output Voltage with Bypass Capacitor and $R_g$

**Problem:** Using the amplifier from Exercise 7 with $R_C = 3.3\,k\Omega$, $R_L = 10\,k\Omega$, $R_g = 600\,\Omega$, $v_g = 5\,\text{mV}$, $\beta = 150$, and a bypass capacitor. Find $v_{out}$.

**Solution:**

$r_c = 3.3k \parallel 10k = \frac{33}{13.3} = 2.48\,k\Omega$

$A_v = \frac{r_c}{r_e'} = \frac{2480}{6.27} = 396$

$Z_{inBase} = \beta \cdot r_e' = 150 \times 6.27 = 941\,\Omega$

$Z_{inStage} = 22k \parallel 10k \parallel 941 = 3.20k \parallel 941$

$3.20k \parallel 941 = \frac{3200 \times 941}{3200 + 941} = \frac{3.01 \times 10^6}{4141} = 727\,\Omega$

$v_{in} = 5 \times \frac{727}{600 + 727} = 5 \times 0.548 = 2.74\,\text{mV}$

$v_{out} = 396 \times 2.74 = 1085\,\text{mV} = 1.085\,\text{V}$

---

## 6. Connections and Cross-References

- Biasing circuits from Lecture 08 form the DC foundation for all amplifiers.
- The $0.7\,\text{V}$ $V_{BE}$ drop and BJT parameters ($\beta$, $\alpha$) are from Lecture 07.
- Capacitor behavior (Lecture 01) explains coupling and bypass functions.
- Thevenin analysis (Lecture 02) is used for $R_g$ voltage divider calculations.

---

## Exam Tip: Bypass Capacitor Impact

The bypass capacitor is the single most impactful component in amplifier gain. Without it, gain is $r_c / (r_e' + R_E)$. With it, gain becomes $r_c / r_e'$ -- typically 10-50 times higher. When an exam problem shows a capacitor in parallel with $R_E$, it is a bypass capacitor and should be treated as a short circuit in AC analysis.