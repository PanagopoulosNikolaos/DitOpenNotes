# University of Ioannina - Department of Informatics and Telecommunications
## Course: Signal Propagation (Course Code: 304)
### Academic Year: 2025-2026
### Synthetic Final Examination Solutions - Paper 01

---

### Solution 1: Electromagnetic Wave Propagation, Lossy Media & Polarization (25 Marks)

#### Part A: Propagation in a Lossy Dielectric (13 Marks)
Operating parameters:
- $f = 900\text{ MHz} \implies \omega = 2\pi(900 \times 10^6) \approx 5.6549 \times 10^9\text{ rad/s}$
- $\mu_r = 1.0 \implies \mu = \mu_0 = 4\pi \times 10^{-7}\text{ H/m}$
- $\epsilon_r = 4.0 \implies \epsilon = 4.0 \times 8.854 \times 10^{-12} \approx 3.5416 \times 10^{-11}\text{ F/m}$
- $\sigma = 0.05\text{ S/m}$

1. **Loss Tangent Classification:**
   $$\tan\delta = \frac{\sigma}{\omega \epsilon} = \frac{0.05}{(5.6549 \times 10^9) \times (3.5416 \times 10^{-11})} = \frac{0.05}{0.20028} \approx 0.2497$$
   Because $0.01 < \tan\delta < 10$, the material falls between an ideal low-loss dielectric and a good conductor. It is classified as a **lossy (quasi-conducting) dielectric medium**.

2. **Propagation Constants:**
   The general formulas for a lossy non-magnetic medium are:
   $$\alpha = \omega \sqrt{\frac{\mu\epsilon}{2}} \left[ \sqrt{1 + \left(\frac{\sigma}{\omega\epsilon}\right)^2} - 1 \right]^{1/2}$$
   $$\beta = \omega \sqrt{\frac{\mu\epsilon}{2}} \left[ \sqrt{1 + \left(\frac{\sigma}{\omega\epsilon}\right)^2} + 1 \right]^{1/2}$$
   Baseline factor:
   $$\omega \sqrt{\mu\epsilon} = \frac{\omega}{c}\sqrt{\epsilon_r} = \frac{2\pi (900 \times 10^6)}{3 \times 10^8} \times 2 = 12\pi \approx 37.6991\text{ rad/m}$$
   Loss term: $\sqrt{1 + (\tan\delta)^2} = \sqrt{1 + 0.2497^2} = \sqrt{1.06235} \approx 1.0307$.
   - **Attenuation Constant $\alpha$:**
     $$\alpha = 37.6991 \times \sqrt{\frac{1.0307 - 1}{2}} = 37.6991 \times \sqrt{0.01535} \approx 4.670\text{ Np/m}$$
     $$\alpha_{[\text{dB/m}]} = 8.686 \times \alpha = 8.686 \times 4.670 \approx 40.56\text{ dB/m}$$
   - **Phase Constant $\beta$:**
     $$\beta = 37.6991 \times \sqrt{\frac{1.0307 + 1}{2}} = 37.6991 \times \sqrt{1.01535} \approx 37.988\text{ rad/m}$$
   - **Phase Velocity and Wavelength:**
     $$v_p = \frac{\omega}{\beta} = \frac{5.6549 \times 10^9}{37.988} \approx 1.4886 \times 10^8\text{ m/s}$$
     $$\lambda = \frac{2\pi}{\beta} = \frac{2\pi}{37.988} \approx 0.1654\text{ m} = 16.54\text{ cm}$$

3. **Skin Depth & Complex Intrinsic Impedance:**
   - **Skin depth:**
     $$\delta_s = \frac{1}{\alpha} = \frac{1}{4.670} \approx 0.2141\text{ m} = 21.41\text{ cm}$$
   - **Intrinsic Impedance:**
     $$|\eta_c| = \frac{\sqrt{\mu/\epsilon}}{\left[1 + (\tan\delta)^2\right]^{1/4}} = \frac{376.73 / \sqrt{4.0}}{(1.06235)^{1/4}} = \frac{188.37}{1.0152} \approx 185.55\,\Omega$$
     $$\theta_\eta = \frac{1}{2}\arctan(\tan\delta) = \frac{1}{2}\arctan(0.2497) \approx 7.01^\circ$$
     $$\eta_c = 185.55 e^{j 7.01^\circ} \approx 184.16 + j 22.64\,\Omega$$

