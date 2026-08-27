"""Hotel Resort Management case study scenario module.

Contains the complete parsed and modeled ER analysis for the International Hotel Resorts Group
(Resort Units, Rooms, Staff, Guests, Bookings, Inspections, Extra Services),
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


def createHotelManagementScenario() -> Scenario:
    """Constructs and returns the Hotel Resort Management database scenario.

    Returns:
        Scenario: Fully populated scenario instance.
    """
    # 1. Text Paragraphs with Interactive Segments
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Ένας διεθνής όμιλος ξενοδοχειακών συγκροτημάτων και θερέτρων (Hotel Resorts) αναπτύσσει ένα ενιαίο σύστημα βάσεων δεδομένων για τη διαχείριση των "),
                TextSegment(
                    text="ξενοδοχειακών μονάδων",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Strong Entity): Αυτοτελής ξενοδοχειακή μονάδα με μοναδικό Hotel ID.",
                ),
                TextSegment(text=", των "),
                TextSegment(
                    text="δωματίων",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΑΣΘΕΝΗΣ ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-weak",
                    tooltip="Ασθενής Οντότητα (Weak Entity): Δωμάτιο που προσδιορίζεται μόνο σε συνδυασμό με το ξενοδοχείο.",
                ),
                TextSegment(text=", του "),
                TextSegment(
                    text="προσωπικού",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Strong Entity): Εργαζόμενος ξενοδοχείου με μοναδικό ΑΜΥ.",
                ),
                TextSegment(text=", των "),
                TextSegment(
                    text="επισκεπτών",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Strong Entity): Φυσικό πρόσωπο επισκέπτη με αριθμό διαβατηρίου/ταυτότητας.",
                ),
                TextSegment(text=", των "),
                TextSegment(
                    text="κρατήσεων",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Strong Entity): Κράτηση διαμονής με μοναδικό Booking ID.",
                ),
                TextSegment(text=" και των "),
                TextSegment(
                    text="πρόσθετων παρεχόμενων υπηρεσιών",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Strong Entity): Έξτρα υπηρεσία θέρετρου με μοναδικό κωδικό υπηρεσίας.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color=None,
        ),
        Paragraph(
            segments=[
                TextSegment(text="1. <strong>Ξενοδοχειακές Μονάδες (Resorts):</strong> Κάθε ξενοδοχειακή μονάδα έχει έναν "),
                TextSegment(
                    text="μοναδικό κωδικό ξενοδοχείου (Hotel ID)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Μοναδικός κωδικός ξενοδοχείου.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="εμπορική επωνυμία (π.χ. 'Aegean Grand Resort')",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Υποψήφιο Κλειδί (Candidate Key): Μοναδική επωνυμία θέρετρου.",
                ),
                TextSegment(text=", "),
                TextSegment(text="κατηγορία αστέρων (1 έως 5)", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="γεωγραφική περιοχή/νήσο", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="πόλη", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="διεύθυνση", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και "),
                TextSegment(text="επίσημο email επικοινωνίας", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=". Κάθε μονάδα προσφέρει μια σειρά από "),
                TextSegment(
                    text="εγκαταστάσεις και παροχές (Amenities: 'Πισίνα Infinity', 'Spa', 'Γήπεδο Τένις')",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΠΛΕΙΟΤΙΜΟ",
                    badge_class="badge-attr-multi",
                    tooltip="Πλειότιμο Γνώρισμα: Εξάγεται στον σχεσιακό πίνακα ΠΑΡΟΧΕΣ_ΞΕΝΟΔΟΧΕΙΟΥ.",
                ),
                TextSegment(text=" που καταγράφονται ως λίστα παροχών. Κάθε ξενοδοχείο "),
                TextSegment(
                    text="διευθύνεται από έναν Γενικό Διευθυντή (General Manager)",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ 1:1",
                    badge_class="badge-rel-11",
                    tooltip="Συσχέτιση 1:1 (ΔΙΕΥΘΥΝΕΙ): Ολική συμμετοχή για Ξενοδοχείο, μερική για Υπάλληλο.",
                ),
                TextSegment(text=", για τον οποίο καταγράφεται η "),
                TextSegment(
                    text="ημερομηνία ανάληψης καθηκόντων",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ ΣΧΕΣΗΣ",
                    badge_class="badge-attr-composite",
                    tooltip="Γνώρισμα Συσχέτισης: Αποθηκεύεται στον πίνακα ΞΕΝΟΔΟΧΕΙΟ.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-blue-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="2. <strong>Δωμάτια (Rooms):</strong> Κάθε ξενοδοχείο διαθέτει πολλαπλά δωμάτια. Κάθε δωμάτιο προσδιορίζεται από τον "),
                TextSegment(
                    text="αριθμό δωματίου (Room Number, π.χ. 101, 204), ο οποίος είναι μοναδικός μόνο εντός της συγκεκριμένης μονάδας",
                    is_highlight=True,
                    category="key",
                    tag_label="PARTIAL KEY",
                    badge_class="badge-key-partial",
                    tooltip="Μερικό Κλειδί (Partial Key / Discriminator): Ταυτοποιεί το δωμάτιο μόνο σε συνδυασμό με το Hotel ID.",
                ),
                TextSegment(text=". Για κάθε δωμάτιο καταγράφονται: ο "),
                TextSegment(text="όροφος", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", ο "),
                TextSegment(text="τύπος δωματίου ('Standard Double', 'Deluxe Suite', 'Family Villa')", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(text="μέγιστη χωρητικότητα ατόμων", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(text="βασική τιμή διανυκτέρευσης", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και η "),
                TextSegment(text="θέα ('Θέα Θάλασσα', 'Θέα Κήπος')", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=". "),
                TextSegment(
                    text="Ένα δωμάτιο δεν μπορεί να υπάρξει χωρίς το αντίστοιχο ξενοδοχείο",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΑΣΘΕΝΗΣ ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-weak",
                    tooltip="Υπαρκτική Εξάρτηση: Προσδιορίζουσα οντότητα είναι η ΞΕΝΟΔΟΧΕΙΑΚΗ_ΜΟΝΑΔΑ.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-amber-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="3. <strong>Επισκέπτες (Guests):</strong> Για κάθε επισκέπτη καταγράφονται: ο "),
                TextSegment(
                    text="μοναδικός Αριθμός Διαβατηρίου ή Ταυτότητας",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Μοναδικό αναγνωριστικό ταξιδιωτικού εγγράφου.",
                ),
                TextSegment(text=", το "),
                TextSegment(text="ονοματεπώνυμο", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(text="εθνικότητα", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(text="ημερομηνία γέννησης", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(text="διεύθυνση κατοικίας", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", το "),
                TextSegment(
                    text="κύριο email",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Υποψήφιο Κλειδί (Candidate Key): Μοναδικό email επικοινωνίας επισκέπτη.",
                ),
                TextSegment(text=" και οι "),
                TextSegment(text="πόντοι επιβράβευσης (Loyalty Points)", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=". Ένας πελάτης μπορεί να δηλώσει "),
                TextSegment(
                    text="πολλαπλά τηλέφωνα επικοινωνίας",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΠΛΕΙΟΤΙΜΟ",
                    badge_class="badge-attr-multi",
                    tooltip="Πλειότιμο Γνώρισμα: Αποθηκεύεται στον σχεσιακό πίνακα ΤΗΛΕΦΩΝΟ_ΕΠΙΣΚΕΠΤΗ.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-purple-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="4. <strong>Κρατήσεις (Bookings):</strong> Ένας πελάτης μπορεί να πραγματοποιήσει κρατήσεις για ένα ή περισσότερα δωμάτια. Κάθε κράτηση λαμβάνει έναν "),
                TextSegment(
                    text="μοναδικό κωδικό κράτησης (Booking ID)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Μοναδικός κωδικός κράτησης.",
                ),
                TextSegment(text=", την "),
                TextSegment(text="ημερομηνία πραγματοποίησης της κράτησης", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", την "),
                TextSegment(text="προγραμματισμένη ημερομηνία άφιξης (Check-in)", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", την "),
                TextSegment(text="ημερομηνία αναχώρησης (Check-out)", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", τον "),
                TextSegment(text="αριθμό ενηλίκων και παιδιών", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", την "),
                TextSegment(text="κατάσταση της κράτησης ('Confirmed', 'Checked-in', 'Completed', 'Cancelled')", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και το "),
                TextSegment(text="συμφωνηθέν συνολικό κόστος διαμονής", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=". Κάθε κράτηση "),
                TextSegment(
                    text="αντιστοιχεί σε έναν συγκεκριμένο πελάτη",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ 1:N",
                    badge_class="badge-rel-1n",
                    tooltip="Συσχέτιση 1:N (ΠΡΑΓΜΑΤΟΠΟΙΕΙ): Ένας πελάτης έχει πολλές κρατήσεις, κάθε κράτηση ανήκει σε έναν πελάτη.",
                ),
                TextSegment(text=" και "),
                TextSegment(
                    text="δεσμεύει ένα συγκεκριμένο δωμάτιο ενός ξενοδοχείου για το ορισμένο χρονικό διάστημα",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ 1:N",
                    badge_class="badge-rel-1n",
                    tooltip="Συσχέτιση 1:N (ΔΕΣΜΕΥΕΙ_ΔΩΜΑΤΙΟ): Ένα δωμάτιο έχει πολλές κρατήσεις σε διαφορετικές περιόδους.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-emerald-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="5. <strong>Προσωπικό & Έλεγχος Δωματίων:</strong> Για κάθε υπάλληλο καταγράφονται: ο "),
                TextSegment(
                    text="ΑΜ υπαλλήλου",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Μοναδικός αριθμός μητρώου υπαλλήλου.",
                ),
                TextSegment(text=", το "),
                TextSegment(text="ονοματεπώνυμο", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(text="ειδικότητα (Καθαριότητα, Συντήρηση, Reception, Chef)", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", ο "),
                TextSegment(text="μηνιαίος μισθός", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και το "),
                TextSegment(text="τηλέφωνο", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=". Κάθε υπάλληλος "),
                TextSegment(
                    text="εργάζεται σε ένα συγκεκριμένο ξενοδοχείο",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ 1:N",
                    badge_class="badge-rel-1n",
                    tooltip="Συσχέτιση 1:N (ΑΠΑΣΧΟΛΕΙ): Ένα ξενοδοχείο απασχολεί πολλούς εργαζομένους.",
                ),
                TextSegment(text=". Επιπλέον, το προσωπικό καθαριότητας και συντήρησης "),
                TextSegment(
                    text="αναλαμβάνει τον έλεγχο και καθαρισμό δωματίων",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ N:M",
                    badge_class="badge-rel-nm",
                    tooltip="Συσχέτιση N:M (ΕΛΕΓΧΟΣ_ΚΑΘΑΡΙΣΜΟΣ): Υλοποιείται με πίνακα διασύνδεσης ΕΛΕΓΧΟΣ_ΔΩΜΑΤΙΟΥ.",
                ),
                TextSegment(text=". Για κάθε ανάθεση καταγράφονται η "),
                TextSegment(
                    text="ημερομηνία/ώρα ελέγχου",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ ΣΧΕΣΗΣ",
                    badge_class="badge-attr-composite",
                    tooltip="Γνώρισμα Συσχέτισης / Discriminator: Χρονοσφραγίδα ελέγχου δωματίου.",
                ),
                TextSegment(text=", η "),
                TextSegment(
                    text="κατάσταση ετοιμότητας του δωματίου",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ ΣΧΕΣΗΣ",
                    badge_class="badge-attr-composite",
                    tooltip="Γνώρισμα Συσχέτισης: 'Έτοιμο', 'Υπό Καθαρισμό', 'Εκτός Λειτουργίας'.",
                ),
                TextSegment(text=" και "),
                TextSegment(
                    text="τυχόν παρατηρήσεις βλαβών",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ ΣΧΕΣΗΣ",
                    badge_class="badge-attr-composite",
                    tooltip="Γνώρισμα Συσχέτισης: Καταγραφή τεχνικών εκκρεμοτήτων.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-rose-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="6. <strong>Πρόσθετες Υπηρεσίες & Χρεώσεις (Services):</strong> Το θέρετρο προσφέρει έξτρα υπηρεσίες (π.χ. 'Μασάζ Αρωματοθεραπείας', 'Ημερήσια Κρουαζιέρα', 'Δείπνο A La Carte'). Κάθε υπηρεσία έχει "),
                TextSegment(
                    text="μοναδικό κωδικό υπηρεσίας",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Μοναδικός κωδικός πρόσθετης υπηρεσίας.",
                ),
                TextSegment(text=", "),
                TextSegment(text="περιγραφή", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και "),
                TextSegment(text="σταθερή τιμή μονάδας", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=". Στα πλαίσια μιας κράτησης, "),
                TextSegment(
                    text="οι επισκέπτες μπορούν να κάνουν χρήση πολλαπλών υπηρεσιών",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ N:M",
                    badge_class="badge-rel-nm",
                    tooltip="Συσχέτιση N:M (ΧΡΕΩΣΗ_ΥΠΗΡΕΣΙΑΣ): Πίνακας διασύνδεσης μεταξύ Κράτησης και Υπηρεσίας.",
                ),
                TextSegment(text=". Για κάθε χρέωση υπηρεσίας σε μια κράτηση καταγράφεται η "),
                TextSegment(
                    text="ημερομηνία/ώρα παροχής",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ ΣΧΕΣΗΣ",
                    badge_class="badge-attr-composite",
                    tooltip="Γνώρισμα Συσχέτισης / Discriminator: Χρονοσφραγίδα παροχής υπηρεσίας.",
                ),
                TextSegment(text=", η "),
                TextSegment(
                    text="ποσότητα",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ ΣΧΕΣΗΣ",
                    badge_class="badge-attr-composite",
                    tooltip="Γνώρισμα Συσχέτισης: Αριθμός μονάδων υπηρεσίας.",
                ),
                TextSegment(text=" και το "),
                TextSegment(
                    text="συνολικό επιπλέον ποσό χρέωσης",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ ΣΧΕΣΗΣ",
                    badge_class="badge-attr-composite",
                    tooltip="Γνώρισμα Συσχέτισης: Τελικό ποσό χρέωσης στο λογαριασμό κράτησης.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-cyan-500",
        ),
    ]

    # 2. Detailed Entities List
    entities = [
        Entity(
            name="ΞΕΝΟΔΟΧΕΙΑΚΗ_ΜΟΝΑΔΑ (Hotel Resort)",
            entity_type="Ισχυρή Οντότητα",
            is_weak=False,
            owner_entity=None,
            justification="Αυτοτελής μονάδα φιλοξενίας με μοναδικό κωδικό Hotel ID και πλήρη επιχειρησιακή ανεξαρτησία.",
            attributes=[
                Attribute("hotel_id", "Απλό / Μονότιμο", is_pk=True, notes="Μοναδικός κωδικός μονάδας (PK)"),
                Attribute("eponymia", "Απλό / Μονότιμο", is_candidate=True, notes="Εμπορική επωνυμία θέρετρου (Candidate Key)"),
                Attribute("asteria", "Απλό / Μονότιμο", notes="Κατηγορία κατάταξης αστέρων (1-5)"),
                Attribute("geografiki_perioxi", "Απλό / Μονότιμο", notes="Γεωγραφική περιοχή / νήσος"),
                Attribute("poli", "Απλό / Μονότιμο", notes="Πόλη έδρας"),
                Attribute("diefthynsi", "Απλό / Μονότιμο", notes="Οδός και αριθμός"),
                Attribute("email", "Απλό / Μονότιμο", notes="Επίσημο email επικοινωνίας"),
                Attribute("amenities", "Πλειότιμο", notes="Λίστα παροχών θέρετρου (Πίνακας ΠΑΡΟΧΕΣ_ΞΕΝΟΔΟΧΕΙΟΥ)"),
            ],
        ),
        Entity(
            name="ΔΩΜΑΤΙΟ (Room)",
            entity_type="Ασθενής Οντότητα",
            is_weak=True,
            owner_entity="ΞΕΝΟΔΟΧΕΙΑΚΗ_ΜΟΝΑΔΑ",
            justification="Ασθενής οντότητα. Ο αριθμός δωματίου επαναλαμβάνεται σε διαφορετικά ξενοδοχεία και απαιτεί το Hotel ID για πλήρη ταυτοποίηση.",
            attributes=[
                Attribute("room_number", "Απλό / Μονότιμο", is_partial=True, notes="Μερικό Κλειδί (Discriminator) εντός της μονάδας"),
                Attribute("orofos", "Απλό / Μονότιμο", notes="Αριθμός ορόφου"),
                Attribute("typos_domatiou", "Απλό / Μονότιμο", notes="Τύπος ('Standard Double', 'Deluxe Suite', 'Family Villa')"),
                Attribute("xoritikotita", "Απλό / Μονότιμο", notes="Μέγιστος αριθμός φιλοξενούμενων ατόμων"),
                Attribute("vasiki_timi", "Απλό / Μονότιμο", notes="Βασική τιμή διανυκτέρευσης"),
                Attribute("thea", "Απλό / Μονότιμο", notes="Προσανατολισμός ('Θέα Θάλασσα', 'Θέα Κήπος')"),
            ],
        ),
        Entity(
            name="ΕΠΙΣΚΕΠΤΗΣ (Guest)",
            entity_type="Ισχυρή Οντότητα",
            is_weak=False,
            owner_entity=None,
            justification="Φυσικό πρόσωπο πελάτη με μοναδικό αριθμό διαβατηρίου ή ταυτότητας.",
            attributes=[
                Attribute("passport_id", "Απλό / Μονότιμο", is_pk=True, notes="Αριθμός Διαβατηρίου ή ΑΔΤ (PK)"),
                Attribute("onomateponymo", "Απλό / Μονότιμο", notes="Ονοματεπώνυμο επισκέπτη"),
                Attribute("ethnikotita", "Απλό / Μονότιμο", notes="Χώρα ιθαγένειας"),
                Attribute("hmer_gennisis", "Απλό / Μονότιμο", notes="Ημερομηνία γέννησης"),
                Attribute("diefthynsi", "Απλό / Μονότιμο", notes="Διεύθυνση μόνιμης κατοικίας"),
                Attribute("email", "Απλό / Μονότιμο", is_candidate=True, notes="Κύριο email (Candidate Key)"),
                Attribute("loyalty_points", "Απλό / Μονότιμο", notes="Συσσωρευμένοι πόντοι πιστότητας"),
                Attribute("tilefona", "Πλειότιμο", notes="Πολλαπλά τηλέφωνα επικοινωνίας (Πίνακας ΤΗΛΕΦΩΝΟ_ΕΠΙΣΚΕΠΤΗ)"),
            ],
        ),
        Entity(
            name="ΚΡΑΤΗΣΗ (Booking / Reservation)",
            entity_type="Ισχυρή Οντότητα",
            is_weak=False,
            owner_entity=None,
            justification="Αυτοτελής συναλλαγή δέσμευσης δωματίου με μοναδικό κωδικό Booking ID.",
            attributes=[
                Attribute("booking_id", "Απλό / Μονότιμο", is_pk=True, notes="Μοναδικός κωδικός κράτησης (PK)"),
                Attribute("hmer_kratisis", "Απλό / Μονότιμο", notes="Ημερομηνία καταχώρισης κράτησης"),
                Attribute("check_in", "Απλό / Μονότιμο", notes="Ημερομηνία άφιξης"),
                Attribute("check_out", "Απλό / Μονότιμο", notes="Ημερομηνία αναχώρησης"),
                Attribute("arithmos_enilikon", "Απλό / Μονότιμο", notes="Αριθμός ενηλίκων"),
                Attribute("arithmos_paidion", "Απλό / Μονότιμο", notes="Αριθμός ανηλίκων"),
                Attribute("katastasi_kratisis", "Απλό / Μονότιμο", notes="Κατάσταση ('Confirmed', 'Checked-in', 'Completed', 'Cancelled')"),
                Attribute("synoliko_kostos", "Απλό / Μονότιμο", notes="Συνολικό κόστος διαμονής"),
            ],
        ),
        Entity(
            name="ΥΠΑΛΛΗΛΟΣ (Staff / Employee)",
            entity_type="Ισχυρή Οντότητα",
            is_weak=False,
            owner_entity=None,
            justification="Εργαζόμενος του ξενοδοχειακού συγκροτήματος με μοναδικό αριθμό μητρώου (ΑΜΥ).",
            attributes=[
                Attribute("amy", "Απλό / Μονότιμο", is_pk=True, notes="Αριθμός Μητρώου Υπαλλήλου (PK)"),
                Attribute("onomateponymo", "Απλό / Μονότιμο", notes="Ονοματεπώνυμο εργαζομένου"),
                Attribute("eidikotita", "Απλό / Μονότιμο", notes="Ειδικότητα ('Καθαριότητα', 'Συντήρηση', 'Reception', 'Chef')"),
                Attribute("misthos", "Απλό / Μονότιμο", notes="Μηνιαίος μισθός"),
                Attribute("tilefono", "Απλό / Μονότιμο", notes="Τηλέφωνο επικοινωνίας"),
            ],
        ),
        Entity(
            name="ΥΠΗΡΕΣΙΑ (Extra Service)",
            entity_type="Ισχυρή Οντότητα",
            is_weak=False,
            owner_entity=None,
            justification="Κατάλογος παρεχόμενων πρόσθετων υπηρεσιών (Spa, Εκδρομές, Γαστρονομία) με μοναδικό κωδικό υπηρεσίας.",
            attributes=[
                Attribute("service_id", "Απλό / Μονότιμο", is_pk=True, notes="Μοναδικός κωδικός υπηρεσίας (PK)"),
                Attribute("perigrafi", "Απλό / Μονότιμο", notes="Περιγραφή υπηρεσίας"),
                Attribute("timi_monadas", "Απλό / Μονότιμο", notes="Σταθερή τιμή χρέωσης ανά μονάδα"),
            ],
        ),
    ]

    # 3. Relationship Attributes
    relationship_attributes = [
        RelationshipAttribute(
            name="hmer_analipsis",
            relationship_name="ΔΙΕΥΘΥΝΕΙ (ΞΕΝΟΔΟΧΕΙΟ - ΥΠΑΛΛΗΛΟΣ)",
            justification="Ημερομηνία κατά την οποία ο Γενικός Διευθυντής ανέλαβε τη διοίκηση της μονάδας.",
        ),
        RelationshipAttribute(
            name="hmer_elegxou, katastasi_etoimotitas, paratiriseis_vlavon",
            relationship_name="ΕΛΕΓΧΟΣ_ΚΑΘΑΡΙΣΜΟΣ (ΔΩΜΑΤΙΟ - ΥΠΑΛΛΗΛΟΣ)",
            justification="Χρονοσφραγίδα επιθεώρησης, κατάσταση ετοιμότητας ('Καθαρό', 'Υπό Συντήρηση') και τεχνικές παρατηρήσεις.",
        ),
        RelationshipAttribute(
            name="hmer_paroxis, posotita, synoliko_poso",
            relationship_name="ΧΡΕΩΣΗ_ΥΠΗΡΕΣΙΑΣ (ΚΡΑΤΗΣΗ - ΥΠΗΡΕΣΙΑ)",
            justification="Χρονοσφραγίδα παροχής έξτρα υπηρεσίας, ποσότητα και υπολογιζόμενο ποσό χρέωσης στην κράτηση.",
        ),
    ]

    # 4. Keys Analysis Table
    keys_analysis = [
        KeyAnalysisRow(
            entity_name="ΞΕΝΟΔΟΧΕΙΑΚΗ_ΜΟΝΑΔΑ",
            key_count="2 Υποψήφια",
            key_types="Υποψήφια: {hotel_id}, {eponymia}",
            final_pk_selection="hotel_id",
            justification="Σταθερός, συμπαγής κωδικός κατάλληλος για αναφορές εξωτερικών κλειδιών.",
        ),
        KeyAnalysisRow(
            entity_name="ΔΩΜΑΤΙΟ",
            key_count="Ασθενής (1 Μερικό)",
            key_types="Μερικό Κλειδί: {room_number}",
            final_pk_selection="(hotel_id, room_number)",
            justification="Σύνθετο πρωτεύον κλειδί: Foreign Key του ξενοδοχείου + αριθμός δωματίου.",
            is_weak=True,
        ),
        KeyAnalysisRow(
            entity_name="ΕΠΙΣΚΕΠΤΗΣ",
            key_count="2 Υποψήφια",
            key_types="Υποψήφια: {passport_id}, {email}",
            final_pk_selection="passport_id",
            justification="Επίσημο κρατικό ταξιδιωτικό έγγραφο ταυτοποίησης πελάτη σε διεθνή θέρετρα.",
        ),
        KeyAnalysisRow(
            entity_name="ΚΡΑΤΗΣΗ",
            key_count="1 Υποψήφιο",
            key_types="Υποψήφιο: {booking_id}",
            final_pk_selection="booking_id",
            justification="Μοναδικός αριθμός κράτησης συστήματος κρατήσεων (CRS).",
        ),
        KeyAnalysisRow(
            entity_name="ΥΠΑΛΛΗΛΟΣ",
            key_count="1 Υποψήφιο",
            key_types="Υποψήφιο: {amy}",
            final_pk_selection="amy",
            justification="Εσωτερικός αριθμός μητρώου προσωπικού.",
        ),
        KeyAnalysisRow(
            entity_name="ΥΠΗΡΕΣΙΑ",
            key_count="1 Υποψήφιο",
            key_types="Υποψήφιο: {service_id}",
            final_pk_selection="service_id",
            justification="Μοναδικός κωδικός τιμοκαταλόγου υπηρεσιών.",
        ),
    ]

    # 5. Relationships List
    relationships = [
        Relationship(
            letter_id="α",
            name="ΔΙΕΥΘΥΝΕΙ (Manages)",
            connected_entities="ΞΕΝΟΔΟΧΕΙΟ <-> ΥΠΑΛΛΗΛΟΣ",
            cardinality="1:1",
            participation="Ολική για Ξενοδοχείο (1,1), Μερική για Υπάλληλο (0,1)",
            relationship_type="Κανονική Σχέση",
            attributes=["hmer_analipsis"],
            justification="Κάθε ξενοδοχείο διευθύνεται από έναν Γενικό Διευθυντή. Ένας υπάλληλος μπορεί να διευθύνει το πολύ μία μονάδα.",
        ),
        Relationship(
            letter_id="β",
            name="ΑΠΑΣΧΟΛΕΙ (Employs)",
            connected_entities="ΞΕΝΟΔΟΧΕΙΟ <-> ΥΠΑΛΛΗΛΟΣ",
            cardinality="1:N",
            participation="Ολική για Υπάλληλο (1,1), Ολική για Ξενοδοχείο (1,N)",
            relationship_type="Κανονική Σχέση",
            attributes=[],
            justification="Κάθε υπάλληλος εργάζεται σε μία συγκεκριμένη μονάδα. Κάθε μονάδα απασχολεί πολλούς εργαζομένους.",
        ),
        Relationship(
            letter_id="γ",
            name="ΔΙΑΘΕΤΕΙ_ΔΩΜΑΤΙΟ (Has Rooms)",
            connected_entities="ΞΕΝΟΔΟΧΕΙΟ <-> ΔΩΜΑΤΙΟ",
            cardinality="1:N",
            participation="Ολική για Δωμάτιο (1,1), Ολική για Ξενοδοχείο (1,N)",
            relationship_type="Ταυτοποιούσα Σχέση (Identifying)",
            attributes=[],
            justification="Ταυτοποιούσα σχέση της ασθενούς οντότητας ΔΩΜΑΤΙΟ από το ΞΕΝΟΔΟΧΕΙΟ.",
        ),
        Relationship(
            letter_id="δ",
            name="ΠΡΑΓΜΑΤΟΠΟΙΕΙ_ΚΡΑΤΗΣΗ (Makes Booking)",
            connected_entities="ΕΠΙΣΚΕΠΤΗΣ <-> ΚΡΑΤΗΣΗ",
            cardinality="1:N",
            participation="Ολική για Κράτηση (1,1), Μερική για Επισκέπτη (0,N)",
            relationship_type="Κανονική Σχέση",
            attributes=[],
            justification="Κάθε κράτηση ανήκει σε έναν πελάτη. Ένας επισκέπτης μπορεί να πραγματοποιήσει πολλαπλές κρατήσεις.",
        ),
        Relationship(
            letter_id="ε",
            name="ΔΕΣΜΕΥΕΙ_ΔΩΜΑΤΙΟ (Reserves Room)",
            connected_entities="ΔΩΜΑΤΙΟ <-> ΚΡΑΤΗΣΗ",
            cardinality="1:N",
            participation="Ολική για Κράτηση (1,1), Μερική για Δωμάτιο (0,N)",
            relationship_type="Κανονική Σχέση",
            attributes=[],
            justification="Κάθε κράτηση δεσμεύει ένα συγκεκριμένο δωμάτιο. Ένα δωμάτιο δεσμεύεται σε πολλές κρατήσεις διαφορετικών χρονικών περιόδων.",
        ),
        Relationship(
            letter_id="στ",
            name="ΕΛΕΓΧΟΣ_ΚΑΘΑΡΙΣΜΟΣ (Room Inspection)",
            connected_entities="ΔΩΜΑΤΙΟ <-> ΥΠΑΛΛΗΛΟΣ",
            cardinality="N:M",
            participation="Μερική για Δωμάτιο (0,N), Μερική για Υπάλληλο (0,N)",
            relationship_type="Κανονική Σχέση (Junction)",
            attributes=["hmer_elegxou", "katastasi_etoimotitas", "paratiriseis_vlavon"],
            justification="Το προσωπικό καθαριότητας/συντήρησης εκτελεί ελέγχους σε πολλαπλά δωμάτια και κάθε δωμάτιο ελέγχεται επανειλημμένα.",
        ),
        Relationship(
            letter_id="ζ",
            name="ΧΡΕΩΣΗ_ΥΠΗΡΕΣΙΑΣ (Service Usage)",
            connected_entities="ΚΡΑΤΗΣΗ <-> ΥΠΗΡΕΣΙΑ",
            cardinality="N:M",
            participation="Μερική για Κράτηση (0,N), Μερική για Υπηρεσία (0,N)",
            relationship_type="Κανονική Σχέση (Junction)",
            attributes=["hmer_paroxis", "posotita", "synoliko_poso"],
            justification="Μια κράτηση μπορεί να χρεωθεί με πολλαπλές υπηρεσίες και μια υπηρεσία παρέχεται σε πολλές κρατήσεις.",
        ),
    ]

    # 6. Design Assumptions
    assumptions = [
        "Ο Γενικός Διευθυντής είναι εγγεγραμμένος στον πίνακα ΥΠΑΛΛΗΛΟΣ και συνδέεται μέσω manager_amy στο ΞΕΝΟΔΟΧΕΙΟ με UNIQUE constraint.",
        "Κάθε κράτηση αφορά δέσμευση ενός δωματίου. Αν ένας πελάτης επιθυμεί πολλαπλά δωμάτια, εκδίδονται αντίστοιχες κρατήσεις.",
        "Οι παροχές (amenities) ξενοδοχείου και τα τηλέφωνα επισκεπτών αποθηκεύονται σε ξεχωριστούς πίνακες 1:N για την επίτευξη 1NF.",
        "Οι χρεώσεις υπηρεσιών συνδέονται με τον κωδικό κράτησης για ενιαία τιμολόγηση κατά το Check-out.",
    ]

    # 7. ER Diagram Tables
    er_tables = [
        ERTable(
            id="t-resort",
            label="XENODOXEIO",
            x=50,
            y=50,
            attrs=[
                ERTableAttr("hotel_id", pk=True),
                ERTableAttr("eponymia"),
                ERTableAttr("asteria"),
                ERTableAttr("geografiki_perioxi"),
                ERTableAttr("poli"),
                ERTableAttr("diefthynsi"),
                ERTableAttr("email"),
                ERTableAttr("manager_amy", fk=True),
                ERTableAttr("appointment_date"),
            ],
        ),
        ERTable(
            id="t-amenities",
            label="PAROXES_XENODOXEIOU",
            x=50,
            y=370,
            attrs=[
                ERTableAttr("hotel_id", pk=True, fk=True),
                ERTableAttr("paroxi", pk=True),
            ],
        ),
        ERTable(
            id="t-room",
            label="DOMATIO",
            x=450,
            y=50,
            attrs=[
                ERTableAttr("hotel_id", pk=True, fk=True),
                ERTableAttr("room_number", pk=True),
                ERTableAttr("orofos"),
                ERTableAttr("typos_domatiou"),
                ERTableAttr("xoritikotita"),
                ERTableAttr("vasiki_timi"),
                ERTableAttr("thea"),
            ],
        ),
        ERTable(
            id="t-inspection",
            label="ELEGXOS_DOMATIOU",
            x=450,
            y=340,
            attrs=[
                ERTableAttr("hotel_id", pk=True, fk=True),
                ERTableAttr("room_number", pk=True, fk=True),
                ERTableAttr("amy", pk=True, fk=True),
                ERTableAttr("hmer_elegxou", pk=True),
                ERTableAttr("katastasi_etoimotitas"),
                ERTableAttr("paratiriseis_vlavon"),
            ],
        ),
        ERTable(
            id="t-employee",
            label="YPALLILOS",
            x=850,
            y=340,
            attrs=[
                ERTableAttr("amy", pk=True),
                ERTableAttr("onomateponymo"),
                ERTableAttr("eidikotita"),
                ERTableAttr("misthos"),
                ERTableAttr("tilefono"),
                ERTableAttr("hotel_id", fk=True),
            ],
        ),
        ERTable(
            id="t-guest",
            label="EPISKEPTIS",
            x=850,
            y=50,
            attrs=[
                ERTableAttr("passport_id", pk=True),
                ERTableAttr("onomateponymo"),
                ERTableAttr("ethnikotita"),
                ERTableAttr("hmer_gennisis"),
                ERTableAttr("diefthynsi"),
                ERTableAttr("email"),
                ERTableAttr("loyalty_points"),
            ],
        ),
        ERTable(
            id="t-guest-phone",
            label="TILEFONO_EPISKEPTI",
            x=850,
            y=600,
            attrs=[
                ERTableAttr("passport_id", pk=True, fk=True),
                ERTableAttr("tilefono", pk=True),
            ],
        ),
        ERTable(
            id="t-booking",
            label="KRATISI",
            x=450,
            y=600,
            attrs=[
                ERTableAttr("booking_id", pk=True),
                ERTableAttr("hmer_kratisis"),
                ERTableAttr("check_in"),
                ERTableAttr("check_out"),
                ERTableAttr("arithmos_enilikon"),
                ERTableAttr("arithmos_paidion"),
                ERTableAttr("katastasi_kratisis"),
                ERTableAttr("synoliko_kostos"),
                ERTableAttr("passport_id", fk=True),
                ERTableAttr("hotel_id", fk=True),
                ERTableAttr("room_number", fk=True),
            ],
        ),
        ERTable(
            id="t-service",
            label="YPIRESIA",
            x=50,
            y=500,
            attrs=[
                ERTableAttr("service_id", pk=True),
                ERTableAttr("perigrafi"),
                ERTableAttr("timi_monadas"),
            ],
        ),
        ERTable(
            id="t-service-charge",
            label="XREOSI_YPIRESIAS",
            x=50,
            y=660,
            attrs=[
                ERTableAttr("booking_id", pk=True, fk=True),
                ERTableAttr("service_id", pk=True, fk=True),
                ERTableAttr("hmer_paroxis", pk=True),
                ERTableAttr("posotita"),
                ERTableAttr("synoliko_poso"),
            ],
        ),
    ]

    # 8. ER Diagram Edges
    er_edges = [
        # Resort directs Employee (1:1)
        EREdge("M 310 80 L 850 360", "start-one", "end-one", "ΔΙΕΥΘΥΝΕΙ (1:1)", 550, 240),
        # Resort employs Employees (1:N)
        EREdge("M 310 120 L 850 400", "start-one", "end-many", "ΑΠΑΣΧΟΛΕΙ (1:N)", 550, 280),
        # Resort has Rooms (1:N identifying)
        EREdge("M 310 100 L 450 100", "start-one", "end-many", "ΔΙΑΘΕΤΕΙ (1:N)", 380, 90),
        # Resort has Amenities (1:N multi-value)
        EREdge("M 180 350 L 180 370", "start-one", "end-many", "ΠΑΡΟΧΗ (1:N)", 195, 360),
        # Room to Inspection (1:N)
        EREdge("M 580 294 L 580 340", "start-one", "end-many", "ΕΛΕΓΧΟΣ (1:N)", 595, 315),
        # Employee to Inspection (1:N)
        EREdge("M 850 370 L 710 370", "start-one", "end-many", "ΕΚΤΕΛΕΙ (1:N)", 780, 360),
        # Room to Booking (1:N)
        EREdge("M 580 556 L 580 600", "start-one", "end-many", "ΔΕΣΜΕΥΕΤΑΙ (1:N)", 595, 575),
        # Guest to Booking (1:N)
        EREdge("M 850 200 L 710 650", "start-one", "end-many", "ΠΡΑΓΜΑΤΟΠΟΙΕΙ (1:N)", 780, 520),
        # Guest to Phone (1:N)
        EREdge("M 980 294 L 980 600", "start-one", "end-many", "ΤΗΛΕΦΩΝΟ (1:N)", 995, 460),
        # Booking to Service Charge (1:N)
        EREdge("M 450 680 L 310 680", "start-one", "end-many", "ΧΡΕΩΣΗ (1:N)", 380, 670),
        # Service to Service Charge (1:N)
        EREdge("M 180 632 L 180 660", "start-one", "end-many", "ΠΑΡΕΧΕΤΑΙ (1:N)", 195, 645),
    ]

    # 9. Relational Conversion Justifications
    relational_justifications = [
        RelationalJustification(
            title="1. Μετατροπή Ισχυρών Οντοτήτων (ΞΕΝΟΔΟΧΕΙΟ, ΕΠΙΣΚΕΠΤΗΣ, ΚΡΑΤΗΣΗ, ΥΠΑΛΛΗΛΟΣ, ΥΠΗΡΕΣΙΑ)",
            color_class="border-blue-500",
            description="Κάθε ισχυρή οντότητα μετατρέπεται σε αυτοτελή πίνακα με πρωτεύον κλειδί το αντίστοιχο κύριο υποψήφιο κλειδί (hotel_id, passport_id, booking_id, amy, service_id).",
        ),
        RelationalJustification(
            title="2. Μετατροπή Ασθενούς Οντότητας (ΔΩΜΑΤΙΟ)",
            color_class="border-red-500",
            description="Ο πίνακας DOMATIO περιλαμβάνει το Foreign Key hotel_id του ξενοδοχείου και το μερικό κλειδί room_number, σχηματίζοντας σύνθετο πρωτεύον κλειδί: PRIMARY KEY (hotel_id, room_number) με ON DELETE CASCADE.",
        ),
        RelationalJustification(
            title="3. Μετατροπή Συσχετίσεων 1:1 και 1:N (ΔΙΕΥΘΥΝΕΙ, ΑΠΑΣΧΟΛΕΙ, ΠΡΑΓΜΑΤΟΠΟΙΕΙ, ΔΕΣΜΕΥΕΙ)",
            color_class="border-emerald-500",
            description="Στη σχέση 1:1 ΔΙΕΥΘΥΝΕΙ το manager_amy εισάγεται στο XENODOXEIO με UNIQUE constraint. Στις σχέσεις 1:N τα αντίστοιχα κλειδιά (passport_id, composite hotel_id + room_number) εισάγονται ως Foreign Keys στον πίνακα KRATISI.",
        ),
        RelationalJustification(
            title="4. Μετατροπή Συσχετίσεων N:M (ΕΛΕΓΧΟΣ_ΚΑΘΑΡΙΣΜΟΣ, ΧΡΕΩΣΗ_ΥΠΗΡΕΣΙΑΣ)",
            color_class="border-amber-500",
            description="Δημιουργούνται οι πίνακες ELEGXOS_DOMATIOU (με σύνθετο PK: hotel_id, room_number, amy, hmer_elegxou) και XREOSI_YPIRESIAS (με σύνθετο PK: booking_id, service_id, hmer_paroxis).",
        ),
        RelationalJustification(
            title="5. Μετατροπή Πλειότιμων Γνωρισμάτων (ΠΑΡΟΧΕΣ, ΤΗΛΕΦΩΝΑ)",
            color_class="border-purple-500",
            description="Τα πλειότιμα γνωρίσματα αποθηκεύονται στους πίνακες PAROXES_XENODOXEIOU (hotel_id, paroxi) και TILEFONO_EPISKEPTI (passport_id, tilefono) με Foreign Keys και ON DELETE CASCADE.",
        ),
    ]

    # 10. Complete Production SQL DDL
    sql_ddl = """-- ==========================================================
