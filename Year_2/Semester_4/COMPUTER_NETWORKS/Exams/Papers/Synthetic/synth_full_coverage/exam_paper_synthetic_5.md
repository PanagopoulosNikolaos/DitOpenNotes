# Computer Networks - Exam Questions (Synthetic Exam 5)
*Computer Networks - Synthetic Exam 5*

## Exam Information
- **Academic Year:** .......................
- **Exam Duration:** 2 hours and 15 minutes

## Student Data
- **Full Name:** ______________________________________________________
- **Registration Number (AM):** __________________

---

## Part A: Multiple Choice & Theory Questions (3 points)

**1.** In the "Encapsulation" process, when data is passed from the Application Layer down to the Physical Layer:
- [ ] A. Headers are removed at each layer.
- [ ] B. Data is obligatorily encrypted by the Data Link Layer.
- [✓] C. A new header is added at each layer, finally creating the frame at Layer 2.
- [ ] D. The recipient IP address changes at each layer.

*Justification:* Encapsulation means higher layer data becomes payload for the lower layer, receiving a new header. De-encapsulation occurs at the receiver.

**2.** What is the main difference between a Collision Domain and a Broadcast Domain?
- [ ] A. There is no difference, they are synonymous.
- [✓] B. A Router separates Broadcast Domains, while a Switch separates Collision Domains.
- [ ] C. A Router separates Collision Domains, while a Switch separates Broadcast Domains.
- [ ] D. A Hub separates Collision Domains.

*Justification:* Switches divide networks into collision-free micro-segments, but forward broadcasts. Only Routers stop broadcast packets.

**3.** The Dijkstra algorithm calculates shortest paths using:
- [ ] A. Hop count alone.
- [✓] B. Full knowledge of topology and costs of all network links (Link State).
- [ ] C. Information received exclusively from immediate neighbors (Distance Vector).
- [ ] D. MAC Addresses exclusively.

*Justification:* Dijkstra requires the full network map to find shortest paths from source.

**4.** If a video streaming flow sends 1,000 packets per second and each packet size is 1,000 Bytes, the minimum required transmission rate (Bandwidth) without loss is:
- [ ] A. 1 Mbps
- [✓] B. 8 Mbps
- [ ] C. 1 Gbps
- [ ] D. 8 Gbps

*Justification:* $1,000\text{ pkts/sec} \times 1,000\text{ Bytes/pkt} = 1,000,000\text{ Bytes/sec} = 8\text{ Mbps}$.

**5.** Select True (T) or False (F):
- **[✓] T** / [ ] F The OSPF protocol supports Hierarchical Routing through division into Areas.
- [ ] T / **[✓] F** In Circuit Switching, if the user is idle, bandwidth is automatically utilized by other users.
- **[✓] T** / [ ] F ARP Reply messages are sent as Unicast to the requesting node.

*Justification:*
- **T (True):** OSPF divides large networks into Areas (e.g. Area 0) to reduce overhead.
- **F (False):** In Circuit Switching, if idle, resources remain reserved and wasted.
- **T (True):** ARP Request is Broadcast, ARP Reply is always Unicast to the requester.

---

## Part B: Exercises and Networks (7 points)

### Exercise 1 (2 points)
**Hamming Code (Odd Parity)**
A sender wishes to transmit data message `0110` using Hamming error-correcting code.

**a.** What is the required number of parity bits ($p$)?
**b.** Form the complete message to be sent, assuming the use of **odd parity**. Show the calculation for each parity bit in detail.

---
**Answers:**
**a.** $$2^p \ge d + p + 1 \Rightarrow 2^p \ge 4 + p + 1 \Rightarrow 2^p \ge p + 5$$
For $p=3$: $2^3 = 8 \ge 8$. So **$p = `3`$** bits.

**b.** 7 bits total.
Parity positions: 1, 2, 4. Data positions: 3, 5, 6, 7.

| Position | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| Bit | $P_1$ | $P_2$ | $D_1$ | $P_4$ | $D_2$ | $D_3$ | $D_4$ |
| Value | `0` | `0` | `0` | `1` | `1` | `1` | `0` |

Calculation of bits (Odd Parity means the total number of '1' bits in the check group must be odd):
- **$P_1$ (positions 1, 3, 5, 7):** $P_1 \oplus D_1 \oplus D_2 \oplus D_4 = P_1 \oplus 0 \oplus 1 \oplus 0 = P_1 \oplus 1$.
  To have an odd number of ones, $P_1 = `0`$.
