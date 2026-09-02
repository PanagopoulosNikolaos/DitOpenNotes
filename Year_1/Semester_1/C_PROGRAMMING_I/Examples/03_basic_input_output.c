/*
 * Exercise 03: Basic Input and Output
 */

#include <stdio.h>

/**
 * Demonstrates interactive console input and formatted output.
 *
 * Args:
 *     None.
 *
 * Returns:
 *     int: Exit status code 0 on success, 1 on input error.
 */
int main(void) {
    int number;

    printf("Enter an integer: ");
    // Reads formatted integer into allocated stack address.
    if (scanf("%d", &number) != 1) {
        return 1;
    }

    printf("You entered: %d\n", number);
    return 0;
}
