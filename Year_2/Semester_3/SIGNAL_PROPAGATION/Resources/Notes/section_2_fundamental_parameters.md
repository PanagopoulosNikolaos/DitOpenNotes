# Fundamental Parameters of Antennas

Antenna fundamental parameters are the set of metrics used to characterize the performance of any antenna in terms of its radiation properties, impedance behavior, polarization characteristics, and system-level interaction. These parameters enable quantitative comparison between different antenna designs and are essential for predicting link performance in wireless communication, radar, and sensing systems. This section defines each parameter formally, establishes the mathematical relationships between them, and provides worked examples demonstrating their computation and application.

---

## 1. Conceptual Foundation

### 1.1 Why Antenna Parameters Are Needed

An antenna is the interface between a guided-wave circuit (transmission line) and free-space propagation. To predict how much power is transferred from the transmitter to the receiver, the following must be known:

- How the antenna distributes power in space (radiation pattern, directivity, gain).
- How efficiently it converts guided power to radiated power (efficiency).
- Over what frequency range it operates effectively (bandwidth).
- How its orientation and wave polarization affect coupling (polarization mismatch).
- How the antenna interacts with the connected circuit (input impedance, VSWR).
- How much noise the antenna contributes to the system (antenna temperature).

These parameters are not independent: directivity, gain, efficiency, beamwidth, and effective area are related through fundamental electromagnetic relationships.

### 1.2 System-Level Perspective

In a communication link, the transmitter delivers power $P_t$ to its antenna, which radiates a fraction $e_{cd}$ (radiation efficiency) of that power. The radiated power is concentrated according to the directivity pattern. At the receiver, the antenna captures power according to its effective area and efficiency. The **Friis transmission equation** ties all these parameters together into a single link budget.

---

## 2. Formal Definitions and Models

### 2.1 Radiation Pattern

The **radiation pattern** (or antenna pattern) is a graphical or mathematical representation of the radiation properties of the antenna as a function of spatial coordinates (typically $\theta$ and $\phi$ in a spherical coordinate system).

**Normalized field pattern:**

$$
F(\theta, \phi) = \frac{|\mathbf{E}(\theta, \phi)|}{|\mathbf{E}_{\text{max}}|}
$$

**Normalized power pattern:**

$$
P_n(\theta, \phi) = \frac{S(\theta, \phi)}{S_{\text{max}}} = |F(\theta, \phi)|^2
$$

where $S(\theta, \phi)$ is the power density at $(\theta, \phi)$.

**Pattern lobes:**
- **Main lobe:** The lobe containing the direction of maximum radiation.
- **Side lobes:** All other lobes. The side lobe level (SLL) is typically expressed in dB relative to the main lobe peak.
- **Back lobe:** The lobe opposite the main lobe ($180^\circ$).

> **[Key Insight]** The radiation pattern is a far-field quantity. It is independent of distance $r$ in the far-field region ($r > 2D^2/\lambda$). Patterns measured at distances closer than this exhibit distance-dependent angular distributions and are not valid for system-level characterization.

### 2.2 Radiation Power Density

The **radiation power density** (or Poynting vector magnitude) at a point in space is the time-average power per unit area.

For the far-field region, where $\mathbf{E}$ and $\mathbf{H}$ are perpendicular and related by $\mathbf{H} = \frac{\hat{\mathbf{r}} \times \mathbf{E}}{\eta}$:

$$
S(\theta, \phi) = \frac{|\mathbf{E}(\theta, \phi)|^2}{2\eta} \quad \text{(W/m}^2\text{, peak formulation)}
$$

where $\eta = \sqrt{\mu/\epsilon} \approx 120\pi \;\Omega$ in free space.

The total radiated power is the integral of the power density over a closed sphere:

$$
P_{\text{rad}} = \oint_S S(\theta, \phi) \, dA = \int_0^{2\pi} \int_0^{\pi} S(\theta, \phi) r^2 \sin\theta \, d\theta \, d\phi
$$

### 2.3 Radiation Intensity

The **radiation intensity** $U(\theta, \phi)$ is the power radiated per unit solid angle (steradian):

$$
U(\theta, \phi) = r^2 S(\theta, \phi) \quad \text{(W/sr)}
$$

The key advantage of radiation intensity is that it is independent of distance $r$ in the far field.

Total radiated power in terms of radiation intensity:

$$
P_{\text{rad}} = \int_0^{2\pi} \int_0^{\pi} U(\theta, \phi) \sin\theta \, d\theta \, d\phi
$$

### 2.4 Beamwidth

Two beamwidth definitions are universally used:

**Half-Power Beamwidth (HPBW):** The angular width of the main lobe measured between the points where the power pattern drops to one-half ($-3$ dB) of its maximum value.

**First-Null Beamwidth (FNBW):** The angular width between the first nulls on either side of the main lobe.

For a uniform line source of length $L$:

$$
\text{HPBW} \approx \frac{0.886\lambda}{L} \quad \text{(radians, large } L/\lambda \text{)}
$$

$$
\text{FNBW} \approx \frac{2\lambda}{L} \quad \text{(radians)}
$$

> **[Key Insight]** There is a fundamental trade-off: higher directivity (narrower beam) requires a larger electrical aperture $D/\lambda$. This is the antenna equivalent of the Heisenberg uncertainty principle — you cannot simultaneously have a small antenna and a narrow beam.

### 2.5 Directivity

**Directivity** $D(\theta, \phi)$ is the ratio of the radiation intensity in a given direction to the radiation intensity averaged over all directions:

$$
D(\theta, \phi) = \frac{U(\theta, \phi)}{U_0} = \frac{4\pi U(\theta, \phi)}{P_{\text{rad}}}
$$

where $U_0 = P_{\text{rad}} / (4\pi)$ is the radiation intensity of an isotropic source radiating the same total power.

**Maximum directivity** $D_0$ (usually simply called "directivity") is the directivity in the direction of maximum radiation:

