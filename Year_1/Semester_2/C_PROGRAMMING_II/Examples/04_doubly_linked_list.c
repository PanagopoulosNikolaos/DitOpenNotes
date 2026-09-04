/**
 * Implements a bidirectional doubly linked list with memory-safe operations.
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

/**
 * Node representation for doubly linked list.
 */
typedef struct DoubleNode {
    int value;
    struct DoubleNode *prev_node;
    struct DoubleNode *next_node;
} DoubleNode;

/**
 * Header wrapper for doubly linked list managing head and tail references.
 */
typedef struct DoublyLinkedList {
    DoubleNode *head_node;
    DoubleNode *tail_node;
    size_t length;
} DoublyLinkedList;

/**
 * Initializes a new empty doubly linked list.
 * Returns:
 *   DoublyLinkedList*: Pointer to allocated list structure.
 */
DoublyLinkedList* createList(void) {
    DoublyLinkedList *list_ptr = (DoublyLinkedList *)malloc(sizeof(DoublyLinkedList));
    if (list_ptr == NULL) {
        return NULL; /* Halts on allocation exhaustion */
    }

    list_ptr->head_node = NULL;
    list_ptr->tail_node = NULL;
    list_ptr->length = 0;
    return list_ptr;
}

/**
 * Appends a new integer value to the tail of the list.
 * Args:
 *   list_ptr (DoublyLinkedList*): Pointer to the list.
 *   val (int): Integer value to append.
 * Returns:
 *   bool: True on successful allocation and insertion, false otherwise.
 */
bool appendValue(DoublyLinkedList *list_ptr, int val) {
    if (list_ptr == NULL) {
        return false;
    }

    DoubleNode *new_node = (DoubleNode *)malloc(sizeof(DoubleNode));
    if (new_node == NULL) {
        return false; /* Preserves list state if node allocation fails */
    }

    new_node->value = val;
    new_node->next_node = NULL;
    new_node->prev_node = list_ptr->tail_node;

    if (list_ptr->tail_node != NULL) {
        list_ptr->tail_node->next_node = new_node;
    } else {
        list_ptr->head_node = new_node; /* Sets head when list was initially empty */
    }

    list_ptr->tail_node = new_node;
    list_ptr->length++;
    return true;
}

/**
 * Traverses and prints the list values from head to tail.
 * Args:
 *   list_ptr (const DoublyLinkedList*): Pointer to the list.
 */
void printForward(const DoublyLinkedList *list_ptr) {
    if (list_ptr == NULL) {
        return;
    }

    printf("Forward:  [");
    DoubleNode *current_node = list_ptr->head_node;
    while (current_node != NULL) {
        printf("%d%s", current_node->value, current_node->next_node ? ", " : "");
        current_node = current_node->next_node;
    }
    printf("] (Length: %zu)\n", list_ptr->length);
}

/**
 * Frees all allocated nodes and the list container structure.
 * Args:
 *   list_ptr (DoublyLinkedList*): Pointer to the list to free.
 */
void destroyList(DoublyLinkedList *list_ptr) {
    if (list_ptr == NULL) {
        return;
    }

    DoubleNode *current_node = list_ptr->head_node;
    while (current_node != NULL) {
        DoubleNode *next_node = current_node->next_node;
        free(current_node); /* Releases individual node block */
        current_node = next_node;
    }

    free(list_ptr); /* Releases parent container */
}

int main(void) {
    DoublyLinkedList *my_list = createList();
    if (my_list == NULL) {
        perror("Failed to allocate list");
        return 1;
    }

    for (int num = 10; num <= 50; num += 10) {
        appendValue(my_list, num);
    }

    printForward(my_list);
    destroyList(my_list);

    return 0;
}

