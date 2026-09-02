# Ασκήσεις Εμπέδωσης: Οργάνωση και Επιδόσεις Κρυφής Μνήμης (Cache)

## Άσκηση 1: Υπολογισμός Πεδίων Διεύθυνσης σε N-way Set Associative Cache
### Εκφώνηση:
Σύστημα υπολογιστή διαθέτει:
- Διευθύνσεις μνήμης εύρους 32 bits (Byte addressable).
- Κρυφή μνήμη (Cache) συνολικής χωρητικότητας $64\text{ KB}$ δεδομένων.
- Οργάνωση 4-way Set Associative.
- Μέγεθος μπλοκ (Block / Line size) $32\text{ Bytes}$.

Ζητούνται:
1. Το πλήθος των γραμμών (blocks) της cache.
2. Το πλήθος των ομάδων (sets).
3. Ο καταμερισμός των 32 bits της διεύθυνσης σε πεδία Tag, Set Index και Byte Offset.
4. Το συνολικό μέγεθος μνήμης σε bits που απαιτείται για την υλοποίηση της cache (συμπεριλαμβανομένου 1 Valid bit και 1 Dirty bit ανά γραμμή).

### Λύση:
1. **Πλήθος γραμμών (Cache Lines):**
   $$\text{Lines} = \frac{\text{Total Capacity}}{\text{Block Size}} = \frac{64 \times 1024\text{ B}}{32\text{ B}} = \frac{65536}{32} = 2048\text{ γραμμές}$$

2. **Πλήθος ομάδων (Sets):**
   $$\text{Sets} = \frac{\text{Lines}}{N} = \frac{2048}{4} = 512\text{ ομάδες}$$

3. **Καταμερισμός Bits:**
   - **Byte Offset:** $\log_2(\text{Block Size}) = \log_2(32) = 5\text{ bits}$
   - **Set Index:** $\log_2(\text{Sets}) = \log_2(512) = 9\text{ bits}$
   - **Tag:** $32 - \text{Index} - \text{Offset} = 32 - 9 - 5 = 18\text{ bits}$

   Διάταξη: `[Tag: 18 bits] [Index: 9 bits] [Offset: 5 bits]`

4. **Συνολικό Μέγεθος Υλικού:**
   Για κάθε γραμμή αποθηκεύονται:
   - Δεδομένα: $32\text{ bytes} \times 8\text{ bits/byte} = 256\text{ bits}$
   - Tag: $18\text{ bits}$
   - Valid bit: $1\text{ bit}$
   - Dirty bit: $1\text{ bit}$
   - Σύνολο ανά γραμμή = $256 + 18 + 1 + 1 = 276\text{ bits}$

   Συνολικό μέγεθος υλικού = $2048\text{ γραμμές} \times 276\text{ bits/γραμμή} = 565,248\text{ bits} = 70,656\text{ Bytes} \approx 69\text{ KB}$.

---

## Άσκηση 2: Υπολογισμός AMAT και Επιτάχυνσης
### Εκφώνηση:
Επεξεργαστής λειτουργεί σε συχνότητα $2\text{ GHz}$ (περίοδος κύκλου $0.5\text{ ns}$) και διαθέτει:
- L1 Hit Time = 1 κύκλος
- L1 Miss Rate = $4\%$
- L2 Hit Time = 8 κύκλοι
- L2 Local Miss Rate = $15\%$
- Χρόνος Προσπέλασης Κύριας Μνήμης (Main Memory Penalty) = 150 κύκλοι

Υπολογίστε:
1. Το Global Miss Rate της L2 Cache.
2. Τον Μέσο Χρόνο Πρόσβασης στη Μνήμη (AMAT) σε κύκλους και σε νανοδευτερόλεπτα (ns).

### Λύση:
1. **Global Miss Rate:**
   $$\text{Global Miss Rate}_{L2} = \text{Miss Rate}_{L1} \times \text{Local Miss Rate}_{L2} = 0.04 \times 0.15 = 0.006\text{ (ή } 0.6\%)$$

2. **Υπολογισμός AMAT:**
   $$\text{AMAT} = \text{Hit Time}_{L1} + \text{Miss Rate}_{L1} \times (\text{Hit Time}_{L2} + \text{Local Miss Rate}_{L2} \times \text{Penalty}_{RAM})$$
   $$\text{AMAT} = 1 + 0.04 \times (8 + 0.15 \times 150)$$
   $$\text{AMAT} = 1 + 0.04 \times (8 + 22.5) = 1 + 0.04 \times 30.5 = 1 + 1.22 = 2.22\text{ κύκλοι}$$

   Σε χρόνο:
   $$\text{AMAT (ns)} = 2.22 \times 0.5\text{ ns} = 1.11\text{ ns}$$

