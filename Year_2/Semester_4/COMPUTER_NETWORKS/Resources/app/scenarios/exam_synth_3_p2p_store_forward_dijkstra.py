"""Synthetic Exam 3: P2P, Store-and-Forward & End-to-End Delays.

Covers Peer-to-Peer vs Client-Server, Store-and-Forward packet transmission,
Traceroute TTL mechanism, /26 subnet matching, and multi-hop delay calculations.
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
    """Constructs and returns Synthetic Exam 3 scenario.

    Returns:
        NetworkScenario: The structured scenario object.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Το διαγώνισμα προσομοίωσης "),
                TextSegment(
                    text="Synthetic & Realistic Exam 3",
                    is_highlight=True,
                    category="protocol",
                    tag_label="SYNTHETIC EXAM",
                    tooltip="Ρεαλιστικό διαγώνισμα προσομοίωσης εξετάσεων",
                ),
                TextSegment(text=" εστιάζει στην αρχιτεκτονική "),
                TextSegment(
                    text="Peer-to-Peer (P2P)",
                    is_highlight=True,
                    category="protocol",
                    tag_label="P2P",
                    tooltip="Κάθε κόμβος λειτουργεί ταυτόχρονα ως client και server",
                ),
                TextSegment(text=", στην αρχή λειτουργίας του "),
                TextSegment(
                    text="Store-and-Forward σε Δρομολογητές",
                    is_highlight=True,
                    category="routing",
                    tag_label="STORE & FORWARD",
                    tooltip="Λήψη ολόκληρου του πακέτου πριν την επαναπροώθηση",
                ),
                TextSegment(text=" και στη λειτουργία του εργαλείου "),
                TextSegment(
                    text="Traceroute μέσω πεδίου TTL (Time-To-Live)",
                    is_highlight=True,
                    category="protocol",
                    tag_label="TRACEROUTE TTL",
                    tooltip="Ανακάλυψη ενδιάμεσων δρομολογητών με ICMP Time Exceeded",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="#e06b3a",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Στο υπολογιστικό μέρος περιλαμβάνεται πλήρης άσκηση υπολογισμού "),
                TextSegment(
                    text="End-to-End Delay για N = 3 Hops",
                    is_highlight=True,
                    category="delay",
                    tag_label="3 HOPS DELAY",
                    tooltip="d = 1000 km, s = 2*10^8 m/s, R = 10 Mbps, L = 10000 bits",
                ),
                TextSegment(text=" με ενδιάμεση επεξεργασία και σύγκριση "),
                TextSegment(
                    text="Υποδικτύωσης IPv4 /26",
                    is_highlight=True,
                    category="routing",
                    tag_label="SUBNET /26",
                    tooltip="Μάσκα 255.255.255.192, Block Size 64 (192-255)",
                ),
                TextSegment(text="."),
            ]
        ),
    ]

    questions = [
        ExamQuestion(
            question_number=1,
            title="Χαρακτηριστικά Αρχιτεκτονικής Peer-to-Peer (P2P)",
            question_type="Multiple Choice",
            prompt_text="Σε ένα καθαρό Peer-to-Peer (P2P) δίκτυο, ποιο από τα παρακάτω ισχύει;",
            options=[
                QuestionOption("A", "Η αξιοπιστία του δικτύου εξαρτάται αποκλειστικά από έναν κεντρικό Server.", False, "Στο P2P δεν υπάρχει κεντρικός server (αποκεντρωμένο)."),
                QuestionOption("B", "Η προσθήκη νέων χρηστών μειώνει πάντα το διαθέσιμο bandwidth.", False, "Οι νέοι χρήστες φέρνουν και upload capacity (αυτο-κλιμάκωση / self-scalability)."),
                QuestionOption("C", "Κάθε κόμβος (peer) λειτουργεί ταυτόχρονα ως client και ως server.", True, "Κάθε peer ζητά αρχεία (client) και ταυτόχρονα εξυπηρετεί άλλους χρήστες (server)."),
                QuestionOption("D", "Είναι αδύνατη η κοινή χρήση αρχείων.", False, "Το P2P χρησιμοποιείται κατά κόρον για file sharing (BitTorrent)."),
            ],
            correct_option_letter="C",
            detailed_justification="Στο μοντέλο Peer-to-Peer όλοι οι κόμβοι είναι ισότιμοι (servents = server + client), προσφέροντας φυσική αυτο-κλιμάκωση.",
        ),
        ExamQuestion(
            question_number=2,
            title="Αρχή Λειτουργίας Store-and-Forward",
            question_type="Multiple Choice",
            prompt_text="Η λειτουργία 'Store-and-Forward' σε έναν δρομολογητή (router) σημαίνει ότι:",
            options=[
                QuestionOption("A", "Ο δρομολογητής πρέπει να λάβει ολόκληρο το πακέτο πριν αρχίσει την προώθησή του.", True, "Πρέπει να ληφθούν όλα τα bits του L ώστε να ελεγχθεί το checksum/CRC πριν αρχίσει η μετάδοση στην επόμενη ζεύξη."),
                QuestionOption("B", "Ο δρομολογητής αποθηκεύει τα πακέτα μόνιμα στο σκληρό του δίσκο.", False, "Αποθηκεύονται προσωρινά σε μνήμη RAM buffer."),
                QuestionOption("C", "Η προώθηση ξεκινά μόλις ληφθεί μόνο η επικεφαλίδα (Cut-through switching).", False, "Αυτό είναι Cut-through switching, όχι Store-and-Forward."),
                QuestionOption("D", "Ο δρομολογητής δεν ελέγχει ποτέ για σφάλματα.", False, "Εκτελεί πλήρη έλεγχο επικεφαλίδας IPv4 checksum."),
            ],
            correct_option_letter="A",
            detailed_justification="Το Store-and-Forward εισάγει καθυστέρηση μετάδοσης (L/R) σε κάθε ενδιάμεσο κόμβο (hop), καθώς το πακέτο πρέπει να αποθηκευτεί ολόκληρο πριν προωθηθεί.",
        ),
        ExamQuestion(
            question_number=3,
            title="Υπολογισμός End-to-End Delay για N = 3 Hops",
            question_type="Calculations",
            prompt_text="Έστω διαδρομή από Host A σε Host B μέσω 2 δρομολογητών (N = 3 hops). Κάθε ζεύξη έχει d = 1000 km, s = 2*10^8 m/s, R = 10 Mbps. Πακέτο L = 10.000 bits αποστέλλεται από το A στο B. Υπολογίστε τη συνολική καθυστέρηση (αγνοώντας ουρές και d_proc).",
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Καθυστέρηση Μετάδοσης ανά Hop (d_trans)",
                    formula="d_trans = L / R = 10,000 bits / (10 * 10^6 bps)",
                    substitution="10,000 / 10,000,000",
                    result="1 * 10^-3 s = 1 ms",
                    rationale="Χρόνος για να τεθούν όλα τα bits σε μία ζεύξη.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Καθυστέρηση Διάδοσης ανά Hop (d_prop)",
                    formula="d_prop = d / s = 1,000,000 m / (2 * 10^8 m/s)",
                    substitution="10^6 / (2 * 10^8)",
                    result="5 * 10^-3 s = 5 ms",
                    rationale="Χρόνος ταξιδιού του σήματος σε απόσταση 1.000 km.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Συνολική Καθυστέρηση σε 3 Hops",
                    formula="T_total = N * d_trans + N * d_prop",
                    substitution="3 * 1.0 ms + 3 * 5.0 ms",
                    result="3 ms + 15 ms = 18 ms",
                    rationale="Το πακέτο μεταδίδεται 3 φορές (A->R1, R1->R2, R2->B) και διαδίδεται 3 φορές.",
                ),
            ],
            detailed_justification="Σε 3 διαδοχικές ζεύξεις με Store-and-Forward, το συνολικό delay είναι T = 3 * (1 ms + 5 ms) = 18 ms.",
        ),
    ]

    nodes = [
        TopologyNode("h_a", "Host A", "host", 100, 150, "172.16.30.1/26"),
        TopologyNode("r_1", "Router 1", "router", 350, 150, "172.16.30.65/26"),
        TopologyNode("r_2", "Router 2", "router", 600, 150, "172.16.30.129/26"),
        TopologyNode("h_b", "Host B", "host", 850, 150, "172.16.30.200/26"),
    ]

    links = [
        TopologyLink("h_a", "r_1", 10, 1000.0, 2.0, "fiber", "10M | 1000km"),
        TopologyLink("r_1", "r_2", 10, 1000.0, 2.0, "fiber", "10M | 1000km"),
        TopologyLink("r_2", "h_b", 10, 1000.0, 2.0, "fiber", "10M | 1000km"),
    ]

    return NetworkScenario(
        id="exam_synth_3",
        title="Synthetic Exam 3: P2P & Store-and-Forward",
        subtitle="P2P Architecture, Store-and-Forward, Traceroute & 3-Hop Delays",
        course_tag="Synthetic Exam",
        duration_info="2 ώρες και 15 λεπτά",
        paragraphs=paragraphs,
        questions=questions,
        nodes=nodes,
        links=links,
        methodology_summary=[
            "1. P2P: Servents (Clients + Servers ταυτόχρονα).",
            "2. Store-and-Forward: Λήψη πλήρους πακέτου L πριν τη μετάδοση.",
            "3. 3-Hop Delay = 3 * (L/R + d/s) = 3*(1ms + 5ms) = 18 ms.",
        ],
        calculator_type="delay",
    )
