#include <stdio.h>
#include <string.h>

/*
 * Exercise 15: Appending Structures to a File (Binary)
 *
 * Objective:
 * Define a structure 'Record' with 'id' and 'description'.
 * Write a program that allows the user to input a new record and append it to an existing binary file.
 */

// Define a structure named Record
struct Record {
    int id;
    char description[100];
};

int main() {
    struct Record new_record;

    // Get input from the user
    printf("Enter Record ID: ");
    scanf("%d", &new_record.id);
    printf("Enter Record Description: ");
    // Clear input buffer
    while (getchar() != '\n');
    fgets(new_record.description, sizeof(new_record.description), stdin);
    // Remove trailing newline character if present
    new_record.description[strcspn(new_record.description, "\n")] = 0;

    // Open the file in binary append mode
    FILE *fp = fopen("records.dat", "ab");
    if (fp == NULL) {
        perror("Error opening file");
        return 1;
    }

    // Write the new record to the file
    fwrite(&new_record, sizeof(struct Record), 1, fp);

    // Close the file
    fclose(fp);

    printf("Record appended to records.dat successfully.\n");

    return 0;
}
