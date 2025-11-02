#include <stdio.h>
#include <string.h>

/*
 * Exercise 11: Writing a Single Structure to a File (Binary)
 *
 * Objective:
 * Define a structure 'Product' with 'id', 'name', and 'price'.
 * Create a 'Product' variable, populate it, and write it to a binary file.
 */

// Define a structure named Product
struct Product {
    int id;
    char name[50];
    float price;
};

int main() {
    // Declare a variable of type struct Product
    struct Product p1 = {101, "Laptop", 1200.50};

    // Open a file in binary write mode
    FILE *fp = fopen("product.bat", "wb");
    if (fp == NULL) {
        perror("Error opening file");
        return 1;
    }

    // Write the structure to the file
    fwrite(&p1, sizeof(struct Product), 1, fp);

    // Close the file
    fclose(fp);

    printf("Product data written to product.bat successfully.\n");

    return 0;
}
