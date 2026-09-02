/**
 * Solves the bounded-buffer Producer-Consumer problem using POSIX semaphores and mutexes.
 *
 * Coordinates producer and consumer threads accessing a circular buffer,
 * enforcing buffer boundaries and mutual exclusion to prevent data corruption.
 */

#define _DEFAULT_SOURCE

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

#define BUFFER_SIZE 5
#define TOTAL_ITEMS 15

static int circular_buffer[BUFFER_SIZE];
static int in_index = 0;
static int out_index = 0;

static sem_t empty_slots;
static sem_t full_slots;
static pthread_mutex_t buffer_mutex = PTHREAD_MUTEX_INITIALIZER;

/**
 * Producer thread routine generating numerical data into the circular buffer.
 *
 * Args:
 *   arg (void*): Unused thread argument pointer.
 *
 * Returns:
 *   void*: Null pointer upon thread termination.
 */
void *producerRoutine(void *arg) {
    (void)arg;

    for (int i = 1; i <= TOTAL_ITEMS; ++i) {
        // Decrements empty slot count, blocks if buffer is completely full.
        sem_wait(&empty_slots);

        pthread_mutex_lock(&buffer_mutex);
        circular_buffer[in_index] = i;
        printf("[Producer] Produced item %d at buffer index %d\n", i, in_index);
        in_index = (in_index + 1) % BUFFER_SIZE;
        pthread_mutex_unlock(&buffer_mutex);

        // Increments full slot count to notify waiting consumer.
        sem_post(&full_slots);

        usleep(20000);
    }

    return NULL;
}

/**
 * Consumer thread routine extracting numerical data from the circular buffer.
 *
 * Args:
 *   arg (void*): Unused thread argument pointer.
 *
 * Returns:
 *   void*: Null pointer upon thread termination.
 */
void *consumerRoutine(void *arg) {
    (void)arg;

    for (int i = 1; i <= TOTAL_ITEMS; ++i) {
        // Decrements full slot count, blocks if buffer is currently empty.
        sem_wait(&full_slots);

        pthread_mutex_lock(&buffer_mutex);
        int consumed_item = circular_buffer[out_index];
        printf("[Consumer] Consumed item %d from buffer index %d\n", consumed_item, out_index);
        out_index = (out_index + 1) % BUFFER_SIZE;
        pthread_mutex_unlock(&buffer_mutex);

        // Increments empty slot count to notify waiting producer.
        sem_post(&empty_slots);

        usleep(35000);
    }

    return NULL;
}

int main(void) {
    // Initializing counting semaphores: empty starts at BUFFER_SIZE, full starts at 0.
    sem_init(&empty_slots, 0, BUFFER_SIZE);
    sem_init(&full_slots, 0, 0);

    pthread_t producer_thread;
    pthread_t consumer_thread;

    if (pthread_create(&producer_thread, NULL, producerRoutine, NULL) != 0 ||
        pthread_create(&consumer_thread, NULL, consumerRoutine, NULL) != 0) {
        perror("Failed to create worker threads");
        return EXIT_FAILURE;
    }

    pthread_join(producer_thread, NULL);
    pthread_join(consumer_thread, NULL);

    sem_destroy(&empty_slots);
    sem_destroy(&full_slots);
    pthread_mutex_destroy(&buffer_mutex);

    printf("Producer-Consumer execution completed successfully.\n");
    return EXIT_SUCCESS;
}
