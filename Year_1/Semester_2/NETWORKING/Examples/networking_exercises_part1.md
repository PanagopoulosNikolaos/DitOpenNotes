# Networking Exercises - Part 1: Foundation
## Introduction to Networking Concepts

This file contains 20 exercises covering basic networking concepts with progressive difficulty. These exercises will prepare you for more advanced topics in Part 2.

---

## Exercise 1: OSI Model Layers
**Question:** List all 7 layers of the OSI model from Layer 1 to Layer 7, and provide the primary function of each layer.

**Solution:**
1. **Physical Layer** - Transmits raw bits over physical medium (cables, signals)
2. **Data Link Layer** - Provides node-to-node data transfer, error detection (MAC addresses)
3. **Network Layer** - Handles routing and IP addressing
4. **Transport Layer** - Provides reliable data transfer (TCP/UDP, port numbers)
5. **Session Layer** - Manages sessions between applications
6. **Presentation Layer** - Data formatting, encryption, compression
7. **Application Layer** - Network services to end-user applications (HTTP, FTP, DNS)

---

## Exercise 2: IP Address Classification
**Question:** Identify the class (A, B, C, D, or E) of the following IP addresses:
- a) 10.25.30.5
- b) 172.16.50.100
- c) 192.168.1.1
- d) 224.0.0.5

**Solution:**
- a) **Class A** (first octet: 1-126)
- b) **Class B** (first octet: 128-191)
- c) **Class C** (first octet: 192-223)
- d) **Class D** (first octet: 224-239) - Multicast address

**Note:** 
- Class A: 0.0.0.0 to 127.255.255.255
- Class B: 128.0.0.0 to 191.255.255.255
- Class C: 192.0.0.0 to 223.255.255.255
- Class D: 224.0.0.0 to 239.255.255.255 (Multicast)
- Class E: 240.0.0.0 to 255.255.255.255 (Reserved)

---

## Exercise 3: Binary to Decimal Conversion
**Question:** Convert the following binary IP address to decimal notation:
`11000000.10101000.00000001.01100100`

**Solution:**
- 11000000 = 128 + 64 = **192**
- 10101000 = 128 + 32 + 8 = **168**
- 00000001 = 1 = **1**
- 01100100 = 64 + 32 + 4 = **100**

**Answer:** 192.168.1.100

---

## Exercise 4: Subnet Mask Basics
**Question:** What is the default subnet mask for a Class B network? Express it in both decimal and CIDR notation.

**Solution:**
- **Decimal notation:** 255.255.0.0
- **CIDR notation:** /16
- **Binary:** 11111111.11111111.00000000.00000000

**Explanation:** Class B networks use the first 16 bits for the network portion.

---

## Exercise 5: TCP vs UDP
**Question:** Fill in the comparison table:

| Feature | TCP | UDP |
|---------|-----|-----|
| Connection Type | ? | ? |
| Reliability | ? | ? |
| Speed | ? | ? |
| Header Size | ? | ? |
| Use Cases | ? | ? |

**Solution:**

| Feature | TCP | UDP |
|---------|-----|-----|
| Connection Type | Connection-oriented | Connectionless |
| Reliability | Reliable (acknowledgments) | Unreliable (no acknowledgments) |
| Speed | Slower | Faster |
| Header Size | 20 bytes (minimum) | 8 bytes |
| Use Cases | HTTP, FTP, Email | DNS, Video streaming, VoIP |

---

## Exercise 6: Network vs Host Bits
**Question:** For the IP address 192.168.10.50/24:
- a) How many bits are used for the network?
- b) How many bits are used for hosts?
- c) What is the subnet mask?
- d) What is the network address?

**Solution:**
- a) **24 bits** for network (indicated by /24)
- b) **8 bits** for hosts (32 - 24 = 8)
- c) **Subnet mask:** 255.255.255.0
- d) **Network address:** 192.168.10.0

---

## Exercise 7: Broadcast Address
**Question:** Calculate the broadcast address for the network 192.168.10.0/24.

**Solution:**
- Network: 192.168.10.0/24
- Subnet mask: 255.255.255.0
- Last 8 bits are for hosts
- Set all host bits to 1: 192.168.10.11111111
- **Broadcast address:** 192.168.10.255

---

## Exercise 8: Valid Host Range
**Question:** For the network 10.20.30.0/24, determine:
- a) First valid host address
- b) Last valid host address
- c) Total number of usable host addresses

**Solution:**
- **Network address:** 10.20.30.0
- **Broadcast address:** 10.20.30.255
- a) **First valid host:** 10.20.30.1
- b) **Last valid host:** 10.20.30.254
- c) **Total usable hosts:** 2^8 - 2 = 254 hosts
  - (256 total addresses - network address - broadcast address)

---

