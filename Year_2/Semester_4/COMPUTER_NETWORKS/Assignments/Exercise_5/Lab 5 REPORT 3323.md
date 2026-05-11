## i. Εφαρμογή του πρωτοκόλλου Spanning Tree
![](images/Lab5_p1.png)
### 1. Εκλογή Γέφυρας Ρίζας (Root Bridge)

Η γέφυρα με το μικρότερο αναγνωριστικό (ID) εκλέγεται ως **Root Bridge**.
- **Αποτέλεσμα:** Η γέφυρα **$B1$** είναι η Ρίζα του δέντρου.

### 2. Ανταλλαγή Μηνυμάτων (BPDU) και Επιλογή Θυρών Ρίζας

- **$B1$:** Στέλνει $(B1, 0, B1)$ στα LAN $A, B, D$.
- **$B3$:** Λαμβάνει το μήνυμα στο LAN $A$. Θέτει ως **Root Port (RP)** τη θύρα προς το $A$ (Κόστος $1$). Στέλνει $(B1, 1, B3)$ στο LAN $C$.
- **$B5$:** Λαμβάνει το μήνυμα στο LAN $D$. Θέτει ως **RP** τη θύρα προς το $D$ (Κόστος $1$). Στέλνει $(B1, 1, B5)$ στα LAN $E, F, G, H$.
- **$B7$:** Λαμβάνει το μήνυμα στο LAN $B$. Θέτει ως **RP** τη θύρα προς το $B$ (Κόστος $1$). Στέλνει $(B1, 1, B7)$ στα LAN $F, K$.
- **$B2$:** Λαμβάνει $(B1, 1, B3)$ από το $C$ και $(B1, 1, B5)$ από το $E$. Το συνολικό κόστος και από τις δύο είναι $2$. Επιλέγει ως **RP** τη θύρα προς το $C$ λόγω χαμηλότερου ID αποστολέα ($B3 < B5$).
- **$B4$:** Λαμβάνει $(B1, 1, B5)$ από το $H$. Θέτει ως **RP** τη θύρα προς το $H$ (Κόστος $2$). Στέλνει $(B1, 2, B4)$ στα $I, J$.
- **$B6$:** Λαμβάνει $(B1, 1, B5)$ από το $G$. Θέτει ως **RP** τη θύρα προς το $G$ (Κόστος $2$). Στέλνει $(B1, 2, B6)$ στο $I$.

---

### 3. Καθορισμένες Γέφυρες (Designated Bridges) ανά LAN

|**LAN**|**Συνδεδεμένες Γέφυρες (Κόστος προς Ρίζα)**|**Καθορισμένη Γέφυρα (Designated)**|
|---|---|---|
|**A**|$B1(0), B3(1)$|**$B1$**|
|**B**|$B1(0), B7(1)$|**$B1$**|
|**D**|$B1(0), B5(1)$|**$B1$**|
|**C**|$B3(1), B2(2)$|**$B3$**|
|**E**|$B5(1), B2(2)$|**$B5$**|
|**F**|$B5(1), B7(1)$|**$B5$** (λόγω ID: $5 < 7$)|
|**G**|$B5(1), B6(2)$|**$B5$**|
|**H**|$B5(1), B4(2)$|**$B5$**|
|**I**|$B4(2), B6(2)$|**$B4$** (λόγω ID: $4 < 6$)|
|**J**|$B4(2)$|**$B4$**|
|**K**|$B7(1)$|**$B7$**|

---

### 4. Συμπέρασμα

Μια γέφυρα δεν συμπεριλαμβάνεται στο ενεργό δέντρο (δηλαδή δεν προωθεί πακέτα δεδομένων) εάν όλες οι θύρες της, εκτός από τη θύρα ρίζας (RP), τίθενται σε κατάσταση **Blocking**. Αυτό συμβαίνει όταν η γέφυρα δεν είναι "Καθορισμένη" (Designated) για κανένα από τα LAN στα οποία συνδέεται.

