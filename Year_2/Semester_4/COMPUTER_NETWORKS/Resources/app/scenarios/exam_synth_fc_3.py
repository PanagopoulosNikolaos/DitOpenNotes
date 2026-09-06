"""Synthetic Full Coverage Exam 3 Scenario Module.

Contains 1-to-1 representation of all exam questions from Synthetic Exam 3 (Full Coverage):
- Part A: Count-to-Infinity in Distance Vector, BGP Hot-Potato Routing, Hub vs Switch collision domains,
  Bandwidth-Delay Product (BDP) definition, True/False (DNS Client-Server, IP vs MAC stability, RIP 15 hop limit).
- Part B: Exercise 1 (Distance Vector Bellman-Ford next-hop calculation), Exercise 2 (ARP addressing across router hops),
  Exercise 3 (BDP propagation delay and router queuing delay evacuation calculation).
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
    """Constructs and returns Synthetic Full Coverage Exam 3 scenario.

    Returns:
        NetworkScenario: The structured scenario object with 1-to-1 parity.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Το διαγώνισμα πλήρους κάλυψης "),
                TextSegment(
                    text="Synthetic Exam 3 (Full Coverage)",
                    is_highlight=True,
                    category="protocol",
                    tag_label="FULL COVERAGE 3",
                    tooltip="Διαγώνισμα συνολικής επανάληψης ύλης",
                ),
                TextSegment(text=" εστιάζει στις παθολογίες των αλγορίθμων δρομολόγησης όπως το "),
                TextSegment(
                    text="Count-to-Infinity",
                    is_highlight=True,
                    category="routing",
                    tag_label="COUNT TO INFINITY",
                    tooltip="Ατέρμονη αύξηση μετρικού κόστους σε Distance Vector",
                ),
                TextSegment(text=", στην πολιτική "),
                TextSegment(
                    text="Hot-Potato Routing στο BGP",
                    is_highlight=True,
                    category="routing",
                    tag_label="HOT POTATO",
                    tooltip="Εξαγωγή κίνησης από την πλησιέστερη έξοδο IGP",
                ),
                TextSegment(text=" και στο διαχωρισμό "),
                TextSegment(
                    text="Collision Domains (Hub vs Switch)",
                    is_highlight=True,
                    category="hardware",
                    tag_label="DOMAINS",
                    tooltip="Shared medium σε Hub έναντι micro-segmentation σε Switch",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="#2b6cb0",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Στο υπολογιστικό μέρος επιλύονται: "),
                TextSegment(
                    text="Εξίσωση Bellman-Ford",
                    is_highlight=True,
                    category="routing",
                    tag_label="BELLMAN-FORD",
                    tooltip="Επιλογή διαδρομής ελάχιστου κόστους προς κόμβο D",
                ),
                TextSegment(text=", ανάλυση επικεφαλίδων "),
                TextSegment(
                    text="ARP και L2/L3 Addressing",
                    is_highlight=True,
                    category="protocol",
                    tag_label="ARP / L2-L3",
                    tooltip="Διατήρηση IP και ανανέωση MAC σε διαδρομή router",
                ),
                TextSegment(text=" και υπολογισμός "),
                TextSegment(
                    text="BDP & Queuing Delay",
                    is_highlight=True,
                    category="delay",
                    tag_label="BDP & QUEUE",
                    tooltip="Καθυστέρηση εκκένωσης buffer 1MB σε ζεύξη 1 Gbps",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="#c53030",
        ),
    ]

    questions = [
        # Part A - Question 1
        ExamQuestion(
            question_number=1,
            title="Count-to-Infinity & Distance Vector",
            question_type="Multiple Choice",
            prompt_text="Το πρόβλημα \"Count-to-Infinity\" (Μέτρηση μέχρι το Άπειρο) είναι μια γνωστή αδυναμία στους αλγόριθμους δρομολόγησης τύπου:",
            options=[
                QuestionOption("A", "Link State (Κατάστασης Ζεύξης)", False, "Τα πρωτόκολλα Link State δεν εμφανίζουν count-to-infinity."),
                QuestionOption("B", "Distance Vector (Διάνυσμα Απόστασης)", True, "Στο Distance Vector οι κόμβοι μπορεί να ανακυκλώνουν απαρχαιωμένες πληροφορίες δρομολόγησης."),
                QuestionOption("C", "Longest Prefix Match", False, "Ο κανόνας LPM είναι αλγόριθμος προώθησης και όχι δρομολόγησης."),
                QuestionOption("D", "CSMA/CD", False, "Το CSMA/CD είναι πρωτόκολλο πολλαπλής πρόσβασης στο Data Link Layer."),
            ],
            correct_option_letter="B",
            detailed_justification=(
                "Στον αλγόριθμο Distance Vector, αν διακοπεί μια σύνδεση, οι κόμβοι μπορεί να ανταλλάσσουν "
                "μεταξύ τους απαρχαιωμένες πληροφορίες δρομολόγησης αυξάνοντας σταδιακά το υποτιθέμενο "
                "κόστος στο άπειρο (Routing Loops / Count to Infinity)."
            ),
        ),
        # Part A - Question 2
        ExamQuestion(
            question_number=2,
            title="BGP Hot-Potato Routing",
            question_type="Multiple Choice",
            prompt_text="Η δρομολόγηση \"Καυτής Πατάτας\" (Hot-Potato Routing) στο πρωτόκολλο BGP περιγράφει την τακτική κατά την οποία:",
            options=[
                QuestionOption("A", "Το πακέτο απορρίπτεται αν υπερβεί το Time To Live (TTL).", False, "Αυτό είναι η λειτουργία του TTL στο IP επίπεδο."),
                QuestionOption("B", "Το AS προσπαθεί να στείλει το πακέτο έξω από το δίκτυό του μέσω του φθηνότερου εσωτερικού μονοπατιού (πλησιέστερη έξοδος).", True, "Επιλέγεται η πύλη εξόδου με το μικρότερο εσωτερικό IGP κόστος."),
                QuestionOption("C", "Το BGP επιλέγει πάντα το μονοπάτι με τα λιγότερα Αυτόνομα Συστήματα (AS-Path length).", False, "Αυτό είναι το γενικό BGP rule επιλογής AS-Path."),
                QuestionOption("D", "Ένα πακέτο αναπηδά ατέρμονα μεταξύ δύο δρομολογητών.", False, "Αυτό περιγράφει routing loop."),
            ],
            correct_option_letter="B",
            detailed_justification=(
                "Το hot-potato routing εφαρμόζεται στο BGP όταν υπάρχουν πολλαπλές πύλες εξόδου προς ένα "
                "επόμενο AS. Το δίκτυο επιλέγει την έξοδο με το μικρότερο εσωτερικό IGP (π.χ. OSPF) κόστος, "
                "ώστε να απαλλαγεί από το πακέτο όσο το δυνατόν γρηγορότερα εξοικονομώντας εσωτερικούς πόρους."
            ),
        ),
        # Part A - Question 3
        ExamQuestion(
            question_number=3,
            title="Hub vs Switch Collision Domains",
            question_type="Multiple Choice",
            prompt_text="Αν ένα τοπικό δίκτυο χρησιμοποιεί αποκλειστικά Hub αντί για Switch, ποια από τις παρακάτω προτάσεις είναι σωστή;",
            options=[
                QuestionOption("A", "Όλοι οι κόμβοι βρίσκονται στο ίδιο πεδίο συγκρούσεων (collision domain).", True, "Ο Hub είναι αναμεταδότης επιπέδου 1 και αποτελεί κοινό μέσο."),
                QuestionOption("B", "Κάθε θύρα αποτελεί ξεχωριστό πεδίο συγκρούσεων (collision domain).", False, "Αυτό συμβαίνει αποκλειστικά σε Switch."),
                QuestionOption("C", "Ο Hub υποστηρίζει CSMA/CA, οπότε δεν υπάρχουν συγκρούσεις.", False, "Ο Hub χρησιμοποιεί κλασικό CSMA/CD Ethernet."),
                QuestionOption("D", "Ο Hub λειτουργεί στο Επίπεδο 3 και κάνει δρομολόγηση.", False, "Ο Hub λειτουργεί στο Φυσικό Επίπεδο (Layer 1)."),
            ],
            correct_option_letter="A",
            detailed_justification=(
                "Ο Hub λειτουργεί στο Φυσικό Επίπεδο (Layer 1) και επαναλαμβάνει κάθε εισερχόμενο ηλεκτρικό "
                "σήμα/bit σε όλες τις υπόλοιπες θύρες. Αποτελεί ένα ενιαίο, κοινόχρηστο μέσο (shared medium), "
                "με αποτέλεσμα όλοι οι συνδεδεμένοι κόμβοι να ανήκουν στο ίδιο collision domain."
            ),
        ),
        # Part A - Question 4
        ExamQuestion(
            question_number=4,
            title="Ορισμός Bandwidth-Delay Product (BDP)",
            question_type="Multiple Choice",
            prompt_text="Το γινόμενο \"Bandwidth-Delay Product\" (BDP) αναπαριστά:",
            options=[
                QuestionOption("A", "Το ρυθμό δεδομένων που μπορεί να επεξεργαστεί ο δρομολογητής ανά δευτερόλεπτο.", False, "Αυτό είναι η χωρητικότητα επεξεργασίας."),
                QuestionOption("B", "Τον χρόνο που απαιτείται για να γίνει αλλαγή πλαισίου στο Physical Layer.", False, "Αυτό αφορά χρονισμό πλαισίωσης."),
                QuestionOption("C", "Τον μέγιστο αριθμό bits που μπορούν να βρίσκονται \"πάνω\" στο φυσικό μέσο (στον αέρα / στο καλώδιο) σε μια δεδομένη χρονική στιγμή.", True, "Το γινόμενο R * d_prop εκφράζει τα bits in-flight μέσα στο κανάλι."),
                QuestionOption("D", "Το μέγεθος της ουράς του δρομολογητή σε πακέτα.", False, "Αυτό είναι το buffer size."),
            ],
            correct_option_letter="C",
            detailed_justification=(
                "Το γινόμενο BDP = R * d_prop εκφράζει τη χωρητικότητα του αγωγού σε δεδομένα. Αντιστοιχεί στον "
                "αριθμό των bits που ταξιδεύουν \"εν πτήσει\" (bits in flight) μέσα στο φυσικό μέσο."
            ),
        ),
        # Part A - Question 5
        ExamQuestion(
            question_number=5,
            title="Ερωτήσεις Σωστού / Λάθους",
            question_type="Multiple Choice",
            prompt_text=(
                "Επιλέξτε Σωστό (Σ) ή Λάθος (Λ):\n"
                "1. Ένα DNS αίτημα λειτουργεί με βάση το μοντέλο Client-Server.\n"
                "2. Η διεύθυνση MAC παραμένει ίδια καθώς το πακέτο διασχίζει πολλούς δρομολογητές στο διαδίκτυο, ενώ η IP αλλάζει σε κάθε hop.\n"
                "3. Το πρωτόκολλο RIP έχει μέγιστο hop count 15, κάνοντας το ακατάλληλο για τεράστια δίκτυα."
            ),
            options=[
                QuestionOption("A", "1-Σ, 2-Λ, 3-Σ", True, "Σωστό: Client-Server DNS, IP παραμένει σταθερή και MAC αλλάζει, RIP max hop 15."),
                QuestionOption("B", "1-Σ, 2-Σ, 3-Λ", False, "Λάθος στο 2 (η MAC αλλάζει) και στο 3."),
                QuestionOption("C", "1-Λ, 2-Λ, 3-Σ", False, "Λάθος στο 1 (το DNS είναι Client-Server)."),
                QuestionOption("D", "1-Σ, 2-Λ, 3-Λ", False, "Λάθος στο 3 (το RIP όντως έχει max hop 15)."),
            ],
            correct_option_letter="A",
            detailed_justification=(
                "1. **Σωστό:** Ο πελάτης (resolver) στέλνει DNS Query στον DNS Server και λαμβάνει DNS Response (Client-Server).\n"
                "2. **Λάθος:** Η διεύθυνση IP παραμένει σταθερή από άκρο σε άκρο (εκτός NAT), ενώ η διεύθυνση MAC αλλάζει σε κάθε hop (από router σε router).\n"
                "3. **Σωστό:** Το RIP θέτει μέγιστο όριο τα 15 hops για αποφυγή βρόχων, θεωρώντας το 16 ως άπειρο (unreachable)."
            ),
        ),
        # Part B - Exercise 1
        ExamQuestion(
            question_number=6,
            title="Άσκηση 1: Distance Vector Routing (Bellman-Ford) & Next-Hop",
            question_type="Calculations",
            prompt_text=(
                "Σε ένα δίκτυο που χρησιμοποιεί τον αλγόριθμο Bellman-Ford (Distance Vector), ο δρομολογητής X "
                "έχει τους εξής γείτονες: Y (κόστος=2), Z (κόστος=5), W (κόστος=1).\n\n"
                "Ο X λαμβάνει τους παρακάτω πίνακες δρομολόγησης από τους γείτονές του, που αφορούν το κόστος "
                "για την άφιξη στον κόμβο προορισμού D:\n"
                "- Από Y: Κόστος προς D = 8\n"
                "- Από Z: Κόστος προς D = 3\n"
                "- Από W: Κόστος προς D = 10\n\n"
                "a. Ποιο είναι το νέο υπολογισμένο κόστος από τον κόμβο X προς τον D; Δείξτε τους υπολογισμούς σας.\n"
                "b. Μέσω ποιου γείτονα (Next-Hop) θα δρομολογεί ο X τα πακέτα του προς τον D;"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Εφαρμογή εξίσωσης Bellman-Ford",
                    formula="d_X(D) = min_v { c(X,v) + d_v(D) }",
                    substitution="v in {Y, Z, W}",
                    result="Αξιολόγηση όλων των γειτόνων",
                    rationale="Ο κόμβος εξετάζει το συνολικό κόστος μέσω κάθε άμεσου γείτονα.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Υπολογισμός διαδρομής μέσω γείτονα Y",
                    formula="c(X,Y) + d_Y(D)",
                    substitution="2 + 8",
                    result="10",
                    rationale="Κόστος τοπικής ζεύξης 2 συν αναφερθέν κόστος 8.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Υπολογισμός διαδρομής μέσω γείτονα Z",
                    formula="c(X,Z) + d_Z(D)",
                    substitution="5 + 3",
                    result="8",
                    rationale="Κόστος τοπικής ζεύξης 5 συν αναφερθέν κόστος 3.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Υπολογισμός διαδρομής μέσω γείτονα W",
                    formula="c(X,W) + d_W(D)",
                    substitution="1 + 10",
                    result="11",
                    rationale="Κόστος τοπικής ζεύξης 1 συν αναφερθέν κόστος 10.",
                ),
                CalculationStep(
                    step_number=5,
                    title="Επιλογή Ελάχιστου Κόστους και Next-Hop",
                    formula="min { 10, 8, 11 }",
                    substitution="min(10, 8, 11) = 8",
                    result="Νέο κόστος = 8, Next-Hop = Z",
                    rationale="Το ελάχιστο κόστος είναι 8 και επιτυγχάνεται μέσω του γείτονα Z.",
                ),
            ],
            detailed_justification=(
                "**a.** Ο αλγόριθμος Bellman-Ford υπολογίζει:\n"
                "$$d_X(D) = \\min_{v} \\{ c(X,v) + d_v(D) \\}$$\n"
                "- Μέσω Y: $c(X,Y) + d_Y(D) = 2 + 8 = 10$\n"
                "- Μέσω Z: $c(X,Z) + d_Z(D) = 5 + 3 = 8$\n"
                "- Μέσω W: $c(X,W) + d_W(D) = 1 + 10 = 11$\n\n"
                "Το ελάχιστο κόστος είναι $\\min \\{10, 8, 11\\} = \\mathbf{8}$. Άρα, το νέο κόστος προς τον D είναι **`8`**.\n\n"
                "**b.** Το ελάχιστο κόστος προέκυψε μέσω του κόμβου Z. Επομένως, το Next-Hop για τον προορισμό D είναι ο κόμβος **`Z`**."
            ),
        ),
        # Part B - Exercise 2
        ExamQuestion(
            question_number=7,
            title="Άσκηση 2: ARP μέσω Δρομολογητή (Router) & Ανάλυση Διευθύνσεων",
            question_type="Calculations",
            prompt_text=(
                "Δίνεται η τοπολογία:\n"
                "[ Υπολογιστής A ] ------------------ [ Δρομολογητής R ] ------------------ [ Υπολογιστής B ]\n"
                " IP: 10.0.0.5                       IP_Left: 10.0.0.1                    IP: 192.168.1.10\n"
                " MAC: 00:AA:11:22:33:44             MAC_Left: 00:RR:AA:BB:CC:01          MAC: 00:BB:99:88:77:66\n"
                "                                    IP_Right: 192.168.1.1\n"
                "                                    MAC_Right: 00:RR:AA:BB:CC:02\n\n"
                "Ο υπολογιστής A γνωρίζει την IP του B, αλλά η ARP Cache του είναι άδεια.\n"
                "a. Ποιο ARP αίτημα πρέπει να κάνει ο υπολογιστής A (Sender IP, Sender MAC, Target IP); "
                "Ποιο θα είναι το Destination MAC στο Layer 2 Ethernet Frame;\n"
                "b. Όταν το πραγματικό IP πακέτο δεδομένων (όχι το ARP) αναχωρεί από τον δρομολογητή R προς "
                "τον υπολογιστή B, ποια είναι τα στοιχεία του (Source IP, Destination IP, Source MAC, Destination MAC);"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ερώτημα a: ARP Request από Host A",
                    formula="Sender: IP_A / MAC_A, Target: Default Gateway IP_R_Left",
                    substitution="Sender: 10.0.0.5 / 00:AA:11:22:33:44, Target: 10.0.0.1",
                    result="Broadcast Frame: FF:FF:FF:FF:FF:FF",
                    rationale="Ο Host A αναγνωρίζει ότι ο B είναι σε άλλο υποδίκτυο και αναζητά τη MAC της πύλης του.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ερώτημα b: IP Πακέτο Δεδομένων (Router R -> Host B)",
                    formula="Src IP σταθερή, Dst IP σταθερή, Src MAC = R_Right, Dst MAC = B",
                    substitution="Src IP: 10.0.0.5, Dst IP: 192.168.1.10 | Src MAC: 00:RR:AA:BB:CC:02, Dst MAC: 00:BB:99:88:77:66",
                    result="Ανανέωση διευθύνσεων L2, διατήρηση διευθύνσεων L3",
                    rationale="Ο δρομολογητής απο-ενθυλακώνει το L2 πλαίσιο και επανα-ενθυλακώνει με τις διευθύνσεις της εξερχόμενης ζεύξης.",
                ),
            ],
            detailed_justification=(
                "**a.** Ο υπολογιστής A αναζητά τη MAC διεύθυνση της πύλης του (Router R), καθώς ο B είναι σε εξωτερικό δίκτυο:\n"
                "- Sender IP: `10.0.0.5`\n"
                "- Sender MAC: `00:AA:11:22:33:44`\n"
                "- Target IP: `10.0.0.1` (Η IP της αριστερής πλευράς του R)\n"
                "- Destination MAC στο Ethernet Frame: `FF:FF:FF:FF:FF:FF` (Broadcast)\n\n"
                "**b.** Κατά την έξοδο από τον δρομολογητή R προς τον B:\n"
                "- Source IP: `10.0.0.5` (παραμένει η αρχική IP του A)\n"
                "- Destination IP: `192.168.1.10` (παραμένει η IP του B)\n"
                "- Source MAC: `00:RR:AA:BB:CC:02` (Η MAC της δεξιάς πλευράς του R)\n"
                "- Destination MAC: `00:BB:99:88:77:66` (Η MAC του B)"
            ),
        ),
        # Part B - Exercise 3
        ExamQuestion(
            question_number=8,
            title="Άσκηση 3: BDP & Καθυστέρηση Ουράς (Queuing Delay)",
            question_type="Calculations",
            prompt_text=(
                "Μια ζεύξη μεταξύ δύο ηπείρων έχει ταχύτητα διάδοσης s = 2 * 10^8 m/s και μήκος καλωδίου d = 6.000 km. "
                "Ο ρυθμός μετάδοσης δεδομένων είναι R = 1 Gbps (10^9 bps).\n\n"
                "a. Ποια είναι η καθυστέρηση διάδοσης (d_prop);\n"
                "b. Ποιος είναι ο μέγιστος αριθμός bits που μπορούν να βρίσκονται μέσα στο καλώδιο ανά πάσα στιγμή (BDP);\n"
                "c. Αν σε έναν ενδιάμεσο δρομολογητή, το μέγεθος της ουράς (buffer) είναι γεμάτο με 1.000.000 bytes κίνησης "
                "τη στιγμή που φτάνει ένα νέο πακέτο σας, και η ταχύτητα εξόδου είναι 1 Gbps, πόσος χρόνος θα περάσει "
                "(Καθυστέρηση Ουράς - d_queue) μέχρι να αρχίσει η μετάδοση του δικού σας πακέτου;"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Ερώτημα a: Καθυστέρηση Διάδοσης d_prop",
                    formula="d_prop = d / s",
                    substitution="(6.000 * 10^3 m) / (2 * 10^8 m/s)",
                    result="0.03 s = 30 ms",
                    rationale="Χρόνος φυσικής μετακίνησης του σήματος κατά μήκος της διαηπειρωτικής ίνας.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ερώτημα b: Bandwidth-Delay Product (BDP)",
                    formula="BDP = R * d_prop",
                    substitution="10^9 bps * 0.03 s",
                    result="30,000,000 bits = 30 Mbits",
                    rationale="Συνολικός όγκος δεδομένων που ταξιδεύει εντός του αγωγού ταυτόχρονα.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Ερώτημα c: Μετατροπή μεγέθους buffer σε bits",
                    formula="L_queue = Buffer_Bytes * 8",
                    substitution="1,000,000 Bytes * 8",
                    result="8,000,000 bits",
                    rationale="Μετατροπή των Bytes σε bits για διαίρεση με το bandwidth εξόδου σε bps.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Ερώτημα c: Καθυστέρηση Ουράς d_queue",
                    formula="d_queue = L_queue / R_out",
                    substitution="8,000,000 bits / 10^9 bps",
                    result="0.008 s = 8 ms",
                    rationale="Χρόνος εκκένωσης της συσσωρευμένης ουράς πριν από την εξυπηρέτηση του πακέτου.",
                ),
            ],
            detailed_justification=(
                "**a.** $$d_{\\text{prop}} = \\frac{d}{s} = \\frac{6.000 \\times 10^3\\text{ m}}{2 \\times 10^8\\text{ m/s}} = \\frac{6 \\times 10^6}{2 \\times 10^8} = 0.03\\text{ s} = `30\\text{ ms}`$$\n\n"
                "**b.** $$\\text{BDP} = R \\times d_{\\text{prop}} = 10^9\\text{ bps} \\times 0.03\\text{ s} = `30.000.000\\text{ bits}` \\text{ (ή 30 Mbits)}$$\n\n"
                "**c.** Ο χρόνος εκκένωσης της ουράς ($1.000.000\\text{ Bytes} = 8.000.000\\text{ bits}$) με ταχύτητα $1\\text{ Gbps}$ είναι:\n"
                "$$d_{\\text{queue}} = \\frac{L_{\\text{queue}}}{R_{\\text{out}}} = \\frac{8.000.000\\text{ bits}}{10^9\\text{ bps}} = 8 \\times 10^{-3}\\text{ s} = `8\\text{ ms}`$$"
            ),
        ),
    ]

    nodes = [
        TopologyNode("host_a", "Host A (Client)", "host", 100, 150, "10.0.0.5"),
        TopologyNode("router_r", "Router R (Gateway)", "router", 450, 150, "10.0.0.1 / 192.168.1.1"),
        TopologyNode("host_b", "Host B (Server)", "host", 800, 150, "192.168.1.10"),
    ]

    links = [
        TopologyLink("host_a", "router_r", 1000, 30.0, 2.0, "fiber", "Transoceanic 6000km Link (1 Gbps)"),
        TopologyLink("router_r", "host_b", 100, 0.5, 2.0, "copper", "LAN Link (100 Mbps)"),
    ]

    return NetworkScenario(
        id="exam_synth_fc_3",
        title="Synthetic Exam 3 (Full Coverage)",
        subtitle="Count-to-Infinity, BGP Hot-Potato, Hub vs Switch Domains, Bellman-Ford Routing, Router ARP, BDP & Queue Delay",
        course_tag="Synthetic Full Coverage",
        duration_info="2 ώρες και 15 λεπτά",
        paragraphs=paragraphs,
        questions=questions,
        nodes=nodes,
        links=links,
        methodology_summary=[
            "1. Distance Vector: Ευάλωτο σε count-to-infinity / routing loops.",
            "2. Hot-Potato: Εξαγωγή κίνησης από την πλησιέστερη έξοδο (ελάχιστο IGP cost).",
            "3. Hub vs Switch: Hub = 1 ενιαίο collision domain, Switch = Micro-segmentation.",
            "4. Bellman-Ford: d_X(D) = min { c(X,v) + d_v(D) } = min{10, 8, 11} = 8 via Z.",
            "5. ARP Router Hop: Sender Target IP = Gateway IP, Dest MAC = Broadcast.",
            "6. BDP = R * d_prop = 30 Mbits, d_queue = 8 ms.",
        ],
        calculator_type="delay",
    )
