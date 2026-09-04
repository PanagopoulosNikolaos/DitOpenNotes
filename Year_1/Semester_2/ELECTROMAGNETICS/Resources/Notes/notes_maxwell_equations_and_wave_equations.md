# Deep-Dive Notes: Maxwell's Equations and Wave Solutions

## Overview
This reference note compiles the formal mathematical derivations for the electromagnetic wave equation from Maxwell's postulates, wave impedance in conducting media, and Poynting energy conservation theorems.

---

## 1. Derivation of the Vector Helmholtz Equation

Beginning with Maxwell's curl equations for time-harmonic fields ($e^{j\omega t}$ convention):
$$\nabla \times \mathbf{E} = -j\omega\mu \mathbf{H}$$
$$\nabla \times \mathbf{H} = (\sigma + j\omega\varepsilon) \mathbf{E}$$

Take the curl of the first equation:
$$\nabla \times (\nabla \times \mathbf{E}) = -j\omega\mu (\nabla \times \mathbf{H})$$
Substitute the second equation:
$$\nabla(\nabla \cdot \mathbf{E}) - \nabla^2 \mathbf{E} = -j\omega\mu (\sigma + j\omega\varepsilon) \mathbf{E}$$

In a source-free region ($\rho_v = 0 \implies \nabla \cdot \mathbf{E} = 0$):
$$\nabla^2 \mathbf{E} - \gamma^2 \mathbf{E} = \mathbf{0}$$
where the **complex propagation constant** $\gamma$ is:
$$\gamma = \alpha + j\beta = \sqrt{j\omega\mu(\sigma + j\omega\varepsilon)}$$

---

## 2. Poynting's Theorem (Energy Conservation)

Using the vector identity $\nabla \cdot (\mathbf{E} \times \mathbf{H}) = \mathbf{H} \cdot (\nabla \times \mathbf{E}) - \mathbf{E} \cdot (\nabla \times \mathbf{H})$:
$$\nabla \cdot (\mathbf{E} \times \mathbf{H}) = \mathbf{H} \cdot \left(-\frac{\partial \mathbf{B}}{\partial t}\right) - \mathbf{E} \cdot \left(\mathbf{J} + \frac{\partial \mathbf{D}}{\partial t}\right)$$
Rearranging terms and integrating over volume $V$ bounded by surface $S$:
$$-\oint_S (\mathbf{E} \times \mathbf{H}) \cdot d\mathbf{S} = \int_V \mathbf{J} \cdot \mathbf{E} \, dv + \frac{\partial}{\partial t} \int_V \left( \frac{1}{2} \varepsilon E^2 + \frac{1}{2} \mu H^2 \right) dv$$

### Physical Interpretation
* **Left-Hand Side**: Total electromagnetic power flowing inward through closed surface $S$.
* **First Term on Right**: Ohmic Joule heating loss in the volume (power dissipated).
* **Second Term on Right**: Time rate of change of energy stored in the electric and magnetic fields.

---

## 3. Transmission Line Telegrapher's Equations
For distributed parameters $R$ (resistance/m), $L$ (inductance/m), $G$ (conductance/m), $C$ (capacitance/m):
$$\frac{\partial V}{\partial z} = -(R + j\omega L) I$$
$$\frac{\partial I}{\partial z} = -(G + j\omega C) V$$
Characteristic impedance:
$$Z_0 = \sqrt{\frac{R + j\omega L}{G + j\omega C}}$$
For a lossless line ($R = G = 0$):
$$Z_0 = \sqrt{\frac{L}{C}}, \quad v_p = \frac{1}{\sqrt{LC}}$$

