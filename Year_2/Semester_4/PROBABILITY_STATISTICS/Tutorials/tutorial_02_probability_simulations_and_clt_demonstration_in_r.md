# Tutorial 02: Probability Distributions and CLT Demonstration in R

This laboratory tutorial demonstrates how to use R's built-in distribution families (`dbinom`, `pbinom`, `rbinom`, `dnorm`, `pnorm`, `qnorm`, `rnorm`) and implements a Monte Carlo simulation verifying the Central Limit Theorem.

---

## 1. Probability Distribution Functions in R

R distribution functions use standard prefixes:
- `d<name>`: Density / Probability Mass Function ($P(X = x)$ or $f(x)$).
- `p<name>`: Cumulative Distribution Function ($F(x) = P(X \le x)$).
- `q<name>`: Quantile function (inverse CDF, $F^{-1}(p)$).
- `r<name>`: Pseudorandom number generation from the distribution.

### 1.1 The Binomial Family: `binom`
Let $X \sim B(n = 20, p = 0.35)$:

```R
# P(X = 6): Exactly 6 successes
prob_exact_6 <- dbinom(x = 6, size = 20, prob = 0.35)

# P(X <= 5): At most 5 successes
prob_at_most_5 <- pbinom(q = 5, size = 20, prob = 0.35)

# P(X >= 8) = 1 - P(X <= 7): At least 8 successes
prob_at_least_8 <- 1 - pbinom(q = 7, size = 20, prob = 0.35)
# or using lower.tail = FALSE:
prob_at_least_8_alt <- pbinom(q = 7, size = 20, prob = 0.35, lower.tail = FALSE)
```

### 1.2 The Normal Family: `norm`
Let $X \sim N(\mu = 100, \sigma = 15)$:

```R
# P(X <= 115)
prob_norm_le_115 <- pnorm(q = 115, mean = 100, sd = 15)

# 95th Percentile: find x such that P(X <= x) = 0.95
x_95 <- qnorm(p = 0.95, mean = 100, sd = 15)

# Standard normal critical value z_0.025 for a two-tailed 95% CI
z_crit <- qnorm(p = 0.975, mean = 0, sd = 1) # Yields 1.959964
```

---

## 2. Central Limit Theorem Monte Carlo Simulation

Simulate drawing $M = 10,000$ samples of size $n$ from a highly skewed Exponential distribution ($\text{Exp}(\lambda = 1)$ where $\mu = 1, \sigma = 1$):

```R
set.seed(42) # Ensure reproducible simulation results

# Simulation parameters
num_experiments <- 10000
sample_sizes <- c(2, 10, 30, 100)

par(mfrow = c(2, 2)) # Arrange plots in 2x2 grid

for (n in sample_sizes) {
  # Generate matrix of simulated values: num_experiments rows, n columns
  samples <- matrix(rexp(num_experiments * n, rate = 1.0),
                    nrow = num_experiments,
                    ncol = n)

  # Compute row means: vector of 10,000 sample means
  sample_means <- rowMeans(samples)

  # Plot distribution of sample means
  hist(sample_means,
       breaks = 40,
       freq = FALSE,
       col = "lightgray",
       main = paste("CLT Convergence (n =", n, ")"),
       xlab = "Sample Mean")

  # Theoretical normal curve: Mean = 1, SD = 1 / sqrt(n)
  curve(dnorm(x, mean = 1, sd = 1 / sqrt(n)),
        add = TRUE,
        col = "blue",
        lwd = 2)
}
```
**Observation:** Even with an underlying exponential population, as sample size $n$ increases from $2$ to $30$ and $100$, the distribution of the sample mean converges to the theoretical Gaussian curve.

