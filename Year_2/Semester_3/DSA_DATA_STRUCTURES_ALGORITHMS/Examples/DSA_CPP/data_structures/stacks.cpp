#include <iostream>
#include <vector>
#include <stdexcept>
#include <memory>
#include <string>

/**
 * @brief STACKS - Data Structure Implementation in C++
 * 
 * A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle.
 * Elements are added and removed from the same end, called the "top" of the stack.
 * 
 * Key Characteristics:
 * - LIFO (Last In, First Out) ordering
 * - Push operation: Add element to top - O(1)
 * - Pop operation: Remove element from top - O(1)
 * - Peek/Top operation: View top element without removing - O(1)
 * - No random access to middle elements
 * - Can be implemented using arrays or linked lists
 * 
 * Visual Representation:
 *     Top → [30]
 *           [20]
 *           [10]
 *     
 * Operations:
 * - Push(40): Add 40 to top
 *     Top → [40]
 *           [30]
 *           [20]
 *           [10]
 * 
 * - Pop(): Remove and return 40
 *     Top → [30]
 *           [20]
 *           [10]
 * 
 * Common Use Cases:
 * - Function call management (call stack)
 * - Expression evaluation and syntax parsing
 * - Undo/Redo functionality
 * - Backtracking algorithms (maze solving, DFS)
 * - Browser history navigation
 * - Balanced parentheses checking
 */

template<typename T>
class ArrayStack {
private:
    std::vector<T> _data;
    size_t _capacity;

public:
    /**
     * @brief Stack implementation using a C++ vector (dynamic array).
     * Provides O(1) push and pop operations.
     */
    explicit ArrayStack(size_t capacity = 0) : _capacity(capacity) {}

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
     * @brief Add element to top of stack - O(1)
     */
    void push(const T& item) {
        if (full()) {
            throw std::overflow_error("Stack is full");
        }
        _data.push_back(item);
    }

    /**
     * @brief Remove and return top element - O(1)
     */
    T pop() {
        if (empty()) {
            throw std::out_of_range("Stack is empty");
        }
        T item = _data.back();
        _data.pop_back();
        return item;
    }

    /**
     * @brief Return top element without removing - O(1)
     */
    T peek() const {
        if (empty()) {
            throw std::out_of_range("Stack is empty");
        }
        return _data.back();
    }

    /**
     * @brief Remove all elements from stack
     */
    void clear() {
        _data.clear();
    }

    void print() const {
        if (empty()) {
            std::cout << "Stack: []" << std::endl;
            return;
        }
        std::cout << "Stack (top → bottom): [";
        for (int i = static_cast<int>(_data.size()) - 1; i >= 0; --i) {
            std::cout << _data[i];
            if (i > 0) std::cout << ", ";
        }
        std::cout << "]" << std::endl;
    }
};

template<typename T>
struct LinkedStackNode {
    T data;
    std::shared_ptr<LinkedStackNode<T>> next;

    LinkedStackNode(const T& data) : data(data), next(nullptr) {}
};

template<typename T>
class LinkedStack {
private:
    std::shared_ptr<LinkedStackNode<T>> _top;
    size_t _size;

public:
    /**
     * @brief Stack implementation using a singly linked list.
     * Provides O(1) push and pop operations with no capacity limit.
     */
    LinkedStack() : _top(nullptr), _size(0) {}

    size_t size() const {
        return _size;
    }

    bool empty() const {
        return _top == nullptr;
    }

    /**
     * @brief Add element to top of stack - O(1)
     */
    void push(const T& item) {
        auto newNode = std::make_shared<LinkedStackNode<T>>(item);
        newNode->next = _top;
        _top = newNode;
        ++_size;
    }

    /**
     * @brief Remove and return top element - O(1)
     */
    T pop() {
        if (empty()) {
            throw std::out_of_range("Stack is empty");
        }
        T data = _top->data;
        _top = _top->next;
        --_size;
        return data;
    }

    /**
     * @brief Return top element without removing - O(1)
     */
    T peek() const {
        if (empty()) {
            throw std::out_of_range("Stack is empty");
        }
        return _top->data;
    }

    /**
     * @brief Remove all elements from stack
     */
    void clear() {
        _top = nullptr;
        _size = 0;
    }

