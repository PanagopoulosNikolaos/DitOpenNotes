# Fundamentals of Electromagnetics

## Course Overview
This course provides a comprehensive mathematical and physical foundation in classical electrodynamics, covering vector calculus, static electric and magnetic fields, boundary value problems, Maxwell's postulates, time-harmonic plane wave propagation, energy conservation via the Poynting vector, and high-frequency transmission line theory.

## Course Code
201 (Fundamentals of Electromagnetics & Telecommunications)

## Prerequisites
* Mathematical Analysis (Code: 101)
* Linear Algebra (Code: 102)

---

## Topics Covered
* **Vector Calculus and Curvilinear Systems**: Gradient, divergence, curl, Laplacian, divergence theorem, Stokes' theorem, and orthogonal coordinates (Cartesian, cylindrical, spherical).
* **Electrostatics and Dielectric Media**: Coulomb's law, Gauss's law, electric displacement $\mathbf{D}$, electrostatic potential $V$, Poisson's and Laplace's equations, polarization, and dielectric boundary conditions.
* **Steady Electric Currents**: Conduction current density $\mathbf{J}$, microscopic Ohm's law, equation of continuity, Joule heating dissipation, and boundary conditions for current flow.
* **Magnetostatics in Free Space and Magnetic Materials**: Biot-Savart law, Ampère's circuital law, magnetic flux density $\mathbf{B}$, magnetic vector potential $\mathbf{A}$, magnetization, and magnetic boundary conditions.
* **Electrodynamics and Maxwell's Equations**: Faraday's law of electromagnetic induction, Maxwell's displacement current, and complete differential/integral forms of Maxwell's equations.
* **Electromagnetic Wave Propagation**: Wave equations in lossless and conducting media, propagation constant $\gamma = \alpha + j\beta$, phase velocity, intrinsic impedance $\eta$, skin depth, and the Poynting vector.
* **Transmission Lines**: Distributed-parameter Telegrapher's equations, characteristic impedance $Z_0$, voltage reflection coefficient $\Gamma$, and Voltage Standing Wave Ratio (VSWR).

---

## Learning Objectives
* Formulate and solve electrostatic and magnetostatic boundary-value problems using differential and integral equations.
* Apply Maxwell's equations to analyze time-varying electromagnetic fields in diverse dielectric and conducting media.
* Calculate propagation constants, polarization states, and power density for plane electromagnetic waves.
* Analyze high-frequency transmission lines, calculate reflection coefficients, and solve impedance matching problems.
* Implement computational field simulators and analytical derivations in Python and SymPy.

---

## Directory Structure

| Directory | Description |
|:---|:---|
| [`Lectures/`](Lectures/) | Structured theory lectures and official slide decks covering the electromagnetic curriculum |
| [`Exercises/`](Exercises/) | Solved exercise drills on vector fields, Gauss's law, Ampere's law, and Maxwell's equations |
| [`Examples/`](Examples/) | Python simulators for electrostatic potential, plane waves, Biot-Savart, and transmission lines |
| [`Assignments/`](Assignments/) | Practical coursework assignments with hardware/field evaluation rubrics |
| [`Tutorials/`](Tutorials/) | Hands-on walkthroughs for boundary conditions, capacitance, and Poynting calculations |
| [`Projects/`](Projects/) | Capstone term design project (Computational Electromagnetic Field Solver) |
| [`Exams/`](Exams/) | Archival examination papers from 2024 and 2026, practice mock exams, and worked solutions |
| [`Resources/`](Resources/) | Detailed chapter notes, vector calculus reference sheets, and textbook bibliographies |

---

## Computational Examples in Python

The [`Examples/`](Examples/) directory contains numerical simulators and analytical notebooks:

```bash
# 1. Electrostatic potential and field vector 2D mesh simulation
python3 Examples/01_electrostatic_field_simulation.py

# 2. Time-harmonic plane wave propagation and attenuation simulator
python3 Examples/02_plane_wave_propagation_simulator.py

# 3. Biot-Savart magnetic field evaluations for wires and circular loops
python3 Examples/03_biot_savart_magnetic_field.py

# 4. Transmission line characteristic impedance, reflection, and VSWR calculator
python3 Examples/04_transmission_line_impedance_and_vswr.py
```