- **Γέφυρα $B2$:**
    - Στο LAN $C$, καθορισμένη είναι η $B3$.
    - Στο LAN $E$, καθορισμένη είναι η $B5$.
    - Η $B2$ δεν εξυπηρετεί κανένα LAN, άρα **δεν συμπεριλαμβάνεται**.
- **Γέφυρα $B6$:**
    - Στο LAN $G$, καθορισμένη είναι η $B5$.
    - Στο LAN $I$, καθορισμένη είναι η $B4$.
    - Η $B6$ δεν εξυπηρετεί κανένα LAN, άρα **δεν συμπεριλαμβάνεται**.

**Απάντηση:** Οι γέφυρες που δεν θα συμπεριληφθούν στο δέντρο διάσχισης είναι οι **$B2$** και **$B6$**.

---
## ii. Εφαρμογή του αλγορίθμου Dijkstra

![](images/Lab5_p2-a.png)
## Πίνακας 1

- Round 1, προσθήκη A: A=0, B=20, C=20, D=∞, E=∞, F=∞, G=∞, H=∞.
- Round 2, προσθήκη B: A=0, B=20, C=20, D=25, E=∞, F=∞, G=∞, H=∞.
- Round 3, προσθήκη C: A=0, B=20, C=20, D=25, E=25, F=∞, G=∞, H=∞.
- Round 4, προσθήκη D: A=0, B=20, C=20, D=25, E=25, F=30, G=∞, H=∞.
- Round 5, προσθήκη E: A=0, B=20, C=20, D=25, E=25, F=30, G=30, H=∞.
- Round 6, προσθήκη F: A=0, B=20, C=20, D=25, E=25, F=30, G=30, H=40.
- Round 7, προσθήκη G: A=0, B=20, C=20, D=25, E=25, F=30, G=30, H=40.
- Round 8, προσθήκη H: A=0, B=20, C=20, D=25, E=25, F=30, G=30, H=40.

## Συμπληρωμένος πίνακας

|Round|Προσθήκη κόμβου|A|B|C|D|E|F|G|H|
|---|---|---|---|---|---|---|---|---|---|
|1|A|0|20|20|∞|∞|∞|∞|∞|
|2|B|0|20|20|25|∞|∞|∞|∞|
|3|C|0|20|20|25|25|∞|∞|∞|
|4|D|0|20|20|25|25|30|∞|∞|
|5|E|0|20|20|25|25|30|30|∞|
|6|F|0|20|20|25|25|30|30|40|
|7|G|0|20|20|25|25|30|30|40|
|8|H|0|20|20|25|25|30|30|40|

## Τελικό αποτέλεσμα

- Σειρά οριστικοποίησης κόμβων: A, B, C, D, E, F, G, H.
- Συντομότερη διαδρομή: A → B → D → F → H.
- Συνολικό κόστος: 40.

## iii. Εφαρμογή του αλγορίθμου Bellman Ford

![](images/Lab5_p3.png)

## Πίνακας 2

|Κόμβος|A|B|C|D|
|---|---|---|---|---|
|A|0|2|7|∞|
|B|2|0|1|3|
|C|7|1|0|1|
|D|∞|3|1|0|

## Πίνακας 3

|Κόμβος|A|B|C|D|
|---|---|---|---|---|
|A|0|2|3|4|
|B|2|0|1|2|
|C|3|1|0|1|
|D|4|2|1|0|

---
## LAB 
## i. Δημιουργία δικτύου

> **File: Lab5-3323-RIP.pkt**

![](images/Main_Network.png)



