# Practice Exam 01: Computer Networks (Course 403)

This comprehensive practice examination covers physical transmission delays, CIDR routing and subnet allocation, TCP state machines and flow control, and Layer 2 switch forwarding operations.

**Duration:** 2 Hours  
**Total Points:** 100 Points  

---

## Part A: Mathematical Modeling and Physical Delay (25 Points)

### Question 1 (15 Points)
A source host transmits a file of size $F = 2 \text{ Megabytes}$ ($2 \times 10^6 \text{ bytes}$) to a destination host over a single direct link. The link has a transmission rate of $R = 100 \text{ Mbps}$ ($10^8 \text{ bps}$), length $d = 4,000 \text{ km}$, and propagation speed $s = 2 \times 10^8 \text{ m/s}$. The file is divided into packets of maximum transmission size $L = 1,000 \text{ bytes}$ each.

1. Calculate the transmission delay $d_{\text{trans}}$ of one individual packet.
2. Calculate the propagation delay $d_{\text{prop}}$ of the link.
3. Calculate the total elapsed time until the destination receives the final bit of the file. (Assume zero processing and queuing delays, and continuous back-to-back packet transmission).

### Question 2 (10 Points)
Define the Bandwidth-Delay Product (BDP) mathematically. What is the physical significance of BDP for TCP window sizing? If a link has $R = 1 \text{ Gbps}$ and one-way propagation delay $d_{\text{prop}} = 25 \text{ ms}$, compute the BDP in Megabytes.

---

## Part B: Subnetting and Routing Protocols (25 Points)

### Question 3 (15 Points)
An ISP assigns the prefix `198.51.100.0/24` to a regional enterprise. The network engineer must carve out four distinct subnets:
- Subnet 1: 58 hosts
- Subnet 2: 26 hosts
- Subnet 3: 10 hosts
- Subnet 4: 2 hosts (router link)

Using Variable-Length Subnet Masking (VLSM), determine for each subnet:
1. The subnet mask in CIDR notation (e.g., `/26`).
2. The network address.
3. The valid host address range.
4. The broadcast address.

### Question 4 (10 Points)
Explain the difference between Link-State (OSPF) and Distance-Vector (RIP) routing algorithms. Describe the **Count-to-Infinity** problem in Distance-Vector routing and specify two techniques used to resolve it.

---

## Part C: Transport Layer Mechanics (25 Points)

### Question 5 (15 Points)
Describe the TCP three-way handshake used to establish a reliable connection between Client and Server.
1. Draw the sequence diagram showing packet transmissions with TCP flags (`SYN`, `ACK`), sequence numbers, and acknowledgment numbers.
2. Explain why a two-way handshake is insufficient for reliable full-duplex connection establishment.

### Question 6 (10 Points)
A TCP Reno sender experiences a loss event when its congestion window is $\text{cwnd} = 32 \text{ MSS}$ and $\text{ssthresh} = 16 \text{ MSS}$.
1. If the loss event is triggered by **3 duplicate ACKs**, state the new values of $\text{ssthresh}$ and $\text{cwnd}$, and name the recovery phase entered.
2. If the loss event is triggered by a **Retransmission Timeout (RTO)**, state the new values of $\text{ssthresh}$ and $\text{cwnd}$, and name the recovery phase entered.

---

## Part D: Data Link Layer and Ethernet Switching (25 Points)

### Question 7 (15 Points)
Consider an Ethernet switch with 4 ports currently empty of forwarding table entries. Hosts $H_1, H_2, H_3, H_4$ are connected to ports 1, 2, 3, and 4 respectively.
The following sequence of frames arrives:
1. $H_1$ transmits frame to $H_2$.
2. $H_2$ transmits frame to $H_1$.
3. $H_3$ transmits frame to $H_2$.
4. $H_4$ transmits frame to $H_1$.

For each step:
- State the switch table updates (MAC address, Port).
- State whether the frame is dropped, forwarded (unicast), or flooded, specifying the outgoing ports.

### Question 8 (10 Points)
What is the purpose of the IEEE 802.1Q tag in Virtual Local Area Networks (VLANs)? Explain the difference between an **Access Port** and a **Trunk Port**.

---

## Complete Solution and Grading Guide

### Solution to Part A

#### Question 1
1. **Packet Transmission Delay:**
   $$L = 1,000 \text{ bytes} \times 8 = 8,000 \text{ bits}$$
   $$d_{\text{trans}} = \frac{L}{R} = \frac{8,000 \text{ bits}}{10^8 \text{ bps}} = 8 \times 10^{-5} \text{ s} = 80 \ \mu\text{s}$$
   *(4 Points)*
2. **Link Propagation Delay:**
   $$d = 4 \times 10^6 \text{ m}, \quad s = 2 \times 10^8 \text{ m/s}$$
   $$d_{\text{prop}} = \frac{d}{s} = \frac{4 \times 10^6}{2 \times 10^8} = 0.02 \text{ s} = 20 \text{ ms}$$
   *(4 Points)*
