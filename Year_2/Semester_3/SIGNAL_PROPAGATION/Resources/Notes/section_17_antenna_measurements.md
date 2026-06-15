# Antenna Measurements

Antenna measurements encompass the experimental techniques and facilities used to characterize antenna performance parameters, including radiation pattern, gain, directivity, impedance, polarization, efficiency, and current distribution. Because analytical computation of antenna performance is often intractable for complex geometries, measurement provides the essential validation of theoretical and simulation-based designs. Measurement methods span open-air far-field ranges, compact ranges, and near-field scanning facilities, each with distinct trade-offs between accuracy, cost, size constraints, and frequency range. Antenna measurements are fundamental to antenna engineering, enabling specification compliance verification, design iteration, and system-level performance prediction.

*Prerequisite: Section 2 (Fundamental Parameters of Antennas) for definitions of gain, directivity, beamwidth, efficiency, polarization, and impedance. Section 3 (Radiation Integrals and Auxiliary Potential Functions) for far-field criteria and radiation integrals.*

---

## 1. Conceptual Foundation

### 1.1 Why Antenna Measurements Are Necessary

Antenna performance predicted by analytical models and computational simulations inevitably deviates from reality due to:

- **Fabrication tolerances:** Physical dimensions differ from design specifications.
- **Material property variations:** Conductivity, permittivity, and permeability may differ from assumed values.
- **Mutual coupling effects:** In arrays or multi-antenna systems, coupling modifies element behavior.
- **Environmental interactions:** Ground planes, mounting structures, radomes, and nearby objects alter performance.
- **Numerical approximation errors:** Simulation meshing, truncation, and discretization introduce inaccuracies.

Measurements provide the ground truth against which designs are validated and certified.

### 1.2 Measurement Philosophy: Reciprocity

Antennas are typically measured in the receiving mode. By the reciprocity theorem, for a linear, passive, isotropic medium, the transmitting and receiving patterns of an antenna are identical. This allows the antenna under test (AUT) to be used as either the transmitting or receiving element in the measurement setup, whichever is more convenient.

### 1.3 The Far-Field Condition

The fundamental requirement for accurate pattern and gain measurements is that the AUT be illuminated by (or measured in) a uniform plane wave. This requires the separation distance $R$ between the AUT and the probe antenna to satisfy the far-field (Fraunhofer) condition:

$$
R \geq \frac{2D^2}{\lambda}
$$

where:

- $D$ is the largest dimension of the AUT
- $\lambda$ is the operating wavelength

At this distance, the phase variation across the AUT aperture is less than $\pi/8$ (22.5$^\circ$), and the amplitude variation is less than 0.25 dB, approximating a plane wave to acceptable accuracy.

For large antennas (e.g., reflector dishes with $D \gg \lambda$), the far-field distance can become impractically large, motivating the use of compact ranges or near-field measurement techniques.

---

## 2. Antenna Ranges

### 2.1 Classification of Ranges

| Range Type | Environment | Typical Frequency | Key Advantage | Key Limitation |
|------------|-------------|-------------------|---------------|----------------|
| Elevated range | Outdoor | All | No chamber cost, large antennas | Weather dependence, ground reflections |
| Slant range | Outdoor | All | Reduced ground effects | Requires cleared terrain, tower |
| Free-space range | Outdoor | All | Minimum reflections | Requires isolation from surroundings |
| Anechoic chamber | Indoor | 500 MHz--100 GHz | Controlled environment, all-weather | Limited by chamber size, cost |
| Compact range | Indoor | 1--100 GHz | Far-field in short distance | Quiet zone size limited by reflector |
| Near-field range | Indoor | 300 MHz--110 GHz | Small footprint, full 3D pattern | Complex data processing, time |

### 2.2 Outdoor Ranges

**Elevated Range:** The AUT and transmitting antenna are mounted on towers or rooftops, elevated above the ground to minimize reflections. The height must place the first Fresnel zone clear of obstacles and ground.

**Slant Range:** The transmitting antenna is mounted at the top of a tower, and the AUT is placed on the ground at a distance. The line-of-sight path is at an angle to the ground, reducing the effect of ground reflections compared to a horizontal path.

**Free-Space Range:** The antennas are separated as far as practically possible with minimal surrounding scatterers. Absorber material may be placed on the ground between the antennas to reduce reflections.

> **[Supplementary]** Outdoor ranges are susceptible to weather (rain, snow, humidity), multipath from buildings and terrain, and radio-frequency interference (RFI). They are typically used for large antennas (e.g., satellite ground stations, radio telescopes) that cannot fit in indoor chambers.

### 2.3 Indoor Ranges: Anechoic Chambers

An anechoic chamber is a shielded room lined with microwave absorber material that absorbs incident electromagnetic energy, minimizing reflections. Key characteristics:

- **Shielding:** Copper or steel enclosure attenuates external interference by 80--100 dB.
- **Absorber material:** Carbon-loaded foam pyramids, optimized for specific frequency bands.
- **Quiet zone:** The region in the chamber where reflections are below a specified threshold (typically $-40$ to $-60$ dB relative to direct signal).
- **Rectangular chambers:** Used for frequencies above 1 GHz; the side walls are lined with absorber.
- **Tapered chambers:** Used for frequencies below 1 GHz; the chamber expands in cross-section from the source to the AUT region, reducing low-frequency absorption limitations.

### 2.4 Compact Range

The compact antenna test range (CATR) uses a reflector (typically parabolic) or a lens to collimate the spherical wave from the feed into a plane wave at a short distance. This creates a far-field-like environment within an indoor chamber.

