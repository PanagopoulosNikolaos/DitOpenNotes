# 08_Polwsi_Transistor Documentation

This lecture covers transistor biasing: the load line, Q-point determination, and six biasing circuit configurations (base bias, emitter bias, voltage divider bias, dual-supply emitter bias, emitter feedback, collector-emitter feedback).

---

## 1. Conceptual Foundation

A transistor amplifier must be biased in the active region to operate linearly. The biasing network establishes DC voltages and currents (the Q-point) that determine where the transistor sits on its characteristic curves. Proper biasing ensures that the transistor remains in the active region across signal swings and temperature variations.

---

## 2. Formal Definition and Model

### 2.1 DC Load Line

The DC load line represents all possible $(I_C, V_{CE})$ operating points for a given circuit.

**Endpoints:**
- $I_{C(sat)}$: $V_{CE} = 0$, $I_C = \frac{V_{CC}}{R_C + R_E}$.
- $V_{CE(cutoff)}$: $I_C = 0$, $V_{CE} = V_{CC}$.

**Methodology for drawing the load line:**
1. Apply KVL to the output loop. Set $V_{CE} = 0$ to find $I_{C(sat)}$.
2. Set $I_C = 0$ to find $V_{CE(cutoff)}$.
3. Plot these two points and connect them with a straight line.

### 2.2 Q-Point Determination

**General methodology:**
1. Calculate $I_C$ using the input loop (usually via $I_B$ or $I_E$ with $\beta$ or $\alpha$).
2. Apply KVL to the output loop to find $V_{CE}$.

---

## 3. Biasing Circuit Configurations

### 3.1 Base Bias (Fixed Bias)

- Single resistor $R_B$ from $V_{BB}$ to base.
- Simple but unstable: Q-point varies strongly with $\beta$.

**Finding Q-point:**
1. KVL input: $V_{BB} = I_B R_B + V_{BE}$ $\rightarrow$ $I_B = \frac{V_{BB} - 0.7}{R_B}$.
2. $I_C = \beta I_B$.
3. KVL output: $V_{CC} = I_C R_C + V_{CE}$ $\rightarrow$ $V_{CE} = V_{CC} - I_C R_C$.

### 3.2 Emitter Bias

- Resistor $R_E$ in the emitter leg stabilizes Q-point.
- KVL input: $V_{BB} = I_B R_B + V_{BE} + I_E R_E$.

**Finding Q-point:**
1. Use input KVL: $V_{BB} = I_B R_B + 0.7 + (\beta + 1) I_B R_E$.
2. Solve for $I_B$, then $I_C = \beta I_B$, $I_E = (\beta + 1) I_B$.
3. KVL output: $V_{CC} = I_C R_C + I_E R_E + V_{CE}$.

**Load line:** $V_{CC} = I_C (R_C + R_E) + V_{CE}$.

### 3.3 Voltage Divider Bias

- Most widely used configuration.
- Base voltage set by $R_1$-$R_2$ divider: $V_B = \frac{R_2}{R_1 + R_2} V_{CC}$.

**Finding Q-point:**
1. $V_B = \frac{R_2}{R_1 + R_2} V_{CC}$.
2. KVL from base to ground through emitter: $V_B = V_{BE} + I_E R_E$ $\rightarrow$ $I_E = \frac{V_B - 0.7}{R_E}$.
3. $I_C \approx I_E$.
4. KVL output: $V_{CC} = I_C R_C + I_E R_E + V_{CE}$.

**Load line:** $V_{CC} = I_C (R_C + R_E) + V_{CE}$.

### 3.4 Dual-Supply Emitter Bias

- Uses both $V_{CC}$ and $V_{EE}$.
- $I_B$ is negligible; Q-point is independent of $\beta$.

**Finding Q-point:**
1. With $I_B \approx 0$, KVL: $V_{EE} = V_{BE} + I_E R_E$ $\rightarrow$ $I_E = \frac{V_{EE} - 0.7}{R_E}$.
2. $I_C \approx I_E$.
3. KVL output: $V_{CC} = I_C R_C + V_{CE} + I_E R_E - V_{EE}$.