$$
D_0 = \frac{4\pi U_{\text{max}}}{P_{\text{rad}}}
$$

For a rotationally symmetric pattern with a single main lobe, an approximate formula is:

$$
D_0 \approx \frac{4\pi}{\Theta_{1r} \Theta_{2r}}
$$

where $\Theta_{1r}$ and $\Theta_{2r}$ are the HPBW in radians in two orthogonal planes.

**Kraus' approximate formula:**

$$
D_0 \approx \frac{41,253}{\Theta_{1d} \Theta_{2d}}
$$

where $\Theta_{1d}$ and $\Theta_{2d}$ are the HPBW in degrees.

> **[Key Insight]** Directivity is purely a function of the radiation pattern shape. It does not include ohmic losses in the antenna structure.

### 2.6 Numerical Techniques

When closed-form pattern integration is not possible, directivity and other parameters are computed numerically. For a pattern sampled at discrete angles $(\theta_i, \phi_j)$:

1. Compute $U_{ij} = U(\theta_i, \phi_j)$.
2. Compute the integral numerically:

   $$
   P_{\text{rad}} \approx \sum_{i} \sum_{j} U_{ij} \sin\theta_i \, \Delta\theta \, \Delta\phi
   $$

3. Compute $D_0 = 4\pi U_{\text{max}} / P_{\text{rad}}$.

Common integration rules: Simpson's rule, trapezoidal rule, or Gauss-Legendre quadrature.

### 2.7 Antenna Efficiency

The **total antenna efficiency** $e_0$ accounts for all losses in the antenna and its near environment:

$$
e_0 = e_r e_c e_d
$$

where:
- $e_r$ = reflection (mismatch) efficiency = $1 - |\Gamma|^2$, where $\Gamma = (Z_{\text{in}} - Z_0)/(Z_{\text{in}} + Z_0)$.
- $e_c$ = conduction efficiency (ohmic losses in conductors).
- $e_d$ = dielectric efficiency (losses in dielectric materials surrounding or supporting the antenna).

The product $e_{cd} = e_c e_d$ is the **radiation efficiency** (often denoted simply as $e$ or $\eta_{\text{rad}}$).

> **[Key Insight]** For well-matched antennas ($\Gamma \approx 0$), $e_0 \approx e_{cd}$. Mismatch losses can dominate if the antenna is not properly matched to the feed line.

### 2.8 Gain

**Gain** $G(\theta, \phi)$ is the ratio of the radiation intensity in a given direction to the radiation intensity that would be obtained if the power accepted by the antenna were radiated isotropically:

$$
G(\theta, \phi) = \frac{4\pi U(\theta, \phi)}{P_{\text{in}}}
$$

where $P_{\text{in}}$ is the power accepted by the antenna (input power minus reflected power).

**Maximum gain** $G_0$ relates to directivity through efficiency:

$$
G_0 = e_{cd} D_0
$$

In decibels:

$$
G_0(\text{dBi}) = 10 \log_{10}(G_0)
$$

The unit "dBi" indicates gain relative to an isotropic radiator.

**Absolute gain** (sometimes called "realized gain") includes all efficiencies including mismatch:

$$
G_{\text{abs}} = e_0 D_0
$$

### 2.9 Beam Efficiency

**Beam efficiency** $\varepsilon_B$ is the ratio of the power radiated within the main lobe to the total radiated power:

$$
\varepsilon_B = \frac{\int_{\text{main lobe}} U(\theta, \phi) \, d\Omega}{\int_{4\pi} U(\theta, \phi) \, d\Omega}
$$

Beam efficiency is a measure of how well the antenna concentrates power in the desired direction. A high beam efficiency implies low side lobe levels.

### 2.10 Bandwidth

**Bandwidth** is the range of frequencies over which the antenna performance meets a specified standard with respect to some characteristic (impedance, pattern, gain, polarization, etc.).

Common definitions:
- **Impedance bandwidth:** Frequencies where VSWR $\leq$ 2:1 (or equivalently $|\Gamma| \leq 1/3$, return loss $\geq$ 9.54 dB).
- **Pattern bandwidth:** Frequencies where the pattern shape (HPBW, SLL) remains within acceptable limits.
- **Gain bandwidth:** Frequencies where gain remains within a specified variation (e.g., $\pm 1$ dB).

**Bandwidth classification:**
- Narrowband: BW $<$ 10% of center frequency.
- Broadband: BW $\geq$ 10%.
- Frequency-independent: BW $\geq$ 10:1 ratio (decades).

### 2.11 Polarization

**Polarization** of a radiated wave is defined by the locus traced by the tip of the electric field vector as a function of time, viewed along the direction of propagation.

**Types:**
- **Linear polarization:** The electric field oscillates along a fixed line.
  - Vertical, horizontal, or slant ($\pm 45^\circ$).
- **Circular polarization:** The electric field vector rotates at a constant magnitude.
  - Right-hand circular (RHCP) or left-hand circular (LHCP), depending on rotation direction.
- **Elliptical polarization:** The general case, where the field vector traces an ellipse.

**Polarization parameters:**
- **Axial ratio (AR):** Ratio of major axis to minor axis of the polarization ellipse:
  $$
  \text{AR} = \frac{E_{\text{max}}}{E_{\text{min}}}, \quad 1 \leq \text{AR} \leq \infty
  $$
  For linear polarization, $\text{AR} \to \infty$; for circular, $\text{AR} = 1$ (0 dB).
- **Tilt angle:** The orientation angle of the ellipse major axis.
- **Sense:** Determined by the direction of rotation (RHCP or LHCP).

**Polarization loss factor (PLF):**

When a receiving antenna with polarization vector $\hat{\mathbf{p}}_r$ is illuminated by a wave with polarization vector $\hat{\mathbf{p}}_w$:

$$
\text{PLF} = |\hat{\mathbf{p}}_w \cdot \hat{\mathbf{p}}_r|^2
$$

