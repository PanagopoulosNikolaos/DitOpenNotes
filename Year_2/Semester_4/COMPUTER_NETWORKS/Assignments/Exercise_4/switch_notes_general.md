# Chapter 6 — How a Switch Works

---

## 1. Frames & MAC Addresses

Every piece of data crossing a LAN is wrapped in a **frame**. The frame is the fundamental unit of transmission at Layer 2 (the Data Link layer). Understanding its structure is prerequisite to understanding everything a switch does.

### Frame Structure

A complete frame has three components:

- **Header** — contains the source and destination MAC addresses. The switch reads the destination MAC from here to decide where to forward the frame.
- **Payload** — the actual data being carried. This is typically a packet from a Layer 3 protocol (e.g. an IP packet), encapsulated inside the frame. The frame doesn't care what's inside — it just carries it.
- **Trailer** — marks the end of the frame and carries the **CRC (Cyclic Redundancy Check)** — a mathematical checksum computed from the number of bits in the frame. The receiving device recomputes the CRC and compares it to the trailer value; a mismatch means the frame was corrupted in transit.

### MAC Addresses

A MAC (Media Access Control) address is the **physical address** burned into every network interface card (NIC) at the factory. It is 48 bits (6 bytes) long and globally unique — no two NICs should share the same MAC address.

It is composed of two 24-bit halves:

| Part | Size | Purpose | Example |
|---|---|---|---|
| OUI (Organizational Unique Identifier) | 24 bits | Identifies the manufacturer | `00-06-0f` |
| Vendor-assigned ID | 24 bits | Unique serial for that specific NIC | `08-b4-12` |

Full example: `00-06-0f-08-b4-12`

There are two types of addresses in a network:
- **Logical address** (IP address) — assigned by software, can change, used at Layer 3
- **Physical address** (MAC address) — burned into hardware, used at Layer 2

Switches operate exclusively on MAC addresses. Routers operate on IP addresses. Both can refer to the same physical host — the router uses the IP to decide *which network* the host is on, and the switch uses the MAC to decide *which port* to deliver the frame to once it's on the right segment.

---

## 2. Transmission Methods

All data transmissions at Layer 2 fall into one of three categories. The category determines how the frame is delivered and how many copies of it are created.

### Unicast — One-to-One

A single frame sent from one source to one specific destination. The switch looks up the destination MAC in its forwarding table and sends the frame out only the port that MAC is associated with.

If multiple users request the same resource simultaneously (e.g. ten workstations all pulling the same video from a server), the server generates ten separate, independent unicast streams — one per recipient. This is simple to implement but scales poorly: ten users means ten times the bandwidth consumed on the uplink.

Unicast is the most common transmission type on a modern LAN.

### Multicast — One-to-Many

A single data stream is sent from one source toward multiple destinations that have explicitly opted into a **multicast group**. Rather than replicating the stream at the source, the network carries one copy across the backbone and only duplicates it at switching or routing points close to the end recipients.

The key distinction from broadcast: multicast is **opt-in**. Devices that are not members of the multicast group do not receive the traffic. This makes multicast significantly more efficient than broadcast for applications like video conferencing, IPTV, or financial data feeds where the same stream needs to reach a defined set of subscribers.

Multicast requires devices and switches to support multicast group management (e.g. IGMP snooping on managed switches) to work correctly.

### Broadcast — One-to-All

A single frame sent to every device on the local network segment simultaneously, whether those devices want the traffic or not. The destination MAC address of a broadcast frame is `FF-FF-FF-FF-FF-FF` — all ones — which every NIC recognizes as addressed to itself.

Broadcasts are used by:
- **ARP** — to resolve an unknown MAC address from a known IP address
- Devices announcing their presence on the network at startup
- Some legacy protocols that rely on network-wide discovery

Critically, **routers do not forward broadcasts**. A broadcast is contained within a single broadcast domain (typically a single VLAN or subnet). This is one of the primary reasons large networks are segmented — to limit how far broadcast traffic can propagate. A network flooded with excessive broadcast traffic suffers a condition called a **broadcast storm**, which can saturate links and crash devices.

---

## 3. Frame Size & Limits

Every networking technology defines a minimum and maximum frame size. These limits exist for physical and timing reasons — on Ethernet, for example, the minimum frame size is tied to the collision detection window of the CSMA/CD protocol.

### Ethernet Limits

| Boundary | Size | Notes |
|---|---|---|
| Minimum | 64 bytes | Includes the 4-byte CRC trailer |
| Maximum (MTU) | 1518 bytes | Standard Ethernet; some switches support jumbo frames up to 9000+ bytes if configured |

### Token Ring Limits

