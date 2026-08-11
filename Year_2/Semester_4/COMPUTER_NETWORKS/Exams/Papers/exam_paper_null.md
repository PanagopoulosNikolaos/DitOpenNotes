# Computer Networks - Exam Paper
*Computer Networks - Exam Paper*

## Exam Information

- **Academic Year:** .......................
- **Exam Duration:** 2 hours and 15 minutes *(Note on paper: 1 hour and 45 minutes)*
- **Examined Course:**
  - [✓] Computer Networks
  - [ ] Local & Metropolitan Area Networks Th
  - [ ] Local & Metropolitan Area Networks Lab

---

## Student Data

- **Full Name:** ______________________________________________________
- **Registration Number (AM):** __________________
- **Seat Number:** __________________

---

## Questions

### Question 1 (1 point)
Consider the network in Figure 1. Define end-to-end delay in detail as a mathematical expression and explain the symbols included in it.

```
                  +-----------+
  ( A ) --------->|   queue   |---------> ( B )
                  +-----------+
                    Figure 1
```

---
**Answer:**
The total end-to-end delay ($d_{\text{end-to-end}}$) consists of the sum of four component delays:
$$d_{\text{end-to-end}} = d_{\text{proc}} + d_{\text{queue}} + d_{\text{trans}} + d_{\text{prop}}$$

**Explanation of symbols:**
1. **$d_{\text{proc}}$ (Processing Delay):** The time required to examine packet headers, determine the next routing node, and check for bit errors.
2. **$d_{\text{queue}}$ (Queuing Delay):** The time a packet waits in the switch/router queue before its turn for transmission. Depends on the arrival rate of other packets.
3. **$d_{\text{trans}}$ (Transmission Delay):** The time required to push all packet bits onto the physical medium. Calculated as $d_{\text{trans}} = \frac{L}{R}$, where $L$ is packet size in bits and $R$ is link transmission rate (Bandwidth).
4. **$d_{\text{prop}}$ (Propagation Delay):** The time needed for a bit to propagate through the physical length of the link from source to destination. Calculated as $d_{\text{prop}} = \frac{d}{s}$, where $d$ is distance and $s$ is signal propagation speed in the specific physical medium.

---

### Question 2 (0.5 points)
Consider a network link with Bandwidth and Delay parameters. What is the maximum number of bits that can be present on this link at any given moment assuming Bandwidth is equal to your Registration Number in KB and Delay is equal to the last digit of your Registration Number in ms. (If the last digit of your Registration Number is 0 (zero), consider Delay = 5ms).

---
**Answer:**
The maximum number of bits present on the link at any given time equals the Bandwidth-Delay Product (BDP):
$$\text{Max Bits} = \text{Bandwidth} \times \text{Delay}$$

Let $N$ be the Registration Number (AM) and $d$ the last digit of AM (if $d = 0$, then $\text{Delay} = 5\text{ ms}$).
- **Bandwidth ($R$):** $N\text{ KB/s} = N \times 1000 \times 8\text{ bps} = 8000 \times N\text{ bps}$
- **Delay ($D$):** $d\text{ ms} = d \times 10^{-3}\text{ s}$

**Mathematical Formula:**
$$\text{Max Bits} = (8000 \times N) \times (d \times 10^{-3}) = 8 \times N \times d\text{ bits}$$
*(Note: If binary convention is used where $1\text{ KB} = 1024\text{ Bytes}$, then $R = N \times 1024 \times 8 = 8192 \times N\text{ bps}$, so $\text{Max Bits} = 8,192 \times N \times d \times 10^{-3}\text{ bits}$).*

**Example for AM = 3323:**
- $N = 3323$, $d = 3$
- $R = 3323 \times 1000 \times 8 = 26,584,000\text{ bps}$
- $D = 3\text{ ms} = 0.003\text{ s}$
- $\text{Max Bits} = 26,584,000 \times 0.003 = `79,752\text{ bits}`$

---

### Question 3 (1 point)
For the network in Figure 2, configure OSPF routing assuming you have only one routing area (fill in the blanks).

```
              172.16.8.0/29
                    |
      10.10.10.0/30 |
              \   /----\
               \ |   R  |
                \ \----/
                /   |
               /    |
      10.10.23.0/30 |
              192.168.1.0/24

                 Figure 2
```

**Blanks to fill:**
```text
R>en
R# configure terminal
R(config)# router ospf 1
R(config-router)# network 10.10.10.0 0.0.0.3 area 0
R(config-router)# network 10.10.23.0 0.0.0.3 area 0
R(config-router)# network 172.16.8.0 0.0.0.7 area 0
R(config-router)# network 192.168.1.0 0.0.0.255 area 0
R(config-router)# end
```

