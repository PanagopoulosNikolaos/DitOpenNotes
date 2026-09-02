# ==============================================================================
# Monte Carlo Simulation of the Central Limit Theorem (CLT) in R
# ==============================================================================
# Demonstrates that the distribution of the sample mean converges to a Normal
# distribution as sample size increases, regardless of the underlying distribution.
# ==============================================================================

set.seed(42)

simulateCentralLimitTheorem <- function(sample_sizes = c(2, 5, 30, 100), num_simulations = 10000) {
  # True parameters for an Exponential distribution with rate lambda = 0.5
  lambda_rate <- 0.5
  true_mean <- 1 / lambda_rate       # E[X] = 2
  true_sd <- 1 / lambda_rate         # SD[X] = 2

  cat("Theoretical Population Mean:", true_mean, "\n")
  cat("Theoretical Population SD:", true_sd, "\n\n")

  results <- list()

  for (n in sample_sizes) {
    # Draws num_simulations samples of size n from Exp(lambda)
    sample_matrix <- matrix(rexp(n * num_simulations, rate = lambda_rate),
                            nrow = num_simulations, ncol = n)

    # Computes sample mean across rows
    sample_means <- rowMeans(sample_matrix)

    # Standardizes the sample means
    theoretical_se <- true_sd / sqrt(n)
    z_scores <- (sample_means - true_mean) / theoretical_se

    results[[as.character(n)]] <- list(
      sample_size = n,
      mean_of_means = mean(sample_means),
      sd_of_means = sd(sample_means),
      expected_se = theoretical_se,
      z_mean = mean(z_scores),
      z_sd = sd(z_scores)
    )

    cat(sprintf("Sample Size n = %3d | Mean: %.4f (Exp: %.4f) | SE: %.4f (Exp: %.4f) | Z-score SD: %.4f\n",
                n, mean(sample_means), true_mean, sd(sample_means), theoretical_se, sd(z_scores)))
  }

  return(results)
}

# Run simulation
cat("Running Central Limit Theorem Monte Carlo Simulation...\n")
sim_results <- simulateCentralLimitTheorem()
cat("Simulation finished.\n")

