/**
 * Demonstrates safe dynamic memory allocation, reallocation, and deallocation in C.
 */

#include <stdio.h>
#include <stdlib.h>

/**
 * Allocates and initializes a dynamic integer buffer with sequential values.
 * Args:
 *   capacity (size_t): Number of integer elements to allocate.
 * Returns:
 *   int*: Pointer to allocated block, or NULL on allocation failure.
 */
int* createBuffer(size_t capacity) {
    int *buf_ptr = (int *)malloc(capacity * sizeof(int));
    if (buf_ptr == NULL) {
        return NULL; /* Signals allocation failure to caller */
    }

    for (size_t idx = 0; idx < capacity; idx++) {
        buf_ptr[idx] = (int)(idx * 10); /* Populates buffer with initial sequence */
    }

    return buf_ptr;
}

/**
 * Resizes an existing heap buffer while preventing memory leakage on failure.
 * Args:
 *   old_ptr (int*): Existing heap-allocated pointer.
 *   new_capacity (size_t): New number of integer elements.
 * Returns:
 *   int*: Pointer to resized buffer, or NULL if reallocation failed.
 */
int* resizeBuffer(int *old_ptr, size_t new_capacity) {
    int *temp_ptr = (int *)realloc(old_ptr, new_capacity * sizeof(int));
    if (temp_ptr == NULL) {
        free(old_ptr); /* Releases old buffer to prevent leakage before aborting */
        return NULL;
    }
    return temp_ptr;
}

int main(void) {
    size_t initial_cap = 5;
    size_t expanded_cap = 10;

    int *my_buffer = createBuffer(initial_cap);
    if (my_buffer == NULL) {
        fprintf(stderr, "Buffer allocation failed\n");
        return EXIT_FAILURE;
    }

    printf("Initial Buffer Contents:\n");
    for (size_t idx = 0; idx < initial_cap; idx++) {
        printf("Index %zu: %d\n", idx, my_buffer[idx]);
    }

    my_buffer = resizeBuffer(my_buffer, expanded_cap);
    if (my_buffer == NULL) {
        fprintf(stderr, "Reallocation failed\n");
        return EXIT_FAILURE;
    }

    /* Populates new indices */
    for (size_t idx = initial_cap; idx < expanded_cap; idx++) {
        my_buffer[idx] = (int)(idx * 10);
    }

    printf("\nExpanded Buffer Contents:\n");
    for (size_t idx = 0; idx < expanded_cap; idx++) {
        printf("Index %zu: %d\n", idx, my_buffer[idx]);
    }

    free(my_buffer); /* Deallocates memory to maintain clean heap state */
    my_buffer = NULL;

    return EXIT_SUCCESS;
}

