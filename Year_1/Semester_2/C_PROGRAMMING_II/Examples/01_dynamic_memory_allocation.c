/**
 * Demonstrates dynamic 1D and 2D memory allocation in C.
 * Focuses on malloc, calloc, realloc, and leak-free resource deallocation.
 */

#include <stdio.h>
#include <stdlib.h>

/**
 * Creates and initializes a dynamic 1D integer array.
 * Args:
 * size (size_t): The number of integer elements to allocate.
 * Returns:
 * int*: Pointer to allocated memory, or NULL upon allocation failure.
 */
int *createArray(size_t size) {
    if (size == 0) {
        return NULL;
    }
    int *arr = (int *)malloc(size * sizeof(int));
    if (arr == NULL) {
        perror("Allocation failed for 1D array");
        return NULL;
    }
    for (size_t i = 0; i < size; i++) {
        arr[i] = (int)(i * 10);
    }
    return arr;
}

/**
 * Expands an existing array to a new capacity using realloc safely.
 * Args:
 * arr (int*): Existing array pointer.
 * new_size (size_t): New number of elements.
 * Returns:
 * int*: Pointer to reallocated array, or NULL upon failure.
 */
int *expandArray(int *arr, size_t new_size) {
    int *temp = (int *)realloc(arr, new_size * sizeof(int));
    if (temp == NULL) {
        perror("Reallocation failed");
        return NULL;
    }
    return temp;
}

/**
 * Allocates a contiguous 2D integer matrix of dimensions rows x cols.
 * Args:
 * rows (size_t): Number of rows.
 * cols (size_t): Number of columns.
 * Returns:
 * int**: Array of row pointers pointing into dynamically allocated memory.
 */
int **createMatrix(size_t rows, size_t cols) {
    if (rows == 0 || cols == 0) {
        return NULL;
    }
    int **matrix = (int **)malloc(rows * sizeof(int *));
    if (matrix == NULL) {
        return NULL;
    }
    for (size_t i = 0; i < rows; i++) {
        matrix[i] = (int *)calloc(cols, sizeof(int));
        if (matrix[i] == NULL) {
            for (size_t j = 0; j < i; j++) {
                free(matrix[j]);
            }
            free(matrix);
            return NULL;
        }
    }
    return matrix;
}

/**
 * Frees a dynamically allocated 2D matrix.
 * Args:
 * matrix (int**): Array of row pointers.
 * rows (size_t): Number of rows to free.
 * Returns:
 * void: No return value.
 */
void freeMatrix(int **matrix, size_t rows) {
    if (matrix == NULL) {
        return;
    }
    for (size_t i = 0; i < rows; i++) {
        free(matrix[i]);
    }
    free(matrix);
}

int main(void) {
    size_t initial_size = 5;
    int *numbers = createArray(initial_size);
    if (numbers == NULL) {
        return EXIT_FAILURE;
    }

    printf("Initial 1D array:\n");
    for (size_t i = 0; i < initial_size; i++) {
        printf("%d ", numbers[i]);
    }
    printf("\n");

    size_t new_size = 8;
    int *expanded = expandArray(numbers, new_size);
    if (expanded != NULL) {
        numbers = expanded;
        for (size_t i = initial_size; i < new_size; i++) {
            numbers[i] = (int)(i * 10);
        }
        printf("Expanded 1D array:\n");
        for (size_t i = 0; i < new_size; i++) {
            printf("%d ", numbers[i]);
        }
        printf("\n");
    }

    free(numbers);
    numbers = NULL;

    size_t rows = 3;
    size_t cols = 4;
    int **grid = createMatrix(rows, cols);
    if (grid != NULL) {
        printf("\nAllocated 2D Matrix (%zux%zu):\n", rows, cols);
        for (size_t r = 0; r < rows; r++) {
            for (size_t c = 0; c < cols; c++) {
                grid[r][c] = (int)((r + 1) * 10 + c);
                printf("%3d ", grid[r][c]);
            }
            printf("\n");
        }
        freeMatrix(grid, rows);
    }

    return EXIT_SUCCESS;
}
