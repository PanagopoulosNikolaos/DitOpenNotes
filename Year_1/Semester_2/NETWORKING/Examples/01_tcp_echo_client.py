"""Demonstrates a TCP client connecting to the Echo Server.

Transmits messages and prints the echoed server response.
"""

import socket

HOST = "127.0.0.1"
PORT = 65432


def send_echo_message(message: str, host: str = HOST, port: int = PORT) -> str:
    """Connects to the server, transmits a message, and receives the echo.

    Args:
        message (str): Text message to transmit.
        host (str): Destination IP or hostname.
        port (int): Destination TCP port.

    Returns:
        str: Echoed response received from server.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        sock.sendall(message.encode("utf-8"))
        data = sock.recv(1024)
        return data.decode("utf-8", errors="replace")


def main() -> None:
    """Executes sample echo transmission."""
    test_msg = "Hello, Computer Networks Lab!"
    print(f"[TCP Client] Sending: '{test_msg}'")
    try:
        reply = send_echo_message(test_msg)
        print(f"[TCP Client] Received Echo: '{reply}'")
    except ConnectionRefusedError:
        print("[TCP Client] Error: Server is not running. Start 01_tcp_echo_server.py first.")


if __name__ == "__main__":
    main()
