# Microstrip Antennas

Microstrip antennas (also called patch antennas) consist of a metallic patch on a grounded dielectric substrate, fed by a microstrip transmission line or coaxial probe. They operate at microwave frequencies (typically 100 MHz -- 100 GHz) and are widely used in wireless communications, aerospace, and mobile systems due to their low profile, light weight, planar geometry, and compatibility with printed circuit board (PCB) fabrication. The analysis of microstrip antennas is based on the cavity model, which treats the region between the patch and ground plane as a dielectric-loaded cavity bounded by electric walls on the top and bottom and magnetic walls along the edges. This section covers the rectangular and circular patch geometries, quality factor and bandwidth, input impedance, coupling methods, circular polarization techniques, and array feed networks.

---

## 1. Conceptual Foundation

### 1.1 The Microstrip Antenna Concept

A microstrip antenna consists of a conducting patch (typically copper or gold) of planar geometry (rectangular, circular, triangular, or other shape) separated from a ground plane by a thin dielectric substrate of thickness $h$, typically $0.003\lambda_0 \le h \le 0.05\lambda_0$. The patch is fed by a microstrip line or coaxial probe, and radiation occurs primarily from the fringing fields between the patch edge and the ground plane.

The fundamental principle underlying microstrip antenna operation is the **cavity model**: the region under the patch behaves as a dielectric-loaded resonant cavity. At resonance, strong fields build up inside the cavity, and the fringing fields at the open edges radiate into free space.

### 1.2 Why Microstrip Antennas?

| Advantage | Explanation |
|:---|:---|
| Low profile | Thickness is typically $h \ll \lambda_0$ |
| Light weight | Reduces structural load in aerospace/mobile applications |
| Planar geometry | Conforms to curved surfaces, integrates with PCB |
| Low fabrication cost | Photolithographic etching is inexpensive and reproducible |
| Linear and circular polarization | Easily achieved by feed placement or perturbation |
| Dual-band/multiband operation | Achieved through slots, stacked patches, or multiple feeds |
| Integration with active devices | Amplifiers, phase shifters, and switches can be co-fabricated |

| Disadvantage | Explanation |
|:---|:---|
| Narrow bandwidth | Typically 1%--5% for standard designs |
| Low gain | Typically 4--8 dBi for a single element |
| Low power handling | Limited by substrate breakdown and conductor losses |
| Surface wave excitation | Reduces efficiency, especially on high-$\epsilon_r$ substrates |
| Polarization purity | Cross-polarization levels can be significant |

### 1.3 Fringing Fields and Radiation Mechanism

The radiation of a microstrip patch arises from the fringing fields at the open edges of the cavity. For a rectangular patch operating in the dominant $TM_{010}$ mode (where the length $L \approx \lambda_0/2\sqrt{\epsilon_r}$), the electric field is maximum at the radiating edges ($y = 0$ and $y = L$) and minimum at the center. The fringing fields at these edges can be modeled as two parallel slots of width $W$ and height $h$, separated by distance $L$, each radiating as a magnetic current source.

> **[Key Insight]** The two radiating slots of a rectangular patch are separated by approximately $\lambda_0/2\sqrt{\epsilon_r}$, which places them in phase. The radiation pattern in the E-plane ($yz$-plane) is broad, while the H-plane ($xz$-plane) pattern is narrower due to the width $W$ of the slots.

---

## 2. Formal Definition and Model

### 2.1 The Cavity Model

The cavity model treats the substrate region under the patch ($0 \le x \le h$, $0 \le y \le L$, $0 \le z \le W$) as a dielectric-loaded resonant cavity with:

- **Electric walls** at $x = 0$ and $x = h$ (top and bottom: the patch and ground plane are PEC conductors).
- **Magnetic walls** at $y = 0$, $y = L$, $z = 0$, and $z = W$ (the open edges approximate open circuits, with vanishing tangential magnetic field).

For the $TM_x$ mode (magnetic field transverse to $x$), the vector magnetic potential $A_x$ satisfies the wave equation:

$$
\nabla^2 A_x + k^2 A_x = 0
$$

where $k^2 = \omega^2 \mu_0 \epsilon_0 \epsilon_r = k_0^2 \epsilon_r$.

The general solution for the rectangular cavity is:

$$
A_x = A_{mnp} \cos(k_x x) \cos(k_y y) \cos(k_z z)
$$

with the wavenumbers constrained by the boundary conditions:

$$
k_x = \frac{m\pi}{h}, \quad m = 0, 1, 2, \dots
$$

$$
k_y = \frac{n\pi}{L}, \quad n = 0, 1, 2, \dots
$$

$$
k_z = \frac{p\pi}{W}, \quad p = 0, 1, 2, \dots
$$

where $m$, $n$, $p$ cannot all be zero simultaneously.

The resonant wavenumber is:

$$
k_{mnp} = \sqrt{\left(\frac{m\pi}{h}\right)^2 + \left(\frac{n\pi}{L}\right)^2 + \left(\frac{p\pi}{W}\right)^2} = k_0 \sqrt{\epsilon_r}
$$

Since $h \ll L$ and $h \ll W$, the lowest-order modes are those with $m = 0$. The dominant mode depends on which dimension ($L$ or $W$) is longer.

### 2.2 Rectangular Patch -- Dominant Mode $TM_{010}$

For a rectangular patch with $L > W > h$, the dominant mode is $TM_{010}$ ($m = 0$, $n = 1$, $p = 0$). The field distribution is:

$$
E_x = E_0 \cos\left(\frac{\pi y}{L}\right)
$$

$$
H_z = -\frac{j\pi}{\omega\mu_0 L} E_0 \sin\left(\frac{\pi y}{L}\right)
$$

$$
H_y = 0
$$

The resonant frequency of the $TM_{010}$ mode (without fringing correction) is:

$$
f_{r010} = \frac{1}{2L\sqrt{\mu_0 \epsilon_0 \epsilon_r}} = \frac{c_0}{2L\sqrt{\epsilon_r}}
$$

### 2.3 Fringing Correction and Effective Parameters

Fringing fields extend the patch electrically beyond its physical boundaries. This is accounted for by using an **effective dielectric constant** $\epsilon_{\text{reff}}$ and an **effective length extension** $\Delta L$.

**Effective dielectric constant** (for $W/h \ge 1$):

$$
\epsilon_{\text{reff}} = \frac{\epsilon_r + 1}{2} + \frac{\epsilon_r - 1}{2} \left[ 1 + 12 \frac{h}{W} \right]^{-1/2}
$$

**Length extension** due to fringing:

$$
\frac{\Delta L}{h} = 0.412 \frac{(\epsilon_{\text{reff}} + 0.3)(W/h + 0.264)}{(\epsilon_{\text{reff}} - 0.258)(W/h + 0.8)}
$$

The **effective length** of the patch is:

$$
L_{\text{eff}} = L + 2\Delta L
$$

The corrected resonant frequency is:

$$
f_{rc010} = \frac{1}{2L_{\text{eff}} \sqrt{\mu_0 \epsilon_0 \epsilon_{\text{reff}}}} = \frac{c_0}{2(L + 2\Delta L) \sqrt{\epsilon_{\text{reff}}}}
$$

The **fringing factor** $q$ relates the corrected to the uncorrected resonant frequency:

$$
q = \frac{f_{rc010}}{f_{r010}} = \frac{L\sqrt{\epsilon_r}}{(L + 2\Delta L)\sqrt{\epsilon_{\text{reff}}}}
$$

### 2.4 Rectangular Patch Width Design

The patch width $W$ is typically chosen to achieve efficient radiation. A common design choice is:

$$
W = \frac{c_0}{2f_r} \sqrt{\frac{2}{\epsilon_r + 1}}
$$

This width yields a good radiation efficiency and a practical input impedance (typically 100--400 $\Omega$ at the edge).

### 2.5 Circular Patch

For the circular patch, the cavity model uses cylindrical coordinates. The dominant mode is $TM_{11}$ (with mode indices $m = 1$, $n = 1$). The field distribution is:

$$
E_z = E_0 J_1(k_{11} \rho) \cos(\phi)
$$

where $J_1$ is the Bessel function of the first kind, order 1, and $k_{11}$ is the eigenvalue.

The resonant frequency for the $TM_{11}$ mode is:

$$
f_{r11} = \frac{c_0 \chi_{11}}{2\pi a \sqrt{\epsilon_r}}
$$