For perfectly matched polarizations, PLF = 1 (0 dB). For orthogonal polarizations (e.g., vertical Tx and horizontal Rx), PLF = 0 ($-\infty$ dB). For circular-to-linear, PLF = 0.5 ($-3$ dB).

### 2.12 Input Impedance

**Input impedance** $Z_{\text{in}}$ is the impedance presented by the antenna at its terminals:

$$
Z_{\text{in}} = R_{\text{in}} + jX_{\text{in}}
$$

where $R_{\text{in}}$ consists of:
- **Radiation resistance** $R_r$: represents power radiated into space.
- **Loss resistance** $R_L$: represents ohmic and dielectric losses.

$$
R_{\text{in}} = R_r + R_L
$$

The **Voltage Standing Wave Ratio (VSWR)** resulting from a mismatch between the antenna impedance $Z_{\text{in}}$ and the transmission line characteristic impedance $Z_0$ is:

$$
\text{VSWR} = \frac{1 + |\Gamma|}{1 - |\Gamma|}, \quad \Gamma = \frac{Z_{\text{in}} - Z_0}{Z_{\text{in}} + Z_0}
$$

### 2.13 Antenna Radiation Efficiency

**Antenna radiation efficiency** $\eta_{\text{rad}}$ (also denoted $e_{cd}$) is the ratio of the power radiated by the antenna to the power accepted by the antenna:

$$
\eta_{\text{rad}} = \frac{P_{\text{rad}}}{P_{\text{in}}} = \frac{R_r}{R_r + R_L}
$$

For a lossless antenna, $\eta_{\text{rad}} = 1$.

### 2.14 Antenna Vector Effective Length and Equivalent Areas

**Vector effective length** $\mathbf{h}_e$ characterizes the receiving properties of an antenna. For an incident plane wave with electric field $\mathbf{E}^i$, the open-circuit voltage at the antenna terminals is:

$$
V_{\text{oc}} = \mathbf{h}_e \cdot \mathbf{E}^i
$$

The vector effective length captures both the magnitude and polarization response of the antenna.

**Equivalent areas:**

- **Effective area** $A_e$ (also $A_{\text{eff}}$): The ratio of power delivered to the load $P_L$ to the incident power density $S$:

  $$
  A_e = \frac{P_L}{S} \quad \text{(m}^2\text{)}
  $$

- **Scattering area** $A_s$: Power re-radiated (scattered) by the receiving antenna.
- **Loss area** $A_L$: Power dissipated as heat in the antenna.
- **Collecting area** $A_c$: Power collected by the antenna (sum of delivered, scattered, and lost).

The effective area relates to directivity:

$$
A_e(\theta, \phi) = \frac{\lambda^2}{4\pi} D(\theta, \phi)
$$

This relationship holds for any lossless antenna ($\eta_{\text{rad}} = 1$). For lossy antennas:

$$
A_e(\theta, \phi) = \frac{\lambda^2}{4\pi} G(\theta, \phi) = \frac{\lambda^2}{4\pi} \eta_{\text{rad}} D(\theta, \phi)
$$

### 2.15 Maximum Directivity and Maximum Effective Area

The maximum effective area $A_{em}$ is related to maximum directivity $D_0$:

$$
A_{em} = \frac{\lambda^2}{4\pi} D_0
$$

This is a fundamental relationship establishing that a more directive antenna (narrower beam) has a larger effective area and therefore captures more power from an incident plane wave.

### 2.16 Friis Transmission Equation

The **Friis transmission equation** relates the power received $P_r$ to the power transmitted $P_t$ in a free-space communication link:

$$
\frac{P_r}{P_t} = G_t G_r \left( \frac{\lambda}{4\pi R} \right)^2
$$

where:
- $G_t$ = gain of the transmitting antenna.
- $G_r$ = gain of the receiving antenna.
- $R$ = distance between antennas.
- $\lambda$ = wavelength.

In decibel form:

$$
P_r(\text{dBm}) = P_t(\text{dBm}) + G_t(\text{dBi}) + G_r(\text{dBi}) - 20\log_{10}\left(\frac{4\pi R}{\lambda}\right)
$$

The term $20\log_{10}(4\pi R/\lambda)$ is the **free-space path loss** (FSPL).

**Radar Range Equation:**

For a monostatic radar (same antenna for transmit and receive):

$$
P_r = \frac{P_t G^2 \lambda^2 \sigma}{(4\pi)^3 R^4}
$$

where $\sigma$ is the radar cross-section (RCS) of the target.

### 2.17 Antenna Temperature

**Antenna temperature** $T_A$ is the temperature of a resistor that would produce the same available noise power per unit bandwidth as the antenna:

$$
T_A = \frac{1}{4\pi} \int_0^{2\pi} \int_0^{\pi} T_b(\theta, \phi) G(\theta, \phi) \sin\theta \, d\theta \, d\phi
$$

where $T_b(\theta, \phi)$ is the brightness temperature distribution of the environment (sky, ground, etc.) weighted by the antenna gain pattern.

The total system noise temperature $T_s$ is:

$$
T_s = T_A + T_{\text{feed}} + T_{\text{receiver}}
$$

where $T_{\text{feed}}$ accounts for ohmic losses in the feed line and $T_{\text{receiver}}$ is the receiver noise temperature.

---

## 3. Key Parameters and Constraints

