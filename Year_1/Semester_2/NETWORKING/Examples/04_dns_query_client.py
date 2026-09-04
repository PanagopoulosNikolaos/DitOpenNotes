"""Constructs and transmits raw DNS A-record query packets over UDP port 53 and parses IP responses."""

import socket
import struct
from typing import List


class DnsQueryClient:
    """Builds raw wire-format DNS queries and extracts resolved IPv4 addresses."""

    def __init__(self, dns_server: str = "8.8.8.8", port: int = 53, timeout: float = 2.0) -> None:
        """Initializes DNS resolver client.

        Args:
            dns_server (str): IP address of recursive DNS server.
            port (int): UDP port number (standard 53).
            timeout (float): Socket read timeout in seconds.
        """
        self.dns_server = dns_server
        self.port = port
        self.timeout = timeout

    @staticmethod
    def _encodeDomainName(domain: str) -> bytes:
        """Encodes domain name into DNS length-prefixed label format.

        Args:
            domain (str): Dotted domain name, e.g. 'example.com'.

        Returns:
            bytes: Encoded wire-format representation.
        """
        encoded = b""
        for part in domain.strip(".").split("."):
            part_bytes = part.encode("ascii")
            encoded += struct.pack("!B", len(part_bytes)) + part_bytes
        return encoded + b"\x00"

    def buildQuery(self, domain: str, transaction_id: int = 0x1A2B) -> bytes:
        """Assembles standard 12-byte DNS header and question section for Type A query.

        Args:
            domain (str): Target domain name.
            transaction_id (int): 16-bit transaction identifier.

        Returns:
            bytes: Binary DNS packet.
        """
        # Flags: Standard query (0), Opcode 0, RD (Recursion Desired = 1) -> 0x0100
        flags = 0x0100
        qdcount = 1 # 1 question
        ancount = 0
        nscount = 0
        arcount = 0

        header = struct.pack("!HHHHHH", transaction_id, flags, qdcount, ancount, nscount, arcount)
        qname = self._encodeDomainName(domain)
        qtype = 1  # Type A (IPv4)
        qclass = 1 # Class IN (Internet)
        question = qname + struct.pack("!HH", qtype, qclass)

        return header + question

    def query(self, domain: str) -> List[str]:
        """Transmits DNS query to upstream resolver and parses resolved IPv4 addresses.

        Args:
            domain (str): Target domain name.

        Returns:
            List[str]: List of resolved IPv4 addresses.
        """
        packet = self.buildQuery(domain)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(self.timeout)

        try:
            sock.sendto(packet, (self.dns_server, self.port))
            response, _ = sock.recvfrom(2048)
        except (socket.timeout, socket.error):
            return []
        finally:
            sock.close()

        # Parses response records
        answers: List[str] = []
        if len(response) < 12:
            return answers

        ancount = struct.unpack("!H", response[6:8])[0]
        if ancount == 0:
            return answers

        # Skips header (12 bytes) and question section
        idx = 12
        while response[idx] != 0:
            idx += 1 + response[idx]
        idx += 5 # Skips null byte, QTYPE (2), QCLASS (2)

        # Scans answer resource records
        for _ in range(ancount):
            if idx >= len(response):
                break
            # Checks pointer compression (0xC0)
            if (response[idx] & 0xC0) == 0xC0:
                idx += 2
            else:
                while response[idx] != 0:
                    idx += 1 + response[idx]
                idx += 1

            rtype, rclass, _, rdlength = struct.unpack("!HHIH", response[idx:idx + 10])
            idx += 10
            if rtype == 1 and rdlength == 4: # Type A
                ip_bytes = response[idx:idx + 4]
                ip_str = ".".join(str(b) for b in ip_bytes)
                answers.append(ip_str)
            idx += rdlength

        return answers


def main() -> None:
    """Demonstrates DNS query packet building and resolution."""
    client = DnsQueryClient(dns_server="8.8.8.8")
    target = "example.com"
    print(f"=== Resolving '{target}' via {client.dns_server}:{client.port} ===")
    packet = client.buildQuery(target)
    print(f"Wire query size: {len(packet)} bytes")
    # Simulation display
    print("DNS Query Packet built successfully with Recursion Desired (RD=1).")


if __name__ == "__main__":
    main()

