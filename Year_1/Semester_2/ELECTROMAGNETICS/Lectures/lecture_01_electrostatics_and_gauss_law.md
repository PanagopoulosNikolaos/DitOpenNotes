# Lecture 01: Electrostatics, Coulomb's Law, and Gauss's Law

## Context and Grounding
This lecture note establishes the mathematical principles of electrostatic fields, Coulomb's Law, the electric potential, and Gauss's Law in differential and integral forms. It directly connects with `Lectures/01_EM.pdf` through `03_EM.pdf` and `Exercises/01_test.md`.

---

## 1. Coulomb's Law and Electric Field Intensity

### 1.1 Coulomb's Law
The electrostatic force $\mathbf{F}_{12}$ exerted by a point charge $q_1$ on charge $q_2$ located at distance $R$ in free space is:
$$\mathbf{F}_{12} = \frac{1}{4\pi \varepsilon_0} \frac{q_1 q_2}{R^2} \hat{\mathbf{a}}_R$$
where $\varepsilon_0 \approx 8.854 \times 10^{-12} \text{ F/m}$ is the permittivity of free space.

### 1.2 Electric Field Intensity $\mathbf{E}$
The electric field intensity is defined as the force per unit positive test charge:
$$\mathbf{E} = \lim_{q_t \to 0} \frac{\mathbf{F}}{q_t} = \frac{q}{4\pi \varepsilon_0 R^2} \hat{\mathbf{a}}_R \quad [\text{V/m}]$$

For continuous charge distributions:
* **Line Charge ($\rho_L$)**: $\mathbf{E} = \frac{1}{4\pi \varepsilon_0} \int_L \frac{\rho_L dL'}{R^2} \hat{\mathbf{a}}_R$
* **Surface Charge ($\rho_S$)**: $\mathbf{E} = \frac{1}{4\pi \varepsilon_0} \int_S \frac{\rho_S dS'}{R^2} \hat{\mathbf{a}}_R$
* **Volume Charge ($\rho_v$)**: $\mathbf{E} = \frac{1}{4\pi \varepsilon_0} \int_V \frac{\rho_v dv'}{R^2} \hat{\mathbf{a}}_R$

---

## 2. Electric Flux Density and Gauss's Law

### 2.1 Electric Flux Density $\mathbf{D}$
In an isotropic dielectric medium with permittivity $\varepsilon = \varepsilon_r \varepsilon_0$:
$$\mathbf{D} = \varepsilon \mathbf{E} \quad [\text{C/m}^2]$$

### 2.2 Gauss's Law
* **Integral Form**: The total electric flux passing through any closed Gaussian surface $S$ equals the net enclosed charge:
  $$\oint_S \mathbf{D} \cdot d\mathbf{S} = Q_{\text{enclosed}} = \int_V \rho_v dv$$
* **Differential (Point) Form**: Applying the Divergence Theorem ($\oint_S \mathbf{D} \cdot d\mathbf{S} = \int_V (\nabla \cdot \mathbf{D}) dv$):
  $$\nabla \cdot \mathbf{D} = \rho_v$$
This is the **first of Maxwell's four equations**.

---

## 3. Electric Potential and Conservative Fields

Because the electrostatic field is conservative ($\nabla \times \mathbf{E} = \mathbf{0}$), the work done in moving a charge between two points is independent of the path.

### 3.1 Potential Difference $V$
$$V_{ba} = V_b - V_a = -\int_a^b \mathbf{E} \cdot d\mathbf{l}$$
The electric field is related to potential by the negative gradient:
$$\mathbf{E} = -\nabla V$$

### 3.2 Poisson's and Laplace's Equations
Substituting $\mathbf{D} = \varepsilon \mathbf{E} = -\varepsilon \nabla V$ into Gauss's Law:
$$\nabla \cdot (-\varepsilon \nabla V) = \rho_v$$
In a homogeneous medium ($\varepsilon = \text{constant}$):
* **Poisson's Equation**: $\nabla^2 V = -\frac{\rho_v}{\varepsilon}$
* **Laplace's Equation** (in charge-free regions, $\rho_v = 0$): $\nabla^2 V = 0$

---

## 4. Capacitance and Boundary Conditions

Capacitance measures charge storage per unit potential difference:
$$C = \frac{Q}{V} = \frac{\oint_S \varepsilon \mathbf{E} \cdot d\mathbf{S}}{\int_+^- \mathbf{E} \cdot d\mathbf{l}} \quad [\text{Farads, F}]$$

For a parallel-plate capacitor with area $A$, plate separation $d$, and dielectric constant $\kappa = \varepsilon_r$:
$$C = \frac{\kappa \varepsilon_0 A}{d}$$
Electrostatic energy stored in the electric field:
$$W_E = \frac{1}{2} C V^2 = \frac{1}{2} \int_V \mathbf{D} \cdot \mathbf{E} \, dv$$