| Parameter | Symbol | Units | Typical Range | Impact |
| :--- | :--- | :--- | :--- | :--- |
| Directivity | $D_0$ | dimensionless (dBi) | 1.5 dBi (short dipole) to 50+ dBi (large reflector) | Determines spatial power concentration |
| Gain | $G_0$ | dBi | $D_0 - 3$ dB (lossy) to $D_0$ (lossless) | System-level link budget parameter |
| Radiation efficiency | $\eta_{\text{rad}}$ | dimensionless | 20% (electrically small) to 99% (large well-designed) | Ohmic/conductor loss factor |
| HPBW | $\Theta$ | degrees | $1^\circ$ (high gain) to $180^\circ$ (omnidirectional) | Angular coverage |
| Input impedance | $Z_{\text{in}}$ | $\Omega$ | $10-700\;\Omega$ | Determines matching network requirement |
| Bandwidth | BW | MHz or % | $<1\%$ (narrow patch) to $>100\%$ (spiral) | Frequency agility |
| Axial ratio | AR | dB | 0 dB (perfect CP) to $\infty$ (linear) | Polarization quality |
| Effective area | $A_e$ | m$^2$ | $\lambda^2/(4\pi)$ (isotropic) to large | Power capture ability |
| Antenna temperature | $T_A$ | K | 3 K (space-looking) to 300 K (ground-looking) | System noise contribution |
| VSWR | — | dimensionless | 1:1 (perfect match) to $\infty$ (open/short) | Impedance match quality |

---

## 4. Step-by-Step Mechanism: Computing Link Power Budget

### 4.1 Procedure for Link Analysis

To compute the power received in a communication link:

1. **Determine operating frequency** $f$ and compute wavelength $\lambda = c/f$.
2. **Obtain antenna gains** $G_t$ and $G_r$ from datasheet or measurement.
3. **Compute free-space path loss**:
   $$
   \text{FSPL} = \left( \frac{4\pi R}{\lambda} \right)^2
   $$
4. **Apply Friis equation** (assuming polarization-matched, impedance-matched antennas):
   $$
   P_r = P_t G_t G_r \frac{\lambda^2}{(4\pi R)^2}
   $$
5. **Apply polarization mismatch** if needed: multiply by PLF.
6. **Apply impedance mismatch**: multiply by $(1 - |\Gamma_t|^2)(1 - |\Gamma_r|^2)$.
7. **Express in dBm** for practical use.

### 4.2 Procedure for Directivity Computation from Pattern

1. Obtain the normalized power pattern $P_n(\theta, \phi)$.
2. Compute the beam solid angle:
   $$
   \Omega_A = \int_0^{2\pi} \int_0^{\pi} P_n(\theta, \phi) \sin\theta \, d\theta \, d\phi
   $$
3. Compute directivity: $D_0 = 4\pi / \Omega_A$.
4. For approximate directivity (single-lobe pattern): $D_0 \approx 4\pi / (\Theta_{1r} \Theta_{2r})$.

---

## 5. Connections and Cross-References

| Parameter | Related To | Relationship |
| :--- | :--- | :--- |
| Directivity $D_0$ | HPBW $\Theta$ | $D_0 \approx 4\pi/(\Theta_1 \Theta_2)$ for a single main lobe |
| Gain $G_0$ | Directivity $D_0$, Efficiency $\eta_{\text{rad}}$ | $G_0 = \eta_{\text{rad}} D_0$ |
| Effective area $A_e$ | Directivity $D$ | $A_e = \lambda^2 D / (4\pi)$ |
| Effective area $A_e$ | Gain $G$ | $A_e = \lambda^2 G / (4\pi)$ |
| Received power $P_r$ | $G_t, G_r, R, \lambda$ | Friis equation |
| Antenna temperature $T_A$ | Gain pattern $G(\theta,\phi)$, brightness $T_b$ | $T_A = \frac{1}{4\pi}\int T_b G \, d\Omega$ |
| Input impedance $Z_{\text{in}}$ | VSWR, reflected power | $\Gamma = (Z_{\text{in}} - Z_0)/(Z_{\text{in}} + Z_0)$ |
| Bandwidth | $Q$, impedance, pattern | Higher $Q$ implies narrower BW |

*Prerequisite: Section 1 (Antennas — Fundamentals).* The current distribution and radiation mechanism concepts from Section 1 are needed to understand how pattern shape determines directivity and beamwidth.

---

## Solved Exercises

### Exercise 1: Directivity from HPBW (Kraus Approximation)

**Problem:** An antenna has an HPBW of $30^\circ$ in the E-plane and $40^\circ$ in the H-plane. Estimate the directivity using Kraus' approximate formula.

**Solution:**

Step 1: State Kraus' formula.

$$
D_0 \approx \frac{41,253}{\Theta_{1d} \Theta_{2d}}
$$

where $\Theta_{1d}$ and $\Theta_{2d}$ are the HPBW in degrees.

Step 2: Substitute the given beamwidths.

$$
D_0 \approx \frac{41,253}{30^\circ \times 40^\circ} = \frac{41,253}{1200}
$$

Step 3: Compute.

$$
D_0 \approx 34.38 \quad \text{(dimensionless, ratio)}
$$

Step 4: Convert to dBi.

$$
D_0(\text{dBi}) = 10 \log_{10}(34.38) = 10 \times 1.536 = 15.36 \text{ dBi}
$$

The estimated directivity is approximately 15.4 dBi.

**Note:** Kraus' formula is an approximation valid for patterns with a single narrow main lobe and low side lobes. For patterns with significant side lobes, the directivity will be lower than the Kraus estimate because power is spread into the side lobes.

---

### Exercise 2: Gain and Efficiency from Measured Data

**Problem:** A transmitting antenna accepts 100 W from the feed line. The measured radiation intensity in the direction of maximum radiation is $U_{\text{max}} = 350$ W/sr. The total radiated power is measured as 85 W. Compute: (a) the radiation efficiency, (b) the directivity, (c) the gain.

**Solution:**

Step 1: Given data.
- $P_{\text{in}} = 100$ W (power accepted).
- $P_{\text{rad}} = 85$ W (power radiated).
- $U_{\text{max}} = 350$ W/sr.

Step 2: Compute radiation efficiency $\eta_{\text{rad}}$.

$$
\eta_{\text{rad}} = \frac{P_{\text{rad}}}{P_{\text{in}}} = \frac{85}{100} = 0.85
$$

The radiation efficiency is 85%.

