# Assignment 01: Electrostatic Fields, Boundary Value Problems, and Capacitance

## Objective
Analyze electrostatic field distributions, solve one-dimensional Laplace boundary value problems, and compute electric flux and capacitance across inhomogeneous dielectric geometries.

---

## Assignment Problems

### Problem 1: Discrete and Line Charge Configurations
A uniform line charge of density $\rho_L = 25 \text{ nC/m}$ lies along the line $x = 2, y = -1$ in free space. A point charge of $Q = 50 \text{ nC}$ is located at the origin $(0, 0, 0)$.
1. Find the total electric field intensity $\mathbf{E}$ at point $P(2, 3, 0)$.
2. Calculate the total electric flux passing through the spherical surface of radius $r = 4\text{ m}$ centered at the origin.

### Problem 2: 1D Boundary Value Problem (Laplace's Equation)
Consider the region between two concentric conducting cylinders of radii $a = 1\text{ cm}$ and $b = 5\text{ cm}$. The inner cylinder is held at potential $V(a) = 100\text{ V}$, while the outer cylinder is grounded at $V(b) = 0\text{ V}$. The space between is filled with an inhomogeneous dielectric whose permittivity varies radially as $\varepsilon(\rho) = \varepsilon_0 \frac{a}{\rho}$.
1. Formulate the governing differential equation from $\nabla \cdot \mathbf{D} = 0$ in cylindrical coordinates.
2. Integrate to find the analytical expression for the potential profile $V(\rho)$.
3. Determine the electric field vector $\mathbf{E}(\rho)$.
4. Compute the capacitance per unit length $C/L$.

### Problem 3: Parallel Plate Capacitor with Multi-Layer Dielectric
A parallel-plate capacitor with plate area $A = 0.05 \text{ m}^2$ and plate separation $d = 6 \text{ mm}$ is filled with two dielectric slabs of equal thickness ($d_1 = d_2 = 3 \text{ mm}$):
* Slab 1 has $\varepsilon_{r1} = 2.5$.
* Slab 2 has $\varepsilon_{r2} = 6.0$.
If a potential difference of $V_0 = 120 \text{ V}$ is applied across the plates:
1. Calculate the equivalent capacitance $C$.
2. Find the electric field magnitude $E_1$ and $E_2$ in each dielectric region.
3. Determine the surface polarization charge density $\rho_{Ps}$ on the interface between the two slabs.

---

## Evaluation Rubric
| Problem | Focus Area | Points |
|---|---|---|
| Problem 1 | Coulomb superposition, line charge field, Gauss's law flux | 30 |
| Problem 2 | Laplace equation integration, variable permittivity, capacitance | 40 |
| Problem 3 | Series dielectric boundary conditions, field distribution, polarization | 30 |
| **Total** | | **100** |

