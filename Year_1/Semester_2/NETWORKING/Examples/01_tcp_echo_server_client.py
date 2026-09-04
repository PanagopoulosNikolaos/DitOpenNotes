"""Demonstrates a standalone TCP client-server exchange using socket abstractions."""

import socket
import threading
from typing import Tuple


class EchoServer:
    """Manages an IPv4 TCP server socket responding to incoming client payloads."""

    def __init__(self, host: str = "127.0.0.1", port: int = 0) -> None:
        """Initializes server binding parameters.
        
        Args:
            host (str): Listening IP address.
            port (int): Port number (0 selects an ephemeral OS-assigned port).
        """
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.host, self.port))
        self.port = self.socket.getsockname()[1]  # Resolves assigned port
        self.is_running = False

    def start(self) -> None:
        """Starts listening and spawns the connection listener thread."""
        self.socket.listen(1)
        self.is_running = True
        self.listener_thread = threading.Thread(target=self._listenLoop, daemon=True)
        self.listener_thread.start()

    def _listenLoop(self) -> None:
        """Internal accept loop receiving and responding to client messages."""
        try:
            client_sock, _ = self.socket.accept()
            with client_sock:
                data = client_sock.recv(1024)
                if data:
                    reply = b"ACK: " + data
                    client_sock.sendall(reply)
        except OSError:
            pass  # Handles clean socket closure during termination

    def stop(self) -> None:
        """Closes the server socket descriptor."""
        self.is_running = False
        self.socket.close()


def sendEchoRequest(server_host: str, server_port: int, message: str) -> str:
    """Connects to an active TCP server, transmits text, and returns the response.
    
    Args:
        server_host (str): Destination server IP.
        server_port (int): Destination port number.
        message (str): Text payload to transmit.
        
    Returns:
        str: Decoded server response string.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_sock:
        client_sock.connect((server_host, server_port))
        client_sock.sendall(message.encode("utf-8"))
        response = client_sock.recv(1024)
        return response.decode("utf-8")


def main() -> None:
    """Runs a self-contained local TCP echo exchange."""
    server = EchoServer(host="127.0.0.1", port=0)
    server.start()

    print(f"Ephemeral Echo Server running on port {server.port}")
    test_msg = "Ping Packet 001"
    response = sendEchoRequest("127.0.0.1", server.port, test_msg)
    print(f"Client Sent:     {test_msg}")
    print(f"Client Received: {response}")

    server.stop()


if __name__ == "__main__":
    main()