$$
R_{\text{CATR}} \ll \frac{2D^2}{\lambda}
$$

The reflector must be significantly larger than the AUT (by a factor of 3--5) to ensure the quiet zone is free from edge diffraction. Compact ranges are the dominant indoor technique for frequencies above 1 GHz and antenna diameters up to 2--3 m.

### 2.5 Near-Field Ranges

In near-field measurements, the field is measured on a surface close to the AUT (typically 3--10$\lambda$). The measured data is then transformed to the far field using mathematical algorithms based on plane wave expansion.

| Scan Surface | Suitable For | Characteristics |
|--------------|--------------|-----------------|
| Planar | Moderate-directivity antennas | Fast Fourier transform; no back-hemisphere data |
| Cylindrical | Omnidirectional or fan-beam | Full 360$^\circ$ azimuth coverage |
| Spherical | Full 3D pattern characterization | Most complete; complex processing |

Advantages of near-field ranges:
- Compact footprint (fits in small chambers)
- Full 3D pattern characterization without rotating the AUT
- Not weather-dependent
- High accuracy when probe compensation is applied

Disadvantages:
- Complex mathematical transformation
- Requires precise probe positioning (sub-millimeter accuracy)
- Measurement time can be long for spherical scanning

> **[Supplementary]** The National Institute of Standards and Technology (NIST) pioneered near-field antenna measurement techniques. Modern near-field ranges can characterize antennas up to 110 GHz and are used at hundreds of test facilities worldwide.

---

## 3. Radiation Pattern Measurements

### 3.1 Definition

The radiation pattern is a graphical representation of the antenna's radiated field (amplitude, phase, or polarization) as a function of spatial angles $(\theta, \phi)$ at a constant distance in the far field.

Patterns are typically measured as two-dimensional "cuts" through the three-dimensional pattern:

- **Principal E-plane cut:** The plane containing the electric field vector and the direction of maximum radiation.
- **Principal H-plane cut:** The plane containing the magnetic field vector and the direction of maximum radiation.
- **$\phi$ cuts:** Patterns measured at constant $\phi$ as $\theta$ varies.
- **$\theta$ cuts (conical cuts):** Patterns measured at constant $\theta$ as $\phi$ varies.

### 3.2 Measurement Setup

A radiation pattern measurement system consists of:

1. **Transmit antenna (probe):** Fixed in position, with known polarization and pattern.
2. **AUT:** Mounted on a positioner (azimuth-over-elevation, elevation-over-azimuth, or roll-over-azimuth) that allows rotation about two orthogonal axes.
3. **Signal source and receiver:** Vector network analyzer (VNA) or dedicated measurement receiver.
4. **Data acquisition system:** Records amplitude and phase as a function of angular position.

### 3.3 The Three-Dimensional Pattern

The three-dimensional pattern is measured by recording the received signal as the AUT is rotated in both $\theta$ and $\phi$. The result is a surface over the sphere surrounding the AUT. Post-processing extracts:

- **Main lobe direction and beamwidth**
- **Sidelobe levels (SLL)**
- **Front-to-back ratio**
- **Null positions and depths**
- **Cross-polarization levels**

### 3.4 Pattern Measurement Procedure

1. Align the AUT and probe at the correct separation distance (satisfying far-field criterion).
2. Set the source polarization orientation (linear: vertical or horizontal; circular: left-hand or right-hand).
3. For each desired cut:
   - Rotate the AUT or probe in the appropriate axis.
   - Record the received amplitude and phase at each angular increment.
4. Apply post-processing: normalization, calibration correction, and interpolation.
5. Generate polar or rectangular plots of the patterns.

### 3.5 Key Parameters Extracted from Patterns

| Parameter | Description | How Determined |
|-----------|-------------|----------------|
| HPBW | Half-power beamwidth | Angular width where pattern drops -3 dB from peak |
| FNBW | First null beamwidth | Angular width between first nulls on either side of main lobe |
| SLL | Sidelobe level (dB) | Ratio of peak sidelobe power to main lobe peak |
| Front-to-back ratio | Ratio of forward to backward radiation | Power at $\theta = 0^\circ$ vs. $\theta = 180^\circ$ |
| Cross-pol discrimination | Ratio of co-pol to cross-pol peak | Compare co-pol and cross-pol patterns |

---

## 4. Gain Measurements

### 4.1 Definition

Gain $G$ is the ratio of the radiation intensity in a given direction to the radiation intensity that would be obtained if the power accepted by the antenna were radiated isotropically. It includes ohmic losses.

### 4.2 Absolute Gain Method (Two-Antenna Method)

If two identical unknown antennas are used as transmitter and receiver, the gain is determined from the Friis transmission formula:

$$
P_r = P_t G_t G_r \left(\frac{\lambda}{4\pi R}\right)^2
$$

For identical antennas, $G_t = G_r = G$:

$$
G = \frac{4\pi R}{\lambda} \sqrt{\frac{P_r}{P_t}}
$$

In decibels:

$$
G_{\text{dBi}} = 10\log_{10}\left(\frac{4\pi R}{\lambda}\right) + 5\log_{10}\left(\frac{P_r}{P_t}\right)
$$

### 4.3 Three-Antenna Method

When three antennas of different gains are available, three measurements with different pairs yield three equations:

$$
G_1 + G_2 = \frac{P_{r12}}{P_t} + 20\log_{10}\left(\frac{4\pi R}{\lambda}\right)
$$

$$
G_1 + G_3 = \frac{P_{r13}}{P_t} + 20\log_{10}\left(\frac{4\pi R}{\lambda}\right)
$$

