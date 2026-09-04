/**
 * Converts all uppercase characters in a string to lowercase.
 */

#include <stdio.h>
#include <string.h>
#include <ctype.h>

/**
 * Converts a null-terminated string to lowercase in-place.
 * Args:
 *   str (char*): The target string to convert.
 * Returns:
 *   char*: Pointer to the converted string.
 */
char* toLowercase(char *str) {
    if (str == NULL) {
        return NULL; /* Handles null pointer argument */
    }

    for (size_t idx = 0; str[idx] != '\0'; idx++) {
        str[idx] = (char)tolower((unsigned char)str[idx]); /* Converts uppercase character to lowercase safely */
    }

    return str;
}

int main(void) {
    char sample_string[] = "HELLO World";

    printf("Original string: %s\n", sample_string);
    toLowercase(sample_string);
    printf("Lowercase string: %s\n", sample_string);

    return 0;
}
