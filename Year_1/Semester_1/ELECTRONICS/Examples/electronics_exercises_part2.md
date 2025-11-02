# Electronics Exercises Part 2: Transistors and Amplifiers

This file contains 30 solved exercises covering Bipolar Junction Transistors (BJTs), including their operating principles, biasing circuits, and application as amplifiers.

---

### BJT Fundamentals

**Exercise 1:** What are the two main types of Bipolar Junction Transistors (BJTs)? Describe their basic structure.
**Solution:**
The two main types are NPN and PNP.
- **NPN:** Consists of a thin layer of P-type semiconductor (the base) sandwiched between two layers of N-type semiconductor (the emitter and collector).
- **PNP:** Consists of a thin layer of N-type semiconductor (the base) sandwiched between two layers of P-type semiconductor (the emitter and collector).

**Exercise 2:** What are the three operating regions of a BJT? Briefly describe the bias condition for the two junctions in each region.
**Solution:**
1.  **Cutoff Region:** The transistor is "off." Both the base-emitter (BE) and base-collector (BC) junctions are reverse-biased. No significant current flows.
2.  **Active Region:** The transistor acts as an amplifier. The BE junction is forward-biased, and the BC junction is reverse-biased.
3.  **Saturation Region:** The transistor is fully "on." Both the BE and BC junctions are forward-biased. The collector current is at its maximum value, limited by the external circuit.

**Exercise 3:** Define the DC current gain, $\beta$ (beta), of a BJT. What is its typical range of values?
**Solution:**
The DC current gain, $\beta$ (also known as $h_{FE}$), is the ratio of the collector current ($I_C$) to the base current ($I_B$) when the transistor is operating in the active region.
$$ \beta = \frac{I_C}{I_B} $$
Typical values for $\beta$ in small-signal transistors range from 50 to over 400.

**Exercise 4:** A transistor has a $\beta$ of 150. If the base current ($I_B$) is 20µA, what is the collector current ($I_C$)?
**Solution:**
Using the formula for beta:
$$ I_C = \beta \times I_B = 150 \times 20\mu A = 3000\mu A = 3mA $$

**Exercise 5:** What is the relationship between the emitter current ($I_E$), collector current ($I_C$), and base current ($I_B$)?
**Solution:**
Based on Kirchhoff's Current Law applied to the transistor, the emitter current is the sum of the collector and base currents:
$$ I_E = I_C + I_B $$

**Exercise 6:** For the transistor in Exercise 4 ($\beta=150$, $I_B=20\mu A$, $I_C=3mA$), calculate the emitter current ($I_E$).
**Solution:**
$$ I_E = I_C + I_B = 3mA + 20\mu A = 3mA + 0.02mA = 3.02mA $$

**Exercise 7:** Define the parameter $\alpha$ (alpha) and express it in terms of $\beta$.
**Solution:**
Alpha ($\alpha$) is the ratio of the collector current ($I_C$) to the emitter current ($I_E$).
$$ \alpha = \frac{I_C}{I_E} $$
It represents the fraction of emitter current that reaches the collector. It can be expressed in terms of $\beta$ as:
$$ \alpha = \frac{\beta}{\beta + 1} $$
Alpha is always slightly less than 1.

**Exercise 8:** If a transistor has a $\beta$ of 100, what is its $\alpha$?
**Solution:**
$$ \alpha = \frac{\beta}{\beta + 1} = \frac{100}{100 + 1} = \frac{100}{101} \approx 0.99 $$

**Exercise 9:** Explain why the base region of a BJT is made very thin and lightly doped.
**Solution:**
The base is made thin and lightly doped to ensure that most of the charge carriers injected from the emitter pass through the base to the collector without recombining with the majority carriers in the base. This maximizes the collector current and results in a high current gain ($\beta$).

**Exercise 10:** What does it mean for a transistor to be in "saturation"? What is the approximate value of $V_{CE}$ in saturation?
**Solution:**
Saturation is the state where the transistor is fully "on" and acts like a closed switch. In this state, an increase in base current does not lead to a further increase in collector current, as the collector current is limited by the external circuit components ($R_C$ and $V_{CC}$). The voltage between the collector and emitter, $V_{CE(sat)}$, is very small, typically around 0.2V for a silicon transistor.

---

### BJT Biasing

**Exercise 11:** What is the purpose of biasing a transistor? What is the "Q-point"?
**Solution:**
Biasing is the process of applying DC voltages to a transistor to set its DC operating point, ensuring it operates correctly in the desired region (usually the active region for amplification). The Q-point (Quiescent point) is the specific DC operating point of the transistor, defined by its DC collector current ($I_{CQ}$) and collector-emitter voltage ($V_{CEQ}$) when no AC signal is applied.

**Exercise 12:** Describe the "base bias" configuration. What is a major disadvantage of this biasing method?
**Solution:**
In a base bias circuit, the base resistor ($R_B$) is connected between the DC supply ($V_{CC}$) and the base. The base current is determined solely by $V_{CC}$ and $R_B$. A major disadvantage is that the Q-point is highly dependent on the transistor's $\beta$, which can vary significantly between transistors of the same type and with temperature. This makes the circuit unstable.

