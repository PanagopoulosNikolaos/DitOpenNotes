# Practice Exam 01: Signal Propagation and Antenna Systems

**Course:** Signal Propagation (Course Code 304)  
**Format:** Comprehensive Practice Examination with Full Solutions  
**Total Points:** 100 points  
**Time Allowed:** 120 minutes  

---

## Part I: Examination Questions

### Section A: Electromagnetic Propagation & Polarization (20 Points)

1. *(10 Points)* A uniform plane wave propagating in free space has electric field:
   $$\mathbf{E}(z, t) = 12 \cos(\omega t - \beta z) \hat{\mathbf{a}}_x + 12 \sin(\omega t - \beta z) \hat{\mathbf{a}}_y \quad [\text{V/m}]$$
   - Identify the frequency $f$ and wavenumber $\beta$ if the wavelength is $\lambda = 20\text{ cm}$.
   - Determine the wave's polarization state (Linear, RHCP, or LHCP). Justify with an orientation sketch.
   - Calculate the time-average Poynting vector $\mathbf{W}_{\text{avg}}$ in $\text{W/m}^2$.
2. *(10 Points)* State the intrinsic impedance of free space $\eta_0$ in terms of permittivity $\epsilon_0$ and permeability $\mu_0$. How does wave impedance change when propagating through a lossless non-magnetic dielectric with relative permittivity $\epsilon_r = 4.0$?

---

### Section B: Antenna Directivity and Efficiency (25 Points)

An antenna has normalized radiation intensity:
$$U(\theta, \phi) = \begin{cases} \cos^2\theta \sin\theta, & 0 \le \theta \le \pi/2, \quad 0 \le \phi \le 2\pi \\ 0, & \text{elsewhere} \end{cases}$$

1. *(10 Points)* Determine the total radiated power $P_{\text{rad}}$ and maximum directivity $D_0$ in dimensionless units and in $\text{dBi}$.
2. *(15 Points)* The antenna has radiation resistance $R_{\text{rad}} = 50\,\Omega$, loss resistance $R_{\text{loss}} = 5\,\Omega$, and is connected to a matched $50\,\Omega$ feed line.
   - Compute the radiation efficiency $\eta_{cd}$.
   - Compute the absolute gain $G_0$ in $\text{dBi}$.
   - Compute the reflection coefficient $\Gamma$ and the actual power radiated when $P_{\text{gen}} = 200\text{ W}$.

---

### Section C: Wire Antennas & Image Theory (25 Points)

1. *(15 Points)* An isolated center-fed half-wave dipole ($l = \lambda/2$) carries peak current $I_0 = 3\text{ A}$.
   - State the radiation resistance $R_{\text{rad}}$ of the half-wave dipole.
   - Compute the electric field amplitude $|E_\theta|$ at broadside ($\theta = 90^\circ$) at distance $r = 5\text{ km}$.
2. *(10 Points)* A vertical quarter-wave monopole ($l = \lambda/4$) is mounted on an infinite ground plane.
   - Using Image Theory, derive the radiation resistance of the monopole from the dipole value.
   - If $100\text{ W}$ is radiated by the monopole, what is the power density $W_{\text{rad}}$ at distance $r = 5\text{ km}$ along the ground plane ($\theta = 90^\circ$)?

---

### Section D: Antenna Arrays and Phased Beam Steering (30 Points)

A 6-element Uniform Linear Array ($N = 6$) has inter-element spacing $d = \frac{\lambda}{2}$ oriented along the $z$-axis.

1. *(10 Points)* Write down the normalized array factor $|\text{AF}_n(\psi)|$. For a broadside array ($\beta = 0$), determine the First-Null Beamwidth ($\text{FNBW}$) in degrees.
2. *(10 Points)* Calculate the progressive phase excitation $\beta$ required to electronically steer the main beam to angle $\theta_0 = 60^\circ$.
3. *(10 Points)* What is the maximum inter-element spacing $d_{\max}$ that prevents grating lobes from entering the visible space for all scan angles $\theta_0 \in [30^\circ, 150^\circ]$?

---

## Part II: Complete Solutions and Grading Rubric

### Section A Solutions

