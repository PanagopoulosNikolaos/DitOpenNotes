import unittest

class Stack:
    """
    A Last-In-First-Out (LIFO) stack implementation using a list.

    Provides core stack operations including push, pop, and clear.
    - __init__: Initializes an empty data list.
    - push: Appends an element to the top of the stack.
    - pop: Removes and returns the top element.
    - clear: Removes all elements from the stack.
    - __str__: Returns a formatted string representing the stack state.
    """

    def __init__(self):
        """
        Initializes an empty stack.
        """
        self.data = []

    def push(self, item: any):
        """
        Adds an item to the top of the stack.
        Args:
            item (any): The item to be added.
        """
        # Appends the new item to the end of the list, treating it as the stack top.
        self.data.append(item)

    def pop(self) -> any:
        """
        Removes and returns the top item from the stack.
        Returns:
            any: The item removed, or None if empty.
        """
        if self.data:
            # Removes the last element added to maintain LIFO order.
            return self.data.pop()
        return None

    def clear(self):
        """
        Clears all items from the stack.
        """
        # Re-initializes the data list to effectively empty the stack.
        self.data = []

    def __str__(self) -> str:
        """
        Provides a visual representation of the stack.
        Returns:
            str: A formatted string showing items from top to bottom.
        """
        if not self.data:
            return "Η στοίβα δεν περιέχει στοιχεία"
        
        output_lines = []
        # Iterates backwards through the list to display the top element first.
        for index in range(len(self.data) - 1, -1, -1):
            # Identifies the top element with an arrow indicator.
            prefix = "->" if index == len(self.data) - 1 else "  "
            output_lines.append(f"{prefix}{self.data[index]}")
            
        return "\n".join(output_lines) + "\n"

# Mην αλλάξετε κάτι από εδώ και κάτω
class TestStack(unittest.TestCase):
    """
    Unit tests for validating Stack functionality.
    """

    def testStack(self):
        """
        Tests push, pop, and string representation of the Stack.
        """
        s = Stack()
        self.assertTrue(str(s) == "Η στοίβα δεν περιέχει στοιχεία")
        s.push(1)
        self.assertTrue(str(s) == "->1\n")
        s.push(2)
        self.assertTrue(str(s) == "->2\n  1\n")
        s.push(3)
        self.assertTrue(str(s) == "->3\n  2\n  1\n")
        s.pop()
        self.assertTrue(str(s) == "->2\n  1\n")

if __name__ == "__main__":
    unittest.main()
