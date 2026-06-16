# 04_Diodos Documentation

This lecture covers the PN junction diode: its construction, electrical characteristics, Shockley equation, load line analysis, operating point, static and dynamic resistance, and the three approximation models (ideal, typical, real).

---

## 1. Conceptual Foundation

A diode is the practical implementation of a PN junction, providing controlled, unidirectional current flow. It functions as an electronic valve -- allowing current in one direction (forward bias) while blocking it in the opposite direction (reverse bias). This fundamental switching property underlies rectification, signal clipping, and countless other applications.

---

## 2. Formal Definition and Model

### 2.1 Crystal Diode (PN Junction Implementation)

- Two-terminal asymmetric device.
- **Anode:** P-type terminal.
- **Cathode:** N-type terminal.
- Symbol: arrow (anode to cathode direction) with a bar at the cathode.
- Marked on physical diodes with a band at the cathode end.

### 2.2 I-V Characteristic Regions

| Bias Condition | Behavior | Resistance |
|:---------------|:---------|:-----------|
| No bias | Depletion region exists; $V_0 \approx 0.6-0.7\,\text{V}$ for Si | High |
| Forward bias ($V > V_T$) | Conduction | Low ($50-100\,\Omega$) |
| Reverse bias ($V < 0$) | Blocking | High ($> 10\,k\Omega$) |
| Breakdown ($V < -V_{br}$) | Avalanche (destructive for standard diodes) | Very low |

### 2.3 Threshold Voltage ($V_T$)

- Silicon: $V_T \approx 0.7\,\text{V}$
- Germanium: $V_T \approx 0.2-0.3\,\text{V}$

### 2.4 Shockley Equation

The diode current as a function of applied voltage:

$$
I_D = I_S \left[ \exp\left(\frac{V_D}{\eta V_T}\right) - 1 \right]
$$

Where:
- $I_S$ = reverse saturation current.
- $V_D$ = voltage across the diode.
- $\eta$ = ideality factor ($1 \leq \eta \leq 2$).
- $V_T$ = thermal voltage ($\approx 25\,\text{mV}$ at $300\,\text{K}$).

For forward bias with $V_D \gg V_T$:

$$
I_D \approx I_S \exp\left(\frac{V_D}{\eta V_T}\right)
$$

---

## 3. Key Parameters and Constraints

### 3.1 DC (Static) Resistance

$$
R_{DC} = \frac{V_{DQ}}{I_{DQ}}
$$

### 3.2 AC (Dynamic) Resistance

$$
r_{AC} = \frac{\Delta V_D}{\Delta I_D} \approx \frac{\eta V_T}{I_D}
$$

---

## 4. Step-by-Step Mechanism

### 4.1 Load Line Analysis

For a circuit with a DC source $V_{DD}$, resistor $R$, and diode:

1. Write the KVL equation: $V_{DD} = I_D R + V_D$.
2. Rearrange to load line: $I_D = \frac{V_{DD} - V_D}{R}$.
3. Plot this line on the diode's I-V characteristic.
4. The intersection is the **Q-point** (quiescent operating point).

### 4.2 Three Approximation Models

| Model | Forward Voltage | Forward Resistance | Best For |
|:------|:----------------|:-------------------|:---------|
| 1st: Ideal | $0\,\text{V}$ | $0\,\Omega$ | Quick estimates, large signals |
| 2nd: Typical | $0.7\,\text{V}$ | $0\,\Omega$ | Most practical analysis |
| 3rd: Real | $0.7\,\text{V}$ | $r_d$ (dynamic) | Precise calculations |

**1st Approximation (Ideal Diode):**
- Forward bias = short circuit.
- Reverse bias = open circuit.
- No threshold voltage.

**2nd Approximation (Typical Diode):**
- Ideal diode in series with a $0.7\,\text{V}$ battery.
- Conducts only when $V_D > 0.7\,\text{V}$.
- Reverse bias: open circuit.

**3rd Approximation (Real Diode):**
- Typical diode model plus internal resistance $r_d$.
- Produces the most accurate I-V characteristic.

---

## 5. Worked Examples

### Exercise 1: Ideal Diode -- Forward Bias

**Problem:** A circuit has $V_{DD} = 10\,\text{V}$, $R = 1\,k\Omega$, and an ideal diode in series. Find $I_D$.

