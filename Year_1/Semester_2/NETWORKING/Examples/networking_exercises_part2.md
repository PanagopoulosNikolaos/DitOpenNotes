# Networking Exercises - Part 2: Advanced Topics
## Comprehensive Exam Preparation

This file contains 20 advanced networking exercises covering IP tables, fragmentation, windowing, routing protocols, and complex scenarios. These exercises simulate real exam conditions.

---

## Exercise 1: Complex Subnetting with VLSM
**Question:** You are given the network 172.16.0.0/16. Design a VLSM (Variable Length Subnet Mask) scheme for the following requirements:
- Network A: 5000 hosts
- Network B: 2000 hosts
- Network C: 500 hosts
- Network D: 100 hosts
- Network E: 2 hosts (point-to-point link)

For each network, provide: subnet address, subnet mask, first host, last host, and broadcast address.

**Solution:**

Start with the largest network and work down:

**Network A: 5000 hosts**
- Need: 2^n - 2 ≥ 5000 → 2^13 - 2 = 8190 hosts ✓
- Host bits: 13, Network bits: 32 - 13 = 19
- Subnet: 172.16.0.0/19
- Mask: 255.255.224.0
- Range: 172.16.0.0 - 172.16.31.255
- First host: 172.16.0.1
- Last host: 172.16.31.254
- Broadcast: 172.16.31.255

**Network B: 2000 hosts**
- Need: 2^11 - 2 = 2046 hosts ✓
- Host bits: 11, Network bits: 21
- Subnet: 172.16.32.0/21
- Mask: 255.255.248.0
- Range: 172.16.32.0 - 172.16.39.255
- First host: 172.16.32.1
- Last host: 172.16.39.254
- Broadcast: 172.16.39.255

**Network C: 500 hosts**
- Need: 2^9 - 2 = 510 hosts ✓
- Host bits: 9, Network bits: 23
- Subnet: 172.16.40.0/23
- Mask: 255.255.254.0
- Range: 172.16.40.0 - 172.16.41.255
- First host: 172.16.40.1
- Last host: 172.16.41.254
- Broadcast: 172.16.41.255

**Network D: 100 hosts**
- Need: 2^7 - 2 = 126 hosts ✓
- Host bits: 7, Network bits: 25
- Subnet: 172.16.42.0/25
- Mask: 255.255.255.128
- Range: 172.16.42.0 - 172.16.42.127
- First host: 172.16.42.1
- Last host: 172.16.42.126
- Broadcast: 172.16.42.127

**Network E: 2 hosts (point-to-point)**
- Need: 2^2 - 2 = 2 hosts ✓
- Host bits: 2, Network bits: 30
- Subnet: 172.16.42.128/30
- Mask: 255.255.255.252
- Range: 172.16.42.128 - 172.16.42.131
- First host: 172.16.42.129
- Last host: 172.16.42.130
- Broadcast: 172.16.42.131

---

## Exercise 2: Routing Table Interpretation
**Question:** Given the following routing table, determine the next hop for packets destined to:
- a) 192.168.50.25
- b) 10.0.0.5
- c) 172.16.100.50
- d) 8.8.8.8

**Routing Table:**
```
Destination      Netmask          Gateway         Interface
192.168.50.0     255.255.255.0    0.0.0.0         eth0
10.0.0.0         255.0.0.0        192.168.50.1    eth0
172.16.0.0       255.255.0.0      192.168.50.2    eth0
0.0.0.0          0.0.0.0          192.168.50.254  eth0
```

**Solution:**

- a) **192.168.50.25**
  - Matches: 192.168.50.0/24 (most specific)
  - Gateway: 0.0.0.0 (directly connected)
  - Interface: eth0
  - **Action:** Deliver directly on local network

- b) **10.0.0.5**
  - Matches: 10.0.0.0/8
  - Gateway: 192.168.50.1
  - Interface: eth0
  - **Next hop:** 192.168.50.1

- c) **172.16.100.50**
  - Matches: 172.16.0.0/16
  - Gateway: 192.168.50.2
  - Interface: eth0
  - **Next hop:** 192.168.50.2

- d) **8.8.8.8**
  - Matches: 0.0.0.0/0 (default route)
  - Gateway: 192.168.50.254
  - Interface: eth0
  - **Next hop:** 192.168.50.254 (default gateway)

**Note:** The router always selects the most specific route (longest prefix match).

---

## Exercise 3: IP Fragmentation with MF and DF Flags
**Question:** A router receives an IP packet with:
- Total Length: 3000 bytes
- Header Length: 20 bytes
- DF flag: 0 (fragmentation allowed)
- Identification: 12345
- MTU of outgoing link: 1500 bytes

