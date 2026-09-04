# Project 01: 2D Finite-Difference Electrostatic Field and Capacitance Solver

## Project Overview
Design, implement, and validate a 2D numerical field solver in Python or C using the Finite Difference Method (FDM) to solve Laplace's and Poisson's equations:
$$\nabla^2 V = \frac{\partial^2 V}{\partial x^2} + \frac{\partial^2 V}{\partial y^2} = -\frac{\rho_v}{\varepsilon}$$
The solver simulates complex conductor geometries (such as microstrip transmission lines, coaxial shields with rectangular cross-sections, and split-cylinder capacitors), computes potential contours, extracts vector electric fields $\mathbf{E} = -\nabla V$, and numerically evaluates total stored energy and capacitance.

---

## 1. Mathematical Formulation and Numerical Schema

### 1.1 Five-Point Stencil Discretization
Using central difference approximations on a uniform 2D grid with spatial step $\Delta x = \Delta y = h$:
$$\frac{V_{i+1, j} - 2V_{i, j} + V_{i-1, j}}{h^2} + \frac{V_{i, j+1} - 2V_{i, j} + V_{i, j-1}}{h^2} = 0$$
Solving for the center node potential $V_{i, j}$:
$$V_{i, j} = \frac{1}{4} \left( V_{i+1, j} + V_{i-1, j} + V_{i, j+1} + V_{i, j-1} \right)$$

### 1.2 Iterative Solvers
Implement both:
1. **Jacobi Iteration**: Updates all grid points simultaneously using values from the previous iteration.
2. **Successive Over-Relaxation (SOR)** with parameter $\omega \in (1, 2)$:
   $$V_{i, j}^{(k+1)} = (1 - \omega) V_{i, j}^{(k)} + \frac{\omega}{4} \left( V_{i-1, j}^{(k+1)} + V_{i+1, j}^{(k)} + V_{i, j-1}^{(k+1)} + V_{i, j+1}^{(k)} \right)$$

---

## 2. Core Functional Requirements

### 2.1 Boundary Condition Support
* **Dirichlet Boundaries**: Fixed potential values on conducting surfaces (e.g., $V = 100\text{ V}$ on inner trace, $V = 0\text{ V}$ on ground plane).
* **Neumann Boundaries**: Normal derivative $\partial V / \partial n = 0$ representing planes of symmetry or insulated boundaries.

### 2.2 Energy and Capacitance Extraction
1. Compute the electric field components at each grid cell:
   $$E_{x, i, j} = -\frac{V_{i+1, j} - V_{i-1, j}}{2h}, \quad E_{y, i, j} = -\frac{V_{i, j+1} - V_{i, j-1}}{2h}$$
2. Calculate total electrostatic energy stored in the computational domain:
   $$W_E = \frac{1}{2} \varepsilon_0 \sum_{i, j} \left( E_{x, i, j}^2 + E_{y, i, j}^2 \right) h^2$$
3. Deduce capacitance per unit length from stored energy:
   $$C = \frac{2 W_E}{V_0^2} \quad [\text{F/m}]$$

### 2.3 Benchmark Validation
Validate the numerical solver against the analytical solution for a standard concentric coaxial cable ($a = 1\text{ cm}, b = 3\text{ cm}, V_0 = 100\text{ V}$), reporting the percentage error as a function of grid resolution $h$.

---

## 3. Project Deliverables and Architecture

* `fdm_solver/`
  * `grid.py` / `grid.c`: Grid representation, boundary masking, and initial conditions.
  * `solver.py` / `solver.c`: Jacobi, Gauss-Seidel, and SOR iterative numerical solvers.
  * `postprocess.py` / `postprocess.c`: Gradient calculation, electric field vector generation, energy summation.
  * `benchmark.py` / `benchmark.c`: Analytical comparison and error convergence curves.
  * `README.md`: Theory summary, execution instructions, and convergence analysis graphs.

---

## 4. Evaluation Rubric
| Criterion | Description | Points |
|---|---|---|
| FDM Implementation | Correct central difference discretization and Dirichlet/Neumann handling | 25 |
| Convergence & Performance | Working SOR solver with optimal relaxation parameter $\omega$ | 25 |
| Field & Energy Derivation | Accurate $\mathbf{E}$-field gradient extraction and discrete energy integration | 20 |
| Analytical Benchmark Verification | Quantitative convergence analysis against coaxial analytical baseline | 20 |
| Code Standards & Documentation | Clean modular structure, Google-style docstrings, zero warnings | 10 |
| **Total** | | **100** |

