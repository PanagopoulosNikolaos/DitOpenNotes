// Tokenizing a String (strtok)

#include <stdio.h>
#include <string.h>

int main() {
    char string[] = "This,is,a,comma,separated,string";
    char *token;
    
    token = strtok(string, ",");
    
    while (token != NULL) {
        printf("%s\n", token);
        token = strtok(NULL, ",");
    }
    
    return 0;
}