-- PostgreSQL / MySQL Relational Schema for Hotel Resort System
-- Case Study: Exam Paper 5 (Ξενοδοχειακά Συγκροτήματα & Θέρετρα)
-- ==========================================================

-- 1. Entity: YPALLILOS (Pre-created for foreign keys)
CREATE TABLE YPALLILOS (
    amy VARCHAR(15) PRIMARY KEY,
    onomateponymo VARCHAR(100) NOT NULL,
    eidikotita VARCHAR(50) NOT NULL CHECK (eidikotita IN ('Καθαριότητα', 'Συντήρηση', 'Reception', 'Chef', 'Διοίκηση')),
    misthos DECIMAL(10, 2) NOT NULL CHECK (misthos > 0),
    tilefono VARCHAR(20) NOT NULL,
    hotel_id VARCHAR(10)
);

-- 2. Entity: XENODOXEIO
CREATE TABLE XENODOXEIO (
    hotel_id VARCHAR(10) PRIMARY KEY,
    eponymia VARCHAR(100) NOT NULL UNIQUE,
    asteria INT NOT NULL CHECK (asteria BETWEEN 1 AND 5),
    geografiki_perioxi VARCHAR(50) NOT NULL,
    poli VARCHAR(50) NOT NULL,
    diefthynsi VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    manager_amy VARCHAR(15) NOT NULL UNIQUE,
    appointment_date DATE NOT NULL,
    FOREIGN KEY (manager_amy) REFERENCES YPALLILOS(amy)
);

