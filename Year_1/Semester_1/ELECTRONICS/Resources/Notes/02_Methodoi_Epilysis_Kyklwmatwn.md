# 02_Methodoi_Epilysis_Kyklwmatwn Documentation

This lecture covers circuit analysis methods: Kirchhoff's laws, mesh analysis, nodal analysis, Thevenin and Norton theorems, and maximum power transfer. It also introduces measurement instruments and additional circuit elements such as voltage dividers, current dividers, and variable resistors.

---

## 1. Conceptual Foundation

Circuit analysis problems involve determining unknown voltages and currents in networks of resistors, independent/dependent sources, and other components. Real-world circuits can be complex, requiring systematic solution methods beyond simple Ohm's law. This lecture presents the theoretical tools needed to solve any linear resistive circuit.

---

## 2. Formal Definitions and Models

### 2.1 Basic Circuit Elements

| Element | Description |
|:--------|:------------|
| Energy source | Voltage or current source |
| Conductors | Wires with negligible resistance |
| Insulators | Materials blocking current flow |
| Semiconductors | Materials with controlled conductivity |
| Control devices | Switches, potentiometers |
| Protection devices | Relays, fuses |

### 2.2 Independent and Dependent Sources

| Source Type | Ideal Behavior | Symbol |
|:------------|:---------------|:-------|
| Independent voltage source | Maintains constant $V$ regardless of $I$ | Circle with $\pm$ |
| Independent current source | Maintains constant $I$ regardless of $V$ | Circle with arrow |
| Dependent (controlled) voltage source | $V = f(V_x, I_x)$ elsewhere | Diamond shape |
| Dependent (controlled) current source | $I = f(V_x, I_x)$ elsewhere | Diamond shape |

### 2.3 Power, Energy, Cost

**Power:**

$$
P = V \cdot I
$$

Unit: W (Watt).

**Energy:**

$$
W = P \cdot t
$$

Unit: J (Joule) or kWh (kilowatt-hour).

**Energy cost:**

$$
\text{Cost} = \text{Price per unit energy} \times \text{Energy consumed}
$$

---

## 3. Measurement Instruments

### 3.1 Classification by Operating Principle

| Type | Principle |
|:-----|:----------|
| Moving coil | Electrodynamic |
| Moving iron | Electromagnetic |
| Electrodynamic | Mutual induction |
| Electrostatic | Electrostatic force |
| Thermal | Heat effect |
| Induction | Electromagnetic induction |

### 3.2 Classification by Measured Quantity

| Instrument | Measures | Connection | Key Property |
|:-----------|:---------|:-----------|:-------------|
| Ammeter | Current $I$ | In series | Very low internal resistance ($< 1\Omega$) |
| Voltmeter | Voltage $V$ | In parallel | Very high internal resistance ($> 10k\Omega$) |
| Wattmeter | Power $P$ | -- | -- |
| Frequency meter | Frequency $f$ | -- | -- |
| Ohmmeter | Resistance $R$ | -- | Uses internal battery; remove circuit power |

### 3.3 Classification by Display Method

- **Indicating:** Show value via pointer or digital display.
- **Recording:** Record value over time.
- **Integrating:** Provide cumulative reading (e.g., energy meter).

### 3.4 Panel Instruments and Multimeters

**Panel instruments:** Permanently connected analog/digital instruments measuring one quantity ($I$, $V$, or $R$).

**Multimeters:** Combine multiple measurement functions (voltage, current, resistance) in one instrument.

### 3.5 Measurement Procedures

**Resistance measurement:**
1. Disconnect all power sources.
2. Use the ohmmeter's internal battery.
3. Ensure the resistor is isolated from other components.
4. Polarity does not matter.

**Voltage measurement:**
1. Power must be applied to the circuit.
2. Select DC or AC mode.
3. Start with the highest range.
4. Respect polarity: black (COM) to negative, red to positive.

