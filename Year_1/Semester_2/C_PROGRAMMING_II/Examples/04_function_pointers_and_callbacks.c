/**
 * Demonstrates function pointers, callback mechanisms, and standard
 * library sorting callbacks (qsort) in C.
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

/**
 * Predicate function pointer type for integer filtering.
 */
typedef bool (*Predicate)(int);

/**
 * Transformation function pointer type for mapping values.
 */
typedef int (*Transform)(int);

/**
 * Checks if a number is even.
 * Args:
 * n (int): Number to inspect.
 * Returns:
 * bool: true if even, false otherwise.
 */
bool isEven(int n) {
    return (n % 2) == 0;
}

/**
 * Squares an integer value.
 * Args:
 * n (int): Number to square.
 * Returns:
 * int: The squared value.
 */
int square(int n) {
    return n * n;
}

/**
 * Applies a transformation function to each element in an array.
 * Args:
 * arr (int*): Source array.
 * size (size_t): Number of elements.
 * func (Transform): Callback transformation function.
 * Returns:
 * void: Modifies array in place.
 */
void mapArray(int *arr, size_t size, Transform func) {
    if (arr == NULL || func == NULL) {
        return;
    }
    for (size_t i = 0; i < size; i++) {
        arr[i] = func(arr[i]);
    }
}

/**
 * Comparator callback for qsort (ascending order).
 * Args:
 * a (const void*): Pointer to first element.
 * b (const void*): Pointer to second element.
 * Returns:
 * int: Negative if *a < *b, positive if *a > *b, 0 if equal.
 */
int compareAscending(const void *a, const void *b) {
    int val_a = *(const int *)a;
    int val_b = *(const int *)b;
    return (val_a > val_b) - (val_a < val_b);
}

int main(void) {
    int data[] = {7, 2, 9, 4, 1, 8, 3};
    size_t n = sizeof(data) / sizeof(data[0]);

    printf("Original array:\n");
    for (size_t i = 0; i < n; i++) {
        printf("%d ", data[i]);
    }
    printf("\n");

    printf("Filtering even numbers via predicate callback:\n");
    for (size_t i = 0; i < n; i++) {
        if (isEven(data[i])) {
            printf("%d ", data[i]);
        }
    }
    printf("\n");

    printf("Sorting array with qsort and custom comparator callback:\n");
    qsort(data, n, sizeof(int), compareAscending);
    for (size_t i = 0; i < n; i++) {
        printf("%d ", data[i]);
    }
    printf("\n");

    printf("Mapping array elements with square function:\n");
    mapArray(data, n, square);
    for (size_t i = 0; i < n; i++) {
        printf("%d ", data[i]);
    }
    printf("\n");

    return EXIT_SUCCESS;
}
