# 03_Hmiagogoi-Epafi_PN Documentation

This lecture covers semiconductor materials, intrinsic and extrinsic doping, the PN junction structure and its energy band analysis, depletion region formation, and the behavior under forward and reverse bias.

---

## 1. Conceptual Foundation

Semiconductors are materials whose conductivity falls between conductors and insulators. By introducing controlled impurities (doping), their electrical properties can be precisely engineered. The PN junction -- the interface between p-type and n-type regions of the same semiconductor crystal -- is the fundamental building block of diodes, transistors, and integrated circuits.

---

## 2. Formal Definition and Model

### 2.1 Material Classification by Resistivity

| Material Type | Resistivity Range ($\Omega \cdot \text{m}$) |
|:--------------|:-------------------------------------------|
| Conductors | $10^{-8}$ |
| Semiconductors | $10^{-6}$ to $10^{6}$ |
| Insulators | $10^{11}$ |

### 2.2 Temperature Dependence

- Conductors and insulators: resistivity does not change significantly with temperature.
- Semiconductors: resistivity changes significantly with temperature.

### 2.3 Semiconductor Crystal Structure

Silicon (Si) and Germanium (Ge) have four valence electrons, forming four covalent bonds in a diamond-like crystal lattice. At $T = 0\,\text{K}$, all electrons are bound (semiconductor behaves as an insulator). At room temperature, thermal energy frees some electrons, creating **electron-hole pairs**.

### 2.4 Charge Carriers

| Carrier | Type | Effective Charge |
|:--------|:-----|:-----------------|
| Electron | Negative charge carrier | $-q$ |
| Hole | Positive charge carrier | $+q$ (absence of electron) |

Holes move in the opposite direction to electrons under an applied field.

---

## 3. Energy Band Approach

### 3.1 Energy Bands

- **Valence band:** Energy levels of bonding electrons.
- **Conduction band:** Energy levels of free electrons.
- **Band gap ($E_g$):** Forbidden region between valence and conduction bands.

### 3.2 Material Comparison

| Material | Band Gap | Behavior |
|:---------|:---------|:---------|
| Insulator (diamond) | Large ($> 5\,\text{eV}$) | Non-conductive |
| Semiconductor (Si) | Small ($1.12\,\text{eV}$) | Partially conductive |
| Conductor (metal) | Zero (bands overlap) | Highly conductive |

---

## 4. Intrinsic and Extrinsic Semiconductors

### 4.1 Intrinsic (Pure) Semiconductors

- All atoms are identical (pure Si or Ge).
- $n = p = n_i$, where $n$ = electron concentration, $p$ = hole concentration.
- $n_i$ depends on temperature and band gap:

$$
n_i^2 = BT^3 e^{-E_g / kT}
$$

Where $B$ is a material constant, $T$ is absolute temperature, $k$ is Boltzmann's constant, and $E_g$ is the band gap energy.

### 4.2 Extrinsic (Doped) Semiconductors

Doping: Adding pentavalent (5 valence electrons) or trivalent (3 valence electrons) impurity atoms to a tetravalent semiconductor.

| Dopant Type | Valence | Role | Example |
|:------------|:--------|:-----|:--------|
| Donor | 5 | Contributes extra electrons | Phosphorus (P) |
| Acceptor | 3 | Creates extra holes | Boron (B) |

**N-type semiconductor:**
- Doped with donor atoms (pentavalent).
- Majority carriers: electrons.
- Minority carriers: holes.

**P-type semiconductor:**
- Doped with acceptor atoms (trivalent).
- Majority carriers: holes.
- Minority carriers: electrons.

### 4.3 Other Semiconductor Types

- **Organic semiconductors:** Fluoresce under applied voltage; color depends on electric field strength.
- **Amorphous semiconductors:** Used in photovoltaic cells (e.g., amorphous silicon).

---

## 5. PN Junction

### 5.1 Diffusion at Junction Formation

When p-type and n-type regions are brought together:

