  
### **1.2 DNS Query Tools**

- **Resolve A/MX records for domains**:
    
    ```Shell
    dig A example.com +short && dig MX example.com +short
    nslookup -type=MX example.com
    ```
    

  

```Python
┌─[ice@parrot]─[~]
└──╼ $dig A example.com +short && dig MX example.com +short
96.7.128.198
23.192.228.80
23.192.228.84
23.215.0.136
23.215.0.138
96.7.128.175
0 .
```

```Python
┌─[ice@parrot]─[~]
└──╼ $nslookup -type=MX example.com
Server:		195.130.72.1
Address:	195.130.72.1#53

Non-authoritative answer:
example.com	mail exchanger = 0 .

Authoritative answers can be found from:
example.com	nameserver = a.iana-servers.net.
example.com	nameserver = b.iana-servers.net.
a.iana-servers.net	internet address = 199.43.135.53
a.iana-servers.net	has AAAA address 2001:500:8f::53
b.iana-servers.net	internet address = 199.43.133.53
b.iana-servers.net	has AAAA address 2001:500:8d::53
```

  

  

- **Reverse DNS lookup for IP 8.8.8.8**:
    
    ```Shell
    dig -x 8.8.8.8 +short
    nslookup 8.8.8.8
    ```
    
    ```Python
    ┌─[ice@parrot]─[~]
    └──╼ $dig -x 8.8.8.8 +noall +answer
    8.8.8.8.in-addr.arpa.	82537	IN	PTR	dns.google.
    ```
    
- **Specify alternate DNS server (e.g., Google DNS)**:
    
    ```Shell
    dig @8.8.8.8 example.com +short
    ```
    
    ```Python
    23.192.228.80
    23.215.0.136
    96.7.128.198
    23.192.228.84
    96.7.128.175
    23.215.0.138
    ```
    

---

### **2. Packet Capture & Analysis**

### **2.1 Baseline Capture Filters**

- **Capture HTTP traffic on port 80 with TCP header analysis**:
    
    ```Shell
    sudo tcpdump -i wlp4s0 -s0 'tcp port 80 and (((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2)) != 0)' -w http.pcap
    ```
    
    - **Filter breakdown**:
        - `tcp port 80`: Match TCP traffic on HTTP port
        - `ip[2:2]`: Total IP packet length
        - `(ip&0xf)<<2`: IP header length
        - `(tcp&0xf0)>>2`: TCP header length
        - `!=0`: Exclude zero-length payloads
- **Isolate DNS MX record queries**:
    
    ```Shell
    sudo tcpdump -i wlp4s0 -s0 -vvv 'port 53 and udp and (udp[10] & 0x7f = 15)' -w dns_mx.pcap
    ```
    
    - **Filter explanation**:
        - `udp`: DNS query type field at offset 10
        - `0x7f = 15`: Match MX record type (value 15)

  

## **Capture DNS queries/responses on port 53 (UDP/TCP)**:

```Shell
sudo timeout 30s tcpdump -i any -s0 -nn 'port 53' -w dns_capture.pca
```

  

# Opening the Captured DNS PCAP File

```Python
tshark -r dns_capture.pcap -Y "dns"
```