### 3.5 Emitter Feedback Bias

- Resistor $R_E$ in emitter, no $R_B$ in base (or minimal).
- Historical significance -- first attempt at Q-point stabilization.

**Finding Q-point:**
1. KVL input: $V_{BB} = V_{BE} + I_E R_E$, using $I_E = (\beta + 1) I_B$.
2. $I_C = \beta I_B$.
3. KVL output: $V_{CC} = I_C R_C + I_E R_E + V_{CE}$.

### 3.6 Collector-Emitter Feedback Bias

- Feedback path from collector to base provides additional stabilization.

**Finding Q-point:**
1. KVL input (loop from collector through $R_B$ to base to emitter): Express $I_C$ and $I_E$ in terms of $I_B$, solve for $I_B$.
2. $I_C = \beta I_B$.
3. KVL output: $V_{CC} = I_C R_C + I_E R_E + V_{CE}$.

---

## 4. Worked Examples

### Exercise 1: Base Bias -- Q-Point

**Problem:** $V_{CC} = 12\,\text{V}$, $R_C = 2.2\,k\Omega$, $R_B = 220\,k\Omega$, $\beta = 100$. Find the Q-point.

**Solution:**

$$
I_B = \frac{V_{CC} - 0.7}{R_B} = \frac{12 - 0.7}{220,000} = \frac{11.3}{220,000} = 51.4\,\mu\text{A}
$$

$$
I_C = \beta I_B = 100 \times 51.4 \times 10^{-6} = 5.14\,\text{mA}
$$

$$
V_{CE} = V_{CC} - I_C R_C = 12 - (0.00514 \times 2200) = 12 - 11.31 = 0.69\,\text{V}
$$

Q-point: $I_{CQ} = 5.14\,\text{mA}$, $V_{CEQ} = 0.69\,\text{V}$.

---

### Exercise 2: Emitter Bias -- Q-Point

**Problem:** $V_{CC} = 15\,\text{V}$, $R_C = 2\,k\Omega$, $R_E = 1\,k\Omega$, $R_B = 100\,k\Omega$, $V_{BB} = 5\,\text{V}$, $\beta = 150$.

**Solution:**

Input KVL: $V_{BB} = I_B R_B + 0.7 + (\beta + 1) I_B R_E$.

$$
5 = I_B \cdot 100{,}000 + 0.7 + 151 \cdot I_B \cdot 1000
$$

$$
5 - 0.7 = I_B (100{,}000 + 151{,}000)
$$

$$
4.3 = I_B \cdot 251{,}000 \quad \Rightarrow \quad I_B = 17.1\,\mu\text{A}
$$

$$
I_C = 150 \times 17.1 \times 10^{-6} = 2.57\,\text{mA}
$$

Output KVL: $V_{CE} = 15 - (2.57\text{m} \times 2000) - (2.59\text{m} \times 1000) = 15 - 5.14 - 2.59 = 7.27\,\text{V}$.

---

### Exercise 3: Voltage Divider Bias -- Q-Point

**Problem:** $V_{CC} = 12\,\text{V}$, $R_1 = 10\,k\Omega$, $R_2 = 4.7\,k\Omega$, $R_C = 1\,k\Omega$, $R_E = 470\,\Omega$, $\beta = 120$.

**Solution:**

$$
V_B = \frac{4.7}{10 + 4.7} \times 12 = \frac{4.7}{14.7} \times 12 = 3.84\,\text{V}
$$

$$
I_E = \frac{V_B - 0.7}{R_E} = \frac{3.84 - 0.7}{470} = \frac{3.14}{470} = 6.68\,\text{mA}
$$

$$
I_C \approx I_E = 6.68\,\text{mA}
$$

$$
V_{CE} = 12 - (6.68\text{m} \times 1000) - (6.68\text{m} \times 470) = 12 - 6.68 - 3.14 = 2.18\,\text{V}
$$

---

