# Lecture 03: Faraday's Law, Maxwell's Equations, and Plane Waves

## Context and Grounding
This lecture note synthesizes electrodynamics, Faraday's induction law, Maxwell's displacement current modification, the full system of Maxwell's equations, and electromagnetic wave propagation. It directly grounds `Lectures/07_EM.pdf` through `09_EM.pdf` and `Exercises/03_test.md`.

---

## 1. Time-Varying Fields and Faraday's Law

Michael Faraday discovered that a time-varying magnetic flux generates an electromotive force (EMF) around a closed loop:
$$\text{EMF} = \oint_C \mathbf{E} \cdot d\mathbf{l} = -\frac{d\Phi}{dt} = -\frac{d}{dt} \int_S \mathbf{B} \cdot d\mathbf{S}$$

Applying Stokes' Theorem yields the differential form:
$$\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$$

---

## 2. Maxwell's Displacement Current

Taking the divergence of static Ampere's Law ($\nabla \times \mathbf{H} = \mathbf{J}$):
$$\nabla \cdot (\nabla \times \mathbf{H}) = 0 \implies \nabla \cdot \mathbf{J} = 0$$
However, the continuity equation requires $\nabla \cdot \mathbf{J} = -\frac{\partial \rho_v}{\partial t}$.
To resolve this inconsistency during capacitor charging/discharging, James Clerk Maxwell added the **displacement current density** $\mathbf{J}_D$:
$$\mathbf{J}_D = \frac{\partial \mathbf{D}}{\partial t}$$

Ampere-Maxwell Law:
$$\nabla \times \mathbf{H} = \mathbf{J} + \frac{\partial \mathbf{D}}{\partial t}$$

---

## 3. The Complete Maxwell Equations

| Law | Differential Form | Integral Form | Physical Significance |
|---|---|---|---|
| **Gauss's Law** | $\nabla \cdot \mathbf{D} = \rho_v$ | $\oint_S \mathbf{D} \cdot d\mathbf{S} = Q_{\text{enc}}$ | Electric charges generate electric flux. |
| **Gauss's Law (Mag)** | $\nabla \cdot \mathbf{B} = 0$ | $\oint_S \mathbf{B} \cdot d\mathbf{S} = 0$ | No isolated magnetic monopoles exist. |
| **Faraday's Law** | $\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$ | $\oint_C \mathbf{E} \cdot d\mathbf{l} = -\int_S \frac{\partial \mathbf{B}}{\partial t} \cdot d\mathbf{S}$ | Time-varying $\mathbf{B}$ induces electric field. |
| **Ampere-Maxwell** | $\nabla \times \mathbf{H} = \mathbf{J} + \frac{\partial \mathbf{D}}{\partial t}$ | $\oint_C \mathbf{H} \cdot d\mathbf{l} = \int_S \left(\mathbf{J} + \frac{\partial \mathbf{D}}{\partial t}\right) \cdot d\mathbf{S}$ | Conduction & displacement currents induce $\mathbf{B}$. |

---

## 4. Electromagnetic Wave Equation in Free Space

In source-free, non-conducting vacuum ($\rho_v = 0, \mathbf{J} = \mathbf{0}, \mu = \mu_0, \varepsilon = \varepsilon_0$):
$$\nabla \times (\nabla \times \mathbf{E}) = -\mu_0 \frac{\partial}{\partial t}(\nabla \times \mathbf{H}) = -\mu_0 \varepsilon_0 \frac{\partial^2 \mathbf{E}}{\partial t^2}$$
Using vector identity $\nabla \times (\nabla \times \mathbf{E}) = \nabla(\nabla \cdot \mathbf{E}) - \nabla^2 \mathbf{E}$ (with $\nabla \cdot \mathbf{E} = 0$):
$$\nabla^2 \mathbf{E} - \mu_0 \varepsilon_0 \frac{\partial^2 \mathbf{E}}{\partial t^2} = \mathbf{0}$$

This is the standard 3D wave equation with propagation speed:
$$c = \frac{1}{\sqrt{\mu_0 \varepsilon_0}} \approx 2.998 \times 10^8 \text{ m/s}$$

---

## 5. Uniform Plane Waves and Poynting Vector

For a transverse electromagnetic (TEM) wave propagating in the $+z$ direction with $\mathbf{E} = E_x(z, t) \hat{\mathbf{a}}_x$:
$$\mathbf{E}(z, t) = E_0 \cos(\omega t - kz) \hat{\mathbf{a}}_x$$
$$\mathbf{B}(z, t) = \frac{E_0}{c} \cos(\omega t - kz) \hat{\mathbf{a}}_y$$
where $k = \frac{\omega}{c} = \frac{2\pi}{\lambda}$ is the wavenumber.

### 5.1 Intrinsic Wave Impedance
$$\eta = \frac{|\mathbf{E}|}{|\mathbf{H}|} = \sqrt{\frac{\mu}{\varepsilon}}$$
In free space:
$$\eta_0 = \sqrt{\frac{\mu_0}{\varepsilon_0}} \approx 120\pi \approx 377 \ \Omega$$

### 5.2 Poynting Vector and Power Flow
The instantaneous rate of energy transfer per unit area is given by the **Poynting vector**:
$$\mathbf{S} = \mathbf{E} \times \mathbf{H} \quad [\text{W/m}^2]$$
For sinusoidal waves, the time-averaged power density (intensity) is:
$$\mathbf{S}_{\text{avg}} = \frac{1}{2} \text{Re}\{\mathbf{E} \times \mathbf{H}^*\} = \frac{E_0^2}{2\eta} \hat{\mathbf{a}}_z$$

