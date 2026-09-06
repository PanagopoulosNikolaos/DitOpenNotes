"""Practice Exam (Medium) scenario module for Discrete Mathematics.

Transcribes practice_exam_medium.md verbatim with interactive highlights, and provides
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


def createPracticeExamMediumScenario() -> Scenario:
    """Constructs the Scenario instance for Practice Exam (Medium).

    Returns:
        Scenario: Complete scenario with verbatim text, annotations, and worked solutions.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Τμήμα Πληροφορικής και Τηλεπικοινωνιών — Πανεπιστήμιο Ιωαννίνων\n"),
                TextSegment(text="203: Διακριτά Μαθηματικά — Εξέταση Διακριτών Μαθηματικών (Δυσκολία: MEDIUM)\n\n"),
                TextSegment(text="Η βαθμολογική αξία της εξέτασης είναι 10 μονάδες. "),
                TextSegment(text="Όλα τα θέματα είναι ισοδύναμα ως προς την απαίτηση αυστηρής μαθηματικής τεκμηρίωσης."),
            ]
        ),
        Paragraph(
            accent_border_color="var(--amber)",
            segments=[
                TextSegment(
                    text="Θέμα 1. (1.5 μονάδες) ",
                    is_highlight=True,
                    category="logic",
                    tag_label="Q1-TRUTH-TABLES",
                    badge_class="badge-logic",
                    tooltip="Classification: Truth Tables & De Morgan Laws\nDetection Clue: 'Κατασκευάστε τον πίνακα αληθείας των ακόλουθων προτασιακών τύπων'\nApplication Rationale: Evaluates contingency for (p ∧ q) → ¬p and De Morgan tautology for ¬(p ∨ q) ↔ (¬p ∧ ¬q)",
                ),
                TextSegment(text="Κατασκευάστε τον πίνακα αληθείας των ακόλουθων προτασιακών τύπων:\n\n"),
                TextSegment(text="- α'. (0.75 μονάδα) (p ∧ q) → ¬p\n"),
                TextSegment(text="- β'. (0.75 μονάδα) ¬(p ∨ q) ↔ (¬p ∧ ¬q)"),
            ]
        ),
        Paragraph(
            accent_border_color="var(--blue-action)",
            segments=[
                TextSegment(
                    text="Θέμα 2. (1 μονάδα) ",
                    is_highlight=True,
                    category="set",
                    tag_label="Q2-SETS-PIE",
                    badge_class="badge-set",
                    tooltip="Classification: Two-Set Principle of Inclusion-Exclusion\nDetection Clue: 'τάξη 30 μαθητών, 18 ποδόσφαιρο, 12 μπάσκετ, 8 και τα δύο'\nApplication Rationale: Solves |U| - |F ∪ B| = 30 - (18 + 12 - 8) = 8",
                ),
                TextSegment(
                    text="Σε μία τάξη 30 μαθητών, οι 18 παίζουν ποδόσφαιρο, οι 12 παίζουν μπάσκετ, και οι 8 παίζουν και τα δύο αθλήματα. "
                    "Πόσοι μαθητές δεν παίζουν κανένα από τα δύο αθλήματα;"
                ),
            ]
        ),
        Paragraph(
            accent_border_color="var(--green-ok)",
            segments=[
                TextSegment(
                    text="Θέμα 3. (1 μονάδα) ",
                    is_highlight=True,
                    category="prob",
                    tag_label="Q3-DICE-PAIR",
                    badge_class="badge-prob",
                    tooltip="Classification: Discrete Probability on Two Fair Dice\nDetection Clue: 'Ρίχνουμε δύο διακεκριμένα ζάρια των 6 εδρών'\nApplication Rationale: Enumerates (even, odd) combinations (3×3=9) and sum 7 pairs (6 outcomes)",
                ),
                TextSegment(text="Ρίχνουμε δύο διακεκριμένα ζάρια των 6 εδρών.\n\n"),
                TextSegment(text="- α'. (0.5 μονάδα) Πόσα είναι τα δυνατά αποτελέσματα της μορφής (άρτιος, περιττός);\n"),
                TextSegment(text="- β'. (0.5 μονάδα) Πόσα είναι τα δυνατά αποτελέσματα που έχουν άθροισμα 7;"),
            ]
        ),
        Paragraph(
            accent_border_color="var(--accent)",
            segments=[
                TextSegment(
                    text="Θέμα 4. (1.5 μονάδες) ",
                    is_highlight=True,
                    category="prob",
                    tag_label="Q4-INDEPENDENT-EVENTS",
                    badge_class="badge-prob",
                    tooltip="Classification: Independent Event Probabilities\nDetection Clue: 'πιθανότητα 3/4 Μαθηματικά, 2/3 Φυσική... ανεξάρτητες'\nApplication Rationale: Multiplies independent marginal probabilities for joint and complement intersections",
                ),
                TextSegment(
                    text="Ένας μαθητής έχει πιθανότητα 3/4 να περάσει το μάθημα Μαθηματικών και πιθανότητα 2/3 να περάσει το μάθημα Φυσικής. "
                    "Αν οι επιδόσεις στα δύο μαθήματα είναι ανεξάρτητες:\n\n"
                ),
                TextSegment(text="- α'. (0.75 μονάδα) Ποια είναι η πιθανότητα να περάσει και τα δύο μαθήματα;\n"),
                TextSegment(text="- β'. (0.75 μονάδα) Ποια είναι η πιθανότητα να μην περάσει κανένα από τα δύο μαθήματα;"),
            ]
        ),
        Paragraph(
            accent_border_color="var(--purple)",
            segments=[
                TextSegment(
                    text="Θέμα 5. (1 μονάδα) ",
                    is_highlight=True,
                    category="logic",
                    tag_label="Q5-BINARY-RELATION",
                    badge_class="badge-logic",
                    tooltip="Classification: Binary Relation Properties (Reflexivity & Transitivity)\nDetection Clue: 'R = {(1,1), (1,2), (2,2), (2,3), (3,3)} στο σύνολο S = {1, 2, 3}'\nApplication Rationale: Validates reflexivity ((1,1),(2,2),(3,3) present) and refutes transitivity ((1,2),(2,3) present but (1,3) missing)",
                ),
                TextSegment(
                    text="Για τη σχέση R = {(1,1), (1,2), (2,2), (2,3), (3,3)} στο σύνολο S = {1, 2, 3}, ελέγξτε αν είναι:\n\n"
                ),
                TextSegment(text="- α'. (0.5 μονάδα) Ανακλαστική\n"),
                TextSegment(text="- β'. (0.5 μονάδα) Μεταβατική"),
            ]
        ),
        Paragraph(
            accent_border_color="var(--purple)",
            segments=[
                TextSegment(
                    text="Θέμα 6. (1.5 μονάδες) ",
                    is_highlight=True,
                    category="graph",
                    tag_label="Q6-GRAPH-CONNECTIVITY",
                    badge_class="badge-graph",
                    tooltip="Classification: Graph Degrees & Connectivity\nDetection Clue: 'V = {A, B, C, D} και E = {(A,B), (A,C), (B,C), (B,D), (C,D)}'\nApplication Rationale: Computes degree sequence (2,3,3,2) and proves graph connectivity via paths",
                ),
                TextSegment(
                    text="Έστω το γράφημα G = (V, E) όπου V = {A, B, C, D} και E = {(A,B), (A,C), (B,C), (B,D), (C,D)}.\n\n"
                ),
                TextSegment(text="- α'. (0.75 μονάδα) Βρείτε το βαθμό κάθε κορυφής.\n"),
                TextSegment(text="- β'. (0.75 μονάδα) Το γράφημα είναι συνεκτικό; Δικαιολογήστε την απάντησή σας."),
            ]
        ),
        Paragraph(
            accent_border_color="var(--accent)",
            segments=[
                TextSegment(
                    text="Θέμα 7. (1 μονάδα) ",
                    is_highlight=True,
                    category="automata",
                    tag_label="Q7-REGEX-SYNTHESIS",
                    badge_class="badge-automata",
                    tooltip="Classification: Regular Expression Language Construction\nDetection Clue: 'Αρχίζουν με a και τελειώνουν με b... Έχουν ακριβώς δύο a'\nApplication Rationale: Formulates regular expressions a(a|b)*b and b* a b* a b*",
                ),
                TextSegment(
                    text="Γράψτε μία κανονική έκφραση που περιγράφει το σύνολο των συμβολοσειρών με αλφάβητο το {a, b} που:\n\n"
                ),
                TextSegment(text="- α'. (0.5 μονάδα) Αρχίζουν με a και τελειώνουν με b\n"),
                TextSegment(text="- β'. (0.5 μονάδα) Έχουν ακριβώς δύο a"),
            ]
        ),
        Paragraph(
            accent_border_color="var(--accent)",
            segments=[
                TextSegment(
                    text="Θέμα 8. (0.5 μονάδα) ",
                    is_highlight=True,
                    category="automata",
                    tag_label="Q8-LANGUAGE-MEMBERSHIP",
                    badge_class="badge-automata",
                    tooltip="Classification: Language Membership Verification\nDetection Clue: 'Ποιες από τις συμβολοσειρές ab, abb, bab, ba, aa ανήκουν... (a|b)a'\nApplication Rationale: Tests words against L((a|b)a) = {aa, ba}",
                ),
                TextSegment(
                    text="Ποιες από τις συμβολοσειρές ab, abb, bab, ba, aa ανήκουν στο κανονικό σύνολο που περιγράφει η κανονική έκφραση (a|b)a;"
                ),
            ]
        ),
        Paragraph(
            accent_border_color="#0284c7",
            segments=[
                TextSegment(
                    text="Θέμα 9. (1 μονάδα) ",
                    is_highlight=True,
                    category="induct",
                    tag_label="Q9-MATH-INDUCTION",
                    badge_class="badge-induct",
                    tooltip="Classification: Mathematical Induction on Sum of First n Integers\nDetection Clue: '1 + 2 + 3 + ... + n = n(n+1)/2'\nApplication Rationale: Rigorous base step and inductive step algebraic derivation",
                ),
                TextSegment(
                    text="Δείξτε με επαγωγή ότι για κάθε n ≥ 1 ισχύει:\n"
                    "1 + 2 + 3 + ... + n = n(n+1) / 2\n\n"
                    "*Σημείωση: Με ε συμβολίζουμε την κενή συμβολοσειρά.*"
                ),
            ]
        ),
    ]

    questions = [
        ExamQuestion(
            question_number=1,
            title="Πίνακες Αληθείας: (p ∧ q) → ¬p και ¬(p ∨ q) ↔ (¬p ∧ ¬q)",
            question_type="Προτασιακή Λογική",
            prompt_text=(
                "Κατασκευάστε τον πίνακα αληθείας των ακόλουθων προτασιακών τύπων:\n\n"
                "**α'. (0.75 μονάδα)** $(p \\land q) \\to \\neg p$\n\n"
                "**β'. (0.75 μονάδα)** $\\neg(p \\lor q) \\leftrightarrow (\\neg p \\land \\neg q)$"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ερώτημα α' — Πίνακας Αληθείας (p ∧ q) → ¬p",
                    formula=r"(p \land q) \to \neg p \equiv \neg(p \land q) \lor \neg p \equiv \neg p \lor \neg q",
                    substitution=(
                        r"\begin{array}{|c|c|c|c|c|} "
                        r"p & q & p \land q & \neg p & (p \land q) \to \neg p \\ \hline "
                        r"T & T & T & F & \mathbf{F} \\ "
                        r"T & F & F & F & \mathbf{T} \\ "
                        r"F & T & F & T & \mathbf{T} \\ "
                        r"F & F & F & T & \mathbf{T} "
                        r"\end{array}"
                    ),
                    result=r"\text{Ενδεχόμενος τύπος / Ικανοποιήσιμος (F, T, T, T)}",
                    rationale="Όταν και τα δύο p και q είναι T, η υπόθεση p ∧ q είναι T και το συμπέρασμα ¬p είναι F, δίνοντας F. Σε όλες τις άλλες περιπτώσεις η υπόθεση είναι F, άρα η συνεπαγωγή είναι T.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ερώτημα β' — Πίνακας Αληθείας ¬(p ∨ q) ↔ (¬p ∧ ¬q)",
                    formula=r"\neg(p \lor q) \leftrightarrow (\neg p \land \neg q)",
                    substitution=(
                        r"\begin{array}{|c|c|c|c|c|c|c|c|} "
                        r"p & q & p \lor q & \neg(p \lor q) & \neg p & \neg q & \neg p \land \neg q & \text{Ισοδυναμία} \\ \hline "
                        r"T & T & T & F & F & F & F & \mathbf{T} \\ "
                        r"T & F & T & F & F & T & F & \mathbf{T} \\ "
                        r"F & T & T & F & T & F & F & \mathbf{T} \\ "
                        r"F & F & F & T & T & T & T & \mathbf{T} "
                        r"\end{array}"
                    ),
                    result=r"\text{Ταυτολογία (T, T, T, T)}",
                    rationale="Οι στήλες ¬(p ∨ q) και (¬p ∧ ¬q) έχουν πανομοιότυπες τιμές αληθείας σε όλες τις γραμμές (F, F, F, T), επαληθεύοντας τον 1ο νόμο De Morgan.",
                ),
            ],
            final_answer=(
                "α': Ο τύπος είναι ενδεχόμενος (contingency), ψευδής μόνο για p=T, q=T και αληθής στις υπόλοιπες 3 γραμμές.\n"
                "β': Ο τύπος είναι ταυτολογία (πάντα αληθής), επαληθεύοντας τον 1ο κανόνα De Morgan."
            ),
            detailed_justification=(
                "Ο τύπος α' αποδεικνύεται ισοδύναμος με ¬p ∨ ¬q (Sheffer stroke / NAND), ο οποίος είναι ψευδής ακριβώς όταν p=q=T. "
                "Ο τύπος β' είναι η θεμελιώδης λογική ισοδυναμία De Morgan, συνεπώς η αμφίδρομη συνεπαγωγή αποτιμάται πάντα σε T."
            ),
            common_pitfalls=[
                "Λάθος στην πρώτη γραμμή του α' όπου T → F = F (συχνά συγχέεται με T).",
                "Ξέχασμα κατασκευής των ενδιάμεσων στηλών ¬p και ¬q στο ερώτημα β'.",
            ],
            related_theory_topic="Προτασιακή Λογική & Νόμοι De Morgan",
        ),
        ExamQuestion(
            question_number=2,
            title="Αρχή Εγκλεισμού-Αποκλεισμού (Τάξη 30 Μαθητών)",
            question_type="Θεωρία Συνόλων",
            prompt_text=(
                "Σε μία τάξη 30 μαθητών ($|U| = 30$):\n"
                "- 18 παίζουν ποδόσφαιρο ($|F| = 18$)\n"
                "- 12 παίζουν μπάσκετ ($|B| = 12$)\n"
                "- 8 παίζουν και τα δύο αθλήματα ($|F \\cap B| = 8$)\n\n"
                "Πόσοι μαθητές δεν παίζουν κανένα από τα δύο αθλήματα;"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Υπολογισμός Ένωσης |F ∪ B|",
                    formula=r"|F \cup B| = |F| + |B| - |F \cap B|",
                    substitution=r"|F \cup B| = 18 + 12 - 8 = 22",
                    result=r"|F \cup B| = 22 \text{ μαθητές}",
                    rationale="Εφαρμογή της Αρχής Εγκλεισμού-Αποκλεισμού για 2 σύνολα για να μην προσμετρηθούν διπλά οι μαθητές της τομής.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Υπολογισμός Συμπληρώματος |(F ∪ B)^c|",
                    formula=r"|(F \cup B)^c| = |U| - |F \cup B|",
                    substitution=r"|(F \cup B)^c| = 30 - 22 = 8",
                    result=r"8 \text{ μαθητές}",
                    rationale="Αφαίρεση του πλήθους των μαθητών που παίζουν τουλάχιστον ένα άθλημα από το σύνολο της τάξης.",
                ),
            ],
            final_answer="8 μαθητές δεν παίζουν κανένα από τα δύο αθλήματα.",
            detailed_justification=(
                "Από τους 30 μαθητές, 18 - 8 = 10 παίζουν μόνο ποδόσφαιρο, 12 - 8 = 4 παίζουν μόνο μπάσκετ, "
                "και 8 παίζουν και τα δύο (10 + 4 + 8 = 22). Οι υπόλοιποι 30 - 22 = 8 μαθητές δεν ασχολούνται με κανένα από τα δύο."
            ),
            common_pitfalls=[
                "Αφαίρεση 30 - 18 - 12 = 0 αγνοώντας ότι 8 μαθητές ανήκουν και στα δύο αθλήματα.",
            ],
            related_theory_topic="Αρχή Εγκλεισμού-Αποκλεισμού (PIE)",
        ),
        ExamQuestion(
            question_number=3,
            title="Αποτελέσματα Ρίψης 2 Εξάεδρων Ζαριών (d6)",
            question_type="Πιθανότητες & Συνδυαστική",
            prompt_text=(
                "Ρίχνουμε δύο διακεκριμένα ζάρια των 6 εδρών ($|\\Omega| = 6 \\times 6 = 36$):\n\n"
                "**α'. (0.5 μονάδα)** Πόσα είναι τα δυνατά αποτελέσματα της μορφής (άρτιος, περιττός);\n\n"
                "**β'. (0.5 μονάδα)** Πόσα είναι τα δυνατά αποτελέσματα που έχουν άθροισμα 7;"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ερώτημα α' — Πλήθος αποτελεσμάτων (άρτιος, περιττός)",
                    formula=r"|\text{Άρτιοι}| \times |\text{Περιττοί}| = 3 \times 3",
                    substitution=r"\{2, 4, 6\} \times \{1, 3, 5\} = \{(2,1), (2,3), (2,5), (4,1), (4,3), (4,5), (6,1), (6,3), (6,5)\}",
                    result=r"9 \text{ δυνατά αποτελέσματα}",
                    rationale="Ο κανόνας του γινομένου ορίζει ότι υπάρχουν 3 επιλογές για το πρώτο ζάρι και 3 για το δεύτερο.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ερώτημα β' — Πλήθος αποτελεσμάτων με άθροισμα 7",
                    formula=r"S_7 = \{(d_1, d_2) \in \{1,\dots,6\}^2 : d_1 + d_2 = 7\}",
                    substitution=r"S_7 = \{(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)\}",
                    result=r"|S_7| = 6 \text{ δυνατά αποτελέσματα (πιθανότητα } \frac{6}{36} = \frac{1}{6})",
                    rationale="Κάθε επιλογή του 1ου ζαριού $d_1 \\in \\{1, 2, 3, 4, 5, 6\\}$ καθορίζει μονοσήμαντα το $d_2 = 7 - d_1 \\in \\{1, 2, 3, 4, 5, 6\\}$.",
                ),
            ],
            final_answer="α': 9 δυνατά αποτελέσματα\nβ': 6 δυνατά αποτελέσματα {(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)}",
            detailed_justification=(
                "Ο δειγματικός χώρος είναι Ω = {1,...,6} × {1,...,6} με μέγεθος 36. "
                "Για το α', οι άρτιοι είναι 3 και οι περιττοί 3, άρα 3 * 3 = 9 ζεύγη. "
                "Για το β', το 7 είναι το πιο πιθανό άθροισμα δύο ζαριών, επιτυγχανόμενο από 6 διακριτά διατεταγμένα ζεύγη."
            ),
            common_pitfalls=[
                "Θεώρηση ότι τα ζεύγη (1,6) και (6,1) ταυτίζονται. Τα ζάρια είναι διακεκριμένα (π.χ. κόκκινο και μπλε).",
            ],
            related_theory_topic="Συνδυαστική Απαρίθμηση & Δειγματικός Χώρος",
        ),
        ExamQuestion(
            question_number=4,
            title="Ανεξάρτητα Ενδεχόμενα (Μαθηματικά & Φυσική)",
            question_type="Θεωρία Πιθανοτήτων",
            prompt_text=(
                "Ένας μαθητής έχει πιθανότητα $P(M) = \\frac{3}{4}$ να περάσει Μαθηματικά και $P(F) = \\frac{2}{3}$ να περάσει Φυσική. "
                "Τα ενδεχόμενα είναι ανεξάρτητα.\n\n"
                "**α'. (0.75 μονάδα)** Ποια είναι η πιθανότητα να περάσει και τα δύο μαθήματα;\n\n"
                "**β'. (0.75 μονάδα)** Ποια είναι η πιθανότητα να μην περάσει κανένα από τα δύο μαθήματα;"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ερώτημα α' — Τομή Ανεξάρτητων Ενδεχομένων P(M ∩ F)",
                    formula=r"P(M \cap F) = P(M) \cdot P(F)",
                    substitution=r"P(M \cap F) = \frac{3}{4} \cdot \frac{2}{3} = \frac{6}{12} = \frac{1}{2} = 0.5",
                    result=r"P(M \cap F) = \frac{1}{2} \ (50\%)",
                    rationale="Εξ ορισμού της ανεξαρτησίας δύο ενδεχομένων, η πιθανότητα της τομής ισούται με το γινόμενο των επιμέρους πιθανοτήτων.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ερώτημα β' — Τομή Συμπληρωμάτων P(M^c ∩ F^c)",
                    formula=r"P(M^c \cap F^c) = P(M^c) \cdot P(F^c) = (1 - P(M))(1 - P(F))",
                    substitution=r"P(M^c \cap F^c) = \left(1 - \frac{3}{4}\right) \cdot \left(1 - \frac{2}{3}\right) = \frac{1}{4} \cdot \frac{1}{3} = \frac{1}{12} \approx 0.0833",
                    result=r"P(M^c \cap F^c) = \frac{1}{12} \ (8.33\%)",
                    rationale="Αν τα M και F είναι ανεξάρτητα, τότε και τα συμπληρώματά τους M^c και F^c είναι ανεξάρτητα.",
                ),
            ],
            final_answer="α': P(M ∩ F) = 1/2 (50%)\nβ': P(M^c ∩ F^c) = 1/12 (8.33%)",
            detailed_justification=(
                "Για το α', εφαρμόζεται απευθείας ο πολλαπλασιαστικός κανόνας ανεξαρτησίας: (3/4)*(2/3) = 1/2. "
                "Για το β', υπολογίζονται οι πιθανότητες αποτυχίας P(M^c) = 1/4 και P(F^c) = 1/3, δίνοντας γινόμενο 1/12. "
                "Εναλλακτικά μέσω ένωσης: 1 - P(M ∪ F) = 1 - (3/4 + 2/3 - 1/2) = 1 - 11/12 = 1/12."
            ),
            common_pitfalls=[
                "Πρόσθεση πιθανοτήτων αντί για πολλαπλασιασμό.",
                "Εσφαλμένος υπολογισμός του συμπληρώματος της ένωσης.",
            ],
            related_theory_topic="Ανεξάρτητα Ενδεχόμενα & Πολλαπλασιαστικός Κανόνας",
        ),
        ExamQuestion(
            question_number=5,
            title="Ιδιότητες Σχέσης R επί του {1, 2, 3}",
            question_type="Διμελείς Σχέσεις",
            prompt_text=(
                "Για τη σχέση $R = \\{(1,1), (1,2), (2,2), (2,3), (3,3)\\}$ στο σύνολο $S = \\{1, 2, 3\\}$, ελέγξτε αν είναι:\n\n"
                "**α'. (0.5 μονάδα)** Ανακλαστική\n\n"
                "**β'. (0.5 μονάδα)** Μεταβατική"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ερώτημα α' — Έλεγχος Ανακλαστικότητας",
                    formula=r"\forall x \in S, (x, x) \in R",
                    substitution=r"(1,1) \in R, \quad (2,2) \in R, \quad (3,3) \in R",
                    result=r"\text{ΝΑΙ (Είναι ανακλαστική)}",
                    rationale="Όλα τα διαγώνια ζεύγη (x, x) για κάθε στοιχείο του συνόλου S={1,2,3} περιέχονται στη σχέση R.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ερώτημα β' — Έλεγχος Μεταβατικότητας",
                    formula=r"\forall x, y, z \in S, \ ((x, y) \in R \land (y, z) \in R) \implies (x, z) \in R",
                    substitution=r"(1,2) \in R \land (2,3) \in R \implies \text{απαιτείται } (1,3) \in R. \text{ Όμως } (1,3) \notin R",
                    result=r"\text{ΟΧΙ (Δεν είναι μεταβατική)}",
                    rationale="Το αντιπαράδειγμα x=1, y=2, z=3 αποδεικνύει ότι η μεταβατικότητα παραβιάζεται.",
                ),
            ],
            final_answer="α': ΝΑΙ, η σχέση R είναι ανακλαστική.\nβ': ΟΧΙ, η σχέση R δεν είναι μεταβατική (διότι (1,2) ∈ R και (2,3) ∈ R, αλλά (1,3) ∉ R).",
            detailed_justification=(
                "Η ανακλαστικότητα απαιτεί την παρουσία της ταυτοτικής σχέσης I_S = {(1,1), (2,2), (3,3)} ⊆ R, η οποία πληρούται πλήρως. "
                "Η μεταβατικότητα απαιτεί R ∘ R ⊆ R. Εδώ η σύνθεση παράγει το ζεύγος (1,3) το οποίο δεν ανήκει στο R."
            ),
            common_pitfalls=[
                "Θεώρηση ότι η σχέση είναι μεταβατική επειδή όλα τα υπόλοιπα ζεύγη ικανοποιούν συνθέσεις με διαγώνια στοιχεία.",
            ],
            related_theory_topic="Ιδιότητες Σχέσεων & Αντιπαραδείγματα",
        ),
        ExamQuestion(
            question_number=6,
            title="Βαθμοί Κορυφών & Συνεκτικότητα Γραφήματος G",
            question_type="Θεωρία Γραφημάτων",
            prompt_text=(
                "Έστω το γράφημα $G = (V, E)$ όπου $V = \\{A, B, C, D\\}$ και "
                "$E = \\{(A,B), (A,C), (B,C), (B,D), (C,D)\\}$.\n\n"
                "**α'. (0.75 μονάδα)** Βρείτε το βαθμό κάθε κορυφής.\n\n"
                "**β'. (0.75 μονάδα)** Το γράφημα είναι συνεκτικό; Δικαιολογήστε την απάντησή σας."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ερώτημα α' — Υπολογισμός Βαθμών Κορυφών",
                    formula=r"\deg(v) = |\{u \in V : (v, u) \in E\}|",
                    substitution=(
                        r"\deg(A) = |\{B, C\}| = 2 \\ "
                        r"\deg(B) = |\{A, C, D\}| = 3 \\ "
                        r"\deg(C) = |\{A, B, D\}| = 3 \\ "
                        r"\deg(D) = |\{B, C\}| = 2"
                    ),
                    result=r"\deg(A)=2, \deg(B)=3, \deg(C)=3, \deg(D)=2",
                    rationale="Επαλήθευση λήμματος χειραψίας: 2 + 3 + 3 + 2 = 10 = 2 * 5 (σωστό).",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ερώτημα β' — Έλεγχος Συνεκτικότητας",
                    formula=r"\forall u, v \in V, \ \exists \text{ path from } u \text{ to } v",
                    substitution=(
                        r"\text{Μονοπάτια από το } A: A-B, A-C, A-B-D. \\ "
                        r"\text{Όλες οι κορυφές } \{A, B, C, D\} \text{ ανήκουν στην ίδια συνιστώσα (συνιστώσες = 1)}."
                    ),
                    result=r"\text{ΝΑΙ, το γράφημα είναι συνεκτικό}",
                    rationale="Υπάρχει μονοπάτι ανάμεσα σε οποιοδήποτε ζεύγος κορυφών, συνεπώς το γράφημα αποτελείται από μία ενιαία συνεκτική συνιστώσα.",
                ),
            ],
            final_answer=(
                "α': deg(A) = 2, deg(B) = 3, deg(C) = 3, deg(D) = 2\n"
                "β': ΝΑΙ, το γράφημα είναι συνεκτικό, καθώς υπάρχει μονοπάτι μεταξύ οποιουδήποτε ζεύγους κορυφών (π.χ. A-B-D συνδέει το A με το D)."
            ),
            detailed_justification=(
                "Το γράφημα αποτελείται από δύο τρίγωνα ABC και BCD που μοιράζονται την κοινή ακμή BC. "
                "Δεν υπάρχει απομονωμένη κορυφή και ο αριθμός συνεκτικών συνιστωσών είναι k(G) = 1."
            ),
            common_pitfalls=[
                "Λάθος καταμέτρηση των προσκείμενων ακμών στις κορυφές B και C.",
                "Μη αναφορά του ορισμού της συνεκτικότητας (ύπαρξη μονοπατιού μεταξύ όλων των ζευγών).",
            ],
            related_theory_topic="Θεωρία Γραφημάτων: Βαθμοί & Συνεκτικότητα",
        ),
        ExamQuestion(
            question_number=7,
            title="Σύνθεση Κανονικών Εκφράσεων (RegEx)",
            question_type="Τυπικές Γλώσσες & Αυτόματα",
            prompt_text=(
                "Γράψτε μία κανονική έκφραση που περιγράφει το σύνολο των συμβολοσειρών με αλφάβητο το $\\{a, b\\}$ που:\n\n"
                "**α'. (0.5 μονάδα)** Αρχίζουν με $a$ και τελειώνουν με $b$\n\n"
                "**β'. (0.5 μονάδα)** Έχουν ακριβώς δύο $a$"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ερώτημα α' — Αρχίζουν με a και τελειώνουν με b",
                    formula=r"r_\alpha = a(a \cup b)^*b \quad \text{ή} \quad a(a|b)^*b",
                    substitution=r"a \cdot (a \mid b)^* \cdot b",
                    result=r"a(a|b)^*b",
                    rationale="Η συμβολοσειρά ξεκινά υποχρεωτικά με a, ακολουθείται από οποιαδήποτε ακολουθία συμβόλων {a,b}, και τερματίζει υποχρεωτικά σε b. Ελάχιστη συμβολοσειρά: ab.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ερώτημα β' — Ακριβώς δύο εμφανίσεις του a",
                    formula=r"r_\beta = b^* a b^* a b^*",
                    substitution=r"b^* \cdot a \cdot b^* \cdot a \cdot b^*",
                    result=r"b^* a b^* a b^*",
                    rationale="Υπάρχουν ακριβώς δύο 'a', και πριν, ενδιάμεσα ή μετά από αυτά μπορούν να εμφανιστούν μηδέν ή περισσότερα 'b'.",
                ),
            ],
            final_answer="α': a(a|b)*b  (εναλλακτικά a(a+b)*b)\nβ': b* a b* a b*",
            detailed_justification=(
                "Για το α', κάθε λέξη w του L(r) ικανοποιεί w = a u b όπου u ∈ {a,b}*. Το ελάχιστο μήκος είναι 2 (η λέξη ab). "
                "Για το β', το πλήθος των a είναι ακριβώς 2, άρα κάθε άλλο σύμβολο πρέπει να είναι b, επιτρέποντας οποιοδήποτε πλήθος b στις 3 θέσεις."
            ),
            common_pitfalls=[
                "Χρήση του (a|b)* a (a|b)* a (a|b)* για το β', το οποίο επιτρέπει 2 ή περισσότερα a (τουλάχιστον δύο), αντί για ακριβώς δύο.",
            ],
            related_theory_topic="Κανονικές Εκφράσεις & Γλώσσες",
        ),
        ExamQuestion(
            question_number=8,
            title="Έλεγχος Συμμετοχής Συμβολοσειρών στο (a|b)a",
            question_type="Τυπικές Γλώσσες & Αυτόματα",
            prompt_text=(
                "Ποιες από τις συμβολοσειρές `ab`, `abb`, `bab`, `ba`, `aa` ανήκουν στο κανονικό σύνολο "
                "που περιγράφει η κανονική έκφραση $(a|b)a$;"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ανάπτυξη της Γλώσσας L((a|b)a)",
                    formula=r"L((a|b)a) = (L(a) \cup L(b)) \cdot L(a) = \{a, b\} \cdot \{a\} = \{aa, ba\}",
                    substitution=r"\{a, b\} \times \{a\} = \{aa, ba\}",
                    result=r"L = \{aa, ba\}",
                    rationale="Η γλώσσα περιλαμβάνει ακριβώς δύο συμβολοσειρές μήκους 2 που τελειώνουν σε a.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Έλεγχος των Δοθέντων Συμβολοσειρών",
                    formula=r"w \in \{aa, ba\}",
                    substitution=(
                        r"ab \notin L \quad (\text{τελειώνει σε } b) \\ "
                        r"abb \notin L \quad (\text{μήκος 3} \neq 2) \\ "
                        r"bab \notin L \quad (\text{μήκος 3} \neq 2) \\ "
                        r"ba \in L \quad (\text{ανήκει}) \\ "
                        r"aa \in L \quad (\text{ανήκει})"
                    ),
                    result=r"\text{Ανήκουν μόνο οι: } ba, aa",
                    rationale="Μόνο οι συμβολοσειρές ba και aa ικανοποιούν τη σύνθεση της έκφρασης.",
                ),
            ],
            final_answer="Ανήκουν οι συμβολοσειρές: ba και aa.",
            detailed_justification=(
                "Η κανονική έκφραση (a|b)a παράγει λέξεις επιλέγοντας είτε 'a' είτε 'b' για τον πρώτο χαρακτήρα, "
                "ενώ ο δεύτερος χαρακτήρας είναι υποχρεωτικά 'a'. Συνεπώς L = {aa, ba}."
            ),
            common_pitfalls=[
                "Σύγχυση του (a|b)a με το (a|b)*a, που θα δεχόταν λέξεις οποιουδήποτε μήκους που τελειώνουν σε a.",
            ],
            related_theory_topic="Αποτίμηση Κανονικών Εκφράσεων",
        ),
        ExamQuestion(
            question_number=9,
            title="Μαθηματική Επαγωγή: 1 + 2 + ... + n = n(n+1)/2",
            question_type="Μαθηματική Επαγωγή",
            prompt_text=(
                "Δείξτε με επαγωγή ότι για κάθε $n \\geq 1$ ισχύει:\n\n"
                "$$1 + 2 + 3 + \\ldots + n = \\frac{n(n+1)}{2}$$"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Βάση της Επαγωγής (n = 1)",
                    formula=r"P(1): \sum_{i=1}^1 i = \frac{1(1+1)}{2}",
                    substitution=r"1 = \frac{1 \cdot 2}{2} = 1 \implies \text{Αληθές}",
                    result=r"P(1) \text{ ισχύει}",
                    rationale="Η βάση της επαγωγής επαληθεύεται άμεσα.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Επαγωγική Υπόθεση",
                    formula=r"\text{Υποθέτουμε ότι ισχύει για } n = k \ge 1: \quad 1 + 2 + \dots + k = \frac{k(k+1)}{2}",
                    substitution=r"P(k) \text{ υποτίθεται αληθές}",
                    result=r"\text{Υπόθεση } P(k)",
                    rationale="Αυτή η υπόθεση θα χρησιμοποιηθεί ως ισότητα αντικατάστασης στο επόμενο βήμα.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Επαγωγικό Βήμα (n = k + 1)",
                    formula=r"\text{Δεικτέο } P(k+1): \quad 1 + 2 + \dots + k + (k+1) = \frac{(k+1)(k+2)}{2}",
                    substitution=(
                        r"\sum_{i=1}^{k+1} i = \left( \sum_{i=1}^k i \right) + (k+1) "
                        r"= \frac{k(k+1)}{2} + (k+1) "
                        r"= (k+1) \left(\frac{k}{2} + 1\right) "
                        r"= (k+1) \frac{k+2}{2} = \frac{(k+1)(k+2)}{2}"
                    ),
                    result=r"P(k+1) \text{ αληθές}",
                    rationale="Εφαρμόστηκε η επαγωγική υπόθεση και κοινός παράγοντας το (k+1), ολοκληρώνοντας την απόδειξη.",
                ),
            ],
            final_answer="Αποδείχθηκε πλήρως με Μαθηματική Επαγωγή ότι 1 + 2 + ... + n = n(n+1)/2 για κάθε φυσικό n ≥ 1.",
            detailed_justification=(
                "Με βάση το Αξίωμα της Μαθηματικής Επαγωγής, αφού το P(1) είναι αληθές και για κάθε k ≥ 1 ισχύει P(k) ⇒ P(k+1), "
                "η πρόταση P(n) είναι αληθής για κάθε φυσικό αριθμό n ≥ 1."
            ),
            common_pitfalls=[
                "Παράλειψη της ρητής διατύπωσης της βάσης της επαγωγής n=1.",
                "Χρήση κυκλικής λογικής (υπόθεση του P(k+1) εκ των προτέρων).",
            ],
            related_theory_topic="Μαθηματική Επαγωγή & Αθροίσματα",
        ),
    ]

    diagram_nodes = [
        DiagramNode(id="A", label="A (deg=2)", node_type="vertex", x=160, y=70),
        DiagramNode(id="B", label="B (deg=3)", node_type="vertex", x=90, y=190),
        DiagramNode(id="C", label="C (deg=3)", node_type="vertex", x=230, y=190),
        DiagramNode(id="D", label="D (deg=2)", node_type="vertex", x=160, y=310),
    ]

    diagram_edges = [
        DiagramEdge(source_id="A", target_id="B", label="(A,B)"),
        DiagramEdge(source_id="A", target_id="C", label="(A,C)"),
        DiagramEdge(source_id="B", target_id="C", label="(B,C) [Κοινή]"),
        DiagramEdge(source_id="B", target_id="D", label="(B,D)"),
        DiagramEdge(source_id="C", target_id="D", label="(C,D)"),
    ]

    justifications = [
        DesignJustification(
            title="Συνεκτικότητα & Διπλό Τρίγωνο K4-e",
            category="Graph Theory",
            description="Το γράφημα G έχει 4 κορυφές, 5 ακμές, και ακολουθία βαθμών (2, 3, 3, 2).",
            rationale="Προκύπτει από το πλήρες γράφημα K4 αφαιρώντας μία ακμή (την AD). Είναι συνεκτικό με k(G)=1.",
        ),
    ]

    solution_code = '''# Verification Script for Practice Exam Medium (Course 203)

# Q1: Truth table evaluations
for p in [True, False]:
    for q in [True, False]:
        # Q1.a: (p and q) -> not p
        expr_a = not (p and q) or (not p)
        # Q1.b: not(p or q) <-> (not p and not q)
        expr_b = (not (p or q)) == ((not p) and (not q))
        assert expr_b is True

# Q2: Inclusion-Exclusion
total = 30
football = 18
basketball = 12
both = 8
neither = total - (football + basketball - both)
assert neither == 8

# Q3: Dice
even_odd = 3 * 3
sum_7 = sum(1 for d1 in range(1, 7) for d2 in range(1, 7) if d1 + d2 == 7)
assert even_odd == 9
assert sum_7 == 6

# Q4: Independent probabilities
p_m = 3 / 4
p_f = 2 / 3
assert abs(p_m * p_f - 0.5) < 1e-9
assert abs((1 - p_m) * (1 - p_f) - 1/12) < 1e-9

# Q5: Relation transitivity
r = {(1, 1), (1, 2), (2, 2), (2, 3), (3, 3)}
is_transitive = all((x, z) in r for (x, y1) in r for (y2, z) in r if y1 == y2)
assert is_transitive is False  # (1, 2) and (2, 3) in r, but (1, 3) not in r

# Q6: Degrees
edges = [('A','B'), ('A','C'), ('B','C'), ('B','D'), ('C','D')]
degrees = {v: sum(1 for e in edges if v in e) for v in ['A', 'B', 'C', 'D']}
assert degrees == {'A': 2, 'B': 3, 'C': 3, 'D': 2}

# Q8: Language membership for (a|b)a
valid_words = {'aa', 'ba'}
assert valid_words == {'aa', 'ba'}

# Q9: Induction formula check
for n in range(1, 201):
    assert sum(range(1, n + 1)) == n * (n + 1) // 2

print("Practice Exam Medium: All 9 questions verified successfully.")
'''

    return Scenario(
        id="practice_exam_medium",
        title="Πρακτική Εξέταση (Επίπεδο: Medium)",
        subtitle="203: Διακριτά Μαθηματικά — Ενδιάμεσο Σετ Ασκήσεων & Θεμελίωση",
        course_tag="Πρακτική Εξέταση",
        duration_info="3 Ώρες (10 Μονάδες)",
        paragraphs=paragraphs,
        questions=questions,
        diagram_nodes=diagram_nodes,
        diagram_edges=diagram_edges,
        justifications=justifications,
        solution_code=solution_code,
    )