**Current measurement:**
1. Break the circuit to insert the ammeter in series.
2. Power must be applied.
3. Select DC/AC mode, start with highest range.
4. Respect polarity.

---

## 4. Step-by-Step Mechanism: Circuit Analysis Methods

### 4.1 Kirchhoff's Laws

**Definitions:**
- **Branch:** A group of connected elements forming a two-terminal set.
- **Node:** A common point where two or more branches meet.
- **Loop:** Any closed path of branches.

**KCL (Kirchhoff's Current Law):**
The algebraic sum of all currents at any node equals zero.

$$
\sum_{k=1}^{n} I_k = 0
$$

**KVL (Kirchhoff's Voltage Law):**
The algebraic sum of all voltages around any loop equals zero.

$$
\sum_{k=1}^{n} V_k = 0
$$

### 4.2 Mesh Analysis (M.A.B.)

**Theorem:** A circuit with $b$ branches and $n$ nodes has $b - n + 1$ independent meshes. Applying KVL to each mesh yields independent equations.

**Matrix form for a 2-mesh circuit:**

$$
\begin{aligned}
R_{11} I_1 + R_{12} I_2 &= \Sigma V_1 \\
R_{21} I_1 + R_{22} I_2 &= \Sigma V_2
\end{aligned}
$$

Where $R_{11}$ is the sum of resistances in mesh 1, $R_{12} = R_{21}$ is the negative sum of common resistances, and $\Sigma V_1$ is the sum of voltage sources in mesh 1.

**Best suited for:** Circuits with many voltage sources.

### 4.3 Nodal Analysis (M.K.)

**Theorem:** A circuit with $n$ nodes requires $n-1$ independent KCL equations.

**Matrix form for a 2-node circuit:**

$$
\begin{aligned}
G_{11} V_1 + G_{12} V_2 &= \Sigma I_1 \\
G_{21} V_1 + G_{22} V_2 &= \Sigma I_2
\end{aligned}
$$

Where $G_{11}$ is the sum of conductances connected to node 1, $G_{12} = G_{21}$ is the negative sum of common conductances, and $\Sigma I_1$ is the sum of current sources entering node 1.

**Best suited for:** Circuits with many current sources.

### 4.4 Thevenin's Theorem

Any two-terminal linear circuit of resistors and independent sources can be replaced by an equivalent circuit consisting of a single voltage source $V_{Th}$ in series with a single resistor $R_{Th}$.

**Procedure:**
1. $V_{Th}$ = open-circuit voltage between terminals A and B.
2. $R_{Th}$ = equivalent resistance between A and B with all independent sources deactivated (voltage sources short-circuited, current sources open-circuited).

### 4.5 Norton's Theorem

Any two-terminal linear circuit can be replaced by an equivalent circuit consisting of a single current source $I_N$ in parallel with a single resistor $R_N$.

**Procedure:**
1. $I_N$ = short-circuit current between terminals A and B.
2. $R_N$ = $R_{Th}$ (same as Thevenin resistance).

### 4.6 Thevenin-Norton Duality

Two circuits are equivalent if for any load, the load current and voltage are identical.

**Source transformation:**

$$
V_{Th} = I_N \cdot R_N, \quad I_N = \frac{V_{Th}}{R_{Th}}
$$

### 4.7 Maximum Power Transfer Theorem

Maximum power is delivered to a load when the load resistance equals the source's internal resistance (or Thevenin resistance):

$$
R_L = R_{source} \quad \text{(or } R_L = R_{Th} \text{)}
$$

---

## 5. Additional Circuits

### 5.1 Voltage Divider

$$
V_{out} = V_{in} \cdot \frac{R_2}{R_1 + R_2}
$$

### 5.2 Current Divider

$$
I_{R1} = I_{total} \cdot \frac{R_2}{R_1 + R_2}, \quad I_{R2} = I_{total} \cdot \frac{R_1}{R_1 + R_2}
$$

### 5.3 Variable Resistors

| Type | Connection | Function |
|:-----|:-----------|:---------|
| Rheostat | In series | Controls current |
| Potentiometer | In parallel/shunt | Controls voltage |

### 5.4 Source Transformations

**Voltage source to current source:**

$$
I = \frac{V}{R}, \quad \text{same } R \text{ in parallel}
$$

**Current source to voltage source:**

$$
V = I \cdot R, \quad \text{same } R \text{ in series}
$$

### 5.5 Simplification Rules

- A resistor in parallel with a voltage source can be omitted.
- A resistor in series with a current source can be omitted.

---

## 6. Worked Examples

### Exercise 1: Kirchhoff's Current Law

**Problem:** At a node, currents $I_1 = 2\,\text{A}$ (entering), $I_2 = 3\,\text{A}$ (entering), $I_3 = 1\,\text{A}$ (leaving). Find $I_4$ (leaving).

**Solution:**

Applying KCL: sum of entering currents = sum of leaving currents.

$$
I_1 + I_2 = I_3 + I_4
$$

$$
2 + 3 = 1 + I_4 \quad \Rightarrow \quad I_4 = 5 - 1 = 4\,\text{A}
$$

---

### Exercise 2: Kirchhoff's Voltage Law

**Problem:** A loop contains a $12\,\text{V}$ source, a $2\,k\Omega$ resistor with $3\,\text{mA}$ flowing, and an unknown voltage $V_x$ of the same polarity as the source. Find $V_x$.

**Solution:**

KVL: $12\,\text{V} - (2\,k\Omega \times 3\,\text{mA}) - V_x = 0$

Voltage across resistor: $V_R = 2000 \times 0.003 = 6\,\text{V}$

$$
12 - 6 - V_x = 0 \quad \Rightarrow \quad V_x = 6\,\text{V}
$$

---

### Exercise 3: Thevenin Equivalent -- Simple Voltage Divider

**Problem:** Find the Thevenin equivalent between terminals A and B for a circuit with $V_s = 10\,\text{V}$, $R_1 = 2\,k\Omega$, $R_2 = 3\,k\Omega$ in series.

**Solution:**

$V_{Th}$ is the open-circuit voltage (voltage across $R_2$):

$$
V_{Th} = 10 \times \frac{3}{2+3} = 10 \times 0.6 = 6\,\text{V}
$$

$R_{Th}$ is the resistance seen from A-B with the source shorted:

$$
R_{Th} = R_1 \parallel R_2 = \frac{2 \times 3}{2 + 3} = \frac{6}{5} = 1.2\,k\Omega
$$

---

### Exercise 4: Thevenin Equivalent with Multiple Sources

**Problem:** Find $V_{Th}$ and $R_{Th}$ for a circuit with $V_1 = 5\,\text{V}$ in series with $R_1 = 1\,k\Omega$, and $V_2 = 10\,\text{V}$ in series with $R_2 = 2\,k\Omega$, both connected to terminal A with the other ends at ground.

**Solution:**

$V_{Th}$ is the open-circuit voltage at A. Using nodal analysis or superposition:

$$
V_{Th} = \frac{V_1/R_1 + V_2/R_2}{1/R_1 + 1/R_2} = \frac{5/1000 + 10/2000}{1/1000 + 1/2000} = \frac{0.005 + 0.005}{0.001 + 0.0005} = \frac{0.01}{0.0015} = 6.67\,\text{V}
$$

$R_{Th}$: short sources, $R_1 \parallel R_2 = \frac{1 \times 2}{1+2} = 0.667\,k\Omega = 667\,\Omega$

---

### Exercise 5: Maximum Power Transfer

**Problem:** A source has $V_{Th} = 12\,\text{V}$ and $R_{Th} = 50\,\Omega$. Find the load resistance for maximum power transfer and the maximum power.

**Solution:**

Maximum power when $R_L = R_{Th} = 50\,\Omega$.

Load current: $I = \frac{V_{Th}}{R_{Th} + R_L} = \frac{12}{50+50} = 0.12\,\text{A}$

Maximum power: $P_{max} = I^2 \cdot R_L = (0.12)^2 \times 50 = 0.0144 \times 50 = 0.72\,\text{W}$

---

### Exercise 6: Norton Equivalent from Thevenin

**Problem:** Given $V_{Th} = 15\,\text{V}$ and $R_{Th} = 3\,k\Omega$, find the Norton equivalent.

**Solution:**

$R_N = R_{Th} = 3\,k\Omega$

$I_N = \frac{V_{Th}}{R_{Th}} = \frac{15}{3000} = 5\,\text{mA}$

The Norton circuit: $5\,\text{mA}$ current source in parallel with $3\,k\Omega$.

---

### Exercise 7: Mesh Analysis -- Two Meshes

**Problem:** Find $I_1$ and $I_2$ for a circuit with $V_1 = 10\,\text{V}$, $V_2 = 5\,\text{V}$, $R_1 = 1\,k\Omega$ (mesh 1), $R_2 = 2\,k\Omega$ (shared), $R_3 = 1\,k\Omega$ (mesh 2). $V_1$ in mesh 1, $V_2$ in mesh 2.

**Solution:**

Mesh equations:

$$
\begin{aligned}
(R_1 + R_2)I_1 - R_2 I_2 &= V_1 \\
-R_2 I_1 + (R_2 + R_3)I_2 &= -V_2
\end{aligned}
$$

$$
\begin{aligned}
(1000 + 2000)I_1 - 2000 I_2 &= 10 \\
-2000 I_1 + (2000 + 1000)I_2 &= -5
\end{aligned}
$$

$$
\begin{aligned}
3000 I_1 - 2000 I_2 &= 10 \\
-2000 I_1 + 3000 I_2 &= -5
\end{aligned}
$$

Solving: $I_1 = 4\,\text{mA}$, $I_2 = 1\,\text{mA}$.

---

### Exercise 8: Nodal Analysis -- Two Nodes

**Problem:** Find $V_1$ and $V_2$ for a circuit with $I_1 = 2\,\text{mA}$ entering node 1, $I_2 = 1\,\text{mA}$ leaving node 2, $R_1 = 1\,k\Omega$ (node 1 to ground), $R_2 = 2\,k\Omega$ (between nodes), $R_3 = 1\,k\Omega$ (node 2 to ground).

**Solution:**

Nodal equations:

$$
\begin{aligned}
(G_1 + G_2)V_1 - G_2 V_2 &= I_1 \\
-G_2 V_1 + (G_2 + G_3)V_2 &= -I_2
\end{aligned}
$$

$$
\begin{aligned}
(0.001 + 0.0005)V_1 - 0.0005 V_2 &= 0.002 \\
-0.0005 V_1 + (0.0005 + 0.001)V_2 &= -0.001
\end{aligned}
$$

$$
\begin{aligned}
0.0015 V_1 - 0.0005 V_2 &= 0.002 \\
-0.0005 V_1 + 0.0015 V_2 &= -0.001
\end{aligned}
$$

Solving: $V_1 = 1.25\,\text{V}$, $V_2 = -0.25\,\text{V}$.

---

## 7. Connections and Cross-References

- Ohm's law (Lecture 01) is the foundation upon which all methods in this lecture are built.
- Thevenin and Norton equivalents are essential for analyzing Zener regulators (Lecture 05) and transistor biasing (Lecture 08).
- Maximum power transfer is critical for amplifier design (Lecture 09).

---

## Exam Tip: Selecting the Right Method

- For circuits with few nodes and many voltage sources, use **mesh analysis**.
- For circuits with few nodes and many current sources, use **nodal analysis**.
- When only the behavior at two terminals is needed, use **Thevenin or Norton**.
- For power delivery problems, use the **maximum power transfer theorem**.
- A common exam mistake is forgetting to deactivate sources when calculating $R_{Th}$: short voltage sources, open current sources.