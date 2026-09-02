# Σχεδίαση Λογικής (Course 104)

## Επισκόπηση Μαθήματος
Το μάθημα αποτελεί τη θεμελιώδη εισαγωγή στα ψηφιακά συστήματα, τη σχεδίαση και ανάλυση ψηφιακών λογικών κυκλωμάτων:
- Αριθμητικά συστήματα (δυαδικό, οκταδικό, δεκαεξαδικό), αναπαράσταση προσημασμένων αριθμών, συμπλήρωμα ως προς 1 και 2, δυαδικοί κώδικες (BCD, Gray, ASCII).
- Άλγεβρα Boole, λογικές πύλες (AND, OR, NOT, NAND, NOR, XOR, XNOR), κανονικές μορφές SOP και POS.
- Ελαχιστοποίηση λογικών συναρτήσεων με Χάρτες Karnaugh (K-Maps) 2, 3 και 4 μεταβλητών και συνθήκες αδιαφορίας (don't cares).
- Σύνθεση συνδυαστικών κυκλωμάτων: ημιαθροιστές, πλήρεις αθροιστές, αθροιστές διάδοσης κρατουμένου (RCA), πολυπλέκτες (MUX), αποπολυπλέκτες (DEMUX), αποκωδικοποιητές (decoders) και κωδικοποιητές προτεραιότητας.
- Στοιχεία μνήμης και ακολουθιακά κυκλώματα: Latches, Flip-Flops (SR, D, JK, T), είσοδοι χρονισμού (clock) και ασύγχρονες είσοδοι (preset/clear).
- Ανάλυση και σύνθεση Σύγχρονων Μηχανών Πεπερασμένων Καταστάσεων (FSM - Mealy και Moore), καταχωρητές ολίσθησης (shift registers) και σύγχρονοι/ασύγχρονοι απαριθμητές (counters).

- **Κωδικός Μαθήματος:** 104 (ΣΧΕΔΙΑΣΗ ΛΟΓΙΚΗΣ)
- **Προαπαιτούμενα:** Κανένα
- **Εξάμηνο:** 1ο

---

## Δομή Καταλόγου

* **[Assignments/](Assignments/)**:
  - [`assignment_01_boolean_algebra_and_minimization.md`](Assignments/assignment_01_boolean_algebra_and_minimization.md): Εργασία Άλγεβρας Boole και ελαχιστοποίησης.
  - [`assignment_02_combinational_logic.md`](Assignments/assignment_02_combinational_logic.md): Εργασία σχεδίασης συνδυαστικών κυκλωμάτων (με Mermaid logic diagrams).
  - [`exercises.md`](Assignments/exercises.md): Πλήρως λυμένες ασκήσεις Boole, K-map, MUX και FSM απαριθμητών.
* **[Examples/](Examples/)**:
  - [`Assistance/`](Examples/Assistance/): 10 διαδραστικοί προσομοιωτές κυκλωμάτων HTML (Flip-Flops, Counters, MUX, Decoders, Shift Registers, K-Maps κ.ά.).
* **[Exams/](Exams/)**:
  - [`practice_exam_01.md`](Exams/practice_exam_01.md): Πλήρες επαναληπτικό διαγώνισμα προσομοίωσης με αναλυτικές λύσεις και αρχείο θεμάτων.
  - `Papers/`: Σαρώσεις και επίσημες λύσεις προόδων (2022, 2023, 2024) και τελικών εξετάσεων (2025).
* **[Exercises/](Exercises/)**:
  - [`exercises_boolean_algebra_and_gates.md`](Exercises/exercises_boolean_algebra_and_gates.md): Άλγεβρα Boole, λογικές πύλες και K-maps.
  - [`exercises_sequential_circuits_and_fsm.md`](Exercises/exercises_sequential_circuits_and_fsm.md): Ακολουθιακά κυκλώματα, Flip-Flops και μηχανές Mealy/Moore.
* **[Lectures/](Lectures/)**:
  - 5 επίσημες παρουσιάσεις θεωρίας σε PDF.
* **[Projects/](Projects/)**:
  - [`project_01_digital_alarm_clock_counter.md`](Projects/project_01_digital_alarm_clock_counter.md): Εξαμηνιαίο συνθετικό project σχεδίασης ψηφιακού ρολογιού-ξυπνητηριού και απαριθμητή στο Logisim.
* **[Resources/](Resources/)**:
  - [`resources.md`](Resources/resources.md): Προτεινόμενα συγγράμματα (Mano/Ciletti, Roth) και εργαλεία CAD.
  - [`Meta/mindmap.md`](Resources/Meta/mindmap.md): Αναλυτικός εννοιολογικός χάρτης μαθήματος (580+ γραμμές).
  - [`Notes/`](Resources/Notes/): 10 αναλυτικές σημειώσεις θεωρίας σε Markdown.
* **[Tutorials/](Tutorials/)**:
  - [`tutorial_01_karnaugh_maps_simplification.md`](Tutorials/tutorial_01_karnaugh_maps_simplification.md): Οδηγός απλοποίησης λογικών συναρτήσεων με Χάρτες Karnaugh.
  - [`tutorial_02_digital_logic_simulation_logisim.md`](Tutorials/tutorial_02_digital_logic_simulation_logisim.md): Προσομοίωση ψηφιακών κυκλωμάτων με Logisim Evolution.