Calculate the fragmentation details for all fragments including:
- Fragment size
- MF (More Fragments) flag
- Fragment Offset
- Total Length field

**Solution:**

**Fragment Calculations:**
- Data to fragment: 3000 - 20 = 2980 bytes
- Maximum data per fragment: 1500 - 20 = 1480 bytes
- Fragment offset unit: 8 bytes
- Data must be multiple of 8: 1480 ÷ 8 = 185 (no remainder, good)

**Fragment 1:**
- Data: 1480 bytes (offset 0 to 1479)
- Total Length: 1480 + 20 = 1500 bytes
- MF flag: 1 (more fragments follow)
- DF flag: 0
- Fragment Offset: 0 ÷ 8 = 0
- Identification: 12345

**Fragment 2:**
- Data: 1480 bytes (offset 1480 to 2959)
- Total Length: 1480 + 20 = 1500 bytes
- MF flag: 1 (more fragments follow)
- DF flag: 0
- Fragment Offset: 1480 ÷ 8 = 185
- Identification: 12345

**Fragment 3:**
- Data: 1020 bytes (offset 2960 to 3979, but only 2980 bytes exist)
- Actual data: 2980 - 2960 = 20 bytes
- Total Length: 20 + 20 = 40 bytes
- MF flag: 0 (last fragment)
- DF flag: 0
- Fragment Offset: 2960 ÷ 8 = 370
- Identification: 12345

**Summary Table:**

| Fragment | Total Length | Data Size | MF | Offset | Offset (bytes) |
|----------|--------------|-----------|-----|--------|----------------|
| 1        | 1500         | 1480      | 1   | 0      | 0              |
| 2        | 1500         | 1480      | 1   | 185    | 1480           |
| 3        | 40           | 20        | 0   | 370    | 2960           |

---

## Exercise 4: TCP Sliding Window Protocol
**Question:** Host A is sending data to Host B with:
- Initial sequence number: 1000
- Window size: 4000 bytes
- Segment size: 1000 bytes

Draw the transmission timeline showing:
- Segments sent
- Acknowledgments received
- Window movements

Assume:
- Segment 1 RTT: 100ms
- Segment 2 is lost
- Segment 3 RTT: 100ms
- Segment 4 RTT: 100ms

**Solution:**

**Time 0ms:** 
- Send Seg1 (seq=1000, len=1000) [1000-1999]
- Send Seg2 (seq=2000, len=1000) [2000-2999]
- Send Seg3 (seq=3000, len=1000) [3000-3999]
- Send Seg4 (seq=4000, len=1000) [4000-4999]
- Window: [1000-4999] (full)

**Time 100ms:**
- Receive ACK=2000 (acknowledges Seg1)
- Window slides: [2000-5999]
- Send Seg5 (seq=5000, len=1000) [5000-5999]
- **Problem:** Seg2 was lost, no ACK=3000 arrives

**Time 200ms:**
- Receive ACK=2000 (duplicate - Seg3 arrived but out of order)
- Receive ACK=2000 (duplicate - Seg4 arrived but out of order)
- **Receiver cannot ACK beyond 2000 due to gap**

**Time 300ms:**
- Receive ACK=2000 (third duplicate from Seg5)
- **Fast Retransmit triggered!**
- Retransmit Seg2 (seq=2000, len=1000)

**Time 400ms:**
- Receive ACK=6000 (cumulative ACK for Seg2-5)
- Window slides: [6000-9999]
- Continue transmission

**Key Points:**
- TCP uses cumulative acknowledgments
- Receiver cannot ACK beyond missing segment
- Three duplicate ACKs trigger fast retransmit
- Sliding window allows pipelining for efficiency

---

## Exercise 5: Complete IP Routing Table Exercise
**Question:** Fill in the missing entries in the routing table:

| Destination Network | Subnet Mask    | Next Hop    | Interface | Metric |
|---------------------|----------------|-------------|-----------|--------|
| 192.168.10.0        | ?              | 0.0.0.0     | eth0      | 0      |
| 10.0.0.0            | 255.0.0.0      | ?           | eth0      | 1      |
| ?                   | 255.255.255.0  | 10.20.30.1  | eth1      | 2      |
| 0.0.0.0             | ?              | 192.168.10.1| eth0      | 10     |

Additional info:
- eth0 IP: 192.168.10.50/24
- eth1 IP: 10.20.30.50/24
- The third entry is for a remote network with 100 usable hosts
- Gateway on 10.0.0.0 network is first usable IP

**Solution:**