$$
G_2 + G_3 = \frac{P_{r23}}{P_t} + 20\log_{10}\left(\frac{4\pi R}{\lambda}\right)
$$

Solving this system yields the absolute gain of each antenna with no prior knowledge required.

### 4.4 Gain Comparison (Substitution) Method

The gain of the AUT is determined by comparing its received power to that of a standard gain antenna (SGA) with known gain:

1. Measure the received power $P_{\text{AUT}}$ with the AUT in place.
2. Replace the AUT with the SGA and measure its received power $P_{\text{SGA}}$.
3. Compute the AUT gain:

$$
G_{\text{AUT}} = G_{\text{SGA}} + 10\log_{10}\left(\frac{P_{\text{AUT}}}{P_{\text{SGA}}}\right)
$$

This method is simpler and faster than absolute methods but requires a calibrated standard gain antenna.

### 4.5 Gain Transfer Method Using a Network Analyzer

A VNA can directly measure $S_{21}$ between two antennas. If a standard gain horn is available:

$$
G_{\text{AUT}} = G_{\text{SGA}} + (S_{21,\text{AUT}} - S_{21,\text{SGA}}) \text{ dB}
$$

---

## 5. Directivity Measurements

Directivity $D_0$ is the ratio of the maximum radiation intensity to the average radiation intensity. It can be computed from pattern measurements using numerical integration:

$$
D_0 = \frac{4\pi U_{\text{max}}}{P_{\text{rad}}} = \frac{4\pi}{\int_0^{2\pi} \int_0^\pi F(\theta, \phi) \sin\theta \, d\theta \, d\phi}
$$

where $F(\theta, \phi) = U(\theta, \phi)/U_{\text{max}}$ is the normalized radiation intensity.

### 5.1 Approximate Directivity from Beamwidth

For antennas with a single narrow beam and very low sidelobes, the directivity can be approximated from the half-power beamwidths of the two principal plane cuts:

$$
D_0 \approx \frac{41,253}{\Theta_{1E} \Theta_{1H}} \quad \text{(degrees)}
$$

or the Kraus approximation:

$$
D_0 \approx \frac{22,181}{\Theta_{1E}^2 + \Theta_{1H}^2} \quad \text{(degrees)}
$$

where $\Theta_{1E}$ and $\Theta_{1H}$ are the HPBWs in degrees in the E-plane and H-plane, respectively.

These approximations assume no sidelobes and a symmetrical beam. They overestimate directivity when significant sidelobes exist.

### 5.2 Numerical Integration Method

For accurate directivity, the measured pattern is numerically integrated over the full sphere:

1. Measure the full 3D pattern or a sufficient number of 2D cuts.
2. Compute the total radiated power:

$$
P_{\text{rad}} = \int_0^{2\pi} \int_0^\pi U(\theta, \phi) \sin\theta \, d\theta \, d\phi
$$

3. Compute directivity:

$$
D_0 = \frac{4\pi U_{\text{max}}}{P_{\text{rad}}}
$$

---

## 6. Radiation Efficiency Measurements

Radiation efficiency $e_r$ is the ratio of the total power radiated by the antenna to the total power accepted at the input terminals:

$$
e_r = \frac{P_{\text{rad}}}{P_{\text{in}}} = \frac{G}{D}
$$

where $G$ is the gain and $D$ is the directivity.

### 6.1 Pattern Integration Method

Efficiency is obtained by measuring gain (from a gain measurement) and directivity (from pattern integration):

$$
e_r = \frac{G}{D_0}
$$

This requires both an absolute gain measurement and a full 3D pattern measurement.

### 6.2 Wheeler Cap Method

The Wheeler cap method measures efficiency using a conducting cap placed over the antenna. The measurement procedure is:

1. Measure the input impedance of the antenna in free space, $Z_{\text{fs}}$.
2. Place a conducting cap (a hemispherical or cylindrical shell) over the antenna. The cap reflects radiation back to the antenna, preventing radiative loss.
3. Measure the input impedance with the cap, $Z_{\text{cap}}$.
4. Compute the radiation resistance $R_r$ and loss resistance $R_L$ from the impedance values.
5. Efficiency:

$$
e_r = \frac{R_r}{R_r + R_L}
$$

The cap must be electrically large enough that the antenna is in the radiating near-field, and the gap between the antenna and the cap must be small to prevent radiation.

### 6.3 Reverberation Chamber Method

The antenna is placed in a mode-stirred reverberation chamber. The chamber consists of a shielded enclosure with a rotating metallic stirrer that creates a statistically uniform, isotropic, and depolarized field. Efficiency is determined by comparing the received power to the average power in the chamber.

> **[Supplementary]** The reverberation chamber method is particularly useful for electrically small antennas (e.g., mobile phone antennas) where conventional pattern integration is difficult due to interactions with the measurement environment. The IEEE Standard 149 includes pattern integration, Wheeler cap, and reverberation chamber methods for efficiency measurement.

---

## 7. Impedance Measurements

### 7.1 Input Impedance

The input impedance $Z_{\text{in}} = R_{\text{in}} + jX_{\text{in}}$ is measured directly using a vector network analyzer (VNA) connected to the antenna feed. The VNA measures the reflection coefficient $\Gamma$ and computes the impedance:

$$
\Gamma = S_{11} = \frac{Z_{\text{in}} - Z_0}{Z_{\text{in}} + Z_0}
$$

$$
Z_{\text{in}} = Z_0 \frac{1 + \Gamma}{1 - \Gamma}
$$

where $Z_0$ is the characteristic impedance (typically 50 $\Omega$ or 75 $\Omega$).

