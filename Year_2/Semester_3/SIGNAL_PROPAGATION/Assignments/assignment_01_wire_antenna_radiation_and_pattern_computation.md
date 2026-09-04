# Assignment 01: Wire Antenna Radiation and Pattern Computation

## Objective
Assess analytical derivations of wire antenna far fields, radiation resistance calculations, directivity calculations, and numerical pattern plotting for infinitesimal dipoles, half-wave dipoles, and quarter-wave monopoles.

---

## Problem Set

### Problem 1: Directivity of an Infinitesimal Dipole
The normalized power pattern of an infinitesimal dipole oriented along the $z$-axis is:
$$
P_n(\theta, \phi) = \sin^2\theta, \quad 0 \le \theta \le \pi, \quad 0 \le \phi \le 2\pi
$$
1. Compute the beam solid angle $\Omega_A$ by evaluating the surface integral over the unit sphere.
2. Determine the exact maximum directivity $D_0$ in dimensionless units and in $\text{dBi}$.
3. Calculate the Half-Power Beamwidth (HPBW) in degrees.

### Problem 2: Radiation Resistance and Efficiency
A center-fed thin dipole has total physical length $l = 10\text{ cm}$ and operates at $f = 150\text{ MHz}$. The wire is constructed from copper ($\sigma = 5.8 \times 10^7\text{ S/m}$) with wire radius $a = 1.0\text{ mm}$.
1. Calculate the wavelength $\lambda$ and express the dipole length in terms of $\lambda$.
2. State whether the infinitesimal dipole or sinusoidal distribution model is appropriate.
3. Compute the radiation resistance $R_{\text{rad}}$ and conduction loss resistance $R_{\text{loss}}$.
4. Determine the radiation efficiency $\eta_{cd}$ of the antenna.

### Problem 3: Quarter-Wave Monopole vs. Free-Space Dipole
Using Image Theory:
1. Explain why the radiation resistance of a quarter-wave monopole over a perfect electric conductor (PEC) ground plane is half that of an isolated half-wave dipole.
2. Explain why the directivity of the monopole is double ($+3\text{ dB}$) that of the half-wave dipole.
3. If an input power of $P_{\text{in}} = 50\text{ W}$ is delivered to a quarter-wave monopole, compute the electric field magnitude $|\mathbf{E}|$ at distance $r = 1.5\text{ km}$ along the horizon ($\theta = 90^\circ$).

---

## Deliverables
A comprehensive engineering report presenting detailed mathematical derivations, numerical evaluations, and annotated polar pattern sketches.