---
*Note: Wildcard masks are calculated by subtracting the subnet mask from 255.255.255.255:*
- $/30 \Rightarrow 255.255.255.252 \Rightarrow \text{Wildcard: } 0.0.0.3$
- $/29 \Rightarrow 255.255.255.248 \Rightarrow \text{Wildcard: } 0.0.0.7$
- $/24 \Rightarrow 255.255.255.0 \Rightarrow \text{Wildcard: } 0.0.0.255$

---

### Question 4 (1.5 points)
The TCP protocol uses the Sliding Window mechanism, and window size calculation is based on timeout. Specifically, the following relations are used:
- $\text{Timeout} = 2 \times \text{EstimatedRTT}$
- $\text{EstimatedRTT} = a \times \text{EstimatedRTT} + (1-a) \times \text{SampleRTT}$

**a.** Suppose you use the TCP protocol to establish a connection with the Department's website (https://dit.uoi.gr/). Propose at least one method for sampling RTT and calculating SampleRTT.

---
**Answer:**
TCP measures **SampleRTT** as the time elapsed between sending a segment and receiving the corresponding acknowledgment (ACK).
- **Karn's Algorithm:** To prevent ambiguous calculation due to retransmissions, TCP collects SampleRTT samples *only* for segments transmitted successfully on the first attempt.
- **TCP Timestamps Option (RFC 7323):** A modern alternative is embedding timestamps in the TCP header. The sender sets the transmit time and the receiver echoes it in the ACK, allowing accurate RTT calculation even during retransmissions.

**b.** How can you trace the path taken by packets from your computer to the Department's website?

---
**Answer:**
The **traceroute** utility (or **tracert** on Windows) is used.
It operates by sending a series of IP packets with increasing Time To Live (**TTL**), starting at $TTL = 1$. Each intermediate router decrements TTL by 1. When TTL becomes 0, the router drops the packet and sends back an **ICMP Time Exceeded** error message, revealing its IP identity.

**c.** Suppose you are provided a direct link to connect with the server hosting the Department's website, where the propagation time on the link is 5 $\mu$s, and the transmission rate is 0.125 GB/s. If you want to download a very, very large file, what is the maximum number of bits that can be sent by the sender until the 1st bit reaches your device (bits in flight)?

---
**Answer:**
- $d_{\text{prop}} = 5\ \mu\text{s} = 5 \times 10^{-6}\text{ s}$
- $R = 0.125\text{ GB/s} = 0.125 \times 10^9\text{ Bytes/s} = 1.25 \times 10^8\text{ Bytes/s}$
- $R = 1.25 \times 10^8 \times 8\text{ bits/byte} = 10^9\text{ bps} = 1\text{ Gbps}$
- **Bits in flight** (one-way link capacity):
  $$\text{Bits in flight} = R \times d_{\text{prop}} = 10^9\text{ bps} \times 5 \times 10^{-6}\text{ s} = `5000\text{ bits}`$$
*(Note: If binary definition is used for GB ($1\text{ GB} = 2^{30}\text{ Bytes}$), then $R = 0.125 \times 2^{30} \times 8 = 1,073,741,824\text{ bps}$, so $\text{Bits in flight} \approx `5369\text{ bits}`$).*

---

### Question 5 (1 point)
Consider the networks shown in Figures 3 and 4. Node X sends packets to node Y. Which path will the packets follow in each case and why? The ellipses correspond to different autonomous systems and the BGP protocol is used.

```
Figure 3:
+-----------------------------------------------------------+
| Verizon AS                                                |
|    [A] ---------- [B] ---------- [C] ---------- [D]       |
|     |                                            |   \    |
|     |                                            |    (Y) |
+-----|--------------------------------------------|--------+
      |                                            |
+-----|--------------------------------------------|--------+
|     |                                            |        |
|    [F] --- [G] --- [H] --- [I]                   |        |
|     /                       |                    |        |
|   [E]                       +--------------------+        |
|   /                                                       |
| (X)                                                       |
| AT&T AS                                                   |
+-----------------------------------------------------------+

Figure 4:
+-----------------------------------------------------------+
| Verizon AS                                                |
|    [A] ------ [B] ------ [C] ------ [D] ------ [E] ------ (Y)
|     |                                           |         |
+-----|-------------------------------------------|---------+
      |                                           |
+-----|-------------------------------------------|---------+
|     |                                           |         |
|    [F] ------ [G] ------ [H] ------ [I] ------ [J]        |
|                           |                               |
|                          (X)                              |
| AT&T AS                                                   |
+-----------------------------------------------------------+
```

---
**Answer:**
In BGP, when AS-Path length is equal (1 transit AS), **hot-potato routing** is applied. Each autonomous system attempts to forward the packet out of its network using the nearest egress router based on internal gateway protocol (IGP) cost.

