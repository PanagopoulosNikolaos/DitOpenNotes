# Lecture 01: Network Core, Packet Switching, and Delay Modeling

This lecture introduces Internet architecture, distinguishing the network edge from the network core, contrasting packet switching with circuit switching, and formulating mathematical models for end-to-end packet transmission delays.

---

## 1. Edge vs. Core in Internet Architecture

The global Internet is conceptually structured into two major subsystems:

```
[ End Systems / Hosts ] <--- Access Networks ---> [ Network Core: Mesh of Interconnected Routers ]
```

### 1.1 The Network Edge
- **End Systems (Hosts):** Machines that run user application programs (e.g., clients, web servers, email hosts, IoT devices).
- **Access Networks:** Technologies connecting end systems to the first edge router:
  - Digital Subscriber Line (DSL) over dedicated twisted-pair copper telephone lines.
  - Hybrid Fiber-Coax (HFC) cable networks using shared frequency-division multiplexing.
  - Fiber-to-the-Home (FTTH) deploying optical splitters (Passive Optical Networks - PON).
  - Wireless access: 4G/5G cellular networks and IEEE 802.11 Wi-Fi.

### 1.2 The Network Core
The network core is a mesh of packet switches and communication links responsible for moving data from source to destination across multiple intermediate hops.

---

## 2. Packet Switching vs. Circuit Switching

Data transfer across the network core fundamentally relies on either packet switching or circuit switching:

| Metric | Circuit Switching | Packet Switching |
|---|---|---|
| **Resource Allocation** | Pre-allocated dedicated channel along path | On-demand dynamic statistical multiplexing |
| **Call Setup Phase** | Mandatory end-to-end circuit reservation | None (connectionless datagram forwarding) |
| **Resource Guarantees** | Guaranteed constant bandwidth, deterministic delay | Best-effort delivery; variable queuing delay |
| **Link Utilization** | Poor during silent periods (idle reserved capacity) | High efficiency through statistical sharing |
| **Congestion Behavior** | Call blocking when capacity is exceeded | Queuing delays and possible packet drops |

### 2.1 Store-and-Forward Transmission
Packet switches employ **store-and-forward transmission**: the switch must receive the entire packet of $L$ bits before it can begin transmitting the first bit onto the outbound link operating at transmission rate $R$ bits/sec.

For a path consisting of $N$ identical links in series (traversing $N - 1$ routers) with zero queuing and propagation delay, the time to transfer a single packet of $L$ bits from source to destination is:

$$
d_{\text{end-to-end}} = N \cdot \frac{L}{R}
$$

If $P$ packets are sent back-to-back over this $N$-hop path, pipelined transmission yields:

$$
d_{\text{total}} = (N + P - 1) \cdot \frac{L}{R}
$$

---

## 3. Four Fundamental Sources of Packet Delay

When a packet traverses a router from an incoming link to an outgoing link, it experiences four distinct delay components:

$$
d_{\text{nodal}} = d_{\text{proc}} + d_{\text{queue}} + d_{\text{trans}} + d_{\text{prop}}
$$

```
+-------------------------------------------------------------------------+
|                              Router Node                                |
|                                                                         |
|  Incoming          [ Processing ]          [ Output Buffer ]   Transmit |
|  Packet   -------> [   Engine   ] -------> [ Queue Queue   ] ---------> |
|                    (d_proc)                (d_queue)           (d_trans)|
+-------------------------------------------------------------------------+
                                                                     |
                                                           Physical Link (d_prop)
                                                                     v
```

### 3.1 Nodal Processing Delay ($d_{\text{proc}}$)
The time required to inspect the packet header, verify the checksum for bit errors, and determine the output link via routing table lookup. Typically microseconds ($\mu\text{s}$) on modern hardware with ternary content-addressable memory (TCAM).

### 3.2 Queuing Delay ($d_{\text{queue}}$)
The time a packet spends waiting in the output buffer queue before being transmitted onto the physical wire. This delay depends dynamically on the queue size and traffic intensity $I$:

$$
I = \frac{L \cdot a}{R}
$$

Where:
- $L$ = packet length in bits
- $a$ = average packet arrival rate (packets/sec)
- $R$ = transmission rate of the output link (bits/sec)

Behavioral regions:
- $I \approx 0$: Negligible queuing delay ($d_{\text{queue}} \approx 0$).
- $I \to 1$: Queuing delay grows asymptotically toward infinity.
- $I > 1$: Arrival rate exceeds departure rate; router buffers overflow, causing packet loss.

### 3.3 Transmission Delay ($d_{\text{trans}}$)
The time required to push all $L$ bits of the packet into the communication link at wire speed $R$:

$$
d_{\text{trans}} = \frac{L}{R}
$$

- $L$ is measured in bits.
- $R$ is link transmission bandwidth (bits per second, bps).
- $d_{\text{trans}}$ is strictly a function of packet size and link bandwidth, completely independent of the physical distance between nodes.

### 3.4 Propagation Delay ($d_{\text{prop}}$)
The time required for a physical signal (electromagnetic wave or light pulse) to propagate from the beginning of the link to the destination switch across physical distance $d$:

$$
d_{\text{prop}} = \frac{d}{s}
$$

- $d$ is the physical length of the link (meters).
- $s$ is the propagation speed of the medium, typically $2 \times 10^8 \text{ m/s}$ in copper or optical fiber, and $3 \times 10^8 \text{ m/s}$ in free space.
- $d_{\text{prop}}$ is strictly a function of physical distance and medium physics, completely independent of packet size $L$ or transmission rate $R$.

---

## 4. Bandwidth-Delay Product (BDP)

The Bandwidth-Delay Product measures the volume of data that can be "in flight" across a transmission link at any given instant:

$$
\text{BDP} = R \times d_{\text{prop}}
$$

- Units: $\text{bits} = (\text{bits/sec}) \times \text{seconds}$.
- Physical Interpretation: The "volume" of the transmission pipe. If $R = 1 \text{ Gbps}$ and Round-Trip Time $\text{RTT} = 50 \text{ ms}$, the pipe capacity is $10^9 \times 0.050 = 50 \text{ Mbits} = 6.25 \text{ MB}$. A sender must maintain a transmission window at least as large as the BDP to fully saturate the link without stalling for acknowledgments.

---

## 5. End-to-End Delay and Throughput

For a path with $K$ router hops (meaning $K+1$ physical links with lengths $d_i$, speeds $s_i$, and bandwidths $R_i$), total end-to-end latency for a single packet is:

$$
d_{\text{end-to-end}} = \sum_{i=1}^{K+1} \left( d_{\text{proc}, i} + d_{\text{queue}, i} + \frac{L}{R_i} + \frac{d_i}{s_i} \right)
$$

The sustained end-to-end **throughput** of a path is constrained by the bottleneck link:

$$
\text{Throughput} = \min(R_1, R_2, \dots, R_{K+1})
$$

