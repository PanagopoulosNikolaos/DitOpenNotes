# Practice Exam 01: Fundamentals of Electromagnetics

## Context and Grounding
This practice exam provides a comprehensive evaluation covering vector calculus, electrostatics, magnetostatics, Maxwell's equations, and electromagnetic wave dynamics. It contains sectioned problems, complete worked solutions, and an analytical grading rubric.

---

## Part 1: Electrostatics and Boundary Conditions (35 Points)

### Question 1.1 (15 Points)
A spherical charge distribution in free space has volume charge density:
$$\rho_v(r) = \begin{cases} \rho_0 \left(1 - \frac{r^2}{R^2}\right), & 0 \le r \le R \\ 0, & r > R \end{cases}$$
1. Find the total enclosed charge $Q_{\text{total}}$.
2. Use Gauss's Law to calculate the electric field intensity $\mathbf{E}(r)$ in both regions ($r \le R$ and $r > R$).
3. Find the scalar electric potential $V(r)$ at the center of the sphere with reference $V(\infty) = 0$.

### Question 1.2 (20 Points)
A dielectric interface at $z = 0$ separates Region 1 ($z < 0$, $\varepsilon_{r1} = 2.0$) from Region 2 ($z > 0$, $\varepsilon_{r2} = 5.0$). The interface is free of surface charge ($\rho_S = 0$). In Region 1, the electric field is:
$$\mathbf{E}_1 = 12 \hat{\mathbf{a}}_x - 8 \hat{\mathbf{a}}_y + 20 \hat{\mathbf{a}}_z \quad [\text{V/m}]$$
1. Determine the electric field vector $\mathbf{E}_2$ in Region 2.
2. Find the electric flux density $\mathbf{D}_2$ in Region 2.
3. Compute the angles $\theta_1$ and $\theta_2$ that the field vectors make with the normal to the interface.

---

## Part 2: Magnetostatics and Induction (30 Points)

### Question 2.1 (15 Points)
A long cylindrical solid conductor of radius $a$ carries a uniformly distributed total current $I$ in the $+z$ direction.
1. Use Ampere's circuital law to find the magnetic field intensity $\mathbf{H}$ inside ($\rho < a$) and outside ($\rho > a$) the conductor.
2. Compute the total magnetic energy stored per unit length inside the conductor.

### Question 2.2 (15 Points)
A square wire loop of side length $s = 10\text{ cm}$ with total resistance $R = 2\ \Omega$ lies in the $xy$-plane. A spatially uniform time-varying magnetic field is applied:
$$\mathbf{B}(t) = 0.5 \cos(120\pi t) \hat{\mathbf{a}}_z \quad [\text{Tesla}]$$
1. Calculate the magnetic flux $\Phi(t)$ linking the loop.
2. Determine the induced electromotive force $\mathcal{E}_{\text{ind}}(t)$ using Faraday's law.
3. Find the induced current $I_{\text{ind}}(t)$ and identify the direction of current flow at $t = 0^+$.

---

## Part 3: Maxwell's Equations and Plane Waves (35 Points)

### Question 3.1 (35 Points)
A uniform plane wave in free space with frequency $f = 300\text{ MHz}$ propagates in the $+z$ direction. The electric field is polarized along the $x$-axis with peak amplitude $E_0 = 60\text{ V/m}$. At $t=0, z=0$, the field is at its positive maximum.
1. Write the complete time-harmonic expression for $\mathbf{E}(z, t)$.
2. Calculate the wavenumber $k$, wavelength $\lambda$, and period $T$.
3. Determine the instantaneous magnetic field intensity $\mathbf{H}(z, t)$.
4. Calculate the time-averaged Poynting vector $\mathbf{S}_{\text{avg}}$ and total power crossing a square aperture of area $4\text{ m}^2$ on the plane $z = 10\text{ m}$.

---

## Complete Worked Solutions and Scoring Breakdown

### Solution 1.1
1. Enclosed charge:
   $$Q_{\text{total}} = \int_0^R \rho_0 \left(1 - \frac{r^2}{R^2}\right) 4\pi r^2 dr = 4\pi \rho_0 \left[ \frac{r^3}{3} - \frac{r^5}{5R^2} \right]_0^R = 4\pi \rho_0 R^3 \left( \frac{1}{3} - \frac{1}{5} \right) = \frac{8\pi \rho_0 R^3}{15}$$
