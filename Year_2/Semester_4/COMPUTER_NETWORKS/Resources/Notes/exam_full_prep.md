# Comprehensive Study Guide - Computer Networks (10/10 Exam Guide)

---

## SECTION 1: Fundamental Concepts, Architecture & Encapsulation

### 1.1 Definition & Basic Network Characteristics
- **Computer Network:** A collection of hardware components and computers, interconnected by communication channels, with the primary purpose of resource (hardware/software) and information sharing.
- **Data Transmission Modes:**
  1. **Simplex:** Communication occurs in only one direction (e.g. broadcast TV, radio).
  2. **Half-Duplex:** Communication occurs in both directions, but **not simultaneously** (e.g. Walkie-Talkie).
  3. **Full-Duplex:** Communication occurs in both directions **simultaneously** (e.g. telephone call).
  *Note:* **Multiplexing** is not a data exchange mode, but a technique for combining multiple signals over a single physical medium (e.g. FDM, TDM).

### 1.2 OSI Model, Layers & Network Devices
- **Physical Layer (Layer 1):** 
  - **Repeater:** Operates **exclusively at Layer 1**. Regenerates and amplifies electrical/optical signals (bits) to cover longer distances, without examining or understanding headers (MAC/IP).
  - **Hub:** Operates at Layer 1 as a multi-port repeater (Shared Medium).
- **Data Link Layer (Layer 2):**
  - **Bridge & Switch:** Connect LAN segments, read MAC addresses, filter traffic, and isolate collision domains. PDU: **Frame**.
- **Network Layer (Layer 3):**
  - **Router:** Routes packets between different subnets based on IP addresses. PDU: **Datagram / Packet**.
- **Transport Layer (Layer 4):**
  - Manages end-to-end communication (TCP/UDP), ports, flow control, and congestion control. PDU: **Segment**.
- **Peer Processes:** Processes/protocols executing at the **same layer** on two different communicating machines.

### 1.3 Data Encapsulation & Address Behavior
- **Encapsulation Process:** When sending, data travels down the TCP/IP stack. Each layer appends its own header:
  $$\text{Message (App)} \rightarrow \text{Segment (Transport)} \rightarrow \text{Packet (Network)} \rightarrow \text{Frame (Data Link)} \rightarrow \text{Bits (Physical)}$$
- **Address Changes Across Routers:**
  - **IP Address (Layer 3):** Remains **constant** from source to final destination (Host A IP -> Host B IP), unless a NAT device intervenes.
  - **MAC Address (Layer 2):** **Changes at every hop (router)**. Each router strips the Layer 2 header, examines the IP, determines the egress interface, and builds a new Layer 2 header with Source MAC set to its own egress interface and Destination MAC set to the next-hop MAC.

### 1.4 Control Plane vs Data Plane
- **Control Plane:** The "intelligence" of the router. Executed in Software, computes routes using routing algorithms (OSPF, BGP, RIP), and builds the Routing Information Base (RIB).
- **Data Plane / Forwarding Plane:** The "speed" of the router. Executed in Hardware/ASICs. Forwards packets from input port to output port in nanoseconds, based on the Forwarding Information Base (FIB).

### 1.5 Packet Switching vs Circuit Switching
- **Circuit Switching:**
  - Requires advance reservation of dedicated resources (bandwidth/circuits) along the entire path before transfer.
  - Multiplexing techniques: **FDM** (Frequency Division Multiplexing) & **TDM** (Time Division Multiplexing).
  - Advantage: Guaranteed performance, zero queuing delay ($d_{\text{queue}} = 0$).
  - Disadvantage: Wasted resources during idle periods.
- **Packet Switching:**
  - Data is broken into packets. Resources are allocated dynamically (**Statistical Multiplexing**).
  - **Store-and-Forward** operation: The router must receive the entire packet before initiating its transmission on the output link.
  - Allows many more users to share the network, but queuing delays and packet loss may occur due to congestion.

### 1.6 Collision Domains & Broadcast Domains
- **Collision Domain:** A network region where if two devices transmit simultaneously, signals collide.
  - **Bus Topology / Hub:** All nodes belong to the **same** collision domain.
  - **Switch:** **Each physical port defines a separate collision domain** (Micro-segmentation).
