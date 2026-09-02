/*
 * Exercise 10: Functions
 */

#include <stdio.h>

/**
 * Finds the maximum of two given integers.
 *
 * Args:
 *     a (int): First operand.
 *     b (int): Second operand.
 *
 * Returns:
 *     int: The greater of the two integers.
 */
int findMax(int a, int b) {
    return (a > b) ? a : b;
}

/**
 * Prompts user for two numbers and prints their maximum.
 *
 * Args:
 *     None.
 *
 * Returns:
 *     int: Exit status code 0 on success, 1 on input error.
 */
int main(void) {
    int num1, num2;

    printf("Enter two integers: ");
    if (scanf("%d %d", &num1, &num2) != 2) {
        return 1;
    }

    // Delegates comparison to pure helper function.
    int max_val = findMax(num1, num2);
    printf("The maximum of %d and %d is %d.\n", num1, num2, max_val);

    return 0;
}
