# Horn Antennas

Horn antennas are a class of aperture antennas formed by flaring a waveguide end, producing a gradual impedance transition between the guided electromagnetic mode and free space. They are among the most widely used antennas at microwave frequencies (above 300 MHz) due to their high gain, low VSWR, broad bandwidth, and straightforward construction. Horn antennas serve as feed elements for reflector antennas, as standard gain references for antenna measurements, and as directive radiators in radar, satellite communication, and microwave relay systems. This section covers the principal types of horn antennas---E-plane sectoral, H-plane sectoral, pyramidal, conical, corrugated, aperture-matched, multimode, and dielectric-loaded---along with their design principles, radiation characteristics, and the concept of phase center.

*Prerequisite: Section 12 (Aperture Antennas) for the field equivalence principle and Fourier transform methods.*

---

## 1. Conceptual Foundation

### 1.1 The Horn Antenna Concept

A horn antenna is a flared section of a waveguide that provides a gradual impedance transition from the waveguide interior to free space. Without the flare, an open-ended waveguide suffers from an abrupt impedance discontinuity (from the waveguide impedance to the free-space impedance of approximately $377\;\Omega$), which causes significant reflection of incident energy back toward the source. The flared geometry acts as an impedance-matching transformer, analogous to a tapered transmission line, allowing most of the incident field to radiate into free space with minimal reflection.

The horn shape also reduces edge diffraction compared to an open waveguide: the wider aperture projects the radiated field into a narrower beam. The practical aperture size of horns is limited to approximately $15\lambda$ because larger apertures require impractically long horns to maintain acceptable phase error, which restricts the maximum gain of practical horns to about $30\;\text{dBi}$ and the minimum beamwidth to approximately $5^\circ$--$10^\circ$.

### 1.2 Historical Development

The first horn antenna was constructed in 1897 by Jagadish Chandra Bose in his pioneering experiments with microwaves. The modern horn antenna was invented independently in 1938 by Wilmer Barrow and G. C. Southworth. The development of radar during World War II stimulated extensive horn research for radar feed applications. The corrugated horn, invented by Kay in 1962, became widely used as a feed horn for satellite dishes and radio telescopes.

### 1.3 Why Horns Are Preferred at Microwave Frequencies

- **Gain scales with frequency:** Directivity is proportional to $A/\lambda^2$, where $A$ is the aperture area; at high frequencies, electrically large apertures are physically compact.
- **Broad bandwidth:** Horns have no resonant elements and can operate over bandwidths of 10:1 or more.
- **Low loss and low VSWR:** The gradual flare provides excellent impedance matching, resulting in low VSWR across the operating band.
- **Simple construction:** Straight-sided horns (pyramidal, conical) have simple geometries that are easy to fabricate.
- **Compatibility with waveguide feeds:** Horns integrate naturally with rectangular or circular waveguide transmission lines.

---

## 2. Formal Definition and Model

### 2.1 The Optimum Horn

For a given frequency and horn length, there exists a flare angle that maximizes gain and minimizes reflection. Reflection occurs at two locations: the aperture (mouth) of the horn and the throat (where the flare begins).

- **Narrow horns** (small flare angle): Most reflection occurs at the mouth; gain is low because the small aperture approximates an open-ended waveguide.
- **Wide horns** (flare angle approaching $90^\circ$): Most reflection occurs at the throat; gain is again low.

The **optimum horn** is the specific flare angle that balances these two effects, producing maximum gain and minimum reflection. Most practical horns are designed as optimum horns.

> **[Supplementary]** The optimal dimensions for a pyramidal horn satisfy:

$$
a_E = \sqrt{2\lambda L_E}, \qquad a_H = \sqrt{3\lambda L_H}
$$

where $a_E$ and $a_H$ are the E-plane and H-plane aperture dimensions, and $L_E$ and $L_H$ are the respective apex lengths. For a conical horn:

$$
d = \sqrt{3\lambda L}
$$

where $d$ is the aperture diameter and $L$ is the slant length. Note that an optimum horn gives maximum gain for a given *length*, not for a given *aperture size*.

### 2.2 Gain of Optimum Horns