Step 3: Compute directivity $D_0$.

$$
D_0 = \frac{4\pi U_{\text{max}}}{P_{\text{rad}}} = \frac{4\pi \times 350}{85}
$$

$$
D_0 = \frac{4398.23}{85} = 51.74
$$

In dBi: $10 \log_{10}(51.74) = 17.14$ dBi.

Step 4: Compute gain $G_0$.

$$
G_0 = \eta_{\text{rad}} D_0 = 0.85 \times 51.74 = 43.98
$$

In dBi: $10 \log_{10}(43.98) = 16.43$ dBi.

**Verification:** $G_0(\text{dBi}) = D_0(\text{dBi}) + 10\log_{10}(\eta) = 17.14 + 10\log_{10}(0.85) = 17.14 - 0.71 = 16.43$ dBi. Consistent.

---

### Exercise 3: Effective Area and Received Power

**Problem:** A geostationary satellite at $R = 36,000$ km transmits at $f = 12$ GHz with power $P_t = 20$ W and antenna gain $G_t = 30$ dBi. A ground station antenna has gain $G_r = 45$ dBi. Assume polarization-matched, lossless antennas. Compute: (a) the effective area of the receiving antenna, (b) the received power.

**Solution:**

Step 1: Compute wavelength.

$$
\lambda = \frac{c}{f} = \frac{3 \times 10^8}{12 \times 10^9} = 0.025 \text{ m} = 2.5 \text{ cm}
$$

Step 2: Compute effective area of receiving antenna.

First, convert $G_r$ from dBi to linear: $G_r = 10^{45/10} = 10^{4.5} = 31,623$.

$$
A_{er} = \frac{\lambda^2}{4\pi} G_r = \frac{(0.025)^2}{4\pi} \times 31,623
$$

$$
A_{er} = \frac{0.000625}{12.566} \times 31,623 = 4.972 \times 10^{-5} \times 31,623
$$

$$
A_{er} = 1.573 \text{ m}^2
$$

The effective area of the receiving antenna is approximately 1.57 m$^2$.

Step 3: Convert $G_t$ from dBi to linear: $G_t = 10^{30/10} = 1000$.

Step 4: Compute received power using Friis equation.

$$
P_r = P_t G_t G_r \left( \frac{\lambda}{4\pi R} \right)^2
$$

$$
P_r = 20 \times 1000 \times 31,623 \times \left( \frac{0.025}{4\pi \times 3.6 \times 10^7} \right)^2
$$

Step 5: Compute the path loss term.

$$
\frac{\lambda}{4\pi R} = \frac{0.025}{4\pi \times 3.6 \times 10^7} = \frac{0.025}{4.524 \times 10^8}
$$

$$
\frac{\lambda}{4\pi R} = 5.527 \times 10^{-11}
$$

Square: $(5.527 \times 10^{-11})^2 = 3.055 \times 10^{-21}$.

Step 6: Multiply all terms.

$$
P_r = 20 \times 1000 \times 31,623 \times 3.055 \times 10^{-21}
$$

$$
P_r = 20 \times 1000 = 20,000
$$

$$
P_r = 20,000 \times 31,623 = 6.325 \times 10^8
$$

$$
P_r = 6.325 \times 10^8 \times 3.055 \times 10^{-21} = 1.932 \times 10^{-12} \text{ W}
$$

Step 7: Express in dBm.

$$
P_r(\text{dBm}) = 10 \log_{10}(1.932 \times 10^{-12}) + 30 = -117.14 + 30 = -87.14 \text{ dBm}
$$

The received power is approximately $1.93 \times 10^{-12}$ W ($-87.1$ dBm).

---

### Exercise 4: Polarization Mismatch Loss

**Problem:** A vertically polarized transmitting antenna radiates toward a receiving antenna that is linearly polarized at $45^\circ$ relative to vertical. Compute the polarization loss factor in dB.

**Solution:**

Step 1: Define the polarization vectors.

Transmitting antenna: $\hat{\mathbf{p}}_t = \hat{\mathbf{v}}$ (vertical).

Receiving antenna: $\hat{\mathbf{p}}_r = \frac{1}{\sqrt{2}}(\hat{\mathbf{v}} + \hat{\mathbf{h}})$ ($45^\circ$ slant).

Step 2: Compute the PLF.

$$
\text{PLF} = |\hat{\mathbf{p}}_t \cdot \hat{\mathbf{p}}_r|^2
$$

$$
\hat{\mathbf{p}}_t \cdot \hat{\mathbf{p}}_r = \hat{\mathbf{v}} \cdot \frac{1}{\sqrt{2}}(\hat{\mathbf{v}} + \hat{\mathbf{h}}) = \frac{1}{\sqrt{2}}(1 + 0) = \frac{1}{\sqrt{2}}
$$

$$
\text{PLF} = \left|\frac{1}{\sqrt{2}}\right|^2 = \frac{1}{2} = 0.5
$$

Step 3: Express in dB.

$$
\text{PLF}_{\text{dB}} = 10 \log_{10}(0.5) = -3.01 \text{ dB}
$$

The polarization mismatch loss is approximately 3 dB. This means half the available power is lost due to polarization mismatch.

**Extension:** If the receiving antenna were horizontally polarized ($\hat{\mathbf{p}}_r = \hat{\mathbf{h}}$), PLF = 0 ($-\infty$ dB) — no power would be received.

---

### Exercise 5: Input Impedance and VSWR Calculation

**Problem:** A dipole antenna has an input impedance $Z_{\text{in}} = 73 + j42.5\;\Omega$ at its design frequency. The feed line has a characteristic impedance $Z_0 = 50\;\Omega$. Compute: (a) the reflection coefficient, (b) the VSWR, (c) the reflection (mismatch) efficiency, (d) the percentage of power reflected.

**Solution:**

Step 1: Compute the reflection coefficient $\Gamma$.

