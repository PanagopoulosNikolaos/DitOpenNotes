# Lecture 03: Transport Layer Protocols, TCP Mechanics, and DNS/HTTP

## Context and Grounding
This lecture note explores transport protocols (TCP vs UDP), TCP state machines, sliding-window flow control, congestion avoidance, and core application-layer services (DNS and HTTP). It directly connects with `Exercises/Exercise 1+2 Packet Sniffing!.md`, `Exercise 3.md`, and `Examples/networking_exercises_part1.md`.

---

## 1. Transport Layer: TCP vs. UDP

| Metric | Transmission Control Protocol (TCP) | User Datagram Protocol (UDP) |
|---|---|---|
| **Connection Model** | Connection-oriented (3-way handshake) | Connectionless |
| **Reliability** | Guaranteed in-order delivery via ACKs and retransmission | Best-effort, unacknowledged, packets may drop/reorder |
| **Flow & Congestion Control** | Dynamic sliding window and congestion window ($cwnd$) | None |
| **Header Overhead** | 20 to 60 bytes | 8 bytes |
| **Typical Use Cases** | Web (HTTP/HTTPS), SSH, File Transfer (FTP), Databases | Real-time streaming (VoIP, video), Gaming, DNS queries |

---

## 2. TCP Connection Lifecycle

### 2.1 Three-Way Handshake (Establishment)
```text
Client                                  Server
  |                                        |  LISTEN
  | ---------- SYN (seq = x) ------------> |  SYN_RCVD
  | <------- SYN-ACK (seq = y, ack = x+1)- |  
  | ---------- ACK (seq = x+1, ack = y+1)->|  ESTABLISHED
  |                                        |
```
* **SYN**: Synchronizes initial sequence numbers (ISN).
* **SYN-ACK**: Server confirms client's sequence number and announces its own ISN.
* **ACK**: Client acknowledges server sequence number; connection is established.

### 2.2 Four-Way Handshake (Termination)
* Initiator sends `FIN` (enters `FIN_WAIT_1`).
* Receiver sends `ACK` (enters `CLOSE_WAIT`). Initiator enters `FIN_WAIT_2`.
* Receiver completes pending writes and sends its own `FIN` (enters `LAST_ACK`).
* Initiator replies with `ACK` and transitions to `TIME_WAIT` (retaining state for $2 \times \text{MSL}$ to prevent delayed segments from colliding with new connections).

---

## 3. Flow Control and Congestion Control

### 3.1 Sliding Window Flow Control
The receiver communicates its available buffer space through the **Receive Window ($rwnd$)** header field. The sender cannot transmit more unacknowledged data than $\min(cwnd, rwnd)$.

### 3.2 Congestion Control Algorithms (RFC 5681)
* **Slow Start**: $cwnd$ starts at small value (e.g., 1 to 10 MSS) and doubles every Round Trip Time (RTT), growing exponentially until reaching slow start threshold ($ssthresh$).
* **Congestion Avoidance**: Above $ssthresh$, $cwnd$ increases linearly by $1\text{ MSS}$ per RTT.
* **Loss Handling**:
  * Triple duplicate ACKs trigger **Fast Retransmit** and **Fast Recovery**.
  * Timeout drops $ssthresh \gets cwnd / 2$ and resets $cwnd \gets 1\text{ MSS}$.

---

## 4. Application Layer Protocols: DNS and HTTP

### 4.1 Domain Name System (DNS)
Operates primarily over UDP port 53 (falls back to TCP port 53 for transfers $> 512$ bytes or zone transfers).
* **Record Types**:
  * `A`: Maps hostname to 32-bit IPv4 address.
  * `AAAA`: Maps hostname to 128-bit IPv6 address.
  * `MX`: Mail Exchanger record with preference weight.
  * `PTR`: Pointer record for reverse DNS lookups (`in-addr.arpa`).
  * `CNAME`: Canonical alias pointing to another domain name.

### 4.2 Hypertext Transfer Protocol (HTTP)
* **HTTP/1.1**: Persistent TCP connections (`Connection: keep-alive`), chunked transfer encoding, pipelining.
* **HTTP Methods**: `GET` (retrieve), `POST` (submit data), `PUT` (replace), `DELETE` (remove), `HEAD` (headers only).
* **Status Codes**: $2xx$ (Success), $3xx$ (Redirection), $4xx$ (Client Error), $5xx$ (Server Error).

