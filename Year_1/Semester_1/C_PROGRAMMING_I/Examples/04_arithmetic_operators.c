/*
 * -----------------------------------------------------------------------------
 *
 *  Exercise 4: Arithmetic Operators
 *
 *  Task:
 *  Write a C program that performs basic arithmetic operations (addition,
 *  subtraction, multiplication, division, and modulus) on two integer
 *  numbers and displays the results.
 *
 *  Instructions:
 *  1. Include the stdio.h library.
 *  2. In the main function, declare two integer variables, `a` and `b`, and
 *     initialize them with values (e.g., a = 10, b = 5).
 *  3. Calculate the sum, difference, product, quotient, and remainder of
 *     `a` and `b`.
 *  4. Use printf to display the results of each operation with clear labels.
 *
 * -----------------------------------------------------------------------------
 */

#include <stdio.h>

int main() {
    // Declare and initialize two integer variables
    int a = 10;
    int b = 5;

    // Perform arithmetic operations
    int sum = a + b;
    int difference = a - b;
    int product = a * b;
    int quotient = a / b;
    int remainder = a % b;

    // Display the results
    printf("a = %d, b = %d\n", a, b);
    printf("Sum: %d\n", sum);
    printf("Difference: %d\n", difference);
    printf("Product: %d\n", product);
    printf("Quotient: %d\n", quotient);
    printf("Remainder: %d\n", remainder);

    return 0;
}
