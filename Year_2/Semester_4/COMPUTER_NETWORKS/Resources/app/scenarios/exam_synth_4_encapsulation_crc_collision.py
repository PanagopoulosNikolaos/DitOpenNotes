"""Synthetic & Realistic Exam 4 Scenario Module.

Contains 1-to-1 representation of all exam questions from Synthetic & Realistic Exam 4:
- Part A: Encapsulation headers, Collision vs Broadcast domains, Dijkstra Link-State prerequisites,
  Video streaming bandwidth (16 Mbps), True/False (OSPF Areas, Circuit switching waste, ARP Unicast Reply).
- Part B: Άσκηση 1 (Dijkstra shortest path execution on 7-node graph to G = cost 5),
  Άσκηση 2 (TCP sliding window BDP sizing = 1.25 MB),
  Άσκηση 3 (Hamming(7,4) odd parity codeword = 0111101).
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
    """Constructs and returns Synthetic & Realistic Exam 4 scenario.

    Returns:
        NetworkScenario: The structured scenario object with 1-to-1 parity.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Το πρότυπο διαγώνισμα "),
                TextSegment(
                    text="Synthetic & Realistic Exam 4",
                    is_highlight=True,
                    category="protocol",
                    tag_label="SYNTHETIC REALISTIC 4",
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
                    text="TCP Sliding Window (BDP = R * RTT = 1.25 MB)",
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
                TextSegment(text="Στο δεύτερο μέρος αναλύεται η εκτέλεση του "),
                TextSegment(
                    text="Αλγορίθμου Dijkstra σε Γράφο 7 Κόμβων",
                    is_highlight=True,
                    category="routing",
                    tag_label="DIJKSTRA 7",
                    tooltip="Συντομότερο μονοπάτι προς τον κόμβο G με κόστος 5",
                ),
                TextSegment(text=", ο υπολογισμός απαιτούμενου "),
                TextSegment(
                    text="Ρυθμού Μετάδοσης Video Streaming (16 Mbps)",
                    is_highlight=True,
                    category="delay",
                    tag_label="BANDWIDTH",
                    tooltip="2000 πακέτα/δευτ * 1000 Bytes = 16 Mbps",
                ),
                TextSegment(text=" και η κωδικοποίηση "),
                TextSegment(
                    text="Hamming(7,4) με Περιττή Ισοτιμία (0111101)",
                    is_highlight=True,
                    category="error_check",
                    tag_label="HAMMING ODD",
                    tooltip="p = 3 bits ισοτιμίας για d = 4 bits (1101)",
                ),
                TextSegment(text="."),
            ]
        ),
    ]

    questions = [
        # Part A - Question 1
        ExamQuestion(
            question_number=1,
            title="Διαδικασία Ενθυλάκωσης (Encapsulation)",
            question_type="Multiple Choice",
            prompt_text="Στη διαδικασία 'Ενθυλάκωσης' (Encapsulation), όταν τα δεδομένα μεταφέρονται από το Επίπεδο Εφαρμογής προς το Φυσικό Επίπεδο:",
            options=[
                QuestionOption("A", "Αφαιρούνται οι κεφαλίδες (headers) σε κάθε επίπεδο.", False, "Αυτό είναι απο-ενθυλάκωση (decapsulation) στον παραλήπτη."),
                QuestionOption("B", "Τα δεδομένα κρυπτογραφούνται υποχρεωτικά από το Data Link Layer.", False, "Η κρυπτογράφηση γίνεται συνήθως σε ανώτερα επίπεδα (TLS)."),
                QuestionOption("C", "Προστίθεται μια νέα κεφαλίδα (header) σε κάθε επίπεδο, δημιουργώντας τελικά το πλαίσιο στο Επίπεδο 2.", True, "Κάθε επίπεδο προσθέτει το δικό του header γύρω από το payload του ανώτερου επιπέδου."),
                QuestionOption("D", "Η διεύθυνση IP του παραλήπτη αλλάζει σε κάθε επίπεδο.", False, "Η IP ανήκει αποκλειστικά στο Network Layer."),
            ],
            correct_option_letter="C",
            detailed_justification="Η ενθυλάκωση σημαίνει ότι τα δεδομένα του ανώτερου επιπέδου γίνονται ωφέλιμο φορτίο (payload) για το κατώτερο, λαμβάνοντας νέο header. Η απο-ενθυλάκωση συμβαίνει στον παραλήπτη.",
        ),
        # Part A - Question 2
        ExamQuestion(
            question_number=2,
            title="Διάκριση Collision Domain έναντι Broadcast Domain",
            question_type="Multiple Choice",
            prompt_text="Ποια είναι η κύρια διαφορά ανάμεσα σε ένα Collision Domain (Πεδίο Συγκρούσεων) και ένα Broadcast Domain (Πεδίο Εκπομπής);",
            options=[
                QuestionOption("A", "Δεν υπάρχει καμία διαφορά, είναι συνώνυμα.", False, "Είναι εντελώς διαφορετικές έννοιες των L2 και L3."),
                QuestionOption("B", "Ένας Δρομολογητής (Router) διαχωρίζει τα Broadcast Domains, ενώ ένας Μεταγωγέας (Switch) διαχωρίζει τα Collision Domains.", True, "Το Switch προσφέρει micro-segmentation ανά θύρα, ενώ μόνο ο Router τερματίζει τα L2 broadcasts."),
                QuestionOption("C", "Ένας Δρομολογητής διαχωρίζει τα Collision Domains, ενώ ένας Μεταγωγέας διαχωρίζει τα Broadcast Domains.", False, "Αντίστροφη διατύπωση."),
                QuestionOption("D", "Ένα Hub διαχωρίζει τα Collision Domains.", False, "Το Hub διατηρεί 1 ενιαίο collision domain."),
            ],
            correct_option_letter="B",
            detailed_justification="Το Switch χωρίζει το δίκτυο σε μικρο-τμήματα χωρίς συγκρούσεις (micro-segments), αλλά προωθεί τα broadcasts. Μόνο ο Router σταματάει τα πακέτα εκπομπής (broadcasts) ανά interface.",
        ),
        # Part A - Question 3
        ExamQuestion(
            question_number=3,
            title="Αρχή Λειτουργίας Αλγορίθμου Dijkstra (Link-State)",
            question_type="Multiple Choice",
            prompt_text="Ο αλγόριθμος Dijkstra υπολογίζει τις συντομότερες διαδρομές χρησιμοποιώντας:",
            options=[
                QuestionOption("A", "Τον αριθμό των κόμβων (hop count) και μόνο.", False, "Αυτό είναι χαρακτηριστικό του RIP."),
                QuestionOption("B", "Πλήρη γνώση της τοπολογίας και των κοστών όλων των ζεύξεων του δικτύου (Link State).", True, "Απαιτείται πλήρης χάρτης της τοπολογίας που συγκεντρώνεται μέσω Link State Advertisements (LSAs)."),
                QuestionOption("C", "Πληροφορίες που λαμβάνει αποκλειστικά από τους άμεσους γείτονές του (Distance Vector).", False, "Αυτό ανήκει στον Bellman-Ford."),
                QuestionOption("D", "MAC Διευθύνσεις αποκλειστικά.", False, "Εκτελείται στο επίπεδο δικτύου (L3)."),
            ],
            correct_option_letter="B",
            detailed_justification="Ο αλγόριθμος Dijkstra είναι Link-State και απαιτεί από κάθε κόμβο να έχει πλήρη εικόνα της παγκόσμιας τοπολογίας και του κόστους όλων των συνδέσμων.",
        ),
        # Part A - Question 4
        ExamQuestion(
            question_number=4,
            title="Υπολογισμός Εύρους Ζώνης Ροής Πολυμέσων (Video Streaming)",
            question_type="Calculations",
            prompt_text="Αν μια ροή video streaming στέλνει 2.000 πακέτα το δευτερόλεπτο και κάθε πακέτο έχει μέγεθος 1.000 Bytes, ο ελάχιστος απαιτούμενος ρυθμός μετάδοσης (Bandwidth) χωρίς απώλειες είναι:",
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Υπολογισμός Ρυθμού σε Bytes και Bits",
                    formula="R = Packets_per_sec * Packet_Size_Bytes * 8",
                    substitution="2,000 pkts/s * 1,000 Bytes/pkt * 8 bits/Byte",
                    result="16,000,000 bps = 16 Mbps",
                    rationale="Μετατροπή ρυθμού πακέτων σε bits ανά δευτερόλεπτο.",
                )
            ],
            detailed_justification="$$2.000\\text{ πακέτα/s} \\times 1.000\\text{ Bytes} = 2.000.000\\text{ Bytes/s} \\times 8 = 16.000.000\\text{ bps} = 16\\text{ Mbps}$$",
        ),
        # Part A - Question 5
        ExamQuestion(
            question_number=5,
            title="Θεωρητικές Προτάσεις OSPF, Μεταγωγής & ARP (Σωστό/Λάθος)",
            question_type="Multiple Choice",
            prompt_text=(
                "Επιλέξτε Σωστό (Σ) ή Λάθος (Λ) για τις παρακάτω προτάσεις:\n"
                "1. Το πρωτόκολλο OSPF υποστηρίζει Ιεραρχική Δρομολόγηση μέσω του διαχωρισμού σε περιοχές (Areas).\n"
                "2. Στη μεταγωγή κυκλώματος (Circuit Switching), αν ο χρήστης δεν μιλάει (αδράνεια), το εύρος ζώνης αξιοποιείται αυτόματα από άλλους χρήστες.\n"
                "3. Τα μηνύματα ARP Reply (Απαντήσεις ARP) στέλνονται ως Unicast προς τον κόμβο που έκανε το αίτημα."
            ),
            options=[
                QuestionOption("A", "1: Σ, 2: Σ, 3: Σ", False, "Η πρόταση 2 είναι λάθος."),
                QuestionOption("B", "1: Σ, 2: Λ, 3: Σ", True, "1=Σ (OSPF Areas), 2=Λ (Στο circuit switching οι πόροι δεσμεύονται αποκλειστικά και σπαταλώνται), 3=Σ (ARP Reply = Unicast)."),
                QuestionOption("C", "1: Λ, 2: Λ, 3: Σ", False, "Το OSPF υποστηρίζει πράγματι ιεραρχία με Areas."),
                QuestionOption("D", "1: Σ, 2: Λ, 3: Λ", False, "Το ARP Reply είναι πάντα unicast."),
            ],
            correct_option_letter="B",
            detailed_justification=(
                "1. **Σωστό:** Το OSPF χωρίζει τα μεγάλα δίκτυα σε Areas (π.χ. Area 0 Backbone) μειώνοντας το routing overhead.\n"
                "2. **Λάθος:** Στη μεταγωγή κυκλώματος οι πόροι παραμένουν δεσμευμένοι ακόμα και σε αδράνεια (σπατάλη πόρων).\n"
                "3. **Σωστό:** Το ARP Request είναι Broadcast (FF:FF...), αλλά το ARP Reply είναι πάντοτε Unicast απευθείας στον αιτούντα."
            ),
        ),
        # Part B - Άσκηση 1
        ExamQuestion(
            question_number=6,
            title="Άσκηση 1: Αλγόριθμος Dijkstra σε Γράφο 7 Κόμβων (A -> G)",
            question_type="Algorithm Step",
            prompt_text=(
                "Εφαρμόστε τον αλγόριθμο Link-State Dijkstra στον παρακάτω γράφο 7 κόμβων και βρείτε τη συντομότερη διαδρομή από τον κόμβο **A** στον **G**:\n"
                "Ακμές: A-B:2, A-C:1, A-D:3, B-E:1, C-D:1, C-F:2, D-E:2, D-F:1, E-G:3, F-G:2."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Βήμα 0: Αρχικοποίηση από A (N = {A})",
                    formula="D(C)=1(A), D(B)=2(A), D(D)=3(A), άλλοι=inf",
                    substitution="Ελάχιστος κόμβος: C με κόστος 1",
                    result="N = {A, C}",
                    rationale="Ο C μονιμοποιείται πρώτος.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Βήμα 1: Επέκταση μέσω C (N = {A, C})",
                    formula="D(D)=min(3(A), 1+1)=2(C) | D(F)=1+2=3(C)",
                    substitution="Υποψήφιοι: B: 2(A), D: 2(C), F: 3(C)",
                    result="N = {A, C, B, D}",
                    rationale="Μονιμοποιούνται οι B και D με κόστος 2.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Βήμα 2: Επέκταση προς E και F",
                    formula="D(E)=min(inf, 2+1)=3(B) | D(F)=min(3(C), 2+1)=3(D)",
                    substitution="Μονιμοποίηση E (κόστος 3) και F (κόστος 3)",
                    result="N = {A, C, B, D, E, F}",
                    rationale="Και οι δύο κόμβοι έχουν κόστος 3.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Βήμα 3: Τελική Άφιξη στον Προορισμό G",
                    formula="D(G) = min(D(E)+3, D(F)+2) = min(3+3, 3+2) = 5(F)",
                    substitution="Μέσω F: 3 + 2 = 5",
                    result="Συντομότερο Μονοπάτι: A -> C -> D -> F -> G (Κόστος = 5)",
                    rationale="Η διαδρομή μέσω F δίνει το ελάχιστο κόστος 5.",
                ),
            ],
            detailed_justification=(
                "Πίνακας Dijkstra:\n\n"
                "| Βήμα | N | B | C | D | E | F | G |\n"
                "|---|---|---|---|---|---|---|---|\n"
                "| 0 | A | 2(A) | **1(A)** | 3(A) | inf | inf | inf |\n"
                "| 1 | AC | **2(A)** | 1 | **2(C)** | inf | 3(C) | inf |\n"
                "| 2 | ACBD | 2 | 1 | 2 | **3(B)** | **3(D)** | inf |\n"
                "| 3 | ACBDEF | 2 | 1 | 2 | 3 | 3 | **5(F)** |\n\n"
                "**Συντομότερο Μονοπάτι:** `A -> C -> D -> F -> G` (ή `A -> C -> F -> G`) με συνολικό κόστος **5**."
            ),
        ),
        # Part B - Άσκηση 2
        ExamQuestion(
            question_number=7,
            title="Άσκηση 2: Υπολογισμός Μεγέθους TCP Sliding Window (BDP)",
            question_type="Calculations",
            prompt_text=(
                "Έστω σύνδεση FTP με Bandwidth R = 200 Mbps και RTT = 50 ms. "
                "Για 100% αξιοποίηση του καναλιού χωρίς idle time, ποιο πρέπει να είναι το ελάχιστο μέγεθος του Sliding Window σε MB;"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Υπολογισμός Bandwidth-Delay Product (BDP)",
                    formula="Window_bits = R * RTT",
                    substitution="(200 * 10^6 bps) * 0.050 s",
                    result="10,000,000 bits",
                    rationale="Όγκος δεδομένων που εκπέμπονται κατά τη διάρκεια ενός γύρου RTT.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Μετατροπή σε Bytes και Megabytes",
                    formula="Window_Bytes = 10,000,000 / 8",
                    substitution="1,250,000 Bytes",
                    result="1.25 MB",
                    rationale="Απαιτείται παράθυρο τουλάχιστον 1.25 MB για να μην περιμένει ο αποστολέας ACKs με κενό κανάλι.",
                ),
            ],
            detailed_justification="$$\\text{Window} = R \\times \\text{RTT} = (200 \\times 10^6\\text{ bps}) \\times 0,050\\text{ s} = 10.000.000\\text{ bits} = 1.250.000\\text{ Bytes} = 1,25\\text{ MB}$$",
        ),
        # Part B - Άσκηση 3
        ExamQuestion(
            question_number=8,
            title="Άσκηση 3: Κώδικας Hamming(7,4) με Περιττή Ισοτιμία (Odd Parity)",
            question_type="Calculations",
            prompt_text="Αποστολέας θέλει να μεταδώσει τα δεδομένα D = `1101` με κώδικα Hamming (Odd Parity). Βρείτε τον αριθμό bits ισοτιμίας p και το τελικό μεταδιδόμενο μήνυμα.",
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Εύρεση Bits Ισοτιμίας",
                    formula="2^p >= d + p + 1",
                    substitution="d = 4 -> 2^p >= 4 + p + 1 <=> 2^p >= p + 5",
                    result="p = 3 bits (2^3 = 8 >= 8)",
                    rationale="Χρειάζονται 3 bits ισοτιμίας στις θέσεις 1, 2, 4. Συνολικό μήκος 7 bits.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Υπολογισμός Bits Ισοτιμίας (Odd Parity)",
                    formula="P1(1,3,5,7), P2(2,3,6,7), P4(4,5,6,7) με D = 1 1 0 1",
                    substitution="D1=1 (θ3), D2=1 (θ5), D3=0 (θ6), D4=1 (θ7)",
                    result="P1=0, P2=1, P4=1",
                    rationale="Κάθε ομάδα πρέπει να έχει περιττό αριθμό άσων.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Τελικό Μήνυμα",
                    formula="[P1, P2, D1, P4, D2, D3, D4]",
                    substitution="0 1 1 1 1 0 1",
                    result="0111101",
                    rationale="Η τελική κωδικολέξη προστατεύει από μονά σφάλματα.",
                ),
            ],
            detailed_justification=(
                "Πίνακας Hamming(7,4) με περιττή ισοτιμία:\n\n"
                "| Θέση | 1 | 2 | 3 | 4 | 5 | 6 | 7 |\n"
                "|---|---|---|---|---|---|---|\n"
                "| Bit | **P1** | **P2** | D1 | **P4** | D2 | D3 | D4 |\n"
                "| Τιμή | `0` | `1` | `1` | `1` | `1` | `0` | `1` |\n\n"
                "- P1 (θέσεις 1, 3, 5, 7): P1, 1, 1, 1 (3 άσοι). Για περιττό: **P1 = 0**.\n"
                "- P2 (θέσεις 2, 3, 6, 7): P2, 1, 0, 1 (2 άσοι). Για περιττό: **P2 = 1**.\n"
                "- P4 (θέσεις 4, 5, 6, 7): P4, 1, 0, 1 (2 άσοι). Για περιττό: **P4 = 1**.\n\n"
                "Τελικό μεταδιδόμενο μήνυμα: **`0111101`**"
            ),
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
        subtitle="Encapsulation, Domains, 7-Node Dijkstra (Cost 5), Streaming (16M), TCP BDP & Hamming",
        course_tag="Synthetic Realistic",
        duration_info="2 ώρες και 15 λεπτά",
        paragraphs=paragraphs,
        questions=questions,
        nodes=nodes,
        links=links,
        methodology_summary=[
            "1. Encapsulation: Header addition per layer.",
            "2. Switch = Collision separation, Router = Broadcast separation.",
            "3. Streaming Bandwidth = 2000 * 1000 * 8 = 16 Mbps.",
            "4. Dijkstra: Συντομότερη διαδρομή A -> G με κόστος 5.",
            "5. TCP Sliding Window = 200 Mbps * 50 ms = 1.25 MB.",
            "6. Hamming(7,4) Odd Parity: 0111101.",
        ],
        calculator_type="delay",
    )
