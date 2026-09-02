# Ασκήσεις Εμπέδωσης: Μετασχηματισμοί Fourier, Laplace και Z

## Άσκηση 1: Μετασχηματισμός Fourier Ορθογώνιου Παλμού
### Εκφώνηση:
Υπολογίστε τον μετασχηματισμό Fourier του ορθογώνιου παλμού:
$$x(t) = \text{rect}(t / T_1) = \begin{cases} 1, & |t| \le T_1 / 2 \\ 0, & |t| > T_1 / 2 \end{cases}$$

### Λύση:
Από τον ορισμό του CTFT:
$$X(j\omega) = \int_{-\infty}^{\infty} x(t) e^{-j \omega t} \, dt = \int_{-T_1/2}^{T_1/2} 1 \cdot e^{-j \omega t} \, dt$$
$$X(j\omega) = \left[ \frac{e^{-j \omega t}}{-j \omega} \right]_{-T_1/2}^{T_1/2} = \frac{e^{-j \omega T_1 / 2} - e^{j \omega T_1 / 2}}{-j \omega} = \frac{2 \sin(\omega T_1 / 2)}{\omega}$$
Πολλαπλασιάζοντας και διαιρώντας με $T_1 / 2$:
$$X(j\omega) = T_1 \frac{\sin(\omega T_1 / 2)}{\omega T_1 / 2} = T_1 \text{sinc}\left(\frac{\omega T_1}{2\pi}\right)$$

---

## Άσκηση 2: Επίλυση Διαφορικής Εξίσωσης με Μετασχηματισμό Laplace
### Εκφώνηση:
Βρείτε την απόκριση $y(t)$ του συστήματος που περιγράφεται από τη διαφορική εξίσωση:
$$\frac{dy(t)}{dt} + 3 y(t) = e^{-t} u(t), \quad y(0^-) = 2$$

### Λύση:
1. Εφαρμογή μονόπλευρου μετασχηματισμού Laplace:
   $$\mathcal{L}\left\{\frac{dy}{dt}\right\} = s Y(s) - y(0^-) = s Y(s) - 2$$
   $$\mathcal{L}\{3 y(t)\} = 3 Y(s)$$
   $$\mathcal{L}\{e^{-t} u(t)\} = \frac{1}{s + 1}, \quad \text{Re}\{s\} > -1$$
2. Αντικατάσταση στην εξίσωση:
   $$s Y(s) - 2 + 3 Y(s) = \frac{1}{s + 1} \implies (s + 3) Y(s) = 2 + \frac{1}{s + 1} = \frac{2s + 3}{s + 1}$$
   $$Y(s) = \frac{2s + 3}{(s + 1)(s + 3)}$$
3. Ανάλυση σε απλά κλάσματα:
   $$\frac{2s + 3}{(s + 1)(s + 3)} = \frac{A}{s + 1} + \frac{B}{s + 3}$$
   - $A = \left. \frac{2s + 3}{s + 3} \right|_{s = -1} = \frac{1}{2} = 0.5$
   - $B = \left. \frac{2s + 3}{s + 1} \right|_{s = -3} = \frac{-3}{-2} = 1.5$
4. Αντίστροφος Μετασχηματισμός Laplace:
   $$y(t) = \left( 0.5 e^{-t} + 1.5 e^{-3t} \right) u(t)$$

