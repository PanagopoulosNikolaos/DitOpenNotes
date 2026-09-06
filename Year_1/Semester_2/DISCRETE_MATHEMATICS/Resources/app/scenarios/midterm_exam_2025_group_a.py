"""Midterm Exam 2025 Group A scenario module for Discrete Mathematics.

Transcribes the official midterm exam paper of 2025 (Group A) verbatim from the PDF,
and provides step-by-step master solutions for all 4 questions.
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


def createMidtermExam2025GroupAScenario() -> Scenario:
    """Constructs the Scenario instance for the 2025 Midterm Exam (Group A).

    Returns:
        Scenario: Complete scenario with verbatim text, annotations, and worked solutions.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Τμήμα Πληροφορικής και Τηλεπικοινωνιών — Πανεπιστήμιο Ιωαννίνων\n"),
                TextSegment(text="Σπυρίδων Τζίμας • Εαρινό Εξάμηνο 2025\n"),
                TextSegment(text="203: Διακριτά Μαθηματικά — Εξέταση Προόδου: Ομάδα Α\n\n"),
                TextSegment(text="Η βαθμολογική αξία της εξέτασης είναι "),
                TextSegment(
                    text="5 μονάδες",
                    is_highlight=True,
                    category="param",
                    tag_label="WEIGHT",
                    badge_class="badge-param",
                    tooltip="Classification: Exam grade weight\nDetection Clue: 'Η βαθμολογική αξία της εξέτασης είναι 5 μονάδες'\nApplication Rationale: Represents 50% of the midterm assessment framework",
                ),
                TextSegment(text=". Η χρονική διάρκεια είναι 1.5 ώρα. Επιτρέπεται στυλό μόνο μπλε και μαύρου χρώματος. Καλή Επιτυχία!"),
            ]
        ),
        Paragraph(
            accent_border_color="var(--amber)",
            segments=[
                TextSegment(text="Θέμα 1. (2.5 μονάδες) ", is_highlight=True, category="logic", tag_label="Q1-LOGIC", badge_class="badge-logic", tooltip="Classification: Propositional Logic & Algebraic Simplification\nDetection Clue: 'p ∧ (p → q) ∧ (q → r) → r... πίνακας αληθείας... απλούστερος τύπος'\nApplication Rationale: Requires constructing an 8-row truth table (tautology) and formal step-by-step equivalence proof to ⊤"),
                TextSegment(text="Δίνεται ο ακόλουθος προτασιακός τύπος: "),
                TextSegment(text="p ∧ (p → q) ∧ (q → r) → r\n\n"),
                TextSegment(text="α'. (1 μονάδα) Κατασκευάστε τον πίνακα αληθείας του και αναφέρετε αν είναι ταυτολογία ή αντίφαση.\n"),
                TextSegment(text="β'. (1.5 μονάδα) Βρείτε τον απλούστερο δυνατό ταυτολογικά ισοδύναμο προτασιακό τύπο κάνοντας χρήση των Κανόνων της Προτασιακής Λογικής."),
            ]
        ),
        Paragraph(
            accent_border_color="var(--blue-action)",
            segments=[
                TextSegment(text="Θέμα 2. (0.5 μονάδα) ", is_highlight=True, category="set", tag_label="Q2-SETS", badge_class="badge-set", tooltip="Classification: Inclusion-Exclusion Principle (2 Sets)\nDetection Clue: '144 άτομα... 100 εσωτερικής καύσης... 64 ηλεκτρικοί... υβριδικοί'\nApplication Rationale: Computes set intersection |H| = |C| + |E| - |U|"),
                TextSegment(text="Σε μία δημοσκόπηση για το μέλλον της αυτοκίνησης συμμετείχαν 144 άτομα. "),
                TextSegment(text="Από αυτούς, οι 100 εξέφρασαν την άποψη ότι είναι οι κινητήρες εσωτερικής καύσης και οι 64 ότι είναι οι ηλεκτρικοί κινητήρες. "),
                TextSegment(text="Υπολογίστε πόσοι από τους συμμετέχοντες πιστεύουν πώς το μέλλον της αυτοκίνησης είναι οι υβριδικοί κινητήρες που αποτελούν συνδυασμό κινητήρα εσωτερικής καύσης και ηλεκτρικού κινητήρα."),
            ]
        ),
        Paragraph(
            accent_border_color="var(--accent)",
            segments=[
                TextSegment(text="Θέμα 3. (1 μονάδα) ", is_highlight=True, category="prob", tag_label="Q3-BALLS-BOXES", badge_class="badge-prob", tooltip="Classification: Combinatorics / Balls-in-Boxes Model\nDetection Clue: 'μοντέλο σφαιρίδια-κουτιά... 2 τμήματα... άρτιοι/περιττοί... 24 γράμματα'\nApplication Rationale: Solves distribution of distinct items with capacity <= 1 and identical items into boxes"),
                TextSegment(text="Για την διεξαγωγή μίας εξέτασης του μαθήματος Διακριτά Μαθηματικά, επιθυμούμε να κατανείμουμε τους φοιτητές με δικαίωμα συμμετοχής σε 2 τμήματα. "),
                TextSegment(text="Απαριθμήστε όλες τις δυνατές επιλογές στις περιπτώσεις που ακολουθούν κάνοντας χρήση του μοντέλου σφαιρίδια-κουτιά.\n\n"),
                TextSegment(text="α'. (0.5 μονάδα) Αν πρέπει να τους διαχωρίσουμε σύμφωνα με τον αριθμό μητρώου τους σε άρτιους και περιττούς.\n"),
                TextSegment(text="β'. (0.5 μονάδα) Αν πρέπει να τους διαχωρίσουμε σύμφωνα με το πρώτο γράμμα του επωνύμου τους σε δύο διαστήματα (π.χ. «από Α έως Μ» και «από Ν έως Ω»)."),
            ]
        ),
        Paragraph(
            accent_border_color="var(--green-ok)",
            segments=[
                TextSegment(text="Θέμα 4. (1 μονάδα) ", is_highlight=True, category="prob", tag_label="Q4-BAYES", badge_class="badge-prob", tooltip="Classification: Law of Total Probability & Bayes' Theorem\nDetection Clue: 'εργοστάσιο A 4000... εργοστάσιο B 1000... ελαττωματικά 10% και 5%'\nApplication Rationale: Solves prior production proportions, total defective rate, and posterior probability P(A|Defective)"),
                TextSegment(text="Μία αυτοκινητοβιομηχανία πουλά αυτοκίνητα του μοντέλου M που κατασκευάζει σε δύο εργοστάσια, έστω A και B. "),
                TextSegment(text="Το εργοστάσιο A έχει ρυθμό παραγωγής 4000 αυτοκίνητα το μήνα και το B έχει 1000 αυτοκίνητα το μήνα. "),
                TextSegment(text="Έχει εκτιμηθεί πως το ποσοστό των αυτοκινήτων που κατασκευάζονται ελαττωματικά στο εργοστάσιο A είναι 10% και στο B είναι 5%.\n\n"),
                TextSegment(text="α'. (0.5 μονάδα) Υπολογίστε την πιθανότητα να αγοράσουμε αυτοκίνητο του μοντέλου M το οποίο είναι ελαττωματικό εκ κατασκευής.\n"),
                TextSegment(text="β'. (0.5 μονάδα) Δεδομένου ότι το αυτοκίνητο του μοντέλου M που αγοράσαμε είναι ελαττωματικό, υπολογίστε την πιθανότητα να κατασκευάστηκε στο εργοστάσιο A."),
            ]
        ),
    ]

    questions = [
        # QUESTION 1
        ExamQuestion(
            question_number=1,
            title="Προτασιακή Λογική: Ταυτολογία & Απλοποίηση με Κανόνες",
            question_type="Προτασιακή Λογική",
            prompt_text=(
                "Δίνεται ο ακόλουθος προτασιακός τύπος:\n"
                "$$p \\land (p \\to q) \\land (q \\to r) \\to r$$\n\n"
                "**α'. (1 μονάδα)** Κατασκευάστε τον πίνακα αληθείας του και αναφέρετε αν είναι ταυτολογία ή αντίφαση.\n\n"
                "**β'. (1.5 μονάδα)** Βρείτε τον απλούστερο δυνατό ταυτολογικά ισοδύναμο προτασιακό τύπο κάνοντας χρήση των Κανόνων της Προτασιακής Λογικής."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ερώτημα α' — Πίνακας Αληθείας (8 γραμμές)",
                    formula=r"P = p \land (p \to q) \land (q \to r), \quad Q = P \to r",
                    substitution=(
                        r"\begin{array}{|c|c|c|c|c|c|c|c|} "
                        r"p & q & r & p \to q & p \land (p \to q) & q \to r & P & Q \\ \hline "
                        r"T & T & T & T & T & T & T & \mathbf{T} \\ "
                        r"T & T & F & T & T & F & F & \mathbf{T} \\ "
                        r"T & F & T & F & F & T & F & \mathbf{T} \\ "
                        r"T & F & F & F & F & T & F & \mathbf{T} \\ "
                        r"F & T & T & T & F & T & F & \mathbf{T} \\ "
                        r"F & T & F & T & F & F & F & \mathbf{T} \\ "
                        r"F & F & T & T & F & T & F & \mathbf{T} \\ "
                        r"F & F & F & T & F & T & F & \mathbf{T} "
                        r"\end{array}"
                    ),
                    result=r"\text{Η στήλη } Q \text{ περιέχει αποκλειστικά } T \implies \mathbf{Ταυτολογία}",
                    rationale="Παρατηρούμε ότι το P είναι αληθές μόνο στην 1η γραμμή (T, T, T), όπου και το r είναι T (T -> T = T). Σε όλες τις άλλες γραμμές P = F, άρα F -> r = T.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ερώτημα β' — Τυπική Απλοποίηση με Κανόνες Λογικής",
                    formula=r"p \land (p \to q) \land (q \to r) \to r",
                    substitution=(
                        r"\begin{aligned} "
                        r"& \equiv p \land (\neg p \lor q) \land (\neg q \lor r) \to r && \text{Συνεπαγωγής} \\ "
                        r"& \equiv ((p \land \neg p) \lor (p \land q)) \land (\neg q \lor r) \to r && \text{Επιμεριστικός} \\ "
                        r"& \equiv (\bot \lor (p \land q)) \land (\neg q \lor r) \to r && \text{Συμπληρώματος} \\ "
                        r"& \equiv (p \land q) \land (\neg q \lor r) \to r && \text{Απορροφητικός} \\ "
                        r"& \equiv p \land (q \land (\neg q \lor r)) \to r && \text{Προσεταιριστικός} \\ "
                        r"& \equiv p \land ((q \land \neg q) \lor (q \land r)) \to r && \text{Επιμεριστικός} \\ "
                        r"& \equiv p \land (\bot \lor (q \land r)) \to r && \text{Συμπληρώματος} \\ "
                        r"& \equiv p \land q \land r \to r && \text{Απορροφητικός} \\ "
                        r"& \equiv \neg(p \land q \land r) \lor r && \text{Συνεπαγωγής} \\ "
                        r"& \equiv (\neg p \lor \neg q \lor \neg r) \lor r && \text{De Morgan} \\ "
                        r"& \equiv (\neg p \lor \neg q) \lor (\neg r \lor r) && \text{Προσεταιριστικός} \\ "
                        r"& \equiv (\neg p \lor \neg q) \lor \top && \text{Συμπληρώματος} \\ "
                        r"& \equiv \top && \text{Απορροφητικός} "
                        r"\end{aligned}"
                    ),
                    result=r"\top \text{ (Αληθής)}",
                    rationale="Ο απλούστερος ταυτολογικά ισοδύναμος προτασιακός τύπος είναι το ⊤.",
                ),
            ],
            final_answer="α': Ταυτολογία (πάντα T)\nβ': ⊤ (με πλήρη αναγραφή των 12 βημάτων κανόνων)",
            detailed_justification="Ο προτασιακός τύπος εκφράζει τον κλασικό κανόνα συμπερασμού Modus Ponens διαδοχικά (Hypothetical Syllogism). Με άλγεβρα Boole απλοποιείται σταδιακά σε p ∧ q ∧ r → r ≡ ¬(p ∧ q ∧ r) ∨ r ≡ ¬p ∨ ¬q ∨ (¬r ∨ r) ≡ ⊤.",
            common_pitfalls=[
                "Παράλειψη ονομάτων κανόνων: Στην εξέταση αφαιρούνται μόρια αν δεν αναγράφεται ο κανόνας δίπλα σε κάθε ισοδυναμία.",
                "Λάθος στον επιμεριστικό νόμο σύζευξης/διάζευξης.",
            ],
            related_theory_topic="Προτασιακή Λογική & Κανόνες Ισοδυναμιών",
        ),

        # QUESTION 2
        ExamQuestion(
            question_number=2,
            title="Αρχή Εγκλεισμού-Αποκλεισμού (Δημοσκόπηση Αυτοκίνησης)",
            question_type="Θεωρία Συνόλων",
            prompt_text=(
                "Σε μία δημοσκόπηση για το μέλλον της αυτοκίνησης συμμετείχαν 144 άτομα.\n"
                "Από αυτούς, οι 100 εξέφρασαν την άποψη ότι είναι οι κινητήρες εσωτερικής καύσης (C) "
                "και οι 64 ότι είναι οι ηλεκτρικοί κινητήρες (E).\n\n"
                "Υπολογίστε πόσοι πιστεύουν στους υβριδικούς κινητήρες ($H = C \\cap E$), "
                "θεωρώντας ότι $U = C \\cup E$."
            ),
            given_parameters=[
                GivenParameter(symbol="|U|", value="144", description="Συνολικό σύμπαν συμμετεχόντων"),
                GivenParameter(symbol="|C|", value="100", description="Συμβατικοί κινητήρες εσωτερικής καύσης"),
                GivenParameter(symbol="|E|", value="64", description="Ηλεκτροκινητήρες"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Εφαρμογή Αρχής Εγκλεισμού-Αποκλεισμού για 2 Σύνολα",
                    formula=r"|U| = |C \cup E| = |C| + |E| - |C \cap E|",
                    substitution=r"144 = 100 + 64 - |H| \iff 144 = 164 - |H| \iff |H| = 164 - 144 = 20",
                    result=r"|H| = 20",
                    rationale="Η τομή των δύο απόψεων αντιπροσωπεύει όσους επέλεξαν και τα δύο, δηλαδή τον συνδυασμό/υβριδικό κινητήρα.",
                ),
            ],
            final_answer="|H| = 20 συμμετέχοντες",
            detailed_justification="Θεωρώντας ότι κάθε συμμετέχων επέλεξε τουλάχιστον μία από τις δύο επιλογές (U = C ∪ E), έχουμε άμεσα |H| = |C| + |E| - |U| = 100 + 64 - 144 = 20.",
            common_pitfalls=[
                "Υπόθεση ότι υπάρχουν άτομα εκτός του C ∪ E: Η επίσημη λύση διευκρινίζει ότι θεωρούμε U = C ∪ E.",
            ],
            related_theory_topic="Θεωρία Συνόλων & Εγκλεισμός-Αποκλεισμός",
        ),

        # QUESTION 3
        ExamQuestion(
            question_number=3,
            title="Μοντέλο Σφαιρίδια-Κουτιά: Κατανομή Φοιτητών σε 2 Τμήματα",
            question_type="Συνδυαστική",
            prompt_text=(
                "Για την διεξαγωγή μίας εξέτασης του μαθήματος Διακριτά Μαθηματικά, επιθυμούμε να κατανείμουμε "
                "τους φοιτητές με δικαίωμα συμμετοχής σε $n = 2$ τμήματα.\n\n"
                "Απαριθμήστε όλες τις δυνατές επιλογές κάνοντας χρήση του μοντέλου σφαιρίδια-κουτιά:\n\n"
                "**α'. (0.5 μονάδα)** Αν πρέπει να τους διαχωρίσουμε σύμφωνα με τον αριθμό μητρώου τους σε άρτιους και περιττούς.\n\n"
                "**β'. (0.5 μονάδα)** Αν πρέπει να τους διαχωρίσουμε σύμφωνα με το πρώτο γράμμα του επωνύμου τους σε δύο διαστήματα (π.χ. «από Α έως Μ» και «από Ν έως Ω»)."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ερώτημα α' — Διαχωρισμός ανά Α.Μ. (Άρτιοι / Περιττοί)",
                    formula=r"P(n, k) = \frac{n!}{(n-k)!}",
                    substitution=r"n = 2 \text{ διακεκριμένα κουτιά (τμήματα)}, \ k = 2 \text{ διακεκριμένα σφαιρίδια (άρτιοι, περιττοί)}, \text{ χωρ. } \le 1 \implies P(2, 2) = \frac{2!}{0!} = 2",
                    result=r"P(2, 2) = 2 \text{ επιλογές}",
                    rationale="Τα 2 μέρη (άρτιοι, περιττοί) είναι διακεκριμένα και ανατίθενται στα 2 διακεκριμένα τμήματα (Τμήμα 1: Άρτιοι / Τμήμα 2: Περιττοί ή αντίστροφα).",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ερώτημα β' — Διαχωρισμός 24 γραμμάτων σε 2 διαστήματα",
                    formula=r"C(n+k-1, k) \times P(2, 2)",
                    substitution=(
                        r"\text{Βήμα 1 (Μήκη διαστημάτων): } n = 2 \text{ διαστήματα (κουτιά)}, \ k = 24 \text{ όμοια γράμματα}, \text{ άπειρη χωρ.} \implies C(2+24-1, 24) = C(25, 24) = 25. \\ "
                        r"\text{Βήμα 2 (Ανάθεση στα τμήματα): } P(2, 2) = 2. \\ "
                        r"\text{Κανόνας Γινομένου: } 25 \times 2 = 50."
                    ),
                    result=r"50 \text{ επιλογές}",
                    rationale="Το ποια είναι τα γράμματα καθορίζεται πλήρως από το μήκος του πρώτου διαστήματος. Τα 24 γράμματα συμπεριφέρονται ως k=24 όμοια αντικείμενα.",
                ),
            ],
            final_answer="α': P(2, 2) = 2 επιλογές\nβ': C(25, 24) × P(2, 2) = 25 × 2 = 50 επιλογές",
            detailed_justification="Η παρατήρηση-κλειδί στο ερώτημα β' είναι ότι η αλφαβητική σειρά είναι σταθερή. Αν γνωρίζουμε πόσα γράμματα περιέχει το πρώτο διάστημα (από 0 έως 24, δηλαδή 25 δυνατά μήκη), γνωρίζουμε αυτόματα και ποια είναι αυτά τα γράμματα.",
            common_pitfalls=[
                "Θεώρηση των γραμμάτων ως διακεκριμένων στο ερώτημα β': Αν θεωρηθούν διακεκριμένα, διαλύεται η απαίτηση για συνεχόμενα αλφαβητικά διαστήματα.",
                "Ξέχασμα του βήματος ανάθεσης των διαστημάτων στα 2 τμήματα (παράλειψη του × 2).",
            ],
            related_theory_topic="Συνδυαστική & Μοντέλο Σφαιρίδια-Κουτιά",
        ),

        # QUESTION 4
        ExamQuestion(
            question_number=4,
            title="Ολική Πιθανότητα & Θεώρημα Bayes (Ελαττωματικά Αυτοκίνητα)",
            question_type="Πιθανότητες & Bayes",
            prompt_text=(
                "Μία αυτοκινητοβιομηχανία κατασκευάζει το μοντέλο M σε δύο εργοστάσια, A και B.\n"
                "- Εργοστάσιο A: παραγωγή 4000 αυτοκίνητα/μήνα, ποσοστό ελαττωματικών 10%\n"
                "- Εργοστάσιο B: παραγωγή 1000 αυτοκίνητα/μήνα, ποσοστό ελαττωματικών 5%\n\n"
                "**α'. (0.5 μονάδα)** Υπολογίστε την πιθανότητα $P(F)$ ένα τυχαίο αυτοκίνητο να είναι ελαττωματικό εκ κατασκευής.\n\n"
                "**β'. (0.5 μονάδα)** Δεδομένου ότι είναι ελαττωματικό, υπολογίστε την πιθανότητα $P(A \\mid F)$ να κατασκευάστηκε στο εργοστάσιο A."
            ),
            given_parameters=[
                GivenParameter(symbol="|A|, |B|", value="4000, 1000", description="Μηνιαία παραγωγή ανά εργοστάσιο"),
                GivenParameter(symbol="|U|", value="5000", description="Συνολική παραγωγή"),
                GivenParameter(symbol="P(F|A), P(F|B)", value="10%, 5%", description="Πιθανότητες ελαττώματος"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Υπολογισμός Εκ των Προτέρων Πιθανοτήτων",
                    formula=r"P(A) = \frac{|A|}{|U|}, \quad P(B) = \frac{|B|}{|U|}",
                    substitution=r"P(A) = \frac{4000}{5000} = 0.8 = 80\%, \quad P(B) = \frac{1000}{5000} = 0.2 = 20\%",
                    result=r"P(A) = 0.8, \quad P(B) = 0.2",
                    rationale="Τα γεγονότα A και B αποτελούν διαμέριση του συνόλου των παραγόμενων αυτοκινήτων U.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ερώτημα α' — Τύπος Ολικής Πιθανότητας",
                    formula=r"P(F) = P(F \mid A)P(A) + P(F \mid B)P(B)",
                    substitution=r"P(F) = 0.10 \times 0.80 + 0.05 \times 0.20 = 0.08 + 0.01 = 0.09 = 9\%",
                    result=r"P(F) = 0.09 \ (9\%)",
                    rationale="Αθροίζουμε τη συνεισφορά των ελαττωματικών από το εργοστάσιο A και το B.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Ερώτημα β' — Θεώρημα Bayes για P(A | F)",
                    formula=r"P(A \mid F) = \frac{P(F \mid A)P(A)}{P(F)}",
                    substitution=r"P(A \mid F) = \frac{0.10 \times 0.80}{0.09} = \frac{0.08}{0.09} = \frac{8}{9} = 0.\bar{8} \approx 88.88\%",
                    result=r"P(A \mid F) = 8/9 \approx 88.88\%",
                    rationale="Το εργοστάσιο A παράγει 8 φορές περισσότερα ελαττωματικά αυτοκίνητα από το B (80 vs 10 ανά 1000).",
                ),
            ],
            final_answer="α': P(F) = 9% (0.09)\nβ': P(A | F) = 8/9 ≈ 88.88%",
            detailed_justification="Στο σύνολο των 5000 αυτοκινήτων, το εργοστάσιο A παράγει 4000 * 10% = 400 ελαττωματικά, ενώ το B παράγει 1000 * 5% = 50 ελαττωματικά. Σύνολο ελαττωματικών: 450 σε 5000, δηλαδή 450/5000 = 9%. Από αυτά τα 450, τα 400 προέρχονται από το A, άρα 400/450 = 8/9 = 88.88%.",
            common_pitfalls=[
                "Λανθασμένος υπολογισμός των εκ των προτέρων πιθανοτήτων: Θεώρηση P(A) = P(B) = 0.5 αντί για τη στάθμιση παραγωγής 80%-20%.",
            ],
            related_theory_topic="Θεώρημα Bayes & Ολική Πιθανότητα",
        ),
    ]

    diagram_nodes = [
        DiagramNode(id="U", label="Σύμπαν U (5000)", node_type="state", x=200, y=80),
        DiagramNode(id="A", label="Εργοστάσιο A (80%)", node_type="state", x=100, y=200),
        DiagramNode(id="B", label="Εργοστάσιο B (20%)", node_type="state", x=300, y=200),
        DiagramNode(id="FA", label="Ελαττωματικό A (10%)", node_type="state", x=100, y=290),
        DiagramNode(id="FB", label="Ελαττωματικό B (5%)", node_type="state", x=300, y=290),
    ]

    diagram_edges = [
        DiagramEdge(source_id="U", target_id="A", label="P(A)=0.8"),
        DiagramEdge(source_id="U", target_id="B", label="P(B)=0.2"),
        DiagramEdge(source_id="A", target_id="FA", label="P(F|A)=0.10", color="var(--red-err)"),
        DiagramEdge(source_id="B", target_id="FB", label="P(F|B)=0.05", color="var(--red-err)"),
    ]

    justifications = [
        DesignJustification(
            title="Αλγεβρική Απλοποίηση Προτασιακής Λογικής",
            category="Logic Rules",
            description="Η χρήση των επίσημων κανόνων μετατρέπει τη συνεπαγωγή σε tautology ⊤.",
            rationale="Απαλλάσσει από την ανάγκη μεγάλων πινάκων αληθείας και πιστοποιεί τη γνώση των αξιωμάτων Boole.",
        ),
        DesignJustification(
            title="Αναγωγή Διαστημάτων σε Stars and Bars",
            category="Combinatorics",
            description="Η διάταξη των γραμμάτων είναι προκαθορισμένη, άρα μετρούνται μόνο τα μήκη.",
            rationale="Ανάγει το πρόβλημα κατανομής γραμμάτων σε μη-αρνητικές ακέραιες λύσεις x1 + x2 = 24.",
        ),
    ]

    solution_code = '''# Verification Script for 2025 Midterm Exam Group A (Course 203)

# Question 1: Truth Table verification for Tautology
def verify_midterm_q1():
    for p in [True, False]:
        for q in [True, False]:
            for r in [True, False]:
                p_imp_q = (not p) or q
                q_imp_r = (not q) or r
                antecedent = p and p_imp_q and q_imp_r
                formula = (not antecedent) or r
                assert formula is True, "Must be tautology!"
    print("Midterm Q1: Verified 8/8 rows are TRUE (Tautology ⊤)")

verify_midterm_q1()

# Question 2: Inclusion-Exclusion
u, c, e = 144, 100, 64
hybrid = c + e - u
print(f"Midterm Q2: Hybrid buyers = {hybrid} (Expected: 20)")
assert hybrid == 20

# Question 3: Balls and Boxes
import math
ans_a = math.perm(2, 2)
ans_b = math.comb(2 + 24 - 1, 24) * math.perm(2, 2)
print(f"Midterm Q3: Part a = {ans_a}, Part b = {ans_b} (Expected: 2 and 50)")
assert ans_a == 2 and ans_b == 50

# Question 4: Bayes
p_a, p_b = 4000 / 5000, 1000 / 5000
p_f_given_a, p_f_given_b = 0.10, 0.05
p_f = p_f_given_a * p_a + p_f_given_b * p_b
p_a_given_f = (p_f_given_a * p_a) / p_f
print(f"Midterm Q4: Total Defective = {p_f*100:.1f}%, P(A|F) = {p_a_given_f:.4f} (8/9 = {8/9:.4f})")
assert abs(p_f - 0.09) < 1e-6
assert abs(p_a_given_f - 8/9) < 1e-6
'''

    return Scenario(
        id="midterm_exam_2025_group_a",
        title="Εξέταση Προόδου 2025 — Ομάδα Α",
        subtitle="203: Διακριτά Μαθηματικά — Εαρινό Εξάμηνο 2025 (Σπυρίδων Τζίμας)",
        course_tag="Εξέταση Προόδου",
        duration_info="1.5 Ώρα (5 Μονάδες)",
        paragraphs=paragraphs,
        questions=questions,
        diagram_nodes=diagram_nodes,
        diagram_edges=diagram_edges,
        justifications=justifications,
        solution_code=solution_code,
    )
