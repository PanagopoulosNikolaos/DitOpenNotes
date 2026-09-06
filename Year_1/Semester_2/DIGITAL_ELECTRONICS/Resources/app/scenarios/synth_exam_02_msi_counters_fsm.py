"""Synthetic Exam 02 scenario module.

Implements the complete verbatim exam paper for hazards, MSI multiplexers/decoders,
synchronous JK counters, and Moore FSM in VHDL, with three-part tooltips,
KaTeX step-by-step solutions, and state diagram SVG.
"""

from models.scenario import (
    Scenario,
    Paragraph,
    TextSegment,
    ExamQuestion,
    QuestionOption,
    CalculationStep,
    GivenParameter,
    DesignJustification,
)


def createSyntheticExam02Scenario() -> Scenario:
    """Creates and returns the Synthetic Exam 02 scenario instance.

    Returns:
        Scenario: Fully configured scenario with verbatim text, questions, and SVG.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Συνθετικό Θέμα Εξετάσεων 02: Ψηφιακά Ηλεκτρονικά", is_highlight=False),
            ],
            accent_border_color=None,
        ),
        Paragraph(
            segments=[
                TextSegment(text="Οδηγίες: Διάρκεια εξέτασης: ", is_highlight=False),
                TextSegment(
                    text="2.5 ώρες",
                    is_highlight=True,
                    category="param",
                    tag_label="TIME",
                    badge_class="badge-param",
                    tooltip="Classification: Χρονικός Περιορισμός Εξέτασης | Detection Clue: 2.5 ώρες συνολική διάρκεια | Application Rationale: Ισομερής κατανομή χρόνου ανάμεσα σε MSI, Hazards, Counters και FSM.",
                ),
                TextSegment(text=". Όλα τα θέματα βαθμολογούνται με ", is_highlight=False),
                TextSegment(
                    text="2.5 μονάδες",
                    is_highlight=True,
                    category="param",
                    tag_label="WEIGHT",
                    badge_class="badge-param",
                    tooltip="Classification: Συντελεστής Βαρύτητας | Detection Clue: 2.5 μονάδες ανά θέμα | Application Rationale: Καλύπτει το 100% της εξεταστέας ύλης πανεπιστημιακών εξετάσεων.",
                ),
                TextSegment(text=" (Σύνολο: 10 μονάδες).", is_highlight=False),
            ],
            accent_border_color=None,
        ),
        # Theme 1 Paragraph
        Paragraph(
            segments=[
                TextSegment(text="Θέμα 1: Ανάλυση Κινδύνων (Hazards) και Θεώρημα Συναίνεσης\n", is_highlight=False),
                TextSegment(text="Δίνεται η λογική συνάρτηση 3 μεταβλητών: ", is_highlight=False),
                TextSegment(
                    text="F(A, B, C) = A · B + A' · C",
                    is_highlight=True,
                    category="boolean",
                    tag_label="HAZARD-EQ",
                    badge_class="badge-boolean",
                    tooltip="Classification: Λογική Συνάρτηση με Στατικό Κίνδυνο 1 | Detection Clue: AB + A'C | Application Rationale: Παρουσιάζει Static-1 hazard λόγω άνισων καθυστερήσεων στον αντιστροφέα του A.",
                ),
                TextSegment(text=".\n1. Εξηγήστε τι είναι ο ", is_highlight=False),
                TextSegment(
                    text="Στατικός Κίνδυνος 1 (Static-1 Hazard)",
                    is_highlight=True,
                    category="boolean",
                    tag_label="STATIC-1",
                    badge_class="badge-boolean",
                    tooltip="Classification: Δυναμικό Σφάλμα Χρονισμού | Detection Clue: Static-1 Hazard | Application Rationale: Στιγμιαία πτώση στο 0 (glitch) κατά τη μετάβαση μεταξύ δύο συνθηκών όπου η έξοδος πρέπει να παραμένει 1.",
                ),
                TextSegment(text=" και δείξτε υπό ποιες συνθήκες εισόδων (B=1, C=1) και ποια μετάβαση (A: 1 -> 0) εμφανίζεται παλμός σφάλματος λόγω καθυστέρησης διάδοσης Δt του αντιστροφέα.\n2. Εντοπίστε την αιτία στον χάρτη Karnaugh.\n3. Εξαλείψτε τον κίνδυνο προσθέτοντας τον ", is_highlight=False),
                TextSegment(
                    text="όρο συναίνεσης (consensus term B · C)",
                    is_highlight=True,
                    category="boolean",
                    tag_label="CONSENSUS",
                    badge_class="badge-boolean",
                    tooltip="Classification: Θεώρημα Συναίνεσης Boole | Detection Clue: Consensus Term BC | Application Rationale: XY + X'Z + YZ = XY + X'Z. Γεφυρώνει τα γειτονικά κελιά m(3) και m(7).",
                ),
                TextSegment(text=".", is_highlight=False),
            ],
            accent_border_color="var(--accent)",
        ),
        # Theme 2 Paragraph
        Paragraph(
            segments=[
                TextSegment(text="Θέμα 2: Σύνθεση Συνδυαστικών Κυκλωμάτων MSI\n", is_highlight=False),
                TextSegment(text="1. Υλοποιήστε τη συνάρτηση ", is_highlight=False),
                TextSegment(
                    text="F(A, B, C, D) = Σ m(1, 3, 4, 11, 12, 13, 14, 15)",
                    is_highlight=True,
                    category="boolean",
                    tag_label="MSI-FUNC",
                    badge_class="badge-boolean",
                    tooltip="Classification: Συνάρτηση Σύνθεσης MSI | Detection Clue: 4 μεταβλητές, 8 minterms | Application Rationale: Υλοποιείται με MUX 8:1 συνδέοντας τις 3 μεταβλητές στις γραμμές επιλογής.",
                ),
                TextSegment(text=" χρησιμοποιώντας έναν ", is_highlight=False),
                TextSegment(
                    text="πολυπλέκτη 8-σε-1 (8-to-1 MUX 74151)",
                    is_highlight=True,
                    category="vhdl",
                    tag_label="MUX-8TO1",
                    badge_class="badge-vhdl",
                    tooltip="Classification: Ολοκληρωμένο Κύκλωμα MSI | Detection Clue: 8-to-1 MUX | Application Rationale: 3 γραμμές επιλογής (S2=A, S1=B, S0=C) και 8 είσοδοι δεδομένων I0-I7.",
                ),
                TextSegment(text=" με γραμμές επιλογής S2=A, S1=B, S0=C και εισόδους I0-I7 από τη μεταβλητή D.\n2. Υλοποιήστε τη συνάρτηση G(A, B, C) = Σ m(0, 2, 6, 7) με ", is_highlight=False),
                TextSegment(
                    text="αποκωδικοποιητή 3:8 (Active-Low)",
                    is_highlight=True,
                    category="vhdl",
                    tag_label="DEC-3TO8",
                    badge_class="badge-vhdl",
                    tooltip="Classification: Αποκωδικοποιητής Ενεργών Χαμηλών Εξόδων | Detection Clue: Active-low outputs Yk' | Application Rationale: Κάθε έξοδος Yk' = mk'. Με De Morgan, το άθροισμα minterms γίνεται NAND των εξόδων.",
                ),
                TextSegment(text=" και μία πύλη NAND.", is_highlight=False),
            ],
            accent_border_color="var(--accent)",
        ),
        # Theme 3 Paragraph
        Paragraph(
            segments=[
                TextSegment(text="Θέμα 3: Σχεδίαση Σύγχρονου Μετρητή Modulo-6 με JK Flip-Flops\n", is_highlight=False),
                TextSegment(text="Σχεδιάστε σύγχρονο μετρητή που μετρά την ακολουθία ", is_highlight=False),
                TextSegment(
                    text="0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 0",
                    is_highlight=True,
                    category="fsm",
                    tag_label="MOD-6-SEQ",
                    badge_class="badge-fsm",
                    tooltip="Classification: Κυκλική Ακολουθία Modulo-6 | Detection Clue: 6 καταστάσεις (0 έως 5) | Application Rationale: Απαιτεί 3 Flip-Flops (2^3 = 8 > 6). Οι καταστάσεις 6 και 7 είναι Don't Cares.",
                ),
                TextSegment(text=" χρησιμοποιώντας ", is_highlight=False),
                TextSegment(
                    text="3 JK Flip-Flops",
                    is_highlight=True,
                    category="fsm",
                    tag_label="JK-FF",
                    badge_class="badge-fsm",
                    tooltip="Classification: Στοιχεία Μνήμης JK | Detection Clue: JK Flip-Flops | Application Rationale: Πίνακας διέγερσης: 0->0: (0,X), 0->1: (1,X), 1->0: (X,1), 1->1: (X,0).",
                ),
                TextSegment(text=".\n1. Κατασκευάστε τον πίνακα διεγέρσεων.\n2. Εξάγετε τις απλοποιημένες συναρτήσεις Jk, Kk.\n3. Εκτελέστε έλεγχο ", is_highlight=False),
                TextSegment(
                    text="αυτοδιόρθωσης (self-starting)",
                    is_highlight=True,
                    category="fsm",
                    tag_label="SELF-START",
                    badge_class="badge-fsm",
                    tooltip="Classification: Έλεγχος Αξιοπιστίας Υλικού | Detection Clue: Self-starting analysis | Application Rationale: Εξασφαλίζει ότι οι μη χρησιμοποιούμενες καταστάσεις 6 και 7 επιστρέφουν στον βρόχο.",
                ),
                TextSegment(text=" για τις μη χρησιμοποιούμενες καταστάσεις 6 και 7.", is_highlight=False),
            ],
            accent_border_color="var(--accent)",
        ),
        # Theme 4 Paragraph
        Paragraph(
            segments=[
                TextSegment(text="Θέμα 4: Περιγραφή Σύγχρονης Μηχανής Moore σε VHDL\n", is_highlight=False),
                TextSegment(text="Σχεδιάστε σύγχρονη FSM ", is_highlight=False),
                TextSegment(
                    text="μοντέλου Moore",
                    is_highlight=True,
                    category="fsm",
                    tag_label="MOORE-FSM",
                    badge_class="badge-fsm",
                    tooltip="Classification: Αρχιτεκτονική Moore FSM | Detection Clue: Moore Model | Application Rationale: Η έξοδος Z εξαρτάται αποκλειστικά από την παρούσα κατάσταση (glitch-free).",
                ),
                TextSegment(text=" η οποία αναγνωρίζει την ακολουθία ", is_highlight=False),
                TextSegment(
                    text="110 με επικάλυψη",
                    is_highlight=True,
                    category="fsm",
                    tag_label="SEQ-110",
                    badge_class="badge-fsm",
                    tooltip="Classification: Σειριακό Πρότυπο Ανίχνευσης | Detection Clue: 110 overlapping | Application Rationale: 4 καταστάσεις: S0 (reset), S1 ('1'), S2 ('11'), S3 ('110' με Z=1).",
                ),
                TextSegment(text=" σε σειριακή είσοδο X.\n1. Σχεδιάστε το διάγραμμα καταστάσεων Moore.\n2. Γράψτε πλήρη συνθέσιμο κώδικα VHDL ακολουθώντας το επαγγελματικό ", is_highlight=False),
                TextSegment(
                    text="πρότυπο δύο διεργασιών (two-process model)",
                    is_highlight=True,
                    category="vhdl",
                    tag_label="TWO-PROCESS",
                    badge_class="badge-vhdl",
                    tooltip="Classification: Βέλτιστη Πρακτική Σύνθεσης VHDL | Detection Clue: Two-process methodology | Application Rationale: 1η διεργασία: καταχωρητής με ασύγχρονο reset. 2η διεργασία: συνδυαστική λογική.",
                ),
                TextSegment(text=" με ασύγχρονη επαναφορά (asynchronous reset).", is_highlight=False),
            ],
            accent_border_color="var(--accent)",
        ),
    ]

    questions = [
        # Question 1: Hazards & Consensus
        ExamQuestion(
            question_number=1,
            title="Στατικοί Κίνδυνοι (Static-1 Hazards) & Θεώρημα Συναίνεσης",
            question_type="Theory Analysis & Circuit Design",
            prompt_text=(
                "Δίνεται η λογική συνάρτηση 3 μεταβλητών:\n"
                "$$F(A, B, C) = A \\cdot B + \\overline{A} \\cdot C$$\n"
                "1. Εξηγήστε τι είναι ο Στατικός Κίνδυνος 1 και δείξτε υπό ποιες συνθήκες εισόδων ($B=1, C=1$) "
                "και ποια μετάβαση ($A: 1 \\to 0$) εμφανίζεται παλμός σφάλματος λόγω καθυστέρησης $\\Delta t$ στον αντιστροφέα.\n"
                "2. Εντοπίστε την αιτία στον χάρτη Karnaugh.\n"
                "3. Εξαλείψτε τον κίνδυνο προσθέτοντας τον όρο συναίνεσης (consensus term) και αποδείξτε αλγεβρικά την ισοδυναμία."
            ),
            given_parameters=[
                GivenParameter(symbol="F", value="AB + \\overline{A}C", description="Αρχική συνάρτηση με κίνδυνο", category="param"),
                GivenParameter(symbol="B, C", value="B=1, \\; C=1", description="Σταθερές συνθήκες εισόδου", category="param"),
                GivenParameter(symbol="A", value="1 \\to 0", description="Μετάβαση εισόδου που προκαλεί glitch", category="param"),
                GivenParameter(symbol="\\Delta t", value="t_{pd\\_not}", description="Καθυστέρηση διάδοσης αντιστροφέα", category="param"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ανάλυση Χρονισμού και Δημιουργία Glitch (Static-1 Hazard)",
                    formula="F(t) = A(t) \\cdot 1 + \\overline{A}(t) \\cdot 1",
                    substitution="t \\in [t_0, t_0 + \\Delta t] \\implies A(t) = 0 \\quad \\text{και} \\quad \\overline{A}(t) = 0 \\implies F = 0 + 0 = 0",
                    result="\\text{Στιγμιαίος παλμός σφάλματος (glitch) } 1 \\to 0 \\to 1 \\text{ διάρκειας } \\Delta t",
                    rationale="Η πύλη AND(A, B) σβήνει αμέσως, αλλά η πύλη AND(A', C) αργεί να ανάψει κατά Δt λόγω του αντιστροφέα NOT.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Γεωμετρικός Εντοπισμός στον Χάρτη Karnaugh 3 Μεταβλητών",
                    formula="K(A, BC) \\quad \\text{με } A \\in \\{0, 1\\}, \\; BC \\in \\{00, 01, 11, 10\\}",
                    substitution=(
                        "m(7) = 111 \\in AB \\quad \\text{και} \\quad m(3) = 011 \\in \\overline{A}C. \\\\"
                        "Τα κελιά 7 και 3 είναι γειτονικά (διαφέρουν μόνο στο A), αλλά ανήκουν σε ξεχωριστούς κύβους!"
                    ),
                    result="\\text{Μη επικαλυπτόμενοι κύβοι μεταξύ λογικά γειτονικών minterms}",
                    rationale="Όποτε ένα σήμα μεταβαίνει μεταξύ δύο γειτονικών 1 που δεν περικλείονται σε κοινό πρωτεύοντα όρο, υπάρχει κίνδυνος.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Εφαρμογή Θεωρήματος Συναίνεσης (Consensus Theorem)",
                    formula="XY + \\overline{X}Z + YZ = XY + \\overline{X}Z",
                    substitution="X = A, \\; Y = B, \\; Z = C \\implies \\text{Όρος Συναίνεσης} = BC \\implies F_{hf} = AB + \\overline{A}C + BC",
                    result="F_{hazard\\_free} = AB + \\overline{A}C + BC",
                    rationale="Ο όρος BC καλύπτει ταυτόχρονα τα κελιά 3 και 7. Όταν B=1 και C=1, ο όρος BC=1 κρατά σταθερά την έξοδο στο 1.",
                ),
            ],
            final_answer="F_{hazard\\_free} = AB + \\overline{A}C + BC \\quad (\\text{Πλήρως απαλλαγμένη από Static-1 Hazard})",
            detailed_justification=(
                "Η προσθήκη του πλεονάζοντος όρου BC (consensus term) γεφυρώνει τα γειτονικά κελιά m(3) και m(7) στον χάρτη Karnaugh. "
                "Όταν B=1 και C=1, ο όρος BC διατηρεί την έξοδο στο 1 ανεξάρτητα από τις μεταβάσεις του A και τις καθυστερήσεις "
                "του αντιστροφέα, εξαλείφοντας πλήρως τον στατικό κίνδυνο χωρίς να αλλοιώνει τον πίνακα αληθείας."
            ),
            common_pitfalls=[
                "Θεώρηση ότι η ελαχιστοποίηση SOP είναι πάντα απαλλαγμένη από κινδύνους: η ελάχιστη μορφή συχνά περιέχει hazards!",
                "Λανθασμένη κατεύθυνση μετάβασης: για static-1 hazard η έξοδος πρέπει θεωρητικά να είναι 1 και στιγμιαία να πέφτει σε 0.",
            ],
            related_theory_topic="Ενότητα 4: Απλοποίηση Boole, Χάρτες K-Map & Κίνδυνοι (Hazards)",
        ),
        # Question 2: MSI Synthesis
        ExamQuestion(
            question_number=2,
            title="Σύνθεση Συνδυαστικών Κυκλωμάτων με Πολυπλέκτη 8:1 & Αποκωδικοποιητή 3:8",
            question_type="MSI Logic Design",
            prompt_text=(
                "1. Υλοποιήστε τη συνάρτηση $F(A, B, C, D) = \\sum m(1, 3, 4, 11, 12, 13, 14, 15)$ χρησιμοποιώντας "
                "έναν πολυπλέκτη 8-σε-1 (74151) με γραμμές επιλογής $S_2 = A, S_1 = B, S_0 = C$ και εισόδους δεδομένων $I_0 - I_7$.\n"
                "2. Υλοποιήστε τη συνάρτηση $G(A, B, C) = \\sum m(0, 2, 6, 7)$ με αποκωδικοποιητή 3:8 ενεργών χαμηλών εξόδων και μία πύλη NAND."
            ),
            given_parameters=[
                GivenParameter(symbol="F", value="\\sum m(1, 3, 4, 11, 12, 13, 14, 15)", description="Συνάρτηση 4 μεταβλητών για MUX", category="param"),
                GivenParameter(symbol="S_2, S_1, S_0", value="A, B, C", description="Γραμμές διεύθυνσης πολυπλέκτη", category="param"),
                GivenParameter(symbol="G", value="\\sum m(0, 2, 6, 7)", description="Συνάρτηση 3 μεταβλητών για Decoder", category="param"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ανάλυση Εισόδων MUX 8:1 ανά Ζεύγος Minterms (D=0, D=1)",
                    formula="I_k = f(m_{2k}, m_{2k+1}) \\quad \\text{για } k \\in [0, 7]",
                    substitution=(
                        "k=0 (ABC=000): m(0)=0, m(1)=1 \\implies I_0 = D \\\\"
                        "k=1 (ABC=001): m(2)=0, m(3)=1 \\implies I_1 = D \\\\"
                        "k=2 (ABC=010): m(4)=1, m(5)=0 \\implies I_2 = \\overline{D} \\\\"
                        "k=3 (ABC=011): m(6)=0, m(7)=0 \\implies I_3 = 0 \\\\"
                        "k=4 (ABC=100): m(8)=0, m(9)=0 \\implies I_4 = 0 \\\\"
                        "k=5 (ABC=101): m(10)=0, m(11)=1 \\implies I_5 = D \\\\"
                        "k=6 (ABC=110): m(12)=1, m(13)=1 \\implies I_6 = 1 \\\\"
                        "k=7 (ABC=111): m(14)=1, m(15)=1 \\implies I_7 = 1"
                    ),
                    result="I_0=D, \\; I_1=D, \\; I_2=\\overline{D}, \\; I_3=0, \\; I_4=0, \\; I_5=D, \\; I_6=1, \\; I_7=1",
                    rationale="Κάθε γραμμή επιλογής ABC απομονώνει δύο διαδοχικά minterms. Η συμπεριφορά της εξόδου ανάγεται σε D, D', 0 ή 1.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Σύνθεση Συνάρτησης G με Αποκωδικοποιητή 3:8 (Active-Low) & NAND",
                    formula="G = m_0 + m_2 + m_6 + m_7 = \\overline{\\overline{m_0} \\cdot \\overline{m_2} \\cdot \\overline{m_6} \\cdot \\overline{m_7}}",
                    substitution="\\overline{Y_k} = \\overline{m_k} \\implies G = \\overline{\\overline{Y_0} \\cdot \\overline{Y_2} \\cdot \\overline{Y_6} \\cdot \\overline{Y_7}} = \\text{NAND}\\Big(\\overline{Y_0}, \\overline{Y_2}, \\overline{Y_6}, \\overline{Y_7}\\Big)",
                    result="G = \\text{NAND}(\\overline{Y_0}, \\overline{Y_2}, \\overline{Y_6}, \\overline{Y_7})",
                    rationale="Οι ενεργές χαμηλές έξοδοι του αποκωδικοποιητή είναι τα συμπληρώματα των minterms. Μια πύλη NAND υλοποιεί άμεσα το άθροισμα!",
                ),
            ],
            final_answer="MUX: (I_0..I_7) = (D, D, \\overline{D}, 0, 0, D, 1, 1) • Decoder: NAND(\\overline{Y_0}, \\overline{Y_2}, \\overline{Y_6}, \\overline{Y_7})",
            detailed_justification=(
                "Οι πολυπλέκτες και οι αποκωδικοποιητές αποτελούν καθολικές συνδυαστικές δομές MSI. Ένας MUX 8:1 με n-1 γραμμές "
                "επιλογής μπορεί να υλοποιήσει οποιαδήποτε συνάρτηση n μεταβλητών χρησιμοποιώντας την τελευταία μεταβλητή "
                "ως είσοδο δεδομένων. Αντίστοιχα, ένας αποκωδικοποιητής active-low παράγει όλα τα maxterms (ή τα αρνημένα minterms), "
                "επιτρέποντας τη σύνθεση οποιουδήποτε αθροίσματος με μία μόνο πύλη NAND (θεώρημα De Morgan)."
            ),
            common_pitfalls=[
                "Λανθασμένη σειρά των γραμμών επιλογής (π.χ. σύνδεση S2=C αντί για S2=A), προκαλώντας ανακάτεμα των minterms.",
                "Χρήση πύλης AND αντί για NAND στις ενεργές χαμηλές εξόδους του αποκωδικοποιητή.",
            ],
            related_theory_topic="Ενότητα 6: Αποκωδικοποιητές, Πολυπλέκτες & Σύνθεση MSI",
        ),
        # Question 3: Mod-6 Counter
        ExamQuestion(
            question_number=3,
            title="Σχεδίαση Σύγχρονου Μετρητή Modulo-6 με JK Flip-Flops & Αυτοδιόρθωση",
            question_type="Counter & Sequential Design",
            prompt_text=(
                "Σχεδιάστε σύγχρονο μετρητή που μετρά την ακολουθία $0 \\to 1 \\to 2 \\to 3 \\to 4 \\to 5 \\to 0$ "
                "χρησιμοποιώντας 3 JK Flip-Flops ($Q_2, Q_1, Q_0$).\n"
                "1. Κατασκευάστε τον πίνακα διεγέρσεων.\n"
                "2. Εξάγετε τις ελάχιστες εξισώσεις $J_k, K_k$.\n"
                "3. Ελέγξτε αν ο μετρητής είναι αυτοδιορθούμενος (self-starting) για τις μη χρησιμοποιούμενες καταστάσεις 6 και 7."
            ),
            given_parameters=[
                GivenParameter(symbol="\\text{States}", value="0, 1, 2, 3, 4, 5", description="Έγκυρες καταστάσεις μέτρησης", category="param"),
                GivenParameter(symbol="\\text{Unused}", value="6 (110), \\; 7 (111)", description="Αχρησιμοποίητες καταστάσεις", category="param"),
                GivenParameter(symbol="\\text{Target}", value="3 \\times \\text{JK Flip-Flops}", description="Στοιχεία μνήμης", category="param"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Πίνακας Μεταβάσεων και Διεγέρσεων JK",
                    formula="Q \\to Q^+ \\implies (J, K) \\in \\{(0, X), (1, X), (X, 1), (X, 0)\\}",
                    substitution=(
                        "0 (000) \\to 1 (001): J_2=0, K_2=X; \\; J_1=0, K_1=X; \\; J_0=1, K_0=X \\\\"
                        "1 (001) \\to 2 (010): J_2=0, K_2=X; \\; J_1=1, K_1=X; \\; J_0=X, K_0=1 \\\\"
                        "2 (010) \\to 3 (011): J_2=0, K_2=X; \\; J_1=X, K_1=0; \\; J_0=1, K_0=X \\\\"
                        "3 (011) \\to 4 (100): J_2=1, K_2=X; \\; J_1=X, K_1=1; \\; J_0=X, K_0=1 \\\\"
                        "4 (100) \\to 5 (101): J_2=X, K_2=0; \\; J_1=0, K_1=X; \\; J_0=1, K_0=X \\\\"
                        "5 (101) \\to 0 (000): J_2=X, K_2=1; \\; J_1=0, K_1=X; \\; J_0=X, K_0=1"
                    ),
                    result="\\text{Πλήρης πίνακας διεγέρσεων 6 καταστάσεων}",
                    rationale="Η εφαρμογή του πίνακα διέγερσης JK παράγει πλήθος don't cares (X) που επιτρέπουν δραστική απλοποίηση.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ελαχιστοποίηση με Χάρτες Karnaugh",
                    formula="K(Q_2, Q_1, Q_0) \\quad \\text{με } d(6, 7) = X",
                    substitution=(
                        "J_0 = 1, \\quad K_0 = 1 \\\\"
                        "J_1 = \\overline{Q_2} \\cdot Q_0, \\quad K_1 = Q_0 \\\\"
                        "J_2 = Q_1 \\cdot Q_0, \\quad K_2 = Q_0"
                    ),
                    result="J_0=1, K_0=1; \\quad J_1=\\overline{Q_2}Q_0, K_1=Q_0; \\quad J_2=Q_1Q_0, K_2=Q_0",
                    rationale="Παρατηρούμε ότι K0=1, ενώ K1=K2=Q0, μειώνοντας δραστικά τις απαιτούμενες εξωτερικές πύλες!",
                ),
                CalculationStep(
                    step_number=3,
                    title="Ανάλυση Αυτοδιόρθωσης (Self-Starting Analysis)",
                    formula="Q^+ = J \\overline{Q} + \\overline{K} Q",
                    substitution=(
                        "\\text{Από κατάσταση } 6 (110): J_0=1, K_0=1 \\implies Q_0^+=1; \\; J_1=0, K_1=0 \\implies Q_1^+=1; \\; J_2=0, K_2=0 \\implies Q_2^+=1 \\implies \\mathbf{111 (7)} \\\\"
                        "\\text{Από κατάσταση } 7 (111): J_0=1, K_0=1 \\implies Q_0^+=0; \\; J_1=0, K_1=1 \\implies Q_1^+=0; \\; J_2=1, K_2=1 \\implies Q_2^+=0 \\implies \\mathbf{000 (0)}"
                    ),
                    result="6 (110) \\to 7 (111) \\to 0 (000) \\implies \\text{Πλήρης Αυτοδιόρθωση}",
                    rationale="Και οι δύο αχρησιμοποίητες καταστάσεις οδηγούν αυτόματα στον κύριο βρόχο μέτρησης. Δεν υπάρχει κίνδυνος εγκλωβισμού.",
                ),
            ],
            final_answer="J_0=K_0=1, \\; J_1=\\overline{Q_2}Q_0, \\; K_1=Q_0, \\; J_2=Q_1Q_0, \\; K_2=Q_0 \\quad (\\text{Self-Starting})",
            detailed_justification=(
                "Ο σχεδιασμός σύγχρονων μετρητών με JK Flip-Flops εκμεταλλεύεται τις συνθήκες don't care της λειτουργίας toggle/hold. "
                "Ο έλεγχος αυτοδιόρθωσης απέδειξε ότι αν κατά την εκκίνηση του συστήματος (power-up) τα Flip-Flops βρεθούν "
                "στην κατάσταση 110 ή 111, ο μετρητής θα επιστρέψει αυτόνομα στην κατάσταση 000 εντός 2 κύκλων ρολογιού, "
                "εξασφαλίζοντας μέγιστη αξιοπιστία χωρίς επιπλέον λογική κυκλώματος reset."
            ),
            common_pitfalls=[
                "Υπόθεση ότι ο μετρητής είναι αυτοδιορθούμενος χωρίς αναλυτικό υπολογισμό της επόμενης κατάστασης των unused states.",
                "Σύγχυση μεταξύ σύγχρονου (κοινό ρολόι) και ασύγχρονου (ripple) μετρητή.",
            ],
            related_theory_topic="Ενότητα 8: Καταχωρητές, Μετρητές & Σύγχρονα Ακολουθιακά",
        ),
        # Question 4: Moore FSM in VHDL
        ExamQuestion(
            question_number=4,
            title="Περιγραφή Σύγχρονης Μηχανής Moore σε VHDL (Two-Process Model)",
            question_type="VHDL Hardware Synthesis",
            prompt_text=(
                "Σχεδιάστε ανιχνευτή ακολουθίας για την ακολουθία `110` με επικάλυψη χρησιμοποιώντας μοντέλο Moore.\n"
                "1. Σχεδιάστε το διάγραμμα καταστάσεων Moore.\n"
                "2. Γράψτε πλήρη συνθέσιμο κώδικα VHDL εφαρμόζοντας το πρότυπο δύο διεργασιών (two-process model) "
                "με ασύγχρονο reset."
            ),
            given_parameters=[
                GivenParameter(symbol="\\text{Sequence}", value="110", description="Ακολουθία-στόχος ανίχνευσης", category="param"),
                GivenParameter(symbol="\\text{Model}", value="\\text{Moore}", description="Έξοδος Z συναρτήσει μόνο της κατάστασης", category="param"),
                GivenParameter(symbol="\\text{Reset}", value="\\text{Asynchronous Active-High}", description="Σήμα επαναφοράς", category="param"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ορισμός Καταστάσεων Μηχανής Moore",
                    formula="S_k / Z \\quad \\text{με } S_k \\in \\{S_0, S_1, S_2, S_3\\}",
                    substitution=(
                        "S_0 / 0: \\text{Reset / Κανένα έγκυρο bit} \\\\"
                        "S_1 / 0: \\text{Έχει ανιχνευθεί '1'} \\\\"
                        "S_2 / 0: \\text{Έχουν ανιχνευθεί '11'} \\\\"
                        "S_3 / 1: \\text{Έχει ανιχνευθεί πλήρως '110'} (Z=1)"
                    ),
                    result="4 \\text{ καταστάσεις Moore } \\implies \\text{Τύπος } type \\; state\\_type \\; is \\; (S0, S1, S2, S3)",
                    rationale="Στο μοντέλο Moore η έξοδος Z=1 ανήκει στην κατάσταση S3, εξασφαλίζοντας έξοδο συγχρονισμένη και χωρίς ακμές θορύβου.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Δομή Δύο Διεργασιών (Two-Process Model) στη VHDL",
                    formula="\\text{Process 1 (Clocked Register) } + \\text{ Process 2 (Combinational Logic)}",
                    substitution=(
                        "Process 1: if reset='1' then current_state <= S0; elsif rising_edge(clk) then current_state <= next_state; \\\\"
                        "Process 2: process(current_state, x) case current_state is ... when S3 => z <= '1'; ..."
                    ),
                    result="\\text{Απόλυτος διαχωρισμός στοιχείων μνήμης και συνδυαστικής λογικής}",
                    rationale="Το two-process model αποτελεί το βιομηχανικό πρότυπο σύνθεσης RTL, αποτρέποντας ασυμφωνίες προσομοίωσης.",
                ),
            ],
            final_answer="Πλήρης, συνθέσιμος κώδικας VHDL Moore FSM Two-Process Architecture.",
            detailed_justification=(
                "Στο μοντέλο Moore, η έξοδος αποκωδικοποιείται αποκλειστικά από την παρούσα κατάσταση (Z <= '1' μόνο στο S3), "
                "γεγονός που αποτρέπει τη διάδοση spikes ή glitches από τις εισόδους προς την έξοδο. Η μέθοδος των δύο "
                "διεργασιών διασφαλίζει ότι ο καταχωρητής κατάστασης συντίθεται με ιδανικά D Flip-Flops με ασύγχρονη "
                "είσοδο clear, ενώ η συνδυαστική λογική συντίθεται σε καθαρά LUTs χωρίς ανεπιθύμητα latches."
            ),
            common_pitfalls=[
                "Ελλιπής ανάθεση του z <= '0' σε όλους τους κλάδους της συνδυαστικής διεργασίας, οδηγώντας σε ανεπιθύμητο latch.",
                "Σύγχυση μεταξύ σύγχρονου και ασύγχρονου reset: το ασύγχροφο reset ελέγχεται ΠΡΙΝ από το rising_edge(clk).",
            ],
            related_theory_topic="Ενότητα 11: Προηγμένη VHDL & Σχεδίαση FSM",
        ),
    ]

    justifications = [
        DesignJustification(
            title="Θεώρημα Συναίνεσης & Εξάλειψη Κινδύνων",
            category="Boolean Theorem",
            description="Η προσθήκη του όρου συναίνεσης BC εξαλείφει το Static-1 Hazard χωρίς να μεταβάλλει τον πίνακα αληθείας.",
            rationale="Αποτρέπει παλμούς σφάλματος που θα μπορούσαν να προκαλέσουν εσφαλμένο trigger σε ασύγχρονες εισόδους Flip-Flops.",
        ),
        DesignJustification(
            title="Καθολική Σύνθεση με Πολυπλέκτες & Αποκωδικοποιητές",
            category="Hardware Efficiency",
            description="Κάθε λογική συνάρτηση n μεταβλητών υλοποιείται με έναν MUX 2^(n-1):1 χωρίς επιπλέον πύλες.",
            rationale="Μειώνει τον αριθμό των ολοκληρωμένων κυκλωμάτων στην πλακέτα και τυποποιεί την καλωδίωση διαύλων.",
        ),
        DesignJustification(
            title="Αυτοδιόρθωση Μετρητών (Self-Starting)",
            category="FSM Timing",
            description="Όλες οι μη χρησιμοποιούμενες καταστάσεις πρέπει να οδηγούν πίσω στον έγκυρο κύκλο μέτρησης.",
            rationale="Αποτρέπει το μόνιμο κόλλημα (deadlock) του συστήματος σε περίπτωση θορύβου ή τυχαίας αρχικοποίησης κατά το power-up.",
        ),
        DesignJustification(
            title="Πρότυπο Δύο Διεργασιών στη VHDL (Two-Process FSM)",
            category="VHDL Idiom",
            description="Διαχωρίζει τα Flip-Flops κατάστασης από τη συνδυαστική λογική μετάβασης και εξόδου.",
            rationale="Εξασφαλίζει βέλτιστη αντιστοίχιση στα CLBs και τα Flip-Flops του FPGA με άριστο στατικό χρονισμό (timing closure).",
        ),
    ]

    # SVG for Modulo-6 Counter / FSM State Transition Graph
    mod6_svg = generateMod6CounterSvg()

    # Verification Code
    python_solution = '''# Python 3 Logic Verification Script
# Synthetic Exam 02: Digital Electronics Solutions Check

def verify_hazard_elimination():
    """Verifies that F = AB + A\'C + BC is logically identical to F = AB + A\'C."""
    for A in (0, 1):
        for B in (0, 1):
            for C in (0, 1):
                f_orig = (A and B) or ((not A) and C)
                f_hf = (A and B) or ((not A) and C) or (B and C)
                assert f_orig == f_hf, f"Mismatch at A={A}, B={B}, C={C}"
    print("Theme 1 Check: Consensus term BC preserves Boolean equivalence perfectly!")

