"""Synthetic Exam 5: Statistical Multiplexing, Throughput & CSMA/CD.

Covers Statistical Multiplexing, Multi-hop Delays & RTT with d_proc,
Cisco IOS RIPv2 configuration, CSMA/CD 100Mbps Fast Ethernet (128 Bytes),
Transoceanic BDP (30 Mbits) and Buffer Queuing Delay (8 ms).
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
    """Constructs and returns Synthetic Exam 5 scenario.

    Returns:
        NetworkScenario: The structured scenario object.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Το πρότυπο διαγώνισμα "),
                TextSegment(
                    text="Synthetic & Realistic Exam 5",
                    is_highlight=True,
                    category="protocol",
                    tag_label="SYNTHETIC EXAM",
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
                TextSegment(text="Στο δεύτερο μέρος υπολογίζεται το "),
                TextSegment(
                    text="Ελάχιστο Μέγεθος Πλαισίου CSMA/CD σε 100 Mbps (128 Bytes)",
                    is_highlight=True,
                    category="error_check",
                    tag_label="CSMA/CD 100M",
                    tooltip="L_min = 2 * 5.12μs * 100Mbps = 1024 bits = 128 Bytes",
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
        ExamQuestion(
            question_number=1,
            title="Πλεονέκτημα Μεταγωγής Πακέτου έναντι Κυκλώματος",
            question_type="Multiple Choice",
            prompt_text="Ποιο από τα παρακάτω είναι χαρακτηριστικό της μεταγωγής πακέτου (packet switching) σε αντίθεση με τη μεταγωγή κυκλώματος (circuit switching);",
            options=[
                QuestionOption("A", "Η αποκλειστική δέσμευση πόρων εκ των προτέρων.", False, "Αυτό είναι χαρακτηριστικό του circuit switching."),
                QuestionOption("B", "Η δυνατότητα στατιστικής πολυπλεξίας (statistical multiplexing).", True, "Το packet switching μοιράζεται δυναμικά τους πόρους, επιτρέποντας σε περισσότερους χρήστες να μοιράζονται το κανάλι."),
                QuestionOption("C", "Η αδυναμία απώλειας πακέτων (μηδενικό packet loss).", False, "Στο packet switching μπορεί να υπάρξει απώλεια λόγω υπερχείλισης ουράς."),
                QuestionOption("D", "Ο απόλυτα εγγυημένος ρυθμός μετάδοσης για κάθε χρήστη.", False, "Εγγυημένο bandwidth προσφέρει το circuit switching."),
            ],
            correct_option_letter="B",
            detailed_justification="Στη στατιστική πολυπλεξία, οι χρήστες δεσμεύουν εύρος ζώνης μόνο όταν έχουν πραγματικά δεδομένα προς αποστολή, βελτιώνοντας δραματικά την αξιοποίηση του καναλιού.",
        ),
        ExamQuestion(
            question_number=2,
            title="Υπολογισμός Ελάχιστου Πλαισίου CSMA/CD σε 100 Mbps",
            question_type="Calculations",
            prompt_text="Ένα δίκτυο Fast Ethernet χρησιμοποιεί CSMA/CD με R = 100 Mbps. Αν ο μέγιστος χρόνος διάδοσης μονής κατεύθυνσης είναι t_prop = 5.12 μs, ποιο είναι το ελάχιστο μέγεθος πλαισίου σε Bytes;",
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Εφαρμογή Κριτηρίου L_min",
                    formula="L_min = 2 * t_prop * R",
                    substitution="2 * (5.12 * 10^-6 s) * (100 * 10^6 bps)",
                    result="1024 bits",
                    rationale="Ο χρόνος μετάδοσης πρέπει να είναι τουλάχιστον ίσος με το RTT (2 * t_prop).",
                ),
                CalculationStep(
                    step_number=2,
                    title="Μετατροπή σε Bytes",
                    formula="L_min (Bytes) = 1024 / 8",
                    substitution="1024 / 8",
                    result="128 Bytes",
                    rationale="Στο 100 Mbps Fast Ethernet με μεγαλύτερη απόσταση, το L_min είναι 128 Bytes (διπλάσιο από το κλασικό 64 Bytes).",
                ),
            ],
            detailed_justification="L_min = 2 * 5.12 μs * 100 Mbps = 1024 bits = 128 Bytes.",
        ),
        ExamQuestion(
            question_number=3,
            title="Υπολογισμός BDP και Καθυστέρησης Ουράς (Buffer)",
            question_type="Calculations",
            prompt_text="Ζεύξη 6.000 km με s = 2*10^8 m/s και Bandwidth R = 1 Gbps. Βρείτε το d_prop, το BDP και την καθυστέρηση ουράς d_queue αν ο buffer περιέχει 1.000.000 Bytes.",
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Καθυστέρηση Διάδοσης d_prop",
                    formula="d_prop = d / s = (6,000 * 10^3 m) / (2 * 10^8 m/s)",
                    substitution="6 * 10^6 / (2 * 10^8)",
                    result="0.03 s = 30 ms",
                    rationale="Χρόνος ταξιδιού φωτεινού παλμού στην υπερωκεάνια οπτική ίνα.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Bandwidth-Delay Product (BDP)",
                    formula="BDP = R * d_prop = (10^9 bps) * 0.03 s",
                    substitution="1,000,000,000 * 0.03",
                    result="30,000,000 bits = 30 Mbits (3.75 MB)",
                    rationale="Μέγιστος αριθμός bits που βρίσκονται μέσα στο καλώδιο.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Καθυστέρηση Ουράς d_queue",
                    formula="d_queue = Buffer_bits / R_out = (1,000,000 * 8 bits) / 10^9 bps",
                    substitution="8,000,000 / 1,000,000,000",
                    result="8 * 10^-3 s = 8 ms",
                    rationale="Χρόνος για να αδειάσει το 1 MB buffer του router με ρυθμό 1 Gbps.",
                ),
            ],
            detailed_justification="d_prop = 30 ms, BDP = 30 Mbits (3.75 MB), d_queue = 8 ms.",
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
        subtitle="Statistical Multiplexing, Multi-Hop Delays, CSMA/CD 100M & Transoceanic BDP",
        course_tag="Synthetic Exam",
        duration_info="2 ώρες και 15 λεπτά",
        paragraphs=paragraphs,
        questions=questions,
        nodes=nodes,
        links=links,
        methodology_summary=[
            "1. Statistical Multiplexing: On-demand bandwidth allocation.",
            "2. CSMA/CD 100M: L_min = 2 * 5.12μs * 100Mbps = 128 Bytes.",
            "3. Transoceanic BDP = 1 Gbps * 30 ms = 30 Mbits.",
            "4. d_queue = 1 MB / 1 Gbps = 8 ms.",
        ],
        calculator_type="delay",
    )
