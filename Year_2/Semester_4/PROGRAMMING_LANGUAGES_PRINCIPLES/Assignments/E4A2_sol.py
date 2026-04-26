class Juice:
    """
    Represents a juice beverage with name, capacity, and price attributes.

    Provides functionality for mixing juices and pouring out portions.
    - __init__: Initializes name, capacity, and price.
    - __str__: Formats the juice information for display.
    - __add__: Mixes two juices together.
    - pour: Extracts a percentage of the juice into a new instance.
    """

    def __init__(self, name: str, capacity: float, price: float):
        """
        Initializes a Juice instance.
        Args:
            name (str): The name of the juice flavor.
            capacity (float): The volume in liters.
            price (float): The cost of the juice.
        """
        self.name = name
        self.capacity = capacity
        self.price = price

    def __str__(self) -> str:
        """
        Returns a formatted string representing the juice.
        Returns:
            str: Juice details including name, volume, and price.
        """
        return f"{self.name} ({self.capacity}L) - {self.price:.2f}€"

    def __add__(self, other: 'Juice') -> 'Juice':
        """
        Combines two Juice instances into a new one.
        Args:
            other (Juice): The other juice to mix with.
        Returns:
            Juice: A new instance with summed capacities, prices, and joined names.
        """
        # Creates a composite juice by aggregating values from both ingredients.
        return Juice(
            f"{self.name}&{other.name}",
            self.capacity + other.capacity,
            self.price + other.price
        )

    def pour(self, percentage: float) -> 'Juice':
        """
        Creates a new Juice instance representing a fraction of the current one.
        Args:
            percentage (float): The portion to take (0-100).
        Returns:
            Juice: A new juice object with the scaled capacity and price.
        """
        # Calculates the fractional volume based on the provided percentage.
        new_capacity = self.capacity * (percentage / 100.0)
        # Scales the price proportionally to the extracted volume.
        new_price = self.price * (percentage / 100.0)
        return Juice(self.name, new_capacity, new_price)

def runExercise():
    """
    Demonstrates Juice class functionality: addition and pouring.
    """
    juice_a = Juice('Orange', 1.5, 2.5)
    juice_b = Juice('Apple', 2.0, 3.0)
    
    # Combines two juices to test operator overloading.
    mixed_juice = juice_a + juice_b
    print(f"Mixed: {mixed_juice}")
    
    # Extracts a portion of the mixed juice to test the pour method.
    poured_juice = mixed_juice.pour(50)
    print(f"Poured (50%): {poured_juice}")

if __name__ == "__main__":
    runExercise()
