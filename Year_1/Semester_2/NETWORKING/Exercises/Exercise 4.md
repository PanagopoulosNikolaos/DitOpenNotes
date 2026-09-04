# Lab Exercise 4: TCP Segment Analysis, Flow Control, and Congestion Mechanics

## Overview
This laboratory exercise covers practical traffic capture, segment header analysis, sequence/acknowledgment tracking, sliding window flow control, and TCP congestion avoidance algorithms using `tcpdump` and Wireshark.

---

## Part 1: TCP Three-Way Handshake Capture and Inspection

### 1.1 Capturing a Full TCP Connection
To capture the establishment, data transfer, and termination of a TCP session over an active interface (e.g., `eth0` or `wlp4s0`):

```bash
# Capture full TCP packet stream to a remote HTTP server
sudo tcpdump -i any -nn -s 0 -w tcp_session.pcap 'tcp and (port 80 or port 443)'
```

Generate traffic in a separate terminal:
```bash
curl -v http://example.com/
```

### 1.2 Handshake Dissection
A standard TCP connection begins with the three-way handshake:

```text
Client                                  Server
  |                                        |
  | -------- SYN (Seq = ISN_c) ----------> |
  |                                        |
  | <-- SYN-ACK (Seq = ISN_s, Ack = ISN_c + 1) -- |
  |                                        |
  | -------- ACK (Seq = ISN_c + 1, Ack = ISN_s + 1) --> |
  |                                        |
```

1. **Packet 1 (SYN)**:
   * Flags: `[SYN]`
   * Sequence Number: Relative `0` (Random 32-bit Initial Sequence Number, e.g. `ISN_c = 2849102910`).
   * Options: Maximum Segment Size (MSS = 1460 bytes), Window Scale factor (WS = 7), SACK permitted.
2. **Packet 2 (SYN-ACK)**:
   * Flags: `[SYN, ACK]`
   * Sequence Number: `ISN_s = 1049281720`.
   * Acknowledgment Number: `ISN_c + 1` (Confirms reception of the SYN flag, which consumes 1 sequence number).
3. **Packet 3 (ACK)**:
   * Flags: `[ACK]`
   * Sequence Number: `ISN_c + 1`.
   * Acknowledgment Number: `ISN_s + 1`.

---

## Part 2: Sequence and Acknowledgment Number Tracking

### 2.1 Forward Acknowledgment Rule
The Acknowledgment number indicates the **next expected byte** of contiguous data from the sender:
$$\text{Next Expected Ack} = \text{Current Seq} + \text{Payload Length (Bytes)}$$

* Note: TCP control flags `SYN` and `FIN` each consume 1 sequence number. Pure `ACK` packets carrying 0 bytes of payload do not advance the sequence number.

### 2.2 Trace Analysis Example
Consider a client sending a 500-byte HTTP POST request:

| Packet | Sender | Flags | Seq | Ack | Payload (Bytes) | Description |
|:---|:---|:---|:---:|:---:|:---:|:---|
| 1 | Client | SYN | 0 | 0 | 0 | Client initiates connection |
| 2 | Server | SYN, ACK | 0 | 1 | 0 | Server responds with SYN-ACK |
| 3 | Client | ACK | 1 | 1 | 0 | Client completes handshake |
| 4 | Client | PSH, ACK | 1 | 1 | 500 | Client transmits HTTP request |
| 5 | Server | ACK | 1 | 501 | 0 | Server acknowledges all 500 bytes |
| 6 | Server | PSH, ACK | 1 | 501 | 1200 | Server sends response chunk |
| 7 | Client | ACK | 501 | 1201 | 0 | Client acknowledges 1200 bytes |

---

## Part 3: Sliding Window Flow Control

### 3.1 Receiver Window (rwnd)
Flow control protects the receiver from being overwhelmed by a faster sender.
* The receiver advertises its available buffer space in the 16-bit **Window Size** header field:
$$\text{Effective Window} = \text{Window Field} \times 2^{\text{Window Scale Factor}}$$
* The sender must never allow the number of unacknowledged in-flight bytes to exceed `rwnd`:
$$\text{LastByteSent} - \text{LastByteAcked} \le \text{rwnd}$$

