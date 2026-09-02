"""Demonstrates a standard multi-client TCP Echo Server using Python sockets.

Binds to localhost, listens for incoming TCP connections, and echoes
received data back to the client until disconnected.
"""

import socket
import sys

HOST = "127.0.0.1"
PORT = 65432


def run_echo_server(host: str = HOST, port: int = PORT) -> None:
    """Starts the TCP echo server.

    Args:
        host (str): IP address or hostname to bind.
        port (int): TCP port number to listen on.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
        server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_sock.bind((host, port))
        server_sock.listen(5)
        print(f"[TCP Server] Listening on {host}:{port}...")

        try:
            conn, addr = server_sock.accept()
            with conn:
                print(f"[TCP Server] Connected by client at {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(f"[TCP Server] Received: {data.decode('utf-8', errors='replace')}")
                    conn.sendall(data)
        except KeyboardInterrupt:
            print("\n[TCP Server] Shutting down.")


if __name__ == "__main__":
    run_echo_server()
