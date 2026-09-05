# Computer Networks: Socket Programming Walkthrough

This guide accompanies [`examples_socket_programming_tcp_udp.py`](examples_socket_programming_tcp_udp.py) to illustrate the fundamental principles of transport layer communication in Python.

---

## 1. Architectural Overview

Network applications interact with operating system protocol stacks via the **Berkeley Sockets API**. The transport layer provides two distinct end-to-end communication abstractions:

```text
Application Layer
       │
┌──────┴───────────────┐
│  Socket Abstraction  │
└──────┬───────────────┘
       │
┌──────┴──────┬────────┴──────┐
│  TCP Stream │  UDP Datagram │
│ (SOCK_STREAM)│  (SOCK_DGRAM) │
└─────────────┴───────────────┘
       │
Network Layer (IP)
```

1. **Transmission Control Protocol (TCP - `SOCK_STREAM`)**:
   - Connection-oriented: Requires a 3-way handshake (`SYN` -> `SYN-ACK` -> `ACK`) before data transmission.
   - Reliable byte-stream: Guarantees delivery via sequence numbers, cumulative acknowledgments, and retransmissions.
   - Flow & Congestion Control: Regulates transmission rate dynamically to protect network buffers and receiver capacity.

2. **User Datagram Protocol (UDP - `SOCK_DGRAM`)**:
   - Connectionless: Sends self-contained messages (datagrams) with zero session setup latency.
   - Unreliable: Packets may arrive out-of-order, duplicated, or get dropped without error indication.
   - Lightweight: Minimal 8-byte header overhead compared to TCP's 20-byte base header.

---

## 2. Executing the Demonstrations

Run the complete test client-server suite directly via command-line:

```bash
python3 Examples/examples_socket_programming_tcp_udp.py
```

### Expected Output Summary

```text
=== TCP Client-Server Demonstration ===
[TCP Server] Listening on 127.0.0.1:9001
[TCP Server] Connection accepted from ('127.0.0.1', ...)
[TCP Client] Received echo: "Network Protocol Test: TCP Echo"
[TCP Server] Client disconnected

=== UDP Client-Server Demonstration ===
[UDP Server] Bound and listening on 127.0.0.1:9002
[UDP Server] Datagram received from ('127.0.0.1', ...): "Network Protocol Test: UDP Datagram"
[UDP Client] Received echo: "ECHO: Network Protocol Test: UDP Datagram"
```

---

## 3. Core Implementation Details

### Socket Lifecycle in TCP
1. **Server Setup**:
   ```python
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
   sock.bind((host, port))
   sock.listen(5)
   client_sock, client_addr = sock.accept()
   ```
2. **Client Setup**:
   ```python
   client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   client_sock.connect((host, port))
   client_sock.sendall(data)
   ```

### Socket Lifecycle in UDP
1. **Server**: `sock.bind((host, port))` followed by `data, addr = sock.recvfrom(buffer_size)`.
2. **Client**: `sock.sendto(data, (host, port))` without establishing a prior connection.

