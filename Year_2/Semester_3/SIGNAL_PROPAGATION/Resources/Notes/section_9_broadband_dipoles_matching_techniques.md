# Broadband Dipoles and Matching Techniques

While thin resonant dipoles are widely used due to their simplicity and low cost, they exhibit a narrow bandwidth (typically a few percent), which limits their applicability in modern wideband communication systems. The narrow bandwidth of thin dipoles is due to the rapid variation of their input reactance near resonance as a function of frequency. To overcome this limitation, broadband dipoles are designed to maintain a stable input impedance and radiation pattern over a wide frequency range. This is achieved by increasing the volume-to-length ratio of the antenna, utilizing self-scaling geometries, or implementing dedicated impedance matching networks. This section covers the theoretical foundations and design principles of biconical antennas, triangular sheet and bow-tie dipoles, cylindrical dipoles, folded dipoles, discones, conical skirt monopoles, and key impedance matching techniques.

---

## 1. Conceptual Foundation

### 1.1 The Bandwidth Limitation of Thin Dipoles

For a thin cylindrical dipole of length $L$ and radius $a$, the input impedance $Z_{\text{in}} = R_{\text{in}} + jX_{\text{in}}$ is highly sensitive to changes in frequency. Near the first resonance ($L \approx 0.5\lambda$), the input resistance $R_{\text{in}}$ increases gradually with frequency, while the input reactance $X_{\text{in}}$ changes rapidly from capacitive ($X_{\text{in}} < 0$ for $L < 0.48\lambda$) to inductive ($X_{\text{in}} > 0$ for $L > 0.48\lambda$). 

The rate of change of reactance with respect to frequency, $\partial X_{\text{in}}/\partial f$, is inversely proportional to the wire radius $a$. For thin wires, this derivative is very large, meaning that a small deviation from the resonant frequency introduces a large mismatch between the antenna and the transmission line. This mismatch increases the voltage standing wave ratio (VSWR) and limits the operational bandwidth of the antenna.

### 1.2 Broadbanding Strategies

To increase the bandwidth of a dipole-like antenna, three primary physical mechanisms can be exploited:

1. **Volume Expansion:** By increasing the transverse dimensions of the antenna (such as using a thick cylinder or a cone), the characteristic impedance of the antenna structure as a transmission line is lowered. This reduces the amplitude of the internal reflections from the antenna ends, damping the resonant behavior and smoothing the impedance variation over frequency.
2. **Angle-Defined (Self-Scaling) Geometries:** If an antenna's shape is defined entirely by angles rather than absolute linear dimensions, its electrical properties (impedance and pattern) remain constant with frequency. The infinite biconical antenna is the classic example of an angle-defined structure. Finite structures approximate this behavior above a lower cutoff frequency determined by their physical size.
3. **Impedance Matching Networks:** Passive circuits (such as baluns, stubs, and lumped-element networks) can transform the varying antenna impedance to match the characteristic impedance of the feedline over a specified band.

### 1.3 Broadband vs. Narrowband Antenna Characteristics

| Property | Narrowband Dipole (Thin Wire) | Broadband Dipole (Thick/Conical) |
| :--- | :--- | :--- |
| **Impedance Variation** | Rapid variation in reactance; sharp resonance peaks | Smooth variation in reactance; broad, shallow peaks |
| **Bandwidth (VSWR < 2)** | $2\% - 5\%$ | $20\% - 200\%+$ (several octaves for discones) |
| **Radiation Pattern** | Stable near resonance; splits into multi-lobe patterns at higher harmonics | Remains relatively stable over a wider frequency range |
| **Current Distribution** | Primarily standing wave (sinusoidal) | Combination of standing wave and traveling wave |
| **Physical Profile** | Lightweight, low wind resistance | Bulkier, higher wind resistance |

> **[Key Insight]** The transition from a narrowband standing-wave antenna to a broadband antenna is physically a transition from a highly reflective structure (which stores energy and exhibits high $Q$) to a guided-wave structure that smoothly releases energy into space (low $Q$).

---

## 2. Formal Definitions and Models

### 2.1 The Biconical Antenna

The biconical antenna consists of two collinear cones with their vertices facing each other, fed by a source at the junction. It serves as the analytical baseline for broadband antennas.

#### 2.1.1 The Infinite Biconical Antenna (TEM Wave Model)

An infinite biconical antenna consists of two infinite cones with half-cone angle $\theta_0$. Because the geometry is infinite and defined only by the angle $\theta$, it supports a pure spherical Transverse Electromagnetic (TEM) wave. The electric and magnetic fields in spherical coordinates $(r, \theta, \phi)$ are given by:

$$
E_\theta(r, \theta) = \frac{V_0 e^{-jkr}}{r \sin\theta \ln\left[\cot\left(\frac{\theta_0}{2}\right)\right]}
$$

$$
H_\phi(r, \theta) = \frac{V_0 e^{-jkr}}{\eta r \sin\theta \ln\left[\cot\left(\frac{\theta_0}{2}\right)\right]}
$$

where $V_0$ is the voltage amplitude of the source, $k = 2\pi/\lambda$ is the wavenumber, and $\eta = \sqrt{\mu/\epsilon} \approx 120\pi \; \Omega$ is the intrinsic impedance of the medium.

To find the voltage $V(r)$ and current $I(r)$ along the cones:

$$
V(r) = \int_{\theta_0}^{\pi - \theta_0} E_\theta(r, \theta) r \, d\theta = 2 V_0 e^{-jkr}
$$

$$
I(r) = \int_0^{2\pi} H_\phi(r, \theta) r \sin\theta \, d\phi = \frac{2\pi V_0 e^{-jkr}}{\eta \ln\left[\cot\left(\frac{\theta_0}{2}\right)\right]}
$$