### PC Configurations

  
**PC0** IP: 10.10.3.1 Mask: 255.255.255.252 Gateway: 10.10.3.2 
**PC1** IP: 10.10.1.1 Mask: 255.255.255.252 Gateway: 10.10.1.2 
**PC2** IP: 10.10.2.1 Mask: 255.255.255.252 Gateway: 10.10.2.2 
**PC3** IP: 10.10.4.1 Mask: 255.255.255.252 Gateway: 10.10.4.2 
**PC4** IP: 10.10.5.1 Mask: 255.255.255.252 Gateway: 10.10.5.2 
**PC5** IP: 10.10.8.1 Mask: 255.255.255.252 Gateway: 10.10.8.2 
**PC6** IP: 10.10.7.1 Mask: 255.255.255.252 Gateway: 10.10.7.2 
**PC7** IP: 10.10.6.1 Mask: 255.255.255.252 Gateway: 10.10.6.2
### Shell input: 
**$PC_χ$:**  
```  
ipconfig <IP> <MASK> <GATEWAY>  
```  
  
---

### Router CLI Commands

#### Router0
```bash
enable
configure terminal
interface fa0/0
 ip address 10.10.3.2 255.255.255.252
 no shutdown
exit
interface s0/0/0
 shutdown
 no ip address
 ip address 10.10.15.1 255.255.255.252
 clock rate 64000
 no shutdown
exit
interface s0/1/0
 shutdown
 no ip address
 ip address 10.10.10.1 255.255.255.252
 clock rate 64000
 no shutdown
exit
interface s0/1/1
 shutdown
 no ip address
 ip address 10.10.12.1 255.255.255.252
 clock rate 64000
 no shutdown
exit
end
write memory
```

#### Router1
```bash
enable
configure terminal
interface fa0/0
 ip address 10.10.1.2 255.255.255.252
 no shutdown
exit
interface s0/1/0
 shutdown
 no ip address
 ip address 10.10.10.2 255.255.255.252
 clock rate 64000
 no shutdown
exit
interface s0/1/1
 shutdown
 no ip address
 ip address 10.10.11.1 255.255.255.252
 clock rate 64000
 no shutdown
exit
end
write memory
```

#### Router2
```bash
enable
configure terminal
interface fa0/0
 ip address 10.10.2.2 255.255.255.252
 no shutdown
exit
interface s0/1/0
 shutdown
 no ip address
 ip address 10.10.11.2 255.255.255.252
 clock rate 64000
 no shutdown
exit
interface s0/1/1
 shutdown
 no ip address
 ip address 10.10.12.2 255.255.255.252
 clock rate 64000
 no shutdown
exit
interface s0/0/0
 shutdown
 no ip address
 ip address 10.10.13.1 255.255.255.252
 clock rate 64000
 no shutdown
exit
end
write memory
```

#### Router3
```bash
enable
configure terminal
interface fa0/0
 ip address 10.10.4.2 255.255.255.252
 no shutdown
exit
interface s0/1/0
 shutdown
 no ip address
 ip address 10.10.15.2 255.255.255.252
 clock rate 64000
 no shutdown
exit
interface s0/0/0
 shutdown
 no ip address
 ip address 10.10.16.1 255.255.255.252
 clock rate 64000
 no shutdown
exit
interface s0/1/1
 shutdown
 no ip address
 ip address 10.10.14.1 255.255.255.252
 clock rate 64000
 no shutdown
exit
end
write memory
```

#### Router4
```bash
enable
configure terminal
interface fa0/0
 ip address 10.10.5.2 255.255.255.252
 no shutdown
exit
interface s0/1/0
 shutdown
 no ip address
 ip address 10.10.16.2 255.255.255.252
 clock rate 64000
 no shutdown
exit
interface s0/0/0
 shutdown
 no ip address
 ip address 10.10.17.1 255.255.255.252
 clock rate 64000
 no shutdown
exit
interface s0/1/1
 shutdown
 no ip address
 ip address 10.10.18.1 255.255.255.252
 clock rate 64000
 no shutdown
exit
end
write memory
```

#### Router5
```bash
enable
configure terminal
interface fa0/0
 ip address 10.10.8.2 255.255.255.252
 no shutdown
exit
interface s0/1/0
 shutdown
 no ip address
 ip address 10.10.13.2 255.255.255.252
 clock rate 64000
 no shutdown
exit
interface s0/1/1
 shutdown
 no ip address
 ip address 10.10.14.2 255.255.255.252
 clock rate 64000
 no shutdown
exit
interface s0/0/0
 shutdown
 no ip address
 ip address 10.10.20.1 255.255.255.252
 clock rate 64000
 no shutdown
exit
end
write memory
```

#### Router6
```bash
enable
configure terminal
interface fa0/0
 ip address 10.10.7.2 255.255.255.252
 no shutdown
exit
interface s0/1/0
 shutdown
 no ip address
 ip address 10.10.20.2 255.255.255.252
 clock rate 64000
 no shutdown
exit
interface s0/1/1
 shutdown
 no ip address
 ip address 10.10.17.2 255.255.255.252
 clock rate 64000
 no shutdown
exit
interface s0/0/0
 shutdown
 no ip address
 ip address 10.10.19.1 255.255.255.252
 clock rate 64000
 no shutdown
exit
end
write memory
```

#### Router7
```bash
enable
configure terminal
interface fa0/0
 ip address 10.10.6.2 255.255.255.252
 no shutdown
exit
interface s0/1/0
 shutdown
 no ip address
 ip address 10.10.19.2 255.255.255.252
 clock rate 64000
 no shutdown
exit
interface s0/1/1
 shutdown
 no ip address
 ip address 10.10.18.2 255.255.255.252
 clock rate 64000
 no shutdown
exit
end
write memory
```


### Testing Network
![](images/Ping_before_rip.png)
- Ολα καταλιγουν σε "Request timed out." καθως οι δρομολογητές γνωρίζουν μόνο τα άμεσα συνδεδεμένα δίκτυά τους. Δεν γνωρίζουν τις διαδρομές προς τα απομακρυσμένα υποδίκτυα επειδή δεν είναι ενεργό πρωτόκολλο δρομολόγησης.
---

## Router0
```bash
enable
configure terminal
router rip
 version 2
 no auto-summary
 network 10.10.3.0
 network 10.10.10.0
 network 10.10.12.0
 network 10.10.15.0
exit
end
write memory
```

## Router1
```bash
enable
configure terminal
router rip
 version 2
 no auto-summary
 network 10.10.1.0
 network 10.10.10.0
 network 10.10.11.0
exit
end
write memory
```

## Router2
```bash
enable
configure terminal
router rip
 version 2
 no auto-summary
 network 10.10.2.0
 network 10.10.11.0
 network 10.10.12.0
 network 10.10.13.0
exit
end
write memory
```

## Router3
```bash
enable
configure terminal
router rip
 version 2
 no auto-summary
 network 10.10.4.0
 network 10.10.14.0
 network 10.10.15.0
 network 10.10.16.0
exit
end
write memory
```

## Router4
```bash
enable
configure terminal
router rip
 version 2
 no auto-summary
 network 10.10.5.0
 network 10.10.16.0
 network 10.10.17.0
 network 10.10.18.0
exit
end
write memory
```

## Router5
```bash
enable
configure terminal
router rip
 version 2
 no auto-summary
 network 10.10.8.0
 network 10.10.13.0
 network 10.10.14.0
 network 10.10.20.0
exit
end
write memory
```

## Router6
```bash
enable
configure terminal
router rip
 version 2
 no auto-summary
 network 10.10.7.0
 network 10.10.17.0
 network 10.10.19.0
 network 10.10.20.0
exit
end
write memory
```

## Router7
```bash
enable
configure terminal
router rip
 version 2
 no auto-summary
 network 10.10.6.0
 network 10.10.18.0
 network 10.10.19.0
exit
end
write memory
```

![](images/Ping_with_RIP.png)
- Το δίκτυο λειτουργεί σωστά αφου οι δρομολογητές γνωρίζουν πλέον τις διαδρομές προς τα απομακρυσμένα υποδίκτυα και είναι δυνατή η επικοινωνία μεταξύ των υπολογιστών.
---

## vi. Δρομολόγηση OSPF 

