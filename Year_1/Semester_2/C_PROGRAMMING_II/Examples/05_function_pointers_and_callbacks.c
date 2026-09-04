/**
 * Demonstrates higher-order programming, function pointers, and transform callbacks in C.
 */

#include <stdio.h>
#include <stdlib.h>

/**
 * Type definition for a unary integer mapping function.
 */
typedef int (*TransformFunc)(int);

/**
 * Type definition for a predicate function testing integer conditions.
 */
typedef int (*PredicateFunc)(int);

/**
 * Multiplies an integer by two.
 * Args:
 *   val (int): Input integer.
 * Returns:
 *   int: Product with two.
 */
int doubleValue(int val) {
    return val * 2; /* Transforms integer via scaling */
}

/**
 * Squares an integer value.
 * Args:
 *   val (int): Input integer.
 * Returns:
 *   int: Squared product.
 */
int squareValue(int val) {
    return val * val; /* Computes second power */
}

/**
 * Checks whether an integer is an even number.
 * Args:
 *   val (int): Target integer.
 * Returns:
 *   int: 1 if even, 0 otherwise.
 */
int isEven(int val) {
    return (val % 2 == 0); /* Tests divisibility by two */
}

/**
 * Applies a transform function to every element in an integer array.
 * Args:
 *   dest_arr (int*): Destination output buffer.
 *   src_arr (const int*): Source input buffer.
 *   elem_count (size_t): Total number of elements.
 *   transform_fn (TransformFunc): Callback transform operator.
 */
void applyTransform(int *dest_arr, const int *src_arr, size_t elem_count, TransformFunc transform_fn) {
    if (dest_arr == NULL || src_arr == NULL || transform_fn == NULL) {
        return; /* Guards against null pointer invocations */
    }

    for (size_t idx = 0; idx < elem_count; idx++) {
        dest_arr[idx] = transform_fn(src_arr[idx]); /* Dispatches callback for element transformation */
    }
}

/**
 * Filters source array elements satisfying a predicate into an output buffer.
 * Args:
 *   dest_arr (int*): Destination output buffer.
 *   src_arr (const int*): Source input buffer.
 *   elem_count (size_t): Total number of elements in source.
 *   predicate_fn (PredicateFunc): Filter condition callback.
 * Returns:
 *   size_t: Number of elements matching the filter condition.
 */
size_t filterElements(int *dest_arr, const int *src_arr, size_t elem_count, PredicateFunc predicate_fn) {
    if (dest_arr == NULL || src_arr == NULL || predicate_fn == NULL) {
        return 0;
    }

    size_t match_count = 0;
    for (size_t idx = 0; idx < elem_count; idx++) {
        if (predicate_fn(src_arr[idx])) {
            dest_arr[match_count] = src_arr[idx]; /* Preserves elements satisfying predicate */
            match_count++;
        }
    }
    return match_count;
}

int main(void) {
    int initial_data[] = {1, 2, 3, 4, 5, 6};
    size_t count = sizeof(initial_data) / sizeof(initial_data[0]);

    int transformed[6];
    int filtered[6];

    applyTransform(transformed, initial_data, count, squareValue);
    printf("Squared values: ");
    for (size_t i = 0; i < count; i++) {
        printf("%d ", transformed[i]);
    }
    printf("\n");

    size_t evens_count = filterElements(filtered, initial_data, count, isEven);
    printf("Even elements:  ");
    for (size_t i = 0; i < evens_count; i++) {
        printf("%d ", filtered[i]);
    }
    printf("\n");

    return 0;
}