| Boundary | Size |
|---|---|
| Minimum | 32 bytes |
| Maximum | 16 KB |

### Runts and Giants

- **Runt** — any frame received below the minimum size. On Ethernet, below 64 bytes. Most commonly caused by collisions or a malfunctioning NIC. The switch discards all runts immediately regardless of switching method.
- **Giant** — any frame received above the MTU. On standard Ethernet, above 1518 bytes. Giants must be fragmented before they can be forwarded across an interface that enforces the MTU limit. A switch that doesn't support jumbo frames discards giants outright.

### MTU (Maximum Transmission Unit)

The MTU is the largest frame (measured in bytes) that a given network interface will accept and forward. It is a property of the technology in use — Ethernet, Token Ring, PPP, Frame Relay all have different MTUs.

When a frame is larger than the MTU of the outgoing interface, Layer 3 (IP) must **fragment** it into smaller pieces before it can be sent. This is expensive in terms of processing and can cause problems if fragments are lost or arrive out of order (covered in section 7).

---

## 4. Layer 2 Switching Methods

A LAN switch's primary job is to receive frames on one port and forward them out the correct port toward the destination. How much of the frame the switch inspects before making that forwarding decision defines which switching method it uses. There are three:

### Store-and-Forward

The switch copies the **entire frame** into its internal memory buffers before doing anything with it. Once the complete frame is received, it:

1. Computes the CRC and compares it to the value in the trailer
2. Checks the frame length — discards runts (< 64 bytes) and giants (> 1518 bytes)
3. If the frame passes all checks, looks up the destination MAC in the forwarding table
4. Forwards the frame out the appropriate port

**Advantages:**
- Only error-free, correctly-sized frames are forwarded. Bad frames never propagate beyond the switch, which protects the rest of the network and conserves bandwidth.
- Provides a foundation for QoS (Quality of Service) since the switch has the full frame available before forwarding.
- Required for Layer 3 (multilayer) switching since the full frame must be read before L3 inspection can occur.

**Disadvantages:**
- Introduces **latency** — the switch cannot begin forwarding until the last bit of the frame has arrived. On a 1 Gbps link a 1518-byte frame takes ~12 microseconds to receive; this delay compounds across multiple switch hops.
- Requires more memory and CPU cycles than other methods.

**Best suited for:** the network access layer, where end-user devices connect, errors are more frequent, and correctness matters more than raw speed.

---

### Cut-Through

The switch reads only the **first 6 bytes of the frame following the preamble** — the destination MAC address — and begins forwarding the frame immediately, before the rest of it has even arrived.

1. Destination MAC is identified from the first 6 bytes
2. Forwarding table is looked up
3. Frame begins exiting the outgoing port while it is still being received on the incoming port

**Advantages:**
- Extremely low latency — forwarding begins in microseconds regardless of frame size.
- Well-suited for high-throughput environments where frames are unlikely to be corrupted.

**Disadvantages:**
- **No error checking whatsoever.** Corrupted frames, runts, and giants all pass straight through.
- The destination device must detect the CRC error itself and discard the frame, then the source must retransmit. If errors are frequent, this wastes significant bandwidth.
- Does not support Layer 3 switching (needs the full frame for that).

**Best suited for:** the network core — high-speed inter-switch links where errors are rare, bandwidth is ample, and minimizing latency is the priority.

---

### Fragment-Free (Runtless)

A hybrid between store-and-forward and cut-through. The switch buffers the **first 64 bytes** of the frame before forwarding.

The rationale: the vast majority of network errors — normal collisions and runts — are detectable within the first 64 bytes of a frame. By reading just this much, fragment-free switching catches the most common error types (collision fragments) without incurring the full delay of buffering the entire frame.

**Late collision** — a collision that occurs after a host has already transmitted the first 64 bytes of its frame. Normal collisions on Ethernet are detected early (within the first 64 bytes). A late collision suggests the LAN segment is too large (exceeds the propagation delay budget), a NIC is faulty, or there is a duplex mismatch between connected devices. **Fragment-free switching CANNOT filter out late collisions** because it has already started forwarding the frame once the 64-byte threshold is reached. It is specifically designed to filter out *normal* (early) collision fragments, not late ones.

**Trade-off:** Fragment-free switching still forwards frames with CRC errors that don't manifest in the first 64 bytes, so it is not as thorough as store-and-forward. But it eliminates the most disruptive class of bad frames (runts and early collision fragments) with minimal added latency.

---

### Summary Comparison

