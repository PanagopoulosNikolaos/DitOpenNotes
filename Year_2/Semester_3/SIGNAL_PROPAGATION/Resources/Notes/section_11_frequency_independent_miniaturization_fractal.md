# Frequency Independent Antennas, Antenna Miniaturization, and Fractal Antennas

Frequency independent antennas constitute a class of radiators whose impedance and radiation pattern remain essentially constant over bandwidths exceeding 40:1 or more, theoretically limited only by practical construction constraints. The fundamental principle, established by Rumsey in 1954, states that an antenna whose geometry is entirely specified by angles will exhibit performance independent of frequency, since scaling the structure is equivalent to rotating it. This section covers the theoretical foundations of frequency independence, the equiangular spiral and log-periodic implementations, the fundamental limits governing electrically small antennas (the Chu-Harrington bound), and the application of fractal geometries to achieve miniaturization and multi-band operation.

---

## 1. Conceptual Foundation

### 1.1 The Scaling Principle

Conventional resonant antennas (dipoles, patches) operate at frequencies where the physical length is a specific fraction of the operating wavelength (typically $\lambda/2$ or $\lambda/4$). If the frequency is changed, the electrical length changes, and the antenna must be redesigned. The key insight for frequency independent antennas is based on the following observation from scale modeling:

> If all physical dimensions of an antenna are scaled by a factor $K$, the antenna's electrical performance at frequency $f$ is identical to that of the unscaled antenna at frequency $f/K$.

Therefore, if an antenna's geometry is such that scaling it by any factor $K$ produces a structure that is congruent to the original (possibly rotated), then the antenna's performance must be independent of frequency.

### 1.2 Angle-Defined Geometry

The only way for a structure to be self-similar under arbitrary scaling is for its shape to be defined entirely in terms of angles, with no characteristic length scale. In spherical coordinates $(r, \theta, \phi)$, a shape specified only by angular coordinates:

$$
r = F(\theta, \phi)
$$

satisfies this condition because scaling $r \to Kr$ produces the same angular relation $Kr = F(\theta, \phi)$, which is equivalent to the original surface rotated or shifted.

### 1.3 The Active Region Concept

In practical frequency independent antennas, not the entire structure radiates at a given frequency. Instead, a specific **active region** — the portion of the antenna where the dimensions are comparable to the operating wavelength — contributes most of the radiation. As frequency changes, the active region shifts along the structure. This is the physical mechanism that enables wideband operation with a finite-sized antenna:

- At high frequencies, the active region is near the feed point (small dimensions).
- At low frequencies, the active region moves outward to where the structure is larger.
- The structure beyond the active region carries negligible current and can be truncated without significant performance degradation.

This property allows the infinite ideal structure to be truncated to a finite practical size while maintaining frequency independent behavior over a bandwidth determined by the ratio of the largest to smallest structural dimensions.

### 1.4 Electrically Small Antenna Limits

An **electrically small antenna** (ESA) is defined as one whose maximum dimension fits within a sphere of radius $a$ satisfying $ka < 0.5$ (or $a < \lambda/2\pi$). As antenna size decreases below this threshold, fundamental physical limits constrain the achievable bandwidth and efficiency.

- **Chu-Harrington Limit (1948):** For a linearly polarized antenna enclosed within a sphere of radius $a$, the minimum achievable radiation quality factor $Q$ is:

  $$
  Q \ge \frac{1}{k^3 a^3} + \frac{1}{ka}
  $$

  where $k = 2\pi/\lambda$ is the wavenumber. For $ka \ll 1$, this simplifies to $Q \gtrsim 1/(k^3 a^3)$.

- For a circularly polarized antenna, the limit is:

  $$
  Q \ge \frac{1}{2}\left(\frac{1}{k^3 a^3} + \frac{1}{ka}\right)
  $$

  approximately half that of the linearly polarized case.

- The fractional impedance bandwidth $B$ is inversely proportional to $Q$:

  $$
  B \approx \frac{1}{Q}
  $$

  This means that halving the antenna size reduces the maximum achievable bandwidth by a factor of approximately 8 (in the $ka \ll 1$ regime).

### 1.5 Fractal Antennas

Fractal geometries — self-similar structures where the same pattern repeats at multiple scales — naturally lend themselves to antenna applications requiring multi-band or wideband operation. Key properties include:

- **Space-Filling:** Fractal curves can pack a long electrical length into a small physical volume, enabling miniaturization.
- **Self-Similarity:** The repeating structure at different scales produces resonant behavior at multiple harmonically related frequencies.
- **Log-Periodic Character:** Some fractal geometries (e.g., Sierpinski gasket) exhibit a log-periodic variation of impedance with frequency, similar to conventional log-periodic antennas.

> **[Supplementary]** The mathematical definition of a fractal set requires that its Hausdorff dimension $D$ exceeds its topological dimension. For antenna applications, the most commonly used fractals include the Koch curve ($D \approx 1.26$), Sierpinski gasket ($D \approx 1.58$), and Minkowski island ($D \approx 1.50$).

---

## 2. Formal Definitions and Models

### 2.1 The Equiangular (Logarithmic) Spiral Antenna

#### 2.1.1 Geometry

