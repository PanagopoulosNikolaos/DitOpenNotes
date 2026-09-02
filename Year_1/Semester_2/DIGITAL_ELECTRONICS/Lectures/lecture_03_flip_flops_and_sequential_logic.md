# Διάλεξη 3: Στοιχεία Μνήμης, Flip-Flops και Ακολουθιακά Κυκλώματα

## 1. Εισαγωγή στην Ακολουθιακή Λογική

Τα ακολουθιακά κυκλώματα (Sequential Circuits) διαθέτουν εσωτερική κατάσταση (μνήμη). Η έξοδος και η επόμενη κατάσταση καθορίζονται τόσο από τις τρέχουσες εισόδους όσο και από την παρούσα κατάσταση του κυκλώματος.

---

## 2. Μανδαλωτές (Latches) vs Flip-Flops

- **Latches (Μανδαλωτές):** Ευαίσθητοι στη στάθμη (Level-triggered).
- **Flip-Flops:** Ευαίσθητοι στο μέτωπο του παλμού ρολογιού (Edge-triggered: θετικό $\uparrow$ ή αρνητικό $\downarrow$).

### Χαρακτηριστικοί Πίνακες και Εξισώσεις

| Τύπος | Εξίσωση Επόμενης Κατάστασης $Q_{next}$ | Χαρακτηριστική Συμπεριφορά |
|---|---|---|
| **SR Flip-Flop** | $Q_{next} = S + \overline{R}Q \quad (S \cdot R = 0)$ | $S=1 \Rightarrow Set$, $R=1 \Rightarrow Reset$, $S=R=1$ Απαγορευμένο |
| **D Flip-Flop** | $Q_{next} = D$ | Αποθήκευση δεδομένων (Data / Delay) |
| **JK Flip-Flop** | $Q_{next} = J\overline{Q} + \overline{K}Q$ | $J=K=1 \Rightarrow Toggle$ (Εναλλαγή) |
| **T Flip-Flop** | $Q_{next} = T \oplus Q$ | $T=1 \Rightarrow Toggle$, $T=0 \Rightarrow Hold$ |

---

## 3. Καταχωρητές (Registers) και Μετρητές (Counters)

### 3.1 Καταχωρητές Ολίσθησης (Shift Registers)
Διατάξεις διαδοχικών D Flip-Flops που μετατοπίζουν τα περιεχόμενά τους κατά μία θέση σε κάθε παλμό ρολογιού:
- SISO (Serial-In Serial-Out)
- SIPO (Serial-In Parallel-Out)
- PISO (Parallel-In Serial-Out)
- PIPO (Parallel-In Parallel-Out)

### 3.2 Σύγχρονοι vs Ασύγχρονοι Μετρητές
- **Ασύγχρονοι (Ripple Counters):** Το ρολόι κάθε βαθμίδας τροφοδοτείται από την έξοδο της προηγούμενης. Παρουσιάζουν καθυστέρηση διάδοσης (propagation delay accumulation).
- **Σύγχρονοι Μετρητές (Synchronous Counters):** Όλα τα Flip-Flops μοιράζονται το ίδιο κοινό σήμα ρολογιού, εξασφαλίζοντας ταυτόχρονη μετάβαση κατάστασης.

