"""Demonstrates a UDP client transmitting datagrams and awaiting acknowledgment."""

import socket

HOST = "127.0.0.1"
PORT = 65433


def send_udp_datagram(message: str, host: str = HOST, port: int = PORT) -> str:
    """Sends a datagram and waits for a response.

    Args:
        message (str): Message payload to send.
        host (str): Destination host.
        port (int): Destination UDP port.

    Returns:
        str: Server response.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.settimeout(2.0)
        sock.sendto(message.encode("utf-8"), (host, port))
        data, _ = sock.recvfrom(1024)
        return data.decode("utf-8", errors="replace")


def main() -> None:
    """Executes sample UDP datagram exchange."""
    message = "Testing UDP Datagram Delivery"
    print(f"[UDP Client] Sending: '{message}'")
    try:
        reply = send_udp_datagram(message)
        print(f"[UDP Client] Received Response: '{reply}'")
    except socket.timeout:
        print("[UDP Client] Request timed out. Ensure 02_udp_server.py is active.")


if __name__ == "__main__":
    main()