**Solution:**

Ideal diode forward bias = short circuit ($V_D = 0$).

$$
I_D = \frac{V_{DD}}{R} = \frac{10}{1000} = 10\,\text{mA}
$$

---

### Exercise 2: Typical Diode Model

**Problem:** Same circuit but use the typical diode model ($V_T = 0.7\,\text{V}$). Find $I_D$.

**Solution:**

$$
I_D = \frac{V_{DD} - V_T}{R} = \frac{10 - 0.7}{1000} = \frac{9.3}{1000} = 9.3\,\text{mA}
$$

---

### Exercise 3: Real Diode Model

**Problem:** Same circuit but diode internal resistance $r_d = 200\,\Omega$. Find $I_D$.

**Solution:**

$$
I_D = \frac{V_{DD} - V_T}{R + r_d} = \frac{10 - 0.7}{1000 + 200} = \frac{9.3}{1200} = 7.75\,\text{mA}
$$

---

### Exercise 4: Diode State Determination

**Problem:** A circuit has $V_{DD} = 5\,\text{V}$, $R = 2.2\,k\Omega$, and a silicon diode. Determine if the diode is forward or reverse biased, and find $I_D$ using the typical model.

**Solution:**

The diode is forward biased (positive voltage to anode, negative to cathode through $R$). Using the typical model:

$$
I_D = \frac{5 - 0.7}{2200} = \frac{4.3}{2200} = 1.95\,\text{mA}
$$

---

### Exercise 5: Reverse Bias

**Problem:** A silicon diode is connected with $V_{DD} = -10\,\text{V}$ (anode negative relative to cathode) and $R = 1\,k\Omega$. Find $I_D$.

**Solution:**

The diode is reverse biased. Using any model:

- Ideal: $I_D = 0$.
- Typical: $I_D = 0$.
- Real: $I_D \approx -I_S$ (negligible, typically $\text{nA}$).

For practical analysis, $I_D \approx 0\,\text{A}$.

---

### Exercise 6: Load Line -- Q-Point

**Problem:** A circuit has $V_{DD} = 12\,\text{V}$, $R = 1\,k\Omega$, and a silicon diode. Find the Q-point using the typical model.

**Solution:**

With $V_D = 0.7\,\text{V}$:

$$
I_D = \frac{12 - 0.7}{1000} = 11.3\,\text{mA}
$$

Q-point: $V_{DQ} = 0.7\,\text{V}$, $I_{DQ} = 11.3\,\text{mA}$.

---

### Exercise 7: Dynamic Resistance Calculation

**Problem:** For a silicon diode operating at $I_D = 5\,\text{mA}$, find the dynamic resistance at room temperature ($V_T = 25\,\text{mV}$, $\eta = 1$).

**Solution:**

$$
r_{AC} = \frac{\eta V_T}{I_D} = \frac{1 \times 0.025}{0.005} = \frac{0.025}{0.005} = 5\,\Omega
$$

---

### Exercise 8: Comparing Models for Low Voltage

**Problem:** For $V_{DD} = 1\,\text{V}$, $R = 100\,\Omega$, find $I_D$ using all three models ($r_d = 200\,\Omega$).

**Solution:**

**1st (Ideal):** $I_D = \frac{1}{100} = 10\,\text{mA}$.

**2nd (Typical):** $I_D = \frac{1 - 0.7}{100} = \frac{0.3}{100} = 3\,\text{mA}$.

**3rd (Real):** $I_D = \frac{1 - 0.7}{100 + 200} = \frac{0.3}{300} = 1\,\text{mA}$.

This demonstrates that at low voltages, the model choice significantly impacts the result.

---

## 6. Connections and Cross-References

- The diode's I-V characteristic derives from PN junction theory (Lecture 03).
- Zener diode operation builds on the breakdown region (Lecture 05).
- Diode applications in rectification (Lecture 06) use the switching model.
- Transistor biasing (Lecture 08) uses the $0.7\,\text{V}$ forward drop of PN junctions.

---

## Exam Tip: Model Selection

When an exam problem does not specify which model to use, solve using the **typical (2nd) model** as it is the most commonly expected approach. The ideal model is acceptable only when signals are much larger than $0.7\,\text{V}$ or when the problem explicitly states "ideal diode." Always state which model you are using.