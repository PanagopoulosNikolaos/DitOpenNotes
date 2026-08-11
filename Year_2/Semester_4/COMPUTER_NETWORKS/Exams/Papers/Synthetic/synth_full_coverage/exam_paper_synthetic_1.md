# Computer Networks - Exam Questions (Synthetic Exam 1)
*Computer Networks - Synthetic Exam 1*

## Exam Information
- **Academic Year:** .......................
- **Exam Duration:** 2 hours and 15 minutes

## Student Data
- **Full Name:** ______________________________________________________
- **Registration Number (AM):** __________________

---

## Part A: Multiple Choice & Theory Questions (3 points)

**1.** Which of the following is a characteristic of packet switching as opposed to circuit switching?
- [ ] A. Dedicated resource reservation in advance
- [✓] B. The capability of statistical multiplexing
- [ ] C. The impossibility of packet loss
- [ ] D. Guaranteed transmission rate (QoS) for each user

*Justification:* Packet switching dynamically shares bandwidth among users, allowing multiple users to share resources efficiently. A, C, and D are characteristics (or drawbacks) of circuit switching.

**2.** The "Store-and-Forward" operation in a router means that:
- [✓] A. The router must receive the entire packet before beginning to forward it.
- [ ] B. The router permanently stores packets on its hard disk.
- [ ] C. Forwarding begins as soon as the packet header is received.
- [ ] D. The router never checks for errors during transfer.

*Justification:* This is the core principle of Store-and-Forward in packet switching, adding transmission delay at each hop.

**3.** Which of the following routing protocols is based on the Link State algorithm and requires complete knowledge of network topology?
- [ ] A. RIP
- [✓] B. OSPF
- [ ] C. BGP
- [ ] D. ARP

*Justification:* OSPF (Open Shortest Path First) is based on Dijkstra's algorithm and is a Link State protocol that builds a complete topological map. RIP is Distance Vector.

**4.** Architecturally, the Client-Server model belongs:
- [ ] A. In the Network Core
- [✓] B. In the Network Edge
- [ ] C. Only in local area networks (LAN)
- [ ] D. In the Data Link Layer

*Justification:* Client and server computers constitute the "end systems" located at the edge of the network.

**5.** Select True (T) or False (F):
- **[✓] T** / [ ] F The Control Plane of a router handles computing and maintaining knowledge of network structure.
- [ ] T / **[✓] F** A Server typically has a dynamic IP address.
- **[✓] T** / [ ] F The BGP protocol is used for routing between different Autonomous Systems (AS).

*Justification:*
- **T (True):** The Control Plane is responsible for routing algorithms.
- **F (False):** Servers require a permanent, static IP to remain accessible to clients.
- **T (True):** BGP is the de facto routing protocol between different ASes on the Internet.

---

## Part B: Exercises and Networks (7 points)

### Exercise 1 (2 points)
For the local area network (LAN) below, suppose computer X wishes to communicate with computer Z. Computer X knows Z's IP address, but not its MAC address.

```
(X) 192.168.1.10                    (Z) 192.168.1.30
    AA:AA:AA:AA:AA:AA                   CC:CC:CC:CC:CC:CC
       |                                   |
       +-----------------------------------+
                       |
                  192.168.1.20 (Y)
                  BB:BB:BB:BB:BB:BB
```

**a.** Fill in the details of the ARP messages exchanged by the two devices.

**Computer X Request (ARP Request)**
Sender MAC: `AA:AA:AA:AA:AA:AA`
Sender IP:  `192.168.1.10`
Target MAC: `00:00:00:00:00:00`
Target IP:  `192.168.1.30`

**Computer Z Reply (ARP Reply)**
Sender MAC: `CC:CC:CC:CC:CC:CC`
Sender IP:  `192.168.1.30`
Target MAC: `AA:AA:AA:AA:AA:AA`
Target IP:  `192.168.1.10`

