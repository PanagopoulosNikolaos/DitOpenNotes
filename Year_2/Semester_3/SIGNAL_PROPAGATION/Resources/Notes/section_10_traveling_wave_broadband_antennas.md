# Traveling Wave and Broadband Antennas

Traveling wave antennas represent a class of non-resonant radiators where the electric current propagates as a unidirectional wave along the guiding structure, rather than forming a standing wave. By terminating the antenna structure with a matched load, reflection from the open end is eliminated, resulting in a low-Q system that exhibits stable input impedance and radiation patterns over a wide frequency band. This section covers the theoretical foundations, mathematical formulations, and engineering design principles of long-wire traveling wave antennas, V antennas, rhombic antennas, helical antennas (operating in normal and axial modes), and Yagi-Uda arrays.

---

## 1. Conceptual Foundation

### 1.1 Resonant vs. Non-Resonant (Traveling Wave) Antennas
Standing waves on traditional resonant antennas (such as thin wire dipoles) are formed by the superposition of waves traveling outward from the feedpoint and their reflections from the open ends of the conductor. The open ends act as large impedance mismatches, reflecting the wave back with a phase shift. This reflections-based resonance stores reactive energy near the antenna, producing a high quality factor ($Q$). Consequently, the input reactance changes rapidly with frequency, limiting the matching bandwidth to typically $2\% - 5\%$.

Non-resonant (traveling wave) antennas suppress end reflections by terminating the antenna structure opposite the feedpoint with a resistive load equal to the antenna's characteristic impedance. Without reflections, the current travels exclusively in one direction. The absence of stored reactive energy results in a very low quality factor ($Q$), enabling stable input impedance and broad bandwidth (often spanning several octaves).

