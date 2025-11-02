// Setting Memory (memset)

#include <stdio.h>
#include <string.h>

int main() {
    char string[20];
    
    memset(string, '*', 10);
    string[10] = '\0';
    
    printf("String after memset: %s\n", string);
    
    return 0;
}
