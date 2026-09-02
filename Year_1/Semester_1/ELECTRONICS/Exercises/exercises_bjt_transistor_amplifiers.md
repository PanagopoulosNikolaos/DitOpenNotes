# Ασκήσεις Εξάσκησης: Πόλωση και Ενισχυτές BJT

## Άσκηση 1: Πόλωση BJT με Διαιρέτη Τάσης

### Εκφώνηση
Δίνεται κύκλωμα πόλωσης npn τρανζίστορ πυριτίου με διαιρέτη τάσης: $V_{CC} = 15\text{ V}$, $R_1 = 68\text{ k}\Omega$, $R_2 = 12\text{ k}\Omega$, $R_C = 3.3\text{ k}\Omega$, $R_E = 1\text{ k}\Omega$ και απολαβή ρεύματος $\beta = 100$. Υποθέστε $V_{BE} = 0.7\text{ V}$.
Υπολογίστε το σημείο λειτουργίας ηρεμίας $Q(V_{CEQ}, I_{CQ})$.

### Λύση
1. **Ισοδύναμο Thevenin στη βάση:**
   $$V_{TH} = V_{CC} \cdot \frac{R_2}{R_1 + R_2} = 15 \cdot \frac{12}{80} = 2.25\text{ V}$$
   $$R_{TH} = R_1 \parallel R_2 = \frac{68 \times 12}{80} = 10.2\text{ k}\Omega$$

2. **Υπολογισμός Ρεύματος Βάσης και Εκπομπού:**
   $$I_B = \frac{V_{TH} - V_{BE}}{R_{TH} + (\beta + 1)R_E} = \frac{2.25 - 0.7}{10.2\text{ k}\Omega + 101 \times 1\text{ k}\Omega} = \frac{1.55\text{ V}}{111.2\text{ k}\Omega} \approx 0.0139\text{ mA} = 13.9\ \mu\text{A}$$
   $$I_{CQ} = \beta \cdot I_B = 100 \times 13.9\ \mu\text{A} = 1.39\text{ mA}$$

3. **Υπολογισμός Τάσης $V_{CEQ}$:**
   $$V_{CEQ} = V_{CC} - I_{CQ}(R_C + R_E) = 15\text{ V} - 1.39\text{ mA} \times (3.3\text{ k}\Omega + 1\text{ k}\Omega)$$
   $$V_{CEQ} = 15\text{ V} - 1.39 \times 4.3 = 15 - 5.98 = 9.02\text{ V}$$

Το σημείο ηρεμίας είναι $Q(9.02\text{ V}, 1.39\text{ mA})$ στην ενεργό περιοχή.