The gain $G$ of a pyramidal horn antenna is:

$$
G = \frac{4\pi A}{\lambda^2} e_A
$$

where $A$ is the physical aperture area and $e_A$ is the aperture efficiency. For optimum pyramidal horns, $e_A \approx 0.511$.

For conical horns:

$$
G = \left(\frac{\pi d}{\lambda}\right)^2 e_A
$$

where $d$ is the horn aperture diameter and $e_A \approx 0.522$ for optimum designs.

> **[Supplementary]** The aperture efficiency ranges from $0.4$ to $0.8$ in practical horn antennas. The optimum total aperture efficiency of a pyramidal horn is the product of the taper efficiency and the phase aperture efficiency: $0.81 \times 0.632 = 0.511$.

### 2.3 Phase Error and Beamwidth

The waves traveling through a horn arrive at the aperture as spherical wavefronts, with their origin at the apex of the horn (the **phase center**). Because the spherical wavefronts are not planar, the phase varies across the aperture, increasing from the center toward the edges. This variation is the **phase error**.

The phase error increases with the flare angle and limits the useful aperture size. As the horn size (in wavelengths) increases, the phase error increases, giving a wider radiation pattern. Maintaining a narrow beamwidth requires a longer horn (smaller flare angle) to keep the phase error constant.

---

## 3. E-Plane Sectoral Horn

The E-plane sectoral horn is flared in the direction of the electric field (E-plane), while the H-plane remains at the waveguide width. This produces a fan-shaped beam: narrow in the E-plane, wide in the H-plane.

### 3.1 Geometry and Parameters

The E-plane sectoral horn has the following key parameters:

| Parameter | Symbol | Description |
|-----------|--------|-------------|
| Aperture height | $B$ | Flared dimension in the E-plane |
| Waveguide width | $a$ | Unflared dimension (same as waveguide) |
| Waveguide height | $b$ | Original waveguide height |
| Slant length | $R_E$ | Distance from apex to aperture plane |
| Apex length | $R_0$ | Distance from apex to flared section start |
| Flare angle | $\alpha_E$ | Angle of flared walls in the E-plane |

The relationship between these parameters:

$$
R_E = \sqrt{R_0^2 + \left(\frac{B}{2}\right)^2}, \qquad \alpha_E = \arctan\frac{B}{2R_0}
$$

### 3.2 Aperture Field Distribution

The field at the aperture of an E-plane sectoral horn is approximated as:

$$
E_x \approx E_0 \frac{\cos\left(\frac{\pi y}{b}\right)}{a} e^{-j\frac{\beta}{2R_0} y^2}
$$

where $\beta = 2\pi/\lambda_0$ is the free-space phase constant. The quadratic phase factor $e^{-j\frac{\beta}{2R_0} y^2}$ arises from the difference in path length from the apex to the center and edges of the aperture.

### 3.3 Directivity

The directivity of the E-plane sectoral horn is:

$$
D_E = \frac{32}{4\pi} \frac{aB}{\lambda^2} e_t e_{ph}^E
$$

where $e_t = \pi^2/8$ (taper efficiency) and $e_{ph}^E$ is the phase efficiency expressed in terms of Fresnel integrals. The optimum directivity is achieved when $B = \sqrt{2\lambda R_0}$, yielding $e_{ph}^E \approx 0.8$.

---

## 4. H-Plane Sectoral Horn

The H-plane sectoral horn is flared in the direction of the magnetic field (H-plane), while the E-plane remains at the waveguide height.

### 4.1 Geometry and Parameters

| Parameter | Symbol | Description |
|-----------|--------|-------------|
| Aperture width | $A$ | Flared dimension in the H-plane |
| Waveguide height | $b$ | Unflared dimension (same as waveguide) |
| Slant length | $R_H$ | Distance from apex to aperture plane |
| Apex length | $R_0$ | Distance from apex to flared section start |
| Flare angle | $\alpha_H$ | Angle of flared walls in the H-plane |

$$
R_H = \sqrt{R_0^2 + \left(\frac{A}{2}\right)^2}, \qquad \alpha_H = \arctan\frac{A}{2R_0}
$$