| Destination Network | Subnet Mask      | Next Hop     | Interface | Metric |
|---------------------|------------------|--------------|-----------|--------|
| 192.168.10.0        | **255.255.255.0**| 0.0.0.0      | eth0      | 0      |
| 10.0.0.0            | 255.0.0.0        | **10.20.30.1**| eth0     | 1      |
| **172.16.5.0**      | 255.255.255.0    | 10.20.30.1   | eth1      | 2      |
| 0.0.0.0             | **0.0.0.0**      | 192.168.10.1 | eth0      | 10     |

**Explanation:**
1. First entry: Directly connected network on eth0 (/24 = 255.255.255.0)
2. Second entry: Gateway must be reachable, so use gateway on eth1's network (10.20.30.1)
3. Third entry: 100 hosts need /25 minimum (2^7-2=126), but answer shows /24 (254 hosts); destination can be any valid network (e.g., 172.16.5.0)
4. Fourth entry: Default route uses 0.0.0.0/0 (0.0.0.0 mask)

---

## Exercise 6: TCP Congestion Window (CWND)
**Question:** Explain TCP congestion control using slow start and congestion avoidance. Given:
- Initial CWND: 1 MSS (Maximum Segment Size = 1460 bytes)
- ssthresh (slow start threshold): 8 MSS
- All ACKs received successfully

Calculate CWND values for the first 10 RTTs.

**Solution:**

**Slow Start Phase (CWND < ssthresh):**
- CWND doubles every RTT
- Exponential growth

**Congestion Avoidance Phase (CWND ≥ ssthresh):**
- CWND increases by 1 MSS per RTT
- Linear growth

**Calculation:**

| RTT | Phase             | CWND (MSS) | CWND (bytes) | Segments Sent |
|-----|-------------------|------------|--------------|---------------|
| 0   | Slow Start        | 1          | 1460         | 1             |
| 1   | Slow Start        | 2          | 2920         | 2             |
| 2   | Slow Start        | 4          | 5840         | 4             |
| 3   | Slow Start        | 8          | 11680        | 8             |
| 4   | Congestion Avoid. | 9          | 13140        | 9             |
| 5   | Congestion Avoid. | 10         | 14600        | 10            |
| 6   | Congestion Avoid. | 11         | 16060        | 11            |
| 7   | Congestion Avoid. | 12         | 17520        | 12            |
| 8   | Congestion Avoid. | 13         | 18980        | 13            |
| 9   | Congestion Avoid. | 14         | 20440        | 14            |
| 10  | Congestion Avoid. | 15         | 21900        | 15            |

**Key Points:**
- Slow start: CWND doubles (1→2→4→8)
- At RTT 3, CWND = ssthresh = 8, switch to congestion avoidance
- Congestion avoidance: CWND += 1 per RTT (8→9→10...)

---

## Exercise 7: NAT (Network Address Translation) Table
**Question:** A company uses NAT with:
- Private network: 192.168.1.0/24
- Public IP: 203.0.113.5
- NAT router translates using port numbers

Fill in the NAT translation table:

**Outbound Connections:**

| Inside Local      | Inside Global      | Outside Global    |
|-------------------|--------------------|-------------------|
| 192.168.1.10:5000 | ?                  | 8.8.8.8:53       |
| 192.168.1.15:5001 | ?                  | 93.184.216.34:80 |
| ?                 | 203.0.113.5:1026   | 151.101.1.69:443 |

**Solution:**

| Inside Local      | Inside Global      | Outside Global    |
|-------------------|--------------------|-------------------|
| 192.168.1.10:5000 | **203.0.113.5:1024**| 8.8.8.8:53       |
| 192.168.1.15:5001 | **203.0.113.5:1025**| 93.184.216.34:80 |
| **192.168.1.x:yyyy**| 203.0.113.5:1026 | 151.101.1.69:443 |

**Explanation:**
- Inside Local: Original private IP:port
- Inside Global: Translated public IP:port (NAT assigns unique ports)
- Outside Global: Destination server IP:port
- NAT router maintains this table to route return traffic correctly
- For third entry, private IP cannot be determined without additional info

**Return Traffic Example:**
- Packet arrives: From 8.8.8.8:53 to 203.0.113.5:1024
- NAT looks up 203.0.113.5:1024 → 192.168.1.10:5000
- Forwards to internal host

---

## Exercise 8: Packet Fragmentation Offset Calculation
**Question:** You receive three IP fragments with the following details:

| Fragment | Total Length | Header Length | MF | Offset |
|----------|--------------|---------------|-----|--------|
| A        | 1500         | 20            | 1   | 0      |
| B        | 1500         | 20            | 1   | 185    |
| C        | 540          | 20            | 0   | 370    |

- a) What was the original packet's data size?
- b) Reconstruct the byte ranges for each fragment
- c) Verify the fragmentation is correct