where $\chi_{11}$ is the first root of $J_1'(x) = 0$, equal to $\chi_{11} = 1.8412$ (for the derivative condition corresponding to the magnetic wall boundary), and $a$ is the physical radius of the patch.

With fringing correction, the effective radius $a_e$ is used:

$$
a_e = a \sqrt{1 + \frac{2h}{\pi a \epsilon_r} \left( \ln\left(\frac{\pi a}{2h}\right) + 1.7726 \right)}
$$

The corrected resonant frequency is:

$$
f_{rc11} = \frac{c_0 \chi_{11}}{2\pi a_e \sqrt{\epsilon_{\text{reff}}}}
$$

> **[Supplementary]** The full expression for the effective radius of a circular microstrip patch, including fringing, is:
>
> $$
> a_e = a \left[ 1 + \frac{2h}{\pi a \epsilon_r} \left( \ln\left( \frac{\pi a}{2h} \right) + 1.7726 \right) \right]^{1/2}
> $$
>
> This formula was developed by Hammerstad and is accurate for $a/h \gg 1$.

### 2.6 Quality Factor, Bandwidth, and Efficiency

The total quality factor $Q_T$ of the microstrip cavity accounts for three loss mechanisms:

1. **Radiation loss** (quality factor $Q_r$): energy radiated into free space.
2. **Conductor loss** (quality factor $Q_c$): ohmic losses in the patch and ground plane.
3. **Dielectric loss** (quality factor $Q_d$): losses in the substrate material.

The total quality factor is:

$$
\frac{1}{Q_T} = \frac{1}{Q_r} + \frac{1}{Q_c} + \frac{1}{Q_d}
$$

**Dielectric quality factor:**

$$
Q_d = \frac{1}{\tan\delta}
$$

where $\tan\delta$ is the loss tangent of the substrate.

**Conductor quality factor:**

$$
Q_c = h \sqrt{\pi f \mu_0 \sigma}
$$

where $\sigma$ is the conductivity of the patch and ground plane.

**Radiation quality factor** (for rectangular patch, $TM_{010}$ mode):

$$
Q_r = \frac{2\omega\epsilon_r}{h G_t} \cdot \frac{\iint_V |E|^2 dV}{\oint_S |E|^2 dS}
$$

where $G_t$ is the total conductance of the radiating slots. An approximate formula, valid for $h/\lambda_0 \ll 1$, is:

$$
Q_r \approx \frac{\epsilon_r W L}{120 \lambda_0 h G_t}
$$

**Bandwidth** (for VSWR $\le S$):

$$
BW = \frac{S - 1}{Q_T \sqrt{S}}
$$

For a matched antenna (VSWR $\le 2$), the fractional bandwidth is:

$$
BW = \frac{1}{Q_T \sqrt{2}} \approx \frac{0.707}{Q_T}
$$

**Radiation efficiency:**

$$
\eta = \frac{Q_T}{Q_r}
$$

### 2.7 Input Impedance

The input impedance of a microstrip patch depends on the feed location. For a rectangular patch fed at a distance $y_0$ from the edge (along the resonant length $L$), the input resistance at resonance is:

$$
R_{\text{in}} = \frac{1}{G_t} \cos^2\left( \frac{\pi y_0}{L} \right)
$$

where $G_t$ is the total conductance of the two radiating slots. For a probe feed, $y_0$ is measured from the patch edge; feeding at the edge ($y_0 = 0$) gives maximum resistance, while feeding at the center ($y_0 = L/2$) gives zero resistance (null).

For the rectangular patch with width $W$, the total slot conductance is:

$$
G_t = \frac{2\pi W}{3\lambda_0^2} \quad \text{(approximate, for $W \gg \lambda_0$)}
$$

### 2.8 Coupling Methods

| Feed Method | Description | Advantages | Disadvantages |
|:---|:---|:---|:---|
| **Microstrip line feed** | A conducting strip of width $w_f$ connects to the patch edge | Planar fabrication, easy impedance matching | Spurious radiation from feed line |
| **Coaxial probe feed** | Inner conductor passes through substrate to the patch | Low spurious radiation, flexible placement | Inductive reactance, difficult to fabricate for thick substrates |
| **Aperture coupling** | A slot in the ground plane couples energy from a microstrip line on the opposite side | No direct connection to patch, separate substrate optimization | Requires multilayer fabrication, backlobe radiation |
| **Proximity coupling** | An open-ended microstrip line is placed beneath the patch, separated by a thin dielectric | High bandwidth, no direct contact | Requires precise alignment, two-layer fabrication |

### 2.9 Circular Polarization

Circular polarization (CP) in microstrip antennas is achieved by exciting two orthogonal modes with a $90^\circ$ phase difference. Common techniques include:

1. **Single-feed CP:** Perturbation of the patch geometry (truncated corners, diagonal slot, nearly square patch) splits the resonant frequencies of two orthogonal modes. By sizing the perturbation appropriately, the two modes are excited with equal amplitude and $90^\circ$ phase shift at the design frequency.

2. **Dual-feed CP:** Two orthogonal feeds with a $90^\circ$ hybrid coupler provide the necessary phase difference. This offers wider bandwidth but requires an external feed network.

3. **Sequential rotation:** In arrays, sequential rotation of patches and feed phases produces CP over a wider bandwidth.

For a nearly square patch (sides $L_x$ and $L_y$ slightly different), the condition for CP is:

$$
\Delta L = L_x - L_y = \frac{1}{\sqrt{2} Q_T} L_{\text{avg}}
$$

where $L_{\text{avg}} = (L_x + L_y)/2$.

### 2.10 Arrays and Feed Networks

Microstrip patches are commonly arranged in arrays to increase directivity and gain. The feed network distributes power to each element with the correct amplitude and phase.

**Series feed:** Elements are connected in a chain. Phase progression is controlled by the line lengths between elements. Simple but has narrow bandwidth due to phase dispersion.

**Corporate feed:** Power dividers (typically $T$-junctions or Wilkinson dividers) split power to each element. Provides broader bandwidth and independent amplitude/phase control, but requires more space and introduces line losses.

**Array factor** for a linear array of $N$ patches with uniform amplitude and spacing $d$:

$$
AF(\theta) = \frac{\sin(N\psi/2)}{N\sin(\psi/2)}, \quad \psi = k_0 d \sin\theta + \beta
$$

where $\beta$ is the progressive phase shift between elements. Beam scanning is achieved by adjusting $\beta$.

---

## 3. Key Parameters and Constraints

### Table 1: Microstrip Patch Antenna Parameters

| Parameter | Symbol | Typical Range | Impact |
|:---|:---:|:---:|:---|
| Substrate thickness | $h$ | $0.003\lambda_0$ -- $0.05\lambda_0$ | Thicker $\to$ wider bandwidth, more surface waves |
| Substrate dielectric constant | $\epsilon_r$ | 2.2 -- 12 | Higher $\epsilon_r$ $\to$ smaller patch, lower efficiency |
| Substrate loss tangent | $\tan\delta$ | 0.0001 -- 0.005 | Higher $\to$ lower efficiency, broader bandwidth (loss-limited) |
| Patch length (rectangular) | $L$ | $0.3\lambda_0/\sqrt{\epsilon_r}$ -- $0.5\lambda_0/\sqrt{\epsilon_r}$ | Determines resonant frequency |
| Patch width (rectangular) | $W$ | $0.5L$ -- $2L$ | Wider $\to$ higher gain, higher input impedance |
| Patch radius (circular) | $a$ | $0.2\lambda_0/\sqrt{\epsilon_r}$ -- $0.4\lambda_0/\sqrt{\epsilon_r}$ | Determines resonant frequency |
| Total quality factor | $Q_T$ | 10 -- 500 | Higher $\to$ narrower bandwidth, higher gain at resonance |
| Bandwidth (VSWR $\le 2$) | $BW$ | 1% -- 5% | Determined by $Q_T$ and matching |
| Gain (single element) | $G$ | 4 -- 8 dBi | Depends on patch size, substrate, losses |
| Polarization purity | $XPD$ | 15 -- 30 dB | Higher $\to$ better isolation of desired polarization |

### Table 2: Common Substrate Materials