### 4.2 Aperture Field Distribution

The field at the aperture of an H-plane sectoral horn is approximated as:

$$
E_y \approx E_0 \cos\left(\frac{\pi x}{a}\right) e^{-j\frac{\beta}{2R_0} x^2}
$$

The H-plane pattern is influenced by both the cosine taper (amplitude distribution) and the quadratic phase error. The E-plane pattern is that of a slit of width $b$ (uniform phase and amplitude in the E-plane).

### 4.3 Directivity

The directivity of the H-plane sectoral horn is:

$$
D_H = \frac{32}{\pi^2} \frac{bA}{\lambda^2} e_t e_{ph}^H
$$

The optimum directivity is achieved when $A = \sqrt{3\lambda R_0}$, which corresponds to $e_{ph}^H \approx 0.79$.

---

## 5. Pyramidal Horn

The pyramidal horn is the most popular horn type at microwave frequencies (1--30 GHz). It flares in both the E-plane and H-plane simultaneously, combining the results of the E-plane and H-plane sectoral horns.

### 5.1 Geometry and Parameters

| Parameter | Symbol | Description |
|-----------|--------|-------------|
| Aperture width | $A$ | Flared dimension in the H-plane |
| Aperture height | $B$ | Flared dimension in the E-plane |
| Waveguide width | $a$ | Input waveguide width |
| Waveguide height | $b$ | Input waveguide height |
| Apex length (H-plane) | $R_H$ | From apex to aperture (H-plane) |
| Apex length (E-plane) | $R_E$ | From apex to aperture (E-plane) |
| Slant length | $R$ | Common apex length ($R_H = R_E = R$) |

### 5.2 Aperture Field Distribution

The field at the aperture is approximated as:

$$
E_x \approx E_0 \cos\left(\frac{\pi x}{a}\right) e^{-j\frac{\beta x^2}{2R_H}} e^{-j\frac{\beta y^2}{2R_E}}
$$

The principal-plane patterns of a pyramidal horn are the same as those of the E-plane and H-plane sectoral horns, respectively.

### 5.3 Directivity

The directivity of the pyramidal horn is found by introducing the phase efficiency factors of both planes and the taper efficiency of the H-plane:

$$
D_P = \frac{4\pi}{\lambda^2} AB \, e_t \, e_{ph}^H \, e_{ph}^E
$$

The optimum pyramidal horn has total aperture efficiency:

$$
e_{ap} = e_t \cdot e_{ph}^H \cdot e_{ph}^E \approx 0.511
$$

> **[Key Insight]** The best achievable directivity for a rectangular waveguide horn is about half that of a uniform rectangular aperture.

### 5.4 Optimum Design Procedure

For a horn of known axial length $R_0$:

1. Compute $A$ from $A = \sqrt{3\lambda R_0}$.
2. Compute $B$ from $B = \sqrt{2\lambda R_0}$.
3. Calculate gain $G$ using $G = \frac{4\pi AB}{\lambda^2} \times 0.511$.

For a desired gain $G$, the design reduces to solving a fourth-order polynomial equation in $A$, derived from the constraint $R_H = R_E$ and the optimum gain conditions.

### 5.5 Pattern Characteristics

The E-plane pattern of a pyramidal horn typically has high side lobes and a large back lobe due to strong edge diffraction at the aperture edges perpendicular to the E-field. The H-plane pattern is generally superior (smoother, lower side lobes) because the boundary conditions force a null field at the edges perpendicular to the H-field.

---

## 6. Conical Horn

The conical horn is the circular-waveguide equivalent of the pyramidal horn. It produces a symmetric beam (equal E-plane and H-plane patterns) and is the natural choice for circular-waveguide systems, satellite feeds, and applications requiring a rotationally symmetric pattern.

### 6.1 Geometry and Parameters

| Parameter | Symbol | Description |
|-----------|--------|-------------|
| Aperture diameter | $d$ | Flared circular aperture dimension |
| Slant length | $L$ | From apex to aperture plane |
| Flare angle | $\alpha$ | Full angle of the cone |
| Waveguide radius | $a$ | Input circular waveguide radius |

