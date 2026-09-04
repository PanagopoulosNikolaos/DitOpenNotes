/**
 * Reverses a string in-place using two-pointer swapping.
 */

#include <stdio.h>
#include <string.h>

/**
 * Reverses a null-terminated string in-place.
 * Args:
 *   str (char*): The target string to reverse.
 * Returns:
 *   char*: Pointer to the reversed string.
 */
char* reverseString(char *str) {
    if (str == NULL) {
        return NULL; /* Handles null pointer argument */
    }

    size_t left_idx = 0;
    size_t right_idx = strlen(str);

    if (right_idx == 0) {
        return str; /* Empty string requires no swapping */
    }

    right_idx--; /* Points to final non-null character */
    while (left_idx < right_idx) {
        char temp_char = str[left_idx];
        str[left_idx] = str[right_idx];
        str[right_idx] = temp_char;
        left_idx++;
        right_idx--;
    }

    return str;
}

int main(void) {
    char sample_string[] = "programming";

    printf("Original string: %s\n", sample_string);
    reverseString(sample_string);
    printf("Reversed string: %s\n", sample_string);

    return 0;
}
