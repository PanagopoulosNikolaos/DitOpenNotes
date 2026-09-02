# Προγραμματισμός C II (Course 204)

## Επισκόπηση Μαθήματος
Το μάθημα αποτελεί τη φυσική συνέχεια του Προγραμματισμού C I, εμβαθύνοντας σε προχωρημένες τεχνικές προγραμματισμού συστημάτων, διαχείριση πόρων μνήμης, δυναμικές δομές δεδομένων και σειριοποίηση αρχείων.

- **Κωδικός Μαθήματος:** 204 (ΠΡΟΓΡΑΜΜΑΤΙΣΜΟΣ C II)
- **Προαπαιτούμενα:** Προγραμματισμός C I (Course 103)
- **Εξάμηνο:** 2ο
- **ECTS:** 6

---

## Δομή Καταλόγου

* **[Assignments/](Assignments/)**: Εργαστηριακές σειρές και εφαρμογές κώδικα:
  - [`assignment_01_character_handling_ctype.md`](Assignments/assignment_01_character_handling_ctype.md): Επεξεργασία χαρακτήρων με `<ctype.h>` (`Ctype_LIB/`).
  - [`assignment_02_string_library_toolkit.md`](Assignments/assignment_02_string_library_toolkit.md): Πλήρης εργαλειοθήκη συμβολοσειρών και αλγόριθμοι κειμένου (`String_LIB/`).
  - [`assignment_03_file_streams_io.md`](Assignments/assignment_03_file_streams_io.md): Ροές εισόδου/εξόδου και αρχεία κειμένου (`File_Handling/`).
  - [`assignment_04_structures_and_records.md`](Assignments/assignment_04_structures_and_records.md): Δομές, δυαδικά αρχεία και τυχαία προσπέλαση (`Structures/`).
* **[Examples/](Examples/)**: Αυτόνομα, μεταγλωττίσιμα προγράμματα επίδειξης προχωρημένων εννοιών:
  - `01_dynamic_memory_allocation.c`: Δυναμική δέσμευση 1D/2D πινάκων και ασφαλές `realloc`.
  - `02_singly_linked_list.c`: Πλήρης υλοποίηση απλά συνδεδεμένης λίστας.
  - `03_binary_search_tree.c`: Δυαδικό δέντρο αναζήτησης (εισαγωγή, αναζήτηση, in-order διάσχιση).
  - `04_function_pointers_and_callbacks.c`: Δείκτες συναρτήσεων, predicates και qsort comparators.
  - `05_binary_file_serialization.c`: Εγγραφή και ανάγνωση εγγραφών με `fseek`/`fread`.
  - `examples_function_pointers_and_callbacks.md`: Θεωρητικά παραδείγματα συναρτήσεων ανάκλησης.
  - `examples_structs_and_file_serialization.md`: Παραδείγματα σειριοποίησης δομών.
* **[Exams/](Exams/)**: Υλικό εξετάσεων και προετοιμασίας:
  - [`practice_exam_01.md`](Exams/practice_exam_01.md): Επαναληπτικό διαγώνισμα προσομοίωσης με λύσεις.
* **[Exercises/](Exercises/)**: Θεματικές σειρές ασκήσεων με αναλυτικές λύσεις:
  - [`exercises_dynamic_memory_and_pointers.md`](Exercises/exercises_dynamic_memory_and_pointers.md): Δυναμική μνήμη, αριθμητική δεικτών και ασφαλής αποδέσμευση.
  - [`exercises_linked_lists_and_trees.md`](Exercises/exercises_linked_lists_and_trees.md): Ασκήσεις συνδεδεμένων λιστών και δέντρων.
* **[Lectures/](Lectures/)**: Διαλέξεις και αναλυτικοί οδηγοί θεωρίας:
  - [`c_programming_guide.md`](Lectures/c_programming_guide.md): Πλήρης οδηγός προχωρημένης C (αρχεία, δείκτες, preprocessor).
  - [`dsa_guide_in_c.md`](Lectures/dsa_guide_in_c.md): Εξαντλητικός οδηγός Δομών Δεδομένων και Αλγορίθμων στη C (3.000+ γραμμές).
  - `lecture_01_pointers_and_dynamic_memory.md`: Διαφάνειες διαχείρισης heap.
  - `lecture_02_advanced_structures_and_file_io.md`: Διαφάνειες σύνθετων δομών και I/O.
* **[Projects/](Projects/)**:
  - [`project_01_custom_memory_allocator.md`](Projects/project_01_custom_memory_allocator.md): Εξαμηνιαίο συνθετικό project ανάπτυξης custom malloc/free memory allocator.
* **[Resources/](Resources/)**:
  - [`resources.md`](Resources/resources.md): Προτεινόμενη βιβλιογραφία και πηγές μελέτης.
  - [`Meta/mindmap_c_programming_advanced.md`](Resources/Meta/mindmap_c_programming_advanced.md): Εννοιολογικός χάρτης προχωρημένης C.
  - [`Notes/notes_dynamic_memory_and_data_structures.md`](Resources/Notes/notes_dynamic_memory_and_data_structures.md): Σημειώσεις μνήμης και alignment.
* **[Tutorials/](Tutorials/)**:
  - [`tutorial_01_valgrind_and_dynamic_memory_debugging.md`](Tutorials/tutorial_01_valgrind_and_dynamic_memory_debugging.md): Εντοπισμός memory leaks και segmentation faults με Valgrind.
  - [`tutorial_02_file_streams_and_binary_io.md`](Tutorials/tutorial_02_file_streams_and_binary_io.md): Οδηγός δυαδικών ροών και αρχείων τυχαίας προσπέλασης.

---

## Μεταγλώττιση και Εκτέλεση Παραδειγμάτων

Για τη μεταγλώττιση οποιουδήποτε παραδείγματος με τον μεταγλωττιστή GCC:

```bash
cd Examples

# Μεταγλώττιση με αυστηρούς ελέγχους προτύπου C11
gcc -Wall -Wextra -pedantic -std=c11 01_dynamic_memory_allocation.c -o dynamic_alloc
./dynamic_alloc

# Έλεγχος διαρροών μνήμης με Valgrind
valgrind --leak-check=full ./dynamic_alloc
```
