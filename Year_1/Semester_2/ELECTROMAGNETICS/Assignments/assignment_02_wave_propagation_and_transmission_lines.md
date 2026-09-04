# Assignment 02: Electromagnetic Wave Propagation and Transmission Lines

## Objective
Evaluate electromagnetic wave parameters in non-ideal media, calculate wave reflection and transmission across plane boundaries, and solve lossless transmission line impedance matching problems.

---

## Assignment Problems

### Problem 1: Wave Propagation in Good Conductors
A plane wave of frequency $f = 10 \text{ MHz}$ propagates in copper with conductivity $\sigma = 5.8 \times 10^7 \text{ S/m}$, relative permittivity $\varepsilon_r = 1$, and relative permeability $\mu_r = 1$.
1. Compute the skin depth $\delta$ of copper at $10\text{ MHz}$.
2. Determine the attenuation constant $\alpha$, phase constant $\beta$, and phase velocity $v_p$.
3. Compute the intrinsic impedance $\eta_c$ and state the phase difference between $\mathbf{E}$ and $\mathbf{H}$.
4. If the surface electric field amplitude is $E_0 = 10\text{ V/m}$, calculate the distance into the conductor at which the field amplitude reduces to $1\text{ mV/m}$.

### Problem 2: Normal Incidence at a Planar Dielectric Boundary
A uniform plane wave propagating in free space (Medium 1: $\varepsilon_{r1} = 1, \mu_{r1} = 1$) impinges normally upon a lossless dielectric half-space (Medium 2: $z \ge 0, \varepsilon_{r2} = 9, \mu_{r2} = 1$). The incident electric field is given by:
$$\mathbf{E}_i(z, t) = 15 \cos(6\pi \times 10^8 t - \beta_1 z) \hat{\mathbf{a}}_x \quad [\text{V/m}]$$
1. Calculate the reflection coefficient $\Gamma$ and transmission coefficient $\tau$.
2. Write complete time-domain expressions for the reflected field $\mathbf{E}_r(z, t)$ and transmitted field $\mathbf{E}_t(z, t)$.
3. Verify the conservation of energy by computing the time-averaged incident, reflected, and transmitted power densities ($S_{\text{avg}, i} = S_{\text{avg}, r} + S_{\text{avg}, t}$).
4. Calculate the Standing Wave Ratio (SWR) in Medium 1.

### Problem 3: Lossless Transmission Line Matching
A lossless transmission line with characteristic impedance $Z_0 = 50 \ \Omega$ is connected to a load impedance $Z_L = 100 + j50 \ \Omega$. The signal wavelength on the line is $\lambda = 2\text{ m}$.
1. Calculate the load reflection coefficient $\Gamma_L$ in polar form.
2. Determine the Voltage Standing Wave Ratio (VSWR).
3. Find the location of the voltage maximum nearest to the load.

---

## Evaluation Rubric
| Question | Focus Area | Points |
|---|---|---|
| Problem 1 | Good conductor approximations, skin depth, attenuation | 30 |
| Problem 2 | Reflection/transmission coefficients, Poynting vector balance, SWR | 40 |
| Problem 3 | Transmission line reflections, VSWR, standing wave peaks | 30 |
| **Total** | | **100** |

