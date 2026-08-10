# Electronics - Mind Map

## 1. Introduction - Ohm's Law (Lecture 01)

### 1.1 Atomic Structure & Material Properties
- 1.1.1 Constituents of an atom: protons, neutrons, electrons
- 1.1.2 Electric charge and conductivity

### 1.2 Conductors, Semiconductors, Insulators
- 1.2.1 Properties of conductors (metals)
- 1.2.2 Properties of insulators
- 1.2.3 Intermediate behavior of semiconductors

### 1.3 Electrical Conductivity of Metals
- 1.3.1 Drude Model (1900)
- 1.3.2 Free electron cloud
- 1.3.3 Current carriers and collisions
- 1.3.4 Energy approach
  - 1.3.4.1 Conduction band and valence band
  - 1.3.4.2 Energy gap
  - 1.3.4.3 Fermi level

### 1.4 Potential - Potential Difference - Voltage
- 1.4.1 Principle of minimum energy
- 1.4.2 Definition of potential V = E/q
- 1.4.3 Voltage as potential difference ΔV

### 1.5 Electric Circuit & Conventional Current Direction
- 1.5.1 Conditions for current flow
- 1.5.2 Resistance (R) and conductance (g)
- 1.5.3 Conventional current vs actual electron movement
- 1.5.4 Ground, reference potential, common conductor

### 1.6 Ohm's Law
- 1.6.1 V = I*R, I = V/R, R = V/I
- 1.6.2 Electrical triangle
- 1.6.3 I-V characteristic curve
- 1.6.4 Conductance g = 1/R

### 1.7 Resistor Connections
- 1.7.1 Series: R_total = R1 + R2 + ...
- 1.7.2 Parallel: 1/R_total = 1/R1 + 1/R2 + ...
- 1.7.3 Mixed connections

### 1.8 Capacitors
- 1.8.1 Capacitance C = Q/V
- 1.8.2 Capacitor energy (electric field)
- 1.8.3 Time constant τ = R*C
- 1.8.4 Dielectric and dielectric strength
- 1.8.5 Series and parallel connections