The characteristic impedance $Z_c$ of the conical transmission line is the ratio of $V(r)$ to $I(r)$:

$$
Z_c = \frac{\eta}{\pi} \ln\left[\cot\left(\frac{\theta_0}{2}\right)\right] \approx 120 \ln\left[\cot\left(\frac{\theta_0}{2}\right)\right] \; \Omega
$$

Since the structure is infinite, there are no reflections, and the input impedance is purely real and equal to the characteristic impedance:

$$
Z_{\text{in}} = Z_c
$$

#### 2.1.2 The Finite Biconical Antenna

A finite biconical antenna has cones of length $l = L/2$. At the boundary sphere of radius $r = l$, the cones terminate abruptly, creating a discontinuity. This boundary separates the space into two regions:
- **Region I (Antenna Region, $r < l$):** Supports the principal TEM mode traveling outward, plus reflected TEM modes and an infinite set of higher-order spherical TM modes ($TM_{n}$ for odd $n$) that represent the localized reactive energy.
- **Region II (Free Space, $r > l$):** Supports only outgoing spherical TM modes ($TM_{n}$ for odd $n$) that represent radiation.

Applying boundary conditions (continuity of tangential fields at $r = l$) yields the input impedance. Schelkunoff approximated this using an equivalent transmission line model:

$$
Z_{\text{in}} = Z_c \frac{Z_L + j Z_c \tan(kl)}{Z_c + j Z_L \tan(kl)}
$$

where $Z_L = R_L + jX_L$ is the equivalent terminal load impedance representing the transition to free space at the boundary sphere:

$$
Z_L = \frac{Z_c^2}{Z_a}
$$

where $Z_a$ is the radiation impedance referred to the terminal sphere. For small cone angles, $Z_L$ is high, leading to significant reflections and resonant behavior. For large cone angles ($\theta_0 > 30^\circ$), $Z_c$ is low, $Z_L$ is close to $Z_c$, and reflections are minimized, leading to a broadband response.

### 2.2 Triangular Sheet, Bow-Tie, and Wire Simulation

#### 2.2.1 Triangular Sheet and Bow-Tie Antennas

The biconical antenna is difficult to fabricate due to its three-dimensional structure. The **bow-tie antenna** is a planar, two-dimensional approximation of the bicone, made of two triangular sheets of metal. While the planar geometry does not support a pure TEM mode, it maintains a wide bandwidth due to the tapered geometry.

The input impedance is determined primarily by the flare angle $\theta_{\text{flare}}$ and the length $L$. A wider flare angle decreases the input resistance and reactance variations, yielding a broader bandwidth.

#### 2.2.2 Wire Simulation

Solid metal sheets are susceptible to wind loading and are heavy. To mitigate this, the solid sheets are simulated using a grid of thin wires (wire simulation). 

The boundary condition that the tangential electric field must vanish is approximated by enforcing it on the grid of wires. For a wire grid to accurately simulate a solid sheet, the spacing between adjacent parallel wires $s$ must satisfy:

$$
s < 0.1\lambda
$$

at the highest operating frequency.

### 2.3 The Cylindrical Dipole

The cylindrical dipole consists of two collinear hollow or solid cylinders of length $L$ and radius $a$. 

#### 2.3.1 Equivalent Radius of Non-Cylindrical Conductors

To analyze antennas with non-circular cross-sections (e.g., flat strips or polygonal wires) using wire-based analytical models, the concept of an **equivalent radius** $a_{\text{eq}}$ is defined. The equivalent radius is the radius of a circular cylinder that exhibits the same electrostatic capacitance per unit length as the non-circular conductor.

For a flat strip of width $w$:

$$
a_{\text{eq}} \approx \frac{w}{4} = 0.25w
$$

For a square conductor of side length $s$:

$$
a_{\text{eq}} \approx 0.59s
$$

For a triangular conductor of side length $s$:

$$
a_{\text{eq}} \approx 0.42s
$$

#### 2.3.2 Impedance Bandwidth and Resonance of Cylindrical Dipoles

As the radius $a$ of a cylindrical dipole increases:
1. **Resonant length decreases:** The self-inductance per unit length decreases while the self-capacitance per unit length increases. This slows down the phase velocity of the wave on the wire, shortening the physical length required for resonance ($L_{\text{res}} < 0.5\lambda$, typically $L_{\text{res}} \approx 0.45\lambda$ to $0.48\lambda$).
2. **Bandwidth increases:** The rate of change of input reactance with frequency $\partial X_{\text{in}}/\partial f$ decreases, widening the frequency range over which the VSWR remains below a target threshold (typically VSWR $< 2$).

### 2.4 The Folded Dipole

A folded dipole consists of two parallel dipoles of length $L \approx \lambda/2$ spaced a distance $s$ apart ($s \ll \lambda$), joined at their outer ends. One dipole is fed at the center, while the other is continuous.

#### 2.4.1 Mode Decomposition

The operation of a folded dipole is analyzed by decomposing its current into two orthogonal modes:
1. **Antenna Mode (Even Mode / Common Mode):** The voltages applied to both conductors are equal and in phase. The currents flow in the same direction, and the structure behaves as a single thick dipole with an equivalent radius.
2. **Transmission-Line Mode (Odd Mode / Differential Mode):** The voltages applied are equal and out of phase. The currents flow in opposite directions, acting as a short-circuited transmission line of length $l = L/2 = \lambda/4$.

#### 2.4.2 Impedance Transformation and Step-Up Ratio

For two parallel conductors with unequal radii ($a_1$ for the driven arm and $a_2$ for the folded arm) and center-to-center spacing $s$:

The current division factor $\alpha$ is given by:

$$
\alpha = \frac{\cosh^{-1}\left(\frac{s^2 + a_1^2 - a_2^2}{2 s a_1}\right)}{\cosh^{-1}\left(\frac{s^2 - a_1^2 + a_2^2}{2 s a_2}\right)} \approx \frac{\ln(s/a_1)}{\ln(s/a_2)}
$$

The input impedance $Z_{\text{in}}$ of the folded dipole is:

$$
Z_{\text{in}} = (1 + \alpha)^2 Z_d
$$

where $Z_d$ is the input impedance of a standard single-wire dipole of the same length and equivalent radius.
- For equal radii ($a_1 = a_2$), the current division factor is $\alpha = 1$. The step-up ratio is:

$$
(1 + \alpha)^2 = 2^2 = 4
$$

yielding an input impedance of $Z_{\text{in}} \approx 4(73 + j42.5) \approx 292 + j170 \; \Omega$.
- At resonance, the reactive component is tuned out, yielding $Z_{\text{in}} \approx 292 \; \Omega$ (commonly matched to $300 \; \Omega$ twin-lead lines).

### 2.5 Discone and Conical Skirt Monopole

#### 2.5.1 Discone Antenna

The **discone antenna** is a single-ended, vertically polarized broadband radiator. It consists of a horizontal disc mounted above a metal cone. The disc is fed by the inner conductor of a coaxial line, while the outer conductor is connected to the apex of the cone.

It behaves as a high-pass filter:
- Above the lower cutoff frequency, it exhibits an omnidirectional radiation pattern in the horizontal plane and a stable input impedance (typically matched to $50 \; \Omega$).
- The lower cutoff frequency $f_{\text{min}}$ is determined by the slant height $L_v$ of the cone, which must be a quarter-wavelength at $f_{\text{min}}$:

$$
L_v \approx \frac{\lambda_{\text{max}}}{4} \implies f_{\text{min}} = \frac{c}{4 L_v}
$$

#### 2.5.2 Conical Skirt Monopole

The **conical skirt monopole** replaces the flat disc of the discone with a vertical monopole element of length $L_m \approx \lambda/4$. This combination preserves the broadband impedance characteristics while altering the elevation radiation pattern, directing the main beam closer to the horizon at higher frequencies.

---

## 3. Key Parameters and Constraints

### Table 1: Broadband Dipole Design Parameters

| Parameter | Symbol | Typical Range | Units | Operational Impact |
| :--- | :--- | :--- | :--- | :--- |
| Half-cone angle | $\theta_0$ | $1^\circ$ to $45^\circ$ | degrees | Determines characteristic impedance $Z_c$ of biconical line |
| Flare angle | $\theta_{\text{flare}}$ | $30^\circ$ to $90^\circ$ | degrees | Determines input impedance and bandwidth of bow-tie dipoles |
| Wire spacing (Grid) | $s_{\text{grid}}$ | $0.01\lambda$ to $0.1\lambda$ | meters | Wire grid density; must be $< 0.1\lambda$ for sheet simulation |
| Spacing ratio | $s/a$ | $5$ to $50$ | dimensionless | Ratio of spacing to radius in folded dipoles; determines $\alpha$ |
| Cone slant height | $L_v$ | $\approx 0.25\lambda_{\text{max}}$ | meters | Establishes the lower cutoff frequency of discone antennas |
| Disc-to-cone gap | $g$ | $0.005\lambda$ to $0.02\lambda$ | meters | Critical for input matching; determines feedpoint capacitance |

### Table 2: Impedance Matching Network Characteristics

| Matching Technique | Balance State | Insertion Loss | Tuning Degrees of Freedom | Key Constraint / Limitation |
| :--- | :--- | :--- | :--- | :--- |
| **Gamma Match** | Unbalanced-to-Balanced | Very low | 2 (rod length, capacitance) | Introduces asymmetry in radiation pattern |
| **T-Match** | Balanced-to-Balanced | Very low | 2 (rod length, dual capacitors) | Requires symmetrical dual adjustments |
| **Omega Match** | Unbalanced-to-Balanced | Low | 3 (rod length, 2 capacitors) | More complex physical assembly |
| **1:1 Balun** | Unbalanced-to-Balanced | Low to Moderate | 0 (fixed ratio) | Bandwidth limited by core material permeability |
| **4:1 Balun** | Unbalanced-to-Balanced | Low to Moderate | 0 (fixed ratio) | Performs impedance transformation only (e.g., $300 \; \Omega$ to $75 \; \Omega$) |

---

## 4. Step-by-Step Mechanism

### 4.1 Mode Decomposition Analysis of the Folded Dipole

To solve for the input impedance of a folded dipole, the excitation is decomposed into two decoupled modes: the **Antenna Mode** and the **Transmission-Line Mode**.

```
   Folded Dipole Excitation:
      Feed: V_in at left arm center. Right arm is continuous.

      [V_in]  ==>  Antenna Mode (Even)   +   Transmission-Line Mode (Odd)
                     [V_in/2]  [V_in/2]         [V_in/2]  [-V_in/2]
                      |          |                |          |
                      o          o                o          o
                     ( )        ( )              ( )        ( )
                      |          |                |          |
                     [V_in/2]  [V_in/2]        -[V_in/2]  [V_in/2]
```

#### Step 1: Antenna Mode (Even Mode)
- **Excitation:** Equal in-phase voltage sources $V_e = V_{\text{in}}/2$ are applied to both the driven arm and the folded arm.
- **Currents:** The currents flow in the same direction in both arms ($I_{e1}$ and $I_{e2}$). Since the spacing $s \ll \lambda$, the structure radiates as a single thick dipole of equivalent radius $a_{\text{eq}} = \sqrt{a_1 s}$ (for equal radii).
- **Impedance:** The total antenna mode current is $I_e = I_{e1} + I_{e2}$. The input impedance of the equivalent dipole is $Z_d = V_e / I_e$. The currents split according to the conductor geometries:

