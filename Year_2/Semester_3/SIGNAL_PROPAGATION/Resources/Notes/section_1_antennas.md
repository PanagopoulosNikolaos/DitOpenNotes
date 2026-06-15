# Antennas — Fundamentals

An antenna is a transducer that converts guided electromagnetic waves (transmission line or waveguide modes) into free-space propagating waves (radiation), and vice versa. Antennas form the interface between a transmitter or receiver and the propagation medium, making them the critical component in any wireless communication system. This section covers the fundamental concepts of antenna operation, classification, the physical mechanism of radiation, current distribution on wire antennas, and the historical development of the field.

---

## 1. Conceptual Foundation

### 1.1 What an Antenna Does

An antenna serves two reciprocal roles:

- **Transmission:** Converts the time-varying electrical signal (voltage/current) from a transmission line into an electromagnetic wave launched into free space.
- **Reception:** Intercepts a portion of the power in an incident electromagnetic wave and converts it back into a guided electrical signal.

The antenna is thus the transition region between two distinct electromagnetic environments: a bounded, guided-wave structure and unbounded free-space propagation. This transition involves impedance matching, radiation pattern shaping, and polarization control.

### 1.2 Why Antennas Are Necessary

Without an antenna, the signal from a transmitter cannot couple efficiently to free space. A transmission line or waveguide confines the fields to its vicinity; an antenna deliberately opens the field structure to allow energy to escape (or enter). The antenna geometry determines:

- The spatial distribution of radiated power (radiation pattern).
- The efficiency of the conversion.
- The frequency range over which the conversion is effective.
- The polarization of the radiated wave.

---

## 2. Formal Definitions and Models

### 2.1 Antenna as a Boundary-Value Problem

From an electromagnetic perspective, an antenna is a structure whose surface supports electric and magnetic currents ($\mathbf{J}_s$ and $\mathbf{M}_s$) that radiate into the surrounding space. The radiated fields are obtained from the vector potentials:

$$
\mathbf{A} = \frac{\mu}{4\pi} \iiint_V \mathbf{J} \frac{e^{-jkr}}{r} \, dV'
$$

$$
\mathbf{F} = \frac{\epsilon}{4\pi} \iiint_V \mathbf{M} \frac{e^{-jkr}}{r} \, dV'
$$

where $\mathbf{J}$ and $\mathbf{M}$ are the electric and magnetic current densities on the antenna structure, $k = 2\pi / \lambda$ is the wavenumber, $r$ is the distance from the source point to the observation point, and $\mu$ and $\epsilon$ are the permeability and permittivity of the medium.

### 2.2 Fundamental Operating Principle

An antenna radiates because of a time-varying current or acceleration of charge. The fundamental relation for radiation from a current element (Hertzian dipole) of length $dl$ carrying current $I_0 \cos(\omega t)$ is:

$$
\mathbf{E}_\theta = j \frac{\eta k I_0 dl \sin\theta}{4\pi r} e^{-jkr}
$$

$$
\mathbf{H}_\phi = j \frac{k I_0 dl \sin\theta}{4\pi r} e^{-jkr}
$$

where $\eta = \sqrt{\mu/\epsilon}$ is the intrinsic impedance of the medium (approximately $120\pi \;\Omega$ for free space).

> **[Key Insight]** The radiation field is proportional to $I_0 dl / \lambda$. A structure that is electrically small ($dl \ll \lambda$) requires a very large current to radiate significant power. This is why practical antennas typically have dimensions comparable to the wavelength.

### 2.3 Reciprocity

A fundamental property of antennas is **reciprocity**: the transmitting and receiving characteristics of an antenna are identical (same radiation pattern, same impedance, same polarization behavior). This means an antenna can be fully characterized in either mode, and the characterization applies to both.

---

## 3. Key Parameters and Constraints

| Parameter | Symbol | Typical Values / Range | Impact of Variation |
| :--- | :--- | :--- | :--- |
| Wavelength | $\lambda$ | Depends on frequency ($\lambda = c/f$) | Determines physical size of resonant antennas |
| Electrical length | $L/\lambda$ | 0.01 (electrically small) to $>10$ (electrically large) | Affects radiation resistance, bandwidth, pattern |
| Operating frequency | $f$ | 3 kHz–300 GHz (radio spectrum) | Determines wavelength, propagation characteristics |
| Antenna impedance | $Z_A$ | 10–700 $\Omega$ typical | Mismatch causes reflections and power loss |
| Polarization | — | Linear, circular, elliptical | Must match between Tx and Rx for maximum power transfer |
| Bandwidth | BW | Narrowband: $<10\%$; Broadband: $>10\%$ | Wider BW enables higher data rates but may constrain design |
| Radiation resistance | $R_r$ | Fractional $\Omega$ to hundreds of $\Omega$ | Higher $R_r$ means more efficient radiation for a given current |

