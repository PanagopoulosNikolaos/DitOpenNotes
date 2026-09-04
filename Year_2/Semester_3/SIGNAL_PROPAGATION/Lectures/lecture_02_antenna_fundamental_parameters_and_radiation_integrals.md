# Lecture 02: Antenna Fundamental Parameters and Radiation Integrals

This lecture defines the primary engineering metrics used to evaluate antennas (radiation patterns, directivity, gain, input impedance, effective area) and derives the vector potential radiation integrals that relate antenna source currents to radiated far fields.

---

## 1. Radiation Pattern and Beamwidth

An antenna's **radiation pattern** is a mathematical function or graphical representation of the radiation properties of the antenna as a function of space coordinates $(\theta, \phi)$.

### 1.1 Radiation Lobes
- **Major Lobe (Main Beam):** Radiation lobe containing the direction of maximum radiation.
- **Side Lobes:** Minor lobes adjacent to the main beam representing undesirable parasitic radiation.
- **Back Lobe:** Minor lobe oriented $180^\circ$ opposite to the main beam.
- **Half-Power Beamwidth (HPBW):** Angular separation between the two directions where the radiation intensity equals half its maximum value ($-3\text{ dB}$ points).
- **First-Null Beamwidth (FNBW):** Angular separation between the first nulls (zeros) of the radiation pattern.

---

## 2. Radiation Intensity and Directivity

### 2.1 Radiation Intensity $U(\theta, \phi)$
Defined as the power radiated from an antenna per unit solid angle:
$$
U(\theta, \phi) = r^2 W_{\text{rad}}(r, \theta, \phi) \quad [\text{W/steradian}]
$$
The total radiated power $P_{\text{rad}}$ is obtained by integrating $U(\theta, \phi)$ over a closed spherical surface:
$$
P_{\text{rad}} = \iint_{4\pi} U(\theta, \phi) \, d\Omega = \int_{0}^{2\pi} \int_{0}^{\pi} U(\theta, \phi) \sin\theta \, d\theta \, d\phi
$$

### 2.2 Directivity $D$
Directivity is the ratio of the radiation intensity in a given direction to the radiation intensity averaged over all directions:
$$
D(\theta, \phi) = \frac{4\pi U(\theta, \phi)}{P_{\text{rad}}}
$$
Maximum directivity $D_0$:
$$
D_0 = \frac{4\pi U_{\max}}{P_{\text{rad}}} = \frac{4\pi}{\Omega_A}
$$
where $\Omega_A$ is the **Beam Solid Angle** (in steradians).

---

## 3. Antenna Efficiency and Gain

The **Gain** $G(\theta, \phi)$ accounts for the antenna's internal dissipation losses in addition to its directional capabilities:

$$
G(\theta, \phi) = \eta_{cd} \cdot D(\theta, \phi)
$$

where $\eta_{cd}$ is the radiation efficiency:
$$
\eta_{cd} = \frac{P_{\text{rad}}}{P_{\text{in}}} = \frac{R_{\text{rad}}}{R_{\text{rad}} + R_{\text{loss}}} \le 1.0
$$

- $R_{\text{rad}}$: Radiation resistance (models energy radiated away).
- $R_{\text{loss}}$: Conduction and dielectric loss resistance (models heat dissipation).

---

## 4. Input Impedance and Return Loss

The input impedance presented by an antenna at its terminals is:
$$
Z_{\text{in}} = R_{\text{in}} + j X_{\text{in}} = (R_{\text{rad}} + R_{\text{loss}}) + j X_{\text{in}}
$$

Connected to a transmission line with characteristic impedance $Z_0$:
- **Voltage Reflection Coefficient:**
  $$\Gamma = \frac{Z_{\text{in}} - Z_0}{Z_{\text{in}} + Z_0}$$
- **Voltage Standing Wave Ratio (VSWR):**
  $$\text{VSWR} = \frac{1 + |\Gamma|}{1 - |\Gamma|}$$
- **Return Loss:**
  $$\text{RL}_{[\text{dB}]} = -20 \log_{10}|\Gamma|$$

---

## 5. Radiation Integrals and Potential Formulation

In electromagnetic theory, radiated fields from an arbitrary electric current density $\mathbf{J}(\mathbf{r}')$ are computed using the **Magnetic Vector Potential** $\mathbf{A}(\mathbf{r})$:

$$
\mathbf{A}(\mathbf{r}) = \frac{\mu}{4\pi} \iiint_{V'} \mathbf{J}(\mathbf{r}') \frac{e^{-jkR}}{R} \, dV'
$$

In the far-field region ($r \gg r'$ and $r \gg \frac{2D^2}{\lambda}$):
- Amplitude approximation: $\frac{1}{R} \approx \frac{1}{r}$
- Phase approximation: $R \approx r - \mathbf{r}' \cdot \hat{\mathbf{a}}_r = r - (x'\sin\theta\cos\phi + y'\sin\theta\sin\phi + z'\cos\theta)$

Far-field magnetic vector potential:
$$
\mathbf{A}(\mathbf{r}) \approx \frac{\mu e^{-jkr}}{4\pi r} \iiint_{V'} \mathbf{J}(\mathbf{r}') e^{j k \mathbf{r}' \cdot \hat{\mathbf{a}}_r} \, dV'
$$

The radiated electric and magnetic far fields are TEM with respect to $\hat{\mathbf{a}}_r$:
$$
\mathbf{E}_{\text{rad}} = -j\omega \left( A_\theta \hat{\mathbf{a}}_\theta + A_\phi \hat{\mathbf{a}}_\phi \right)
$$
$$
\mathbf{H}_{\text{rad}} = \frac{1}{\eta_0} \hat{\mathbf{a}}_r \times \mathbf{E}_{\text{rad}}
$$