$$
\Gamma = \frac{Z_{\text{in}} - Z_0}{Z_{\text{in}} + Z_0} = \frac{(73 + j42.5) - 50}{(73 + j42.5) + 50}
$$

$$
\Gamma = \frac{23 + j42.5}{123 + j42.5}
$$

Step 2: Compute magnitude.

Numerator magnitude: $|23 + j42.5| = \sqrt{23^2 + 42.5^2} = \sqrt{529 + 1806.25} = \sqrt{2335.25} = 48.32$

Denominator magnitude: $|123 + j42.5| = \sqrt{123^2 + 42.5^2} = \sqrt{15,129 + 1806.25} = \sqrt{16,935.25} = 130.14$

$$
|\Gamma| = \frac{48.32}{130.14} = 0.371
$$

Step 3: Compute VSWR.

$$
\text{VSWR} = \frac{1 + |\Gamma|}{1 - |\Gamma|} = \frac{1 + 0.371}{1 - 0.371} = \frac{1.371}{0.629} = 2.18
$$

The VSWR is 2.18:1.

Step 4: Compute the reflection (mismatch) efficiency $e_r$.

$$
e_r = 1 - |\Gamma|^2 = 1 - (0.371)^2 = 1 - 0.138 = 0.862
$$

Step 5: Compute the percentage of power reflected.

$$
\text{Reflected power} = |\Gamma|^2 \times 100\% = 0.138 \times 100\% = 13.8\%
$$

Approximately 13.8% of the incident power is reflected due to impedance mismatch. The remaining 86.2% is accepted by the antenna.

---

### Exercise 6: Beam Efficiency Computation

**Problem:** An antenna has a rotationally symmetric power pattern approximated by:
- Main lobe: $P_n(\theta) = \cos^2(\theta)$ for $0 \leq \theta \leq \pi/3$, and $P_n(\theta) = 0$ for $\theta > \pi/3$.
- Side lobes are negligible.
- The pattern is uniform in $\phi$.

Compute the beam efficiency.

**Solution:**

Step 1: Define the beam efficiency.

$$
\varepsilon_B = \frac{\int_{\text{main lobe}} U(\theta, \phi) \, d\Omega}{\int_{4\pi} U(\theta, \phi) \, d\Omega}
$$

Since the pattern is defined as the power pattern, $U(\theta, \phi) = U_{\text{max}} P_n(\theta)$.

Step 2: Compute the numerator (power in main lobe, which is the entire pattern for $\theta \leq \pi/3$).

$$
P_{\text{main}} = \int_0^{2\pi} \int_0^{\pi/3} U_{\text{max}} \cos^2(\theta) \sin\theta \, d\theta \, d\phi
$$

Separate integrals:

$$
P_{\text{main}} = U_{\text{max}} \int_0^{2\pi} d\phi \int_0^{\pi/3} \cos^2(\theta) \sin\theta \, d\theta
$$

$$
P_{\text{main}} = U_{\text{max}} \times 2\pi \times \int_0^{\pi/3} \cos^2(\theta) \sin\theta \, d\theta
$$

Step 3: Evaluate the $\theta$ integral. Let $u = \cos\theta$, $du = -\sin\theta \, d\theta$.

When $\theta = 0$, $u = 1$. When $\theta = \pi/3$, $u = 0.5$.

$$
\int_0^{\pi/3} \cos^2(\theta) \sin\theta \, d\theta = \int_1^{0.5} u^2 (-du) = \int_{0.5}^1 u^2 \, du
$$

$$
= \left[ \frac{u^3}{3} \right]_{0.5}^1 = \frac{1}{3} \left(1^3 - 0.5^3\right) = \frac{1}{3}\left(1 - 0.125\right) = \frac{0.875}{3} = 0.2917
$$

Step 4: Compute $P_{\text{main}}$.

$$
P_{\text{main}} = U_{\text{max}} \times 2\pi \times 0.2917 = 0.5834\pi U_{\text{max}}
$$

Step 5: Compute the denominator (total radiated power, over all $4\pi$ sr). Since $P_n(\theta) = 0$ for $\theta > \pi/3$, the total power equals the main lobe power.

Therefore, the beam efficiency is:

$$
\varepsilon_B = \frac{P_{\text{main}}}{P_{\text{total}}} = \frac{0.5834\pi U_{\text{max}}}{0.5834\pi U_{\text{max}}} = 1.0
$$

**Interpretation:** The beam efficiency is 100% because there are no side lobes — all radiated power is within the defined main lobe. In practical antennas with finite side lobes, $\varepsilon_B < 1$.

---

### Exercise 7: Antenna Temperature and System Noise

**Problem:** A receiving antenna with a uniform gain pattern over a $10^\circ$ cone half-angle points at the sky (brightness temperature $T_{\text{sky}} = 10$ K). Outside this cone, the pattern is zero. The ambient temperature is 290 K. The antenna has ohmic loss of 0.5 dB ($L_{\text{feed}} = 1.122$). Compute: (a) the antenna temperature $T_A$, (b) the system noise temperature if the receiver $T_{\text{rec}} = 50$ K.

**Solution:**

Step 1: The antenna temperature is the weighted average of brightness temperature over the gain pattern.

Since the gain is uniform within the cone and zero outside, the solid angle of the cone is:

$$
\Omega_{\text{cone}} = 2\pi(1 - \cos\theta_0) = 2\pi(1 - \cos 10^\circ)
$$

$$
\Omega_{\text{cone}} = 2\pi(1 - 0.9848) = 2\pi \times 0.0152 = 0.0955 \text{ sr}
$$

Step 2: The gain within the cone must satisfy the normalization:

$$
\int_{4\pi} G(\theta, \phi) \, d\Omega = 4\pi
$$

Since gain is uniform ($G_0$) over $\Omega_{\text{cone}}$ and zero elsewhere:

$$
G_0 \Omega_{\text{cone}} = 4\pi \quad \Rightarrow \quad G_0 = \frac{4\pi}{0.0955} = 131.6
$$

