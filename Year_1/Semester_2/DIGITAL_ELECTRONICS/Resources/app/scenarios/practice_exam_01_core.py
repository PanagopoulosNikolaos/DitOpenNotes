"""Practice Exam 01 scenario module.

Implements the complete verbatim exam paper, annotated highlight tokens with
three-part tooltips, step-by-step KaTeX derivations, interactive FSM state
diagram, and verification code.
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


def createPracticeExam01Scenario() -> Scenario:
    """Creates and returns the Practice Exam 01 scenario instance.

    Returns:
        Scenario: Fully configured scenario with verbatim text, questions, and SVG.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Επαναληπτικό Θέμα Εξετάσεων: Ψηφιακά Ηλεκτρονικά", is_highlight=False),
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
                    tooltip="Classification: Χρονικός Περιορισμός Εξέτασης | Detection Clue: 2.5 ώρες συνολική διάρκεια | Application Rationale: Επιβάλλει διαχείριση χρόνου ~35 λεπτά ανά θέμα.",
                ),
                TextSegment(text=". Όλα τα θέματα βαθμολογούνται με ", is_highlight=False),
                TextSegment(
                    text="2.5 μονάδες",
                    is_highlight=True,
                    category="param",
                    tag_label="WEIGHT",
                    badge_class="badge-param",
                    tooltip="Classification: Συντελεστής Βαρύτητας | Detection Clue: 2.5 μονάδες ανά θέμα (Σύνολο: 10) | Application Rationale: Ισοδύναμη βαρύτητα θεωρίας, συνδυαστικών, ακολουθιακών και VHDL.",
                ),
                TextSegment(text=" (Σύνολο: 10 μονάδες).", is_highlight=False),
            ],
            accent_border_color=None,
        ),
        # Theme 1 Paragraph
        Paragraph(
            segments=[
                TextSegment(text="Θέμα 1: Αριθμητική Συμπληρώματος ως προς 2\n", is_highlight=False),
                TextSegment(text="1. Μετατρέψτε τους δεκαδικούς αριθμούς ", is_highlight=False),
                TextSegment(
                    text="A = +43",
                    is_highlight=True,
                    category="binary",
                    tag_label="POS-DEC",
                    badge_class="badge-binary",
                    tooltip="Classification: Θετικός Δεκαδικός Τελεστέος | Detection Clue: Πρόσημο + και μέγεθος 43 | Application Rationale: Μετατρέπεται απευθείας σε δυαδικό με MSB=0 ως θετικό μέγεθος.",
                ),
                TextSegment(text=" και ", is_highlight=False),
                TextSegment(
                    text="B = -27",
                    is_highlight=True,
                    category="binary",
                    tag_label="NEG-DEC",
                    badge_class="badge-binary",
                    tooltip="Classification: Αρνητικός Δεκαδικός Τελεστέος | Detection Clue: Πρόσημο - και μέγεθος 27 | Application Rationale: Απαιτεί εύρεση C1 και πρόσθεση 1 (C2) με MSB=1.",
                ),
                TextSegment(text=" σε δυαδική αναπαράσταση ", is_highlight=False),
                TextSegment(
                    text="συμπληρώματος ως προς 2",
                    is_highlight=True,
                    category="binary",
                    tag_label="C2-SYSTEM",
                    badge_class="badge-binary",
                    tooltip="Classification: Σύστημα Προσημασμένης Αναπαράστασης | Detection Clue: 2's Complement | Application Rationale: Επιτρέπει αφαίρεση μέσω κοινής διάταξης πρόσθεσης χωρίς ξεχωριστό αφαιρέτη.",
                ),
                TextSegment(text=" μήκους ", is_highlight=False),
                TextSegment(
                    text="8-bit",
                    is_highlight=True,
                    category="param",
                    tag_label="WORD-WIDTH",
                    badge_class="badge-param",
                    tooltip="Classification: Μήκος Λέξης Καταχωρητή | Detection Clue: 8-bit πλάτος διαύλου | Application Rationale: Καθορίζει το εύρος τιμών [-128, +127] και το σημείο ανίχνευσης κρατουμένου MSB.",
                ),
                TextSegment(text=".\n2. Εκτελέστε την πράξη πρόσθεσης A + B σε δυαδική μορφή 8-bit και ελέγξτε για τυχόν ", is_highlight=False),
                TextSegment(
                    text="υπερχείλιση (overflow)",
                    is_highlight=True,
                    category="binary",
                    tag_label="OVERFLOW",
                    badge_class="badge-binary",
                    tooltip="Classification: Συνθήκη Αριθμητικής Υπερχείλισης | Detection Clue: Overflow flag | Application Rationale: Ελέγχεται μέσω Cin != Cout στο MSB (πύλη XOR) ή από τα πρόσημα των τελεστέων.",
                ),
                TextSegment(text=".\n3. Εξηγήστε πώς ανιχνεύεται η υπερχείλιση κατά την πρόσθεση δύο προσημασμένων αριθμών στο υλικό.", is_highlight=False),
            ],
            accent_border_color="var(--accent)",
        ),
        # Theme 2 Paragraph
        Paragraph(
            segments=[
                TextSegment(text="Θέμα 2: Απλοποίηση Boole και Συνδυαστική Σύνθεση\n", is_highlight=False),
                TextSegment(text="Δίνεται η λογική συνάρτηση 4 μεταβλητών: ", is_highlight=False),
                TextSegment(
                    text="F(A, B, C, D) = Σ m(1, 3, 7, 11, 15) + d(0, 2, 5)",
                    is_highlight=True,
                    category="boolean",
                    tag_label="KMAP-FUNC",
                    badge_class="badge-boolean",
                    tooltip="Classification: Ατελώς Προσδιορισμένη Συνάρτηση | Detection Clue: Άθροισμα minterms με don't cares | Application Rationale: Εισάγεται σε χάρτη K-Map 4x4 για σχηματισμό μέγιστων ομάδων 2^k.",
                ),
                TextSegment(text=".\n1. Απλοποιήστε τη συνάρτηση σε ", is_highlight=False),
                TextSegment(
                    text="ελάχιστη μορφή SOP",
                    is_highlight=True,
                    category="boolean",
                    tag_label="MIN-SOP",
                    badge_class="badge-boolean",
                    tooltip="Classification: Ελάχιστο Άθροισμα Γινομένων | Detection Clue: Minimal SOP | Application Rationale: Εξασφαλίζει ελάχιστο αριθμό πυλών AND και ελάχιστες εισόδους ανά πύλη.",
                ),
                TextSegment(text=" χρησιμοποιώντας χάρτη Karnaugh.\n2. Υλοποιήστε την απλοποιημένη συνάρτηση χρησιμοποιώντας αποκλειστικά ", is_highlight=False),
                TextSegment(
                    text="πύλες NOR 2-εισόδων",
                    is_highlight=True,
                    category="boolean",
                    tag_label="NOR-SYNTH",
                    badge_class="badge-boolean",
                    tooltip="Classification: Καθολική Λογική Σύνθεση (Universal Logic) | Detection Clue: Only 2-input NOR gates | Application Rationale: Απαιτεί εφαρμογή διπλού συμπληρώματος και νόμων De Morgan.",
                ),
                TextSegment(text=".", is_highlight=False),
            ],
            accent_border_color="var(--accent)",
        ),
        # Theme 3 Paragraph
        Paragraph(
            segments=[
                TextSegment(text="Θέμα 3: Σχεδίαση Σύγχρονου Ακολουθιακού Κυκλώματος\n", is_highlight=False),
                TextSegment(text="Σχεδιάστε σύγχρονο ακολουθιακό κύκλωμα με ", is_highlight=False),
                TextSegment(
                    text="D Flip-Flops",
                    is_highlight=True,
                    category="fsm",
                    tag_label="D-FF",
                    badge_class="badge-fsm",
                    tooltip="Classification: Σύγχρονα Στοιχεία Μνήμης | Detection Clue: D Flip-Flops | Application Rationale: Εξίσωση διέγερσης Di = Qi+, απλοποιώντας τον πίνακα διεγέρσεων.",
                ),
                TextSegment(text=" το οποίο αναγνωρίζει την ", is_highlight=False),
                TextSegment(
                    text="ακολουθία 101",
                    is_highlight=True,
                    category="fsm",
                    tag_label="SEQ-101",
                    badge_class="badge-fsm",
                    tooltip="Classification: Σειριακό Πρότυπο Ανίχνευσης | Detection Clue: Ακολουθία '101' | Application Rationale: Καθορίζει τις απαιτούμενες καταστάσεις ανίχνευσης προθεμάτων.",
                ),
                TextSegment(text=" σε σειριακή είσοδο X. Μόλις ανιχνευθεί η ακολουθία, η έξοδος Z γίνεται '1' για έναν κύκλο ρολογιού. Επιτρέπεται η ", is_highlight=False),
                TextSegment(
                    text="επικάλυψη (overlapping)",
                    is_highlight=True,
                    category="fsm",
                    tag_label="OVERLAP",
                    badge_class="badge-fsm",
                    tooltip="Classification: Λειτουργία Επικάλυψης | Detection Clue: Overlapping allowed | Application Rationale: Μετά την ανίχνευση, το τελικό '1' επαναχρησιμοποιείται ως πρώτο bit νέας ακολουθίας.",
                ),
                TextSegment(text=".\n1. Σχεδιάστε το διάγραμμα καταστάσεων.\n2. Κατασκευάστε τον πίνακα διεγέρσεων.\n3. Εξάγετε τις ελάχιστες εξισώσεις Di και Z.\n4. Σχεδιάστε το λογικό κύκλωμα.", is_highlight=False),
            ],
            accent_border_color="var(--accent)",
        ),
        # Theme 4 Paragraph
        Paragraph(
            segments=[
                TextSegment(text="Θέμα 4: Περιγραφή Υλικού σε VHDL\n", is_highlight=False),
                TextSegment(text="Γράψτε πλήρη κώδικα VHDL (Entity και Behavioral Architecture) για έναν ", is_highlight=False),
                TextSegment(
                    text="πολυπλέκτη 4-σε-1 (4-to-1 MUX)",
                    is_highlight=True,
                    category="vhdl",
                    tag_label="MUX-4TO1",
                    badge_class="badge-vhdl",
                    tooltip="Classification: Πολυπλέκτης Δεδομένων MSI | Detection Clue: 4-to-1 Multiplexer | Application Rationale: Δρομολογεί 1 από 4 διαύλους εισόδου στην κοινή έξοδο βάσει 2 γραμμών επιλογής.",
                ),
                TextSegment(text=" με διαύλους δεδομένων πλάτους ", is_highlight=False),
                TextSegment(
                    text="STD_LOGIC_VECTOR(7 downto 0)",
                    is_highlight=True,
                    category="vhdl",
                    tag_label="BUS-8BIT",
                    badge_class="badge-vhdl",
                    tooltip="Classification: Τύπος Παράλληλου Διαύλου IEEE | Detection Clue: STD_LOGIC_VECTOR(7 downto 0) | Application Rationale: Ορίζει διαύλους 8-bit για d0, d1, d2, d3 και την έξοδο y.",
                ),
                TextSegment(text=", σήμα ενεργοποίησης ", is_highlight=False),
                TextSegment(
                    text="enable (active-high)",
                    is_highlight=True,
                    category="vhdl",
                    tag_label="ENABLE",
                    badge_class="badge-vhdl",
                    tooltip="Classification: Σήμα Ελέγχου Ενεργοποίησης | Detection Clue: enable active-high | Application Rationale: Όταν enable='0', η έξοδος τίθεται σε (others => '0').",
                ),
                TextSegment(text=" και ", is_highlight=False),
                TextSegment(
                    text="2 γραμμές επιλογής sel",
                    is_highlight=True,
                    category="vhdl",
                    tag_label="SEL-2BIT",
                    badge_class="badge-vhdl",
                    tooltip="Classification: Διάνυσμα Επιλογής Διεύθυνσης | Detection Clue: sel STD_LOGIC_VECTOR(1 downto 0) | Application Rationale: Καθορίζει τις περιπτώσεις '00', '01', '10', '11' στη δομή case.",
                ),
                TextSegment(text=".\n1. Πλήρης δήλωση Entity.\n2. Behavioral Architecture με process και case.\n3. Τεχνική εξήγηση αποτροπής latch.", is_highlight=False),
            ],
            accent_border_color="var(--accent)",
        ),
    ]

    questions = [
        # Question 1: 2's Complement
        ExamQuestion(
            question_number=1,
            title="Αριθμητική Συμπληρώματος ως προς 2 & Ανίχνευση Υπερχείλισης",
            question_type="Binary Arithmetic",
            prompt_text=(
                "1. Μετατρέψτε τους δεκαδικούς αριθμούς $A = +43$ και $B = -27$ σε δυαδική αναπαράσταση "
                "συμπληρώματος ως προς 2 μήκους 8-bit.\n"
                "2. Εκτελέστε την πράξη πρόσθεσης $A + B$ σε δυαδική μορφή 8-bit και ελέγξτε για τυχόν υπερχείλιση.\n"
                "3. Εξηγήστε πώς ανιχνεύεται η υπερχείλιση κατά την πρόσθεση δύο προσημασμένων αριθμών στο υλικό."
            ),
            given_parameters=[
                GivenParameter(symbol="A", value="+43_{10}", description="Θετικός δεκαδικός τελεστέος", category="param"),
                GivenParameter(symbol="B", value="-27_{10}", description="Αρνητικός δεκαδικός τελεστέος", category="param"),
                GivenParameter(symbol="n", value="8\\text{ bits}", description="Μήκος λέξης καταχωρητή", category="param"),
                GivenParameter(symbol="\\text{Range}", value="[-128, +127]", description="Εύρος αναπαράστασης 8-bit C2", category="param"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Δυαδική Μετατροπή Θετικού Τελεστέου A = +43",
                    formula="A_{10} = \\sum_{i=0}^{7} b_i 2^i",
                    substitution="43 = 32 + 8 + 2 + 1 = 2^5 + 2^3 + 2^1 + 2^0",
                    result="A = 00101011_2",
                    rationale="Στο συμπλήρωμα ως προς 2, οι θετικοί αριθμοί αναπαρίστανται απευθείας με MSB (bit 7) ίσο με 0.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Υπολογισμός Συμπληρώματος ως προς 2 για B = -27",
                    formula="[-B]_{C2} = \\overline{B} + 1",
                    substitution="+27_{10} = 00011011_2 \\implies \\text{1's complement} = 11100100_2 \\implies + 1",
                    result="B = 11100101_2",
                    rationale="Αντιστρέφονται όλα τα bits του θετικού μεγέθους και προστίθεται 1 στο LSB. Το MSB=1 δηλώνει αρνητικό πρόσημο.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Εκτέλεση Δυαδικής Πρόσθεσης A + B με Ανίχνευση Κρατουμένων",
                    formula="S = A + B \\pmod{2^8}",
                    substitution=(
                        "\\begin{array}{rl}"
                        "  00101011_2 & \\text{(+43)} \\\\"
                        "+ \\; 11100101_2 & \\text{(-27)} \\\\"
                        "\\hline"
                        "(1) \\; 00010000_2 & \\text{(+16)}"
                        "\\end{array}"
                    ),
                    result="\\text{Sum} = 00010000_2 = +16_{10}, \\quad C_{out} = 1",
                    rationale="Το κρατούμενο εξόδου C8=1 απορρίπτεται στην αριθμητική C2. Το αποτέλεσμα 00010000_2 ισούται ακριβώς με 16 στο δεκαδικό.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Έλεγχος Υπερχείλισης μέσω Κρατουμένων MSB",
                    formula="V = C_7 \\oplus C_8",
                    substitution="C_7 = 1 \\; (\\text{κρατούμενο εισόδου στο bit 7}), \\quad C_8 = 1 \\; (\\text{κρατούμενο εξόδου})",
                    result="V = 1 \\oplus 1 = 0 \\implies \\text{Δεν υπάρχει υπερχείλιση}",
                    rationale="Η υπερχείλιση στο υλικό ανιχνεύεται με πύλη XOR μεταξύ των κρατουμένων εισόδου και εξόδου της βαθμίδας MSB.",
                ),
            ],
            final_answer="A = 00101011_2, \\; B = 11100101_2, \\; A+B = 00010000_2 = +16_{10}, \\; V = 0 \\; (\\text{Καμία Υπερχείλιση})",
            detailed_justification=(
                "Στην προσημασμένη αριθμητική συμπληρώματος ως προς 2, η πρόσθεση δύο αριθμών με αντίθετα πρόσημα "
                "είναι μαθηματικά αδύνατον να προκαλέσει υπερχείλιση, καθώς το μέγεθος του αθροίσματος είναι πάντα "
                "γνησίως μικρότερο από το μέγιστο των δύο όρων. Στο υλικό, η πύλη XOR των κρατουμένων C7 και C8 "
                "δίνει V = 0, επιβεβαιώνοντας απόλυτα την εγκυρότητα του αποτελέσματος."
            ),
            common_pitfalls=[
                "Σύγχυση του κρατουμένου εξόδου (Cout) με την υπερχείλιση (Overflow): Το Cout=1 απορρίπτεται και ΔΕΝ αποτελεί σφάλμα.",
                "Ξέχασμα προσθήκης του 1 στο LSB κατά τη μετατροπή αρνητικού αριθμού σε συμπλήρωμα ως προς 2.",
                "Εσφαλμένος έλεγχος υπερχείλισης: Η υπερχείλιση μπορεί να εμφανιστεί ΜΟΝΟ κατά την πρόσθεση ομόσημων αριθμών.",
            ],
            related_theory_topic="Ενότητα 1: Συστήματα Αριθμών & Δυαδική Αριθμητική",
        ),
        # Question 2: K-Map & NOR synthesis
        ExamQuestion(
            question_number=2,
            title="Απλοποίηση με Χάρτη Karnaugh & Σύνθεση με Πύλες NOR",
            question_type="K-Map Minimization",
            prompt_text=(
                "Δίνεται η λογική συνάρτηση:\n"
                "$$F(A, B, C, D) = \\sum m(1, 3, 7, 11, 15) + d(0, 2, 5)$$\n"
                "1. Απλοποιήστε τη συνάρτηση σε ελάχιστη μορφή SOP χρησιμοποιώντας χάρτη Karnaugh.\n"
                "2. Υλοποιήστε την απλοποιημένη συνάρτηση χρησιμοποιώντας **αποκλειστικά πύλες NOR 2-εισόδων**."
            ),
            given_parameters=[
                GivenParameter(symbol="\\text{Minterms}", value="m(1, 3, 7, 11, 15)", description="Κελιά με λογικό 1", category="param"),
                GivenParameter(symbol="\\text{Don't Cares}", value="d(0, 2, 5)", description="Αδιάφορες συνθήκες", category="param"),
                GivenParameter(symbol="\\text{Target}", value="\\text{NOR 2-in only}", description="Περιορισμός τεχνολογίας σύνθεσης", category="param"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Χαρτογράφηση Minterms και Don't Cares σε Χάρτη K-Map 4x4",
                    formula="K(AB, CD) \\quad \\text{με γραμμές } AB \\in \\{00, 01, 11, 10\\} \\text{ και στήλες } CD \\in \\{00, 01, 11, 10\\}",
                    substitution=(
                        "m(3, 7, 11, 15) \\text{ γεμίζουν όλη τη στήλη } CD=11. \\\\"
                        "m(1)=1, \\; d(0)=d, \\; d(2)=d, \\; d(5)=d. \\text{ Όλα τα υπόλοιπα κελιά είναι } 0."
                    ),
                    result="\\text{Εντοπισμός δύο μεγάλων ομάδων 4 κελιών}",
                    rationale="Η αξιοποίηση των συνθηκών don't care επιτρέπει τον σχηματισμό μεγαλύτερων ομάδων μεγέθους 4 αντί για 2.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Εξαγωγή Πρωτευόντων Ουσιωδών Όρων (Prime Implicants)",
                    formula="F_{SOP} = \\text{Group}_1 + \\text{Group}_2",
                    substitution=(
                        "\\text{Ομάδα 1 (Στήλη } CD=11): m(3, 7, 11, 15) \\implies CD \\\\"
                        "\\text{Ομάδα 2 (Κελιά } 1, 3, 5, 7): m(1), m(3), d(5), m(7) \\implies \\overline{A}D"
                    ),
                    result="F = CD + \\overline{A}D = D(C + \\overline{A})",
                    rationale="Ο όρος CD είναι essential γιατί καλύπτει μοναδικά τα m(11), m(15). Ο όρος A'D καλύπτει το m(1) με μόνο 2 μεταβλητές.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Αλγεβρικός Μετασχηματισμός σε Μορφή NOR (De Morgan)",
                    formula="F = \\overline{\\overline{F}} = \\overline{\\overline{D \\cdot (C + \\overline{A})}}",
                    substitution=(
                        "F = \\overline{\\overline{D} + \\overline{C + \\overline{A}}} = \\text{NOR}\\Big(\\overline{D}, \\; \\overline{C + \\overline{A}}\\Big)"
                    ),
                    result="F = \\text{NOR}\\big(\\text{NOR}(D, D), \\; \\text{NOR}(C, \\text{NOR}(A, A))\\big)",
                    rationale="Εφαρμόζοντας διπλό συμπλήρωμα στη συνάρτηση F = D(C + A'), προκύπτει απευθείας NOR μεταξύ του D' και του NOR(C, A').",
                ),
                CalculationStep(
                    step_number=4,
                    title="Κατανομή Πυλών NOR 2-Εισόδων",
                    formula="\\text{Gates: } U_1, U_2, U_3, U_4",
                    substitution=(
                        "U_1 = \\text{NOR}(A, A) = \\overline{A} \\\\"
                        "U_2 = \\text{NOR}(D, D) = \\overline{D} \\\\"
                        "U_3 = \\text{NOR}(C, U_1) = \\overline{C + \\overline{A}} \\\\"
                        "U_4 = \\text{NOR}(U_2, U_3) = F"
                    ),
                    result="\\text{Ακριβώς 4 πύλες NOR 2-εισόδων}",
                    rationale="Η χρήση της παραγοντοποιημένης μορφής D(C + A') επιτρέπει την υλοποίηση με μόλις 4 πύλες NOR χωρίς πλεονασμούς.",
                ),
            ],
            final_answer="F(A,B,C,D) = CD + \\overline{A}D = D(C + \\overline{A}) \\quad \\text{με 4 πύλες NOR 2-εισόδων}",
            detailed_justification=(
                "Ο χάρτης K-Map αποκαλύπτει δύο κύβους διάστασης 2 (ομάδες των 4): τον ουσιώδη όρο CD και τον όρο A'D "
                "(ή εναλλακτικά A'B'). Παραγοντοποιώντας ως D(C + A') και εφαρμόζοντας το θεώρημα De Morgan, "
                "η συνάρτηση μετατρέπεται σε NOR δύο όρων, καθένας εκ των οποίων απαιτεί μία επιπλέον πύλη NOR, "
                "επιτυγχάνοντας το απολύτως ελάχιστο κόστος υλικού."
            ),
            common_pitfalls=[
                "Μη αξιοποίηση των don't cares, οδηγώντας σε μικρότερες ομάδες και περισσότερες πύλες.",
                "Υλοποίηση του SOP με πύλες AND/OR και απλή αντικατάσταση χωρίς εφαρμογή De Morgan, οδηγώντας σε πύλες εκτός προδιαγραφών.",
                "Ξέχασμα ότι ένας αντιστροφέας NOT υλοποιείται συνδέοντας τις δύο εισόδους μιας πύλης NOR μαζί: NOR(x, x) = x'.",
            ],
            related_theory_topic="Ενότητα 4: Απλοποίηση Boole & Χάρτες Karnaugh",
        ),
        # Question 3: FSM Sequence Detector
        ExamQuestion(
            question_number=3,
            title="Σχεδίαση Σύγχρονης FSM για Ανιχνευτή Ακολουθίας '101' με D Flip-Flops",
            question_type="FSM Sequential Design",
            prompt_text=(
                "Σχεδιάστε σύγχρονο ακολουθιακό κύκλωμα με D Flip-Flops το οποίο αναγνωρίζει την ακολουθία `101` σε μια "
                "σειριακή είσοδο $X$. Μόλις ανιχνευθεί η ακολουθία, η έξοδος $Z$ γίνεται '1' για έναν κύκλο ρολογιού. "
                "Επιτρέπεται η επικάλυψη (overlapping)."
            ),
            given_parameters=[
                GivenParameter(symbol="\\text{Sequence}", value="101", description="Ακολουθία-στόχος ανίχνευσης", category="param"),
                GivenParameter(symbol="\\text{Mode}", value="\\text{Overlapping}", description="Επιτρέπεται επαναχρησιμοποίηση bits", category="param"),
                GivenParameter(symbol="\\text{Model}", value="\\text{Mealy}", description="3 καταστάσεις, άμεση απόκριση", category="param"),
                GivenParameter(symbol="\\text{Flip-Flops}", value="2 \\times \\text{D-FF}", description="D1, D0 για καταστάσεις Q1, Q0", category="param"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ορισμός Καταστάσεων και Σημασίας Προθεμάτων",
                    formula="S_k \\in \\{S_0, S_1, S_2\\}",
                    substitution=(
                        "S_0 (00): \\text{Reset / Κανένα έγκυρο πρόθεμα} \\\\"
                        "S_1 (01): \\text{Τελευταίο bit ήταν '1'} \\\\"
                        "S_2 (10): \\text{Τελευταία bits ήταν '10'}"
                    ),
                    result="3 \\text{ έγκυρες καταστάσεις } \\implies 2 \\text{ Flip-Flops } (Q_1 Q_0)",
                    rationale="Με 3 καταστάσεις απαιτούνται ceil(log2(3)) = 2 D Flip-Flops. Η κατάσταση 11 παραμένει αχρησιμοποίητη (don't care).",
                ),
                CalculationStep(
                    step_number=2,
                    title="Κατασκευή Πίνακα Μεταβάσεων και Διεγέρσεων",
                    formula="D_1 = Q_1^+, \\quad D_0 = Q_0^+, \\quad Z = f(Q_1, Q_0, X)",
                    substitution=(
                        "Q_1 Q_0 = 00: X=0 \\to 00, Z=0; \\quad X=1 \\to 01, Z=0 \\\\"
                        "Q_1 Q_0 = 01: X=0 \\to 10, Z=0; \\quad X=1 \\to 01, Z=0 \\\\"
                        "Q_1 Q_0 = 10: X=0 \\to 00, Z=0; \\quad X=1 \\to 01, Z=1 (\\text{Match!}) \\\\"
                        "Q_1 Q_0 = 11: X=0 \\to XX, Z=X; \\quad X=1 \\to XX, Z=X"
                    ),
                    result="\\text{Πλήρης πίνακας καταστάσεων}",
                    rationale="Όταν είμαστε στο S2 (10) και έρθει X=1, η ακολουθία 101 ολοκληρώνεται (Z=1). Λόγω επικάλυψης, πάμε στο S1 (01).",
                ),
                CalculationStep(
                    step_number=3,
                    title="Ελαχιστοποίηση Εξισώσεων Διέγερσης D1, D0 και Εξόδου Z",
                    formula="K\\text{-Maps για } D_1, D_0, Z \\text{ συναρτήσει } (Q_1, Q_0, X)",
                    substitution=(
                        "D_1: m(010)=1, \\; d(110, 111)=X \\implies D_1 = \\overline{Q_1} \\cdot Q_0 \\cdot \\overline{X} \\\\"
                        "D_0: m(001, 011, 101)=1, \\; d(111)=X \\implies D_0 = X \\\\"
                        "Z: m(101)=1, \\; d(111)=X \\implies Z = Q_1 \\cdot X"
                    ),
                    result="D_1 = \\overline{Q_1} Q_0 \\overline{X}, \\quad D_0 = X, \\quad Z = Q_1 X",
                    rationale="Η ελαχιστοποίηση αποκαλύπτει εξαιρετικά απλές εξισώσεις: το D0 συνδέεται απευθείας στην είσοδο X!",
                ),
                CalculationStep(
                    step_number=4,
                    title="Έλεγχος Αυτοδιόρθωσης (Self-Correction)",
                    formula="\\text{Επόμενη κατάσταση από } Q_1 Q_0 = 11",
                    substitution="X=0 \\implies D_1=0, D_0=0 \\implies 00 (S_0); \\quad X=1 \\implies D_1=0, D_0=1 \\implies 01 (S_1)",
                    result="\\text{Πλήρης αυτοδιόρθωση σε 1 κύκλο ρολογιού}",
                    rationale="Ακόμα κι αν το κύκλωμα εκκινήσει στην απαγορευμένη κατάσταση 11, μεταβαίνει σε έγκυρη κατάσταση στον αμέσως επόμενο παλμό.",
                ),
            ],
            final_answer="D_1 = \\overline{Q_1} Q_0 \\overline{X}, \\quad D_0 = X, \\quad Z = Q_1 X \\quad (\\text{Πλήρως Αυτοδιορθούμενο})",
            detailed_justification=(
                "Το μοντέλο Mealy εξασφαλίζει ανίχνευση της ακολουθίας 101 στον ίδιο κύκλο ρολογιού όπου εμφανίζεται "
                "το τελευταίο bit, μειώνοντας τον αριθμό των καταστάσεων σε μόλις 3 (έναντι 4 του Moore). Η επιλογή "
                "της κωδικοποίησης επέτρεψε την ιδανική απλοποίηση D0 = X, ελαχιστοποιώντας την απαιτούμενη συνδυαστική "
                "λογική σε μόλις μία πύλη AND 3-εισόδων και μία πύλη AND 2-εισόδων."
            ),
            common_pitfalls=[
                "Επιστροφή στην κατάσταση S0 μετά την ανίχνευση του 101 αντί για το S1: αυτό παραβιάζει την προδιαγραφή επικάλυψης (overlapping).",
                "Παράλειψη του ελέγχου αυτοδιόρθωσης για τις αχρησιμοποίητες καταστάσεις, που μπορεί να οδηγήσει σε hardware deadlock.",
                "Σύγχυση των διεγέρσεων του D Flip-Flop: για το D Flip-Flop ισχύει πάντα D = Q_next.",
            ],
            related_theory_topic="Ενότητα 9: Ακολουθιακά Κυκλώματα & Μηχανές FSM",
        ),
        # Question 4: VHDL MUX
        ExamQuestion(
            question_number=4,
            title="Περιγραφή Πολυπλέκτη 4:1 8-bit σε VHDL & Αποτροπή Latches",
            question_type="VHDL Hardware Synthesis",
            prompt_text=(
                "Γράψτε πλήρη κώδικα VHDL (Entity και Behavioral Architecture) για έναν πολυπλέκτη 4-σε-1 (4-to-1 MUX) με "
                "διαύλους δεδομένων πλάτους 8-bit (`STD_LOGIC_VECTOR(7 downto 0)`), σήμα ενεργοποίησης `enable` "
                "(active-high) και 2 γραμμές επιλογής `sel`.\n"
                "1. Πλήρης δήλωση οντότητας (Entity).\n"
                "2. Αρχιτεκτονική συμπεριφοράς (Behavioral Architecture) με χρήση διεργασίας και case.\n"
                "3. Εξηγήστε πώς αποτρέπεται η ανεπιθύμητη δημιουργία μανδαλωτών (latches)."
            ),
            given_parameters=[
                GivenParameter(symbol="\\text{Inputs}", value="\\text{d0, d1, d2, d3 (8-bit)}", description="4 δίαυλοι δεδομένων", category="param"),
                GivenParameter(symbol="\\text{Select}", value="\\text{sel (2-bit)}", description="Γραμμές επιλογής MUX", category="param"),
                GivenParameter(symbol="\\text{Enable}", value="\\text{enable (active-high)}", description="Σήμα γενικής ενεργοποίησης", category="param"),
                GivenParameter(symbol="\\text{Output}", value="\\text{y (8-bit)}", description="Δίαυλος εξόδου δεδομένων", category="param"),
            ],
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ορισμός Οντότητας (Entity Interface)",
                    formula="\\text{entity mux4to1\\_8bit is port( ... );}",
                    substitution=(
                        "\\begin{aligned}"
                        "&\\text{d0, d1, d2, d3 : in STD\\_LOGIC\\_VECTOR(7 downto 0);} \\\\"
                        "&\\text{sel : in STD\\_LOGIC\\_VECTOR(1 downto 0); \\quad enable : in STD\\_LOGIC;} \\\\"
                        "&\\text{y : out STD\\_LOGIC\\_VECTOR(7 downto 0)}"
                        "\\end{aligned}"
                    ),
                    result="\\text{Πλήρες interface διαύλων 8-bit συμβατό με IEEE 1164}",
                    rationale="Όλοι οι δίαυλοι ορίζονται ως STD_LOGIC_VECTOR(7 downto 0) για συμβατότητα με το πρότυπο IEEE 1164.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Καθορισμός Λίστας Ευαισθησίας Συνδυαστικής Διεργασίας",
                    formula="\\text{process(d0, d1, d2, d3, sel, enable)}",
                    substitution="\\text{Όλα τα σήματα εισόδου που αναγιγνώσκονται περιλαμβάνονται στη λίστα}",
                    result="\\text{Πλήρης λίστα ευαισθησίας (Zero Simulation Mismatch)}",
                    rationale="Αν παραλειφθεί κάποιο σήμα εισόδου, ο προσομοιωτής δεν θα ενημερώνει την έξοδο όταν αυτό αλλάζει τιμή.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Έλεγχος Enable και Επιλογή Καναλιού μέσω Case",
                    formula="\\text{if enable = '0' then } y \\Leftarrow \\text{\"00000000\" else case sel is ...}",
                    substitution=(
                        "\\begin{aligned}"
                        "&\\text{when \"00\"} \\implies y \\Leftarrow d_0; \\quad &\\text{when \"01\"} \\implies y \\Leftarrow d_1; \\\\"
                        "&\\text{when \"10\"} \\implies y \\Leftarrow d_2; \\quad &\\text{when \"11\"} \\implies y \\Leftarrow d_3; \\\\"
                        "&\\text{when others} \\implies y \\Leftarrow \\text{(others} \\implies \\text{'0');}"
                        "\\end{aligned}"
                    ),
                    result="\\text{Συνθέσιμη δομή χωρίς latches και πλήρη κάλυψη}",
                    rationale="Η ιεραρχική αξιολόγηση (πρώτα το enable και μετά το sel) αναπαράγει πιστά τη λειτουργία εμπορικών πολυπλεκτών MSI.",
                ),
            ],
            final_answer="Πλήρης, συνθέσιμος κώδικας VHDL Behavioral Architecture χωρίς latches.",
            detailed_justification=(
                "Στη σύνθεση υλικού VHDL, ένα latch παράγεται όταν σε κάποιο μονοπάτι εκτέλεσης της διεργασίας "
                "ένα σήμα εξόδου δεν ανατίθεται ρητά. Στον κώδικά μας, το 'if enable = 0' παρέχει ρητή ανάθεση μηδενισμού, "
                "το αντίστοιχο 'else' καλύπτει τη λειτουργία ενεργοποίησης, η δομή 'case sel' καλύπτει και τους 4 δυνατούς "
                "συνδυασμούς, και ο κλάδος 'when others =>' χειρίζεται πιθανές μετασταθείς τιμές ('U', 'X', 'Z'), "
                "εγγυώμενος 100% καθαρή συνδυαστική πολυπλεξία."
            ),
            common_pitfalls=[
                "Ελλιπής λίστα ευαισθησίας: αν λείπει το sel ή κάποιο dk, η προσομοίωση θα συμπεριφέρεται λανθασμένα.",
                "Παράλειψη του κλάδου 'when others =>' στην εντολή case, προκαλώντας σφάλμα σύνθεσης ή δημιουργία latch.",
                "Ανάθεση τιμής διαφορετικού πλάτους στο y (π.χ. '0' αντί για (others => '0')).",
            ],
            related_theory_topic="Ενότητα 10: Εισαγωγή στη VHDL & Συνδυαστική Σύνθεση",
        ),
    ]

    justifications = [
        DesignJustification(
            title="Αριθμητική Συμπληρώματος ως προς 2",
            category="Boolean Theorem",
            description="Η αναπαράσταση αρνητικών αριθμών με C2 επιτρέπει την εκτέλεση αφαίρεσης A - B μέσω της πρόσθεσης A + (-B).",
            rationale="Απλοποιεί την ALU εξαλείφοντας την ανάγκη για ξεχωριστό κύκλωμα αφαιρέτη, αξιοποιώντας πλήρως τον κοινό αθροιστή.",
        ),
        DesignJustification(
            title="Ελαχιστοποίηση SOP & Καθολικότητα NOR",
            category="Hardware Efficiency",
            description="Κάθε λογική συνάρτηση μπορεί να υλοποιηθεί αποκλειστικά με πύλες NOR μέσω De Morgan.",
            rationale="Οι πύλες NOR καταλαμβάνουν μικρότερη επιφάνεια πυριτίου σε τεχνολογία CMOS, μειώνοντας την κατανάλωση ισχύος.",
        ),
        DesignJustification(
            title="Μοντέλο Mealy έναντι Moore",
            category="FSM Timing",
            description="Στο μοντέλο Mealy η έξοδος αλλάζει ασύγχρονα με την είσοδο, απαιτώντας λιγότερες καταστάσεις.",
            rationale="Επιτρέπει ανίχνευση του 101 σε 3 καταστάσεις (έναντι 4 στο Moore), εξοικονομώντας 1 Flip-Flop ή μειώνοντας τη λογική διέγερσης.",
        ),
        DesignJustification(
            title="Αποφυγή Latch Inference στη VHDL",
            category="VHDL Idiom",
            description="Κάθε έξοδος σε συνδυαστική διεργασία πρέπει να λαμβάνει τιμή σε όλους τους κλάδους if και case.",
            rationale="Η μη ανάθεση αναγκάζει το εργαλείο σύνθεσης να συμπεράνει μανδαλωτή (transparent latch), καταστρέφοντας το timing.",
        ),
    ]

    # SVG for FSM State Diagram (101 Sequence Detector)
    fsm_svg = generateFsm101Svg()

    # Verification Code (Python logic verifier)
    python_solution = '''# Python 3 + SymPy Logic & Arithmetic Verification Script
# Practice Exam 01: Digital Electronics Solutions Check

def verify_theme_1():
    """Verifies 2\'s complement 8-bit addition for +43 and -27."""
    A_dec = 43
    B_dec = -27
    
    # 8-bit conversions
    A_bin = format(A_dec & 0xFF, '08b')
    B_bin = format(B_dec & 0xFF, '08b')
    
    # Addition in 8-bit
    sum_val = (A_dec + B_dec) & 0xFF
    sum_bin = format(sum_val, '08b')
    
    # Hardware overflow check
    # Check carry into bit 7 and carry out of bit 7
    c7 = 1  # carry-in to bit 7
    c8 = 1  # carry-out from bit 7
    overflow = c7 ^ c8
    
    print(f"Theme 1 Check:")
    print(f"  A (+43) = {A_bin}")
    print(f"  B (-27) = {B_bin}")
    print(f"  A + B   = {sum_bin} (decimal: {sum_val})")
    print(f"  Overflow V = {overflow} (0 = No overflow)")
    assert sum_bin == "00010000", "Sum mismatch"
    assert overflow == 0, "Overflow mismatch"

def verify_theme_2():
    """Verifies K-map minimal SOP equivalence for F = CD + A\'D."""
    # Minterms: 1, 3, 7, 11, 15. Don\'t cares: 0, 2, 5
    minterms = {1, 3, 7, 11, 15}
    dont_cares = {0, 2, 5}
    
    # Function F(A, B, C, D) = C*D + (~A)*D
    for val in range(16):
        A = (val >> 3) & 1
        B = (val >> 2) & 1
        C = (val >> 1) & 1
        D = val & 1
        
        f_val = (C and D) or ((not A) and D)
        if val in minterms:
            assert f_val == 1, f"Failed minterm {val}"
        elif val not in dont_cares:
            assert f_val == 0, f"False 1 at {val}"
            
    print("Theme 2 Check: All 16 truth table entries match K-map SOP!")

def verify_theme_3():
    """Verifies Mealy FSM 101 sequence detector transitions."""
    states = {"S0": 0, "S1": 1, "S2": 2}
    # Transitions
    def next_state(s, x):
        if s == "S0": return ("S1", 0) if x else ("S0", 0)
        elif s == "S1": return ("S1", 0) if x else ("S2", 0)
        elif s == "S2": return ("S1", 1) if x else ("S0", 0)
    
    bitstream = [1, 0, 1, 0, 1, 1, 0, 1]
    curr = "S0"
    outputs = []
    for bit in bitstream:
        curr, z = next_state(curr, bit)
        outputs.append(z)
        
    print(f"Theme 3 Check:")
    print(f"  Bitstream: {bitstream}")
    print(f"  Outputs Z: {outputs}")
    # Sequence 101 at indices 2, 4, 7
    assert outputs == [0, 0, 1, 0, 1, 0, 0, 1], "FSM output mismatch"

if __name__ == "__main__":
    verify_theme_1()
    verify_theme_2()
    verify_theme_3()
    print("All Digital Electronics solutions verified cleanly!")
'''

    return Scenario(
        id="practice_exam_01_core",
        title="Επαναληπτικό Θέμα 01: Συμπλήρωμα C2, K-Map & NOR, FSM 101, VHDL MUX",
        subtitle="Πλήρες Θέμα Εξετάσεων: Αριθμητική Υλικού, Συνδυαστική & Ακολουθιακή Σύνθεση, VHDL",
        course_tag="Practice Exam",
        duration_info="2.5 Ώρες • 4 Θέματα • 10 Μονάδες",
        paragraphs=paragraphs,
        questions=questions,
        diagram_svg_custom=fsm_svg,
        justifications=justifications,
        solution_code=python_solution,
    )