def verify_mux_synthesis():
    """Verifies 8:1 MUX synthesis of F = sum m(1, 3, 4, 11, 12, 13, 14, 15)."""
    minterms = {1, 3, 4, 11, 12, 13, 14, 15}
    # Inputs: I0=D, I1=D, I2=~D, I3=0, I4=0, I5=D, I6=1, I7=1
    for val in range(16):
        A = (val >> 3) & 1
        B = (val >> 2) & 1
        C = (val >> 1) & 1
        D = val & 1
        
        sel = (A << 2) | (B << 1) | C
        mux_inputs = [D, D, 1 - D, 0, 0, D, 1, 1]
        mux_out = mux_inputs[sel]
        
        expected = 1 if val in minterms else 0
        assert mux_out == expected, f"MUX mismatch at {val}"
    print("Theme 2 Check: MUX 8:1 reproduces exact function output across all 16 minterms!")

def verify_mod6_self_starting():
    """Verifies Modulo-6 JK Counter transitions and self-starting from states 6 and 7."""
    def next_state(q2, q1, q0):
        j0, k0 = 1, 1
        j1 = (1 - q2) & q0
        k1 = q0
        j2 = q1 & q0
        k2 = q0
        
        # JK Flip-Flop excitation rule: Q+ = J*(~Q) + (~K)*Q
        q0_next = (j0 and (not q0)) or ((not k0) and q0)
        q1_next = (j1 and (not q1)) or ((not k1) and q1)
        q2_next = (j2 and (not q2)) or ((not k2) and q2)
        return int(q2_next), int(q1_next), int(q0_next)
    
    # Check regular sequence: 0->1->2->3->4->5->0
    curr = (0, 0, 0)
    for expected in [(0,0,1), (0,1,0), (0,1,1), (1,0,0), (1,0,1), (0,0,0)]:
        curr = next_state(*curr)
        assert curr == expected, f"Sequence error: {curr} != {expected}"
        
    # Check self-starting from 6 (110) and 7 (111)
    assert next_state(1, 1, 0) == (1, 1, 1), "State 6 must transition to 7"
    assert next_state(1, 1, 1) == (0, 0, 0), "State 7 must transition to 0"
    print("Theme 3 Check: Modulo-6 sequence and self-starting property verified 100%!")