-- Add foreign key constraint for employee's workplace
ALTER TABLE YPALLILOS
ADD CONSTRAINT fk_emp_hotel
FOREIGN KEY (hotel_id) REFERENCES XENODOXEIO(hotel_id);

-- 3. Multi-valued Attribute: PAROXES_XENODOXEIOU
CREATE TABLE PAROXES_XENODOXEIOU (
    hotel_id VARCHAR(10) NOT NULL,
    paroxi VARCHAR(100) NOT NULL,
    PRIMARY KEY (hotel_id, paroxi),
    FOREIGN KEY (hotel_id) REFERENCES XENODOXEIO(hotel_id) ON DELETE CASCADE
);

-- 4. Weak Entity: DOMATIO
CREATE TABLE DOMATIO (
    hotel_id VARCHAR(10) NOT NULL,
    room_number VARCHAR(10) NOT NULL,
    orofos INT NOT NULL,
    typos_domatiou VARCHAR(50) NOT NULL CHECK (typos_domatiou IN ('Standard Double', 'Deluxe Suite', 'Family Villa', 'Superior Room')),
    xoritikotita INT NOT NULL CHECK (xoritikotita > 0),
    vasiki_timi DECIMAL(10, 2) NOT NULL CHECK (vasiki_timi > 0),
    thea VARCHAR(50) NOT NULL CHECK (thea IN ('Θέα Θάλασσα', 'Θέα Κήπος', 'Θέα Βουνό', 'Θέα Πισίνα')),
    PRIMARY KEY (hotel_id, room_number),
    FOREIGN KEY (hotel_id) REFERENCES XENODOXEIO(hotel_id) ON DELETE CASCADE
);