$$
L = \sqrt{R_0^2 + \left(\frac{d}{2}\right)^2}, \qquad \alpha = 2\arctan\frac{d}{2R_0}
$$

### 6.2 Gain and Aperture Efficiency

For a conical horn, the gain is:

$$
G = \left(\frac{\pi d}{\lambda}\right)^2 e_A
$$

For optimum conical horns, $e_A \approx 0.522$, which is slightly higher than the pyramidal optimum due to better phase uniformity in the circular cross-section.

### 6.3 Radiation Pattern

For a uniform circular aperture, the far-field pattern is:

$$
f(\theta) = \frac{J_1(u)}{u}, \qquad u = \beta a \sin\theta
$$

where $J_1(\cdot)$ is a Bessel function of the first kind of order one. The half-power beamwidth for large apertures is:

$$
\text{HPBW} \approx 2\arcsin\frac{1.6}{\beta a} \approx \frac{58.4}{(2a/\lambda)} \;\text{deg}
$$

---

## 7. Corrugated Horn

The corrugated horn uses circumferential grooves (corrugations) cut into the interior walls of the horn to modify the boundary conditions. These corrugations force the field to support the hybrid HE$_{11}$ mode, which has nearly identical E-plane and H-plane patterns, extremely low cross-polarization (below $-30\;\text{dB}$), and low sidelobe levels (below $-25\;\text{dB}$).

### 7.1 Operating Principle

The corrugations on the interior walls of the horn create a capacitive surface impedance. The key boundary condition is that the tangential electric field is not forced to zero at the horn walls (as in smooth-walled horns), but instead has a finite value that depends on the corrugation depth.

When the corrugations are approximately $\lambda/4$ deep, the surface impedance is capacitive, which allows the TE$_{11}$ and TM$_{11}$ modes to couple and form the hybrid HE$_{11}$ mode. This mode provides:

- Symmetric E-plane and H-plane patterns.
- Low cross-polarization.
- Low sidelobe levels.

### 7.2 Key Parameters and Performance

| Parameter | Smooth Conical | Corrugated Conical |
|-----------|----------------|-------------------|
| Aperture efficiency | $\approx 0.52$ | $0.70$--$0.80$ |
| Cross-polarization | $-15$ to $-20\;\text{dB}$ | $< -30\;\text{dB}$ |
| Sidelobe level | $\sim -20\;\text{dB}$ | $< -25\;\text{dB}$ |
| Typical bandwidth | $50\%$ | Up to 2:1 |
| Beam symmetry | Moderate | Excellent |

### 7.3 Design Considerations

- **Corrugation depth:** Between $\lambda/4$ and $\lambda/2$ (typical choice is $0.43\lambda$ at the center frequency for optimal impedance match).
- **Number of corrugations per wavelength:** More than 5 (typically 8--15 per wavelength).
- **Corrugation spacing:** Below $0.1\lambda$ at the highest operating frequency.
- **Total number of corrugations:** Should be sufficient for mode purity; empirical results suggest at least 15--20 total corrugations for symmetrical beam patterns.

> **[Key Insight]** The corrugated horn is the standard feed for Cassegrain and Gregorian reflector antennas in satellite earth stations and radio telescopes. The low cross-polarization is critical for dual-polarization systems requiring polarization isolation of $30\;\text{dB}$ or more.

---

## 8. Aperture-Matched Horns

The aperture-matched horn eliminates troublesome edge diffractions by attaching curved surface sections to the aperture edges. These curved sections form a smooth transition between the horn modes and free-space, reducing the diffraction at the aperture edges.

### 8.1 Operating Principle

In a conventional horn, the E-plane pattern is dominated by three terms: direct throat radiation plus two aperture edge diffraction terms. The aperture-matched horn reduces the magnitude of the diffraction coefficient by modifying the geometry at the aperture edges, rather than reducing the field incident on the edges (as with corrugated or dual-mode horns).

The curved sections can be elliptic cylinder sections, quarter-cylinder sections, or arbitrary smooth convex shapes attached to the aperture edges so that the junction forms a smooth surface.

