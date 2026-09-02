# Διάλεξη 2: Επίπεδο Μεταφοράς — Πρωτόκολλα TCP, UDP και Έλεγχος Συμφόρησης

## 1. Ο Ρόλος του Επιπέδου Μεταφοράς
Το Επίπεδο Μεταφοράς (Transport Layer) παρέχει λογική επικοινωνία (logical communication) απευθείας μεταξύ διεργασιών (process-to-process) που εκτελούνται σε διαφορετικούς υπολογιστές.

### Πολυπλεξία και Αποπολυπλεξία (Multiplexing / Demultiplexing)
- **Πολυπλεξία (Multiplexing) στην Πηγή:** Συλλογή δεδομένων από πολλαπλά sockets, προσθήκη επικεφαλίδων μεταφοράς (συμπεριλαμβανομένων θυρών πηγής και προορισμού) και προώθηση στο επίπεδο δικτύου.
- **Αποπολυπλεξία (Demultiplexing) στον Προορισμό:** Εξέταση των πεδίων επικεφαλίδας του τμήματος για την παράδοση των δεδομένων στο κατάλληλο socket.
  - *UDP Socket:* Προσδιορίζεται από το ζεύγος `(Destination IP, Destination Port)`.
  - *TCP Socket:* Προσδιορίζεται από την τετράδα `(Source IP, Source Port, Destination IP, Destination Port)`.

---

## 2. Πρωτόκολλο UDP (User Datagram Protocol - RFC 768)
Το UDP είναι ένα ασύνδετο (connectionless), απλό και ελαφρύ πρωτόκολλο:
- **Χαρακτηριστικά:** Απουσία εγγύησης παράδοσης, απουσία ελέγχου συμφόρησης, διατήρηση ορίων μηνυμάτων (datagram-oriented), ελάχιστη καθυστέρηση επικεφαλίδας (μόλις 8 bytes).
- **Πεδία Επικεφαλίδας UDP:**
  1. Θύρα Πηγής (Source Port) — 16 bits
  2. Θύρα Προορισμού (Destination Port) — 16 bits
  3. Μήκος (Length) — 16 bits
  4. Άθροισμα Ελέγχου (Checksum) — 16 bits
- **Τυπικές Χρήσεις:** DNS, VoIP, streaming πολυμέσων πραγματικού χρόνου, DHCP.

---

## 3. Πρωτόκολλο TCP (Transmission Control Protocol - RFC 793)
Το TCP είναι ένα συνδετικό (connection-oriented), αξιόπιστο πρωτόκολλο ροής byte (byte-stream):
- **Χειραψία Τριών Βημάτων (Three-Way Handshake):**
  1. `Client -> Server: SYN (seq = client_isn)`
  2. `Server -> Client: SYN-ACK (seq = server_isn, ack = client_isn + 1)`
  3. `Client -> Server: ACK (seq = client_isn + 1, ack = server_isn + 1)`
- **Τερματισμός Σύνδεσης (Four-Way Teardown):**
  - Ανταλλαγή πακέτων `FIN` και `ACK` και από τις δύο κατευθύνσεις, με κατάσταση αναμονής `TIME_WAIT` στον αποστολέα του πρώτου `FIN`.

### Έλεγχος Ροής (Flow Control)
Αποτροπή υπερχείλισης του buffer του παραλήπτη. Ο παραλήπτης διαφημίζει το διαθέσιμο μέγεθος παραθύρου στο πεδίο `Receive Window (rwnd)` της επικεφαλίδας TCP. Ο αποστολέας διασφαλίζει:
$$\text{LastByteSent} - \text{LastByteAcked} \le \text{rwnd}$$

---

## 4. Έλεγχος Συμφόρησης TCP (Congestion Control)
Αποτροπή κορεσμού των ενδιάμεσων δρομολογητών του διαδικτύου. Ορίζεται η μεταβλητή παραθύρου συμφόρησης `cwnd` (Congestion Window). Ο αποστολέας περιορίζει τα μη επιβεβαιωμένα δεδομένα σε $\min(\text{cwnd}, \text{rwnd})$.

### Φάσεις Αλγορίθμου AIMD (Additive Increase, Multiplicative Decrease):
1. **Αργή Εκκίνηση (Slow Start):**
   - Αρχικοποίηση `cwnd = 1 MSS`.
   - Για κάθε ληφθέν ACK, το `cwnd` αυξάνεται κατά 1 MSS (εκθετική αύξηση: διπλασιασμός ανά RTT).
   - Διαρκεί μέχρι το `cwnd >= ssthresh` (slow start threshold).
2. **Αποφυγή Συμφόρησης (Congestion Avoidance):**
   - Για κάθε RTT, το `cwnd` αυξάνεται γραμμικά κατά 1 MSS ($+1\text{ MSS}/\text{RTT}$).
3. **Αντίδραση σε Απώλεια Πακέτου:**
   - *Τριπλό διπλότυπο ACK (Triple Duplicate ACK - TCP Reno):* Γρήγορη επανεκπομπή (Fast Retransmit), `ssthresh = cwnd / 2`, `cwnd = ssthresh + 3 MSS`, μετάβαση σε Fast Recovery.
   - *Λήξη Χρονικού Ορίου (Timeout):* `ssthresh = cwnd / 2`, `cwnd = 1 MSS`, επαναφορά σε Slow Start.

