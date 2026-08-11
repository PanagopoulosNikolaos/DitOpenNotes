# Computer Networks - Exam Questions (Synthetic Exam 4)
*Computer Networks - Synthetic Exam 4*

## Exam Information
- **Academic Year:** .......................
- **Exam Duration:** 2 hours and 15 minutes

## Student Data
- **Full Name:** ______________________________________________________
- **Registration Number (AM):** __________________

---

## Part A: Multiple Choice & Theory Questions (3 points)

**1.** In a pure Peer-to-Peer (P2P) network, which of the following is true?
- [ ] A. Network reliability depends exclusively on a central Server (always-on).
- [ ] B. Adding new users always reduces available bandwidth.
- [✓] C. Each node (peer) operates simultaneously as a client and as a server.
- [ ] D. File sharing is impossible.

*Justification:* In P2P networks, nodes (peers) exchange resources directly, requesting (as client) and offering (as server).

**2.** Transmission delay ($d_{trans}$) of a packet of size $L$ on a link of capacity $R$ is calculated as:
- [✓] A. $L / R$
- [ ] B. $R / L$
- [ ] C. $\text{Distance} / \text{Speed of Light}$
- [ ] D. $\text{Distance} / R$

*Justification:* Transmission delay depends on packet size $L$ (bits) and link rate $R$ (bits/sec).

**3.** Which of the following IP addresses belongs to the same subnet as $192.168.10.55/26$?
- [ ] A. 192.168.10.65
- [✓] B. 192.168.10.15
- [ ] C. 192.168.10.128
- [ ] D. 192.168.10.255

*Justification:* Prefix /26 means mask 255.255.255.192. Block size is 256 - 192 = 64. Subnets are .0 to .63, .64 to .127 etc. 192.168.10.55/26 belongs to the first subnet (0-63). 192.168.10.15 also belongs to the same subnet.

**4.** Traceroute (or Tracert) is a tool that:
- [ ] A. Returns the MAC address of a remote computer.
- [✓] B. Traces the path of routers taken by a packet using the TTL field.
- [ ] C. Measures hard disk speed.
- [ ] D. Encrypts data between two nodes.

*Justification:* Traceroute sends packets with increasing TTL, causing intermediate routers to respond with ICMP Time Exceeded messages, revealing their identity.

**5.** Select True (T) or False (F):
- **[✓] T** / [ ] F The Pipelining effect in packet switching dramatically reduces total transfer time of multiple packets across many hops compared to sending them one by one end-to-end.
- [ ] T / **[✓] F** OSPF (Open Shortest Path First) protocol uses the Bellman-Ford algorithm.
- **[✓] T** / [ ] F A Web Server is typically hosted in a Data Center for high availability.

*Justification:*
- **T (True):** Pipelining (simultaneous transmission of consecutive packets over different links) saves massive time in packet switching.
- **F (False):** OSPF uses Dijkstra's algorithm (Link State). Bellman-Ford belongs to DV (e.g. RIP).
- **T (True):** Due to always-on, static IP, and high-bandwidth needs, servers are almost always in Data Centers.

---

## Part B: Exercises and Networks (7 points)

### Exercise 1 (2.5 points)
**Link State Algorithm (Dijkstra)**
Consider the network topology below, with edge transmission costs.

```
          3
      (A)---(B)
      / \     \
    1/   \2    \4
    /     \     \
  (C)---5-(D)---(E)
         /   \2
       1/     \
      (F)---3-(G)
```

Apply Dijkstra's algorithm with **starting node A** to find shortest paths to all nodes. Fill in the table giving total cost and previous node in parentheses.

| Step | Visited | B | C | D | E | F | G |
|---|---|---|---|---|---|---|---|
| 0 | A | `3(A)` | `1(A)` | `2(A)` | `\infty` | `\infty` | `\infty` |
| 1 | `A, C` | `3(A)` | `**1(A)**` | `2(A)` | `\infty` | `\infty` | `\infty` |
| 2 | `A, C, D` | `3(A)` | `1(A)` | `**2(A)**` | `\infty` | `3(D)` | `4(D)` |
| 3 | `A, C, D, B` | `**3(A)**` | `1(A)` | `2(A)` | `7(B)` | `3(D)` | `4(D)` |
| 4 | `A, C, D, B, F` | `3(A)` | `1(A)` | `2(A)` | `7(B)` | `**3(D)**` | `4(D)` |
| 5 | `A, C, D, B, F, G` | `3(A)` | `1(A)` | `2(A)` | `7(B)` | `3(D)` | `**4(D)**` |

