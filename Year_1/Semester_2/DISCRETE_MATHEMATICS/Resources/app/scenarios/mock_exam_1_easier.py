"""Mock Exam 1 (Easier) scenario module for Discrete Mathematics.

Transcribes Mock Exam 1 verbatim with interactive highlights, and provides
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


def createMockExam1EasierScenario() -> Scenario:
    """Constructs the Scenario instance for Mock Exam 1 (Easier).

    Returns:
        Scenario: Complete scenario with verbatim text, annotations, and worked solutions.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Τμήμα Πληροφορικής και Τηλεπικοινωνιών — Πανεπιστήμιο Ιωαννίνων\n"),
                TextSegment(text="Σπυρίδων Τζίμας • Εαρινό Εξάμηνο 2025\n"),
                TextSegment(text="203: Διακριτά Μαθηματικά — Εικονική Εξέταση 1 (Ευκολότερη)\n\n"),
                TextSegment(text="Η βαθμολογική αξία της εξέτασης είναι 10 μονάδες. Η χρονική διάρκεια είναι 3 ώρες. "),
                TextSegment(text="Επιτρέπεται στυλό μόνο μπλε και μαύρου χρώματος. Επιτρέπεται μολύβι μόνο για γραφή στο πρόχειρο. Καλή Επιτυχία!"),
            ]
        ),
        Paragraph(
            accent_border_color="var(--blue-action)",
            segments=[
                TextSegment(text="Θέμα 1. (3 μονάδες) ", is_highlight=True, category="set", tag_label="Q1-SETS", badge_class="badge-set", tooltip="Classification: Set Operations & Complements\nDetection Clue: 'A = {1, 2, 3, 4}, B = {3, 4, 5, 6}... (A ∪ B)^c ∪ (?)'\nApplication Rationale: Compute union, relative complement, and set union with group parameter"),
                TextSegment(text="Δίνονται τα σύνολα A = {1, 2, 3, 4}, B = {3, 4, 5, 6} και το καθολικό σύνολο Ω = {1, 2, 3, 4, 5, 6, 7, 8}.\n"),
                TextSegment(text="Υπολογίστε το σύνολο: (A ∪ B)^c ∪ (?)\n\n"),
                TextSegment(text="Ομάδα Α: (?) = A ∩ B | Ομάδα Β: (?) = A \\ B | Ομάδα Γ: (?) = B \\ A | Ομάδα Δ: (?) = A ⊕ B"),
            ]
        ),
        Paragraph(
            accent_border_color="var(--amber)",
            segments=[
                TextSegment(text="Θέμα 2. (3 μονάδες) ", is_highlight=True, category="logic", tag_label="Q2-TRUTH-TABLE", badge_class="badge-logic", tooltip="Classification: Truth Table & Propositional Classification\nDetection Clue: '((p ∨ q) ∧ ¬p) → (?)... ταυτολογία, αντίφαση ή ενδεχομενικότητα'\nApplication Rationale: Evaluates conditional expression with reduced premise (¬p ∧ q)"),
                TextSegment(text="Κατασκευάστε τον πίνακα αληθείας για τον παρακάτω προτασιακό τύπο και προσδιορίστε αν είναι ταυτολογία, αντίφαση ή ενδεχομενικότητα:\n"),
                TextSegment(text="((p ∨ q) ∧ ¬p) → (?)\n\n"),
                TextSegment(text="Ομάδα Α: (?) = q | Ομάδα Β: (?) = ¬q | Ομάδα Γ: (?) = p ∧ q | Ομάδα Δ: (?) = p ∨ q"),
            ]
        ),
        Paragraph(
            accent_border_color="var(--purple)",
            segments=[
                TextSegment(text="Θέμα 3. (4 μονάδες) ", is_highlight=True, category="graph", tag_label="Q3-HANDSHAKING", badge_class="badge-graph", tooltip="Classification: Handshaking Lemma & Graphical Degree Sequences\nDetection Clue: 'απλό μη κατευθυνόμενο γράφημα... βαθμοί {2, 2, 2, 3, (?)}'\nApplication Rationale: Validates Handshaking Lemma (even degree sum) and simple graph maximum degree <= 4"),
                TextSegment(text="Δίνεται ένα απλό μη κατευθυνόμενο γράφημα G = (V, E) με σύνολο κορυφών V = {v1, v2, v3, v4, v5}. "),
                TextSegment(text="Οι βαθμοί των κορυφών είναι αντίστοιχα {2, 2, 2, 3, (?)}.\n\n"),
                TextSegment(text="Ομάδα Α: (?) = 1 | Ομάδα Β: (?) = 3 | Ομάδα Γ: (?) = 5 | Ομάδα Δ: (?) = 7\n\n"),
                TextSegment(text="α'. (2 μονάδες) Σχεδιάστε ένα τέτοιο γράφημα, αν υπάρχει. Αν δεν υπάρχει, εξηγήστε το γιατί.\n"),
                TextSegment(text="β'. (2 μονάδες) Πόσες ακμές έχει το γράφημα (αν υπάρχει);"),
            ]
        ),
    ]

    questions = [
        # QUESTION 1
        ExamQuestion(
            question_number=1,
            title="Πράξεις Συνόλων & Συμπληρώματα",
            question_type="Θεωρία Συνόλων",
            prompt_text=(
                "Δίνονται τα σύνολα $A = \\{1, 2, 3, 4\\}$, $B = \\{3, 4, 5, 6\\}$ και το καθολικό σύνολο $\\Omega = \\{1, 2, 3, 4, 5, 6, 7, 8\\}$.\n"
                "Υπολογίστε το σύνολο: $(A \\cup B)^c \\cup (?)$\n\n"
                "- **Ομάδα Α:** $(?) = A \\cap B$\n"
                "- **Ομάδα Β:** $(?) = A \\setminus B$\n"
                "- **Ομάδα Γ:** $(?) = B \\setminus A$\n"
                "- **Ομάδα Δ:** $(?) = A \\oplus B$"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Υπολογισμός Κοινού Τμήματος (A ∪ B)^c",
                    formula=r"(A \cup B)^c = \Omega \setminus (A \cup B)",
                    substitution=r"A \cup B = \{1, 2, 3, 4, 5, 6\} \implies (A \cup B)^c = \{7, 8\}",
                    result=r"(A \cup B)^c = \{7, 8\}",
                    rationale="Τα στοιχεία 7 και 8 είναι τα μόνα στοιχεία του καθολικού συνόλου Ω που δεν ανήκουν ούτε στο A ούτε στο B.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Υπολογισμός των Επιμέρους Συνόλων (?) ανά Ομάδα",
                    formula=r"\text{Υπολογισμός } (?)",
                    substitution=(
                        r"\text{Ομάδα Α: } A \cap B = \{3, 4\} \\ "
                        r"\text{Ομάδα Β: } A \setminus B = \{1, 2\} \\ "
                        r"\text{Ομάδα Γ: } B \setminus A = \{5, 6\} \\ "
                        r"\text{Ομάδα Δ: } A \oplus B = (A \setminus B) \cup (B \setminus A) = \{1, 2, 5, 6\}"
                    ),
                    result=r"\text{Επιμέρους σύνολα έτοιμα για ένωση}",
                    rationale="Βασικές πράξεις τομής, διαφοράς και συμμετρικής διαφοράς συνόλων.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Τελική Ένωση με το {7, 8}",
                    formula=r"\{7, 8\} \cup (?)",
                    substitution=(
                        r"\text{Ομάδα Α: } \{7, 8\} \cup \{3, 4\} = \{3, 4, 7, 8\} \\ "
                        r"\text{Ομάδα Β: } \{7, 8\} \cup \{1, 2\} = \{1, 2, 7, 8\} \\ "
                        r"\text{Ομάδα Γ: } \{7, 8\} \cup \{5, 6\} = \{5, 6, 7, 8\} \\ "
                        r"\text{Ομάδα Δ: } \{7, 8\} \cup \{1, 2, 5, 6\} = \{1, 2, 5, 6, 7, 8\}"
                    ),
                    result=r"\text{Ομάδα Α: } \{3,4,7,8\} \mid \text{Ομάδα Β: } \{1,2,7,8\} \mid \text{Ομάδα Γ: } \{5,6,7,8\} \mid \text{Ομάδα Δ: } \{1,2,5,6,7,8\}",
                    rationale="Προσθέτουμε τα στοιχεία 7 και 8 σε κάθε επιμέρους σύνολο.",
                ),
            ],
            final_answer="Ομάδα Α: {3, 4, 7, 8}\nΟμάδα Β: {1, 2, 7, 8}\nΟμάδα Γ: {5, 6, 7, 8}\nΟμάδα Δ: {1, 2, 5, 6, 7, 8}",
            detailed_justification="Το συμπλήρωμα (A ∪ B)^c ισούται με {7, 8}. Η ένωση αυτού με το εκάστοτε σύνολο (?) της ομάδας δίνει άμεσα το ζητούμενο.",
            common_pitfalls=[
                "Ξέχασμα του καθολικού συνόλου Ω κατά τον υπολογισμό του συμπληρώματος.",
            ],
            related_theory_topic="Θεωρία Συνόλων & Πράξεις",
        ),

        # QUESTION 2
        ExamQuestion(
            question_number=2,
            title="Πίνακες Αληθείας & Ταξινόμηση Προτασιακού Τύπου",
            question_type="Προτασιακή Λογική",
            prompt_text=(
                "Κατασκευάστε τον πίνακα αληθείας για τον παρακάτω προτασιακό τύπο και προσδιορίστε αν είναι "
                "**ταυτολογία**, **αντίφαση** ή **ενδεχομενικότητα**:\n"
                "$$((p \\lor q) \\land \\neg p) \\to (?)$$\n\n"
                "- **Ομάδα Α:** $(?) = q$\n"
                "- **Ομάδα Β:** $(?) = \\neg q$\n"
                "- **Ομάδα Γ:** $(?) = p \\land q$\n"
                "- **Ομάδα Δ:** $(?) = p \\lor q$"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Απλοποίηση της Υπόθεσης",
                    formula=r"(p \lor q) \land \neg p \equiv (\neg p \land p) \lor (\neg p \land q) \equiv \bot \lor (\neg p \land q) \equiv \neg p \land q",
                    substitution=r"\text{Η υπόθεση είναι αληθής ΜΟΝΟ όταν } p = F \text{ και } q = T",
                    result=r"\text{Υπόθεση } = T \iff (p, q) = (F, T)",
                    rationale="Σε όλες τις άλλες 3 γραμμές (F,F), (T,F), (T,T), η υπόθεση είναι F, άρα η συνεπαγωγή F -> (?) είναι αυτόματα T!",
                ),
                CalculationStep(
                    step_number=2,
                    title="Έλεγχος της Γραμμής (p=F, q=T) ανά Ομάδα",
                    formula=r"\text{Στη γραμμή } (F, T): \text{Υπόθεση} = T \implies \text{Τελική Τιμή} = (?)",
                    substitution=(
                        r"\text{Ομάδα Α: } (?) = q = T \implies T \to T = \mathbf{T} \implies \mathbf{Ταυτολογία} \\ "
                        r"\text{Ομάδα Β: } (?) = \neg q = F \implies T \to F = \mathbf{F} \implies \mathbf{Ενδεχομενικότητα} \\ "
                        r"\text{Ομάδα Γ: } (?) = p \land q = F \land T = F \implies T \to F = \mathbf{F} \implies \mathbf{Ενδεχομενικότητα} \\ "
                        r"\text{Ομάδα Δ: } (?) = p \lor q = F \lor T = T \implies T \to T = \mathbf{T} \implies \mathbf{Ταυτολογία}"
                    ),
                    result=r"\text{Ομάδες Α, Δ: Ταυτολογίες} \mid \text{Ομάδες Β, Γ: Ενδεχομενικότητες}",
                    rationale="Επειδή στις άλλες 3 γραμμές η συνεπαγωγή είναι T, ο τύπος γίνεται F αν και μόνο αν το (?) είναι F στη γραμμή (F, T).",
                ),
            ],
            final_answer="Ομάδα Α: Ταυτολογία (Tautology)\nΟμάδα Β: Ενδεχομενικότητα (Contingency - F στη γραμμή p=F, q=T)\nΟμάδα Γ: Ενδεχομενικότητα (Contingency - F στη γραμμή p=F, q=T)\nΟμάδα Δ: Ταυτολογία (Tautology)",
            detailed_justification="Η έκφραση (p ∨ q) ∧ ¬p είναι ισοδύναμη με ¬p ∧ q. Αυτή είναι αληθής μόνο όταν p=F και q=T. Στις υπόλοιπες περιπτώσεις η υπόθεση είναι ψευδής, οπότε η συνεπαγωγή είναι τετριμμένα αληθής. Άρα η τιμή αληθείας καθορίζεται εξ ολοκλήρου από την τιμή του συμπεράσματος (?) στη γραμμή p=F, q=T.",
            common_pitfalls=[
                "Λανθασμένη εκτίμηση της αντίφασης: Κανένας από τους τύπους δεν είναι αντίφαση, καθώς σε 3 από τις 4 γραμμές αποτιμώνται πάντα σε T.",
            ],
            related_theory_topic="Προτασιακή Λογική & Ταξινόμηση",
        ),

        # QUESTION 3
        ExamQuestion(
            question_number=3,
            title="Γραφήματα, Λήμμα Χειραψιών & Βαθμοί Κορυφών",
            question_type="Θεωρία Γραφημάτων",
            prompt_text=(
                "Δίνεται ένα απλό μη κατευθυνόμενο γράφημα $G = (V, E)$ με σύνολο κορυφών $V = \\{v_1, v_2, v_3, v_4, v_5\\}$. "
                "Οι βαθμοί των κορυφών είναι αντίστοιχα $\\{2, 2, 2, 3, (?)\\}$.\n\n"
                "- **Ομάδα Α:** $(?) = 1$\n"
                "- **Ομάδα Β:** $(?) = 3$\n"
                "- **Ομάδα Γ:** $(?) = 5$\n"
                "- **Ομάδα Δ:** $(?) = 7$\n\n"
                "**α'. (2 μονάδες)** Σχεδιάστε ένα τέτοιο γράφημα, αν υπάρχει. Αν δεν υπάρχει, εξηγήστε το γιατί.\n\n"
                "**β'. (2 μονάδες)** Πόσες ακμές έχει το γράφημα (αν υπάρχει);"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Έλεγχος Θεωρήματος Χειραψιών & Μέγιστου Βαθμού",
                    formula=r"\sum_{i=1}^{n} \deg(v_i) = 2|E| \quad \text{και} \quad \deg_{\max} \le n - 1",
                    substitution=r"n = |V| = 5 \implies \deg_{\max} \le 5 - 1 = 4",
                    result=r"\text{Μέγιστος επιτρεπτός βαθμός σε απλό γράφημα με 5 κορυφές: } 4",
                    rationale="Σε απλό γράφημα δεν επιτρέπονται βρόχοι ούτε παράλληλες ακμές, άρα κάθε κορυφή μπορεί να συνδεθεί με το πολύ n-1 άλλες κορυφές.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ανάλυση ανά Ομάδα",
                    formula=r"\text{Έλεγχος } (?) \in \{1, 3, 5, 7\}",
                    substitution=(
                        r"\text{Ομάδα Α } ((?) = 1): \sum \deg = 2+2+2+3+1 = 10 \text{ (άρτιο)}. |E| = 10/2 = 5. \deg_{\max} = 3 \le 4. \implies \mathbf{Υπάρχει, } |E|=5. \\ "
                        r"\text{Ομάδα Β } ((?) = 3): \sum \deg = 2+2+2+3+3 = 12 \text{ (άρτιο)}. |E| = 12/2 = 6. \deg_{\max} = 3 \le 4. \implies \mathbf{Υπάρχει, } |E|=6. \\ "
                        r"\text{Ομάδα Γ } ((?) = 5): \mathbf{ΠΑΓΙΔΑ!} \deg(v_5) = 5 > 4 = n-1. \implies \mathbf{ΔΕΝ Υπάρχει}. \\ "
                        r"\text{Ομάδα Δ } ((?) = 7): \mathbf{ΠΑΓΙΔΑ!} \deg(v_5) = 7 > 4 = n-1. \implies \mathbf{ΔΕΝ Υπάρχει}."
                    ),
                    result=r"\text{Ομάδα Α: Υπάρχει (5 ακμές)} \mid \text{Ομάδα Β: Υπάρχει (6 ακμές)} \mid \text{Ομάδες Γ, Δ: ΔΕΝ υπάρχουν}",
                    rationale="Στις ομάδες Γ και Δ, ο βαθμός 5 και 7 υπερβαίνει το θεωρητικό όριο n-1=4 ενός απλού γραφήματος.",
                ),
            ],
            final_answer="Ομάδα Α: Γράφημα Υπάρχει, Ακμές = 5\nΟμάδα Β: Γράφημα Υπάρχει, Ακμές = 6\nΟμάδα Γ: Γράφημα ΔΕΝ υπάρχει (deg(v5)=5 > n-1=4)\nΟμάδα Δ: Γράφημα ΔΕΝ υπάρχει (deg(v5)=7 > n-1=4)",
            detailed_justification="Σε ένα απλό γράφημα με 5 κορυφές, η μέγιστη δυνατή τιμή βαθμού είναι 4. Συνεπώς, για τις Ομάδες Γ και Δ το γράφημα είναι αδύνατον να υπάρξει. Για την Ομάδα Α, το άθροισμα των βαθμών είναι 10, άρα e = 5. Για την Ομάδα Β, το άθροισμα είναι 12, άρα e = 6.",
            common_pitfalls=[
                "Εφαρμογή μόνο του λήμματος χειραψιών: Στην Ομάδα Γ, το άθροισμα 2+2+2+3+5 = 14 είναι άρτιο, αλλά το γράφημα ΔΕΝ υπάρχει γιατί deg=5 σε 5 κορυφές απαιτεί βρόχο ή πολλαπλή ακμή.",
            ],
            related_theory_topic="Θεωρία Γραφημάτων & Βαθμοί Κορυφών",
        ),
    ]

    diagram_nodes = [
        DiagramNode(id="v1", label="v1 (d=3)", node_type="vertex", x=200, y=80),
        DiagramNode(id="v2", label="v2 (d=2)", node_type="vertex", x=320, y=160),
        DiagramNode(id="v3", label="v3 (d=2)", node_type="vertex", x=270, y=260),
        DiagramNode(id="v4", label="v4 (d=2)", node_type="vertex", x=130, y=260),
        DiagramNode(id="v5", label="v5 (d=1)", node_type="vertex", x=80, y=160),
    ]

    diagram_edges = [
        DiagramEdge(source_id="v1", target_id="v2", label="(v1,v2)"),
        DiagramEdge(source_id="v1", target_id="v3", label="(v1,v3)"),
        DiagramEdge(source_id="v1", target_id="v4", label="(v1,v4)"),
        DiagramEdge(source_id="v3", target_id="v4", label="(v3,v4)"),
        DiagramEdge(source_id="v2", target_id="v5", label="(v2,v5)"),
    ]

    justifications = [
        DesignJustification(
            title="Περιορισμός Μέγιστου Βαθμού Απλού Γραφήματος",
            category="Graph Theory",
            description="Σε απλό γράφημα με n κορυφές, deg(v) <= n - 1 για κάθε v.",
            rationale="Εξηγεί γιατί βαθμοί 5 και 7 αποκλείουν την ύπαρξη απλού γραφήματος με 5 κορυφές.",
        ),
    ]

    solution_code = '''# Verification Script for Mock Exam 1 (Course 203)

# Q1 Verification:
u = set(range(1, 9))
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
comp_union = u - (a | b)  # {7, 8}

print("Mock Exam 1 - Question 1:")
print("Group A:", comp_union | (a & b))
print("Group B:", comp_union | (a - b))
print("Group C:", comp_union | (b - a))
print("Group D:", comp_union | (a ^ b))

# Q3 Verification:
def check_graph_degrees(degrees, n=5):
    if any(d > n - 1 for d in degrees):
        return False, "Degree exceeds n-1"
    if sum(degrees) % 2 != 0:
        return False, "Odd sum of degrees"
    return True, sum(degrees) // 2

print("\\nMock Exam 1 - Question 3:")
for grp, q_val in [("A", 1), ("B", 3), ("C", 5), ("D", 7)]:
    degs = [2, 2, 2, 3, q_val]
    exists, edges = check_graph_degrees(degs)
    print(f"Group {grp} (? = {q_val}): Exists = {exists}, Edges = {edges}")
'''

    return Scenario(
        id="mock_exam_1_easier",
        title="Εικονική Εξέταση 1 (Ευκολότερη)",
        subtitle="203: Διακριτά Μαθηματικά — Σύνολα, Πίνακες Αληθείας & Γραφήματα",
        course_tag="Εικονική Εξέταση",
        duration_info="3 Ώρες (10 Μονάδες)",
        paragraphs=paragraphs,
        questions=questions,
        diagram_nodes=diagram_nodes,
        diagram_edges=diagram_edges,
        justifications=justifications,
        solution_code=solution_code,
    )