2. Electric Field via Gauss's Law ($\oint \mathbf{E} \cdot d\mathbf{S} = E_r (4\pi r^2) = \frac{Q_{\text{enc}}}{\varepsilon_0}$):
   * For $r > R$: $Q_{\text{enc}} = Q_{\text{total}} \implies \mathbf{E}(r) = \frac{2\rho_0 R^3}{15\varepsilon_0 r^2} \hat{\mathbf{a}}_r$.
   * For $r \le R$:
     $$Q_{\text{enc}}(r) = 4\pi \rho_0 \left[ \frac{r^3}{3} - \frac{r^5}{5R^2} \right] = 4\pi \rho_0 r^3 \left( \frac{1}{3} - \frac{r^2}{5R^2} \right)$$
     $$\mathbf{E}(r) = \frac{\rho_0}{\varepsilon_0} \left( \frac{r}{3} - \frac{r^3}{5R^2} \right) \hat{\mathbf{a}}_r$$
3. Potential at center:
   $$V(0) = -\int_\infty^0 \mathbf{E} \cdot d\mathbf{r} = \int_R^\infty \frac{2\rho_0 R^3}{15\varepsilon_0 r^2} dr + \int_0^R \frac{\rho_0}{\varepsilon_0} \left( \frac{r}{3} - \frac{r^3}{5R^2} \right) dr$$
   $$= \frac{2\rho_0 R^2}{15\varepsilon_0} + \frac{\rho_0}{\varepsilon_0} \left[ \frac{R^2}{6} - \frac{R^2}{20} \right] = \frac{2\rho_0 R^2}{15\varepsilon_0} + \frac{7\rho_0 R^2}{60\varepsilon_0} = \frac{15\rho_0 R^2}{60\varepsilon_0} = \frac{\rho_0 R^2}{4\varepsilon_0}$$

### Solution 1.2
1. Interface normal is $\hat{\mathbf{a}}_z$.
   * Tangential components ($x, y$) are continuous: $E_{2x} = E_{1x} = 12$, $E_{2y} = E_{1y} = -8$.
   * Normal components satisfy $D_{1n} = D_{2n}$ since $\rho_S = 0$:
     $$\varepsilon_1 E_{1z} = \varepsilon_2 E_{2z} \implies E_{2z} = \frac{\varepsilon_{r1}}{\varepsilon_{r2}} E_{1z} = \frac{2.0}{5.0} (20) = 8.0 \text{ V/m}$$
   $$\mathbf{E}_2 = 12 \hat{\mathbf{a}}_x - 8 \hat{\mathbf{a}}_y + 8 \hat{\mathbf{a}}_z \quad [\text{V/m}]$$
2. Electric flux density $\mathbf{D}_2 = \varepsilon_2 \mathbf{E}_2 = 5\varepsilon_0 \mathbf{E}_2$:
   $$\mathbf{D}_2 = \varepsilon_0 (60 \hat{\mathbf{a}}_x - 40 \hat{\mathbf{a}}_y + 40 \hat{\mathbf{a}}_z) \quad [\text{C/m}^2]$$
3. Angles with normal ($\hat{\mathbf{a}}_z$):
   * $\tan \theta_1 = \frac{E_{1t}}{E_{1n}} = \frac{\sqrt{12^2 + (-8)^2}}{20} = \frac{\sqrt{208}}{20} = \frac{14.42}{20} = 0.721 \implies \theta_1 \approx 35.8^\circ$
   * $\tan \theta_2 = \frac{E_{2t}}{E_{2n}} = \frac{\sqrt{12^2 + (-8)^2}}{8} = \frac{14.42}{8} = 1.803 \implies \theta_2 \approx 61.0^\circ$