- **Broadcast Domain:** A network region reached by a broadcast frame (MAC: `FF-FF-FF-FF-FF-FF`).
  - Switches **preserve** the broadcast domain (all ports belong to the same broadcast domain, unless VLANs exist).
  - **Each physical port (interface) of a Router defines a separate broadcast domain.**

---

## SECTION 2: Delay Calculations, Nodal Delay, RTT, Pipelining & Capacity

### 2.1 Nodal Delay & Components
The total delay experienced by a packet at an individual node/router is called **Nodal Delay ($d_{\text{nodal}}$)**:
$$d_{\text{nodal}} = d_{\text{proc}} + d_{\text{queue}} + d_{\text{trans}} + d_{\text{prop}}$$

**Detailed explanation of components:**
1. **$d_{\text{proc}}$ (Processing Delay):** Time to check headers, bit errors (checksum), and determine the output port.
2. **$d_{\text{queue}}$ (Queuing Delay):** Waiting time in the buffer queue. Depends on traffic intensity ($\text{Traffic Intensity} = \frac{L \cdot a}{R}$). If $\frac{L \cdot a}{R} > 1$, the queue grows infinitely causing packet loss.
3. **$d_{\text{trans}}$ (Transmission Delay):** Time to push all packet bits into the medium:
   $$d_{\text{trans}} = \frac{L}{R}$$
   ($L$: Packet size in bits, $R$: Transmission rate / Bandwidth in bps).
4. **$d_{\text{prop}}$ (Propagation Delay):** Time for a bit to travel from the start to the end of the physical medium:
   $$d_{\text{prop}} = \frac{l}{u}$$
   ($l$: Distance in meters, $u$: Propagation speed in medium, typically $2 \times 10^8 \text{ m/s}$ to $3 \times 10^8 \text{ m/s}$).

---

### 2.2 Total End-to-End Delay & Hop Count $N$

> [!IMPORTANT]
> **Hop Count Rule ($N$):** $N$ represents the number of **links / hops** (intervals between nodes) and **NOT the number of routers**.
> - If there are 4 routers in series ($R_1 \rightarrow R_2 \rightarrow R_3 \rightarrow R_4$), there are 3 links between them, so **$N = 3$ hops**.
> - If there are 2 host computers ($A, B$) and 2 intermediate routers ($A \rightarrow R_1 \rightarrow R_2 \rightarrow B$), there are **$N = 3$ hops** and 2 intermediate routers.

#### Case A: Identical / Symmetric Links
When all $N$ links have identical characteristics ($R, l, u, d_{\text{proc}}, d_{\text{queue}}$):
$$d_{\text{end-to-end}} = N \cdot d_{\text{nodal}} = N \cdot (d_{\text{proc}} + d_{\text{queue}} + d_{\text{trans}} + d_{\text{prop}})$$

*(If end hosts introduce no processing delay and there are $N-1$ intermediate routers with $d_{\text{proc}}$):*
$$d_{\text{end-to-end}} = N \cdot d_{\text{trans}} + N \cdot d_{\text{prop}} + N \cdot d_{\text{queue}} + (N-1) \cdot d_{\text{proc}}$$

#### Case B: Asymmetric Links (General Case)
When links differ in physical medium, bandwidth, or delays:
$$d_{\text{end-to-end}} = \sum_{i=1}^{N} (d_{\text{proc},i} + d_{\text{queue},i} + d_{\text{trans},i} + d_{\text{prop},i})$$

---

### 2.3 Store-and-Forward & Multi-Packet Pipelining Effect
When a file is split into **$P$ packets** and transmitted over **$N$ hops**:
- The 1st packet reaches the destination in time: $t_{1\text{st}} = N \cdot d_{\text{trans}} + N \cdot d_{\text{prop}}$.
- Due to parallel transmission across consecutive links (**Pipelining**), each of the remaining $(P-1)$ packets arrives at the destination with delay $d_{\text{trans}}$ after the previous one.
- **Total Transfer Time ($d_{\text{total}}$):**
  $$d_{\text{total}} = (N + P - 1) \cdot d_{\text{trans}} + N \cdot d_{\text{prop}}$$

