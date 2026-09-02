/**
 * Demonstrates a complete singly linked list implementation in C.
 * Covers node creation, insertion at head/tail, searching, deletion,
 * and memory cleanup.
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

/**
 * Node representation in a singly linked list.
 */
typedef struct Node {
    int value;
    struct Node *next;
} Node;

/**
 * Creates a new heap-allocated node.
 * Args:
 * value (int): Integer value stored in node.
 * Returns:
 * Node*: Pointer to created node, or NULL upon failure.
 */
Node *createNode(int value) {
    Node *node = (Node *)malloc(sizeof(Node));
    if (node == NULL) {
        perror("Failed to allocate list node");
        return NULL;
    }
    node->value = value;
    node->next = NULL;
    return node;
}

/**
 * Inserts a value at the head of the linked list.
 * Args:
 * head_ref (Node**): Pointer to head pointer.
 * value (int): Value to insert.
 * Returns:
 * bool: true if successful, false otherwise.
 */
bool insertHead(Node **head_ref, int value) {
    if (head_ref == NULL) {
        return false;
    }
    Node *new_node = createNode(value);
    if (new_node == NULL) {
        return false;
    }
    new_node->next = *head_ref;
    *head_ref = new_node;
    return true;
}

/**
 * Inserts a value at the tail of the linked list.
 * Args:
 * head_ref (Node**): Pointer to head pointer.
 * value (int): Value to append.
 * Returns:
 * bool: true if successful, false otherwise.
 */
bool insertTail(Node **head_ref, int value) {
    if (head_ref == NULL) {
        return false;
    }
    Node *new_node = createNode(value);
    if (new_node == NULL) {
        return false;
    }
    if (*head_ref == NULL) {
        *head_ref = new_node;
        return true;
    }
    Node *current = *head_ref;
    while (current->next != NULL) {
        current = current->next;
    }
    current->next = new_node;
    return true;
}

/**
 * Deletes the first node matching the target value.
 * Args:
 * head_ref (Node**): Pointer to head pointer.
 * value (int): Value to remove.
 * Returns:
 * bool: true if a node was removed, false if not found.
 */
bool deleteValue(Node **head_ref, int value) {
    if (head_ref == NULL || *head_ref == NULL) {
        return false;
    }
    Node *current = *head_ref;
    if (current->value == value) {
        *head_ref = current->next;
        free(current);
        return true;
    }
    while (current->next != NULL && current->next->value != value) {
        current = current->next;
    }
    if (current->next == NULL) {
        return false;
    }
    Node *to_delete = current->next;
    current->next = to_delete->next;
    free(to_delete);
    return true;
}

/**
 * Prints all elements in the linked list.
 * Args:
 * head (const Node*): Head pointer of list.
 * Returns:
 * void: No return value.
 */
void printList(const Node *head) {
    const Node *curr = head;
    printf("List: ");
    while (curr != NULL) {
        printf("%d -> ", curr->value);
        curr = curr->next;
    }
    printf("NULL\n");
}

/**
 * Deallocates all nodes in the linked list.
 * Args:
 * head_ref (Node**): Pointer to head pointer.
 * Returns:
 * void: No return value.
 */
void freeList(Node **head_ref) {
    if (head_ref == NULL) {
        return;
    }
    Node *curr = *head_ref;
    while (curr != NULL) {
        Node *next_node = curr->next;
        free(curr);
        curr = next_node;
    }
    *head_ref = NULL;
}

int main(void) {
    Node *head = NULL;

    insertHead(&head, 30);
    insertHead(&head, 20);
    insertHead(&head, 10);
    insertTail(&head, 40);
    insertTail(&head, 50);

    printList(head);

    printf("Deleting value 30...\n");
    deleteValue(&head, 30);
    printList(head);

    printf("Deleting head (10)...\n");
    deleteValue(&head, 10);
    printList(head);

    freeList(&head);
    printList(head);

    return EXIT_SUCCESS;
}
