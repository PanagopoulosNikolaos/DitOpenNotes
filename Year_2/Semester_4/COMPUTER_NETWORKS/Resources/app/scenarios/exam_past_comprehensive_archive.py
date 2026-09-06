"""Past Exam Comprehensive Archive Scenario Module.

Contains 1-to-1 representation of all exam questions from the comprehensive archival paper:
- Part 1: The 4 Nodal Delays (d_proc, d_queue, d_trans, d_prop), AM-based BDP,
  Cisco IOS OSPF CLI configuration (4 subnets), TCP Sliding Window & Bits in Flight, BGP Hot-Potato Routing.
- Part 2: 1η Άσκηση (2-link delay & RTT), 2η Άσκηση (8-node Dijkstra execution table from root E,
  CSMA/CD 15 Mbps frame size), 3η Άσκηση Bonus (12-bit Hamming code with odd parity).
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
        NetworkScenario: The structured scenario object with 1-to-1 parity.
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
                TextSegment(text=" περιλαμβάνει πλήρη μαθηματική ανάλυση της "),
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
                    tooltip="Χωρητικότητα ζεύξης σε bits εν πτήσει",
                ),
                TextSegment(text=" και διαμόρφωση πρωτοκόλλου "),
                TextSegment(
                    text="OSPF σε Cisco IOS με 4 Υποδίκτυα",
                    is_highlight=True,
                    category="routing",
                    tag_label="OSPF L3",
                    tooltip="Διαμόρφωση Open Shortest Path First με wildcard masks",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="#e06b3a",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Στο δεύτερο μέρος αναλύεται η δρομολόγηση μεταξύ "),
                TextSegment(
                    text="Αυτόνομων Συστημάτων (BGP Hot-Potato Routing)",
                    is_highlight=True,
                    category="routing",
                    tag_label="BGP",
                    tooltip="Hot Potato routing vs shortest AS path",
                ),
                TextSegment(text=", υπολογισμοί "),
                TextSegment(
                    text="RTT σε 2 Ζεύξεις με ενδιάμεση επεξεργασία d_proc = 0.02 ms",
                    is_highlight=True,
                    category="delay",
                    tag_label="RTT STORE-FORWARD",
                    tooltip="Χρόνος αποστολής και επιστροφής πακέτων",
                ),
                TextSegment(text=", πλήρης εκτέλεση αλγορίθμου "),
                TextSegment(
                    text="Dijkstra σε τοπολογία 8 κόμβων από τη ρίζα E",
                    is_highlight=True,
                    category="routing",
                    tag_label="DIJKSTRA 8",
                    tooltip="Συντομότερο μονοπάτι προς όλους τους κόμβους",
                ),
                TextSegment(text=", υπολογισμός "),
                TextSegment(
                    text="Ελάχιστου Πλαισίου CSMA/CD στα 15 Mbps (96 Bytes)",
                    is_highlight=True,
                    category="error_check",
                    tag_label="CSMA/CD 15M",
                    tooltip="L_min = 2 * d_prop * R = 768 bits = 96 Bytes",
                ),
                TextSegment(text=" και κατασκευή "),
                TextSegment(
                    text="Κώδικα Hamming(12,8) με Περιττή Ισοτιμία",
                    is_highlight=True,
                    category="error_check",
                    tag_label="HAMMING(12,8)",
                    tooltip="Προστασία 8 bits δεδομένων με 4 bits ισοτιμίας",
                ),
                TextSegment(text="."),
            ]
        ),
    ]

    questions = [
        # Part 1 - Θέμα 1
        ExamQuestion(
            question_number=1,
            title="Θέμα 1: Ανάλυση των 4 Συνιστωσών Καθυστέρησης (Nodal Delays)",
            question_type="Theory Analysis",
            prompt_text=(
                "Έστω το δίκτυο της Εικόνας 1: `(A) -------> [queue] -------> (B)`\n"
                "Ορίστε αναλυτικά την καθυστέρηση από άκρο σε άκρο (end-to-end delay) ως μαθηματική έκφραση "
                "και εξηγήστε λεπτομερώς τα 4 επιμέρους σύμβολα που τη συνθέτουν."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Μαθηματικό Μοντέλο Κομβικής Καθυστέρησης",
                    formula="d_nodal = d_proc + d_queue + d_trans + d_prop",
                    substitution="Άθροισμα 4 ανεξάρτητων καθυστερήσεων σε κάθε κόμβο δικτύου",
                    result="d_end-to-end = Σ(d_nodal)",
                    rationale="Το συνολικό delay προκύπτει από τη διαδοχική συσσώρευση επεξεργασίας, ουράς, εκπομπής και διάδοσης.",
                ),
            ],
            detailed_justification=(
                "Η συνολική καθυστέρηση από άκρο σε άκρο ($d_{\\text{end-to-end}}$) αποτελείται από το άθροισμα τεσσάρων επιμέρους καθυστερήσεων:\n"
                "$$d_{\\text{end-to-end}} = d_{\\text{proc}} + d_{\\text{queue}} + d_{\\text{trans}} + d_{\\text{prop}}$$\n\n"
                "**Επεξήγηση συμβόλων:**\n"
                "1. **$d_{\\text{proc}}$ (Καθυστέρηση Επεξεργασίας / Processing Delay):** Ο χρόνος που απαιτείται για τον έλεγχο των επικεφαλίδων των πακέτων, την ανίχνευση σφαλμάτων bit (CRC/checksum) και τον προσδιορισμό του επόμενου κόμβου δρομολόγησης.\n"
                "2. **$d_{\\text{queue}}$ (Καθυστέρηση Ουράς / Queuing Delay):** Ο χρόνος αναμονής του πακέτου στην ουρά του μεταγωγέα/δρομολογητή μέχρι να ελευθερωθεί ο δίαυλος μετάδοσης. Εξαρτάται από τον ρυθμό άφιξης άλλων πακέτων και τη συμφόρηση.\n"
                "3. **$d_{\\text{trans}}$ (Καθυστέρηση Μετάδοσης / Transmission Delay):** Ο χρόνος διοχέτευσης όλων των bits του πακέτου στο φυσικό μέσο. Υπολογίζεται ως $d_{\\text{trans}} = \\frac{L}{R}$, όπου $L$ το μέγεθος του πακέτου σε bits και $R$ το Bandwidth σε bps.\n"
                "4. **$d_{\\text{prop}}$ (Καθυστέρηση Διάδοσης / Propagation Delay):** Ο χρόνος που χρειάζεται ένα bit για να διατρέξει τη φυσική απόσταση της ζεύξης. Υπολογίζεται ως $d_{\\text{prop}} = \\frac{d}{s}$, όπου $d$ η απόσταση και $s$ η ταχύτητα διάδοσης στο συγκεκριμένο μέσο (π.χ. $2 \\times 10^8$ m/s)."
            ),
            common_pitfalls=[
                "Σύγχυση καθυστέρησης μετάδοσης (L/R) με καθυστέρηση διάδοσης (d/s).",
                "Παράλειψη της καθυστέρησης ουράς όταν υπάρχει υψηλή ένταση κίνησης.",
            ],
        ),
        # Part 1 - Θέμα 2
        ExamQuestion(
            question_number=2,
            title="Θέμα 2: Bandwidth-Delay Product (BDP) με Παραμέτρους ΑΜ",
            question_type="Calculations",
            prompt_text=(
                "Έστω ζεύξη με Bandwidth = AM σε KB και Delay = τελευταίο ψηφίο AM σε ms (αν 0, θεωρείστε Delay = 5 ms). "
                "Ποιος είναι ο μέγιστος αριθμός bits που μπορούν να μεταφέρονται σε αυτή τη ζεύξη σε κάθε χρονική στιγμή (BDP); "
                "Εφαρμόστε αναλυτικά για AM = 3323."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Μαθηματικός Τύπος και Μετατροπή Μονάδων",
                    formula="BDP = Bandwidth * Delay",
                    substitution="Bandwidth = N * 1000 * 8 = 8000 * N bps | Delay = d * 10^-3 s",
                    result="BDP = 8 * N * d bits",
                    rationale="Μετατροπή KB σε bits/s και ms σε s.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Αριθμητική Εφαρμογή για AM = 3323 (d = 3)",
                    formula="BDP = 8 * 3323 * 3",
                    substitution="26,584,000 bps * 0.003 s",
                    result="79,752 bits",
                    rationale="Ο μέγιστος αριθμός bits που μπορούν να βρίσκονται 'εν πτήσει' πάνω στο φυσικό μέσο.",
                ),
            ],
            detailed_justification=(
                "$$\\text{Max Bits} = \\text{Bandwidth} \\times \\text{Delay} = (8000 \\times N) \\times (d \\times 10^{-3}) = 8 \\times N \\times d\\text{ bits}$$\n\n"
                "Για AM = 3323 ($N = 3323, d = 3$):\n"
                "- $R = 3323 \\times 1000 \\times 8 = 26.584.000\\text{ bps}$\n"
                "- $D = 3\\text{ ms} = 0,003\\text{ s}$\n"
                "- $\\text{Max Bits} = 26.584.000 \\times 0,003 = 79.752\\text{ bits}$."
            ),
        ),
        # Part 1 - Θέμα 3
        ExamQuestion(
            question_number=3,
            title="Θέμα 3: Διαμόρφωση OSPF με 4 Υποδίκτυα σε Cisco IOS",
            question_type="Calculations",
            prompt_text=(
                "Για το δίκτυο της Εικόνας 2 ορίστε δρομολόγηση OSPF υποθέτοντας μόνο μία περιοχή (Area 0):\n"
                "```text\n"
                "              172.16.8.0/29\n"
                "                    |\n"
                "      10.10.10.0/30 |\n"
                "              \\   /----\\\n"
                "               \\ |   R  |\n"
                "                \\ \\----/\n"
                "                /   |\n"
                "               /    |\n"
                "      10.10.23.0/30 |\n"
                "              192.168.1.0/24\n"
                "```\n"
                "Συμπληρώστε τα κενά της γραμμής εντολών Cisco CLI."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Υπολογισμός Wildcard Masks",
                    formula="Wildcard = 255.255.255.255 - Subnet_Mask",
                    substitution="/30: 255.255.255.252 -> 0.0.0.3 | /29: 255.255.255.248 -> 0.0.0.7 | /24: 255.255.255.0 -> 0.0.0.255",
                    result="0.0.0.3, 0.0.0.3, 0.0.0.7, 0.0.0.255",
                    rationale="Αφαίρεση της μάσκας υποδικτύου από το broadcast wildcard 255.255.255.255.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Εντολές CLI Cisco IOS",
                    formula="network <ip> <wildcard> area 0",
                    substitution="network 10.10.10.0 0.0.0.3 area 0 | network 10.10.23.0 0.0.0.3 area 0 | network 172.16.8.0 0.0.0.7 area 0 | network 192.168.1.0 0.0.0.255 area 0",
                    result="Πλήρης διαμόρφωση OSPF",
                    rationale="Ενεργοποιεί το OSPF στα 4 interfaces του δρομολογητή R.",
                ),
            ],
            detailed_justification=(
                "```text\n"
                "R>en\n"
                "R# configure terminal\n"
                "R(config)# router ospf 1\n"
                "R(config-router)# network 10.10.10.0 0.0.0.3 area 0\n"
                "R(config-router)# network 10.10.23.0 0.0.0.3 area 0\n"
                "R(config-router)# network 172.16.8.0 0.0.0.7 area 0\n"
                "R(config-router)# network 192.168.1.0 0.0.0.255 area 0\n"
                "R(config-router)# end\n"
                "```"
            ),
        ),
        # Part 1 - Θέμα 4
        ExamQuestion(
            question_number=4,
            title="Θέμα 4: Μηχανισμός TCP Sliding Window, Timeout & Bits in Flight",
            question_type="Calculations",
            prompt_text=(
                "Το TCP χρησιμοποιεί κυλιόμενο παράθυρο (Sliding Window):\n"
                "- Timeout = 2 * EstimatedRTT\n"
                "- EstimatedRTT = a * EstimatedRTT + (1-a) * SampleRTT\n\n"
                "**a.** Πώς λαμβάνονται δείγματα RTT και πώς υπολογίζεται το SampleRTT;\n"
                "**b.** Με ποιο τρόπο παρακολουθείτε τη διαδρομή των πακέτων;\n"
                "**c.** Έστω σύνδεσμος με d_prop = 5 μs και R = 0,125 GB/s. Ποιος είναι ο μέγιστος αριθμός των bits in flight;"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Υπολογισμός Bits in Flight (Μονοδρομική Χωρητικότητα)",
                    formula="Bits_in_flight = R * d_prop",
                    substitution="R = 0.125 GB/s = 0.125 * 10^9 Bytes/s * 8 = 10^9 bps | d_prop = 5 * 10^-6 s",
                    result="10^9 bps * (5 * 10^-6 s) = 5,000 bits",
                    rationale="Ο αριθμός bits που αποστέλλονται πριν φτάσει το 1ο bit στον παραλήπτη.",
                ),
            ],
            detailed_justification=(
                "**a. SampleRTT & Κανόνας Karn:**\n"
                "- Το TCP μετράει το χρόνο μεταξύ αποστολής ενός segment και λήψης του αντίστοιχου ACK.\n"
                "- **Κανόνας Karn:** Δεν λαμβάνονται δείγματα RTT για τμήματα που επανεκπέμφθηκαν.\n"
                "- **TCP Timestamps (RFC 7323):** Εναλλακτικά, εισάγονται timestamps στην κεφαλίδα για ακριβή μέτρηση σε κάθε ACK.\n\n"
                "**b. Παρακολούθηση διαδρομής:**\n"
                "- Το πρόγραμμα **traceroute** στέλνει πακέτα με αυξανόμενο TTL. Οι ενδιάμεσοι routers επιστρέφουν **ICMP Time Exceeded** αποκαλύπτοντας την ταυτότητά τους.\n\n"
                "**c. Υπολογισμός Bits in flight:**\n"
                "- $R = 0,125 \\times 10^9 \\times 8 = 10^9\\text{ bps} = 1\\text{ Gbps}$\n"
                "- $d_{\\text{prop}} = 5\\ \\mu\\text{s} = 5 \\times 10^{-6}\\text{ s}$\n"
                "- $\\text{Bits in flight} = 10^9 \\times 5 \\times 10^{-6} = 5000\\text{ bits}$."
            ),
        ),
        # Part 1 - Θέμα 5
        ExamQuestion(
            question_number=5,
            title="Θέμα 5: BGP Hot-Potato Routing μεταξύ Αυτόνομων Συστημάτων",
            question_type="Theory Analysis",
            prompt_text=(
                "Έστω τα δίκτυα των Εικόνων 3 και 4 όπου ο κόμβος X στέλνει πακέτα στον Y. "
                "Ποια διαδρομή θα ακολουθήσουν τα πακέτα στην κάθε περίπτωση και γιατί, "
                "χρησιμοποιώντας το πρωτόκολλο BGP μεταξύ Verizon AS και AT&T AS;"
            ),
            detailed_justification=(
                "Στο BGP εφαρμόζεται η τακτική **δρομολόγησης 'καυτής πατάτας' (hot-potato routing)**:\n\n"
                "**Εικόνα 3:**\n"
                "- Η AT&T διαθέτει εξόδους F (2 hops από X) και I (5 hops από X).\n"
                "- Επιλέγεται η πλησιέστερη έξοδος F.\n"
                "- **Διαδρομή:** `X -> E -> F -> A -> B -> C -> D -> Y`.\n\n"
                "**Εικόνα 4:**\n"
                "- Η AT&T διαθέτει εξόδους F (2 hops) και J (2 hops).\n"
                "- Λόγω ισοπαλίας IGP, επιλέγεται η έξοδος J (δίνει 5 hops συνολικά `X -> H -> I -> J -> E -> Y` έναντι 9 hops μέσω F)."
            ),
        ),
        # Part 2 - 1η Άσκηση
        ExamQuestion(
            question_number=6,
            title="1η Άσκηση: Store-and-Forward Delays & RTT (A-B-C)",
            question_type="Calculations",
            prompt_text=(
                "Έστω `(A) ==== Link 1 ==== (B) ==== Link 2 ==== (C)`\n"
                "Link 1: R1 = 12000 bps, L1 = 10 km, u1 = 2.5*10^8 m/s.\n"
                "Link 2: R2 = 15000 bps, L2 = 50 km, u2 = 2.5*10^8 m/s.\n"
                "Μέγεθος πακέτου P bits (P = 1/2 AM).\n\n"
                "**A.** Χρόνος αποστολής ενός πακέτου A -> C.\n"
                "**B.** RTT πακέτου A -> B -> A (αγνοώντας d_proc).\n"
                "**C.** RTT πακέτου A -> C -> A με d_proc = 0.02 ms."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ερώτημα A: Χρόνος Αποστολής A -> C",
                    formula="t_total = d_trans1 + d_prop1 + d_trans2 + d_prop2",
                    substitution="d_trans1 = P/12000 | d_prop1 = 10000/2.5*10^8 = 0.04 ms | d_trans2 = P/15000 | d_prop2 = 50000/2.5*10^8 = 0.2 ms",
                    result="1.5 * 10^-4 * P + 0.00024 s",
                    rationale="Άθροισμα μετάδοσης και διάδοσης στις δύο διαδοχικές ζεύξεις.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ερώτημα B: RTT A -> B -> A",
                    formula="RTT_AB = 2 * d_trans1 + 2 * d_prop1",
                    substitution="2 * (P/12000) + 2 * (4 * 10^-5)",
                    result="P / 6000 + 8 * 10^-5 s",
                    rationale="Μετάδοση και διάδοση στη ζεύξη 1 κατά τη μετάβαση και την επιστροφή.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Ερώτημα C: RTT A -> C -> A με d_proc = 0.02 ms",
                    formula="RTT_AC = 2 * t_total + 3 * d_proc",
                    substitution="2 * (1.5 * 10^-4 * P + 0.00024) + 3 * (2 * 10^-5)",
                    result="3 * 10^-4 * P + 0.00054 s",
                    rationale="3 καθυστερήσεις επεξεργασίας: στο B στη μετάβαση, στο C στην αναστροφή και στο B στην επιστροφή.",
                ),
            ],
            detailed_justification=(
                "Αναλυτικές μαθηματικές εκφράσεις συναρτήσει του $P$:\n"
                "- **A:** $t_{\\text{total}} = 1,5 \\times 10^{-4} \\times P + 0,00024\\text{ s}$\n"
                "- **B:** $\\text{RTT}_{A-B} = \\frac{P}{6000} + 8 \\times 10^{-5}\\text{ s}$\n"
                "- **C:** $\\text{RTT}_{A-C} = 3 \\times 10^{-4} \\times P + 0,00054\\text{ s}$"
            ),
        ),
        # Part 2 - 2η Άσκηση A
        ExamQuestion(
            question_number=7,
            title="2η Άσκηση (A): Αλγόριθμος Dijkstra σε Γράφο 8 Κόμβων από Ρίζα E",
            question_type="Algorithm Step",
            prompt_text=(
                "Εφαρμόστε τον αλγόριθμο Link-State Dijkstra στον γράφο 8 κόμβων (A, B, C, D, E, F, G, H) "
                "και υπολογίστε το συντομότερο μονοπάτι από τον κόμβο **E** προς όλους τους άλλους κόμβους.\n"
                "Ακμές: E-F:3, E-D:3, E-C:3, F-D:1, F-G:6, D-B:2, D-C:3, D-G:5, C-B:4, C-A:1, B-A:4, B-G:9, B-H:14, G-H:2."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Βήμα 1: Αρχικοποίηση από E (N = {E})",
                    formula="D(C)=3(E), D(D)=3(E), D(F)=3(E), άλλοι=inf",
                    substitution="Τριπλή ισοπαλία κόστους 3",
                    result="Μονιμοποίηση C, D, F",
                    rationale="Οι άμεσοι γείτονες του E έχουν όλοι κόστος 3.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Βήμα 2: Επέκταση προς A και B",
                    formula="D(A) = D(C) + c(C,A) = 3 + 1 = 4(C) | D(B) = D(D) + c(D,B) = 3 + 2 = 5(D)",
                    substitution="Μονιμοποίηση A με κόστος 4, έπειτα B με κόστος 5",
                    result="N = {E, C, D, F, A, B}",
                    rationale="Το A είναι προσβάσιμο μέσω C με κόστος 4, το B μέσω D με κόστος 5.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Βήμα 3: Επέκταση προς G και H",
                    formula="D(G) = D(D) + c(D,G) = 3 + 5 = 8(D) | D(H) = D(G) + c(G,H) = 8 + 2 = 10(G)",
                    substitution="Μονιμοποίηση G με κόστος 8, έπειτα H με κόστος 10",
                    result="Συντομότερα μονοπάτια για όλους τους κόμβους",
                    rationale="Η διαδρομή προς H μέσω G (κόστος 10) είναι πολύ συντομότερη από τη διαδρομή μέσω B (κόστος 19).",
                ),
            ],
            detailed_justification=(
                "Πλήρης πίνακας εκτέλεσης αλγορίθμου Dijkstra:\n\n"
                "| Βήμα | N | A | B | C | D | E | F | G | H |\n"
                "|---|---|---|---|---|---|---|---|---|---|\n"
                "| 1 | E | inf | inf | **3(E)** | **3(E)** | 0 | **3(E)** | inf | inf |\n"
                "| 2 | EC | **4(C)** | 7(C) | 3 | 3 | 0 | 3 | inf | inf |\n"
                "| 3 | ECD | 4 | **5(D)** | 3 | 3 | 0 | 3 | 8(D) | inf |\n"
                "| 4 | ECDF | 4 | 5 | 3 | 3 | 0 | 3 | 8(D) | inf |\n"
                "| 5 | ECDFA | 4 | 5 | 3 | 3 | 0 | 3 | 8(D) | inf |\n"
                "| 6 | ECDFAB | 4 | 5 | 3 | 3 | 0 | 3 | 8(D) | 19(B) |\n"
                "| 7 | ECDFABG | 4 | 5 | 3 | 3 | 0 | 3 | 8(D) | **10(G)** |\n"
                "| 8 | ECDFABGH | 4 | 5 | 3 | 3 | 0 | 3 | 8 | 10 |\n\n"
                "**Συντομότερα Μονοπάτια από E:**\n"
                "- Προς **C**: $E \\rightarrow C$ (Κόστος: 3)\n"
                "- Προς **D**: $E \\rightarrow D$ (Κόστος: 3)\n"
                "- Προς **F**: $E \\rightarrow F$ (Κόστος: 3)\n"
                "- Προς **A**: $E \\rightarrow C \\rightarrow A$ (Κόστος: 4)\n"
                "- Προς **B**: $E \\rightarrow D \\rightarrow B$ (Κόστος: 5)\n"
                "- Προς **G**: $E \\rightarrow D \\rightarrow G$ (Κόστος: 8)\n"
                "- Προς **H**: $E \\rightarrow D \\rightarrow G \\rightarrow H$ (Κόστος: 10)"
            ),
        ),
        # Part 2 - 2η Άσκηση B
        ExamQuestion(
            question_number=8,
            title="2η Άσκηση (B): Ελάχιστο Μέγεθος Πλαισίου CSMA/CD στα 15 Mbps",
            question_type="Calculations",
            prompt_text=(
                "Ένα δίκτυο χρησιμοποιεί CSMA/CD και έχει bandwidth R = 15 Mbps. "
                "Αν ο μέγιστος χρόνος διάδοσης είναι t_prop = 25.6 μs, ποιο είναι το ελάχιστο μέγεθος του πλαισίου σε Bytes;"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Εφαρμογή Κριτηρίου L_min",
                    formula="L_min >= 2 * t_prop * R",
                    substitution="2 * (25.6 * 10^-6 s) * (15 * 10^6 bps)",
                    result="768 bits",
                    rationale="Ο πομπός πρέπει να εκπέμπει για τουλάχιστον ένα RTT.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Μετατροπή σε Bytes",
                    formula="L_min (Bytes) = 768 / 8",
                    substitution="768 / 8",
                    result="96 Bytes",
                    rationale="Στα 15 Mbps το ελάχιστο πλαίσιο είναι 96 Bytes.",
                ),
            ],
            detailed_justification="$$L_{\\text{min}} = 2 \\times (25,6 \\times 10^{-6}\\text{ s}) \\times (15 \\times 10^6\\text{ bps}) = 768\\text{ bits} = 96\\text{ Bytes}$$",
        ),
        # Part 2 - 3η Άσκηση Bonus
        ExamQuestion(
            question_number=9,
            title="3η Άσκηση (Bonus): Κατασκευή Κώδικα Hamming με Περιττή Ισοτιμία",
            question_type="Calculations",
            prompt_text=(
                "Αποστολέας στέλνει το μήνυμα δεδομένων `10001011` εφαρμόζοντας τον κώδικα Hamming. "
                "Ποιο είναι το μήνυμα που θα μεταδοθεί; Υποθέστε χρήση περιττής ισοτιμίας (Odd Parity)."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Εύρεση Αριθμού Bits Ισοτιμίας p",
                    formula="2^p >= d + p + 1",
                    substitution="d = 8 bits -> 2^p >= 8 + p + 1",
                    result="p = 4 bits (γιατί 2^4 = 16 >= 13)",
                    rationale="Συνολικό μήκος κωδικολέξης n = 8 + 4 = 12 bits. Θέσεις ισοτιμίας: 1, 2, 4, 8.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Τοποθέτηση Δεδομένων στις Θέσεις",
                    formula="Θέσεις: 1(P1), 2(P2), 3(D1), 4(P4), 5(D2), 6(D3), 7(D4), 8(P8), 9(D5), 10(D6), 11(D7), 12(D8)",
                    substitution="D = 1 0 0 0 1 0 1 1",
                    result="D1=1, D2=0, D3=0, D4=0, D5=1, D6=0, D7=1, D8=1",
                    rationale="Τα bits δεδομένων καταλαμβάνουν όλες τις μη δυνάμεις του 2 θέσεις.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Υπολογισμός Bits Ισοτιμίας (Odd Parity / Περιττός αριθμός 1)",
                    formula="P1(1,3,5,7,9,11), P2(2,3,6,7,10,11), P4(4,5,6,7,12), P8(8,9,10,11,12)",
                    substitution="P1 XOR (1,0,0,1,1)=0 -> P1=0 | P2 XOR (1,0,0,0,1)=1 -> P2=1 | P4 XOR (0,0,0,1)=1 -> P4=0 | P8 XOR (1,0,1,1)=1 -> P8=0",
                    result="P1=0, P2=1, P4=0, P8=0",
                    rationale="Κάθε ομάδα ισοτιμίας πρέπει να περιέχει περιττό αριθμό άσων.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Τελικό Μεταδιδόμενο Μήνυμα",
                    formula="[P1, P2, D1, P4, D2, D3, D4, P8, D5, D6, D7, D8]",
                    substitution="0 1 1 0 0 0 0 0 1 0 1 1",
                    result="011000001011",
                    rationale="Η τελική κωδικολέξη 12 bits.",
                ),
            ],
            detailed_justification=(
                "Πίνακας θέσεων bits κώδικα Hamming(12,8):\n\n"
                "| Θέση | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |\n"
                "|---|---|---|---|---|---|---|---|---|---|---|---|---|\n"
                "| Bit | **P1** | **P2** | D1 | **P4** | D2 | D3 | D4 | **P8** | D5 | D6 | D7 | D8 |\n"
                "| Τιμή | `0` | `1` | `1` | `0` | `0` | `0` | `0` | `0` | `1` | `0` | `1` | `1` |\n\n"
                "- P1 καλύπτει 1, 3, 5, 7, 9, 11: bits = P1, 1, 0, 0, 1, 1 (3 άσοι). Για περιττό: **P1 = 0**.\n"
                "- P2 καλύπτει 2, 3, 6, 7, 10, 11: bits = P2, 1, 0, 0, 0, 1 (2 άσοι). Για περιττό: **P2 = 1**.\n"
                "- P4 καλύπτει 4, 5, 6, 7, 12: bits = P4, 0, 0, 0, 1 (1 άσος). Για περιττό: **P4 = 0**.\n"
                "- P8 καλύπτει 8, 9, 10, 11, 12: bits = P8, 1, 0, 1, 1 (3 άσοι). Για περιττό: **P8 = 0**.\n\n"
                "Τελικό μήνυμα: **`011000001011`**."
            ),
        ),
    ]

    nodes = [
        TopologyNode("node_a", "Node A", "host", 100, 150, "10.0.1.1", "00:11:22:33:44:01"),
        TopologyNode("node_b", "Router B (OSPF)", "router", 380, 150, "10.0.1.2", "00:11:22:33:44:02"),
        TopologyNode("node_c", "Node C", "host", 660, 150, "10.0.2.1", "00:11:22:33:44:03"),
    ]

    links = [
        TopologyLink("node_a", "node_b", 12, 10.0, 2.5, "fiber", "12k | 10km"),
        TopologyLink("node_b", "node_c", 15, 50.0, 2.5, "fiber", "15k | 50km"),
    ]

    return NetworkScenario(
        id="exam_past_archive",
        title="Θέματα Εξετάσεων (Comprehensive Archive)",
        subtitle="4 Delays, BDP, OSPF (4 Subnets), Sliding Window, BGP, Dijkstra, CSMA/CD & Hamming",
        course_tag="Past Exam",
        duration_info="2 ώρες και 15 λεπτά",
        paragraphs=paragraphs,
        questions=questions,
        nodes=nodes,
        links=links,
        methodology_summary=[
            "1. d_nodal = d_proc + d_queue + d_trans + d_prop.",
            "2. BDP = Bandwidth * Delay = 8 * AM * Delay bits.",
            "3. OSPF Single Area: 255.255.255.255 - Mask = Wildcard mask.",
            "4. TCP Bits in Flight = R * d_prop (5000 bits).",
            "5. Dijkstra Link-State: Εύρεση ελάχιστων αποστάσεων από ρίζα E.",
            "6. CSMA/CD 15M: L_min = 2 * d_prop * R = 768 bits = 96 Bytes.",
            "7. Hamming(12,8) Odd Parity: 2^p >= d + p + 1 (p = 4 bits).",
        ],
        calculator_type="delay",
    )
