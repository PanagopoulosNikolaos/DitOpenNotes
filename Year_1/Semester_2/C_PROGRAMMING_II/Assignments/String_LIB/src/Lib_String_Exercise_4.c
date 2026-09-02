// Reversing a String (portable standard C implementation)

#include <stdio.h>
#include <string.h>

/**
 * Reverses a null-terminated string in place.
 * Args:
 * str (char *): Pointer to the target string buffer.
 * Returns:
 * void: No return value.
 */
void reverseString(char *str) {
    if (str == NULL) {
        return;
    }
    size_t length = strlen(str);
    if (length <= 1) {
        return;
    }
    size_t left = 0;
    size_t right = length - 1;
    while (left < right) {
        char temp = str[left];
        str[left] = str[right];
        str[right] = temp;
        left++;
        right--;
    }
}

int main(void) {
    char string[] = "programming";
    
    printf("Original string: %s\n", string);
    reverseString(string);
    printf("Reversed string: %s\n", string);
    
    return 0;
}