```Python
1   0.000000 172.16.3.244 → 195.130.72.1 DNS 77 Standard query 0x00e0 A example.com
    2   0.148216 195.130.72.1 → 172.16.3.244 DNS 309 Standard query response 0x00e0 A example.com A 23.192.228.80 A 23.192.228.84 A 23.215.0.136 A 23.215.0.138 A 96.7.128.175 A 96.7.128.198 NS a.iana-servers.net NS b.iana-servers.net A 199.43.135.53 AAAA 2001:500:8f::53 A 199.43.133.53 AAAA 2001:500:8d::53
    3   0.148564 172.16.3.244 → 195.130.72.1 DNS 77 Standard query 0xb6d0 AAAA example.com
    4   0.289000 195.130.72.1 → 172.16.3.244 DNS 381 Standard query response 0xb6d0 AAAA example.com AAAA 2600:1406:3a00:21::173e:2e65 AAAA 2600:1406:3a00:21::173e:2e66 AAAA 2600:1406:bc00:53::b81e:94c8 AAAA 2600:1406:bc00:53::b81e:94ce AAAA 2600:1408:ec00:36::1736:7f24 AAAA 2600:1408:ec00:36::1736:7f31 NS a.iana-servers.net NS b.iana-servers.net A 199.43.135.53 AAAA 2001:500:8f::53 A 199.43.133.53 AAAA 2001:500:8d::53
    5   0.312852 172.16.3.244 → 195.130.72.1 DNS 100 Standard query 0xed37 A example.com OPT
    6   0.315829 195.130.72.1 → 172.16.3.244 DNS 320 Standard query response 0xed37 A example.com A 96.7.128.198 A 23.192.228.80 A 23.192.228.84 A 23.215.0.136 A 23.215.0.138 A 96.7.128.175 NS b.iana-servers.net NS a.iana-servers.net A 199.43.135.53 AAAA 2001:500:8f::53 A 199.43.133.53 AAAA 2001:500:8d::53 OPT
    7   0.348294 172.16.3.244 → 195.130.72.1 DNS 86 Standard query 0x37a3 PTR 8.8.8.8.in-addr.arpa
    8   0.353866 195.130.72.1 → 172.16.3.244 DNS 192 Standard query response 0x37a3 PTR 8.8.8.8.in-addr.arpa PTR dns.google NS ns1.google.com NS ns2.google.com NS ns3.google.com NS ns4.google.com
    9   3.544431 172.16.3.244 → 195.130.72.1 DNS 86 Standard query 0x8202 PTR 8.8.8.8.in-addr.arpa
   10   3.547442 195.130.72.1 → 172.16.3.244 DNS 192 Standard query response 0x8202 PTR 8.8.8.8.in-addr.arpa PTR dns.google NS ns4.google.com NS ns1.google.com NS ns2.google.com NS ns3.google.com
   11   8.073309 172.16.3.244 → 195.130.72.1 DNS 100 Standard query 0xedb7 A example.com OPT
   12   8.076302 195.130.72.1 → 172.16.3.244 DNS 320 Standard query response 0xedb7 A example.com A 96.7.128.175 A 96.7.128.198 A 23.192.228.80 A 23.192.228.84 A 23.215.0.136 A 23.215.0.138 NS a.iana-servers.net NS b.iana-servers.net A 199.43.135.53 AAAA 2001:500:8f::53 A 199.43.133.53 AAAA 2001:500:8d::53 OPT
   13  13.648039 172.16.3.244 → 195.130.72.1 DNS 100 Standard query 0x1195 MX example.com OPT
   14  13.652586 195.130.72.1 → 172.16.3.244 DNS 239 Standard query response 0x1195 MX example.com MX 0 <Root> NS b.iana-servers.net NS a.iana-servers.net A 199.43.135.53 AAAA 2001:500:8f::53 A 199.43.133.53 AAAA 2001:500:8d::53 OPT
   15  13.677262 172.16.3.244 → 195.130.72.1 DNS 100 Standard query 0xa69c NS example.com OPT
   16  13.679713 195.130.72.1 → 172.16.3.244 DNS 224 Standard query response 0xa69c NS example.com NS a.iana-servers.net NS b.iana-servers.net A 199.43.135.53 AAAA 2001:500:8f::53 A 199.43.133.53 AAAA 2001:500:8d::53 OPT
   17  26.439082 172.16.3.244 → 195.130.72.1 DNS 83 Standard query 0x9b68 A www1.bobmovies.us
   18  26.439143 172.16.3.244 → 195.130.72.1 DNS 83 Standard query 0xa41d HTTPS www1.bobmovies.us
```

  

## Second command:

- more info harder to read

```Python
tcpdump -r dns_capture.pcap -n -vvv -X
```

