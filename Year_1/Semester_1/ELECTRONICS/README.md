# Electronics

## Course Overview
This course provides a rigorous introduction to basic electric circuit analysis, semiconductor physics, and fundamental analog electronic devices. Students develop theoretical and practical skills in analyzing linear resistive networks, PN-junction diodes, Zener regulators, and Bipolar Junction Transistor (BJT) amplifiers.

## Course Code
105 (ELECTRONICS)

## Prerequisites
None (Foundational course in circuit theory and solid-state devices)

---

## Topics Covered
* **DC Circuit Fundamentals**: Ohm's Law, Joule's Law, Kirchhoff's Current and Voltage Laws (KCL, KVL).
* **Systematic Network Analysis**: Nodal analysis, mesh-current analysis, superposition principle, Thevenin and Norton equivalent circuits, maximum power transfer theorem.
* **Semiconductor Physics**: Atomic structure, energy band theory, intrinsic and extrinsic semiconductors (n-type and p-type), drift and diffusion currents.
* **PN Junction Diodes**: Depletion region physics, forward and reverse bias characteristics, Shockley diode equation, piecewise linear model, Zener breakdown.
* **Diode Applications**: Half-wave and full-wave bridge rectifiers, capacitive filtering, peak inverse voltage (PIV), clipping circuits, clamping circuits, and voltage regulation.
* **Bipolar Junction Transistors (BJT)**: Physical structure (NPN, PNP), modes of operation (cutoff, active, saturation), current gain parameters ($\alpha$ and $\beta$), DC load line analysis.
* **Transistor Biasing and Amplification**: Fixed-bias, emitter-stabilized bias, voltage-divider bias networks, small-signal AC modeling, common-emitter (CE) voltage amplifier configurations.

---

## Learning Objectives
* Analyze complex linear DC electrical networks using systematic nodal and mesh methods.
* Determine equivalent Thevenin and Norton circuits for two-terminal networks.
* Understand carrier transport mechanics in semiconductor junctions and diode operating regimes.
* Design DC power supply conversion stages including rectification, filtering, and regulation.
* Bias BJT transistors into stable Q-points and calculate small-signal amplifier gain.
* Model and verify analog circuits using SPICE computer-aided simulation tools.

---

## Directory Structure

| Directory | Description |
|:---|:---|
| [`Lectures/`](Lectures/) | Structured theory lecture modules and official professor slide presentations |
| [`Exercises/`](Exercises/) | Practice drills, problem sets on circuit theorems, diodes, and BJTs |
| [`Examples/`](Examples/) | Comprehensive sets of 60 solved circuit and transistor analysis problems |
| [`Assignments/`](Assignments/) | Practical coursework assignments with technical specifications and rubrics |
| [`Tutorials/`](Tutorials/) | Simulation guides for SPICE netlists and schematic capture |
| [`Projects/`](Projects/) | Capstone design project (Regulated DC Power Supply) |
| [`Exams/`](Exams/) | Archival exam papers, problem scans, and practice mock tests |
| [`Resources/`](Resources/) | Granular chapter notes, reference textbooks, and curriculum mindmaps |

---

## Laboratory & Simulation Tools
Circuit designs are evaluated using SPICE simulation suites such as NGSPICE, LTspice, or web-based Falstad simulators. For detailed instructions on SPICE netlist syntax and operating point analysis, consult [`Tutorials/tutorial_01_circuit_simulation_with_spice.md`](Tutorials/tutorial_01_circuit_simulation_with_spice.md).
