# Δίκτυα Υπολογιστών (Course 202)

## Επισκόπηση Μαθήματος
Το μάθημα καλύπτει τις βασικές αρχές της αρχιτεκτονικής δικτύων υπολογιστών με βάση τα μοντέλα OSI και TCP/IP. Εξετάζονται τα πρωτόκολλα του επιπέδου εφαρμογής (HTTP, DNS), του επιπέδου μεταφοράς (TCP, UDP), του επιπέδου δικτύου (IPv4, ICMP, δρομολόγηση, υποδικτύωση CIDR), καθώς και του επιπέδου σύνδεσης δεδομένων (Ethernet, ARP).

- **Κωδικός Μαθήματος:** 202 (ΔΙΚΤΥΑ ΥΠΟΛΟΓΙΣΤΩΝ)
- **Προαπαιτούμενα:** Εισαγωγή στην Πληροφορική (Course 104)
- **Εξάμηνο:** 2ο
- **ECTS:** 6

---

## Δομή Καταλόγου

* **[Assignments/](Assignments/)**: Εργαστηριακές ασκήσεις ανάλυσης δικτυακής κίνησης και πρωτοκόλλων:
  - [`exercise_01_02_packet_sniffing.md`](Assignments/exercise_01_02_packet_sniffing.md): Πίνακες ARP και σύλληψη πακέτων με `tcpdump`.
  - [`exercise_03.md`](Assignments/exercise_03.md): Ανάλυση ερωτημάτων DNS με `dig`, `tcpdump` και `tshark`.
  - [`exercise_04.md`](Assignments/exercise_04.md): Ανάλυση διαδρομής (`traceroute`), πρωτόκολλο ICMP και μηχανισμός TTL.
  - [`exercise_05.md`](Assignments/exercise_05.md): Ανάλυση συνδέσεων TCP, παραθύρων ροής (flow control) και handshakes.
* **[Examples/](Examples/)**: Υπολογιστικά εργαλεία και προγράμματα socket programming:
  - [`01_tcp_echo_server.py`](Examples/01_tcp_echo_server.py) & [`01_tcp_echo_client.py`](Examples/01_tcp_echo_client.py): Επικοινωνία TCP stream socket client-server.
  - [`02_udp_server.py`](Examples/02_udp_server.py) & [`02_udp_client.py`](Examples/02_udp_client.py): Επικοινωνία UDP datagram socket.
  - [`03_subnet_calculator.py`](Examples/03_subnet_calculator.py): Πλήρης υπολογιστής υποδικτύων CIDR (μάσκες, broadcasts, εύρος hosts).
  - `data/`: Δικτυακά αρχεία δοκιμών και μεταφοράς δεδομένων (`alice.txt`).
* **[Exams/](Exams/)**: Υλικό εξετάσεων και προετοιμασίας:
  - [`practice_exam_01.md`](Exams/practice_exam_01.md): Επαναληπτικό διαγώνισμα προσομοίωσης με λύσεις.
  - **`Papers/`**: Παλαιότερα θέματα εξετάσεων (`2024_06_June_exam.md` έως `2025_02_Feb_exam.md`).
* **[Exercises/](Exercises/)**: Θεματικές σειρές ασκήσεων με αναλυτικές λύσεις:
  - [`networking_exercises_part1.md`](Exercises/networking_exercises_part1.md): 20 αναλυτικές ασκήσεις υποδικτύωσης, καθυστέρησης πακέτων και πρωτοκόλλων εφαρμογής.
  - [`networking_exercises_part2.md`](Exercises/networking_exercises_part2.md): 20 προχωρημένες ασκήσεις TCP sliding windows, εξισώσεων διακίνησης και δρομολόγησης.
  - [`exercises_ip_addressing_and_subnetting.md`](Exercises/exercises_ip_addressing_and_subnetting.md): Ασκήσεις διευθυνσιοδότησης IPv4/IPv6 και υποδικτύωσης.
  - [`exercises_tcp_congestion_control_and_routing.md`](Exercises/exercises_tcp_congestion_control_and_routing.md): Έλεγχος συμφόρησης TCP, αλγόριθμοι δρομολόγησης και υπολογισμοί καθυστέρησης.
* **[Lectures/](Lectures/)**: Επίσημες διαλέξεις θεωρίας σε PDF:
  - `01_Εισαγωγή.pdf` έως `10_Επίπεδο Εφαρμογής.pdf`
* **[Projects/](Projects/)**:
  - [`project_01_client_server_socket_chat_application.md`](Projects/project_01_client_server_socket_chat_application.md): Εξαμηνιαίο συνθετικό project ανάπτυξης εφαρμογής δικτυακής συνομιλίας (chat client/server) με sockets.
* **[Resources/](Resources/)**:
  - [`resources.md`](Resources/resources.md): Προτεινόμενα συγγράμματα (Kurose & Ross, Tanenbaum).
  - [`Meta/mindmap_computer_networks_osi_tcpip.md`](Resources/Meta/mindmap_computer_networks_osi_tcpip.md): Εννοιολογικός χάρτης δικτύων.
  - `Notes/`: Αναλυτικές σημειώσεις θεωρίας (`notes_ip_addressing...`, `notes_osi_tcp_ip_layers...`).
* **[Tutorials/](Tutorials/)**:
  - [`tutorial_01_wireshark_packet_analysis.md`](Tutorials/tutorial_01_wireshark_packet_analysis.md): Εργαστηριακός οδηγός ανάλυσης πακέτων με Wireshark.
  - [`tutorial_02_cisco_packet_tracer_subnetting_and_routing.md`](Tutorials/tutorial_02_cisco_packet_tracer_subnetting_and_routing.md): Οδηγός προσομοίωσης τοπολογιών και δρομολόγησης στο Cisco Packet Tracer.

---

## Εκτέλεση Παραδειγμάτων

```bash
cd Examples

# Εκτέλεση του υπολογιστή υποδικτύων IPv4
python3 03_subnet_calculator.py

# Εκτέλεση παραδείγματος TCP Client/Server (σε δύο τερματικά):
# Τερματικό 1:
python3 01_tcp_echo_server.py
# Τερματικό 2:
python3 01_tcp_echo_client.py
```
