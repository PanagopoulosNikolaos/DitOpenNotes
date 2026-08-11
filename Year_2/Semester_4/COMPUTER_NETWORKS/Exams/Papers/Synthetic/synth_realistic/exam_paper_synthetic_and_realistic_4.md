# Computer Networks - Exam Questions (Synthetic & Realistic Exam 4)
*Computer Networks - Synthetic & Realistic Exam 4*

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

*Justification:* Encapsulation means higher layer data becomes payload for lower layer, receiving new header. De-encapsulation occurs at the receiver.

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

*Justification:* Dijkstra requires full network map to find shortest paths from source.

**4.** If a video streaming flow sends 2,000 packets per second and each packet size is 1,000 Bytes, the minimum required transmission rate (Bandwidth) without loss is:
- [ ] A. 2 Mbps
- [✓] B. 16 Mbps
- [ ] C. 2 Gbps
- [ ] D. 16 Gbps

*Justification:* $2,000\text{ pkts/sec} \times 1,000\text{ Bytes/pkt} = 2,000,000\text{ Bytes/sec} = 16\text{ Mbps}$.

**5.** Select True (T) or False (F):
- **[✓] T** / [ ] F The OSPF protocol supports Hierarchical Routing through division into Areas.
- [ ] T / **[✓] F** In Circuit Switching, if the user is idle, bandwidth is automatically utilized by other users.
- **[✓] T** / [ ] F ARP Reply messages are sent as Unicast to the requesting node.

*Justification:*
- **T (True):** OSPF divides large networks into Areas (e.g. Area 0) to reduce overhead.
- **F (False):** In Circuit Switching, if idle, resources remain reserved and wasted.
- **T (True):** ARP Request is Broadcast, ARP Reply is always Unicast to requester.

---

## Part B: Exercises and Networks (7 points)

### Exercise 1 (2 points)
**TCP Timeout & Sliding Window Calculation**
In TCP protocol, Timeout calculation is based on EstimatedRTT:
- $\text{Timeout} = 2 \times \text{EstimatedRTT}$ *(in simplified form)*

**a.** If current $\text{EstimatedRTT}$ is $80\text{ ms}$ and a new $\text{SampleRTT} = 120\text{ ms}$ is received, calculate the new $\text{Timeout}$.
(Assume relation: $\text{EstimatedRTT}_{new} = 0.875 \cdot \text{EstimatedRTT}_{old} + 0.125 \cdot \text{SampleRTT}$).

---
**Answer:**
$$ \text{EstimatedRTT}_{new} = 0.875 \cdot 80 + 0.125 \cdot 120 = 70 + 15 = 85\text{ ms} $$
$$ \text{Timeout} = 2 \cdot \text{EstimatedRTT}_{new} = 2 \cdot 85\text{ ms} = `170\text{ ms}` $$

**b.** Suppose you connect to an FTP Server. The file size you are downloading is huge. Connection Bandwidth is $R = 200\text{ Mbps}$, and connection RTT (Round Trip Time) is constant at $50\text{ ms}$.
To fully utilize available Bandwidth without the "channel" running empty awaiting acknowledgements (ACKs), what must be the minimum Sliding Window size in MBytes?

---
**Answer:**
To eliminate idle time, the sender must continuously send data during one RTT:
$$ \text{Window Size} = \text{Bandwidth} \times \text{RTT} = (200 \times 10^6\text{ bps}) \times 0.05\text{ s} = 10,000,000\text{ bits} $$
Conversion to MBytes:
$$ \text{Window Size (Bytes)} = \frac{10,000,000}{8} = 1,250,000\text{ Bytes} = `1.25\text{ MB}` $$

---

### Exercise 2 (2.5 points)
**Dijkstra Algorithm (Link State)**
Consider the network topology below, with edge transmission costs.

```
           2
      (A)---(B)
      / \     \
    1/   \3    \4
    /     \     \
  (C)---4-(D)---(E)
         /   \2
       1/     \
      (F)---3-(G)
```

Apply Dijkstra's algorithm with **starting node A** to find shortest paths to all nodes. Fill in the table giving total cost and previous node in parentheses.

| Step | Visited | B | C | D | E | F | G |
|---|---|---|---|---|---|---|---|
| 0 | A | `2(A)` | `1(A)` | `3(A)` | `\infty` | `\infty` | `\infty` |
| 1 | `A, C` | `2(A)` | `**1(A)**` | `3(A)` | `\infty` | `\infty` | `\infty` |
| 2 | `A, C, B` | `**2(A)**` | `1(A)` | `3(A)` | `6(B)` | `\infty` | `\infty` |
| 3 | `A, C, B, D` | `2(A)` | `1(A)` | `**3(A)**` | `6(B)` | `4(D)` | `5(D)` |
| 4 | `A, C, B, D, F` | `2(A)` | `1(A)` | `3(A)` | `6(B)` | `**4(D)**` | `5(D)` |
| 5 | `A, C, B, D, F, G` | `2(A)` | `1(A)` | `3(A)` | `6(B)` | `4(D)` | `**5(D)**` |
| 6 | `A, C, B, D, F, G, E` | `2(A)` | `1(A)` | `3(A)` | `**6(B)**` | `4(D)` | `5(D)` |

Based on the table, what is the shortest path to reach node G?
---
**Answer:**
Based on the table: Minimum cost is 5. Previous to G is D. Previous to D is A.
- Path: **`A ➔ D ➔ G`**
- Cost: **`5`**

---

### Exercise 3 (2.5 points)
**Hamming Code (Odd Parity)**
A sender wishes to transmit data message `1101` using Hamming error-correcting code.

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
| Value | `0` | `1` | `1` | `1` | `1` | `0` | `1` |

Calculation of bits (Odd Parity means total number of '1' bits in check group must be odd):
- **$P_1$ (positions 1, 3, 5, 7):** $P_1 \oplus D_1 \oplus D_2 \oplus D_4 = P_1 \oplus 1 \oplus 1 \oplus 1 = P_1 \oplus 1$.
  To have an odd number of ones, $P_1 = `0`$.
- **$P_2$ (positions 2, 3, 6, 7):** $P_2 \oplus D_1 \oplus D_3 \oplus D_4 = P_2 \oplus 1 \oplus 0 \oplus 1 = P_2 \oplus 0$.
  We have 0 ones (even). To make it odd, $P_2 = `1`$.
- **$P_4$ (positions 4, 5, 6, 7):** $P_4 \oplus D_2 \oplus D_3 \oplus D_4 = P_4 \oplus 1 \oplus 0 \oplus 1 = P_4 \oplus 0$.
  We have 0 ones (even). To make it odd, $P_4 = `1`$.

Final transmitted message: **`0111101`**