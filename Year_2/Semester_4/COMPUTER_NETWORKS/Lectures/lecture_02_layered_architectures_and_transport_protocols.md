# Lecture 02: Layered Architectures and Transport Protocols

This lecture explores protocol layering principles, comparing the OSI 7-layer reference model with the Internet TCP/IP 5-layer stack, and analyzes transport-layer mechanics including UDP, TCP connection management, sliding window flow control, and Reno congestion control.

---

## 1. Protocol Layering and Encapsulation

Modern computer networks organize complex communication functions into hierarchical protocol layers.

### 1.1 The Five-Layer Internet Protocol Stack

| Layer | Protocol Examples | Data Unit (PDU) | Primary Responsibilities |
|---|---|---|---|
| **5. Application** | HTTP, DNS, SMTP, FTP, SSH | Message | User-facing network services and distributed applications |
| **4. Transport** | TCP, UDP | Segment | Process-to-process communication, reliability, multiplexing |
| **3. Network** | IPv4, IPv6, ICMP, OSPF, BGP | Datagram / Packet | Host-to-host routing and logical addressing |
| **2. Data Link** | Ethernet (802.3), Wi-Fi (802.11) | Frame | Hop-to-hop transfer across single communication link |
| **1. Physical** | 1000BASE-T, Optical fiber, RF | Bit | Physical bit encoding, modulation, and electrical signaling |

### 1.2 Encapsulation and Decapsulation
At each sending layer, a header containing protocol control information is prepended to the data payload passed from the layer above:

```
[ Application Message ]
               |
               v
[ Transport Header | Application Message ]                  (Segment)
               |
               v
[ Network Header   | Transport Header | Message ]           (Datagram)
               |
               v
[ Link Header      | Network Header   | Segment | Link Trailer ] (Frame)
```

At the receiver, headers are stripped sequentially (**decapsulation**) and delivered upward.

---

## 2. Transport-Layer Multiplexing and Demultiplexing

The transport layer delivers data between specific application processes using **ports** (16-bit integers, range 0 to 65535):
- **Well-known ports (0–1023):** HTTP (80), HTTPS (443), SSH (22), DNS (53).
- **Registered ports (1024–49151).**
- **Dynamic/Ephemeral ports (49152–65535):** Allocated by operating system for client connections.

### 2.1 Demultiplexing Key Invariants
- **UDP Socket Identification:** Identified by a 2-tuple:
  $$(\text{Destination IP}, \text{Destination Port})$$
  All datagrams addressed to this destination port are routed to the same UDP socket regardless of source.
- **TCP Socket Identification:** Identified by a 4-tuple:
  $$(\text{Source IP}, \text{Source Port}, \text{Destination IP}, \text{Destination Port})$$
  Every active TCP client connection binds to its own dedicated socket descriptor on the server.

---

## 3. User Datagram Protocol (UDP)

UDP (RFC 768) provides a lightweight, connectionless, best-effort transport abstraction:
- **No connection state:** Zero round-trip time overhead for handshake.
- **Header size:** Minimal 8 bytes (Source Port, Destination Port, Length, Checksum).
- **No congestion control:** Transmits as fast as the application generates data.
- **Use cases:** DNS queries, real-time audio/video streaming (VoIP), online gaming.

---

## 4. Transmission Control Protocol (TCP)

TCP (RFC 793, 5681) provides a connection-oriented, full-duplex, reliable byte-stream abstraction over an unreliable network layer.

### 4.1 TCP Connection Management: Three-Way Handshake

```
Client                                                  Server
  |                                                       |
  | -------- SYN (seq = x) ---------------------------->  | Listen -> SYN-RCVD
  |                                                       |
  | <------- SYN-ACK (seq = y, ack = x + 1) -----------  |
  | ESTABLISHED                                           |
  | -------- ACK (seq = x + 1, ack = y + 1) ----------->  | ESTABLISHED
  |                                                       |
```

