# Statistics and Time Domain Analysis Mindmap

* **Statistics and Time Domain Analysis**
* **Phase 1: Descriptive Statistics**
* Data Organization & Tables
* Frequency ($f_i$) and Relative frequency ($h_i$)
* Cumulative absolute ($F_i$) and relative frequency ($H_i$)
* Range ($R$), Number of classes ($k$), and Class width ($w$)
* Data points ($x_i$)


* Central Tendency
* Arithmetic mean ($\bar{x}$), Median ($M_e$), and Mode ($M_o$)
* Circular mean for cyclic clock times (invalid naive arithmetic mean)
* Skewness — distribution asymmetry measure


* Position Metrics
* Quartiles ($Q_1, Q_2, Q_3$), Deciles ($D_k$), and Percentiles ($P_k$)
* Interquartile Range (IQR) and 5-number summary
* Boxplot construction


* Dispersion
* Variance ($s^2$) and Standard deviation ($s$)
* Coefficient of variation (CV)
* 1.5 IQR rule for outliers
* Data transformations
* The $c^2$ rule — variance scales by $c^2$, SD by $c$ on unit conversion




* **Phase 2: Probability Theory**
* Set Theory
* Sample space ($\Omega$)
* Union ($\cup$), Intersection ($\cap$), Complement ($A'$)
* Disjoint sets


* Venn Diagrams
* Layout and 4-region decomposition
* Phrase translation (e.g., "at least one", "exactly two")


* Axioms & Rules
* Kolmogorov axioms
* Addition rule and De Morgan’s laws
* Inclusion-exclusion principle for three events


* Combinatorics
* Product/sum rules
* Permutations ($n!$) and Combinations ($nCr$)
* Circular permutations ($(n-1)!$) and combinations with replacement
* Multinomial coefficients




* **Phase 3: Conditional Probability**
* Core Concepts
* Definition: $P(A\vert{}B) = P(A \cap B) / P(B)$
* Multiplication rule
* Reduced sample space concept
* Conditional survival probability $P(T > t+s \vert{} T > t)$
* Right-censored observation windows


* Independence
* Definition: $P(A \cap B) = P(A)P(B)$
* Distinction from mutual exclusivity
* System reliability (series/parallel components)


* Partitions & Bayes
* Law of total probability
* Bayes' theorem for posterior probability




* **Phase 4: Discrete Random Variables**
* Fundamentals
* Probability Mass Function (PMF) validity conditions
* Expected value $E[X]$
* Variance $Var(X) = E[X^2] - (E[X])^2$
* Linearity of expectation


* Common Distributions
* Binomial $Bin(n,p)$ — number of successes in fixed trials
* Poisson $Poisson(\lambda)$ — event count over continuous interval
* Rate scaling and Poisson approximation of Binomial
* Geometric $Geo(p)$ (trials vs. failures variants) — memoryless property
* Hypergeometric $HG(N,K,n)$ — sampling without replacement


* Moment Generating & Characteristic Functions
* Moment Generating Functions $M_X(t) = E[e^{tX}]$
* Deriving moments via differentiation
* Characteristic functions $\phi(t)$




* **Phase 5: Continuous Random Variables**
* Normal Distribution
* Z-score transformation: $(X-\mu)/\sigma$
* Z-table lookup and symmetry properties
* Empirical 68-95-99.7% rule


* Other Core Distributions
* Uniform distribution $U(a,b)$
* Exponential distribution $Exp(\lambda)$ — memoryless property


* Advanced Distributions
* Gamma Distribution — Gamma function ($\Gamma(\alpha)$)
* Erlang — Gamma with integer shape (sum of identical Exponentials)
* Weibull — time-to-failure with changing hazard rates
* Rate vs. scale parameterization
* Chi-square relationship


* Transformations
* Cumulative Distribution Function (CDF) method
* Jacobian change of variables




* **Phase 5B: Multivariate Random Variables**
* Joint Distributions
* Joint PMF/PDF and Marginal distributions
* Joint CDF and Conditional PMF/PDF


* Expectation & Moments
* Joint expectation $E[g(X,Y)]$
* Covariance and Correlation coefficient ($\rho$)


* Combinations & Total Rules
* Variance of linear combinations: $V(aX+bY)$
* Adam’s Law (law of total expectation)
* Eve’s Law (law of total variance)


* Functions of Multiple RVs
* Bivariate Jacobian matrices
* Convolution of sums (PDF of $T_1 + T_2$)
* Order statistics (minimum and maximum distributions)




* **Phase 6: Inferential Statistics**
* Central Limit Theorem (CLT)
* Sample mean: $\bar{X} \sim N(\mu, \sigma^2/n)$
* Sample sum: $S_n \sim N(n\mu, n\sigma^2)$
* Sample size requirements ($n \ge 30$)


* Estimation & Hypothesis Testing
* Confidence intervals (CI) for mean/proportion and variance ($\chi^2$-based)
* Z-test vs. t-test decision criteria
* Type I ($\alpha$) and Type II ($\beta$) errors, P-values
* Statistical power ($1 - \beta$)


* Sampling Distributions
* Variance distribution: $(n-1)S^2/\sigma^2 \sim \chi^2$
* Chi-square, Student’s t, and Fisher’s F distributions


* Inequalities & Limits
* Markov’s and Chebyshev’s inequalities
* Cantelli’s inequality
* Weak/Strong Law of Large Numbers (LLN)




* **Phase 7: Time Domain Data & Clock Statistics**
* Time Series Metrics & Fundamental Variations
* Fractional frequency offset ($\Delta f/f$) — dimensionless measure of frequency deviation
* Time Interval Error (TIE) — cumulative phase difference between ideal and actual clock times
* Maximum Time Interval Error (MTIE) — peak-to-peak observation of delay variations
* Distinguishing population statistics vs. sampling statistics for infinite time series


* Frequency Stability Analysis (Variances)
* Allan Variance (AVAR) — two-sample variance replacing standard variance to handle frequency drift
* Allan Deviation (ADEV) — square root of AVAR, standard metric for timekeeping stability
* Overlapping Allan Deviation (OADEV) — multi-sample technique for maximum confidence estimation
* Modified Allan Variance (MVAR) — incorporates phase averaging to distinguish white vs. flicker PM noise
* Time Variance (TVAR) and Time Deviation (TDEV) — estimators for absolute clock time error
* Hadamard Variance (HVAR) — three-sample variance based on 2nd differences, immune to linear frequency drift


* Hardware-Level Timing & Noise Properties
* Stochastic noise modeling — White Phase/Frequency Modulation, Flicker Phase/Frequency Modulation
* Clock-to-Q delay ($T_{clk\to q}$) — hardware propagation delay after a clock trigger
* Clock Skew — latency differences across locations; positive skew aids setup, negative aids hold
* Deep metastability — calculating Mean Time Between Failures (MTBF) when resolving sub-picosecond overlaps




* **Phase 8: Probability of Network & Clock Delays**
* Protocol-Specific Synchronization Models
* Precision Time Protocol (PTP / IEEE 1588) — targeting sub-microsecond synchronization networks
* Grandmaster vs. Boundary vs. Ordinary clocks — hierarchy of clock reliability and source origins
* Path delay calculations — compensating for round-trip time (RTT) and detecting asymmetric routing
* Absolute clock drift — measured difference formulas $(RX_{ts} - TX_{ts}) - path\_delay$


* Delay Distribution Modeling
* Queuing and forwarding jitter — modeling switch/router delays via Weibull or Gamma continuous distributions
* Quantization error probability — discrete error bounds based on timestamp resolution limits


* Multi-Clock Delay Probabilities
* Joint delay probability — calculating $P(\Delta t_1 > x \cap \Delta t_2 > x \cap \Delta t_3 > x)$ for redundant systems
* Modeling cascaded microsecond loss — convolution of individual link delay probability density functions
* Tail probability estimation — evaluating worst-case jitter beyond acceptable tolerances ($P(delay > \mu s_{max})$)
* Markov chain modeling for probabilistic clock state deviations over sequential periods




* **Phase 9: R Programming Commands**
* Descriptive Stats: `mean()`, `median()`, `var()`, `sd()`, `IQR()`, `quantile()`, handling `na.rm` and `trim`
* Distribution Prefixes: `d-` (PMF/PDF), `p-` (CDF), `q-` (Quantiles), `r-` (Random sampling)
* Distribution Set: `*binom`, `*norm`, `*geom`, `*hyper`, `*exp`, `*unif`, `*gamma`, `*weibull`
* Sampling & Gotchas: `*chisq`, `*t`, `*f`
* Interpretation issues — $P(X < k)$ vs $P(X \le k)$
* Lower tail toggling — `lower.tail = FALSE`
* Input distinctions — providing standard deviation (`sd`) versus variance (`var`) parameters




