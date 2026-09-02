# ==============================================================================
# Statistical Hypothesis Testing and Confidence Intervals in R
# ==============================================================================
# Implements one-sample and two-sample Student t-tests, z-tests, and
# confidence intervals for population means and proportions.
# ==============================================================================

calculateOneSampleTest <- function(sample_data, null_mean, alpha = 0.05) {
  n <- length(sample_data)
  sample_mean <- mean(sample_data)
  sample_sd <- sd(sample_data)
  se <- sample_sd / sqrt(n)

  # Calculates t test statistic
  t_statistic <- (sample_mean - null_mean) / se
  degrees_of_freedom <- n - 1

  # Two-tailed p-value
  p_value <- 2 * (1 - pt(abs(t_statistic), df = degrees_of_freedom))

  # 1 - alpha Confidence Interval
  t_critical <- qt(1 - alpha / 2, df = degrees_of_freedom)
  ci_lower <- sample_mean - t_critical * se
  ci_upper <- sample_mean + t_critical * se

  cat("--- One-Sample t-Test ---\n")
  cat("Sample Size (n):", n, "\n")
  cat("Sample Mean:", round(sample_mean, 4), "\n")
  cat("Null Hypothesis Mean (mu0):", null_mean, "\n")
  cat("t-Statistic:", round(t_statistic, 4), "\n")
  cat("Degrees of Freedom:", degrees_of_freedom, "\n")
  cat("p-Value:", format.pval(p_value, digits = 5), "\n")
  cat(sprintf("%.0f%% Confidence Interval: [%.4f, %.4f]\n", (1 - alpha) * 100, ci_lower, ci_upper))
  
  if (p_value < alpha) {
    cat("Decision: Reject H0 at alpha =", alpha, "\n\n")
  } else {
    cat("Decision: Fail to reject H0 at alpha =", alpha, "\n\n")
  }

  return(list(t_stat = t_statistic, p_val = p_value, ci = c(ci_lower, ci_upper)))
}

# Example run
synthetic_measurements <- c(102.3, 98.7, 101.5, 103.1, 99.8, 104.0, 102.6, 100.9, 101.8, 103.5)
calculateOneSampleTest(synthetic_measurements, null_mean = 100.0, alpha = 0.05)