## Exercise 9: MAC Address Format
**Question:** Which of the following MAC addresses are valid? Explain why or why not.
- a) 00:1A:2B:3C:4D:5E
- b) 00-1A-2B-3C-4D-5E
- c) 001A.2B3C.4D5E
- d) 00:1G:2B:3C:4D:5E

**Solution:**
- a) **Valid** - Colon-separated hexadecimal format
- b) **Valid** - Hyphen-separated hexadecimal format
- c) **Valid** - Cisco notation (dot-separated groups of 4)
- d) **Invalid** - Contains 'G' which is not a hexadecimal digit (0-9, A-F)

**Note:** MAC addresses are 48 bits (6 bytes) in hexadecimal.

---

## Exercise 10: Port Numbers
**Question:** Match the following well-known port numbers with their services:
- Ports: 20/21, 22, 23, 25, 53, 80, 443, 110, 143
- Services: HTTP, HTTPS, FTP, SSH, Telnet, SMTP, DNS, POP3, IMAP

**Solution:**
- **20/21** - FTP (File Transfer Protocol)
- **22** - SSH (Secure Shell)
- **23** - Telnet
- **25** - SMTP (Simple Mail Transfer Protocol)
- **53** - DNS (Domain Name System)
- **80** - HTTP (Hypertext Transfer Protocol)
- **443** - HTTPS (HTTP Secure)
- **110** - POP3 (Post Office Protocol v3)
- **143** - IMAP (Internet Message Access Protocol)

---

## Exercise 11: Subnetting - Number of Hosts
**Question:** How many usable host addresses are available in each of the following subnets?
- a) /25
- b) /26
- c) /27
- d) /30

**Solution:**
- a) **/25** → Host bits: 32 - 25 = 7 → 2^7 - 2 = **126 hosts**
- b) **/26** → Host bits: 32 - 26 = 6 → 2^6 - 2 = **62 hosts**
- c) **/27** → Host bits: 32 - 27 = 5 → 2^5 - 2 = **30 hosts**
- d) **/30** → Host bits: 32 - 30 = 2 → 2^2 - 2 = **2 hosts** (point-to-point links)

**Formula:** 2^(host bits) - 2

---

## Exercise 12: Private IP Ranges
**Question:** List all three private IP address ranges as defined by RFC 1918.

**Solution:**
1. **Class A:** 10.0.0.0 to 10.255.255.255 (10.0.0.0/8)
2. **Class B:** 172.16.0.0 to 172.31.255.255 (172.16.0.0/12)
3. **Class C:** 192.168.0.0 to 192.168.255.255 (192.168.0.0/16)

**Note:** These addresses are not routable on the public Internet.

---

## Exercise 13: CIDR Notation Conversion
**Question:** Convert the following subnet masks to CIDR notation:
- a) 255.255.255.0
- b) 255.255.255.128
- c) 255.255.240.0
- d) 255.255.255.252

**Solution:**
- a) 255.255.255.0 = 11111111.11111111.11111111.00000000 = **/24**
- b) 255.255.255.128 = 11111111.11111111.11111111.10000000 = **/25**
- c) 255.255.240.0 = 11111111.11111111.11110000.00000000 = **/20**
- d) 255.255.255.252 = 11111111.11111111.11111111.11111100 = **/30**

---

## Exercise 14: Basic Subnetting Problem
**Question:** You have the network 192.168.1.0/24. Divide it into 4 equal subnets. For each subnet, provide:
- Subnet address
- Subnet mask
- First usable host
- Last usable host
- Broadcast address

**Solution:**
To create 4 subnets, we need 2 additional bits (2^2 = 4).
New subnet mask: /26 (255.255.255.192)
Each subnet has 64 addresses (2^6).

**Subnet 1:**
- Subnet: 192.168.1.0/26
- Mask: 255.255.255.192
- First host: 192.168.1.1
- Last host: 192.168.1.62
- Broadcast: 192.168.1.63

**Subnet 2:**
- Subnet: 192.168.1.64/26
- Mask: 255.255.255.192
- First host: 192.168.1.65
- Last host: 192.168.1.126
- Broadcast: 192.168.1.127

**Subnet 3:**
- Subnet: 192.168.1.128/26
- Mask: 255.255.255.192
- First host: 192.168.1.129
- Last host: 192.168.1.190
- Broadcast: 192.168.1.191

**Subnet 4:**
- Subnet: 192.168.1.192/26
- Mask: 255.255.255.192
- First host: 192.168.1.193
- Last host: 192.168.1.254
- Broadcast: 192.168.1.255

---

## Exercise 15: Three-Way Handshake
**Question:** Describe the TCP three-way handshake process. What flags are set in each step?

**Solution:**
The TCP three-way handshake establishes a connection between client and server:

**Step 1: SYN**
- Client → Server
- Flags: SYN = 1
- Client sends SYN packet with initial sequence number (ISN)

**Step 2: SYN-ACK**
- Server → Client
- Flags: SYN = 1, ACK = 1
- Server acknowledges client's SYN and sends its own SYN with its ISN
- ACK number = Client's ISN + 1

