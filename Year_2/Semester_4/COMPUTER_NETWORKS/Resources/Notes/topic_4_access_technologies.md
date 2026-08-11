# Access Technologies
*Access Technologies*

---

## Table of Contents

- [Introduction](#introduction)
- [Residential Access Networks](#residential-access-networks)
  - [DSL (Asymmetric / Symmetric)](#dsl-asymmetric--symmetric)
  - [HFC / Cable (Coaxial & Fiber)](#hfc--cable-coaxial--fiber)
  - [FTTH](#ftth)
- [Enterprise / Institutional Access Networks](#enterprise--institutional-access-networks)
  - [Ethernet](#ethernet)
- [Mobile / Wireless Access Networks](#mobile--wireless-access-networks)
  - [Wi-Fi](#wi-fi)
  - [4G / 5G](#4g--5g)
- [Worked Numerical Example](#worked-numerical-example)
- [Summary Table](#summary-table)
- [Key Takeaways](#key-takeaways)

---

## Introduction

**Access technologies** form the bridge connecting end systems (computers, smartphones, servers) to the ISP's edge router, injecting data into the Internet Network Core. This addresses the "last-mile problem": delivering high-speed connectivity from the Internet backbone to the end user's home, office, or mobile device. Different user categories (residential, enterprise, mobile) have distinct requirements for speed, cost, and mobility, giving rise to diverse technologies. Understanding access technologies is essential, as they link physical transmission media with the network architecture discussed in previous topics.

---

## Residential Access Networks
*Residential Access Networks*

Residential access networks deliver broadband connectivity to home users at low infrastructure deployment costs. The three dominant technologies are DSL, HFC/Cable, and FTTH, each defined by distinct physical media, architecture, and performance characteristics.

```
  Residential Access Network Architecture
  ─────────────────────────────────────────────────────────────────────
                          [ISP / Edge Router]
                                  |
              ┌───────────────────┼───────────────────┐
              |                   |                   |
         [DSL CO / DSLAM]    [Cable Headend]     [OLT - FTTH]
              |                   |                   |
         [DSL Modem]          [Cable Modem]       [ONT]
              |                   |                   |
         [Home Router]        [Home Router]       [Home Router]
          /   |   \            /   |   \            /   |   \
      [PC] [TV] [Phone]   [PC] [TV] [Phone]   [PC] [TV] [Phone]
```

---

### DSL (Asymmetric / Symmetric)
*Digital Subscriber Line*

#### What is DSL

**DSL (Digital Subscriber Line)** transmits digital data over **existing copper telephone lines**. Its primary advantage is leveraging legacy telephone infrastructure without requiring new wiring. Transmission occurs at **higher frequencies** than human voice (0–4 kHz), allowing **simultaneous** voice calls and Internet access over the same wire pair.

**Analogy:** A telephone line is like a road originally built for cars (voice). DSL opens extra lanes for cargo trucks (data) on the same road without disrupting car traffic.

#### DSL Architecture

```
  DSL Architecture
  ─────────────────────────────────────────────────────────────────────────
  [Home]                            [CO: Central Office]          [ISP]
     |                                      |                        |
  [DSL Modem] ──────── copper ────────► [DSLAM] ──── optical fiber ─► [Router]
     |          (telephone line)       (DSL Access                   |
  [Splitter]    0-4kHz: voice           Multiplexer)              [Internet]
   /       \    25kHz+: data
 [POTS]  [Router]
 (Phone) (LAN)
```

- **DSLAM (DSL Access Multiplexer):** Located at the ISP **Central Office (CO)**. Aggregates hundreds of subscriber DSL lines onto a single high-speed fiber link to the edge router.
- **Splitter:** Passive splitter separating copper signals into two frequency bands:
  - **Voice (POTS):** 0–4 kHz → connected to the telephone.
  - **Data:** 25 kHz and above → connected to the DSL modem.

#### DMT Modulation and Spectrum Use

DSL uses **DMT (Discrete Multitone Modulation)** — dividing spectrum into 256 subchannels of 4.3 kHz each. QAM modulation is applied per subchannel. Subchannels with high Signal-to-Noise Ratios (SNR) carry more bits, while degraded subchannels are disabled.

```
  ADSL2+ Frequency Spectrum Allocation
  ─────────────────────────────────────────────────────────────────────
  Frequency (kHz):
  0──4    25──138          138────────────────────────2208
  ├─────┤├─────────────────┤├────────────────────────────────────────┤
  │Voice││    Upstream     ││              Downstream                │
  │(POTS)│   (upload)      ││              (download)                │
  └──────┘└────────────────┘└────────────────────────────────────────┘
  Upstream bandwidth << Downstream bandwidth → Asymmetry!
```

#### DSL Types: Asymmetric and Symmetric

- **Asymmetric DSL (ADSL):** **Download** speed is substantially **faster** than **upload**. Designed intentionally for residential users who consume far more data than they generate.
- **Symmetric DSL (SDSL):** Provides **equal** download and upload speeds, preferred by businesses (VoIP, cloud backups, video conferencing).

| Technology | Standard | Download | Upload | Characteristics |
|---|---|---|---|---|
| **ADSL** | ITU-T G.992.1 | 1–8 Mbps | 0.5–1 Mbps | Pure copper, legacy |
| **ADSL2+** | ITU-T G.992.5 | Up to 24 Mbps | Up to 3.5 Mbps | Wider spectrum (2.2 MHz) |
| **VDSL** | ITU-T G.993.1 | 30–52 Mbps | 10–26 Mbps | Short copper loop, FTTC |
| **VDSL2** | ITU-T G.993.2 | Up to 100 Mbps | Up to 50 Mbps | Vectoring, FTTC/FTTB |
| **G.fast** | ITU-T G.9700 | Up to 1 Gbps | High | Ultra-short copper (<250 m) |
| **SDSL** | — | Equal | Equal | Symmetric, business-grade |

#### Distance Limitation

**Exam Note:** DSL performance degrades sharply with distance from the CO:

$$\text{Attenuation (dB)} \propto \sqrt{f} \cdot d$$

Where $f$ is frequency and $d$ is distance. VDSL requires short copper loops using **FTTC (Fiber to the Cabinet)** — optical fiber runs to street cabinets, leaving only the final meters to copper.

```
  ADSL vs VDSL2: Speed Degradation over Distance
  ─────────────────────────────────────────────────────────────────────
  Download Speed (Mbps)
  100 |                    ●──VDSL2 (start)
      |                   /
   52 |                  /
      |                 /
   24 |────────────────●──ADSL2+ (start)
      |               / \
    8 |──────────────●   \──VDSL2 (500m)
      |             /     \
    2 |────────────●────────●──ADSL2+ (2km)   ●──VDSL2 (1.5km)
      |──────────────────────────────────────────────────────────
      0          500m        1km        2km        3km    Distance from CO
```

---

### HFC / Cable (Coaxial & Fiber)
*Hybrid Fiber-Coaxial*

#### What is HFC

**HFC (Hybrid Fiber-Coaxial)** is the broadband technology used by cable TV operators. "Hybrid" indicates the network uses **optical fiber** for high-capacity trunk lines (headend to neighborhood node) and **coaxial cable** for last-mile delivery (node to homes).

```
  HFC Architecture
  ───────────────────────────────────────────────────────────────────────────
  [Cable Headend]
       |
  [CMTS]  ← Cable Modem Termination System
       |
  [Optical Fiber] ← High-capacity backbone
       |
  [HFC Node] ← Optical to RF (coaxial) conversion
       |
  ┌────┴────────────────────────────────────────────┐
  | Shared Coaxial Cable                           |
  |                                                  |
  [Home 1]   [Home 2]   [Home 3]   ...   [Home N]
  [Cable     [Cable     [Cable           (500-2000 homes
   Modem]     Modem]     Modem]           per coax segment)
```

- **Headend:** Central facility housing the **CMTS (Cable Modem Termination System)** — managing subscriber cable modems.
- **HFC Node:** Converts optical signals to RF signals over coaxial cable and vice versa. Each node serves **500–2,000 homes**.

#### DOCSIS Protocol

Data over HFC is governed by **DOCSIS (Data Over Cable Service Interface Specification)**:

| Version | Download | Upload | Modulation Technology |
|---|---|---|---|
| **DOCSIS 3.0** | ~1 Gbps (bonded) | ~200 Mbps | 256-QAM, Channel Bonding |
| **DOCSIS 3.1** | Up to 10 Gbps | Up to 2 Gbps | OFDM, 4096-QAM |
| **DOCSIS 4.0** | Up to 10 Gbps | Up to 6 Gbps | Full Duplex / Extended Spectrum |

**Key Distinction — Shared Medium:** Unlike DSL's dedicated copper pairs, HFC coaxial segments are **shared media**. Users in the same neighborhood share total segment bandwidth:

```
  DSL (Dedicated) vs HFC (Shared)
  ─────────────────────────────────────────────────────────────────────
  DSL:
  [User A] ──────── Dedicated Line ──────── [DSLAM]
  [User B] ──────── Dedicated Line ──────── [DSLAM]
  [User C] ──────── Dedicated Line ──────── [DSLAM]
  → Guaranteed individual line capacity

  HFC:
  [User A] ─┐
  [User B] ─┤── Shared Coax ──── [HFC Node] ── Fiber ──[Headend]
  [User C] ─┘
  → Shared bandwidth: peak hours reduce per-user throughput
```

**Exam Note:** During peak usage hours (evenings), effective HFC speeds may decrease because neighborhood coaxial bandwidth is shared. DSL dedicated loops are unaffected by neighbor traffic.

---

### FTTH
*Fiber to the Home*

#### What is FTTH

**FTTH (Fiber to the Home)** extends **optical fiber** directly into subscriber residences, eliminating copper or coaxial segments. An **ONT (Optical Network Terminal)** converts optical signals to Ethernet inside or outside the premises. FTTH represents the fastest, most future-proof residential access solution.

#### PON Architecture (Passive Optical Network)

FTTH predominantly uses **PON (Passive Optical Network)** architecture, employing **passive optical splitters** to distribute light signals from an OLT port to multiple subscribers without active electronics in the field.

```
  FTTH / PON Architecture (1:4 Splitter Example)
  ─────────────────────────────────────────────────────────────────────────
  [ISP Central Office]
         |
  [OLT] ← Optical Line Terminal
         |
  [Fiber Backbone]
         |
  [Passive Optical Splitter] ← 1:32 or 1:64 ratio
   /    |    |    \
  /     |    |     \
[ONT] [ONT] [ONT] [ONT]   ← Optical Network Terminal per home
  |     |     |     |
[Home1][Home2][Home3][Home4]
```

- **OLT (Optical Line Terminal):** Located at the ISP Central Office, controlling PON data traffic and assigning upstream TDMA time slots to ONTs.
- **Passive Optical Splitter:** Unpowered optical device splitting light into 32 or 64 subscriber strands.
- **ONT (Optical Network Terminal):** Home unit converting optical signals into electrical Ethernet frames.

#### PON Standards and Speeds

| Standard | ITU-T Standard | Download | Upload | Symmetry |
|---|---|---|---|---|
| **GPON** | G.984 | 2.5 Gbps | 1.25 Gbps | Asymmetric |
| **XG-PON** | G.987 | 10 Gbps | 2.5 Gbps | Asymmetric |
| **XGS-PON** | G.9807 | 10 Gbps | 10 Gbps | **Symmetric** |
| **25G-PON** | In development | 25 Gbps | 25 Gbps | Symmetric |

**Exam Note:** **FTTH/XGS-PON** is the only mainstream residential technology providing fully **symmetric** 10 Gbps speeds.

#### Residential Access Technology Comparison

| Feature | DSL (ADSL2+) | DSL (VDSL2) | HFC (DOCSIS 3.1) | FTTH (XGS-PON) |
|---|---|---|---|---|
| **Physical Medium** | Copper | Copper + Fiber (FTTC) | Fiber + Coaxial | Optical Fiber |
| **Max Download** | ~24 Mbps | ~100 Mbps | ~10 Gbps | ~10 Gbps |
| **Max Upload** | ~3.5 Mbps | ~50 Mbps | ~2 Gbps | ~10 Gbps |
| **Symmetry** | Asymmetric | Asymmetric | Asymmetric | **Symmetric** |
| **Shared Medium?** | No (dedicated) | No (dedicated) | **Yes** (shared coax) | Yes (PON splitter) |
| **Distance Impact** | High | High | Minimal | Minimal |
| **Deployment Cost** | Low | Moderate | Moderate | High (initial) |

---

## Enterprise / Institutional Access Networks
*Enterprise / Institutional Access Networks*

Enterprise and institutional networks (offices, universities, data centers) mandate far higher bandwidth, lower latency, superior reliability, and robust security compared to residential networks. **Ethernet** is the dominant access technology in these environments.

---

### Ethernet
*IEEE 802.3*

#### What is Ethernet

**Ethernet** (IEEE 802.3) is the ubiquitous wired LAN technology operating at OSI **Layer 1 (Physical)** and **Layer 2 (Data Link)**. In enterprise settings, Ethernet serves as the campus backbone connecting hosts, servers, and switches prior to edge router connectivity.

#### Enterprise Network Architecture

```
  Typical Enterprise / Campus Network Architecture
  ─────────────────────────────────────────────────────────────────────
  [Internet / ISP]
         |
  [Edge Router / Firewall]
         |
  [Core Switch] (Layer 3, 10-100 Gbps)
   /       |       \
[Distribution  [Distribution  [Distribution
 Switch]        Switch]        Switch]
(Layer 3,      (Layer 3,      (Layer 3,
 1-10 Gbps)     1-10 Gbps)     1-10 Gbps)
  /   \           /   \           /   \
[Access] [Access] [Access] [Access] [Access] [Access]
[Switch] [Switch] [Switch] [Switch] [Switch] [Switch]
(L2, 1Gbps)
  / | \
[PC][PC][PC]  ← End systems (1 Gbps links)
```

This 3-tier hierarchical architecture (Core – Distribution – Access) is the enterprise design standard.

#### Ethernet Speed Evolution

| Generation | Standard | Speed | Medium | Typical Application |
|---|---|---|---|---|
| **Ethernet** | IEEE 802.3 | 10 Mbps | Coaxial / UTP | Legacy LANs |
| **Fast Ethernet** | IEEE 802.3u | 100 Mbps | Cat 5 UTP | Access layer |
| **Gigabit Ethernet** | IEEE 802.3ab/z | 1 Gbps | Cat 5e/6 / Fiber | Desktop access / uplinks |
| **10GbE** | IEEE 802.3ae/an | 10 Gbps | Cat 6a / Fiber | Switches / servers |
| **100GbE** | IEEE 802.3ba/bm | 100 Gbps | Fiber | Data center backbones |
| **400GbE** | IEEE 802.3bs | 400 Gbps | Fiber | Hyperscale data centers |

#### Ethernet Operation: CSMA/CD (Legacy) vs Full-Duplex Switched (Modern)

- **CSMA/CD (Carrier Sense Multiple Access / Collision Detection):** Legacy MAC protocol for shared Ethernet hubs. Stations sense carriers before transmitting and abort upon collision detection.
- **Minimum Frame Size in CSMA/CD:**
  To guarantee collision detection before transmission finishes:
  $$t_{trans} \ge 2 \times t_{prop}$$
  $$L_{min} \ge 2 \times t_{prop} \times R$$
  *Where $t_{prop}$ is one-way propagation delay between furthest nodes and $R$ is link bandwidth.*
  
  *Calculation Example:*
  For $R = 15 \text{ Mbps}$ and $t_{prop} = 25.6\ \mu s$:
  $$L_{min} = 2 \times (25.6 \times 10^{-6}) \times (15 \times 10^6) = 768 \text{ bits} \text{ (96 Bytes)}$$

- **Modern Switched Ethernet:** Uses point-to-point **full-duplex** links connected to Layer 2 switches. Collisions are entirely eliminated.

```
  Ethernet Frame Format
  ─────────────────────────────────────────────────────────────────────
  ┌──────────┬──────────┬──────┬──────────────────────┬─────┐
  │ Preamble │ Dst MAC  │ Src  │      Payload         │ FCS │
  │  8 bytes │  6 bytes │ MAC  │   46 - 1500 bytes    │ 4B  │
  │          │          │ 6 B  │  (Ethernet MTU=1500) │(CRC)│
  └──────────┴──────────┴──────┴──────────────────────┴─────┘
  FCS: CRC-32 for error detection
  Ethernet MTU: 1,500 bytes payload
```

---

## Mobile / Wireless Access Networks
*Mobile / Wireless Access Networks*

Wireless access technologies substitute physical cabling for untethered mobility. They fall into **Wi-Fi** (local WLAN coverage) and **cellular networks** (4G LTE, 5G NR wide-area coverage).

---

### Wi-Fi
*IEEE 802.11 — Wireless LAN*

#### What is Wi-Fi

**Wi-Fi** (IEEE 802.11) enables wireless communication between client devices and an **Access Point (AP)** connected to a wired Ethernet LAN.

```
  Wi-Fi Infrastructure Mode
  ─────────────────────────────────────────────────────────────────────
  [Internet / ISP] ──▶ [Router] ──▶ [Wi-Fi Access Point]
                                              )))  2.4/5/6 GHz RF
                                         ┌─────┴─────┐
                                         |[PC][Phone]|
                                         └───────────┘
```

- **BSS (Basic Service Set):** An AP and its associated clients. Identified by **BSSID** (AP MAC address) and **SSID** (network name).
- **ESS (Extended Service Set):** Multiple BSSs sharing an SSID across a wired distribution system, supporting client **roaming**.

#### Wi-Fi Evolution

| Generation | Standard | Frequencies | Max Speed | Core Technologies |
|---|---|---|---|---|
| Wi-Fi 4 | 802.11n | 2.4 / 5 GHz | 600 Mbps | MIMO, 40 MHz |
| Wi-Fi 5 | 802.11ac | 5 GHz | 3.5 Gbps | MU-MIMO, 80/160 MHz |
| **Wi-Fi 6** | **802.11ax** | **2.4 / 5 / 6 GHz** | **9.6 Gbps** | **OFDMA, 1024-QAM** |
| Wi-Fi 7 | 802.11be | 2.4 / 5 / 6 GHz | ~46 Gbps | Multi-Link, 4096-QAM |

#### CSMA/CA Access Control

Wi-Fi uses **CSMA/CA (Collision Avoidance)** because wireless collision detection (CSMA/CD) is physically impossible (transmitters blind their own receivers).

```
  CSMA/CA Flow
  ─────────────────────────────────────────────────────────────────────
  1. Carrier Sense (Listen to medium)
  2. If clear, wait DIFS interval
  3. Choose random backoff timer in Contention Window
  4. Decrement timer while channel stays clear
  5. Transmit when backoff = 0
  6. Await ACK from receiver (retransmit if ACK missing)
```

---

### 4G / 5G
*Cellular Mobile Networks*

#### Cellular Network Architecture

Cellular networks divide geographical space into **cells**, each served by a **Base Station (BS)** — termed **eNodeB** (4G LTE) or **gNodeB** (5G NR).

```
  Cellular Architecture
  ─────────────────────────────────────────────────────────────────────
                   [Core Network: EPC (4G) / 5GC (5G)]
                        |           |           |
               [eNodeB/gNodeB] [eNodeB] [eNodeB]
                      ))))))))  RF Coverage
                     ┌────┴────┐
                     |[UE] [UE]|  User Equipment
                     └─────────┘
```

- **Handover:** Automatic transfer of an active connection from one base station to another as user equipment moves.

#### 4G LTE

- **Peak Speeds:** ~300 Mbps download, ~75 Mbps upload (LTE-Advanced: ~1 Gbps).
- **Latency:** ~30–50 ms.
- **Core Architecture:** **EPC (Evolved Packet Core)** — All-IP network.

#### 5G NR (New Radio)

**Frequency Ranges:**
- **FR1 (Sub-6 GHz):** 410 MHz – 7.125 GHz (Wide coverage, speeds up to 4 Gbps).
- **FR2 (mmWave):** 24.25 GHz – 71 GHz (Ultra-high speed up to 20 Gbps, short range, poor penetration).

```
  5G Service Triangle (ITU IMT-2020)
  ─────────────────────────────────────────────────────────────────────
            eMBB (Enhanced Mobile Broadband)
             /\  ← High throughput (streaming, AR/VR)
            /  \
           /    \
  URLLC  /________\  mMTC
  (Ultra-Reliable    (Massive Machine-Type
   Low-Latency)       Comm: 1M IoT devices/km²)
   ← <1ms latency: autonomous vehicles, robotics
```

**Key 5G Technologies:** Massive MIMO, Beamforming, Network Slicing, Edge Computing (MEC).

#### Wi-Fi vs Cellular Comparison

| Feature | Wi-Fi 6 (802.11ax) | 4G LTE | 5G NR |
|---|---|---|---|
| **Spectrum** | Unlicensed (free) | Licensed | Licensed |
| **Coverage** | Local (~100m) | Wide-area (km) | Wide-area + mmWave cells |
| **Mobility** | Limited | High (handover) | High (handover) |
| **Latency** | ~5–20 ms | ~30–50 ms | < 1 ms (URLLC) |

---

## Worked Numerical Example
*Access Technology Transfer Time Comparison*

**Scenario:** A user downloads a file of size $F = 10 \text{ MB} = 80 \times 10^6 \text{ bits}$ across different access technologies. Compute theoretical transmission time $T_{trans} = F / R$.

| Technology | Bandwidth $R$ | $T_{trans} = F / R$ |
|---|---|---|
| ADSL (download) | 24 Mbps | $\frac{80 \times 10^6}{24 \times 10^6} = 3.33 \text{ s}$ |
| HFC DOCSIS 3.1 | 1 Gbps | $\frac{80 \times 10^6}{10^9} = 0.08 \text{ s} = 80 \text{ ms}$ |
| FTTH XGS-PON | 10 Gbps | $\frac{80 \times 10^6}{10^{10}} = 0.008 \text{ s} = 8 \text{ ms}$ |
| Wi-Fi 6 (practical) | 500 Mbps | $\frac{80 \times 10^6}{5 \times 10^8} = 0.16 \text{ s} = 160 \text{ ms}$ |
| 4G LTE (practical) | 100 Mbps | $\frac{80 \times 10^6}{10^8} = 0.8 \text{ s}$ |
| 5G NR (Sub-6) | 500 Mbps | $\frac{80 \times 10^6}{5 \times 10^8} = 0.16 \text{ s} = 160 \text{ ms}$ |

**Conclusion:** FTTH XGS-PON is **416x faster** than 24 Mbps ADSL for downloading this file.

---

## Summary Table

| Technology | Medium | Download | Upload | Shared Medium? | OSI Layer |
|---|---|---|---|---|---|
| **ADSL** | Copper | 1–24 Mbps | 0.5–3.5 Mbps | No (dedicated) | L1/L2 |
| **VDSL2** | Copper + Fiber | 30–100 Mbps | 10–50 Mbps | No (dedicated) | L1/L2 |
| **HFC (DOCSIS 3.1)** | Fiber + Coax | Up to 10 Gbps | Up to 2 Gbps | **Yes** (coax) | L1/L2 |
| **FTTH (GPON)** | Optical Fiber | 2.5 Gbps | 1.25 Gbps | Yes (PON) | L1/L2 |
| **FTTH (XGS-PON)** | Optical Fiber | 10 Gbps | 10 Gbps | Yes (PON) | L1/L2 |
| **Ethernet (1GbE)** | UTP Cat5e/6 | 1 Gbps | 1 Gbps | No (switched) | L1/L2 |
| **Wi-Fi 6 (802.11ax)** | RF (2.4/5/6 GHz) | Up to 9.6 Gbps | Same | **Yes** (RF) | L1/L2 |
| **4G LTE** | RF (sub-3 GHz) | ~50–300 Mbps | ~25–75 Mbps | **Yes** (cell) | L1/L2 |
| **5G NR (Sub-6)** | RF (sub-6 GHz) | ~100 Mbps–4 Gbps | High | **Yes** (cell) | L1/L2 |
| **5G NR (mmWave)** | RF (24–71 GHz) | Up to 20 Gbps | High | **Yes** (cell) | L1/L2 |

---

## Key Takeaways

- **DSL** reuses legacy copper pairs, but performance drops severely with distance from the CO.
- **HFC** combines fiber backhaul with shared coaxial last-mile distribution; peak traffic degrades per-user speeds.
- **FTTH (XGS-PON)** delivers end-to-end optical fiber offering symmetric 10 Gbps speeds.
- **Ethernet** dominates campus networks in 3-tier topologies (Core–Distribution–Access).
- **Wi-Fi 6** uses **CSMA/CA**, **OFDMA**, and **MU-MIMO** for high-density WLAN access.
- **Cellular networks (4G/5G)** provide wide-area mobility through cell **handover**.
- **5G** defines three service profiles: **eMBB** (throughput), **URLLC** (<1ms latency), and **mMTC** (massive IoT density).
- Access technologies operate strictly at **Layer 1 (Physical)** and **Layer 2 (Data Link)**.
- **Exam Note:** Distinguish between **dedicated** (DSL, switched Ethernet) and **shared** media (HFC coax, Wi-Fi, cellular) to determine bandwidth contention risks.
