// Finding String Length (strlen)

#include <stdio.h>
#include <string.h>

int main() {
    char string[] = "Hello, World!";
    int length = strlen(string);
    
    printf("The string: %s\n", string);
    printf("Length of the string: %d\n", length);
    
    return 0;
}
