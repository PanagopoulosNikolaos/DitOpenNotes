# Network Structure
*Network Structure*

---

## Table of Contents

- [Introduction](#introduction)
- [Network Edge](#network-edge)
  - [Clients and Servers](#clients-and-servers)
  - [Access Networks](#access-networks)
- [Network Core](#network-core)
  - [Interconnected Routers](#interconnected-routers)
  - [Network of Networks](#network-of-networks)
- [Nodes](#nodes)
  - [Routers, Switches, Modems](#routers-switches-modems)
  - [Intermediate Nodes in Access Networks](#intermediate-nodes-in-access-networks)
- [Worked Numerical Example](#worked-numerical-example)
- [Summary Table](#summary-table)
- [Key Takeaways](#key-takeaways)

---

## Introduction

To understand the functioning of the Internet in depth, it is necessary to first grasp its **structure** — how it is architecturally divided into layers and segments. The fundamental distinction lies between the **Network Edge**, where end users and their applications reside, and the **Network Core**, consisting of interconnected networks and routers responsible for forwarding data between them. **Nodes** — routers, switches, modems — serve as basic structural building blocks in both domains, performing different functions depending on their location. This topic builds directly upon previous concepts ("Network Edge", "The Internet") and provides the architectural framework for access technologies, data switching, and routing algorithms.

---

## Network Edge
*The Network Edge*

The **Network Edge** is defined as the outer portion of the Internet — where end users and applications connect. It encompasses **end systems** (hosts), meaning any device generating or consuming data: computers, smartphones, servers, IoT sensors, smart TVs, and any other IP-addressable device connected to the Internet.

**Analogy:** If the Internet were a highway system, the Network Edge would be homes, office buildings, and shopping centers — the origins and destinations of trips. The Network Core would be the highway system connecting them.

```
  Architecture: Network Edge vs Network Core
  ──────────────────────────────────────────────────────────────────────
                         ╔══════════════════════════════╗
                         ║       NETWORK CORE           ║
                         ║                              ║
  [ISP Router A] ════════╣  [Core Router 1]             ║
       |                 ║       |       \              ║
  [ISP Router B] ════════╣  [Core Router 2]─[Core R3]  ║
                         ║       |                      ║
                         ╚═══════╪══════════════════════╝
                                 |
        ┌───────────────────────┬┴─────────────────────┐
        |                       |                       |
  [Access Network]        [Access Network]        [Access Network]
  (DSL/HFC/FTTH)          (Ethernet/Wi-Fi)        (4G/5G)
        |                       |                       |
  ┌─────┴─────┐          ┌──────┴──────┐         ┌─────┴─────┐
  | [Client]  |          | [Server]    |         | [Mobile]  |
  | [Client]  |          | [Server]    |         | [IoT]     |
  └───────────┘          └─────────────┘         └───────────┘
       NETWORK EDGE                                    NETWORK EDGE
```

The Network Edge is functionally divided into two primary categories: **clients** and **servers**, while their physical connection to the Network Core is achieved via **access networks**.

---

### Clients and Servers
*Clients and Servers*

#### The Client-Server Model

The **client-server model** is the dominant architecture of the modern Internet:

- The **client** is the end system **initiating** a request for a service or data. The client requests, receives, and displays — it does not offer services to others.
- The **server** is the end system **listening** for requests, processing them, and returning responses. A server is always-on and reachable via a permanent IP address.

```
  Client-Server Model
  ─────────────────────────────────────────────────────────────────
  [Client: Browser]                         [Server: Google.com]
         |                                           |
         |──── HTTP GET /search?q=networks ─────────>|
         |                                           |
         |<─── HTTP 200 OK + HTML/JSON ──────────────|
         |                                           |
  (Accepts and displays                      (Listens, processes,
   response)                                  responds)
```

**Client Characteristics:**
- Initiates communication with server.
- May be intermittently connected.
- Typically assigned dynamic IP addresses.
- Does not communicate **directly** with other clients (in pure client-server model).
- Examples: web browser, email client, mobile app.

**Server Characteristics:**
- Always-on (24/7 uptime) to serve requests.
- Permanent IP address or DNS hostname.
- Typically hosted in **data centers** for high availability, cooling, and power redundancy.
- Examples: web server (Apache, Nginx), DNS server, email server (SMTP), database server.

#### Data Centers: The Physical Side of Servers

Major companies (Google, Amazon, Meta, Microsoft) operate massive **data centers** — buildings housing thousands of servers. Amazon AWS, for example, operates over 100 data centers globally. These servers have ultra-high-speed connectivity (tens or hundreds of Gbps) to the Network Core.

```
  Data Center Physical Infrastructure
  ──────────────────────────────────────────────────────────────
  ┌─────────────────────────────────────────────────────────┐
  │                     DATA CENTER                         │
  │                                                         │
  │  [Rack 1]   [Rack 2]   [Rack 3]   ... [Rack N]         │
  │  ┌──────┐   ┌──────┐   ┌──────┐       ┌──────┐         │
  │  │Srv 1 │   │Srv 4 │   │Srv 7 │       │Srv N │         │
  │  │Srv 2 │   │Srv 5 │   │Srv 8 │       │...   │         │
  │  │Srv 3 │   │Srv 6 │   │Srv 9 │       │      │         │
  │  └──┬───┘   └──┬───┘   └──┬───┘       └──┬───┘         │
  │     └──────────┴──────────┴───────────────┘             │
  │                     [Top-of-Rack Switch]                │
  │                             |                           │
  │                    [Core Switch / Router]               │
  └─────────────────────────────┬───────────────────────────┘
                                |
                    [ISP / Internet Backbone]
```

#### Peer-to-Peer (P2P) as an Alternative Architecture

In the **Peer-to-Peer (P2P)** model, each end system (peer) acts **simultaneously as client and server** — sharing and consuming resources without a central server.

| Characteristic | Client-Server | Peer-to-Peer (P2P) |
|---|---|---|
| Central server | Yes, always-on | Not required |
| Scalability | Limited (bottleneck) | High (increases with peers) |
| Reliability | Server dependent | Distributed |
| Examples | HTTP, Email, DNS | BitTorrent, Blockchain |
| Management | Centralized (easy) | Distributed (complex) |

**Exam Note:** P2P **scales automatically** — as more peers join, total available bandwidth increases. In client-server models, adding clients increases server load.

---

### Access Networks
*Access Networks*

**Access networks** connect end systems (clients, servers) to the **edge router** of the core network ("last mile").

```
  Access Network Types
  ─────────────────────────────────────────────────────────────────────
                        [Edge Router / ISP]
                               |
          ┌────────────────────┼─────────────────────┐
          |                    |                      |
  [Residential Network][Enterprise Network]   [Mobile Network]
  DSL / HFC / FTTH    Ethernet LAN          4G / 5G
  ~10-1000 Mbps       ~1-100 Gbps           ~10-1000 Mbps
          |                    |                      |
   [Home Router]        [Campus Switch]       [Base Station]
    /    |    \          /    |    \            /    |    \
  [PC][TV][Phone]   [PC][PC][Server]    [Phone][Tablet][IoT]
```

#### Residential Access
- **DSL (Digital Subscriber Line):** Copper telephone lines, asymmetric (ADSL).
- **HFC (Hybrid Fiber-Coaxial):** Shared coaxial cable among neighbors.
- **FTTH (Fiber to the Home):** Optical fiber directly into homes (fastest residential option).
- **Wi-Fi (Wireless LAN):** Wireless connection within homes.

#### Enterprise/Institutional Access
Uses **Ethernet** — high-speed wired LAN (100 Mbps to 100+ Gbps) with hierarchical Ethernet switches.

#### Mobile/Wireless Access
Cellular coverage via **base stations**. **4G LTE** and **5G NR** provide speeds from 10 to 1000+ Mbps.

**Key Distinction:** Residential lines are dedicated (DSL) or shared (HFC). Mobile radio spectrum is always **shared** among users in a cell.

---

## Network Core
*The Network Core*

The **Network Core** is the mesh of interconnected routers and networks responsible for long-distance data transport. The core does not execute application software; its sole function is **forwarding** and **routing** packets as efficiently as possible.

```
  Core Router Forwarding Process
  ─────────────────────────────────────────────────────────────────
  Incoming Packet (Destination IP: 198.51.100.45)
          │
          ▼
  ┌────────────────────────────────────────────────────────┐
  │ [Input Port] ──▶ [Forwarding Table Lookup]             │
  │                  Matches 198.51.100.0/24 ──▶ Port 3    │
  └───────────────────────────┬────────────────────────────┘
                              │
                              ▼
                       [Output Port 3] ──▶ Next Hop Router
```

---

### Interconnected Routers
*Interconnected Routers*

The core relies on **packet switching** across hundreds of thousands of high-speed routers.

#### Packet Switching: Store-and-Forward

In packet switching, each router:
1. **Stores** the entire packet before forwarding (cannot transmit until the final bit arrives).
2. **Processes** the packet header (inspects destination IP).
3. **Forwards** the packet to the output link.

This **store-and-forward** principle introduces transmission delay at every hop.

```
  Store-and-Forward Packet Switching (2 Hops)
  ──────────────────────────────────────────────────────────────────
  [Host A]        [Router R1]        [Router R2]        [Host B]
      |                |                  |                  |
  t=0 |── Packet 1 ───>|                  |                  |
      |                | (receives        |                  |
  t=L/R               |  completely)     |                  |
      |                |── Packet 1 ─────>|                  |
      |                |                  | (receives        |
  t=2L/R              |                  |  completely)     |
      |                |                  |── Packet 1 ─────>|
  t=3L/R              |                  |                  |

  Total end-to-end transmission delay: N * L/R
```

**Exam Note:** **Store-and-forward** requires receiving the **entire** packet before beginning transmission on the next link. It differs from **cut-through switching** which forwards immediately without error checking.

#### Queuing and Packet Loss

If packet arrival rate exceeds link output capacity, packets queue in buffers. If buffers fill completely, arriving packets are **dropped** — resulting in **packet loss**.

```
  Router Queuing: Congestion
  ──────────────────────────────────────────────────────────────────
  [Link 1: 100 Mbps] ──\
  [Link 2: 100 Mbps] ───╬──> [Buffer/Queue] ──> [Link Out: 100 Mbps]
  [Link 3: 100 Mbps] ──/
  (Total Inflow: up to 300 Mbps, Outflow: 100 Mbps → Congestion!)
```

**Traffic Intensity Formula:**

$$\rho = \frac{L \cdot a}{R}$$

- $L$ = packet size (bits)
- $a$ = packet arrival rate (packets/sec)
- $R$ = link bandwidth (bps)

When $\rho \rightarrow 1$, queuing delay approaches infinity. When $\rho > 1$, packet loss is unavoidable.

#### Forwarding vs Routing: Critical Distinction

| Term | Definition | Decision Scope | Speed |
|---|---|---|---|
| **Forwarding** | Transferring packet from input to output interface | Local (per router) | Nanoseconds (hardware) |
| **Routing** | Computing end-to-end paths across network | Global (network-wide) | Seconds/Minutes (software) |

---

### Network of Networks
*Network of Networks*

The Internet is a **network of networks** managed hierarchically by ISPs:

```
  ISP Hierarchy
  ──────────────────────────────────────────────────────────────────────
  ┌─────────────────────────────────────────────────────────────────┐
  │               TIER-1 ISPs (Global Backbone)                     │
  │   AT&T, Lumen, NTT, Deutsche Telekom, Telia                      │
  │   ─────────────────── Peering (free) ──────────────────────────  │
  └────────────────────────────┬────────────────────────────────────┘
                               |  Transit (paid)
          ┌────────────────────┼──────────────────────┐
          |                    |                       |
  ┌───────┴───────┐   ┌────────┴────────┐   ┌─────────┴──────┐
  │  TIER-2 ISP   │   │   TIER-2 ISP   │   │  TIER-2 ISP    │
  │ (Regional)    │   │  (Regional)     │   │  (Regional)    │
  └───────┬───────┘   └────────┬────────┘   └─────────┬──────┘
          |                    |                        |
  ┌───────┴───────┐   ┌────────┴────────┐   ┌─────────┴──────┐
  │  TIER-3 /     │   │   TIER-3 /      │   │  TIER-3 /      │
  │  Access ISP   │   │   Access ISP    │   │  Access ISP    │
  └───────┬───────┘   └────────┬────────┘   └─────────┬──────┘
          |                    |                        |
       [Users]              [Users]                  [Users]
```

- **Tier-1 ISPs:** Global backbone. Interconnect via **peering** (free exchange) without paying transit.
- **Tier-2 ISPs:** Regional providers buying **transit** from Tier-1 and peering with each other.
- **Tier-3 / Access ISPs:** Local providers connecting end users to Tier-2 networks.
- **IXP (Internet Exchange Point):** Physical facilities where ISPs interconnect directly to exchange traffic without Tier-1 transit.
- **Content Provider Networks:** Private networks operated by Google, Meta, Netflix bypass Tier-1 backbones for direct ISP delivery.

---

## Nodes
*Network Nodes*

### Routers, Switches, Modems
*Routers, Switches, Modems*

#### Router
Operates at **Layer 3 (Network Layer)**, routing packets between **different networks** using IP addresses and routing tables.

```
  Simplified Router Architecture
  ──────────────────────────────────────────────────────────────────
  Input Ports ──▶ [Switching Fabric] ──▶ Output Ports
                         ▲
                         │
                 [Routing Processor] (OSPF/BGP software)
```

#### Switch
Operates at **Layer 2 (Data Link Layer)**, forwarding frames between devices **within the same network (LAN)** using MAC addresses. Switch learns MAC locations dynamically in its **MAC Address Table (CAM Table)**.

#### Modem
Operates at **Layer 1 (Physical Layer)** performing signal modulation/demodulation between digital hosts and ISP transmission media (DSL, DOCSIS cable, optical PON).

#### Router vs Switch vs Modem Comparison

| Property | Router | Switch | Modem |
|---|---|---|---|
| **OSI Layer** | Layer 3 (Network) | Layer 2 (Data Link) | Layer 1 (Physical) |
| **Identifier** | IP Address | MAC Address | No addressing |
| **Scope** | Inter-network | Intra-network (LAN) | ISP connection |
| **Primary Function** | Packet routing | Frame switching | Modulation/Demodulation |

---

### Intermediate Nodes in Access Networks
*Intermediate Nodes in Access Networks*

Access networks use specialized intermediate nodes:

#### DSL Access Network
- **DSLAM (DSL Access Multiplexer):** Located at the ISP Central Office, aggregates hundreds of subscriber copper lines into a single fiber trunk toward the core.

#### HFC Access Network
- **HFC Node:** Converts optical signals to coaxial RF signals for neighborhood distribution.
- **CMTS (Cable Modem Termination System):** Located at cable headends, managing subscriber cable modems over a shared coaxial medium.

#### FTTH Access Network (PON)
- **OLT (Optical Line Terminal):** Central office equipment managing the PON network.
- **Optical Splitter:** Passive device splitting single optical fibers to 32–64 subscriber fibers without electrical power.
- **ONT (Optical Network Terminal):** Home subscriber terminal converting optical signals to Ethernet.

---

## Worked Numerical Example
*End-to-End Delay across 3 Hops*

**Scenario:** A packet of size $L = 12,000$ bits is transmitted from a client across 3 hops (2 core routers) to a server.
- Bandwidth: $R = 10 \text{ Mbps} = 10 \times 10^6 \text{ bps}$
- Distance per hop: $d = 500 \text{ km} = 5 \times 10^5 \text{ m}$
- Propagation Speed: $s = 2 \times 10^8 \text{ m/s}$
- Ignore queuing and processing delays.

```
  Topology:
  [Client] ──R1──> [Core Router A] ──R2──> [Core Router B] ──R3──> [Server]
       hop 1                  hop 2                    hop 3
```

**Step 1: Transmission Delay per Hop ($d_{trans}$):**

$$d_{trans} = \frac{L}{R} = \frac{12,000}{10 \times 10^6} = 1.2 \times 10^{-3} \text{ s} = 1.2 \text{ ms}$$

**Step 2: Propagation Delay per Hop ($d_{prop}$):**

$$d_{prop} = \frac{d}{s} = \frac{5 \times 10^5}{2 \times 10^8} = 2.5 \times 10^{-3} \text{ s} = 2.5 \text{ ms}$$

**Step 3: Total End-to-End Delay (Store-and-Forward, $N = 3$ hops):**

$$d_{end\text{-}to\text{-}end} = N \cdot (d_{trans} + d_{prop}) = 3 \times (1.2 + 2.5) = 3 \times 3.7 = 11.1 \text{ ms}$$

**Step 4: Component Breakdown:**

| Component | Per Hop | Total (3 hops) | Share |
|---|---|---|---|
| $d_{trans}$ (Transmission) | 1.2 ms | 3.6 ms | 32% |
| $d_{prop}$ (Propagation) | 2.5 ms | 7.5 ms | 68% |
| **Total** | **3.7 ms** | **11.1 ms** | **100%** |

---

## Summary Table

| Concept | Definition | Key Characteristic |
|---|---|---|
| **Network Edge** | Network segment containing end systems | Users and applications reside here |
| **Network Core** | Mesh of interconnected core routers | Dedicated to packet forwarding & routing |
| **Client** | End system initiating service requests | Dynamic IP, intermittent connection |
| **Server** | End system responding to requests | Always-on, static IP, data centers |
| **Access Network** | Infrastructure connecting edge hosts to ISP | Last-mile connectivity |
| **Router** | Forwards packets between different networks | Layer 3, IP addresses, routing tables |
| **Switch** | Forwards frames within local network | Layer 2, MAC addresses, CAM table |
| **Modem** | Converts signals for ISP physical medium | Layer 1, modulation/demodulation |
| **Packet Switching** | Independent packet transport node-to-node | Store-and-forward, statistical multiplexing |
| **Store-and-Forward** | Router receives full packet before forwarding | Adds $L/R$ delay per hop |
| **Tier-1 ISP** | Global backbone ISP, pays no transit | Settlement-free peering |
| **IXP** | Facility for direct ISP traffic exchange | Reduces latency and transit cost |
| **DSLAM** | Aggregates DSL lines at central office | DSL access network node |
| **CMTS** | Aggregates HFC cable lines at headend | Cable access network node |
| **OLT** | Central PON node controlling FTTH network | Controls optical splitters and ONTs |
| **Packet Loss** | Dropped packets due to full router buffers | Occurs when $\rho = L \cdot a / R > 1$ |

---

## Key Takeaways

- The Internet is architecturally divided into the **Network Edge** (end users, hosts) and the **Network Core** (routers, forwarding, routing).
- In **client-server** models, clients initiate requests to an always-on server with a static IP. **P2P** models distribute roles equally across peers.
- **Access networks** (DSL, HFC, FTTH, Ethernet, 4G/5G) constitute the last-mile connectivity to edge routers.
- **Routers** operate at Layer 3 (IP), **switches** at Layer 2 (MAC), and **modems** at Layer 1 (Physical).
- The Internet is a **network of networks** organized hierarchically: Tier-1 (global backbone) → Tier-2 (regional) → Tier-3/Access ISPs.
- **Store-and-forward** packet switching requires receiving a complete packet before forwarding, introducing $L/R$ delay per hop.
- **Forwarding** (local, hardware, nanoseconds) and **routing** (global path calculation, software, seconds) are distinct, complementary functions.
- **Packet loss** occurs when router queues overflow when traffic intensity $\rho = L \cdot a / R > 1$.
- Intermediate nodes such as **DSLAMs**, **CMTSs**, and **OLTs/Splitters** are specialized access network elements.
- **IXPs** allow ISPs to exchange traffic directly, avoiding Tier-1 transit costs and lowering latency.
