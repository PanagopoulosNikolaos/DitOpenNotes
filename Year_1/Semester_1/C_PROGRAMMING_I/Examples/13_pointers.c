/*
 * Exercise 13: Pointers
 */

#include <stdio.h>

/**
 * Demonstrates pointer declaration, address retrieval, and dereferencing.
 *
 * Args:
 *     None.
 *
 * Returns:
 *     int: Exit status code 0 on successful execution.
 */
int main(void) {
    int value = 42;
    // Binds pointer to variable address in memory.
    int *ptr = &value;

    printf("Value: %d\n", value);
    printf("Memory address of value: %p\n", (void *)&value);
    printf("Value stored in ptr: %p\n", (void *)ptr);
    // Dereferences pointer to retrieve target value.
    printf("Value pointed to by ptr: %d\n", *ptr);

    return 0;
}