### 8.2 Performance Comparison

| Parameter | Conventional | Aperture-Matched | Corrugated |
|-----------|-------------|-----------------|------------|
| E-plane pattern | Multiple sidelobes, large back lobe | Smooth, low back lobe | Symmetric, low back lobe |
| Back lobe level | $-20$ to $-30\;\text{dB}$ | $-35$ to $-60\;\text{dB}$ | $-35$ to $-60\;\text{dB}$ |
| Bandwidth | As designed | Up to 2:1 | Up to 1.7:1 |
| Cross-polarization | $-15$ to $-20\;\text{dB}$ | $-15$ to $-20\;\text{dB}$ | $< -30\;\text{dB}$ |
| VSWR (with throat matching) | 1.5--2.0 | $\leq 1.2$ | $\leq 1.2$ |

> **[Supplementary]** The curved surface sections can be attached as a retrofit to improve the electromagnetic performance of virtually any horn. The modification increases size and weight, but this can be minimized using quadrant sections.

---

## 9. Multimode Horns

Multimode horns deliberately excite higher-order modes in addition to the fundamental mode to create a tapered aperture field that produces symmetric, low-sidelobe, low-cross-polarization radiation patterns.

### 9.1 Operating Principle

A multimode horn is designed so that a higher-order mode is generated within the horn (usually by a step discontinuity). The two modes are adjusted in amplitude and phase so that they sum constructively at the aperture center and cancel at the aperture edges, producing a tapered distribution.

The most common example is the **Potter horn** (circular waveguide), which uses the TE$_{11}$ and TM$_{11}$ modes. A step discontinuity in the throat generates the TM$_{11}$ mode, and the horn length is adjusted so that the two modes have the correct relative amplitude and phase at the aperture.

### 9.2 Key Parameters

| Parameter | Typical Value | Description |
|-----------|---------------|-------------|
| TM$_{11}$ mode amplitude | Equal to TE$_{11}$ amplitude | Required for optimal taper |
| Differential phase shift | $0.84\lambda$--$1.84\lambda$ | From step to aperture |
| Flare angle | $5^\circ$--$15^\circ$ | Typically small for compact designs |
| Bandwidth | $5\%$--$10\%$ | Narrower than corrugated horn |

### 9.3 Comparison with Corrugated Horns

| Feature | Corrugated Horn | Multimode Horn (Potter) |
|---------|-----------------|------------------------|
| Bandwidth | Up to 2:1 | $5\%$--$10\%$ |
| Pattern symmetry | Excellent over full band | Excellent in narrow band |
| Cross-polarization | $< -30\;\text{dB}$ | $< -30\;\text{dB}$ (narrow band) |
| Complexity | Moderate (corrugated structure) | Low (smooth walls) |
| Size | Compact | Longer than corrugated |

---

## 10. Dielectric-Loaded Horns

Dielectric-loaded horns use dielectric material inside the horn to shape the aperture field and improve performance characteristics such as gain, beamwidth, and cross-polarization.

### 10.1 Operating Principle

A dielectric loading insert modifies the boundary conditions at the walls. By controlling the dielectric constant and thickness, the aperture field distribution can be equalized, improving aperture efficiency.

### 10.2 Design Considerations

- **Dielectric constant $\epsilon_r$:** Typically between $1.2$ and $10$, depending on the application.
- **Thickness:** Determined by the operating frequency and required phase correction.
- **Loss:** Dielectric loading introduces dielectric losses, which must be kept low for high-efficiency applications.

> **[Supplementary]** Dielectric-loaded horns are often used in millimeter-wave applications (above $30\;\text{GHz}$), where metallic walls become more difficult to fabricate with high precision. They also find application as radiometer antennas, where high aperture efficiency and low sidelobes are required.

---

## 11. Phase Center

The **phase center** is the point from which the radiated field appears to emanate as a spherically expanding wavefront. For horn antennas, the phase center is a fixed location determined by the horn geometry and operating frequency, and its position must be known when the horn is used as a feed for reflector antennas.

### 11.1 Definition

