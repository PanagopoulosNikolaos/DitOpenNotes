# Exercises 01: Network Delay, Transmission Rates, and Queuing Calculations

This practice problem set reinforces core calculations for transmission delay, propagation delay, queuing intensity, and store-and-forward packet switching over multi-hop links.

---

## Problem 1: Transmission Delay vs. Propagation Delay

### Question
Two hosts, $A$ and $B$, are separated by a physical distance $d = 20,000 \text{ km}$ connected by a direct point-to-point link with bandwidth $R = 2.5 \text{ Gbps}$. Signal propagation velocity is $s = 2 \times 10^8 \text{ m/s}$. Host $A$ sends a packet of size $L = 1,000 \text{ bytes}$ to Host $B$.

1. Calculate the transmission delay $d_{\text{trans}}$.
2. Calculate the propagation delay $d_{\text{prop}}$.
3. Determine whether the last bit of the packet is still being transmitted when the first bit arrives at Host $B$.
4. Calculate the Bandwidth-Delay Product (BDP) of the link.

### Solution

#### Part 1: Transmission Delay
$$L = 1000 \text{ bytes} \times 8 \text{ bits/byte} = 8,000 \text{ bits}$$
$$R = 2.5 \text{ Gbps} = 2.5 \times 10^9 \text{ bits/second}$$

$$
d_{\text{trans}} = \frac{L}{R} = \frac{8 \times 10^3}{2.5 \times 10^9} = 3.2 \times 10^{-6} \text{ seconds} = 3.2 \ \mu\text{s}
$$

#### Part 2: Propagation Delay
$$d = 20,000 \text{ km} = 2 \times 10^7 \text{ meters}$$
$$s = 2 \times 10^8 \text{ m/s}$$

$$
d_{\text{prop}} = \frac{d}{s} = \frac{2 \times 10^7}{2 \times 10^8} = 0.10 \text{ seconds} = 100 \text{ ms}
$$

#### Part 3: Packet Position Analysis
The first bit arrives at Host $B$ at time:
$$t_{\text{first bit}} = d_{\text{trans\_first\_bit}} + d_{\text{prop}} \approx 0 + 100 \text{ ms} = 100 \text{ ms}$$
Transmission finishes at time:
$$t_{\text{transmission\_done}} = d_{\text{trans}} = 3.2 \ \mu\text{s}$$
Since $3.2 \ \mu\text{s} \ll 100 \text{ ms}$, transmission finishes long before the first bit arrives at Host $B$. The entire packet is in flight along the physical cable.

#### Part 4: Bandwidth-Delay Product
$$
\text{BDP} = R \times d_{\text{prop}} = (2.5 \times 10^9 \text{ bps}) \times (0.10 \text{ s}) = 2.5 \times 10^8 \text{ bits} = 31.25 \text{ MB}
$$

---

## Problem 2: Store-and-Forward Pipelining Delay

### Question
Suppose 3 packets, each of size $L = 1,500 \text{ bytes}$, are sent from source $S$ to destination $D$ through two intermediate store-and-forward routers ($R_1$ and $R_2$). Each link has bandwidth $R = 10 \text{ Mbps}$. Neglect propagation delay and queuing delay.

1. Calculate the transmission time of one packet across one link.
2. Calculate the total time until all 3 packets are completely received at destination $D$.

### Solution

#### Part 1: Single Link Packet Transmission Time
$$L = 1500 \times 8 = 12,000 \text{ bits}$$
$$R = 10 \times 10^6 \text{ bps}$$

$$
t_{\text{link}} = \frac{L}{R} = \frac{12,000}{10^7} = 1.2 \times 10^{-3} \text{ s} = 1.2 \text{ ms}
$$

#### Part 2: Pipelined Transfer Time
The path has $N = 3$ links in series ($S \to R_1$, $R_1 \to R_2$, $R_2 \to D$).
For $P = 3$ packets, applying the pipelining formula:

$$
T_{\text{total}} = (N + P - 1) \cdot t_{\text{link}} = (3 + 3 - 1) \cdot 1.2 \text{ ms} = 5 \cdot 1.2 \text{ ms} = 6.0 \text{ ms}
$$

Timeline check:
- At $t = 1.2 \text{ ms}$: Packet 1 is at $R_1$; $S$ begins transmitting Packet 2.
- At $t = 2.4 \text{ ms}$: Packet 1 is at $R_2$; Packet 2 is at $R_1$; $S$ begins transmitting Packet 3.
- At $t = 3.6 \text{ ms}$: Packet 1 arrives at $D$; Packet 2 is at $R_2$; Packet 3 is at $R_1$.
- At $t = 4.8 \text{ ms}$: Packet 2 arrives at $D$; Packet 3 is at $R_2$.
- At $t = 6.0 \text{ ms}$: Packet 3 arrives at $D$. Total time $= 6.0 \text{ ms}$.

