"""Hospital Management case study scenario module.

Contains the complete parsed and modeled ER analysis for the University Hospital
Management Information System (Clinics, Doctors, Dependents, Patients, Admissions, Medications),
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


def createHospitalManagementScenario() -> Scenario:
    """Constructs and returns the Hospital Management database scenario.

    Returns:
        Scenario: Fully populated scenario instance.
    """
    # 1. Text Paragraphs with Interactive Segments
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Ένα μεγάλο Πανεπιστημιακό Νοσοκομειακό Ίδρυμα επιθυμεί να αναπτύξει ένα σύγχρονο Σύστημα Διαχείρισης Βάσεων Δεδομένων (ΣΔΒΔ) για την ολοκληρωμένη παρακολούθηση των "),
                TextSegment(
                    text="κλινικών",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Strong Entity): Αυτοτελής ιατρική μονάδα με μοναδικό κωδικό κλινικής.",
                ),
                TextSegment(text=", του "),
                TextSegment(
                    text="ιατρικού προσωπικού",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Strong Entity): Φυσικό πρόσωπο ιατρού με μοναδικό ΑΜΙ και ΑΦΜ.",
                ),
                TextSegment(text=", των "),
                TextSegment(
                    text="ασθενών",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Strong Entity): Φυσικό πρόσωπο ασθενούς με μοναδικό ΑΜΚΑ.",
                ),
                TextSegment(text=", των "),
                TextSegment(
                    text="νοσηλειών",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΑΣΘΕΝΗΣ ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-weak",
                    tooltip="Ασθενής Οντότητα (Weak Entity): Περιστατικό εισαγωγής εξαρτώμενο υπαρκτικά από τον ασθενή.",
                ),
                TextSegment(text=" και των χορηγούμενων θεραπειών."),
            ],
            accent_border_color=None,
        ),
        Paragraph(
            segments=[
                TextSegment(text="1. <strong>Κλινικές (Clinics):</strong> Κάθε κλινική χαρακτηρίζεται από έναν "),
                TextSegment(
                    text="μοναδικό κωδικό κλινικής (π.χ. K01, K02)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Μοναδικός τεχνητός κωδικός κλινικής.",
                ),
                TextSegment(text=", μια "),
                TextSegment(
                    text="μοναδική ονομασία (π.χ. 'Καρδιολογική')",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Υποψήφιο Κλειδί (Candidate Key): Εναλλακτικό μοναδικό αναγνωριστικό όνομα κλινικής.",
                ),
                TextSegment(text=", τον "),
                TextSegment(text="όροφο", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" στον οποίο στεγάζεται και το "),
                TextSegment(text="τηλέφωνο γραμματείας", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=". Κάθε κλινική "),
                TextSegment(
                    text="διευθύνεται",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ 1:1",
                    badge_class="badge-rel",
                    tooltip="Σχέση 1:1 (Κλινική - Ιατρός): Ολική συμμετοχή κλινικής, μερική συμμετοχή ιατρού.",
                ),
                TextSegment(text=" υποχρεωτικά από έναν συγκεκριμένο ιατρό (Διευθυντής Κλινικής), για τον οποίο καταγράφεται η "),
                TextSegment(
                    text="ημερομηνία ανάληψης της διεύθυνσης",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ ΣΧΕΣΗΣ",
                    badge_class="badge-attr-simple",
                    tooltip="Γνώρισμα Σχέσης: Περιγράφει πότε ανέλαβε καθήκοντα διευθυντή ο ιατρός στη συγκεκριμένη κλινική.",
                ),
                TextSegment(text=". Ένας ιατρός μπορεί να διευθύνει το πολύ μία κλινική. Επιπλέον, κάθε κλινική μπορεί να διαθέτει "),
                TextSegment(
                    text="εξειδικευμένες πτέρυγες/εγκαταστάσεις σε διάφορα κτίρια (πολλαπλές τοποθεσίες)",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΠΛΕΙΟΤΙΜΟ",
                    badge_class="badge-attr-multi",
                    tooltip="Πλειότιμο Γνώρισμα (Multi-valued): Μία κλινική μπορεί να εκτείνεται σε πολλές πτέρυγες.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-blue-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="2. <strong>Ιατρικό Προσωπικό (Doctors):</strong> Για κάθε ιατρό καταγράφονται τα εξής στοιχεία: "),
                TextSegment(
                    text="μοναδικός αριθμός ιατρικού μητρώου (ΑΜΙ)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Μοναδικός αριθμός επαγγελματικού μητρώου ιατρού.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="Αριθμός Φορολογικού Μητρώου (ΑΦΜ)",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Υποψήφιο Κλειδί (Candidate Key): Κρατικό μοναδικό φορολογικό αναγνωριστικό.",
                ),
                TextSegment(text=", "),
                TextSegment(text="όνομα", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="επώνυμο", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="ειδικότητα", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="βαθμίδα (π.χ. Επιμελητής Α', Διευθυντής)", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="μηνιαίος βασικός μισθός", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="ημερομηνία πρόσληψης", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και "),
                TextSegment(
                    text="διεύθυνση κατοικίας (οδός, αριθμός, ΤΚ, πόλη)",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΣΥΝΘΕΤΟ",
                    badge_class="badge-attr-composite",
                    tooltip="Σύνθετο Γνώρισμα (Composite): Διασπάται σε Οδός, Αριθμός, ΤΚ και Πόλη.",
                ),
                TextSegment(text=". Ένας ιατρός μπορεί να διαθέτει "),
                TextSegment(
                    text="περισσότερα από ένα τηλέφωνα επικοινωνίας (π.χ. εσωτερικό, κινητό)",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΠΛΕΙΟΤΙΜΟ",
                    badge_class="badge-attr-multi",
                    tooltip="Πλειότιμο Γνώρισμα (Multi-valued): Ένας ιατρός μπορεί να έχει πολλαπλά τηλέφωνα.",
                ),
                TextSegment(text=". Κάθε ιατρός "),
                TextSegment(
                    text="ανήκει υποχρεωτικά σε μία και μόνο κλινική",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ 1:N",
                    badge_class="badge-rel",
                    tooltip="Σχέση 1:N (Κλινική -> Ιατρός): Ολική συμμετοχή ιατρού, μία κλινική απασχολεί πολλούς ιατρούς.",
                ),
                TextSegment(text=", ενώ σε κάθε κλινική υπηρετούν πολλοί ιατροί. Επιπλέον, ένας έμπειρος ιατρός μπορεί να "),
                TextSegment(
                    text="επιβλέπει και να καθοδηγεί",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΑΝΑΔΡΟΜΙΚΗ 1:N",
                    badge_class="badge-rel",
                    tooltip="Αναδρομική Σχέση 1:N (Ιατρός-Επόπτης -> Ιατρός-Ειδικευόμενος): Κάθε ειδικευόμενος έχει 1 επόπτη.",
                ),
                TextSegment(text=" νεότερους ειδικευόμενους ιατρούς."),
            ],
            accent_border_color="border-emerald-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="3. <strong>Εξαρτώμενα Μέλη (Dependents):</strong> Για ασφαλιστικούς και φορολογικούς λόγους, το ίδρυμα καταγράφει τα "),
                TextSegment(
                    text="εξαρτώμενα μέλη",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΑΣΘΕΝΗΣ ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-weak",
                    tooltip="Ασθενής Οντότητα (Weak Entity): Εξαρτάται υπαρκτικά από τον Ιατρό και δεν διαθέτει αυτόνομο PK.",
                ),
                TextSegment(text=" της οικογένειας των ιατρών. Για κάθε εξαρτώμενο μέλος τηρούνται: το "),
                TextSegment(
                    text="μικρό όνομα",
                    is_highlight=True,
                    category="key",
                    tag_label="PARTIAL KEY",
                    badge_class="badge-key-partial",
                    tooltip="Μερικό Κλειδί (Partial Key / Discriminator): Μοναδικό μόνο στα πλαίσια της οικογένειας του ιατρού.",
                ),
                TextSegment(text=", το "),
                TextSegment(text="φύλο", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(text="ημερομηνία γέννησης", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και η "),
                TextSegment(text="συγγενική σχέση (π.χ. τέκνο, σύζυγος)", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text="."),
            ],
            accent_border_color="border-purple-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="4. <strong>Ασθενείς (Patients):</strong> Για κάθε ασθενή καταγράφονται: ο "),
                TextSegment(
                    text="μοναδικός ΑΜΚΑ",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Μοναδικός Αριθμός Μητρώου Κοινωνικής Ασφάλισης.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="Αριθμός Ταυτότητας (ΑΔΤ)",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Υποψήφιο Κλειδί (Candidate Key): Κρατικό αναγνωριστικό αστυνομικής ταυτότητας.",
                ),
                TextSegment(text=", "),
                TextSegment(text="όνομα", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="επώνυμο", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="ημερομηνία γέννησης", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="φύλο", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="ομάδα αίματος", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και η "),
                TextSegment(
                    text="τρέχουσα ηλικία του (υπολογίζεται δυναμικά)",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΠΑΡΑΓΩΓΟ",
                    badge_class="badge-attr-derived",
                    tooltip="Παράγωγο Γνώρισμα (Derived Attribute): Υπολογίζεται από την τρέχουσα ημερομηνία και την ημερομηνία γέννησης.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-amber-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="5. <strong>Εισαγωγές / Νοσηλείες (Admissions):</strong> Κάθε φορά που ένας ασθενής εισάγεται στο νοσοκομείο, καταγράφεται ένα νέο περιστατικό νοσηλείας. Για κάθε νοσηλεία καταγράφεται ένας "),
                TextSegment(
                    text="αύξων αριθμός εισαγωγής για τον συγκεκριμένο ασθενή",
                    is_highlight=True,
                    category="key",
                    tag_label="PARTIAL KEY",
                    badge_class="badge-key-partial",
                    tooltip="Μερικό Κλειδί (Partial Key): Αριθμεί διαδοχικά τις νοσηλείες του ίδιου ασθενούς (1, 2, 3...).",
                ),
                TextSegment(text=", η "),
                TextSegment(text="ημερομηνία και ώρα εισαγωγής", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(text="ημερομηνία και ώρα εξιτηρίου", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", ο "),
                TextSegment(text="αριθμός θαλάμου", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(text="αρχική διάγνωση", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και η "),
                TextSegment(
                    text="κλινική στην οποία πραγματοποιείται η νοσηλεία",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ 1:N",
                    badge_class="badge-rel",
                    tooltip="Σχέση 1:N (Κλινική -> Νοσηλεία): Κάθε νοσηλεία φιλοξενείται σε 1 κλινική.",
                ),
                TextSegment(text=". Ένας ασθενής μπορεί να έχει πραγματοποιήσει πολλαπλές νοσηλείες στην πορεία του χρόνου, αλλά κάθε νοσηλεία "),
                TextSegment(
                    text="αφορά αποκλειστικά έναν ασθενή",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΤΑΥΤΟΠΟΙΟΥΣΑ 1:N",
                    badge_class="badge-rel",
                    tooltip="Ταυτοποιούσα Σχέση 1:N (Ασθενής -> Νοσηλεία): Ολική υπαρκτική εξάρτηση νοσηλείας από τον ασθενή.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-cyan-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="6. <strong>Θεραπευτικές Αγωγές & Φάρμακα (Treatments & Medications):</strong> Το νοσοκομείο διαθέτει κατάλογο "),
                TextSegment(
                    text="φαρμάκων",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Strong Entity): Φαρμακευτικό σκεύασμα με μοναδικό εθνικό κωδικό ΕΟΦ.",
                ),
                TextSegment(text=". Κάθε φάρμακο έχει "),
                TextSegment(
                    text="μοναδικό εθνικό κωδικό φαρμάκου (ΕΟΦ)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Μοναδικός κωδικός Εθνικού Οργανισμού Φαρμάκων.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="εμπορική ονομασία",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Υποψήφιο Κλειδί (Candidate Key): Μοναδική εμπορική ονομασία σκευάσματος.",
                ),
                TextSegment(text=", "),
                TextSegment(text="δραστική ουσία", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και "),
                TextSegment(text="μονάδα μέτρησης (π.χ. mg, ml)", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=". Στα πλαίσια μιας νοσηλείας, ένας θεράπων ιατρός "),
                TextSegment(
                    text="συνταγογραφεί και χορηγεί φάρμακα",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ N:M",
                    badge_class="badge-rel",
                    tooltip="Συσχετιστική Οντότητα / Σχέση N:M (Νοσηλεία <-> Φάρμακο με αναφορά θεράποντος ιατρού).",
                ),
                TextSegment(text=" στον νοσηλευόμενο ασθενή. Για κάθε χορήγηση φαρμάκου καταγράφονται: η "),
                TextSegment(
                    text="δοσολογία",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ ΣΧΕΣΗΣ",
                    badge_class="badge-attr-simple",
                    tooltip="Γνώρισμα Σχέσης / Συνδετικού Πίνακα: Ποσότητα χορήγησης.",
                ),
                TextSegment(text=", η "),
                TextSegment(
                    text="συχνότητα λήψης ανά 24ωρο",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ ΣΧΕΣΗΣ",
                    badge_class="badge-attr-simple",
                    tooltip="Γνώρισμα Σχέσης / Συνδετικού Πίνακα: Συχνότητα δόσεων.",
                ),
                TextSegment(text=", η "),
                TextSegment(
                    text="ημερομηνία έναρξης",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ ΣΧΕΣΗΣ",
                    badge_class="badge-attr-simple",
                    tooltip="Γνώρισμα Σχέσης / Συνδετικού Πίνακα: Ημερομηνία έναρξης αγωγής.",
                ),
                TextSegment(text=" και η "),
                TextSegment(
                    text="ημερομηνία λήξης της αγωγής",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ ΣΧΕΣΗΣ",
                    badge_class="badge-attr-simple",
                    tooltip="Γνώρισμα Σχέσης / Συνδετικού Πίνακα: Ημερομηνία ολοκλήρωσης αγωγής.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-rose-500",
        ),
    ]

    # 2. Entities & Attributes
    entities = [
        Entity(
            name="ΚΛΙΝΙΚΗ",
            entity_type="Ισχυρή Οντότητα (Strong Entity)",
            is_weak=False,
            justification="Αυτοτελής διοικητική και νοσηλευτική μονάδα με πρωτεύον κλειδί τον Κωδικό_Κλινικής.",
            attributes=[
                Attribute(name="Κωδικός_Κλινικής", attr_type="Απλό, Μονότιμο, Primary Key", is_pk=True),
                Attribute(name="Όνομα_Κλινικής", attr_type="Απλό, Μονότιμο, Candidate Key", is_candidate=True),
                Attribute(name="Όροφος", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Τηλέφωνο_Γραμματείας", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Πτέρυγες_Εγκαταστάσεις", attr_type="Πλειότιμο (Multi-valued)", notes="Εξάγεται σε ξεχωριστό πίνακα ΠΤΕΡΥΓΑ_ΚΛΙΝΙΚΗΣ"),
            ],
        ),
        Entity(
            name="ΙΑΤΡΟΣ",
            entity_type="Ισχυρή Οντότητα (Strong Entity)",
            is_weak=False,
            justification="Φυσικό πρόσωπο ιατρικού προσωπικού με μοναδικό αναγνωριστικό τον ΑΜΙ και ΑΦΜ.",
            attributes=[
                Attribute(name="ΑΜΙ", attr_type="Απλό, Μονότιμο, Primary Key", is_pk=True),
                Attribute(name="ΑΦΜ", attr_type="Απλό, Μονότιμο, Candidate Key", is_candidate=True),
                Attribute(name="Όνομα", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Επώνυμο", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Ειδικότητα", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Βαθμίδα", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Βασικός_Μισθός", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Ημερ_Πρόσληψης", attr_type="Απλό, Μονότιμο"),
                Attribute(
                    name="Διεύθυνση_Κατοικίας",
                    attr_type="Σύνθετο (Composite)",
                    components=["Οδός", "Αριθμός", "ΤΚ", "Πόλη"],
                ),
                Attribute(name="Τηλέφωνα_Επικοινωνίας", attr_type="Πλειότιμο (Multi-valued)", notes="Εξάγεται σε ξεχωριστό πίνακα ΤΗΛΕΦΩΝΟ_ΙΑΤΡΟΥ"),
            ],
        ),
        Entity(
            name="ΕΞΑΡΤΩΜΕΝΟ_ΜΕΛΟΣ",
            entity_type="Ασθενής Οντότητα (Weak Entity)",
            is_weak=True,
            owner_entity="ΙΑΤΡΟΣ",
            justification="Εξαρτάται υπαρκτικά από τον Ιατρό. Ταυτοποιείται συνδυαστικά με το FK του Ιατρού και το Όνομα Μέλους.",
            attributes=[
                Attribute(name="Όνομα_Μέλους", attr_type="Απλό, Μερικό Κλειδί (Partial Key)", is_partial=True),
                Attribute(name="Φύλο", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Ημερ_Γέννησης", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Συγγενική_Σχέση", attr_type="Απλό, Μονότιμο"),
            ],
        ),
        Entity(
            name="ΑΣΘΕΝΗΣ",
            entity_type="Ισχυρή Οντότητα (Strong Entity)",
            is_weak=False,
            justification="Φυσικό πρόσωπο λήπτη υπηρεσιών υγείας με μοναδικό κρατικό αναγνωριστικό το ΑΜΚΑ.",
            attributes=[
                Attribute(name="ΑΜΚΑ", attr_type="Απλό, Μονότιμο, Primary Key", is_pk=True),
                Attribute(name="ΑΔΤ", attr_type="Απλό, Μονότιμο, Candidate Key", is_candidate=True),
                Attribute(name="Όνομα", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Επώνυμο", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Ημερ_Γέννησης", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Φύλο", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Ομάδα_Αίματος", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Ηλικία", attr_type="Παράγωγο (Derived)", notes="Υπολογίζεται δυναμικά από την Ημερ_Γέννησης"),
            ],
        ),
        Entity(
            name="ΝΟΣΗΛΕΙΑ",
            entity_type="Ασθενής Οντότητα (Weak Entity)",
            is_weak=True,
            owner_entity="ΑΣΘΕΝΗΣ",
            justification="Επεισόδιο εισαγωγής στο νοσοκομείο. Προσδιορίζεται από το ΑΜΚΑ του ασθενούς και τον Αύξοντα Αριθμό Εισαγωγής.",
            attributes=[
                Attribute(name="Αύξων_Αριθμός_Εισαγωγής", attr_type="Απλό, Μερικό Κλειδί (Partial Key)", is_partial=True),
                Attribute(name="Ημερ_Ώρα_Εισαγωγής", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Ημερ_Ώρα_Εξιτηρίου", attr_type="Απλό, Μονότιμο (Nullable)"),
                Attribute(name="Αριθμός_Θαλάμου", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Αρχική_Διάγνωση", attr_type="Απλό, Μονότιμο"),
            ],
        ),
        Entity(
            name="ΦΑΡΜΑΚΟ",
            entity_type="Ισχυρή Οντότητα (Strong Entity)",
            is_weak=False,
            justification="Εγκεκριμένο θεραπευτικό σκεύασμα με μοναδικό εθνικό κωδικό ΕΟΦ.",
            attributes=[
                Attribute(name="Κωδικός_ΕΟΦ", attr_type="Απλό, Μονότιμο, Primary Key", is_pk=True),
                Attribute(name="Εμπορική_Ονομασία", attr_type="Απλό, Μονότιμο, Candidate Key", is_candidate=True),
                Attribute(name="Δραστική_Ουσία", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Μονάδα_Μέτρησης", attr_type="Απλό, Μονότιμο"),
            ],
        ),
    ]

    # 3. Relationship Attributes
    relationship_attributes = [
        RelationshipAttribute(
            name="Ημερομηνία_Ανάληψης_Διεύθυνσης",
            relationship_name="ΔΙΕΥΘΥΝΕΙ_ΚΛΙΝΙΚΗ (1:1)",
            justification="Περιγράφει πότε ανέλαβε επίσημα καθήκοντα διευθυντή ο ιατρός στη συγκεκριμένη κλινική.",
        ),
        RelationshipAttribute(
            name="Δοσολογία",
            relationship_name="ΧΟΡΗΓΗΣΗ_ΦΑΡΜΑΚΟΥ (N:M)",
            justification="Ποσότητα φαρμάκου ανά δόση για τη συγκεκριμένη νοσηλεία.",
        ),
        RelationshipAttribute(
            name="Συχνότητα_24ωρου",
            relationship_name="ΧΟΡΗΓΗΣΗ_ΦΑΡΜΑΚΟΥ (N:M)",
            justification="Αριθμός επαναλήψεων λήψης ανά ημέρα.",
        ),
        RelationshipAttribute(
            name="Ημερομηνία_Έναρξης",
            relationship_name="ΧΟΡΗΓΗΣΗ_ΦΑΡΜΑΚΟΥ (N:M)",
            justification="Ημερομηνία έναρξης της φαρμακευτικής αγωγής.",
        ),
        RelationshipAttribute(
            name="Ημερομηνία_Λήξης",
            relationship_name="ΧΟΡΗΓΗΣΗ_ΦΑΡΜΑΚΟΥ (N:M)",
            justification="Ημερομηνία ολοκλήρωσης της αγωγής.",
        ),
    ]

    # 4. Keys Analysis Table
    keys_analysis = [
        KeyAnalysisRow(
            entity_name="Κλινική",
            key_count="2",
            key_types="Υποψήφια: {Κωδικός_Κλινικής}, {Όνομα_Κλινικής}",
            final_pk_selection="Κωδικός_Κλινικής",
            justification="Σύντομος τεχνητός κωδικός σταθερού μήκους.",
        ),
        KeyAnalysisRow(
            entity_name="Ιατρός",
            key_count="2",
            key_types="Υποψήφια: {ΑΜΙ}, {ΑΦΜ}",
            final_pk_selection="ΑΜΙ",
            justification="Εσωτερικός αναγνωριστικός αριθμός ιατρικού μητρώου.",
        ),
        KeyAnalysisRow(
            entity_name="Εξαρτώμενο Μέλος",
            key_count="0 (Ασθενής)",
            key_types="Μερικό Κλειδί: {Όνομα_Μέλους}",
            final_pk_selection="Σύνθετο PK: {Ιατρός.ΑΜΙ, Όνομα_Μέλους}",
            justification="Ασθενής οντότητα με υπαρκτική εξάρτηση από τον Ιατρό.",
            is_weak=True,
        ),
        KeyAnalysisRow(
            entity_name="Ασθενής",
            key_count="2",
            key_types="Υποψήφια: {ΑΜΚΑ}, {ΑΔΤ}",
            final_pk_selection="ΑΜΚΑ",
            justification="Μοναδικός αριθμός κοινωνικής ασφάλισης για κάθε πολίτη/ασθενή.",
        ),
        KeyAnalysisRow(
            entity_name="Νοσηλεία",
            key_count="0 (Ασθενής)",
            key_types="Μερικό Κλειδί: {Αύξων_Αριθμός_Εισαγωγής}",
            final_pk_selection="Σύνθετο PK: {Ασθενής.ΑΜΚΑ, Αύξων_Αριθμός_Εισαγωγής}",
            justification="Ασθενής οντότητα εξαρτώμενη από τον ασθενή.",
            is_weak=True,
        ),
        KeyAnalysisRow(
            entity_name="Φάρμακο",
            key_count="2",
            key_types="Υποψήφια: {Κωδικός_ΕΟΦ}, {Εμπορική_Ονομασία}",
            final_pk_selection="Κωδικός_ΕΟΦ",
            justification="Επίσημος κρατικός αριθμός αναγνώρισης σκευάσματος.",
        ),
    ]

    # 5. Relationships
    relationships = [
        Relationship(
            letter_id="α",
            name="ΔΙΕΥΘΥΝΕΙ_ΚΛΙΝΙΚΗ",
            connected_entities="Κλινική <-> Ιατρός",
            cardinality="1:1",
            participation="Ολική για Κλινική, Μερική για Ιατρό",
            relationship_type="Κανονική Σχέση",
            attributes=["Ημερομηνία_Ανάληψης_Διεύθυνσης"],
            justification="Κάθε κλινική έχει υποχρεωτικά 1 διευθυντή ιατρό, κάθε ιατρός διευθύνει το πολύ 1 κλινική.",
        ),
        Relationship(
            letter_id="β",
            name="ΥΠΗΡΕΤΕΙ_ΣΕ",
            connected_entities="Ιατρός <-> Κλινική",
            cardinality="1:N",
            participation="Ολική για Ιατρό, Μερική για Κλινική",
            relationship_type="Κανονική Σχέση",
            attributes=[],
            justification="Κάθε ιατρός ανήκει υποχρεωτικά σε 1 κλινική, σε κάθε κλινική υπηρετούν πολλοί ιατροί.",
        ),
        Relationship(
            letter_id="γ",
            name="ΕΠΟΠΤΕΥΕΙ",
            connected_entities="Ιατρός (Επόπτης) <-> Ιατρός (Ειδικευόμενος)",
            cardinality="1:N",
            participation="Μερική για Επόπτη (0,N), Ολική για Ειδικευόμενο (1,1)",
            relationship_type="Αναδρομική Σχέση (Recursive)",
            attributes=[],
            justification="Ένας έμπειρος ιατρός καθοδηγεί πολλούς ειδικευόμενους, κάθε ειδικευόμενος έχει 1 επόπτη.",
        ),
        Relationship(
            letter_id="δ",
            name="ΕΧΕΙ_ΕΞΑΡΤΩΜΕΝΟ",
            connected_entities="Ιατρός <-> Εξαρτώμενο Μέλος",
            cardinality="1:N",
            participation="Ολική για Εξαρτώμενο Μέλος, Μερική για Ιατρό",
            relationship_type="Ταυτοποιούσα Σχέση (Identifying)",
            attributes=[],
            justification="Συνδέει την ασθενή οντότητα Εξαρτώμενο Μέλος με τον προσδιορίζοντα Ιατρό.",
        ),
        Relationship(
            letter_id="ε",
            name="ΕΙΣΑΓΩΓΗ_ΑΣΘΕΝΟΥΣ",
            connected_entities="Ασθενής <-> Νοσηλεία",
            cardinality="1:N",
            participation="Ολική για Νοσηλεία, Μερική για Ασθενή",
            relationship_type="Ταυτοποιούσα Σχέση (Identifying)",
            attributes=[],
            justification="Κάθε νοσηλεία αφορά αποκλειστικά 1 ασθενή, ο ασθενής μπορεί να έχει πολλές νοσηλείες.",
        ),
        Relationship(
            letter_id="στ",
            name="ΦΙΛΟΞΕΝΕΙ_ΝΟΣΗΛΕΙΑ",
            connected_entities="Κλινική <-> Νοσηλεία",
            cardinality="1:N",
            participation="Ολική για Νοσηλεία, Μερική για Κλινική",
            relationship_type="Κανονική Σχέση",
            attributes=[],
            justification="Κάθε νοσηλεία πραγματοποιείται σε 1 κλινική, μια κλινική φιλοξενεί πολλές νοσηλείες.",
        ),
        Relationship(
            letter_id="ζ",
            name="ΧΟΡΗΓΗΣΗ_ΦΑΡΜΑΚΟΥ",
            connected_entities="Νοσηλεία <-> Φάρμακο (με Θεράποντα Ιατρό)",
            cardinality="N:M",
            participation="Μερική και για τις δύο πλευρές",
            relationship_type="Συσχετιστική Οντότητα / Junction",
            attributes=["Δοσολογία", "Συχνότητα_24ωρου", "Ημερομηνία_Έναρξης", "Ημερομηνία_Λήξης"],
            justification="Σε μια νοσηλεία χορηγούνται πολλά φάρμακα και κάθε φάρμακο χορηγείται σε πολλές νοσηλείες.",
        ),
    ]

    # 6. Assumptions
    assumptions = [
        "Διεύθυνση Κατοικίας: Αναλύεται σε 4 ατομικά γνωρίσματα (Οδός, Αριθμός, ΤΚ, Πόλη) για εξασφάλιση 1NF.",
        "Πλειότιμα Γνωρίσματα: Τα τηλέφωνα ιατρών και οι πτέρυγες κλινικών υλοποιούνται ως αυτόνομοι σχεσιακοί πίνακες.",
        "Χορήγηση Φαρμάκου: Υλοποιείται ως συνδετικός πίνακας με Foreign Key και προς τον θεράποντα ιατρό που συνταγογράφησε την αγωγή.",
        "Νοσηλεία & Εξαρτώμενα: Ως ασθενείς οντότητες, διαθέτουν σύνθετο πρωτεύον κλειδί αποτελούμενο από το PK του κατόχου και το δικό τους μερικό κλειδί.",
    ]

    # 7. ER Table Nodes for SVG Crow's Foot Diagram
    er_tables = [
        ERTable(
            id="kliniki",
            label="ΚΛΙΝΙΚΗ",
            x=50,
            y=80,
            attrs=[
                ERTableAttr(name="Κωδικός_Κλινικής", pk=True),
                ERTableAttr(name="Όνομα_Κλινικής"),
                ERTableAttr(name="Όροφος"),
                ERTableAttr(name="Τηλέφωνο_Γραμματείας"),
                ERTableAttr(name="Διευθυντής_ΑΜΙ", fk=True),
                ERTableAttr(name="Ημερ_Ανάληψης_Διεύθυνσης"),
            ],
        ),
        ERTable(
            id="pteriga",
            label="ΠΤΕΡΥΓΑ_ΚΛΙΝΙΚΗΣ",
            x=50,
            y=400,
            attrs=[
                ERTableAttr(name="Κωδικός_Κλινικής", pk=True, fk=True),
                ERTableAttr(name="Τοποθεσία_Πτέρυγας", pk=True),
            ],
        ),
        ERTable(
            id="iatros",
            label="ΙΑΤΡΟΣ",
            x=450,
            y=50,
            attrs=[
                ERTableAttr(name="ΑΜΙ", pk=True),
                ERTableAttr(name="ΑΦΜ"),
                ERTableAttr(name="Όνομα"),
                ERTableAttr(name="Επώνυμο"),
                ERTableAttr(name="Ειδικότητα"),
                ERTableAttr(name="Βαθμίδα"),
                ERTableAttr(name="Βασικός_Μισθός"),
                ERTableAttr(name="Ημερ_Πρόσληψης"),
                ERTableAttr(name="Οδός_Κατοικίας"),
                ERTableAttr(name="Αριθμός_Κατοικίας"),
                ERTableAttr(name="ΤΚ_Κατοικίας"),
                ERTableAttr(name="Πόλη_Κατοικίας"),
                ERTableAttr(name="Κωδικός_Κλινικής_Ανήκει", fk=True),
                ERTableAttr(name="Επόπτης_ΑΜΙ", fk=True),
            ],
        ),
        ERTable(
            id="tilefono_iatroy",
            label="ΤΗΛΕΦΩΝΟ_ΙΑΤΡΟΥ",
            x=450,
            y=540,
            attrs=[
                ERTableAttr(name="ΑΜΙ", pk=True, fk=True),
                ERTableAttr(name="Αριθμός_Τηλεφώνου", pk=True),
            ],
        ),
        ERTable(
            id="exartomeno",
            label="ΕΞΑΡΤΩΜΕΝΟ_ΜΕΛΟΣ",
            x=450,
            y=680,
            attrs=[
                ERTableAttr(name="Ιατρός_ΑΜΙ", pk=True, fk=True),
                ERTableAttr(name="Όνομα_Μέλους", pk=True),
                ERTableAttr(name="Φύλο"),
                ERTableAttr(name="Ημερ_Γέννησης"),
                ERTableAttr(name="Συγγενική_Σχέση"),
            ],
        ),
        ERTable(
            id="asthenis",
            label="ΑΣΘΕΝΗΣ",
            x=850,
            y=50,
            attrs=[
                ERTableAttr(name="ΑΜΚΑ", pk=True),
                ERTableAttr(name="ΑΔΤ"),
                ERTableAttr(name="Όνομα"),
                ERTableAttr(name="Επώνυμο"),
                ERTableAttr(name="Ημερ_Γέννησης"),
                ERTableAttr(name="Φύλο"),
                ERTableAttr(name="Ομάδα_Αίματος"),
            ],
        ),
        ERTable(
            id="nosileia",
            label="ΝΟΣΗΛΕΙΑ",
            x=850,
            y=350,
            attrs=[
                ERTableAttr(name="ΑΜΚΑ", pk=True, fk=True),
                ERTableAttr(name="Αύξων_Αριθμός", pk=True),
                ERTableAttr(name="Ημερ_Ώρα_Εισαγωγής"),
                ERTableAttr(name="Ημερ_Ώρα_Εξιτηρίου"),
                ERTableAttr(name="Αριθμός_Θαλάμου"),
                ERTableAttr(name="Αρχική_Διάγνωση"),
                ERTableAttr(name="Κωδικός_Κλινικής", fk=True),
            ],
        ),
        ERTable(
            id="farmako",
            label="ΦΑΡΜΑΚΟ",
            x=50,
            y=600,
            attrs=[
                ERTableAttr(name="Κωδικός_ΕΟΦ", pk=True),
                ERTableAttr(name="Εμπορική_Ονομασία"),
                ERTableAttr(name="Δραστική_Ουσία"),
                ERTableAttr(name="Μονάδα_Μέτρησης"),
            ],
        ),
        ERTable(
            id="chorigisi",
            label="ΧΟΡΗΓΗΣΗ_ΦΑΡΜΑΚΟΥ",
            x=850,
            y=640,
            attrs=[
                ERTableAttr(name="ΑΜΚΑ", pk=True, fk=True),
                ERTableAttr(name="Αύξων_Αριθμός", pk=True, fk=True),
                ERTableAttr(name="Κωδικός_ΕΟΦ", pk=True, fk=True),
                ERTableAttr(name="Θεράπων_ΑΜΙ", fk=True),
                ERTableAttr(name="Δοσολογία"),
                ERTableAttr(name="Συχνότητα_24h"),
                ERTableAttr(name="Ημερ_Έναρξης"),
                ERTableAttr(name="Ημερ_Λήξης"),
            ],
        ),
    ]

    # 8. ER Diagram Edges
    er_edges = [
        EREdge(
            path="M 310,120 L 450,120",
            marker_start="start-one-mandatory",
            marker_end="end-one-optional",
            label="Διευθύνει (1:1)",
            lx=380,
            ly=110,
        ),
        # Doctor recursive supervisor (1:N)
        EREdge(
            path="M 710,90 C 770,30 770,170 710,150",
            marker_start="start-one-optional",
            marker_end="end-many-optional",
            label="Εποπτεύει (1:N)",
            lx=780,
            ly=100,
        ),
        EREdge(
            path="M 310,200 L 450,200",
            marker_start="start-one-optional",
            marker_end="end-many-mandatory",
            label="Υπηρετεί (1:N)",
            lx=380,
            ly=190,
        ),
        EREdge(
            path="M 180,240 L 180,400",
            marker_start="start-one-mandatory",
            marker_end="end-many-mandatory",
            label="Πτέρυγες (1:N)",
            lx=180,
            ly=320,
        ),
        EREdge(
            path="M 580,490 L 580,540",
            marker_start="start-one-mandatory",
            marker_end="end-many-mandatory",
            label="Τηλέφωνα (1:N)",
            lx=580,
            ly=515,
        ),
        EREdge(
            path="M 710,350 L 750,350 L 750,720 L 710,720",
            marker_start="start-one-optional",
            marker_end="end-many-mandatory",
            label="Εξαρτώμενα (1:N)",
            lx=760,
            ly=535,
        ),
        EREdge(
            path="M 980,294 L 980,350",
            marker_start="start-one-optional",
            marker_end="end-many-mandatory",
            label="Εισαγωγή (1:N)",
            lx=980,
            ly=322,
        ),
        EREdge(
            path="M 310,240 L 310,360 L 850,360",
            marker_start="start-one-optional",
            marker_end="end-many-mandatory",
            label="Φιλοξενεί (1:N)",
            lx=580,
            ly=360,
        ),
        EREdge(
            path="M 980,594 L 980,640",
            marker_start="start-one-mandatory",
            marker_end="end-many-optional",
            label="Χορήγηση (1:N)",
            lx=980,
            ly=617,
        ),
        EREdge(
            path="M 310,680 L 850,680",
            marker_start="start-one-mandatory",
            marker_end="end-many-optional",
            label="Φάρμακο (1:N)",
            lx=580,
            ly=670,
        ),
    ]

    # 9. Relational Justifications
    relational_justifications = [
        RelationalJustification(
            title="1. Σχέση 1:1 Διεύθυνσης Κλινικής:",
            color_class="text-blue-400",
            description="Η ΚΛΙΝΙΚΗ έχει ολική συμμετοχή στη σχέση Διεύθυνσης. Τοποθετούμε το foreign key Διευθυντής_ΑΜΙ στον πίνακα ΚΛΙΝΙΚΗ μαζί με το γνώρισμα Ημερομηνία_Ανάληψης_Διεύθυνσης.",
        ),
        RelationalJustification(
            title="2. Ασθενείς Οντότητες (Εξαρτώμενα & Νοσηλείες):",
            color_class="text-purple-400",
            description="Το ΕΞΑΡΤΩΜΕΝΟ_ΜΕΛΟΣ και η ΝΟΣΗΛΕΙΑ μετατρέπονται σε πίνακες με σύνθετο πρωτεύον κλειδί {Ιατρός_ΑΜΙ, Όνομα_Μέλους} και {ΑΜΚΑ, Αύξων_Αριθμός} αντίστοιχα, με κανόνα διαγραφής ON DELETE CASCADE.",
        ),
        RelationalJustification(
            title="3. Πλειότιμα Γνωρίσματα (1NF):",
            color_class="text-amber-400",
            description="Οι πτέρυγες των κλινικών και τα τηλέφωνα των ιατρών διασπώνται στους ανεξάρτητους πίνακες ΠΤΕΡΥΓΑ_ΚΛΙΝΙΚΗΣ και ΤΗΛΕΦΩΝΟ_ΙΑΤΡΟΥ.",
        ),
        RelationalJustification(
            title="4. Συσχετιστική Οντότητα Χορήγησης Φαρμάκων:",
            color_class="text-emerald-400",
            description="Η σχέση ΧΟΡΗΓΗΣΗ_ΦΑΡΜΑΚΟΥ υλοποιείται ως συνδετικός πίνακας με σύνθετο PK {ΑΜΚΑ, Αύξων_Αριθμός, Κωδικός_ΕΟΦ} και FK προς τον θεράποντα ιατρό.",
        ),
    ]

    # 10. SQL DDL Script
    sql_ddl = """-- SQL DDL Schema: Hospital Management Database
