/*
 * Exercise 16: Unions
 */

#include <stdio.h>
#include <string.h>

/**
 * Represents memory-shared multi-type data container.
 */
union Data {
    int i;
    float f;
    char str[20];
};

/**
 * Demonstrates memory sharing and member overwrite in C unions.
 *
 * Args:
 *     None.
 *
 * Returns:
 *     int: Exit status code 0 on successful execution.
 */
int main(void) {
    union Data data;

    // Writes integer member and prints value.
    data.i = 10;
    printf("data.i: %d\n", data.i);

    // Overwrites memory with float value.
    data.f = 220.5f;
    printf("data.f: %.2f\n", data.f);

    // Overwrites memory with string.
    strncpy(data.str, "C Programming", sizeof(data.str) - 1);
    data.str[sizeof(data.str) - 1] = '\0';
    printf("data.str: %s\n", data.str);

    return 0;
}