**Figure 3:**
- AT&T (bottom AS) has two egress routers to Verizon: $F$ (left) and $I$ (right).
- Distance from $X$ to $F$ is 2 hops ($X \rightarrow E \rightarrow F$).
- Distance from $X$ to $I$ is 5 hops ($X \rightarrow E \rightarrow F \rightarrow G \rightarrow H \rightarrow I$).
- AT&T chooses $F$ as the nearest egress. Verizon handles internal routing from $A$ to $Y$.
- **Path:** `X -> E -> F -> A -> B -> C -> D -> Y`.

**Figure 4:**
- AT&T has two egresses: $F$ (connecting to $A$) and $J$ (connecting to $E$).
- Distance from $X$ (via $H$) to $F$ is 2 hops ($H \rightarrow G \rightarrow F$).
- Distance from $X$ (via $H$) to $J$ is 2 hops ($H \rightarrow I \rightarrow J$).
- A tie occurs in hot-potato routing. Selection is made based on secondary rules (e.g. lower Router ID of neighbor BGP peer). If egress $J$ is selected, the path is significantly shorter overall (`X -> H -> I -> J -> E -> Y`, 5 hops), whereas if $F$ is selected the path is 9 hops.

---

### Exercise 1 (2.5 points)

```
              Link 1                      Link 2
   ( A ) =================== ( B ) =================== ( C )
          L1 (m), u1, R1              L2 (m), u2, R2
```

Consider the diagram above. Link 1 (Link1) has length $L_1$ (m) and permits sending packets propagating at speed $u_1$ (m/sec), while link 2 (Link2) has length $L_2$ (m) and permits packet propagation at speed $u_2$ (m/sec). Link1 has transmission rate $R_1$ (bps) and Link2 has transmission rate $R_2$ (bps). For all the following, assume packet size is equal to 1/2 of your Registration Number.

Calculate:

**A.** The time required to send a packet from node A to node C, given that $R_1 = 12000$, $L_1 = 10\text{ Km}$ and $u_1 = u_2 = 2.5 \times 10^8$, $R_2 = 15000$, $L_2 = 50\text{ Km}$.

---
**Answer:**
Let $P$ be packet size in bits ($P = \frac{1}{2} \text{AM} \times 8 \text{ bits/byte}$).
$$t_{\text{total}} = d_{\text{trans1}} + d_{\text{prop1}} + d_{\text{trans2}} + d_{\text{prop2}}$$
- $d_{\text{trans1}} = \frac{P}{R_1} = \frac{P}{12000}\text{ s}$
- $d_{\text{prop1}} = \frac{L_1}{u_1} = \frac{10000\text{ m}}{2.5 \times 10^8\text{ m/s}} = 4 \times 10^{-5}\text{ s} = 0.04\text{ ms}$
- $d_{\text{trans2}} = \frac{P}{R_2} = \frac{P}{15000}\text{ s}$
- $d_{\text{prop2}} = \frac{L_2}{u_2} = \frac{50000\text{ m}}{2.5 \times 10^8\text{ m/s}} = 2 \times 10^{-4}\text{ s} = 0.2\text{ ms}$

$$t_{\text{total}} = P \times \left( \frac{1}{12000} + \frac{1}{15000} \right) + 0.00024\text{ s} = `1.5 \times 10^{-4} \times P + 0.00024\text{ s}`$$

**B.** The RTT (round trip time) for a packet sent from node A to node B (the packet is received and transmitted back by node B immediately after reception) ignoring processing delay.

---
**Answer:**
$$\text{RTT}_{A-B} = 2 \times d_{\text{trans1}} + 2 \times d_{\text{prop1}} = 2 \times \frac{P}{12000} + 2 \times 4 \times 10^{-5}\text{ s} = `\frac{P}{6000} + 8 \times 10^{-5}\text{ s}`$$

**C.** The RTT (round trip time) for a packet sent from node A to node C (the packet is received and transmitted back by node C immediately after reception) if the processing delay at each node is $0.02\text{ ms}$.

---
**Answer:**
The path is $A \rightarrow B \rightarrow C \rightarrow B \rightarrow A$. 3 processing delays occur (at $B$ during forward transit, at $C$ during reversal, and at $B$ during return transit):
$$\text{RTT}_{A-C} = 2 \times d_{\text{trans1}} + 2 \times d_{\text{prop1}} + 2 \times d_{\text{trans2}} + 2 \times d_{\text{prop2}} + 3 \times d_{\text{proc}}$$
$$\text{RTT}_{A-C} = 2 \times t_{\text{total}} + 3 \times d_{\text{proc}} = 2 \times (1.5 \times 10^{-4} \times P + 0.00024) + 3 \times 2 \times 10^{-5}$$
$$\text{RTT}_{A-C} = `3 \times 10^{-4} \times P + 0.00054\text{ s}`$$

---

### Exercise 2 (2.5 points)

