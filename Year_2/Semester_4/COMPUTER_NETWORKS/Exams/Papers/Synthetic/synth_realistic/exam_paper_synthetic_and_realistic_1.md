# Computer Networks - Exam Questions (Synthetic & Realistic Exam 1)
*Computer Networks - Synthetic & Realistic Exam 1*

## Exam Information
- **Academic Year:** .......................
- **Exam Duration:** 2 hours and 15 minutes

## Student Data
- **Full Name:** ______________________________________________________
- **Registration Number (AM):** __________________

---

## Part A: Multiple Choice & Theory Questions (3 points)

**1.** Which of the following layers of the OSI model uses "Frame" as its PDU?
- [ ] A. Physical Layer
- [✓] B. Data Link Layer
- [ ] C. Network Layer
- [ ] D. Transport Layer

*Justification:* The Data Link Layer (Layer 2) organizes bits into frames with MAC headers. Network Layer uses packets/datagrams and Transport Layer uses segments.

**2.** In a Star network using exclusively Switches, how many collision domains are created for 8 connected computers?
- [ ] A. 1
- [✓] B. 8
- [ ] C. 4
- [ ] D. 0

*Justification:* Each physical port of a Switch constitutes a separate collision domain (micro-segmentation). With 8 computers on 8 ports, there are 8 separate collision domains.

**3.** Transmission delay ($d_{trans}$) of a packet of size $L = 2000$ bits on a link of rate $R = 1$ Mbps is:
- [ ] A. 0.5 ms
- [✓] B. 2 ms
- [ ] C. 20 ms
- [ ] D. 0.2 ms

*Justification:* $d_{trans} = \frac{L}{R} = \frac{2000}{10^6} = 2 \times 10^{-3}\text{ s} = 2\text{ ms}$.

**4.** Which of the following IP addresses belongs to the same subnet as $192.168.5.130/25$?
- [ ] A. 192.168.5.10
- [✓] B. 192.168.5.200
- [ ] C. 192.168.5.255
- [ ] D. 192.168.5.126

*Justification:* Mask /25 means 255.255.255.128. Block size is 128. Subnets are .0 to .127 and .128 to .255. 192.168.5.130 belongs to the second subnet (128-255), as does 192.168.5.200.

**5.** Select True (T) or False (F):
- **[✓] T** / [ ] F Packet switching uses statistical multiplexing.
- [ ] T / **[✓] F** A Router separates collision domains but not broadcast domains.
- **[✓] T** / [ ] F ARP Request is sent as Broadcast, while ARP Reply as Unicast.

*Justification:*
- **T (True):** Packet switching allocates resources dynamically, allowing multiple users to share bandwidth (statistical multiplexing).
- **F (False):** A router separates broadcast domains (each interface is separate). Switches separate collision domains.
- **T (True):** ARP Request is broadcast, ARP Reply is unicast to requester.

---

## Part B: Exercises and Networks (7 points)

### Exercise 1 (2 points)
**Delay & RTT Calculation**
Consider the network below with two links in series:

```
( A ) ============ ( B ) ============ ( C )
       Link 1              Link 2
       R1, L1, u1          R2, L2, u2
```

Given: $R_1 = 10000$ bps, $L_1 = 100$ Km, $u_1 = 2.5 \times 10^8$ m/s, $R_2 = 20000$ bps, $L_2 = 50$ Km, $u_2 = 2.5 \times 10^8$ m/s. Packet size is $P = 1000$ bits.

**a.** Calculate the time required to send a packet from node A to node C.

---
**Answer:**
$$t_{\text{total}} = d_{\text{trans1}} + d_{\text{prop1}} + d_{\text{trans2}} + d_{\text{prop2}}$$
- $d_{\text{trans1}} = \frac{P}{R_1} = \frac{1000}{10000} = 0.1\text{ s}$
- $d_{\text{prop1}} = \frac{L_1}{u_1} = \frac{100 \times 10^3}{2.5 \times 10^8} = 4 \times 10^{-4}\text{ s} = 0.4\text{ ms}$
- $d_{\text{trans2}} = \frac{P}{R_2} = \frac{1000}{20000} = 0.05\text{ s}$
- $d_{\text{prop2}} = \frac{L_2}{u_2} = \frac{50 \times 10^3}{2.5 \times 10^8} = 2 \times 10^{-4}\text{ s} = 0.2\text{ ms}$

