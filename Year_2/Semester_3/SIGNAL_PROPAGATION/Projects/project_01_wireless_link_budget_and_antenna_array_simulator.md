# Project 01: Wireless Link Budget and Phased Array Beamforming Simulator

## Project Overview
Develop a comprehensive RF engineering simulation suite in Python that combines physical antenna array pattern synthesis with realistic radio wave propagation models (Free-Space Path Loss and the Two-Ray Ground Reflection model).

---

## Technical Specifications

### 1. Phased Array Beamforming Engine
- Support $N$-element Uniform Linear Arrays (ULA) and planar rectangular arrays.
- Dynamically synthesize the normalized Array Factor:
  $$\text{AF}_n(\theta, \phi) = \frac{1}{N} \sum_{n=0}^{N-1} a_n e^{j (n k d \cos\theta + \beta)}$$
- Implement electronic beam steering to user-specified coordinates $(\theta_0, \phi_0)$.
- Calculate Half-Power Beamwidth (HPBW), First-Null Beamwidth (FNBW), and peak Side Lobe Level (SLL) in $\text{dB}$.

### 2. Multi-Mechanism Propagation Models
1. **Free-Space Path Loss (FSPL):**
   $$\text{FSPL}_{[\text{dB}]} = 32.44 + 20 \log_{10}(R_{[\text{km}]}) + 20 \log_{10}(f_{[\text{MHz}]})$$
2. **Two-Ray Ground Reflection Model:**
   For base station height $h_t$, mobile height $h_r$, and distance $R \gg h_t, h_r$:
   $$P_r \approx P_t G_t G_r \frac{h_t^2 h_r^2}{R^4}$$
   $$\text{PL}_{2\text{-ray}[\text{dB}]} = 40 \log_{10}(R) - 20 \log_{10}(h_t) - 20 \log_{10}(h_r)$$
3. **Crossover Distance Calculation:**
   Compute the critical distance $d_c = \frac{4\pi h_t h_r}{\lambda}$ where propagation transitions from $R^{-2}$ free-space loss to $R^{-4}$ ground-reflection loss.

---

## Project Milestones

| Milestone | Target Objective | Deliverables |
|---|---|---|
| **Phase 1** | Antenna Array Pattern Engine | Vectorized array factor calculation and 2D polar/Cartesian plotting module |
| **Phase 2** | Beam Steering & Grating Lobe Detector | Dynamic phase steering with automatic warning on grating lobe emergence |
| **Phase 3** | Propagation Channel Simulator | Combined FSPL and Two-Ray ground reflection path loss curves vs. distance |
| **Phase 4** | End-to-End Link Budget Suite | Complete CLI tool reporting SNR, receiver sensitivity, fade margins, and final report |

---

## Grading Rubric

| Assessment Criteria | Description | Weight |
|---|---|---|
| **Electromagnetic Accuracy** | Correct mathematical implementation of array factors and Two-Ray path loss | 30% |
| **Beamforming Features** | Precise electronic steering, HPBW/FNBW calculation, grating lobe detection | 30% |
| **Channel Modeling** | Accurate crossover distance modeling and realistic fade margin telemetry | 20% |
| **Software Architecture** | Clean modular Python code, unit tests, automated polar plot generation | 20% |

