"""Synthetic & Realistic Exam 3 Scenario Module.

Contains 1-to-1 representation of all exam questions from Synthetic & Realistic Exam 3:
- Part A: Peer-to-Peer architecture, Store-and-Forward principles, /26 subnet boundaries,
  Traceroute TTL mechanics, True/False (DNS Client-Server, MAC vs IP stability, RIP hop limit).
- Part B: Άσκηση 1 (3-hop Store-and-Forward with intermediate processing delay = 19 ms),
  Άσκηση 2 (Pipelining effect of 50 packets across 2 hops = 0.255 s),
  Άσκηση 3 (Cisco IOS OSPF CLI configuration & Google BBR CWND = 2.5 MB).
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
    """Constructs and returns Synthetic & Realistic Exam 3 scenario.

    Returns:
        NetworkScenario: The structured scenario object with 1-to-1 parity.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Το διαγώνισμα προσομοίωσης "),
                TextSegment(
                    text="Synthetic & Realistic Exam 3",
                    is_highlight=True,
                    category="protocol",
                    tag_label="SYNTHETIC REALISTIC 3",
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
                TextSegment(text="Στο υπολογιστικό μέρος περιλαμβάνεται πλήρης ανάλυση "),
                TextSegment(
                    text="Store-and-Forward με Processing Delay (d_total = 19 ms)",
                    is_highlight=True,
                    category="delay",
                    tag_label="3 HOPS DELAY",
                    tooltip="N = 3 hops, d_proc = 0.5 ms -> 19 ms",
                ),
                TextSegment(text=", το φαινόμενο της "),
                TextSegment(
                    text="Διοχέτευσης Πακέτων (Pipelining Effect)",
                    is_highlight=True,
                    category="delay",
                    tag_label="PIPELINING",
                    tooltip="(N + P - 1) * d_trans για 50 πακέτα σε 2 hops",
                ),
                TextSegment(text=", καθώς και διαμόρφωση "),
                TextSegment(
                    text="OSPF σε Cisco IOS & Google BBR CWND",
                    is_highlight=True,
                    category="routing",
                    tag_label="OSPF & BBR",
                    tooltip="Wildcard masks και CWND = RtProp * BtlBw = 2.5 MB",
                ),
                TextSegment(text="."),
            ]
        ),
    ]

    questions = [
        # Part A - Question 1
        ExamQuestion(
            question_number=1,
            title="Χαρακτηριστικά Αρχιτεκτονικής Peer-to-Peer (P2P)",
            question_type="Multiple Choice",
            prompt_text="Σε ένα καθαρό Peer-to-Peer (P2P) δίκτυο, ποιο από τα παρακάτω ισχύει;",
            options=[
                QuestionOption("A", "Η αξιοπιστία του δικτύου εξαρτάται αποκλειστικά από έναν κεντρικό Server.", False, "Στο P2P δεν υπάρχει κεντρικός server (αποκεντρωμένο)."),
                QuestionOption("B", "Η προσθήκη νέων χρηστών μειώνει πάντα το διαθέσιμο bandwidth.", False, "Οι νέοι χρήστες φέρνουν και upload capacity (αυτο-κλιμάκωση / self-scalability)."),
                QuestionOption("C", "Κάθε κόμβος (peer) λειτουργεί ταυτόχρονα ως client και ως server.", True, "Κάθε peer ζητά αρχεία (client) και ταυτόχρονα εξυπηρετεί άλλους χρήστες (server)."),
                QuestionOption("D", "Είναι αδύνατη η κοινή χρήση αρχείων.", False, "Το P2P χρησιμοποιείται κατά κόρον για file sharing (π.χ. BitTorrent)."),
            ],
            correct_option_letter="C",
            detailed_justification="Στο μοντέλο Peer-to-Peer όλοι οι κόμβοι είναι ισότιμοι (servents = server + client), προσφέροντας φυσική αυτο-κλιμάκωση (self-scalability).",
        ),
        # Part A - Question 2
        ExamQuestion(
            question_number=2,
            title="Αρχή Λειτουργίας Store-and-Forward",
            question_type="Multiple Choice",
            prompt_text="Η λειτουργία 'Store-and-Forward' σε έναν δρομολογητή (router) σημαίνει ότι:",
            options=[
                QuestionOption("A", "Ο δρομολογητής πρέπει να λάβει ολόκληρο το πακέτο πριν αρχίσει την προώθησή του.", True, "Πρέπει να ληφθούν όλα τα bits του πακέτου ώστε να ελεγχθεί το checksum/CRC πριν ξεκινήσει η μετάδοση στην επόμενη ζεύξη."),
                QuestionOption("B", "Ο δρομολογητής αποθηκεύει τα πακέτα μόνιμα στο σκληρό του δίσκο.", False, "Αποθηκεύονται προσωρινά στη μνήμη buffer."),
                QuestionOption("C", "Η προώθηση ξεκινά μόλις ληφθεί η κεφαλίδα (header) του πακέτου.", False, "Αυτό είναι Cut-through switching, όχι Store-and-Forward."),
                QuestionOption("D", "Ο δρομολογητής δεν ελέγχει ποτέ για σφάλματα κατά τη μεταφορά.", False, "Ελέγχει πλήρως για σφάλματα."),
            ],
            correct_option_letter="A",
            detailed_justification="Αυτή είναι η βασική αρχή του Store-and-Forward στο packet switching, προσθέτοντας καθυστέρηση μετάδοσης σε κάθε hop.",
        ),
        # Part A - Question 3
        ExamQuestion(
            question_number=3,
            title="Ταύτιση Υποδικτύου IPv4 /26",
            question_type="Multiple Choice",
            prompt_text="Ποια από τις παρακάτω IP διευθύνσεις ανήκει στο ίδιο υποδίκτυο με την 172.16.30.200/26;",
            options=[
                QuestionOption("A", "172.16.30.10", False, "Ανήκει στο 1ο υποδίκτυο (0-63)."),
                QuestionOption("B", "172.16.30.63", False, "Είναι το broadcast του 1ου υποδικτύου."),
                QuestionOption("C", "172.16.30.250", True, "Η μάσκα /26 έχει block size 64. Το 4ο υποδίκτυο καλύπτει 192-255. Το .200 και το .250 ανήκουν και τα δύο σε αυτό."),
                QuestionOption("D", "172.16.30.127", False, "Είναι το broadcast του 2ου υποδικτύου (64-127)."),
            ],
            correct_option_letter="C",
            detailed_justification="Η μάσκα /26 σημαίνει 255.255.255.192. Block size = 256 - 192 = 64. Υποδίκτυα: .0-.63, .64-.127, .128-.191, .192-.255. Το 172.16.30.200 και το 172.16.30.250 ανήκουν και τα δύο στο 4ο υποδίκτυο.",
        ),
        # Part A - Question 4
        ExamQuestion(
            question_number=4,
            title="Μηχανισμός Εργαλείου Traceroute (TTL)",
            question_type="Multiple Choice",
            prompt_text="Το Traceroute (ή Tracert) είναι ένα εργαλείο που:",
            options=[
                QuestionOption("A", "Επιστρέφει τη MAC διεύθυνση ενός απομακρυσμένου υπολογιστή.", False, "Αυτό είναι λειτουργία του ARP."),
                QuestionOption("B", "Εντοπίζει τη διαδρομή των δρομολογητών που ακολουθεί ένα πακέτο χρησιμοποιώντας το πεδίο TTL.", True, "Στέλνει πακέτα με αυξανόμενο TTL ώστε οι ενδιάμεσοι routers να απαντούν με ICMP Time Exceeded."),
                QuestionOption("C", "Μετράει την ταχύτητα του σκληρού δίσκου.", False, "Δεν έχει σχέση με δίσκους."),
                QuestionOption("D", "Κρυπτογραφεί τα δεδομένα μεταξύ δύο κόμβων.", False, "Δεν εκτελεί κρυπτογράφηση."),
            ],
            correct_option_letter="B",
            detailed_justification="Το Traceroute στέλνει πακέτα με αυξανόμενο TTL ($1, 2, 3, \\dots$), κάνοντας τους ενδιάμεσους δρομολογητές να απορρίπτουν το πακέτο και να επιστρέφουν ICMP Time Exceeded μηνύματα, αποκαλύπτοντας την ταυτότητά τους.",
        ),
        # Part A - Question 5
        ExamQuestion(
            question_number=5,
            title="Θεωρητικές Προτάσεις DNS, Addressing & RIP (Σωστό/Λάθος)",
            question_type="Multiple Choice",
            prompt_text=(
                "Επιλέξτε Σωστό (Σ) ή Λάθος (Λ) για τις παρακάτω προτάσεις:\n"
                "1. Ένα DNS αίτημα λειτουργεί με βάση το μοντέλο Client-Server.\n"
                "2. Η διεύθυνση MAC παραμένει ίδια καθώς το πακέτο διασχίζει πολλούς δρομολογητές στο διαδίκτυο, ενώ η IP αλλάζει σε κάθε hop.\n"
                "3. Το πρωτόκολλο RIP έχει μέγιστο hop count 15, κάνοντας το ακατάλληλο για τεράστια δίκτυα."
            ),
            options=[
                QuestionOption("A", "1: Σ, 2: Σ, 3: Σ", False, "Η πρόταση 2 είναι λάθος."),
                QuestionOption("B", "1: Σ, 2: Λ, 3: Σ", True, "1=Σ (Ο host κάνει DNS request στον DNS server), 2=Λ (Η IP μένει σταθερή, η MAC αλλάζει ανά hop), 3=Σ (RIP metric max 15, 16=άπειρο)."),
                QuestionOption("C", "1: Λ, 2: Λ, 3: Σ", False, "Το DNS είναι κλασικό client-server."),
                QuestionOption("D", "1: Σ, 2: Λ, 3: Λ", False, "Το RIP έχει όριο 15 hops."),
            ],
            correct_option_letter="B",
            detailed_justification=(
                "1. **Σωστό:** Ο υπολογιστής στέλνει DNS Request (Client) και ο DNS server απαντά με την αντιστοιχία IP.\n"
                "2. **Λάθος:** Συμβαίνει ακριβώς το αντίστροφο: Η IP παραμένει σταθερή end-to-end, ενώ η MAC διεύθυνση αλλάζει σε κάθε router hop.\n"
                "3. **Σωστό:** Το RIP χρησιμοποιεί metric το hop count με μέγιστο το 15 (το 16 θεωρείται άπειρο/μη προσβάσιμο)."
            ),
        ),
        # Part B - Άσκηση 1
        ExamQuestion(
            question_number=6,
            title="Άσκηση 1: Store-and-Forward με Processing Delay (3 Hops)",
            question_type="Calculations",
            prompt_text=(
                "Διαδρομή από Υπολογιστή Α σε Υπολογιστή Β μέσω 2 ενδιάμεσων δρομολογητών (N = 3 hops).\n"
                "Κάθε ζεύξη: d = 1.000 km, s = 2*10^8 m/s, R = 10 Mbps.\n"
                "Μέγεθος πακέτου: L = 10.000 bits. Κάθε ενδιάμεσος δρομολογητής έχει d_proc = 0,5 ms. Αγνοήστε ουρές.\n\n"
                "**a.** Πόση είναι η καθυστέρηση μετάδοσης (d_trans) ανά hop;\n"
                "**b.** Πόση είναι η καθυστέρηση διάδοσης (d_prop) ανά hop;\n"
                "**c.** Υπολογίστε τη συνολική καθυστέρηση από άκρο σε άκρο (Total end-to-end delay)."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ερώτημα a: Καθυστέρηση Μετάδοσης ανά Hop",
                    formula="d_trans = L / R",
                    substitution="10,000 bits / (10 * 10^6 bps)",
                    result="0.001 s = 1 ms",
                    rationale="Χρόνος διοχέτευσης των bits σε μία ζεύξη.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ερώτημα b: Καθυστέρηση Διάδοσης ανά Hop",
                    formula="d_prop = d / s",
                    substitution="1,000,000 m / (2 * 10^8 m/s)",
                    result="0.005 s = 5 ms",
                    rationale="Χρόνος ταξιδιού φωτεινού παλμού στην οπτική ίνα 1.000 km.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Ερώτημα c: Συνολική Καθυστέρηση με 2 Ενδιάμεσους Routers",
                    formula="d_total = N * d_trans + N * d_prop + (N - 1) * d_proc",
                    substitution="3 * (1 ms) + 3 * (5 ms) + 2 * (0.5 ms)",
                    result="3 ms + 15 ms + 1 ms = 19 ms",
                    rationale="3 μεταδόσεις, 3 διαδόσεις και 2 καθυστερήσεις επεξεργασίας στους 2 ενδιάμεσους δρομολογητές.",
                ),
            ],
            detailed_justification=(
                "- **a.** $d_{\\text{trans}} = \\frac{10.000}{10 \\times 10^6} = 0,001\\text{ s} = 1\\text{ ms}$\n"
                "- **b.** $d_{\\text{prop}} = \\frac{1 \\times 10^6}{2 \\times 10^8} = 0,005\\text{ s} = 5\\text{ ms}$\n"
                "- **c.** $d_{\\text{total}} = 3 \\cdot (1\\text{ ms}) + 3 \\cdot (5\\text{ ms}) + 2 \\cdot (0,5\\text{ ms}) = 3 + 15 + 1 = 19\\text{ ms}$."
            ),
        ),
        # Part B - Άσκηση 2
        ExamQuestion(
            question_number=7,
            title="Άσκηση 2: Φαινόμενο Διοχέτευσης (Pipeline Effect) με 50 Πακέτα",
            question_type="Calculations",
            prompt_text=(
                "Ένα αρχείο χωρίζεται σε 50 πακέτα. Αποστέλλεται από τον Host X στον Host Y μέσω ενός ενδιάμεσου "
                "δρομολογητή Router R (N = 2 hops συνολικά). Ρυθμός κάθε ζεύξης R = 1 Mbps, L = 5.000 bits. "
                "(Αγνοήστε διάδοση, επεξεργασία και ουρές).\n\n"
                "**a.** Πόσος χρόνος χρειάζεται για να μεταδοθεί ένα πακέτο σε μια ζεύξη;\n"
                "**b.** Πόσος χρόνος χρειάζεται για να φτάσει το 1ο πακέτο στον Host Y;\n"
                "**c.** Ποιος είναι ο συνολικός χρόνος μέχρι να φτάσει και το 50ό (τελευταίο) πακέτο στον Host Y;"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ερώτημα a: Μετάδοση Ενός Πακέτου σε 1 Ζεύξη",
                    formula="d_trans = L / R",
                    substitution="5,000 bits / 1,000,000 bps",
                    result="0.005 s = 5 ms",
                    rationale="Χρόνος μετάδοσης ενός μεμονωμένου πακέτου.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ερώτημα b: Άφιξη 1ου Πακέτου στον Host Y",
                    formula="d_1st = 2 * d_trans",
                    substitution="2 * 0.005 s",
                    result="0.01 s = 10 ms",
                    rationale="Το πρώτο πακέτο διασχίζει 2 hops με Store-and-Forward.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Ερώτημα c: Συνολικός Χρόνος για 50 Πακέτα με Pipelining",
                    formula="d_total = (N + P - 1) * d_trans",
                    substitution="(2 + 50 - 1) * 0.005 s = 51 * 0.005 s",
                    result="0.255 s",
                    rationale="Ενώ το 1ο πακέτο προωθείται στο link 2, το 2ο πακέτο μεταδίδεται ταυτόχρονα στο link 1 (pipeline).",
                ),
            ],
            detailed_justification=(
                "Λόγω pipelining (ταυτόχρονη αξιοποίηση πολλαπλών ζεύξεων):\n"
                "- **a.** $d_{\\text{trans}} = \\frac{5.000}{10^6} = 0,005\\text{ s} = 5\\text{ ms}$\n"
                "- **b.** $d_{\\text{1st}} = 2 \\times 0,005\\text{ s} = 0,01\\text{ s} = 10\\text{ ms}$\n"
                "- **c.** $d_{\\text{total}} = (2 + 50 - 1) \\times 0,005 = 51 \\times 0,005 = 0,255\\text{ s}$."
            ),
        ),
        # Part B - Άσκηση 3
        ExamQuestion(
            question_number=8,
            title="Άσκηση 3: Διαμόρφωση OSPF & Google BBR CWND",
            question_type="Calculations",
            prompt_text=(
                "**a.** Για το δίκτυο της εικόνας ορίστε δρομολόγηση OSPF Single Area (συμπληρώστε τα κενά):\n"
                "Subnets: 172.16.8.0/29, 10.10.10.0/30, 192.168.1.0/24.\n\n"
                "**b.** Έστω σύνδεσμος BBR με RtProp = 10 ms και BtlBw = 0,25 GB/s. "
                "Υπολογίστε το μέγεθος του παραθύρου συμφόρησης CWND σε bits και Bytes."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ερώτημα a: Cisco OSPF CLI Commands",
                    formula="router ospf 1  &&  network <ip> <wildcard> area 0",
                    substitution="/30 -> 0.0.0.3 | /29 -> 0.0.0.7 | /24 -> 0.0.0.255",
                    result="network 10.10.10.0 0.0.0.3 area 0, network 172.16.8.0 0.0.0.7 area 0, network 192.168.1.0 0.0.0.255 area 0",
                    rationale="Ορθός υπολογισμός wildcard μάσκας ανά υποδίκτυο.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ερώτημα b: Υπολογισμός CWND BBR",
                    formula="CWND = RtProp * BtlBw",
                    substitution="0.01 s * (0.25 * 10^9 * 8 bps) = 0.01 * 2 * 10^9 bps",
                    result="20,000,000 bits = 2,500,000 Bytes (2.5 MB)",
                    rationale="Χωρητικότητα Bandwidth-Delay Product για πλήρη αξιοποίηση.",
                ),
            ],
            detailed_justification=(
                "**a. OSPF CLI:**\n"
                "```text\n"
                "R>en\n"
                "R# configure terminal\n"
                "R(config)# router ospf 1\n"
                "R(config-router)# network 10.10.10.0 0.0.0.3 area 0\n"
                "R(config-router)# network 172.16.8.0 0.0.0.7 area 0\n"
                "R(config-router)# network 192.168.1.0 0.0.0.255 area 0\n"
                "R(config-router)# end\n"
                "```\n\n"
                "**b. BBR CWND:**\n"
                "- $RtProp = 10\\text{ ms} = 0,01\\text{ s}$\n"
                "- $BtlBw = 0,25\\text{ GB/s} = 2,5 \\times 10^8\\text{ Bytes/s} = 2 \\times 10^9\\text{ bits/s}$\n"
                "- $CWND = 0,01 \\times 2 \\times 10^9 = 20.000.000\\text{ bits} = 2.500.000\\text{ Bytes} = 2,5\\text{ MB}$."
            ),
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
        subtitle="P2P Architecture, Store-and-Forward Delays (19ms), Pipelining (50 pkts), OSPF & BBR",
        course_tag="Synthetic Realistic",
        duration_info="2 ώρες και 15 λεπτά",
        paragraphs=paragraphs,
        questions=questions,
        nodes=nodes,
        links=links,
        methodology_summary=[
            "1. P2P: Servents (Clients + Servers ταυτόχρονα).",
            "2. Store-and-Forward: d_total = N*(L/R + d/s) + (N-1)*d_proc = 19 ms.",
            "3. Pipelining: d_total = (N + P - 1) * d_trans = 51 * 5 ms = 0.255 s.",
            "4. OSPF: 255.255.255.255 - Mask = Wildcard.",
            "5. BBR CWND = RtProp * BtlBw = 20 Mbits = 2.5 MB.",
        ],
        calculator_type="delay",
    )