$$t_{\text{total}} = 0.1 + 0.0004 + 0.05 + 0.0002 = `0.1506\text{ s}`$$

**b.** Calculate the RTT for a packet sent from A to B and returning immediately, ignoring processing delay.

---
**Answer:**
$$\text{RTT}_{A-B} = 2 \times d_{\text{trans1}} + 2 \times d_{\text{prop1}} = 2 \times 0.1 + 2 \times 0.0004 = `0.2008\text{ s}`$$

---

### Exercise 2 (2.5 points)
**Dijkstra Algorithm (Link State)**
Consider the network graph below. Apply Dijkstra's algorithm with starting node **A** and find shortest paths to all nodes.

```
      (A) --- 2 --- (B) --- 4 --- (C)
       |             |             |
       5             1             3
       |             |             |
      (D) --- 3 --- (E) --- 2 --- (F)
```

| Step | Visited | B | C | D | E | F |
|---|---|---|---|---|---|---|
| 0 | A | `2(A)` | `\infty` | `5(A)` | `\infty` | `\infty` |
| 1 | `A, B` | `**2(A)**` | `6(B)` | `5(A)` | `3(B)` | `\infty` |
| 2 | `A, B, E` | `2(A)` | `6(B)` | `5(A)` | `**3(B)**` | `5(E)` |
| 3 | `A, B, E, D` | `2(A)` | `6(B)` | `**5(A)**` | `3(B)` | `5(E)` |
| 4 | `A, B, E, D, F` | `2(A)` | `6(B)` | `5(A)` | `3(B)` | `**5(E)**` |
| 5 | `A, B, E, D, F, C` | `2(A)` | `**6(B)**` | `5(A)` | `3(B)` | `5(E)` |

**Shortest paths from A:**
- To **B**: $A \rightarrow B$ (Cost: `2`)
- To **E**: $A \rightarrow B \rightarrow E$ (Cost: `3`)
- To **D**: $A \rightarrow D$ (Cost: `5`)
- To **F**: $A \rightarrow B \rightarrow E \rightarrow F$ (Cost: `5`)
- To **C**: $A \rightarrow B \rightarrow C$ (Cost: `6`)

---

### Exercise 3 (2.5 points)
**CSMA/CD & Hamming Code**

**a.** A network uses CSMA/CD with bandwidth $R = 10$ Mbps. If maximum propagation time is $t_{prop} = 25.6\ \mu\text{s}$, what is the minimum frame size in Bytes?

---
**Answer:**
$$L_{\text{min}} \ge 2 \times t_{\text{prop}} \times R = 2 \times (25.6 \times 10^{-6}) \times (10 \times 10^6) = 512\text{ bits}$$
$$L_{\text{min}} = \frac{512}{8} = `64\text{ Bytes}`$$

**b.** A sender transmits message `1011` using Hamming code with **even parity**. What is the final transmitted message?

---
**Answer:**
Data message: $D = 1011$ ($d = 4$ bits).
Parity bits: $2^p \ge 4 + p + 1 \Rightarrow p = 3$.
Total message: $n = 4 + 3 = 7$ bits.
Parity positions: 1, 2, 4. Data positions: 3, 5, 6, 7.

| Position | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| Bit | $P_1$ | $P_2$ | $D_1$ | $P_4$ | $D_2$ | $D_3$ | $D_4$ |
| Value | `0` | `1` | `1` | `0` | `0` | `1` | `1` |

Calculation (even parity):
- **$P_1$ (positions 1, 3, 5, 7):** $P_1 \oplus 1 \oplus 0 \oplus 1 = P_1 \oplus 0$. For even number of ones: **$P_1 = 0$**.
- **$P_2$ (positions 2, 3, 6, 7):** $P_2 \oplus 1 \oplus 1 \oplus 1 = P_2 \oplus 1$. For even number of ones: **$P_2 = 1$**.
- **$P_4$ (positions 4, 5, 6, 7):** $P_4 \oplus 0 \oplus 1 \oplus 1 = P_4 \oplus 0$. For even number of ones: **$P_4 = 0$**.

Final transmitted message: **`0110011`**