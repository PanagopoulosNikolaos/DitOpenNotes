// Exercise 3: Append to a File
// Problem: Write a C program to open "greeting.txt" in append mode ("a")
// and add a new line "Appending a new message!" to the end of the file.

#include <stdio.h>
#include <stdlib.h>

int main(){
    FILE *file = fopen("greeting.txt", "a");
    if (file == NULL) {
        perror("Error opening file");
        return EXIT_FAILURE;
    }
    fprintf(file, "Appending a new message!\n");
    fclose(file);
}