**Exercise 13:** In a base bias circuit, $V_{CC} = 12V$ and $R_B = 220k\Omega$. Assuming a silicon transistor ($V_{BE} = 0.7V$), calculate the base current $I_B$.
**Solution:**
Applying KVL to the base-emitter loop:
$$ V_{CC} - I_B R_B - V_{BE} = 0 $$
$$ I_B = \frac{V_{CC} - V_{BE}}{R_B} = \frac{12V - 0.7V}{220k\Omega} = \frac{11.3V}{220 \times 10^3 \Omega} \approx 51.4\mu A $$

**Exercise 14:** For the circuit in Exercise 13, if $\beta = 100$ and $R_C = 1k\Omega$, what are $I_C$ and $V_{CE}$?
**Solution:**
$$ I_C = \beta \times I_B = 100 \times 51.4\mu A = 5.14mA $$
Applying KVL to the collector-emitter loop:
$$ V_{CC} - I_C R_C - V_{CE} = 0 $$
$$ V_{CE} = V_{CC} - I_C R_C = 12V - (5.14mA \times 1k\Omega) = 12V - 5.14V = 6.86V $$
The Q-point is ($I_{CQ} = 5.14mA$, $V_{CEQ} = 6.86V$).

**Exercise 15:** Describe the "voltage-divider bias" configuration. Why is it more stable than base bias?
**Solution:**
Voltage-divider bias uses two resistors ($R_1$ and $R_2$) connected to $V_{CC}$ to create a voltage divider that sets a stable voltage at the base ($V_B$). An emitter resistor ($R_E$) is also included. This configuration is much more stable because the base voltage is held nearly constant, regardless of the transistor's $\beta$. The emitter current, and thus the collector current, is primarily determined by this stable base voltage and the emitter resistor, making the Q-point largely independent of $\beta$.

**Exercise 16:** In a voltage-divider bias circuit, $V_{CC} = 15V$, $R_1 = 10k\Omega$, and $R_2 = 2.2k\Omega$. Calculate the approximate base voltage $V_B$.
**Solution:**
The voltage divider sets the base voltage:
$$ V_B = V_{CC} \times \frac{R_2}{R_1 + R_2} = 15V \times \frac{2.2k\Omega}{10k\Omega + 2.2k\Omega} = 15V \times \frac{2.2}{12.2} \approx 2.7V $$

**Exercise 17:** For the circuit in Exercise 16, if $R_E = 1k\Omega$, calculate the emitter current $I_E$. Assume a silicon transistor.
**Solution:**
The emitter voltage is one diode drop below the base voltage:
$$ V_E = V_B - V_{BE} = 2.7V - 0.7V = 2.0V $$
The emitter current is found using Ohm's law on the emitter resistor:
$$ I_E = \frac{V_E}{R_E} = \frac{2.0V}{1k\Omega} = 2.0mA $$

**Exercise 18:** For the circuit in Exercises 16-17, if $R_C = 3.3k\Omega$, what is $V_{CE}$?
**Solution:**
First, assume $I_C \approx I_E = 2.0mA$.
The collector voltage is:
$$ V_C = V_{CC} - I_C R_C = 15V - (2.0mA \times 3.3k\Omega) = 15V - 6.6V = 8.4V $$
The collector-emitter voltage is:
$$ V_{CE} = V_C - V_E = 8.4V - 2.0V = 6.4V $$

**Exercise 19:** What is a DC load line? What two points are used to draw it?
**Solution:**
A DC load line is a line drawn on the transistor's characteristic curves ($I_C$ vs. $V_{CE}$) that represents all possible Q-points for a given amplifier circuit. The two endpoints of the load line are:
1.  **Saturation Point:** Where the transistor is fully on ($V_{CE} \approx 0$). The collector current is at its maximum, $I_{C(sat)} = V_{CC} / (R_C + R_E)$.
2.  **Cutoff Point:** Where the transistor is fully off ($I_C = 0$). The collector-emitter voltage is at its maximum, $V_{CE(cutoff)} = V_{CC}$.

**Exercise 20:** For a circuit with $V_{CC} = 20V$, $R_C = 2k\Omega$, and $R_E = 0.5k\Omega$, find the two endpoints of the DC load line.
**Solution:**
1.  **Saturation Point ($V_{CE} = 0$):**
    $$ I_{C(sat)} = \frac{V_{CC}}{R_C + R_E} = \frac{20V}{2k\Omega + 0.5k\Omega} = \frac{20V}{2.5k\Omega} = 8mA $$
2.  **Cutoff Point ($I_C = 0$):**
    $$ V_{CE(cutoff)} = V_{CC} = 20V $$
The endpoints are (0V, 8mA) and (20V, 0mA).

---

### BJT Amplifiers

