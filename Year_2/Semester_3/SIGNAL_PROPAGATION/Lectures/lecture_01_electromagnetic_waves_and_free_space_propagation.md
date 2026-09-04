# Lecture 01: Electromagnetic Waves and Free-Space Propagation

This lecture covers the electromagnetic foundation of radio wave propagation, Maxwell's equations, wave impedance, the Poynting vector, wave polarization, and the mathematical derivation of the Friis transmission equation.

---

## 1. Maxwell's Equations and the Helmholtz Wave Equation

In a linear, isotropic, homogeneous, source-free dielectric medium, electromagnetic fields satisfy Maxwell's curl equations:

$$
\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t} = -j\omega \mu \mathbf{H}
$$
$$
\nabla \times \mathbf{H} = \mathbf{J} + \frac{\partial \mathbf{D}}{\partial t} = j\omega \epsilon \mathbf{E}
$$

Taking the curl of both sides of Faraday's Law and utilizing the vector identity $\nabla \times (\nabla \times \mathbf{E}) = \nabla(\nabla \cdot \mathbf{E}) - \nabla^2 \mathbf{E}$ yields the **Vector Helmholtz Wave Equation**:

$$
\nabla^2 \mathbf{E} + k^2 \mathbf{E} = 0
$$

where the wavenumber $k$ and propagation constant $\beta$ in a lossless medium are:
$$
k = \omega \sqrt{\mu \epsilon} = \frac{2\pi}{\lambda}
$$

In free space ($\epsilon_0 \approx 8.854 \times 10^{-12}\text{ F/m}$, $\mu_0 = 4\pi \times 10^{-7}\text{ H/m}$):
- Phase velocity: $c = \frac{1}{\sqrt{\mu_0 \epsilon_0}} \approx 3 \times 10^8\text{ m/s}$.
- Intrinsic impedance of free space:
  $$
  \eta_0 = \sqrt{\frac{\mu_0}{\epsilon_0}} \approx 120\pi \approx 376.73\,\Omega \approx 377\,\Omega
  $$

---

## 2. Poynting Vector and Radiated Power Density

The instantaneous spatial flow of electromagnetic power per unit area is quantified by the **Poynting Vector** $\mathbf{S}$:

$$
\mathbf{S} = \mathbf{E} \times \mathbf{H} \quad [\text{W/m}^2]
$$

For time-harmonic fields, the time-averaged power density vector $\mathbf{W}_{\text{avg}}$ is:
$$
\mathbf{W}_{\text{avg}} = \frac{1}{2} \text{Re}\left\{ \mathbf{E} \times \mathbf{H}^* \right\}
$$

For a transverse electromagnetic (TEM) spherical wave propagating radially outward:
$$
\mathbf{W}_{\text{avg}}(r, \theta, \phi) = \frac{|\mathbf{E}(r, \theta, \phi)|^2}{2\eta_0} \hat{\mathbf{a}}_r
$$

---

## 3. Wave Polarization

Polarization describes the time-varying spatial orientation of the electric field vector $\mathbf{E}$ at a fixed point in space:

1. **Linear Polarization:** The electric field vector oscillates along a fixed straight line over time. Occurs when orthogonal field components $E_x$ and $E_y$ have zero phase difference ($\Delta \phi = 0$ or $\pi$).
2. **Circular Polarization:** The electric field tip traces a circle in the transverse plane over time. Requires equal magnitudes ($|E_x| = |E_y|$) and a quadrature phase difference ($\Delta \phi = \pm \frac{\pi}{2}$).
   - **RHCP (Right-Hand Circular):** Field rotates clockwise along propagation direction.
   - **LHCP (Left-Hand Circular):** Field rotates counter-clockwise.
3. **Elliptical Polarization:** The general state where orthogonal components have unequal amplitudes and an arbitrary phase difference.

---

## 4. Free-Space Path Loss and Friis Transmission Equation

Consider a transmitter emitting total power $P_t$ through an antenna with gain $G_t$. At distance $R$, the power density is:

$$
W_t = \frac{P_t G_t}{4\pi R^2} \quad [\text{W/m}^2]
$$

A receiving antenna with effective aperture $A_r$ captures power $P_r$:
$$
P_r = W_t \cdot A_r = \frac{P_t G_t A_r}{4\pi R^2}
$$

Using the fundamental relationship between effective aperture and antenna gain $A_r = \frac{\lambda^2}{4\pi} G_r$:

$$
P_r = P_t G_t G_r \left( \frac{\lambda}{4\pi R} \right)^2
$$

This is the **Friis Transmission Equation**.

### 4.1 Free-Space Path Loss (FSPL)
The path loss factor $\text{FSPL}$ represents the isotropic geometric attenuation:

$$
\text{FSPL} = \left(\frac{4\pi R}{\lambda}\right)^2 = \left(\frac{4\pi f R}{c}\right)^2
$$

Expressed in decibels ($\text{dB}$):
$$
\text{FSPL}_{[\text{dB}]} = 20 \log_{10}(R) + 20 \log_{10}(f) + 20 \log_{10}\left(\frac{4\pi}{c}\right)
$$
For distance $R$ in kilometers and frequency $f$ in megahertz:
$$
\text{FSPL}_{[\text{dB}]} = 32.44 + 20 \log_{10}(R_{[\text{km}]}) + 20 \log_{10}(f_{[\text{MHz}]})
$$

---

## 5. Summary

- Electromagnetic waves propagate at speed $c$ in free space with intrinsic impedance $\eta_0 \approx 377\,\Omega$.
- The Poynting vector calculates real power density transmitted through space.
- The Friis formula quantifies wireless link received power as an inverse-square law function of distance and frequency.

