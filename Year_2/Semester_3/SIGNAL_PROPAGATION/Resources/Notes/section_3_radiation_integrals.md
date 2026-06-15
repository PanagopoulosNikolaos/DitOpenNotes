# Radiation Integrals and Auxiliary Potential Functions

Radiation integrals provide the mathematical framework for computing the electromagnetic fields radiated by arbitrary current distributions. Rather than solving for the electric and magnetic fields directly from Maxwell's equations, the approach introduces auxiliary potential functions — the magnetic vector potential $\mathbf{A}$ and the electric vector potential $\mathbf{F}$ — which satisfy simpler wave equations. Once these potentials are obtained from the source currents via integral formulations, the radiated fields follow by differentiation. This section covers the definition of the vector potentials, the solution of their inhomogeneous wave equations, far-field approximations, and the duality and reciprocity theorems that relate solutions across different source configurations.

---

## 1. Conceptual Foundation

### 1.1 Why Auxiliary Potentials Are Needed

Solving Maxwell's equations directly for the radiated fields $\mathbf{E}$ and $\mathbf{H}$ from an arbitrary current distribution $\mathbf{J}$ is mathematically cumbersome because it requires solving coupled vector partial differential equations. By introducing the magnetic vector potential $\mathbf{A}$, the problem is decomposed into two simpler steps:

1. Compute $\mathbf{A}$ from the source $\mathbf{J}$ by solving a scalar Helmholtz equation per component.
2. Derive $\mathbf{E}$ and $\mathbf{H}$ from $\mathbf{A}$ using straightforward differentiation.

A parallel approach using the electric vector potential $\mathbf{F}$ handles magnetic current sources $\mathbf{M}$, which are mathematical fictions introduced by the equivalence principle to simplify aperture and surface radiation problems.

### 1.2 System-Level Perspective

In antenna engineering, the radiation integrals are applied whenever the current distribution on an antenna structure is known or approximated. For wire antennas, the current is approximated as a sinusoidal or triangular distribution along the wire, and the vector potential integral reduces to a one-dimensional line integral. For aperture antennas, the field equivalence principle replaces the aperture fields with equivalent surface currents, and the potentials are integrated over the aperture plane. The far-field forms of these integrals — the core of practical antenna pattern computation — are the foundation for computing radiation patterns, directivity, and polarization of virtually all antenna types.

> **[Key Insight]** The auxiliary potential approach transforms a three-dimensional vector wave equation into a set of scalar wave equations, one per Cartesian component. The solution is then obtained by convolution of the source distribution with the free-space Green's function.

---

## 2. Formal Definitions and Models

### 2.1 Maxwell's Equations in the Presence of Sources

In a homogeneous, isotropic, linear medium with permittivity $\epsilon$, permeability $\mu$, and conductivity $\sigma = 0$ (lossless), the time-harmonic Maxwell's equations with electric current density $\mathbf{J}$ and magnetic current density $\mathbf{M}$ (fictitious) are:

$$
\nabla \times \mathbf{E} = -j\omega \mu \mathbf{H} - \mathbf{M}
$$

$$
\nabla \times \mathbf{H} = j\omega \epsilon \mathbf{E} + \mathbf{J}
$$

$$
\nabla \cdot \mathbf{D} = \rho_e
$$

$$
\nabla \cdot \mathbf{B} = \rho_m
$$

where $\rho_e$ and $\rho_m$ are the electric and (fictitious) magnetic charge densities, related to the current densities by the continuity equations:

$$
\nabla \cdot \mathbf{J} = -j\omega \rho_e
$$

$$
\nabla \cdot \mathbf{M} = -j\omega \rho_m
$$

An $e^{j\omega t}$ time dependence is assumed throughout and suppressed.

### 2.2 The Vector Potential $\mathbf{A}$ for an Electric Current Source $\mathbf{J}$

The magnetic vector potential $\mathbf{A}$ is defined such that the magnetic flux density $\mathbf{B}$ is solenoidal:

$$
\mathbf{B} = \nabla \times \mathbf{A}
$$

Since $\mathbf{B} = \mu \mathbf{H}$, this gives $\mathbf{H} = \frac{1}{\mu} \nabla \times \mathbf{A}$. Substituting into the Maxwell-Faraday equation:

$$
\nabla \times \mathbf{E} = -j\omega \mu \mathbf{H} - \mathbf{M} = -j\omega (\nabla \times \mathbf{A}) - \mathbf{M}
$$

Rearranging:

$$
\nabla \times (\mathbf{E} + j\omega \mathbf{A}) = -\mathbf{M}
$$

When $\mathbf{M} = 0$ (no magnetic currents), the curl of $(\mathbf{E} + j\omega \mathbf{A})$ is zero, so it can be expressed as the gradient of a scalar potential $\Phi_e$:

$$
\mathbf{E} + j\omega \mathbf{A} = -\nabla \Phi_e
$$

Thus:

$$
\mathbf{E} = -j\omega \mathbf{A} - \nabla \Phi_e
$$

Applying the Lorentz gauge condition:

$$
\nabla \cdot \mathbf{A} = -j\omega \mu \epsilon \Phi_e
$$

the electric field becomes:

$$
\mathbf{E} = -j\omega \mathbf{A} - \frac{j}{\omega \mu \epsilon} \nabla (\nabla \cdot \mathbf{A})
$$

The wave equation for $\mathbf{A}$ derives from the Ampere-Maxwell law:

$$
\nabla \times \mathbf{H} = \nabla \times \left( \frac{1}{\mu} \nabla \times \mathbf{A} \right) = \frac{1}{\mu} (\nabla (\nabla \cdot \mathbf{A}) - \nabla^2 \mathbf{A}) = j\omega \epsilon \mathbf{E} + \mathbf{J}
$$

Substituting $\mathbf{E}$ and applying the Lorentz gauge gives the inhomogeneous vector Helmholtz equation:

