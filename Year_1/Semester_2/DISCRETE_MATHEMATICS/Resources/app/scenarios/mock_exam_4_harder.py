"""Mock Exam 4 (Harder) scenario module for Discrete Mathematics.

Transcribes Mock Exam 4 verbatim with interactive highlights, and provides
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


def createMockExam4HarderScenario() -> Scenario:
    """Constructs the Scenario instance for Mock Exam 4 (Harder).

    Returns:
        Scenario: Complete scenario with verbatim text, annotations, and worked solutions.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Τμήμα Πληροφορικής και Τηλεπικοινωνιών — Πανεπιστήμιο Ιωαννίνων\n"),
                TextSegment(text="Σπυρίδων Τζίμας • Εαρινό Εξάμηνο 2025\n"),
                TextSegment(text="203: Διακριτά Μαθηματικά — Εικονική Εξέταση 4 (Δυσκολότερη)\n\n"),
                TextSegment(text="Η βαθμολογική αξία της εξέτασης είναι 10 μονάδες. Η χρονική διάρκεια είναι 3 ώρες. "),
                TextSegment(text="Επιτρέπεται στυλό μόνο μπλε και μαύρου χρώματος. Επιτρέπεται μολύβι μόνο για γραφή στο πρόχειρο. Καλή Επιτυχία!"),
            ]
        ),
        Paragraph(
            accent_border_color="var(--purple)",
            segments=[
                TextSegment(text="Θέμα 1. (3 μονάδες) ", is_highlight=True, category="graph", tag_label="Q1-PLANAR-BOUNDS", badge_class="badge-graph", tooltip="Classification: Planar Graphs & Handshaking Inequalities\nDetection Clue: 'συνεκτικό επίπεδο γράφημα... deg(v) >= 3... e >= (?)'\nApplication Rationale: Solves lower bounds for edges using 2e = sum deg(v) >= 3v and boundary face relations"),
                TextSegment(text="Έστω G = (V, E) ένα συνεκτικό επίπεδο γράφημα με v κορυφές, e ακμές και f περιοχές. "),
                TextSegment(text="Γνωρίζουμε ότι ο βαθμός κάθε κορυφής είναι τουλάχιστον 3. Αποδείξτε ότι e ≥ (?):\n\n"),
                TextSegment(text="Ομάδα Α: (?) = 3v/2 | Ομάδα Β: (?) = 3f/2 | Ομάδα Γ: (?) = 3v - 6 | Ομάδα Δ: (?) = 2v - 4\n"),
                TextSegment(text="(Προσοχή στην «παγίδα»: Ποιες ανισότητες ισχύουν πάντα σε επίπεδα γραφήματα και πώς συνδυάζονται με τον τύπο του Euler;)"),
            ]
        ),
        Paragraph(
            accent_border_color="var(--accent)",
            segments=[
                TextSegment(text="Θέμα 2. (4 μονάδες) ", is_highlight=True, category="automata", tag_label="Q2-ADV-REGEX", badge_class="badge-automata", tooltip="Classification: Advanced Regular Expressions with Substring Constraints\nDetection Clue: 'αλφάβητο Σ = {a, b}... κανονική έκφραση... δεν εμφανίζεται bb...'\nApplication Rationale: Synthesizes complex regexes avoiding forbidden sequences or matching count divisibility"),
                TextSegment(text="Δίνεται το αλφάβητο Σ = {a, b}. Γράψτε την κανονική έκφραση για τη γλώσσα L που περιλαμβάνει όλες τις λέξεις όπου:\n\n"),
                TextSegment(text="Ομάδα Α: Δεν εμφανίζεται η υποσυμβολοσειρά bb.\n"),
                TextSegment(text="Ομάδα Β: Κάθε a ακολουθείται άμεσα από τουλάχιστον ένα b.\n"),
                TextSegment(text="Ομάδα Γ: Το πλήθος των a είναι πολλαπλάσιο του 3 (συμπεριλαμβανομένου του 0).\n"),
                TextSegment(text="Ομάδα Δ: Δεν περιέχουν ούτε aa ούτε bb ως υποσυμβολοσειρές."),
            ]
        ),
        Paragraph(
            accent_border_color="var(--blue-action)",
            segments=[
                TextSegment(text="Θέμα 3. (3 μονάδες) ", is_highlight=True, category="set", tag_label="Q3-PIE-BOUNDS", badge_class="badge-set", tooltip="Classification: Inclusion-Exclusion with Unknown Pairwise Intersections\nDetection Clue: '100 φοιτητές... 60 DM, 50 Prog, 40 LinAlg... (?) παρακολουθούν και τα 3... μέγιστος και ελάχιστος'\nApplication Rationale: Derives extreme values for complement using Bonferroni bounds and Venn consistency"),
                TextSegment(text="Σε μία τάξη 100 φοιτητών, 60 παρακολουθούν Διακριτά Μαθηματικά, 50 παρακολουθούν Προγραμματισμό και 40 παρακολουθούν Γραμμική Άλγεβρα. "),
                TextSegment(text="Γνωρίζουμε επίσης ότι (?) φοιτητές παρακολουθούν και τα 3 μαθήματα. "),
                TextSegment(text="Ποιος είναι ο μέγιστος και ποιος ο ελάχιστος δυνατός αριθμός φοιτητών που ΔΕΝ παρακολουθούν κανένα από τα 3 μαθήματα;\n\n"),
                TextSegment(text="Ομάδα Α: (?) = 10 | Ομάδα Β: (?) = 15 | Ομάδα Γ: (?) = 20 | Ομάδα Δ: (?) = 5\n"),
                TextSegment(text="(Παγίδα: Εφαρμόστε σωστά την Αρχή Εγκλεισμού-Αποκλεισμού λαμβάνοντας υπόψη τα άγνωστα όρια για τις τομές ανά δύο)."),
            ]
        ),
    ]

    questions = [
        # QUESTION 1
        ExamQuestion(
            question_number=1,
            title="Ανισότητες Ακμών & Περιοχών σε Επίπεδα Γραφήματα",
            question_type="Θεωρία Γραφημάτων",
            prompt_text=(
                "Έστω $G = (V, E)$ ένα συνεκτικό επίπεδο γράφημα με $v$ κορυφές, $e$ ακμές και $f$ περιοχές. "
                "Γνωρίζουμε ότι $\\deg(v) \\ge 3$ για κάθε κορυφή $v \\in V$. Αποδείξτε ότι $e \\ge (?)$:\n\n"
                "- **Ομάδα Α:** $(?) = \\frac{3v}{2}$\n"
                "- **Ομάδα Β:** $(?) = \\frac{3f}{2}$\n"
                "- **Ομάδα Γ:** $(?) = 3v - 6$ (Παγίδα: Ποια φορά έχει η ανισότητα;)\n"
                "- **Ομάδα Δ:** $(?) = 2v - 4$"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Απόδειξη Ομάδας Α: e ≥ 3v/2",
                    formula=r"\sum_{v \in V} \deg(v) = 2e",
                    substitution=r"\forall v \in V, \ \deg(v) \ge 3 \implies 2e = \sum_{v \in V} \deg(v) \ge \sum_{v \in V} 3 = 3v \implies e \ge \frac{3v}{2}",
                    result=r"e \ge \frac{3v}{2} \ (\text{Αποδείχθηκε})",
                    rationale="Άμεση συνέπεια του Λήμματος Χειραψιών.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Απόδειξη Ομάδας Β: e ≥ 3f/2",
                    formula=r"\sum_{F \text{ face}} \deg(F) = 2e",
                    substitution=r"\text{Σε απλό επίπεδο γράφημα κάθε έδρα ορίζεται από τουλάχιστον } 3 \text{ ακμές: } \deg(F) \ge 3 \implies 2e = \sum \deg(F) \ge 3f \implies e \ge \frac{3f}{2}",
                    result=r"e \ge \frac{3f}{2} \ (\text{Αποδείχθηκε})",
                    rationale="Δυϊκό λήμμα χειραψιών για τις περιοχές ενός επιπέδου γραφήματος.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Ανάλυση Παγίδας Ομάδων Γ & Δ: e ≤ 3v - 6",
                    formula=r"v - e + f = 2 \land 2e \ge 3f \implies f \le \frac{2}{3}e \implies v - e + \frac{2}{3}e \ge 2 \implies e \le 3v - 6",
                    substitution=r"\text{Η ανισότητα του Euler δίνει } \mathbf{ΑΝΩ} \text{ φράγμα } e \le 3v - 6 \text{ (και όχι κάτω φράγμα!)}",
                    result=r"\text{Παγίδα: Ισχύει } e \le 3v - 6 \text{ και } e \le 2v - 4 \text{ (αν δεν έχει τρίγωνα)}",
                    rationale="Η εκφώνηση υπογραμμίζει την παγίδα: το 3v-6 είναι άνω φράγμα για το πλήθος των ακμών σε επίπεδο γράφημα.",
                ),
            ],
            final_answer="Ομάδα Α: e ≥ 3v/2 (από Handshaking Lemma)\nΟμάδα Β: e ≥ 3f/2 (από άθροισμα βαθμών εδρών)\nΟμάδες Γ, Δ: Παγίδα! Το 3v-6 και 2v-4 είναι ΑΝΩ φράγματα (e ≤ 3v - 6)",
            detailed_justification="Από το λήμμα των χειραψιών, 2e = Σ deg(v) >= 3v άρα e >= 3v/2. Ομοίως για τις έδρες, 2e = Σ deg(F) >= 3f άρα e >= 3f/2. Σε συνδυασμό με τον τύπο Euler v - e + f = 2, προκύπτει το κλασικό άνω φράγμα e <= 3v - 6.",
            common_pitfalls=[
                "Αντιστροφή της φοράς της ανισότητας: Θεώρηση ότι e >= 3v - 6 (είναι e <= 3v - 6).",
            ],
            related_theory_topic="Επίπεδα Γραφήματα & Τύπος Euler",
        ),

        # QUESTION 2
        ExamQuestion(
            question_number=2,
            title="Κανονικές Εκφράσεις με Περιορισμούς Υποσυμβολοσειρών",
            question_type="Αυτόματα & Τυπικές Γλώσσες",
            prompt_text=(
                "Δίνεται το αλφάβητο $\\Sigma = \\{a, b\\}$. Γράψτε την κανονική έκφραση για τη γλώσσα $L$:\n\n"
                "- **Ομάδα Α:** Δεν εμφανίζεται η υποσυμβολοσειρά $bb$.\n"
                "- **Ομάδα Β:** Κάθε $a$ ακολουθείται άμεσα από τουλάχιστον ένα $b$.\n"
                "- **Ομάδα Γ:** Το πλήθος των $a$ είναι πολλαπλάσιο του 3 (συμπεριλαμβανομένου του 0).\n"
                "- **Ομάδα Δ:** Δεν περιέχουν ούτε $aa$ ούτε $bb$ ως υποσυμβολοσειρές."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ομάδα Α — Χωρίς υποσυμβολοσειρά bb",
                    formula=r"\text{Τα } b \text{ εμφανίζονται μόνο μεμονωμένα, περιβαλλόμενα από } a",
                    substitution=r"(a \cup ba)^*(b \cup \epsilon) \quad \text{ή} \quad (b \cup \epsilon)(a \cup ab)^*",
                    result=r"(a \cup ba)^*(b \cup \epsilon)",
                    rationale="Κάθε b που δεν βρίσκεται στο τέλος πρέπει υποχρεωτικά να ακολουθείται από a.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ομάδα Β — Κάθε a ακολουθείται άμεσα από τουλάχιστον ένα b",
                    formula=r"\text{Κάθε } a \text{ συνδυάζεται με μπλοκ } b^+",
                    substitution=r"(b \cup ab^+)^* \quad \text{ή ισοδύναμα} \quad (b \cup ab b^*)^*",
                    result=r"(b \cup ab^+)^*",
                    rationale="Δεν μπορεί να υπάρξει ποτέ a στο τέλος της λέξης ούτε διαδοχικά a χωρίς ενδιάμεσο b.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Ομάδα Γ — Πλήθος των a πολλαπλάσιο του 3",
                    formula=r"\text{Μπλοκ τριάδων } a",
                    substitution=r"(b^* a b^* a b^* a b^*)^* \quad \text{ή} \quad (b \cup a b^* a b^* a)^*",
                    result=r"(b^* a b^* a b^* a b^*)^*",
                    rationale="Κάθε επανάληψη του βασικού μοτίβου περιέχει ακριβώς τρία a, ενώ επιτρέπονται αυθαίρετα b παντού.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Ομάδα Δ — Ούτε aa ούτε bb (Εναλλασσόμενα σύμβολα)",
                    formula=r"\text{Αυστηρά εναλλασσόμενα } a \text{ και } b",
                    substitution=r"(ab)^*(a \cup \epsilon) \cup (ba)^*(b \cup \epsilon)",
                    result=r"(ab)^*(a \cup \epsilon) \cup (ba)^*(b \cup \epsilon)",
                    rationale="Οι μόνες επιτρεπτές λέξεις είναι: ε, a, b, ab, ba, aba, bab, abab, baba, κλπ.",
                ),
            ],
            final_answer="Ομάδα Α: (a | ba)*(b | ε)\nΟμάδα Β: (b | ab+)*\nΟμάδα Γ: (b* a b* a b* a b*)*\nΟμάδα Δ: (ab)*(a | ε) | (ba)*(b | ε)",
            detailed_justification="Κάθε έκφραση απομονώνει τις επιτρεπτές αλληλουχίες συμβόλων εξασφαλίζοντας ότι η γλώσσα περιλαμβάνει και το κενό σύμβολο ε εφόσον ικανοποιεί τις συνθήκες.",
            common_pitfalls=[
                "Στην Ομάδα Α, το (a | b)* χωρίς περιορισμό παράγει το bb.",
                "Στην Ομάδα Δ, ξεχνιέται ότι η λέξη μπορεί να ξεκινά είτε με a είτε με b.",
            ],
            related_theory_topic="Κανονικές Εκφράσεις & Περιορισμοί",
        ),

        # QUESTION 3
        ExamQuestion(
            question_number=3,
            title="Αρχή Εγκλεισμού-Αποκλεισμού: Μέγιστος & Ελάχιστος Αριθμός",
            question_type="Θεωρία Συνόλων",
            prompt_text=(
                "Σε μία τάξη 100 φοιτητών:\n"
                "- 60 παρακολουθούν Διακριτά Μαθηματικά (D)\n"
                "- 50 παρακολουθούν Προγραμματισμό (P)\n"
                "- 40 παρακολουθούν Γραμμική Άλγεβρα (L)\n"
                "- (?) φοιτητές παρακολουθούν και τα 3 μαθήματα ($|D \\cap P \\cap L| = (?)$)\n\n"
                "Ποιος είναι ο μέγιστος και ποιος ο ελάχιστος δυνατός αριθμός φοιτητών που ΔΕΝ παρακολουθούν κανένα μάθημα;\n\n"
                "- **Ομάδα Α:** $(?) = 10$\n"
                "- **Ομάδα Β:** $(?) = 15$\n"
                "- **Ομάδα Γ:** $(?) = 20$\n"
                "- **Ομάδα Δ:** $(?) = 5$"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Τύπος Εγκλεισμού-Αποκλεισμού με Άγνωστες Τομές",
                    formula=r"|D \cup P \cup L| = |D| + |P| + |L| - S_2 + |D \cap P \cap L| = 150 - S_2 + (?)",
                    substitution=r"\text{Όπου } S_2 = |D \cap P| + |P \cap L| + |D \cap L|. \text{ Το πλήθος εκτός είναι } N = 100 - |D \cup P \cup L| = 100 - (150 - S_2 + (?)) = S_2 - 50 - (?)",
                    result=r"N = S_2 - 50 - (?)",
                    rationale="Για να βρούμε το ελάχιστο και μέγιστο N, αρκεί να βρούμε τα όρια του S2.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Όρια του S2 και της Ένωσης",
                    formula=r"\max(|D|, |P|, |L|) \le |D \cup P \cup L| \le 100",
                    substitution=(
                        r"60 \le |D \cup P \cup L| \le 100 \implies 60 \le 150 - S_2 + (?) \le 100 \\ "
                        r"\implies 50 + (?) \le S_2 \le 90 + (?)"
                    ),
                    result=r"N_{\min} = 0, \quad N_{\max} = 100 - 60 = 40",
                    rationale="Ο ελάχιστος αριθμός εκτός είναι 0 (όταν η ένωση καλύπτει και τους 100). Ο μέγιστος αριθμός εκτός είναι 100 - 60 = 40 (όταν P και L είναι υποσύνολα του D, οπότε η ένωση είναι τουλάχιστον 60).",
                ),
            ],
            final_answer="Ελάχιστος δυνατός αριθμός: 0 φοιτητές (όταν η ένωση είναι 100)\nΜέγιστος δυνατός αριθμός: 40 φοιτητές (αφού τουλάχιστον 60 παρακολουθούν D, άρα το μέγιστο εκτός είναι 100 - 60 = 40)",
            detailed_justification="Επειδή 60 φοιτητές παρακολουθούν Διακριτά Μαθηματικά, η ένωση των τριών μαθημάτων έχει μέγεθος τουλάχιστον 60 (|D ∪ P ∪ L| >= 60). Άρα οι φοιτητές εκτός δεν μπορούν να υπερβαίνουν τους 100 - 60 = 40. Αντίστοιχα, αν οι φοιτητές κατανέμονται ώστε να καλύψουν όλη την τάξη, η ένωση μπορεί να φτάσει τους 100, δίνοντας ελάχιστο 0.",
            common_pitfalls=[
                "Ξέχασμα του κάτω φράγματος της ένωσης: |D ∪ P ∪ L| >= max(60, 50, 40) = 60.",
            ],
            related_theory_topic="Εγκλεισμός-Αποκλεισμός & Όρια",
        ),
    ]

    diagram_nodes = [
        DiagramNode(id="D", label="D (60)", node_type="state", x=160, y=140),
        DiagramNode(id="P", label="P (50)", node_type="state", x=340, y=140),
        DiagramNode(id="L", label="L (40)", node_type="state", x=250, y=260),
    ]

    diagram_edges = [
        DiagramEdge(source_id="D", target_id="P", label="D ∩ P"),
        DiagramEdge(source_id="P", target_id="L", label="P ∩ L"),
        DiagramEdge(source_id="D", target_id="L", label="D ∩ L"),
    ]

    justifications = [
        DesignJustification(
            title="Ανισότητες Bonferroni",
            category="Set Bounds",
            description="Η ένωση συνόλων φράσσεται από κάτω από το μέγιστο μεμονωμένο σύνολο.",
            rationale="Επιτρέπει τον άμεσο προσδιορισμό του μέγιστου πλήθους μη συμμετεχόντων: 100 - 60 = 40.",
        ),
    ]

    solution_code = '''# Verification Script for Mock Exam 4 (Course 203)

# Q1: Planar graph inequalities check
# For simple planar graphs: e <= 3v - 6
# For degrees >= 3: 2e >= 3v => e >= 1.5v
v = 6
min_e = 1.5 * v
max_e = 3 * v - 6
print(f"Mock Exam 4 - Q1: For v={v}, 1.5v = {min_e} <= e <= 3v-6 = {max_e}")

# Q3: PIE Bounds
u = 100
d, p, l = 60, 50, 40
min_outside = max(0, u - (d + p + l))  # Can easily be 0 since d+p+l = 150 >= 100
max_outside = u - max(d, p, l)  # 100 - 60 = 40
print(f"Mock Exam 4 - Q3: Outside students in [Min: {min_outside}, Max: {max_outside}]")
'''

    return Scenario(
        id="mock_exam_4_harder",
        title="Εικονική Εξέταση 4 (Δυσκολότερη)",
        subtitle="203: Διακριτά Μαθηματικά — Επίπεδα Γραφήματα, RegEx & Όρια Συνόλων",
        course_tag="Εικονική Εξέταση",
        duration_info="3 Ώρες (10 Μονάδες)",
        paragraphs=paragraphs,
        questions=questions,
        diagram_nodes=diagram_nodes,
        diagram_edges=diagram_edges,
        justifications=justifications,
        solution_code=solution_code,
    )
