// Converting to Lowercase (strlwr)

#include <stdio.h>
#include <string.h>

int main() {
    char string[] = "HELLO World";
    
    printf("Original string: %s\n", string);
    strlwr(string);
    printf("Lowercase string: %s\n", string);
    
    return 0;
}
