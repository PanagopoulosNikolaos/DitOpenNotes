#include <iostream>
#include <vector>
#include <stdexcept>
#include <memory>
#include <deque>

/**
 * @brief QUEUES - Data Structure Implementation in C++
 * 
 * A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle.
 * Elements are added at the rear (enqueue) and removed from the front (dequeue).
 * 
 * Key Characteristics:
 * - FIFO (First In, First Out) ordering
 * - Enqueue operation: Add element to rear - O(1)
 * - Dequeue operation: Remove element from front - O(1)
 * - Front/Peek operation: View front element without removing - O(1)
 * - No random access to middle elements
 * - Can be implemented using arrays, linked lists, or circular arrays
 * 
 * Visual Representation:
 *     Front → [10] [20] [30] ← Rear
 *     
 * Operations:
 * - Enqueue(40): Add 40 to rear
 *     Front → [10] [20] [30] [40] ← Rear
 * 
 * - Dequeue(): Remove and return 10
 *     Front → [20] [30] [40] ← Rear
 * 
 * Common Use Cases:
 * - Task scheduling (CPU, printer queues)
 * - Breadth-First Search (BFS) in graphs
 * - Buffering (IO buffers, pipes)
 * - Asynchronous data transfer
 * - Call center systems
 * - Process management in operating systems
 */

template<typename T>
class ArrayQueue {
private:
    std::vector<T> _data;
    size_t _capacity;

public:
    /**
     * @brief Queue implementation using C++ vector.
     * Simple but dequeue is O(n) due to shifting elements.
     */
    explicit ArrayQueue(size_t capacity = 0) : _capacity(capacity) {}

    size_t size() const {
        return _data.size();
    }

    bool empty() const {
        return _data.empty();
    }

    bool full() const {
        if (_capacity == 0) {
            return false;  // No capacity limit
        }
        return _data.size() >= _capacity;
    }

    /**
     * @brief Add element to rear of queue - O(1) amortized
     */
    void enqueue(const T& item) {
        if (full()) {
            throw std::overflow_error("Queue is full");
        }
        _data.push_back(item);
    }

    /**
     * @brief Remove and return front element - O(n) due to vector shifting
     */
    T dequeue() {
        if (empty()) {
            throw std::out_of_range("Queue is empty");
        }
        T item = _data.front();
        _data.erase(_data.begin());  // This is O(n) - inefficient
        return item;
    }

    /**
     * @brief Return front element without removing - O(1)
     */
    T front() const {
        if (empty()) {
            throw std::out_of_range("Queue is empty");
        }
        return _data.front();
    }

    void print() const {
        if (empty()) {
            std::cout << "Queue: []" << std::endl;
            return;
        }
        std::cout << "Queue (front → rear): [";
        for (size_t i = 0; i < _data.size(); ++i) {
            std::cout << _data[i];
            if (i < _data.size() - 1) std::cout << ", ";
        }
        std::cout << "]" << std::endl;
    }
};

template<typename T>
class CircularQueue {
private:
    std::unique_ptr<T[]> _data;
    size_t _capacity;
    size_t _size;
    size_t _front;

public:
    /**
     * @brief Circular queue using fixed-size array with front and rear pointers.
     * Provides O(1) enqueue and dequeue operations.
     */
    explicit CircularQueue(size_t capacity) : _capacity(capacity), _size(0), _front(0) {
        _data = std::make_unique<T[]>(capacity);
    }

    size_t size() const {
        return _size;
    }

    bool empty() const {
        return _size == 0;
    }

    bool full() const {
        return _size == _capacity;
    }

    /**
     * @brief Add element to rear - O(1)
     */
    void enqueue(const T& item) {
        if (full()) {
            throw std::overflow_error("Queue is full");
        }
        size_t rear = (_front + _size) % _capacity;
        _data[rear] = item;
        ++_size;
    }

    /**
     * @brief Remove and return front element - O(1)
     */
    T dequeue() {
        if (empty()) {
            throw std::out_of_range("Queue is empty");
        }
        T item = _data[_front];
        _data[_front] = T{};  // Reset to default value
        _front = (_front + 1) % _capacity;
        --_size;
        return item;
    }

