# Computer Networks - Exam Questions (Synthetic & Realistic Exam 2)
*Computer Networks - Synthetic & Realistic Exam 2*

## Exam Information
- **Academic Year:** .......................
- **Exam Duration:** 2 hours and 15 minutes

## Student Data
- **Full Name:** ______________________________________________________
- **Registration Number (AM):** __________________

---

## Part A: Multiple Choice & Theory Questions (3 points)

**1.** Which of the following belongs exclusively to the Network Core?
- [ ] A. Web Servers
- [✓] B. Routers
- [ ] C. Mobile phones
- [ ] D. Email Applications (Clients)

*Justification:* The core consists of routers and switches (the network of networks). Web servers, mobile phones, and apps are located at the Network Edge.

**2.** According to the Longest Prefix Match (LPM) rule, when a destination address matches multiple entries in a forwarding table, which entry is selected?
- [ ] A. The entry with the smallest number of prefix bits.
- [✓] B. The entry with the largest number of prefix bits.
- [ ] C. The default route.
- [ ] D. The first entry found in the table.

*Justification:* Longest Prefix Match means the "longest prefix in length" that matches. It is the most specific.

**3.** The Data Plane of a router is responsible for:
- [ ] A. Executing Dijkstra's algorithm.
- [✓] B. Physical forwarding of packets from input to the appropriate output.
- [ ] C. Exchanging OSPF messages with other routers.
- [ ] D. Maintaining the Routing Table (RIB).

*Justification:* The Data plane operates at hardware speed for fast forwarding. The Control plane handles routing algorithms and table creation.

**4.** The "Count-to-Infinity" problem is a known vulnerability in routing algorithms of type:
- [ ] A. Link State
- [✓] B. Distance Vector
- [ ] C. Longest Prefix Match
- [ ] D. CSMA/CD

*Justification:* In Distance Vector algorithm, if a link breaks, nodes may exchange outdated routing info with each other increasing the assumed cost to infinity.

**5.** Select True (T) or False (F):
- **[✓] T** / [ ] F TCP uses cumulative acknowledgements (cumulative ACKs).
- [ ] T / **[✓] F** A Tier-1 ISP typically pays for traffic exchange (transit) with other Tier-1 ISPs.
- **[✓] T** / [ ] F A Layer 2 Switch separates collision domains but not broadcast domains.

*Justification:*
- **T (True):** TCP acknowledges data cumulatively.
- **F (False):** Tier-1 ISPs offer free peering to each other.
- **T (True):** L2 switch separates collision domains, keeps broadcast domain intact.

---

## Part B: Exercises and Networks (7 points)

### Exercise 1 (2 points)
**Longest Prefix Match (LPM)**
Given the following forwarding table of a router:

| Network Prefix | Interface |
|---|---|
| 10.20.0.0/16 | Eth0 |
| 10.20.30.0/24 | Eth1 |
| 10.20.30.64/26 | Eth2 |
| 0.0.0.0/0 (Default) | Eth3 |

To which Interface (Eth0, Eth1, Eth2, or Eth3) will packets with the following destination IP addresses be forwarded? Justify your answer.

1. **IP:** 10.20.30.100
2. **IP:** 10.20.31.5
3. **IP:** 10.21.5.1
4. **IP:** 10.20.30.20

---
**Answers:**
The LPM rule dictates that packets are forwarded based on longest prefix match.
- `10.20.0.0/16` covers from 10.20.0.0 to 10.20.255.255
- `10.20.30.0/24` covers from 10.20.30.0 to 10.20.30.255
- `10.20.30.64/26` covers from 10.20.30.64 to 10.20.30.127

1. **IP: 10.20.30.100** $\rightarrow$ `Eth2` (Matches /16, /24, and /26. Applying LPM, /26 is selected).
2. **IP: 10.20.31.5** $\rightarrow$ `Eth0` (Matches /16, but not /24 or /26).
3. **IP: 10.21.5.1** $\rightarrow$ `Eth3` (Matches no specific prefix, thus goes to default 0.0.0.0/0).
4. **IP: 10.20.30.20** $\rightarrow$ `Eth1` (Matches /16 and /24. Does not match /26 since it is below 64).

