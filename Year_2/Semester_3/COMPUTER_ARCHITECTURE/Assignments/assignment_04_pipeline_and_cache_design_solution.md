# Λύση Εργασίας 4: Σχεδιασμός Μονάδας Διασωλήνωσης και Ανάλυση Επιδόσεων Cache

## Μέρος Α: Ανάλυση Εξαρτήσεων και Επιτάχυνσης (Pipelining)

### Δοθείς Κώδικας MIPS:
```assembly
loop:
    lw   $t1, 0($s0)       # I1
    addi $t2, $t1, 10      # I2
    sw   $t2, 0($s0)       # I3
    addi $s0, $s0, 4       # I4
    bne  $s0, $s1, loop    # I5
```

### 1. Εντοπισμός Εξαρτήσεων Δεδομένων RAW (Read-After-Write):
- **RAW στο `$t1`**: Η `lw` (I1) εγγράφει στον `$t1` στο στάδιο WB. Η `addi` (I2) διαβάζει τον `$t1` στο στάδιο ID. (Κίνδυνος Load-Use Hazard).
- **RAW στο `$t2`**: Η `addi` (I2) εγγράφει στον `$t2` στο στάδιο WB. Η `sw` (I3) διαβάζει τον `$t2` στο στάδιο MEM.
- **RAW στο `$s0`**: Η `addi` (I4) εγγράφει στον `$s0`. Η `bne` (I5) διαβάζει τον `$s0`.
- **RAW μεταξύ επαναλήψεων στο `$s0`**: Η I4 της τρέχουσας επανάληψης ενημερώνει τον `$s0`, ο οποίος διαβάζεται από την I1 της επόμενης επανάληψης.

---

### 2. Διάγραμμα Ροής Εκτέλεσης (5 Στάδια: IF, ID, EX, MEM, WB)

#### Περίπτωση 1: Χωρίς Μηχανισμό Forwarding
Χωρίς forwarding, τα αποτελέσματα είναι διαθέσιμα μόνο μετά την ολοκλήρωση του σταδίου WB (κύκλος 5 για μια εντολή).
- Μεταξύ I1 (`lw`) και I2 (`addi`): απαιτούνται **2 κύκλοι καθυστέρησης (bubbles / stalls)** ώστε το WB της I1 να ολοκληρωθεί πριν το ID της I2 διαβάσει τον `$t1`.
- Μεταξύ I2 (`addi`) και I3 (`sw`): απαιτούνται **2 κύκλοι καθυστέρησης (stalls)**.
- Μεταξύ I4 (`addi`) και I5 (`bne`): απαιτούνται **2 κύκλοι καθυστέρησης (stalls)**.
- Επιπλέον, για τη διάκλαση `bne`, αν επιλύεται στο στάδιο MEM, εισάγονται 3 κύκλοι stall αν είναι taken.

**Συνολικοί Κύκλοι ανά Επανάληψη (Χωρίς Forwarding):**
- 5 εντολές + $2 + 2 + 2 = 11$ κύκλοι (συν ποινή διακλάδωσης).
- $\text{CPI}_{\text{no-forwarding}} \approx \frac{11}{5} = 2.2$.

#### Περίπτωση 2: Με Πλήρη Μηχανισμό Forwarding
- Μεταξύ I1 (`lw`) και I2 (`addi`): Load-Use Hazard. Το δεδομένο είναι διαθέσιμο μόνο στο τέλος του MEM της I1. Επομένως, απαιτείται **μόνο 1 κύκλος stall**. Στη συνέχεια, γίνεται forwarding από MEM/WB σε EX.
- Μεταξύ I2 (`addi`) και I3 (`sw`): Forwarding απευθείας από EX/MEM της I2 στο MEM της I3. **0 stalls**.
- Μεταξύ I4 (`addi`) και I5 (`bne`): Forwarding από EX/MEM σε ID/EX. **0 stalls**.

**Συνολικοί Κύκλοι ανά Επανάληψη (Με Forwarding):**
- 5 εντολές + 1 stall load-use = 6 κύκλοι.
- $\text{CPI}_{\text{forwarding}} = \frac{6}{5} = 1.2$.

**Επιτάχυνση (Speedup):**
$$\text{Speedup} = \frac{\text{Time}_{\text{no-forwarding}}}{\text{Time}_{\text{forwarding}}} = \frac{\text{CPI}_{\text{no-forwarding}}}{\text{CPI}_{\text{forwarding}}} = \frac{2.2}{1.2} \approx 1.833$$

---

## Μέρος Β: Σχεδιασμός και Ανάλυση Κρυφής Μνήμης L1 & L2

