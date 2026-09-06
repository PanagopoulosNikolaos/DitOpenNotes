"""Past Exam 2026 Team Edition Scenario Module.

Contains 1-to-1 representation of all exam questions from the 2026 Team Edition paper:
- Part 1: End-to-End Delay Derivation, AM-based Bandwidth-Delay Product (BDP), Cisco OSPF configuration.
- Part 2: Google BBR (RTT samples, traceroute, CWND calculation), BGP Autonomous System Routing,
  Multi-hop 2-link store-and-forward delay and RTT (A-B, A-C with processing delay).
- Part 3: 12-Node Dijkstra Shortest Path execution table (a to k), CSMA/CD Minimum Frame Size (64 Bytes).
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
        NetworkScenario: The structured scenario object with 1-to-1 parity.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Το εξεταστικό δοκίμιο "),
                TextSegment(
                    text="Δίκτυα Υπολογιστών 2026 (Team Edition)",
                    is_highlight=True,
                    category="protocol",
                    tag_label="ΕΞΕΤΑΣΗ 2026",
                    tooltip="Προχωρημένα θέματα αρχιτεκτονικής, δρομολόγησης και αλγορίθμων δικτύων",
                ),
                TextSegment(text=" εστιάζει στη θεωρητική και υπολογιστική ανάλυση "),
                TextSegment(
                    text="Καθυστέρησης από Άκρο σε Άκρο (End-to-End Delay)",
                    is_highlight=True,
                    category="delay",
                    tag_label="DELAYS",
                    tooltip="Μαθηματικό μοντέλο χρόνου μετάδοσης και διάδοσης",
                ),
                TextSegment(text=", στον υπολογισμό του "),
                TextSegment(
                    text="Bandwidth-Delay Product (BDP = R * Delay)",
                    is_highlight=True,
                    category="delay",
                    tag_label="BDP",
                    tooltip="Μέγιστη χωρητικότητα bits εν πτήσει (in flight) στο κανάλι",
                ),
                TextSegment(text=" και στην εφαρμογή του σύγχρονου αλγορίθμου συμφόρησης "),
                TextSegment(
                    text="Google BBR (CWND = RtProp * BtlBw)",
                    is_highlight=True,
                    category="protocol",
                    tag_label="BBR",
                    tooltip="Έλεγχος συμφόρησης βάσει ελάχιστου RTT και μέγιστου ρυθμού",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="#e06b3a",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Στο δεύτερο μέρος εξετάζονται πολιτικές δρομολόγησης μεταξύ "),
                TextSegment(
                    text="Αυτόνομων Συστημάτων (BGP Hot-Potato Routing)",
                    is_highlight=True,
                    category="routing",
                    tag_label="BGP AS",
                    tooltip="Δρομολόγηση μεταξύ Verizon και AT&T",
                ),
                TextSegment(text=", η διαμόρφωση του πρωτοκόλλου "),
                TextSegment(
                    text="OSPF σε Cisco IOS",
                    is_highlight=True,
                    category="routing",
                    tag_label="OSPF L3",
                    tooltip="Link-State εσωτερική δρομολόγηση με wildcard masks",
                ),
                TextSegment(text=", η εκτέλεση του αλγορίθμου "),
                TextSegment(
                    text="Dijkstra Shortest Path σε Γράφο 12 Κόμβων",
                    is_highlight=True,
                    category="routing",
                    tag_label="DIJKSTRA 12",
                    tooltip="Εύρεση βέλτιστης διαδρομής από κόμβο a σε κόμβο k",
                ),
                TextSegment(text=" και ο υπολογισμός του "),
                TextSegment(
                    text="Ελάχιστου Μεγέθους Πλαισίου CSMA/CD (L_min = 2 * d_prop * R)",
                    is_highlight=True,
                    category="error_check",
                    tag_label="CSMA/CD L_MIN",
                    tooltip="Αποφυγή μη ανιχνεύσιμων συγκρούσεων στο Ethernet (64 Bytes)",
                ),
                TextSegment(text="."),
            ]
        ),
    ]

    questions = [
        # Part 1 - Question 1
        ExamQuestion(
            question_number=1,
            title="Μαθηματικός Ορισμός Καθυστέρησης από Άκρο σε Άκρο",
            question_type="Calculations",
            prompt_text=(
                "Έστω το δίκτυο της Εικόνας 1: `(A)====[Packet]====(B)`\n"
                "Ορίστε αναλυτικά την καθυστέρηση από άκρο σε άκρο (end-to-end delay), ως μαθηματική έκφραση και "
                "εξηγήστε τα σύμβολα που θα συμπεριλάβετε σε αυτή. Υποθέτουμε ότι το μέγεθος του πακέτου είναι L, "
                "ο ρυθμός μετάδοσης R, η απόσταση l και η ταχύτητα διάδοσης u. Σημειώστε τυχόν άλλες παραδοχές."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Καθυστέρηση Μετάδοσης (Transmission Delay)",
                    formula="d_trans = L / R",
                    substitution="L bits / R bps",
                    result="L / R (sec)",
                    rationale="Ο χρόνος που απαιτείται για να διοχετευτούν όλα τα bits του πακέτου πάνω στο φυσικό μέσο από τον πομπό.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Καθυστέρηση Διάδοσης (Propagation Delay)",
                    formula="d_prop = l / u",
                    substitution="l meters / u (m/s)",
                    result="l / u (sec)",
                    rationale="Ο χρόνος που χρειάζεται ένα bit για να ταξιδέψει τη φυσική απόσταση l με ταχύτητα διάδοσης u.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Συνολική Καθυστέρηση Ζεύξης",
                    formula="d_total = d_trans + d_prop",
                    substitution="(L / R) + (l / u)",
                    result="(L / R) + (l / u) (sec)",
                    rationale="Σε μία απλή απευθείας ζεύξη χωρίς ενδιάμεσο δρομολογητή, το άθροισμα των δύο συνιστωσών δίνει τον συνολικό χρόνο άφιξης.",
                ),
            ],
            detailed_justification=(
                "Γενικό μοντέλο κομβικής καθυστέρησης:\n"
                "$$d_{end-to-end} = d_{proc} + d_{queue} + d_{trans} + d_{prop}$$\n\n"
                "**Παραδοχές:**\n"
                "- $d_{proc}$ (Καθυστέρηση επεξεργασίας): Χρόνος ελέγχου σφαλμάτων και επικεφαλίδας στον κόμβο Α (αν αγνοηθεί = 0).\n"
                "- $d_{queue}$ (Καθυστέρηση ουράς): Χρόνος αναμονής σε ουρά εξόδου (αν δεν υπάρχει κίνηση = 0).\n"
                "- $d_{trans} = \\frac{L}{R}$: Εξαρτάται αποκλειστικά από το μέγεθος πακέτου $L$ και το bandwidth $R$.\n"
                "- $d_{prop} = \\frac{l}{u}$: Εξαρτάται αποκλειστικά από το μήκος $l$ και το φυσικό μέσο $u$ (συνήθως $2 \\times 10^8$ m/s σε καλώδιο/ίνα)."
            ),
        ),
        # Part 1 - Question 2
        ExamQuestion(
            question_number=2,
            title="Υπολογισμός Bandwidth-Delay Product (BDP) με Παραμέτρους ΑΜ",
            question_type="Calculations",
            prompt_text=(
                "Έστω ζεύξη δικτύου με χαρακτηριστικά Bandwidth και Delay. Ποιος είναι ο μέγιστος αριθμός bits που "
                "μπορούν να μεταφέρονται σε αυτή τη ζεύξη σε κάθε χρονική στιγμή (bits in flight), αν υποθέσουμε ότι "
                "το Bandwidth είναι ίσο με τον ΑΜ σας σε KB και το Delay είναι ίσο με το τελευταίο ψηφίο του ΑΜ σας σε ms; "
                "(Αν το τελευταίο ψηφίο είναι 0, θεωρείστε Delay = 6 ms). Εφαρμόστε αναλυτικά για ΑΜ = 3323."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Μαθηματικός Τύπος BDP",
                    formula="BDP = Bandwidth * Delay",
                    substitution="(AM * 1000 * 8 bps) * (Delay_ms * 10^-3 s)",
                    result="8 * AM * Delay_ms (bits)",
                    rationale="Μετατροπή KB σε bits/sec (1 KB = 1000 Bytes = 8000 bits) και ms σε seconds (10^-3 s).",
                ),
                CalculationStep(
                    step_number=2,
                    title="Αριθμητική Εφαρμογή για AM = 3323 (Τελευταίο Ψηφίο d = 3)",
                    formula="Max_Bits = (3323 * 8000) * (3 * 10^-3)",
                    substitution="26,584,000 bps * 0.003 s",
                    result="79,752 bits",
                    rationale="Σε κάθε δεδομένη χρονική στιγμή, ακριβώς 79.752 bits βρίσκονται μέσα στο κανάλι εν πτήσει.",
                ),
            ],
            detailed_justification=(
                "Το γινόμενο εύρους ζώνης-καθυστέρησης (Bandwidth-Delay Product - BDP) αντιπροσωπεύει τη μέγιστη χωρητικότητα του αγωγού επικοινωνίας σε bits. "
                "Αν χρησιμοποιηθεί η δυαδική προσέγγιση ($1\\text{ KB} = 1024\\text{ Bytes}$):\n"
                "$$R = 3323 \\times 1024 \\times 8 = 27.222.016\\text{ bps}$$\n"
                "$$\\text{Max Bits} = 27.222.016 \\times 0,003 = 81.666\\text{ bits}$$\n"
                "Στην εξέταση γίνεται δεκτή και η δεκαδική προσέγγιση ($8 \\times N \\times d = 79.752\\text{ bits}$)."
            ),
        ),
        # Part 1 - Question 3
        ExamQuestion(
            question_number=3,
            title="Διαμόρφωση Δρομολόγησης OSPF σε Cisco IOS",
            question_type="Calculations",
            prompt_text=(
                "Για το δίκτυο της Εικόνας ορίστε δρομολόγηση OSPF υποθέτοντας μία περιοχή (Area 0):\n"
                "```text\n"
                "        172.16.8.0/29\n"
                "              |\n"
                " 10.10.10.0/30-O-\n"
                "              |\n"
                "        192.168.1.0/24\n"
                "```\n"
                "Συμπληρώστε τα κενά της γραμμής εντολών Cisco CLI."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Υπολογισμός Wildcard Masks",
                    formula="Wildcard = 255.255.255.255 - Subnet_Mask",
                    substitution="/30: 255.255.255.252 -> 0.0.0.3 | /29: 255.255.255.248 -> 0.0.0.7 | /24: 255.255.255.0 -> 0.0.0.255",
                    result="0.0.0.3, 0.0.0.7, 0.0.0.255",
                    rationale="Το OSPF στο Cisco IOS απαιτεί wildcard μάσκες αντί για τις κλασικές μάσκες υποδικτύου.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Εντολές Διαμόρφωσης Cisco CLI",
                    formula="router ospf <process_id>  &&  network <net> <wildcard> area <area_id>",
                    substitution="router ospf 1 -> network 10.10.10.0 0.0.0.3 area 0 -> network 172.16.8.0 0.0.0.7 area 0 -> network 192.168.1.0 0.0.0.255 area 0",
                    result="Ενεργοποίηση Single Area OSPF",
                    rationale="Διαφημίζει τα τρία συνδεδεμένα δίκτυα στην ενιαία κεντρική περιοχή Area 0 (Backbone).",
                ),
            ],
            detailed_justification=(
                "Πλήρης ακολουθία εντολών:\n"
                "```text\n"
                "R>en\n"
                "R# configure terminal\n"
                "R(config)# router ospf 1\n"
                "R(config-router)# network 10.10.10.0 0.0.0.3 area 0\n"
                "R(config-router)# network 172.16.8.0 0.0.0.7 area 0\n"
                "R(config-router)# network 192.168.1.0 0.0.0.255 area 0\n"
                "R(config-router)# end\n"
                "```"
            ),
        ),
        # Part 2 - Question 4
        ExamQuestion(
            question_number=4,
            title="Αλγόριθμος Ελέγχου Συμφόρησης Google BBR",
            question_type="Calculations",
            prompt_text=(
                "Το πρωτόκολλο Google BBR θέτει CWND = RtProp * BtlBw, όπου RtProp = min(RTTt).\n"
                "**a.** Πώς λαμβάνονται δείγματα RTT και πώς υπολογίζεται το RtProp;\n"
                "**b.** Με ποιο τρόπο παρακολουθείτε τη διαδρομή των πακέτων προς τον server;\n"
                "**c.** Έστω σύνδεσμος με RtProp = 5 ms και ρυθμό BtlBw = 0,125 GB/s. Υπολογίστε το CWND."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Υπολογισμός Παραθύρου Συμφόρησης BBR (CWND)",
                    formula="CWND = RtProp * BtlBw",
                    substitution="5 ms = 0.005 s | 0.125 GB/s = 0.125 * 10^9 Bytes/s = 125,000,000 Bytes/s",
                    result="CWND = 0.005 * 125,000,000 = 625,000 Bytes = 625 KB",
                    rationale="Το παράθυρο συμφόρησης στο BBR ταυτίζεται με το φυσικό Bandwidth-Delay Product χωρίς περιττό bufferbloat.",
                ),
            ],
            detailed_justification=(
                "**a. Λήψη δειγμάτων RTT και υπολογισμός RtProp:**\n"
                "- Το TCP μετράει το SampleRTT μεταξύ αποστολής τμήματος και λήψης του ACK (κανόνας Karn ή TCP Timestamps Option - RFC 7323).\n"
                "- Το BBR διατηρεί κινούμενο ελάχιστο παράθυρο (rolling minimum window): $RtProp = \\min_{t \\in W}(SampleRTT_t)$ ώστε να αντικατοπτρίζει την πραγματική φυσική καθυστέρηση διάδοσης χωρίς καθυστέρηση ουράς.\n\n"
                "**b. Παρακολούθηση διαδρομής:**\n"
                "- Χρησιμοποιείται το εργαλείο **traceroute** (ή **tracert** στα Windows). Αποστέλλει πακέτα με σταδιακά αυξανόμενο TTL ($1, 2, 3, \\dots$). Όταν ένας ενδιάμεσος δρομολογητής μηδενίσει το TTL, απορρίπτει το πακέτο και επιστρέφει ICMP Time Exceeded μήνυμα, αποκαλύπτοντας την IP του.\n\n"
                "**c. Υπολογισμός CWND:**\n"
                "- $CWND = 0,005\\text{ s} \\times 125.000.000\\text{ Bytes/s} = 625.000\\text{ Bytes} = 625\\text{ KB}$ (ή $5.000.000\\text{ bits}$)."
            ),
        ),
        # Part 2 - Question 5
        ExamQuestion(
            question_number=5,
            title="Δρομολόγηση BGP μεταξύ Αυτόνομων Συστημάτων (Verizon & AT&T)",
            question_type="Theory Analysis",
            prompt_text=(
                "Έστω τα δίκτυα των Εικόνων 3 και 4 όπου ο κόμβος X στέλνει πακέτα στον Y. "
                "Ποια διαδρομή θα ακολουθήσουν τα πακέτα στην κάθε περίπτωση και γιατί, "
                "χρησιμοποιώντας το πρωτόκολλο BGP μεταξύ Verizon AS και AT&T AS;"
            ),
            detailed_justification=(
                "Στο BGP εφαρμόζεται η τακτική **δρομολόγησης 'καυτής πατάτας' (hot-potato routing)**. "
                "Κάθε Αυτόνομο Σύστημα επιδιώκει να απομακρύνει το πακέτο εκτός των ορίων του χρησιμοποιώντας την πλησιέστερη πύλη εξόδου (egress router) βάσει του εσωτερικού κόστους IGP.\n\n"
                "**Εικόνα 3:**\n"
                "- Η AT&T διαθέτει δύο εξόδους προς Verizon: την F (αριστερά) και την I (δεξιά).\n"
                "- Απόσταση από X: προς F είναι 2 hops ($X \\rightarrow E \\rightarrow F$), ενώ προς I είναι 5 hops.\n"
                "- Η AT&T επιλέγει την έξοδο F (Hot-Potato). Η Verizon αναλαμβάνει την εσωτερική προώθηση.\n"
                "- **Διαδρομή:** `X -> E -> F -> A -> B -> C -> D -> Y`.\n\n"
                "**Εικόνα 4:**\n"
                "- Η AT&T διαθέτει δύο εξόδους: F (σύνδεση με A) και J (σύνδεση με E).\n"
                "- Από τον X (μέσω H), η απόσταση προς F είναι 2 hops ($H \\rightarrow G \\rightarrow F$) και προς J είναι 2 hops ($H \\rightarrow I \\rightarrow J$).\n"
                "- Υπάρχει ισοπαλία στο IGP κόστος. Βάσει BGP κανόνων (π.χ. χαμηλότερο BGP Router ID ή συνολικό μήκος), η επιλογή της εξόδου J δίνει συντομότερη συνολική διαδρομή 5 hops (`X -> H -> I -> J -> E -> Y`) έναντι 9 hops μέσω F."
            ),
        ),
        # Part 2 - 1η Άσκηση
        ExamQuestion(
            question_number=6,
            title="1η Άσκηση: Υπολογισμός Χρόνου Αποστολής & RTT σε 2 Ζεύξεις (A-B-C)",
            question_type="Calculations",
            prompt_text=(
                "Έστω ζεύξεις: `(A)---Link 1---(B)---Link 2---(C)`.\n"
                "Link 1: R1 = 10000 bps, L1 = 100 km, u1 = 2.5*10^8 m/s.\n"
                "Link 2: R2 = 10000 bps, L2 = 50 km, u2 = 2.5*10^8 m/s.\n"
                "Μέγεθος πακέτου P = 1/2 AM (θεωρείστε παράδειγμα P = 8000 bits / 1000 Bytes).\n"
                "**A.** Χρόνος αποστολής ενός πακέτου από το A στο C.\n"
                "**B.** RTT πακέτου A -> B -> A (αγνοώντας d_proc).\n"
                "**C.** RTT πακέτου A -> C -> A με d_proc = 0.02 ms σε κάθε κόμβο."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Καθυστερήσεις Μετάδοσης και Διάδοσης ανά Ζεύξη",
                    formula="d_trans = P / R  &&  d_prop = L / u",
                    substitution="d_trans1 = d_trans2 = 8000 / 10000 = 0.8 s | d_prop1 = 100,000 / 2.5*10^8 = 0.4 ms | d_prop2 = 50,000 / 2.5*10^8 = 0.2 ms",
                    result="d_trans = 0.8 s | d_prop1 = 0.4 ms | d_prop2 = 0.2 ms",
                    rationale="Μετάδοση Store-and-Forward σε κάθε hop και φυσικός χρόνος διάδοσης φωτεινού παλμού.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ερώτημα A: Χρόνος Αποστολής A -> C",
                    formula="t_total = d_trans1 + d_prop1 + d_trans2 + d_prop2",
                    substitution="0.8 + 0.0004 + 0.8 + 0.0002",
                    result="1.6006 s (ή 2*10^-4 * P + 0.0006 s)",
                    rationale="Το πακέτο μεταδίδεται πλήρως στο A, διαδίδεται στο B, επαναμεταδίδεται πλήρως στο B και διαδίδεται στο C.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Ερώτημα B: RTT A -> B -> A (χωρίς d_proc)",
                    formula="RTT_AB = 2 * d_trans1 + 2 * d_prop1",
                    substitution="2 * 0.8 + 2 * 0.0004",
                    result="1.6008 s (ή 2*10^-4 * P + 0.0008 s)",
                    rationale="Αποστολή A->B και άμεση επιστροφή B->A.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Ερώτημα C: RTT A -> C -> A με d_proc = 0.02 ms",
                    formula="RTT_AC = 4 * d_trans + 2 * (d_prop1 + d_prop2) + 3 * d_proc",
                    substitution="4 * 0.8 + 2 * 0.0006 + 3 * 0.00002",
                    result="3.20126 s (ή 4*10^-4 * P + 0.00126 s)",
                    rationale="4 μεταδόσεις, 4 διαδόσεις και 3 καθυστερήσεις επεξεργασίας (στο B κατά τη μετάβαση, στο C κατά την επιστροφή και στο B κατά την επιστροφή).",
                ),
            ],
            detailed_justification=(
                "Αναλυτικοί τύποι συναρτήσει του μεγέθους πακέτου $P$ (σε bits):\n"
                "- **A:** $t_{total} = \\frac{P}{10000} + 0,0004 + \\frac{P}{10000} + 0,0002 = 2 \\times 10^{-4} P + 0,0006\\text{ s}$.\n"
                "- **B:** \\text{RTT}_{A-B} = 2 \\times \\frac{P}{10000} + 2 \\times 0,0004 = 2 \\times 10^{-4} P + 0,0008\\text{ s}.\n"
                "- **C:** \\text{RTT}_{A-C} = 4 \\times \\frac{P}{10000} + 2 \\times (0,0004 + 0,0002) + 3 \\times (0,00002) = 4 \\times 10^{-4} P + 0,00126\\text{ s}."
            ),
        ),
        # Part 3 - 2η Άσκηση A
        ExamQuestion(
            question_number=7,
            title="2η Άσκηση (A): Αλγόριθμος Dijkstra σε Γράφο 12 Κόμβων (a -> k)",
            question_type="Algorithm Step",
            prompt_text=(
                "Εφαρμόστε τον αλγόριθμο Link-State Dijkstra στον γράφο 12 κόμβων και υπολογίστε "
                "το συντομότερο μονοπάτι από τον κόμβο **a** στον κόμβο **k**.\n"
                "Γράφος: a, b, c, d, e, f, h, i, j, k, l, m με κόστη ζεύξεων:\n"
                "a-b:2, a-e:1, a-c:5, e-f:1, f-b:2, f-c:3, b-c:3, c-d:1, c-h:2, c-i:5, h-i:2, h-m:1, h-d:2, d-m:1, m-i:3, m-l:1, i-j:3, i-l:2, j-k:5, j-l:1, l-k:1."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Βήμα 1: Εκκίνηση από Κόμβο a",
                    formula="D(e)=1(a), D(b)=2(a), D(c)=5(a), άλλοι=inf",
                    substitution="Ελάχιστος κόμβος: e με κόστος 1",
                    result="N = {a, e}",
                    rationale="Ο κόμβος e μονιμοποιείται πρώτος με κόστος 1.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Βήμα 2: Επέκταση μέσω e",
                    formula="D(f) = D(e) + c(e,f) = 1 + 1 = 2(e)",
                    substitution="Υποψήφιοι: b: 2(a), f: 2(e), c: 5(a)",
                    result="N = {a, e, b, f}",
                    rationale="Ισοπαλία κόστους 2. Μονιμοποιούνται οι b και f.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Βήμα 3: Επέκταση μέσω f και b προς c και d",
                    formula="D(c) = min(5(a), D(b)+3, D(f)+3) = 5",
                    substitution="D(d) = D(f) + c(f,d) = 2 + 1 = 3(f)",
                    result="N = {a, e, b, f, d}",
                    rationale="Μονιμοποιείται ο d με κόστος 3.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Τελική Βέλτιστη Διαδρομή προς k",
                    formula="Path: a -> e -> f -> d -> m -> l -> k",
                    substitution="c(a,e)=1 + c(e,f)=1 + c(f,d)=1 + c(d,m)=1 + c(m,l)=1 + c(l,k)=1",
                    result="Συντομότερο Μονοπάτι: a -> e -> f -> d -> m -> l -> k (Κόστος = 6)",
                    rationale="Χρησιμοποιώντας τις ακμές κόστους 1 στην κάτω αρτηρία, επιτυγχάνεται το ελάχιστο συνολικό κόστος 6.",
                ),
            ],
            detailed_justification=(
                "Πλήρης πίνακας εκτέλεσης αλγορίθμου Dijkstra (12 Κόμβοι):\n\n"
                "| Βήμα | Μόνιμοι Κόμβοι (N) | D(b) | D(c) | D(d) | D(e) | D(f) | D(h) | D(i) | D(j) | D(k) | D(l) | D(m) |\n"
                "|---|---|---|---|---|---|---|---|---|---|---|---|---|\n"
                "| 0 | a | 2(a) | 5(a) | inf | **1(a)** | inf | inf | inf | inf | inf | inf | inf |\n"
                "| 1 | a, e | **2(a)** | 5(a) | inf | 1 | 2(e) | inf | inf | inf | inf | inf | inf |\n"
                "| 2 | a, e, b | 2 | 5(a) | inf | 1 | **2(e)** | inf | inf | inf | inf | inf | inf |\n"
                "| 3 | a, e, b, f | 2 | 5(a) | **3(f)** | 1 | 2 | inf | inf | inf | inf | inf | inf |\n"
                "| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |\n"
                "| Τελικό | a, e, f, d, m, l, k | 2 | 5 | 3 | 1 | 2 | 5(c) | 6(l) | 6(l) | **6(l)** | 5(m) | 4(d) |\n\n"
                "**Συντομότερη Διαδρομή:** `a -> e -> f -> d -> m -> l -> k` με συνολικό κόστος **6**."
            ),
        ),
        # Part 3 - 2η Άσκηση B
        ExamQuestion(
            question_number=8,
            title="2η Άσκηση (B): Ελάχιστο Μέγεθος Πλαισίου CSMA/CD",
            question_type="Calculations",
            prompt_text=(
                "Ένα δίκτυο χρησιμοποιεί CSMA/CD και έχει bandwidth R = 10 Mbps. "
                "Αν ο μέγιστος χρόνος διάδοσης (συμπεριλαμβανομένων καθυστερήσεων) είναι d_prop = 25.6 μs, "
                "ποιο είναι το ελάχιστο μέγεθος του πλαισίου (L_min) σε bits και σε Bytes;"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Κριτήριο Ανίχνευσης Σύγκρουσης CSMA/CD",
                    formula="d_trans >= 2 * d_prop  <=>  (L_min / R) >= 2 * d_prop",
                    substitution="L_min = 2 * d_prop * R",
                    result="L_min = 2 * (25.6 * 10^-6 s) * (10 * 10^6 bps)",
                    rationale="Ο πομπός πρέπει να συνεχίζει τη μετάδοση τουλάχιστον για ένα RTT (2*d_prop) ώστε να ανιχνεύσει σύγκρουση στο χειρότερο σενάριο απόστασης.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Τελικός Υπολογισμός σε Bits και Bytes",
                    formula="L_min = 51.2 * 10 = 512 bits",
                    substitution="512 bits / 8 bits per byte",
                    result="64 Bytes",
                    rationale="Αυτός είναι ο ακριβής λόγος που το κλασικό Ethernet IEEE 802.3 έχει ελάχιστο μέγεθος πλαισίου 64 Bytes.",
                ),
            ],
            detailed_justification=(
                "Αν το πλαίσιο ήταν μικρότερο από 64 Bytes (512 bits), η εκπομπή θα ολοκληρωνόταν πριν επιστρέψει το σήμα σύγκρουσης "
                "(JAM signal) από το πιο απομακρυσμένο άκρο του καλωδίου, οδηγώντας σε μη ανιχνεύσιμη απώλεια δεδομένων."
            ),
            common_pitfalls=[
                "Παράλειψη του συντελεστή 2 (RTT = 2 * d_prop).",
                "Μη μετατροπή των 512 bits σε 64 Bytes.",
            ],
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
        subtitle="End-to-End Delays, BDP, Google BBR CWND, OSPF, BGP AS, 12-Node Dijkstra & CSMA/CD",
        course_tag="Past Exam",
        duration_info="2 ώρες και 15 λεπτά",
        paragraphs=paragraphs,
        questions=questions,
        nodes=nodes,
        links=links,
        methodology_summary=[
            "1. d_total = (L/R) + (l/u) για 1 ζεύξη.",
            "2. BDP = Bandwidth * Delay = 8 * AM * Delay bits.",
            "3. Google BBR: CWND = RtProp * BtlBw (Bandwidth-Delay Product).",
            "4. OSPF: Single Area 0 με wildcard masks (255.255.255.255 - Mask).",
            "5. BGP Hot-Potato Routing: Επιλογή πλησιέστερης εξόδου βάσει εσωτερικού IGP κόστους.",
            "6. CSMA/CD: L_min = 2 * d_prop * R = 512 bits = 64 Bytes.",
        ],
        calculator_type="delay",
    )
