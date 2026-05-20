# Phase 4.4: Geometric and Hypergeometric Distributions

This file covers two important discrete distributions: the **Geometric Distribution** (which models the number of trials until the first success) and the **Hypergeometric Distribution** (which models sampling without replacement).

---

## 1. Geometric Distribution ($X \sim Geo(p)$)

The Geometric distribution models the number of independent Bernoulli trials required to obtain the first success. 

> **Critical Exam Gotcha:** There are two common definitions of the Geometric distribution used in university syllabi. Confusing them will lead to wrong formulas for the PMF and expected value. Always check which definition your professor uses.

### Definition A: Counting the Number of Trials ($k = 1, 2, 3, \dots$)
Here, $X$ is the trial number of the first success.
*   **PMF:** $P(X = k) = (1-p)^{k-1} p$
*   **Mean (Expected Value):** $E[X] = \frac{1}{p}$
*   **Variance:** $Var(X) = \frac{1-p}{p^2}$
*   **CDF:** $P(X \le k) = 1 - (1-p)^k$

### Definition B: Counting the Number of Failures Before the First Success ($k = 0, 1, 2, \dots$)
Here, $Y$ is the number of failures before the first success occurs. Note that $Y = X - 1$.
*   **PMF:** $P(Y = k) = (1-p)^k p$
*   **Mean (Expected Value):** $E[Y] = \frac{1-p}{p}$
*   **Variance:** $Var(Y) = \frac{1-p}{p^2}$
*   **CDF:** $P(Y \le k) = 1 - (1-p)^{k+1}$

---

## 2. Hypergeometric Distribution ($X \sim HG(N, K, n)$)

The Hypergeometric distribution models the number of successes in a sample of size $n$ drawn from a finite population of size $N$ containing exactly $K$ successes, **without replacement**.

Unlike the Binomial distribution, the trials are **not independent** because the probability of success changes with each draw.

*   **Parameters:**
    *   $N$: Total population size
    *   $K$: Number of success items in the population
    *   $n$: Number of items drawn (sample size)
    *   $k$: Number of success items in the sample
*   **PMF:**
    $$P(X = k) = \frac{\binom{K}{k} \binom{N-K}{n-k}}{\binom{N}{n}}, \quad \max(0, n - (N - K)) \le k \le \min(n, K)$$
*   **Expected Value:** $E[X] = n \cdot \frac{K}{N}$
*   **Variance:**
    $$Var(X) = n \cdot \frac{K}{N} \cdot \left(1 - \frac{K}{N}\right) \cdot \left(\frac{N - n}{N - 1}\right)$$
    The term $\frac{N-n}{N-1}$ is known as the **finite population correction factor**.

---

## 3. Solved Exercises (10 Examples)

### Exercise 1: Finding first success on a specific trial (Geometric)
**Problem:** A basketball player makes a free throw with probability $p = 0.7$. Find the probability that they make their first successful free throw on their 4th attempt.

**Solution:**
- **Step 1: Identify distribution and parameters.**
  We count the trials, so we use Definition A ($X \sim Geo(0.7)$). We want to find $P(X = 4)$.
- **Step 2: WIP State.**
  Formula: $P(X=4) = (1-p)^{4-1} p = (0.3)^3 \cdot ?$
- **Step 3: Final Calculation.**
  $$P(X=4) = (0.3)^3 \cdot 0.7 = 0.027 \cdot 0.7 = 0.0189.$$

---

### Exercise 2: Rolling a Die (Geometric)
**Problem:** A fair six-sided die is rolled repeatedly. What is the expected number of rolls needed to get the first 6?

**Solution:**
- **Step 1: Identify parameter.**
  Success is rolling a 6, so $p = 1/6$. We are counting the number of rolls (trials), so we use Definition A.
- **Step 2: WIP State.**
  Expected value $E[X] = \frac{1}{?}$
- **Step 3: Final Calculation.**
  $$E[X] = \frac{1}{1/6} = 6 \text{ rolls}.$$

---

