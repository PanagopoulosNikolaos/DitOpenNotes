"""Comprehensive Master Theory Guide component for Digital Electronics curriculum.

Provides a self-contained, authoritative handbook covering 100% of the theoretical
principles, mathematical models, circuit designs, and VHDL syntax required to achieve
a perfect score (100%) on university digital electronics examinations.
"""

from nicegui import ui
from config import renderMathHtml


def renderTheoryPage() -> None:
    """Renders the comprehensive Digital Electronics educational handbook.

    Returns:
        None
    """
    with ui.column().classes("w-full max-w-6xl mx-auto px-4 py-8 space-y-10 latex-target").props('id="theory-guide-container"'):
        # Hero Title Card
        with ui.column().classes("w-full glass-panel gap-3 p-8 border border-[var(--border-accent)] shadow-md"):
            with ui.row().classes("items-center gap-4"):
                ui.html('<i class="fa-solid fa-book-bookmark text-[var(--accent)] text-3xl"></i>')
                with ui.column().classes("gap-1"):
                    ui.html('<h1 class="text-2xl md:text-3xl font-black text-[var(--text-1)] m-0">Εγχειρίδιο Πλήρους Θεωρίας Ψηφιακών Ηλεκτρονικών</h1>')
                    ui.label(
                        "Αυτοτελής οδηγός μελέτης: Συστήματα Αριθμών, Άλγεβρα Boole, Χάρτες K-Map, "
                        "Συνδυαστικά/Ακολουθιακά Κυκλώματα, Μετρητές, Μηχανές FSM και Σύνθεση VHDL/FPGA."
                    ).classes("text-sm text-[var(--text-2)]")

        # MODULE 1: Number Systems & Arithmetic
        with ui.column().classes("w-full glass-panel gap-4 p-6 border border-[var(--border)]"):
            with ui.row().classes("items-center gap-3 pb-2 border-b border-[var(--border)]"):
                ui.html('<i class="fa-solid fa-binary text-[var(--blue-action)] text-xl"></i>')
                ui.html('<h2 class="text-lg md:text-xl font-bold text-[var(--text-1)] m-0">1. Συστήματα Αριθμών, Βάσεις & Προσημασμένη Αριθμητική</h2>')

            m1_content = r"""
### 1.1 Βάσεις Αρίθμησης & Μετατροπές
Κάθε αριθμός $N$ σε βάση $r$ εκφράζεται ως πολυώνυμο θέσης:
$$N = \sum_{i=-m}^{n-1} d_i \cdot r^i$$
- **Δυαδικό (r=2):** Ψηφία $\{0, 1\}$.
- **Οκταδικό (r=8):** Ομαδοποίηση ανά 3 δυαδικά ψηφία ($2^3=8$).
- **Δεκαεξαδικό (r=16):** Ψηφία $\{0..9, A..F\}$, ομαδοποίηση ανά 4 bits ($2^4=16$).
- **Κώδικας Gray:** Μονομεταβλητός κώδικας (διαδοχικές τιμές διαφέρουν μόνο κατά 1 bit). Μετατροπή Binary $\to$ Gray: $G_i = B_i \oplus B_{i+1}$.

### 1.2 Προσημασμένη Αναπαράσταση
Σε μήκος λέξης $n$ bits, το MSB είναι το bit προσήμου (0 = θετικός, 1 = αρνητικός).
1. **Πρόσημο και Μέγεθος (Sign-Magnitude):** MSB πρόσημο, τα υπόλοιπα $n-1$ bits είναι το απόλυτο μέγεθος. Εύρος: $[-(2^{n-1}-1), +(2^{n-1}-1)]$. Δύο μηδενικά (+0, -0).
2. **Συμπλήρωμα ως προς 1 (1's Complement):** Αντιστροφή όλων των bits του θετικού μεγέθους ($\overline{X}$). Δύο μηδενικά.
3. **Συμπλήρωμα ως προς 2 (2's Complement):**
   $$[-X]_{C2} = \overline{X} + 1 = 2^n - X$$
   - **Μοναδικό μηδέν (00...0).**
   - **Εύρος τιμών:** $[-2^{n-1}, +2^{n-1}-1]$ (για $n=8$: $[-128, +127]$).
   - Το βάρος του MSB είναι αρνητικό: $-d_{n-1} \cdot 2^{n-1} + \sum_{i=0}^{n-2} d_i 2^i$.

### 1.3 Αφαίρεση & Ανίχνευση Υπερχείλισης (Overflow)
- Η αφαίρεση εκτελείται ως πρόσθεση: $A - B = A + [-B]_{C2}$.
- Το τελικό κρατούμενο εξόδου ($C_{out} = C_n$) **απορρίπτεται**.
- **Κανόνας Υπερχείλισης:**
  1. Συμβαίνει **μόνο** κατά την πρόσθεση ομόσημων αριθμών που δίνει αποτέλεσμα αντίθετου προσήμου.
  2. Στο υλικό ανιχνεύεται με πύλη XOR στα κρατούμενα του MSB:
     $$V = C_{in\_msb} \oplus C_{out\_msb} = C_{n-1} \oplus C_n$$
     Αν $V = 1$, το αποτέλεσμα υπερβαίνει το εύρος $[-2^{n-1}, +2^{n-1}-1]$ και είναι εσφαλμένο.
"""
            ui.html(f'<div class="text-sm text-[var(--text-1)] leading-relaxed latex-target">{renderMathHtml(m1_content)}</div>')

        # MODULE 2: Boolean Algebra & Logic Gates
        with ui.column().classes("w-full glass-panel gap-4 p-6 border border-[var(--border)]"):
            with ui.row().classes("items-center gap-3 pb-2 border-b border-[var(--border)]"):
                ui.html('<i class="fa-solid fa-shapes text-[var(--orange)] text-xl"></i>')
                ui.html('<h2 class="text-lg md:text-xl font-bold text-[var(--text-1)] m-0">2. Άλγεβρα Boole, Πύλες & Καθολικότητα (NAND/NOR)</h2>')

            m2_content = r"""
### 2.1 Θεμελιώδη Αξιώματα & Θεωρήματα
- **Ταυτοπάθεια:** $x + x = x, \quad x \cdot x = x$
- **Συμπληρωματικότητα:** $x + \overline{x} = 1, \quad x \cdot \overline{x} = 0$
- **Απορρόφηση:** $x + x y = x, \quad x (x + y) = x$
- **Εξάλειψη:** $x + \overline{x} y = x + y, \quad x (\overline{x} + y) = x y$
- **Θεώρημα Συναίνεσης (Consensus Theorem):**
  $$x y + \overline{x} z + y z = x y + \overline{x} z$$
  $$\text{Δυϊκό:} \quad (x + y)(\overline{x} + z)(y + z) = (x + y)(\overline{x} + z)$$
- **Νόμοι De Morgan:**
  $$\overline{x_1 + x_2 + \dots + x_n} = \overline{x_1} \cdot \overline{x_2} \cdots \overline{x_n}$$
  $$\overline{x_1 \cdot x_2 \cdots x_n} = \overline{x_1} + \overline{x_2} + \dots + \overline{x_n}$$

### 2.2 Καθολικότητα Πυλών NAND & NOR (Universal Gates)
Κάθε λογική συνάρτηση μπορεί να υλοποιηθεί αποκλειστικά με πύλες NAND ή αποκλειστικά με πύλες NOR:
1. **Αντιστροφέας (NOT):** $\overline{x} = \text{NAND}(x, x) = \text{NOR}(x, x)$.
2. **Πύλη AND:**
   - Μέσω NAND: $\text{NAND}(\text{NAND}(x, y), \text{NAND}(x, y))$.
   - Μέσω NOR: $\text{NOR}(\overline{x}, \overline{y}) = \overline{\overline{x} + \overline{y}} = x \cdot y$.
3. **Πύλη OR:**
   - Μέσω NAND: $\text{NAND}(\overline{x}, \overline{y}) = \overline{\overline{x} \cdot \overline{y}} = x + y$.
   - Μέσω NOR: $\text{NOR}(\text{NOR}(x, y), \text{NOR}(x, y))$.
"""
            ui.html(f'<div class="text-sm text-[var(--text-1)] leading-relaxed latex-target">{renderMathHtml(m2_content)}</div>')

        # MODULE 3: Canonical Forms
        with ui.column().classes("w-full glass-panel gap-4 p-6 border border-[var(--border)]"):
            with ui.row().classes("items-center gap-3 pb-2 border-b border-[var(--border)]"):
                ui.html('<i class="fa-solid fa-table text-[var(--amber)] text-xl"></i>')
                ui.html('<h2 class="text-lg md:text-xl font-bold text-[var(--text-1)] m-0">3. Κανονικές Μορφές: Minterms (SOP) & Maxterms (POS)</h2>')

            m3_content = r"""
### 3.1 Ελαχιστόροι (Minterms) & Κανονικό SOP
- **Minterm ($m_i$):** Γινόμενο $n$ μεταβλητών όπου κάθε μεταβλητή εμφανίζεται είτε σε απλή είτε σε συμπληρωμένη μορφή ακριβώς μία φορά. Παίρνει τιμή 1 σε μία μοναδική γραμμή του πίνακα αληθείας.
- **Κανονική Μορφή SOP:**
  $$F(A, B, C) = \sum m(1, 4, 6, 7) = \overline{A}\overline{B}C + A\overline{B}\overline{C} + AB\overline{C} + ABC$$

### 3.2 Μεγιστόροι (Maxterms) & Κανονικό POS
- **Maxterm ($M_i$):** Άθροισμα $n$ μεταβλητών που παίρνει τιμή 0 σε μία μοναδική γραμμή.
- **Σχέση Συμπληρωματικότητας:** $M_i = \overline{m_i}$.
- **Κανονική Μορφή POS:**
  $$F(A, B, C) = \prod M(0, 2, 3, 5) = (A+B+C)(A+\overline{B}+C)(A+\overline{B}+\overline{C})(\overline{A}+B+\overline{C})$$
- **Κανόνας Μετατροπής:** Τα maxterms μιας συνάρτησης είναι ακριβώς οι δείκτες που λείπουν από τα minterms της!
"""
            ui.html(f'<div class="text-sm text-[var(--text-1)] leading-relaxed latex-target">{renderMathHtml(m3_content)}</div>')

        # MODULE 4: Karnaugh Maps & Hazard Analysis
        with ui.column().classes("w-full glass-panel gap-4 p-6 border border-[var(--border)]"):
            with ui.row().classes("items-center gap-3 pb-2 border-b border-[var(--border)]"):
                ui.html('<i class="fa-solid fa-table-cells text-[var(--accent)] text-xl"></i>')
                ui.html('<h2 class="text-lg md:text-xl font-bold text-[var(--text-1)] m-0">4. Χάρτες Karnaugh & Ανάλυση Κινδύνων (Hazards)</h2>')

            m4_content = r"""
### 4.1 Κανόνες Ελαχιστοποίησης K-Map
1. **Διάταξη Gray Code:** Γραμμές και στήλες διατάσσονται ως $\{00, 01, 11, 10\}$ ώστε γειτονικά κελιά να διαφέρουν κατά 1 bit.
2. **Μέγεθος Ομάδων:** Οι ομάδες πρέπει να περιέχουν $2^k$ κελιά ($1, 2, 4, 8, 16$) και να είναι όσο το δυνατόν μεγαλύτερες.
3. **Τυλίγματα (Toroidal Wrap):** Τα άκρα του χάρτη είναι γειτονικά (οι 4 γωνίες σχηματίζουν ομάδα 4 κελιών: $\overline{B}\overline{D}$).
4. **Ουσιώδεις Πρωτεύοντες Όροι (Essential Prime Implicants - EPIs):** Κάθε ομάδα που περιέχει τουλάχιστον ένα minterm που δεν καλύπτεται από καμία άλλη ομάδα είναι EPI και **πρέπει οπωσδήποτε** να συμπεριληφθεί στην ελάχιστη λύση.
5. **Αδιάφορες Συνθήκες (Don't Cares, $d$):** Χρησιμοποιούνται ως 1 μόνο αν συμβάλλουν στη μεγέθυνση ομάδας. Διαφορετικά θεωρούνται 0.

### 4.2 Στατικοί & Δυναμικοί Κίνδυνοι (Hazards)
- **Static-1 Hazard:** Η έξοδος πρέπει θεωρητικά να διατηρείται στο 1, αλλά στιγμιαία πέφτει στο 0 ($1 \to 0 \to 1$) λόγω καθυστέρησης $\Delta t$ σε αντιστροφέα.
- **Εντοπισμός:** Εμφανίζεται όταν δύο γειτονικά minterms με τιμή 1 ανήκουν σε διαφορετικούς κύβους (πρωτεύοντες όρους).
- **Εξάλειψη (Hazard-Free SOP):** Προσθήκη του **όρου συναίνεσης (consensus term)** που περικλείει και τα δύο γειτονικά minterms.
  $$F = AB + \overline{A}C \implies F_{hazard\_free} = AB + \overline{A}C + BC$$
- **Static-0 Hazard:** Αντίστοιχο φαινόμενο σε μορφή POS (η έξοδος πρέπει να είναι 0 και στιγμιαία κάνει παλμό $0 \to 1 \to 0$).
"""
            ui.html(f'<div class="text-sm text-[var(--text-1)] leading-relaxed latex-target">{renderMathHtml(m4_content)}</div>')

        # MODULE 5: Combinational Arithmetic (Adders, CLA, ALU)
        with ui.column().classes("w-full glass-panel gap-4 p-6 border border-[var(--border)]"):
            with ui.row().classes("items-center gap-3 pb-2 border-b border-[var(--border)]"):
                ui.html('<i class="fa-solid fa-calculator text-[var(--green-ok)] text-xl"></i>')
                ui.html('<h2 class="text-lg md:text-xl font-bold text-[var(--text-1)] m-0">5. Συνδυαστικά Αριθμητικά Κυκλώματα (Adders, CLA, ALU)</h2>')

            m5_content = r"""
### 5.1 Ημιαθροιστής & Πλήρης Αθροιστής
- **Ημιαθροιστής (Half Adder):**
  $$S = A \oplus B, \quad C = A \cdot B$$
- **Πλήρης Αθροιστής (Full Adder):**
  $$S = A \oplus B \oplus C_{in}$$
  $$C_{out} = AB + C_{in}(A \oplus B) = AB + BC_{in} + AC_{in}$$

### 5.2 Αθροιστής Διάδοσης Κρατουμένου (Ripple Carry Adder - RCA)
Σύνδεση $n$ πλήρων αθροιστών σε σειρά. Η συνολική καθυστέρηση εξαρτάται γραμμικά από το $n$:
$$t_{delay} = t_{HA} + (n-1) \cdot t_{carry}$$

### 5.3 Αθροιστής Πρόβλεψης Κρατουμένου (Carry Lookahead Adder - CLA)
Εξαλείφει την αλυσιδωτή καθυστέρηση υπολογίζοντας όλα τα κρατούμενα παράλληλα:
- **Σήμα Παραγωγής (Generate):** $G_i = A_i \cdot B_i$
- **Σήμα Διάδοσης (Propagate):** $P_i = A_i \oplus B_i$
- **Εξισώσεις Κρατουμένων:**
  $$C_1 = G_0 + P_0 C_0$$
  $$C_2 = G_1 + P_1 G_0 + P_1 P_0 C_0$$
  $$C_3 = G_2 + P_2 G_1 + P_2 P_1 G_0 + P_2 P_1 P_0 C_0$$
  $$C_4 = G_3 + P_3 G_2 + P_3 P_2 G_1 + P_3 P_2 P_1 G_0 + P_3 P_2 P_1 P_0 C_0$$
Όλα τα κρατούμενα παράγονται σε σταθερό χρόνο 2 βαθμίδων πυλών ανεξάρτητα από το $n$!
"""
            ui.html(f'<div class="text-sm text-[var(--text-1)] leading-relaxed latex-target">{renderMathHtml(m5_content)}</div>')

        # MODULE 6: MSI Components (Decoders, MUX, Encoders)
        with ui.column().classes("w-full glass-panel gap-4 p-6 border border-[var(--border)]"):
            with ui.row().classes("items-center gap-3 pb-2 border-b border-[var(--border)]"):
                ui.html('<i class="fa-solid fa-microchip text-[var(--accent)] text-xl"></i>')
                ui.html('<h2 class="text-lg md:text-xl font-bold text-[var(--text-1)] m-0">6. Κυκλώματα MSI: Αποκωδικοποιητές, Κωδικοποιητές & Πολυπλέκτες</h2>')

            m6_content = r"""
### 6.1 Αποκωδικοποιητές (Decoders - 74138)
Μετατρέπει δυαδικό κώδικα $n$ εισόδων σε $2^n$ γραμμές εξόδου.
- **Active-Low Outputs ($\overline{Y_k}$):** Κάθε έξοδος ισούται με $\overline{m_k}$.
- **Σύνθεση Συναρτήσεων:** Κάθε συνάρτηση $F = \sum m(a, b, c)$ υλοποιείται συνδέοντας τις εξόδους $\overline{Y_a}, \overline{Y_b}, \overline{Y_c}$ σε **μία πύλη NAND** (θεώρημα De Morgan: $\overline{\overline{m_a} \cdot \overline{m_b}} = m_a + m_b$).

### 6.2 Κωδικοποιητές Προτεραιότητας (Priority Encoders - 74148)
Αν πολλαπλές είσοδοι είναι ενεργές ταυτόχρονα, κωδικοποιείται αποκλειστικά η είσοδος με την υψηλότερη προτεραιότητα. Παρέχει έξοδο $V$ (Valid) που δείχνει αν τουλάχιστον μία είσοδος είναι ενεργή.

### 6.3 Πολυπλέκτες (Multiplexers - 74151)
Δρομολογεί 1 από $2^k$ εισόδους δεδομένων στην έξοδο βάσει $k$ γραμμών επιλογής.
$$\text{MUX 4:1} \implies Y = \overline{S_1}\overline{S_0}I_0 + \overline{S_1}S_0 I_1 + S_1 \overline{S_0}I_2 + S_1 S_0 I_3$$
- **Καθολική Σύνθεση Συναρτήσεων με MUX:**
  Μία συνάρτηση $n$ μεταβλητών υλοποιείται με MUX $2^{n-1}:1$ συνδέοντας $n-1$ μεταβλητές στις γραμμές επιλογής και την $n$-οστή μεταβλητή ($0, 1, D, \overline{D}$) στις εισόδους δεδομένων.
"""
            ui.html(f'<div class="text-sm text-[var(--text-1)] leading-relaxed latex-target">{renderMathHtml(m6_content)}</div>')

        # MODULE 7: Latches & Flip-Flops
        with ui.column().classes("w-full glass-panel gap-4 p-6 border border-[var(--border)]"):
            with ui.row().classes("items-center gap-3 pb-2 border-b border-[var(--border)]"):
                ui.html('<i class="fa-solid fa-clock text-[var(--purple)] text-xl"></i>')
                ui.html('<h2 class="text-lg md:text-xl font-bold text-[var(--text-1)] m-0">7. Στοιχεία Μνήμης: Latches, Flip-Flops & Χρονισμοί</h2>')

            m7_content = r"""
### 7.1 Latch έναντι Flip-Flop
- **Latch (Μανδαλωτής):** Διαφανής στη στάθμη του ρολογιού (Level-sensitive). Όσο $CLK=1$, η έξοδος ακολουθεί άμεσα την είσοδο.
- **Flip-Flop:** Πυροδοτείται αποκλειστικά στην ακμή του ρολογιού (Edge-triggered: θετική $\uparrow$ ή αρνητική $\downarrow$).

### 7.2 Χαρακτηριστικές Εξισώσεις & Πίνακες Διεγέρσεων
| Τύπος Flip-Flop | Χαρακτηριστική Εξίσωση $Q^+$ | Πίνακας Διεγέρσεων $Q \to Q^+$ |
| :---: | :---: | :---: |
| **D Flip-Flop** | $Q^+ = D$ | $0\to0: D=0, \quad 0\to1: D=1, \quad 1\to0: D=0, \quad 1\to1: D=1$ |
| **T Flip-Flop** | $Q^+ = T \oplus Q$ | $0\to0: T=0, \quad 0\to1: T=1, \quad 1\to0: T=1, \quad 1\to1: T=0$ |
| **JK Flip-Flop** | $Q^+ = J\overline{Q} + \overline{K}Q$ | $0\to0: (0,X), \quad 0\to1: (1,X), \quad 1\to0: (X,1), \quad 1\to1: (X,0)$ |
| **SR Latch/FF** | $Q^+ = S + \overline{R}Q \quad (SR=0)$ | $0\to0: (0,X), \quad 0\to1: (1,0), \quad 1\to0: (0,1), \quad 1\to1: (X,0)$ |

### 7.3 Παράμετροι Χρονισμού
- **Χρόνος Προετοιμασίας (Setup Time, $t_{su}$):** Ελάχιστος χρόνος που τα δεδομένα εισόδου πρέπει να είναι σταθερά **πριν** την ακμή του ρολογιού.
- **Χρόνος Συγκράτησης (Hold Time, $t_h$):** Ελάχιστος χρόνος που τα δεδομένα εισόδου πρέπει να παραμείνουν σταθερά **μετά** την ακμή του ρολογιού.
- **Καθυστέρηση Διάδοσης Ρολογιού σε Έξοδο ($t_{cq}$):** Χρόνος από την ακμή του ρολογιού μέχρι να αλλάξει η έξοδος $Q$.
- Παραβίαση των $t_{su}$ ή $t_h$ οδηγεί σε **μεταστάθεια (metastability)**.
"""
            ui.html(f'<div class="text-sm text-[var(--text-1)] leading-relaxed latex-target">{renderMathHtml(m7_content)}</div>')

        # MODULE 8: Registers & Counters
        with ui.column().classes("w-full glass-panel gap-4 p-6 border border-[var(--border)]"):
            with ui.row().classes("items-center gap-3 pb-2 border-b border-[var(--border)]"):
                ui.html('<i class="fa-solid fa-arrows-left-right text-[var(--blue-action)] text-xl"></i>')
                ui.html('<h2 class="text-lg md:text-xl font-bold text-[var(--text-1)] m-0">8. Καταχωρητές Ολίσθησης & Σύγχρονοι Μετρητές</h2>')

            m8_content = r"""
### 8.1 Καταχωρητές Ολίσθησης (Shift Registers)
Διατάξεις $n$ Flip-Flops σε σειρά για αποθήκευση και σειριακή/παράλληλη μεταφορά:
- **SISO:** Serial-In, Serial-Out.
- **SIPO:** Serial-In, Parallel-Out (μετατροπή σειριακού διαύλου σε παράλληλο).
- **PISO:** Parallel-In, Serial-Out.
- **PIPO:** Parallel-In, Parallel-Out (κλασικός καταχωρητής αποθήκευσης δεδομένων).
- **Ring Counter:** Κυκλική επανατροφοδότηση $Q_n \to D_1$. Μετρά $n$ καταστάσεις με $n$ Flip-Flops.
- **Johnson Counter:** Ανεστραμμένη επανατροφοδότηση $\overline{Q_n} \to D_1$. Μετρά $2n$ καταστάσεις με $n$ Flip-Flops.

### 8.2 Ασύγχρονοι (Ripple) έναντι Σύγχρονων Μετρητών
- **Ασύγχρονος (Ripple):** Το ρολόι εφαρμόζεται μόνο στο 1ο FF. Κάθε επόμενο FF οδηγείται από την έξοδο του προηγούμενου. Μειονέκτημα: συσσωρευτική καθυστέρηση διάδοσης $n \cdot t_{pd}$, προκαλώντας ακμές σφάλματος (ripples).
- **Σύγχρονος Μετρητής:** Κοινό σήμα ρολογιού $CLK$ συνδεδεμένο ταυτόχρονα σε όλα τα Flip-Flops. Όλες οι αλλαγές καταστάσεων συμβαίνουν συγχρονισμένα.

### 8.3 Μεθοδολογία Σχεδίασης Σύγχρονου Μετρητή Modulo-N
1. Προσδιορισμός αριθμού Flip-Flops: $2^m \ge N \implies m = \lceil \log_2 N \rceil$.
2. Κατασκευή πίνακα καταστάσεων $Q \to Q^+$.
3. Αντιστοίχιση διεγέρσεων βασιζόμενοι στον πίνακα διέγερσης του επιλεγμένου FF (π.χ. JK ή D).
4. Ελαχιστοποίηση με χάρτες Karnaugh, θεωρώντας τις υπόλοιπες $2^m - N$ καταστάσεις ως Don't Cares.
5. **Έλεγχος Αυτοδιόρθωσης (Self-Starting):** Επαλήθευση ότι αν ο μετρητής βρεθεί σε αχρησιμοποίητη κατάσταση, θα επανέλθει στον κύριο βρόχο εντός πεπερασμένων κύκλων (αποφυγή lockup/deadlock).
"""
            ui.html(f'<div class="text-sm text-[var(--text-1)] leading-relaxed latex-target">{renderMathHtml(m8_content)}</div>')

        # MODULE 9: Finite State Machines (FSM)
        with ui.column().classes("w-full glass-panel gap-4 p-6 border border-[var(--border)]"):
            with ui.row().classes("items-center gap-3 pb-2 border-b border-[var(--border)]"):
                ui.html('<i class="fa-solid fa-arrows-spin text-[var(--purple)] text-xl"></i>')
                ui.html('<h2 class="text-lg md:text-xl font-bold text-[var(--text-1)] m-0">9. Σύγχρονες Μηχανές Πεπερασμένων Καταστάσεων (Mealy & Moore FSM)</h2>')

            m9_content = r"""
### 9.1 Σύγκριση Μοντέλων Mealy και Moore
| Χαρακτηριστικό | Μηχανή Moore | Μηχανή Mealy |
| :---: | :---: | :---: |
| **Εξάρτηση Εξόδου** | Αποκλειστικά από την παρούσα κατάσταση: $Z = g(Q)$ | Από την κατάσταση και την είσοδο: $Z = g(Q, X)$ |
| **Συγχρονισμός Εξόδου** | Αυστηρά συγχρονισμένη με το ρολόι, Glitch-free | Μπορεί να εμφανίσει glitches αν η είσοδος μεταβληθεί ασύγχρονα |
| **Πλήθος Καταστάσεων** | Συνήθως απαιτεί $N+1$ καταστάσεις για μήκος ακολουθίας $N$ | Συνήθως απαιτεί $N$ καταστάσεις (πιο συμπαγής) |
| **Ταχύτητα Απόκρισης** | Η έξοδος εμφανίζεται 1 κύκλο ρολογιού αργότερα | Η έξοδος ενεργοποιείται στον ίδιο κύκλο με το τελευταίο bit |

### 9.2 Βήματα Σχεδίασης FSM (Design Cycle)
1. **Διατύπωση Προδιαγραφών:** Αναγνώριση εισόδων, εξόδων και απαίτησης επικάλυψης (overlapping vs non-overlapping).
2. **Διάγραμμα Καταστάσεων (State Diagram):** Ορισμός καταστάσεων με σαφή σημασία προθέματος.
3. **Ελαχιστοποίηση Καταστάσεων:** Απαλοιφή ισοδύναμων καταστάσεων μέσω πίνακα συνειρμών (implication table).
4. **Κωδικοποίηση Καταστάσεων (State Assignment):**
   - *Binary/Gray:* Ελάχιστος αριθμός Flip-Flops ($\lceil \log_2 K \rceil$).
   - *One-Hot:* 1 Flip-Flop ανά κατάσταση. Ιδανικό για FPGAs, ελαχιστοποιεί τη συνδυαστική λογική αποκωδικοποίησης.
5. **Εξαγωγή Εξισώσεων Διέγερσης:** Επίλυση K-maps για τα $D_i$ ή $J_i, K_i$ και την έξοδο $Z$.
"""
            ui.html(f'<div class="text-sm text-[var(--text-1)] leading-relaxed latex-target">{renderMathHtml(m9_content)}</div>')

        # MODULE 10 & 11: VHDL Synthesis & Idioms
        with ui.column().classes("w-full glass-panel gap-4 p-6 border border-[var(--border)]"):
            with ui.row().classes("items-center gap-3 pb-2 border-b border-[var(--border)]"):
                ui.html('<i class="fa-solid fa-code text-[var(--green-ok)] text-xl"></i>')
                ui.html('<h2 class="text-lg md:text-xl font-bold text-[var(--text-1)] m-0">10 & 11. Περιγραφή Υλικού σε VHDL: Συνδυαστική & Ακολουθιακή Σύνθεση</h2>')

            m10_content = r"""
### 10.1 Δομή Προγράμματος VHDL
Κάθε μονάδα VHDL αποτελείται από:
1. **Βιβλιοθήκες (Libraries):**
   ```vhdl
   library IEEE;
   use IEEE.STD_LOGIC_1164.ALL;
   use IEEE.NUMERIC_STD.ALL;
   ```
2. **Οντότητα (Entity):** Ορίζει τις θύρες (ports: `in`, `out`, `inout`, `buffer`) και το πλάτος τους.
3. **Αρχιτεκτονική (Architecture):** Περιγράφει τη λειτουργία (Dataflow, Behavioral ή Structural).

### 10.2 Παράλληλες (Concurrent) έναντι Σειριακών (Sequential) Εντολών
- **Εκτός διεργασίας (Concurrent):** Εκτελούνται όλες παράλληλα στον χρόνο προσομοίωσης:
  - Υπό συνθήκη ανάθεση: `y <= a when sel = '1' else b;`
  - Επιλεκτική ανάθεση: `with sel select y <= a when "00", b when "01", ...;`
- **Εντός διεργασίας (Sequential):** Εκτελούνται σειριακά μέσα σε `process(sensitivity_list)`:
  - `if ... then ... elsif ... else ... end if;`
  - `case ... is when ... => ... when others => ... end case;`

### 10.3 Αποτροπή Ανεπιθύμητων Μανδαλωτών (Latch Avoidance)
Σε συνδυαστική διεργασία (`combinational process`):
- **Κανόνας 1:** Όλα τα σήματα εισόδου που διαβάζονται μέσα στο process πρέπει να βρίσκονται στη λίστα ευαισθησίας.
- **Κανόνας 2:** Κάθε σήμα εξόδου **πρέπει να ανατίθεται σε όλους τους δυνατούς κλάδους** (κάθε `if` πρέπει να έχει πλήρες `else`, κάθε `case` πρέπει να έχει `when others =>`). Αν παραλειφθεί ανάθεση, το εργαλείο σύνθεσης παράγει latch!

### 10.4 Πρότυπο Δύο Διεργασιών για FSM (Two-Process Model)
```vhdl
-- Διεργασία 1: Σύγχρονος Καταχωρητής Κατάστασης με Ασύγχρονο Reset
process(clk, reset)
begin
    if reset = '1' then
        current_state <= S0;
    elsif rising_edge(clk) then
        current_state <= next_state;
    end if;
end process;

-- Διεργασία 2: Συνδυαστική Λογική Επόμενης Κατάστασης & Εξόδων
process(current_state, x)
begin
    next_state <= current_state;
    z <= '0';
    case current_state is
        when S0 => if x = '1' then next_state <= S1; end if;
        when S1 => if x = '0' then next_state <= S2; end if;
        when others => next_state <= S0;
    end case;
end process;
```
"""
            ui.html(f'<div class="text-sm text-[var(--text-1)] leading-relaxed latex-target">{renderMathHtml(m10_content)}</div>')

        # MODULE 12: FPGA Architecture & STA
        with ui.column().classes("w-full glass-panel gap-4 p-6 border border-[var(--border)]"):
            with ui.row().classes("items-center gap-3 pb-2 border-b border-[var(--border)]"):
                ui.html('<i class="fa-solid fa-microchip text-[var(--accent)] text-xl"></i>')
                ui.html('<h2 class="text-lg md:text-xl font-bold text-[var(--text-1)] m-0">12. Αρχιτεκτονική FPGA & Στατική Ανάλυση Χρονισμού (STA)</h2>')

            m12_content = r"""
### 12.1 Δομικά Στοιχεία FPGA
- **LUT (Look-Up Table):** Μικρή μνήμη SRAM (συνήθως 4-input ή 6-input LUT) που μπορεί να υλοποιήσει οποιαδήποτε συνδυαστική λογική συνάρτηση $k$ μεταβλητών ως πίνακα αληθείας.
- **CLB (Configurable Logic Block) / Slice:** Περιέχει πολλαπλά LUTs, Flip-Flops, πολυπλέκτες και ταχείες αλυσίδες διάδοσης κρατουμένων (Carry Chains).
- **Προγραμματιζόμενο Δίκτυο Διασυνδέσεων (Routing Matrix):** Συνδέει τα CLBs μεταξύ τους και με τα I/O blocks.

### 12.2 Στατική Ανάλυση Χρονισμού (Static Timing Analysis - STA)
Η μέγιστη συχνότητα λειτουργίας ενός σύγχρονου ψηφιακού κυκλώματος ($f_{max}$) περιορίζεται από τη διαδρομή μεταξύ δύο διαδοχικών Flip-Flops (Register-to-Register Path):
$$T_{clk} \ge t_{cq} + t_{\text{comb,max}} + t_{su} - t_{skew}$$
$$f_{max} = \frac{1}{T_{\text{clk,min}}} = \frac{1}{t_{cq} + t_{\text{comb,max}} + t_{su}}$$
- **Setup Slack:** $Slack_{\text{setup}} = T_{\text{required}} - T_{\text{arrival}} = (T_{clk} - t_{su}) - (t_{cq} + t_{comb})$. Πρέπει να είναι $\ge 0$!
- **Hold Slack:** $Slack_{\text{hold}} = (t_{cq} + t_{\text{comb,min}}) - t_h \ge 0$.
"""
            ui.html(f'<div class="text-sm text-[var(--text-1)] leading-relaxed latex-target">{renderMathHtml(m12_content)}</div>')

        # MODULE 13: Summary Cheatsheet & Pitfalls
        with ui.column().classes("w-full glass-panel gap-4 p-6 border border-[var(--border)]"):
            with ui.row().classes("items-center gap-3 pb-2 border-b border-[var(--border)]"):
                ui.html('<i class="fa-solid fa-triangle-exclamation text-red-500 text-xl"></i>')
                ui.html('<h2 class="text-lg md:text-xl font-bold text-[var(--text-1)] m-0">13. Οδηγός Αποφυγής Παγίδων Εξετάσεων (Exam Traps Checklist)</h2>')

            m13_content = r"""
- [ ] **Υπερχείλιση C2:** Μην συγχέετε το κρατούμενο εξόδου $C_{out}=1$ με την υπερχείλιση. Το $C_{out}=1$ είναι φυσιολογικό και απορρίπτεται. Υπερχείλιση υπάρχει **μόνο** όταν $C_{\text{in,msb}} \neq C_{\text{out,msb}}$.
- [ ] **K-Map Don't Cares:** Μην συμπεριλαμβάνετε don't cares ($d$) σε ομάδες αν δεν διπλασιάζουν το μέγεθος της ομάδας (δεν εξοικονομούν μεταβλητή). Ομάδα που περιέχει **μόνο** don't cares είναι σοβαρό λάθος!
- [ ] **Σύνθεση με NOR:** Θυμηθείτε ότι $F = \text{SOP} \implies$ εφαρμόζουμε διπλό συμπλήρωμα $F = \overline{\overline{F}}$ και De Morgan στον **εσωτερικό** όρο.
- [ ] **Επικάλυψη FSM (Overlapping):** Όταν ολοκληρωθεί η ακολουθία (π.χ. `101`), η FSM δεν επιστρέφει στην αρχική κατάσταση $S_0$, αλλά στην κατάσταση που αντιστοιχεί στο μέγιστο κατάλληλο πρόθεμα (εδώ $S_1$).
- [ ] **Αυτοδιόρθωση Μετρητών:** Ελέγχετε πάντα τις αχρησιμοποίητες καταστάσεις. Αν μια κατάσταση ανακυκλώνεται στον εαυτό της ή σε κλειστό βρόχο εκτός κύκλου μέτρησης, ο μετρητής δεν είναι αυτοδιορθούμενος.
- [ ] **VHDL Latches:** Σε συνδυαστική διεργασία `process`, κάθε σήμα εξόδου πρέπει να ανατίθεται ρητά σε όλες τις περιπτώσεις `if/else` και `case/when others`.
- [ ] **VHDL Reset:** Στο ασύγχροφο reset, το `if reset = '1'` ελέγχεται **πριν** από το `elsif rising_edge(clk)`. Στο σύγχρονο reset ελέγχεται **μετά**.
"""
            ui.html(f'<div class="text-sm text-[var(--text-1)] leading-relaxed latex-target">{renderMathHtml(m13_content)}</div>')

