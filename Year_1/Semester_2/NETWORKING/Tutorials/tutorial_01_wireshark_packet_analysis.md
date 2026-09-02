# Εργαστηριακός Οδηγός 1: Ανάλυση Πακέτων Δικτύου με το Wireshark (TCP, HTTP, DNS, ARP)

## 1. Σκοπός Εργαστηρίου
Εξοικείωση με τη χρήση του αναλυτή πρωτοκόλλων `Wireshark` για την καταγραφή και αποσφαλμάτωση κίνησης δικτύου σε πραγματικό χρόνο.

---

## 2. Βασικά Φίλτρα Εμφάνισης (Display Filters)

| Πρωτόκολλο / Στόχος | Φίλτρο Wireshark | Περιγραφή |
|---|---|---|
| HTTP GET | `http.request.method == "GET"` | Προβολή αιτημάτων HTTP GET |
| TCP Handshake | `tcp.flags.syn == 1` | Εντοπισμός έναρξης συνδέσεων TCP (SYN / SYN-ACK) |
| DNS | `dns` ή `dns.qry.name contains "example.com"` | Ερωτήματα και απαντήσεις DNS |
| Συγκεκριμένη IP | `ip.addr == 192.168.1.1` | Πακέτα από/προς τη διεύθυνση IP |
| Συγκεκριμένη Θύρα | `tcp.port == 80 || tcp.port == 443` | Κίνηση Web (HTTP/HTTPS) |

---

## 3. Ανάλυση TCP 3-Way Handshake
Κατά την έναρξη σύνδεσης TCP παρατηρούνται 3 διαδοχικά πακέτα:
1. **Client $\rightarrow$ Server [SYN]:**
   - Flags: `SYN=1, ACK=0`.
   - Sequence Number: $ISN_c$ (αρχικός αριθμός σειράς πελάτη).
2. **Server $\rightarrow$ Client [SYN, ACK]:**
   - Flags: `SYN=1, ACK=1`.
   - Sequence Number: $ISN_s$, Acknowledgment Number: $ISN_c + 1$.
3. **Client $\rightarrow$ Server [ACK]:**
   - Flags: `SYN=0, ACK=1`.
   - Sequence Number: $ISN_c + 1$, Acknowledgment Number: $ISN_s + 1$.

---

## 4. Βήματα Εργαστηριακής Άσκησης
1. Ξεκινήστε την καταγραφή στη διεπαφή δικτύου σας (`eth0` ή `wlan0`).
2. Σε ένα τερματικό εκτελέστε: `curl http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file1.html`.
3. Σταματήστε την καταγραφή.
4. Εφαρμόστε το φίλτρο `http` και εντοπίστε το πακέτο GET και την απόκριση `200 OK`.
5. Κάντε δεξί κλικ στο πακέτο TCP και επιλέξτε **Follow $\rightarrow$ TCP Stream** για να δείτε την πλήρη ανταλλαγή δεδομένων.