### Ρύθμιση OSPF
---
> **File: Lab5-3323-OSPF.pkt**
## Router0
```bash
enable
configure terminal
router ospf 1
 network 10.10.3.0 0.0.0.3 area 0
 network 10.10.10.0 0.0.0.3 area 0
 network 10.10.12.0 0.0.0.3 area 0
 network 10.10.15.0 0.0.0.3 area 0
exit
end
write memory
```

## Router1
```bash
enable
configure terminal
router ospf 1
 network 10.10.1.0 0.0.0.3 area 0
 network 10.10.10.0 0.0.0.3 area 0
 network 10.10.11.0 0.0.0.3 area 0
exit
end
write memory
```

## Router2
```bash
enable
configure terminal
router ospf 1
 network 10.10.2.0 0.0.0.3 area 0
 network 10.10.11.0 0.0.0.3 area 0
 network 10.10.12.0 0.0.0.3 area 0
 network 10.10.13.0 0.0.0.3 area 0
exit
end
write memory
```

## Router3
```bash
enable
configure terminal
router ospf 1
 network 10.10.4.0 0.0.0.3 area 0
 network 10.10.14.0 0.0.0.3 area 0
 network 10.10.15.0 0.0.0.3 area 0
 network 10.10.16.0 0.0.0.3 area 0
exit
end
write memory
```

## Router4
```bash
enable
configure terminal
router ospf 1
 network 10.10.5.0 0.0.0.3 area 0
 network 10.10.16.0 0.0.0.3 area 0
 network 10.10.17.0 0.0.0.3 area 0
 network 10.10.18.0 0.0.0.3 area 0
exit
end
write memory
```

## Router5
```bash
enable
configure terminal
router ospf 1
 network 10.10.8.0 0.0.0.3 area 0
 network 10.10.13.0 0.0.0.3 area 0
 network 10.10.14.0 0.0.0.3 area 0
 network 10.10.20.0 0.0.0.3 area 0
exit
end
write memory
```

## Router6
```bash
enable
configure terminal
router ospf 1
 network 10.10.7.0 0.0.0.3 area 0
 network 10.10.17.0 0.0.0.3 area 0
 network 10.10.19.0 0.0.0.3 area 0
 network 10.10.20.0 0.0.0.3 area 0
exit
end
write memory
```

## Router7
```bash
enable
configure terminal
router ospf 1
 network 10.10.6.0 0.0.0.3 area 0
 network 10.10.18.0 0.0.0.3 area 0
 network 10.10.19.0 0.0.0.3 area 0
exit
end
write memory
```

