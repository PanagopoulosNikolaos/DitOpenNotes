/*
 * Exercise 05: Control Flow (if-else)
 */

#include <stdio.h>

/**
 * Evaluates whether an input integer is positive, negative, or zero.
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
    if (scanf("%d", &number) != 1) {
        return 1;
    }

    // Evaluates numeric sign via conditional branching.
    if (number > 0) {
        printf("%d is positive.\n", number);
    } else if (number < 0) {
        printf("%d is negative.\n", number);
    } else {
        printf("The number is zero.\n");
    }

    return 0;
}
