# Παραδείγματα: Συγχρονισμός με Mutex και POSIX Semaphores

## Παράδειγμα 1: Υλοποίηση Φραγμού Συγχρονισμού (Thread Barrier)

### Περιγραφή:
Ένας φραγμός (Barrier) εξαναγκάζει $N$ νήματα να αναμείνουν μέχρι όλα να φτάσουν στο ίδιο σημείο εκτέλεσης πριν επιτραπεί σε οποιοδήποτε να συνεχίσει.

### Υλοποίηση σε C με Mutex και Condition Variable:
```c
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

typedef struct {
    pthread_mutex_t mutex;
    pthread_cond_t cond;
    int threshold;
    int count;
} barrier_t;

void barrier_init(barrier_t *b, int count) {
    b->threshold = count;
    b->count = 0;
    pthread_mutex_init(&b->mutex, NULL);
    pthread_cond_init(&b->cond, NULL);
}

void barrier_wait(barrier_t *b) {
    pthread_mutex_lock(&b->mutex);
    b->count++;
    if (b->count >= b->threshold) {
        b->count = 0; // Επαναφορά για επόμενη χρήση
        pthread_cond_broadcast(&b->cond); // Αφύπνιση όλων των νημάτων
    } else {
        pthread_cond_wait(&b->cond, &b->mutex);
    }
    pthread_mutex_unlock(&b->mutex);
}

void barrier_destroy(barrier_t *b) {
    pthread_mutex_destroy(&b->mutex);
    pthread_cond_destroy(&b->cond);
}

barrier_t my_barrier;

void* worker(void* arg) {
    long id = (long)arg;
    printf("[Nhma %ld] Ektelesi protis fasis...\n", id);
    sleep(1 + (id % 2)); // Διαφορετικός χρόνος εκτέλεσης

    printf("[Nhma %ld] Eftasa ston fragmo. Perimenw toys alloys...\n", id);
    barrier_wait(&my_barrier);

    printf("[Nhma %ld] Perasa ton fragmo! Ektelesi deuteris fasis...\n", id);
    return NULL;
}

int main() {
    int num_threads = 4;
    pthread_t threads[4];
    barrier_init(&my_barrier, num_threads);

    for (long i = 0; i < num_threads; i++) {
        pthread_create(&threads[i], NULL, worker, (void*)i);
    }

    for (int i = 0; i < num_threads; i++) {
        pthread_join(threads[i], NULL);
    }

    barrier_destroy(&my_barrier);
    printf("[Main] Oloi oi workers oloklirosan.\n");
    return 0;
}
```