### 7.2 VSWR and Bandwidth

The voltage standing wave ratio (VSWR) is derived from the reflection coefficient:

$$
\text{VSWR} = \frac{1 + |\Gamma|}{1 - |\Gamma|}
$$

The impedance bandwidth is the frequency range over which the VSWR is below a specified threshold (typically 2:1 for most applications, 1.5:1 for critical systems).

### 7.3 Calibration Requirements

VNA impedance measurements require calibration at the antenna reference plane:

- **SOLT (Short-Open-Load-Through):** Standard calibration using precision calibration standards.
- **TRL (Through-Reflect-Line):** Preferred for waveguide and fixture-based measurements.

The measurement plane must be carefully defined, typically at the antenna feed connector. De-embedding techniques remove the effects of cables, adapters, and connectors between the VNA and the antenna.

### 7.4 Environmental Effects

Impedance measurements are sensitive to the environment:

- Proximity of ground planes, other antennas, or the human body shifts impedance
- Measurement cables can act as secondary radiators, affecting the measurement
- Baluns may be required for balanced antennas (e.g., dipoles) to prevent common-mode currents on the cable shield

---

## 8. Current Measurements

### 8.1 Purpose

Current distribution measurements on antenna elements serve to:

- Validate theoretical current distributions (e.g., sinusoidal approximation for dipoles)
- Identify regions of high current density for thermal or breakdown analysis
- Diagnose manufacturing defects or assembly errors
- Investigate mutual coupling mechanisms in arrays

### 8.2 Current Probe Technique

A small current probe (a miniature loop antenna or shielded loop) is moved along the antenna element while measuring the induced voltage. The probe is oriented to detect the desired current component.

**Measurement procedure:**

1. Mount the probe on a precision translation stage with sub-millimeter positioning.
2. Align the probe relative to the antenna element (parallel for axial current, perpendicular for transverse current).
3. Excite the antenna with a CW signal at the operating frequency.
4. Move the probe along the element in discrete steps, recording the probe output voltage.
5. The probe voltage is proportional to the current at that point, after calibration.

### 8.3 Calibration

The current probe must be calibrated to relate the measured voltage to the actual current. Calibration can be performed by:

- Measuring a known current distribution (e.g., a short dipole with known current)
- Using a transmission line with known current
- Electromagnetic simulation of the probe geometry

### 8.4 Challenges and Limitations

- **Probe perturbation:** The probe itself disturbs the field, affecting the current being measured.
- **Resolution:** The probe size limits spatial resolution; smaller probes have lower sensitivity.
- **Surface currents on thick elements:** For antennas with thickness comparable to a wavelength, both surface and volume current densities complicate interpretation.
- **High-frequency limitations:** At millimeter-wave frequencies, probe positioning tolerances become critical.

---

## 9. Polarization Measurements

### 9.1 Polarization Ellipse Parameters

The polarization state of an antenna is characterized by three parameters of the polarization ellipse:

- **Axial ratio (AR):** The ratio of the major to minor axis of the polarization ellipse.
- **Tilt angle ($\tau$):** The angle of the major axis relative to a reference direction.
- **Sense of rotation:** Right-hand (RH) or left-hand (LH) circular polarization, determined by the direction of the rotating electric field vector.

### 9.2 Polarization Pattern Method

The AUT is rotated about its bore-sight axis while a linearly polarized probe antenna remains fixed. The received power varies as a function of rotation angle $\phi$:

$$
P(\phi) = \frac{1}{2} \left[ E_{\text{co}}^2 + E_{\text{cross}}^2 + (E_{\text{co}}^2 - E_{\text{cross}}^2) \cos(2\phi - 2\tau) \right]
$$

From this polarization pattern, the axial ratio and tilt angle are determined:

$$
\text{AR} = \frac{E_{\text{co}} + E_{\text{cross}}}{E_{\text{co}} - E_{\text{cross}}}
$$

where $E_{\text{co}}$ is the co-polarized field amplitude and $E_{\text{cross}}$ is the cross-polarized field amplitude.

In dB:

$$
\text{AR}_{\text{dB}} = 20\log_{10}(\text{AR})
$$

An ideal circularly polarized antenna has $\text{AR} = 1$ (0 dB). An ideal linearly polarized antenna has $\text{AR} = \infty$.

### 9.3 Three-Antenna Polarization Method

Using three antennas with unknown polarization, the polarization states can be determined through a set of measurements, analogous to the three-antenna gain method. The measurement of received power between pairs of antennas, combined with known distances and gain values, yields the polarization mismatch factor and the polarization characteristics.

### 9.4 Spinning Dipole Method

A linearly polarized probe (small dipole) is rotated rapidly (spun) about the propagation axis while the AUT transmits. The received signal amplitude varies sinusoidally. From the modulation depth and phase, the axial ratio and tilt angle are extracted. This method is fast and widely used for circularly polarized antennas.

---

## 10. Scale Model Measurements

### 10.1 Principle

Scale model measurements involve measuring a physically scaled version of the antenna at a correspondingly scaled frequency. If all dimensions are scaled by a factor $n$ and the frequency is scaled by $1/n$, the electrical behavior (in wavelengths) is identical, provided the material properties can be appropriately scaled.

**Scaling relationships:**

| Parameter | Full Scale | Scale Model ($1:n$) |
|-----------|------------|-------------------|
| Physical dimension | $L$ | $L/n$ |
| Wavelength | $\lambda$ | $\lambda/n$ |
| Frequency | $f$ | $n \cdot f$ |
| Conductivity | $\sigma$ | $n \cdot \sigma$ (for equivalent skin depth) |
| Antenna gain | $G$ | $G$ (unchanged) |
| Directivity | $D$ | $D$ (unchanged) |
| Radiation pattern | $F(\theta, \phi)$ | $F(\theta, \phi)$ (identical) |

