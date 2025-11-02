"""
QUEUES - Data Structure Implementation

A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle.
Elements are added at the rear (enqueue) and removed from the front (dequeue).

Key Characteristics:
- FIFO (First In, First Out) ordering
- Enqueue operation: Add element to rear - O(1)
- Dequeue operation: Remove element from front - O(1)
- Front/Peek operation: View front element without removing - O(1)
- No random access to middle elements
- Can be implemented using arrays, linked lists, or circular arrays

Visual Representation:
    Front → [10] [20] [30] ← Rear
    
Operations:
- Enqueue(40): Add 40 to rear
    Front → [10] [20] [30] [40] ← Rear

- Dequeue(): Remove and return 10
    Front → [20] [30] [40] ← Rear

Common Use Cases:
- Task scheduling (CPU, printer queues)
- Breadth-First Search (BFS) in graphs
- Buffering (IO buffers, pipes)
- Asynchronous data transfer
- Call center systems
- Process management in operating systems
"""

class ArrayQueue:
    """
    Queue implementation using Python list.
    Simple but dequeue is O(n) due to shifting elements.
    """
    
    def __init__(self, capacity=None):
        self._data = []
        self._capacity = capacity
    
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def is_full(self):
        if self._capacity is None:
            return False
        return len(self._data) >= self._capacity
    
    def enqueue(self, item):
        """Add element to rear of queue - O(1)"""
        if self.is_full():
            raise OverflowError("Queue is full")
        self._data.append(item)
    
    def dequeue(self):
        """Remove and return front element - O(n) due to list shifting"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._data.pop(0)
    
    def front(self):
        """Return front element without removing - O(1)"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._data[0]
    
    def __str__(self):
        if self.is_empty():
            return "Queue: []"
        return "Queue (front → rear): [" + ", ".join(str(x) for x in self._data) + "]"

class CircularQueue:
    """
    Circular queue using fixed-size array with front and rear pointers.
    Provides O(1) enqueue and dequeue operations.
    """
    
    def __init__(self, capacity):
        self._data = [None] * capacity
        self._capacity = capacity
        self._size = 0
        self._front = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def is_full(self):
        return self._size == self._capacity
    
    def enqueue(self, item):
        """Add element to rear - O(1)"""
        if self.is_full():
            raise OverflowError("Queue is full")
        rear = (self._front + self._size) % self._capacity
        self._data[rear] = item
        self._size += 1
    
    def dequeue(self):
        """Remove and return front element - O(1)"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        item = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return item
    
    def front(self):
        """Return front element without removing - O(1)"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._data[self._front]
    
    def __str__(self):
        if self.is_empty():
            return "Queue: []"
        elements = []
        index = self._front
        for _ in range(self._size):
            elements.append(str(self._data[index]))
            index = (index + 1) % self._capacity
        return "Queue (front → rear): [" + ", ".join(elements) + "]"

class LinkedQueue:
    """
    Queue implementation using singly linked list.
    Provides O(1) enqueue and dequeue operations with no capacity limit.
    """
    
    class _Node:
        """Lightweight node class"""
        def __init__(self, data, next_node=None):
            self.data = data
            self.next = next_node
    
    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._front is None
    
    def enqueue(self, item):
        """Add element to rear - O(1)"""
        new_node = self._Node(item)
        if self.is_empty():
            self._front = self._rear = new_node
        else:
            self._rear.next = new_node
            self._rear = new_node
        self._size += 1
    
    def dequeue(self):
        """Remove and return front element - O(1)"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        item = self._front.data
        self._front = self._front.next
        if self._front is None:
            self._rear = None
        self._size -= 1
        return item
    
    def front(self):
        """Return front element without removing - O(1)"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._front.data
    
    def __str__(self):
        if self.is_empty():
            return "Queue: []"
        elements = []
        current = self._front
        while current:
            elements.append(str(current.data))
            current = current.next
        return "Queue (front → rear): [" + ", ".join(elements) + "]"

