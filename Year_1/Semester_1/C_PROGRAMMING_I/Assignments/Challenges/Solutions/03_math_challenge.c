#include <stdio.h>
#include <math.h>

int main() {
    double number;
    float float_number;

    printf("Enter a number: ");
    scanf("%lf", &number);

    printf("The square root of %.2lf is %.2lf\n", number, sqrt(number));

    printf("Enter a float number: ");
    scanf("%f", &float_number);

    printf("The rounded value of %.2f is %.0f\n", float_number, round(float_number));

    return 0;
}
