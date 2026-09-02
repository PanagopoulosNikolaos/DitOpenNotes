// Exercise 2: Read from a File
// Problem: Write a C program to read the content of "greeting.txt"
// (created in Exercise 1) and print it to the console.
// Use fgets() to read line by line.
#include <string.h>
#include <stdio.h>
#include <stdlib.h> // For exit()
#define MAX_LINE_LENGTH 256

int main() {
    char lineBuffer[MAX_LINE_LENGTH];// makes a list of size MAX_LINE_LENGTH
    FILE *file = fopen("greeting.txt", "r");
    if (file == NULL){
        perror("Error opening file");
        exit(EXIT_FAILURE);
    }

    printf("Content of greeting.txt:\n");
    printf("------------------------\n");
    while (fgets(lineBuffer, MAX_LINE_LENGTH, file) != NULL) {
        printf("%s", lineBuffer);
    }

    if (ferror(file)) { 
        perror("Error reading file");
        fclose(file);
        return 1;
    }
    if (fclose(file) == EOF) {
        perror("Error closing file");
        return 1;
    }
    return 0;
}