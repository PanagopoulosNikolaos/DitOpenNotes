# Tutorial 02: Wireshark Packet Dissection and RTT Analysis

This tutorial introduces practical network analysis using Wireshark, focusing on packet capture filtering, dissecting the TCP three-way handshake, and analyzing empirical Round-Trip Time (RTT) and delay variance.

---

## 1. Wireshark Capture and Display Filters

Wireshark distinguishes between two filtering engines:

### 1.1 Capture Filters (libpcap syntax)
Evaluated before packet buffering; drops unwanted packets at the kernel level:
- `host 192.168.1.1`
- `tcp port 80 or tcp port 443`
- `not arp and not broadcast`

### 1.2 Display Filters (Wireshark syntax)
Applied post-capture to explore stored trace files:
- Filter by protocol: `http`, `dns`, `tcp`, `icmp`
- Filter by IP address: `ip.addr == 192.168.1.50`
- Filter TCP flags: `tcp.flags.syn == 1 and tcp.flags.ack == 0`
- Filter packet loss / retransmissions: `tcp.analysis.retransmission`

---

## 2. Dissecting the TCP Three-Way Handshake

Execute a curl request to trigger a clean HTTP connection:

```bash
curl -I http://example.com
```

In Wireshark, apply the display filter:

```text
tcp.port == 80 and ip.addr == 93.184.216.34
```

### 2.1 Handshake Sequence Analysis

```
Frame 1: Client -> Server [SYN]
  Transmission Control Protocol:
    Source Port: 54120
    Destination Port: 80
    Sequence Number: 0 (relative sequence number)
    Flags: 0x002 (SYN)
    Options: (MSS = 1460, SACK permitted, Window scale = 7)

Frame 2: Server -> Client [SYN, ACK]
  Transmission Control Protocol:
    Source Port: 80
    Destination Port: 54120
    Sequence Number: 0 (relative sequence number)
    Acknowledgment Number: 1 (relative ack number = Client ISN + 1)
    Flags: 0x012 (SYN, ACK)

Frame 3: Client -> Server [ACK]
  Transmission Control Protocol:
    Source Port: 54120
    Destination Port: 80
    Sequence Number: 1
    Acknowledgment Number: 1
    Flags: 0x010 (ACK)
```

---

## 3. Measuring Empirical Round-Trip Time (RTT)

The Round-Trip Time (RTT) is the time interval between sending a packet and receiving its corresponding acknowledgment.

### 3.1 Handshake RTT Calculation
1. Locate the timestamp of Frame 1 (`SYN`): $t_1 = 0.000000 \text{ s}$.
2. Locate the timestamp of Frame 2 (`SYN-ACK`): $t_2 = 0.042318 \text{ s}$.
3. Empirical RTT estimation:

$$
\text{RTT} = t_2 - t_1 = 42.318 \text{ ms}
$$

### 3.2 Exponential Weighted Moving Average (EWMA) of RTT
TCP maintains smoothed RTT estimates using standard RFC 6298 formulas:

$$
\text{EstimatedRTT} = (1 - \alpha) \cdot \text{EstimatedRTT} + \alpha \cdot \text{SampleRTT}
$$

$$
\text{DevRTT} = (1 - \beta) \cdot \text{DevRTT} + \beta \cdot |\text{SampleRTT} - \text{EstimatedRTT}|
$$

$$
\text{RTO} = \text{EstimatedRTT} + 4 \cdot \text{DevRTT}
$$

Where standard recommended constants are $\alpha = 0.125$ and $\beta = 0.25$.

