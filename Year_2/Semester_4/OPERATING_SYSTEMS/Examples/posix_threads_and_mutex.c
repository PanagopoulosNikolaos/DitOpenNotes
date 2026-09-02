/**
 * Demonstrates thread synchronization using POSIX threads and mutual exclusion locks.
 *
 * Spawns multiple worker threads that increment a shared counter concurrently,
 * using a pthread_mutex_t to eliminate race conditions and guarantee mutual exclusion.
 */

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define NUM_THREADS 4
#define ITERATIONS_PER_THREAD 100000

// Shared counter protected by mutex lock.
static long global_counter = 0;
static pthread_mutex_t counter_mutex = PTHREAD_MUTEX_INITIALIZER;

/**
 * Worker thread routine that increments the shared counter.
 *
 * Args:
 *   arg (void*): Unused thread argument pointer.
 *
 * Returns:
 *   void*: Null pointer upon thread termination.
 */
void *workerRoutine(void *arg) {
    (void)arg;

    for (int i = 0; i < ITERATIONS_PER_THREAD; ++i) {
        // Acquires mutex to ensure exclusive access to the shared counter.
        pthread_mutex_lock(&counter_mutex);
        global_counter++;
        pthread_mutex_unlock(&counter_mutex);
    }

    return NULL;
}

int main(void) {
    pthread_t thread_pool[NUM_THREADS];

    printf("Starting %d threads, each incrementing %d times...\n",
           NUM_THREADS, ITERATIONS_PER_THREAD);

    for (int i = 0; i < NUM_THREADS; ++i) {
        if (pthread_create(&thread_pool[i], NULL, workerRoutine, NULL) != 0) {
            perror("pthread_create failed");
            return EXIT_FAILURE;
        }
    }

    for (int i = 0; i < NUM_THREADS; ++i) {
        if (pthread_join(thread_pool[i], NULL) != 0) {
            perror("pthread_join failed");
            return EXIT_FAILURE;
        }
    }

    pthread_mutex_destroy(&counter_mutex);

    long expected_value = (long)NUM_THREADS * ITERATIONS_PER_THREAD;
    printf("Final counter: %ld (Expected: %ld)\n", global_counter, expected_value);

    if (global_counter == expected_value) {
        printf("Success: Shared memory protected with zero race conditions.\n");
    } else {
        printf("Error: Race condition observed.\n");
    }

    return EXIT_SUCCESS;
}

