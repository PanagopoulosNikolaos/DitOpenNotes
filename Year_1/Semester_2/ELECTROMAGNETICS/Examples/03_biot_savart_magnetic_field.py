"""Computes magnetic field intensity using the Biot-Savart law for finite straight wire segments and circular loops."""

import math
from typing import Tuple

MU_0 = 4.0 * math.pi * 1e-7 # Permeability of free space in H/m


class BiotSavartCalculator:
    """Provides numerical evaluation of magnetic fields from elementary current configurations."""

    @staticmethod
    def straightWireField(current: float, distance_rho: float) -> float:
        """Calculates B-field magnitude for an infinitely long straight conductor: B = (mu_0 * I) / (2 * pi * rho).

        Args:
            current (float): Electric current in Amperes.
            distance_rho (float): Radial perpendicular distance from conductor in meters.

        Returns:
            float: Magnetic flux density B in Tesla.
        """
        if distance_rho <= 0.0:
            raise ValueError("Perpendicular distance must be strictly positive.")
        return (MU_0 * current) / (2.0 * math.pi * distance_rho)

    @staticmethod
    def circularLoopOnAxisField(current: float, loop_radius: float, z_distance: float) -> float:
        """Calculates axial B-field for a circular current loop: B_z = (mu_0 * I * a^2) / (2 * (a^2 + z^2)^(3/2)).

        Args:
            current (float): Loop current in Amperes.
            loop_radius (float): Radius of loop in meters.
            z_distance (float): Axial distance along loop center axis in meters.

        Returns:
            float: Axial magnetic field B_z in Tesla.
        """
        numerator = MU_0 * current * (loop_radius ** 2)
        denominator = 2.0 * ((loop_radius ** 2 + z_distance ** 2) ** 1.5)
        return numerator / denominator


def main() -> None:
    """Executes demonstration of Biot-Savart magnetic field evaluations."""
    sample_current = 10.0 # 10 Amperes
    test_distance = 0.05  # 5 centimeters
    loop_radius = 0.1     # 10 centimeters

    b_wire = BiotSavartCalculator.straightWireField(sample_current, test_distance)
    b_loop_center = BiotSavartCalculator.circularLoopOnAxisField(sample_current, loop_radius, 0.0)
    b_loop_offset = BiotSavartCalculator.circularLoopOnAxisField(sample_current, loop_radius, 0.1)

    print("=== Biot-Savart Law Computations ===")
    print(f"B-field 5cm from 10A wire:       {b_wire * 1e6:.2f} microTesla")
    print(f"B-field at center of 10A loop:    {b_loop_center * 1e6:.2f} microTesla")
    print(f"B-field 10cm on-axis from loop:   {b_loop_offset * 1e6:.2f} microTesla")


if __name__ == "__main__":
    main()

