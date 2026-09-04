# Electronics: Practice Examination 01

**Course**: Electronics (Code: 105)  
**Duration**: 2 Hours  
**Evaluation**: Maximum 100 Points  
**Format**: Closed Book, Standard Scientific Calculator Allowed  

---

## Part A: Theoretical Concepts and Multiple Choice (25 Points)

### Question 1 (5 Points)
In an extrinsic n-type semiconductor at room temperature, which of the following statements is correct?
* A) Electrons are minority carriers and holes are majority carriers.
* B) Free electron concentration is approximately equal to donor impurity concentration ($n \approx N_D$).
* C) The Fermi level shifts downward toward the valence band.
* D) Conduction occurs solely via ion transport through the lattice.

### Question 2 (5 Points)
A linear DC network has a Thevenin equivalent resistance of $R_{\text{th}} = 50\,\Omega$. What load resistance $R_L$ connected to the network extracts maximum power?
* A) $R_L = 0\,\Omega$
* B) $R_L = 25\,\Omega$
* C) $R_L = 50\,\Omega$
* D) $R_L = \infty$

### Question 3 (5 Points)
What is the peak inverse voltage (PIV) rating required for each diode in a full-wave bridge rectifier circuit fed by secondary peak voltage $V_p$?
* A) $V_p / 2$
* B) $V_p$
* C) $2 V_p$
* D) $4 V_p$

### Question 4 (5 Points)
When a Bipolar Junction Transistor is biased into its saturation region:
* A) Both Base-Emitter and Base-Collector junctions are reverse-biased.
* B) The Base-Emitter junction is forward-biased and the Base-Collector junction is reverse-biased.
* C) Both Base-Emitter and Base-Collector junctions are forward-biased.
* D) The collector current is independent of base current and equals zero.

### Question 5 (5 Points)
In a common-emitter BJT amplifier with a completely bypassed emitter resistor ($C_E$ connected across $R_E$), what is the ideal small-signal voltage gain $A_v$?
* A) $A_v = +\frac{R_C}{R_E}$
* B) $A_v = -\frac{R_C \parallel R_L}{r_e}$
* C) $A_v = +1$
* D) $A_v = -\beta$

---

## Part B: DC Circuit Theorem Problem (25 Points)

In the two-source circuit below, find the current $I_L$ passing through load resistor $R_L = 10\,\Omega$ using **Thevenin's Theorem**:
* Voltage source $V_1 = 30\text{ V}$ in series with $R_1 = 15\,\Omega$.
* Parallel branch resistor $R_2 = 30\,\Omega$.
* Output branch series resistor $R_3 = 5\,\Omega$ leading to load terminal $A$.
* Return line connected to load terminal $B$.

---

## Part C: Diode Rectifier & Filter Problem (25 Points)

A full-wave bridge rectifier is supplied by a $230\text{ V} / 12\text{ V}_{\text{rms}}$ 50 Hz transformer. Each silicon diode exhibits a forward drop of $0.7\text{ V}$.
1. Determine the peak output voltage across the load resistor before filtering ($V_{p,\text{out}}$).
2. Calculate the filter capacitance $C$ required to keep the peak-to-peak ripple voltage $V_r \le 0.8\text{ V}$ when feeding a DC load current $I_{\text{dc}} = 200\text{ mA}$.
3. Calculate the DC output voltage $V_{\text{dc}}$ under this capacitive filtering regime.

---

## Part D: BJT Amplifier Biasing & AC Gain (25 Points)

An NPN BJT amplifier with $V_{CC} = 12\text{ V}$ uses voltage-divider biasing:
$R_1 = 33\text{ k}\Omega$, $R_2 = 10\text{ k}\Omega$, $R_C = 2.0\text{ k}\Omega$, $R_E = 1.0\text{ k}\Omega$.
The transistor has $\beta = 100$, $V_{BE} = 0.7\text{ V}$.
1. Verify whether the approximate $(\beta R_E \ge 10 R_2)$ condition holds.
2. Determine $V_B, V_E, I_{CQ}$, and $V_{CEQ}$.
3. Calculate dynamic emitter resistance $r_e$.
4. Calculate small-signal voltage gain $A_v$ assuming an external load $R_L = 10\text{ k}\Omega$ and bypassed $R_E$.

---

## Model Solutions & Marking Rubric

