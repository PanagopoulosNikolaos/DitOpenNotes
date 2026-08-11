# Computer Networks - Exam Questions (Synthetic Exam 2)
*Computer Networks - Synthetic Exam 2*

## Exam Information
- **Academic Year:** .......................
- **Exam Duration:** 2 hours and 15 minutes

## Student Data
- **Full Name:** ______________________________________________________
- **Registration Number (AM):** __________________

---

## Part A: Multiple Choice & Theory Questions (3 points)

**1.** According to the Longest Prefix Match (LPM) rule, when a destination address matches multiple entries in a forwarding table, which entry is selected?
- [ ] A. The entry with the smallest number of prefix bits.
- [✓] B. The entry with the largest number of prefix bits.
- [ ] C. The default route.
- [ ] D. The first entry found in the table.

*Justification:* Longest Prefix Match means the "longest prefix in length" that matches. It is the most specific.

**2.** Queuing delay in a router:
- [ ] A. Depends exclusively on distance between two nodes.
- [ ] B. Is constant and calculated as $L/R$.
- [✓] C. Depends on packet arrival rate (traffic load) and varies continuously.
- [ ] D. Is due to error check (checksum) time.

*Justification:* Queuing delay depends exclusively on traffic intensity at the router at a given moment. It is not constant like transmission delay.

**3.** Which of the following belongs exclusively to the Network Core?
- [ ] A. Web Servers
- [✓] B. Routers
- [ ] C. Mobile phones
- [ ] D. Email Applications (Clients)

*Justification:* The core consists of routers and switches (the network of networks). Web servers, mobile phones, and apps are located at the Network Edge.

**4.** The Data Plane of a router is responsible for:
- [ ] A. Executing Dijkstra's algorithm.
- [✓] B. Physical forwarding of packets from input to the appropriate output.
- [ ] C. Exchanging OSPF messages with other routers.
- [ ] D. Maintaining the Routing Table (RIB).

*Justification:* The Data plane operates at hardware speed for fast forwarding. The Control plane handles routing algorithms and table creation.

**5.** Select True (T) or False (F):
- **[✓] T** / [ ] F TCP uses cumulative acknowledgements (cumulative ACKs).
- [ ] T / **[✓] F** A Tier-1 ISP typically pays for traffic exchange (transit) with other Tier-1 ISPs.
- **[✓] T** / [ ] F A Layer 2 Switch separates collision domains but not broadcast domains.

*Justification:*
- **T (True):** TCP acknowledges data cumulatively (cumulative ACK indicates next expected sequence number).
- **F (False):** Tier-1 ISPs offer free peering to each other and do NOT pay transit to anyone.
- **T (True):** An L2 switch separates collision domains (each port is separate), but forwards broadcasts (e.g. ARP requests) to all ports, keeping them in the same broadcast domain.

---

## Part B: Exercises and Networks (7 points)

### Exercise 1 (2 points)
**Longest Prefix Match (LPM)**
Given the following forwarding table of a router:

| Network Prefix | Interface |
|---|---|
| 10.15.0.0/16 | Eth0 |
| 10.15.20.0/24 | Eth1 |
| 10.15.20.128/25 | Eth2 |
| 0.0.0.0/0 (Default) | Eth3 |

To which Interface (Eth0, Eth1, Eth2, or Eth3) will packets with the following destination IP addresses be forwarded? Justify your answer.

1. **IP:** 10.15.20.200
2. **IP:** 10.15.21.5
3. **IP:** 10.16.5.1
4. **IP:** 10.15.20.50

---
**Answers:**
The LPM rule dictates that packets are forwarded based on longest prefix match.
- `10.15.0.0/16` covers from 10.15.0.0 to 10.15.255.255
- `10.15.20.0/24` covers from 10.15.20.0 to 10.15.20.255
- `10.15.20.128/25` covers from 10.15.20.128 to 10.15.20.255

1. **IP: 10.15.20.200** $\rightarrow$ `Eth2` (Matches /16, /24, and /25. Applying LPM, /25 is selected).
2. **IP: 10.15.21.5** $\rightarrow$ `Eth0` (Matches /16, but not /24 or /25).
3. **IP: 10.16.5.1** $\rightarrow$ `Eth3` (Matches no specific prefix, thus goes to default 0.0.0.0/0).
4. **IP: 10.15.20.50** $\rightarrow$ `Eth1` (Matches /16 and /24. Does not match /25 since it is below 128).

