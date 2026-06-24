/*
Exercise 3: Append to a file

Problem:
Write a C program that opens a file named "data3.txt" in append mode.
Write the string "Appending new line." to this file.
After writing, close the file.
*/
#include <string.h>
#include <stdio.h>

int main() {
    // Your code here
    FILE *file = fopen("data3.txt", "a");
    if (file == NULL){
        printf("error opening file");
        return -1;
    }
    char *message = "Appending new line.\n";
    size_t message_length = strlen(message);
    size_t written = fwrite(message, sizeof(char), message_length, file);
    if (written != message_length){
        printf("error writing to file\n");
        fclose(file);
        return -1;
    }
    fclose(file);
    return 0;
}
