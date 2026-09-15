# Διακριτά Μαθηματικά (Course 203)

## Επισκόπηση Μαθήματος
Το μάθημα εισάγει τις θεμελιώδεις μαθηματικές δομές που αποτελούν τη βάση της θεωρητικής και εφαρμοσμένης επιστήμης υπολογιστών. Περιλαμβάνει προτασιακή και κατηγορηματική λογική, θεωρία συνόλων, συνδυαστική ανάλυση, πιθανότητες, σχέσεις, θεωρία γράφων και δέντρων, καθώς και εισαγωγή στα πεπερασμένα αυτόματα και στις τυπικές γλώσσες.

- **Κωδικός Μαθήματος:** 203 (ΔΙΑΚΡΙΤΑ ΜΑΘΗΜΑΤΙΚΑ)
- **Προαπαιτούμενα:** Μαθηματική Ανάλυση (Course 101)
- **Εξάμηνο:** 2ο
- **ECTS:** 6

---

## Δομή Καταλόγου

* **[Examples/](Examples/)**: Υπολογιστικά εργαλεία και αλγόριθμοι σε Python:
  - [`01_truth_table_generator.py`](Examples/01_truth_table_generator.py): Αυτόματη κατασκευή πινάκων αληθείας και επαλήθευση λογικών ισοδυναμιών.
  - [`02_graph_algorithms_traversal.py`](Examples/02_graph_algorithms_traversal.py): Υλοποίηση γράφων, αλγόριθμοι διάσχισης BFS / DFS και έλεγχος συνεκτικότητας.
* **[Exams/](Exams/)**: Υλικό εξετάσεων και προετοιμασίας:
  - **`Papers/Official/`**: Επίσημα θέματα εξετάσεων:
    - [`2025_june_final_exam.md`](Exams/Papers/Official/2025_june_final_exam.md): Θέματα τελικής εξέτασης Ιουνίου 2025 (Ομάδες Α, Β, Γ, Δ).
    - [`2026_june_final_exam.md`](Exams/Papers/Official/2026_june_final_exam.md): Θέματα τελικής εξέτασης Ιουνίου 2026 (Ομάδες Α, Β, Γ, Δ).
    - `2025_midterm_group_a.pdf`: Επίσημα θέματα προόδου 2025 (Ομάδα Α).
    - `2025_midterm_group_b.pdf`: Επίσημα θέματα προόδου 2025 (Ομάδα Β).
  - **`Papers/Practice/`**: Διαγωνίσματα προσομοίωσης διαβαθμισμένης δυσκολίας:
    - [`mock_exam_01_easier.md`](Exams/Papers/Practice/mock_exam_01_easier.md): Προσομοίωση 1 (Βασικό επίπεδο: Σύνολα, Πίνακες Αληθείας, Βαθμοί Κορυφών).
    - [`mock_exam_02_standard.md`](Exams/Papers/Practice/mock_exam_02_standard.md): Προσομοίωση 2 (Κανονικό επίπεδο: Κλειστότητες Σχέσεων, DFA, Πιθανότητες).
    - [`mock_exam_03_standard.md`](Exams/Papers/Practice/mock_exam_03_standard.md): Προσομοίωση 3 (Κανονικό επίπεδο: Πύλες NAND/XOR, Σύνολα, Επαγωγή).
    - [`mock_exam_04_harder.md`](Exams/Papers/Practice/mock_exam_04_harder.md): Προσομοίωση 4 (Αυξημένο επίπεδο: Επίπεδοι Γράφοι/Euler, Περιορισμένες RegEx, PIE).
    - [`mock_exam_05_gotchas.md`](Exams/Papers/Practice/mock_exam_05_gotchas.md): Προσομοίωση 5 (Παγίδες εξετάσεων: Δυναμοσύνολα, NFA σε DFA, Σύνθεση Συναρτήσεων).
  - **`Solutions/`**: Πλήρεις λύσεις εξετάσεων και προσομοιώσεων:
    - `2025_midterm_with_solutions_group_a.pdf`: Αναλυτικές επίσημες λύσεις προόδου 2025 (Ομάδα Α).
    - `2025_midterm_with_solutions_group_b.pdf`: Αναλυτικές επίσημες λύσεις προόδου 2025 (Ομάδα Β).
    - [`solution_key_01_easier.md`](Exams/Solutions/solution_key_01_easier.md): Πλήρεις λύσεις για το Mock Exam 01.
    - [`solution_key_02_standard.md`](Exams/Solutions/solution_key_02_standard.md): Πλήρεις λύσεις για το Mock Exam 02.
    - [`solution_key_03_standard.md`](Exams/Solutions/solution_key_03_standard.md): Πλήρεις λύσεις για το Mock Exam 03.
    - [`solution_key_04_harder.md`](Exams/Solutions/solution_key_04_harder.md): Πλήρεις λύσεις για το Mock Exam 04.
    - [`solution_key_05_gotchas.md`](Exams/Solutions/solution_key_05_gotchas.md): Πλήρεις λύσεις για το Mock Exam 05.
  - **`images/`**: Σαρώσεις πρωτότυπων θεμάτων εξετάσεων:
    - `Exam_paper_2025_06_Team_All_Page_1.jpg`, `Exam_paper_2025_06_Team_All_Page_2.jpg`
    - `Exam_paper_2026_06_Team_All_Page_1.png`, `Exam_paper_2026_06_Team_All_Page_2.png`