1. Electrons diffuse from n to p region.
2. Holes diffuse from p to n region.
3. A **diffusion region** forms around the junction containing both carrier types.
4. Recombination occurs: free electrons fill holes, eliminating both carriers.

### 5.2 Depletion Region

- **Depletion region (space charge region):** The region near the junction depleted of free carriers.
- Fixed ionized impurities remain, creating a **space charge distribution**:
  - Negative charge on p-side (acceptors).
  - Positive charge on n-side (donors).

### 5.3 Contact Potential ($V_0$)

The space charge creates a built-in electric field and a potential difference across the junction called the **contact potential** (or built-in potential). For silicon, $V_0 \approx 0.6 - 0.7\,\text{V}$.

### 5.4 Junction Capacitance ($C_0$)

The depletion region, with its two oppositely charged layers, behaves as a capacitor:

$$
C_0 = \frac{\epsilon A}{W}
$$

Where $\epsilon$ is permittivity, $A$ is cross-sectional area, and $W$ is depletion width.

### 5.5 Energy Barrier ($E_0$)

At equilibrium, the Fermi levels of both sides equalize. This creates an energy barrier $E_0 = qV_0$ that prevents further diffusion.

---

## 6. Step-by-Step Mechanism: PN Junction Bias

### 6.1 Reverse Bias

**Configuration:** Positive terminal to n-side, negative terminal to p-side.

1. External field pulls majority carriers away from the junction.
2. Depletion region **widens**.
3. The potential barrier **increases**.
4. The junction acts as an **insulator** (open circuit).
5. A negligible leakage current flows due to thermally generated minority carriers.

### 6.2 Forward Bias

**Configuration:** Positive terminal to p-side, negative terminal to n-side.

1. External field pushes majority carriers toward the junction.
2. Depletion region **narrows**.
3. The potential barrier **decreases**.
4. When applied voltage exceeds $V_0$, the barrier is overcome.
5. Current flows freely through the junction.

---

## 7. Worked Examples

### Exercise 1: Intrinsic Carrier Concentration

**Problem:** For intrinsic silicon at $300\,\text{K}$, $n_i = 1.5 \times 10^{10}\,\text{cm}^{-3}$. If for intrinsic germanium at the same temperature $n_i = 2.4 \times 10^{13}\,\text{cm}^{-3}$, which has a larger band gap?

**Solution:**

