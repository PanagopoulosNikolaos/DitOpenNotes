# Exercises: Antenna Parameters, Directivity, and Gain

This practice problem set provides step-by-step derivations and numerical evaluations for radiation intensity, beam solid angle, maximum directivity, radiation efficiency, and antenna gain.

---

## Problem 1: Directivity from Radiation Intensity

The radiation intensity of an directional antenna is modeled by:
$$
U(\theta, \phi) = \begin{cases} B_0 \cos^3\theta, & 0 \le \theta \le \frac{\pi}{2}, \quad 0 \le \phi \le 2\pi \\ 0, & \frac{\pi}{2} < \theta \le \pi \end{cases}
$$
where $B_0$ is a constant representing the peak radiation intensity.

### Questions:
1. Find the total radiated power $P_{\text{rad}}$ in terms of $B_0$.
2. Calculate the maximum directivity $D_0$ in dimensionless units and in $\text{dBi}$.
3. Calculate the beam solid angle $\Omega_A$.
4. Determine the Half-Power Beamwidth (HPBW) in degrees.

---

### Solution to Problem 1

#### 1. Radiated Power $P_{\text{rad}}$:
$$
P_{\text{rad}} = \int_{0}^{2\pi} \int_{0}^{\pi/2} B_0 \cos^3\theta \sin\theta \, d\theta \, d\phi
$$
Evaluating the $\phi$ integral:
$$
\int_{0}^{2\pi} d\phi = 2\pi
$$
Evaluating the $\theta$ integral using $u = \cos\theta, du = -\sin\theta d\theta$:
$$
\int_{0}^{\pi/2} \cos^3\theta \sin\theta \, d\theta = \int_{0}^{1} u^3 \, du = \left[ \frac{u^4}{4} \right]_0^1 = \frac{1}{4}
$$
Multiplying:
$$
P_{\text{rad}} = 2\pi B_0 \cdot \frac{1}{4} = \frac{\pi B_0}{2}\text{ W}
$$

#### 2. Maximum Directivity $D_0$:
Peak radiation intensity occurs at $\theta = 0$:
$$
U_{\max} = U(0, \phi) = B_0 \cos^3(0) = B_0
$$
Directivity definition:
$$
D_0 = \frac{4\pi U_{\max}}{P_{\text{rad}}} = \frac{4\pi B_0}{\frac{\pi B_0}{2}} = 4 \times 2 = 8
$$
Expressed in decibels relative to isotropic ($\text{dBi}$):
$$
D_{0[\text{dBi}]} = 10 \log_{10}(8) \approx 9.03\text{ dBi}
$$

#### 3. Beam Solid Angle $\Omega_A$:
$$
\Omega_A = \frac{4\pi}{D_0} = \frac{4\pi}{8} = \frac{\pi}{2} \approx 1.5708\text{ steradians}
$$

#### 4. Half-Power Beamwidth (HPBW):
The half-power points occur where radiation intensity drops to half of maximum:
$$
\cos^3(\theta_{1/2}) = 0.5 \implies \cos(\theta_{1/2}) = (0.5)^{1/3} \approx 0.7937
$$
$$
\theta_{1/2} = \arccos(0.7937) \approx 37.47^\circ
$$
Because the pattern is symmetric around $\theta = 0$, the full beamwidth is:
$$
\text{HPBW} = 2 \times \theta_{1/2} = 2 \times 37.47^\circ \approx 74.94^\circ
$$

---

## Problem 2: Radiation Efficiency and Terminal Power

An antenna has a radiation resistance $R_{\text{rad}} = 68\,\Omega$ and an internal loss resistance $R_{\text{loss}} = 4\,\Omega$. The input reactance is $X_{\text{in}} = 0$ (resonant). The antenna has maximum directivity $D_0 = 6.5\text{ dBi}$.
A transmitter delivers an available power of $100\text{ W}$ through a $50\,\Omega$ transmission line.

### Questions:
1. Compute the radiation efficiency $\eta_{cd}$.
2. Calculate the antenna gain $G_0$ in dimensionless units and in $\text{dBi}$.
3. Calculate the reflection coefficient $\Gamma$ and the total power actually radiated into space $P_{\text{rad}}$.

---

### Solution to Problem 2

#### 1. Radiation Efficiency:
$$
\eta_{cd} = \frac{R_{\text{rad}}}{R_{\text{rad}} + R_{\text{loss}}} = \frac{68}{68 + 4} = \frac{68}{72} \approx 0.9444 \quad (94.44\%)
$$

#### 2. Antenna Gain:
Convert directivity from $\text{dBi}$ to linear scale:
$$
D_0 = 10^{\frac{6.5}{10}} \approx 4.4668
$$
Gain:
$$
G_0 = \eta_{cd} \cdot D_0 = 0.9444 \times 4.4668 \approx 4.2185
$$
In $\text{dBi}$:
$$
G_{0[\text{dBi}]} = 10 \log_{10}(4.2185) \approx 6.25\text{ dBi}
$$
*(Or $G_{0[\text{dBi}]} = D_{0[\text{dBi}]} + 10 \log_{10}(\eta_{cd}) = 6.5 - 0.25 = 6.25\text{ dBi}$).*

#### 3. Terminal Reflection and Radiated Power:
Antenna input impedance: $Z_{\text{in}} = R_{\text{rad}} + R_{\text{loss}} = 72\,\Omega$.
Reflection coefficient relative to $Z_0 = 50\,\Omega$:
$$
\Gamma = \frac{72 - 50}{72 + 50} = \frac{22}{122} \approx 0.1803
$$
Fraction of power reflected:
$$
|\Gamma|^2 = (0.1803)^2 \approx 0.0325 \quad (3.25\%)
$$
Power accepted by antenna terminals:
$$
P_{\text{in}} = P_{\text{trans}} \cdot (1 - |\Gamma|^2) = 100 \times (1 - 0.0325) = 96.75\text{ W}
$$
Total power radiated:
$$
P_{\text{rad}} = \eta_{cd} \cdot P_{\text{in}} = 0.9444 \times 96.75 \approx 91.37\text{ W}
$$

