"""Midterm Exam 2025 Group B scenario module for Discrete Mathematics.

Transcribes the official midterm exam paper of 2025 (Group B) verbatim from the PDF,
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


def createMidtermExam2025GroupBScenario() -> Scenario:
    """Constructs the Scenario instance for the 2025 Midterm Exam (Group B).

    Returns:
        Scenario: Complete scenario with verbatim text, annotations, and worked solutions.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Τμήμα Πληροφορικής και Τηλεπικοινωνιών — Πανεπιστήμιο Ιωαννίνων\n"),
                TextSegment(text="Σπυρίδων Τζίμας • Εαρινό Εξάμηνο 2025\n"),
                TextSegment(text="203: Διακριτά Μαθηματικά — Εξέταση Προόδου: Ομάδα Β\n\n"),
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
            accent_border_color="var(--red-err)",
            segments=[
                TextSegment(text="Θέμα 1. (2.5 μονάδες) ", is_highlight=True, category="logic", tag_label="Q1-CONTRADICTION", badge_class="badge-logic", tooltip="Classification: Propositional Logic & Contradiction Proof\nDetection Clue: 'p ∧ (p → q) ∧ (q → r) ∧ ¬r... πίνακας αληθείας... απλούστερος τύπος'\nApplication Rationale: Requires constructing an 8-row truth table (all False) and formal equivalence proof to ⊥"),
                TextSegment(text="Δίνεται ο ακόλουθος προτασιακός τύπος: "),
                TextSegment(text="p ∧ (p → q) ∧ (q → r) ∧ ¬r\n\n"),
                TextSegment(text="α'. (1 μονάδα) Κατασκευάστε τον πίνακα αληθείας του και αναφέρετε αν είναι ταυτολογία ή αντίφαση.\n"),
                TextSegment(text="β'. (1.5 μονάδα) Βρείτε τον απλούστερο δυνατό ταυτολογικά ισοδύναμο προτασιακό τύπο κάνοντας χρήση των Κανόνων της Προτασιακής Λογικής."),
            ]
        ),
        Paragraph(
            accent_border_color="var(--blue-action)",
            segments=[
                TextSegment(text="Θέμα 2. (0.5 μονάδα) ", is_highlight=True, category="set", tag_label="Q2-SETS", badge_class="badge-set", tooltip="Classification: Inclusion-Exclusion Principle (2 Sets)\nDetection Clue: '169 άτομα... 121 εσωτερικής καύσης... 81 ηλεκτρικοί... υβριδικοί'\nApplication Rationale: Computes set intersection |H| = |C| + |E| - |U| = 121 + 81 - 169 = 33"),
                TextSegment(text="Σε μία δημοσκόπηση για το μέλλον της αυτοκίνησης συμμετείχαν 169 άτομα. "),
                TextSegment(text="Από αυτούς, οι 121 εξέφρασαν την άποψη ότι είναι οι κινητήρες εσωτερικής καύσης και οι 81 ότι είναι οι ηλεκτρικοί κινητήρες. "),
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
                TextSegment(text="Θέμα 4. (1 μονάδα) ", is_highlight=True, category="prob", tag_label="Q4-BAYES", badge_class="badge-prob", tooltip="Classification: Law of Total Probability & Bayes' Theorem\nDetection Clue: 'εργοστάσιο A 2000... εργοστάσιο B 8000... ελαττωματικά 10% και 5%'\nApplication Rationale: Solves prior production proportions (20%-80%), total defective rate (6%), and posterior probability P(B|Defective)"),
                TextSegment(text="Μία αυτοκινητοβιομηχανία πουλά αυτοκίνητα του μοντέλου M που κατασκευάζει σε δύο εργοστάσια, έστω A και B. "),
                TextSegment(text="Το εργοστάσιο A έχει ρυθμό παραγωγής 2000 αυτοκίνητα το μήνα και το B έχει 8000 αυτοκίνητα το μήνα. "),
                TextSegment(text="Έχει εκτιμηθεί πως το ποσοστό των αυτοκινήτων που κατασκευάζονται ελαττωματικά στο εργοστάσιο A είναι 10% και στο B είναι 5%.\n\n"),
                TextSegment(text="α'. (0.5 μονάδα) Υπολογίστε την πιθανότητα να αγοράσουμε αυτοκίνητο του μοντέλου M το οποίο είναι ελαττωματικό εκ κατασκευής.\n"),
                TextSegment(text="β'. (0.5 μονάδα) Δεδομένου ότι το αυτοκίνητο του μοντέλου M που αγοράσαμε είναι ελαττωματικό, υπολογίστε την πιθανότητα να κατασκευάστηκε στο εργοστάσιο B."),
            ]
        ),
    ]

    questions = [
        # QUESTION 1
        ExamQuestion(
            question_number=1,
            title="Προτασιακή Λογική: Αντίφαση & Απλοποίηση σε ⊥",
            question_type="Προτασιακή Λογική",
            prompt_text=(
                "Δίνεται ο ακόλουθος προτασιακός τύπος:\n"
                "$$p \\land (p \\to q) \\land (q \\to r) \\land \\neg r$$\n\n"
                "**α'. (1 μονάδα)** Κατασκευάστε τον πίνακα αληθείας του και αναφέρετε αν είναι ταυτολογία ή αντίφαση.\n\n"
                "**β'. (1.5 μονάδα)** Βρείτε τον απλούστερο δυνατό ταυτολογικά ισοδύναμο προτασιακό τύπο κάνοντας χρήση των Κανόνων της Προτασιακής Λογικής."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ερώτημα α' — Πίνακας Αληθείας (8 γραμμές)",
                    formula=r"P = p \land (p \to q) \land (q \to r), \quad Q = P \land \neg r",
                    substitution=(
                        r"\begin{array}{|c|c|c|c|c|c|c|c|c|} "
                        r"p & q & r & p \to q & p \land (p \to q) & q \to r & P & \neg r & Q \\ \hline "
                        r"T & T & T & T & T & T & T & F & \mathbf{F} \\ "
                        r"T & T & F & T & T & F & F & T & \mathbf{F} \\ "
                        r"T & F & T & F & F & T & F & F & \mathbf{F} \\ "
                        r"T & F & F & F & F & T & F & T & \mathbf{F} \\ "
                        r"F & T & T & T & F & T & F & F & \mathbf{F} \\ "
                        r"F & T & F & T & F & F & F & T & \mathbf{F} \\ "
                        r"F & F & T & T & F & T & F & F & \mathbf{F} \\ "
                        r"F & F & F & T & F & T & F & T & \mathbf{F} "
                        r"\end{array}"
                    ),
                    result=r"\text{Η στήλη } Q \text{ περιέχει αποκλειστικά } F \implies \mathbf{Αντίφαση (Contradiction)}",
                    rationale="Όλες οι γραμμές δίνουν τιμή F, καθώς η 1η γραμμή όπου P=T έχει ¬r=F, ενώ όλες οι υπόλοιπες γραμμές έχουν P=F.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ερώτημα β' — Τυπική Απλοποίηση με Κανόνες Λογικής",
                    formula=r"p \land (p \to q) \land (q \to r) \land \neg r",
                    substitution=(
                        r"\begin{aligned} "
                        r"& \equiv p \land (\neg p \lor q) \land (\neg q \lor r) \land \neg r && \text{Συνεπαγωγής} \\ "
                        r"& \equiv ((p \land \neg p) \lor (p \land q)) \land (\neg q \lor r) \land \neg r && \text{Επιμεριστικός} \\ "
                        r"& \equiv (\bot \lor (p \land q)) \land (\neg q \lor r) \land \neg r && \text{Συμπληρώματος} \\ "
                        r"& \equiv (p \land q) \land (\neg q \lor r) \land \neg r && \text{Απορροφητικός} \\ "
                        r"& \equiv p \land (q \land (\neg q \lor r)) \land \neg r && \text{Προσεταιριστικός} \\ "
                        r"& \equiv p \land ((q \land \neg q) \lor (q \land r)) \land \neg r && \text{Επιμεριστικός} \\ "
                        r"& \equiv p \land (\bot \lor (q \land r)) \land \neg r && \text{Συμπληρώματος} \\ "
                        r"& \equiv p \land q \land r \land \neg r && \text{Απορροφητικός} \\ "
                        r"& \equiv (p \land q) \land (r \land \neg r) && \text{Προσεταιριστικός} \\ "
                        r"& \equiv (p \land q) \land \bot && \text{Συμπληρώματος} \\ "
                        r"& \equiv \bot && \text{Απορροφητικός} "
                        r"\end{aligned}"
                    ),
                    result=r"\bot \text{ (Ψευδής)}",
                    rationale="Ο απλούστερος ταυτολογικά ισοδύναμος προτασιακός τύπος είναι το ⊥.",
                ),
            ],
            final_answer="α': Αντίφαση (πάντα F)\nβ': ⊥ (με πλήρη αναγραφή των 11 βημάτων κανόνων)",
            detailed_justification="Ο τύπος δηλώνει: p, αν p τότε q, αν q τότε r, αλλά όχι r. Αυτό είναι κλασική αντίφαση (reductio ad absurdum). Απλοποιείται σε (p ∧ q ∧ r) ∧ ¬r ≡ (p ∧ q) ∧ (r ∧ ¬r) ≡ (p ∧ q) ∧ ⊥ ≡ ⊥.",
            common_pitfalls=[
                "Σύγχυση μεταξύ ταυτολογίας και αντίφασης: Εδώ το συμπέρασμα δεν είναι συνεπαγωγή αλλά σύζευξη με το ¬r, άρα οδηγεί σε ⊥.",
            ],
            related_theory_topic="Προτασιακή Λογική & Κανόνες Ισοδυναμιών",
        ),

        # QUESTION 2
        ExamQuestion(
            question_number=2,
            title="Αρχή Εγκλεισμού-Αποκλεισμού (Δημοσκόπηση 169 ατόμων)",
            question_type="Θεωρία Συνόλων",
            prompt_text=(
                "Σε μία δημοσκόπηση για το μέλλον της αυτοκίνησης συμμετείχαν 169 άτομα.\n"
                "Από αυτούς, οι 121 εξέφρασαν την άποψη ότι είναι οι κινητήρες εσωτερικής καύσης (C) "
                "και οι 81 ότι είναι οι ηλεκτρικοί κινητήρες (E).\n\n"
                "Υπολογίστε πόσοι πιστεύουν στους υβριδικούς κινητήρες ($H = C \\cap E$), "
                "θεωρώντας ότι $U = C \\cup E$."
            ),
            given_parameters=[
                GivenParameter(symbol="|U|", value="169", description="Συνολικό σύμπαν συμμετεχόντων"),
                GivenParameter(symbol="|C|", value="121", description="Συμβατικοί κινητήρες εσωτερικής καύσης"),
                GivenParameter(symbol="|E|", value="81", description="Ηλεκτροκινητήρες"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Εφαρμογή Αρχής Εγκλεισμού-Αποκλεισμού για 2 Σύνολα",
                    formula=r"|U| = |C \cup E| = |C| + |E| - |C \cap E|",
                    substitution=r"169 = 121 + 81 - |H| \iff 169 = 202 - |H| \iff |H| = 202 - 169 = 33",
                    result=r"|H| = 33",
                    rationale="Υπολογίζουμε την τομή αφαιρώντας το σύμπαν από το άθροισμα των μονοσυνόλων.",
                ),
            ],
            final_answer="|H| = 33 συμμετέχοντες",
            detailed_justification="Με U = C ∪ E, η τομή υπολογίζεται άμεσα: |H| = 121 + 81 - 169 = 33.",
            common_pitfalls=[
                "Αριθμητικό λάθος στην αφαίρεση: 202 - 169 = 33.",
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
                "**β'. (0.5 μονάδα)** Αν πρέπει να τους διαχωρίσουμε σύμφωνα με το πρώτο γράμμα του επωνύμου τους σε δύο διαστήματα."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ερώτημα α' — Διαχωρισμός ανά Α.Μ. (Άρτιοι / Περιττοί)",
                    formula=r"P(n, k) = \frac{n!}{(n-k)!}",
                    substitution=r"n = 2 \text{ τμήματα (κουτιά)}, \ k = 2 \text{ μέρη (σφαιρίδια)}, \text{ χωρ. } \le 1 \implies P(2, 2) = 2",
                    result=r"P(2, 2) = 2",
                    rationale="Ακριβώς 2 δυνατές αναθέσεις των άρτιων/περιττών στα 2 διακεκριμένα τμήματα.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ερώτημα β' — Διαχωρισμός 24 γραμμάτων σε 2 διαστήματα",
                    formula=r"C(n+k-1, k) \times P(2, 2)",
                    substitution=r"C(2+24-1, 24) \times P(2, 2) = C(25, 24) \times 2 = 25 \times 2 = 50",
                    result=r"50 \text{ επιλογές}",
                    rationale="25 δυνατά μήκη διαστημάτων επί 2 αναθέσεις στα τμήματα.",
                ),
            ],
            final_answer="α': P(2, 2) = 2 επιλογές\nβ': C(25, 24) × P(2, 2) = 25 × 2 = 50 επιλογές",
            detailed_justification="Η δομή είναι ταυτόσημη με την Ομάδα Α, καθώς τα 24 γράμματα και τα 2 τμήματα παραμένουν αναλλοίωτα.",
            common_pitfalls=[
                "Ξέχασμα του πολλαπλασιαστή 2 για την ανάθεση των διαστημάτων στα τμήματα 1 και 2.",
            ],
            related_theory_topic="Συνδυαστική & Μοντέλο Σφαιρίδια-Κουτιά",
        ),

        # QUESTION 4
        ExamQuestion(
            question_number=4,
            title="Ολική Πιθανότητα & Θεώρημα Bayes (Εργοστάσιο B)",
            question_type="Πιθανότητες & Bayes",
            prompt_text=(
                "Μία αυτοκινητοβιομηχανία κατασκευάζει το μοντέλο M σε δύο εργοστάσια, A και B.\n"
                "- Εργοστάσιο A: παραγωγή 2000 αυτοκίνητα/μήνα, ποσοστό ελαττωματικών 10%\n"
                "- Εργοστάσιο B: παραγωγή 8000 αυτοκίνητα/μήνα, ποσοστό ελαττωματικών 5%\n\n"
                "**α'. (0.5 μονάδα)** Υπολογίστε την πιθανότητα $P(F)$ ένα τυχαίο αυτοκίνητο να είναι ελαττωματικό εκ κατασκευής.\n\n"
                "**β'. (0.5 μονάδα)** Δεδομένου ότι είναι ελαττωματικό, υπολογίστε την πιθανότητα $P(B \\mid F)$ να κατασκευάστηκε στο εργοστάσιο B."
            ),
            given_parameters=[
                GivenParameter(symbol="|A|, |B|", value="2000, 8000", description="Μηνιαία παραγωγή ανά εργοστάσιο"),
                GivenParameter(symbol="|U|", value="10000", description="Συνολική παραγωγή"),
                GivenParameter(symbol="P(F|A), P(F|B)", value="10%, 5%", description="Πιθανότητες ελαττώματος"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Υπολογισμός Εκ των Προτέρων Πιθανοτήτων",
                    formula=r"P(A) = \frac{|A|}{|U|}, \quad P(B) = \frac{|B|}{|U|}",
                    substitution=r"P(A) = \frac{2000}{10000} = 0.2 = 20\%, \quad P(B) = \frac{8000}{10000} = 0.8 = 80\%",
                    result=r"P(A) = 0.2, \quad P(B) = 0.8",
                    rationale="Το εργοστάσιο B παράγει το 80% των συνολικών αυτοκινήτων.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ερώτημα α' — Τύπος Ολικής Πιθανότητας",
                    formula=r"P(F) = P(F \mid A)P(A) + P(F \mid B)P(B)",
                    substitution=r"P(F) = 0.10 \times 0.20 + 0.05 \times 0.80 = 0.02 + 0.04 = 0.06 = 6\%",
                    result=r"P(F) = 0.06 \ (6\%)",
                    rationale="Η ολική πιθανότητα ελαττωματικού αυτοκινήτου είναι 6%.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Ερώτημα β' — Θεώρημα Bayes για P(B | F)",
                    formula=r"P(B \mid F) = \frac{P(F \mid B)P(B)}{P(F)}",
                    substitution=r"P(B \mid F) = \frac{0.05 \times 0.80}{0.06} = \frac{0.04}{0.06} = \frac{2}{3} = 0.\bar{6} \approx 66.66\%",
                    result=r"P(B \mid F) = 2/3 \approx 66.66\%",
                    rationale="Από τα 600 ελαττωματικά στα 10000 αυτοκίνητα, τα 400 προέρχονται από το B (400/600 = 2/3).",
                ),
            ],
            final_answer="α': P(F) = 6% (0.06)\nβ': P(B | F) = 2/3 ≈ 66.66%",
            detailed_justification="Το εργοστάσιο A παράγει 200 ελαττωματικά (2000 * 10%) και το B παράγει 400 ελαττωματικά (8000 * 5%). Σύνολο ελαττωματικών 600 στα 10000, άρα P(F) = 6%. Από τα 600 ελαττωματικά, τα 400 είναι από το B, άρα P(B|F) = 400/600 = 2/3 = 66.66%.",
            common_pitfalls=[
                "Προσοχή στην εκφώνηση: Στην Ομάδα B ζητείται το P(B | F) και όχι το P(A | F).",
            ],
            related_theory_topic="Θεώρημα Bayes & Ολική Πιθανότητα",
        ),
    ]

    diagram_nodes = [
        DiagramNode(id="U", label="Σύμπαν U (10000)", node_type="state", x=200, y=80),
        DiagramNode(id="A", label="Εργοστάσιο A (20%)", node_type="state", x=100, y=200),
        DiagramNode(id="B", label="Εργοστάσιο B (80%)", node_type="state", x=300, y=200),
        DiagramNode(id="FA", label="Ελαττωματικό A (10%)", node_type="state", x=100, y=290),
        DiagramNode(id="FB", label="Ελαττωματικό B (5%)", node_type="state", x=300, y=290),
    ]

    diagram_edges = [
        DiagramEdge(source_id="U", target_id="A", label="P(A)=0.2"),
        DiagramEdge(source_id="U", target_id="B", label="P(B)=0.8"),
        DiagramEdge(source_id="A", target_id="FA", label="P(F|A)=0.10", color="var(--red-err)"),
        DiagramEdge(source_id="B", target_id="FB", label="P(F|B)=0.05", color="var(--red-err)"),
    ]

    justifications = [
        DesignJustification(
            title="Απόδειξη Αντίφασης ⊥",
            category="Logic Rules",
            description="Ο τύπος καταλήγει στο ψευδές ⊥ λόγω της σύζευξης r ∧ ¬r ≡ ⊥.",
            rationale="Αποδεικνύει τυπικά ότι η ταυτόχρονη υπόθεση p ∧ (p→q) ∧ (q→r) και ¬r είναι ασυμβίβαστη.",
        ),
        DesignJustification(
            title="Στάθμιση Παραγωγής στο Bayes",
            category="Probability",
            description="Το εργοστάσιο B έχει χαμηλότερο ποσοστό ελαττωματικών (5% vs 10%), αλλά μεγαλύτερο όγκο παραγωγής (80% vs 20%).",
            rationale="Εξηγεί διαισθητικά γιατί ένα ελαττωματικό αυτοκίνητο είναι 2 φορές πιθανότερο να προήλθε από το B (2/3) παρά από το A (1/3).",
        ),
    ]

    solution_code = '''# Verification Script for 2025 Midterm Exam Group B (Course 203)

# Question 1: Truth Table verification for Contradiction
def verify_midterm_q1_group_b():
    for p in [True, False]:
        for q in [True, False]:
            for r in [True, False]:
                p_imp_q = (not p) or q
                q_imp_r = (not q) or r
                formula = p and p_imp_q and q_imp_r and (not r)
                assert formula is False, "Must be contradiction!"
    print("Midterm Q1 Group B: Verified 8/8 rows are FALSE (Contradiction ⊥)")

verify_midterm_q1_group_b()

# Question 2: Inclusion-Exclusion
u, c, e = 169, 121, 81
hybrid = c + e - u
print(f"Midterm Q2 Group B: Hybrid buyers = {hybrid} (Expected: 33)")
assert hybrid == 33

# Question 4: Bayes
p_a, p_b = 2000 / 10000, 8000 / 10000
p_f_given_a, p_f_given_b = 0.10, 0.05
p_f = p_f_given_a * p_a + p_f_given_b * p_b
p_b_given_f = (p_f_given_b * p_b) / p_f
print(f"Midterm Q4 Group B: Total Defective = {p_f*100:.1f}%, P(B|F) = {p_b_given_f:.4f} (2/3 = {2/3:.4f})")
assert abs(p_f - 0.06) < 1e-6
assert abs(p_b_given_f - 2/3) < 1e-6
'''

    return Scenario(
        id="midterm_exam_2025_group_b",
        title="Εξέταση Προόδου 2025 — Ομάδα Β",
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
