/*
 * -----------------------------------------------------------------------------
 *
 *  Exercise 11: Arrays
 *
 *  Task:
 *  Write a C program that initializes an array of 5 integers, calculates
 *  the sum of its elements, and prints the sum.
 *
 *  Instructions:
 *  1. Include the stdio.h library.
 *  2. In the main function, declare and initialize an integer array of size 5.
 *  3. Use a for loop to iterate through the array and calculate the sum of
 *     its elements.
 *  4. Print the final sum.
 *
 * -----------------------------------------------------------------------------
 */

#include <stdio.h>

int main() {
    // Declare and initialize an integer array
    int numbers[5] = {10, 20, 30, 40, 50};
    int sum = 0;

    // Calculate the sum of the array elements
    for (int i = 0; i < 5; i++) {
        sum += numbers[i];
    }

    // Print the sum
    printf("The sum of the array elements is: %d\n", sum);

    return 0;
}