-- 5. Entity: EPISKEPTIS
CREATE TABLE EPISKEPTIS (
    passport_id VARCHAR(20) PRIMARY KEY,
    onomateponymo VARCHAR(100) NOT NULL,
    ethnikotita VARCHAR(50) NOT NULL,
    hmer_gennisis DATE NOT NULL,
    diefthynsi VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    loyalty_points INT DEFAULT 0 CHECK (loyalty_points >= 0)
);

-- 6. Multi-valued Attribute: TILEFONO_EPISKEPTI
CREATE TABLE TILEFONO_EPISKEPTI (
    passport_id VARCHAR(20) NOT NULL,
    tilefono VARCHAR(20) NOT NULL,
    PRIMARY KEY (passport_id, tilefono),
    FOREIGN KEY (passport_id) REFERENCES EPISKEPTIS(passport_id) ON DELETE CASCADE
);

-- 7. Entity: KRATISI
CREATE TABLE KRATISI (
    booking_id VARCHAR(20) PRIMARY KEY,
    hmer_kratisis DATE NOT NULL,
    check_in DATE NOT NULL,
    check_out DATE NOT NULL,
    arithmos_enilikon INT NOT NULL CHECK (arithmos_enilikon > 0),
    arithmos_paidion INT DEFAULT 0 CHECK (arithmos_paidion >= 0),
    katastasi_kratisis VARCHAR(30) NOT NULL CHECK (katastasi_kratisis IN ('Confirmed', 'Checked-in', 'Completed', 'Cancelled')),
    synoliko_kostos DECIMAL(10, 2) NOT NULL CHECK (synoliko_kostos >= 0),
    passport_id VARCHAR(20) NOT NULL,
    hotel_id VARCHAR(10) NOT NULL,
    room_number VARCHAR(10) NOT NULL,
    CHECK (check_out > check_in),
    FOREIGN KEY (passport_id) REFERENCES EPISKEPTIS(passport_id) ON DELETE CASCADE,
    FOREIGN KEY (hotel_id, room_number) REFERENCES DOMATIO(hotel_id, room_number)
);

