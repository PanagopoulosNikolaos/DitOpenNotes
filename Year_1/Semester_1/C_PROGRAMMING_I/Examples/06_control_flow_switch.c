/*
 * -----------------------------------------------------------------------------
 *
 *  Exercise 6: Control Flow (switch)
 *
 *  Task:
 *  Write a C program that takes a number from 1 to 7 as input and prints
 *  the corresponding day of the week.
 *
 *  Instructions:
 *  1. Include the stdio.h library.
 *  2. In the main function, declare an integer variable `day`.
 *  3. Prompt the user to enter a number between 1 and 7.
 *  4. Read the user's input.
 *  5. Use a switch statement to print the day of the week based on the
 *     input number.
 *  6. Include a default case to handle invalid input.
 *
 * -----------------------------------------------------------------------------
 */

#include <stdio.h>

int main() {
    // Declare an integer variable for the day
    int day;

    // Prompt the user for input
    printf("Enter a number (1-7) for the day of the week: ");
    scanf("%d", &day);

    // Use a switch statement to determine the day
    switch (day) {
        case 1:
            printf("Sunday\n");
            break;
        case 2:
            printf("Monday\n");
            break;
        case 3:
            printf("Tuesday\n");
            break;
        case 4:
            printf("Wednesday\n");
            break;
        case 5:
            printf("Thursday\n");
            break;
        case 6:
            printf("Friday\n");
            break;
        case 7:
            printf("Saturday\n");
            break;
        default:
            printf("Invalid input. Please enter a number between 1 and 7.\n");
            break;
    }

    return 0;
}