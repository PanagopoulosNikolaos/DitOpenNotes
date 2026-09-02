// Reversing a String (strrev)

#include <stdio.h>
#include <string.h>

int main() {
    char string[] = "programming";
    
    printf("Original string: %s\n", string);
    strrev(string);
    printf("Reversed string: %s\n", string);
    
    return 0;
}
