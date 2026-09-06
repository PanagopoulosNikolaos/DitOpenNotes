"""Mock Exam 2 (Standard) scenario module for Discrete Mathematics.

Transcribes Mock Exam 2 verbatim with interactive highlights, and provides
step-by-step master solutions across Groups A, B, C, D for all 3 questions.
"""

from models.scenario import (
    Scenario,
    Paragraph,
    TextSegment,
    ExamQuestion,
    CalculationStep,
    GivenParameter,
    DiagramNode,
    DiagramEdge,
    DesignJustification,
)


def createMockExam2StandardScenario() -> Scenario:
    """Constructs the Scenario instance for Mock Exam 2 (Standard).

    Returns:
        Scenario: Complete scenario with verbatim text, annotations, and worked solutions.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Τμήμα Πληροφορικής και Τηλεπικοινωνιών — Πανεπιστήμιο Ιωαννίνων\n"),
                TextSegment(text="Σπυρίδων Τζίμας • Εαρινό Εξάμηνο 2025\n"),
                TextSegment(text="203: Διακριτά Μαθηματικά — Εικονική Εξέταση 2 (Κανονική)\n\n"),
                TextSegment(text="Η βαθμολογική αξία της εξέτασης είναι 10 μονάδες. Η χρονική διάρκεια είναι 3 ώρες. "),
                TextSegment(text="Επιτρέπεται στυλό μόνο μπλε και μαύρου χρώματος. Επιτρέπεται μολύβι μόνο για γραφή στο πρόχειρο. Καλή Επιτυχία!"),
            ]
        ),
        Paragraph(
            accent_border_color="var(--blue-action)",
            segments=[
                TextSegment(text="Θέμα 1. (3 μονάδες) ", is_highlight=True, category="logic", tag_label="Q1-EQUIVALENCE", badge_class="badge-logic", tooltip="Classification: Equivalence Relations & Closures\nDetection Clue: 'A = {a, b, c, d}, R = {(a,a), (b,b), (c,c), (d,d), (a,b), (b,a), (?)}... σχέση ισοδυναμίας... ελάχιστο πλήθος στοιχείων'\nApplication Rationale: Checks reflexivity, symmetry, transitivity and calculates minimum closure addition"),
                TextSegment(text="Έστω R μία σχέση στο σύνολο A = {a, b, c, d}. Η σχέση δίνεται ως εξής: R = {(a, a), (b, b), (c, c), (d, d), (a, b), (b, a), (?)}.\n\n"),
                TextSegment(text="Ομάδα Α: (?) = (b, c) | Ομάδα Β: (?) = (a, c) | Ομάδα Γ: (?) = (c, d), (d, c) | Ομάδα Δ: (?) = (a, d), (d, a)\n\n"),
                TextSegment(text="Εξετάστε αν η σχέση R είναι σχέση ισοδυναμίας. Αν δεν είναι, προσθέστε το ελάχιστο πλήθος στοιχείων ώστε να γίνει σχέση ισοδυναμίας."),
            ]
        ),
        Paragraph(
            accent_border_color="var(--accent)",
            segments=[
                TextSegment(text="Θέμα 2. (4 μονάδες) ", is_highlight=True, category="automata", tag_label="Q2-DFA", badge_class="badge-automata", tooltip="Classification: Deterministic Finite Automata (DFA)\nDetection Clue: 'Σχεδιάστε ένα Ντετερμινιστικό Πεπερασμένο Αυτόματο (DFA) επί του Σ = {0, 1}'\nApplication Rationale: Synthesizes state diagram and transition table for specified language conditions"),
                TextSegment(text="Σχεδιάστε ένα Ντετερμινιστικό Πεπερασμένο Αυτόματο (DFA) που να αναγνωρίζει τη γλώσσα επί του αλφαβήτου Σ = {0, 1} η οποία περιέχει όλες τις συμβολοσειρές που:\n\n"),
                TextSegment(text="Ομάδα Α: Λήγουν σε 10\n"),
                TextSegment(text="Ομάδα Β: Ξεκινούν με 01\n"),
                TextSegment(text="Ομάδα Γ: Περιέχουν την υποσυμβολοσειρά 11\n"),
                TextSegment(text="Ομάδα Δ: Έχουν άρτιο αριθμό από 0 και περιττό από 1"),
            ]
        ),
        Paragraph(
            accent_border_color="var(--green-ok)",
            segments=[
                TextSegment(text="Θέμα 3. (3 μονάδες) ", is_highlight=True, category="prob", tag_label="Q3-PROB-LOTTERY", badge_class="badge-prob", tooltip="Classification: Combinatorial Probability without Replacement\nDetection Clue: '10 μπάλες αριθμημένες 1 έως 10... τραβάμε 3 χωρίς επανατοποθέτηση... άθροισμα'\nApplication Rationale: Uses C(10, 3) = 120 and counts favorable triplets according to parity or sum thresholds"),
                TextSegment(text="Σε μία κληρωτίδα υπάρχουν 10 μπάλες αριθμημένες από το 1 έως το 10. Τραβάμε 3 μπάλες χωρίς επανατοποθέτηση. "),
                TextSegment(text="Ποια η πιθανότητα το άθροισμα των αριθμών στις μπάλες να είναι:\n\n"),
                TextSegment(text="Ομάδα Α: άρτιο | Ομάδα Β: περιττό | Ομάδα Γ: μεγαλύτερο του 24 | Ομάδα Δ: μικρότερο του 10"),
            ]
        ),
    ]

    questions = [
        # QUESTION 1
        ExamQuestion(
            question_number=1,
            title="Σχέσεις Ισοδυναμίας & Ελάχιστη Προσθήκη Στοιχείων",
            question_type="Σχέσεις & Συναρτήσεις",
            prompt_text=(
                "Έστω $R$ μία σχέση στο σύνολο $A = \\{a, b, c, d\\}$:\n"
                "$$R = \\{(a, a), (b, b), (c, c), (d, d), (a, b), (b, a), (?)\\}$$\n\n"
                "- **Ομάδα Α:** $(?) = (b, c)$\n"
                "- **Ομάδα Β:** $(?) = (a, c)$\n"
                "- **Ομάδα Γ:** $(?) = (c, d), (d, c)$\n"
                "- **Ομάδα Δ:** $(?) = (a, d), (d, a)$\n\n"
                "Εξετάστε αν η σχέση $R$ είναι σχέση ισοδυναμίας. Αν δεν είναι, προσθέστε το ελάχιστο πλήθος στοιχείων ώστε να γίνει σχέση ισοδυναμίας."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ανάλυση Ομάδας Α: (?) = (b, c)",
                    formula=r"\text{Έλεγχος Ανακλαστικότητας, Συμμετρίας, Μεταβατικότητας}",
                    substitution=(
                        r"\text{Ανακλαστικότητα: Υπάρχουν όλα τα } (x, x) \implies \checkmark. \\ "
                        r"\text{Συμμετρία: Υπάρχει } (b, c) \text{ αλλά λείπει το } (c, b). \\ "
                        r"\text{Μεταβατικότητα: Υπάρχουν } (a, b) \text{ και } (b, c) \implies \text{απαιτείται } (a, c). \\ "
                        r"\text{Επίσης με } (c, b) \text{ και } (b, a) \implies \text{απαιτείται } (c, a)."
                    ),
                    result=r"\text{ΔΕΝ είναι ισοδυναμίας. Ελάχιστη προσθήκη: } \{(c, b), (a, c), (c, a)\} \text{ (3 ζεύγη)}",
                    rationale="Με την προσθήκη των 3 ζευγών, η κλάση ισοδυναμίας γίνεται [a] = {a, b, c} και [d] = {d}.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ανάλυση Ομάδας Β: (?) = (a, c)",
                    formula=r"\text{Απαιτούμενα ζεύγη για συμμετρία και μεταβατικότητα}",
                    substitution=r"(a, c) \implies (c, a) \text{ (συμμετρία)}, \ (b, a) \land (a, c) \implies (b, c), \ (c, a) \land (a, b) \implies (c, b)",
                    result=r"\text{ΔΕΝ είναι ισοδυναμίας. Ελάχιστη προσθήκη: } \{(c, a), (b, c), (c, b)\} \text{ (3 ζεύγη)}",
                    rationale="Και εδώ δημιουργείται η κλάση {a, b, c}.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Ανάλυση Ομάδας Γ: (?) = (c, d), (d, c)",
                    formula=r"\text{Έλεγχος μεταβατικότητας μεταξύ } \{a, b\} \text{ και } \{c, d\}",
                    substitution=(
                        r"\text{Υπάρχουν: } (a, a), (b, b), (c, c), (d, d), (a, b), (b, a), (c, d), (d, c). \\ "
                        r"\text{Δεν υπάρχει κανένα ζεύγος που να συνδέει το } \{a, b\} \text{ με το } \{c, d\}."
                    ),
                    result=r"\mathbf{ΕΙΝΑΙ} \text{ σχέση ισοδυναμίας! Προσθήκη: } \emptyset \text{ (0 ζεύγη)}",
                    rationale="Διαμερίζει το A σε δύο κλάσεις ισοδυναμίας: [a] = {a, b} και [c] = {c, d}.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Ανάλυση Ομάδας Δ: (?) = (a, d), (d, a)",
                    formula=r"\text{Έλεγχος μεταβατικότητας}",
                    substitution=r"(b, a) \in R \land (a, d) \in R \implies \text{απαιτείται } (b, d). \text{ Λόγω συμμετρίας απαιτείται και το } (d, b).",
                    result=r"\text{ΔΕΝ είναι ισοδυναμίας. Ελάχιστη προσθήκη: } \{(b, d), (d, b)\} \text{ (2 ζεύγη)}",
                    rationale="Κλάσεις ισοδυναμίας: [a] = {a, b, d} και [c] = {c}.",
                ),
            ],
            final_answer="Ομάδα Α: ΔΕΝ είναι ισοδυναμίας. Προσθήκη: {(c,b), (a,c), (c,a)} (3 ζεύγη)\nΟμάδα Β: ΔΕΝ είναι ισοδυναμίας. Προσθήκη: {(c,a), (b,c), (c,b)} (3 ζεύγη)\nΟμάδα Γ: ΕΙΝΑΙ σχέση ισοδυναμίας (0 ζεύγη)\nΟμάδα Δ: ΔΕΝ είναι ισοδυναμίας. Προσθήκη: {(b,d), (d,b)} (2 ζεύγη)",
            detailed_justification="Μία σχέση ισοδυναμίας αντιστοιχεί πάντοτε σε διαμέριση του συνόλου. Στην Ομάδα Γ έχουμε ήδη πλήρεις κλίκες {a, b} και {c, d}. Στις Ομάδες Α, Β, Δ, η προσθήκη μιας ακμής μεταξύ στοιχείων επιβάλλει τη συνένωση των κλάσεων σε μία μεγαλύτερη κλίκα μέσω μεταβατικής και συμμετρικής κλειστότητας.",
            common_pitfalls=[
                "Ξέχασμα του αντίστροφου ζεύγους: Πολλοί προσθέτουν το (a, c) αλλά ξεχνούν το (c, a).",
            ],
            related_theory_topic="Σχέσεις Ισοδυναμίας & Διαμερίσεις",
        ),

        # QUESTION 2
        ExamQuestion(
            question_number=2,
            title="Σχεδιασμός Ντετερμινιστικού Πεπερασμένου Αυτομάτου (DFA)",
            question_type="Αυτόματα & Τυπικές Γλώσσες",
            prompt_text=(
                "Σχεδιάστε ένα Ντετερμινιστικό Πεπερασμένο Αυτόματο (DFA) επί του $\\Sigma = \\{0, 1\\}$:\n\n"
                "- **Ομάδα Α:** Λήγουν σε 10\n"
                "- **Ομάδα Β:** Ξεκινούν με 01\n"
                "- **Ομάδα Γ:** Περιέχουν την υποσυμβολοσειρά 11\n"
                "- **Ομάδα Δ:** Άρτιος αριθμός από 0 και περιττός από 1"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ομάδα Α — Συμβολοσειρές που λήγουν σε 10 (3 καταστάσεις)",
                    formula=r"Q = \{q_0, q_1, q_2\}, \ q_0 \text{ αρχική}, \ F = \{q_2\}",
                    substitution=(
                        r"\delta(q_0, 0) = q_0, \ \delta(q_0, 1) = q_1 \\ "
                        r"\delta(q_1, 0) = q_2, \ \delta(q_1, 1) = q_1 \\ "
                        r"\delta(q_2, 0) = q_0, \ \delta(q_2, 1) = q_1"
                    ),
                    result=r"\text{DFA 3 καταστάσεων, αποδεκτή: } q_2",
                    rationale="Η q1 θυμάται ότι το προηγούμενο σύμβολο ήταν 1, και η q2 ότι τα δύο τελευταία ήταν 10.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ομάδα Β — Ξεκινούν με 01 (4 καταστάσεις με Dead State)",
                    formula=r"Q = \{q_0, q_1, q_2, q_{dead}\}, \ F = \{q_2\}",
                    substitution=(
                        r"\delta(q_0, 0) = q_1, \ \delta(q_0, 1) = q_{dead} \\ "
                        r"\delta(q_1, 0) = q_{dead}, \ \delta(q_1, 1) = q_2 \\ "
                        r"\delta(q_2, 0) = q_2, \ \delta(q_2, 1) = q_2 \\ "
                        r"\delta(q_{dead}, 0) = q_{dead}, \ \delta(q_{dead}, 1) = q_{dead}"
                    ),
                    result=r"\text{DFA 4 καταστάσεων}",
                    rationale="Οποιαδήποτε απόκλιση από το πρόθεμα 01 οδηγεί στην παγίδα q_dead.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Ομάδα Γ — Περιέχουν 11 (3 καταστάσεις)",
                    formula=r"Q = \{q_0, q_1, q_2\}, \ F = \{q_2\}",
                    substitution=(
                        r"\delta(q_0, 0) = q_0, \ \delta(q_0, 1) = q_1 \\ "
                        r"\delta(q_1, 0) = q_0, \ \delta(q_1, 1) = q_2 \\ "
                        r"\delta(q_2, 0) = q_2, \ \delta(q_2, 1) = q_2"
                    ),
                    result=r"\text{DFA 3 καταστάσεων}",
                    rationale="Μόλις διαβαστεί 11, το αυτόματο εισέρχεται στην αποδεκτή κατάσταση q2 και παραμένει εκεί.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Ομάδα Δ — Άρτια 0 ΚΑΙ Περιττά 1 (4 καταστάσεις modulo 2)",
                    formula=r"Q = \{(0,0), (0,1), (1,0), (1,1)\}, \ q_0 = (0,0), \ F = \{(0,1)\}",
                    substitution=(
                        r"\delta((i,j), 0) = (i \oplus 1, j), \quad \delta((i,j), 1) = (i, j \oplus 1) \\ "
                        r"\text{Αποδεκτή κατάσταση είναι η } (0, 1) \text{ (0 mod 2 = 0, 1 mod 2 = 1)}"
                    ),
                    result=r"\text{DFA 4 καταστάσεων}",
                    rationale="Κλασικό γινόμενο αυτομάτων για ταυτόχρονη παρακολούθηση της ισοτιμίας των 0 και των 1.",
                ),
            ],
            final_answer="Ομάδα Α: DFA 3 καταστάσεων (q0, q1, q2=αποδεκτή)\nΟμάδα Β: DFA 4 καταστάσεων (με κατάσταση απόρριψης q_dead)\nΟμάδα Γ: DFA 3 καταστάσεων (παγίδα αποδοχής q2)\nΟμάδα Δ: DFA 4 καταστάσεων (ισοτιμίες mod 2, αποδεκτή η (0,1))",
            detailed_justification="Κάθε DFA κατασκευάζεται με ελάχιστες καταστάσεις που αντιστοιχούν στις κλάσεις ισοδυναμίας Myhill-Nerode της εκάστοτε γλώσσας.",
            common_pitfalls=[
                "Στην Ομάδα Β, παράλειψη της dead state (ένα DFA πρέπει να είναι πλήρως ορισμένο για κάθε σύμβολο του αλφαβήτου).",
            ],
            related_theory_topic="Αυτόματα & DFA",
        ),

        # QUESTION 3
        ExamQuestion(
            question_number=3,
            title="Πιθανότητες Κληρωτίδας: 3 Μπάλες από τις 10",
            question_type="Πιθανότητες & Συνδυαστική",
            prompt_text=(
                "Σε μία κληρωτίδα υπάρχουν 10 μπάλες αριθμημένες από το 1 έως το 10. Τραβάμε 3 μπάλες χωρίς επανατοποθέτηση.\n"
                "Συνολικές εκβάσεις: $|\\Omega| = \\binom{10}{3} = 120$.\n\n"
                "Ποια η πιθανότητα το άθροισμα να είναι:\n"
                "- **Ομάδα Α:** άρτιο\n"
                "- **Ομάδα Β:** περιττό\n"
                "- **Ομάδα Γ:** μεγαλύτερο του 24\n"
                "- **Ομάδα Δ:** μικρότερο του 10"
            ),
            given_parameters=[
                GivenParameter(symbol="|\\Omega|", value="120", description="Σύνολο τριάδων C(10, 3)"),
                GivenParameter(symbol="Άρτιες μπάλες", value="5", description="{2, 4, 6, 8, 10}"),
                GivenParameter(symbol="Περιττές μπάλες", value="5", description="{1, 3, 5, 7, 9}"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ομάδα Α — Άθροισμα Άρτιο",
                    formula=r"|E_A| = \binom{5}{3} + \binom{5}{2}\binom{5}{1}",
                    substitution=r"|E_A| = 10 + 10 \times 5 = 10 + 50 = 60 \implies P = \frac{60}{120} = \frac{1}{2}",
                    result=r"P = 1/2 = 50\%",
                    rationale="Άθροισμα 3 αριθμών είναι άρτιο αν είναι: (3 άρτιοι) ή (2 περιττοί + 1 άρτιος).",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ομάδα Β — Άθροισμα Περιττό",
                    formula=r"P = 1 - P(\text{άρτιο})",
                    substitution=r"P = 1 - \frac{1}{2} = \frac{1}{2}",
                    result=r"P = 1/2 = 50\%",
                    rationale="Το συμπληρωματικό ενδεχόμενο του άρτιου αθροίσματος.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Ομάδα Γ — Άθροισμα > 24 (δηλαδή >= 25)",
                    formula=r"\text{Απαρίθμηση τριάδων με άθροισμα } \ge 25",
                    substitution=(
                        r"\Sigma = 27: \{8, 9, 10\} \ [1] \\ "
                        r"\Sigma = 26: \{7, 9, 10\} \ [1] \\ "
                        r"\Sigma = 25: \{6, 9, 10\}, \{7, 8, 10\} \ [2] \\ "
                        r"\text{Σύνολο ευνοϊκών: } 1 + 1 + 2 = 4 \implies P = \frac{4}{120} = \frac{1}{30}"
                    ),
                    result=r"P = 1/30 \approx 3.33\%",
                    rationale="Υπάρχουν ακριβώς 4 τριάδες με άθροισμα τουλάχιστον 25.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Ομάδα Δ — Άθροισμα < 10 (δηλαδή <= 9)",
                    formula=r"\text{Απαρίθμηση τριάδων με άθροισμα } \le 9",
                    substitution=(
                        r"\Sigma = 6: \{1, 2, 3\} \ [1] \\ "
                        r"\Sigma = 7: \{1, 2, 4\} \ [1] \\ "
                        r"\Sigma = 8: \{1, 2, 5\}, \{1, 3, 4\} \ [2] \\ "
                        r"\Sigma = 9: \{1, 2, 6\}, \{1, 3, 5\}, \{2, 3, 4\} \ [3] \\ "
                        r"\text{Σύνολο ευνοϊκών: } 1 + 1 + 2 + 3 = 7 \implies P = \frac{7}{120}"
                    ),
                    result=r"P = 7/120 \approx 5.83\%",
                    rationale="Υπάρχουν ακριβώς 7 τριάδες με άθροισμα το πολύ 9.",
                ),
            ],
            final_answer="Ομάδα Α: P = 1/2 (50%)\nΟμάδα Β: P = 1/2 (50%)\nΟμάδα Γ: P = 1/30 (3.33%)\nΟμάδα Δ: P = 7/120 (5.83%)",
            detailed_justification="Συνολικός δειγματικός χώρος C(10, 3) = 120. Για τις Ομάδες Α και Β η συμμετρία των 5 άρτιων και 5 περιττών δίνει ακριβώς 60 άρτια και 60 περιττά αθροίσματα. Για τις Ομάδες Γ και Δ η άμεση απαρίθμηση των οριακών τριάδων δίνει 4 και 7 ευνοϊκές εκβάσεις αντίστοιχα.",
            common_pitfalls=[
                "Στην Ομάδα Γ: 'μεγαλύτερο του 24' σημαίνει >= 25 (δεν περιλαμβάνει το 24).",
                "Στην Ομάδα Δ: 'μικρότερο του 10' σημαίνει <= 9.",
            ],
            related_theory_topic="Πιθανότητες & Συνδυαστική",
        ),
    ]

    diagram_nodes = [
        DiagramNode(id="q0", label="q0", node_type="state", x=120, y=160, properties={"is_start": True}),
        DiagramNode(id="q1", label="q1", node_type="state", x=280, y=160),
        DiagramNode(id="q2", label="q2 (End)", node_type="state", x=440, y=160, properties={"is_accept": True}),
    ]

    diagram_edges = [
        DiagramEdge(source_id="q0", target_id="q0", label="0", path_d="M 110 138 C 90 90, 150 90, 130 138"),
        DiagramEdge(source_id="q0", target_id="q1", label="1"),
        DiagramEdge(source_id="q1", target_id="q1", label="1", path_d="M 270 138 C 250 90, 310 90, 290 138"),
        DiagramEdge(source_id="q1", target_id="q2", label="0", color="var(--green-ok)"),
        DiagramEdge(source_id="q2", target_id="q0", label="0", path_d="M 440 184 C 360 250, 200 250, 120 184"),
        DiagramEdge(source_id="q2", target_id="q1", label="1", path_d="M 420 170 L 300 170"),
    ]

    justifications = [
        DesignJustification(
            title="Κλάσεις Μερικής Διάταξης & Ισοδυναμίας",
            category="Relations",
            description="Η μεταβατικότητα απαιτεί πλήρη σύνδεση όλων των στοιχείων της ίδιας κλάσης.",
            rationale="Εξηγεί γιατί η εισαγωγή ενός ζεύγους επιβάλλει αναδρομικά όλα τα απαραίτητα ζεύγη για τη διατήρηση της ισοδυναμίας.",
        ),
    ]

    solution_code = '''# Verification Script for Mock Exam 2 (Course 203)
import itertools

# Q3: Lottery probabilities from 10 balls
balls = list(range(1, 11))
all_triplets = list(itertools.combinations(balls, 3))
total = len(all_triplets)
assert total == 120

even_sums = [t for t in all_triplets if sum(t) % 2 == 0]
odd_sums = [t for t in all_triplets if sum(t) % 2 != 0]
gt_24 = [t for t in all_triplets if sum(t) > 24]
lt_10 = [t for t in all_triplets if sum(t) < 10]

print("Mock Exam 2 - Question 3:")
print(f"Total triplets: {total}")
print(f"Group A (Even): {len(even_sums)} / {total} = {len(even_sums)/total}")
print(f"Group B (Odd):  {len(odd_sums)} / {total} = {len(odd_sums)/total}")
print(f"Group C (> 24): {len(gt_24)} / {total} = {len(gt_24)/total} (Triplets: {gt_24})")
print(f"Group D (< 10): {len(lt_10)} / {total} = {len(lt_10)/total} (Triplets: {lt_10})")
'''

    return Scenario(
        id="mock_exam_2_standard",
        title="Εικονική Εξέταση 2 (Κανονική)",
        subtitle="203: Διακριτά Μαθηματικά — Σχέσεις Ισοδυναμίας, DFA & Πιθανότητες",
        course_tag="Εικονική Εξέταση",
        duration_info="3 Ώρες (10 Μονάδες)",
        paragraphs=paragraphs,
        questions=questions,
        diagram_nodes=diagram_nodes,
        diagram_edges=diagram_edges,
        justifications=justifications,
        solution_code=solution_code,
    )