The intrinsic carrier concentration $n_i$ depends exponentially on the band gap. A smaller $n_i$ corresponds to a larger $E_g$. Since silicon has $n_i = 1.5 \times 10^{10}\,\text{cm}^{-3}$ (much smaller than germanium's $2.4 \times 10^{13}\,\text{cm}^{-3}$), silicon has a larger band gap.

---

### Exercise 2: N-type Doping

**Problem:** A silicon crystal is doped with $10^{16}\,\text{cm}^{-3}$ phosphorus atoms. Assuming complete ionization at room temperature, find the electron and hole concentrations. ($n_i = 1.5 \times 10^{10}\,\text{cm}^{-3}$)

**Solution:**

For n-type doping, $N_D = 10^{16}\,\text{cm}^{-3}$.

$$
n \approx N_D = 10^{16}\,\text{cm}^{-3}
$$

Using the mass action law $n \cdot p = n_i^2$:

$$
p = \frac{n_i^2}{n} = \frac{(1.5 \times 10^{10})^2}{10^{16}} = \frac{2.25 \times 10^{20}}{10^{16}} = 2.25 \times 10^{4}\,\text{cm}^{-3}
$$

Majority carriers (electrons): $10^{16}\,\text{cm}^{-3}$. Minority carriers (holes): $2.25 \times 10^{4}\,\text{cm}^{-3}$.

---

### Exercise 3: P-type Doping

**Problem:** A silicon crystal is doped with $5 \times 10^{15}\,\text{cm}^{-3}$ boron atoms. Find the hole and electron concentrations at room temperature.

**Solution:**

For p-type doping, $N_A = 5 \times 10^{15}\,\text{cm}^{-3}$.

$$
p \approx N_A = 5 \times 10^{15}\,\text{cm}^{-3}
$$

$$
n = \frac{n_i^2}{p} = \frac{(1.5 \times 10^{10})^2}{5 \times 10^{15}} = \frac{2.25 \times 10^{20}}{5 \times 10^{15}} = 4.5 \times 10^{4}\,\text{cm}^{-3}
$$

Majority carriers (holes): $5 \times 10^{15}\,\text{cm}^{-3}$. Minority carriers (electrons): $4.5 \times 10^{4}\,\text{cm}^{-3}$.

---

### Exercise 4: Energy Band Gap Identification

**Problem:** Three materials have band gaps of $0\,\text{eV}$, $1.1\,\text{eV}$, and $6\,\text{eV}$. Classify each as conductor, semiconductor, or insulator.

**Solution:**

- $0\,\text{eV}$ (bands overlap): **Conductor** (metal).
- $1.1\,\text{eV}$: **Semiconductor** (silicon).
- $6\,\text{eV}$: **Insulator** (diamond).

---

### Exercise 5: Depletion Region -- Forward Bias Effect

**Problem:** Explain why forward bias reduces the depletion region width.

**Solution:**

Under forward bias, the external voltage opposes the built-in potential. Positive voltage applied to p-side repels holes toward the junction; negative voltage on n-side repels electrons toward the junction. This influx of carriers neutralizes the fixed space charge, narrowing the depletion region. When the external voltage exceeds $V_0$, the depletion region practically disappears and current flows.

---

### Exercise 6: Reverse Bias -- Leakage Current

**Problem:** A silicon diode at room temperature has a reverse saturation current of $10\,\text{nA}$. If the temperature rises, does the reverse current increase or decrease? Explain.

**Solution:**

The reverse current in a PN junction is primarily due to thermally generated minority carriers. As temperature increases, more electron-hole pairs are generated, so the reverse current **increases**. This is why reverse leakage current is temperature-dependent.

---

### Exercise 7: Depletion Capacitance

**Problem:** A PN junction has a depletion width of $0.5\,\mu\text{m}$ and area $1\,\text{mm}^2$. The permittivity of silicon is $\epsilon = 11.7 \times 8.85 \times 10^{-14}\,\text{F/cm}$. Estimate the junction capacitance.

**Solution:**

$$
C_0 = \frac{\epsilon A}{W}
$$

Convert units: $A = 1\,\text{mm}^2 = 0.01\,\text{cm}^2$, $W = 0.5\,\mu\text{m} = 5 \times 10^{-5}\,\text{cm}$.

$$
\epsilon = 11.7 \times 8.85 \times 10^{-14} = 1.036 \times 10^{-12}\,\text{F/cm}
$$

$$
C_0 = \frac{1.036 \times 10^{-12} \times 0.01}{5 \times 10^{-5}} = \frac{1.036 \times 10^{-14}}{5 \times 10^{-5}} = 2.07 \times 10^{-10}\,\text{F} = 207\,\text{pF}
$$

---

### Exercise 8: PN Junction -- Equilibrium Analysis

**Problem:** For a PN junction in thermal equilibrium, why must the Fermi level be constant across the junction?

**Solution:**

In thermal equilibrium, there is no net current flow. If the Fermi level were different on the two sides, electrons from the higher Fermi level side would have a statistical tendency to flow to the lower side, creating a net current. Therefore, the Fermi level must be constant (flat) across the entire junction at equilibrium. This equalization process creates the energy barrier $E_0$.

---

## 8. Connections and Cross-References

- The PN junction is the basis for the diode (Lecture 04, Lecture 05).
- Semiconductor doping concepts are essential for understanding BJT transistors (Lecture 07).
- The depletion region and its capacitance are critical for high-frequency diode behavior.

---

## Exam Tip: Identifying Doping Type

In exams, remember: **Donor** (5 valence electrons) gives **N-type** (Negative majority carriers). **Acceptor** (3 valence electrons) gives **P-type** (Positive majority carriers). The number 5 starts with "f" like "five" and "free electrons" -- a simple mnemonic: pentavalent donors produce n-type.