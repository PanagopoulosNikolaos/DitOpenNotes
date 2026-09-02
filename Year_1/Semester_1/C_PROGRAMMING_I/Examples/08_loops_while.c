/*
 * Exercise 08: While Loops
 */

#include <stdio.h>

/**
 * Prints numbers from 1 to 10 sequentially using a while loop.
 *
 * Args:
 *     None.
 *
 * Returns:
 *     int: Exit status code 0 on successful execution.
 */
int main(void) {
    int counter = 1;

    // Evaluates loop condition prior to each iteration.
    while (counter <= 10) {
        printf("%d ", counter);
        ++counter;
    }
    printf("\n");

    return 0;
}
