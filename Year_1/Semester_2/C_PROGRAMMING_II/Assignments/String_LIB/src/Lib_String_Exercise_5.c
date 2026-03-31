// Finding a Character in String (strchr)

#include <stdio.h>
#include <string.h>

int main() {
    char string[] = "programming";
    char *position;
    
    position = strchr(string, 'g');
    
    if (position != NULL)
        printf("First occurrence of 'g' is at position: %ld\n", position - string + 1);
    else
        printf("Character not found\n");
    
    return 0;
}
