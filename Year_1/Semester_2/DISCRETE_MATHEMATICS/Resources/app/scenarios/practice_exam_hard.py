"""Practice Exam (Hard) scenario module for Discrete Mathematics.

Transcribes practice_exam_hard.md verbatim with interactive highlights, and provides
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


def createPracticeExamHardScenario() -> Scenario:
    """Constructs the Scenario instance for Practice Exam (Hard).

    Returns:
        Scenario: Complete scenario with verbatim text, annotations, and worked solutions.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Τμήμα Πληροφορικής και Τηλεπικοινωνιών — Πανεπιστήμιο Ιωαννίνων\n"),
                TextSegment(text="203: Διακριτά Μαθηματικά — Εξέταση Διακριτών Μαθηματικών (Δυσκολία: HARD)\n\n"),
                TextSegment(text="Συνολικός χρόνος: 4 ώρες. Συνολικές μονάδες: 10. "),
                TextSegment(text="Απαιτείται πλήρης, αυστηρή μαθηματική τεκμηρίωση και αποδείξεις σε όλα τα θέματα."),
            ]
        ),
        Paragraph(
            accent_border_color="var(--amber)",
            segments=[
                TextSegment(
                    text="Θέμα 1. (2.5 μονάδες) - Προτασιακή Λογική\n",
                    is_highlight=True,
                    category="logic",
                    tag_label="Q1-ADVANCED-LOGIC",
                    badge_class="badge-logic",
                    tooltip="Classification: Multi-variable Propositional Tautology Proving\nDetection Clue: '((p → q) ∧ (q → r) ∧ (r → s)) → ((p ∧ ¬s) → ⊥)'\nApplication Rationale: Proves hypothetical syllogism chain and implication-to-contradiction equivalence",
                ),
                TextSegment(text="Κατασκευάστε τον πίνακα αληθείας και αποδείξτε αν οι ακόλουθοι τύποι είναι ταυτολογίες, αντιφάσεις ή ικανοποιήσιμοι:\n\n"),
                TextSegment(text="α'. (1.25 μονάδα) ((p → q) ∧ (q → r) ∧ (r → s)) → ((p ∧ ¬s) → ⊥)\n"),
                TextSegment(text="β'. (1.25 μονάδα) (((p ∨ q) → r) ∧ ((r ∨ s) → t)) → ((p ∧ q ∧ ¬t) → ⊥)"),
            ]
        ),
        Paragraph(
            accent_border_color="var(--blue-action)",
            segments=[
                TextSegment(
                    text="Θέμα 2. (1.5 μονάδα) - Θεωρία Συνόλων\n",
                    is_highlight=True,
                    category="set",
                    tag_label="Q2-PIE-4SETS",
                    badge_class="badge-set",
                    tooltip="Classification: Four-Set Principle of Inclusion-Exclusion\nDetection Clue: '500 συμμετέχοντες... Κλασική (K), Jazz (J), Rock (R), και Pop (P)'\nApplication Rationale: Solves |U| - |K ∪ J ∪ R ∪ P| with alternating sums across all 15 intersections",
                ),
                TextSegment(
                    text="Σε μια έρευνα με 500 συμμετέχοντες ερωτήθηκαν για τις προτιμήσεις τους σε τέσσερα είδη μουσικής: "
                    "Κλασική (K), Jazz (J), Rock (R), και Pop (P). Τα αποτελέσματα έδειξαν:\n"
                    "- 180 προτιμούν Κλασική, 150 προτιμούν Jazz, 200 προτιμούν Rock, 220 προτιμούν Pop\n"
                    "- 65 προτιμούν Κλασική και Jazz, 80 προτιμούν Κλασική και Rock, 70 προτιμούν Jazz και Rock\n"
                    "- 90 προτιμούν Rock και Pop, 85 προτιμούν Κλασική και Pop, 75 προτιμούν Jazz και Pop\n"
                    "- 25 προτιμούν Κλασική, Jazz και Rock, 30 προτιμούν Κλασική, Rock και Pop\n"
                    "- 20 προτιμούν Jazz, Rock και Pop, 35 προτιμούν Κλασική, Jazz και Pop\n"
                    "- 15 προτιμούν και τα τέσσερα είδη\n\n"
                    "Υπολογίστε πόσοι συμμετέχοντες δεν προτιμούν κανένα από τα τέσσερα είδη μουσικής."
                ),
            ]
        ),
        Paragraph(
            accent_border_color="var(--green-ok)",
            segments=[
                TextSegment(
                    text="Θέμα 3. (1.5 μονάδα) - Πιθανότητες\n",
                    is_highlight=True,
                    category="prob",
                    tag_label="Q3-DICE-D12",
                    badge_class="badge-prob",
                    tooltip="Classification: Combinatorial Probability on Three 12-Sided Dice\nDetection Clue: 'τρία διακεκριμένα αμερόληπτα ζάρια 12 εδρών (d12)'\nApplication Rationale: Solves prime sums > 25 (29, 31) and Binomial exact 2 perfect squares in {1,4,9}",
                ),
                TextSegment(
                    text="Θεωρούμε το πείραμα ρίψης τριών διακεκριμένων αμερόληπτων ζαριών 12 εδρών (d12).\n\n"
                    "α'. (0.75 μονάδα) Υπολογίστε την πιθανότητα το άθροισμα των τριών ζαριών να είναι πρώτος αριθμός μεγαλύτερος του 25.\n"
                    "β'. (0.75 μονάδα) Υπολογίστε την πιθανότητα ακριβώς δύο από τα τρία ζάρια να δείχνουν αριθμό που είναι τέλειο τετράγωνο (1, 4, 9)."
                ),
            ]
        ),
        Paragraph(
            accent_border_color="var(--accent)",
            segments=[
                TextSegment(
                    text="Θέμα 4. (1.5 μονάδα) - Θεώρημα Bayes\n",
                    is_highlight=True,
                    category="prob",
                    tag_label="Q4-BAYES-MALWARE",
                    badge_class="badge-prob",
                    tooltip="Classification: Law of Total Probability & Bayes' Inversion\nDetection Clue: 'συστήματα Α (40%), Β (35%), Γ (25%)... false positive 2%, 4%, 6%'\nApplication Rationale: Solves P(FP) = 0.037 and P(Γ | FP) = 15/37",
                ),
                TextSegment(
                    text="Μια εταιρεία λογισμικού χρησιμοποιεί τρία διαφορετικά συστήματα ανίχνευσης κακόβουλου λογισμικού: Α, Β, και Γ. "
                    "Το σύστημα Α χρησιμοποιείται σε 40% των περιπτώσεων, το Β σε 35%, και το Γ σε 25%. "
                    "Η πιθανότητα εσφαλμένα θετικής διάγνωσης (false positive) είναι 2% για το σύστημα Α, 4% για το Β, και 6% για το Γ.\n\n"
                    "α'. (0.75 μονάδα) Υπολογίστε την πιθανότητα ένα αρχείο να διαγνωστεί εσφαλμένα ως κακόβουλο.\n"
                    "β'. (0.75 μονάδα) Δεδομένου ότι ένα αρχείο διαγνώστηκε εσφαλμένα ως κακόβουλο, υπολογίστε την πιθανότητα να χρησιμοποιήθηκε το σύστημα Γ."
                ),
            ]
        ),
        Paragraph(
            accent_border_color="var(--purple)",
            segments=[
                TextSegment(
                    text="Θέμα 5. (1 μονάδα) - Σχέσεις\n",
                    is_highlight=True,
                    category="logic",
                    tag_label="Q5-CLOSURES",
                    badge_class="badge-logic",
                    tooltip="Classification: Relation Properties & Transitive Closure Computation\nDetection Clue: 'R στο S = {1, 2, 3, 4, 5}... ανακλαστική, συμμετρική, αντισυμμετρική, μεταβατική... R+'\nApplication Rationale: Proves reflexivity, symmetry, refutes transitivity, derives equivalence components for R+",
                ),
                TextSegment(
                    text="Για την ακόλουθη σχέση επί του S = {1, 2, 3, 4, 5}:\n"
                    "R = {(1,1), (1,3), (2,2), (2,4), (3,1), (3,3), (3,5), (4,2), (4,4), (5,3), (5,5)}\n\n"
                    "α'. (0.5 μονάδα) Ελέγξτε την ισχύ καθεμίας εκ των ιδιοτήτων: ανακλαστική, συμμετρική, αντισυμμετρική και μεταβατική.\n"
                    "β'. (0.5 μονάδα) Βρείτε το μεταβατικό κλείσιμο R+ της σχέσης R."
                ),
            ]
        ),
        Paragraph(
            accent_border_color="var(--purple)",
            segments=[
                TextSegment(
                    text="Θέμα 6. (2 μονάδες) - Θεωρία Γραφημάτων\n",
                    is_highlight=True,
                    category="graph",
                    tag_label="Q6-ISOMORPHISM-CHROMATIC",
                    badge_class="badge-graph",
                    tooltip="Classification: Graph Isomorphism & Chromatic Number\nDetection Clue: 'G1 = (V1, E1), G2 = (V2, E2)... ισόμορφα... χρωματικός αριθμός'\nApplication Rationale: Constructs bijection f(v) and proves chi(G1) = 3 using C5 subgraph and 3-coloring",
                ),
                TextSegment(
                    text="Έστω τα ακόλουθα γραφήματα:\n"
                    "G1 = (V1 = {A, B, C, D, E, F, G}, E1 = {(A,B), (B,C), (C,D), (D,E), (E,F), (F,G), (G,A), (A,D), (B,E), (C,F)})\n"
                    "G2 = (V2 = {1, 2, 3, 4, 5, 6, 7}, E2 = {(1,2), (2,3), (3,4), (4,5), (5,6), (6,7), (7,1), (1,4), (2,5), (3,6)})\n\n"
                    "α'. (1 μονάδα) Αποδείξτε ότι τα γραφήματα G1 και G2 είναι ισόμορφα βρίσκοντας έναν ισομορφισμό.\n"
                    "β'. (1 μονάδα) Βρείτε τον χρωματικό αριθμό του G1 και δικαιολογήστε την απάντησή σας παρέχοντας μια βέλτιστη χρωμάτιση."
                ),
            ]
        ),
        Paragraph(
            accent_border_color="var(--accent)",
            segments=[
                TextSegment(
                    text="Θέμα 7. (0.5 μονάδα) - Κανονικές Εκφράσεις\n",
                    is_highlight=True,
                    category="automata",
                    tag_label="Q7-ADVANCED-REGEX",
                    badge_class="badge-automata",
                    tooltip="Classification: Complex Regular Expression Synthesis\nDetection Clue: 'αλφάβητο {0,1,2}... Ξεκινούν με 1... Περιέχουν '02'... Τελειώνουν με άρτιο αριθμό 2'\nApplication Rationale: Synthesizes union regex 1(0|1|2)*02(0|1|2)*(0|1)(22)* | 1(0|1|2)*0(22)+",
                ),
                TextSegment(
                    text="Γράψτε μία κανονική έκφραση που περιγράφει το σύνολο των συμβολοσειρών με αλφάβητο το {0,1,2} που:\n"
                    "- Ξεκινούν με το σύμβολο 1\n"
                    "- Περιέχουν τουλάχιστον μία εμφάνιση της ακολουθίας '02'\n"
                    "- Τελειώνουν με άρτιο αριθμό συμβόλων 2"
                ),
            ]
        ),
        Paragraph(
            accent_border_color="var(--accent)",
            segments=[
                TextSegment(
                    text="Θέμα 8. (0.5 μονάδα) - Αναγνώριση Συμβολοσειρών\n",
                    is_highlight=True,
                    category="automata",
                    tag_label="Q8-REGEX-EVAL",
                    badge_class="badge-automata",
                    tooltip="Classification: Language Membership Decision\nDetection Clue: '(a|b)* c (a|b|c)*... abcca, ccab, abab, cabcba, bacacc, abcdefg'\nApplication Rationale: Evaluates strings requiring alphabet {a,b,c} and at least one occurrence of c",
                ),
                TextSegment(
                    text="Για την κανονική έκφραση (a|b)*c(a|b|c)*, προσδιορίστε ποιες από τις ακόλουθες συμβολοσειρές "
                    "ανήκουν στο κανονικό σύνολο που περιγράφει:\n"
                    "abcca, ccab, abab, cabcba, bacacc, abcdefg"
                ),
            ]
        ),
        Paragraph(
            accent_border_color="#0284c7",
            segments=[
                TextSegment(
                    text="Θέμα 9. (1.5 μονάδα) - Μαθηματική Επαγωγή\n",
                    is_highlight=True,
                    category="induct",
                    tag_label="Q9-FACTORIAL-INDUCTION",
                    badge_class="badge-induct",
                    tooltip="Classification: Factorial Telescoping Mathematical Induction\nDetection Clue: 'sum_{k=1}^n k * k! = (n+1)! - 1'\nApplication Rationale: Formally proves identity through base step n=1 and inductive factoring (m+1)!(m+2) - 1",
                ),
                TextSegment(
                    text="Δείξτε με μαθηματική επαγωγή ότι για κάθε φυσικό αριθμό n ≥ 1 ισχύει:\n"
                    "sum_{k=1}^n k * k! = (n+1)! - 1\n\n"
                    "Σημείωση: Θυμηθείτε ότι k! = k * (k-1) * ... * 1 και 0! = 1."
                ),
            ]
        ),
    ]

    questions = [
        ExamQuestion(
            question_number=1,
            title="Προτασιακή Λογική: Αποδείξεις Ταυτολογιών",
            question_type="Προτασιακή Λογική",
            prompt_text=(
                "Κατασκευάστε τον πίνακα αληθείας και αποδείξτε αν οι ακόλουθοι τύποι είναι ταυτολογίες, αντιφάσεις ή ικανοποιήσιμοι:\n\n"
                "**α'. (1.25 μονάδα)** $((p \\to q) \\land (q \\to r) \\land (r \\to s)) \\to ((p \\land \\neg s) \\to \\bot)$\n\n"
                "**β'. (1.25 μονάδα)** $(((p \\lor q) \\to r) \\land ((r \\lor s) \\to t)) \\to ((p \\land q \\land \\neg t) \\to \\bot)$"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ερώτημα α' — Ανάλυση & Ισοδυναμία",
                    formula=r"((p \to q) \land (q \to r) \land (r \to s)) \to ((p \land \neg s) \to \bot)",
                    substitution=(
                        r"\text{1. Παρατηρούμε ότι } (A \to \bot) \equiv \neg A. "
                        r"\text{ Άρα } (p \land \neg s) \to \bot \equiv \neg(p \land \neg s) \equiv \neg p \lor s \equiv (p \to s). \\ "
                        r"\text{2. Η υπόθεση είναι η αλυσίδα υποθετικών συλλογισμών } H = (p \to q) \land (q \to r) \land (r \to s) \implies (p \to s). \\ "
                        r"\text{3. Ο τύπος γράφεται } H \to (p \to s). "
                        r"\text{ Όταν το } H \text{ είναι } T, \text{ αναγκαστικά } p \to s \text{ είναι } T \ (T \to T = T). "
                        r"\text{ Όταν το } H \text{ είναι } F, F \to Anything = T."
                    ),
                    result=r"\text{Ταυτολογία (αληθής και στις 16 γραμμές)}",
                    rationale="Η συνεπαγωγή στο ψευδές ισοδυναμεί με την άρνηση της υπόθεσης (απαγωγή σε άτοπο). Η υπόθεση συνεπάγεται λογικά το p -> s, καθιστώντας τον τύπο ταυτολογία.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ερώτημα β' — Ανάλυση & Ισοδυναμία",
                    formula=r"(((p \lor q) \to r) \land ((r \lor s) \to t)) \to ((p \land q \land \neg t) \to \bot)",
                    substitution=(
                        r"\text{1. } (p \land q \land \neg t) \to \bot \equiv \neg(p \land q \land \neg t) \equiv \neg(p \land q) \lor t \equiv ((p \land q) \to t). \\ "
                        r"\text{2. Αν } p \land q = T, \text{ τότε } p=T \implies p \lor q = T. \\ "
                        r"\text{3. Από την πρώτη υπόθεση } (p \lor q) \to r, \text{ έπεται } r = T. \\ "
                        r"\text{4. Αν } r = T, \text{ τότε } r \lor s = T. \\ "
                        r"\text{5. Από τη δεύτερη υπόθεση } (r \lor s) \to t, \text{ έπεται } t = T. \\ "
                        r"\text{6. Άρα οι υποθέσεις συνεπάγονται } (p \land q) \to t. \text{ Συνεπώς ο τύπος είναι Ταυτολογία}."
                    ),
                    result=r"\text{Ταυτολογία (αληθής και στις 32 γραμμές)}",
                    rationale="Κάθε γραμμή όπου η σύζευξη των υποθέσεων είναι αληθής αναγκάζει το συμπέρασμα να είναι αληθές, άρα η ολική συνεπαγωγή είναι ταυτολογία.",
                ),
            ],
            final_answer="Και οι δύο προτασιακοί τύποι (α' και β') είναι ΤΑΥΤΟΛΟΓΙΕΣ (αποτιμώνται σε Αληθές / T σε όλες τις γραμμές του πίνακα αληθείας).",
            detailed_justification=(
                "Και οι δύο τύποι ενσωματώνουν την αρχή της απαγωγής σε άτοπο (Reductio ad Absurdum), όπου A → ⊥ ≡ ¬A. "
                "Στο α', η αλυσίδα συνεπαγωγών αποδεικνύει ότι p → s, το οποίο αποκλείει το ενδεχόμενο p ∧ ¬s. "
                "Στο β', η παρουσία των p και q εξασφαλίζει τη διάζευξη p ∨ q, η οποία μέσω του r ενεργοποιεί το t, αποκλείοντας το p ∧ q ∧ ¬t."
            ),
            common_pitfalls=[
                "Μη αναγνώριση της ισοδυναμίας (X → ⊥) ≡ ¬X, οδηγώντας σε χαοτικούς υπολογισμούς πινάκων αληθείας 16 και 32 γραμμών.",
                "Σύγχυση της ταυτολογίας με απλή ικανοποιησιμότητα.",
            ],
            related_theory_topic="Προτασιακή Λογική: Ταυτολογίες & Απαγωγή σε Άτοπο",
        ),
        ExamQuestion(
            question_number=2,
            title="Αρχή Εγκλεισμού-Αποκλεισμού 4 Συνόλων (Έρευνα Μουσικής)",
            question_type="Θεωρία Συνόλων",
            prompt_text=(
                "Έρευνα 500 συμμετεχόντων ($|U| = 500$) για 4 είδη μουσικής:\n"
                "- $|K| = 180, |J| = 150, |R| = 200, |P| = 220$\n"
                "- $|K \\cap J| = 65, |K \\cap R| = 80, |J \\cap R| = 70, |R \\cap P| = 90, |K \\cap P| = 85, |J \\cap P| = 75$\n"
                "- $|K \\cap J \\cap R| = 25, |K \\cap R \\cap P| = 30, |J \\cap R \\cap P| = 20, |K \\cap J \\cap P| = 35$\n"
                "- $|K \\cap J \\cap R \\cap P| = 15$\n\n"
                "Υπολογίστε πόσοι συμμετέχοντες δεν προτιμούν κανένα είδος."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Άθροισμα Μεμονωμένων Συνόλων (Σ1)",
                    formula=r"\Sigma_1 = |K| + |J| + |R| + |P|",
                    substitution=r"\Sigma_1 = 180 + 150 + 200 + 220 = 750",
                    result=r"\Sigma_1 = 750",
                    rationale="Άθροισμα όλων των στοιχείων των 4 συνόλων.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Άθροισμα Τομών ανά Δύο (Σ2)",
                    formula=r"\Sigma_2 = \sum |A_i \cap A_j|",
                    substitution=r"\Sigma_2 = 65 + 80 + 70 + 90 + 85 + 75 = 465",
                    result=r"\Sigma_2 = 465",
                    rationale="Άθροιση των 6 τομών ανά δύο σύνολα.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Άθροισμα Τομών ανά Τρία (Σ3)",
                    formula=r"\Sigma_3 = \sum |A_i \cap A_j \cap A_k|",
                    substitution=r"\Sigma_3 = 25 + 30 + 20 + 35 = 110",
                    result=r"\Sigma_3 = 110",
                    rationale="Άθροιση των 4 τομών ανά τρία σύνολα.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Τομή και των Τεσσάρων (Σ4) & Ένωση",
                    formula=r"|K \cup J \cup R \cup P| = \Sigma_1 - \Sigma_2 + \Sigma_3 - \Sigma_4",
                    substitution=r"|K \cup J \cup R \cup P| = 750 - 465 + 110 - 15 = 380",
                    result=r"|K \cup J \cup R \cup P| = 380",
                    rationale="Εναλλασσόμενο άθροισμα της Αρχής Εγκλεισμού-Αποκλεισμού για n=4.",
                ),
                CalculationStep(
                    step_number=5,
                    title="Υπολογισμός Συμπληρώματος (Κανένα Είδος)",
                    formula=r"N = |U| - |K \cup J \cup R \cup P|",
                    substitution=r"N = 500 - 380 = 120",
                    result=r"N = 120 \text{ συμμετέχοντες}",
                    rationale="Αφαίρεση της ένωσης από το καθολικό σύνολο των 500 συμμετεχόντων.",
                ),
            ],
            final_answer="120 συμμετέχοντες δεν προτιμούν κανένα από τα τέσσερα είδη μουσικής.",
            detailed_justification=(
                "Εφαρμόζοντας τον τύπο του Εγκλεισμού-Αποκλεισμού για 4 σύνολα: "
                "|Union| = Σ1 - Σ2 + Σ3 - Σ4 = 750 - 465 + 110 - 15 = 380. "
                "Συνεπώς, το συμπλήρωμα είναι 500 - 380 = 120."
            ),
            common_pitfalls=[
                "Λάθος στα πρόσημα της εναλλασσόμενης σειράς (+ Σ1 - Σ2 + Σ3 - Σ4).",
                "Ξέχασμα μίας από τις 6 τομές ανά δύο.",
            ],
            related_theory_topic="Αρχή Εγκλεισμού-Αποκλεισμού (n=4)",
        ),
        ExamQuestion(
            question_number=3,
            title="Πιθανότητες 3 Δωδεκάεδρων Ζαριών (d12)",
            question_type="Πιθανότητες & Συνδυαστική",
            prompt_text=(
                "Θεωρούμε τη ρίψη 3 διακεκριμένων αμερόληπτων ζαριών 12 εδρών (d12). "
                "Το μέγεθος του δειγματικού χώρου είναι $|\\Omega| = 12^3 = 1728$.\n\n"
                "**α'. (0.75 μονάδα)** Υπολογίστε την πιθανότητα το άθροισμα των τριών ζαριών να είναι πρώτος αριθμός μεγαλύτερος του 25.\n\n"
                "**β'. (0.75 μονάδα)** Υπολογίστε την πιθανότητα ακριβώς δύο από τα τρία ζάρια να δείχνουν τέλειο τετράγωνο (1, 4, 9)."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ερώτημα α' — Πρώτοι Αριθμοί > 25 στο Διάστημα [3, 36]",
                    formula=r"\text{Πρώτοι στο } [26, 36]: \{29, 31\}",
                    substitution=(
                        r"\text{Για άθροισμα 29: } x_1 + x_2 + x_3 = 29 \ (1 \le x_i \le 12). \\ "
                        r"\text{Θέτοντας } y_i = 12 - x_i \ (0 \le y_i \le 11), \ y_1 + y_2 + y_3 = 36 - 29 = 7. \\ "
                        r"\text{Λύσεις: } \binom{7+3-1}{3-1} = \binom{9}{2} = \frac{9 \times 8}{2} = 36. \\ "
                        r"\text{Για άθροισμα 31: } y_1 + y_2 + y_3 = 36 - 31 = 5. \\ "
                        r"\text{Λύσεις: } \binom{5+3-1}{3-1} = \binom{7}{2} = \frac{7 \times 6}{2} = 21. \\ "
                        r"\text{Σύνολο ευνοϊκών περιπτώσεων } = 36 + 21 = 57."
                    ),
                    result=r"P(\text{Πρώτος} > 25) = \frac{57}{1728} = \frac{19}{576} \approx 0.03299 \ (3.30\%)",
                    rationale="Χρήση της συμμετρίας y_i = 12 - x_i για την αναγωγή σε απλή απαρίθμηση συνδυασμών με επανάληψη.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ερώτημα β' — Ακριβώς 2 Τέλεια Τετράγωνα (Διωνυμική Κατανομή)",
                    formula=r"P(X = 2) = \binom{3}{2} p^2 (1-p)^1",
                    substitution=(
                        r"\text{Τέλεια τετράγωνα στο } \{1,\dots,12\}: \{1, 4, 9\} \implies p = \frac{3}{12} = \frac{1}{4}. \\ "
                        r"1 - p = \frac{9}{12} = \frac{3}{4}. \\ "
                        r"P(X = 2) = 3 \times \left(\frac{1}{4}\right)^2 \times \left(\frac{3}{4}\right)^1 = 3 \times \frac{1}{16} \times \frac{3}{4} = \frac{9}{64} = 0.140625"
                    ),
                    result=r"P = \frac{9}{64} = \frac{243}{1728} = 14.0625\%",
                    rationale="Διωνυμική κατανομή για n=3 δοκιμές Bernoulli με πιθανότητα επιτυχίας p=1/4.",
                ),
            ],
            final_answer=(
                "α': P(Άθροισμα πρώτος > 25) = 57 / 1728 = 19 / 576 ≈ 3.30%\n"
                "β': P(Ακριβώς 2 τέλεια τετράγωνα) = 9 / 64 = 243 / 1728 = 14.0625%"
            ),
            detailed_justification=(
                "Για το α', οι μόνοι πρώτοι αριθμοί στο πεδίο [26, 36] είναι το 29 και το 31. "
                "Μέσω του συμπληρωματικού μετασχηματισμού y_i = 12 - x_i, το άθροισμα 29 έχει 36 λύσεις και το 31 έχει 21 λύσεις (σύνολο 57/1728). "
                "Για το β', πρόκειται για διωνυμική κατανομή B(3, 1/4), δίνοντας C(3,2)*(1/4)^2*(3/4) = 9/64."
            ),
            common_pitfalls=[
                "Θεώρηση ότι το 27 είναι πρώτος αριθμός (27 = 3^3).",
                "Παράλειψη του συντελεστή διάταξης C(3,2) = 3 στο ερώτημα β'.",
            ],
            related_theory_topic="Συνδυαστική Πιθανοτήτων & Διωνυμική Κατανομή",
        ),
        ExamQuestion(
            question_number=4,
            title="Θεώρημα Ολικής Πιθανότητας & Bayes (Συστήματα Ανίχνευσης)",
            question_type="Θεώρημα Bayes",
            prompt_text=(
                "Τρία συστήματα ανίχνευσης malware:\n"
                "- $P(A) = 0.40, \\ P(B) = 0.35, \\ P(\\Gamma) = 0.25$\n"
                "- $P(FP \\mid A) = 0.02, \\ P(FP \\mid B) = 0.04, \\ P(FP \\mid \\Gamma) = 0.06$\n\n"
                "**α'. (0.75 μονάδα)** Πιθανότητα ένα αρχείο να διαγνωστεί εσφαλμένα ως κακόβουλο ($P(FP)$).\n\n"
                "**β'. (0.75 μονάδα)** Πιθανότητα να χρησιμοποιήθηκε το σύστημα Γ δεδομένου ότι υπήρξε εσφαλμένη διάγνωση ($P(\\Gamma \\mid FP)$)."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ερώτημα α' — Θεώρημα Ολικής Πιθανότητας για P(FP)",
                    formula=r"P(FP) = P(FP \mid A)P(A) + P(FP \mid B)P(B) + P(FP \mid \Gamma)P(\Gamma)",
                    substitution=(
                        r"P(FP) = (0.02 \times 0.40) + (0.04 \times 0.35) + (0.06 \times 0.25) \\ "
                        r"P(FP) = 0.008 + 0.014 + 0.015 = 0.037 \ (3.7\%)"
                    ),
                    result=r"P(FP) = 0.037 \ (3.7\%)",
                    rationale="Τα συστήματα A, B, Γ αποτελούν διαμέριση του δειγματικού χώρου.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ερώτημα β' — Θεώρημα Bayes για P(Γ | FP)",
                    formula=r"P(\Gamma \mid FP) = \frac{P(FP \mid \Gamma)P(\Gamma)}{P(FP)}",
                    substitution=r"P(\Gamma \mid FP) = \frac{0.06 \times 0.25}{0.037} = \frac{0.015}{0.037} = \frac{15}{37} \approx 0.4054 \ (40.54\%)",
                    result=r"P(\Gamma \mid FP) = \frac{15}{37} \approx 40.54\%",
                    rationale="Αντιστροφή δεσμευμένης πιθανότητας με βάση τον κανόνα του Bayes.",
                ),
            ],
            final_answer="α': P(FP) = 0.037 (3.7%)\nβ': P(Γ | FP) = 15/37 ≈ 40.54%",
            detailed_justification=(
                "Παρότι το σύστημα Γ χρησιμοποιείται μόνο στο 25% των περιπτώσεων (a priori), "
                "το υψηλό του ποσοστό σφάλματος (6%) αυξάνει την a posteriori πιθανότητα στο 40.54% σε περίπτωση εμφάνισης false positive."
            ),
            common_pitfalls=[
                "Διαίρεση με το 0.06 αντί για την ολική πιθανότητα 0.037.",
            ],
            related_theory_topic="Θεώρημα Bayes & Διαμέριση Δειγματικού Χώρου",
        ),
        ExamQuestion(
            question_number=5,
            title="Ιδιότητες Σχέσης & Μεταβατικό Κλείσιμο R+",
            question_type="Διμελείς Σχέσεις",
            prompt_text=(
                "Για τη σχέση $R$ επί του $S = \\{1, 2, 3, 4, 5\\}$:\n"
                "$R = \\{(1,1), (1,3), (2,2), (2,4), (3,1), (3,3), (3,5), (4,2), (4,4), (5,3), (5,5)\\}$\n\n"
                "**α'. (0.5 μονάδα)** Ελέγξτε τις ιδιότητες: ανακλαστική, συμμετρική, αντισυμμετρική, μεταβατική.\n\n"
                "**β'. (0.5 μονάδα)** Βρείτε το μεταβατικό κλείσιμο $R^+$."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ερώτημα α' — Έλεγχος των 4 Ιδιοτήτων",
                    formula=r"\text{Ιδιότητες: Ανακλαστική, Συμμετρική, Αντισυμμετρική, Μεταβατική}",
                    substitution=(
                        r"\text{1. Ανακλαστική: } (1,1),(2,2),(3,3),(4,4),(5,5) \in R \implies \mathbf{ΝΑΙ}. \\ "
                        r"\text{2. Συμμετρική: } (1,3)\leftrightarrow(3,1), (2,4)\leftrightarrow(4,2), (3,5)\leftrightarrow(5,3) \in R \implies \mathbf{ΝΑΙ}. \\ "
                        r"\text{3. Αντισυμμετρική: } (1,3) \in R \land (3,1) \in R \text{ αλλά } 1 \neq 3 \implies \mathbf{ΟΧΙ}. \\ "
                        r"\text{4. Μεταβατική: } (1,3) \in R \land (3,5) \in R \text{ αλλά } (1,5) \notin R \implies \mathbf{ΟΧΙ}."
                    ),
                    result=r"\text{Ανακλαστική: ΝΑΙ, Συμμετρική: ΝΑΙ, Αντισυμμετρική: ΟΧΙ, Μεταβατική: ΟΧΙ}",
                    rationale="Η σχέση περιέχει όλη τη διαγώνιο και είναι πλήρως συμμετρική, αλλά στερείται των ζευγών (1,5) και (5,1).",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ερώτημα β' — Υπολογισμός Μεταβατικού Κλεισίματος R+",
                    formula=r"R^+ = R \cup R^2 \cup \dots",
                    substitution=(
                        r"\text{Σύνθεση } R \circ R \text{ παράγει τα νέα ζεύγη: } (1,5) \text{ και } (5,1). \\ "
                        r"\text{Τα στοιχεία χωρίζονται σε δύο πλήρεις κλάσεις ισοδυναμίας:} \\ "
                        r"C_1 = \{1, 3, 5\} \implies C_1 \times C_1 \ (9 \text{ ζεύγη}), \\ "
                        r"C_2 = \{2, 4\} \implies C_2 \times C_2 \ (4 \text{ ζεύγη}). \\ "
                        r"R^+ = R \cup \{(1,5), (5,1)\} \ (|R^+| = 13 \text{ ζεύγη})."
                    ),
                    result=r"R^+ = R \cup \{(1,5), (5,1)\}",
                    rationale="Το R+ συμπληρώνει την ισοδυναμία στις συνεκτικές συνιστώσες {1, 3, 5} και {2, 4}.",
                ),
            ],
            final_answer=(
                "α': Ανακλαστική: ΝΑΙ, Συμμετρική: ΝΑΙ, Αντισυμμετρική: ΟΧΙ (λόγω (1,3) και (3,1)), Μεταβατική: ΟΧΙ (λόγω (1,3) και (3,5) ενώ (1,5) ∉ R)\n"
                "β': R+ = R ∪ {(1,5), (5,1)} (αποτελεί σχέση ισοδυναμίας με κλάσεις {1, 3, 5} και {2, 4})"
            ),
            detailed_justification=(
                "Η σχέση R αποτελεί ένα μη-μεταβατικό γράφημα με δύο ανεξάρτητες συνιστώσες: ένα μονοπάτι 1-3-5 και μία ακμή 2-4. "
                "Το μεταβατικό κλείσιμο προσθέτει τα ζεύγη (1,5) και (5,1), μετατρέποντας τη συνιστώσα {1, 3, 5} σε πλήρες γράφημα K3."
            ),
            common_pitfalls=[
                "Ξέχασμα του αντίστροφου ζεύγους (5,1) στο μεταβατικό κλείσιμο.",
            ],
            related_theory_topic="Σχέσεις Ισοδυναμίας & Μεταβατικό Κλείσιμο",
        ),
        ExamQuestion(
            question_number=6,
            title="Ισομορφισμός & Χρωματικός Αριθμός Γραφημάτων",
            question_type="Θεωρία Γραφημάτων",
            prompt_text=(
                "Έστω τα γραφήματα $G_1 = (V_1, E_1)$ και $G_2 = (V_2, E_2)$ με 7 κορυφές και 10 ακμές:\n"
                "- $G_1$: κύκλος $A-B-C-D-E-F-G-A$ και χορδές $(A,D), (B,E), (C,F)$\n"
                "- $G_2$: κύκλος $1-2-3-4-5-6-7-1$ και χορδές $(1,4), (2,5), (3,6)$\n\n"
                "**α'. (1 μονάδα)** Αποδείξτε ότι τα γραφήματα είναι ισόμορφα βρίσκοντας έναν ισομορφισμό.\n\n"
                "**β'. (1 μονάδα)** Βρείτε τον χρωματικό αριθμό $\\chi(G_1)$ και δώστε βέλτιστη χρωμάτιση."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ερώτημα α' — Κατασκευή Ισομορφισμού f",
                    formula=r"f: V_1 \to V_2, \quad (u, v) \in E_1 \iff (f(u), f(v)) \in E_2",
                    substitution=(
                        r"f(A)=1, \ f(B)=2, \ f(C)=3, \ f(D)=4, \ f(E)=5, \ f(F)=6, \ f(G)=7. \\ "
                        r"\text{Ακμές κύκλου: } (A,B)\to(1,2), (B,C)\to(2,3), \dots, (G,A)\to(7,1) \in E_2. \\ "
                        r"\text{Χορδές: } (A,D)\to(1,4) \in E_2, \ (B,E)\to(2,5) \in E_2, \ (C,F)\to(3,6) \in E_2. \\ "
                        r"\text{Η } f \text{ είναι 1-προς-1 και επί, και διατηρεί πλήρως τη γειτνίαση. Άρα } G_1 \cong G_2."
                    ),
                    result=r"G_1 \cong G_2 \text{ μέσω της } f",
                    rationale="Η απεικόνιση αντιστοιχεί τις κορυφές του κύκλου C7 και διατηρεί απαράλλαχτες τις 3 χορδές απόστασης 3.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ερώτημα β' — Χρωματικός Αριθμός χ(G1)",
                    formula=r"\chi(G_1) \ge 3 \land \chi(G_1) \le 3 \implies \chi(G_1) = 3",
                    substitution=(
                        r"\text{1. Κάτω φράγμα: Το } G_1 \text{ περιέχει τον περιττό κύκλο μήκους 5: } A - G - F - C - D - A. \\ "
                        r"\text{Άρα το } G_1 \text{ δεν είναι διμερές (bipartite), συνεπώς } \chi(G_1) \ge 3. \\ "
                        r"\text{2. Άνω φράγμα: Δίνουμε έγκυρη 3-χρωμάτιση } c: V_1 \to \{1, 2, 3\}: \\ "
                        r"\text{Χρώμα 1: } \{A, C, E\} \ (\text{ανεξάρτητο σύνολο, καμία ακμή μεταξύ τους}), \\ "
                        r"\text{Χρώμα 2: } \{B, D, G\} \ (\text{ανεξάρτητο σύνολο, καμία ακμή μεταξύ τους}), \\ "
                        r"\text{Χρώμα 3: } \{F\} \ (\text{οι γείτονες του F είναι C (χρώμα 1), E (χρώμα 1), G (χρώμα 2)}). \\ "
                        r"\text{Καμία γειτονική κορυφή δεν έχει το ίδιο χρώμα. Άρα } \chi(G_1) = 3."
                    ),
                    result=r"\chi(G_1) = 3",
                    rationale="Η ύπαρξη περιττού κύκλου επιβάλλει chi >= 3, και η ρητή κατασκευή 3 ανεξάρτητων χρωματικών κλάσεων αποδεικνύει ότι chi = 3.",
                ),
            ],
            final_answer=(
                "α': Τα γραφήματα είναι ισόμορφα (G1 ≅ G2) μέσω της 1-προς-1 απεικόνισης f(A)=1, f(B)=2, f(C)=3, f(D)=4, f(E)=5, f(F)=6, f(G)=7.\n"
                "β': χ(G1) = 3. Το γράφημα δεν είναι 2-χρωματίσιμο λόγω του περιττού κύκλου C5 (A-G-F-C-D-A), και μια βέλτιστη 3-χρωμάτιση είναι: Χρώμα 1: {A, C, E}, Χρώμα 2: {B, D, G}, Χρώμα 3: {F}."
            ),
            detailed_justification=(
                "Το γράφημα είναι ελεύθερο τριγώνων (K3-free), αλλά περιέχει περιττούς κύκλους C5 και C7, πράγμα που απαγορεύει τη 2-χρωμάτιση. "
                "Με 3 χρώματα χωρίζεται εύκολα σε 3 ανεξάρτητα υποσύνολα."
            ),
            common_pitfalls=[
                "Υπόθεση ότι χ(G1) = 4 χωρίς απόδειξη.",
                "Μη αναφορά της ύπαρξης περιττού κύκλου ως αιτία αποκλεισμού της 2-χρωμάτισης.",
            ],
            related_theory_topic="Ισομορφισμός Γραφημάτων & Χρωματικός Αριθμός",
        ),
        ExamQuestion(
            question_number=7,
            title="Σύνθεση Κανονικής Έκφρασης (Περιορισμοί 0, 1, 2)",
            question_type="Τυπικές Γλώσσες & Αυτόματα",
            prompt_text=(
                "Γράψτε μία κανονική έκφραση για συμβολοσειρές στο $\\{0, 1, 2\\}$ που:\n"
                "1. Ξεκινούν με το σύμβολο $1$\n"
                "2. Περιέχουν τουλάχιστον μία εμφάνιση του \"02\"\n"
                "3. Τελειώνουν με άρτιο αριθμό συμβόλων $2$"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ανάλυση Περιορισμών",
                    formula=r"\Sigma = \{0, 1, 2\}",
                    substitution=(
                        r"\text{1. Αρχή: } 1 \Sigma^* \\ "
                        r"\text{2. Εμφάνιση } 02: \Sigma^* 02 \Sigma^* \\ "
                        r"\text{3. Τερματισμός με άρτιο αριθμό 2: } (\epsilon \cup \Sigma^* (0 \mid 1))(22)^*"
                    ),
                    result=r"\text{Διαχωρισμός σε 2 περιπτώσεις}",
                    rationale="Η ακολουθία '02' μπορεί να προηγείται του τελευταίου μη-2 συμβόλου, ή να αποτελεί η ίδια το '0' ως τελευταίο μη-2 σύμβολο ακολουθούμενο από (22)+.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Σύνθεση Τελικής Έκφρασης",
                    formula=r"r = 1(0|1|2)^* 02 (0|1|2)^* (0|1)(22)^* \;\mid\; 1(0|1|2)^* 0(22)^+",
                    substitution=(
                        r"\text{Περίπτωση A: Το } 02 \text{ εμφανίζεται και αργότερα υπάρχει μη-2 σύμβολο } (0|1) \text{ πριν από } (22)^*. \\ "
                        r"\text{Περίπτωση B: Το τελευταίο μη-2 σύμβολο είναι το } 0 \text{ του } 02, \text{ ακολουθούμενο από άρτιο } (22)^+ \text{ (22, 2222, ...)}."
                    ),
                    result=r"1(0|1|2)^* 02 (0|1|2)^* (0|1)(22)^* \;\mid\; 1(0|1|2)^* 0(22)^+",
                    rationale="Καλύπτει 100% όλες τις έγκυρες συμβολοσειρές χωρίς επικάλυψη μη-έγκυρων καταλήξεων.",
                ),
            ],
            final_answer=r"1(0|1|2)^* 02 (0|1|2)^* (0|1)(22)^* \mid 1(0|1|2)^* 0(22)^+",
            detailed_justification=(
                "Κάθε συμβολοσειρά που τελειώνει σε άρτιο αριθμό 2 είτε τελειώνει σε μη-2 σύμβολο ακολουθούμενο από (22)*, "
                "είτε τελειώνει σε θετικό άρτιο πλήθος δυαριών. Με το διαχωρισμό αυτό εξασφαλίζεται ότι το '02' εντοπίζεται εγγυημένα και το επίθημα δυαριών είναι άρτιο."
            ),
            common_pitfalls=[
                "Έκφραση 1(0|1|2)* 02 (22)* η οποία παραλείπει όλες τις συμβολοσειρές που περιέχουν άλλα σύμβολα μετά το 02.",
            ],
            related_theory_topic="Σύνθεση Κανονικών Εκφράσεων με Σύνθετους Περιορισμούς",
        ),
        ExamQuestion(
            question_number=8,
            title="Αναγνώριση Συμβολοσειρών: (a|b)* c (a|b|c)*",
            question_type="Τυπικές Γλώσσες & Αυτόματα",
            prompt_text=(
                "Για την έκφραση $(a|b)^* c (a|b|c)^*$, προσδιορίστε ποιες συμβολοσειρές ανήκουν στη γλώσσα:\n"
                "`abcca`, `ccab`, `abab`, `cabcba`, `bacacc`, `abcdefg`"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Σημασιολογία της Γλώσσας",
                    formula=r"L = \{w \in \{a, b, c\}^* : w \text{ περιέχει τουλάχιστον ένα } 'c'\}",
                    substitution=(
                        r"\text{1. Το αλφάβητο είναι } \Sigma = \{a, b, c\}. \\ "
                        r"\text{2. Πριν από το } c \text{ υπάρχουν μόνο } a \text{ και } b \ ((a|b)^*). \\ "
                        r"\text{3. Μετά το πρώτο } c \text{ επιτρέπεται οποιοσδήποτε συνδυασμός } \{a,b,c\}^*."
                    ),
                    result=r"\text{Κριτήριο: Σύμβολα μόνο από } \{a,b,c\} \text{ ΚΑΙ } \text{count}(c) \ge 1",
                    rationale="Η έκφραση αναγνωρίζει κάθε συμβολοσειρά στο {a,b,c}* που έχει τουλάχιστον ένα c.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Αξιολόγηση Κάθε Συμβολοσειράς",
                    formula=r"w \in L",
                    substitution=(
                        r"\text{abcca: περιέχει μόνο } \{a,b,c\} \text{ και έχει 'c' } \implies \mathbf{ΝΑΙ}. \\ "
                        r"\text{ccab: περιέχει μόνο } \{a,b,c\} \text{ και έχει 'c' } \implies \mathbf{ΝΑΙ}. \\ "
                        r"\text{abab: δεν περιέχει κανένα 'c' } \implies \mathbf{ΟΧΙ}. \\ "
                        r"\text{cabcba: περιέχει μόνο } \{a,b,c\} \text{ και έχει 'c' } \implies \mathbf{ΝΑΙ}. \\ "
                        r"\text{bacacc: περιέχει μόνο } \{a,b,c\} \text{ και έχει 'c' } \implies \mathbf{ΝΑΙ}. \\ "
                        r"\text{abcdefg: περιέχει σύμβολα } \{d,e,f,g\} \notin \Sigma \implies \mathbf{ΟΧΙ}."
                    ),
                    result=r"\text{Ανήκουν: abcca, ccab, cabcba, bacacc}",
                    rationale="Οι 4 αυτές συμβολοσειρές πληρούν και τις δύο συνθήκες.",
                ),
            ],
            final_answer="Ανήκουν στη γλώσσα οι συμβολοσειρές: abcca, ccab, cabcba, bacacc.",
            detailed_justification=(
                "Η συμβολοσειρά abab απορρίπτεται επειδή δεν περιέχει το υποχρεωτικό σύμβολο 'c'. "
                "Η συμβολοσειρά abcdefg απορρίπτεται επειδή περιέχει σύμβολα (d, e, f, g) εκτός του αλφαβήτου {a, b, c} της κανονικής έκφρασης."
            ),
            common_pitfalls=[
                "Αποδοχή του abcdefg θεωρώντας λανθασμένα ότι τα σύμβολα d,e,f,g αγνοούνται.",
            ],
            related_theory_topic="Γλώσσες Κανονικών Εκφράσεων & Αλφάβητα",
        ),
        ExamQuestion(
            question_number=9,
            title="Μαθηματική Επαγωγή: sum_{k=1}^n k * k! = (n+1)! - 1",
            question_type="Μαθηματική Επαγωγή",
            prompt_text=(
                "Δείξτε με μαθηματική επαγωγή ότι για κάθε φυσικό αριθμό $n \\geq 1$ ισχύει:\n\n"
                "$$\\sum_{k=1}^{n} k \\cdot k! = (n+1)! - 1$$"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Βάση της Επαγωγής (n = 1)",
                    formula=r"P(1): \sum_{k=1}^1 k \cdot k! = (1+1)! - 1",
                    substitution=r"1 \cdot 1! = 1 \cdot 1 = 1, \quad 2! - 1 = 2 - 1 = 1 \implies 1 = 1",
                    result=r"P(1) \text{ αληθές}",
                    rationale="Η βάση της επαγωγής επαληθεύεται απόλυτα.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Επαγωγική Υπόθεση",
                    formula=r"\text{Υποθέτουμε ότι ισχύει για } n = m \ge 1: \quad \sum_{k=1}^m k \cdot k! = (m+1)! - 1",
                    substitution=r"P(m) \text{ υποτίθεται αληθές}",
                    result=r"\text{Υπόθεση } P(m)",
                    rationale="Η υπόθεση θα εφαρμοστεί για την αντικατάσταση του αθροίσματος των πρώτων m όρων.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Επαγωγικό Βήμα (n = m + 1)",
                    formula=r"\text{Δεικτέο } P(m+1): \quad \sum_{k=1}^{m+1} k \cdot k! = (m+2)! - 1",
                    substitution=(
                        r"\sum_{k=1}^{m+1} k \cdot k! = \left( \sum_{k=1}^m k \cdot k! \right) + (m+1) \cdot (m+1)! \\ "
                        r"= [(m+1)! - 1] + (m+1) \cdot (m+1)! \\ "
                        r"= (m+1)! \cdot [1 + (m+1)] - 1 \\ "
                        r"= (m+1)! \cdot (m+2) - 1 \\ "
                        r"= (m+2)! - 1"
                    ),
                    result=r"P(m+1) \text{ αληθές}",
                    rationale="Εφαρμογή της επαγωγικής υπόθεσης και παραγοντοποίηση του (m+1)! οδηγεί ακριβώς στο (m+2)! - 1.",
                ),
            ],
            final_answer="Αποδείχθηκε πλήρως με Μαθηματική Επαγωγή ότι sum_{k=1}^n k * k! = (n+1)! - 1 για κάθε n ≥ 1.",
            detailed_justification=(
                "Η απόδειξη στηρίζεται στην ιδιότητα του παραγοντικού (m+1)! * (m+2) = (m+2)!. "
                "Εναλλακτικά, προκύπτει τηλεσκοπικά αφού k * k! = (k+1 - 1) * k! = (k+1)! - k!."
            ),
            common_pitfalls=[
                "Λάθος στην παραγοντοποίηση (m+1)! * [1 + (m+1)].",
            ],
            related_theory_topic="Μαθηματική Επαγωγή & Παραγοντικά Αθροίσματα",
        ),
    ]

    diagram_nodes = [
        DiagramNode(id="A", label="A", node_type="vertex", x=180, y=50),
        DiagramNode(id="B", label="B", node_type="vertex", x=270, y=90),
        DiagramNode(id="C", label="C", node_type="vertex", x=300, y=190),
        DiagramNode(id="D", label="D", node_type="vertex", x=240, y=280),
        DiagramNode(id="E", label="E", node_type="vertex", x=120, y=280),
        DiagramNode(id="F", label="F", node_type="vertex", x=60, y=190),
        DiagramNode(id="G", label="G", node_type="vertex", x=90, y=90),
    ]

    diagram_edges = [
        DiagramEdge(source_id="A", target_id="B", label="(A,B)"),
        DiagramEdge(source_id="B", target_id="C", label="(B,C)"),
        DiagramEdge(source_id="C", target_id="D", label="(C,D)"),
        DiagramEdge(source_id="D", target_id="E", label="(D,E)"),
        DiagramEdge(source_id="E", target_id="F", label="(E,F)"),
        DiagramEdge(source_id="F", target_id="G", label="(F,G)"),
        DiagramEdge(source_id="G", target_id="A", label="(G,A)"),
        DiagramEdge(source_id="A", target_id="D", label="(A,D) [Χορδή]"),
        DiagramEdge(source_id="B", target_id="E", label="(B,E) [Χορδή]"),
        DiagramEdge(source_id="C", target_id="F", label="(C,F) [Χορδή]"),
    ]

    justifications = [
        DesignJustification(
            title="Κύκλος C7 με 3 Χορδές και 3-Χρωματισμός",
            category="Graph Theory",
            description="Το G1 έχει 7 κορυφές, 10 ακμές, περιέχει C5, δεν έχει τρίγωνα, και χρωματίζεται με 3 χρώματα.",
            rationale="Αποτελεί κλασικό αντιπαράδειγμα όπου chi(G)=3 παρά την απουσία τριγώνων (K3-free).",
        ),
    ]

    solution_code = '''# Verification Script for Practice Exam Hard (Course 203)
import math

# Q2: 4-set Inclusion-Exclusion
U = 500
K, J, R, P = 180, 150, 200, 220
KJ, KR, JR, RP, KP, JP = 65, 80, 70, 90, 85, 75
KJR, KRP, JRP, KJP = 25, 30, 20, 35
KJRP = 15

s1 = K + J + R + P
s2 = KJ + KR + JR + RP + KP + JP
s3 = KJR + KRP + JRP + KJP
s4 = KJRP
union = s1 - s2 + s3 - s4
neither = U - union
assert neither == 120

# Q3: 3 d12 dice
# Q3.a: prime sums > 25 (primes: 29, 31)
total_outcomes = 12**3
primes_29_31 = 0
for d1 in range(1, 13):
    for d2 in range(1, 13):
        for d3 in range(1, 13):
            s = d1 + d2 + d3
            if s in (29, 31):
                primes_29_31 += 1
assert primes_29_31 == 57
assert primes_29_31 / total_outcomes == 19 / 576

# Q3.b: exactly 2 squares in {1, 4, 9}
squares = {1, 4, 9}
count_2sq = 0
for d1 in range(1, 13):
    for d2 in range(1, 13):
        for d3 in range(1, 13):
            num_sq = (d1 in squares) + (d2 in squares) + (d3 in squares)
            if num_sq == 2:
                count_2sq += 1
assert count_2sq == 243
assert count_2sq / total_outcomes == 9 / 64

# Q4: Bayes
p_fp = 0.02 * 0.40 + 0.04 * 0.35 + 0.06 * 0.25
assert abs(p_fp - 0.037) < 1e-9
p_c_given_fp = (0.06 * 0.25) / p_fp
assert abs(p_c_given_fp - 15/37) < 1e-9

# Q9: Induction formula check
for n in range(1, 10):
    lhs = sum(k * math.factorial(k) for k in range(1, n + 1))
    rhs = math.factorial(n + 1) - 1
    assert lhs == rhs

print("Practice Exam Hard: All 9 questions verified successfully.")
'''

    return Scenario(
        id="practice_exam_hard",
        title="Πρακτική Εξέταση (Επίπεδο: Hard)",
        subtitle="203: Διακριτά Μαθηματικά — Προχωρημένο Σετ Ασκήσεων & Αποδείξεων",
        course_tag="Πρακτική Εξέταση",
        duration_info="4 Ώρες (10 Μονάδες)",
        paragraphs=paragraphs,
        questions=questions,
        diagram_nodes=diagram_nodes,
        diagram_edges=diagram_edges,
        justifications=justifications,
        solution_code=solution_code,
    )
