"""Simulation of probability distributions and empirical Central Limit Theorem convergence.

Demonstrates random sampling, binomial probabilities, and the empirical convergence
of sample means toward Gaussian distributions using standard Python math routines.
"""

import math
import random


def computeBinomialPmf(n: int, k: int, p: float) -> float:
    """Calculates the exact binomial probability mass function P(X = k).

    Args:
        n (int): Total number of independent trials.
        k (int): Number of successful outcomes.
        p (float): Probability of success on an individual trial.

    Returns:
        float: Evaluated binomial probability P(X = k).
    """
    comb = math.comb(n, k)
    # Computes probability mass using exact exponential powers
    return comb * (p ** k) * ((1.0 - p) ** (n - k))


def simulateCentralLimitTheorem(sample_size: int = 30, num_experiments: int = 10000) -> tuple[float, float]:
    """Demonstrates CLT convergence by drawing samples from a uniform population.

    Args:
        sample_size (int): Number of observations per drawn sample.
        num_experiments (int): Total number of simulated sample mean trials.

    Returns:
        tuple[float, float]: Empirical mean and variance of the generated sample means.
    """
    random.seed(42)
    sample_means: list[float] = []

    for _ in range(num_experiments):
        # Draws sample from continuous Uniform(0, 1) population (mu = 0.5, var = 1/12)
        sample = [random.random() for _ in range(sample_size)]
        sample_mean = sum(sample) / sample_size
        sample_means.append(sample_mean)

    # Computes grand mean of sample means
    grand_mean = sum(sample_means) / num_experiments
    # Computes sample variance across sample means
    empirical_var = sum((x - grand_mean) ** 2 for x in sample_means) / (num_experiments - 1)

    return grand_mean, empirical_var


if __name__ == "__main__":
    print("=== Binomial Probability Mass Function ===")
    n_trials, p_success = 10, 0.3
    for k_val in range(n_trials + 1):
        pmf_val = computeBinomialPmf(n_trials, k_val, p_success)
        print(f"P(X = {k_val:2d}) = {pmf_val:.4f}")

    print("\n=== Central Limit Theorem Simulation ===")
    mean_val, var_val = simulateCentralLimitTheorem(sample_size=36, num_experiments=10000)
    theoretical_mean = 0.5
    theoretical_var = (1.0 / 12.0) / 36 # Population variance (1/12) divided by n (36)
    print(f"Simulated Grand Mean: {mean_val:.4f} (Theoretical: {theoretical_mean:.4f})")
    print(f"Simulated Variance:   {var_val:.6f} (Theoretical: {theoretical_var:.6f})")