-- 1. Entity: KLINIKI
CREATE TABLE KLINIKI (
    kodikos_klinikis VARCHAR(10) PRIMARY KEY,
    onoma_klinikis VARCHAR(100) NOT NULL UNIQUE,
    orofos INT NOT NULL,
    thlefono_grammateias VARCHAR(20) NOT NULL,
    diefthyntis_ami VARCHAR(15) NOT NULL UNIQUE,
    hmer_analipsis_diefthynsis DATE NOT NULL
);

-- 2. Multivalued Attribute: PTERIGA_KLINIKIS
CREATE TABLE PTERIGA_KLINIKIS (
    kodikos_klinikis VARCHAR(10) NOT NULL,
    topothesia_pterigas VARCHAR(100) NOT NULL,
    PRIMARY KEY (kodikos_klinikis, topothesia_pterigas),
    FOREIGN KEY (kodikos_klinikis) REFERENCES KLINIKI(kodikos_klinikis) ON DELETE CASCADE
);

-- 3. Entity: IATROS
CREATE TABLE IATROS (
    ami VARCHAR(15) PRIMARY KEY,
    afm VARCHAR(10) NOT NULL UNIQUE,
    onoma VARCHAR(50) NOT NULL,
    eponymo VARCHAR(50) NOT NULL,
    eidikotita VARCHAR(50) NOT NULL,
    vathmida VARCHAR(50) NOT NULL,
    vasikos_misthos DECIMAL(10, 2) NOT NULL,
    hmer_proslipsis DATE NOT NULL,
    odos VARCHAR(100) NOT NULL,
    arithmos VARCHAR(10) NOT NULL,
    tk VARCHAR(10) NOT NULL,
    poli VARCHAR(50) NOT NULL,
    kodikos_klinikis VARCHAR(10) NOT NULL,
    epoptis_ami VARCHAR(15),
    FOREIGN KEY (kodikos_klinikis) REFERENCES KLINIKI(kodikos_klinikis),
    FOREIGN KEY (epoptis_ami) REFERENCES IATROS(ami)
);