The equiangular spiral (also called the logarithmic spiral) is defined in polar coordinates $(r, \phi)$ on a planar surface by:

$$
r = r_0 e^{a\phi}
$$

where:
- $r_0$ is the starting radius at $\phi = 0$,
- $a$ is the spiral rate (the reciprocal of the tangent angle).

The defining property of this curve is that scaling $r$ by any factor $K$ is equivalent to rotation by $\Delta\phi = (\ln K)/a$:

$$
K r = K r_0 e^{a\phi} = r_0 e^{a(\phi + (\ln K)/a)}
$$

A planar equiangular spiral antenna consists of two or four metallic arms bounded by spiral curves. For a two-arm antenna, the arm edges are defined by:

- Arm 1, Edge 1: $r = r_1 e^{a\phi}$
- Arm 1, Edge 2: $r = r_2 e^{a\phi}$
- Arm 2, Edge 1: $r = r_1 e^{a(\phi - \pi)}$
- Arm 2, Edge 2: $r = r_2 e^{a(\phi - \pi)}$

The antenna is fed at the center ($r \to 0$) where the arms converge.

#### 2.1.2 Operating Band Determination

The frequency range of a practical equiangular spiral antenna is determined by:

- **Highest frequency** $f_{\text{max}}$: Determined by the inner radius $r_{\text{in}}$ (the smallest dimension near the feed):

  $$
  f_{\text{max}} \approx \frac{c}{4 r_{\text{in}}}
  $$

- **Lowest frequency** $f_{\text{min}}$: Determined by the outer radius $r_{\text{out}}$ (the largest dimension of the truncated structure):

  $$
  f_{\text{min}} \approx \frac{c}{4 r_{\text{out}}}
  $$

#### 2.1.3 Radiation Characteristics

The planar equiangular spiral antenna radiates:
- **Bidirectional beams** perpendicular to the plane of the spiral (broadside).
- **Circular polarization:** The sense of polarization depends on the winding direction:
  - Right-handed spiral $\to$ Right-Hand Circular Polarization (RHCP) on one side.
  - Left-handed spiral $\to$ Left-Hand Circular Polarization (LHCP) on the opposite side.
- **Half-Power Beamwidth:** Approximately $70^\circ - 90^\circ$.

#### 2.1.4 Conical Equiangular Spiral

The planar spiral can be conformally mapped onto a conical surface to achieve unidirectional radiation. The cone angle $\theta_0$ determines the pattern shape. For $\theta_0 < 45^\circ$, radiation is confined to a single lobe directed off the apex.

### 2.2 Log-Periodic Antennas

#### 2.2.1 Theory of Periodic Structures

A log-periodic antenna achieves nearly frequency independent operation by using a structure whose geometry repeats periodically with the logarithm of frequency. The scaling factor $\tau$ defines the ratio between successive element dimensions:

$$
\tau = \frac{L_{n+1}}{L_n} = \frac{d_{n+1}}{d_n}
$$

where $L_n$ is the length of the $n$-th element and $d_n$ is its spacing from the preceding element. Typical values are $0.7 \le \tau \le 0.95$.

The performance repeats periodically at frequencies:

$$
f_n = \frac{f_0}{\tau^n}
$$

where $f_0$ is a reference frequency.

#### 2.2.2 Log-Periodic Dipole Array (LPDA)

The LPDA is the most common log-periodic antenna configuration. It consists of a series of dipole elements of increasing length, fed by a balanced transmission line with a phase reversal between adjacent elements (crisscross feed).

```
            Feed Point (Apex)
                 |
           +-----+-----+-----+-----+-----+-----+-----+
           |     |     |     |     |     |     |     |
    ---(---|--(--|----(----|----(---|----(---|----(---|----)---)
           |     |     |     |     |     |     |     |
           +-----+-----+-----+-----+-----+-----+-----+
                Short    Medium    Long     Longest
                dipole   dipole    dipole   dipole
           <------ Active Region moves outward as f decreases ------>
```

**Design Parameters:**

| Parameter | Symbol | Definition |
|:---|:---|:---|
| Scaling factor | $\tau$ | $L_{n+1}/L_n$ |
| Spacing factor | $\sigma$ | $d_n/(2L_n)$ |
| Included angle | $2\alpha$ | $\tan^{-1}\left(\frac{1-\tau}{4\sigma}\right)$ |
| Structure bandwidth | $B_s$ | Desired operating bandwidth |
| Active region bandwidth | $B_{\text{ar}}$ | $1.1 + 7.7(1-\tau)^2\cot\alpha$ |
| Number of elements | $N$ | $1 + \frac{\ln(B_s B_{\text{ar}})}{\ln(1/\tau)}$ |

**Design Procedure (Carrel Method):**

1. Choose the desired directivity $D_0$ (in dB) for the application.
2. From the directivity curves, select $\tau$ and $\sigma$.
3. Compute the included angle $\alpha$:

   $$
   \alpha = \tan^{-1}\left(\frac{1-\tau}{4\sigma}\right)
   $$