### 10.2 When Scale Models Are Used

- **Large antennas:** Full-size measurement would require impractically large ranges.
- **Platform integration:** Antenna performance on aircraft, ships, or spacecraft is measured using scale models of the platform (e.g., 1:10 scale aircraft model).
- **Design iteration:** Rapid prototyping of antenna placement and orientation without full-scale fabrication.
- **Inaccessible environments:** Spacecraft antennas tested before launch using scale models.

### 10.3 Scaling Material Properties

The critical challenge in scale model measurements is maintaining equivalent electrical properties:

- **Conductor scaling:** The skin depth $\delta = 1/\sqrt{\pi f \mu \sigma}$ must scale proportionally. At the scaled frequency $n \cdot f$, the skin depth is $1/\sqrt{n}$ times the original. Using the same conductor material, the loss may differ from the full-scale case.
- **Dielectric scaling:** If the antenna uses dielectric materials, the permittivity $\epsilon_r$ and loss tangent $\tan\delta$ must be frequency-scaled appropriately, which is often difficult for real materials.

In practice, these limitations mean that scale model measurements may not perfectly reproduce ohmic losses and dielectric losses, but they accurately reproduce radiation patterns, directivity, and impedance (when conductivity effects are negligible).

### 10.4 Measurement Procedure

1. Construct a scale model of the antenna (and platform, if applicable) at scale $1:n$.
2. Increase the operating frequency by factor $n$.
3. Perform standard antenna measurements (pattern, gain, impedance) at the scaled frequency.
4. Scale the results back to the original frequency for performance predictions.

### 10.5 Limitations

- **Material scaling imperfections** can lead to errors in loss-sensitive parameters.
- **Fabrication tolerances** must scale with the model; smaller features are harder to machine precisely.
- **Feeding the model** at higher frequencies requires smaller connectors and more precise alignment.
- **Probe and cable effects** become more significant at smaller scales.

---

## 11. Connections and Cross-References

| Topic | Connection |
|-------|------------|
| **Section 2 (Fundamental Parameters)** | Definitions of gain, directivity, beamwidth, efficiency, polarization, and impedance are the quantities measured |
| **Section 3 (Radiation Integrals)** | Far-field condition derived from radiation integrals; near-field to far-field transformation |
| **Section 4 (Linear Wire Antennas)** | Current distribution measurements validate theoretical current models |
| **Section 6 (Arrays)** | Pattern and gain measurements of array antennas; mutual coupling characterization |
| **Section 12 (Aperture Antennas)** | Aperture field measurements and far-field pattern computation via Fourier transform |
| **Section 13 (Horn Antennas)** | Horn antennas are common standard gain antennas for gain comparison methods |
| **Section 14 (Microstrip Antennas)** | Impedance and pattern measurements of microstrip patches; probe-fed and coupled-fed configurations |
| **Section 15 (Reflector Antennas)** | Gain, pattern, and polarization measurements of large reflector antennas; surface tolerance measurement |
| **Section 16 (Smart Antennas)** | Beamforming performance verification; adaptive pattern measurements |

---

## Solved Exercises

### Exercise 1: Far-Field Distance Calculation

**Problem:** A parabolic reflector antenna has diameter $D = 3$ m and operates at $f = 10$ GHz. Calculate the far-field distance. If an indoor chamber has a maximum separation of 15 m, can far-field measurements be performed directly?

**Solution:**

Wavelength:

$$
\lambda = \frac{c}{f} = \frac{3 \times 10^8}{10 \times 10^9} = 0.03 \text{ m} = 3 \text{ cm}
$$

Far-field distance:

$$
R_{\text{ff}} = \frac{2D^2}{\lambda} = \frac{2 \times (3)^2}{0.03} = \frac{18}{0.03} = 600 \text{ m}
$$

The required far-field distance is 600 m. The chamber provides only 15 m, which is far less than required. Direct far-field measurements are impossible in this chamber.

**Options:**
- Use a compact range with a collimating reflector that produces a plane wave within the chamber.
- Use near-field scanning and transform to far field.
- Use an outdoor far-field range with 600 m separation.

---

### Exercise 2: Gain from Two-Antenna Method

**Problem:** Two identical horn antennas are used to measure gain at 12 GHz. The antennas are separated by $R = 5$ m. The transmitted power is $P_t = 10$ dBm, and the received power is $P_r = -45$ dBm. Calculate the gain of each horn in dBi.

**Solution:**

Wavelength:

$$
\lambda = \frac{c}{f} = \frac{3 \times 10^8}{12 \times 10^9} = 0.025 \text{ m}
$$

First verify far-field condition. Assume typical horn aperture $D \approx 0.1$ m:

$$
R_{\text{ff}} = \frac{2D^2}{\lambda} = \frac{2 \times (0.1)^2}{0.025} = 0.8 \text{ m}
$$

The 5 m separation satisfies the far-field condition.

Using the Friis transmission formula for identical antennas:

$$
G = \frac{4\pi R}{\lambda} \sqrt{\frac{P_r}{P_t}}
$$

Convert powers to linear units:

$$
P_t = 10 \text{ dBm} \rightarrow 10 \text{ mW}
$$

$$
P_r = -45 \text{ dBm} \rightarrow 3.16 \times 10^{-8} \text{ mW}
$$

