/*
 * -----------------------------------------------------------------------------
 *
 *  Exercise 5: Control Flow (if-else)
 *
 *  Task:
 *  Write a C program that checks if a given number is even or odd.
 *
 *  Instructions:
 *  1. Include the stdio.h library.
 *  2. In the main function, declare an integer variable `number`.
 *  3. Prompt the user to enter an integer.
 *  4. Read the user's input and store it in the `number` variable.
 *  5. Use an if-else statement to check if the number is divisible by 2.
 *  6. Print a message indicating whether the number is even or odd.
 *
 * -----------------------------------------------------------------------------
 */

#include <stdio.h>

int main() {
    // Declare an integer variable
    int number;

    // Prompt the user to enter a number
    printf("Enter an integer: ");
    scanf("%d", &number);

    // Check if the number is even or odd
    if (number % 2 == 0) {
        printf("%d is an even number.\n", number);
    } else {
        printf("%d is an odd number.\n", number);
    }

    return 0;
}
