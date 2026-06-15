# Linear Wire Antennas

Linear wire antennas are the simplest and most extensively studied class of antennas. They consist of thin, straight conductors carrying time-harmonic currents that radiate electromagnetic energy. Despite their geometric simplicity, linear wire antennas form the building blocks for more complex structures: arrays, Yagi-Uda antennas, log-periodic dipoles, and many other practical designs derive their behaviour from the fundamental current distributions and field patterns of single-wire radiators. This section covers the canonical cases — the infinitesimal dipole, the small dipole, and the finite-length dipole — along with region separation, ground-plane effects, and the computational tools used to analyse wire antennas.

---

## 1. Conceptual Foundation

### 1.1 Why Linear Wire Antennas

The linear wire antenna is the natural starting point for antenna theory for three reasons:

1. **Analytical tractability:** The current distribution on a thin wire can be approximated by a sinusoidal function, leading to closed-form expressions for the radiated fields, directivity, and input impedance.
2. **Practical ubiquity:** Half-wavelength dipoles, quarter-wavelength monopoles, and folded dipoles are among the most common antenna elements in commercial, military, and amateur radio systems.
3. **Pedagogical value:** Every concept introduced later — vector potentials, far-field approximations, impedance, mutual coupling — has a concrete manifestation in the wire antenna, making it the ideal vehicle for building physical intuition.

### 1.2 The Central Problem

Given a straight wire of length $L$ and radius $a$ (with $a \ll L$ and $a \ll \lambda$), carrying a known current distribution $I(z')$ along its axis, compute:

- The vector potential $\mathbf{A}$ at an observation point.
- The radiated electric and magnetic fields $\mathbf{E}$, $\mathbf{H}$.
- The radiation pattern, directivity, and input impedance.

The current distribution is the key unknown. For thin wires, the distribution is well approximated by a sinusoidal standing wave:

$$
I(z') = I_m \sin\left[k\left(\frac{L}{2} - |z'|\right)\right], \quad -\frac{L}{2} \leq z' \leq \frac{L}{2}
$$

where $I_m$ is the current maximum amplitude and $k = 2\pi/\lambda$ is the wavenumber.

> **[Key Insight]** The sinusoidal current approximation assumes the wire is perfectly conducting and infinitely thin. For finite-radius wires, the exact current distribution requires solving an integral equation (Pocklington's or Hallen's equation) using numerical methods such as the Method of Moments, covered in Section 8 of the mindmap.

---

## 2. Formal Definitions and Models

### 2.1 The Infinitesimal Dipole (Hertzian Dipole)

The infinitesimal dipole is the fundamental radiating element: a wire of length $dl \ll \lambda$ carrying a uniform current $I_0$. Despite being physically unrealisable (a finite current over an infinitesimal length would require infinite charge acceleration), it serves as the building block from which all wire antenna fields are derived via superposition.

**Current distribution:** Uniform, $I(z') = I_0$ over $-\frac{dl}{2} \leq z' \leq \frac{dl}{2}$.

**Magnetic vector potential:** For a $z$-oriented dipole centred at the origin:

$$
\mathbf{A} = A_z \hat{\mathbf{z}}, \quad A_z = \frac{\mu I_0 dl}{4\pi} \frac{e^{-jkr}}{r}
$$

**Radiated fields (spherical coordinates):**

$$
E_r = \eta \frac{I_0 dl \cos\theta}{2\pi r^2} \left(1 + \frac{1}{jkr}\right) e^{-jkr}
$$

$$
E_\theta = j\eta \frac{k I_0 dl \sin\theta}{4\pi r} \left[1 + \frac{1}{jkr} - \frac{1}{(kr)^2}\right] e^{-jkr}
$$

$$
H_\phi = j \frac{k I_0 dl \sin\theta}{4\pi r} \left[1 + \frac{1}{jkr}\right] e^{-jkr}
$$

**Far-field (Fraunhofer zone, $kr \gg 1$):**

$$
E_\theta \approx j\eta \frac{k I_0 dl \sin\theta}{4\pi r} e^{-jkr}, \quad H_\phi \approx \frac{E_\theta}{\eta}, \quad E_r \approx 0
$$

**Directivity:** $D_0 = 1.5$ (or $1.76$ dB).

**Radiation resistance:**

$$
R_r = 80\pi^2 \left(\frac{dl}{\lambda}\right)^2 = 20 k^2 (dl)^2 \quad \text{(in free space)}
$$

### 2.2 The Small Dipole

The small dipole has length $L \leq \lambda/10$ but is not infinitesimal. The current cannot be assumed uniform; instead, it varies linearly from a maximum at the centre to zero at the ends:

**Current distribution (triangular):**

$$
I(z') = I_0 \left(1 - \frac{2|z'|}{L}\right), \quad -\frac{L}{2} \leq z' \leq \frac{L}{2}
$$

**Vector potential (approximated using average current $I_{\text{av}} = I_0/2$):**

$$
A_z \approx \frac{\mu I_0 L}{8\pi} \frac{e^{-jkr}}{r} \quad \text{(far-field approximation)}
$$

**Far-field:**

$$
E_\theta \approx j\eta \frac{k I_0 L \sin\theta}{8\pi r} e^{-jkr}
$$

The small dipole has **half the radiation resistance** of an equivalent-length infinitesimal dipole with uniform current:

$$
R_r = 20\pi^2 \left(\frac{L}{\lambda}\right)^2
$$

**Directivity:** $D_0 = 1.5$ (same as infinitesimal dipole, because the pattern shape is identical).

