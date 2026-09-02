/*
 * Exercise 04: Arithmetic Operators
 */

#include <stdio.h>

/**
 * Computes arithmetic operations between two operands.
 *
 * Args:
 *     None.
 *
 * Returns:
 *     int: Exit status code 0 on successful execution.
 */
int main(void) {
    int num_a = 10;
    int num_b = 3;

    // Evaluates and outputs standard arithmetic operations.
    printf("Addition: %d + %d = %d\n", num_a, num_b, num_a + num_b);
    printf("Subtraction: %d - %d = %d\n", num_a, num_b, num_a - num_b);
    printf("Multiplication: %d * %d = %d\n", num_a, num_b, num_a * num_b);
    printf("Division: %d / %d = %d\n", num_a, num_b, num_a / num_b);
    printf("Modulus: %d %% %d = %d\n", num_a, num_b, num_a % num_b);

    return 0;
}
