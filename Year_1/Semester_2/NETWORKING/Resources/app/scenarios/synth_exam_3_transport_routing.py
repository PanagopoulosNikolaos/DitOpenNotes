"""Synthetic Exam 3 (Transport Layer & Routing Algorithms) scenario module.

A complete synthetic exam paper in the exact structure of the course's
practice exam (4 Themata x 2.5 points, 2.5 hours), covering well-known ports,
the TCP three-way handshake, window/flow-control fields, congestion control
with Tahoe/Reno, throughput and bandwidth-delay product, a full Dijkstra
execution on a five-router topology, and TCP sequence/acknowledgment
tracing. Every question carries a worked step-by-step solution.
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


def createSynthExam3Scenario() -> Scenario:
    """Constructs and returns the Synthetic Exam 3 (Transport & Routing) scenario.

    Returns:
        Scenario: Fully populated scenario instance.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(
                    text="<strong>Συνθετικό Θέμα Εξετάσεων 3: Δίκτυα Υπολογιστών — Επίπεδο Μεταφοράς & Αλγόριθμοι Δρομολόγησης</strong>",
                    is_highlight=True,
                    category="term",
                    tag_label="ΣΥΝΘΕΤΙΚΗ ΕΞΕΤΑΣΗ",
                    badge_class="badge-term",
                    tooltip="Ταξινόμηση: Συνθετικό θέμα εξετάσεων για μεταφορά και δρομολόγηση. Εντοπισμός: Τίτλος του συνθετικού θέματος. Εφαρμογή: Καλύπτει θύρες, χειραψία, συμφόρηση, Dijkstra και seq/ACK.",
                ),
            ],
            accent_border_color="accent",
        ),
        Paragraph(
            segments=[
                TextSegment(text="<strong>Οδηγίες:</strong> Διάρκεια εξέτασης: "),
                TextSegment(text="2.5 ώρες", is_highlight=True, category="given", tag_label="ΔΕΔΟΜΕΝΟ", badge_class="badge-given", tooltip="Ταξινόμηση: Χρονικό όριο. Εντοπισμός: Επίσημη οδηγία. Εφαρμογή: Περίπου 35 λεπτά ανά Θέμα."),
                TextSegment(text=". "),
                TextSegment(text="Όλα τα θέματα βαθμολογούνται με 2.5 μονάδες", is_highlight=True, category="given", tag_label="ΒΑΘΜΟΛΟΓΙΑ", badge_class="badge-given", tooltip="Ταξινόμηση: Κανόνας βαθμολόγησης (σύνολο 10). Εντοπισμός: Επίσημη οδηγία. Εφαρμογή: Ίση βαρύτητα Θεμάτων."),
                TextSegment(text="."),
            ],
        ),
        Paragraph(
            segments=[
                TextSegment(
                    text="Θέμα 1: Επίπεδο Μεταφοράς — Θύρες & Μηχανισμοί TCP/UDP (Πολλαπλής Επιλογής)",
                    is_highlight=True,
                    category="proto",
                    tag_label="MCQ",
                    badge_class="badge-proto",
                    tooltip="Ταξινόμηση: Θέμα πολλαπλής επιλογής για θύρες και πεδία TCP. Εντοπισμός: Επικεφαλίδα «Θέμα 1». Εφαρμογή: Λύνεται με τον πίνακα well-known ports και τη σημασιολογία της χειραψίας.",
                ),
            ],
            is_heading=True,
        ),
        Paragraph(
            segments=[
                TextSegment(text="α. Ο αριθμός θύρας "),
                TextSegment(
                    text="110",
                    is_highlight=True,
                    category="given",
                    tag_label="ΔΕΔΟΜΕΝΟ",
                    badge_class="badge-given",
                    tooltip="Ταξινόμηση: Well-known port. Εντοπισμός: Ερώτημα α. Εφαρμογή: 110 = POP3 (ανάκτηση email)· IMAP = 143, SMTP = 25, SSH = 22.",
                ),
                TextSegment(text=" αντιστοιχεί στην υπηρεσία:"),
            ],
        ),
        Paragraph(
            segments=[
                TextSegment(text="β. Στο δεύτερο βήμα της "),
                TextSegment(
                    text="χειραψίας τριών βημάτων (three-way handshake)",
                    is_highlight=True,
                    category="method",
                    tag_label="ΜΕΘΟΔΟΣ",
                    badge_class="badge-method",
                    tooltip="Ταξινόμηση: Διαδικασία εγκαθίδρυσης σύνδεσης TCP. Εντοπισμός: Ερώτημα β. Εφαρμογή: Βήμα 2 = SYN+ACK από τον διακομιστή με ACK = ISN πελάτη + 1.",
                ),
                TextSegment(text=" του TCP, ο διακομιστής αποστέλλει:"),
            ],
        ),
        Paragraph(
            segments=[
                TextSegment(text="γ. Για τη μετάδοση φωνής πάνω σε IP ("),
                TextSegment(
                    text="VoIP",
                    is_highlight=True,
                    category="term",
                    tag_label="ΕΦΑΡΜΟΓΗ",
                    badge_class="badge-term",
                    tooltip="Ταξινόμηση: Εφαρμογή πραγματικού χρόνου. Εντοπισμός: Ερώτημα γ. Εφαρμογή: Απαιτεί χαμηλή καθυστέρηση/jitter — προτιμάται UDP.",
                ),
                TextSegment(text=") προτιμάται το πρωτόκολλο:"),
            ],
        ),
        Paragraph(
            segments=[
                TextSegment(text="δ. Το πεδίο "),
                TextSegment(
                    text="Window",
                    is_highlight=True,
                    category="term",
                    tag_label="ΠΕΔΙΟ TCP",
                    badge_class="badge-term",
                    tooltip="Ταξινόμηση: Πεδίο 16-bit της επικεφαλίδας TCP. Εντοπισμός: Ερώτημα δ. Εφαρμογή: Μεταφέρει το rwnd του παραλήπτη για έλεγχο ροής.",
                ),
                TextSegment(text=" της επικεφαλίδας TCP χρησιμοποιείται για:"),
            ],
        ),
        Paragraph(
            segments=[
                TextSegment(
                    text="Θέμα 2: Έλεγχος Συμφόρησης TCP & Ρυθμοαπόδοση",
                    is_highlight=True,
                    category="method",
                    tag_label="ΥΠΟΛΟΓΙΣΤΙΚΟ",
                    badge_class="badge-method",
                    tooltip="Ταξινόμηση: Υπολογιστικό θέμα AIMD/throughput. Εντοπισμός: Επικεφαλίδα «Θέμα 2». Εφαρμογή: Εξέλιξη cwnd, αντίδραση Tahoe/Reno, τύπος T = W/RTT.",
                ),
            ],
            is_heading=True,
        ),
        Paragraph(
            segments=[
                TextSegment(text="1. Μια σύνδεση TCP λειτουργεί με "),
                TextSegment(
                    text="MSS = 1 KB",
                    is_highlight=True,
                    category="given",
                    tag_label="ΔΕΔΟΜΕΝΟ",
                    badge_class="badge-given",
                    tooltip="Ταξινόμηση: Μέγιστο μέγεθος τμήματος. Εντοπισμός: Ρητό δεδομένο του ερωτήματος 1. Εφαρμογή: Μονάδα μέτρησης του cwnd — 1 MSS = 1 KB.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="αρχικό ssthresh = 16 KB",
                    is_highlight=True,
                    category="given",
                    tag_label="ΔΕΔΟΜΕΝΟ",
                    badge_class="badge-given",
                    tooltip="Ταξινόμηση: Κατώφλι αργής εκκίνησης. Εντοπισμός: Ρητό δεδομένο. Εφαρμογή: Κάτω από 16 KB το cwnd διπλασιάζεται ανά RTT· πάνω αυξάνεται γραμμικά.",
                ),
                TextSegment(text=" και "),
                TextSegment(
                    text="cwnd = 1 MSS στην εκκίνηση",
                    is_highlight=True,
                    category="given",
                    tag_label="ΔΕΔΟΜΕΝΟ",
                    badge_class="badge-given",
                    tooltip="Ταξινόμηση: Αρχική τιμή παραθύρου συμφόρησης. Εντοπισμός: Ρητό δεδομένο. Εφαρμογή: Εκκίνηση Slow Start από 1.",
                ),
                TextSegment(text=". Όλα τα ACK παραλαμβάνονται επιτυχώς μέχρι τον "),
                TextSegment(
                    text="7ο γύρο RTT",
                    is_highlight=True,
                    category="given",
                    tag_label="ΓΥΡΟΣ ΑΠΩΛΕΙΑΣ",
                    badge_class="badge-given",
                    tooltip="Ταξινόμηση: Χρονική στιγμή απώλειας. Εντοπισμός: Ρητό δεδομένο. Εφαρμογή: Στον 7ο γύρο λαμβάνονται 3 διπλότυπα ACK και ενεργοποιείται Fast Retransmit.",
                ),
                TextSegment(text=", όπου λαμβάνονται "),
                TextSegment(
                    text="3 διπλότυπα ACK (3 duplicate ACKs)",
                    is_highlight=True,
                    category="term",
                    tag_label="ΣΗΜΑ ΑΠΩΛΕΙΑΣ",
                    badge_class="badge-term",
                    tooltip="Ταξινόμηση: Ένδειξη απώλειας τμήματος. Εντοπισμός: Ρητό δεδομένο. Εφαρμογή: Πυροδοτεί Fast Retransmit/Recovery· ssthresh = floor(cwnd/2).",
                ),
                TextSegment(text=". Να υπολογιστεί η εξέλιξη του cwnd ανά γύρο (1 έως 7), η τιμή του cwnd στον 6ο γύρο, και η αντίδραση TCP Tahoe και TCP Reno (Fast Recovery) μετά την απώλεια."),
            ],
        ),
        Paragraph(
            segments=[
                TextSegment(text="2. Σύνδεση TCP με "),
                TextSegment(
                    text="μέγεθος παραθύρου 64 KB",
                    is_highlight=True,
                    category="given",
                    tag_label="ΔΕΔΟΜΕΝΟ",
                    badge_class="badge-given",
                    tooltip="Ταξινόμηση: Σταθερό παράθυρο. Εντοπισμός: Ρητό δεδομένο του ερωτήματος 2. Εφαρμογή: 64 KB = 524.288 bits → ρυθμοαπόδοση W/RTT.",
                ),
                TextSegment(text=" και "),
                TextSegment(
                    text="RTT = 100 ms",
                    is_highlight=True,
                    category="given",
                    tag_label="ΔΕΔΟΜΕΝΟ",
                    badge_class="badge-given",
                    tooltip="Ταξινόμηση: Χρόνος επιστροφής. Εντοπισμός: Ρητό δεδομένο. Εφαρμογή: 0,1 s — διαιρέτης του τύπου ρυθμοαπόδοσης.",
                ),
                TextSegment(text=", χωρίς απώλειες. Να υπολογιστεί η μέγιστη ρυθμοαπόδοση (throughput) και το απαιτούμενο μέγεθος παραθύρου για ρυθμοαπόδοση 100 Mbps με το ίδιο RTT (γινόμενο εύρους-καθυστέρησης)."),
            ],
        ),
        Paragraph(
            segments=[
                TextSegment(
                    text="Θέμα 3: Αλγόριθμος Δρομολόγησης Link-State (Dijkstra)",
                    is_highlight=True,
                    category="method",
                    tag_label="ΥΠΟΛΟΓΙΣΤΙΚΟ",
                    badge_class="badge-method",
                    tooltip="Ταξινόμηση: Εκτέλεση Dijkstra σε σταθμισμένο γράφο. Εντοπισμός: Επικεφαλίδα «Θέμα 3». Εφαρμογή: Πίνακας βημάτων N'/D() και τελικός πίνακας δρομολόγησης του u.",
                ),
            ],
            is_heading=True,
        ),
        Paragraph(
            segments=[
                TextSegment(text="Δίνεται τοπολογία "),
                TextSegment(
                    text="5 δρομολογητών (u, v, w, x, y)",
                    is_highlight=True,
                    category="given",
                    tag_label="ΔΕΔΟΜΕΝΟ",
                    badge_class="badge-given",
                    tooltip="Ταξινόμηση: Κόμβοι του γραφήματος. Εντοπισμός: Ρητό δεδομένο του Θέματος 3. Εφαρμογή: Πηγή το u· προορισμοί τα v, w, x, y.",
                ),
                TextSegment(text=" με κόστη ζεύξεων "),
                TextSegment(
                    text="c(u,v)=2, c(u,w)=5, c(u,x)=1, c(x,v)=2, c(x,w)=3, c(x,y)=1, c(v,w)=3, c(y,w)=1",
                    is_highlight=True,
                    category="given",
                    tag_label="ΚΟΣΤΗ",
                    badge_class="badge-given",
                    tooltip="Ταξινόμηση: Σταθμοί ακμών του γραφήματος. Εντοπισμός: Ρητή λίστα του Θέματος 3. Εφαρμογή: Είσοδοι του Dijkstra· κάθε βήμα χαλαρώνει τις ακμές του νέου κόμβου.",
                ),
                TextSegment(text=". Εκτελέστε τον αλγόριθμο "),
                TextSegment(
                    text="Dijkstra",
                    is_highlight=True,
                    category="method",
                    tag_label="ΑΛΓΟΡΙΘΜΟΣ",
                    badge_class="badge-method",
                    tooltip="Ταξινόμηση: Αλγόριθμος βραχύτερων μονοπατιών (SPF). Εντοπισμός: Ρητό αίτημα. Εφαρμογή: D(v) = min(D(v), D(u) + c(u,v)) σε κάθε βήμα.",
                ),
                TextSegment(text=" με αρχικό κόμβο το u, βήμα-βήμα, και προσδιορίστε τον πίνακα δρομολόγησης του u (ελάχιστο κόστος & επόμενο άλμα)."),
            ],
        ),
        Paragraph(
            segments=[
                TextSegment(
                    text="Θέμα 4: Αριθμοί Ακολουθίας & Επιβεβαιώσεις TCP",
                    is_highlight=True,
                    category="method",
                    tag_label="ΥΠΟΛΟΓΙΣΤΙΚΟ",
                    badge_class="badge-method",
                    tooltip="Ταξινόμηση: Ιχνηλάτιση SEQ/ACK σε σύνδεση TCP. Εντοπισμός: Επικεφαλίδα «Θέμα 4». Εφαρμογή: Κανόνες: SEQ = πρώτο byte, ACK = επόμενο αναμενόμενο, SYN καταναλώνει 1 αριθμό.",
                ),
            ],
            is_heading=True,
        ),
        Paragraph(
            segments=[
                TextSegment(text="Μια σύνδεση TCP ξεκινά με "),
                TextSegment(
                    text="ISN πελάτη = 3000",
                    is_highlight=True,
                    category="given",
                    tag_label="ΔΕΔΟΜΕΝΟ",
                    badge_class="badge-given",
                    tooltip="Ταξινόμηση: Αρχικός αριθμός ακολουθίας πελάτη. Εντοπισμός: Ρητό δεδομένο του Θέματος 4. Εφαρμογή: Το SYN του πελάτη φέρει SEQ 3000· τα δεδομένα ξεκινούν από 3001.",
                ),
                TextSegment(text=" και "),
                TextSegment(
                    text="ISN διακομιστή = 5000",
                    is_highlight=True,
                    category="given",
                    tag_label="ΔΕΔΟΜΕΝΟ",
                    badge_class="badge-given",
                    tooltip="Ταξινόμηση: Αρχικός αριθμός ακολουθίας διακομιστή. Εντοπισμός: Ρητό δεδομένο. Εφαρμογή: Το SYN-ACK φέρει SEQ 5000, ACK 3001.",
                ),
                TextSegment(text=". Μετά τη χειραψία: ο πελάτης στέλνει "),
                TextSegment(
                    text="500 bytes",
                    is_highlight=True,
                    category="given",
                    tag_label="ΔΕΔΟΜΕΝΟ",
                    badge_class="badge-given",
                    tooltip="Ταξινόμηση: Όγκος πρώτης αποστολής. Εντοπισμός: Ρητό δεδομένο. Εφαρμογή: Bytes 3001-3500· απάντηση ACK 3501.",
                ),
                TextSegment(text=", ο διακομιστής "),
                TextSegment(
                    text="300 bytes",
                    is_highlight=True,
                    category="given",
                    tag_label="ΔΕΔΟΜΕΝΟ",
                    badge_class="badge-given",
                    tooltip="Ταξινόμηση: Όγκος απάντησης. Εντοπισμός: Ρητό δεδομένο. Εφαρμογή: Bytes 5001-5300· ACK 5301.",
                ),
                TextSegment(text=", και ο πελάτης άλλα "),
                TextSegment(
                    text="200 bytes",
                    is_highlight=True,
                    category="given",
                    tag_label="ΔΕΔΟΜΕΝΟ",
                    badge_class="badge-given",
                    tooltip="Ταξινόμηση: Όγκος δεύτερης αποστολής. Εντοπισμός: Ρητό δεδομένο. Εφαρμογή: Bytes 3501-3700· τελικό ACK 3701.",
                ),
                TextSegment(text=". Εμφανίστε για κάθε segment: κατεύθυνση, σημαίες, SEQ, ACK και τα bytes δεδομένων."),
            ],
        ),
    ]

    questions = [
        ExamQuestion(
            thema="Θέμα 1",
            thema_title="Επίπεδο Μεταφοράς — Θύρες & Μηχανισμοί TCP/UDP (Πολλαπλής Επιλογής)",
            sub_number="1α",
            title="Θύρα 110",
            question_type="mcq",
            prompt="Ο αριθμός θύρας 110 αντιστοιχεί στην υπηρεσία:",
            options=[
                QuestionOption(letter="A", text="POP3", is_correct=True, explanation="Το POP3 (ανάκτηση email από τον διακομιστή) χρησιμοποιεί τη θύρα 110 — ο πελάτης κατεβάζει τα μηνύματα και συνήθως τα διαγράφει από τον server."),
                QuestionOption(letter="B", text="IMAP", is_correct=False, explanation="Το IMAP χρησιμοποιεί τη θύρα 143 και κρατά τα μηνύματα στον διακομιστή με συγχρονισμό φακέλων."),
                QuestionOption(letter="C", text="SMTP", is_correct=False, explanation="Το SMTP (αποστολή email) χρησιμοποιεί τη θύρα 25 — είναι η θύρα «προς τα έξω», όχι ανάκτησης."),
                QuestionOption(letter="D", text="SSH", is_correct=False, explanation="Το SSH χρησιμοποιεί τη θύρα 22 για κρυπτογραφημένη απομακρυσμένη πρόσβαση κονσόλας."),
            ],
            answer="Σωστή απάντηση: <strong>A</strong> — POP3 (θύρα 110).",
            tips=["Συνήθη ζεύγη-παγίδες: 25 SMTP (αποστολή) ↔ 110 POP3 / 143 IMAP (λήψη)· 80 HTTP ↔ 443 HTTPS· 20/21 FTP · 22 SSH · 23 Telnet · 53 DNS."],
        ),
        ExamQuestion(
            thema="Θέμα 1",
            thema_title="Επίπεδο Μεταφοράς — Θύρες & Μηχανισμοί TCP/UDP (Πολλαπλής Επιλογής)",
            sub_number="1β",
            title="Δεύτερο Βήμα Χειραψίας",
            question_type="mcq",
            prompt="Στο δεύτερο βήμα της χειραψίας τριών βημάτων (three-way handshake) του TCP, ο διακομιστής αποστέλλει:",
            options=[
                QuestionOption(letter="A", text="SYN", is_correct=False, explanation="Το σκέτο SYN είναι το ΠΡΩΤΟ βήμα και αποστέλλεται από τον πελάτη με τον δικό του ISN."),
                QuestionOption(letter="B", text="SYN-ACK", is_correct=True, explanation="Ο διακομιστής επιβεβαιώνει το SYN του πελάτη (ACK = ISN πελάτη + 1) και αποστέλλει συγχρόνως το δικό του SYN με τον ISN του — μία κίνηση με ενεργές και τις δύο σημαίες SYN=1, ACK=1."),
                QuestionOption(letter="C", text="ACK", is_correct=False, explanation="Το σκέτο ACK είναι το ΤΡΙΤΟ βήμα, από τον πελάτη, και ολοκληρώνει την εγκαθίδρυση."),
                QuestionOption(letter="D", text="FIN", is_correct=False, explanation="Το FIN χρησιμοποιείται στην ΤΕΡΜΑΤΙΣΗ της σύνδεσης (teardown), όχι στην εγκαθίδρυση."),
            ],
            answer="Σωστή απάντηση: <strong>B</strong> — SYN-ACK (γιατί επιβεβαιώνει το SYN του πελάτη και δηλώνει τον δικό του ISN).",
            tips=["Το SYN και το FIN καταναλώνουν από 1 αριθμό ακολουθίας το καθένα — κρίσιμο για τα θέματα seq/ACK."],
        ),
        ExamQuestion(
            thema="Θέμα 1",
            thema_title="Επίπεδο Μεταφοράς — Θύρες & Μηχανισμοί TCP/UDP (Πολλαπλής Επιλογής)",
            sub_number="1γ",
            title="Πρωτόκολλο για VoIP",
            question_type="mcq",
            prompt="Για τη μετάδοση φωνής πάνω σε IP (VoIP) προτιμάται το πρωτόκολλο:",
            options=[
                QuestionOption(letter="A", text="UDP", is_correct=True, explanation="Η φωνή είναι εφαρμογή πραγματικού χρόνου: ένα χαμένο πακέτο προτιμάται από την καθυστέρηση μιας επαναμετάδοσης. Το UDP δεν έχει χειραψία (άμεση εκκίνηση), έχει επικεφαλίδα 8 bytes (ελάχιστη επιβάρυνση/καθυστέρηση) και υποστηρίζει multicast για τηλεδιασκέψεις."),
                QuestionOption(letter="B", text="TCP", is_correct=False, explanation="Οι επαναμεταδόσεις και η χειραψία του TCP εισάγουν καθυστέρηση και jitter απαράδεκτα για ζωντανή φωνή."),
                QuestionOption(letter="C", text="HTTP", is_correct=False, explanation="Το HTTP είναι πρωτόκολλο εφαρμογής (μεταφορά υπερκειμένου) πάνω από TCP — όχι μεταφοράς."),
                QuestionOption(letter="D", text="ICMP", is_correct=False, explanation="Το ICMP είναι πρωτόκολλο ελέγχου/σφαλμάτων του επιπέδου δικτύου (ping, traceroute)."),
            ],
            answer="Σωστή απάντηση: <strong>A</strong> — UDP (πραγματικός χρόνος, ελάχιστη επιβάρυνση, ανοχή σε απώλειες).",
            tips=["Τυπικά UDP: VoIP, video streaming, DNS, DHCP, TFTP, gaming — αποστηθίστε τη λίστα."],
        ),
        ExamQuestion(
            thema="Θέμα 1",
            thema_title="Επίπεδο Μεταφοράς — Θύρες & Μηχανισμοί TCP/UDP (Πολλαπλής Επιλογής)",
            sub_number="1δ",
            title="Ρόλος του Πεδίου Window",
            question_type="mcq",
            prompt="Το πεδίο Window της επικεφαλίδας TCP χρησιμοποιείται για:",
            options=[
                QuestionOption(letter="A", text="Τον έλεγχο ροής (flow control) — την αναγγελία του rwnd", is_correct=True, explanation="Ο παραλήπτης ανακοινώνει με το πεδίο Window τον διαθέσιμο χώρο του buffer του (rwnd)· ο αποστολέας κραίνει τα unACKed bytes ≤ rwnd, ώστε να μην υπερχειλίσει τη μνήμη του παραλήπτη."),
                QuestionOption(letter="B", text="Τον έλεγχο λαθών", is_correct=False, explanation="Τον έλεγχο λαθών αναλαμβάνουν τα πεδία Sequence + ACK + Checksum (και τα διπλότυπα ACK για Fast Retransmit), όχι το Window."),
                QuestionOption(letter="C", text="Τη δρομολόγηση των πακέτων", is_correct=False, explanation="Η δρομολόγηση είναι αντικείμενο του επιπέδου δικτύου (IP + πίνακες δρομολόγησης)."),
                QuestionOption(letter="D", text="Τη συμπίεση των δεδομένων", is_correct=False, explanation="Η συμπίεση ανήκει στο επίπεδο εφαρμογής/παρουσίασης — καμία σχέση με το TCP."),
            ],
            answer="Σωστή απάντηση: <strong>A</strong> — έλεγχος ροής (rwnd advertisement).",
            tips=["Το ενεργό παράθυρο του αποστολέα είναι min(rwnd, cwnd): ροή + συμφόρηση από κοινού."],
        ),
        ExamQuestion(
            thema="Θέμα 2",
            thema_title="Έλεγχος Συμφόρησης TCP & Ρυθμοαπόδοση",
            sub_number="2α",
            title="Εξέλιξη cwnd: Tahoe vs Reno σε Απώλεια 3 dup ACK",
            question_type="computational",
            prompt="Μια σύνδεση TCP λειτουργεί με MSS = 1 KB, αρχικό ssthresh = 16 KB και cwnd = 1 MSS στην εκκίνηση. Όλα τα ACK παραλαμβάνονται επιτυχώς μέχρι τον 7ο γύρο RTT, όπου λαμβάνονται 3 διπλότυπα ACK. Να υπολογιστεί η εξέλιξη του cwnd ανά γύρο (1 έως 7), η τιμή του cwnd στον 6ο γύρο, και η αντίδραση TCP Tahoe και TCP Reno (Fast Recovery) μετά την απώλεια.",
            given=[
                GivenParameter(label="MSS", value="1 KB", source="εκφώνηση Θέματος 2.1"),
                GivenParameter(label="ssthresh (αρχικό)", value="16 KB", source="εκφώνηση Θέματος 2.1"),
                GivenParameter(label="cwnd εκκίνησης", value="1 MSS = 1 KB", source="εκφώνηση Θέματος 2.1"),
                GivenParameter(label="Απώλεια", value="7ος γύρος RTT — 3 duplicate ACKs", source="εκφώνηση Θέματος 2.1"),
            ],
            steps=[
                CalculationStep(
                    label="Βήμα 1 — Φάση Slow Start (γύροι 1-5)",
                    description="Όσο cwnd &lt; ssthresh το παράθυρο διπλασιάζεται κάθε RTT (εκθετική αύξηση): 1 → 2 → 4 → 8 → 16 KB. Στον 5ο γύρο το cwnd φτάνει το ssthresh = 16 KB.",
                    latex=r"1 \rightarrow 2 \rightarrow 4 \rightarrow 8 \rightarrow 16 \;\;(\text{Slow Start, } \times 2\,\text{ανά RTT})",
                ),
                CalculationStep(
                    label="Βήμα 2 — Φάση Congestion Avoidance (γύροι 6-7)",
                    description="Για cwnd ≥ ssthresh η αύξηση γίνεται γραμμική: +1 MSS ανά RTT (AIMD). Γύρος 6: 16 + 1 = 17 KB· γύρος 7: 17 + 1 = 18 KB — όπου συμβαίνει η απώλεια.",
                    latex=r"16 \rightarrow 17 \rightarrow 18 \;\;(\text{CA, } +1\,\text{MSS ανά RTT})",
                    result="cwnd στον 6ο γύρο: 17 KB (στον 7ο: 18 KB, εκεί η απώλεια)",
                ),
                CalculationStep(
                    label="Βήμα 3 — Αντίδραση TCP Tahoe",
                    description="Το Tahoe δεν διακρίνει τη σοβαρότητα των 3 dup ACK: μειώνει το ssthresh στο μισό του τρέχοντος cwnd και επιστρέφει σε πλήρη Slow Start από 1 MSS.",
                    latex=r"\text{Tahoe}\!: \; ssthresh = \lfloor 18/2 \rfloor = 9\,\text{KB}, \qquad cwnd = 1\,\text{KB}",
                    result="Tahoe: ssthresh = 9 KB, cwnd = 1 KB (επιστροφή σε Slow Start)",
                ),
                CalculationStep(
                    label="Βήμα 4 — Αντίδραση TCP Reno (Fast Retransmit & Fast Recovery)",
                    description="Το Reno εκμεταλλεύεται τα 3 dup ACK: επαναμεταδίδει αμέσως το χαμένο τμήμα (Fast Retransmit) και αντί να γυρίσει στο 1, θέτει cwnd = ssthresh + 3 (τα 3 dup ACK «μετρήθηκαν» ως σε πτήση) και συνεχίζει απευθείας σε Congestion Avoidance.",
                    latex=r"\text{Reno}\!: \; ssthresh = \lfloor 18/2 \rfloor = 9\,\text{KB}, \qquad cwnd = ssthresh + 3 = 12\,\text{KB}",
                    result="Reno: ssthresh = 9 KB, cwnd = 12 KB → απευθείας CA χωρίς Slow Start",
                ),
            ],
            answer_tables=[
                AnalysisTable(
                    title="Εξέλιξη cwnd ανά Γύρο RTT (μέχρι την απώλεια)",
                    headers=["Γύρος RTT", "Φάση", "cwnd (KB)", "cwnd (MSS)", "Σχόλιο"],
                    rows=[
                        AnalysisRow(cells=["1", "Slow Start", "1", "1", "Εκκίνηση"]),
                        AnalysisRow(cells=["2", "Slow Start", "2", "2", "× 2"]),
                        AnalysisRow(cells=["3", "Slow Start", "4", "4", "× 2"]),
                        AnalysisRow(cells=["4", "Slow Start", "8", "8", "× 2"]),
                        AnalysisRow(cells=["5", "Slow Start", "16", "16", "cwnd = ssthresh"], highlight=True),
                        AnalysisRow(cells=["6", "Congestion Avoidance", "17", "17", "+1 MSS"], highlight=True),
                        AnalysisRow(cells=["7", "Congestion Avoidance", "18", "18", "Εδώ: 3 duplicate ACKs → απώλεια"], highlight=True),
                    ],
                    note="Μετά την απώλεια: Tahoe → (ssthresh 9, cwnd 1)· Reno → (ssthresh 9, cwnd 12 = ssthresh + 3) και συνέχεια σε CA.",
                ),
            ],
            answer="Γύροι 1-7: 1, 2, 4, 8, 16, 17, 18 KB. Στον 6ο γύρο cwnd = 17 KB. Μετά την απώλεια: Tahoe θέτει ssthresh = 9 KB και cwnd = 1 KB (Slow Start)· Reno θέτει ssthresh = 9 KB και cwnd = 12 KB (Fast Recovery, απευθείας CA).",
            tips=[
                "Η εκθετική φάση σταματά στο ssthresh — από εκεί μπαίνουμε σε AIMD (+1 MSS/RTT).",
                "Το floor στη διαίρεση: floor(18/2) = 9 — με μονάδες MSS πάντα.",
                "Τα 3 dup ACK υποδηλώνουν ότι ο δίαυλος λειτουργεί (μόνο ένα τμήμα χάθηκε) — γι' αυτό το Reno δεν πέφτει στο 1.",
            ],
        ),
        ExamQuestion(
            thema="Θέμα 2",
            thema_title="Έλεγχος Συμφόρησης TCP & Ρυθμοαπόδοση",
            sub_number="2β",
            title="Ρυθμοαπόδοση Παραθύρου & BDP",
            question_type="computational",
            prompt="Σύνδεση TCP με μέγεθος παραθύρου 64 KB και RTT = 100 ms, χωρίς απώλειες. Να υπολογιστεί η μέγιστη ρυθμοαπόδοση (throughput) και το απαιτούμενο μέγεθος παραθύρου για ρυθμοαπόδοση 100 Mbps με το ίδιο RTT (γινόμενο εύρους-καθυστέρησης).",
            given=[
                GivenParameter(label="Μέγεθος παραθύρου W", value="64 KB = 65.536 bytes = 524.288 bits", source="εκφώνηση Θέματος 2.2"),
                GivenParameter(label="RTT", value="100 ms = 0,1 s", source="εκφώνηση Θέματος 2.2"),
                GivenParameter(label="Στόχος ρυθμοαπόδοσης", value="100 Mbps", source="εκφώνηση Θέματος 2.2"),
            ],
            steps=[
                CalculationStep(
                    label="Βήμα 1 — Τύπος Ρυθμοαπόδοσης",
                    description="Με σταθερό παράθυρο W και RTT, ο αποστολέας μπορεί να «ελέγξει» W bytes ανά RTT (το παράθυρο γεμίζει και περιμένει ACK):",
                    latex=r"\text{Throughput}_{max} = \frac{W}{\text{RTT}}",
                ),
                CalculationStep(
                    label="Βήμα 2 — Υπολογισμός για W = 64 KB",
                    description="Μετατροπή σε bits: 64 KB = 65.536 bytes × 8 = 524.288 bits. Διαίρεση με RTT = 0,1 s:",
                    latex=r"T = \frac{524.288\ \text{bits}}{0{,}1\ \text{s}} = 5.242.880\ \text{bps} \approx 5{,}24\ \text{Mbps}",
                    result="Μέγιστη ρυθμοαπόδοση: 5,24 Mbps",
                ),
                CalculationStep(
                    label="Βήμα 3 — Απαιτούμενο Παράθυρο για 100 Mbps",
                    description="Αναιρούμε τον τύπο ως προς W: το παράθυρο πρέπει να καλύπτει το γινόμενο εύρους-καθυστέρησης (BDP), δηλαδή τα bits που «ταξιδεύουν» στον δίαυλο πριν επιστρέψει το πρώτο ACK:",
                    latex=r"W = R \times \text{RTT} = 100 \times 10^{6} \times 0{,}1 = 10^{7}\ \text{bits} = 1.250.000\ \text{bytes} = 1{,}25\ \text{MB}",
                    result="Απαιτούμενο παράθυρο: 1,25 MB (= BDP)",
                ),
                CalculationStep(
                    label="Βήμα 4 — Παρατήρηση Window Scaling",
                    description="Το πεδίο Window της επικεφαλίδας TCP είναι 16-bit: μέγιστο 65.535 bytes ≈ 64 KB — μικρότερο του BDP των 1,25 MB. Για πλήρη αξιοποίηση των 100 Mbps απαιτείται η επιλογή window scaling (παράγοντας κλιμάκωσης κατά τη χειραψία).",
                ),
            ],
            answer="Throughput: 64 KB / 0,1 s = 5,24 Mbps. Για 100 Mbps χρειάζεται W = 100 Mbps × 0,1 s = 1,25 MB (BDP) — επιτεύξιμο μόνο με TCP window scaling.",
            tips=[
                "Προσοχή στις μονάδες: πάντα bits για τοthroughput (× 8 από bytes).",
                "Κανόνας: αν W &lt; BDP ο δίαυλος μένει υποχρησιμοποιημένος· αν W ≥ BDP, το throughput οριοθετείται από το εύρος ζώνης.",
            ],
        ),
        ExamQuestion(
            thema="Θέμα 3",
            thema_title="Αλγόριθμος Δρομολόγησης Link-State (Dijkstra)",
            sub_number="3",
            title="Εκτέλεση Dijkstra από τον u + Πίνακας Δρομολόγησης",
            question_type="computational",
            prompt="Δίνεται τοπολογία 5 δρομολογητών (u, v, w, x, y) με κόστη ζεύξεων: c(u,v)=2, c(u,w)=5, c(u,x)=1, c(x,v)=2, c(x,w)=3, c(x,y)=1, c(v,w)=3, c(y,w)=1. Εκτελέστε τον αλγόριθμο Dijkstra με αρχικό κόμβο το u, βήμα-βήμα, και προσδιορίστε τον πίνακα δρομολόγησης του u (ελάχιστο κόστος & επόμενο άλμα).",
            given=[
                GivenParameter(label="Κόμβοι", value="u (πηγή), v, w, x, y", source="εκφώνηση Θέματος 3"),
                GivenParameter(label="Ζεύξεις", value="u-v:2, u-w:5, u-x:1, x-v:2, x-w:3, x-y:1, v-w:3, y-w:1", source="εκφώνηση Θέματος 3"),
                GivenParameter(label="Πηγή", value="u", source="εκφώνηση Θέματος 3"),
            ],
            steps=[
                CalculationStep(
                    label="Βήμα 0 — Αρχικοποίηση",
                    description="N' = {u} (κλίκα οριστικοποιημένων). Άμεσοι γείτονες του u: D(v) = 2, D(w) = 5, D(x) = 1· ο y δεν είναι γείτονας, άρα D(y) = άπειρο. Ελάχιστο: x με D(x) = 1 → προστίθεται στην N'.",
                    latex=r"N' = \{u\}\!: \; D(x)=1,\; D(v)=2,\; D(w)=5,\; D(y)=\infty \Rightarrow \text{επιλογή } x",
                ),
                CalculationStep(
                    label="Βήμα 1 — Προσθήκη του x",
                    description="Νέα κλίκα N' = {u, x}. Χαλαρώνουμε τις ακμές του x: προς v: min(2, 1+2) = 2 (απευθείας παραμένει)· προς w: min(5, 1+3) = 4 (βελτιώνεται μέσω x)· προς y: min(∞, 1+1) = 2 (νέα διαδρομή μέσω x). Ελάχιστα v και y με 2 — επιλέγουμε το y.",
                    latex=r"D(v) = \min(2, 1{+}2) = 2,\;\; D(w) = \min(5, 1{+}3) = 4,\;\; D(y) = \min(\infty, 1{+}1) = 2",
                ),
                CalculationStep(
                    label="Βήμα 2 — Προσθήκη του y",
                    description="N' = {u, x, y}. Χαλάρωση της ακμής y-w: min(4, 2+1) = 3 — το w βελτιώνεται μέσω y. Ελάχιστο πλέον το v με D(v) = 2.",
                    latex=r"D(w) = \min(4, 2{+}1) = 3 \;\;(\text{μέσω } y) \Rightarrow \text{επιλογή } v",
                ),
                CalculationStep(
                    label="Βήμα 3 — Προσθήκη του v",
                    description="N' = {u, x, y, v}. Χαλάρωση v-w: min(3, 2+3) = 3 — καμία βελτίωση. Ελάχιστο το w με D(w) = 3.",
                    latex=r"D(w) = \min(3, 2{+}3) = 3 \Rightarrow \text{επιλογή } w",
                ),
                CalculationStep(
                    label="Βήμα 4 — Ολοκλήρωση",
                    description="N' = {u, x, y, v, w}: όλοι οι κόμβοι οριστικοποιήθηκαν. Το δένδρο SPF από το u: u→x (1), x→y (1), u→v (2), y→w (1). Ο πίνακας δρομολόγησης προκύπτει από τα τελικά D() και το πρώτο άλμα κάθε διαδρομής.",
                ),
            ],
            answer_tables=[
                AnalysisTable(
                    title="Πίνακας Βημάτων Dijkstra (N' & D())",
                    headers=["Βήμα", "N' (οριστικοποιημένα)", "D(v)", "D(w)", "D(x)", "D(y)", "Επιλογή"],
                    rows=[
                        AnalysisRow(cells=["0", "{u}", "2", "5", "1", "∞", "x (1)"], highlight=False),
                        AnalysisRow(cells=["1", "{u, x}", "2", "4 (μέσω x)", "1*", "2 (μέσω x)", "y (2)"], highlight=False),
                        AnalysisRow(cells=["2", "{u, x, y}", "2", "3 (μέσω y)", "1*", "2*", "v (2)"], highlight=False),
                        AnalysisRow(cells=["3", "{u, x, y, v}", "2*", "3", "1*", "2*", "w (3)"], highlight=False),
                        AnalysisRow(cells=["4", "{u, x, y, v, w}", "2*", "3*", "1*", "2*", "Τέλος"], highlight=True),
                    ],
                    note="Ο αστερίσκος (*) δηλώνει οριστικοποιημένη τιμή· σε ισοβαθμία (v/y με 2 στο Βήμα 1) η επιλογή είναι αυθαίρετη και δεν αλλάζει το αποτέλεσμα.",
                ),
                AnalysisTable(
                    title="Τελικός Πίνακας Δρομολόγησης του u",
                    headers=["Προορισμός", "Ελάχιστο Κόστος", "Διαδρομή", "Επόμενο Άλμα"],
                    rows=[
                        AnalysisRow(cells=["x", "1", "u → x", "x (απευθείας)"], highlight=True),
                        AnalysisRow(cells=["v", "2", "u → v", "v (απευθείας, ζεύξη κόστους 2)"], highlight=True),
                        AnalysisRow(cells=["y", "2", "u → x → y", "x"], highlight=True),
                        AnalysisRow(cells=["w", "3", "u → x → y → w", "x"], highlight=True),
                    ],
                ),
            ],
            answer="D(x)=1 απευθείας · D(v)=2 απευθείας · D(y)=2 μέσω x · D(w)=3 μέσω x (διαδρομή u→x→y→w). Σειρά οριστικοποίησης: x, y, v, w.",
            tips=[
                "Κάθε βήμα: προσθέτεις τον ελάχιστο εκτός N', χαλαρώνεις τις ακμές του, προχώρας — μέχρι να γεμίσει το N'.",
                "Το επόμενο άλμα για τον w είναι το x (όχι το y): η διαδρομή ξεκινά u→x και το u βλέπει μόνο το τοπικό πρώτο άλμα.",
                "Η απευθείας ζεύξη u-w (κόστος 5) χάνει από το μονοπάτι μέσω x-y (1+1+1 = 3) — μην υποθέτετε ότι οι άμεσες ζεύξεις είναι πάντα η βέλτιστη επιλογή.",
            ],
        ),
        ExamQuestion(
            thema="Θέμα 4",
            thema_title="Αριθμοί Ακολουθίας & Επιβεβαιώσεις TCP",
            sub_number="4",
            title="Ιχνηλάτιση SEQ/ACK με ISN 3000 / 5000",
            question_type="computational",
            prompt="Μια σύνδεση TCP ξεκινά με ISN πελάτη 3000 και ISN διακομιστή 5000. Μετά τη χειραψία: ο πελάτης στέλνει 500 bytes, ο διακομιστής 300 bytes, και ο πελάτης άλλα 200 bytes. Εμφανίστε για κάθε segment: κατεύθυνση, σημαίες, SEQ, ACK και τα bytes δεδομένων.",
            given=[
                GivenParameter(label="ISN πελάτη", value="3000", source="εκφώνηση Θέματος 4"),
                GivenParameter(label="ISN διακομιστή", value="5000", source="εκφώνηση Θέματος 4"),
                GivenParameter(label="Μεταφορά", value="C: 500 B → S: 300 B → C: 200 B", source="εκφώνηση Θέματος 4"),
            ],
            steps=[
                CalculationStep(
                    label="Βήμα 1 — Κανόνες SEQ / ACK",
                    description="SEQ = ο αριθμός του ΠΡΩΤΟΥ byte δεδομένων του segment· ACK = το επόμενο αναμενόμενο byte (συσσωρευτικά)· τα SYN και FIN καταναλώνουν από 1 αριθμό ακολουθίας το καθένα (τα δεδομένα μετρώνται σε bytes).",
                ),
                CalculationStep(
                    label="Βήμα 2 — Χειραψία (segments 1-3)",
                    description="SYN (C→S): SEQ 3000, χωρίς ACK — το SYN «καταναλώνει» το 3000. SYN+ACK (S→C): SEQ 5000, ACK 3001. ACK (C→S): SEQ 3001, ACK 5001 — η σύνδεση εγκαθίσταται.",
                ),
                CalculationStep(
                    label="Βήμα 3 — Εναλλαγή Δεδομένων (segments 4-6)",
                    description="Δεδομένα πελάτη 500 B: SEQ 3001 (bytes 3001-3500), ACK 5001 → ο server απαντά ACK 3501. Δεδομένα server 300 B: SEQ 5001 (bytes 5001-5300), ACK 3501 → ο client δέχεται και απαντά. Δεδομένα πελάτη 200 B: SEQ 3501 (bytes 3501-3700), ACK 5301.",
                ),
                CalculationStep(
                    label="Βήμα 4 — Τελική Επιβεβαίωση (segment 7)",
                    description="Ο διακομιστής επιβεβαιώνει τα τελευταία 200 bytes: σκέτο ACK με SEQ 5301 και ACK 3701.",
                ),
            ],
            answer_tables=[
                AnalysisTable(
                    title="Πλήρης Ιχνηλάτιση Segments",
                    headers=["#", "Κατεύθυνση", "Σημαίες", "SEQ", "ACK", "Bytes Δεδομένων"],
                    rows=[
                        AnalysisRow(cells=["1", "Πελάτης → Διακομιστής", "SYN", "3000", "—", "0 (το SYN καταναλώνει τον 3000)"]),
                        AnalysisRow(cells=["2", "Διακομιστής → Πελάτης", "SYN + ACK", "5000", "3001", "0"]),
                        AnalysisRow(cells=["3", "Πελάτης → Διακομιστής", "ACK", "3001", "5001", "0"], highlight=False),
                        AnalysisRow(cells=["4", "Πελάτης → Διακομιστής", "PSH + ACK", "3001", "5001", "500 (bytes 3001-3500)"], highlight=True),
                        AnalysisRow(cells=["5", "Διακομιστής → Πελάτης", "PSH + ACK", "5001", "3501", "300 (bytes 5001-5300)"], highlight=True),
                        AnalysisRow(cells=["6", "Πελάτης → Διακομιστής", "PSH + ACK", "3501", "5301", "200 (bytes 3501-3700)"], highlight=True),
                        AnalysisRow(cells=["7", "Διακομιστής → Πελάτης", "ACK", "5301", "3701", "0"], highlight=False),
                    ],
                    note="Έλεγχος: μετά τα 500 B ο client περιμένει ACK 3501· μετά τα 300 B ο server έχει στείλει 5300 bytes-1 → επόμενο 5301· μετά τα 200 B το τελικό ACK 3701 = 3001 + 500 + 200.",
                ),
            ],
            answer="SEG/ACK ανά segment όπως στον πίνακα: SYN(3000) → SYN+ACK(5000, ACK 3001) → ACK(3001, ACK 5001) → DATA(SEQ 3001, 500B) → DATA+ACK(SEQ 5001, ACK 3501, 300B) → DATA+ACK(SEQ 3501, ACK 5301, 200B) → ACK(SEQ 5301, ACK 3701).",
            tips=[
                "Το SYN «τραβάει» τον SEQ μία θέση: τα δεδομένα του πελάτη ξεκινούν στο 3001, όχι στο 3000.",
                "Τα ACK είναι συσσωρευτικά: ACK 3701 σημαίνει «λήφθηκαν όλα τα bytes μέχρι το 3700».",
                "Το piggybacking (segment 5: δεδομένα + επιβεβαίωση μαζί) είναι συνηθισμένο και εξοικονομεί segments.",
            ],
        ),
    ]

    analysis_tables = [
        AnalysisTable(
            title="Αναφορά: Well-Known Ports",
            headers=["Θύρα", "Υπηρεσία", "Μεταφορά"],
            rows=[
                AnalysisRow(cells=["20 / 21", "FTP (δεδομένα / έλεγχος)", "TCP"]),
                AnalysisRow(cells=["22 / 23", "SSH / Telnet", "TCP"]),
                AnalysisRow(cells=["25", "SMTP (αποστολή)", "TCP"]),
                AnalysisRow(cells=["53", "DNS (queries)", "UDP (και TCP σε zone transfer)"], highlight=True),
                AnalysisRow(cells=["80 / 443", "HTTP / HTTPS", "TCP"]),
                AnalysisRow(cells=["110 / 143", "POP3 / IMAP (λήψη)", "TCP"], highlight=True),
            ],
        ),
    ]

    diagram_title = "Τοπολογία Dijkstra: Κόστη Ζεύξεων & Τελικά Ελάχιστα Κόστη από το u"
    diagram_nodes = [
        DiagramNode(id="u", label="u (Πηγή)", x=80, y=260, w=170, details=["Dijkstra: αρχικός κόμβος", "D(u) = 0", "SPF: u→x→y→w, u→v"], highlight=True),
        DiagramNode(id="v", label="v", x=430, y=40, w=170, details=["D(v) = 2", "Απευθείας ζεύξη u-v (2)", "Διαδρομή: u → v"]),
        DiagramNode(id="x", label="x", x=430, y=260, w=170, details=["D(x) = 1", "Απευθείας ζεύξη u-x (1)", "Πρώτη οριστικοποίηση"]),
        DiagramNode(id="y", label="y", x=430, y=480, w=170, details=["D(y) = 2", "Διαδρομή: u → x → y", "Κόστος 1 + 1 = 2"]),
        DiagramNode(id="w", label="w", x=880, y=260, w=200, details=["D(w) = 3", "Διαδρομή: u → x → y → w", "1 + 1 + 1 = 3", "Επόμενο άλμα από u: x"], highlight=True),
    ]
    diagram_edges = [
        DiagramEdge(path="M 250,300 L 430,300", label="c = 1", lx=340, ly=283),
        DiagramEdge(path="M 250,270 L 430,85", label="c = 2", lx=315, ly=160),
        DiagramEdge(path="M 250,330 C 450,430 700,430 880,330", label="c = 5", lx=640, ly=408),
        DiagramEdge(path="M 515,260 L 515,118", label="c = 2", lx=545, ly=190),
        DiagramEdge(path="M 515,338 L 515,480", label="c = 1", lx=545, ly=412),
        DiagramEdge(path="M 600,300 L 880,300", label="c = 3", lx=740, ly=283),
        DiagramEdge(path="M 600,519 L 880,338", label="c = 1", lx=740, ly=445),
        DiagramEdge(path="M 600,80 C 800,110 980,170 980,260", label="c = 3", lx=880, ly=140),
    ]
    diagram_note = "Οι ετικέτες ζεύξεων δείχνουν τα κόστη c()· οι κόμβες συνοψίζουν τα τελικά D() και τις βραχύτερες διαδρομές του SPF δένδρου από το u."

    justifications = [
        DesignJustification(
            title="1. Εκθετική και μετά Γραμμική Αύξηση (AIMD)",
            color_class="text-blue-500",
            description="Το TCP ξεκινά επιθετικά (διπλασιασμός ανά RTT) για να βρει γρήγορα το σημείο συμφόρησης, και συνεχίζει συντηρητικά (+1 MSS) για να μην το υπερβεί — η κλασική λογική AIMD.",
        ),
        DesignJustification(
            title="2. Reno: Γιατί ssthresh + 3",
            color_class="text-amber-500",
            description="Τα 3 διπλότυπα ACK αποδεικνύουν ότι 3 τμήματα παραδόθηκαν μετά το χαμένο: το κανάλι δεν είναι κατεστραμμένο, οπότε το Reno κρατά το παράθυρο κοντά στο μισό (ssthresh + 3) αντί να πέσει στο 1 όπως το Tahoe.",
        ),
        DesignJustification(
            title="3. BDP ως Κατώφλι Παραθύρου",
            color_class="text-emerald-500",
            description="Το γινόμενο εύρους-καθυστέρησης (R × RTT) δίνει τα bytes «σε πτήση»: μόνο παράθυρο ≥ BDP αξιοποιεί πλήρως τον δίαυλο — εξ ου και η ανάγκη window scaling για μεγάλους BDP.",
        ),
        DesignJustification(
            title="4. Dijkstra με Χαλάρωση Ακμών",
            color_class="text-purple-500",
            description="Κάθε νέος οριστικοποιημένος κόμβος χαλαρώνει τις ακμές του (min(D, D(u)+c)): έτσι η ελάχιστη διαδρομή προς το w (μέσω x-y, κόστος 3) νικά την απευθείας ζεύξη κόστους 5.",
        ),
    ]

    solution_code = """# Θέμα 2α & 3: Προσομοίωση cwnd (Tahoe/Reno) και εκτέλεση Dijkstra
import heapq

# --- Θέμα 2α: Εξέλιξη cwnd (MSS = 1 KB, ssthresh = 16 KB, απώλεια στον 7ο) ---
MSS, ssthresh, cwnd = 1, 16, 1
rounds = []
for rtt in range(1, 8):
    rounds.append((rtt, cwnd))
    cwnd = cwnd * 2 if cwnd < ssthresh else cwnd + MSS

print("Εξέλιξη cwnd:", " -> ".join(f"Γ{r}:{c}" for r, c in rounds))
print(f"cwnd στον 6ο γύρο: {rounds[5][1]} KB")
print("Απώλεια στον 7ο (cwnd = 18):")
print(f"  Tahoe: ssthresh = {18 // 2}, cwnd = 1")
print(f"  Reno:  ssthresh = {18 // 2}, cwnd = {18 // 2 + 3}")

# --- Θέμα 3: Dijkstra από τον u ---
graph = {
    "u": {"v": 2, "w": 5, "x": 1},
    "x": {"v": 2, "w": 3, "y": 1},
    "y": {"w": 1},
    "v": {"w": 3},
}
dist, nxt, heap = {"u": 0}, {"u": "u"}, [(0, "u")]
done = set()
while heap:
    d, node = heapq.heappop(heap)
    if node in done:
        continue
    done.add(node)
    for nb, cost in graph.get(node, {}).items():
        if nb in done:
            continue
        cand = d + cost
        if cand < dist.get(nb, 10**9):
            dist[nb] = cand
            # Πρώτο άλμα από το u: ο ίδιος ο γείτονας αν χαλαρώνουμε από την πηγή,
            # αλλιώς κληρονομούμε το πρώτο άλμα του ενδιάμεσου κόμβου
            nxt[nb] = nb if node == "u" else nxt[node]
            heapq.heappush(heap, (cand, nb))

for dest in ("v", "w", "x", "y"):
    print(f"Προορισμός {dest}: D = {dist[dest]}, επόμενο άλμα {nxt[dest]}")
"""

    return Scenario(
        id="synth_exam_3",
        title="Συνθετικό Θέμα 3",
        subtitle="Θύρες & Χειραψία TCP · cwnd Tahoe/Reno & BDP · Dijkstra Link-State · SEQ/ACK",
        course_tag="NETWORKING (Συνθετική Εξέταση 3)",
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
