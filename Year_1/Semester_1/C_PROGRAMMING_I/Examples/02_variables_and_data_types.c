/*
 * Exercise 02: Variables and Data Types
 */

#include <stdio.h>

/**
 * Demonstrates primitive data types and format specifiers in C.
 *
 * Args:
 *     None.
 *
 * Returns:
 *     int: Exit status code 0 on successful execution.
 */
int main(void) {
    // Initializes primitive variables with sample values.
    int integer_var = 10;
    float float_var = 3.14f;
    double double_var = 3.1415926535;
    char char_var = 'A';

    // Prints variable values with corresponding type specifiers.
    printf("Integer: %d\n", integer_var);
    printf("Float: %f\n", float_var);
    printf("Double: %lf\n", double_var);
    printf("Character: %c\n", char_var);

    return 0;
}
