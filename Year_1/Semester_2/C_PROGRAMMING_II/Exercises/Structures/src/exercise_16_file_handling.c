#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
 * Exercise 16: Reading Records from a File (Text)
 *
 * Objective:
 * Define a structure 'Contact' with 'name', 'phone', and 'email'.
 * Write a program that reads contact information from a text file (e.g., 'contacts.txt')
 * where each line represents a contact, and stores them in an array of 'Contact' structures.
 * Then print the contacts. Assume the format in the file is "Name,Phone,Email".
 */

#define MAX_CONTACTS 10
#define MAX_LINE_LENGTH 256

// Define a structure named Contact
struct Contact {
    char name[50];
    char phone[20];
    char email[50];
};

int main() {
    struct Contact contacts[MAX_CONTACTS];
    int count = 0;
    FILE *fp;
    char line[MAX_LINE_LENGTH];

    fp = fopen("contacts.txt", "r");
    if (fp == NULL) {
        perror("Error opening contacts.txt");
        return 1;
    }

    printf("Reading contacts from contacts.txt:\n");
    while (fgets(line, sizeof(line), fp) != NULL && count < MAX_CONTACTS) {
        // Remove newline character
        line[strcspn(line, "\n")] = 0;

        // Parse the line: Name,Phone,Email
        char *token;
        token = strtok(line, ",");
        if (token != NULL) {
            strcpy(contacts[count].name, token);
        }
        token = strtok(NULL, ",");
        if (token != NULL) {
            strcpy(contacts[count].phone, token);
        }
        token = strtok(NULL, ",");
        if (token != NULL) {
            strcpy(contacts[count].email, token);
        }
        count++;
    }

    fclose(fp);

    printf("\n--- Contact List ---\n");
    for (int i = 0; i < count; i++) {
        printf("Name: %s, Phone: %s, Email: %s\n",
               contacts[i].name, contacts[i].phone, contacts[i].email);
    }

    return 0;
}
