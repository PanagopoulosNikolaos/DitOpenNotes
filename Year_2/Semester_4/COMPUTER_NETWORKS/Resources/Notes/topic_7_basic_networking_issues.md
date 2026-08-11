# Basic Issues in Networking
*Basic Issues in Networking*

---

## Table of Contents

- [Introduction](#introduction)
- [Addresses and Names](#addresses-and-names)
  - [Physical Addresses (MAC Addresses)](#physical-addresses-mac-addresses)
  - [Logical Addresses (IP Addresses)](#logical-addresses-ip-addresses)
  - [System Names (Hostnames) and DNS](#system-names-hostnames-and-dns)
  - [Address Resolution Protocol (ARP)](#address-resolution-protocol-arp)
- [Routing](#routing)
  - [Routing vs Forwarding](#routing-vs-forwarding)
  - [Link-State Algorithms](#link-state-algorithms)
  - [Distance-Vector Algorithms](#distance-vector-algorithms)
  - [Hierarchical Routing Architecture (Autonomous Systems)](#hierarchical-routing-architecture-autonomous-systems)
  - [Worked Numerical Example: Dijkstra's Algorithm](#worked-numerical-example-dijkstras-algorithm)
- [Error Detection](#error-detection)
  - [Parity Checking](#parity-checking)
  - [Hamming Code](#hamming-code)
  - [Internet Checksum](#internet-checksum)
  - [Cyclic Redundancy Check (CRC)](#cyclic-redundancy-check-crc)
  - [Worked Numerical Example: CRC Calculation](#worked-numerical-example-crc-calculation)
- [Security and Cryptography](#security-and-cryptography)
  - [Symmetric-Key Cryptography](#symmetric-key-cryptography)
  - [Public-Key Cryptography](#public-key-cryptography)
  - [Digital Signatures & Certificates](#digital-signatures--certificates)
  - [Security Protocols (SSL/TLS, IPsec)](#security-protocols-ssltls-ipsec)
- [Summary Table](#summary-table)
- [Key Takeaways](#key-takeaways)

---

## Introduction

The operation of modern computer networks rests on solving four fundamental challenges: identifying devices, discovering optimal data transmission paths, ensuring data integrity, and protecting communication against malicious interference. These **basic issues** cut horizontally across all protocol stack layers. Mastering them enables network engineers to understand how the Internet scales globally while remaining reliable and secure despite physical transmission media noise and constant security threats.

---

## Addresses and Names
*Addresses and Names*

In a global network, every entity (host, router, interface) requires an identity. Identification operates across three abstraction layers: physical addressing, logical addressing, and human-readable hostnames.

```
  Relationship & Mapping of Addresses & Names
  ──────────────────────────────────────────────────────────────────────────
  [Application Layer]       Hostname (e.g., www.uoa.gr)
         │
         │ (DNS Resolution)
         ▼
  [Network Layer]           IP Address (Logical) (e.g., 195.134.100.2)
         │
         │ (ARP Resolution within local subnet)
         ▼
  [Data Link Layer]         MAC Address (Physical) (e.g., 00:1A:2B:3C:4D:5E)
```

### Physical Addresses (MAC Addresses)

A **MAC (Media Access Control) Address** is a physical address uniquely identifying a Network Interface Card (NIC).
- **Properties**: 48 bits (6 bytes) long, represented in hexadecimal notation (`00:1A:2B:3C:4D:5E`). Burned into device hardware during manufacturing.
- **Structure**: Flat address space. The first 24 bits comprise the **OUI (Organizationally Unique Identifier)** identifying the manufacturer; the remaining 24 bits represent the card's unique serial number.
- **Function**: Operates at the Data Link Layer (Layer 2) to transfer frames between devices residing on the **same local area network (LAN/subnet)**.

---

### Logical Addresses (IP Addresses)

An **IP (Internet Protocol) Address** is a logical address assigned dynamically or statically to a host when connecting to a network.
- **Properties**: IPv4 addresses are 32 bits (4 bytes) long, written in dotted-decimal notation (`192.168.1.1`). IPv6 addresses are 128 bits long, written in 8 groups of hexadecimal digits separated by colons.
- **Structure**: Hierarchical address space comprising a **Network Prefix** (identifying the destination network) and a **Host Identifier** (identifying the specific host within that network).
- **Function**: Operates at the Network Layer (Layer 3) for global packet routing across disparate networks worldwide.

---

### System Names (Hostnames) and DNS

**Hostnames / Domain Names** are human-readable alphanumeric strings (`www.example.com`) used at the Application Layer.

Because routers process numerical IP addresses, translation is mandatory. The **DNS (Domain Name System)** performs this role:
- **Definition**: A distributed, hierarchical database and application-layer protocol resolving hostnames into IP addresses.
- **Hierarchy**: Root DNS Servers $\to$ Top-Level Domain (TLD) DNS Servers (`.com`, `.gr`) $\to$ Authoritative DNS Servers $\to$ Local DNS Resolvers.

#### DNS Query-Response Sequence

```
  Client (Resolver)                      Local DNS Server             Authoritative Server
         │                                      │                               │
         ├────── DNS Query (UDP Port 53) ──────►│                               │
         │       "What is IP for                │                               │
         │        www.example.com?"             ├────── DNS Query ─────────────►│
         │                                      │       "What is IP for         │
         │                                      │        www.example.com?"      │
         │                                      │                               │
         │                                      │◄───── DNS Response ───────────┤
         │                                      │       "IP: 192.0.2.1"         │
         │◄───── DNS Response ──────────────────┤                               │
         │       "IP: 192.0.2.1"                │                               │
```

---

### Address Resolution Protocol (ARP)

When a packet arrives at the destination local subnet, the sender knows the destination IP address but lacks its MAC address, which is required to construct the Ethernet frame.
- **Definition**: **ARP (Address Resolution Protocol)** resolves a known IP address to its corresponding physical MAC address within the same subnet.
- **Function**:
  1. The sender broadcasts an **ARP Request** (`FF:FF:FF:FF:FF:FF`) asking: *"Who has IP X? Send me your MAC."*
  2. The target host holding IP X returns a unicast **ARP Reply**: *"I have IP X; my MAC is Y."*
  3. The sender caches the IP-to-MAC mapping in its **ARP Cache**.

#### Address and Name Comparison

| Feature | MAC Address | IP Address | Hostname / Domain Name |
|---|---|---|---|
| **OSI Layer** | Data Link Layer (Layer 2) | Network Layer (Layer 3) | Application Layer (Layer 7) |
| **Format / Size** | 48 bits (Hexadecimal) | 32 bits (IPv4) / 128 bits (IPv6) | Variable length alphanumeric string |
| **Structure** | Flat (OUI + Serial) | Hierarchical (Network ID + Host ID) | Hierarchical (Root, TLD, Domain) |
| **Assignment** | Permanent (Burned-in) | Dynamic (DHCP) or Static | Registered via Domain Registrar |
| **Scope** | Local Subnet | Globally Routable | Global (via DNS) |

---

## Routing
*Routing*

Routing is the primary Layer 3 function determining end-to-end paths across complex meshes of interconnected routers.

### Routing vs Forwarding

- **Routing**: Determining the **end-to-end path** packets follow from source to destination. Executes in the **Control Plane** via routing algorithms.
- **Forwarding**: The local action of transferring a packet from a router's **input interface** to the appropriate **output interface**. Executes in the **Data Plane** in hardware (nanoseconds) based on the forwarding table.

```
  Router Architecture: Routing vs Forwarding
  ──────────────────────────────────────────────────────────────────────────
       [ Routing Algorithm ] (Control Plane - software routing math)
                │
                ▼ (Installs entries)
       ┌────────────────────────┐
       │   Forwarding Table     │
       └────────────────────────┘
                │
  [Input Port] ─┼───────────────► [Output Port] (Data Plane - hardware switching)
```

---

### Link-State Algorithms

- **Mechanism**: Every router collects information about its directly connected links and broadcasts these link states to all routers in the network via **Link-State Advertisements (LSAs)**.
- **Result**: All routers construct identical topology maps of the network.
- **Computation**: Each router independently runs **Dijkstra's Algorithm** to compute the shortest path tree rooted at itself.
- **Protocol**: **OSPF (Open Shortest Path First)** is the dominant link-state protocol.

---

### Distance-Vector Algorithms

- **Mechanism**: Routers maintain vectors of estimated distances to all destinations, knowing only immediate neighbors.
- **Computation**: Neighbors periodically exchange distance vectors. Routers update estimates using the **Bellman-Ford equation**:
  $$D_x(y) = \min_v \{ c(x,v) + D_v(y) \}$$
- **Issues**: Slow convergence, count-to-infinity problem (mitigated via split horizon and poison reverse).
- **Protocol**: **RIP (Routing Information Protocol)**.

---

### Hierarchical Routing Architecture (Autonomous Systems)

Internet routing is organized hierarchically into **Autonomous Systems (AS)**:
- **Autonomous System (AS)**: A group of routers under common administrative control.
- **Intra-AS Routing (IGP)**: Routing within an AS prioritizing performance (OSPF, RIP).
- **Inter-AS Routing (EGP)**: Routing between ASes prioritizing policies and business agreements (**BGP**).

---

### Worked Numerical Example: Dijkstra's Algorithm

**Network Topology Costs:**
- $u \to v: 2$, $u \to x: 1$
- $x \to v: 2$, $x \to y: 1$
- $v \to w: 3$, $v \to y: 3$
- $y \to w: 1$, $y \to z: 2$
- $w \to z: 5$

**Source Node:** $u$

```
          2           3
     u ──────── v ──────── w
     │        ╱ │        ╱ │
   1 │      ╱   │      ╱   │ 5
     │    ╱ 2   │ 3  ╱ 1   │
     │  ╱       │  ╱       │
     x ──────── y ──────── z
          1           2
```

#### Step-by-Step Dijkstra Execution Table:

| Step | $N'$ | $D(v), p(v)$ | $D(w), p(w)$ | $D(x), p(x)$ | $D(y), p(y)$ | $D(z), p(z)$ |
|:---:|---|:---:|:---:|:---:|:---:|:---:|
| Initial | $\{u\}$ | $2, u$ | $\infty$ | $1, u$ | $\infty$ | $\infty$ |
| 1 | $\{u, x\}$ | $2, u$ | $\infty$ | | $2, x$ | $\infty$ |
| 2 | $\{u, x, v\}$ | | $5, v$ | | $2, x$ | $\infty$ |
| 3 | $\{u, x, v, y\}$ | | $3, y$ | | | $4, y$ |
| 4 | $\{u, x, v, y, w\}$ | | | | | $4, y$ |
| 5 | $\{u, x, v, y, w, z\}$ | | | | | |

**Result**: The shortest path from $u$ to $z$ has a total cost of **$4$**: path **$u \to x \to y \to z$**.

---

## Error Detection
*Error Detection*

Transmission over noisy physical media can invert bits ($0 \to 1$ or $1 \to 0$). Error detection allows receivers to identify corrupted frames and drop or request retransmission.

---

### Parity Checking

- **Single Parity Bit**: Appends 1 bit to data. In **even parity**, the total number of 1s in the frame is made even; in **odd parity**, odd. Detects single-bit errors (or odd numbers of bit errors).
- **Two-Dimensional Parity**: Arranges data into rows and columns, calculating parity per row and column. Can detect and **correct** single-bit errors (Forward Error Correction - FEC).

---

### Hamming Code

**Hamming Code** is a Forward Error Correction scheme that detects and corrects single-bit errors by placing parity bits at power-of-two positions ($1, 2, 4, 8 \dots$).

**Example (Odd Parity for Data `1110`):**
Data bits placed at non-power-of-two positions: `[P1] [P2] [1] [P4] [1] [1] [0]`.
- **P1** checks positions 1, 3, 5, 7 (`P1`, `1`, `1`, `0`): Requires odd number of 1s $\to$ **P1 = 1**.
- **P2** checks positions 2, 3, 6, 7 (`P2`, `1`, `1`, `0`) $\to$ **P2 = 1**.
- **P4** checks positions 4, 5, 6, 7 (`P4`, `1`, `1`, `0`) $\to$ **P4 = 1**.

Transmitted Hamming Codeword: **`1 1 1 1 1 1 0`**.

---

### Internet Checksum

Used in IP, TCP, and UDP protocols.
1. Data split into 16-bit integers.
2. Summed using **1s complement arithmetic** (end-around carry added back to LSB).
3. Bitwise NOT applied to sum to generate checksum.
4. Receiver adds 16-bit words including checksum; result must be all 1s (`1111111111111111`).

---

### Cyclic Redundancy Check (CRC)

**CRC** uses polynomial division in Galois Field arithmetic (XOR operations) implemented in hardware shift registers.

#### Mechanism:
1. Sender and receiver agree on a **generator polynomial $G$** of length $r+1$ bits.
2. Sender appends $r$ zeros to data $D$ ($D \cdot 2^r$).
3. Performs modulo-2 division of $D \cdot 2^r$ by $G$.
4. The remainder $R$ ($r$ bits) is appended to data: Transmitted frame $T = D \cdot 2^r \oplus R$.
5. Receiver divides $T$ by $G$. Zero remainder indicates no errors.

---

### Worked Numerical Example: CRC Calculation

Data $D = 101001$, Generator $G = 1101$ ($r = 3$).

1. **Appended Data:** $D \cdot 2^3 = 101001000$
2. **Modulo-2 Division ($101001000 \div 1101$ using XOR):**

```
             101101  (Quotient)
      ───────┐─────────────────
 1101 │ 101001000
        1101
        ─────
        01110
         1101
         ────
         00111
          0000
          ────
          01110
           1101
           ────
           00110
            1101
            ────
            0101
            0000
            ────
             011  (Remainder R = 011)
```

3. **Transmitted Codeword:** $T = 101001011$
4. **Receiver Verification:** $101001011 \div 1101$ yields remainder **`000`** $\to$ Data accepted cleanly.

---

## Security and Cryptography
*Security and Cryptography*

Network security enforces **Confidentiality**, **Integrity**, **Authentication**, and **Non-repudiation**.

---

### Symmetric-Key Cryptography

Sender and receiver share a **single secret key ($K$)** for encryption and decryption.
- Encryption: $C = E_K(M)$
- Decryption: $M = D_K(C)$
- **Pros:** Fast and efficient (e.g. **AES**, DES).
- **Cons:** Key distribution challenge across untrusted channels.

---

### Public-Key Cryptography

Uses asymmetric **key pairs**: **Public Key ($K^+$)** (shared freely) and **Private Key ($K^-$)** (kept secret).
- Sender encrypts message with receiver's Public Key: $C = E_{K_B^+}(M)$.
- Receiver decrypts using private key: $M = D_{K_B^-}(C)$.
- **Pros:** Solves key distribution.
- **Cons:** Computationally expensive (e.g. **RSA**, ECC).
- **Hybrid Systems:** Asymmetric encryption securely exchanges a temporary symmetric **session key**, which encrypts payload data via AES.

---

### Digital Signatures & Certificates

#### Digital Signatures
Ensures integrity, authentication, and non-repudiation.
1. Sender hashes message $M$ using SHA-256 to produce digest $H(M)$.
2. Sender encrypts digest with private key ($K^-$): $\text{Sig} = E_{K_A^-}(H(M))$.
3. Receiver decrypts signature with sender's public key ($K_A^+$) and compares computed digest.

#### Digital Certificates
A **Digital Certificate** binds a public key to an entity identity, digitally signed by a trusted **Certificate Authority (CA)**.

---

### Security Protocols (SSL/TLS, IPsec)

- **TLS (Transport Layer Security)**: Secures transport connections (HTTPS port 443) via TLS Handshake (certificate verification and session key exchange) and Record Protocol (symmetric encryption).
- **IPsec**: Secures Layer 3 IP traffic for Virtual Private Networks (VPNs).

---

## Summary Table

| Concept | Definition | Key Feature |
|---|---|---|
| **MAC Address** | 48-bit physical hardware identifier | Layer 2 local subnet delivery |
| **IP Address** | 32-bit (v4) / 128-bit (v6) logical address | Layer 3 global routing |
| **DNS** | Distributed domain naming system | Resolves hostnames to IP addresses |
| **ARP** | Address resolution protocol | Maps IP addresses to MAC addresses via broadcast |
| **Routing** | Computing end-to-end network paths | Control plane software operation |
| **Forwarding** | Local packet switching from input to output | Data plane hardware operation |
| **Parity Check** | Single bit error check | Detects odd number of bit errors |
| **Checksum** | 1s complement sum of 16-bit words | Used in IP, TCP, UDP transport headers |
| **CRC** | Polynomial division error detection | Hardware-accelerated, robust against burst errors |
| **Symmetric Encryption** | Single shared secret key (AES) | High speed payload encryption |
| **Public-Key Encryption** | Key pair (RSA/ECC) | Solves key exchange |
| **TLS/SSL** | Transport layer security protocol | Hybrid encryption powering HTTPS |

---

## Key Takeaways

- **Layered Identification**: MAC addresses serve Layer 2 local delivery, IP addresses handle Layer 3 global routing, and Hostnames provide human-readable names; ARP and DNS bridge these layers.
- **Control vs Data Plane**: Routing algorithms run in software within the control plane, while forwarding executes instantly in data plane hardware.
- **Link-State vs Distance-Vector**: OSPF (Link-State) floods local link info to all nodes for global topology maps; RIP (Distance-Vector) exchanges full distance tables only with neighbors.
- **CRC Hardware Strength**: CRC polynomial division reliably catches error bursts over physical media.
- **Hybrid Cryptography**: Modern security protocols (TLS) combine public-key cryptography for initial handshake key exchange with symmetric-key cryptography for payload encryption.
