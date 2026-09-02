# Προγραμματισμός C I (Course 103)

## Επισκόπηση Μαθήματος
Το μάθημα αποτελεί τη θεμελιώδη εισαγωγή στον δομημένο προγραμματισμό και τη γλώσσα προγραμματισμού C. Καλύπτει θεμελιώδεις έννοιες όπως μεταβλητές, τύπους δεδομένων, έλεγχο ροής, συναρτήσεις, μονοδιάστατους και δισδιάστατους πίνακες, συμβολοσειρές, αριθμητική δεικτών, δυναμική διαχείριση μνήμης, δομές (`struct`), ενώσεις (`union`) και λειτουργίες αρχείων I/O.

- **Κωδικός Μαθήματος:** 103 (ΠΡΟΓΡΑΜΜΑΤΙΣΜΟΣ I)
- **Προαπαιτούμενα:** Κανένα
- **Εξάμηνο:** 1ο

---

## Δομή Καταλόγου

* **[Assignments/](Assignments/)**: Εργασίες και πρακτικές προκλήσεις προγραμματισμού.
  - [`assignment_01_matrix_and_text_processing.md`](Assignments/assignment_01_matrix_and_text_processing.md): Εργασία επεξεργασίας πινάκων και αρχείων κειμένου.
  - [`Challenges/`](Assignments/Challenges/): 7 διαβαθμισμένες προκλήσεις προγραμματισμού (`challenges.md`) με πλήρεις λύσεις στο `Solutions/`.
  - [`exercises.md`](Assignments/exercises.md): Βασικές ασκήσεις εμπέδωσης.
* **[Examples/](Examples/)**: 20 αυτόνομα, μεταγλωττίσιμα προγράμματα επίδειξης εννοιών:
  1. `01_hello_world.c`: Βασική δομή προγράμματος.
  2. `02_variables_and_data_types.c`: Πρωτογενείς τύποι δεδομένων.
  3. `03_basic_input_output.c`: Είσοδος/έξοδος με `scanf` και `printf`.
  4. `04_arithmetic_operators.c`: Αριθμητικοί τελεστές και modulus.
  5. `05_control_flow_if_else.c`: Δομές επιλογής.
  6. `06_control_flow_switch.c`: Επιλογή πολλαπλών κλάδων (`switch`).
  7. `07_loops_for.c`: Βρόχος επανάληψης `for`.
  8. `08_loops_while.c`: Βρόχος επανάληψης `while`.
  9. `09_loops_do_while.c`: Βρόχος `do-while`.
  10. `10_functions.c`: Ορισμός και κλήση συναρτήσεων.
  11. `11_arrays.c`: Μονοδιάστατοι πίνακες.
  12. `12_strings.c`: Συμβολοσειρές χαρακτήρων.
  13. `13_pointers.c`: Βασική χρήση δεικτών και διευθύνσεων μνήμης.
  14. `14_functions_and_pointers.c`: Πέρασμα παραμέτρων κατ' αναφορά.
  15. `15_structures.c`: Δομές δεδομένων (`struct`).
  16. `16_unions.c`: Ενώσεις κοινής μνήμης (`union`).
  17. `17_file_handling_write.c`: Εγγραφή σε αρχεία κειμένου.
  18. `18_file_handling_read.c`: Ανάγνωση από αρχεία κειμένου.
  19. `19_preprocessor_directives.c`: Μακροεντολές και οδηγίες προεπεξεργαστή.
  20. `20_ctype_library.c`: Συναρτήσεις ελέγχου χαρακτήρων (`ctype.h`).
* **[Exams/](Exams/)**: Υλικό εξετάσεων και προετοιμασίας.
  - [`practice_exam_01.md`](Exams/practice_exam_01.md): Επαναληπτικό διαγώνισμα με ενδεικτικές λύσεις και αρχείο θεμάτων.
  - `Papers/images/`: Σαρώσεις παλαιότερων θεμάτων εξετάσεων.
* **[Exercises/](Exercises/)**: Θεματικές σειρές ασκήσεων με αναλυτικές λύσεις:
  - [`exercises_pointers_and_memory.md`](Exercises/exercises_pointers_and_memory.md): Δείκτες και διαχείριση μνήμης.
  - [`exercises_exam_preparation.md`](Exercises/exercises_exam_preparation.md): Θέματα προσομοίωσης εξετάσεων.
* **[Lectures/](Lectures/)**: Σημειώσεις θεωρίας και οδηγοί:
  - [`c-programming-guide.md`](Lectures/c-programming-guide.md): Πλήρης αναλυτικός οδηγός της γλώσσας C.
  - `lecture_01` έως `lecture_04`: Διαλέξεις θεωρίας.
* **[Projects/](Projects/)**:
  - [`project_01_student_management_system.md`](Projects/project_01_student_management_system.md): Εξαμηνιαίο project ανάπτυξης modular συστήματος φοιτητολογίου.
* **[Resources/](Resources/)**:
  - [`resources.md`](Resources/resources.md): Προτεινόμενα συγγράμματα και τεκμηρίωση.
  - [`Meta/mindmap_c_programming.md`](Resources/Meta/mindmap_c_programming.md): Εννοιολογικός χάρτης μαθήματος.
  - [`Notes/notes_pointers_and_dynamic_memory.md`](Resources/Notes/notes_pointers_and_dynamic_memory.md): Σημειώσεις δεικτών και heap.
* **[Tutorials/](Tutorials/)**:
  - [`tutorial_01_gcc_and_cli_workflow.md`](Tutorials/tutorial_01_gcc_and_cli_workflow.md): Οδηγός μεταγλώττισης με GCC στο Linux CLI.
  - [`tutorial_02_gdb_debugging_and_valgrind.md`](Tutorials/tutorial_02_gdb_debugging_and_valgrind.md): Αποσφαλμάτωση με GDB και έλεγχος διαρροών με Valgrind.

---

## Μεταγλώττιση και Εκτέλεση Παραδειγμάτων

Για τη μεταγλώττιση οποιουδήποτε παραδείγματος με τον μεταγλωττιστή GCC:

```bash
# Μετάβαση στον φάκελο παραδειγμάτων
cd Examples

# Μεταγλώττιση με αυστηρούς ελέγχους προτύπου C11
gcc -Wall -Wextra -pedantic -std=c11 01_hello_world.c -o hello_world

# Εκτέλεση του προγράμματος
./hello_world
```