"""Master Theory & Syllabus Reference Handbook for Course 203: Discrete Mathematics.

Comprehensive and compact reference covering the 7 fundamental course modules:
1. Foundations, Sets & Power Sets (01_foundations_and_sets.md)
2. Set Operations, Venn Diagrams & Principle of Inclusion-Exclusion (PIE) (02_set_operations_and_venn.md)
3. Boolean Algebra, Logic Gates & Normal Forms (CNF/DNF) (03_logic_gates.md)
4. Indexed Families of Sets & Well-Ordering Principle (WOP) (04_indexed_sets_and_well_ordering.md)
5. Propositional Logic, Truth Tables & Rules of Inference (05_propositional_logic.md)
6. Graph Theory, Isomorphism, Euler Planarity & Trees (06_graph_theory.md)
7. Automata, Formal Languages & Regular Expressions (07_automata_and_formal_languages.md)
"""

from nicegui import ui


def renderTheoryPage() -> None:
    """Renders the comprehensive Discrete Mathematics syllabus theory handbook.

    Returns:
        None
    """
    with ui.column().classes("w-full px-5 py-8 space-y-8 items-stretch"):
        # Header Banner
        with ui.column().classes("dash-card w-full p-6 gap-3 bg-gradient-to-r from-[var(--surface-2)] to-[var(--bg-card)] border-l-4 border-[var(--accent)]"):
            with ui.row().classes("items-center gap-3"):
                ui.html('<i class="fa-solid fa-book-open-reader text-2xl text-[var(--accent)]"></i>')
                ui.label("Οδηγός Θεωρίας & Μεθοδολογίας Ύλης (Course 203)").classes("text-xl md:text-2xl font-black")
            ui.label(
                "Συμπυκνωμένο εγχειρίδιο θεωρητικών αρχών, τυπολογίου, ορισμών και μεθοδολογιών επίλυσης "
                "από το σύνολο των σημειώσεων του μαθήματος των Διακριτών Μαθηματικών."
            ).classes("text-xs text-[var(--text-2)] leading-relaxed")

        # Quick Navigation Bar
        with ui.row().classes("w-full gap-2 flex-wrap items-center"):
            ui.label("Ενότητες:").classes("text-xs font-bold text-[var(--text-3)]")
            sections = [
                ("1. Σύνολα & Θεμέλια", "#unit-1"),
                ("2. Πράξεις, Venn & PIE", "#unit-2"),
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
                ui.label("Θεμελιώδη Στοιχεία Θεωρίας Συνόλων & Δυναμοσύνολα").classes("text-lg font-bold text-[var(--text-1)]")

            ui.html(r"""
            <div class="text-xs leading-relaxed space-y-3">
                <p><b>1.1 Ορισμός & Περιγραφή Συνόλου:</b> Ένα σύνολο $S$ είναι καλώς ορισμένη συλλογή διακριτών αντικειμένων. Περιγράφεται είτε με αναγραφή στοιχείων ($S = \{a, b, c\}$) είτε με περιγραφική ιδιότητα ($S = \{x \in \Omega \mid P(x)\}$).</p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                    <div class="callout-formula">
                        <b>Σχέσεις Συνόλων:</b><br/>
                        • <b>Υποσύνολο:</b> $A \subseteq B \iff \forall x (x \in A \to x \in B)$<br/>
                        • <b>Γνήσιο Υποσύνολο:</b> $A \subset B \iff (A \subseteq B \land A \neq B)$<br/>
                        • <b>Ισότητα Συνόλων:</b> $A = B \iff (A \subseteq B \land B \subseteq A)$<br/>
                        • <b>Κενό Σύνολο ($\emptyset$):</b> $|\emptyset| = 0$. Ισχύει πάντα: $\forall A, \ \emptyset \subseteq A$.
                    </div>
                    <div class="callout-gotcha">
                        <b>Παγίδες Κενού Συνόλου:</b><br/>
                        • $\emptyset \neq \{\emptyset\}$: Το $\emptyset$ έχει 0 στοιχεία, ενώ το $\{\emptyset\}$ έχει 1 στοιχείο.<br/>
                        • $\emptyset \subseteq A$ (αληθές για κάθε σύνολο $A$).<br/>
                        • $\emptyset \in A$ είναι αληθές <i>μόνο</i> αν το ίδιο το σύμβολο $\emptyset$ περιέχεται ως στοιχείο στο $A$.
                    </div>
                </div>
                <div class="callout-formula">
                    <b>Δυναμοσύνολο (Power Set) $\mathcal{P}(S)$:</b><br/>
                    Το σύνολο όλων των υποσυνόλων του $S$: $\mathcal{P}(S) = \{X \mid X \subseteq S\}$.<br/>
                    <b>Θεώρημα Πληθικότητας:</b> Αν $|S| = n$, τότε $|\mathcal{P}(S)| = 2^n$.<br/>
                    <i>Παραδείγματα:</i> $\mathcal{P}(\emptyset) = \{\emptyset\}$ (μέγεθος $2^0 = 1$), $\mathcal{P}(\{a\}) = \{\emptyset, \{a\}\}$ (μέγεθος $2^1 = 2$), $\mathcal{P}(\{a, b\}) = \{\emptyset, \{a\}, \{b\}, \{a, b\}\}$ (μέγεθος $2^2 = 4$).
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
                <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                    <div class="callout-formula">
                        <b>Βασικές Πράξεις Συνόλων:</b><br/>
                        • <b>Ένωση:</b> $A \cup B = \{x \mid x \in A \lor x \in B\}$<br/>
                        • <b>Τομή:</b> $A \cap B = \{x \mid x \in A \land x \in B\}$<br/>
                        • <b>Σχετική Διαφορά:</b> $A \setminus B = \{x \mid x \in A \land x \notin B\}$<br/>
                        • <b>Συμπλήρωμα:</b> $A^c = \overline{A} = \Omega \setminus A = \{x \in \Omega \mid x \notin A\}$<br/>
                        • <b>Συμμετρική Διαφορά:</b> $A \oplus B = (A \setminus B) \cup (B \setminus A) = (A \cup B) \setminus (A \cap B)$
                    </div>
                    <div class="callout-formula">
                        <b>Ταυτότητες Boole για Σύνολα:</b><br/>
                        • <b>Νόμοι De Morgan:</b> $\overline{A \cup B} = \overline{A} \cap \overline{B}, \quad \overline{A \cap B} = \overline{A} \cup \overline{B}$<br/>
                        • <b>Επιμεριστικοί:</b> $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$<br/>
                        • <b>Απορρόφησης:</b> $A \cup (A \cap B) = A, \quad A \cap (A \cup B) = A$<br/>
                        • <b>Διπλού Συμπληρώματος:</b> $\overline{\overline{A}} = A$
                    </div>
                </div>
                <div class="callout-formula">
                    <b>Αρχή Εγκλεισμού - Αποκλεισμού (Principle of Inclusion-Exclusion - PIE):</b><br/>
                    • <b>Για 2 σύνολα:</b> $|A \cup B| = |A| + |B| - |A \cap B|$<br/>
                    • <b>Για 3 σύνολα:</b><br/>
                    $$|A \cup B \cup C| = |A| + |B| + |C| - (|A \cap B| + |A \cap C| + |B \cap C|) + |A \cap B \cap C|$$<br/>
                    • <b>Στοιχεία εκτός των τριών συνόλων:</b> $|(A \cup B \cup C)^c| = |\Omega| - |A \cup B \cup C|$<br/>
                    • <b>Ακριβώς σε ένα σύνολο:</b> $|A| + |B| + |C| - 2(|A \cap B| + |A \cap C| + |B \cap C|) + 3|A \cap B \cap C|$<br/>
                    • <b>Ακριβώς σε δύο σύνολα:</b> $(|A \cap B| + |A \cap C| + |B \cap C|) - 3|A \cap B \cap C|$
                </div>
            </div>
            """)

        # UNIT 3: Boolean Algebra, Logic Gates & Normal Forms
        with ui.column().classes("dash-card w-full p-6 gap-4").props('id="unit-3"'):
            with ui.row().classes("items-center gap-2 border-b border-[var(--border)] pb-2"):
                ui.html('<span class="px-2 py-0.5 rounded bg-[var(--accent)] text-white text-xs font-bold">Ενότητα 3</span>')
                ui.label("Λογικές Πύλες, Άλγεβρα Boole & Κανονικές Μορφές (CNF/DNF)").classes("text-lg font-bold text-[var(--text-1)]")

            ui.html(r"""
            <div class="text-xs leading-relaxed space-y-3">
                <p><b>3.1 Οι Επτά Βασικές Λογικές Πύλες (2 Εισόδων):</b></p>
                <div class="overflow-x-auto">
                    <table class="truth-table w-full text-xs">
                        <thead>
                            <tr>
                                <th>Πύλη</th><th>Έκφραση Boolean</th><th>00</th><th>01</th><th>10</th><th>11</th><th>Κανόνας Εξόδου</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr><td><b>AND</b></td><td>$Y = A \cdot B$</td><td>0</td><td>0</td><td>0</td><td class="val-true">1</td><td>1 μόνο αν και οι δύο είσοδοι είναι 1</td></tr>
                            <tr><td><b>OR</b></td><td>$Y = A + B$</td><td>0</td><td class="val-true">1</td><td class="val-true">1</td><td class="val-true">1</td><td>1 αν τουλάχιστον μία είσοδος είναι 1</td></tr>
                            <tr><td><b>NOT</b></td><td>$Y = \overline{A}$</td><td colspan="4" class="text-center">0 &rarr; 1, \quad 1 &rarr; 0</td><td>Αντιστρέφει τη μία και μοναδική είσοδο</td></tr>
                            <tr><td><b>NAND</b></td><td>$Y = \overline{A \cdot B}$</td><td class="val-true">1</td><td class="val-true">1</td><td class="val-true">1</td><td>0</td><td>0 μόνο αν και οι δύο είσοδοι είναι 1</td></tr>
                            <tr><td><b>NOR</b></td><td>$Y = \overline{A + B}$</td><td class="val-true">1</td><td>0</td><td>0</td><td>0</td><td>1 μόνο αν και οι δύο είσοδοι είναι 0</td></tr>
                            <tr><td><b>XOR</b></td><td>$Y = A \oplus B = \overline{A}B + A\overline{B}$</td><td>0</td><td class="val-true">1</td><td class="val-true">1</td><td>0</td><td>1 όταν οι είσοδοι διαφέρουν</td></tr>
                            <tr><td><b>XNOR</b></td><td>$Y = \overline{A \oplus B} = AB + \overline{A}\,\overline{B}$</td><td class="val-true">1</td><td>0</td><td>0</td><td class="val-true">1</td><td>1 όταν οι είσοδοι ταυτίζονται</td></tr>
                        </tbody>
                    </table>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                    <div class="callout-formula">
                        <b>Καθολικές Πύλες (Functional Completeness):</b><br/>
                        Οι πύλες NAND και NOR είναι καθολικές (universal). Μπορούν να υλοποιήσουν οποιαδήποτε λογική συνάρτηση:<br/>
                        • $\text{NOT}(A) = A \text{ NAND } A$<br/>
                        • $\text{AND}(A, B) = \overline{A \text{ NAND } B} = (A \text{ NAND } B) \text{ NAND } (A \text{ NAND } B)$<br/>
                        • $\text{OR}(A, B) = (A \text{ NAND } A) \text{ NAND } (B \text{ NAND } B)$
                    </div>
                    <div class="callout-formula">
                        <b>Κανονικές Μορφές (Canonical Forms):</b><br/>
                        • <b>Διαζευκτική Κανονική Μορφή (DNF / SOP):</b> Άθροισμα ελαχιστόρων (minterms $m_i$). Κάθε $m_i$ αντιστοιχεί σε γραμμή του πίνακα με τιμή 1.<br/>
                        • <b>Συζευκτική Κανονική Μορφή (CNF / POS):</b> Γινόμενο μεγιστόρων (maxterms $M_i$). Κάθε $M_i$ αντιστοιχεί σε γραμμή του πίνακα με τιμή 0.<br/>
                        • <b>Συμπληρωματικότητα:</b> $\overline{m_i} = M_i$.
                    </div>
                </div>
            </div>
            """)

        # UNIT 4: Indexed Sets & Well-Ordering Principle
        with ui.column().classes("dash-card w-full p-6 gap-4").props('id="unit-4"'):
            with ui.row().classes("items-center gap-2 border-b border-[var(--border)] pb-2"):
                ui.html('<span class="px-2 py-0.5 rounded bg-[var(--accent)] text-white text-xs font-bold">Ενότητα 4</span>')
                ui.label("Δεικτοδοτημένες Οικογένειες & Αρχή Καλής Διάταξης (WOP)").classes("text-lg font-bold text-[var(--text-1)]")

            ui.html(r"""
            <div class="text-xs leading-relaxed space-y-3">
                <p><b>4.1 Γενικευμένες Πράξεις Δεικτοδοτημένων Συνόλων:</b> Για οικογένεια συνόλων $\{A_i\}_{i \in I}$ με σύνολο δεικτών $I$:</p>
                <div class="callout-formula">
                    $$\bigcup_{i \in I} A_i = \{x \mid \exists i \in I: x \in A_i\}, \qquad \bigcap_{i \in I} A_i = \{x \mid \forall i \in I: x \in A_i\}$$
                    <b>Γενικευμένοι Νόμοι De Morgan:</b>
                    $$\left(\bigcup_{i \in I} A_i\right)^c = \bigcap_{i \in I} A_i^c, \qquad \left(\bigcap_{i \in I} A_i\right)^c = \bigcup_{i \in I} A_i^c$$
                </div>
                <div class="callout-formula">
                    <b>Αρχή Καλής Διάταξης (Well-Ordering Principle - WOP):</b><br/>
                    <i>«Κάθε μη κενό υποσύνολο των μη αρνητικών ακεραίων $\mathbb{N} = \{0, 1, 2, \dots\}$ περιέχει ένα ελάχιστο στοιχείο».</i><br/>
                    $$\forall S \subseteq \mathbb{N}, \ (S \neq \emptyset \implies \exists m \in S, \ \forall x \in S: m \le x)$$<br/>
                    • <b>Λογική Ισοδυναμία:</b> Η WOP είναι λογικά ισοδύναμη με την Αρχή της Μαθηματικής Επαγωγής και την Ισχυρή Επαγωγή.<br/>
                    • <b>Μεθοδολογία Απόδειξης με WOP (Εις Άτοπον):</b> Έστω $C = \{n \in \mathbb{N} \mid \neg P(n)\}$ το σύνολο των αντιπαραδειγμάτων. Υποθέτουμε $C \neq \emptyset$. Από WOP, υπάρχει ελάχιστο στοιχείο $m = \min(C)$. Κατασκευάζουμε μικρότερο αντιπαράδειγμα $m' < m$ ή καταλήγουμε σε αντίφαση $\implies C = \emptyset$, άρα $P(n)$ αληθές για κάθε $n$.
                </div>
            </div>
            """)

        # UNIT 5: Propositional Logic & Inference Rules
        with ui.column().classes("dash-card w-full p-6 gap-4").props('id="unit-5"'):
            with ui.row().classes("items-center gap-2 border-b border-[var(--border)] pb-2"):
                ui.html('<span class="px-2 py-0.5 rounded bg-[var(--accent)] text-white text-xs font-bold">Ενότητα 5</span>')
                ui.label("Προτασιακή Λογική, Ισοδυναμίες & Κανόνες Συμπερασμού").classes("text-lg font-bold text-[var(--text-1)]")

            ui.html(r"""
            <div class="text-xs leading-relaxed space-y-4">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                    <div class="callout-formula">
                        <b>Παραλλαγές της Συνεπαγωγής $p \to q$:</b><br/>
                        • <b>Αρχική Συνεπαγωγή:</b> $p \to q$ (Ψευδής μόνο όταν $p=1, q=0$)<br/>
                        • <b>Αντιθετοαντίστροφη:</b> $\neg q \to \neg p \equiv p \to q$ (<b>Λογικά Ισοδύναμη!</b>)<br/>
                        • <b>Αντίστροφη:</b> $q \to p$ (<b>ΔΕΝ</b> είναι ισοδύναμη με την αρχική)<br/>
                        • <b>Αρνητική Αντίστροφη:</b> $\neg p \to \neg q \equiv q \to p$
                    </div>
                    <div class="callout-formula">
                        <b>Θεμελιώδεις Λογικές Ισοδυναμίες:</b><br/>
                        • <b>Συνεπαγωγής:</b> $p \to q \equiv \neg p \lor q$<br/>
                        • <b>Ισοδυναμίας:</b> $p \leftrightarrow q \equiv (p \to q) \land (q \to p)$<br/>
                        • <b>De Morgan:</b> $\neg(p \land q) \equiv \neg p \lor \neg q, \quad \neg(p \lor q) \equiv \neg p \land \neg q$<br/>
                        • <b>Επιμεριστικότητας:</b> $p \land (q \lor r) \equiv (p \land q) \lor (p \land r)$<br/>
                        • <b>Εξαγωγής (Exportation):</b> $(p \land q) \to r \equiv p \to (q \to r)$
                    </div>
                </div>

                <div>
                    <p class="font-bold text-xs mb-1">Πίνακας Κανόνων Συμπερασμού (Rules of Inference):</p>
                    <div class="overflow-x-auto">
                        <table class="truth-table w-full text-xs">
                            <thead>
                                <tr>
                                    <th>Κανόνας Συμπερασμού</th>
                                    <th>Προκείμενες (Υποθέσεις)</th>
                                    <th>Συμπέρασμα</th>
                                    <th>Μορφή Ταυτολογίας</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><b>Modus Ponens (Κατάφαση)</b></td>
                                    <td>$p, \quad p \to q$</td>
                                    <td>$\therefore q$</td>
                                    <td>$(p \land (p \to q)) \to q$</td>
                                </tr>
                                <tr>
                                    <td><b>Modus Tollens (Άρνηση)</b></td>
                                    <td>$\neg q, \quad p \to q$</td>
                                    <td>$\therefore \neg p$</td>
                                    <td>$(\neg q \land (p \to q)) \to \neg p$</td>
                                </tr>
                                <tr>
                                    <td><b>Υποθετικός Συλλογισμός (Hypothetical Syllogism)</b></td>
                                    <td>$p \to q, \quad q \to r$</td>
                                    <td>$\therefore p \to r$</td>
                                    <td>$((p \to q) \land (q \to r)) \to (p \to r)$</td>
                                </tr>
                                <tr>
                                    <td><b>Διαζευκτικός Συλλογισμός (Disjunctive Syllogism)</b></td>
                                    <td>$p \lor q, \quad \neg p$</td>
                                    <td>$\therefore q$</td>
                                    <td>$((p \lor q) \land \neg p) \to q$</td>
                                </tr>
                                <tr>
                                    <td><b>Κανόνας Επίλυσης (Resolution)</b></td>
                                    <td>$p \lor q, \quad \neg p \lor r$</td>
                                    <td>$\therefore q \lor r$</td>
                                    <td>$((p \lor q) \land (\neg p \lor r)) \to (q \lor r)$</td>
                                </tr>
                                <tr>
                                    <td><b>Πρόσθεση (Addition)</b></td>
                                    <td>$p$</td>
                                    <td>$\therefore p \lor q$</td>
                                    <td>$p \to (p \lor q)$</td>
                                </tr>
                                <tr>
                                    <td><b>Απλοποίηση (Simplification)</b></td>
                                    <td>$p \land q$</td>
                                    <td>$\therefore p$</td>
                                    <td>$(p \land q) \to p$</td>
                                </tr>
                                <tr>
                                    <td><b>Σύζευξη (Conjunction)</b></td>
                                    <td>$p, \quad q$</td>
                                    <td>$\therefore p \land q$</td>
                                    <td>$((p) \land (q)) \to (p \land q)$</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
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
                <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                    <div class="callout-formula">
                        <b>Βασικές Έννοιες & Βαθμοί:</b><br/>
                        • Γράφημα $G = (V, E)$, $|V|$ κορυφές, $|E|$ ακμές.<br/>
                        • <b>Θεώρημα Χειραψιών (Handshaking):</b> $\sum_{v \in V} \deg(v) = 2|E|$.<br/>
                        • <b>Πόρισμα:</b> Ο αριθμός των κορυφών με περιττό βαθμό είναι <b>πάντα άρτιος</b>.<br/>
                        • <b>Κατευθυνόμενοι Γράφοι:</b> $\sum \deg^-(v) = \sum \deg^+(v) = |E|$.<br/>
                        • <b>Διμερείς Γράφοι (Bipartite):</b> $V = V_1 \cup V_2$. Χαρακτηρισμός: Δεν περιέχει κανέναν περιττό κύκλο.
                    </div>
                    <div class="callout-formula">
                        <b>Ισομορφισμός Γραφημάτων ($G_1 \cong G_2$):</b><br/>
                        Αμφιμονοσήμαντη συνάρτηση $f: V_1 \to V_2$ που διατηρεί τη γειτνίαση: $\{u, v\} \in E_1 \iff \{f(u), f(v)\} \in E_2$.<br/>
                        <b>Αναλλοίωτα Ισομορφισμού (Invariants):</b><br/>
                        1. Ίδιο πλήθος κορυφών ($|V_1| = |V_2|$) και ακμών ($|E_1| = |E_2|$).<br/>
                        2. Ίδια ταξινομημένη ακολουθία βαθμών.<br/>
                        3. Ίδιο πλήθος κύκλων μήκους $k$ (π.χ. τρίγωνα, τετράγωνα).
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                    <div class="callout-formula">
                        <b>Επίπεδοι Γράφοι (Planar Graphs) & Euler:</b><br/>
                        • <b>Τύπος Euler:</b> Για κάθε συνεκτικό επίπεδο γράφο:
                        $$V - E + R = 2 \quad (R: \text{αριθμός περιοχών μαζί με την εξωτερική})$$
                        • <b>Όριο Ακμών (για $V \ge 3$ χωρίς πολλαπλές ακμές):</b> $E \le 3V - 6$.<br/>
                        • <b>Χωρίς τρίγωνα (ή διμερής):</b> $E \le 2V - 4$.<br/>
                        • <b>Θεώρημα Kuratowski:</b> Ένας γράφος είναι επίπεδος αν και μόνο αν δεν περιέχει υπογράφο ομοιόμορφο με το $K_5$ ή το $K_{3,3}$.
                    </div>
                    <div class="callout-formula">
                        <b>Κυκλώματα Euler & Hamilton:</b><br/>
                        • <b>Κύκλωμα Euler:</b> Διασχίζει κάθε <i>ακμή</i> ακριβώς 1 φορά. Υπάρχει $\iff$ ο γράφος είναι συνεκτικός και <b>κάθε κορυφή έχει άρτιο βαθμό</b>.<br/>
                        • <b>Μονοπάτι Euler:</b> Υπάρχει $\iff$ ακριβώς <b>δύο κορυφές</b> έχουν περιττό βαθμό.<br/>
                        • <b>Κύκλωμα Hamilton:</b> Επισκέπτεται κάθε <i>κορυφή</i> ακριβώς 1 φορά. Ικανή συνθήκη Dirac: $\deg(v) \ge n/2$ για κάθε $v$.
                    </div>
                </div>
                <div class="callout-formula">
                    <b>Δέντρα (Trees):</b> Συνεκτικοί γράφοι χωρίς κύκλους. Ιδιότητες: $|E| = |V| - 1$. Υπάρχει ακριβώς ένα απλό μονοπάτι μεταξύ οποιωνδήποτε δύο κορυφών.
                </div>
            </div>
            """)

        # UNIT 7: Automata & Formal Languages
        with ui.column().classes("dash-card w-full p-6 gap-4").props('id="unit-7"'):
            with ui.row().classes("items-center gap-2 border-b border-[var(--border)] pb-2"):
                ui.html('<span class="px-2 py-0.5 rounded bg-[var(--accent)] text-white text-xs font-bold">Ενότητα 7</span>')
                ui.label("Πεπερασμένα Αυτόματα (DFA/NFA) & Κανονικές Εκφράσεις (RegEx)").classes("text-lg font-bold text-[var(--text-1)]")

            ui.html(r"""
            <div class="text-xs leading-relaxed space-y-3">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                    <div class="callout-formula">
                        <b>Κανονικές Εκφράσεις (RegEx):</b><br/>
                        • <b>Συνένωση ($ab$):</b> Το $a$ ακολουθούμενο από το $b$.<br/>
                        • <b>Διάζευξη ($a \mid b$ ή $a + b$):</b> Είτε $a$ είτε $b$.<br/>
                        • <b>Αστέρι Kleene ($a^*$):</b> Μηδέν ή περισσότερες εμφανίσεις: $\{\epsilon, a, aa, aaa, \dots\}$.<br/>
                        • <b>Συν Kleene ($a^+$):</b> Μία ή περισσότερες εμφανίσεις: $a^+ = aa^*$.<br/>
                        • <b>Προτεραιότητα:</b> $() > * > \text{Συνένωση} > \mid$
                    </div>
                    <div class="callout-formula">
                        <b>Ντετερμινιστικό Πεπερασμένο Αυτόματο (DFA):</b><br/>
                        Πεντάδα $M = (Q, \Sigma, \delta, q_0, F)$ όπου:<br/>
                        • $Q$: Πεπερασμένο σύνολο καταστάσεων.<br/>
                        • $\Sigma$: Αλφάβητο εισόδου.<br/>
                        • $\delta: Q \times \Sigma \to Q$: Συνάρτηση μετάβασης (ακριβώς 1 επόμενη κατάσταση ανά σύμβολο).<br/>
                        • $q_0 \in Q$: Αρχική κατάσταση.<br/>
                        • $F \subseteq Q$: Σύνολο αποδεκτών (τελικών) καταστάσεων.
                    </div>
                </div>
                <div class="callout-formula">
                    <b>Θεώρημα Kleene & Ισοδυναμία:</b><br/>
                    Μία γλώσσα $L$ είναι <b>κανονική</b> αν και μόνο αν αναγνωρίζεται από ένα DFA, ή αναγνωρίζεται από ένα NFA, ή περιγράφεται από μία Κανονική Έκφραση (RegEx):<br/>
                    $$\text{DFA} \equiv \text{NFA} \equiv \text{RegEx}$$<br/>
                    • <b>Μετατροπή NFA σε DFA:</b> Υλοποιείται με την κατασκευή υποσυνόλων (Powerset / Subset Construction). Αν το NFA έχει $k$ καταστάσεις, το ισοδύναμο DFA έχει το πολύ $2^k$ καταστάσεις.
                </div>
            </div>
            """)
