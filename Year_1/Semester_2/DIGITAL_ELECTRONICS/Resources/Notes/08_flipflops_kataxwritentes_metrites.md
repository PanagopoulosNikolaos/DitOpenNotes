# 8. Flip-Flops, Καταχωρητές & Μετρητές

Η ενότητα αυτή μεταβαίνει από τα συνδυαστικά στα ακολουθιακά κυκλώματα. Τα flip-flops αποτελούν τα βασικά κτίρια από τα οποία κατασκευάζονται οι καταχωρητές, οι μετρητές και οι πιο πολύπλοκες ακολουθιακές μονάδες. Η διαφορά μεταξύ latch (επίπεδη διέγερση) και flip-flop (οξεία ακμή) είναι θεμελιώδης.

---

## 1. Αστατες (Latches)

### 1.1 SR Latch (NOR)

Δύο NOR πύλες αλληλοσύνδετες:

| $S$ | $R$ | $Q$ | $\bar{Q}$ | Κατάσταση |
|:---:|:---:|:---:|:---------:|:---|
| 0 | 0 | $Q_{prev}$ | $\bar{Q}_{prev}$ | Hold (κράτηση) |
| 1 | 0 | 1 | 0 | Set |
| 0 | 1 | 0 | 1 | Reset |
| 1 | 1 | X | X | Forbidden |

### 1.2 SR Latch με NAND

Ομοίως, αλλά με NAND: η είσοδος 0 είναι ενεργή (active-low):
- $\bar{S}=0, \bar{R}=1$: Set
- $\bar{S}=1, \bar{R}=0$: Reset
- $\bar{S}=1, \bar{R}=1$: Hold
- $\bar{S}=0, \bar{R}=0$: Forbidden

### 1.3 D Latch (Level-Triggered)

Επιλύει το πρόβλημα του forbidden state: $D = S$, $\bar{D} = R$:

| $EN$ | $D$ | $Q$ |
|:---:|:---:|:---:|
| 0 | X | $Q_{prev}$ |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

Η έξοδος ακολουθεί την είσοδο $D$ όσο το $EN = 1$. Αυτό οδηγεί σε transparency problems.

> **[Key Insight]** Η κατάσταση forbidden στο SR latch ($S=R=1$) μπορεί να προκαλέσει metastability — το κύκλωμα μπορεί να "κρεμαστεί" ανάμεσα σε 0 και 1 για αόριστο χρόνο.

---

## 2. Flip-Flops (Edge-Triggered)

### 2.1 SR Flip-Flop

Ομοίως με το SR latch, αλλά διεγείρεται μόνο στην οξεία (rising/falling edge) του ρολογιού.

### 2.2 D Flip-Flop

$$
Q(t+1) = D
$$

Η τιμή του $D$ στην οξεία ρολογιού καταχωρείται στο $Q$. Αυτό το FF χρησιμοποιείται σε καταχωρητές.

**Πίνακας αλήθειας:**

| $CLK$ | $D$ | $Q(t+1)$ |
|:---:|:---:|:--------:|
| Rising | 0 | 0 |
| Rising | 1 | 1 |
| Falling | X | $Q(t)$ |
| Steady | X | $Q(t)$ |

### 2.3 JK Flip-Flop

Πιο γενικό: $J=K=1$ αντιστοιχεί σε toggle.

$$
Q(t+1) = J\bar{Q}(t) + \bar{K}Q(t)
$$

| $J$ | $K$ | $Q(t+1)$ |
|:---:|:---:|:--------:|
| 0 | 0 | $Q(t)$ (Hold) |
| 0 | 1 | 0 (Reset) |
| 1 | 0 | 1 (Set) |
| 1 | 1 | $\bar{Q}(t)$ (Toggle) |

### 2.4 T Flip-Flop

$$
Q(t+1) = T \oplus Q(t)
$$

- $T = 0$: Hold
- $T = 1$: Toggle

### 2.5 Master-Slave JK FF

Συνδυασμός δύο JK FF (master και slave) για αποφυγή race-around condition:
- Το master διαβάζεται στην ανοδική ακμή
- Το slave ενεργοποιείται στην καθοδική ακμή

### 2.6 Asynchronous vs Synchronous

