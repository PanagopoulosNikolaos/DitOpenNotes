# Computer Networks - Exam Questions (Synthetic & Realistic Exam 3)
*Computer Networks - Synthetic & Realistic Exam 3*

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

**2.** The "Store-and-Forward" operation in a router means that:
- [✓] A. The router must receive the entire packet before beginning to forward it.
- [ ] B. The router permanently stores packets on its hard disk.
- [ ] C. Forwarding begins as soon as the packet header is received.
- [ ] D. The router never checks for errors during transfer.

*Justification:* This is the core principle of Store-and-Forward in packet switching, adding transmission delay at each hop.

**3.** Which of the following IP addresses belongs to the same subnet as $172.16.30.200/26$?
- [ ] A. 172.16.30.10
- [ ] B. 172.16.30.63
- [✓] C. 172.16.30.250
- [ ] D. 172.16.30.127

*Justification:* Mask /26 means 255.255.255.192. Block size is 256 - 192 = 64. Subnets are .0 to .63, .64 to .127, .128 to .191, .192 to .255. 172.16.30.200 belongs to the fourth subnet (192-255), as does 172.16.30.250.

**4.** Traceroute (or Tracert) is a tool that:
- [ ] A. Returns the MAC address of a remote computer.
- [✓] B. Traces the path of routers taken by a packet using the TTL field.
- [ ] C. Measures hard disk speed.
- [ ] D. Encrypts data between two nodes.

*Justification:* Traceroute sends packets with increasing TTL, causing intermediate routers to respond with ICMP Time Exceeded messages, revealing their identity.

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
**End-to-End Delay with Processing (Store-and-Forward)**
Consider the path from Computer A to Computer B passing through 2 Routers (total $N = 3$ hops).
Each of the 3 links has the following characteristics:
- Link length: $d = 1,000$ km
- Propagation speed: $s = 2 \times 10^8$ m/s
- Transmission Rate (Bandwidth): $R = 10$ Mbps

A packet of size $L = 10,000$ bits is sent from A to B.
Additionally, each of the two intermediate Routers introduces a Processing Delay $d_{proc} = 0.5$ ms. There is no queuing delay.

**a.** What is the transmission delay ($d_{trans}$) per hop?
**b.** What is the propagation delay ($d_{prop}$) per hop?
**c.** Calculate the total end-to-end delay (Total end-to-end delay).

---
**Answers:**
**a.** $$d_{trans} = \frac{L}{R} = \frac{10,000}{10 \times 10^6} = 0.001\text{ s} = `1\text{ ms}`$$

**b.** $$d_{prop} = \frac{d}{s} = \frac{1 \times 10^6\text{ m}}{2 \times 10^8\text{ m/s}} = 0.005\text{ s} = `5\text{ ms}`$$

**c.** The formula for store-and-forward of a packet over $N$ hops with processing delay at $N-1$ intermediate routers is:
$$ d_{total} = N \cdot d_{trans} + N \cdot d_{prop} + (N-1) \cdot d_{proc} $$
With $N = 3$ hops, we have $3-1 = 2$ intermediate routers:
$$ d_{total} = 3 \cdot (1\text{ ms}) + 3 \cdot (5\text{ ms}) + 2 \cdot (0.5\text{ ms}) $$
$$ d_{total} = 3\text{ ms} + 15\text{ ms} + 1\text{ ms} = `19\text{ ms}` $$

---

### Exercise 2 (2.5 points)
**Pipeline Effect & Store-and-Forward**
A file is split into **50 packets**. It must be sent from Host X to Host Y via an intermediate router Router R (i.e. **2 hops** total).
Transmission rate of each link is $R = 1$ Mbps, and packet size is $L = 5,000$ bits.
(Ignore propagation, processing, and queuing delays).

**a.** How much time (in seconds) is required to transmit **one packet** over one link (hop)?
**b.** How much time (in seconds) is required for the **1st packet** to reach Host Y?
**c.** What is the **total time** until the 50th (last) packet reaches Host Y?

---
**Answers:**
**a.** $$ d_{trans} = \frac{L}{R} = \frac{5,000\text{ bits}}{1,000,000\text{ bps}} = 0.005\text{ s} = `5\text{ ms}` $$

**b.** The 1st packet traverses 2 hops (Store-and-Forward):
$$ d_{1st\_packet} = 2 \times d_{trans} = 2 \times 0.005\text{ s} = `0.01\text{ s}`\ (10\text{ ms}) $$

**c.** Due to pipelining, the general formula for $N$ hops and $P$ packets is:
$$ d_{total} = (N + P - 1) \times d_{trans} $$
With $N=2$ and $P=50$:
$$ d_{total} = (2 + 50 - 1) \times 0.005\text{ s} = 51 \times 0.005 = `0.255\text{ s}` $$

---

### Exercise 3 (2.5 points)
**OSPF Configuration & TCP BBR**

**a.** For the network in the figure below, configure OSPF routing assuming you have only one routing area (fill in the blanks).

```
        172.16.8.0/29
              |
 10.10.10.0/30-O-
              |
        192.168.1.0/24

          Figure 1
```

```text
R>en
R# configure terminal
R(config)# router ospf 1
R(config-router)# network 10.10.10.0 0.0.0.3 area 0
R(config-router)# network 172.16.8.0 0.0.0.7 area 0
R(config-router)# network 192.168.1.0 0.0.0.255 area 0
R(config-router)# end
```

*Note: Wildcard masks are calculated by subtracting the subnet mask from $255.255.255.255$:*
- $/30 \Rightarrow 255.255.255.252 \Rightarrow \text{Wildcard: } 0.0.0.3$
- $/29 \Rightarrow 255.255.255.248 \Rightarrow \text{Wildcard: } 0.0.0.7$
- $/24 \Rightarrow 255.255.255.0 \Rightarrow \text{Wildcard: } 0.0.0.255$

**b.** In 2016, Google published the BBR congestion control algorithm. The BBR protocol sets CWND = RtProp x BtlBw, where RtProp = min(RTT).

Suppose a link is provided to connect directly with the server, round-trip time is 10 ms, and transmission rate is 0.25 GB/s. Calculate the congestion window size.

---
**Answer:**
- $RtProp = 10\text{ ms} = 0.01\text{ s}$
- $BtlBw = 0.25\text{ GB/s} = 0.25 \times 10^9\text{ Bytes/s} = 2.5 \times 10^8\text{ Bytes/s} = 2 \times 10^9\text{ bits/s}$
- $CWND = RtProp \times BtlBw = 0.01 \times 2 \times 10^9 = `20,000,000\text{ bits}` \ (2,500,000\text{ Bytes})$