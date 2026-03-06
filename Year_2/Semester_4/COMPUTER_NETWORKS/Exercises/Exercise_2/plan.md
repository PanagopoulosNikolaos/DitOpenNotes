# Lab Exercise 2: Computer Networks
**Student Name:** [Name]

**Student ID (AM):** [AM]

**Due Date:** March 15, 2026 

---

## Part 1: Network Delay Measurement (35%) 

### 1.1 Data Collection
Use the [online simulator](https://computerscience.unicam.it/marcantoni/reti/applet/TransmissionVsPropagationDelay/traProp.html) to measure delay (A1) and use the theoretical formula (A2) to verify results.

**Theoretical Formula:** $$d_{nodal} = d_{proc} + d_{queue} + \frac{L}{R} + \frac{d}{u}$$ 

*Note: $L$ = packet length, $R$ = transmission rate, $d$ = distance, $u$ = propagation speed.*

#### Table 1-1: Delay vs. Distance 
*(Parameters: R = 512 Kbps, L = 100 Bytes)* 

| Distance (d) | Measured Delay (A1) | Calculated Delay (A2) |
| :--- | :--- | :--- |
| 10 Km | 1.6 ms  | |
| 100 Km | | |
| 500 Km | | |
| 1000 Km | | |

#### Table 1-2: Delay vs. Packet Size 
*(Parameters: d = 10 Km, R = 512 Kbps)* 

| Packet Size (L) | Measured Delay (A1) | Calculated Delay (A2) |
| :--- | :--- | :--- |
| 100 Bytes | | |
| 500 Bytes | | |
| 1 KB | | |
| 2 KB | | |

#### Table 1-3: Delay vs. Transmission Rate 
*(Parameters: d = 10 Km, L = 500 Bytes)* 

| Rate (R) | Measured Delay (A1) | Calculated Delay (A2) |
| :--- | :--- | :--- |
| 512 Kbps | | |
| 1 Mbps | | |
| 10 Mbps | | |
| 100 Mbps | | |

### 1.2 Analysis & Jitter 
1. **Graphs:** Create three charts (Delay vs. Distance, Size, and Rate) using Excel or gnuplot.
2. **Commentary:** Compare measured vs. theoretical results and explain if they match expectations.
3. **Jitter Calculation:** * Run command: `ping -l 100 -n 50 1.1.1.1 > a.txt`.
   * Calculate Jitter using: $Jitter = \frac{\sum_{i=2}^{N} |x_i - x_{i-1}|}{N-1}$.
   * Create a Jitter graph showing delay per packet.

---

## Part 2: Network Creation (35%) 

### 2.1 Topology Implementation
Use **Cisco Packet Tracer v. 6.2** exclusively. (must use windows as shit is outdated as heck! made 2015 no real linux support god pray internet archive download is not a virus.)

1. **Switch Topology:** Build the network from Figure 2.1 (PCs connected via switches).
2. **Router Topology:** Replace Switch S2 with a **1941 Router**.
3. **Configuration:** * Set IP addresses and Subnet Masks as per Figure 2.2.
   * Enable router interfaces (GigabitEthernet 0/0 and 0/1).
4. **Testing:** Perform Pings between PC0/PC1 and PC2/PC3.
   * *Take screenshots of the topology and successful ping results*.

---

## Part 3: File Transfer Math (30%) 

**Scenario:** Transfer a file of size **[AM eg: 3323] KB**.
* One-way delay: 40 ms (RTT = 80 ms).
* Initial RTT handshake required before data.
* $1\text{ KB} = 1024\text{ bytes}$; $1\text{ Mbps} = 10^6\text{ bps}$.

**Calculate total time for:**
* **Case A:** Continuous transmission (1 Mbps, 1 KB packets, 40B header).
* **Case B:** Stop-and-Wait (Wait 1 RTT after each packet).
* **Case C:** Infinite bandwidth with exponential increase (Send 1, then 2, then 4 packets per RTT).

---

## Submission Checklist 

- [ ] **Lab Report (Word/PDF):**
    - [ ] Title page (Name, AM, Course, Date).
    - [ ] Screenshots of Packet Tracer topologies and Ping results.
    - [ ] Completed tables from Part 1.
    - [ ] Graphs for delay and Jitter.
    - [ ] Detailed answers for Part 3 calculations.
- [ ] **Packet Tracer Files:** (.pkt files).
- [ ] **Zip Archive:** Compress all files into one `.zip` for upload to ecourse.