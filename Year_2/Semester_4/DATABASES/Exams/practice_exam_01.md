# Πρότυπη Εξεταστική Δοκιμασία: Βάσεις Δεδομένων (Practice Exam 01)

## Οδηγίες
- Χρονική διάρκεια: 2 ώρες.
- 4 ισοδύναμα θέματα (2.5 μονάδες έκαστο).
- Πλήρης τεκμηρίωση και χρήση καθαρής μαθηματικής/SQL σημειογραφίας.

---

## Θέμα 1: Σχεδίαση ER και Μετατροπή σε Πίνακες
Μια βιβλιοθήκη διαχειρίζεται βιβλία, συγγραφείς, αντίτυπα και δανεισμούς μελών.
- Κάθε Βιβλίο έχει ISBN, τίτλο, έτος και γράφεται από έναν ή περισσότερους Συγγραφείς.
- Κάθε Βιβλίο υπάρχει σε πολλαπλά Αντίτυπα (ασθενής οντότητα με αύξοντα αριθμό αντιτύπου και κατάσταση φθοράς).
- Τα Μέλη (αριθμός μητρώου, ονοματεπώνυμο, τηλέφωνο) δανείζονται συγκεκριμένα αντίτυπα καταγράφοντας ημερομηνία δανεισμού και ημερομηνία επιστροφής.
1. Σχεδιάστε το διάγραμμα ER.
2. Μετατρέψτε το διάγραμμα σε σχεσιακούς πίνακες προσδιορίζοντας ρητά Primary και Foreign Keys.

---

## Θέμα 2: Σχεσιακή Άλγεβρα
Δίνεται το σχήμα:
- `Foititis(am, onoma, etos)`
- `Mathima(kodikos, titlos, vathmida)`
- `Eggrafi(am, kodikos, vathmos)`
Διατυπώστε σε Σχεσιακή Άλγεβρα τα εξής:
1. Τα ονόματα των φοιτητών 2ου έτους (`etos = 2`) που έχουν περάσει το μάθημα με κωδικό `'DB101'` (`vathmos >= 5`).
2. Τους τίτλους των μαθημάτων στα οποία δεν έχει εγγραφεί κανένας φοιτητής.
3. Τα ονόματα των φοιτητών που έχουν εγγραφεί σε **όλα** τα μαθήματα βαθμίδας `'A'`.

---

## Θέμα 3: Ερωτήματα SQL
Βάσει του παραπάνω σχήματος, γράψτε τα αντίστοιχα ερωτήματα SQL:
1. Βρείτε για κάθε φοιτητή (AM και όνομα) τον μέσο όρο βαθμολογίας του στα μαθήματα που έχει περάσει (`vathmos >= 5`), υπό την προϋπόθεση ότι έχει περάσει τουλάχιστον 3 μαθήματα.
2. Αυξήστε κατά 10% (μέγιστο 10.0) τη βαθμολογία όλων των φοιτητών στο μάθημα με τίτλο `'Operating Systems'`.

---

## Θέμα 4: Συναρτησιακές Εξαρτήσεις και Κανονικοποίηση
Δίνεται το σχήμα $R(A, B, C, D, E)$ με $F = \{ A \to B C, \; C D \to E, \; E \to A \}$.
1. Βρείτε όλα τα υποψήφια κλειδιά.
2. Ελέγξτε αν η σχέση είναι σε 3NF και αν είναι σε BCNF.
3. Εάν δεν είναι σε BCNF, διασπάστε την σε BCNF σχέσεις με εγγύηση lossless-join.

---

## Ενδεικτικές Λύσεις

### Λύση Θέματος 1
1. Οντότητες: `Vivlio`, `Syggrafeas`, `Melos`. Ασθενής οντότητα: `Antitypo` (εξαρτάται από `Vivlio`). Συσχετίσεις: `Syggrafei` ($M:N$), `Exei_Antitypa` ($1:N$, identifying), `Daneizetai` ($M:N$ μεταξύ `Melos` και `Antitypo`).
2. Σχεσιακό Σχήμα:
   - `Vivlio(ISBN, titlos, etos)`
   - `Syggrafeas(syggrafeas_id, onoma)`
   - `VivlioSyggrafeas(ISBN, syggrafeas_id)` -> FKs σε Vivlio, Syggrafeas
   - `Antitypo(ISBN, arithmos_antitypou, katastasi)` -> PK (ISBN, arithmos_antitypou), FK ISBN -> Vivlio
   - `Melos(melos_id, onoma, tilefono)`
   - `Daneismos(melos_id, ISBN, arithmos_antitypou, imerominia_daneismou, imerominia_epistrofis)` -> PK (ISBN, arithmos_antitypou, imerominia_daneismou)

### Λύση Θέματος 2
1. $\pi_{\text{onoma}}(\sigma_{\text{etos}=2}(\text{Foititis}) \bowtie \sigma_{\text{kodikos}='DB101' \land \text{vathmos} \ge 5}(\text{Eggrafi}))$
2. $\pi_{\text{titlos}}(\text{Mathima}) - \pi_{\text{titlos}}(\text{Mathima} \bowtie \pi_{\text{kodikos}}(\text{Eggrafi}))$
3. $\pi_{\text{onoma}}((\pi_{\text{am, kodikos}}(\text{Eggrafi}) \div \pi_{\text{kodikos}}(\sigma_{\text{vathmida}='A'}(\text{Mathima}))) \bowtie \text{Foititis})$

### Λύση Θέματος 3
1.
```sql
SELECT F.am, F.onoma, ROUND(AVG(E.vathmos), 2) AS mesos_oros
FROM Foititis F
JOIN Eggrafi E ON F.am = E.am
WHERE E.vathmos >= 5.0
GROUP BY F.am, F.onoma
HAVING COUNT(E.kodikos) >= 3;
```
2.
```sql
UPDATE Eggrafi
SET vathmos = LEAST(10.0, vathmos * 1.1)
WHERE kodikos IN (SELECT kodikos FROM Mathima WHERE titlos = 'Operating Systems');
```

### Λύση Θέματος 4
1. Υποψήφια Κλειδιά:
   - $\{A, D\}^+ = \{A, D, B, C, E\}$ (από $A \to BC$, $CD \to E$).
   - $\{C, D\}^+ = \{C, D, E, A, B\}$ (από $CD \to E$, $E \to A$, $A \to BC$).
   - $\{E, D\}^+ = \{E, D, A, B, C\}$ (από $E \to A$, $A \to BC$, $CD \to E$).
   - Υποψήφια κλειδιά: $\{A, D\}, \{C, D\}, \{E, D\}$.
2. Έλεγχος Κανονικής Μορφής:
   - Για $A \to BC$: Το $A$ δεν είναι υπερκλειδί (λείπει το $D$). Όμως $B, C$ είναι prime attributes; άρα ικανοποιείται η 3NF, παραβιάζεται το BCNF.
3. Διάσπαση σε BCNF:
   - Με βάση $A \to BC$: $R_1(A, B, C)$ με κλειδί $A$.
   - Υπόλοιπο: $R_2(A, D, E)$ με κλειδιά $AD, ED$.
   - Και οι δύο σχέσεις $R_1$ και $R_2$ είναι πλέον σε BCNF.