| Substrate | $\epsilon_r$ | $\tan\delta$ | Typical $h$ (mm) | Application |
|:---|:---:|:---:|:---:|:---|
| RT/Duroid 5880 | 2.2 | 0.0009 | 0.254 -- 3.175 | High-frequency, low-loss |
| RT/Duroid 5870 | 2.33 | 0.0012 | 0.254 -- 3.175 | General microwave |
| FR-4 | 4.4 | 0.02 | 0.8 -- 1.6 | Low-cost, lossy above 2 GHz |
| Rogers 4003C | 3.55 | 0.0027 | 0.2 -- 1.52 | Low-cost microwave |
| Alumina ($Al_2O_3$) | 9.8 | 0.0001 | 0.254 -- 1.0 | High $\epsilon_r$, high-frequency |
| GaAs | 12.9 | 0.002 | 0.1 -- 0.5 | MMIC integration |

### Table 3: Modes of Rectangular Patch ($L > W > h$)

| Mode | $(m,n,p)$ | $E_x$ Distribution | $f_r$ (relative) | Notes |
|:---|:---:|:---|:---:|:---|
| $TM_{010}$ | (0,1,0) | $\cos(\pi y/L)$ | $f_0$ | Dominant mode, broadside radiation |
| $TM_{001}$ | (0,0,1) | $\cos(\pi z/W)$ | $(L/W)f_0$ | Higher than $TM_{010}$, orthogonal polarization |
| $TM_{020}$ | (0,2,0) | $\cos(2\pi y/L)$ | $2f_0$ | Null at boresight, conical pattern |
| $TM_{110}$ | (1,1,0) | $\cos(\pi y/L)\cos(\pi z/W)$ | $\sqrt{1+(L/W)^2}f_0$ | Higher-order, dual-polarization |

---

## 4. Step-by-Step Mechanism

### 4.1 How a Microstrip Patch Radiates

**Step 1: Resonance establishment.** A feed (coaxial probe or microstrip line) launches a wave into the cavity formed by the patch, ground plane, and magnetic walls. When the frequency matches the resonant condition $L \approx \lambda_g/2$ (where $\lambda_g = \lambda_0/\sqrt{\epsilon_{\text{reff}}}$ is the guided wavelength), a standing wave pattern develops under the patch.

**Step 2: Field concentration.** In the $TM_{010}$ mode, the electric field $E_x$ is maximum at the radiating edges ($y = 0$, $y = L$) and minimum at the center ($y = L/2$). The magnetic field $H_z$ is maximum at the center and zero at the edges.

**Step 3: Fringing field formation.** At the radiating edges, the electric field does not terminate abruptly at the patch boundary but extends into the region beyond the patch. These fringing fields can be modeled as equivalent magnetic current sources at the edges:

$$
\mathbf{M}_s = -2\hat{n} \times \mathbf{E}_a
$$

where $\hat{n}$ is the outward normal from the patch edge and $\mathbf{E}_a$ is the aperture field at the edge.

**Step 4: Slot radiation.** Each radiating edge behaves as a slot antenna of width $W$ and height $h$, radiating into the half-space above the ground plane. The two slots (separated by distance $L$) act as a two-element array. For the $TM_{010}$ mode, the slots are in phase, producing a broadside radiation pattern.

**Step 5: Pattern formation.** The far-field pattern is the product of a single slot pattern and an array factor. In the E-plane ($\phi = 90^\circ$, $yz$-plane), the pattern is broad with a half-power beamwidth typically $60^\circ$--$80^\circ$. In the H-plane ($\phi = 0^\circ$, $xz$-plane), the pattern is narrower due to the slot width $W$.

### 4.2 Rectangular Patch Design Procedure

**Step 1: Determine patch width $W$.**

$$
W = \frac{c_0}{2f_r} \sqrt{\frac{2}{\epsilon_r + 1}}
$$

**Step 2: Calculate $\epsilon_{\text{reff}}$ and $\Delta L$.**

$$
\epsilon_{\text{reff}} = \frac{\epsilon_r + 1}{2} + \frac{\epsilon_r - 1}{2} \left[ 1 + 12\frac{h}{W} \right]^{-1/2}
$$

$$
\Delta L = 0.412h \frac{(\epsilon_{\text{reff}} + 0.3)(W/h + 0.264)}{(\epsilon_{\text{reff}} - 0.258)(W/h + 0.8)}
$$

**Step 3: Determine patch length $L$.**

$$
L = \frac{c_0}{2f_r \sqrt{\epsilon_{\text{reff}}}} - 2\Delta L
$$

**Step 4: Determine feed location.** For a probe feed at distance $y_0$ from the edge along the resonant dimension:

$$
R_{\text{in}}(y_0) = R_{\text{in}}(0) \cos^2\left( \frac{\pi y_0}{L} \right)
$$

where $R_{\text{in}}(0)$ is the edge input resistance (typically 100--400 $\Omega$). Solve for $y_0$ numerically to match the desired feed impedance (typically $50\ \Omega$).

### 4.3 Circular Patch Design Procedure

**Step 1: Determine physical radius $a$ (initial estimate, ignoring fringing).**

$$
a = \frac{c_0 \chi_{11}}{2\pi f_r \sqrt{\epsilon_r}} = \frac{1.8412 c_0}{2\pi f_r \sqrt{\epsilon_r}}
$$

**Step 2: Calculate effective radius $a_e$.**

$$
a_e = a \left[ 1 + \frac{2h}{\pi a \epsilon_r} \left( \ln\left( \frac{\pi a}{2h} \right) + 1.7726 \right) \right]^{1/2}
$$

**Step 3: Correct resonant frequency.**

$$
f_{rc} = \frac{c_0 \chi_{11}}{2\pi a_e \sqrt{\epsilon_{\text{reff}}}}
$$

If $f_{rc}$ differs from the design $f_r$, iterate by adjusting $a$ and recomputing until convergence.

### 4.4 Bandwidth Enhancement

Standard microstrip patches have bandwidths of 1%--5%. Techniques to increase bandwidth include:

1. **Increasing substrate thickness:** $BW \propto h/\lambda_0$ (up to the point where surface waves become significant).
2. **Using low-$\epsilon_r$ substrates:** Lower $\epsilon_r$ reduces $Q_r$, increasing bandwidth.
3. **Adding parasitic elements:** Stacked patches or coplanar parasitics create multiple resonances that merge into a wider bandwidth.
4. **Aperture coupling:** Provides a wider impedance bandwidth than probe feeds for thick substrates.
5. **U-slot or L-probe feeding:** Introduces additional resonances that broaden the total bandwidth.

### 4.5 Surface Wave Effects

Surface waves are guided modes supported by the grounded dielectric substrate. They are excited by the patch and propagate within the substrate, eventually radiating at substrate edges or being absorbed. Surface waves reduce radiation efficiency and can degrade pattern shape.

The cutoff frequency for the first surface wave mode ($TM_0$) is zero (the $TM_0$ surface wave propagates at all frequencies). The $TE_1$ surface wave cutoff occurs when:

$$
f_c = \frac{c_0}{4h\sqrt{\epsilon_r - 1}}
$$

For efficient operation, the substrate thickness should satisfy $h \le 0.03\lambda_0/\sqrt{\epsilon_r}$ to minimize surface wave excitation.

---

## Solved Exercises

### Exercise 1: Rectangular Patch Dimensions at 2.4 GHz

**Problem:** Design a rectangular microstrip patch antenna on an FR-4 substrate ($\epsilon_r = 4.4$, $h = 1.6$ mm, $\tan\delta = 0.02$) for operation at $f_r = 2.4$ GHz. Determine:
1. The patch width $W$.
2. The effective dielectric constant $\epsilon_{\text{reff}}$.
3. The length extension $\Delta L$.
4. The patch length $L$.
5. The actual resonant frequency if $L$ is rounded to the nearest 0.1 mm.

**Solution:**

#### Step 1: Patch width

$$
W = \frac{c_0}{2f_r} \sqrt{\frac{2}{\epsilon_r + 1}} = \frac{3 \times 10^8}{2 \times 2.4 \times 10^9} \sqrt{\frac{2}{4.4 + 1}} = 0.0625 \sqrt{\frac{2}{5.4}}
$$

$$
W = 0.0625 \times \sqrt{0.3704} = 0.0625 \times 0.6086 = 0.0380 \text{ m} = 38.0 \text{ mm}
$$

#### Step 2: Effective dielectric constant

$$
\frac{W}{h} = \frac{38.0}{1.6} = 23.75
$$

$$
\epsilon_{\text{reff}} = \frac{4.4 + 1}{2} + \frac{4.4 - 1}{2} \left[ 1 + \frac{12}{23.75} \right]^{-1/2}
$$

