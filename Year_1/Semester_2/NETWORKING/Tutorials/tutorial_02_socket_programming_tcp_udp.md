# Tutorial 02: Network Socket Programming in Python (TCP and UDP)

## Context and Grounding
This tutorial walks through building client-server network applications using standard BSD sockets in Python. It reinforces transport-layer communication mechanics covered in `Lectures/lecture_03_transport_and_application_protocols.md`.

---

## 1. Socket API Architecture

The Berkeley socket API provides the OS interface for network communication:
* `socket(AF_INET, SOCK_STREAM)`: Creates a reliable, byte-stream IPv4 TCP socket.
* `socket(AF_INET, SOCK_DGRAM)`: Creates an unacknowledged, message-oriented IPv4 UDP socket.

### Socket Lifecycle Summary
* **TCP Server**: `socket()` $\to$ `bind()` $\to$ `listen()` $\to$ `accept()` $\to$ `recv()` / `send()` $\to$ `close()`.
* **TCP Client**: `socket()` $\to$ `connect()` $\to$ `send()` / `recv()` $\to$ `close()`.
* **UDP Server**: `socket()` $\to$ `bind()` $\to$ `recvfrom()` / `sendto()` $\to$ `close()`.
* **UDP Client**: `socket()` $\to$ `sendto()` / `recvfrom()` $\to$ `close()`.

---

## 2. Implementation: Multi-Threaded TCP Server

```python
"""Multi-threaded TCP echo server demonstrating concurrent socket handling."""

import socket
import threading


def handleClient(conn: socket.socket, addr: tuple) -> None:
    """Handles an individual client connection session.
    
    Args:
        conn (socket.socket): The established client socket descriptor.
        addr (tuple): Tuple of (client_ip, client_port).
    """
    print(f"Accepted connection from {addr}")
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break  # Client closed connection cleanly
            conn.sendall(b"ECHO: " + data)
    finally:
        conn.close()
        print(f"Closed connection from {addr}")


def runServer(host: str = "127.0.0.1", port: int = 8080) -> None:
    """Binds and listens for incoming TCP client connections.
    
    Args:
        host (str): Listening IP address.
        port (int): Port number to bind.
    """
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind((host, port))
    server_sock.listen(5)
    print(f"Server listening on {host}:{port}...")

    try:
        while True:
            client_conn, client_addr = server_sock.accept()
            client_thread = threading.Thread(
                target=handleClient, 
                args=(client_conn, client_addr), 
                daemon=True
            )
            client_thread.start()
    except KeyboardInterrupt:
        print("\nTerminating server...")
    finally:
        server_sock.close()


if __name__ == "__main__":
    runServer()
```

---

## 3. Implementation: TCP Client

```python
"""TCP client communicating with the echo server."""

import socket


def runClient(server_host: str = "127.0.0.1", server_port: int = 8080) -> None:
    """Connects to server, transmits test message, and prints response.
    
    Args:
        server_host (str): Destination server IP.
        server_port (int): Destination port.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((server_host, server_port))
        message = "Hello from DitOpenNotes Networking Client"
        sock.sendall(message.encode("utf-8"))

        response = sock.recv(1024)
        print("Server Response:", response.decode("utf-8"))


if __name__ == "__main__":
    runClient()
```