**b.** If computer X wished to send a packet to an IP address outside the local network (e.g. 8.8.8.8), whose MAC address would it attempt to communicate with?

---
**Answer:**
With the MAC address of the **Default Gateway / Router** of its local network (since IP 8.8.8.8 lies outside the local broadcast domain).

---

### Exercise 2 (2.5 points)
Consider a network with 3 hops (Host A $\rightarrow$ Router 1 $\rightarrow$ Router 2 $\rightarrow$ Host B). Each link has a transmission rate $R = 2\text{ Mbps}$ ($2 \times 10^6\text{ bps}$) and physical length of $10,000\text{ km}$. Signal propagation speed is $s = 2 \times 10^8\text{ m/s}$. Host A wants to send a packet of size $L = 10,000\text{ bits}$ to Host B.

(Assume zero processing and queuing delays).

**a.** Calculate the transmission delay ($d_{trans}$) for one hop.
---
**Answer:**
$$d_{trans} = \frac{L}{R} = \frac{10,000\text{ bits}}{2 \times 10^6\text{ bps}} = 0.005\text{ s} = `5\text{ ms}`$$

**b.** Calculate the propagation delay ($d_{prop}$) for one hop.
---
**Answer:**
$$d_{prop} = \frac{d}{s} = \frac{10,000 \times 10^3\text{ m}}{2 \times 10^8\text{ m/s}} = \frac{10^7}{2 \times 10^8} = 0.05\text{ s} = `50\text{ ms}`$$

**c.** Calculate the end-to-end delay from the instant Host A begins transmitting the packet until Host B receives the entire packet. (Routers operate in store-and-forward mode).
---
**Answer:**
The path consists of $N = 3$ hops. In a store-and-forward network without other delays:
$$d_{total} = N \times (d_{trans} + d_{prop})$$
$$d_{total} = 3 \times (5\text{ ms} + 50\text{ ms}) = 3 \times 55\text{ ms} = `165\text{ ms}`$$

---

### Exercise 3 (2.5 points)
A sender wishes to transmit the original data message `1101` using Hamming code.

**a.** How many parity bits ($p$) are required?
---
**Answer:**
The relation $2^p \ge d + p + 1 \Rightarrow 2^p \ge 4 + p + 1 \Rightarrow 2^p \ge p + 5$ applies.
For $p=3$: $2^3 = 8 \ge 3 + 5 = 8$. 
**$p = `3`$** parity bits are required.

**b.** What is the complete message transmitted assuming the use of **even parity**? Show bit positions and calculation in detail.
---
**Answer:**
The complete message will have $4 + 3 = 7$ bits.
Parity bit positions: $1, 2, 4$ (powers of 2).
Data bit positions: $3, 5, 6, 7$.

| Position | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| Bit | $P_1$ | $P_2$ | $D_1$ | $P_4$ | $D_2$ | $D_3$ | $D_4$ |
| Value | `1` | `0` | `1` | `0` | `1` | `0` | `1` |

Bit calculation (even parity):
- **$P_1$ (checks positions 1, 3, 5, 7):** $P_1 \oplus D_1 \oplus D_2 \oplus D_4 = P_1 \oplus 1 \oplus 1 \oplus 1 = P_1 \oplus 1$. For even number of ones: **$P_1 = `1`$**.
- **$P_2$ (checks positions 2, 3, 6, 7):** $P_2 \oplus D_1 \oplus D_3 \oplus D_4 = P_2 \oplus 1 \oplus 0 \oplus 1 = P_2 \oplus 0$. For even number of ones: **$P_2 = `0`$**.
- **$P_4$ (checks positions 4, 5, 6, 7):** $P_4 \oplus D_2 \oplus D_3 \oplus D_4 = P_4 \oplus 1 \oplus 0 \oplus 1 = P_4 \oplus 0$. For even number of ones: **$P_4 = `0`$**.

Final transmitted message: **`1010101`**