class Deque:
    """
    Double-ended queue (deque) that allows insertion and deletion at both ends.
    Implemented using a doubly linked list for O(1) operations at both ends.
    """
    
    class _Node:
        """Node with both next and prev pointers"""
        def __init__(self, data, prev_node=None, next_node=None):
            self.data = data
            self.prev = prev_node
            self.next = next_node
    
    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def add_front(self, item):
        """Add element to front - O(1)"""
        new_node = self._Node(item, None, self._front)
        if self.is_empty():
            self._front = self._rear = new_node
        else:
            self._front.prev = new_node
            self._front = new_node
        self._size += 1
    
    def add_rear(self, item):
        """Add element to rear - O(1)"""
        new_node = self._Node(item, self._rear, None)
        if self.is_empty():
            self._front = self._rear = new_node
        else:
            self._rear.next = new_node
            self._rear = new_node
        self._size += 1
    
    def remove_front(self):
        """Remove and return front element - O(1)"""
        if self.is_empty():
            raise IndexError("Deque is empty")
        item = self._front.data
        self._front = self._front.next
        if self._front is None:
            self._rear = None
        else:
            self._front.prev = None
        self._size -= 1
        return item
    
    def remove_rear(self):
        """Remove and return rear element - O(1)"""
        if self.is_empty():
            raise IndexError("Deque is empty")
        item = self._rear.data
        self._rear = self._rear.prev
        if self._rear is None:
            self._front = None
        else:
            self._rear.next = None
        self._size -= 1
        return item
    
    def front(self):
        """Return front element - O(1)"""
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self._front.data
    
    def rear(self):
        """Return rear element - O(1)"""
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self._rear.data
    
    def __str__(self):
        if self.is_empty():
            return "Deque: []"
        elements = []
        current = self._front
        while current:
            elements.append(str(current.data))
            current = current.next
        return "Deque (front → rear): [" + ", ".join(elements) + "]"

# Example usage
if __name__ == "__main__":
    print("=== Array Queue Demo ===")
    queue = ArrayQueue()
    
    for i in [10, 20, 30, 40]:
        queue.enqueue(i)
        print(f"Enqueued {i}: {queue}")
    
    print(f"Front element: {queue.front()}")
    
    while not queue.is_empty():
        dequeued = queue.dequeue()
        print(f"Dequeued {dequeued}: {queue}")
    
    print("\n=== Circular Queue Demo ===")
    circ_queue = CircularQueue(5)
    
    for i in range(1, 6):
        circ_queue.enqueue(i * 10)
        print(f"Enqueued {i * 10}: {circ_queue}")
    
    # Dequeue two elements
    circ_queue.dequeue()
    circ_queue.dequeue()
    print(f"After 2 dequeues: {circ_queue}")
    
    # Add more (demonstrates circular nature)
    circ_queue.enqueue(60)
    circ_queue.enqueue(70)
    print(f"After adding 60, 70: {circ_queue}")
    
    print("\n=== Linked Queue Demo ===")
    linked_queue = LinkedQueue()
    
    for char in ['A', 'B', 'C', 'D']:
        linked_queue.enqueue(char)
        print(f"Enqueued {char}: {linked_queue}")
    
    print(f"Size: {len(linked_queue)}")
    
    print("\n=== Deque Demo ===")
    deque = Deque()
    
    deque.add_rear(10)
    deque.add_rear(20)
    print(f"Added 10, 20 to rear: {deque}")
    
    deque.add_front(5)
    deque.add_front(1)
    print(f"Added 5, 1 to front: {deque}")
    
    print(f"Front: {deque.front()}, Rear: {deque.rear()}")
    
    print(f"Remove front: {deque.remove_front()}")
    print(f"Remove rear: {deque.remove_rear()}")
    print(f"After removals: {deque}")
