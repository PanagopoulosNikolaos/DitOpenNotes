// Exercise 1: Create and Write to a File
// Problem: Write a C program to create a file named "greeting.txt"
// and write the message "Hello, World from C File Handling!" into it.

#include <stdio.h>
#include <stdlib.h> // For exit()

int main(){
    FILE *file = fopen("greeting.txt", "w"); 
    if (file == NULL){
        perror("Error opening file");
        exit(EXIT_FAILURE);
    }
    fprintf(file, "Hello, World from C File Handling!\n");
    fprintf(file, "This is a second line.\n");
    if (fclose(file) != 0){
        perror("Error closing file");
        exit(EXIT_FAILURE);
    }
        printf("Successfully wrote to greeting.txt\n");

}