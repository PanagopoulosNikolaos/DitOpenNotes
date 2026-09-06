"""Synthetic Full Coverage Exam 5 Scenario Module.

Contains 1-to-1 representation of all exam questions from Synthetic Exam 5 (Full Coverage):
- Part A: Protocol encapsulation, Collision vs Broadcast domains, Link-State Dijkstra requirements,
  Video streaming bandwidth calculation (1000 pkts/s * 1000 Bytes = 8 Mbps), True/False (OSPF Areas, Circuit switching idle waste, ARP Reply Unicast).
- Part B: Exercise 1 (Hamming(7,4) code with Odd Parity for data 0110 -> 0001110), Exercise 2 (End-to-end 3-hop store-and-forward delay with processing delay = 38 ms),
  Exercise 3 (Cisco IOS RIPv2 configuration and Route Redistribution requirements).
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
    """Constructs and returns Synthetic Full Coverage Exam 5 scenario.

    Returns:
        NetworkScenario: The structured scenario object with 1-to-1 parity.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Το διαγώνισμα πλήρους κάλυψης "),
                TextSegment(
                    text="Synthetic Exam 5 (Full Coverage)",
                    is_highlight=True,
                    category="protocol",
                    tag_label="FULL COVERAGE 5",
                    tooltip="Διαγώνισμα συνολικής επανάληψης ύλης",
                ),
                TextSegment(text=" ανακεφαλαιώνει την αρχή της "),
                TextSegment(
                    text="Ενθυλάκωσης (Encapsulation)",
                    is_highlight=True,
                    category="protocol",
                    tag_label="ENCAPSULATION",
                    tooltip="Διαδοχική προσθήκη κεφαλίδων από το L7 στο L2",
                ),
                TextSegment(text=", το διαχωρισμό "),
                TextSegment(
                    text="Collision Domains & Broadcast Domains",
                    is_highlight=True,
                    category="hardware",
                    tag_label="DOMAINS",
                    tooltip="Οριοθέτηση από Switches και Routers αντίστοιχα",
                ),
                TextSegment(text=" και τον υπολογισμό απαιτήσεων "),
                TextSegment(
                    text="Bandwidth Πολυμέσων",
                    is_highlight=True,
                    category="delay",
                    tag_label="STREAMING",
                    tooltip="Ρυθμός bit για 1000 πακέτα των 1000 Bytes/s",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="#d69e2e",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Στο πρακτικό μέρος εξετάζονται: "),
                TextSegment(
                    text="Κώδικας Hamming(7,4) Περιττής Ισοτιμίας",
                    is_highlight=True,
                    category="protocol",
                    tag_label="HAMMING ODD",
                    tooltip="Κατασκευή πλαισίου 0001110 για δεδομένα 0110",
                ),
                TextSegment(text=", ανάλυση "),
                TextSegment(
                    text="Καθυστέρησης 3 Hops με Processing",
                    is_highlight=True,
                    category="delay",
                    tag_label="END-TO-END",
                    tooltip="Υπολογισμός d_total = 38 ms σε 2 ενδιάμεσους routers",
                ),
                TextSegment(text=" και πλήρης παραμετροποίηση "),
                TextSegment(
                    text="Cisco IOS RIPv2 CLI & Route Redistribution",
                    is_highlight=True,
                    category="routing",
                    tag_label="RIPV2 CLI",
                    tooltip="Εντολές δικτύων και ανάγκη αναδιανομής με OSPF",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="#38a169",
        ),
    ]

    questions = [
        # Part A - Question 1
        ExamQuestion(
            question_number=1,
            title="Διαδικασία Ενθυλάκωσης (Encapsulation)",
            question_type="Multiple Choice",
            prompt_text=(
                "Στη διαδικασία \"Ενθυλάκωσης\" (Encapsulation), όταν τα δεδομένα μεταφέρονται από το "
                "Επίπεδο Εφαρμογής (Application Layer) προς το Φυσικό Επίπεδο (Physical Layer):"
            ),
            options=[
                QuestionOption("A", "Αφαιρούνται οι κεφαλίδες (headers) σε κάθε επίπεδο.", False, "Αυτό είναι η απο-ενθυλάκωση (decapsulation) στον παραλήπτη."),
                QuestionOption("B", "Τα δεδομένα κρυπτογραφούνται υποχρεωτικά από το Data Link Layer.", False, "Η κρυπτογράφηση είναι προαιρετική και συνήθως γίνεται σε L6/L7 ή L3."),
                QuestionOption(
                    "C",
                    "Προστίθεται μια νέα κεφαλίδα (header) σε κάθε επίπεδο, δημιουργώντας τελικά το πλαίσιο (frame) στο Επίπεδο 2.",
                    True,
                    "Κάθε επίπεδο προσθέτει header και μετατρέπει τα δεδομένα σε L2 frame.",
                ),
                QuestionOption("D", "Η διεύθυνση IP του παραλήπτη αλλάζει σε κάθε επίπεδο.", False, "Η IP παραμένει σταθερή στο IP header."),
            ],
            correct_option_letter="C",
            detailed_justification=(
                "Η ενθυλάκωση σημαίνει ότι τα δεδομένα του ανώτερου επιπέδου αντιμετωπίζονται ως ωφέλιμο "
                "φορτίο (payload) από το αμέσως κατώτερο επίπεδο, το οποίο προσθέτει τη δική του κεφαλίδα (header) "
                "(και ουρά/trailer στο Layer 2), σχηματίζοντας διαδοχικά Segments, Packets και Frames. "
                "Η αντίστροφη διαδικασία (Decapsulation) πραγματοποιείται στον παραλήπτη."
            ),
        ),
        # Part A - Question 2
        ExamQuestion(
            question_number=2,
            title="Collision Domain έναντι Broadcast Domain",
            question_type="Multiple Choice",
            prompt_text=(
                "Ποια είναι η κύρια διαφορά ανάμεσα σε ένα Collision Domain (Πεδίο Συγκρούσεων) "
                "και ένα Broadcast Domain (Πεδίο Εκπομπής);"
            ),
            options=[
                QuestionOption("A", "Δεν υπάρχει καμία διαφορά, είναι συνώνυμα.", False, "Είναι εντελώς διαφορετικές έννοιες δικτύωσης."),
                QuestionOption(
                    "B",
                    "Ένας Δρομολογητής (Router) διαχωρίζει τα Broadcast Domains, ενώ ένας Μεταγωγέας (Switch) διαχωρίζει τα Collision Domains.",
                    True,
                    "Τα switches απομονώνουν collisions σε κάθε θύρα, ενώ οι routers τερματίζουν broadcasts.",
                ),
                QuestionOption(
                    "C",
                    "Ένας Δρομολογητής διαχωρίζει τα Collision Domains, ενώ ένας Μεταγωγέας διαχωρίζει τα Broadcast Domains.",
                    False,
                    "Αντεστραμμένος ορισμός ρόλων.",
                ),
                QuestionOption("D", "Ένα Hub διαχωρίζει τα Collision Domains.", False, "Ο Hub είναι ένα ενιαίο collision domain."),
            ],
            correct_option_letter="B",
            detailed_justification=(
                "Ο Μεταγωγέας (Switch, Layer 2) απομονώνει τις συγκρούσεις σε κάθε θύρα ξεχωριστά "
                "(διαχωρίζει collision domains), αλλά προωθεί τα πλαίσια broadcast σε όλες τις θύρες. "
                "Μόνο ο Δρομολογητής (Router, Layer 3) τερματίζει τα broadcast πακέτα, δημιουργώντας ξεχωριστά broadcast domains."
            ),
        ),
        # Part A - Question 3
        ExamQuestion(
            question_number=3,
            title="Απαιτήσεις Αλγορίθμου Dijkstra (Link State)",
            question_type="Multiple Choice",
            prompt_text="Ο αλγόριθμος Dijkstra υπολογίζει τις συντομότερες διαδρομές χρησιμοποιώντας:",
            options=[
                QuestionOption("A", "Τον αριθμό των κόμβων (hop count) και μόνο.", False, "Αυτό είναι το metric του RIP."),
                QuestionOption(
                    "B",
                    "Πλήρη γνώση της τοπολογίας και των κοστών όλων των ζεύξεων του δικτύου (Link State).",
                    True,
                    "Ο Dijkstra απαιτεί πλήρη εικόνα ολόκληρου του δικτύου (Link State Database).",
                ),
                QuestionOption(
                    "C",
                    "Πληροφορίες που λαμβάνει αποκλειστικά από τους άμεσους γείτονές του (Distance Vector).",
                    False,
                    "Αυτό είναι χαρακτηριστικό του Distance Vector / Bellman-Ford.",
                ),
                QuestionOption("D", "MAC Διευθύνσεις αποκλειστικά.", False, "Ο Dijkstra λειτουργεί σε Layer 3 τοπολογίες."),
            ],
            correct_option_letter="B",
            detailed_justification=(
                "Ο αλγόριθμος Dijkstra (κεντρικοποιημένος/Link-State) απαιτεί κάθε δρομολογητής να διαθέτει "
                "πλήρη εικόνα ολόκληρης της τοπολογίας του δικτύου και των κοστών όλων των ζεύξεων "
                "(Link-State Database) προκειμένου να κατασκευάσει το δέντρο συντομότερων διαδρομών."
            ),
        ),
        # Part A - Question 4
        ExamQuestion(
            question_number=4,
            title="Υπολογισμός Bandwidth Ροής Πολυμέσων (Video Streaming)",
            question_type="Multiple Choice",
            prompt_text=(
                "Αν μια ροή πολυμέσων (video streaming) στέλνει 1.000 πακέτα το δευτερόλεπτο και κάθε πακέτο "
                "έχει μέγεθος 1.000 Bytes, ο ελάχιστος απαιτούμενος ρυθμός μετάδοσης (Bandwidth) χωρίς απώλειες είναι:"
            ),
            options=[
                QuestionOption("A", "1 Mbps", False, "Αυτό θα αντιστοιχούσε σε 1.000.000 bits και όχι Bytes."),
                QuestionOption("B", "8 Mbps", True, "1.000 pkts/s * 1.000 Bytes * 8 bits = 8.000.000 bps = 8 Mbps."),
                QuestionOption("C", "1 Gbps", False, "Υπερβολικό μέγεθος."),
                QuestionOption("D", "8 Gbps", False, "Λάθος πολλαπλασιασμός κλίμακας."),
            ],
            correct_option_letter="B",
            detailed_justification=(
                "Ο ρυθμός σε Bytes είναι:\n"
                "1.000 πακέτα/δευτ * 1.000 Bytes/πακέτο = 1.000.000 Bytes/δευτ.\n"
                "Μετατροπή σε bits ανά δευτερόλεπτο (bps):\n"
                "1.000.000 * 8 = 8.000.000 bps = 8 Mbps."
            ),
        ),
        # Part A - Question 5
        ExamQuestion(
            question_number=5,
            title="Ερωτήσεις Σωστού / Λάθους",
            question_type="Multiple Choice",
            prompt_text=(
                "Επιλέξτε Σωστό (Σ) ή Λάθος (Λ):\n"
                "1. Το πρωτόκολλο OSPF υποστηρίζει Ιεραρχική Δρομολόγηση μέσω του διαχωρισμού σε περιοχές (Areas).\n"
                "2. Στη μεταγωγή κυκλώματος (Circuit Switching), αν ο χρήστης δεν μιλάει (αδράνεια), το εύρος ζώνης αξιοποιείται αυτόματα από άλλους χρήστες.\n"
                "3. Τα μηνύματα ARP Reply (Απαντήσεις ARP) στέλνονται ως Unicast προς τον κόμβο που έκανε το αίτημα."
            ),
            options=[
                QuestionOption("A", "1-Σ, 2-Λ, 3-Σ", True, "Σωστό: OSPF Areas, Σπατάλη στο Circuit Switching σε αδράνεια, ARP Reply είναι Unicast."),
                QuestionOption("B", "1-Σ, 2-Σ, 3-Λ", False, "Λάθος στο 2 (στο circuit switching ο πόρος παραμένει δεσμευμένος) και στο 3."),
                QuestionOption("C", "1-Λ, 2-Λ, 3-Σ", False, "Λάθος στο 1 (το OSPF υποστηρίζει Areas)."),
                QuestionOption("D", "1-Σ, 2-Λ, 3-Λ", False, "Λάθος στο 3 (το ARP Reply είναι πράγματι Unicast)."),
            ],
            correct_option_letter="A",
            detailed_justification=(
                "1. **Σωστό:** Το OSPF υποστηρίζει ιεραρχική δρομολόγηση διαιρώντας το δίκτυο σε Areas (π.χ. Backbone Area 0) "
                "για μείωση της επιβάρυνσης πλημμυρισμού LSA.\n"
                "2. **Λάθος:** Στη μεταγωγή κυκλώματος, οι πόροι παραμένουν αποκλειστικά δεσμευμένοι για όλη τη διάρκεια "
                "της κλήσης, επομένως η αδράνεια οδηγεί σε καθαρή σπατάλη bandwidth.\n"
                "3. **Σωστό:** Ενώ το ARP Request είναι Broadcast (FF:FF:FF:FF:FF:FF), το ARP Reply στέλνεται ως Unicast "
                "απευθείας στη MAC διεύθυνση του αιτούντος."
            ),
        ),
        # Part B - Exercise 1
        ExamQuestion(
            question_number=6,
            title="Άσκηση 1: Κώδικας Hamming(7,4) με Περιττή Ισοτιμία (Odd Parity)",
            question_type="Calculations",
            prompt_text=(
                "Αποστολέας θέλει να μεταδώσει το μήνυμα δεδομένων 0110 εφαρμόζοντας τον κώδικα "
                "διόρθωσης σφαλμάτων Hamming.\n\n"
                "a. Ποιος είναι ο απαιτούμενος αριθμός bits ισοτιμίας (p);\n"
                "b. Σχηματίστε το τελικό μήνυμα που θα σταλεί, υποθέτοντας χρήση περιττής ισοτιμίας (Odd Parity). "
                "Να φανεί αναλυτικά ο υπολογισμός για κάθε bit ισοτιμίας."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ερώτημα a: Υπολογισμός bits ισοτιμίας p",
                    formula="2^p >= d + p + 1",
                    substitution="2^p >= 4 + p + 1 => 2^p >= p + 5",
                    result="p = 3 bits (2^3 = 8 >= 8)",
                    rationale="Ικανοποίηση της ανισότητας Hamming για d = 4 bits δεδομένων.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ερώτημα b: Τοποθέτηση bits σε θέσεις ισχύος του 2",
                    formula="Θέσεις 1, 2, 4 = Parity, Θέσεις 3, 5, 6, 7 = Data",
                    substitution="P1(1), P2(2), D1=0(3), P4(4), D2=1(5), D3=1(6), D4=0(7)",
                    result="Πλαίσιο: [P1, P2, 0, P4, 1, 1, 0]",
                    rationale="Αντιστοίχιση των 4 bits δεδομένων 0110.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Ερώτημα b: Υπολογισμός P1 (Περιττή Ισοτιμία)",
                    formula="Ομάδα P1: θέσεις 1, 3, 5, 7 -> {P1, 0, 1, 0}",
                    substitution="Τα δεδομένα έχουν ένα 1 (περιττός αριθμός). Για να παραμείνει περιττός: P1 = 0",
                    result="P1 = 0",
                    rationale="Περιττή ισοτιμία: συνολικός αριθμός άσων = περιττός.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Ερώτημα b: Υπολογισμός P2 (Περιττή Ισοτιμία)",
                    formula="Ομάδα P2: θέσεις 2, 3, 6, 7 -> {P2, 0, 1, 0}",
                    substitution="Τα δεδομένα έχουν ένα 1 (περιττός αριθμός). Για να παραμείνει περιττός: P2 = 0",
                    result="P2 = 0",
                    rationale="Περιττή ισοτιμία: συνολικός αριθμός άσων = περιττός.",
                ),
                CalculationStep(
                    step_number=5,
                    title="Ερώτημα b: Υπολογισμός P4 (Περιττή Ισοτιμία)",
                    formula="Ομάδα P4: θέσεις 4, 5, 6, 7 -> {P4, 1, 1, 0}",
                    substitution="Τα δεδομένα έχουν δύο 1 (άρτιος αριθμός). Για να γίνει περιττός: P4 = 1",
                    result="P4 = 1",
                    rationale="Περιττή ισοτιμία: απαιτείται ένας επιπλέον άσος.",
                ),
                CalculationStep(
                    step_number=6,
                    title="Ερώτημα b: Τελική Κωδικολέξη",
                    formula="[P1, P2, D1, P4, D2, D3, D4]",
                    substitution="[0, 0, 0, 1, 1, 1, 0]",
                    result="0001110",
                    rationale="Τελικό μεταδιδόμενο πλαίσιο Hamming(7,4).",
                ),
            ],
            detailed_justification=(
                "**a.** Ανισότητα Hamming:\n"
                "$$2^p \\ge d + p + 1 \\Rightarrow 2^p \\ge 4 + p + 1 \\Rightarrow 2^p \\ge p + 5$$\n"
                "Για $p=3$: $2^3 = 8 \\ge 8$. Άρα **$p = `3`$** bits.\n\n"
                "**b.** Συνολικό μέγεθος = 7 bits. Θέσεις ισοτιμίας: 1, 2, 4. Θέσεις δεδομένων: 3, 5, 6, 7.\n\n"
                "| Θέση | 1 | 2 | 3 | 4 | 5 | 6 | 7 |\n"
                "|---|---|---|---|---|---|---|---|\n"
                "| Bit | $P_1$ | $P_2$ | $D_1$ | $P_4$ | $D_2$ | $D_3$ | $D_4$ |\n"
                "| Τιμή | `0` | `0` | `0` | `1` | `1` | `1` | `0` |\n\n"
                "Υπολογισμός με **Περιττή Ισοτιμία (Odd Parity)** (συνολικό πλήθος άσων = μονός):\n"
                "- **$P_1$ (θέσεις 1, 3, 5, 7):** $D_1=0, D_2=1, D_4=0$ (ένας άσος). Άρα **$P_1 = `0`**.\n"
                "- **$P_2$ (θέσεις 2, 3, 6, 7):** $D_1=0, D_3=1, D_4=0$ (ένας άσος). Άρα **$P_2 = `0`**.\n"
                "- **$P_4$ (θέσεις 4, 5, 6, 7):** $D_2=1, D_3=1, D_4=0$ (δύο άσοι). Άρα **$P_4 = `1`**.\n\n"
                "Τελικό μεταδιδόμενο μήνυμα: **`0001110`**"
            ),
        ),
        # Part B - Exercise 2
        ExamQuestion(
            question_number=7,
            title="Άσκηση 2: Ολοκληρωμένη Καθυστέρηση End-to-End (3 Hops με Processing)",
            question_type="Calculations",
            prompt_text=(
                "Θεωρήστε τη διαδρομή από τον Υπολογιστή A στον Υπολογιστή B μέσω 2 Δρομολογητών (N = 3 hops).\n"
                "Κάθε ζεύξη έχει:\n"
                "- Μήκος: d = 2.000 km\n"
                "- Ταχύτητα διάδοσης: s = 2 * 10^8 m/s\n"
                "- Bandwidth: R = 10 Mbps\n\n"
                "Πακέτο μεγέθους L = 20.000 bits αποστέλλεται από A σε B.\n"
                "Κάθε ενδιάμεσος δρομολογητής εισάγει d_proc = 1 ms. Queuing delay = 0.\n\n"
                "a. Πόση είναι η καθυστέρηση μετάδοσης (d_trans) ανά hop;\n"
                "b. Πόση είναι η καθυστέρηση διάδοσης (d_prop) ανά hop;\n"
                "c. Υπολογίστε τη συνολική καθυστέρηση από άκρο σε άκρο (Total end-to-end delay)."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ερώτημα a: Καθυστέρηση μετάδοσης ανά hop",
                    formula="d_trans = L / R",
                    substitution="20,000 bits / (10 * 10^6 bps)",
                    result="0.002 s = 2 ms",
                    rationale="Χρόνος ώθησης του πακέτου στη γραμμή.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ερώτημα b: Καθυστέρηση διάδοσης ανά hop",
                    formula="d_prop = d / s",
                    substitution="(2,000 * 10^3 m) / (2 * 10^8 m/s)",
                    result="0.01 s = 10 ms",
                    rationale="Χρόνος φυσικής διέλευσης του σήματος στο μέσο.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Ερώτημα c: Συνολική καθυστέρηση End-to-End",
                    formula="d_total = N * d_trans + N * d_prop + (N - 1) * d_proc",
                    substitution="3 * (2 ms) + 3 * (10 ms) + 2 * (1 ms)",
                    result="6 ms + 30 ms + 2 ms = 38 ms",
                    rationale="Store-and-forward σε 3 hops με 2 ενδιάμεσους δρομολογητές επεξεργασίας.",
                ),
            ],
            detailed_justification=(
                "**a.** $$d_{\\text{trans}} = \\frac{L}{R} = \\frac{20.000}{10 \\times 10^6} = 0.002\\text{ s} = `2\\text{ ms}`$$\n\n"
                "**b.** $$d_{\\text{prop}} = \\frac{d}{s} = \\frac{2 \\times 10^6\\text{ m}}{2 \\times 10^8\\text{ m/s}} = 0.01\\text{ s} = `10\\text{ ms}`$$\n\n"
                "**c.** Για store-and-forward σε $N = 3$ hops με $N-1 = 2$ ενδιάμεσους δρομολογητές:\n"
                "$$d_{\\text{total}} = N \\cdot d_{\\text{trans}} + N \\cdot d_{\\text{prop}} + (N-1) \\cdot d_{\\text{proc}}$$\n"
                "$$d_{\\text{total}} = 3 \\cdot (2\\text{ ms}) + 3 \\cdot (10\\text{ ms}) + 2 \\cdot (1\\text{ ms}) = 6 + 30 + 2 = `38\\text{ ms}`$$"
            ),
        ),
        # Part B - Exercise 3
        ExamQuestion(
            question_number=8,
            title="Άσκηση 3: Διαμόρφωση Cisco IOS RIPv2 & Route Redistribution",
            question_type="Calculations",
            prompt_text=(
                "Για το δίκτυο με Router1 συνδεδεμένο σε Fa0/0 (192.168.10.0/24), Se0/0/0 (10.0.1.0/24) "
                "και Se0/0/1 (10.0.2.0/24):\n\n"
                "a. Συμπληρώστε τις εντολές ενεργοποίησης RIPv2 στο Cisco IOS.\n"
                "b. Αν προστεθεί τρίτος δρομολογητής (Router3) στο δίκτυο 10.0.1.0/24 που τρέχει OSPF αντί για RIP, "
                "θα μπορέσει ο Router1 να μάθει τις διαδρομές του Router3 μέσω RIP αυτόματα; Δικαιολογήστε."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ερώτημα a: Είσοδος σε Global Config",
                    formula="enable -> configure terminal",
                    substitution="Router1# configure terminal",
                    result="Router1(config)#",
                    rationale="Μετάβαση στη γραμμή εντολών καθολικής διαμόρφωσης.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ερώτημα a: Ενεργοποίηση RIP Routing Process",
                    formula="router rip -> version 2 -> no auto-summary",
                    substitution="Router1(config)# router rip\nRouter1(config-router)# version 2\nRouter1(config-router)# no auto-summary",
                    result="Ενεργοποίηση classless RIPv2",
                    rationale="Υποστήριξη VLSM και κατάργηση αυτόματης σύνοψης.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Ερώτημα a: Δήλωση συνδεδεμένων δικτύων",
                    formula="network <major-network-or-subnet>",
                    substitution="network 192.168.10.0\nnetwork 10.0.1.0\nnetwork 10.0.2.0",
                    result="Ανακοίνωση και ακρόαση RIP στις 3 θύρες",
                    rationale="Ενεργοποίηση αποστολής/λήψης RIP updates.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Ερώτημα b: Αξιολόγηση επικοινωνίας RIP και OSPF",
                    formula="Distance Vector vs Link-State metrics",
                    substitution="Hop count vs Cumulative Cost",
                    result="Ασυμβατότητα χωρίς Route Redistribution",
                    rationale="Διαφορετικοί αλγόριθμοι και μετρικά.",
                ),
            ],
            detailed_justification=(
                "**a. Συμπληρωμένες εντολές CLI Cisco IOS:**\n"
                "```text\n"
                "Router1> enable\n"
                "Router1# configure terminal\n"
                "Router1(config)# router rip\n"
                "Router1(config-router)# version 2\n"
                "Router1(config-router)# no auto-summary\n"
                "Router1(config-router)# network 192.168.10.0\n"
                "Router1(config-router)# network 10.0.1.0\n"
                "Router1(config-router)# network 10.0.2.0\n"
                "Router1(config-router)# end\n"
                "```\n\n"
                "**b.** **`Όχι`**, δεν θα μπορέσει να τις μάθει αυτόματα. Το RIP και το OSPF είναι δύο εντελώς διαφορετικά "
                "πρωτόκολλα δρομολόγησης με ασύμβατα metrics (hop count έναντι link cost) και αλγορίθμους "
                "(Distance Vector έναντι Link State). Για να γίνει ανταλλαγή πληροφοριών δρομολόγησης, απαιτείται "
                "χειροκίνητη παραμετροποίηση **αναδιανομής δρομολόγησης (route redistribution)** από τον διαχειριστή "
                "σε έναν ενδιάμεσο δρομολογητή που εκτελεί ταυτόχρονα και τα δύο πρωτόκολλα (ASBR)."
            ),
        ),
    ]

    nodes = [
        TopologyNode("r1", "Router 1 (RIPv2)", "router", 450, 150, "192.168.10.1"),
        TopologyNode("lan", "LAN Subnet", "host", 450, 20, "192.168.10.0/24 (Fa0/0)"),
        TopologyNode("r2", "Router 2", "router", 150, 280, "10.0.1.0/24 (Se0/0/0)"),
        TopologyNode("r3", "Router 3 (OSPF)", "router", 750, 280, "10.0.2.0/24 (Se0/0/1)"),
    ]

    links = [
        TopologyLink("r1", "lan", 100, 0.1, 2.0, "copper", "Fa0/0 (192.168.10.0/24)"),
        TopologyLink("r1", "r2", 10, 10.0, 2.0, "serial", "Se0/0/0 (10.0.1.0/24)"),
        TopologyLink("r1", "r3", 10, 10.0, 2.0, "serial", "Se0/0/1 (10.0.2.0/24)"),
    ]

    return NetworkScenario(
        id="exam_synth_fc_5",
        title="Synthetic Exam 5 (Full Coverage)",
        subtitle="Encapsulation, Collision vs Broadcast Domains, Dijkstra Link State, Video Streaming Bandwidth, Hamming(7,4) Odd Parity, 3-Hop Delay with d_proc, Cisco IOS RIPv2 CLI",
        course_tag="Synthetic Full Coverage",
        duration_info="2 ώρες και 15 λεπτά",
        paragraphs=paragraphs,
        questions=questions,
        nodes=nodes,
        links=links,
        methodology_summary=[
            "1. Ενθυλάκωση: Προσθήκη L4 segment -> L3 packet -> L2 frame.",
            "2. Collision vs Broadcast: Switch = Collision, Router = Broadcast.",
            "3. Bandwidth Video: 1000 pkts/s * 1000 Bytes = 8 Mbps.",
            "4. Hamming(7,4) Odd Parity: p=3, κωδικολέξη για 0110 = 0001110.",
            "5. End-to-End 3-Hop Delay: 3 * d_trans + 3 * d_prop + 2 * d_proc = 38 ms.",
            "6. Cisco RIPv2 CLI: version 2, no auto-summary, network δηλώσεις.",
            "7. Route Redistribution: Απαραίτητη για OSPF <-> RIP.",
        ],
        calculator_type="delay",
    )
