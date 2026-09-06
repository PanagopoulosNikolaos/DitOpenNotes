"""Mock Exam 3 (Standard) scenario module for Discrete Mathematics.

Transcribes Mock Exam 3 verbatim with interactive highlights, and provides
step-by-step master solutions across Groups A, B, C, D for all 3 questions.
"""

from models.scenario import (
    Scenario,
    Paragraph,
    TextSegment,
    ExamQuestion,
    CalculationStep,
    DiagramNode,
    DiagramEdge,
    DesignJustification,
)


def createMockExam3StandardScenario() -> Scenario:
    """Constructs the Scenario instance for Mock Exam 3 (Standard).

    Returns:
        Scenario: Complete scenario with verbatim text, annotations, and worked solutions.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Τμήμα Πληροφορικής και Τηλεπικοινωνιών — Πανεπιστήμιο Ιωαννίνων\n"),
                TextSegment(text="Σπυρίδων Τζίμας • Εαρινό Εξάμηνο 2025\n"),
                TextSegment(text="203: Διακριτά Μαθηματικά — Εικονική Εξέταση 3 (Κανονική)\n\n"),
                TextSegment(text="Η βαθμολογική αξία της εξέτασης είναι 10 μονάδες. Η χρονική διάρκεια είναι 3 ώρες. "),
                TextSegment(text="Επιτρέπεται στυλό μόνο μπλε και μαύρου χρώματος. Επιτρέπεται μολύβι μόνο για γραφή στο πρόχειρο. Καλή Επιτυχία!"),
            ]
        ),
        Paragraph(
            accent_border_color="var(--amber)",
            segments=[
                TextSegment(text="Θέμα 1. (3 μονάδες) ", is_highlight=True, category="logic", tag_label="Q1-LOGIC-GATES", badge_class="badge-logic", tooltip="Classification: Logic Gates & Truth Table Synthesis\nDetection Clue: 'F(A, B, C) = (A NAND B) XOR (?)... Boolean έκφραση... πίνακας αληθείας'\nApplication Rationale: Translates gate operators to Boolean symbols and builds full 8-row truth table"),
                TextSegment(text="Δίνεται η παρακάτω λογική συνάρτηση F(A, B, C) = (A NAND B) XOR (?):\n\n"),
                TextSegment(text="Ομάδα Α: (?) = C | Ομάδα Β: (?) = (B OR C) | Ομάδα Γ: (?) = (A AND C) | Ομάδα Δ: (?) = (NOT C)\n\n"),
                TextSegment(text="α'. (1.5 μονάδες) Γράψτε την αντίστοιχη Boolean έκφραση με σύμβολα (∧, ∨, ¬, ⊕).\n"),
                TextSegment(text="β'. (1.5 μονάδες) Κατασκευάστε τον πίνακα αληθείας της συνάρτησης."),
            ]
        ),
        Paragraph(
            accent_border_color="var(--blue-action)",
            segments=[
                TextSegment(text="Θέμα 2. (4 μονάδες) ", is_highlight=True, category="set", tag_label="Q2-INDEXED-SETS", badge_class="badge-set", tooltip="Classification: Indexed Family of Sets & Intervals\nDetection Clue: 'A_i = [i, i+2] για i ∈ Z^+... ένωση... τομή'\nApplication Rationale: Calculates union [1, n+2] and intersection endpoints depending on group parameter (?)"),
                TextSegment(text="Έστω η οικογένεια συνόλων A_i = [i, i+2] για i ∈ Z^+. Υπολογίστε τα ακόλουθα:\n"),
                TextSegment(text="1. ⋃_{i=1}^n A_i\n"),
                TextSegment(text="2. ⋂_{i=(?)}^{n+2} A_i\n\n"),
                TextSegment(text="Ομάδα Α: (?) = n | Ομάδα Β: (?) = n-1 | Ομάδα Γ: (?) = 1 | Ομάδα Δ: (?) = n+1\n"),
                TextSegment(text="(Προσοχή: Εξετάστε προσεκτικά τα άκρα των διαστημάτων στις τομές και ενώσεις)."),
            ]
        ),
        Paragraph(
            accent_border_color="#0284c7",
            segments=[
                TextSegment(text="Θέμα 3. (3 μονάδες) ", is_highlight=True, category="induct", tag_label="Q3-INDUCTION", badge_class="badge-induct", tooltip="Classification: Mathematical Induction (Summations & Divisibility)\nDetection Clue: 'Αποδείξτε χρησιμοποιώντας Μαθηματική Επαγωγή'\nApplication Rationale: Formally constructs base step, inductive hypothesis, and algebraic induction step"),
                TextSegment(text="Αποδείξτε χρησιμοποιώντας Μαθηματική Επαγωγή ότι:\n\n"),
                TextSegment(text="Ομάδα Α: Το άθροισμα των πρώτων n περιττών αριθμών είναι n^2.\n"),
                TextSegment(text="Ομάδα Β: Το άθροισμα των πρώτων n άρτιων αριθμών είναι n(n+1).\n"),
                TextSegment(text="Ομάδα Γ: Το 3^n - 1 είναι πολλαπλάσιο του 2 για κάθε n ≥ 1.\n"),
                TextSegment(text="Ομάδα Δ: Το 5^n - 1 είναι πολλαπλάσιο του 4 για κάθε n ≥ 1."),
            ]
        ),
    ]

    questions = [
        # QUESTION 1
        ExamQuestion(
            question_number=1,
            title="Λογικές Πύλες NAND/XOR σε Boolean & Πίνακες Αληθείας",
            question_type="Προτασιακή Λογική",
            prompt_text=(
                "Δίνεται η παρακάτω λογική συνάρτηση $F(A, B, C) = (A \\text{ NAND } B) \\text{ XOR } (?)$:\n\n"
                "- **Ομάδα Α:** $(?) = C$\n"
                "- **Ομάδα Β:** $(?) = (B \\lor C)$\n"
                "- **Ομάδα Γ:** $(?) = (A \\land C)$\n"
                "- **Ομάδα Δ:** $(?) = \\neg C$\n\n"
                "**α'. (1.5 μονάδες)** Γράψτε την αντίστοιχη Boolean έκφραση με σύμβολα ($\\land, \\lor, \\neg, \\oplus$).\n\n"
                "**β'. (1.5 μονάδες)** Κατασκευάστε τον πίνακα αληθείας της συνάρτησης."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ερώτημα α' — Μετατροπή σε Boolean Συμβολισμό",
                    formula=r"A \text{ NAND } B \equiv \neg(A \land B)",
                    substitution=(
                        r"\text{Ομάδα Α: } F = \neg(A \land B) \oplus C \\ "
                        r"\text{Ομάδα Β: } F = \neg(A \land B) \oplus (B \lor C) \\ "
                        r"\text{Ομάδα Γ: } F = \neg(A \land B) \oplus (A \land C) \\ "
                        r"\text{Ομάδα Δ: } F = \neg(A \land B) \oplus \neg C"
                    ),
                    result=r"\text{Έγκυρος Boolean συμβολισμός για όλες τις ομάδες}",
                    rationale="Η πύλη NAND αντιστοιχεί στην άρνηση της σύζευξης και η XOR στο σύμβολο ⊕.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ερώτημα β' — Πίνακας Αληθείας Ομάδας Α: F = ¬(A ∧ B) ⊕ C",
                    formula=r"\text{Πίνακας 8 γραμμών}",
                    substitution=(
                        r"\begin{array}{|c|c|c|c|c|c|} "
                        r"A & B & C & A \land B & \neg(A \land B) & F = \neg(A \land B) \oplus C \\ \hline "
                        r"0 & 0 & 0 & 0 & 1 & \mathbf{1} \\ "
                        r"0 & 0 & 1 & 0 & 1 & \mathbf{0} \\ "
                        r"0 & 1 & 0 & 0 & 1 & \mathbf{1} \\ "
                        r"0 & 1 & 1 & 0 & 1 & \mathbf{0} \\ "
                        r"1 & 0 & 0 & 0 & 1 & \mathbf{1} \\ "
                        r"1 & 0 & 1 & 0 & 1 & \mathbf{0} \\ "
                        r"1 & 1 & 0 & 1 & 0 & \mathbf{0} \\ "
                        r"1 & 1 & 1 & 1 & 0 & \mathbf{1} "
                        r"\end{array}"
                    ),
                    result=r"\text{Διάνυσμα Εξόδου Ομάδας Α: } (1, 0, 1, 0, 1, 0, 0, 1)",
                    rationale="Η πράξη XOR (⊕) δίνει 1 όταν οι δύο είσοδοι διαφέρουν και 0 όταν είναι ίδιες.",
                ),
            ],
            final_answer="α': Ομάδα Α: ¬(A ∧ B) ⊕ C | Ομάδα Β: ¬(A ∧ B) ⊕ (B ∨ C) | Ομάδα Γ: ¬(A ∧ B) ⊕ (A ∧ C) | Ομάδα Δ: ¬(A ∧ B) ⊕ ¬C\nβ': Πλήρης πίνακας αληθείας 8 γραμμών",
            detailed_justification="Η πύλη NAND έχει έξοδο 0 μόνο όταν A=1 και B=1 (σε όλες τις άλλες γραμμές είναι 1). Συνεπώς, για τις 6 πρώτες γραμμές το πρώτο όρισμα του XOR είναι σταθερά 1, αντιστρέφοντας το δεύτερο όρισμα (1 ⊕ X ≡ ¬X).",
            common_pitfalls=[
                "Λάθος στην προτεραιότητα των πράξεων: Πρώτα εκτελείται το NAND και μετά το XOR.",
            ],
            related_theory_topic="Λογικές Πύλες & Άλγεβρα Boole",
        ),

        # QUESTION 2
        ExamQuestion(
            question_number=2,
            title="Ευρετηριασμένη Οικογένεια Συνόλων A_i = [i, i+2]",
            question_type="Θεωρία Συνόλων",
            prompt_text=(
                "Έστω η οικογένεια συνόλων $A_i = [i, i+2]$ για $i \\in \\mathbb{Z}^+$ (κλειστά διαστήματα πραγματικών).\n\n"
                "**1.** Υπολογίστε την ένωση: $\\bigcup_{i=1}^{n} A_i$\n\n"
                "**2.** Υπολογίστε την τομή: $\\bigcap_{i=(?)}^{n+2} A_i$\n"
                "- **Ομάδα Α:** $(?) = n$\n"
                "- **Ομάδα Β:** $(?) = n-1$\n"
                "- **Ομάδα Γ:** $(?) = 1$\n"
                "- **Ομάδα Δ:** $(?) = n+1$"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Υπολογισμός Ένωσης (Κοινό για όλες τις ομάδες)",
                    formula=r"\bigcup_{i=1}^{n} A_i = [1, 3] \cup [2, 4] \cup \dots \cup [n, n+2]",
                    substitution=r"\text{Επειδή κάθε } [i, i+2] \text{ επικαλύπτεται με το } [i+1, i+3], \text{ η ένωση είναι το ενιαίο διάστημα } [1, n+2]",
                    result=r"\bigcup_{i=1}^{n} A_i = [1, n+2]",
                    rationale="Το ελάχιστο αριστερό άκρο είναι 1 και το μέγιστο δεξί άκρο είναι n+2.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Υπολογισμός Τομής ανά Ομάδα",
                    formula=r"\bigcap_{i=k}^{n+2} A_i = [\max_{i} \{i\}, \min_{i} \{i+2\}] = [n+2, k+2]",
                    substitution=(
                        r"\text{Ομάδα Α } (k = n): [n+2, n+2] = \{n+2\} \text{ (μονοσύνολο)}. \\ "
                        r"\text{Ομάδα Β } (k = n-1): [n+2, (n-1)+2] = [n+2, n+1] = \emptyset \text{ (αφού } n+2 > n+1). \\ "
                        r"\text{Ομάδα Γ } (k = 1): [n+2, 1+2] = [n+2, 3]. \text{ Για } n \ge 2 \implies \emptyset. \text{ (Για } n=1 \implies \{3\}). \\ "
                        r"\text{Ομάδα Δ } (k = n+1): [n+2, (n+1)+2] = [n+2, n+3] \text{ (κλειστό διάστημα)}."
                    ),
                    result=r"\text{Ομάδα Α: } \{n+2\} \mid \text{Ομάδα Β: } \emptyset \mid \text{Ομάδα Γ: } \emptyset \mid \text{Ομάδα Δ: } [n+2, n+3]",
                    rationale="Η τομή κλειστών διαστημάτων ορίζεται από το μέγιστο των κάτω άκρων και το ελάχιστο των άνω άκρων.",
                ),
            ],
            final_answer="1. Ένωση: [1, n+2] για όλες τις ομάδες\n2. Τομή:\n- Ομάδα Α: {n+2}\n- Ομάδα Β: ∅\n- Ομάδα Γ: ∅ (για n ≥ 2)\n- Ομάδα Δ: [n+2, n+3]",
            detailed_justification="Στην τομή κλειστών διαστημάτων, το αριστερό άκρο καθορίζεται από το τελευταίο διάστημα (δείκτης n+2, άρα άκρο n+2). Το δεξί άκρο καθορίζεται από το πρώτο διάστημα (δείκτης k, άρα άκρο k+2). Αν n+2 > k+2, η τομή είναι κενή.",
            common_pitfalls=[
                "Θεώρηση της τομής ως διακριτού συνόλου αντί για διάστημα πραγματικών αριθμών.",
                "Στην Ομάδα Β, το διάστημα [n+2, n+1] είναι κενό σύνολο (και όχι μονοσύνολο).",
            ],
            related_theory_topic="Ευρετηριασμένα Σύνολα & Διαστήματα",
        ),

        # QUESTION 3
        ExamQuestion(
            question_number=3,
            title="Μαθηματική Επαγωγή (Αθροίσματα & Διαιρετότητα)",
            question_type="Μαθηματική Επαγωγή",
            prompt_text=(
                "Αποδείξτε χρησιμοποιώντας Μαθηματική Επαγωγή ότι:\n\n"
                "- **Ομάδα Α:** Το άθροισμα των πρώτων $n$ περιττών αριθμών είναι $n^2$: $\\sum_{i=1}^n (2i-1) = n^2$\n"
                "- **Ομάδα Β:** Το άθροισμα των πρώτων $n$ άρτιων αριθμών είναι $n(n+1)$: $\\sum_{i=1}^n 2i = n(n+1)$\n"
                "- **Ομάδα Γ:** Το $3^n - 1$ είναι πολλαπλάσιο του 2 ($2 \\mid (3^n - 1)$) για κάθε $n \\ge 1$\n"
                "- **Ομάδα Δ:** Το $5^n - 1$ είναι πολλαπλάσιο του 4 ($4 \\mid (5^n - 1)$) για κάθε $n \\ge 1$"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ομάδα Α — Άθροισμα Περιττών: 1 + 3 + ... + (2n-1) = n^2",
                    formula=r"\text{Βάση } n=1: 2(1)-1 = 1 = 1^2 \ (\checkmark). \quad \text{Υπόθεση } n=k: \sum_{i=1}^k (2i-1) = k^2",
                    substitution=r"\text{Βήμα } k+1: \sum_{i=1}^{k+1} (2i-1) = k^2 + (2k+1) = (k+1)^2",
                    result=r"\text{Αποδείχθηκε πλήρως για } n \ge 1",
                    rationale="Η ταυτότητα k^2 + 2k + 1 = (k+1)^2 ολοκληρώνει άμεσα το επαγωγικό βήμα.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ομάδα Γ — Διαιρετότητα: 2 | (3^n - 1)",
                    formula=r"\text{Βάση } n=1: 3^1 - 1 = 2 = 2 \times 1 \ (\checkmark). \quad \text{Υπόθεση } n=k: 3^k - 1 = 2m",
                    substitution=r"3^{k+1} - 1 = 3 \cdot 3^k - 1 = 3(2m + 1) - 1 = 6m + 2 = 2(3m + 1)",
                    result=r"2(3m + 1) \implies \text{Πολλαπλάσιο του } 2 \ (\checkmark)",
                    rationale="Αντικαθιστούμε 3^k = 2m + 1 από την επαγωγική υπόθεση.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Ομάδα Δ — Διαιρετότητα: 4 | (5^n - 1)",
                    formula=r"\text{Βάση } n=1: 5^1 - 1 = 4 = 4 \times 1 \ (\checkmark). \quad \text{Υπόθεση } n=k: 5^k - 1 = 4m",
                    substitution=r"5^{k+1} - 1 = 5 \cdot 5^k - 1 = 5(4m + 1) - 1 = 20m + 4 = 4(5m + 1)",
                    result=r"4(5m + 1) \implies \text{Πολλαπλάσιο του } 4 \ (\checkmark)",
                    rationale="Αντικαθιστούμε 5^k = 4m + 1 από την επαγωγική υπόθεση.",
                ),
            ],
            final_answer="Αποδείχθηκαν όλες οι προτάσεις με πλήρη εφαρμογή των 3 βημάτων της Μαθηματικής Επαγωγής.",
            detailed_justification="Στις αποδείξεις διαιρετότητας (Ομάδες Γ, Δ), γράφουμε το a^(k+1) - 1 ως a * a^k - 1 και αντικαθιστούμε το a^k = d * m + 1, οδηγώντας σε ακέραιο πολλαπλάσιο του διαιρέτη d.",
            common_pitfalls=[
                "Ξέχασμα διατύπωσης της Επαγωγικής Υπόθεσης.",
            ],
            related_theory_topic="Μαθηματική Επαγωγή",
        ),
    ]

    diagram_nodes = [
        DiagramNode(id="A", label="A", node_type="state", x=100, y=100),
        DiagramNode(id="B", label="B", node_type="state", x=100, y=180),
        DiagramNode(id="C", label="C", node_type="state", x=100, y=260),
        DiagramNode(id="NAND", label="NAND", node_type="state", x=240, y=140),
        DiagramNode(id="XOR", label="XOR", node_type="state", x=380, y=200),
        DiagramNode(id="OUT", label="F", node_type="state", x=480, y=200),
    ]

    diagram_edges = [
        DiagramEdge(source_id="A", target_id="NAND", label=""),
        DiagramEdge(source_id="B", target_id="NAND", label=""),
        DiagramEdge(source_id="NAND", target_id="XOR", label="¬(A∧B)"),
        DiagramEdge(source_id="C", target_id="XOR", label="?"),
        DiagramEdge(source_id="XOR", target_id="OUT", label="F"),
    ]

    justifications = [
        DesignJustification(
            title="Ανάλυση Επικαλυπτόμενων Διαστημάτων",
            category="Set Theory",
            description="Η οικογένεια [i, i+2] έχει επικάλυψη μήκους 1 με το επόμενο διάστημα.",
            rationale="Δικαιολογεί γιατί η ένωση σχηματίζει ένα ενιαίο συνεχές κλειστό διάστημα [1, n+2].",
        ),
    ]

    solution_code = '''# Verification Script for Mock Exam 3 (Course 203)

# Q1: Boolean Truth Table Verification
print("Mock Exam 3 - Question 1 Truth Table:")
print("A B C | F_A F_B F_C F_D")
for a in [0, 1]:
    for b in [0, 1]:
        for c in [0, 1]:
            nand_ab = int(not (a and b))
            f_a = nand_ab ^ c
            f_b = nand_ab ^ (b or c)
            f_c = nand_ab ^ (a and c)
            f_d = nand_ab ^ int(not c)
            print(f"{a} {b} {c} |  {f_a}   {f_b}   {f_c}   {f_d}")

# Q3: Induction formulas check
assert [sum(2*i - 1 for i in range(1, n+1)) for n in range(1, 6)] == [n**2 for n in range(1, 6)]
assert [3**n - 1 for n in range(1, 6)] == [2, 8, 26, 80, 242]
assert all((3**n - 1) % 2 == 0 for n in range(1, 15))
assert all((5**n - 1) % 4 == 0 for n in range(1, 15))
print("\\nMock Exam 3 - Question 3: Induction assertions verified.")
'''

    return Scenario(
        id="mock_exam_3_standard",
        title="Εικονική Εξέταση 3 (Κανονική)",
        subtitle="203: Διακριτά Μαθηματικά — Πύλες Boole, Ευρετηριασμένα Σύνολα & Επαγωγή",
        course_tag="Εικονική Εξέταση",
        duration_info="3 Ώρες (10 Μονάδες)",
        paragraphs=paragraphs,
        questions=questions,
        diagram_nodes=diagram_nodes,
        diagram_edges=diagram_edges,
        justifications=justifications,
        solution_code=solution_code,
    )