$$
\epsilon_{\text{reff}} = 2.7 + 1.7 \times [1 + 0.5053]^{-1/2} = 2.7 + 1.7 \times [1.5053]^{-1/2}
$$

$$
\epsilon_{\text{reff}} = 2.7 + 1.7 \times 0.8151 = 2.7 + 1.3857 = 4.086
$$

#### Step 3: Length extension

$$
\frac{\Delta L}{h} = 0.412 \frac{(4.086 + 0.3)(23.75 + 0.264)}{(4.086 - 0.258)(23.75 + 0.8)}
$$

$$
\frac{\Delta L}{h} = 0.412 \frac{4.386 \times 24.014}{3.828 \times 24.55} = 0.412 \frac{105.32}{93.98}
$$

$$
\frac{\Delta L}{h} = 0.412 \times 1.121 = 0.462
$$

$$
\Delta L = 0.462 \times 1.6 = 0.739 \text{ mm}
$$

#### Step 4: Patch length

$$
L = \frac{c_0}{2f_r \sqrt{\epsilon_{\text{reff}}}} - 2\Delta L
$$

$$
L = \frac{3 \times 10^8}{2 \times 2.4 \times 10^9 \times \sqrt{4.086}} - 2 \times 0.000739
$$

$$
L = \frac{0.0625}{2.021} - 0.001478 = 0.03092 - 0.00148 = 0.02944 \text{ m} = 29.44 \text{ mm}
$$

Rounded to nearest 0.1 mm: $L = 29.4$ mm.

#### Step 5: Actual resonant frequency

With $L = 29.4$ mm:

$$
L_{\text{eff}} = L + 2\Delta L = 29.4 + 2 \times 0.739 = 29.4 + 1.478 = 30.878 \text{ mm}
$$

$$
f_{rc} = \frac{c_0}{2L_{\text{eff}} \sqrt{\epsilon_{\text{reff}}}} = \frac{3 \times 10^8}{2 \times 0.030878 \times 2.021}
$$

$$
f_{rc} = \frac{3 \times 10^8}{0.1248} = 2.404 \text{ GHz}
$$

The resonant frequency shifts from 2.400 GHz to 2.404 GHz, a very small shift of 0.17%.

---

### Exercise 2: Circular Patch Dimensions at 5.8 GHz

**Problem:** Design a circular microstrip patch antenna on RT/Duroid 5880 ($\epsilon_r = 2.2$, $h = 0.787$ mm) for $f_r = 5.8$ GHz. Determine:
1. The physical radius $a$ (initial estimate).
2. The effective radius $a_e$.
3. The corrected resonant frequency.
4. The patch diameter in millimeters.

**Solution:**

#### Step 1: Physical radius (initial estimate)

For the $TM_{11}$ mode, $\chi_{11} = 1.8412$.

$$
a = \frac{c_0 \chi_{11}}{2\pi f_r \sqrt{\epsilon_r}} = \frac{3 \times 10^8 \times 1.8412}{2\pi \times 5.8 \times 10^9 \times \sqrt{2.2}}
$$

$$
a = \frac{5.5236 \times 10^8}{2\pi \times 5.8 \times 10^9 \times 1.4832} = \frac{5.5236 \times 10^8}{5.405 \times 10^{10}}
$$

$$
a = 0.01022 \text{ m} = 10.22 \text{ mm}
$$

#### Step 2: Effective radius

First compute the effective dielectric constant:

$$
\frac{W}{h} \text{ not directly applicable. For circular patch, compute } \frac{a}{h} = \frac{10.22}{0.787} = 12.98
$$

$$
\epsilon_{\text{reff}} \approx \frac{2.2 + 1}{2} + \frac{2.2 - 1}{2} \left[ 1 + 12\frac{0.787}{2 \times 10.22} \right]^{-1/2}
$$

We approximate $\epsilon_{\text{reff}}$ for the circular patch by using an effective width $W_{\text{eff}} \approx 2a$:

$$
\frac{h}{W_{\text{eff}}} = \frac{0.787}{20.44} = 0.0385
$$

$$
\epsilon_{\text{reff}} = 1.6 + 0.6 \times [1 + 12 \times 0.0385]^{-1/2} = 1.6 + 0.6 \times [1.462]^{-1/2}
$$

$$
\epsilon_{\text{reff}} = 1.6 + 0.6 \times 0.827 = 1.6 + 0.496 = 2.096
$$

Now compute the effective radius:

$$
a_e = a \left[ 1 + \frac{2h}{\pi a \epsilon_r} \left( \ln\left( \frac{\pi a}{2h} \right) + 1.7726 \right) \right]^{1/2}
$$

$$
\frac{2h}{\pi a \epsilon_r} = \frac{2 \times 0.000787}{\pi \times 0.01022 \times 2.2} = \frac{0.001574}{0.07063} = 0.02229
$$

$$
\frac{\pi a}{2h} = \frac{\pi \times 10.22}{2 \times 0.787} = \frac{32.11}{1.574} = 20.40
$$

$$
\ln(20.40) = 3.015
$$

$$
\text{Correction} = 3.015 + 1.7726 = 4.788
$$

$$
\text{Inner term} = 0.02229 \times 4.788 = 0.1067
$$

$$
a_e = 10.22 \times [1 + 0.1067]^{1/2} = 10.22 \times \sqrt{1.1067} = 10.22 \times 1.0519
$$

$$
a_e = 10.75 \text{ mm}
$$

#### Step 3: Corrected resonant frequency

$$
f_{rc} = \frac{c_0 \chi_{11}}{2\pi a_e \sqrt{\epsilon_{\text{reff}}}} = \frac{3 \times 10^8 \times 1.8412}{2\pi \times 0.01075 \times \sqrt{2.096}}
$$

$$
f_{rc} = \frac{5.5236 \times 10^8}{2\pi \times 0.01075 \times 1.448} = \frac{5.5236 \times 10^8}{0.09776}
$$

$$
f_{rc} = 5.649 \times 10^9 = 5.649 \text{ GHz}
$$

#### Step 4: Patch diameter

$$
D = 2a_e = 2 \times 10.75 = 21.5 \text{ mm}
$$

> **[Supplementary]** The effective radius correction shifts the resonant frequency from the design target of 5.800 GHz to 5.649 GHz (a 2.6% difference). For precise designs, an iterative adjustment of $a$ is performed until $f_{rc}$ converges to the target.

---

### Exercise 3: Quality Factor and Bandwidth

**Problem:** A rectangular microstrip patch on Rogers 4003C ($\epsilon_r = 3.55$, $h = 1.52$ mm, $\tan\delta = 0.0027$) operates at 3.5 GHz. The patch dimensions are $L = 26.5$ mm, $W = 32.0$ mm. The copper conductivity is $\sigma = 5.8 \times 10^7$ S/m.
1. Estimate $Q_d$.
2. Estimate $Q_c$ (conductor loss in patch and ground plane).
3. Estimate $Q_r$ (radiation loss), assuming $Q_r \approx 30$ for this geometry (typical for $h/\lambda_0 \approx 0.018$ with $\epsilon_r = 3.55$).
4. Determine $Q_T$ and the VSWR $\le 2$ bandwidth.
5. Determine the radiation efficiency.

**Solution:**

#### Step 1: Dielectric quality factor

$$
Q_d = \frac{1}{\tan\delta} = \frac{1}{0.0027} = 370.4
$$

#### Step 2: Conductor quality factor

$$
Q_c = h \sqrt{\pi f \mu_0 \sigma}
$$

$$
Q_c = 0.00152 \times \sqrt{\pi \times 3.5 \times 10^9 \times 4\pi \times 10^{-7} \times 5.8 \times 10^7}
$$

$$
Q_c = 0.00152 \times \sqrt{\pi \times 3.5 \times 10^9 \times 4\pi \times 5.8}
$$

$$
Q_c = 0.00152 \times \sqrt{3.5 \times 4 \times 5.8 \times \pi^2 \times 10^9 \times 10^{-7}}
$$

$$
Q_c = 0.00152 \times \sqrt{3.5 \times 4 \times 5.8 \times \pi^2 \times 10^2}
$$

$$
Q_c = 0.00152 \times \sqrt{3.5 \times 4 \times 5.8 \times 9.8696 \times 100}
$$

$$
Q_c = 0.00152 \times \sqrt{80166} = 0.00152 \times 283.1 = 0.430
$$

