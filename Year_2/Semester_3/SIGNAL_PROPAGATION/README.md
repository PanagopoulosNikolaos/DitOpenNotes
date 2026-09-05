# Signal Propagation

## Course Overview
This course provides a rigorous engineering treatment of electromagnetic wave propagation and antenna systems in telecommunications. Topics include Maxwell's equations in media, uniform plane waves, polarization, reflection and refraction, Poynting vector power density, radiation integrals and potentials, fundamental antenna parameters, wire antennas and dipoles, antenna arrays, phased beam steering, Friis transmission equations, and RF link budget modeling.

## Course Code
304 (SIGNAL PROPAGATION)

## Prerequisites
* Electromagnetics (Code: 201)
* Mathematical Analysis (Code: 101)

---

## Topics Covered
* **Electromagnetic Wave Propagation**: Maxwell's equations in differential and time-harmonic form, wave equations in lossless and lossy media, intrinsic impedance $\eta$, attenuation and phase constants ($\alpha, \beta$), skin depth, and polarization states (Linear, Circular, Elliptical).
* **Power and Energy Flow**: Poynting's Theorem, instantaneous and time-average Poynting vectors, radiation intensity, and power density.
* **Antenna Fundamentals**: Radiation mechanisms, radiation patterns (Cartesian and polar), half-power beamwidth (HPBW), first-null beamwidth (FNBW), radiation resistance, input impedance, directivity ($D_0$), antenna efficiency, and absolute gain ($G_0$).
* **Linear Wire Antennas**: Infinitesimal dipoles, finite-length center-fed dipoles, half-wave dipoles ($l = \lambda/2$), quarter-wave monopoles, image theory over perfect electric conductors (PEC), and small loop antennas.
* **Antenna Arrays & Phased Synthesis**: Two-element arrays, $N$-element Uniform Linear Arrays (ULA), Array Factor (AF), pattern multiplication theorem, broadside and end-fire arrays, electronic beam steering, and grating lobe avoidance.
* **Wireless Link Budgets & Propagation Models**: Free-Space Path Loss (FSPL), Friis transmission equation, Two-Ray ground reflection model, crossover distance, fade margins, receiver sensitivity, and noise figures.
* **Impedance Matching & Smith Charts**: Transmission line theory, reflection coefficient $\Gamma$, Voltage Standing Wave Ratio (VSWR), quarter-wave transformer matching, and single-stub tuning.

---

## Learning Objectives
* Calculate electromagnetic field quantities, wave velocity, polarization, and power flow through diverse physical media.
* Design and compute performance parameters (directivity, radiation resistance, effective aperture) for dipoles, monopoles, and loops.
* Synthesize phased antenna arrays to steer main radiation beams to target angles while suppressing side lobes and grating lobes.
* Construct end-to-end RF link budgets evaluating received power, path losses, and system fade margins for terrestrial and satellite links.
* Perform impedance matching calculations using analytical methods and Smith Chart techniques.

---

## Directory Structure

| Directory | Description |
|:---|:---|
| [`Lectures/`](Lectures/) | Structured theory lectures on EM waves, antenna parameters, wire antennas, and phased arrays |
| [`Exercises/`](Exercises/) | Solved quantitative problem sets on antenna directivity, dipole radiation, and array factors |
| [`Examples/`](Examples/) | Executable Python simulations for radiation patterns, array factor synthesis, and RF link budgets |
| [`Assignments/`](Assignments/) | Computational coursework on wire antenna patterns and phased linear array beamforming |
| [`Tutorials/`](Tutorials/) | Hands-on walkthroughs for Friis link budgets and Smith Chart impedance matching |
| [`Projects/`](Projects/) | Capstone design project: Wireless Link Budget and Phased Array Beamforming Simulator |
| [`Exams/`](Exams/) | 100-point model practice examination with complete worked solutions and grading rubrics |
| [`Resources/`](Resources/) | 17 comprehensive topic notes, curriculum mindmap, and curated antenna textbooks |

---

## Computational Simulations

To execute the RF link budget and radiation pattern generator:
```bash
python3 Examples/examples_radiation_pattern_and_link_budget.py
```
