
# Part 1

**Theoretical Formula:** $$d_{nodal} = d_{proc} + d_{queue} + \frac{L}{R} + \frac{d}{u}$$ 

*Note: $L$ = packet length, $R$ = transmission rate, $d$ = distance, $u$ = propagation speed.*
> Propagation speed: 2.8 * 10^8 m/sec.

#### Table 1-1: Delay vs. Distance 
*(Parameters: R = 512 Kbps, L = 100 Bytes)* 

| Distance (d) | Measured Delay (A1) | Calculated Delay (A2) |
| :--- | :--- | :--- |
| 10 Km | 1.6 ms | 1.5982 ms |
| 100 Km | 1.090 ms | 1.9196 ms |
| 500 Km | 4.06 ms | 3.3482 ms |
| 1000 Km | 6.56 ms | 5.1339 ms |

**Formulas used to calculate it:**

- for 10 km: Calculated Delay = $\frac{800 \text{ bits}}{512,000 \text{ bps}} + \frac{10,000 \text{ m}}{2.8 \times 10^8 \text{ m/s}} = 1.5625 \text{ ms} + 0.0357 \text{ ms} = 1.5982 \text{ ms}$
- for 100 km: Calculated Delay = $\frac{800 \text{ bits}}{512,000 \text{ bps}} + \frac{100,000 \text{ m}}{2.8 \times 10^8 \text{ m/s}} = 1.5625 \text{ ms} + 0.3571 \text{ ms} = 1.9196 \text{ ms}$
- for 500 km: Calculated Delay = $\frac{800 \text{ bits}}{512,000 \text{ bps}} + \frac{500,000 \text{ m}}{2.8 \times 10^8 \text{ m/s}} = 1.5625 \text{ ms} + 1.7857 \text{ ms} = 3.3482 \text{ ms}$
- for 1000 km: Calculated Delay = $\frac{800 \text{ bits}}{512,000 \text{ bps}} + \frac{1,000,000 \text{ m}}{2.8 \times 10^8 \text{ m/s}} = 1.5625 \text{ ms} + 3.5714 \text{ ms} = 5.1339 \text{ ms}$



#### Table 1-2: Delay vs. Packet Size 
*(Parameters: d = 10 Km, R = 512 Kbps)* 

| Packet Size (L) | Measured Delay (A1) | Calculated Delay (A2) |
| :--- | :--- | :--- |
| 100 Bytes | 1.612 ms| |
| 500 Bytes | 7.86 ms | |
| 1 KB | 16.05 ms | |
| 2 KB | 32.05 ms| |

**Formulas used to calculate it:**

- for 100 Bytes: $\frac{800 \text{ bits}}{512,000 \text{ bps}} + \frac{10,000 \text{ m}}{2.8 \times 10^8 \text{ m/s}} = 1.5625 \text{ ms} + 0.0357 \text{ ms} = 1.5982 \text{ ms}$
- for 500 Bytes: $\frac{4000 \text{ bits}}{512,000 \text{ bps}} + \frac{10,000 \text{ m}}{2.8 \times 10^8 \text{ m/s}} = 1.5625 \text{ ms} + 0.0357 \text{ ms} = 1.5982 \text{ ms}$
- for 1 KB: $\frac{8000 \text{ bits}}{512,000 \text{ bps}} + \frac{10,000 \text{ m}}{2.8 \times 10^8 \text{ m/s}} = 1.5625 \text{ ms} + 0.0357 \text{ ms} = 1.5982 \text{ ms}$
- for 2 KB: $\frac{16000 \text{ bits}}{512,000 \text{ bps}} + \frac{10,000 \text{ m}}{2.8 \times 10^8 \text{ m/s}} = 1.5625 \text{ ms} + 0.0357 \text{ ms} = 1.5982 \text{ ms}$


#### Table 1-3: Delay vs. Transmission Rate 
*(Parameters: d = 10 Km, L = 500 Bytes)* 

| Rate (R) | Measured Delay (A1) | Calculated Delay (A2) |
| :--- | :--- | :--- |
| 512 Kbps | | |
| 1 Mbps | | |
| 10 Mbps | | |
| 100 Mbps | | |

**Formulas used to calculate it:**

- for 512 Kbps:
- for 1 Mbps:
- for 10 Mbps:
- for 100 Mbps:
