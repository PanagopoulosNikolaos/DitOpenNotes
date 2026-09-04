# Assignment 02: Network Traffic Capture and Protocol Deep-Dive Report

## Objective
Capture real-world network traffic using `tcpdump` on a Linux environment, analyze protocol layers from raw PCAP traces, and synthesize a comprehensive packet inspection report covering ARP resolution, DNS exchanges, TCP 3-way handshakes, and HTTP/HTTPS transactions.

---

## Lab Instructions and Tasks

### Task 1: ARP Table Inspection and Cache Manipulation
1. Display your operating system's active ARP cache using `ip neigh` or `arp -a`.
2. Clear the ARP cache using `sudo ip neigh flush all`.
3. Ping an active host on your local network (e.g., your default gateway) while capturing ARP packets via `tcpdump -i any -e -nn arp`.
4. Document the exact hardware MAC and logical IP addresses observed in the ARP Request (broadcast `ff:ff:ff:ff:ff:ff`) and ARP Reply (unicast).

### Task 2: DNS Protocol Analysis
1. Capture DNS traffic while querying the authoritative nameservers for an educational institution:
   ```bash
   sudo tcpdump -i any -s 0 -nn 'port 53' -w dns_test.pcap
   dig +trace www.mit.edu
   ```
2. Open `dns_test.pcap` with `tshark` or Wireshark.
3. Identify the Root DNS server query, TLD nameserver referral, and final Authoritative response.
4. Extract the Transaction ID, Query Flags (Recursion Desired, Authoritative Answer), and TTL values from the answer section.

### Task 3: TCP Connection Teardown and Sequence Reconstruction
1. Capture an HTTP download session using `wget` or `curl`:
   ```bash
   sudo tcpdump -i any -s 0 -w http_trace.pcap 'tcp port 80'
   curl http://example.com
   ```
2. Reconstruct the TCP 3-way handshake:
   * Record Initial Sequence Numbers (ISN) from the `SYN` and `SYN-ACK` frames.
   * Explain how relative sequence numbers map to raw 32-bit integer wire values.
   * Calculate the Round-Trip Time (RTT) of the handshake from packet timestamps.
3. Inspect TCP window scale, maximum segment size (MSS), and TCP selective acknowledgment (SACK) options negotiated during the handshake.

---

## Deliverables
Submit a formal technical report (`packet_analysis_report.md` or PDF) including:
1. Exact CLI commands used for each capture stage.
2. Formatted terminal snippets showing packet headers and hex/ASCII outputs.
3. Chronological timeline diagrams illustrating packet exchanges.
4. Answers to all analytical questions detailing flags, header offsets, and protocol behaviors.