---

## 4. Types of Antennas

Antennas are classified by geometry, operating principle, and frequency range. The major categories follow.

### 4.1 Wire Antennas

- **Dipole antennas:** Straight conductors fed at the center. The half-wavelength dipole ($L = \lambda/2$) is the most widely used reference antenna.
- **Monopole antennas:** Half of a dipole mounted above a ground plane. The quarter-wavelength monopole ($L = \lambda/4$) is common in mobile communications.
- **Loop antennas:** Closed conducting loops. Small loops ($C \ll \lambda$) are used for reception and direction finding; large loops ($C \approx \lambda$) are used as radiating elements.
- **Helical antennas:** Wire wound in a helix, producing circular polarization. Used for satellite communications.

### 4.2 Aperture Antennas

- **Horn antennas:** Flared waveguide terminations that produce directional radiation. Used as feeds for reflector antennas and as stand-alone radiators at microwave frequencies.
- **Slot antennas:** Cutouts in a conducting surface, often used in waveguide arrays.
- **Reflector antennas:** Parabolic, spherical, or corner reflectors that collimate radiation from a feed element.

### 4.3 Printed and Planar Antennas

- **Microstrip patch antennas:** Metallic patches on a dielectric substrate, fed by a microstrip line. Low profile, lightweight, and easily integrated into printed circuits. Common in personal communication devices and arrays.
- **Printed dipoles and slots:** Wire or aperture equivalents realized in printed circuit board technology.

### 4.4 Array Antennas

- **Linear arrays:** Elements arranged along a line. Beam steering is achieved by phase shifting.
- **Planar arrays:** Elements arranged in a two-dimensional grid, providing beam steering in both azimuth and elevation.
- **Phased arrays:** Arrays with electronically controlled phase shifters for rapid beam scanning without mechanical movement.

### 4.5 Broadband and Frequency-Independent Antennas

- **Log-periodic antennas:** Structure repeats logarithmically, producing nearly constant impedance and pattern over a wide frequency range (e.g., 10:1 bandwidth).
- **Spiral antennas:** Self-complementary equiangular spirals that are frequency-independent over multi-octave ranges.

---

## 5. Radiation Mechanism

### 5.1 Physical Picture

Radiation from an antenna is a consequence of **accelerating charges**. A charge moving at constant velocity produces a static field pattern that moves with it. When the charge accelerates (or decelerates), the field lines cannot adjust instantaneously (because the speed of light is finite), and a kink propagates outward — this kink is the radiated wave.

For a time-harmonic current distribution, the key requirement for radiation is that the current must be **time-varying** and the structure must allow the field to detach. For a two-wire transmission line carrying equal and opposite currents, the fields cancel at large distances. If the wires are bent apart (forming a dipole), the cancellation is incomplete, and the net field propagates.

### 5.2 Conditions for Radiation

For a current element to radiate, two conditions are necessary:

1. **Time variation of the source:** $\partial \mathbf{J} / \partial t \neq 0$. A static current does not radiate.
2. **Geometric asymmetry:** The current distribution must produce a non-zero net radiation vector. In a transmission line, equal and opposite currents produce cancelling fields; separating the conductors breaks this cancellation.

### 5.3 The Three Field Regions Around an Antenna

The space around an antenna is divided into three regions based on the dominant field behavior:

1. **Reactive near-field ($r < 0.62 \sqrt{D^3/\lambda}$):** Electric and magnetic fields are predominantly reactive (standing wave). The field structure is highly dependent on the detailed current distribution.
2. **Radiating near-field (Fresnel) region ($0.62 \sqrt{D^3/\lambda} < r < 2D^2/\lambda$):** The radiation pattern is a function of distance; the angular field distribution depends on $r$.
3. **Far-field (Fraunhofer) region ($r > 2D^2/\lambda$):** The radiation pattern is independent of distance. The fields are transverse electromagnetic (TEM) and decay as $1/r$.

where $D$ is the largest dimension of the antenna.

---

## 6. Current Distribution on a Thin Wire Antenna

### 6.1 Assumptions

For an electrically thin wire (radius $a \ll \lambda$), the current distribution is approximated as a standing wave on the wire. The dominant effect is that the current must vanish at the open ends of the dipole.

### 6.2 Standing-Wave Current on a Center-Fed Dipole

For a center-fed dipole of total length $L$, the current distribution is approximately sinusoidal:

$$
I(z) = I_m \sin\left[ k\left( \frac{L}{2} - |z| \right) \right], \quad -\frac{L}{2} \leq z \leq \frac{L}{2}
$$

where $I_m$ is the maximum current amplitude and $k = 2\pi/\lambda$ is the wavenumber. For specific lengths:

- **Half-wavelength dipole ($L = \lambda/2$):**
  $$
  I(z) = I_m \cos\left( \frac{\pi z}{L} \right), \quad -\frac{L}{4} \leq z \leq \frac{L}{4}
  $$

- **Full-wavelength dipole ($L = \lambda$):**
  $$
  I(z) = I_m \sin\left( k|z| \right), \quad -\frac{\lambda}{2} \leq z \leq \frac{\lambda}{2}
  $$

The sinusoidal approximation assumes the wire is infinitely thin and lossless. For finite-radius wires, the current distribution is slightly modified due to the finite thickness and internal impedance.

### 6.3 Current Distribution and Radiation

The current distribution directly determines the radiated fields. Each infinitesimal segment $dz$ of the wire behaves as a Hertzian dipole with current $I(z)$. The total radiated field is the superposition (integral) of contributions from all segments:

$$
\mathbf{E}(\theta, \phi) = \int_{-L/2}^{L/2} d\mathbf{E}(z, \theta, \phi)
$$

The radiation pattern is the Fourier transform of the current distribution along the wire. This relationship is fundamental to antenna synthesis: the desired radiation pattern dictates the required current distribution.

---

## 7. Historical Advancement

The development of antenna theory and practice spans more than a century, driven by the evolution of wireless communication technologies.

| Era | Key Contributors / Milestones | Contribution |
| :--- | :--- | :--- |
| 1887–1890 | Heinrich Hertz | First experimental demonstration of radio wave transmission and reception using a spark-gap transmitter, dipole, and loop antennas. Verified Maxwell's equations experimentally. |
| 1895–1901 | Guglielmo Marconi | First transatlantic wireless transmission (1901). Used long-wire antennas and ground systems. Pioneered practical wireless telegraphy. |
| 1910–1930s | Alexanderson, Beverage, Franklin | Development of directional antennas (Beverage antenna), standing-wave ratio concepts, and array theory. |
| 1930s–1940s | Carter, Chu, Schelkunoff | Formal antenna impedance theory, equivalence principle, and the Chu-Harrington limit (fundamental limit on electrically small antenna Q). Development of horn and reflector antennas for radar (WWII). |
| 1940s–1950s | Kraus, Hansen, Woodward | Helical antenna, frequency-independent antenna concept, and the Woodward-Lawson synthesis method. |
| 1960s–1970s | Harrington, Mautz, Mittra | Moment method (computational electromagnetics), numerical analysis of antenna problems, microstrip antenna development. |
| 1980s–present | Various | Phased array radar, smart antennas (adaptive beamforming), fractal antennas, metamaterial-based antennas, MIMO antenna systems for 5G/6G. |

> **[Key Insight]** The fundamental theoretical framework of antennas — Maxwell's equations, the vector potential, and reciprocity — was essentially complete by the 1940s. Subsequent progress has been driven by computational techniques (enabling the analysis of structures too complex for closed-form solutions), new materials, and the demand for higher frequencies, wider bandwidths, and smaller form factors.

---

## Solved Exercises

### Exercise 1: Wavelength Calculation for a Resonant Dipole

**Problem:** A half-wavelength dipole antenna is designed to operate at $f = 150$ MHz. Determine the physical length of the dipole. Assume free-space propagation ($c = 3 \times 10^8$ m/s).

**Solution:**

Step 1: Compute the wavelength.

$$
\lambda = \frac{c}{f} = \frac{3 \times 10^8}{150 \times 10^6} = 2.0 \text{ m}
$$

Step 2: For a half-wavelength dipole, $L = \lambda / 2$.

$$
L = \frac{2.0}{2} = 1.0 \text{ m}
$$

The physical length of the dipole is 1.0 m.

**Note:** In practice, the required length is slightly shorter than $\lambda/2$ due to end effects (the current distribution extends slightly beyond the physical ends). A common correction is $L \approx 0.95 \times (\lambda/2)$ for typical wire radii.

---

### Exercise 2: Sinusoidal Current Distribution Computation

**Problem:** A center-fed dipole of length $L = 1.5\lambda$ has a maximum current $I_m = 2$ A. Compute the current at $z = 0.3\lambda$ from the feed point.

**Solution:**

Step 1: Apply the sinusoidal current distribution formula.

