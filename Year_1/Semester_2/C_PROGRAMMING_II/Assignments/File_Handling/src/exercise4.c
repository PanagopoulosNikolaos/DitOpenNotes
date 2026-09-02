/*
Exercise 4: Read integers from a file

Problem:
Write a C program that opens a file named "data4.txt" in read mode.
The file contains a list of integers, one per line.
Read each integer from the file and print it to the console.
After reading all integers, close the file.
*/
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

int main() {
    // Your code here
    FILE *file = fopen("data4.txt", "r");
    if (file == NULL){
        printf("error opening file");
        return -1;
    }
    int numbers[100];
    int count = 0;
    while (fscanf(file, "%d", &numbers[count]) == 1) {
        count++;
    }
    fclose(file);
    for (int i = 0; i < count; i++) {
        printf("%d\n", numbers[i]);
    }
    return 0;
}