-- Add Circular Foreign Key for Clinic Director
ALTER TABLE KLINIKI ADD CONSTRAINT fk_kliniki_diefthyntis
    FOREIGN KEY (diefthyntis_ami) REFERENCES IATROS(ami);

-- 4. Multivalued Attribute: TILEFONO_IATROY
CREATE TABLE TILEFONO_IATROY (
    ami VARCHAR(15) NOT NULL,
    arithmos_tilefonou VARCHAR(20) NOT NULL,
    PRIMARY KEY (ami, arithmos_tilefonou),
    FOREIGN KEY (ami) REFERENCES IATROS(ami) ON DELETE CASCADE
);

-- 5. Weak Entity: EXARTOMENO_MELOS
CREATE TABLE EXARTOMENO_MELOS (
    iatros_ami VARCHAR(15) NOT NULL,
    onoma_melous VARCHAR(50) NOT NULL,
    fylo CHAR(1) CHECK (fylo IN ('M', 'F', 'O')),
    hmer_gennisis DATE NOT NULL,
    syggeniki_schesi VARCHAR(30) NOT NULL,
    PRIMARY KEY (iatros_ami, onoma_melous),
    FOREIGN KEY (iatros_ami) REFERENCES IATROS(ami) ON DELETE CASCADE
);

