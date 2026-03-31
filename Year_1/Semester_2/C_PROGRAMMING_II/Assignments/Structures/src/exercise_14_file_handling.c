#include <stdio.h>
#include <stdlib.h> // Required for malloc, free

/*
 * Exercise 14: Reading Multiple Structures from a File (Binary)
 *
 * Objective:
 * Using the 'Student' structure from Exercise 13, read all student records
 * from the binary file created in Exercise 13 and print their contents.
 */

// Define a structure named Student (same as Exercise 13)
struct Student {
    int id;
    char name[50];
    char grade;
};

int main() {
    // Open the file in binary read mode
    FILE *fp = fopen("students.dat", "rb");
    if (fp == NULL) {
        perror("Error opening file");
        return 1;
    }

    // Determine the number of records in the file
    fseek(fp, 0, SEEK_END);// Move to the end of the file
    long file_size = ftell(fp);// Get the current position (end of file)
    rewind(fp); // Go back to the beginning of the file

    int num_students = file_size / sizeof(struct Student);

    // Allocate memory to hold all student records
    struct Student *students = (struct Student*)malloc(num_students * sizeof(struct Student));
    if (students == NULL) {
        perror("Error allocating memory");
        fclose(fp);
        return 1;
    }

    // Read all student records from the file
    fread(students, sizeof(struct Student), num_students, fp);

    // Close the file
    fclose(fp);

    // Print the read data
    printf("Student data read from file:\n");
    for (int i = 0; i < num_students; i++) {
        printf("ID: %d, Name: %s, Grade: %c\n", students[i].id, students[i].name, students[i].grade);
    }

    // Free allocated memory
    free(students);

    return 0;
}