### Exercise 3: Cumulative Geometric Probability ("At Most")
**Problem:** A computer system has a 5% chance of crash during a boot sequence. What is the probability that the first crash occurs within the first 3 boots?

**Solution:**
- **Step 1: Define variables.**
  Let $X$ be the boot sequence number of the first crash. $X \sim Geo(0.05)$. We want $P(X \le 3)$.
- **Step 2: WIP State.**
  Use the CDF formula: $P(X \le 3) = 1 - (1-p)^3 = 1 - (0.95)^3 = 1 - ?$
- **Step 3: Final Calculation.**
  $$(0.95)^3 = 0.857375$$
  $$P(X \le 3) = 1 - 0.857375 = 0.142625 \approx 0.1426.$$

---

### Exercise 4: Geometric Complement Rule ("More Than")
**Problem:** A salesman makes a sale with a probability of 0.2 on any call. What is the probability that he needs more than 5 calls to make his first sale?

**Solution:**
- **Step 1: Define target probability.**
  We want $P(X > 5)$, where $X \sim Geo(0.2)$.
- **Step 2: WIP State.**
  The complement rule for "more than $k$ trials" is:
  $$P(X > k) = (1-p)^k$$
  So, $P(X > 5) = (1 - 0.2)^5 = (0.8)^5 = ?$
- **Step 3: Final Calculation.**
  $$P(X > 5) = 0.32768 \approx 0.3277.$$
  *(Exam shortcut: "More than $k$" simply means the first $k$ trials were all failures. So the probability is just $(1-p)^k$. Never sum terms or use the CDF if you can avoid it!)*

---

### Exercise 5: Memoryless Property of Geometric Distribution
**Problem:** A tester is testing chips until a defective one is found. The probability of finding a defect on any chip is $p = 0.1$. If the first 5 chips tested were good, what is the probability that the first defective chip is found on the 8th test?

**Solution:**
- **Step 1: Understand the setup.**
  We want the conditional probability $P(X = 8 | X > 5)$.
- **Step 2: WIP State.**
  By the memoryless property of the Geometric distribution, the fact that 5 trials failed does not affect future trials. Thus, finding the first defect on the 8th trial (which is 3 additional trials) is equivalent to finding the first defect on the 3rd trial starting from scratch:
  $$P(X = 8 | X > 5) = P(X = 3) = (0.9)^2 \cdot ?$$
- **Step 3: Final Calculation.**
  $$P(X=3) = 0.81 \cdot 0.1 = 0.081.$$

---

### Exercise 6: Card Selection (Hypergeometric)
**Problem:** A hand of 5 cards is dealt from a standard deck of 52 cards. What is the probability that the hand contains exactly 3 Aces?

**Solution:**
- **Step 1: Identify population and sample parameters.**
  - Total population $N = 52$
  - Successes in population $K = 4$ (Aces)
  - Sample size $n = 5$
  - Successes in sample $k = 3$
- **Step 2: WIP State.**
  We apply the Hypergeometric PMF:
  $$P(X = 3) = \frac{\binom{K}{k} \binom{N-K}{n-k}}{\binom{N}{n}} = \frac{\binom{4}{3} \binom{48}{2}}{\binom{52}{5}}$$
  - $\binom{4}{3} = 4$
  - $\binom{48}{2} = \frac{48 \cdot 47}{2} = 1128$
  - $\binom{52}{5} = ?$
- **Step 3: Final Calculation.**
  - $\binom{52}{5} = 2,598,960$
  - $P(X=3) = \frac{4 \cdot 1128}{2,598,960} = \frac{4512}{2,598,960} \approx 0.001736$.

---

### Exercise 7: Quality Control (Hypergeometric)
**Problem:** A box contains 20 components, of which 4 are defective. An engineer randomly selects 5 components without replacement. Find the probability that no defective components are in the sample.

**Solution:**
- **Step 1: Map parameters.**
  - Population $N = 20$, Defectives (successes) $K = 4$, Sample size $n = 5$.
  - We want $P(X = 0)$ successes in the sample.
