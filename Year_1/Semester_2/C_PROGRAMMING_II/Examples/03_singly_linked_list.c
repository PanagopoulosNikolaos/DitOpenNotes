/**
 * Demonstrates basic linked list operations including insertion, traversal, and deallocation.
 */

#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int value;
    struct Node *next_node;
} Node;

/**
 * Inserts a new integer node at the front of a linked list.
 * Args:
 *   head_ref (Node**): Double pointer to the head of the list.
 *   new_value (int): Integer payload to store.
 * Returns:
 *   int: 1 on success, 0 on allocation failure.
 */
int insertFront(Node **head_ref, int new_value) {
    Node *new_node = (Node *)malloc(sizeof(Node));
    if (new_node == NULL) {
        return 0; /* Dynamic allocation error */
    }

    new_node->value = new_value;
    new_node->next_node = *head_ref;
    *head_ref = new_node; /* Repositions head pointer to new element */

    return 1;
}

/**
 * Prints all elements in a linked list from head to tail.
 * Args:
 *   head_ptr (const Node*): Pointer to head node.
 * Returns:
 *   void
 */
void printList(const Node *head_ptr) {
    const Node *curr_ptr = head_ptr;
    while (curr_ptr != NULL) {
        printf("%d -> ", curr_ptr->value);
        curr_ptr = curr_ptr->next_node;
    }
    printf("NULL\n");
}

/**
 * Deallocates all nodes in a linked list and sets the head pointer to NULL.
 * Args:
 *   head_ref (Node**): Double pointer to the head node.
 * Returns:
 *   void
 */
void freeList(Node **head_ref) {
    if (head_ref == NULL) return;

    Node *curr_ptr = *head_ref;
    while (curr_ptr != NULL) {
        Node *temp_ptr = curr_ptr->next_node; /* Preserves next node pointer before free */
        free(curr_ptr);
        curr_ptr = temp_ptr;
    }
    *head_ref = NULL; /* Eliminates dangling pointer */
}

int main(void) {
    Node *list_head = NULL;

    insertFront(&list_head, 30);
    insertFront(&list_head, 20);
    insertFront(&list_head, 10);

    printf("Linked List Elements:\n");
    printList(list_head);

    freeList(&list_head);
    return EXIT_SUCCESS;
}