$$
I_{e1} = \frac{1}{1 + \alpha} I_e, \quad I_{e2} = \frac{\alpha}{1 + \alpha} I_e
$$

#### Step 2: Transmission-Line Mode (Odd Mode)
- **Excitation:** Out-of-phase voltage sources $V_0/2$ are applied to the driven arm, and $-V_0/2$ is applied to the folded arm.
- **Currents:** The currents are equal and opposite, flowing up one arm and down the other ($I_t$ and $-I_t$). No radiation occurs because the fields cancel in the far field ($s \ll \lambda$).
- **Impedance:** The structure acts as a short-circuited transmission line of length $l = L/2$ with characteristic impedance $Z_0$. The input impedance of a short-circuited stub of length $L/2$ is:

$$
Z_t = j Z_0 \tan\left(k \frac{L}{2}\right)
$$

The characteristic impedance of the two-wire line is:

$$
Z_0 = \frac{\eta}{\pi} \cosh^{-1}\left(\frac{s^2 + a_1^2 + a_2^2}{2 a_1 a_2}\right) \approx 120 \ln\left(\frac{s}{\sqrt{a_1 a_2}}\right)
$$

#### Step 3: Synthesis of Input Impedance
The total input current at the feedpoint is the sum of the antenna mode current and the transmission-line mode current:

$$
I_{\text{in}} = I_{e1} + I_t = \frac{V_{\text{in}}/2}{(1 + \alpha)^2 Z_d} + \frac{V_{\text{in}}/2}{2 Z_t}
$$

Rearranging this yields the total input impedance $Z_{\text{in}}$:

$$
Z_{\text{in}} = \frac{V_{\text{in}}}{I_{\text{in}}} = \frac{2 (1+\alpha)^2 Z_d (2 Z_t)}{(1+\alpha)^2 Z_d + 2 Z_t} = \frac{4 (1+\alpha)^2 Z_d Z_t}{(1+\alpha)^2 Z_d + 2 Z_t}
$$

For a half-wavelength dipole ($L = \lambda/2$), the stub length is $\lambda/4$, making $Z_t = j Z_0 \tan(\pi/2) \to \infty$. Taking the limit as $Z_t \to \infty$:

$$
Z_{\text{in}} \approx (1 + \alpha)^2 Z_d
$$

### 4.2 Tuning Mechanism of the Gamma Match

The Gamma match is used to match a coaxial feedline ($50 \; \Omega$) to a balanced dipole element. Tuning involves adjusting the tapping point $l$ and the series capacitance $C$.

```
                       Dipole Element (Radius a)
   ======================+===================================
                         |                    |
                         |<---- Spacing s --->| Gamma Rod (Radius a')
                         |                    +==============
                         |                    |             |
                        _|_                   |          [ C ] Series Cap
                       ///// (Coax Shield)   _|_            |
                                            /////          (o) Coax Center
```

#### Step 1: Impedance Step-Up Adjustment
- **Mechanism:** The Gamma match acts as a parallel transmission line over the length $l$. The current divides between the main dipole and the Gamma rod based on their radii $a, a'$ and spacing $s$.
- **Action:** Move the shorting clamp along the dipole to adjust the tapping length $l$. This adjusts the effective step-up transformation ratio:

$$
N^2 = (1 + \alpha)^2
$$

This steps up the radiation resistance of the dipole ($R_d \approx 73 \; \Omega$ or lower if parasitic elements are present) to match the target resistance:

$$
R_{\text{in}} \approx R_d (1 + \alpha)^2 \sin^2(kl)
$$

#### Step 2: Reactance Cancellation
- **Mechanism:** The matching section introduces an inductive reactance due to the loop formed by the dipole, the shorting clamp, and the Gamma rod. This behaves like a short-circuited stub, adding an inductive component $j X_{\text{stub}}$.
- **Action:** Adjust the variable series capacitor $C$ in series with the Gamma feed point. The capacitive reactance cancels the inductive loop reactance:

$$
X_c = \frac{1}{\omega C} = X_{\text{stub}} \implies C = \frac{1}{\omega X_{\text{stub}}}
$$

This returns the input impedance to a purely real state: $Z_{\text{in}} = R_{\text{in}} \approx 50 \; \Omega$.

---

## 5. Connections and Cross-References

- **Section 2 (Fundamental Parameters):** Impedance matching directly influences return loss, VSWR, mismatch efficiency ($\eta_{\text{reflection}} = 1 - |\Gamma|^2$), and fractional bandwidth.
- **Section 4 (Linear Wire Antennas):** The input impedance of the resonant half-wave dipole ($Z_d \approx 73 + j42.5 \; \Omega$) acts as the load baseline $Z_d$ for folded dipoles and matching networks.
- **Section 6 (Arrays: Linear, Planar, and Circular):** Driven elements in Yagi-Uda arrays have lower input impedances ($10 \; \Omega$ to $30 \; \Omega$) due to mutual coupling. Folded dipoles and Gamma matches are used to step up this low impedance to the standard $50 \; \Omega$ or $75 \; \Omega$ feedlines.
- **Section 11 (Frequency Independent Antennas):** The self-scaling angle-defined biconical and bow-tie concepts are the direct physical precursors to equiangular spiral and log-periodic frequency-independent antennas.

*Prerequisite: Section 2 (Fundamental Parameters) — understanding of VSWR, reflection coefficient, and impedance. Section 4 (Linear Wire Antennas) — dipole radiation characteristics.*

---

## 6. Worked Examples