**Solution:**

**a) Original packet data size:**
- Fragment C has MF=0 (last fragment)
- Fragment C offset: 370 × 8 = 2960 bytes
- Fragment C data: 540 - 20 = 520 bytes
- Last byte position: 2960 + 520 = 3480 bytes
- **Original data size: 3480 bytes**
- **Original packet size: 3480 + 20 = 3500 bytes**

**b) Byte ranges:**

**Fragment A:**
- Offset: 0 × 8 = 0
- Data length: 1500 - 20 = 1480 bytes
- Range: bytes 0-1479
- MF=1 ✓ (more fragments)

**Fragment B:**
- Offset: 185 × 8 = 1480
- Data length: 1500 - 20 = 1480 bytes
- Range: bytes 1480-2959
- MF=1 ✓ (more fragments)

**Fragment C:**
- Offset: 370 × 8 = 2960
- Data length: 540 - 20 = 520 bytes
- Range: bytes 2960-3479
- MF=0 ✓ (last fragment)

**c) Verification:**
- Fragment A ends at byte 1479
- Fragment B starts at byte 1480 ✓ (no gap)
- Fragment B ends at byte 2959
- Fragment C starts at byte 2960 ✓ (no gap)
- Fragment C is last (MF=0) ✓
- **Fragmentation is correct!**

---

## Exercise 9: CIDR Supernetting (Route Summarization)
**Question:** You have the following networks:
- 192.168.16.0/24
- 192.168.17.0/24
- 192.168.18.0/24
- 192.168.19.0/24

Find the single CIDR route that summarizes all four networks.

**Solution:**

**Step 1: Convert to binary (third octet only)**
- 192.168.**16**.0/24 = 192.168.**00010000**.0
- 192.168.**17**.0/24 = 192.168.**00010001**.0
- 192.168.**18**.0/24 = 192.168.**00010010**.0
- 192.168.**19**.0/24 = 192.168.**00010011**.0

**Step 2: Find common bits**
```
00010000
00010001
00010010
00010011
------
0001xxxx  ← First 4 bits are common
```

**Step 3: Calculate summary**
- Common prefix in third octet: 0001 (4 bits)
- Total network bits: 16 (first two octets) + 4 = 20 bits
- Summary: **192.168.16.0/22**
- Subnet mask: **255.255.252.0**

**Step 4: Verification**
- 192.168.16.0/22 covers: 192.168.16.0 to 192.168.19.255
- Binary: 192.168.000100xx.xxxxxxxx
- This includes all four /24 networks ✓

**Answer: 192.168.16.0/22**

---

## Exercise 10: TCP Window Size and Throughput
**Question:** Calculate the maximum throughput for a TCP connection with:
- RTT (Round Trip Time): 100 ms
- Window size: 64 KB
- No packet loss

Then determine the required window size for 100 Mbps throughput with the same RTT.

**Solution:**

**Part 1: Maximum Throughput**

Formula: **Throughput = Window Size / RTT**

- Window size: 64 KB = 64 × 1024 = 65,536 bytes = 524,288 bits
- RTT: 100 ms = 0.1 seconds
- Throughput = 524,288 bits / 0.1 s = **5,242,880 bps = 5.24 Mbps**

**Part 2: Required Window Size for 100 Mbps**

Rearranging: **Window Size = Throughput × RTT**

- Throughput: 100 Mbps = 100,000,000 bps
- RTT: 0.1 seconds
- Window size = 100,000,000 × 0.1 = 10,000,000 bits = 1,250,000 bytes
- **Window size = 1.25 MB = 1,220 KB**

**Bandwidth-Delay Product (BDP):**
- BDP = Bandwidth × RTT
- BDP = 100 Mbps × 100 ms = 10 Mb = 1.25 MB
- Window size must be ≥ BDP for optimal throughput

---

## Exercise 11: Subnet Design with Requirements
**Question:** Design a subnet scheme for a company with three departments:
- Sales: 60 hosts
- Engineering: 120 hosts
- Management: 30 hosts

Use the network 192.168.100.0/24. Minimize IP waste.

**Solution:**

**Step 1: Sort by size (largest first)**
1. Engineering: 120 hosts
2. Sales: 60 hosts
3. Management: 30 hosts

**Step 2: Engineering subnet (120 hosts)**
- Need: 2^n - 2 ≥ 120 → 2^7 - 2 = 126 ✓
- Subnet: 192.168.100.0/25
- Mask: 255.255.255.128
- Hosts: 126 usable
- Range: 192.168.100.0 - 192.168.100.127
- First host: 192.168.100.1
- Last host: 192.168.100.126
- Broadcast: 192.168.100.127

