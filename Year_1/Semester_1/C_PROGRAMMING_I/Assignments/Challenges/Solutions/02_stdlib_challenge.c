#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/**
 * Generates and displays a pseudo-random integer in range [1, 100].
 *
 * Args:
 *     None.
 *
 * Returns:
 *     int: Exit status code 0 on successful execution.
 */
int main(void) {
    // Seeds random number generator with current UNIX timestamp.
    srand((unsigned int)time(NULL));

    // Constrains random value to desired range [1, 100].
    int random_number = (rand() % 100) + 1;
    printf("Random number: %d\n", random_number);

    return 0;
}
