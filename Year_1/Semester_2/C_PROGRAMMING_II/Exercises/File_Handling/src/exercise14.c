// Exercise 4: Count Characters in a File
// Problem: Write a C program to count the total number of characters
// (including spaces, newlines, etc.) in "greeting.txt".

#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *file = fopen("greeting.txt", "r");
    if (file == NULL){
        perror("Error opening file");
        return EXIT_FAILURE;
    }
    int count = 0;
    char ch;
    while((ch = fgetc(file)) != EOF) {
        count++;
    }
    fclose(file);
    printf("Total number of characters in the file: %d\n", count);
    return 0;
}