/*
Exercise 10: Error handling for file opening

Problem:
Write a C program that attempts to open a non-existent file named "nonexistent.txt" in read mode.
Implement error handling to check if the file opening was successful.
If the file cannot be opened, print an error message to the console.
If it opens (which it shouldn't), print a success message and close it.
*/

#include <stdio.h>

int main() {
    // Your code here
    FILE *file = fopen("nonexistent.txt", "r");
    if (file == NULL) {
        printf("Error: Could not open the file 'nonexistent.txt'.\n");
    } else {
        printf("File opened successfully.\n");
        fclose(file);
    }

    return 0;
}
