# Practice Exercises: Circuit Theorems and Semiconductor Devices

This drill document provides comprehensive solved exercises covering DC circuit theorems, diode rectification, Zener regulation, and BJT amplifier biasing.

---

## Section 1: DC Resistive Circuits and Network Theorems

### Problem 1: Voltage and Current Division
**Problem:** In the circuit below, $V_S = 36\text{ V}$, $R_1 = 6\,\Omega$, $R_2 = 12\,\Omega$, and $R_3 = 4\,\Omega$. $R_2$ and $R_3$ are connected in parallel, and their combination is in series with $R_1$. Calculate the current flowing through $R_3$ and the total power dissipated by the circuit.

**Step-by-Step Solution:**
1. Compute parallel equivalent resistance $R_p$ of $R_2$ and $R_3$:
   $$R_p = \frac{R_2 \cdot R_3}{R_2 + R_3} = \frac{12 \cdot 4}{12 + 4} = \frac{48}{16} = 3\,\Omega$$
2. Compute total circuit resistance:
   $$R_{\text{total}} = R_1 + R_p = 6\,\Omega + 3\,\Omega = 9\,\Omega$$
3. Total source current $I_S$:
   $$I_S = \frac{V_S}{R_{\text{total}}} = \frac{36\text{ V}}{9\,\Omega} = 4\text{ A}$$
4. Voltage across the parallel combination $V_p$:
   $$V_p = I_S \cdot R_p = 4\text{ A} \cdot 3\,\Omega = 12\text{ V}$$
5. Current through $R_3$ by Ohm's Law (or current division):
   $$I_3 = \frac{V_p}{R_3} = \frac{12\text{ V}}{4\,\Omega} = 3\text{ A}$$
6. Total power dissipated:
   $$P_{\text{total}} = V_S \cdot I_S = 36\text{ V} \cdot 4\text{ A} = 144\text{ W}$$

---

### Problem 2: Thevenin Equivalent Circuit
**Problem:** A network consists of a $20\text{ V}$ independent voltage source in series with an $8\,\Omega$ resistor, shunted by a $12\,\Omega$ resistor across terminals $A-B$. Determine the Thevenin equivalent circuit ($V_{\text{th}}, R_{\text{th}}$).

**Step-by-Step Solution:**
1. **Thevenin Voltage $V_{\text{th}}$**:
   The open-circuit voltage across terminals $A-B$ is determined by the voltage divider between the $8\,\Omega$ and $12\,\Omega$ resistors:
   $$V_{\text{th}} = V_{AB,\text{oc}} = 20\text{ V} \cdot \frac{12\,\Omega}{8\,\Omega + 12\,\Omega} = 20 \cdot \frac{12}{20} = 12\text{ V}$$
2. **Thevenin Resistance $R_{\text{th}}$**:
   Deactivate the independent voltage source (replace with a short circuit). The resistance seen looking into terminals $A-B$ is the parallel combination of $8\,\Omega$ and $12\,\Omega$:
   $$R_{\text{th}} = 8\,\Omega \parallel 12\,\Omega = \frac{8 \cdot 12}{8 + 12} = \frac{96}{20} = 4.8\,\Omega$$
3. Thevenin Equivalent: An ideal voltage source $V_{\text{th}} = 12\text{ V}$ in series with $R_{\text{th}} = 4.8\,\Omega$.

---

## Section 2: Diode Circuits and Regulators

### Problem 3: Zener Diode Voltage Regulator
**Problem:** A Zener diode with $V_Z = 6.8\text{ V}$ and maximum power rating $P_{Z,\text{max}} = 500\text{ mW}$ regulates an input voltage varying between $10\text{ V}$ and $14\text{ V}$. The load resistor draws current between $I_L = 10\text{ mA}$ and $30\text{ mA}$. If $I_{Z,\text{min}} = 5\text{ mA}$, determine the allowable range for the series current-limiting resistor $R_S$.