    /**
     * @brief Return front element without removing - O(1)
     */
    T front() const {
        if (empty()) {
            throw std::out_of_range("Queue is empty");
        }
        return _data[_front];
    }

    void print() const {
        if (empty()) {
            std::cout << "Queue: []" << std::endl;
            return;
        }
        std::cout << "Queue (front → rear): [";
        size_t index = _front;
        for (size_t i = 0; i < _size; ++i) {
            std::cout << _data[index];
            if (i < _size - 1) std::cout << ", ";
            index = (index + 1) % _capacity;
        }
        std::cout << "]" << std::endl;
    }
};

template<typename T>
struct LinkedQueueNode {
    T data;
    std::shared_ptr<LinkedQueueNode<T>> next;

    LinkedQueueNode(const T& data) : data(data), next(nullptr) {}
};

template<typename T>
class LinkedQueue {
private:
    std::shared_ptr<LinkedQueueNode<T>> _front;
    std::shared_ptr<LinkedQueueNode<T>> _rear;
    size_t _size;

public:
    /**
     * @brief Queue implementation using singly linked list.
     * Provides O(1) enqueue and dequeue operations with no capacity limit.
     */
    LinkedQueue() : _front(nullptr), _rear(nullptr), _size(0) {}

    size_t size() const {
        return _size;
    }

    bool empty() const {
        return _front == nullptr;
    }

    /**
     * @brief Add element to rear - O(1)
     */
    void enqueue(const T& item) {
        auto newNode = std::make_shared<LinkedQueueNode<T>>(item);
        if (empty()) {
            _front = _rear = newNode;
        } else {
            _rear->next = newNode;
            _rear = newNode;
        }
        ++_size;
    }

    /**
     * @brief Remove and return front element - O(1)
     */
    T dequeue() {
        if (empty()) {
            throw std::out_of_range("Queue is empty");
        }
        T item = _front->data;
        _front = _front->next;
        if (_front == nullptr) {
            _rear = nullptr;
        }
        --_size;
        return item;
    }

    /**
     * @brief Return front element without removing - O(1)
     */
    T front() const {
        if (empty()) {
            throw std::out_of_range("Queue is empty");
        }
        return _front->data;
    }

    void print() const {
        if (empty()) {
            std::cout << "Queue: []" << std::endl;
            return;
        }
        std::cout << "Queue (front → rear): [";
        auto current = _front;
        bool first = true;
        while (current) {
            if (!first) std::cout << ", ";
            std::cout << current->data;
            first = false;
            current = current->next;
        }
        std::cout << "]" << std::endl;
    }
};

template<typename T>
struct DequeNode {
    T data;
    std::shared_ptr<DequeNode<T>> next;
    std::weak_ptr<DequeNode<T>> prev;  // Use weak_ptr to avoid circular references

    explicit DequeNode(const T& data) : data(data), next(nullptr) {}
};

template<typename T>
class Deque {
private:
    std::shared_ptr<DequeNode<T>> _front;
    std::shared_ptr<DequeNode<T>> _rear;
    size_t _size;

public:
    /**
     * @brief Double-ended queue (deque) that allows insertion and deletion at both ends.
     * Implemented using a doubly linked list for O(1) operations at both ends.
     */
    Deque() : _front(nullptr), _rear(nullptr), _size(0) {}

    size_t size() const {
        return _size;
    }

    bool empty() const {
        return _size == 0;
    }

    /**
     * @brief Add element to front - O(1)
     */
    void addFront(const T& item) {
        auto newNode = std::make_shared<DequeNode<T>>(item);
        if (empty()) {
            _front = _rear = newNode;
        } else {
            newNode->next = _front;
            _front->prev = newNode;
            _front = newNode;
        }
        ++_size;
    }