    void print() const {
        if (empty()) {
            std::cout << "Stack: []" << std::endl;
            return;
        }
        std::cout << "Stack (top → bottom): [";
        auto current = _top;
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

class StackApplications {
public:
    /**
     * @brief Check if parentheses/brackets are balanced - O(n)
     */
    static bool isBalancedParentheses(const std::string& expression) {
        ArrayStack<char> stack;
        std::string opening = "({[";
        std::string closing = ")}]";
        
        for (char c : expression) {
            if (opening.find(c) != std::string::npos) {
                stack.push(c);
            } else if (closing.find(c) != std::string::npos) {
                if (stack.empty()) {
                    return false;
                }
                
                char top = stack.pop();
                if ((c == ')' && top != '(') ||
                    (c == '}' && top != '{') ||
                    (c == ']' && top != '[')) {
                    return false;
                }
            }
        }
        
        return stack.empty();
    }

    /**
     * @brief Reverse a string using stack - O(n)
     */
    static std::string reverseString(const std::string& text) {
        ArrayStack<char> stack;
        for (char c : text) {
            stack.push(c);
        }
        
        std::string result;
        while (!stack.empty()) {
            result += stack.pop();
        }
        
        return result;
    }

    /**
     * @brief Evaluate postfix expression - O(n)
     */
    static double evaluatePostfix(const std::string& expression) {
        ArrayStack<double> stack;
        std::string operators = "+-*/";
        
        // Split the expression by spaces
        size_t start = 0;
        size_t end = 0;
        
        while (end < expression.length()) {
            // Skip leading spaces
            while (start < expression.length() && expression[start] == ' ') {
                start++;
            }
            
            end = start;
            // Find the next space
            while (end < expression.length() && expression[end] != ' ') {
                end++;
            }
            
            if (start < expression.length()) {
                std::string token = expression.substr(start, end - start);
                
                if (operators.find(token[0]) == std::string::npos && token.length() == 1) {
                    // It's an operand (number)
                    stack.push(static_cast<double>(token[0] - '0'));
                } else {
                    // It's an operator
                    double b = stack.pop();
                    double a = stack.pop();
                    
                    if (token[0] == '+') {
                        stack.push(a + b);
                    } else if (token[0] == '-') {
                        stack.push(a - b);
                    } else if (token[0] == '*') {
                        stack.push(a * b);
                    } else if (token[0] == '/') {
                        stack.push(a / b);
                    }
                }
            }
            
            start = end + 1;
        }
        
        return stack.pop();
    }
};

// Example usage
#ifndef SKIP_STANDALONE_MAIN
int main() {
    std::cout << "=== Array Stack Demo ===" << std::endl;
    ArrayStack<int> stack;

    // Push elements
    for (int i : {10, 20, 30, 40}) {
        stack.push(i);
        std::cout << "Pushed " << i << ": ";
        stack.print();
    }

    // Peek
    std::cout << "Top element: " << stack.peek() << std::endl;

    // Pop elements
    while (!stack.empty()) {
        int popped = stack.pop();
        std::cout << "Popped " << popped << ": ";
        stack.print();
    }

    std::cout << "\n=== Linked Stack Demo ===" << std::endl;
    LinkedStack<char> linkedStack;

    for (char c : {'A', 'B', 'C', 'D'}) {
        linkedStack.push(c);
        std::cout << "Pushed " << c << ": ";
        linkedStack.print();
    }

    std::cout << "Size: " << linkedStack.size() << std::endl;

    std::cout << "\n=== Stack Applications ===" << std::endl;

    // Balanced parentheses
    std::vector<std::string> testCases = {"((()))", "({[]})", "(()", "({[}]}", "({[]})"};
    for (const std::string& expr : testCases) {
        bool result = StackApplications::isBalancedParentheses(expr);
        std::cout << "'" << expr << "' is balanced: " << (result ? "true" : "false") << std::endl;
    }

    // Reverse string
    std::string text = "Hello, World!";
    std::string reversedText = StackApplications::reverseString(text);
    std::cout << "\nOriginal: " << text << std::endl;
    std::cout << "Reversed: " << reversedText << std::endl;

    // Note: The postfix evaluation function assumes single-digit numbers
    // For simplicity, we'll demonstrate with a basic example
    std::cout << "\nFor postfix evaluation, we'd evaluate expressions like '3 4 + 2 * 7 /'" << std::endl;

    return 0;
}
#endif // SKIP_STANDALONE_MAIN
