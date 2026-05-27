# Probability & Statistics Study Notes Mindmap

This document presents a condensed, grouped mindmap of the terms, formulas, distributions, R commands, and gotchas across the curriculum.

## Grouped Mindmap Diagram

```mermaid
mindmap
  root((Probability & Statistics))
    phase_1["Phase 1: Descriptive Statistics"]
      data_org["Data Org & Tables: f_i, h_i, F_i, H_i, R, k, w, x_i"]
      central_tendency["Central Tendency: Mean (x̄), Median (M_e), Mode (M_o), Skewness"]
      position_meas["Position: Q_1, Q_2, Q_3, P_k, IQR, 5-Number Summary, Boxplot"]
      dispersion_meas["Dispersion: Variance (s²), SD (s), CV, 1.5 IQR Outliers, Transformations"]

    phase_2["Phase 2: Probability Theory"]
      set_theory["Set Theory: Sample Space (Ω), Union (∪), Intersection (∩), Complement (A'), Disjoint"]
      venn_diagrams["Venn Diagrams: Layout, Phrase translation, 4-Region Decomposition"]
      prob_axioms["Axioms & Rules: Kolmogorov Axioms, Addition Rule, De Morgan's Laws"]
      combinatorics["Combinatorics: Product/Sum Rules, Permutations (n!), Combinations (nCr), Multinomials"]

    phase_3["Phase 3: Conditional Probability"]
      cond_prob["Conditional Probability: P(A|B) = P(A∩B)/P(B), Multiplication Rule, Reduced Space"]
      independence["Independence: P(A∩B) = P(A)P(B), vs Mutual Exclusivity, Reliability"]
      total_bayes["Partitions & Bayes: Law of Total Probability, Bayes' Theorem"]

    phase_4["Phase 4: Discrete Random Variables"]
      drv_fundamentals["DRV Fundamentals: PMF Validity, E[X], Var(X) = E[X²]-E[X]², Linearity"]
      binomial_dist["Binomial & Poisson: Bin(n,p), Poisson(λ), Rate Scaling, Approximation"]
      geom_hyper["Geometric & Hypergeometric: Geo(p) (trials vs failures), HG(N,K,n)"]
      mgfs_char["MGFs & Char Functions: MGF M_X(t) = E[e^{tX}], Moment Deriv, Char Function φ(t)"]

    phase_5["Phase 5: Continuous Random Variables"]
      normal_dist["Normal Distribution: Z-score (X-μ)/σ, Z-Table lookup, Symmetry rules"]
      empirical_rule["Empirical & Other: 68-95-99.7% Rule, Uniform U(a,b), Exponential Exp(λ)"]
      gamma_dist["Gamma Distribution: Gamma Function Γ(α), Rate vs Scale, Chi-Square link"]
      crv_transformations["Transformations: CDF Method, Jacobian Change of Variables"]

    phase_5b["Phase 5B: Multivariate Random Variables"]
      joint_marginal["Joint, Marginal & Conditional: Joint PMF/PDF, Marginals, Joint CDF, Conditional PMF/PDF"]
      multiv_moments["Expectation & Moments: Joint E[g(X,Y)], Covariance, Correlation (ρ)"]
      combo_variance["Combo Var & Total Rules: V(aX+bY), Adam's Law (Total E), Eve's Law (Total Var)"]
      func_multiple["Functions of Multiple RVs: Bivariate Jacobian, Order Statistics (Min & Max)"]

    phase_6["Phase 6: Inferential Statistics"]
      clt_section["CLT: Sample Mean X̄ ~ N(μ, σ²/n), Sum S_n ~ N(nμ, nσ²), n >= 30"]
      estimations["Estimation & Tests: CI for Mean/Proportion, Z vs t test, Errors (α, β), P-values"]
      sampling_dists["Sampling Distributions: (n-1)S²/σ² ~ χ², Chi-Square, Student's t, Fisher's F"]
      inequalities_lln["Inequalities & LLN: Markov, Chebyshev, Cantelli, Weak/Strong LLN"]

    phase_7["Phase 7: R Programming Commands"]
      r_descr_stats["Descriptive Stats: mean(), median(), var(), sd(), IQR(), quantile(), na.rm"]
      r_dist_prefixes["Prefixes: d- (PMF/PDF), p- (CDF), q- (Quantile), r- (Random)"]
      r_dists["Distribution Set: *binom, *norm, *geom (failures), *hyper (m,n,k), *exp, *unif, *gamma"]
      r_sampling_inf["Sampling & Gotchas: *chisq, *t, *f, P(X < k) vs P(X <= k), lower.tail, sd vs var arg"]
```

## Summary Index of Phase Material

