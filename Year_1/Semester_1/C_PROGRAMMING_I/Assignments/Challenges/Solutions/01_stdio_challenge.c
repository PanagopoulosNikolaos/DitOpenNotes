#include <stdio.h>

/**
 * Reads user name and favorite number, then prints a personalized greeting.
 *
 * Args:
 *     None.
 *
 * Returns:
 *     int: Exit status code 0 on successful execution.
 */
int main(void) {
    char name[20];
    int number;

    printf("Enter your name: ");
    // Reads up to 19 characters into buffer to prevent overflow.
    if (scanf("%19s", name) != 1) {
        return 1;
    }

    printf("Enter your favorite number: ");
    if (scanf("%d", &number) != 1) {
        return 1;
    }

    printf("Hello, %s! Your favorite number is %d.\n", name, number);

    return 0;
}