| Method | What it reads | CRC check | Size check | Latency | Error filtering |
|---|---|---|---|---|---|
| Store-and-forward | Full frame | Yes | Yes (runts + giants) | Highest | Complete |
| Cut-through | First 6 bytes (dest MAC) | No | No | Lowest | None |
| Fragment-free | First 64 bytes | No | Partial (runts only) | Medium | Partial |

> Modern switch hardware is fast enough that store-and-forward latency is rarely a practical concern. Most enterprise switches default to store-and-forward and only fall back to cut-through under very specific high-performance requirements.

---

## 5. Layer 3 Switching & Routing

### The OSI Context

- **Layer 2 (Data Link)** — deals with frames and MAC addresses. Switches and bridges live here.
- **Layer 3 (Network)** — deals with packets and IP addresses. Routers and Layer 3 switches live here.

These layers don't replace each other — they work together. An IP packet (L3) is encapsulated inside an Ethernet frame (L2) for transport across a local network segment. When the frame arrives at a router, the L2 encapsulation is stripped off, the L3 packet is inspected, and a new L2 frame is constructed for the next hop.

### Layer 2 Switching vs. Layer 3 Switching

| | L2 Switch | L3 Switch | Traditional Router |
|---|---|---|---|
| Forwarding basis | MAC address table | IP routing table | IP routing table |
| Address lookup | Exact match, flat space | Longest prefix match, hierarchical | Longest prefix match, hierarchical |
| Implementation | Hardware ASICs | Hardware ASICs | Historically software, now often hardware |
| Speed | Wire speed | Wire speed | Generally slower than dedicated switching hardware |
| Features | Port-based forwarding, VLANs | Routing between VLANs, basic routing | Full routing: NAT, WAN interfaces, advanced routing protocols |

A **Layer 3 switch** is essentially a router implemented in dedicated switching hardware. It makes forwarding decisions based on IP addresses (Layer 3) but does so at the wire speeds normally associated with Layer 2 switching. The trade-off is that Layer 3 switches typically lack the full feature set of a software router — complex NAT configurations, WAN protocol support, and advanced routing policy are usually still the domain of a dedicated router.

### Multilayer Switching

A multilayer switch operates at both L2 and L3 simultaneously. It must use **store-and-forward** because the switch needs the complete frame in memory before it can perform L3 header inspection — you cannot read the IP destination address until you've received enough of the frame to get past the L2 headers.

### Media Transition — A Router-Only Feature

When a packet must cross between two different network technologies (e.g. from an Ethernet LAN to a Token Ring segment), a router (or L3 switch) must:

1. Strip the incoming L2 frame (Ethernet)
2. Inspect the L3 packet inside
3. Construct a new L2 frame in the format required by the outgoing interface (Token Ring)
4. Transmit the new frame

This process is called **media transition** and is one of the defining capabilities of Layer 3 devices. A pure L2 switch cannot do this — it can only forward frames within the same network technology.

### Routing Protocols

Routers learn about the network through three mechanisms:

- **Directly connected networks** — automatically known when an interface is brought up
- **Static routes** — manually configured by a network administrator
- **Dynamic routing protocols** — automatically exchanged between routers:
  - **RIP** (Routing Information Protocol) — simple, distance-vector, limited scalability
  - **OSPF** (Open Shortest Path First) — link-state, widely used in enterprise
  - **IGRP/EIGRP** — Cisco proprietary
  - **BGP** (Border Gateway Protocol) — used on the internet between autonomous systems

---

## 6. Routing Table Lookup & ARP

### How a Router Forwards a Packet

When a packet arrives at a router interface, the router performs a **routing table lookup** using the destination IP address. Unlike a switch's MAC table (exact match on a flat address space), a router's lookup uses **longest prefix match** on a hierarchical address space — it finds the most specific route entry that matches the destination.

The lookup returns one of three outcomes:

#### 1. Destination unreachable
No route exists for the destination network and no default route is configured. The router drops the packet and may send an ICMP "Destination Unreachable" message back to the sender.

#### 2. Destination reachable via another router
The routing table contains a matching entry pointing to a next-hop router. The router:
1. Identifies the next-hop IP address from the routing table
2. Performs a second lookup to find which local interface can reach that next-hop
3. Checks the ARP cache for the next-hop router's MAC address (or sends an ARP request if unknown)
4. Encapsulates the packet in a new frame addressed to the next-hop router's MAC and forwards it

#### 3. Destination on a directly attached network
The destination host is on one of the router's own local interfaces. The router:
1. Checks its ARP cache for the destination host's MAC address
2. If found, encapsulates the packet in a frame with that MAC as destination and sends it
3. If not found, broadcasts an ARP request and (in Cisco IOS) drops the triggering packet. If the packet belongs to a reliable protocol like TCP, the source will automatically retransmit it; for unreliable protocols (like UDP or ICMP), the packet is simply lost.