4. Determine the longest and shortest element lengths:

   $$
   L_{\text{max}} = \frac{\lambda_{\text{max}}}{2}, \quad L_{\text{min}} = \frac{\lambda_{\text{min}}}{2}
   $$

   where $\lambda_{\text{max}} = c/f_{\text{min}}$ and $\lambda_{\text{min}} = c/f_{\text{max}}$.

5. Compute the number of elements $N$.
6. Calculate element lengths $L_n = \tau^{n-1} L_{\text{max}}$ for $n = 1, 2, \ldots, N$.
7. Calculate element spacings $d_n = 2\sigma L_n$.

#### 2.2.3 Radiation Characteristics

- **Linear polarization** (for dipole-based designs).
- **Unidirectional beam** directed toward the apex (the smaller end).
- **Beamwidth** decreases as directivity increases.
- **Input impedance** remains nearly constant over the operating band (typically $50 - 200 \; \Omega$ depending on the feed design).

### 2.3 Fundamental Limits of Electrically Small Antennas

#### 2.3.1 The Chu-Harrington Bound

For an antenna enclosed in a sphere of radius $a$, the minimum quality factor $Q$ for a lossless antenna is:

$$
Q_{\text{min}} = \frac{1}{k^3 a^3} + \frac{1}{ka}
$$

For $ka \ll 1$, the dominant term is:

$$
Q_{\text{min}} \approx \frac{1}{k^3 a^3} = \frac{\lambda^3}{8\pi^3 a^3}
$$

The maximum fractional bandwidth (for a matched load) is:

$$
B_{\text{max}} \approx \frac{1}{Q_{\text{min}}} \approx k^3 a^3 \quad (ka \ll 1)
$$

#### 2.3.2 Radiation Efficiency and Size

For a lossy small antenna with conductor losses, the actual quality factor $Q_L$ becomes:

$$
Q_L = \frac{Q_{\text{min}}}{\eta_r}
$$

where $\eta_r$ is the radiation efficiency. The efficiency itself degrades as the size decreases:

$$
\eta_r \approx \frac{R_r}{R_r + R_l}
$$

where $R_r$ is the radiation resistance and $R_l$ is the loss resistance. For electrically small dipoles:

$$
R_r \propto (ka)^4, \quad R_l \propto \frac{l}{A}\sqrt{\frac{\pi f \mu}{\sigma}}
$$

where $l$ is the conductor length, $A$ is the cross-sectional area, and $\sigma$ is the conductivity.

> **[Key Insight]** The radiation resistance of an electrically small antenna scales as $(ka)^4$, while ohmic losses scale roughly linearly with frequency. Below a critical size $ka_{\text{crit}} \approx \left(\frac{2}{\eta_0}\sqrt{\frac{\pi f \mu}{\sigma}}\right)^{1/3}$, the efficiency degrades catastrophically — dropping from near 100% to near 0% over a very narrow size range.

#### 2.3.3 Gain-Bandwidth Product

For small antennas, there is a fundamental tradeoff captured by the gain-bandwidth product:

$$
G \cdot B \le \frac{1}{Q_{\text{min}}}
$$

This means that high gain and wide bandwidth cannot be simultaneously achieved from a small antenna. Any attempt to increase one necessarily reduces the other.

### 2.4 Fractal Antennas

#### 2.4.1 Koch Fractal Monopole

The Koch curve is generated by an iterative process starting from a straight line segment (initiator). Each segment is replaced by four segments of length $1/3$ of the original, arranged to form an equilateral triangle protrusion.

```
Iteration 0:  _______________
Iteration 1:  __/\__
Iteration 2:  _/\_  _/\_
Iteration 3:  /\  /\  /\  /\
```

The total length of the Koch curve after $n$ iterations is:

$$
L_n = L_0 \left(\frac{4}{3}\right)^n
$$

where $L_0$ is the initiator length. This increase in electrical length within a fixed physical footprint enables antenna miniaturization. A Koch fractal monopole can achieve the same resonant frequency as a standard monopole with a physical height reduction of $30\% - 50\%$.

#### 2.4.2 Sierpinski Gasket Monopole

The Sierpinski gasket is a triangular fractal structure. Starting from an equilateral triangle, the central inverted triangle is removed, and the process is repeated for the remaining three triangles.

The Sierpinski gasket antenna exhibits **log-periodic behavior** — its input impedance and radiation pattern repeat periodically with frequency. The period is determined by the scaling factor $\delta = 2$ (the linear scaling factor between successive iterations):

$$
f_{n+1} = \delta f_n = 2 f_n
$$

This makes the Sierpinski gasket naturally suited for dual-band or multi-band operation with octave spacing between bands.

#### 2.4.3 Hilbert Curve Fractal

The Hilbert curve is a continuous, space-filling fractal that maps a one-dimensional line into a two-dimensional plane. For antenna applications, the Hilbert curve provides the maximum possible length within a given area. A Hilbert curve of iteration order $n$ fills a square of side length $(2^n - 1) \times \text{segment length}$ with a total length of $(2^{2n} - 1)$ segments.

---

## 3. Key Parameters and Constraints

### Table 1: Design Parameters for Frequency Independent and Fractal Antennas

