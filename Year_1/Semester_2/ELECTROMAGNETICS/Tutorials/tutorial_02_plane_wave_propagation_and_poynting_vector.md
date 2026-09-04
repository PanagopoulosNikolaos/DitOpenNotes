# Tutorial 02: Plane Wave Propagation and Poynting Power Analysis

## Context and Grounding
This tutorial provides numerical recipes and analytical steps for computing wave parameters, phase velocity, skin depth, attenuation, and average power density (Poynting vector) for sinusoidal plane waves propagating in lossless and lossy media. It directly connects with `Lectures/08_EM.pdf` and `Exercises/02_test.md` (Exercise 3).

---

## 1. Wave Propagation in Lossy Media

In a medium with conductivity $\sigma$, permittivity $\varepsilon$, and permeability $\mu$, the complex propagation constant $\gamma$ is:
$$\gamma = \alpha + j\beta = \sqrt{j\omega\mu(\sigma + j\omega\varepsilon)}$$

* **Attenuation Constant ($\alpha$)**: Rate of exponential spatial decay $[\text{Np/m}]$.
* **Phase Constant ($\beta$)**: Rate of phase change $[\text{rad/m}]$.
* **Skin Depth ($\delta$)**: Distance over which field amplitude decays to $1/e \approx 36.8\%$:
  $$\delta = \frac{1}{\alpha}$$
* **Intrinsic Impedance ($\eta$)**:
  $$\eta = \sqrt{\frac{j\omega\mu}{\sigma + j\omega\varepsilon}} = |\eta| e^{j\theta_\eta}$$

---

## 2. Worked Problem: Power Flow in Lossless Dielectric

### Problem Statement
A uniform plane wave in a non-magnetic lossless medium ($\mu_r = 1, \varepsilon_r = 4, \sigma = 0$) has electric field:
$$\mathbf{E}(z, t) = 24 \cos(2\pi \times 10^8 t - \beta z) \hat{\mathbf{a}}_x \quad [\text{V/m}]$$

Find:
1. The phase velocity $v_p$ and phase constant $\beta$.
2. The intrinsic impedance $\eta$.
3. The magnetic field expression $\mathbf{H}(z, t)$.
4. The time-averaged Poynting vector $\mathbf{S}_{\text{avg}}$.

### Step 1: Phase Velocity and Phase Constant
* Angular frequency: $\omega = 2\pi \times 10^8 \text{ rad/s}$. Frequency $f = 10^8 \text{ Hz} = 100\text{ MHz}$.
* Velocity in dielectric:
  $$v_p = \frac{c}{\sqrt{\varepsilon_r \mu_r}} = \frac{3 \times 10^8}{\sqrt{4 \times 1}} = \frac{3 \times 10^8}{2} = 1.5 \times 10^8 \text{ m/s}$$
* Phase constant:
  $$\beta = \frac{\omega}{v_p} = \frac{2\pi \times 10^8}{1.5 \times 10^8} = \frac{4\pi}{3} \approx 4.189 \text{ rad/m}$$
* Wavelength:
  $$\lambda = \frac{2\pi}{\beta} = \frac{2\pi}{4\pi/3} = 1.5 \text{ m}$$

### Step 2: Intrinsic Wave Impedance
$$\eta = \sqrt{\frac{\mu}{\varepsilon}} = \sqrt{\frac{\mu_0}{\varepsilon_r \varepsilon_0}} = \frac{\eta_0}{\sqrt{\varepsilon_r}} = \frac{120\pi}{\sqrt{4}} = 60\pi \approx 188.5 \ \Omega$$

### Step 3: Magnetic Field Equation $\mathbf{H}$
The wave propagates in $+z$ with $\mathbf{E}$ polarized in $+\hat{\mathbf{a}}_x$. Because $\hat{\mathbf{a}}_E \times \hat{\mathbf{a}}_H = \hat{\mathbf{a}}_k = \hat{\mathbf{a}}_z$, the magnetic field is oriented in $+\hat{\mathbf{a}}_y$:
$$H_0 = \frac{E_0}{\eta} = \frac{24}{60\pi} = \frac{0.4}{\pi} \approx 0.1273 \text{ A/m}$$
$$\mathbf{H}(z, t) = 0.1273 \cos\left(2\pi \times 10^8 t - \frac{4\pi}{3} z\right) \hat{\mathbf{a}}_y \quad [\text{A/m}]$$

### Step 4: Time-Averaged Poynting Vector
$$\mathbf{S}_{\text{avg}} = \frac{1}{2} \frac{E_0^2}{\eta} \hat{\mathbf{a}}_z = \frac{1}{2} \frac{24^2}{60\pi} \hat{\mathbf{a}}_z = \frac{288}{60\pi} \hat{\mathbf{a}}_z = \frac{4.8}{\pi} \hat{\mathbf{a}}_z \approx 1.528 \hat{\mathbf{a}}_z \quad [\text{W/m}^2]$$

