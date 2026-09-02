// Finding a Substring (strstr)

#include <stdio.h>
#include <string.h>

int main() {
    char haystack[] = "This is a simple string";
    char needle[] = "simple";
    char *result;
    
    result = strstr(haystack, needle);
    
    if (result)
        printf("Substring found at position: %ld\n", result - haystack + 1);
    else
        printf("Substring not found\n");
    
    return 0;
}
