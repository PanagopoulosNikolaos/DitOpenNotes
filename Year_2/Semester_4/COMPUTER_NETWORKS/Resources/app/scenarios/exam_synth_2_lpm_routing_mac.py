"""Synthetic Exam 2: Longest Prefix Match, Forwarding Tables & ARP.

Covers Network Core components, Longest Prefix Match (LPM) rules,
Data Plane vs Control Plane, Count-to-Infinity in Distance Vector,
Cumulative ACKs in TCP, and Forwarding Table lookups.
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
    """Constructs and returns Synthetic Exam 2 scenario.

    Returns:
        NetworkScenario: The structured scenario object.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Το πρότυπο δοκίμιο "),
                TextSegment(
                    text="Synthetic & Realistic Exam 2",
                    is_highlight=True,
                    category="protocol",
                    tag_label="SYNTHETIC EXAM",
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
                TextSegment(text=" και η απομόνωση των "),
                TextSegment(
                    text="Collision Domains ανά θύρα Switch",
                    is_highlight=True,
                    category="device",
                    tag_label="SWITCH L2",
                    tooltip="Διαχωρισμός collision domains χωρίς διαχωρισμό broadcast",
                ),
                TextSegment(text="."),
            ]
        ),
    ]

    questions = [
        ExamQuestion(
            question_number=1,
            title="Στοιχεία Πυρήνα του Δικτύου (Network Core)",
            question_type="Multiple Choice",
            prompt_text="Ποιο από τα παρακάτω ανήκει αποκλειστικά στον **πυρήνα του δικτύου (Network Core)**;",
            options=[
                QuestionOption("A", "Web Servers", False, "Οι servers βρίσκονται στα άκρα του δικτύου (Network Edge)."),
                QuestionOption("B", "Δρομολογητές (Routers)", True, "Ο πυρήνας αποτελείται από routers και switches που διασυνδέουν τα δίκτυα."),
                QuestionOption("C", "Κινητά τηλέφωνα (Smartphones)", False, "Είναι τελικά συστήματα (hosts) στο Network Edge."),
                QuestionOption("D", "Εφαρμογές Email (Clients)", False, "Εκτελούνται στα τελικά συστήματα."),
            ],
            correct_option_letter="B",
            detailed_justification="Ο πυρήνας (Network Core) αποτελείται από το πλέγμα των διασυνδεδεμένων δρομολογητών και μεταγωγέων που προωθούν δεδομένα.",
        ),
        ExamQuestion(
            question_number=2,
            title="Κανόνας Longest Prefix Match (LPM)",
            question_type="Multiple Choice",
            prompt_text="Σύμφωνα με τον κανόνα Longest Prefix Match (LPM), όταν μια διεύθυνση προορισμού ταιριάζει σε πολλαπλές εγγραφές του πίνακα προώθησης, ποια εγγραφή επιλέγεται;",
            options=[
                QuestionOption("A", "Η εγγραφή με το μικρότερο αριθμό bits στο prefix.", False, "Το μικρότερο πρόθεμα είναι πιο γενικό και απορρίπτεται."),
                QuestionOption("B", "Η εγγραφή με το μεγαλύτερο αριθμό bits στο prefix.", True, "Το μεγαλύτερο πρόθεμα είναι το πιο ειδικό (specific) και υπερισχύει πάντοτε."),
                QuestionOption("C", "Η προεπιλεγμένη διαδρομή (default route 0.0.0.0/0).", False, "Η default route επιλέγεται μόνο όταν κανένα άλλο prefix δεν ταιριάζει."),
                QuestionOption("D", "Η πρώτη εγγραφή που βρίσκεται τυχαία στον πίνακα.", False, "Η σειρά στον πίνακα δεν καθορίζει την επιλογή στο LPM."),
            ],
            correct_option_letter="B",
            detailed_justification="Το Longest Prefix Match επιλέγει την εγγραφή με τη μεγαλύτερη μάσκα υποδικτύου (π.χ. το /28 υπερισχύει του /24 και του /16).",
        ),
        ExamQuestion(
            question_number=3,
            title="Ρόλος του Data Plane έναντι του Control Plane",
            question_type="Multiple Choice",
            prompt_text="Το Data Plane ενός δρομολογητή είναι υπεύθυνο για:",
            options=[
                QuestionOption("A", "Την εκτέλεση του αλγορίθμου Dijkstra.", False, "Ανήκει στο Control Plane."),
                QuestionOption("B", "Τη φυσική προώθηση των πακέτων από την είσοδο στην έξοδο (forwarding).", True, "Το Data Plane υλοποιείται σε hardware (ASIC/TCAM) για ταχύτατη προώθηση ανά nanoseconds."),
                QuestionOption("C", "Την ανταλλαγή μηνυμάτων OSPF με άλλους δρομολογητές.", False, "Ανήκει στο Control Plane."),
                QuestionOption("D", "Τη διατήρηση του Routing Table (RIB).", False, "Ανήκει στο Control Plane."),
            ],
            correct_option_letter="B",
            detailed_justification="Διάκριση: Forwarding (Data Plane - τοπική προώθηση σε hardware) vs Routing (Control Plane - παγκόσμιος υπολογισμός διαδρομών με αλγορίθμους).",
        ),
        ExamQuestion(
            question_number=4,
            title="Πρόβλημα Count-to-Infinity σε Αλγορίθμους Δρομολόγησης",
            question_type="Multiple Choice",
            prompt_text="Το πρόβλημα 'Count-to-Infinity' είναι μια γνωστή αδυναμία στους αλγόριθμους δρομολόγησης τύπου:",
            options=[
                QuestionOption("A", "Link State (Κατάστασης Ζεύξης - Dijkstra)", False, "Το Link-State έχει καθολική γνώση και δεν υποφέρει από Count-to-Infinity."),
                QuestionOption("B", "Distance Vector (Διάνυσμα Απόστασης - Bellman-Ford)", True, "Λόγω της αργής διάδοσης κακών ειδήσεων (bad news travel slow), οι κόμβοι δημιουργούν βρόχους αυξάνοντας το κόστος στο άπειρο."),
                QuestionOption("C", "Longest Prefix Match", False, "Το LPM είναι μέθοδος αναζήτησης IP, όχι αλγόριθμος δρομολόγησης."),
                QuestionOption("D", "CSMA/CD", False, "Είναι πρωτόκολλο πολλαπλής πρόσβασης στο Layer 2."),
            ],
            correct_option_letter="B",
            detailed_justification="Στους Distance Vector αλγορίθμους (π.χ. RIP), χρησιμοποιούνται τεχνικές όπως Split Horizon και Poison Reverse για να μετριαστεί το Count-to-Infinity.",
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
        subtitle="Network Core, Longest Prefix Match, Data Plane & Count-to-Infinity",
        course_tag="Synthetic Exam",
        duration_info="2 ώρες και 15 λεπτά",
        paragraphs=paragraphs,
        questions=questions,
        nodes=nodes,
        links=links,
        methodology_summary=[
            "1. Routers = Network Core (Data plane forwarding).",
            "2. LPM: Μεγαλύτερο μήκος prefix = Πιο ειδική διαδρομή.",
            "3. Distance-Vector: Count-to-Infinity (Αργή σύγκλιση σε αστοχία).",
        ],
        calculator_type="lpm",
    )
