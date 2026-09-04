# Lecture 02: Magnetostatics, Biot-Savart Law, and Ampere's Law

## Context and Grounding
This lecture note introduces magnetic flux density, steady electric currents, the Biot-Savart law, Ampere's circuital law, and magnetic boundary conditions. It directly connects with `Lectures/04_EM.pdf`, `05_EM.pdf`, and `Exercises/02_test.md`.

---

## 1. Steady Currents and the Continuity Equation

A steady current flow implies constant charge density over time ($\partial \rho_v / \partial t = 0$).

### 1.1 Current Density $\mathbf{J}$
The current $I$ passing through surface $S$ is the flux of current density $\mathbf{J}$:
$$I = \int_S \mathbf{J} \cdot d\mathbf{S} \quad [\text{Amperes, A}]$$
Ohm's law in point form:
$$\mathbf{J} = \sigma \mathbf{E}$$
where $\sigma$ is the electrical conductivity $[\text{S/m}]$.

### 1.2 Principle of Conservation of Charge
$$\nabla \cdot \mathbf{J} = -\frac{\partial \rho_v}{\partial t}$$
For magnetostatic steady currents:
$$\nabla \cdot \mathbf{J} = 0$$

---

## 2. The Biot-Savart Law

The magnetic field increment $d\mathbf{B}$ produced at point $P$ by differential current element $I d\mathbf{l}'$ located at distance $R$ is:
$$d\mathbf{B} = \frac{\mu_0 I}{4\pi} \frac{d\mathbf{l}' \times \hat{\mathbf{a}}_R}{R^2} \quad [\text{Tesla, T}]$$
where $\mu_0 = 4\pi \times 10^{-7} \text{ T}\cdot\text{m/A}$ is the permeability of free space.

### 2.1 Infinite Straight Conductor
Integrating the Biot-Savart law for an infinitely long wire carrying current $I$ along the $z$-axis yields:
$$\mathbf{B} = \frac{\mu_0 I}{2\pi \rho} \hat{\mathbf{a}}_\phi$$

---

## 3. Ampere's Circuital Law

Ampere's Circuital Law states that the line integral of magnetic field intensity $\mathbf{H} = \mathbf{B}/\mu$ around any closed path $C$ equals the net electric current enclosed:
$$\oint_C \mathbf{H} \cdot d\mathbf{l} = I_{\text{enclosed}} = \int_S \mathbf{J} \cdot d\mathbf{S}$$

### 3.1 Differential Form
Applying Stokes' Theorem ($\oint_C \mathbf{H} \cdot d\mathbf{l} = \int_S (\nabla \times \mathbf{H}) \cdot d\mathbf{S}$):
$$\nabla \times \mathbf{H} = \mathbf{J}$$

---

## 4. Gauss's Law for Magnetism and Vector Potential

Magnetic field lines form continuous closed loops without start or termination points.
* **Integral Form**:
  $$\oint_S \mathbf{B} \cdot d\mathbf{S} = 0$$
* **Differential Form**:
  $$\nabla \cdot \mathbf{B} = 0$$
Physical Meaning: **Isolated magnetic monopoles do not exist in nature**.

### 4.1 Magnetic Vector Potential $\mathbf{A}$
Since $\nabla \cdot \mathbf{B} = 0$ and the divergence of any curl is identically zero ($\nabla \cdot (\nabla \times \mathbf{A}) = 0$), $\mathbf{B}$ can be derived from a magnetic vector potential $\mathbf{A}$:
$$\mathbf{B} = \nabla \times \mathbf{A}$$

---

## 5. Forces in Magnetic Fields

* **Lorentz Force on a Moving Charge**:
  $$\mathbf{F} = q(\mathbf{E} + \mathbf{v} \times \mathbf{B})$$
* **Magnetic Force on a Current Element**:
  $$d\mathbf{F} = I d\mathbf{l} \times \mathbf{B}$$
* **Force Between Two Parallel Wires**:
  $$\frac{F}{L} = \frac{\mu_0 I_1 I_2}{2\pi d}$$
  (Attractive when currents flow in the same direction; repulsive when anti-parallel).

