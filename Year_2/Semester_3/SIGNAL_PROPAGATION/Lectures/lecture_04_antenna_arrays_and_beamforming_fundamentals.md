# Lecture 04: Antenna Arrays and Beamforming Fundamentals

This lecture examines antenna array theory, the pattern multiplication theorem, Uniform Linear Arrays (ULAs), array factor derivation, phased array beam steering, and spatial aliasing (grating lobes).

---

## 1. Motivation for Antenna Arrays

Individual wire antennas produce relatively broad radiation patterns with limited directivity ($D_0 \le 2.15\text{ dBi}$). In long-distance wireless communications, satellite uplinks, and radar systems, high directivity and pencil beams are required.

An **Antenna Array** synthesizes high-gain directional patterns by arranging multiple radiating elements in space and controlling their relative excitation amplitudes and phases.

---

## 2. Pattern Multiplication Theorem

For an array of identical radiating elements with identical spatial orientations:

$$
\mathbf{E}_{\text{total}}(\theta, \phi) = \mathbf{E}_{\text{element}}(\theta, \phi) \times \text{AF}(\theta, \phi)
$$

- **$\mathbf{E}_{\text{element}}(\theta, \phi)$:** Radiation pattern of an individual reference element located at the coordinate origin.
- **$\text{AF}(\theta, \phi)$:** The **Array Factor**, a function purely of array geometry, element positions, relative excitation amplitudes, and progressive phases.

---

## 3. Uniform Linear Arrays (ULA)

Consider an array of $N$ identical elements positioned along the $z$-axis with uniform inter-element spacing $d$, equal excitation amplitudes $a_0 = 1$, and a progressive phase shift $\beta$ between adjacent elements.

```
Element:     0           1           2                     N - 1
             o-----------o-----------o----------- ... ------o
Position:   z=0         z=d         z=2d                 z=(N-1)d
Phase:       0          beta       2*beta               (N-1)*beta
```

### 3.1 Derivation of the Array Factor
Summing the contributions at a far-field observation point:
$$
\text{AF} = 1 + e^{j(kd\cos\theta + \beta)} + e^{j 2(kd\cos\theta + \beta)} + \dots + e^{j (N - 1)(kd\cos\theta + \beta)} = \sum_{n=0}^{N-1} e^{j n \psi}
$$
where $\psi$ is the total phase parameter:
$$
\psi = kd\cos\theta + \beta
$$

Using the finite geometric progression sum formula:
$$
\text{AF} = \frac{1 - e^{j N \psi}}{1 - e^{j \psi}} = e^{j \frac{(N - 1)\psi}{2}} \frac{\sin\left(\frac{N\psi}{2}\right)}{\sin\left(\frac{\psi}{2}\right)}
$$

Normalizing by the maximum value $N$ (occurring at $\psi = 0$):
$$
|\text{AF}_n(\psi)| = \left| \frac{\sin\left(\frac{N\psi}{2}\right)}{N \sin\left(\frac{\psi}{2}\right)} \right|
$$

---

## 4. Array Operation Modes

The maximum of the array factor occurs when $\psi = 0$:
$$
\psi = kd\cos\theta_0 + \beta = 0 \implies \beta = -kd\cos\theta_0
$$

### 4.1 Broadside Array ($\theta_0 = 90^\circ$)
Main beam radiates perpendicular to the array axis:
$$
\beta = -kd\cos(90^\circ) = 0
$$
All elements are excited in phase ($\beta = 0$).

### 4.2 End-Fire Array ($\theta_0 = 0^\circ$ or $180^\circ$)
Main beam radiates along the axis of the array:
- For $\theta_0 = 0^\circ$: $\beta = -kd = -\frac{2\pi d}{\lambda}$.
- For $\theta_0 = 180^\circ$: $\beta = +kd = +\frac{2\pi d}{\lambda}$.

### 4.3 Phased Array (Electronic Beam Steering)
By dynamically adjusting phase shift $\beta$ using electronic phase shifters, the main beam is steered to any desired elevation angle $\theta_0$ without physical mechanical rotation:
$$
\beta(t) = -kd\cos\theta_0(t)
$$

---

## 5. Grating Lobes and Element Spacing

**Grating Lobes** are secondary principal maxima with amplitude equal to the main lobe ($|\text{AF}_n| = 1$). They represent spatial aliasing and waste radiated power in unintended directions.

To avoid grating lobes over all possible scan angles $\theta_0$:
$$
\frac{d}{\lambda} < \frac{1}{1 + |\cos\theta_0|}
$$
For a broadside array ($\theta_0 = 90^\circ$), grating lobes are prevented if $d < \lambda$.  
For an array steered up to end-fire ($\theta_0 = 0^\circ$), grating lobes are prevented if:
$$
d < \frac{\lambda}{2}
$$
Therefore, **half-wavelength spacing ($d = \lambda/2$)** is the standard design benchmark in practical phased array antennas.

