# Part 1: Network Delay Measurement

**Theoretical Formula:** $$d_{nodal} = d_{proc} + d_{queue} + \frac{L}{R} + \frac{d}{u}$$ 

Where:
* $L$ = packet length
* $R$ = transmission rate
* $d$ = distance
* $u$ = propagation speed ($2.8 \times 10^8$ m/sec)

#### Table 1-1: Delay vs. Distance (Parameters: R = 512 Kbps, L = 100 Bytes)
| Distance (d) | Measured Delay (A1) | Calculated Delay (A2) |
| :--- | :--- | :--- |
| 10 Km | 1.6 ms | 1.5982 ms |
| 100 Km | 2.090 ms | 1.9196 ms |
| 500 Km | null (`site limit`) | 3.3482 ms |
| 1000 Km | 7.030 ms | 5.1339 ms |

#### Table 1-2: Delay vs. Packet Size (Parameters: d = 10 Km, R = 512 Kbps)
| Packet Size (L) | Measured Delay (A1) | Calculated Delay (A2) |
| :--- | :--- | :--- |
| 100 Bytes | 1.600 ms | 1.5982 ms |
| 500 Bytes | 7.74 ms | 7.8482 ms |
| 1 KB | 15.430 ms | 15.6607 ms |
| 2 KB | null (`site limit`) | 31.2857 ms |

#### Table 1-3: Delay vs. Transmission Rate (Parameters: d = 10 Km, L = 500 Bytes)
| Rate (R) | Measured Delay (A1) | Calculated Delay (A2) |
| :--- | :--- | :--- |
| 512 Kbps | 1.600 ms | 7.8482 ms |
| 1 Mbps | 0.850 ms | 4.0357 ms |
| 10 Mbps | 0.140 ms | 0.4357 ms |
| 100 Mbps | 0.070 ms | 0.0757 ms |

---

### **Visualization Analysis**
![Network Performance Analysis](images/combined_delay_analysis.png)

### **Analytical Commentary**
The comparison between the measured data ($A_1$) from the simulator and the calculated theoretical values ($A_2$) reveals several key insights into network performance:

1.  **Discrepancy Rationale:** The measured delays consistently exceed the theoretical values in several scenarios. This is primarily attributed to the omission of **Processing Delay** ($d_{proc}$) and **Queuing Delay** ($d_{queue}$) in the simplified theoretical model. While the formula focuses on the physical constraints of transmission and propagation, real-world devices (and high-fidelity simulators) must account for the time taken by a router to examine a packet header and the time spent waiting in a buffer when the outgoing link is busy.
2.  **Linearity of Distance:** As observed in Table 1-1, the delay increases linearly with distance, confirming that propagation delay ($\frac{d}{u}$) behaves as expected. The growing gap between $A_1$ and $A_2$ at larger distances suggests that the simulator might be introducing additional overhead proportional to the link complexity.
3.  **Transmission Efficiency:** In Table 1-3, high transmission rates drastically reduce the total delay. However, notice that once the transmission rate reaches 100 Mbps, the delay plateaued. At this point, the transmission delay becomes negligible, and the total latency is dominated by propagation speed.
4.  **Packet Size Impact:** Larger packets increase the "Time on Wire." The slight deviations in Table 1-2 suggest that larger packets might trigger slight queuing or packet fragmentation checks within the simulator's internal logic.

---

### **Jitter Investigation**
![Jitter Analysis](images/combined_jitter_analysis.png)

Jitter represents the variation in latency over time. In our captured data, the inter-packet jitter remains relatively low, indicating a stable link with consistent queuing times. High jitter would typically be caused by transient network congestion or varying path lengths in more complex routing environments.

---

# Part 2: Network Creation
### todo!

---

# Part 3: File Transfer Performance

### Scenario Parameters

| Parameter | Value |
| :--- | :--- |
| File size (AM) | 3,323 KB = 3,402,752 bytes |
| Link rate | 1 Mbps = 1,000,000 bps |
| Packet payload | 1 KB = 1,024 bytes |
| Header overhead | 40 bytes |
| Packet total on wire | 1,064 bytes = 8,512 bits |
| One-way propagation delay | 40 ms |
| RTT | 80 ms |
| Initial handshake | 1 RTT = 80 ms |
| Total packets | 3,323 |
| Transmission time per packet | 8.512 ms |

---

### Case A: Continuous Transmission

All packets are sent back-to-back without waiting for acknowledgements. The total time accounts for the initial handshake, the time to clock all bits onto the wire, and the propagation delay for the last bit to reach the receiver.

$$T_A = \text{Handshake} + \frac{\text{TotalBits}}{\text{Rate}} + d_{prop}$$

$$T_A = 80 + \frac{27{,}222{,}016}{1{,}000{,}000} + 40 = 80 + 27{,}222.016 + 40$$

$$\boxed{T_A = 27{,}342.016 \text{ ms} \approx 27.34 \text{ s}}$$

---

### Case B: Stop-and-Wait

After transmitting each packet, the sender waits for a full RTT before sending the next one. This is the least efficient strategy, as the link is idle for the majority of each cycle.

$$T_B = \text{Handshake} + N \times (T_{packet} + RTT)$$

$$T_B = 80 + 3{,}323 \times (8.512 + 80) = 80 + 3{,}323 \times 88.512$$

$$\boxed{T_B = 294{,}205.376 \text{ ms} \approx 294.21 \text{ s}}$$

---

### Case C: Exponential Window Growth (TCP Slow-Start)

The link is assumed to have infinite bandwidth (transmission delay = 0). The sender starts with a window of 1 packet and doubles it each RTT, following the TCP slow-start doubling rule ($2^0, 2^1, 2^2, \ldots$). The process continues until all 3,323 packets have been sent.

$$T_C = \text{Handshake} + \text{DataRTTs} \times RTT$$

| RTT | Window (pkts) | Sent This RTT | Remaining |
| :---: | :---: | :---: | :---: |
| 1 | 1 | 1 | 3,322 |
| 2 | 2 | 2 | 3,320 |
| 3 | 4 | 4 | 3,316 |
| 4 | 8 | 8 | 3,308 |
| 5 | 16 | 16 | 3,292 |
| 6 | 32 | 32 | 3,260 |
| 7 | 64 | 64 | 3,196 |
| 8 | 128 | 128 | 3,068 |
| 9 | 256 | 256 | 2,812 |
| 10 | 512 | 512 | 2,300 |
| 11 | 1,024 | 1,024 | 1,276 |
| 12 | 2,048 | 1,276 | 0 |

12 data RTTs are required. The final RTT sends only 1,276 packets (the remainder), not a full window of 2,048.

$$T_C = 80 + 12 \times 80$$

$$\boxed{T_C = 1{,}040 \text{ ms} \approx 1.04 \text{ s}}$$

---

### Summary

| Case | Strategy | Total Time |
| :--- | :--- | :--- |
| A | Continuous Transmission | 27,342.016 ms (27.34 s) |
| B | Stop-and-Wait | 294,205.376 ms (294.21 s) |
| C | Exponential Window Growth | 1,040.000 ms (1.04 s) |

The results highlight the dramatic impact of the transmission strategy on overall transfer time. Case B is approximately **10.7x slower** than Case A, as the link sits idle waiting for an ACK after every single packet — the propagation delay dominates each cycle. Case C, despite using infinite bandwidth as a simplification, demonstrates why TCP slow-start is so effective: by doubling the in-flight window every RTT, all 3,323 packets are delivered in just 12 RTTs, making it **26x faster** than Case A and **283x faster** than Case B.