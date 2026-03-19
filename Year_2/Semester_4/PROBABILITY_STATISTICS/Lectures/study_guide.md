### Phase 1: Descriptive Statistics
* **Data Organization:** Frequency tables for ungrouped and grouped data. Calculate absolute ($f_i$), relative, and cumulative frequencies ($F_i$).
* **Measures of Central Tendency:** Mean ($\bar{x}$), Median ($M_e$), and Mode ($M_o$) for both standard and grouped data (using class centers $x_i$).
* **Measures of Position:** First Quartile ($Q_1$), Third Quartile ($Q_3$), and general Percentiles. Master linear interpolation for grouped data percentiles.
* **Measures of Dispersion:** Variance ($s^2$), Standard Deviation ($s$), and Range.
* **Core Formulas (Grouped Data):**
    * Mean: $\bar{x} = \frac{\sum f_i x_i}{n}$
    * Variance: $s^2 = \frac{\sum f_i(x_i - \bar{x})^2}{n-1}$ (or divided by $n$ depending on population vs. sample context).

### Phase 2: Probability Theory & Set Operations
* **Set Theory Fundamentals:** Sample space ($\Omega$), events, union ($\cup$), intersection ($\cap$), and complement ($'$).
* **Venn Diagrams:** Mapping worded problems ("at least one", "only one", "neither") to set notation.
* **Probability Axioms & Rules:**
    * Addition Rule: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
    * De Morgan's Laws: $P((A \cup B)') = P(A' \cap B')$ and $P((A \cap B)') = P(A' \cup B')$

### Phase 3: Conditional Probability & Independence
* **Conditional Probability:** $P(A|B) = \frac{P(A \cap B)}{P(B)}$
* **Independence:** Events $A$ and $B$ are independent if $P(A \cap B) = P(A) \cdot P(B)$.
* **Advanced Probability (Potential Additions):** Law of Total Probability and Bayes' Theorem.

### Phase 4: Discrete Random Variables & Distributions
* **Fundamentals:** Probability Mass Function (PMF), Expected Value $E[X]$, Variance $V(X)$.
* **Binomial Distribution ($X \sim B(n, p)$):**
    * Formula: $P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$
    * Conditions: Fixed number of independent trials, constant probability of success.
* **Poisson Distribution ($X \sim Po(\lambda)$):** Often covers the "missing" parts of basic discrete probabilities in university syllabi.

### Phase 5: Continuous Random Variables & Distributions
* **Normal Distribution ($X \sim N(\mu, \sigma^2)$):**
    * Standardization process: $Z = \frac{X - \mu}{\sigma}$ to transform to $Z \sim N(0, 1)$.
    * Reading Z-tables: Finding $P(Z \le z)$ using provided values (e.g., $\Phi(0.5)=0.69146$).
    * Symmetry rules: $P(Z \le -z) = 1 - P(Z \le z)$.
    * Interval probabilities: $P(a < X < b) = P(Z_a < Z < Z_b) = P(Z \le Z_b) - P(Z \le Z_a)$.
* **Empirical Rule:** 68% within $1\sigma$, 95% within $2\sigma$, 99.7% within $3\sigma$.
* **Other Continuous Distributions (Potential Additions):** Uniform and Exponential distributions.

### Phase 6: Inferential Statistics (0 to 100 Completion)
* **Central Limit Theorem (CLT):** Distribution of sample means approaches normal as $n \to \infty$.
* **Confidence Intervals:** Estimating population mean $\mu$ and proportion $p$.
* **Hypothesis Testing:** Formulating $H_0$ and $H_1$, calculating test statistics, interpreting p-values.

### Phase 7: R Programming Commands
* **Descriptive Stats:** `mean(x)`, `median(x)`, `sd(x)`, `var(x)`.
* **Quantiles/Percentiles:** `quantile(x, probs = c(0.25, 0.5, 0.75))`
* **Mode:** R lacks a built-in mode function. Common implementation requires `table()` and `max()`.
* **Binomial Distribution:**
    * $P(X=k)$: `dbinom(x=k, size=n, prob=p)`
    * $P(X \le k)$: `pbinom(q=k, size=n, prob=p)`
* **Normal Distribution:**
    * $P(X \le x)$: `pnorm(q=x, mean=\mu, sd=\sigma)`
    * Finding the $x$ value for a given probability: `qnorm(p, mean=\mu, sd=\sigma)`