```Python
reading from file dns_capture.pcap, link-type LINUX_SLL2 (Linux cooked v2), snapshot length 262144
Warning: interface names might be incorrect
11:42:33.478466 wlx3c52a12adedc Out IP (tos 0x0, ttl 64, id 14539, offset 0, flags [none], proto UDP (17), length 57)
    172.16.3.244.42198 > 195.130.72.1.53: [udp sum ok] 224+ A? example.com. (29)
	0x0000:  4500 0039 38cb 0000 4011 8661 ac10 03f4  E..98...@..a....
	0x0010:  c382 4801 a4d6 0035 0025 cec2 00e0 0100  ..H....5.%......
	0x0020:  0001 0000 0000 0000 0765 7861 6d70 6c65  .........example
	0x0030:  0363 6f6d 0000 0100 01                   .com.....
11:42:33.626682 wlx3c52a12adedc In  IP (tos 0xe0, ttl 254, id 16422, offset 0, flags [DF], proto UDP (17), length 289)
    195.130.72.1.53 > 172.16.3.244.42198: [udp sum ok] 224 q: A? example.com. 6/2/4 example.com. [5m] A 23.192.228.80, example.com. [5m] A 23.192.228.84, example.com. [5m] A 23.215.0.136, example.com. [5m] A 23.215.0.138, example.com. [5m] A 96.7.128.175, example.com. [5m] A 96.7.128.198 ns: example.com. [2h29m58s] NS a.iana-servers.net., example.com. [2h29m58s] NS b.iana-servers.net. ar: a.iana-servers.net. [7m20s] A 199.43.135.53, a.iana-servers.net. [7m20s] AAAA 2001:500:8f::53, b.iana-servers.net. [7m20s] A 199.43.133.53, b.iana-servers.net. [7m20s] AAAA 2001:500:8d::53 (261)
	0x0000:  45e0 0121 4026 4000 fe11 7f3d c382 4801  E..!@&@....=..H.
	0x0010:  ac10 03f4 0035 a4d6 010d a60a 00e0 8180  .....5..........
	0x0020:  0001 0006 0002 0004 0765 7861 6d70 6c65  .........example
	0x0030:  0363 6f6d 0000 0100 01c0 0c00 0100 0100  .com............
	0x0040:  0001 2c00 0417 c0e4 50c0 0c00 0100 0100  ..,.....P.......
	0x0050:  0001 2c00 0417 c0e4 54c0 0c00 0100 0100  ..,.....T.......
	0x0060:  0001 2c00 0417 d700 88c0 0c00 0100 0100  ..,.............
	0x0070:  0001 2c00 0417 d700 8ac0 0c00 0100 0100  ..,.............
	0x0080:  0001 2c00 0460 0780 afc0 0c00 0100 0100  ..,..`..........
	0x0090:  0001 2c00 0460 0780 c6c0 0c00 0200 0100  ..,..`..........
	0x00a0:  0023 2600 1401 610c 6961 6e61 2d73 6572  .#&...a.iana-ser
	0x00b0:  7665 7273 036e 6574 00c0 0c00 0200 0100  vers.net........
	0x00c0:  0023 2600 0401 62c0 8bc0 8900 0100 0100  .#&...b.........
	0x00d0:  0001 b800 04c7 2b87 35c0 8900 1c00 0100  ......+.5.......
	0x00e0:  0001 b800 1020 0105 0000 8f00 0000 0000  ................
	0x00f0:  0000 0000 53c0 a900 0100 0100 0001 b800  ....S...........
	0x0100:  04c7 2b85 35c0 a900 1c00 0100 0001 b800  ..+.5...........
	0x0110:  1020 0105 0000 8d00 0000 0000 0000 0000  ................
	0x0120:  53                                       S
11:42:33.627030 wlx3c52a12adedc Out IP (tos 0x0, ttl 64, id 24719, offset 0, flags [none], proto UDP (17), length 57)
    172.16.3.244.39779 > 195.130.72.1.53: [udp sum ok] 46800+ AAAA? example.com. (29)
	0x0000:  4500 0039 608f 0000 4011 5e9d ac10 03f4  E..9`...@.^.....
	0x0010:  c382 4801 9b63 0035 0025 0745 b6d0 0100  ..H..c.5.%.E....
	0x0020:  0001 0000 0000 0000 0765 7861 6d70 6c65  .........example
	0x0030:  0363 6f6d 0000 1c00 01                   .com.....
