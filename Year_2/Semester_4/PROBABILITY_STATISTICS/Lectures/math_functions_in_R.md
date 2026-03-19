## Math Functions in R

* `log(x)` : Returns the logarithm of a variable
* `exp(x)` : Returns exponential of a variable
* `max(x)` : Returns the maximum value of a vector
* `min(x)` : Returns the minimum value of a vector
* `mean(x)` : Returns the mean of a vector
* `sum(x)` : Returns the sum of a vector
* `median(x)` : Returns the median of a vector
* `quantile(x)` : Percentage quantiles of a vector
* `round(x, n)` : Round to n decimal places
* `rank(x)` : Rank of elements in a vector
* `signif(x, n)` : Round off n significant figures
* `var(x)` : Variance of a vector
* `cor(x, y)` : Correlation between two vectors
* `sd(x)` : Standard deviation of a vector

---

### Exercises: Probability and Statistics in R

1. **Calculate the mean and median of the vector `x <- c(2, 4, 4, 4, 5, 5, 7, 9)`.**
   - **Solution:**
     ```R
     x <- c(2, 4, 4, 4, 5, 5, 7, 9)
     avg_val <- mean(x)
     med_val <- median(x)
     print(avg_val)
     print(med_val)
     ```

2. **Find the variance and standard deviation of `x <- c(10, 12, 23, 23, 16, 23, 21, 16)`.**
   - **Solution:**
     ```R
     data <- c(10, 12, 23, 23, 16, 23, 21, 16)
     variance_res <- var(data)
     sd_res <- sd(data)
     ```

3. **Calculate the sum of the first 100 integers.**
   - **Solution:**
     ```R
     numbers <- 1:100
     total_sum <- sum(numbers)
     ```

4. **Find the 25th, 50th, and 75th percentiles of a random normal distribution of 1000 observations.**
   - **Solution:**
     ```R
     obs <- rnorm(1000)
     probs_target <- c(0.25, 0.5, 0.75)
     percentiles <- quantile(obs, probs = probs_target)
     ```

5. **Given two vectors `height <- c(170, 180, 190)` and `weight <- c(65, 80, 95)`, find their correlation.**
   - **Solution:**
     ```R
     h <- c(170, 180, 190)
     w <- c(65, 80, 95)
     relationship <- cor(h, w)
     ```

6. **Round the value of `pi` to 4 decimal places.**
   - **Solution:**
     ```R
     constant_pi <- pi
     rounded_pi <- round(constant_pi, 4)
     ```

7. **Find the maximum and minimum values in the vector `v <- c(-5, 10, 0, 100, 45)`.**
   - **Solution:**
     ```R
     v <- c(-5, 10, 0, 100, 45)
     highest <- max(v)
     lowest <- min(v)
     ```

8. **Calculate the exponential of the mean of `c(1, 2, 3)`.**
   - **Solution:**
     ```R
     vals <- c(1, 2, 3)
     m <- mean(vals)
     result <- exp(m)
     ```

9. **Rank the elements in the vector `scores <- c(88, 95, 88, 70, 100)`.**
   - **Solution:**
     ```R
     scores <- c(88, 95, 88, 70, 100)
     position_ranks <- rank(scores)
     ```

10. **Calculate the natural logarithm of the sum of `c(10, 20, 30)`.**
    - **Solution:**
      ```R
      dataset <- c(10, 20, 30)
      s_val <- sum(dataset)
      log_result <- log(s_val)
      ```

11. **Find the range of a sample by subtracting the minimum from the maximum.**
    - **Solution:**
      ```R
      sample_data <- rnorm(50)
      data_range <- max(sample_data) - min(sample_data)
      ```

12. **Calculate the coefficient of variation (SD/Mean) for `x <- rpois(100, lambda = 5)`.**
    - **Solution:**
      ```R
      x <- rpois(100, lambda = 5)
      cv <- sd(x) / mean(x)
      ```

13. **Round the number 123.4567 to 2 significant figures.**
    - **Solution:**
      ```R
      val <- 123.4567
      sig_fig_res <- signif(val, 2)
      ```

14. **Find the median of absolute deviations from the mean for `x <- c(1, 3, 5, 7, 9)`.**
    - **Solution:**
      ```R
      x <- c(1, 3, 5, 7, 9)
      deviations <- abs(x - mean(x))
      mad_custom <- median(deviations)
      ```

