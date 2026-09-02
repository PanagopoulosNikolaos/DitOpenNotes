"""Demonstrates an asynchronous connectionless UDP Server using Python sockets.

Receives datagrams and responds back to the client socket address.
"""

import socket

HOST = "127.0.0.1"
PORT = 65433


def run_udp_server(host: str = HOST, port: int = PORT) -> None:
    """Starts the UDP datagram server.

    Args:
        host (str): IP address or hostname to bind.
        port (int): UDP port number to listen on.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind((host, port))
        print(f"[UDP Server] Listening for datagrams on {host}:{port}...")

        try:
            while True:
                data, addr = sock.recvfrom(1024)
                text = data.decode("utf-8", errors="replace")
                print(f"[UDP Server] Received '{text}' from {addr}")
                reply = f"ACK: {text}".encode("utf-8")
                sock.sendto(reply, addr)
        except KeyboardInterrupt:
            print("\n[UDP Server] Shutting down.")


if __name__ == "__main__":
    run_udp_server()
