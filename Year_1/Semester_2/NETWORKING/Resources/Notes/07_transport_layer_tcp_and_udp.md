# Transport Layer Protocols: TCP, UDP, Flow and Congestion Control

## Overview
The Transport Layer provides logical end-to-end process-to-process communication between application processes on host systems, utilizing port numbers to multiplex and demultiplex data streams.

---

## 1. Transmission Control Protocol (TCP)

TCP (RFC 793, RFC 5681) provides connection-oriented, reliable, in-order byte stream delivery with end-to-end flow and congestion control.

### 1.1 TCP Header Format (20 Bytes Minimal)
* **Source Port** (16 bits) & **Destination Port** (16 bits)
* **Sequence Number** (32 bits): Byte offset of the first data byte in this segment.
* **Acknowledgment Number** (32 bits): Next byte expected from the peer.
* **Data Offset** (4 bits): Header length in 32-bit words (e.g. 5 = 20 bytes).
* **Control Flags** (9 bits): `URG`, `ACK`, `PSH`, `RST`, `SYN`, `FIN`, `ECE`, `CWR`, `NS`.
* **Window Size** (16 bits): Advertised receive buffer space (`rwnd`).
* **Checksum** (16 bits): Covers header, payload, and IP pseudo-header.
* **Urgent Pointer** (16 bits) & **Options** (Variable: MSS, SACK, Window Scale).

### 1.2 Handshake and Teardown Lifecycles
* **3-Way Handshake**:
  1. Client $\to$ Server: `SYN (Seq=x)`
  2. Server $\to$ Client: `SYN+ACK (Seq=y, Ack=x+1)`
  3. Client $\to$ Server: `ACK (Seq=x+1, Ack=y+1)`
* **4-Way Teardown**:
  1. Active close: `FIN (Seq=u)` $\to$ Peer enters `CLOSE-WAIT`, returns `ACK (Ack=u+1)`
  2. Passive close: `FIN (Seq=w, Ack=u+1)` $\to$ Active peer returns `ACK (Ack=w+1)` and enters `TIME-WAIT` for $2\text{MSL}$.

---

## 2. User Datagram Protocol (UDP)

UDP (RFC 768) provides lightweight, connectionless, unreliable transport with minimal protocol overhead (8-byte fixed header):
* **Source Port** (16 bits)
* **Destination Port** (16 bits)
* **Length** (16 bits): Total length of UDP header plus payload in bytes.
* **Checksum** (16 bits)

UDP does not perform handshakes, sequence tracking, retransmissions, or flow/congestion throttling, making it optimal for real-time streaming, VoIP, DNS, and NTP.

