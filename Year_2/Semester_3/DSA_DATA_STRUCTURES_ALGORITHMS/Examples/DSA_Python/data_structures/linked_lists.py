"""
LINKED LISTS - Data Structure Implementation

A linked list is a linear data structure where elements (nodes) are stored in non-contiguous memory 
locations. Each node contains data and a reference (pointer/link) to the next node in the sequence.

Key Characteristics:
- Dynamic size (grows and shrinks at runtime)
- Non-contiguous memory allocation
- Efficient insertion/deletion at beginning: O(1)
- Insertion/deletion at end or middle: O(n) due to traversal
- Access by index: O(n) - must traverse from head
- No wasted memory from pre-allocation
- Extra memory for storing references

Memory Layout (Singly Linked List):
Memory is not contiguous. Nodes can be anywhere in memory:
Address 1000: [Data: 10 | Next: 2500] → Address 2500: [Data: 20 | Next: 1800] → Address 1800: [Data: 30 | Next: None]

Types of Linked Lists:
1. Singly Linked List - each node points to next node
2. Doubly Linked List - each node points to both next and previous nodes
3. Circular Linked List - last node points back to first node

Common Use Cases:
- Implementing stacks and queues
- Managing memory allocation (free lists)
- Undo functionality in applications
- Music playlists, browser history
- Hash table collision resolution (chaining)
"""

class Node:
    """A node in a singly linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    """
    Singly Linked List implementation where each node points to the next node.
    Maintains a reference to the head (first node) of the list.
    """
    
    def __init__(self):
        self.head = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self.head is None
    
    def prepend(self, data):
        """Add node at the beginning - O(1)"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self._size += 1
    
    def append(self, data):
        """Add node at the end - O(n)"""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1
    
    def insert_after(self, target_data, new_data):
        """Insert node after a specific value - O(n)"""
        current = self.head
        while current:
            if current.data == target_data:
                new_node = Node(new_data)
                new_node.next = current.next
                current.next = new_node
                self._size += 1
                return True
            current = current.next
        return False
    
    def delete(self, data):
        """Delete first occurrence of node with given data - O(n)"""
        if self.is_empty():
            return False
        
        if self.head.data == data:
            self.head = self.head.next
            self._size -= 1
            return True
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self._size -= 1
                return True
            current = current.next
        return False
    
    def search(self, data):
        """Search for a value - O(n)"""
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1
    
    def reverse(self):
        """Reverse the linked list in-place - O(n)"""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    def __str__(self):
        if self.is_empty():
            return "[]"
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements)

class DoublyNode:
    """A node in a doubly linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    """
    Doubly Linked List where each node has references to both next and previous nodes.
    Allows bidirectional traversal and more efficient operations.
    """
    
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self.head is None
    
    def prepend(self, data):
        """Add node at the beginning - O(1)"""
        new_node = DoublyNode(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._size += 1
    
    def append(self, data):
        """Add node at the end - O(1)"""
        new_node = DoublyNode(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1
    
    def delete(self, data):
        """Delete first occurrence of node - O(n)"""
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                
                self._size -= 1
                return True
            current = current.next
        return False
    
    def reverse(self):
        """Reverse the doubly linked list - O(n)"""
        current = self.head
        self.head, self.tail = self.tail, self.head
        
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev
    
    def __str__(self):
        if self.is_empty():
            return "[]"
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " <-> ".join(elements)

# Example usage
if __name__ == "__main__":
    print("=== Singly Linked List Demo ===")
    sll = SinglyLinkedList()
    
    print(f"Empty list: {sll}")
    
    # Add elements
    sll.append(10)
    sll.append(20)
    sll.append(30)
    print(f"After appending 10, 20, 30: {sll}")
    
    sll.prepend(5)
    print(f"After prepending 5: {sll}")
    
    sll.insert_after(20, 25)
    print(f"After inserting 25 after 20: {sll}")
    
    # Search
    pos = sll.search(25)
    print(f"Position of 25: {pos}")
    
    # Delete
    sll.delete(20)
    print(f"After deleting 20: {sll}")
    
    # Reverse
    sll.reverse()
    print(f"After reversing: {sll}")
    print(f"Size: {len(sll)}")
    
    print("\n=== Doubly Linked List Demo ===")
    dll = DoublyLinkedList()
    
    dll.append(100)
    dll.append(200)
    dll.append(300)
    print(f"After appending 100, 200, 300: {dll}")
    
    dll.prepend(50)
    print(f"After prepending 50: {dll}")
    
    dll.delete(200)
    print(f"After deleting 200: {dll}")
    
    dll.reverse()
    print(f"After reversing: {dll}")
    print(f"Size: {len(dll)}")
