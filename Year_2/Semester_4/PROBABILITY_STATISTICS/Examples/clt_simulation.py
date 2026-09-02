"""Monte Carlo simulation demonstrating the Central Limit Theorem.

Draws repeated random samples from a non-normal exponential distribution,
computes sample means, and illustrates convergence towards a Normal distribution.
"""

import math
import random


def simulateCentralLimitTheorem(
    sample_sizes: list[int] = None, num_simulations: int = 10000
) -> dict:
    """Simulates sample mean convergence under increasing sample sizes.

    Args:
        sample_sizes (list[int]): List of sample sizes n to evaluate.
        num_simulations (int): Number of Monte Carlo iterations per sample size.

    Returns:
        dict: Empirical statistics mapping sample sizes to mean and standard error.
    """
    if sample_sizes is None:
        sample_sizes = [2, 5, 30, 100]

    # Uses an exponential distribution with rate lambda = 0.5.
    lambda_param = 0.5
    true_mean = 1.0 / lambda_param  # Theoretical E[X] = 2.0
    true_sd = 1.0 / lambda_param  # Theoretical SD[X] = 2.0

    print(f"Population Distribution: Exponential(lambda={lambda_param})")
    print(f"Theoretical Mean: {true_mean:.4f}, Theoretical SD: {true_sd:.4f}\n")

    empirical_results = {}
    random.seed(42)

    for n in sample_sizes:
        sample_means = []
        for _ in range(num_simulations):
            # Draws n i.i.d. observations from Exp(lambda).
            sample = [random.expovariate(lambda_param) for _ in range(n)]
            sample_means.append(sum(sample) / n)

        mean_of_means = sum(sample_means) / num_simulations
        variance = sum((x - mean_of_means) ** 2 for x in sample_means) / (
            num_simulations - 1
        )
        sd_of_means = math.sqrt(variance)
        theoretical_se = true_sd / math.sqrt(n)

        empirical_results[n] = {
            "empirical_mean": mean_of_means,
            "empirical_se": sd_of_means,
            "theoretical_se": theoretical_se,
        }

        print(
            f"Sample Size n = {n:3d} | Mean: {mean_of_means:.4f} (True: {true_mean:.4f}) | "
            f"SE: {sd_of_means:.4f} (Theory SE: {theoretical_se:.4f})"
        )

    return empirical_results


if __name__ == "__main__":
    simulateCentralLimitTheorem()