### Επαλήθευση
```bash
show ip protocols
show ip route
show ip ospf neighbor
```
Router2:
```bash
Router>show ip protocols
Routing Protocol is "rip"
Sending updates every 30 seconds, next due in 11 seconds
Invalid after 180 seconds, hold down 180, flushed after 240
Outgoing update filter list for all interfaces is not set
Incoming update filter list for all interfaces is not set
Redistributing: rip
Default version control: send version 2, receive 2
  Interface             Send  Recv  Triggered RIP  Key-chain
  FastEthernet0/0       2     2     
  Serial0/0/0           2     2     
  Serial0/1/0           2     2     
  Serial0/1/1           2     2     
Automatic network summarization is not in effect
Maximum path: 4
Routing for Networks:
	10.0.0.0
Passive Interface(s):
Routing Information Sources:
	Gateway         Distance      Last Update
	10.10.11.1           120      00:00:12
	10.10.12.1           120      00:00:03
	10.10.13.2           120      00:00:12
Distance: (default is 120)

Routing Protocol is "ospf 1"
  Outgoing update filter list for all interfaces is not set 
  Incoming update filter list for all interfaces is not set 
  Router ID 10.10.13.1
  Number of areas in this router is 1. 1 normal 0 stub 0 nssa
  Maximum path: 4
  Routing for Networks:
    10.10.2.0 0.0.0.3 area 0
    10.10.11.0 0.0.0.3 area 0
    10.10.12.0 0.0.0.3 area 0
    10.10.13.0 0.0.0.3 area 0
  Routing Information Sources:  
    Gateway         Distance      Last Update 
    10.10.11.1           110      00:11:14
    10.10.13.1           110      00:10:13
    10.10.15.1           110      00:11:02
    10.10.16.1           110      00:10:17
    10.10.18.1           110      00:10:37
    10.10.19.2           110      00:09:48
    10.10.20.1           110      00:10:03
    10.10.20.2           110      00:09:48
  Distance: (default is 110)

Router>
Router>show ip route
Codes: C - connected, S - static, I - IGRP, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
       i - IS-IS, L1 - IS-IS level-1, L2 - IS-IS level-2, ia - IS-IS inter area
       * - candidate default, U - per-user static route, o - ODR
       P - periodic downloaded static route

Gateway of last resort is not set

     10.0.0.0/30 is subnetted, 19 subnets
O       10.10.1.0 [110/65] via 10.10.11.1, 00:11:19, Serial0/1/0
C       10.10.2.0 is directly connected, FastEthernet0/0
O       10.10.3.0 [110/65] via 10.10.12.1, 00:11:29, Serial0/1/1
O       10.10.4.0 [110/129] via 10.10.12.1, 00:10:21, Serial0/1/1
                  [110/129] via 10.10.13.2, 00:10:21, Serial0/0/0
O       10.10.5.0 [110/193] via 10.10.12.1, 00:10:21, Serial0/1/1
                  [110/193] via 10.10.13.2, 00:10:21, Serial0/0/0
O       10.10.6.0 [110/193] via 10.10.13.2, 00:09:50, Serial0/0/0
O       10.10.7.0 [110/129] via 10.10.13.2, 00:10:00, Serial0/0/0
O       10.10.8.0 [110/65] via 10.10.13.2, 00:10:21, Serial0/0/0
O       10.10.10.0 [110/128] via 10.10.11.1, 00:11:19, Serial0/1/0
                   [110/128] via 10.10.12.1, 00:11:19, Serial0/1/1
C       10.10.11.0 is directly connected, Serial0/1/0
C       10.10.12.0 is directly connected, Serial0/1/1
C       10.10.13.0 is directly connected, Serial0/0/0
O       10.10.14.0 [110/128] via 10.10.13.2, 00:10:21, Serial0/0/0
O       10.10.15.0 [110/128] via 10.10.12.1, 00:11:29, Serial0/1/1
O       10.10.16.0 [110/192] via 10.10.12.1, 00:10:21, Serial0/1/1
                   [110/192] via 10.10.13.2, 00:10:21, Serial0/0/0
O       10.10.17.0 [110/192] via 10.10.13.2, 00:10:00, Serial0/0/0
O       10.10.18.0 [110/256] via 10.10.12.1, 00:10:21, Serial0/1/1
                   [110/256] via 10.10.13.2, 00:10:21, Serial0/0/0
O       10.10.19.0 [110/192] via 10.10.13.2, 00:10:00, Serial0/0/0
O       10.10.20.0 [110/128] via 10.10.13.2, 00:10:21, Serial0/0/0
Router>
Router>show ip ospf neighbor


Neighbor ID     Pri   State           Dead Time   Address         Interface
10.10.20.1        0   FULL/  -        00:00:39    10.10.13.2      Serial0/0/0
10.10.11.1        0   FULL/  -        00:00:37    10.10.11.1      Serial0/1/0
10.10.15.1        0   FULL/  -        00:00:30    10.10.12.1      Serial0/1/1
Router>
Router>
```

![](images/Ping_with_OSPF.png)
- Το δίκτυο λειτουργεί σωστά με OSPF καθώς οι δρομολογητές ανταλλάσσουν LSA (Link State Advertisements) και δομούν πλήρη εικόνα της τοπολογίας μέσω του Shortest Path First αλγορίθμου.


Resources:
> 	`https://networklessons.com/system-management`