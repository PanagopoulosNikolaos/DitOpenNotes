import unittest
from itertools import (
    count,
    combinations,
    product,
    accumulate,
    cycle,
    islice,
)


def firstNumbers(start: int, step: int, n: int) -> list[int]:
    """
    Generates the first n numbers of an arithmetic progression.

    Args:
        start (int): The starting number of the sequence.
        step (int): The difference between consecutive numbers.
        n (int): The total number of values to generate.

    Returns:
        list[int]: A list containing the first n generated numbers.
    """
    # Clips the infinite count generator using islice to obtain first n elements.
    return list(islice(count(start, step), n))


def pairCombinations(items: list) -> list[tuple]:
    """
    Finds all unique 2-element combinations of the provided items.

    Args:
        items (list): A list of elements to pair.

    Returns:
        list[tuple]: A list of tuples containing combinations of length 2.
    """
    # Computes unique pairs where order does not matter.
    return list(combinations(items, 2))


def cartesianProduct(a: list, b: list) -> list[tuple]:
    """
    Computes the cartesian product of two lists.

    Args:
        a (list): The first list.
        b (list): The second list.

    Returns:
        list[tuple]: A list of tuples representing the cartesian product.
    """
    # Computes the cross product of list a and list b.
    return list(product(a, b))


def cumulativeSums(numbers: list[int]) -> list[int]:
    """
    Computes the running totals of a sequence of numbers.

    Args:
        numbers (list[int]): A list of numerical values.

    Returns:
        list[int]: A list of cumulative sums.
    """
    # Generates cumulative sums step-by-step using accumulate.
    return list(accumulate(numbers))


def repeatPattern(pattern: list, n: int) -> list:
    """
    Repeats a list pattern until it reaches a total length of n.

    Args:
        pattern (list): The list sequence to cycle through.
        n (int): The total number of elements to produce.

    Returns:
        list: A list containing the repeated pattern of length n.
    """
    # Cycles through the base pattern and slices it to the desired length.
    return list(islice(cycle(pattern), n))


class TestItertools(unittest.TestCase):
    """
    Tests the itertools helper functions to ensure correctness.

    Provides unit tests checking arithmetic progressions, combinations,
    cartesian products, running totals, and pattern repetition.
    - testCount: Validates firstNumbers progression generation.
    - testCombinations: Validates pairCombinations output.
    - testProduct: Validates cartesianProduct output.
    - testAccumulate: Validates cumulativeSums output.
    - testCycle: Validates repeatPattern output.
    """

    def testCount(self) -> None:
        """
        Validates the output of firstNumbers function.
        """
        self.assertEqual(
            firstNumbers(0, 2, 5),
            [0, 2, 4, 6, 8]
        )

    def testCombinations(self) -> None:
        """
        Validates the output of pairCombinations function.
        """
        self.assertEqual(
            pairCombinations(["A", "B", "C"]),
            [("A", "B"), ("A", "C"), ("B", "C")]
        )

    def testProduct(self) -> None:
        """
        Validates the output of cartesianProduct function.
        """
        self.assertEqual(
            cartesianProduct([1, 2], ["x", "y"]),
            [(1, "x"), (1, "y"), (2, "x"), (2, "y")]
        )

    def testAccumulate(self) -> None:
        """
        Validates the output of cumulativeSums function.
        """
        self.assertEqual(
            cumulativeSums([1, 2, 3, 4]),
            [1, 3, 6, 10]
        )

    def testCycle(self) -> None:
        """
        Validates the output of repeatPattern function.
        """
        self.assertEqual(
            repeatPattern(["A", "B"], 5),
            ["A", "B", "A", "B", "A"]
        )


if __name__ == "__main__":
    unittest.main()