---

### 2.4 Bandwidth-Delay Product (BDP)
Expresses the **maximum number of bits** that can be present inside the wire (bits in flight / one-way link capacity) at any given moment:
$$\text{BDP (Max Bits)} = \text{Bandwidth (R)} \times d_{\text{prop}}$$

#### Typical Exam Problem Format (based on Student ID AM):
> *Given Bandwidth = $N \text{ KB/s}$ (where $N = \text{AM}$) and Delay = $d \text{ ms}$ (where $d = \text{last digit of AM}$, if $d=0 \Rightarrow Delay = 5\text{ ms}$ or $6\text{ ms}$).*

**Calculation Methodology:**
- $R = N \times 1000 \times 8 \text{ bps} = 8000 \cdot N \text{ bps}$ *(or $N \times 1024 \times 8 \text{ bps}$ if binary defined)*.
- $D = d \times 10^{-3} \text{ sec}$.
- $\text{Max Bits} = (8000 \cdot N) \times (d \cdot 10^{-3}) = 8 \cdot N \cdot d \text{ bits}$.

---

### 2.5 Sliding Window Throughput
To achieve **maximum throughput (100% utilisation)** of the link without the sender staying idle awaiting ACKs, window size $W$ must cover all bits transmitted during one RTT:
$$W \ge \text{Bandwidth (R)} \times \text{RTT}$$

---

### 2.6 RTT (Round Trip Time) & Multi-Node Path Calculations

#### Scenario A: Link A-B (1 Hop)
$$\text{RTT}_{A-B} = 2 \times d_{\text{trans1}} + 2 \times d_{\text{prop1}} = 2 \left( \frac{L}{R_1} \right) + 2 \left( \frac{l_1}{u_1} \right)$$

#### Scenario B: Path A - B - C (2 Hops, 3 Processing Delays)
Path includes outbound and return journey: $A \xrightarrow{\text{proc B}} B \xrightarrow{\text{proc C}} C \xrightarrow{\text{proc B}} B \rightarrow A$.
$$\text{RTT}_{A-C} = 2 \cdot (d_{\text{trans1}} + d_{\text{prop1}} + d_{\text{trans2}} + d_{\text{prop2}}) + 3 \cdot d_{\text{proc}}$$

---

## SECTION 3: Subnetting, CIDR & Longest Prefix Match (LPM)

### 3.1 IPv4 Addressing, Subnet Mask & CIDR
- **Subnet Mask:** Splits an IP address into Network ID and Host ID.
- **CIDR Notation (`/prefix`):** Indicates the number of '1' bits in the mask.
  - `/24` $\Rightarrow 255.255.255.0$ (256 IPs, 254 usable).
  - `/26` $\Rightarrow 255.255.255.192$ (Block size: 64, 62 usable IPs per subnet).
  - `/29` $\Rightarrow 255.255.255.248$ (Block size: 8, 6 usable IPs).
  - `/30` $\Rightarrow 255.255.255.252$ (Block size: 4, 2 usable IPs — typical for Point-to-Point links).
- **Network Address:** All host bits are '0'.
- **Broadcast Address:** All host bits are '1'.

---

### 3.2 Longest Prefix Match (LPM) Rule
When a router receives a packet, it compares the destination IP against all entries in the Forwarding Table.
**LPM Rule:** Select the entry matching the **longest prefix length (most bits in prefix / most specific subnet)**.

#### Exam Example:
Router Forwarding Table:
1. `10.15.0.0/16` $\rightarrow$ Interface `Eth0`
2. `10.15.20.0/24` $\rightarrow$ Interface `Eth1`
3. `10.15.20.128/25` $\rightarrow$ Interface `Eth2`
4. `0.0.0.0/0` (Default Route) $\rightarrow$ Interface `Eth3`

