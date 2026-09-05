"""Past Exam 2026 Team Edition Scenario Module.

Covers End-to-End Delay Derivations, Bandwidth-Delay Product, Google BBR Congestion Control,
OSPF configuration, BGP Autonomous System Routing, Dijkstra Graph Shortest Path,
and CSMA/CD Minimum Frame Size calculation.
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
    """Constructs and returns the complete Past Exam 2026 (Team Edition) scenario.

    Returns:
        NetworkScenario: The structured scenario object.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Το εξεταστικό δοκίμιο "),
                TextSegment(
                    text="Δίκτυα Υπολογιστών 2026 (Team Edition)",
                    is_highlight=True,
                    category="protocol",
                    tag_label="ΕΞΕΤΑΣΗ",
                    tooltip="Προχωρημένα θέματα αρχιτεκτονικής και αλγορίθμων δικτύων",
                ),
                TextSegment(text=" εστιάζει στη θεωρητική και υπολογιστική ανάλυση "),
                TextSegment(
                    text="Καθυστέρησης από Άκρο σε Άκρο (End-to-End Delay)",
                    is_highlight=True,
                    category="delay",
                    tag_label="DELAYS L/R+d/s",
                    tooltip="Μαθηματικό μοντέλο χρόνου μετάδοσης και διάδοσης",
                ),
                TextSegment(text=", στον υπολογισμό του "),
                TextSegment(
                    text="Bandwidth-Delay Product (BDP)",
                    is_highlight=True,
                    category="delay",
                    tag_label="BDP = R * RTT",
                    tooltip="Μέγιστη χωρητικότητα bits εν πτήσει (in flight) στο κανάλι",
                ),
                TextSegment(text=" και στην εφαρμογή του σύγχρονου αλγορίθμου συμφόρησης "),
                TextSegment(
                    text="Google BBR (CWND = RtProp * BtlBw)",
                    is_highlight=True,
                    category="protocol",
                    tag_label="BBR CONGESTION",
                    tooltip="Έλεγχος συμφόρησης βάσει RTT και Bottleneck Bandwidth",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="#e06b3a",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Στο δεύτερο μέρος εξετάζονται πολιτικές δρομολόγησης μεταξύ "),
                TextSegment(
                    text="Αυτόνομων Συστημάτων (BGP Autonomous Systems)",
                    is_highlight=True,
                    category="routing",
                    tag_label="BGP AS",
                    tooltip="Δρομολόγηση μεταξύ Verizon και AT&T",
                ),
                TextSegment(text=", η διαμόρφωση του πρωτοκόλλου "),
                TextSegment(
                    text="OSPF (Open Shortest Path First)",
                    is_highlight=True,
                    category="routing",
                    tag_label="OSPF L3",
                    tooltip="Link-State εσωτερική δρομολόγηση",
                ),
                TextSegment(text=", η εκτέλεση του αλγορίθμου "),
                TextSegment(
                    text="Dijkstra Shortest Path",
                    is_highlight=True,
                    category="routing",
                    tag_label="DIJKSTRA",
                    tooltip="Εύρεση βέλτιστης διαδρομής σε γράφο κόστους ζεύξεων",
                ),
                TextSegment(text=" και ο υπολογισμός του "),
                TextSegment(
                    text="Ελάχιστου Μεγέθους Πλαισίου CSMA/CD (L_min = 2 * d_prop * R)",
                    is_highlight=True,
                    category="error_check",
                    tag_label="CSMA/CD L_MIN",
                    tooltip="Αποφυγή μη ανιχνεύσιμων συγκρούσεων στο Ethernet",
                ),
                TextSegment(text="."),
            ]
        ),
    ]

    questions = [
        ExamQuestion(
            question_number=1,
            title="Μαθηματικός Ορισμός Καθυστέρησης από Άκρο σε Άκρο",
            question_type="Calculations",
            prompt_text="Ορίστε αναλυτικά την καθυστέρηση από άκρο σε άκρο για μία ζεύξη (A -> B) με μέγεθος πακέτου L, ρυθμό R, απόσταση l και ταχύτητα u.",
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Καθυστέρηση Μετάδοσης (Transmission Delay)",
                    formula="d_trans = L / R",
                    substitution="L bits / R bps",
                    result="L / R (sec)",
                    rationale="Ο χρόνος που απαιτείται για να τεθούν όλα τα bits του πακέτου πάνω στο φυσικό μέσο.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Καθυστέρηση Διάδοσης (Propagation Delay)",
                    formula="d_prop = l / u",
                    substitution="l meters / u (meters/sec)",
                    result="l / u (sec)",
                    rationale="Ο χρόνος που χρειάζεται ένα bit για να ταξιδέψει τη φυσική απόσταση l.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Συνολική Καθυστέρηση (χωρίς ουρές/επεξεργασία)",
                    formula="d_total = d_trans + d_prop",
                    substitution="(L / R) + (l / u)",
                    result="(L / R) + (l / u) (sec)",
                    rationale="Σε μία μόνο ζεύξη χωρίς ενδιάμεσο δρομολογητή, το άθροισμα μετάδοσης και διάδοσης δίνει τον συνολικό χρόνο.",
                ),
            ],
            detailed_justification="Σημείωση παραδοχών: Αν συμπεριληφθεί καθυστέρηση επεξεργασίας d_proc στον κόμβο Α ή ουρά αναμονής d_queue, προστίθενται γραμμικά: d_nodal = d_proc + d_queue + d_trans + d_prop.",
        ),
        ExamQuestion(
            question_number=2,
            title="Υπολογισμός Ελάχιστου Μεγέθους Πλαισίου CSMA/CD",
            question_type="Calculations",
            prompt_text="Ένα δίκτυο χρησιμοποιεί CSMA/CD και έχει bandwidth R = 10 Mbps. Αν ο μέγιστος χρόνος διάδοσης μονής κατεύθυνσης είναι d_prop = 25.6 μs, ποιο είναι το ελάχιστο μέγεθος του πλαισίου (L_min);",
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Κριτήριο Ανίχνευσης Σύγκρουσης CSMA/CD",
                    formula="d_trans >= 2 * d_prop  <=>  (L_min / R) >= 2 * d_prop",
                    substitution="L_min = 2 * d_prop * R",
                    result="L_min = 2 * (25.6 * 10^-6) * (10 * 10^6)",
                    rationale="Ο πομπός πρέπει να συνεχίζει να εκπέμπει τουλάχιστον για χρόνο 2*d_prop (Round Trip Time) ώστε να ανιχνεύσει σύγκρουση στο πιο απομακρυσμένο σημείο.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Υπολογισμός σε Bits και Bytes",
                    formula="L_min = 51.2 * 10 = 512 bits",
                    substitution="512 bits / 8 bits per byte",
                    result="64 Bytes",
                    rationale="Αυτός είναι ακριβώς ο λόγος που το πρότυπο IEEE 802.3 Ethernet έχει ελάχιστο μέγεθος πλαισίου 64 Bytes.",
                ),
            ],
            detailed_justification="Αν ένα πλαίσιο ήταν μικρότερο από 64 bytes (512 bits), ο πομπός θα τελείωνε τη μετάδοση προτού φτάσει το σήμα σύγκρουσης (JAM signal), θεωρώντας λανθασμένα ότι η αποστολή πέτυχε.",
            common_pitfalls=[
                "Ξέχασμα του συντελεστή 2 (2 * d_prop για RTT).",
                "Μη μετατροπή των 512 bits σε 64 Bytes.",
            ],
        ),
        ExamQuestion(
            question_number=3,
            title="Έλεγχος Συμφόρησης Google BBR (CWND)",
            question_type="Calculations",
            prompt_text="Έστω RTT = 5 ms (RtProp) και ρυθμός μετάδοσης R = 0.125 GB/s (BtlBw). Να υπολογιστεί το μέγεθος του παραθύρου συμφόρησης CWND σύμφωνα με το πρωτόκολλο BBR.",
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Μετατροπή Μονάδων",
                    formula="BtlBw = 0.125 GB/s = 0.125 * 10^9 Bytes/sec = 125 MB/s, RtProp = 5 ms = 0.005 sec",
                    substitution="CWND = RtProp * BtlBw",
                    result="0.005 s * 125,000,000 Bytes/s",
                    rationale="Το παράθυρο συμφόρησης στο BBR ισούται με το Bandwidth-Delay Product (BDP).",
                ),
                CalculationStep(
                    step_number=2,
                    title="Τελικός Υπολογισμός Παραθύρου",
                    formula="CWND = 0.005 * 125 * 10^6",
                    substitution="CWND = 625,000 Bytes",
                    result="625 KB (ή 625.000 Bytes)",
                    rationale="Το BBR κρατά τον αγωγό γεμάτο χωρίς να δημιουργεί περιττές ουρές αναμονής (bufferbloat).",
                ),
            ],
            detailed_justification="Το BBR (Bottleneck Bandwidth and RTT) μοντελοποιεί το κανάλι μετρώντας ανεξάρτητα το ελάχιστο RTT (χωρίς ουρές) και το μέγιστο throughput, αποτρέποντας την κατάρρευση συμφόρησης.",
        ),
    ]

    nodes = [
        TopologyNode("host_a", "Host A", "host", 100, 150, "10.10.10.1", "00:AA:11:22:33:01"),
        TopologyNode("router_b", "Router B (OSPF)", "router", 340, 150, "10.10.10.2", "00:BB:22:33:44:02"),
        TopologyNode("router_c", "Router C (Core)", "router", 580, 150, "172.16.8.1", "00:CC:33:44:55:03"),
        TopologyNode("server_k", "DIT UoI Server", "server", 800, 150, "192.168.1.10", "00:DD:44:55:66:04"),
    ]

    links = [
        TopologyLink("host_a", "router_b", 10, 100.0, 2.5, "copper", "10M | 100km"),
        TopologyLink("router_b", "router_c", 10, 50.0, 2.5, "fiber", "10M | 50km"),
        TopologyLink("router_c", "server_k", 1000, 1.0, 2.0, "fiber", "1G Server Link"),
    ]

    return NetworkScenario(
        id="exam_past_2026_team",
        title="Θέματα Εξετάσεων (2026 Team Edition)",
        subtitle="End-to-End Delays, Google BBR CWND, OSPF, Dijkstra & CSMA/CD L_min",
        course_tag="Past Exam",
        duration_info="2 ώρες και 15 λεπτά",
        paragraphs=paragraphs,
        questions=questions,
        nodes=nodes,
        links=links,
        methodology_summary=[
            "1. d_total = (L/R) + (l/u) για 1 ζεύξη.",
            "2. CSMA/CD Ελάχιστο Πλαίσιο: L_min = 2 * d_prop * R (64 Bytes στο 10 Mbps Ethernet).",
            "3. BBR Congestion Window: CWND = RtProp * BtlBw (Bandwidth-Delay Product).",
        ],
        calculator_type="delay",
    )
