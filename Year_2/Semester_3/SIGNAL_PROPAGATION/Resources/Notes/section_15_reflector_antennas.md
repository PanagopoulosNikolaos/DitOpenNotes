# Reflector Antennas

Reflector antennas are high-gain aperture antennas that use a reflecting surface to redirect and concentrate electromagnetic energy from a primary feed antenna into a desired radiation pattern. They are among the most widely used high-gain antennas at microwave frequencies (1--100 GHz), capable of achieving gains above 30 dB with narrow pencil beams. Reflector antennas are employed in radio astronomy, satellite communications, radar systems, microwave relay links, and deep-space communication. The principal reflector geometries include plane, corner, parabolic (paraboloidal), and spherical reflectors, each offering different trade-offs between gain, beamwidth, complexity, and cost.

*Prerequisite: Section 12 (Aperture Antennas) for the field equivalence principle and aperture integration methods. Section 13 (Horn Antennas) for horn feeds commonly used with reflectors.*

---

## 1. Conceptual Foundation

### 1.1 The Purpose of a Reflector Antenna

A primary (feed) antenna by itself typically radiates with limited directivity -- for example, a dipole or a horn produces a broad beam. To achieve the very high directivity required for long-distance communication (satellite links, radar, radio astronomy), the feed antenna is placed at the focus of a large conducting surface (the reflector). The reflector collects the energy from the feed and redirects it into a narrow beam, effectively increasing the effective aperture area of the antenna system.

The fundamental principle is analogous to an optical reflecting telescope: the reflector acts as a "mirror" for radio waves, converting the spherical wavefront from the feed into a more collimated (plane) wavefront.

### 1.2 Active and Passive Elements

- **Active element (feed antenna):** The radiating source directly connected to the transmitter or receiver. Common feeds include dipole antennas, horn antennas (pyramidal or conical), and array feeds.
- **Passive element (reflector surface):** A conducting surface (solid metal, wire mesh, or perforated sheet) that redirects the feed radiation. The reflector is not directly connected to the feed circuit.

### 1.3 Historical Context

Heinrich Hertz used the first cylindrical parabolic reflector in 1888 to demonstrate radio wave propagation. The development of radar during World War II drove rapid advances in reflector antenna theory and design. Since then, reflector antennas have become the dominant high-gain antenna type for microwave systems, with dishes ranging from small satellite TV antennas (0.5 m) to giant radio telescopes (300 m aperture).

---

## 2. Formal Definitions and Models

### 2.1 Image Theory for Reflector Analysis

The simplest analytical tool for plane and corner reflectors is image theory. A conducting plane reflector is replaced by an image of the feed source located symmetrically on the opposite side of the plane. For a corner reflector with included angle $\alpha = \pi/n$ (where $n$ is an integer), $2n-1$ image sources are used to satisfy the boundary conditions.

### 2.2 Geometric Optics (GO) for Curved Reflectors

For curved reflectors (parabolic, spherical), analysis proceeds via geometric optics (ray tracing) when the reflector dimensions are large compared to the wavelength. The key assumptions are:

- The reflector surface is locally planar at each reflection point.
- The incident wavefront from the feed is locally planar at the reflection point.
- The reflector is a perfect electric conductor.

### 2.3 The Parabola Equation

A parabola in the $yz$-plane (with axis along $z$) is defined as the locus of points equidistant from a fixed point (focus $F$) and a fixed line (the directrix). In polar coordinates with origin at the focus:

$$
r_f = \frac{2F}{1 + \cos\theta_f} = \frac{F}{\cos^2(\theta_f/2)}
$$

where:

- $r_f$ is the distance from the focus to a point on the reflector
- $\theta_f$ is the angle from the reflector axis to the ray
- $F$ is the focal length

---

## 3. Key Parameters and Constraints

