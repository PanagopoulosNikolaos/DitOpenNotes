# Computer Networks - Exam Questions (Synthetic & Realistic Exam 5)
*Computer Networks - Synthetic & Realistic Exam 5*

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

**2.** Architecturally, the Client-Server model belongs:
- [ ] A. In the Network Core
- [✓] B. In the Network Edge
- [ ] C. Only in local area networks (LAN)
- [ ] D. In the Data Link Layer

*Justification:* Client and server computers constitute the "end systems" located at the edge of the network.

**3.** Queuing delay in a router:
- [ ] A. Depends exclusively on distance between two nodes.
- [ ] B. Is constant and calculated as $L/R$.
- [✓] C. Depends on packet arrival rate (traffic load) and varies continuously.
- [ ] D. Is due to checksum time.

*Justification:* Queuing delay depends exclusively on traffic intensity at the router at a given moment. It is not constant like transmission delay.

**4.** Which of the following routing protocols is based on the Link State algorithm and requires complete knowledge of network topology?
- [ ] A. RIP
- [✓] B. OSPF
- [ ] C. BGP
- [ ] D. ARP

*Justification:* OSPF (Open Shortest Path First) is based on Dijkstra's algorithm and is a Link State protocol that builds a complete topological map. RIP is Distance Vector.

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
**Delay & RTT Calculation (Multi-node Path)**
Consider the network below with two links in series:

```
( A ) ============ ( B ) ============ ( C )
       Link 1              Link 2
       R1, L1, u1          R2, L2, u2
```

Given: $R_1 = 20000$ bps, $L_1 = 50$ Km, $u_1 = 2.5 \times 10^8$ m/s, $R_2 = 10000$ bps, $L_2 = 100$ Km, $u_2 = 2.5 \times 10^8$ m/s. Packet size is $P = 2000$ bits.

**a.** Calculate the time required to send a packet from node A to node C.

---
**Answer:**
$$t_{\text{total}} = d_{\text{trans1}} + d_{\text{prop1}} + d_{\text{trans2}} + d_{\text{prop2}}$$
- $d_{\text{trans1}} = \frac{P}{R_1} = \frac{2000}{20000} = 0.1\text{ s}$
- $d_{\text{prop1}} = \frac{L_1}{u_1} = \frac{50 \times 10^3}{2.5 \times 10^8} = 2 \times 10^{-4}\text{ s} = 0.2\text{ ms}$
- $d_{\text{trans2}} = \frac{P}{R_2} = \frac{2000}{10000} = 0.2\text{ s}$
- $d_{\text{prop2}} = \frac{L_2}{u_2} = \frac{100 \times 10^3}{2.5 \times 10^8} = 4 \times 10^{-4}\text{ s} = 0.4\text{ ms}$

$$t_{\text{total}} = 0.1 + 0.0002 + 0.2 + 0.0004 = `0.3006\text{ s}`$$

**b.** Calculate the RTT for a packet sent from A to C and returning immediately, if processing delay at each node is $0.01$ ms.

---
**Answer:**
The path is $A \rightarrow B \rightarrow C \rightarrow B \rightarrow A$. There are 3 processing delays (at $B$ outbound, at $C$ turnaround, and at $B$ return):
$$\text{RTT}_{A-C} = 2 \times t_{\text{total}} + 3 \times d_{\text{proc}}$$
$$\text{RTT}_{A-C} = 2 \times 0.3006 + 3 \times 0.00001 = 0.6012 + 0.00003 = `0.60123\text{ s}`$$

---

### Exercise 2 (2.5 points)
**RIP Configuration & Topology**
For the network in the figure below, Router "Router1" must be configured using RIP version 2.

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

---

### Exercise 3 (2.5 points)
**CSMA/CD & BDP (Bandwidth-Delay Product)**

**a.** A network uses CSMA/CD with bandwidth $R = 100$ Mbps. If maximum propagation time is $t_{prop} = 5.12\ \mu\text{s}$, what is the minimum frame size in Bytes?

---
**Answer:**
$$L_{\text{min}} \ge 2 \times t_{\text{prop}} \times R = 2 \times (5.12 \times 10^{-6}) \times (100 \times 10^6) = 1024\text{ bits}$$
$$L_{\text{min}} = \frac{1024}{8} = `128\text{ Bytes}`$$

**b.** An intercontinental link has a propagation speed of $2 \times 10^8$ m/s and cable length of $6,000$ km. Data transmission rate (Bandwidth) is $R = 1$ Gbps ($10^9$ bps).

- **i.** What is the propagation delay ($d_{prop}$)?
- **ii.** What is the maximum number of bits that can be present inside the cable at any given moment (BDP)?
- **iii.** If at an intermediate router, the buffer size is filled with $1,000,000$ bytes of traffic at the moment your new packet arrives, and output rate is $1$ Gbps, how much time will pass (Queuing Delay - $d_{queue}$) before transmission of your packet begins?

---
**Answers:**
**i.** $$ d_{prop} = \frac{d}{s} = \frac{6,000 \times 10^3\text{ m}}{2 \times 10^8\text{ m/s}} = \frac{6 \times 10^6}{2 \times 10^8} = 0.03\text{ s} = `30\text{ ms}` $$

**ii.** $$ \text{BDP} = R \times d_{prop} = 10^9\text{ bps} \times 0.03\text{ s} = `30,000,000\text{ bits}` \text{ (or 30 Mbits)} $$

**iii.** Buffer draining time ($1,000,000\text{ Bytes} = 8,000,000\text{ bits}$) at rate $1$ Gbps is:
$$ d_{queue} = \frac{L_{queue}}{R_{out}} = \frac{8,000,000\text{ bits}}{10^9\text{ bps}} = 8 \times 10^{-3}\text{ s} = `8\text{ ms}` $$