Step 3: Compute antenna temperature. The brightness temperature is $T_{\text{sky}} = 10$ K within the cone.

$$
T_A = \frac{1}{4\pi} \int_{4\pi} T_b(\theta, \phi) G(\theta, \phi) \, d\Omega
$$

Within the cone: $T_b = 10$ K, $G = 131.6$. Outside: pattern is zero.

$$
T_A = \frac{1}{4\pi} \times 10 \times 131.6 \times 0.0955
$$

$$
T_A = \frac{1}{4\pi} \times 125.7 = \frac{125.7}{12.566} = 10.0 \text{ K}
$$

Step 4: Account for ohmic losses. The feed loss reduces the effective antenna temperature at the receiver input:

$$
T'_A = \frac{T_A}{L_{\text{feed}}} + \left(1 - \frac{1}{L_{\text{feed}}}\right) T_{\text{amb}}
$$

where $L_{\text{feed}} = 10^{0.5/10} = 1.122$.

$$
T'_A = \frac{10.0}{1.122} + \left(1 - \frac{1}{1.122}\right) \times 290
$$

$$
T'_A = 8.91 + (1 - 0.891) \times 290 = 8.91 + 0.109 \times 290 = 8.91 + 31.58 = 40.49 \text{ K}
$$

Step 5: Compute system noise temperature.

$$
T_s = T'_A + T_{\text{rec}} = 40.49 + 50 = 90.49 \text{ K}
$$

The system noise temperature is approximately 90.5 K.

> **[Supplementary]** Antenna temperature is a critical parameter in low-noise receiving systems such as satellite ground stations and radio telescopes. A ground-looking antenna sees $T_b \approx 290$ K, while a sky-looking antenna can see $T_b$ as low as 3 K (cosmic microwave background). This is why satellite ground stations point antennas at the sky rather than toward the warm ground.

---

### Exercise 8: Friis Equation with All Loss Factors

**Problem:** A 5.8 GHz link has the following parameters:
- Transmit power: $P_t = 10$ dBm.
- Transmit antenna gain: $G_t = 12$ dBi, with VSWR$_t = 1.5:1$.
- Receive antenna gain: $G_r = 18$ dBi, with VSWR$_r = 2.0:1$.
- Distance: $R = 500$ m.
- Polarization: transmit is RHCP, receive is linear vertical (PLF = 0.5).

Compute the received power in dBm.

**Solution:**

Step 1: Compute wavelength.

$$
\lambda = \frac{3 \times 10^8}{5.8 \times 10^9} = 0.0517 \text{ m}
$$

Step 2: Compute free-space path loss.

$$
\text{FSPL} = \left( \frac{4\pi R}{\lambda} \right)^2 = \left( \frac{4\pi \times 500}{0.0517} \right)^2
$$

$$
\text{FSPL} = \left( \frac{6283.2}{0.0517} \right)^2 = (1.215 \times 10^5)^2 = 1.476 \times 10^{10}
$$

$$
\text{FSPL}_{\text{dB}} = 10 \log_{10}(1.476 \times 10^{10}) = 101.69 \text{ dB}
$$

Step 3: Compute mismatch efficiencies.

For $VSWR_t = 1.5$:

$$
|\Gamma_t| = \frac{\text{VSWR} - 1}{\text{VSWR} + 1} = \frac{1.5 - 1}{1.5 + 1} = \frac{0.5}{2.5} = 0.2
$$

$$
e_{rt} = 1 - |\Gamma_t|^2 = 1 - 0.04 = 0.96
$$

For VSWR$_r = 2.0$:

$$
|\Gamma_r| = \frac{2 - 1}{2 + 1} = \frac{1}{3} = 0.333
$$

$$
e_{rr} = 1 - |\Gamma_r|^2 = 1 - 0.111 = 0.889
$$

Step 4: Express all gains and losses in dB.

$P_t = 10$ dBm, $G_t = 12$ dBi, $G_r = 18$ dBi, FSPL = 101.69 dB.

Mismatch losses: $L_{mt} = -10 \log_{10}(0.96) = -0.177$ dB, $L_{mr} = -10 \log_{10}(0.889) = -0.511$ dB.

Polarization loss: $L_{\text{pol}} = -10 \log_{10}(0.5) = 3.01$ dB.

Step 5: Compute $P_r$ in dBm.

$$
P_r(\text{dBm}) = P_t + G_t + G_r - \text{FSPL}_{\text{dB}} + L_{mt} + L_{mr} - L_{\text{pol}}
$$

Note: Mismatch losses are subtracted (negative dB values).

$$
P_r = 10 + 12 + 18 - 101.69 - 0.177 - 0.511 - 3.01
$$

$$
P_r = 40 - 105.388 = -65.388 \text{ dBm}
$$

The received power is approximately $-65.4$ dBm.

---

### Exercise 9: Directivity from Numerical Integration

**Problem:** A measured power pattern has the following samples at $\theta = 0^\circ, 30^\circ, 60^\circ, 90^\circ$ (rotation is symmetric, no $\phi$ variation):

| $\theta$ (degrees) | $P_n(\theta)$ |
| :--- | :--- |
| 0 | 1.0 |
| 30 | 0.8 |
| 60 | 0.3 |
| 90 | 0.1 |

The pattern is zero for $\theta > 90^\circ$. Estimate the directivity using numerical integration with the trapezoidal rule.

**Solution:**

Step 1: Convert angles to radians.

$\theta_1 = 0$, $\theta_2 = \pi/6$, $\theta_3 = \pi/3$, $\theta_4 = \pi/2$.

Step 2: The directivity formula requires integration:

$$
D_0 = \frac{4\pi}{\displaystyle \int_0^{2\pi} \int_0^{\pi/2} P_n(\theta) \sin\theta \, d\theta \, d\phi}
$$

Because of $\phi$ symmetry:

