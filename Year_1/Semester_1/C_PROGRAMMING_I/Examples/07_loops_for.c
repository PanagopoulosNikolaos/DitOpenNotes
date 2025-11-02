/*
 * -----------------------------------------------------------------------------
 *
 *  Exercise 7: Loops (for)
 *
 *  Task:
 *  Write a C program that prints the first 10 natural numbers using a for
 *  loop.
 *
 *  Instructions:
 *  1. Include the stdio.h library.
 *  2. In the main function, use a for loop to iterate from 1 to 10.
 *  3. Inside the loop, print the value of the loop counter.
 *
 * -----------------------------------------------------------------------------
 */

#include <stdio.h>

int main() {
    // Print the first 10 natural numbers
    printf("The first 10 natural numbers are:\n");

    // Use a for loop to iterate from 1 to 10
    for (int i = 1; i <= 10; i++) {
        printf("%d\n", i);
    }

    return 0;
}
