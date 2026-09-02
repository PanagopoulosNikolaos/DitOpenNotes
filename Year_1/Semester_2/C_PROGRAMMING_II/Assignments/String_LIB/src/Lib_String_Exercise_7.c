// Converting to Lowercase (portable standard C implementation)

#include <stdio.h>
#include <string.h>
#include <ctype.h>

/**
 * Converts all uppercase characters in a string to lowercase in place.
 * Args:
 * str (char *): Pointer to the target string buffer.
 * Returns:
 * void: No return value.
 */
void toLowerString(char *str) {
    if (str == NULL) {
        return;
    }
    for (size_t i = 0; str[i] != '\0'; i++) {
        str[i] = (char)tolower((unsigned char)str[i]);
    }
}

int main(void) {
    char string[] = "HELLO World";
    
    printf("Original string: %s\n", string);
    toLowerString(string);
    printf("Lowercase string: %s\n", string);
    
    return 0;
}

