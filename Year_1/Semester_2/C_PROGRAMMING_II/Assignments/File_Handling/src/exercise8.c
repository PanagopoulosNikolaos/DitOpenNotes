/*
Exercise 8: Search for a word in a file

Problem:
Write a C program that opens "data8.txt" for reading.
Search for the word "example" (case-sensitive) in the file.
Print a message indicating if the word was found or not.
After searching, close the file.
*/

#include <stdio.h>
#include <string.h> // You might need this for string operations

int main() {
    // Your code here
    FILE *file = fopen("data8.txt", "r");
    if (file == NULL) {
        printf("Error opening file\n");
        return -1;
    }
    char line[256];
    int found = 0;
    int count_found = 0;
    while (fgets(line, sizeof(line), file) != NULL) {
        if (strstr(line, "example") != NULL) {
            found = 1;
            count_found++;
        }
    }
    fclose(file);
    if (found) {
        printf("The word 'example' was found in the file.%d\n", count_found);
    } else {
        printf("The word 'example' was not found in the file.\n");
    }
    return 0;
}
