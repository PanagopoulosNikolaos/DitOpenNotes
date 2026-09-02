# 7. Αθροιστές & Αριθμητικές Μονάδες

Οι αθροιστές αποτελούν το θεμέλιο κτίριο των αριθμητικών μονάδων (ALU). Η κατανόηση της διάδοσης κρατουμένου (carry propagation) είναι κρίσιμη για την ανάλυση της ταχύτητας και την επιλογή μεταξύ ripple carry και carry lookahead αρχιτεκτονικής.

---

## 1. Ημιαθροιστής (Half Adder)

### 1.1 Ορισμος

Δέχεται δύο εισόδους ($A$, $B$) και παράγει δύο εξόδους: άθροισμα ($S$) και κρατούμενο ($C$).

| $A$ | $B$ | $S$ | $C$ |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

$$
S = A \oplus B,\quad C = A \cdot B
$$

---

## 2. Πλήρης Αθροιστής (Full Adder)

### 2.1 Ορισμος

Δέχεται τρεις εισόδους ($A$, $B$, $C_{in}$) και παράγει ($S$, $C_{out}$).

| $A$ | $B$ | $C_{in}$ | $S$ | $C_{out}$ |
|:---:|:---:|:--------:|:---:|:---------:|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

$$
S = A \oplus B \oplus C_{in}
$$
$$
C_{out} = AB + BC_{in} + AC_{in}
$$

### 2.2 Υλοποιηση με 2 Ημιαθροιστες

**Δομική (structural) υλοποίηση:**
1. HA1: $S_1 = A \oplus B$, $C_1 = AB$
2. HA2: $S = S_1 \oplus C_{in}$, $C_2 = S_1 \cdot C_{in}$
3. $C_{out} = C_1 + C_2$

### 2.3 VHDL Μοντελοποιηση

**Behavioral:**
```vhdl
S <= A XOR B XOR Cin;
Cout <= (A AND B) OR (A AND Cin) OR (B AND Cin);
```

**Dataflow:**
```vhdl
S <= A XOR B XOR Cin;
Cout <= (A AND B) OR ((A XOR B) AND Cin);
```

**Structural:**
```vhdl
HA1: half_adder port map (A => A, B => B, S => S1, C => C1);
HA2: half_adder port map (A => S1, B => Cin, S => S, C => C2);
Cout <= C1 OR C2;
```

---

## 3. Παραλληλος Αθροιστής Ripple Carry

### 3.1 Αρχιτεκτονική

n Full Adders αλυσιδωτά συνδεμένοι: το $C_{out}$ κάθε FA συνδέεται με το $C_{in}$ του επόμενου.

### 3.2 Καθυστέρηση

Ο χρόνος καθυστέρησης προκύπτει από την αλυσιδωτή διάδοση του carry:

$$
T_{total} = n \cdot T_{carry}
$$

όπου $T_{carry}$ είναι ο χρόνος καθυστέρησης ενός FA για το carry.

Για 32-bit ripple carry adder με $T_{carry} = 1\text{ns}$:
$$
T_{total} = 32 \text{ns}
$$

> **[Key Insight]** Η ακρίβεια του ripple carry είναι πλήρης, αλλά η ταχύτητα είναι γραμμικά ανάλογη με το πλήθος των bits. Αυτό τονίζει την ανάγκη για carry lookahead.

---

## 4. Carry Lookahead Adder (CLA)

### 4.1 Generate και Propagate

**Generate:** $G_i = A_i \cdot B_i$ — το bit $i$ θα δημιουργήσει κρατούμενο ανεξάρτητα από την είσοδο.

**Propagate:** $P_i = A_i \oplus B_i$ — το bit $i$ θα διαδώσει κρατούμενο εάν υπάρχει είσοδος.

### 4.2 Εξισώσεις Carry

$$
C_i = G_i + P_i \cdot C_{i-1}
$$

