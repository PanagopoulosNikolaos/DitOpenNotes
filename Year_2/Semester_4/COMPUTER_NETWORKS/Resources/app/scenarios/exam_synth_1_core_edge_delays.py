"""Synthetic Exam 1: Core vs Edge, Delay Breakdown & Subnetting.

Covers OSI layer PDUs, Collision domains in Star topology,
d_trans calculations, IPv4 subnet matching (/25), statistical multiplexing,
and multi-hop delay derivations.
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
    """Constructs and returns Synthetic Exam 1 scenario.

    Returns:
        NetworkScenario: The structured scenario object.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Το πρότυπο δοκίμιο "),
                TextSegment(
                    text="Synthetic & Realistic Exam 1",
                    is_highlight=True,
                    category="protocol",
                    tag_label="SYNTHETIC EXAM",
                    tooltip="Ρεαλιστικό διαγώνισμα προσομοίωσης εξετάσεων",
                ),
                TextSegment(text=" επικεντρώνεται στη δομή των πρωτοκόλλων, στο "),
                TextSegment(
                    text="Data Link Layer (PDU: Frame)",
                    is_highlight=True,
                    category="protocol",
                    tag_label="L2 FRAME",
                    tooltip="Οργάνωση bits σε πλαίσια με MAC διευθύνσεις",
                ),
                TextSegment(text=", στον υπολογισμό "),
                TextSegment(
                    text="Collision Domains σε Switch (Micro-segmentation)",
                    is_highlight=True,
                    category="device",
                    tag_label="DOMAINS",
                    tooltip="1 Collision Domain ανά θύρα switch",
                ),
                TextSegment(text=" και στον ακριβή υπολογισμό της "),
                TextSegment(
                    text="Καθυστέρησης Μετάδοσης d_trans = L / R",
                    is_highlight=True,
                    category="delay",
                    tag_label="D_TRANS",
                    tooltip="L = 2000 bits, R = 1 Mbps -> d_trans = 2 ms",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="#e06b3a",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Επιπλέον εξετάζεται η εύρεση ορίων υποδικτύων για διεύθυνση "),
                TextSegment(
                    text="192.168.5.130/25",
                    is_highlight=True,
                    category="routing",
                    tag_label="SUBNET /25",
                    tooltip="Μάσκα 255.255.255.128, Block Size 128 (128-255)",
                ),
                TextSegment(text=" και η αρχή λειτουργίας της "),
                TextSegment(
                    text="Στατιστικής Πολυπλεξίας (Statistical Multiplexing)",
                    is_highlight=True,
                    category="protocol",
                    tag_label="STAT MULTIPLEX",
                    tooltip="Δυναμικός διαμοιρασμός εύρους ζώνης on-demand",
                ),
                TextSegment(text=" στη μεταγωγή πακέτου."),
            ]
        ),
    ]

    questions = [
        ExamQuestion(
            question_number=1,
            title="Μονάδα Δεδομένων Πρωτοκόλλου (PDU) στο Επίπεδο 2",
            question_type="Multiple Choice",
            prompt_text="Ποιο από τα παρακάτω επίπεδα του μοντέλου OSI χρησιμοποιεί ως PDU το **'Πλαίσιο' (Frame)**;",
            options=[
                QuestionOption("A", "Physical Layer (Επίπεδο 1)", False, "Το Physical Layer χρησιμοποιεί bits."),
                QuestionOption("B", "Data Link Layer (Επίπεδο 2)", True, "Το Data Link Layer οργανώνει τα bits σε πλαίσια (frames) με επικεφαλίδες MAC."),
                QuestionOption("C", "Network Layer (Επίπεδο 3)", False, "Το Network Layer χρησιμοποιεί πακέτα (packets/datagrams)."),
                QuestionOption("D", "Transport Layer (Επίπεδο 4)", False, "Το Transport Layer χρησιμοποιεί τμήματα (segments/datagrams)."),
            ],
            correct_option_letter="B",
            detailed_justification="Κάθε επίπεδο έχει τη δική του ονομασία PDU: L1=Bit, L2=Frame, L3=Packet, L4=Segment, L5-7=Message.",
        ),
        ExamQuestion(
            question_number=2,
            title="Πεδία Συγκρούσεων (Collision Domains) σε Switch",
            question_type="Multiple Choice",
            prompt_text="Σε ένα δίκτυο αστέρα (Star) που χρησιμοποιεί αποκλειστικά Switch, πόσα πεδία συγκρούσεων δημιουργούνται για 8 συνδεδεμένους υπολογιστές;",
            options=[
                QuestionOption("A", "1", False, "Αυτό θα ίσχυε μόνο αν χρησιμοποιούνταν παλιό Hub (Layer 1)."),
                QuestionOption("B", "8", True, "Κάθε φυσική θύρα του Switch αποτελεί ανεξάρτητο collision domain (micro-segmentation)."),
                QuestionOption("C", "4", False, "Δεν υπάρχει ομαδοποίηση ανά 2 θύρες."),
                QuestionOption("D", "0", False, "Κάθε ζεύξη είναι collision domain."),
            ],
            correct_option_letter="B",
            detailed_justification="Τα switches απομονώνουν την κίνηση ανά θύρα. Για 8 υπολογιστές σε 8 θύρες, υπάρχουν ακριβώς 8 πεδία συγκρούσεων.",
        ),
        ExamQuestion(
            question_number=3,
            title="Υπολογισμός d_trans για Πακέτο L = 2000 bits",
            question_type="Calculations",
            prompt_text="Η καθυστέρηση μετάδοσης (d_trans) ενός πακέτου μεγέθους L = 2000 bits σε μια ζεύξη με ρυθμό R = 1 Mbps είναι:",
            calculation_steps=[
                CalculationStep(
                    step_number=1,
                    title="Εφαρμογή Τύπου Μετάδοσης",
                    formula="d_trans = L / R",
                    substitution="2000 bits / (1 * 10^6 bps)",
                    result="2 * 10^-3 sec = 2 ms",
                    rationale="Μετατροπή 1 Mbps = 1.000.000 bps.",
                )
            ],
            detailed_justification="d_trans = 2000 / 10^6 = 0.002 s = 2 ms.",
        ),
        ExamQuestion(
            question_number=4,
            title="Ταύτιση Υποδικτύου IPv4 /25",
            question_type="Multiple Choice",
            prompt_text="Ποια από τις παρακάτω IP διευθύνσεις ανήκει στο ίδιο υποδίκτυο με την 192.168.5.130/25;",
            options=[
                QuestionOption("A", "192.168.5.10", False, "Ανήκει στο 1ο υποδίκτυο (.0 έως .127)."),
                QuestionOption("B", "192.168.5.200", True, "Η μάσκα /25 χωρίζει το C class σε δύο μπλοκ: 0-127 και 128-255. Το 130 και το 200 ανήκουν στο 2ο μπλοκ (128-255)."),
                QuestionOption("C", "192.168.5.255", False, "Αποτελεί τη διεύθυνση Broadcast του 2ου υποδικτύου (όχι διαθέσιμη για host)."),
                QuestionOption("D", "192.168.5.126", False, "Ανήκει στο 1ο υποδίκτυο (0-127)."),
            ],
            correct_option_letter="B",
            detailed_justification="Block size = 256 - 128 = 128. Υποδίκτυο 1: 192.168.5.0/25 (.1-.126), Υποδίκτυο 2: 192.168.5.128/25 (.129-.254). Το .200 είναι έγκυρος host στο ίδιο υποδίκτυο με το .130.",
        ),
    ]

    nodes = [
        TopologyNode("h1", "Host 1", "host", 100, 100, "192.168.5.130/25"),
        TopologyNode("h2", "Host 2", "host", 100, 200, "192.168.5.200/25"),
        TopologyNode("sw", "Switch L2", "switch", 350, 150),
        TopologyNode("r1", "Gateway Router", "router", 600, 150, "192.168.5.129/25"),
    ]

    links = [
        TopologyLink("h1", "sw", 100, 0.02, 2.0, "copper", "100M UTP"),
        TopologyLink("h2", "sw", 100, 0.02, 2.0, "copper", "100M UTP"),
        TopologyLink("sw", "r1", 1000, 0.05, 2.0, "copper", "1G UTP"),
    ]

    return NetworkScenario(
        id="exam_synth_1",
        title="Synthetic Exam 1: Core, Delays & Subnetting",
        subtitle="PDUs, Micro-segmentation, d_trans = L/R & /25 Subnet Boundaries",
        course_tag="Synthetic Exam",
        duration_info="2 ώρες και 15 λεπτά",
        paragraphs=paragraphs,
        questions=questions,
        nodes=nodes,
        links=links,
        methodology_summary=[
            "1. L2 PDU = Frame.",
            "2. Switch ports = 1 collision domain ανά πόρτα.",
            "3. d_trans = L / R = 2000 / 10^6 = 2 ms.",
            "4. /25 CIDR Subnetting: Block size 128 (Υποδίκτυο 128-255).",
        ],
        calculator_type="delay",
    )
