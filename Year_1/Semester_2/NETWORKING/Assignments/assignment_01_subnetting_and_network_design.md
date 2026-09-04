# Assignment 01: Enterprise VLSM Subnetting and IP Addressing Design

## Objective
Design an optimal, non-overlapping hierarchical IPv4 addressing plan for an enterprise campus network using Variable Length Subnet Masking (VLSM), formulate router forwarding tables, and configure static route aggregation.

---

## Network Topology Scenario
An enterprise has been assigned the private address block `172.20.0.0/16`. The organization comprises four regional branches and three inter-router point-to-point serial links connecting the sites.

### Host Requirements per Department:
1. **Engineering Department (HQ)**: 450 hosts
2. **Operations & Finance**: 210 hosts
3. **Data Center & Servers**: 110 hosts
4. **Customer Support Call Center**: 55 hosts
5. **Research Lab**: 28 hosts
6. **Executive Management**: 12 hosts
7. **WAN Link 1 (HQ to Branch 1)**: 2 IP addresses (point-to-point)
8. **WAN Link 2 (HQ to Branch 2)**: 2 IP addresses (point-to-point)
9. **WAN Link 3 (Branch 1 to Branch 2)**: 2 IP addresses (point-to-point)

---

## Assignment Requirements

### 1. VLSM Addressing Table
Construct a complete addressing table sorted in descending order of size:
| Subnet Name | Needed Hosts | Allocated Hosts | Subnet Mask (Dotted Decimal) | CIDR Prefix | Network Address | First Usable Host | Last Usable Host | Broadcast Address |
|---|---|---|---|---|---|---|---|---|

### 2. Router Routing Table Construction
Construct the routing table for the Central HQ Router connecting the Engineering, Operations, Data Center subnets, and WAN links 1 and 2.
Include fields: `Destination Network`, `Subnet Mask`, `Next-Hop IP Address`, `Exit Interface`, `Metric`.

### 3. Route Aggregation (Supernetting)
Calculate the most compact summary route that encompasses the Customer Support, Research Lab, and Executive Management subnets without announcing unallocated address space.

---

## Deliverables & Grading Rubric
| Criterion | Description | Points |
|---|---|---|
| VLSM Sizing & Block Alignment | Correct power-of-two host allocations with zero overlapping boundaries | 35 |
| Address Boundary Precision | Accurate Network, First/Last Usable, and Broadcast IPs across all 9 subnets | 35 |
| Router Forwarding Tables | Valid routing table entries, correct next-hops, and default gateway logic | 20 |
| CIDR Route Summarization | Minimal supernet calculation with binary prefix alignment derivation | 10 |
| **Total** | | **100** |

