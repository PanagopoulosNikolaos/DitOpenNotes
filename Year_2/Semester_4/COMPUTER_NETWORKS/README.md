# Computer Networks

## Course Overview
This course provides a comprehensive exploration of telecommunication network architectures, core internetworking protocols, and analytical performance modeling. Topics include layered protocol architectures (OSI 7-layer and TCP/IP 5-layer stacks), packet switching vs. circuit switching, quantitative four-component delay modeling (transmission, propagation, processing, queuing), Classless Inter-Domain Routing (CIDR) and Variable Length Subnet Masking (VLSM), intra-domain and inter-domain routing protocols (RIP, OSPF, BGP), transport layer reliability and congestion control (TCP Reno/Cubic, UDP), data link protocols, Ethernet switching, and network socket programming.

## Course Code
403 (COMPUTER NETWORKS)

## Prerequisites
* Networking (Code: 204)
* C Programming II (Code: 201)

---

## Topics Covered
* **Layered Architectures & The Network Core**: OSI 7-layer reference model vs. TCP/IP stack, encapsulation and decapsulation, packet switching, statistical multiplexing, and store-and-forward mechanisms.
* **Network Performance Modeling**: End-to-end delay components ($d_{\text{trans}} = L/R$, $d_{\text{prop}} = d/s$, $d_{\text{proc}}$, $d_{\text{queue}}$), queuing models, packet loss, throughput, bottleneck analysis, and Bandwidth-Delay Product (BDP).
* **Network Layer & IP Addressing**: IPv4 datagram formats, Classless Inter-Domain Routing (CIDR), Variable Length Subnet Masking (VLSM), network and broadcast address calculation, Longest Prefix Matching (LPM), NAT, and ICMP.
* **Routing Algorithms & Autonomous Systems**: Link-State routing (Dijkstra's Shortest Path Algorithm), Distance Vector routing (Bellman-Ford equation, count-to-infinity problem, split horizon, poison reverse), OSPF hierarchical areas, and BGP inter-domain policies.
* **Transport Layer Protocols**: Multiplexing/demultiplexing, UDP lightweight datagram communication, TCP 3-way handshake, reliable data transfer (ARQ, Stop-and-Wait, Go-Back-N, Selective Repeat), flow control via sliding receive window, and AIMD congestion control (Slow Start, Congestion Avoidance, Fast Retransmit, Fast Recovery).
* **Data Link Layer & Local Area Networks**: Framing, Cyclic Redundancy Checks (CRC), CSMA/CD random access, MAC addressing, ARP resolution, Layer 2 Ethernet switching, collision domains vs. broadcast domains, and Virtual LANs (VLANs).
* **Socket Programming**: Client-server network architecture, POSIX Berkeley sockets, TCP stream sockets (`SOCK_STREAM`), and UDP datagram sockets (`SOCK_DGRAM`).

---

## Learning Objectives
* Calculate end-to-end latency, transmission delays, propagation times, and queuing behavior across multi-hop packet-switched network paths.
* Design efficient IPv4 addressing schemes utilizing CIDR notation and construct hierarchical routing tables via Longest Prefix Matching.
* Compute shortest paths and construct forwarding tables using Dijkstra's algorithm and Bellman-Ford distance vector updates.
* Trace TCP congestion window dynamics ($cwnd$) through slow start, congestion avoidance, and packet loss recovery phases.
* Develop functional client-server network applications in Python using TCP and UDP socket primitives.

---

## Directory Structure

| Directory | Description |
|:---|:---|
| [`Lectures/`](Lectures/) | Structured theory modules covering network core, delays, IP subnetting, and switching |
| [`Exercises/`](Exercises/) | Solved quantitative drills on delay calculations, CIDR subnetting, and distance vector routing |
| [`Examples/`](Examples/) | Executable TCP/UDP Python socket implementations, walkthrough guides, and lecture drills |
| [`Assignments/`](Assignments/) | Laboratory coursework: delay/jitter packet analysis, Wireshark traces, and Packet Tracer labs |
| [`Tutorials/`](Tutorials/) | Hands-on guides for Cisco Packet Tracer VLAN switching and Wireshark packet dissection |
| [`Projects/`](Projects/) | Capstone design specification for an enterprise multi-campus network architecture |
| [`Exams/`](Exams/) | Past examination papers, synthetic practice drills, and original paper scans |
| [`Resources/`](Resources/) | Granular topic notes (1-7), presentation decks, interactive web application, and quizzes |

---

## Tooling and Simulation Environment

### Python Socket Client-Server Execution
To run the automated TCP and UDP client-server demonstration:
```bash
python3 Examples/examples_socket_programming_tcp_udp.py
```

### Packet Analysis with Wireshark / TShark
To inspect active network traffic on the loopback interface:
```bash
tshark -i lo -f "tcp port 9001"
```

### Interactive Learning & Exam Web Application
To launch the interactive Computer Networks web platform:
```bash
cd Resources/app
python3 -m pip install -r requirements.txt
python3 main.py
```