| Parameter | Symbol | Definition | Typical Range | Impact |
|-----------|--------|-----------|---------------|--------|
| Focal length | $F$ | Distance from vertex to focus | $0.25D \leq F \leq 0.50D$ | Determines feed angle, spillover, and illumination taper |
| Aperture diameter | $D$ | Diameter of the reflector rim | $10\lambda$ to $1000\lambda$ | Primary determinant of gain and beamwidth |
| F/D ratio | $F/D$ | Focal length to diameter ratio | $0.25$ to $0.50$ | Controls reflector depth, feed placement, illumination |
| Aperture efficiency | $e_A$ | Ratio of effective to physical aperture | $0.50$ to $0.80$ | Reduces gain from ideal; includes taper, spillover, blockage |
| Half-power beamwidth | $\text{HPBW}$ | Angular width at -3 dB points | $58\lambda/D$ degrees (circular) | Inverse measure of directivity |
| Gain | $G$ | Ratio of radiated intensity to isotropic | $15$ to $80$ dBi | Increases with $(D/\lambda)^2$ |
| Spillover efficiency | $\varepsilon_s$ | Fraction of feed power intercepted | $0.75$ to $0.95$ | Trade-off with illumination taper |
| Surface accuracy | $\Delta$ | RMS deviation from ideal shape | $<\lambda/16$ | Limits maximum gain; Ruze formula |
| Cross-polarization | XPOL | Ratio of cross-pol to co-pol peak | $-30$ to $-20$ dB | Depends on feed pattern and F/D ratio |

---

## 4. Plane Reflector

### 4.1 Configuration

The plane reflector is the simplest reflector type: a flat conducting sheet placed behind a feed antenna (typically a dipole) at a distance $d$ from the feed.

### 4.2 Principle of Operation

Using image theory, the conducting plane is replaced by an image dipole located at a distance $d$ behind the plane, with opposite polarity. The field in front of the plane is the superposition of the direct field from the feed and the reflected field from the image.

### 4.3 Array Factor

For a dipole at distance $d$ from an infinite conducting plane, the array factor in the far field is:

$$
AF(\theta) = 2j\sin(kd\cos\theta)
$$

where $\theta$ is measured from the plane normal, and $k = 2\pi/\lambda$.

### 4.4 Gain Enhancement

The maximum gain occurs when $d = \lambda/4$ (i.e., $kd = \pi/2$), producing constructive interference in the forward direction. The gain enhancement over the isolated dipole is a factor of 4 (6 dB).

### 4.5 Limitations

A plane reflector cannot collimate energy into a truly directional beam -- the reflected wavefront remains spherical, not planar. The directivity improvement is modest, and significant radiation remains in the backward hemisphere.

> **[Supplementary]** For a short dipole with a plane reflector at $d = \lambda/4$, the radiation pattern has a single main lobe in the forward direction with HPBW of approximately $90^\circ$, and a front-to-back ratio of about 15 dB. The input impedance is modified by mutual coupling with the image: $Z_{in} = Z_{11} - Z_{12}$, where $Z_{11}$ is the self-impedance and $Z_{12}$ is the mutual impedance between the dipole and its image.

---

## 5. Corner Reflector

### 5.1 Configuration

The corner reflector consists of two conducting planes joined at an included angle $\alpha$ (typically $90^\circ$). A feed dipole is placed parallel to the vertex at a distance $s$ from it.

### 5.2 Principle of Operation

For an included angle $\alpha = \pi/n$ where $n$ is an integer, image theory yields $2n-1$ image sources arranged around the vertex. For the most common case $\alpha = 90^\circ$ ($n=2$), there are three images forming a symmetrical four-source array.

### 5.3 Array Factor for $\alpha = 90^\circ$

For a $90^\circ$ corner reflector with feed at distance $s$ from the vertex (measured along the bisector), the array factor is:

$$
AF(\theta, \phi) = 4\sin(ks\sin\theta\cos\phi)\sin(ks\sin\theta\sin\phi)
$$

The maximum forward gain occurs when $s = 0.5\lambda$ to $0.7\lambda$.

### 5.4 Gain Enhancement

The $90^\circ$ corner reflector provides a gain enhancement factor of approximately 16 (12 dB) over an isolated dipole for optimum spacing. The HPBW is approximately $40^\circ$--$50^\circ$ in the $H$-plane.

### 5.5 Characteristics of the $90^\circ$ Corner Reflector

