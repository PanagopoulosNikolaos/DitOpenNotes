#!/usr/bin/env python3
"""
File: examples_radiation_pattern_and_link_budget.py
Description: Computes and plots radiation patterns for half-wave dipoles and
uniform linear arrays, and performs RF link budget calculations.
"""

import numpy as np
import matplotlib.pyplot as plt

def compute_dipole_field(theta):
    """
    Computes normalized electric field for a half-wave dipole.
    """
    sin_theta = np.sin(theta)
    # Avoid division by zero at poles
    sin_theta = np.where(np.abs(sin_theta) < 1e-6, 1e-6, sin_theta)
    field = np.abs(np.cos(0.5 * np.pi * np.cos(theta)) / sin_theta)
    return field

def compute_array_factor(N, d_over_lambda, beta_rad, theta):
    """
    Computes normalized array factor |AF_n(theta)| for an N-element ULA.
    """
    psi = 2.0 * np.pi * d_over_lambda * np.cos(theta) + beta_rad
    numerator = np.sin(0.5 * N * psi)
    denominator = N * np.sin(0.5 * psi)
    # Handle indeterminate form 0/0 at psi = 0 via limit = 1.0
    with np.errstate(divide='ignore', invalid='ignore'):
        af = np.where(np.abs(np.sin(0.5 * psi)) < 1e-7, 1.0, np.abs(numerator / denominator))
    return af

def calculate_link_budget(f_mhz, distance_km, pt_dbm, gt_dbi, gr_dbi, l_cable_db=2.0):
    """
    Calculates received power using the Friis transmission equation in dBm.
    """
    fspl_db = 32.44 + 20.0 * np.log10(distance_km) + 20.0 * np.log10(f_mhz)
    pr_dbm = pt_dbm + gt_dbi + gr_dbi - fspl_db - l_cable_db
    return pr_dbm, fspl_db

def main():
    theta = np.linspace(0.0, 2.0 * np.pi, 720)

    # 1. Half-Wave Dipole Pattern
    dipole_pat = compute_dipole_field(theta)

    # 2. 8-Element Broadside ULA (d = 0.5 lambda, beta = 0)
    af_broadside = compute_array_factor(N=8, d_over_lambda=0.5, beta_rad=0.0, theta=theta)

    # 3. 8-Element Steered ULA (theta_0 = 45 deg, beta = -kd*cos(45))
    theta_0 = np.radians(45.0)
    beta_steered = -2.0 * np.pi * 0.5 * np.cos(theta_0)
    af_steered = compute_array_factor(N=8, d_over_lambda=0.5, beta_rad=beta_steered, theta=theta)

    # 4. RF Link Budget Evaluation
    f_carrier = 2400.0  # MHz (2.4 GHz)
    r_dist = 3.5        # km
    pt = 23.0           # dBm (200 mW)
    gt = 12.0           # dBi
    gr = 6.0            # dBi

    pr, fspl = calculate_link_budget(f_carrier, r_dist, pt, gt, gr)

    print("--- RF Link Budget Analysis ---")
    print(f"Carrier Frequency:     {f_carrier:.1f} MHz")
    print(f"Path Distance:         {r_dist:.2f} km")
    print(f"Free Space Path Loss:  {fspl:.2f} dB")
    print(f"Transmit Power:        {pt:.1f} dBm")
    print(f"Antenna Gains (Tx/Rx): {gt:.1f} dBi / {gr:.1f} dBi")
    print(f"Received Power (Pr):   {pr:.2f} dBm ({10**(pr/10.0)*1e6:.4f} pW)")

if __name__ == "__main__":
    main()