4. **Attenuation Distance to $1\text{ V/m}$:**
   $$E(z_1) = E_0 e^{-\alpha z_1} \implies 1 = 100 e^{-4.670 z_1} \implies 4.670 z_1 = \ln(100) \approx 4.6052$$
   $$z_1 = \frac{4.6052}{4.670} \approx 0.986\text{ m} = 98.6\text{ cm}$$

---

#### Part B: Polarization Analysis & Axial Ratio (12 Marks)
Given:
$$\mathbf{E}(z, t) = 15 \cos(\omega t - \beta z) \hat{\mathbf{a}}_x + 20 \cos\left(\omega t - \beta z + \frac{2\pi}{3}\right) \hat{\mathbf{a}}_y$$

1. **Phasor Representation:**
   $$\tilde{\mathbf{E}}(z) = \left( 15 \hat{\mathbf{a}}_x + 20 e^{j 2\pi/3} \hat{\mathbf{a}}_y \right) e^{-j\beta z} \quad [\text{V/m}]$$

2. **Polarization State:**
   Amplitudes are unequal ($E_{0x} = 15 \ne E_{0y} = 20$), and the phase difference is $\delta = \phi_y - \phi_x = \frac{2\pi}{3} = 120^\circ$ (which is neither an integer multiple of $\pi$ nor $\pm \pi/2$ with equal amplitudes). Hence, the wave is **Elliptically Polarized**.

3. **Sense of Rotation:**
   Examine field evolution at observation plane $z = 0$:
   - At $\omega t = 0$: $E_x = 15$, $E_y = 20 \cos(120^\circ) = -10$. Vector position: $(15, -10)$ (Quadrant IV).
   - At $\omega t = \pi/2$ ($90^\circ$): $E_x = 0$, $E_y = 20 \cos(210^\circ) \approx -17.32$. Vector position: $(0, -17.32)$.
   - At $\omega t = \pi$ ($180^\circ$): $E_x = -15$, $E_y = 20 \cos(300^\circ) = +10$. Vector position: $(-15, 10)$ (Quadrant II).
   Looking in the direction of wave propagation ($+z$), the tip of the vector traces an ellipse moving in a **clockwise** direction. Under IEEE standard definitions, this corresponds to **Right-Handed Elliptical Polarization (RHEP)**.

4. **Axial Ratio (AR):**
   Using the semi-axis equations for an ellipse:
   $$OA, OB = \sqrt{\frac{1}{2} \left[ E_{0x}^2 + E_{0y}^2 \pm \sqrt{E_{0x}^4 + E_{0y}^4 + 2E_{0x}^2 E_{0y}^2 \cos(2\delta)} \right]}$$
   - $E_{0x}^2 + E_{0y}^2 = 225 + 400 = 625$.
   - $\cos(2\delta) = \cos(240^\circ) = -0.5$.
   - $\Delta = \sqrt{225^2 + 400^2 + 2(225)(400)(-0.5)} = \sqrt{50625 + 160000 - 90000} = \sqrt{120625} \approx 347.31$.
   - Major semi-axis $OA$:
     $$OA = \sqrt{\frac{625 + 347.31}{2}} = \sqrt{486.155} \approx 22.05\text{ V/m}$$
   - Minor semi-axis $OB$:
     $$OB = \sqrt{\frac{625 - 347.31}{2}} = \sqrt{138.845} \approx 11.78\text{ V/m}$$
   - Axial Ratio:
     $$\text{AR} = \frac{OA}{OB} = \frac{22.05}{11.78} \approx 1.872$$
     $$\text{AR}_{[\text{dB}]} = 20 \log_{10}(1.872) \approx 5.45\text{ dB}$$

---

### Solution 2: Radiation Intensity, Directivity & Satellite Link Budget (25 Marks)

#### Part A: Radiation Pattern & Directivity Integration (13 Marks)
Given:
$$U(\theta, \phi) = B_0 \cos^3\theta \sin^2\phi, \quad 0 \le \theta \le \frac{\pi}{2}, \quad 0 \le \phi \le \pi$$

