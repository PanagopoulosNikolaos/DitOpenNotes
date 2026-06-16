# 01_Eisagwgh-Nomos_Ohm Documentation

This lecture introduces the fundamental concepts of electronics: atomic structure, electrical conductivity, Ohm's law, circuit elements (resistors, capacitors, inductors), signal types, and voltage/current sources. It establishes the theoretical foundation required for all subsequent circuit analysis.

---

## 1. Core Definitions

### 1.1 Atomic Structure and Electrical Charge

Matter consists of molecules, which subdivide into atoms. Atoms contain protons (positive charge), neutrons (neutral), and electrons (negative charge). The electron is the primary charge carrier in electrical circuits.

### 1.2 Electrical Conductivity and Current

Electrical conductivity is the ability of a material to support directed movement of charged particles. This directed flow is called electric current $I$, defined as the rate of charge flow:

$$
I = \frac{d|Q|}{dt}
$$

| Symbol | Quantity | Unit |
|:-------|:---------|:-----|
| $I$ | Current | A (Ampere) |
| $Q$ | Charge | Cb (Coulomb) |
| $t$ | Time | s (second) |

### 1.3 Conductors, Semiconductors, Insulators

| Material Type | Conductivity | Example |
|:--------------|:-------------|:--------|
| Conductor | Allows current flow | Metals (Cu, Al, Ag) |
| Insulator | Blocks current | Plastics, rubber |
| Semiconductor | Intermediate behavior | Silicon (Si), Germanium (Ge) |

### 1.4 Drude Model (1900)

Proposed by P. Drude: in metals, valence electrons form a cloud of free electrons that move between positively charged ion cores. Under an electric field, these free electrons move directionally, constituting current. Collisions with the lattice cause electrical resistance and heat dissipation.

### 1.5 Energy Band Approach

In isolated atoms, electrons occupy discrete energy levels (orbits). In crystalline solids, these levels broaden into energy bands separated by band gaps.

| Band | Description |
|:-----|:------------|
| Valence band | Energy levels of valence electrons |
| Conduction band | Energy levels where electrons are free to conduct |
| Band gap | Forbidden energy region between bands |

**Fermi level:** The maximum energy an electron can have at absolute zero ($0\,K$).

**Material classification by energy bands:**

- **Conductors:** No band gap (valence and conduction bands overlap).
- **Insulators:** Large band gap -- electrons cannot jump to conduction band.
- **Semiconductors:** Small band gap -- electrons can jump with small energy (e.g., thermal).

---

## 2. Foundational Formulas

### 2.1 Electric Potential and Voltage

**Potential** is energy per unit charge:

$$
V = \frac{E}{q}
$$

Unit: $1\,\text{Volt} = 1\,\text{Joule} / 1\,\text{Coulomb}$

**Voltage (potential difference):**

$$
\Delta V = V_1 - V_2
$$

According to the principle of minimum energy, charge flows from higher to lower potential (for positive charges). Negative charges (electrons) flow from lower to higher potential.

### 2.2 Ohm's Law

For a resistor $R$ with voltage $V$ applied across it:

$$
I = \frac{V}{R} \quad \text{or} \quad V = I \cdot R \quad \text{or} \quad R = \frac{V}{I}
$$

| Symbol | Quantity | Unit |
|:-------|:---------|:-----|
| $V$ | Voltage | V (Volt) |
| $I$ | Current | A (Ampere) |
| $R$ | Resistance | $\Omega$ (Ohm) |

**Conductance:**

$$
g = \frac{1}{R} = \frac{I}{V}
$$

Unit: Siemens (S) or mho ($\mho$).

### 2.3 I-V Characteristic Curve

For an ohmic resistor, the I-V characteristic is a straight line through the origin with slope equal to $1/R$.

### 2.4 Resistor Combinations

**Series:**

$$
R_{total} = R_1 + R_2 + R_3 + \dots
$$

**Parallel:**