**Forwarding Decisions:**
- IP `10.15.20.200`: Matches `/16`, `/24`, and `/25`. By LPM `/25` selected $\Rightarrow$ **Interface Eth2**.
- IP `10.15.20.50`: Matches `/16` and `/24`. By LPM `/24` selected $\Rightarrow$ **Interface Eth1**.
- IP `10.15.21.5`: Matches only `/16` $\Rightarrow$ **Interface Eth0**.
- IP `10.16.5.1`: Matches no specific prefix $\Rightarrow$ **Interface Eth3** (Default).

---

## SECTION 4: Data Link Layer & Error Detection/Correction

### 4.1 Access Protocols: CSMA/CD vs CSMA/CA
- **CSMA/CD (Collision Detection - Wired Ethernet IEEE 802.3):**
  - Nodes listen before transmitting (Carrier Sense) and during transmission (Collision Detection).
  - If a collision is detected, transmission stops immediately, a Jam signal is transmitted, and Exponential Backoff is applied.
  - **Minimum Frame Size ($L_{\text{min}}$):** For sender to detect collision before transmission completes, $t_{\text{trans}} \ge 2 \cdot t_{\text{prop}}$:
    $$L_{\text{min}} \ge 2 \cdot t_{\text{prop}} \cdot R$$
- **CSMA/CA (Collision Avoidance - Wireless Wi-Fi IEEE 802.11):**
  - In wireless medium **collision detection is impossible** (half-duplex transceiver nature, Hidden Terminal problem).
  - Uses **Collision Avoidance** with random backoff timer and optional **RTS / CTS (Request to Send / Clear to Send)** control exchange.

---

### 4.2 Error Detection & Correction

#### A. Parity Bits
Used **exclusively for 1-bit Error Detection**.

#### B. Internet Checksum
Used in IP, UDP, TCP protocols. Data is split into 16-bit words, added using 1's complement addition, and the result is inverted (complemented).

#### C. Hamming Code
Enables **Single Error Correction (1-bit error detection and correction)**.

**Calculation Methodology (e.g. for message $D = 10001011$, 8 bits):**
1. **Calculate Parity Bits ($p$):** $2^p \ge d + p + 1$. For $d = 8 \Rightarrow p = 4$ bits ($2^4 = 16 \ge 13$).
2. **Bit Positioning:** $P_i$ are placed at powers-of-2 positions (1, 2, 4, 8) and data bits in remaining positions.

   | Position | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
   |---|---|---|---|---|---|---|---|---|---|---|---|---|
   | Bit | **$P_1$** | **$P_2$** | $D_1$ | **$P_4$** | $D_2$ | $D_3$ | $D_4$ | **$P_8$** | $D_5$ | $D_6$ | $D_7$ | $D_8$ |
   | Value | ? | ? | 1 | ? | 0 | 0 | 0 | ? | 1 | 0 | 1 | 1 |

3. **Calculate $P_i$ (e.g. with Odd Parity):**
   - $P_1$ (positions 1, 3, 5, 7, 9, 11) $\rightarrow$ values $P_1, 1, 0, 0, 1, 1$ (3 ones). For odd parity $\Rightarrow P_1 = 0$.
   - $P_2$ (positions 2, 3, 6, 7, 10, 11) $\rightarrow$ values $P_2, 1, 0, 0, 0, 1$ (2 ones). For odd parity $\Rightarrow P_2 = 1$.
   - $P_4$ (positions 4, 5, 6, 7, 12) $\rightarrow$ values $P_4, 0, 0, 0, 1$ (1 one). For odd parity $\Rightarrow P_4 = 0$.
   - $P_8$ (positions 8, 9, 10, 11, 12) $\rightarrow$ values $P_8, 1, 0, 1, 1$ (3 ones). For odd parity $\Rightarrow P_8 = 0$.
   - **Final Transmitted Message:** `011000001011`

#### D. Cyclic Redundancy Check (CRC)
Powerful hardware error detection technique using polynomial division with **modulo-2 arithmetic (XOR)**.
- Given original message $D$ (length $d$ bits) and generator $G$ (length $r+1$ bits).
- Append $r$ zeros to the end of $D$ ($D \cdot 2^r$).
- Perform modulo-2 division of $D \cdot 2^r$ by $G$. Remainder $R$ (length $r$ bits) is appended to $D$.
- Transmitted sequence: $D \cdot 2^r \oplus R$.