### Part A Solutions
1. **B**: In n-type semiconductors, donor impurities donate conduction band electrons, making $n \approx N_D$.
2. **C**: Maximum power transfer theorem mandates $R_L = R_{\text{th}} = 50\,\Omega$.
3. **B**: In a bridge rectifier, each reverse-biased diode experiences at most $V_p$ across its terminals.
4. **C**: Saturation occurs when both BEJ and BCJ are forward-biased.
5. **B**: $A_v = -\frac{R_C \parallel R_L}{r_e}$ with $180^\circ$ phase inversion.

### Part B Solution
1. **Open-Circuit Voltage $V_{\text{th}}$**:
   With $R_L$ disconnected, no current flows through $R_3$. The voltage across terminals $A-B$ equals the voltage across $R_2$:
   $$V_{\text{th}} = V_1 \cdot \frac{R_2}{R_1 + R_2} = 30\text{ V} \cdot \frac{30\,\Omega}{15\,\Omega + 30\,\Omega} = 30 \cdot \frac{30}{45} = 20\text{ V}$$
2. **Thevenin Resistance $R_{\text{th}}$**:
   Short-circuit $V_1$:
   $$R_{\text{th}} = R_3 + (R_1 \parallel R_2) = 5\,\Omega + \left( \frac{15 \cdot 30}{15 + 30} \right) = 5 + 10 = 15\,\Omega$$
3. **Load Current $I_L$**:
   $$I_L = \frac{V_{\text{th}}}{R_{\text{th}} + R_L} = \frac{20\text{ V}}{15\,\Omega + 10\,\Omega} = \frac{20}{25} = 0.8\text{ A} = 800\text{ mA}$$

### Part C Solution
1. Peak secondary voltage:
   $$V_{s,\text{peak}} = \sqrt{2} \cdot 12\text{ V} \approx 16.97\text{ V}$$
   Accounting for two forward conducting diodes in the bridge:
   $$V_{p,\text{out}} = V_{s,\text{peak}} - 2 V_D = 16.97 - 1.4 = 15.57\text{ V}$$
2. Filter capacitance ($f_{\text{rect}} = 2 \cdot 50 = 100\text{ Hz}$):
   $$C = \frac{I_{\text{dc}}}{f_{\text{rect}} \cdot V_r} = \frac{0.200\text{ A}}{100\text{ Hz} \cdot 0.8\text{ V}} = \frac{0.200}{80} = 2.5 \times 10^{-3}\text{ F} = 2500\,\mu\text{F}$$
3. Average DC filtered voltage:
   $$V_{\text{dc}} = V_{p,\text{out}} - \frac{V_r}{2} = 15.57\text{ V} - \frac{0.8\text{ V}}{2} = 15.17\text{ V}$$

### Part D Solution
1. Checking $\beta$-independent condition:
   $$\beta R_E = 100 \cdot 1.0\text{ k}\Omega = 100\text{ k}\Omega$$
   $$10 R_2 = 10 \cdot 10\text{ k}\Omega = 100\text{ k}\Omega$$
   Since $\beta R_E \ge 10 R_2$, the condition is satisfied.
2. DC Operating Point:
   $$V_B = V_{CC} \frac{R_2}{R_1 + R_2} = 12 \cdot \frac{10}{33 + 10} = 12 \cdot \frac{10}{43} \approx 2.79\text{ V}$$
   $$V_E = V_B - 0.7\text{ V} = 2.79 - 0.7 = 2.09\text{ V}$$
   $$I_{CQ} \approx I_E = \frac{V_E}{R_E} = \frac{2.09\text{ V}}{1.0\text{ k}\Omega} = 2.09\text{ mA}$$
   $$V_{CEQ} = V_{CC} - I_{CQ}(R_C + R_E) = 12 - 2.09\text{ mA} \cdot (2.0 + 1.0)\text{ k}\Omega = 12 - 6.27 = 5.73\text{ V}$$
3. Dynamic emitter resistance:
   $$r_e = \frac{26\text{ mV}}{I_{CQ}} = \frac{26\text{ mV}}{2.09\text{ mA}} \approx 12.44\,\Omega$$
4. Small-signal AC gain:
   $$R_L' = R_C \parallel R_L = \frac{2.0 \cdot 10}{2.0 + 10} = \frac{20}{12} \approx 1.667\text{ k}\Omega = 1667\,\Omega$$
   $$A_v = -\frac{R_L'}{r_e} = -\frac{1667\,\Omega}{12.44\,\Omega} \approx -134$$