1. **Peak Coordinates:**
   Maximum occurs when $\cos\theta = 1 \implies \theta_{\max} = 0\text{ rad}$ and $\sin\phi = 1 \implies \phi_{\max} = \frac{\pi}{2}\text{ rad}$.
   $$U_{\max} = B_0 (1)^3 (1)^2 = B_0$$

2. **Total Radiated Power:**
   $$P_{\text{rad}} = \int_{0}^{\pi} \sin^2\phi \, d\phi \int_{0}^{\pi/2} B_0 \cos^3\theta \sin\theta \, d\theta$$
   - Integral over $\phi$: $\int_{0}^{\pi} \sin^2\phi \, d\phi = \frac{\pi}{2}$.
   - Integral over $\theta$: substitute $u = \cos\theta \implies du = -\sin\theta \, d\theta$:
     $$\int_{0}^{\pi/2} \cos^3\theta \sin\theta \, d\theta = \int_{0}^{1} u^3 \, du = \left[ \frac{u^4}{4} \right]_0^1 = \frac{1}{4}$$
   $$P_{\text{rad}} = B_0 \left(\frac{\pi}{2}\right) \left(\frac{1}{4}\right) = \frac{\pi}{8} B_0 \approx 0.3927 B_0\text{ W}$$

3. **Maximum Directivity:**
   $$D_0 = \frac{4\pi U_{\max}}{P_{\text{rad}}} = \frac{4\pi B_0}{\frac{\pi}{8} B_0} = 32 \quad (\text{dimensionless})$$
   $$D_{0[\text{dBi}]} = 10 \log_{10}(32) \approx 15.05\text{ dBi}$$

4. **Half-Power Beamwidth (HPBW):**
   In elevation plane $\phi = \pi/2$, $\sin^2(\pi/2) = 1$:
   $$U(\theta, \pi/2) = B_0 \cos^3\theta$$
   Set to half maximum: $\cos^3\theta_{1/2} = 0.5 \implies \cos\theta_{1/2} = (0.5)^{1/3} \approx 0.7937$.
   $$\theta_{1/2} = \arccos(0.7937) \approx 37.47^\circ$$
   The full half-power beamwidth is symmetric about broadside:
   $$\text{HPBW} = 2 \theta_{1/2} = 2 \times 37.47^\circ \approx 74.94^\circ$$

---

#### Part B: Friis Satellite Downlink Budget (12 Marks)
Parameters:
- $f = 12\text{ GHz} \implies \lambda = \frac{3 \times 10^8}{12 \times 10^9} = 0.025\text{ m} = 2.5\text{ cm}$
- $d = 3.6 \times 10^7\text{ m}$
- $P_t = 60\text{ W} \implies P_{t[\text{dBm}]} = 10 \log_{10}(60 \times 10^3) \approx 47.78\text{ dBm}$
- $G_t = 43.0\text{ dBi}$
- Dish diameter $D = 1.2\text{ m} \implies$ Area $A_{\text{phys}} = \pi \left(\frac{1.2}{2}\right)^2 \approx 1.1310\text{ m}^2$
- Effective aperture $A_e = \epsilon_{\text{ap}} A_{\text{phys}} = 0.65 \times 1.1310 \approx 0.7351\text{ m}^2$

1. **Free Space Path Loss (FSPL):**
   $$\text{FSPL}_{[\text{dB}]} = 20 \log_{10}\left(\frac{4\pi d}{\lambda}\right) = 20 \log_{10}\left(\frac{4\pi \times 3.6 \times 10^7}{0.025}\right) = 20 \log_{10}(1.80956 \times 10^{10}) \approx 205.15\text{ dB}$$

2. **Ground Station Receiver Antenna Gain:**
   $$G_r = \frac{4\pi A_e}{\lambda^2} = \frac{4\pi \times 0.7351}{(0.025)^2} \approx 14,780.8$$
   $$G_{r[\text{dBi}]} = 10 \log_{10}(14,780.8) \approx 41.70\text{ dBi}$$

