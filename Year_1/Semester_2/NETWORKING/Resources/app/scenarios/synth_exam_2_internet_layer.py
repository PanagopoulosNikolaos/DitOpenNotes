"""Synthetic Exam 2 (Internet Layer: IP Datagram, Fragmentation, TTL & NAT) scenario module.

A complete synthetic exam paper in the exact structure of the course's
practice exam (4 Themata x 2.5 points, 2.5 hours), covering the IPv4 header
fields, ICMP message types, ARP resolution, IP fragmentation and
reassembly mechanics, TTL hop tracing with ICMP Time Exceeded, and NAT
translation tables. Every question carries a worked step-by-step solution.
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


def createSynthExam2Scenario() -> Scenario:
    """Constructs and returns the Synthetic Exam 2 (Internet Layer) scenario.

    Returns:
        Scenario: Fully populated scenario instance.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(
                    text="<strong>Συνθετικό Θέμα Εξετάσεων 2: Δίκτυα Υπολογιστών — Επίπεδο Internet (IP Datagram, Κατάτμηση, TTL & NAT)</strong>",
                    is_highlight=True,
                    category="term",
                    tag_label="ΣΥΝΘΕΤΙΚΗ ΕΞΕΤΑΣΗ",
                    badge_class="badge-term",
                    tooltip="Ταξινόμηση: Συνθετικό θέμα εξετάσεων για το επίπεδο Internet. Εντοπισμός: Τίτλος του συνθετικού θέματος. Εφαρμογή: Καλύπτει επικεφαλίδα IPv4, ICMP/ARP, κατάτμηση, TTL και NAT.",
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
                    text="Θέμα 1: Επικεφαλίδα IPv4 & Πρωτόκολλα Υποστήριξης (Πολλαπλής Επιλογής)",
                    is_highlight=True,
                    category="proto",
                    tag_label="MCQ",
                    badge_class="badge-proto",
                    tooltip="Ταξινόμηση: Θέμα πολλαπλής επιλογής για πεδία IPv4 και ICMP/ARP. Εντοπισμός: Επικεφαλίδα «Θέμα 1». Εφαρμογή: Λύνεται με τις τιμές IHL, Protocol, τύπων ICMP και το αντικείμενο του ARP.",
                ),
            ],
            is_heading=True,
        ),
        Paragraph(
            segments=[
                TextSegment(text="α. Ποιο είναι το "),
                TextSegment(
                    text="ελάχιστο μήκος της επικεφαλίδας IPv4",
                    is_highlight=True,
                    category="term",
                    tag_label="ΖΗΤΟΥΜΕΝΟ",
                    badge_class="badge-term",
                    tooltip="Ταξινόμηση: Ελάχιστο μέγεθος επικεφαλίδας. Εντοπισμός: Ερώτημα α του Θέματος 1. Εφαρμογή: Το IHL μετρά σε λέξεις των 32 bits· ελάχιστο IHL = 5 → 20 bytes.",
                ),
                TextSegment(text=" (χωρίς Options);"),
            ],
        ),
        Paragraph(
            segments=[
                TextSegment(text="β. Η τιμή "),
                TextSegment(
                    text="17",
                    is_highlight=True,
                    category="given",
                    tag_label="ΔΕΔΟΜΕΝΟ",
                    badge_class="badge-given",
                    tooltip="Ταξινόμηση: Τιμή του πεδίου Protocol. Εντοπισμός: Ερώτημα β. Εφαρμογή: 6 = TCP, 17 = UDP, 1 = ICMP, 2 = IGMP.",
                ),
                TextSegment(text=" στο πεδίο Protocol της επικεφαλίδας IPv4 δηλώνει ότι το ωφέλιμο φορτίο μεταφέρεται από το:"),
            ],
        ),
        Paragraph(
            segments=[
                TextSegment(text="γ. Ένας "),
                TextSegment(
                    text="δρομολογητής δεν μπορεί να παρακολουθήσει τον όγκο της κίνησης",
                    is_highlight=True,
                    category="given",
                    tag_label="ΣΕΝΑΡΙΟ",
                    badge_class="badge-given",
                    tooltip="Ταξινόμηση: Σενάριο υπερφόρτωσης δρομολογητή. Εντοπισμός: Ερώτημα γ, διατύπωση από τη θεωρία ICMP. Εφαρμογή: Ενεργοποιείται το μήνυμα Source Quench για συγχρονισμό ταχύτητας.",
                ),
                TextSegment(text=". Τι είδους μήνυμα ICMP στέλνει;"),
            ],
        ),
        Paragraph(
            segments=[
                TextSegment(text="δ. Το πρωτόκολλο "),
                TextSegment(
                    text="ARP",
                    is_highlight=True,
                    category="proto",
                    tag_label="ΠΡΩΤΟΚΟΛΛΟ",
                    badge_class="badge-proto",
                    tooltip="Ταξινόμηση: Address Resolution Protocol. Εντοπισμός: Ερώτημα δ. Εφαρμογή: Δεδομένης IP εντός τοπικού δικτύου επιστρέφει τη φυσική MAC διεύθυνση.",
                ),
                TextSegment(text=", όταν λαμβάνει μια διεύθυνση IP, επιστρέφει:"),
            ],
        ),
        Paragraph(
            segments=[
                TextSegment(
                    text="Θέμα 2: Κατάτμηση IP (Fragmentation) & Επανασύνθεση",
                    is_highlight=True,
                    category="method",
                    tag_label="ΥΠΟΛΟΓΙΣΤΙΚΟ",
                    badge_class="badge-method",
                    tooltip="Ταξινόμηση: Υπολογιστικό θέμα κατάτμησης/επανασύνθεσης. Εντοπισμός: Επικεφαλίδα «Θέμα 2». Εφαρμογή: Εφαρμογή των κανόνων πολλαπλασίων του 8, MF και offset/8.",
                ),
            ],
            is_heading=True,
        ),
        Paragraph(
            segments=[
                TextSegment(text="1. Ένας δρομολογητής λαμβάνει ένα πακέτο IP με "),
                TextSegment(
                    text="Συνολικό Μήκος: 3000 bytes, Μήκος Επικεφαλίδας: 20 bytes, DF: 0, Identification: 12345",
                    is_highlight=True,
                    category="given",
                    tag_label="ΔΕΔΟΜΕΝΑ",
                    badge_class="badge-given",
                    tooltip="Ταξινόμηση: Παράμετροι κατάτμησης. Εντοπισμός: Ρητά δεδομένα του ερωτήματος 1. Εφαρμογή: Δεδομένα 2980 B, ανά τμήμα 1480 B → 3 τμήματα.",
                ),
                TextSegment(text=" και "),
                TextSegment(
                    text="MTU εξερχόμενης ζεύξης: 1500 bytes",
                    is_highlight=True,
                    category="given",
                    tag_label="ΔΕΔΟΜΕΝΟ",
                    badge_class="badge-given",
                    tooltip="Ταξινόμηση: Μέγιστη μονάδα μετάδοσης της εξερχόμενης ζεύξης. Εντοπισμός: Ρητό δεδομένο. Εφαρμογή: Περιορίζει κάθε τμήμα σε 1500 B συνολικά.",
                ),
                TextSegment(text=". Υπολογίστε για κάθε τμήμα: Μέγεθος, Total Length, Σημαία MF, Fragment Offset."),
            ],
        ),
        Paragraph(
            segments=[
                TextSegment(text="2. Λαμβάνετε τρία τμήματα IP: "),
                TextSegment(
                    text="A: Total Length 1500, Header 20, MF 1, Offset 0 · B: Total Length 1500, Header 20, MF 1, Offset 185 · C: Total Length 540, Header 20, MF 0, Offset 370",
                    is_highlight=True,
                    category="given",
                    tag_label="ΔΕΔΟΜΕΝΑ",
                    badge_class="badge-given",
                    tooltip="Ταξινόμηση: Σύνολο τμημάτων προς επανασύνθεση. Εντοπισμός: Πεδίο δεδομένων του ερωτήματος 2. Εφαρμογή: Το C είναι τελευταίο (MF=0)· αρχικά δεδομένα = 370×8 + 520 = 3480 B.",
                ),
                TextSegment(text=". Να βρεθεί το μέγεθος των αρχικών δεδομένων, το εύρος bytes κάθε τμήματος και να επαληθευθεί η ορθότητα της κατάτμησης."),
            ],
        ),
        Paragraph(
            segments=[
                TextSegment(
                    text="Θέμα 3: TTL & Ροή Πακέτου στο Δίκτυο",
                    is_highlight=True,
                    category="method",
                    tag_label="ΙΧΝΗΛΑΣΗ",
                    badge_class="badge-method",
                    tooltip="Ταξινόμηση: Θέμα ανίχνευσης TTL hop-by-hop. Εντοπισμός: Επικεφαλίδα «Θέμα 3». Εφαρμογή: Προσομοίωση μείωσης TTL ανά δρομολογητή και των μηνυμάτων ICMP.",
                ),
            ],
            is_heading=True,
        ),
        Paragraph(
            segments=[
                TextSegment(text="Ένα πακέτο ταξιδεύει μέσω της διαδρομής "),
                TextSegment(
                    text="Πηγή (192.168.1.10) → Δρομολογητής A → Δρομολογητής B → Δρομολογητής C → Προορισμός (10.0.0.5)",
                    is_highlight=True,
                    category="given",
                    tag_label="ΔΕΔΟΜΕΝΟ",
                    badge_class="badge-given",
                    tooltip="Ταξινόμηση: Διαδρομή τριών hops. Εντοπισμός: Ρητό δεδομένο του Θέματος 3. Εφαρμογή: Τρεις ενδιάμεσοι δρομολογητές μειώνουν διαδοχικά το TTL.",
                ),
                TextSegment(text=" με "),
                TextSegment(
                    text="αρχικό TTL: 5",
                    is_highlight=True,
                    category="given",
                    tag_label="ΔΕΔΟΜΕΝΟ",
                    badge_class="badge-given",
                    tooltip="Ταξινόμηση: Αρχική τιμή TTL. Εντοπισμός: Ρητό δεδομένο. Εφαρμογή: 5 − 3 hops = 2 κατά την παράδοση· αν ήταν 3, θα μηδένιζε στον C.",
                ),
                TextSegment(text=". Περιγράψτε τι συμβαίνει σε κάθε άλμα, ποιο μήνυμα ICMP (εάν υπάρχει) δημιουργείται, και τι θα άλλαζε αν το αρχικό TTL ήταν 3."),
            ],
        ),
        Paragraph(
            segments=[
                TextSegment(
                    text="Θέμα 4: NAT & Ιδιωτική Διευθυνσιοδότηση",
                    is_highlight=True,
                    category="method",
                    tag_label="ΠΙΝΑΚΑΣ",
                    badge_class="badge-method",
                    tooltip="Ταξινόμηση: Θέμα συμπλήρωσης πίνακα μετάφρασης NAT. Εντοπισμός: Επικεφαλίδα «Θέμα 4». Εφαρμογή: Αντιστοίχιση Inside Local ↔ Inside Global με μοναδικές θύρες.",
                ),
            ],
            is_heading=True,
        ),
        Paragraph(
            segments=[
                TextSegment(text="Μια εταιρεία χρησιμοποιεί "),
                TextSegment(
                    text="NAT",
                    is_highlight=True,
                    category="proto",
                    tag_label="ΠΡΩΤΟΚΟΛΛΟ",
                    badge_class="badge-proto",
                    tooltip="Ταξινόμηση: Network Address Translation στον ακραίο δρομολογητή. Εντοπισμός: «χρησιμοποιεί NAT» στην εκφώνηση. Εφαρμογή: Μεταφράζει ιδιωτικές διευθύνσεις στη δημόσια 203.0.113.5 με διακριτές θύρες.",
                ),
                TextSegment(text=" με ιδιωτικό δίκτυο "),
                TextSegment(
                    text="192.168.1.0/24",
                    is_highlight=True,
                    category="given",
                    tag_label="ΔΕΔΟΜΕΝΟ",
                    badge_class="badge-given",
                    tooltip="Ταξινόμηση: Εσωτερικό δίκτυο RFC 1918. Εντοπισμός: Ρητό δεδομένο. Εφαρμογή: Οι σταθμοί έχουν Inside Local διευθύνσεις 192.168.1.x.",
                ),
                TextSegment(text=" και "),
                TextSegment(
                    text="δημόσια IP: 203.0.113.5",
                    is_highlight=True,
                    category="given",
                    tag_label="ΔΕΔΟΜΕΝΟ",
                    badge_class="badge-given",
                    tooltip="Ταξινόμηση: Μία δημόσια διεύθυνση κοινή για όλες τις εξερχόμενες συνδέσεις. Εντοπισμός: Ρητό δεδομένο. Εφαρμογή: Ο NAT διαφοροποιεί τις συνδέσεις με μοναδικές θύρες (1024, 1025, ...).",
                ),
                TextSegment(text=". Ο δρομολογητής NAT μεταφράζει χρησιμοποιώντας αριθμούς θυρών. Συμπληρώστε τον πίνακα μετάφρασης και εξηγήστε τη ροή της επιστρεφόμενης κίνησης."),
            ],
        ),
        Paragraph(
            segments=[
                TextSegment(text="<code>Inside Local&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Inside Global&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Outside Global</code><br><code>192.168.1.10:5000&nbsp;&nbsp;&nbsp;?&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8.8.8.8:53</code><br><code>192.168.1.15:5001&nbsp;&nbsp;&nbsp;?&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;93.184.216.34:80</code><br><code>?&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;203.0.113.5:1026&nbsp;&nbsp;&nbsp;151.101.1.69:443</code>"),
            ],
            accent_border_color="accent",
        ),
    ]

    questions = [
        ExamQuestion(
            thema="Θέμα 1",
            thema_title="Επικεφαλίδα IPv4 & Πρωτόκολλα Υποστήριξης (Πολλαπλής Επιλογής)",
            sub_number="1α",
            title="Ελάχιστο Μήκος Επικεφαλίδας IPv4",
            question_type="mcq",
            prompt="Ποιο είναι το ελάχιστο μήκος της επικεφαλίδας IPv4 (χωρίς Options);",
            options=[
                QuestionOption(letter="A", text="8 bytes", is_correct=False, explanation="Τα 8 bytes είναι η επικεφαλίδα του UDP — όχι του IPv4."),
                QuestionOption(letter="B", text="16 bytes", is_correct=False, explanation="Δεν αντιστοιχεί σε κανένα βασικό πεδίο· προέρχεται από σύγχυση με 4 λέξεις των 32 bits."),
                QuestionOption(letter="C", text="20 bytes", is_correct=True, explanation="Το πεδίο IHL μετράει λέξεις των 32 bits (4 bytes)· ελάχιστη τιμή IHL = 5, άρα 5 × 4 = 20 bytes. Πρόσθετα Options αυξάνουν την επικεφαλίδα κατά πολλαπλάσια των 4 bytes."),
                QuestionOption(letter="D", text="24 bytes", is_correct=False, explanation="Το 24 θα σήμαινε IHL = 6, δηλαδή μία λέξη Options — όχι το ελάχιστο χωρίς Options."),
            ],
            answer="Σωστή απάντηση: <strong>C</strong> — 20 bytes (IHL = 5 λέξεις των 4 bytes).",
            tips=["Το ελάχιστο MTU ωφέλιμου φορτίου IPv4 πάνω σε Ethernet είναι 1500 − 20 = 1480 bytes.", "IHL = 5 είναι και η τιμή του πεδίου έκδοσης 0x45 που βλέπουμε σε dumps (4 = έκδοση, 5 = IHL)."],
        ),
        ExamQuestion(
            thema="Θέμα 1",
            thema_title="Επικεφαλίδα IPv4 & Πρωτόκολλα Υποστήριξης (Πολλαπλής Επιλογής)",
            sub_number="1β",
            title="Πεδίο Protocol = 17",
            question_type="mcq",
            prompt="Η τιμή 17 στο πεδίο Protocol της επικεφαλίδας IPv4 δηλώνει ότι το ωφέλιμο φορτίο μεταφέρεται από το:",
            options=[
                QuestionOption(letter="A", text="TCP", is_correct=False, explanation="Το TCP έχει αριθμό πρωτοκόλλου 6."),
                QuestionOption(letter="B", text="UDP", is_correct=True, explanation="Το UDP καταγράφεται με Protocol = 17· ακολουθούν TCP = 6, ICMP = 1, IGMP = 2. Ο παραλήπτης έτσι ξέρει σε ποιο πρωτόκολλο να παραδώσει το φορτίο (demultiplexing)."),
                QuestionOption(letter="C", text="ICMP", is_correct=False, explanation="Το ICMP έχει αριθμό 1 (μηνύματα ελέγχου/σφαλμάτων όπως ping)."),
                QuestionOption(letter="D", text="IGMP", is_correct=False, explanation="Το IGMP (διαχείριση multicast ομάδων) έχει αριθμό 2."),
            ],
            answer="Σωστή απάντηση: <strong>B</strong> — UDP (Protocol = 17).",
            tips=["Αποστηθίστε την τριάδα: 6 = TCP, 17 = UDP, 1 = ICMP (και 2 = IGMP)."],
        ),
        ExamQuestion(
            thema="Θέμα 1",
            thema_title="Επικεφαλίδα IPv4 & Πρωτόκολλα Υποστήριξης (Πολλαπλής Επιλογής)",
            sub_number="1γ",
            title="ICMP για Υπερφορτωμένο Δρομολογητή",
            question_type="mcq",
            prompt="Ένας δρομολογητής δεν μπορεί να παρακολουθήσει τον όγκο της κίνησης. Τι είδους μήνυμα ICMP στέλνει;",
            options=[
                QuestionOption(letter="A", text="Echo Request", is_correct=False, explanation="Το Echo Request είναι το αίτημα του ping για έλεγχο συνδεσιμότητας, όχι μήνυμα ρύθμισης ροής."),
                QuestionOption(letter="B", text="Source Quench", is_correct=True, explanation="Το Source Quench στέλνεται από τον δρομολογητή προς την πηγή για να «συγχρονίσει» γρήγορους αποστολείς με αργούς/υπερφορτωμένους κόμβους — μηχανισμός ελέγχου ροής στο επίπεδο IP."),
                QuestionOption(letter="C", text="Destination Unreachable", is_correct=False, explanation="Αποστέλλεται όταν το datagram δεν μπορεί να παραδοθεί (προσβάσιμος προορισμός/δίκτυο/θύρα), όχι για υπερφόρτωση."),
                QuestionOption(letter="D", text="Time Exceeded", is_correct=False, explanation="Αποστέλλεται όταν το TTL μηδενιστεί ή όταν λήξει ο χρόνος επανασύνθεσης τμημάτων."),
            ],
            answer="Σωστή απάντηση: <strong>B</strong> — Source Quench (συγχρονισμός ροής πηγής με υπερφορτωμένο δρομολογητή).",
            tips=["Δομή πακέτου ICMP: Type + Code + Checksum + Data· ο πίνακας τύπων είναι βασικός για MCQ."],
        ),
        ExamQuestion(
            thema="Θέμα 1",
            thema_title="Επικεφαλίδα IPv4 & Πρωτόκολλα Υποστήριξης (Πολλαπλής Επιλογής)",
            sub_number="1δ",
            title="Τι Επιστρέφει το ARP",
            question_type="mcq",
            prompt="Το πρωτόκολλο ARP, όταν λαμβάνει μια διεύθυνση IP, επιστρέφει:",
            options=[
                QuestionOption(letter="A", text="Τη φυσική διεύθυνση (MAC) που αντιστοιχεί στην IP", is_correct=True, explanation="Το ARP επιλύει IP → MAC εντός του τοπικού δικτύου: ARP Request σε broadcast («Ποιος έχει την IP X;») και ARP Reply σε unicast με τη MAC του κάτοχου· η αντιστοίχιση αποθηκεύεται σε ARP cache."),
                QuestionOption(letter="B", text="Τον αριθμό θύρας της εφαρμογής", is_correct=False, explanation="Οι θύρες ανήκουν στο επίπεδο μεταφοράς (TCP/UDP) και δεν επιλύονται από το ARP."),
                QuestionOption(letter="C", text="Τη διεύθυνση της προεπιλεγμένης πύλης", is_correct=False, explanation="Η default gateway επιλέγεται από τον πίνακα δρομολόγησης, όχι από το ARP — το ARP απλώς θα βρει τη MAC της πύλης αφού γνωρίζει την IP της."),
                QuestionOption(letter="D", text="Τη μάσκα υποδικτύου", is_correct=False, explanation="Η μάσκα προκύπτει από τη διαμόρφωση DHCP/στατική, δεν είναι αντικείμενο του ARP."),
            ],
            answer="Σωστή απάντηση: <strong>A</strong> — τη φυσική διεύθυνση (MAC) που αντιστοιχεί στη δοσμένη IP.",
            tips=["Παράδειγμα ροής: A θέλει τον C (192.168.1.12) → ARP broadcast → C απαντά με MAC → αποθήκευση στον πίνακα ARP → έναρξη επικοινωνίας."],
        ),
        ExamQuestion(
            thema="Θέμα 2",
            thema_title="Κατάτμηση IP (Fragmentation) & Επανασύνθεση",
            sub_number="2α",
            title="Κατάτμηση Datagram 3000 B με MTU 1500",
            question_type="computational",
            prompt="Ένας δρομολογητής λαμβάνει ένα πακέτο IP με Συνολικό Μήκος 3000 bytes, Μήκος Επικεφαλίδας 20 bytes, DF 0, Identification 12345 και MTU εξερχόμενης ζεύξης 1500 bytes. Υπολογίστε για κάθε τμήμα: Μέγεθος, Total Length, Σημαία MF, Fragment Offset.",
            given=[
                GivenParameter(label="Συνολικό Μήκος", value="3000 bytes", source="εκφώνηση Θέματος 2.1"),
                GivenParameter(label="Μήκος Επικεφαλίδας", value="20 bytes", source="εκφώνηση Θέματος 2.1"),
                GivenParameter(label="Σημαία DF", value="0 (επιτρέπεται η κατάτμηση)", source="εκφώνηση Θέματος 2.1"),
                GivenParameter(label="Identification", value="12345", source="εκφώνηση Θέματος 2.1"),
                GivenParameter(label="MTU εξερχόμενης ζεύξης", value="1500 bytes", source="εκφώνηση Θέματος 2.1"),
            ],
            steps=[
                CalculationStep(
                    label="Βήμα 1 — Δεδομένα προς Κατάτμηση",
                    description="Το αρχικό datagram μεταφέρει 3000 − 20 = 2980 bytes δεδομένων. Κάθε τμήμα επαναλαμβάνει την 20-byte επικεφαλίδα IPv4.",
                    latex=r"\text{Δεδομένα} = 3000 - 20 = 2980\,\text{bytes}",
                ),
                CalculationStep(
                    label="Βήμα 2 — Ωφέλιμα Ανά Τμήμα (πολλαπλάσιο του 8)",
                    description="Κάθε τμήμα χωράει έως 1500 − 20 = 1480 bytes δεδομένων. Το 1480 είναι πολλαπλάσιο του 8 (1480 / 8 = 185) — απαραίτητη προϋπόθεση επειδή το Fragment Offset μετρά σε μονάδες των 8 bytes.",
                    latex=r"\text{ανά τμήμα} = 1500 - 20 = 1480,\qquad 1480 / 8 = 185 \;\;(\text{ακέραιο})",
                ),
                CalculationStep(
                    label="Βήμα 3 — Αριθμός Τμημάτων",
                    description="2980 / 1480 = 2,01..., άρα χρειάζονται 2 πλήρη τμήματα και ένα τρίτο με το υπόλοιπο: 2980 − 2 × 1480 = 20 bytes δεδομένων.",
                    latex=r"2980 = 1480 + 1480 + 20 \Rightarrow 3\,\text{τμήματα}",
                ),
                CalculationStep(
                    label="Βήμα 4 — Πεδία Κάθε Τμήματος",
                    description="Τα δύο πρώτα τμήματα φέρουν MF = 1 (ακολουθούν κι άλλα) και offsets 0 και 1480/8 = 185· το τελευταίο φέρει MF = 0 και offset 2960/8 = 370. Όλα μοιράζονται το Identification 12345 και DF = 0.",
                    latex=r"F_1\!(0),\; F_2\!(1480/8 = 185),\; F_3\!(2960/8 = 370),\;\; \text{ID} = 12345",
                ),
            ],
            answer_tables=[
                AnalysisTable(
                    title="Τελικός Πίνακας Κατάτμησης (Ζητούμενη Απάντηση)",
                    headers=["Τμήμα", "Δεδομένα (bytes)", "Total Length (bytes)", "MF", "Fragment Offset", "Offset (bytes)"],
                    rows=[
                        AnalysisRow(cells=["1", "1480", "1500 (1480 + 20)", "1", "0", "0"], highlight=True),
                        AnalysisRow(cells=["2", "1480", "1500 (1480 + 20)", "1", "185", "1480"], highlight=True),
                        AnalysisRow(cells=["3", "20", "40 (20 + 20)", "0", "370", "2960"], highlight=True),
                    ],
                    note="Έλεγχος: 1480 + 1480 + 20 = 2980 bytes δεδομένων — ακριβώς το αρχικό φορτίο· όλα τα offsets επί 8 (0, 185, 370).",
                ),
            ],
            answer="Τμήμα 1: 1500 B, MF 1, offset 0 · Τμήμα 2: 1500 B, MF 1, offset 185 · Τμήμα 3: 40 B, MF 0, offset 370 — όλα με ID 12345 και DF 0.",
            tips=[
                "Αν το δεδομένο φορτίο ανά τμήμα δεν ήταν πολλαπλάσιο του 8, θα στρογγυλοποιούσαμε προς τα κάτω στο πλησιέστερο πολλαπλάσιο.",
                "Το τελευταίο τμήμα δεν χρειάζεται πολλαπλάσιο του 8 — μόνο τα μη τελευταία.",
                "DF = 1 θα απέριπτε το πακέτο με ICMP Fragmentation Needed — εδώ DF = 0 οπότε προχωράμε σε κατάτμηση.",
            ],
        ),
        ExamQuestion(
            thema="Θέμα 2",
            thema_title="Κατάτμηση IP (Fragmentation) & Επανασύνθεση",
            sub_number="2β",
            title="Επανασύνθεση Τμημάτων A / B / C",
            question_type="computational",
            prompt="Λαμβάνετε τρία τμήματα IP: A: Total Length 1500, Header 20, MF 1, Offset 0 · B: Total Length 1500, Header 20, MF 1, Offset 185 · C: Total Length 540, Header 20, MF 0, Offset 370. Να βρεθεί το μέγεθος των αρχικών δεδομένων, το εύρος bytes κάθε τμήματος και να επαληθευθεί η ορθότητα της κατάτμησης.",
            given=[
                GivenParameter(label="Τμήμα A", value="Length 1500 · MF 1 · Offset 0", source="εκφώνηση Θέματος 2.2"),
                GivenParameter(label="Τμήμα B", value="Length 1500 · MF 1 · Offset 185", source="εκφώνηση Θέματος 2.2"),
                GivenParameter(label="Τμήμα C", value="Length 540 · MF 0 · Offset 370", source="εκφώνηση Θέματος 2.2"),
            ],
            steps=[
                CalculationStep(
                    label="Βήμα 1 — Αναγνώριση Τελευταίου Τμήματος",
                    description="Το τμήμα C έχει MF = 0, άρα είναι το τελευταίο· τα A και B με MF = 1 δηλώνουν ότι ακολουθούν κι άλλα. Η επανασύνθεση ξεκινά από το C.",
                ),
                CalculationStep(
                    label="Βήμα 2 — Μέγεθος Αρχικών Δεδομένων",
                    description="Το C τοποθετεί τα δεδομένα του στη θέση 370 × 8 = 2960 και μεταφέρει 540 − 20 = 520 bytes. Άρα το τελευταίο byte των αρχικών δεδομένων είναι στο 2960 + 520 − 1 = 3479, δηλαδή συνολικά 3480 bytes δεδομένων (αρχικό πακέτο 3480 + 20 = 3500 bytes).",
                    latex=r"\text{Δεδομένα} = 370 \times 8 + (540 - 20) = 2960 + 520 = 3480\,\text{bytes}",
                    result="Αρχικά δεδομένα: 3480 B · Αρχικό πακέτο: 3500 B",
                ),
                CalculationStep(
                    label="Βήμα 3 — Εύρη Bytes ανά Τμήμα",
                    description="Μετατρέπουμε κάθε offset σε byte-θέση (× 8) και προσθέτουμε το μέγεθος δεδομένων του τμήματος.",
                ),
                CalculationStep(
                    label="Βήμα 4 — Επαλήθευση Συνέχειας",
                    description="Τα εύρη πρέπει να καλύπτονται χωρίς κενά και επικαλύψεις: A τελειώνει στο 1479, B ξεκινά στο 1480· B τελειώνει στο 2959, C ξεκινά στο 2960· C τελειώνει στο 3479 = συνολικό μέγεθος − 1. Η κατάτμηση είναι ορθή.",
                    latex=r"[0,1479] \cup [1480,2959] \cup [2960,3479] = [0,3479]",
                ),
            ],
            answer_tables=[
                AnalysisTable(
                    title="Εύρη Bytes & Επαλήθευση",
                    headers=["Τμήμα", "Offset × 8 (θέση)", "Δεδομένα", "Εύρος Bytes", "MF"],
                    rows=[
                        AnalysisRow(cells=["A", "0 × 8 = 0", "1500 − 20 = 1480", "0 – 1479", "1"]),
                        AnalysisRow(cells=["B", "185 × 8 = 1480", "1500 − 20 = 1480", "1480 – 2959", "1"]),
                        AnalysisRow(cells=["C", "370 × 8 = 2960", "540 − 20 = 520", "2960 – 3479", "0"], highlight=True),
                    ],
                    note="Συνεχής κάλυψη 0-3479 χωρίς κενά: η κατάτμηση είναι έγκυρη και επανασυντίθεται σε πακέτο 3500 bytes (3480 δεδομένα + 20 επικεφαλίδα).",
                ),
            ],
            answer="Αρχικά δεδομένα 3480 bytes (πακέτο 3500 B)· εύρη: A [0-1479], B [1480-2959], C [2960-3479] — συνέχεια χωρίς κενά, κατάτμηση ορθή.",
            tips=[
                "Το κλειδί της επανασύνθεσης: τελευταίο τμήμα = MF 0· συνολικά δεδομένα = offset_τελευταίου × 8 + δεδομένα_τελευταίου.",
                "Η επανασύνθεση γίνεται ΜΟΝΟ στον τελικό προορισμό, όχι στους ενδιάμεσους δρομολογητές.",
            ],
        ),
        ExamQuestion(
            thema="Θέμα 3",
            thema_title="TTL & Ροή Πακέτου στο Δίκτυο",
            sub_number="3",
            title="Ιχνηλάτιση TTL σε Διαδρομή 3 Hops",
            question_type="computational",
            prompt="Ένα πακέτο ταξιδεύει μέσω της διαδρομής Πηγή (192.168.1.10) → Δρομολογητής A → Δρομολογητής B → Δρομολογητής C → Προορισμός (10.0.0.5) με αρχικό TTL 5. Περιγράψτε τι συμβαίνει σε κάθε άλμα, ποιο μήνυμα ICMP (εάν υπάρχει) δημιουργείται, και τι θα άλλαζε αν το αρχικό TTL ήταν 3.",
            given=[
                GivenParameter(label="Πηγή", value="192.168.1.10", source="εκφώνηση Θέματος 3"),
                GivenParameter(label="Διαδρομή", value="A → B → C (3 δρομολογητές)", source="εκφώνηση Θέματος 3"),
                GivenParameter(label="Προορισμός", value="10.0.0.5", source="εκφώνηση Θέματος 3"),
                GivenParameter(label="Αρχικό TTL", value="5", source="εκφώνηση Θέματος 3"),
            ],
            steps=[
                CalculationStep(
                    label="Βήμα 1 — Σενάριο με TTL = 5",
                    description="Στην πηγή δημιουργείται το πακέτο με TTL 5. Κάθε δρομολογητής μειώνει το TTL κατά 1 ΠΡΙΝ προωθήσει: ο A το παραδίδει με TTL 4, ο B με TTL 3, ο C με TTL 2 — και ο προορισμός το λαμβάνει με TTL 2. Καμία απόρριψη, κανένα ICMP.",
                ),
                CalculationStep(
                    label="Βήμα 2 — Σενάριο με TTL = 3",
                    description="Ο A μειώνει 3 → 2 και προωθεί· ο B μειώνει 2 → 1 και προωθεί· ο C μειώνει 1 → 0. Επειδή το TTL έφθασε το 0, ο C ΔΕΝ προωθεί: απορρίπτει το πακέτο.",
                    latex=r"\text{TTL}=3\!: \; A\!: 3{-}1{=}2,\; B\!: 2{-}1{=}1,\; C\!: 1{-}1{=}0 \Rightarrow \text{απόρριψη}",
                ),
                CalculationStep(
                    label="Βήμα 3 — Μήνυμα ICMP",
                    description="Μαζί με την απόρριψη, ο δρομολογητής C στέλνει στην πηγή 192.168.1.10 μήνυμα ICMP Time Exceeded: Τύπος 11, Κωδικός 0 (TTL έληξε σε μεταφορά). Έτσι η πηγή μαθαίνει ότι το πακέτο δεν έφτασε.",
                    result="ICMP Time Exceeded (Type 11, Code 0) από τον C προς 192.168.1.10",
                ),
                CalculationStep(
                    label="Βήμα 4 — Λειτουργική Σημασία",
                    description="Ο μηχανισμός αυτός αποτρέπει αιώνια κυκλοφορία σε βρόχους δρομολόγησης και αξιοποιείται από το traceroute, που στέλνει packets με TTL 1, 2, 3, ... για να αποκαλύψει τους διαδοχικούς δρομολογητές της διαδρομής.",
                ),
            ],
            answer_tables=[
                AnalysisTable(
                    title="Ιχνηλάτιση TTL ανά Hops (Τα Δύο Σενάρια)",
                    headers=["Κόμβος", "Εισερχόμενο TTL (αρχή 5)", "Εξερχόμενο TTL", "Ενέργεια", "Εισερχόμενο TTL (αρχή 3)"],
                    rows=[
                        AnalysisRow(cells=["Πηγή", "-", "5 (δημιουργία)", "Αποστολή προς A", "-"]),
                        AnalysisRow(cells=["Δρομολογητής A", "5", "4", "Έλεγχος TTL &gt; 0 → προώθηση σε B", "3 → 2"]),
                        AnalysisRow(cells=["Δρομολογητής B", "4", "3", "Έλεγχος TTL &gt; 0 → προώθηση σε C", "2 → 1"]),
                        AnalysisRow(cells=["Δρομολογητής C", "3", "2", "Έλεγχος TTL &gt; 0 → προώθηση στον προορισμό", "1 → 0: ΑΠΟΡΡΙΨΗ"], highlight=True),
                        AnalysisRow(cells=["Προορισμός 10.0.0.5", "2", "-", "Παράδοση επιτυχής", "Δεν λαμβάνεται ποτέ + ICMP Time Exceeded προς την πηγή"], highlight=True),
                    ],
                ),
            ],
            answer="Με TTL 5 το πακέτο παραδίδεται με TTL 2 (5 → 4 → 3 → 2 στα τρία hops). Με TTL 3 ο δρομολογητής C το μηδενίζει και το απορρίπτει, στέλνοντας ICMP Time Exceeded (Type 11, Code 0) στην πηγή 192.168.1.10.",
            tips=[
                "Ο δρομολογητής μειώνει ΠΡΙΝ ελέγξει: αν εισέλθει με TTL 1, εξέρχεται με 0 και απορρίπτεται.",
                "Ο τελικός προορισμός δεν απορρίπτει πακέτα λόγω TTL — μόνο οι ενδιάμεσοι δρομολογητές.",
            ],
        ),
        ExamQuestion(
            thema="Θέμα 4",
            thema_title="NAT & Ιδιωτική Διευθυνσιοδότηση",
            sub_number="4",
            title="Συμπλήρωση Πίνακα Μετάφρασης NAT",
            question_type="computational",
            prompt="Μια εταιρεία χρησιμοποιεί NAT με ιδιωτικό δίκτυο 192.168.1.0/24 και δημόσια IP 203.0.113.5. Ο δρομολογητής NAT μεταφράζει χρησιμοποιώντας αριθμούς θυρών. Συμπληρώστε τον πίνακα μετάφρασης (Inside Local / Inside Global / Outside Global) και εξηγήστε τη ροή της επιστρεφόμενης κίνησης.",
            given=[
                GivenParameter(label="Ιδιωτικό δίκτυο", value="192.168.1.0/24", source="εκφώνηση Θέματος 4"),
                GivenParameter(label="Inside Global (δημόσια)", value="203.0.113.5", source="εκφώνηση Θέματος 4"),
                GivenParameter(label="Σύνδεση 1", value="192.168.1.10:5000 → 8.8.8.8:53", source="πρώτη γραμμή πίνακα"),
                GivenParameter(label="Σύνδεση 2", value="192.168.1.15:5001 → 93.184.216.34:80", source="δεύτερη γραμμή πίνακα"),
                GivenParameter(label="Σύνδεση 3", value="Inside Global 203.0.113.5:1026 → 151.101.1.69:443", source="τρίτη γραμμή πίνακα"),
            ],
            steps=[
                CalculationStep(
                    label="Βήμα 1 — Οι Τρεις Τύποι Διευθύνσεων",
                    description="<strong>Inside Local</strong>: η ιδιωτική IP:θύρα του εσωτερικού σταθμού. <strong>Inside Global</strong>: η δημόσια IP:θύρα με την οποία φαίνεται η σύνδεση προς τα έξω. <strong>Outside Global</strong>: η IP:θύρα του εξωτερικού διακομιστή προορισμού.",
                ),
                CalculationStep(
                    label="Βήμα 2 — Ανάθεση Μοναδικών Global Θυρών",
                    description="Ο NAT χρειάζεται μια μοναδική θύρα ανά ενεργή σύνδεση: εκχωρεί διαδοχικά 1024, 1025, 1026 στη δημόσια διεύθυνση 203.0.113.5. Έτσι πολλαπλές εσωτερικές συνδέσεις μοιράζονται μία δημόσια IP χωρίς σύγχυση.",
                    result="192.168.1.10:5000 → 203.0.113.5:1024 · 192.168.1.15:5001 → 203.0.113.5:1025",
                ),
                CalculationStep(
                    label="Βήμα 3 — Η Τρίτη Γραμμή (Αντίστροφη Ανάγνωση)",
                    description="Για τη σύνδεση με Inside Global 203.0.113.5:1026 προς 151.101.1.69:443, το Inside Local ΔΕΝ προσδιορίζεται από τα δεδομένα: χρειάζεται ο πίνακας του NAT (ποιος εσωτερικός σταθμός πήρε τη θύρα 1026). Η απάντηση είναι «απροσδιόριστη χωρίς πρόσθετες πληροφορίες».",
                    result="Inside Local = άγνωστο χωρίς τον πίνακα NAT (κάποιος 192.168.1.x με θύρα yyyy)",
                ),
                CalculationStep(
                    label="Βήμα 4 — Επιστρεφόμενη Κίνηση",
                    description="Όταν ο 8.8.8.8 απαντήσει προς 203.0.113.5:1024, ο NAT αναζητά τη θύρα 1024 στον πίνακά του, βρίσκει την αντιστοίχιση με 192.168.1.10:5000 και προωθεί το πακέτο στον εσωτερικό σταθμό — αυτός δεν γνωρίζει ποτέ τη μετάφραση.",
                ),
                CalculationStep(
                    label="Βήμα 5 — Γιατί NAT",
                    description="Οι ιδιωτικές διευθύνσεις RFC 1918 δεν δρομολογούνται στο δημόσιο διαδίκτυο: το NAT επιτρέπει σε χιλιάδες εσωτερικούς σταθμούς να μοιράζονται λίγες δημόσιες IP (αντιμετώπιση εξάντλησης IPv4) και κρύβει την εσωτερική τοπολογία (βασική ασφάλεια).",
                ),
            ],
            answer_tables=[
                AnalysisTable(
                    title="Συμπληρωμένος Πίνακας Μετάφρασης NAT",
                    headers=["Inside Local", "Inside Global", "Outside Global"],
                    rows=[
                        AnalysisRow(cells=["192.168.1.10:5000", "203.0.113.5:1024", "8.8.8.8:53"], highlight=True),
                        AnalysisRow(cells=["192.168.1.15:5001", "203.0.113.5:1025", "93.184.216.34:80"], highlight=True),
                        AnalysisRow(cells=["Απροσδιόριστο (192.168.1.x:yyyy) — χρειάζεται ο πίνακας NAT", "203.0.113.5:1026", "151.101.1.69:443"], highlight=True),
                    ],
                    note="Κάθε γραμμή = μία ενεργή σύνδεση· ο πίνακας διατηρείται στον δρομολογητή NAT για τη δρομολόγηση των απαντήσεων.",
                ),
            ],
            answer="1024 / 1025 στις δύο πρώτες γραμμές· το Inside Local της τρίτης είναι απροσδιόριστο χωρίς τον πίνακα NAT. Οι επιστρεφόμενες απαντήσεις μεταφράζονται αντίστροφα (π.χ. 203.0.113.5:1024 → 192.168.1.10:5000).",
            tips=[
                "Οι θύρες NAT ξεκινούν συνήθως από το 1024 (πάνω από τα well-known 0-1023).",
                "Το NAT αλλάζει IP/θύρα στην επικεφαλίδα και επανυπολογίζει τα checksums (IP και TCP/UDP).",
            ],
        ),
    ]

    analysis_tables = [
        AnalysisTable(
            title="Αναφορά: Πεδία & Τιμές-Κλειδιά της Επικεφαλίδας IPv4",
            headers=["Πεδίο", "Τιμές Εξετάσεων", "Ρόλος"],
            rows=[
                AnalysisRow(cells=["Version / IHL", "4 / ελάχιστο 5 (20 bytes)", "Έκδοση και μήκος σε λέξεις των 32 bits"]),
                AnalysisRow(cells=["Total Length", "bytes, άθροισμα header + data", "Μέγιστο 65.535 bytes"]),
                AnalysisRow(cells=["Identification", "κοινό σε όλα τα τμήματα", "Ταυτότητα αρχικού datagram"]),
                AnalysisRow(cells=["Flags", "DF = 1 → απαγόρευση κατάτμησης· MF = 1 → ακολουθούν άλλα", "Έλεγχος κατάτμησης"], highlight=True),
                AnalysisRow(cells=["Fragment Offset", "θέση / 8", "Μονάδα μέτρησης 8 bytes"]),
                AnalysisRow(cells=["TTL", "μειώνεται 1/hop· 0 → απόρριψη", "ICMP Time Exceeded (Type 11)"]),
                AnalysisRow(cells=["Protocol", "6 TCP · 17 UDP · 1 ICMP · 2 IGMP", "Demultiplexing προς το ανώτερο επίπεδο"], highlight=True),
                AnalysisRow(cells=["Header Checksum", "συμπλήρωμα ως προς 1 του αθροίσματος", "Επικεφαλίδα μόνο, ανά hop"]),
            ],
        ),
    ]

    diagram_title = "Διαδρομή Κατάτμησης: Datagram 3000 B → MTU 1500 → 3 Τμήματα"
    diagram_nodes = [
        DiagramNode(id="src", label="Πηγή (Host)", x=30, y=60, w=230, details=["Αποστολή datagram", "Total Length: 3000 B", "Header: 20 B · ID 12345", "DF = 0"]),
        DiagramNode(id="rtr", label="Δρομολογητής (MTU 1500)", x=430, y=60, w=280, details=["Δεδομένα: 2980 B", "Ανά τμήμα: 1480 B", "Δημιουργεί 3 τμήματα"], highlight=True),
        DiagramNode(id="dst", label="Προορισμός (Host)", x=940, y=60, w=230, details=["Επανασύνθεση", "Από offsets 0/185/370", "Δεδομένα: 2980 B"]),
        DiagramNode(id="f1", label="Τμήμα 1 (MF = 1)", x=60, y=300, w=280, details=["Total Length: 1500 B", "Δεδομένα: 1480 B", "Fragment Offset: 0"]),
        DiagramNode(id="f2", label="Τμήμα 2 (MF = 1)", x=440, y=300, w=280, details=["Total Length: 1500 B", "Δεδομένα: 1480 B", "Fragment Offset: 185 (×8 = 1480)"]),
        DiagramNode(id="f3", label="Τμήμα 3 (MF = 0)", x=820, y=300, w=280, details=["Total Length: 40 B", "Δεδομένα: 20 B", "Fragment Offset: 370 (×8 = 2960)"]),
    ]
    diagram_edges = [
        DiagramEdge(path="M 260,100 L 430,100", label="Datagram 3000 B", lx=345, ly=78),
        DiagramEdge(path="M 710,100 L 940,100", label="1500 + 1500 + 40", lx=825, ly=78),
        DiagramEdge(path="M 570,140 C 570,230 200,230 200,300", label="F1", lx=320, ly=235, dashed=True),
        DiagramEdge(path="M 570,140 C 570,230 580,230 580,300", label="F2", lx=565, ly=235, dashed=True),
        DiagramEdge(path="M 570,140 C 570,230 960,230 960,300", label="F3", lx=800, ly=235, dashed=True),
    ]
    diagram_note = "Ο δρομολογητής τεμαχίζει τα 2980 bytes δεδομένων σε 1480 + 1480 + 20· η επανασύνθεση γίνεται μόνον στον τελικό προορισμό με βάση τα offsets."

    justifications = [
        DesignJustification(
            title="1. Πολλαπλάσια του 8 στα Τμήματα",
            color_class="text-blue-500",
            description="Το Fragment Offset μετρά σε μονάδες των 8 bytes, οπότε κάθε μη-τελευταίο τμήμα φέρει δεδομένα πολλαπλάσια του 8 — γι' αυτό το 1480 (και όχι π.χ. 1483) είναι το μέγιστο ωφέλιμο φορτίο.",
        ),
        DesignJustification(
            title="2. Κοινό Identification σε Όλα τα Τμήματα",
            color_class="text-amber-500",
            description="Όλα τα τμήματα κρατούν το ID 12345: μόνο έτσι ο προορισμός γνωρίζει ότι ανήκουν στο ίδιο αρχικό datagram και μπορεί να τα επανασυνθέσει.",
        ),
        DesignJustification(
            title="3. Επανασύνθεση μόνο στον Προορισμό",
            color_class="text-emerald-500",
            description="Οι ενδιάμεσοι δρομολογητές προωρούν τμήματα ως ανεξάρτητα packets· μόνο ο τελικός hosts συγκεντρώνει (buffer εκτός σειράς) και συναρμολογεί με βάση MF/offset.",
        ),
        DesignJustification(
            title="4. NAT & Θύρες αντί για Διευθύνσεις",
            color_class="text-purple-500",
            description="Με μία δημόσια IP για όλο το δίκτυο, η διαφοροποίηση των συνδέσεων γίνεται με μοναδικές θύρες (1024, 1025, 1026) — ο πίνακας μετάφρασης είναι η μοναδική πηγή για την αντίστροφη ευρεση.",
        ),
    ]

    solution_code = """# Θέμα 2: Υπολογισμός & επαλήθευση της κατάτμησης 3000 B / MTU 1500
HEADER = 20

def fragment(total_length: int, mtu: int) -> list[tuple[int, int, int, int]]:
    # Returns (total_len, data_len, mf, offset_units) for every fragment.
    data = total_length - HEADER
    chunk = (mtu - HEADER) // 8 * 8   # μεγαλύτερο πολλαπλάσιο του 8
    frags, position = [], 0
    while position < data:
        take = min(chunk, data - position)
        mf = 1 if position + take < data else 0
        frags.append((take + HEADER, take, mf, position // 8))
        position += take
    return frags

for i, (length, data, mf, offset) in enumerate(fragment(3000, 1500), start=1):
    print(f"Τμήμα {i}: Total {length} B | Δεδομένα {data} B | "
          f"MF {mf} | Offset {offset} (= byte {offset * 8})")

# Θέμα 2.2: Επανασύνθεση των A/B/C
last_offset_bytes = 370 * 8
last_data = 540 - HEADER
original_data = last_offset_bytes + last_data
print(f"Αρχικά δεδομένα: {original_data} B | Αρχικό πακέτο: "
      f"{original_data + HEADER} B")
"""

    return Scenario(
        id="synth_exam_2",
        title="Συνθετικό Θέμα 2",
        subtitle="Επικεφαλίδα IPv4 & ICMP/ARP · Κατάτμηση & Επανασύνθεση · Ιχνηλάτιση TTL · Πίνακες NAT",
        course_tag="NETWORKING (Συνθετική Εξέταση 2)",
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
