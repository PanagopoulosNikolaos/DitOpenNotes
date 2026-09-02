/*
 * Exercise 17: File Handling (Write)
 */

#include <stdio.h>

/**
 * Writes formatted text data into an output file.
 *
 * Args:
 *     None.
 *
 * Returns:
 *     int: Exit status code 0 on success, 1 on file error.
 */
int main(void) {
    // Opens file stream in write mode.
    FILE *fptr = fopen("example.txt", "w");
    if (fptr == NULL) {
        printf("Error opening file for writing.\n");
        return 1;
    }

    // Writes formatted message to stream.
    fprintf(fptr, "Hello, file handling in C!\n");
    // Flushes buffer and releases OS file handle.
    fclose(fptr);

    printf("File written successfully.\n");
    return 0;
}
