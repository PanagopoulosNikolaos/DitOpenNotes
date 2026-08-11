# Computer Networks - Exam Questions (2023-2024)
*Computer Networks - Exam Paper 2023-2024*

## Exam Information
- **Academic Year:** 2023-2024
- **Exam Duration:** 2 hours and 15 minutes

## Student Data
- **Full Name:** ______________________________________________________
- **Registration Number (AM):** __________________

---

## Part A: Multiple Choice & Theory Questions

**1.** Which of the following is not among the possible data exchange modes?
- [ ] A. Simplex
- [✓] B. Multiplex
- [ ] C. Half-duplex
- [ ] D. Full duplex

*Justification:* Simplex, Half-duplex, and Full-duplex describe the direction and timing of data exchange in a channel. Multiplexing is a technique for combining multiple signals over a shared medium and does not describe communication direction.

**2.** A computer network is:
- [ ] A. A collection of hardware components and computers
- [ ] B. Interconnection via communication channels
- [ ] C. Resource and information sharing
- [✓] D. All of the above

*Justification:* A computer network consists of hardware (routers, switches, PCs), communication channels (cables, wireless links) and has the primary goal of resource and information sharing.

**3.** At which layer of the OSI model does a Repeater operate?
- [✓] A. Physical layer
- [ ] B. Data link layer
- [ ] C. Network layer
- [ ] D. Transport layer

*Justification:* A Repeater operates exclusively at the Physical layer (Layer 1). It regenerates and amplifies electrical/optical signals (bits) without examining frame (MAC) or packet (IP) headers.

**4.** What is the function of a Bridge in a network?
- [ ] A. connecting LANs
- [ ] B. separating LANs
- [ ] C. controlling speed in the network
- [✓] D. All of the above

*Justification:* A Bridge operates at Layer 2 (Data Link Layer). It connects multiple LAN segments (A) and filters traffic based on MAC addresses, thereby separating a large collision domain into smaller ones (B). In exam papers, answer D is often considered correct (if "speed control" refers loosely to collision reduction that improves throughput), although the main functions are A and B.

**5.** Congestion occurs in a network when:
- [✓] A. excessive traffic
- [ ] B. when a system terminates
- [ ] C. when the link between two nodes terminates
- [ ] D. None of the above

*Justification:* Congestion is caused when packets arrive at a router/switch at a rate faster than it can process them, filling queues (buffers) and ultimately leading to packet loss.

**6.** Suppose two machines communicate with each other. The process that communicates with a specific layer on each machine is called:
- [ ] A. UDP process
- [ ] B. Intranet process
- [ ] C. Server
- [✓] D. Peer-peer process

*Justification:* In network architecture (e.g. OSI model), entities at the same layer on different nodes (e.g. Transport layer on sender and Transport layer on receiver) are called "peer processes".

**Unnumbered.** "Parity bits" are used for the following purpose:
- [ ] Data encryption
- [ ] Faster data transmission
- [✓] Error detection
- [ ] Usage identification

*Justification:* Parity bits are the simplest form of error checking and are used exclusively for error detection during transmission.

---

## Part B: Exercises and Networks

### Exercise 4
```
                       (D)
                       |
               137.196.7.78
           1A-2F-BB-76-09-AD
                       |
(A) --------------+   LAN   +-------------- (C)
137.196.7.23      | 137.196.7.0/24 |      137.196.7.14
71-65-F7-2B-08-53 +----------------+      58-23-D7-FA-20-B0
                       |
                       |
               137.196.7.88
           0C-C4-11-6F-E3-98
                       |
                      (B)
                     Figure 3
```

For the network in Figure 3, suppose computer A wishes to communicate with computer C, for which it knows the IP but not the MAC address. Answer the following questions:

**a.** What are the contents of the ARP messages exchanged by the two devices?

**Computer A Request (ARP Request)**
Sender MAC: `71-65-F7-2B-08-53`
Sender IP:  `137.196.7.23`
Target MAC: `00:00:00:00:00:00`
Target IP:  `137.196.7.14`

**Computer C Reply (ARP Reply)**
Sender MAC: `58-23-D7-FA-20-B0`
Sender IP:  `137.196.7.14`
Target MAC: `71-65-F7-2B-08-53`
Target IP:  `137.196.7.23`

**b.** What type of transmission is used for sending the request (ARP Request) and receiving the reply (ARP Reply) by each device?
---
**Answer:**
- The **ARP Request** is sent as **Broadcast** (destination MAC: `FF-FF-FF-FF-FF-FF`) so all nodes on the LAN receive it.
- The **ARP Reply** is sent as **Unicast** directly to computer A, since A's MAC is now known to C.

**c.** If after 5 minutes, computer C wants to send a packet to computer A, will it use the ARP protocol again? (1 point)
---
**Answer:**
**`No`**, it will not use ARP again. The IP-to-MAC mapping is cached in the devices' **ARP Cache** for several minutes (typically 15-20 minutes), so C retrieves A's MAC directly from memory.

---

### Exercise 23
Fill in the contents of the ARP message exchanged by the two devices in the Figure:

```
    [PC] ---------------------------------- ( Router ) ----------- ( Internet )
 IP: 195.130.8.25                     IP: 195.130.8.1     IP: 172.16.1.1
 MAC: 00:25:64:D5:10:8B               MAC: 00:00:5E:00:10:01   MAC: 00:0B:14:E0:00:35
```

**Computer Request (ARP Request)**
Sender MAC: `00:25:64:D5:10:8B`
Sender IP:  `195.130.8.25`
Target MAC: `00:00:00:00:00:00`
Target IP:  `195.130.8.1`

**Device Reply (Router ARP Reply)**
Sender MAC: `00:00:5E:00:10:01`
Sender IP:  `195.130.8.1`
Target MAC: `00:25:64:D5:10:8B`
Target IP:  `195.130.8.25`

---

### Exercise 24
For the network in the Figure, configure RIP version 2 routing (fill in the blanks)

```
        10.15.2.0/24
             \
              \ Se0/1/1
  Se0/0/0 +---( 1841 )---+ Fa0/0
 ---------+              +---------
10.15.3.0/24             10.15.6.0/24
```

**Blanks to fill:**
```text
R>en
R# configure terminal
R(config)# router rip
R(config-router)# version 2
R(config-router)# no auto-summary
R(config-router)# network 10.15.2.0
R(config-router)# network 10.15.3.0
R(config-router)# network 10.15.6.0
R(config-router)# end
```

---

### Exercise 32
Select True (T) or False (F):

- **[✓] T** / [ ] F In a Bus topology, all nodes are in the same collision domain
- [ ] T / **[✓] F** In a Star topology, all nodes are in the same collision domain
- **[✓] T** / [ ] F In a Star topology, each link is itself a collision domain
- **[✓] T** / [ ] F Each physical router port defines a broadcast domain

*Justification:*
1. **True:** All computers share the same physical medium (e.g. coaxial cable).
2. **False:** In modern star networks, Switches are used, where each port is a separate collision domain (would only be true if Hubs were used).
3. **True:** Each micro-segment connected to a switch port isolates collisions.
4. **True:** Routers break Layer 2 broadcasts. Each interface connects to a different subnet.