11:42:33.767466 wlx3c52a12adedc In  IP (tos 0xe0, ttl 254, id 16423, offset 0, flags [DF], proto UDP (17), length 361)
    195.130.72.1.53 > 172.16.3.244.39779: [udp sum ok] 46800 q: AAAA? example.com. 6/2/4 example.com. [5m] AAAA 2600:1406:3a00:21::173e:2e65, example.com. [5m] AAAA 2600:1406:3a00:21::173e:2e66, example.com. [5m] AAAA 2600:1406:bc00:53::b81e:94c8, example.com. [5m] AAAA 2600:1406:bc00:53::b81e:94ce, example.com. [5m] AAAA 2600:1408:ec00:36::1736:7f24, example.com. [5m] AAAA 2600:1408:ec00:36::1736:7f31 ns: example.com. [2h29m58s] NS a.iana-servers.net., example.com. [2h29m58s] NS b.iana-servers.net. ar: a.iana-servers.net. [7m20s] A 199.43.135.53, a.iana-servers.net. [7m20s] AAAA 2001:500:8f::53, b.iana-servers.net. [7m20s] A 199.43.133.53, b.iana-servers.net. [7m20s] AAAA 2001:500:8d::53 (333)
	0x0000:  45e0 0169 4027 4000 fe11 7ef4 c382 4801  E..i@'@...~...H.
	0x0010:  ac10 03f4 0035 9b63 0155 9771 b6d0 8180  .....5.c.U.q....
	0x0020:  0001 0006 0002 0004 0765 7861 6d70 6c65  .........example
	0x0030:  0363 6f6d 0000 1c00 01c0 0c00 1c00 0100  .com............
	0x0040:  0001 2c00 1026 0014 063a 0000 2100 0000  ..,..&...:..!...
	0x0050:  0017 3e2e 65c0 0c00 1c00 0100 0001 2c00  ..>.e.........,.
	0x0060:  1026 0014 063a 0000 2100 0000 0017 3e2e  .&...:..!.....>.
	0x0070:  66c0 0c00 1c00 0100 0001 2c00 1026 0014  f.........,..&..
	0x0080:  06bc 0000 5300 0000 00b8 1e94 c8c0 0c00  ....S...........
	0x0090:  1c00 0100 0001 2c00 1026 0014 06bc 0000  ......,..&......
	0x00a0:  5300 0000 00b8 1e94 cec0 0c00 1c00 0100  S...............
	0x00b0:  0001 2c00 1026 0014 08ec 0000 3600 0000  ..,..&......6...
	0x00c0:  0017 367f 24c0 0c00 1c00 0100 0001 2c00  ..6.$.........,.
	0x00d0:  1026 0014 08ec 0000 3600 0000 0017 367f  .&......6.....6.
	0x00e0:  31c0 0c00 0200 0100 0023 2600 1401 610c  1........#&...a.
	0x00f0:  6961 6e61 2d73 6572 7665 7273 036e 6574  iana-servers.net
	0x0100:  00c0 0c00 0200 0100 0023 2600 0401 62c0  .........#&...b.
	0x0110:  d3c0 d100 0100 0100 0001 b800 04c7 2b87  ..............+.
	0x0120:  35c0 d100 1c00 0100 0001 b800 1020 0105  5...............
	0x0130:  0000 8f00 0000 0000 0000 0000 53c0 f100  ............S...
	0x0140:  0100 0100 0001 b800 04c7 2b85 35c0 f100  ..........+.5...
	0x0150:  1c00 0100 0001 b800 1020 0105 0000 8d00  ................
	0x0160:  0000 0000 0000 0000 53                   ........S
11:42:33.791318 wlx3c52a12adedc Out IP (tos 0x0, ttl 64, id 46056, offset 0, flags [none], proto UDP (17), length 80)
    172.16.3.244.55383 > 195.130.72.1.53: [udp sum ok] 60727+ [1au] A? example.com. ar: . OPT UDPsize=1232 [COOKIE 10dc6e6196f53354] (52)
	0x0000:  4500 0050 b3e8 0000 4011 0b2d ac10 03f4  E..P....@..-....
	0x0010:  c382 4801 d857 0035 003c 5ffc ed37 0120  ..H..W.5.<_..7..
	0x0020:  0001 0000 0000 0001 0765 7861 6d70 6c65  .........example
	0x0030:  0363 6f6d 0000 0100 0100 0029 04d0 0000  .com.......)....
	0x0040:  0000 000c 000a 0008 10dc 6e61 96f5 3354  ..........na..3T
