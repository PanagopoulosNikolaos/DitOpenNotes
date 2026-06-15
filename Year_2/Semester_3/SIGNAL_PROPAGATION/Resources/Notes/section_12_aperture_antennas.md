# Aperture Antennas

Aperture antennas constitute a fundamental class of radiators that emit electromagnetic waves through an opening (aperture), commonly used at microwave frequencies (300 MHz -- 300 GHz) where their physical dimensions are on the order of a wavelength or larger. Examples include open-ended waveguides, horn antennas, reflector antennas, and slot antennas. The analysis of aperture antennas relies on the field equivalence principle (Huygens' principle), which replaces the aperture fields with equivalent surface current densities, enabling far-field radiation pattern calculation through Fourier transform techniques. This section covers the theoretical foundations, radiation equations for rectangular and circular apertures, directivity and aperture efficiency, Babinet's principle, Fourier transform methods in aperture theory, and ground plane edge effects via geometrical theory of diffraction.

---

## 1. Conceptual Foundation

### 1.1 The Aperture Antenna Concept

Aperture antennas radiate through an opening in a conducting surface or through the open end of a waveguide. Unlike wire antennas, where the current distribution along the conductor is the source of radiation, aperture antennas are analyzed by considering the field distribution across the aperture opening. The fundamental principle underlying aperture antenna analysis is the **field equivalence principle**, which is a rigorous formulation of Huygens' principle.

> **Huygens' Principle:** Every point on a wavefront may be considered a source of secondary spherical wavelets which spread out in the forward direction at the speed of light. The new wavefront is the tangential surface to all of these secondary wavelets.

**A. Schelkunoff (1936) formalized this into a rigorous mathematical framework** — the field equivalence principle — which states that the actual sources behind an aperture can be replaced by equivalent electric and magnetic surface currents over the aperture surface, radiating into free space.

### 1.2 Why Aperture Antennas?

Aperture antennas dominate at microwave frequencies for several reasons:

- **Gain scales with frequency:** The directivity of an aperture antenna is proportional to $A/\lambda^2$, where $A$ is the physical area. At high frequencies, electrically large apertures are physically small.
- **Waveguide compatibility:** Aperture antennas integrate naturally with waveguide transmission lines.
- **High directivity achievable:** Large apertures (many wavelengths across) produce narrow beams.
- **Control of sidelobes:** The aperture field distribution (tapering) can be tailored to control sidelobe levels.

### 1.3 The Uniqueness Theorem

The equivalence principle is based on the **uniqueness theorem**: a field in a lossy region is uniquely specified by the sources within the region plus:
- The tangential components of the electric field over the boundary, **or**
- The tangential components of the magnetic field over the boundary, **or**
- A combination of both.

This means that if we know the tangential fields $E_a$ and $H_a$ over an aperture surface, we can uniquely determine the radiated fields.

---

## 2. Formal Definition and Model

### 2.1 The Field Equivalence Principle

Consider an aperture $A$ in an infinite conducting screen. The aperture fields $E_a$, $H_a$ are assumed known. The equivalent surface currents that replace the aperture are:

$$
\mathbf{J}_s = \hat{n} \times \mathbf{H}_a \quad \text{(electric surface current)}
$$

$$
\mathbf{M}_s = -\hat{n} \times \mathbf{E}_a \quad \text{(magnetic surface current)}
$$

where $\hat{n}$ is the unit normal pointing into the region of interest (the radiation half-space).

For a flat aperture in the $xy$-plane with $\hat{n} = \hat{z}$:

$$
\mathbf{J}_s = \hat{z} \times \mathbf{H}_a, \qquad \mathbf{M}_s = -\hat{z} \times \mathbf{E}_a
$$

These equivalent currents radiate in free space, and the radiated fields are calculated using the vector potentials $\mathbf{A}$ (from $\mathbf{J}_s$) and $\mathbf{F}$ (from $\mathbf{M}_s$).

#### 2.1.1 Alternative Forms Using Image Theory

If the screen is a **perfect electric conductor (PEC)**:

$$
\mathbf{J}_s = 0, \qquad \mathbf{M}_s = -2(\hat{n} \times \mathbf{E}_a)
$$

If the screen is a **perfect magnetic conductor (PMC)**:

$$
\mathbf{J}_s = 2(\hat{n} \times \mathbf{H}_a), \qquad \mathbf{M}_s = 0
$$

These forms use image theory: the conducting screen is eliminated and replaced by an image current, doubling the remaining current density.

### 2.2 The Huygens Source Approximation

If the aperture fields satisfy the uniform plane-wave relationship (a **Huygens source**):

$$
\mathbf{H}_a = \frac{1}{\eta} \hat{n} \times \mathbf{E}_a
$$

where $\eta = \sqrt{\mu/\epsilon}$ is the intrinsic impedance of free space. The Fourier transforms of the aperture fields then satisfy:

$$
\mathbf{g} = \frac{1}{\eta} \hat{z} \times \mathbf{f}
$$

where:

$$
\mathbf{f}(\theta, \phi) = \iint_A \mathbf{E}_a(x', y') e^{j(k_x x' + k_y y')} \, dx' dy'
$$

$$
\mathbf{g}(\theta, \phi) = \iint_A \mathbf{H}_a(x', y') e^{j(k_x x' + k_y y')} \, dx' dy'
$$

with $k_x = k \sin\theta \cos\phi$, $k_y = k \sin\theta \sin\phi$, $k = 2\pi/\lambda$.

### 2.3 General Radiation Equations

For a flat aperture in the $xy$-plane with $\hat{n} = \hat{z}$, the far-field electric field components are:

$$
E_\theta = \frac{jk e^{-jkr}}{4\pi r} \left[ (f_x \cos\phi + f_y \sin\phi) + \eta \cos\theta (g_y \cos\phi - g_x \sin\phi) \right]
$$

$$
E_\phi = \frac{jk e^{-jkr}}{4\pi r} \left[ \cos\theta (f_y \cos\phi - f_x \sin\phi) - \eta (g_x \cos\phi + g_y \sin\phi) \right]
$$

For a **Huygens source**, these simplify using the obliquity factor $(1 + \cos\theta)/2$:

$$
E_\theta = \frac{jk e^{-jkr}}{2\pi r} \left( \frac{1 + \cos\theta}{2} \right) (f_x \cos\phi + f_y \sin\phi)
$$

$$
E_\phi = \frac{jk e^{-jkr}}{2\pi r} \left( \frac{1 + \cos\theta}{2} \right) (f_y \cos\phi - f_x \sin\phi)
$$

The normalized field strength is:

$$
\frac{|E(\theta, \phi)|}{|E|_{\text{max}}} = \left( \frac{1 + \cos\theta}{2} \right) |\bar{f}(\theta, \phi)|
$$

where $\bar{f}(\theta, \phi)$ is the normalized Fourier transform of the aperture field.

### 2.4 Directivity and Aperture Efficiency

The **directivity** of an aperture antenna is:

$$
D_0 = \frac{4\pi}{\lambda^2} A_{\text{eff}} = \frac{4\pi}{\lambda^2} \eta_{\text{ap}} A_{\text{phys}}
$$

where:
- $A_{\text{eff}}$ is the effective area,
- $A_{\text{phys}}$ is the physical area of the aperture,
- $\eta_{\text{ap}}$ is the aperture efficiency.

The **aperture efficiency** is defined as:

$$
\eta_{\text{ap}} = \frac{A_{\text{eff}}}{A_{\text{phys}}} = \frac{\left| \iint_A \mathbf{E}_a(x', y') \, dS' \right|^2}{A_{\text{phys}} \iint_A |\mathbf{E}_a(x', y')|^2 \, dS'}
$$

The aperture efficiency can be factored into two components:
- **Taper efficiency** $\eta_t$: depends on the amplitude distribution,
- **Phase error efficiency** $\eta_p$: depends on the phase uniformity.

For a **uniformly illuminated aperture**, $\eta_{\text{ap}} = 1$ (100% efficiency), giving the maximum possible directivity for the given physical area.

### 2.5 Babinet's Principle

Babinet's principle establishes a duality relationship between the radiation patterns of an aperture and its complementary screen:

> The sum of the fields radiated by an aperture and those radiated by its complementary screen (where the aperture and screen are swapped) equals the field that would exist in the absence of any screen.

For an aperture in a conducting screen, if we define:
- $\mathbf{E}_a$, $\mathbf{H}_a$: fields from the aperture,
- $\mathbf{E}_c$, $\mathbf{H}_c$: fields from the complementary screen,

then:

$$
\mathbf{E}_a + \mathbf{E}_c = \mathbf{E}_{\text{inc}}, \quad \mathbf{H}_a + \mathbf{H}_c = \mathbf{H}_{\text{inc}}
$$

where $\mathbf{E}_{\text{inc}}$, $\mathbf{H}_{\text{inc}}$ are the incident fields in the absence of any screen.

A practical consequence: the radiation pattern of a slot antenna is the dual of a dipole antenna of complementary shape. For example, a half-wavelength slot in a conducting plane produces a pattern identical to a half-wave dipole, but with the electric and magnetic fields swapped.

### 2.6 Fourier Transforms in Aperture Antenna Theory

The far-field radiation pattern of an aperture antenna is the **two-dimensional Fourier transform** of the aperture field distribution. This fundamental relationship arises because the far-field integral has the form:

$$
\mathbf{E}(\theta, \phi) \propto \iint_A \mathbf{E}_a(x', y') e^{j(k_x x' + k_y y')} \, dx' dy'
$$

where $k_x = k \sin\theta \cos\phi$ and $k_y = k \sin\theta \sin\phi$ are the spatial frequency variables.

> **[Key Insight]** This Fourier transform relationship means that:
> - A large aperture (wide in space) produces a narrow beam (narrow in angular spectrum).
> - A uniform aperture distribution produces a sinc-function pattern with high sidelobes.
> - Tapered (amplitude-weighted) distributions produce lower sidelobes but wider main beams.
> - A linear phase variation across the aperture steers the beam (equivalent to the Fourier shift theorem).

### 2.7 Geometrical Theory of Diffraction (GTD) for Ground Plane Edge Effects

When an aperture antenna is mounted on a finite ground plane, diffraction from the edges modifies the radiation pattern, particularly in the backward direction and at wide angles. The **Geometrical Theory of Diffraction (GTD)** extends geometrical optics by adding diffracted rays from edges.

The **knife-edge diffraction coefficient** for a conducting half-plane is given by Sommerfeld's exact solution. For an incident plane wave at angle $\alpha$ relative to the edge, the diffraction coefficient for the TE case is:

$$
D_{\text{edge}} = -\frac{1-j}{4\sqrt{\pi k}} \left( \frac{1}{\cos\frac{\phi-\alpha}{2}} - \frac{1}{\cos\frac{\phi+\alpha}{2}} \right)
$$

where $\phi$ is the observation angle measured from the conducting plane.

For the Fresnel (paraxial) approximation near the forward direction ($\theta \approx 0$):

$$
D_{\text{edge}} \approx \frac{1-j}{2\sqrt{\pi k} \, \theta}
$$

The diffracted field behaves as a cylindrical wave emanating from the edge:

$$
E_d = E_{\text{edge}} \frac{e^{-jkl}}{\sqrt{l}} D_{\text{edge}}
$$

---

## 3. Key Parameters and Constraints

### Table 1: Aperture Antenna Parameters

| Parameter | Symbol | Definition | Typical Range | Impact |
|:---|:---|:---|:---|:---|
| Aperture dimensions | $a$, $b$ | Physical width and height | $0.5\lambda$ -- $100\lambda$ | Determines beamwidth and gain |
| Electrical size | $a/\lambda$, $b/\lambda$ | Normalized dimensions | $0.5$ -- $100$ | Larger $\to$ narrower beam |
| Aperture efficiency | $\eta_{\text{ap}}$ | $A_{\text{eff}}/A_{\text{phys}}$ | $0.5$ -- $1.0$ | Higher $\to$ higher directivity |
| Taper efficiency | $\eta_t$ | Amplitude taper loss | $0.7$ -- $1.0$ | Lower $\to$ lower sidelobes |
| Phase error | $\eta_p$ | Phase uniformity loss | $0.8$ -- $1.0$ | Phase errors reduce gain |
| 3-dB beamwidth | $\Theta_{3\text{dB}}$ | Half-power beamwidth | $0.5^\circ$ -- $60^\circ$ | Inverse to $a/\lambda$ |
| First null beamwidth | $\Theta_{\text{null}}$ | Angle to first null | $2\times$ to $3\times \Theta_{3\text{dB}}$ | Resolution limit |
| Sidelobe level | SLL | Peak sidelobe relative to main beam | $-13$ dB to $-60$ dB | Determined by aperture taper |
| Directivity | $D_0$ | Peak directivity | $10$ -- $50$ dBi | Scales with $A/\lambda^2$ |

### Table 2: Comparison of Aperture Illuminations

| Illumination Type | Aperture Efficiency | SLL (dB) | Beamwidth Factor | Relative Directivity |
|:---|:---:|:---:|:---:|:---:|
| **Uniform** | 100% | $-13.26$ | $0.886\lambda/a$ | 1.00 (reference) |
| **Cosine taper** | 81% | $-23$ | $1.20\lambda/a$ | 0.81 |
| **Cosine-squared taper** | 67% | $-32$ | $1.44\lambda/a$ | 0.67 |
| **Taylor ($\bar{n}=5$, $-35$ dB)** | $\approx 95$% | $-35$ | $1.09\lambda/a$ | $\approx 0.95$ |
| **Taylor ($\bar{n}=8$, $-40$ dB)** | $\approx 90$% | $-40$ | $1.14\lambda/a$ | $\approx 0.90$ |

### Table 3: Circular Aperture Pattern Characteristics

| Parameter | Uniform Circular | Tapered Circular (Taylor) |
|:---|:---:|:---:|
| First null location ($u = a\sin\theta/\lambda$) | $0.6098$ | Design-dependent |
| 3-dB point ($u$) | $0.2572$ | Broader |
| SLL | $-17.56$ dB | Design level ($-30$ to $-50$ dB) |
| Directivity formula | $4\pi(\pi a^2)/\lambda^2$ | Reduced by efficiency factor |
| Beamwidth | $1.22\lambda/D$ | Broader by broadening factor |

---

## 4. Step-by-Step Mechanism

### 4.1 How an Aperture Antenna Radiates

**Step 1: Aperture Field Establishment.** A source (waveguide feed, horn, or reflector) establishes electric and magnetic field distributions across the aperture opening. This field distribution is the primary determinant of the radiation pattern.

**Step 2: Equivalence Current Formation.** By the field equivalence principle, the tangential aperture fields $E_a$ and $H_a$ define equivalent surface currents $\mathbf{J}_s = \hat{n} \times \mathbf{H}_a$ and $\mathbf{M}_s = -\hat{n} \times \mathbf{E}_a$ on the aperture surface. These currents act as sources radiating into free space.

**Step 3: Fourier Transform Relationship.** The far-field radiation pattern is the 2-D Fourier transform of the aperture field distribution. The spatial frequency variables $k_x$, $k_y$ map to angular coordinates $\theta$, $\phi$ through $k_x = k\sin\theta\cos\phi$ and $k_y = k\sin\theta\sin\phi$.

**Step 4: Obliquity Factor.** The factor $(1 + \cos\theta)/2$ (for a Huygens source) accounts for the projection of the aperture plane onto the observation direction. At boresight ($\theta = 0^\circ$), this factor equals 1; at $\theta = 90^\circ$, it reduces to 0.5.

**Step 5: Main Beam Formation.** The main beam forms in the direction perpendicular to the aperture plane (broadside) when the aperture fields have uniform phase. The beamwidth is approximately $\lambda/a$ radians for a rectangular aperture of width $a$.

**Step 6: Sidelobe Structure.** The sidelobes result from constructive interference of radiation from different parts of the aperture at angles where the phase difference between aperture elements is an integer multiple of $2\pi$ (except at boresight). Tapering the amplitude distribution reduces the effective aperture size for sidelobe formation, lowering sidelobe levels at the cost of beamwidth broadening.

### 4.2 Radiation Pattern Formation for a Uniform Rectangular Aperture

1. **Aperture field:** $\mathbf{E}_a = \hat{y} E_0$ for $|x| \le a/2$, $|y| \le b/2$, zero elsewhere.
2. **Fourier transform:** The normalized pattern function is:
   $$
   \bar{f}(\theta, \phi) = \frac{\sin(\pi a \sin\theta \cos\phi / \lambda)}{\pi a \sin\theta \cos\phi / \lambda} \cdot \frac{\sin(\pi b \sin\theta \sin\phi / \lambda)}{\pi b \sin\theta \sin\phi / \lambda}
   $$

3. **Principal plane patterns:**
   - **E-plane** ($\phi = 90^\circ$, $yz$-plane):
     $$
     |E(\theta)| \propto \frac{\sin(\pi b \sin\theta / \lambda)}{\pi b \sin\theta / \lambda}
     $$
   - **H-plane** ($\phi = 0^\circ$, $xz$-plane):
     $$
     |E(\theta)| \propto \cos\theta \cdot \frac{\sin(\pi a \sin\theta / \lambda)}{\pi a \sin\theta / \lambda}
     $$

4. **Beamwidth:** The 3-dB beamwidth in each principal plane is approximately:
   $$
   \Theta_{3\text{dB}}^{(x)} = 0.886 \frac{\lambda}{a} \text{ rad}, \quad \Theta_{3\text{dB}}^{(y)} = 0.886 \frac{\lambda}{b} \text{ rad}
   $$

5. **Sidelobe level:** First sidelobe is $-13.26$ dB down from the main beam peak.

### 4.3 Radiation Pattern Formation for a Circular Aperture

1. **Aperture field:** $\mathbf{E}_a = \hat{x} E_0$ for $\rho \le a$ (uniform).
2. **Fourier transform in cylindrical coordinates:** The normalized pattern function is:
   $$
   \bar{f}(\theta) = \frac{2J_1(ka\sin\theta)}{ka\sin\theta} = \frac{2J_1(2\pi a\sin\theta/\lambda)}{2\pi a\sin\theta/\lambda}
   $$
   where $J_1$ is the Bessel function of the first kind, order 1.

3. **Pattern characteristics:**
   - First null: $a\sin\theta/\lambda = 0.6098$
   - 3-dB point: $a\sin\theta/\lambda = 0.2572$
   - 3-dB beamwidth: $\Theta_{3\text{dB}} = 0.5144 \, \lambda/a$ rad $= 29.47^\circ \, \lambda/a$
   - First sidelobe level: $-17.56$ dB

4. **Airy pattern:** The resulting pattern is known as the **Airy pattern**, which describes the Fraunhofer diffraction pattern of a circular aperture (also the point spread function of an ideal optical system).

### 4.4 Edge Diffraction Mechanism (GTD)

1. When an aperture is mounted on a finite ground plane, the incident field illuminates the edges of the plane.
2. Each edge generates diffracted rays according to the local geometry of the edge (knife-edge, wedge, etc.).
3. These diffracted rays propagate into both the illuminated and shadow regions.
4. The total field is the sum of the geometrical optics field (direct + reflected rays) and the diffracted field.
5. The diffracted field is significant in directions where the geometrical optics field is discontinuous (e.g., at the shadow boundary).
6. For forward scattering near the main beam direction, edge diffraction primarily affects the far-out sidelobes and the backlobe region.

---

## Solved Exercises

### Exercise 1: Directivity of a Uniform Rectangular Aperture

**Problem:** A rectangular aperture measures $a = 10\lambda$ along the $x$-axis and $b = 5\lambda$ along the $y$-axis. The aperture is uniformly illuminated.
1. Calculate the directivity $D_0$.
2. Calculate the 3-dB beamwidths in the $xz$- and $yz$-planes.
3. Calculate the first-null beamwidths.

**Solution:**

#### Step 1: Directivity

For a uniform aperture, $\eta_{\text{ap}} = 1$, so $A_{\text{eff}} = A_{\text{phys}} = ab$.

$$
D_0 = \frac{4\pi}{\lambda^2} A_{\text{eff}} = \frac{4\pi}{\lambda^2} (10\lambda)(5\lambda) = \frac{4\pi}{\lambda^2} \cdot 50\lambda^2 = 200\pi \approx 628.3
$$

In dB: $D_0(\text{dB}) = 10\log_{10}(200\pi) \approx 28.0$ dBi.

#### Step 2: 3-dB beamwidths

$$
\Theta_{3\text{dB}}^{(x)} = 0.886 \frac{\lambda}{a} = 0.886 \frac{\lambda}{10\lambda} = 0.0886 \text{ rad} \approx 5.08^\circ
$$

$$
\Theta_{3\text{dB}}^{(y)} = 0.886 \frac{\lambda}{b} = 0.886 \frac{\lambda}{5\lambda} = 0.1772 \text{ rad} \approx 10.15^\circ
$$

#### Step 3: First-null beamwidths

The first null in the sinc pattern occurs at $u = 1$, where $u = (a/\lambda)\sin\theta$. For $\phi = 0^\circ$:

$$
\sin\theta_{\text{null}}^{(x)} = \frac{\lambda}{a} = \frac{1}{10} \quad \Rightarrow \quad \theta_{\text{null}}^{(x)} = 5.74^\circ
$$

The first-null beamwidth (FNBW) is $2\theta_{\text{null}}$:

$$
\text{FNBW}^{(x)} = 2 \times 5.74^\circ = 11.48^\circ
$$

Similarly:

$$
\sin\theta_{\text{null}}^{(y)} = \frac{\lambda}{b} = \frac{1}{5} \quad \Rightarrow \quad \theta_{\text{null}}^{(y)} = 11.54^\circ
$$

$$
\text{FNBW}^{(y)} = 2 \times 11.54^\circ = 23.08^\circ
$$

---

### Exercise 2: Circular Aperture Beamwidth and SLL

**Problem:** A uniformly illuminated circular aperture has a diameter $D = 20\lambda$.
1. Calculate the 3-dB beamwidth.
2. Calculate the Rayleigh resolution limit (first null).
3. Calculate the directivity.
4. Determine the angle and level of the first sidelobe.

**Solution:**

#### Step 1: 3-dB beamwidth

For a circular aperture, $\Theta_{3\text{dB}} = 1.02 \frac{\lambda}{D}$ rad (using diameter $D = 2a$).

More precisely: $\Theta_{3\text{dB}} = 0.5144 \frac{\lambda}{a} = 1.0288 \frac{\lambda}{D} = 1.0288 \frac{\lambda}{20\lambda} = 0.05144$ rad.

$$
\Theta_{3\text{dB}} = 0.05144 \text{ rad} \times \frac{180^\circ}{\pi} \approx 2.95^\circ
$$

#### Step 2: Rayleigh resolution limit

The first null occurs at $u = a\sin\theta/\lambda = 0.6098$:

$$
\sin\theta_{\text{null}} = \frac{0.6098\lambda}{a} = \frac{0.6098\lambda}{10\lambda} = 0.06098
$$

$$
\theta_{\text{null}} = 3.495^\circ
$$

The Rayleigh resolution limit (half of the first-null beamwidth for a point source) is:

$$
\Delta\theta = 1.22 \frac{\lambda}{D} = 1.22 \frac{\lambda}{20\lambda} = 0.061 \text{ rad} = 3.50^\circ
$$

#### Step 3: Directivity

$$
D_0 = \frac{4\pi}{\lambda^2} A = \frac{4\pi}{\lambda^2} (\pi a^2) = \frac{4\pi}{\lambda^2} \cdot \pi(10\lambda)^2 = 4\pi \cdot 100\pi = 400\pi^2 \approx 3948
$$

In dB: $D_0 = 10\log_{10}(400\pi^2) \approx 35.96$ dBi.

#### Step 4: First sidelobe

The first sidelobe occurs at $u = a\sin\theta/\lambda = 0.8174$:

$$
\sin\theta_{\text{sl}} = \frac{0.8174\lambda}{a} = \frac{0.8174\lambda}{10\lambda} = 0.08174
$$

$$
\theta_{\text{sl}} = 4.69^\circ
$$

The sidelobe level relative to the main beam:

$$
|2J_1(2\pi \times 0.8174)/(2\pi \times 0.8174)| = 0.1323
$$

In dB: $20\log_{10}(0.1323) \approx -17.56$ dB.

---

### Exercise 3: Aperture Efficiency and Taper Design

**Problem:** A rectangular aperture of dimensions $a = 8\lambda$, $b = 4\lambda$ has a cosine-tapered illumination in the $x$-direction and uniform in the $y$-direction:

$$
\mathbf{E}_a = \hat{y} E_0 \cos\left( \frac{\pi x}{a} \right), \quad |x| \le a/2, \; |y| \le b/2
$$

1. Calculate the aperture efficiency $\eta_{\text{ap}}$.
2. Compare the directivity to the uniform aperture case.
3. Estimate the change in 3-dB beamwidth in the H-plane.

**Solution:**

#### Step 1: Aperture efficiency

First compute the numerator of the efficiency expression:

$$
\left| \iint_A \mathbf{E}_a \, dS' \right|^2 = \left| E_0 \int_{-b/2}^{b/2} dy' \int_{-a/2}^{a/2} \cos\left( \frac{\pi x'}{a} \right) dx' \right|^2
$$

The $y$-integral gives $b$. The $x$-integral:

$$
\int_{-a/2}^{a/2} \cos\left( \frac{\pi x'}{a} \right) dx' = \frac{a}{\pi} \left[ \sin\left( \frac{\pi x'}{a} \right) \right]_{-a/2}^{a/2} = \frac{a}{\pi}(\sin(\pi/2) - \sin(-\pi/2)) = \frac{2a}{\pi}
$$

So the numerator is $|E_0 \cdot b \cdot 2a/\pi|^2 = \frac{4a^2 b^2 E_0^2}{\pi^2}$.

The denominator:

$$
A_{\text{phys}} \iint_A |\mathbf{E}_a|^2 \, dS' = (ab) \cdot E_0^2 \int_{-b/2}^{b/2} dy' \int_{-a/2}^{a/2} \cos^2\left( \frac{\pi x'}{a} \right) dx'
$$

The $y$-integral gives $b$. The $x$-integral:

$$
\int_{-a/2}^{a/2} \cos^2\left( \frac{\pi x'}{a} \right) dx' = \int_{-a/2}^{a/2} \frac{1}{2}\left(1 + \cos\left( \frac{2\pi x'}{a} \right)\right) dx' = \frac{a}{2}
$$

So the denominator is $(ab) \cdot E_0^2 \cdot b \cdot a/2 = a^2 b^2 E_0^2/2$.

Therefore:

$$
\eta_{\text{ap}} = \frac{4a^2 b^2 E_0^2 / \pi^2}{a^2 b^2 E_0^2 / 2} = \frac{8}{\pi^2} \approx 0.8106
$$

The aperture efficiency is approximately 81%.

#### Step 2: Directivity comparison

Uniform aperture: $D_{0,\text{uniform}} = 4\pi ab/\lambda^2 = 4\pi \cdot 8\lambda \cdot 4\lambda / \lambda^2 = 128\pi \approx 402.1$ (26.0 dBi).

Cosine-tapered aperture: $D_{0,\text{tapered}} = \eta_{\text{ap}} \cdot D_{0,\text{uniform}} = 0.8106 \times 402.1 \approx 325.9$ (25.1 dBi).

The tapered aperture has about 0.9 dB lower directivity.

#### Step 3: H-plane beamwidth change

For the cosine-tapered aperture, the H-plane 3-dB beamwidth is approximately:

$$
\Theta_{3\text{dB}}^{(H)} \approx 1.20 \frac{\lambda}{a} = 1.20 \frac{\lambda}{8\lambda} = 0.15 \text{ rad} \approx 8.6^\circ
$$

Compared to the uniform aperture: $\Theta_{3\text{dB}}^{(H,\text{uniform})} = 0.886\lambda/a = 0.1108 \text{ rad} \approx 6.35^\circ$.

The beamwidth increases by a factor of $1.20/0.886 \approx 1.35$ due to the cosine taper.

---

### Exercise 4: Fourier Transform Relationship — Aperture Size Scaling

**Problem:** An aperture antenna has a uniform field distribution over a rectangular aperture of dimensions $a = 5\lambda$, $b = 3\lambda$. If the aperture dimensions are doubled ($a = 10\lambda$, $b = 6\lambda$) while maintaining the same illumination, by what factor do the following change:
1. Directivity.
2. 3-dB beamwidth (in each principal plane).
3. Sidelobe level.

**Solution:**

#### Step 1: Directivity change

For a uniform aperture, $D_0 = 4\pi ab/\lambda^2 \propto ab$.

Original: $D_{0,1} = 4\pi(5\lambda)(3\lambda)/\lambda^2 = 60\pi$.

Doubled: $D_{0,2} = 4\pi(10\lambda)(6\lambda)/\lambda^2 = 240\pi$.

The directivity increases by a factor of $240\pi / 60\pi = 4$.

In dB: $10\log_{10}(4) = 6.02$ dB increase.

#### Step 2: Beamwidth change

Beamwidth scales inversely with aperture dimension:

$$
\Theta_{3\text{dB}}^{(x)} = 0.886 \frac{\lambda}{a} \propto \frac{1}{a}
$$

Original: $\Theta_{3\text{dB,1}}^{(x)} = 0.886/5 \approx 0.1772$ rad.
Doubled: $\Theta_{3\text{dB,2}}^{(x)} = 0.886/10 \approx 0.0886$ rad.

The beamwidth is halved. Similarly for the $y$-plane: original $0.886/3 \approx 0.2953$ rad, doubled $0.886/6 \approx 0.1478$ rad.

#### Step 3: Sidelobe level change

The sidelobe level of a uniformly illuminated rectangular aperture is determined by the sinc function pattern, which has a first sidelobe at $-13.26$ dB regardless of the aperture size. **Doubling the aperture dimensions does not change the sidelobe level.** The angular position of the sidelobe changes ($\theta_{\text{sl}} \propto 1/a$), but not the relative level.

---

### Exercise 5: Babinet's Principle — Slot Antenna Pattern

**Problem:** A narrow slot of length $L = \lambda/2$ and width $w \ll \lambda$ is cut in an infinite conducting plane. Using Babinet's principle, determine:
1. The radiation pattern of the slot.
2. The input impedance of the slot.
3. The directivity.

**Solution:**

#### Step 1: Pattern determination by duality

By Babinet's principle, the slot antenna is the dual of a dipole antenna of the same length. A half-wave dipole has a well-known pattern:

$$
\mathbf{E}_{\text{dipole}} \propto \frac{\cos(\pi\cos\theta/2)}{\sin\theta} \hat{\theta}
$$

The slot in a conducting plane radiates only into the half-space $z > 0$. By duality:

- The **E-plane** pattern of the slot corresponds to the **H-plane** pattern of the complementary dipole.
- The **H-plane** pattern of the slot corresponds to the **E-plane** pattern of the complementary dipole.

For the half-wave slot:
- E-plane ($\phi = 90^\circ$): omnidirectional in the half-space (constant with $\theta$).
- H-plane ($\phi = 0^\circ$): follows the dipole E-plane pattern:
  $$
  |E| \propto \frac{\cos(\pi\sin\theta/2)}{\cos\theta}
  $$

#### Step 2: Input impedance

The input impedance of a slot antenna and its complementary dipole are related by:

$$
Z_{\text{slot}} \cdot Z_{\text{dipole}} = \frac{\eta^2}{4}
$$

For a half-wave dipole, $Z_{\text{dipole}} \approx 73 + j42.5$ $\Omega$.

Therefore:

$$
Z_{\text{slot}} = \frac{\eta^2}{4Z_{\text{dipole}}} = \frac{(377)^2}{4(73 + j42.5)} = \frac{142129}{292 + j170} \approx \frac{142129}{338.7 \angle 30.2^\circ}
$$

$$
Z_{\text{slot}} \approx 419.6 \angle -30.2^\circ \approx 363 - j211 \; \Omega
$$

#### Step 3: Directivity

The half-wave slot radiates only into half-space, concentrating the same power into $2\pi$ steradians instead of $4\pi$. Therefore, the directivity of the slot is twice that of the complementary dipole:

$$
D_{\text{slot}} = 2 \times D_{\text{dipole}} = 2 \times 1.64 = 3.28 \approx 5.15 \text{ dBi}
$$

---

### Exercise 6: Edge Diffraction from a Finite Ground Plane

**Problem:** A slot antenna is centered in a square ground plane of side $W = 10\lambda$. The slot is $L = \lambda/2$ long. Estimate the effect of edge diffraction on the forward radiation pattern at $\theta = 60^\circ$ off boresight, using the knife-edge diffraction model.

**Solution:**

#### Step 1: Geometry and Fresnel parameter

The observation angle relative to the edge is approximately $\theta = 60^\circ$ (assuming the boresight is normal to the ground plane). The clearance distance from the edge to the line of sight depends on the geometry.

For an edge at distance $d = W/2 = 5\lambda$ from the antenna center, the Fresnel parameter $v$ is:

$$
v \approx \sqrt{\frac{2}{\lambda}} \cdot \text{clearance} \approx \sqrt{\frac{2}{\lambda}} \cdot d\sin\theta
$$

Wait — the appropriate Fresnel parameter for a distance $d$ to the edge and observation at angle $\theta$ is:

For a source-to-edge distance $d_1$ and edge-to-observation distance $d_2$, with the observation at angle $\theta$ from the normal:

The Fresnel parameter is:

$$
v = \sqrt{\frac{2}{\lambda F}} \cdot b
$$

where $F = d_1 d_2/(d_1 + d_2)$ and $b$ is the perpendicular distance from the line of sight to the edge.

#### Step 2: Simplified calculation

For large distances (far-field observation), the diffraction coefficient from the GTD model gives:

For $\theta = 60^\circ$:

$$
D_{\text{edge}} \approx \frac{1 - j}{2\sqrt{\pi k} \, \theta} = \frac{1 - j}{2\sqrt{\pi \cdot 2\pi/\lambda} \cdot (\pi/3)}
$$

$$
D_{\text{edge}} \approx \frac{1 - j}{2\pi\sqrt{2/\lambda} \cdot (\pi/3)} = \frac{3(1 - j)}{2\pi^2} \sqrt{\frac{\lambda}{2}}
$$

The relative diffracted field amplitude is:

$$
|D_{\text{edge}}| \approx \frac{3}{2\pi^2} \sqrt{\frac{\lambda}{2}} = \frac{3}{2\pi^2} \cdot 0.707\sqrt{\lambda} \approx 0.107\sqrt{\lambda}
$$

For $\lambda = 1$ (normalized), $|D_{\text{edge}}| \approx 0.107$ or approximately $-19.4$ dB relative to the direct field. This is a significant contribution that distorts the pattern at wide angles.

> **[Key Insight]** Edge diffraction from a finite ground plane limits the achievable front-to-back ratio and distorts the pattern at wide angles. For ground planes smaller than $10\lambda$, the distortion is severe enough that simple aperture models assuming an infinite ground plane become inaccurate.

---

### Exercise 7: Design of a Rectangular Aperture for Specified Beamwidth

**Problem:** Design a uniformly illuminated rectangular aperture to achieve a 3-dB beamwidth of $2^\circ$ in the $xz$-plane and $4^\circ$ in the $yz$-plane at a frequency of 10 GHz.
1. Determine the required aperture dimensions $a$ and $b$.
2. Calculate the directivity.
3. Determine the first-null beamwidths.

**Solution:**

#### Step 1: Aperture dimensions

At 10 GHz, $\lambda = c/f = 3\times 10^8 / 10^{10} = 0.03$ m = 3 cm.

Using the beamwidth formula $\Theta_{3\text{dB}} = 0.886\lambda/a$:

For $\Theta_{3\text{dB}}^{(x)} = 2^\circ = 0.03491$ rad:

$$
a = 0.886 \frac{\lambda}{\Theta_{3\text{dB}}^{(x)}} = 0.886 \frac{0.03}{0.03491} = 0.886 \times 0.8594 \approx 0.761 \text{ m}
$$

For $\Theta_{3\text{dB}}^{(y)} = 4^\circ = 0.06981$ rad:

$$
b = 0.886 \frac{\lambda}{\Theta_{3\text{dB}}^{(y)}} = 0.886 \frac{0.03}{0.06981} = 0.886 \times 0.4297 \approx 0.381 \text{ m}
$$

#### Step 2: Directivity

$$
D_0 = \frac{4\pi}{\lambda^2} ab = \frac{4\pi}{(0.03)^2} (0.761)(0.381) = \frac{4\pi}{0.0009} \times 0.290
$$

$$
D_0 = \frac{4\pi \times 0.290}{0.0009} \approx 4050
$$

In dB: $D_0 = 10\log_{10}(4050) \approx 36.1$ dBi.

#### Step 3: First-null beamwidths

The first null occurs at $\sin\theta_{\text{null}} = \lambda/a$:

For the $xz$-plane:

$$
\sin\theta_{\text{null}}^{(x)} = \frac{0.03}{0.761} = 0.03942 \quad \Rightarrow \quad \theta_{\text{null}}^{(x)} = 2.26^\circ
$$

$$
\text{FNBW}^{(x)} = 2 \times 2.26^\circ = 4.52^\circ
$$

For the $yz$-plane:

$$
\sin\theta_{\text{null}}^{(y)} = \frac{0.03}{0.381} = 0.07874 \quad \Rightarrow \quad \theta_{\text{null}}^{(y)} = 4.52^\circ
$$

$$
\text{FNBW}^{(y)} = 2 \times 4.52^\circ = 9.04^\circ
$$

---

### Exercise 8: Comparison of Circular and Rectangular Apertures

**Problem:** Compare a circular aperture of radius $a = 5\lambda$ with a square aperture of side $a = 5\lambda$, both uniformly illuminated.
1. Which has higher directivity and by how much?
2. Which has a narrower beamwidth?
3. Which has lower sidelobes?

**Solution:**

#### Step 1: Directivity comparison

**Circular:** $D_{\text{circ}} = 4\pi A/\lambda^2 = 4\pi(\pi a^2)/\lambda^2 = 4\pi^2 a^2/\lambda^2$.

With $a = 5\lambda$: $D_{\text{circ}} = 4\pi^2(25\lambda^2)/\lambda^2 = 100\pi^2 \approx 986.96$.

In dB: $D_{\text{circ}} = 10\log_{10}(100\pi^2) \approx 29.94$ dBi.

**Square:** $D_{\text{sq}} = 4\pi a^2/\lambda^2 = 4\pi(25\lambda^2)/\lambda^2 = 100\pi \approx 314.16$.

In dB: $D_{\text{sq}} = 10\log_{10}(100\pi) \approx 24.97$ dBi.

The circular aperture has $986.96/314.16 \approx 3.14$ times higher directivity (about 4.97 dB more). However, this comparison is misleading because the circular aperture has area $\pi a^2$ while the square has area $a^2$. For the same **radius**/side length, the circular aperture has $3.14$ times more area.

**Fair comparison — same physical area:**

For a circular aperture with area $A = 25\lambda^2$: $a = \sqrt{A/\pi} = \sqrt{25/\pi} \approx 2.82\lambda$.

$D_{\text{circ, equal area}} = 4\pi A/\lambda^2 = 4\pi \cdot 25 = 100\pi \approx 314.16$ (same as the square).

For equal physical area, the directivity is identical for uniform illumination, since $D_0 = 4\pi A/\lambda^2$ regardless of shape.

#### Step 2: Beamwidth comparison

**Square (for equal area $A = 25\lambda^2$, side $a = 5\lambda$):**

$\Theta_{3\text{dB,sq}} = 0.886\lambda/a = 0.886/5 = 0.1772$ rad $\approx 10.15^\circ$.

**Circular (for equal area, $a \approx 2.82\lambda$):**

$\Theta_{3\text{dB,circ}} = 0.5144\lambda/a = 0.5144/2.82 \approx 0.1824$ rad $\approx 10.45^\circ$.

For equal area, the square aperture has a slightly narrower beamwidth in one principal plane, but the circular aperture produces a circularly symmetric pattern with nearly the same beamwidth.

#### Step 3: Sidelobe comparison

**Square aperture:** First sidelobe level depends on the plane. In the principal planes, SLL $= -13.26$ dB (from the sinc pattern). In the diagonal plane ($\phi = 45^\circ$), the product of two sinc functions produces a lower effective SLL.

**Circular aperture:** First sidelobe level is $-17.56$ dB — lower than the square aperture's $-13.26$ dB. The circular aperture has inherently lower sidelobes due to the Bessel function pattern which exhibits faster amplitude decay away from the main beam.

---

### Exercise 9: Fourier Transform and Pattern Synthesis

**Problem:** An aperture has the following field distribution (one-dimensional case):

$$
E_a(x) = E_0 \left[ 1 - \left( \frac{2x}{a} \right)^2 \right], \quad |x| \le a/2
$$

1. Find the far-field pattern (normalized).
2. Determine the first sidelobe level.
3. Compare with the uniform aperture case.

**Solution:**

#### Step 1: Far-field pattern

The far-field pattern is the Fourier transform of the aperture distribution (ignoring the obliquity factor):

$$
F(u) = \int_{-a/2}^{a/2} E_a(x) e^{jkx\sin\theta} \, dx
$$

Let $u = (a/\lambda)\sin\theta$, $p = x/a$, $k\sin\theta = 2\pi u/a$:

$$
F(u) = E_0 a \int_{-1/2}^{1/2} (1 - 4p^2) e^{j2\pi u p} \, dp
$$

The integral can be evaluated as:

$$
F(u) = E_0 a \left[ \int_{-1/2}^{1/2} e^{j2\pi u p} dp - 4 \int_{-1/2}^{1/2} p^2 e^{j2\pi u p} dp \right]
$$

First integral: $\frac{\sin(\pi u)}{\pi u}$.

Second integral (using integration by parts): results in $\frac{\sin(\pi u)}{\pi u} \cdot \frac{1}{\pi^2 u^2} \left( 1 - \frac{\pi^2 u^2}{2} \right) - \frac{3\cos(\pi u)}{2\pi^2 u^2}$.

The full expression simplifies to:

$$
F(u) = E_0 a \cdot \frac{3\sin(\pi u)}{(\pi u)^3} \left[ 1 - (\pi u)^2 \right] \quad \text{(this is approximate — the full form involves spherical Bessel functions)}
$$

Equivalently, the normalized pattern function is:

$$
\bar{f}(u) = \frac{3}{(\pi u)^2} \left( \frac{\sin(\pi u)}{\pi u} - \cos(\pi u) \right)
$$

#### Step 2: First sidelobe level

The first sidelobe of this parabolic taper distribution occurs at approximately $u \approx 1.43$:

$$
|\bar{f}(1.43)| \approx 0.050
$$

In dB: $20\log_{10}(0.050) \approx -26.0$ dB.

#### Step 3: Comparison with uniform aperture

| Parameter | Uniform | Parabolic Taper |
|:---|:---:|:---:|
| First SLL | $-13.26$ dB | $-26.0$ dB |
| 3-dB beamwidth factor | $0.886\lambda/a$ | $\approx 1.15\lambda/a$ |
| Aperture efficiency | 100% | $\approx 75$% |

The parabolic taper reduces sidelobes by about 12.7 dB compared to the uniform aperture, at the cost of a broader main beam (about 30% wider) and lower aperture efficiency.

---

### Exercise 10: Gain-Bandwidth Product of an Aperture Antenna

**Problem:** An aperture antenna operating at 10 GHz has a 3-dB beamwidth of $3^\circ$ in both principal planes (a pencil beam). The system requires the antenna to scan $\pm 20^\circ$ from boresight.
1. Estimate the required aperture size.
2. Estimate the gain.
3. If a sidelobe level of $-30$ dB is required, what taper efficiency is needed and how does this affect the gain?

**Solution:**

#### Step 1: Aperture size

For a uniformly illuminated rectangular aperture with equal beamwidths in both planes:

$$
\Theta_{3\text{dB}} = 0.886\frac{\lambda}{a} = 3^\circ = 0.05236 \text{ rad}
$$

$$
a = 0.886 \frac{\lambda}{\Theta_{3\text{dB}}} = 0.886 \frac{0.03}{0.05236} = 0.508 \text{ m}
$$

Since both beamwidths are equal, $a = b = 0.508$ m. The aperture is approximately $0.508/0.03 \approx 17\lambda$ on each side.

#### Step 2: Gain estimate

For uniform illumination:

$$
G_0 \approx D_0 = \frac{4\pi}{\lambda^2} A = \frac{4\pi}{(0.03)^2} (0.508)^2 = \frac{4\pi}{0.0009} \times 0.258
$$

$$
G_0 \approx \frac{4\pi \times 0.258}{0.0009} \approx 3603 \approx 35.6 \text{ dBi}
$$

Using the gain-beamwidth product formula:

$$
G = \frac{32400}{\Theta_{3\text{dB}}^{(x)} \Theta_{3\text{dB}}^{(y)}} = \frac{32400}{3 \times 3} = 3600
$$

This confirms the calculation. (The constant 32400 applies when beamwidths are in degrees.)

#### Step 3: Taper for $-30$ dB sidelobes

To achieve $-30$ dB sidelobes, a significant taper is needed. A Taylor distribution with $-30$ dB design level has an efficiency of approximately 95--98%, depending on the $\bar{n}$ parameter.

The gain reduction factor is approximately the aperture efficiency. Using $\eta_{\text{ap}} \approx 0.96$:

$$
G_{\text{tapered}} = 0.96 \times 3603 \approx 3459 \approx 35.4 \text{ dBi}
$$

The gain loss is only about $10\log_{10}(0.96) \approx 0.18$ dB — a very modest reduction for achieving $-30$ dB sidelobes.

> **[Key Insight]** The gain penalty for sidelobe reduction through aperture tapering is surprisingly small (typically less than 1 dB for designs down to $-40$ dB SLL). This is because the taper reduces the effective area mainly at the outer edges where the directivity contribution is already small. The beamwidth broadens more noticeably than the gain decreases.

---

## Connections and Cross-References

- **Section 2 (Fundamental Parameters of Antennas):** The definitions of directivity, gain, beamwidth, polarization, and effective area are essential for characterizing aperture antennas. The Friis transmission equation (Section 2.q) relates aperture effective area to received power.
- **Section 3 (Radiation Integrals):** The vector potential method and far-field approximations developed in Section 3 are directly applied in the aperture radiation equations.
- **Section 4 (Linear Wire Antennas):** The infinitesimal dipole is the elementary radiator used in equivalence principle derivations. The half-wave dipole serves as the dual of the half-wave slot via Babinet's principle.
- **Section 6 (Arrays):** Aperture antennas can be viewed as continuous arrays of infinitesimal Huygens sources. The Fourier transform relationship in aperture theory is the continuous analogue of the array factor formulation.
- **Section 11 (Frequency Independent Antennas):** Spiral antennas are sometimes used as feeds for reflector apertures. The log-periodic dipole array shares the LPDA terminology with certain aperture designs.
- **Section 13 (Horn Antennas):** Horn antennas are the most common implementation of aperture antennas, providing a transition from waveguide to free space.
- **Section 15 (Reflector Antennas):** Reflector antennas use the aperture field method for pattern analysis, where the reflector creates a large effective aperture from a small feed.

*Prerequisites: Section 2 (Fundamental Parameters) — directivity, gain, polarization. Section 3 (Radiation Integrals) — vector potentials, far-field approximation.*

---

## Exam Tip: Aperture Antennas

1. **Fourier Transform Pair:** The far-field pattern is the Fourier transform of the aperture field. A uniform distribution (rectangular function in space) produces a sinc pattern in angle. A Gaussian distribution produces a Gaussian pattern (no sidelobes). A cosine taper lowers sidelobes from $-13.26$ dB to $-23$ dB.

2. **Beamwidth Formula:** For a uniformly illuminated rectangular aperture, the 3-dB beamwidth in one principal plane is $\Theta_{3\text{dB}} \approx 0.886\lambda/L$ (in radians), where $L$ is the aperture dimension in that plane. For a circular aperture, $\Theta_{3\text{dB}} \approx 1.02\lambda/D$ (where $D$ is the diameter).

3. **Aperture Efficiency:** The maximum directivity is $D_0 = 4\pi A_{\text{phys}}/\lambda^2$ only for uniform illumination. Any taper reduces the directivity. The aperture efficiency $\eta_{\text{ap}}$ equals the ratio of the effective area to the physical area.

4. **Babinet's Principle Shortcut:** The radiation pattern of a slot is the same as that of the complementary dipole with E and H swapped. The input impedance of the slot is $\eta^2/(4Z_{\text{dipole}})$. A half-wave slot has approximately $363 - j211$ $\Omega$ impedance, which is much higher than a half-wave dipole's $73 + j42.5$ $\Omega$.

5. **Circular vs. Rectangular:** For the same physical area, a rectangular aperture produces a narrower beam in one principal plane (the longer dimension) and a wider beam in the other. A circular aperture produces a rotationally symmetric pattern. The circular aperture has inherently lower sidelobes ($-17.56$ dB vs. $-13.26$ dB) for uniform illumination.

6. **Phase Errors:** A quadratic phase error across the aperture (as in a horn antenna) reduces directivity and fills in the nulls. The phase error efficiency is $\eta_p = 1 - \frac{\pi^2}{6} \left( \frac{\Delta\phi}{\pi} \right)^2$ for small phase errors, where $\Delta\phi$ is the peak phase deviation.

7. **Edge Effects:** Finite ground planes produce edge diffraction that modifies the pattern, especially at wide angles. The diffraction is strongest in the plane perpendicular to the edge (the Keller cone). The GTD provides a systematic framework for incorporating these effects.

8. **Rayleigh Resolution Limit:** The minimum angular separation that can be resolved by a circular aperture (the Rayleigh criterion) is $\Delta\theta = 1.22\lambda/D$, where $D$ is the aperture diameter. This is the first null of the Airy pattern.

---

*This file covers Section 12 (Aperture Antennas) as listed in the Signal Propagation mindmap, following the Type C (Engineering and Applied Science) content standard with 10 fully worked exercises spanning directivity calculations, beamwidth design, pattern synthesis, Babinet's principle, edge diffraction, and comparative analysis of different aperture configurations.*