3. **Total Received Power:**
   Total miscellaneous losses:
   $$L_{\text{total}} = L_{\text{atm}} + L_{\text{pol}} + L_{\text{rec}} = 1.8 + 0.5 + 1.2 = 3.50\text{ dB}$$
   Friis Link Equation in decibels:
   $$P_{r[\text{dBm}]} = P_{t[\text{dBm}]} + G_{t[\text{dBi}]} + G_{r[\text{dBi}]} - \text{FSPL}_{[\text{dB}]} - L_{\text{total}}$$
   $$P_{r[\text{dBm}]} = 47.78 + 43.00 + 41.70 - 205.15 - 3.50 = -76.17\text{ dBm}$$
   Converting to Watts:
   $$P_r = 10^{\frac{-76.17 - 30}{10}} = 10^{-10.617} \approx 2.415 \times 10^{-11}\text{ W} = 24.15\text{ pW}$$

---

### Solution 3: Wire Antennas, Ground Planes & Impedance Matching (25 Marks)

#### Part A: Dipole, Monopole & Image Theory (13 Marks)

1. **Center-Fed Half-Wave Dipole ($l = \lambda/2$):**
   - Far-zone electric field:
     $$E_\theta(r, \theta) = j \eta_0 \frac{I_0 e^{-j\beta r}}{2\pi r} \left[ \frac{\cos\left(\frac{\pi}{2}\cos\theta\right)}{\sin\theta} \right]$$
   - Radiation resistance: $R_{\text{rad}} \approx 73.13\,\Omega$.
   - Input impedance: $Z_{\text{in}} \approx 73.13 + j 42.5\,\Omega$.
   - **Trimming Rationale:** The ideal $\lambda/2$ dipole possesses an inductive reactance of $+j42.5\,\Omega$. Trimming the physical wire length to approximately $l \approx 0.48\lambda$ to $0.485\lambda$ introduces capacitive foreshortening, neutralizing the imaginary reactance ($X_{\text{in}} = 0$) and resulting in a purely resistive input impedance $Z_{\text{in}} \approx 70\,\Omega$.

2. **Quarter-Wave Monopole on PEC Ground Plane:**
   - **Image Theory:** By the surface equivalence principle, an image current identical in magnitude and direction is induced beneath the PEC plane, forming an effective half-wave dipole radiating exclusively into the upper hemisphere ($z > 0$).
   - **Radiation Resistance:** For the same peak current $I_0$, the electric field in the upper hemisphere is unchanged, while in the lower hemisphere it is zero. Hence, total power radiated is halved:
     $$P_{\text{rad,mono}} = \frac{1}{2} P_{\text{rad,dip}} \implies R_{\text{rad,mono}} = \frac{1}{2} R_{\text{rad,dip}} \approx \frac{73.13}{2} \approx 36.56\,\Omega$$
   - **Directivity:** Because the entire radiated energy is concentrated in half the spatial sphere ($2\pi$ steradians instead of $4\pi$):
     $$D_{\text{mono}} = 2 \times D_{\text{dip}} = 2 \times 1.643 \approx 3.286 \quad (5.17\text{ dBi})$$

---

#### Part B: Quarter-Wave Transformer Matching (12 Marks)
Given: $Z_L = 72\,\Omega$, $Z_0 = 50\,\Omega$, $f_0 = 600\text{ MHz}$, $VF = 0.70$.

1. **Unmatched Metrics:**
   $$\Gamma_L = \frac{Z_L - Z_0}{Z_L + Z_0} = \frac{72 - 50}{72 + 50} = \frac{22}{122} \approx 0.1803$$
   $$\text{VSWR} = \frac{1 + |\Gamma_L|}{1 - |\Gamma_L|} = \frac{1 + 0.1803}{1 - 0.1803} \approx 1.44$$

2. **Quarter-Wave Line Parameters:**
   - **Characteristic Impedance:**
     $$Z_T = \sqrt{Z_0 Z_L} = \sqrt{50 \times 72} = \sqrt{3600} = 60\,\Omega$$
   - **Physical Length:**
     $$\lambda_0 = \frac{c}{f_0} = \frac{3 \times 10^8}{600 \times 10^6} = 0.50\text{ m} = 50\text{ cm}$$
     $$\lambda_g = VF \times \lambda_0 = 0.70 \times 50 = 35.0\text{ cm}$$
     $$l_T = \frac{\lambda_g}{4} = \frac{35.0}{4} = 8.75\text{ cm}$$
   At $f_0$, input impedance matches perfectly: $Z_{\text{in}} = \frac{Z_T^2}{Z_L} = \frac{3600}{72} = 50\,\Omega$, yielding $\Gamma = 0$ and $\text{VSWR} = 1.00$.