**Step 3: ACK**
- Client → Server
- Flags: ACK = 1
- Client acknowledges server's SYN
- ACK number = Server's ISN + 1

After these three steps, the connection is established and data transfer can begin.

---

## Exercise 16: IPv4 Header Fields
**Question:** List and briefly explain 5 important fields in the IPv4 header.

**Solution:**
1. **Version (4 bits):** Indicates IP version (IPv4 = 4)
2. **Header Length (4 bits):** Length of header in 32-bit words
3. **Total Length (16 bits):** Total length of IP packet (header + data)
4. **Time to Live - TTL (8 bits):** Prevents packets from looping indefinitely; decremented by each router
5. **Protocol (8 bits):** Identifies next-level protocol (6 = TCP, 17 = UDP, 1 = ICMP)
6. **Source IP Address (32 bits):** IP address of sender
7. **Destination IP Address (32 bits):** IP address of recipient

---

## Exercise 17: Calculate Subnet Mask
**Question:** A network administrator needs to create subnets for 50 hosts each. What is the appropriate subnet mask for a Class C network (starting with 192.168.1.0)?

**Solution:**
- Need 50 usable hosts per subnet
- Formula: 2^n - 2 ≥ 50
- 2^6 - 2 = 62 hosts ✓ (2^5 - 2 = 30 is too few)
- Need 6 bits for hosts
- Network bits: 32 - 6 = 26 bits

**Answer:**
- **CIDR notation:** /26
- **Subnet mask:** 255.255.255.192
- **Number of subnets possible:** 4 (from original /24)
- **Usable hosts per subnet:** 62

---

## Exercise 18: Loopback and Special Addresses
**Question:** Explain the purpose of the following special IP addresses:
- a) 127.0.0.1
- b) 0.0.0.0
- c) 255.255.255.255
- d) 169.254.x.x

**Solution:**
- a) **127.0.0.1** - Loopback address (localhost), used to test TCP/IP stack on local machine
- b) **0.0.0.0** - Represents "any address" or unknown address; used by hosts during DHCP discovery
- c) **255.255.255.255** - Limited broadcast address; packet sent to all devices on local network
- d) **169.254.x.x** - APIPA (Automatic Private IP Addressing); self-assigned when DHCP fails

---

## Exercise 19: Maximum Transmission Unit (MTU)
**Question:** 
- a) What is the standard MTU for Ethernet?
- b) A packet of 2000 bytes needs to be transmitted over Ethernet. How many fragments will be created? (Assume 20-byte IP header)

**Solution:**
- a) **Standard Ethernet MTU:** 1500 bytes

- b) **Fragmentation calculation:**
  - Total packet size: 2000 bytes
  - Available payload per fragment: 1500 - 20 (IP header) = 1480 bytes
  - First fragment: 1480 bytes of data + 20 byte header = 1500 bytes
  - Second fragment: 520 bytes of data + 20 byte header = 540 bytes
  - **Answer: 2 fragments**

---

## Exercise 20: ARP (Address Resolution Protocol)
**Question:** 
- a) What is the purpose of ARP?
- b) Host A (IP: 192.168.1.10, MAC: AA:AA:AA:AA:AA:AA) wants to communicate with Host B (IP: 192.168.1.20). Host A doesn't know Host B's MAC address. Describe the ARP process.

**Solution:**
- a) **Purpose of ARP:** Maps IP addresses (Layer 3) to MAC addresses (Layer 2) on a local network.

- b) **ARP Process:**

**Step 1: ARP Request (Broadcast)**
- Source IP: 192.168.1.10
- Source MAC: AA:AA:AA:AA:AA:AA
- Target IP: 192.168.1.20
- Target MAC: FF:FF:FF:FF:FF:FF (broadcast)
- Message: "Who has IP 192.168.1.20? Tell 192.168.1.10"
- Sent to all devices on the local network

**Step 2: ARP Reply (Unicast)**
- Host B responds directly to Host A
- Source IP: 192.168.1.20
- Source MAC: BB:BB:BB:BB:BB:BB (Host B's MAC)
- Target IP: 192.168.1.10
- Target MAC: AA:AA:AA:AA:AA:AA
- Message: "192.168.1.20 is at BB:BB:BB:BB:BB:BB"

**Step 3: Cache Update**
- Host A stores the mapping in its ARP cache
- Future communications don't require ARP requests until cache expires

---

## Summary
You've completed Part 1! You should now understand:
- OSI Model layers
- IP addressing and classification
- Binary/decimal conversions
- Subnet masks and CIDR notation
- Basic subnetting
- TCP vs UDP
- Port numbers
- MAC addresses
- Special IP addresses
- ARP protocol

**Next:** Proceed to Part 2 for advanced topics including IP tables, fragmentation, windowing, and complex routing scenarios.
