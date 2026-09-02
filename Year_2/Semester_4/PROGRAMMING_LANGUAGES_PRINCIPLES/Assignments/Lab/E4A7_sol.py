class Length:
    """
    Represents a physical length with a value and a unit (cm or in).

    Supports unit-aware addition and multiple string representations.
    - __init__: Initializes value and unit.
    - __str__: Formats the length as 'value.unit'.
    - __repr__: Returns a detailed representation 'value=X unit=Y'.
    - __add__: Adds two Length objects, converting to cm if units differ.
    """

    def __init__(self, value: float, unit: str):
        """
        Initializes a Length instance.
        Args:
            value (float): The numeric value of the length.
            unit (str): The unit of measurement ('cm' or 'in').
        """
        self.value = value
        self.unit = unit

    def __str__(self) -> str:
        """
        Returns a concise string representation.
        Returns:
            str: Formatted value and unit.
        """
        return f"{self.value:.2f}{self.unit}"

    def __repr__(self) -> str:
        """
        Returns a detailed string for debugging.
        Returns:
            str: Field names and values.
        """
        return f"value={self.value} unit={self.unit}"

    def __add__(self, other: 'Length') -> 'Length':
        """
        Adds two length objects together.
        Args:
            other (Length): The length to add.
        Returns:
            Length: A new Length object with the summed value.
        """
        if self.unit == other.unit:
            # Performs direct addition if units are already identical.
            return Length(self.value + other.value, self.unit)
        
        # Standardizes both values to centimeters if units are mismatched.
        val1 = self.value * 2.54 if self.unit == "in" else self.value
        val2 = other.value * 2.54 if other.unit == "in" else other.value
        
        # Returns the result in centimeters as the fallback common unit.
        return Length(val1 + val2, "cm")

def runExercise():
    """
    Demonstrates Length object creation, representation, and addition.
    """
    print("Εκτύπωση αντικειμένου με τη μέθοδο __str__ (3 τρόποι)")
    len1 = Length(5.5, "cm")
    print(len1)
    print(str(len1))
    print(f"{len1}")
    
    print("Εκτύπωση αντικειμένου με τη μέθοδο __repr__ (2 τρόποι)")
    len2 = Length(3.0, "in")
    print(repr(len2))
    print(f"{len2!r}")
    
    print("Υπερφόρτωση τελεστή +")
    result = len1 + len2
    print(f"{len1} + {len2} = {result}")

if __name__ == "__main__":
    runExercise()
