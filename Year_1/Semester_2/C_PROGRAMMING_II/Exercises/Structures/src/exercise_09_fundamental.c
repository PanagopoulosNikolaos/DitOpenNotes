#include <stdio.h>
#include <stdlib.h> // Required for malloc

/*
 * Exercise 9: Self-Referential Structures (Linked List Node)
 *
 * Objective:
 * Define a self-referential structure 'Node' for a singly linked list,
 * containing an integer 'data' and a pointer to the next 'Node'.
 * Create a few nodes and link them together to form a simple list,
 * then traverse and print the data.
 */

// Define a self-referential structure for a linked list node
struct Node {
    int data;
    struct Node *next;
};

int main() {
    // Create nodes
    struct Node *head = NULL;
    struct Node *second = NULL;
    struct Node *third = NULL;

    // Allocate memory for nodes
    head = (struct Node*)malloc(sizeof(struct Node));// Allocate memory for head
    second = (struct Node*)malloc(sizeof(struct Node));// Allocate memory for second
    third = (struct Node*)malloc(sizeof(struct Node));// Allocate memory for third
    if (head == NULL || second == NULL || third == NULL) {
        printf("Memory allocation failed\n");
        return 1; // Exit if memory allocation fails
    }

    // Assign data and link nodes
    head->data = 1;
    head->next = second;

    second->data = 2;
    second->next = third;

    third->data = 3;
    third->next = NULL; // End of the list

    // Traverse and print the list
    struct Node *current = head;
    printf("Linked List: ");
    while (current != NULL) {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");

    // Free allocated memory
    free(head);
    free(second);
    free(third);

    return 0;
}
