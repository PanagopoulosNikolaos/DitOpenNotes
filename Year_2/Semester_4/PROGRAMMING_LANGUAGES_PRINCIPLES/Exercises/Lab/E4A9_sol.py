import random

class Dice:
    """
    Represents a dice with customizable side probabilities.

    Supports rolling, expected value calculation, and combining dice.
    - __init__: Initializes with a probability dictionary.
    - roll: Simulates n rolls based on weights.
    - expectedValue (property): Calculates the theoretical mean.
    - fromSides (classmethod): Creates a fair die with a given number of sides.
    - __len__: Returns the number of distinct sides.
    - __add__: Combines two dice into a new one representing their sum.
    """

    def __init__(self, probs: dict):
        """
        Initializes a Dice instance.
        Args:
            probs (dict): Dictionary mapping side value to probability.
        """
        self.probs = probs

    def roll(self, n: int = 1) -> list:
        """
        Simulates rolling the die multiple times.
        Args:
            n (int): Number of rolls to perform. Default is 1.
        Returns:
            list: The results of the rolls.
        """
        sides = list(self.probs.keys())
        weights = list(self.probs.values())
        # Uses weighted selection to respect the probability distribution.
        return random.choices(sides, weights=weights, k=n)

    @property
    def expectedValue(self) -> float:
        """
        Calculates the expected value (mean) of the die.
        Returns:
            float: The sum of (side * probability) for all sides.
        """
        # Sums the product of each side and its likelihood.
        return sum(side * prob for side, prob in self.probs.items())

    @classmethod
    def fromSides(cls, sides: int) -> 'Dice':
        """
        Creates a fair die with the specified number of sides.
        Args:
            sides (int): Number of sides (e.g., 6).
        Returns:
            Dice: A new Dice instance with equal probabilities.
        """
        # Distributes probability evenly across all integer values from 1 to sides.
        prob = 1.0 / sides
        equal_probs = {i: prob for i in range(1, sides + 1)}
        return cls(equal_probs)

    def __len__(self) -> int:
        """
        Returns the number of sides the die has.
        Returns:
            int: Count of keys in the probability dictionary.
        """
        return len(self.probs)

    def __add__(self, other: 'Dice') -> 'Dice':
        """
        Creates a new 'die' representing the sum of two dice.
        Args:
            other (Dice): The other die to add.
        Returns:
            Dice: A new die with probabilities of sums.
        """
        new_probs = {}
        # Iterates through all possible combinations of outcomes to calculate sum probabilities.
        for side1, prob1 in self.probs.items():
            for side2, prob2 in other.probs.items():
                total_side = side1 + side2
                # Multiplies probabilities for independent events (rolling two dice).
                new_probs[total_side] = new_probs.get(total_side, 0) + (prob1 * prob2)
        
        return Dice(new_probs)

def runExercise():
    """
    Demonstrates Dice operations: fair dice, rolling, and addition.
    """
    # Creates two standard 6-sided dice.
    d6_a = Dice.fromSides(6)
    d6_b = Dice.fromSides(6)
    
    print(f"Expected value of 1d6: {d6_a.expectedValue}")
    print(f"Sides in 1d6: {len(d6_a)}")
    
    # Combines them to represent 2d6.
    d12_sum = d6_a + d6_b
    print(f"Expected value of 2d6: {d12_sum.expectedValue}")
    print(f"Possible sums in 2d6: {len(d12_sum)}")
    
    # Simulates rolling 2d6 five times.
    results = d12_sum.roll(5)
    print(f"5 rolls of 2d6: {results}")

if __name__ == "__main__":
    runExercise()