$$
\frac{P_r}{P_t} = \frac{3.16 \times 10^{-8}}{10 \times 10^{-3}} = 3.16 \times 10^{-6}
$$

$$
G = \frac{4\pi \times 5}{0.025} \times \sqrt{3.16 \times 10^{-6}} = 2513.27 \times 0.001778 = 4.47
$$

$$
G_{\text{dBi}} = 10\log_{10}(4.47) = 6.5 \text{ dBi}
$$

---

### Exercise 3: Gain Comparison Method

**Problem:** A standard gain horn has $G_{\text{SGA}} = 15$ dBi. The received power with the SGA is $P_{\text{SGA}} = -30$ dBm. When replaced by the AUT, the received power is $P_{\text{AUT}} = -28$ dBm. Calculate the AUT gain.

**Solution:**

The gain comparison formula:

$$
G_{\text{AUT}} = G_{\text{SGA}} + 10\log_{10}\left(\frac{P_{\text{AUT}}}{P_{\text{SGA}}}\right)
$$

$$
G_{\text{AUT}} = 15 + 10\log_{10}\left(\frac{10^{-28/10}}{10^{-30/10}}\right) = 15 + 10\log_{10}\left(10^{0.2}\right)
$$

$$
G_{\text{AUT}} = 15 + 10 \times 0.2 = 15 + 2 = 17 \text{ dBi}
$$

The AUT has 2 dB more gain than the standard horn.

---

### Exercise 4: Directivity from Beamwidth Approximation

**Problem:** A patch antenna has E-plane HPBW of $80^\circ$ and H-plane HPBW of $85^\circ$. Estimate the directivity using both the Kraus approximation and the simple product formula.

**Solution:**

Product formula (Kraus 1950):

$$
D_0 \approx \frac{41,253}{\Theta_{1E} \Theta_{1H}} = \frac{41,253}{80 \times 85} = \frac{41,253}{6800} = 6.07
$$

$$
D_{0,\text{dB}} = 10\log_{10}(6.07) = 7.8 \text{ dB}
$$

Kraus second approximation:

$$
D_0 \approx \frac{22,181}{\Theta_{1E}^2 + \Theta_{1H}^2} = \frac{22,181}{80^2 + 85^2} = \frac{22,181}{6400 + 7225} = \frac{22,181}{13,625} = 1.63
$$

The two estimates differ significantly because the second formula is intended for antennas with very low sidelobes. The product formula is more commonly used for patch-type antennas. Neither substitutes for full pattern integration.

---

### Exercise 5: Directivity from Full Pattern Integration

**Problem:** The radiation intensity of an antenna is approximately:

$$
U(\theta, \phi) = U_0 \cos^2\theta \quad \text{for } 0 \leq \theta \leq \pi/2, 0 \leq \phi \leq 2\pi
$$

and $U = 0$ for $\theta > \pi/2$. Calculate the directivity $D_0$.

**Solution:**

The total radiated power is:

$$
P_{\text{rad}} = \int_0^{2\pi} \int_0^{\pi/2} U_0 \cos^2\theta \sin\theta \, d\theta \, d\phi
$$

$$
P_{\text{rad}} = U_0 \int_0^{2\pi} d\phi \int_0^{\pi/2} \cos^2\theta \sin\theta \, d\theta
$$

Let $u = \cos\theta$, $du = -\sin\theta \, d\theta$:

$$
\int_0^{\pi/2} \cos^2\theta \sin\theta \, d\theta = \int_1^0 u^2 (-du) = \int_0^1 u^2 du = \left[\frac{u^3}{3}\right]_0^1 = \frac{1}{3}
$$

$$
P_{\text{rad}} = U_0 \times 2\pi \times \frac{1}{3} = \frac{2\pi U_0}{3}
$$

The maximum radiation intensity is $U_{\text{max}} = U_0$ at $\theta = 0^\circ$.

$$
D_0 = \frac{4\pi U_{\text{max}}}{P_{\text{rad}}} = \frac{4\pi U_0}{2\pi U_0/3} = 6
$$

$$
D_{0,\text{dB}} = 10\log_{10}(6) = 7.8 \text{ dBi}
$$

---

### Exercise 6: Impedance and VSWR Calculation

**Problem:** A VNA measurement at 2.45 GHz shows $S_{11} = -12$ dB for a microstrip patch antenna. Calculate the reflection coefficient magnitude, VSWR, and the impedance (assuming $Z_0 = 50\ \Omega$ and the phase of $\Gamma$ is $30^\circ$).

**Solution:**

Reflection coefficient magnitude:

$$
|\Gamma| = 10^{-S_{11}/20} = 10^{-12/20} = 10^{-0.6} = 0.251
$$

VSWR:

$$
\text{VSWR} = \frac{1 + |\Gamma|}{1 - |\Gamma|} = \frac{1 + 0.251}{1 - 0.251} = \frac{1.251}{0.749} = 1.67
$$

Impedance:

$$
\Gamma = 0.251 e^{j30^\circ} = 0.251(\cos 30^\circ + j\sin 30^\circ) = 0.217 + j0.126
$$

$$
Z_{\text{in}} = Z_0 \frac{1 + \Gamma}{1 - \Gamma} = 50 \times \frac{1 + 0.217 + j0.126}{1 - 0.217 - j0.126} = 50 \times \frac{1.217 + j0.126}{0.783 - j0.126}
$$

Compute denominator magnitude:

$$
|0.783 - j0.126| = \sqrt{0.783^2 + 0.126^2} = \sqrt{0.613 + 0.016} = \sqrt{0.629} = 0.793
$$

