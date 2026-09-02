/*
 * Exercise 11: Arrays
 */

#include <stdio.h>

/**
 * Demonstrates array initialization and index-based element access.
 *
 * Args:
 *     None.
 *
 * Returns:
 *     int: Exit status code 0 on successful execution.
 */
int main(void) {
    // Allocates contiguous storage for five integer elements.
    int numbers[5] = {10, 20, 30, 40, 50};

    // Traverses elements using zero-indexed offset.
    for (int i = 0; i < 5; ++i) {
        printf("Element at index %d: %d\n", i, numbers[i]);
    }

    return 0;
}