**Step 3: Sales subnet (60 hosts)**
- Need: 2^6 - 2 = 62 ✓
- Subnet: 192.168.100.128/26
- Mask: 255.255.255.192
- Hosts: 62 usable
- Range: 192.168.100.128 - 192.168.100.191
- First host: 192.168.100.129
- Last host: 192.168.100.190
- Broadcast: 192.168.100.191

**Step 4: Management subnet (30 hosts)**
- Need: 2^5 - 2 = 30 ✓
- Subnet: 192.168.100.192/27
- Mask: 255.255.255.224
- Hosts: 30 usable
- Range: 192.168.100.192 - 192.168.100.223
- First host: 192.168.100.193
- Last host: 192.168.100.222
- Broadcast: 192.168.100.223

**Step 5: Remaining space**
- Available: 192.168.100.224 - 192.168.100.255 (32 addresses)
- Can be used for future expansion or point-to-point links

---

## Exercise 12: IPv4 Header Checksum Verification
**Question:** Given an IPv4 header (simplified):

```
Version/IHL: 0x45
Type of Service: 0x00
Total Length: 0x003C (60 bytes)
Identification: 0x1A2B
Flags/Fragment: 0x4000
TTL: 0x40 (64)
Protocol: 0x06 (TCP)
Header Checksum: 0xB861
Source IP: 192.168.1.1 (0xC0A80101)
Dest IP: 10.0.0.5 (0x0A000005)
```

Verify if the checksum is correct.

**Solution:**

**Step 1: Sum all 16-bit words (excluding checksum field)**

```
0x4500  (Version/IHL + TOS)
0x003C  (Total Length)
0x1A2B  (Identification)
0x4000  (Flags/Fragment)
0x4006  (TTL + Protocol)
[Skip checksum field]
0xC0A8  (Source IP - upper)
0x0101  (Source IP - lower)
0x0A00  (Dest IP - upper)
0x0005  (Dest IP - lower)
```

**Step 2: Add values**
```
  4500
  003C
  1A2B
  4000
  4006
  C0A8
  0101
  0A00
+ 0005
------
 1479F (carry: 1, sum: 479F)
```

**Step 3: Add carry**
```
  479F
+    1
------
  47A0
```

**Step 4: One's complement**
```
47A0 → B85F (flip all bits)
```

**Expected checksum: 0xB85F**
**Given checksum: 0xB861**

**Result: Checksum is INCORRECT** ❌

The packet may be corrupted and should be discarded.

**Note:** This simplified example demonstrates the checksum algorithm. Actual headers may have options that affect the calculation.

---

## Exercise 13: Bandwidth Calculation with Overhead
**Question:** A satellite link has:
- Physical bandwidth: 10 Mbps
- IP header: 20 bytes
- TCP header: 20 bytes
- Application data per packet: 1000 bytes
- Propagation delay: 270 ms (one way)

Calculate:
- a) Efficiency (%)
- b) Effective application throughput
- c) RTT
- d) Maximum window size needed for full bandwidth utilization

**Solution:**

**a) Efficiency:**
- Total packet size: 20 + 20 + 1000 = 1040 bytes
- Payload: 1000 bytes
- Overhead: 40 bytes
- Efficiency = (1000 / 1040) × 100 = **96.15%**

**b) Effective throughput:**
- Physical bandwidth: 10 Mbps
- Effective throughput = 10 × 0.9615 = **9.615 Mbps**

**c) RTT:**
- One-way delay: 270 ms
- RTT = 2 × 270 = **540 ms**

**d) Maximum window size:**
- BDP = Bandwidth × RTT
- BDP = 10 Mbps × 0.54 s = 5.4 Mb = 675,000 bytes
- **Window size needed: 675 KB ≈ 659 KB**

For TCP window scaling, this requires window scale option since standard TCP window field is only 16 bits (max 64 KB).

---

## Exercise 14: Distance Vector Routing (RIP)
**Question:** Given the following network topology and initial routing tables:

```
Router A --- 5 --- Router B --- 10 --- Router C
   |                  |
   8                  3
   |                  |
Router D ------------ 7 ----------- Router E
```

Complete Router B's routing table after one update cycle using RIP (count-to-infinity not considered).

**Initial Router B table:**
| Destination | Cost | Next Hop |
|-------------|------|----------|
| A           | 5    | A        |
| B           | 0    | -        |
| C           | 10   | C        |

**Router B receives updates from neighbors:**
- From A: {D: 8, E: ∞}
- From C: {E: 3}
- From D: {A: 8, E: 7}

**Solution:**

**Update process:**