### Solution 2.1
1. Current density: $J = \frac{I}{\pi a^2}$.
   * For $\rho \le a$: $\oint \mathbf{H} \cdot d\mathbf{l} = H_\phi (2\pi \rho) = J (\pi \rho^2) = I \frac{\rho^2}{a^2} \implies \mathbf{H} = \frac{I\rho}{2\pi a^2} \hat{\mathbf{a}}_\phi$.
   * For $\rho > a$: $H_\phi (2\pi \rho) = I \implies \mathbf{H} = \frac{I}{2\pi \rho} \hat{\mathbf{a}}_\phi$.
2. Internal magnetic energy per unit length:
   $$W_H = \frac{1}{2} \int_V \mu_0 H^2 dv = \frac{\mu_0}{2} \int_0^L dz \int_0^{2\pi} d\phi \int_0^a \left(\frac{I\rho}{2\pi a^2}\right)^2 \rho \, d\rho = \frac{\mu_0 L I^2}{4\pi a^4} \left[ \frac{a^4}{4} \right] = \frac{\mu_0 I^2 L}{16\pi}$$
   Energy per unit length: $\frac{W_H}{L} = \frac{\mu_0 I^2}{16\pi} \text{ J/m}$.

### Solution 2.2
1. Area $A = s^2 = (0.10)^2 = 0.01 \text{ m}^2$.
   $$\Phi(t) = B(t) A = 0.5 \cos(120\pi t) \times 0.01 = 5 \times 10^{-3} \cos(120\pi t) \quad [\text{Weber}]$$
2. Induced EMF:
   $$\mathcal{E}_{\text{ind}}(t) = -\frac{d\Phi}{dt} = - (5 \times 10^{-3}) (-120\pi \sin(120\pi t)) = 0.6\pi \sin(120\pi t) \approx 1.885 \sin(120\pi t) \quad [\text{Volts}]$$
3. Induced current:
   $$I_{\text{ind}}(t) = \frac{\mathcal{E}_{\text{ind}}(t)}{R} = \frac{0.6\pi \sin(120\pi t)}{2} = 0.3\pi \sin(120\pi t) \approx 0.942 \sin(120\pi t) \quad [\text{A}]$$
   At $t = 0^+$, $\sin(120\pi t) > 0 \implies \mathcal{E} > 0$. By Lenz's law, the induced current produces a magnetic field opposing the change in flux (flowing counter-clockwise when viewed looking down the $+z$ axis).

### Solution 3.1
1. $\omega = 2\pi f = 2\pi \times (3 \times 10^8) = 6\pi \times 10^8 \text{ rad/s}$.
   $$k = \frac{\omega}{c} = \frac{6\pi \times 10^8}{3 \times 10^8} = 2\pi \text{ rad/m}$$
   $$\mathbf{E}(z, t) = 60 \cos(6\pi \times 10^8 t - 2\pi z) \hat{\mathbf{a}}_x \quad [\text{V/m}]$$
2. $\lambda = \frac{2\pi}{k} = \frac{2\pi}{2\pi} = 1.0 \text{ m}$.
   Period $T = \frac{1}{f} = \frac{1}{3 \times 10^8} \approx 3.333 \text{ ns}$.
3. In free space, $\eta_0 = 120\pi \approx 377 \ \Omega$.
   $$H_0 = \frac{E_0}{\eta_0} = \frac{60}{120\pi} = \frac{1}{2\pi} \approx 0.1592 \text{ A/m}$$
   $$\mathbf{H}(z, t) = 0.1592 \cos(6\pi \times 10^8 t - 2\pi z) \hat{\mathbf{a}}_y \quad [\text{A/m}]$$
4. Poynting vector:
   $$\mathbf{S}_{\text{avg}} = \frac{1}{2} E_0 H_0 \hat{\mathbf{a}}_z = \frac{1}{2} (60) \left(\frac{1}{2\pi}\right) \hat{\mathbf{a}}_z = \frac{15}{\pi} \hat{\mathbf{a}}_z \approx 4.775 \hat{\mathbf{a}}_z \quad [\text{W/m}^2]$$
   Power crossing $4\text{ m}^2$ aperture:
   $$P_{\text{total}} = |\mathbf{S}_{\text{avg}}| \times \text{Area} = 4.775 \times 4 \approx 19.10 \text{ Watts}$$

