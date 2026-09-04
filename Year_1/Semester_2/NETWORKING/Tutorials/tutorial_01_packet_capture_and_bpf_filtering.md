# Tutorial 01: Packet Capture and Berkeley Packet Filtering (BPF)

## Context and Grounding
This tutorial provides a hands-on technical guide to capturing raw network traffic on Linux interfaces using `tcpdump` and `tshark`, designing precise Berkeley Packet Filters (BPF), and extracting protocol metadata. It directly builds on the practical workflows in `Exercises/Exercise 1+2 Packet Sniffing!.md` and `Exercise 3.md`.

---

## 1. Network Interface Inspection and Capture Basics

Identify active network adapters and interfaces:
```bash
ip -br link
# Output:
# eth0             UP             52:54:00:12:34:56 <BROADCAST,MULTICAST,UP,LOWER_UP>
# wlp4s0           UP             00:17:08:ff:60:73 <BROADCAST,MULTICAST,UP,LOWER_UP>
```

### 1.1 Essential tcpdump Command Options
| Flag | Description |
|---|---|
| `-i <interface>` | Network interface to listen on (or `any` for all interfaces) |
| `-n` | Do not resolve IP addresses to hostnames (prevents DNS delay) |
| `-nn` | Do not resolve IP addresses OR port names (shows raw port numbers) |
| `-s 0` | Set snapshot length to 0 (captures full un-truncated packets) |
| `-w <file.pcap>` | Writes raw captured packets directly to a PCAP trace file |
| `-r <file.pcap>` | Reads and parses packets from a previously saved PCAP file |
| `-X` | Displays packet payload simultaneously in hexadecimal and ASCII |
| `-c <count>` | Stops capture after receiving exactly `count` packets |

---

## 2. Berkeley Packet Filter (BPF) Syntax

BPF expressions are evaluated inside kernel space before packets are copied to user-space tools, maximizing capture efficiency.

### 2.1 Primitive Filters
* **By Host**: `host 192.168.1.100` or `src host 10.0.0.1`
* **By Subnet**: `net 172.16.0.0/16`
* **By Port**: `port 80 or port 443`
* **By Protocol**: `tcp`, `udp`, `icmp`, `arp`

### 2.2 Advanced Byte-Offset Filtering
BPF allows inspecting arbitrary header bytes using slice syntax: `proto[offset:size]`.

1. **Capture TCP SYN packets (Connection Initiation)**:
   The TCP flags byte is at offset 13 of the TCP header. The SYN bit is bit 1 ($0x02$):
   ```bash
   sudo tcpdump -i eth0 'tcp[tcpflags] & (tcp-syn) != 0 and tcp[tcpflags] & (tcp-ack) == 0'
   ```

2. **Capture HTTP GET Requests**:
   Inspect the first 4 bytes of the TCP payload for ASCII `"GET "` ($0x47455420$):
   ```bash
   sudo tcpdump -i eth0 -s 0 -A 'tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x47455420'
   ```

3. **Capture DNS Queries for Specific Record Types**:
   Filter UDP port 53 where DNS Query Type is MX (value 15, $0x000F$):
   ```bash
   sudo tcpdump -i eth0 -vvv -nn 'port 53 and udp and (udp[10] & 0x80 == 0)'
   ```

---

## 3. Post-Capture Trace Analysis with TShark

Extract tabular fields from a capture without loading graphical Wireshark:

```bash
tshark -r capture.pcap -Y "http.request" -T fields \
  -e frame.number \
  -e ip.src \
  -e ip.dst \
  -e http.request.method \
  -e http.host \
  -e http.request.uri
```

Expected Terminal Output:
```text
1   172.21.2.48   104.18.26.48    GET   example.com      /index.html
5   172.21.2.48   142.251.209.42  GET   google.com       /search?q=dit
```

