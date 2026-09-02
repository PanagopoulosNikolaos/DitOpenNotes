# Εργαστηριακή Άσκηση 4: Ανάλυση Διαδρομής (Traceroute), Πρωτόκολλο ICMP και Μηχανισμός TTL

## 1. Σκοπός της Άσκησης
Σκοπός της παρούσας εργαστηριακής άσκησης είναι η πρακτική κατανόηση του πρωτοκόλλου ελέγχου μηνυμάτων Internet (ICMP - Internet Control Message Protocol), του πεδίου Time-To-Live (TTL) της επικεφαλίδας IPv4, και της λειτουργίας των εργαλείων ανάλυσης διαδρομής (`traceroute` / `tracepath`).

---

## 2. Θεωρητικό Υπόβαθρο

### 2.1 Ο Μηχανισμός Time-To-Live (TTL)
Κάθε πακέτο IPv4 περιέχει ένα πεδίο TTL 8-bit (μέγιστη τιμή 255). Κάθε δρομολογητής (router) που προωθεί το πακέτο μειώνει το TTL κατά 1. Όταν το TTL φτάσει στο 0:
1. Ο δρομολογητής απορρίπτει το πακέτο.
2. Επιστρέφει στον αποστολέα ένα μήνυμα **ICMP Type 11 (Time Exceeded)**, Code 0.

### 2.2 Λειτουργία του Traceroute
Το εργαλείο `traceroute` εκμεταλλεύεται αυτόν τον μηχανισμό αποστέλλοντας διαδοχικές σειρές πακέτων (συνήθως UDP probes σε υψηλές θύρες ή ICMP Echo Requests) με αυξανόμενο TTL ($TTL = 1, 2, 3, \dots$):
- Με $TTL = 1$, ο πρώτος δρομολογητής απαντά με ICMP Time Exceeded.
- Με $TTL = 2$, ο δεύτερος δρομολογητής απαντά με ICMP Time Exceeded.
- Η διαδικασία συνεχίζεται μέχρι το πακέτο να φτάσει στον τελικό προορισμό, ο οποίος απαντά με **ICMP Type 3 (Destination Unreachable / Port Unreachable)** ή **ICMP Type 0 (Echo Reply)**.

---

## 3. Εργαστηριακές Δοκιμές και Εντολές

### 3.1 Εκτέλεση Traceroute με Διαφορετικά Πρωτόκολλα
```bash
# 1. Κλασικό Traceroute μέσω UDP (προεπιλογή σε Linux)
traceroute -q 3 -w 2 example.com

# 2. Traceroute μέσω ICMP Echo (όμοιο με των Windows tracert)
sudo traceroute -I -q 3 example.com

# 3. Traceroute μέσω TCP SYN στη θύρα 80 (για παράκαμψη firewalls)
sudo traceroute -T -p 80 example.com
```

### 3.2 Σύλληψη Πακέτων Traceroute με tcpdump
Σε ξεχωριστό τερματικό, ξεκινήστε τη σύλληψη της κίνησης ICMP:
```bash
sudo tcpdump -i any -n "icmp" -w traceroute_icmp.pcap
```

Στη συνέχεια εκτελέστε:
```bash
ping -c 4 -t 1 example.com   # Σκόπιμη πρόκληση TTL Exceeded
```

### 3.3 Ανάλυση του Αρχείου Σύλληψης με tshark
```bash
tshark -r traceroute_icmp.pcap -Y "icmp" -T fields \
  -e frame.number \
  -e ip.src \
  -e ip.dst \
  -e icmp.type \
  -e icmp.code
```

**Ερμηνεία Τύπων ICMP:**
- `icmp.type == 8`: Echo Request (Ping αίτημα)
- `icmp.type == 0`: Echo Reply (Ping απάντηση)
- `icmp.type == 11`: Time Exceeded (Υπέρβαση χρόνου ζωής TTL)
- `icmp.type == 3`: Destination Unreachable (Απρόσιτος προορισμός)

---

## 4. Ερωτήσεις Κατανόησης προς Παράδοση
1. Γιατί ορισμένοι ενδιάμεσοι κόμβοι σε μια εκτέλεση traceroute εμφανίζουν αστερίσκους (`* * *`);
2. Ποια είναι η διαφορά μεταξύ ICMP Type 11 Code 0 και Code 1;
3. Πώς προστατεύει το πεδίο TTL ένα δίκτυο μεταγωγής πακέτων από βρόχους δρομολόγησης (routing loops);