- Most popular corner reflector angle due to attractive radiation characteristics.
- When used as a passive reflector (without feed), it acts as a retro-reflector: an incident wave is reflected back exactly toward its source. This property is exploited in radar targets and navigation markers.
- Practical designs use wire-grid surfaces (grid spacing $\leq \lambda/10$) rather than solid sheet metal to reduce wind resistance and weight.
- Side length is typically $1.5\lambda$ to $2\lambda$; extending sides beyond this range does not significantly improve directivity.

> **[Supplementary]** The optimum feed-to-vertex spacing $s$ depends on the included angle:
> - For $\alpha = 90^\circ$: optimum $s \approx 0.5\lambda$
> - For $\alpha = 60^\circ$: optimum $s \approx 0.8\lambda$
> - For $\alpha = 45^\circ$: optimum $s \approx 1.2\lambda$
>
> If $s$ is too small, the radiation resistance drops and ohmic losses dominate. If $s$ is too large, multiple lobes appear and directivity degrades.

### 5.6 Active vs. Passive Corner Reflectors

- **Active corner reflector:** A feed antenna (dipole) is placed at the vertex; the reflector shapes the radiated beam.
- **Passive corner reflector:** No feed antenna; the reflector alone is used as a radar target. A $90^\circ$ corner retro-reflects incident waves.

---

## 6. Parabolic Reflector

### 6.1 Configuration

The parabolic (paraboloidal) reflector is a surface formed by rotating a parabola about its axis. The feed antenna is placed at the focal point. This is by far the most important and widely used reflector type.

### 6.2 Key Geometrical Properties

Two properties make the parabolic reflector indispensable:

**Property 1: Collimation.** All rays originating from the focal point are reflected parallel to the reflector axis. This converts the spherical wavefront from the feed into a plane wavefront at the aperture.

**Property 2: Equal Path Length.** The total path length from the focal point to the reflector and then to the aperture plane (a plane perpendicular to the axis passing through the focal point) is constant, equal to $2F$, regardless of the angle $\theta_f$. This ensures uniform phase across the aperture.

### 6.3 Surface Geometry

