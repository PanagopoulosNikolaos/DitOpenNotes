# Computer Networks - Exam Questions (Synthetic Exam 3)
*Computer Networks - Synthetic Exam 3*

## Exam Information
- **Academic Year:** .......................
- **Exam Duration:** 2 hours and 15 minutes

## Student Data
- **Full Name:** ______________________________________________________
- **Registration Number (AM):** __________________

---

## Part A: Multiple Choice & Theory Questions (3 points)

**1.** The "Count-to-Infinity" problem is a known vulnerability in routing algorithms of type:
- [ ] A. Link State
- [✓] B. Distance Vector
- [ ] C. Longest Prefix Match
- [ ] D. CSMA/CD

*Justification:* In Distance Vector algorithm, if a link breaks, nodes may exchange outdated routing info with each other increasing the assumed cost to infinity.

**2.** "Hot-Potato Routing" in BGP protocol describes the practice where:
- [ ] A. The packet is dropped if it exceeds Time To Live (TTL).
- [✓] B. The AS tries to send the packet out of its network via the cheapest internal path (nearest egress).
- [ ] C. BGP always selects the path with fewest Autonomous Systems (AS-Path length).
- [ ] D. A packet loops indefinitely between two routers.

*Justification:* Hot-potato routing is applied in BGP when there are multiple egresses to the next AS and the network selects the one with the smallest internal IGP (e.g. OSPF) cost.

**3.** If a local area network uses exclusively Hubs instead of Switches, which of the following statements is correct?
- [✓] A. All nodes are in the same collision domain.
- [ ] B. Each port constitutes a separate collision domain.
- [ ] C. The Hub supports CSMA/CA, so collisions do not occur.
- [ ] D. The Hub operates at Layer 3 and performs routing.

*Justification:* A Hub repeats every bit to all ports, forming a single shared medium - thus a single collision domain.

**4.** The "Bandwidth-Delay Product" (BDP) represents:
- [ ] A. The data rate a router can process per second.
- [ ] B. The time required for frame change at the Physical Layer.
- [✓] C. The maximum number of bits that can be "in-flight" on the physical medium at any given time.
- [ ] D. The router queue size in packets.

*Justification:* $R \times d_{prop}$ gives the total volume of bits traveling "in-flight" within the communication channel.

**5.** Select True (T) or False (F):
- **[✓] T** / [ ] F A DNS request operates based on the Client-Server model.
- [ ] T / **[✓] F** The MAC address remains unchanged as a packet traverses multiple routers on the Internet, while the IP changes at each hop.
- **[✓] T** / [ ] F The RIP protocol has a maximum hop count of 15, making it unsuitable for huge networks.

*Justification:*
- **T (True):** Computer sends DNS Request (Client) and DNS server replies with matching address.
- **F (False):** Exactly the opposite occurs: IP remains constant (unless NAT is used), while MAC changes at each router hop.
- **T (True):** RIP uses hop count metric. If it reaches 15, 16 is considered infinity.

---

## Part B: Exercises and Networks (7 points)

### Exercise 1 (2 points)
**Distance Vector Routing (RIP) & Routing Tables**
In a network using the Bellman-Ford (Distance Vector) algorithm, router X has the following neighbors: Y (cost=2), Z (cost=5), W (cost=1). 

Router X receives the following routing tables from its neighbors regarding the cost to reach destination node **D**:
- From Y: Cost to D = 8
- From Z: Cost to D = 3
- From W: Cost to D = 10

**a.** What is the new calculated cost from node X to D? Show your calculations.
**b.** Via which neighbor (Next-Hop) will X route its packets to D?

---
**Answers:**
**a.** Bellman-Ford algorithm calculates: $d_x(D) = \min_{v} \{ c(x,v) + d_v(D) \}$
- Via Y: $c(X,Y) + d_Y(D) = 2 + 8 = 10$
- Via Z: $c(X,Z) + d_Z(D) = 5 + 3 = 8$
- Via W: $c(X,W) + d_W(D) = 1 + 10 = 11$

Minimum cost is $\min \{10, 8, 11\} = \mathbf{8}$.
So, the new cost to D is **`8`**.

**b.** Minimum cost was achieved via node Z.
Therefore, the Next-Hop for destination D is node **`Z`**.

---

### Exercise 2 (3 points)
**ARP across a Router**
Consider the topology below. Computer A (Client) wants to send an IP packet to computer B (Server).

```
[ Computer A ] ------------------ [ Router R ] ------------------ [ Computer B ]
 IP: 10.0.0.5                       IP_Left: 10.0.0.1                    IP: 192.168.1.10
 MAC: 00:AA:11:22:33:44             MAC_Left: 00:RR:AA:BB:CC:01          MAC: 00:BB:99:88:77:66
                                    IP_Right: 192.168.1.1                
                                    MAC_Right: 00:RR:AA:BB:CC:02         
```

Computer A knows B's IP (via DNS), but its ARP Cache is empty.
**a.** Computer A recognizes that B is not on the local network. What ARP request must computer A make (Specify Sender IP, Sender MAC, Target IP)? What will be the Destination MAC in the Layer 2 Ethernet Frame of the ARP message?
**b.** When the **actual data IP packet (not the ARP)** departs from router R towards computer B, what are its header fields? (Specify Source IP, Destination IP, Source MAC, Destination MAC).

---
**Answers:**
**a.** Computer A searches for its gateway's MAC address (Router R), since B is on an external network.
- Sender IP: `10.0.0.5`
- Sender MAC: `00:AA:11:22:33:44`
- Target IP: `10.0.0.1` (IP of the left side of R)
- Destination MAC in Ethernet Frame: `FF:FF:FF:FF:FF:FF` (Broadcast)

**b.** Exiting router R towards B:
- Source IP: `10.0.0.5` (remains original IP of A)
- Destination IP: `192.168.1.10` (remains IP of B)
- Source MAC: `00:RR:AA:BB:CC:02` (MAC of right side of R)
- Destination MAC: `00:BB:99:88:77:66` (MAC of B)

---

### Exercise 3 (2 points)
**BDP Product & Queuing Delay**

An intercontinental link has a propagation speed of $2 \times 10^8\text{ m/s}$ and cable length of $6,000\text{ km}$. Data transmission rate (Bandwidth) is $R = 1\text{ Gbps}$ ($10^9\text{ bps}$).

**a.** What is the propagation delay ($d_{prop}$)?
**b.** What is the maximum number of bits that can be present inside the cable at any given moment (BDP)?
**c.** If at an intermediate router, the queue buffer is filled with $1,000,000\text{ bytes}$ of traffic (from other connections) at the moment your new packet arrives, and the output rate is $1\text{ Gbps}$, how much time will pass (Queuing Delay - $d_{queue}$) before transmission of your packet begins?

---
**Answers:**
**a.** $$ d_{prop} = \frac{d}{s} = \frac{6,000 \times 10^3\text{ m}}{2 \times 10^8\text{ m/s}} = \frac{6 \times 10^6}{2 \times 10^8} = 0.03\text{ s} = `30\text{ ms}` $$

**b.** $$ \text{BDP} = R \times d_{prop} = 10^9\text{ bps} \times 0.03\text{ s} = `30,000,000\text{ bits}` \text{ (or 30 Mbits)} $$

**c.** Queue draining time ($1,000,000\text{ Bytes} = 8,000,000\text{ bits}$) at rate $1\text{ Gbps}$:
$$ d_{queue} = \frac{L_{queue}}{R_{out}} = \frac{8,000,000\text{ bits}}{10^9\text{ bps}} = 8 \times 10^{-3}\text{ s} = `8\text{ ms}` $$
