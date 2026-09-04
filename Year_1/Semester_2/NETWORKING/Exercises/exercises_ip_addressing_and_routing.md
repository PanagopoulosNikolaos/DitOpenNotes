# Exercises: IP Addressing, Subnetting, and Routing Algorithms

## Context and Grounding
This practice exercise set provides comprehensive problems and worked solutions on IPv4 CIDR subnetting, wildcard masks, longest-prefix-match forwarding, and TCP sliding-window flow control. It directly reinforces `Lectures/lecture_02_ip_addressing_and_subnetting.md` and `Resources/Notes/5. Subnetting.md`.

---

## Problems

### Problem 1: Subnet Identification and Boundary Derivations
For the host IP address `192.168.45.138/27`:
1. What is the subnet mask in dotted-decimal format?
2. What is the network address of the subnet?
3. What is the directed broadcast address of the subnet?
4. What is the range of usable host IP addresses in this subnet?
5. How many total subnets and usable hosts per subnet are created if a `/24` network is divided into `/27` subnets?

### Problem 2: Longest Prefix Match Routing Lookup
A router has the following forwarding table:

| Destination Network Prefix | Next Hop | Interface |
|---|---|---|
| `0.0.0.0/0` (Default) | `10.1.1.1` | `eth0` |
| `172.16.0.0/12` | `10.2.1.1` | `eth1` |
| `172.24.0.0/14` | `10.3.1.1` | `eth2` |
| `172.26.0.0/16` | `10.4.1.1` | `eth3` |
| `172.26.32.0/20` | `10.5.1.1` | `eth4` |

Determine the next-hop IP and exit interface for each incoming destination IP packet:
1. Packet A: `172.26.35.12`
2. Packet B: `172.26.60.1`
3. Packet C: `172.25.10.5`
4. Packet D: `192.168.1.1`

### Problem 3: TCP Sliding Window Throughput Calculation
Two endpoints communicate across a cross-continental path with a Round-Trip Time (RTT) of $80\text{ ms}$. The bottleneck link bandwidth is $1\text{ Gbps}$ ($10^9\text{ bps}$). The sender and receiver negotiate a fixed TCP receive window size $rwnd = 64\text{ KB}$ ($65,536\text{ bytes}$) with no window scaling option enabled.
1. Calculate the Bandwidth-Delay Product (BDP) of the link.
2. What is the maximum theoretical throughput achievable by this TCP connection?
3. What window scale factor would be required to achieve full link utilization?

---

## Detailed Step-by-Step Solutions

### Solution 1
1. Prefix length $/27$ means 27 consecutive 1s followed by $32 - 27 = 5$ zeros:
   * Binary: `11111111.11111111.11111111.11100000`
   * Dotted-decimal: `255.255.255.224`
2. The block size in the 4th octet is $2^5 = 32$.
   * Subnet multiples in 4th octet: $0, 32, 64, 96, 128, 160, \dots$
   * Since $128 \le 138 < 160$, the network address is **`192.168.45.128`**.
3. Broadcast address is the last address in the block ($128 + 32 - 1$):
   * Broadcast address: **`192.168.45.159`**.
4. Usable host range:
   * First usable: Network $+ 1$ = **`192.168.45.129`**.
   * Last usable: Broadcast $- 1$ = **`192.168.45.158`**.
5. Dividing a $/24$ (8 host bits) into $/27$ (5 host bits):
   * Subnets created: $2^{27 - 24} = 2^3 = 8\text{ subnets}$.
   * Usable hosts per subnet: $2^5 - 2 = 32 - 2 = 30\text{ hosts}$.

### Solution 2
The router chooses the route matching the destination IP with the longest prefix length (most specific mask):

1. **Packet A (`172.26.35.12`)**:
   * Matches `0.0.0.0/0` (/0).
   * Matches `172.16.0.0/12` (/12) since $172.16 \dots 172.31$ are in range.
   * Matches `172.26.0.0/16` (/16).
   * Range for `172.26.32.0/20`: $32 \le 4\text{th octet} < 48$ (block size 16 in 3rd octet: $32 \dots 47$). Since $35 \in [32, 47]$, it matches `/20`.
   * **Longest Match:** `172.26.32.0/20`. **Next Hop:** `10.5.1.1`, **Interface:** `eth4`.

2. **Packet B (`172.26.60.1`)**:
   * Matches `0.0.0.0/0` (/0).
   * Matches `172.16.0.0/12` (/12).
   * Matches `172.26.0.0/16` (/16).
   * Does NOT match `172.26.32.0/20` because $60 \notin [32, 47]$.
   * **Longest Match:** `172.26.0.0/16`. **Next Hop:** `10.4.1.1`, **Interface:** `eth3`.

3. **Packet C (`172.25.10.5`)**:
   * Matches `0.0.0.0/0` (/0).
   * Matches `172.16.0.0/12` (/12).
   * Range for `172.24.0.0/14`: block size 4 ($172.24 \dots 172.27$). Since $25 \in [24, 27]$, it matches `/14`.
   * Does not match `172.26.0.0/16`.
   * **Longest Match:** `172.24.0.0/14`. **Next Hop:** `10.3.1.1`, **Interface:** `eth2`.

4. **Packet D (`192.168.1.1`)**:
   * Does not match any `172.*` route.
   * Matches only the default route `0.0.0.0/0`.
   * **Longest Match:** `0.0.0.0/0`. **Next Hop:** `10.1.1.1`, **Interface:** `eth0`.

### Solution 3
1. Bandwidth-Delay Product (BDP):
   $$\text{BDP} = \text{Bandwidth} \times \text{RTT} = 10^9 \text{ bps} \times 0.080 \text{ s} = 80,000,000 \text{ bits} = 10,000,000 \text{ bytes} \approx 10\text{ MB}$$
2. Maximum TCP throughput without window scaling is capped by window buffer:
   $$\text{Throughput}_{\max} = \frac{W_{\max}}{\text{RTT}} = \frac{65,536 \times 8 \text{ bits}}{0.080 \text{ s}} = \frac{524,288}{0.080} = 6,553,600 \text{ bps} \approx 6.55 \text{ Mbps}$$
   Notice that due to the $64\text{ KB}$ window constraint, the connection achieves less than $1\%$ of the $1\text{ Gbps}$ capacity!
3. To fully utilize the $1\text{ Gbps}$ pipeline, the window must equal or exceed BDP ($10\text{ MB} = 10,000,000\text{ bytes}$):
   $$\text{Window} = \text{Base Window} \times 2^S \ge 10,000,000$$
   $$65,536 \times 2^S \ge 10,000,000 \implies 2^S \ge \frac{10,000,000}{65,536} \approx 152.6 \implies S \ge 8$$
   A scale factor of $S = 8$ ($2^8 = 256$, yielding effective window $65,536 \times 256 = 16.7\text{ MB}$) enables $100\%$ link utilization.

