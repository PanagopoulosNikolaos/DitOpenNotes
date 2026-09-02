/*
 * Exercise 14: Functions and Pointers
 */

#include <stdio.h>

/**
 * Swaps two integers in-place via pointer indirection.
 *
 * Args:
 *     a (int*): Pointer to first integer operand.
 *     b (int*): Pointer to second integer operand.
 *
 * Returns:
 *     void: Modifies referenced values directly in caller scope.
 */
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

/**
 * Demonstrates pass-by-reference simulation in C using pointers.
 *
 * Args:
 *     None.
 *
 * Returns:
 *     int: Exit status code 0 on successful execution.
 */
int main(void) {
    int x = 5;
    int y = 10;

    printf("Before swap: x = %d, y = %d\n", x, y);
    // Passes memory addresses to permit in-place mutation.
    swap(&x, &y);
    printf("After swap: x = %d, y = %d\n", x, y);

    return 0;
}