**Step-by-Step Solution:**
1. Maximum allowable Zener current:
   $$I_{Z,\text{max}} = \frac{P_{Z,\text{max}}}{V_Z} = \frac{0.500\text{ W}}{6.8\text{ V}} \approx 73.5\text{ mA}$$
2. To guarantee regulation under worst-case low input voltage and high load current:
   $$R_{S,\text{max}} = \frac{V_{\text{in,min}} - V_Z}{I_{Z,\text{min}} + I_{L,\text{max}}} = \frac{10\text{ V} - 6.8\text{ V}}{5\text{ mA} + 30\text{ mA}} = \frac{3.2\text{ V}}{35\text{ mA}} \approx 91.4\,\Omega$$
3. To prevent Zener burnout under worst-case high input voltage and low load current:
   $$R_{S,\text{min}} = \frac{V_{\text{in,max}} - V_Z}{I_{Z,\text{max}} + I_{L,\text{min}}} = \frac{14\text{ V} - 6.8\text{ V}}{73.5\text{ mA} + 10\text{ mA}} = \frac{7.2\text{ V}}{83.5\text{ mA}} \approx 86.2\,\Omega$$
4. Allowable resistance window: $86.2\,\Omega \le R_S \le 91.4\,\Omega$. Selecting a standard resistor $R_S = 91\,\Omega$ ensures safe regulation.

---

## Section 3: BJT Transistor Biasing

### Problem 4: Voltage-Divider Biased BJT Operating Point
**Problem:** An NPN BJT circuit with $V_{CC} = 18\text{ V}$ has bias resistors $R_1 = 56\text{ k}\Omega$, $R_2 = 12\text{ k}\Omega$, collector resistor $R_C = 2.2\text{ k}\Omega$, and emitter resistor $R_E = 680\,\Omega$. The transistor has $\beta = 100$ and $V_{BE} = 0.7\text{ V}$. Find the quiescent operating point ($I_{CQ}, V_{CEQ}$).

**Step-by-Step Solution:**
1. Compute Thevenin equivalent base voltage and resistance:
   $$V_{\text{th}} = V_{CC} \cdot \frac{R_2}{R_1 + R_2} = 18 \cdot \frac{12}{56 + 12} = 18 \cdot \frac{12}{68} \approx 3.176\text{ V}$$
   $$R_{\text{th}} = R_1 \parallel R_2 = \frac{56 \cdot 12}{68} \approx 9.882\text{ k}\Omega$$
2. Base current $I_B$ from Base-Emitter KVL:
   $$I_B = \frac{V_{\text{th}} - V_{BE}}{R_{\text{th}} + (\beta + 1) R_E} = \frac{3.176 - 0.7}{9882 + (101 \cdot 680)} = \frac{2.476}{9882 + 68680} = \frac{2.476}{78562} \approx 31.52\,\mu\text{A}$$
3. Quiescent Collector Current $I_{CQ}$:
   $$I_{CQ} = \beta \cdot I_B = 100 \cdot 31.52\,\mu\text{A} \approx 3.152\text{ mA}$$
4. Quiescent Collector-Emitter Voltage $V_{CEQ}$:
   $$I_E = (\beta + 1) I_B = 101 \cdot 31.52\,\mu\text{A} \approx 3.184\text{ mA}$$
   $$V_{CEQ} = V_{CC} - I_{CQ} R_C - I_E R_E$$
   $$V_{CEQ} = 18 - (3.152\text{ mA} \cdot 2.2\text{ k}\Omega) - (3.184\text{ mA} \cdot 0.680\text{ k}\Omega)$$
   $$V_{CEQ} = 18 - 6.934 - 2.165 = 8.90\text{ V}$$
5. Quiescent Point: $Q = (I_{CQ} = 3.15\text{ mA}, V_{CEQ} = 8.90\text{ V})$. Since $V_{CEQ} > 0.2\text{ V}$ and $I_{CQ} > 0$, the BJT is operating in the linear forward active region.

