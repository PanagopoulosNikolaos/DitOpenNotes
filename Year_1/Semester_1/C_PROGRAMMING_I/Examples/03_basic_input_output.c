/*
 * -----------------------------------------------------------------------------
 *
 *  Exercise 3: Basic Input and Output
 *
 *  Task:
 *  Write a C program that prompts the user to enter their age and then
 *  displays the entered age back to them.
 *
 *  Instructions:
 *  1. Include the stdio.h library.
 *  2. In the main function, declare an integer variable `age`.
 *  3. Use printf to ask the user to enter their age.
 *  4. Use scanf to read the integer value entered by the user and store it
 *     in the `age` variable.
 *  5. Use printf to display the user's age with a descriptive message.
 *
 * -----------------------------------------------------------------------------
 */

#include <stdio.h>

int main() {
    // Declare an integer variable to store the user's age
    int age;

    // Prompt the user to enter their age
    printf("Enter your age: ");

    // Read the integer input from the user
    scanf("%d", &age);

    // Display the age entered by the user
    printf("You are %d years old.\n", age);

    return 0;
}