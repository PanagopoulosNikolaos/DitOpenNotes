# Lecture 02: IPv4 Header Structure, CIDR, and VLSM Subnetting

## Context and Grounding
This lecture note formalizes IPv4 datagram formats, bit-level header fields, Classless Inter-Domain Routing (CIDR), and Variable Length Subnet Masking (VLSM) calculations. It connects directly with `Resources/Notes/4. Internet Layer.md` and `5. Subnetting.md`.

---

## 1. IPv4 Header Format

An IPv4 header has a minimum length of 20 bytes (5 32-bit words) when options are absent.

```text
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|Version|  IHL  |Type of Service|          Total Length         |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|         Identification        |Flags|     Fragment Offset     |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|  Time to Live |    Protocol   |        Header Checksum        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                       Source Address                          |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Destination Address                        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Options                    |    Padding    |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

### 1.1 Field Descriptions
* **Version (4 bits)**: Binary `0100` (IPv4).
* **IHL (Internet Header Length, 4 bits)**: Number of 32-bit words in header (minimum value 5, representing 20 bytes).
* **Total Length (16 bits)**: Total datagram size in bytes (header + payload, maximum 65,535 bytes).
* **Identification, Flags, Fragment Offset**: Reassembles fragmented packets. Flags include Don't Fragment (`DF`) and More Fragments (`MF`).
* **TTL (Time to Live, 8 bits)**: Hop count decremented by each router. Packet is discarded with ICMP Time Exceeded (Type 11) when $\text{TTL} = 0$.
* **Protocol (8 bits)**: Next-layer identifier (e.g., `1` for ICMP, `6` for TCP, `17` for UDP).
* **Header Checksum (16 bits)**: 16-bit one's complement checksum protecting the IP header against bit errors.

---

## 2. IP Addressing and CIDR Notation

An IPv4 address consists of 32 binary bits represented as four dot-separated octets ($0 \dots 255$).

### 2.1 Network and Host Separation
An IP address is split into two logical segments:
$$\text{IP Address} = [\text{Network Prefix}] \quad | \quad [\text{Host Identifier}]$$
The **Subnet Mask** determines this boundary. A contiguous sequence of $N$ leading 1s represents the network bits (written in CIDR prefix notation as $/N$).

* **Network Address**: Host bits all zero ($00\dots0$). Identifies the subnet itself.
* **Directed Broadcast Address**: Host bits all ones ($11\dots1$). Targets all hosts on the subnet.
* **Usable Host Capacity**: For a $/N$ prefix, there are $32 - N = H$ host bits:
  $$\text{Usable Hosts} = 2^H - 2$$

---

## 3. Variable Length Subnet Masking (VLSM)

VLSM enables allocating subnets of varying sizes from a single base block, preventing address exhaustion.

### 3.1 Design Rules
1. Sort all subnet requirements in **strictly descending order** by number of required hosts.
2. For each requirement, determine host bits $H$ satisfying $2^H - 2 \ge \text{required hosts}$.
3. Calculate subnet prefix length: $N = 32 - H$.
4. Align each subnet on valid block boundaries that are exact multiples of its block size $2^H$.
5. Assign the next available IP address block immediately following the preceding subnet's broadcast address.

