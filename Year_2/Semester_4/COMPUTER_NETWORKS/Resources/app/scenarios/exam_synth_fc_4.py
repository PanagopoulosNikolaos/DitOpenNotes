"""Synthetic Full Coverage Exam 4 Scenario Module.

Contains 1-to-1 representation of all exam questions from Synthetic Exam 4 (Full Coverage):
- Part A: P2P architecture, Transmission delay formula (d_trans = L/R), Subnet matching (/26),
  Traceroute TTL mechanism, True/False (Pipelining effect, OSPF Dijkstra, Data Centers).
- Part B: Exercise 1 (Dijkstra algorithm from root node A across 7 nodes), Exercise 2 (TCP Timeout calculation
  and TCP Sliding Window BDP sizing = 2 MB), Exercise 3 (Pipelined packet switching delay for 100 packets across 2 hops).
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
    """Constructs and returns Synthetic Full Coverage Exam 4 scenario.

    Returns:
        NetworkScenario: The structured scenario object with 1-to-1 parity.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Το διαγώνισμα πλήρους κάλυψης "),
                TextSegment(
                    text="Synthetic Exam 4 (Full Coverage)",
                    is_highlight=True,
                    category="protocol",
                    tag_label="FULL COVERAGE 4",
                    tooltip="Διαγώνισμα συνολικής επανάληψης ύλης",
                ),
                TextSegment(text=" καλύπτει θεμελιώδεις αρχιτεκτονικές όπως τα "),
                TextSegment(
                    text="Peer-to-Peer (P2P) δίκτυα",
                    is_highlight=True,
                    category="protocol",
                    tag_label="P2P",
                    tooltip="Ισότιμοι κόμβοι ως client και server ταυτόχρονα",
                ),
                TextSegment(text=", τον τύπο της "),
                TextSegment(
                    text="Καθυστέρησης Μετάδοσης (d_trans = L/R)",
                    is_highlight=True,
                    category="delay",
                    tag_label="D_TRANS",
                    tooltip="Χρόνος ώθησης όλων των bits του πακέτου στη ζεύξη",
                ),
                TextSegment(text=", καθώς και την ανάλυση μασκών "),
                TextSegment(
                    text="CIDR /26 Subnetting",
                    is_highlight=True,
                    category="routing",
                    tag_label="/26 SUBNET",
                    tooltip="Μάσκα 255.255.255.192 και block size 64",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="#3182ce",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Στο υπολογιστικό μέρος περιλαμβάνονται: "),
                TextSegment(
                    text="Εκτέλεση Αλγορίθμου Dijkstra",
                    is_highlight=True,
                    category="routing",
                    tag_label="DIJKSTRA 7-NODES",
                    tooltip="Πίνακας καταστάσεων με ρίζα τον κόμβο A",
                ),
                TextSegment(text=", εκτίμηση "),
                TextSegment(
                    text="TCP Timeout & Παραθύρου BDP",
                    is_highlight=True,
                    category="protocol",
                    tag_label="TCP RTT / WINDOW",
                    tooltip="Υπολογισμός EstimatedRTT και buffer 2 MB",
                ),
                TextSegment(text=" και ανάλυση "),
                TextSegment(
                    text="Pipelining Effect 100 Πακέτων",
                    is_highlight=True,
                    category="delay",
                    tag_label="PIPELINING",
                    tooltip="Συνολικός χρόνος άφιξης σε 2 hops = 1.01 s",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="#805ad5",
        ),
    ]

    questions = [
        # Part A - Question 1
        ExamQuestion(
            question_number=1,
            title="Peer-to-Peer (P2P) Αρχιτεκτονική",
            question_type="Multiple Choice",
            prompt_text="Σε ένα καθαρό Peer-to-Peer (P2P) δίκτυο, ποιο από τα παρακάτω ισχύει;",
            options=[
                QuestionOption("A", "Η αξιοπιστία του δικτύου εξαρτάται αποκλειστικά από έναν κεντρικό Server (always-on).", False, "Αυτό είναι το μοντέλο Client-Server."),
                QuestionOption("B", "Η προσθήκη νέων χρηστών μειώνει πάντα το διαθέσιμο bandwidth.", False, "Στο P2P κάθε νέος χρήστης προσφέρει και χωρητικότητα εξυπηρέτησης."),
                QuestionOption("C", "Κάθε κόμβος (peer) λειτουργεί ταυτόχρονα ως client και ως server.", True, "Οι κόμβοι ανταλλάσσουν πόρους απευθείας, όντας ταυτόχρονα πελάτες και διακομιστές."),
                QuestionOption("D", "Είναι αδύνατη η κοινή χρήση αρχείων.", False, "Το P2P χρησιμοποιείται κατεξοχήν για file sharing."),
            ],
            correct_option_letter="C",
            detailed_justification=(
                "Στα P2P δίκτυα, οι κόμβοι (peers) είναι ισότιμοι και επικοινωνούν απευθείας μεταξύ τους. "
                "Κάθε κόμβος λειτουργεί ταυτόχρονα ως client (ζητά πόρους) και ως server (παρέχει πόρους), "
                "επιτρέποντας αυτο-κλιμάκωση (self-scalability)."
            ),
        ),
        # Part A - Question 2
        ExamQuestion(
            question_number=2,
            title="Τύπος Καθυστέρησης Μετάδοσης (Transmission Delay)",
            question_type="Multiple Choice",
            prompt_text="Η καθυστέρηση μετάδοσης (d_trans) ενός πακέτου μεγέθους L σε μια ζεύξη χωρητικότητας R υπολογίζεται ως:",
            options=[
                QuestionOption("A", "L / R", True, "Χρόνος ώθησης όλων των bits του πακέτου στο φυσικό μέσο."),
                QuestionOption("B", "R / L", False, "Αντίστροφο κλάσμα, εσφαλμένη διάσταση."),
                QuestionOption("C", "Απόσταση / Ταχύτητα Φωτός", False, "Αυτό είναι η καθυστέρηση διάδοσης (d_prop)."),
                QuestionOption("D", "Απόσταση / R", False, "Ανάμειξη μεγεθών χωρίς φυσικό νόημα."),
            ],
            correct_option_letter="A",
            detailed_justification=(
                "Η καθυστέρηση μετάδοσης (Transmission Delay) είναι ο χρόνος που απαιτείται για να σπρωχτούν "
                "όλα τα bits του πακέτου στο φυσικό μέσο: d_trans = L / R, όπου L είναι το μήκος του πακέτου σε bits "
                "και R ο ρυθμός μετάδοσης της ζεύξης σε bits/sec."
            ),
        ),
        # Part A - Question 3
        ExamQuestion(
            question_number=3,
            title="Υποδικτύωση /26 CIDR Match",
            question_type="Multiple Choice",
            prompt_text="Ποια από τις παρακάτω IP διευθύνσεις ανήκει στο ίδιο υποδίκτυο με την 192.168.10.55/26;",
            options=[
                QuestionOption("A", "192.168.10.65", False, "Ανήκει στο 2ο υποδίκτυο (64-127)."),
                QuestionOption("B", "192.168.10.15", True, "Ανήκει στο 1ο υποδίκτυο (0-63), όπως και η 192.168.10.55."),
                QuestionOption("C", "192.168.10.128", False, "Ανήκει στο 3ο υποδίκτυο (128-191)."),
                QuestionOption("D", "192.168.10.255", False, "Είναι το broadcast address του 4ου υποδικτύου."),
            ],
            correct_option_letter="B",
            detailed_justification=(
                "Η μάσκα /26 σημαίνει 255.255.255.192. Το μέγεθος μπλοκ (block size) είναι 256 - 192 = 64.\n"
                "Τα υποδίκτυα είναι:\n"
                "- 1ο: 192.168.10.0 έως 192.168.10.63\n"
                "- 2ο: 192.168.10.64 έως 192.168.10.127\n"
                "- 3ο: 192.168.10.128 έως 192.168.10.191\n"
                "Η διεύθυνση 192.168.10.55 ανήκει στο 1ο εύρος (0-63). Συνεπώς, μόνο η 192.168.10.15 ανήκει στο ίδιο υποδίκτυο."
            ),
        ),
        # Part A - Question 4
        ExamQuestion(
            question_number=4,
            title="Λειτουργία Εργαλείου Traceroute",
            question_type="Multiple Choice",
            prompt_text="Το Traceroute (ή Tracert) είναι ένα εργαλείο που:",
            options=[
                QuestionOption("A", "Επιστρέφει τη MAC διεύθυνση ενός απομακρυσμένου υπολογιστή.", False, "Αυτό είναι λειτουργία του ARP."),
                QuestionOption("B", "Εντοπίζει τη διαδρομή των δρομολογητών (routers) που ακολουθεί ένα πακέτο χρησιμοποιώντας το πεδίο TTL.", True, "Χρησιμοποιεί αυξανόμενο TTL και μηνύματα ICMP Time Exceeded."),
                QuestionOption("C", "Μετράει την ταχύτητα του σκληρού δίσκου.", False, "Εργαλείο benchmarking συστήματος."),
                QuestionOption("D", "Κρυπτογραφεί τα δεδομένα μεταξύ δύο κόμβων.", False, "Λειτουργία IPsec/TLS."),
            ],
            correct_option_letter="B",
            detailed_justification=(
                "Το Traceroute στέλνει διαδοχικά πακέτα με αυξανόμενες τιμές TTL (Time-To-Live = 1, 2, 3...). "
                "Κάθε ενδιάμεσος δρομολογητής μειώνει το TTL κατά 1, και όταν αυτό μηδενιστεί, απορρίπτει το πακέτο "
                "και επιστρέφει μήνυμα ICMP Time Exceeded (Type 11), αποκαλύπτοντας την IP ταυτότητά του."
            ),
        ),
        # Part A - Question 5
        ExamQuestion(
            question_number=5,
            title="Ερωτήσεις Σωστού / Λάθους",
            question_type="Multiple Choice",
            prompt_text=(
                "Επιλέξτε Σωστό (Σ) ή Λάθος (Λ):\n"
                "1. Το Pipelining effect στο packet switching μειώνει δραματικά τον συνολικό χρόνο μεταφοράς "
                "πολλαπλών πακέτων μέσω πολλών hops, συγκριτικά με το αν τα στέλναμε ένα-ένα από άκρο σε άκρο.\n"
                "2. Το πρωτόκολλο OSPF (Open Shortest Path First) χρησιμοποιεί τον αλγόριθμο Bellman-Ford.\n"
                "3. Ο εξυπηρετητής ιστού (Web Server) συνήθως φιλοξενείται σε Data Center για υψηλή διαθεσιμότητα."
            ),
            options=[
                QuestionOption("A", "1-Σ, 2-Λ, 3-Σ", True, "Σωστό: Pipelining κέρδος, OSPF χρησιμοποιεί Dijkstra και όχι Bellman-Ford, Data Center φιλοξενία."),
                QuestionOption("B", "1-Σ, 2-Σ, 3-Λ", False, "Λάθος στο 2 (το OSPF είναι Dijkstra) και στο 3."),
                QuestionOption("C", "1-Λ, 2-Λ, 3-Σ", False, "Λάθος στο 1 (το pipelining όντως μειώνει το χρόνο)."),
                QuestionOption("D", "1-Σ, 2-Λ, 3-Λ", False, "Λάθος στο 3."),
            ],
            correct_option_letter="A",
            detailed_justification=(
                "1. **Σωστό:** Το Pipelining επιτρέπει την ταυτόχρονη μετάδοση διαδοχικών πακέτων σε διαφορετικά "
                "links της διαδρομής, εκμηδενίζοντας τις περιττές καθυστερήσεις αναμονής.\n"
                "2. **Λάθος:** Το OSPF είναι πρωτόκολλο Link-State και χρησιμοποιεί τον αλγόριθμο Dijkstra. "
                "Ο αλγόριθμος Bellman-Ford ανήκει στα Distance Vector πρωτόκολλα (όπως το RIP).\n"
                "3. **Σωστό:** Οι Web Servers φιλοξενούνται σε Data Centers που προσφέρουν αδιάλειπτη παροχή ενέργειας, "
                "πλεονασμό δικτύου και τεράστιο bandwidth."
            ),
        ),
        # Part B - Exercise 1
        ExamQuestion(
            question_number=6,
            title="Άσκηση 1: Αλγόριθμος Dijkstra & Πίνακας Συντομότερων Διαδρομών",
            question_type="Algorithm Step",
            prompt_text=(
                "Θεωρήστε την παρακάτω τοπολογία δικτύου με κόστη ζεύξεων:\n"
                "          3\n"
                "      (A)---(B)\n"
                "      / \\     \\\n"
                "    1/   \\2    \\4\n"
                "    /     \\     \\\n"
                "  (C)---5-(D)---(E)\n"
                "         /   \\2\n"
                "       1/     \\\n"
                "      (F)---3-(G)\n\n"
                "Εφαρμόστε τον αλγόριθμο Dijkstra με κόμβο εκκίνησης τον A για να βρείτε τα συντομότερα μονοπάτια.\n"
                "Συμπληρώστε τον πίνακα δίνοντας το συνολικό κόστος και τον προηγούμενο κόμβο στην παρένθεση.\n"
                "Ποιο είναι το συντομότερο μονοπάτι και το τελικό κόστος για τον κόμβο G;"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Βήμα 0: Αρχικοποίηση από κόμβο A",
                    formula="D(v) = c(A,v), N' = {A}",
                    substitution="B: 3(A), C: 1(A), D: 2(A), E: inf, F: inf, G: inf",
                    result="Επιλογή C με ελάχιστο κόστος 1",
                    rationale="Ο κόμβος C έχει το μικρότερο αρχικό κόστος.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Βήμα 1: Επέκταση N' = {A, C}",
                    formula="D(v) = min(D(v), D(C) + c(C,v))",
                    substitution="D(D) = min(2, 1+5) = 2(A)",
                    result="B: 3(A), D: 2(A), E: inf, F: inf, G: inf -> Επιλογή D (κόστος 2)",
                    rationale="Ο κόμβος D παραμένει με ελάχιστο κόστος 2.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Βήμα 2: Επέκταση N' = {A, C, D}",
                    formula="D(v) = min(D(v), D(D) + c(D,v))",
                    substitution="F: 2+1=3(D), G: 2+2=4(D)",
                    result="B: 3(A), F: 3(D), G: 4(D), E: inf -> Επιλογή B (κόστος 3)",
                    rationale="Ανανεώνονται οι F και G μέσω D.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Βήμα 3: Επέκταση N' = {A, C, D, B}",
                    formula="D(v) = min(D(v), D(B) + c(B,v))",
                    substitution="E: 3+4=7(B)",
                    result="F: 3(D), G: 4(D), E: 7(B) -> Επιλογή F (κόστος 3)",
                    rationale="Ο κόμβος F έχει κόστος 3(D).",
                ),
                CalculationStep(
                    step_number=5,
                    title="Βήμα 4: Επέκταση N' = {A, C, D, B, F}",
                    formula="D(G) = min(4(D), 3+3=6(F)) = 4(D)",
                    substitution="Το κόστος προς G παραμένει 4(D)",
                    result="Επιλογή G με ελάχιστο κόστος 4",
                    rationale="Επιλέγεται ο κόμβος G με ελάχιστο κόστος 4 μέσω D.",
                ),
                CalculationStep(
                    step_number=6,
                    title="Βήμα 5: Τελική Διαδρομή προς G",
                    formula="Backtracking από G",
                    substitution="G <- D <- A",
                    result="Μονοπάτι: A -> D -> G, Κόστος: 4",
                    rationale="Συντομότερο μονοπάτι βάσει του πίνακα Dijkstra.",
                ),
            ],
            detailed_justification=(
                "Πίνακας εκτέλεσης αλγορίθμου Dijkstra:\n\n"
                "| Βήμα | Επισκέφθηκε | B | C | D | E | F | G |\n"
                "|---|---|---|---|---|---|---|---|\n"
                "| 0 | A | `3(A)` | `1(A)` | `2(A)` | `\\infty` | `\\infty` | `\\infty` |\n"
                "| 1 | `A, C` | `3(A)` | `**1(A)**` | `2(A)` | `\\infty` | `\\infty` | `\\infty` |\n"
                "| 2 | `A, C, D` | `3(A)` | `1(A)` | `**2(A)**` | `\\infty` | `3(D)` | `4(D)` |\n"
                "| 3 | `A, C, D, B` | `**3(A)**` | `1(A)` | `2(A)` | `7(B)` | `3(D)` | `4(D)` |\n"
                "| 4 | `A, C, D, B, F` | `3(A)` | `1(A)` | `2(A)` | `7(B)` | `**3(D)**` | `4(D)` |\n"
                "| 5 | `A, C, D, B, F, G` | `3(A)` | `1(A)` | `2(A)` | `7(B)` | `3(D)` | `**4(D)**` |\n\n"
                "Βάσει του πίνακα:\n"
                "- Προηγούμενος του G είναι ο D.\n"
                "- Προηγούμενος του D είναι ο A.\n"
                "- Συντομότερο μονοπάτι: **`A -> D -> G`** με συνολικό κόστος **`4`**."
            ),
        ),
        # Part B - Exercise 2
        ExamQuestion(
            question_number=7,
            title="Άσκηση 2: TCP Timeout & Sliding Window Sizing",
            question_type="Calculations",
            prompt_text=(
                "Στο πρωτόκολλο TCP, ο υπολογισμός του Timeout γίνεται βάσει της εκτίμησης του RTT:\n"
                "Timeout = 2 * EstimatedRTT (απλοποιημένη μορφή)\n\n"
                "a. Αν το τρέχον EstimatedRTT είναι 50 ms και λαμβάνεται νέο SampleRTT = 90 ms, υπολογίστε το νέο Timeout "
                "(EstimatedRTT_new = 0.8 * EstimatedRTT_old + 0.2 * SampleRTT).\n\n"
                "b. Έστω ότι συνδέεστε με FTP Server. Το Bandwidth είναι R = 400 Mbps και το RTT = 40 ms σταθερό. "
                "Ποιο πρέπει να είναι το ελάχιστο μέγεθος του Κυλιόμενου Παραθύρου (Sliding Window) σε MBytes "
                "για να αξιοποιηθεί στο έπακρο το κανάλι χωρίς αδράνεια;"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ερώτημα a: Υπολογισμός νέου EstimatedRTT",
                    formula="EstimatedRTT_new = 0.8 * EstimatedRTT_old + 0.2 * SampleRTT",
                    substitution="0.8 * 50 ms + 0.2 * 90 ms",
                    result="40 + 18 = 58 ms",
                    rationale="Εφαρμογή εκθετικά σταθμισμένου κινητού μέσου (EWMA).",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ερώτημα a: Υπολογισμός νέου Timeout",
                    formula="Timeout = 2 * EstimatedRTT_new",
                    substitution="2 * 58 ms",
                    result="116 ms",
                    rationale="Διπλάσιο του εκτιμώμενου RTT.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Ερώτημα b: Υπολογισμός Window Size σε bits",
                    formula="Window = Bandwidth * RTT",
                    substitution="(400 * 10^6 bps) * 0.04 s",
                    result="16,000,000 bits",
                    rationale="Δεδομένα που μπορούν να σταλούν κατά τη διάρκεια ενός πλήρους RTT.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Ερώτημα b: Μετατροπή σε MBytes",
                    formula="Window_Bytes = Window_bits / 8",
                    substitution="16,000,000 / 8",
                    result="2,000,000 Bytes = 2 MB",
                    rationale="Μετατροπή bits σε Bytes και MBytes (10^6).",
                ),
            ],
            detailed_justification=(
                "**a.** Νέο EstimatedRTT:\n"
                "$$\\text{EstimatedRTT}_{\\text{new}} = 0.8 \\cdot 50 + 0.2 \\cdot 90 = 40 + 18 = 58\\text{ ms}$$\n"
                "$$\\text{Timeout} = 2 \\cdot \\text{EstimatedRTT}_{\\text{new}} = 2 \\cdot 58\\text{ ms} = `116\\text{ ms}`$$\n\n"
                "**b.** Για πλήρη αξιοποίηση της ζεύξης χωρίς αδράνεια αναμονής ACKs:\n"
                "$$\\text{Window Size} = \\text{Bandwidth} \\times \\text{RTT} = (400 \\times 10^6\\text{ bps}) \\times 0.04\\text{ s} = 16.000.000\\text{ bits}$$\n"
                "Μετατροπή σε MBytes:\n"
                "$$\\text{Window Size (Bytes)} = \\frac{16.000.000}{8} = 2.000.000\\text{ Bytes} = `2\\text{ MB}`$$"
            ),
        ),
        # Part B - Exercise 3
        ExamQuestion(
            question_number=8,
            title="Άσκηση 3: Pipeline Effect & Store-and-Forward σε 2 Hops",
            question_type="Calculations",
            prompt_text=(
                "Ένα αρχείο χωρίζεται σε 100 πακέτα και αποστέλλεται από τον Host X στον Host Y μέσω ενός "
                "ενδιάμεσου Router R (σύνολο 2 hops). Κάθε ζεύξη έχει R = 1 Mbps και μέγεθος πακέτου L = 10.000 bits. "
                "Αγνοήστε propagation, processing και queuing delay.\n\n"
                "a. Πόσος χρόνος (σε δευτερόλεπτα) χρειάζεται για να μεταδοθεί ένα πακέτο σε μια ζεύξη (hop);\n"
                "b. Πόσος χρόνος (σε δευτερόλεπτα) χρειάζεται για να φτάσει το 1ο πακέτο στον Host Y;\n"
                "c. Ποιος είναι ο συνολικός χρόνος μέχρι να φτάσει και το 100ό (τελευταίο) πακέτο στον Host Y;"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ερώτημα a: Καθυστέρηση μετάδοσης ανά hop",
                    formula="d_trans = L / R",
                    substitution="10,000 bits / 1,000,000 bps",
                    result="0.01 s = 10 ms",
                    rationale="Χρόνος ώθησης όλων των bits ενός πακέτου στο link.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ερώτημα b: Άφιξη 1ου πακέτου στον προορισμό",
                    formula="d_1st = N * d_trans",
                    substitution="2 * 0.01 s",
                    result="0.02 s = 20 ms",
                    rationale="Το 1ο πακέτο αποθηκεύεται και προωθείται (Store-and-Forward) σε 2 hops.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Ερώτημα c: Συνολικός χρόνος με Pipelining",
                    formula="d_total = (N + P - 1) * d_trans",
                    substitution="(2 + 100 - 1) * 0.01 s = 101 * 0.01 s",
                    result="1.01 s = 1010 ms",
                    rationale="Κάθε ένα από τα υπόλοιπα 99 πακέτα φτάνει ακριβώς 10 ms μετά το προηγούμενό του (20 ms + 99 * 10 ms = 1010 ms).",
                ),
            ],
            detailed_justification=(
                "**a.** Καθυστέρηση μετάδοσης ανά ζεύξη:\n"
                "$$d_{\\text{trans}} = \\frac{L}{R} = \\frac{10.000\\text{ bits}}{1.000.000\\text{ bps}} = 0.01\\text{ s} = `10\\text{ ms}`$$\n\n"
                "**b.** Χρόνος άφιξης 1ου πακέτου στον Host Y (2 hops store-and-forward):\n"
                "$$d_{1\\text{st\\_packet}} = 2 \\times d_{\\text{trans}} = 2 \\times 0.01\\text{ s} = `0.02\\text{ s}`\\ (20\\text{ ms})$$\n\n"
                "**c.** Συνολικός χρόνος για P = 100 πακέτα σε N = 2 hops:\n"
                "$$d_{\\text{total}} = (N + P - 1) \\times d_{\\text{trans}} = (2 + 100 - 1) \\times 0.01\\text{ s} = 101 \\times 0.01 = `1.01\\text{ s}`$$\n"
                "*(Εναλλακτικά: 20 ms για το πρώτο πακέτο + 99 × 10 ms για τα υπόλοιπα = 1010 ms = 1.01 s).*"
            ),
        ),
    ]

    nodes = [
        TopologyNode("host_x", "Host X (Sender)", "host", 100, 150, "192.168.10.55/26"),
        TopologyNode("router_r", "Router R (Core)", "router", 450, 150, "192.168.10.1/26"),
        TopologyNode("host_y", "Host Y (Receiver)", "host", 800, 150, "192.168.10.15/26"),
    ]

    links = [
        TopologyLink("host_x", "router_r", 1, 0.0, 1.0, "copper", "Link 1 (1 Mbps)"),
        TopologyLink("router_r", "host_y", 1, 0.0, 1.0, "copper", "Link 2 (1 Mbps)"),
    ]

    return NetworkScenario(
        id="exam_synth_fc_4",
        title="Synthetic Exam 4 (Full Coverage)",
        subtitle="P2P Architecture, Transmission Delay, /26 Subnetting, Traceroute, Dijkstra Table from A, TCP Timeout & Window, Pipeline Effect",
        course_tag="Synthetic Full Coverage",
        duration_info="2 ώρες και 15 λεπτά",
        paragraphs=paragraphs,
        questions=questions,
        nodes=nodes,
        links=links,
        methodology_summary=[
            "1. P2P: Ισότιμη αρχιτεκτονική χωρίς κεντρικό σημείο αποτυχίας.",
            "2. d_trans = L / R, d_prop = d / s.",
            "3. /26: Block size 64 -> 192.168.10.55 και 192.168.10.15 ανήκουν στο ίδιο subnet.",
            "4. Dijkstra: Μονοπάτι προς G είναι A -> D -> G με κόστος 4.",
            "5. TCP EWMA: EstimatedRTT = 58 ms, Timeout = 116 ms, Window = 2 MB.",
            "6. Pipelining: d_total = (N + P - 1) * d_trans = 1.01 s.",
        ],
        calculator_type="dijkstra",
    )
