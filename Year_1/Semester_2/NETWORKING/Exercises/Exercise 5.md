- The name of your network adapter.
```
sudo iwconfig

wlp4s0    IEEE 802.11  ESSID:"uoi open"
```

- The current connection speed.

```
sudo iwconfig

 Bit Rate=541.6 Mb/s   Tx-Power=20 dBm
```

- The MAC address of your network adapter (in hexadecimal format).
```
sudo iwconfig

D4:4F:67:03:F6:70
```

- The manufacturer of your network adapter.
```
D4:4F:67 # # HUAWEI TECHNOLOGIES CO.,LTD
```

- The network protocols currently connected to your adapter.
```
netstat -ap
# tcp        0      0 172.16.4.108:51834      104.18.26.48:https      ESTABLISHED 3333/brave --type=u

```

- The protocols related to the interface.
```
sudo ifconfig
```

```shell
wlp4s0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
````

- The total amount of data (both transmitted and received) from your network adapter.
```
ip -s link show dev wlp4s0
```

```
3: wlp4s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DORMANT group default qlen 1000
    link/ether f8:54:f6:bf:d1:6e brd ff:ff:ff:ff:ff:ff
    RX:  bytes packets errors dropped  missed    mcast        
      22858337    42522       0       120        0          0  
    TX:  bytes packets errors dropped carrier collsns        
     2673235    15322       0          0        0          0  
```

- A list of IP addresses with which your computer has recently communicated.


```
ss -ntu
```

```
Netid     State     Recv-Q     Send-Q              Local Address:Port               Peer Address:Port  
udp       ESTAB     0          0                     172.16.4.108:57352           142.251.209.42:443   
udp       ESTAB     0          0          172.16.4.108%wlp4s0:68                  172.16.0.1:67    
udp       ESTAB     0          0                     172.16.4.108:48660           104.21.59.235:443   
tcp       ESTAB     0          0                     172.16.4.108:46192           172.67.40.104:443   
tcp       ESTAB     0          0                     172.16.4.108:51834            104.18.26.48:443   
tcp       ESTAB     0          0                     172.16.4.108:44392           172.67.185.109:443  
```

---

# Wireshark Part 2

![[Pasted image 20250513120244.png]]

---

- Port 53: Common DNS port
- pcap file
- Website visited: "search.censys.io" ![[Pasted image 20250513121157.png]]

### Standard query

![[Pasted image 20250513121456.png]]

### Standard query response

![[Pasted image 20250513121723.png]]
or with TCPDUMP
```
tcpdump -X -s0 -tttt -nn -vv -r capture.pcap | grep -C 400 --color=auto 'search.censys.io'

```

|Flag|Purpose|
|---|---|
|`-X`|Show packet contents in hex and ASCII|
|`-s0`|Capture the entire packet (unlimited snapshot length)|
|`-tttt`|Show timestamps with date/time and microseconds (for even finer precision, use `-ttttt`)|
|`-vv`|Show more detailed (verbose) packet information (`-vvv` for even more)|
|`-nn`|Do not resolve hostnames or port names (show addresses and ports numerically)|
