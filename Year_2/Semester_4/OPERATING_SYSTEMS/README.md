# Λειτουργικά Συστήματα (402)

## Επισκόπηση Μαθήματος
Το μάθημα καλύπτει τις θεμελιώδεις έννοιες, τις αρχιτεκτονικές και τις τεχνικές υλοποίησης των σύγχρονων λειτουργικών συστημάτων. Εξετάζονται οι κλήσεις συστήματος POSIX, η διαχείριση και ο προγραμματισμός διεργασιών και νημάτων (CPU scheduling), ο συγχρονισμός και η αποτροπή αδιεξόδων (deadlocks), η φυσική και εικονική διαχείριση μνήμης (σελιδοποίηση, αλγόριθμοι αντικατάστασης σελίδων), η υλοποίηση συστημάτων αρχείων (inodes, FCB) και η μαζική αποθήκευση/εικονικοποίηση.

---

## Γενικές Πληροφορίες
- **Κωδικός Μαθήματος:** 402
- **Εξάμηνο:** 4ο (Εαρινό)
- **ECTS:** 6
- **Τύπος:** Υποχρεωτικό

---

## Δομή Καταλόγου

* [Assignments/](Assignments/) — Εργαστηριακές ασκήσεις προγραμματισμού συστήματος σε γλώσσα C (κλήσεις συστήματος, διαχείριση διεργασιών, POSIX pipes και signals).
* [Examples/](Examples/) — Μεταγλωττίσιμα προγράμματα επίδειξης σε C:
  * `process_creation_fork_exec.c` — Δημιουργία και παρακολούθηση διεργασιών με `fork()`, `execvp()`, `waitpid()`.
  * `posix_threads_and_mutex.c` — Πολυνηματικός προγραμματισμός με pthreads και κλειδώματα mutex.
  * `producer_consumer_semaphores.c` — Επίλυση του προβλήματος παραγωγού-καταναλωτή με σηματοφορείς (semaphores).
  * `named_pipe_ipc.c` — Διαδιεργασιακή επικοινωνία (IPC) μέσω ανώνυμων σωληνώσεων (pipes).
* [Exams/](Exams/) — Παλαιότερα θέματα εξετάσεων (Combined Past Exam 2023) και διαγωνίσματα προσομοίωσης με λύσεις.
* [Exercises/](Exercises/) — Λυμένες ασκήσεις δρομολόγησης CPU (FCFS, SJF, SRTF, Round Robin), ανάλυσης αδιεξόδων (Τραπεζίτης) και αντικατάστασης σελίδων (FIFO, LRU, Optimal).
* [Lectures/](Lectures/) — Ολοκληρωμένες σημειώσεις διαλέξεων (Διαλέξεις 01 έως 08):
  * [Διάλεξη 1: Εισαγωγή στα Λειτουργικά Συστήματα και Δομές Πυρήνα](Lectures/lecture_01_introduction_to_operating_systems.md)
  * [Διάλεξη 2: Διαχείριση Διεργασιών, Νήματα και Δρομολόγηση CPU](Lectures/lecture_02_processes_threads_and_cpu_scheduling.md)
  * [Διάλεξη 3: Συγχρονισμός Διεργασιών και Αδιέξοδα (Deadlocks)](Lectures/lecture_03_process_synchronization_and_deadlocks.md)
  * [Διάλεξη 4: Διαχείριση Μνήμης και Εικονική Μνήμη](Lectures/lecture_04_memory_management_and_virtual_memory.md)
  * [Διάλεξη 5: Διεπαφή Συστήματος Αρχείων και Αποθήκευση](Lectures/lecture_05_storage_and_file_system_interface.md)
  * [Διάλεξη 6: Υλοποίηση Συστημάτων Αρχείων και Εσωτερικές Δομές](Lectures/lecture_06_file_system_implementation_and_internals.md)
  * [Διάλεξη 7: Μαζική Αποθήκευση, Συστήματα Ε/Ε και Δρομολόγηση Δίσκου](Lectures/lecture_07_mass_storage_io_systems_and_disk_scheduling.md)
  * [Διάλεξη 8: Προστασία, Ασφάλεια και Εικονικοποίηση](Lectures/lecture_08_protection_security_and_virtualization.md)
* [Projects/](Projects/) — Συνθετικά θέματα υλοποίησης λειτουργικού συστήματος (π.χ. ανάπτυξη απλού shell, διαχείριση μνήμης).
* [Resources/](Resources/) — Προτεινόμενη βιβλιογραφία (Silberschatz, Tanenbaum), εννοιολογικοί χάρτες και οδηγοί κλήσεων συστήματος POSIX.
* [Tutorials/](Tutorials/) — Οδηγοί χρήσης εργαλείων μεταγλώττισης (GCC, Makefiles, GDB) και ανάλυσης μνήμης (Valgrind).