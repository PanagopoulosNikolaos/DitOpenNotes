# Computer Networks - Exam Questions (Part 1)

**Exam Duration:** 1 hour and 45 minutes

---

## Questions

### 1. (1 point)
Consider the network in Figure 1. Define end-to-end delay in detail as a mathematical expression and explain the symbols included in it.
Assume packet size is L, transmission rate R, distance l, and propagation speed u.
Note any other assumptions.

```
       Packet
 (A)====[======]========(B)
         link
       Figure 1
```

---

### 2. (0.5 points)
Consider a network link with Bandwidth and Delay parameters. What is the maximum number of bits that can be present on this link at any given moment assuming Bandwidth is equal to your Registration Number in KB and Delay is equal to the last digit of your Registration Number in ms. (If the last digit of your Registration Number is 0 (zero), consider Delay = 6 ms).

---

### 3. (1 point)
For the network in Figure 2, configure OSPF routing assuming you have only one routing area (fill in the blanks)

```
        172.16.8.0/29
              |
10.10.10.0/30-O-
              |
        192.168.1.0/24

          Figure 2
```

```
R>en
R# __________________________________________________
   __________________________________________________
   __________________________________________________
   __________________________________________________
   __________________________________________________
   __________________________________________________
```

---
# Computer Networks - Exam Questions (Part 2)

**Exam Duration:** 2 hours and 15 minutes

---

### 4. (1.5 points)
In 2016, Google published the Bottleneck Bandwidth and Round-trip propagation time (BBR) congestion control algorithm. The BBR protocol sets the congestion window CWND = RtProp x BtlBw, where RtProp = min(RTTt).

a. Suppose you use the TCP protocol to establish a connection with the Department's website (https://dit.uoi.gr/). Propose at least one method for sampling RTT and calculating RtProp.
b. How can you trace the path taken by packets from your computer to the Department's website?
c. Suppose you are provided a direct link to connect with the server hosting the Department's website, where the round-trip propagation time is 5 ms and the transmission rate is 0.125 GB/s. Calculate the congestion window size.

---

### 5. (1 point)
Consider the networks shown in Figures 3 and 4. Node X sends packets to node Y. Which path will the packets follow in each case and why? The ellipses correspond to different autonomous systems and the BGP protocol is used.

```
Figure 3:
Verizon:  [A] --- [B] --- [C] --- [D] ===> (Y)
                                   |
AT&T: (X) --- [E] --- [F] --- [G] --- [H] --- [I]

Figure 4:
Verizon:  [A] --- [B] --- [C] --- [D] --- [E] ===> (Y)
           |               |               |
AT&T:     [F] --- [G] --- [H] --- [I] --- [J]
                           |
                          (X)
```

---

## Exercise 1 (2.5 points)

```
( A ) --------- Link 1 --------- ( B ) --------- Link 2 --------- ( C )
```

Consider the diagram above. Link 1 (Link1) has length L1 (m) (where m stands for meters) and permits sending packets propagating at speed u1 (m/sec), while link 2 (Link2) has length L2 (m) and permits packet propagation at speed u2 (m/sec). Link1 has a transmission rate R1 (bps) and Link2 has a transmission rate R2 (bps). For all the following, assume packet size is equal to 1/2 of your Registration Number.

Calculate:

A. The time required to send a packet from node A to node C, given that R1 = 10000, L1 = 100Km and u1 = u2 = 2.5 * 10^8, R2 = 10000, L2 = 50Km.
B. The RTT (round trip time) for a packet sent from node A to node B (the packet is received and transmitted back by node B immediately after reception) ignoring processing delay.

---
# Computer Networks - Exam Questions (Part 3)

**Exam Questions**  
**Exam Duration:** 2 hours and 15 minutes

---

## Exercise 1 (continued)

C. The RTT (round trip time) for a packet sent from node A to node C (the packet is received and transmitted back by node C immediately after reception) if the processing delay at each node is 0.02 ms.

---

## Exercise 2 (2.5 points)

### A)
Consider the graph corresponding to the topology of a network. The number next to each edge indicates the link cost. Apply Dijkstra's link-state algorithm and calculate the shortest path from node a to node k.

```
           5            5
     /------------\ /---------\
    /   2    3     V     2     \ 3     5
  (a)-----(b)-----(c)-----(h)-----(i)-----(j)-----(k)
   |       |    / | \   / | \      |     / |       ^
   | 1     |2 / 3| 1|2/  |1 \3    |2    /2 |1     /1
   |       |/    |  |/   |   \    |   /   |    /
  (e)-----(f)----+(d)+----+---(m)+---+---(l)+--/
     \  1     3  |    \______1____/      /
      \__________|______________________/
                         1
```

| N | A | B | C | D | E | F | G | H | I | J | K |
|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | |
| | | | | | | | | | | | |
| | | | | | | | | | | | |
| | | | | | | | | | | | |
| | | | | | | | | | | | |
| | | | | | | | | | | | |
| | | | | | | | | | | | |
| | | | | | | | | | | | |
| | | | | | | | | | | | |

---

### B)
A network uses CSMA/CD and has a bandwidth of 10 Mbps. If the maximum propagation time (including delays) is 25.6 $\mu s$, what is the minimum frame size?