### 1.9 Inductors
- 1.9.1 Self-induction phenomenon (Lenz's rule)
- 1.9.2 Mutual induction
- 1.9.3 Inductor energy (magnetic field)
- 1.9.4 Series and parallel connections

### 1.10 Analog and Digital Signal

### 1.11 Direct and Alternating Current
- 1.11.1 DC: constant polarity
- 1.11.2 AC: polarity alternation

### 1.12 Voltage Sources
- 1.12.1 Real sources: internal resistance r
- 1.12.2 Ideal source: r << RL
- 1.12.3 Maximum current Imax

### 1.13 Current Sources
- 1.13.1 Ideal source condition: r >> RL
- 1.13.2 Minimum voltage Vmin

### 1.14 Source Connections
- 1.14.1 Series connection of voltage sources
- 1.14.2 Parallel connection of identical voltage sources
- 1.14.3 Current source connections

---

## 2. Circuit Analysis Methods (Lecture 02)

### 2.1 Basic Circuit Elements
- 2.1.1 Energy sources
- 2.1.2 Conductors, insulators, semiconductors
- 2.1.3 Switches, potentiometers
- 2.1.4 Relays, fuses
- 2.1.5 Component symbols and schematic diagrams

### 2.2 Independent and Dependent Sources
- 2.2.1 Ideal independent voltage source
- 2.2.2 Ideal independent current source
- 2.2.3 Dependent (controlled) sources

### 2.3 Power, Energy, Cost
- 2.3.1 Power: P = V * I
- 2.3.2 Energy: W = P * t
- 2.3.3 Energy cost

### 2.4 Measuring Instruments
- 2.4.1 By operating principle (moving coil, moving iron, electrodynamic, electrostatic, thermal, induction)
- 2.4.2 By measured quantity (voltmeter, ammeter, wattmeter, frequency meter)
- 2.4.3 By display method (indicating, recording, integrating)
- 2.4.4 Ammeter: series, low internal resistance
- 2.4.5 Voltmeter: parallel, high internal resistance
- 2.4.6 Panel instruments and multimeters
- 2.4.7 Resistance measurement (ohmmeter)
- 2.4.8 Voltage measurement
- 2.4.9 Current measurement

### 2.5 Circuit Analysis Methods
- 2.5.1 Ohm's law and connections
- 2.5.2 Kirchhoff's rules
- 2.5.3 Mesh Analysis Method (M.A.M.)
- 2.5.4 Nodal Analysis Method (M.N.)
- 2.5.5 Maximum Power Transfer Theorem
- 2.5.6 Thevenin and Norton Theorems

### 2.6 Kirchhoff's Rules
- 2.6.1 Definitions: branch, node, loop
- 2.6.2 Reference direction and polarity
- 2.6.3 1st Rule (currents): ΣI = 0
- 2.6.4 2nd Rule (voltages): ΣV = 0

### 2.7 Mesh Analysis Method (M.A.M.)
- 2.7.1 Number of independent loops: b - n + 1
- 2.7.2 Matrix form: R11*I1 + R12*I2 = ΣV1
- 2.7.3 Suitable for circuits with many voltage sources

### 2.8 Nodal Analysis Method (M.N.)
- 2.8.1 Number of equations: n - 1
- 2.8.2 Matrix form: G11*V1 + G12*V2 = ΣI1
- 2.8.3 Suitable for circuits with many current sources

### 2.9 Maximum Power Transfer Theorem
- 2.9.1 Condition: R_load = R_internal

### 2.10 Thevenin Theorem
- 2.10.1 Equivalent circuit: VTh in series with RTh
- 2.10.2 VTh: open-circuit voltage
- 2.10.3 RTh: short-circuit voltage sources, open-circuit current sources

### 2.11 Norton Theorem
- 2.11.1 Equivalent circuit: IN parallel with RN
- 2.11.2 IN: short-circuit current
- 2.11.3 RN = RTh

### 2.12 Thevenin-Norton Duality
- 2.12.1 Network equivalence
- 2.12.2 Source conversion

### 2.13 Additional Circuits
- 2.13.1 Voltage divider
- 2.13.2 Current divider
- 2.13.3 Variable resistors (rheostat, potentiometer)
- 2.13.4 Voltage source to current source conversion
- 2.13.5 Current source to voltage source conversion
- 2.13.6 Resistor in parallel with voltage source (omitted)
- 2.13.7 Resistor in series with current source (omitted)

---

## 3. Semiconductors - PN Junction (Lecture 03)

### 3.1 Conductors, Insulators, Semiconductors
- 3.1.1 Classification by electrical properties
- 3.1.2 Resistivity values

### 3.2 Causes of Semiconductor Behavior Change
- 3.2.1 Resistivity
- 3.2.2 Temperature

### 3.3 Semiconductor Structure
- 3.3.1 Silicon (Si) and Germanium (Ge)
- 3.3.2 Four valence electrons, covalent bonds
- 3.3.3 Crystal lattice

### 3.4 Semiconductors as Insulators
- 3.4.1 At T = 0K: no free electrons

### 3.5 Semiconductors as Conductors
- 3.5.1 At room temperature: free electrons
- 3.5.2 Hole and electron movement
  - 3.5.2.1 Hole: positive carrier (vacant position)
  - 3.5.2.2 Opposite direction of movement

### 3.6 Energy Bands
- 3.6.1 Valence band and conduction band
- 3.6.2 Energy gap
- 3.6.3 Insulator: large gap
- 3.6.4 Semiconductor: small gap
- 3.6.5 Conductor: zero gap (overlap)

### 3.7 Intrinsic and Extrinsic Semiconductors
- 3.7.1 Intrinsic: pure, n = p = ni
- 3.7.2 Extrinsic: doped with impurities
- 3.7.3 Carrier concentration

### 3.8 Intrinsic (Pure) Semiconductors
- 3.8.1 Uniform structure
- 3.8.2 Exclusively Ge or Si
- 3.8.3 Two types of carriers: holes and electrons

### 3.9 Extrinsic Semiconductors
- 3.9.1 Addition of pentavalent or trivalent atoms
- 3.9.2 Donors and acceptors (impurities)
- 3.9.3 n-type and p-type

### 3.10 n-type Semiconductors
- 3.10.1 Doping with 5 valence electrons (donors) - e.g. Phosphorus
- 3.10.2 Majority carriers: electrons
- 3.10.3 Minority carriers: holes

### 3.11 p-type Semiconductors
- 3.11.1 Doping with 3 valence electrons (acceptors) - e.g. Boron
- 3.11.2 Majority carriers: holes
- 3.11.3 Minority carriers: electrons

### 3.12 Other Semiconductors
- 3.12.1 Organic semiconductors
- 3.12.2 Amorphous semiconductors (photovoltaic)

### 3.13 PN Junction
- 3.13.1 Diffusion phenomenon
  - 3.13.1.1 Electron diffusion from n to p
  - 3.13.1.2 Hole diffusion from p to n
- 3.13.2 Diffusion region
- 3.13.3 Space charge formation
- 3.13.4 Equilibrium

### 3.14 Energy Approach of PN Junction
- 3.14.1 Fermi level in p-type (near valence band)
- 3.14.2 Fermi level in n-type (near conduction band)
- 3.14.3 Energy barrier formation E0
- 3.14.4 Fermi level equalization at equilibrium

### 3.15 Depletion Region
- 3.15.1 Carrier recombination
- 3.15.2 Carrier depletion
- 3.15.3 Width increase toward equilibrium

### 3.16 Electrical Characteristics of PN Junction
- 3.16.1 Space charge distribution
- 3.16.2 Junction potential V0
- 3.16.3 Junction capacitance C0

### 3.17 Reverse Bias
- 3.17.1 Positive to n, negative to p
- 3.17.2 Depletion region widening
- 3.17.3 Insulator behavior (open circuit)
- 3.17.4 Negligible current (thermal excitation)

### 3.18 Forward Bias
- 3.18.1 Positive to p, negative to n
- 3.18.2 Depletion region narrowing
- 3.18.3 Potential barrier removal
- 3.18.4 Current flow

---

## 4. Diode (Lecture 04)

### 4.1 Crystal Diode
- 4.1.1 PN junction implementation
- 4.1.2 Unidirectional current flow
- 4.1.3 Asymmetric two-terminal arrangement
- 4.1.4 Anode (p) and Cathode (n)
- 4.1.5 Solid-state diode vs vacuum tube

### 4.2 Electrical Characteristics
- 4.2.1 No bias: depletion region, 0.6-0.7V barrier (Si)
- 4.2.2 Forward bias: narrows, low resistance (50-100Ω)
- 4.2.3 Reverse bias: widens, high resistance (>10kΩ)
- 4.2.4 Threshold voltage VT (0.7V Si, 0.2V Ge)
- 4.2.5 Diode as switch (closed/open)

### 4.3 Theoretical Model
- 4.3.1 Non-linear element
- 4.3.2 Forward/reverse resistance ratio >1000:1
- 4.3.3 Breakdown voltage Vbr
- 4.3.4 Breakdown region (destructive for common diodes)

### 4.4 Characteristic Equation
- 4.4.1 Shockley equation: ID = Is * exp(VD / (ηVT))
- 4.4.2 Thermal voltage VT

### 4.5 Load Line and Operating Point
- 4.5.1 DC analysis: Q point
- 4.5.2 Load line: VDD = ID*R + VD
- 4.5.3 Static (DC) resistance
- 4.5.4 Dynamic (AC) resistance
- 4.5.5 Small-signal analysis

### 4.6 Operating Models
- 4.6.1 Ideal diode (1st approximation)
- 4.6.2 Typical diode (2nd approximation)
- 4.6.3 Real diode (3rd approximation)

### 4.7 Practical
- 4.7.1 Ohmmeter testing
- 4.7.2 Manufacturer datasheets (1N4001)
- 4.7.3 Calculation example

---

## 5. Special Diode Types (Lecture 05)

### 5.1 Zener Diode
- 5.1.1 Breakdown region operation
- 5.1.2 Breakdown voltages 2V-200V
- 5.1.3 I-V characteristic
- 5.1.4 Forward bias: like a standard diode
- 5.1.5 Reverse: constant voltage VZ
- 5.1.6 Key parameters
- 5.1.7 Voltage regulator
  - 5.1.7.1 Line (constant IL)
  - 5.1.7.2 Load (constant VI)
- 5.1.8 Percentage regulation
- 5.1.9 Practical analysis with Thevenin

### 5.2 Schottky Diode
- 5.2.1 Metal-N semiconductor junction
- 5.2.2 Majority carrier device (speed)

### 5.3 Optoelectronic Devices
- 5.3.1 Optoelectronics: optics + electronics
- 5.3.2 Based on PN junction

### 5.4 LED (Light Emitting Diode)
- 5.4.1 Light emission in forward bias
- 5.4.2 Colors and infrared
- 5.4.3 Current 10-20mA, voltage 1.5-2.5V
- 5.4.4 Protection resistor
- 5.4.5 Applications
- 5.4.6 Advantages and disadvantages

### 5.5 Laser Diode
- 5.5.1 Cavity with polished surfaces

### 5.6 Photodiode
- 5.6.1 Reverse bias + illumination = current Iλ

### 5.7 Phototransistor

### 5.8 Optocouplers (Optoisolators)
- 5.8.1 Complete electrical isolation

---

## 6. Diode Applications - Power Supplies (Lecture 06)

### 6.1 Power Supplies
- 6.1.1 Rectifier (AC to DC)
- 6.1.2 Smoothing filter (ripple reduction)
- 6.1.3 Voltage regulator

### 6.2 Conversion Stages
- 6.2.1 Step-down transformer
- 6.2.2 Rectification (half-wave or full-wave)
- 6.2.3 Smoothing
- 6.2.4 Regulation

### 6.3 Half-Wave Rectification
- 6.3.1 Blocking of negative half-cycles
- 6.3.2 Average value: Vdc = 0.318 * Vout(max)
- 6.3.3 Peak Inverse Voltage (PIV)

### 6.4 Full-Wave Rectification with 2 Diodes
- 6.4.1 Center-tapped transformer
- 6.4.2 Output frequency: fout = 2 * fin
- 6.4.3 PIV = 2*Vout(max) + 0.7V

### 6.5 Bridge Rectification
- 6.5.1 Four diodes
- 6.5.2 PIV = Vout(max) + 0.7V
- 6.5.3 Bridge packages

### 6.6 Comparison
- 6.6.1 Double DC voltage
- 6.6.2 Lower ripple factor
- 6.6.3 Double power factor

### 6.7 Three-Phase Rectification
- 6.7.1 Half-wave: Vdc = 0.831 * Vmax
- 6.7.2 Full-wave rectification

### 6.8 Smoothing Filters
- 6.8.1 Capacitor smoothing
- 6.8.2 Inductor smoothing
- 6.8.3 Stabilization factor γ

### 6.9 Zener Regulator
- 6.9.1 Line
- 6.9.2 Load

### 6.10 Voltage Multipliers
- 6.10.1 Half-wave doubler
- 6.10.2 Full-wave doubler
- 6.10.3 Tripler
- 6.10.4 Quadrupler

### 6.11 Fault Detection

---

## 7. Bipolar Junction Transistor (Lecture 07)

### 7.1 Introduction
- 7.1.1 Transistor: solid-state semiconductor device
- 7.1.2 Applications: amplification, regulation, modulation, switching

### 7.2 Historical Overview
- 7.2.1 Lilienfeld (1928)
- 7.2.2 Heil (1934)
- 7.2.3 Bardeen, Brattain, Shockley (Bell Labs, 1948)
- 7.2.4 Nobel Prize in Physics 1956
- 7.2.5 First silicon transistor (Texas Instruments, 1954)
- 7.2.6 First MOSFET (Kahng & Atalla, Bell Labs, 1960)

### 7.3 Bipolar Junction Transistor (BJT)
- 7.3.1 Types: NPN and PNP
- 7.3.2 Terminals: Emitter (E), Base (B), Collector (C)
- 7.3.3 Structure: two back-to-back diodes
- 7.3.4 Terminal identification

### 7.4 Operating Principle
- 7.4.1 Biasing: BE forward, BC reverse
- 7.4.2 Small base current controls large collector current
- 7.4.3 IE = IB + IC
- 7.4.4 Thin and lightly doped base

### 7.5 Biasing Configurations
- 7.5.1 Common Base
- 7.5.2 Common Emitter
- 7.5.3 Common Collector

### 7.6 Characteristic Curves
- 7.6.1 Input (Base) characteristics
- 7.6.2 Output (Collector) characteristics
- 7.6.3 Curve family

### 7.7 Operating Regions
- 7.7.1 Cutoff
- 7.7.2 Saturation
- 7.7.3 Active region
- 7.7.4 Breakdown

### 7.8 Parameters
- 7.8.1 βDC = IC/IB, αDC = IC/IE
- 7.8.2 Relationships: α = β/(β+1), β = α/(1-α)
- 7.8.3 IC = β*IB, IE = (β+1)*IB
- 7.8.4 Early effect, VA voltage

### 7.9 Applications
- 7.9.1 Switch (cutoff/saturation)
- 7.9.2 Amplifier

---

## 8. Transistor Biasing (Lecture 08)

### 8.1 Load Line
- 8.1.1 Operating point Q(VCE, IC)
- 8.1.2 Load line intersection with characteristic curve
- 8.1.3 Methodology for finding Q
- 8.1.4 Methodology for drawing load line

### 8.2 DC Analysis
- 8.2.1 Calculation of DC currents and voltages
- 8.2.2 Q-point identification
- 8.2.3 Load line drawing

### 8.3 Biasing Circuits

#### 8.3.1 Base Biasing
- 8.3.1.1 Fixed base current
- 8.3.1.2 Q-point methodology
- 8.3.1.3 Load line

#### 8.3.2 Emitter Biasing
- 8.3.2.1 Q-point stabilization
- 8.3.2.2 Emitter resistor

#### 8.3.3 Voltage Divider Biasing
- 8.3.3.1 Widely used
- 8.3.3.2 VB calculation from divider
- 8.3.3.3 Maintains stable Q

#### 8.3.4 Dual-Supply Emitter Biasing
- 8.3.4.1 Stable Q independent of β
- 8.3.4.2 IB negligible

#### 8.3.5 Emitter Feedback Biasing
- 8.3.5.1 Historical significance

#### 8.3.6 Collector and Emitter Feedback Biasing
- 8.3.6.1 Historical significance
- 8.3.6.2 Input loop from collector

---

## 9. Transistor Amplifiers (Lecture 09)

### 9.1 Introduction
- 9.1.1 Small-signal amplifiers
- 9.1.2 Active region operation

### 9.2 Amplifier Implementation
- 9.2.1 Input coupling capacitor
- 9.2.2 Load resistor RL at output
- 9.2.3 Input resistance Rg
- 9.2.4 Bypass capacitor

### 9.3 Amplifier Variants
- 9.3.1 Base biasing based
- 9.3.2 Emitter biasing based
- 9.3.3 Voltage divider based
- 9.3.4 Dual-supply based
- 9.3.5 With emitter feedback
- 9.3.6 With collector and emitter feedback

### 9.4 Amplifier Parameters
- 9.4.1 Notation (DC: capitals, AC: lowercase)
- 9.4.2 DC and AC superposition
- 9.4.3 Transconductance gm = IC/VT
- 9.4.4 Input resistance rπ' = β/gm
- 9.4.5 Emitter resistance re' = VT/IE

### 9.5 DC Analysis of Amplifiers
- 9.5.1 Emitter current IE calculation
- 9.5.2 Capacitors = open switches

### 9.6 AC Analysis
- 9.6.1 T model (common base)
- 9.6.2 Pi model (common emitter)
- 9.6.3 Complex input resistances
- 9.6.4 Voltage gain Av = rc / (re' + RE)
- 9.6.5 Bypass capacitor effect
- 9.6.6 Voltage divider with Rg

### 9.7 Generalized Methodology
- 9.7.1 DC Analysis: finding IE
- 9.7.2 Calculating re' = 25mV/IE
- 9.7.3 AC Analysis with Pi model
- 9.7.4 Calculating Av and Vout

---

## 10. Course Summary (Lecture 10)
Overview of all topics with key diagrams and formulas.
