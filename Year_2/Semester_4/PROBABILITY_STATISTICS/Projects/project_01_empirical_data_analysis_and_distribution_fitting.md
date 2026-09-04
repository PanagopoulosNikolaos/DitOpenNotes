# Project 01: Empirical Telemetry Data Analysis and Distribution Fitting

## Project Overview
Execute an end-to-end computational data analysis project in R or Python using real-world or high-fidelity simulated telemetry datasets (e.g., cloud web-service request latencies or packet interarrival delays). The project encompasses data cleaning, frequency discretization, exploratory data visualization, parametric distribution fitting (Exponential vs. Normal vs. Log-Normal), goodness-of-fit testing, and Monte Carlo verification of the Central Limit Theorem.

---

## Technical Architecture and Milestones

### 1. Dataset Ingestion and Cleaning
- Ingest a minimum of $N = 2,500$ observations of positive continuous metric values.
- Handle missing values, detect and categorize extreme outliers using Tukey's fences ($1.5 \times \text{IQR}$).
- Compute comprehensive summary statistics: mean, median, standard deviation, interquartile range, skewness, and kurtosis.

### 2. Exploratory Distribution Analysis
- Construct frequency distribution tables with optimized binning (Sturges' and Freedman-Diaconis rules).
- Generate visualizations:
  - Histogram overlaid with empirical kernel density estimation (KDE).
  - Normal Quantile-Quantile (Q-Q) plot to evaluate departure from normality.
  - Boxplot illustrating five-number summary and detected outliers.

### 3. Parametric Model Fitting and Hypothesis Testing
- Estimate distribution parameters via Method of Moments (MoM) and Maximum Likelihood Estimation (MLE).
- Fit candidate distributions:
  - Exponential: $\hat{\lambda} = \frac{1}{\bar{x}}$
  - Normal: $\hat{\mu} = \bar{x}, \hat{\sigma} = s$
  - Log-Normal: $\hat{\mu}_{\log}, \hat{\sigma}_{\log}$
- Conduct goodness-of-fit hypothesis testing:
  - Chi-Square ($\chi^2$) goodness-of-fit test.
  - Kolmogorov-Smirnov (K-S) two-sided test.

### 4. Empirical Central Limit Theorem Simulation
- Draw $M = 5,000$ random bootstrap subsamples of sizes $n \in \{5, 15, 30, 100\}$.
- Plot the empirical distributions of the sample means $\bar{X}_n$.
- Verify that the variance of sample means converges precisely to $\frac{\sigma^2}{n}$.

---

## Project Milestones

| Milestone | Deliverable | Target Validation |
|---|---|---|
| **Phase 1** | Data Cleaning & Summary Statistics | Table of moments, skewness, and clean dataset submitted |
| **Phase 2** | Exploratory Visualizations | Histogram with KDE and Q-Q plots generated |
| **Phase 3** | MLE Parameter Estimation & Goodness-of-Fit | Fitted parameters, K-S test $p$-values, and distribution selection |
| **Phase 4** | CLT Simulation & Final Technical Report | Multi-panel CLT convergence plots and comprehensive report |

---

## Grading Rubric

| Criterion | Evaluation Metric | Weight |
|---|---|---|
| **Exploratory Data Analysis Rigor** | Accurate mathematical metrics, outlier handling, and appropriate binning | 25% |
| **Parametric Fitting & Hypothesis Testing** | Valid derivation of MLE estimators, correct K-S test implementation and interpretation | 30% |
| **CLT Simulation & Verification** | Clean vectorized simulation code, convergence plots, variance validation | 25% |
| **Technical Report Quality** | Academic presentation, LaTeX formulas, structured discussion of results | 20% |

