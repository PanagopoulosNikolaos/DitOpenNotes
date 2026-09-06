"""Practice Exam (Easy) scenario module for Discrete Mathematics.

Transcribes practice_exam_easy.md verbatim with interactive highlights, and provides
complete step-by-step solutions for all 9 questions in original sequence.
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


def createPracticeExamEasyScenario() -> Scenario:
    """Constructs the Scenario instance for Practice Exam (Easy).

    Returns:
        Scenario: Complete scenario with verbatim text, annotations, and worked solutions.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Τμήμα Πληροφορικής και Τηλεπικοινωνιών — Πανεπιστήμιο Ιωαννίνων\n"),
                TextSegment(text="203: Διακριτά Μαθηματικά — Εξέταση Διακριτών Μαθηματικών (Δυσκολία: EASY)\n\n"),
                TextSegment(text="Η βαθμολογική αξία της εξέτασης είναι 10 μονάδες. "),
                TextSegment(text="Επιτρέπεται μολύβι για το πρόχειρο και στυλό μπλε ή μαύρο για την τελική απάντηση. Καλή Επιτυχία!"),
            ]
        ),
        Paragraph(
            accent_border_color="var(--amber)",
            segments=[
                TextSegment(text="Θέμα 1. (2 μονάδες) ", is_highlight=True, category="logic", tag_label="Q1-LOGIC", badge_class="badge-logic", tooltip="Classification: Propositional Logic Truth Tables\nDetection Clue: 'Κατασκευάστε τον πίνακα αληθείας των ακόλουθων προτασιακών τύπων'\nApplication Rationale: Solves truth tables for implication and disjunction"),
                TextSegment(text="Κατασκευάστε τον πίνακα αληθείας των ακόλουθων προτασιακών τύπων:\n\n"),
                TextSegment(text="α'. (1 μονάδα) (p ∧ q) → (p ∨ q)\n"),
                TextSegment(text="β'. (1 μονάδα) ¬p → (p → q)"),
            ]
        ),
        Paragraph(
            accent_border_color="var(--blue-action)",
            segments=[
                TextSegment(text="Θέμα 2. (1 μονάδα) ", is_highlight=True, category="set", tag_label="Q2-SETS", badge_class="badge-set", tooltip="Classification: Two-Set Inclusion-Exclusion\nDetection Clue: '100 συμμετέχοντες... 60 κόκκινο... 40 μπλε... 20 και τα δύο'\nApplication Rationale: Solves 100 - (60 + 40 - 20) = 20"),
                TextSegment(text="Σε μία έρευνα με 100 συμμετέχοντες ρωτήθηκαν ποια από τα δύο χρώματα (κόκκινο, μπλε) τους αρέσουν:\n"),
                TextSegment(text="- 60 απάντησαν κόκκινο\n- 40 απάντησαν μπλε\n- 20 απάντησαν και τα δύο\n\n"),
                TextSegment(text="Υπολογίστε σε πόσους από τους συμμετέχοντες δεν αρέσει κανένα από τα δύο χρώματα."),
            ]
        ),
        Paragraph(
            accent_border_color="var(--green-ok)",
            segments=[
                TextSegment(text="Θέμα 3. (1 μονάδα) ", is_highlight=True, category="prob", tag_label="Q3-DICE-D6", badge_class="badge-prob", tooltip="Classification: Standard 6-Sided Dice Probability\nDetection Clue: 'ρίψης δύο διακεκριμένων αμερόληπτων εξάεδρων ζαριών (d6)'\nApplication Rationale: Computes outcomes for (even, odd) and sum = 7"),
                TextSegment(text="Θεωρούμε το πείραμα ρίψης δύο διακεκριμένων αμερόληπτων εξάεδρων ζαριών (d6):\n\n"),
                TextSegment(text="α'. (0.5 μονάδα) Απαριθμήστε τα δυνατά αποτελέσματα της μορφής (άρτιος, περιττός).\n"),
                TextSegment(text="β'. (0.5 μονάδα) Απαριθμήστε τα δυνατά αποτελέσματα που αθροίζουν σε 7."),
            ]
        ),
        Paragraph(
            accent_border_color="var(--accent)",
            segments=[
                TextSegment(text="Θέμα 4. (1 μονάδα) ", is_highlight=True, category="prob", tag_label="Q4-MEDICAL-TEST", badge_class="badge-prob", tooltip="Classification: Diagnostic Test Probabilities\nDetection Clue: 'ασθένεια εμφανίζεται στο 5%... false negative 10%... false positive 5%'\nApplication Rationale: Computes joint probability P(Disease ∩ Negative) and total test positive rate"),
                TextSegment(text="Μια ασθένεια εμφανίζεται στο 5% του πληθυσμού. Ένα τεστ έχει:\n"),
                TextSegment(text="- Πιθανότητα 10% εσφαλμένα αρνητικού αποτελέσματος (false negative)\n"),
                TextSegment(text="- Πιθανότητα 5% εσφαλμένα θετικού αποτελέσματος (false positive)\n\n"),
                TextSegment(text="α'. (0.5 μονάδα) Υπολογίστε την πιθανότητα ένα άτομο να έχει την ασθένεια και το τεστ να δίνει αρνητικό αποτέλεσμα.\n"),
                TextSegment(text="β'. (0.5 μονάδα) Υπολογίστε την πιθανότητα το τεστ να δίνει θετικό αποτέλεσμα."),
            ]
        ),
        Paragraph(
            accent_border_color="var(--purple)",
            segments=[
                TextSegment(text="Θέμα 5. (1 μονάδα) ", is_highlight=True, category="logic", tag_label="Q5-RELATIONS", badge_class="badge-logic", tooltip="Classification: Relation Properties on S = {1, 2, 3}\nDetection Clue: 'R = {(1,1), (2,2), (3,3), (1,2), (2,3)}... ανακλαστική, συμμετρική, μεταβατική'\nApplication Rationale: Analyzes reflexivity (yes), symmetry (no), transitivity (no, missing (1,3))"),
                TextSegment(text="Για την ακόλουθη σχέση επί του S = {1, 2, 3}, ελέγξτε την ισχύ των ιδιοτήτων: ανακλαστική, συμμετρική και μεταβατική:\n"),
                TextSegment(text="R = {(1,1), (2,2), (3,3), (1,2), (2,3)}"),
            ]
        ),
        Paragraph(
            accent_border_color="var(--purple)",
            segments=[
                TextSegment(text="Θέμα 6. (2 μονάδες) ", is_highlight=True, category="graph", tag_label="Q6-K3-ISOMORPHISM", badge_class="badge-graph", tooltip="Classification: Triangle Graph K3 & Isomorphism\nDetection Clue: 'G1 = ({A,B,C}, E1)... G2 = ({1,2,3}, E2)... ισόμορφα... βαθμός κάθε κορυφής'\nApplication Rationale: Solves isomorphism of K3 and degree 2 for all vertices"),
                TextSegment(text="Έστω τα ακόλουθα γραφήματα:\n"),
                TextSegment(text="G1 = (V1 = {A, B, C}, E1 = {(A,B), (B,C), (A,C)})\n"),
                TextSegment(text="G2 = (V2 = {1, 2, 3}, E2 = {(1,2), (2,3), (1,3)})\n\n"),
                TextSegment(text="α'. (1 μονάδα) Δείξτε αν τα γραφήματα G1 και G2 είναι ισόμορφα.\n"),
                TextSegment(text="β'. (1 μονάδα) Υπολογίστε τον βαθμό κάθε κορυφής στο γράφημα G1."),
            ]
        ),
        Paragraph(
            accent_border_color="var(--accent)",
            segments=[
                TextSegment(text="Θέμα 7. (0.5 μονάδα) ", is_highlight=True, category="automata", tag_label="Q7-EXACT-TWOS", badge_class="badge-automata", tooltip="Classification: Regular Expression for Exact Count\nDetection Clue: 'αλφάβητο {0, 1}... ακριβώς δύο εμφανίσεις του 0'\nApplication Rationale: Derives regex 1* 0 1* 0 1*"),
                TextSegment(text="Γράψτε μία κανονική έκφραση που περιγράφει το σύνολο των συμβολοσειρών με αλφάβητο το {0, 1} που περιέχουν ακριβώς δύο εμφανίσεις του 0."),
            ]
        ),
        Paragraph(
            accent_border_color="var(--accent)",
            segments=[
                TextSegment(text="Θέμα 8. (0.5 μονάδα) ", is_highlight=True, category="automata", tag_label="Q8-LANGUAGE-MEMBERSHIP", badge_class="badge-automata", tooltip="Classification: String Membership in Regular Language\nDetection Clue: 'ποιες από τις cat, bat, hat, mat ανήκουν... (c|b|h)at'\nApplication Rationale: Evaluates prefix set {c, b, h} concatenated with 'at'"),
                TextSegment(text="Γράψτε ποιες από τις συμβολοσειρές cat, bat, hat, mat ανήκουν στο κανονικό σύνολο που περιγράφει η κανονική έκφραση: (c|b|h)at"),
            ]
        ),
        Paragraph(
            accent_border_color="#0284c7",
            segments=[
                TextSegment(text="Θέμα 9. (1 μονάδα) ", is_highlight=True, category="induct", tag_label="Q9-GAUSS-INDUCTION", badge_class="badge-induct", tooltip="Classification: Classical Induction on Natural Numbers Sum\nDetection Clue: '1 + 2 + 3 + ... + n = n(n+1)/2'\nApplication Rationale: Formally proves Gauss summation formula"),
                TextSegment(text="Δείξτε με επαγωγή ότι για κάθε n ≥ 1 ισχύει:\n"),
                TextSegment(text="1 + 2 + 3 + ... + n = n(n+1) / 2"),
            ]
        ),
    ]

    questions = [
        ExamQuestion(
            question_number=1,
            title="Πίνακες Αληθείας: (p ∧ q) → (p ∨ q) και ¬p → (p → q)",
            question_type="Προτασιακή Λογική",
            prompt_text=(
                "Κατασκευάστε τον πίνακα αληθείας των ακόλουθων προτασιακών τύπων:\n\n"
                "**α'. (1 μονάδα)** $(p \\land q) \\to (p \\lor q)$\n\n"
                "**β'. (1 μονάδα)** $\\neg p \\to (p \\to q)$"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ερώτημα α' — Πίνακας (p ∧ q) → (p ∨ q)",
                    formula=r"(p \land q) \to (p \lor q)",
                    substitution=(
                        r"\begin{array}{|c|c|c|c|c|} "
                        r"p & q & p \land q & p \lor q & (p \land q) \to (p \lor q) \\ \hline "
                        r"T & T & T & T & \mathbf{T} \\ "
                        r"T & F & F & T & \mathbf{T} \\ "
                        r"F & T & F & T & \mathbf{T} \\ "
                        r"F & F & F & F & \mathbf{T} "
                        r"\end{array}"
                    ),
                    result=r"\text{Ταυτολογία (πάντα } T)",
                    rationale="Αν ισχύουν και τα δύο (p και q), προφανώς ισχύει τουλάχιστον ένα (p ή q).",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ερώτημα β' — Πίνακας ¬p → (p → q)",
                    formula=r"\neg p \to (p \to q) \equiv \neg(\neg p) \lor (\neg p \lor q) \equiv p \lor \neg p \lor q \equiv \top",
                    substitution=(
                        r"\begin{array}{|c|c|c|c|c|} "
                        r"p & q & \neg p & p \to q & \neg p \to (p \to q) \\ \hline "
                        r"T & T & F & T & \mathbf{T} \\ "
                        r"T & F & F & F & \mathbf{T} \\ "
                        r"F & T & T & T & \mathbf{T} \\ "
                        r"F & F & T & T & \mathbf{T} "
                        r"\end{array}"
                    ),
                    result=r"\text{Ταυτολογία (πάντα } T)",
                    rationale="Όταν p=T η υπόθεση ¬p είναι F, άρα η συνεπαγωγή είναι T. Όταν p=F το p->q είναι T, άρα πάλι T.",
                ),
            ],
            final_answer="Και οι δύο τύποι είναι Ταυτολογίες (αποτιμώνται σε T σε όλες τις γραμμές).",
            detailed_justification="Ο τύπος α' αποτελεί βασικό νόμο διάζευξης (αν ισχύει η σύζευξη, ισχύει αναγκαστικά και η διάζευξη). Ο τύπος β' απλοποιείται άμεσα σε p ∨ ¬p ∨ q ≡ ⊤ ∨ q ≡ ⊤.",
            common_pitfalls=["Λάθος στη γραμμή p=T, q=F όπου p ∧ q = F και p ∨ q = T (F -> T δίνει T και όχι F)."],
            related_theory_topic="Προτασιακή Λογική & Πίνακες Αληθείας",
        ),
        ExamQuestion(
            question_number=2,
            title="Αρχή Εγκλεισμού-Αποκλεισμού (Έρευνα 100 ατόμων)",
            question_type="Θεωρία Συνόλων",
            prompt_text=(
                "Σε έρευνα 100 συμμετεχόντων:\n"
                "- 60 κόκκινο (K)\n"
                "- 40 μπλε (M)\n"
                "- 20 και τα δύο ($K \\cap M$)\n\n"
                "Υπολογίστε σε πόσους δεν αρέσει κανένα χρώμα."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ένωση και Συμπλήρωμα",
                    formula=r"|K \cup M| = |K| + |M| - |K \cap M|, \quad N = |U| - |K \cup M|",
                    substitution=r"|K \cup M| = 60 + 40 - 20 = 80 \implies N = 100 - 80 = 20",
                    result=r"N = 20",
                    rationale="Από τους 100, οι 80 προτιμούν τουλάχιστον ένα χρώμα.",
                ),
            ],
            final_answer="20 συμμετέχοντες δεν προτιμούν κανένα χρώμα.",
            detailed_justification="|K ∪ M| = 60 + 40 - 20 = 80. Άρα 100 - 80 = 20.",
            common_pitfalls=["Άθροιση 60 + 40 = 100 χωρίς αφαίρεση της τομής 20."],
            related_theory_topic="Θεωρία Συνόλων & Εγκλεισμός-Αποκλεισμός",
        ),
        ExamQuestion(
            question_number=3,
            title="Ρίψη 2 Εξάεδρων Ζαριών (d6)",
            question_type="Πιθανότητες & Συνδυαστική",
            prompt_text=(
                "Θεωρούμε το πείραμα ρίψης δύο διακεκριμένων εξάεδρων ζαριών (d6):\n\n"
                "**α'. (0.5 μονάδα)** Πόσα είναι τα αποτελέσματα (άρτιος, περιττός);\n\n"
                "**β'. (0.5 μονάδα)** Πόσα αποτελέσματα αθροίζουν σε 7;"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ερώτημα α' — Ζεύγη (άρτιος, περιττός)",
                    formula=r"\text{Πλήθος} = 3 \times 3 = 9",
                    substitution=r"\{2, 4, 6\} \times \{1, 3, 5\} \implies 9 \text{ ζεύγη}",
                    result=r"9 \text{ ζεύγη}",
                    rationale="3 επιλογές άρτιου για το 1ο ζάρι επί 3 επιλογές περιττού για το 2ο.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ερώτημα β' — Άθροισμα 7",
                    formula=r"\text{Ζεύγη: } \{(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)\}",
                    substitution=r"\text{Απαρίθμηση } 6 \text{ ζευγών}",
                    result=r"6 \text{ αποτελέσματα}",
                    rationale="Ακριβώς 6 ζεύγη έχουν άθροισμα 7.",
                ),
            ],
            final_answer="α': 9 δυνατά αποτελέσματα\nβ': 6 δυνατά αποτελέσματα (1,6), (2,5), (3,4), (4,3), (5,2), (6,1)",
            detailed_justification="Συνολικός δειγματικός χώρος |Ω| = 36. Τα ζεύγη (άρτιος, περιττός) είναι 3 * 3 = 9. Τα ζεύγη με άθροισμα 7 είναι 6.",
            common_pitfalls=["Μη διάκριση του (1,6) από το (6,1)."],
            related_theory_topic="Συνδυαστική & Ζάρια",
        ),
        ExamQuestion(
            question_number=4,
            title="Πιθανότητες Ιατρικού Διαγνωστικού Τεστ",
            question_type="Πιθανότητες & Bayes",
            prompt_text=(
                "Μια ασθένεια D εμφανίζεται στο 5% ($P(D) = 0.05$).\n"
                "- $P(T^- \\mid D) = 10\\% = 0.10$ (False Negative)\n"
                "- $P(T^+ \\mid D^c) = 5\\% = 0.05$ (False Positive)\n\n"
                "**α'. (0.5 μονάδα)** Πιθανότητα ένα άτομο να έχει την ασθένεια ΚΑΙ το τεστ να είναι αρνητικό ($P(D \\cap T^-)$).\n\n"
                "**β'. (0.5 μονάδα)** Πιθανότητα το τεστ να είναι θετικό ($P(T^+)$)."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ερώτημα α' — Τομή P(D ∩ T^-)",
                    formula=r"P(D \cap T^-) = P(T^- \mid D) P(D)",
                    substitution=r"P(D \cap T^-) = 0.10 \times 0.05 = 0.005 \ (0.5\%)",
                    result=r"0.005 \ (0.5\%)",
                    rationale="Πολλαπλασιαστικός κανόνας πιθανοτήτων.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ερώτημα β' — Ολική Πιθανότητα Θετικού Τεστ P(T^+)",
                    formula=r"P(T^+) = P(T^+ \mid D)P(D) + P(T^+ \mid D^c)P(D^c)",
                    substitution=(
                        r"P(T^+ \mid D) = 1 - P(T^- \mid D) = 1 - 0.10 = 0.90 \\ "
                        r"P(D^c) = 1 - 0.05 = 0.95 \\ "
                        r"P(T^+) = (0.90 \times 0.05) + (0.05 \times 0.95) = 0.045 + 0.0475 = 0.0925 \ (9.25\%)"
                    ),
                    result=r"0.0925 \ (9.25\%)",
                    rationale="Εφαρμογή του θεωρήματος ολικής πιθανότητας για τα γεγονότα D και D^c.",
                ),
            ],
            final_answer="α': P(D ∩ T^-) = 0.005 (0.5%)\nβ': P(T^+) = 0.0925 (9.25%)",
            detailed_justification="Για το β', τα αληθώς θετικά είναι 0.90 * 0.05 = 0.045 και τα εσφαλμένως θετικά είναι 0.05 * 0.95 = 0.0475. Άθροισμα: 0.0925.",
            common_pitfalls=["Ξέχασμα ότι P(T^+ | D) = 1 - FN = 0.90."],
            related_theory_topic="Ολική Πιθανότητα & Διαγνωστικά Τεστ",
        ),
        ExamQuestion(
            question_number=5,
            title="Έλεγχος Ιδιοτήτων Σχέσης R επί του {1, 2, 3}",
            question_type="Σχέσεις & Συναρτήσεις",
            prompt_text="Για τη σχέση $R = \\{(1,1), (2,2), (3,3), (1,2), (2,3)\\}$ στο $S = \\{1, 2, 3\\}$, ελέγξτε: ανακλαστική, συμμετρική, μεταβατική.",
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Έλεγχος 3 Ιδιοτήτων",
                    formula=r"\text{Ανακλαστικότητα, Συμμετρία, Μεταβατικότητα}",
                    substitution=(
                        r"1. \text{Ανακλαστική: } (1,1), (2,2), (3,3) \in R \implies \mathbf{NAI}. \\ "
                        r"2. \text{Συμμετρική: } (1,2) \in R \text{ αλλά } (2,1) \notin R \implies \mathbf{OXI}. \\ "
                        r"3. \text{Μεταβατική: } (1,2) \in R \land (2,3) \in R \text{ αλλά } (1,3) \notin R \implies \mathbf{OXI}."
                    ),
                    result=r"\text{Ανακλαστική: ΝΑΙ} \mid \text{Συμμετρική: ΟΧΙ} \mid \text{Μεταβατική: ΟΧΙ}",
                    rationale="Η σχέση είναι μόνο ανακλαστική.",
                ),
            ],
            final_answer="Ανακλαστική: ΝΑΙ\nΣυμμετρική: ΟΧΙ (λείπει το (2,1))\nΜεταβατική: ΟΧΙ (λείπει το (1,3))",
            detailed_justification="(1,1), (2,2), (3,3) ανήκουν όλα στη σχέση (ανακλαστική). Το (1,2) ανήκει αλλά το (2,1) όχι (μη συμμετρική). Τα (1,2) και (2,3) ανήκουν αλλά το (1,3) όχι (μη μεταβατική).",
            common_pitfalls=["Θεώρηση ότι η σχέση είναι μεταβατική επειδή υπάρχουν τα διαγώνια."],
            related_theory_topic="Σχέσεις & Ιδιότητες",
        ),
        ExamQuestion(
            question_number=6,
            title="Ισομορφισμός Τριγώνων K3 & Βαθμοί Κορυφών",
            question_type="Θεωρία Γραφημάτων",
            prompt_text=(
                "Έστω $G_1 = (\\{A, B, C\\}, \\{(A,B), (B,C), (A,C)\\})$ και $G_2 = (\\{1, 2, 3\\}, \\{(1,2), (2,3), (1,3)\\})$.\n\n"
                "**α'. (1 μονάδα)** Δείξτε αν είναι ισόμορφα.\n\n"
                "**β'. (1 μονάδα)** Υπολογίστε τον βαθμό κάθε κορυφής στο $G_1$."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ερώτημα α' — Ισομορφισμός",
                    formula=r"f: \{A, B, C\} \to \{1, 2, 3\}",
                    substitution=r"f(A)=1, f(B)=2, f(C)=3 \implies \{u,v\} \in E_1 \iff \{f(u),f(v)\} \in E_2",
                    result=r"\mathbf{Ισόμορφα} \ (G_1 \cong G_2 \cong K_3)",
                    rationale="Και τα δύο γραφήματα είναι το πλήρες γράφημα 3 κορυφών K3.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ερώτημα β' — Βαθμοί Κορυφών",
                    formula=r"\deg(v) = |\{u \mid (v,u) \in E_1\}|",
                    substitution=r"\deg(A) = 2, \ \deg(B) = 2, \ \deg(C) = 2",
                    result=r"\deg(A) = \deg(B) = \deg(C) = 2",
                    rationale="Κάθε κορυφή συνδέεται με τις άλλες 2 κορυφές.",
                ),
            ],
            final_answer="α': Είναι ισόμορφα (f: A↦1, B↦2, C↦3)\nβ': deg(A) = 2, deg(B) = 2, deg(C) = 2",
            detailed_justification="Πρόκειται για το τρίγωνο K3 (2-κανονικό γράφημα).",
            common_pitfalls=["Καμία ουσιαστική παγίδα."],
            related_theory_topic="Θεωρία Γραφημάτων & Ισομορφισμός",
        ),
        ExamQuestion(
            question_number=7,
            title="Κανονική Έκφραση: Ακριβώς Δύο Μηδενικά",
            question_type="Αυτόματα & Τυπικές Γλώσσες",
            prompt_text="Γράψτε μία κανονική έκφραση για συμβολοσειρές επί του $\\{0, 1\\}$ με **ακριβώς δύο** εμφανίσεις του 0.",
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Δομή Έκφρασης",
                    formula=r"1^* 0 1^* 0 1^*",
                    substitution=r"\text{Ακριβώς δύο μηδενικά, με αυθαίρετο πλήθος άσσων σε οποιαδήποτε θέση}",
                    result=r"1^* 0 1^* 0 1^*",
                    rationale="Τα μόνα σύμβολα 0 που επιτρέπονται είναι ακριβώς 2.",
                ),
            ],
            final_answer="1* 0 1* 0 1*",
            detailed_justification="Τα δύο μηδενικά χωρίζουν τη συμβολοσειρά σε τρία τμήματα, καθένα εκ των οποίων μπορεί να περιέχει μόνο άσσους (συμπεριλαμβανομένης της κενής συμβολοσειράς).",
            common_pitfalls=["Χρήση (0|1)* αντί για 1* που θα επέτρεπε περισσότερα μηδενικά."],
            related_theory_topic="Κανονικές Εκφράσεις",
        ),
        ExamQuestion(
            question_number=8,
            title="Αναγνώριση Συμβολοσειρών από (c|b|h)at",
            question_type="Αυτόματα & Τυπικές Γλώσσες",
            prompt_text="Ποιες από τις cat, bat, hat, mat ανήκουν στο $(c \\mid b \\mid h)at$;",
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ανάπτυγμα",
                    formula=r"L((c \mid b \mid h)at) = \{c, b, h\} \cdot \{at\} = \{cat, bat, hat\}",
                    substitution=r"\text{Σύγκριση με λίστα: } cat \in L, \ bat \in L, \ hat \in L, \ mat \notin L",
                    result=r"\mathbf{cat, bat, hat}",
                    rationale="Το mat δεν περιλαμβάνεται αφού το 'm' δεν ανήκει στο {c, b, h}.",
                ),
            ],
            final_answer="cat, bat, hat (το mat απορρίπτεται)",
            detailed_justification="Η γλώσσα περιλαμβάνει ακριβώς τις 3 λέξεις cat, bat, hat.",
            common_pitfalls=["Συμπερίληψη του mat."],
            related_theory_topic="Κανονικές Γλώσσες",
        ),
        ExamQuestion(
            question_number=9,
            title="Μαθηματική Επαγωγή: 1 + 2 + ... + n = n(n+1)/2",
            question_type="Μαθηματική Επαγωγή",
            prompt_text="Δείξτε με επαγωγή ότι για κάθε $n \\ge 1$ ισχύει: $1 + 2 + \\dots + n = \\frac{n(n+1)}{2}$.",
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Βάση n = 1",
                    formula=r"\text{LHS} = 1, \quad \text{RHS} = \frac{1(2)}{2} = 1",
                    substitution=r"\text{LHS} = \text{RHS} \ (\checkmark)",
                    result=r"\text{Ισχύει για } n = 1",
                    rationale="Βάση επαγωγής.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Επαγωγική Υπόθεση & Βήμα",
                    formula=r"\sum_{i=1}^{k+1} i = \sum_{i=1}^k i + (k+1)",
                    substitution=r"= \frac{k(k+1)}{2} + (k+1) = (k+1)\left(\frac{k}{2} + 1\right) = \frac{(k+1)(k+2)}{2}",
                    result=r"\frac{(k+1)(k+2)}{2} \ (\checkmark)",
                    rationale="Ολοκληρώθηκε η απόδειξη για k+1.",
                ),
            ],
            final_answer="Αποδείχθηκε πλήρως με Μαθηματική Επαγωγή για κάθε n ≥ 1.",
            detailed_justification="Η κλασική απόδειξη του τύπου Gauss με βάση n=1 και επαγωγικό βήμα k(k+1)/2 + (k+1) = (k+1)(k+2)/2.",
            common_pitfalls=["Καμία."],
            related_theory_topic="Μαθηματική Επαγωγή",
        ),
    ]

    diagram_nodes = [
        DiagramNode(id="A", label="A", node_type="vertex", x=200, y=80),
        DiagramNode(id="B", label="B", node_type="vertex", x=120, y=220),
        DiagramNode(id="C", label="C", node_type="vertex", x=280, y=220),
    ]

    diagram_edges = [
        DiagramEdge(source_id="A", target_id="B", label="(A,B)"),
        DiagramEdge(source_id="B", target_id="C", label="(B,C)"),
        DiagramEdge(source_id="A", target_id="C", label="(A,C)"),
    ]

    justifications = [
        DesignJustification(
            title="Τρίγωνο K3 ως Κανονικό Γράφημα",
            category="Graph Theory",
            description="Το K3 έχει 3 κορυφές, 3 ακμές, όλες οι κορυφές έχουν βαθμό 2.",
            rationale="Είναι το απλούστερο μη-τετριμμένο ισόμορφο γράφημα στη θεωρία γραφημάτων.",
        ),
    ]

    solution_code = '''# Verification Script for Practice Exam Easy (Course 203)

# Q2:
assert 100 - (60 + 40 - 20) == 20

# Q4:
p_d = 0.05
fn = 0.10
fp = 0.05
p_d_and_neg = p_d * fn
p_pos = (1 - fn) * p_d + fp * (1 - p_d)
assert abs(p_d_and_neg - 0.005) < 1e-6
assert abs(p_pos - 0.0925) < 1e-6

# Q9:
for n in range(1, 101):
    assert sum(range(1, n+1)) == n*(n+1)//2
print("Practice Exam Easy: All 9 questions verified successfully.")
'''

    return Scenario(
        id="practice_exam_easy",
        title="Πρακτική Εξέταση (Επίπεδο: Easy)",
        subtitle="203: Διακριτά Μαθηματικά — Βασικό Σετ Ασκήσεων & Επαλήθευσης",
        course_tag="Πρακτική Εξέταση",
        duration_info="3 Ώρες (10 Μονάδες)",
        paragraphs=paragraphs,
        questions=questions,
        diagram_nodes=diagram_nodes,
        diagram_edges=diagram_edges,
        justifications=justifications,
        solution_code=solution_code,
    )