| Parameter | Symbol | Typical Range | Units | Operational Impact |
|:---|:---|:---|:---|:---|
| Spiral growth rate | $a$ | $0.1 - 0.3$ | dimensionless | Faster growth reduces number of turns; too fast degrades pattern |
| Spiral turns | $N$ | $1.5 - 5$ | dimensionless | More turns increases low-frequency cutoff and bandwidth ratio |
| Log-periodic scaling factor | $\tau$ | $0.7 - 0.95$ | dimensionless | Higher $\tau$ increases directivity but requires more elements |
| Log-periodic spacing factor | $\sigma$ | $0.03 - 0.25$ | dimensionless | Controls mutual coupling and input impedance |
| Electrical size | $ka$ | $0.1 - 0.5$ | dimensionless | Determines $Q$ and maximum bandwidth via Chu limit |
| Fractal iteration order | $n$ | $1 - 4$ | dimensionless | Higher order increases electrical length but adds complexity |
| Fractal scaling factor | $\delta$ | $2 - 4$ | dimensionless | Determines frequency ratio between bands |

### Table 2: Comparative Summary of Frequency Independent and Miniature Antenna Types

| Antenna Type | Bandwidth (VSWR < 2) | Polarization | Directivity | Key Advantage | Key Disadvantage |
|:---|:---|:---|:---|:---|:---|
| **Planar Equiangular Spiral** | Very Broad (40:1+) | Circular (RHCP/LHCP) | Low-Moderate (3-6 dBi) | Theoretical unlimited bandwidth | Bidirectional; needs cavity for unidirectional |
| **Conical Equiangular Spiral** | Very Broad (40:1+) | Circular | Moderate (5-8 dBi) | Unidirectional; extremely wideband | Complex construction; large size |
| **Log-Periodic Dipole Array** | Broad (10:1+) | Linear | Moderate-High (6-10 dBi) | Linear polarization; modest gain | Large physical size; phase center varies with frequency |
| **Log-Periodic Zigzag** | Broad (10:1+) | Linear (vertical) | High (8-12 dBi) | High gain over ground | Narrower bandwidth than spiral |
| **Electrically Small Dipole** | Very Narrow (< 1%) | Linear | Very Low (1-2 dBi) | Small physical size | Very high $Q$; extreme matching challenge |
| **Koch Fractal Monopole** | Narrow-Moderate (2-10%) | Linear | Low (1-3 dBi) | Miniaturization (30-50% height reduction) | Multi-band not always controllable |
| **Sierpinski Gasket** | Multi-band (log-periodic) | Linear | Low-Moderate (3-6 dBi) | Natural multi-band with octave spacing | Complex geometry |

---

## 4. Step-by-Step Mechanism

### 4.1 How an Equiangular Spiral Antenna Radiates

1. **Center Feed Excitation:** The two arms of the spiral are fed at the center by a balanced transmission line (or an "infinite balun" where the coaxial feed cable becomes one arm).
2. **Outward Traveling Current:** The applied voltage launches an outward-traveling current wave along the spiral arms. The current magnitude decays as it propagates due to radiation.
3. **Active Region Formation:** At a given frequency $f$, there exists a circumferential band around the spiral where the circumference is approximately one wavelength ($C \approx \lambda$). In this active region, currents on adjacent spiral turns are in phase, leading to constructive radiation.
4. **Phase Matching Condition:** The spiral geometry ensures that the phase velocity of the current wave matches the speed of light, and the path length difference between adjacent turns is one wavelength. This produces broadside radiation perpendicular to the spiral plane.
5. **Current Decay:** Beyond the active region, the current amplitude has decayed to negligible levels (due to radiation damping), so truncation of the spiral at the outer radius does not cause significant reflections.
6. **Frequency Shift:** As the operating frequency changes, the active region shifts radially. At higher frequencies, it moves inward toward the center; at lower frequencies, it moves outward. The pattern and impedance remain essentially unchanged as long as the active region fits within the physical structure.

### 4.2 How a Log-Periodic Dipole Array Radiates

1. **Transmission Line Feed:** All dipoles are connected in parallel across a balanced transmission line with alternating phase (crisscross feed). This introduces a $180^\circ$ phase shift between successive dipoles.
2. **Active Region Formation:** At a given frequency $f$, the dipoles whose lengths are near resonance (approximately $\lambda/2$) carry the largest currents. Shorter dipoles have high capacitive reactance and carry little current; longer dipoles are inductive and also carry reduced current.
3. **Phase Alignment Toward Apex:** The combination of the transmission line phase delay and the spacing between elements causes the fields from the active dipoles to add constructively in the direction toward the apex (the smaller end), producing a unidirectional beam.
4. **Frequency Shift:** When the frequency decreases, the active region moves toward the longer dipoles. When the frequency increases, it moves toward the shorter dipoles. Over the designed scaling range, the pattern and impedance remain essentially constant.
5. **Truncation Effect:** Dipoles much longer than resonance (beyond the active region) are not strongly excited and can be omitted. Similarly, dipoles much shorter than resonance can be omitted at the high-frequency end, establishing the practical bandwidth limits.

### 4.3 Miniaturization via Fractal Geometry

The miniaturization effect of fractal antennas is explained by the following mechanism:

1. **Increased Effective Length:** A fractal curve compresses a long conductor into a small area. For the Koch curve, each iteration multiplies the total length by $4/3$, so after $n$ iterations the length is $L_0(4/3)^n$ while the end-to-end distance remains $L_0$.
2. **Resonant Frequency Shift:** The resonant frequency of a monopole is inversely proportional to its electrical length. Since a fractal monopole has a longer current path than a straight monopole of the same height, the resonant frequency is lower. Equivalently, for a given target frequency, the fractal monopole can be physically shorter.
3. **Multi-Resonant Behavior (Sierpinski):** The self-similar structure supports multiple resonant modes at frequencies corresponding to the different scales present in the geometry. For the Sierpinski gasket with scaling factor $\delta = 2$, the resonances occur at $f_0, 2f_0, 4f_0, \ldots$.

---

## Solved Exercises

### Exercise 1: Bandwidth Ratio of an Equiangular Spiral Antenna

**Problem:** A planar equiangular spiral antenna has an outer radius $r_{\text{out}} = 25$ cm and an inner radius $r_{\text{in}} = 2$ mm. Calculate:
1. The lowest operating frequency $f_{\text{min}}$.
2. The highest operating frequency $f_{\text{max}}$.
3. The bandwidth ratio $f_{\text{max}}/f_{\text{min}}$.

**Solution:**

#### Step 1: Calculate the lowest frequency

Using the relation $f_{\text{min}} \approx c/(4 r_{\text{out}})$:

$$
f_{\text{min}} \approx \frac{3 \times 10^8 \text{ m/s}}{4 \times 0.25 \text{ m}} = 300 \text{ MHz}
$$

#### Step 2: Calculate the highest frequency

Using $f_{\text{max}} \approx c/(4 r_{\text{in}})$:

$$
f_{\text{max}} \approx \frac{3 \times 10^8 \text{ m/s}}{4 \times 0.002 \text{ m}} = 37.5 \text{ GHz}
$$

#### Step 3: Compute the bandwidth ratio

$$
\frac{f_{\text{max}}}{f_{\text{min}}} = \frac{37.5 \times 10^9}{300 \times 10^6} = 125:1
$$

This is an extremely wide bandwidth, far exceeding what any resonant antenna can achieve.

---

### Exercise 2: Log-Periodic Dipole Array Design

**Problem:** Design an LPDA to operate from $f_{\text{min}} = 200$ MHz to $f_{\text{max}} = 2$ GHz with a directivity of $8$ dBi. Use the Carrel design method with $\tau = 0.87$ and $\sigma = 0.08$.

1. Calculate the included angle $2\alpha$.
2. Determine the structure bandwidth $B_s$.
3. Compute the active region bandwidth $B_{\text{ar}}$.
4. Find the number of elements $N$ required.
5. Calculate the longest and shortest element lengths.
6. Calculate the first three element lengths and spacings.

**Solution:**

#### Step 1: Calculate the included angle

$$
\alpha = \tan^{-1}\left(\frac{1-\tau}{4\sigma}\right) = \tan^{-1}\left(\frac{1-0.87}{4 \times 0.08}\right) = \tan^{-1}\left(\frac{0.13}{0.32}\right)
$$

$$
\alpha = \tan^{-1}(0.40625) \approx 22.1^\circ
$$

The included angle is $2\alpha \approx 44.2^\circ$.

#### Step 2: Determine the structure bandwidth

$$
B_s = \frac{f_{\text{max}}}{f_{\text{min}}} = \frac{2000}{200} = 10
$$

#### Step 3: Compute the active region bandwidth

$$
B_{\text{ar}} = 1.1 + 7.7(1-\tau)^2\cot\alpha
$$

First compute $\cot\alpha$:

$$
\cot(22.1^\circ) = \frac{1}{\tan(22.1^\circ)} = \frac{1}{0.40625} \approx 2.462
$$

Then:

$$
B_{\text{ar}} = 1.1 + 7.7(1-0.87)^2(2.462) = 1.1 + 7.7(0.0169)(2.462)
$$

$$
B_{\text{ar}} = 1.1 + 7.7 \times 0.0416 = 1.1 + 0.320 = 1.42
$$

#### Step 4: Find the number of elements

$$
N = 1 + \frac{\ln(B_s B_{\text{ar}})}{\ln(1/\tau)} = 1 + \frac{\ln(10 \times 1.42)}{\ln(1/0.87)}
$$

$$
N = 1 + \frac{\ln(14.2)}{\ln(1.1494)} = 1 + \frac{2.653}{0.1393} = 1 + 19.05 \approx 20
$$

Twenty elements are needed.

#### Step 5: Calculate the extreme element lengths

First, compute the wavelength extremes:

$$
\lambda_{\text{max}} = \frac{c}{f_{\text{min}}} = \frac{3 \times 10^8}{200 \times 10^6} = 1.5 \text{ m}
$$

$$
\lambda_{\text{min}} = \frac{c}{f_{\text{max}}} = \frac{3 \times 10^8}{2 \times 10^9} = 0.15 \text{ m}
$$

Element lengths:

$$
L_{\text{max}} = \frac{\lambda_{\text{max}}}{2} = 0.75 \text{ m}
$$

