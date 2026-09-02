# Διάλεξη 3: Συνεχείς Τυχαίες Μεταβλητές και η Κανονική Κατανομή

## 1. Συνεχείς Τυχαίες Μεταβλητές
Μια Τ.Μ. $X$ ονομάζεται συνεχής εάν το πεδίο τιμών της είναι συνεχές διάστημα του $\mathbb{R}$.

### Συνάρτηση Πυκνότητας Πιθανότητας (Probability Density Function - PDF)
Μια συνάρτηση $f_X(x)$ ικανοποιεί:
1. $f_X(x) \ge 0$ για κάθε $x \in \mathbb{R}$.
2. $\int_{-\infty}^\infty f_X(x) \, dx = 1$.
3. $P(a \le X \le b) = \int_a^b f_X(x) \, dx$.
*Σημείωση:* Για κάθε συγκεκριμένη τιμή $c$, $P(X = c) = 0$.

### Αθροιστική Συνάρτηση Κατανομής (Cumulative Distribution Function - CDF)
$$F_X(x) = P(X \le x) = \int_{-\infty}^x f_X(t) \, dt$$
και ισχύει: $f_X(x) = \frac{d}{dx} F_X(x)$.

---

## 2. Κυριότερες Συνεχείς Κατανομές

### 1. Ομοιόμορφη Κατανομή (Uniform Distribution) — $X \sim U(a, b)$
$$f(x) = \frac{1}{b - a}, \quad a \le x \le b$$
- $E[X] = \frac{a + b}{2}$, $\operatorname{Var}(X) = \frac{(b - a)^2}{12}$.

### 2. Εκθετική Κατανομή (Exponential Distribution) — $X \sim \operatorname{Exp}(\lambda)$
Μοντελοποιεί χρόνους αναμονής/ζωής. Είναι η μόνη συνεχής κατανομή με την ιδιότητα της **αμνησίας (memoryless property)**:
$$f(x) = \lambda e^{-\lambda x}, \quad x \ge 0$$
- $E[X] = \frac{1}{\lambda}$, $\operatorname{Var}(X) = \frac{1}{\lambda^2}$.

---

## 3. Η Κανονική Κατανομή (Normal / Gaussian Distribution) — $X \sim N(\mu, \sigma^2)$
Η σπουδαιότερη κατανομή στη Στατιστική. Η συνάρτηση πυκνότητας ορίζεται ως:
$$f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}, \quad -\infty < x < \infty$$
- **Συμμετρία:** Καμπανοειδής καμπύλη συμμετρική γύρω από τη μέση τιμή $\mu$.

### Τυποποιημένη Κανονική Κατανομή (Standard Normal) — $Z \sim N(0, 1)$
Κάθε κανονική μεταβλητή μετατρέπεται σε τυποποιημένη μέσω του μετασχηματισμού z-score:
$$Z = \frac{X - \mu}{\sigma}$$
Η CDF της $Z$ συμβολίζεται με $\Phi(z) = P(Z \le z)$ και οι τιμές της λαμβάνονται από πίνακες της κανονικής κατανομής:
- $P(Z \le -z) = 1 - \Phi(z)$.

### Εμπειρικός Κανόνας (68-95-99.7):
- $P(\mu - \sigma \le X \le \mu + \sigma) \approx 68.27\%$
- $P(\mu - 2\sigma \le X \le \mu + 2\sigma) \approx 95.45\%$
- $P(\mu - 3\sigma \le X \le \mu + 3\sigma) \approx 99.73\%$

