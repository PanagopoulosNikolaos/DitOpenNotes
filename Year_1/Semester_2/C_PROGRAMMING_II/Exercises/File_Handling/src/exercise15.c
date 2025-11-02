// Exercise 5: Count Lines in a File
// Problem: Write a C program to count the total number of lines in "greeting.txt".
// A simple way is to count newline characters.

#include <stdio.h>
#include <stdlib.h>

int main(){
    int character;
    int linesCount = 0;
    int isEmpty = 0;
    FILE *file = fopen("greeting.txt", "r");
    if (file == NULL) {
        perror("Error opening file");
        return EXIT_FAILURE;
    }
    while ((character = fgetc(file)) != EOF){
        if (character == '\n'){
            linesCount++;
        }
        if (linesCount == 0 && character == EOF){
            isEmpty = 1;
        }
       
    }
    fclose(file);
    if (isEmpty){
        printf("The file is empty.\n");
    } else {
        printf("Total number of lines in the file: %d\n", linesCount);
    }
    return 0;
}