---

## SECTION 5: ARP Protocol & Diagnostic Tools

### 5.1 Address Resolution Protocol (ARP)
Maps IP addresses (Layer 3) to MAC addresses (Layer 2) within the **same local area network (LAN)**.

- **ARP Request:** 
  - **Transmission Type:** **Broadcast** to all on LAN (`FF-FF-FF-FF-FF-FF`).
  - **Target MAC:** `00:00:00:00:00:00` (Unknown).
- **ARP Reply:** 
  - **Transmission Type:** **Unicast** directly to requester.
  - **Sender MAC:** Real MAC address of responding device.
- **ARP Cache:** 
  - Caches IP-MAC mappings locally for a given duration (15-20 minutes). If a new packet is sent within the window, **no new ARP request is sent**.
- **External LAN Communication (Default Gateway):**
  - If destination IP is outside local network, sender sends **ARP Request for Default Gateway / Router Interface MAC**.

---

### 5.2 Traceroute / Tracert & TTL Mechanism
- **Purpose:** Records intermediate routers (hops) along path to destination.
- **Operating Mechanism:**
  1. Sends series of IP packets starting with **$\text{TTL} = 1$**.
  2. 1st router decrements TTL by 1 ($\text{TTL} = 0$), drops packet, and returns **ICMP Time Exceeded** error message (revealing its IP).
  3. Source increments TTL to 2 ($\text{TTL} = 2$) and repeats process for next router.

---

## SECTION 6: Access Technologies & Communication Media

### 6.1 Access Networks
- **DSL (Digital Subscriber Line):** Uses existing copper telephone lines. **DMT** modulation. Asymmetric (ADSL - higher downstream rate) or Symmetric (SDSL). Limited strictly by distance to Central Office (DSLAM).
- **HFC (Hybrid Fiber-Coaxial / Cable):** Combination of optical fiber and coaxial cable. Uses **DOCSIS** protocol. Shared medium in coaxial portion.
- **FTTH (Fiber to the Home):** Fiber directly to home. **PON (Passive Optical Network)** architecture with passive optical splitters, **OLT** at central office and **ONT** at subscriber.
- **Wi-Fi (IEEE 802.11):** Wireless LAN. **CSMA/CA** protocol. Frequency bands: 2.4 GHz (long range, interference), 5 GHz (higher speeds), 6 GHz (Wi-Fi 6E/7).
- **4G LTE / 5G NR:** Cellular networks. 5G provides ultra-low latency (URLLC), massive device density (mMTC), and supports Network Slicing.

---

### 6.2 Communication Media
- **Twisted Pair:** UTP (unshielded), STP (shielded). Categories: Cat5e (1 Gbps), Cat6/6a (10 Gbps), Cat7/8. Twisting reduces crosstalk and noise.
- **Coaxial Cable:** Central copper conductor with shielding braid.
- **Optical Fiber:**
  - **Single-Mode Fiber (SMF):** Very thin core ($8-10 \ \mu\text{m}$), uses Laser. Suitable for long distances (tens of km) due to zero modal dispersion.
  - **Multi-Mode Fiber (MMF):** Wider core ($50-62.5 \ \mu\text{m}$), uses LED. Suitable for short distances (Data Centers / buildings) due to modal dispersion.
- **Satellite Communications:**
  - **GEO (Geostationary Earth Orbit - 36,000 km):** Stationary relative to Earth, high propagation delay ($d_{\text{prop}} \approx 250 \text{ ms}$).
  - **LEO (Low Earth Orbit - 500-1500 km, e.g. Starlink):** Low latency ($d_{\text{prop}} \approx 10-20 \text{ ms}$), requires large satellite constellations.

---

## SECTION 7: Routing Algorithms & Protocols

### 7.1 Link State (Dijkstra) vs Distance Vector (Bellman-Ford)