Ανάπτυξη:
$$
C_0 = G_0 + P_0 \cdot C_{-1}
$$
$$
C_1 = G_1 + P_1 \cdot G_0 + P_1 \cdot P_0 \cdot C_{-1}
$$
$$
C_2 = G_2 + P_2 \cdot G_1 + P_2 \cdot P_1 \cdot G_0 + P_2 \cdot P_1 \cdot P_0 \cdot C_{-1}
$$

### 4.3 Ταχυτητα vs Πολυπλοκοτητα

| Χαρακτηριστικό | Ripple Carry | CLA |
|:---|:---:|:---:|
| Καθυστέρηση | $O(n)$ | $O(\log n)$ |
| Πλήθος πυλών | $O(n)$ | $O(n \log n)$ |
| Εύρεση κρατουμένου | Αλυσιδωτά | Παράλληλα |

> **[Exam Tip]** Σε εξεταστικό πρόβλημα, αν σας ζητηθεί να υπολογίσετε τον χρόνο καθυστέρησης, ελέγξτε αν ζητείται ripple carry (απλός αλλά αργός) ή CLA (πολύπλοκος αλλά γρήγορος).

---

## 5. Αφαιρέτης

### 5.1 Με 2's Complement και Αθροιστή

Η αφαίρεση $A - B$ υλοποιείται ως $A + \bar{B} + 1$.

**Κύκλωμα:**
1. Αντιστροφή όλων των bits του $B$ (NOT gates)
2. Πρόσθεση με full adder, με $C_{in} = 1$

