import time


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
    Measures computation time for recursive Fibonacci until execution exceeds 10 seconds.
    """
    n = 0
    while True:
        start = time.perf_counter()
        result = fibonacci(n)
        elapsed = time.perf_counter() - start

        print(f"n={n}, fib={result}, time={elapsed:.4f} sec")

        # Terminates the search when a calculation exceeds the 10-second threshold.
        if elapsed > 10.0:
            break

        n += 1


if __name__ == "__main__":
    runExercise()