$$
\nabla^2 \mathbf{A} + k^2 \mathbf{A} = -\mu \mathbf{J}
$$

where $k = \omega \sqrt{\mu \epsilon}$ is the wavenumber.

### 2.3 The Vector Potential $\mathbf{F}$ for a Magnetic Current Source $\mathbf{M}$

By duality, the electric vector potential $\mathbf{F}$ is defined for magnetic current sources $\mathbf{M}$:

$$
\mathbf{D} = -\nabla \times \mathbf{F}
$$

Since $\mathbf{D} = \epsilon \mathbf{E}$, this gives $\mathbf{E} = -\frac{1}{\epsilon} \nabla \times \mathbf{F}$. Following the same procedure as for $\mathbf{A}$, the fields are:

$$
\mathbf{H} = -j\omega \mathbf{F} - \frac{j}{\omega \mu \epsilon} \nabla (\nabla \cdot \mathbf{F})
$$

and $\mathbf{F}$ satisfies:

$$
\nabla^2 \mathbf{F} + k^2 \mathbf{F} = -\epsilon \mathbf{M}
$$

### 2.4 Total Fields from Combined Sources

When both electric and magnetic current sources are present, the total fields are the superposition of the contributions from $\mathbf{A}$ and $\mathbf{F}$:

**From $\mathbf{A}$ only (electric sources $\mathbf{J}$):**

$$
\mathbf{E}_A = -j\omega \mathbf{A} - \frac{j}{\omega \mu \epsilon} \nabla (\nabla \cdot \mathbf{A})
$$

$$
\mathbf{H}_A = \frac{1}{\mu} \nabla \times \mathbf{A}
$$

**From $\mathbf{F}$ only (magnetic sources $\mathbf{M}$):**

$$
\mathbf{H}_F = -j\omega \mathbf{F} - \frac{j}{\omega \mu \epsilon} \nabla (\nabla \cdot \mathbf{F})
$$

$$
\mathbf{E}_F = -\frac{1}{\epsilon} \nabla \times \mathbf{F}
$$

**Total fields:**

$$
\mathbf{E} = \mathbf{E}_A + \mathbf{E}_F = -j\omega \mathbf{A} - \frac{j}{\omega \mu \epsilon} \nabla (\nabla \cdot \mathbf{A}) - \frac{1}{\epsilon} \nabla \times \mathbf{F}
$$

$$
\mathbf{H} = \mathbf{H}_A + \mathbf{H}_F = \frac{1}{\mu} \nabla \times \mathbf{A} - j\omega \mathbf{F} - \frac{j}{\omega \mu \epsilon} \nabla (\nabla \cdot \mathbf{F})
$$

### 2.5 Solution of the Inhomogeneous Vector Potential Wave Equation

The inhomogeneous Helmholtz equation:

$$
\nabla^2 \mathbf{A} + k^2 \mathbf{A} = -\mu \mathbf{J}
$$

is solved using the free-space Green's function $G(\mathbf{r}, \mathbf{r}')$, which satisfies:

$$
\nabla^2 G + k^2 G = -\delta(\mathbf{r} - \mathbf{r}')
$$

The solution is:

$$
G(\mathbf{r}, \mathbf{r}') = \frac{e^{-jk|\mathbf{r} - \mathbf{r}'|}}{4\pi |\mathbf{r} - \mathbf{r}'|}
$$

The vector potential $\mathbf{A}$ is obtained by convolution of the source $\mathbf{J}$ with the Green's function:

$$
\mathbf{A}(\mathbf{r}) = \mu \iiint_V \mathbf{J}(\mathbf{r}') \frac{e^{-jk|\mathbf{r} - \mathbf{r}'|}}{4\pi |\mathbf{r} - \mathbf{r}'|} \, dv'
$$

Similarly, for $\mathbf{F}$:

$$
\mathbf{F}(\mathbf{r}) = \epsilon \iiint_V \mathbf{M}(\mathbf{r}') \frac{e^{-jk|\mathbf{r} - \mathbf{r}'|}}{4\pi |\mathbf{r} - \mathbf{r}'|} \, dv'
$$

For surface currents $\mathbf{J}_s$ and $\mathbf{M}_s$, the volume integrals reduce to surface integrals:

$$
\mathbf{A}(\mathbf{r}) = \mu \iint_S \mathbf{J}_s(\mathbf{r}') \frac{e^{-jk|\mathbf{r} - \mathbf{r}'|}}{4\pi |\mathbf{r} - \mathbf{r}'|} \, ds'
$$

$$
\mathbf{F}(\mathbf{r}) = \epsilon \iint_S \mathbf{M}_s(\mathbf{r}') \frac{e^{-jk|\mathbf{r} - \mathbf{r}'|}}{4\pi |\mathbf{r} - \mathbf{r}'|} \, ds'
$$

### 2.6 Far-Field Radiation

In the far-field region, the distance from the source to the observation point is much larger than both the source dimensions and the wavelength ($r \gg 2D^2/\lambda$, where $D$ is the largest source dimension). The following approximations apply:

**Distance approximation in the phase term:**

$$
|\mathbf{r} - \mathbf{r}'| \approx r - \mathbf{r}' \cdot \hat{\mathbf{r}} = r - (x' \sin\theta \cos\phi + y' \sin\theta \sin\phi + z' \cos\theta)
$$

**Distance approximation in the amplitude term:**

$$
\frac{1}{|\mathbf{r} - \mathbf{r}'|} \approx \frac{1}{r}
$$

The far-field vector potential becomes:

$$
\mathbf{A}(\mathbf{r}) \approx \mu \frac{e^{-jkr}}{4\pi r} \iiint_V \mathbf{J}(\mathbf{r}') e^{jk \mathbf{r}' \cdot \hat{\mathbf{r}}} \, dv'
$$

$$
\mathbf{F}(\mathbf{r}) \approx \epsilon \frac{e^{-jkr}}{4\pi r} \iiint_V \mathbf{M}(\mathbf{r}') e^{jk \mathbf{r}' \cdot \hat{\mathbf{r}}} \, dv'
$$

**Far-field simplification of fields:**

In the far-field, only the transverse (radial) components of the potentials contribute to the radiated fields. The fields simplify to:

$$
\mathbf{E}_A \approx -j\omega \mathbf{A}_\theta \hat{\boldsymbol{\theta}} - j\omega \mathbf{A}_\phi \hat{\boldsymbol{\phi}}
$$

$$
\mathbf{H}_A \approx \frac{1}{\eta} \hat{\mathbf{r}} \times \mathbf{E}_A
$$

$$
\mathbf{H}_F \approx -j\omega \mathbf{F}_\theta \hat{\boldsymbol{\theta}} - j\omega \mathbf{F}_\phi \hat{\boldsymbol{\phi}}
$$

$$
\mathbf{E}_F \approx -\eta \, \hat{\mathbf{r}} \times \mathbf{H}_F
$$

where $\eta = \sqrt{\mu/\epsilon}$ is the intrinsic impedance of the medium.

> **[Key Insight]** In the far-field, the radiated field is purely transverse (TEM) — there is no radial component of $\mathbf{E}$ or $\mathbf{H}$. The fields are related by the free-space impedance $\eta$, and the power density decays as $1/r^2$.

### 2.7 Duality Theorem

Duality states that if a set of field equations is solved for one type of source, the solution for the dual source is obtained by interchanging quantities according to the following mapping:

| Electric Quantity | Dual Magnetic Quantity |
|:---|:---|
| $\mathbf{E}$ | $\mathbf{H}$ |
| $\mathbf{H}$ | $-\mathbf{E}$ |
| $\mathbf{J}$ | $\mathbf{M}$ |
| $\mathbf{M}$ | $-\mathbf{J}$ |
| $\epsilon$ | $\mu$ |
| $\mu$ | $\epsilon$ |
| $\eta$ | $1/\eta$ |
| $\mathbf{A}$ | $\mathbf{F}$ |
| $\mathbf{F}$ | $-\mathbf{A}$ |

This theorem allows immediate translation of known solutions. For example, the far-field pattern of a magnetic dipole (small loop antenna) is the dual of the far-field pattern of an electric dipole (short dipole antenna).

### 2.8 Reciprocity and Reaction Theorems

**Reciprocity Theorem (Lorentz form):**

If $\mathbf{E}_1$, $\mathbf{H}_1$ are the fields produced by sources $\mathbf{J}_1$, $\mathbf{M}_1$ in a linear isotropic medium, and $\mathbf{E}_2$, $\mathbf{H}_2$ are the fields produced by $\mathbf{J}_2$, $\mathbf{M}_2$ in the same medium, then:

$$
\iiint_V (\mathbf{J}_1 \cdot \mathbf{E}_2 - \mathbf{M}_1 \cdot \mathbf{H}_2) \, dv = \iiint_V (\mathbf{J}_2 \cdot \mathbf{E}_1 - \mathbf{M}_2 \cdot \mathbf{H}_1) \, dv
$$

A special case for two antennas: The receive pattern of an antenna is identical to its transmit pattern. Equivalently, the mutual impedance $Z_{12}$ between two antennas satisfies $Z_{12} = Z_{21}$.

**Reaction Theorem:**

The reaction of field $\mathbf{a}$ on source $\mathbf{b}$ is defined as:

$$
\langle \mathbf{a}, \mathbf{b} \rangle = \iiint_V (\mathbf{E}_a \cdot \mathbf{J}_b - \mathbf{H}_a \cdot \mathbf{M}_b) \, dv
$$

Reciprocity then states $\langle 1, 2 \rangle = \langle 2, 1 \rangle$.

---

## 3. Key Parameters and Constraints

| Parameter | Symbol | Definition/Form | Units | Role |
|:---|:---|:---|:---|:---|
| Wavenumber | $k$ | $2\pi/\lambda$ | rad/m | Determines phase progression and oscillation scale |
| Intrinsic impedance | $\eta$ | $\sqrt{\mu/\epsilon}$ | $\Omega$ | Ratio of transverse $\mathbf{E}$ to $\mathbf{H}$ in far-field |
| Free-space Green's function | $G$ | $e^{-jkR}/(4\pi R)$ | m$^{-1}$ | Point-source response used in potential integrals |
| Far-field distance | $R_{ff}$ | $2D^2/\lambda$ | m | Minimum distance for far-field approximations to hold |
| Magnetic vector potential | $\mathbf{A}$ | $\mu \iiint \mathbf{J} G \, dv$ | Wb/m | Intermediate quantity from electric sources |
| Electric vector potential | $\mathbf{F}$ | $\epsilon \iiint \mathbf{M} G \, dv$ | C/m | Intermediate quantity from magnetic sources |

---

## 4. Step-by-Step Mechanism: Computing Radiated Fields from a Known Current Distribution

The following procedure is used to compute the radiated electric and magnetic fields from an arbitrary current distribution:

1. **Identify the source currents:** Determine $\mathbf{J}(\mathbf{r}')$ and/or $\mathbf{M}(\mathbf{r}')$ over the source volume or surface.
2. **Choose the observation point:** Define $\mathbf{r}$ in the region of interest (near-field, Fresnel, or far-field).
3. **Compute the vector potentials:**
   - Evaluate $\mathbf{A}(\mathbf{r}) = \mu \iiint \mathbf{J}(\mathbf{r}') G(\mathbf{r}, \mathbf{r}') \, dv'$
   - Evaluate $\mathbf{F}(\mathbf{r}) = \epsilon \iiint \mathbf{M}(\mathbf{r}') G(\mathbf{r}, \mathbf{r}') \, dv'$
4. **If far-field, apply approximations:**
   - Phase: $|\mathbf{r} - \mathbf{r}'| \approx r - \mathbf{r}' \cdot \hat{\mathbf{r}}$
   - Amplitude: $1/|\mathbf{r} - \mathbf{r}'| \approx 1/r$
   - Extract the $\theta$ and $\phi$ components of the potentials.
5. **Derive the fields:**
   - $\mathbf{E} = -j\omega \mathbf{A} - \frac{j}{\omega \mu \epsilon} \nabla (\nabla \cdot \mathbf{A}) - \frac{1}{\epsilon} \nabla \times \mathbf{F}$
   - $\mathbf{H} = \frac{1}{\mu} \nabla \times \mathbf{A} - j\omega \mathbf{F} - \frac{j}{\omega \mu \epsilon} \nabla (\nabla \cdot \mathbf{F})$
6. **Simplify in far-field:** Use the transverse approximations with $\mathbf{E} \perp \mathbf{H} \perp \hat{\mathbf{r}}$.

---

## 5. Connections and Cross-References

- **Section 2 (Fundamental Parameters):** Directivity, gain, and radiation pattern are computed from the far-field $\mathbf{E}$ and $\mathbf{H}$ derived via the radiation integrals.
- **Section 4 (Linear Wire Antennas):** The current distribution $\mathbf{J}$ on wire antennas is approximated, then integrated to obtain $\mathbf{A}$ and the radiated fields.
- **Section 5 (Loop Antennas):** Loop antennas use the same $\mathbf{A}$ formulation with the current flowing along a closed path.
- **Section 12 (Aperture Antennas):** The equivalence principle introduces equivalent $\mathbf{M}$ sources over the aperture, requiring the $\mathbf{F}$ potential.
- **Section 8 (Integral Equations and Moment Method):** Numerical solutions use these integral formulations as the kernel of the method of moments.

---

## Solved Exercises

### Exercise 1: Vector Potential of an Infinitesimal Electric Dipole at the Origin

**Problem:** An infinitesimal electric dipole of length $dl$ is located at the origin, oriented along the $z$-axis, carrying a constant current $I_0$. Compute the magnetic vector potential $\mathbf{A}$ everywhere in space.

**Solution:**

Step 1: Define the current density.
The current density for a Hertzian dipole at the origin oriented along $z$ is:

$$
\mathbf{J}(\mathbf{r}') = I_0 \, dl \, \delta(\mathbf{r}') \, \hat{\mathbf{z}}
$$

where $\delta(\mathbf{r}')$ is the three-dimensional Dirac delta function.

Step 2: Apply the volume integral for $\mathbf{A}$.

$$
\mathbf{A}(\mathbf{r}) = \mu \iiint_{V'} \mathbf{J}(\mathbf{r}') G(\mathbf{r}, \mathbf{r}') \, dv'
$$

$$
\mathbf{A}(\mathbf{r}) = \mu \iiint_{V'} I_0 \, dl \, \delta(\mathbf{r}') \frac{e^{-jk|\mathbf{r} - \mathbf{r}'|}}{4\pi |\mathbf{r} - \mathbf{r}'|} \, dv' \, \hat{\mathbf{z}}
$$

The delta function sifts out the value at $\mathbf{r}' = \mathbf{0}$:

$$
\mathbf{A}(\mathbf{r}) = \mu I_0 \, dl \frac{e^{-jk|\mathbf{r}|}}{4\pi |\mathbf{r}|} \hat{\mathbf{z}}
$$

Since $|\mathbf{r}| = r$, the result is:

$$
\mathbf{A}(\mathbf{r}) = \mu I_0 \, dl \frac{e^{-jkr}}{4\pi r} \hat{\mathbf{z}}
$$

Step 3: Express in spherical components.
In spherical coordinates, $\hat{\mathbf{z}} = \cos\theta \, \hat{\mathbf{r}} - \sin\theta \, \hat{\boldsymbol{\theta}}$. Therefore:

$$
A_r = A_z \cos\theta = \mu I_0 \, dl \frac{e^{-jkr}}{4\pi r} \cos\theta
$$

$$
A_\theta = -A_z \sin\theta = -\mu I_0 \, dl \frac{e^{-jkr}}{4\pi r} \sin\theta
$$

$$
A_\phi = 0
$$

The vector potential has both radial and $\theta$ components. In the far-field, only $A_\theta$ contributes to the radiated field.

---

### Exercise 2: Far-Field of an Infinitesimal Dipole from the Vector Potential

**Problem:** Using the vector potential $\mathbf{A}$ from Exercise 1, compute the far-field $\mathbf{E}$ and $\mathbf{H}$ of the infinitesimal dipole.

**Solution:**

Step 1: Far-field simplification.
In the far-field ($kr \gg 1$), the radial component $A_r$ does not contribute to the radiated power. The transverse component $A_\theta$ determines the fields:

$$
\mathbf{E}_A \approx -j\omega \mathbf{A}_\perp
$$

where $\mathbf{A}_\perp = A_\theta \hat{\boldsymbol{\theta}} = -\mu I_0 \, dl \frac{e^{-jkr}}{4\pi r} \sin\theta \, \hat{\boldsymbol{\theta}}$.

Step 2: Compute the electric field.

$$
\mathbf{E} = -j\omega \left( -\mu I_0 \, dl \frac{e^{-jkr}}{4\pi r} \sin\theta \right) \hat{\boldsymbol{\theta}}
$$

$$
\mathbf{E} = j\omega\mu I_0 \, dl \frac{e^{-jkr}}{4\pi r} \sin\theta \, \hat{\boldsymbol{\theta}}
$$

Since $k = \omega \sqrt{\mu\epsilon} = \omega \mu / \eta$ (because $\eta = \sqrt{\mu/\epsilon} = \mu / \sqrt{\mu\epsilon} = \mu\omega/k$), we have $\omega\mu = k\eta$:

$$
\mathbf{E} = j \eta k I_0 \, dl \frac{e^{-jkr}}{4\pi r} \sin\theta \, \hat{\boldsymbol{\theta}}
$$

Step 3: Compute the magnetic field.
In the far-field, $\mathbf{H} = \frac{1}{\eta} \hat{\mathbf{r}} \times \mathbf{E}$:

$$
\mathbf{H} = \frac{1}{\eta} (j \eta k I_0 \, dl \frac{e^{-jkr}}{4\pi r} \sin\theta) (\hat{\mathbf{r}} \times \hat{\boldsymbol{\theta}})
$$

Since $\hat{\mathbf{r}} \times \hat{\boldsymbol{\theta}} = \hat{\boldsymbol{\phi}}$:

$$
\mathbf{H} = j k I_0 \, dl \frac{e^{-jkr}}{4\pi r} \sin\theta \, \hat{\boldsymbol{\phi}}
$$

The radiated fields are purely transverse, with $\mathbf{E}$ along $\hat{\boldsymbol{\theta}}$ and $\mathbf{H}$ along $\hat{\boldsymbol{\phi}}$, confirming the TEM nature of the far-field radiation.

---

### Exercise 3: Verification of the Wave Equation for $\mathbf{A}$

**Problem:** Show that the expression $\mathbf{A}(\mathbf{r}) = \mu \iiint \mathbf{J}(\mathbf{r}') \frac{e^{-jk|\mathbf{r} - \mathbf{r}'|}}{4\pi |\mathbf{r} - \mathbf{r}'|} dv'$ satisfies the inhomogeneous Helmholtz equation $\nabla^2 \mathbf{A} + k^2 \mathbf{A} = -\mu \mathbf{J}$.

**Solution:**

Step 1: Recognize that the operator $\nabla^2 + k^2$ acts only on the observation coordinate $\mathbf{r}$, not on $\mathbf{r}'$. Thus:

$$
(\nabla^2 + k^2) \mathbf{A}(\mathbf{r}) = \mu \iiint \mathbf{J}(\mathbf{r}') (\nabla^2 + k^2) G(\mathbf{r}, \mathbf{r}') \, dv'
$$

where $G(\mathbf{r}, \mathbf{r}') = e^{-jkR} / (4\pi R)$ and $R = |\mathbf{r} - \mathbf{r}'|$.

Step 2: Use the property of the Green's function.
The free-space Green's function satisfies:

$$
(\nabla^2 + k^2) G(\mathbf{r}, \mathbf{r}') = -\delta(\mathbf{r} - \mathbf{r}')
$$

Step 3: Evaluate the integral.

$$
(\nabla^2 + k^2) \mathbf{A}(\mathbf{r}) = \mu \iiint \mathbf{J}(\mathbf{r}') [-\delta(\mathbf{r} - \mathbf{r}')] \, dv'
$$

$$
(\nabla^2 + k^2) \mathbf{A}(\mathbf{r}) = -\mu \mathbf{J}(\mathbf{r})
$$

This verifies the inhomogeneous Helmholtz equation. The result holds for any point $\mathbf{r}$ inside the source region.

---

### Exercise 4: Vector Potential of a Uniform Line Current

**Problem:** A uniform electric current $I_0$ flows along the $z$-axis from $z = -L/2$ to $z = L/2$. Find the far-field vector potential $\mathbf{A}$.

**Solution:**

Step 1: Define the current density.
For a thin wire along the $z$-axis:

$$
\mathbf{J}(\mathbf{r}') = I_0 \delta(x') \delta(y') \hat{\mathbf{z}}, \quad -\frac{L}{2} \leq z' \leq \frac{L}{2}
$$

Step 2: Express the vector potential integral.

$$
\mathbf{A}(\mathbf{r}) = \mu \iiint I_0 \delta(x') \delta(y') \frac{e^{-jk|\mathbf{r} - \mathbf{r}'|}}{4\pi |\mathbf{r} - \mathbf{r}'|} \, dx' dy' dz' \, \hat{\mathbf{z}}
$$

The delta functions reduce the volume integral to a line integral along $z'$:

$$
\mathbf{A}(\mathbf{r}) = \mu I_0 \int_{-L/2}^{L/2} \frac{e^{-jk|\mathbf{r} - z'\hat{\mathbf{z}}|}}{4\pi |\mathbf{r} - z'\hat{\mathbf{z}}|} \, dz' \, \hat{\mathbf{z}}
$$

Step 3: Apply the far-field approximation.
For $r \gg L$ and $r \gg \lambda$:

$$
|\mathbf{r} - z'\hat{\mathbf{z}}| \approx r - z' \cos\theta
$$

$$
\frac{1}{|\mathbf{r} - z'\hat{\mathbf{z}}|} \approx \frac{1}{r}
$$

Thus:

$$
\mathbf{A}(\mathbf{r}) \approx \mu I_0 \frac{e^{-jkr}}{4\pi r} \int_{-L/2}^{L/2} e^{jkz' \cos\theta} \, dz' \, \hat{\mathbf{z}}
$$

Step 4: Evaluate the integral.

$$
\int_{-L/2}^{L/2} e^{jkz' \cos\theta} \, dz' = \left[ \frac{e^{jkz' \cos\theta}}{jk\cos\theta} \right]_{-L/2}^{L/2}
$$

$$
= \frac{1}{jk\cos\theta} (e^{jk(L/2)\cos\theta} - e^{-jk(L/2)\cos\theta})
$$

$$
= \frac{2}{k\cos\theta} \sin\left( \frac{kL}{2} \cos\theta \right) = L \frac{\sin\left( \frac{kL}{2} \cos\theta \right)}{\frac{kL}{2} \cos\theta}
$$

Using the sinc function, $\text{sinc}(x) = \sin(x)/x$:

$$
\mathbf{A}(\mathbf{r}) = \mu I_0 L \frac{e^{-jkr}}{4\pi r} \, \text{sinc}\left( \frac{kL}{2} \cos\theta \right) \hat{\mathbf{z}}
$$

where the argument of sinc is $\frac{kL}{2} \cos\theta = \frac{\pi L}{\lambda} \cos\theta$.

Step 5: Extract the transverse component.
In spherical coordinates, $A_\theta = -A_z \sin\theta$:

$$
A_\theta = -\mu I_0 L \frac{e^{-jkr}}{4\pi r} \sin\theta \, \text{sinc}\left( \frac{\pi L}{\lambda} \cos\theta \right)
$$

This $A_\theta$ component, when multiplied by $-j\omega$, gives the far-field $\mathbf{E}_\theta$, showing that the radiation pattern is modulated by the sinc factor due to the finite wire length.

---

### Exercise 5: Duality — Electric Dipole to Magnetic Dipole (Small Loop)

**Problem:** Use duality to find the far-field expressions for a small magnetic dipole (loop antenna) from the known far-field of an infinitesimal electric dipole.

**Solution:**

Step 1: Recall the far-field of an infinitesimal electric dipole.
From Exercise 2, for an electric dipole of moment $I_0 \, dl$:

$$
\mathbf{E}_e = j \eta k I_0 \, dl \frac{e^{-jkr}}{4\pi r} \sin\theta \, \hat{\boldsymbol{\theta}}
$$

$$
\mathbf{H}_e = j k I_0 \, dl \frac{e^{-jkr}}{4\pi r} \sin\theta \, \hat{\boldsymbol{\phi}}
$$

Step 2: Apply duality mapping.
The dual of an electric dipole is a magnetic dipole. The mapping exchanges:
- $\mathbf{E} \to \mathbf{H}$
- $\mathbf{H} \to -\mathbf{E}$
- $I_0 \, dl$ (electric dipole moment) $\to M_0 \, dl$ (magnetic dipole moment)

Under duality:

$$
\mathbf{H}_m = j \eta k M_0 \, dl \frac{e^{-jkr}}{4\pi r} \sin\theta \, \hat{\boldsymbol{\theta}}
$$

$$
-\mathbf{E}_m = j k M_0 \, dl \frac{e^{-jkr}}{4\pi r} \sin\theta \, \hat{\boldsymbol{\phi}}
$$

Step 3: Rearrange for $\mathbf{E}_m$.

$$
\mathbf{E}_m = -j k M_0 \, dl \frac{e^{-jkr}}{4\pi r} \sin\theta \, \hat{\boldsymbol{\phi}}
$$

Step 4: Express the magnetic dipole moment in terms of loop parameters.
For a small loop of area $S$ carrying current $I_0$, the magnetic dipole moment is:

$$
M_0 \, dl \longleftrightarrow I_0 S \quad \text{(by equivalence of dipole moments)}
$$

But the duality mapping relates the electric and magnetic dipole moments. More precisely, the magnetic dipole moment $p_m$ relates to the electric dipole moment $p_e$ through $p_e \to p_m/\eta$. For a small loop of area $S$, the equivalent magnetic dipole strength is $I_0 S$, and $k I_0 S = \eta M_0 dl$ from the dual form. The final fields for a small loop are:

$$
\mathbf{E}_{\text{loop}} = \eta k^2 I_0 S \frac{e^{-jkr}}{4\pi r} \sin\theta \, \hat{\boldsymbol{\phi}}
$$

$$
\mathbf{H}_{\text{loop}} = -k^2 I_0 S \frac{e^{-jkr}}{4\pi r} \sin\theta \, \hat{\boldsymbol{\theta}}
$$

Notice that $\mathbf{E}$ is along $\hat{\boldsymbol{\phi}}$ (azimuthal polarization) for the loop, whereas it was along $\hat{\boldsymbol{\theta}}$ for the electric dipole — a direct consequence of duality.

---

### Exercise 6: Far-Field Approximation Error Analysis

**Problem:** A $z$-directed infinitesimal dipole is at the origin. Compare the exact expression for $A_z$ with the far-field approximation at a distance $r = \lambda$ and angle $\theta = 45^\circ$. Compute the percentage error in the phase.

**Solution:**

Step 1: Exact expression.
The exact vector potential at $(\lambda, 45^\circ, 0^\circ)$ for a dipole at the origin is:

$$
A_z^{\text{exact}} = \mu I_0 \, dl \frac{e^{-jk\lambda}}{4\pi \lambda}
$$

Since $k\lambda = 2\pi$:

$$
A_z^{\text{exact}} = \mu I_0 \, dl \frac{e^{-j2\pi}}{4\pi \lambda} = \mu I_0 \, dl \frac{1}{4\pi \lambda}
$$

The phase is exactly $2\pi$ radians (or $0$ mod $2\pi$).

Step 2: Far-field approximation.
The far-field expression is identical because the dipole is a point source at the origin — there is no spatial extent, so the far-field approximation is exact for the infinitesimal dipole. To demonstrate the approximation, consider instead a dipole of finite length $L = \lambda/2$ centered at the origin along $z$, with observation point at $r = \lambda$, $\theta = 45^\circ$.

For a finite dipole of length $L$, the exact phase is $k|\mathbf{r} - \mathbf{r}'|$, while the far-field approximates it as $kr - k\mathbf{r}' \cdot \hat{\mathbf{r}}$.

Exact phase at the dipole tip $z' = L/2 = \lambda/4$:

$$
R = |\mathbf{r} - (\lambda/4)\hat{\mathbf{z}}| = \sqrt{\lambda^2 + (\lambda/4)^2 - 2\lambda(\lambda/4)\cos45^\circ}
$$

$$
R = \lambda \sqrt{1 + \frac{1}{16} - \frac{1}{2} \times \frac{\sqrt{2}}{2}} = \lambda \sqrt{1 + 0.0625 - 0.3536}
$$

$$
R = \lambda \sqrt{0.7089} = 0.842\lambda
$$

Phase error = $kR - kr + k\mathbf{r}' \cdot \hat{\mathbf{r}}$:

$$
kR = 2\pi \times 0.842 = 5.290 \text{ rad}
$$

$$
kr = 2\pi \times 1 = 6.283 \text{ rad}
$$

$$
k\mathbf{r}' \cdot \hat{\mathbf{r}} = k \frac{\lambda}{4} \cos45^\circ = 2\pi \times \frac{1}{4} \times 0.707 = 1.111 \text{ rad}
$$

Far-field phase estimate: $kr - k\mathbf{r}' \cdot \hat{\mathbf{r}} = 6.283 - 1.111 = 5.172$ rad.

Step 3: Compute the phase error.

$$
\Delta\phi = |5.290 - 5.172| = 0.118 \text{ rad}
$$

Step 4: Interpret the result.
The phase error is $0.118$ rad, which is $6.76^\circ$. The standard far-field criterion requires phase error $< \pi/8 = 0.393$ rad ($22.5^\circ$) across the source. At $r = \lambda$, the error of $0.118$ rad is well within this limit, confirming that $r = \lambda$ is sufficient for the far-field for a source of size $\lambda/2$. However, the formal far-field distance $2D^2/\lambda = 2(\lambda/2)^2/\lambda = \lambda/2$, so $r = \lambda$ satisfies $r \gg \lambda/2$, confirming the approximation is valid.

> **[Supplementary]** The standard far-field criterion of $r \geq 2D^2/\lambda$ ensures that the maximum phase error across the aperture is $\pi/8$ ($22.5^\circ$) or less. This is the accepted engineering threshold for pattern measurements.

---

### Exercise 7: Reciprocity — Mutual Impedance Between Two Dipoles

**Problem:** Two identical infinitesimal dipoles of length $dl$ are spaced $d = \lambda/4$ apart along the $x$-axis, both oriented along $z$. Use the reaction theorem to compute the mutual impedance $Z_{12}$.

**Solution:**

Step 1: Set up the geometry.
Dipole 1 is at $\mathbf{r}_1 = (0, 0, 0)$, Dipole 2 is at $\mathbf{r}_2 = (\lambda/4, 0, 0)$. Both are $z$-directed.

Step 2: Recall the reaction theorem definition.
The mutual impedance between two antennas is:

$$
Z_{12} = -\frac{1}{I_1 I_2} \iiint_{V_2} \mathbf{J}_2 \cdot \mathbf{E}_1 \, dv
$$

where $\mathbf{E}_1$ is the field produced by antenna 1 at the location of antenna 2, and $I_1$, $I_2$ are the input currents.

Step 3: Compute $\mathbf{E}_1$ at the location of dipole 2.
From Exercise 2, the field of an infinitesimal dipole at the origin is:

$$
\mathbf{E}_1 = j \eta k I_1 \, dl \frac{e^{-jkr}}{4\pi r} \sin\theta \, \hat{\boldsymbol{\theta}}
$$

At the location of dipole 2: $\mathbf{r}_2 = (\lambda/4, 0, 0)$, so $r = \lambda/4$, $\theta = 90^\circ$ (equatorial plane), $\phi = 0^\circ$.

$$
\mathbf{E}_1(\mathbf{r}_2) = j \eta k I_1 \, dl \frac{e^{-jk(\lambda/4)}}{4\pi (\lambda/4)} \sin(90^\circ) \, \hat{\boldsymbol{\theta}}
$$

At $\phi = 0^\circ$ in the $x$-$z$ plane, $\hat{\boldsymbol{\theta}} = \hat{\mathbf{z}}$ for a point on the $x$-axis. Therefore:

$$
\mathbf{E}_1(\mathbf{r}_2) = j \eta k I_1 \, dl \frac{e^{-j\pi/2}}{\pi \lambda} \hat{\mathbf{z}}
$$

$$
\mathbf{E}_1(\mathbf{r}_2) = j \eta k I_1 \, dl \frac{-j}{\pi \lambda} \hat{\mathbf{z}} = \eta k I_1 \, dl \frac{1}{\pi \lambda} \hat{\mathbf{z}}
$$

Since $k = 2\pi/\lambda$:

$$
\mathbf{E}_1(\mathbf{r}_2) = \eta \frac{2\pi}{\lambda} I_1 \, dl \frac{1}{\pi \lambda} \hat{\mathbf{z}} = \frac{2\eta I_1 dl}{\lambda^2} \hat{\mathbf{z}}
$$

Step 4: Compute the mutual impedance.
The current density of dipole 2 is $\mathbf{J}_2 = I_2 \delta(\mathbf{r} - \mathbf{r}_2) \hat{\mathbf{z}}$. The volume integral becomes:

$$
\iiint_{V_2} \mathbf{J}_2 \cdot \mathbf{E}_1 \, dv = I_2 \int_{\text{dipole 2}} \mathbf{E}_1(\mathbf{r}_2) \cdot \hat{\mathbf{z}} \, dl = I_2 \frac{2\eta I_1 dl}{\lambda^2} \, dl
$$

Therefore:

$$
Z_{12} = -\frac{1}{I_1 I_2} \cdot I_2 \frac{2\eta I_1 (dl)^2}{\lambda^2} = -\frac{2\eta (dl)^2}{\lambda^2}
$$

The negative sign indicates that the induced voltage in antenna 2 due to antenna 1 has a specific phase relationship. For typical antennas, $Z_{12} = Z_{21}$ by reciprocity.

---

### Exercise 8: Fictitious Magnetic Currents in the Equivalence Principle

**Problem:** An aperture in a perfectly conducting ground plane has a tangential electric field $\mathbf{E}_a = E_0 \hat{\mathbf{x}}$ over a rectangular region $0 \leq x \leq a$, $0 \leq y \leq b$. Use the equivalence principle to determine the equivalent magnetic current $\mathbf{M}_s$ on the aperture and set up the integral for the radiated fields.

**Solution:**

Step 1: Apply the equivalence principle.
For an aperture in a perfect electric conductor (PEC), the tangential electric field in the aperture acts as an equivalent magnetic current:

$$
\mathbf{M}_s = -\hat{\mathbf{n}} \times \mathbf{E}_a
$$

where $\hat{\mathbf{n}}$ is the outward normal to the aperture. For the aperture in the $x$-$y$ plane radiating into the $z > 0$ half-space, $\hat{\mathbf{n}} = \hat{\mathbf{z}}$.

Step 2: Compute the equivalent magnetic current.

$$
\mathbf{M}_s = -\hat{\mathbf{z}} \times (E_0 \hat{\mathbf{x}}) = -E_0 (\hat{\mathbf{z}} \times \hat{\mathbf{x}}) = -E_0 \hat{\mathbf{y}}
$$

The equivalent magnetic current flows in the $-\hat{\mathbf{y}}$ direction across the aperture.

Step 3: Set up the electric vector potential.
Since only magnetic sources exist (the PEC backplane eliminates the need for electric currents in the equivalence formulation for $z > 0$), the radiated fields come entirely from $\mathbf{F}$:

$$
\mathbf{F}(\mathbf{r}) = \epsilon \iint_S \mathbf{M}_s(\mathbf{r}') \frac{e^{-jk|\mathbf{r} - \mathbf{r}'|}}{4\pi |\mathbf{r} - \mathbf{r}'|} \, ds'
$$

$$
\mathbf{F}(\mathbf{r}) = \epsilon (-E_0 \hat{\mathbf{y}}) \int_{x'=0}^{a} \int_{y'=0}^{b} \frac{e^{-jk|\mathbf{r} - \mathbf{r}'|}}{4\pi |\mathbf{r} - \mathbf{r}'|} \, dx' dy'
$$

Step 4: Far-field form.
In the far-field:

$$
\mathbf{F}(\mathbf{r}) \approx -\epsilon E_0 \frac{e^{-jkr}}{4\pi r} \iint_S e^{jk(x' \sin\theta \cos\phi + y' \sin\theta \sin\phi)} \, dx' dy' \, \hat{\mathbf{y}}
$$

Step 5: Express $\mathbf{F}$ in spherical components.
$\hat{\mathbf{y}} = \sin\theta \sin\phi \, \hat{\mathbf{r}} + \cos\theta \sin\phi \, \hat{\boldsymbol{\theta}} + \cos\phi \, \hat{\boldsymbol{\phi}}$. For far-field, only $\theta$ and $\phi$ components matter:

$$
F_\theta = \mathbf{F} \cdot \hat{\boldsymbol{\theta}} = -\epsilon E_0 \frac{e^{-jkr}}{4\pi r} \cos\theta \sin\phi \times (\text{aperture integral})
$$

$$
F_\phi = \mathbf{F} \cdot \hat{\boldsymbol{\phi}} = -\epsilon E_0 \frac{e^{-jkr}}{4\pi r} \cos\phi \times (\text{aperture integral})
$$

Step 6: Derive the far-field $\mathbf{E}$.
From $\mathbf{E}_F = -\frac{1}{\epsilon} \nabla \times \mathbf{F}$, in the far-field:

$$
\mathbf{E} \approx \eta \, (\mathbf{F}_\theta \hat{\boldsymbol{\phi}} - \mathbf{F}_\phi \hat{\boldsymbol{\theta}})
$$

This provides the complete far-field pattern of the rectangular aperture antenna, establishing the connection between the aperture field distribution (Section 12) and the radiation integrals of Section 3.

---

## Exam Tip: The Far-Field Approximation and Its Validity

A frequent exam question asks you to justify or apply the far-field approximation. Memorize these three conditions and their consequences:

1. **Phase approximation:** $|\mathbf{r} - \mathbf{r}'| \approx r - \mathbf{r}' \cdot \hat{\mathbf{r}}$ is valid when $r \gg D$, where $D$ is the largest source dimension. The maximum phase error is $kD^2/(2r)$. Setting this to $\pi/8$ gives the Rayleigh distance $r_{ff} = 2D^2/\lambda$.

2. **Amplitude approximation:** $1/|\mathbf{r} - \mathbf{r}'| \approx 1/r$ is valid when $r \gg D$. The amplitude error is typically negligible compared to the phase error.

3. **Transverse field condition:** In the far-field, the $\hat{\mathbf{r}}$ component of the vector potential does not contribute. Only the $\theta$ and $\phi$ components matter, and $\mathbf{E} \perp \mathbf{H} \perp \hat{\mathbf{r}}$.

**Common pitfalls:**
- Forgetting that the Lorentz gauge condition $\nabla \cdot \mathbf{A} = -j\omega\mu\epsilon\Phi_e$ is needed to derive the wave equation. Exam solutions sometimes omit this step and lose marks.
- Using the far-field form $e^{-jkr}/r$ without verifying that the observation point is indeed in the far-field zone. Always compute $2D^2/\lambda$ explicitly.
- Confusing the radiated fields from $\mathbf{A}$ and $\mathbf{F}$: $\mathbf{A}$ gives $\mathbf{H} = \nabla \times \mathbf{A}/\mu$, while $\mathbf{F}$ gives $\mathbf{E} = -\nabla \times \mathbf{F}/\epsilon$. The signs and the $\mu$ vs. $\epsilon$ factors are critical.
- Applying duality without adjusting the intrinsic impedance: when $\mathbf{E}$ and $\mathbf{H}$ are swapped, $\eta$ becomes $1/\eta$.

**Pattern recognition shortcut:** If an exam problem gives you a current distribution on a wire or aperture and asks for the radiation pattern, follow the steps: current $\to$ vector potential integral $\to$ far-field approximation $\to$ transverse components $\to$ $\mathbf{E}$ via $-j\omega\mathbf{A}_\perp$. This mechanical procedure works for virtually all antenna types.