### Exercise 1: Characteristic Impedance of an Infinite Bicone

**Problem:** Calculate the characteristic impedance $Z_c$ of an infinite biconical antenna in free space ($\eta = 120\pi \; \Omega$) for the following half-cone angles:
1. $\theta_0 = 1^\circ$
2. $\theta_0 = 12^\circ$
3. $\theta_0 = 35^\circ$

**Solution:**

The characteristic impedance of an infinite biconical antenna is given by:

$$
Z_c = \frac{\eta}{\pi} \ln\left[\cot\left(\frac{\theta_0}{2}\right)\right] = 120 \ln\left[\cot\left(\frac{\theta_0}{2}\right)\right]
$$

#### Step 1: Compute for $\theta_0 = 1^\circ$
- Half-angle: $\theta_0/2 = 0.5^\circ$
- Cotangent calculation:

$$
\cot(0.5^\circ) = \frac{1}{\tan(0.5^\circ)} = \frac{1}{0.00872687} \approx 114.58865
$$

- Logarithm calculation:

$$
\ln(114.58865) \approx 4.74136
$$

- Impedance calculation:

$$
Z_c = 120 \times 4.74136 \approx 568.96 \; \Omega
$$

#### Step 2: Compute for $\theta_0 = 12^\circ$
- Half-angle: $\theta_0/2 = 6^\circ$
- Cotangent calculation:

$$
\cot(6^\circ) = \frac{1}{\tan(6^\circ)} = \frac{1}{0.1051042} \approx 9.51436
$$

- Logarithm calculation:

$$
\ln(9.51436) \approx 2.25279
$$

- Impedance calculation:

$$
Z_c = 120 \times 2.25279 \approx 270.33 \; \Omega
$$

#### Step 3: Compute for $\theta_0 = 35^\circ$
- Half-angle: $\theta_0/2 = 17.5^\circ$
- Cotangent calculation:

$$
\cot(17.5^\circ) = \frac{1}{\tan(17.5^\circ)} = \frac{1}{0.3152988} \approx 3.17160
$$

- Logarithm calculation:

$$
\ln(3.17160) \approx 1.15424
$$

- Impedance calculation:

$$
Z_c = 120 \times 1.15424 \approx 138.51 \; \Omega
$$

**Result:**
1. For $\theta_0 = 1^\circ$, $Z_c \approx 568.96 \; \Omega$.
2. For $\theta_0 = 12^\circ$, $Z_c \approx 270.33 \; \Omega$.
3. For $\theta_0 = 35^\circ$, $Z_c \approx 138.51 \; \Omega$.

---

### Exercise 2: Equivalent Radius and Resonant Length of a Flat Strip Dipole

**Problem:** A flat metallic strip dipole antenna is fabricated on a thin substrate. The strip has a width $w = 8$ mm. 
1. Determine the equivalent radius $a_{\text{eq}}$ of a cylindrical wire antenna.
2. The operating frequency is $f = 1.8$ GHz. Compute the free-space wavelength $\lambda$.
3. Estimate the actual resonant length $L$ of the dipole, assuming that the equivalent cylindrical dipole has a shortening factor $F = L/L_{\text{ideal}} \approx 0.47$ due to its finite thickness (since the cylinder is relatively thick).

**Solution:**

#### Step 1: Calculate the equivalent radius
The equivalent radius of a flat strip of width $w$ is:

$$
a_{\text{eq}} \approx 0.25 w = 0.25 \times 8 \text{ mm} = 2.0 \text{ mm}
$$

The equivalent diameter of the cylindrical wire is $d_{\text{eq}} = 2 a_{\text{eq}} = 4.0$ mm.

#### Step 2: Compute the free-space wavelength
At $f = 1.8$ GHz ($1.8 \times 10^9$ Hz):

$$
\lambda = \frac{c}{f} = \frac{3 \times 10^8 \text{ m/s}}{1.8 \times 10^9 \text{ Hz}} = 0.16667 \text{ m} = 166.67 \text{ mm}
$$

The ideal half-wavelength dipole length is:

$$
L_{\text{ideal}} = \frac{\lambda}{2} = 83.33 \text{ mm}
$$

#### Step 3: Calculate the resonant length
Using the shortening factor $F = 0.47$:

$$
L = F \lambda = 0.47 \times 166.67 \text{ mm} = 78.33 \text{ mm}
$$

Let us check the length-to-diameter ratio to justify this shortening factor:

$$
\frac{L}{2 a_{\text{eq}}} = \frac{78.33 \text{ mm}}{4.0 \text{ mm}} \approx 19.58
$$

A ratio of $\approx 20$ represents a thick dipole, which justifies the shortening factor of $0.47$ (compared to $0.485$ for thinner wires).

**Result:** The equivalent radius is $a_{\text{eq}} = 2.0$ mm, the wavelength is $\lambda \approx 166.67$ mm, and the estimated resonant length is $L \approx 78.33$ mm.

---

### Exercise 3: Folded Dipole with Unequal Radii

**Problem:** A two-wire folded dipole of length $L = \lambda/2$ has a wire spacing $s = 18$ mm. The driven wire has a radius $a_1 = 1.0$ mm, and the parallel folded wire has a radius $a_2 = 3.0$ mm. The antenna is placed in free space, where the isolated dipole input impedance at resonance is $Z_d = 73 + j0 \; \Omega$.
1. Calculate the current division factor $\alpha$ using both the exact formula and the logarithmic approximation.
2. Find the impedance step-up ratio using both values of $\alpha$.
3. Compute the resulting input resistance $R_{\text{in}}$ at resonance in both cases.

**Solution:**

#### Step 1: Compute the current division factor $\alpha$

