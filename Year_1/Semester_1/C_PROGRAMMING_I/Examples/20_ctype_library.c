/*
 * Exercise 20: ctype Library
 */

#include <stdio.h>
#include <ctype.h>

/**
 * Demonstrates character classification and case-conversion functions from ctype.h.
 *
 * Args:
 *     None.
 *
 * Returns:
 *     int: Exit status code 0 on successful execution.
 */
int main(void) {
    char ch = 'a';

    // Evaluates character properties using ctype predicates.
    printf("Character: %c\n", ch);
    printf("isalpha: %d\n", isalpha(ch));
    printf("isdigit: %d\n", isdigit(ch));
    printf("toupper: %c\n", toupper(ch));

    return 0;
}