| Characteristic | Link State (LS) | Distance Vector (DV) |
|---|---|---|
| **Algorithm** | Dijkstra (Shortest Path First) | Bellman-Ford |
| **Topology Knowledge** | Full network map at every router | Knowledge of immediate neighbors only |
| **Update Equation** | $D(v) = \min(D(v), D(w) + c(w,v))$ | $d_x(y) = \min_v \{ c(x,v) + d_v(y) \}$ |
| **Protocols** | OSPF, IS-IS | RIP, EIGRP |
| **Convergence Speed** | Fast (loop-free) | Slow (vulnerable to Count-to-Infinity) |

---

### 7.2 Dijkstra Link-State Algorithm
Calculates shortest paths from source node $u$ to all other nodes.

**Execution Steps:**
1. Initialization: $N' = \{u\}$. For each neighbor $v$, $D(v) = c(u,v)$, else $D(v) = \infty$.
2. At each step, select node $w \notin N'$ with minimum $D(w)$ and add it to $N'$.
3. Update values of neighbors of $w$: $D(v) = \min(D(v), D(w) + c(w,v))$.

---

### 7.3 Bellman-Ford Distance Vector Algorithm & Vulnerabilities
In DV, each router maintains distance table and exchanges vectors only with immediate neighbors.

- **Count-to-Infinity Problem:** If a link fails, neighboring routers may exchange stale information incrementally increasing cost to infinity.
- **Mitigation Techniques:**
  - **Split Horizon:** A router does not advertise a route back out the interface from which it learned that route.
  - **Poison Reverse:** If router $X$ routes to $Y$ via $Z$, it advertises to $Z$ that its cost to $Y$ is infinity ($\infty$).
  - **RIP Hop Limit:** RIP protocol caps maximum hop count at **15 hops** (16 considered infinity / unreachable).

---

### 7.4 Cisco IOS Router Configuration & Route Redistribution

#### A. OSPF Routing (Single Area 0)
Wildcard Mask = $255.255.255.255 - \text{Subnet Mask}$.
```text
R>enable
R#configure terminal
R(config)#router ospf 1
R(config-router)#network 10.10.10.0 0.0.0.3 area 0
R(config-router)#network 172.16.8.0 0.0.0.7 area 0
R(config-router)#network 192.168.1.0 0.0.0.255 area 0
R(config-router)#end
```

#### B. RIP version 2 Routing
```text
R>enable
R#configure terminal
R(config)#router rip
R(config-router)#version 2
R(config-router)#no auto-summary
R(config-router)#network 10.15.2.0
R(config-router)#network 10.15.3.0
R(config-router)#network 10.15.6.0
R(config-router)#end
```

#### C. Route Redistribution
If one network uses OSPF and another RIP, routers **do NOT automatically exchange routes**. **Route Redistribution** must be configured on an ASBR (Autonomous System Boundary Router) running both protocols.

---

### 7.5 BGP Routing & Hot-Potato Routing
In BGP (Border Gateway Protocol) between Autonomous Systems (AS):
- **Hot-Potato Routing:**
  When an AS has multiple egress routers towards another AS and AS-Path length is equal, the AS selects the egress router **internally closest to sender** (based on internal IGP cost), to offload the packet as quickly as possible.

---

## SECTION 8: Transport Layer (TCP) & Network Security

### 8.1 TCP Congestion Control
TCP adjusts congestion window ($CWND$) dynamically across 3 states:
1. **Slow Start:** $CWND$ starts at 1 MSS and **doubles every RTT** (exponential growth) until reaching `ssthresh`.
2. **Congestion Avoidance:** $CWND$ increases linearly by **1 MSS per RTT** (Additive Increase).
3. **Loss Event Handling (Fast Retransmit / Fast Recovery):**
   - **Timeout:** `ssthresh` set to half of current $CWND$, and $CWND$ reset to 1 MSS (Slow Start).
   - **Triple Duplicate ACKs:** TCP applies **Fast Recovery**: `ssthresh` set to half, and $CWND$ set to new `ssthresh` (Multiplicative Decrease).

---

### 8.2 RTT Estimation, Timeout & TCP BBR

