"""Synthetic Full Coverage Exam 1 Scenario Module.

Contains 1-to-1 representation of all exam questions from Synthetic Exam 1 (Full Coverage):
- Part A: Statistical multiplexing, Store-and-Forward principles, OSPF Link-State characteristics,
  Client-Server Network Edge placement, True/False (Control plane, Server static IP, BGP AS).
- Part B: Άσκηση 1 (Multi-hop 2-link store-and-forward delay and RTT), Άσκηση 2 (6-node Link-State Dijkstra table),
  Άσκηση 3 (CSMA/CD 64-Byte minimum frame & 7-bit Hamming code with even parity).
"""

from models.scenario import (
    NetworkScenario,
    Paragraph,
    TextSegment,
    ExamQuestion,
    QuestionOption,
    CalculationStep,
    TopologyNode,
    TopologyLink,
)


def createScenario() -> NetworkScenario:
    """Constructs and returns Synthetic Full Coverage Exam 1 scenario.

    Returns:
        NetworkScenario: The structured scenario object with 1-to-1 parity.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Το διαγώνισμα πλήρους κάλυψης "),
                TextSegment(
                    text="Synthetic Exam 1 (Full Coverage)",
                    is_highlight=True,
                    category="protocol",
                    tag_label="FULL COVERAGE 1",
                    tooltip="Διαγώνισμα συνολικής επανάληψης ύλης",
                ),
                TextSegment(text=" εστιάζει στις θεμελιώδεις αρχές της "),
                TextSegment(
                    text="Στατιστικής Πολυπλεξίας (Statistical Multiplexing)",
                    is_highlight=True,
                    category="protocol",
                    tag_label="STAT MULTIPLEX",
                    tooltip="Δυναμικός διαμοιρασμός πόρων on-demand στη μεταγωγή πακέτου",
                ),
                TextSegment(text=", στη λειτουργία "),
                TextSegment(
                    text="Store-and-Forward σε Δρομολογητές",
                    is_highlight=True,
                    category="routing",
                    tag_label="STORE & FORWARD",
                    tooltip="Λήψη ολόκληρου του πακέτου πριν την προώθηση",
                ),
                TextSegment(text=" και στην αρχιτεκτονική του πρωτοκόλλου "),
                TextSegment(
                    text="OSPF (Link State)",
                    is_highlight=True,
                    category="routing",
                    tag_label="OSPF LSA",
                    tooltip="Απαιτεί πλήρη γνώση της τοπολογίας δικτύου",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="#e06b3a",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Στο δεύτερο μέρος αναλύονται οι υπολογισμοί "),
                TextSegment(
                    text="Καθυστερήσεων Μετάδοσης και Διάδοσης σε 2 Ζεύξεις",
                    is_highlight=True,
                    category="delay",
                    tag_label="2 HOPS DELAY",
                    tooltip="t_total = 0.1506 s και RTT = 0.2008 s",
                ),
                TextSegment(text=", η εφαρμογή του αλγορίθμου "),
                TextSegment(
                    text="Dijkstra σε 6 Κόμβους",
                    is_highlight=True,
                    category="routing",
                    tag_label="DIJKSTRA 6",
                    tooltip="Βέλτιστες διαδρομές από ρίζα A",
                ),
                TextSegment(text=" και η κωδικοποίηση "),
                TextSegment(
                    text="Hamming(7,4) με Άρτια Ισοτιμία (0110011)",
                    is_highlight=True,
                    category="error_check",
                    tag_label="HAMMING EVEN",
                    tooltip="Διόρθωση μονών σφαλμάτων bit",
                ),
                TextSegment(text="."),
            ]
        ),
    ]

    questions = [
        # Part A - Question 1
        ExamQuestion(
            question_number=1,
            title="Χαρακτηριστικό Μεταγωγής Πακέτου έναντι Κυκλώματος",
            question_type="Multiple Choice",
            prompt_text="Ποιο από τα παρακάτω είναι χαρακτηριστικό της μεταγωγής πακέτου (packet switching) σε αντίθεση με τη μεταγωγή κυκλώματος (circuit switching);",
            options=[
                QuestionOption("A", "Η αποκλειστική δέσμευση πόρων εκ των προτέρων.", False, "Αυτό είναι χαρακτηριστικό του circuit switching."),
                QuestionOption("B", "Η δυνατότητα στατιστικής πολυπλεξίας (statistical multiplexing).", True, "Το packet switching μοιράζεται δυναμικά τους πόρους, επιτρέποντας σε πολλούς χρήστες να μοιράζονται αποδοτικά το κανάλι."),
                QuestionOption("C", "Η αδυναμία απώλειας πακέτων (packet loss).", False, "Στο packet switching μπορεί να συμβεί απώλεια λόγω buffer overflow."),
                QuestionOption("D", "Ο εγγυημένος ρυθμός μετάδοσης (QoS) για κάθε χρήστη.", False, "Εγγυημένο rate προσφέρει το circuit switching."),
            ],
            correct_option_letter="B",
            detailed_justification="Η μεταγωγή πακέτου μοιράζεται δυναμικά το εύρος ζώνης μεταξύ των χρηστών on-demand (statistical multiplexing).",
        ),
        # Part A - Question 2
        ExamQuestion(
            question_number=2,
            title="Λειτουργία Store-and-Forward σε Δρομολογητή",
            question_type="Multiple Choice",
            prompt_text="Η λειτουργία 'Store-and-Forward' σε έναν δρομολογητή (router) σημαίνει ότι:",
            options=[
                QuestionOption("A", "Ο δρομολογητής πρέπει να λάβει ολόκληρο το πακέτο πριν αρχίσει την προώθησή του.", True, "Πρέπει να ληφθούν όλα τα bits του πακέτου ώστε να ελεγχθεί το checksum/CRC."),
                QuestionOption("B", "Ο δρομολογητής αποθηκεύει τα πακέτα μόνιμα στο σκληρό του δίσκο.", False, "Αποθηκεύονται προσωρινά σε μνήμη RAM buffer."),
                QuestionOption("C", "Η προώθηση ξεκινά μόλις ληφθεί η κεφαλίδα (header) του πακέτου.", False, "Αυτό είναι Cut-through switching."),
                QuestionOption("D", "Ο δρομολογητής δεν ελέγχει ποτέ για σφάλματα κατά τη μεταφορά.", False, "Ελέγχει πλήρως για σφάλματα bit."),
            ],
            correct_option_letter="A",
            detailed_justification="Αυτή είναι η βασική αρχή του Store-and-Forward στο packet switching, προσθέτοντας καθυστέρηση μετάδοσης σε κάθε hop.",
        ),
        # Part A - Question 3
        ExamQuestion(
            question_number=3,
            title="Απαιτήσεις Πρωτοκόλλου OSPF (Link-State)",
            question_type="Multiple Choice",
            prompt_text="Ποιο από τα παρακάτω πρωτόκολλα δρομολόγησης βασίζεται στον αλγόριθμο Κατάστασης Ζεύξης (Link State) και απαιτεί πλήρη γνώση της τοπολογίας του δικτύου;",
            options=[
                QuestionOption("A", "RIP", False, "Το RIP είναι Distance Vector."),
                QuestionOption("B", "OSPF", True, "Το OSPF βασίζεται στον αλγόριθμο Dijkstra και χτίζει πλήρη τοπολογικό χάρτη."),
                QuestionOption("C", "BGP", False, "Το BGP είναι Path Vector."),
                QuestionOption("D", "ARP", False, "Το ARP είναι πρωτόκολλο Layer 2/3."),
            ],
            correct_option_letter="B",
            detailed_justification="Το OSPF (Open Shortest Path First) βασίζεται στον αλγόριθμο Dijkstra και είναι ένα πρωτόκολλο Link State που απαιτεί πλήρη τοπολογική γνώση.",
        ),
        # Part A - Question 4
        ExamQuestion(
            question_number=4,
            title="Αρχιτεκτονική Θέση Μοντέλου Client-Server",
            question_type="Multiple Choice",
            prompt_text="Το μοντέλο Client-Server ανήκει αρχιτεκτονικά:",
            options=[
                QuestionOption("A", "Στο Network Core (Πυρήνας Δικτύου)", False, "Ο πυρήνας περιλαμβάνει routers και switches."),
                QuestionOption("B", "Στο Network Edge (Άκρο Δικτύου)", True, "Clients και Servers αποτελούν τα τερματικά συστήματα (end systems)."),
                QuestionOption("C", "Μόνο σε τοπικά δίκτυα (LAN)", False, "Ισχύει παγκοσμίως."),
                QuestionOption("D", "Στο Επίπεδο Σύνδεσης Δεδομένων (Data Link Layer)", False, "Ανήκει στο Application Layer."),
            ],
            correct_option_letter="B",
            detailed_justification="Οι υπολογιστές-πελάτες και οι εξυπηρετητές αποτελούν τα τερματικά συστήματα που βρίσκονται στο άκρο του δικτύου.",
        ),
        # Part A - Question 5
        ExamQuestion(
            question_number=5,
            title="Θεωρητικές Προτάσεις Control Plane, Servers & BGP (Σωστό/Λάθος)",
            question_type="Multiple Choice",
            prompt_text=(
                "Επιλέξτε Σωστό (Σ) ή Λάθος (Λ) για τις παρακάτω προτάσεις:\n"
                "1. Το Control Plane ενός router αναλαμβάνει τον υπολογισμό και τη διατήρηση της γνώσης για τη δομή του δικτύου.\n"
                "2. Ένας εξυπηρετητής (Server) συνήθως έχει δυναμική IP διεύθυνση.\n"
                "3. Το πρωτόκολλο BGP χρησιμοποιείται για δρομολόγηση μεταξύ διαφορετικών Αυτόνομων Συστημάτων (AS)."
            ),
            options=[
                QuestionOption("A", "1: Σ, 2: Σ, 3: Σ", False, "Η πρόταση 2 είναι λάθος."),
                QuestionOption("B", "1: Σ, 2: Λ, 3: Σ", True, "1=Σ (Control plane routing computation), 2=Λ (Στατική IP για αξιοπιστία), 3=Σ (Inter-AS routing protocol)."),
                QuestionOption("C", "1: Λ, 2: Λ, 3: Σ", False, "Το Control plane είναι όντως υπεύθυνο για τους αλγορίθμους δρομολόγησης."),
                QuestionOption("D", "1: Σ, 2: Λ, 3: Λ", False, "Το BGP είναι το παγκόσμιο πρότυπο routing μεταξύ AS."),
            ],
            correct_option_letter="B",
            detailed_justification=(
                "1. **Σωστό:** Το Control Plane είναι υπεύθυνο για τους αλγορίθμους δρομολόγησης.\n"
                "2. **Λάθος:** Οι Servers απαιτούν μόνιμη, σταθερή IP για να είναι πάντα διαθέσιμοι στους πελάτες.\n"
                "3. **Σωστό:** Το BGP είναι το de facto πρωτόκολλο δρομολόγησης μεταξύ διαφορετικών AS στο διαδίκτυο."
            ),
        ),
        # Part B - Άσκηση 1
        ExamQuestion(
            question_number=6,
            title="Άσκηση 1: Υπολογισμός Καθυστερήσεων & RTT σε 2 Ζεύξεις",
            question_type="Calculations",
            prompt_text=(
                "Έστω δίκτυο με δύο ζεύξεις σε σειρά: `(A) ============ (B) ============ (C)`\n"
                "Link 1: R1 = 10000 bps, L1 = 100 km, u1 = 2.5*10^8 m/s.\n"
                "Link 2: R2 = 20000 bps, L2 = 50 km, u2 = 2.5*10^8 m/s.\n"
                "Μέγεθος πακέτου P = 1000 bits.\n\n"
                "**a.** Υπολογίστε τον χρόνο που χρειάζεται για την αποστολή ενός πακέτου από τον A στον C.\n"
                "**b.** Υπολογίστε το RTT για ένα πακέτο που αποστέλλεται από τον A στον B και επιστρέφει αμέσως."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Καθυστερήσεις Ζεύξης 1 (A -> B)",
                    formula="d_trans1 = P / R1  &&  d_prop1 = L1 / u1",
                    substitution="1000 / 10000 = 0.1 s | 100,000 / 2.5*10^8 = 0.4 ms = 0.0004 s",
                    result="d_trans1 = 0.1 s | d_prop1 = 0.4 ms",
                    rationale="Μετάδοση και διάδοση στην πρώτη ζεύξη.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Καθυστερήσεις Ζεύξης 2 (B -> C)",
                    formula="d_trans2 = P / R2  &&  d_prop2 = L2 / u2",
                    substitution="1000 / 20000 = 0.05 s | 50,000 / 2.5*10^8 = 0.2 ms = 0.0002 s",
                    result="d_trans2 = 0.05 s | d_prop2 = 0.2 ms",
                    rationale="Μετάδοση και διάδοση στη δεύτερη ζεύξη.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Ερώτημα a: Συνολικός Χρόνος A -> C",
                    formula="t_total = d_trans1 + d_prop1 + d_trans2 + d_prop2",
                    substitution="0.1 + 0.0004 + 0.05 + 0.0002",
                    result="0.1506 s",
                    rationale="Συνολικός χρόνος άφιξης του τελευταίου bit στον κόμβο C.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Ερώτημα b: RTT A -> B -> A",
                    formula="RTT_AB = 2 * d_trans1 + 2 * d_prop1",
                    substitution="2 * 0.1 + 2 * 0.0004",
                    result="0.2008 s",
                    rationale="Χρόνος αποστολής και επιστροφής μεταξύ άμεσων γειτόνων.",
                ),
            ],
            detailed_justification=(
                "- **a.** $t_{\\text{total}} = 0,1 + 0,0004 + 0,05 + 0,0002 = 0,1506\\text{ s}$\n"
                "- **b.** $\\text{RTT}_{A-B} = 2 \\times 0,1 + 2 \\times 0,0004 = 0,2008\\text{ s}$"
            ),
        ),
        # Part B - Άσκηση 2
        ExamQuestion(
            question_number=7,
            title="Άσκηση 2: Αλγόριθμος Dijkstra σε Γράφο 6 Κόμβων από Ρίζα A",
            question_type="Algorithm Step",
            prompt_text=(
                "Εφαρμόστε τον αλγόριθμο Dijkstra με κόμβο εκκίνησης τον **A** και βρείτε τα συντομότερα "
                "μονοπάτια προς όλους τους κόμβους.\n"
                "Τοπολογία: A-B:2, A-D:5, B-C:4, B-E:1, C-F:3, D-E:3, E-F:2."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Βήμα 0: Αρχικοποίηση (N = {A})",
                    formula="D(B)=2(A), D(D)=5(A), άλλοι=inf",
                    substitution="Ελάχιστος κόμβος: B με κόστος 2",
                    result="N = {A, B}",
                    rationale="Ο B μονιμοποιείται πρώτος.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Βήμα 1: Επέκταση μέσω B (N = {A, B})",
                    formula="D(C)=min(inf, 2+4)=6(B) | D(E)=min(inf, 2+1)=3(B)",
                    substitution="Ελάχιστος κόμβος: E με κόστος 3",
                    result="N = {A, B, E}",
                    rationale="Ο E μονιμοποιείται με κόστος 3.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Βήμα 2: Επέκταση μέσω E (N = {A, B, E})",
                    formula="D(D)=min(5(A), 3+3)=5(A) | D(F)=min(inf, 3+2)=5(E)",
                    substitution="Ισοπαλία κόστους 5 μεταξύ D και F",
                    result="N = {A, B, E, D, F, C}",
                    rationale="Μονιμοποίηση D (κόστος 5), F (κόστος 5) και C (κόστος 6).",
                ),
            ],
            detailed_justification=(
                "Πίνακας Dijkstra:\n\n"
                "| Βήμα | Επισκέφθηκε | B | C | D | E | F |\n"
                "|---|---|---|---|---|---|---|\n"
                "| 0 | A | **2(A)** | inf | 5(A) | inf | inf |\n"
                "| 1 | A, B | 2 | 6(B) | 5(A) | **3(B)** | inf |\n"
                "| 2 | A, B, E | 2 | 6(B) | **5(A)** | 3 | 5(E) |\n"
                "| 3 | A, B, E, D | 2 | 6(B) | 5 | 3 | **5(E)** |\n"
                "| 4 | A, B, E, D, F | 2 | **6(B)** | 5 | 3 | 5 |\n\n"
                "**Συντομότερα μονοπάτια από A:**\n"
                "- Προς **B**: $A \\rightarrow B$ (Κόστος: 2)\n"
                "- Προς **E**: $A \\rightarrow B \\rightarrow E$ (Κόστος: 3)\n"
                "- Προς **D**: $A \\rightarrow D$ (Κόστος: 5)\n"
                "- Προς **F**: $A \\rightarrow B \\rightarrow E \\rightarrow F$ (Κόστος: 5)\n"
                "- Προς **C**: $A \\rightarrow B \\rightarrow C$ (Κόστος: 6)"
            ),
        ),
        # Part B - Άσκηση 3
        ExamQuestion(
            question_number=8,
            title="Άσκηση 3: CSMA/CD L_min & Κώδικας Hamming με Άρτια Ισοτιμία",
            question_type="Calculations",
            prompt_text=(
                "**a.** Ένα δίκτυο χρησιμοποιεί CSMA/CD με bandwidth R = 10 Mbps. "
                "Αν ο μέγιστος χρόνος διάδοσης είναι t_prop = 25.6 μs, ποιο είναι το ελάχιστο μέγεθος πλαισίου σε Bytes;\n\n"
                "**b.** Αποστολέας στέλνει το μήνυμα `1011` εφαρμόζοντας τον κώδικα Hamming με **άρτια ισοτιμία (even parity)**. "
                "Ποιο είναι το τελικό μεταδιδόμενο μήνυμα;"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ερώτημα a: Ελάχιστο Πλαίσιο CSMA/CD",
                    formula="L_min = 2 * t_prop * R",
                    substitution="2 * (25.6 * 10^-6 s) * (10 * 10^6 bps)",
                    result="512 bits = 64 Bytes",
                    rationale="Απαραίτητο για την ανίχνευση συγκρούσεων στο IEEE 802.3.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ερώτημα b: Αριθμός Bits Ισοτιμίας Hamming",
                    formula="2^p >= d + p + 1",
                    substitution="d = 4 bits -> 2^p >= 4 + p + 1",
                    result="p = 3 bits (2^3 = 8 >= 8)",
                    rationale="Συνολικό μήκος κωδικολέξης n = 4 + 3 = 7 bits. Θέσεις ισοτιμίας: 1, 2, 4.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Ερώτημα b: Υπολογισμός με Άρτια Ισοτιμία (Even Parity)",
                    formula="P1(1,3,5,7), P2(2,3,6,7), P4(4,5,6,7) με D = 1 0 1 1",
                    substitution="P1 XOR (1,0,1)=0 -> P1=0 | P2 XOR (1,1,1)=1 -> P2=1 | P4 XOR (0,1,1)=0 -> P4=0",
                    result="P1=0, P2=1, P4=0",
                    rationale="Κάθε ομάδα ισοτιμίας πρέπει να περιέχει άρτιο (ζυγό) αριθμό άσων.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Τελική Κωδικολέξη",
                    formula="[P1, P2, D1, P4, D2, D3, D4]",
                    substitution="0 1 1 0 0 1 1",
                    result="0110011",
                    rationale="Τελικό μεταδιδόμενο μήνυμα 7 bits.",
                ),
            ],
            detailed_justification=(
                "**a. CSMA/CD:**\n"
                "$$L_{\\text{min}} = 2 \\times (25,6 \\times 10^{-6}\\text{ s}) \\times (10 \\times 10^6\\text{ bps}) = 512\\text{ bits} = 64\\text{ Bytes}$$\n\n"
                "**b. Hamming(7,4) Άρτια Ισοτιμία:**\n"
                "- $P_1$ (θέσεις 1, 3, 5, 7): $P_1 \\oplus 1 \\oplus 0 \\oplus 1 = P_1 \\oplus 0 \\Rightarrow \\mathbf{P_1 = 0}$\n"
                "- $P_2$ (θέσεις 2, 3, 6, 7): $P_2 \\oplus 1 \\oplus 1 \\oplus 1 = P_2 \\oplus 1 \\Rightarrow \\mathbf{P_2 = 1}$\n"
                "- $P_4$ (θέσεις 4, 5, 6, 7): $P_4 \\oplus 0 \\oplus 1 \\oplus 1 = P_4 \\oplus 0 \\Rightarrow \\mathbf{P_4 = 0}$\n\n"
                "Τελικό μεταδιδόμενο μήνυμα: **`0110011`**"
            ),
        ),
    ]

    nodes = [
        TopologyNode("h1", "Host 1", "host", 100, 150, "10.0.1.10"),
        TopologyNode("r1", "Router 1", "router", 380, 150, "10.0.1.1"),
        TopologyNode("r2", "Router 2", "router", 650, 150, "10.0.2.1"),
        TopologyNode("h2", "Host 2", "host", 900, 150, "10.0.2.10"),
    ]

    links = [
        TopologyLink("h1", "r1", 10, 100.0, 2.5, "copper", "10M | 100km"),
        TopologyLink("r1", "r2", 20, 50.0, 2.5, "fiber", "20M | 50km"),
        TopologyLink("r2", "h2", 100, 0.5, 2.0, "copper", "100M LAN"),
    ]

    return NetworkScenario(
        id="exam_synth_fc_1",
        title="Synthetic Exam 1 (Full Coverage)",
        subtitle="Statistical Multiplexing, Store-and-Forward, 2-Link Delays, Dijkstra & Hamming(7,4)",
        course_tag="Synthetic Full Coverage",
        duration_info="2 ώρες και 15 λεπτά",
        paragraphs=paragraphs,
        questions=questions,
        nodes=nodes,
        links=links,
        methodology_summary=[
            "1. Statistical Multiplexing: On-demand dynamic bandwidth allocation.",
            "2. Store-and-Forward: Full packet reception before forwarding.",
            "3. 2-Link Delays: t_total = 0.1506 s, RTT = 0.2008 s.",
            "4. Dijkstra: Συντομότερες διαδρομές από ρίζα A.",
            "5. CSMA/CD: L_min = 2 * d_prop * R = 64 Bytes.",
            "6. Hamming(7,4) Even: 0110011.",
        ],
        calculator_type="delay",
    )