Wait -- this result is too small. Let me re-check the formula. The conductor quality factor for a microstrip patch is:

$$
Q_c = \frac{h}{\delta_s} \cdot \frac{\text{(geometric factor)}}{\text{...}}
$$

A more appropriate formula for $Q_c$ of a rectangular patch is:

$$
Q_c = h \sqrt{\pi f \mu_0 \sigma}
$$

For $f = 3.5$ GHz:

$$
\sqrt{2\pi f \mu_0} = \sqrt{2\pi \times 3.5 \times 10^9 \times 4\pi \times 10^{-7}} = \sqrt{2 \times 3.5 \times 4 \times \pi^2 \times 10^2}
$$

$$
\sqrt{2\pi f \mu_0} = \sqrt{28 \times 9.8696 \times 100} = \sqrt{27635} = 166.2
$$

The skin depth $\delta_s$ is:

$$
\delta_s = \frac{1}{\sqrt{\pi f \mu_0 \sigma}} = \frac{1}{\sqrt{\pi \times 3.5 \times 10^9 \times 4\pi \times 10^{-7} \times 5.8 \times 10^7}}
$$

$$
\delta_s = \frac{1}{\sqrt{3.5 \times 4 \times 5.8 \times \pi^2 \times 10^9 \times 10^{-7} \times 10^7}} = \frac{1}{\sqrt{3.5 \times 4 \times 5.8 \times 9.8696 \times 10^9}}
$$

$$
\delta_s = \frac{1}{\sqrt{801.7 \times 10^9}} = \frac{1}{895.4 \times 10^3} = 1.117 \times 10^{-6} \text{ m} = 1.117 \ \mu\text{m}
$$

For a microstrip patch, a common approximation for $Q_c$ is:

$$
Q_c = \frac{h}{\delta_s} = \frac{0.00152}{1.117 \times 10^{-6}} = 1361
$$

#### Step 3: Radiation quality factor

Given: $Q_r \approx 30$ (typical for this geometry).

#### Step 4: Total quality factor

$$
\frac{1}{Q_T} = \frac{1}{Q_r} + \frac{1}{Q_c} + \frac{1}{Q_d} = \frac{1}{30} + \frac{1}{1361} + \frac{1}{370.4}
$$

$$
\frac{1}{Q_T} = 0.03333 + 0.000735 + 0.002699 = 0.03676
$$

$$
Q_T = \frac{1}{0.03676} = 27.2
$$

**VSWR $\le 2$ bandwidth:**

$$
BW = \frac{1}{Q_T \sqrt{2}} = \frac{0.7071}{27.2} = 0.0260 = 2.60\%
$$

#### Step 5: Radiation efficiency

$$
\eta = \frac{Q_T}{Q_r} = \frac{27.2}{30} = 0.907 = 90.7\%
$$

The antenna is radiation-efficient, with only 9.3% of input power lost to conductor and dielectric losses.

---

### Exercise 4: Input Impedance and Feed Location

**Problem:** A rectangular microstrip patch has dimensions $L = 28.0$ mm, $W = 36.0$ mm on a substrate with $\epsilon_r = 2.2$, $h = 1.6$ mm. The edge input resistance is $R_{\text{in}}(0) = 280\ \Omega$. Find the probe feed location $y_0$ (measured from the radiating edge) required to match a $50\ \Omega$ feed.

**Solution:**

The input resistance at a distance $y_0$ from the edge is:

$$
R_{\text{in}}(y_0) = R_{\text{in}}(0) \cos^2\left( \frac{\pi y_0}{L} \right)
$$

Set $R_{\text{in}}(y_0) = 50\ \Omega$:

$$
50 = 280 \cos^2\left( \frac{\pi y_0}{L} \right)
$$

$$
\cos^2\left( \frac{\pi y_0}{L} \right) = \frac{50}{280} = 0.1786
$$

$$
\cos\left( \frac{\pi y_0}{L} \right) = \sqrt{0.1786} = 0.4226
$$

$$
\frac{\pi y_0}{L} = \arccos(0.4226) = 1.134 \text{ rad}
$$

$$
y_0 = \frac{1.134}{\pi} \times L = 0.3610 \times 28.0 = 10.11 \text{ mm}
$$

The probe should be placed 10.11 mm from the radiating edge of the patch.

**Check:** The center of the patch is at $y = L/2 = 14.0$ mm. The feed at $y_0 = 10.11$ mm is 3.89 mm from the center. At the center, $R_{\text{in}} = 0$ (null), so the feed must be offset from the centerline of the resonant dimension.

---

### Exercise 5: Two-Element Microstrip Array Pattern

**Problem:** Two identical rectangular patches, each with an H-plane beamwidth of $70^\circ$, are placed in a linear array along the $x$-axis with spacing $d = 0.7\lambda_0$ at 5 GHz. The patches are fed with equal amplitude and in phase.
1. Calculate the array factor.
2. Determine the grating lobe condition.
3. Sketch the total H-plane pattern (array factor $\times$ element pattern).
4. If the array is scanned to $\theta_0 = 30^\circ$, what phase shift $\beta$ is required?
5. At scan angle $\theta_0 = 30^\circ$, will a grating lobe appear?

**Solution:**

#### Step 1: Array factor

For two isotropic elements with spacing $d$ and phase shift $\beta = 0$:

$$
AF(\theta) = \cos\left( \frac{\psi}{2} \right), \quad \psi = k_0 d \sin\theta + \beta
$$

where $k_0 = 2\pi/\lambda_0$.

With $\beta = 0$ and $d = 0.7\lambda_0$:

$$
\psi = \frac{2\pi}{\lambda_0} \times 0.7\lambda_0 \times \sin\theta = 1.4\pi \sin\theta
$$

$$
AF(\theta) = \cos(0.7\pi \sin\theta)
$$

#### Step 2: Grating lobe condition

Grating lobes appear when the argument of the array factor produces multiple main-beam maxima. For a two-element array, the condition for the first grating lobe is:

$$
\frac{d}{\lambda_0} \ge 1.0 \quad \text{for broadside}
$$

Since $d = 0.7\lambda_0 < \lambda_0$, no grating lobe exists at broadside ($\beta = 0$).

#### Step 3: Total H-plane pattern

The element pattern of a rectangular patch in the H-plane ($xz$-plane) is approximately:

$$
E_{\text{elem}}(\theta) = \cos\theta \cdot \frac{\sin(k_0 W\sin\theta/2)}{k_0 W\sin\theta/2}
$$

where $W$ is the patch width. For a $70^\circ$ beamwidth, $W \approx 0.5\lambda_0$.

The normalized element factor at H-plane is approximately:

$$
E_{\text{elem}}(\theta) \approx \cos\theta \cdot \text{sinc}(k_0 W\sin\theta/2)
$$

The total pattern is $E_{\text{total}}(\theta) = \cos(0.7\pi \sin\theta) \cdot \cos\theta \cdot \text{sinc}(0.5\pi \sin\theta)$.

#### Step 4: Scan phase shift

For beam scanning to $\theta_0 = 30^\circ$:

$$
\beta = -k_0 d \sin\theta_0 = -\frac{2\pi}{\lambda_0} \times 0.7\lambda_0 \times \sin 30^\circ
$$

$$
\beta = -2\pi \times 0.7 \times 0.5 = -0.7\pi \text{ rad} = -126^\circ
$$

The negative sign indicates that element 2 must lag element 1 by $126^\circ$ in phase.

#### Step 5: Grating lobe at $\theta_0 = 30^\circ$

The grating lobe condition for a scanned array is:

$$
\frac{d}{\lambda_0} \ge \frac{1}{1 + |\sin\theta_0|}
$$

With $\theta_0 = 30^\circ$, $\sin 30^\circ = 0.5$:

$$
\frac{d}{\lambda_0} \ge \frac{1}{1 + 0.5} = \frac{1}{1.5} = 0.667
$$

Since $d/\lambda_0 = 0.7 > 0.667$, **a grating lobe will appear** at:

$$
\sin\theta_g = \sin\theta_0 - \frac{\lambda_0}{d} = 0.5 - \frac{1}{0.7} = 0.5 - 1.4286 = -0.9286
$$

$$
\theta_g = -68.2^\circ
$$

A grating lobe appears at $-68.2^\circ$ from broadside, with an amplitude equal to the main beam.

