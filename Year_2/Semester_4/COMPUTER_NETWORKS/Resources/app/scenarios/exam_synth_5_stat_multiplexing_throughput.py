"""Synthetic & Realistic Exam 5 Scenario Module.

Contains 1-to-1 representation of all exam questions from Synthetic & Realistic Exam 5:
- Part A: Packet vs circuit switching, Client-Server edge architecture, Queuing delay dynamics,
  OSPF link-state topology requirements, True/False (Control plane, Server static IP, BGP AS).
- Part B: Άσκηση 1 (Multi-hop delays & RTT = 0.6012 s), Άσκηση 2 (Cisco IOS RIPv2 CLI configuration),
  Άσκηση 3 (Fast Ethernet 100M CSMA/CD L_min = 128 Bytes & Transoceanic BDP = 30 Mbits with 8 ms queue delay).
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
    """Constructs and returns Synthetic & Realistic Exam 5 scenario.

    Returns:
        NetworkScenario: The structured scenario object with 1-to-1 parity.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Το πρότυπο διαγώνισμα "),
                TextSegment(
                    text="Synthetic & Realistic Exam 5",
                    is_highlight=True,
                    category="protocol",
                    tag_label="SYNTHETIC REALISTIC 5",
                    tooltip="Ρεαλιστικό διαγώνισμα προσομοίωσης εξετάσεων",
                ),
                TextSegment(text=" αναλύει τα πλεονεκτήματα της "),
                TextSegment(
                    text="Στατιστικής Πολυπλεξίας (Statistical Multiplexing)",
                    is_highlight=True,
                    category="protocol",
                    tag_label="STAT MULTIPLEX",
                    tooltip="Δυναμικός διαμοιρασμός πόρων on-demand",
                ),
                TextSegment(text=", τους υπολογισμούς "),
                TextSegment(
                    text="Καθυστερήσεων σε Σειρά 2 Ζεύξεων (t_total = 0.3006 s)",
                    is_highlight=True,
                    category="delay",
                    tag_label="MULTI-HOP DELAY",
                    tooltip="R1=20kbps, L1=50km, R2=10kbps, L2=100km, P=2000bits",
                ),
                TextSegment(text=" και τη διαμόρφωση "),
                TextSegment(
                    text="Δρομολογητή Cisco RIPv2",
                    is_highlight=True,
                    category="routing",
                    tag_label="CISCO RIPV2",
                    tooltip="Εντολές CLI: router rip, version 2, network...",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="#e06b3a",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Στο δεύτερο μέρος εξετάζεται ο υπολογισμός "),
                TextSegment(
                    text="Ελάχιστου Πλαισίου CSMA/CD Fast Ethernet (128 Bytes)",
                    is_highlight=True,
                    category="error_check",
                    tag_label="CSMA/CD 100M",
                    tooltip="R = 100 Mbps, t_prop = 5.12 μs -> L_min = 128 Bytes",
                ),
                TextSegment(text=", το "),
                TextSegment(
                    text="Υπερωκεάνιο BDP (30 Mbits)",
                    is_highlight=True,
                    category="delay",
                    tag_label="TRANSOCEANIC BDP",
                    tooltip="d = 6000 km, s = 2*10^8 m/s, R = 1 Gbps -> BDP = 30 Mbits",
                ),
                TextSegment(text=" και η "),
                TextSegment(
                    text="Καθυστέρηση Ουράς Buffer (d_queue = 8 ms)",
                    is_highlight=True,
                    category="delay",
                    tag_label="D_QUEUE",
                    tooltip="1 MB buffer / 1 Gbps bandwidth = 8 ms",
                ),
                TextSegment(text="."),
            ]
        ),
    ]

    questions = [
        # Part A - Question 1
        ExamQuestion(
            question_number=1,
            title="Πλεονέκτημα Μεταγωγής Πακέτου έναντι Κυκλώματος",
            question_type="Multiple Choice",
            prompt_text="Ποιο από τα παρακάτω είναι χαρακτηριστικό της μεταγωγής πακέτου (packet switching) σε αντίθεση με τη μεταγωγή κυκλώματος (circuit switching);",
            options=[
                QuestionOption("A", "Η αποκλειστική δέσμευση πόρων εκ των προτέρων.", False, "Αυτό είναι χαρακτηριστικό του circuit switching."),
                QuestionOption("B", "Η δυνατότητα στατιστικής πολυπλεξίας (statistical multiplexing).", True, "Το packet switching μοιράζεται δυναμικά τους πόρους on-demand, επιτρέποντας σε περισσότερους χρήστες να μοιράζονται το κανάλι."),
                QuestionOption("C", "Η αδυναμία απώλειας πακέτων (μηδενικό packet loss).", False, "Στο packet switching μπορεί να υπάρξει απώλεια λόγω υπερχείλισης buffer."),
                QuestionOption("D", "Ο απόλυτα εγγυημένος ρυθμός μετάδοσης για κάθε χρήστη.", False, "Εγγυημένο bandwidth προσφέρει το circuit switching."),
            ],
            correct_option_letter="B",
            detailed_justification="Στη στατιστική πολυπλεξία, οι χρήστες δεσμεύουν εύρος ζώνης μόνο όταν έχουν πραγματικά δεδομένα προς αποστολή, βελτιώνοντας δραματικά την αξιοποίηση του καναλιού.",
        ),
        # Part A - Question 2
        ExamQuestion(
            question_number=2,
            title="Αρχιτεκτονική Θέση Μοντέλου Client-Server",
            question_type="Multiple Choice",
            prompt_text="Το μοντέλο Client-Server ανήκει αρχιτεκτονικά:",
            options=[
                QuestionOption("A", "Στο Network Core (Πυρήνας Δικτύου)", False, "Ο πυρήνας αποτελείται από routers και switches."),
                QuestionOption("B", "Στο Network Edge (Άκρο Δικτύου)", True, "Οι υπολογιστές-πελάτες και οι εξυπηρετητές αποτελούν τα τερματικά συστήματα (end systems) στο άκρο."),
                QuestionOption("C", "Μόνο σε τοπικά δίκτυα (LAN)", False, "Χρησιμοποιείται παγκοσμίως στο Web."),
                QuestionOption("D", "Στο Επίπεδο Σύνδεσης Δεδομένων (Data Link Layer)", False, "Είναι μοντέλο επιπέδου εφαρμογής."),
            ],
            correct_option_letter="B",
            detailed_justification="Οι υπολογιστές-πελάτες και οι εξυπηρετητές αποτελούν τα 'τελικά συστήματα' (end systems) που βρίσκονται στο άκρο του δικτύου (Network Edge).",
        ),
        # Part A - Question 3
        ExamQuestion(
            question_number=3,
            title="Φύση της Καθυστέρησης Ουράς (Queuing Delay)",
            question_type="Multiple Choice",
            prompt_text="Η καθυστέρηση ουράς (queuing delay) σε έναν δρομολογητή:",
            options=[
                QuestionOption("A", "Εξαρτάται αποκλειστικά από την απόσταση μεταξύ των δύο κόμβων.", False, "Αυτό είναι η καθυστέρηση διάδοσης."),
                QuestionOption("B", "Είναι σταθερή και υπολογίζεται ως L/R.", False, "Αυτό είναι η καθυστέρηση μετάδοσης."),
                QuestionOption("C", "Εξαρτάται από τον ρυθμό άφιξης πακέτων (traffic load) και μεταβάλλεται συνεχώς.", True, "Είναι στοχαστική και εξαρτάται από την ένταση κίνησης και την πληρότητα των buffers."),
                QuestionOption("D", "Οφείλεται στο χρόνο ελέγχου των σφαλμάτων (checksum).", False, "Αυτό είναι η καθυστέρηση επεξεργασίας."),
            ],
            correct_option_letter="C",
            detailed_justification="Η καθυστέρηση ουράς εξαρτάται αποκλειστικά από την ένταση κίνησης στον δρομολογητή σε μια δεδομένη χρονική στιγμή. Δεν είναι σταθερή όπως η καθυστέρηση μετάδοσης.",
        ),
        # Part A - Question 4
        ExamQuestion(
            question_number=4,
            title="Χαρακτηριστικά Πρωτοκόλλου OSPF (Link-State)",
            question_type="Multiple Choice",
            prompt_text="Ποιο από τα παρακάτω πρωτόκολλα δρομολόγησης βασίζεται στον αλγόριθμο Κατάστασης Ζεύξης (Link State) και απαιτεί πλήρη γνώση της τοπολογίας;",
            options=[
                QuestionOption("A", "RIP", False, "Το RIP είναι Distance Vector."),
                QuestionOption("B", "OSPF", True, "Το OSPF (Open Shortest Path First) βασίζεται στον αλγόριθμο Dijkstra και κατασκευάζει πλήρη τοπολογικό χάρτη."),
                QuestionOption("C", "BGP", False, "Το BGP είναι Path Vector."),
                QuestionOption("D", "ARP", False, "Το ARP είναι πρωτόκολλο L2/L3 αντιστοίχισης διευθύνσεων."),
            ],
            correct_option_letter="B",
            detailed_justification="Το OSPF βασίζεται στον αλγόριθμο Dijkstra και είναι ένα Link State πρωτόκολλο που χτίζει πλήρη τοπολογικό χάρτη της περιοχής.",
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
                QuestionOption("A", "1: Σ, 2: Σ, 3: Σ", False, "Οι servers απαιτούν στατικές IPs."),
                QuestionOption("B", "1: Σ, 2: Λ, 3: Σ", True, "1=Σ (Control plane routing algorithms), 2=Λ (Στατική IP για διαθεσιμότητα), 3=Σ (BGP είναι inter-AS routing protocol)."),
                QuestionOption("C", "1: Λ, 2: Λ, 3: Σ", False, "Το Control plane είναι όντως υπεύθυνο για τον υπολογισμό διαδρομών."),
                QuestionOption("D", "1: Σ, 2: Λ, 3: Λ", False, "Το BGP είναι το παγκόσμιο πρότυπο μεταξύ AS."),
            ],
            correct_option_letter="B",
            detailed_justification=(
                "1. **Σωστό:** Το Control Plane εκτελεί τους αλγορίθμους δρομολόγησης και συντάσσει το Routing Table.\n"
                "2. **Λάθος:** Οι Servers απαιτούν μόνιμη, στατική IP ώστε να είναι αξιόπιστα προσβάσιμοι στους clients.\n"
                "3. **Σωστό:** Το BGP είναι το de facto πρότυπο δρομολόγησης μεταξύ διαφορετικών Αυτόνομων Συστημάτων (AS) στο διαδίκτυο."
            ),
        ),
        # Part B - Άσκηση 1
        ExamQuestion(
            question_number=6,
            title="Άσκηση 1: Υπολογισμός Καθυστερήσεων & RTT σε 2 Ζεύξεις",
            question_type="Calculations",
            prompt_text=(
                "Έστω δίκτυο: `(A) ============ (B) ============ (C)`\n"
                "Link 1: R1 = 20000 bps, L1 = 50 km, u1 = 2.5*10^8 m/s.\n"
                "Link 2: R2 = 10000 bps, L2 = 100 km, u2 = 2.5*10^8 m/s.\n"
                "Μέγεθος πακέτου P = 2000 bits. (Αγνοήστε ουρές και d_proc).\n\n"
                "**a.** Χρόνος αποστολής πακέτου από A σε C.\n"
                "**b.** RTT για αποστολή από A σε C και άμεση επιστροφή (A -> C -> A)."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Καθυστερήσεις Ζεύξης 1 (A -> B)",
                    formula="d_trans1 = P / R1  &&  d_prop1 = L1 / u1",
                    substitution="2000 / 20000 = 0.1 s | 50,000 / 2.5*10^8 = 0.2 ms = 0.0002 s",
                    result="d_trans1 = 0.1 s | d_prop1 = 0.2 ms",
                    rationale="Μετάδοση και διάδοση στην πρώτη ζεύξη.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Καθυστερήσεις Ζεύξης 2 (B -> C)",
                    formula="d_trans2 = P / R2  &&  d_prop2 = L2 / u2",
                    substitution="2000 / 10000 = 0.2 s | 100,000 / 2.5*10^8 = 0.4 ms = 0.0004 s",
                    result="d_trans2 = 0.2 s | d_prop2 = 0.4 ms",
                    rationale="Μετάδοση και διάδοση στη δεύτερη ζεύξη.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Ερώτημα a: Συνολικός Χρόνος Μετάβασης A -> C",
                    formula="t_total = d_trans1 + d_prop1 + d_trans2 + d_prop2",
                    substitution="0.1 + 0.0002 + 0.2 + 0.0004",
                    result="0.3006 s",
                    rationale="Χρόνος ολοκλήρωσης της λήψης του πακέτου στον κόμβο C.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Ερώτημα b: Συνολικό RTT (A -> C -> A)",
                    formula="RTT = 2 * t_total",
                    substitution="2 * 0.3006 s",
                    result="0.6012 s",
                    rationale="Χρόνος μετάβασης και συμμετρικής επιστροφής του πακέτου.",
                ),
            ],
            detailed_justification=(
                "- **a.** $t_{\\text{total}} = 0,1 + 0,0002 + 0,2 + 0,0004 = 0,3006\\text{ s}$\n"
                "- **b.** $\\text{RTT} = 2 \\times 0,3006 = 0,6012\\text{ s}$"
            ),
        ),
        # Part B - Άσκηση 2
        ExamQuestion(
            question_number=7,
            title="Άσκηση 2: Διαμόρφωση Cisco IOS RIPv2 με 3 Interfaces",
            question_type="Calculations",
            prompt_text=(
                "Για δρομολογητή Cisco με interfaces Fa0/0 (192.168.10.0/24), Se0/0/0 (10.0.1.0/30) "
                "και Se0/0/1 (10.0.2.0/30), ορίστε πλήρη διαμόρφωση RIPv2 συμπληρώνοντας τις εντολές CLI."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Είσοδος σε Global Configuration Mode",
                    formula="configure terminal",
                    substitution="R# configure terminal",
                    result="R(config)#",
                    rationale="Απαραίτητο για είσοδο στις παραμέτρους του δρομολογητή.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ενεργοποίηση RIPv2 & no auto-summary",
                    formula="router rip -> version 2 -> no auto-summary",
                    substitution="router rip | version 2 | no auto-summary",
                    result="Classless routing",
                    rationale="Αποτρέπει την αυτόματη σύνοψη στα classful όρια.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Δήλωση Υποδικτύων",
                    formula="network <net_id>",
                    substitution="network 192.168.10.0 | network 10.0.1.0 | network 10.0.2.0",
                    result="Ενεργοποίηση RIP στα 3 interfaces",
                    rationale="Διαφημίζει τα υποδίκτυα και ενεργοποιεί αποστολή/λήψη RIP updates.",
                ),
            ],
            detailed_justification=(
                "```text\n"
                "R>en\n"
                "R# configure terminal\n"
                "R(config)# router rip\n"
                "R(config-router)# version 2\n"
                "R(config-router)# no auto-summary\n"
                "R(config-router)# network 192.168.10.0\n"
                "R(config-router)# network 10.0.1.0\n"
                "R(config-router)# network 10.0.2.0\n"
                "R(config-router)# end\n"
                "```"
            ),
        ),
        # Part B - Άσκηση 3
        ExamQuestion(
            question_number=8,
            title="Άσκηση 3: CSMA/CD Fast Ethernet L_min & Υπερωκεάνιο BDP με Buffer Delay",
            question_type="Calculations",
            prompt_text=(
                "**a.** Δίκτυο Fast Ethernet 100 Mbps με μέγιστο χρόνο διάδοσης t_prop = 5.12 μs. "
                "Υπολογίστε το ελάχιστο μέγεθος πλαισίου σε Bytes.\n\n"
                "**b.** Υπερωκεάνια ζεύξη d = 6.000 km, s = 2*10^8 m/s, R = 1 Gbps και buffer = 1.000.000 Bytes.\n"
                "- i. Καθυστέρηση διάδοσης d_prop.\n"
                "- ii. Bandwidth-Delay Product (BDP).\n"
                "- iii. Καθυστέρηση ουράς d_queue όταν ο buffer είναι γεμάτος."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ερώτημα a: Ελάχιστο Πλαίσιο CSMA/CD στα 100 Mbps",
                    formula="L_min = 2 * t_prop * R",
                    substitution="2 * (5.12 * 10^-6 s) * (100 * 10^6 bps)",
                    result="1024 bits = 128 Bytes",
                    rationale="Στα 100 Mbps με μεγαλύτερο t_prop, το ελάχιστο πλαίσιο είναι 128 Bytes.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ερώτημα b.i: Καθυστέρηση Διάδοσης d_prop",
                    formula="d_prop = d / s",
                    substitution="(6,000 * 10^3 m) / (2 * 10^8 m/s)",
                    result="0.03 s = 30 ms",
                    rationale="Χρόνος διάδοσης στην οπτική ίνα 6.000 km.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Ερώτημα b.ii: Υπολογισμός BDP",
                    formula="BDP = R * d_prop",
                    substitution="10^9 bps * 0.03 s",
                    result="30,000,000 bits = 30 Mbits (3.75 MB)",
                    rationale="Χωρητικότητα bits εν πτήσει μέσα στην υπερωκεάνια ίνα.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Ερώτημα b.iii: Καθυστέρηση Ουράς Buffer",
                    formula="d_queue = Buffer_bits / R",
                    substitution="(1,000,000 Bytes * 8) / 10^9 bps = 8,000,000 / 10^9",
                    result="0.008 s = 8 ms",
                    rationale="Χρόνος για να αδειάσει το 1 MB buffer του router με ρυθμό 1 Gbps.",
                ),
            ],
            detailed_justification=(
                "- **a.** $L_{\\text{min}} = 2 \\times (5,12 \\times 10^{-6}) \\times 10^8 = 1024\\text{ bits} = 128\\text{ Bytes}$\n"
                "- **b.i.** $d_{\\text{prop}} = \\frac{6 \\times 10^6}{2 \\times 10^8} = 0,03\\text{ s} = 30\\text{ ms}$\n"
                "- **b.ii.** $\\text{BDP} = 10^9 \\times 0,03 = 30.000.000\\text{ bits} = 30\\text{ Mbits} = 3,75\\text{ MB}$\n"
                "- **b.iii.** $d_{\\text{queue}} = \\frac{10^6 \\times 8}{10^9} = 0,008\\text{ s} = 8\\text{ ms}$."
            ),
        ),
    ]

    nodes = [
        TopologyNode("r_trans1", "Router Europe", "router", 120, 150, "192.168.10.1"),
        TopologyNode("r_trans2", "Router US Coast", "router", 620, 150, "10.0.1.1"),
        TopologyNode("srv_us", "US Data Center", "server", 850, 150, "10.0.2.10"),
    ]

    links = [
        TopologyLink("r_trans1", "r_trans2", 1000, 6000.0, 2.0, "fiber", "1G Transatlantic | 6000km"),
        TopologyLink("r_trans2", "srv_us", 10000, 10.0, 2.0, "fiber", "10G Metro"),
    ]

    return NetworkScenario(
        id="exam_synth_5",
        title="Synthetic Exam 5: Stat Multiplexing & BDP",
        subtitle="Statistical Multiplexing, Multi-Hop Delays, Cisco RIPv2, CSMA/CD 100M & Transoceanic BDP",
        course_tag="Synthetic Realistic",
        duration_info="2 ώρες και 15 λεπτά",
        paragraphs=paragraphs,
        questions=questions,
        nodes=nodes,
        links=links,
        methodology_summary=[
            "1. Statistical Multiplexing: On-demand bandwidth allocation.",
            "2. Multi-hop Delays: t_total = 0.3006 s, RTT = 0.6012 s.",
            "3. Cisco RIPv2: router rip -> version 2 -> no auto-summary -> network.",
            "4. CSMA/CD 100M: L_min = 2 * 5.12μs * 100Mbps = 128 Bytes.",
            "5. Transoceanic BDP = 1 Gbps * 30 ms = 30 Mbits.",
            "6. d_queue = 1 MB / 1 Gbps = 8 ms.",
        ],
        calculator_type="delay",
    )
