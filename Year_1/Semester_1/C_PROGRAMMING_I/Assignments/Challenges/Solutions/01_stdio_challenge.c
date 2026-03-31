#include <stdio.h>

int main() {
    char name[20];
    int number;

    printf("Enter your name: ");
    scanf("%s", name);

    printf("Enter your favorite number: ");
    scanf("%d", &number);

    printf("Hello, %s! Your favorite number is %d.\n", name, number);

    return 0;
}