> **[Key Insight]** The condition $d/\lambda_0 < 1/(1 + |\sin\theta_0|)$ is critical for grating-lobe-free scanning in arrays. For $\pm 30^\circ$ scan, the element spacing must be $d < 0.667\lambda_0$.

---

### Exercise 6: Circular Polarization with Truncated Corners

**Problem:** A square microstrip patch ($L = W = 30$ mm) on a substrate with $\epsilon_r = 2.55$, $h = 1.57$ mm resonates at 3.1 GHz. The measured $Q_T = 25$. Determine the amount of corner truncation $\Delta s$ (length of each truncated corner) required to produce circular polarization.

**Solution:**

#### Step 1: Perturbation theory for CP

For a nearly square patch, CP is achieved when the two orthogonal $TM_{010}$ modes (one along $L$, one along $W$) are excited with equal amplitude and $90^\circ$ phase difference. With truncated corners, the two resonant frequencies are split. The condition for CP is:

$$
\frac{\Delta f}{f_r} = \frac{1}{Q_T}
$$

where $\Delta f = |f_{r1} - f_{r2}|$ is the frequency splitting.

#### Step 2: Relating truncation to frequency split

For truncated corners of side $\Delta s$ (each of the four corners is cut by a right isosceles triangle of legs $\Delta s$):

The perturbation area is the sum of the truncated corner areas: $A_{\text{pert}} = 2(\Delta s)^2$ (since each of the four corners has area $(\Delta s)^2/2$, and the total is $4 \times (\Delta s)^2/2 = 2(\Delta s)^2$).

The frequency splitting for a square patch ($L = W$) with corner truncation is:

$$
\frac{\Delta f}{f_r} = \frac{2(\Delta s)^2}{A_{\text{patch}}}
$$

where $A_{\text{patch}} = L^2 = W^2$.

#### Step 3: Solve for $\Delta s$

Set $\Delta f/f_r = 1/Q_T = 1/25 = 0.04$:

$$
\frac{2(\Delta s)^2}{30^2} = 0.04
$$

$$
2(\Delta s)^2 = 0.04 \times 900 = 36
$$

$$
(\Delta s)^2 = 18
$$

$$
\Delta s = \sqrt{18} = 4.24 \text{ mm}
$$

Each corner should be truncated by cutting off a right isosceles triangle with legs of 4.24 mm.

#### Step 4: Verification

The axial ratio (AR) at the design frequency can be estimated:

$$
AR = \sqrt{\frac{1 + \sqrt{1 + (Q_T \Delta f/f_r)^{-2}}}{1 - \sqrt{1 + (Q_T \Delta f/f_r)^{-2}}}}
$$

Since $Q_T \cdot \Delta f/f_r = 25 \times 0.04 = 1$, this is the ideal ratio for perfect CP (AR = 0 dB theoretically at the design frequency).

> **[Supplementary]** In practice, the truncation must be tuned through electromagnetic simulation because the simple perturbation formula neglects fringing field effects at the truncated corners. A typical design procedure is to start with $\Delta s \approx L/(6Q_T)$ and optimize via simulation.

---

### Exercise 7: Aperture-Coupled Patch

**Problem:** An aperture-coupled microstrip patch antenna uses a slot of length $L_s = 12$ mm and width $W_s = 1$ mm in the ground plane. The patch is on the top substrate ($\epsilon_{r1} = 2.2$, $h_1 = 0.787$ mm) and the feed line is on the bottom substrate ($\epsilon_{r2} = 3.55$, $h_2 = 0.508$ mm). The patch is a square of side 20 mm.
1. What is the approximate resonant frequency of the patch?
2. How does the slot length affect coupling?
3. Estimate the backlobe level relative to the main beam (qualitative).

**Solution:**

#### Step 1: Resonant frequency

The resonant frequency of a square patch ($L = W = 20$ mm) on substrate $\epsilon_{r1} = 2.2$, $h_1 = 0.787$ mm:

First compute effective parameters:

$$
\epsilon_{\text{reff}} = \frac{2.2 + 1}{2} + \frac{2.2 - 1}{2} \left[ 1 + 12 \frac{0.787}{20} \right]^{-1/2}
$$

$$
\epsilon_{\text{reff}} = 1.6 + 0.6 \times [1 + 0.4722]^{-1/2} = 1.6 + 0.6 \times [1.4722]^{-1/2}
$$

$$
\epsilon_{\text{reff}} = 1.6 + 0.6 \times 0.8242 = 1.6 + 0.4945 = 2.095
$$

$$
\frac{\Delta L}{h} = 0.412 \frac{(2.095 + 0.3)(20/0.787 + 0.264)}{(2.095 - 0.258)(20/0.787 + 0.8)}
$$

$$
\frac{20}{0.787} = 25.41
$$

$$
\frac{\Delta L}{h} = 0.412 \frac{2.395 \times 25.674}{1.837 \times 26.21} = 0.412 \frac{61.49}{48.15} = 0.412 \times 1.277 = 0.526
$$

$$
\Delta L = 0.526 \times 0.787 = 0.414 \text{ mm}
$$

$$
L_{\text{eff}} = 20 + 2 \times 0.414 = 20.828 \text{ mm}
$$

$$
f_r = \frac{c_0}{2L_{\text{eff}} \sqrt{\epsilon_{\text{reff}}}} = \frac{3 \times 10^8}{2 \times 0.020828 \times \sqrt{2.095}}
$$

$$
f_r = \frac{3 \times 10^8}{0.041656 \times 1.4474} = \frac{3 \times 10^8}{0.06029}
$$

$$
f_r = 4.976 \times 10^9 \approx 4.98 \text{ GHz}
$$

#### Step 2: Effect of slot length

The slot acts as a resonant coupling element. Maximum coupling occurs when the slot is resonant, which requires $L_s \approx \lambda_g/2$ where $\lambda_g$ is the guided wavelength in the slot environment.

For the slot in the ground plane between two dielectrics, the effective dielectric constant is approximately:

$$
\epsilon_{r,\text{slot}} \approx \frac{\epsilon_{r1} + \epsilon_{r2}}{2} = \frac{2.2 + 3.55}{2} = 2.875
$$

The resonant slot length is:

$$
L_{s,\text{res}} = \frac{c_0}{2f_r \sqrt{\epsilon_{r,\text{slot}}}} = \frac{3 \times 10^8}{2 \times 4.98 \times 10^9 \times \sqrt{2.875}}
$$

$$
L_{s,\text{res}} = \frac{0.03012}{\sqrt{2.875}} = \frac{0.03012}{1.696} = 0.01776 \text{ m} = 17.76 \text{ mm}
$$

The given slot length $L_s = 12$ mm is shorter than the resonant length, so the coupling will be weaker but the operational bandwidth may be wider because the slot is not resonant (coupling is more gradual with frequency).

#### Step 3: Backlobe level

The slot in the ground plane radiates in both directions. The forward radiation couples to the patch, while the backward radiation forms the backlobe. The backlobe level depends on:

- The slot size (larger slots $\to$ more backward radiation).
- The ground plane size (larger ground plane $\to$ reduced diffraction at edges).
- The substrate thickness on the feed side (thicker $\to$ more backlobe).

For an aperture-coupled patch with a slot of $L_s = 12$ mm at 5 GHz ($0.2\lambda_0$), the backlobe is typically 10--15 dB below the main beam for a moderate ground plane ($\approx 3\lambda_0$). The exact level requires full-wave simulation.

---

### Exercise 8: Proximity-Coupled Patch Bandwidth Enhancement

**Problem:** A proximity-coupled microstrip patch achieves a bandwidth of 0.8% with $h = 0.5$ mm on $\epsilon_r = 10.2$ substrate. By switching to a thicker substrate ($h = 1.5$ mm, same $\epsilon_r$) and optimizing the feed line position, by what factor does the bandwidth approximately increase? What effect does this have on surface wave losses?

**Solution:**

#### Step 1: Bandwidth scaling with substrate thickness

The bandwidth of a microstrip patch is approximately proportional to the substrate thickness (for $h/\lambda_0$ up to approximately 0.03, beyond which surface waves dominate):

$$
BW \propto \frac{h}{\lambda_0}
$$

Increasing $h$ from 0.5 mm to 1.5 mm (factor of 3):

$$
BW_{\text{new}} \approx BW_{\text{old}} \times \frac{h_{\text{new}}}{h_{\text{old}}} = 0.8\% \times 3 = 2.4\%
$$