-- 6. Entity: ASTHENIS
CREATE TABLE ASTHENIS (
    amka VARCHAR(15) PRIMARY KEY,
    adt VARCHAR(15) NOT NULL UNIQUE,
    onoma VARCHAR(50) NOT NULL,
    eponymo VARCHAR(50) NOT NULL,
    hmer_gennisis DATE NOT NULL,
    fylo CHAR(1) CHECK (fylo IN ('M', 'F', 'O')),
    omada_aimatos VARCHAR(5) NOT NULL
);

-- 7. Weak Entity: NOSILEIA
CREATE TABLE NOSILEIA (
    amka VARCHAR(15) NOT NULL,
    arithmos_eisagogis INT NOT NULL,
    hmer_wra_eisagogis TIMESTAMP NOT NULL,
    hmer_wra_exitiriou TIMESTAMP,
    arithmos_thalamou VARCHAR(10) NOT NULL,
    archiki_diagnosi TEXT NOT NULL,
    kodikos_klinikis VARCHAR(10) NOT NULL,
    PRIMARY KEY (amka, arithmos_eisagogis),
    FOREIGN KEY (amka) REFERENCES ASTHENIS(amka) ON DELETE CASCADE,
    FOREIGN KEY (kodikos_klinikis) REFERENCES KLINIKI(kodikos_klinikis)
);