$$
I(z) = I_m \sin\left[ k\left( \frac{L}{2} - |z| \right) \right]
$$

where $k = 2\pi/\lambda$, $L/2 = 0.75\lambda$, and $z = 0.3\lambda$.

Step 2: Substitute values.

$$
I(0.3\lambda) = 2 \sin\left[ \frac{2\pi}{\lambda} \left( 0.75\lambda - 0.3\lambda \right) \right]
$$

$$
I(0.3\lambda) = 2 \sin\left[ 2\pi (0.45) \right]
$$

Step 3: Evaluate.

$$
I(0.3\lambda) = 2 \sin(2.8274 \text{ rad}) = 2 \times 0.309 = 0.618 \text{ A}
$$

The current at $z = 0.3\lambda$ is approximately 0.618 A.

---

### Exercise 3: Determining the Region Boundaries

**Problem:** An antenna has a largest dimension $D = 0.5$ m and operates at $f = 300$ MHz. Compute the distances defining the reactive near-field, radiating near-field, and far-field region boundaries.

**Solution:**

Step 1: Compute the wavelength.

$$
\lambda = \frac{c}{f} = \frac{3 \times 10^8}{300 \times 10^6} = 1.0 \text{ m}
$$

Step 2: Reactive near-field boundary ($r_1 = 0.62 \sqrt{D^3/\lambda}$).

$$
r_1 = 0.62 \sqrt{\frac{(0.5)^3}{1.0}} = 0.62 \sqrt{0.125} = 0.62 \times 0.354 = 0.219 \text{ m}
$$

Step 3: Far-field boundary ($r_2 = 2D^2/\lambda$).

$$
r_2 = \frac{2(0.5)^2}{1.0} = \frac{0.5}{1.0} = 0.5 \text{ m}
$$

Step 4: Region summary.

- Reactive near-field: $r < 0.219$ m
- Radiating near-field (Fresnel): $0.219 \text{ m} < r < 0.5$ m
- Far-field (Fraunhofer): $r > 0.5$ m

---

### Exercise 4: Comparing Half-Wave and Full-Wave Dipole Currents

**Problem:** For center-fed dipoles of lengths $L = \lambda/2$ and $L = \lambda$, compute the ratio of the currents at $z = \lambda/8$ to the maximum current.

**Solution:**

Case 1: Half-wavelength dipole ($L = \lambda/2$).

$$
I(z) = I_m \cos\left( \frac{\pi z}{L} \right) = I_m \cos\left( \frac{\pi (\lambda/8)}{\lambda/2} \right) = I_m \cos\left( \frac{\pi}{4} \right) = I_m \times 0.707
$$

Ratio = $0.707$.

Case 2: Full-wavelength dipole ($L = \lambda$).

First, $L/2 = \lambda/2$. At $z = \lambda/8$, $|z| = 0.125\lambda$.

$$
I(z) = I_m \sin\left[ k\left( \frac{L}{2} - |z| \right) \right] = I_m \sin\left[ \frac{2\pi}{\lambda} \left( \frac{\lambda}{2} - \frac{\lambda}{8} \right) \right]
$$

$$
I(z) = I_m \sin\left[ 2\pi \left( \frac{3}{8} \right) \right] = I_m \sin\left( \frac{3\pi}{4} \right) = I_m \times 0.707
$$

Ratio = $0.707$.

**Observation:** Both dipoles produce the same normalized current value at $z = \lambda/8$, but the full-wave dipole has a null at its center ($z = 0$) while the half-wave has a maximum there.

---

### Exercise 5: Radiation Field from a Short Dipole

**Problem:** A short dipole of length $dl = \lambda/50$ carries a uniform current $I_0 = 1$ A. Compute the magnitude of the radiated electric field at $r = 1$ km in the direction $\theta = 90^\circ$ (broadside). Free-space impedance $\eta = 120\pi \;\Omega$.

**Solution:**

Step 1: Use the far-field expression for an infinitesimal dipole.

$$
|E_\theta| = \frac{\eta k I_0 dl \sin\theta}{4\pi r}
$$

Step 2: Compute $k$.

$$
k = \frac{2\pi}{\lambda}
$$

Step 3: Substitute values at $\theta = 90^\circ$ ($\sin\theta = 1$).

$$
|E_\theta| = \frac{120\pi \cdot (2\pi/\lambda) \cdot 1 \cdot (\lambda/50) \cdot 1}{4\pi \cdot 1000}
$$

Step 4: Simplify.

$$
|E_\theta| = \frac{120\pi \cdot 2\pi \cdot 1}{4\pi \cdot 1000 \cdot 50} = \frac{240\pi^2}{200,000\pi} = \frac{240\pi}{200,000}
$$

