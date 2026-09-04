# Electrostatics, Gauss's Law, and Electric Potential

## Overview
Electrostatics investigates the physical laws governing stationary electric charges, Coulomb forces, electric field intensity $\mathbf{E}$, electric displacement $\mathbf{D}$, and conservative electrostatic scalar potential $V$.

---

## 1. Fundamental Postulates of Electrostatics

In differential and integral forms:
$$\nabla \cdot \mathbf{D} = \rho_v \iff \oint_S \mathbf{D} \cdot d\mathbf{S} = Q_{\text{enclosed}}$$
$$\nabla \times \mathbf{E} = \mathbf{0} \iff \oint_C \mathbf{E} \cdot d\mathbf{l} = 0$$

Constitutive relation in isotropic, linear, homogeneous media:
$$\mathbf{D} = \varepsilon \mathbf{E} = \varepsilon_r \varepsilon_0 \mathbf{E}$$
where $\varepsilon_0 \approx 8.854 \times 10^{-12}\text{ F/m}$ is the permittivity of free space.

---

## 2. Electric Potential and Poisson's / Laplace's Equations

Because $\nabla \times \mathbf{E} = \mathbf{0}$, the electric field can be expressed as the negative gradient of a scalar potential:
$$\mathbf{E} = -\nabla V$$

Substituting into Gauss's Law yields **Poisson's Equation**:
$$\nabla \cdot (\varepsilon \nabla V) = -\rho_v \implies \nabla^2 V = -\frac{\rho_v}{\varepsilon}$$

In charge-free dielectric regions ($\rho_v = 0$), this simplifies to **Laplace's Equation**:
$$\nabla^2 V = 0$$

---

## 3. Electrostatic Boundary Conditions

At the planar interface between two dielectric media:
1. **Tangential Electric Field**: Continuous across interface:
   $$E_{1t} = E_{2t} \iff \hat{\mathbf{n}} \times (\mathbf{E}_1 - \mathbf{E}_2) = \mathbf{0}$$
2. **Normal Electric Flux Density**: Discontinuous by surface charge density $\rho_s$:
   $$D_{1n} - D_{2n} = \rho_s \iff \hat{\mathbf{n}} \cdot (\mathbf{D}_1 - \mathbf{D}_2) = \rho_s$$
   For ideal dielectrics without free surface charge ($\rho_s = 0$):
   $$D_{1n} = D_{2n} \implies \varepsilon_1 E_{1n} = \varepsilon_2 E_{2n}$$

