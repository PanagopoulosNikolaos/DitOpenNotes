# Εργαστηριακός Οδηγός 1: Σενάρια Φλοιού Bash και Κλήσεις Συστήματος Διεργασιών σε C

## 1. Σκοπός Εργαστηρίου
Εξοικείωση με τη συγγραφή σεναρίων κελύφους (Bash scripts), τη διοχέτευση σημάτων (pipes, redirection) και τη δημιουργία διεργασιών μέσω των κλήσεων συστήματος `fork()`, `execvp()`, και `waitpid()` στη γλώσσα C.

---

## 2. Σενάρια Bash: Αυτοματοποίηση και Φίλτρα
Δημιουργήστε το αρχείο `analyze_logs.sh`:
```bash
#!/bin/bash

LOGFILE="/var/log/syslog"
OUTPUT="error_report.txt"

echo "=== Euresi sfalmaton sto $LOGFILE ===" > "$OUTPUT"
grep -i "error" "$LOGFILE" | awk '{print $1, $2, $3, $5, substr($0, index($0,$6))}' >> "$OUTPUT"

TOTAL_ERRORS=$(grep -c -i "error" "$LOGFILE")
echo "Synolo sfalmaton: $TOTAL_ERRORS" >> "$OUTPUT"

echo "H anafora dimiourgithike sto arxeio $OUTPUT"
```

---

## 3. Κλήσεις Συστήματος σε C: Δημιουργία και Συγχρονισμός Διεργασιών

### Πρόγραμμα `process_tree.c`:
```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    pid_t pid = fork();

    if (pid < 0) {
        perror("Apotyxia fork");
        exit(EXIT_FAILURE);
    } else if (pid == 0) {
        // Κώδικας Παιδιού
        printf("[Paidi] PID: %d | Parent PID: %d\n", getpid(), getppid());
        char *args[] = {"ls", "-l", "/usr/bin", NULL};
        execvp(args[0], args);
        perror("Apotyxia execvp");
        exit(EXIT_FAILURE);
    } else {
        // Κώδικας Γονέα
        printf("[Goneas] PID: %d | Dhmiourghthike to paidi me PID: %d\n", getpid(), pid);
        int status;
        waitpid(pid, &status, 0);
        if (WIFEXITED(status)) {
            printf("[Goneas] To paidi termatise kanonika me exit code: %d\n", WEXITSTATUS(status));
        }
    }

    return 0;
}
```

### Μεταγλώττιση και Εκτέλεση:
```bash
gcc -Wall -Wextra process_tree.c -o process_tree
./process_tree
```

