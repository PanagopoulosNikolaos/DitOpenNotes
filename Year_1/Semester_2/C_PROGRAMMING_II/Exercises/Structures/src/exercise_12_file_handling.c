#include <stdio.h>
#include <string.h>

/*
 * Exercise 12: Reading a Single Structure from a File (Binary)
 *
 * Objective:
 * Using the 'Product' structure from Exercise 11, read the data from the binary file
 * created in Exercise 11 and print its contents.
 */

// Define a structure named Product (same as Exercise 11)
struct Product {
    int id;
    char name[50];
    float price;
};

int main() {
    // Declare a variable of type struct Product to store read data
    struct Product p_read;

    // Open the file in binary read mode
    FILE *fp = fopen("product.bat", "rb");
    if (fp == NULL) {
        perror("Error opening file");
        return 1;
    }

    // Read the structure from the file
    fread(&p_read, sizeof(struct Product), 1, fp);

    // Close the file
    fclose(fp);

    // Print the read data
    printf("Product data read from file:\n");
    printf("ID: %d\n", p_read.id);
    printf("Name: %s\n", p_read.name);
    printf("Price: %.2f\n", p_read.price);

    return 0;
}
