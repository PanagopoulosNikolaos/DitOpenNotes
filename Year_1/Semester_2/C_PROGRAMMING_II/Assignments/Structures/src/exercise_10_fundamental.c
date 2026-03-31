#include <stdio.h>
#include <stdlib.h> // Required for malloc, free, and size_t

/*
 * Exercise 10: Structures with Flexible Array Members (C99)
 *
 * Objective:
 * Define a structure 'DynamicArray' with an integer 'size' and a flexible array member 'data'.
 * Dynamically allocate memory for the structure and its array, populate it,
 * and print the elements.
 */

// Define a structure with a Flexible Array Member (FAM)
// FAM allows for variable-length arrays as the last member of a struct
// This is a C99 feature that enables dynamic sizing at runtime
struct DynamicArray {
    int size;    // Number of elements in the flexible array
    int data[];  // Flexible array member - MUST be the last member
                 // No memory is allocated for this at compile time
};

int main() {
    int num_elements = 5;
    
    // Calculate total memory needed:
    // - Base structure size (excluding the flexible array)
    // - Plus space for the actual array elements
    size_t total_size = sizeof(struct DynamicArray) + num_elements * sizeof(int); // total_size = 4 + 5 * 4 = 24 bytes

    // Allocate memory for both the structure and its flexible array in one block
    // This creates a contiguous memory layout: [size][data[0]][data[1]]...[data[n-1]]
    struct DynamicArray *arr = (struct DynamicArray*)malloc(total_size);// allocates 14 bytes on the 

    // Always check if memory allocation succeeded
    if (arr == NULL) {
        perror("Failed to allocate memory");
        return 1;
    }

    // Initialize the size field to track array length
    arr->size = num_elements;

    // Fill the flexible array with sample data
    printf("Populating array:\n");
    for (int i = 0; i < arr->size; i++) {
        arr->data[i] = (i + 1) * 10;  // Store values: 10, 20, 30, 40, 50
        printf("data[%d] = %d\n", i, arr->data[i]);
    }

    // Display all elements stored in the dynamic array
    printf("\nElements in DynamicArray:\n");
    for (int i = 0; i < arr->size; i++) {
        printf("%d ", arr->data[i]);
    }
    printf("\n");

    // Free allocated memory
    free(arr);

    return 0;
}
