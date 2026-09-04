"""Computes IPv4 subnetting parameters, network addresses, and usable IP ranges."""

from typing import Dict, List


class SubnetCalculator:
    """Calculates IPv4 subnet parameters from CIDR notation."""

    def __init__(self, cidr_input: str) -> None:
        """Initializes calculator with address in format 'IP/Prefix'.
        
        Args:
            cidr_input (str): Target address string, e.g. '192.168.10.45/26'.
            
        Raises:
            ValueError: If the input IP format or prefix length is invalid.
        """
        parts = cidr_input.strip().split("/")
        if len(parts) != 2:
            raise ValueError("Input must follow format 'IP/Prefix'")

        self.ip_str = parts[0]
        self.prefix_len = int(parts[1])

        if not (0 <= self.prefix_len <= 32):
            raise ValueError("Prefix length must reside in range [0, 32]")

        self.ip_int = self._ipToInt(self.ip_str)
        self.mask_int = (0xFFFFFFFF << (32 - self.prefix_len)) & 0xFFFFFFFF

    @staticmethod
    def _ipToInt(ip_str: str) -> int:
        """Converts dotted-decimal string into 32-bit integer.
        
        Args:
            ip_str (str): Dotted-decimal IPv4 address.
            
        Returns:
            int: 32-bit unsigned representation.
        """
        octets = [int(x) for x in ip_str.split(".")]
        return (octets[0] << 24) | (octets[1] << 16) | (octets[2] << 8) | octets[3]

    @staticmethod
    def _intToIp(ip_int: int) -> str:
        """Converts 32-bit integer into dotted-decimal IPv4 string.
        
        Args:
            ip_int (int): 32-bit unsigned address integer.
            
        Returns:
            str: Dotted-decimal string.
        """
        return f"{(ip_int >> 24) & 0xFF}.{(ip_int >> 16) & 0xFF}.{(ip_int >> 8) & 0xFF}.{ip_int & 0xFF}"

    def computeReport(self) -> Dict[str, str]:
        """Calculates subnet boundaries and returns a formatted metric report.
        
        Returns:
            Dict[str, str]: Key-value pairs of subnet parameters.
        """
        network_int = self.ip_int & self.mask_int
        broadcast_int = network_int | (~self.mask_int & 0xFFFFFFFF)

        host_bits = 32 - self.prefix_len
        total_hosts = 2 ** host_bits
        usable_hosts = total_hosts - 2 if host_bits >= 2 else 0

        first_host_int = network_int + 1 if usable_hosts > 0 else network_int
        last_host_int = broadcast_int - 1 if usable_hosts > 0 else broadcast_int

        return {
            "CIDR": f"{self.ip_str}/{self.prefix_len}",
            "Subnet Mask": self._intToIp(self.mask_int),
            "Network Address": self._intToIp(network_int),
            "Broadcast Address": self._intToIp(broadcast_int),
            "First Usable Host": self._intToIp(first_host_int),
            "Last Usable Host": self._intToIp(last_host_int),
            "Total Addresses": str(total_hosts),
            "Usable Hosts": str(usable_hosts)
        }


def main() -> None:
    """Runs demonstration of subnet calculation across sample addresses."""
    test_subnets: List[str] = [
        "192.168.1.135/27",
        "10.50.12.0/22",
        "172.16.80.200/20"
    ]

    for cidr in test_subnets:
        calc = SubnetCalculator(cidr)
        report = calc.computeReport()
        print(f"=== Subnet Analysis for {cidr} ===")
        for key, value in report.items():
            print(f"{key:<20}: {value}")
        print()


if __name__ == "__main__":
    main()

