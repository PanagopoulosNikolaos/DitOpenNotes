# Exercises: Dipole Radiation and Antenna Array Factors

This practice problem set provides detailed solutions for half-wave dipole field computations, power capture, and linear array factor synthesis.

---

## Problem 1: Half-Wave Dipole Far-Field and Power Capture

A center-fed half-wave dipole ($l = \lambda/2$) operating at frequency $f = 300\text{ MHz}$ carries a terminal peak current $I_0 = 2.0\text{ A}$.
The dipole is oriented along the $z$-axis in free space.

### Questions:
1. Find the free-space wavelength $\lambda$ and total dipole length $l$.
2. Calculate the electric field amplitude $|E_\theta|$ at a distance $r = 10\text{ km}$ along the broadside horizon ($\theta = 90^\circ$).
3. Find the total power radiated $P_{\text{rad}}$ by the dipole (using $R_{\text{rad}} = 73.13\,\Omega$).
4. A second identical half-wave dipole is situated at $r = 10\text{ km}$, oriented parallel to the transmitting dipole ($\theta = 90^\circ$). Using the Friis transmission formula ($D_0 = 1.643$, $\eta_{cd} = 1.0$), compute the power received $P_r$ in microwatts ($\mu\text{W}$).

---

### Solution to Problem 1

#### 1. Wavelength and Dipole Length:
$$
\lambda = \frac{c}{f} = \frac{3 \times 10^8\text{ m/s}}{300 \times 10^6\text{ Hz}} = 1.0\text{ meter}
$$
Dipole length:
$$
l = \frac{\lambda}{2} = 0.5\text{ meters} = 50\text{ cm}
$$

#### 2. Broadside Electric Field Amplitude:
For a half-wave dipole:
$$
|E_\theta| = \frac{\eta_0 I_0}{2\pi r} \left| \frac{\cos\left(\frac{\pi}{2}\cos\theta\right)}{\sin\theta} \right|
$$
At $\theta = 90^\circ$:
$$
\frac{\cos\left(\frac{\pi}{2}\cos(90^\circ)\right)}{\sin(90^\circ)} = \frac{\cos(0)}{1} = 1.0
$$
$$
|E_\theta| = \frac{120\pi \times 2.0}{2\pi \times 10,000} = \frac{240\pi}{20,000\pi} = \frac{240}{20,000} = 0.012\text{ V/m} = 12\text{ mV/m}
$$

#### 3. Total Radiated Power:
$$
P_{\text{rad}} = \frac{1}{2} I_0^2 R_{\text{rad}} = \frac{1}{2} (2.0)^2 \times 73.13 = \frac{1}{2} \times 4.0 \times 73.13 = 146.26\text{ Watts}
$$

#### 4. Received Power via Friis Formula:
Transmit and receive antenna gains: $G_t = G_r = 1.643$.
$$
P_r = P_t G_t G_r \left(\frac{\lambda}{4\pi r}\right)^2
$$
$$
\frac{\lambda}{4\pi r} = \frac{1.0}{4\pi \times 10,000} = \frac{1}{40,000\pi} \approx 7.9577 \times 10^{-6}
$$
$$
\left(\frac{\lambda}{4\pi r}\right)^2 = (7.9577 \times 10^{-6})^2 \approx 6.3326 \times 10^{-11}
$$
$$
P_r = 146.26 \times (1.643)^2 \times (6.3326 \times 10^{-11}) = 146.26 \times 2.6994 \times 6.3326 \times 10^{-11} \approx 2.4999 \times 10^{-8}\text{ W} = 0.025\,\mu\text{W}
$$

---

## Problem 2: 4-Element Uniform Linear Array Nulls and Steering

A 4-element uniform linear array ($N = 4$) with inter-element spacing $d = \frac{\lambda}{2}$ is aligned along the $z$-axis.

### Questions:
1. Write the normalized array factor $|\text{AF}_n(\psi)|$ as a function of $\psi = kd\cos\theta + \beta$.
2. For a broadside array ($\beta = 0$), determine all values of $\theta$ in $[0^\circ, 180^\circ]$ where nulls occur.
3. What progressive phase shift $\beta$ is required to steer the main beam to end-fire direction $\theta_0 = 0^\circ$?

---

### Solution to Problem 2

#### 1. Array Factor:
$$
|\text{AF}_n(\psi)| = \left| \frac{\sin\left(\frac{4\psi}{2}\right)}{4\sin\left(\frac{\psi}{2}\right)} \right| = \left| \frac{\sin(2\psi)}{4\sin(\psi/2)} \right|
$$

#### 2. Broadside Nulls ($\beta = 0$):
With $d = \lambda/2$, $kd = \frac{2\pi}{\lambda} \frac{\lambda}{2} = \pi$.
$$
\psi = \pi \cos\theta
$$
Nulls occur where $\sin(2\psi) = 0$ while $\sin(\psi/2) \ne 0$:
$$
2\psi = \pm m\pi \implies \psi = \pm \frac{m\pi}{2}, \quad m = 1, 2, 3, \dots \quad (m \ne 0, 4, 8)
$$
Equating $\psi = \pi\cos\theta$:
$$
\pi \cos\theta = \pm \frac{m\pi}{2} \implies \cos\theta = \pm \frac{m}{4}, \quad m = 1, 2, 3
$$
- $m = 1 \implies \cos\theta = \pm 0.25 \implies \theta_1 = \arccos(0.25) \approx 75.52^\circ, \quad \theta_2 = \arccos(-0.25) \approx 104.48^\circ$.
- $m = 2 \implies \cos\theta = \pm 0.50 \implies \theta_3 = \arccos(0.50) = 60.00^\circ, \quad \theta_4 = \arccos(-0.50) = 120.00^\circ$.
- $m = 3 \implies \cos\theta = \pm 0.75 \implies \theta_5 = \arccos(0.75) \approx 41.41^\circ, \quad \theta_6 = \arccos(-0.75) \approx 138.59^\circ$.

The broadside array has 6 nulls in $[0^\circ, 180^\circ]$:
$$
41.41^\circ, \quad 60.00^\circ, \quad 75.52^\circ, \quad 104.48^\circ, \quad 120.00^\circ, \quad 138.59^\circ
$$

#### 3. End-Fire Steering Phase ($\theta_0 = 0^\circ$):
The main beam maximum requires $\psi = 0$ at $\theta_0$:
$$
\psi = kd\cos(0^\circ) + \beta = 0 \implies \pi (1) + \beta = 0 \implies \beta = -\pi\text{ rad} = -180^\circ
$$
Adjacent elements must be driven with alternating opposite phase ($180^\circ$ out-of-phase).