##### Method A: Logarithmic Approximation
The logarithmic approximation for $\alpha$ is:

$$
\alpha_{\text{approx}} \approx \frac{\ln(s/a_1)}{\ln(s/a_2)} = \frac{\ln(18/1.0)}{\ln(18/3.0)} = \frac{\ln(18.0)}{\ln(6.0)}
$$

Calculating the natural logarithms:

$$
\ln(18.0) \approx 2.89037, \quad \ln(6.0) \approx 1.79176
$$

$$
\alpha_{\text{approx}} \approx \frac{2.89037}{1.79176} \approx 1.6131
$$

##### Method B: Exact Formula
The exact formula using inverse hyperbolic cosines is:

$$
\alpha_{\text{exact}} = \frac{\cosh^{-1}\left(\frac{s^2 + a_1^2 - a_2^2}{2 s a_1}\right)}{\cosh^{-1}\left(\frac{s^2 - a_1^2 + a_2^2}{2 s a_2}\right)}
$$

Calculate the arguments of the hyperbolic cosines:
- Numerator argument:

$$
x_1 = \frac{s^2 + a_1^2 - a_2^2}{2 s a_1} = \frac{18^2 + 1.0^2 - 3.0^2}{2 \times 18 \times 1.0} = \frac{324 + 1.0 - 9.0}{36} = \frac{316}{36} \approx 8.77778
$$

- Denominator argument:

$$
x_2 = \frac{s^2 - a_1^2 + a_2^2}{2 s a_2} = \frac{18^2 - 1.0^2 + 3.0^2}{2 \times 18 \times 3.0} = \frac{324 - 1.0 + 9.0}{108} = \frac{332}{108} \approx 3.07407
$$

Calculate the inverse hyperbolic cosines using $\cosh^{-1}(x) = \ln(x + \sqrt{x^2 - 1})$:
- Numerator term:

$$
\cosh^{-1}(8.77778) = \ln(8.77778 + \sqrt{8.77778^2 - 1}) = \ln(8.77778 + 8.72064) = \ln(17.49842) \approx 2.86211
$$

- Denominator term:

$$
\cosh^{-1}(3.07407) = \ln(3.07407 + \sqrt{3.07407^2 - 1}) = \ln(3.07407 + 2.90680) = \ln(5.98087) \approx 1.78857
$$

- Exact current division factor:

$$
\alpha_{\text{exact}} = \frac{2.86211}{1.78857} \approx 1.6002
$$

#### Step 2: Calculate the impedance step-up ratio
- Using the approximate current division factor $\alpha_{\text{approx}} = 1.6131$:

$$
\text{Step-up Ratio}_{\text{approx}} = (1 + \alpha_{\text{approx}})^2 = (1 + 1.6131)^2 = 2.6131^2 \approx 6.8283
$$

- Using the exact current division factor $\alpha_{\text{exact}} = 1.6002$:

$$
\text{Step-up Ratio}_{\text{exact}} = (1 + \alpha_{\text{exact}})^2 = (1 + 1.6002)^2 = 2.6002^2 \approx 6.7610
$$

#### Step 3: Compute the input resistance $R_{\text{in}}$
- Case A (Approximation):

$$
R_{\text{in, approx}} = 6.8283 \times 73 \; \Omega \approx 498.47 \; \Omega
$$

- Case B (Exact):

$$
R_{\text{in, exact}} = 6.7610 \times 73 \; \Omega \approx 493.55 \; \Omega
$$

**Result:**
- Using the logarithmic approximation: $\alpha \approx 1.6131$, step-up ratio $\approx 6.83$, and $R_{\text{in}} \approx 498.47 \; \Omega$.
- Using the exact formula: $\alpha \approx 1.6002$, step-up ratio $\approx 6.76$, and $R_{\text{in}} \approx 493.55 \; \Omega$. The approximation error is $1.0\%$.

---

### Exercise 4: Gamma Match Design calculations

**Problem:** A resonant half-wave dipole operating at $f = 145$ MHz in free space has an input impedance $Z_d = 73 + j0 \; \Omega$. It is matched to a $50 \; \Omega$ coaxial cable using a Gamma match. The dipole wire radius is $a = 3.0$ mm, the Gamma rod radius is $a' = 1.0$ mm, and the center-to-center spacing is $s = 20$ mm.
1. Determine the current division factor $\alpha$ of the two-wire system using the logarithmic approximation.
2. Find the characteristic impedance $Z_0$ of the two-wire line formed by the dipole and the matching rod.
3. If the required tapping point length $l_g$ is determined to be $l_g = 0.08\lambda$ to achieve the $50 \; \Omega$ input resistance, calculate the matching section's inductive input reactance before tuning:

$$
X_{\text{in}} = Z_0 \tan(k l_g)
$$

4. Calculate the required series capacitance $C$ to tune out this reactance at $f = 145$ MHz.

**Solution:**

#### Step 1: Calculate the current division factor
Using the logarithmic approximation:

