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

int main() {
    // Declare a character array to store the name
    char name[50];

    // Prompt the user to enter their name
    printf("Enter your name: ");
    scanf("%s", name);

    // Print a greeting message
    printf("Hello, %s! Welcome to C programming.\n", name);

    return 0;
}