### Δεδομένα Συστήματος:
- Μέγεθος Διεύθυνσης: $32\text{ bits}$
- **L1 Cache:** Μέγεθος $C_1 = 32\text{ KB} = 32 \times 1024\text{ B} = 32768\text{ B}$, $N_1 = 4\text{-way}$, Block Size $B = 64\text{ B}$, $t_1 = 1\text{ κύκλος}$, $h_1 = 94\% \implies m_1 = 6\%$.
- **L2 Cache:** Μέγεθος $C_2 = 512\text{ KB} = 512 \times 1024\text{ B} = 524288\text{ B}$, $N_2 = 8\text{-way}$, Block Size $B = 64\text{ B}$, $t_2 = 10\text{ κύκλοι}$, Local Hit Rate $h_{2,\text{local}} = 80\% \implies m_{2,\text{local}} = 20\%$.
- **Κύρια Μνήμη (Main Memory):** $t_{\text{mem}} = 120\text{ κύκλοι}$.

---

### 1. Υπολογισμός Bits (Tag, Index, Offset)

#### L1 Cache:
1. **Offset Bits ($b$):**
   $$b = \log_2(\text{Block Size}) = \log_2(64) = 6\text{ bits}$$
2. **Πλήθος Sets ($S_1$):**
   $$S_1 = \frac{C_1}{N_1 \times B} = \frac{32768}{4 \times 64} = \frac{32768}{256} = 128\text{ sets}$$
3. **Index Bits ($s_1$):**
   $$s_1 = \log_2(S_1) = \log_2(128) = 7\text{ bits}$$
4. **Tag Bits ($t_1$):**
   $$\text{Tag}_1 = 32 - (s_1 + b) = 32 - (7 + 6) = 32 - 13 = 19\text{ bits}$$

#### L2 Cache:
1. **Offset Bits ($b$):**
   $$b = \log_2(64) = 6\text{ bits}$$
2. **Πλήθος Sets ($S_2$):**
   $$S_2 = \frac{C_2}{N_2 \times B} = \frac{524288}{8 \times 64} = \frac{524288}{512} = 1024\text{ sets}$$
3. **Index Bits ($s_2$):**
   $$s_2 = \log_2(S_2) = \log_2(1024) = 10\text{ bits}$$
4. **Tag Bits ($t_2$):**
   $$\text{Tag}_2 = 32 - (s_2 + b) = 32 - (10 + 6) = 32 - 16 = 16\text{ bits}$$

---

### 2. Υπολογισμός Συνολικού Μεγέθους Υλικού για L1 Cache

Κάθε γραμμή (block) της L1 Cache περιέχει:
- Δεδομένα: $64\text{ Bytes} \times 8\text{ bits/Byte} = 512\text{ bits}$
- Tag: $19\text{ bits}$
- Valid bit: $1\text{ bit}$
- Dirty bit: $1\text{ bit}$
- Συνολικά bits ανά γραμμή: $512 + 19 + 1 + 1 = 533\text{ bits}$

Συνολικό πλήθος γραμμών στην L1 Cache:
$$\text{Total Blocks} = S_1 \times N_1 = 128 \times 4 = 512\text{ blocks}$$

Συνολικό μέγεθος υλικού (Hardware Storage Overhead):
$$\text{Total Storage} = 512 \times 533\text{ bits} = 272896\text{ bits} = 34112\text{ Bytes} \approx 33.31\text{ KB}$$

---

### 3. Μέσος Χρόνος Πρόσβασης στη Μνήμη (AMAT)

Ο τύπος AMAT για ιεραρχία 2 επιπέδων:
$$\text{AMAT} = t_{\text{hit, L1}} + m_1 \times \text{Miss Penalty}_{\text{L1}}$$

Όπου η ποινή αστοχίας της L1 είναι η πρόσβαση στην L2 και, σε περίπτωση αστοχίας της L2, η πρόσβαση στην κύρια μνήμη:
$$\text{Miss Penalty}_{\text{L1}} = t_{\text{hit, L2}} + m_{2,\text{local}} \times t_{\text{mem}}$$

Αντικατάσταση τιμών:
$$\text{Miss Penalty}_{\text{L1}} = 10 + 0.20 \times 120 = 10 + 24 = 34\text{ κύκλοι}$$

Υπολογισμός τελικής AMAT:
$$\text{AMAT} = 1 + 0.06 \times 34 = 1 + 2.04 = 3.04\text{ κύκλοι}$$

**Συμπέρασμα:** Ο μέσος χρόνος πρόσβασης στη μνήμη για το σύστημα είναι **$3.04$ κύκλοι ρολογιού**.

