/*
 * -----------------------------------------------------------------------------
 *
 *  Exercise 8: Loops (while)
 *
 *  Task:
 *  Write a C program that calculates the sum of all positive integers
 *  entered by the user until the user enters a negative number.
 *
 *  Instructions:
 *  1. Include the stdio.h library.
 *  2. In the main function, initialize a variable `sum` to 0 and a variable
 *     `num` to a positive value.
 *  3. Use a while loop that continues as long as the entered number is not
 *     negative.
 *  4. Inside the loop, prompt the user to enter a number, read it, and if
 *     it's positive, add it to the sum.
 *  5. After the loop terminates, print the total sum.
 *
 * -----------------------------------------------------------------------------
 */

#include <stdio.h>

int main() {
    int num;
    int sum = 0;

    // Prompt the user to enter a number
    printf("Enter a positive integer (or a negative number to quit): ");
    scanf("%d", &num);

    // Loop while the entered number is not negative
    while (num >= 0) {
        sum += num; // Add the number to the sum

        // Prompt for the next number
        printf("Enter another positive integer (or a negative number to quit): ");
        scanf("%d", &num);
    }

    // Print the final sum
    printf("The sum of the positive integers entered is: %d\n", sum);

    return 0;
}
