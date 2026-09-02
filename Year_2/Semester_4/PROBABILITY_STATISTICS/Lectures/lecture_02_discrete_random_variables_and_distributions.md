# Διάλεξη 2: Διακριτές Τυχαίες Μεταβλητές και Κατανομές

## 1. Ορισμός Τυχαίας Μεταβλητής
Μια τυχαία μεταβλητή (Τ.Μ.) $X$ είναι μια συνάρτηση που απεικονίζει τον δειγματικό χώρο στο σύνολο των πραγματικών αριθμών: $X: \Omega \to \mathbb{R}$.
Μια Τ.Μ. ονομάζεται **διακριτή (discrete)** αν το πεδίο τιμών της $S_X$ είναι πεπερασμένο ή αριθμήσιμο.

### Συνάρτηση Μάζας Πιθανότητας (Probability Mass Function - PMF)
$$p_X(x) = P(X = x), \quad \text{με } p_X(x) \ge 0 \quad \text{και} \quad \sum_{x \in S_X} p_X(x) = 1$$

### Μέση Τιμή (Μαθηματική Ελπίδα) και Διακύμανση
- **Μέση Τιμή (Expected Value):**
$$E[X] = \mu = \sum_{x \in S_X} x \cdot p_X(x)$$
- **Διακύμανση (Variance):**
$$\operatorname{Var}(X) = \sigma^2 = E[(X - \mu)^2] = E[X^2] - (E[X])^2$$
- **Τυπική Απόκλιση (Standard Deviation):** $\sigma = \sqrt{\operatorname{Var}(X)}$.

---

## 2. Κυριότερες Διακριτές Κατανομές

### 1. Διωνυμική Κατανομή (Binomial Distribution) — $X \sim B(n, p)$
Αριθμός επιτυχιών σε $n$ ανεξάρτητες δοκιμές Bernoulli με πιθανότητα επιτυχίας $p$:
$$P(X = k) = \binom{n}{k} p^k (1 - p)^{n - k}, \quad k = 0, 1, \dots, n$$
- **Μέση Τιμή:** $E[X] = n p$
- **Διακύμανση:** $\operatorname{Var}(X) = n p (1 - p)$

### 2. Γεωμετρική Κατανομή (Geometric Distribution) — $X \sim \operatorname{Geom}(p)$
Αριθμός δοκιμών Bernoulli μέχρι την πρώτη επιτυχία (χωρίς μνήμη):
$$P(X = k) = (1 - p)^{k - 1} p, \quad k = 1, 2, \dots$$
- **Μέση Τιμή:** $E[X] = \frac{1}{p}$
- **Διακύμανση:** $\operatorname{Var}(X) = \frac{1 - p}{p^2}$

### 3. Κατανομή Poisson — $X \sim \operatorname{Poisson}(\lambda)$
Αριθμός γεγονότων που συμβαίνουν σε σταθερό χρονικό ή χωρικό διάστημα με σταθερό ρυθμό $\lambda > 0$:
$$P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}, \quad k = 0, 1, 2, \dots$$
- **Μέση Τιμή:** $E[X] = \lambda$
- **Διακύμανση:** $\operatorname{Var}(X) = \lambda$

