# The Internet
*The Internet*

---

## Table of Contents

- [Introduction](#introduction)
- [Hardware: Equipment and Cables](#hardware-equipment-and-cables)
  - [End Devices](#end-devices)
  - [Interconnection Devices](#interconnection-devices)
  - [Physical Transmission Media](#physical-transmission-media)
- [Protocols (TCP/IP, DNS, etc.)](#protocols-tcpip-dns-etc)
  - [What is a Protocol](#what-is-a-protocol)
  - [The TCP/IP Stack](#the-tcpip-stack)
  - [IP (Internet Protocol)](#ip-internet-protocol)
  - [TCP and UDP](#tcp-and-udp)
  - [Traceroute Utility](#traceroute-utility)
  - [DNS (Domain Name System)](#dns-domain-name-system)
  - [HTTP / HTTPS](#http--https)
- [Fiber Optic and Satellite](#fiber-optic-and-satellite)
  - [Fiber Optic as the Internet Backbone](#fiber-optic-as-the-internet-backbone)
  - [Satellite Communication](#satellite-communication)
  - [Comparison of Fiber Optic and Satellite](#comparison-of-fiber-optic-and-satellite)
- [Data Transfer Between Devices](#data-transfer-between-devices)
  - [Message Segmentation into Packets](#message-segmentation-into-packets)
  - [Transfer Delays](#transfer-delays)
  - [Worked Numerical Example](#worked-numerical-example)
  - [Data Encapsulation](#data-encapsulation)
- [Summary Table](#summary-table)
- [Key Takeaways](#key-takeaways)

---

## Introduction

The **Internet** is the largest and most complex computer network ever constructed — a global "network of networks" connecting billions of devices through standardized communication protocols. Understanding it requires examining three interconnected dimensions: **hardware** — the physical devices and media that constitute it —, **protocols** defining communication rules, and **mechanisms** by which data travels from device to device. This topic explores these three dimensions with an emphasis on high-speed physical media (optical fibers, satellites) and foundational protocols (TCP/IP, DNS) enabling global interconnection. It serves as a bridge between the "Network Edge" previously examined and the deeper analysis of structure, switching, and protocols that follow.

---

## Hardware: Equipment and Cables
*Hardware: Equipment and Cables*

At its most fundamental level, the Internet is a vast physical infrastructure of devices and transmission media. Without this infrastructure, no protocol would function.

### End Devices
*End Devices / Hosts*

**End devices** (hosts) reside at the network edges and generate or consume data. Every such device features a **NIC (Network Interface Card)** — the network card providing physical connectivity.

| Category | Examples | Connection Type |
|---|---|---|
| Personal Computers | Desktop, Laptop | Ethernet (wired), Wi-Fi |
| Mobile Devices | Smartphone, Tablet | Wi-Fi, 4G/5G |
| Servers | Web servers, DNS servers | Ethernet (Gbps or 10 Gbps) |
| IoT Devices | Smart TV, smart thermostat, camera | Wi-Fi, Ethernet, Zigbee |
| Industrial | PLC, sensors | Industrial Ethernet (Profinet) |

---

### Interconnection Devices
*Interconnection Devices*

**Interconnection devices** form the "backbone" of the Internet — nodes receiving, processing, and forwarding data between networks.

#### Router

A **router** is a device connecting different networks and determining the optimal path for each packet. It operates at **Layer 3 (Network Layer)** of the OSI model, using **IP addresses** for routing decisions.

**Analogy:** A router acts like a postal sorting center — receiving letters (packets) from everywhere, reading the recipient (IP address), and dispatching them in the correct direction.

#### Switch

A **switch** connects devices within the **same** network (LAN). It operates at **Layer 2 (Data Link Layer)**, using **MAC addresses** to send data directly to the correct recipient within the LAN.

#### Modem

A **modem** (MOdulator-DEModulator) converts digital signals to analog (and vice versa), enabling data transmission over telephone lines (DSL modem) or coaxial cables (cable modem).

#### Comparison of Core Network Devices

```
  Typical Home Network Architecture
  ────────────────────────────────────────────────────────────
  [Internet / ISP]
         |
     [Modem]   ← Analog to digital conversion
         |
    [Router]   ← Routing between home LAN and Internet
         |
      [Switch]  ← (Internal) Connects LAN devices
     /   |   \
[PC] [Laptop] [NAS]
         |
      [Wi-Fi AP] ← Wireless connectivity
     /        \
[Smartphone] [Tablet]
```

| Device | OSI Layer | Identifier | Application Domain |
|---|---|---|---|
| **Hub** | Layer 1 (Physical) | None | Legacy, broadcast |
| **Switch** | Layer 2 (Data Link) | MAC Address | Within LAN |
| **Router** | Layer 3 (Network) | IP Address | Between networks |
| **Firewall** | Layer 3-7 | IP + Ports | Security |

**Exam Note:** A router joins *different* networks (e.g. LAN to Internet). A switch joins devices *within* the same network. This distinction is critical.

---

### Physical Transmission Media
*Physical Transmission Media*

**Physical transmission media** are channels through which bits travel. Classified into **guided media** (cables) and **unguided media** (wireless).

#### Copper

Copper is used in two primary forms:

- **Twisted Pair:** Two copper wires twisted together to reduce electromagnetic interference. The most widespread form for Ethernet LAN (Cat5e: 1 Gbps, Cat6a: 10 Gbps) and DSL.
- **Coaxial:** Central copper conductor with shielding. Used in HFC networks (cable internet) — speeds from hundreds of Mbps to Gbps.

#### Fiber Optic

**Optical fiber** transmits data as light pulses through glass or plastic fiber. Explored extensively in subsequent sections.

#### Wireless

Wireless media use electromagnetic waves (radio waves, microwaves) to transfer data without physical connections. Examples: Wi-Fi (IEEE 802.11), 4G LTE, 5G NR, Bluetooth.

---

## Protocols (TCP/IP, DNS, etc.)
*Protocols (TCP/IP, DNS, etc.)*

### What is a Protocol
*What is a Protocol*

A **protocol** is a set of rules defining how devices communicate — what messages they send, in what order, and what actions they take.

**Analogy:** A protocol is like a language with strict grammar rules. Two devices speaking different protocols cannot communicate, just as two humans speaking different languages cannot understand each other.

```
  Protocol Analogy: Human Conversation vs Network Communication
  ─────────────────────────────────────────────────────────────────────
  Human:                        Network:
  "Hello!"          →           TCP SYN
  "Hi! How are you?"→           TCP SYN-ACK
  "Good, you?"      →           TCP ACK
  (conversation)    →           (data transfer)
  "Goodbye"         →           TCP FIN
```

Protocols define: (a) message **type** and **format**, (b) **sequence** of exchange, and (c) **actions** taken upon receiving a message.

---

### The TCP/IP Stack
*The TCP/IP Stack*

The **TCP/IP stack** is a 4-layer architectural model describing how protocols work together to enable Internet communication. It is the practical implementation of the theoretical 7-layer OSI model.

```
  TCP/IP Stack (4 Layers)                      Corresponding OSI Layer(s)
  ──────────────────────────────────────────────────────────────────────
  ┌─────────────────────────────────┐
  │   Application Layer             │  ← OSI: Layer 7, 6, 5
  │   HTTP, SMTP, DNS, FTP, SSH     │
  ├─────────────────────────────────┤
  │   Transport Layer               │  ← OSI: Layer 4
  │   TCP, UDP                      │
  ├─────────────────────────────────┤
  │   Internet Layer                │  ← OSI: Layer 3
  │   IP (IPv4, IPv6), ICMP         │
  ├─────────────────────────────────┤
  │   Network Access Layer          │  ← OSI: Layer 2, 1
  │   Ethernet, Wi-Fi, PPP          │
  └─────────────────────────────────┘
```

**Core Principle:** Each layer provides services to the layer above and consumes services from the layer below. A layer does not "know" the internal details of other layers — this principle is called **encapsulation**.

---

### IP (Internet Protocol)
*Internet Protocol*

**IP (Internet Protocol)** is the foundational routing protocol of the Internet. Operating at the **Internet Layer**, it is responsible for:

1. **Addressing:** Every device on the Internet possesses a unique **IP address** used to identify it.
2. **Fragmentation:** Splitting large data items into transmittable packets.
3. **Routing:** Delivering each packet toward its destination via appropriate routers.

#### IPv4 vs IPv6

| Characteristic | IPv4 | IPv6 |
|---|---|---|
| Address length | 32 bits | 128 bits |
| Format | `192.168.1.1` | `2001:db8::1` |
| Number of addresses | ~4.3 billion | ~3.4 × 10^38 |
| Status | Exhausted | In adoption |
| Header | 20 bytes (fixed) | 40 bytes (simplified) |

**Key Distinction:** IPv4 exhausted available address space in 2011. Transitioning to IPv6 provides practically unlimited address space for IoT, 5G, and future devices.

**Exam Note:** IP is **connectionless** and **best-effort** — it does not guarantee delivery, ordering, or duplicate avoidance. These guarantees are provided by TCP at the upper layer.

---

### TCP and UDP
*Transmission Control Protocol and User Datagram Protocol*

The **Transport Layer** provides two primary protocols offering different guarantees:

#### TCP (Transmission Control Protocol)

**TCP** provides **reliable, connection-oriented** communication. Before any data transfer occurs, the **Three-Way Handshake** procedure is executed:

```
  TCP Three-Way Handshake
  ─────────────────────────────────────────────────────
  [Client]                             [Server]
      |                                    |
      |──── SYN (seq=x) ─────────────────>|   Connection request
      |                                    |
      |<─── SYN-ACK (seq=y, ack=x+1) ─────|   Acceptance
      |                                    |
      |──── ACK (ack=y+1) ───────────────>|   Acknowledgement
      |                                    |
      |════ DATA TRANSFER ════════════════>|   Data transfer
      |                                    |
```

**TCP Characteristics:**
- **Reliable delivery:** Retransmission of lost packets.
- **In-order delivery:** Data is delivered in sequence even if packets arrived out of order.
- **Flow control:** Sender adjusts transmission rate to match receiver capacity.
- **Congestion control:** Sender reduces transmission rate when the network is congested.
- **Applications:** HTTP/HTTPS, SMTP, FTP, SSH.

**TCP Sliding Window & Timeout Calculation:**
TCP employs a sliding window mechanism for reliable transfer. The timeout interval before segment retransmission depends on the estimated RTT (Round Trip Time).
- **SampleRTT:** Time measured from segment transmission to receiving corresponding ACK (excluding retransmissions, per Karn's Algorithm). TCP Timestamps option is alternatively used.
- **EstimatedRTT:** Weighted average smoothing network variations (typically $\alpha = 0.875$):
  $$\text{EstimatedRTT} = a \times \text{EstimatedRTT} + (1-a) \times \text{SampleRTT}$$
- **Timeout Interval:** Wait time before retransmission is calculated as:
  $$\text{Timeout} = 2 \times \text{EstimatedRTT}$$

#### UDP (User Datagram Protocol)

**UDP** is **connectionless** and **unreliable** — sending datagrams without guarantees of delivery, ordering, or duplicate avoidance. Conversely, it is **much faster** than TCP due to minimal overhead.

**UDP Applications:** DNS (quick queries), video streaming (better latency), VoIP (Skype, WhatsApp), online gaming, DHCP.

#### TCP vs UDP Comparison

| Characteristic | TCP | UDP |
|---|---|---|
| Connection | Connection-oriented (3-way handshake) | Connectionless |
| Reliability | Guaranteed delivery | No guarantee |
| Data ordering | Preserved | Not preserved |
| Flow control | Yes | No |
| Congestion control | Yes | No |
| Speed | Slower (overhead) | Faster |
| Use cases | HTTP, email, file transfer | DNS, streaming, gaming, VoIP |

---

### Traceroute Utility
*Traceroute Utility*

**Traceroute** (or `tracert` in Windows) is a diagnostic tool tracing the path packets take from sender to destination.
- **Mechanism:** Sends a sequence of IP packets with incrementally increasing Time To Live (**TTL**), starting at $TTL = 1$.
- Each intermediate router decrements TTL by 1.
- When TTL reaches 0, the router drops the packet and returns an **ICMP Time Exceeded** error message, revealing its IP address to the sender.

---

### DNS (Domain Name System)
*Domain Name System*

**DNS** is the "phonebook" of the Internet. It translates human-readable domain names (e.g. `www.google.com`) into numerical IP addresses (e.g. `142.250.185.78`) used by computers.

**Analogy:** DNS is like a multi-tiered directory — instead of knowing everyone's phone number, you ask the directory which looks it up for you.

#### DNS Hierarchy

```
  DNS Hierarchy
  ──────────────────────────────────────────────────────────────
                     [Root DNS Servers]  (13 logical root servers globally)
                    /        |         \
          [.com TLD]    [.org TLD]   [.gr TLD]     (Top-Level Domain)
              |
       [google.com]   (Authoritative DNS server)
              |
       [www.google.com]  → 142.250.185.78
```

**Types of DNS Servers:**
1. **Root DNS Server:** Top level — knows servers for each TLD (Top-Level Domain). 13 logical root servers exist globally (a through m).
2. **TLD DNS Server:** Responsible for a specific TLD (e.g. `.com`, `.gr`).
3. **Authoritative DNS Server:** Holds exact IP addresses for a specific domain (e.g. `google.com`).
4. **Local DNS Server (Resolver):** First contact point — typically provided by ISP or public resolvers (Google: `8.8.8.8`, Cloudflare: `1.1.1.1`).

#### DNS Query Sequence

```
  Complete DNS Query Sequence for "www.example.com"
  ─────────────────────────────────────────────────────────────────
  [Browser / Client]
       |
       |──(1) "Do you know www.example.com?" ───>[Local DNS Resolver]
       |                                                    |
       |                  (2) Don't know, asking Root ─>[Root Server]
       |                                                    |
       |                  (3) Don't know, ask .com ─────>[TLD .com Server]
       |                                                    |
       |                  (4) Ask example.com ─────>[Authoritative Server]
       |                                                    |
       |                  (5) 93.184.216.34 ←──────────────|
       |                                                    |
       |<─(6) 93.184.216.34 ─────────────────────────────|
       |
       |──(7) HTTP GET http://93.184.216.34/ ──────>[Web Server]
```

**Exam Note:** DNS primarily uses **UDP** (port 53) for queries due to speed. It uses **TCP** (port 53) for zone transfers or large responses.

#### DNS Caching

To prevent redundant queries, DNS servers **cache** responses for a duration specified by **TTL (Time To Live)** — a counter in seconds defining how long a record may stay in cache. Typical TTLs: 300 seconds (5 mins) to 86400 seconds (1 day).

---

### HTTP / HTTPS
*HyperText Transfer Protocol / Secure*

**HTTP (HyperText Transfer Protocol)** is the web content transfer protocol operating at the Application Layer. It uses a request-response model between client (browser) and server.

**HTTPS** (HTTP Secure) is the encrypted version — using **TLS (Transport Layer Security)** for encryption, server authentication, and data integrity. Today, over 95% of web traffic uses HTTPS.

---

## Fiber Optic and Satellite
*Fiber Optic and Satellite*

### Fiber Optic as the Internet Backbone
*Fiber Optic as the Internet Backbone*

**Optical fiber** forms the backbone of the modern Internet. It transmits data as light pulses (lasers) inside an extremely thin glass or plastic fiber.

**Operating Principles:** Light travels inside the fiber due to **total internal reflection** — when light strikes the cladding at an angle smaller than the critical angle, it reflects completely and stays inside the core.

```
  Optical Fiber Structure (Single-mode)
  ───────────────────────────────────────────────────────────────
  ╔══════════════════════════════════════════════════════╗
  ║  Outer Jacket (external protection)                 ║
  ║  ┌──────────────────────────────────────────────┐   ║
  ║  │  Cladding (low refractive index n)           │   ║
  ║  │  ┌──────────────────────────────────────┐   │   ║
  ║  │  │  Core (~9 μm for SMF)                │   │   ║
  ║  │  │  → → → [light pulses (laser)] → →    │   │   ║
  ║  │  └──────────────────────────────────────┘   │   ║
  ║  └──────────────────────────────────────────────┘   ║
  ╚══════════════════════════════════════════════════════╝
```

#### Types of Optical Fiber

| Type | Core Diameter | Light Source | Distance | Application |
|---|---|---|---|---|
| **Single-mode (SMF)** | ~9 μm | Laser | >100 km | Submarine cables, ISP backbone |
| **Multi-mode (MMF)** | ~50-62.5 μm | LED | <2 km | Data centers, intra-building |

**Key Distinction:** SMF (single-mode fiber) has a narrower core so only one light mode travels — eliminating **modal dispersion** and allowing transmission over vastly greater distances without amplification.

#### Submarine Cables: Backbone of Global Communication

**Submarine fiber optic cables** carry approximately **99% of all international Internet traffic**. Without them, the global Internet could not exist in its modern form.

**Characteristics:**
- Capacity of modern cables: hundreds of **Tbps (Terabits per second)**.
- **DWDM (Dense Wavelength Division Multiplexing):** Simultaneous transmission of multiple signals at different wavelengths (colors) in the same fiber — like multiple traffic lanes inside one fiber.
- Depth: up to 8 km below sea level.
- Vulnerabilities: ship anchors, earthquakes, commercial fishing.

---

### Satellite Communication
*Satellite Communication*

Satellites serve as transmission media primarily in regions where terrain makes cable infrastructure impossible (oceans, remote areas, polar zones).

#### Geostationary Satellites (GEO)

**GEO satellites** orbit at an altitude of **~36,000 km** above the Equator. At this altitude, orbital speed matches Earth's rotation exactly — thus the satellite appears **stationary** from the ground, allowing fixed parabolic dish antennas.

```
  Geostationary Satellite (GEO)
  ────────────────────────────────────────────────────────────────
                    [GEO Satellite]
                   ~36,000 km altitude
                  /              \
       [Gateway Station]      [Remote Dish]
             |                      |
         [Internet]            [Home/Ship]

  Round-trip latency: ~500-700 ms
  (Signal: Earth → Sat → Earth → Sat → Earth = ~144,000 km)
```

**GEO Characteristics:**
- Latency: **500-700 ms** RTT (very high).
- Download speed: 25-100+ Mbps.
- Coverage: Just 3 satellites cover nearly the entire Earth.
- Applications: Satellite TV, broadcasting, remote communications.
- **Unsuitable** for: VoIP, online gaming, video conferencing — due to excessive latency.

#### Low Earth Orbit Satellites (LEO)

**LEO satellites** orbit at altitudes of **500-2,000 km**. Due to low orbit, they travel rapidly (period: ~90-120 mins), requiring a large **constellation** of satellites for continuous coverage.

```
  LEO Constellation (e.g. Starlink)
  ────────────────────────────────────────────────────────────────
    [LEO sat 1] ← → [LEO sat 2] ← → [LEO sat 3]
         \               |               /
          \              |              /
     ~550 km altitude    |
          \              |              /
           [Gateway]  [Dish]  [Gateway]
                |
            [Internet]

  Round-trip latency: ~20-50 ms
  (Much shorter light path)
```

**LEO Characteristics:**
- Latency: **20-50 ms** RTT — comparable to terrestrial broadband.
- Download speed: 50-500 Mbps (Starlink).
- Requires hundreds to thousands of satellites (Starlink: ~6,000+ in orbit).
- Applications: Rural broadband, maritime, aviation.

---

### Comparison of Fiber Optic and Satellite

| Characteristic | Optical Fiber (Submarine) | GEO Satellite | LEO Satellite |
|---|---|---|---|
| Latency (RTT) | 10-30 ms | 500-700 ms | 20-50 ms |
| Bandwidth | Millions of Tbps | 25-100 Mbps per user | 50-500 Mbps per user |
| Coverage | At landing points | Nearly global (3 sats) | Global (1000+ sats) |
| Reliability | Extremely high | High | Moderate (handover) |
| Installation cost | Very high | High | High (constellation) |
| Ideal for | Backbone, massive speed | Broadcast, remote | Remote broadband |

**Exam Note:** The main drawback of GEO satellites is **excessive latency** (~500 ms) due to 36,000 km distance. This renders them unsuitable for real-time applications. LEO satellites (Starlink) resolve this with lower orbits but require complex constellation management.

---

## Data Transfer Between Devices
*Data Transfer Between Devices*

### Message Segmentation into Packets
*Message Segmentation into Packets*

On the Internet, data is **not** transmitted as a single large block. Instead, it is segmented into small pieces called **packets** — typically **1,500 bytes** for Ethernet (the **MTU — Maximum Transmission Unit**).

**Why packets instead of one large message?**

1. **Efficient network use:** Multiple conversations share the same link simultaneously (statistical multiplexing).
2. **Easier error handling:** If a packet is lost, only that packet is retransmitted — not the entire message.
3. **Routing flexibility:** Different packets can follow different routes depending on network congestion.

```
  Message Segmentation into Packets
  ────────────────────────────────────────────────────────────────
  Original Message (e.g. 4,500 bytes):
  [═══════════════════════════════════════════]

  After segmentation (MTU = 1,500 bytes):
  Packet 1: [Header | Data (1,460 bytes)]
  Packet 2: [Header | Data (1,460 bytes)]
  Packet 3: [Header | Data (580 bytes)  ]

  Each packet:
  ┌─────────────────────────────────────────────┐
  │ IP Header (20 bytes) │ TCP Header (20 bytes) │ Data (payload) │
  └─────────────────────────────────────────────┘
  Sender IP ─────────────────────────────────────▶ Receiver IP
  Source Port ───────────────────────────────────▶ Destination Port
```

---

### Transfer Delays
*Transfer Delays*

As a packet travels node to node, it experiences four delay types. Their sum constitutes **nodal delay**:

$$d_{nodal} = d_{proc} + d_{queue} + d_{trans} + d_{prop}$$

#### 1. Processing Delay ($d_{proc}$)

Time required for a router to inspect the packet header, check errors, and select the outbound link.

**Value:** Typically < 1 ms in modern routers.

#### 2. Queuing Delay ($d_{queue}$)

Time a packet spends waiting in a router queue (buffer) until the link becomes free for transmission.

**Note:** Queuing delay depends on **traffic intensity**: $ L \cdot a / R $, where $L$ is packet size, $a$ is arrival rate, $R$ is link bandwidth. As this ratio approaches 1, queuing delay approaches infinity.

#### 3. Transmission Delay ($d_{trans}$)

Time required to push all packet bits onto the physical link.

$$d_{trans} = \frac{L}{R}$$

- **$L$:** Packet length in bits.
- **$R$:** Link transmission rate (bandwidth) in bps.

**Example:** 12,000-bit packet on 1 Mbps link: $d_{trans} = 12,000 / 1,000,000 = 0.012 s = 12 ms$.

#### 4. Propagation Delay ($d_{prop}$)

Time required for a bit to physically travel from sender to receiver across the physical medium.

$$d_{prop} = \frac{d}{s}$$

- **$d$:** Physical distance between nodes.
- **$s$:** Signal propagation speed in medium (≈ $2 \times 10^8$ m/s in copper/fiber, ~2/3 speed of light).

**Exam Note:** Do not confuse $d_{trans}$ and $d_{prop}$. Transmission delay depends on **packet size and bandwidth**. Propagation delay depends on **distance** between nodes.

---

### Worked Numerical Example
*Worked Numerical Example*

**Scenario:** A 750,000-byte file is sent from node A to node C, via intermediate router B (2 hops). Each link has:
- Bandwidth: $R = 1.5 \text{ Mbps} = 1.5 \times 10^6 \text{ bps}$
- Distance: $d = 300 \text{ km} = 3 \times 10^5 \text{ m}$
- Propagation speed: $s = 2 \times 10^8 \text{ m/s}$

Ignore queuing delay and processing delay.

**Step 1: Calculate file size in bits:**

$$L = 750,000 \times 8 = 6 \times 10^6 \text{ bits}$$

**Step 2: Transmission delay per hop:**

$$d_{trans} = \frac{L}{R} = \frac{6 \times 10^6}{1.5 \times 10^6} = 4 \text{ sec}$$

**Step 3: Propagation delay per hop:**

$$d_{prop} = \frac{d}{s} = \frac{3 \times 10^5}{2 \times 10^8} = 1.5 \times 10^{-3} \text{ s} = 1.5 \text{ ms}$$

**Step 4: Store-and-Forward End-to-End Delay:**

In store-and-forward packet switching, router B must receive the **entire** packet before forwarding it:

$$d_{end-to-end} = N \cdot d_{trans} + N \cdot d_{prop}$$

For $N = 2$ hops (A→B, B→C):

$$d_{end-to-end} = 2 \times 4 + 2 \times 0.0015 = 8 + 0.003 \approx 8.003 \text{ sec}$$

---

### Data Encapsulation
*Data Encapsulation*

During data transfer, each layer of the TCP/IP stack **appends** its own header to data — this process is called **encapsulation**. At the receiver, each layer **strips** its header (de-encapsulation).

```
  Encapsulation: Sender (Moving down the stack)
  ──────────────────────────────────────────────────────────────
  Application:   [   DATA   ]
                      ↓  + Application Header (HTTP)
  Transport:     [TCP HDR | DATA           ]
                      ↓  + TCP Header
  Internet:      [IP HDR | TCP HDR | DATA  ]
                      ↓  + IP Header
  Network Access:[ETH HDR | IP HDR | TCP HDR | DATA | ETH TRAIL]
                      ↓
                   Physical Medium (bits)

  PDU Names per Layer:
  Application:  Message
  Transport:    Segment (TCP) / Datagram (UDP)
  Internet:     Datagram (or packet)
  Network Acc.: Frame
  Physical:     Bits
```

---

## Summary Table

| Concept | Definition | Key Characteristic |
|---|---|---|
| **Router** | Packet routing device between networks | Layer 3, uses IP addresses |
| **Switch** | Device connecting nodes within LAN | Layer 2, uses MAC addresses |
| **Modem** | Digital/analog signal converter | Bridge between LAN and ISP line |
| **NIC** | Network Interface Card | Provides physical connectivity |
| **IP (Internet Protocol)** | Routing protocol — Internet Layer | Connectionless, best-effort |
| **IPv4** | 32-bit addresses (~4.3B) | Exhausted, uses NAT |
| **IPv6** | 128-bit addresses | Practically unlimited |
| **TCP** | Reliable, connection-oriented protocol | 3-way handshake, flow control |
| **UDP** | Connectionless, unreliable protocol | Faster, streaming/DNS/gaming |
| **DNS** | Domain name to IP translation | Internet "phonebook" |
| **HTTP/HTTPS** | Web content transfer protocol | HTTPS = HTTP + TLS encryption |
| **Single-mode Fiber** | Fiber, ~9 μm core, laser | Tbps, hundreds of km without repeaters |
| **Multi-mode Fiber** | Fiber, ~50 μm core, LED | Short distance (<2 km), data centers |
| **GEO Satellite** | Orbit ~36,000 km, stationary | Latency 500-700 ms, global coverage (3 sats) |
| **LEO Satellite** | Orbit 500-2,000 km, constellation | Latency 20-50 ms, requires many satellites |
| **Transmission Delay** | $d_{trans} = L/R$ | Depends on packet size + bandwidth |
| **Propagation Delay** | $d_{prop} = d/s$ | Depends on distance + medium |
| **Encapsulation** | Header addition at each TCP/IP layer | PDU: Message → Segment → Datagram → Frame → Bits |
| **MTU** | Maximum Transmission Unit, 1,500 bytes (Ethernet) | Max packet size on Ethernet |
| **DWDM** | Dense Wavelength Division Multiplexing | Multiple signals in single optical fiber |

---

## Key Takeaways

- The Internet comprises **three complementary layers**: physical infrastructure (hardware/cables), communication protocols (TCP/IP, DNS), and data transfer mechanisms (packet switching).
- A **router** operates at Layer 3 (IP) interconnecting **different** networks. A **switch** operates at Layer 2 (MAC) connecting devices **within** a network.
- **TCP/IP** is the 4-layer protocol stack (Application, Transport, Internet, Network Access) defining Internet operations.
- **TCP** provides reliable communication (3-way handshake, flow/congestion control). **UDP** is faster but offers no delivery guarantees.
- **DNS** translates human-readable domain names into IP addresses, operating hierarchically: Root → TLD → Authoritative.
- **Single-mode optical fiber** (SMF) with DWDM technology forms the Internet backbone — transporting **99%** of international traffic.
- **GEO satellites** (~36,000 km) provide global coverage with just three satellites, but have unacceptable latency (~600 ms) for real-time applications. **LEO satellites** (500-2,000 km) resolve this with latency ~20-50 ms.
- **Transmission delay** ($d_{trans} = L/R$) depends on packet size and bandwidth. **Propagation delay** ($d_{prop} = d/s$) depends on distance.
- In **store-and-forward** packet switching, a router must receive an **entire** packet before forwarding it — adding $d_{trans}$ delay per hop.
- **IPv4** (32-bit) address space is exhausted. **IPv6** (128-bit) provides virtually unlimited addresses for future expansion.
