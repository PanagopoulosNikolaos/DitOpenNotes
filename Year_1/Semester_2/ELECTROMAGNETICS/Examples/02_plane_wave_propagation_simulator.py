"""Simulates 1D plane wave attenuation, phase velocity, and Poynting power density in arbitrary media."""

import cmath
import math
from typing import Dict

SPEED_OF_LIGHT = 299792458.0  # Speed of light in vacuum (m/s)
MU_0 = 4.0 * math.pi * 1e-7   # Permeability of free space (H/m)
EPSILON_0 = 8.8541878128e-12  # Permittivity of free space (F/m)


class PlaneWaveMedium:
    """Calculates electromagnetic wave parameters across lossy and lossless media."""

    def __init__(
        self, 
        freq_hz: float, 
        eps_r: float = 1.0, 
        mu_r: float = 1.0, 
        sigma_s_per_m: float = 0.0
    ) -> None:
        """Initializes material electromagnetic properties and operating frequency.
        
        Args:
            freq_hz (float): Operating frequency in Hertz.
            eps_r (float): Relative permittivity (dielectric constant).
            mu_r (float): Relative permeability.
            sigma_s_per_m (float): Specific conductivity in Siemens per meter.
        """
        self.freq = freq_hz
        self.omega = 2.0 * math.pi * freq_hz
        self.eps = eps_r * EPSILON_0
        self.mu = mu_r * MU_0
        self.sigma = sigma_s_per_m

    def computeParameters(self) -> Dict[str, float]:
        """Calculates attenuation, phase constant, wave velocity, and impedance.
        
        Returns:
            Dict[str, float]: Physical wave metrics dictionary.
        """
        # Complex propagation constant: gamma = sqrt(j * omega * mu * (sigma + j * omega * eps))
        complex_eps = complex(self.eps, -self.sigma / self.omega)
        gamma = 1j * self.omega * cmath.sqrt(self.mu * complex_eps)
        alpha = gamma.real  # Attenuation constant (Np/m)
        beta = gamma.imag   # Phase constant (rad/m)

        phase_velocity = self.omega / beta
        wavelength = 2.0 * math.pi / beta
        skin_depth = 1.0 / alpha if alpha > 1e-12 else float("inf")

        # Intrinsic wave impedance: eta = sqrt(j * omega * mu / (sigma + j * omega * eps))
        eta = cmath.sqrt((1j * self.omega * self.mu) / (self.sigma + 1j * self.omega * self.eps))

        return {
            "alpha_np_per_m": alpha,
            "beta_rad_per_m": beta,
            "wavelength_m": wavelength,
            "phase_velocity_m_per_s": phase_velocity,
            "skin_depth_m": skin_depth,
            "eta_magnitude_ohms": abs(eta),
            "eta_phase_deg": math.degrees(cmath.phase(eta))
        }

    def computeFieldAtDistance(self, e0: float, z_meters: float, t_seconds: float) -> float:
        """Computes instantaneous electric field amplitude at distance z and time t.
        
        Args:
            e0 (float): Initial surface electric field amplitude in V/m.
            z_meters (float): Propagation distance in meters.
            t_seconds (float): Instant in time in seconds.
            
        Returns:
            float: Instantaneous field value in V/m.
        """
        params = self.computeParameters()
        decay = math.exp(-params["alpha_np_per_m"] * z_meters)
        oscillation = math.cos(self.omega * t_seconds - params["beta_rad_per_m"] * z_meters)
        return e0 * decay * oscillation


def main() -> None:
    """Executes wave simulation across seawater and free space."""
    freq = 1e6  # 1 MHz wave

    free_space = PlaneWaveMedium(freq_hz=freq, eps_r=1.0, sigma_s_per_m=0.0)
    seawater = PlaneWaveMedium(freq_hz=freq, eps_r=81.0, sigma_s_per_m=4.0)

    print(f"Simulation Frequency: {freq / 1e6:.1f} MHz\n")

    for name, medium in [("Free Space (Vacuum)", free_space), ("Seawater", seawater)]:
        p = medium.computeParameters()
        print(f"=== Medium: {name} ===")
        print(f"Attenuation Constant (alpha): {p['alpha_np_per_m']:.4e} Np/m")
        print(f"Phase Constant (beta):        {p['beta_rad_per_m']:.4e} rad/m")
        print(f"Phase Velocity:               {p['phase_velocity_m_per_s']:.4e} m/s")
        print(f"Wavelength:                   {p['wavelength_m']:.4f} m")
        print(f"Skin Depth:                   {p['skin_depth_m']:.4f} m")
        print(f"Wave Impedance (|eta|):       {p['eta_magnitude_ohms']:.2f} Ohms\n")


if __name__ == "__main__":
    main()

