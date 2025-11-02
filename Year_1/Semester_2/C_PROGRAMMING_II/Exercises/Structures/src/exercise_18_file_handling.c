#include <stdio.h>
#include <string.h>

/*
 * Exercise 18: Updating a Specific Record in a Binary File
 *
 * Objective:
 * Define a structure 'Item' with 'item_id', 'name', and 'quantity'.
 * Write a program that reads a binary file of 'Item' records,
 * allows the user to specify an 'item_id' to update,
 * and then modifies the 'quantity' for that item in the file.
 */

// Define a structure named Item
struct Item {
    int item_id;
    char name[50];
    int quantity;
};

int main() {
    FILE *fp;
    struct Item item;
    int target_id;
    int new_quantity;
    int found = 0;

    // Open the file in binary read and write mode
    fp = fopen("items.dat", "rb+");
    if (fp == NULL) {
        perror("Error opening items.dat");
        return 1;
    }

    printf("Enter Item ID to update: ");
    scanf("%d", &target_id);
    printf("Enter new quantity: ");
    scanf("%d", &new_quantity);

    // Read records one by one and update if ID matches
    while (fread(&item, sizeof(struct Item), 1, fp) == 1) {
        if (item.item_id == target_id) {
            item.quantity = new_quantity;
            // Move file pointer back to the beginning of the current record
            fseek(fp, -sizeof(struct Item), SEEK_CUR);
            // Write the updated record
            fwrite(&item, sizeof(struct Item), 1, fp);
            found = 1;
            printf("Item ID %d updated successfully.\n", target_id);
            break;
        }
    }

    if (!found) {
        printf("Item ID %d not found.\n", target_id);
    }

    fclose(fp);

    return 0;
}