3. **Total Transfer Time:**
   $$N_{\text{packets}} = \frac{2 \times 10^6 \text{ bytes}}{1,000 \text{ bytes/packet}} = 2,000 \text{ packets}$$
   Total time to transmit all 2,000 packets:
   $$T_{\text{all\_trans}} = \frac{F \times 8}{R} = \frac{16 \times 10^6 \text{ bits}}{10^8 \text{ bps}} = 0.16 \text{ s} = 160 \text{ ms}$$
   The last bit of the final packet leaves the sender at $t = 160 \text{ ms}$ and propagates across the link for $d_{\text{prop}} = 20 \text{ ms}$.
   $$T_{\text{total}} = T_{\text{all\_trans}} + d_{\text{prop}} = 160 \text{ ms} + 20 \text{ ms} = 180 \text{ ms} = 0.180 \text{ s}$$
   *(7 Points)*

#### Question 2
- **Definition:** $\text{BDP} = R \times d_{\text{prop}}$. It represents the maximum volume of bits that can fill the transmission pipe at any instant.
- **TCP Significance:** If the TCP sender window size $\text{W} < \text{BDP}$, the sender runs out of authorization to send data before receiving the first ACK, causing the sender to idle and leaving link capacity underutilized.
- **Calculation:**
  $$\text{BDP} = 10^9 \text{ bps} \times 0.025 \text{ s} = 25 \times 10^6 \text{ bits} = 3.125 \text{ Megabytes}$$
  *(10 Points)*

---

### Solution to Part B

#### Question 3
- **Subnet 1 (58 hosts):** Need $2^h - 2 \ge 58 \implies h = 6 \implies /26$.
  - Network: `198.51.100.0/26`
  - Range: `198.51.100.1` – `198.51.100.62`
  - Broadcast: `198.51.100.63`
- **Subnet 2 (26 hosts):** Need $2^h - 2 \ge 26 \implies h = 5 \implies /27$.
  - Network: `198.51.100.64/27`
  - Range: `198.51.100.65` – `198.51.100.94`
  - Broadcast: `198.51.100.95`
- **Subnet 3 (10 hosts):** Need $2^h - 2 \ge 10 \implies h = 4 \implies /28$.
  - Network: `198.51.100.96/28`
  - Range: `198.51.100.97` – `198.51.100.110`
  - Broadcast: `198.51.100.111`
- **Subnet 4 (2 hosts):** Need $2^h - 2 \ge 2 \implies h = 2 \implies /30$.
  - Network: `198.51.100.112/30`
  - Range: `198.51.100.113` – `198.51.100.114`
  - Broadcast: `198.51.100.115`
*(15 Points: 4+4+4+3)*

#### Question 4
- **Difference:** Link-State floods link advertisements globally so each node independently builds the full graph and computes Dijkstra's algorithm. Distance-Vector shares local estimates only with physical neighbors iteratively using the Bellman-Ford equation.
- **Count-to-Infinity:** When a link fails, adjacent routers continuously increment costs to each other believing an alternate path exists through the other router, converging very slowly.
- **Solutions:** Split Horizon, Poison Reverse, and maximum hop limit (e.g., 16 in RIP).
*(10 Points)*

---

### Solution to Part C

#### Question 5
1. **Diagram:**
   - Message 1: Client $\to$ Server: `SYN = 1`, `seq = x`
   - Message 2: Server $\to$ Client: `SYN = 1`, `ACK = 1`, `seq = y`, `ack = x + 1`
   - Message 3: Client $\to$ Server: `ACK = 1`, `seq = x + 1`, `ack = y + 1`
2. **Why 2-way is insufficient:** In a 2-way handshake, the server cannot confirm that the client actually received its `SYN-ACK`, and duplicate delayed `SYN` segments from previous crashed connections could trick the server into opening invalid half-open connections.
*(15 Points)*

#### Question 6
1. **3 Duplicate ACKs (Fast Recovery):**
   - $\text{ssthresh} = \frac{\text{cwnd}}{2} = \frac{32}{2} = 16 \text{ MSS}$.
   - $\text{cwnd} = \text{ssthresh} + 3 = 19 \text{ MSS}$.
   - Phase entered: **Fast Recovery**.
2. **Timeout (RTO):**
   - $\text{ssthresh} = \frac{\text{cwnd}}{2} = 16 \text{ MSS}$.
   - $\text{cwnd} = 1 \text{ MSS}$.
   - Phase entered: **Slow Start**.
*(10 Points: 5+5)*

---

### Solution to Part D

#### Question 7
1. Frame 1 ($H_1 \to H_2$): Switch learns $(H_1, \text{Port 1})$. Destination $H_2$ is unknown. Action: **Flood** out Ports 2, 3, 4.
2. Frame 2 ($H_2 \to H_1$): Switch learns $(H_2, \text{Port 2})$. Destination $H_1$ is in table (Port 1). Action: **Forward (unicast)** out Port 1 only.
3. Frame 3 ($H_3 \to H_2$): Switch learns $(H_3, \text{Port 3})$. Destination $H_2$ is in table (Port 2). Action: **Forward (unicast)** out Port 2 only.
4. Frame 4 ($H_4 \to H_1$): Switch learns $(H_4, \text{Port 4})$. Destination $H_1$ is in table (Port 1). Action: **Forward (unicast)** out Port 1 only.
*(15 Points)*

#### Question 8
- **IEEE 802.1Q Tag:** A 4-byte header inserted into Ethernet frames crossing trunk links containing a 12-bit VLAN Identifier (VID) to preserve broadcast domain segmentation across switches.
- **Access vs Trunk:** An access port connects to a single host and carries untagged frames belonging to exactly one VLAN. A trunk port interconnects switches or switches to routers and carries frames tagged with 802.1Q for multiple VLANs simultaneously.
*(10 Points)*

