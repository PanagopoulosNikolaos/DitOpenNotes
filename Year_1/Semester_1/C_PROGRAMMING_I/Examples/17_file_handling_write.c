/*
 * -----------------------------------------------------------------------------
 *
 *  Exercise 17: File Handling (Writing to a File)
 *
 *  Task:
 *  Write a C program that creates a file named "example.txt" and writes a
 *  short text message to it.
 *
 *  Instructions:
 *  1. Include the stdio.h library.
 *  2. In the main function, declare a file pointer.
 *  3. Open the file "example.txt" in write mode ("w").
 *  4. Check if the file was opened successfully. If not, print an error
 *     message and exit.
 *  5. Use fprintf to write a string to the file.
 *  6. Close the file using fclose.
 *  7. Print a success message to the console.
 *
 * -----------------------------------------------------------------------------
 */

#include <stdio.h>

int main() {
    // Declare a file pointer
    FILE *filePtr;

    // Open the file in write mode
    filePtr = fopen("example.txt", "w");

    // Check if the file was opened successfully
    if (filePtr == NULL) {
        printf("Error opening file!\n");
        return 1; // Indicate an error
    }

    // Write to the file
    fprintf(filePtr, "This is a sample text written to the file.\n");

    // Close the file
    fclose(filePtr);

    printf("Successfully wrote to the file 'example.txt'.\n");

    return 0;
}
