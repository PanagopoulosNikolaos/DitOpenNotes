class Cylinder:
    """
    Represents a cylinder with radius and height.

    Calculates volume and provides string representation.
    - __init__: Initializes private radius and height.
    - calculateVolume: Computes the volume of the cylinder.
    - __str__: Returns details in (radius, height, volume) format.
    """

    def __init__(self, radius: float, height: float):
        """
        Initializes a Cylinder instance.
        Args:
            radius (float): The radius of the base.
            height (float): The height of the cylinder.
        """
        self._radius = radius
        self._height = height

    def calculateVolume(self) -> float:
        """
        Calculates the volume of the cylinder using V = π * r^2 * h.
        Returns:
            float: The calculated volume.
        """
        # Uses the specified constant 3.14 for pi as per instructions.
        return 3.14 * (self._radius ** 2) * self._height

    def __str__(self) -> str:
        """
        Returns a string representation of the cylinder.
        Returns:
            str: (radius, height, volume) formatted string.
        """
        # Formats the calculated volume to two decimal places for clarity.
        return f"({self._radius}, {self._height}, {self.calculateVolume():.2f})"

def runExercise():
    """
    Collects 5 cylinders from user input, sorts them by volume descending, and displays them.
    """
    cylinders = []
    # Collects five sets of dimensions from the user to populate the list.
    for i in range(5):
        try:
            print(f"Εισαγωγή στοιχείων για τον κύλινδρο {i+1}:")
            radius = float(input("Ακτίνα: "))
            height = float(input("Ύψος: "))
            cylinders.append(Cylinder(radius, height))
        except ValueError:
            print("Μη έγκυρη τιμή. Παρακαλώ εισάγετε αριθμούς.")
            continue

    # Sorts the cylinders in descending order of volume to highlight the largest first.
    cylinders.sort(key=lambda cyl: cyl.calculateVolume(), reverse=True)

    print("\nΤαξινομημένοι κύλινδροι (φθίνουσα σειρά όγκου):")
    for cyl in cylinders:
        print(cyl)

if __name__ == "__main__":
    runExercise()
