  

# Part 1: Working with ARP Tables

The Address Resolution Protocol (ARP) table maps IP addresses to MAC addresses on your local network. Here's how to view it:

```JavaScript
arp -a # or arp
```

Example output showing IP addresses and their corresponding MAC addresses:

```Shell
┌─[✗]─[root@parrot]─[/home/ice]
└──╼ \#arp
Address                  HWtype  HWaddress           Flags Mask            Iface
172.21.0.2               ether   00:17:08:ff:60:73   C                     wlp4s0
172.21.0.1               ether   32:eb:45:fc:5a:34   C                     wlp4s0
┌─[root@parrot]─[/home/ice]
└──╼ \#arp -a
? (172.21.0.2) at 00:17:08:ff:60:73 [ether] on wlp4s0
? (172.21.0.1) at 32:eb:45:fc:5a:34 [ether] on wlp4s0
```

# Lab Exercise: Packet Capture with tcpdump

  

### 1. Capturing HTTP/HTTPS Traffic

This command captures packets for 23 seconds on interface wlp4s0:

```JavaScript
timeout 23s tcpdump -i wlp4s0 -s 0 -w capture.pcap 'tcp port 80 or tcp port 443'
```

Flags explained:

- timeout 23s: Limits capture duration to 23 seconds
- -i wlp4s0: Specifies the network interface
- -s 0: Captures entire packets
- -w capture.pcap: Saves output to a file
- 'tcp port 80 or tcp port 443': Filters for HTTP/HTTPS traffic

### 2. Analyzing HTTP GET Requests

```JavaScript
tcpdump -r capture.pcap -n -A | grep -B3 -A10 "GET"
```

Flags explained:

- -r: Reads from capture file
- -n: Displays IP addresses (no DNS resolution)
- -A: Shows packet content in ASCII
- `**| grep -B3 -A10 "GET / HTTP"**`: Pipes the output to grep, which searches for "GET / HTTP" and shows 3 lines before and 10 lines after each match

  

Sample output showing captured HTTP requests:

```Shell
reading from file capture.pcap, link-type EN10MB (Ethernet), snapshot length 262144
18:33:24.355112 IP 172.21.2.48.47276 > 49.7.133.88.80: Flags [.], ack 1, win 502, options [nop,nop,TS val 621284886 ecr 3849939146], length 0
E..4e.@.@.pt...01..X...PI,._.i.......3.....
%....yh.
18:33:24.355432 IP 172.21.2.48.47264 > 49.7.133.88.80: Flags [P.], seq 1:392, ack 1, win 502, options [nop,nop,TS val 621284887 ecr 3849939051], length 391: HTTP: GET / HTTP/1.1
E...A.@.@......01..X...Pa.A@'i......u......
%....yhkGET / HTTP/1.1
Host: people.com.cn
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8
Sec-GPC: 1
Accept-Language: en-US,en;q=0.8
Accept-Encoding: gzip, deflate


--

18:33:26.077374 IP 172.21.2.48.42486 > 138.113.149.152.80: Flags [.], ack 1, win 502, length 0
E..(..@.@......0.q.....P.....K..P....>..
18:33:26.077605 IP 172.21.2.48.42486 > 138.113.149.152.80: Flags [P.], seq 1:396, ack 1, win 502, length 395: HTTP: GET / HTTP/1.1
E.....@.@..+...0.q.....P.....K..P.......GET / HTTP/1.1
Host: www.people.com.cn
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8
Sec-GPC: 1
Accept-Language: en-US,en;q=0.8
Accept-Encoding: gzip, deflate
```

### 3. Detailed Packet Analysis

For more detailed analysis, we can use:

```Shell
sudo timeout 10s tcpdump -i any -s 0 -w capture.pcap -vvv -X 'tcp port 80 and tcp[((tcp[12:1] & 0xf0) >> 2):4] != 0'
```

This modified command does the following:

1. Uses `**timeout 10s**` to run tcpdump for 10 seconds
2. Captures on all interfaces (`**i any**`)
3. Captures full packet size (`**s 0**`)
4. Writes to a file named capture.pcap (`**w capture.pcap**`)
5. Uses very verbose output (`**vvv**`)
6. Shows packet contents in hex and ASCII (`**X**`)
7. Uses a simplified filter expression that achieves the same goal:
    - Captures TCP traffic on port 80
    - Only captures packets with data payload (not just TCP handshakes)

The simplified filter `**tcp[((tcp[12:1] & 0xf0) >> 2):4] != 0**` checks if there's data in the TCP payload

Example output:

```Shell
tcpdump: data link type LINUX_SLL2
tcpdump: listening on any, link-type LINUX_SLL2 (Linux cooked v2), snapshot length 262144 bytes
4 packets captured
4 packets received by filter
0 packets dropped by kernel
```

Note: LINUX_SLL2 doesn't include Ethernet frame information.

To read the detailed capture:

```Shell
tcpdump -r capture.pcap -n -vvv -X
```

This will read the capture file and display:

1. Source and destination MAC addresses (part of the verbose output)
2. Protocol information (HTTP in this case)
3. Full contents of the HTTP GET requests

Sample detailed output showing packet contents and headers:

```Shell
reading from file capture.pcap, link-type LINUX_SLL2 (Linux cooked v2), snapshot length 262144
Warning: interface names might be incorrect
18:57:01.069457 wlp4s0 Out IP (tos 0x0, ttl 64, id 2747, offset 0, flags [DF], proto TCP (6), length 431)
    172.21.2.48.56586 > 38.175.44.19.80: Flags [P.], cksum 0x0930 (correct), seq 3165230696:3165231087, ack 1916994400, win 502, length 391: HTTP, length: 391
	GET / HTTP/1.1
	Host: xinhuanet.com
	Connection: keep-alive
	Upgrade-Insecure-Requests: 1
	User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36
	Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8
	Sec-GPC: 1
	Accept-Language: en-US,en;q=0.5
	Accept-Encoding: gzip, deflate
	
	0x0000:  4500 01af 0abb 4000 4006 2d87 ac15 0230  E.....@.@.-....0
	0x0010:  26af 2c13 dd0a 0050 bca9 9668 7243 0360  &.,....P...hrC.`
	0x0020:  5018 01f6 0930 0000 4745 5420 2f20 4854  P....0..GET./.HT
	0x0030:  5450 2f31 2e31 0d0a 486f 7374 3a20 7869  TP/1.1..Host:.xi
	0x0040:  6e68 7561 6e65 742e 636f 6d0d 0a43 6f6e  nhuanet.com..Con
	0x0050:  6e65 6374 696f 6e3a 206b 6565 702d 616c  nection:.keep-al
	0x0060:  6976 650d 0a55 7067 7261 6465 2d49 6e73  ive..Upgrade-Ins
	0x0070:  6563 7572 652d 5265 7175 6573 7473 3a20  ecure-Requests:.
	0x0080:  310d 0a55 7365 722d 4167 656e 743a 204d  1..User-Agent:.M
	0x0090:  6f7a 696c 6c61 2f35 2e30 2028 5831 313b  ozilla/5.0.(X11;
	0x00a0:  204c 696e 7578 2078 3836 5f36 3429 2041  .Linux.x86_64).A
	0x00b0:  7070 6c65 5765 624b 6974 2f35 3337 2e33  ppleWebKit/537.3
	0x00c0:  3620 284b 4854 4d4c 2c20 6c69 6b65 2047  6.(KHTML,.like.G
	0x00d0:  6563 6b6f 2920 4368 726f 6d65 2f31 3334  ecko).Chrome/134
	0x00e0:  2e30 2e30 2e30 2053 6166 6172 692f 3533  .0.0.0.Safari/53
	0x00f0:  372e 3336 0d0a 4163 6365 7074 3a20 74ure using n65  7.36..Accept:.te
	0x0100:  7874 2f68 746d 6c2c 6170 706c 6963 6174  xt/html,applicat
	0x0110:  696f 6e2f 7868 746d 6c2b 786d 6c2c 6170  ion/xhtml+xml,ap
	0x0120:  706c 6963 6174 696f 6e2f 786d 6c3b 713d  plication/xml;q=
	0x0130:  302e 392c 696d 6167 652f 6176 6966 2c69  0.9,image/avif,i
	0x0140:  6d61 6765 2f77 6562 702c 696d 6167 652f  mage/webp,image/
	0x0150:  6170 6e67 2c2a 2f2a 3b71 3d30 2e38 0d0a  apng,*/*;q=0.8..
	0x0160:  5365 632d 4750 433a 2031 0d0a 4163 6365  Sec-GPC:.1..Acce
	0x0170:  7074 2d4c 616e 6775 6167 653a 2065 6e2d  pt-Language:.en-
	0x0180:  5553 2c65 6e3b 713d 302e 350d 0a41 6363  US,en;q=0.5..Acc
	0x0190:  6570 742d 456e 636f 6469 6e67 3a20 677a  ept-Encoding:.gz
	0x01a0:  6970 2c20 6465 666c 6174 650d 0a0d 0a    ip,.deflate....
18:57:01.171702 wlp4s0 In  IP (tos 0x0, ttl 44, id 42778, offset 0, flags [DF], proto TCP (6), length 1476)
    38.175.44.19.80 > 172.21.2.48.56586: Flags [.], cksum 0x2112 (correct), seq 1:1437, ack 391, win 165, length 1436: HTTP, length: 1436
	HTTP/1.1 200 OK
	Date: Tue, 18 Mar 2025 16:57:01 GMT
	Content-Type: text/html; charset=utf-8
	Content-Length: 43087
	Connection: keep-alive
	Vary: Accept-Encoding
	Content-Encoding: gzip
	X-Cache: HIT from x-s-v-15
	Accept-Ranges: bytes
	X-Ser: i62142_c26647, i2103121_c25795, i89830_c26665, i1979031_c23797
	X-Cache: HIT from i1979031_c23797(cloudsvr)
	
	0x0000:  4500 05c4 a71a 4000 2c06 a112 26af 2c13  E.....@.,...&.,.
...
...
...
...
	0xa2c0:  15d3 366d cd6c 7257 6d53 7832 c1f7 50f8  ..6m.lrWmSx2..P.
	0xa2d0:  a3c7 ddde                                ....
18:57:01.174488 wlp4s0 In  IP (tos 0x80, ttl 44, id 42808, offset 0, flags [DF], proto TCP (6), length 403)
    38.175.44.19.80 > 172.21.2.48.56586: Flags [P.], cksum 0xf261 (correct), seq 43081:43444, ack 391, win 165, length 363: HTTP
	0x0000:  4580 0193 a738 4000 2c06 a4a5 26af 2c13  E....8@.,...&.,.
	0x0010:  ac15 0230 0050 dd0a 7243 aba8 bca9 97ef  ...0.P..rC......
	0x0020:  5018 00a5 f261 0000 3edb d8a1 f9d9 cf32  P....a..>......2
	0x0030:  6cbe 60ff 571f bcaa 5e3e cc74 0678 9585  l.`.W...^>.t.x..
	0x0040:  3ce0 cf1a 45ad 4899 a3be ba74 6c75 f959  <...E.H....tlu.Y
	0x0050:  ebcd 3dbb 95ac 9ad5 2a67 e72b c70f a469  ..=.....*g.+...i
	0x0060:  ae67 792e aeb5 3b22 0e1d 7e0d 6895 da85  .gy...;"..~.h...
	0x0070:  91ec cefe 6261 9066 7f33 448b a4d1 497b  ....ba.f.3D...I{
	0x0080:  fba6 f1e2 86ad ddae 9c7f b067 b7e6 cc4c  ...........g...L
	0x0090:  ad2e df59 5d38 5679 3a53 bb37 d1f2 af58  ...Y]8Vy:S.7...X
	0x00a0:  26ea 3dbb 6111 fe71 db1f f8c6 463a cb36  &.=.a..q....F:.6
	0x00b0:  bd67 b79f 071b 286e 873c 56bf 7a39 4afb  .g....(n.<V.z9J.
	0x00c0:  73a5 5ef7 1d3c 9860 911b 0837 b5dc 94a8  s.^..<.`...7....
	0x00d0:  518f 8185 8606 6899 b659 204d 4b27 2695  Q.....h..Y.MK'&.
	0x00e0:  7283 79c3 5baa 800c c07e 030d 534d 347c  r.y.[....~..SM4|
	0x00f0:  ffe2 b887 5ef8 c410 0c1f 5c14 474c 3cd1  ....^.....\.GL<.
	0x0100:  9888 042e 1c94 dce4 4da3 608d 7a69 e477  ........M.`.zi.w
	0x0110:  f6e7 06ac cdde 28ec 55d6 3cc0 fa3d d9ec  ......(.U.<..=..
	0x0120:  befd a479 f304 6dfe 2c29 e608 c896 5f40  ...y..m.,)...._@
	0x0130:  3f39 6bbb 6af2 bc6d 8854 b664 aa18 26a7  ?9k.j..m.T.d..&.
	0x0140:  daa6 aa09 9622 1243 e579 4d0b 07bb 0605  .....".C.yM.....
	0x0150:  ea6f fe05 90ed da4f 2da1 1714 72b9 c1be  .o.....O-...r...
	0x0160:  5273 fc7d d4b0 727d 5926 f53e 61bf b962  Rs.}..r}Y&.>a..b
	0x0170:  aeb1 29b4 7d93 4fca c508 bf8c 2b54 def6  ..).}.O.....+T..
	0x0180:  4959 440b fc83 fbd6 6fff ffef 6f45 711a  IYD.....o...oEq.
	0x0190:  8602 00                                  ...
```