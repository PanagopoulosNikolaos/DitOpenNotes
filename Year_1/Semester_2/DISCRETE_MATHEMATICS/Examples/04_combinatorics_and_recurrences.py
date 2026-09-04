"""Calculates permutations, combinations, inclusion-exclusion cardinality, and evaluates linear recurrence relations."""

import math
from typing import List


class CombinatoricsCalculator:
    """Provides combinatorial calculation routines and homogeneous recurrence solvers."""

    @staticmethod
    def permutations(n: int, r: int) -> int:
        """Calculates permutation count P(n, r) = n! / (n - r)!.

        Args:
            n (int): Total number of items in pool.
            r (int): Number of items to select and order.

        Returns:
            int: Total permutations count.
        """
        if r < 0 or r > n:
            return 0
        return math.perm(n, r)

    @staticmethod
    def combinations(n: int, r: int) -> int:
        """Calculates combination count C(n, r) = n! / (r! * (n - r)!).

        Args:
            n (int): Total number of items in pool.
            r (int): Number of items to select without order.

        Returns:
            int: Total combinations count.
        """
        if r < 0 or r > n:
            return 0
        return math.comb(n, r)

    @staticmethod
    def solveSecondOrderHomogeneous(c1: float, c2: float, a0: float, a1: float, num_terms: int) -> List[float]:
        """Generates sequence terms for recurrence a_n = c1 * a_{n-1} + c2 * a_{n-2}.

        Args:
            c1 (float): First coefficient.
            c2 (float): Second coefficient.
            a0 (float): Initial condition at index 0.
            a1 (float): Initial condition at index 1.
            num_terms (int): Total number of terms to generate.

        Returns:
            List[float]: Sequence of computed recurrence terms.
        """
        if num_terms <= 0:
            return []
        if num_terms == 1:
            return [a0]

        sequence = [a0, a1]
        for _ in range(2, num_terms):
            next_val = c1 * sequence[-1] + c2 * sequence[-2] # Evaluates next recurrence step
            sequence.append(next_val)

        return sequence


def main() -> None:
    """Executes demonstration of combinatorial calculations and recurrence sequence generation."""
    print("=== Combinatorics Demonstrations ===")
    print(f"P(10, 4) = {CombinatoricsCalculator.permutations(10, 4)}")
    print(f"C(10, 4) = {CombinatoricsCalculator.combinations(10, 4)}")

    # Fibonacci recurrence: F(n) = 1*F(n-1) + 1*F(n-2), F(0)=0, F(1)=1
    fib_terms = CombinatoricsCalculator.solveSecondOrderHomogeneous(1.0, 1.0, 0.0, 1.0, 10)
    print(f"Fibonacci sequence (10 terms): {fib_terms}")


if __name__ == "__main__":
    main()