```

  

---

Full complete analysis:

```Python
┌─[ice@parrot]─[~]
└──╼ $tshark -r dns_capture.pcap -Y "dns" -T fields \
  -e frame.number \
  -e frame.time \
  -e ip.src \
  -e ip.dst \
  -e _ws.col.Protocol \
  -e udp.srcport -e udp.dstport \
  -e tcp.srcport -e tcp.dstport \
  -e dns.flags.response \
  -e dns.qry.name \
  -e dns.qry.type \
  -e dns.count.answers \
  -e dns.a
1	Apr 29, 2025 11:42:33.478466000 EEST	172.16.3.244	195.130.72.1	DNS	4219853			0	example.com	1	0	
2	Apr 29, 2025 11:42:33.626682000 EEST	195.130.72.1	172.16.3.244	DNS	53	42198			1	example.com	1	6	23.192.228.80,23.192.228.84,23.215.0.136,23.215.0.138,96.7.128.175,96.7.128.198,199.43.135.53,199.43.133.53
3	Apr 29, 2025 11:42:33.627030000 EEST	172.16.3.244	195.130.72.1	DNS	3977953			0	example.com	28	0	
4	Apr 29, 2025 11:42:33.767466000 EEST	195.130.72.1	172.16.3.244	DNS	53	39779			1	example.com	28	6	199.43.135.53,199.43.133.53
5	Apr 29, 2025 11:42:33.791318000 EEST	172.16.3.244	195.130.72.1	DNS	5538353			0	example.com	1	0	
6	Apr 29, 2025 11:42:33.794295000 EEST	195.130.72.1	172.16.3.244	DNS	53	55383			1	example.com	1	6	96.7.128.198,23.192.228.80,23.192.228.84,23.215.0.136,23.215.0.138,96.7.128.175,199.43.135.53,199.43.133.53
7	Apr 29, 2025 11:42:33.826760000 EEST	172.16.3.244	195.130.72.1	DNS	3393653			0	8.8.8.8.in-addr.arpa	12	0	
8	Apr 29, 2025 11:42:33.832332000 EEST	195.130.72.1	172.16.3.244	DNS	53	33936			1	8.8.8.8.in-addr.arpa	12	1	
9	Apr 29, 2025 11:42:37.022897000 EEST	172.16.3.244	195.130.72.1	DNS	4801753			0	8.8.8.8.in-addr.arpa	12	0	
10	Apr 29, 2025 11:42:37.025908000 EEST	195.130.72.1	172.16.3.244	DNS	53	48017			1	8.8.8.8.in-addr.arpa	12	1	
11	Apr 29, 2025 11:42:41.551775000 EEST	172.16.3.244	195.130.72.1	DNS	4071853			0	example.com	1	0	
12	Apr 29, 2025 11:42:41.554768000 EEST	195.130.72.1	172.16.3.244	DNS	53	40718			1	example.com	1	6	96.7.128.175,96.7.128.198,23.192.228.80,23.192.228.84,23.215.0.136,23.215.0.138,199.43.135.53,199.43.133.53
13	Apr 29, 2025 11:42:47.126505000 EEST	172.16.3.244	195.130.72.1	DNS	3418253			0	example.com	15	0	
14	Apr 29, 2025 11:42:47.131052000 EEST	195.130.72.1	172.16.3.244	DNS	53	34182			1	example.com	15	1	199.43.135.53,199.43.133.53
15	Apr 29, 2025 11:42:47.155728000 EEST	172.16.3.244	195.130.72.1	DNS	4291253			0	example.com	2	0	
16	Apr 29, 2025 11:42:47.158179000 EEST	195.130.72.1	172.16.3.244	DNS	53	42912			1	example.com	2	2	199.43.135.53,199.43.133.53
17	Apr 29, 2025 11:42:59.917548000 EEST	172.16.3.244	195.130.72.1	DNS	2020653			0	www1.bobmovies.us	1	0	
18	Apr 29, 2025 11:42:59.917609000 EEST	172.16.3.244	195.130.72.1	DNS	3171	53			0	www1.bobmovies.us	65	0	
 
