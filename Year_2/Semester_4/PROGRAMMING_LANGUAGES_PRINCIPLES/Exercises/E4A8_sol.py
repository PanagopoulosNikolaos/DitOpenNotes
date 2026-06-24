class TodoItem:
    """
    Represents a single task in a to-do list.

    - __init__: Initializes the task description and sets completed to False.
    - toggle: Flips the completion status.
    - __repr__: Returns a string format 'description=X completed=Y'.
    """

    def __init__(self, description: str):
        """
        Initializes a TodoItem instance.
        Args:
            description (str): The text of the task.
        """
        self.description = description
        self.completed = False

    def toggle(self):
        """
        Toggles the completion status of the task.
        """
        # Switches the boolean state from True to False or vice-versa.
        self.completed = not self.completed

    def __repr__(self) -> str:
        """
        Returns the formal string representation of the task.
        Returns:
            str: Task details for list representation.
        """
        return f"description={self.description} completed={self.completed}"


class TodoList:
    """
    Manages a collection of TodoItem objects.

    - __init__: Initializes the list name and an empty items list.
    - add: Appends a new TodoItem to the collection.
    - stats: Returns a dictionary with counts of open and completed tasks.
    """

    def __init__(self, name: str):
        """
        Initializes a TodoList instance.
        Args:
            name (str): The name of the list (e.g., 'groceries').
        """
        self.name = name
        self.todos = []

    def add(self, description: str):
        """
        Adds a new task to the list.
        Args:
            description (str): The task description.
        """
        # Instantiates a TodoItem and adds it to the internal storage.
        self.todos.append(TodoItem(description))

    def stats(self) -> dict:
        """
        Calculates the number of open and completed tasks.
        Returns:
            dict: Counts for 'open' and 'completed' items.
        """
        # Aggregates completion states to provide a summary of the list's progress.
        completed_count = sum(1 for item in self.todos if item.completed)
        open_count = len(self.todos) - completed_count
        
        stats_dict = {'open': open_count, 'completed': completed_count}
        print(stats_dict)
        return stats_dict

def runExercise():
    """
    Demonstrates the functionality of the TodoList and TodoItem classes.
    """
    tdl = TodoList("groceries")
    tdl.add("milk")
    tdl.add("bread")
    
    # Displays the current items in the to-do list.
    print(tdl.todos) # [description=milk completed=False, description=bread completed=False]
    
    # Marks the first item as done.
    tdl.todos[0].toggle()
    
    # Shows the statistics of the list.
    tdl.stats() # {'open': 1, 'completed': 1}

if __name__ == "__main__":
    runExercise()
