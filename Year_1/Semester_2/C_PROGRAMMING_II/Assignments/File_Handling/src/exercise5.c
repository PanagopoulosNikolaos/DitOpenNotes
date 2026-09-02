/*
Exercise 5: Write integers to a file

Problem:
Write a C program that opens a file named "data5.txt" in write mode.
Write the integers from 1 to 5, each on a new line, into this file.
After writing, close the file.
*/

#include <stdio.h>

int main() {
    // Your code here
    FILE *file = fopen("data5.txt", "w");
    if (file == NULL){
        printf("error opening the file");
        return -1;
    }
    for (int i = 1; i < 6; i++){
        size_t written = fprintf(file, "%d\n", i);
        if (written < 0){
            printf("error writing to file");
            fclose(file);
            return -1;
        }
    }
    fclose(file);
    return 0;
}
