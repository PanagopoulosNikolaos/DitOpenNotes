# Tutorial 01: Friis Transmission Equation and RF Link Budget Analysis

This tutorial provides practical engineering procedures for calculating line-of-sight (LOS) wireless link budgets, computing Free-Space Path Loss (FSPL), accounting for system margins, and determining receiver sensitivity thresholds.

---

## 1. The Decibel Link Budget Equation

In RF systems engineering, the Friis transmission equation is expressed in logarithmic form ($\text{dBm}$ and $\text{dB}$):

$$
P_{r[\text{dBm}]} = P_{t[\text{dBm}]} + G_{t[\text{dBi}]} + G_{r[\text{dBi}]} - \text{FSPL}_{[\text{dB}]} - L_{\text{tx}[\text{dB}]} - L_{\text{rx}[\text{dB}]} - L_{\text{misc}[\text{dB}]}
$$

### Parameter Definitions:
- $P_t$: Transmitter output power in $\text{dBm}$ ($P_{[\text{dBm}]} = 10 \log_{10}\left(\frac{P_{[\text{mW}]}}{1\text{ mW}}\right)$).
- $G_t, G_r$: Transmit and receive antenna gains in $\text{dBi}$.
- $L_{\text{tx}}, L_{\text{rx}}$: Cable, connector, and insertion losses.
- $L_{\text{misc}}$: Atmospheric attenuation, polarization mismatch loss ($\text{PLF}$), and obstacle fading margins.
- $\text{FSPL}$: Free-Space Path Loss:
  $$\text{FSPL}_{[\text{dB}]} = 32.44 + 20 \log_{10}(R_{[\text{km}]}) + 20 \log_{10}(f_{[\text{MHz}]})$$

---

## 2. Receiver Sensitivity and Fade Margin

The thermal noise floor $N_0$ of a receiver with bandwidth $B$ at temperature $T_0 = 290\text{ K}$ is:
$$
N_{\text{floor}[\text{dBm}]} = -174\text{ dBm/Hz} + 10 \log_{10}(B_{[\text{Hz}]}) + \text{NF}_{[\text{dB}]}
$$
where $\text{NF}$ is the receiver Noise Figure.

The minimum detectable received signal power (Receiver Sensitivity $S_{\text{rx}}$) for a required Signal-to-Noise Ratio ($\text{SNR}_{\text{min}}$):
$$
S_{\text{rx}[\text{dBm}]} = N_{\text{floor}[\text{dBm}]} + \text{SNR}_{\text{min}[\text{dB}]}
$$

The **Fade Margin** evaluates link reliability against atmospheric and multipath degradation:
$$
\text{Fade Margin}_{[\text{dB}]} = P_{r[\text{dBm}]} - S_{\text{rx}[\text{dBm}]} \ge 15\text{ to } 25\text{ dB}
$$

---

## 3. Worked Engineering Scenario

**System Parameters:**
- Carrier Frequency $f = 2.4\text{ GHz} = 2,400\text{ MHz}$.
- Link Distance $R = 5.0\text{ km}$.
- Transmit Power $P_t = 20\text{ dBm}$ ($100\text{ mW}$).
- Transmit Antenna Gain $G_t = 14\text{ dBi}$ (Directional patch).
- Receive Antenna Gain $G_r = 8\text{ dBi}$.
- Cable and connector losses: $L_{\text{tx}} = 1.5\text{ dB}$, $L_{\text{rx}} = 1.0\text{ dB}$.
- Channel Bandwidth $B = 20\text{ MHz}$, Receiver $\text{NF} = 5\text{ dB}$.
- Required $\text{SNR}_{\text{min}} = 12\text{ dB}$ (for QPSK modulation).

### Calculations:
1. **Free-Space Path Loss:**
   $$\text{FSPL} = 32.44 + 20 \log_{10}(5.0) + 20 \log_{10}(2400) = 32.44 + 13.98 + 67.60 = 114.02\text{ dB}$$

2. **Received Power $P_r$:**
   $$P_r = 20 + 14 + 8 - 114.02 - 1.5 - 1.0 = -74.52\text{ dBm}$$

3. **Receiver Noise Floor:**
   $$N_{\text{floor}} = -174 + 10 \log_{10}(20 \times 10^6) + 5 = -174 + 73.01 + 5 = -95.99\text{ dBm}$$

4. **Receiver Sensitivity:**
   $$S_{\text{rx}} = -95.99 + 12 = -83.99\text{ dBm}$$

5. **Link Fade Margin:**
   $$\text{Fade Margin} = P_r - S_{\text{rx}} = -74.52 - (-83.99) = +9.47\text{ dB}$$
   *Design Decision:* A fade margin of $9.47\text{ dB}$ is below the recommended $15\text{ dB}$ threshold for outdoor terrestrial links. To improve margin, the receiver antenna should be upgraded to a $14\text{ dBi}$ dish or transmitter power increased.

