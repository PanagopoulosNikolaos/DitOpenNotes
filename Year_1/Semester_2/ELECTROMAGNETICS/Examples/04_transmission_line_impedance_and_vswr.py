"""Calculates characteristic impedance, reflection coefficient, and VSWR for RF transmission lines."""

import cmath
from typing import Dict


class TransmissionLineAnalyzer:
    """Calculates transmission line high-frequency reflection metrics and standing wave parameters."""

    def __init__(self, z0: complex, z_load: complex) -> None:
        """Initializes analyzer with characteristic and load impedances.

        Args:
            z0 (complex): Line characteristic impedance in Ohms.
            z_load (complex): Terminating load impedance in Ohms.
        """
        self.z0 = z0
        self.z_load = z_load

    def computeReflectionCoefficient(self) -> complex:
        """Calculates voltage reflection coefficient Gamma = (Z_L - Z_0) / (Z_L + Z_0).

        Returns:
            complex: Complex voltage reflection coefficient.
        """
        return (self.z_load - self.z0) / (self.z_load + self.z0)

    def computeVswr(self) -> float:
        """Calculates Voltage Standing Wave Ratio VSWR = (1 + |Gamma|) / (1 - |Gamma|).

        Returns:
            float: Dimensionless VSWR metric (>= 1.0).
        """
        gamma_mag = abs(self.computeReflectionCoefficient())
        if gamma_mag >= 1.0:
            return float("inf") # Complete reflection
        return (1.0 + gamma_mag) / (1.0 - gamma_mag)

    def computeReport(self) -> Dict[str, str]:
        """Compiles analytical report of transmission line termination behavior.

        Returns:
            Dict[str, str]: Key-value pairs summarizing line behavior.
        """
        gamma = self.computeReflectionCoefficient()
        vswr = self.computeVswr()
        return_loss_db = -20.0 * cmath.log10(abs(gamma)).real if abs(gamma) > 0 else float("inf")

        return {
            "Characteristic Z0": f"{self.z0.real:.1f} + {self.z0.imag:.1f}j Ohm",
            "Load Z_L": f"{self.z_load.real:.1f} + {self.z_load.imag:.1f}j Ohm",
            "Reflection Coefficient Gamma": f"{gamma.real:.4f} + {gamma.imag:.4f}j (|Gamma| = {abs(gamma):.4f})",
            "VSWR": f"{vswr:.3f}",
            "Return Loss": f"{return_loss_db:.2f} dB" if return_loss_db != float("inf") else "Infinite (Matched)"
        }


def main() -> None:
    """Demonstrates transmission line reflection and standing wave calculations."""
    line_z0 = 50.0 + 0j # 50 Ohm coaxial cable
    load_cases = [
        50.0 + 0j,         # Matched load
        100.0 + 0j,        # Resistive mismatch
        25.0 + 40.0j,      # Complex impedance mismatch
        0.0 + 0j           # Short circuit
    ]

    for load in load_cases:
        analyzer = TransmissionLineAnalyzer(line_z0, load)
        report = analyzer.computeReport()
        print(f"=== Transmission Analysis for Z_L = {load} ===")
        for key, val in report.items():
            print(f"  {key:<30}: {val}")
        print()


if __name__ == "__main__":
    main()