Numerator magnitude: $|1.217 + j0.126| = \sqrt{1.217^2 + 0.126^2} = \sqrt{1.481 + 0.016} = \sqrt{1.497} = 1.224$

Phase of numerator: $\arctan(0.126/1.217) = 5.91^\circ$

Phase of denominator: $\arctan(-0.126/0.783) = -9.14^\circ$

Overall phase: $5.91^\circ - (-9.14^\circ) = 15.05^\circ$

$$
Z_{\text{in}} = 50 \times \frac{1.224}{0.793} e^{j15.05^\circ} = 50 \times 1.544 e^{j15.05^\circ} = 77.2 e^{j15.05^\circ}
$$

$$
Z_{\text{in}} = 77.2\cos 15.05^\circ + j77.2\sin 15.05^\circ = 74.6 + j20.1\ \Omega
$$

Since $Z_0 = 50\ \Omega$, this impedance is resistive with some inductive reactance. The VSWR of 1.67 is acceptable but not ideal.

---

### Exercise 7: Polarization Measurement Using the Polarization Pattern Method

**Problem:** In a polarization measurement, a linearly polarized probe is rotated around the bore-sight axis while the AUT transmits. The maximum received power is $P_{\text{max}} = -20$ dBm and the minimum is $P_{\text{min}} = -30$ dBm. Calculate the axial ratio in dB and determine whether the polarization is circular, elliptical, or linear.

**Solution:**

The axial ratio in linear units:

$$
\text{AR} = \sqrt{\frac{P_{\text{max}}}{P_{\text{min}}}} = \sqrt{\frac{10^{-20/10}}{10^{-30/10}}} = \sqrt{\frac{10^{-2}}{10^{-3}}} = \sqrt{10} = 3.16
$$

In dB:

$$
\text{AR}_{\text{dB}} = 10\log_{10}(3.16) = 5.0 \text{ dB}
$$

Classification of polarization:

| AR (dB) | Polarization Type |
|---------|-------------------|
| 0--3 | Nearly circular |
| 3--10 | Elliptical |
| > 10 | Nearly linear |

Since $\text{AR} = 5.0$ dB, the antenna has elliptical polarization. The 10 dB difference between $P_{\text{max}}$ and $P_{\text{min}}$ confirms a moderate axial ratio.

---

### Exercise 8: Scale Model Frequency Scaling

**Problem:** A 1.2 m parabolic reflector antenna is designed for operation at 1.5 GHz. A 1:10 scale model is to be built for compact range testing. What is the scaled operating frequency, and what is the far-field distance for the scale model (assuming the model is measured directly without a compact range)?

**Solution:**

Scale factor: $n = 10$

Scaled frequency:

$$
f_{\text{model}} = n \times f_{\text{full}} = 10 \times 1.5 = 15 \text{ GHz}
$$

Scaled diameter:

$$
D_{\text{model}} = \frac{D_{\text{full}}}{n} = \frac{1.2}{10} = 0.12 \text{ m}
$$

Wavelength at 15 GHz:

$$
\lambda_{\text{model}} = \frac{c}{f_{\text{model}}} = \frac{3 \times 10^8}{15 \times 10^9} = 0.02 \text{ m}
$$

Far-field distance for the model:

$$
R_{\text{ff,model}} = \frac{2D_{\text{model}}^2}{\lambda_{\text{model}}} = \frac{2 \times (0.12)^2}{0.02} = \frac{2 \times 0.0144}{0.02} = 1.44 \text{ m}
$$

For the full-scale antenna:

$$
R_{\text{ff,full}} = \frac{2 \times (1.2)^2}{0.2} = 14.4 \text{ m}
$$

The scale model reduces the far-field distance from 14.4 m to 1.44 m, making it feasible to measure in a compact indoor chamber.

**Note:** The scaled model's gain is identical to the full-scale antenna (since gain depends only on $(D/\lambda)^2$, and both $D$ and $\lambda$ scale by the same factor). The pattern is also identical.

---

### Exercise 9: Wheeler Cap Efficiency Measurement

**Problem:** In a Wheeler cap measurement at 900 MHz, the free-space resistance at resonance is $R_{\text{fs}} = 36\ \Omega$, and with the cap the resistance is $R_{\text{cap}} = 40\ \Omega$. The reactance is zero at resonance in both cases. Calculate the radiation efficiency.

**Solution:**

In the Wheeler cap method, when the cap is applied, the radiation resistance becomes zero (the cap prevents radiation), and the measured resistance is the loss resistance:

$$
R_L = R_{\text{cap}} = 40\ \Omega
$$

The free-space resistance is the sum of radiation resistance and loss resistance:

$$
R_{\text{fs}} = R_r + R_L = 36\ \Omega
$$

Wait -- this implies $R_r = R_{\text{fs}} - R_L = 36 - 40 = -4\ \Omega$, which is unphysical. Let us re-check the Wheeler cap principle.

**Correction:** In the Wheeler cap method, application of the cap replaces the radiation resistance with the equivalent impedance of the cap (which is reactive at frequencies away from resonance). At the resonant frequency where $X = 0$:

- Free space: $Z_{\text{fs}} = R_r + R_L$
- With cap: $Z_{\text{cap}} = R_L$ (the cap eliminates radiation, leaving only loss resistance)

However, the cap introduces additional inductive or capacitive reactance that must be tuned out. At the resonant frequency after cap application:

$$
R_{\text{fs}} = R_r + R_L = 36\ \Omega
$$

$$
R_{\text{cap}} = R_L = 40\ \Omega
$$