### ARP — Address Resolution Protocol

IP operates at 32 bits. MAC addresses are 48 bits. There is no mathematical relationship between them — you cannot derive a MAC from an IP or vice versa. ARP solves this problem.

**ARP process:**
1. Device A wants to send to IP `192.168.1.50` but doesn't know its MAC
2. Device A broadcasts an ARP request: *"Who has 192.168.1.50? Tell 192.168.1.1"*
3. The device with IP `192.168.1.50` responds with a unicast ARP reply containing its MAC address
4. Device A caches this IP→MAC mapping in its ARP table and uses it for subsequent frames

The ARP cache has a TTL — entries expire after a period of inactivity and must be re-learned. Under normal steady-state conditions, the ARP cache is warm and lookups are instant. The first packet to a new destination may be dropped while ARP resolves.

### IP Address Structure

IP addresses are 32 bits divided into two variable-length fields:


[ Network identifier | Host identifier ]


The dividing point between network and host is not fixed — it depends on the subnet mask in use. This variable-length structure is what makes routing table lookups more complex than MAC table lookups:

- MAC lookup: exact match on a fixed 48-bit field
- IP lookup: longest prefix match on a variable-length network portion of a 32-bit field

A routing table can contain entries ranging from a /0 (default route, matches everything) to a /32 (host-specific route, matches exactly one IP address). The router always selects the most specific (longest) matching prefix.

---

## 7. Fragmentation

### What Is It?

Every network interface has an MTU — the maximum frame size it will accept. When a router must forward a packet out an interface whose MTU is smaller than the packet itself, the packet must be **fragmented**: broken into multiple smaller pieces, each small enough to fit within the MTU, each independently routed to the destination.

At the destination host, IP reassembles the fragments back into the original packet before passing it up to the transport layer (TCP/UDP). Intermediate routers do not reassemble — they only fragment further if needed.

### Why It's Expensive

- **CPU overhead** — every device that fragments must compute new headers and checksums for each fragment
- **Out-of-order arrival** — fragments travel independently and may arrive in any order; the destination must buffer and reorder them
- **Fragment loss** — if even one fragment of a packet is lost, the entire original packet must be retransmitted. TCP will detect the loss and retransmit, but the retransmitted packet may be fragmented again
- **Amplification** — a single large packet can become many fragments, each consuming header overhead and switch/router processing

### Why Bridges Cannot Fragment

Bridges (and pure L2 switches) operate only at Layer 2. Fragmentation and reassembly is an IP (Layer 3) function — it requires understanding IP headers, fragment offsets, and the ability to reorder and reassemble. A bridge has none of this; it only sees frames. If a frame is too large for the outgoing interface, a bridge simply drops it.

### Best Practice: Path MTU Discovery

Rather than relying on intermediate devices to fragment on the fly, the preferred approach is **Path MTU Discovery (PMTUD)**:

1. The sending host sends packets with the "Don't Fragment" (DF) bit set in the IP header
2. If an intermediate router cannot forward the packet without fragmenting, it drops it and sends an ICMP "Fragmentation Needed" message back to the sender, including the MTU of the blocking interface
3. The sender reduces its packet size to fit and retransmits

This way, fragmentation never actually occurs — the sender learns the bottleneck MTU and sizes its packets appropriately from the start. The processing cost is paid once at session setup rather than on every packet.

> Avoid fragmentation in your network design wherever possible. Engineer your MTUs so that packets can traverse the entire path from source to destination without ever needing to be broken up.

---

## Quick Reference Tables

### Switching Methods
| Method | Reads | CRC | Size | Latency | Best for |
|---|---|---|---|---|---|
| Store-and-forward | Full frame | Yes | Yes | High | Access layer |
| Cut-through | First 6 bytes | No | No | Low | Core layer |
| Fragment-free | First 64 bytes | No | Runts only | Medium | General use |

### Transmission Types
| Type | Scope | MAC destination | Crossed by routers? |
|---|---|---|---|
| Unicast | One device | Specific MAC | Yes |
| Multicast | Group of devices | Group MAC | Yes (with multicast routing) |
| Broadcast | All devices on segment | `FF-FF-FF-FF-FF-FF` | No |

### L2 vs L3 Devices
| Feature | L2 Switch | L3 Switch | Router |
|---|---|---|---|
| Forwarding basis | MAC | IP | IP |
| Speed | Wire | Wire | Variable |
| Fragments? | No | Yes | Yes |
| Media transition? | No | Yes | Yes |
| Routing protocols? | No | Limited | Full |
| Blocks broadcasts? | No | Yes | Yes |
