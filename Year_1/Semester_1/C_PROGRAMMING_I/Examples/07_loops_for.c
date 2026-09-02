/*
 * Exercise 07: For Loops
 */

#include <stdio.h>

/**
 * Prints numbers from 1 to 10 sequentially using a for loop.
 *
 * Args:
 *     None.
 *
 * Returns:
 *     int: Exit status code 0 on successful execution.
 */
int main(void) {
    // Iterates across finite integer interval [1, 10].
    for (int i = 1; i <= 10; ++i) {
        printf("%d ", i);
    }
    printf("\n");

    return 0;
}