$$
L_{\text{min}} = \frac{\lambda_{\text{min}}}{2} = 0.075 \text{ m}
$$

#### Step 6: Calculate the first three element lengths and spacings

Starting from the largest element ($n = 1$):

$$
L_1 = L_{\text{max}} = 0.75 \text{ m}
$$

$$
L_2 = \tau L_1 = 0.87 \times 0.75 = 0.6525 \text{ m}
$$

$$
L_3 = \tau L_2 = 0.87 \times 0.6525 = 0.5677 \text{ m}
$$

Spacings:

$$
d_1 = 2\sigma L_1 = 2 \times 0.08 \times 0.75 = 0.12 \text{ m}
$$

$$
d_2 = 2\sigma L_2 = 2 \times 0.08 \times 0.6525 = 0.1044 \text{ m}
$$

$$
d_3 = 2\sigma L_3 = 2 \times 0.08 \times 0.5677 = 0.0908 \text{ m}
$$

---

### Exercise 3: Chu-Harrington Limit Computation

**Problem:** An electrically small antenna must fit inside a sphere of radius $a = 5$ cm and operate at $f = 400$ MHz. Determine:
1. The electrical size $ka$.
2. The minimum $Q$ for a linearly polarized antenna.
3. The maximum achievable fractional bandwidth.
4. How many times worse the bandwidth would be if the antenna size were halved (to $a = 2.5$ cm).

**Solution:**

#### Step 1: Compute the wavelength and $ka$

$$
\lambda = \frac{c}{f} = \frac{3 \times 10^8}{400 \times 10^6} = 0.75 \text{ m} = 75 \text{ cm}
$$

$$
k = \frac{2\pi}{\lambda} = \frac{2\pi}{0.75} \approx 8.378 \text{ rad/m}
$$

$$
ka = 8.378 \times 0.05 = 0.4189
$$

Since $ka = 0.4189 < 0.5$, the antenna is electrically small.

#### Step 2: Compute the minimum $Q$

$$
Q_{\text{min}} = \frac{1}{(ka)^3} + \frac{1}{ka} = \frac{1}{(0.4189)^3} + \frac{1}{0.4189}
$$

First compute $(ka)^3$:

$$
(ka)^3 = (0.4189)^3 = 0.0735
$$

Then:

$$
Q_{\text{min}} = \frac{1}{0.0735} + \frac{1}{0.4189} = 13.60 + 2.39 = 15.99 \approx 16
$$

#### Step 3: Compute the maximum fractional bandwidth

$$
B_{\text{max}} \approx \frac{1}{Q_{\text{min}}} = \frac{1}{16} = 0.0625 \text{ (or } 6.25\%)
$$

#### Step 4: Effect of halving the size

With $a = 2.5$ cm:

$$
ka = 0.4189/2 = 0.20945
$$

$$
(ka)^3 = (0.20945)^3 = 0.00919
$$

$$
Q_{\text{min}}' = \frac{1}{0.00919} + \frac{1}{0.20945} = 108.8 + 4.77 = 113.6
$$

The bandwidth degrades by:

$$
\frac{B_{\text{max}}}{B_{\text{max}}'} = \frac{Q_{\text{min}}'}{Q_{\text{min}}} = \frac{113.6}{16} \approx 7.1
$$

Halving the antenna radius reduces the maximum bandwidth by a factor of approximately 7.

---

### Exercise 4: Koch Fractal Monopole Miniaturization

**Problem:** A standard quarter-wave monopole resonates at $f = 900$ MHz. If a Koch fractal monopole of iteration $n = 2$ is used, estimate the physical height reduction.

**Solution:**

#### Step 1: Calculate the standard monopole height

$$
h_{\text{std}} = \frac{\lambda}{4} = \frac{c}{4f} = \frac{3 \times 10^8}{4 \times 900 \times 10^6} = 0.0833 \text{ m} = 8.33 \text{ cm}
$$

#### Step 2: Calculate the Koch length multiplication factor

For $n = 2$ iterations:

$$
\frac{L_2}{L_0} = \left(\frac{4}{3}\right)^2 = \frac{16}{9} \approx 1.778
$$

#### Step 3: Estimate the resonant height of the fractal monopole

The electrical length of the fractal monopole is the physical height times the length multiplication factor:

$$
L_{\text{elec}} = h_{\text{fractal}} \times 1.778
$$

For resonance, $L_{\text{elec}} = h_{\text{std}}$, so:

$$
h_{\text{fractal}} = \frac{h_{\text{std}}}{1.778} = \frac{8.33}{1.778} \approx 4.68 \text{ cm}
$$

#### Step 4: Compute the height reduction

$$
\text{Reduction} = \frac{h_{\text{std}} - h_{\text{fractal}}}{h_{\text{std}}} \times 100\% = \frac{8.33 - 4.68}{8.33} \times 100\% \approx 43.8\%
$$

The Koch fractal monopole achieves a $43.8\%$ height reduction compared to the standard quarter-wave monopole.

---

### Exercise 5: Sierpinski Gasket Multi-Band Operation

**Problem:** A Sierpinski gasket antenna has its lowest resonant frequency at $f_1 = 800$ MHz. Determine:
1. The next two resonant frequencies $f_2$ and $f_3$.
2. The frequency bands suitable for Wi-Fi (2.4 GHz) and Bluetooth (2.45 GHz).

