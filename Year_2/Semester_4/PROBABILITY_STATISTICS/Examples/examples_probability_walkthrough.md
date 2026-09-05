# Probability and Statistics: Computational Modeling Walkthrough

This guide accompanies [`examples_probability_distributions_and_clt.py`](examples_probability_distributions_and_clt.py) and [`examples_descriptive_statistics_in_r.R`](examples_descriptive_statistics_in_r.R) to illustrate practical data analysis, probability modeling, and empirical distribution verification.

---

## 1. Computational Implementations Overview

### Python Distribution & CLT Simulation (`examples_probability_distributions_and_clt.py`)
- **Central Limit Theorem (CLT)**: Demonstrates that the standardized distribution of sample means converges to standard normal $\mathcal{N}(0, 1)$ regardless of underlying population distribution (tested against Uniform, Exponential, and Binomial distributions).
- **Probability Mass Functions (PMF) & Probability Density Functions (PDF)**: Numerical evaluation of Binomial, Poisson, Uniform, and Normal probability metrics.
- **Monte Carlo Estimation**: Empirical estimation of probabilities and confidence intervals through repeated random sampling.

### R Descriptive Statistics (`examples_descriptive_statistics_in_r.R`)
- **Summary Statistics**: Location (Mean, Median), Spread (Variance, Standard Deviation, IQR, Coefficient of Variation).
- **Grouped Frequency Tables**: Automatic bin calculation, interval cuts, relative frequencies, and cumulative distribution columns.

---

## 2. Executing the Demonstrations

### Python Script
```bash
python3 Examples/examples_probability_distributions_and_clt.py
```

### R Script
```bash
Rscript Examples/examples_descriptive_statistics_in_r.R
```

---

## 3. Mathematical Reference

### Central Limit Theorem
For a sequence of independent and identically distributed (i.i.d.) random variables $X_1, X_2, \dots, X_n$ with mean $\mu$ and finite variance $\sigma^2$:

$$\bar{X}_n = \frac{1}{n} \sum_{i=1}^{n} X_i \xrightarrow{d} \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right) \quad \text{as } n \to \infty$$

Standardized Z-Score:
$$Z = \frac{\bar{X}_n - \mu}{\sigma / \sqrt{n}} \xrightarrow{d} \mathcal{N}(0, 1)$$