-- 8. Entity: YPIRESIA
CREATE TABLE YPIRESIA (
    service_id VARCHAR(15) PRIMARY KEY,
    perigrafi VARCHAR(150) NOT NULL,
    timi_monadas DECIMAL(8, 2) NOT NULL CHECK (timi_monadas >= 0)
);

-- 9. Junction Table: ELEGXOS_DOMATIOU (N:M)
CREATE TABLE ELEGXOS_DOMATIOU (
    hotel_id VARCHAR(10) NOT NULL,
    room_number VARCHAR(10) NOT NULL,
    amy VARCHAR(15) NOT NULL,
    hmer_elegxou TIMESTAMP NOT NULL,
    katastasi_etoimotitas VARCHAR(30) NOT NULL CHECK (katastasi_etoimotitas IN ('Έτοιμο', 'Υπό Καθαρισμό', 'Εκτός Λειτουργίας', 'Επισκευάστηκε')),
    paratiriseis_vlavon TEXT,
    PRIMARY KEY (hotel_id, room_number, amy, hmer_elegxou),
    FOREIGN KEY (hotel_id, room_number) REFERENCES DOMATIO(hotel_id, room_number) ON DELETE CASCADE,
    FOREIGN KEY (amy) REFERENCES YPALLILOS(amy) ON DELETE CASCADE
);

-- 10. Junction Table: XREOSI_YPIRESIAS (N:M)
CREATE TABLE XREOSI_YPIRESIAS (
    booking_id VARCHAR(20) NOT NULL,
    service_id VARCHAR(15) NOT NULL,
    hmer_paroxis TIMESTAMP NOT NULL,
    posotita INT NOT NULL DEFAULT 1 CHECK (posotita > 0),
    synoliko_poso DECIMAL(10, 2) NOT NULL CHECK (synoliko_poso >= 0),
    PRIMARY KEY (booking_id, service_id, hmer_paroxis),
    FOREIGN KEY (booking_id) REFERENCES KRATISI(booking_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES YPIRESIA(service_id)
);"""

    return Scenario(
        id="hotel_management",
        title="Σύστημα Διαχείρισης Ξενοδοχειακών Συγκροτημάτων & Θερέτρων",
        subtitle="Μοντελοποίηση Μονάδων, Δωματίων, Επισκεπτών, Κρατήσεων, Προσωπικού & Επιπλέον Υπηρεσιών",
        course_tag="Βάσεις Δεδομένων (Πρόοδος 2025-2026 - Θέμα 5)",
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