**Route to D:**
- Via A: 5 (A→B) + 8 (A→D) = 13
- Via D: 3 (D→B direct, need to check topology) - NOT DIRECT CONNECTION
- Via C: not advertised
- **Best: cost 13 via A** (if A-D link exists)
- Note: Topology doesn't show direct B-D, so via A

**Route to E:**
- Via A: 5 + ∞ = ∞
- Via C: 10 (B→C) + 3 (C→E) = 13
- Via D: not directly connected
- **Best: cost 13 via C**

**Updated Router B table:**
| Destination | Cost | Next Hop |
|-------------|------|----------|
| A           | 5    | A        |
| B           | 0    | -        |
| C           | 10   | C        |
| D           | 13   | A        |
| E           | 13   | C        |

**Note:** RIP uses hop count (max 15). This example uses link costs.

---

## Exercise 15: TCP Sequence Numbers and Acknowledgments
**Question:** A TCP connection has:
- Client ISN (Initial Sequence Number): 3000
- Server ISN: 5000
- Client sends 500 bytes of data
- Server sends 300 bytes of data
- Then client sends another 200 bytes

Show the sequence and acknowledgment numbers for each segment.

**Solution:**

**Segment 1: Three-way handshake - SYN**
- Direction: Client → Server
- Flags: SYN
- SEQ: 3000
- ACK: (none)
- Data: 0 bytes

**Segment 2: Three-way handshake - SYN-ACK**
- Direction: Server → Client
- Flags: SYN, ACK
- SEQ: 5000
- ACK: 3001 (acknowledges SYN, which consumes 1 seq number)
- Data: 0 bytes

**Segment 3: Three-way handshake - ACK**
- Direction: Client → Server
- Flags: ACK
- SEQ: 3001
- ACK: 5001 (acknowledges SYN)
- Data: 0 bytes

**Segment 4: Client data**
- Direction: Client → Server
- Flags: PSH, ACK
- SEQ: 3001
- ACK: 5001
- Data: 500 bytes (SEQ 3001-3500)

**Segment 5: Server ACK + data**
- Direction: Server → Client
- Flags: PSH, ACK
- SEQ: 5001
- ACK: 3501 (acknowledges 500 bytes)
- Data: 300 bytes (SEQ 5001-5300)

**Segment 6: Client ACK + data**
- Direction: Client → Server
- Flags: PSH, ACK
- SEQ: 3501
- ACK: 5301 (acknowledges 300 bytes)
- Data: 200 bytes (SEQ 3501-3700)

**Segment 7: Server ACK**
- Direction: Server → Client
- Flags: ACK
- SEQ: 5301
- ACK: 3701 (acknowledges 200 bytes)
- Data: 0 bytes

**Summary:**
- SEQ numbers advance by data bytes sent
- ACK numbers indicate next expected byte
- SYN and FIN flags consume 1 sequence number each

---

## Exercise 16: Complex Packet Flow with TTL
**Question:** A packet travels through the following path:

```
Source (192.168.1.10) → Router A → Router B → Router C → Destination (10.0.0.5)
Initial TTL: 5
```

At each router:
- Router A: TTL decremented, forwards packet
- Router B: TTL decremented, forwards packet
- Router C: TTL decremented, should forward but...

What happens at each hop? What ICMP message (if any) is generated?

**Solution:**

**At Source:**
- Packet created
- TTL: 5
- Action: Send to Router A

**At Router A:**
- Receives packet, TTL: 5
- Decrements TTL: 5 - 1 = 4
- Check: TTL > 0 ✓
- Action: Forward to Router B

**At Router B:**
- Receives packet, TTL: 4
- Decrements TTL: 4 - 1 = 3
- Check: TTL > 0 ✓
- Action: Forward to Router C

**At Router C:**
- Receives packet, TTL: 3
- Decrements TTL: 3 - 1 = 2
- Check: TTL > 0 ✓
- Action: Forward to destination

**At Destination:**
- Receives packet, TTL: 2
- Packet delivered successfully ✓

**Scenario 2: If initial TTL was 3:**

**At Router C:**
- Receives packet, TTL: 1
- Decrements TTL: 1 - 1 = 0
- Check: TTL = 0 ✗ **DISCARD PACKET**
- Action: 
  - Drop packet
  - Generate **ICMP Time Exceeded** message
  - Send to source: 192.168.1.10
  - ICMP Type: 11 (Time Exceeded)
  - ICMP Code: 0 (TTL expired in transit)

**Purpose of TTL:**
- Prevents packets from looping infinitely
- Each router decrements by 1
- When TTL reaches 0, packet is dropped
- Used by traceroute to map network paths

---

## Exercise 17: IPv6 Address Compression
**Question:** Compress the following IPv6 addresses using standard notation rules:

