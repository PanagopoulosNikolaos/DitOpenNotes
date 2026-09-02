/*
 * Exercise 09: Do-While Loops
 */

#include <stdio.h>

/**
 * Prints numbers from 1 to 10 sequentially using a do-while loop.
 *
 * Args:
 *     None.
 *
 * Returns:
 *     int: Exit status code 0 on successful execution.
 */
int main(void) {
    int counter = 1;

    // Executes body at least once before testing condition.
    do {
        printf("%d ", counter);
        ++counter;
    } while (counter <= 10);
    printf("\n");

    return 0;
}
