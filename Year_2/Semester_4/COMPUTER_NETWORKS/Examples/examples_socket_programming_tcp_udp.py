"""Socket programming demonstrations implementing TCP and UDP client-server communication.

Provides minimal, self-contained socket implementations in standard Python
to illustrate process-to-process communication over transport layer protocols.
"""

import socket
import threading
import time


def runTcpServer(host: str = "127.0.0.1", port: int = 9001) -> None:
    """Runs a multithreaded TCP echo server.

    Args:
        host (str): Listening IP interface.
        port (int): Listening TCP port.
    """
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Allows immediate reuse of the address port after process termination
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind((host, port))
    server_sock.listen(5)
    print(f"[TCP Server] Listening on {host}:{port}")

    def handleClient(conn: socket.socket, addr: tuple[str, int]) -> None:
        """Handles single incoming client connection lifecycle."""
        with conn:
            print(f"[TCP Server] Connection accepted from {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break # Client closed connection via FIN handshake
                # Echoes received payload back to client
                conn.sendall(data)
            print(f"[TCP Server] Client {addr} disconnected")

    try:
        conn, addr = server_sock.accept()
        handleClient(conn, addr)
    finally:
        server_sock.close()


def runTcpClient(host: str = "127.0.0.1", port: int = 9001, message: str = "Network Protocol Test") -> str:
    """Executes a single TCP client query and retrieves server echo.

    Args:
        host (str): Destination server IP address.
        port (int): Destination server TCP port.
        message (str): Text message to transmit.

    Returns:
        str: Echoed text response received from server.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_sock:
        # Initiates TCP three-way handshake (SYN -> SYN-ACK -> ACK)
        client_sock.connect((host, port))
        client_sock.sendall(message.encode("utf-8"))
        response = client_sock.recv(1024)
        return response.decode("utf-8")


def runUdpEchoPair(host: str = "127.0.0.1", port: int = 9002) -> None:
    """Demonstrates connectionless datagram exchange over UDP.

    Args:
        host (str): Loopback IP interface for datagram delivery.
        port (int): Target UDP port.
    """
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_sock.bind((host, port))

    def serverWorker() -> None:
        data, addr = server_sock.recvfrom(1024)
        # Responds directly without prior session setup
        server_sock.sendto(data.upper(), addr)
        server_sock.close()

    server_thread = threading.Thread(target=serverWorker)
    server_thread.start()

    time.sleep(0.05) # Yields briefly to ensure server socket binding completion

    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_sock.sendto(b"udp datagram packet", (host, port))
    reply, _ = client_sock.recvfrom(1024)
    print(f"[UDP Client] Received echo: {reply.decode('utf-8')}")
    client_sock.close()
    server_thread.join()


if __name__ == "__main__":
    print("Executing UDP loopback test:")
    runUdpEchoPair()