**Asynchronous (Preset, Clear):** Επιδρούν άμεσα, εκτός ρολογιού.
- `Preset (PR)`: Οδηγεί $Q \to 1$
- `Clear (CLR)`: Οδηγεί $Q \to 0$

**Synchronous:** Επιδρούν μόνο στην ακμή ρολογιού.

---

## 3. Μετατροπες Flip-Flops

### 3.1 Πινακες Διεγερσης (Excitation Tables)

**D Flip-Flop:**

| $Q(t)$ | $Q(t+1)$ | $D$ |
|:---:|:--------:|:---:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

**JK Flip-Flop:**

| $Q(t)$ | $Q(t+1)$ | $J$ | $K$ |
|:---:|:--------:|:---:|:---:|
| 0 | 0 | 0 | X |
| 0 | 1 | 1 | X |
| 1 | 0 | X | 1 |
| 1 | 1 | X | 0 |

**T Flip-Flop:**

| $Q(t)$ | $Q(t+1)$ | $T$ |
|:---:|:--------:|:---:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

### 3.2 Μετατροπές Μεταξύ Τύπων

**D → JK:** $D = J\bar{Q} + \bar{K}Q$
**JK → D:** $J = D$, $K = \bar{D}$ (απλός συνδεσμός)
**T → D:** $D = T \oplus Q$

---

## 4. Καταχωρητές (Registers)

### 4.1 4-Bit D FF Register (Parallel Load)

Τέσσερα D flip-flops με κοινό ρολόγι. Κάθε FF αποθηκεύει ένα bit:
- Parallel load: όλα τα $D_i$ καταχωρούνται ταυτόχρονα
- Parallel read: όλα τα $Q_i$ είναι διαθέσιμα ταυτόχρονα

### 4.2 Shift Registers

**SISO (Serial-In, Serial-Out):**
- Είσοδος ενός bit κάθε κύκλο ρολογιού
- Τα bits ολισθαίνουν κάθε κύκλο
- Εξόδος μετά από n κύκλους

**SIPO (Serial-In, Parallel-Out):**
- Είσοδος serial, ανάγνωση parallel

**PISO (Parallel-In, Serial-Out):**
- Παραλληλή φόρτωση, serial εξόδος

**PIPO (Parallel-In, Parallel-Out):**
- Παραλληλή φόρτωση, παραλληλή ανάγνωση (buffer)

### 4.3 Universal Shift Register

Μπορεί να εκτελέσει: hold, shift right, shift left, parallel load.

**Λειτουργία με 2-bit selector:**
- 00: Hold
- 01: Shift right
- 10: Shift left
- 11: Parallel load

### 4.4 Εφαρμογές

- **Buffer:** PIPO register ως μεταβατικός buffer
- **Serial communication:** SISO/SIPO/PISO για αποστολή/λήψη δεδομένων

---

## 5. Μετρητές (Counters)

### 5.1 Ασύγχρονος (Ripple) Μετρητής

Κάθε flip-flop τροφοδοτείται από την έξοδο του προηγούμενου. Ο μετρητής "χτυπά" (ripple) από το LSB στο MSB.

- 4-bit binary up counter: $0000 \to 0001 \to 0010 \to \dots \to 1111 \to 0000$
- Καθυστέρηση: αθροιστική (ripple)

### 5.2 Σύγχρονος Μετρητής

Όλα τα flip-flops διεγείρονται από το ίδιο ρολόγι. Η λογική ελέγχου εξασφαλίζει τη σωστή ακολουθία.

### 5.3 Μετρητής mod-N

Μετρητής που επαναφέρεται μετά από N καταστάσεις (0 έως N-1).

**mod-6 μετρητής:** Μετρά $000 \to 001 \to 010 \to 011 \to 100 \to 101 \to 000$
- Χρειάζεται 3 FF
- Reset: όταν μετρήσει 6 ($110$), επαναφέρεται σε 0

### 5.4 Ring Counter και Johnson Counter

**Ring Counter:** n FF σε αλυσίδα, με το τελευταίο FF να τροφοδοτεί το πρώτο (circular shift). Ενεργό bit "περνά" από θέση σε θέση.

**Johnson Counter:** n FF με το $\bar{Q}$ του τελευταίου να τροφοδοτεί το $D$ του πρώτου. Παράγει $2n$ μοναδικές καταστάσεις.

### 5.5 Up/Down Counter

