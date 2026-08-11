# Exercises

## E1. Broadcast Channel Characteristics
Consider the following four desirable characteristics of a broadcast channel.

Which of these characteristics are satisfied by FDMA, pure ALOHA, slotted ALOHA, and CSMA? Let $R$ be the bandwidth of the channel.

(a) When only one node has data to send, that node has a throughput equal to $R$.

(b) When $M$ nodes have data to send, each of them has on average a fair share of the channel's bandwidth.

(c) The protocol is decentralized, i.e., there is no master node that acts as a single point of failure.

(d) The protocol is simple, resulting in low implementation cost.

## A1. Slotted ALOHA
Consider two nodes, A and B, which use the slotted ALOHA protocol to compete for access to a channel with bandwidth $R$. Suppose node A has more data to transmit than node B and that node A's retransmission probability, $p_A$, is greater than node B's retransmission probability, $p_B$.

(a) Give a formula for the average throughput of node A.

(b) Give a formula for the average throughput of node B.

(c) What is the total efficiency of the protocol with these two nodes?

(d) If $p_A = 2 \cdot p_B$, is node A's average throughput double that of node B? Why or why not? If not, how can you choose $p_A$ and $p_B$ so that this is the case?

(e) In general, suppose there are $N$ nodes, of which node A has a retransmission probability of $2 \cdot p$ and all other nodes have a retransmission probability of $p$. Give expressions to calculate the average throughput of node A and any other node.

### A1-ans. Slotted ALOHA
(a) Node A's average throughput is given by:
$p_A(1 - p_B)$

(b) Node B's average throughput is given by:
$p_B(1 - p_A)$

(c) The total efficiency is:
throughput of A + throughput of B
$p_A(1 - p_B) + p_B(1 - p_A)$

(d) If $p_A = 2 \cdot p_B$, then node A's average throughput becomes:
$2p_B(1 - p_B)$
Furthermore, node B's average throughput becomes:
$p_B(1 - 2p_B)$
We can clearly see that node A's throughput is not double that of node B.
For node A's throughput to be double that of node B, it must hold:
$p_A(1 - p_B) = 2 p_B(1 - p_A)$
$p_A = 2 \cdot p_B / (1 + p_B)$

(e) Given that node A's retransmission probability is $2 \cdot p$, and all other ($N - 1$) nodes have a retransmission probability of $p$, 
node A's average throughput must be:
$2 \cdot p(1 - p)^{N-1}$

For the remaining nodes, the average throughput will be:
$p(1 - p)^{N-2}(1 - 2p)$

## A2. Link State Protocols
Suppose we have an L3 network with the topology shown above (figure missing) and that the routing algorithm used is the link state algorithm.

1. After convergence, what is the path cost from H1 to H2 and what are the possible paths with this cost?

## A3. Multiple Access Protocols: Collisions
Consider the figure above, which shows the arrival of 9 messages for transmission at different wireless multiple access nodes, at times:
$t = \{0.1, 0.6, 1.7, 2.7, 2.8, 3.5, 4.2, 4.3, 4.9\}$
and each transmission requires exactly one time unit.
Suppose all nodes implement the ALOHA protocol.
For each message, indicate the time instant at which each transmission begins.

## A4. Error Detection And Correction: Two Dimensional Parity
10001100 01101000
10111011 01100001
01000110 11110101
00010000 00011001
11101010 01101110

**Solution:**
00010010 10100001 **1**
11101111 10100111 **1**
10000101 10000001 **1**
10010110 00101001 **1**
00110010 01110100 **1**
**11011110 11011010 1**

## A5. Transmission Time
Suppose you send a packet of size L bits over a path of Q links. Each link has a transmission rate of R bps. Assume that both queuing delay and propagation delay are negligible. Calculate the time it takes for the packet to reach its destination in the following cases:

a) The network is virtual circuit packet-switched. In this case, assume that the virtual circuit setup time (VC setup time) is $t_s$ sec, while the total packet header size is $h$ bits.

### A5a)-ans. Transmission Time
The transmission time of a packet on the link is:
$(L+h)/R$
The total transmission time across Q links is: 
$Q (L+h)/R$
Therefore, the required time is sec. 
$t_s + Q (L+h)/R$

### A5b, c). Transmission Time
b) The network provides a connectionless service. In this case, assume that each packet has a header equal to $2h$ bits. 
$Q (L+2h)/R$

c) The network is circuit-switched. In this case, assume that the circuit transmission rate between source and destination is $R$ bps, the circuit setup time is $t_s$ sec, and each packet header size is $h$ bits. 
$t_s+(h+L)/R$

## A6. Bandwidth-Delay Product
Suppose two computers, A and B, are 10,000 km apart and connected by a direct link of $R = 1$ Mbps. Assume also that the propagation speed on the link is $2.5 \cdot 10^8$ m/sec.

a) Calculate the bandwidth-delay product, $R \cdot D_{prop}$
b) Consider sending a 400,000-bit file from computer A to computer B. Assume the file is sent continuously as one large message. What is the maximum number of bits that will be on the link at any given time?
c) Give an interpretation of the bandwidth-delay product.
d) What is the width of a bit (in meters) on the link? Is it larger than a football field?
e) How much time is required to transmit the file, assuming it is sent continuously?
f) Suppose the file is broken down into 10 individual packets where each packet consists of 40,000 bits. Assume also that the receiver acknowledges receipt of each packet and that the transmission time of the acknowledgment packet is negligible. Finally, assume that the sender cannot send a new packet to the receiver without receiving an acknowledgment of receipt of the previous packet. How much time is required to transmit the file?

### A6-ans. Bandwidth-Delay Product
• a) 40,000 bits 
• b) 40,000 bits 
• c) The bandwidth-delay product represents the maximum number of bits that can be present on the link. 
• d) The width of a bit = link length / bandwidth-delay product. Therefore, the width of 1 bit is 250 meters, which is larger than a football field. 
• e) $t_{trans} + t_{prop} = 400 \text{ msec} + 40 \text{ msec} = 440 \text{ msec}$
• f) $10 \cdot (t_{trans} + 2 t_{prop}) = 10 \cdot (40 \text{ msec} + 80 \text{ msec}) = 1.2 \text{ sec}$