The paraboloidal surface in cylindrical coordinates $(\rho', z)$:

$$
z = \frac{\rho'^2}{4F} = \frac{x^2 + y^2}{4F}
$$

The rim angle $\theta_0$ (half-angle subtended by the reflector rim at the focus) relates to $F/D$:

$$
\theta_0 = 2\arctan\left(\frac{1}{4F/D}\right)
$$

| $F/D$ | $\theta_0$ | Characteristics |
|-------|-----------|-----------------|
| 0.25 | $90^\circ$ | Focus in rim plane; deep dish |
| 0.35 | $71.1^\circ$ | Common in practice |
| 0.50 | $53.1^\circ$ | Shallow dish; long focal length |

### 6.4 Feed Types

| Feed Type | Description | Typical Use |
|-----------|-------------|-------------|
| **Front-feed (axial)** | Feed at focal point; simplest configuration | General-purpose dishes; efficiency 55-60% |
| **Offset-feed** | Feed offset from aperture; no blockage | Satellite TV; avoids aperture blockage |
| **Cassegrain** | Dual-reflector: parabolic main + hyperbolic subreflector | Radio telescopes, satellite ground stations; efficiency 65-80% |
| **Gregorian** | Dual-reflector: parabolic main + elliptical subreflector | Radio astronomy; very low noise |

### 6.5 Gain and Aperture Efficiency

The gain of a parabolic reflector antenna is:

$$
G = \frac{4\pi A}{\lambda^2} e_A = \left(\frac{\pi D}{\lambda}\right)^2 e_A
$$

where $A = \pi D^2/4$ is the physical aperture area.

Aperture efficiency $e_A$ is the product of several sub-efficiencies:

$$
e_A = e_r \cdot \varepsilon_t \cdot \varepsilon_s \cdot \varepsilon_a
$$

| Efficiency | Typical Value | Description |
|-----------|--------------|-------------|
| Radiation efficiency $e_r$ | 0.95--0.99 | Ohmic losses in reflector and feed |
| Taper efficiency $\varepsilon_t$ | 0.80--0.91 | Non-uniform amplitude across aperture |
| Spillover efficiency $\varepsilon_s$ | 0.75--0.95 | Power from feed that misses reflector |
| Achievement efficiency $\varepsilon_a$ | 0.80--0.95 | Surface errors, blockage, phase errors |
| **Total aperture efficiency $e_A$** | **0.50--0.80** | Product of all factors |

For a well-designed front-fed paraboloid, $e_A \approx 0.55$--$0.60$. Cassegrain designs achieve $e_A \approx 0.65$--$0.80$.

### 6.6 Beamwidth

For a circular aperture with uniform illumination:

$$
\text{HPBW} \approx 58\frac{\lambda}{D} \text{ degrees}
$$

$$
\text{BWFN} \approx 140\frac{\lambda}{D} \text{ degrees}
$$

In practice, the illumination taper broadens the beam slightly, so the often-used formula is:

$$
\text{HPBW} \approx 70\frac{\lambda}{D} \text{ degrees}
$$

### 6.7 Factors Affecting Efficiency

**Feed spillover:** Radiation from the feed that misses the reflector is wasted. It also contributes to backlobes and, in receiving systems, increases noise temperature by "seeing" the warm ground.

**Illumination taper:** To reduce spillover, the feed pattern is tapered so that the illumination at the reflector edge is typically 10 dB below the center illumination. This reduces aperture efficiency but improves sidelobe levels.

**Aperture blockage:** The feed and its support struts block part of the aperture, reducing effective area and increasing sidelobes. Offset feed designs eliminate this problem.

**Surface errors:** Random surface deviations from the ideal paraboloid cause phase errors that reduce gain. The Ruze formula gives the gain reduction:

$$
\frac{G}{G_0} = e^{-(4\pi\Delta/\lambda)^2}
$$

where $\Delta$ is the RMS surface error. To keep gain loss below 1 dB, $\Delta \leq \lambda/16$ is required.

**Cross-polarization:** A linearly polarized feed produces a cross-polarized component in the aperture field when the feed pattern is not rotationally symmetric. Cross-polarization is zero in the principal planes and maximum at $\phi = 45^\circ$ and $135^\circ$. It decreases as $F/D$ increases.

### 6.8 Cassegrain Dual-Reflector System

The Cassegrain configuration uses:
- **Main reflector:** Paraboloid
- **Subreflector:** Hyperboloid (convex)
- **Feed:** Located at or near the vertex of the main reflector

The hyperbolic subreflector has one focus coincident with the paraboloid focus and the other at the feed location. The equivalent parabola concept shows that the Cassegrain system behaves like a single reflector with an equivalent focal length:

$$
F_e = F \cdot M = F \cdot \frac{e+1}{e-1}
$$

where $M$ is the magnification and $e$ is the eccentricity of the hyperbola ($e > 1$). The increased effective focal length reduces spherical spreading loss at the rim, improving aperture efficiency.

Advantages of Cassegrain feeds:
- Feed is accessible at the vertex (short waveguide runs).
- Reduced spillover toward ground (lower noise temperature).
- Higher aperture efficiency (65--80%).

### 6.9 Offset Parabolic Reflector

The offset reflector uses a portion of a parent paraboloid, with the feed placed away from the aperture. This eliminates aperture blockage from the feed and supports, improving efficiency and reducing sidelobes. The trade-off is increased cross-polarization, which can be mitigated by using a feed with rotationally symmetric pattern.

---

## 7. Spherical Reflector

### 7.1 Configuration

A spherical reflector uses a surface that is a segment of a sphere. Unlike the paraboloid, it does not have a unique focal point -- parallel rays incident on a sphere do not converge to a single point.

### 7.2 Spherical Aberration

The departure of the reflected wavefront from a plane wave is called spherical aberration. For a point source placed at the paraxial focus (at half the radius, $F = R/2$), rays near the axis focus well but rays from the edge focus at different points. This creates a caustic region rather than a single focal point.

### 7.3 Reduction of Spherical Aberration

To minimize path error in a spherical reflector, the feed is placed not at the paraxial focus but displaced slightly toward the reflector. The optimum focal length for an aperture of radius $a$ on a sphere of radius $R$ is:

$$
f_0 = \frac{R}{2} - \frac{a^2}{8R}
$$

The maximum path error for this optimum placement is:

$$
\Delta_{\text{max}} = \frac{a^4}{32R^3}
$$

### 7.4 Limitations and Applications

Spherical reflectors are less efficient than parabolic reflectors because of the aberrated phase distribution. However, they offer one significant advantage: the feed can be moved to point the beam in different directions without moving the entire reflector (the Arecibo telescope used this principle). Spherical reflectors are used where a fixed reflector and steerable feed are required.

> **[Supplementary]** The Arecibo radio telescope (305 m diameter, collapsed in 2020) used a spherical reflector with line feeds and later a Gregorian dual-reflector system to correct spherical aberration. The Five-hundred-meter Aperture Spherical Telescope (FAST) in China uses an active spherical surface with deformable panels to correct spherical aberration dynamically.

---

## 8. Connections and Cross-References

| Topic | Connection |
|-------|------------|
| **Section 2 (Fundamental Parameters)** | Gain, directivity, beamwidth, efficiency definitions apply directly |
| **Section 3 (Radiation Integrals)** | Aperture distribution and current distribution methods for reflector analysis |
| **Section 12 (Aperture Antennas)** | Reflectors are aperture antennas; Huygens' principle and Fourier transform methods apply |
| **Section 13 (Horn Antennas)** | Horns are the most common feed for parabolic and spherical reflectors |
| **Section 14 (Microstrip Antennas)** | Microstrip patch arrays can serve as feeds for reflector antennas |
| **Section 6 (Arrays)** | Array feeds can shape reflector beams; mutual coupling in feed arrays |
| **Section 17 (Antenna Measurements)** | Gain, pattern, and polarization measurement of reflector antennas |

---

## Solved Exercises

### Exercise 1: Plane Reflector Spacing

**Problem:** A short dipole is placed at a distance $d$ from an infinite conducting plane reflector. Find the spacing $d$ (in wavelengths) that maximizes the gain in the forward direction.

**Solution:**
Using image theory, the dipole and its image form a two-element array with spacing $2d$ and opposite phase (image current is opposite polarity).

The array factor is:
$$AF(\theta) = 2j\sin(kd\cos\theta)$$

Maximum forward radiation at $\theta = 0$ occurs when $|\sin(kd)| = 1$, i.e., when:

$$kd = \frac{\pi}{2} \quad \Rightarrow \quad d = \frac{\lambda}{4}$$

At $d = \lambda/4$:

$$AF(0) = 2j\sin(\pi/2) = 2j$$

The power gain increases by a factor of $|AF|^2 = 4$ (6 dB) relative to the isolated dipole.

The radiation pattern in the $H$-plane ($\theta$ from $-90^\circ$ to $90^\circ$):

$$p(\theta) = \sin^2(kd\cos\theta) = \sin^2\left(\frac{\pi}{2}\cos\theta\right)$$

The HPBW is found by solving $\sin^2(\pi\cos\theta/2) = 0.5$, giving $\text{HPBW} \approx 90^\circ$.

---

### Exercise 2: $90^\circ$ Corner Reflector Gain

**Problem:** A $90^\circ$ corner reflector is fed by a short dipole at spacing $s = 0.5\lambda$ from the vertex along the bisector. Calculate the gain enhancement factor over an isolated dipole.

**Solution:**
For $\alpha = 90^\circ$ ($n = 2$), image theory gives three image sources. The four-source array (feed + 3 images) forms a symmetrical configuration.

The array factor in the forward direction ($\theta = 90^\circ$, $\phi = 0^\circ$) for a feed at $s = \lambda/2$ from the vertex is:

$$AF = 4\sin(ks\cos 0^\circ)\sin(ks\sin 0^\circ) = 4\sin(ks)$$

$$AF = 4\sin(2\pi \cdot 0.5) = 4\sin(\pi) = 0$$

Wait -- at $s = 0.5\lambda$, the pattern has a null in the forward direction. Let us check the optimum spacing.

For a $90^\circ$ corner, the radiation pattern maximum occurs for $s \approx 0.5\lambda$ in the $H$-plane ($\theta = 90^\circ$), but the direction of maximum radiation depends on the array factor. Let us recalculate for the direction along the bisector ($\phi = 45^\circ$, $\theta = 90^\circ$).

At $\theta = 90^\circ$ and $\phi = 45^\circ$:

$$AF(90^\circ, 45^\circ) = 4\sin(ks\sin45^\circ)\sin(ks\sin45^\circ) = 4\sin^2(ks/\sqrt{2})$$

For $s = 0.5\lambda$, $ks = \pi$, so $ks/\sqrt{2} = \pi/\sqrt{2} \approx 2.22$ rad $\approx 127^\circ$.

$$\sin(2.22) \approx 0.798$$

$$AF = 4 \times (0.798)^2 = 4 \times 0.637 = 2.55$$

The gain enhancement relative to an isolated dipole is:

$$G_{\text{enh}} = |AF|^2 = (2.55)^2 \approx 6.5$$

In dB: $G_{\text{enh,dB}} = 10\log_{10}(6.5) \approx 8.1$ dB.

---

### Exercise 3: Parabolic Reflector Gain Calculation

**Problem:** A front-fed parabolic dish has diameter $D = 2$ m and operates at 12 GHz ($\lambda = 0.025$ m). The aperture efficiency is $e_A = 0.55$. Calculate the gain in dBi.

**Solution:**
The gain formula for a parabolic reflector:

$$G = \left(\frac{\pi D}{\lambda}\right)^2 e_A$$

$$G = \left(\frac{\pi \cdot 2}{0.025}\right)^2 \times 0.55 = (251.33)^2 \times 0.55 = 63165 \times 0.55 = 34741$$

$$G_{\text{dBi}} = 10\log_{10}(34741) = 10 \times 4.541 = 45.4 \text{ dBi}$$

---

### Exercise 4: HPBW of a Parabolic Reflector

**Problem:** Calculate the half-power beamwidth (HPBW) of the 2 m dish from Exercise 3 operating at 12 GHz.

**Solution:**
Using the practical formula for a circular aperture:

$$\text{HPBW} \approx 70\frac{\lambda}{D} \text{ degrees}$$

$$\text{HPBW} \approx 70 \times \frac{0.025}{2} = 70 \times 0.0125 = 0.875^\circ$$

For comparison, the ideal uniform illumination would give:

$$\text{HPBW}_{\text{ideal}} \approx 58\frac{\lambda}{D} = 58 \times 0.0125 = 0.725^\circ$$

The broader beam in practice is due to the illumination taper (lower amplitude at the edges of the dish).

---

### Exercise 5: Depth of a Parabolic Reflector

**Problem:** A parabolic reflector has diameter $D = 3$ m and focal length $F = 0.9$ m. Find the depth $H_0$ of the dish (distance from the rim plane to the vertex).

**Solution:**
The paraboloid equation is:

$$z = \frac{\rho'^2}{4F}$$

At the rim, $\rho' = D/2 = 1.5$ m. The depth $H_0$ is the $z$-coordinate at the rim:

$$H_0 = \frac{(D/2)^2}{4F} = \frac{(1.5)^2}{4 \times 0.9} = \frac{2.25}{3.6} = 0.625 \text{ m}$$

The $F/D$ ratio is:

$$\frac{F}{D} = \frac{0.9}{3.0} = 0.30$$

The rim angle $\theta_0$ is:

$$\theta_0 = 2\arctan\left(\frac{1}{4F/D}\right) = 2\arctan\left(\frac{1}{4 \times 0.3}\right) = 2\arctan(0.833) = 2 \times 39.8^\circ = 79.6^\circ$$

---

### Exercise 6: Surface Error Tolerance

**Problem:** A parabolic reflector operating at 10 GHz must have gain loss less than 0.5 dB due to surface errors. Calculate the maximum allowed RMS surface deviation $\Delta$.

**Solution:**
The Ruze formula gives the gain reduction ratio:

$$\frac{G}{G_0} = e^{-(4\pi\Delta/\lambda)^2}$$

For 0.5 dB loss:

$$10\log_{10}(G/G_0) = -0.5 \text{ dB}$$

$$\frac{G}{G_0} = 10^{-0.5/10} = 10^{-0.05} = 0.891$$

$$e^{-(4\pi\Delta/\lambda)^2} = 0.891$$

$$-(4\pi\Delta/\lambda)^2 = \ln(0.891) = -0.115$$

$$(4\pi\Delta/\lambda)^2 = 0.115$$

$$4\pi\Delta/\lambda = \sqrt{0.115} = 0.339$$

$$\Delta = \frac{0.339\lambda}{4\pi} = 0.0270\lambda$$

At 10 GHz, $\lambda = 0.03$ m = 30 mm:

$$\Delta = 0.0270 \times 30 = 0.81 \text{ mm} = 810 \text{ }\mu\text{m}$$

For 1 dB loss: $\Delta \approx \lambda/16 = 1.875$ mm at 10 GHz.

---

### Exercise 7: Cassegrain Equivalent Focal Length

**Problem:** A Cassegrain antenna has a main reflector with $F = 1$ m and a hyperbolic subreflector with eccentricity $e = 2.5$. Find the equivalent focal length and the magnification.

**Solution:**
The magnification of a Cassegrain system is:

$$M = \frac{e+1}{e-1} = \frac{2.5+1}{2.5-1} = \frac{3.5}{1.5} = 2.33$$

The equivalent focal length is:

$$F_e = F \cdot M = 1 \times 2.33 = 2.33 \text{ m}$$

The increased effective focal length means that from the aperture perspective, the system behaves like a single paraboloid with $F/D$ ratio 2.33 times larger. This reduces the feed angle $\theta_0$ and the spherical spreading loss at the rim, improving taper efficiency.

---

### Exercise 8: Corner Reflector as Radar Target

**Problem:** A $90^\circ$ corner reflector with side length $L = 2\lambda$ is used as a passive radar target. Calculate its radar cross-section (RCS) relative to a flat metal plate of the same area.

**Solution:**
The maximum RCS of a $90^\circ$ corner reflector (trihedral) is:

$$\sigma_{\text{corner}} = \frac{4\pi L^4}{3\lambda^2}$$

For $L = 2\lambda$:

$$\sigma_{\text{corner}} = \frac{4\pi (2\lambda)^4}{3\lambda^2} = \frac{4\pi \cdot 16\lambda^4}{3\lambda^2} = \frac{64\pi}{3}\lambda^2 \approx 67.0\lambda^2$$

A flat plate of area $A = L^2 = 4\lambda^2$ has a maximum RCS (normal incidence):

$$\sigma_{\text{plate}} = \frac{4\pi A^2}{\lambda^2} = \frac{4\pi (4\lambda^2)^2}{\lambda^2} = \frac{4\pi \cdot 16\lambda^4}{\lambda^2} = 64\pi\lambda^2 \approx 201\lambda^2$$

However, the flat plate RCS drops rapidly as the aspect angle changes, while the corner reflector maintains high RCS over a wide angular range ($\pm 40^\circ$ from the axis).

The corner reflector's advantage is its wide angular coverage -- it acts as a retro-reflector, returning signals toward the source over a broad range of incidence angles.

---

### Exercise 9: Spherical Reflector Path Error

**Problem:** A spherical reflector has radius $R = 50\lambda$ and an aperture of radius $a = 20\lambda$. Calculate the maximum path error when the feed is placed at the optimum focal length.

**Solution:**
The maximum path error for a spherical reflector with feed at optimum location is:

$$\Delta_{\text{max}} = \frac{a^4}{32R^3}$$

Substituting:

$$\Delta_{\text{max}} = \frac{(20\lambda)^4}{32(50\lambda)^3} = \frac{160000\lambda^4}{32 \times 125000\lambda^3} = \frac{160000}{4000000}\lambda = 0.04\lambda$$

The total phase error is:

$$\phi_{\text{err}} = \frac{2\pi}{\lambda} \times 0.04\lambda = 0.08\pi \text{ radians} = 14.4^\circ$$

This phase error is significantly larger than the $\pi/8$ (22.5$) criterion for tolerable gain loss, indicating that a spherical reflector with this aperture will have notable gain reduction compared to a paraboloid.

To maintain $\phi_{\text{err}} < \pi/8$, we need $\Delta_{\text{max}} < \lambda/16 = 0.0625\lambda$, which is satisfied here, but the spherical aberration will still reduce efficiency below that of a parabolic reflector.

---

### Exercise 10: Aperture Efficiency Breakdown

**Problem:** A front-fed parabolic reflector is designed with the following sub-efficiencies: taper efficiency $\varepsilon_t = 0.85$, spillover efficiency $\varepsilon_s = 0.88$, radiation efficiency $e_r = 0.98$, and achievement efficiency $\varepsilon_a = 0.90$. Calculate the total aperture efficiency and the gain for a 1.8 m dish at 14.25 GHz.

**Solution:**
Total aperture efficiency:

$$e_A = e_r \cdot \varepsilon_t \cdot \varepsilon_s \cdot \varepsilon_a = 0.98 \times 0.85 \times 0.88 \times 0.90 = 0.659$$

At 14.25 GHz, $\lambda = c/f = 3\times 10^8 / 14.25\times 10^9 = 0.02105$ m.

$$G = \left(\frac{\pi D}{\lambda}\right)^2 e_A = \left(\frac{\pi \times 1.8}{0.02105}\right)^2 \times 0.659 = (268.6)^2 \times 0.659$$

$$G = 72146 \times 0.659 = 47544$$

$$G_{\text{dBi}} = 10\log_{10}(47544) = 46.8 \text{ dBi}$$

The HPBW is approximately:

$$\text{HPBW} \approx 70\frac{\lambda}{D} = 70 \times \frac{0.02105}{1.8} = 0.819^\circ$$

---

## Exam Tip: Common Problem Patterns

Reflector antenna exam problems typically fall into four categories:

1. **Gain and beamwidth calculations** ($G = (\pi D/\lambda)^2 e_A$, $\text{HPBW} \approx 70\lambda/D$). Memorize these formulas. Note the inverse relationship: doubling $D$ quadruples gain and halves HPBW.

2. **$F/D$ ratio implications.** Remember that $F/D = 0.25$ puts the focus in the rim plane ($\theta_0 = 90^\circ$); $F/D = 0.5$ gives $\theta_0 \approx 53^\circ$. Larger $F/D$ means shallower dish, less spillover, but more taper (lower illumination at edges).

3. **Surface accuracy tolerance.** The $\lambda/16$ rule for 1 dB gain loss from the Ruze formula. Surface errors become more critical at higher frequencies.

4. **Comparison of reflector types.** On exams, expect to compare:
   - Plane vs. corner: image theory, number of images, gain enhancement
   - Parabolic vs. spherical: collimation vs. aberration, single-focus vs. caustic
   - Front-fed vs. Cassegrain: blockage, efficiency, feed accessibility

---

## Exam Tip: Common Mistakes

1. **Assuming uniform illumination.** Real reflector feeds have tapered illumination, reducing aperture efficiency to 50-80% of the ideal. Never use $e_A = 1$ unless explicitly stated.

2. **Confusing $F/D$ with $D/F$.** The $F/D$ ratio is the focal length divided by diameter. A "deep" dish has small $F/D$ (e.g., 0.25); a "shallow" dish has larger $F/D$ (e.g., 0.5).

3. **Forgetting that the Cassegrain equivalent focal length is longer than the physical one.** The magnification factor $M = (e+1)/(e-1)$ can significantly increase $F_e$, affecting feed design.

4. **Using the wrong beamwidth formula.** The $70\lambda/D$ formula applies to circular apertures. For rectangular apertures, use $115\lambda/L$ for BWFN (first null beamwidth).

5. **Neglecting aperture blockage in gain calculations.** Front-fed dishes suffer 5-15% gain reduction due to feed and support strut blockage. Offset feeds eliminate this.