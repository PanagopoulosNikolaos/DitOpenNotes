# Εργαστηριακός Οδηγός 2: Υποδικτύωση (Subnetting) και Διαμόρφωση Στατικής Δρομολόγησης στο Cisco Packet Tracer

## 1. Σκοπός Εργαστηρίου
Σχεδίαση τοπολογίας δικτύου με πολλαπλά υποδίκτυα (VLSM - Variable Length Subnet Masking) και ρύθμιση δρομολογητών Cisco (Cisco IOS) με στατικές διαδρομές (Static Routes).

---

## 2. Τοπολογία και Σχέδιο Διευθυνσιοδότησης

Δίνεται το δίκτυο `192.168.10.0/24`. Απαιτείται υποδιαίρεση για 3 τμήματα:
- **LAN A (Τμήμα Πωλήσεων):** Απαιτεί 50 διευθύνσεις hosts $\rightarrow$ Μάσκα `/26` ($2^6 - 2 = 62$ hosts).
  - Δίκτυο: `192.168.10.0/26` (Εύρος: `192.168.10.1` έως `192.168.10.62`, Broadcast: `192.168.10.63`).
- **LAN B (Τμήμα Μηχανικών):** Απαιτεί 25 διευθύνσεις hosts $\rightarrow$ Μάσκα `/27` ($2^5 - 2 = 30$ hosts).
  - Δίκτυο: `192.168.10.64/27` (Εύρος: `192.168.10.65` έως `192.168.10.94`, Broadcast: `192.168.10.95`).
- **WAN Link (Σύνδεση Δρομολογητών R1-R2):** Απαιτεί 2 διευθύνσεις $\rightarrow$ Μάσκα `/30` ($2^2 - 2 = 2$ hosts).
  - Δίκτυο: `192.168.10.96/30` (R1: `192.168.10.97`, R2: `192.168.10.98`, Broadcast: `192.168.10.99`).

---

## 3. Εντολές Διαμόρφωσης Δρομολογητή Cisco (CLI)

### Ρύθμιση R1
```text
Router> enable
Router# configure terminal
Router(config)# hostname R1
R1(config)# interface GigabitEthernet0/0
R1(config-if)# ip address 192.168.10.1 255.255.255.192
R1(config-if)# no shutdown
R1(config-if)# exit

R1(config)# interface Serial0/1/0
R1(config-if)# ip address 192.168.10.97 255.255.255.252
R1(config-if)# clock rate 64000
R1(config-if)# no shutdown
R1(config-if)# exit

# Στατική διαδρομή προς το LAN B
R1(config)# ip route 192.168.10.64 255.255.255.224 192.168.10.98
```

### Έλεγχος Συνδεσιμότητας
Εκτελέστε από έναν υπολογιστή του LAN A:
```bash
ping 192.168.10.65
traceroute 192.168.10.65
```