> **[Key Insight]** The directivity of both the infinitesimal dipole and the small dipole is $1.5$ because the pattern function $\sin\theta$ is identical. The difference lies in the radiation resistance, which depends on the total current moment $\int I(z') dz'$.

### 2.3 Region Separation

The fields of any antenna are classified into three regions based on the distance $r$ from the source and the maximum dimension $D$ of the antenna.

**Table 1: Field Regions for Wire Antennas**

| Region | Criterion | Phase Front | Field Behaviour |
| :--- | :--- | :--- | :--- |
| Reactive Near-Field | $r < 0.62 \sqrt{D^3/\lambda}$ | Highly spherical, no $1/r$ term dominant | Reactive energy dominates; $E_r$ and $H_r$ components significant |
| Radiating Near-Field (Fresnel) | $0.62 \sqrt{D^3/\lambda} \leq r < 2D^2/\lambda$ | Spherical but locally planar | Angular field distribution depends on $r$; not fully formed pattern |
| Far-Field (Fraunhofer) | $r \geq 2D^2/\lambda$ | Planar over the antenna | $1/r$ dependence; pattern independent of $r$; $E \perp H \perp \hat{\mathbf{r}}$ |

For a dipole of length $L$, the maximum dimension is $D = L$. The far-field distance simplifies to:

$$
r_{\text{ff}} = \frac{2L^2}{\lambda}
$$

**Practical implication:** For a half-wavelength dipole ($L = \lambda/2$), $r_{\text{ff}} = \frac{2(\lambda/2)^2}{\lambda} = \lambda/2$. The far-field begins at half a wavelength from the antenna, which means most practical measurements of dipole patterns are in the far-field.

### 2.4 Finite Length Dipole

For a dipole of arbitrary length $L$, the current distribution is sinusoidal:

$$
I(z') = \begin{cases}
I_m \sin\left[k\left(\frac{L}{2} - z'\right)\right], & 0 \leq z' \leq \frac{L}{2} \\[4pt]
I_m \sin\left[k\left(\frac{L}{2} + z'\right)\right], & -\frac{L}{2} \leq z' \leq 0
\end{cases}
$$

**Vector potential (far-field approximation):**

$$
A_z = \frac{\mu I_m e^{-jkr}}{4\pi r} \int_{-L/2}^{L/2} \sin\left[k\left(\frac{L}{2} - |z'|\right)\right] e^{jkz' \cos\theta} \, dz'
$$

**Far-field electric field (the radiation integral evaluates to a closed form):**

$$
E_\theta = j\eta \frac{I_m e^{-jkr}}{2\pi r} \left[ \frac{\cos\left(\frac{kL}{2} \cos\theta\right) - \cos\left(\frac{kL}{2}\right)}{\sin\theta} \right]
$$

The term in brackets is the **array factor** for a continuous line source, often denoted as $F(\theta)$.

**Normalised power pattern:**

$$
F(\theta) = \left[ \frac{\cos\left(\frac{kL}{2} \cos\theta\right) - \cos\left(\frac{kL}{2}\right)}{\sin\theta} \right]^2
$$

**Table 2: Key Dipole Properties vs. Length**

| $L/\lambda$ | Current Distribution | Pattern Lobes | $D_0$ (dB) | $R_r$ ($\Omega$) | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $\ll 1$ | Triangular | 1 | 1.76 | $20\pi^2(L/\lambda)^2$ | Small dipole regime |
| $0.25$ | Sinusoidal (low amplitude) | 1 | 1.76 | $\approx 10$ | Short monopole equivalent |
| $0.5$ | Half sine | 1 | 2.15 | $73$ | Half-wave dipole |
| $1.0$ | Full sine | 2 | 3.82 | $199$ | Full-wave dipole |
| $1.25$ | 1.25 sine periods | 3 | 4.26 | $\approx 250$ | Multiple lobes appear |
| $1.5$ | 1.5 sine periods | 3 | 3.18 | $\approx 105$ | Directivity decreases |

### 2.5 Half-Wavelength Dipole

The half-wavelength dipole ($L = \lambda/2$) is the most practically important wire antenna because its input impedance is purely real at resonance ($Z_{\text{in}} \approx 73 + j0\ \Omega$), making it easy to match to standard $50\ \Omega$ or $75\ \Omega$ transmission lines.

**Current distribution:**
$$
I(z') = I_m \cos(kz'), \quad -\frac{\lambda}{4} \leq z' \leq \frac{\lambda}{4}
$$

**Far-field:**

$$
E_\theta = j\eta \frac{I_m e^{-jkr}}{2\pi r} \left[ \frac{\cos\left(\frac{\pi}{2} \cos\theta\right)}{\sin\theta} \right]
$$

**Directivity:** $D_0 = 1.643$ ($2.15$ dB).

**Radiation resistance:** $R_r = 73\ \Omega$ (assuming perfectly conducting, infinitely thin wire).

**Input impedance:** $Z_{\text{in}} \approx 73 + j42.5\ \Omega$ for a centre-fed thin dipole. The reactance vanishes at $L \approx 0.48\lambda$ for a typical wire radius.

**Half-power beamwidth (HPBW):** $78^\circ$ in the $E$-plane.

**Effective area:** $A_e = \frac{\lambda^2}{4\pi} D_0 = 0.131\lambda^2$.

### 2.6 Linear Elements Near or on Infinite Perfect Conductors

When a linear wire antenna is placed near an infinite perfect electric conductor (PEC), the boundary condition $\hat{\mathbf{n}} \times \mathbf{E} = 0$ on the conductor surface is satisfied by introducing an **image** of the antenna on the opposite side of the conductor.

**Image Theory Rules:**

| Antenna Orientation | Image Orientation | Current Direction |
| :--- | :--- | :--- |
| Vertical (parallel to $\hat{\mathbf{n}}$) | Vertical, same side | Same direction (constructive) |
| Horizontal (parallel to surface) | Horizontal, opposite side | Opposite direction (cancellation at grazing) |
| Inclined | Inclined, reflected | Component-wise application |

**Monopole:** A quarter-wavelength monopole ($L = \lambda/4$) over a PEC ground plane produces the same radiation pattern in the upper half-space as a half-wavelength dipole in free space. The input impedance is half: $Z_{\text{in}} \approx 36.5\ \Omega$.

**Effect on radiation pattern:**

- A vertical dipole at height $h$ above a PEC ground has a far-field pattern multiplied by the array factor $2\sin(kh \cos\theta)$.
- A horizontal dipole at height $h$ has an array factor $2\cos(kh \cos\theta)$, producing nulls at angles where $\cos(kh \cos\theta) = 0$.

### 2.7 Ground Effects

Real ground is not a perfect conductor. The finite conductivity affects the antenna pattern through:

1. **Reflection coefficient:** The ground reflects waves with a complex reflection coefficient $\Gamma(\theta_i)$ that depends on the polarization, incidence angle, and ground electrical properties ($\epsilon_r$, $\sigma$).
2. **Surface waves:** A vertical electric dipole near a lossy ground launches a Norton surface wave that propagates along the air-ground interface.
3. **Power dissipation:** The ground absorbs a fraction of the radiated power, reducing the antenna efficiency.

**Ground parameters for typical soil:**

| Soil Type | Relative Permittivity $\epsilon_r$ | Conductivity $\sigma$ (S/m) | Loss Tangent $\tan\delta$ at 100 MHz |
| :--- | :--- | :--- | :--- |
| Dry sandy soil | $3-5$ | $10^{-4} - 10^{-3}$ | $0.01 - 0.07$ |
| Wet soil | $10-30$ | $10^{-3} - 10^{-2}$ | $0.1 - 1.0$ |
| Fresh water | $81$ | $10^{-3}$ | $0.002$ |
| Sea water | $81$ | $4$ | $8.8$ |

The ground model uses the **Sommerfeld formulation** for the fields of a dipole over a lossy half-space, which is significantly more complex than the PEC image method.

### 2.8 Computer Codes

Modern analysis of wire antennas relies on numerical electromagnetic codes. The most widely used are:

**Table 3: Wire Antenna Simulation Codes**

| Code | Method | Key Features |
| :--- | :--- | :--- |
| NEC (Numerical Electromagnetics Code) | Method of Moments (MoM) | Thin-wire kernel; ground effects using Sommerfeld-Norton; frequency domain |
| FEKO | MoM + hybrid methods | Commercial; wire segments, surfaces, dielectrics |
| HFSS | Finite Element Method (FEM) | Full-wave 3D; suitable for finite-radius wires and dielectrics |
| CST Microwave Studio | Finite Integration Technique (FIT) | Time-domain; broadband results from single simulation |
| Python (PyNEC, scikit-RF) | Wrapper for NEC engine | Open-source; integration with scientific Python ecosystem |

The standard workflow for computational wire antenna analysis:

1. **Geometry definition:** Specify wire endpoints, radius, and segmentation length (typically $\lambda/10$ to $\lambda/20$ per segment).
2. **Excitation:** Apply a voltage source or current source at the feed point.
3. **Solution:** Solve the matrix equation $[Z][I] = [V]$ for the currents on all segments.
4. **Post-processing:** Compute far-field pattern, input impedance, directivity, gain, and efficiency.

> **[Supplementary]** The segmentation rule $\Delta \ell \leq \lambda/10$ ensures that the current variation over each segment is approximately linear, which is the fundamental assumption of the Method of Moments with pulse basis functions. For sinusoidal basis functions, larger segments ($\lambda/4$) can be used.

---

## 3. Key Parameters and Constraints

**Table 4: Parameters of Linear Wire Antennas**

| Parameter | Symbol | Typical Range | Impact on Performance |
| :--- | :--- | :--- | :--- |
| Dipole length | $L$ | $0.01\lambda$ to $1.5\lambda$ | Determines directivity, impedance, pattern lobes |
| Wire radius | $a$ | $10^{-5}\lambda$ to $10^{-2}\lambda$ | Affects input reactance, bandwidth (thicker $\rightarrow$ wider bandwidth) |
| Feed gap | $g$ | $10^{-4}\lambda$ to $10^{-2}\lambda$ | Capacitive effect; modifies input impedance |
| Height above ground | $h$ | $0.01\lambda$ to $10\lambda$ | Pattern lobing and elevation angle of maximum radiation |
| Ground conductivity | $\sigma$ | $0$ to $4$ S/m | Affects reflection coefficient, surface wave, efficiency |
| Frequency | $f$ | Application-dependent | All electrical dimensions scale as $L/\lambda$ |

---

## 4. Step-by-Step Mechanism: Computing Fields of a Finite Dipole

The following procedure is the standard workflow for computing the radiated fields of any linear wire antenna.

**Step 1: Specify the geometry.**
Place the dipole along the $z$-axis from $-L/2$ to $+L/2$. The source point is $(0, 0, z')$ in Cartesian coordinates.

**Step 2: Write the current distribution.**
For a centre-fed dipole of length $L$, the current is sinusoidal:

$$
I(z') = I_m \sin\left[k\left(\frac{L}{2} - |z'|\right)\right]
$$

**Step 3: Compute the vector potential.**
In the far-field ($r \gg L$), the distance $R = |\mathbf{r} - \mathbf{r}'|$ in the phase is approximated as $R \approx r - z' \cos\theta$, and in the amplitude $R \approx r$:

$$
A_z = \frac{\mu e^{-jkr}}{4\pi r} \int_{-L/2}^{L/2} I(z') e^{jkz' \cos\theta} \, dz'
$$

**Step 4: Evaluate the radiation integral.**
Substitute $I(z')$ and evaluate the integral. The result is:

$$
A_z = \frac{\mu I_m e^{-jkr}}{2\pi r} \cdot \frac{\cos\left(\frac{kL}{2} \cos\theta\right) - \cos\left(\frac{kL}{2}\right)}{k \sin^2\theta}
$$

**Step 5: Compute the far-field electric field.**
In the far-field, $\mathbf{E} = -j\omega \mathbf{A}_\perp$, where $\mathbf{A}_\perp$ is the component of $\mathbf{A}$ transverse to $\hat{\mathbf{r}}$. Since $\mathbf{A} = A_z \hat{\mathbf{z}}$, and $\hat{\mathbf{z}} = \cos\theta \, \hat{\mathbf{r}} - \sin\theta \, \hat{\boldsymbol{\theta}}$:

$$
E_\theta = -j\omega A_z (-\sin\theta) = j\omega A_z \sin\theta
$$

Substituting $A_z$:

$$
E_\theta = j\eta \frac{I_m e^{-jkr}}{2\pi r} \left[ \frac{\cos\left(\frac{kL}{2} \cos\theta\right) - \cos\left(\frac{kL}{2}\right)}{\sin\theta} \right]
$$

**Step 6: Extract the pattern and directivity.**
The normalised power pattern is $|F(\theta)|^2$ where $F(\theta)$ is the bracketed term. The directivity is:

$$
D_0 = \frac{4\pi |F(\theta_{\max})|^2}{\int_0^{2\pi} \int_0^\pi |F(\theta)|^2 \sin\theta \, d\theta \, d\phi}
$$

---

## 5. Connections and Cross-References

- **Section 1 (Antennas):** The radiation mechanism described in Section 1 — charge acceleration producing time-varying currents — is physically realised in the wire antenna. The current distribution on a thin wire is the concrete example of the abstract current density $\mathbf{J}$ introduced there.
- **Section 2 (Fundamental Parameters):** Directivity, gain, radiation pattern, beamwidth, input impedance, and polarization are all computed for the specific case of the wire antenna in this section. The half-wavelength dipole's $73\ \Omega$ radiation resistance is the classical reference value.
- **Section 3 (Radiation Integrals):** The vector potential $\mathbf{A}$ and the far-field approximation derived in Section 3 are applied directly here. The far-field electric field expression for the finite dipole is the result of evaluating the radiation integral of Section 3 with the specific current distribution of Section 4.
- **Section 6 (Arrays):** Linear wire antennas are the elements used in linear, planar, and circular arrays. The element pattern computed here becomes the "element factor" in the pattern multiplication rule of array theory.
- **Section 8 (Integral Equations, Moment Method):** When the sinusoidal current approximation is insufficient (e.g., for thick wires, folded dipoles, or antennas near complex structures), the exact current must be found by solving Pocklington's integral equation numerically. This is the subject of Section 8.

*Prerequisite: Section 3 (Radiation Integrals) — the vector potential method and far-field approximations are used throughout Section 4.*

---

## Solved Exercises

### Exercise 1: Infinitesimal Dipole Radiation Resistance

**Problem:** An infinitesimal dipole of length $dl = \lambda/50$ operates at $f = 300$ MHz. Compute (a) the radiation resistance, (b) the directivity in dB, and (c) the total radiated power if the current amplitude is $I_0 = 1$ A.

**Solution:**

Step 1: Compute the wavenumber.
$$
k = \frac{2\pi}{\lambda}, \quad \frac{dl}{\lambda} = \frac{1}{50} = 0.02
$$

Step 2: Radiation resistance.
$$
R_r = 80\pi^2 \left(\frac{dl}{\lambda}\right)^2 = 80\pi^2 (0.02)^2 = 80 \times 9.8696 \times 0.0004 = 0.316\ \Omega
$$

Step 3: Directivity.
$$
D_0 = 1.5 \quad \Rightarrow \quad D_0(\text{dB}) = 10\log_{10}(1.5) = 1.76\ \text{dB}
$$

Step 4: Radiated power.
$$
P_{\text{rad}} = \frac{1}{2} |I_0|^2 R_r = \frac{1}{2} (1)^2 (0.316) = 0.158\ \text{W}
$$

**Result:** $R_r = 0.316\ \Omega$, $D_0 = 1.76$ dB, $P_{\text{rad}} = 0.158$ W. The extremely low radiation resistance indicates that the infinitesimal dipole is an inefficient radiator unless the current is very large.

---

### Exercise 2: Small Dipole vs. Infinitesimal Dipole Comparison

**Problem:** A small dipole of length $L = \lambda/20$ carries a triangular current distribution with centre amplitude $I_0 = 1$ A. Compare its radiation resistance with that of an infinitesimal dipole of the same length carrying uniform current $I_0$.

**Solution:**

Step 1: Infinitesimal dipole radiation resistance.
$$
R_{r,\text{inf}} = 80\pi^2 \left(\frac{L}{\lambda}\right)^2 = 80\pi^2 (0.05)^2 = 80\pi^2 (0.0025) = 1.974\ \Omega
$$

Step 2: Small dipole radiation resistance.
$$
R_{r,\text{small}} = 20\pi^2 \left(\frac{L}{\lambda}\right)^2 = 20\pi^2 (0.05)^2 = 20\pi^2 (0.0025) = 0.493\ \Omega
$$

Step 3: Ratio.
$$
\frac{R_{r,\text{small}}}{R_{r,\text{inf}}} = \frac{0.493}{1.974} = 0.25 = \frac{1}{4}
$$

**Explanation:** The integral of the triangular current distribution is half that of the uniform distribution ($\int I(z') dz' = I_0 L/2$ vs. $I_0 L$). The radiated power depends on the square of the current moment, so the radiation resistance is reduced by a factor of $4$.

**Result:** $R_{r,\text{small}} = 0.493\ \Omega$ (one-quarter of the uniform-current case).

---

### Exercise 3: Half-Wavelength Dipole Pattern Nulls

**Problem:** Determine the angles $\theta$ (measured from the $z$-axis) at which the far-field pattern of a half-wavelength dipole has nulls. Verify the HPBW is approximately $78^\circ$.

**Solution:**

Step 1: Pattern function for $L = \lambda/2$.
$$
F(\theta) = \frac{\cos\left(\frac{kL}{2} \cos\theta\right)}{\sin\theta} = \frac{\cos\left(\frac{\pi}{2} \cos\theta\right)}{\sin\theta}
$$

The factor $\cos(kL/2) = \cos(\pi/2) = 0$ has been dropped because it is zero.

Step 2: Find nulls by setting $E_\theta = 0$.
Nulls occur when the numerator is zero (provided the denominator is non-zero):

$$
\cos\left(\frac{\pi}{2} \cos\theta\right) = 0 \quad \Rightarrow \quad \frac{\pi}{2} \cos\theta = \pm (2n-1)\frac{\pi}{2}, \ n = 1, 2, \ldots
$$

For $n = 1$:
$$
\frac{\pi}{2} \cos\theta = \pm \frac{\pi}{2} \quad \Rightarrow \quad \cos\theta = \pm 1 \quad \Rightarrow \quad \theta = 0^\circ, 180^\circ
$$

These are the nulls along the dipole axis (the $z$-axis).

For $n = 2$:
$$
\frac{\pi}{2} \cos\theta = \pm \frac{3\pi}{2} \quad \Rightarrow \quad \cos\theta = \pm 3
$$

No solution, since $|\cos\theta| \leq 1$.

Step 3: Determine the HPBW.
The half-power points occur when $|F(\theta)|^2 = 1/2$. Solve numerically:

$$
\frac{\cos\left(\frac{\pi}{2} \cos\theta\right)}{\sin\theta} = \frac{1}{\sqrt{2}}
$$

Using the approximation $\theta_{1/2} \approx 51^\circ$ from the $z$-axis, the HPBW is:

$$
\text{HPBW} = 2(90^\circ - 51^\circ) = 78^\circ
$$

**Result:** Nulls at $\theta = 0^\circ$ and $180^\circ$ (along the dipole axis). HPBW $\approx 78^\circ$.

---

### Exercise 4: Half-Wavelength Dipole Directivity Calculation

**Problem:** Compute the directivity of a half-wavelength dipole by evaluating the radiation integral.

**Solution:**

Step 1: Directivity formula.
$$
D_0 = \frac{4\pi U_{\max}}{P_{\text{rad}}}, \quad U(\theta) = \frac{r^2}{2\eta} |E_\theta|^2
$$

Step 2: Radiation intensity.
$$
U(\theta) = \frac{\eta |I_m|^2}{8\pi^2} \left[ \frac{\cos^2\left(\frac{\pi}{2} \cos\theta\right)}{\sin^2\theta} \right]
$$

The maximum occurs at $\theta = 90^\circ$:

$$
U_{\max} = \frac{\eta |I_m|^2}{8\pi^2} \cdot 1 = \frac{\eta |I_m|^2}{8\pi^2}
$$

Step 3: Total radiated power.
$$
P_{\text{rad}} = \int_0^{2\pi} \int_0^\pi U(\theta) \sin\theta \, d\theta \, d\phi = 2\pi \int_0^\pi U(\theta) \sin\theta \, d\theta
$$

$$
P_{\text{rad}} = \frac{\eta |I_m|^2}{4\pi} \int_0^\pi \frac{\cos^2\left(\frac{\pi}{2} \cos\theta\right)}{\sin\theta} \, d\theta
$$

The definite integral evaluates to:

$$
\int_0^\pi \frac{\cos^2\left(\frac{\pi}{2} \cos\theta\right)}{\sin\theta} \, d\theta = 1.2188
$$

Step 4: Compute directivity.
$$
P_{\text{rad}} = \frac{\eta |I_m|^2}{4\pi} \times 1.2188
$$

$$
D_0 = \frac{4\pi \cdot \frac{\eta |I_m|^2}{8\pi^2}}{\frac{\eta |I_m|^2}{4\pi} \times 1.2188} = \frac{\frac{1}{2\pi}}{\frac{1.2188}{4\pi}} = \frac{2}{1.2188} = 1.641
$$

**Result:** $D_0 = 1.641$ (or $2.15$ dB), which matches the standard value.

---

### Exercise 5: Monopole over a Perfect Ground

**Problem:** A quarter-wavelength monopole ($L = \lambda/4$) is mounted vertically over an infinite PEC ground plane. Determine (a) the radiation pattern in the upper half-space, (b) the directivity, and (c) the input impedance.

**Solution:**

Step 1: Image theory application.
The monopole of length $\lambda/4$ and its image form a half-wavelength dipole of total length $\lambda/2$ in free space. The fields in the upper half-space ($0 \leq \theta \leq \pi/2$) are identical to those of the dipole.

Step 2: Radiation pattern.
The far-field is the same as the half-wavelength dipole pattern, restricted to the upper hemisphere:

$$
E_\theta = j\eta \frac{I_m e^{-jkr}}{2\pi r} \left[ \frac{\cos\left(\frac{\pi}{2} \cos\theta\right)}{\sin\theta} \right], \quad 0 \leq \theta \leq \frac{\pi}{2}
$$

Step 3: Directivity.
The monopole radiates only into $2\pi$ steradians. The radiated power is half that of the dipole:

$$
P_{\text{rad, monopole}} = \frac{1}{2} P_{\text{rad, dipole}}
$$

The directivity doubles:

$$
D_{0,\text{monopole}} = \frac{4\pi U_{\max}}{P_{\text{rad, monopole}}} = 2 \times D_{0,\text{dipole}} = 2 \times 1.64 = 3.28 \ (\approx 5.16\ \text{dB})
$$

Step 4: Input impedance.
The monopole impedance is half that of the dipole:

$$
Z_{\text{in, monopole}} = \frac{1}{2} Z_{\text{in, dipole}} \approx \frac{73 + j42.5}{2} = 36.5 + j21.25\ \Omega
$$

**Result:** Pattern is the upper lobe of the dipole pattern; $D_0 = 3.28$ ($5.16$ dB); $Z_{\text{in}} \approx 36.5 + j21.25\ \Omega$.

---

### Exercise 6: Vertical Dipole at Height $h$ Above a PEC Ground

**Problem:** A vertical half-wavelength dipole is placed at a height $h = \lambda/2$ above an infinite PEC ground plane. Compute the elevation plane pattern and find the angle of maximum radiation.

**Solution:**

Step 1: Pattern multiplication.
The total far-field is the product of the element pattern and the array factor due to the ground:

$$
E_{\text{total}} = E_{\text{dipole}}(\theta) \times \text{AF}(\theta)
$$

For a vertical dipole and its image (both vertical, same current direction):

$$
\text{AF}(\theta) = 2 \sin(kh \cos\theta)
$$

The $\sin$ function arises because the image current flows in the same direction, producing constructive and destructive interference.

Step 2: Substitute the half-wave dipole pattern.

$$
E_{\text{total}} = j\eta \frac{I_m e^{-jkr}}{2\pi r} \left[ \frac{\cos\left(\frac{\pi}{2} \cos\theta\right)}{\sin\theta} \right] \times 2 \sin(kh \cos\theta)
$$

For $h = \lambda/2$, $kh = 2\pi(\lambda/2)/\lambda = \pi$:

$$
\text{AF}(\theta) = 2 \sin(\pi \cos\theta)
$$

Step 3: Find the angle of maximum radiation.
The element pattern is maximum at $\theta = 90^\circ$. The array factor at $\theta = 90^\circ$:

$$
\text{AF}(90^\circ) = 2 \sin(\pi \cdot 0) = 0
$$

The null from the array factor suppresses the broadside direction. The maximum occurs where:

$$
|E_{\text{total}}| \text{ is maximised} \quad \Rightarrow \quad \text{Solve } \frac{d}{d\theta} |E_{\text{total}}| = 0
$$

The maximum occurs approximately at $\theta \approx 45^\circ$ (elevation angle of $45^\circ$ above the horizon, or $\theta = 45^\circ$ from the $z$-axis).

Step 4: Pattern characteristics.
The pattern has a null at $\theta = 90^\circ$ (horizon) and additional nulls when $\sin(\pi \cos\theta) = 0$, i.e., $\pi \cos\theta = n\pi$ or $\cos\theta = n$, which gives $\theta = 0^\circ$ (zenith) and $\theta = 90^\circ$ (horizon). The pattern consists of two main lobes above the horizon.

**Result:** Maximum radiation at $\theta \approx 45^\circ$; nulls at $\theta = 0^\circ$ and $90^\circ$.

---

### Exercise 7: Finite Dipole Length for Specific Directivity

**Problem:** Determine the length $L$ (in wavelengths) of a centre-fed dipole that achieves a directivity of $D_0 = 3.0$ ($4.77$ dB). Assume a sinusoidal current distribution.

**Solution:**

Step 1: Directivity as a function of length.
The directivity of a finite-length dipole with sinusoidal current is:

$$
D_0 = \frac{2 F^2(\theta_{\max})}{\int_0^\pi F^2(\theta) \sin\theta \, d\theta}
$$

where:

$$
F(\theta) = \frac{\cos\left(\frac{kL}{2} \cos\theta\right) - \cos\left(\frac{kL}{2}\right)}{\sin\theta}
$$

Step 2: Trial and evaluation.
For $L = \lambda$ ($kL/2 = \pi$):
- Numerator: $\cos(\pi \cos\theta) - \cos(\pi) = \cos(\pi \cos\theta) + 1$
- Maximum at $\theta = 90^\circ$: $F(90^\circ) = \cos(0) + 1 = 2$
- $D_0 \approx 3.82$ ($5.82$ dB) — exceeds target.

For $L = 0.75\lambda$ ($kL/2 = 0.75\pi = 135^\circ$):
- $\cos(kL/2) = \cos(135^\circ) = -0.707$
- $F(\theta) = [\cos(135^\circ \cos\theta) + 0.707]/\sin\theta$
- Maximum at $\theta = 90^\circ$: $F(90^\circ) = \cos(0) + 0.707 = 1.707$
- The integral evaluates to approximately $1.94$.
- $D_0 = 2(1.707)^2 / 1.94 = 2(2.914)/1.94 = 3.00$

Step 3: Verify.
For $L = 0.75\lambda$, $D_0 \approx 3.00$. This lies between the half-wave ($D_0 = 1.64$) and full-wave ($D_0 = 3.82$) values.

**Result:** $L \approx 0.75\lambda$ achieves $D_0 = 3.0$.

---

### Exercise 8: Input Impedance Variation with Radius

**Problem:** A centre-fed half-wavelength dipole has a wire radius $a = 0.001\lambda$. Using the induced EMF method approximation, estimate the input reactance. How does it change if the radius is increased to $a = 0.01\lambda$?

**Solution:**

Step 1: Input impedance of a thin half-wavelength dipole.
The input impedance of a centre-fed dipole of length $L = \lambda/2$ with radius $a$ can be approximated by:

$$
Z_{\text{in}} \approx R_r + jX_{\text{in}}
$$

where $R_r = 73\ \Omega$ and the reactance depends on the wire thickness.

Step 2: Reactance approximation.
For a dipole near resonance ($L \approx \lambda/2$), the input reactance is approximately:

$$
X_{\text{in}} \approx 42.5 - 10 \log_{10}\left(\frac{\lambda}{a}\right) \quad \text{(empirical for thin dipoles)}
$$

For $a = 0.001\lambda$, $\lambda/a = 1000$:
$$
X_{\text{in}} \approx 42.5 - 10 \log_{10}(1000) = 42.5 - 30 = 12.5\ \Omega
$$

Step 3: For $a = 0.01\lambda$, $\lambda/a = 100$:
$$
X_{\text{in}} \approx 42.5 - 10 \log_{10}(100) = 42.5 - 20 = 22.5\ \Omega
$$

Step 4: More accurate reactance using the induced EMF method.
The exact induced EMF method gives the reactance of a dipole of length $L = 0.5\lambda$ as approximately $X_{\text{in}} = 42.5\ \Omega$ for an infinitely thin wire. For finite radius, the resonant length shifts slightly, and the reactance at $L = 0.5\lambda$ changes. The general formula is:

$$
X_{\text{in}} \approx 30 \left[ 2 \text{Ci}(kL) - \text{Ci}(2kL) - \text{Ci}\left(\frac{2ka^2}{L}\right) \right]
$$

where $\text{Ci}(x)$ is the cosine integral.

For $L = \lambda/2$, $kL = \pi$:
- $\text{Ci}(2\pi) \approx -0.0226$
- $\text{Ci}(\pi) \approx 0.0748$
- $\text{Ci}(2ka^2/L)$ depends on $a$.

For $a = 0.001\lambda$: $2ka^2/L = 2(2\pi/\lambda)(0.001\lambda)^2/(0.5\lambda) = 8\pi \times 10^{-6} \approx 2.51 \times 10^{-5}$. Then $\text{Ci}(2.51 \times 10^{-5}) \approx \ln(2.51 \times 10^{-5}) + \gamma \approx -10.59 + 0.577 = -10.01$.

$$
X_{\text{in}} \approx 30[2(0.0748) - (-0.0226) - (-10.01)] = 30[0.1496 + 0.0226 + 10.01] = 30(10.182) \approx 305\ \Omega
$$

This value appears large because the dipole is not exactly at resonance. At the exact resonant length ($L \approx 0.48\lambda$), the reactance vanishes.

**Result:** For $a = 0.001\lambda$, $X_{\text{in}} \approx 12.5\ \Omega$ (approximation) at $L = \lambda/2$. Increasing the radius to $a = 0.01\lambda$ increases the reactance and shifts the resonant length to a slightly shorter value. The practical takeaway is that thicker dipoles have wider bandwidth and lower Q.

---

### Exercise 9: Horizontal Dipole Over Ground

**Problem:** A horizontal half-wavelength dipole is placed at height $h = 0.25\lambda$ above a PEC ground. Determine the far-field pattern and find the elevation angle of the first maximum above the ground plane.

**Solution:**

Step 1: Array factor for a horizontal dipole.
For a horizontal dipole and its image (opposite current direction):

$$
\text{AF}(\theta) = 2 \cos(kh \cos\theta)
$$

For $h = 0.25\lambda$, $kh = 2\pi(0.25\lambda)/\lambda = \pi/2$:

$$
\text{AF}(\theta) = 2 \cos\left(\frac{\pi}{2} \cos\theta\right)
$$

Step 2: Total pattern (assuming dipole along $x$-axis, pattern in the $y$-$z$ plane).

In the $y$-$z$ plane ($\phi = 90^\circ$), the half-wave dipole element pattern is omnidirectional in $\theta$:
$$
E_{\text{element}} \propto \frac{\cos\left(\frac{\pi}{2} \cos\theta\right)}{\sin\theta}
$$

Total:
$$
E_{\text{total}} \propto \frac{\cos\left(\frac{\pi}{2} \cos\theta\right)}{\sin\theta} \times 2 \cos\left(\frac{\pi}{2} \cos\theta\right)
$$

Step 3: Simplify.
$$
E_{\text{total}} \propto \frac{2 \cos^2\left(\frac{\pi}{2} \cos\theta\right)}{\sin\theta}
$$

Step 4: Find maxima.
The maximum occurs where:
$$
\frac{d}{d\theta} \left[ \frac{\cos^2\left(\frac{\pi}{2} \cos\theta\right)}{\sin\theta} \right] = 0
$$

The first maximum (closest to the horizon, $\theta = 90^\circ$) occurs at approximately $\theta \approx 60^\circ$, i.e., $30^\circ$ above the horizon.

Step 5: Nulls.
Nulls occur when $\cos\left(\frac{\pi}{2} \cos\theta\right) = 0$, i.e., $\frac{\pi}{2} \cos\theta = \pi/2$ giving $\theta = 0^\circ$, or $\frac{\pi}{2} \cos\theta = 3\pi/2$ giving $\cos\theta = 3$ (no solution). So the only null is at $\theta = 0^\circ$ (zenith).

**Result:** The pattern has a maximum at $\theta \approx 60^\circ$ ($30^\circ$ elevation) and a null at the zenith ($\theta = 0^\circ$).

---

### Exercise 10: NEC Simulation of a Centre-Fed Dipole

**Problem:** Outline the steps to model a centre-fed half-wavelength dipole in NEC and compute its input impedance. Use the following parameters: frequency $f = 300$ MHz, wire radius $a = 1$ mm, segmentation length $\Delta \ell = \lambda/20$.

**Solution:**

Step 1: Compute physical dimensions.
$$
\lambda = \frac{c}{f} = \frac{3 \times 10^8}{300 \times 10^6} = 1.0\ \text{m}
$$

Dipole length: $L = \lambda/2 = 0.5$ m.
Segmentation length: $\Delta \ell = \lambda/20 = 0.05$ m.
Number of segments: $N = L / \Delta \ell = 0.5 / 0.05 = 10$ segments (each half: 5 segments).

Step 2: NEC geometry card syntax.
```
GW  1  11  0.0 0.0 -0.25  0.0 0.0  0.25  0.001
```
- `GW` = geometry wire card
- `1` = tag number
- `11` = number of segments (11 segments for 10 segments plus 1 for the feed)
- `0.0 0.0 -0.25` = first endpoint ($x, y, z$)
- `0.0 0.0 0.25` = second endpoint
- `0.001` = wire radius in metres ($1$ mm)

Step 3: Excitation card.
```
GW  1  11  0.0 0.0 -0.25  0.0 0.0  0.25  0.001
EX  0  6  0  1.0  0.0
```
- `EX 0` = voltage source excitation
- `6` = segment number at the feed (centre segment of 11)
- `1.0 0.0` = voltage magnitude and phase (1 V, 0 degrees)

Step 4: Frequency and ground plane.
```
FR  0  1  0  0  300.0  0.0
GD  0  0  0  0  1.0  0.0  0.0
```
- `FR` = frequency card (300 MHz)
- `GD` = ground card (0 = free space, no ground)

Step 5: Run and post-process.
The NEC output provides:
- Input impedance: $Z_{\text{in}} = R_{\text{in}} + jX_{\text{in}}$
- Current distribution: $I_n$ on each segment $n$
- Far-field pattern at specified angles

Expected result (thin wire): $Z_{\text{in}} \approx 73 + j42.5\ \Omega$.

Step 6: Convergence check.
Refine the segmentation to $\Delta \ell = \lambda/40$ (20 segments per half) and compare. If the impedance changes by less than $1\ \Omega$, the solution is converged.

**Result:** The NEC simulation produces $Z_{\text{in}} \approx 73 + j42.5\ \Omega$ for the thin half-wavelength dipole. The current distribution follows a cosine shape as expected.

---

## Exam Tip: Pattern Function Evaluation for Finite Dipoles

A common exam problem provides a dipole length $L$ and asks for the far-field pattern, directivity, or radiation resistance. The critical steps are:

1. **Write the pattern function immediately:**
   $$
   F(\theta) = \frac{\cos\left(\frac{kL}{2} \cos\theta\right) - \cos\left(\frac{kL}{2}\right)}{\sin\theta}
   $$
   This is the universal form for a centre-fed dipole with sinusoidal current.

2. **Simplify using the specific $kL/2$ value.** For $L = \lambda/2$, $kL/2 = \pi/2$, so $\cos(\pi/2) = 0$ and the pattern reduces to:
   $$
   F(\theta) = \frac{\cos\left(\frac{\pi}{2} \cos\theta\right)}{\sin\theta}
   $$

3. **Identify nulls and maxima.** Nulls occur when the numerator is zero (except where $\sin\theta = 0$ also, which requires L'Hopital's rule). Maxima typically occur at $\theta = 90^\circ$ for $L \leq \lambda$.

4. **For directivity, use the ratio formula:**
   $$
   D_0 = \frac{2}{\int_0^\pi \left[ \frac{\cos\left(\frac{kL}{2} \cos\theta\right) - \cos\left(\frac{kL}{2}\right)}{\sin\theta} \right]^2 \sin\theta \, d\theta}
   $$
   The integral often simplifies to known values for $L = \lambda/2$ ($1.2188$) and $L = \lambda$ ($0.610$).

**Common pitfalls:**
- Forgetting that the infinitesimal dipole and small dipole have the same directivity (1.5) but different radiation resistances.
- Using the uniform current formula $R_r = 80\pi^2(L/\lambda)^2$ for a dipole with triangular current distribution. The correct formula for a small dipole is $R_r = 20\pi^2(L/\lambda)^2$.
- Confusing the dipole length $L$ with the half-length used in the pattern function argument. The pattern function uses $kL/2$, not $kL$.
- When using image theory for a monopole, forgetting that the directivity doubles because the power is radiated into only half the space.
- For horizontal dipoles over ground, mixing up the array factor: vertical dipoles use $2\sin(kh \cos\theta)$, horizontal dipoles use $2\cos(kh \cos\theta)$.

**Pattern recognition shortcut:** If an exam problem gives a dipole length $L$ and asks for the pattern, write the universal pattern function $F(\theta)$ first with $kL/2$ expressed as $\pi L/\lambda$. Then substitute $L/\lambda$ and simplify. This mechanical approach works for any centre-fed dipole length.