a) 2001:0DB8:0000:0000:0000:0000:0000:0001
b) FE80:0000:0000:0000:0202:B3FF:FE1E:8329
c) 2001:0DB8:0000:0042:0000:8A2E:0370:7334
d) 0000:0000:0000:0000:0000:0000:0000:0001

**Solution:**

**Rules:**
1. Remove leading zeros in each group
2. Replace longest string of consecutive zero groups with ::
3. Use :: only once

**a) 2001:0DB8:0000:0000:0000:0000:0000:0001**
- Remove leading zeros: 2001:DB8:0:0:0:0:0:1
- Replace longest zero string: **2001:DB8::1**

**b) FE80:0000:0000:0000:0202:B3FF:FE1E:8329**
- Remove leading zeros: FE80:0:0:0:202:B3FF:FE1E:8329
- Replace longest zero string: **FE80::202:B3FF:FE1E:8329**

**c) 2001:0DB8:0000:0042:0000:8A2E:0370:7334**
- Remove leading zeros: 2001:DB8:0:42:0:8A2E:370:7334
- Replace first/longest zero string: **2001:DB8:0:42::8A2E:370:7334**
- Alternative: 2001:DB8::42:0:8A2E:370:7334 (both valid, use first occurrence)

**d) 0000:0000:0000:0000:0000:0000:0000:0001**
- This is the loopback address: **::1**

**Expanding back example (::1):**
- :: represents 7 groups of zeros (since one group is :1)
- Expanded: 0000:0000:0000:0000:0000:0000:0000:0001

---

## Exercise 18: Buffer Overflow and Window Management
**Question:** A receiver has:
- Buffer size: 8000 bytes
- Application reads 1000 bytes every 100ms
- Sender transmits 2000 bytes every 50ms

Model the buffer state and TCP window advertisements for 500ms.

**Solution:**

| Time (ms) | Event                    | Buffer Used | Available | Window Advertised |
|-----------|--------------------------|-------------|-----------|-------------------|
| 0         | Initial                  | 0           | 8000      | 8000              |
| 50        | Receive 2000 bytes       | 2000        | 6000      | 6000              |
| 100       | Receive 2000 bytes       | 4000        | 4000      | 4000              |
|           | App reads 1000 bytes     | 3000        | 5000      | 5000              |
| 150       | Receive 2000 bytes       | 5000        | 3000      | 3000              |
| 200       | Receive 2000 bytes       | 7000        | 1000      | 1000              |
|           | App reads 1000 bytes     | 6000        | 2000      | 2000              |
| 250       | Receive 2000 bytes       | 8000        | 0         | **0 (FULL!)**     |
|           |                          |             |           | **Zero Window**   |
| 300       | **Sender must stop**     | 8000        | 0         | 0                 |
|           | App reads 1000 bytes     | 7000        | 1000      | 1000              |
| 350       | **Window update sent**   | 7000        | 1000      | 1000              |
| 400       | App reads 1000 bytes     | 6000        | 2000      | 2000              |
| 450       | Receive 2000 bytes       | 8000        | 0         | 0                 |
| 500       | App reads 1000 bytes     | 7000        | 1000      | 1000              |

**Analysis:**
- **At 250ms:** Buffer full! Receiver advertises window = 0
- Sender must stop transmitting
- **Silly Window Syndrome:** Small window advertisements are inefficient
- **Solution:** Delayed ACK or wait until substantial space available

**Flow Control:**
- TCP window prevents sender from overwhelming receiver
- Window size dynamically adjusts based on buffer availability
- Zero window probe: Sender periodically checks if window opened

---

## Exercise 19: Routing Protocol Comparison
**Question:** Complete the comparison table for RIP, OSPF, and BGP:

| Feature              | RIP | OSPF | BGP |
|----------------------|-----|------|-----|
| Type                 | ?   | ?    | ?   |
| Metric               | ?   | ?    | ?   |
| Max Network Size     | ?   | ?    | ?   |
| Convergence Speed    | ?   | ?    | ?   |
| Algorithm            | ?   | ?    | ?   |
| Use Case             | ?   | ?    | ?   |

**Solution:**

| Feature              | RIP                | OSPF                | BGP                    |
|----------------------|--------------------|---------------------|------------------------|
| Type                 | Distance Vector    | Link State          | Path Vector            |
| Metric               | Hop count          | Cost (bandwidth)    | AS path, policies      |
| Max Network Size     | 15 hops (small)    | Large (areas)       | Internet-scale         |
| Convergence Speed    | Slow (minutes)     | Fast (seconds)      | Slow (path-dependent)  |
| Algorithm            | Bellman-Ford       | Dijkstra (SPF)      | Path attributes        |
| Use Case             | Small networks     | Enterprise          | Internet (ISPs)        |
| Protocol Type        | IGP                | IGP                 | EGP                    |
| Update Method        | Periodic (30s)     | Event-triggered     | Incremental            |
| Overhead             | High               | Moderate            | Low after convergence  |

