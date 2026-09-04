"""Demonstrates UDP socket communication, ping latency measurement, and packet loss detection."""

import socket
import time
from typing import Optional, Tuple


class UdpPingManager:
    """Manages UDP ping transmission and latency benchmarking."""

    def __init__(self, host: str = "127.0.0.1", port: int = 12000, timeout: float = 1.0) -> None:
        """Initializes ping manager with destination address and socket timeout.

        Args:
            host (str): Target hostname or IPv4 address.
            port (int): Target UDP port.
            timeout (float): Socket receive timeout in seconds.
        """
        self.host = host
        self.port = port
        self.timeout = timeout

    def sendPing(self, sequence_num: int) -> Tuple[bool, Optional[float]]:
        """Transmits an individual UDP ping packet and measures round-trip time.

        Args:
            sequence_num (int): Monotonically increasing ping sequence identifier.

        Returns:
            Tuple[bool, Optional[float]]: (Success flag, RTT in milliseconds if received).
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(self.timeout)

        send_time = time.time()
        message = f"PING {sequence_num} {send_time}".encode("utf-8")

        try:
            sock.sendto(message, (self.host, self.port))
            data, _ = sock.recvfrom(1024)
            recv_time = time.time()
            rtt_ms = (recv_time - send_time) * 1000.0
            return True, rtt_ms
        except socket.timeout:
            return False, None # Signals packet loss or unresponsive peer
        finally:
            sock.close()


def main() -> None:
    """Executes demonstration of UDP ping benchmarking."""
    print("=== UDP Ping Latency Test Demonstration ===")
    manager = UdpPingManager(host="127.0.0.1", port=12000, timeout=0.5)

    # Simulates ping sequence against local port
    print(f"Targeting {manager.host}:{manager.port} with timeout {manager.timeout}s...")
    for seq in range(1, 4):
        success, rtt = manager.sendPing(seq)
        if success and rtt is not None:
            print(f"Reply from {manager.host}: seq={seq} time={rtt:.2f} ms")
        else:
            print(f"Request timed out for seq={seq}")


if __name__ == "__main__":
    main()