1. **Step 1 (SYN):** Client chooses initial sequence number $x$ and sends `SYN` segment (`SYN = 1`, `ACK = 0`).
2. **Step 2 (SYN-ACK):** Server allocates buffers, chooses initial sequence number $y$, and sends `SYN-ACK` (`SYN = 1`, `ACK = 1`, `ack = x + 1`).
3. **Step 3 (ACK):** Client acknowledges server's sequence number (`ack = y + 1`). May carry payload.

### 4.2 Connection Teardown (Four-Way Handshake)
1. Active closer sends `FIN`.
2. Passive receiver replies with `ACK` and notifies application.
3. Passive receiver finishes sending remaining data and issues its own `FIN`.
4. Active closer replies with `ACK` and enters `TIME_WAIT` state for $2 \times \text{MSL}$ (Maximum Segment Lifetime, typically 60–120s) to guarantee last ACK delivery.

---

## 5. Flow Control: Sliding Window

Flow control prevents a fast sender from overflowing a slow receiver's buffer.
- The receiver advertises its available buffer capacity in the TCP header **Receive Window** field (`rwnd`):

$$
\text{rwnd} = \text{RcvBuffer} - (\text{LastByteRcvd} - \text{LastByteRead})
$$

- The sender enforces:

$$
\text{LastByteSent} - \text{LastByteAcked} \le \text{rwnd}
$$

If `rwnd = 0`, the sender ceases transmission but periodically emits 1-byte probe segments to trigger updated window announcements.

---

## 6. TCP Congestion Control (Tahoe and Reno)

Congestion control dynamically limits transmission rate based on perceived network core congestion using the **Congestion Window** (`cwnd`):

$$
\text{Effective Window} = \min(\text{cwnd}, \text{rwnd})
$$

TCP Reno operates across three sequential operational phases:

```
cwnd (MSS)
  ^
32|                                         ssthresh = 16
  |                              /-----\    (cut in half)
16|                /-----------/       \    \
  |               /                     \----\ (Additive Increase)
 8|             /
 4|           /  Slow Start (Exponential)
 2|         /
 1|________/
  +------------------------------------------------------------> Time (RTT)
```

### 6.1 Slow Start (SS)
- Initial state: $\text{cwnd} = 1 \text{ MSS}$.
- For every received ACK: $\text{cwnd} \leftarrow \text{cwnd} + 1 \text{ MSS}$.
- Net effect: $\text{cwnd}$ doubles every RTT ($1 \to 2 \to 4 \to 8 \to \dots$).
- Transitions to Congestion Avoidance when $\text{cwnd} \ge \text{ssthresh}$.

### 6.2 Congestion Avoidance (CA)
- Additive Increase: For each full window of ACKs acknowledged (one RTT):

$$
\text{cwnd} \leftarrow \text{cwnd} + 1 \text{ MSS} \quad \left(\text{increment per ACK: } \Delta \text{cwnd} = \frac{\text{MSS}^2}{\text{cwnd}}\right)
$$

### 6.3 Loss Events and Recovery
1. **Triple Duplicate ACKs (Mild Congestion):**
   - Three duplicate ACKs arrive for the same segment (indicating out-of-order delivery, but network is still moving packets).
   - TCP Reno Fast Retransmit: Immediately retransmit the missing segment without waiting for timeout.
   - Fast Recovery:
     $$\text{ssthresh} \leftarrow \max\left(\frac{\text{cwnd}}{2}, 2\text{ MSS}\right), \quad \text{cwnd} \leftarrow \text{ssthresh} + 3\text{ MSS}$$
2. **Timeout Expiration (Severe Congestion):**
   - No feedback received; network path is blocked or buffer overflow occurred.
   - Action:
     $$\text{ssthresh} \leftarrow \max\left(\frac{\text{cwnd}}{2}, 2\text{ MSS}\right), \quad \text{cwnd} \leftarrow 1\text{ MSS}$$
   - Return to Slow Start phase.