3. **Fractional Bandwidth for $\text{VSWR} \le 1.5$:**
   $$\Gamma_m = \frac{1.5 - 1}{1.5 + 1} = \frac{0.5}{2.5} = 0.20$$
   Notice that the unmatched line already has $|\Gamma_L| = 0.1803 < 0.20$ ($\text{VSWR} = 1.44 \le 1.5$). Thus, the condition $\text{VSWR} \le 1.5$ is satisfied across the entire operational band around resonance, providing an ultra-broad fractional bandwidth exceeding $100\%$.

---

### Solution 4: Antenna Arrays & Phased Beam Steering (25 Marks)

Given: $N = 8$, $d = 0.5\lambda \implies \beta d = \left(\frac{2\pi}{\lambda}\right)(0.5\lambda) = \pi\text{ rad}$.

1. **Normalized Array Factor:**
   Composite phase: $\psi = \pi \cos\theta + \alpha_p$.
   $$\text{AF}_n(\psi) = \frac{\sin(N\psi/2)}{N \sin(\psi/2)} = \frac{\sin(4\psi)}{8 \sin(\psi/2)}$$

2. **Broadside Array Characteristics ($\alpha_p = 0$):**
   - **Null Locations:** Nulls occur when the numerator is zero while the denominator is non-zero:
     $$4\psi = m\pi \implies 4\pi \cos\theta_{\text{null}} = m\pi \implies \cos\theta_{\text{null}} = \frac{m}{4} \quad (m = \pm 1, \pm 2, \pm 3)$$
     - $m = \pm 1 \implies \cos\theta = \pm 0.25 \implies \theta = 75.52^\circ, 104.48^\circ$
     - $m = \pm 2 \implies \cos\theta = \pm 0.50 \implies \theta = 60.00^\circ, 120.00^\circ$
     - $m = \pm 3 \implies \cos\theta = \pm 0.75 \implies \theta = 41.41^\circ, 138.59^\circ$
   - **First-Null Beamwidth (FNBW):**
     $$\text{FNBW} = 104.48^\circ - 75.52^\circ = 28.96^\circ \approx 29.0^\circ$$
   - **Half-Power Beamwidth (HPBW):**
     Half power occurs when $4\psi \approx 1.391\text{ rad} \implies \psi \approx 0.3478\text{ rad}$.
     $$\pi \cos\theta \approx 0.3478 \implies \cos\theta \approx 0.1107 \implies \theta \approx 83.64^\circ$$
     $$\text{HPBW} = 2 \times (90^\circ - 83.64^\circ) = 12.72^\circ$$

3. **Progressive Phase Shift for Beam Steering:**
   The main beam peak occurs when $\psi = 0 \implies \beta d \cos\theta_0 + \alpha_p = 0 \implies \alpha_p = -\pi \cos\theta_0$.
   - For $\theta_0 = 45^\circ$:
     $$\alpha_p = -\pi \cos(45^\circ) = -\frac{\pi}{\sqrt{2}} \approx -2.221\text{ rad} \approx -127.28^\circ$$
   - For end-fire $\theta_0 = 0^\circ$:
     $$\alpha_p = -\pi \cos(0^\circ) = -\pi\text{ rad} = -180.00^\circ$$

4. **Grating Lobe Suppression Condition:**
   Grating lobes emerge when $\psi = \pm 2\pi$. The visible range of $\psi$ is $\psi \in [-\beta d + \alpha_p, \, \beta d + \alpha_p]$.
   Substituting $\alpha_p = -\beta d \cos\theta_0$, the condition to avoid grating lobes in visible space for any scan angle $\theta_0$ is:
   $$\beta d (1 + |\cos\theta_0|) < 2\pi \implies \frac{d}{\lambda} < \frac{1}{1 + |\cos\theta_0|_{\max}}$$
   For the scan range $\theta_0 \in [45^\circ, 135^\circ]$:
   $$|\cos\theta_0|_{\max} = \cos(45^\circ) = \frac{1}{\sqrt{2}} \approx 0.7071$$
   $$d_{\max} < \frac{\lambda}{1 + 0.7071} = \frac{\lambda}{1.7071} \approx 0.5858\lambda$$
   Therefore, the maximum allowable spacing is $d_{\max} \approx 0.586\lambda$.