1. **Plane Wave & Polarization (10 Points):**
   - $\lambda = 0.20\text{ m}$.
     $$f = \frac{c}{\lambda} = \frac{3 \times 10^8}{0.20} = 1.5 \times 10^9\text{ Hz} = 1.5\text{ GHz}$$
     $$\beta = \frac{2\pi}{\lambda} = \frac{2\pi}{0.20} = 10\pi\text{ rad/m} \approx 31.42\text{ rad/m}$$
     *(3 pts)*
   - Both components have equal amplitude ($E_{0x} = E_{0y} = 12\text{ V/m}$).
     At $z = 0$: $E_x(t) = 12 \cos(\omega t)$, $E_y(t) = 12 \sin(\omega t) = 12 \cos(\omega t - \pi/2)$.
     $E_y$ lags $E_x$ by $90^\circ$. Looking along the $+z$ propagation direction, the vector rotates clockwise as time advances. Therefore, the wave is **Right-Hand Circularly Polarized (RHCP)**. *(4 pts)*
   - Time-average Poynting vector:
     $$\mathbf{W}_{\text{avg}} = \frac{|\mathbf{E}|^2}{2\eta_0} \hat{\mathbf{a}}_z = \frac{12^2 + 12^2}{2 \times 377} \hat{\mathbf{a}}_z = \frac{288}{754} \hat{\mathbf{a}}_z \approx 0.382\text{ W/m}^2 \hat{\mathbf{a}}_z$$
     *(3 pts)*

2. **Intrinsic Impedance (10 Points):**
   - In free space: $\eta_0 = \sqrt{\frac{\mu_0}{\epsilon_0}} \approx 120\pi \approx 377\,\Omega$. *(4 pts)*
   - In medium with $\epsilon_r = 4.0$, $\mu_r = 1.0$:
     $$\eta = \sqrt{\frac{\mu_0}{\epsilon_r \epsilon_0}} = \frac{\eta_0}{\sqrt{\epsilon_r}} = \frac{376.73}{\sqrt{4}} = \frac{376.73}{2} \approx 188.37\,\Omega$$
     The intrinsic impedance is halved. *(6 pts)*

---

### Section B Solutions

1. **Radiated Power and Directivity (10 Points):**
   $$U(\theta, \phi) = \cos^2\theta \sin\theta, \quad 0 \le \theta \le \pi/2$$
   $$P_{\text{rad}} = \int_{0}^{2\pi} \int_{0}^{\pi/2} \cos^2\theta \sin\theta \cdot \sin\theta \, d\theta \, d\phi = 2\pi \int_{0}^{\pi/2} \cos^2\theta \sin^2\theta \, d\theta$$
   Using $\sin(2\theta) = 2\sin\theta\cos\theta$:
   $$\cos^2\theta \sin^2\theta = \frac{1}{4}\sin^2(2\theta) = \frac{1}{8}(1 - \cos(4\theta))$$
   $$\int_{0}^{\pi/2} \frac{1}{8}(1 - \cos(4\theta)) \, d\theta = \frac{1}{8} \left[ \theta - \frac{\sin(4\theta)}{4} \right]_0^{\pi/2} = \frac{1}{8}\left(\frac{\pi}{2}\right) = \frac{\pi}{16}$$
   $$P_{\text{rad}} = 2\pi \cdot \frac{\pi}{16} = \frac{\pi^2}{8} \approx 1.2337\text{ W}$$
   Maximum of $U(\theta)$:
   $\frac{d}{d\theta}[\cos^2\theta \sin\theta] = -2\cos\theta\sin^2\theta + \cos^3\theta = \cos\theta(\cos^2\theta - 2\sin^2\theta) = 0$.
   $\tan^2\theta = 0.5 \implies \tan\theta = \frac{1}{\sqrt{2}} \implies \sin\theta = \frac{1}{\sqrt{3}}, \cos\theta = \sqrt{\frac{2}{3}}$.
   $$U_{\max} = \left(\frac{2}{3}\right) \cdot \frac{1}{\sqrt{3}} = \frac{2}{3\sqrt{3}} \approx 0.3849$$
   Directivity:
   $$D_0 = \frac{4\pi U_{\max}}{P_{\text{rad}}} = \frac{4\pi \left(\frac{2}{3\sqrt{3}}\right)}{\frac{\pi^2}{8}} = \frac{64}{3\sqrt{3}\pi} \approx 3.918$$
   $$D_{0[\text{dBi}]} = 10\log_{10}(3.918) \approx 5.93\text{ dBi}$$
   *(10 pts)*

