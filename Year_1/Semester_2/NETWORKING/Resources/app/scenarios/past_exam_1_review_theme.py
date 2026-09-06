"""Past/Practice Exam Paper 1 (Review Theme) scenario module.

Contains the COMPLETE original exam paper transcribed verbatim (every
Themata, sub-question, given parameter, and boundary condition, in the exact
original order) together with fully worked, step-by-step solutions for all
four Themata. The source paper ships indicative solutions only for Themata
1 and 2; this scenario extends them and completes Themata 3 and 4.
"""

from models.scenario import (
    Scenario,
    ExamMeta,
    Paragraph,
    TextSegment,
    GivenParameter,
    QuestionOption,
    CalculationStep,
    AnalysisRow,
    AnalysisTable,
    ProtocolLayer,
    DiagramNode,
    DiagramEdge,
    DesignJustification,
    ExamQuestion,
)


def createPastExam1Scenario() -> Scenario:
    """Constructs and returns the Past Exam 1 (Review Theme) scenario.

    Returns:
        Scenario: Fully populated scenario instance.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(
                    text="<strong>Επαναληπτικό Θέμα Εξετάσεων: Δίκτυα Υπολογιστών</strong>",
                    is_highlight=True,
                    category="term",
                    tag_label="ΕΞΕΤΑΣΗ",
                    badge_class="badge-term",
                    tooltip="Ταξινόμηση: Επαναληπτικό (πρότυπο) θέμα εξετάσεων του μαθήματος. Εντοπισμός: Τίτλος του εγγράφου της εξέτασης. Εφαρμογή: Δίνει τη δομή 4 Θεμάτων × 2.5 μονάδων που ακολουθεί ολόκληρο το φύλλο.",
                ),
            ],
            accent_border_color="accent",
        ),
        Paragraph(
            segments=[
                TextSegment(text="<strong>Οδηγίες:</strong> Διάρκεια εξέτασης: "),
                TextSegment(
                    text="2.5 ώρες",
                    is_highlight=True,
                    category="given",
                    tag_label="ΔΕΔΟΜΕΝΟ",
                    badge_class="badge-given",
                    tooltip="Ταξινόμηση: Χρονικό όριο εξέτασης. Εντοπισμός: Επίσημη οδηγία στο εισαγωικό τμήμα του θέματος. Εφαρμογή: Καθορίζει ρυθμό ~35 λεπτά ανά Θέμα για τέσσερα θέματα.",
                ),
                TextSegment(text=". "),
                TextSegment(
                    text="Όλα τα θέματα βαθμολογούνται με 2.5 μονάδες",
                    is_highlight=True,
                    category="given",
                    tag_label="ΒΑΘΜΟΛΟΓΙΑ",
                    badge_class="badge-given",
                    tooltip="Ταξινόμηση: Κανόνας βαθμολόγησης (4 × 2.5 = 10 μονάδες). Εντοπισμός: Δεύτερη επίσημη οδηγία του θέματος. Εφαρμογή: Κάθε Θέμα σταθμίζει εξίσου — καμία ενότητα δεν παραλείπεται.",
                ),
                TextSegment(text="."),
            ],
        ),
        Paragraph(
            segments=[
                TextSegment(
                    text="Θέμα 1: Μοντέλο Αναφοράς OSI και TCP/IP Stack",
                    is_highlight=True,
                    category="term",
                    tag_label="ΘΕΩΡΙΑ",
                    badge_class="badge-term",
                    tooltip="Ταξινόμηση: Θέμα θεωρίας για μοντέλα αναφοράς. Εντοπισμός: Επικεφαλίδα «Θέμα 1» της εκφώνησης. Εφαρμογή: Ζητείται αντιστοίχιση επιπέδων, ενθυλάκωση/PDU και διάκριση MAC/IP.",
                ),
            ],
            is_heading=True,
        ),
        Paragraph(
            segments=[
                TextSegment(text="1. Συγκρίνετε τα επίπεδα του μοντέλου "),
                TextSegment(
                    text="OSI",
                    is_highlight=True,
                    category="term",
                    tag_label="ΤΕΧΝΙΚΟΣ ΟΡΟΣ",
                    badge_class="badge-term",
                    tooltip="Ταξινόμηση: Μοντέλο αναφοράς 7 επιπέδων (ISO/OSI). Εντοπισμός: Ρητή αναφορά «μοντέλο OSI» στην ερώτηση 1. Εφαρμογή: Σύγκριση με την 4-επίπεδη στοίβα TCP/IP — αντιστοίχιση 7 ↔ 4 επιπέδων.",
                ),
                TextSegment(text=" με τα επίπεδα της στοίβας "),
                TextSegment(
                    text="TCP/IP",
                    is_highlight=True,
                    category="proto",
                    tag_label="ΠΡΩΤΟΚΟΛΛΟ",
                    badge_class="badge-proto",
                    tooltip="Ταξινόμηση: Στοίβα πρωτοκόλλων 4 επιπέδων. Εντοπισμός: Ρητή αναφορά «στοίβας TCP/IP» στην ερώτηση 1. Εφαρμογή: Πρέπει να αντιστοιχιστούν τα επίπεδα Εφαρμογής/Μεταφοράς/Internet/Πρόσβασης με τα 7 του OSI.",
                ),
                TextSegment(text="."),
            ],
        ),
        Paragraph(
            segments=[
                TextSegment(text="2. Εξηγήστε αναλυτικά τη διαδικασία "),
                TextSegment(
                    text="ενθυλάκωσης (encapsulation) και απο-ενθυλάκωσης (decapsulation)",
                    is_highlight=True,
                    category="method",
                    tag_label="ΜΕΘΟΔΟΣ",
                    badge_class="badge-method",
                    tooltip="Ταξινόμηση: Μηχανισμός προσθήκης/αφαίρεσης επικεφαλίδων ανά επίπεδο. Εντοπισμός: Ρητό αίτημα της ερώτησης 2 με τον αγγλικό όρο. Εφαρμογή: Η αλυσίδα Data → Segment/Datagram → Packet → Frame → Bits αποτελεί τη δομή της απάντησης.",
                ),
                TextSegment(text=" δεδομένων από την εφαρμογή μέχρι το φυσικό μέσο, αναφέροντας τα "),
                TextSegment(
                    text="PDUs",
                    is_highlight=True,
                    category="term",
                    tag_label="ΤΕΧΝΙΚΟΣ ΟΡΟΣ",
                    badge_class="badge-term",
                    tooltip="Ταξινόμηση: Protocol Data Units — οι οντότητες δεδομένων κάθε επιπέδου. Εντοπισμός: «αναφέροντας τα PDUs σε κάθε επίπεδο» στην ερώτηση 2. Εφαρμογή: Κάθε βήμα της ενθυλάκωσης ονομάζει το PDU που παράγει το αντίστοιχο επίπεδο.",
                ),
                TextSegment(text=" σε κάθε επίπεδο."),
            ],
        ),
        Paragraph(
            segments=[
                TextSegment(text="3. Ποιος είναι ο ρόλος της διεύθυνσης "),
                TextSegment(
                    text="MAC",
                    is_highlight=True,
                    category="term",
                    tag_label="ΤΕΧΝΙΚΟΣ ΟΡΟΣ",
                    badge_class="badge-term",
                    tooltip="Ταξινόμηση: Φυσική διεύθυνση 48-bit του επιπέδου ζεύξης (L2). Εντοπισμός: «ρόλος της διεύθυνσης MAC» στην ερώτηση 3. Εφαρμογή: Συγκρίνεται με τη λογική IP του L3 ως προς μέγεθος, φύση και πεδίο ισχύος.",
                ),
                TextSegment(text=" και ποια η διαφορά της από τη διεύθυνση "),
                TextSegment(
                    text="IP",
                    is_highlight=True,
                    category="term",
                    tag_label="ΤΕΧΝΙΚΟΣ ΟΡΟΣ",
                    badge_class="badge-term",
                    tooltip="Ταξινόμηση: Λογική διεύθυνση 32-bit (IPv4) του επιπέδου δικτύου (L3). Εντοπισμός: «τη διαφορά της από τη διεύθυνση IP» στην ερώτηση 3. Εφαρμογή: Ζητείται η σύγκριση φύσης (φυσική vs λογική), εύρους (τοπική vs διαδίκτυα) και ρόλου.",
                ),
                TextSegment(text=";"),
            ],
        ),
        Paragraph(
            segments=[
                TextSegment(
                    text="Θέμα 2: Υποδικτύωση IPv4 (VLSM)",
                    is_highlight=True,
                    category="method",
                    tag_label="ΥΠΟΛΟΓΙΣΤΙΚΟ",
                    badge_class="badge-method",
                    tooltip="Ταξινόμηση: Υπολογιστικό θέμα με μάσκες μεταβλητού μήκους. Εντοπισμός: Επικεφαλίδα «Θέμα 2» της εκφώνησης. Εφαρμογή: Λύνεται με ταξινόμηση αναγκών και εφαρμογή του τύπου 2^h - 2 ≥ hosts ανά υποδίκτυο.",
                ),
            ],
            is_heading=True,
        ),
        Paragraph(
            segments=[
                TextSegment(text="Μια εταιρεία διαθέτει το δίκτυο "),
                TextSegment(
                    text="192.168.100.0/24",
                    is_highlight=True,
                    category="given",
                    tag_label="ΔΕΔΟΜΕΝΟ",
                    badge_class="badge-given",
                    tooltip="Ταξινόμηση: Αρχικό block διευθύνσεων (ιδιωτικός χώρος 192.168.0.0/16). Εντοπισμός: Ρητό δεδομένο της εκφώνησης του Θέματος 2. Εφαρμογή: 256 συνολικές διευθύνσεις που κατανέμονται με VLSM στα τέσσερα υποδίκτυα.",
                ),
                TextSegment(text=" και θέλει να δημιουργήσει:"),
            ],
        ),
        Paragraph(segments=[TextSegment(text="Υποδίκτυο 1: "), TextSegment(text="60 υπολογιστές", is_highlight=True, category="given", tag_label="ΑΝΑΓΚΗ: 60", badge_class="badge-given", tooltip="Ταξινόμηση: Απαίτηση φιλοξενίας 60 σταθμών. Εντοπισμός: Αριθμός στη λίστα του Θέματος 2. Εφαρμογή: 2^h - 2 ≥ 60 δίνει h = 6 → πρόθεμα /26 και block 64 διευθύνσεων.")]),
        Paragraph(segments=[TextSegment(text="Υποδίκτυο 2: "), TextSegment(text="28 υπολογιστές", is_highlight=True, category="given", tag_label="ΑΝΑΓΚΗ: 28", badge_class="badge-given", tooltip="Ταξινόμηση: Απαίτηση φιλοξενίας 28 σταθμών. Εντοπισμός: Αριθμός στη λίστα του Θέματος 2. Εφαρμογή: 2^h - 2 ≥ 28 δίνει h = 5 → πρόθεμα /27 και block 32 διευθύνσεων.")]),
        Paragraph(segments=[TextSegment(text="Υποδίκτυο 3: "), TextSegment(text="12 υπολογιστές", is_highlight=True, category="given", tag_label="ΑΝΑΓΚΗ: 12", badge_class="badge-given", tooltip="Ταξινόμηση: Απαίτηση φιλοξενίας 12 σταθμών. Εντοπισμός: Αριθμός στη λίστα του Θέματος 2. Εφαρμογή: 2^h - 2 ≥ 12 δίνει h = 4 → πρόθεμα /28 και block 16 διευθύνσεων.")]),
        Paragraph(segments=[TextSegment(text="Υποδίκτυο 4: "), TextSegment(text="2 δρομολογητές", is_highlight=True, category="given", tag_label="ΑΝΑΓΚΗ: 2 (p2p)", badge_class="badge-given", tooltip="Ταξινόμηση: Ζεύξη σημείου-προς-σημείο μεταξύ δύο δρομολογητών. Εντοπισμός: «2 δρομολογητές (Point-to-point link)» στο Θέμα 2. Εφαρμογή: 2^h - 2 ≥ 2 δίνει h = 2 → πρόθεμα /30 (ακριβώς 2 χρησιμοποιήσιμοι hosts)."), TextSegment(text=" (Point-to-point link)")]),
        Paragraph(
            segments=[
                TextSegment(text="Βρείτε για κάθε υποδίκτυο: "),
                TextSegment(
                    text="Network Address, Subnet Mask, First/Last Usable IP, Broadcast Address",
                    is_highlight=True,
                    category="method",
                    tag_label="ΖΗΤΟΥΜΕΝΑ",
                    badge_class="badge-method",
                    tooltip="Ταξινόμηση: Οι πέντε στήλες της τυπικής απάντησης υποδικτύωσης. Εντοπισμός: Ρητή απαρίθμηση στο κλείσιμο του Θέματος 2. Εφαρμογή: Η λύση ολοκληρώνεται με πίνακα 4 γραμμών × 5 στηλών.",
                ),
                TextSegment(text="."),
            ],
        ),
        Paragraph(
            segments=[
                TextSegment(
                    text="Θέμα 3: Επίπεδο Μεταφοράς — TCP vs UDP & Έλεγχος Ροής",
                    is_highlight=True,
                    category="proto",
                    tag_label="ΘΕΩΡΙΑ",
                    badge_class="badge-proto",
                    tooltip="Ταξινόμηση: Θέμα θεωρίας μεταφοράς. Εντοπισμός: Επικεφαλίδα «Θέμα 3» της εκφώνησης. Εφαρμογή: Ζητείται sliding window/flow control, εφαρμογές UDP και ρόλος TTL.",
                ),
            ],
            is_heading=True,
        ),
        Paragraph(
            segments=[
                TextSegment(text="1. Περιγράψτε τον μηχανισμό "),
                TextSegment(
                    text="συρόμενου παραθύρου (Sliding Window)",
                    is_highlight=True,
                    category="method",
                    tag_label="ΜΕΘΟΔΟΣ",
                    badge_class="badge-method",
                    tooltip="Ταξινόμηση: Μηχανισμός ελέγχου ροής του TCP. Εντοπισμός: Ρητή αναφορά στην ερώτηση 1 του Θέματος 3. Εφαρμογή: Το παράθυρο rwnd που ανακοινώνει ο παραλήπτης περιορίζει τα unACKed bytes του αποστολέα.",
                ),
                TextSegment(text=" στο "),
                TextSegment(
                    text="TCP",
                    is_highlight=True,
                    category="proto",
                    tag_label="ΠΡΩΤΟΚΟΛΛΟ",
                    badge_class="badge-proto",
                    tooltip="Ταξινόμηση: Πρωτόκολλο μεταφοράς με σύνδεση. Εντοπισμός: «στο TCP» στην ερώτηση 1 του Θέματος 3. Εφαρμογή: Το sliding window υλοποιείται στο πεδίο Window της επικεφαλίδας TCP.",
                ),
                TextSegment(text=" και πώς αποτρέπει την υπερχείλιση της προσωρινής μνήμης του παραλήπτη ("),
                TextSegment(
                    text="Flow Control",
                    is_highlight=True,
                    category="term",
                    tag_label="ΤΕΧΝΙΚΟΣ ΟΡΟΣ",
                    badge_class="badge-term",
                    tooltip="Ταξινόμηση: Έλεγχος ροής άκρου-προς-άκρο (receiver-driven). Εντοπισμός: Παρενθετικός όρος «(Flow Control)» στην ερώτηση 1. Εφαρμογή: Διακρίνεται από τον έλεγχο συμφόρησης που αφορά το δίκτυο συνολικά.",
                ),
                TextSegment(text=")."),
            ],
        ),
        Paragraph(
            segments=[
                TextSegment(text="2. Σε ποιες εφαρμογές προτιμάται το "),
                TextSegment(
                    text="UDP",
                    is_highlight=True,
                    category="proto",
                    tag_label="ΠΡΩΤΟΚΟΛΛΟ",
                    badge_class="badge-proto",
                    tooltip="Ταξινόμηση: Ασυνδεξούμενο, μη αξιόπιστο πρωτόκολλο μεταφοράς. Εντοπισμός: «προτιμάται το UDP έναντι του TCP» στην ερώτηση 2. Εφαρμογή: Η απάντηση στηρίζεται σε επικεφαλίδα 8 bytes, απουσία χειραψίας και υποστήριξη multicast.",
                ),
                TextSegment(text=" έναντι του "),
                TextSegment(
                    text="TCP",
                    is_highlight=True,
                    category="proto",
                    tag_label="ΠΡΩΤΟΚΟΛΛΟ",
                    badge_class="badge-proto",
                    tooltip="Ταξινόμηση: Πρωτόκολλο μεταφοράς με σύνδεση και επιβεβαιώσεις. Εντοπισμός: «έναντι του TCP» στην ερώτηση 2. Εφαρμογή: Το TCP απορρίπτεται όταν η καθυστέρηση επαναμετάδοσης χαλάει την εφαρμογή (π.χ. ζωντανή ροή).",
                ),
                TextSegment(text=" και για ποιους λόγους;"),
            ],
        ),
        Paragraph(
            segments=[
                TextSegment(text="3. Εξηγήστε τον ρόλο του πεδίου "),
                TextSegment(
                    text="TTL (Time to Live)",
                    is_highlight=True,
                    category="term",
                    tag_label="ΠΕΔΙΟ IPv4",
                    badge_class="badge-term",
                    tooltip="Ταξινόμηση: Πεδίο 8-bit της επικεφαλίδας IPv4 με όριο hops. Εντοπισμός: Ρητή αναφορά «TTL (Time to Live)» στην ερώτηση 3. Εφαρμογή: Αποτρέπει αιώνια κυκλοφορία πακέτων σε βρόχους δρομολόγησης και θεμελιώνει το traceroute.",
                ),
                TextSegment(text=" στην επικεφαλίδα "),
                TextSegment(
                    text="IPv4",
                    is_highlight=True,
                    category="proto",
                    tag_label="ΠΡΩΤΟΚΟΛΛΟ",
                    badge_class="badge-proto",
                    tooltip="Ταξινόμηση: Πρωτόκολλο δικτύου, έκδοση 4 (32-bit διευθυνσιοδότηση). Εντοπισμός: «στην επικεφαλίδα IPv4» στην ερώτηση 3. Εφαρμογή: Το TTL είναι ένα από τα πεδία της 20-byte ελάχιστης επικεφαλίδας του IPv4.",
                ),
                TextSegment(text="."),
            ],
        ),
        Paragraph(
            segments=[
                TextSegment(
                    text="Θέμα 4: Αλγόριθμοι Δρομολόγησης",
                    is_highlight=True,
                    category="method",
                    tag_label="ΣΥΓΚΡΙΣΗ",
                    badge_class="badge-method",
                    tooltip="Ταξινόμηση: Θέμα σύγκρισης αλγορίθμων δρομολόγησης. Εντοπισμός: Επικεφαλίδα «Θέμα 4» της εκφώνησης. Εφαρμογή: Οργώνεται στα τρία ρητά κριτήρια: ανταλλαγή πληροφορίας, σύγκλιση, βρόχοι.",
                ),
            ],
            is_heading=True,
        ),
        Paragraph(
            segments=[
                TextSegment(text="Συγκρίνετε τους αλγορίθμους δρομολόγησης "),
                TextSegment(
                    text="Link-State (π.χ. OSPF)",
                    is_highlight=True,
                    category="proto",
                    tag_label="LS / OSPF",
                    badge_class="badge-proto",
                    tooltip="Ταξινόμηση: Οικογένεια Link-State με εκπρόσωπο το OSPF. Εντοπισμός: Ρητή αναφορά στην εκφώνηση του Θέματος 4. Εφαρμογή: Συγκρίνεται ως προς πλημυρική διάδοση LSA, Dijkstra και σύγκλιση σε δευτερόλεπτα.",
                ),
                TextSegment(text=" και "),
                TextSegment(
                    text="Distance-Vector (π.χ. RIP)",
                    is_highlight=True,
                    category="proto",
                    tag_label="DV / RIP",
                    badge_class="badge-proto",
                    tooltip="Ταξινόμηση: Οικογένεια Distance-Vector με εκπρόσωπο το RIP. Εντοπισμός: Ρητή αναφορά στην εκφώνηση του Θέματος 4. Εφαρμογή: Συγκρίνεται ως προς ανταλλαγή με γείτονες, Bellman-Ford και ευπάθεια στο count-to-infinity.",
                ),
                TextSegment(text=" ως προς:"),
            ],
        ),
        Paragraph(segments=[TextSegment(text="Τον "), TextSegment(text="τρόπο ανταλλαγής πληροφορίας", is_highlight=True, category="term", tag_label="ΚΡΙΤΗΡΙΟ 1", badge_class="badge-term", tooltip="Ταξινόμηση: Κριτήριο σύγκρισης — τι ανταλλάσσουν και με ποιον. Εντοπισμός: Πρώτο στιγμιότυπο της λίστας του Θέματος 4. Εφαρμογή: LS: πλημυρική διάδοση ολόκληρης τοπολογίας σε όλους· DV: διανύσματα μόνο προς γείτονες.")]),
        Paragraph(segments=[TextSegment(text="Την "), TextSegment(text="ταχύτητα σύγκλισης (convergence time)", is_highlight=True, category="term", tag_label="ΚΡΙΤΗΡΙΟ 2", badge_class="badge-term", tooltip="Ταξινόμηση: Κριτήριο σύγκρισης — χρόνος σταθεροποίησης πινάκων. Εντοπισμός: Δεύτερο στιγμιότυπο της λίστας του Θέματος 4. Εφαρμογή: LS συγκλίνει σε δευτερόλεπτα (event-driven)· DV σε λεπτά (περιοδική προσέγγιση hop-by-hop).")]),
        Paragraph(segments=[TextSegment(text="Την "), TextSegment(text="ευπάθεια σε βρόχους δρομολόγησης (Routing Loops / Count-to-Infinity problem)", is_highlight=True, category="term", tag_label="ΚΡΙΤΗΡΙΟ 3", badge_class="badge-term", tooltip="Ταξινόμηση: Κριτήριο σύγκρισης — κυκλική δρομολόγηση πακέτων. Εντοπισμός: Τρίτο στιγμιότυπο της λίστας του Θέματος 4. Εφαρμογή: Το DV υποκύπτει στο count-to-infinity (μετριασμός: split horizon, poison reverse, triggered updates, όριο 16 στο RIP)· το LS με καθολική εικόνα είναι ουσιαστικά απαλλαγμένο.")]),
    ]

    questions = [
        ExamQuestion(
            thema="Θέμα 1",
            thema_title="Μοντέλο Αναφοράς OSI και TCP/IP Stack",
            sub_number="1.1",
            title="Σύγκριση Επιπέδων OSI ↔ TCP/IP",
            question_type="comparison",
            prompt="Συγκρίνετε τα επίπεδα του μοντέλου OSI με τα επίπεδα της στοίβας TCP/IP.",
            steps=[
                CalculationStep(
                    label="Βήμα 1 — Δομή των δύο μοντέλων",
                    description="Το OSI είναι μοντέλο αναφοράς 7 επιπέδων (Εφαρμογής, Παρουσίασης, Συνόδου, Μεταφοράς, Δικτύου, Σύνδεσης Δεδομένων, Φυσικό), ενώ η στοίβα TCP/IP είναι λειτουργική αρχιτεκτονική 4 επιπέδων (Εφαρμογής, Μεταφοράς, Internet, Πρόσβασης Δικτύου).",
                ),
                CalculationStep(
                    label="Βήμα 2 — Αντιστοίχιση επιπέδων",
                    description="Τα τρία ανώτερα επίπεδα του OSI συνενώνονται στο επίπεδο Εφαρμογής του TCP/IP, και τα δύο κατώτερα στο επίπεδο Πρόσβασης Δικτύου· τα ενδιάμεσα αντιστοιχούν ένα-προς-ένα.",
                ),
                CalculationStep(
                    label="Βήμα 3 — Πρωτόκολλα & PDUs ανά επίπεδο",
                    description="Η σύγκριση ολοκληρώνεται με τα αντιπροσωπευτικά πρωτόκολλα και το PDU κάθε επιπέδου (δελτίο πίνακα παρακάτω και αναλυτικός πίνακας επιπέδων στο τέλος του σεναρίου).",
                ),
            ],
            answer_tables=[
                AnalysisTable(
                    title="Σύνοψη Αντιστοίχισης OSI ↔ TCP/IP",
                    headers=["OSI (7 επίπεδα)", "TCP/IP (4 επίπεδα)", "Αντιπροσωπευτικά Πρωτόκολλα"],
                    rows=[
                        AnalysisRow(cells=["Εφαρμογής + Παρουσίασης + Συνόδου", "Εφαρμογής", "HTTP/S, SMTP, FTP, DNS, TELNET, SNMP, SSH, POP3"], highlight=False),
                        AnalysisRow(cells=["Μεταφοράς", "Μεταφοράς", "TCP, UDP"], highlight=False),
                        AnalysisRow(cells=["Δικτύου", "Internet", "IP (v4/v6), ICMP, ARP, IGMP, OSPF"], highlight=False),
                        AnalysisRow(cells=["Σύνδεσης Δεδομένων + Φυσικό", "Πρόσβασης Δικτύου", "Ethernet, WiFi (802.11), PPP, ARC/RARP"], highlight=False),
                    ],
                    note="Τα επίπεδα Παρουσίασης (κρυπτογράφηση/συμπίεση/μορφοποίηση) και Συνόδου (διαχείριση συνόδων) δεν υπάρχουν ως χωριστές οντότητες στο TCP/IP — ενσωματώνονται στις εφαρμογές.",
                ),
            ],
            answer="Το OSI έχει 7 επίπεδα και το TCP/IP 4: (App+Pres+Session) ↔ Εφαρμογής, Transport ↔ Μεταφοράς, Network ↔ Internet, (DataLink+Physical) ↔ Πρόσβασης Δικτύου.",
            tips=[
                "Το TCP/IP προέκυψε από το πρακτικό ARPANET, το OSI από θεωρητική τυποποίηση — γι' αυτό το TCP/IP έχει περισσότερα λειτουργικά πρωτόκολλα ανά επίπεδο.",
                "Το επίπεδο Πρόσβασης καλύπτεται από τα υποεπίπεδα LLC, MAC και PHY.",
            ],
        ),
        ExamQuestion(
            thema="Θέμα 1",
            thema_title="Μοντέλο Αναφοράς OSI και TCP/IP Stack",
            sub_number="1.2",
            title="Ενθυλάκωση & Απο-ενθυλάκωση με PDUs",
            question_type="theory",
            prompt="Εξηγήστε αναλυτικά τη διαδικασία ενθυλάκωσης (encapsulation) και απο-ενθυλάκωσης (decapsulation) δεδομένων από την εφαρμογή μέχρι το φυσικό μέσο, αναφέροντας τα PDUs σε κάθε επίπεδο.",
            steps=[
                CalculationStep(
                    label="Βήμα 1 — Επίπεδο Εφαρμογής",
                    description="Η εφαρμογή παράγει το μήνυμα δεδομένων. PDU: <strong>Data / Message</strong> (χωρίς να προστίθεται header μεταφοράς ακόμη — τυλίγεται από τα πρωτόκολλα της εφαρμογής).",
                    latex=r"\text{Data (Message)} \rightarrow \text{εδώ ξεκινά η αλυσίδα}",
                ),
                CalculationStep(
                    label="Βήμα 2 — Επίπεδο Μεταφοράς",
                    description="Το TCP (ή UDP) προσθέτει τη δική του επικεφαλίδα (θύρες, seq/ack, checksum). PDU: <strong>Segment</strong> για TCP ή <strong>Datagram</strong> για UDP.",
                    latex=r"\text{TCP Header} + \text{Data} \Rightarrow \text{Segment} \;(|\; \text{UDP Header} + \text{Data} \Rightarrow \text{Datagram})",
                ),
                CalculationStep(
                    label="Βήμα 3 — Επίπεδο Internet (Δικτύου)",
                    description="Το IP προσθέτει την επικεφαλίδα του (διευθύνσεις πηγής/προορισμού, TTL, protocol). PDU: <strong>Packet / IP Datagram</strong>.",
                    latex=r"\text{IP Header} + \text{Segment} \Rightarrow \text{Packet}",
                ),
                CalculationStep(
                    label="Βήμα 4 — Επίπεδο Πρόσβασης (Ζεύξης)",
                    description="Η θύρα δικτύου (NIC) προσθέτει header και trailer πλαισίου (MAC πηγής/προορισμού, FCS). PDU: <strong>Frame</strong>.",
                    latex=r"\text{Frame Header} + \text{Packet} + \text{Trailer (FCS)} \Rightarrow \text{Frame}",
                ),
                CalculationStep(
                    label="Βήμα 5 — Φυσικό Μέσο & Απο-ενθυλάκωση",
                    description="Το frame σειριοποιείται σε <strong>Bits</strong> (ηλεκτρικά/οπτικά/ασύρματα σήματα). Στον παραλήπτη εκτελείται η αντίστροφη απο-ενθυλάκωση: κάθε επίπεδο αφαιρεί την επικεφαλίδα του προηγούμενου και παραδίδει τα δεδομένα ένα επίπεδο ψηλότερα, μέχρι το μήνυμα της εφαρμογής.",
                    latex=r"\text{Bits} \rightarrow \text{Frame} \rightarrow \text{Packet} \rightarrow \text{Segment} \rightarrow \text{Data}",
                ),
            ],
            answer="Ενθυλάκωση: Data → Segment (TCP) / Datagram (UDP) → Packet (IP) → Frame (Ethernet) → Bits. Απο-ενθυλάκωση: η αντίστροφη διαδρομή με αφαίρεση επικεφαλίδων σε κάθε επίπεδο του παραλήπτη.",
            tips=[
                "Το κάθε επίπεδο βλέπει το PDU του ανώτερου επίπεδου ως καθαρά δεδομένα (payload) — αρχή της αρθρωτής σχεδίασης.",
                "Μόνο το επίπεδο Πρόσβασης προσθέτει και trailer (FCS), όλα τα άλλα προσθέτουν μόνο header.",
            ],
        ),
        ExamQuestion(
            thema="Θέμα 1",
            thema_title="Μοντέλο Αναφοράς OSI και TCP/IP Stack",
            sub_number="1.3",
            title="Ρόλος MAC και Διαφορά από την IP",
            question_type="comparison",
            prompt="Ποιος είναι ο ρόλος της διεύθυνσης MAC και ποια η διαφορά της από τη διεύθυνση IP;",
            steps=[
                CalculationStep(
                    label="Βήμα 1 — Ρόλος της MAC",
                    description="Η MAC είναι η <strong>φυσική διεύθυνση 48-bit</strong> (6 bytes, π.χ. 00:1A:2B:3C:4D:5E) που είναι μοναδική και σταθερή για κάθε προσαρμογέα (NIC). Χρησιμοποιείται από το επίπεδο Σύνδεσης Δεδομένων (L2) για την <strong>τοπική παράδοση</strong> μέσα στον ίδιο σύνδεσμο/υποδίκτυο: το πλαίσιο παραδίδεται στη MAC του επόμενου κόμβου.",
                ),
                CalculationStep(
                    label="Βήμα 2 — Ρόλος της IP",
                    description="Η IP είναι η <strong>λογική διεύθυνση 32-bit</strong> (IPv4) με ιεραρχική δομή net_ID/host_ID. Ανατίθεται δυναμικά (DHCP) ή στατικά και χρησιμοποιείται από το επίπεδο Δικτύου (L3) για τη <strong>δρομολόγηση μεταξύ διαφορετικών δικτύων</strong> — διασχηματίζει το γεωγραφικό/λογικό topology από το υλικό.",
                ),
                CalculationStep(
                    label="Βήμα 3 — Γεφύρωση των δύο",
                    description="Στο ίδιο τοπικό δίκτυο το ARP μεταφράζει IP → MAC (broadcast αίτημα, unicast απάντηση, αποθήκευση σε ARP cache). Σε κάθε hop το packet επενδύεται σε νέο frame με νέες MAC (πηγή/προορισμός αλλάζουν), ενώ οι IP πηγής/προορισμού παραμένουν ίδιες άκρο-προς-άκρο.",
                ),
            ],
            answer="MAC: φυσική/σταθερή 48-bit διεύθυνση L2 για τοπική παράδοση στον σύνδεσμο. IP: λογική/ιεραρχική 32-bit διεύθυνση L3 για δρομολόγηση μεταξύ δικτύων. Το ARP γεφυρώνει τις δύο στον ίδιο σύνδεσμο.",
            answer_tables=[
                AnalysisTable(
                    title="Σύγκριση MAC ↔ IP",
                    headers=["Κριτήριο", "Διεύθυνση MAC", "Διεύθυνση IP (IPv4)"],
                    rows=[
                        AnalysisRow(cells=["Μήκος", "48 bits (6 bytes)", "32 bits (4 bytes)"]),
                        AnalysisRow(cells=["Φύση", "Φυσική — «καμένη» στον NIC από τον κατασκευαστή", "Λογική — στατική ή μέσω DHCP"]),
                        AnalysisRow(cells=["Επίπεδο", "Σύνδεσης Δεδομένων (L2)", "Δικτύου (L3)"]),
                        AnalysisRow(cells=["Δομή", "Επίπεδη (flat), χωρίς ιεραρχία", "Ιεραρχική: net_ID + subnet_ID + host_ID"]),
                        AnalysisRow(cells=["Πεδίο ισχύος", "Μόνο στον τοπικό σύνδεσμο (λλάσει σε κάθε hop)", "Άκρο-προς-άκρο, σε όλο το διαδίκτυο"]),
                        AnalysisRow(cells=["Ρόλος", "Τοπική παράδοση του frame στον επόμενο κόμβο", "Δρομολόγηση του packet προς το δίκτυο προορισμού"]),
                    ],
                ),
            ],
            tips=[
                "Οι MAC αλλάζουν σε κάθε hop (hop-by-hop παράδοση), οι IP πηγής/προορισμού μένουν σταθεμένες — κλασική ερώτηση πολλαπλής επιλογής.",
                "Η MAC δεν αλλάζει εύκολα (σταθερή στο υλικό)· η IP αλλάζει με το δίκτυο σύνδεσης — γι' αυτό η IP είναι «λογική».",
            ],
        ),
        ExamQuestion(
            thema="Θέμα 2",
            thema_title="Υποδικτύωση IPv4 (VLSM)",
            sub_number="2",
            title="Κατανομή VLSM του 192.168.100.0/24 σε 4 Υποδίκτυα",
            question_type="computational",
            prompt="Μια εταιρεία διαθέτει το δίκτυο 192.168.100.0/24 και θέλει να δημιουργήσει: Υποδίκτυο 1: 60 υπολογιστές, Υποδίκτυο 2: 28 υπολογιστές, Υποδίκτυο 3: 12 υπολογιστές, Υποδίκτυο 4: 2 δρομολογητές (Point-to-point link). Βρείτε για κάθε υποδίκτυο: Network Address, Subnet Mask, First/Last Usable IP, Broadcast Address.",
            given=[
                GivenParameter(label="Αρχικό δίκτυο", value="192.168.100.0/24", source="εκφώνηση Θέματος 2"),
                GivenParameter(label="Ανάγκη Υποδικτύου 1", value="60 hosts", source="λίστα εκφώνησης"),
                GivenParameter(label="Ανάγκη Υποδικτύου 2", value="28 hosts", source="λίστα εκφώνησης"),
                GivenParameter(label="Ανάγκη Υποδικτύου 3", value="12 hosts", source="λίστα εκφώνησης"),
                GivenParameter(label="Ανάγκη Υποδικτύου 4", value="2 hosts (p2p)", source="λίστα εκφώνησης"),
                GivenParameter(label="Συνολικός χώρος", value="256 διευθύνσεις (2^8)", source="από το /24"),
            ],
            steps=[
                CalculationStep(
                    label="Βήμα 1 — Ταξινόμηση κατά Φθίνουσα Σειρά",
                    description="Στο VLSM ικανοποιούμε πρώτα τη μεγαλύτερη ανάγκη: 60 → 28 → 12 → 2. Έτσι κάθε υποδίκτυο παίρνει το μικρότερο δυνατό block και δεν προκύπτουν επικαλύψεις ή ασυνεχή κενά.",
                    latex=r"60 \ge 28 \ge 12 \ge 2 \;\Rightarrow\; \text{σειρά κατανομής: } S_1, S_2, S_3, S_4",
                ),
                CalculationStep(
                    label="Βήμα 2 — Υποδίκτυο 1 (60 hosts)",
                    description="Ζητούμε το ελάχιστο h με 2^h − 2 ≥ 60. Το h = 5 δίνει 30 (ανεπαρκές), το h = 6 δίνει 62 ≥ 60. Πρόθεμα /26, μάσκα 255.255.255.192, block 256 − 192 = 64 διευθύνσεις. Το υποδίκτυο ξεκινά στο 192.168.100.0 (πρώτο ελεύθερο).",
                    latex=r"2^h - 2 \ge 60 \Rightarrow h = 6 \;(2^6 - 2 = 62) \Rightarrow /26,\; \text{block} = 256 - 192 = 64",
                    result="Δίκτυο 192.168.100.0/26 · Usable .1 – .62 · Broadcast .63",
                ),
                CalculationStep(
                    label="Βήμα 3 — Υποδίκτυο 2 (28 hosts)",
                    description="Το επόμενο ελεύθερο byte-μάρτυρας είναι το .63 + 1 = 64. Για 28 hosts το h = 5 (2^5 − 2 = 30 ≥ 28) δίνει πρόθεμα /27, μάσκα 255.255.255.224, block 32. Χωρητικότητα 30 hosts για ανάγκη 28 — ελάχιστη σπατάλη 2 διευθύνσεων.",
                    latex=r"2^h - 2 \ge 28 \Rightarrow h = 5 \;(30) \Rightarrow /27,\; \text{block} = 256 - 224 = 32,\; \text{start} = 63 + 1 = 64",
                    result="Δίκτυο 192.168.100.64/27 · Usable .65 – .94 · Broadcast .95",
                ),
                CalculationStep(
                    label="Βήμα 4 — Υποδίκτυο 3 (12 hosts)",
                    description="Επόμενο ελεύθερο σημείο: .95 + 1 = 96. Για 12 hosts το h = 4 (2^4 − 2 = 14 ≥ 12) δίνει πρόθεμα /28, μάσκα 255.255.255.240, block 16.",
                    latex=r"2^h - 2 \ge 12 \Rightarrow h = 4 \;(14) \Rightarrow /28,\; \text{block} = 256 - 240 = 16,\; \text{start} = 95 + 1 = 96",
                    result="Δίκτυο 192.168.100.96/28 · Usable .97 – .110 · Broadcast .111",
                ),
                CalculationStep(
                    label="Βήμα 5 — Υποδίκτυο 4 (2 δρομολογητές, p2p)",
                    description="Για ζεύξη σημείου-προς-σημείο αρκούν ακριβώς 2 hosts: h = 2 (2^2 − 2 = 2), πρόθεμα /30, μάσκα 255.255.255.252, block 4. Το /30 είναι η κανονική επιλογή για p2p συνδέσεις δρομολογητών.",
                    latex=r"2^h - 2 \ge 2 \Rightarrow h = 2 \;(2) \Rightarrow /30,\; \text{block} = 256 - 252 = 4,\; \text{start} = 111 + 1 = 112",
                    result="Δίκτυο 192.168.100.112/30 · Usable .113 – .114 · Broadcast .115",
                ),
                CalculationStep(
                    label="Βήμα 6 — Επαλήθευση Χώρου",
                    description="Έλεγχος: τα blocks 64 + 32 + 16 + 4 = 116 διευθύνσεις στο 0–115, χωρίς επικαλύψεις· το εύρος .116 – .255 (140 διευθύνσεις) παραμένει ελεύθερο για μελλοντική επέκταση. Κάθε υποδίκτυο ξεκινά ακριβώς μετά το broadcast του προηγούμενου.",
                    latex=r"64 + 32 + 16 + 4 = 116 \le 256 \;(\text{χωρίς επικάλυψη}), \;\; \text{ελεύθερο: } .116 - .255",
                ),
            ],
            answer_tables=[
                AnalysisTable(
                    title="Τελικός Πίνακας Κατανομής VLSM (Ζητούμενη Απάντηση)",
                    headers=["Υποδίκτυο", "Ανάγκη (hosts)", "Network Address", "Subnet Mask (CIDR)", "First Usable", "Last Usable", "Broadcast"],
                    rows=[
                        AnalysisRow(cells=["Υποδίκτυο 1", "60", "192.168.100.0", "255.255.255.192 (/26)", "192.168.100.1", "192.168.100.62", "192.168.100.63"], highlight=True),
                        AnalysisRow(cells=["Υποδίκτυο 2", "28", "192.168.100.64", "255.255.255.224 (/27)", "192.168.100.65", "192.168.100.94", "192.168.100.95"], highlight=True),
                        AnalysisRow(cells=["Υποδίκτυο 3", "12", "192.168.100.96", "255.255.255.240 (/28)", "192.168.100.97", "192.168.100.110", "192.168.100.111"], highlight=True),
                        AnalysisRow(cells=["Υποδίκτυο 4 (p2p)", "2", "192.168.100.112", "255.255.255.252 (/30)", "192.168.100.113", "192.168.100.114", "192.168.100.115"], highlight=True),
                    ],
                    note="Ισοδυναμία με τις ενδεικτικές λύσεις του θέματος: /26 (62 usable), /27 (30), /28 (14), /30 (2) — η ταξινόμηση κατά φθίνουσα σειρά εξασφαλίζει τη συνέχεια των blocks.",
                ),
            ],
            answer="Υποδίκτυο 1: 192.168.100.0/26 (.1–.62, BC .63) · Υποδίκτυο 2: 192.168.100.64/27 (.65–.94, BC .95) · Υποδίκτυο 3: 192.168.100.96/28 (.97–.110, BC .111) · Υποδίκτυο 4: 192.168.100.112/30 (.113–.114, BC .115).",
            tips=[
                "Το −2 στον τύπο αφαιρεί τη διεύθυνση δικτύου (host bits όλα 0) και το broadcast (όλα 1) — χωρίς αυτό το h βγαίνει ένα bit μικρότερο και το υποδίκτυο δεν επαρκεί.",
                "Παγίδα: το /27 δεν χωράει τους 60 hosts του Υποδικτύου 1 (30 < 60) και το /26 σπαταλά χώρο για 28 hosts — γι' αυτό το VLSM χρησιμοποιεί διαφορετική μάσκα ανά υποδίκτυο.",
                "Έλεγχος σειράς: broadcast του προηγούμενου + 1 = δίκτυο του επόμενου (.63+1=.64, .95+1=.96, .111+1=.112).",
            ],
        ),
        ExamQuestion(
            thema="Θέμα 3",
            thema_title="Επίπεδο Μεταφοράς — TCP vs UDP & Έλεγχος Ροής",
            sub_number="3.1",
            title="Συρόμενο Παράθυρο (Sliding Window) & Flow Control",
            question_type="theory",
            prompt="Περιγράψτε τον μηχανισμό συρόμενου παραθύρου (Sliding Window) στο TCP και πώς αποτρέπει την υπερχείλιση της προσωρινής μνήμης του παραλήπτη (Flow Control).",
            steps=[
                CalculationStep(
                    label="Βήμα 1 — Παράθυρο & Buffer Παραλήπτη",
                    description="Ο παραλήπτη διαθέτει προσωρινή μνήμη (receive buffer) για δεδομένα που έχουν φτάσει αλλά δεν έχει διαβάσει ακόμη η εφαρμογή του. Ο διαθέσιτος χώρος ανακοινώνεται στον αποστολέα ως <strong>rwnd</strong> μέσω του πεδίου Window κάθε ACK.",
                    latex=r"\text{rwnd} = \text{μεγέθος buffer} - (\text{εισαγμένα} - \text{αναγνωσμένα από την εφαρμογή})",
                ),
                CalculationStep(
                    label="Βήμα 2 — Περιορισμός του Αποστολέα",
                    description="Ο αποστολέας κρατά ένα παράθυρο από bytes που έχουν σταλεί αλλά δεν έχουν επιβεβαιωθεί (unACKed). Ισχύει πάντα: unACKed bytes &le; rwnd. Όσο το παράθυρο «ολισθαίνει» με τις επιβεβαιώσεις, νέα segments αποστέλλονται από τη δεξιά άκρη.",
                ),
                CalculationStep(
                    label="Βήμα 3 — Συσσωρευτικές Επιβεβαιώσεις & Ολίσθηση",
                    description="Οι ACK του TCP είναι <strong>συσσωρευτικά</strong>: ACK = n σημαίνει «λήφθηκαν όλα τα bytes μέχρι το n−1, περιμένω το n». Με κάθε νέο ACK το αριστερό άκρο του παραθύρου μετακινείται μπροστά (το παράθυρο ολισθαίνει) και απελευθερώνει χώρο για νέα δεδομένα.",
                ),
                CalculationStep(
                    label="Βήμα 4 — Μηδενικό Παράθυρο (Zero Window)",
                    description="Αν η εφαρμογή του παραλήπτη διαβάζει αργά και το buffer γεμίσει, ο παραλήπτης ανακοινώνει rwnd = 0: ο αποστολέας <strong>σταματά πλήρως</strong> τη μετάδοση. Ελέγχει περιοδικά (zero-window probe) αν άνοιξε ξανά το παράθυρο. Έτσι δεν «πνίγει» ποτέ τη μνήμη του παραλήπτη.",
                ),
                CalculationStep(
                    label="Βήμα 5 — Διαχωρισμός από τον Έλεγχο Συμφόρησης",
                    description="Το flow control προστατεύει τον <strong>παραλήπτη</strong> (rwnd), ενώ το congestion control προστατεύει το <strong>δίκτυο</strong> (cwnd). Το ενεργό παράθυρο του αποστολέα είναι το ελάχιστο των δύο: min(rwnd, cwnd).",
                    latex=r"\text{ενεργό παράθυρο} = \min(\text{rwnd}, \text{cwnd})",
                ),
            ],
            answer="Το sliding window περιορίζει τα unACKed bytes του αποστολέα στο rwnd που ανακοινώνει ο παραλήπτης· οι συσσωρευτικές ACKs ολισθαίνουν το παράθυρο, και σε buffer πληρότητας (rwnd = 0) η αποστολή διακόπτεται — με αυτόν τον τρόπο αποτρέπεται η υπερχείλιση της μνήμης του παραλήπτη.",
            tips=[
                "Μην συγχέετε το rwnd (έλεγχος ροής, πεδίο Window) με το cwnd (έλεγχος συμφόρησης, υπολογίζεται στο TCP Reno/Tahoe).",
                "Τρία διπλότυπα ACK για το ίδιο byte = Fast Retransmit πριν λήξει το timeout.",
            ],
        ),
        ExamQuestion(
            thema="Θέμα 3",
            thema_title="Επίπεδο Μεταφοράς — TCP vs UDP & Έλεγχος Ροής",
            sub_number="3.2",
            title="Εφαρμογές που Προτιμούν το UDP",
            question_type="theory",
            prompt="Σε ποιες εφαρμογές προτιμάται το UDP έναντι του TCP και για ποιους λόγους;",
            steps=[
                CalculationStep(
                    label="Βήμα 1 — Ιδιότητες του UDP",
                    description="Το UDP είναι ασυνδεξούμενο (χωρίς χειραψία), μη αξιόπιστο (χωρίς επιβεβαιώσεις/επαναμεταδόσεις), με ελάχιστη επικεφαλίδα 8 bytes και με υποστήριξη multicast/broadcast. Προσφέρει ταχύτητα και χαμηλή επιβάρυνση αντί για εγγυημένη παράδοση.",
                ),
                CalculationStep(
                    label="Βήμα 2 — Πότε η αξιοπιστία του TCP γίνεται μειονέκτημα",
                    description="Σε εφαρμογές πραγματικού χρόνου μια παλιά τιμή που επαναμεταδίδεται είναι άχρηστη: η επαναμετάδοση προσθέτει καθυστέρηση και jitter, ενώ η χειραψία 3 βημάτων καθυστερεί την έναρξη. Εκεί προτιμάται το best-effort UDP.",
                ),
                CalculationStep(
                    label="Βήμα 3 — Κατάλογος Τυπικών Εφαρμογών",
                    description="Τυπικές εφαρμογές UDP και ο λόγος προτίμησης συνοψίζονται στον παρακάτω πίνακα.",
                ),
            ],
            answer_tables=[
                AnalysisTable(
                    title="Εφαρμογές UDP & Λόγοι Προτίμησης έναντι του TCP",
                    headers=["Εφαρμογή", "Λόγος Προτίμησης UDP"],
                    rows=[
                        AnalysisRow(cells=["DNS (ερωτήματα/απαντήσεις)", "Ένα μικρό αίτημα-απάντηση ανά lookup· η επαναφυλλομέτρηση από την εφαρμογή είναι φθηνότερη από σύνδεση TCP"]),
                        AnalysisRow(cells=["VoIP / Τηλεφωνία", "Πραγματικός χρόνος: ένα χαμένο πακέτο προτιμάται από καθυστέρηση επαναμετάδοσης (jitter)"]),
                        AnalysisRow(cells=["Video streaming / Ζωντανή μετάδοση", "Συνεχής ροή: τα παλιά frames δεν χρειάζονται ξανά· multicast διανομή σε πολλούς δέκτες"]),
                        AnalysisRow(cells=["Online gaming", "Χαμηλή καθυστέρηση και απλότητα· η κατάσταση παιχνιδιού διορθώνεται από τα επόμενα πακέτα"]),
                        AnalysisRow(cells=["DHCP / TFTP / IGMP", "Απλά αιτήματα-απαντήσεις και ανακοινώσεις ομάδων· εκκίνηση χωρίς διαθέσιμη στοίβα σύνδεσης"]),
                    ],
                    note="Κοινός παρονομαστής: επικεφαλίδα 8 bytes ( έναντι 20 του TCP), καμία χειραψία, καμία αναμονή επιβεβαίωσης, δυνατότητα multicast.",
                ),
            ],
            answer="Το UDP προτιμάται σε DNS, VoIP, video streaming, online gaming και DHCP/TFTP/IGMP — λόγω ελάχιστης επικεφαλίδας (8 bytes), απουσίας χειραψίας και επαναμεταδόσεων (χαμηλή καθυστέρηση/jitter) και υποστήριξης multicast.",
            tips=[
                "Το DNS χρησιμοποιεί TCP μόνο σε zone transfers και μεγάλες απαντήσεις — τα απλά queries πάντα UDP θύρα 53.",
                "Αν η ερώτηση ζητά «για ποιους λόγους», απαντήστε με τα τρία: μικρή επικεφαλίδα, μηδενική καθυστέρηση σύνδεσης, ανοχή σε απώλειες πραγματικού χρόνου.",
            ],
        ),
        ExamQuestion(
            thema="Θέμα 3",
            thema_title="Επίπεδο Μεταφοράς — TCP vs UDP & Έλεγχος Ροής",
            sub_number="3.3",
            title="Ρόλος του TTL στην Επικεφαλίδα IPv4",
            question_type="theory",
            prompt="Εξηγήστε τον ρόλο του πεδίου TTL (Time to Live) στην επικεφαλίδα IPv4.",
            steps=[
                CalculationStep(
                    label="Βήμα 1 — Ορισμός & Μηχανισμός",
                    description="Το TTL είναι πεδίο 8-bit της επικεφαλίδας IPv4. Οριακά δέχεται τιμή 1–255· <strong>κάθε δρομολογητής που προωθεί το packet το μειώνει κατά 1</strong> πριν το προωθήσει.",
                ),
                CalculationStep(
                    label="Βήμα 2 — Προστασία από Βρόχους",
                    description="Αν due σε βρόχο δρομολόγησης (routing loop) το packet κυκλοφορεί επ' άπειρον, το TTL φθάνει στο 0: ο δρομολογητής <strong>απορρίπτει</strong> το packet και στέλνει στην πηγή μήνυμα <strong>ICMP Time Exceeded (Τύπος 11, Code 0)</strong>. Έτσι αποτρέπεται η κατάκλιση του δικτύου από αθάνατα πακέτα.",
                    latex=r"\text{TTL} \xrightarrow{\text{hop}} \text{TTL} - 1, \qquad \text{TTL} = 0 \Rightarrow \text{απόρριψη} + \text{ICMP Time Exceeded}",
                ),
                CalculationStep(
                    label="Βήμα 3 — Λειτουργική Χρήση (traceroute)",
                    description="Το εργαλείο traceroute αξιοποιεί το TTL: στέλνει packets με TTL = 1, 2, 3, ... και συλλέγει τα ICMP Time Exceeded των διαδοχικών δρομολογητών — χαρτογραφώντας έτσι τη διαδρομή hop-by-hop.",
                ),
            ],
            answer="Το TTL είναι μετρητής hops που μειώνεται κατά 1 από κάθε δρομολογητή· στο 0 το πακέτο απορρίπτεται με ICMP Time Exceeded προς την πηγή. Αποτρέπει την αιώνια κυκλοφορία πακέτων σε βρόχους δρομολόγησης και θεμελιώνει το traceroute.",
            tips=[
                "Ο προορισμός δεν μειώνει περαιτέρω το TTL· μετράει μόνο στους ενδιάμεσους δρομολογητές.",
                "Τυπικές αρχικές τιμές: 64 (Linux), 128 (Windows).",
            ],
        ),
        ExamQuestion(
            thema="Θέμα 4",
            thema_title="Αλγόριθμοι Δρομολόγησης",
            sub_number="4",
            title="Link-State (OSPF) vs Distance-Vector (RIP)",
            question_type="comparison",
            prompt="Συγκρίνετε τους αλγορίθμους δρομολόγησης Link-State (π.χ. OSPF) και Distance-Vector (π.χ. RIP) ως προς: Τον τρόπο ανταλλαγής πληροφορίας. Την ταχύτητα σύγκλισης (convergence time). Την ευπάθεια σε βρόχους δρομολόγησης (Routing Loops / Count-to-Infinity problem).",
            steps=[
                CalculationStep(
                    label="Κριτήριο 1 — Τρόπος Ανταλλαγής Πληροφορίας",
                    description="<strong>Link-State (OSPF):</strong> κάθε δρομολογητής συλλέγει την κατάσταση των γειτονικών του ζεύξεων και τη <strong>πλημυρικά (flooding) διαδίδει σε ΟΛΟΥΣ</strong> τους δρομολογητές της περιοχής (LSA). Έτσι όλοι αποκτούν την ίδια πλήρη τοπολογία και υπολογίζουν τοπικά τις βραχύτερες διαδρομές με <strong>Dijkstra (SPF)</strong>. <strong>Distance-Vector (RIP):</strong> κάθε δρομολογητής γνωρίζει μόνο τους <strong>γειτόνες</strong> και τους αποστέλλει περιοδικά (ανά 30 s) το διάνυσμα των αποστάσεών του (προορισμός → κόστος)· η ενημέρωση γίνεται με τη λογική Bellman-Ford: dx(y) = min over γείτονες v { c(x,v) + dv(y) }.",
                    latex=r"DV\text{: } D_x(y) = \min_{v \in \text{γείτονες}} \{ c(x,v) + D_v(y) \}",
                ),
                CalculationStep(
                    label="Κριτήριο 2 — Ταχύτητα Σύγκλισης",
                    description="<strong>LS:</strong> σύγκλιση σε <strong>δευτερόλεπτα</strong> — η τοπική αλλαγή διάδοσης πλημυρικά και ο Dijkstra επανεκτελείται αμέσως (event-triggered ενημερώσεις). <strong>DV:</strong> σύγκλιση σε <strong>λεπτά</strong> — η αλλαγή διαδίδεται hop-by-hop, ένα επίπεδο γειτόνων ανά περίοδο ενημέρωσης· στο RIP με όριο 15 hops (16 = άπειρο) οι μακρινές αλλαγές αργούν ακόμη περισσότερο.",
                ),
                CalculationStep(
                    label="Κριτήριο 3 — Ευπάθεια σε Βρόχους (Count-to-Infinity)",
                    description="<strong>LS:</strong> με καθολική, συνεπή εικόνα της τοπολογίας, ο Dijkstra παράγει ακυκλικό δένδρο SPF — ουσιαστικά <strong>απαλλαγμένο από βρόχους</strong>. <strong>DV:</strong> ευάλωτο στο <strong>count-to-infinity</strong>: αν η ζεύξη προς έναν προορισμό κοπεί, ο δρομολογητής ακούει από γείτονα (που δρομολογεί μέσα από αυτόν) κόστος = παλιό + 1 και το «ανεβάζει» βήμα-βήμα προς το άπειρο (3, 4, 5, ...), με πακέτα να κυκλοφορούν σε βρόχο meanwhile. Μετριασμοί: <strong>split horizon</strong> (μην διαφημίσεις διαδρομή πίσω από την πηγή της), <strong>poison reverse</strong> (διαφήμιση με κόστος ∞), <strong>triggered updates</strong> και το όριο 16 του RIP.",
                ),
            ],
            answer_tables=[
                AnalysisTable(
                    title="Συγκριτικός Πίνακας LS (OSPF) vs DV (RIP) — τα Τρία Κριτήρια του Θέματος",
                    headers=["Κριτήριο", "Link-State (OSPF)", "Distance-Vector (RIP)"],
                    rows=[
                        AnalysisRow(cells=["Ανταλλαγή πληροφορίας", "Πλημυρική διάδοση LSA (τοπικές ζεύξεις) σε όλους τους δρομολογητές· καθένας χτίζει πλήρη τοπολογία και τρέχει Dijkstra", "Ανταλλαγή διανυσμάτων απόστασης (προορισμός, κόστος) μόνο μεταξύ γειτόνων, περιοδικά ανά 30 s (Bellman-Ford)"], highlight=False),
                        AnalysisRow(cells=["Ταχύτητα σύγκλισης", "Γρήγορη — δευτερόλεπτα (event-triggered ενημερώσεις + τοπικός επανυπολογισμός SPF)", "Αργή — λεπτά (hop-by-hop διάδοση, περιοδικοί κύκλοι)· επιπλέον όριο 15 hops"], highlight=False),
                        AnalysisRow(cells=["Βρόχοι δρομολόγησης", "Ουσιαστικά απαλλαγμένο (καθολική εικόνα + ακυκλικό δένδρο SPF)", "Ευάλωτο σε count-to-infinity· μετριασμός με split horizon, poison reverse, triggered updates, max hops = 15/16 = ∞"], highlight=False),
                    ],
                    note="Επιπλέον διαφορές: μετρική κόστους/εύρους ζώνης (OSPF) έναντι hop count (RIP)· ιεραρχικές περιοχές & VLSM (OSPF) έναντι απλότητας μικρών δικτύων (RIP).",
                ),
            ],
            answer="LS: πλημυρική διάδοση σε όλους + Dijkstra, σύγκλιση σε δευτερόλεπτα, ουσιαστικά χωρίς βρόχους. DV: διανύσματα μόνο σε γείτονες + Bellman-Ford, σύγκλιση σε λεπτά, ευάλωτο σε count-to-infinity (split horizon / poison reverse / triggered updates / max 15 hops).",
            tips=[
                "Γράψτε και το παράδειγμα count-to-infinity: A–B κοπή → B ακούει από C κόστος 3 → 4 → 5 ... μέχρι το 16 (∞) του RIP.",
                "Και οι δύο οικογένειες είναι IGP· το BGP (πολιτικές, AS) είναι το EGP του διαδικτύου — μην το ανακατεύετε με OSPF/RIP.",
            ],
        ),
    ]

    layers = [
        ProtocolLayer(osi_position=7, osi_name="Εφαρμογής", osi_role="Υπηρεσίες δικτύου σε εφαρμογές τελικού χρήστη", tcpip_name="Εφαρμογής", pdu="Data / Message", protocols="HTTP/S, SMTP, FTP, DNS, TELNET, SNMP, SSH", correspondence="Τα OSI 5-7 συνενώνονται στο TCP/IP Εφαρμογής"),
        ProtocolLayer(osi_position=6, osi_name="Παρουσίασης", osi_role="Μορφοποίηση δεδομένων, κρυπτογράφηση, συμπίεση", tcpip_name="Εφαρμογής", pdu="Data / Message", protocols="MPEG, ASCII, SSL, TLS", correspondence="Ενσωματώνεται στις εφαρμογές / SSL-TLS"),
        ProtocolLayer(osi_position=5, osi_name="Συνόδου", osi_role="Διαχείριση συνόδων μεταξύ εφαρμογών", tcpip_name="Εφαρμογής", pdu="Data / Message", protocols="NetBIOS, SAP", correspondence="Ενσωματώνεται στη λογική της εφαρμογής"),
        ProtocolLayer(osi_position=4, osi_name="Μεταφοράς", osi_role="Έλεγχος λαθών & ροής, ports, αξιόπιστη μεταφορά", tcpip_name="Μεταφοράς", pdu="Segment (TCP) / Datagram (UDP)", protocols="TCP, UDP", correspondence="Πλήρης αντιστοίχιση 1:1"),
        ProtocolLayer(osi_position=3, osi_name="Δικτύου", osi_role="Λογική διευθυνσιοδότηση & δρομολόγηση", tcpip_name="Internet", pdu="Packet / IP Datagram", protocols="IP (v4/v6), ICMP, ARP, IGMP, OSPF", correspondence="Πλήρης αντιστοίχιση 1:1"),
        ProtocolLayer(osi_position=2, osi_name="Σύνδεσης Δεδομένων", osi_role="Διαμόρφωση πλαισίων, MAC, έλεγχος πρόσβασης", tcpip_name="Πρόσβασης Δικτύου", pdu="Frame", protocols="Ethernet, PPP, WiFi 802.11 (MAC/LLC)", correspondence="Τα OSI 1-2 συνενώνονται στην Πρόσβαση Δικτύου"),
        ProtocolLayer(osi_position=1, osi_name="Φυσικό", osi_role="Μετατροπή σε σήματα, καλώδια, ηλεκτρικά/οπτικά/ασύρματα", tcpip_name="Πρόσβασης Δικτύου", pdu="Bits", protocols="100BASE-TX, RS232, ISDN, IEEE 802.3 PHY", correspondence="Εντάσσεται στο PHY της Πρόσβασης"),
    ]

    analysis_tables = [
        AnalysisTable(
            title="Έλεγχος Επικαλύψεων & Εναπομένοντας Χώρου (Θέμα 2)",
            headers=["Τμήμα", "Εύρος", "Διευθύνσεις", "Σχόλιο"],
            rows=[
                AnalysisRow(cells=["Υποδίκτυο 1 (/26)", "192.168.100.0 – .63", "64", "0–63 χωρίς επικάλυψη με το επόμενο"]),
                AnalysisRow(cells=["Υποδίκτυο 2 (/27)", "192.168.100.64 – .95", "32", "ξεκινά στο .63 + 1"]),
                AnalysisRow(cells=["Υποδίκτυο 3 (/28)", "192.168.100.96 – .111", "16", "ξεκινά στο .95 + 1"]),
                AnalysisRow(cells=["Υποδίκτυο 4 (/30)", "192.168.100.112 – .115", "4", "ξεκινά στο .111 + 1"]),
                AnalysisRow(cells=["Ελεύθερο υπόλοιπο", "192.168.100.116 – .255", "140", "διάθεσιμο για μελλοντική επέκταση"], highlight=True),
                AnalysisRow(cells=["ΣΥΝΟΛΟ", "0 – 255", "256", "64 + 32 + 16 + 4 + 140 = 256 — πλήρης κάλυψη χωρίς κενά/επικαλύψεις"], highlight=True),
            ],
            note="Η αθροιστική επαλήθευση αποδεικνύει τη συνέχεια της κατανομής: κάθε επόμενο δίκτυο ξεκινά ακριβώς μετά το broadcast του προηγούμενου.",
        ),
    ]

    diagram_title = "Χάρτης Κατανομής VLSM: 192.168.100.0/24"
    diagram_nodes = [
        DiagramNode(id="parent", label="192.168.100.0/24 — Εταιρεία", x=430, y=24, w=340, details=["Μάσκα: 255.255.255.0", "Εύρος: .0 – .255 (256 διευθ.)"], highlight=True),
        DiagramNode(id="s1", label="Υποδίκτυο 1 — /26", x=30, y=210, w=235, details=["Μάσκα: 255.255.255.192", "Δίκτυο: 192.168.100.0", "Usable: .1 – .62", "Broadcast: .63", "Ανάγκη/Χωρητικότητα: 60/62"]),
        DiagramNode(id="s2", label="Υποδίκτυο 2 — /27", x=295, y=210, w=235, details=["Μάσκα: 255.255.255.224", "Δίκτυο: 192.168.100.64", "Usable: .65 – .94", "Broadcast: .95", "Ανάγκη/Χωρητικότητα: 28/30"]),
        DiagramNode(id="s3", label="Υποδίκτυο 3 — /28", x=560, y=210, w=235, details=["Μάσκα: 255.255.255.240", "Δίκτυο: 192.168.100.96", "Usable: .97 – .110", "Broadcast: .111", "Ανάγκη/Χωρητικότητα: 12/14"]),
        DiagramNode(id="s4", label="Υποδίκτυο 4 — /30 (p2p)", x=825, y=210, w=235, details=["Μάσκα: 255.255.255.252", "Δίκτυο: 192.168.100.112", "Usable: .113 – .114", "Broadcast: .115", "Ανάγκη/Χωρητικότητα: 2/2"]),
        DiagramNode(id="free", label="Ελεύθερος Χώρος (Επέκταση)", x=30, y=420, w=500, details=["Εύρος: 192.168.100.116 – .255", "Διαθέσιμες διευθύνσεις: 140"]),
    ]
    diagram_edges = [
        DiagramEdge(path="M 600,87 C 600,150 147,150 147,210", label="/26 (64)", lx=300, ly=143),
        DiagramEdge(path="M 600,87 C 600,150 412,150 412,210", label="/27 (32)", lx=495, ly=160),
        DiagramEdge(path="M 600,87 C 600,150 677,150 677,210", label="/28 (16)", lx=672, ly=160),
        DiagramEdge(path="M 600,87 C 600,150 942,150 942,210", label="/30 (4)", lx=880, ly=143),
        DiagramEdge(path="M 600,87 C 600,300 280,300 280,420", label="υπόλοιπο (140)", lx=405, ly=330, dashed=True),
    ]
    diagram_note = "Ο γονικός όγκος /24 τεμαχίζεται με φθίνουσα σειρά ανάγκης· κάθε block ξεκινά μετά το broadcast του προηγούμενου και το υπόλοιπο .116–.255 παραμένει ελεύθερο."

    justifications = [
        DesignJustification(
            title="1. Ταξινόμηση Κατά Φθίνουσα Σειρά (VLSM)",
            color_class="text-blue-500",
            description="Η επίλυση του μεγαλύτερου υποδικτύου πρώτο εξασφαλίζει ότι κάθε επόμενο block ξεκινά σε συνεχόμενο σημείο χωρίς επικαλύψεις — η κανονική μεθοδολογία VLSM.",
        ),
        DesignJustification(
            title="2. Ελάχιστη Ικανοποιούμενη Μάσκα ανά Υποδίκτυο",
            color_class="text-amber-500",
            description="/26 για 60 (62 usable), /27 για 28 (30), /28 για 12 (14), /30 για 2 (2): κάθε μάσκα είναι η μικρότερη που επαρκεί, ελαχιστοποιώντας τη σπατάλη διευθύνσεων.",
        ),
        DesignJustification(
            title="3. Το /30 ως Κανονική Επιλογή για p2p",
            color_class="text-emerald-500",
            description="Οι ζεύξεις σημείου-προς-σημείο δρομολογητών χρειάζονται ακριβώς 2 χρησιμοποιήσιμες διευθύνσεις — όσο δίνει το /30 (255.255.255.252), οπότε δεν σπαταλάται ούτε μία διεύθυνση.",
        ),
        DesignJustification(
            title="4. Συνέχεια Blocks & Ελεύθερο Υπόλοιπο",
            color_class="text-purple-500",
            description="Τα 4 blocks καταλαμβάνουν συνεχόμενα το .0–.115 και το .116–.255 παραμένει ενιαίο ελεύθερο: επεκτασιμότητα χωρίς ανακατανομή (re-addressing) των υπαρχόντων υποδικτύων.",
        ),
    ]

    solution_code = """# Θέμα 2: Αυτόματη επαλήθευση της κατανομής VLSM του 192.168.100.0/24
