/*
 * -----------------------------------------------------------------------------
 *
 *  Exercise 2: Variables and Data Types
 *
 *  Task:
 *  Write a C program that declares and initializes variables of different
 *  data types (int, float, double, char) and then prints their values to the
 *  console.
 *
 *  Instructions:
 *  1. Include the stdio.h library.
 *  2. In the main function, declare and initialize the following variables:
 *     - An integer `age` with the value 25.
 *     - A float `height` with the value 1.75.
 *     - A double `pi` with the value 3.14159265359.
 *     - A char `initial` with the value 'J'.
 *  3. Use printf to display the values of these variables with appropriate
 *     labels.
 *
 * -----------------------------------------------------------------------------
 */

#include <stdio.h>

int main() {
    // Declare and initialize an integer variable
    int age = 25;

    // Declare and initialize a float variable
    float height = 1.75;

    // Declare and initialize a double variable
    double pi = 3.14159265359;

    // Declare and initialize a char variable
    char initial = 'J';

    // Print the values of the variables
    printf("Age: %d\n", age);
    printf("Height: %.2f meters\n", height);
    printf("Pi: %lf\n", pi);
    printf("Initial: %c\n", initial);

    return 0;
}