$$
D_0 = \frac{4\pi}{2\pi \displaystyle \int_0^{\pi/2} P_n(\theta) \sin\theta \, d\theta} = \frac{2}{\displaystyle \int_0^{\pi/2} P_n(\theta) \sin\theta \, d\theta}
$$

Step 3: Compute the integrand $f(\theta) = P_n(\theta) \sin\theta$ at each sample point.

| $\theta$ (rad) | $P_n$ | $\sin\theta$ | $f(\theta)$ |
| :--- | :--- | :--- | :--- |
| 0 | 1.0 | 0 | 0 |
| $\pi/6$ | 0.8 | 0.5 | 0.4 |
| $\pi/3$ | 0.3 | 0.866 | 0.260 |
| $\pi/2$ | 0.1 | 1.0 | 0.1 |

Step 4: Apply the trapezoidal rule.

$\Delta\theta_1 = \pi/6$, $\Delta\theta_2 = \pi/6$, $\Delta\theta_3 = \pi/6$.

$$
\int_0^{\pi/2} f(\theta) \, d\theta \approx \frac{\pi/6}{2}[f(0) + 2f(\pi/6) + 2f(\pi/3) + f(\pi/2)]
$$

$$
= \frac{\pi}{12}[0 + 2(0.4) + 2(0.260) + 0.1]
$$

$$
= \frac{\pi}{12}[0 + 0.8 + 0.52 + 0.1] = \frac{\pi}{12} \times 1.42
$$

$$
= 0.3718
$$

Step 5: Compute directivity.

$$
D_0 = \frac{2}{0.3718} = 5.38
$$

In dBi: $10 \log_{10}(5.38) = 7.31$ dBi.

The estimated directivity is approximately 5.4 (7.3 dBi).

**Note:** The accuracy of this numerical estimate depends on the sampling density. With only 4 sample points, the true directivity may differ. For practical antenna measurements, pattern sampling at $1^\circ$ to $5^\circ$ intervals is typical.

---

### Exercise 10: Radar Range Equation

**Problem:** A monostatic radar operating at $f = 10$ GHz has the following parameters:
- Transmit power: $P_t = 1$ kW.
- Antenna gain: $G = 35$ dBi.
- Target RCS: $\sigma = 1$ m$^2$.
- Minimum detectable signal: $P_{r,\min} = -90$ dBm.

Compute the maximum detection range.

**Solution:**

Step 1: Express all quantities in linear units.

$P_t = 1000$ W.

$G = 10^{35/10} = 10^{3.5} = 3162.3$.

$\lambda = \frac{3 \times 10^8}{10 \times 10^9} = 0.03$ m.

$P_{r,\min} = -90$ dBm $= 10^{-90/10} \times 10^{-3} = 10^{-12}$ W.

Step 2: State the radar range equation solved for $R$.

$$
P_r = \frac{P_t G^2 \lambda^2 \sigma}{(4\pi)^3 R^4} \quad \Rightarrow \quad R_{\max} = \left( \frac{P_t G^2 \lambda^2 \sigma}{(4\pi)^3 P_{r,\min}} \right)^{1/4}
$$

Step 3: Compute numerator.

$$
P_t G^2 \lambda^2 \sigma = 1000 \times (3162.3)^2 \times (0.03)^2 \times 1
$$

$$
= 1000 \times 10,000,000 \times 0.0009 \times 1
$$

$$
= 9 \times 10^9
$$

Step 4: Compute denominator.

$(4\pi)^3 = (12.566)^3 = 1984.4$.

$$
P_{r,\min} (4\pi)^3 = 10^{-12} \times 1984.4 = 1.984 \times 10^{-9}
$$

Step 5: Compute range.

$$
R_{\max} = \left( \frac{9 \times 10^9}{1.984 \times 10^{-9}} \right)^{1/4} = \left( 4.536 \times 10^{18} \right)^{1/4}
$$

$$
R_{\max} = (4.536)^{1/4} \times (10^{18})^{1/4} = 1.459 \times 10^{4.5}
$$

$$
R_{\max} = 1.459 \times 31,623 = 46,137 \text{ m}
$$

The maximum detection range is approximately 46.1 km.

---

## Exam Tip: Parameter Relationships and Common Pitfalls

A frequent exam pattern asks you to compute one parameter from others using the fundamental relationships. Memorize these key equations:

1. **Gain-Directivity-Efficiency:** $G(\text{dBi}) = D(\text{dBi}) + 10\log_{10}(\eta_{\text{rad}})$. Gain is always less than or equal to directivity.

2. **Effective Area-Directivity:** $A_e = \frac{\lambda^2}{4\pi} D_0$. A larger effective area means higher directivity.

3. **Friis equation:** Do not forget the $\lambda^2/(4\pi R)^2$ term. A common mistake is to use the path loss in dB but forget to convert gains to linear units when multiplying.

4. **VSWR to mismatch loss:** $|\Gamma| = (\text{VSWR} - 1)/(\text{VSWR} + 1)$, then mismatch loss $= -10\log_{10}(1 - |\Gamma|^2)$ dB.

**Common pitfalls:**
- Confusing dBi (gain relative to isotropic) with dBd (gain relative to a dipole). $G(\text{dBi}) = G(\text{dBd}) + 2.15$ dB.
- Using HPBW in degrees directly in formulas requiring radians. Kraus formula uses degrees; the exact $4\pi/(\Theta_1 \Theta_2)$ formula uses radians.
- Forgetting that the Friis equation assumes polarization match. Always check if a PLF adjustment is needed.
- Confusing effective area with physical area. For aperture antennas, $A_e = \eta_{\text{ap}} A_p$, where $\eta_{\text{ap}}$ is aperture efficiency (typically 50-80%).

**Pattern recognition shortcut:** If an exam problem gives you HPBW in two planes, you can always provide an approximate directivity using Kraus' formula. It is not exact but is a valid engineering estimate and shows understanding of the concept.