-- 8. Entity: FARMAKO
CREATE TABLE FARMAKO (
    kodikos_eof VARCHAR(20) PRIMARY KEY,
    emporiki_onomasia VARCHAR(100) NOT NULL UNIQUE,
    drastiki_ousia VARCHAR(100) NOT NULL,
    monada_metrisis VARCHAR(20) NOT NULL
);

-- 9. Relationship / Junction Table: CHORIGISI_FARMAKOU
CREATE TABLE CHORIGISI_FARMAKOU (
    amka VARCHAR(15) NOT NULL,
    arithmos_eisagogis INT NOT NULL,
    kodikos_eof VARCHAR(20) NOT NULL,
    therapon_ami VARCHAR(15) NOT NULL,
    dosologia VARCHAR(50) NOT NULL,
    sychnotita_24h INT NOT NULL,
    hmer_enarxis DATE NOT NULL,
    hmer_lixis DATE,
    PRIMARY KEY (amka, arithmos_eisagogis, kodikos_eof),
    FOREIGN KEY (amka, arithmos_eisagogis) REFERENCES NOSILEIA(amka, arithmos_eisagogis) ON DELETE CASCADE,
    FOREIGN KEY (kodikos_eof) REFERENCES FARMAKO(kodikos_eof),
    FOREIGN KEY (therapon_ami) REFERENCES IATROS(ami)
);"""

    return Scenario(
        id="hospital_management",
        title="Σύστημα Διαχείρισης Νοσοκομειακού Ιδρύματος",
        subtitle="Μοντελοποίηση Κλινικών, Ιατρών, Ασθενών, Νοσηλειών & Θεραπειών",
        course_tag="Βάσεις Δεδομένων (Πρόοδος 2025-2026 - Θέμα 1)",
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