**Exercise 21:** What is the purpose of coupling capacitors in a BJT amplifier circuit?
**Solution:**
Coupling capacitors are used at the input and output of an amplifier stage. Their purpose is to block DC current while allowing the AC signal to pass through. This prevents the DC bias of one stage from affecting the bias of the next stage, and it also prevents the DC voltage of the amplifier from affecting the source or load.

**Exercise 22:** What is the purpose of an emitter bypass capacitor?
**Solution:**
An emitter bypass capacitor is placed in parallel with the emitter resistor ($R_E$). For AC signals, the capacitor acts as a short circuit, effectively "bypassing" the emitter resistor. This significantly increases the amplifier's voltage gain, because without it, $R_E$ would introduce negative feedback that reduces the gain.

**Exercise 23:** What is the AC emitter resistance, $r'_e$? How is it calculated?
**Solution:**
The AC emitter resistance, $r'_e$, is the dynamic resistance of the base-emitter junction to AC signals. It is an internal property of the transistor, not a physical resistor. It is calculated based on the DC emitter current ($I_E$):
$$ r'_e = \frac{25mV}{I_E} $$
This value is crucial for calculating the voltage gain of an amplifier.

**Exercise 24:** An amplifier is biased such that its DC emitter current $I_E$ is 2.5mA. Calculate the AC emitter resistance $r'_e$.
**Solution:**
$$ r'_e = \frac{25mV}{I_E} = \frac{25mV}{2.5mA} = 10\Omega $$

**Exercise 25:** For a common-emitter amplifier, what is the formula for voltage gain ($A_v$) if the emitter resistor is fully bypassed?
**Solution:**
The voltage gain ($A_v$) is the ratio of the total AC collector resistance ($r_C$) to the AC emitter resistance ($r'_e$). The total AC collector resistance is the parallel combination of the collector resistor ($R_C$) and the load resistor ($R_L$).
$$ A_v = \frac{r_C}{r'_e} = \frac{R_C || R_L}{r'_e} $$

**Exercise 26:** A common-emitter amplifier has $R_C = 4k\Omega$, $R_L = 4k\Omega$, and is biased so that $r'_e = 20\Omega$. The emitter resistor is fully bypassed. Calculate the voltage gain.
**Solution:**
First, find the total AC collector resistance:
$$ r_C = R_C || R_L = \frac{4k\Omega \times 4k\Omega}{4k\Omega + 4k\Omega} = \frac{16}{8}k\Omega = 2k\Omega $$
Now, calculate the voltage gain:
$$ A_v = \frac{r_C}{r'_e} = \frac{2k\Omega}{20\Omega} = \frac{2000\Omega}{20\Omega} = 100 $$

**Exercise 27:** How does the voltage gain change if the emitter resistor is *not* bypassed?
**Solution:**
If the emitter resistor ($R_E$) is not bypassed, it is part of the AC circuit. The total AC resistance in the emitter circuit becomes $R_E + r'_e$. The voltage gain formula is modified to:
$$ A_v = \frac{r_C}{R_E + r'_e} $$
Since the denominator is now much larger, the voltage gain is significantly reduced. This is a form of negative feedback, which increases stability and input impedance at the cost of lower gain.

**Exercise 28:** For the amplifier in Exercise 26 ($r_C = 2k\Omega$, $r'_e = 20\Omega$), if an unbypassed emitter resistor of $R_E = 180\Omega$ is added, what is the new voltage gain?
**Solution:**
$$ A_v = \frac{r_C}{R_E + r'_e} = \frac{2k\Omega}{180\Omega + 20\Omega} = \frac{2000\Omega}{200\Omega} = 10 $$
The gain drops from 100 to 10.

**Exercise 29:** What is the input impedance of a common-emitter amplifier with voltage-divider bias and a bypassed emitter resistor?
**Solution:**
The input impedance of the stage ($Z_{in(stage)}$) is the parallel combination of the biasing resistors ($R_1$ and $R_2$) and the input impedance looking into the base of the transistor ($\beta r'_e$).
$$ Z_{in(stage)} = R_1 || R_2 || (\beta r'_e) $$

**Exercise 30:** A common-emitter amplifier has $R_1 = 10k\Omega$, $R_2 = 2.2k\Omega$, $\beta = 150$, and $r'_e = 15\Omega$. Calculate the input impedance of the stage.
**Solution:**
First, find the input impedance at the base:
$$ Z_{in(base)} = \beta r'_e = 150 \times 15\Omega = 2250\Omega = 2.25k\Omega $$
Next, find the parallel combination of the biasing resistors:
$$ R_{1,2} = R_1 || R_2 = \frac{10k\Omega \times 2.2k\Omega}{10k\Omega + 2.2k\Omega} \approx 1.8k\Omega $$
Finally, find the total input impedance:
$$ Z_{in(stage)} = R_{1,2} || Z_{in(base)} = \frac{1.8k\Omega \times 2.25k\Omega}{1.8k\Omega + 2.25k\Omega} \approx \frac{4.05}{4.05}k\Omega = 1k\Omega $$
