"""Past Exam 2023-2024 Scenario Module.

Contains 1-to-1 representation of all exam questions from the 2023-2024 paper:
- Part A: Modes of data exchange, network definition, repeater OSI layer, bridge utility,
  congestion causes, peer processes, and parity bits.
- Part B: Exercise 4 (ARP on subnet 137.196.7.0/24), Exercise 23 (Router gateway ARP),
  Exercise 24 (Cisco IOS RIPv2 configuration CLI), and Exercise 32 (Collision & Broadcast domains).
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
    """Constructs and returns the complete Past Exam 2023-2024 scenario.

    Returns:
        NetworkScenario: The structured scenario object with 1-to-1 parity.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Στο πλαίσιο της τελικής εξέτασης του μαθήματος "),
                TextSegment(
                    text="Δίκτυα Υπολογιστών (Ακαδημαϊκό Έτος 2023-2024)",
                    is_highlight=True,
                    category="protocol",
                    tag_label="ΕΞΕΤΑΣΗ 2023-2024",
                    tooltip="Επίσημο γραπτό εξέτασης Τμήματος Πληροφορικής & Τηλεπικοινωνιών",
                ),
                TextSegment(text=", οι φοιτητές εξετάζονται σε θέματα που καλύπτουν "),
                TextSegment(
                    text="τρόπους ανταλλαγής δεδομένων (Simplex, Duplex)",
                    is_highlight=True,
                    category="protocol",
                    tag_label="ΕΠΙΚΟΙΝΩΝΙΑ",
                    tooltip="Κατευθύνσεις και χρονισμός ροής δεδομένων",
                ),
                TextSegment(text=", λειτουργίες συσκευών φυσικού και ζευκτικού επιπέδου όπως "),
                TextSegment(
                    text="Repeater (Physical Layer)",
                    is_highlight=True,
                    category="device",
                    tag_label="L1 DEVICE",
                    tooltip="Αναπαράγει σήματα bit χωρίς ανάλυση πλαισίων",
                ),
                TextSegment(text=" και "),
                TextSegment(
                    text="Bridge (Data Link Layer)",
                    is_highlight=True,
                    category="device",
                    tag_label="L2 DEVICE",
                    tooltip="Συνδέει τμήματα LAN και απομονώνει collision domains",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="#e06b3a",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Στο πρακτικό μέρος εξετάζεται η λειτουργία του "),
                TextSegment(
                    text="Πρωτοκόλλου ARP (Address Resolution Protocol)",
                    is_highlight=True,
                    category="protocol",
                    tag_label="ARP PROTOCOL",
                    tooltip="Αντιστοίχιση λογικής διεύθυνσης IP σε φυσική MAC",
                ),
                TextSegment(text=" με αποστολή "),
                TextSegment(
                    text="ARP Request ως Broadcast",
                    is_highlight=True,
                    category="routing",
                    tag_label="BROADCAST",
                    tooltip="Αποστολή στη διεύθυνση FF:FF:FF:FF:FF:FF",
                ),
                TextSegment(text=" και "),
                TextSegment(
                    text="ARP Reply ως Unicast",
                    is_highlight=True,
                    category="routing",
                    tag_label="UNICAST",
                    tooltip="Απευθείας επιστροφή της MAC στον αιτούντα",
                ),
                TextSegment(text=", καθώς και διαμόρφωση "),
                TextSegment(
                    text="Δρομολόγησης RIP v2 σε Cisco IOS",
                    is_highlight=True,
                    category="routing",
                    tag_label="RIPV2 CISCO",
                    tooltip="Distance-Vector πρωτόκολλο με metric το hop count",
                ),
                TextSegment(text=" και διαχωρισμός "),
                TextSegment(
                    text="Collision & Broadcast Domains",
                    is_highlight=True,
                    category="device",
                    tag_label="DOMAINS",
                    tooltip="Οριοθέτηση πεδίων συγκρούσεων και εκπομπής",
                ),
                TextSegment(text=" σε τοπολογίες διαύλου και αστέρα."),
            ]
        ),
    ]

    questions = [
        # Part A - Question 1
        ExamQuestion(
            question_number=1,
            title="Τρόποι Ανταλλαγής Δεδομένων σε Κανάλι",
            question_type="Multiple Choice",
            prompt_text="Ποιο από τα ακόλουθα δεν ανήκει στους πιθανούς τρόπους ανταλλαγής δεδομένων;",
            options=[
                QuestionOption("A", "Simplex", False, "Το Simplex περιγράφει μονόδρομη επικοινωνία (π.χ. ραδιόφωνο)."),
                QuestionOption("B", "Multiplex", True, "Η πολυπλεξία (Multiplexing) είναι τεχνική συνένωσης πολλαπλών σημάτων σε κοινό μέσο και δεν περιγράφει κατεύθυνση επικοινωνίας."),
                QuestionOption("C", "Half-duplex", False, "Το Half-duplex επιτρέπει αμφίδρομη επικοινωνία αλλά όχι ταυτόχρονα (π.χ. walkie-talkie)."),
                QuestionOption("D", "Full duplex", False, "Το Full-duplex επιτρέπει ταυτόχρονη αμφίδρομη επικοινωνία (π.χ. τηλεφωνία)."),
            ],
            correct_option_letter="B",
            detailed_justification="Το Simplex, το Half-duplex και το Full-duplex περιγράφουν την κατεύθυνση και τη χρονικότητα με την οποία γίνεται η ανταλλαγή δεδομένων σε ένα κανάλι. Η πολυπλεξία (Multiplexing) είναι τεχνική συνένωσης πολλών σημάτων σε ένα κοινό μέσο και δεν περιγράφει κατεύθυνση επικοινωνίας.",
        ),
        # Part A - Question 2
        ExamQuestion(
            question_number=2,
            title="Ορισμός Δικτύου Υπολογιστών",
            question_type="Multiple Choice",
            prompt_text="Δίκτυο υπολογιστών είναι:",
            options=[
                QuestionOption("A", "Μια συλλογή από υλικά (hardware) συστατικά και υπολογιστές", False, "Αποτελεί μέρος του ορισμού, αλλά δεν καλύπτει τη σύνδεση και τον σκοπό."),
                QuestionOption("B", "Διασύνδεση με κανάλια επικοινωνίας", False, "Αποτελεί το μέσο διασύνδεσης, αλλά όχι τον πλήρη ορισμό."),
                QuestionOption("C", "Διαμοίραση πόρων και πληροφορίας", False, "Αποτελεί τον βασικό σκοπό του δικτύου."),
                QuestionOption("D", "Όλα τα παραπάνω", True, "Ένα δίκτυο αποτελείται από υλικό, διασυνδέεται μέσω καναλιών επικοινωνίας και εξυπηρετεί τη διαμοίραση πόρων και δεδομένων."),
            ],
            correct_option_letter="D",
            detailed_justification="Ένα δίκτυο υπολογιστών αποτελείται από υλικό (routers, switches, PCs), κανάλια επικοινωνίας (καλώδια, ασύρματες ζεύξεις) και έχει ως πρωταρχικό σκοπό τη διαμοίραση πόρων και πληροφοριών.",
        ),
        # Part A - Question 3
        ExamQuestion(
            question_number=3,
            title="Επίπεδο Λειτουργίας Επαναλήπτη (Repeater)",
            question_type="Multiple Choice",
            prompt_text="Σε ποιο επίπεδο του OSI λειτουργεί ο επαναλήπτης (Repeater);",
            options=[
                QuestionOption("A", "Physical layer (Επίπεδο 1)", True, "Ο επαναλήπτης αναπαράγει και ενισχύει ηλεκτρικά/οπτικά σήματα bits χωρίς ανάλυση πλαισίων ή πακέτων."),
                QuestionOption("B", "Data link layer (Επίπεδο 2)", False, "Στο Layer 2 λειτουργούν Bridges και Switches."),
                QuestionOption("C", "Network layer (Επίπεδο 3)", False, "Στο Layer 3 λειτουργούν οι δρομολογητές (Routers)."),
                QuestionOption("D", "Transport layer (Επίπεδο 4)", False, "Στο Layer 4 λειτουργούν πρωτόκολλα όπως TCP και UDP."),
            ],
            correct_option_letter="A",
            detailed_justification="Ο επαναλήπτης (Repeater) λειτουργεί αποκλειστικά στο φυσικό επίπεδο (Layer 1). Αναπαράγει και ενισχύει τα ηλεκτρικά/οπτικά σήματα (bits) χωρίς να εξετάζει κεφαλίδες πλαισίων (MAC) ή πακέτων (IP).",
        ),
        # Part A - Question 4
        ExamQuestion(
            question_number=4,
            title="Χρήση της Γέφυρας (Bridge) στο Δίκτυο",
            question_type="Multiple Choice",
            prompt_text="Ποια είναι η χρήση της γέφυρας (Bridge) στο δίκτυο;",
            options=[
                QuestionOption("A", "Σύνδεση LANs", False, "Συνδέει τμήματα LAN, αλλά ισχύουν και τα υπόλοιπα."),
                QuestionOption("B", "Να ξεχωρίσει LANs", False, "Απομονώνει τμήματα δικτύου χωρίζοντας collision domains."),
                QuestionOption("C", "Να έχει τον έλεγχο της ταχύτητας στο δίκτυο", False, "Μειώνει τη συμφόρηση περιορίζοντας τις συγκρούσεις."),
                QuestionOption("D", "Όλα τα παραπάνω", True, "Η γέφυρα συνδέει LAN segments, φιλτράρει κίνηση βάσει MAC, διαχωρίζει collision domains και βελτιώνει την ταχύτητα/απόδοση."),
            ],
            correct_option_letter="D",
            detailed_justification="Η γέφυρα (Bridge) λειτουργεί στο Επίπεδο 2 (Data Link Layer). Συνδέει πολλαπλά LAN segments (Α) και φιλτράρει την κίνηση βάσει MAC διευθύνσεων, χωρίζοντας έτσι ένα μεγάλο collision domain σε μικρότερα (Β). Η μείωση των συγκρούσεων βελτιώνει την πραγματική ταχύτητα και απόδοση του δικτύου (Γ).",
        ),
        # Part A - Question 5
        ExamQuestion(
            question_number=5,
            title="Αιτία Συμφόρησης (Congestion)",
            question_type="Multiple Choice",
            prompt_text="Σε ένα δίκτυο εμφανίζεται συμφόρηση όταν:",
            options=[
                QuestionOption("A", "Υπερβολική κίνηση", True, "Όταν ο ρυθμός άφιξης πακέτων υπερβαίνει την ικανότητα επεξεργασίας/εξόδου, γεμίζοντας τους buffers."),
                QuestionOption("B", "Όταν ένα σύστημα τερματίσει", False, "Ο τερματισμός ενός host δεν προκαλεί από μόνος του συμφόρηση."),
                QuestionOption("C", "Όταν η σύνδεση μεταξύ δύο κόμβων τερματιστεί", False, "Η διακοπή ζεύξης προκαλεί αποσύνδεση ή επαναδρομολόγηση, όχι συμφόρηση καθεαυτή."),
                QuestionOption("D", "Κανένα από τα παραπάνω", False, "Η υπερβολική κίνηση είναι η βασική αιτία συμφόρησης."),
            ],
            correct_option_letter="A",
            detailed_justification="Η συμφόρηση (congestion) προκαλείται όταν τα πακέτα καταφθάνουν σε ένα δρομολογητή/μεταγωγέα με ρυθμό μεγαλύτερο από αυτόν που μπορεί να εξυπηρετήσει, οδηγώντας σε γέμισμα των ουρών αναμονής (buffers) και εν τέλει σε απόρριψη πακέτων (packet loss).",
        ),
        # Part A - Question 6
        ExamQuestion(
            question_number=6,
            title="Ομότιμες Διαδικασίες (Peer-to-Peer Processes)",
            question_type="Multiple Choice",
            prompt_text="Έστω δύο μηχανές που επικοινωνούν μεταξύ τους. Η διαδικασία που επικοινωνεί με ένα συγκεκριμένο επίπεδο σε κάθε μηχανή καλείται:",
            options=[
                QuestionOption("A", "UDP process", False, "Αφορά συγκεκριμένο πρωτόκολλο μεταφοράς."),
                QuestionOption("B", "Intranet process", False, "Αφορά τοπικό ιδιωτικό δίκτυο."),
                QuestionOption("C", "Server", False, "Αφορά ρόλο εξυπηρετητή στο Network Edge."),
                QuestionOption("D", "Peer-peer process (Ομότιμη Διαδικασία)", True, "Οντότητες στο ίδιο ακριβώς επίπεδο της στοίβας πρωτοκόλλων καλούνται ομότιμες (peer processes)."),
            ],
            correct_option_letter="D",
            detailed_justification="Στην αρχιτεκτονική δικτύων (π.χ. μοντέλο OSI), οντότητες που βρίσκονται στο ίδιο επίπεδο σε διαφορετικούς κόμβους (π.χ. Transport layer στον αποστολέα και Transport layer στον παραλήπτη) ονομάζονται ομότιμες διαδικασίες (peer-to-peer processes).",
        ),
        # Part A - Question 7 (Unnumbered in exam)
        ExamQuestion(
            question_number=7,
            title="Χρήση των Parity Bits (Bits Ισοτιμίας)",
            question_type="Multiple Choice",
            prompt_text="Τα 'Parity bits' χρησιμοποιούνται για τον ακόλουθο σκοπό:",
            options=[
                QuestionOption("A", "Κρυπτογράφηση δεδομένων", False, "Η κρυπτογράφηση απαιτεί αλγορίθμους όπως AES/RSA."),
                QuestionOption("B", "Ταχύτερη μετάδοση δεδομένων", False, "Η προσθήκη bits ισοτιμίας αυξάνει ελαφρώς το overhead."),
                QuestionOption("C", "Ανίχνευση λαθών (Error Detection)", True, "Τα bits ισοτιμίας χρησιμοποιούνται για τον εντοπισμό μονού αριθμού σφαλμάτων bit."),
                QuestionOption("D", "Αναγνώριση χρήσης", False, "Δεν σχετίζονται με authentication ή accounting."),
            ],
            correct_option_letter="C",
            detailed_justification="Τα bits ισοτιμίας (parity bits) είναι η απλούστερη μορφή ελέγχου σφαλμάτων και χρησιμοποιούνται αποκλειστικά για την ανίχνευση λαθών (error detection) κατά τη μετάδοση.",
        ),
        # Part B - Exercise 4
        ExamQuestion(
            question_number=8,
            title="Άσκηση 4: Ανάλυση Πρωτοκόλλου ARP σε Τοπικό Δίκτυο LAN",
            question_type="Theory Analysis",
            prompt_text=(
                "Για το δίκτυο LAN `137.196.7.0/24`, υποθέστε ότι ο υπολογιστής A (`137.196.7.23`, `71-65-F7-2B-08-53`) "
                "επιθυμεί να επικοινωνήσει με τον υπολογιστή C (`137.196.7.14`, `58-23-D7-FA-20-B0`) για τον οποίο γνωρίζει "
                "την IP αλλά όχι την MAC address. Στο LAN συνδέονται επίσης ο B (`137.196.7.88`) και ο D (`137.196.7.78`).\n\n"
                "**Ερωτήματα:**\n"
                "**a.** Ποια είναι τα στοιχεία των μηνυμάτων ARP Request και ARP Reply που ανταλλάσσουν οι δύο συσκευές;\n"
                "**b.** Ποιο είναι το είδος της εκπομπής (Broadcast ή Unicast) για το Request και ποιο για το Reply;\n"
                "**c.** Αν μετά από 5 λεπτά ο C θέλει να στείλει πακέτο στον A, θα χρησιμοποιήσει ξανά το ARP;"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Μήνυμα ARP Request (Αίτημα Υπολογιστή A)",
                    formula="ARP_Request = [Sender_MAC, Sender_IP, Target_MAC, Target_IP]",
                    substitution="Sender MAC: 71-65-F7-2B-08-53 | Sender IP: 137.196.7.23 | Target MAC: 00:00:00:00:00:00 | Target IP: 137.196.7.14",
                    result="L2 Frame Dest MAC: FF:FF:FF:FF:FF:FF (Broadcast)",
                    rationale="Ο υπολογιστής A δεν γνωρίζει τη φυσική διεύθυνση του C, επομένως θέτει το Target MAC σε μηδενικά στο σώμα του ARP και στέλνει το πλαίσιο σε εκπομπή.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Μήνυμα ARP Reply (Απάντηση Υπολογιστή C)",
                    formula="ARP_Reply = [Sender_MAC, Sender_IP, Target_MAC, Target_IP]",
                    substitution="Sender MAC: 58-23-D7-FA-20-B0 | Sender IP: 137.196.7.14 | Target MAC: 71-65-F7-2B-08-53 | Target IP: 137.196.7.23",
                    result="L2 Frame Dest MAC: 71-65-F7-2B-08-53 (Unicast)",
                    rationale="Ο υπολογιστής C αναγνωρίζει την IP του, καταγράφει τη MAC του A από το Request και απαντά απευθείας στον A.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Είδος Εκπομπής και Μνήμη ARP Cache",
                    formula="Request = Broadcast (FF-FF-FF-FF-FF-FF) | Reply = Unicast",
                    substitution="Χρόνος αποθήκευσης cache: 15-20 λεπτά > 5 λεπτά",
                    result="Όχι νέα αποστολή ARP",
                    rationale="Η αντιστοίχιση IP-MAC παραμένει έγκυρη στην ARP Cache του κόμβου C για τουλάχιστον 15-20 λεπτά, οπότε το πακέτο αποστέλλεται άμεσα.",
                ),
            ],
            detailed_justification=(
                "1. **Στοιχεία ARP Request:** Sender MAC: `71-65-F7-2B-08-53`, Sender IP: `137.196.7.23`, Target MAC: `00:00:00:00:00:00`, Target IP: `137.196.7.14`.\n"
                "2. **Στοιχεία ARP Reply:** Sender MAC: `58-23-D7-FA-20-B0`, Sender IP: `137.196.7.14`, Target MAC: `71-65-F7-2B-08-53`, Target IP: `137.196.7.23`.\n"
                "3. **Τύπος μετάδοσης:** Το ARP Request είναι **Broadcast** (`FF-FF-FF-FF-FF-FF`) ώστε να το λάβουν όλοι οι κόμβοι στο LAN segment. Το ARP Reply είναι **Unicast** απευθείας προς τον A.\n"
                "4. **Επαναχρησιμοποίηση:** **Όχι**, ο C δεν θα εκτελέσει ξανά ARP. Η αντιστοίχιση διατηρείται στην **ARP Cache**."
            ),
            common_pitfalls=[
                "Θεώρηση ότι το ARP Reply αποστέλλεται επίσης ως Broadcast.",
                "Ξέχασμα ότι το Target MAC στο Request είναι άγνωστο και τίθεται ως 00:00:00:00:00:00.",
                "Παράλειψη της λειτουργίας της τοπικής μνήμης ARP Cache.",
            ],
        ),
        # Part B - Exercise 23
        ExamQuestion(
            question_number=9,
            title="Άσκηση 23: Ανταλλαγή ARP μεταξύ Υπολογιστή και Gateway Router",
            question_type="Calculations",
            prompt_text=(
                "Συμπληρώστε τα στοιχεία του μηνύματος ARP που ανταλλάσσουν οι δύο συσκευές:\n"
                "```text\n"
                "    [PC] ---------------------------------- ( Router ) ----------- ( Internet )\n"
                " IP: 195.130.8.25                     IP: 195.130.8.1     IP: 172.16.1.1\n"
                " MAC: 00:25:64:D5:10:8B               MAC: 00:00:5E:00:10:01   MAC: 00:0B:14:E0:00:35\n"
                "```\n"
                "Ο υπολογιστής επιθυμεί να επικοινωνήσει με εξωτερικό κόμβο στο Internet μέσω του προεπιλεγμένου δρομολογητή (Gateway)."
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Αίτημα Υπολογιστή (PC ARP Request)",
                    formula="ARP_Request = [Sender_MAC, Sender_IP, Target_MAC, Target_IP]",
                    substitution="Sender MAC: 00:25:64:D5:10:8B | Sender IP: 195.130.8.25 | Target MAC: 00:00:00:00:00:00 | Target IP: 195.130.8.1",
                    result="Αποστολή στο L2 Broadcast FF:FF:FF:FF:FF:FF",
                    rationale="Ο υπολογιστής αναζητά τη φυσική διεύθυνση της προεπιλεγμένης πύλης (195.130.8.1) για να της προωθήσει τα πακέτα.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Απάντηση Δρομολογητή (Router ARP Reply)",
                    formula="ARP_Reply = [Sender_MAC, Sender_IP, Target_MAC, Target_IP]",
                    substitution="Sender MAC: 00:00:5E:00:10:01 | Sender IP: 195.130.8.1 | Target MAC: 00:25:64:D5:10:8B | Target IP: 195.130.8.25",
                    result="Unicast απάντηση προς τη MAC του PC",
                    rationale="Ο δρομολογητής επιστρέφει τη δική του MAC διεύθυνση (00:00:5E:00:10:01) στο τοπικό LAN interface.",
                ),
            ],
            detailed_justification=(
                "Για να στείλει πακέτο προς το Internet, το PC διαπιστώνει ότι η IP προορισμού δεν ανήκει στο τοπικό υποδίκτυο. "
                "Επομένως, αναζητά τη MAC διεύθυνση της πύλης εξόδου (Default Gateway `195.130.8.1`).\n\n"
                "**Αίτημα Υπολογιστή (ARP Request):**\n"
                "- Sender MAC: `00:25:64:D5:10:8B`\n"
                "- Sender IP: `195.130.8.25`\n"
                "- Target MAC: `00:00:00:00:00:00`\n"
                "- Target IP: `195.130.8.1`\n\n"
                "**Απάντηση Δρομολογητή (Router ARP Reply):**\n"
                "- Sender MAC: `00:00:5E:00:10:01`\n"
                "- Sender IP: `195.130.8.1`\n"
                "- Target MAC: `00:25:64:D5:10:8B`\n"
                "- Target IP: `195.130.8.25`"
            ),
        ),
        # Part B - Exercise 24
        ExamQuestion(
            question_number=10,
            title="Άσκηση 24: Διαμόρφωση Δρομολόγησης RIP Version 2 σε Cisco IOS",
            question_type="Calculations",
            prompt_text=(
                "Για το δίκτυο της εικόνας ορίστε δρομολόγηση RIP version 2 συμπληρώνοντας τα κενά:\n"
                "```text\n"
                "        10.15.2.0/24\n"
                "             \\\n"
                "              \\ Se0/1/1\n"
                "   Se0/0/0 +---( 1841 )---+ Fa0/0\n"
                "  ---------+              +---------\n"
                " 10.15.3.0/24             10.15.6.0/24\n"
                "```\n"
                "**Κενά προς συμπλήρωση στη γραμμή εντολών (CLI):**\n"
                "```text\n"
                "R>en\n"
                "R# __________________________________\n"
                "R(config)# __________________________\n"
                "R(config-router)# ___________________\n"
                "R(config-router)# ___________________\n"
                "R(config-router)# ___________________\n"
                "R(config-router)# ___________________\n"
                "R(config-router)# ___________________\n"
                "R(config-router)# ___________________\n"
                "```"
            ),
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Είσοδος σε Global Configuration Mode",
                    formula="R# configure terminal",
                    substitution="configure terminal (ή conf t)",
                    result="R(config)#",
                    rationale="Απαραίτητο βήμα για μετάβαση από Privileged EXEC mode σε Global Configuration mode.",
                ),
                CalculationStep(
                    step_number=2,
                    title="Ενεργοποίηση Πρωτοκόλλου RIP",
                    formula="R(config)# router rip",
                    substitution="router rip",
                    result="R(config-router)#",
                    rationale="Ξεκινά τη διαδικασία διαμόρφωσης της δρομολόγησης RIP.",
                ),
                CalculationStep(
                    step_number=3,
                    title="Ορισμός RIP Version 2 & Απενεργοποίηση Αυτόματης Συνοψίσεως",
                    formula="version 2  &&  no auto-summary",
                    substitution="version 2 | no auto-summary",
                    result="Classless routing υποστήριξη",
                    rationale="Η έκδοση 2 υποστηρίζει μάσκες υποδικτύου μεταβλητού μήκους (VLSM/CIDR). Η εντολή no auto-summary αποτρέπει τη σύνοψη στα classful όρια.",
                ),
                CalculationStep(
                    step_number=4,
                    title="Δήλωση Απευθείας Συνδεδεμένων Δικτύων",
                    formula="network <network_address>",
                    substitution="network 10.15.2.0 | network 10.15.3.0 | network 10.15.6.0",
                    result="Ενεργοποίηση RIP στα interfaces Se0/1/1, Se0/0/0, Fa0/0",
                    rationale="Ενημερώνει τον δρομολογητή να διαφημίζει αυτά τα υποδίκτυα και να στέλνει/λαμβάνει RIP updates στις αντίστοιχες θύρες.",
                ),
                CalculationStep(
                    step_number=5,
                    title="Έξοδος από το Configuration Mode",
                    formula="end (ή exit)",
                    substitution="end",
                    result="R#",
                    rationale="Επιστροφή στο προνομιακό περιβάλλον διαχείρισης.",
                ),
            ],
            detailed_justification=(
                "Η πλήρης ακολουθία εντολών Cisco IOS για την άσκηση είναι:\n"
                "```text\n"
                "R>en\n"
                "R# configure terminal\n"
                "R(config)# router rip\n"
                "R(config-router)# version 2\n"
                "R(config-router)# no auto-summary\n"
                "R(config-router)# network 10.15.2.0\n"
                "R(config-router)# network 10.15.3.0\n"
                "R(config-router)# network 10.15.6.0\n"
                "R(config-router)# end\n"
                "```"
            ),
            common_pitfalls=[
                "Παράλειψη της εντολής version 2 (προεπιλογή είναι το RIPv1 που είναι classful).",
                "Παράλειψη της εντολής no auto-summary που προκαλεί ανεπιθύμητη σύνοψη σε Class A /8.",
                "Εισαγωγή μάσκας υποδικτύου στις εντολές network (το RIP στο Cisco IOS δέχεται μόνο network ID χωρίς μάσκα).",
            ],
        ),
        # Part B - Exercise 32
        ExamQuestion(
            question_number=11,
            title="Άσκηση 32: Ανάλυση Collision και Broadcast Domains (Σωστό/Λάθος)",
            question_type="Multiple Choice",
            prompt_text=(
                "Επιλέξτε Σωστό (Σ) ή Λάθος (Λ) για τις ακόλουθες προτάσεις σχετικά με τοπολογίες δικτύου και domains:\n\n"
                "1. Στην τοπολογία διαύλου (Bus), όλοι οι κόμβοι βρίσκονται στο ίδιο πεδίο συγκρούσεων (collision domain).\n"
                "2. Στην τοπολογία αστέρα (Star), όλοι οι κόμβοι βρίσκονται στο ίδιο πεδίο συγκρούσεων (collision domain).\n"
                "3. Στην τοπολογία αστέρα (Star), κάθε ζεύξη είναι από μόνη της πεδίο συγκρούσεων (collision domain).\n"
                "4. Κάθε φυσική θύρα του δρομολογητή ορίζει ένα πεδίο εκπομπής (broadcast domain)."
            ),
            options=[
                QuestionOption("A", "1: Σ, 2: Σ, 3: Λ, 4: Σ", False, "Η πρόταση 2 είναι λάθος στα σύγχρονα αστέρια με Switch."),
                QuestionOption("B", "1: Σ, 2: Λ, 3: Σ, 4: Σ", True, "1=Σ (Κοινό μέσο διαύλου), 2=Λ (Το switch απομονώνει συγκρούσεις), 3=Σ (Micro-segmentation ανά θύρα), 4=Σ (Ο router τερματίζει τα L2 broadcasts)."),
                QuestionOption("C", "1: Λ, 2: Λ, 3: Σ, 4: Λ", False, "Ο δίαυλος μοιράζεται το μέσο και ο router διαχωρίζει broadcast domains."),
                QuestionOption("D", "1: Σ, 2: Λ, 3: Λ, 4: Σ", False, "Στην τοπολογία αστέρα με switch, κάθε ζεύξη είναι πράγματι ξεχωριστό collision domain."),
            ],
            correct_option_letter="B",
            detailed_justification=(
                "Αναλυτική αιτιολόγηση κάθε πρότασης:\n"
                "1. **Σωστό:** Στην τοπολογία διαύλου (Bus) όλοι οι υπολογιστές μοιράζονται το ίδιο φυσικό μέσο (π.χ. ομοαξονικό καλώδιο 10BASE2). Οποιαδήποτε ταυτόχρονη εκπομπή προκαλεί σύγκρουση.\n"
                "2. **Λάθος:** Στα σύγχρονα δίκτυα αστέρα χρησιμοποιούνται Switches, όπου κάθε θύρα αποτελεί ξεχωριστό collision domain (θα ίσχυε μόνο αν χρησιμοποιούνταν παλιό Hub).\n"
                "3. **Σωστό:** Κάθε μικρο-τμήμα (micro-segment) που συνδέεται σε switch port απομονώνει πλήρως τις συγκρούσεις.\n"
                "4. **Σωστό:** Οι δρομολογητές (Routers) διακόπτουν τα broadcasts του Layer 2. Κάθε interface συνδέεται σε διαφορετικό υποδίκτυο και ορίζει ένα ανεξάρτητο broadcast domain."
            ),
        ),
    ]

    nodes = [
        TopologyNode("pc_a", "Host A (Client)", "host", 100, 150, "137.196.7.23", "71-65-F7-2B-08-53"),
        TopologyNode("sw_lan", "Switch LAN 137.196.7.0/24", "switch", 340, 150),
        TopologyNode("pc_c", "Host C (Target)", "host", 580, 80, "137.196.7.14", "58-23-D7-FA-20-B0"),
        TopologyNode("pc_b", "Host B", "host", 580, 220, "137.196.7.88", "0C-C4-11-6F-E3-98"),
        TopologyNode("r_1841", "Cisco 1841 (RIPv2)", "router", 820, 150, "10.15.6.1", "00:00:5E:00:10:01"),
    ]

    links = [
        TopologyLink("pc_a", "sw_lan", 100, 0.05, 2.0, "copper", "100M UTP"),
        TopologyLink("sw_lan", "pc_c", 100, 0.05, 2.0, "copper", "100M UTP"),
        TopologyLink("sw_lan", "pc_b", 100, 0.05, 2.0, "copper", "100M UTP"),
        TopologyLink("sw_lan", "r_1841", 1000, 0.1, 2.0, "copper", "Fa0/0 (10.15.6.0/24)"),
    ]

    return NetworkScenario(
        id="exam_past_2023_2024",
        title="Θέματα Εξετάσεων (2023-2024)",
        subtitle="Επίσημο Γραπτό: Simplex/Duplex, OSI Layers, ARP Exchange, RIPv2 CLI & Domains",
        course_tag="Past Exam",
        duration_info="2 ώρες και 15 λεπτά",
        paragraphs=paragraphs,
        questions=questions,
        nodes=nodes,
        links=links,
        methodology_summary=[
            "1. Αναγνώριση επιπέδου λειτουργίας συσκευών: Repeater (L1), Bridge/Switch (L2), Router (L3).",
            "2. Μοντέλο ανταλλαγής ARP: Request = Broadcast (FF:FF:FF:FF:FF:FF), Reply = Unicast, Cache = Temporary Memory.",
            "3. Διαμόρφωση Cisco RIPv2: router rip -> version 2 -> no auto-summary -> network declarations.",
            "4. Οριοθέτηση domains: 1 Collision domain ανά switch port, 1 Broadcast domain ανά router interface.",
        ],
        calculator_type="delay",
    )