### 3.2 Zero-Window and Persistence Timer
When the receiver's application buffer is completely full:
1. The receiver emits a packet with `Window = 0` (Zero Window Notification).
2. The sender immediately suspends transmission.
3. To prevent deadlocks, the sender initiates a **persist timer**. Upon expiry, the sender transmits a 1-byte **Zero Window Probe (ZWP)** packet.
4. The receiver responds with an ACK stating its updated window size.

---

## Part 4: TCP Congestion Control Algorithms

TCP utilizes four intertwined congestion control algorithms defined in RFC 5681:

```text
              Slow Start
                  |
    (cwnd reaches ssthresh or packet loss occurs)
                  |
                  v
         Congestion Avoidance
                  |
    (3 Duplicate ACKs received)
                  |
                  v
       Fast Retransmit / Fast Recovery
```

### 4.1 Slow Start
* Initial state: $\text{cwnd} = 1 \text{ SMSS}$ (or $10 \text{ SMSS}$ in modern kernels).
* For each received ACK that acknowledges new data:
$$\text{cwnd} \leftarrow \text{cwnd} + 1 \text{ SMSS}$$
* The congestion window doubles every Round Trip Time (RTT), demonstrating exponential growth until $\text{cwnd} \ge \text{ssthresh}$.

### 4.2 Congestion Avoidance
* Once $\text{cwnd} \ge \text{ssthresh}$, the growth changes from exponential to linear:
$$\text{cwnd} \leftarrow \text{cwnd} + \frac{1}{\text{cwnd}} \text{ SMSS per ACK}$$
* Over one full RTT, $\text{cwnd}$ increases by exactly $1 \text{ SMSS}$ (Additive Increase).

### 4.3 Fast Retransmit and Fast Recovery
* When an isolated packet is dropped in transit, subsequent packets arrive out-of-order at the receiver.
* The receiver generates an immediate duplicate ACK specifying the last in-sequence byte expected.
* Upon receiving **3 duplicate ACKs** (4 identical ACKs total):
  1. **Fast Retransmit**: Sender immediately retransmits the missing segment without waiting for the retransmission timeout (RTO).
  2. **Multiplicative Decrease**:
     $$\text{ssthresh} \leftarrow \max\left(\frac{\text{FlightSize}}{2}, 2 \text{ SMSS}\right)$$
     $$\text{cwnd} \leftarrow \text{ssthresh} + 3 \text{ SMSS}$$
  3. **Fast Recovery**: The connection continues in congestion avoidance without dropping down to $\text{cwnd} = 1$.

---

## Part 5: TCP Teardown (Connection Termination)

### 5.1 Four-Way Handshake
Graceful connection teardown occurs when both endpoints close their respective half-connections:

```text
Client                                  Server
  |                                        |
  | -------- FIN (Seq = u) --------------> |  (Client enters FIN-WAIT-1)
  |                                        |
  | <-- ACK (Seq = v, Ack = u + 1) ------- |  (Client enters FIN-WAIT-2)
  |                                        |
  | <-- FIN (Seq = w, Ack = u + 1) ------- |  (Server enters LAST-ACK)
  |                                        |
  | -------- ACK (Seq = u + 1, Ack = w + 1) -> | (Client enters TIME-WAIT)
  |                                        |
```

### 5.2 The TIME-WAIT State
The initiating peer remains in the `TIME-WAIT` state for $2 \times \text{MSL}$ (Maximum Segment Lifetime, typically 60 to 120 seconds):
1. **Ensure Final ACK Delivery**: If the client's final ACK is lost, the server retransmits the FIN. Being in `TIME-WAIT` enables the client to resend the ACK.
2. **Drain Delayed Packets**: Prevents old duplicate segments from an earlier session from being misinterpreted by a newly opened incarnation of the same socket pair `(IP_src, Port_src, IP_dst, Port_dst)`.

---

## Verification and Laboratory Checklist

1. Execute `tcpdump -i any -nn -tt 'tcp[tcpflags] & (tcp-syn|tcp-fin) != 0'` and observe active connection handshakes and terminations on your system.
2. In Wireshark, open your capture file and inspect the TCP header:
   * Locate the Source Port, Destination Port, Sequence Number, and Acknowledgment Number.
   * View the TCP Stream Graph via **Statistics -> TCP Stream Graph -> Time Sequence (Stevens)**.
   * Verify the linear ramp-up of Sequence Numbers during bulk data transfer.