For a horn antenna, the phase center is the point $O_{pc}$ from which the far-field radiation pattern has a spherical (constant-phase) wavefront over the main beam region. The phase center is typically located near the apex of the horn.

### 11.2 Characteristics by Horn Type

- **Smooth-walled pyramidal horn:** The phase center is located near the apex, typically $0.2\lambda$ to $0.5\lambda$ behind the aperture, and varies with frequency.
- **Corrugated horn:** The phase center is more stable and moves from near the aperture toward the apex as frequency increases.
- **E-plane sectoral horn:** The phase center is closer to the aperture than the apex.
- **H-plane sectoral horn:** The phase center is at the apex for the dominant mode.

> **[Supplementary]** The phase center can be determined by analyzing the phase of the far-field pattern at various angles. If the radiated field at angle $\theta$ has a phase $\phi(\theta)$, the phase center is the point such that the phase remains constant over the main beam. For corrugated horns, the phase center variation can be as low as $0.1\lambda$ over an octave bandwidth.

---

## 12. Key Parameters and Constraints

### 12.1 Comparative Performance Summary

| Horn Type | Aperture Efficiency | Cross-Pol | Beam Shape | Primary Application |
|-----------|-------------------|-----------|------------|-------------------|
| **Pyramidal** | $\sim 51\%$ | $-15$ to $-20\;\text{dB}$ | Elliptical pencil | Calibration, gain standards, lab measurements |
| **Conical** | $\sim 52\%$ | $-15$ to $-20\;\text{dB}$ | Circular pencil | Satellite feeds, circular waveguide systems |
| **Corrugated** | $70$--$80\%$ | $< -30\;\text{dB}$ | Symmetric pencil | Reflector feeds, radio telescopes, dual-pol systems |
| **Sectoral (E/H)** | $40$--$50\%$ | $-10$ to $-15\;\text{dB}$ | Fan beam | Shaped coverage, direction finding, 1D scanning |

### 12.2 Waveguide Bands and Typical Gain

| Waveguide | Frequency Range | Typical Horn Gain (opt.) |
|-----------|----------------|------------------------|
| WR-284 | 2.60--3.95 GHz | 15--24 dBi |
| WR-137 | 5.85--8.20 GHz | 15--24 dBi |
| WR-90 | 8.20--12.40 GHz | 15--25 dBi |
| WR-42 | 18.0--26.5 GHz | 15--25 dBi |
| WR-28 | 26.5--40.0 GHz | 15--25 dBi |

---

## 13. Connections and Cross-References

| Topic | Connection |
|-------|------------|
| **Section 6 (Arrays)** | Horns are used as feed elements in arrays |
| **Section 7 (Antenna Synthesis)** | Horn design involves synthesis of aperture field distribution |
| **Section 11 (Fractal Antennas)** | Frequency-independent concepts apply to log-periodic horns |
| **Section 12 (Aperture Antennas)** | Horns are a subclass of aperture antennas; field equivalence principle applies |
| **Section 14 (Microstrip Antennas)** | Horns and microstrip antennas serve as feeds for reflector antennas |
| **Section 15 (Reflector Antennas)** | Horns are the most common feed element for reflector antennas |

---

## Solved Exercises

### Exercise 1: E-Plane Sectoral Horn Geometry

**Problem:** A rectangular waveguide of dimensions $a = 0.5\lambda$ and $b = 0.25\lambda$ is flared in the E-plane with apex length $R_0 = 2\lambda$. Find the aperture height $B$ for optimum directivity.

**Solution:**
For an E-plane sectoral horn, the optimum directivity is achieved when $B = \sqrt{2\lambda R_0}$.

Substituting $R_0 = 2\lambda$:

$$
B = \sqrt{2\lambda \cdot 2\lambda} = \sqrt{4\lambda^2} = 2\lambda
$$

The aperture field is:

$$
E_x \approx E_0 \frac{\cos(\pi y / b)}{a} e^{-j\beta y^2 / (2R_0)}
$$

where $\beta = 2\pi/\lambda$, $b = 0.25\lambda$, and $a = 0.5\lambda$.

---

### Exercise 2: Pyramidal Horn Gain

