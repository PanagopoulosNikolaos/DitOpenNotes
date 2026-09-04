# ==============================================================================
# Script: examples_descriptive_statistics_in_r.R
# Purpose: Comprehensive Descriptive Statistics and Frequency Table Construction
# ==============================================================================

computeFrequencyTable <- function(data_vector, num_bins = 5) {
  # Computes grouped frequency distribution metrics for a numeric sample
  sample_size <- length(data_vector)
  min_val <- min(data_vector)
  max_val <- max(data_vector)

  # Determines class width and interval cut points
  bin_width <- (max_val - min_val) / num_bins
  breaks <- seq(min_val, max_val, by = bin_width)

  # Categorizes data into discrete intervals
  classes <- cut(data_vector, breaks = breaks, include.lowest = TRUE, right = FALSE)
  freq_table <- as.data.frame(table(classes))
  colnames(freq_table) <- c("Class_Interval", "Absolute_Freq")

  # Computes relative and cumulative frequencies
  freq_table$Relative_Freq <- freq_table$Absolute_Freq / sample_size
  freq_table$Cum_Absolute_Freq <- cumsum(freq_table$Absolute_Freq)
  freq_table$Cum_Relative_Freq <- cumsum(freq_table$Relative_Freq)

  return(freq_table)
}

# Sample telemetry execution latencies (milliseconds)
latency_sample <- c(
  22.1, 24.3, 19.8, 31.4, 25.0, 28.6, 21.3, 23.9, 35.1, 26.5,
  20.4, 29.8, 27.2, 22.9, 33.0, 25.4, 24.1, 26.8, 30.2, 23.5
)

# 1. Location and Spread Metrics
sample_mean <- mean(latency_sample)
sample_median <- median(latency_sample)
sample_var <- var(latency_sample)
sample_sd <- sd(latency_sample)
sample_iqr <- IQR(latency_sample)
sample_cv <- (sample_sd / sample_mean) * 100

cat("=== Summary Statistics ===\n")
cat(sprintf("Sample Size:        %d\n", length(latency_sample)))
cat(sprintf("Arithmetic Mean:    %.3f ms\n", sample_mean))
cat(sprintf("Median:             %.3f ms\n", sample_median))
cat(sprintf("Sample Variance:    %.3f ms^2\n", sample_var))
cat(sprintf("Standard Deviation: %.3f ms\n", sample_sd))
cat(sprintf("Interquartile Range:%.3f ms\n", sample_iqr))
cat(sprintf("Coeff. of Variation:%.2f%%\n", sample_cv))

cat("\n=== Grouped Frequency Distribution ===\n")
freq_df <- computeFrequencyTable(latency_sample, num_bins = 5)
print(freq_df)