### Phase 1: Descriptive Statistics

* Data Org & Tables: frequency ($f_i$), relative frequency ($h_i$), cumulative absolute frequency ($F_i$), cumulative relative frequency ($H_i$), range ($R$), number of classes ($k$), class width ($w$), data points ($x_i$).
* Central Tendency: Arithmetic mean ($\bar{x}$), median ($M_e$), mode ($M_o$), skewness.
* Position: Quartiles ($Q_1, Q_2, Q_3$), percentiles ($P_k$), Interquartile Range (IQR), 5-number summary, boxplot construction.
* Dispersion: Variance ($s^2$), standard deviation ($s$), coefficient of variation (CV), 1.5 IQR rule for outliers, data transformations.

### Phase 2: Probability Theory

* Set Theory: Sample space ($\Omega$), union ($\cup$), intersection ($\cap$), complement ($A'$), disjoint sets.
* Venn Diagrams: Layout, phrase translation, 4-region decomposition.
* Axioms & Rules: Kolmogorov axioms, addition rule, De Morgan’s laws.
* Combinatorics: Product/sum rules, permutations ($n!$), combinations ($nCr$), multinomial coefficients.

### Phase 3: Conditional Probability

* Conditional Probability: $P(A|B) = P(A \cap B) / P(B)$, multiplication rule, reduced sample space.
* Independence: $P(A \cap B) = P(A)P(B)$, distinction from mutual exclusivity, system reliability.
* Partitions & Bayes: Law of total probability, Bayes' theorem.

### Phase 4: Discrete Random Variables

* DRV Fundamentals: Probability Mass Function (PMF) validity, expected value $E[X]$, variance $Var(X) = E[X^2] - E[X]^2$, linearity of expectation.
* Binomial & Poisson: Binomial distribution $Bin(n,p)$, Poisson distribution $Poisson(\lambda)$, rate scaling, approximation methods.
* Geometric & Hypergeometric: Geometric distribution $Geo(p)$ (trials vs. failures), Hypergeometric distribution $HG(N,K,n)$.
* MGFs & Char Functions: Moment Generating Functions $M_X(t) = E[e^{tX}]$, moment derivation, characteristic functions $\phi(t)$.

### Phase 5: Continuous Random Variables

* Normal Distribution: Z-score transformation $(X-\mu)/\sigma$, Z-table lookup, symmetry properties.
* Empirical & Other: 68-95-99.7% rule, Uniform distribution $U(a,b)$, Exponential distribution $Exp(\lambda)$.
* Gamma Distribution: Gamma function $\Gamma(\alpha)$, rate vs. scale parameterization, Chi-square relationship.
* CRV Transformations: CDF method, Jacobian change of variables.

### Phase 5B: Multivariate Random Variables

* Joint, Marginal & Conditional: Joint PMF/PDF, marginal distributions, joint CDF, conditional PMF/PDF.
* Expectation & Moments: Joint expectation $E[g(X,Y)]$, covariance, correlation coefficient ($\rho$).
* Combo Var & Total Rules: Variance of linear combinations $V(aX+bY)$, Adam’s Law (law of total expectation), Eve’s Law (law of total variance).
* Functions of Multiple RVs: Bivariate Jacobian, order statistics (minimum and maximum).

### Phase 6: Inferential Statistics

* CLT: Central Limit Theorem for sample mean $\bar{X} \sim N(\mu, \sigma^2/n)$, sum $S_n \sim N(n\mu, n\sigma^2)$, requirements ($n \geq 30$).
* Estimation & Tests: Confidence intervals (CI) for mean/proportion, Z-test vs. t-test, Type I ($\alpha$) and Type II ($\beta$) errors, P-values.
* Sampling Distributions: $(n-1)S^2/\sigma^2 \sim \chi^2$, Chi-square distribution, Student’s t-distribution, Fisher’s F-distribution.
* Inequalities & LLN: Markov’s inequality, Chebyshev’s inequality, Cantelli’s inequality, Weak/Strong Law of Large Numbers (LLN).

### Phase 7: R Programming Commands

* Descriptive Stats: `mean()`, `median()`, `var()`, `sd()`, `IQR()`, `quantile()`, handling `na.rm`.
* Dist Prefixes: `d-` (PMF/PDF), `p-` (CDF), `q-` (Quantiles), `r-` (Random sampling).
* Distribution Set: `*binom`, `*norm`, `*geom` (based on failures), `*hyper` (m,n,k), `*exp`, `*unif`, `*gamma`.
* Sampling & Gotchas: `*chisq`, `*t`, `*f`, interpretation of $P(X < k)$ vs $P(X \le k)$, `lower.tail` argument, distinguishing `sd` vs `var` inputs.