import ipaddress

requirements = [
    ("Υποδίκτυο 1 (υπολογιστές)", 60),
    ("Υποδίκτυο 2 (υπολογιστές)", 28),
    ("Υποδίκτυο 3 (υπολογιστές)", 12),
    ("Υποδίκτυο 4 (p2p δρομολογητές)", 2),
]

base = ipaddress.ip_network("192.168.100.0/24")
cursor = int(base.network_address)

# VLSM: μεγαλύτερη ανάγκη πρώτη — κάθε block ξεκινά στο broadcast+1 του προηγούμενου
for name, hosts in sorted(requirements, key=lambda item: -item[1]):
    host_bits = 1
    while 2 ** host_bits - 2 < hosts:
        host_bits += 1
    subnet = ipaddress.ip_network((cursor, 32 - host_bits))
    print(f"{name}: {subnet.with_prefixlen} | Μάσκα {subnet.netmask}")
    print(f"    First usable: {subnet.network_address + 1}")
    print(f"    Last usable:  {subnet.broadcast_address - 1}")
    print(f"    Broadcast:    {subnet.broadcast_address}")
    cursor = int(subnet.broadcast_address) + 1

free_start = ipaddress.ip_address(cursor)
free_count = int(base.broadcast_address) - cursor + 1
print(f"Ελεύθερος χώρος: {free_start} έως {base.broadcast_address} "
      f"({free_count} διευθύνσεις)")
"""

    return Scenario(
        id="past_exam_1",
        title="Επαναληπτικό Θέμα Εξετάσεων 1",
        subtitle="OSI/TCP-IP & Ενθυλάκωση · VLSM 192.168.100.0/24 · Sliding Window & TTL · LS vs DV",
        course_tag="NETWORKING (Εξέταση 1)",
        exam_meta=ExamMeta(duration="Διάρκεια: 2.5 ώρες", scoring="4 Θέματα × 2.5 μονάδες = 10"),
        paragraphs=paragraphs,
        questions=questions,
        layers=layers,
        analysis_tables=analysis_tables,
        diagram_title=diagram_title,
        diagram_nodes=diagram_nodes,
        diagram_edges=diagram_edges,
        diagram_note=diagram_note,
        justifications=justifications,
        solution_code=solution_code,
        code_language="python",
    )
