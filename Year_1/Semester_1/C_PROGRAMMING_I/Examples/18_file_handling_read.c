/*
 * -----------------------------------------------------------------------------
 *
 *  Exercise 18: File Handling (Reading from a File)
 *
 *  Task:
 *  Write a C program that reads the content of the file "example.txt"
 *  (created in the previous exercise) and displays it on the console.
 *
 *  Instructions:
 *  1. Include the stdio.h library.
 *  2. In the main function, declare a file pointer and a character array to
 *     store the file content.
 *  3. Open the file "example.txt" in read mode ("r").
 *  4. Check if the file was opened successfully.
 *  5. Use fgets to read the content of the file line by line and print it
 *     to the console.
 *  6. Close the file.
 *
 * -----------------------------------------------------------------------------
 */

#include <stdio.h>

int main() {
    // Declare a file pointer and a buffer to read the file content
    FILE *filePtr;
    char buffer[255];

    // Open the file in read mode
    filePtr = fopen("example.txt", "r");

    // Check if the file was opened successfully
    if (filePtr == NULL) {
        printf("Error opening file! Make sure 'example.txt' exists.\n");
        return 1; // Indicate an error
    }

    // Read and display the file content
    printf("Content of 'example.txt':\n");
    while (fgets(buffer, sizeof(buffer), filePtr) != NULL) {
        printf("%s", buffer);
    }

    // Close the file
    fclose(filePtr);

    return 0;
}