#### Step 2: Surface wave effects

The cutoff frequency for the $TE_1$ surface wave is:

$$
f_c = \frac{c_0}{4h\sqrt{\epsilon_r - 1}}
$$

For $h = 0.5$ mm ($\epsilon_r = 10.2$):

$$
f_c = \frac{3 \times 10^8}{4 \times 0.0005 \times \sqrt{10.2 - 1}} = \frac{3 \times 10^8}{0.002 \times \sqrt{9.2}} = \frac{3 \times 10^8}{0.002 \times 3.033}
$$

$$
f_c = \frac{3 \times 10^8}{0.006066} = 4.95 \times 10^{10} = 49.5 \text{ GHz}
$$

For $h = 1.5$ mm:

$$
f_c = \frac{3 \times 10^8}{4 \times 0.0015 \times 3.033} = \frac{3 \times 10^8}{0.01820} = 16.5 \text{ GHz}
$$

If the operating frequency is above 16.5 GHz, the $TE_1$ surface wave mode is above cutoff and will be excited, reducing the antenna efficiency. If the operating frequency is below 16.5 GHz, the $TE_1$ mode is below cutoff and does not propagate, but the $TM_0$ mode (which has no cutoff) will still carry surface wave power. The surface wave efficiency loss increases with $h/\lambda_0$.

> **[Supplementary]** The surface wave efficiency $\eta_{sw}$ for a patch on a grounded dielectric substrate can be approximated by:
>
> $$
> \eta_{sw} \approx 1 - \frac{1}{1 + \frac{4\pi h}{\lambda_0} \cdot \frac{\epsilon_r^{3/2}}{(\epsilon_r - 1)(\epsilon_r + 1)}}
> $$
>
> For $\epsilon_r = 10.2$, $h/\lambda_0 = 0.015$ ($h = 1.5$ mm at 3 GHz), $\eta_{sw} \approx 0.92$, meaning approximately 8% of the radiated power goes into surface waves. For the thinner substrate ($h/\lambda_0 = 0.005$), $\eta_{sw} \approx 0.97$, with only 3% surface wave loss.

---

### Exercise 9: Corporate Feed Network for a 4x4 Array

**Problem:** Design a corporate feed network for a $4 \times 4$ microstrip patch array operating at 10 GHz on a substrate with $\epsilon_r = 2.2$, $h = 0.254$ mm. Each patch has an input impedance of 200 $\Omega$ (edge-fed). The system impedance is 50 $\Omega$. Determine:
1. The impedance transformation required at each power division level.
2. The number of T-junction dividers needed.
3. The quarter-wave transformer impedances at the first division level.
4. The total line loss if each power divider introduces 0.1 dB loss and the total feed line length is $20\lambda_g$.

**Solution:**

#### Step 1: Impedance transformation requirements

The array has a $4 \times 4$ configuration. Each row of 4 patches is fed by a 1-to-4 power divider, and the 4 rows are combined by another 1-to-4 power divider.

**Level 1 (row feed):** 4 patches in parallel, each 200 $\Omega$. The combined impedance at the row feed point (all 4 in parallel):

$$
Z_{\text{row}} = \frac{200}{4} = 50\ \Omega
$$

This is already matched to 50 $\Omega$! No transformer needed at the last division level if each patch is 200 $\Omega$ and the row has 4 patches.

**Level 2 (column feed):** 4 rows, each presenting 50 $\Omega$ at the feed point. Combined:

$$
Z_{\text{array}} = \frac{50}{4} = 12.5\ \Omega
$$

The array feed point impedance is 12.5 $\Omega$, which must be transformed to 50 $\Omega$.

#### Step 2: Number of T-junction dividers

Total dividers needed:
- 4 row dividers (one per row): each is a 1-to-4 divider.
- 1 column divider: combines 4 rows.

For 1-to-4: need 3 two-way dividers (a binary tree: 1 $\to$ 2 $\to$ 4).

Total two-way dividers: $4 \times 3 + 3 = 15$ T-junction dividers.

#### Step 3: Quarter-wave transformer for array impedance

The 12.5 $\Omega$ to 50 $\Omega$ transformation at the array feed point:

$$
Z_{\text{QW}} = \sqrt{Z_{\text{in}} \times Z_{\text{out}}} = \sqrt{12.5 \times 50} = \sqrt{625} = 25\ \Omega
$$

The quarter-wave transformer has impedance 25 $\Omega$.

Length of the quarter-wave section:

$$
\lambda_g = \frac{\lambda_0}{\sqrt{\epsilon_{\text{reff}}}} \approx \frac{30\ \text{mm}}{\sqrt{2.2}} = 20.22 \text{ mm}
$$

$$
L_{\text{QW}} = \frac{\lambda_g}{4} = 5.06 \text{ mm}
$$

The required microstrip line width for 25 $\Omega$ on the given substrate can be found from microstrip impedance formulas. For $\epsilon_r = 2.2$, $h = 0.254$ mm, a 25 $\Omega$ line is quite wide (approximately $W_{25} \approx 1.2$ mm).

#### Step 4: Total line loss

Each divider: 0.1 dB loss. 15 dividers $\to$ 1.5 dB loss.

Feed line length: $20\lambda_g = 20 \times 20.22 = 404.4$ mm.

Microstrip line loss on RT/Duroid 5880 at 10 GHz is approximately 0.05 dB/cm for a 50 $\Omega$ line:

$$
\text{Line loss} = 0.05 \times 40.44 = 2.02 \text{ dB}
$$

**Total feed network loss:** $1.5 + 2.02 = 3.52$ dB.

If each patch has 6 dBi gain, the array gain before feed loss is:

$$
G_{\text{array}} = G_{\text{elem}} + 10\log_{10}(16) = 6 + 12.0 = 18.0 \text{ dBi}
$$

After feed loss: $G_{\text{total}} = 18.0 - 3.52 = 14.48$ dBi.

> **[Supplementary]** The feed network loss is a critical design consideration for large arrays. At higher frequencies (above 10 GHz), corporate feed losses can dominate, and series-fed arrays or reflectarrays may be preferred to reduce feed path lengths.

---

### Exercise 10: Dual-Band Operation Using a Stacked Patch

**Problem:** A stacked microstrip patch antenna consists of a lower patch (driven) and an upper parasitic patch (stacked). The lower patch is on a substrate with $\epsilon_{r1} = 2.2$, $h_1 = 1.57$ mm, and $L_1 = 38$ mm, $W_1 = 45$ mm. The upper patch is on a foam layer ($\epsilon_{r2} \approx 1.05$, $h_2 = 5$ mm) with $L_2 = 42$ mm, $W_2 = 50$ mm.
1. Estimate the two resonant frequencies.
2. Estimate the bandwidth improvement over a single patch.
3. Determine the approximate separation between the two resonances.

**Solution:**

#### Step 1: Resonant frequencies

**Lower patch (driven):** The lower patch resonates at a frequency determined primarily by its own dimensions and the lower substrate.

$$
\epsilon_{\text{reff},1} \approx \frac{2.2 + 1}{2} + \frac{2.2 - 1}{2} \left[ 1 + 12 \frac{1.57}{45} \right]^{-1/2}
$$

$$
\frac{h_1}{W_1} = \frac{1.57}{45} = 0.0349
$$

$$
\epsilon_{\text{reff},1} = 1.6 + 0.6 \times [1 + 12 \times 0.0349]^{-1/2} = 1.6 + 0.6 \times [1.4188]^{-1/2}
$$

$$
\epsilon_{\text{reff},1} = 1.6 + 0.6 \times 0.8395 = 1.6 + 0.5037 = 2.104
$$

$$
\frac{\Delta L_1}{h_1} = 0.412 \frac{(2.104 + 0.3)(45/1.57 + 0.264)}{(2.104 - 0.258)(45/1.57 + 0.8)}
$$

$$
\frac{45}{1.57} = 28.66
$$

$$
\frac{\Delta L_1}{h_1} = 0.412 \frac{2.404 \times 28.924}{1.846 \times 29.46} = 0.412 \frac{69.53}{54.38} = 0.412 \times 1.279 = 0.527
$$

$$
\Delta L_1 = 0.527 \times 1.57 = 0.827 \text{ mm}
$$

$$
L_{\text{eff},1} = 38 + 2 \times 0.827 = 39.654 \text{ mm}
$$

