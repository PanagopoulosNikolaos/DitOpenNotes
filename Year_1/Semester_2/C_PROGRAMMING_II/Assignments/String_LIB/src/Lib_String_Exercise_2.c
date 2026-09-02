// Concatenating Strings (strcat)

#include <stdio.h>
#include <string.h>

int main() {
    char first[50] = "Hello ";
    char second[] = "World!";
    
    strcat(first, second);
    
    printf("Concatenated string: %s\n", first);
    
    return 0;
}
