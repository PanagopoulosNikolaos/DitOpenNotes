# Assignment 02: Linear Array Factors and Beam Synthesis

## Objective
Assess analytical evaluation and synthesis of Uniform Linear Arrays (ULAs), calculation of null angles, half-power beamwidths, phased array steering phases, and grating lobe prevention criteria.

---

## Problem Set

### Problem 1: 8-Element Broadside Uniform Linear Array
A uniform linear array consists of $N = 8$ isotropic elements spaced $d = \frac{\lambda}{2}$ apart along the $z$-axis. The excitation phase difference between adjacent elements is $\beta = 0$.
1. Derive the normalized array factor expression $|\text{AF}_n(\theta)|$.
2. Calculate the exact angles $\theta_{\text{null}}$ where the array factor vanishes (first nulls on either side of the broadside maximum).
3. Compute the First-Null Beamwidth ($\text{FNBW}$) in degrees.
4. Calculate the Half-Power Beamwidth ($\text{HPBW}$) using the small-angle approximation $\text{HPBW} \approx \frac{0.886 \lambda}{N d}$ and compare against the exact numerical solution.

### Problem 2: Phased Array Beam Steering
The array from Problem 1 is modified to electronically steer the main beam to angle $\theta_0 = 45^\circ$.
1. Determine the required progressive phase shift $\beta$ in degrees and radians.
2. Determine if any grating lobes enter the visible space ($\theta \in [0, 180^\circ]$). Justify mathematically.
3. Compute the new First-Null Beamwidth ($\text{FNBW}$) at this steered angle.

### Problem 3: Python Radiation Pattern Synthesis
Write a Python script using NumPy and Matplotlib to:
1. Plot the polar radiation pattern of the broadside array ($\theta_0 = 90^\circ$) in decibels down to $-40\text{ dB}$.
2. Plot the polar radiation pattern of the steered array ($\theta_0 = 45^\circ$) on the same figure.
3. Calculate and display the maximum side lobe level (SLL) relative to the main beam in $\text{dB}$.