$$
\alpha \approx \frac{\ln(s/a)}{\ln(s/a')} = \frac{\ln(20/3.0)}{\ln(20/1.0)} = \frac{\ln(6.66667)}{\ln(20.0)}
$$

Calculating logarithms:

$$
\ln(6.66667) \approx 1.89712, \quad \ln(20.0) \approx 2.99573
$$

$$
\alpha \approx \frac{1.89712}{2.99573} \approx 0.63328
$$

#### Step 2: Compute the characteristic impedance $Z_0$ of the matching section
The characteristic impedance of the two-wire transmission line of unequal radii is:

$$
Z_0 \approx 120 \ln\left(\frac{s}{\sqrt{a a'}}\right)
$$

Substitute the radii:

$$
\sqrt{a a'} = \sqrt{3.0 \text{ mm} \times 1.0 \text{ mm}} = \sqrt{3.0} \approx 1.73205 \text{ mm}
$$

$$
Z_0 \approx 120 \ln\left(\frac{20}{1.73205}\right) = 120 \ln(11.5470)
$$

Calculating the logarithm:

$$
\ln(11.5470) \approx 2.44643
$$

$$
Z_0 \approx 120 \times 2.44643 \approx 293.57 \; \Omega
$$

#### Step 3: Compute the inductive reactance of the matching stub
For $l_g = 0.08\lambda$:

$$
k l_g = \frac{2\pi}{\lambda} (0.08\lambda) = 0.16\pi \text{ radians} = 28.8^\circ
$$

Calculate the tangent:

$$
\tan(28.8^\circ) \approx 0.54984
$$

The inductive reactance is:

$$
X_{\text{in}} = Z_0 \tan(k l_g) = 293.57 \times 0.54984 \approx 161.42 \; \Omega
$$

#### Step 4: Calculate the required series capacitance
At resonance, the capacitive reactance must cancel the inductive reactance:

$$
X_C = \frac{1}{2\pi f C} = X_{\text{in}} \implies C = \frac{1}{2\pi f X_{\text{in}}}
$$

Substitute $f = 145$ MHz ($1.45 \times 10^8$ Hz) and $X_{\text{in}} = 161.42 \; \Omega$:

$$
C = \frac{1}{2\pi \times (1.45 \times 10^8 \text{ Hz}) \times 161.42 \; \Omega}
$$

$$
C = \frac{1}{1.47076 \times 10^{11}} \approx 6.799 \times 10^{-12} \text{ F} \approx 6.80 \text{ pF}
$$

**Result:** The current division factor is $\alpha \approx 0.633$, the characteristic impedance is $Z_0 \approx 293.57 \; \Omega$, the input reactance of the stub is $X_{\text{in}} \approx 161.42 \; \Omega$, and the required series tuning capacitor is $C \approx 6.80$ pF.

---

### Exercise 5: Cutoff Frequency and Dimensions of a Discone Antenna

**Problem:** A discone antenna is designed to cover the entire VHF air band ($108$ MHz to $137$ MHz) and the UHF public service band, with a lower cutoff frequency of $f_{\text{min}} = 100$ MHz. 
1. Compute the maximum wavelength $\lambda_{\text{max}}$ at the cutoff frequency.
2. Determine the physical parameters of the discone antenna:
   - Cone slant height $L_v$ (based on $\lambda_{\text{max}}/4$).
   - Disc diameter $D_d$ (using the standard design guideline $D_d \approx 0.7 L_v$ or $0.7 \lambda_{\text{max}}/4$).
   - Spacing gap $g$ at the feedpoint (assuming a standard choice of $0.015 \lambda_{\text{max}}$).
3. If the cone half-angle is chosen to be $\theta_0 = 30^\circ$ (cone flare angle of $60^\circ$), calculate the diameter $D_c$ of the cone base.

**Solution:**

#### Step 1: Calculate the wavelength at the cutoff frequency
At $f_{\text{min}} = 100$ MHz ($1.0 \times 10^8$ Hz):

$$
\lambda_{\text{max}} = \frac{c}{f_{\text{min}}} = \frac{3 \times 10^8 \text{ m/s}}{1.0 \times 10^8 \text{ Hz}} = 3.0 \text{ meters} = 3000 \text{ mm}
$$

#### Step 2: Determine discone dimensions
- Slant Height $L_v$:

$$
L_v = \frac{\lambda_{\text{max}}}{4} = \frac{3000 \text{ mm}}{4} = 750 \text{ mm}
$$

- Disc Diameter $D_d$:

$$
D_d = 0.7 \times L_v = 0.7 \times 750 \text{ mm} = 525 \text{ mm}
$$

- Feed Gap $g$:

$$
g = 0.015 \times \lambda_{\text{max}} = 0.015 \times 3000 \text{ mm} = 45 \text{ mm}
$$

#### Step 3: Compute the diameter of the cone base
The cone forms a right-angled triangle in its cross-section. For a slant length $L_v$ and half-angle $\theta_0$:

The radius of the cone base $R_c$ is:

$$
R_c = L_v \sin\theta_0
$$

For $\theta_0 = 30^\circ$ (where $\sin(30^\circ) = 0.5$):

$$
R_c = 750 \text{ mm} \times 0.5 = 375 \text{ mm}
$$

The total cone base diameter is:

$$
D_c = 2 R_c = 2 \times 375 \text{ mm} = 750 \text{ mm}
$$

The vertical height of the cone $H_c$ is:

$$
H_c = L_v \cos\theta_0 = 750 \times \cos(30^\circ) = 750 \times 0.86603 \approx 649.52 \text{ mm}
$$

**Result:** At $f_{\text{min}} = 100$ MHz, the discone parameters are: cone slant height $L_v = 750$ mm, disc diameter $D_d = 525$ mm, feed gap $g = 45$ mm, and cone base diameter $D_c = 750$ mm.

---

### Exercise 6: VSWR and Mismatch Loss Before and After Matching

**Problem:** A broadband dipole antenna has an input impedance of $Z_{\text{in}} = 120 - j80 \; \Omega$ at a specific out-of-resonance operating frequency. The feed transmission line is a standard $50 \; \Omega$ coaxial cable.
1. Calculate the reflection coefficient $\Gamma_{\text{unmatched}}$ and the standing wave ratio $\text{VSWR}_{\text{unmatched}}$ without any matching network.
2. Determine the mismatch loss in dB for the unmatched antenna.
3. A matching circuit is introduced that transforms the antenna impedance to $Z_{\text{in, matched}} = 55 + j8 \; \Omega$. Calculate the new reflection coefficient $\Gamma_{\text{matched}}$, $\text{VSWR}_{\text{matched}}$, and the improved mismatch loss.

**Solution:**

#### Step 1: Calculate unmatched parameters
The reflection coefficient is:

$$
\Gamma = \frac{Z_{\text{in}} - Z_0}{Z_{\text{in}} + Z_0}
$$

Substitute $Z_{\text{in}} = 120 - j80 \; \Omega$ and $Z_0 = 50 \; \Omega$:

$$
\Gamma_{\text{unmatched}} = \frac{120 - j80 - 50}{120 - j80 + 50} = \frac{70 - j80}{170 - j80}
$$

Convert numerator and denominator to polar form:
- Numerator:

$$
|70 - j80| = \sqrt{70^2 + (-80)^2} = \sqrt{4900 + 6400} = \sqrt{11300} \approx 106.301
$$

$$
\theta_{\text{num}} = \tan^{-1}\left(\frac{-80}{70}\right) \approx -48.81^\circ
$$

- Denominator:

$$
|170 - j80| = \sqrt{170^2 + (-80)^2} = \sqrt{28900 + 6400} = \sqrt{35300} \approx 187.883
$$

$$
\theta_{\text{den}} = \tan^{-1}\left(\frac{-80}{170}\right) \approx -25.20^\circ
$$

- Reflection coefficient magnitude:

$$
|\Gamma_{\text{unmatched}}| = \frac{106.301}{187.883} \approx 0.56578
$$

- Phase:

$$
\theta_\Gamma = -48.81^\circ - (-25.20^\circ) = -23.61^\circ
$$

$$
\Gamma_{\text{unmatched}} \approx 0.566 \angle -23.61^\circ
$$

- Standing Wave Ratio (VSWR):

$$
\text{VSWR}_{\text{unmatched}} = \frac{1 + |\Gamma_{\text{unmatched}}|}{1 - |\Gamma_{\text{unmatched}}|} = \frac{1 + 0.56578}{1 - 0.56578} = \frac{1.56578}{0.43422} \approx 3.606 \approx 3.61
$$

#### Step 2: Compute mismatch loss for unmatched case
The transmission coefficient (mismatch efficiency) is:

$$
M = 1 - |\Gamma|^2 = 1 - (0.56578)^2 = 1 - 0.32011 = 0.67989 \approx 68.0\%
$$

This means $68\%$ of the power is transmitted, and $32\%$ is reflected.
The mismatch loss in decibels is:

$$
\text{Loss}_{\text{dB}} = -10 \log_{10}(M) = -10 \log_{10}(0.67989) \approx 1.676 \text{ dB}
$$

#### Step 3: Calculate matched parameters
For $Z_{\text{in, matched}} = 55 + j8 \; \Omega$:

$$
\Gamma_{\text{matched}} = \frac{55 + j8 - 50}{55 + j8 + 50} = \frac{5 + j8}{105 + j8}
$$

- Numerator magnitude:

$$
|5 + j8| = \sqrt{25 + 64} = \sqrt{89} \approx 9.4340
$$

- Denominator magnitude:

$$
|105 + j8| = \sqrt{11025 + 64} = \sqrt{11089} \approx 105.3043
$$

- Magnitude:

$$
|\Gamma_{\text{matched}}| = \frac{9.4340}{105.3043} \approx 0.08959
$$

- Standing Wave Ratio:

$$
\text{VSWR}_{\text{matched}} = \frac{1 + 0.08959}{1 - 0.08959} = \frac{1.08959}{0.91041} \approx 1.197 \approx 1.20
$$

- Mismatch efficiency:

$$
M_{\text{matched}} = 1 - |\Gamma_{\text{matched}}|^2 = 1 - (0.08959)^2 = 1 - 0.00803 = 0.99197 \approx 99.2\%
$$

- Mismatch loss:

$$
\text{Loss}_{\text{dB, matched}} = -10 \log_{10}(0.99197) \approx 0.035 \text{ dB}
$$

**Result:**
- Unmatched: $\Gamma \approx 0.566 \angle -23.61^\circ$, $\text{VSWR} \approx 3.61$, mismatch loss $\approx 1.68$ dB.
- Matched: $\Gamma \approx 0.090$, $\text{VSWR} \approx 1.20$, mismatch loss $\approx 0.035$ dB.

---

## 7. Exam Tip: Impedance Step-Up and Matching Networks

When dealing with exam problems on broadband dipoles and matching, keep the following relationships and pitfalls in mind:

1. **Folded Dipole Impedance Multiplication:** The step-up factor is $(1 + \alpha)^2$. For two wires, it simplifies to $2^2 = 4$ only if their radii are identical. If the driven arm is thinner than the folded arm ($a_1 < a_2$), the step-up factor is greater than 4. If the driven arm is thicker ($a_1 > a_2$), the step-up factor is less than 4.
2. **Equivalent Radius of Flat Strips:** Do not confuse equivalent radius with equivalent diameter. A flat strip of width $w$ is electrostatically equivalent to a cylinder of radius $a_{\text{eq}} \approx 0.25w$ (so diameter is $0.5w$).
3. **Biconical Input Impedance:** An infinite biconical antenna has a purely real input impedance equal to $Z_c$. It does not vary with frequency. A finite biconical antenna, however, has an input impedance that oscillates around $Z_c$ as frequency increases. The oscillation amplitude decays for wider cone angles due to reduced end reflections.
4. **Gamma Match Variable Roles:**
   - The shorting bar position (length $l_g$) controls the resistive part of the matched impedance.
   - The series capacitor $C$ cancels the inductive reactance of the matching loop, restoring the match to real resonance.
