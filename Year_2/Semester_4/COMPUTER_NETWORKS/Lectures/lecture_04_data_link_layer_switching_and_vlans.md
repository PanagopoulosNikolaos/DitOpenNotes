# Lecture 04: Data Link Layer, Ethernet Switching, and VLANs

This lecture covers the Data Link Layer (Layer 2): MAC addressing, Ethernet frame structures, transparent bridging, switch self-learning algorithms, collision vs. broadcast domains, and Virtual Local Area Networks (VLANs).

---

## 1. Data Link Layer Fundamentals

The data link layer transfers frames across a single physical link connecting adjacent nodes (host-to-switch, switch-to-switch, or host-to-router).

### 1.1 MAC Addressing
- **Media Access Control (MAC) Address:** 48-bit (6-byte) physical hardware address burned into the network interface card (NIC) ROM.
- **Notation:** Hexadecimal format (e.g., `00:1A:2B:3C:4D:5E`).
- **Hierarchy:** First 24 bits = Organizationally Unique Identifier (OUI) assigned by IEEE; last 24 bits = vendor-specific NIC identifier.
- **Broadcast MAC:** `FF:FF:FF:FF:FF:FF` (received by all interfaces on the local LAN).

### 1.2 Ethernet Frame Format (IEEE 802.3)

| Preamble | Destination MAC | Source MAC | Type / Length | Data Payload | Frame Check Sequence (FCS) |
|---|---|---|---|---|---|
| 8 bytes | 6 bytes | 6 bytes | 2 bytes | 46 to 1500 bytes (MTU) | 4 bytes (CRC-32) |

---

## 2. Transparent Switching and Self-Learning

A network switch operates at Layer 2, selectively forwarding Ethernet frames based on destination MAC addresses without requiring manual configuration.

```
       Host A (MAC_A)                   Host B (MAC_B)
             |                                |
        Port 1|                          Port 2|
       +---------------------------------------------+
       |             Ethernet Switch                 |
       |  Switch Table: [ MAC | Port | Aging TTL ]   |
       +---------------------------------------------+
        Port 3|                          Port 4|
             |                                |
       Host C (MAC_C)                   Host D (MAC_D)
```

### 2.1 The Self-Learning Algorithm
When a frame arrives at switch port $P$ with Source MAC $S$ and Destination MAC $D$:

1. **Table Record:** Inspect Source MAC $S$. Record or update entry in switch table:
   $$(S, P, \text{current\_time})$$
2. **Forwarding Decision:** Look up Destination MAC $D$ in switch table:
   - **Case 1 (Hit on same port $P$):** Destination is on the same segment. **Filter (drop)** the frame.
   - **Case 2 (Hit on different port $Q \neq P$):** Destination location is known. **Forward (unicast)** frame out port $Q$ only.
   - **Case 3 (Miss / Broadcast MAC):** Destination is unknown or broadcast. **Flood** the frame out all ports except arriving port $P$.
3. **Table Aging:** Entries expire after an aging timer (typically 300 seconds) to adapt dynamically to host relocations.

---

## 3. Collision Domains vs. Broadcast Domains

| Feature | Collision Domain | Broadcast Domain |
|---|---|---|
| **Definition** | Network segment where simultaneous transmissions cause signal collision | Network region where a broadcast frame (`FF:FF:FF:FF:FF:FF`) propagates |
| **Delimited by** | Layer 2 Switch ports, Layer 3 Router interfaces | Layer 3 Router interfaces |
| **Hub / Repeater (Layer 1)** | Extends single collision domain | Extends single broadcast domain |
| **Switch (Layer 2)** | Each individual switch port forms its own collision domain | All switch ports belong to one shared broadcast domain |
| **Router (Layer 3)** | Separates collision domains | Separates broadcast domains |

---

## 4. Virtual Local Area Networks (VLANs)

A Virtual Local Area Network (VLAN) logically segments a single physical switch into multiple isolated broadcast domains.

```
[ Switch Physical Chassis ]
  Port 1, 2, 3: VLAN 10 (Engineering)  ---> Broadcast Domain 10
  Port 4, 5, 6: VLAN 20 (Marketing)    ---> Broadcast Domain 20
```

### 4.1 Benefits of VLAN Segmentation
- **Traffic Isolation:** Broadcast traffic generated within VLAN 10 never leaks into VLAN 20.
- **Security:** Hosts in different VLANs cannot communicate directly at Layer 2; all cross-VLAN traffic must traverse a Layer 3 router or multilayer switch (**Inter-VLAN Routing**).
- **Physical Flexibility:** Departmental subnets do not require dedicated physical switches or wiring closets.

### 4.2 Port Types
- **Access Port:** Connects to an end host. Carries untagged Ethernet frames belonging exclusively to a single assigned VLAN.
- **Trunk Port:** Connects switches together or connects a switch to a router. Carries multiplexed frames from multiple VLANs over a single physical cable.

### 4.3 IEEE 802.1Q Frame Tagging
When an Ethernet frame traverses a trunk link, an 802.1Q header (4 bytes) is inserted immediately after the Source MAC field:

```
[ Dest MAC | Src MAC | 802.1Q Tag (4 Bytes) | Type | Payload | FCS ]
                         |
                         +---> TPID (0x8100) : 2 bytes
                         +---> Priority      : 3 bits
                         +---> CFI / DEI     : 1 bit
                         +---> VLAN ID (VID) : 12 bits (values 1 to 4094)
```

The receiving switch inspects the 12-bit VLAN ID, strips the 802.1Q tag, and forwards the native frame only to ports assigned to that specific VLAN.