#### A. RTT Estimation & Timeout
- $\text{EstimatedRTT} = (1-\alpha) \cdot \text{EstimatedRTT} + \alpha \cdot \text{SampleRTT}$ ($\alpha = 0.125$).
- $\text{Timeout} = 2 \times \text{EstimatedRTT}$ (or $\text{EstimatedRTT} + 4 \cdot \text{DevRTT}$).
- **Karn's Algorithm:** $SampleRTT$ samples are taken **only** for segments transmitted successfully **without retransmission**.
- **TCP Timestamps Option (RFC 7323):** Adds timestamp header for accurate RTT computation even during retransmissions.

#### B. TCP BBR Algorithm (Bottleneck Bandwidth and RTT)
$$CWND = RtProp \times BtlBw$$
- $RtProp = \min(RTT)$, $BtlBw$: Bottleneck bandwidth.
- **Example:** If $RtProp = 5 \text{ ms}$ and $BtlBw = 0.125 \text{ GB/s} = 10^8 \text{ Bytes/s} = 8 \times 10^8 \text{ bps}$:
  $$CWND = 0.005 \text{ s} \times 8 \times 10^8 \text{ bps} = 4,000,000 \text{ bits} \ (500,000 \text{ Bytes})$$

---

### 8.3 Basic Principles of Network Security
- **Symmetric Encryption:** Same secret key for encryption/decryption (e.g. AES). Extremely fast.
- **Asymmetric Encryption / Public Key:** Pair of Public & Private Keys (e.g. RSA).
- **Digital Signature:** Ensures Authentication and Non-repudiation.
- **Firewalls:**
  - **Stateless Packet Filter:** Inspects each packet independently based on IP, Port, Protocol.
  - **Stateful Inspection:** Tracks connection state (Connection state table).

---

## Complete Exam Preparation Checklist (10/10)

- [ ] Distinguish Simplex, Half-Duplex, Full-Duplex, and Multiplexing (FDM/TDM).
- [ ] Know difference between Encapsulation/Decapsulation and how MAC changes while IP remains constant.
- [ ] Understand difference between Control Plane (Software/RIB) and Data Plane (Hardware/FIB).
- [ ] Calculate Nodal Delay ($d_{\text{nodal}}$) and know $N$ is measured in **hops**, not routers.
- [ ] Apply End-to-End delay formulas for Symmetric ($N \cdot d_{\text{nodal}}$) and Asymmetric ($\sum d_i$) links.
- [ ] Calculate total multi-packet transfer time with Pipelining: $(N + P - 1) \cdot d_{\text{trans}} + N \cdot d_{\text{prop}}$.
- [ ] Know minimum window size formula $W = R \times \text{RTT}$ for 100% utilisation.
- [ ] Calculate BDP based on Student ID.
- [ ] Solve Subnetting problems (CIDR /26, /29, /30) and apply Longest Prefix Match (LPM) rule.
- [ ] Know formula $L_{\text{min}} \ge 2 \cdot t_{\text{prop}} \cdot R$ in CSMA/CD and difference with CSMA/CA (Wi-Fi).
- [ ] Construct Hamming code (odd/even parity) and calculate CRC divisions (Modulo-2 / XOR).
- [ ] Know ARP Request (Broadcast) / Reply (Unicast) operations, ARP Cache, and Default Gateway.
- [ ] Understand Traceroute mechanism (TTL decrement, ICMP Time Exceeded).
- [ ] Distinguish access technologies (DSL, HFC/DOCSIS, FTTH/PON) and media (Single-Mode vs Multi-Mode Fiber, GEO vs LEO Satellites).
- [ ] Solve Dijkstra algorithm exercises using tables.
- [ ] Calculate Bellman-Ford equations in Distance Vector and understand Count-to-Infinity, Split Horizon, Poison Reverse.
- [ ] Know Cisco IOS CLI commands for OSPF (wildcard masks) and RIPv2, and concept of Route Redistribution.
- [ ] Understand Hot-Potato routing in BGP.
- [ ] Understand TCP Congestion Control phases (Slow Start, Congestion Avoidance, Fast Recovery), Karn's algorithm, RFC 7323, and TCP BBR formula $CWND = RtProp \times BtlBw$.
- [ ] Know fundamental Security principles (Symmetric/Asymmetric encryption, Stateful vs Stateless Firewalls).