    /**
     * @brief Add element to rear - O(1)
     */
    void addRear(const T& item) {
        auto newNode = std::make_shared<DequeNode<T>>(item);
        if (empty()) {
            _front = _rear = newNode;
        } else {
            _rear->next = newNode;
            newNode->prev = _rear;
            _rear = newNode;
        }
        ++_size;
    }

    /**
     * @brief Remove and return front element - O(1)
     */
    T removeFront() {
        if (empty()) {
            throw std::out_of_range("Deque is empty");
        }
        T item = _front->data;
        _front = _front->next;
        if (_front) {
            _front->prev.reset();
        } else {
            _rear = nullptr;
        }
        --_size;
        return item;
    }

    /**
     * @brief Remove and return rear element - O(1)
     */
    T removeRear() {
        if (empty()) {
            throw std::out_of_range("Deque is empty");
        }
        T item = _rear->data;
        _rear = _rear->prev.lock();
        if (_rear) {
            _rear->next = nullptr;
        } else {
            _front = nullptr;
        }
        --_size;
        return item;
    }

    /**
     * @brief Return front element - O(1)
     */
    T front() const {
        if (empty()) {
            throw std::out_of_range("Deque is empty");
        }
        return _front->data;
    }

    /**
     * @brief Return rear element - O(1)
     */
    T rear() const {
        if (empty()) {
            throw std::out_of_range("Deque is empty");
        }
        return _rear->data;
    }

    void print() const {
        if (empty()) {
            std::cout << "Deque: []" << std::endl;
            return;
        }
        std::cout << "Deque (front → rear): [";
        auto current = _front;
        bool first = true;
        while (current) {
            if (!first) std::cout << ", ";
            std::cout << current->data;
            first = false;
            current = current->next;
        }
        std::cout << "]" << std::endl;
    }
};

// Example usage
#ifndef SKIP_STANDALONE_MAIN
int main() {
    std::cout << "=== Array Queue Demo ===" << std::endl;
    ArrayQueue<int> queue;

    for (int i : {10, 20, 30, 40}) {
        queue.enqueue(i);
        std::cout << "Enqueued " << i << ": ";
        queue.print();
    }

    std::cout << "Front element: " << queue.front() << std::endl;

    while (!queue.empty()) {
        int dequeued = queue.dequeue();
        std::cout << "Dequeued " << dequeued << ": ";
        queue.print();
    }

    std::cout << "\n=== Circular Queue Demo ===" << std::endl;
    CircularQueue<int> circQueue(5);

    for (int i = 1; i <= 5; ++i) {
        circQueue.enqueue(i * 10);
        std::cout << "Enqueued " << i * 10 << ": ";
        circQueue.print();
    }

    // Dequeue two elements
    circQueue.dequeue();
    circQueue.dequeue();
    std::cout << "After 2 dequeues: ";
    circQueue.print();

    // Add more (demonstrates circular nature)
    circQueue.enqueue(60);
    circQueue.enqueue(70);
    std::cout << "After adding 60, 70: ";
    circQueue.print();

    std::cout << "\n=== Linked Queue Demo ===" << std::endl;
    LinkedQueue<int> linkedQueue;

    for (char c : {'A', 'B', 'C', 'D'}) {
        int val = static_cast<int>(c);  // Convert char to int for storage
        linkedQueue.enqueue(val);
        std::cout << "Enqueued " << c << ": ";
        linkedQueue.print();
    }

    std::cout << "Size: " << linkedQueue.size() << std::endl;

    std::cout << "\n=== Deque Demo ===" << std::endl;
    Deque<int> dq;

    dq.addRear(10);
    dq.addRear(20);
    std::cout << "Added 10, 20 to rear: ";
    dq.print();

    dq.addFront(5);
    dq.addFront(1);
    std::cout << "Added 5, 1 to front: ";
    dq.print();

    std::cout << "Front: " << dq.front() << ", Rear: " << dq.rear() << std::endl;

    std::cout << "Remove front: " << dq.removeFront() << std::endl;
    std::cout << "Remove rear: " << dq.removeRear() << std::endl;
    std::cout << "After removals: ";
    dq.print();

    return 0;
}
#endif // SKIP_STANDALONE_MAIN
