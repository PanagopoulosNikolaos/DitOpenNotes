/*
 * -----------------------------------------------------------------------------
 *
 *  Exercise 13: Pointers
 *
 *  Task:
 *  Write a C program that demonstrates the use of pointers. Declare an
 *  integer variable, a pointer to that variable, and then use the pointer
 *  to change the value of the variable.
 *
 *  Instructions:
 *  1. Include the stdio.h library.
 *  2. In the main function, declare an integer `x` and initialize it.
 *  3. Declare a pointer `ptr` to an integer and assign it the address of `x`.
 *  4. Print the original value of `x`.
 *  5. Use the pointer to modify the value of `x`.
 *  6. Print the new value of `x` to show that it has been changed via the
 *     pointer.
 *
 * -----------------------------------------------------------------------------
 */

#include <stdio.h>

int main() {
    // Declare an integer variable
    int x = 10;

    // Declare a pointer to an integer
    int *ptr;

    // Assign the address of x to the pointer
    ptr = &x;

    // Print the original value of x
    printf("Original value of x: %d\n", x);

    // Modify the value of x using the pointer
    *ptr = 20;

    // Print the new value of x
    printf("New value of x after modification via pointer: %d\n", x);

    return 0;
}