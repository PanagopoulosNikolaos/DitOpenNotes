/*
 * Exercise 19: Preprocessor Directives
 */

#include <stdio.h>

#define PI 3.14159
#define CIRCLE_AREA(r) ((PI) * (r) * (r))

/**
 * Demonstrates preprocessor macro definitions and function-like macros.
 *
 * Args:
 *     None.
 *
 * Returns:
 *     int: Exit status code 0 on successful execution.
 */
int main(void) {
    double radius = 5.0;
    // Expands macro at compile time.
    double area = CIRCLE_AREA(radius);

    printf("Radius: %.2f\n", radius);
    printf("Area of circle: %.4f\n", area);

    return 0;
}