**Solution:**

#### Step 1: Apply the log-periodic scaling

The Sierpinski gasket has a scaling factor $\delta = 2$ between successive resonances:

$$
f_2 = \delta f_1 = 2 \times 800 \text{ MHz} = 1.6 \text{ GHz}
$$

$$
f_3 = \delta f_2 = 2 \times 1.6 \text{ GHz} = 3.2 \text{ GHz}
$$

#### Step 2: Evaluate suitability for Wi-Fi/Bluetooth

The Wi-Fi/Bluetooth bands (2.4 - 2.48 GHz) fall between $f_2 = 1.6$ GHz and $f_3 = 3.2$ GHz. The Sierpinski gasket does not provide a resonance exactly at 2.45 GHz with this scaling factor.

> **[Supplementary]** To cover the 2.45 GHz band, a modified Sierpinski geometry with a non-integer scaling factor (e.g., $\delta \approx 1.75$) could be used, or the antenna could be fed with a modified feed structure to shift the impedance bandwidth of one of the existing resonances to cover the desired frequency.

---

### Exercise 6: Comparison Between Spiral and Log-Periodic Antennas

**Problem:** Compare the planar equiangular spiral antenna and the LPDA for the following application requirements and determine which is better suited for each case:
1. Application A: Requires circular polarization, bandwidth 20:1.
2. Application B: Requires linear polarization, bandwidth 10:1, directivity $>$ 8 dBi.
3. Application C: Requires the smallest possible physical size at 1 GHz.

**Solution:**

#### Application A (Circular Polarization, 20:1 Bandwidth)

The equiangular spiral antenna naturally radiates circular polarization and can easily achieve a 20:1 bandwidth. The LPDA radiates linear polarization and would require an external polarizer. The spiral antenna is the clear choice.

#### Application B (Linear Polarization, 10:1 Bandwidth, High Directivity)

The LPDA can achieve 10:1 bandwidth with directivity exceeding 8 dBi (requires $\tau > 0.9$ and $\sigma \approx 0.08 - 0.12$). The spiral antenna has lower directivity (typically $3 - 6$ dBi). The LPDA is better suited.

#### Application C (Smallest Size at 1 GHz)

At 1 GHz, an LPDA must have a longest element of $\lambda/2 = 15$ cm, and the overall length along the boom is typically several times this. A spiral antenna at 1 GHz requires an outer radius of approximately $\lambda/4 = 7.5$ cm. The spiral is more compact for a given lowest operating frequency. However, an electrically small fractal monopole could be even smaller (a few cm) if narrow bandwidth is acceptable. Among the two frequency independent types, the spiral is the smaller choice.

---

### Exercise 7: Spiral Antenna Parameter Effects

**Problem:** A planar equiangular spiral antenna is designed with a growth rate $a = 0.22$ and 3 turns.
1. Calculate the ratio of the outer radius to the inner radius.
2. Determine the bandwidth ratio.
3. If the growth rate is changed to $a = 0.15$ with the same number of turns, how does the bandwidth change?
4. If the number of turns is increased to 5 with $a = 0.22$, how does the bandwidth change?

**Solution:**

#### Step 1: Calculate the radius ratio for $a = 0.22$, $N = 3$

Each turn corresponds to $\Delta\phi = 2\pi$. For $N$ turns:

$$
\phi_{\text{total}} = 2\pi N = 2\pi \times 3 = 6\pi \text{ radians}
$$

The radius ratio is:

$$
\frac{r_{\text{out}}}{r_{\text{in}}} = e^{a\phi_{\text{total}}} = e^{0.22 \times 6\pi}
$$

First compute $0.22 \times 6\pi = 0.22 \times 18.850 = 4.147$:

$$
\frac{r_{\text{out}}}{r_{\text{in}}} = e^{4.147} \approx 63.3
$$

#### Step 2: Bandwidth ratio

Since $f \propto 1/r$:

$$
\frac{f_{\text{max}}}{f_{\text{min}}} \approx \frac{r_{\text{out}}}{r_{\text{in}}} = 63.3:1
$$

#### Step 3: Effect of slower growth rate ($a = 0.15$, $N = 3$)

The slower growth rate means the spiral expands less per turn:

$$
\frac{r_{\text{out}}}{r_{\text{in}}} = e^{0.15 \times 6\pi} = e^{2.827} \approx 16.9:1
$$

The bandwidth is reduced from $63.3:1$ to $16.9:1$. A slower growth rate requires more turns to achieve the same bandwidth.

#### Step 4: Effect of more turns ($a = 0.22$, $N = 5$)

$$
\frac{r_{\text{out}}}{r_{\text{in}}} = e^{0.22 \times 10\pi} = e^{6.912} \approx 1006:1
$$

The bandwidth increases dramatically. However, practical considerations limit the achievable bandwidth (conductor losses, manufacturing tolerances, truncated currents).

---

### Exercise 8: Electrically Small Antenna Matching Challenge

