# Probability and Statistics

## Course Overview
This course provides an extensive foundation in mathematical probability theory, random variables, distribution analysis, and inferential statistics for computer science and engineering. Topics include axiomatic probability, conditional probability, Bayes' Theorem, discrete and continuous random variables, joint distributions, mathematical expectation and moments, the Law of Large Numbers, the Central Limit Theorem (CLT), point and interval estimation, hypothesis testing, linear regression, and computational statistics in R and Python.

## Course Code
405 (PROBABILITY STATISTICS)

## Prerequisites
* Mathematical Analysis (Code: 103)
* Linear Algebra (Code: 102)
* Discrete Mathematics (Code: 202)

---

## Topics Covered
* **Axiomatic Probability Theory**: Sample spaces, events, Kolmogorov axioms, combinatorics (permutations, combinations), conditional probability $P(A|B) = P(A \cap B)/P(B)$, Law of Total Probability, and Bayes' Theorem.
* **Discrete Random Variables & Distributions**: Probability Mass Functions (PMF), Cumulative Distribution Functions (CDF), Expected Value $E[X]$, Variance $\text{Var}(X)$, Bernoulli trials, Binomial distribution $\mathcal{B}(n, p)$, Geometric distribution, Hypergeometric distribution, and Poisson distribution $\text{Pois}(\lambda)$.
* **Continuous Random Variables & Distributions**: Probability Density Functions (PDF), continuous CDFs, Uniform distribution $\mathcal{U}(a, b)$, Exponential distribution $\text{Exp}(\lambda)$ and memoryless property, Normal (Gaussian) distribution $\mathcal{N}(\mu, \sigma^2)$, standard normal Z-scores, and the Gamma distribution.
* **Multivariate Distributions & Moments**: Joint PMF/PDF, marginal distributions, conditional expectation, covariance $\text{Cov}(X, Y)$, Pearson correlation coefficient $\rho$, independence of random variables, and Moment Generating Functions (MGF).
* **Limit Theorems & Asymptotic Theory**: Markov's Inequality, Chebyshev's Inequality, Weak Law of Large Numbers (WLLN), and the Central Limit Theorem (CLT).
* **Inferential Statistics**: Point estimation (Method of Moments, Maximum Likelihood Estimation MLE), sampling distributions ($\chi^2$, Student's $t$, Snedecor's $F$), Confidence Intervals for means and proportions, and null hypothesis significance testing (z-test, t-test, p-values, Type I and Type II errors).
* **Statistical Computing in R**: Vectorized operations, grouped frequency distribution construction, summary statistics, Monte Carlo distribution simulation, and linear regression models.

---

## Learning Objectives
* Solve multi-stage conditional probability and decision problems by formulating Bayes' Theorem decompositions.
* Identify appropriate probability distribution models for discrete and continuous computational processes and calculate expectations and variances.
* Apply the Central Limit Theorem to compute approximate probabilities for large sample sums and averages.
* Construct and interpret 95% and 99% confidence intervals for population parameters from empirical sample data.
* Perform formal parametric hypothesis tests and draw data-driven conclusions with rigorous significance levels ($\alpha$).
* Implement exploratory data analyses, frequency distributions, and distribution simulations using R and Python.

---

## Directory Structure

| Directory | Description |
|:---|:---|
| [`Lectures/`](Lectures/) | Structured theory lecture modules, mathematical study notes, and distribution guides |
| [`Exercises/`](Exercises/) | Solved numerical drills on Bayes' Theorem, discrete distributions, and CLT normalization |
| [`Examples/`](Examples/) | Executable Monte Carlo Python scripts, descriptive statistics in R, and walkthrough guides |
| [`Assignments/`](Assignments/) | Practical coursework projects covering exploratory data analysis and probability simulations |
| [`Tutorials/`](Tutorials/) | Hands-on guides for statistical data analysis, visualization, and CLT simulation in R |
| [`Projects/`](Projects/) | Capstone design specification for empirical data modeling and parametric distribution fitting |
| [`Exams/`](Exams/) | Past examination papers with worked solutions, synthetic practice drills, and formula sheets |
| [`Resources/`](Resources/) | Consolidated master theory guides, topic phase summaries, and analysis scripts |

---

## Tooling and Simulation Environment

### Python Statistical Simulation
To execute the Central Limit Theorem and distribution simulations:
```bash
python3 Examples/examples_probability_distributions_and_clt.py
```

### R Script Execution via Command-Line
To compute descriptive metrics and grouped frequency distribution tables:
```bash
Rscript Examples/examples_descriptive_statistics_in_r.R
```

### Interactive R Session
To explore datasets interactively via the R REPL:
```bash
R
> source("Examples/examples_descriptive_statistics_in_r.R")
> q()
```