$$
f_{r1} = \frac{c_0}{2L_{\text{eff},1} \sqrt{\epsilon_{\text{reff},1}}} = \frac{3 \times 10^8}{2 \times 0.039654 \times \sqrt{2.104}}
$$

$$
f_{r1} = \frac{3 \times 10^8}{0.079308 \times 1.451} = \frac{3 \times 10^8}{0.1151} = 2.606 \text{ GHz}
$$

**Upper patch (parasitic):** The upper patch is on a low-dielectric foam ($\epsilon_{r2} \approx 1.05$). The effective dielectric constant will be close to 1.05.

$$
\epsilon_{\text{reff},2} \approx \frac{1.05 + 1}{2} + \frac{1.05 - 1}{2} \left[ 1 + 12 \frac{5}{50} \right]^{-1/2}
$$

$$
\epsilon_{\text{reff},2} = 1.025 + 0.025 \times [1 + 1.2]^{-1/2} = 1.025 + 0.025 \times [2.2]^{-1/2}
$$

$$
\epsilon_{\text{reff},2} = 1.025 + 0.025 \times 0.6742 = 1.025 + 0.0169 = 1.042
$$

The fringing correction is small for the low $\epsilon_r$ foam substrate. Approximating:

$$
f_{r2} \approx \frac{c_0}{2L_2 \sqrt{\epsilon_{\text{reff},2}}} = \frac{3 \times 10^8}{2 \times 0.042 \times \sqrt{1.042}}
$$

$$
f_{r2} = \frac{3 \times 10^8}{0.084 \times 1.021} = \frac{3 \times 10^8}{0.08576} = 3.498 \text{ GHz}
$$

#### Step 2: Bandwidth improvement

A single patch on the lower substrate ($h = 1.57$ mm, $\epsilon_r = 2.2$) at 2.6 GHz has:

$$
\frac{h}{\lambda_0} = \frac{0.00157}{0.1154} = 0.0136
$$

A typical bandwidth for a patch with $h/\lambda_0 \approx 0.014$ on $\epsilon_r = 2.2$ is approximately 2.0% (VSWR $\le 2$).

For the stacked configuration, the two resonances merge into a single wider impedance bandwidth. The total bandwidth can be estimated as approximately the sum of the individual bandwidths plus the separation between the resonances, provided the resonances are close enough to overlap.

With $f_{r1} = 2.606$ GHz and $f_{r2} = 3.498$ GHz, the separation is 892 MHz. This is too large for the two bands to merge into a single wide band. Instead, the stacked patch will exhibit **dual-band** behavior with two distinct operating bands.

#### Step 3: Separation between resonances

The frequency separation:

$$
\Delta f = f_{r2} - f_{r1} = 3.498 - 2.606 = 0.892 \text{ GHz} = 892 \text{ MHz}
$$

The fractional separation:

$$
\frac{\Delta f}{f_{\text{center}}} = \frac{0.892}{3.052} = 29.2\%
$$

This is a large separation. The two bands will be distinct:
- Lower band: approximately 2.5--2.7 GHz (centered at 2.606 GHz).
- Upper band: approximately 3.4--3.6 GHz (centered at 3.498 GHz).

> **[Supplementary]** To merge the two resonances into a single wide band, the patch sizes should be chosen such that the resonant frequencies are within approximately 10%--15% of each other. The lower patch size should be larger (resonating at a lower frequency), and the upper patch smaller (higher frequency), with the upper patch being parasitically coupled to the lower driven patch. By adjusting the foam thickness $h_2$, the coupling between the patches can be optimized for maximum bandwidth.

---

## Connections and Cross-References

- **Section 2 (Fundamental Parameters of Antennas):** Definitions of directivity, gain, bandwidth, polarization, and input impedance are directly applied to microstrip antenna characterization.
- **Section 3 (Radiation Integrals):** The vector potential method developed in Section 3 is used to derive the far-field patterns of microstrip patches.
- **Section 6 (Arrays: Linear, Planar, and Circular):** Microstrip patch arrays use the array factor formulation developed in Section 6. Corporate and series feed networks rely on array techniques.
- **Section 8 (Integral Equations, Moment Method):** Accurate analysis of microstrip antennas beyond the cavity model requires full-wave method of moments (MoM) solutions.
- **Section 9 (Broadband Dipoles and Matching Techniques):** Matching techniques from Section 9 apply to microstrip feeds. The folded dipole is related to the microstrip inverted-F antenna.
- **Section 12 (Aperture Antennas):** The aperture coupling method for microstrip antennas uses a slot aperture -- the radiation equations from Section 12 apply directly to the coupling slot analysis.
- **Section 13 (Horn Antennas):** Stacked patches and horn antennas both use multiple resonators to achieve broadband operation.
- **Section 15 (Reflector Antennas):** Microstrip patch arrays are commonly used as feeds for reflector antennas, especially in array-fed reflector systems.
- **Section 17 (Antenna Measurements):** The measurement techniques in Section 17 apply fully to microstrip antennas, including pattern, gain, impedance, and polarization measurements.

*Prerequisites: Section 2 (Fundamental Parameters), Section 3 (Radiation Integrals), Section 4 (Linear Wire Antennas -- slot equivalence).*

---

## Exam Tip: Microstrip Antennas

1. **Cavity Model Shortcut:** For a rectangular patch, the dominant mode is $TM_{010}$ (when $L > W$). The resonant frequency is approximately $f_r \approx c_0/(2L\sqrt{\epsilon_r})$, and the width is $W \approx (c_0/2f_r)\sqrt{2/(\epsilon_r+1)}$. Always apply fringing correction for accurate results.

2. **Bandwidth Estimation:** The VSWR $\le 2$ bandwidth of a microstrip patch is approximately $BW \approx 0.707/Q_T$. Since $Q_T$ is dominated by $Q_r$ (radiation loss) for low-loss substrates, a quick estimate is $BW \approx 3.5(h/\lambda_0)$ for $\epsilon_r \approx 2.2$, and $BW \approx 2.0(h/\lambda_0)$ for $\epsilon_r \approx 10$.

3. **Impedance Matching Rule:** The patch input resistance varies as $\cos^2(\pi y_0/L)$ along the resonant dimension. The edge resistance is typically 100--400 $\Omega$. To match to 50 $\Omega$, the feed is placed approximately $0.3L$--$0.4L$ from the edge.

4. **Surface Wave Limit:** For substrates with $\epsilon_r > 2.5$, surface waves become significant when $h/\lambda_0 > 0.03$. The surface wave efficiency $\eta_{sw}$ degrades rapidly beyond this limit. For high-efficiency designs, keep $h \le 0.02\lambda_0/\sqrt{\epsilon_r}$.

5. **Circular Polarization by Truncation:** The corner truncation for CP in a square patch is approximately $\Delta s \approx L/(6Q_T)$. For $Q_T \approx 25$--$50$, $\Delta s \approx L/150$ to $L/300$. The truncated corners must be on opposite diagonal pairs to excite orthogonal modes.

6. **Grating Lobe Rule (Arrays):** For a broadside beam without grating lobes, $d/\lambda_0 < 1$. For scanning to $\theta_0$, the condition is $d/\lambda_0 < 1/(1 + |\sin\theta_0|)$. The first grating lobe appears at $\theta_g = \arcsin(\sin\theta_0 - \lambda_0/d)$.

7. **Dielectric Constant Trade-off:** Low $\epsilon_r$ ($2.2$--$3.5$) gives wider bandwidth and higher efficiency but larger patch size. High $\epsilon_r$ ($10$--$12$) gives smaller patches but narrower bandwidth and more surface wave loss. For MMIC integration (GaAs, $\epsilon_r = 12.9$), the patch is very small but bandwidth is typically $< 2\%$.

8. **Feed Network Loss:** In corporate-fed arrays, the feed loss can be estimated as $L_{\text{feed}} \approx \alpha \cdot N \cdot \bar{d}$, where $\alpha$ is the line attenuation constant, $N$ is the number of elements, and $\bar{d}$ is the average line length per element. For arrays larger than $8 \times 8$, feed loss can exceed 3 dB at $X$-band.

---

*This file covers Section 14 (Microstrip Antennas) as listed in the Signal Propagation mindmap, following the Type C (Engineering and Applied Science) content standard with 10 fully worked exercises spanning rectangular and circular patch design, quality factor analysis, impedance matching, array design, circular polarization, aperture coupling, proximity coupling, corporate feed networks, and stacked patch dual-band operation.*