if __name__ == "__main__":
    verify_hazard_elimination()
    verify_mux_synthesis()
    verify_mod6_self_starting()
    print("All Synthetic Exam 02 derivations verified cleanly!")
'''

    return Scenario(
        id="synth_exam_02_msi_counters_fsm",
        title="Συνθετικό Θέμα 02: Hazards, MSI MUX/Decoder, Μετρητής Mod-6, Moore FSM",
        subtitle="Πλήρες Εξεταστικό Θέμα: Ανάλυση Κινδύνων, Σύνθεση MSI, JK Μετρητές, VHDL Two-Process",
        course_tag="Synthetic Exam",
        duration_info="2.5 Ώρες • 4 Θέματα • 10 Μονάδες",
        paragraphs=paragraphs,
        questions=questions,
        diagram_svg_custom=mod6_svg,
        justifications=justifications,
        solution_code=python_solution,
    )


def generateMod6CounterSvg() -> str:
    """Generates the interactive SVG state transition diagram for the Modulo-6 Counter.

    Returns:
        str: Scalable vector graphic markup.
    """
    return """
    <svg width="860" height="420" viewBox="0 0 860 420" xmlns="http://www.w3.org/2000/svg" class="select-none">
        <defs>
            <marker id="arrow-acc" markerWidth="10" markerHeight="10" refX="8" refY="3.5" orient="auto">
                <polygon points="0 0, 10 3.5, 0 7" fill="var(--accent)" />
            </marker>
            <marker id="arrow-green" markerWidth="10" markerHeight="10" refX="8" refY="3.5" orient="auto">
                <polygon points="0 0, 10 3.5, 0 7" fill="var(--green-ok)" />
            </marker>
            <marker id="arrow-red" markerWidth="10" markerHeight="10" refX="8" refY="3.5" orient="auto">
                <polygon points="0 0, 10 3.5, 0 7" fill="var(--red-err)" />
            </marker>
        </defs>

        <!-- Center of circular layout: (380, 210), Radius = 135 -->
        <!-- S0: (380, 75) -->
        <!-- S1: (497, 142) -->
        <!-- S2: (497, 278) -->
        <!-- S3: (380, 345) -->
        <!-- S4: (263, 278) -->
        <!-- S5: (263, 142) -->

        <!-- Main Counter Cycle Transitions (Curved Arcs) -->
        <!-- S0 -> S1 -->
        <path d="M 415,95 C 460,105 475,115 485,130" fill="none" stroke="var(--accent)" stroke-width="3" marker-end="url(#arrow-acc)" />
        <!-- S1 -> S2 -->
        <path d="M 505,185 C 520,210 520,225 505,245" fill="none" stroke="var(--accent)" stroke-width="3" marker-end="url(#arrow-acc)" />
        <!-- S2 -> S3 -->
        <path d="M 480,295 C 460,320 430,335 410,340" fill="none" stroke="var(--accent)" stroke-width="3" marker-end="url(#arrow-acc)" />
        <!-- S3 -> S4 -->
        <path d="M 350,340 C 330,335 300,320 280,295" fill="none" stroke="var(--accent)" stroke-width="3" marker-end="url(#arrow-acc)" />
        <!-- S4 -> S5 -->
        <path d="M 255,245 C 240,225 240,210 255,185" fill="none" stroke="var(--accent)" stroke-width="3" marker-end="url(#arrow-acc)" />
        <!-- S5 -> S0 -->
        <path d="M 275,130 C 285,115 300,105 345,95" fill="none" stroke="var(--accent)" stroke-width="3" marker-end="url(#arrow-acc)" />

        <!-- Self-Starting Recovery Paths (From 6 -> 7 -> 0) -->
        <!-- Unused State 6 (110) at (710, 130) -->
        <!-- Unused State 7 (111) at (710, 290) -->
        <path d="M 710,165 L 710,245" fill="none" stroke="var(--red-err)" stroke-width="2.5" stroke-dasharray="5 5" marker-end="url(#arrow-red)" />
        <text x="735" y="210" text-anchor="middle" font-family="Outfit, sans-serif" font-size="11" font-weight="bold" fill="var(--red-err)">CLK</text>

        <!-- 7 -> S0 Recovery -->
        <path d="M 675,290 C 600,290 480,180 415,85" fill="none" stroke="var(--green-ok)" stroke-width="3" stroke-dasharray="6 4" marker-end="url(#arrow-green)" />
        <text x="590" y="215" text-anchor="middle" font-family="Outfit, sans-serif" font-size="12" font-weight="bold" fill="var(--green-ok)">Αυτοδιόρθωση: 7 → 0</text>

        <!-- State Nodes -->
        <!-- State 0 (000) -->
        <g transform="translate(380, 75)">
            <circle r="34" fill="var(--svg-fill)" stroke="var(--accent)" stroke-width="3.5" />
            <text x="0" y="-3" text-anchor="middle" font-family="Outfit, sans-serif" font-weight="bold" font-size="15" fill="var(--text-1)">0</text>
            <text x="0" y="15" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="11" fill="var(--text-3)">000</text>
        </g>
        <!-- State 1 (001) -->
        <g transform="translate(497, 142)">
            <circle r="34" fill="var(--svg-fill)" stroke="var(--accent)" stroke-width="3.5" />
            <text x="0" y="-3" text-anchor="middle" font-family="Outfit, sans-serif" font-weight="bold" font-size="15" fill="var(--text-1)">1</text>
            <text x="0" y="15" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="11" fill="var(--text-3)">001</text>
        </g>
        <!-- State 2 (010) -->
        <g transform="translate(497, 278)">
            <circle r="34" fill="var(--svg-fill)" stroke="var(--accent)" stroke-width="3.5" />
            <text x="0" y="-3" text-anchor="middle" font-family="Outfit, sans-serif" font-weight="bold" font-size="15" fill="var(--text-1)">2</text>
            <text x="0" y="15" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="11" fill="var(--text-3)">010</text>
        </g>
        <!-- State 3 (011) -->
        <g transform="translate(380, 345)">
            <circle r="34" fill="var(--svg-fill)" stroke="var(--accent)" stroke-width="3.5" />
            <text x="0" y="-3" text-anchor="middle" font-family="Outfit, sans-serif" font-weight="bold" font-size="15" fill="var(--text-1)">3</text>
            <text x="0" y="15" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="11" fill="var(--text-3)">011</text>
        </g>
        <!-- State 4 (100) -->
        <g transform="translate(263, 278)">
            <circle r="34" fill="var(--svg-fill)" stroke="var(--accent)" stroke-width="3.5" />
            <text x="0" y="-3" text-anchor="middle" font-family="Outfit, sans-serif" font-weight="bold" font-size="15" fill="var(--text-1)">4</text>
            <text x="0" y="15" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="11" fill="var(--text-3)">100</text>
        </g>
        <!-- State 5 (101) -->
        <g transform="translate(263, 142)">
            <circle r="34" fill="var(--svg-fill)" stroke="var(--accent)" stroke-width="3.5" />
            <text x="0" y="-3" text-anchor="middle" font-family="Outfit, sans-serif" font-weight="bold" font-size="15" fill="var(--text-1)">5</text>
            <text x="0" y="15" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="11" fill="var(--text-3)">101</text>
        </g>

        <!-- Unused State 6 (110) -->
        <g transform="translate(710, 130)">
            <circle r="32" fill="var(--surface-2)" stroke="var(--red-err)" stroke-width="2.5" stroke-dasharray="4 3" />
            <text x="0" y="-3" text-anchor="middle" font-family="Outfit, sans-serif" font-weight="bold" font-size="14" fill="var(--red-err)">6</text>
            <text x="0" y="15" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="11" fill="var(--text-3)">110</text>
            <text x="0" y="48" text-anchor="middle" font-family="Outfit, sans-serif" font-size="10" fill="var(--red-err)" class="de-diagram-detail">Unused (d)</text>
        </g>

        <!-- Unused State 7 (111) -->
        <g transform="translate(710, 290)">
            <circle r="32" fill="var(--surface-2)" stroke="var(--red-err)" stroke-width="2.5" stroke-dasharray="4 3" />
            <text x="0" y="-3" text-anchor="middle" font-family="Outfit, sans-serif" font-weight="bold" font-size="14" fill="var(--red-err)">7</text>
            <text x="0" y="15" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="11" fill="var(--text-3)">111</text>
            <text x="0" y="48" text-anchor="middle" font-family="Outfit, sans-serif" font-size="10" fill="var(--red-err)" class="de-diagram-detail">Unused (d)</text>
        </g>

        <!-- Legend Overlay in SVG -->
        <g class="de-diagram-detail" transform="translate(180, 390)">
            <rect x="0" y="0" width="500" height="24" rx="6" fill="var(--surface-2)" stroke="var(--border)" />
            <text x="250" y="16" text-anchor="middle" font-family="Outfit, sans-serif" font-size="11" fill="var(--text-2)">
                Κύκλος Modulo-6 (Πορτοκαλί) • Αυτοδιόρθωση: 6 → 7 → 0 (Κόκκινο / Πράσινο διακεκομμένο) • Μηδενικός κίνδυνος Lockup
            </text>
        </g>
    </svg>
    """