* **[Exercises/](Exercises/)**: Θεματικές σειρές ασκήσεων με πλήρεις λύσεις και τράπεζα θεμάτων εξετάσεων:
  - [`01_foundations_and_sets_exercises.md`](Exercises/01_foundations_and_sets_exercises.md): Θεμέλια, περιγραφή συνόλων, πληθικότητα, κενό σύνολο, υποσύνολα και δυναμοσύνολα.
  - [`02_set_operations_and_venn_exercises.md`](Exercises/02_set_operations_and_venn_exercises.md): Πράξεις συνόλων, διαγράμματα Venn, Αρχή Εγκλεισμού - Αποκλεισμού (PIE) και αλγεβρικές αποδείξεις ταυτοτήτων.
  - [`03_logic_gates_exercises.md`](Exercises/03_logic_gates_exercises.md): Λογικές πύλες (AND, OR, NOT, NAND, NOR, XOR, XNOR), μετατροπή κυκλωμάτων και απλοποίηση Boole.
  - [`04_indexed_sets_and_well_ordering_exercises.md`](Exercises/04_indexed_sets_and_well_ordering_exercises.md): Δεικτοδοτημένες οικογένειες συνόλων, γενικευμένες ενώσεις/τομές και Αρχή Καλής Διάταξης (WOP).
  - [`05_propositional_logic_exercises.md`](Exercises/05_propositional_logic_exercises.md): Πίνακες αληθείας, λογικές ισοδυναμίες, κανονικές μορφές (CNF/DNF) και κανόνες συμπερασμού.
  - [`06_graph_theory_exercises.md`](Exercises/06_graph_theory_exercises.md): Θεώρημα χειραψιών, πίνακες γειτνίασης, ισομορφισμός, κυκλώματα Euler/Hamilton, επιπεδότητα και δέντρα.
  - [`07_automata_and_formal_languages_exercises.md`](Exercises/07_automata_and_formal_languages_exercises.md): Τυπικές γλώσσες, κανονικές εκφράσεις (RegEx), σχεδιασμός DFA και μετατροπές NFA σε DFA.
  - [`08_exam_problem_bank.md`](Exercises/08_exam_problem_bank.md): Τράπεζα θεμάτων επίσημων εξετάσεων με πλήρη καταγραφή και 40+ ασκήσεις διαβαθμισμένης εξάσκησης.
* **[Lectures/](Lectures/)**: Επίσημες διαλέξεις μαθήματος σε μορφή PDF:
  - `0 Μαθηματική Επαγωγή.pdf`
  - `1 Μαθηματική Λογική.pdf`
  - `2 Θεωρία Συνόλων.pdf`
  - `3 Συνδυαστική.pdf`
  - `4 Θεωρία Πιθανοτήτων.pdf`
  - `5 Σχέσεις.pdf`
  - `6 Θεωρία Γραφημάτων.pdf`
  - `7 Θεωρία Αυτομάτων και Τυπικών Γλωσσών.pdf`
  - `_ Πληροφορίες.pdf`
* **[Resources/](Resources/)**:
  - [`app/`](Resources/app/): Διαδραστική εκπαιδευτική εφαρμογή NiceGUI για μελέτη και επαλήθευση θεμάτων εξετάσεων.
  - [`resources.md`](Resources/resources.md): Προτεινόμενη διεθνής και ελληνική βιβλιογραφία (Rosen, Epp, Liu κ.ά.).
  - [`Meta/mindmap_discrete_mathematics.md`](Resources/Meta/mindmap_discrete_mathematics.md): Εννοιολογικός χάρτης διακριτών μαθηματικών σε Mermaid.
  - **`Notes/`**: Αναλυτικές σημειώσεις θεωρίας ανά ενότητα:
    - [`01_foundations_and_sets.md`](Resources/Notes/01_foundations_and_sets.md): Εισαγωγή, θεωρία συνόλων και θεμέλια.
    - [`02_set_operations_and_venn.md`](Resources/Notes/02_set_operations_and_venn.md): Πράξεις συνόλων και διαγράμματα Venn.
    - [`03_logic_gates.md`](Resources/Notes/03_logic_gates.md): Θεωρία λογικών πυλών και ψηφιακά κυκλώματα.
    - [`04_indexed_sets_and_well_ordering.md`](Resources/Notes/04_indexed_sets_and_well_ordering.md): Δεικτοδοτημένα σύνολα και Αρχή Καλής Διάταξης.
    - [`05_propositional_logic.md`](Resources/Notes/05_propositional_logic.md): Προτασιακή λογική, αποδείξεις και συμπερασμοί.
    - [`06_graph_theory.md`](Resources/Notes/06_graph_theory.md): Θεωρία γραφημάτων και δέντρα.
    - [`07_automata_and_formal_languages.md`](Resources/Notes/07_automata_and_formal_languages.md): Πεπερασμένα αυτόματα και τυπικές γλώσσες.

---

## Εκτέλεση Παραδειγμάτων & Εφαρμογής

### Υπολογιστικά Script (Python)

```bash
cd Examples

# Εκτέλεση του παραγωγού πινάκων αληθείας
python3 01_truth_table_generator.py

# Εκτέλεση αλγορίθμων διάσχισης γράφων
python3 02_graph_algorithms_traversal.py
```

### Διαδραστική Εφαρμογή (NiceGUI)

```bash
cd Resources/app

# Εγκατάσταση εξαρτήσεων
pip install -r requirements.txt

# Εκτέλεση εφαρμογής
python3 main.py
```