---

### Exercise 2 (2.5 points)
**Distance Vector Routing (Bellman-Ford)**
In a network using the Bellman-Ford (Distance Vector) algorithm, router X has the following neighbors: Y (cost=3), Z (cost=2), W (cost=4).

Router X receives the following routing tables from its neighbors regarding the cost to reach destination node **D**:
- From Y: Cost to D = 5
- From Z: Cost to D = 6
- From W: Cost to D = 2

**a.** What is the new calculated cost from node X to D? Show your calculations.
**b.** Via which neighbor (Next-Hop) will X route its packets to D?

---
**Answers:**
**a.** Bellman-Ford algorithm calculates: $d_x(D) = \min_{v} \{ c(x,v) + d_v(D) \}$
- Via Y: $c(X,Y) + d_Y(D) = 3 + 5 = 8$
- Via Z: $c(X,Z) + d_Z(D) = 2 + 6 = 8$
- Via W: $c(X,W) + d_W(D) = 4 + 2 = 6$

Minimum cost is $\min \{8, 8, 6\} = \mathbf{6}$.
So, the new cost to D is **`6`**.

**b.** Minimum cost was achieved via node W.
Therefore, Next-Hop for destination D is node **`W`**.

---

### Exercise 3 (2.5 points)
**ARP across a Router & BDP**

**a.** Consider the topology below. Computer A (Client) wants to send an IP packet to computer B (Server).

```
[ Computer A ] ------------------ [ Router R ] ------------------ [ Computer B ]
 IP: 10.0.0.5                       IP_Left: 10.0.0.1                    IP: 192.168.1.10
 MAC: 00:AA:11:22:33:44             MAC_Left: 00:RR:AA:BB:CC:01          MAC: 00:BB:99:88:77:66
                                    IP_Right: 192.168.1.1
                                    MAC_Right: 00:RR:AA:BB:CC:02
```

Computer A knows B's IP (via DNS), but its ARP Cache is empty.
- **i.** What ARP request must computer A make (Specify Sender IP, Sender MAC, Target IP)? What will be the Destination MAC in the Layer 2 Ethernet Frame of the ARP message?
- **ii.** When the actual data IP packet departs from router R towards computer B, what are its header fields? (Specify Source IP, Destination IP, Source MAC, Destination MAC).

---
**Answers:**
**i.** Computer A searches for its gateway's MAC address (Router R), since B is on an external network.
- Sender IP: `10.0.0.5`
- Sender MAC: `00:AA:11:22:33:44`
- Target IP: `10.0.0.1` (IP of the left side of R)
- Destination MAC in Ethernet Frame: `FF:FF:FF:FF:FF:FF` (Broadcast)

**ii.** Exiting router R towards B:
- Source IP: `10.0.0.5` (remains original IP of A)
- Destination IP: `192.168.1.10` (remains IP of B)
- Source MAC: `00:RR:AA:BB:CC:02` (MAC of right side of R)
- Destination MAC: `00:BB:99:88:77:66` (MAC of B)

**b.** An intercontinental link has a propagation speed of $2 \times 10^8$ m/s and cable length of $4,000$ km. Data transmission rate (Bandwidth) is $R = 1$ Gbps ($10^9$ bps).

- **i.** What is the propagation delay ($d_{prop}$)?
- **ii.** What is the maximum number of bits that can be present inside the cable at any given moment (BDP)?

---
**Answers:**
**i.** $$ d_{prop} = \frac{d}{s} = \frac{4,000 \times 10^3\text{ m}}{2 \times 10^8\text{ m/s}} = \frac{4 \times 10^6}{2 \times 10^8} = 0.02\text{ s} = `20\text{ ms}` $$

**ii.** $$ \text{BDP} = R \times d_{prop} = 10^9\text{ bps} \times 0.02\text{ s} = `20,000,000\text{ bits}` \text{ (or 20 Mbits)} $$