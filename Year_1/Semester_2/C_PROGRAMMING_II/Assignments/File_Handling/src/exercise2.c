/*
Exercise 2: Read from a file

Problem:
Write a C program that opens a file named "data2.txt" in read mode.
Read the content of the file character by character and print it to the console.
After reading, close the file.
*/

#include <stdio.h>

int main() {
    // Your code here
    FILE *file = fopen("data2.txt", "r");
    if (file == NULL){
        printf("Error opening file\n");
        return - 1;
    }
    char ch;
    while ((ch = fgetc(file)) != EOF) {
        putchar(ch);
    }
    if (ferror(file)) {
        printf("Error reading from file\n");
        fclose(file);
        return -1;
    }
    fclose(file);
    return 0;
}