---

### Exercise 2 (2.5 points)
**Dijkstra Algorithm**
Consider the network below, where numbers represent transmission cost between nodes:

```
      (A) --- 3 --- (B) --- 1 --- (C)
       |             |             |
       5             2             4
       |             |             |
      (D) --- 1 --- (E) --- 2 --- (F)
```

Apply Dijkstra's algorithm starting from **node D** and find the shortest path for all other nodes. Fill in the table (number shows current minimum cost and in parentheses the previous node, e.g., 5(D)).

| Step | Visited | A | B | C | E | F |
|---|---|---|---|---|---|---|
| 0 | D | `5(D)` | `\infty` | `\infty` | `1(D)` | `\infty` |
| 1 | `D, E` | `5(D)` | `3(E)` | `\infty` | `**1(D)**` | `3(E)` |
| 2 | `D, E, B` | `5(D)` | `**3(E)**` | `4(B)` | `1(D)` | `3(E)` |
| 3 | `D, E, B, F` | `5(D)` | `3(E)` | `4(B)` | `1(D)` | `**3(E)**` |
| 4 | `D, E, B, F, C` | `5(D)` | `3(E)` | `**4(B)**` | `1(D)` | `3(E)` |
| 5 | `D, E, B, F, C, A` | `**5(D)**` | `3(E)` | `4(B)` | `1(D)` | `3(E)` |

*Note on step 1: E connects to B (1+2=3), and to F (1+2=3).*
*Note on step 2: B connects to A (3+3=6, but 5(D) is smaller) and to C (3+1=4).*

What is the shortest path from node D to node C and what is its cost?
---
**Answer:**
Recursively: C connects optimally via B, B via E, E via D.
- Path: **`D ➔ E ➔ B ➔ C`**
- Total cost: **`4`**

---

### Exercise 3 (2.5 points)
**a. EstimatedRTT Calculation in TCP (1 point)**
Calculations for EstimatedRTT in TCP use the formula:
$$\text{EstimatedRTT} = (1 - \alpha) \cdot \text{EstimatedRTT} + \alpha \cdot \text{SampleRTT}$$
Suppose initial $\text{EstimatedRTT}$ is $100\text{ ms}$ and $\alpha = 0.125$. 
TCP receives 2 consecutive SampleRTTs: $120\text{ ms}$ and then $80\text{ ms}$. 
Calculate the new value of $\text{EstimatedRTT}$ after the second sample.

---
**Answer:**
$$ \text{EstimatedRTT}_{0} = 100\text{ ms} $$
After 1st sample ($\text{SampleRTT} = 120\text{ ms}$):
$$ \text{EstimatedRTT}_{1} = (1 - 0.125) \cdot 100 + 0.125 \cdot 120 = 87.5 + 15 = 102.5\text{ ms} $$
After 2nd sample ($\text{SampleRTT} = 80\text{ ms}$):
$$ \text{EstimatedRTT}_{2} = 0.875 \cdot 102.5 + 0.125 \cdot 80 = 89.6875 + 10 = `99.6875\text{ ms}` $$

**b. CSMA/CD Minimum Frame Size (1.5 points)**
In a Local Area Network (LAN) using CSMA/CD protocol with transmission rate (Bandwidth) $R = 100\text{ Mbps}$, the total propagation delay between the two furthest nodes (end-to-end propagation delay) is $d_{prop} = 5.12\ \mu\text{s}$.
Find the minimum frame size in Bytes for collision detection mechanism to operate correctly. (Reminder: Transmission time must be at least twice the maximum propagation time).

---
**Answer:**
CSMA/CD operating condition:
$$ d_{trans} \ge 2 \cdot d_{prop} \Rightarrow \frac{L_{min}}{R} \ge 2 \cdot d_{prop} \Rightarrow L_{min} \ge 2 \cdot d_{prop} \cdot R $$
With $d_{prop} = 5.12 \times 10^{-6}\text{ s}$ and $R = 100 \times 10^6\text{ bps}$:
$$ L_{min} \ge 2 \cdot (5.12 \times 10^{-6}) \cdot (100 \times 10^6) = 1024\text{ bits} $$
In Bytes:
$$ L_{min\text{ (Bytes)}} = \frac{1024}{8} = `128\text{ Bytes}` $$
