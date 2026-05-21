from collections.abc import Generator


def runningTotals(numbers: list[int]) -> Generator[int, None, None]:
    """
    Yields the running cumulative sum of numbers.

    Args:
        numbers (list[int]): A list of numerical values.

    Yields:
        int: The cumulative sum calculated up to the current element.
    """
    total = 0
    for n in numbers:
        total += n
        yield total


def runExercise() -> None:
    """
    Demonstrates the runningTotals generator with a sample list of integers.
    """
    numbers = [4, 7, 2, 10]
    # Iterates over each running total yielded by the generator function.
    for value in runningTotals(numbers):
        print(value)


if __name__ == "__main__":
    runExercise()