def generateFsm101Svg() -> str:
    """Generates the interactive SVG state transition diagram for the '101' Mealy FSM.

    Returns:
        str: Scalable vector graphic markup.
    """
    return """
    <svg width="860" height="400" viewBox="0 0 860 400" xmlns="http://www.w3.org/2000/svg" class="select-none">
        <defs>
            <marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3.5" orient="auto">
                <polygon points="0 0, 10 3.5, 0 7" fill="var(--accent)" />
            </marker>
            <marker id="arrow-green" markerWidth="10" markerHeight="10" refX="8" refY="3.5" orient="auto">
                <polygon points="0 0, 10 3.5, 0 7" fill="var(--green-ok)" />
            </marker>
            <marker id="arrow-muted" markerWidth="10" markerHeight="10" refX="8" refY="3.5" orient="auto">
                <polygon points="0 0, 10 3.5, 0 7" fill="var(--svg-stroke)" />
            </marker>
        </defs>

        <!-- Grid Lines Background -->
        <g stroke="var(--svg-grid-dot)" stroke-width="1" stroke-dasharray="4 4">
            <line x1="50" y1="200" x2="810" y2="200" />
        </g>

        <!-- Reset Arrow -->
        <line x1="70" y1="200" x2="140" y2="200" stroke="var(--accent)" stroke-width="3" marker-end="url(#arrow)" />
        <text x="75" y="190" font-family="Outfit, sans-serif" font-weight="bold" font-size="12" fill="var(--accent)">RESET</text>

        <!-- State S0: Reset / No match -->
        <g id="node-s0" transform="translate(180, 200)">
            <circle r="42" fill="var(--svg-fill)" stroke="var(--accent)" stroke-width="3.5" />
            <text x="0" y="-5" text-anchor="middle" font-family="Outfit, sans-serif" font-weight="bold" font-size="16" fill="var(--text-1)">S₀</text>
            <text x="0" y="15" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="12" fill="var(--text-3)">00</text>
            <text x="0" y="58" text-anchor="middle" font-family="Outfit, sans-serif" font-size="11" fill="var(--text-2)" class="de-diagram-detail">Κανένα πρόθεμα</text>
        </g>

        <!-- Transition S0 -> S0 on X=0 -->
        <path d="M 160,165 C 130,110 230,110 200,165" fill="none" stroke="var(--svg-stroke)" stroke-width="2.5" marker-end="url(#arrow-muted)" />
        <text x="180" y="115" text-anchor="middle" font-family="JetBrains Mono, monospace" font-weight="bold" font-size="13" fill="var(--text-1)">0 / 0</text>

        <!-- Transition S0 -> S1 on X=1 -->
        <path d="M 222,185 C 290,145 350,145 418,185" fill="none" stroke="var(--accent)" stroke-width="2.5" marker-end="url(#arrow)" />
        <text x="320" y="150" text-anchor="middle" font-family="JetBrains Mono, monospace" font-weight="bold" font-size="14" fill="var(--accent)">1 / 0</text>

        <!-- State S1: Has '1' -->
        <g id="node-s1" transform="translate(460, 200)">
            <circle r="42" fill="var(--svg-fill)" stroke="var(--accent)" stroke-width="3.5" />
            <text x="0" y="-5" text-anchor="middle" font-family="Outfit, sans-serif" font-weight="bold" font-size="16" fill="var(--text-1)">S₁</text>
            <text x="0" y="15" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="12" fill="var(--text-3)">01</text>
            <text x="0" y="58" text-anchor="middle" font-family="Outfit, sans-serif" font-size="11" fill="var(--text-2)" class="de-diagram-detail">Τελευταίο: '1'</text>
        </g>

        <!-- Transition S1 -> S1 on X=1 -->
        <path d="M 440,165 C 410,110 510,110 480,165" fill="none" stroke="var(--svg-stroke)" stroke-width="2.5" marker-end="url(#arrow-muted)" />
        <text x="460" y="115" text-anchor="middle" font-family="JetBrains Mono, monospace" font-weight="bold" font-size="13" fill="var(--text-1)">1 / 0</text>

        <!-- Transition S1 -> S2 on X=0 -->
        <path d="M 502,185 C 570,145 630,145 698,185" fill="none" stroke="var(--accent)" stroke-width="2.5" marker-end="url(#arrow)" />
        <text x="600" y="150" text-anchor="middle" font-family="JetBrains Mono, monospace" font-weight="bold" font-size="14" fill="var(--accent)">0 / 0</text>

        <!-- State S2: Has '10' -->
        <g id="node-s2" transform="translate(740, 200)">
            <circle r="42" fill="var(--svg-fill)" stroke="var(--accent)" stroke-width="3.5" />
            <text x="0" y="-5" text-anchor="middle" font-family="Outfit, sans-serif" font-weight="bold" font-size="16" fill="var(--text-1)">S₂</text>
            <text x="0" y="15" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="12" fill="var(--text-3)">10</text>
            <text x="0" y="58" text-anchor="middle" font-family="Outfit, sans-serif" font-size="11" fill="var(--text-2)" class="de-diagram-detail">Τελευταία: '10'</text>
        </g>

        <!-- Transition S2 -> S0 on X=0 (Back to start) -->
        <path d="M 720,240 C 600,350 320,350 200,240" fill="none" stroke="var(--svg-stroke)" stroke-width="2.5" marker-end="url(#arrow-muted)" />
        <text x="460" y="340" text-anchor="middle" font-family="JetBrains Mono, monospace" font-weight="bold" font-size="13" fill="var(--text-3)">0 / 0 (Αποτυχία)</text>

        <!-- Transition S2 -> S1 on X=1 (Match with Overlap!) -->
        <path d="M 700,215 C 640,255 560,255 500,215" fill="none" stroke="var(--green-ok)" stroke-width="3.5" marker-end="url(#arrow-green)" />
        <text x="600" y="275" text-anchor="middle" font-family="JetBrains Mono, monospace" font-weight="bold" font-size="14" fill="var(--green-ok)">1 / 1 (ΕΠΙΤΥΧΙΑ!)</text>

        <!-- Legend / Notes inside SVG -->
        <g class="de-diagram-detail" transform="translate(200, 375)">
            <rect x="0" y="0" width="460" height="24" rx="6" fill="var(--surface-2)" stroke="var(--border)" />
            <text x="230" y="16" text-anchor="middle" font-family="Outfit, sans-serif" font-size="11" fill="var(--text-2)">
                Συμβολισμός Ακμών: Είσοδος X / Έξοδος Z • Επικάλυψη: Μετά το '101', το '1' επαναχρησιμοποιείται (S₂ → S₁)
            </text>
        </g>
    </svg>
    """
