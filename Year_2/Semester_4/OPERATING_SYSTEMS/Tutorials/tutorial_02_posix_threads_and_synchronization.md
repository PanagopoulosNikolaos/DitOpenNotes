# Εργαστηριακός Οδηγός 2: Πολυπλοκότητα Νημάτων POSIX και Συγχρονισμός με Mutex

## 1. Σκοπός Εργαστηρίου
Εκμάθηση της βιβλιοθήκης POSIX Threads (`pthreads`) στη γλώσσα C. Εντοπισμός συνθηκών ανταγωνισμού (race conditions) σε κοινόχρηστες μεταβλητές και επίλυσή τους με χρήση αμοιβαίου αποκλεισμού (`pthread_mutex_t`).

---

## 2. Πρόβλημα Race Condition και Επίλυση με Mutex

### Πηγαίος Κώδικας (`thread_safe_counter.c`):
```c
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define NUM_THREADS 4
#define ITERATIONS 1000000

long long global_counter = 0;
pthread_mutex_t counter_mutex = PTHREAD_MUTEX_INITIALIZER;

void* increment_task(void* arg) {
    (void)arg;
    for (int i = 0; i < ITERATIONS; i++) {
        pthread_mutex_lock(&counter_mutex);
        global_counter++;
        pthread_mutex_unlock(&counter_mutex);
    }
    return NULL;
}

int main() {
    pthread_t threads[NUM_THREADS];

    printf("[Main] Ekinisi %d nhmatwn gia ayksisi kata %d to kathena...\n", 
           NUM_THREADS, ITERATIONS);

    for (int i = 0; i < NUM_THREADS; i++) {
        if (pthread_create(&threads[i], NULL, increment_task, NULL) != 0) {
            perror("Apotyxia pthread_create");
            exit(EXIT_FAILURE);
        }
    }

    for (int i = 0; i < NUM_THREADS; i++) {
        pthread_join(threads[i], NULL);
    }

    pthread_mutex_destroy(&counter_mutex);

    printf("[Main] Anamenomeni timi: %lld\n", (long long)NUM_THREADS * ITERATIONS);
    printf("[Main] Teliki timi metrhti: %lld\n", global_counter);

    return 0;
}
```

### Μεταγλώττιση και Έλεγχος:
```bash
gcc -Wall -Wextra -pthread thread_safe_counter.c -o thread_safe_counter
./thread_safe_counter
```