```

- the tcpdump analysis was the most complete but most complex to read!

  

  

  

---

### **3. Exercise-Specific Commands**

### **3.1 SET 1: Web Browsing Traffic Analysis**

1. **Capture all HTTP/HTTPS and DNS traffic**:
    
    ```Shell
    sudo tcpdump -i wlp4s0 -s0 -w browsing.pcap '(tcp port 80 or tcp port 443 or port 53)'
    ```
    
2. **Extract DNS query/response pairs**:
    
    ```Shell
    tshark -r browsing.pcap -Y 'dns' -T fields -e frame.time -e dns.qry.name -e dns.a
    ```
    

### **3.2 SET 2: nslookup [www.mit.edu](http://www.mit.edu/) Analysis**

1. **Targeted capture during nslookup**:
    
    ```Shell
    sudo tcpdump -i wlp4s0 -s0 -w mit.pcap 'host www.mit.edu and port 53' &
    nslookup www.mit.edu
    ```
    
2. **Identify source/dest ports and DNS server**:
    
    ```Shell
    tshark -r mit.pcap -Y 'dns' -T fields -e dns.id -e ip.src -e udp.srcport -e ip.dst -e udp.dstport
    ```
    

### **3.3 SET 3: Advanced DNS Record Analysis**

1. **Capture iterative DNS resolution process**:
    
    ```Shell
    sudo tcpdump -i wlp4s0 -s0 -w iterative.pcap 'port 53 and (udp[10] & 0x80 = 0)'
    dig +trace example.com
    ```
    
    - `udp & 0x80 = 0`: Match DNS queries (non-responses)
2. **Extract authoritative name server responses**:
    
    ```Shell
    tshark -r iterative.pcap -Y 'dns.flags.response == 1 and dns.flags.auth == 1' -V
    ```
    

---

### **4. Post-Capture Analysis Tools**

1. **Extract HTTP headers from PCAP**:
    
    ```Shell
    tshark -r capture.pcap -Y 'http' -T json --no-duplicate-keys
    ```
    
2. **Detect DNS tunneling attempts**:
    
    ```Shell
    tshark -r dns.pcap -Y 'dns.qry.name matches ".*[.]exe$|.*[.]zip$"'
    ```
    
3. **Map DNS query/response timing**:
    
    ```Shell
    tshark -r dns.pcap -Y 'dns' -T fields -e frame.time_delta -e dns.qry.name
    ```
    

---

### **5. Wireless Analysis (Bonus)**

### **5.1 Monitor-mode capture with aircrack-ng**

```Shell
sudo airmon-ng start wlan0
sudo airodump-ng wlan0mon --channel 6 --write wireless.pcap
```

### **5.2 WPA handshake capture**

```Shell
sudo tcpdump -i wlan0mon -s0 -w wpa_handshake.pcap '(ether proto 0x888e)'
```

### **5.3 Pre-shared key cracking**

```Shell
aircrack-ng -w rockyou.txt -b AA:BB:CC:DD:EE:FF wireless.pcap
```

---

### **Filter Design Principles**

1. **Specificity**: Use BPF syntax to isolate layers (e.g., `udp` for DNS query types).
2. **Performance**: Limit captures with `c 1000` (packet count) or `G 60` (rotate files every 60s).
3. **Readability**: Add comments for complex filters:
    
    ```Shell
    # Capture TCP SYN packets excluding loopback
    sudo tcpdump -i any 'tcp[tcpflags] & (tcp-syn) != 0 and not dst net 127.0.0.0/8'
    ```
    
4. **Verification**: Validate filters with `d` to dump compiled BPF code:
    
    ```Shell
    tcpdump -d 'port 53 and (udp or tcp)'
    ```
    

This CLI-focused approach ensures reproducibility and granular control over network analysis tasks. For GUI-based tools like Wireshark, substitute `tcpdump` captures with `tshark` for similar functionality in automated pipelines.