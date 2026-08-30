"""Past Exam 2023-2024 Scenario Module.

Contains all multiple choice questions, network delay calculations,
ARP tables, RIP routing configurations, and collision/broadcast domain analysis.
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
        NetworkScenario: The structured scenario object.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Στο πλαίσιο της τελικής εξέτασης του μαθήματος "),
                TextSegment(
                    text="Δίκτυα Υπολογιστών (Ακαδημαϊκό Έτος 2023-2024)",
                    is_highlight=True,
                    category="protocol",
                    tag_label="ΕΞΕΤΑΣΗ",
                    tooltip="Επίσημο γραπτό εξέτασης Τμήματος Πληροφορικής & Τηλεπικοινωνιών",
                ),
                TextSegment(text=", οι φοιτητές καλούνται να απαντήσουν σε ερωτήσεις πολλαπλής επιλογής και ασκήσεις που καλύπτουν "),
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
                    tag_label="ARP L2/L3",
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
                    text="Δρομολόγησης RIP v2",
                    is_highlight=True,
                    category="routing",
                    tag_label="ROUTING PROTOCOL",
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
        ExamQuestion(
            question_number=1,
            title="Τρόποι Ανταλλαγής Δεδομένων σε Κανάλι",
            question_type="Multiple Choice",
            prompt_text="Ποιο από τα ακόλουθα **δεν** ανήκει στους πιθανούς τρόπους ανταλλαγής δεδομένων όσον αφορά την κατεύθυνση και τη χρονικότητα της επικοινωνίας;",
            options=[
                QuestionOption("A", "Simplex", False, "Το Simplex είναι μονόδρομη επικοινωνία (π.χ. ραδιόφωνο)."),
                QuestionOption("B", "Multiplex (Πολυπλεξία)", True, "Η πολυπλεξία (Multiplexing) είναι τεχνική συνένωσης πολλαπλών σημάτων σε κοινό μέσο, όχι τρόπος/κατεύθυνση ανταλλαγής δεδομένων."),
                QuestionOption("C", "Half-duplex", False, "Το Half-duplex επιτρέπει αμφίδρομη επικοινωνία αλλά όχι ταυτόχρονα (π.χ. walkie-talkie)."),
                QuestionOption("D", "Full duplex", False, "Το Full-duplex επιτρέπει ταυτόχρονη αμφίδρομη επικοινωνία (π.χ. τηλεφωνία, σύγχρονο Ethernet)."),
            ],
            correct_option_letter="B",
            detailed_justification="Το Simplex, το Half-duplex και το Full-duplex περιγράφουν τη ροή των δεδομένων στο κανάλι. Η πολυπλεξία (FDM, TDM, WDM) είναι μέθοδος διαμοιρασμού του φυσικού μέσου.",
        ),
        ExamQuestion(
            question_number=2,
            title="Επίπεδο Λειτουργίας Επαναλήπτη (Repeater)",
            question_type="Multiple Choice",
            prompt_text="Σε ποιο επίπεδο του μοντέλου OSI λειτουργεί ο επαναλήπτης (Repeater);",
            options=[
                QuestionOption("A", "Physical layer (Επίπεδο 1)", True, "Ο επαναλήπτης λειτουργεί αποκλειστικά στο Φυσικό Επίπεδο (Layer 1). Αναπαράγει και ενισχύει ηλεκτρικά/οπτικά σήματα."),
                QuestionOption("B", "Data link layer (Επίπεδο 2)", False, "Στο Layer 2 λειτουργούν τα Switches και τα Bridges."),
                QuestionOption("C", "Network layer (Επίπεδο 3)", False, "Στο Layer 3 λειτουργούν οι Routers."),
                QuestionOption("D", "Transport layer (Επίπεδο 4)", False, "Στο Layer 4 λειτουργούν πρωτόκολλα όπως TCP/UDP."),
            ],
            correct_option_letter="A",
            detailed_justification="Ο επαναλήπτης (Repeater) δεν γνωρίζει έννοιες όπως MAC addresses ή IP packets. Η μοναδική του δουλειά είναι η αναγέννηση των bits που εξασθενούν λόγω απόστασης.",
        ),
        ExamQuestion(
            question_number=3,
            title="Λειτουργία Πρωτοκόλλου ARP & ARP Cache",
            question_type="Theory Analysis",
            prompt_text="Έστω υπολογιστής Α που θέλει να επικοινωνήσει με υπολογιστή C στο ίδιο LAN. Αναλύστε τον τύπο εκπομπής του ARP Request, του ARP Reply και τη λειτουργία της ARP Cache αν υπάρξει νέα αποστολή μετά από 5 λεπτά.",
            detailed_justification=(
                "1. **ARP Request:** Αποστέλλεται ως **Broadcast** (MAC: `FF:FF:FF:FF:FF:FF`). Όλοι οι κόμβοι στο LAN το λαμβάνουν και το εξετάζουν.\n"
                "2. **ARP Reply:** Ο κόμβος με την αντίστοιχη IP απαντά με **Unicast** απευθείας στον Α, καθώς γνωρίζει ήδη τη MAC του Α από το Request.\n"
                "3. **Επόμενη αποστολή μετά από 5 λεπτά:** **Δεν** θα εκτελεστεί ξανά ARP Request. Η αντιστοίχιση IP-MAC έχει αποθηκευτεί στην τοπική **ARP Cache** (συνήθης χρόνος διατήρησης 15-20 λεπτά)."
            ),
            common_pitfalls=[
                "Θεώρηση ότι το ARP Reply είναι Broadcast (ενώ είναι πάντα Unicast).",
                "Παράβλεψη της ύπαρξης της τοπικής μνήμης ARP Cache.",
            ],
        ),
        ExamQuestion(
            question_number=4,
            title="Διαχωρισμός Πεδίων Συγκρούσεων & Εκπομπής (Domains)",
            question_type="Multiple Choice",
            prompt_text="Επιλέξτε τη σωστή πρόταση σχετικά με τα Collision Domains και Broadcast Domains:",
            options=[
                QuestionOption("A", "Στην τοπολογία αστέρα με Switch, όλοι οι κόμβοι ανήκουν στο ίδιο collision domain.", False, "Κάθε θύρα του Switch αποτελεί ξεχωριστό collision domain."),
                QuestionOption("B", "Στην τοπολογία διαύλου (Bus), όλοι οι κόμβοι ανήκουν στο ίδιο collision domain.", True, "Στο κοινό ομοαξονικό καλώδιο, κάθε μετάδοση είναι ορατή από όλους και μπορεί να συγκρουστεί."),
                QuestionOption("C", "Ο δρομολογητής δεν διαχωρίζει broadcast domains.", False, "Ο δρομολογητής διαχωρίζει πάντα τα broadcast domains ανά θύρα."),
                QuestionOption("D", "Το Hub δημιουργεί ξεχωριστό collision domain ανά θύρα.", False, "Το Hub διατηρεί 1 ενιαίο collision domain."),
            ],
            correct_option_letter="B",
            detailed_justification="Στην τοπολογία διαύλου (Bus topology) όλοι οι υπολογιστές μοιράζονται το ίδιο φυσικό μέσο. Αντίθετα, στα switches έχουμε micro-segmentation όπου κάθε θύρα είναι απομονωμένο collision domain.",
        ),
    ]

    nodes = [
        TopologyNode("pc_a", "PC A", "host", 120, 150, "195.130.8.25", "00:25:64:D5:10:8B"),
        TopologyNode("sw_1", "Switch LAN", "switch", 320, 150),
        TopologyNode("router_1", "Router Core", "router", 540, 150, "195.130.8.1", "00:00:5E:00:10:01"),
        TopologyNode("cloud_1", "Internet WAN", "cloud", 740, 150, "172.16.1.1", "00:0B:14:E0:00:35"),
    ]

    links = [
        TopologyLink("pc_a", "sw_1", 100, 0.05, 2.0, "copper", "100M UTP"),
        TopologyLink("sw_1", "router_1", 1000, 0.1, 2.0, "copper", "1G Fiber/UTP"),
        TopologyLink("router_1", "cloud_1", 10000, 50.0, 2.0, "fiber", "10G WAN Link"),
    ]

    return NetworkScenario(
        id="exam_past_2023_2024",
        title="Θέματα Εξετάσεων (2023-2024)",
        subtitle="Επίσημο Γραπτό Εξέτασης: Delays, ARP Protocol, RIP Configuration & Domains",
        course_tag="Past Exam",
        duration_info="2 ώρες και 15 λεπτά",
        paragraphs=paragraphs,
        questions=questions,
        nodes=nodes,
        links=links,
        methodology_summary=[
            "1. Αναγνώριση επιπέδου λειτουργίας συσκευών δικτύου (Repeater L1, Switch L2, Router L3).",
            "2. Μοντέλο ανταλλαγής ARP (Request = Broadcast, Reply = Unicast, Cache = Temporary Memory).",
            "3. Διάκριση Collision Domain (ανά πόρτα switch) vs Broadcast Domain (ανά πόρτα router).",
        ],
        calculator_type="delay",
    )
