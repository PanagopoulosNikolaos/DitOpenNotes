#include <stdio.h>
#include <math.h>

/**
 * Computes square root, exponential, and power functions from math.h.
 *
 * Args:
 *     None.
 *
 * Returns:
 *     int: Exit status code 0 on success, 1 on input error.
 */
int main(void) {
    double num;

    printf("Enter a number: ");
    if (scanf("%lf", &num) != 1) {
        return 1;
    }

    // Computes mathematical transformations via libm.
    printf("Square root of %.2f is %.2f\n", num, sqrt(num));
    printf("%.2f raised to the power 2 is %.2f\n", num, pow(num, 2));

    return 0;
}
