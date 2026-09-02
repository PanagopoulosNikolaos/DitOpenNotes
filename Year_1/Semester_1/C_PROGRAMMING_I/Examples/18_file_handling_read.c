/*
 * Exercise 18: File Handling (Read)
 */

#include <stdio.h>

/**
 * Reads and prints text lines from an existing file.
 *
 * Args:
 *     None.
 *
 * Returns:
 *     int: Exit status code 0 on success, 1 on file error.
 */
int main(void) {
    char buffer[100];

    // Opens file stream in read mode.
    FILE *fptr = fopen("example.txt", "r");
    if (fptr == NULL) {
        printf("Error opening file for reading.\n");
        return 1;
    }

    // Reads line up to buffer capacity.
    if (fgets(buffer, sizeof(buffer), fptr) != NULL) {
        printf("Read from file: %s", buffer);
    }
    fclose(fptr);

    return 0;
}
