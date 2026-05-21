def fibonacci(n: int) -> int:
    """
    Computes the n-th Fibonacci number recursively.

    Args:
        n (int): The index of the Fibonacci sequence.

    Returns:
        int: The Fibonacci number at index n.
    """
    if n <= 1:
        return n
    # Performs exponential recursive branching to compute Fibonacci sequence value.
    return fibonacci(n - 1) + fibonacci(n - 2)


def runExercise() -> None:
    """
    Runs the recursive Fibonacci computation for index 40.
    """
    x = fibonacci(40)
    print(x)


if __name__ == "__main__":
    runExercise()