**Additional Details:**

**RIP (Routing Information Protocol):**
- Simple, easy to configure
- Max 15 hops (16 = infinity)
- Count-to-infinity problem
- RIPv2 supports CIDR

**OSPF (Open Shortest Path First):**
- Hierarchical (areas, backbone)
- Fast convergence
- Supports VLSM
- Complex configuration

**BGP (Border Gateway Protocol):**
- Policy-based routing
- Autonomous System (AS) based
- eBGP (external) and iBGP (internal)
- Internet backbone protocol

---

## Exercise 20: Comprehensive Network Troubleshooting
**Question:** A user at 192.168.10.50/24 (gateway: 192.168.10.1) cannot reach www.example.com (IP: 93.184.216.34). Run these diagnostic steps and interpret results:

**Given outputs:**
```
ping 127.0.0.1 → Success
ping 192.168.10.50 → Success
ping 192.168.10.1 → Request timeout
ping 93.184.216.34 → Request timeout
nslookup www.example.com → Returns 93.184.216.34
```

Diagnose the problem and suggest solutions.

**Solution:**

**Analysis:**

**Test 1: ping 127.0.0.1 → Success ✓**
- **Interpretation:** TCP/IP stack is working
- Loopback interface operational
- Problem is NOT in OS network stack

**Test 2: ping 192.168.10.50 → Success ✓**
- **Interpretation:** NIC (Network Interface Card) is working
- IP configuration is correct
- Problem is NOT in local interface

**Test 3: ping 192.168.10.1 → Request timeout ✗**
- **Interpretation:** Cannot reach default gateway
- **Critical problem identified!**
- Possible causes:
  - Gateway is down
  - Physical connection issue (cable, switch)
  - Firewall blocking ICMP on gateway
  - ARP resolution failure

**Test 4: ping 93.184.216.34 → Request timeout ✗**
- **Expected:** Fails because gateway unreachable
- Cannot route outside local network

**Test 5: nslookup www.example.com → Returns IP ✓**
- **Interpretation:** DNS resolution working
- But this might be cached or local hosts file
- DNS server might be on local network

**Root Cause:**
**Gateway unreachable - Layer 2 or Layer 3 issue between host and gateway**

**Additional Diagnostics:**

```bash
# Check ARP table
arp -a
# Should show: 192.168.10.1 → (MAC address)
# If incomplete → Layer 2 problem

# Check physical connection
ethtool eth0  # Linux
# Link detected: yes/no?

# Check routing table
route -n
# Default route: 0.0.0.0 → 192.168.10.1?

# Check if gateway responds to ARP
arping 192.168.10.1
```

**Solutions:**

1. **Check physical layer:**
   - Verify cable connections
   - Check link lights on NIC/switch
   - Try different cable/port

2. **Check gateway:**
   - Verify gateway is powered on
   - Check gateway configuration
   - Reboot gateway if accessible

3. **Check firewall:**
   - Temporarily disable host firewall
   - Check gateway firewall rules

4. **Network configuration:**
   - Verify IP settings: `ipconfig /all` or `ip addr`
   - Renew DHCP: `ipconfig /renew`
   - Static IP: verify correct gateway

5. **ARP issues:**
   - Clear ARP cache: `arp -d` or `ip neigh flush`
   - Check for ARP conflicts

**Troubleshooting Order (OSI Model):**
1. ✓ Physical: Cable, link status
2. ✓ Data Link: ARP, MAC address
3. → Network: IP configuration, routing
4. → Transport: TCP/UDP (not reached yet)
5. → Application: DNS, services (not reached yet)

---

## Final Exam Tips

**Key Topics Mastered:**
1. ✓ VLSM and complex subnetting
2. ✓ Routing tables and packet forwarding
3. ✓ IP fragmentation (MF, DF, offsets)
4. ✓ TCP windowing and flow control
5. ✓ NAT translation tables
6. ✓ Congestion control algorithms
7. ✓ Routing protocols (RIP, OSPF, BGP)
8. ✓ Network troubleshooting methodology
9. ✓ TCP sequence/ACK numbers
10. ✓ Bandwidth calculations and overhead

**Exam Strategy:**
- Draw diagrams for complex problems
- Show all calculations step-by-step
- Verify answers (especially subnetting)
- Watch for trick questions (DF flag set = no fragmentation!)
- Use binary for subnet calculations when needed
- Remember: network address and broadcast address are not usable