**Problem:** A pyramidal horn has dimensions $A = 3\lambda$ and $B = 2\lambda$. Calculate the gain in dBi.

**Solution:**
The gain of a pyramidal horn is:

$$
G = \frac{4\pi AB}{\lambda^2} e_{ap}
$$

Using the optimum efficiency $e_{ap} = 0.511$:

$$
G = \frac{4\pi \cdot 3\lambda \cdot 2\lambda}{\lambda^2} \times 0.511 = 24\pi \times 0.511 = 38.6
$$

$$
G_{\text{dBi}} = 10\log_{10}(38.6) = 15.9\;\text{dBi}
$$

---

### Exercise 3: Conical Horn Optimal Aperture

**Problem:** A conical horn with apex length $L = 10\lambda$ is desired. Find the optimal aperture diameter and gain.

**Solution:**
The optimal aperture diameter for a conical horn satisfies:

$$
d = \sqrt{3\lambda L} = \sqrt{3\lambda \cdot 10\lambda} = \sqrt{30}\lambda \approx 5.48\lambda
$$

The gain is:

$$
G = \left(\frac{\pi d}{\lambda}\right)^2 e_A = \left(\pi \cdot 5.48\right)^2 \times 0.522 = 296.2 \times 0.522 = 154.6
$$

$$
G_{\text{dBi}} = 10\log_{10}(154.6) \approx 21.9\;\text{dBi}
$$

---

### Exercise 4: Corrugated Horn Aperture Efficiency

**Problem:** A corrugated horn has aperture diameter $d = 10\lambda$ and aperture efficiency $e_A = 0.75$. Find the gain in dBi. Compare with an optimum conical horn of the same aperture.

**Solution:**
For the corrugated horn:

$$
G = \left(\frac{\pi \cdot 10}{1}\right)^2 \times 0.75 = 986.96 \times 0.75 = 740.22
$$

$$
G_{\text{dBi}} = 10\log_{10}(740.22) \approx 28.7\;\text{dBi}
$$

For an optimum conical horn ($e_A = 0.522$):

$$
G = 986.96 \times 0.522 = 515.2
$$

$$
G_{\text{dBi}} = 10\log_{10}(515.2) \approx 27.1\;\text{dBi}
$$

The corrugated horn provides $1.6\;\text{dB}$ more gain due to higher aperture efficiency.

---

### Exercise 5: HPBW of a Large Conical Horn

**Problem:** A conical horn has aperture radius $a = 5\lambda$. Find the half-power beamwidth (HPBW).

**Solution:**
For a large circular aperture:

$$
\text{HPBW} \approx 2\arcsin\frac{1.6}{\beta a}
$$

where $\beta = 2\pi/\lambda$, so $\beta a = 2\pi \cdot 5 = 10\pi$.

$$
\text{HPBW} \approx 2\arcsin\frac{1.6}{10\pi} = 2\arcsin(0.0509) = 2 \times 2.917^\circ = 5.83^\circ
$$

---

### Exercise 6: Pyramidal Horn Design

**Problem:** Design an optimum pyramidal horn with axial length $R_0 = 8\lambda$. The feeding waveguide has dimensions $a = 0.7\lambda$ and $b = 0.35\lambda$. Find the aperture dimensions $A$, $B$, and the gain.

**Solution:**
Step 1: Compute $A$ from the H-plane optimum condition:

$$
A = \sqrt{3\lambda R_0} = \sqrt{3\lambda \cdot 8\lambda} = \sqrt{24}\lambda \approx 4.90\lambda
$$

Step 2: Compute $B$ from the E-plane optimum condition:

$$
B = \sqrt{2\lambda R_0} = \sqrt{2\lambda \cdot 8\lambda} = \sqrt{16}\lambda = 4\lambda
$$

Step 3: Compute the gain using $e_{ap} = 0.511$:

$$
G = \frac{4\pi \cdot 4.90\lambda \cdot 4\lambda}{\lambda^2} \times 0.511 = \frac{4\pi \cdot 19.6}{1} \times 0.511 = 246.3 \times 0.511 = 125.8
$$