$$
\frac{1}{R_{total}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + \dots
$$

### 2.5 Capacitance

Capacitance $C$ of a capacitor is the ratio of charge $Q$ to voltage $V$:

$$
C = \frac{Q}{V}
$$

Unit: F (Farad). Typical circuit values: $\mu\text{F}$ or $\text{nF}$.

**Time constant:**

$$
\tau = R \cdot C \quad (\text{seconds})
$$

A capacitor is considered fully charged after $5\tau$.

**Energy stored in a capacitor (electric field):**

$$
E = \frac{1}{2} C V^2
$$

**Capacitors in series:**

$$
\frac{1}{C_{total}} = \frac{1}{C_1} + \frac{1}{C_2} + \dots
$$

**Capacitors in parallel:**

$$
C_{total} = C_1 + C_2 + \dots
$$

### 2.6 Inductance

**Self-induction (Lenz's law):** When current through an inductor changes, an induced voltage appears across it with polarity opposing the change.

**Mutual induction:** An induced voltage appears in a secondary coil when current changes in a primary coil, and vice versa.

**Energy stored in an inductor (magnetic field):**

$$
E = \frac{1}{2} L I^2
$$

**Inductors in series:**

$$
L_{total} = L_1 + L_2 + \dots
$$

**Inductors in parallel:**

$$
\frac{1}{L_{total}} = \frac{1}{L_1} + \frac{1}{L_2} + \dots
$$

---

## 3. Key Parameters and Constraints

| Component | Parameter | Unit | Notes |
|:----------|:----------|:-----|:------|
| Resistor | $R$ | $\Omega$ | $k\Omega$ common in circuits |
| Capacitor | $C$ | F | $\mu\text{F}$, $\text{nF}$, $\text{pF}$ common |
| Inductor | $L$ | H | Henry |
| Time constant | $\tau = RC$ | s | Full charge at $5\tau$ |
| Dielectric strength | -- | V/m | Maximum field before breakdown |

---

## 4. Step-by-Step Mechanisms

### 4.1 Conventional Current vs Electron Flow

1. Electrons (negative charge carriers) move from the negative to the positive terminal of a source.
2. By historical convention, current direction is defined as opposite to electron flow (positive to negative).
3. This conventional direction corresponds to the flow of hypothetical positive charge carriers.

### 4.2 Ground and Reference Potential

1. A reference point (ground) is assigned $0\,\text{V}$ potential.
2. All voltages in the circuit are measured relative to this reference.
3. In single-supply circuits, the negative terminal of the source is typically chosen as ground.
4. The common terminal of voltmeters (COM) connects to this ground point.

---

## 5. Signal Types and Sources

### 5.1 Analog and Digital Signals

| Signal Type | Characteristics |
|:------------|:----------------|
| Analog | Continuous in time and amplitude; all natural sources produce analog signals |
| Digital | Discrete amplitude; binary signals take only two values |

### 5.2 DC and AC Signals

| Signal | Definition | Characteristics |
|:-------|:-----------|:----------------|
| DC (Direct Current) | Maintains constant sign over time | May be constant or varying, but polarity never changes |
| AC (Alternating Current) | Alternates polarity over time | Periodically reverses direction |

> **[Key Insight]** A constant voltage is always DC, but not all DC is constant. Varying waveforms that maintain a single polarity are still considered DC.

### 5.3 Voltage Sources

**Ideal voltage source:** Maintains constant voltage regardless of load current ($r \to 0$).

**Real voltage source:** Has internal resistance $r$. Condition for proper operation: $r \ll R_L$.

**Maximum current $I_{max}$:** The highest current the source can deliver while maintaining its specified voltage.

### 5.4 Current Sources

**Ideal current source:** Delivers constant current regardless of load voltage ($r \to \infty$).

**Real current source:** Condition: $r \gg R_L$.

**Minimum voltage $V_{min}$:** The lowest voltage at which the source operates correctly.

### 5.5 Source Connections

**Voltage sources in series:** Total voltage is the sum of individual voltages. The maximum current is limited by the lowest $I_{max}$.

**Voltage sources in parallel (identical only):** Total voltage equals the common voltage; maximum current equals the sum of individual $I_{max}$ values.

**Current sources in parallel:** Total current is the sum of individual currents.

---

## 6. Solved Exercises

### Exercise 1: Ohm's Law -- Direct Calculation

**Problem:** A $10\,k\Omega$ resistor has $12\,\text{V}$ applied across it. Find the current.

**Solution:**

Using Ohm's law $I = V/R$:

$$
I = \frac{12\,\text{V}}{10 \times 10^3\,\Omega} = 1.2 \times 10^{-3}\,\text{A} = 1.2\,\text{mA}
$$

---

### Exercise 2: Ohm's Law -- Finding Resistance

**Problem:** A current of $5\,\text{mA}$ flows through a resistor when $15\,\text{V}$ is applied. Find the resistance.

**Solution:**

$$
R = \frac{V}{I} = \frac{15\,\text{V}}{5 \times 10^{-3}\,\text{A}} = 3000\,\Omega = 3\,k\Omega
$$

---

### Exercise 3: Resistors in Series

**Problem:** Three resistors $R_1 = 1\,k\Omega$, $R_2 = 2.2\,k\Omega$, $R_3 = 3.3\,k\Omega$ are connected in series. Find the total resistance.

**Solution:**

$$
R_{total} = R_1 + R_2 + R_3 = 1 + 2.2 + 3.3 = 6.5\,k\Omega
$$

---

### Exercise 4: Resistors in Parallel

**Problem:** Two resistors $R_1 = 2\,k\Omega$ and $R_2 = 3\,k\Omega$ are connected in parallel. Find the total resistance.

**Solution:**

$$
\frac{1}{R_{total}} = \frac{1}{R_1} + \frac{1}{R_2} = \frac{1}{2} + \frac{1}{3} = \frac{3+2}{6} = \frac{5}{6}
$$

$$
R_{total} = \frac{6}{5} = 1.2\,k\Omega
$$

---

### Exercise 5: Mixed Resistor Network

**Problem:** $R_1 = 1\,k\Omega$ is in series with a parallel combination of $R_2 = 2\,k\Omega$ and $R_3 = 2\,k\Omega$. Find the total resistance.

**Solution:**

Step 1: Calculate the parallel combination:

$$
\frac{1}{R_{23}} = \frac{1}{2} + \frac{1}{2} = 1 \quad \Rightarrow \quad R_{23} = 1\,k\Omega
$$

Step 2: Add the series resistor:

$$
R_{total} = R_1 + R_{23} = 1 + 1 = 2\,k\Omega
$$

---

### Exercise 6: Capacitor Charge Calculation

**Problem:** A $10\,\mu\text{F}$ capacitor is connected to a $12\,\text{V}$ source. Find the stored charge and energy.

**Solution:**

Charge:

$$
Q = C \cdot V = 10 \times 10^{-6} \times 12 = 120 \times 10^{-6} = 120\,\mu\text{C}
$$

Energy:

$$
E = \frac{1}{2} C V^2 = \frac{1}{2} \times 10 \times 10^{-6} \times 12^2 = \frac{1}{2} \times 10 \times 10^{-6} \times 144 = 720 \times 10^{-6} = 720\,\mu\text{J}
$$

---

### Exercise 7: RC Time Constant

**Problem:** A $1\,k\Omega$ resistor and a $100\,\mu\text{F}$ capacitor form an RC circuit. Find the time constant and the time required for full charge.

**Solution:**

Time constant:

$$
\tau = R \cdot C = 1000 \times 100 \times 10^{-6} = 0.1\,\text{s}
$$

Full charge time ($5\tau$):

$$
t_{full} = 5 \times 0.1 = 0.5\,\text{s}
$$

---

### Exercise 8: Voltage Source with Internal Resistance

**Problem:** A $12\,\text{V}$ battery has an internal resistance of $0.5\,\Omega$. It is connected to a $10\,\Omega$ load. Find the actual voltage across the load.

**Solution:**

Using the voltage divider principle:

$$
V_{load} = V \cdot \frac{R_L}{r + R_L} = 12 \times \frac{10}{0.5 + 10} = 12 \times \frac{10}{10.5} = 12 \times 0.9524 = 11.43\,\text{V}
$$

The internal resistance causes a $0.57\,\text{V}$ drop.

---

## Exam Tip: Recognizing DC vs Constant Signals

In exam problems, pay careful attention to whether a source is ideal ($r=0$) or has an internal resistance. When a problem states "ideal voltage source," treat the internal resistance as zero. When a real battery is specified, always account for the voltage drop across its internal resistance. A common mistake is to treat real sources as ideal.

Electronics typically uses $k\Omega$ for resistors and $\mu\text{F}$ or $\text{nF}$ for capacitors -- ensure your unit conversions are correct.