- **Step 2: WIP State.**
  $$P(X = 0) = \frac{\binom{4}{0} \binom{16}{5}}{\binom{20}{5}} = \frac{1 \cdot \frac{16!}{5! \cdot 11!}}{\frac{20!}{5! \cdot 15!}} = \frac{4368}{?}$$
- **Step 3: Final Calculation.**
  - $\binom{20}{5} = 15,504$
  - $P(X = 0) = \frac{4368}{15,504} \approx 0.2817$.

---

### Exercise 8: Expected Value & Variance of Hypergeometric
**Problem:** Using the same quality control setup from Exercise 7 ($N=20, K=4, n=5$), calculate the expected number of defective components in the sample and the variance.

**Solution:**
- **Step 1: Calculate Mean.**
  $$E[X] = n \cdot \frac{K}{N} = 5 \cdot \frac{4}{20} = 1$$
- **Step 2: WIP State for Variance.**
  $$Var(X) = n \cdot \frac{K}{N} \cdot \left(1 - \frac{K}{N}\right) \cdot \left(\frac{N - n}{N - 1}\right)$$
  $$Var(X) = 5 \cdot \frac{4}{20} \cdot \left(1 - \frac{4}{20}\right) \cdot \left(\frac{20 - 5}{20 - 1}\right) = 1 \cdot 0.8 \cdot \frac{15}{?}$$
- **Step 3: Final Calculation.**
  $$Var(X) = 0.8 \cdot \frac{15}{19} = \frac{12}{19} \approx 0.6316.$$

---

### Exercise 9: Hypergeometric vs. Binomial Approximation
**Problem:** A batch of 1000 items contains 100 defective items. If a sample of 10 items is selected without replacement, find the exact probability of getting exactly 1 defective item using the Hypergeometric distribution, and compare it to the Binomial approximation.

**Solution:**
- **Step 1: Exact Hypergeometric calculation.**
  $N = 1000, K = 100, n = 10, k = 1$.
  $$P(X = 1) = \frac{\binom{100}{1} \binom{900}{9}}{\binom{1000}{10}} \approx 0.3899$$
- **Step 2: WIP State for Binomial approximation.**
  Since the population $N$ is very large compared to the sample size $n$ ($n/N = 10/1000 = 0.01 \le 0.05$), we can approximate this using a Binomial model with $p = K/N = 0.1$.
  $$Y \sim B(10, 0.1)$$
  $$P(Y = 1) = \binom{10}{1} (0.1)^1 (0.9)^9 = 10 \cdot 0.1 \cdot ?$$
- **Step 3: Final Calculation.**
  $$(0.9)^9 = 0.38742$$
  $$P(Y=1) = 1 \cdot 0.38742 = 0.3874$$
  **Comparison:** The difference is very small ($0.3899 - 0.3874 = 0.0025$). This illustrates why the Binomial approximation is highly accurate when the sample is less than 5% of the population.

---

### Exercise 10: Cumulative Hypergeometric ("At Least")
**Problem:** A bag contains 6 red marbles and 4 blue marbles. A child draws 3 marbles at random without replacement. Find the probability of getting at least 2 red marbles.

**Solution:**
- **Step 1: Map variables.**
  - Population $N = 10$, Red Marbles $K = 6$, Sample size $n = 3$.
  - We want $P(X \ge 2) = P(X = 2) + P(X = 3)$.
- **Step 2: WIP State.**
  - $P(X=2) = \frac{\binom{6}{2} \binom{4}{1}}{\binom{10}{3}} = \frac{15 \cdot 4}{120} = \frac{60}{120} = 0.5$
  - $P(X=3) = \frac{\binom{6}{3} \binom{4}{0}}{\binom{10}{3}} = \frac{20 \cdot 1}{?}$
- **Step 3: Final Calculation.**
  - $P(X=3) = \frac{20}{120} \approx 0.1667$.
  - $P(X \ge 2) = 0.5 + 0.1667 = 0.6667$.