$$
G_{\text{dBi}} = 10\log_{10}(125.8) \approx 21.0\;\text{dBi}
$$

---

### Exercise 7: Fresnel Zone Analysis for a Sectoral Horn

**Problem:** An H-plane sectoral horn has apex length $R_0 = 6\lambda$ and aperture width $A = 4\lambda$. Determine the phase error at the edge of the aperture relative to the center.

**Solution:**
The path length difference from the apex to the aperture edge compared to the center is:

$$
\Delta R = \sqrt{R_0^2 + (A/2)^2} - R_0 = \sqrt{(6\lambda)^2 + (2\lambda)^2} - 6\lambda = \sqrt{40}\lambda - 6\lambda
$$

$$
\Delta R = 6.325\lambda - 6\lambda = 0.325\lambda
$$

The phase error is:

$$
\Delta \phi = \frac{2\pi}{\lambda} \Delta R = 2\pi \times 0.325 = 0.65\pi
$$

The phase error is $0.65\pi$ radians, or approximately $117^\circ$, which is significant and will affect the gain and pattern.

---

### Exercise 8: Horn Type Selection

**Problem:** An application requires a horn antenna with:
- Symmetric beam pattern
- Cross-polarization below $-25\;\text{dB}$
- Bandwidth of $40\%$
- Aperture diameter $8\lambda$ (fixed)
- Maximum gain

Which horn type should be selected? Compare the gain to a smooth conical horn.

**Solution:**
The requirements of symmetric beam pattern, low cross-polarization ($< -25\;\text{dB}$), and wide bandwidth ($40\%$) rule out:
- **Sectoral horns:** Fan-shaped beam (asymmetric).
- **Multimode horns:** Bandwidth $< 10\%$.

The corrugated horn is the best choice as it provides:
- Symmetric HE$_{11}$ mode pattern.
- Cross-polarization below $-30\;\text{dB}$.
- Bandwidth up to 2:1.
- Aperture efficiency $70$--$80\%$.

Gain comparison for $d = 8\lambda$:

Smooth conical: $G = (\pi \cdot 8)^2 \times 0.522 = 631.7 \times 0.522 = 329.7 \;(25.2\;\text{dBi})$

Corrugated: $G = 631.7 \times 0.75 = 473.8 \;(26.8\;\text{dBi})$

The corrugated horn provides approximately $1.6\;\text{dB}$ more gain.

---

## Exam Tip: Standard Horn Selection for Exams

In exam problems involving horn antennas, three key optimization conditions recur:

1. **Pyramidal horn optimum design** is always based on $A = \sqrt{3\lambda R_H}$ and $B = \sqrt{2\lambda R_E}$ with $R_H = R_E$.
2. **Total aperture efficiency** for optimum pyramidal horns is always $0.511$, and for optimum conical horns is $0.522$.
3. **Phase error** is the dominant factor limiting horn gain: the Fresnel integral formulation for directivity accounts for both amplitude taper and phase error across the aperture.

When comparing horn types, the corrugated horn always wins in pattern symmetry and cross-polarization, but the pyramidal horn wins in simplicity and cost. Memorize the gain formula $G = 4\pi A e_A / \lambda^2$ for aperture antennas---it applies to all horn types with appropriate $e_A$ values.

---

## Exam Tip: Common Mistakes

1. **Confusing optimum gain vs. maximum gain:** The optimum horn gives the highest gain for a given *length*, not for a given *aperture size*. A longer horn can always produce higher gain from the same aperture by reducing phase error.
2. **Assuming uniform phase across the aperture:** Phase error due to the spherical wavefront inside the horn is a critical factor that reduces gain and broadens the beamwidth.
3. **Neglecting the E-plane/H-plane asymmetry:** Sectoral and pyramidal horns have inherently asymmetric patterns. If beam symmetry is needed, use corrugated or conical horns.
4. **Using $e_A = 1$ for horn antennas:** This is only valid for aperture-limited (very long) horns. Optimum horns have $e_A \approx 0.5$ due to phase error and amplitude taper.
5. **Forgetting that $R_H = R_E$ for a realizable pyramidal horn:** The two apex lengths must be equal for a single physical horn structure.