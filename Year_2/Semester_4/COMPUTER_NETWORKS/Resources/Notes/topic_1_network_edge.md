# Network at the Edge
*The Network at a Glance*

---

## Table of Contents

- [Introduction](#introduction)
- [End Systems](#end-systems)
  - [The Network as a Service](#the-network-as-a-service)
  - [Client Application](#client-application)
  - [Central Node](#central-node)
  - [Peer-to-Peer Networks](#peer-to-peer-networks)
- [Network Access Provision](#network-access-provision)
  - [Wired System Connectivity](#wired-system-connectivity)
  - [Wireless Connectivity](#wireless-connectivity)
  - [Communication Media (Cables)](#communication-media-cables)
  - [Telecommunications Services](#telecommunications-services)
- [Summary Table](#summary-table)
- [Key Takeaways](#key-takeaways)

---

## Introduction

The **Network at the Edge** (network at a glance / network edge) constitutes the outer layer of the Internet architecture — the collection of devices and access mechanisms located at the "periphery" of the network infrastructure. Understanding this domain is fundamental, as it is here that data traffic managed by the network core is generated and consumed. This topic explores **end systems** (hosts) — devices running applications —, their communication models (client-server, peer-to-peer), as well as access technologies and physical media connecting them to the rest of the network. Knowledge of this section serves as an essential foundation for studying network structure, data switching, and protocols to follow.

---

## End Systems
*End Systems / Hosts*

**End systems**, also known as **hosts**, are devices located at the edges of the network that execute applications. Examples: personal computers, smartphones, tablets, servers, IoT sensors, smart TVs. They are called "end" systems because they represent the starting or ending point of communication — in contrast to intermediate nodes (routers, switches) that merely forward data.

```
  Network Edge
  ─────────────────────────────────────────────────────
  [Laptop]   [Smartphone]   [Smart TV]   [IoT Sensor]
      \           |              |             /
       \          |              |            /
        ──────────[Access Network]─────────────────
                                   |
                          [Network Core]
                                   |
                          [Other End Systems]
```

End systems communicate via **application-layer protocols** such as HTTP, SMTP, FTP, DNS, belonging to Layer 7 of the OSI model.

---

### The Network as a Service
*The Network as a Service*

#### Technical Terminology

The concept of "network as a service" examines communication infrastructure from the perspective of **what it provides** to applications running on end systems. In this framework, the network functions as an **abstract pipe** transporting data between applications, without the developer needing to know internal implementation details.

In modern times, this concept is often realized as **NaaS (Network as a Service)** — a cloud service delivery model where organizations "rent" network capabilities (bandwidth, routing, firewalling) instead of purchasing and maintaining physical hardware.

#### ISP Model (Internet Service Provider)

Internet access is provided hierarchically via **ISPs (Internet Service Providers)**:

| ISP Tier | Role | Examples |
|---|---|---|
| **Tier 1** | Global backbone — owns undersea fiber-optic cables | AT&T, Deutsche Telekom, NTT |
| **Tier 2** | Regional — buys transit from Tier 1 | Vodafone, Cosmote |
| **Tier 3** | Local — "last mile" to home or business | local ISPs, cable companies |

**Important Distinction:** Tier 1 ISPs exchange data traffic with each other via **settlement-free peering** (free of charge), while Tier 2 and Tier 3 pay for transit.

#### What the Network Offers to Applications

The Internet offers two primary service categories to applications:

1. **Connection-oriented reliable service (TCP):** Guaranteed, in-order data delivery, flow control, congestion control. Used by HTTP, SMTP, FTP.
2. **Connectionless unreliable service (UDP):** Faster, without delivery or ordering guarantees. Used by DNS, video streaming, VoIP.

```
  Application Layer
         |
  [TCP or UDP] ← Selection based on requirements
         |
  [IP - Network Layer]
         |
  [Link Layer + Physical Layer]
         |
  ~~~~~~ Physical Network ~~~~~~
```

---

### Client Application
*Client Application / Client-Server Architecture*

#### Client-Server Architecture

In the **client-server** model, there is a clear division of roles:

- **Client:** The host requesting a service. Initiates communication, has dynamic (non-permanent) connection, often has a changing IP address. Example: web browser (Chrome, Firefox).
- **Server:** The host providing the service. Operates continuously (always-on), has a static IP address, serves multiple clients simultaneously. Example: web server (Apache, Nginx).

```
  Client-Server Model
  ─────────────────────────────────────────────
  [Client A]               [Server]
      |                       |
      |--- HTTP GET /index --> |
      |                       |
      | <-- HTTP 200 OK ------  |
      |    (HTML content)     |
      |                       |
  [Client B]                 |
      |                       |
      |--- HTTP GET /login --> |
      |                       |
      | <-- HTTP 200 OK ------  |
```

#### Characteristics and Examples

Today, servers are hosted in large **data centers** (e.g. AWS, Google Cloud, Azure) housing thousands of servers simultaneously. A Google data center may contain hundreds of thousands of servers.

| Application | Client | Server |
|---|---|---|
| Web browsing | Chrome, Firefox | Apache, Nginx |
| Email | Outlook, Gmail app | SMTP/IMAP server |
| Streaming | Netflix app | CDN servers (Akamai) |
| Online gaming | Game client | Game server |

**Exam Note:** In client-server architecture, only the server has a permanently known IP address. The client does not need to know the IP addresses of other clients.

---

### Central Node
*Central Node / Server*

#### Definition and Function

The **central node** (server) is the dedicated host providing services to multiple clients simultaneously. Within the course context, this term refers to the server in client-server architecture.

**Key characteristics of a server:**
- Runs continuously (24/7 uptime)
- Has a static, well-known IP address
- Can serve thousands of concurrent connections
- Typically located in data centers with guaranteed uptime, cooling, and power

#### Scalability

An individual server has limited capacity. To serve millions of users, **server farms** or **cloud platforms** with load balancing are utilized:

```
                   [DNS / Load Balancer]
                   /        |         \
            [Server 1]  [Server 2]  [Server 3]
                \          |           /
                 [Shared Database / Storage]
```

**Key Distinction:** A central node is an *end system* — it does not forward packets to other networks. That is the responsibility of routers, which belong to the network *core*.

---

### Peer-to-Peer Networks
*Peer-to-Peer (P2P) Networks*

#### Operating Principle

In the **Peer-to-Peer (P2P)** model, there is no dedicated server. Instead, participating devices — **peers** — communicate directly with each other, acting simultaneously as clients *and* servers.

**Analogy:** Imagine a group of students sharing notes directly with each other, rather than all fetching them from a central printer (server).

```
  Peer-to-Peer Model
  ─────────────────────────────────────────────
       [Peer A] ←──────────→ [Peer B]
           \                   /
            \                 /
             \               /
              [Peer C] ←──→ [Peer D]
                \
                 [Peer E]

  Each Peer: Downloads AND uploads data simultaneously
```

#### Characteristics and Advantages

| Characteristic | Client-Server | Peer-to-Peer |
|---|---|---|
| Dedicated server | Yes | No (or minimal) |
| Scalability | Limited by server | Increases with peers |
| Reliability | Dependent on server | Resilient to failures |
| Control | Centralized | Decentralized |
| Server bandwidth | Bottleneck | Distributed |

**P2P Examples:**
- **BitTorrent:** Every peer downloading a file simultaneously uploads it to others. The more peers present (seeders), the faster the download.
- **Skype (legacy architecture):** Used P2P for call management.
- **Blockchain/Cryptocurrencies:** Bitcoin, Ethereum operate on decentralized P2P networks.

**Exam Note:** In P2P, **self-scalability** is the main advantage: every new peer joining brings additional resources (bandwidth, storage) to the network. In client-server, adding clients increases demand only on the server.

#### Hybrid Models

Many modern systems use a **hybrid architecture**: central server for **discovery** (finding peers) and direct P2P communication for data transfer. Example: modern Skype (Microsoft) and streaming platforms.

---

## Network Access Provision
*Network Access Provision*

**Network access provision** refers to how end systems physically connect to the Internet core. It addresses the **"last-mile"** connectivity problem — connecting from home or office to the nearest ISP node.

---

### Wired System Connectivity
*Wired System Connectivity*

#### DSL (Digital Subscriber Line)

**DSL** uses existing **copper telephone lines** to transmit digital data. A **DSL modem** at home converts digital data into high-frequency signals, which are separated from voice traffic at the **DSLAM** (DSL Access Multiplexer) in the ISP local central office.

```
  DSL Architecture
  ─────────────────────────────────────────────────────────────
  [Home]                                      [Central Office]
  [PC] ── [DSL Modem] ── copper line ──────── [DSLAM] ──── [Internet]
                          (existing phone line)     |
                                                [Telephone Network]
```

**DSL Types:**

| Type | Download | Upload | Characteristic |
|---|---|---|---|
| **ADSL** (Asymmetric DSL) | 1 – 24 Mbps | 0.5 – 3 Mbps | Download >> Upload |
| **VDSL** (Very-high-speed DSL) | 52 – 100 Mbps | 16 – 40 Mbps | Close to central office |
| **SDSL** (Symmetric DSL) | = Upload | = Download | Business applications |

**Key Distinction:** DSL speed critically depends on **distance** to the central office. For distance > 5 km, speed degrades dramatically due to signal attenuation.

#### HFC (Hybrid Fiber-Coaxial)

**HFC** ("cable Internet") uses **optical fiber** up to a local neighborhood node (**fiber node**) and **coaxial cable** from the node to the home.

```
  HFC Architecture
  ─────────────────────────────────────────────────────────────
  [ISP Headend] ── [Fiber] ── [Fiber Node] ── [Coaxial] ── [Home 1]
                                                         └── [Home 2]
                                                         └── [Home 3]
                        (shared coaxial segment)
```

**HFC Characteristics:**
- Speeds: 10 Mbps – 2+ Gbps (with DOCSIS 3.1)
- **Shared medium:** Coaxial segment is shared among neighbors — speeds can drop during peak hours
- Asymmetric: download >> upload

#### FTTH (Fiber to the Home)

**FTTH** brings **optical fiber** directly into the user's home. It is the gold standard for residential connections.

**FTTH Architectures:**
- **AON (Active Optical Network):** Uses active equipment (switches) in the network.
- **PON (Passive Optical Network):** Uses passive optical splitters without electricity in the external network — cheaper and more widespread.

```
  PON Architecture (Passive Optical Network)
  ──────────────────────────────────────────────────────────
  [OLT at ISP] ── Fiber ── [Passive Splitter] ── [ONT at Home 1]
                                              ├── [ONT at Home 2]
                                              └── [ONT at Home 3]
  OLT = Optical Line Terminal
  ONT = Optical Network Terminal
```

**Comparative Table of Wired Technologies:**

| Technology | Physical Medium | Typical Speeds | Main Advantage | Main Disadvantage |
|---|---|---|---|---|
| DSL | Copper (telephone line) | 1 – 140 Mbps | Uses existing infrastructure | Distance-dependent |
| HFC / Cable | Fiber + Coaxial | 10 Mbps – 2 Gbps | Faster than DSL | Shared bandwidth |
| FTTH | Optical fiber (100%) | 200 Mbps – 20 Gbps | Fastest, symmetric | High installation cost |

**Numerical Example (File Transfer Time):**

Consider a 100 MB file = $100 \times 10^6 \times 8 = 8 \times 10^8$ bits.

$$T_{DSL} = \frac{8 \times 10^8 \text{ bits}}{10 \times 10^6 \text{ bps}} = 80 \text{ sec}$$

$$T_{FTTH} = \frac{8 \times 10^8 \text{ bits}}{1 \times 10^9 \text{ bps}} = 0.8 \text{ sec}$$

FTTH is **100 times** faster than typical DSL (10 Mbps) for the same file transfer.

---

### Wireless Connectivity
*Wireless Connectivity*

#### Wi-Fi (IEEE 802.11)

**Wi-Fi** provides wireless LAN (Local Area Network) access via radio waves. Devices connect to a **Wireless Access Point (WAP)** or **router**, which in turn connects to the Internet via a wired connection (DSL, HFC, or FTTH).

**Wi-Fi Standards:**

| Standard | Frequency Band | Max Speed | Year |
|---|---|---|---|
| 802.11b | 2.4 GHz | 11 Mbps | 1999 |
| 802.11g | 2.4 GHz | 54 Mbps | 2003 |
| 802.11n (Wi-Fi 4) | 2.4 / 5 GHz | 600 Mbps | 2009 |
| 802.11ac (Wi-Fi 5) | 5 GHz | 3.5 Gbps | 2013 |
| 802.11ax (Wi-Fi 6) | 2.4 / 5 / 6 GHz | 9.6 Gbps | 2019 |

**Key Distinction:** Wi-Fi is a **LAN** technology (local range, ~30-100m). It is not a WAN technology — it does not independently provide Internet access without a wired backhaul connection.

#### 4G LTE (Long Term Evolution)

**4G LTE** is the fourth generation of mobile telecommunications. Based on **all-packet architecture** (no circuit switching for data — packet switching only).

**4G LTE Characteristics:**
- Typical speeds: 20 – 150 Mbps download, 10 – 50 Mbps upload
- Latency: ~30-50 ms
- Technology: OFDMA (Orthogonal Frequency Division Multiple Access), MIMO
- Applications: HD video streaming, VoLTE, mobile web

#### 5G New Radio (NR)

**5G** represents a radical evolution in mobile communications. Uses **millimeter wave (mmWave)** frequencies (24-100 GHz) for ultra-high speeds, alongside lower frequencies for wider coverage.

**4G vs 5G Comparison Table:**

| Parameter | 4G LTE | 5G NR |
|---|---|---|
| Max speed | ~1 Gbps (theoretical) | ~20 Gbps (theoretical) |
| Typical speed | 20-150 Mbps | 100 Mbps – 1 Gbps |
| Latency | 30-50 ms | < 1 ms |
| Device density | ~100K/km² | ~1M/km² |
| Core use case | Smartphone broadband | IoT, autonomous vehicles, AR/VR |

**5G Technologies:**
- **Massive MIMO:** Hundreds of antennas at the base station to serve many users simultaneously.
- **Beamforming:** Directing signals toward a specific user instead of radial broadcasting.
- **Network Slicing:** Creating virtual networks on top of the same infrastructure (e.g., one slice for autonomous vehicles with ultra-low latency, another for streaming).

---

### Communication Media (Cables)
*Communication Media (Cables)*

**Physical transmission media** define how bits physically travel from sender to receiver. Divided into **guided media** (cables, fibers) and **unguided media** (wireless).

#### Twisted Pair Copper Wire

**Twisted pair** is the most common cable in LANs. Consists of two insulated copper wires twisted around each other (to reduce electromagnetic interference).

- **UTP (Unshielded Twisted Pair):** Categories Cat5e (1 Gbps), Cat6 (10 Gbps at 55m), Cat6a (10 Gbps at 100m).
- **Uses:** Ethernet LAN, DSL.

#### Coaxial Cable

**Coaxial** consists of a central copper conductor, insulation, an outer conductor (braid), and outer shielding. Offers better shielding than twisted pair.

- **Speeds:** Hundreds of Mbps to Gbps.
- **Uses:** HFC networks (cable internet), TV signal.

#### Fiber Optic Cable

**Optical fiber** transmits data as pulses of **light** inside glass or plastic fibers. Immune to electromagnetic interference and allows long distances without repeaters.

- **Single-Mode Fiber (SMF):** Thin core (~9 $\mu m$), uses laser. For long distances (intercontinental links, > 100 km).
- **Multi-Mode Fiber (MMF):** Thicker core (~50-62.5 $\mu m$), uses LED. For short distances (data centers, buildings).
- **Speeds:** 10 Gbps – Tbps (Terabits per second).

```
  Optical Fiber Structure (Single-Mode)
  ─────────────────────────────────────
  | Jacket (outer) |
  | Cladding (reflection) |
  | Core (light beam, ~9 $\mu m$) |
     → → → → → → → → (light pulses)
```

**Physical Media Comparison:**

| Medium | Bandwidth | Distance | Cost | Vulnerability |
|---|---|---|---|---|
| Twisted Pair (Cat6) | 10 Gbps | ~100 m | Low | EM interference |
| Coaxial | Hundreds Mbps | Km | Medium | Moderate |
| Optical Fiber (SMF) | Tbps | Hundreds Km | High | Physical damage |

---

### Telecommunications Services
*Telecommunications Services*

#### PSTN (Public Switched Telephone Network)

**PSTN** is the global voice communication network developed during the 20th century. Historically based on **circuit switching** — before each call, a dedicated channel (circuit) is reserved for the duration of the conversation.

```
  Circuit Switching (PSTN)
  ────────────────────────────────────────────────────────
  Call from Athens → Thessaloniki:
  [A] ──[link1]── [Switch1] ──[link2]── [Switch2] ──[link3]── [B]
        Reserved:  link1 + link2 + link3  for full duration
                   (idle if no one talks)
```

**Circuit switching characteristics:**
- Guaranteed bandwidth for connection duration
- Wasted resources during silent periods (if no one talks, resource remains reserved but idle)
- Today, PSTN uses digital switching

#### VoIP (Voice over Internet Protocol)

**VoIP** carries voice as digital packets (packet switching) over the Internet, instead of dedicated circuits. Examples: Skype, WhatsApp, Viber, Microsoft Teams.

**Protocols:** SIP (Session Initiation Protocol) for call setup, RTP (Real-time Transport Protocol) for voice transport.

#### Mobile Network Evolution

| Generation | Technology | Switching Type | Key Feature |
|---|---|---|---|
| 2G (GSM) | TDMA/CDMA | Circuit (voice) + Packet (GPRS/EDGE) | SMS, basic web |
| 3G (UMTS) | WCDMA | Both | Mobile internet, video calls |
| 4G (LTE) | OFDMA | All-Packet | HD streaming, VoLTE |
| 5G (NR) | OFDMA + mmWave | All-Packet | IoT, ultra-low latency |

**Exam Note:** The transition from 3G to 4G marks the complete shift to **all-IP architecture** in the network core. In 4G, voice is transported as VoLTE (Voice over LTE) — packet-switched, not circuit-switched.

#### Protocol Interaction (HTTP Request)

Example interaction of an end system with a telecom/web service:

```
  HTTP Request-Response Sequence
  ─────────────────────────────────────────────────────
  [Client / Browser]                 [Web Server]
        |                                  |
        |-- TCP SYN ---------------------->|
        |<-- TCP SYN-ACK ------------------|
        |-- TCP ACK ---------------------->|
        |   (TCP Three-way handshake)      |
        |                                  |
        |-- GET /index.html HTTP/1.1 ----->|
        |   Host: www.example.com          |
        |                                  |
        |<-- HTTP/1.1 200 OK --------------|
        |   Content-Type: text/html        |
        |   (HTML body)                    |
        |                                  |
```

---

## Summary Table

| Concept | Definition | Key Characteristic |
|---|---|---|
| **End System / Host** | Peripheral device running applications | Origin/destination of communication |
| **Client-Server** | Model where server provides services to clients | Server: always-on, static IP |
| **Peer-to-Peer (P2P)** | Decentralized model — peers exchange directly | Self-scalability, resilience |
| **ISP** | Internet Service Provider | Tier 1/2/3 hierarchy |
| **DSL** | Digital connection over copper (phone line) | Speed distance-dependent |
| **HFC** | Hybrid (fiber + coaxial) cable connection | Shared bandwidth |
| **FTTH** | Optical fiber directly to home | Fastest, symmetric |
| **Wi-Fi (802.11)** | Wireless LAN | Local range (~100m) |
| **4G LTE** | 4th generation mobile telecommunications | All-packet, VoLTE |
| **5G NR** | 5th generation — mmWave + Massive MIMO | Ultra-low latency, network slicing |
| **Twisted Pair** | Two twisted copper wires | Ethernet LAN, DSL, low cost |
| **Coaxial** | Central conductor + shielding braid | HFC, cable TV |
| **Optical Fiber (SMF)** | Light transmission in glass fiber | Tbps, immune to EM interference |
| **PSTN** | Public Switched Telephone Network | Circuit switching |
| **VoIP** | Voice as packets over IP | Packet switching, SIP/RTP |
| **Circuit Switching** | Dedicated channel for connection duration | Guaranteed QoS, resource waste |
| **Packet Switching** | Data segmented into packets | Efficient resource use, delays possible |

---

## Key Takeaways

- **End systems** (hosts) reside at the Internet periphery and execute applications — not routers forwarding traffic.
- The **client-server** model requires an always-on server with a static IP, scaled via data centers and load balancers.
- The **peer-to-peer** model is decentralized: each new peer adds both demand *and resources* — this is self-scalability.
- **DSL** speed critically depends on distance to the central office. **HFC** shares bandwidth among neighbors. **FTTH** provides maximum speed and symmetry.
- **Wi-Fi** is a local area network (LAN) technology, not WAN — requires a wired backhaul connection.
- **5G** surpasses 4G in speed (20 Gbps vs 1 Gbps), latency (< 1 ms vs 30-50 ms), and IoT device density.
- **Single-mode optical fiber** delivers Tbps speeds over hundreds of kilometers — forming the Internet backbone.
- **PSTN** relies on circuit switching (dedicated channel), whereas the Internet and 4G/5G rely on packet switching (more efficient).
- **VoIP** (Skype, WhatsApp) transports voice as IP packets, gradually replacing traditional PSTN.
- The ISP hierarchy (Tier 1/2/3) implements the Internet as a "network of networks" — Tier 1 exchange traffic for free (settlement-free peering), Tier 2/3 pay for transit.
