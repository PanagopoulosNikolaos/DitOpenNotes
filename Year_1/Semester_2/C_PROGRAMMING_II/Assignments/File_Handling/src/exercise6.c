/*
Exercise 6: Count lines in a file

Problem:
Write a C program that opens a file named "data6.txt" in read mode.
Count the number of lines in the file and print the count to the console.
After counting, close the file.
*/

#include <stdio.h>

int main() {
    // Your code here
    FILE *file = fopen("data6.txt", "r");
    if (file == NULL){
        printf("error opening file");
        return -1;
    }
    int count = 0;
    char ch;
    while ((ch = fgetc(file)) != EOF) {
        if (ch == '\n') {
            count++;
        }
    }
    fclose(file);
    // If the file is not empty, add one to count for the last line
    if (count > 0) {
        count++;
    }
    printf("Number of lines: %d\n", count);
    return 0;
}
