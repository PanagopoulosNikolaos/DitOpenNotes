import time
from functools import cache
from sympy import fibonacci


@cache
def fibonacciCached(n: int) -> int:
    """
    Computes the n-th Fibonacci number using memoized recursion.

    Args:
        n (int): The index of the Fibonacci sequence.

    Returns:
        int: The Fibonacci number at index n.
    """
    if n <= 1:
        return n
    # Employs cached recursive calls to prevent redundant subproblem computation.
    return fibonacciCached(n - 1) + fibonacciCached(n - 2)

def sympyFibonacci(n: int) -> int:
    """
    Computes the n-th Fibonacci number using sympy library.

    Args:
        n (int): The index of the Fibonacci sequence.

    Returns:
        int: The Fibonacci number at index n.
    """
    return fibonacci(n)

def runExercise() -> None:
    """
    Measures the execution time of the cached Fibonacci implementation for index 50.
    """
    n = 991
    start = time.perf_counter()
    result = fibonacciCached(n)
    elapsed = time.perf_counter() - start

    print(f"With cache: n={n}, fib={result}, time={elapsed:.8f} sec")

    start = time.perf_counter()
    result = sympyFibonacci(n)
    elapsed = time.perf_counter() - start

    print(f"With sympy: n={n}, fib={result}, time={elapsed:.8f} sec")


if __name__ == "__main__":
    runExercise()
