# Data Switching and Routing
*Data Switching and Routing*

---

## Table of Contents

- [Introduction](#introduction)
- [Information Exchange](#information-exchange)
  - [The Information Exchange Problem](#the-information-exchange-problem)
  - [The Switching Problem](#the-switching-problem)
  - [The Four Types of Delay](#the-four-types-of-delay)
- [Packet Switching and Circuit Switching](#packet-switching-and-circuit-switching)
  - [Circuit Switching](#circuit-switching)
  - [Packet Switching](#packet-switching)
  - [Store-and-Forward Transmission](#store-and-forward-transmission)
  - [Statistical Multiplexing](#statistical-multiplexing)
  - [Comparative Table](#comparative-table)
  - [Worked Numerical Example](#worked-numerical-example)
- [Packet Forwarding](#packet-forwarding)
  - [Control Plane and Data Plane](#control-plane-and-data-plane)
  - [Routing Table and Forwarding Table](#routing-table-and-forwarding-table)
  - [Longest Prefix Match](#longest-prefix-match)
  - [LPM Lookup Example](#lpm-lookup-example)
  - [Packet Lifecycle Trace](#packet-lifecycle-trace)
- [Routing Algorithms](#routing-algorithms)
  - [Routing Algorithm Categories](#routing-algorithm-categories)
  - [Distance Vector Routing](#distance-vector-routing)
  - [Link State Routing](#link-state-routing)
  - [Dijkstra Worked Numerical Example](#dijkstra-worked-numerical-example)
  - [Routing Protocols: RIP, OSPF, BGP](#routing-protocols-rip-ospf-bgp)
  - [Distance Vector vs Link State Comparison](#distance-vector-vs-link-state-comparison)
- [Summary Table](#summary-table)
- [Key Takeaways](#key-takeaways)

---

## Introduction

**Data switching** is the core function of the network core — the mechanism by which information travels from source to destination across chains of intermediate nodes (routers, switches). Effective switching enables data exchange across billions of Internet hosts. Two dominant switching paradigms exist: **circuit switching**, which reserves dedicated resources per connection, and **packet switching**, which dynamically shares capacity across active flows. Understanding these paradigms, packet forwarding mechanisms, and routing algorithms is fundamental for network engineering.

---

## Information Exchange
*Information Exchange*

### The Information Exchange Problem

When two end systems communicate, data rarely flows over a direct physical channel. Instead, it traverses a sequence of **intermediate nodes**. Each node determines how to forward incoming data toward its destination.

```
  Information Exchange across the Network Core
  ────────────────────────────────────────────────────────────────
  [Host A]                                              [Host B]
   Athens                                               New York
     │                                                     │
     │──────[Router 1]──────[Router 2]──────[Router 3]─────│
     │       Athens          Rome            London        │
```

Information exchange achieves two main goals:
1. **Data Transfer:** Delivering bits accurately from source to destination.
2. **Resource Sharing:** Multiplexing multiple flows across shared physical infrastructure.

---

### The Switching Problem

How do we allocate network resources (link bandwidth, router buffers) to serve multiple users concurrently?

| Paradigm | Resource Allocation | Example |
|---|---|---|
| **Circuit Switching** | Dedicated pre-allocated resources | Legacy PSTN telephone network |
| **Packet Switching** | Dynamic on-demand resource allocation | The Internet (IP) |

---

### The Four Types of Delay

At each hop in a packet-switched network, a packet experiences four delay components:

1. **Processing Delay ($d_{proc}$):** Time required for a router to inspect the packet header, check for bit errors, and determine the output interface (< 1 ms in modern routers).
2. **Queuing Delay ($d_{queue}$):** Time spent waiting in router buffer queues for the outbound link to become free.
3. **Transmission Delay ($d_{trans}$):** Time required to push all packet bits onto the link:
   $$d_{trans} = \frac{L}{R}$$
   *(where $L$ is packet length in bits and $R$ is link transmission rate in bps).*
4. **Propagation Delay ($d_{prop}$):** Time required for a bit to travel physical distance $d$ at propagation speed $s$:
   $$d_{prop} = \frac{d}{s}$$

$$\text{Total Nodal Delay } d_{total} = d_{proc} + d_{queue} + d_{trans} + d_{prop}$$

**Key Distinction:** $d_{trans}$ depends on **packet length and link bandwidth**. $d_{prop}$ depends solely on **physical distance and medium speed**.

**Bandwidth-Delay Product & Bits in Flight:**
The maximum number of bits traversing a link at any instant:
$$\text{Bits in flight} = R \times d_{prop}$$

---

## Packet Switching and Circuit Switching
*Packet Switching and Circuit Switching*

### Circuit Switching

**Circuit switching** establishes a **dedicated, end-to-end circuit** between source and destination prior to data transfer. Resources are reserved for the duration of the call.

```
  Circuit Switching Phases
  ────────────────────────────────────────────────────────────────
  Phase 1: Connection Setup
  [Host A]──SETUP──>[R1]──SETUP──>[R2]──SETUP──>[R3]──>[Host B]
            <──ACK──       <──ACK──       <──ACK──

  Phase 2: Data Transfer
  [Host A]══════DATA════[R1]════DATA════[R2]════DATA════[Host B]
           ← Dedicated end-to-end bandwidth reserved →

  Phase 3: Connection Teardown
  [Host A]──RELEASE──>[R1]──RELEASE──>[R2]──RELEASE──>[R3]──>[Host B]
```

**Multiplexing in Circuit Switching:**
- **FDM (Frequency Division Multiplexing):** Total bandwidth is split into narrow frequency bands assigned per circuit.
- **TDM (Time Division Multiplexing):** Time is divided into frames containing fixed slots per circuit.

```
  FDM vs TDM
  ─────────────────────────────────────────────────────────────
  FDM:
  ┌──────────────────────────────────────────────────────────┐
  │ Freq 1: User A                                           │
  │ Freq 2: User B                                           │
  │ Freq 3: User C                                           │
  └──────────────────────────────────────────────────────────┘

  TDM:
  ┌──────────────────────────────────────────────────────────┐
  │ Frame: [A][B][C][D][A][B][C][D][A][B][C][D]             │
  └──────────────────────────────────────────────────────────┘
```

**Drawbacks:** Idle capacity is wasted when active connections are silent; setup phase introduces connection establishment latency.

---

### Packet Switching

**Packet switching** divides data streams into discrete **packets**. Each packet carries destination addressing headers and is routed independently hop-by-hop.

```
  Packet Switching
  ────────────────────────────────────────────────────────────────
  Message split into packets (e.g. 3 x 1000 bits):
  [Host A]       [Router 1]       [Router 2]       [Host B]
     │──Pkt 1───>│                │                │
     │──Pkt 2───>│                │                │
     │           │──Pkt 1────────>│                │
     │           │                │──Pkt 1────────>│
```

- **No Resource Reservation:** Links are consumed on-demand.
- **Store-and-Forward:** Routers store complete packets before forwarding.
- **Queuing & Loss:** Overflowing router buffers drop packets (**packet loss**).

---

### Store-and-Forward Transmission

A router must receive the **entire packet** before transmitting the first bit onto the next link.

```
  Store-and-Forward Delay (2 Hops, R = 1 Mbps, L = 1000 bits)
  ────────────────────────────────────────────────────────────────
  Time:   0ms          1ms          2ms
  [Host A] ═══PKT══════▶
  [Router]             ┌──────▶ Store PKT
                       ═══PKT══════▶
  [Host B]                          Received
```

$$\text{End-to-End Store-and-Forward Delay for } N \text{ links: } d_{end-to-end} = N \times \frac{L}{R}$$

---

### Statistical Multiplexing

Packet switching uses **statistical multiplexing** to share bandwidth dynamically. Because Internet traffic is **bursty**, idle periods from one user are harvested to carry packets for another, achieving higher link utilization than TDM/FDM.

---

### Comparative Table

| Feature | Packet Switching | Circuit Switching |
|---|---|---|
| **Resource Reservation** | None (on-demand) | Dedicated pre-allocation |
| **Bandwidth Efficiency** | High (statistical multiplexing) | Low (idle time wasted) |
| **Setup Delay** | None | Required setup phase |
| **Packet Loss** | Possible (buffer overflow) | None (dedicated path) |
| **QoS Guarantees** | Best-effort (default) | Guaranteed fixed bandwidth |
| **Primary Use Case** | Bursty data (web, email) | Constant rate (PSTN voice) |

---

### Worked Numerical Example

**Scenario:** Transmitting a 3 MB file from Host A to Host B across 3 hops ($N=3$). Link rate $R = 10 \text{ Mbps}$. Packet size $L = 12,000 \text{ bits}$ (1,500 bytes MTU). Ignore queuing/propagation delay.

1. **File size in bits:** $F = 3 \times 10^6 \text{ bytes} = 24 \times 10^6 \text{ bits}$
2. **Number of packets:** $n = \frac{24,000,000}{12,000} = 2,000 \text{ packets}$
3. **Transmission delay per packet:** $d_{trans} = \frac{12,000}{10^7} = 1.2 \text{ ms}$
4. **Pipelined End-to-End Delay:**
   $$d_{total} = (n + N - 1) \times d_{trans} = (2000 + 3 - 1) \times 1.2 \text{ ms} = 2,002 \times 1.2 \text{ ms} \approx 2.4024 \text{ s}$$

---

## Packet Forwarding
*Packet Forwarding*

### Control Plane and Data Plane

- **Control Plane:** Router logic computing topology and paths using routing protocols (OSPF, BGP). Operates in software.
- **Data Plane:** High-speed hardware (ASICs/TCAM) forwarding packets from input to output ports using forwarding tables. Operates in nanoseconds.

```
  Control Plane vs Data Plane
  ────────────────────────────────────────────────────────────────
  ┌──────────────────────────────────────────────────────────┐
  │                    ROUTER                                │
  │  Control Plane (Software): Routing Protocols (OSPF/BGP)  │
  │  └──────────────────────┬─────────────────────────────┘  │
  │                         │ Installs routes                │
  │                         ▼                                │
  │  Data Plane (Hardware): Forwarding Table (FIB) Lookup    │
  └──────────────────────────────────────────────────────────┘
```

---

### Routing Table and Forwarding Table

- **RIB (Routing Information Base / Routing Table):** Master database of all routes known to the control plane.
- **FIB (Forwarding Information Base / Forwarding Table):** Hardware-optimized subset of best routes used by the data plane.

---

### Longest Prefix Match

When looking up a packet's destination IP in a forwarding table, multiple matching prefix entries may exist. The router enforces **Longest Prefix Match (LPM)**: selecting the entry with the longest (most specific) subnet mask.

#### LPM Lookup Example

Forwarding Table:
- `192.168.0.0/16` → Router A
- `192.168.20.0/24` → Router B
- `192.168.20.128/25` → Router C
- `0.0.0.0/0` → Router D

**Destination IP:** `192.168.20.150`
Matches `/16`, `/24`, and `/25`. The router selects **Router C** (`/25` prefix match).

---

### Packet Lifecycle Trace

```
  Host A (Sender) ──▶ Encapsulates IP Packet (TTL=64)
         │
         ▼
  Router R1 (Hop 1) ──▶ Decodes Frame ──▶ FIB Lookup (LPM) ──▶ Decrements TTL (63) ──▶ Recomputes Checksum
         │
         ▼
  Router R2 (Hop 2) ──▶ FIB Lookup (LPM) ──▶ Decrements TTL (62)
         │
         ▼
  Host B (Receiver) ──▶ Decapsulates Packet to Application Layer
```

---

## Routing Algorithms
*Routing Algorithms*

### Routing Algorithm Categories

- **Distance Vector (Bellman-Ford):** Nodes exchange routing vectors only with immediate neighbors (e.g. RIP).
- **Link State (Dijkstra):** Nodes broadcast link states to all routers, constructing full topology maps locally (e.g. OSPF).

```
  Routing Algorithms
       │
       ├── Static Routing (Manual entries)
       └── Dynamic Routing
               ├── Distance Vector (Bellman-Ford: RIP)
               └── Link State (Dijkstra: OSPF)
```

---

### Distance Vector Routing

Nodes calculate distance vectors using the **Bellman-Ford equation**:

$$d_x(y) = \min_{v \in \text{neighbors}(x)} \{ c(x,v) + d_v(y) \}$$

Nodes lack complete topology maps ("routing by rumor"). Vulnerable to **count-to-infinity** loops (mitigated by split horizon and poison reverse).

---

### Link State Routing

Each node floods **Link State Advertisements (LSAs)** across the domain. All routers build identical **Link State Databases (LSDB)** and run **Dijkstra's Shortest Path First (SPF)** algorithm.

---

### Dijkstra Worked Numerical Example

**Topology Costs:**
- $A \to B: 1$, $A \to C: 4$
- $B \to D: 2$, $B \to E: 3$
- $D \to F: 1$, $C \to E: 2$

**Dijkstra Execution from Source A:**

| Step | Visited | A | B | C | D | E | F |
|---|---|---|---|---|---|---|---|
| 0 | — | **0** | ∞ | ∞ | ∞ | ∞ | ∞ |
| 1 | A | 0 | **1** (via A) | 4 (via A) | ∞ | ∞ | ∞ |
| 2 | B | 0 | 1 | 4 | **3** (via B) | **4** (via B) | ∞ |
| 3 | D | 0 | 1 | 4 | 3 | 4 | **4** (via D) |
| 4 | E | 0 | 1 | 4 | 3 | 4 | 4 |

**Shortest Paths from A:**
- $A \to B: 1$
- $A \to D: 3$ (path $A \to B \to D$)
- $A \to F: 4$ (path $A \to B \to D \to F$)

---

### Routing Protocols: RIP, OSPF, BGP

#### RIP (Routing Information Protocol)
- Distance Vector IGP.
- Metric: Hop count (Max 15 hops; 16 = unreachable).
- Uses UDP port 520, updates every 30 seconds.

```bash
Router(config)# router rip
Router(config-router)# version 2
Router(config-router)# no auto-summary
Router(config-router)# network 192.168.1.0
```

#### OSPF (Open Shortest Path First)
- Link State IGP using Dijkstra.
- Metric: Cost (inversely proportional to bandwidth).
- Organizes large networks into hierarchical **Areas** (Area 0 backbone).
- Operates on IP protocol 89.

```bash
Router(config)# router ospf 1
Router(config-router)# network 192.168.1.0 0.0.0.255 area 0
```
*\*Wildcard mask for `/24` is `0.0.0.255`.*

**Verification Commands:**
- `show ip route`
- `show ip ospf neighbor`
- `show ip ospf interface brief`

#### BGP (Border Gateway Protocol)
- **Path-Vector EGP** inter-connecting **Autonomous Systems (AS)** across the global Internet.
- Operates over TCP port 179.
- Prevents loops by checking for its own AS number in the **AS-Path** attribute.

---

### Distance Vector vs Link State Comparison

| Feature | Distance Vector | Link State |
|---|---|---|
| **Algorithm** | Bellman-Ford | Dijkstra (SPF) |
| **Topology View** | Neighbor vectors only | Full topology map |
| **Updates** | Full table to neighbors periodically | Triggered LSA flooding to all nodes |
| **Convergence** | Slow | Fast |
| **CPU/Memory Demand** | Low | High |
| **Protocols** | RIP, EIGRP | OSPF, IS-IS |

---

## Summary Table

| Concept | Definition | Key Characteristic |
|---|---|---|
| **Circuit Switching** | Reserved dedicated channels per call | Fixed capacity, zero queuing delay |
| **Packet Switching** | Store-and-forward packet transport | High efficiency, statistical multiplexing |
| **Control Plane** | Software routing logic (OSPF/BGP) | Builds RIB/routing table |
| **Data Plane** | Hardware packet forwarding (ASIC) | Uses FIB forwarding table |
| **LPM** | Longest Prefix Match rule | Selects most specific route entry |
| **Distance Vector** | Neighbor-based vector routing | Bellman-Ford algorithm (RIP) |
| **Link State** | Topology map flood routing | Dijkstra algorithm (OSPF) |
| **BGP** | Path-vector inter-AS routing protocol | Powers global Internet routing |

---

## Key Takeaways

- **Packet switching** utilizes statistical multiplexing to serve bursty Internet traffic efficiently.
- **Nodal delay** equals $d_{proc} + d_{queue} + d_{trans} + d_{prop}$.
- **Store-and-forward** requires complete packet reception before retransmission, adding $L/R$ delay per hop.
- Routers separate the **Control Plane** (routing calculations) from the **Data Plane** (hardware forwarding).
- Forwarding lookups enforce **Longest Prefix Match (LPM)**.
- **Link State (OSPF)** provides fast convergence using Dijkstra on full topology maps, while **Distance Vector (RIP)** relies on neighbor rumors.
- **BGP** interconnects Autonomous Systems using path vectors to prevent inter-domain loops.
