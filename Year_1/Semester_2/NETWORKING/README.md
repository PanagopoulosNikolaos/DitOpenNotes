# Computer Networking and Telecommunications

## Course Overview
This course introduces the architecture, protocols, standards, and algorithms that govern computer networks and the global Internet, systematically exploring the layered protocol stack from the physical and data link layers up through network routing, transport reliability, and modern application services.

## Course Code
202 (NETWORKING)

## Prerequisites
* None (Foundational computer systems and architecture recommended)

---

## Topics Covered
* **Layered Network Architectures**: The OSI 7-Layer reference model, the TCP/IP Internet model, encapsulation, multiplexing, and Protocol Data Units (PDUs).
* **Data Link Layer and Local Area Networks**: Ethernet framing, MAC addressing, Address Resolution Protocol (ARP), CSMA/CD collision detection, and bridging/switching.
* **Network Layer and IP Addressing**: IPv4 classful vs CIDR addressing, Variable Length Subnet Masking (VLSM), subnet calculation, Internet Control Message Protocol (ICMP), and routing tables.
* **Transport Layer Protocols**: UDP datagram delivery, TCP connection establishment (3-way handshake) and teardown, sequence/acknowledgment numbers, sliding window flow control, and TCP congestion algorithms (Slow Start, Congestion Avoidance, Fast Retransmit).
* **Application Layer Protocols**: Domain Name System (DNS) resolution, HTTP/1.1 vs HTTP/2 protocol exchange, DHCP dynamic addressing, and SMTP email transfer.
* **Network Analysis and Diagnostic Tools**: Packet capture and inspection with `tcpdump` and Wireshark, Berkeley Packet Filters (BPF), socket programming, and interface diagnostics.

---

## Learning Objectives
* Calculate optimal VLSM subnetting topologies and determine network, broadcast, and usable host address boundaries.
* Capture and dissect live network traffic at the byte level using Wireshark and `tcpdump`.
* Analyze TCP stream graphs, flow control dynamics, sequence tracking, and congestion events.
* Implement robust client-server socket communication architectures in Python.
* Evaluate routing table decisions based on longest prefix matching rules.

---

## Directory Structure

| Directory | Description |
|:---|:---|
| [`Lectures/`](Lectures/) | Structured theory lectures and authoritative reference monographs (Tanenbaum, TCP/IP Guide) |
| [`Exercises/`](Exercises/) | Five laboratory exercises covering ARP tables, packet capture, DNS lookups, and TCP segment analysis |
| [`Examples/`](Examples/) | Python implementations for TCP echo servers, subnet calculators, UDP pings, DNS clients, and HTTP parsers |
| [`Assignments/`](Assignments/) | Practical laboratory assignments with formal evaluation rubrics (Subnetting, tcpdump reports) |
| [`Tutorials/`](Tutorials/) | Hands-on walkthroughs for BPF packet filtering and TCP/UDP socket programming |
| [`Projects/`](Projects/) | Capstone term design project (Custom Packet Analyzer and Network Sniffer) |
| [`Exams/`](Exams/) | Comprehensive model practice examinations with complete worked solutions and grading rubrics |
| [`Resources/`](Resources/) | Deep-dive study notes, RFC protocol standards, and textbook references |

---

## Computational Examples in Python

The [`Examples/`](Examples/) directory provides standalone Python tools:

```bash
# 1. TCP Echo Server and Interactive Client
python3 Examples/01_tcp_echo_server_client.py

# 2. IPv4 CIDR Subnet Calculator
python3 Examples/02_subnet_calculator.py

# 3. UDP Socket Ping Latency Tester
python3 Examples/03_udp_ping_client_server.py

# 4. Raw Wire-Format DNS Query Client
python3 Examples/04_dns_query_client.py

# 5. RFC 7230 HTTP Header Parser
python3 Examples/05_http_header_parser.py
```
