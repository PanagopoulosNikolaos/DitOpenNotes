"""Synthetic Exam 4: Encapsulation, TCP Timeout, Dijkstra & Hamming Codes.

Covers Encapsulation, Collision vs Broadcast Domains, TCP Timeout estimation,
BDP sliding window sizing, Dijkstra Link-State execution, and Hamming Error-Correcting Code.
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
    """Constructs and returns Synthetic Exam 4 scenario.

    Returns:
        NetworkScenario: The structured scenario object.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Το πρότυπο διαγώνισμα "),
                TextSegment(
                    text="Synthetic & Realistic Exam 4",
                    is_highlight=True,
                    category="protocol",
                    tag_label="SYNTHETIC EXAM",
                    tooltip="Ρεαλιστικό διαγώνισμα προσομοίωσης εξετάσεων",
                ),
                TextSegment(text=" εξετάζει τη διαδικασία "),
                TextSegment(
                    text="Ενθυλάκωσης (Encapsulation)",
                    is_highlight=True,
                    category="protocol",
                    tag_label="ENCAPSULATION",
                    tooltip="Προσθήκη επικεφαλίδων σε κάθε επίπεδο",
                ),
                TextSegment(text=", τον διαχωρισμό "),
                TextSegment(
                    text="Collision Domains (Switches) vs Broadcast Domains (Routers)",
                    is_highlight=True,
                    category="device",
                    tag_label="DOMAINS",
                    tooltip="Οριοθέτηση πεδίων συγκρούσεων και εκπομπής",
                ),
                TextSegment(text=", τον υπολογισμό "),
                TextSegment(
                    text="TCP Timeout & Sliding Window (BDP = R * RTT)",
                    is_highlight=True,
                    category="delay",
                    tag_label="TCP BDP",
                    tooltip="R = 200 Mbps, RTT = 50 ms -> Window = 1.25 MB",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="#e06b3a",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Στο δεύτερο μέρος εκτελείται ο αλγόριθμος "),
                TextSegment(
                    text="Dijkstra Shortest Path σε Γράφο 7 Κόμβων",
                    is_highlight=True,
                    category="routing",
                    tag_label="DIJKSTRA",
                    tooltip="Βέλτιστο μονοπάτι από A σε G με κόστος 5 (A -> D -> G)",
                ),
                TextSegment(text=" και κατασκευάζεται "),
                TextSegment(
                    text="Κώδικας Διόρθωσης Σφαλμάτων Hamming (Odd Parity)",
                    is_highlight=True,
                    category="error_check",
                    tag_label="HAMMING CODE",
                    tooltip="2^p >= d + p + 1 -> p = 3 bits ισοτιμίας για d = 4 bits",
                ),
                TextSegment(text="."),
            ]
        ),
    ]

    questions = [
        ExamQuestion(
            question_number=1,
            title="Διαδικασία Ενθυλάκωσης (Encapsulation)",
            question_type="Multiple Choice",
            prompt_text="Στη διαδικασία 'Ενθυλάκωσης' (Encapsulation), όταν τα δεδομένα μεταφέρονται από το Επίπεδο Εφαρμογής προς το Φυσικό Επίπεδο:",
            options=[
                QuestionOption("A", "Αφαιρούνται οι κεφαλίδες (headers) σε κάθε επίπεδο.", False, "Αυτό είναι αποενθυλάκωση (decapsulation) στον παραλήπτη."),
                QuestionOption("B", "Τα δεδομένα κρυπτογραφούνται υποχρεωτικά από το Data Link Layer.", False, "Η κρυπτογράφηση γίνεται συνήθως στο TLS/Application layer."),
                QuestionOption("C", "Προστίθεται νέα κεφαλίδα σε κάθε επίπεδο, δημιουργώντας τελικά το πλαίσιο στο Επίπεδο 2.", True, "Κάθε επίπεδο προσθέτει το δικό του header (NH, TH, DH/DT) γύρω από το payload."),
                QuestionOption("D", "Η διεύθυνση IP αλλάζει σε κάθε επίπεδο.", False, "Η IP ανήκει αποκλειστικά στο Network Layer."),
            ],
            correct_option_letter="C",
            detailed_justification="Στην αποστολή (Encapsulation), τα δεδομένα κατεβαίνουν στη στοίβα πρωτοκόλλων και σε κάθε στάδιο προστίθεται header (και trailer στο L2).",
        ),
        ExamQuestion(
            question_number=2,
            title="Υπολογισμός TCP Sliding Window (BDP)",
            question_type="Calculations",
            prompt_text="Έστω σύνδεση FTP με Bandwidth R = 200 Mbps και RTT = 50 ms. Για 100% αξιοποίηση του καναλιού χωρίς idle time, ποιο πρέπει να είναι το ελάχιστο μέγεθος του Sliding Window σε MB;",
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Υπολογισμός Bandwidth-Delay Product (BDP)",
                    formula="Window Size = Bandwidth * RTT",
                    substitution="(200 * 10^6 bps) * 0.050 s",
                    result="10,000,000 bits",
                    rationale="Όγκος δεδομένων που εκπέμπονται κατά τη διάρκεια ενός γύρου RTT.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Μετατροπή σε Bytes και MBytes",
                    formula="Window (Bytes) = 10,000,000 / 8",
                    substitution="1,250,000 Bytes",
                    result="1.25 MBytes",
                    rationale="Απαιτείται παράθυρο τουλάχιστον 1.25 MB για να μη σταματήσει ο αποστολέας περιμένοντας ACKs.",
                ),
            ],
            detailed_justification="Window = Bandwidth * RTT = 200 Mbps * 0.05 s = 10 Mbits = 1.25 MB.",
        ),
        ExamQuestion(
            question_number=3,
            title="Κώδικας Hamming (d = 4 bits, Περιττή Ισοτιμία)",
            question_type="Calculations",
            prompt_text="Αποστολέας θέλει να μεταδώσει τα δεδομένα D = 1101 με κώδικα Hamming (Odd Parity). Βρείτε τον αριθμό bits ισοτιμίας p και το τελικό μεταδιδόμενο μήνυμα.",
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Εύρεση Αριθμού Bits Ισοτιμίας p",
                    formula="2^p >= d + p + 1",
                    substitution="2^p >= 4 + p + 1  <=>  2^p >= p + 5",
                    result="p = 3 bits (γιατί 2^3 = 8 >= 8)",
                    rationale="Χρειάζονται 3 bits ισοτιμίας στις θέσεις 1, 2, 4 (δυνάμεις του 2). Συνολικό μήκος 7 bits.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Υπολογισμός Bits Ισοτιμίας (Odd Parity / Περιττή Ισοτιμία)",
                    formula="P1 (θέσεις 1,3,5,7), P2 (2,3,6,7), P4 (4,5,6,7)",
                    substitution="D = 1101 στις θέσεις (3,5,6,7) -> D1=1, D2=1, D3=0, D4=1",
                    result="P1=0, P2=1, P4=1",
                    rationale="Με περιττή ισοτιμία, ο συνολικός αριθμός των '1' σε κάθε ομάδα πρέπει να είναι μονός.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Τελικό Μεταδιδόμενο Μήνυμα 7 Bits",
                    formula="[P1, P2, D1, P4, D2, D3, D4]",
                    substitution="[0, 1, 1, 1, 1, 0, 1]",
                    result="0111101",
                    rationale="Το πλαίσιο προστατεύεται από μονά σφάλματα και μπορεί να τα διορθώσει αυτόματα.",
                ),
            ],
            detailed_justification="Κώδικας Hamming(7,4): 4 bits δεδομένων + 3 bits ισοτιμίας = 7 bits (0111101).",
        ),
    ]

    nodes = [
        TopologyNode("n_a", "Node A", "router", 120, 150, "10.0.1.1"),
        TopologyNode("n_b", "Node B", "router", 320, 80, "10.0.1.2"),
        TopologyNode("n_c", "Node C", "router", 320, 220, "10.0.2.2"),
        TopologyNode("n_d", "Node D", "router", 520, 150, "10.0.3.1"),
        TopologyNode("n_g", "Node G", "host", 750, 150, "10.0.4.1"),
    ]

    links = [
        TopologyLink("n_a", "n_b", 100, 10.0, 2.0, "fiber", "Cost: 2"),
        TopologyLink("n_a", "n_c", 100, 5.0, 2.0, "copper", "Cost: 1"),
        TopologyLink("n_a", "n_d", 100, 15.0, 2.0, "fiber", "Cost: 3"),
        TopologyLink("n_d", "n_g", 100, 10.0, 2.0, "fiber", "Cost: 2"),
    ]

    return NetworkScenario(
        id="exam_synth_4",
        title="Synthetic Exam 4: TCP BDP, Dijkstra & Hamming",
        subtitle="Encapsulation, TCP Sliding Window (BDP = 1.25MB), Dijkstra & Hamming(7,4)",
        course_tag="Synthetic Exam",
        duration_info="2 ώρες και 15 λεπτά",
        paragraphs=paragraphs,
        questions=questions,
        nodes=nodes,
        links=links,
        methodology_summary=[
            "1. Encapsulation: Header addition per layer.",
            "2. TCP Sliding Window = Bandwidth * RTT = 200 Mbps * 50 ms = 1.25 MB.",
            "3. Hamming(7,4): 2^p >= d + p + 1 (p = 3 bits).",
        ],
        calculator_type="delay",
    )
