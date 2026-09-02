# Ασκήσεις Εμπέδωσης: Πρωτόκολλα Μεταφοράς και Έλεγχος Συμφόρησης

## Άσκηση 1: Εξέλιξη Παραθύρου Συμφόρησης (TCP Reno AIMD)

### Εκφώνηση:
Μια σύνδεση TCP Reno ξεκινά με `cwnd = 1 MSS` και κατώφλι αργής εκκίνησης `ssthresh = 16 MSS`.
1. Ποιο θα είναι το μέγεθος του παραθύρου `cwnd` μετά από 4 RTTs αν δεν υπάρξει καμία απώλεια;
2. Αν στον 6ο γύρο (RTT 6) συμβεί απώλεια πακέτου που εντοπίζεται από **3 διπλότυπα ACKs**, ποιο θα είναι το νέο `ssthresh` και το νέο `cwnd`;
3. Αν στον 6ο γύρο η απώλεια οφειλόταν σε **Timeout**, ποιες θα ήταν οι αντίστοιχες τιμές;

### Λύση:
1. **Εξέλιξη Παραθύρου στα πρώτα 4 RTTs (Slow Start, καθώς cwnd < ssthresh = 16):**
   - RTT 0: cwnd = 1 MSS
   - RTT 1: cwnd = 2 MSS
   - RTT 2: cwnd = 4 MSS
   - RTT 3: cwnd = 8 MSS
   - RTT 4: cwnd = 16 MSS (φτάνει το ssthresh).
2. **Απώλεια με 3 Duplicate ACKs (Fast Retransmit / Fast Recovery):**
   - Στον γύρο 5 (RTT 5): cwnd = 16 + 1 = 17 MSS (Congestion Avoidance: γραμμική αύξηση).
   - Στον γύρο 6 (RTT 6): cwnd = 18 MSS. Εκεί συμβαίνει η απώλεια.
   - Νέο κατώφλι: $\text{ssthresh} = \lfloor \text{cwnd} / 2 \rfloor = \lfloor 18 / 2 \rfloor = 9\text{ MSS}$.
   - Νέο παράθυρο: $\text{cwnd} = \text{ssthresh} + 3\text{ MSS} = 9 + 3 = 12\text{ MSS}$.
3. **Απώλεια με Timeout:**
   - Νέο κατώφλι: $\text{ssthresh} = \lfloor \text{cwnd} / 2 \rfloor = 9\text{ MSS}$.
   - Νέο παράθυρο: $\text{cwnd} = 1\text{ MSS}$ (επαναφορά σε Slow Start).

---

## Άσκηση 2: Υπολογισμός Ρυθμαπόδοσης και Χρόνου Μετάδοσης

### Εκφώνηση:
Ένας αποστολέας θέλει να μεταφέρει ένα αρχείο μεγέθους $F = 10\text{ MB}$ ($10 \times 10^6\text{ bytes}$) σε έναν παραλήπτη μέσω σύνδεσης εύρους ζώνης $R = 100\text{ Mbps}$ και χρόνου διάδοσης RTT $= 40\text{ ms}$.
Αγνοώντας τις καθυστερήσεις επεξεργασίας και τις επικεφαλίδες:
1. Ποιος είναι ο καθαρός χρόνος μετάδοσης (transmission delay) του αρχείου;
2. Αν χρησιμοποιείται πρωτόκολλο Stop-and-Wait με μέγεθος πακέτου $L = 1500\text{ bytes}$, ποια είναι η μέγιστη θεωρητική ρυθμαπόδοση (throughput);

### Λύση:
1. **Καθαρός Χρόνος Μετάδοσης:**
   $$d_{\text{trans}} = \frac{F \times 8\text{ bits}}{R} = \frac{10 \times 10^6 \times 8\text{ bits}}{100 \times 10^6\text{ bits/s}} = \frac{80}{100} = 0.8\text{ δευτερόλεπτα} = 800\text{ ms}$$
2. **Μέγιστη Ρυθμαπόδοση Stop-and-Wait:**
   - Χρόνος αποστολής ενός πακέτου:
     $$t_{\text{frame}} = \frac{1500 \times 8}{100 \times 10^6} = \frac{12000}{10^8} = 0.12\text{ ms}$$
   - Συνολικός χρόνος κύκλου αποστολής και λήψης ACK:
     $$T_{\text{cycle}} = t_{\text{frame}} + \text{RTT} \approx 0.12\text{ ms} + 40\text{ ms} = 40.12\text{ ms}$$
   - Ρυθμαπόδοση:
     $$\text{Throughput} = \frac{L \times 8}{T_{\text{cycle}}} = \frac{12000\text{ bits}}{0.04012\text{ s}} \approx 299.1\text{ Kbps}$$
   - Παρατηρούμε ότι χωρίς μηχανισμό συρόμενου παραθύρου (sliding window), η αξιοποίηση του καναλιού είναι ελάχιστη ($\approx 0.3\%$).

