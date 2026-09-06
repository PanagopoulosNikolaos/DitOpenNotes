"""Synthetic & Realistic Exam 2 Scenario Module.

Contains 1-to-1 representation of all exam questions from Synthetic & Realistic Exam 2:
- Part A: Network core routers, Longest Prefix Match (LPM) rule, Data vs Control plane,
  Count-to-Infinity in Distance Vector, True/False (Cumulative ACKs, Tier-1 Peering, Switch domains).
- Part B: Άσκηση 1 (LPM Forwarding Table lookups), Άσκηση 2 (Bellman-Ford Distance Vector next-hop),
  Άσκηση 3 (ARP across router with L2/L3 addressing & Transoceanic BDP).
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
    """Constructs and returns Synthetic & Realistic Exam 2 scenario.

    Returns:
        NetworkScenario: The structured scenario object with 1-to-1 parity.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Το πρότυπο διαγώνισμα "),
                TextSegment(
                    text="Synthetic & Realistic Exam 2",
                    is_highlight=True,
                    category="protocol",
                    tag_label="SYNTHETIC REALISTIC 2",
                    tooltip="Ρεαλιστικό διαγώνισμα προσομοίωσης εξετάσεων",
                ),
                TextSegment(text=" αναλύει τη λειτουργία του "),
                TextSegment(
                    text="Πυρήνα του Δικτύου (Network Core - Routers)",
                    is_highlight=True,
                    category="device",
                    tag_label="ROUTER CORE",
                    tooltip="Ενδιάμεσοι κόμβοι μεταγωγής πακέτων",
                ),
                TextSegment(text=", τον κανόνα επιλογής "),
                TextSegment(
                    text="Longest Prefix Match (LPM)",
                    is_highlight=True,
                    category="routing",
                    tag_label="LPM RULE",
                    tooltip="Επιλογή της εγγραφής με το μεγαλύτερο μήκος μάσκας",
                ),
                TextSegment(text=" και τη διάκριση μεταξύ "),
                TextSegment(
                    text="Data Plane (Forwarding) και Control Plane (Routing)",
                    is_highlight=True,
                    category="routing",
                    tag_label="PLANES",
                    tooltip="Hardware forwarding vs Routing algorithm computation",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="#e06b3a",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Στο δεύτερο μέρος εξετάζεται η αδυναμία "),
                TextSegment(
                    text="Count-to-Infinity στους Distance-Vector Αλγορίθμους",
                    is_highlight=True,
                    category="routing",
                    tag_label="BELLMAN-FORD",
                    tooltip="Αργή σύγκλιση και βρόχοι δρομολόγησης σε αστοχία ζεύξης",
                ),
                TextSegment(text=", η λειτουργία των "),
                TextSegment(
                    text="Cumulative ACKs στο TCP",
                    is_highlight=True,
                    category="protocol",
                    tag_label="TCP ACKs",
                    tooltip="Επιβεβαίωση όλων των συνεχόμενων bytes",
                ),
                TextSegment(text=" και η ανάλυση "),
                TextSegment(
                    text="Διευθυνσιοδότησης L2/L3 μέσω Router",
                    is_highlight=True,
                    category="protocol",
                    tag_label="ROUTER ARP",
                    tooltip="Αλλαγή MAC διευθύνσεων σε κάθε hop με σταθερή IP",
                ),
                TextSegment(text="."),
            ]
        ),
    ]

    questions = [
        # Part A - Question 1
        ExamQuestion(
            question_number=1,
            title="Στοιχεία Πυρήνα του Δικτύου (Network Core)",
            question_type="Multiple Choice",
            prompt_text="Ποιο από τα παρακάτω ανήκει αποκλειστικά στον πυρήνα του δικτύου (Network Core);",
            options=[
                QuestionOption("A", "Web Servers", False, "Οι servers βρίσκονται στα άκρα του δικτύου (Network Edge)."),
                QuestionOption("B", "Δρομολογητές (Routers)", True, "Ο πυρήνας αποτελείται από routers και switches που διασυνδέουν τα δίκτυα."),
                QuestionOption("C", "Κινητά τηλέφωνα (Smartphones)", False, "Είναι τελικά συστήματα (hosts) στο Network Edge."),
                QuestionOption("D", "Εφαρμογές Email (Clients)", False, "Εκτελούνται στα τελικά συστήματα."),
            ],
            correct_option_letter="B",
            detailed_justification="Ο πυρήνας αποτελείται από routers και switches (το πλέγμα των δικτύων). Web servers, κινητά και εφαρμογές βρίσκονται στο Network Edge.",
        ),
        # Part A - Question 2
        ExamQuestion(
            question_number=2,
            title="Κανόνας Longest Prefix Match (LPM)",
            question_type="Multiple Choice",
            prompt_text="Σύμφωνα με τον κανόνα Longest Prefix Match (LPM), όταν μια διεύθυνση προορισμού ταιριάζει σε πολλαπλές εγγραφές του πίνακα προώθησης, ποια εγγραφή επιλέγεται;",
            options=[
                QuestionOption("A", "Η εγγραφή με το μικρότερο αριθμό bits στο prefix.", False, "Το μικρότερο πρόθεμα είναι πιο γενικό και απορρίπτεται."),
                QuestionOption("B", "Η εγγραφή με το μεγαλύτερο αριθμό bits στο prefix.", True, "Το μεγαλύτερο πρόθεμα είναι το πιο ειδικό (specific) και υπερισχύει πάντοτε."),
                QuestionOption("C", "Η προεπιλεγμένη διαδρομή (default route).", False, "Η default route επιλέγεται μόνο όταν κανένα άλλο prefix δεν ταιριάζει."),
                QuestionOption("D", "Η πρώτη εγγραφή που βρίσκεται στον πίνακα.", False, "Η σειρά στον πίνακα δεν καθορίζει την επιλογή στο LPM."),
            ],
            correct_option_letter="B",
            detailed_justification="Το Longest Prefix Match σημαίνει 'το μεγαλύτερο σε μήκος πρόθεμα' που ταιριάζει. Είναι το πιο ειδικό/συγκεκριμένο (π.χ. /28 υπερισχύει του /24 και του /16).",
        ),
        # Part A - Question 3
        ExamQuestion(
            question_number=3,
            title="Ρόλος του Data Plane έναντι του Control Plane",
            question_type="Multiple Choice",
            prompt_text="Το Data Plane ενός δρομολογητή είναι υπεύθυνο για:",
            options=[
                QuestionOption("A", "Την εκτέλεση του αλγορίθμου Dijkstra.", False, "Ανήκει στο Control Plane."),
                QuestionOption("B", "Τη φυσική προώθηση των πακέτων από την είσοδο στην κατάλληλη έξοδο (forwarding).", True, "Το Data Plane υλοποιείται σε εξειδικευμένο hardware (ASIC/TCAM) για ταχύτατη προώθηση."),
                QuestionOption("C", "Την ανταλλαγή μηνυμάτων OSPF με άλλους δρομολογητές.", False, "Ανήκει στο Control Plane."),
                QuestionOption("D", "Τη διατήρηση του Routing Table (RIB).", False, "Ανήκει στο Control Plane."),
            ],
            correct_option_letter="B",
            detailed_justification="Το Data plane δουλεύει στο επίπεδο του hardware για την ταχύτατη τοπική προώθηση (Forwarding). Το Control plane ασχολείται με τη συνολική δρομολόγηση, τους αλγορίθμους και τη σύνταξη των πινάκων.",
        ),
        # Part A - Question 4
        ExamQuestion(
            question_number=4,
            title="Πρόβλημα Count-to-Infinity σε Αλγορίθμους Δρομολόγησης",
            question_type="Multiple Choice",
            prompt_text="Το πρόβλημα 'Count-to-Infinity' είναι μια γνωστή αδυναμία στους αλγόριθμους δρομολόγησης τύπου:",
            options=[
                QuestionOption("A", "Link State (Κατάστασης Ζεύξης)", False, "Το Link-State έχει καθολική γνώση και δεν υποφέρει από Count-to-Infinity."),
                QuestionOption("B", "Distance Vector (Διάνυσμα Απόστασης)", True, "Λόγω της αργής διάδοσης κακών ειδήσεων (bad news travel slow), οι κόμβοι δημιουργούν βρόχους αυξάνοντας το κόστος στο άπειρο."),
                QuestionOption("C", "Longest Prefix Match", False, "Είναι μέθοδος αναζήτησης IP, όχι αλγόριθμος δρομολόγησης."),
                QuestionOption("D", "CSMA/CD", False, "Είναι πρωτόκολλο Layer 2."),
            ],
            correct_option_letter="B",
            detailed_justification="Στον αλγόριθμο Distance Vector (π.χ. RIP/Bellman-Ford), αν διακοπεί μια σύνδεση, οι κόμβοι μπορεί να ανταλλάσσουν μεταξύ τους απαρχαιωμένες πληροφορίες αυξάνοντας το υποτιθέμενο κόστος στο άπειρο (16 στο RIP).",
        ),
        # Part A - Question 5
        ExamQuestion(
            question_number=5,
            title="Θεωρητικές Προτάσεις TCP & Δικτύων (Σωστό/Λάθος)",
            question_type="Multiple Choice",
            prompt_text=(
                "Επιλέξτε Σωστό (Σ) ή Λάθος (Λ) για τις παρακάτω προτάσεις:\n"
                "1. Το πρωτόκολλο TCP χρησιμοποιεί αθροιστικές επιβεβαιώσεις (cumulative ACKs).\n"
                "2. Ένας Tier-1 ISP συνήθως πληρώνει για την ανταλλαγή κίνησης (transit) με άλλους Tier-1 ISPs.\n"
                "3. Ένα Layer 2 Switch χωρίζει το collision domain αλλά όχι το broadcast domain."
            ),
            options=[
                QuestionOption("A", "1: Σ, 2: Σ, 3: Σ", False, "Οι Tier-1 ISPs δεν πληρώνουν transit."),
                QuestionOption("B", "1: Σ, 2: Λ, 3: Σ", True, "1=Σ (Cumulative ACKs υποδηλώνουν επόμενο αναμενόμενο byte), 2=Λ (Δωρεάν peering μεταξύ Tier-1), 3=Σ (Απομόνωση collisions, κοινό broadcast)."),
                QuestionOption("C", "1: Λ, 2: Λ, 3: Σ", False, "Το TCP χρησιμοποιεί όντως cumulative ACKs."),
                QuestionOption("D", "1: Σ, 2: Λ, 3: Λ", False, "Το switch προωθεί τα broadcasts σε όλες τις θύρες."),
            ],
            correct_option_letter="B",
            detailed_justification=(
                "1. **Σωστό:** Το TCP επιβεβαιώνει τα δεδομένα αθροιστικά (το ACK number δηλώνει το επόμενο byte που αναμένει).\n"
                "2. **Λάθος:** Οι Tier-1 ISPs συνδέονται μεταξύ τους με settlement-free peering (χωρίς χρέωση) και δεν πληρώνουν κανέναν για transit.\n"
                "3. **Σωστό:** Το switch δημιουργεί ανεξάρτητο collision domain ανά θύρα, αλλά διατηρεί 1 ενιαίο broadcast domain."
            ),
        ),
        # Part B - Άσκηση 1
        ExamQuestion(
            question_number=6,
            title="Άσκηση 1: Αναζήτηση σε Πίνακα Προώθησης με Longest Prefix Match",
            question_type="Calculations",
            prompt_text=(
                "Δίνεται ο παρακάτω πίνακας προώθησης ενός δρομολογητή:\n\n"
                "| Prefix Δικτύου | Interface |\n"
                "|---|---|\n"
                "| 10.20.0.0/16 | Eth0 |\n"
                "| 10.20.30.0/24 | Eth1 |\n"
                "| 10.20.30.64/26 | Eth2 |\n"
                "| 0.0.0.0/0 (Default) | Eth3 |\n\n"
                "Σε ποιο Interface θα προωθηθούν τα πακέτα με τις ακόλουθες IP διευθύνσεις προορισμού;\n"
                "1. `10.20.30.100`\n"
                "2. `10.20.31.5`\n"
                "3. `10.21.5.1`\n"
                "4. `10.20.30.20`"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ανάλυση Εύρους Δικτύων",
                    formula="CIDR Ranges",
                    substitution="/16: 10.20.0.0 - 10.20.255.255 | /24: 10.20.30.0 - 10.20.30.255 | /26: 10.20.30.64 - 10.20.30.127",
                    result="3 ιεραρχικά επικαλυπτόμενα δίκτυα",
                    rationale="Όσο μεγαλύτερο το πρόθεμα (prefix length), τόσο πιο συγκεκριμένη η εγγραφή.",
                ),
                CalculationStep(
                    step_number=2,
                    title="1. IP 10.20.30.100 -> Eth2",
                    formula="LPM: Match /16, /24, /26 -> Select /26",
                    substitution="Το 100 βρίσκεται εντός 64-127",
                    result="Eth2",
                    rationale="Η εγγραφή /26 έχει το μεγαλύτερο μήκος προθέματος (26 bits).",
                ),
                CalculationStep(
                    step_number=3,
                    title="2. IP 10.20.31.5 -> Eth0",
                    formula="Match /16 (όχι /24, όχι /26)",
                    substitution="Το τρίτο byte είναι 31, άρα δεν ταιριάζει με 10.20.30.0/24",
                    result="Eth0",
                    rationale="Ταιριάζει μόνο με το /16.",
                ),
                CalculationStep(
                    step_number=4,
                    title="3. IP 10.21.5.1 -> Eth3",
                    formula="No specific match -> Default Route",
                    substitution="Το δεύτερο byte είναι 21, άρα καμία εγγραφή 10.20 δεν ταιριάζει",
                    result="Eth3",
                    rationale="Επιλέγεται η προεπιλεγμένη διαδρομή (default route 0.0.0.0/0).",
                ),
                CalculationStep(
                    step_number=5,
                    title="4. IP 10.20.30.20 -> Eth1",
                    formula="Match /16 και /24 (εκτός /26)",
                    substitution="Το 20 είναι μικρότερο από το 64, άρα δεν ανήκει στο /26",
                    result="Eth1",
                    rationale="Μεταξύ /16 και /24, το /24 είναι μακρύτερο και επιλέγεται.",
                ),
            ],
            detailed_justification=(
                "Ο κανόνας LPM υπαγορεύει:\n"
                "1. **IP: 10.20.30.100** -> **Eth2** (Ταιριάζει με /16, /24 και /26. Επιλέγεται το /26).\n"
                "2. **IP: 10.20.31.5** -> **Eth0** (Ταιριάζει μόνο με το /16).\n"
                "3. **IP: 10.21.5.1** -> **Eth3** (Δεν ταιριάζει σε κανένα συγκεκριμένο prefix, προωθείται στο Default Eth3).\n"
                "4. **IP: 10.20.30.20** -> **Eth1** (Ταιριάζει με /16 και /24. Επιλέγεται το /24 καθώς το 20 < 64)."
            ),
        ),
        # Part B - Άσκηση 2
        ExamQuestion(
            question_number=7,
            title="Άσκηση 2: Αλγόριθμος Distance Vector (Bellman-Ford) & Next-Hop",
            question_type="Calculations",
            prompt_text=(
                "Σε ένα δίκτυο Bellman-Ford, ο δρομολογητής X έχει γείτονες: Y (κόστος=3), Z (κόστος=2), W (κόστος=4).\n"
                "Ο X λαμβάνει τους παρακάτω πίνακες από τους γείτονές του προς τον προορισμό **D**:\n"
                "- Από Y: Κόστος προς D = 5\n"
                "- Από Z: Κόστος προς D = 6\n"
                "- Από W: Κόστος προς D = 2\n\n"
                "**a.** Ποιο είναι το νέο υπολογισμένο κόστος από τον κόμβο X προς τον D;\n"
                "**b.** Μέσω ποιου γείτονα (Next-Hop) θα δρομολογεί ο X τα πακέτα του προς τον D;"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Εξίσωση Bellman-Ford",
                    formula="d_X(D) = min_v { c(X, v) + d_v(D) }",
                    substitution="v in {Y, Z, W}",
                    result="Ελάχιστο άθροισμα άμεσου κόστους και διαφημιζόμενης απόστασης",
                    rationale="Ο δρομολογητής εξετάζει όλες τις εναλλακτικές μέσω των άμεσων γειτόνων του.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Υπολογισμός Κόστους ανά Γείτονα",
                    formula="Μέσω Y, Z, W",
                    substitution="Y: 3 + 5 = 8 | Z: 2 + 6 = 8 | W: 4 + 2 = 6",
                    result="min(8, 8, 6) = 6",
                    rationale="Η διαδρομή μέσω του κόμβου W δίνει το ελάχιστο συνολικό κόστος.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Προσδιορισμός Next-Hop",
                    formula="Next_Hop = argmin_v { c(X,v) + d_v(D) }",
                    substitution="Επιτυγχάνεται για v = W",
                    result="Next-Hop: W",
                    rationale="Ο X θα καταχωρήσει στον πίνακα δρομολόγησής του: Destination D -> Next-Hop W, Cost 6.",
                ),
            ],
            detailed_justification=(
                "- **a. Νέο κόστος:** $d_X(D) = \\min \\{3+5, 2+6, 4+2\\} = \\mathbf{6}$.\n"
                "- **b. Next-Hop:** Ο γείτονας **W**."
            ),
        ),
        # Part B - Άσκηση 3
        ExamQuestion(
            question_number=8,
            title="Άσκηση 3: Διευθυνσιοδότηση ARP μέσω Router & BDP",
            question_type="Calculations",
            prompt_text=(
                "**a.** Δίνεται τοπολογία:\n"
                "`[Host A] ------------------ [Router R] ------------------ [Host B]`\n"
                "Host A: IP 10.0.0.5, MAC 00:AA:11:22:33:44\n"
                "Router R: IP_Left 10.0.0.1, MAC_Left 00:RR:AA:BB:CC:01 | IP_Right 192.168.1.1, MAC_Right 00:RR:AA:BB:CC:02\n"
                "Host B: IP 192.168.1.10, MAC 00:BB:99:88:77:66\n"
                "- i. Ποιο ARP αίτημα θα στείλει ο A για να επικοινωνήσει με τον B;\n"
                "- ii. Ποιες είναι οι L2/L3 διευθύνσεις όταν το πακέτο αναχωρεί από τον R προς τον B;\n\n"
                "**b.** Ζεύξη μεταξύ δύο ηπείρων με s = 2*10^8 m/s, d = 4.000 km και R = 1 Gbps.\n"
                "- i. Ποια είναι η καθυστέρηση διάδοσης (d_prop);\n"
                "- ii. Ποιο είναι το Bandwidth-Delay Product (BDP);"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ερώτημα a.i: ARP Request από Host A",
                    formula="ARP_Request(Gateway)",
                    substitution="Sender IP: 10.0.0.5, Sender MAC: 00:AA:11:22:33:44, Target IP: 10.0.0.1",
                    result="L2 Frame Dest MAC: FF:FF:FF:FF:FF:FF",
                    rationale="Επειδή ο B είναι σε εξωτερικό δίκτυο, ο A αναζητά τη MAC της πύλης του (10.0.0.1).",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ερώτημα a.ii: Στοιχεία Πακέτου κατά την Έξοδο από τον Router R",
                    formula="L3 IPs remain unchanged, L2 MACs change",
                    substitution="Src IP: 10.0.0.5, Dst IP: 192.168.1.10 | Src MAC: 00:RR:AA:BB:CC:02, Dst MAC: 00:BB:99:88:77:66",
                    result="Src MAC = MAC_Right του R, Dst MAC = MAC του B",
                    rationale="Οι IP διευθύνσεις παραμένουν σταθερές end-to-end, ενώ οι MAC διευθύνσεις αντικαθίστανται σε κάθε hop.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Ερώτημα b.i: Καθυστέρηση Διάδοσης d_prop",
                    formula="d_prop = d / s",
                    substitution="(4000 * 10^3 m) / (2 * 10^8 m/s) = 4*10^6 / 2*10^8",
                    result="0.02 s = 20 ms",
                    rationale="Χρόνος ταξιδιού σήματος στο υπερωκεάνιο καλώδιο.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Ερώτημα b.ii: Υπολογισμός BDP",
                    formula="BDP = R * d_prop",
                    substitution="10^9 bps * 0.02 s",
                    result="20,000,000 bits (20 Mbits)",
                    rationale="Μέγιστος αριθμός bits εν πτήσει στο φυσικό καλώδιο.",
                ),
            ],
            detailed_justification=(
                "**a.i ARP Request από A:**\n"
                "- Sender IP: `10.0.0.5`, Sender MAC: `00:AA:11:22:33:44`\n"
                "- Target IP: `10.0.0.1` (IP της πύλης R)\n"
                "- Frame Dest MAC: `FF:FF:FF:FF:FF:FF` (Broadcast)\n\n"
                "**a.ii Πακέτο Δεδομένων R -> B:**\n"
                "- Source IP: `10.0.0.5` (αμετάβλητη)\n"
                "- Destination IP: `192.168.1.10` (αμετάβλητη)\n"
                "- Source MAC: `00:RR:AA:BB:CC:02` (δεξιά πόρτα του R)\n"
                "- Destination MAC: `00:BB:99:88:77:66` (MAC του B)\n\n"
                "**b. Υπερωκεάνια Ζεύξη:**\n"
                "- $d_{\\text{prop}} = \\frac{4.000 \\times 10^3}{2 \\times 10^8} = 0,02\\text{ s} = 20\\text{ ms}$\n"
                "- $\\text{BDP} = 10^9 \\times 0,02 = 20.000.000\\text{ bits} = 20\\text{ Mbits}$."
            ),
        ),
    ]

    nodes = [
        TopologyNode("r_in", "Ingress Router", "router", 120, 150, "192.168.1.1", "00:11:22:33:44:01"),
        TopologyNode("r_core", "Core Router (LPM)", "router", 420, 150, "10.0.0.1", "00:11:22:33:44:02"),
        TopologyNode("sub1", "Subnet /24 (eth0)", "host", 720, 80, "192.168.10.0/24"),
        TopologyNode("sub2", "Subnet /28 (eth1)", "host", 720, 220, "192.168.10.16/28"),
    ]

    links = [
        TopologyLink("r_in", "r_core", 1000, 10.0, 2.0, "fiber", "1G Fiber"),
        TopologyLink("r_core", "sub1", 100, 0.5, 2.0, "copper", "eth0 /24"),
        TopologyLink("r_core", "sub2", 100, 0.5, 2.0, "copper", "eth1 /28 (LPM Match)"),
    ]

    return NetworkScenario(
        id="exam_synth_2",
        title="Synthetic Exam 2: LPM & Distance-Vector",
        subtitle="Network Core, LPM Forwarding Lookups, Bellman-Ford Next-Hop, ARP & BDP",
        course_tag="Synthetic Realistic",
        duration_info="2 ώρες και 15 λεπτά",
        paragraphs=paragraphs,
        questions=questions,
        nodes=nodes,
        links=links,
        methodology_summary=[
            "1. Routers = Network Core (Data plane forwarding).",
            "2. LPM: Μεγαλύτερο μήκος prefix = Πιο ειδική διαδρομή.",
            "3. Distance-Vector: d_X(D) = min_v { c(X,v) + d_v(D) }.",
            "4. L2/L3 Addressing: IP μένει σταθερή, MAC αλλάζει ανά hop.",
            "5. BDP = R * d_prop (20 Mbits).",
        ],
        calculator_type="lpm",
    )
