/*
 * -----------------------------------------------------------------------------
 *
 *  Exercise 14: Functions and Pointers (Call by Reference)
 *
 *  Task:
 *  Write a C program that uses a function to swap the values of two
 *  integer variables. The function should take pointers to the variables
 *  as arguments.
 *
 *  Instructions:
 *  1. Include the stdio.h library.
 *  2. Define a function `swap` that takes two integer pointers as arguments
 *     and swaps the values they point to.
 *  3. In the main function, declare and initialize two integer variables.
 *  4. Print their values before the swap.
 *  5. Call the `swap` function with the addresses of the two variables.
 *  6. Print their values after the swap to verify the change.
 *
 * -----------------------------------------------------------------------------
 */

#include <stdio.h>

// Function to swap two integers using pointers
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int num1 = 5;
    int num2 = 10;

    // Print the values before swapping
    printf("Before swap: num1 = %d, num2 = %d\n", num1, num2);

    // Call the swap function with the addresses of the variables
    swap(&num1, &num2);

    // Print the values after swapping
    printf("After swap: num1 = %d, num2 = %d\n", num1, num2);

    return 0;
}