### 1.2 Radiation Mechanism and Wave Lobe Offsets
In a traveling wave antenna, radiation occurs along the length of the conductor. As the electromagnetic wave propagates along the wire, it leaks energy into space. Because the current phase varies continuously along the wire ($e^{-jkz'}$), the radiation from different segments of the wire adds constructively at an oblique angle $\theta_{\text{max}}$ relative to the wire axis. As the wire length increases, the phase velocity of the wave along the wire relative to the speed of light causes the main lobe of the radiation pattern to tilt closer to the axis of the wire (tending toward an endfire configuration).

### 1.3 Helical Antenna Modes and Polarization Transitions
A helical antenna consists of a conducting wire wound in the form of a helix and backed by a ground plane. Depending on the ratio of the helix dimensions (diameter and pitch spacing) to the operating wavelength, the antenna exhibits distinct physical behaviors:
1. **Normal Mode (Broadside):** When the helix diameter and spacing are much smaller than a wavelength ($D \ll \lambda$, $S \ll \lambda$), the phase of the current is nearly uniform across the structure. The radiation pattern is omnidirectional in the plane perpendicular to the helix axis. The helix behaves as a superposition of short vertical dipoles (axial current) and small loops (circular current). Under a specific geometry, the orthogonal fields from these components are in phase quadrature and equal in magnitude, yielding circular polarization perpendicular to the axis.
2. **Axial Mode (Endfire):** When the circumference of the helix is comparable to the wavelength ($C \approx \lambda$), the current along the wire behaves as a traveling wave. The radiation pattern transitions from broadside to a highly directive beam along the axis of the helix (endfire). The fields radiated by the loops and dipoles add constructively in the axial direction, producing a circularly polarized beam with high gain and broad bandwidth.

---

## 2. Formal Definitions and Models

### 2.1 Single-Wire Traveling Wave Antenna (Long Wire)
A long-wire traveling wave antenna consists of a thin, straight wire of physical length $L$ aligned along the $z$-axis ($0 \le z' \le L$), terminated with a matched load at $z' = L$.

```
   Feed                                          Termination
    (o)==============================================[ R_L ]====_|_
   z' = 0                   Wire Length L                   z' = L  ///
```

#### 2.1.1 Current Distribution
Assuming a lossless wire in free space, the unidirectional current distribution $I(z')$ is modeled as:
$$
I(z') = I_0 e^{-jkz'} \quad (0 \le z' \le L)
$$
where:
- $I_0$ is the current amplitude at the feedpoint ($z' = 0$),
- $k = \frac{2\pi}{\lambda}$ is the free-space wavenumber,
- $z'$ is the position along the wire.

#### 2.1.2 Far-Zone Radiation Fields
The vector potential $A_z$ in the far-zone ($r \gg L$) is:
$$
A_z \approx \mu \frac{e^{-jkr}}{4\pi r} \int_{0}^{L} I(z') e^{jkz'\cos\theta} \, dz'
$$
where $\theta$ is the angle relative to the $+z$ axis. Substituting the current distribution:
$$
A_z \approx \mu I_0 \frac{e^{-jkr}}{4\pi r} \int_{0}^{L} e^{-jkz'(1-\cos\theta)} \, dz'
$$
Evaluating the integral:
$$
\int_{0}^{L} e^{-jkz'(1-\cos\theta)} \, dz' = L e^{-j\frac{kL}{2}(1-\cos\theta)} \left[ \frac{\sin\left(\frac{kL}{2}(1-\cos\theta)\right)}{\frac{kL}{2}(1-\cos\theta)} \right]
$$
The far-zone electric field $E_\theta$ is related to $A_z$ by $E_\theta \approx j\omega A_\theta = -j\omega A_z \sin\theta$. Substituting $\omega \mu = k \eta$:
$$
E_\theta \approx j\eta I_0 \frac{e^{-jkr}}{2\pi r} e^{-j\psi_0} \left[ \frac{\sin\theta}{1 - \cos\theta} \sin\left(\frac{kL}{2}(1-\cos\theta)\right) \right]
$$
where:
- $\eta \approx 120\pi \; \Omega$ is the intrinsic impedance of free space,
- $\psi_0 = \frac{kL}{2}(1-\cos\theta)$ is the phase term.

The radiation intensity $U(\theta)$ is:
$$
U(\theta) = \frac{r^2}{2\eta} |E_\theta|^2 = \frac{\eta I_0^2}{8\pi^2} \left[ \cot\left(\frac{\theta}{2}\right) \sin\left(\frac{kL}{2}(1-\cos\theta)\right) \right]^2
$$

#### 2.1.3 Angle of Maximum Radiation
The angle of maximum radiation $\theta_{\text{max}}$ with respect to the wire axis is given by:
$$
\theta_{\text{max}} = \arccos\left(1 - \frac{0.371}{L/\lambda}\right)
$$

> **[Supplementary]** For long wires ($L \gg \lambda$), the radiation resistance $R_{\text{rad}}$ can be approximated using:
> $$
> R_{\text{rad}} \approx 60 \left[ \gamma + \ln\left( \frac{4\pi L}{\lambda} \right) \right] \; \Omega
> $$
> where $\gamma \approx 0.5772$ is the Euler-Mascheroni constant.

### 2.2 V Antenna (Traveling Wave)
A traveling-wave V antenna is formed by two long-wire traveling wave antennas arranged in a "V" configuration with an apex angle $2\theta_0$. The arms are fed out-of-phase at the apex and terminated with matched loads at their open ends.

```
                  Arm 1 (Length L)
                 /====================[ R_L ]--_|_
                /                                ///
         Feed  /  Apex Angle 2\theta_0
          (o) <
               \
                \====================[ R_L ]--_|_
                  Arm 2 (Length L)               ///
```

To align the main radiation lobes of both wires constructively along the bisector of the V, the apex half-angle $\theta_0$ is designed to equal the angle of maximum radiation $\theta_{\text{max}}$ of an isolated wire:
$$
\theta_0 = \theta_{\text{max}} = \arccos\left(1 - \frac{0.371}{L/\lambda}\right)
$$
This alignment produces a unidirectional beam along the symmetric axis of the V, with suppressed sidelobes.

### 2.3 Rhombic Antenna
A rhombic antenna consists of four long-wire traveling wave elements of length $L$ arranged in a diamond (rhombus) coplanar shape. One apex is connected to a balanced feedline, while the opposite apex is terminated with a non-inductive resistor $R_L \approx 600 - 800 \; \Omega$ to absorb remaining power and prevent reflections.

```
                           Tilt Angle \psi
                                 /\
                                /  \
              Arm 1 (Length L) /    \ Arm 3 (Length L)
                              /      \
                       Feed  /        \ Termination
                        (o) <          > [ R_L ]
                             \        /
                              \      /
              Arm 2 (Length L) \    / Arm 4 (Length L)
                                \  /
                                 \/
```

#### 2.3.1 Alignment Design in Free Space
The tilt angle $\psi$ (the angle between each wire and the major axis of the rhombus) is designed to align the main lobes of all four wires constructively along the major axis:
$$
\psi = 90^\circ - \theta_{\text{max}} \implies \cos\psi = \sin\theta_{\text{max}}
$$

#### 2.3.2 Design Over Ground Plane
When suspended horizontally at a height $H$ above a ground plane, the vertical radiation pattern is shaped by ground reflection. To align the main lobe with a specific elevation (wave) angle $\Delta$:
- **Optimum Tilt Angle:**
  $$
  \psi = 90^\circ - \Delta
  $$
- **Optimum Height:**
  $$
  H = \frac{\lambda}{4 \sin\Delta}
  $$
- **Optimum Leg Length:**
  $$
  L = \frac{\lambda}{2 \sin^2\Delta}
  $$

### 2.4 Helical Antenna
A helical antenna consists of a conducting wire wound in a helix of diameter $D$ and spacing $S$, backed by a flat ground plane of diameter $D_g \ge 0.8\lambda$.

```
         Helix axis (z-axis)
         |<-------------------- Total length A = N * S ------------------->|
         |   __             __             __             __             __
   Feed (o)-/  \-----------/  \-----------/  \-----------/  \-----------/  \
     ||  | |    |         |    |         |    |         |    |         |    |
   ======|  \__/           \__/           \__/           \__/           \__/
   Ground |<-D->|
   Plane   Diameter D
```

The geometry is defined by:
- **Diameter:** $D$
- **Circumference:** $C = \pi D$
- **Spacing (Pitch):** $S$
- **Pitch Angle ($\alpha$):**
  $$
  \alpha = \tan^{-1}\left(\frac{S}{C}\right) = \tan^{-1}\left(\frac{S}{\pi D}\right)
  $$
- **Number of Turns:** $N$
- **Total Axial Length:** $A = NS$
- **Single-Turn Wire Length ($L_0$):**
  $$
  L_0 = \sqrt{C^2 + S^2}
  $$

#### 2.4.1 Normal Mode ($C \ll \lambda$, $S \ll \lambda$)
In normal mode, the helix is electrically small. The far-zone fields are represented by the superposition of fields from equivalent short dipoles of length $S$ and small loops of diameter $D$.

The electric field components are:
$$
E_\theta = j\eta \frac{k I_0 S e^{-jkr}}{4\pi r} \sin\theta, \quad E_\phi = \eta \frac{k^2 I_0 \pi D^2 e^{-jkr}}{16\pi r} \sin\theta
$$
The axial ratio (AR) of the polarization ellipse is:
$$
\text{AR} = \frac{|E_\theta|}{|E_\phi|} = \frac{2 S \lambda}{\pi^2 D^2} = \frac{2 S \lambda}{C^2}
$$
To achieve circular polarization ($\text{AR} = 1$):
$$
C = \sqrt{2 S \lambda} \implies \pi D = \sqrt{2 S \lambda}
$$
Under this circular polarization condition, the pitch angle $\alpha$ is related to the circumference by:
$$
\tan\alpha = \frac{S}{C} = \frac{C^2 / (2\lambda)}{C} = \frac{C}{2\lambda}
$$

#### 2.4.2 Axial Mode ($0.8\lambda \le C \le 1.2\lambda$)
In axial mode, the helix operates as a traveling wave antenna. Radiation is directed along the helix axis. The empirical Kraus formulas estimate the performance of an axial-mode helix with $12^\circ \le \alpha \le 14^\circ$ and $N \ge 4$:

- **Input Resistance ($R_{\text{in}}$):**
  $$
  R_{\text{in}} \approx 140 \left(\frac{C}{\lambda}\right) \; \Omega
  $$
- **Half-Power Beamwidth (HPBW):**
  $$
  \text{HPBW} \approx \frac{52^\circ}{\left(\frac{C}{\lambda}\right) \sqrt{N\left(\frac{S}{\lambda}\right)}}
  $$
- **First-Null Beamwidth (FNBW):**
  $$
  \text{FNBW} \approx \frac{115^\circ}{\left(\frac{C}{\lambda}\right) \sqrt{N\left(\frac{S}{\lambda}\right)}}
  $$
- **Directivity ($D_0$):**
  $$
  D_0 \approx 15 N \left(\frac{C}{\lambda}\right)^2 \left(\frac{S}{\lambda}\right)
  $$
- **Axial Ratio (AR):**
  $$
  \text{AR} \approx \frac{2N+1}{2N}
  $$

### 2.5 Yagi-Uda Array
A Yagi-Uda array is a directive parasitic linear array. It consists of a single driven element (usually a half-wave folded dipole) and several parasitic elements (one reflector and one or more directors) aligned parallel to each other.

```
       Reflector        Driven Element        Director 1        Director 2
           |                 ||                   |                 |
           |                 ||                   |                 |
           |                 (o) Feed             |                 |
           |                 ||                   |                 |
           |<--- S_rd ------>|<----- S_dd ------->|<---- S_dd ----->|
         L_r \approx 0.50\lambda  L_d \approx 0.47\lambda  L_dir1 \approx 0.44\lambda  L_dir2 \approx 0.43\lambda
```

#### 2.5.1 Element Roles and Reactances
- **Driven Element ($L_d \approx 0.45\lambda - 0.49\lambda$):** Fed directly, acting as the primary source of electromagnetic energy.
- **Reflector ($L_r \approx 0.50\lambda$):** Slightly longer than the driven element, making its input impedance inductive. The induced current lags the excitation phase, reflecting the wave back toward the driven element. Typically placed at a spacing of $S_{rd} \approx 0.15\lambda - 0.25\lambda$.
- **Directors ($L_{\text{dir}} \approx 0.40\lambda - 0.45\lambda$):** Slightly shorter than the driven element, making their input impedances capacitive. The induced currents lead the excitation phase, focusing the radiation forward. Typically spaced at $S_{dd} \approx 0.15\lambda - 0.40\lambda$.

---

## 3. Key Parameters and Constraints

### Table 1: Design Parameters of Traveling Wave and Broadband Antennas

| Parameter | Symbol | Typical Range | Units | Operational Impact |
| :--- | :--- | :--- | :--- | :--- |
| Long-wire length | $L$ | $2\lambda$ to $10\lambda$ | meters | Determines directivity, gain, and beam tilt angle $\theta_{\text{max}}$ |
| Termination resistance | $R_L$ | $600$ to $800$ | ohms | Absorbs reflected wave to maintain traveling wave mode |
| Rhombic tilt angle | $\psi$ | $40^\circ$ to $75^\circ$ | degrees | Aligns individual wire lobes along the major rhombic axis |
| Helical pitch angle | $\alpha$ | $12^\circ$ to $14^\circ$ | degrees | Establishes axial mode operation and circular polarization |
| Helical circumference | $C$ | $0.8\lambda$ to $1.2\lambda$ | meters | Controls input resistance and spatial mode transition |
| Parasitic spacing | $S_{rd}, S_{dd}$ | $0.15\lambda$ to $0.4\lambda$ | meters | Determines mutual coupling, front-to-back ratio, and gain |

### Table 2: Comparative Summary of Antenna Configurations

| Antenna Type | Bandwidth (VSWR < 2) | Polarization | Directivity | Main Advantage | Key Disadvantage |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Long Wire** | Moderate (2:1) | Linear | Moderate | Simple construction | High sidelobes |
| **V Antenna** | Moderate (2:1) | Linear | High | Directive beam along bisector | Requires balanced termination |
| **Rhombic** | Very Broad (5:1) | Linear | Very High | Excellent HF ionospheric match | Large physical footprint; $50\%$ loss in termination |
| **Helical (Normal)** | Narrow ($5\%$) | Circular | Low | Electrically small | Low radiation efficiency |
| **Helical (Axial)** | Broad ($2:1$) | Circular | High | Circular polarization; high gain | High wind loading profile |
| **Yagi-Uda** | Narrow ($5\% - 10\%$) | Linear | High | High gain-to-size ratio | Frequency sensitive; narrow band |

---

## 4. Step-by-Step Mechanism

### 4.1 Radiation Mechanism of a Traveling Wave Wire
The process by which a straight terminated wire radiates a directive beam is described as follows:

1. **Excitation:** A high-frequency signal is applied at the feedpoint ($z' = 0$). An electromagnetic wave propagates along the wire with phase velocity $v \approx c$.
2. **Phase Matching:** The phase along the wire varies as $e^{-jkz'}$. At a far-field point at angle $\theta$ relative to the wire axis, the path length difference introduces a phase shift $e^{jkz'\cos\theta}$.
3. **Coherent Integration:** The total electric field is the sum of radiation from all incremental elements $dz'$. The differential phase between adjacent elements is:
   $$
   d\Phi = -k \, dz' + k \, dz' \cos\theta = -k \, dz' (1 - \cos\theta)
   $$
4. **Main Lobe Formation:** When $d\Phi = 0$ (at $\theta = 0$), the fields would add in-phase, but the dipole element factor $\sin\theta$ goes to zero at $\theta = 0$. This forces the radiation to zero along the wire axis. The vector sum of the fields peaks at an angle $\theta_{\text{max}}$ where the phase difference over the wire length accumulates to approximately $0.371\lambda$, leading to constructive interference.
5. **Termination Absorption:** The wave reaches the far end ($z' = L$) and is completely absorbed by the matching resistor $R_L$, preventing a backward standing wave.

### 4.2 Mode Transition in Helical Antennas
The transition of a helix from normal mode to axial mode occurs through the following steps as frequency increases:

1. **Low Frequency ($C \ll \lambda$):** The current is nearly uniform and in-phase across the helical turns. Radiation is dominated by the axial dipole moment (vertical polarization) and loop moment (horizontal polarization), adding to form a broadside omnidirectional pattern.
2. **Frequency Increase ($C \to 0.8\lambda$):** The electrical length of each turn approaches one wavelength. The current along the helix wire can no longer be assumed in-phase. The phase delay along the helix wire matches the spatial path delay along the helix axis:
   $$
   k_0 L_0 \approx k_z S + 2\pi m \quad \text{[Supplementary]}
   $$
   where $k_z$ is the axial phase constant.
3. **Axial Alignment:** The outgoing fields from successive turns add in-phase along the helix axis (z-axis), creating an endfire beam.
4. **Polarization Circularity:** Since the current rotates as it travels along the helix, the radiated electric field components $E_x$ and $E_y$ maintain a $90^\circ$ phase difference and equal magnitude in the axial direction, resulting in circular polarization.

---

## 5. Connections and Cross-References

- **Section 2 (Fundamental Parameters):** The directivity $D_0$, input resistance $R_{\text{in}}$, and axial ratio (AR) formulas developed here map directly to the general antenna definitions in Section 2.
- **Section 4 (Linear Wire Antennas):** The single-wire traveling wave analysis uses the same vector potential integration method introduced in Section 4, but replaces the standing-wave current distribution ($I(z') = I_0 \sin[k(L-z')] $) with a traveling-wave distribution ($I(z') = I_0 e^{-jkz'}$).
- **Section 6 (Arrays):** The Yagi-Uda array and V-antenna are analyzed by treating their elements as an array of line sources, utilizing the array factor principles developed in Section 6.
- **Section 11 (Frequency Independent Antennas):** The broadband, self-scaling concepts of traveling-wave structures serve as a prerequisite for understanding the frequency-independent log-periodic and spiral antennas.

*Prerequisite: Section 2 (Fundamental Parameters) — understanding of polarization, directivity, and VSWR. Section 4 (Linear Wire Antennas) — far-field integration techniques.*

---

## Solved Exercises

### Exercise 1: Angle of Maximum Radiation for a Long Wire
**Problem:** A single-wire traveling-wave antenna of length $L = 5\lambda$ is placed in free space. Calculate the angle of maximum radiation $\theta_{\text{max}}$ with respect to the wire axis.

**Solution:**

#### Step 1: Identify the formula
The angle of maximum radiation for a terminated long-wire antenna is:
$$
\theta_{\text{max}} = \arccos\left(1 - \frac{0.371}{L/\lambda}\right)
$$

#### Step 2: Substitute the electrical length
Given $L/\lambda = 5$:
$$
\cos\theta_{\text{max}} = 1 - \frac{0.371}{5}
$$
$$
\cos\theta_{\text{max}} = 1 - 0.0742 = 0.9258
$$

#### Step 3: Compute the angle
$$
\theta_{\text{max}} = \arccos(0.9258) \approx 22.21^\circ
$$

> **[Supplementary]** We can verify this using the small-angle approximation for long wires, $\theta_{\text{max}} \approx \sqrt{\frac{0.742}{L/\lambda}}$:
> $$
> \theta_{\text{max, approx}} \approx \sqrt{\frac{0.742}{5}} = \sqrt{0.1484} \approx 0.3852 \text{ rad} \approx 22.07^\circ
> $$
> The two methods differ by only $0.14^\circ$, validating the calculation.

---

### Exercise 2: Apex Angle of a Traveling-Wave V Antenna
**Problem:** A traveling-wave V antenna operating in free space is constructed from two wire arms of length $L = 6\lambda$ each. 
1. Determine the angle of maximum radiation $\theta_{\text{max}}$ for an individual arm.
2. Calculate the optimum apex angle $2\theta_0$ of the V antenna to align the main lobes along the bisecting axis.

**Solution:**

#### Step 1: Calculate the single-wire lobe angle
For a wire of length $L/\lambda = 6$:
$$
\cos\theta_{\text{max}} = 1 - \frac{0.371}{6}
$$
$$
\cos\theta_{\text{max}} = 1 - 0.061833 = 0.938167
$$
$$
\theta_{\text{max}} = \arccos(0.938167) \approx 20.25^\circ
$$

#### Step 2: Determine the optimum half-apex angle $\theta_0$
For optimum alignment, the half-apex angle must match the single-wire maximum angle:
$$
\theta_0 = \theta_{\text{max}} = 20.25^\circ
$$

#### Step 3: Compute the total apex angle $2\theta_0$
$$
2\theta_0 = 2 \times 20.25^\circ = 40.50^\circ
$$

---

### Exercise 3: Rhombic Antenna Optimum Design Over Ground
**Problem:** Design a horizontal rhombic antenna operating in free space at $f = 15$ MHz for ionospheric propagation with a desired elevation (wave) angle $\Delta = 18^\circ$ above the ground plane.
1. Calculate the optimum tilt angle $\psi$.
2. Calculate the optimum leg length $L$ in meters.
3. Calculate the optimum height $H$ of the antenna above ground in meters.

**Solution:**

#### Step 1: Find the wavelength
At $f = 15$ MHz ($15 \times 10^6$ Hz):
$$
\lambda = \frac{c}{f} = \frac{3 \times 10^8 \text{ m/s}}{15 \times 10^6 \text{ Hz}} = 20.0 \text{ meters}
$$

#### Step 2: Calculate the optimum tilt angle $\psi$
$$
\psi = 90^\circ - \Delta = 90^\circ - 18^\circ = 72.0^\circ
$$

#### Step 3: Calculate the optimum leg length $L$
The formula for optimum leg length is:
$$
L = \frac{\lambda}{2 \sin^2\Delta}
$$
First compute $\sin(18^\circ)$:
$$
\sin(18^\circ) \approx 0.309017 \implies \sin^2(18^\circ) \approx 0.095492
$$
Substitute into the formula:
$$
L = \frac{20.0}{2 \times 0.095492} = \frac{20.0}{0.190984} \approx 104.72 \text{ meters}
$$

#### Step 4: Calculate the optimum height $H$
The formula for optimum height is:
$$
H = \frac{\lambda}{4 \sin\Delta}
$$
Substitute the values:
$$
H = \frac{20.0}{4 \times 0.309017} = \frac{20.0}{1.236068} \approx 16.18 \text{ meters}
$$

---

### Exercise 4: Performance of an Axial-Mode Helical Antenna
**Problem:** An axial-mode helical antenna is designed for Wi-Fi communication at $f = 2.45$ GHz with $N = 8$ turns, a circumference $C = 1.05\lambda$, and a pitch angle $\alpha = 12.5^\circ$.
1. Compute the operating wavelength $\lambda$ in millimeters.
2. Determine the spacing $S$ between turns in millimeters.
3. Calculate the input resistance $R_{\text{in}}$.
4. Calculate the Half-Power Beamwidth (HPBW) and First-Null Beamwidth (FNBW) in degrees.
5. Compute the directivity $D_0$ in dimensionless units and in dB.
6. Find the axial ratio (AR).

**Solution:**

#### Step 1: Compute the operating wavelength
$$
\lambda = \frac{3 \times 10^8 \text{ m/s}}{2.45 \times 10^9 \text{ Hz}} = 0.122449 \text{ m} = 122.45 \text{ mm}
$$

#### Step 2: Calculate the spacing $S$
Using $S = C \tan\alpha$:
$$
C = 1.05\lambda = 1.05 \times 122.45 \text{ mm} = 128.57 \text{ mm}
$$
$$
S = 128.57 \text{ mm} \times \tan(12.5^\circ)
$$
Calculate the tangent:
$$
\tan(12.5^\circ) \approx 0.221695
$$
$$
S = 128.57 \text{ mm} \times 0.221695 \approx 28.50 \text{ mm}
$$
Normalized spacing:
$$
\frac{S}{\lambda} = \frac{28.50 \text{ mm}}{122.45 \text{ mm}} \approx 0.2328
$$

#### Step 3: Calculate the input resistance $R_{\text{in}}$
$$
R_{\text{in}} \approx 140 \left(\frac{C}{\lambda}\right) = 140 \times 1.05 = 147.0 \; \Omega
$$

#### Step 4: Calculate the beamwidths
- **Half-Power Beamwidth (HPBW):**
  $$
  \text{HPBW} \approx \frac{52^\circ}{\left(\frac{C}{\lambda}\right) \sqrt{N\left(\frac{S}{\lambda}\right)}}
  $$
  Evaluate the denominator term:
  $$
  \sqrt{N\left(\frac{S}{\lambda}\right)} = \sqrt{8 \times 0.2328} = \sqrt{1.8624} \approx 1.3647
  $$
  $$
  \text{HPBW} \approx \frac{52^\circ}{1.05 \times 1.3647} = \frac{52^\circ}{1.4329} \approx 36.29^\circ
  $$
- **First-Null Beamwidth (FNBW):**
  $$
  \text{FNBW} \approx \frac{115^\circ}{\left(\frac{C}{\lambda}\right) \sqrt{N\left(\frac{S}{\lambda}\right)}} = \frac{115^\circ}{1.4329} \approx 80.26^\circ
  $$

#### Step 5: Compute the directivity $D_0$
$$
D_0 \approx 15 N \left(\frac{C}{\lambda}\right)^2 \left(\frac{S}{\lambda}\right)
$$
$$
D_0 \approx 15 \times 8 \times (1.05)^2 \times 0.2328
$$
$$
D_0 \approx 120 \times 1.1025 \times 0.2328 \approx 30.80
$$
In decibels relative to isotropic (dBi):
$$
D_{\text{dB}} = 10 \log_{10}(30.80) \approx 14.89 \text{ dBi}
$$

#### Step 6: Find the axial ratio (AR)
$$
\text{AR} \approx \frac{2N+1}{2N} = \frac{2(8)+1}{2(8)} = \frac{17}{16} = 1.0625 \text{ (or } 0.53 \text{ dB)}
$$

---

### Exercise 5: Normal Mode Circular Polarization Design
**Problem:** A normal-mode helical antenna is to be designed to produce circular polarization at $f = 433$ MHz. The helix diameter is chosen as $D = 2.0$ cm.
1. Find the wavelength $\lambda$.
2. Compute the required spacing $S$ between turns.
3. Compute the resulting pitch angle $\alpha$.
4. Verify that the helix dimensions satisfy the electrically small assumption ($C \ll \lambda$ and $S \ll \lambda$).

**Solution:**

#### Step 1: Compute the wavelength
$$
\lambda = \frac{c}{f} = \frac{3 \times 10^8 \text{ m/s}}{4.33 \times 10^8 \text{ Hz}} \approx 0.6928 \text{ m} = 69.28 \text{ cm}
$$

#### Step 2: Calculate the circumference and spacing
$$
C = \pi D = \pi \times 2.0 \text{ cm} \approx 6.2832 \text{ cm}
$$
The circular polarization condition is:
$$
C = \sqrt{2 S \lambda} \implies C^2 = 2 S \lambda \implies S = \frac{C^2}{2\lambda}
$$
Substitute the values:
$$
S = \frac{(6.2832)^2}{2 \times 69.28} = \frac{39.4786}{138.56} \approx 0.2849 \text{ cm} = 2.85 \text{ mm}
$$

#### Step 3: Compute the pitch angle $\alpha$
$$
\alpha = \tan^{-1}\left(\frac{S}{C}\right) = \tan^{-1}\left(\frac{0.2849}{6.2832}\right) = \tan^{-1}(0.04534) \approx 2.59^\circ
$$

#### Step 4: Verify the assumptions
Check the normalized dimensions:
$$
\frac{C}{\lambda} = \frac{6.2832}{69.28} \approx 0.0907 \ll 1
$$
$$
\frac{S}{\lambda} = \frac{0.2849}{69.28} \approx 0.00411 \ll 1
$$
Since both $C < 0.1\lambda$ and $S < 0.1\lambda$, the normal mode approximations are valid.

---

### Exercise 6: Yagi-Uda Array Design Calculations
**Problem:** A 3-element Yagi-Uda antenna is designed for operation in the FM band at $f = 100$ MHz. The array contains a reflector, a folded dipole driven element, and one director.
1. Calculate the wavelength $\lambda$.
2. Determine typical physical lengths for the reflector, folded dipole driven element, and director using standard design parameters.
3. If the reflector-to-driver spacing is $0.2\lambda$ and the driver-to-director spacing is $0.15\lambda$, calculate the overall length of the boom in meters.
4. Estimate the input impedance of the array at resonance, assuming the mutual coupling effects result in a single isolated dipole impedance of $Z_d \approx 70 + j0 \; \Omega$, and the folded dipole has equal conductor radii.

**Solution:**

#### Step 1: Compute the wavelength
$$
\lambda = \frac{c}{f} = \frac{3 \times 10^8 \text{ m/s}}{100 \times 10^6 \text{ Hz}} = 3.0 \text{ meters}
$$

#### Step 2: Determine element lengths
Using typical design coefficients:
- **Reflector ($L_r \approx 0.50\lambda$):**
  $$
  L_r = 0.50 \times 3.0 \text{ m} = 1.50 \text{ m}
  $$
- **Driven Element ($L_d \approx 0.47\lambda$):**
  $$
  L_d = 0.47 \times 3.0 \text{ m} = 1.41 \text{ m}
  $$
- **Director ($L_{\text{dir}} \approx 0.44\lambda$):**
  $$
  L_{\text{dir}} = 0.44 \times 3.0 \text{ m} = 1.32 \text{ m}
  $$

#### Step 3: Compute the boom length
The spacings between the elements are:
$$
S_{rd} = 0.2 \times 3.0 \text{ m} = 0.60 \text{ m}
$$
$$
S_{dd} = 0.15 \times 3.0 \text{ m} = 0.45 \text{ m}
$$
The total length of the boom is the sum of these spacings:
$$
L_{\text{boom}} = S_{rd} + S_{dd} = 0.60 + 0.45 = 1.05 \text{ meters}
$$

#### Step 4: Calculate the input impedance
For a folded dipole with equal conductor radii, the impedance step-up ratio is:
$$
(1 + \alpha)^2 = 2^2 = 4
$$
With the isolated dipole impedance $Z_d = 70 \; \Omega$, the stepped-up input impedance is:
$$
Z_{\text{in}} \approx 4 \times Z_d = 4 \times 70 \; \Omega = 280 \; \Omega
$$

---

## Exam Tip: Traveling Wave and Helical Antennas

When solving exam problems on traveling-wave and broadband antennas, watch out for these common pitfalls and patterns:

1. **Traveling Wave Main Lobe Offset:** The radiation lobe of a traveling wave single-wire antenna is NEVER along the axis of the wire ($\theta = 0$) due to the element factor $\sin\theta = 0$. It is always tilted at an angle $\theta_{\text{max}}$. Do not confuse the axial direction of the current flow with the direction of maximum radiation.
2. **Rhombic Antenna Ground Height:** Make sure to note whether the rhombic antenna is in free space or suspended over a ground plane. In free space, the tilt angle matches the single-wire lobe angle ($\psi = 90^\circ - \theta_{\text{max}}$). Over ground, it is designed in conjunction with height to match a desired ground elevation angle $\Delta$.
3. **Helical Normal Mode Circular Polarization:** Circular polarization in the normal mode is highly sensitive to the geometry. The condition is $C = \sqrt{2 S \lambda}$. If the frequency changes, the antenna will lose its circular polarization and become elliptically polarized, since $\lambda$ changes.
4. **Helical Axial Mode Input Resistance:** The input resistance of an axial-mode helix is purely real and estimated as $R_{\text{in}} \approx 140 (C/\lambda) \; \Omega$. Notice that this does NOT depend on the number of turns $N$. Adding turns increases directivity and decreases beamwidth, but leaves the input resistance virtually unchanged.
5. **Yagi-Uda Reactances:** Directors are always shorter than the resonant length (capacitive reactance, directing the wave forward), while reflectors are always longer (inductive reactance, reflecting the wave back).
