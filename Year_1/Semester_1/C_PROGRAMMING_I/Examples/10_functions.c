/*
 * -----------------------------------------------------------------------------
 *
 *  Exercise 10: Functions
 *
 *  Task:
 *  Write a C program that uses a function to find the maximum of two numbers.
 *
 *  Instructions:
 *  1. Include the stdio.h library.
 *  2. Define a function `findMax` that takes two integer arguments and
 *     returns the larger of the two.
 *  3. In the main function, prompt the user to enter two numbers.
 *  4. Call the `findMax` function with the user's input.
 *  5. Print the result returned by the function.
 *
 * -----------------------------------------------------------------------------
 */

#include <stdio.h>

// Function to find the maximum of two integers
int findMax(int a, int b) {
    if (a > b) {
        return a;
    } else {
        return b;
    }
}

int main() {
    int num1, num2;

    // Prompt the user to enter two numbers
    printf("Enter two integers: ");
    scanf("%d %d", &num1, &num2);

    // Call the findMax function and store the result
    int max = findMax(num1, num2);

    // Print the maximum number
    printf("The maximum of %d and %d is %d.\n", num1, num2, max);

    return 0;
}
