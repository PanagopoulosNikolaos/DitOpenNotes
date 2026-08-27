"""Municipal Library Network case study scenario module.

Contains the complete parsed and modeled ER analysis for the Municipal Library Network
(Branches, Staff/Librarians, Book Titles, Authors, Physical Copies, Members, Loans & Reservations),
including full attribute breakdowns, relationship cardinalities, keys analysis, Crow's Foot
ER diagram layout, relational schema mapping, and SQL DDL.
"""

from models.scenario import (
    Scenario,
    Paragraph,
    TextSegment,
    Entity,
    Attribute,
    RelationshipAttribute,
    KeyAnalysisRow,
    Relationship,
    ERTable,
    ERTableAttr,
    EREdge,
    RelationalJustification,
)


def createLibraryManagementScenario() -> Scenario:
    """Constructs and returns the Municipal Library Network database scenario.

    Returns:
        Scenario: Fully populated scenario instance.
    """
    # 1. Text Paragraphs with Interactive Segments
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Ένας μητροπολιτικός δήμος αναπτύσσει ένα ενιαίο πληροφοριακό σύστημα βάσεων δεδομένων για το δίκτυο των δημοτικών βιβλιοθηκών του, με σκοπό τη διαχείριση των "),
                TextSegment(
                    text="παραρτημάτων",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Strong Entity): Αυτοτελές φυσικό παράρτημα δημοτικής βιβλιοθήκης με μοναδικό Branch ID.",
                ),
                TextSegment(text=", των "),
                TextSegment(
                    text="καταλόγων βιβλιογραφικών τίτλων",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Strong Entity): Βιβλιογραφικός τίτλος/έργο με μοναδικό διεθνή αριθμό ISBN.",
                ),
                TextSegment(text=", των "),
                TextSegment(
                    text="φυσικών αντιτύπων",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΑΣΘΕΝΗΣ ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-weak",
                    tooltip="Ασθενής Οντότητα (Weak Entity): Φυσικό αντίτυπο βιβλίου που προσδιορίζεται σε συνδυασμό με το ISBN του τίτλου.",
                ),
                TextSegment(text=", των "),
                TextSegment(
                    text="μελών/αναγνωστών",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Strong Entity): Εγγεγραμμένο μέλος βιβλιοθήκης με μοναδικό Αριθμό Κάρτας Μέλους.",
                ),
                TextSegment(text=", των "),
                TextSegment(
                    text="δανεισμών",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ (ΣΥΝΑΛΛΑΓΗ)",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή/Συσχετιστική Οντότητα (Transaction Entity): Πράξη δανεισμού φυσικού αντιτύπου από μέλος.",
                ),
                TextSegment(text=" και των "),
                TextSegment(
                    text="κρατήσεων",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ (ΟΥΡΑ)",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή/Συσχετιστική Οντότητα (Queue Entity): Αίτημα κράτησης τίτλου από μέλος σε συγκεκριμένο παράρτημα.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color=None,
        ),
        Paragraph(
            segments=[
                TextSegment(text="1. <strong>Παραρτήματα Βιβλιοθήκης (Branches):</strong> Κάθε παράρτημα χαρακτηρίζεται από έναν "),
                TextSegment(
                    text="μοναδικό κωδικό παραρτήματος (Branch ID)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Μοναδικός αριθμητικός ή αλφαριθμητικός κωδικός παραρτήματος.",
                ),
                TextSegment(text=", μια "),
                TextSegment(
                    text="μοναδική ονομασία (π.χ. 'Κεντρική Δημοτική Βιβλιοθήκη', 'Παράρτημα Άνω Πόλης')",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Υποψήφιο Κλειδί (Candidate Key): Μοναδική επίσημη ονομασία παραρτήματος εντός του δήμου.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="διεύθυνση (οδός, αριθμός, ΤΚ, συνοικία)",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΣΥΝΘΕΤΟ",
                    badge_class="badge-attr-composite",
                    tooltip="Σύνθετο Γνώρισμα: Αποτελείται από επιμέρους γνωρίσματα οδός, αριθμός, ταχυδρομικός κώδικας και συνοικία.",
                ),
                TextSegment(text=", "),
                TextSegment(text="τηλέφωνο", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και "),
                TextSegment(text="χωρητικότητα αναγνωστών", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=". Κάθε παράρτημα έχει ένα καθορισμένο "),
                TextSegment(
                    text="εβδομαδιαίο ωράριο λειτουργίας (πολλαπλές ημέρες/ώρες λειτουργίας)",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΠΛΕΙΟΤΙΜΟ",
                    badge_class="badge-attr-multi",
                    tooltip="Πλειότιμο Γνώρισμα: Εξάγεται στον σχεσιακό πίνακα ORARIO_LEITOURGIAS.",
                ),
                TextSegment(text=". Κάθε παράρτημα "),
                TextSegment(
                    text="διευθύνεται από έναν έμπειρο Βιβλιοθηκονόμο-Διευθυντή",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ 1:1",
                    badge_class="badge-rel-11",
                    tooltip="Συσχέτιση 1:1 (ΔΙΕΥΘΥΝΕΙ): Ολική συμμετοχή για Παράρτημα, μερική για Βιβλιοθηκονόμο.",
                ),
                TextSegment(text=", για τον οποίο καταγράφεται η "),
                TextSegment(
                    text="ημερομηνία ανάληψης καθηκόντων",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ ΣΧΕΣΗΣ",
                    badge_class="badge-attr-composite",
                    tooltip="Γνώρισμα Συσχέτισης: Αποθηκεύεται στον σχεσιακό πίνακα PARARTIMA.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-blue-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="2. <strong>Βιβλιογραφικοί Τίτλοι & Συγγραφείς:</strong> Για κάθε βιβλιογραφικό τίτλο καταγράφονται: ο "),
                TextSegment(
                    text="μοναδικός διεθνής αριθμός ISBN (International Standard Book Number)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Παγκόσμιος μοναδικός αριθμός ISBN.",
                ),
                TextSegment(text=", ο "),
                TextSegment(text="τίτλος", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", ο "),
                TextSegment(text="εκδοτικός οίκος", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", το "),
                TextSegment(text="έτος έκδοσης", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(text="κατηγορία/θεματική (π.χ. 'Επιστήμη Υπολογιστών', 'Ιστορία')", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και ο "),
                TextSegment(text="αριθμός σελίδων", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=". Ένα βιβλίο μπορεί να έχει γραφτεί από "),
                TextSegment(
                    text="έναν ή περισσότερους συγγραφείς (Συσχέτιση N:M)",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ N:M",
                    badge_class="badge-rel-nm",
                    tooltip="Συσχέτιση N:M (ΣΥΓΓΡΑΦΗ): Ένα βιβλίο γράφεται από πολλούς συγγραφείς και ένας συγγραφέας γράφει πολλά βιβλία.",
                ),
                TextSegment(text=". Για κάθε "),
                TextSegment(
                    text="συγγραφέα",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Strong Entity): Φυσικό πρόσωπο συγγραφέα με μοναδικό κωδικό.",
                ),
                TextSegment(text=" καταγράφονται: ο "),
                TextSegment(
                    text="κωδικός συγγραφέα",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Μοναδικός αναγνωριστικός κωδικός συγγραφέα.",
                ),
                TextSegment(text=", το "),
                TextSegment(text="ονοματεπώνυμο", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(text="εθνικότητα", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και το "),
                TextSegment(text="έτος γέννησης", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text="."),
            ],
            accent_border_color="border-amber-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="3. <strong>Φυσικά Αντίτυπα (Physical Copies):</strong> Κάθε παράρτημα διαθέτει ένα ή περισσότερα φυσικά αντίτυπα διαφόρων βιβλίων. Κάθε αντίτυπο ταυτοποιείται από τον "),
                TextSegment(
                    text="μοναδικό γραμμωτό κώδικα (Barcode) ή αύξοντα αριθμό αντιτύπου εντός του συγκεκριμένου ISBN",
                    is_highlight=True,
                    category="key",
                    tag_label="ΜΕΡΙΚΟ ΚΛΕΙΔΙ",
                    badge_class="badge-key-partial",
                    tooltip="Μερικό Κλειδί (Partial Key): Αύξων αριθμός αντιτύπου (copy_number) που σε συνδυασμό με το ISBN συνθέτει το PK.",
                ),
                TextSegment(text=". Για κάθε αντίτυπο καταγράφονται: η "),
                TextSegment(text="φυσική κατάσταση (π.χ. 'Άριστη', 'Καλή', 'Φθαρμένο', 'Υπό Επισκευή')", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(text="ένδειξη διαθεσιμότητας ('Διαθέσιμο', 'Δανεισμένο', 'Δεσμευμένο')", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", ο "),
                TextSegment(text="αριθμός ραφιού/θέσης στο αναγνωστήριο", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και το "),
                TextSegment(
                    text="παράρτημα στο οποίο ανήκει μόνιμα",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ 1:N",
                    badge_class="badge-rel-1n",
                    tooltip="Συσχέτιση 1:N (ΣΤΕΓΑΖΕΙ_ΑΝΤΙΤΥΠΟ): Κάθε αντίτυπο ανήκει μόνιμα σε ένα συγκεκριμένο παράρτημα.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-red-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="4. <strong>Μέλη / Αναγνώστες (Library Members):</strong> Για κάθε εγγεγραμμένο μέλος καταγράφονται: ο "),
                TextSegment(
                    text="μοναδικός Αριθμός Κάρτας Μέλους",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Μοναδικός αριθμός κάρτας αναγνώστη.",
                ),
                TextSegment(text=", ο "),
                TextSegment(
                    text="Αριθμός Δελτίου Ταυτότητας (ΑΔΤ)",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Υποψήφιο Κλειδί (Candidate Key): Μοναδικός κρατικός αριθμός ταυτότητας μέλους.",
                ),
                TextSegment(text=", το "),
                TextSegment(text="όνομα", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", το "),
                TextSegment(text="επώνυμο", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(text="ημερομηνία γέννησης", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(
                    text="διεύθυνση κατοικίας (οδός, αριθμός, ΤΚ, πόλη)",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΣΥΝΘΕΤΟ",
                    badge_class="badge-attr-composite",
                    tooltip="Σύνθετο Γνώρισμα: Αναλύεται σε οδό, αριθμό, ΤΚ και πόλη κατοικίας.",
                ),
                TextSegment(text=", το "),
                TextSegment(
                    text="email",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Υποψήφιο Κλειδί (Candidate Key): Μοναδική διεύθυνση ηλεκτρονικού ταχυδρομείου.",
                ),
                TextSegment(text=", η "),
                TextSegment(text="ημερομηνία εγγραφής", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και η "),
                TextSegment(text="κατάσταση μέλους ('Ενεργό', 'Σε Αναστολή')", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=". Ένα μέλος μπορεί να δηλώσει "),
                TextSegment(
                    text="πολλαπλά τηλέφωνα επικοινωνίας",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΠΛΕΙΟΤΙΜΟ",
                    badge_class="badge-attr-multi",
                    tooltip="Πλειότιμο Γνώρισμα: Εξάγεται στον σχεσιακό πίνακα TILEFONA_MELOUS.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-purple-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="5. <strong>Δανεισμοί Αντιτύπων (Loans):</strong> Τα μέλη μπορούν να δανείζονται διαθέσιμα αντίτυπα βιβλίων. Για κάθε δανεισμό καταγράφονται: ένας "),
                TextSegment(
                    text="μοναδικός κωδικός δανεισμού (Loan ID)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Μοναδικός κωδικός συναλλαγής δανεισμού.",
                ),
                TextSegment(text=", η "),
                TextSegment(text="ημερομηνία δανεισμού", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(text="προκαθορισμένη ημερομηνία υποχρεωτικής επιστροφής", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(text="πραγματική ημερομηνία επιστροφής (εφόσον επεστράφη)", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και το "),
                TextSegment(
                    text="τυχόν χρηματικό πρόστιμο καθυστέρησης (που υπολογίζεται βάσει των ημερών καθυστέρησης)",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΠΑΡΑΓΩΓΟ",
                    badge_class="badge-attr-derived",
                    tooltip="Παράγωγο Γνώρισμα (Derived Attribute): Υπολογίζεται δυναμικά από τη διαφορά πραγματικής και προκαθορισμένης ημερομηνίας.",
                ),
                TextSegment(text=". Ένα αντίτυπο "),
                TextSegment(
                    text="μπορεί να δανειστεί μόνο σε ένα μέλος κάθε φορά",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΠΕΡΙΟΡΙΣΜΟΣ 1:1",
                    badge_class="badge-rel-11",
                    tooltip="Επιχειρησιακός Κανόνας: Ένα φυσικό αντίτυπο μπορεί να έχει το πολύ έναν ενεργό δανεισμό ανά χρονική στιγμή.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-emerald-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="6. <strong>Κρατήσεις Τίτλων (Reservations):</strong> Όταν όλα τα αντίτυπα ενός επιθυμητού τίτλου (ISBN) είναι δανεισμένα, ένα μέλος μπορεί να υποβάλει "),
                TextSegment(
                    text="αίτημα κράτησης για τον συγκεκριμένο τίτλο σε ένα συγκεκριμένο παράρτημα",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ N:M / ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-rel-nm",
                    tooltip="Συσχετιστική Οντότητα (ΚΡΑΤΗΣΗ): Συνδέει Μέλος, Βιβλιογραφικό Τίτλο και Παράρτημα παραλαβής.",
                ),
                TextSegment(text=". Για κάθε κράτηση καταγράφονται: ο "),
                TextSegment(
                    text="μοναδικός κωδικός κράτησης (Reservation ID)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Μοναδικός κωδικός αιτήματος κράτησης.",
                ),
                TextSegment(text=", η "),
                TextSegment(text="ημερομηνία και ώρα υποβολής", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(text="σειρά προτεραιότητας στην ουρά αναμονής", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και η "),
                TextSegment(text="κατάσταση του αιτήματος ('Σε αναμονή', 'Ειδοποιήθηκε το μέλος', 'Ολοκληρώθηκε', 'Ακυρώθηκε')", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text="."),
            ],
            accent_border_color="border-cyan-500",
        ),
    ]

    # 2. Complete Entity List with Detailed Attributes
    entities = [
        Entity(
            name="ΠΑΡΑΡΤΗΜΑ_ΒΙΒΛΙΟΘΗΚΗΣ",
            entity_type="Ισχυρή Οντότητα",
            is_weak=False,
            owner_entity=None,
            justification="Αυτοτελές φυσικό κτίριο/παράρτημα δημοτικής βιβλιοθήκης με δική του αυτόνομη υπόσταση και μοναδικό Branch ID.",
            attributes=[
                Attribute("branch_id", "Απλό / Μονότιμο", is_pk=True, notes="Μοναδικός κωδικός παραρτήματος."),
                Attribute("onomasia", "Απλό / Μονότιμο", is_candidate=True, notes="Μοναδική επίσημη ονομασία παραρτήματος."),
                Attribute(
                    "dieythynsi",
                    "Σύνθετο",
                    components=["odos", "arithmos", "tk", "synoikia"],
                    notes="Πλήρης ταχυδρομική διεύθυνση παραρτήματος.",
                ),
                Attribute("tilefono", "Απλό / Μονότιμο", notes="Κεντρικό τηλέφωνο επικοινωνίας."),
                Attribute("xoritikotita", "Απλό / Μονότιμο", notes="Μέγιστη χωρητικότητα καθήμενων αναγνωστών."),
                Attribute("orario_leitourgias", "Πλειότιμο", notes="Πολλαπλές ημέρες και ώρες λειτουργίας (εξάγεται σε ξεχωριστό πίνακα)."),
            ],
        ),
        Entity(
            name="ΒΙΒΛΙΟΘΗΚΟΝΟΜΟΣ",
            entity_type="Ισχυρή Οντότητα",
            is_weak=False,
            owner_entity=None,
            justification="Φυσικό πρόσωπο υπαλλήλου/βιβλιοθηκονόμου που απασχολείται σε παράρτημα και μπορεί να διευθύνει αυτό.",
            attributes=[
                Attribute("staff_id", "Απλό / Μονότιμο", is_pk=True, notes="Μοναδικός αριθμός μητρώου υπαλλήλου."),
                Attribute("adt", "Απλό / Μονότιμο", is_candidate=True, notes="Αριθμός Δελτίου Αστυνομικής Ταυτότητας."),
                Attribute("onoma", "Απλό / Μονότιμο", notes="Όνομα υπαλλήλου."),
                Attribute("eponymo", "Απλό / Μονότιμο", notes="Επώνυμο υπαλλήλου."),
                Attribute("eidikotita", "Απλό / Μονότιμο", notes="Επιστημονική/τεχνική ειδικότητα (π.χ. 'Αρχειονόμος', 'Βιβλιοθηκονόμος')."),
                Attribute("tilefono", "Απλό / Μονότιμο", notes="Τηλέφωνο επικοινωνίας υπαλλήλου."),
            ],
        ),
        Entity(
            name="ΒΙΒΛΙΟΓΡΑΦΙΚΟΣ_ΤΙΤΛΟΣ",
            entity_type="Ισχυρή Οντότητα",
            is_weak=False,
            owner_entity=None,
            justification="Αφηρημένο πνευματικό έργο/βιβλίο που ταυτοποιείται παγκοσμίως από το διεθνές πρότυπο ISBN.",
            attributes=[
                Attribute("isbn", "Απλό / Μονότιμο", is_pk=True, notes="Διεθνής μοναδικός αριθμός βιβλίου (ISBN-13)."),
                Attribute("titlos", "Απλό / Μονότιμο", notes="Πλήρης τίτλος του βιβλίου."),
                Attribute("ekdotikos_oikos", "Απλό / Μονότιμο", notes="Εκδοτικός οίκος έκδοσης."),
                Attribute("etos_ekdosis", "Απλό / Μονότιμο", notes="Έτος κυκλοφορίας της έκδοσης."),
                Attribute("katigoria", "Απλό / Μονότιμο", notes="Θεματική ταξινόμηση (π.χ. 'Πληροφορική', 'Ιστορία')."),
                Attribute("arithmos_selidon", "Απλό / Μονότιμο", notes="Συνολικός αριθμός σελίδων τόμου."),
            ],
        ),
        Entity(
            name="ΣΥΓΓΡΑΦΕΑΣ",
            entity_type="Ισχυρή Οντότητα",
            is_weak=False,
            owner_entity=None,
            justification="Φυσικό πρόσωπο δημιουργού/συγγραφέα με αυτόνομη οντολογική υπόσταση.",
            attributes=[
                Attribute("author_id", "Απλό / Μονότιμο", is_pk=True, notes="Μοναδικός κωδικός συγγραφέα."),
                Attribute("onomateponymo", "Απλό / Μονότιμο", notes="Πλήρες ονοματεπώνυμο συγγραφέα."),
                Attribute("ethnikotita", "Απλό / Μονότιμο", notes="Χώρα καταγωγής/εθνικότητα."),
                Attribute("etos_gennisis", "Απλό / Μονότιμο", notes="Έτος γέννησης συγγραφέα."),
            ],
        ),
        Entity(
            name="ΑΝΤΙΤΥΠΟ",
            entity_type="Ασθενής Οντότητα",
            is_weak=True,
            owner_entity="ΒΙΒΛΙΟΓΡΑΦΙΚΟΣ_ΤΙΤΛΟΣ",
            justification="Φυσικό υλικό αντίγραφο βιβλίου. Ταυτοποιείται από τον αριθμό αντιτύπου σε συνδυασμό με το ISBN του αντίστοιχου τίτλου.",
            attributes=[
                Attribute("copy_number", "Απλό / Μονότιμο", is_partial=True, notes="Μερικό κλειδί (αύξων αριθμός αντιτύπου εντός του ISBN)."),
                Attribute("barcode", "Απλό / Μονότιμο", is_candidate=True, notes="Μοναδικός γραμμωτός κώδικας ιχνηλάτησης."),
                Attribute("katastasi_fysiki", "Απλό / Μονότιμο", notes="'Άριστη', 'Καλή', 'Φθαρμένο', 'Υπό Επισκευή'."),
                Attribute("diathesimotita", "Απλό / Μονότιμο", notes="'Διαθέσιμο', 'Δανεισμένο', 'Δεσμευμένο'."),
                Attribute("thesi_rafi", "Απλό / Μονότιμο", notes="Κωδικός ραφιού/θέσης στο αναγνωστήριο."),
            ],
        ),
        Entity(
            name="ΜΕΛΟΣ",
            entity_type="Ισχυρή Οντότητα",
            is_weak=False,
            owner_entity=None,
            justification="Εγγεγραμμένος πολίτης/αναγνώστης με δικαίωμα δανεισμού και κράτησης υλικού.",
            attributes=[
                Attribute("card_number", "Απλό / Μονότιμο", is_pk=True, notes="Μοναδικός αριθμός κάρτας μέλους."),
                Attribute("adt", "Απλό / Μονότιμο", is_candidate=True, notes="Αριθμός Δελτίου Ταυτότητας μέλους."),
                Attribute("onoma", "Απλό / Μονότιμο", notes="Όνομα μέλους."),
                Attribute("eponymo", "Απλό / Μονότιμο", notes="Επώνυμο μέλους."),
                Attribute("hmer_gennisis", "Απλό / Μονότιμο", notes="Ημερομηνία γέννησης μέλους."),
                Attribute(
                    "dieythynsi_katoikias",
                    "Σύνθετο",
                    components=["odos", "arithmos", "tk", "poli"],
                    notes="Πλήρης διεύθυνση μόνιμης κατοικίας μέλους.",
                ),
                Attribute("email", "Απλό / Μονότιμο", is_candidate=True, notes="Μοναδική διεύθυνση ηλεκτρονικού ταχυδρομείου."),
                Attribute("hmer_eggrafis", "Απλό / Μονότιμο", notes="Ημερομηνία αρχικής εγγραφής στη βιβλιοθήκη."),
                Attribute("katastasi_melous", "Απλό / Μονότιμο", notes="'Ενεργό', 'Σε Αναστολή'."),
                Attribute("tilefona", "Πλειότιμο", notes="Πολλαπλά τηλέφωνα επικοινωνίας (εξάγεται σε ξεχωριστό πίνακα)."),
            ],
        ),
        Entity(
            name="ΔΑΝΕΙΣΜΟΣ",
            entity_type="Ισχυρή Οντότητα",
            is_weak=False,
            owner_entity=None,
            justification="Αυτοτελής πράξη/συναλλαγή δανεισμού φυσικού αντιτύπου από μέλος για ορισμένη χρονική διάρκεια.",
            attributes=[
                Attribute("loan_id", "Απλό / Μονότιμο", is_pk=True, notes="Μοναδικός κωδικός πράξης δανεισμού."),
                Attribute("hmer_daneismou", "Απλό / Μονότιμο", notes="Ημερομηνία παραλαβής του αντιτύπου."),
                Attribute("hmer_epistrofis_prokathorismeni", "Απλό / Μονότιμο", notes="Υποχρεωτική ημερομηνία επιστροφής."),
                Attribute("hmer_epistrofis_pragmatiki", "Απλό / Μονότιμο", notes="Πραγματική ημερομηνία επιστροφής (NULL αν εκκρεμεί)."),
                Attribute("prostimo", "Παράγωγο", notes="Υπολογιζόμενο πρόστιμο βάσει ημερών καθυστέρησης."),
            ],
        ),
        Entity(
            name="ΚΡΑΤΗΣΗ",
            entity_type="Ισχυρή Οντότητα",
            is_weak=False,
            owner_entity=None,
            justification="Αίτημα κράτησης τίτλου στην ουρά αναμονής όταν όλα τα αντίτυπα είναι δανεισμένα.",
            attributes=[
                Attribute("reservation_id", "Απλό / Μονότιμο", is_pk=True, notes="Μοναδικός κωδικός αιτήματος κράτησης."),
                Attribute("hmer_ypovolis", "Απλό / Μονότιμο", notes="Ημερομηνία και ώρα καταχώρισης του αιτήματος."),
                Attribute("seira_proteraiotitas", "Απλό / Μονότιμο", notes="Αριθμός προτεραιότητας στην ουρά αναμονής."),
                Attribute("katastasi_aitimatos", "Απλό / Μονότιμο", notes="'Σε αναμονή', 'Ειδοποιήθηκε το μέλος', 'Ολοκληρώθηκε', 'Ακυρώθηκε'."),
            ],
        ),
    ]

    # 3. Relationship Attributes
    relationship_attributes = [
        RelationshipAttribute(
            name="hmer_analipsis",
            relationship_name="ΔΙΕΥΘΥΝΕΙ (ΠΑΡΑΡΤΗΜΑ - ΒΙΒΛΙΟΘΗΚΟΝΟΜΟΣ)",
            justification="Ημερομηνία έναρξης άσκησης καθηκόντων διευθυντή παραρτήματος.",
        ),
        RelationshipAttribute(
            name="seira_syggrafea, rolos_symvolis",
            relationship_name="ΣΥΓΓΡΑΦΗ (ΣΥΓΓΡΑΦΕΑΣ - ΒΙΒΛΙΟΓΡΑΦΙΚΟΣ_ΤΙΤΛΟΣ)",
            justification="Σειρά εμφάνισης των συγγραφέων (π.χ. 1ος συγγραφέας, επιμελητής).",
        ),
    ]

    # 4. Keys Analysis Table
    keys_analysis = [
        KeyAnalysisRow(
            entity_name="ΠΑΡΑΡΤΗΜΑ_ΒΙΒΛΙΟΘΗΚΗΣ",
            key_count="2 Υποψήφια",
            key_types="Υποψήφια: {branch_id}, {onomasia}",
            final_pk_selection="branch_id",
            justification="Σταθερός, συμπαγής κωδικός κατάλληλος για αναφορές ξένων κλειδιών.",
        ),
        KeyAnalysisRow(
            entity_name="ΒΙΒΛΙΟΘΗΚΟΝΟΜΟΣ",
            key_count="2 Υποψήφια",
            key_types="Υποψήφια: {staff_id}, {adt}",
            final_pk_selection="staff_id",
            justification="Εσωτερικός αριθμός μητρώου υπαλλήλου.",
        ),
        KeyAnalysisRow(
            entity_name="ΒΙΒΛΙΟΓΡΑΦΙΚΟΣ_ΤΙΤΛΟΣ",
            key_count="1 Υποψήφιο",
            key_types="Υποψήφιο: {isbn}",
            final_pk_selection="isbn",
            justification="Διεθνές αναγνωρισμένο πρότυπο μοναδικής ταυτοποίησης εκδόσεων βιβλίων.",
        ),
        KeyAnalysisRow(
            entity_name="ΣΥΓΓΡΑΦΕΑΣ",
            key_count="1 Υποψήφιο",
            key_types="Υποψήφιο: {author_id}",
            final_pk_selection="author_id",
            justification="Μοναδικός τεχνητός κωδικός συγγραφέα.",
        ),
        KeyAnalysisRow(
            entity_name="ΑΝΤΙΤΥΠΟ",
            key_count="Ασθενής (1 Μερικό + 1 Υποψήφιο Barcode)",
            key_types="Μερικό: {copy_number}, Υποψήφιο: {barcode}",
            final_pk_selection="(isbn, copy_number)",
            justification="Σύνθετο πρωτεύον κλειδί: Foreign Key του τίτλου (isbn) + αύξων αριθμός αντιτύπου (copy_number).",
            is_weak=True,
        ),
        KeyAnalysisRow(
            entity_name="ΜΕΛΟΣ",
            key_count="3 Υποψήφια",
            key_types="Υποψήφια: {card_number}, {adt}, {email}",
            final_pk_selection="card_number",
            justification="Επίσημος αριθμός κάρτας μέλους του δικτύου βιβλιοθηκών.",
        ),
        KeyAnalysisRow(
            entity_name="ΔΑΝΕΙΣΜΟΣ",
            key_count="1 Υποψήφιο",
            key_types="Υποψήφιο: {loan_id}",
            final_pk_selection="loan_id",
            justification="Μοναδικός αριθμός πράξης δανεισμού.",
        ),
        KeyAnalysisRow(
            entity_name="ΚΡΑΤΗΣΗ",
            key_count="1 Υποψήφιο",
            key_types="Υποψήφιο: {reservation_id}",
            final_pk_selection="reservation_id",
            justification="Μοναδικός κωδικός αιτήματος κράτησης.",
        ),
    ]

    # 5. Relationships List
    relationships = [
        Relationship(
            letter_id="α",
            name="ΔΙΕΥΘΥΝΕΙ (Manages Branch)",
            connected_entities="ΠΑΡΑΡΤΗΜΑ <-> ΒΙΒΛΙΟΘΗΚΟΝΟΜΟΣ",
            cardinality="1:1",
            participation="Ολική για Παράρτημα (1,1), Μερική για Βιβλιοθηκονόμο (0,1)",
            relationship_type="Κανονική Σχέση",
            attributes=["hmer_analipsis"],
            justification="Κάθε παράρτημα έχει υποχρεωτικά έναν διευθυντή. Ένας βιβλιοθηκονόμος διευθύνει το πολύ ένα παράρτημα.",
        ),
        Relationship(
            letter_id="β",
            name="ΑΠΑΣΧΟΛΕΙ (Employs Staff)",
            connected_entities="ΠΑΡΑΡΤΗΜΑ <-> ΒΙΒΛΙΟΘΗΚΟΝΟΜΟΣ",
            cardinality="1:N",
            participation="Ολική για Βιβλιοθηκονόμο (1,1), Ολική για Παράρτημα (1,N)",
            relationship_type="Κανονική Σχέση",
            attributes=[],
            justification="Κάθε υπάλληλος ανήκει οργανικά σε ένα παράρτημα. Κάθε παράρτημα απασχολεί πολλούς υπαλλήλους.",
        ),
        Relationship(
            letter_id="γ",
            name="ΣΥΓΓΡΑΦΗ (Authorship)",
            connected_entities="ΣΥΓΓΡΑΦΕΑΣ <-> ΒΙΒΛΙΟΓΡΑΦΙΚΟΣ_ΤΙΤΛΟΣ",
            cardinality="N:M",
            participation="Ολική για Τίτλο (1,N), Μερική για Συγγραφέα (1,N)",
            relationship_type="Κανονική Σχέση (Junction)",
            attributes=["seira_syggrafea", "rolos_symvolis"],
            justification="Ένα βιβλίο μπορεί να γραφτεί από πολλούς συγγραφείς και ένας συγγραφέας μπορεί να έχει συγγράψει πολλά βιβλία.",
        ),
        Relationship(
            letter_id="δ",
            name="ΕΧΕΙ_ΑΝΤΙΤΥΠΑ (Has Physical Copies)",
            connected_entities="ΒΙΒΛΙΟΓΡΑΦΙΚΟΣ_ΤΙΤΛΟΣ <-> ΑΝΤΙΤΥΠΟ",
            cardinality="1:N",
            participation="Ολική για Αντίτυπο (1,1), Μερική για Τίτλο (0,N)",
            relationship_type="Ταυτοποιούσα Σχέση (Identifying)",
            attributes=[],
            justification="Ταυτοποιούσα σχέση της ασθενούς οντότητας ΑΝΤΙΤΥΠΟ από τον ΒΙΒΛΙΟΓΡΑΦΙΚΟ ΤΙΤΛΟ.",
        ),
        Relationship(
            letter_id="ε",
            name="ΣΤΕΓΑΖΕΙ_ΑΝΤΙΤΥΠΟ (Houses Copy)",
            connected_entities="ΠΑΡΑΡΤΗΜΑ <-> ΑΝΤΙΤΥΠΟ",
            cardinality="1:N",
            participation="Ολική για Αντίτυπο (1,1), Μερική για Παράρτημα (0,N)",
            relationship_type="Κανονική Σχέση",
            attributes=[],
            justification="Κάθε φυσικό αντίτυπο ανήκει στη συλλογή ενός συγκεκριμένου παραρτήματος.",
        ),
        Relationship(
            letter_id="στ",
            name="ΠΡΑΓΜΑΤΟΠΟΙΕΙ_ΔΑΝΕΙΣΜΟ (Borrows Copy)",
            connected_entities="ΜΕΛΟΣ <-> ΔΑΝΕΙΣΜΟΣ",
            cardinality="1:N",
            participation="Ολική για Δανεισμό (1,1), Μερική για Μέλος (0,N)",
            relationship_type="Κανονική Σχέση",
            attributes=[],
            justification="Κάθε δανεισμός γίνεται από ένα συγκεκριμένο μέλος. Ένα μέλος πραγματοποιεί πολλαπλούς δανεισμούς.",
        ),
        Relationship(
            letter_id="ζ",
            name="ΑΦΟΡΑ_ΑΝΤΙΤΥΠΟ (Loan Target)",
            connected_entities="ΑΝΤΙΤΥΠΟ <-> ΔΑΝΕΙΣΜΟΣ",
            cardinality="1:N",
            participation="Ολική για Δανεισμό (1,1), Μερική για Αντίτυπο (0,N)",
            relationship_type="Κανονική Σχέση",
            attributes=[],
            justification="Κάθε δανεισμός αφορά ένα συγκεκριμένο φυσικό αντίτυπο. Ένα αντίτυπο μπορεί να έχει ιστορικό πολλών δανεισμών.",
        ),
        Relationship(
            letter_id="η",
            name="ΥΠΟΒΑΛΛΕΙ_ΚΡΑΤΗΣΗ (Submits Reservation)",
            connected_entities="ΜΕΛΟΣ <-> ΚΡΑΤΗΣΗ",
            cardinality="1:N",
            participation="Ολική για Κράτηση (1,1), Μερική για Μέλος (0,N)",
            relationship_type="Κανονική Σχέση",
            attributes=[],
            justification="Κάθε κράτηση υποβάλλεται από ένα μέλος.",
        ),
        Relationship(
            letter_id="θ",
            name="ΑΦΟΡΑ_ΤΙΤΛΟ_ΚΡΑΤΗΣΗΣ (Reserved Title)",
            connected_entities="ΒΙΒΛΙΟΓΡΑΦΙΚΟΣ_ΤΙΤΛΟΣ <-> ΚΡΑΤΗΣΗ",
            cardinality="1:N",
            participation="Ολική για Κράτηση (1,1), Μερική για Τίτλο (0,N)",
            relationship_type="Κανονική Σχέση",
            attributes=[],
            justification="Η κράτηση αφορά τον αφηρημένο τίτλο (ISBN) και όχι συγκεκριμένο αντίτυπο.",
        ),
        Relationship(
            letter_id="ι",
            name="ΠΑΡΑΛΑΒΗ_ΣΕ_ΠΑΡΑΡΤΗΜΑ (Pickup Branch)",
            connected_entities="ΠΑΡΑΡΤΗΜΑ <-> ΚΡΑΤΗΣΗ",
            cardinality="1:N",
            participation="Ολική για Κράτηση (1,1), Μερική για Παράρτημα (0,N)",
            relationship_type="Κανονική Σχέση",
            attributes=[],
            justification="Το μέλος επιλέγει το επιθυμητό παράρτημα παραλαβής του δεσμευμένου βιβλίου.",
        ),
    ]

    # 6. Design Assumptions
    assumptions = [
        "Ο Βιβλιοθηκονόμος-Διευθυντής συνδέεται στον πίνακα PARARTIMA μέσω foreign key manager_staff_id με UNIQUE constraint (1:1).",
        "Το φυσικό αντίτυπο μοντελοποιείται ως ασθενής οντότητα με σύνθετο κλειδί (isbn, copy_number) και επιπλέον UNIQUE constraint στο barcode.",
        "Τα πλειότιμα γνωρίσματα (εβδομαδιαίο ωράριο λειτουργίας παραρτήματος και τηλέφωνα μελών) εξάγονται σε ανεξάρτητους σχεσιακούς πίνακες 1:N.",
        "Ο δανεισμός συνδέεται με συγκεκριμένο φυσικό αντίτυπο, ενώ η κράτηση συνδέεται με τον γενικό τίτλο (ISBN) και το παράρτημα παραλαβής.",
    ]

    # 7. ER Diagram Tables
    er_tables = [
        ERTable(
            id="t-branch",
            label="PARARTIMA",
            x=60,
            y=50,
            attrs=[
                ERTableAttr("branch_id", pk=True),
                ERTableAttr("onomasia"),
                ERTableAttr("odos"),
                ERTableAttr("arithmos"),
                ERTableAttr("tk"),
                ERTableAttr("synoikia"),
                ERTableAttr("tilefono"),
                ERTableAttr("xoritikotita"),
                ERTableAttr("manager_staff_id", fk=True),
                ERTableAttr("hmer_analipsis_director"),
            ],
        ),
        ERTable(
            id="t-staff",
            label="VIVLIOTHIKONOMOS",
            x=460,
            y=50,
            attrs=[
                ERTableAttr("staff_id", pk=True),
                ERTableAttr("adt"),
                ERTableAttr("onoma"),
                ERTableAttr("eponymo"),
                ERTableAttr("eidikotita"),
                ERTableAttr("tilefono"),
                ERTableAttr("branch_id", fk=True),
            ],
        ),
        ERTable(
            id="t-author",
            label="SYGGRAFEAS",
            x=860,
            y=50,
            attrs=[
                ERTableAttr("author_id", pk=True),
                ERTableAttr("onomateponymo"),
                ERTableAttr("ethnikotita"),
                ERTableAttr("etos_gennisis"),
            ],
        ),
        ERTable(
            id="t-copy",
            label="ANTITYPO",
            x=60,
            y=400,
            attrs=[
                ERTableAttr("isbn", pk=True, fk=True),
                ERTableAttr("copy_number", pk=True),
                ERTableAttr("barcode"),
                ERTableAttr("katastasi_fysiki"),
                ERTableAttr("diathesimotita"),
                ERTableAttr("thesi_rafi"),
                ERTableAttr("branch_id", fk=True),
            ],
        ),
        ERTable(
            id="t-book",
            label="TITLOS_VIVLIOU",
            x=460,
            y=350,
            attrs=[
                ERTableAttr("isbn", pk=True),
                ERTableAttr("titlos"),
                ERTableAttr("ekdotikos_oikos"),
                ERTableAttr("etos_ekdosis"),
                ERTableAttr("katigoria"),
                ERTableAttr("arithmos_selidon"),
            ],
        ),
        ERTable(
            id="t-book-author",
            label="SYGGRAFI_TITLOU",
            x=860,
            y=350,
            attrs=[
                ERTableAttr("isbn", pk=True, fk=True),
                ERTableAttr("author_id", pk=True, fk=True),
                ERTableAttr("seira_syggrafea"),
                ERTableAttr("rolos_symvolis"),
            ],
        ),
        ERTable(
            id="t-member",
            label="MELOS",
            x=60,
            y=680,
            attrs=[
                ERTableAttr("card_number", pk=True),
                ERTableAttr("adt"),
                ERTableAttr("onoma"),
                ERTableAttr("eponymo"),
                ERTableAttr("hmer_gennisis"),
                ERTableAttr("odos"),
                ERTableAttr("arithmos"),
                ERTableAttr("tk"),
                ERTableAttr("poli"),
                ERTableAttr("email"),
                ERTableAttr("hmer_eggrafis"),
                ERTableAttr("katastasi_melous"),
            ],
        ),
        ERTable(
            id="t-loan",
            label="DANEISMOS",
            x=460,
            y=680,
            attrs=[
                ERTableAttr("loan_id", pk=True),
                ERTableAttr("card_number", fk=True),
                ERTableAttr("isbn", fk=True),
                ERTableAttr("copy_number", fk=True),
                ERTableAttr("hmer_daneismou"),
                ERTableAttr("hmer_epistrofis_prokathorismeni"),
                ERTableAttr("hmer_epistrofis_pragmatiki"),
                ERTableAttr("prostimo_poso"),
            ],
        ),
        ERTable(
            id="t-reservation",
            label="KRATISI",
            x=860,
            y=680,
            attrs=[
                ERTableAttr("reservation_id", pk=True),
                ERTableAttr("card_number", fk=True),
                ERTableAttr("isbn", fk=True),
                ERTableAttr("branch_id", fk=True),
                ERTableAttr("hmer_ypovolis"),
                ERTableAttr("seira_proteraiotitas"),
                ERTableAttr("katastasi_aitimatos"),
            ],
        ),
    ]

    # 8. ER Diagram Edges
    er_edges = [
        # Branch manages Staff (1:1)
        EREdge("M 320 80 L 460 80", "start-one-mandatory", "end-one-optional", "ΔΙΕΥΘΥΝΕΙ (1:1)", 390, 70),
        # Branch employs Staff (1:N)
        EREdge("M 320 120 L 460 120", "start-one-mandatory", "end-many-optional", "ΑΠΑΣΧΟΛΕΙ (1:N)", 390, 140),
        # Author to Book Authorship (1:N)
        EREdge("M 960 250 L 960 350", "start-one-mandatory", "end-many-optional", "ΣΥΓΓΡΑΦΕΙ (1:N)", 975, 300),
        # Book Title to Book Authorship (1:N)
        EREdge("M 720 380 L 860 380", "start-one-mandatory", "end-many-optional", "ΕΧΕΙ_ΣΥΓΓΡΑΦΕΙΣ (1:N)", 790, 370),
        # Book Title to Copies (1:N identifying)
        EREdge("M 460 410 L 320 410", "start-one-mandatory", "end-many-optional", "ΕΧΕΙ_ΑΝΤΙΤΥΠΑ (1:N)", 390, 400),
        # Branch to Copies (1:N)
        EREdge("M 190 378 L 190 400", "start-one-mandatory", "end-many-optional", "ΣΤΕΓΑΖΕΙ (1:N)", 205, 390),
        # Member to Loan (1:N)
        EREdge("M 320 700 L 460 700", "start-one-mandatory", "end-many-optional", "ΔΑΝΕΙΖΕΤΑΙ (1:N)", 390, 690),
        # Copy to Loan (1:N)
        EREdge("M 320 520 L 460 690", "start-one-mandatory", "end-many-optional", "ΑΦΟΡΑ_ΑΝΤΙΤΥΠΟ (1:N)", 390, 600),
        # Member to Reservation (1:N)
        EREdge("M 320 740 L 860 740", "start-one-mandatory", "end-many-optional", "ΥΠΟΒΑΛΛΕΙ (1:N)", 590, 755),
        # Book Title to Reservation (1:N)
        EREdge("M 720 480 L 860 690", "start-one-mandatory", "end-many-optional", "ΚΡΑΤΗΣΗ_ΤΙΤΛΟΥ (1:N)", 790, 585),
        # Branch to Reservation (1:N)
        EREdge("M 320 160 L 860 700", "start-one-mandatory", "end-many-optional", "ΠΑΡΑΛΑΒΗ_ΣΕ (1:N)", 590, 430),
    ]

    # 9. Relational Conversion Justifications
    relational_justifications = [
        RelationalJustification(
            title="1. Μετατροπή Ασθενούς Οντότητας (ΑΝΤΙΤΥΠΟ)",
            color_class="border-red-500",
            description="Ο πίνακας ANTITYPO λαμβάνει ως Foreign Key το isbn του τίτλου και σχηματίζει σύνθετο Primary Key (isbn, copy_number). Επιπλέον, ορίζεται foreign key προς το PARARTIMA για το παράρτημα στέγασης.",
        ),
        RelationalJustification(
            title="2. Μετατροπή Συσχέτισης N:M (ΣΥΓΓΡΑΦΗ)",
            color_class="border-amber-500",
            description="Η συσχέτιση N:M μεταξύ ΣΥΓΓΡΑΦΕΑ και ΒΙΒΛΙΟΓΡΑΦΙΚΟΥ ΤΙΤΛΟΥ μετατρέπεται στον ενδιάμεσο πίνακα SYGGRAFI_TITLOU με σύνθετο Primary Key (isbn, author_id) και τα γνωρίσματα της σχέσης.",
        ),
        RelationalJustification(
            title="3. Μετατροπή Συσχέτισης 1:1 (ΔΙΕΥΘΥΝΕΙ)",
            color_class="border-blue-500",
            description="Επειδή το Παράρτημα έχει ολική συμμετοχή (κάθε παράρτημα έχει υποχρεωτικά διευθυντή), τοποθετείται το manager_staff_id στον πίνακα PARARTIMA με UNIQUE constraint.",
        ),
        RelationalJustification(
            title="4. Μετατροπή Πλειότιμων Γνωρισμάτων (ΩΡΑΡΙΟ_ΠΑΡΑΡΤΗΜΑΤΟΣ, ΤΗΛΕΦΩΝΑ_ΜΕΛΟΥΣ)",
            color_class="border-purple-500",
            description="Τα πλειότιμα γνωρίσματα αναλύονται στους σχεσιακούς πίνακες ORARIO_LEITOURGIAS (branch_id, imera, ora_enarxis, ora_lixis) και TILEFONA_MELOUS (card_number, tilefono).",
        ),
        RelationalJustification(
            title="5. Υλοποίηση Συναλλαγών Δανεισμού & Κρατήσεων",
            color_class="border-emerald-500",
            description="Ο πίνακας DANEISMOS συνδέει το αντίτυπο (isbn, copy_number) με το μέλος (card_number). Ο πίνακας KRATISI συνδέει τον τίτλο (isbn), το μέλος (card_number) και το παράρτημα παραλαβής (branch_id).",
        ),
    ]

    # 10. Complete Production SQL DDL
    sql_ddl = """-- ==========================================================
-- PostgreSQL / MySQL Relational Schema for Municipal Library Network
-- Case Study: Exam Paper 7 (Δίκτυο Δημοτικών Βιβλιοθηκών)
-- ==========================================================

-- 1. Entity: VIVLIOTHIKONOMOS (Staff / Librarians)
CREATE TABLE VIVLIOTHIKONOMOS (
    staff_id VARCHAR(15) PRIMARY KEY,
    adt VARCHAR(10) NOT NULL UNIQUE,
    onoma VARCHAR(50) NOT NULL,
    eponymo VARCHAR(50) NOT NULL,
    eidikotita VARCHAR(60) NOT NULL,
    tilefono VARCHAR(20) NOT NULL,
    branch_id VARCHAR(10) -- Will be referenced by FK after branch table creation
);

-- 2. Entity: PARARTIMA (Library Branches)
CREATE TABLE PARARTIMA (
    branch_id VARCHAR(10) PRIMARY KEY,
    onomasia VARCHAR(100) NOT NULL UNIQUE,
    odos VARCHAR(60) NOT NULL,
    arithmos VARCHAR(10) NOT NULL,
    tk VARCHAR(10) NOT NULL,
    synoikia VARCHAR(50) NOT NULL,
    tilefono VARCHAR(20) NOT NULL,
    xoritikotita INT NOT NULL CHECK (xoritikotita > 0),
    manager_staff_id VARCHAR(15) UNIQUE,
    hmer_analipsis_director DATE,
    FOREIGN KEY (manager_staff_id) REFERENCES VIVLIOTHIKONOMOS(staff_id) ON DELETE SET NULL
);

-- Add Foreign Key for Staff Branch employment
ALTER TABLE VIVLIOTHIKONOMOS
ADD CONSTRAINT fk_staff_branch
FOREIGN KEY (branch_id) REFERENCES PARARTIMA(branch_id) ON DELETE RESTRICT;

-- 3. Multi-valued Attribute: ORARIO_LEITOURGIAS
CREATE TABLE ORARIO_LEITOURGIAS (
    branch_id VARCHAR(10) NOT NULL,
    imera VARCHAR(20) NOT NULL CHECK (imera IN ('Δευτέρα', 'Τρίτη', 'Τετάρτη', 'Πέμπτη', 'Παρασκευή', 'Σάββατο', 'Κυριακή')),
    ora_enarxis TIME NOT NULL,
    ora_lixis TIME NOT NULL,
    PRIMARY KEY (branch_id, imera, ora_enarxis),
    FOREIGN KEY (branch_id) REFERENCES PARARTIMA(branch_id) ON DELETE CASCADE,
    CHECK (ora_lixis > ora_enarxis)
);

-- 4. Entity: TITLOS_VIVLIOU (Book Titles / Catalog)
CREATE TABLE TITLOS_VIVLIOU (
    isbn VARCHAR(20) PRIMARY KEY,
    titlos VARCHAR(200) NOT NULL,
    ekdotikos_oikos VARCHAR(100) NOT NULL,
    etos_ekdosis INT NOT NULL CHECK (etos_ekdosis >= 1450),
    katigoria VARCHAR(60) NOT NULL,
    arithmos_selidon INT NOT NULL CHECK (arithmos_selidon > 0)
);

-- 5. Entity: SYGGRAFEAS (Authors)
CREATE TABLE SYGGRAFEAS (
    author_id VARCHAR(15) PRIMARY KEY,
    onomateponymo VARCHAR(120) NOT NULL,
    ethnikotita VARCHAR(50) NOT NULL,
    etos_gennisis INT CHECK (etos_gennisis >= 1000)
);

-- 6. Junction Table: SYGGRAFI_TITLOU (N:M Book Authorship)
CREATE TABLE SYGGRAFI_TITLOU (
    isbn VARCHAR(20) NOT NULL,
    author_id VARCHAR(15) NOT NULL,
    seira_syggrafea INT NOT NULL DEFAULT 1 CHECK (seira_syggrafea > 0),
    rolos_symvolis VARCHAR(50) DEFAULT 'Κύριος Συγγραφέας',
    PRIMARY KEY (isbn, author_id),
    FOREIGN KEY (isbn) REFERENCES TITLOS_VIVLIOU(isbn) ON DELETE CASCADE,
    FOREIGN KEY (author_id) REFERENCES SYGGRAFEAS(author_id) ON DELETE CASCADE
);

-- 7. Weak Entity: ANTITYPO (Physical Copies)
CREATE TABLE ANTITYPO (
    isbn VARCHAR(20) NOT NULL,
    copy_number INT NOT NULL CHECK (copy_number > 0),
    barcode VARCHAR(40) NOT NULL UNIQUE,
    katastasi_fysiki VARCHAR(30) NOT NULL CHECK (katastasi_fysiki IN ('Άριστη', 'Καλή', 'Φθαρμένο', 'Υπό Επισκευή')),
    diathesimotita VARCHAR(30) NOT NULL DEFAULT 'Διαθέσιμο' CHECK (diathesimotita IN ('Διαθέσιμο', 'Δανεισμένο', 'Δεσμευμένο')),
    thesi_rafi VARCHAR(30) NOT NULL,
    branch_id VARCHAR(10) NOT NULL,
    PRIMARY KEY (isbn, copy_number),
    FOREIGN KEY (isbn) REFERENCES TITLOS_VIVLIOU(isbn) ON DELETE CASCADE,
    FOREIGN KEY (branch_id) REFERENCES PARARTIMA(branch_id) ON DELETE RESTRICT
);

-- 8. Entity: MELOS (Library Members)
CREATE TABLE MELOS (
    card_number VARCHAR(20) PRIMARY KEY,
    adt VARCHAR(10) NOT NULL UNIQUE,
    onoma VARCHAR(50) NOT NULL,
    eponymo VARCHAR(50) NOT NULL,
    hmer_gennisis DATE NOT NULL,
    odos VARCHAR(60) NOT NULL,
    arithmos VARCHAR(10) NOT NULL,
    tk VARCHAR(10) NOT NULL,
    poli VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    hmer_eggrafis DATE NOT NULL,
    katastasi_melous VARCHAR(20) NOT NULL DEFAULT 'Ενεργό' CHECK (katastasi_melous IN ('Ενεργό', 'Σε Αναστολή'))
);

-- 9. Multi-valued Attribute: TILEFONA_MELOUS
CREATE TABLE TILEFONA_MELOUS (
    card_number VARCHAR(20) NOT NULL,
    tilefono VARCHAR(20) NOT NULL,
    PRIMARY KEY (card_number, tilefono),
    FOREIGN KEY (card_number) REFERENCES MELOS(card_number) ON DELETE CASCADE
);

-- 10. Entity: DANEISMOS (Loan Transactions)
CREATE TABLE DANEISMOS (
    loan_id VARCHAR(20) PRIMARY KEY,
    card_number VARCHAR(20) NOT NULL,
    isbn VARCHAR(20) NOT NULL,
    copy_number INT NOT NULL,
    hmer_daneismou DATE NOT NULL,
    hmer_epistrofis_prokathorismeni DATE NOT NULL,
    hmer_epistrofis_pragmatiki DATE,
    prostimo_poso DECIMAL(8, 2) DEFAULT 0.00 CHECK (prostimo_poso >= 0),
    FOREIGN KEY (card_number) REFERENCES MELOS(card_number) ON DELETE RESTRICT,
    FOREIGN KEY (isbn, copy_number) REFERENCES ANTITYPO(isbn, copy_number) ON DELETE RESTRICT,
    CHECK (hmer_epistrofis_prokathorismeni >= hmer_daneismou)
);

-- 11. Entity: KRATISI (Reservations Queue)
CREATE TABLE KRATISI (
    reservation_id VARCHAR(20) PRIMARY KEY,
    card_number VARCHAR(20) NOT NULL,
    isbn VARCHAR(20) NOT NULL,
    branch_id VARCHAR(10) NOT NULL,
    hmer_ypovolis TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    seira_proteraiotitas INT NOT NULL CHECK (seira_proteraiotitas > 0),
    katastasi_aitimatos VARCHAR(30) NOT NULL DEFAULT 'Σε αναμονή' CHECK (
        katastasi_aitimatos IN ('Σε αναμονή', 'Ειδοποιήθηκε το μέλος', 'Ολοκληρώθηκε', 'Ακυρώθηκε')
    ),
    PRIMARY KEY (reservation_id),
    FOREIGN KEY (card_number) REFERENCES MELOS(card_number) ON DELETE CASCADE,
    FOREIGN KEY (isbn) REFERENCES TITLOS_VIVLIOU(isbn) ON DELETE CASCADE,
    FOREIGN KEY (branch_id) REFERENCES PARARTIMA(branch_id) ON DELETE RESTRICT
);

-- Indexes for Query Performance
CREATE INDEX idx_antitypo_branch ON ANTITYPO(branch_id);
CREATE INDEX idx_daneismos_active ON DANEISMOS(card_number, hmer_epistrofis_pragmatiki);
CREATE INDEX idx_kratisi_queue ON KRATISI(isbn, branch_id, seira_proteraiotitas);
"""

    return Scenario(
        id="library_management",
        title="Σύστημα Διαχείρισης Δικτύου Δημοτικών Βιβλιοθηκών",
        subtitle="Δίκτυο Δημοτικών Βιβλιοθηκών, Παραρτήματα, Βιβλιογραφικοί Τίτλοι, Αντίτυπα, Μέλη, Δανεισμοί & Κρατήσεις",
        course_tag="Βάσεις Δεδομένων (Πρόοδος 2025-2026 - Θέμα 7)",
        paragraphs=paragraphs,
        entities=entities,
        relationship_attributes=relationship_attributes,
        keys_analysis=keys_analysis,
        relationships=relationships,
        assumptions=assumptions,
        er_tables=er_tables,
        er_edges=er_edges,
        relational_justifications=relational_justifications,
        sql_ddl=sql_ddl,
    )
