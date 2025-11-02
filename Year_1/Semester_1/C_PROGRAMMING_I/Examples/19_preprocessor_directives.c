/*
 * -----------------------------------------------------------------------------
 *
 *  Exercise 19: Preprocessor Directives
 *
 *  Task:
 *  Write a C program that uses preprocessor directives (#define, #ifdef,
 *  #ifndef, #endif) to define a constant and conditionally compile a
 *  block of code.
 *
 *  Instructions:
 *  1. Include the stdio.h library.
 *  2. Use #define to create a symbolic constant for the value of PI.
 *  3. Use #define to create a macro for calculating the area of a circle.
 *  4. Use #ifdef to check if a certain symbol (e.g., DEBUG) is defined.
 *     If it is, print a debug message.
 *  5. In the main function, use the defined constant and macro.
 *
 * -----------------------------------------------------------------------------
 */

#include <stdio.h>

// Define a constant for PI
#define PI 3.14159

// Define a macro to calculate the area of a circle
#define CIRCLE_AREA(r) (PI * (r) * (r))

// Define a symbol to enable debug messages
#define DEBUG

int main() {
    double radius = 5.0;
    double area;

    // Calculate the area of the circle using the macro
    area = CIRCLE_AREA(radius);

    printf("The area of a circle with radius %.2f is %.2f\n", radius, area);

    // Conditionally compile a debug message
#ifdef DEBUG
    printf("Debug mode is ON.\n");
#endif

#ifndef RELEASE
    printf("This is not a release build.\n");
#endif

    return 0;
}