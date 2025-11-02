/*
Exercise 7: Copy file content

Problem:
Write a C program that opens "data7.txt" for reading and "output7.txt" for writing.
Read the content from "data7.txt" and write it to "output7.txt".
After copying, close both files.
*/

#include <stdio.h>

int main() {
    // Your code here
    FILE *inputFile = fopen("data7.txt", "r");
    if (inputFile == NULL) {
        printf("Error opening input file\n");
        return -1;
    }
    FILE *outputFile = fopen("output7.txt", "w");
    if (outputFile == NULL){
        printf("Error opening output file\n");
        fclose(inputFile);
        return -1;
    }
    char ch;
    while ((ch = fgetc(inputFile))!= EOF){
        fputc(ch, outputFile);

    }
    fclose(inputFile);
    fclose(outputFile);
    printf("File copied successfully\n");
    return 0;
}
