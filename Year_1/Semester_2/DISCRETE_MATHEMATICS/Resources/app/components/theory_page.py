"""Master Theory & Syllabus Reference Handbook for Course 203: Discrete Mathematics.

Comprehensive reference covering the 7 fundamental course modules:
1. Foundations, Sets & Power Sets
2. Set Operations, Venn Diagrams & Principle of Inclusion-Exclusion (PIE)
3. Boolean Algebra, Logic Gates & Normal Forms (CNF/DNF)
4. Indexed Families of Sets & Well-Ordering Principle (WOP)
5. Propositional Logic, Truth Tables & Inference Rules
6. Graph Theory, Isomorphism, Euler Planarity & Trees
7. Automata, Formal Languages & Regular Expressions
"""

from nicegui import ui


def renderTheoryPage() -> None:
    """Renders the comprehensive Discrete Mathematics syllabus theory handbook.

    Returns:
        None
    """
    with ui.column().classes("w-full max-w-5xl mx-auto px-4 py-8 space-y-10"):
        # Header Banner
        with ui.column().classes("dash-card w-full p-6 gap-3 bg-gradient-to-r from-[var(--surface-2)] to-[var(--bg-card)] border-l-4 border-[var(--accent)]"):
            with ui.row().classes("items-center gap-3"):
                ui.html('<i class="fa-solid fa-book-open-reader text-2xl text-[var(--accent)]"></i>')
                ui.label("Οδηγός Θεωρίας & Μεθοδολογίας Ύλης (Course 203)").classes("text-xl md:text-2xl font-black")
            ui.label(
                "Συνοπτικό εγχειρίδιο θεωρητικών αρχών, αξιωμάτων, τυπολογίου και μεθοδολογιών επίλυσης θεμάτων "
                "για το μάθημα των Διακριτών Μαθηματικών."
            ).classes("text-xs text-[var(--text-2)] leading-relaxed")

        # Quick Navigation Bar
        with ui.row().classes("w-full gap-2 flex-wrap items-center"):
            ui.label("Ενότητες:").classes("text-xs font-bold text-[var(--text-3)]")
            sections = [
                ("1. Σύνολα & Θεμέλια", "#unit-1"),
                ("2. Πράξεις & PIE", "#unit-2"),
                ("3. Πύλες & Boole", "#unit-3"),
                ("4. Δεικτοδοτημένα & WOP", "#unit-4"),
                ("5. Προτασιακή Λογική", "#unit-5"),
                ("6. Θεωρία Γραφημάτων", "#unit-6"),
                ("7. Αυτόματα & RegEx", "#unit-7"),
            ]
            for title, anchor in sections:
                ui.html(f'<a href="{anchor}" class="kpi-badge hover:bg-[var(--surface-hover)] transition-all cursor-pointer">{title}</a>')

        # UNIT 1: Foundations, Sets & Power Sets
        with ui.column().classes("dash-card w-full p-6 gap-4").props('id="unit-1"'):
            with ui.row().classes("items-center gap-2 border-b border-[var(--border)] pb-2"):
                ui.html('<span class="px-2 py-0.5 rounded bg-[var(--accent)] text-white text-xs font-bold">Ενότητα 1</span>')
                ui.label("Θεμέλια, Θεωρία Συνόλων & Δυναμοσύνολα").classes("text-lg font-bold text-[var(--text-1)]")

            ui.html(r"""
            <div class="text-xs leading-relaxed space-y-3">
                <p><b>1.1 Ορισμός & Περιγραφή Συνόλου:</b> Ένα σύνολο $S$ είναι μία καλώς ορισμένη συλλογή διακριτών αντικειμένων. Περιγράφεται είτε με αναγραφή των στοιχείων του ($S = \\{x_1, x_2, \\dots\\}$) είτε με περιγραφική ιδιότητα ($S = \\{x \\in \\Omega \\mid P(x)\\}$).</p>
                <div class="callout-formula">
                    <b>Πληθικότητα & Κενό Σύνολο:</b><br/>
                    Το κενό σύνολο $\\emptyset = \\{\\}$ έχει πληθικότητα $|\\emptyset| = 0$ και αποτελεί υποσύνολο κάθε συνόλου: $\\forall A, \\emptyset \\subseteq A$.<br/>
                    <b>Προσοχή στην Παγίδα:</b> Το σύνολο $\\{\\emptyset\\}$ δεν είναι κενό! Έχει πληθικότητα $|\\{\\emptyset\\}| = 1$ διότι περιέχει ένα στοιχείο (το κενό σύνολο).
                </div>
                <p><b>1.2 Δυναμοσύνολο (Power Set):</b> Για κάθε πεπερασμένο σύνολο $S$, το δυναμοσύνολο $\\mathcal{P}(S)$ είναι το σύνολο όλων των υποσυνόλων του $S$.</p>
                <div class="callout-formula">
                    <b>Θεώρημα Πληθικότητας Δυναμοσυνόλου:</b><br/>
                    $$|\\mathcal{P}(S)| = 2^{|S|}$$<br/>
                    Αν $|S| = n$, το $\\mathcal{P}(S)$ περιέχει ακριβώς $2^n$ στοιχεία, συμπεριλαμβανομένων του $\\emptyset$ και του ίδιου του $S$.
                </div>
            </div>
            """)

        # UNIT 2: Set Operations, Venn Diagrams & PIE
        with ui.column().classes("dash-card w-full p-6 gap-4").props('id="unit-2"'):
            with ui.row().classes("items-center gap-2 border-b border-[var(--border)] pb-2"):
                ui.html('<span class="px-2 py-0.5 rounded bg-[var(--accent)] text-white text-xs font-bold">Ενότητα 2</span>')
                ui.label("Πράξεις Συνόλων, Διαγράμματα Venn & Αρχή Εγκλεισμού - Αποκλεισμού (PIE)").classes("text-lg font-bold text-[var(--text-1)]")

            ui.html(r"""
            <div class="text-xs leading-relaxed space-y-3">
                <p><b>2.1 Θεμελιώδεις Πράξεις:</b></p>
                <ul class="list-disc pl-5 space-y-1">
                    <li><b>Ένωση:</b> $A \\cup B = \\{x \\mid x \\in A \\lor x \\in B\\}$</li>
                    <li><b>Τομή:</b> $A \\cap B = \\{x \\mid x \\in A \\land x \\in B\\}$</li>
                    <li><b>Σχετική Διαφορά:</b> $A \\setminus B = \\{x \\mid x \\in A \\land x \\notin B\\}$</li>
                    <li><b>Συμμετρική Διαφορά:</b> $A \\oplus B = (A \\setminus B) \\cup (B \\setminus A) = (A \\cup B) \\setminus (A \\cap B)$</li>
                    <li><b>Συμπλήρωμα:</b> $A^c = \\Omega \\setminus A = \\{x \\in \\Omega \\mid x \\notin A\\}$</li>
                </ul>
                <div class="callout-formula">
                    <b>Αρχή Εγκλεισμού - Αποκλεισμού (PIE) για 3 Σύνολα:</b><br/>
                    $$|A \\cup B \\cup C| = |A| + |B| + |C| - (|A \\cap B| + |A \\cap C| + |B \\cap C|) + |A \\cap B \\cap C|$$<br/>
                    Αριθμός στοιχείων εκτός και των τριών συνόλων:
                    $$|(A \\cup B \\cup C)^c| = |\\Omega| - |A \\cup B \\cup C|$$
                </div>
            </div>
            """)

        # UNIT 3: Boolean Algebra & Logic Gates
        with ui.column().classes("dash-card w-full p-6 gap-4").props('id="unit-3"'):
            with ui.row().classes("items-center gap-2 border-b border-[var(--border)] pb-2"):
                ui.html('<span class="px-2 py-0.5 rounded bg-[var(--accent)] text-white text-xs font-bold">Ενότητα 3</span>')
                ui.label("Άλγεβρα Boole, Λογικές Πύλες & Κανονικές Μορφές").classes("text-lg font-bold text-[var(--text-1)]")

            ui.html(r"""
            <div class="text-xs leading-relaxed space-y-3">
                <p><b>3.1 Λογικές Πύλες:</b> AND ($\land$), OR ($\lor$), NOT ($\neg$), NAND ($\neg(p \land q)$), NOR ($\neg(p \lor q)$), XOR ($\oplus$).</p>
                <div class="callout-formula">
                    <b>Πληρότητα Πυλών NAND & NOR (Functional Completeness):</b><br/>
                    Οι πύλες NAND και NOR είναι καθολικές (universal gates). Οποιαδήποτε λογική έκφραση μπορεί να υλοποιηθεί αποκλειστικά με πύλες NAND ή αποκλειστικά με πύλες NOR.<br/>
                    $$\\neg p \\equiv p \\text{ NAND } p, \\quad p \\land q \\equiv (p \\text{ NAND } q) \\text{ NAND } (p \\text{ NAND } q)$$
                </div>
                <p><b>3.2 Κανονικές Μορφές:</b></p>
                <ul class="list-disc pl-5 space-y-1">
                    <li><b>Διαζευκτική Κανονική Μορφή (DNF / Minterms):</b> Άθροισμα γινομένων ($\bigvee \bigwedge l_i$). Κάθε όρος αντιστοιχεί σε γραμμή του πίνακα αληθείας με τιμή 1.</li>
                    <li><b>Συζευκτική Κανονική Μορφή (CNF / Maxterms):</b> Γινόμενο αθροισμάτων ($\bigwedge \bigvee l_i$). Κάθε όρος αντιστοιχεί σε γραμμή με τιμή 0.</li>
                </ul>
            </div>
            """)

        # UNIT 4: Indexed Sets & Well-Ordering Principle
        with ui.column().classes("dash-card w-full p-6 gap-4").props('id="unit-4"'):
            with ui.row().classes("items-center gap-2 border-b border-[var(--border)] pb-2"):
                ui.html('<span class="px-2 py-0.5 rounded bg-[var(--accent)] text-white text-xs font-bold">Ενότητα 4</span>')
                ui.label("Δεικτοδοτημένες Οικογένειες & Αρχή Καλής Διάταξης (WOP)").classes("text-lg font-bold text-[var(--text-1)]")

            ui.html(r"""
            <div class="text-xs leading-relaxed space-y-3">
                <p><b>4.1 Γενικευμένες Ενώσεις & Τομές:</b> Για οικογένεια συνόλων $\{A_i\}_{i \in I}$ με σύνολο δεικτών $I$:</p>
                $$\\bigcup_{i \\in I} A_i = \\{x \\mid \\exists i \\in I, x \\in A_i\\}, \\qquad \\bigcap_{i \\in I} A_i = \\{x \\mid \\forall i \\in I, x \\in A_i\\}$$
                <div class="callout-formula">
                    <b>Αρχή Καλής Διάταξης (Well-Ordering Principle - WOP):</b><br/>
                    Κάθε μη κενό υποσύνολο του συνόλου των μη αρνητικών ακεραίων $\\mathbb{N} = \\{0, 1, 2, \\dots\\}$ περιέχει ένα ελάχιστο στοιχείο.<br/>
                    $$S \\subseteq \\mathbb{N}, S \\neq \\emptyset \\implies \\exists m \\in S, \\forall x \\in S: m \\le x$$<br/>
                    Η WOP είναι λογικά ισοδύναμη με την Αρχή της Μαθηματικής Επαγωγής και χρησιμοποιείται εκτενώς σε αποδείξεις με απαγωγή σε άτοπο.
                </div>
            </div>
            """)

        # UNIT 5: Propositional Logic & Inference Rules
        with ui.column().classes("dash-card w-full p-6 gap-4").props('id="unit-5"'):
            with ui.row().classes("items-center gap-2 border-b border-[var(--border)] pb-2"):
                ui.html('<span class="px-2 py-0.5 rounded bg-[var(--accent)] text-white text-xs font-bold">Ενότητα 5</span>')
                ui.label("Προτασιακή Λογική, Ισοδυναμίες & Κανόνες Συμπερασμού").classes("text-lg font-bold text-[var(--text-1)]")

            ui.html(r"""
            <div class="text-xs leading-relaxed space-y-3">
                <div class="callout-formula">
                    <b>Θεμελιώδεις Κανόνες Συμπερασμού:</b><br/>
                    $$\\begin{array}{lcl}
                    \\text{Modus Ponens:} & p, \\; p \\to q & \\vdash q \\\\
                    \\text{Modus Tollens:} & \\neg q, \\; p \\to q & \\vdash \\neg p \\\\
                    \\text{Υποθετικός Συλλογισμός:} & p \\to q, \\; q \\to r & \\vdash p \\to r \\\\
                    \\text{Διαζευκτικός Συλλογισμός:} & p \\lor q, \\; \\neg p & \\vdash q \\\\
                    \\text{Κανόνας Επίλυσης (Resolution):} & p \\lor q, \\; \\neg p \\lor r & \\vdash q \\lor r
                    \\end{array}$$
                </div>
                <div class="callout-gotcha">
                    <b>Παγίδα Συνεπαγωγής:</b> Η συνεπαγωγή $p \\to q$ είναι ψευδής <b>μόνο</b> όταν $p$ είναι αληθής και $q$ είναι ψευδής ($T \\to F \\equiv F$). Σε όλες τις άλλες περιπτώσεις ($F \\to F, F \\to T, T \\to T$) είναι αληθής!
                </div>
            </div>
            """)

        # UNIT 6: Graph Theory & Trees
        with ui.column().classes("dash-card w-full p-6 gap-4").props('id="unit-6"'):
            with ui.row().classes("items-center gap-2 border-b border-[var(--border)] pb-2"):
                ui.html('<span class="px-2 py-0.5 rounded bg-[var(--accent)] text-white text-xs font-bold">Ενότητα 6</span>')
                ui.label("Θεωρία Γραφημάτων, Ισομορφισμός, Επίπεδοι Γράφοι & Δέντρα").classes("text-lg font-bold text-[var(--text-1)]")

            ui.html(r"""
            <div class="text-xs leading-relaxed space-y-3">
                <div class="callout-formula">
                    <b>Θεώρημα Χειραψιών (Handshaking Theorem):</b><br/>
                    Σε κάθε μη κατευθυνόμενο γράφημα $G = (V, E)$, το άθροισμα των βαθμών όλων των κορυφών ισούται με το διπλάσιο του αριθμού των ακμών:<br/>
                    $$\\sum_{v \\in V} \\deg(v) = 2|E|$$<br/>
                    <b>Πόρισμα:</b> Ο αριθμός των κορυφών με περιττό βαθμό είναι πάντα άρτιος.
                </div>
                <div class="callout-formula">
                    <b>Τύπος Euler για Επίπεδους Γράφους:</b><br/>
                    Για κάθε συνεκτικό επίπεδο γράφημα με $V$ κορυφές, $E$ ακμές και $R$ περιοχές (συμπεριλαμβανομένης της εξωτερικής/άπειρης περιοχής):<br/>
                    $$V - E + R = 2$$<br/>
                    <b>Αναγκαία Συνθήκη Επιπεδότητας ($V \\ge 3$ χωρίς πολλαπλές ακμές):</b> $E \\le 3V - 6$.
                </div>
                <div class="callout-formula">
                    <b>Κυκλώματα Euler & Hamilton:</b><br/>
                    <b>Euler:</b> Περιέχει κάθε ακμή ακριβώς μία φορά. Υπάρχει αν και μόνο αν ο γράφος είναι συνεκτικός και <i>κάθε κορυφή έχει άρτιο βαθμό</i>.<br/>
                    <b>Hamilton:</b> Περιέχει κάθε κορυφή ακριβώς μία φορά (εκτός από την κορυφή εκκίνησης/τέλους).
                </div>
            </div>
            """)

        # UNIT 7: Automata & Formal Languages
        with ui.column().classes("dash-card w-full p-6 gap-4").props('id="unit-7"'):
            with ui.row().classes("items-center gap-2 border-b border-[var(--border)] pb-2"):
                ui.html('<span class="px-2 py-0.5 rounded bg-[var(--accent)] text-white text-xs font-bold">Ενότητα 7</span>')
                ui.label("Πεπερασμένα Αυτόματα (DFA/NFA) & Κανονικές Εκφράσεις").classes("text-lg font-bold text-[var(--text-1)]")

            ui.html(r"""
            <div class="text-xs leading-relaxed space-y-3">
                <p><b>7.1 Ντετερμινιστικό Πεπερασμένο Αυτόματο (DFA):</b> Ορίζεται ως 5-άδα $M = (Q, \\Sigma, \\delta, q_0, F)$ όπου $Q$ είναι το σύνολο καταστάσεων, $\\Sigma$ το αλφάβητο, $\\delta: Q \\times \\Sigma \\to Q$ η συνάρτηση μετάβασης, $q_0 \\in Q$ η αρχική κατάσταση, και $F \\subseteq Q$ οι τελικές/αποδεκτές καταστάσεις.</p>
                <div class="callout-formula">
                    <b>Κανονικές Εκφράσεις (Regular Expressions):</b><br/>
                    Βασικές πράξεις: Συνένωση ($ab$), Διάζευξη ($a \\mid b$), Αστέρι Kleene ($a^* = \\{\\epsilon, a, aa, \\dots\\}$).<br/>
                    <b>Θεώρημα Kleene:</b> Μία γλώσσα είναι κανονική αν και μόνο αν αναγνωρίζεται από κάποιο DFA ή περιγράφεται από κανονική έκφραση.
                </div>
            </div>
            """)