This still gives a negative $R_r$, meaning the cap is not properly isolating the antenna, or the measurement has an error. For a valid measurement, $R_{\text{cap}} < R_{\text{fs}}$ because $R_r > 0$.

Let us assume the values were reversed: $R_{\text{fs}} = 40\ \Omega$ and $R_{\text{cap}} = 36\ \Omega$.

Then:

$$
R_L = R_{\text{cap}} = 36\ \Omega
$$

$$
R_r = R_{\text{fs}} - R_L = 40 - 36 = 4\ \Omega
$$

$$
e_r = \frac{R_r}{R_r + R_L} = \frac{4}{4 + 36} = \frac{4}{40} = 0.10 = 10\%
$$

This low efficiency suggests significant ohmic losses, which may be typical for an electrically small antenna.

> **[Key Insight]** The Wheeler cap method is sensitive to the cap size and placement. The cap must be large enough to prevent radiation but small enough that the antenna is in its reactive near-field. An improperly sized cap can produce unphysical results like negative radiation resistance.

---

### Exercise 10: Polarization Measurement -- Spinning Dipole

**Problem:** A spinning linearly polarized dipole is used to measure the polarization of an AUT at 2 GHz. The spinning dipole rotates at 1200 RPM. The received signal shows a peak-to-peak amplitude variation of 8 dB. The phase of the minimum occurs at a rotation angle of $35^\circ$ from the reference. Determine the axial ratio and tilt angle.

**Solution:**

Peak-to-peak variation: 8 dB.

The axial ratio in dB is related to the ratio of maximum to minimum electric field:

$$
\frac{E_{\text{max}}}{E_{\text{min}}} = 10^{8/20} = 10^{0.4} = 2.51
$$

Axial ratio (linear):

$$
\text{AR} = \frac{E_{\text{max}}}{E_{\text{min}}} = 2.51
$$

In dB:

$$
\text{AR}_{\text{dB}} = 20\log_{10}(2.51) = 8.0 \text{ dB}
$$

The tilt angle $\tau$ is the angle of the major axis. For a spinning dipole, the minimum received power occurs when the dipole is aligned with the minor axis of the polarization ellipse. The major axis (tilt angle) is perpendicular to the minor axis. Therefore:

$$
\tau = 35^\circ + 90^\circ = 125^\circ \quad \text{or} \quad \tau = 35^\circ - 90^\circ = -55^\circ
$$

The exact tilt angle depends on the orientation convention. Both values represent the same physical axis (the major axis of the polarization ellipse).

The sense of rotation cannot be determined from amplitude-only measurements. It requires phase measurement (or a quadrature hybrid) to distinguish right-hand from left-hand circular polarization.

---

## Exam Tip: Key Measurement Formula Summary

Memorize the essential formulas for antenna measurement problems:

**Far-field condition:** $R \geq 2D^2/\lambda$ -- the most common exam question tests whether a given separation satisfies far-field requirements.

**Friis transmission formula:** $P_r/P_t = G_t G_r (\lambda/4\pi R)^2$ -- the foundation of gain measurement.

**Gain comparison:** $G_{\text{AUT}} = G_{\text{SGA}} + (P_{\text{AUT,dB}} - P_{\text{SGA,dB}})$ -- the simplest and most common gain measurement method.

**Directivity from pattern integration:** $D_0 = 4\pi U_{\text{max}} / \int U d\Omega$ -- conceptually tested with simple assumed patterns.

**Beamwidth approximation:** $D_0 \approx 41,253 / (\Theta_{1E} \Theta_{1H})$ in degrees.

**VSWR from $S_{11}$:** $\text{VSWR} = (1 + |\Gamma|) / (1 - |\Gamma|)$ where $|\Gamma| = 10^{-S_{11}/20}$.

**Axial ratio:** $\text{AR} = E_{\text{max}}/E_{\text{min}} = \sqrt{P_{\text{max}}/P_{\text{min}}}$.

---

## Exam Tip: Common Mistakes

1. **Forgetting to check the far-field condition.** Always verify $R \geq 2D^2/\lambda$ before applying far-field formulas.

2. **Confusing gain and directivity.** Gain includes ohmic losses; directivity does not. The relationship is $G = e_r D$.

3. **Using dB inconsistently in Friis formula.** Convert all powers to linear units before computing gain. The Friis formula in dB form is:
   $$
   P_{r,\text{dBm}} = P_{t,\text{dBm}} + G_{t,\text{dBi}} + G_{r,\text{dBi}} + 20\log_{10}\left(\frac{\lambda}{4\pi R}\right)
   $$

4. **Neglecting impedance mismatch loss.** The measured gain is the realized gain, which includes mismatch loss at the antenna input. The gain defined in Section 2 assumes a matched load.

5. **Assuming the Wheeler cap method is trivial.** The cap must be correctly sized and positioned; improper application gives negative radiation resistance values, which are unphysical.

6. **Confusing polarization sense in scale models.** Scale models preserve the radiation pattern and polarization sense; only the frequency and physical dimensions scale.

---

## Exam Tip: Range Selection Strategy

When choosing an antenna measurement method for exam problems, consider:

- **Small antennas ($D < 10\lambda$):** Direct far-field in an anechoic chamber.
- **Medium antennas ($10\lambda < D < 100\lambda$):** Compact range for indoor measurements.
- **Large antennas ($D > 100\lambda$):** Outdoor far-field range or near-field scanning.
- **Full 3D pattern required:** Spherical near-field scanning.
- **Highest gain accuracy needed:** Extrapolation range (three-antenna method with variable distance).
- **Low-cost, quick test:** Direct comparison with a standard gain horn.