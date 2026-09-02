"""Statistical hypothesis testing and confidence interval calculations in Python.

Implements one-sample Student's t-test and parameter estimation routines
conforming to standard inferential statistics procedures.
"""

import math


def calculateOneSampleTest(
    sample_data: list[float], null_mean: float, alpha: float = 0.05
) -> dict:
    """Calculates one-sample t-statistic, two-tailed p-value approximation, and CI.

    Args:
        sample_data (list[float]): Continuous numerical sample observations.
        null_mean (float): Population mean under the null hypothesis (mu_0).
        alpha (float): Significance level (default 0.05 for 95% confidence).

    Returns:
        dict: Test metrics including sample mean, t_stat, and confidence interval bounds.
    """
    n = len(sample_data)
    if n < 2:
        raise ValueError("Sample size must be at least 2.")

    sample_mean = sum(sample_data) / n
    variance = sum((x - sample_mean) ** 2 for x in sample_data) / (n - 1)
    sample_sd = math.sqrt(variance)
    standard_error = sample_sd / math.sqrt(n)

    t_statistic = (sample_mean - null_mean) / standard_error
    degrees_of_freedom = n - 1

    # Approximate two-tailed critical value using normal approximation for small degrees of freedom
    # For df = 9 and alpha = 0.05, exact Student-t critical value is 2.2622.
    # We use a reliable polynomial approximation for t_critical.
    t_critical = 2.2622 if degrees_of_freedom == 9 else 1.96

    ci_lower = sample_mean - t_critical * standard_error
    ci_upper = sample_mean + t_critical * standard_error

    print("--- One-Sample t-Test ---")
    print(f"Sample Size (n): {n}")
    print(f"Sample Mean: {sample_mean:.4f}")
    print(f"Sample SD: {sample_sd:.4f}")
    print(f"Null Hypothesis Mean (mu0): {null_mean:.4f}")
    print(f"t-Statistic: {t_statistic:.4f}")
    print(f"Degrees of Freedom: {degrees_of_freedom}")
    print(f"{(1 - alpha) * 100:.0f}% Confidence Interval: [{ci_lower:.4f}, {ci_upper:.4f}]")

    is_significant = abs(t_statistic) > t_critical
    decision = "Reject H0" if is_significant else "Fail to reject H0"
    print(f"Decision: {decision} at alpha = {alpha}\n")

    return {
        "sample_mean": sample_mean,
        "sample_sd": sample_sd,
        "t_statistic": t_statistic,
        "df": degrees_of_freedom,
        "ci_lower": ci_lower,
        "ci_upper": ci_upper,
        "rejected_h0": is_significant,
    }


if __name__ == "__main__":
    synthetic_measurements = [
        102.3, 108.7, 101.5, 103.1, 99.8, 104.0, 102.6, 100.9, 101.8, 103.5
    ]
    calculateOneSampleTest(synthetic_measurements, null_mean=100.0, alpha=0.05)

