# Παραδείγματα: Δημιουργία Διεργασιών με fork() και exec() σε C

## Παράδειγμα 1: Δημιουργία Αλυσίδας Διεργασιών και Επικοινωνία με Pipe

### Περιγραφή:
Υλοποίηση προγράμματος C που εκτελεί την ισοδύναμη λειτουργία της εντολής κελύφους:
`cat /etc/passwd | grep -v "nologin" | wc -l`

### Πλήρης Κώδικας C:
```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    int pipefd[2];
    if (pipe(pipefd) == -1) {
        perror("Apotyxia pipe");
        exit(EXIT_FAILURE);
    }

    pid_t pid1 = fork();
    if (pid1 < 0) {
        perror("Apotyxia fork 1");
        exit(EXIT_FAILURE);
    }

    if (pid1 == 0) {
        // Πρώτο Παιδί: Εκτελεί "grep -v nologin /etc/passwd"
        close(pipefd[0]); // Κλείσιμο άκρου ανάγνωσης
        dup2(pipefd[1], STDOUT_FILENO); // Ανακατεύθυνση stdout στο pipe
        close(pipefd[1]);

        char *args[] = {"grep", "-v", "nologin", "/etc/passwd", NULL};
        execvp(args[0], args);
        perror("Apotyxia execvp 1");
        exit(EXIT_FAILURE);
    }

    pid_t pid2 = fork();
    if (pid2 < 0) {
        perror("Apotyxia fork 2");
        exit(EXIT_FAILURE);
    }

    if (pid2 == 0) {
        // Δεύτερο Παιδί: Εκτελεί "wc -l"
        close(pipefd[1]); // Κλείσιμο άκρου εγγραφής
        dup2(pipefd[0], STDIN_FILENO); // Ανακατεύθυνση stdin από το pipe
        close(pipefd[0]);

        char *args[] = {"wc", "-l", NULL};
        execvp(args[0], args);
        perror("Apotyxia execvp 2");
        exit(EXIT_FAILURE);
    }

    // Γονέας: Κλείνει και τα δύο άκρα και περιμένει τα παιδιά
    close(pipefd[0]);
    close(pipefd[1]);

    waitpid(pid1, NULL, 0);
    waitpid(pid2, NULL, 0);

    return 0;
}
```

