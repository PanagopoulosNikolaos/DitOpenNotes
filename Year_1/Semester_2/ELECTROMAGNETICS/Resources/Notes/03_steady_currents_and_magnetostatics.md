# Steady Currents and Magnetostatics

## Overview
Magnetostatics addresses constant, time-invariant magnetic fields produced by steady electric currents, governed by the Biot-Savart Law and Ampère's Circuital Law.

---

## 1. Current Density and Continuity Equation

Electric current density $\mathbf{J}$ represents charge flow per unit cross-sectional area:
$$I = \int_S \mathbf{J} \cdot d\mathbf{S}$$

Ohm's Law in point form:
$$\mathbf{J} = \sigma \mathbf{E}$$
where $\sigma$ is electrical conductivity ($\text{S/m}$).

The **Continuity Equation** enforces conservation of charge:
$$\nabla \cdot \mathbf{J} = -\frac{\partial \rho_v}{\partial t}$$
For steady direct currents ($\partial \rho_v / \partial t = 0$), the divergence vanishes:
$$\nabla \cdot \mathbf{J} = 0 \iff \oint_S \mathbf{J} \cdot d\mathbf{S} = 0$$

---

## 2. Fundamental Postulates of Magnetostatics

In differential and integral forms:
$$\nabla \cdot \mathbf{B} = 0 \iff \oint_S \mathbf{B} \cdot d\mathbf{S} = 0$$
$$\nabla \times \mathbf{H} = \mathbf{J} \iff \oint_C \mathbf{H} \cdot d\mathbf{l} = I_{\text{enclosed}}$$

Constitutive relation in isotropic, linear media:
$$\mathbf{B} = \mu \mathbf{H} = \mu_r \mu_0 \mathbf{H}$$
where $\mu_0 = 4\pi \times 10^{-7}\text{ H/m}$ is the permeability of free space.

---

## 3. Magnetic Vector Potential ($\mathbf{A}$)

Because $\nabla \cdot \mathbf{B} = 0$, the magnetic flux density can be defined as the curl of a magnetic vector potential $\mathbf{A}$:
$$\mathbf{B} = \nabla \times \mathbf{A}$$

Under the Coulomb gauge condition ($\nabla \cdot \mathbf{A} = 0$):
$$\nabla^2 \mathbf{A} = -\mu \mathbf{J}$$

For an arbitrary steady current distribution:
$$\mathbf{A}(\mathbf{r}) = \frac{\mu}{4\pi} \int_V \frac{\mathbf{J}(\mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|} \, dv'$$

---

## 4. Magnetostatic Boundary Conditions

At the interface between two magnetic media:
1. **Normal Magnetic Flux Density**: Always continuous across interface:
   $$B_{1n} = B_{2n} \iff \hat{\mathbf{n}} \cdot (\mathbf{B}_1 - \mathbf{B}_2) = 0$$
2. **Tangential Magnetic Field Intensity**: Discontinuous by surface current density $\mathbf{J}_s$:
   $$\hat{\mathbf{n}} \times (\mathbf{H}_1 - \mathbf{H}_2) = \mathbf{J}_s$$
   When no surface currents exist ($\mathbf{J}_s = \mathbf{0}$):
   $$H_{1t} = H_{2t}$$

