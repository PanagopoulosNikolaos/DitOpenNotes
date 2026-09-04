/**
 * Writes a sequence of integers to a text file.
 */

#include <stdio.h>

int main(void) {
    FILE *file_ptr = fopen("data5.txt", "w");
    if (file_ptr == NULL) {
        perror("Error opening file");
        return 1;
    }

    for (int val = 1; val <= 5; val++) {
        int written = fprintf(file_ptr, "%d\n", val);
        if (written < 0) {
            perror("Error writing to file");
            fclose(file_ptr);
            return 1;
        }
    }

    fclose(file_ptr);
    return 0;
}
