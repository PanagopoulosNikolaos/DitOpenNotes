/*
 * -----------------------------------------------------------------------------
 *
 *  Exercise 12: Strings
 *
 *  Task:
 *  Write a C program that asks the user for their name and then prints a
 *  greeting message including their name.
 *
 *  Instructions:
 *  1. Include the stdio.h library.
 *  2. In the main function, declare a character array (string) to store the
 *     user's name.
 *  3. Prompt the user to enter their name.
 *  4. Use scanf to read the name.
 *  5. Print a greeting message that includes the entered name.
 *
 * -----------------------------------------------------------------------------
 */

#include <stdio.h>

/**
 * Demonstrates string input and output in C.
 *
 * Args:
 *     None.
 *
 * Returns:
 *     int: Exit status code 0 on successful execution.
 */
int main(void) {
    char name[50];

    printf("Enter your name: ");
    // Limits input to 49 characters to ensure null terminator fits safely.
    if (scanf("%49s", name) != 1) {
        return 1;
    }

    printf("Hello, %s! Welcome to C programming.\n", name);

    return 0;
}