```
          (H)
         /   \
       2/     \14
       /       \
     (G)-------(B)-------4-------(A)
     / \   9   / \               /
    6   \     /2  \4            /1
   /     \   /     \           /
 (F)---1---(D)---3---(C)-------
   \       /
   3\     /3
     \   /
      (E)
```

**A)** Consider the graph above corresponding to network topology. The number next to each edge indicates link cost. Apply Dijkstra's link-state algorithm and calculate the shortest path from node E to all other nodes in the network.

| Step | N | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|---|
| `1` | `E` | `\infty` | `\infty` | `3(E)` | `3(E)` | `0` | `3(E)` | `\infty` | `\infty` |
| `2` | `EC` | `4(C)` | `7(C)` | `3(E)` | `3(E)` | `0` | `3(E)` | `\infty` | `\infty` |
| `3` | `ECD` | `4(C)` | `5(D)` | `3(E)` | `3(E)` | `0` | `3(E)` | `8(D)` | `\infty` |
| `4` | `ECDF` | `4(C)` | `5(D)` | `3(E)` | `3(E)` | `0` | `3(E)` | `8(D)` | `\infty` |
| `5` | `ECDFA` | `4(C)` | `5(D)` | `3(E)` | `3(E)` | `0` | `3(E)` | `8(D)` | `\infty` |
| `6` | `ECDFAB` | `4(C)` | `5(D)` | `3(E)` | `3(E)` | `0` | `3(E)` | `8(D)` | `19(B)` |
| `7` | `ECDFABG` | `4(C)` | `5(D)` | `3(E)` | `3(E)` | `0` | `3(E)` | `8(D)` | `10(G)` |
| `8` | `ECDFABGH` | `4(C)` | `5(D)` | `3(E)` | `3(E)` | `0` | `3(E)` | `8(D)` | `10(G)` |

**Shortest paths from E:**
- To **C**: $E \rightarrow C$ (Cost: `3`)
- To **D**: $E \rightarrow D$ (Cost: `3`)
- To **F**: $E \rightarrow F$ (Cost: `3`)
- To **A**: $E \rightarrow C \rightarrow A$ (Cost: `4`)
- To **B**: $E \rightarrow D \rightarrow B$ (Cost: `5`)
- To **G**: $E \rightarrow D \rightarrow G$ (Cost: `8`)
- To **H**: $E \rightarrow D \rightarrow G \rightarrow H$ (Cost: `10`)

**B)** A network uses CSMA/CD and has a bandwidth of 15 Mbps. If the maximum propagation time (including delays) is $25.6\ \mu\text{s}$, what is the minimum frame size?

---
**Answer:**
$$t_{\text{trans}} \ge 2 \times t_{\text{prop}} \Rightarrow L_{\text{min}} \ge 2 \times t_{\text{prop}} \times R$$
With $R = 15\text{ Mbps} = 15 \times 10^6\text{ bps}$ and $t_{\text{prop}} = 25.6\ \mu\text{s} = 25.6 \times 10^{-6}\text{ s}$:
$$L_{\text{min}} = 2 \times (25.6 \times 10^{-6}\text{ s}) \times (15 \times 10^6\text{ bps}) = 768\text{ bits}$$
In Bytes: $\frac{768}{8} = `96\text{ Bytes}`$.

---

### Exercise 3 (Bonus +1 point)
A sender transmits message `10001011` using Hamming code. What is the transmitted message? Assume odd parity.

---
**Answer:**
Data message: $D = 10001011$ ($d = 8$ bits).
Number of parity bits ($p$): $2^p \ge 8 + p + 1 \Rightarrow p = 4$.
Total message $n = d + p = 12$ bits.

Calculations with odd parity:
- **$P_1$ (positions 1, 3, 5, 7, 9, 11):** $P_1 \oplus 1 \oplus 0 \oplus 0 \oplus 1 \oplus 1 \Rightarrow P_1 \oplus 3$. To get an odd number of ones, $P_1 = `0`$.
- **$P_2$ (positions 2, 3, 6, 7, 10, 11):** $P_2 \oplus 1 \oplus 0 \oplus 0 \oplus 0 \oplus 1 \Rightarrow P_2 \oplus 2$. To get an odd number of ones, $P_2 = `1`$.
- **$P_4$ (positions 4, 5, 6, 7, 12):** $P_4 \oplus 0 \oplus 0 \oplus 0 \oplus 1 \Rightarrow P_4 \oplus 1$. To get an odd number of ones, $P_4 = `0`$.
- **$P_8$ (positions 8, 9, 10, 11, 12):** $P_8 \oplus 1 \oplus 0 \oplus 1 \oplus 1 \Rightarrow P_8 \oplus 3$. To get an odd number of ones, $P_8 = `0`$.

Final transmitted Hamming message: **`011000001011`**
