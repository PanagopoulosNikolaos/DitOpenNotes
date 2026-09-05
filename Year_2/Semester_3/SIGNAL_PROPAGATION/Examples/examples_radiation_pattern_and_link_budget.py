#!/usr/bin/env python3
"""Calculates antenna radiation patterns and RF link budgets.

This module computes normalized far-field radiation patterns for half-wave
dipoles and uniform linear arrays (ULA), and evaluates Friis transmission
link budgets.
"""

import numpy as np


def computeDipoleField(theta: np.ndarray) -> np.ndarray:
    """Calculates the normalized far-field pattern for a half-wave dipole.

    Args:
        theta (np.ndarray): Polar elevation angle array in radians [0, 2*pi].

    Returns:
        np.ndarray: Normalized electric field magnitude values.
    """
    sin_theta = np.sin(theta)
    # Replaces pole singularities with small epsilon to prevent zero division.
    sin_theta = np.where(np.abs(sin_theta) < 1e-6, 1e-6, sin_theta)
    field_magnitude = np.abs(np.cos(0.5 * np.pi * np.cos(theta)) / sin_theta)
    return field_magnitude


def computeArrayFactor(
    num_elements: int,
    spacing_ratio: float,
    phase_shift_rad: float,
    theta: np.ndarray
) -> np.ndarray:
    """Calculates the normalized array factor for a uniform linear array.

    Args:
        num_elements (int): Number of antenna elements in the linear array.
        spacing_ratio (float): Inter-element spacing normalized by wavelength (d/lambda).
        phase_shift_rad (float): Progressive inter-element phase excitation in radians.
        theta (np.ndarray): Observation angle array in radians.

    Returns:
        np.ndarray: Normalized array factor values in range [0.0, 1.0].
    """
    psi = 2.0 * np.pi * spacing_ratio * np.cos(theta) + phase_shift_rad
    numerator = np.sin(0.5 * num_elements * psi)
    denominator = num_elements * np.sin(0.5 * psi)
    # Applies limit value of 1.0 when denominator approaches zero at psi = 0.
    with np.errstate(divide="ignore", invalid="ignore"):
        array_factor = np.where(
            np.abs(np.sin(0.5 * psi)) < 1e-7,
            1.0,
            np.abs(numerator / denominator)
        )
    return array_factor


def calculateLinkBudget(
    freq_mhz: float,
    distance_km: float,
    tx_power_dbm: float,
    tx_gain_dbi: float,
    rx_gain_dbi: float,
    cable_loss_db: float = 2.0
) -> tuple[float, float]:
    """Evaluates received RF power using the Friis transmission equation.

    Args:
        freq_mhz (float): Operating carrier frequency in Megahertz.
        distance_km (float): Line-of-sight propagation distance in kilometers.
        tx_power_dbm (float): Transmitter output power in dBm.
        tx_gain_dbi (float): Transmitter antenna directivity gain in dBi.
        rx_gain_dbi (float): Receiver antenna directivity gain in dBi.
        cable_loss_db (float): Combined insertion and cable losses in dB. Default is 2.0.

    Returns:
        tuple[float, float]: Pair containing received power (dBm) and free space path loss (dB).
    """
    free_space_loss = 32.44 + 20.0 * np.log10(distance_km) + 20.0 * np.log10(freq_mhz)
    rx_power_dbm = tx_power_dbm + tx_gain_dbi + rx_gain_dbi - free_space_loss - cable_loss_db
    return rx_power_dbm, free_space_loss


def main() -> None:
    """Executes demonstration of dipole radiation and RF link budget evaluation.

    Args:
        None.

    Returns:
        None.
    """
    theta = np.linspace(0.0, 2.0 * np.pi, 720)

    # Computes half-wave dipole pattern.
    dipole_pattern = computeDipoleField(theta)

    # Computes 8-element broadside linear array pattern.
    af_broadside = computeArrayFactor(
        num_elements=8,
        spacing_ratio=0.5,
        phase_shift_rad=0.0,
        theta=theta
    )

    # Computes steered linear array pattern to 45 degrees.
    steer_angle_rad = np.radians(45.0)
    steer_phase_rad = -2.0 * np.pi * 0.5 * np.cos(steer_angle_rad)
    af_steered = computeArrayFactor(
        num_elements=8,
        spacing_ratio=0.5,
        phase_shift_rad=steer_phase_rad,
        theta=theta
    )

    # Evaluates point-to-point link budget parameters.
    carrier_freq_mhz = 2400.0
    link_distance_km = 3.5
    tx_power_dbm = 23.0
    tx_gain_dbi = 12.0
    rx_gain_dbi = 6.0

    rx_power, path_loss = calculateLinkBudget(
        freq_mhz=carrier_freq_mhz,
        distance_km=link_distance_km,
        tx_power_dbm=tx_power_dbm,
        tx_gain_dbi=tx_gain_dbi,
        rx_gain_dbi=rx_gain_dbi
    )

    print("--- RF Link Budget Analysis ---")
    print(f"Carrier Frequency:     {carrier_freq_mhz:.1f} MHz")
    print(f"Path Distance:         {link_distance_km:.2f} km")
    print(f"Free Space Path Loss:  {path_loss:.2f} dB")
    print(f"Transmit Power:        {tx_power_dbm:.1f} dBm")
    print(f"Antenna Gains (Tx/Rx): {tx_gain_dbi:.1f} dBi / {rx_gain_dbi:.1f} dBi")
    received_picowatts = 10 ** (rx_power / 10.0) * 1e6
    print(f"Received Power (Pr):   {rx_power:.2f} dBm ({received_picowatts:.4f} pW)")


if __name__ == "__main__":
    main()
