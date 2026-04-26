class Interval:
    """
    Represents a numeric interval [from, to).

    Maintains a count of valid instances and allows dynamic length adjustment.
    - __init__: Initializes boundaries and validates range.
    - length (property): Gets or sets the length of the interval.
    - __str__: Returns a string with the length.
    - __repr__: Returns a formal representation of the interval boundaries.
    - numberOfIntervals: Returns the total count of valid Interval instances.
    """
    
    _cnt = 0

    def __init__(self, from_val: float, to_val: float):
        """
        Initializes an Interval instance.
        Args:
            from_val (float): Start of the interval.
            to_val (float): End of the interval.
        Raises:
            ValueError: If from_val is greater than or equal to to_val.
        """
        if from_val >= to_val:
            # Enforces the mathematical requirement that the start must precede the end.
            raise ValueError("Η τιμή 'από' πρέπει να είναι μικρότερη από την τιμή 'έως'.")
        
        self._from = from_val
        self._to = to_val
        # Increments the class-level counter only for successfully initialized objects.
        Interval._cnt += 1

    @property
    def length(self) -> float:
        """
        Gets the length of the interval.
        Returns:
            float: The difference between _to and _from.
        """
        return self._to - self._from

    @length.setter
    def length(self, value: float):
        """
        Sets the length of the interval by adjusting the _to boundary.
        Args:
            value (float): The new length.
        """
        # Updates the upper bound while keeping the starting point fixed.
        self._to = self._from + value

    def __str__(self) -> str:
        """
        Returns a string representation of the interval's length.
        Returns:
            str: Description of the length.
        """
        return f"Μήκος διαστήματος: {self.length}"

    def __repr__(self) -> str:
        """
        Returns the formal representation showing the boundaries.
        Returns:
            str: Representation in [from, to) format.
        """
        return f"Interval({self._from}, {self._to})"

    @staticmethod
    def numberOfIntervals() -> int:
        """
        Returns the total number of Interval objects created.
        Returns:
            int: The value of the private class counter.
        """
        return Interval._cnt

def runExercise():
    """
    Collects 5 intervals, handles errors, and demonstrates property updates.
    """
    for i in range(5):
        try:
            print(f"\nΕίσοδος δεδομένων για το διάστημα {i+1}:")
            f_val = float(input("Από: "))
            t_val = float(input("Έως: "))
            
            interval = Interval(f_val, t_val)
            print(interval)
            
            # Resizes the interval to a length of 10 to demonstrate the setter logic.
            interval.length = 10
            print(f"Μετά την αλλαγή μήκους σε 10: {repr(interval)}")
            
        except ValueError as e:
            # Catches validation errors to prevent the program from crashing on bad input.
            print(f"Σφάλμα: {e}")

    print(f"\nΣυνολικά έγκυρα διαστήματα: {Interval.numberOfIntervals()}")

if __name__ == "__main__":
    runExercise()