Μετρητής που μπορεί να μετρήσει είτε προς τα πάνω είτε προς τα κάτω, ανάλογα με ένα control signal `UP/DOWN`.

---

## Solved Exercises

### Exercise 1: SR Latch

**Problem:** Να παρουσιαστεί η λειτουργία SR latch με NOR για αλλεπάλληλες εισόδους.

**Solution:**

$S=1, R=0$: $Q=1$ (Set)
$S=0, R=0$: $Q=1$ (Hold)
$S=0, R=1$: $Q=0$ (Reset)
$S=1, R=1$: Forbidden (αποφευκτέο)

### Exercise 2: JK Flip-Flop Toggle

**Problem:** Να αποδειχθεί ότι με $J=K=1$, το JK FF κάνει toggle σε κάθε ακμή.

**Solution:**
$Q(t+1) = J\bar{Q}(t) + \bar{K}Q(t) = 1 \cdot \bar{Q}(t) + 0 \cdot Q(t) = \bar{Q}(t)$

### Exercise 3: 4-Bit Shift Register

**Problem:** Ένα 4-bit SIPO shift register δέχεται την ακολουθία $1011$ (LSB πρώτα). Να παρουσιαστεί η κατάσταση μετά από 4 κύκλους.

**Solution:**

| Κύκλος | Είσοδος | Q3 | Q2 | Q1 | Q0 |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 1 | 0 | 0 | 0 | 1 |
| 2 | 1 | 0 | 0 | 1 | 1 |
| 3 | 0 | 0 | 1 | 1 | 1 |
| 4 | 1 | 1 | 1 | 1 | 0 |

### Exercise 4: mod-5 Counter

**Problem:** Να σχεδιαστεί mod-5 binary up counter με D flip-flops.

**Solution:**

Χρειάζονται 3 FF ($Q_2 Q_1 Q_0$). Μετρά: $000 \to 001 \to 010 \to 011 \to 100 \to 000$.

Κατάσταση reset: $101$ (5) → $000$ (0).

### Exercise 5: D→JK Μετατροπή

**Problem:** Να υλοποιηθεί JK FF χρησιμοποιώντας D FF.

**Solution:**
$$
D = J\bar{Q} + \bar{K}Q
$$

### Exercise 6: Ring Counter vs Johnson

**Problem:** Να συγκριθούν 4-bit ring και Johnson counters.

**Solution:**

| Counter | Καταστάσεις | Πλήθος |
|:---|:---:|:---:|
| Ring | $1000 \to 0100 \to 0010 \to 0001 \to 1000$ | 4 |
| Johnson | $0000 \to 1000 \to 1100 \to 1110 \to 1111 \to 0111 \to 0011 \to 0001 \to 0000$ | 8 |

### Exercise 7: Parallel Load Register

**Problem:** Να σχεδιαστεί 4-bit register με parallel load και enable.

**Solution:**

4 D-FF με MUX σε κάθε είσοδο:
- $EN = 1$: $D_i = \text{input}_i$ (parallel load)
- $EN = 0$: $D_i = Q_i$ (hold)

### Exercise 8: Up/Down mod-8 Counter

**Problem:** Να σχεδιαστεί mod-8 up/down counter με JK flip-flops.

**Solution:**

3 JK-FF με κοινό ρολόγι. Control signal $M$:
- $M = 1$: Up (normal binary)
- $M = 0$: Down (reverse binary)

$$
J_0 = K_0 = 1 \text{ (always toggle)}
$$
$$
J_1 = K_1 = Q_0 \oplus \bar{M}
$$
$$
J_2 = K_2 = Q_0 \cdot Q_1 \oplus \bar{M}
$$

---

## Exam Tip: Επιλογη Flip-Flop

Σε προβλήματα σχεδίασης FSM:
- **D FF:** Πιο απλός σχεδιασμός (εξισώσεις επόμενης κατάστασης = εξίσωση εξόδου)
- **JK FF:** Πιο ελεγκτό αλλά πιο πολύπλοκο. Αποφεύγει το invalid state
- **T FF:** Ιδανικό για counters (toggle behavior)

Θυμηθείτε: οι excitation tables είναι το κλειδί. Αν γνωρίζετε $Q(t)$ και $Q(t+1)$, μπορείτε να βρείτε πάντα την απαιτούμενη τιμή εισόδου.