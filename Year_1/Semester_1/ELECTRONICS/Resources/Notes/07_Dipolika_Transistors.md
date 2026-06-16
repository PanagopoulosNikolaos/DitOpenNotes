# 07_Dipolika_Transistors Documentation

This lecture introduces the Bipolar Junction Transistor (BJT): its history, NPN and PNP types, terminal identification, operating principle, the three amplifier configurations, characteristic curves, operating regions, and key parameters ($\alpha$, $\beta$).

---

## 1. Conceptual Foundation

The transistor is a three-terminal semiconductor device that can amplify signals and act as a switch. By controlling a small base current, a much larger collector current can be regulated, enabling amplification. The BJT was invented at Bell Labs in 1948 (Bardeen, Brattain, Shockley -- Nobel Prize 1956) and revolutionized electronics.

---

## 2. Formal Definition and Model

### 2.1 BJT Types

| Type | Structure | Symbol |
|:-----|:----------|:-------|
| NPN | N-P-N layers | Arrow points out at emitter |
| PNP | P-N-P layers | Arrow points in at emitter |

### 2.2 Terminals

| Terminal | Symbol | Function |
|:---------|:-------|:---------|
| Emitter | E | Heavily doped; emits charge carriers |
| Base | B | Thin, lightly doped; controls current |
| Collector | C | Collects charge carriers |

### 2.3 Terminal Identification

- Dot on package: indicates collector.
- Protrusion: indicates emitter.
- Power transistors: metal case = collector.
- Always consult the manufacturer's datasheet for pinout.

### 2.4 Operating Principle (NPN)

1. Base-emitter junction: forward biased ($V_{BE} \approx 0.7\,\text{V}$).
2. Base-collector junction: reverse biased.
3. Electrons from emitter diffuse through the thin base into the collector.
4. Base is thin and lightly doped -- most electrons reach the collector rather than recombining.

**Key relationships:**

$$
I_E = I_C + I_B
$$

$$
I_C = \beta \cdot I_B
$$

$$
I_E = (\beta + 1) I_B
$$

### 2.5 Current Gain Parameters

| Parameter | Definition | Relationship |
|:----------|:-----------|:-------------|
| $\beta_{DC}$ (or $h_{FE}$) | $I_C / I_B$ | $\beta = \alpha / (1 - \alpha)$ |
| $\alpha_{DC}$ | $I_C / I_E$ | $\alpha = \beta / (\beta + 1)$ |
| | | $\beta + 1 = 1 / (1 - \alpha)$ |

Typical values: $\beta = 50$ to $300$, $\alpha = 0.9$ to $0.998$.

---

## 3. Characteristic Curves and Operating Regions

### 3.1 Input (Base) Characteristics

Plot of $I_B$ vs $V_{BE}$ for fixed $V_{CE}$. Shows diode-like exponential behavior.

### 3.2 Output (Collector) Characteristics

Family of curves: $I_C$ vs $V_{CE}$ for various $I_B$ values.

### 3.3 Operating Regions

| Region | BE Junction | BC Junction | Conditions |
|:-------|:------------|:------------|:-----------|
| Active (forward) | Forward biased | Reverse biased | $I_B > 0$, $V_{BC} < 0$ |
| Saturation | Forward biased | Forward biased | $I_B > 0$, $V_{BC} > 0$ |
| Cutoff | Reverse biased | Forward biased | $I_B < 0$ or $V_{BE} < V_T$ |
| Breakdown | -- | -- | $V_{CE}$ too high (avalanche) |

**Active region:** $I_C = \beta I_B$ (amplification).
**Cutoff:** $I_C = 0$ (open switch).
**Saturation:** $V_{CE(sat)} \approx 0.2\,\text{V}$ (closed switch).

### 3.4 Early Effect

In the active region, $I_C$ increases slightly with $V_{CE}$ due to base width modulation.

$$
i_C = I_S e^{v_{BE} / V_T} \left(1 + \frac{v_{CE}}{V_A}\right)
$$

Where $V_A$ is the Early voltage ($50-100\,\text{V}$ typically). Output resistance:

$$
r_o = \frac{V_A}{I_C}
$$

---

## 4. Three Amplifier Configurations

| Configuration | Common Terminal | Input | Output | Characteristics |
|:--------------|:----------------|:------|:-------|:----------------|
| Common Emitter | Emitter | Base | Collector | High voltage and current gain |
| Common Base | Base | Emitter | Collector | Low input impedance, high voltage gain |
| Common Collector | Collector | Base | Emitter | Unity voltage gain, high input impedance |

