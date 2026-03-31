#include <stdio.h>

int main() {
    char sentence[100];
    FILE *fptr;

    printf("Enter a sentence: ");
    fgets(sentence, sizeof(sentence), stdin);

    fptr = fopen("sentence.txt", "w");
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

    fgets(sentence, sizeof(sentence), fptr);
    printf("\nFrom file: %s", sentence);
    fclose(fptr);

    return 0;
}
