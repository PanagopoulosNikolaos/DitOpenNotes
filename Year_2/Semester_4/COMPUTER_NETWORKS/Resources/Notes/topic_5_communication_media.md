# Communication Media
*Communication Media*

---

## Table of Contents

- [Introduction](#introduction)
- [Copper Media: Coaxial and Twisted Pair](#copper-media-coaxial-and-twisted-pair)
  - [Twisted Pair Cable](#twisted-pair-cable)
  - [Coaxial Cable](#coaxial-cable)
  - [Copper Comparison Table](#copper-comparison-table)
- [Single-Mode Fiber Optic](#single-mode-fiber-optic)
  - [Operating Principle](#operating-principle)
  - [Structure and Physical Characteristics](#structure-and-physical-characteristics)
  - [Single-Mode vs Multi-Mode Fiber](#single-mode-vs-multi-mode-fiber)
  - [Dense Wavelength Division Multiplexing (DWDM)](#dense-wavelength-division-multiplexing-dwdm)
  - [Worked Numerical Example](#worked-numerical-example)
- [Satellite Communications](#satellite-communications)
  - [Geostationary Earth Orbit (GEO)](#geostationary-earth-orbit-geo)
  - [Low Earth Orbit Satellites (LEO)](#low-earth-orbit-satellites-leo)
  - [GEO vs LEO Comparison](#geo-vs-leo-comparison)
  - [Worked Numerical Example](#worked-numerical-example-1)
- [Wireless — Terrestrial Microwave Links](#wireless--terrestrial-microwave-links)
  - [Operating Principle](#operating-principle-1)
  - [Frequency Bands and Applications](#frequency-bands-and-applications)
  - [Factors Affecting Microwave Links](#factors-affecting-microwave-links)
- [Guided vs Unguided Media: General Comparison](#guided-vs-unguided-media-general-comparison)
- [Summary Table](#summary-table)
- [Key Takeaways](#key-takeaways)

---

## Introduction

**Communication media** form the physical foundation underpinning computer networks — from office Ethernet LANs to transoceanic submarine cables. Media belong to the OSI **Physical Layer (Layer 1)**, which specifies bit encoding and physical transmission. Choosing a medium influences bandwidth, latency, attenuation, noise immunity, and deployment cost. Understanding media properties (copper, fiber, satellite, wireless) is prerequisite to evaluating access technologies (Topic 4) and data switching (Topic 6).

---

## Copper Media: Coaxial and Twisted Pair
*Copper Media: Coaxial and Twisted Pair*

**Copper** remains widely deployed due to low cost, ease of installation, and backward compatibility. Copper cables belong to **guided media**, channeling electromagnetic signals as AC electrical current.

### Twisted Pair Cable
*Twisted Pair Cable*

**Twisted pair** cabling consists of insulated copper wires twisted around each other in a helix. Twisting reduces **electromagnetic interference (EMI)** and **crosstalk** between adjacent pairs. Standard Ethernet cables bundle **4 pairs** (8 wires).

```
  Twisted Pair Cable Structure
  ───────────────────────────────────────────────────────
  ╔═══════════════════════════════════════════╗
  ║  Outer Jacket (PVC)                       ║
  ║  ┌───────────────────────────────────┐   ║
  ║  │  Pair 1: ─────/─────/─────        │   ║
  ║  │  Pair 2:   ──/──/──/──/──         │   ║ ← 4 pairs / 8 wires
  ║  │  Pair 3:  ────/────/────          │   ║
  ║  │  Pair 4:   ───/───/───/           │   ║
  ║  └───────────────────────────────────┘   ║
  ╚═══════════════════════════════════════════╝
```

| Category | Max Speed | Bandwidth | Max Distance | Typical Application |
|---|---|---|---|---|
| **Cat5e** | 1 Gbps | 100 MHz | 100 m | Ethernet LAN, DSL |
| **Cat6** | 1 Gbps / 10 Gbps* | 250 MHz | 100 m / 55 m* | Offices, switches |
| **Cat6a** | 10 Gbps | 500 MHz | 100 m | Data centers, enterprise |
| **Cat7** | 10 Gbps | 600 MHz | 100 m | High-performance LANs |
| **Cat8** | 25/40 Gbps | 2000 MHz | 30 m | Server racks, short links |

*\*Cat6 supports 10 Gbps up to ~55 m.*

**Shielding Types:**
- **UTP (Unshielded Twisted Pair):** Unshielded, flexible, standard for indoor Ethernet.
- **STP (Shielded Twisted Pair):** Shielded pairs, providing superior EMI immunity for industrial environments.
- **FTP (Foiled Twisted Pair):** Overall foil shield wrapping all pairs.

**Power over Ethernet (PoE):** Delivers DC power alongside data over the same Ethernet cable, powering IP cameras, VoIP phones, and Wi-Fi APs without separate power supplies.

**Key Distinction:** **Attenuation** increases with frequency and distance. Ethernet standards enforce a **100 m** segment limit before requiring switches or repeaters.

---

### Coaxial Cable
*Coaxial Cable*

**Coaxial cable** features four concentric layers along a common axis:

```
  Coaxial Cable Structure
  ───────────────────────────────────────────────────────
  ╔═══════════════════════════════════════════════════╗
  ║  4. Outer PVC Jacket                             ║
  ║  ┌───────────────────────────────────────────┐   ║
  ║  │  3. Metallic Shielding Braid (Faraday)    │   ║  ← EMI Shielding
  ║  │  ┌─────────────────────────────────────┐  │   ║
  ║  │  │  2. Dielectric Insulator           │  │   ║
  ║  │  │  ┌───────────────────────────────┐  │  │   ║
  ║  │  │  │  1. Central Copper Conductor  │  │  │   ║  ← Carries signal
  ║  │  │  └───────────────────────────────┘  │  │   ║
  ║  └───────────────────────────────────────────┘   ║
  ╚═══════════════════════════════════════════════════╝
```

- **75 $\Omega$ (RG-6, RG-11):** Standard for cable TV (CATV) and HFC last-mile broadband (DOCSIS).
- **50 $\Omega$ (RG-8, RG-58):** Specialized RF radio communication.

**Coaxial vs Twisted Pair:**
- **Superior EMI Shielding:** Central conductor rests inside a metallic Faraday cage.
- **Longer distance without amplification:** 100–500 m segments.
- **Higher RF bandwidth:** Ideal for multi-channel RF signals (cable modems).
- **Drawbacks:** Stiffer, lacks PoE support, complex F-type connectors.

---

### Copper Comparison Table

| Property | Twisted Pair (UTP Cat6a) | Coaxial (75 $\Omega$ RG-6) |
|---|---|---|
| **Typical Use** | Ethernet LAN, DSL | HFC, cable TV |
| **Max Speed** | 10 Gbps (100 m) | Gbps+ (DOCSIS 3.1) |
| **Max Distance** | 100 m | 500 m unamplified |
| **EMI Shielding** | Moderate (UTP) / High (STP) | Superior (Faraday cage) |
| **Flexibility** | High | Low |
| **PoE Support** | Yes | No |
| **Cost** | Low | Moderate |
| **Connector** | RJ-45 | F-type / BNC |

---

## Single-Mode Fiber Optic
*Single-Mode Fiber Optic*

### Operating Principle

**Optical fiber** transmits **light pulses** instead of electrical currents. Photons travel inside glass fibers at roughly **$\frac{2}{3}c \approx 2 \times 10^8$ m/s** due to the glass refractive index.

#### Total Internal Reflection

Light stays trapped inside the fiber core due to **total internal reflection**: when light strikes the core-cladding boundary at an angle greater than the critical angle, it reflects completely into the core.

```
  Total Internal Reflection in Fiber
  ───────────────────────────────────────────────────────────────
  Cladding (low index n2)
  ─────────────────────────────────────────────────────────────
  Core     (high index n1)
       ╲       ╱       ╲       ╱       ╲       ╱
        ╲     ╱         ╲     ╱         ╲     ╱
   Laser ╲   ╱           ╲   ╱           ╲   ╱   → Light pulse
   source ╲ ╱             ╲ ╱             ╲ ╱
  ─────────V───────────────V───────────────V──────────────────
  Cladding (low index n2)

  Condition: n1 > n2  ⟹ Total internal reflection
```

**Single-Mode Fiber (SMF)** uses semiconductor **lasers** to inject light into an 8–10 $\mu m$ core.

---

### Structure and Physical Characteristics

```
  Single-Mode Fiber Optic Structure (SMF)
  ────────────────────────────────────────────────────────────────
  ╔════════════════════════════════════════════════════════╗
  ║  Outer Buffer Coating (250–900 $\mu m$)              ║  ← Mechanical protection
  ║  ┌──────────────────────────────────────────────────┐  ║
  ║  │  Cladding (125 $\mu m$ outer diameter)           │  ║  ← Low n, reflection
  ║  │  ┌────────────────────────────────────────────┐  │  ║
  ║  │  │  Core (~8-10 $\mu m$ diameter)              │  │  ║  ← Carries laser light
  ║  │  └────────────────────────────────────────────┘  │  ║
  ║  └──────────────────────────────────────────────────┘  ║
  ╚════════════════════════════════════════════════════════╝
```

| Parameter | Value |
|---|---|
| Core diameter | ~8–10 $\mu m$ |
| Cladding diameter | 125 $\mu m$ |
| Light source | Laser |
| Operating Wavelengths | 1310 nm (O-band) and 1550 nm (C-band) |
| Attenuation @ 1310 nm | ~0.35 dB/km |
| Attenuation @ 1550 nm | ~0.20 dB/km (lowest loss) |
| Max Distance | >100 km (hundreds of km with EDFAs) |
| Channel Bandwidth | 100 Gbps+ |

**1550 nm Window:** Represents the **attenuation minimum** in silica glass (~0.20 dB/km). Erbium-Doped Fiber Amplifiers (EDFA) amplify 1550 nm signals optically without electrical conversion.

**Exam Note:** Single-mode fiber admits only **one light mode (ray)**. This eliminates **modal dispersion**, enabling multi-hundred-kilometer links without pulse distortion.

---

### Single-Mode vs Multi-Mode Fiber

| Property | Single-Mode (SMF) | Multi-Mode (MMF) |
|---|---|---|
| Core Diameter | ~8–10 $\mu m$ | ~50–62.5 $\mu m$ |
| Light Modes | 1 | Many (100+) |
| Light Source | Laser | LED or VCSEL |
| Modal Dispersion | None | Significant |
| Max Distance | >100 km | <2 km |
| Bandwidth | Extremely High | Moderate |
| Transceiver Cost | High | Low |
| Primary Use | ISP backbones, WAN, submarine | Data centers, intra-building |

---

### Dense Wavelength Division Multiplexing (DWDM)

**DWDM** multiplexes dozens of parallel optical channels over a single fiber using distinct laser wavelengths.

```
  DWDM Concept
  ────────────────────────────────────────────────────────────────
  [Laser $\lambda_1$ = 1530.33 nm] ─────┐
  [Laser $\lambda_2$ = 1531.12 nm] ─────┤
  [Laser $\lambda_3$ = 1531.90 nm] ─────┤  [Multiplexer]═══════[SMF]═══════[Demultiplexer]
  [Laser $\lambda_4$ = 1532.68 nm] ─────┤                                        │
        ...                    ┤                                   $\lambda_1$..$\lambda_N$ channels
  [Laser $\lambda_N$ = 1561.42 nm] ─────┘

  Capacity: 80–160 channels × 100 Gbps/channel = 8–16+ Tbps per fiber
```

---

### Worked Numerical Example
*Propagation Delay in Fiber*

**Scenario:** Transmitting a packet across a $d = 3,800 \text{ km}$ submarine fiber cable between Lisbon and Athens.
- Propagation speed in fiber: $s = 2 \times 10^8 \text{ m/s}$
- Link bandwidth: $R = 100 \text{ Gbps} = 10^{11} \text{ bps}$
- Packet size: $L = 12,000 \text{ bits}$

**Propagation Delay:**

$$d_{prop} = \frac{d}{s} = \frac{3.8 \times 10^6}{2 \times 10^8} = 0.019 \text{ s} = 19 \text{ ms}$$

**Transmission Delay:**

$$d_{trans} = \frac{L}{R} = \frac{12,000}{10^{11}} = 1.2 \times 10^{-7} \text{ s} = 0.00012 \text{ ms}$$

**Conclusion:** At high optical rates (100 Gbps), transmission delay is negligible ($0.00012\text{ ms}$) compared to propagation delay ($19\text{ ms}$). Physical distance and light speed dictate total delay.

---

## Satellite Communications
*Satellite Communications*

Satellites act as spaceborne **relay stations**, receiving signals from ground stations (**uplink**) and retransmitting them to distant terminals (**downlink**).

### Geostationary Earth Orbit (GEO)

GEO satellites orbit at an altitude of **~35,786 km** above the Equator. Their orbital velocity matches Earth's rotation speed, making them appear **stationary** from the ground.

```
  Geostationary Satellite (GEO)
  ────────────────────────────────────────────────────────────────
                        [GEO Satellite]
                       ~35,786 km altitude
                      /               \
           [Uplink]  /                 \  [Downlink]
                    /                   \
          [Gateway Station]        [Dish Antenna]
                |                       |
           [Internet]              [Home / Ship]

  Signal Path RTT: ~4 × 35,786 km ≈ 143,144 km
  Latency RTT: ~500–700 ms
```

- **Latency:** ~500–700 ms RTT (excessive for real-time traffic).
- **Coverage:** Just 3 GEO satellites cover almost the entire planet.
- **Unsuitable for:** Real-time VoIP, online gaming, interactive applications.

---

### Low Earth Orbit Satellites (LEO)

LEO satellites orbit at **~500–2,000 km**. Moving at ~7–8 km/s, they complete orbits in ~90–120 minutes, requiring large satellite **constellations** (e.g. Starlink) for continuous coverage.

```
  LEO Constellation (e.g. Starlink)
  ────────────────────────────────────────────────────────────────
  [LEO Sat A] ←──Laser ISL──→ [LEO Sat B] ←──Laser ISL──→ [LEO Sat C]
       ↑  ~550 km                    ↑                           ↑
   [Gateway]                     [User Dish]                [Gateway]
```

- **Latency:** 20–50 ms RTT (comparable to landline broadband).
- **Speeds:** 50–300+ Mbps.
- **Inter-Satellite Links (ISL):** Laser cross-links route packets space-to-space without intermediate ground hops.

---

### GEO vs LEO Comparison

| Property | GEO Satellite | LEO Constellation |
|---|---|---|
| **Orbital Altitude** | ~35,786 km | ~500–2,000 km |
| **Latency (RTT)** | 500–700 ms | 20–50 ms |
| **Download Speeds** | 25–100 Mbps | 50–1,000 Mbps |
| **Satellites Needed** | 3 for global coverage | 1,000+ |
| **Handover** | None | Every 5–7 minutes |
| **Antenna** | Fixed dish | Phased-array auto-tracking |

---

### Worked Numerical Example
*GEO vs LEO RTT Propagation Latency*

**Theoretical GEO RTT:**

$$RTT_{GEO} = \frac{4 \times 35,786,000}{3 \times 10^8} \approx 0.477 \text{ s} = 477 \text{ ms}$$

*(Real-world RTT with processing: 500–700 ms).*

**Theoretical LEO RTT (550 km):**

$$RTT_{LEO} = \frac{4 \times 550,000}{3 \times 10^8} \approx 0.0073 \text{ s} = 7.3 \text{ ms}$$

*(Real-world RTT with routing/handover: 20–50 ms).*

---

## Wireless — Terrestrial Microwave Links
*Wireless — Terrestrial Microwave Links*

### Operating Principle

Terrestrial microwave links provide point-to-point wireless connections across **1 GHz – 90+ GHz** radio frequencies using directional parabolic dish antennas.

```
  Point-to-Point Microwave Link
  ────────────────────────────────────────────────────────────────
  [Parabolic Antenna]                     [Parabolic Antenna]
         ║                                         ║
     [Router]        ~~~ microwave ~~~        [Router]

  Range: Up to 50+ km (Line-of-sight required)
```

**Requirements:** Clear **Line-of-Sight (LOS)** and unobstructed **Fresnel Zone**.

---

### Frequency Bands and Applications

| Band | Application | Distance | Properties |
|---|---|---|---|
| **2–11 GHz** | Long-haul backhaul | 10–50+ km | Resistant to rain attenuation |
| **13–23 GHz** | Cellular backhaul (4G/5G) | 5–15 km | High capacity |
| **70–80 GHz (E-band)** | Short high-speed links | 1–3 km | Multi-Gbps throughput |

---

### Factors Affecting Microwave Links

1. **Rain Attenuation (Rain Fade):** Frequencies above 10 GHz suffer severe signal absorption during heavy rain.
2. **Multipath Fading:** Reflections from ground/water cause destructive phase interference.
3. **Adaptive Modulation (ACM):** Dynamically adjusts QAM order (e.g. 256-QAM to 16-QAM) to sustain links during rain fade.

---

## Guided vs Unguided Media: General Comparison

```
  Physical Media Classification
  ────────────────────────────────────────────────────────────────
  Physical Media
       │
       ├── Guided (Wired / Cables)
       │       ├── Copper (Twisted Pair, Coaxial)
       │       └── Optical Fiber (Single-Mode, Multi-Mode)
       │
       └── Unguided (Wireless / Space)
               ├── Terrestrial (Microwave links, Wi-Fi, Cellular)
               └── Satellite (GEO, LEO)
```

---

## Summary Table

| Medium | Type | Bandwidth | Typical Range | Latency | Key Application |
|---|---|---|---|---|---|
| **Twisted Pair (Cat6a)** | Guided / Copper | 10 Gbps | 100 m | <1 ms | Ethernet LAN, DSL |
| **Coaxial (RG-6)** | Guided / Copper | Gbps+ | 500 m | <1 ms | HFC cable internet |
| **Single-Mode Fiber** | Guided / Optical | 100 Gbps+ (DWDM: Tbps) | >100 km | ~19 ms (3800 km) | Backbone, WAN, submarine |
| **GEO Satellite** | Unguided / Satellite | 25–100 Mbps | Global (3 sats) | 500–700 ms | TV broadcast, remote sites |
| **LEO Satellite** | Unguided / Satellite | 50–1000 Mbps | Global (1000+ sats) | 20–50 ms | Rural broadband |
| **Terrestrial Microwave** | Unguided / Wireless | Gbps | 1–50 km | <5 ms | Cellular backhaul, ISP WAN |

---

## Key Takeaways

- **Guided media** (copper, fiber) offer high speed and reliability over physically wired paths.
- **Unguided media** (satellite, wireless) enable untethered mobility and remote coverage.
- **Twisted pair** is the standard Ethernet LAN cable supporting PoE up to 100 meters.
- **Single-Mode Fiber** with **DWDM** transports terabits per second across oceanic distances.
- **GEO satellites** offer wide coverage at the expense of high latency (~600 ms).
- **LEO constellations** (Starlink) reduce satellite latency to 20–50 ms.
- **Terrestrial microwaves** provide high-capacity wireless backhaul where running fiber is cost-prohibitive.
