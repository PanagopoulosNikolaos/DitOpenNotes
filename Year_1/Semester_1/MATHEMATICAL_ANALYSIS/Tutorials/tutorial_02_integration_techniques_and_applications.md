# Εργαστηριακός Οδηγός 2: Μέθοδοι Ολοκλήρωσης και Γεωμετρικές Εφαρμογές

## 1. Μέθοδος Αντικατάστασης (Αλλαγή Μεταβλητής)
$$\int f(g(x)) g'(x)\,dx = \int f(u)\,du, \quad \text{όπου } u = g(x), \; du = g'(x)\,dx$$

## 2. Ολοκλήρωση κατά Παράγοντες (Integration by Parts)
$$\int u(x) v'(x)\,dx = u(x) v(x) - \int u'(x) v(x)\,dx$$

### Κανόνας Προτεραιότητας Επιλογής $u$ (LIATE)
1. **L** - Logarithmic functions ($\ln x$)
2. **I** - Inverse trigonometric functions ($\arctan x, \arcsin x$)
3. **A** - Algebraic / Polynomial functions ($x^n$)
4. **T** - Trigonometric functions ($\sin x, \cos x$)
5. **E** - Exponential functions ($e^x$)

---

## 3. Ανάλυση σε Απλά Κλάσματα
Χρησιμοποιείται για ρητές συναρτήσεις $\frac{P(x)}{Q(x)}$ όπου $\deg(P) < \deg(Q)$:
* Πρωτοβάθμιος παράγοντας $(ax + b)$: $\frac{A}{ax + b}$
* Επαναλαμβανόμενος $(ax + b)^k$: $\frac{A_1}{ax + b} + \dots + \frac{A_k}{(ax + b)^k}$
* Ανάγωγο δευτεροβάθμιο $(ax^2 + bx + c)$: $\frac{Ax + B}{ax^2 + bx + c}$
