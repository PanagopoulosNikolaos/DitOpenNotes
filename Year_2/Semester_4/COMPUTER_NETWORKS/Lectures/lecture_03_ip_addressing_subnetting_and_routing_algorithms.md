# Lecture 03: IP Addressing, CIDR Subnetting, and Routing Algorithms

This lecture examines the network layer: IPv4 datagram formats, Classless Inter-Domain Routing (CIDR) subnetting algorithms, longest prefix matching, and fundamental routing algorithms (Link-State / Dijkstra vs. Distance-Vector / Bellman-Ford).

---

## 1. Network Layer Responsibilities

The network layer provides host-to-host communication through two distinct functions:
- **Forwarding (Data Plane):** Moving arriving packets from router input interface to appropriate output interface based on forwarding table lookup. Executed in hardware ($O(\text{nanoseconds})$).
- **Routing (Control Plane):** Network-wide logic coordinating routing protocols (OSPF, BGP) to determine end-to-end paths between sources and destinations. Executed in software.

---

## 2. IPv4 Addressing and CIDR Subnetting

An IPv4 address consists of 32 bits (4 octets) written in dotted-decimal format:

$$
\text{192.168.1.1} \iff \text{11000000.10101000.00000001.00000001}_2
$$

### 2.1 CIDR (Classless Inter-Domain Routing)
An address is represented as `a.b.c.d/x`, where $x$ specifies the number of bits in the **Network Prefix**:
- **Prefix ($x$ bits):** Identifies the subnet.
- **Host identifier ($32 - x$ bits):** Identifies the specific host interface on that subnet.

### 2.2 Subnet Mathematical Calculations
For a subnet with prefix length $x$:
- **Subnet Mask:** $x$ leading ones followed by $32 - x$ zeros.
- **Total IP Addresses:** $2^{32 - x}$.
- **Usable Host Addresses:** $2^{32 - x} - 2$.
  - All host bits $= 0$: **Network Address** (identifies the subnet).
  - All host bits $= 1$: **Directed Broadcast Address** (targets all hosts on the subnet).
- **Network Address Formula:** Perform bitwise AND between any host IP and the subnet mask:

$$
\text{Network Address} = \text{IP Address} \ \& \ \text{Subnet Mask}
$$

### 2.3 Longest Prefix Matching
When a router receives a packet with destination address $D$, it compares $D$ against all entries in its forwarding table. If multiple entries match, the router forwards to the interface matching the **longest prefix** (most specific network mask):

| Destination Prefix | Next Hop Interface |
|---|---|
| `192.168.1.0/24` | `eth0` |
| `192.168.1.128/25` | `eth1` |
| `0.0.0.0/0` (Default) | `eth2` |

- Packet to `192.168.1.130`: matches both `/24` and `/25`. Routed to `eth1` (longest prefix length 25).
- Packet to `192.168.1.20`: matches `/24`. Routed to `eth0`.
- Packet to `10.0.0.1`: matches only default route. Routed to `eth2`.

---

## 3. Link-State Routing: Dijkstra's Algorithm

Link-State protocols (e.g., OSPF) require every router to possess a global, complete topology map of the network graph $G = (V, E)$.

### 3.1 Algorithm Formulation
Let $c(u, v)$ be the link cost between adjacent nodes $u$ and $v$. If $(u, v) \notin E$, $c(u, v) = \infty$.
- $D(v)$: Current estimated cost of the least-cost path from source $u$ to destination $v$.
- $p(v)$: Previous node along the current best path to $v$.
- $N'$: Subset of nodes whose least-cost paths have been definitively determined.

**Algorithm Steps:**
1. **Initialization:**
   $$N' = \{u\}$$
   $$\forall v \notin N': D(v) = c(u, v), \quad p(v) = u \text{ if } c(u, v) < \infty \text{ else undefined}$$
2. **Loop:**
   - Find $w \notin N'$ such that $D(w) = \min_{v \notin N'} D(v)$.
   - Add $w$ to $N'$: $N' \leftarrow N' \cup \{w\}$.
   - Update $D(v)$ for all adjacent neighbors $v \notin N'$:
     $$D(v) \leftarrow \min(D(v), D(w) + c(w, v))$$
3. **Termination:** When $N' = V$.

**Complexity:** $O(|V|^2)$ with array implementation; $O((|V| + |E|) \log |V|)$ using a binary min-heap.

---

## 4. Distance-Vector Routing: Bellman-Ford Algorithm

Distance-Vector protocols (e.g., RIP) operate in a decentralized, iterative fashion: each node communicates only with its directly connected physical neighbors.

### 4.1 Bellman-Ford Optimality Equation
Let $d_x(y)$ be the cost of the least-cost path from node $x$ to node $y$:

$$
d_x(y) = \min_{v \in \text{neighbors}(x)} \left\{ c(x, v) + d_v(y) \right\}
$$

```
   (x) --- c(x, v) ---> (v) ===== d_v(y) =====> (y)
```

### 4.2 Distance-Vector Protocol Mechanics
1. Each node maintains its own distance vector $D_x = [D_x(y) : y \in V]$.
2. Periodically, or upon local link cost change, node $x$ transmits $D_x$ to direct neighbors.
3. Upon receiving neighbor $v$'s vector $D_v$, node $x$ computes:
   $$D_x(y) \leftarrow \min_{w} \left\{ c(x, w) + D_w(y) \right\}$$
4. If $D_x(y)$ changes, node $x$ advertises its new vector to all neighbors.

### 4.3 Count-to-Infinity Problem
When link costs increase or links fail, routing loops can emerge where nodes iteratively inflate costs ($1 \to 2 \to 3 \to \dots \to \infty$).
- **Mitigation 1: Split Horizon:** If node $x$ routes to destination $y$ via neighbor $z$, node $x$ suppresses advertising its route to $y$ back to $z$.
- **Mitigation 2: Poison Reverse:** Node $x$ explicitly advertises $D_x(y) = \infty$ to neighbor $z$.
- **Mitigation 3: Hop Count Limit:** RIP caps infinity at 16 hops.

