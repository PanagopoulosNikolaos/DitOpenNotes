#include <stdio.h>
#include <string.h>

// Define a structure named Item (same as Exercise 18)
struct Item {
    int item_id;
    char name[50];
    int quantity;
};

int main() {
    struct Item items[] = {
        {1, "Keyboard", 100},
        {2, "Mouse", 150},
        {3, "Monitor", 50},
        {4, "Webcam", 75}
    };
    int num_items = sizeof(items) / sizeof(struct Item);

    FILE *fp = fopen("items.dat", "wb");
    if (fp == NULL) {
        perror("Error opening items.dat for writing");
        return 1;
    }

    fwrite(items, sizeof(struct Item), num_items, fp);
    fclose(fp);

    printf("%d items written to items.dat successfully.\n", num_items);
    printf("You can now run exercise_18_file_handling.c to update records.\n");

    return 0;
}
