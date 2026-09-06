"""Synthetic Exam 1 (IPv4 Addressing, VLSM & CIDR) scenario module.

A complete synthetic exam paper authored in the exact structure of the
course's practice exam (4 Themata x 2.5 points, 2.5 hours), covering IP
class identification, RFC 1918 private ranges, special addresses, CIDR
mask conversion, a full VLSM design of 172.16.0.0/16, subnet parameter
extraction with binary AND, route summarization, and longest-prefix-match
routing table lookups. Every question carries a worked step-by-step solution.
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
    DiagramNode,
    DiagramEdge,
    DesignJustification,
    ExamQuestion,
)


def createSynthExam1Scenario() -> Scenario:
    """Constructs and returns the Synthetic Exam 1 (IP Addressing & VLSM) scenario.

    Returns:
        Scenario: Fully populated scenario instance.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(
                    text="<strong>Συνθετικό Θέμα Εξετάσεων 1: Δίκτυα Υπολογιστών — Διευθυνσιοδότηση & Υποδικτύωση</strong>",
                    is_highlight=True,
                    category="term",
                    tag_label="ΣΥΝΘΕΤΙΚΗ ΕΞΕΤΑΣΗ",
                    badge_class="badge-term",
                    tooltip="Ταξινόμηση: Συνθετικό θέμα εξετάσεων που καλύπτει το σύνολο της ύλης διευθυνσιοδότησης. Εντοπισμός: Τίτλος του συνθετικού θέματος. Εφαρμογή: Ακολουθεί δομή 4 Θεμάτων × 2.5 μονάδων όπως το επίσημο επαναληπτικό θέμα.",
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
                    tooltip="Ταξινόμηση: Χρονικό όριο εξέτασης. Εντοπισμός: Επίσημη οδηγία. Εφαρμογή: Περίπου 35 λεπτά ανά Θέμα.",
                ),
                TextSegment(text=". "),
                TextSegment(
                    text="Όλα τα θέματα βαθμολογούνται με 2.5 μονάδες",
                    is_highlight=True,
                    category="given",
                    tag_label="ΒΑΘΜΟΛΟΓΙΑ",
                    badge_class="badge-given",
                    tooltip="Ταξινόμηση: Κανόνας βαθμολόγησης (σύνολο 10). Εντοπισμός: Επίσημη οδηγία. Εφαρμογή: Όλα τα Θέματα σταθμίζουν εξίσου.",
                ),
                TextSegment(text="."),
            ],
        ),
        Paragraph(
            segments=[
                TextSegment(
                    text="Θέμα 1: Θεμελιώδεις Έννοιες Διευθυνσιοδότησης IPv4 (Πολλαπλής Επιλογής)",
                    is_highlight=True,
                    category="term",
                    tag_label="MCQ",
                    badge_class="badge-term",
                    tooltip="Ταξινόμηση: Θέμα πολλαπλής επιλογής πάνω σε κλάσεις, ιδιωτικά εύρη και μορφές μάσκας. Εντοπισμός: Επικεφαλίδα «Θέμα 1». Εφαρμογή: Κάθε ερώτημα α-δ λύνεται με τα εύρη των κλάσεων και τις ισοδυναμίες μάσκας/CIDR.",
                ),
            ],
            is_heading=True,
        ),
        Paragraph(
            segments=[
                TextSegment(text="α. Σε ποια κλάση ανήκει η διεύθυνση IP "),
                TextSegment(
                    text="172.16.50.100",
                    is_highlight=True,
                    category="given",
                    tag_label="ΔΕΔΟΜΕΝΟ",
                    badge_class="badge-given",
                    tooltip="Ταξινόμηση: Διεύθυνση προς ταξινόμηση κλάσης. Εντοπισμός: Ερώτημα α του Θέματος 1. Εφαρμογή: Το πρώτο οκτάδιο 172 καθορίζει την κλάση (εύρος 128-191 = Κλάση B).",
                ),
                TextSegment(text=";"),
            ],
        ),
        Paragraph(
            segments=[
                TextSegment(text="β. Ποιο από τα παρακάτω εύρη "),
                TextSegment(
                    text="ΔΕΝ ανήκει στα ιδιωτικά εύρη του RFC 1918",
                    is_highlight=True,
                    category="term",
                    tag_label="ΤΕΧΝΙΚΟΣ ΟΡΟΣ",
                    badge_class="badge-term",
                    tooltip="Ταξινόμηση: Κανόνας ιδιωτικής διευθυνσιοδότησης RFC 1918. Εντοπισμός: Λέξη-κλειδί «RFC 1918» στο ερώτημα β. Εφαρμογή: Συγκρίνονται τα τέσσερα εύρη με τα 10/8, 172.16/12, 192.168/16.",
                ),
                TextSegment(text=";"),
            ],
        ),
        Paragraph(
            segments=[
                TextSegment(text="γ. Η διεύθυνση "),
                TextSegment(
                    text="127.0.0.1",
                    is_highlight=True,
                    category="given",
                    tag_label="ΔΕΔΟΜΕΝΟ",
                    badge_class="badge-given",
                    tooltip="Ταξινόμηση: Ειδική διεύθυνση loopback. Εντοπισμός: Ερώτημα γ του Θέματος 1. Εφαρμογή: Ζητείται ο σκοπός της διεύθυνσης localhost.",
                ),
                TextSegment(text=" χρησιμοποιείται ως:"),
            ],
        ),
        Paragraph(
            segments=[
                TextSegment(text="δ. Η μάσκα υποδικτύου "),
                TextSegment(
                    text="255.255.240.0",
                    is_highlight=True,
                    category="given",
                    tag_label="ΔΕΔΟΜΕΝΟ",
                    badge_class="badge-given",
                    tooltip="Ταξινόμηση: Μάσκα προς μετατροπή σε CIDR. Εντοπισμός: Ερώτημα δ του Θέματος 1. Εφαρμογή: Το 240 = 11110000 δίνει 4 άσσους στο 3ο οκτάδιο → πρόθεμα 16 + 4 = /20.",
                ),
                TextSegment(text=" σε μορφή CIDR ισοδυναμεί με:"),
            ],
        ),
        Paragraph(
            segments=[
                TextSegment(
                    text="Θέμα 2: Σχεδίαση Υποδικτύωσης VLSM",
                    is_highlight=True,
                    category="method",
                    tag_label="ΥΠΟΛΟΓΙΣΤΙΚΟ",
                    badge_class="badge-method",
                    tooltip="Ταξινόμηση: Υπολογιστικό θέμα σχεδίασης VLSM. Εντοπισμός: Επικεφαλίδα «Θέμα 2». Εφαρμογή: Λύνεται με ταξινόμηση κατά φθίνουσα σειρά και εφαρμογή 2^h - 2 ≥ hosts.",
                ),
            ],
            is_heading=True,
        ),
        Paragraph(
            segments=[
                TextSegment(text="Ένας οργανισμός λαμβάνει το μπλοκ διευθύνσεων "),
                TextSegment(
                    text="172.16.0.0/16",
                    is_highlight=True,
                    category="given",
                    tag_label="ΔΕΔΟΜΕΝΟ",
                    badge_class="badge-given",
                    tooltip="Ταξινόμηση: Αρχικό block (ιδιωτικό εύρος 172.16.0.0/12, Κλάση B). Εντοπισμός: Ρητό δεδομένο του Θέματος 2. Εφαρμογή: 65.536 συνολικές διευθύνσεις προς κατανομή VLSM.",
                ),
                TextSegment(text=" και απαιτείται να σχεδιαστούν 5 υποδίκτυα με τις εξής ανάγκες:"),
            ],
        ),
        Paragraph(segments=[TextSegment(text="Δίκτυο A: "), TextSegment(text="5000 hosts", is_highlight=True, category="given", tag_label="ΑΝΑΓΚΗ: 5000", badge_class="badge-given", tooltip="Ταξινόμηση: Μεγαλύτερη απαίτηση φιλοξενίας. Εντοπισμός: Πρώτη γραμμή της λίστας του Θέματος 2. Εφαρμογή: 2^h - 2 ≥ 5000 → h = 13 (8190) → /19, block 32 × /24.")]),
        Paragraph(segments=[TextSegment(text="Δίκτυο B: "), TextSegment(text="2000 hosts", is_highlight=True, category="given", tag_label="ΑΝΑΓΚΗ: 2000", badge_class="badge-given", tooltip="Ταξινόμηση: Δεύτερη απαίτηση. Εντοπισμός: Λίστα Θέματος 2. Εφαρμογή: h = 11 (2046) → /21, block 8 × /24.")]),
        Paragraph(segments=[TextSegment(text="Δίκτυο C: "), TextSegment(text="500 hosts", is_highlight=True, category="given", tag_label="ΑΝΑΓΚΗ: 500", badge_class="badge-given", tooltip="Ταξινόμηση: Τρίτη απαίτηση. Εντοπισμός: Λίστα Θέματος 2. Εφαρμογή: h = 9 (510) → /23, block 2 × /24.")]),
        Paragraph(segments=[TextSegment(text="Δίκτυο D: "), TextSegment(text="100 hosts", is_highlight=True, category="given", tag_label="ΑΝΑΓΚΗ: 100", badge_class="badge-given", tooltip="Ταξινόμηση: Τέταρτη απαίτηση. Εντοπισμός: Λίστα Θέματος 2. Εφαρμογή: h = 7 (126) → /25.")]),
        Paragraph(segments=[TextSegment(text="Δίκτυο E: "), TextSegment(text="2 hosts (ζεύξη σημείου-προς-σημείο)", is_highlight=True, category="given", tag_label="ΑΝΑΓΚΗ: 2 (p2p)", badge_class="badge-given", tooltip="Ταξινόμηση: Ζεύξη p2p δρομολογητών. Εντοπισμός: Τελευταία γραμμή της λίστας. Εφαρμογή: h = 2 → /30 με ακριβώς 2 χρησιμοποιήσιμους hosts.")]),
        Paragraph(
            segments=[
                TextSegment(text="Για κάθε δίκτυο δώστε: "),
                TextSegment(
                    text="Διεύθυνση Υποδικτύου, Μάσκα, Πρώτο/Τελευταίο Έγκυρο Host, Διεύθυνση Broadcast",
                    is_highlight=True,
                    category="method",
                    tag_label="ΖΗΤΟΥΜΕΝΑ",
                    badge_class="badge-method",
                    tooltip="Ταξινόμηση: Οι ζητούμενες στήλες της απάντησης VLSM. Εντοπισμός: Κλείσιμο της εκφώνησης του Θέματος 2. Εφαρμογή: Η λύση ολοκληρώνεται με πίνακα 5 γραμμών.",
                ),
                TextSegment(text="."),
            ],
        ),
        Paragraph(
            segments=[
                TextSegment(
                    text="Θέμα 3: Παράμετροι Υποδικτύου",
                    is_highlight=True,
                    category="method",
                    tag_label="ΥΠΟΛΟΓΙΣΤΙΚΟ",
                    badge_class="badge-method",
                    tooltip="Ταξινόμηση: Ανάλυση μεμονωμένης διεύθυνσης με πρόθεμα. Εντοπισμός: Επικεφαλίδα «Θέμα 3». Εφαρμογή: Λύνεται με bitwise AND της IP με τη μάσκα.",
                ),
            ],
            is_heading=True,
        ),
        Paragraph(
            segments=[
                TextSegment(text="Δίνεται η διεύθυνση IP ενός υπολογιστή: "),
                TextSegment(
                    text="172.16.45.130/22",
                    is_highlight=True,
                    category="given",
                    tag_label="ΔΕΔΟΜΕΝΟ",
                    badge_class="badge-given",
                    tooltip="Ταξινόμηση: Διεύθυνση σταθμού με πρόθεμα /22. Εντοπισμός: Ρητό δεδομένο του Θέματος 3. Εφαρμογή: 22 bits δικτύου → μάσκα 255.255.252.0 → 10 bits hosts.",
                ),
                TextSegment(text="."),
            ],
        ),
        Paragraph(segments=[TextSegment(text="α. Ποια είναι η "), TextSegment(text="μάσκα υποδικτύου", is_highlight=True, category="term", tag_label="ΖΗΤΟΥΜΕΝΟ", badge_class="badge-term", tooltip="Ταξινόμηση: Ζητούμενη μάσκα σε δεκαδική μορφή. Εντοπισμός: Ερώτημα α. Εφαρμογή: /22 → 11111111.11111111.11111100.00000000 → 255.255.252.0.")]),
        Paragraph(segments=[TextSegment(text="β. Ποια είναι η "), TextSegment(text="διεύθυνση δικτύου", is_highlight=True, category="term", tag_label="ΖΗΤΟΥΜΕΝΟ", badge_class="badge-term", tooltip="Ταξινόμηση: Network Address. Εντοπισμός: Ερώτημα β. Εφαρμογή: Bitwise AND: 45 AND 252 = 44 → 172.16.44.0.")]),
        Paragraph(segments=[TextSegment(text="γ. Ποια είναι η "), TextSegment(text="διεύθυνση εκπομπής (broadcast)", is_highlight=True, category="term", tag_label="ΖΗΤΟΥΜΕΝΟ", badge_class="badge-term", tooltip="Ταξινόμηση: Broadcast Address. Εντοπισμός: Ερώτημα γ. Εφαρμογή: Host bits όλα 1 → 172.16.47.255.")]),
        Paragraph(segments=[TextSegment(text="δ. Ποιο είναι το "), TextSegment(text="εύρος των έγκυρων διευθύνσεων", is_highlight=True, category="term", tag_label="ΖΗΤΟΥΜΕΝΟ", badge_class="badge-term", tooltip="Ταξινόμηση: Usable host range. Εντοπισμός: Ερώτημα δ. Εφαρμογή: .44.1 έως .47.254.")]),
        Paragraph(segments=[TextSegment(text="ε. Πόσοι συνολικά "), TextSegment(text="υπολογιστές", is_highlight=True, category="term", tag_label="ΖΗΤΟΥΜΕΝΟ", badge_class="badge-term", tooltip="Ταξινόμηση: Μέγιστος αριθμός hosts. Εντοπισμός: Ερώτημα ε. Εφαρμογή: 2^10 - 2 = 1022.")]),
        Paragraph(
            segments=[
                TextSegment(
                    text="Θέμα 4: Σύνοψη Διαδρομών (CIDR) & Πίνακες Δρομολόγησης",
                    is_highlight=True,
                    category="method",
                    tag_label="ΥΠΟΛΟΓΙΣΤΙΚΟ",
                    badge_class="badge-method",
                    tooltip="Ταξινόμηση: Θέμα σύνοψης διαδρομών και αναζήτησης πίνακα δρομολόγησης. Εντοπισμός: Επικεφαλίδα «Θέμα 4». Εφαρμογή: Κοινά αρχικά bits για την σύνοψη· longest prefix match για τα next hops.",
                ),
            ],
            is_heading=True,
        ),
        Paragraph(
            segments=[
                TextSegment(text="1. Διαθέτετε τα δίκτυα "),
                TextSegment(
                    text="192.168.16.0/24, 192.168.17.0/24, 192.168.18.0/24, 192.168.19.0/24",
                    is_highlight=True,
                    category="given",
                    tag_label="ΔΕΔΟΜΕΝΑ",
                    badge_class="badge-given",
                    tooltip="Ταξινόμηση: Τέσσερα διαδοχικά δίκτυα /24. Εντοπισμός: Ρητά δεδομένα του ερωτήματος 1. Εφαρμογή: Η σύνοψη προκύπτει από τα κοινά αρχικά bits του τρίτου οκταδίου (16-19 = 000100xx).",
                ),
                TextSegment(text=". Βρείτε τη "),
                TextSegment(
                    text="μία διαδρομή CIDR",
                    is_highlight=True,
                    category="method",
                    tag_label="ΖΗΤΟΥΜΕΝΟ",
                    badge_class="badge-method",
                    tooltip="Ταξινόμηση: Route summarization (supernet). Εντοπισμός: «μία διαδρομή CIDR που τα συνοψίζει όλα». Εφαρμογή: Νέο πρόθεμα = 16 + 4 κοινά bits = /22.",
                ),
                TextSegment(text=" που τα συνοψίζει όλα."),
            ],
        ),
        Paragraph(
            segments=[
                TextSegment(text="2. Δοθέντος του παρακάτω "),
                TextSegment(
                    text="πίνακα δρομολόγησης",
                    is_highlight=True,
                    category="given",
                    tag_label="ΔΕΔΟΜΕΝΑ",
                    badge_class="badge-given",
                    tooltip="Ταξινόμηση: Πίνακας δρομολόγησης με 4 γραμμές (δημοφιλείς + default). Εντοπισμός: Πεδίο δεδομένων του ερωτήματος 2. Εφαρμογή: Για κάθε προορισμό εφαρμόζεται longest prefix match.",
                ),
                TextSegment(text=", προσδιορίστε το επόμενο άλμα για πακέτα με προορισμό: a) 192.168.50.25, b) 10.0.0.5, c) 172.16.100.50, d) 8.8.8.8."),
            ],
        ),
        Paragraph(
            segments=[
                TextSegment(text="<code>Destination&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Netmask&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Gateway&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Interface</code><br><code>192.168.50.0&nbsp;&nbsp;&nbsp;255.255.255.0&nbsp;&nbsp;&nbsp;0.0.0.0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;eth0</code><br><code>10.0.0.0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;255.0.0.0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;192.168.50.1&nbsp;&nbsp;&nbsp;&nbsp;eth0</code><br><code>172.16.0.0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;255.255.0.0&nbsp;&nbsp;&nbsp;&nbsp;192.168.50.2&nbsp;&nbsp;&nbsp;&nbsp;eth0</code><br><code>0.0.0.0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0.0.0.0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;192.168.50.254&nbsp;eth0</code>"),
            ],
            accent_border_color="accent",
        ),
    ]

    questions = [
        ExamQuestion(
            thema="Θέμα 1",
            thema_title="Θεμελιώδεις Έννοιες Διευθυνσιοδότησης IPv4 (Πολλαπλής Επιλογής)",
            sub_number="1α",
            title="Ταξινόμηση Κλάσης της 172.16.50.100",
            question_type="mcq",
            prompt="Σε ποια κλάση ανήκει η διεύθυνση IP 172.16.50.100;",
            options=[
                QuestionOption(letter="A", text="Κλάση A", is_correct=False, explanation="Η Κλάση A καλύπτει πρώτο οκτάδιο 0-127 (αρχικό bit 0)· το 172 είναι εκτός εύρους."),
                QuestionOption(letter="B", text="Κλάση B", is_correct=True, explanation="Πρώτο οκτάδιο 128-191 (αρχικά bits 10)· το 172 ανήκει στο 128-191, άρα Κλάση B με προεπιλεγμένη μάσκα 255.255.0.0 (/16). Επιπλέον, επειδή 172.16.x.x βρίσκεται στο 172.16.0.0/12, είναι και ιδιωτική διεύθυνση RFC 1918."),
                QuestionOption(letter="C", text="Κλάση C", is_correct=False, explanation="Η Κλάση C καλύπτει 192-223 (αρχικά bits 110)· το 172 είναι μικρότερο του 192."),
                QuestionOption(letter="D", text="Κλάση D (multicast)", is_correct=False, explanation="Η Κλάση D καλύπτει 224-239 (αρχικά bits 1110) και χρησιμοποιείται για multicast ομάδες, όχι για σταθμούς."),
            ],
            answer="Σωστή απάντηση: <strong>B</strong> — Κλάση B (πρώτο οκτάδιο 128-191), ιδιωτική διεύθυνση εντός του 172.16.0.0/12.",
            tips=["Ο ορισμός της κλάσης βγαίνει από τα πρώτα bits του πρώτου οκταδίου: 0→A, 10→B, 110→C, 1110→D, 1111→E.", "Το 172.16.50.100 είναι ταυτόχρονα και ιδιωτική (RFC 1918) — αναφέρετε και τα δύο στη γραπτή απάντηση."],
        ),
        ExamQuestion(
            thema="Θέμα 1",
            thema_title="Θεμελιώδεις Έννοιες Διευθυνσιοδότησης IPv4 (Πολλαπλής Επιλογής)",
            sub_number="1β",
            title="Εύρος εκτός RFC 1918",
            question_type="mcq",
            prompt="Ποιο από τα παρακάτω εύρη ΔΕΝ ανήκει στα ιδιωτικά εύρη του RFC 1918;",
            options=[
                QuestionOption(letter="A", text="10.0.0.0/8 (10.0.0.0 - 10.255.255.255)", is_correct=False, explanation="Είναι το ιδιωτικό εύρος της Κλάσης A του RFC 1918 — άρα ανήκει, δεν είναι η σωστή απάντηση."),
                QuestionOption(letter="B", text="172.16.0.0/12 (172.16.0.0 - 172.31.255.255)", is_correct=False, explanation="Είναι το ιδιωτικό εύρος της Κλάσης B του RFC 1918 — ανήκει στα ιδιωτικά εύρη."),
                QuestionOption(letter="C", text="192.168.0.0/16 (192.168.0.0 - 192.168.255.255)", is_correct=False, explanation="Είναι το ιδιωτικό εύρος της Κλάσης C του RFC 1918 — ανήκει στα ιδιωτικά εύρη."),
                QuestionOption(letter="D", text="169.254.0.0/16 (169.254.0.0 - 169.254.255.255)", is_correct=True, explanation="Είναι διευθύνσεις APIPA / link-local (RFC 3927): εκχωρούνται αυτόματα όταν αποτύχει το DHCP. ΔΕΝ ανήκουν στο RFC 1918 και δεν δρομολογούνται στο διαδίκτυο."),
            ],
            answer="Σωστή απάντηση: <strong>D</strong> — το 169.254.0.0/16 είναι APIPA/link-local, όχι ιδιωτικό εύρος RFC 1918.",
            tips=["Τα RFC 1918 εύρη είναι ακριβώς τρία: 10/8, 172.16/12 (μέχρι 172.31!), 192.168/16 — προσέξτε ότι το /12 σταματά στο 172.31.255.255.", "Το 169.254.x.x σημαίνει συνήθως αποτυχία DHCP — κλασικό διαγνωστικό σημάδι."],
        ),
        ExamQuestion(
            thema="Θέμα 1",
            thema_title="Θεμελιώδεις Έννοιες Διευθυνσιοδότησης IPv4 (Πολλαπλής Επιλογής)",
            sub_number="1γ",
            title="Χρήση της 127.0.0.1",
            question_type="mcq",
            prompt="Η διεύθυνση 127.0.0.1 χρησιμοποιείται ως:",
            options=[
                QuestionOption(letter="A", text="Διεύθυνση loopback (localhost) για τοπικό έλεγχο της στοίβας TCP/IP", is_correct=True, explanation="Στέλνοντας ping 127.0.0.1 ελέγχεται ότι η στοίβα πρωτοκόλλων του λειτουργικού λειτουργεί, χωρίς κανένα πακέτο να φτάσει ποτέ στο φυσικό δίκτυο (όλο το 127.0.0.0/8 είναι loopback)."),
                QuestionOption(letter="B", text="Τοπική διεύθυνση broadcast", is_correct=False, explanation="Η τοπική/περιορισμένη broadcast είναι η 255.255.255.255 — δεν σχετίζεται με το loopback."),
                QuestionOption(letter="C", text="Προεπιλεγμένη πύλη (default gateway)", is_correct=False, explanation="Η default gateway είναι η IP ενός δρομολογητή στο τοπικό δίκτυο (συνήθως .1), όχι διεύθυνση loopback."),
                QuestionOption(letter="D", text="Διεύθυνση διακομιστή DNS", is_correct=False, explanation="Οι διακομιστές DNS χρησιμοποιούν κανονικές διευθύνσεις δικτύου (π.χ. 8.8.8.8), όχι loopback."),
            ],
            answer="Σωστή απάντηση: <strong>A</strong> — loopback (localhost) για δοκιμή της τοπικής στοίβας TCP/IP.",
            tips=["Σειρά διαγνωστικών: ping 127.0.0.1 (στοίβα) → ping δική μου IP (NIC) → ping gateway (L2/L3) → ping εξωτερικός σταθμός (δρομολόγηση)."],
        ),
        ExamQuestion(
            thema="Θέμα 1",
            thema_title="Θεμελιώδεις Έννοιες Διευθυνσιοδότησης IPv4 (Πολλαπλής Επιλογής)",
            sub_number="1δ",
            title="Μετατροπή 255.255.240.0 σε CIDR",
            question_type="mcq",
            prompt="Η μάσκα υποδικτύου 255.255.240.0 σε μορφή CIDR ισοδυναμεί με:",
            options=[
                QuestionOption(letter="A", text="/20", is_correct=True, explanation="240 = 11110000, δηλαδή 4 άσσοι στο τρίτο οκτάδιο: 8 + 8 + 4 = 20 bits δικτύου. Η /20 δίνει 12 bits hosts = 4094 hosts και block 16 × /24."),
                QuestionOption(letter="B", text="/22", is_correct=False, explanation="Η /22 ισοδυναμεί με 255.255.252.0 (252 = 11111100, 6 άσσοι στο τρίτο οκτάδιο)."),
                QuestionOption(letter="C", text="/24", is_correct=False, explanation="Η /24 ισοδυναμεί με 255.255.255.0 (το τρίτο οκτάδιο γεμάτο άσσους = 255)."),
                QuestionOption(letter="D", text="/28", is_correct=False, explanation="Η /28 ισοδυναμεί με 255.255.255.240 — το 240 εμφανίζεται στο τέταρτο, όχι στο τρίτο οκτάδιο."),
            ],
            answer="Σωστή απάντηση: <strong>A</strong> — /20 (240 = 11110000 → 4 άσσοι στο 3ο οκτάδιο → 16 + 4 = 20).",
            tips=["Παγίδα: το 240 μπορεί να βρίσκεται σε διαφορετικό οκτάδιο — /20 = 255.255.240.0 αλλά /28 = 255.255.255.240.", "Γρήγορος κανόνας: 128→1, 192→2, 224→3, 240→4, 248→5, 252→6, 254→7, 255→8 άσσοι ανά οκτάδιο."],
        ),
        ExamQuestion(
            thema="Θέμα 2",
            thema_title="Σχεδίαση Υποδικτύωσης VLSM",
            sub_number="2",
            title="Κατανομή VLSM του 172.16.0.0/16 σε 5 Δίκτυα",
            question_type="computational",
            prompt="Ένας οργανισμός λαμβάνει το μπλοκ διευθύνσεων 172.16.0.0/16 και απαιτείται να σχεδιαστούν 5 υποδίκτυα: Δίκτυο A: 5000 hosts, Δίκτυο B: 2000 hosts, Δίκτυο C: 500 hosts, Δίκτυο D: 100 hosts, Δίκτυο E: 2 hosts (p2p). Για κάθε δίκτυο δώστε: Διεύθυνση Υποδικτύου, Μάσκα, Πρώτο/Τελευταίο Έγκυρο Host, Διεύθυνση Broadcast.",
            given=[
                GivenParameter(label="Αρχικό block", value="172.16.0.0/16 (65.536 διευθ.)", source="εκφώνηση Θέματος 2"),
                GivenParameter(label="Δίκτυο A", value="5000 hosts", source="λίστα εκφώνησης"),
                GivenParameter(label="Δίκτυο B", value="2000 hosts", source="λίστα εκφώνησης"),
                GivenParameter(label="Δίκτυο C", value="500 hosts", source="λίστα εκφώνησης"),
                GivenParameter(label="Δίκτυο D", value="100 hosts", source="λίστα εκφώνησης"),
                GivenParameter(label="Δίκτυο E", value="2 hosts (p2p)", source="λίστα εκφώνησης"),
            ],
            steps=[
                CalculationStep(
                    label="Βήμα 1 — Ταξινόμηση Κατά Φθίνουσα Σειρά",
                    description="Σειρά κατανομής: 5000 → 2000 → 500 → 100 → 2. Το μεγαλύτερο δίκτυο παίρνει πρώτο τη μικρότερη μάσκα (περισσότερα host bits) ώστε τα blocks να είναι συνεχόμενα χωρίς επικαλύψεις.",
                ),
                CalculationStep(
                    label="Βήμα 2 — Δίκτυο A (5000 hosts)",
                    description="Ζητούμε το ελάχιστο h με 2^h − 2 ≥ 5000: h = 12 δίνει 4094 (ανεπαρκές), h = 13 δίνει 8190 ≥ 5000. Πρόθεμα /19, μάσκα 255.255.224.0, block 32 × /24 = 8192 διευθύνσεις, ξεκινώντας από το 172.16.0.0.",
                    latex=r"2^{13} - 2 = 8190 \ge 5000 \Rightarrow h = 13 \Rightarrow /19,\; \text{block} = 8192",
                    result="Δίκτυο A: 172.16.0.0/19 · Usable 172.16.0.1 – 172.16.31.254 · BC 172.16.31.255",
                ),
                CalculationStep(
                    label="Βήμα 3 — Δίκτυο B (2000 hosts)",
                    description="Επόμενο ελεύθερο σημείο: 172.16.31.255 + 1 = 172.16.32.0. Για 2000 hosts: h = 11 (2^11 − 2 = 2046 ≥ 2000), πρόθεμα /21, μάσκα 255.255.248.0, block 8 × /24 = 2048.",
                    latex=r"2^{11} - 2 = 2046 \ge 2000 \Rightarrow h = 11 \Rightarrow /21,\; \text{start} = 172.16.32.0",
                    result="Δίκτυο B: 172.16.32.0/21 · Usable 172.16.32.1 – 172.16.39.254 · BC 172.16.39.255",
                ),
                CalculationStep(
                    label="Βήμα 4 — Δίκτυο C (500 hosts)",
                    description="Επόμενο ελεύθερο: 172.16.39.255 + 1 = 172.16.40.0. Για 500 hosts: h = 9 (2^9 − 2 = 510 ≥ 500), πρόθεμα /23, μάσκα 255.255.254.0, block 2 × /24 = 512.",
                    latex=r"2^{9} - 2 = 510 \ge 500 \Rightarrow h = 9 \Rightarrow /23,\; \text{start} = 172.16.40.0",
                    result="Δίκτυο C: 172.16.40.0/23 · Usable 172.16.40.1 – 172.16.41.254 · BC 172.16.41.255",
                ),
                CalculationStep(
                    label="Βήμα 5 — Δίκτυο D (100 hosts)",
                    description="Επόμενο ελεύθερο: 172.16.41.255 + 1 = 172.16.42.0. Για 100 hosts: h = 7 (2^7 − 2 = 126 ≥ 100), πρόθεμα /25, μάσκα 255.255.255.128, block 128.",
                    latex=r"2^{7} - 2 = 126 \ge 100 \Rightarrow h = 7 \Rightarrow /25,\; \text{start} = 172.16.42.0",
                    result="Δίκτυο D: 172.16.42.0/25 · Usable 172.16.42.1 – 172.16.42.126 · BC 172.16.42.127",
                ),
                CalculationStep(
                    label="Βήμα 6 — Δίκτυο E (2 hosts, p2p)",
                    description="Επόμενο ελεύθερο: 172.16.42.127 + 1 = 172.16.42.128. Για τη ζεύξη p2p: h = 2 (2^2 − 2 = 2), πρόθεμα /30, μάσκα 255.255.255.252, block 4.",
                    latex=r"2^{2} - 2 = 2 \Rightarrow h = 2 \Rightarrow /30,\; \text{start} = 172.16.42.128",
                    result="Δίκτυο E: 172.16.42.128/30 · Usable 172.16.42.129 – 172.16.42.130 · BC 172.16.42.131",
                ),
                CalculationStep(
                    label="Βήμα 7 — Επαλήθευση Χώρου",
                    description="Καταλαμβανόμενες διευθύνσεις: 8192 + 2048 + 512 + 128 + 4 = 10884 στο 172.16.0.0 – 172.16.42.131. Το υπόλοιπο 172.16.42.132 – 172.16.255.255 (54.652 διευθύνσεις) παραμένει ελεύθερο για επέκταση.",
                    latex=r"8192 + 2048 + 512 + 128 + 4 = 10884 \le 65536",
                ),
            ],
            answer_tables=[
                AnalysisTable(
                    title="Τελικός Πίνακας VLSM (Ζητούμενη Απάντηση)",
                    headers=["Δίκτυο", "Ανάγκη", "Υποδίκτυο", "Μάσκα (CIDR)", "First / Last Usable", "Broadcast"],
                    rows=[
                        AnalysisRow(cells=["A", "5000", "172.16.0.0/19", "255.255.224.0", "172.16.0.1 / 172.16.31.254", "172.16.31.255"], highlight=True),
                        AnalysisRow(cells=["B", "2000", "172.16.32.0/21", "255.255.248.0", "172.16.32.1 / 172.16.39.254", "172.16.39.255"], highlight=True),
                        AnalysisRow(cells=["C", "500", "172.16.40.0/23", "255.255.254.0", "172.16.40.1 / 172.16.41.254", "172.16.41.255"], highlight=True),
                        AnalysisRow(cells=["D", "100", "172.16.42.0/25", "255.255.255.128", "172.16.42.1 / 172.16.42.126", "172.16.42.127"], highlight=True),
                        AnalysisRow(cells=["E (p2p)", "2", "172.16.42.128/30", "255.255.255.252", "172.16.42.129 / 172.16.42.130", "172.16.42.131"], highlight=True),
                    ],
                    note="Χωρητικότητες: 8190 / 2046 / 510 / 126 / 2 hosts — καθεμία η ελάχιστη που ικανοποιεί την αντίστοιχη ανάγκη.",
                ),
            ],
            answer="A: 172.16.0.0/19 · B: 172.16.32.0/21 · C: 172.16.40.0/23 · D: 172.16.42.0/25 · E: 172.16.42.128/30 (p2p) — με BC 31.255 / 39.255 / 41.255 / 42.127 / 42.131 αντίστοιχα.",
            tips=[
                "Για το A μην επιλέξετε h = 12 (4094 < 5000) — το ελάχιστο ικανοποιούν h είναι 13.",
                "Το /23 του C καλύπτει ακριβώς 510 hosts — αν η ανάγκη ήταν 511, θα χρειαζόταν /22.",
                "Έλεγχος συνέχειας: 31.255+1=32.0, 39.255+1=40.0, 41.255+1=42.0, 42.127+1=42.128.",
            ],
        ),
        ExamQuestion(
            thema="Θέμα 3",
            thema_title="Παράμετροι Υποδικτύου",
            sub_number="3",
            title="Ανάλυση της 172.16.45.130/22 (α-ε)",
            question_type="computational",
            prompt="Δίνεται η διεύθυνση IP ενός υπολογιστή: 172.16.45.130/22. α. Ποια είναι η μάσκα υποδικτύου σε δεκαδική μορφή; β. Ποια είναι η διεύθυνση δικτύου; γ. Ποια είναι η διεύθυνση εκπομπής (broadcast); δ. Ποιο είναι το εύρος των έγκυρων διευθύνσεων; ε. Πόσοι συνολικά υπολογιστές μπορούν να συνδεθούν;",
            given=[
                GivenParameter(label="Διεύθυνση σταθμού", value="172.16.45.130", source="εκφώνηση Θέματος 3"),
                GivenParameter(label="Πρόθεμα", value="/22", source="εκφώνηση Θέματος 3"),
            ],
            steps=[
                CalculationStep(
                    label="Βήμα 1 — Μάσκα (ερώτημα α)",
                    description="Το /22 σημαίνει 22 άσσους: 11111111.11111111.11111100.00000000. Τα πρώτα δύο οκτάδια γεμάτα (8+8 = 16 bits) και 6 ακόμη bits στο τρίτο (252 = 11111100).",
                    latex=r"/22 \Rightarrow 11111111.11111111.11111100.00000000 = 255.255.252.0",
                    result="Μάσκα: 255.255.252.0",
                ),
                CalculationStep(
                    label="Βήμα 2 — Bitwise AND για Δίκτυο (ερώτημα β)",
                    description="Εφαρμόζουμε AND byte-προς-byte στο τρίτο οκτάδιο: 45 = 00101101 και 252 = 11111100 δίνουν 00101100 = 44. Τα δύο πρώτα οκτάδια (172, 16) περνούν ανέπαφα, το τέταρτο μηδενίζεται.",
                    latex=r"00101101_2 \;\text{AND}\; 11111100_2 = 00101100_2 = 44_{10} \Rightarrow 172.16.44.0",
                    result="Network Address: 172.16.44.0",
                ),
                CalculationStep(
                    label="Βήμα 3 — Broadcast (ερώτημα γ)",
                    description="Θέτουμε όλα τα 10 host bits σε 1: τα 2 χαμηλά bits του τρίτου οκταδίου γίνονται 11 (44 + 3 = 47) και το τέταρτο γίνεται 255.",
                    latex=r"00101100 \rightarrow 00101111 = 47,\;\; 00000000 \rightarrow 11111111 = 255",
                    result="Broadcast Address: 172.16.47.255",
                ),
                CalculationStep(
                    label="Βήμα 4 — Έγκυρο Εύρος (ερώτημα δ)",
                    description="Πρώτη έγκυρη = δίκτυο + 1, τελευταία = broadcast − 1.",
                    result="Usable: 172.16.44.1 – 172.16.47.254",
                ),
                CalculationStep(
                    label="Βήμα 5 — Πλήθος Hosts (ερώτημα ε)",
                    description="Host bits h = 32 − 22 = 10, οπότε οι χρησιμοποιήσιμοι σταθμοί είναι 2^10 − 2 (αφαιρώντας δίκτυο και broadcast).",
                    latex=r"2^{10} - 2 = 1024 - 2 = 1022",
                    result="Μέγιστοι hosts: 1022",
                ),
            ],
            answer_tables=[
                AnalysisTable(
                    title="Σύνοψη Παραμέτρων του Υποδικτύου 172.16.45.130/22",
                    headers=["Παράμετρος", "Τιμή"],
                    rows=[
                        AnalysisRow(cells=["Μάσκα (δεκαδική)", "255.255.252.0"]),
                        AnalysisRow(cells=["Network Address", "172.16.44.0"]),
                        AnalysisRow(cells=["Broadcast Address", "172.16.47.255"], highlight=True),
                        AnalysisRow(cells=["First / Last Usable", "172.16.44.1 / 172.16.47.254"]),
                        AnalysisRow(cells=["Χρησιμοποιήσιμοι Hosts", "1022 (2^10 − 2)"]),
                    ],
                ),
            ],
            answer="Μάσκα 255.255.252.0 · Δίκτυο 172.16.44.0 · Broadcast 172.16.47.255 · Usable .44.1 – .47.254 · 1022 hosts.",
            tips=[
                "Το block του /22 είναι 256 − 252 = 4 × /24, οπότε το δίκτυο ξεκινά σε πολλαπλάσιο του 4 στο τρίτο οκτάδιο: 44 = 4 × 11.",
                "Έλεγχος: 44 (δίκτυο) + 4 (block) − 1 = 47 → broadcast στο .47.255 — σωστό.",
            ],
        ),
        ExamQuestion(
            thema="Θέμα 4",
            thema_title="Σύνοψη Διαδρομών (CIDR) & Πίνακες Δρομολόγησης",
            sub_number="4.1",
            title="Σύνοψη των 192.168.16-19.0/24 σε μία Διαδρομή",
            question_type="computational",
            prompt="Διαθέτετε τα δίκτυα 192.168.16.0/24, 192.168.17.0/24, 192.168.18.0/24 και 192.168.19.0/24. Βρείτε τη μία διαδρομή CIDR που συνοψίζει και τα τέσσερα δίκτυα.",
            given=[
                GivenParameter(label="Δίκτυα προς σύνοψη", value="192.168.16.0/24 έως 192.168.19.0/24", source="εκφώνηση Θέματος 4.1"),
            ],
            steps=[
                CalculationStep(
                    label="Βήμα 1 — Δυαδική Αναπαράσταση 3ου Οκταδίου",
                    description="Μετατρέπουμε τα 16, 17, 18, 19 σε δυαδικό: όλα μοιράζονται το πρόθεμα 0001 και διαφέρουν μόνο στα 4 χαμηλά bits.",
                    latex=r"16 = 00010000,\; 17 = 00010001,\; 18 = 00010010,\; 19 = 00010011",
                ),
                CalculationStep(
                    label="Βήμα 2 — Κοινά Αρχικά Bits & Μέγεθος Block",
                    description="Συγκρίνοντας bit-προς-bit: τα 16, 17, 18, 19 μοιράζονται τα πρώτα 5 bits (00010) — το έκτο bit διαφέρει (0 για 16-17, 1 για 18-19). Το /21 (00010xxx) όμως θα κάλυπτε τα 16-23, δηλαδή 8 δίκτυα — πλατύτερο από το απαραίτητο. Για σύνοψη ακριβώς 4 διαδοχικών /24 χρειάζονται 2^2 = 4 δίκτυα ανά block, δηλαδή πρόθεμα 24 − 2 = /22, εφόσον η αρχή (16) είναι πολλαπλάσιο του 4.",
                    latex=r"4\,\text{διαδοχικά } /24 = 2^2 \Rightarrow 24 - 2 = 22 \Rightarrow /22,\; 16 = 4 \times 4 \;\text{(ευθυγραμμισμένο block)}",
                ),
                CalculationStep(
                    label="Βήμα 3 — Σύνοψη & Μάσκα",
                    description="Η συνοπτική διαδρομή παίρνει τη διεύθυνση του πρώτου δικτύου με το νέο πρόθεμα: 192.168.16.0/22, μάσκα 255.255.252.0. Σε δυαδικό: 192.168.000100xx.xxxxxxxx.",
                    result="Σύνοψη: 192.168.16.0/22 · Μάσκα: 255.255.252.0",
                ),
                CalculationStep(
                    label="Βήμα 4 — Επαλήθευση Εύρους",
                    description="Το block του /22 στο τρίτο οκτάδιο είναι 256 − 252 = 4, άρα το 192.168.16.0/22 καλύπτει ακριβώς το 192.168.16.0 έως 192.168.19.255 — ούτε περισσότερα, ούτε λιγότερα δίκτυα.",
                    latex=r"000100\,xx \Rightarrow \text{κάλυψη } 192.168.16.0 - 192.168.19.255 \;(\text{ακριβώς } 4 \times /24)",
                ),
            ],
            answer="192.168.16.0/22 — μάσκα 255.255.252.0: καλύπτει ακριβώς τα 192.168.16.0 έως 192.168.19.255 (4 × /24, κοινά bits 192.168.0001xx).",
            tips=[
                "Μην σταματάτε στο πρώτο κοινό πρόθεμα: ψάξτε το μακρύτερο κοινό πρόθεμα που εξακολουθεί να τα καλύπτει ΟΛΑ — εδώ /22 και όχι /20.",
                "Η σύνοψη είναι έγκυρη μόνο όταν τα δίκτυα είναι διαδοχικά και σε δύναμη του δύο — 4 δίκτυα = 2 επιπλέον bits.",
            ],
        ),
        ExamQuestion(
            thema="Θέμα 4",
            thema_title="Σύνοψη Διαδρομών (CIDR) & Πίνακες Δρομολόγησης",
            sub_number="4.2",
            title="Αναζήτηση Επόμενου Άλματος (Longest Prefix Match)",
            question_type="computational",
            prompt="Δοθέντος του πίνακα δρομολόγησης (192.168.50.0/24 → 0.0.0.0/eth0· 10.0.0.0/8 → 192.168.50.1/eth0· 172.16.0.0/16 → 192.168.50.2/eth0· 0.0.0.0/0 → 192.168.50.254/eth0), προσδιορίστε το επόμενο άλμα για πακέτα με προορισμό: a) 192.168.50.25, b) 10.0.0.5, c) 172.16.100.50, d) 8.8.8.8.",
            given=[
                GivenParameter(label="Γραμμή 1", value="192.168.50.0/24 → GW 0.0.0.0 (direct), eth0", source="πίνακας εκφώνησης"),
                GivenParameter(label="Γραμμή 2", value="10.0.0.0/8 → GW 192.168.50.1, eth0", source="πίνακας εκφώνησης"),
                GivenParameter(label="Γραμμή 3", value="172.16.0.0/16 → GW 192.168.50.2, eth0", source="πίνακας εκφώνησης"),
                GivenParameter(label="Γραμμή 4", value="0.0.0.0/0 → GW 192.168.50.254, eth0 (default)", source="πίνακας εκφώνησης"),
            ],
            steps=[
                CalculationStep(
                    label="Βήμα 1 — Προορισμός a) 192.168.50.25",
                    description="Ταιριάζει στη γραμμή 192.168.50.0/24 (η 50.25 ∈ 50.0-50.255) και ταυτόχρονα στην default 0.0.0.0/0. Κερδίζει η πιο εξειδικευμένη (/24 έναντι /0). Gateway 0.0.0.0 σημαίνει άμεσα συνδεδεμένο δίκτυο.",
                    result="a) Άμεση παράδοση στο τοπικό δίκτυο (gateway 0.0.0.0, eth0) — χωρίς επόμενο άλμα δρομολογητή",
                ),
                CalculationStep(
                    label="Βήμα 2 — Προορισμός b) 10.0.0.5",
                    description="Ταιριάζει μόνο στη γραμμή 10.0.0.0/8 (10.x.x.x). Επόμενο άλμα ο gateway της γραμμής.",
                    result="b) Επόμενο άλμα: 192.168.50.1 (eth0)",
                ),
                CalculationStep(
                    label="Βήμα 3 — Προορισμός c) 172.16.100.50",
                    description="Ταιριάζει στη γραμμή 172.16.0.0/16 (172.16.x.x)· το 100.50 είναι εντός. Επόμενο άλμα ο gateway της.",
                    result="c) Επόμενο άλμα: 192.168.50.2 (eth0)",
                ),
                CalculationStep(
                    label="Βήμα 4 — Προορισμός d) 8.8.8.8",
                    description="Δεν ταιριάζει καμία συγκεκριμένη γραμμή (ούτε 192.168.50/24, ούτε 10/8, ούτε 172.16/16)· εφαρμόζεται η προεπιλεγμένη διαδρομή 0.0.0.0/0.",
                    result="d) Επόμενο άλμα: 192.168.50.254 (default gateway, eth0)",
                ),
            ],
            answer_tables=[
                AnalysisTable(
                    title="Αποτελέσματα Αναζήτησης (Longest Prefix Match)",
                    headers=["Προορισμός", "Ταίριασμα", "Επόμενο Άλμα", "Ενέργεια"],
                    rows=[
                        AnalysisRow(cells=["192.168.50.25", "192.168.50.0/24", "0.0.0.0 (direct)", "Άμεση παράδοση μέσω ARP στο τοπικό δίκτυο"], highlight=True),
                        AnalysisRow(cells=["10.0.0.5", "10.0.0.0/8", "192.168.50.1", "Προώθηση στον γειτονικό δρομολογητή"]),
                        AnalysisRow(cells=["172.16.100.50", "172.16.0.0/16", "192.168.50.2", "Προώθηση στον γειτονικό δρομολογητή"]),
                        AnalysisRow(cells=["8.8.8.8", "0.0.0.0/0 (default)", "192.168.50.254", "Προώθηση μέσω προεπιλεγμένης πύλης"], highlight=True),
                    ],
                ),
            ],
            answer="a) άμεση παράδοση (0.0.0.0) · b) 192.168.50.1 · c) 192.168.50.2 · d) 192.168.50.254 (default) — πάντα με longest prefix match.",
            tips=[
                "Κανόνας: αν πολλές γραμμές ταιριάζουν, κερδίζει αυτή με το μακρύτερο πρόθεμα — όχι η πρώτη στη σειρά ούτε αυτή με τη μικρότερη μετρική.",
                "Gateway 0.0.0.0 = το δίκτυο είναι απευθείας συνδεδεμένο στη διεπαφή: ο σταθμός επιλύεται με ARP και παραδίδεται χωρίς δρομολογητή.",
            ],
        ),
    ]

    analysis_tables = [
        AnalysisTable(
            title="Αναφορά: Ιδιωτικά & Ειδικά Εύρη Διευθύνσεων",
            headers=["Εύρος / Διεύθυνση", "Κατηγορία", "Σημειώσεις"],
            rows=[
                AnalysisRow(cells=["10.0.0.0/8", "Ιδιωτικό (RFC 1918)", "Κλάση A, 16.777.214 hosts"]),
                AnalysisRow(cells=["172.16.0.0/12", "Ιδιωτικό (RFC 1918)", "Κλάση B, φτάνει έως 172.31.255.255"]),
                AnalysisRow(cells=["192.168.0.0/16", "Ιδιωτικό (RFC 1918)", "Κλάση C"]),
                AnalysisRow(cells=["127.0.0.0/8", "Loopback", "Το 127.0.0.1 = localhost"]),
                AnalysisRow(cells=["169.254.0.0/16", "APIPA / link-local", "Αυτόματη εκχώρηση όταν αποτύχει το DHCP"], highlight=True),
                AnalysisRow(cells=["0.0.0.0 / 255.255.255.255", "Ειδικές", "«Οποιαδήποτε» / τοπική broadcast"]),
            ],
        ),
    ]

    diagram_title = "Χάρτης Κατανομής VLSM: 172.16.0.0/16"
    diagram_nodes = [
        DiagramNode(id="parent", label="172.16.0.0/16 — Οργανισμός", x=450, y=20, w=300, details=["Μάσκα: 255.255.0.0", "Εύρος: 172.16.0.0 – 172.16.255.255"], highlight=True),
        DiagramNode(id="a", label="Δίκτυο A — /19 (5000)", x=30, y=200, w=250, details=["Μάσκα: 255.255.224.0", "Δίκτυο: 172.16.0.0", "Usable: .0.1 – .31.254", "Broadcast: 172.16.31.255", "Χωρητικότητα: 8190"]),
        DiagramNode(id="b", label="Δίκτυο B — /21 (2000)", x=310, y=200, w=250, details=["Μάσκα: 255.255.248.0", "Δίκτυο: 172.16.32.0", "Usable: .32.1 – .39.254", "Broadcast: 172.16.39.255", "Χωρητικότητα: 2046"]),
        DiagramNode(id="c", label="Δίκτυο C — /23 (500)", x=590, y=200, w=250, details=["Μάσκα: 255.255.254.0", "Δίκτυο: 172.16.40.0", "Usable: .40.1 – .41.254", "Broadcast: 172.16.41.255", "Χωρητικότητα: 510"]),
        DiagramNode(id="d", label="Δίκτυο D — /25 (100)", x=870, y=200, w=250, details=["Μάσκα: 255.255.255.128", "Δίκτυο: 172.16.42.0", "Usable: .42.1 – .42.126", "Broadcast: 172.16.42.127", "Χωρητικότητα: 126"]),
        DiagramNode(id="e", label="Δίκτυο E — /30 (p2p)", x=30, y=430, w=250, details=["Μάσκα: 255.255.255.252", "Δίκτυο: 172.16.42.128", "Usable: .42.129 – .42.130", "Broadcast: 172.16.42.131", "Χωρητικότητα: 2"]),
        DiagramNode(id="free", label="Ελεύθερος Χώρος (Επέκταση)", x=310, y=430, w=500, details=["Εύρος: 172.16.42.132 – 172.16.255.255", "Διαθέσιμες διευθύνσεις: 54.652"]),
    ]
    diagram_edges = [
        DiagramEdge(path="M 600,80 C 600,140 155,140 155,200", label="/19 (8192)", lx=300, ly=133),
        DiagramEdge(path="M 600,80 C 600,140 435,140 435,200", label="/21 (2048)", lx=500, ly=150),
        DiagramEdge(path="M 600,80 C 600,140 715,140 715,200", label="/23 (512)", lx=690, ly=150),
        DiagramEdge(path="M 600,80 C 600,140 995,140 995,200", label="/25 (128)", lx=915, ly=133),
        DiagramEdge(path="M 600,80 C 600,330 155,330 155,430", label="/30 (4)", lx=330, ly=350, dashed=True),
        DiagramEdge(path="M 600,80 C 600,330 560,330 560,430", label="υπόλοιπο", lx=545, ly=350, dashed=True),
    ]
    diagram_note = "Κατανομή με φθίνουσα σειρά ανάγκης από το 172.16.0.0: κάθε block ξεκινά στο broadcast + 1 του προηγούμενου και το υπόλοιπο παραμένει ενιαίο προς το τέλος του /16."

    justifications = [
        DesignJustification(
            title="1. Σειρά Μεγαλού-Προς-Μικρό (VLSM)",
            color_class="text-blue-500",
            description="Με κατά φθίνουσα ταξινόμηση (5000 → 2000 → 500 → 100 → 2) κάθε block προστίθεται στο επόμενο ελεύθερο όριο, χωρίς επικαλύψεις και χωρίς κατακερματισμένο ελεύθερο χώρο.",
        ),
        DesignJustification(
            title="2. Ελάχιστη Ικανοποιούμενη Μάσκα",
            color_class="text-amber-500",
            description="Επιλέχθηκαν /19, /21, /23, /25, /30 — χωρητικότητες 8190, 2046, 510, 126, 2: η μικρότερη δυνατή για κάθε ανάγκη, ελαχιστοποιώντας τη σπατάλη (π.χ. το /20 με 4094 δεν θα χώραγε τους 5000).",
        ),
        DesignJustification(
            title="3. Διατήρηση Ενιαίου Ελεύθερου Υπολοίπου",
            color_class="text-emerald-500",
            description="Η συσσώρευση των blocks στη βάση του /16 αφήνει το 172.16.42.132 – 172.16.255.255 ενιαίο: μελλοντικά δίκτυα κάθε μεγέθους μπορούν να προστεθούν χωρίς ανακατανομή.",
        ),
        DesignJustification(
            title="4. Σύνοψη με Μακρύτερο Κοινό Πρόθεμα",
            color_class="text-purple-500",
            description="Στο Θέμα 4 επιλέχθηκε το /22 αντί του πρώτου κοινού προθέματος /20, γιατί καλύπτει ακριβώς τα 4 διαδοχικά /24 χωρίς να απορροφά άσχετα δίκτυα (20-31).",
        ),
    ]

    solution_code = """# Θέμα 2 & 3 & 4: Επαλήθευση VLSM, παραμέτρων υποδικτύου και σύνοψης
import ipaddress

# --- Θέμα 2: VLSM του 172.16.0.0/16 ---
needs = [("A", 5000), ("B", 2000), ("C", 500), ("D", 100), ("E", 2)]
cursor = int(ipaddress.ip_network("172.16.0.0/16").network_address)

for name, hosts in sorted(needs, key=lambda item: -item[1]):
    h = 1
    while 2 ** h - 2 < hosts:
        h += 1
    net = ipaddress.ip_network((cursor, 32 - h))
    print(f"Δίκτυο {name}: {net.with_prefixlen} | Μάσκα {net.netmask} | "
          f"Usable {net.network_address + 1} – {net.broadcast_address - 1} | "
          f"BC {net.broadcast_address}")
    cursor = int(net.broadcast_address) + 1

# --- Θέμα 3: Παράμετροι της 172.16.45.130/22 ---
host_net = ipaddress.ip_network("172.16.45.130/22", strict=False)
print(f"Μάσκα: {host_net.netmask} | Δίκτυο: {host_net.network_address} | "
      f"BC: {host_net.broadcast_address} | Hosts: {host_net.num_addresses - 2}")

# --- Θέμα 4: Σύνοψη των 16-19.0/24 ---
routes = [ipaddress.ip_network(f"192.168.{octet}.0/24") for octet in (16, 17, 18, 19)]
collapsed = list(ipaddress.collapse_addresses(routes))
print(f"Σύνοψη: {collapsed[0].with_prefixlen} | Μάσκα: {collapsed[0].netmask}")
"""

    return Scenario(
        id="synth_exam_1",
        title="Συνθετικό Θέμα 1",
        subtitle="Κλάσεις & Ιδιωτικά Εύρη · VLSM 172.16.0.0/16 · Παράμετροι /22 · Σύνοψη & Longest Prefix Match",
        course_tag="NETWORKING (Συνθετική Εξέταση 1)",
        exam_meta=ExamMeta(duration="Διάρκεια: 2.5 ώρες", scoring="4 Θέματα × 2.5 μονάδες = 10"),
        paragraphs=paragraphs,
        questions=questions,
        layers=[],
        analysis_tables=analysis_tables,
        diagram_title=diagram_title,
        diagram_nodes=diagram_nodes,
        diagram_edges=diagram_edges,
        diagram_note=diagram_note,
        justifications=justifications,
        solution_code=solution_code,
        code_language="python",
    )
