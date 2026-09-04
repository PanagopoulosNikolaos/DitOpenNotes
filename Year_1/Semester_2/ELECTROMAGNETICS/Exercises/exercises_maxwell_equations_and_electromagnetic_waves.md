# Exercises: Maxwell's Equations and Plane Wave Dynamics

## Context and Grounding
This practice exercise set provides analytical problems and complete solutions covering Maxwell's displacement current, induction in moving circuits, plane wave polarization, and Poynting power flow. It directly reinforces `Lectures/lecture_03_maxwell_equations_and_em_waves.md` and `Exercises/03_test.md`.

---

## Problems

### Problem 1: Displacement Current in a Charging Capacitor
A circular parallel-plate capacitor with plate radius $R = 8\text{ cm}$ and plate separation $d = 2\text{ mm}$ is connected to an AC voltage source:
$$V(t) = 150 \sin(1000\pi t) \quad [\text{V}]$$
The region between the plates is filled with a dielectric of relative permittivity $\varepsilon_r = 3.5$. Neglecting fringing fields:
1. Find the electric field $\mathbf{E}(t)$ between the plates.
2. Determine the displacement current density $\mathbf{J}_D(t)$.
3. Compute the total displacement current $I_D(t)$ through the capacitor and compare it to the conduction current $I_C(t)$ in the connecting wires.
4. Calculate the induced magnetic field magnitude $B(r, t)$ inside the capacitor at radial distance $r < R$.

### Problem 2: Poynting Vector and Radiation Pressure
The electric field of a plane electromagnetic wave traveling in a vacuum in the $+z$ direction is:
$$\mathbf{E}(z, t) = 30 \cos(10^8 \pi t - \beta z) \hat{\mathbf{a}}_x + 40 \sin(10^8 \pi t - \beta z) \hat{\mathbf{a}}_y \quad [\text{V/m}]$$
1. Determine the wave frequency $f$ and phase constant $\beta$.
2. Identify the polarization state of the wave (linear, circular, or elliptical; right-handed or left-handed).
3. Compute the instantaneous and time-averaged Poynting vectors $\mathbf{S}$ and $\mathbf{S}_{\text{avg}}$.

---

## Detailed Step-by-Step Solutions

### Solution 1
1. Assuming uniform field between parallel plates:
   $$\mathbf{E}(t) = \frac{V(t)}{d} \hat{\mathbf{a}}_z = \frac{150 \sin(1000\pi t)}{2 \times 10^{-3}} \hat{\mathbf{a}}_z = 75,000 \sin(1000\pi t) \hat{\mathbf{a}}_z \quad [\text{V/m}]$$
2. Displacement current density:
   $$\mathbf{D}(t) = \varepsilon_r \varepsilon_0 \mathbf{E}(t)$$
   $$\mathbf{J}_D(t) = \frac{\partial \mathbf{D}}{\partial t} = \varepsilon_r \varepsilon_0 \frac{\partial \mathbf{E}}{\partial t}$$
   Substitute numerical values ($\varepsilon_r \varepsilon_0 = 3.5 \times 8.854 \times 10^{-12} \approx 3.099 \times 10^{-11} \text{ F/m}$):
   $$\mathbf{J}_D(t) = (3.099 \times 10^{-11}) \times 75,000 \times 1000\pi \cos(1000\pi t) \hat{\mathbf{a}}_z$$
   $$\mathbf{J}_D(t) \approx 7.30 \times 10^{-3} \cos(1000\pi t) \hat{\mathbf{a}}_z \quad [\text{A/m}^2]$$
3. Total displacement current:
   $$I_D(t) = \int_{\text{plate}} \mathbf{J}_D \cdot d\mathbf{S} = J_D(t) \times (\pi R^2)$$
   Plate area: $A = \pi (0.08)^2 \approx 0.0201 \text{ m}^2$.
   $$I_D(t) = (7.30 \times 10^{-3}) \times 0.0201 \cos(1000\pi t) \approx 1.467 \times 10^{-4} \cos(1000\pi t) \text{ A} = 0.1467 \cos(1000\pi t) \text{ mA}$$
   Capacitance $C = \frac{\varepsilon A}{d} = \frac{3.099 \times 10^{-11} \times 0.0201}{2 \times 10^{-3}} \approx 3.116 \times 10^{-10} \text{ F} = 311.6 \text{ pF}$.
   Conduction current:
   $$I_C(t) = C \frac{dV}{dt} = (3.116 \times 10^{-10}) \times (150 \times 1000\pi \cos(1000\pi t)) \approx 1.468 \times 10^{-4} \cos(1000\pi t) \text{ A}$$
   Thus, $I_D(t) = I_C(t)$ exactly, demonstrating continuity across the dielectric gap.
4. Using Ampere's Law around a circle of radius $r < R$:
   $$\oint \mathbf{B} \cdot d\mathbf{l} = \mu_0 I_{D, \text{enclosed}} = \mu_0 J_D \times (\pi r^2)$$
   $$B(r, t) (2\pi r) = \mu_0 J_D \pi r^2 \implies B(r, t) = \frac{\mu_0 J_D r}{2}$$
   $$B(r, t) = \frac{(4\pi \times 10^{-7}) \times (7.30 \times 10^{-3})}{2} r \cos(1000\pi t) \approx 4.59 \times 10^{-9} r \cos(1000\pi t) \quad [\text{Tesla}]$$

### Solution 2
1. Angular frequency: $\omega = 10^8 \pi \text{ rad/s}$.
   Frequency: $f = \frac{\omega}{2\pi} = \frac{10^8 \pi}{2\pi} = 50\text{ MHz}$.
   In free space:
   $$\beta = \frac{\omega}{c} = \frac{10^8 \pi}{3 \times 10^8} = \frac{\pi}{3} \approx 1.047 \text{ rad/m}$$
2. Polarization state:
   * $E_x = 30 \cos(\omega t - \beta z)$
   * $E_y = 40 \sin(\omega t - \beta z) = 40 \cos(\omega t - \beta z - \pi/2)$
   The two components have unequal amplitudes ($30 \neq 40$) and a phase difference of $\Delta \phi = -\pi/2$ (a $90^\circ$ quadrature shift).
   At $z=0$:
   * At $\omega t = 0$: $E_x = 30, E_y = 0$.
   * At $\omega t = \pi/2$: $E_x = 0, E_y = 40$.
   The field vector traces an ellipse in the counter-clockwise direction as viewed from $+z$ (looking in the direction of propagation). Therefore, the wave is **Left-Handed Elliptically Polarized**.
3. In free space, $\eta_0 \approx 120\pi \approx 377 \ \Omega$.
   The time-averaged Poynting vector is the sum of the power densities of the two orthogonal components:
   $$\mathbf{S}_{\text{avg}} = \left( \frac{E_{0x}^2}{2\eta_0} + \frac{E_{0y}^2}{2\eta_0} \right) \hat{\mathbf{a}}_z = \frac{30^2 + 40^2}{2 \times 377} \hat{\mathbf{a}}_z = \frac{900 + 1600}{754} \hat{\mathbf{a}}_z = \frac{2500}{754} \hat{\mathbf{a}}_z \approx 3.316 \hat{\mathbf{a}}_z \quad [\text{W/m}^2]$$

