# Lecture 01: OSI 7-Layer and TCP/IP 4-Layer Architecture Models

## Context and Grounding
This lecture note establishes the conceptual foundation of layered network communications, protocol data units (PDUs), packet encapsulation, and functional layer responsibilities. It directly grounds `Resources/Notes/1. Basic Elements of Computer Communication.md`, `2. TCP-IP Protocol System - Key Points.md`, and `3. OSI and TCP-IP.md`.

---

## 1. Network Layering Principles

Network communications utilize layered abstractions to isolate distinct technical responsibilities, enable multi-vendor interoperability, and permit independent protocol evolution without breaking adjacent layers.

### 1.1 Encapsulation and Protocol Data Units (PDUs)
As application data descends the protocol stack, each layer prepends a protocol header containing routing, control, and integrity metadata.

```text
Application Layer    [        Application Payload Data        ]  Message
        |
        v
Transport Layer      [TCP Hdr |      Application Data         ]  Segment (or Datagram for UDP)
        |
        v
Network Layer        [IP Hdr  |  TCP Hdr  | Application Data  ]  Packet
        |
        v
Data Link Layer      [Eth Hdr | IP Hdr | TCP | Data | Eth FCS ]  Frame
        |
        v
Physical Layer       011010010110001101100101...                 Bits
```

---

## 2. Comparison: OSI Reference Model vs. TCP/IP Architecture

| OSI 7-Layer Reference Model | TCP/IP 4-Layer Architecture | Primary Protocols | Addressing / Identifier |
|---|---|---|---|
| **7. Application**<br/>**6. Presentation**<br/>**5. Session** | **Application Layer** | HTTP, HTTPS, DNS, SSH, SMTP, DHCP, FTP | URLs, Domain Names, URI |
| **4. Transport Layer** | **Transport Layer** | TCP (Connection-oriented, reliable), UDP (Connectionless, datagram) | Port Numbers (0 to 65535) |
| **3. Network Layer** | **Internet Layer** | IPv4, IPv6, ICMP, IGMP, ARP, OSPF, BGP | Logical IP Addresses (32-bit / 128-bit) |
| **2. Data Link Layer** | **Network Access / Link Layer** | Ethernet (802.3), Wi-Fi (802.11), PPP | Physical MAC Addresses (48-bit EUI-48) |
| **1. Physical Layer** | *(Hardware Substrate)* | Cat6 copper, Single-mode fiber, RF spectrum | Voltages, light pulses, modulation symbols |

---

## 3. Detailed Layer Mechanics

### 3.1 Network Access (Data Link) Layer
* **Framing**: Delineates discrete packet boundaries using preamble and start-of-frame delimiters.
* **MAC Addressing**: 48-bit burned-in hardware address (`XX:XX:XX:YY:YY:YY`, where `XX` is the Organizationally Unique Identifier (OUI)).
* **Error Detection**: Frame Check Sequence (FCS) using 32-bit Cyclic Redundancy Check (CRC-32).

### 3.2 Internet Layer
* **Hop-by-Hop Routing**: Directs packets across multiple intermediate router boundaries based on destination IP address.
* **Fragmentation**: Divides oversized packets when the outgoing link Maximum Transmission Unit (MTU, typically 1500 bytes on Ethernet) is exceeded.
* **Best-Effort Delivery**: Does not guarantee delivery, packet order, or error correction.

### 3.3 Transport Layer
* **Multiplexing / Demultiplexing**: Directs concurrent network communications to distinct user-space application processes using port numbers.
* **Reliability Mechanics (TCP)**: Provides byte-stream abstraction with sequence numbers, positive acknowledgments (ACK), retransmission timeouts (RTO), and sliding-window flow control.