Based on the table, what is the shortest path to reach node G?
---
**Answer:**
Based on the table: Minimum cost is 4. Previous to G is D. Previous to D is A.
- Path: **`A ➔ D ➔ G`**
- Cost: **`4`**

---

### Exercise 2 (2.5 points)
**TCP Timeout & Sliding Window Calculation**
In TCP protocol, Timeout calculation is based on EstimatedRTT:
- $\text{Timeout} = 2 \times \text{EstimatedRTT}$ *(in simplified form)*

**a. (1 point)** If current $\text{EstimatedRTT}$ is $50\text{ ms}$ and a new $\text{SampleRTT} = 90\text{ ms}$ is received, calculate the new $\text{Timeout}$. 
(Assume relation: $\text{EstimatedRTT}_{new} = 0.8 \cdot \text{EstimatedRTT}_{old} + 0.2 \cdot \text{SampleRTT}$).

---
**Answer:**
$$ \text{EstimatedRTT}_{new} = 0.8 \cdot 50 + 0.2 \cdot 90 = 40 + 18 = 58\text{ ms} $$
$$ \text{Timeout} = 2 \cdot \text{EstimatedRTT}_{new} = 2 \cdot 58\text{ ms} = `116\text{ ms}` $$

**b. (1.5 points)** Suppose you connect to an FTP Server. The file size you are downloading is huge. Connection Bandwidth is $R = 400\text{ Mbps}$, and connection RTT (Round Trip Time) is constant at $40\text{ ms}$. 
To fully utilize available Bandwidth without the "channel" running empty awaiting acknowledgements (ACKs), what must be the minimum Sliding Window size in MBytes?
*(Hint: Calculate how much data can be sent in one RTT timeframe)*.

---
**Answer:**
To eliminate idle time, the sender must continuously send data during one RTT:
$$ \text{Window Size} = \text{Bandwidth} \times \text{RTT} = (400 \times 10^6\text{ bps}) \times 0.04\text{ s} = 16,000,000\text{ bits} $$
Conversion to MBytes:
$$ \text{Window Size (Bytes)} = \frac{16,000,000}{8} = 2,000,000\text{ Bytes} = `2\text{ MB}` $$

---

### Exercise 3 (2 points)
**Pipeline Effect & Store-and-Forward**
A file is split into **100 packets**. It must be sent from Host X to Host Y via an intermediate router Router R (i.e. **2 hops** total).
Transmission rate of each link is $R = 1\text{ Mbps}$, and packet size is $L = 10,000\text{ bits}$. 
(Ignore propagation, processing, and queuing delays).

**a.** How much time (in seconds) is required to transmit **one packet** over one link (hop)?
---
**Answer:**
$$ d_{trans} = \frac{L}{R} = \frac{10,000\text{ bits}}{1,000,000\text{ bps}} = 0.01\text{ s} = `10\text{ ms}` $$

**b.** How much time (in seconds) is required for the **1st packet** to reach Host Y?
---
**Answer:**
The 1st packet traverses 2 hops (Store-and-Forward):
$$ d_{1st\_packet} = 2 \times d_{trans} = 2 \times 0.01\text{ s} = `0.02\text{ s}`\ (20\text{ ms}) $$

**c.** What is the **total time** until the 100th (last) packet reaches Host Y?
---
**Answer:**
Due to pipelining, the general formula for $N$ hops and $P$ packets is:
$$ d_{total} = (N + P - 1) \times d_{trans} $$
With $N=2$ and $P=100$:
$$ d_{total} = (2 + 100 - 1) \times 0.01\text{ s} = 101 \times 0.01 = `1.01\text{ s}` $$
