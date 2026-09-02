// Comparing Strings (strcmp

#include <stdio.h>
#include <string.h>

int main() {
    char str1[] = "apple";
    char str2[] = "banana";
    int result;
    
    result = strcmp(str1, str2);
    
    if (result < 0)
        printf("%s comes before %s\n", str1, str2);
    else if (result > 0)
        printf("%s comes after %s\n", str1, str2);
    else
        printf("%s is equal to %s\n", str1, str2);
    
    return 0;
}
