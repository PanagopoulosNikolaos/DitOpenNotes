"""IPv4 Subnet and CIDR Calculator.

Calculates network address, broadcast address, netmask, wildcard mask,
usable host range, and total host capacity using python standard library.
"""

import ipaddress
import sys
from typing import Dict, Any


def calculate_subnet(cidr_str: str) -> Dict[str, Any]:
    """Calculates all key IPv4 subnet parameters for a given CIDR notation.

    Args:
        cidr_str (str): CIDR network representation (e.g., '172.16.45.130/22').

    Returns:
        Dict[str, Any]: Dictionary containing network parameters.
    """
    interface = ipaddress.IPv4Interface(cidr_str)
    network = interface.network

    usable_hosts = list(network.hosts())
    first_host = usable_hosts[0] if usable_hosts else None
    last_host = usable_hosts[-1] if usable_hosts else None
    total_usable = len(usable_hosts)

    # Calculate wildcard mask
    netmask_int = int(network.netmask)
    wildcard_int = ~netmask_int & 0xFFFFFFFF
    wildcard_mask = str(ipaddress.IPv4Address(wildcard_int))

    return {
        "input_ip": str(interface.ip),
        "prefix_len": interface.network.prefixlen,
        "network_address": str(network.network_address),
        "broadcast_address": str(network.broadcast_address),
        "netmask": str(network.netmask),
        "wildcard_mask": wildcard_mask,
        "first_usable_host": str(first_host) if first_host else "N/A",
        "last_usable_host": str(last_host) if last_host else "N/A",
        "total_usable_hosts": total_usable,
        "is_private": network.is_private
    }


def print_subnet_info(info: Dict[str, Any]) -> None:
    """Formats and prints subnet calculation details.

    Args:
        info (Dict[str, Any]): Dictionary of subnet parameters.
    """
    print("=" * 55)
    print(f"IPv4 Subnet Analysis for: {info['input_ip']}/{info['prefix_len']}")
    print("=" * 55)
    print(f"Network Address:    {info['network_address']}")
    print(f"Broadcast Address:  {info['broadcast_address']}")
    print(f"Subnet Mask:        {info['netmask']}")
    print(f"Wildcard Mask:      {info['wildcard_mask']}")
    print(f"Usable Host Range:  {info['first_usable_host']} - {info['last_usable_host']}")
    print(f"Total Usable Hosts: {info['total_usable_hosts']}")
    print(f"Private Network:    {info['is_private']}")
    print("=" * 55)


def main() -> None:
    """Demonstrates subnet calculations on common student exam scenarios."""
    test_subnets = ["172.16.45.130/22", "192.168.10.0/26", "10.0.0.0/29"]
    for cidr in test_subnets:
        res = calculate_subnet(cidr)
        print_subnet_info(res)
        print()


if __name__ == "__main__":
    main()
