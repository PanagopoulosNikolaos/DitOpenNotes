"""Synthetic Full Coverage Exam 2 Scenario Module.

Contains 1-to-1 representation of all exam questions from Synthetic Exam 2 (Full Coverage):
- Part A: Longest Prefix Match (LPM), Queuing delay dynamics, Network core routers,
  Data Plane forwarding in hardware, True/False (Cumulative ACKs, Tier-1 Peering, Switch domains).
- Part B: Άσκηση 1 (Forwarding Table lookups with LPM), Άσκηση 2 (Bellman-Ford Distance Vector next-hop),
  Άσκηση 3 (ARP across router addressing & Transoceanic BDP = 20 Mbits).
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
    """Constructs and returns Synthetic Full Coverage Exam 2 scenario.

    Returns:
        NetworkScenario: The structured scenario object with 1-to-1 parity.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Το διαγώνισμα πλήρους κάλυψης "),
                TextSegment(
                    text="Synthetic Exam 2 (Full Coverage)",
                    is_highlight=True,
                    category="protocol",
                    tag_label="FULL COVERAGE 2",
                    tooltip="Διαγώνισμα συνολικής επανάληψης ύλης",
                ),
                TextSegment(text=" αναλύει σε βάθος τον κανόνα επιλογής "),
                TextSegment(
                    text="Longest Prefix Match (LPM)",
                    is_highlight=True,
                    category="routing",
                    tag_label="LPM",
                    tooltip="Επιλογή της εγγραφής με το μεγαλύτερο μήκος μάσκας",
                ),
                TextSegment(text=", τη φύση της "),
                TextSegment(
                    text="Καθυστέρησης Ουράς (Queuing Delay)",
                    is_highlight=True,
                    category="delay",
                    tag_label="D_QUEUE",
                    tooltip="Στοχαστική διακύμανση βάσει έντασης κίνησης",
                ),
                TextSegment(text=" και τον ρόλο του "),
                TextSegment(
                    text="Data Plane έναντι του Control Plane",
                    is_highlight=True,
                    category="routing",
                    tag_label="FORWARDING",
                    tooltip="Τοπική προώθηση σε hardware vs συνολική δρομολόγηση",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="#e06b3a",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Στο πρακτικό μέρος εξετάζονται αναζητήσεις σε "),
                TextSegment(
                    text="Πίνακα Προώθησης με LPM",
                    is_highlight=True,
                    category="routing",
                    tag_label="TABLE LOOKUP",
                    tooltip="Εύρεση interface εξόδου για 4 διευθύνσεις IP",
                ),
                TextSegment(text=", ο αλγόριθμος "),
                TextSegment(
                    text="Bellman-Ford Distance Vector",
                    is_highlight=True,
                    category="routing",
                    tag_label="BELLMAN-FORD",
                    tooltip="Εύρεση ελάχιστου κόστους και Next-Hop",
                ),
                TextSegment(text=", η λειτουργία του "),
                TextSegment(
                    text="ARP μέσω Δρομολογητή",
                    is_highlight=True,
                    category="protocol",
                    tag_label="ROUTER ARP",
                    tooltip="Αλλαγή MAC διευθύνσεων σε κάθε hop",
                ),
                TextSegment(text=" και ο υπολογισμός του "),
                TextSegment(
                    text="Bandwidth-Delay Product (20 Mbits)",
                    is_highlight=True,
                    category="delay",
                    tag_label="BDP",
                    tooltip="Μέγιστα bits εν πτήσει",
                ),
                TextSegment(text="."),
            ]
        ),
    ]

    questions = [
        # Part A - Question 1
        ExamQuestion(
            question_number=1,
            title="Κανόνας Longest Prefix Match (LPM)",
            question_type="Multiple Choice",
            prompt_text="Σύμφωνα με τον κανόνα Longest Prefix Match (LPM), όταν μια διεύθυνση προορισμού ταιριάζει σε πολλαπλές εγγραφές του πίνακα προώθησης, ποια εγγραφή επιλέγεται;",
            options=[
                QuestionOption("A", "Η εγγραφή με το μικρότερο αριθμό bits στο prefix.", False, "Το μικρότερο πρόθεμα είναι πιο γενικό."),
                QuestionOption("B", "Η εγγραφή με το μεγαλύτερο αριθμό bits στο prefix.", True, "Το μεγαλύτερο πρόθεμα είναι το πιο ειδικό (specific) και υπερισχύει πάντοτε."),
                QuestionOption("C", "Η προεπιλεγμένη διαδρομή (default route).", False, "Επιλέγεται μόνο αν δεν υπάρχει άλλο ταίριασμα."),
                QuestionOption("D", "Η πρώτη εγγραφή που βρίσκεται στον πίνακα.", False, "Η σειρά στον πίνακα δεν καθορίζει την επιλογή."),
            ],
            correct_option_letter="B",
            detailed_justification="Το Longest Prefix Match επιλέγει την εγγραφή με τη μεγαλύτερη μάσκα (π.χ. /26 υπερισχύει των /24 και /16).",
        ),
        # Part A - Question 2
        ExamQuestion(
            question_number=2,
            title="Δυναμική της Καθυστέρησης Ουράς (Queuing Delay)",
            question_type="Multiple Choice",
            prompt_text="Η καθυστέρηση ουράς (queuing delay) σε έναν δρομολογητή:",
            options=[
                QuestionOption("A", "Εξαρτάται αποκλειστικά από την απόσταση μεταξύ των δύο κόμβων.", False, "Αυτό είναι η καθυστέρηση διάδοσης."),
                QuestionOption("B", "Είναι σταθερή και υπολογίζεται ως L/R.", False, "Αυτό είναι η καθυστέρηση μετάδοσης."),
                QuestionOption("C", "Εξαρτάται από τον ρυθμό άφιξης πακέτων (traffic load) και μεταβάλλεται συνεχώς.", True, "Είναι στοχαστική και εξαρτάται από την ένταση κίνησης και την πληρότητα των buffers."),
                QuestionOption("D", "Οφείλεται στο χρόνο ελέγχου των σφαλμάτων (checksum).", False, "Αυτό είναι καθυστέρηση επεξεργασίας."),
            ],
            correct_option_letter="C",
            detailed_justification="Η καθυστέρηση ουράς εξαρτάται αποκλειστικά από την ένταση κίνησης στον δρομολογητή σε μια δεδομένη χρονική στιγμή.",
        ),
        # Part A - Question 3
        ExamQuestion(
            question_number=3,
            title="Στοιχεία Πυρήνα του Δικτύου (Network Core)",
            question_type="Multiple Choice",
            prompt_text="Ποιο από τα παρακάτω ανήκει αποκλειστικά στον πυρήνα του δικτύου (Network Core);",
            options=[
                QuestionOption("A", "Web Servers", False, "Ανήκουν στο Network Edge."),
                QuestionOption("B", "Δρομολογητές (Routers)", True, "Ο πυρήνας αποτελείται από routers και switches."),
                QuestionOption("C", "Κινητά τηλέφωνα", False, "Είναι τελικά συστήματα."),
                QuestionOption("D", "Εφαρμογές Email (Clients)", False, "Εκτελούνται στα άκρα."),
            ],
            correct_option_letter="B",
            detailed_justification="Ο πυρήνας αποτελείται από routers και switches που διασυνδέουν τα δίκτυα.",
        ),
        # Part A - Question 4
        ExamQuestion(
            question_number=4,
            title="Ρόλος του Data Plane ενός Δρομολογητή",
            question_type="Multiple Choice",
            prompt_text="Το Data Plane ενός δρομολογητή είναι υπεύθυνο για:",
            options=[
                QuestionOption("A", "Την εκτέλεση του αλγορίθμου Dijkstra.", False, "Ανήκει στο Control Plane."),
                QuestionOption("B", "Τη φυσική προώθηση των πακέτων από την είσοδο στην κατάλληλη έξοδο (forwarding).", True, "Υλοποιείται σε εξειδικευμένο hardware για ταχύτατη προώθηση."),
                QuestionOption("C", "Την ανταλλαγή μηνυμάτων OSPF με άλλους δρομολογητές.", False, "Ανήκει στο Control Plane."),
                QuestionOption("D", "Τη διατήρηση του Routing Table (RIB).", False, "Ανήκει στο Control Plane."),
            ],
            correct_option_letter="B",
            detailed_justification="Το Data plane δουλεύει στο επίπεδο του hardware για την ταχύτατη προώθηση (forwarding). Το Control plane ασχολείται με τους αλγορίθμους δρομολόγησης.",
        ),
        # Part A - Question 5
        ExamQuestion(
            question_number=5,
            title="Θεωρητικές Προτάσεις TCP, Peering & Switches (Σωστό/Λάθος)",
            question_type="Multiple Choice",
            prompt_text=(
                "Επιλέξτε Σωστό (Σ) ή Λάθος (Λ) για τις παρακάτω προτάσεις:\n"
                "1. Το πρωτόκολλο TCP χρησιμοποιεί αθροιστικές επιβεβαιώσεις (cumulative ACKs).\n"
                "2. Ένας Tier-1 ISP συνήθως πληρώνει για την ανταλλαγή κίνησης (transit) με άλλους Tier-1 ISPs.\n"
                "3. Ένα Layer 2 Switch χωρίζει το collision domain αλλά όχι το broadcast domain."
            ),
            options=[
                QuestionOption("A", "1: Σ, 2: Σ, 3: Σ", False, "Η πρόταση 2 είναι λάθος."),
                QuestionOption("B", "1: Σ, 2: Λ, 3: Σ", True, "1=Σ (Cumulative ACKs), 2=Λ (Settlement-free peering), 3=Σ (Collision separation, κοινό broadcast)."),
                QuestionOption("C", "1: Λ, 2: Λ, 3: Σ", False, "Το TCP έχει cumulative ACKs."),
                QuestionOption("D", "1: Σ, 2: Λ, 3: Λ", False, "Το switch χωρίζει όντως τα collision domains."),
            ],
            correct_option_letter="B",
            detailed_justification=(
                "1. **Σωστό:** Το TCP επιβεβαιώνει τα δεδομένα αθροιστικά.\n"
                "2. **Λάθος:** Οι Tier-1 ISPs δεν πληρώνουν transit, έχουν δωρεάν peering.\n"
                "3. **Σωστό:** Κάθε πόρτα του switch είναι ανεξάρτητο collision domain, αλλά όλα ανήκουν στο ίδιο broadcast domain."
            ),
        ),
        # Part B - Άσκηση 1
        ExamQuestion(
            question_number=6,
            title="Άσκηση 1: Longest Prefix Match (LPM) σε Πίνακα Προώθησης",
            question_type="Calculations",
            prompt_text=(
                "Δίνεται ο πίνακας προώθησης:\n"
                "- `10.20.0.0/16` -> Eth0\n"
                "- `10.20.30.0/24` -> Eth1\n"
                "- `10.20.30.64/26` -> Eth2\n"
                "- `0.0.0.0/0` -> Eth3 (Default)\n\n"
                "Βρείτε το Interface προώθησης για:\n"
                "1. `10.20.30.100`\n"
                "2. `10.20.31.5`\n"
                "3. `10.21.5.1`\n"
                "4. `10.20.30.20`"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="1. IP 10.20.30.100 -> Eth2",
                    formula="LPM: Match /16, /24, /26 -> /26",
                    substitution="100 in [64, 127]",
                    result="Eth2",
                    rationale="Το /26 είναι το μακρύτερο πρόθεμα (26 bits).",
                ),
                CalculationStep(
                    step_number=2,
                    title="2. IP 10.20.31.5 -> Eth0",
                    formula="Match /16",
                    substitution="31 != 30",
                    result="Eth0",
                    rationale="Ταιριάζει μόνο στο /16.",
                ),
                CalculationStep(
                    step_number=3,
                    title="3. IP 10.21.5.1 -> Eth3",
                    formula="Default Route",
                    substitution="21 != 20",
                    result="Eth3",
                    rationale="Κανένα συγκεκριμένο ταίριασμα, επιλέγεται η default route.",
                ),
                CalculationStep(
                    step_number=4,
                    title="4. IP 10.20.30.20 -> Eth1",
                    formula="LPM: Match /16, /24 -> /24",
                    substitution="20 < 64 (όχι /26)",
                    result="Eth1",
                    rationale="Το /24 είναι μακρύτερο από το /16.",
                ),
            ],
            detailed_justification=(
                "1. **10.20.30.100** -> **Eth2** (/26)\n"
                "2. **10.20.31.5** -> **Eth0** (/16)\n"
                "3. **10.21.5.1** -> **Eth3** (Default)\n"
                "4. **10.20.30.20** -> **Eth1** (/24)"
            ),
        ),
        # Part B - Άσκηση 2
        ExamQuestion(
            question_number=7,
            title="Άσκηση 2: Distance Vector (Bellman-Ford) & Next-Hop",
            question_type="Calculations",
            prompt_text=(
                "Δρομολογητής X με γείτονες Y (cost 3), Z (cost 2), W (cost 4).\n"
                "Κόστη προς D: από Y: 5, από Z: 6, από W: 2.\n"
                "**a.** Ποιο είναι το νέο κόστος προς D;\n"
                "**b.** Ποιος είναι ο Next-Hop;"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Εξίσωση Bellman-Ford",
                    formula="d_X(D) = min { c(X,v) + d_v(D) }",
                    substitution="Y: 3+5=8 | Z: 2+6=8 | W: 4+2=6",
                    result="min(8, 8, 6) = 6",
                    rationale="Το ελάχιστο κόστος επιτυγχάνεται μέσω W.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Επιλογή Next-Hop",
                    formula="Next-Hop = argmin",
                    substitution="v = W",
                    result="Next-Hop: W",
                    rationale="Ο δρομολογητής W καταχωρείται ως επόμενος κόμβος.",
                ),
            ],
            detailed_justification="- **a. Νέο Κόστος:** **6**\n- **b. Next-Hop:** **W**",
        ),
        # Part B - Άσκηση 3
        ExamQuestion(
            question_number=8,
            title="Άσκηση 3: ARP μέσω Router & Υπερωκεάνιο BDP",
            question_type="Calculations",
            prompt_text=(
                "**a.** Τοπολογία: `[Host A: 10.0.0.5] ---- [Router R: 10.0.0.1 / 192.168.1.1] ---- [Host B: 192.168.1.10]`\n"
                "- i. Ποιο ARP request θα στείλει ο A;\n"
                "- ii. Ποιες L2/L3 διευθύνσεις έχει το πακέτο αναχωρώντας από τον R προς τον B;\n\n"
                "**b.** Ζεύξη 4.000 km, s = 2*10^8 m/s, R = 1 Gbps.\n"
                "- i. Υπολογίστε το d_prop.\n"
                "- ii. Υπολογίστε το BDP σε bits."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ερώτημα a.i: ARP Request από Host A",
                    formula="Target_IP = Gateway_IP",
                    substitution="Sender IP: 10.0.0.5, Sender MAC: 00:AA:11:22:33:44, Target IP: 10.0.0.1",
                    result="L2 Broadcast: FF:FF:FF:FF:FF:FF",
                    rationale="Ο A αναζητά τη MAC της πύλης του.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ερώτημα a.ii: Πακέτο R -> B",
                    formula="Src IP: 10.0.0.5, Dst IP: 192.168.1.10",
                    substitution="Src MAC: 00:RR:AA:BB:CC:02, Dst MAC: 00:BB:99:88:77:66",
                    result="IP σταθερή, MAC αλλάζει σε κάθε hop",
                    rationale="Το L3 παραμένει αναλλοίωτο, το L2 ανανεώνεται.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Ερώτημα b.i: Καθυστέρηση Διάδοσης d_prop",
                    formula="d_prop = d / s",
                    substitution="(4000 * 10^3) / (2 * 10^8)",
                    result="0.02 s = 20 ms",
                    rationale="Χρόνος διάδοσης στην οπτική ίνα.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Ερώτημα b.ii: BDP",
                    formula="BDP = R * d_prop",
                    substitution="10^9 bps * 0.02 s",
                    result="20,000,000 bits = 20 Mbits",
                    rationale="Μέγιστος αριθμός bits εν πτήσει.",
                ),
            ],
            detailed_justification=(
                "**a.i:** Sender IP: `10.0.0.5`, Sender MAC: `00:AA:11:22:33:44`, Target IP: `10.0.0.1`, Frame MAC: `FF:FF:FF:FF:FF:FF`.\n"
                "**a.ii:** Src IP: `10.0.0.5`, Dst IP: `192.168.1.10`, Src MAC: `00:RR:AA:BB:CC:02`, Dst MAC: `00:BB:99:88:77:66`.\n"
                "**b.i:** $d_{\\text{prop}} = 20\\text{ ms}$.\n"
                "**b.ii:** $\\text{BDP} = 20\\text{ Mbits}$."
            ),
        ),
    ]

    nodes = [
        TopologyNode("r_in", "Ingress Router", "router", 120, 150, "192.168.1.1"),
        TopologyNode("r_core", "Core Router (LPM)", "router", 420, 150, "10.0.0.1"),
        TopologyNode("sub1", "Subnet /24 (eth0)", "host", 720, 80, "192.168.10.0/24"),
        TopologyNode("sub2", "Subnet /28 (eth1)", "host", 720, 220, "192.168.10.16/28"),
    ]

    links = [
        TopologyLink("r_in", "r_core", 1000, 10.0, 2.0, "fiber", "1G Fiber"),
        TopologyLink("r_core", "sub1", 100, 0.5, 2.0, "copper", "eth0 /24"),
        TopologyLink("r_core", "sub2", 100, 0.5, 2.0, "copper", "eth1 /28 (LPM Match)"),
    ]

    return NetworkScenario(
        id="exam_synth_fc_2",
        title="Synthetic Exam 2 (Full Coverage)",
        subtitle="LPM Rules, Queuing Delay, Network Core, Bellman-Ford Next-Hop, Router ARP & BDP",
        course_tag="Synthetic Full Coverage",
        duration_info="2 ώρες και 15 λεπτά",
        paragraphs=paragraphs,
        questions=questions,
        nodes=nodes,
        links=links,
        methodology_summary=[
            "1. LPM: Μεγαλύτερο prefix = Πιο συγκεκριμένη διαδρομή.",
            "2. Queuing Delay: Μεταβάλλεται συνεχώς βάσει traffic load.",
            "3. Bellman-Ford: d_X(D) = min { c(X,v) + d_v(D) }.",
            "4. L2/L3: IP παραμένει σταθερή, MAC αλλάζει ανά hop.",
            "5. BDP = R * d_prop = 20 Mbits.",
        ],
        calculator_type="lpm",
    )
