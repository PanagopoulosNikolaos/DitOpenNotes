"""
STACKS - Data Structure Implementation

A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle.
Elements are added and removed from the same end, called the "top" of the stack.

Key Characteristics:
- LIFO (Last In, First Out) ordering
- Push operation: Add element to top - O(1)
- Pop operation: Remove element from top - O(1)
- Peek/Top operation: View top element without removing - O(1)
- No random access to middle elements
- Can be implemented using arrays or linked lists

Visual Representation:
    Top → [30]
          [20]
          [10]
    
Operations:
- Push(40): Add 40 to top
    Top → [40]
          [30]
          [20]
          [10]

- Pop(): Remove and return 40
    Top → [30]
          [20]
          [10]

Common Use Cases:
- Function call management (call stack)
- Expression evaluation and syntax parsing
- Undo/Redo functionality
- Backtracking algorithms (maze solving, DFS)
- Browser history navigation
- Balanced parentheses checking
"""

class ArrayStack:
    """
    Stack implementation using a Python list (dynamic array).
    Provides O(1) push and pop operations.
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
    
    def push(self, item):
        """Add element to top of stack - O(1)"""
        if self.is_full():
            raise OverflowError("Stack is full")
        self._data.append(item)
    
    def pop(self):
        """Remove and return top element - O(1)"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._data.pop()
    
    def peek(self):
        """Return top element without removing - O(1)"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._data[-1]
    
    def clear(self):
        """Remove all elements from stack"""
        self._data.clear()
    
    def __str__(self):
        if self.is_empty():
            return "Stack: []"
        return "Stack (top → bottom): [" + ", ".join(str(x) for x in reversed(self._data)) + "]"

class LinkedStack:
    """
    Stack implementation using a singly linked list.
    Provides O(1) push and pop operations with no capacity limit.
    """
    
    class _Node:
        """Lightweight node class for linked stack"""
        def __init__(self, data, next_node=None):
            self.data = data
            self.next = next_node
    
    def __init__(self):
        self._top = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._top is None
    
    def push(self, item):
        """Add element to top of stack - O(1)"""
        self._top = self._Node(item, self._top)
        self._size += 1
    
    def pop(self):
        """Remove and return top element - O(1)"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        data = self._top.data
        self._top = self._top.next
        self._size -= 1
        return data
    
    def peek(self):
        """Return top element without removing - O(1)"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._top.data
    
    def clear(self):
        """Remove all elements from stack"""
        self._top = None
        self._size = 0
    
    def __str__(self):
        if self.is_empty():
            return "Stack: []"
        elements = []
        current = self._top
        while current:
            elements.append(str(current.data))
            current = current.next
        return "Stack (top → bottom): [" + ", ".join(elements) + "]"

class StackApplications:
    """Common stack application examples"""
    
    @staticmethod
    def is_balanced_parentheses(expression):
        """Check if parentheses/brackets are balanced - O(n)"""
        stack = ArrayStack()
        opening = "({["
        closing = ")}]"
        matches = {')': '(', '}': '{', ']': '['}
        
        for char in expression:
            if char in opening:
                stack.push(char)
            elif char in closing:
                if stack.is_empty():
                    return False
                if stack.pop() != matches[char]:
                    return False
        
        return stack.is_empty()
    
    @staticmethod
    def reverse_string(text):
        """Reverse a string using stack - O(n)"""
        stack = ArrayStack()
        for char in text:
            stack.push(char)
        
        result = []
        while not stack.is_empty():
            result.append(stack.pop())
        
        return ''.join(result)
    
    @staticmethod
    def evaluate_postfix(expression):
        """Evaluate postfix expression - O(n)"""
        stack = ArrayStack()
        operators = {'+', '-', '*', '/'}
        
        for token in expression.split():
            if token not in operators:
                stack.push(float(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.push(a + b)
                elif token == '-':
                    stack.push(a - b)
                elif token == '*':
                    stack.push(a * b)
                elif token == '/':
                    stack.push(a / b)
        
        return stack.pop()

# Example usage
if __name__ == "__main__":
    print("=== Array Stack Demo ===")
    stack = ArrayStack()
    
    # Push elements
    for i in [10, 20, 30, 40]:
        stack.push(i)
        print(f"Pushed {i}: {stack}")
    
    # Peek
    print(f"Top element: {stack.peek()}")
    
    # Pop elements
    while not stack.is_empty():
        popped = stack.pop()
        print(f"Popped {popped}: {stack}")
    
    print("\n=== Linked Stack Demo ===")
    linked_stack = LinkedStack()
    
    for i in ['A', 'B', 'C', 'D']:
        linked_stack.push(i)
        print(f"Pushed {i}: {linked_stack}")
    
    print(f"Size: {len(linked_stack)}")
    
    print("\n=== Stack Applications ===")
    
    # Balanced parentheses
    test_cases = ["((()))", "({[]})", "(()", "({[}])"]
    for expr in test_cases:
        result = StackApplications.is_balanced_parentheses(expr)
        print(f"'{expr}' is balanced: {result}")
    
    # Reverse string
    text = "Hello, World!"
    reversed_text = StackApplications.reverse_string(text)
    print(f"\nOriginal: {text}")
    print(f"Reversed: {reversed_text}")
    
    # Evaluate postfix
    postfix = "3 4 + 2 * 7 /"
    result = StackApplications.evaluate_postfix(postfix)
    print(f"\nPostfix: {postfix}")
    print(f"Result: {result}")
