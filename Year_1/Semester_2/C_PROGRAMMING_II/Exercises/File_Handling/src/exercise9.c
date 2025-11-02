/*
Exercise 9: Read and write mixed data types

Problem:
Write a C program that opens "data9.txt" for reading.
The file contains a name (string) and an age (integer) on separate lines.
Read the name and age from the file and print them to the console.
Then, open "output9.txt" for writing and write the name and age to it.
After processing, close both files.
*/
#include <string.h>

#include <stdio.h>

int main() {
    // Your code here
    FILE *inputFile = fopen("data9.txt", "r");
    if (inputFile == NULL) {
        printf("Error opening input file\n");
        return -1;
    }
    FILE *outputFile = fopen("output9.txt", "w");
    if (outputFile == NULL) {
        printf("Error opening output file\n");
        fclose(inputFile);
        return -1;
    }
    char name[50];
    int age;
    if (fgets(name, sizeof(name), inputFile) != NULL) { // Gets the name from the file
        // Remove newline character from name
        name[strcspn(name, "\n")] = 0;
    }
    if (fscanf(inputFile, "%d", &age) != 1) { // Reads the age from the file
        printf("Error reading age from file\n");
        fclose(inputFile);
        fclose(outputFile);
        return -1;
    }
    printf("Name: %s\n", name);
    printf("Age: %d\n", age);
    fprintf(outputFile, "Name: %s\n", name);
    fprintf(outputFile, "Age: %d\n", age);
    fclose(inputFile);
    return 0;
}