2. **Efficiency, Gain, and Reflections (15 Points):**
   - Radiation efficiency:
     $$\eta_{cd} = \frac{R_{\text{rad}}}{R_{\text{rad}} + R_{\text{loss}}} = \frac{50}{50 + 5} = \frac{50}{55} = \frac{10}{11} \approx 0.9091 \quad (90.91\%)$$
     *(5 pts)*
   - Gain:
     $$G_0 = \eta_{cd} D_0 = 0.9091 \times 3.918 \approx 3.562$$
     $$G_{0[\text{dBi}]} = 10\log_{10}(3.562) \approx 5.52\text{ dBi}$$
     *(5 pts)*
   - Input impedance: $Z_{\text{in}} = 50 + 5 = 55\,\Omega$.
     $$\Gamma = \frac{55 - 50}{55 + 50} = \frac{5}{105} \approx 0.0476$$
     Power accepted by antenna:
     $$P_{\text{in}} = P_{\text{gen}}(1 - |\Gamma|^2) = 200(1 - 0.00227) \approx 199.55\text{ W}$$
     Radiated power:
     $$P_{\text{rad}} = \eta_{cd} P_{\text{in}} = 0.9091 \times 199.55 \approx 181.41\text{ W}$$
     *(5 pts)*

---

### Section C Solutions

1. **Half-Wave Dipole (15 Points):**
   - $R_{\text{rad}} \approx 73.13\,\Omega$. *(5 pts)*
   - Broadside field at $r = 5\text{ km}$:
     $$|E_\theta| = \frac{\eta_0 I_0}{2\pi r} = \frac{120\pi \times 3.0}{2\pi \times 5000} = \frac{360\pi}{10,000\pi} = \frac{360}{10,000} = 0.036\text{ V/m} = 36\text{ mV/m}$$
     *(10 pts)*

2. **Quarter-Wave Monopole (10 Points):**
   - By Image Theory, the field in the upper hemisphere is identical to a dipole, but fields in the lower hemisphere are zero.
     Total radiated power is halved for the same current: $P_{\text{rad, mono}} = \frac{1}{2} P_{\text{rad, dipole}} \implies R_{\text{rad, mono}} = \frac{73.13}{2} \approx 36.56\,\Omega$. *(5 pts)*
   - Power density on ground plane:
     Monopole directivity is $D_0 = 2 \times 1.643 = 3.286$.
     $$W_{\text{rad}} = \frac{P_{\text{rad}} D_0}{4\pi r^2} = \frac{100 \times 3.286}{4\pi \times (5000)^2} = \frac{328.6}{3.1416 \times 10^8} \approx 1.046 \times 10^{-6}\text{ W/m}^2 = 1.05\,\mu\text{W/m}^2$$
     *(5 pts)*

---

### Section D Solutions

1. **Array Factor & Broadside FNBW (10 Points):**
   $$|\text{AF}_n(\psi)| = \left| \frac{\sin(3\psi)}{6\sin(\psi/2)} \right|, \quad \psi = \pi\cos\theta$$
   Nulls occur where $3\psi = \pm \pi \implies \psi = \pm \frac{\pi}{3}$.
   $$\pi\cos\theta = \pm \frac{\pi}{3} \implies \cos\theta = \pm \frac{1}{3}$$
   $$\theta_{\text{null, 1}} = \arccos(1/3) \approx 70.53^\circ, \quad \theta_{\text{null, 2}} = \arccos(-1/3) \approx 109.47^\circ$$
   $$\text{FNBW} = 109.47^\circ - 70.53^\circ = 38.94^\circ$$
   *(10 pts)*

2. **Steering Phase for $\theta_0 = 60^\circ$ (10 Points):**
   $$\psi = kd\cos\theta_0 + \beta = 0 \implies \pi \cos(60^\circ) + \beta = 0$$
   $$\pi(0.5) + \beta = 0 \implies \beta = -\frac{\pi}{2}\text{ rad} = -90^\circ$$
   *(10 pts)*

3. **Grating Lobe Elimination (10 Points):**
   To eliminate grating lobes for any scan angle within $[\theta_{\min}, \theta_{\max}]$:
   $$\frac{d}{\lambda} < \frac{1}{1 + |\cos\theta_0|_{\max}}$$
   The maximum $|\cos\theta_0|$ in $[30^\circ, 150^\circ]$ is $\cos(30^\circ) = \frac{\sqrt{3}}{2} \approx 0.866$.
   $$\frac{d_{\max}}{\lambda} < \frac{1}{1 + 0.866} = \frac{1}{1.866} \approx 0.5359$$
   $$d_{\max} < 0.536\,\lambda$$
   *(10 pts)*

