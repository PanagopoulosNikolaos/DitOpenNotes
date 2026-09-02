#include <stdio.h>

/**
 * Demonstrates sequential file write followed by read verification.
 *
 * Args:
 *     None.
 *
 * Returns:
 *     int: Exit status code 0 on success, 1 on file error.
 */
int main(void) {
    char sentence[100];

    printf("Enter a sentence: ");
    if (fgets(sentence, sizeof(sentence), stdin) == NULL) {
        return 1;
    }

    FILE *fptr = fopen("sentence.txt", "w");
    if (fptr == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    fprintf(fptr, "%s", sentence);
    fclose(fptr);

    fptr = fopen("sentence.txt", "r");
    if (fptr == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    if (fgets(sentence, sizeof(sentence), fptr) != NULL) {
        printf("\nFrom file: %s", sentence);
    }
    fclose(fptr);

    return 0;
}