- **$P_2$ (positions 2, 3, 6, 7):** $P_2 \oplus D_1 \oplus D_3 \oplus D_4 = P_2 \oplus 0 \oplus 1 \oplus 0 = P_2 \oplus 1$.
  Similarly, $P_2 = `0`$.
- **$P_4$ (positions 4, 5, 6, 7):** $P_4 \oplus D_2 \oplus D_3 \oplus D_4 = P_4 \oplus 1 \oplus 1 \oplus 0 = P_4 \oplus 2$.
  We have 2 ones (even). To make it odd, we need a 1 bit. So $P_4 = `1`$.

Final transmitted message: **`0001110`**

---

### Exercise 2 (2.5 points)
**End-to-End Delay with Processing**
Consider the path from Computer A to Computer B passing through 2 Routers (total $N = 3$ hops).
Each of the 3 links has the following characteristics:
- Link length: $d = 2,000\text{ km}$
- Propagation speed: $s = 2 \times 10^8\text{ m/s}$
- Transmission Rate (Bandwidth): $R = 10\text{ Mbps}$

A packet of size $L = 20,000\text{ bits}$ is sent from A to B.
Additionally, each of the two intermediate Routers introduces a **Processing Delay** $d_{proc} = 1\text{ ms}$. 
There is no queuing delay (queuing delay = 0).

**a.** What is the transmission delay ($d_{trans}$) per hop?
**b.** What is the propagation delay ($d_{prop}$) per hop?
**c.** Calculate the total end-to-end delay from the moment transmission of the first bit starts from A until the last bit is received by B. Show formula and calculations.

---
**Answers:**
**a.** $$d_{trans} = \frac{L}{R} = \frac{20,000}{10 \times 10^6} = 0.002\text{ s} = `2\text{ ms}`$$

**b.** $$d_{prop} = \frac{d}{s} = \frac{2 \times 10^6\text{ m}}{2 \times 10^8\text{ m/s}} = 0.01\text{ s} = `10\text{ ms}`$$

**c.** The formula for store-and-forward of a packet over $N$ hops with processing delay at $N-1$ intermediate routers is:
$$ d_{total} = N \cdot d_{trans} + N \cdot d_{prop} + (N-1) \cdot d_{proc} $$
With $N = 3$ hops, we have $3-1 = 2$ intermediate routers:
$$ d_{total} = 3 \cdot (2\text{ ms}) + 3 \cdot (10\text{ ms}) + 2 \cdot (1\text{ ms}) $$
$$ d_{total} = 6\text{ ms} + 30\text{ ms} + 2\text{ ms} = `38\text{ ms}` $$

---

### Exercise 3 (2.5 points)
**RIP Configuration & Topology**
For the network in the figure below, Router "Router1" must be configured using the RIP version 2 protocol.

```
       192.168.10.0/24
             |
             | Fa0/0
      +-------------+
      |   Router1   |
      +-------------+
        /           \
 Se0/0/0           Se0/0/1
   /                   \
10.0.1.0/24          10.0.2.0/24
```

**a.** Fill in the blanks for the commands to activate RIPv2 in Cisco IOS:
```text
Router1> enable
Router1# configure terminal
Router1(config)# _________________________
Router1(config-router)# _________________________
Router1(config-router)# no auto-summary
Router1(config-router)# _________________________
Router1(config-router)# _________________________
Router1(config-router)# _________________________
Router1(config-router)# end
```

**b.** If a third router "Router3" is added to network 10.0.1.0/24 later and uses OSPF instead of RIP, will Router1 be able to "learn" Router3's routes via RIP without any other intervention? Justify.

---
**Answers:**
**a.** Completed CLI commands:
```text
Router1> enable
Router1# configure terminal
Router1(config)# `router rip`
Router1(config-router)# `version 2`
Router1(config-router)# no auto-summary
Router1(config-router)# `network 192.168.10.0`
Router1(config-router)# `network 10.0.1.0`
Router1(config-router)# `network 10.0.2.0`
Router1(config-router)# end
```

**b.** **`No`**, it will not be able to learn them. RIP and OSPF are two different routing protocols with different metrics (hop count vs cost) and algorithms (Distance Vector vs Link State). To communicate, manual configuration of **route redistribution** by an administrator is required on a router running both protocols (ASBR).