$$
|E_\theta| = \frac{240 \times 3.1416}{200,000} = \frac{753.98}{200,000} = 3.77 \times 10^{-3} \text{ V/m}
$$

The radiated electric field magnitude is approximately $3.77$ mV/m.

---

### Exercise 6: Identifying Antenna Types from Constraints

**Problem:** A wireless system requires an antenna that is:
- Low-profile and flush-mounted on an aircraft fuselage.
- Circularly polarized.
- Operates at 2.4 GHz with a bandwidth of 100 MHz.

Propose a suitable antenna type and justify the choice.

**Solution:**

Step 1: The low-profile, flush-mounted requirement eliminates wire antennas (dipoles, monopoles) and large aperture antennas (horns, reflectors).

Step 2: A **microstrip patch antenna** meets the low-profile requirement. A square or circular patch can be designed for circular polarization by using dual feeds with a $90^\circ$ phase shift or by perturbing the patch geometry.

Step 3: Bandwidth calculation.

$$
BW_{\%} = \frac{100}{2400} \times 100\% = 4.17\%
$$

Standard rectangular patches have bandwidths of 2–5%, so 4.17% is achievable with a thicker substrate or parasitic elements.

**Proposed antenna:** Microstrip square patch with dual-probe feed and quadrature hybrid for circular polarization.

---

### Exercise 7: Current Distribution and Pattern Relationship

**Problem:** A dipole antenna has a measured current distribution showing a null at the feed point and maxima at $z = \pm \lambda/4$ from the center. Determine the approximate length and type of this dipole.

**Solution:**

Step 1: A null at the feed point ($z = 0$) indicates $I(0) = 0$.

From the sinusoidal distribution $I(z) = I_m \sin[k(L/2 - |z|)]$, at $z = 0$:

$$
I(0) = I_m \sin(kL/2) = 0 \quad \Rightarrow \quad \frac{kL}{2} = n\pi, \; n = 1, 2, 3, \dots
$$

$$
\frac{2\pi}{\lambda} \cdot \frac{L}{2} = n\pi \quad \Rightarrow \quad L = n\lambda
$$

Step 2: With maxima at $z = \pm \lambda/4$, the dipole length satisfies $L/2 \geq \lambda/4$, so $L \geq \lambda/2$. The simplest solution is $L = \lambda$ ($n = 1$).

Step 3: Verify: For $L = \lambda$, $I(z) = I_m \sin(k|z|)$. At $z = 0$, $I = 0$. Maxima occur when $k|z| = \pi/2$, i.e., $|z| = \lambda/4$. Consistent.

**Conclusion:** The dipole is a full-wavelength dipole ($L = \lambda$).

---

### Exercise 8: Historical Impact — Selecting a Dipole Length for Maximum Power

**Problem:** Marconi's first transatlantic transmission in 1901 used a long-wire antenna operated at approximately 300 kHz. Calculate the wavelength, and determine whether a practical half-wavelength dipole could have been built. What antenna type was actually used?

**Solution:**

Step 1: Compute the wavelength at $f = 300$ kHz.

$$
\lambda = \frac{3 \times 10^8}{300 \times 10^3} = 1000 \text{ m}
$$

Step 2: A half-wavelength dipole would require $L = 500$ m. While theoretically possible, constructing and supporting a 500 m structure was impractical in 1901.

Step 3: Marconi used a **long-wire antenna** (monopole configuration with a ground system) of length significantly shorter than $\lambda/2$, relying on a large ground plane (buried radial wires) to improve radiation efficiency.

**Key insight:** Electrically short antennas ($L \ll \lambda$) have low radiation resistance and require matching networks and high currents for efficient operation. This limitation drove the development of impedance matching techniques and electrically larger antenna structures.

---

## Exam Tip: Distinguishing Antenna Types by Current Distribution

A common exam question presents a current distribution plot and asks to identify the antenna type or length. The pattern to recognize:

- **Half-wavelength dipole:** Maximum current at the center (feed point), zero at ends.
- **Full-wavelength dipole:** Zero current at the center, maxima halfway between center and ends, zero at ends.
- **Short dipole ($L \ll \lambda$):** Approximately triangular current distribution (maximum at center, linear decrease to zero at ends).
- **Traveling-wave antenna:** Phase progression along the wire with no standing-wave nulls.

Memorize the sinusoidal current distribution formula $I(z) = I_m \sin[k(L/2 - |z|)]$ and the specific forms for $L = \lambda/2$ and $L = \lambda$. These appear frequently in both theoretical and numerical problems.