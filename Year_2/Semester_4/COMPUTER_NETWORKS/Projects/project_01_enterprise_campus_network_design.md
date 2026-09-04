# Project 01: Multi-Tier Enterprise Campus Network Architecture

## Project Overview
Design, simulate, and validate an enterprise campus network infrastructure using Cisco Packet Tracer. The architecture implements a three-tier hierarchical model (Core, Distribution, Access), segregates traffic using IEEE 802.1Q VLANs, provides inter-VLAN routing, and implements Open Shortest Path First (OSPFv2) dynamic routing across redundant distribution multilayer switches.

---

## Architectural and Technical Specifications

```
                       [ ISP Edge Router ]
                                |
                        [ Core Router ]
                          /          \
                         /            \
          [ Distribution-1 ] ========= [ Distribution-2 ]  (OSPF Area 0)
                 |       \             /       |
                 |        \           /        |
          [ Access Switch 1 ]       [ Access Switch 2 ]   (802.1Q Trunks)
             /           \             /           \
        VLAN 10        VLAN 20     VLAN 30       VLAN 40
        (Admin)        (Faculty)   (Student)     (Servers)
```

### 1. Hierarchical Network Infrastructure
- **Core Layer:** Provides high-speed packet switching and connectivity to edge firewalls and external ISP links.
- **Distribution Layer:** Two multilayer switches configured with Hot Standby Router Protocol (HSRP) or Virtual Router Redundancy Protocol (VRRP) providing redundant default gateways for user VLANs.
- **Access Layer:** Layer 2 Catalyst switches enforcing port security, access controls, and VLAN port assignments.

### 2. IP Subnet Plan (CIDR / VLSM)
Supernet: `10.50.0.0/16`
- **VLAN 10 (Administration):** `10.50.10.0/24` (Gateway: `10.50.10.1`)
- **VLAN 20 (Faculty / Research):** `10.50.20.0/24` (Gateway: `10.50.20.1`)
- **VLAN 30 (Student Lab):** `10.50.30.0/23` (Gateway: `10.50.30.1`)
- **VLAN 40 (Data Center / Servers):** `10.50.40.0/26` (Gateway: `10.50.40.1`)
- **Point-to-point Router Links:** `10.50.254.0/30` subnets.

### 3. Core Protocol Configurations
- **Trunking:** IEEE 802.1Q trunking on all inter-switch uplinks.
- **Routing Protocol:** Single-area OSPFv2 (Area 0) active across Core and Distribution routers with loopback interfaces configured as router IDs.
- **DHCP Service:** Centralized DHCP server configured with exclusion pools for static infrastructure devices.

---

## Project Milestones

| Milestone | Deliverable | Target Verification |
|---|---|---|
| **Phase 1** | Topology Layout & Addressing Schema | Packet Tracer topology created; IP documentation table submitted |
| **Phase 2** | Layer 2 Switching & VLAN Trunking | Access ports assigned; trunks established; VLAN segregation verified |
| **Phase 3** | Inter-VLAN Routing & Dynamic OSPF | Switched Virtual Interfaces (SVIs) configured; OSPF neighbor adjacencies formed |
| **Phase 4** | DHCP, NAT & Service Verification | Dynamic host IP allocation verified; end-to-end ping testing across subnets |

---

## Grading Rubric

| Criterion | Evaluation Metric | Weight |
|---|---|---|
| **VLAN & Trunking Configuration** | Clean 802.1Q encapsulation, correct native VLANs, strict trunk pruning | 25% |
| **Routing Architecture & OSPF** | Full convergence, loop-free routing tables, correct metric assignments | 25% |
| **Addressing Efficiency (VLSM)** | Zero IP address overlap, accurate mask calculations, minimal wasted space | 20% |
| **Redundancy & Failover** | Automatic default gateway failover testing upon primary link shutdown | 15% |
| **Technical Documentation** | Clear network topology diagram, configuration transcripts, and verification output | 15% |

