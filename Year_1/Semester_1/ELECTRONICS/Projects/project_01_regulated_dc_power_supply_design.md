# Term Project: Design and Simulation of a Regulated Linear DC Power Supply

## Project Overview
Design, calculate, and validate a dual-output linear DC bench power supply converting 230V AC mains at 50 Hz into regulated $+5\text{ V}$ and $+12\text{ V}$ DC rails delivering up to $1.0\text{ A}$ continuous load current. This capstone engineering design synthesizes transformer coupling, bridge rectification, reservoir filter dimensioning, thermal heatsink modeling, and voltage regulation.

---

## 1. System Block Diagram and Architecture

```text
230V AC Mains
     │
     ▼
[Step-Down Transformer] (Turns ratio N1:N2)
     │
     ▼  Secondary AC Voltage (15V RMS)
[Full-Wave Bridge Rectifier] (4x 1N4007 diodes)
     │
     ▼  Pulsating DC Voltage
[Bulk Reservoir Capacitor C1] (Low-frequency ripple reduction)
     │
     ├───► [High-Frequency Filter C2] ──► [LM7812 Linear Regulator] ──► +12V DC Rail
     │                                           │
     └───► [High-Frequency Filter C3] ──► [LM7805 Linear Regulator] ──► +5V DC Rail
```

---

## 2. Technical Requirements and Specifications

| Parameter | Specification | Verification Method |
|:---|:---|:---|
| Primary AC Input | $230\text{ V}_{\text{rms}} \pm 10\%, 50\text{ Hz}$ | AC Source parameter |
| Output Rail 1 | $+12.0\text{ V}_{\text{dc}} \pm 2\%$, up to $1.0\text{ A}$ | DC load sweep |
| Output Rail 2 | $+5.0\text{ V}_{\text{dc}} \pm 2\%$, up to $1.0\text{ A}$ | DC load sweep |
| Maximum Voltage Ripple | $V_{r(p-p)} \le 1.5\text{ V}$ at bulk capacitor under full load | Transient analysis |
| Minimum Regulator Dropout | $V_{\text{in}} - V_{\text{out}} \ge 2.5\text{ V}$ across all operating conditions | Operating point inspection |
| Thermal Management | Maximum junction temperature $T_j \le 125^\circ\text{C}$ at $T_a = 40^\circ\text{C}$ | Thermal resistance equation |

---

## 3. Engineering Calculations and Sizing

### 3.1 Bulk Reservoir Filter Sizing
For full-wave rectified 50 Hz AC ($f_{\text{rect}} = 100\text{ Hz}$):
$$C \ge \frac{I_{\text{load,total}}}{f_{\text{rect}} \cdot V_{r(p-p)}} = \frac{1.0\text{ A} + 1.0\text{ A}}{100\text{ Hz} \cdot 1.5\text{ V}} \approx 13,333\,\mu\text{F}$$
Select two standard $6800\,\mu\text{F} / 35\text{ V}$ electrolytic capacitors in parallel ($C_{\text{total}} = 13,600\,\mu\text{F}$).

### 3.2 Diode Bridge Ratings
* Peak secondary voltage: $V_{s,\text{peak}} = \sqrt{2} \cdot 15\text{ V}_{\text{rms}} \approx 21.2\text{ V}$.
* Diode Peak Inverse Voltage: $\text{PIV} = V_{s,\text{peak}} = 21.2\text{ V}$.
* Use 1N4007 diodes ($\text{PIV} = 1000\text{ V}, I_F = 1.0\text{ A}$ average, $30\text{ A}$ surge).

### 3.3 Thermal Dissipation and Heatsink Selection
The power dissipated as heat in the linear regulators is:
$$P_D = (V_{\text{in,avg}} - V_{\text{out}}) \cdot I_{\text{load}}$$
For the +5V regulator with $V_{\text{in,avg}} \approx 19.8\text{ V}$:
$$P_D = (19.8\text{ V} - 5.0\text{ V}) \cdot 1.0\text{ A} = 14.8\text{ W}$$
Required heatsink thermal resistance to keep junction below $120^\circ\text{C}$:
$$\theta_{sa} \le \frac{T_{j,\text{max}} - T_a}{P_D} - (\theta_{jc} + \theta_{cs}) = \frac{120 - 40}{14.8} - (3.0 + 0.5) \approx 1.9^\circ\text{C/W}$$

---

## 4. Deliverables and Simulation Requirements
1. **Design Report**: Full mathematical justifications, component datasheets, schematic schematics, and bill of materials (BOM).
2. **SPICE Netlist (`power_supply.cir`)**: Full transient and DC sweep analysis demonstrating line regulation and load regulation from 0 to 1.0 A.
3. **Protection Circuits**: Reverse polarity protection diode and transient decoupling ceramic capacitors ($0.1\,\mu\text{F}$).

---

## 5. Evaluation Rubric

| Criterion | Target Metric | Points |
|:---|:---|:---:|
| Analytical Design Precision | Correct mathematical sizing of transformer, bridge, filter, and thermal heatsinks | 30 |
| SPICE Simulation Fidelity | Accurate model representations and valid transient waveforms | 25 |
| Regulation & Ripple Compliance | Verified compliance with output voltage tolerances and ripple limits | 20 |
| Safety & Protection Circuits | Implementation of reverse polarity diodes, bleeder resistors, and fuses | 15 |
| Documentation & Presentation | Schematic clarity, engineering BOM, and professional technical writing | 10 |
| **Total** | | **100** |

