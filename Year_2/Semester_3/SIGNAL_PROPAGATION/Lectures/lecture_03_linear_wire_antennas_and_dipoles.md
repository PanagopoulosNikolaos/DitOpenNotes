# Lecture 03: Linear Wire Antennas and Dipoles

This lecture analyzes linear wire antennas, establishing current distribution models, deriving far-zone radiated electric and magnetic fields, calculating radiation resistance, and evaluating half-wave dipoles and quarter-wave monopoles using Image Theory.

---

## 1. The Infinitesimal (Hertzian) Dipole

An infinitesimal dipole is a linear wire of length $l \ll \lambda$ carrying a uniform current $I(z') = I_0$.

### 1.1 Vector Potential and Far Fields
Aligning the dipole along the $z$-axis, the magnetic vector potential in the far-field is:
$$
A_z = \frac{\mu I_0 l e^{-jkr}}{4\pi r}
$$

Converting to spherical coordinates ($A_\theta = -A_z \sin\theta$) yields the far-field radiation:
$$
E_\theta = j \eta_0 \frac{k I_0 l e^{-jkr}}{4\pi r} \sin\theta
$$
$$
H_\phi = \frac{E_\theta}{\eta_0} = j \frac{k I_0 l e^{-jkr}}{4\pi r} \sin\theta
$$

### 1.2 Radiated Power and Radiation Resistance
The time-average power density is:
$$
W_{\text{rad}} = \frac{1}{2\eta_0} |E_\theta|^2 = \frac{\eta_0 k^2 I_0^2 l^2}{32\pi^2 r^2} \sin^2\theta
$$

Integrating over the sphere to obtain total radiated power $P_{\text{rad}}$:
$$
P_{\text{rad}} = \int_{0}^{2\pi} \int_{0}^{\pi} W_{\text{rad}} r^2 \sin\theta \, d\theta \, d\phi = \frac{\eta_0 k^2 I_0^2 l^2}{12\pi}
$$

Using $P_{\text{rad}} = \frac{1}{2} I_0^2 R_{\text{rad}}$, the **radiation resistance** is:
$$
R_{\text{rad}} = \frac{2 P_{\text{rad}}}{I_0^2} = \frac{\eta_0 k^2 l^2}{6\pi} = 80\pi^2 \left( \frac{l}{\lambda} \right)^2 \quad [\Omega]
$$
- Maximum Directivity: $D_0 = 1.5 = 1.76\text{ dBi}$.
- Half-Power Beamwidth (HPBW): $90^\circ$.

---

## 2. Finite-Length Dipole

For thin wire antennas with length $l$ comparable to $\lambda$, current vanishes at the ends ($z' = \pm l/2$) and is modeled accurately by a standing wave sinusoidal distribution:

$$
I(z') = I_0 \sin\left( k \left(\frac{l}{2} - |z'|\right) \right), \quad -l/2 \le z' \le l/2
$$

Evaluating the far-field radiation integral gives the electric field:
$$
E_\theta \approx j \eta_0 \frac{I_0 e^{-jkr}}{2\pi r} \left[ \frac{\cos\left(\frac{kl}{2}\cos\theta\right) - \cos\left(\frac{kl}{2}\right)}{\sin\theta} \right]
$$

---

## 3. The Half-Wave Dipole ($l = \lambda / 2$)

For a dipole of total length $l = \frac{\lambda}{2}$, $kl = \frac{2\pi}{\lambda} \frac{\lambda}{2} = \pi$:

$$
E_\theta = j \eta_0 \frac{I_0 e^{-jkr}}{2\pi r} \left[ \frac{\cos\left(\frac{\pi}{2}\cos\theta\right)}{\sin\theta} \right]
$$

### 3.1 Performance Metrics:
- **Radiation Resistance:**
  $$R_{\text{rad}} = \frac{\eta_0}{2\pi} \text{Cin}(2\pi) \approx 73.13\,\Omega$$
- **Input Impedance (at resonance with slight shortening $\sim 0.48\lambda$):**
  $$Z_{\text{in}} \approx 73 + j42.5\,\Omega \quad \longrightarrow \quad Z_{\text{in, resonant}} \approx 70 + j0\,\Omega$$
- **Maximum Directivity:**
  $$D_0 \approx 1.643 = 2.15\text{ dBi}$$
- **Half-Power Beamwidth (HPBW):**
  $$\text{HPBW} \approx 78^\circ$$

---

## 4. Quarter-Wave Monopole on Ground Plane

By **Image Theory**, a vertical antenna of length $l = \frac{\lambda}{4}$ mounted on an infinite, perfectly conducting ground plane radiates only into the upper hemisphere ($0 \le \theta \le \pi/2$), forming a virtual image below the ground.

```
       Monopole (l = lambda/4)
               |
   ============+============ Ground Plane (z = 0)
               :
         Virtual Image
```

Because radiation exists only in the upper hemisphere ($2\pi$ steradians instead of $4\pi$):
- Total radiated power is halved: $P_{\text{rad, mono}} = \frac{1}{2} P_{\text{rad, dipole}}$.
- Radiation resistance is halved:
  $$R_{\text{rad, mono}} = \frac{1}{2} R_{\text{rad, dipole}} \approx \frac{73.13}{2} \approx 36.56\,\Omega$$
- Input impedance:
  $$Z_{\text{in, mono}} = \frac{1}{2} Z_{\text{in, dipole}} \approx 36.5 + j21.25\,\Omega$$
- Directivity is doubled:
  $$D_{\text{0, mono}} = 2 \cdot D_{\text{0, dipole}} \approx 3.286 = 5.16\text{ dBi}$$

