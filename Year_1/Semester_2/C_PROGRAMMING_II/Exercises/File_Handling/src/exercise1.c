/*
Exercise 1: Write to a file

Problem:
Write a C program that opens a file named "data1.txt" in write mode.
Write the string "Hello, C File Handling!" into this file.
After writing, close the file.
*/
#include <string.h>
#include <stdio.h>

int main() {
    FILE *file = fopen("data1.txt", "w");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }
    const char *message = "Hello, C File Handling!";
    size_t message_length = strlen(message);
    size_t written = fwrite(message, sizeof(char), message_length, file);
    if (written != message_length) {
        perror("Error writing to file");
        fclose(file);
        return 1;
    }
    fclose(file);
    // Your code here
    return 0;
}