15. **Standardize a vector `x` (subtract mean and divide by SD).**
    - **Solution:**
      ```R
      x <- runif(20)
      centered <- x - mean(x)
      standardized <- centered / sd(x)
      ```

16. **Calculate the sum of squared differences from the mean for `x <- c(2, 4, 6)`.**
    - **Solution:**
      ```R
      x <- c(2, 4, 6)
      diffs <- x - mean(x)
      sq_diffs <- diffs^2
      ss_val <- sum(sq_diffs)
      ```

17. **Check if `var(x)` is equal to `sd(x)^2` for any vector `x`.**
    - **Solution:**
      ```R
      x <- rnorm(10)
      variance <- var(x)
      std_dev_sq <- sd(x)^2
      is_equal <- (variance == std_dev_sq)
      ```

18. **Find the 0.975 quantile of a standard normal distribution.**
    - **Solution:**
      ```R
      dist_sample <- rnorm(10000)
      q_point <- 0.975
      critical_val <- quantile(dist_sample, q_point)
      ```

19. **Calculate `log10(x)` using the `log()` function.**
    - **Solution:**
      ```R
      x_val <- 1000
      log_base_10 <- log(x_val, base = 10)
      ```

20. **Find the rank of the maximum value in `x <- c(1, 5, 2, 8, 3)`.**
    - **Solution:**
      ```R
      x <- c(1, 5, 2, 8, 3)
      ranks <- rank(x)
      max_rank <- ranks[which.max(x)]
      ```

21. **Calculate the geometric mean of `x` using `log` and `exp`.**
    - **Solution:**
      ```R
      x <- c(1, 10, 100)
      logs <- log(x)
      avg_log <- mean(logs)
      geo_mean <- exp(avg_log)
      ```

22. **Find the interquartile range (IQR) using the `quantile` function.**
    - **Solution:**
      ```R
      data <- rnorm(100)
      qs <- quantile(data, probs = c(0.25, 0.75))
      iqr_val <- qs[2] - qs[1]
      ```

23. **Round the correlation between `rnorm(50)` and `rnorm(50)` to 3 decimal places.**
    - **Solution:**
      ```R
      var1 <- rnorm(50)
      var2 <- rnorm(50)
      correlation_coeff <- cor(var1, var2)
      final_res <- round(correlation_coeff, 3)
      ```

24. **Find the sum of ranks for a vector of size 10.**
    - **Solution:**
      ```R
      v <- runif(10)
      v_ranks <- rank(v)
      total_ranks <- sum(v_ranks)
      ```

25. **Calculate the standard error of the mean (SD / sqrt(n)).**
    - **Solution:**
      ```R
      x <- rgamma(30, shape = 2)
      standard_dev <- sd(x)
      n_size <- length(x)
      se_mean <- standard_dev / sqrt(n_size)
      ```

26. **Compute the log-likelihood of a single observation `x` from a normal distribution (manually using math functions).**
    - **Solution:**
      ```R
      data_stream <- rnorm(100)
      target_x <- 1.5
      mu <- mean(data_stream)
      sigma2 <- var(data_stream)
      
      term1 <- -0.5 * log(2 * pi * sigma2)
      term2 <- -((target_x - mu)^2 / (2 * sigma2))
      log_lik <- term1 + term2
      ```

27. **Determine the number of significant figures in `0.001234` rounded to 3 figures.**
    - **Solution:**
      ```R
      num <- 0.001234
      sf_rounded <- signif(num, 3)
      ```

28. **Calculate the mean of the logs of a sample from an exponential distribution.**
    - **Solution:**
      ```R
      exp_sample <- rexp(100, rate = 0.5)
      logged_vals <- log(exp_sample)
      avg_log_val <- mean(logged_vals)
      ```

29. **Find the maximum absolute correlation between a matrix `X` and a vector `y`.**
    - **Solution:**
      ```R
      X_mat <- matrix(rnorm(100), ncol = 5)
      y_vec <- rnorm(20)
      correlations <- cor(X_mat, y_vec)
      max_abs_cor <- max(abs(correlations))
      ```

30. **Calculate the root mean square (RMS) of a vector `x`.**
    - **Solution:**
      ```R
      x <- c(-2, 3, -1, 4)
      squared_vals <- x^2
      mean_sq <- mean(squared_vals)
      rms_val <- sqrt(mean_sq)
      ```
