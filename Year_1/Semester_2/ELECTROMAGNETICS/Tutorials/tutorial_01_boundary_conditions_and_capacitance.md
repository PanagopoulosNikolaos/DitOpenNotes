# Tutorial 01: Electrostatic Boundary Conditions and Capacitance Calculations

## Context and Grounding
This tutorial provides a step-by-step problem-solving methodology for applying interface boundary conditions across dielectric and conductor boundaries, and calculating the capacitance of coaxial, spherical, and parallel geometries. It directly grounds `Lectures/02_EM.pdf` and `Exercises/01_test.md`.

---

## 1. Summary of Boundary Conditions

At an interface between two media (Medium 1 and Medium 2):

### 1.1 Tangential Components
Apply Faraday's Law around an infinitesimal loop across the interface:
$$E_{1t} = E_{2t} \iff \frac{D_{1t}}{\varepsilon_1} = \frac{D_{2t}}{\varepsilon_2}$$
**Rule:** The tangential component of the electric field $\mathbf{E}$ is continuous across any boundary.

### 1.2 Normal Components
Apply Gauss's Law to a small pillbox spanning the interface:
$$D_{1n} - D_{2n} = \rho_S \iff \varepsilon_1 E_{1n} - \varepsilon_2 E_{2n} = \rho_S$$
If the interface is charge-free ($\rho_S = 0$):
$$D_{1n} = D_{2n} \iff \varepsilon_1 E_{1n} = \varepsilon_2 E_{2n}$$
**Rule:** The normal component of $\mathbf{D}$ is continuous across a charge-free dielectric interface.

---

## 2. Worked Capacitance Problem: Coaxial Cable

### Problem Statement
Find the capacitance per unit length of a coaxial cable consisting of an inner conductor of radius $a$ and an outer conductor of inner radius $b$, filled with a dielectric of relative permittivity $\varepsilon_r$.

### Step 1: Assume Charge Distribution
Assume the inner conductor carries uniform line charge $+Q$ per length $L$ ($\rho_L = Q/L$), and the outer conductor carries $-Q$.

### Step 2: Determine Electric Field using Gauss's Law
Construct a cylindrical Gaussian surface of radius $\rho$ ($a < \rho < b$) and length $L$:
$$\oint_S \mathbf{D} \cdot d\mathbf{S} = D_\rho (2\pi \rho L) = Q$$
$$D_\rho = \frac{Q}{2\pi \rho L} \implies \mathbf{E} = \frac{Q}{2\pi \varepsilon_r \varepsilon_0 \rho L} \hat{\mathbf{a}}_\rho$$

### Step 3: Compute Potential Difference $V$
Integrate $\mathbf{E}$ from the outer conductor ($\rho = b$) to the inner conductor ($\rho = a$):
$$V = -\int_b^a \mathbf{E} \cdot d\mathbf{l} = -\int_b^a \frac{Q}{2\pi \varepsilon \rho L} d\rho = \frac{Q}{2\pi \varepsilon L} \int_a^b \frac{d\rho}{\rho}$$
$$V = \frac{Q}{2\pi \varepsilon_r \varepsilon_0 L} \ln\left(\frac{b}{a}\right)$$

### Step 4: Calculate Capacitance
$$C = \frac{Q}{V} = \frac{2\pi \varepsilon_r \varepsilon_0 L}{\ln(b/a)}$$
Capacitance per unit length:
$$\frac{C}{L} = \frac{2\pi \varepsilon_r \varepsilon_0}{\ln(b/a)} \quad [\text{F/m}]$$

