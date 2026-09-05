# University of Ioannina - Department of Informatics and Telecommunications
## Course: Signal Propagation (Course Code: 304)
### Academic Year: 2025-2026
### Synthetic Final Examination - Paper 01

**Time Allowed:** 3 Hours  
**Total Marks:** 100 Points  
**Instructions:**
- Answer all four questions with complete step-by-step mathematical working.
- Use the standard physical constants:
  - Speed of light in vacuum: $c = 3 \times 10^8\text{ m/s}$
  - Permittivity of free space: $\epsilon_0 = 8.854 \times 10^{-12}\text{ F/m}$
  - Permeability of free space: $\mu_0 = 4\pi \times 10^{-7}\text{ H/m}$
  - Intrinsic impedance of free space: $\eta_0 \approx 120\pi \approx 376.73\,\Omega$
- Clearly state all assumptions, coordinate systems, and boundary conditions.

---

### Question 1: Electromagnetic Wave Propagation, Lossy Media & Polarization (25 Marks)

#### Part A: Propagation in a Lossy Dielectric (13 Marks)
A uniform plane wave operating at frequency $f = 900\text{ MHz}$ propagates in the $+z$ direction through a non-magnetic medium ($\mu_r = 1.0$) characterized by relative permittivity $\epsilon_r = 4.0$ and conductivity $\sigma = 0.05\text{ S/m}$.

1. Calculate the loss tangent $\tan\delta = \frac{\sigma}{\omega \epsilon}$. Classify whether the medium behaves as a good dielectric, a good conductor, or a quasi-conducting lossy medium.
2. Calculate the complex propagation constant $\gamma = \alpha + j\beta$:
   - The attenuation constant $\alpha$ in $\text{Np/m}$ and in $\text{dB/m}$.
   - The phase constant $\beta$ in $\text{rad/m}$.
   - The phase velocity $v_p$ in $\text{m/s}$ and the wavelength $\lambda$ in $\text{cm}$.
3. Calculate the skin depth $\delta_s$ and the complex intrinsic impedance $\eta_c = |\eta_c| e^{j\theta_\eta}$.
4. If the electric field amplitude at $z = 0$ is $E_0 = 100\text{ V/m}$, determine the distance $z_1$ where the field amplitude attenuates to $1\text{ V/m}$.

#### Part B: Polarization Analysis & Axial Ratio (12 Marks)
The instantaneous electric field of a wave propagating in free space is given by:
$$\mathbf{E}(z, t) = 15 \cos(\omega t - \beta z) \hat{\mathbf{a}}_x + 20 \cos\left(\omega t - \beta z + \frac{2\pi}{3}\right) \hat{\mathbf{a}}_y \quad [\text{V/m}]$$

1. Express the electric field in phasor form $\tilde{\mathbf{E}}(z)$.
2. Determine the polarization state of the wave (Linear, Circular, or Elliptical).
3. Determine the sense of rotation (Right-Handed or Left-Handed) looking in the direction of propagation ($+z$).
4. Compute the Axial Ratio ($\text{AR}$) of the polarization ellipse in linear terms and in decibels ($\text{dB}$).

---

### Question 2: Radiation Intensity, Directivity & Satellite Link Budget (25 Marks)

#### Part A: Radiation Pattern & Directivity Integration (13 Marks)
An antenna operating at $f = 2.4\text{ GHz}$ has a normalized radiation intensity given by:
$$U(\theta, \phi) = \begin{cases} B_0 \cos^3\theta \sin^2\phi, & 0 \le \theta \le \frac{\pi}{2} \text{ and } 0 \le \phi \le \pi \\ 0, & \text{elsewhere} \end{cases}$$
where $B_0$ is the peak intensity constant.

1. Find the coordinates $(\theta_{\max}, \phi_{\max})$ that maximize $U(\theta, \phi)$, and express $U_{\max}$ in terms of $B_0$.
2. Calculate the total radiated power $P_{\text{rad}}$ by performing the double spherical surface integral:
   $$P_{\text{rad}} = \int_{0}^{2\pi} \int_{0}^{\pi} U(\theta, \phi) \sin\theta \, d\theta \, d\phi$$
3. Calculate the maximum directivity $D_0$ in dimensionless units and in $\text{dBi}$.
4. Determine the Half-Power Beamwidth ($\text{HPBW}$) in the principal elevation plane ($\phi = \pi/2$).

#### Part B: Friis Satellite Downlink Budget (12 Marks)
A geostationary communication satellite at an orbital distance of $d = 36,000\text{ km}$ transmits a downlink signal at carrier frequency $f = 12\text{ GHz}$.

