"""Past Exam Comprehensive Archive Scenario Module.

Contains all questions from the archival exam paper:
- The 4 Nodal Delays (d_proc, d_queue, d_trans, d_prop)
- Bandwidth-Delay Product (BDP)
- OSPF Area Configuration
- BGP Path Routing & Autonomous Systems
- Multi-hop RTT Calculations with Intermediate Router Processing
- Dijkstra Shortest Path Algorithm Execution
- CSMA/CD Minimum Frame Size Criteria
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
    """Constructs and returns the comprehensive archival exam scenario.

    Returns:
        NetworkScenario: The structured scenario object.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Το αρχειακό γραπτό εξέτασης "),
                TextSegment(
                    text="Δίκτυα Υπολογιστών (Comprehensive Archive)",
                    is_highlight=True,
                    category="protocol",
                    tag_label="ΑΡΧΕΙΟ",
                    tooltip="Συγκεντρωτική εξέταση όλων των ενοτήτων του μαθήματος",
                ),
                TextSegment(text=" περιλαμβάνει πλήρη ανάλυση της "),
                TextSegment(
                    text="Κομβικής Καθυστέρησης d_nodal = d_proc + d_queue + d_trans + d_prop",
                    is_highlight=True,
                    category="delay",
                    tag_label="4 DELAYS",
                    tooltip="Ανάλυση των 4 συνιστωσών καθυστέρησης",
                ),
                TextSegment(text=", υπολογισμό του "),
                TextSegment(
                    text="BDP (Bandwidth-Delay Product)",
                    is_highlight=True,
                    category="delay",
                    tag_label="BDP",
                    tooltip="Χωρητικότητα ζεύξης σε bits",
                ),
                TextSegment(text=" και διαμόρφωση πρωτοκόλλου "),
                TextSegment(
                    text="OSPF σε Single Area",
                    is_highlight=True,
                    category="routing",
                    tag_label="OSPF",
                    tooltip="Διαμόρφωση Open Shortest Path First",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="#e06b3a",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Στο δεύτερο μέρος αναλύεται η δρομολόγηση μεταξύ "),
                TextSegment(
                    text="Αυτόνομων Συστημάτων (BGP)",
                    is_highlight=True,
                    category="routing",
                    tag_label="BGP",
                    tooltip="Hot Potato routing vs shortest AS path",
                ),
                TextSegment(text=", υπολογισμοί "),
                TextSegment(
                    text="RTT με ενδιάμεση επεξεργασία d_proc = 0.02 ms",
                    is_highlight=True,
                    category="delay",
                    tag_label="RTT",
                    tooltip="Χρόνος αποστολής και επιστροφής πακέτων",
                ),
                TextSegment(text=", εκτέλεση αλγορίθμου "),
                TextSegment(
                    text="Dijkstra σε τοπολογία 11 κόμβων",
                    is_highlight=True,
                    category="routing",
                    tag_label="DIJKSTRA LSA",
                    tooltip="Συντομότερο μονοπάτι από κόμβο a σε κόμβο k",
                ),
                TextSegment(text=" και εύρεση "),
                TextSegment(
                    text="Ελάχιστου Πλαισίου CSMA/CD",
                    is_highlight=True,
                    category="error_check",
                    tag_label="CSMA/CD",
                    tooltip="L_min = 2 * d_prop * R = 512 bits = 64 Bytes",
                ),
                TextSegment(text="."),
            ]
        ),
    ]

    questions = [
        ExamQuestion(
            question_number=1,
            title="Ανάλυση των 4 Συνιστωσών Καθυστέρησης (Nodal Delays)",
            question_type="Theory Analysis",
            prompt_text="Ορίστε αναλυτικά τη συνολική καθυστέρηση από άκρο σε άκρο (end-to-end delay) ως μαθηματική έκφραση και εξηγήστε λεπτομερώς τα 4 επιμέρους σύμβολα.",
            detailed_justification=(
                "Η συνολική καθυστέρηση ισούται με: **d_nodal = d_proc + d_queue + d_trans + d_prop**\n\n"
                "1. **d_proc (Processing Delay):** Χρόνος ελέγχου επικεφαλίδας, επιλογής θύρας εξόδου και ανίχνευσης σφαλμάτων bits (συνήθως μs).\n"
                "2. **d_queue (Queuing Delay):** Χρόνος αναμονής στην ουρά εξόδου μέχρι να ελευθερωθεί ο δίαυλος μετάδοσης. Εξαρτάται από την ένταση κίνησης.\n"
                "3. **d_trans (Transmission Delay):** d_trans = L / R, όπου L το μέγεθος του πακέτου σε bits και R το bandwidth σε bps.\n"
                "4. **d_prop (Propagation Delay):** d_prop = d / s, όπου d το φυσικό μήκος της ζεύξης και s η ταχύτητα διάδοσης στο μέσο (π.χ. 2*10^8 m/s)."
            ),
            common_pitfalls=[
                "Σύγχυση μετάδοσης (L/R) με διάδοση (d/s).",
                "Παράλειψη της καθυστέρησης ουράς ή επεξεργασίας.",
            ],
        ),
        ExamQuestion(
            question_number=2,
            title="Υπολογισμός Bandwidth-Delay Product (BDP)",
            question_type="Calculations",
            prompt_text="Έστω ζεύξη με Bandwidth R = 1000 KB/s και Delay D = 5 ms. Ποιος είναι ο μέγιστος αριθμός bits που μπορούν να βρίσκονται 'εν πτήσει' πάνω στη ζεύξη;",
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Μετατροπή Μονάδων Bandwidth και Delay",
                    formula="R = 1000 KB/s = 1000 * 8000 bps = 8,000,000 bps, D = 5 ms = 0.005 s",
                    substitution="BDP = R * D",
                    result="8,000,000 bps * 0.005 s",
                    rationale="Το γινόμενο εύρους ζώνης-καθυστέρησης ορίζει τη χωρητικότητα του αγωγού σε bits.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Τελικός Υπολογισμός Bits και Bytes",
                    formula="BDP = 40,000 bits",
                    substitution="40,000 bits / 8 bits per byte",
                    result="5,000 Bytes (5 KB)",
                    rationale="Αν ο αποστολέας θέλει να κρατήσει τη ζεύξη 100% απασχολημένη, το παράθυρο αποστολής πρέπει να είναι τουλάχιστον 5 KB.",
                ),
            ],
            detailed_justification="Το BDP αντιπροσωπεύει τον όγκο δεδομένων που 'γεμίζει' το φυσικό καλώδιο. Στα δίκτυα υψηλής ταχύτητας και μεγάλης απόστασης (Long Fat Networks - LFN), το BDP είναι πολύ μεγάλο.",
        ),
        ExamQuestion(
            question_number=3,
            title="Υπολογισμός RTT με Ενδιάμεση Επεξεργασία (A -> C -> A)",
            question_type="Calculations",
            prompt_text="Έστω 2 διαδοχικές ζεύξεις (A-B και B-C) με R1 = R2 = 10 Mbps, L1 = 100 km, L2 = 50 km, u = 2.5 * 10^8 m/s. Πακέτο L = 10.000 bits αποστέλλεται από το A στο C και επιστρέφει αμέσως. Κάθε κόμβος έχει d_proc = 0.02 ms. Υπολογίστε το συνολικό RTT.",
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Καθυστέρηση Μετάδοσης ανά Ζεύξη",
                    formula="d_trans = L / R = 10,000 / (10 * 10^6)",
                    substitution="10,000 / 10,000,000",
                    result="1 ms",
                    rationale="Απαιτείται 1 ms για τη μετάδοση του πακέτου σε κάθε hop.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Καθυστερήσεις Διάδοσης",
                    formula="d_prop1 = 100,000m / 2.5*10^8 = 0.4 ms, d_prop2 = 50,000m / 2.5*10^8 = 0.2 ms",
                    substitution="d_prop_oneway = 0.4 + 0.2",
                    result="0.6 ms μονής κατεύθυνσης",
                    rationale="Συνολική διάδοση μετάβασης και επιστροφής = 2 * 0.6 = 1.2 ms.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Συνολικό RTT",
                    formula="RTT = 4 * d_trans + 2 * d_prop_oneway + d_proc_total",
                    substitution="4 * 1.0ms + 2 * 0.6ms + 3 * 0.02ms (στους ενδιάμεσους κόμβους)",
                    result="5.26 ms",
                    rationale="Το πακέτο μεταδίδεται 4 φορές (A->B, B->C, C->B, B->A) και διαδίδεται 2 φορές σε κάθε ζεύξη.",
                ),
            ],
            detailed_justification="Στο RTT προσμετρώνται όλες οι μεταδόσεις Store-and-Forward τόσο στη διαδρομή μετάβασης όσο και στη διαδρομή επιστροφής.",
        ),
    ]

    nodes = [
        TopologyNode("node_a", "Node A", "host", 100, 150, "10.0.1.1", "00:11:22:33:44:01"),
        TopologyNode("node_b", "Router B", "router", 380, 150, "10.0.1.2", "00:11:22:33:44:02"),
        TopologyNode("node_c", "Node C", "host", 660, 150, "10.0.2.1", "00:11:22:33:44:03"),
    ]

    links = [
        TopologyLink("node_a", "node_b", 10, 100.0, 2.5, "fiber", "10M | 100km"),
        TopologyLink("node_b", "node_c", 10, 50.0, 2.5, "fiber", "10M | 50km"),
    ]

    return NetworkScenario(
        id="exam_past_archive",
        title="Θέματα Εξετάσεων (Comprehensive Archive)",
        subtitle="4 Nodal Delays, BDP Product, OSPF, BGP Routing & Multi-hop RTT",
        course_tag="Past Exam",
        duration_info="2 ώρες και 15 λεπτά",
        paragraphs=paragraphs,
        questions=questions,
        nodes=nodes,
        links=links,
        methodology_summary=[
            "1. d_nodal = d_proc + d_queue + d_trans + d_prop.",
            "2. BDP = Bandwidth * Delay (Μέγιστα bits εν πτήσει).",
            "3. RTT πολλαπλών hops = Σ(d_trans_go + d_trans_back) + 2*Σ(d_prop) + Σ(d_proc).",
        ],
        calculator_type="delay",
    )
