#include <iostream>
#include <memory>

/**
 * @brief Linked Lists - Data Structure Implementation in C++
 * 
 * A linked list is a linear data structure where elements (nodes) are stored in non-contiguous memory 
 * locations. Each node contains data and a reference (pointer/link) to the next node in the sequence.
 * 
 * Key Characteristics:
 * - Dynamic size (grows and shrinks at runtime)
 * - Non-contiguous memory allocation
 * - Efficient insertion/deletion at beginning: O(1)
 * - Insertion/deletion at end or middle: O(n) due to traversal
 * - Access by index: O(n) - must traverse from head
 * - No wasted memory from pre-allocation
 * - Extra memory for storing references
 * 
 * Memory Layout (Singly Linked List):
 * Memory is not contiguous. Nodes can be anywhere in memory:
 * Address 1000: [Data: 10 | Next: 2500] → Address 2500: [Data: 20 | Next: 1800] → Address 1800: [Data: 30 | Next: NULL]
 * 
 * Types of Linked Lists:
 * 1. Singly Linked List - each node points to next node
 * 2. Doubly Linked List - each node points to both next and previous nodes
 * 3. Circular Linked List - last node points back to first node
 * 
 * Common Use Cases:
 * - Implementing stacks and queues
 * - Managing memory allocation (free lists)
 * - Undo functionality in applications
 * - Music playlists, browser history
 * - Hash table collision resolution (chaining)
 */

struct Node {
    int data;
    std::shared_ptr<Node> next;
    
    explicit Node(int data) : data(data), next(nullptr) {}
};

class SinglyLinkedList {
private:
    std::shared_ptr<Node> head;
    size_t _size;

public:
    /**
     * @brief Singly Linked List implementation where each node points to the next node.
     * Maintains a reference to the head (first node) of the list.
     */
    SinglyLinkedList() : head(nullptr), _size(0) {}

    size_t size() const {
        return _size;
    }

    bool isEmpty() const {
        return head == nullptr;
    }

    /**
     * @brief Add node at the beginning - O(1)
     */
    void prepend(int data) {
        auto newNode = std::make_shared<Node>(data);
        newNode->next = head;
        head = newNode;
        ++_size;
    }

    /**
     * @brief Add node at the end - O(n)
     */
    void append(int data) {
        auto newNode = std::make_shared<Node>(data);
        if (isEmpty()) {
            head = newNode;
        } else {
            auto current = head;
            while (current->next) {
                current = current->next;
            }
            current->next = newNode;
        }
        ++_size;
    }

    /**
     * @brief Insert node after a specific value - O(n)
     */
    bool insertAfter(int targetData, int newData) {
        auto current = head;
        while (current) {
            if (current->data == targetData) {
                auto newNode = std::make_shared<Node>(newData);
                newNode->next = current->next;
                current->next = newNode;
                ++_size;
                return true;
            }
            current = current->next;
        }
        return false;
    }

    /**
     * @brief Delete first occurrence of node with given data - O(n)
     */
    bool remove(int data) {
        if (isEmpty()) {
            return false;
        }

        if (head->data == data) {
            head = head->next;
            --_size;
            return true;
        }

        auto current = head;
        while (current->next) {
            if (current->next->data == data) {
                current->next = current->next->next;
                --_size;
                return true;
            }
            current = current->next;
        }
        return false;
    }

    /**
     * @brief Search for a value - O(n)
     */
    int search(int data) const {
        auto current = head;
        int position = 0;
        while (current) {
            if (current->data == data) {
                return position;
            }
            current = current->next;
            ++position;
        }
        return -1;
    }

    /**
     * @brief Reverse the linked list in-place - O(n)
     */
    void reverse() {
        std::shared_ptr<Node> prev = nullptr;
        auto current = head;
        std::shared_ptr<Node> next = nullptr;

        while (current) {
            next = current->next;
            current->next = prev;
            prev = current;
            current = next;
        }
        head = prev;
    }

    void print() const {
        if (isEmpty()) {
            std::cout << "[]" << std::endl;
            return;
        }
        auto current = head;
        while (current) {
            std::cout << current->data;
            if (current->next) {
                std::cout << " -> ";
            }
            current = current->next;
        }
        std::cout << std::endl;
    }
};

