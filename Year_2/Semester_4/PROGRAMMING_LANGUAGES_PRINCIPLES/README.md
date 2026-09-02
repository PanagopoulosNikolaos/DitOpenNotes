# Αρχές Γλωσσών Προγραμματισμού (401)

## Επισκόπηση Μαθήματος
Το μάθημα εξετάζει σε βάθος τις θεμελιώδεις έννοιες, τις αρχιτεκτονικές σχεδίασης και τους μηχανισμούς υλοποίησης των γλωσσών προγραμματισμού. Αναλύονται η τυπική σύνταξη (γραμματικές BNF/EBNF, δένδρα συντακτικής ανάλυσης), η στατική και δυναμική σημασιολογία, τα συστήματα και οι έλεγχοι τύπων, τα προγραμματιστικά παραδείγματα (Προστακτικός, Συναρτησιακός με Haskell, Λογικός με Prolog), τα περιβάλλοντα εκτέλεσης και οι εγγραφές ενεργοποίησης (activation records), οι μηχανισμοί περάσματος παραμέτρων, η δυναμική αποστολή μεθόδων (vtables) και η αυτόματη διαχείριση μνήμης (Garbage Collection).

---

## Γενικές Πληροφορίες
- **Κωδικός Μαθήματος:** 401
- **Εξάμηνο:** 4ο (Εαρινό)
- **ECTS:** 6
- **Τύπος:** Υποχρεωτικό

---

## Δομή Καταλόγου

* [Assignments/](Assignments/) — Επίσημες εργαστηριακές ασκήσεις και σειρές προγραμματισμού:
  * [Lab/](Assignments/Lab/) — Ολοκληρωμένη σουίτα 51 εργαστηριακών ασκήσεων σε Python (E1 έως E7) με εκφωνήσεις, λύσεις και αυτοματοποιημένα τεστ.
  * [Python/](Assignments/Python/) — Διαδραστικά Jupyter Notebooks και σενάρια ασκήσεων.
* [Examples/](Examples/) — Παραδείγματα κώδικα σε διαφορετικά προγραμματιστικά παραδείγματα (Haskell, Prolog, Python, C++).
* [Exams/](Exams/) — Παλαιότερα θέματα θεωρίας και εργαστηρίου με υποδειγματικές λύσεις.
* [Exercises/](Exercises/) — Λυμένες ασκήσεις γραμματικών BNF, δένδρων παραγωγής, κανόνων αποτίμησης τύπων και ανάλυσης εμβέλειας (scoping).
* [Lectures/](Lectures/) — Ολοκληρωμένες σημειώσεις διαλέξεων (Διαλέξεις 01 έως 08):
  * [Διάλεξη 1: Εισαγωγή και Κριτήρια Αξιολόγησης Γλωσσών Προγραμματισμού](Lectures/lecture_01_introduction_and_language_evaluation.md)
  * [Διάλεξη 2: Σύνταξη, Γραμματικές χωρίς Συμφραζόμενα και BNF](Lectures/lecture_02_syntax_and_context_free_grammars.md)
  * [Διάλεξη 3: Ονόματα, Συνδέσεις, Έλεγχος Τύπων και Εμβέλεια](Lectures/lecture_03_names_bindings_type_checking_and_scopes.md)
  * [Διάλεξη 4: Συναρτησιακός και Λογικός Προγραμματισμός (Haskell & Prolog)](Lectures/lecture_04_functional_and_logic_programming.md)
  * [Διάλεξη 5: Υποπρογράμματα, Περάσματα Παραμέτρων και Περιβάλλοντα Εκτέλεσης](Lectures/lecture_05_subprograms_parameter_passing_and_runtime_environments.md)
  * [Διάλεξη 6: Αντικειμενοστρεφής Προγραμματισμός και Δυναμική Αποστολή (vtable)](Lectures/lecture_06_object_oriented_programming_and_dynamic_dispatch.md)
  * [Διάλεξη 7: Μοντέλα Ταυτοχρονισμού και Παράλληλος Προγραμματισμός](Lectures/lecture_07_concurrency_models_and_parallel_programming.md)
  * [Διάλεξη 8: Διαχείριση Μνήμης και Συλλογή Απορριμμάτων (Garbage Collection)](Lectures/lecture_08_memory_management_and_garbage_collection.md)
* [Projects/](Projects/) — Εξαμηνιαία project ανάπτυξης διερμηνέα (interpreter) ή επεξεργαστή γλώσσας (DSL).
* [Resources/](Resources/) — Βιβλιογραφία (Sebesta, Scott), cheat-sheets για Haskell και Prolog, και εννοιολογικοί χάρτες.
* [Tutorials/](Tutorials/) — Οδηγοί εγκατάστασης και εκτέλεσης περιβαλλόντων GHCi (Haskell) και SWI-Prolog.