- Transmitter output power: $P_t = 60\text{ W}$
- Transmit antenna gain: $G_t = 43\text{ dBi}$
- Ground station receiver antenna: Parabolic dish of diameter $D_{\text{dish}} = 1.2\text{ m}$ with aperture efficiency $\epsilon_{\text{ap}} = 0.65$
- Atmospheric and rain attenuation: $L_{\text{atm}} = 1.8\text{ dB}$
- Polarization mismatch loss: $L_{\text{pol}} = 0.5\text{ dB}$
- Receiver feed and waveguide loss: $L_{\text{rec}} = 1.2\text{ dB}$

1. Compute the free space wavelength $\lambda$ and Free Space Path Loss ($\text{FSPL}$) in decibels.
2. Calculate the ground station receiver antenna gain $G_r$ in $\text{dBi}$.
3. Formulate the complete Friis link equation in logarithmic form ($\text{dBm}$) and compute the total received power $P_r$ arriving at the low-noise receiver amplifier in both $\text{dBm}$ and Picowatts ($\text{pW}$).

---

### Question 3: Wire Antennas, Ground Planes & Impedance Matching (25 Marks)

#### Part A: Dipole, Monopole & Image Theory (13 Marks)
1. Consider an ideal center-fed half-wave thin wire dipole ($l = \lambda/2$) radiating in free space.
   - Write the far-zone electric field expression $E_\theta(r, \theta)$.
   - State the theoretical radiation resistance $R_{\text{rad}}$ and total input impedance $Z_{\text{in}} = R_{\text{in}} + j X_{\text{in}}$.
   - Explain why practical half-wave dipoles are trimmed to approximately $l \approx 0.48\lambda$ to $0.485\lambda$.
2. A vertical quarter-wave monopole ($l = \lambda/4$) is mounted on an infinite, perfectly electrically conducting (PEC) ground plane ($z = 0$).
   - Using Image Theory, sketch the equivalent structure.
   - Derive the relationship between the radiation resistance of the monopole $R_{\text{rad,mono}}$ and that of the half-wave dipole $R_{\text{rad,dip}}$.
   - Derive the directivity of the monopole $D_{\text{mono}}$ relative to the dipole directivity $D_{\text{dip}}$.

#### Part B: Quarter-Wave Transformer Matching (12 Marks)
A resonant antenna presents a purely resistive load impedance $Z_L = 72\,\Omega$ at its operating frequency $f_0 = 600\text{ MHz}$. It is fed by a standard coaxial transmission line having characteristic impedance $Z_0 = 50\,\Omega$.

1. Compute the voltage reflection coefficient $\Gamma_L$ and the Voltage Standing Wave Ratio ($\text{VSWR}$) on the feed line when directly connected without matching.
2. Design a lossless quarter-wave transmission line section ($l = \lambda_g / 4$) to achieve a perfect match ($\Gamma = 0$) at $f_0$:
   - Calculate the required characteristic impedance $Z_T$ of the transformer line.
   - If the transformer has a dielectric velocity factor $VF = 0.70$, compute the physical length $l_T$ in centimeters.
3. Calculate the fractional bandwidth over which the input $\text{VSWR} \le 1.5$.

---

### Question 4: Antenna Arrays & Phased Beam Steering (25 Marks)

An 8-element Uniform Linear Array ($N = 8$) of isotropic radiators is aligned along the $z$-axis with uniform inter-element spacing $d = 0.5\lambda$.

1. *(6 Marks)* Write the mathematical expression for the normalized array factor $\text{AF}_n(\psi)$ as a function of the composite array phase $\psi = \beta d \cos\theta + \alpha_p$, where $\alpha_p$ is the progressive inter-element phase shift.
2. *(6 Marks)* For a broadside array ($\alpha_p = 0$):
   - Determine all null angles $\theta_{\text{null}}$ in the visible region $0^\circ \le \theta \le 180^\circ$.
   - Calculate the First-Null Beamwidth ($\text{FNBW}$) and the Half-Power Beamwidth ($\text{HPBW}$) in degrees.
3. *(6 Marks)* Calculate the required progressive phase shift $\alpha_p$ (in degrees) to steer the principal maximum of the main beam to:
   - Elevation angle $\theta_0 = 45^\circ$
   - End-fire direction $\theta_0 = 0^\circ$
4. *(7 Marks)* Grating Lobe Suppression:
   - Derive the mathematical condition on inter-element spacing $d/\lambda$ required to guarantee that no grating lobes appear in the visible space for scan angles over the range $\theta_0 \in [45^\circ, 135^\circ]$.
   - Compute the maximum numerical spacing $d_{\max}$ in terms of $\lambda$.

