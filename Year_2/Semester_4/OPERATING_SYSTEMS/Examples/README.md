# Παραδείγματα Προγραμμάτων C & POSIX API

## Περίληψη Καταλόγου
Πλήρως λειτουργικά και μεταγλωττίσιμα προγράμματα σε C που επιδεικνύουν τις θεμελιώδεις κλήσεις συστήματος POSIX για διεργασίες, νήματα, συγχρονισμό και διαδιεργασιακή επικοινωνία.

## Περιεχόμενα Καταλόγου
- [process_creation_fork_exec.c](process_creation_fork_exec.c) — Δημιουργία διεργασιών με fork(), αντικατάσταση εικόνας με execvp(), και αναμονή με waitpid().
- [posix_threads_and_mutex.c](posix_threads_and_mutex.c) — Πολυνηματικός προγραμματισμός (pthreads) με κλειδώματα mutex για αποτροπή race conditions.
- [producer_consumer_semaphores.c](producer_consumer_semaphores.c) — Επίλυση προβλήματος παραγωγού-καταναλωτή με χρήση POSIX σηματοφορέων (sem_t).
- [named_pipe_ipc.c](named_pipe_ipc.c) — Διαδιεργασιακή επικοινωνία (IPC) μεταξύ γονέα και παιδιού μέσω ανώνυμης σωλήνωσης (pipe).