struct DoublyNode {
    int data;
    std::shared_ptr<DoublyNode> next;
    std::weak_ptr<DoublyNode> prev;  // Use weak_ptr to avoid circular references
    
    explicit DoublyNode(int data) : data(data), next(nullptr) {}
};

class DoublyLinkedList {
private:
    std::shared_ptr<DoublyNode> head;
    std::shared_ptr<DoublyNode> tail;
    size_t _size;

public:
    /**
     * @brief Doubly Linked List where each node has references to both next and previous nodes.
     * Allows bidirectional traversal and more efficient operations.
     */
    DoublyLinkedList() : head(nullptr), tail(nullptr), _size(0) {}

    size_t size() const {
        return _size;
    }

    bool isEmpty() const {
        return head == nullptr;
    }

    /**
     * @brief Add node at the beginning - O(1)
     */
    void prepend(int data) {
        auto newNode = std::make_shared<DoublyNode>(data);
        if (isEmpty()) {
            head = tail = newNode;
        } else {
            newNode->next = head;
            head->prev = newNode;
            head = newNode;
        }
        ++_size;
    }

    /**
     * @brief Add node at the end - O(1)
     */
    void append(int data) {
        auto newNode = std::make_shared<DoublyNode>(data);
        if (isEmpty()) {
            head = tail = newNode;
        } else {
            newNode->prev = tail;
            tail->next = newNode;
            tail = newNode;
        }
        ++_size;
    }

    /**
     * @brief Delete first occurrence of node - O(n)
     */
    bool remove(int data) {
        auto current = head;
        while (current) {
            if (current->data == data) {
                if (auto prev_node = current->prev.lock()) {
                    prev_node->next = current->next;
                } else {
                    head = current->next;
                }

                if (current->next) {
                    current->next->prev = current->prev;
                } else {
                    tail = current->prev.lock();
                }

                --_size;
                return true;
            }
            current = current->next;
        }
        return false;
    }

    /**
     * @brief Reverse the doubly linked list - O(n)
     */
    void reverse() {
        auto current = head;
        std::shared_ptr<DoublyNode> temp = nullptr;

        while (current) {
            temp = current->next;
            current->next = current->prev.lock();
            current->prev = temp;

            if (!current->next) {
                head = current;
            }
            current = temp;
        }

        if (tail) {
            tail = head;
            head = tail;
        }
    }

    void print() const {
        if (isEmpty()) {
            std::cout << "[]" << std::endl;
            return;
        }
        auto current = head;
        while (current) {
            std::cout << current->data;
            if (current->next) {
                std::cout << " <-> ";
            }
            current = current->next;
        }
        std::cout << std::endl;
    }
};

// Example usage
#ifndef SKIP_STANDALONE_MAIN
int main() {
    std::cout << "=== Singly Linked List Demo ===" << std::endl;
    SinglyLinkedList sll;

    std::cout << "Empty list: ";
    sll.print();

    // Add elements
    sll.append(10);
    sll.append(20);
    sll.append(30);
    std::cout << "After appending 10, 20, 30: ";
    sll.print();

    sll.prepend(5);
    std::cout << "After prepending 5: ";
    sll.print();

    sll.insertAfter(20, 25);
    std::cout << "After inserting 25 after 20: ";
    sll.print();

    // Search
    int pos = sll.search(25);
    std::cout << "Position of 25: " << pos << std::endl;

    // Delete
    sll.remove(20);
    std::cout << "After deleting 20: ";
    sll.print();

    // Reverse
    sll.reverse();
    std::cout << "After reversing: ";
    sll.print();
    std::cout << "Size: " << sll.size() << std::endl;

    std::cout << "\n=== Doubly Linked List Demo ===" << std::endl;
    DoublyLinkedList dll;

    dll.append(100);
    dll.append(200);
    dll.append(300);
    std::cout << "After appending 100, 200, 300: ";
    dll.print();

    dll.prepend(50);
    std::cout << "After prepending 50: ";
    dll.print();

    dll.remove(200);
    std::cout << "After deleting 200: ";
    dll.print();

    dll.reverse();
    std::cout << "After reversing: ";
    dll.print();
    std::cout << "Size: " << dll.size() << std::endl;

    return 0;
}
#endif // SKIP_STANDALONE_MAIN