### Exercise 4: Dual-Supply -- Q-Point

**Problem:** $V_{CC} = 10\,\text{V}$, $V_{EE} = -10\,\text{V}$, $R_C = 3.3\,k\Omega$, $R_E = 2.2\,k\Omega$, $\beta = 200$.

**Solution:**

With $I_B \approx 0$: $V_{EE} = V_{BE} + I_E R_E$.

$$
10 = 0.7 + I_E \cdot 2200 \quad \Rightarrow \quad I_E = \frac{10 - 0.7}{2200} = 4.23\,\text{mA}
$$

$$
I_C \approx 4.23\,\text{mA}
$$

$$
V_{CE} = 10 - (4.23\text{m} \times 3300) + 10 - (4.23\text{m} \times 2200) = 20 - 13.96 - 9.31 = -3.27\,\text{V}
$$

---

### Exercise 5: Load Line -- Drawing

**Problem:** For a circuit with $V_{CC} = 10\,\text{V}$, $R_C = 2\,k\Omega$, $R_E = 500\,\Omega$, find the load line intercepts.

**Solution:**

$I_{C(sat)}$ (set $V_{CE} = 0$):

$$
I_{C(sat)} = \frac{10}{2000 + 500} = \frac{10}{2500} = 4\,\text{mA}
$$

$V_{CE(cutoff)}$ (set $I_C = 0$):

$$
V_{CE(cutoff)} = 10\,\text{V}
$$

Load line: connects $(0\,\text{mA}, 10\,\text{V})$ to $(4\,\text{mA}, 0\,\text{V})$.

---

### Exercise 6: Base Bias -- Saturation Check

**Problem:** $V_{CC} = 9\,\text{V}$, $R_C = 1\,k\Omega$, $R_B = 50\,k\Omega$, $\beta = 50$. Determine if the transistor is in saturation.

**Solution:**

$$
I_B = \frac{9 - 0.7}{50{,}000} = 166\,\mu\text{A}
$$

$$
I_{C(sat)} = \frac{9}{1000} = 9\,\text{mA}
$$

$I_C$ if active: $I_C = 50 \times 166 \times 10^{-6} = 8.3\,\text{mA}$.

Since $8.3\,\text{mA} < 9\,\text{mA}$, the transistor is in the **active region**.

---

### Exercise 7: Voltage Divider -- Percentage Change

**Problem:** For Exercise 3, if $\beta$ changes from 120 to 200, find the new $I_C$ and the percentage change.

**Solution:**

$V_B$ and $R_E$ determine $I_E$, which is independent of $\beta$ (assuming $I_B \ll I_{divider}$).

$I_E$ remains $6.68\,\text{mA}$, so $I_C \approx 6.68\,\text{mA}$ (essentially unchanged). This demonstrates the stability of voltage divider bias.

---

### Exercise 8: Load Line with Q-Point Verification

**Problem:** For Exercise 3, verify that the Q-point lies on the load line and is in the active region.

**Solution:**

$I_{C(sat)} = \frac{12}{1000 + 470} = \frac{12}{1470} = 8.16\,\text{mA}$.

$V_{CE(cutoff)} = 12\,\text{V}$.

Q-point $(6.68\,\text{mA}, 2.18\,\text{V})$ lies on the line connecting these endpoints. $V_{CE} > 0.2\,\text{V}$ and $I_B > 0$: active region confirmed.

---

## 5. Connections and Cross-References

- Biasing assumes $V_{BE} = 0.7\,\text{V}$ (Lecture 04, Lecture 07).
- The load line method is analogous to the diode load line (Lecture 04).
- These biasing circuits are the foundation for amplifier design (Lecture 09).

---

## Exam Tip: Voltage Divider Stability

Voltage divider bias is the most common exam configuration because it provides the most stable Q-point. The key insight is that $V_B$ is fixed by the divider resistors, so $I_E = (V_B - 0.7)/R_E$ is independent of $\beta$. Always calculate $V_B$ first, then $I_E$, then $V_{CE}$.