$$
D = A + (2's \text{ complement of } B)
$$

### 5.2 Ενοποίηση Αθροιστή-Αφαιρέτη

Χρήση ελεγκτή `M`:
- $M = 0$: πρόσθεση
- $M = 1$: αφαίρεση

$$
\text{Output} = A + (B \oplus M) + M
$$

---

## 6. ALU (Arithmetic Logic Unit)

### 6.1 Συνδυασμος Λειτουργιων

Η ALU συνδυάζει αριθμητικές (πρόσθεση, αφαίρεση) και λογικές (AND, OR, XOR, NOT) λειτουργίες σε μία μονάδα.

### 6.2 Επιλογη Λειτουργιας με MUX

**Σήματα ελέγχου (ALUOp):**

| ALUOp | Λειτουργία |
|:-----:|:---|
| 00 | AND |
| 01 | OR |
| 10 | XOR |
| 11 | ADD/SUB |

---

## Solved Exercises

### Exercise 1: Half Adder Truth Table

**Problem:** Να αποδειχθεί ότι $S = A \oplus B$ και $C = AB$ για half adder.

**Solution:**

Παράγοντας τον πίνακα αλήθειας:
- $S = 1$ όταν $A \neq B$, δηλαδή $S = A \oplus B$
- $C = 1$ μόνο όταν $A = B = 1$, δηλαδή $C = AB$

### Exercise 2: Full Adder από Half Adders

**Problem:** Να αποδειχθεί ότι $C_{out} = AB + (A \oplus B)C_{in}$.

**Solution:**
$$
C_{out} = C_1 + C_2 = AB + S_1 \cdot C_{in} = AB + (A \oplus B)C_{in}
$$

### Exercise 3: 4-Bit Ripple Carry Adder

**Problem:** Να υπολογιστεί το άθροισμα $A = 1011$ και $B = 0110$ σε 4-bit ripple carry.

**Solution:**
```
  1 0 0 0    (κρατούμενα C4, C3, C2, C1)
  1 0 1 1  (11)
+ 0 1 1 0  (6)
---------
1 0 0 0 1  (17)
```

$C_{-1} = 0$:
- $C_0 = 0$: $1+0+0=1$, $S_0=1$, $C_1=0$
- $C_1 = 0$: $1+1+0=0$, $S_1=0$, $C_2=1$
- $C_2 = 1$: $0+1+1=0$, $S_2=0$, $C_3=1$
- $C_3 = 1$: $1+0+1=0$, $S_3=0$, $C_4=1$
- $S = 0001$ (με $C_4=1$)

### Exercise 4: CLA Carry Calculations

**Problem:** Για $A = 1011$, $B = 0110$ να υπολογιστούν τα Generate/Propagate και τα carry με CLA.

**Solution:**

| $i$ | $A_i$ | $B_i$ | $G_i = A_iB_i$ | $P_i = A_i \oplus B_i$ |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 0 |
| 2 | 0 | 1 | 0 | 1 |
| 3 | 1 | 0 | 0 | 1 |

$C_{-1} = 0$:
$$
C_0 = G_0 + P_0 \cdot C_{-1} = 0 + 1 \cdot 0 = 0
$$
$$
C_1 = G_1 + P_1 \cdot G_0 + P_1 \cdot P_0 \cdot C_{-1} = 1 + 0 + 0 = 1
$$
$$
C_2 = G_2 + P_2 \cdot G_1 + P_2 \cdot P_1 \cdot G_0 + P_2 \cdot P_1 \cdot P_0 \cdot C_{-1} = 0 + 1 \cdot 1 + 0 + 0 = 1
$$
$$
C_3 = G_3 + P_3 \cdot G_2 + P_3 \cdot P_2 \cdot G_1 + P_3 \cdot P_2 \cdot P_1 \cdot G_0 + \dots = 0 + 0 + 1 \cdot 0 + \dots = 0
$$

### Exercise 5: Αφαιρετης

**Problem:** Να υπολογιστεί $13 - 7$ σε 4-bit με 2's complement.

**Solution:**
1. $A = 13 = 1101$
2. $B = 7 = 0111$
3. $\bar{B} = 1000$, $2's\ complement = 1001$
4. $A + (-B) = 1101 + 1001 = 10110 \to 0110$ (απόρριψη carry)
5. $S = 0110 = 6$

### Exercise 6: 8-to-1 MUX ALU

**Problem:** Να σχεδιαστεί ALU που εκτελεί 4 λειτουργίες με 2-to-4 decoder και MUX.

**Solution:**
1. 2-to-4 decoder δημιουργεί enable signals για 4 λειτουργίες
2. Κάθε λειτουργία (AND, OR, XOR, ADD) έχει εξειδικευμένο κύκλωμα
3. 4-to-1 MUX επιλέγει το αποτέλεσμα

### Exercise 7: Ενοποιημενος Αθροιστης-Αφαιρέτης

**Problem:** Να σχεδιαστεί 4-bit adder/subtractor με M = control.

**Solution:**

4 XOR πύλες: $B_i \oplus M$ για κάθε bit $B_i$
4 FA: $A_i + (B_i \oplus M) + C_{i-1}$

- $M = 0$: $A + B + 0$ (πρόσθεση)
- $M = 1$: $A + \bar{B} + 1$ (αφαίρεση)

### Exercise 8: Συγκριση Adders

**Problem:** Συγκρίνετε τον χρόνο εκτέλεσης ενός 16-bit ripple carry vs CLA adder με $t_{gate} = 1\text{ns}$.

**Solution:**

**Ripple Carry:**
- Carry delay ανά bit: 2 gate delays (AND + OR)
- Συνολική καθυστέρηση: $16 \times 2 = 32$ gate delays

**CLA:**
- Carry compute: 2 gate delays (παράλληλα)
- Sum compute: 2 gate delays
- Συνολική καθυστέρηση: 4 gate delays

Διαφορά: $32/4 = 8$ φορές ταχύτερος ο CLA.

---

## Exam Tip: Κρισιμο Μονοπατι (Critical Path)

Στον ripple carry adder, το κρίσιμο μονοπάτι είναι από το $C_{-1}$ (LSB) μέχρι το $C_{n-1}$ (MSB carry) και στη συνέχεια στο $S_{n-1}$ (MSB sum). Αν σας ζητηθεί να βελτιώσετε την ταχύτητα, προτείνετε CLA ή αλλαγή σε μικρότερα chunks (block CLA).