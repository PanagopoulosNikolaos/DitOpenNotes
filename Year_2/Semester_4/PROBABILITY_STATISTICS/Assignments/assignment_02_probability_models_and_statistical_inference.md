# Assignment 02: Probability Models and Statistical Inference

This coursework assignment evaluates probability calculations (Bayes' Theorem, conditional independence, Binomial model), Central Limit Theorem approximations, confidence interval formulation, and one-sample hypothesis testing.

---

## 1. Problem Specifications

### Problem 1: Network Intrusion and Bayes' Theorem (30 Points)
A university data center firewall processes incoming network sessions. From long-term logs:
- $97\%$ of incoming sessions are benign ($B$), while $3\%$ are malicious intrusion attempts ($M$).
- The deep packet inspection (DPI) filter flags a session as anomalous ($A$) with probability $0.95$ if it is malicious ($P(A \mid M) = 0.95$).
- If a session is benign, the filter erroneously flags it as anomalous with probability $0.04$ ($P(A \mid B) = 0.04$).

1. Compute the total probability that an incoming session is flagged as anomalous ($P(A)$).
2. Given that the filter flags a session as anomalous, calculate the posterior probability that the session is actually malicious ($P(M \mid A)$).
3. Explain why $P(M \mid A)$ is substantially lower than $0.95$, identifying the statistical phenomenon responsible.

---

### Problem 2: Packet Corruption and Normal Approximation (35 Points)
A wireless sensor node transmits $n = 400$ packets across a noisy channel. The probability that an individual packet is corrupted is $p = 0.08$. Let $X$ represent the total number of corrupted packets.
1. State the exact distribution of $X$, and calculate its expected value $E[X]$ and standard deviation $\sigma_X$.
2. Verify whether the Normal approximation to the Binomial distribution is justified.
3. Using the Normal distribution with **continuity correction**, calculate the probability that:
   - Exactly 32 packets are corrupted ($P(X = 32)$).
   - At least 36 packets are corrupted ($P(X \ge 36)$).
   - Strictly between 25 and 45 packets are corrupted ($P(25 < X < 45)$).

---

### Problem 3: Server Response Time Inference (35 Points)
A cloud engineering team measures the response times of a new microservice. A random sample of $n = 64$ query requests yields a sample mean $\bar{x} = 142.5 \text{ ms}$ and a sample standard deviation $s = 24.0 \text{ ms}$.
1. Construct a $95\%$ confidence interval for the true population mean response time $\mu$.
2. The service level agreement (SLA) requires that the mean response time must not exceed $135 \text{ ms}$. Set up the null hypothesis $H_0: \mu \le 135$ and alternative hypothesis $H_1: \mu > 135$.
3. Compute the test statistic $Z_{\text{stat}}$, determine the critical value at significance level $\alpha = 0.05$, compute the $p$-value, and formulate an engineering conclusion.

