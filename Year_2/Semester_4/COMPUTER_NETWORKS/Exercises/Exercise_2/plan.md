# Lab Exercise 2: Computer Networks
**Student Name:** Panagopoullos Nikolaos

**Student ID (AM):** 3323

**Due Date:** March 15, 2026

---

## Progress Overview

| Part | Weight | Status |
| :--- | :---: | :---: |
| Part 1: Network Delay Measurement | 35% | Complete |
| Part 2: Network Creation (Packet Tracer) | 35% | Not Started |
| Part 3: File Transfer Math | 30% | Complete |

---

## Part 1: Network Delay Measurement (35%) — COMPLETE

### 1.1 Data Collection

Use the [online simulator](https://computerscience.unicam.it/marcantoni/reti/applet/TransmissionVsPropagationDelay/traProp.html) to measure delay (A1) and use the theoretical formula (A2) to verify results.

**Theoretical Formula:** $$d_{nodal} = d_{proc} + d_{queue} + \frac{L}{R} + \frac{d}{u}$$

*Note: $L$ = packet length, $R$ = transmission rate, $d$ = distance, $u$ = propagation speed.*

#### Table 1-1: Delay vs. Distance
*(Parameters: R = 512 Kbps, L = 100 Bytes)*

| Distance (d) | Measured Delay (A1) | Calculated Delay (A2) |
| :--- | :--- | :--- |
| 10 Km | 1.6 ms | 1.5982 ms |
| 100 Km | 2.090 ms | 1.9196 ms |
| 500 Km | null (`site limit`) | 3.3482 ms |
| 1000 Km | 7.030 ms | 5.1339 ms |

#### Table 1-2: Delay vs. Packet Size
*(Parameters: d = 10 Km, R = 512 Kbps)*

| Packet Size (L) | Measured Delay (A1) | Calculated Delay (A2) |
| :--- | :--- | :--- |
| 100 Bytes | 1.600 ms | 1.5982 ms |
| 500 Bytes | 7.74 ms | 7.8482 ms |
| 1 KB | 15.430 ms | 15.6607 ms |
| 2 KB | null (`site limit`) | 31.2857 ms |

#### Table 1-3: Delay vs. Transmission Rate
*(Parameters: d = 10 Km, L = 500 Bytes)*

| Rate (R) | Measured Delay (A1) | Calculated Delay (A2) |
| :--- | :--- | :--- |
| 512 Kbps | 1.600 ms | 7.8482 ms |
| 1 Mbps | 0.850 ms | 4.0357 ms |
| 10 Mbps | 0.140 ms | 0.4357 ms |
| 100 Mbps | 0.070 ms | 0.0757 ms |

### 1.2 Analysis & Jitter

- [x] **Graphs:** Three charts (Delay vs. Distance, Size, and Rate) generated via Plotly.
  - Source: `_plots.py` -> `images/combined_delay_analysis.png`
- [x] **Commentary:** Analytical comparison of measured vs. theoretical results written.
  - Source: `solution.md` -> "Analytical Commentary" section
- [x] **Jitter Calculation:** Jitter computed from `ping_output.txt` using the formula
  $Jitter = \frac{\sum_{i=2}^{N} |x_i - x_{i-1}|}{N-1}$
  - Source: `_plots.py` -> `images/combined_jitter_analysis.png`
  - Ping command used: `ping -l 100 -n 50 1.1.1.1 > a.txt`

**Deliverable files:**
- `_delay_calculator.py` — theoretical delay calculations
- `_plots.py` — all plot generation (delay + jitter)
- `solution.md` — tables, commentary, and jitter writeup
- `ping_output.txt` — raw ping data
- `images/combined_delay_analysis.png`
- `images/combined_jitter_analysis.png`

---

## Part 2: Network Creation (35%) — NOT STARTED

> Requires **Cisco Packet Tracer v. 6.2** (Windows only — no native Linux support).

### 2.1 Topology Implementation

- [ ] **Step a — Switch Topology:** Build the network from Figure 2.1 (PCs connected via switches S1 and S2). Test end-to-end communication.
- [ ] **Step b — Router Topology:** Replace Switch S2 with a **1941 Router**. Test end-to-end communication. Document whether it works and explain any failures.
- [ ] **Step c — Router Configuration (if needed):**
  - Set IP addresses and Subnet Masks per Figure 2.2.
  - Enable router interfaces: `GigabitEthernet 0/0` and `GigabitEthernet 0/1` (see Figure 2.3).
  - Verify end-to-end connectivity.
- [ ] **Screenshots required:**
  - Both topology views (switch and router).
  - Successful ping results between PC0/PC1 and PC2/PC3.
  - Router interface configuration (CLI output from Figure 2.3).

**Deliverable files:**
- `.pkt` Packet Tracer file(s) (both topologies preferably in one file).
- Screenshots embedded in the lab report.

---

## Part 3: File Transfer Math (30%) — COMPLETE

**Scenario:** Transfer a file of size **3323 KB** (AM = 3323).
- One-way delay: 40 ms (RTT = 80 ms).
- Initial RTT handshake required before data.
- $1\text{ KB} = 1024\text{ bytes}$; $1\text{ Mbps} = 10^6\text{ bps}$.

**Results (from `_delay_calculator.py`):**

| Case | Description | Total Time |
| :--- | :--- | :--- |
| A | Continuous Transmission (1 Mbps, 1 KB packets, 40B header) | 27,342.016 ms (27.34 s) |
| B | Stop-and-Wait (wait 1 RTT after each packet) | 294,205.376 ms (294.21 s) |
| C | Infinite bandwidth, exponential window growth (TCP Slow-Start) | 1,040.000 ms (1.04 s) |

**Deliverable files:**
- `_delay_calculator.py` — `calculateFileTransfer()` function
- `solution.md` — full Case A/B/C breakdown with per-RTT table for Case C

---

## Submission Checklist

- [ ] **Lab Report (Word/PDF):**
    - [ ] Title page (Name, AM, Course, Date).
    - [x] Completed tables from Part 1 (all three tables).
    - [x] Graphs for delay (Delay vs. Distance / Size / Rate).
    - [x] Jitter graph and calculated jitter value.
    - [ ] Screenshots of Packet Tracer topologies (Part 2 — pending).
    - [ ] Screenshots of successful ping results in Packet Tracer (Part 2 — pending).
    - [x] Detailed answers for Part 3 calculations (Cases A, B, C).
- [ ] **Packet Tracer File:** `.pkt` file(s) for both topologies.
- [ ] **Code files:** `_delay_calculator.py`, `_plots.py`.
- [ ] **Zip Archive:** Compress all files into one `.zip` for upload to ecourse.