---

## 5. Worked Examples

### Exercise 1: Current Calculation -- NPN

**Problem:** An NPN BJT has $\beta = 150$ and $I_B = 20\,\mu\text{A}$. Find $I_C$ and $I_E$.

**Solution:**

$$
I_C = \beta I_B = 150 \times 20 \times 10^{-6} = 3 \times 10^{-3} = 3\,\text{mA}
$$

$$
I_E = I_C + I_B = 3 + 0.02 = 3.02\,\text{mA}
$$

---

### Exercise 2: Alpha Calculation

**Problem:** A BJT has $\beta = 100$. Find $\alpha$.

**Solution:**

$$
\alpha = \frac{\beta}{\beta + 1} = \frac{100}{101} = 0.9901
$$

---

### Exercise 3: Beta from Alpha

**Problem:** A BJT has $\alpha = 0.99$. Find $\beta$.

**Solution:**

$$
\beta = \frac{\alpha}{1 - \alpha} = \frac{0.99}{0.01} = 99
$$

---

### Exercise 4: Region Determination

**Problem:** A BJT circuit has $V_{BE} = 0.7\,\text{V}$ and $V_{BC} = -2\,\text{V}$. In which region does the transistor operate?

**Solution:**

$V_{BE} = 0.7\,\text{V} > 0$: BE junction forward biased.
$V_{BC} = -2\,\text{V} < 0$: BC junction reverse biased.

The transistor operates in the **active region**.

---

### Exercise 5: Beta from Characteristic Curves

**Problem:** From the output characteristics at $V_{CE} = 7.5\,\text{V}$, $I_C$ changes from $2.2\,\text{mA}$ to $3.2\,\text{mA}$ as $I_B$ changes from $20\,\mu\text{A}$ to $30\,\mu\text{A}$. Find $\beta_{AC}$.

**Solution:**

$$
\beta_{AC} = \frac{\Delta I_C}{\Delta I_B} = \frac{3.2 - 2.2}{30 - 20} = \frac{1.0\,\text{mA}}{10\,\mu\text{A}} = \frac{0.001}{0.00001} = 100
$$

---

### Exercise 6: DC Beta

**Problem:** At $V_{CE} = 7.5\,\text{V}$, $I_C = 2.7\,\text{mA}$, and $I_B = 25\,\mu\text{A}$. Find $\beta_{DC}$.

**Solution:**

$$
\beta_{DC} = \frac{I_C}{I_B} = \frac{2.7 \times 10^{-3}}{25 \times 10^{-6}} = 108
$$

---

### Exercise 7: Transistor as Switch

**Problem:** An NPN transistor with $\beta = 100$ is used as a switch with $V_{CC} = 12\,\text{V}$, $R_C = 1\,k\Omega$. Find the minimum $I_B$ to saturate the transistor.

**Solution:**

Saturation condition: $I_C = I_{C(sat)} = \frac{V_{CC}}{R_C} = \frac{12}{1000} = 12\,\text{mA}$

Minimum base current for saturation:

$$
I_{B(min)} = \frac{I_{C(sat)}}{\beta} = \frac{12}{100} = 0.12\,\text{mA} = 120\,\mu\text{A}
$$

---

### Exercise 8: Output Resistance (Early Effect)

**Problem:** A BJT has $V_A = 80\,\text{V}$ and operates at $I_C = 2\,\text{mA}$. Find the output resistance $r_o$.

**Solution:**

$$
r_o = \frac{V_A}{I_C} = \frac{80}{0.002} = 40,000\,\Omega = 40\,k\Omega
$$

---

## 6. Connections and Cross-References

- The BJT's PN junctions rely on semiconductor theory (Lecture 03).
- Transistor biasing circuits (Lecture 08) determine the Q-point.
- Amplifier design (Lecture 09) uses BJT parameters from this lecture.
- The $0.7\,\text{V}$ base-emitter voltage follows from PN junction behavior (Lecture 04).

---

## Exam Tip: Identifying Operating Region

To determine the transistor region, always follow this method: (1) assume active region, set $V_{BE} = 0.7\,\text{V}$. (2) Calculate $I_B$ and $V_{BC}$. (3) If $I_B > 0$ and $V_{BC} < 0$: active. If $I_B > 0$ and $V_{BC} > 0$: saturation. If $I_B < 0$: cutoff.