import random
import unittest


def eApprox(n):
    """
    Approximates the constant e by simulating random number summation processes.

    The process sums random floats in the range (0, 1) until the sum exceeds 1.
    The expected number of such random variables is mathematically equal to e.

    Args:
        n (int): The number of independent simulations to perform.

    Returns:
        float: The average number of iterations required across all simulations.
    """
    total_iterations = 0

    for _ in range(n):
        current_sum = 0.0
        iterations = 0

        while current_sum <= 1.0:
            current_sum += random.random() # Accumulates a random float between 0 and 1.
            iterations += 1

        total_iterations += iterations

    return total_iterations / n # Calculates the mean to approximate the value of e.


class TestEApproximation(unittest.TestCase):
    """
    Verifies the accuracy of the e approximation function.

    Contains a test case to ensure the calculated value is within a reasonable
    error margin from Euler's number.
    """

    def test_e_approximation(self):
        """
        Validates that eApprox(1,000,000) is approximately equal to 2.718.
        """
        self.assertAlmostEqual(eApprox(1_000_000), 2.718, delta=0.001)


if __name__ == "__main__":
    unittest.main()