**Problem:** An electrically small loop antenna has $ka = 0.2$, radiation resistance $R_r = 0.05 \; \Omega$, and loss resistance $R_l = 0.5 \; \Omega$. The antenna must be matched to a $50 \; \Omega$ source.
1. Calculate the radiation efficiency $\eta_r$.
2. Calculate the minimum $Q$ from the Chu-Harrington limit.
3. Estimate the required matching network bandwidth.
4. Discuss the feasibility of matching.

**Solution:**

#### Step 1: Calculate the radiation efficiency

$$
\eta_r = \frac{R_r}{R_r + R_l} = \frac{0.05}{0.05 + 0.5} = \frac{0.05}{0.55} \approx 0.091 \text{ (or } 9.1\%)
$$

#### Step 2: Calculate the Chu-Harrington $Q$ limit

$$
Q_{\text{min}} = \frac{1}{(ka)^3} + \frac{1}{ka} = \frac{1}{(0.2)^3} + \frac{1}{0.2} = \frac{1}{0.008} + 5
$$

$$
Q_{\text{min}} = 125 + 5 = 130
$$

#### Step 3: Estimate the matching network bandwidth

The $Q$ of the antenna is so high ($Q > 100$) that the matching network would have a fractional bandwidth of less than $1\%$. The actual bandwidth of the matched antenna is:

$$
B \approx \frac{1}{Q_{\text{min}}} \approx 0.0077 \text{ (or } 0.77\%)
$$

#### Step 4: Feasibility discussion

Matching this antenna is extremely challenging for several reasons:

1. **High $Q$:** The bandwidth is under $1\%$, meaning the antenna can only operate effectively over a very narrow frequency range.
2. **Low radiation resistance:** $R_r = 0.05 \; \Omega$ requires a large impedance transformation ratio ($50/0.05 = 1000:1$), which is difficult to achieve with low loss.
3. **Low efficiency:** Only $9.1\%$ of the input power is radiated; $90.9\%$ is lost as heat in the conductor.
4. **Matching network losses:** The matching network itself will introduce additional losses, further reducing the overall efficiency.

This antenna would only be practical in applications where extreme miniaturization is essential and very low efficiency is acceptable.

---

## Exam Tip: Frequency Independent and Miniature Antennas

1. **Active Region Concept:** Remember that in any frequency independent antenna, only a portion of the structure (the "active region") radiates at a given frequency. The active region shifts with frequency. This is the key to understanding why these antennas can be truncated to finite size while maintaining wideband performance.

2. **Chu-Harrington Inverse Cube Law:** The minimum quality factor scales as $1/(ka)^3$ for small antennas. This means reducing the size by half increases $Q$ by a factor of approximately 8, and reduces the maximum bandwidth by the same factor. This is a fundamental physical limit — no matching network, metamaterial, or other technique can circumvent it.

3. **Logarithmic Spiral vs. Archimedean Spiral:** Do not confuse the two. The logarithmic (equiangular) spiral has frequency independent properties because its geometry is angle-defined ($r = r_0 e^{a\phi}$). The Archimedean spiral ($r = a\phi$) introduces a fixed length scale and does not achieve true frequency independence, though it still offers broad bandwidth.

4. **Log-Periodic Dipole Array Feed:** The crisscross (alternating) feed line is essential for the LPDA to achieve a unidirectional beam toward the apex. Without the phase reversal between elements, the array would radiate bidirectionally and would not be frequency independent.

5. **Fractal Miniaturization Limitation:** While fractal geometries can reduce the physical size of an antenna, the Chu-Harrington limit still applies — the fundamental $Q$ bound is determined by the smallest sphere that encloses the entire antenna. A fractal antenna cannot exceed the gain-bandwidth product limit any more than a conventional antenna can.

6. **Polarization of Spiral Antennas:** The handedness of the spiral determines the polarization sense. A right-handed spiral radiates RHCP on one side and LHCP on the opposite side. Switching the feed connections does not change the handedness; it only changes which side radiates.

7. **LPDA Directivity Design:** Higher directivity requires a scaling factor $\tau$ closer to unity (typically $\tau > 0.9$ for $D > 8$ dBi). However, this increases the number of elements and the overall size of the antenna. There is a direct tradeoff between directivity and compactness.

---

## Connections and Cross-References

- **Section 2 (Fundamental Parameters):** The definitions of directivity, gain, bandwidth, polarization, and input impedance are all used to characterize frequency independent antennas. The polarization definitions are essential for understanding spiral antenna operation.
- **Section 4 (Linear Wire Antennas):** The half-wave dipole is the basic building block of the LPDA. Understanding the impedance and radiation patterns of isolated dipoles is a prerequisite for LPDA design.
- **Section 10 (Traveling Wave and Broadband Antennas):** The traveling wave mechanism and the Yagi-Uda array are historically and conceptually related. Log-periodic arrays can be viewed as a generalization of the Yagi-Uda concept to wideband operation.
- **Section 12 (Aperture Antennas):** Spiral antennas are sometimes used as feeds for reflector antennas, where their wideband circularly polarized output is advantageous.

*Prerequisite: Section 2 (Fundamental Parameters) — polarization definitions, bandwidth, directivity. Section 4 (Linear Wire Antennas) — dipole impedance and patterns.*
