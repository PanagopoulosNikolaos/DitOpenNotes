"""Streaming Platform and Digital Content case study scenario module.

Contains the complete parsed and modeled ER analysis for the Global On-demand Streaming Platform
(Media Titles, Movies, TV Series, Episodes, Cast & Crew, Subscribers, Profiles, Viewing History & Ratings),
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


def createStreamingPlatformScenario() -> Scenario:
    """Constructs and returns the Streaming Platform database scenario.

    Returns:
        Scenario: Fully populated scenario instance.
    """
    # 1. Text Paragraphs with Interactive Segments
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Μια παγκόσμια πλατφόρμα συνεχούς ροής βίντεο και παραγωγής ψηφιακού κινηματογραφικού περιεχομένου (On-demand Streaming Platform) αναπτύσσει τη βάση δεδομένων της για τη διαχείριση "),
                TextSegment(
                    text="τίτλων / έργων (ταινιών και σειρών)",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ (ΥΠΕΡΚΛΑΣΗ)",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Superclass): Ψηφιακό οπτικοακουστικό έργο με μοναδικό ISAN.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="συντελεστών",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Strong Entity): Ηθοποιός, σκηνοθέτης ή δημιουργός με αριθμό μητρώου.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="συνδρομητών",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Strong Entity): Κάτοχος λογαριασμού με μοναδικό email.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="προφίλ χρηστών",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΑΣΘΕΝΗΣ ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-weak",
                    tooltip="Ασθενής Οντότητα (Weak Entity): Προφίλ χρήστη εξαρτώμενο από τον συνδρομητή.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="ιστορικού θεάσεων και αξιολογήσεων",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ N:M",
                    badge_class="badge-rel-nm",
                    tooltip="Συσχέτιση N:M (ΙΣΤΟΡΙΚΟ_ΘΕΑΣΗΣ): Καταγραφή αναπαραγωγής και κριτικών ανά προφίλ.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color=None,
        ),
        Paragraph(
            segments=[
                TextSegment(text="1. <strong>Οπτικοακουστικά Έργα (Media Titles):</strong> Κάθε έργο ταυτοποιείται από τον "),
                TextSegment(
                    text="διεθνή μοναδικό κωδικό ISAN (International Standard Audiovisual Number)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Παγκόσμιος μοναδικός αριθμός ISAN.",
                ),
                TextSegment(text=", τον "),
                TextSegment(text="πρωτότυπο τίτλο", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", το "),
                TextSegment(text="έτος παραγωγής/κυκλοφορίας", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", την "),
                TextSegment(text="ηλικιακή καταλληλότητα (π.χ. 'PG-13', '18+')", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", την "),
                TextSegment(text="κύρια κατηγορία/είδος ('Sci-Fi', 'Drama', 'Thriller')", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και τη "),
                TextSegment(text="σύνοψη", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=". Κάθε έργο διατίθεται σε "),
                TextSegment(
                    text="πολλαπλές γλώσσες μεταγλώττισης (Audio Tracks)",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΠΛΕΙΟΤΙΜΟ",
                    badge_class="badge-attr-multi",
                    tooltip="Πλειότιμο Γνώρισμα: Εξάγεται στον πίνακα GLOSSA_HXOU.",
                ),
                TextSegment(text=" και "),
                TextSegment(
                    text="πολλαπλές γλώσσες υποτίτλων (Subtitles)",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΠΛΕΙΟΤΙΜΟ",
                    badge_class="badge-attr-multi",
                    tooltip="Πλειότιμο Γνώρισμα: Εξάγεται στον πίνακα GLOSSA_YPOTITLON.",
                ),
                TextSegment(text=" που καταγράφονται ως λίστες διαθέσιμων γλωσσών. Τα έργα διακρίνονται σε αυτοτελείς "),
                TextSegment(
                    text="Ταινίες (με συγκεκριμένη διάρκεια σε λεπτά)",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΥΠΟΚΛΑΣΗ",
                    badge_class="badge-entity-strong",
                    tooltip="Εξειδίκευση/Υποκλάση: Πίνακας TAINIA με διάρκεια σε λεπτά.",
                ),
                TextSegment(text=" και "),
                TextSegment(
                    text="Τηλεοπτικές Σειρές",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΥΠΟΚΛΑΣΗ",
                    badge_class="badge-entity-strong",
                    tooltip="Εξειδίκευση/Υποκλάση: Πίνακας TILEOPTIKI_SEIRA με επεισόδια.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-blue-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="2. <strong>Επεισόδια Σειρών (Episodes):</strong> Για κάθε τηλεοπτική σειρά υπάρχουν διακριτά επεισόδια. Κάθε επεισόδιο προσδιορίζεται από τον "),
                TextSegment(
                    text="αριθμό σεζόν (Season Number) και τον αύξοντα αριθμό επεισοδίου (Episode Number) εντός της συγκεκριμένης σειράς",
                    is_highlight=True,
                    category="key",
                    tag_label="PARTIAL KEY",
                    badge_class="badge-key-partial",
                    tooltip="Μερικό Κλειδί (Partial Key): (Season, Episode) εντός του ISAN της σειράς.",
                ),
                TextSegment(text=". Για κάθε επεισόδιο καταγράφονται ο "),
                TextSegment(text="τίτλος του επεισοδίου", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(text="διάρκεια σε λεπτά", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και η "),
                TextSegment(text="ημερομηνία πρώτης προβολής", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=". "),
                TextSegment(
                    text="Ένα επεισόδιο δεν μπορεί να υπάρξει αυτόνομα χωρίς την αντίστοιχη τηλεοπτική σειρά",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΑΣΘΕΝΗΣ ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-weak",
                    tooltip="Υπαρκτική Εξάρτηση: Προσδιορίζουσα οντότητα είναι η ΤΗΛΕΟΠΤΙΚΗ_ΣΕΙΡΑ.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-amber-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="3. <strong>Συντελεστές & Συμμετοχές (Cast & Crew):</strong> Για κάθε συντελεστή καταγράφονται: ο "),
                TextSegment(
                    text="μοναδικός Αριθμός Μητρώου Συντελεστή",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Μοναδικός κωδικός συντελεστή.",
                ),
                TextSegment(text=", το "),
                TextSegment(text="ονοματεπώνυμο", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", το "),
                TextSegment(text="καλλιτεχνικό ψευδώνυμο", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(text="ημερομηνία γέννησης", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(text="εθνικότητα", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και η "),
                TextSegment(text="βιογραφία", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=". Ένας συντελεστής "),
                TextSegment(
                    text="συμμετέχει στην παραγωγή πολλαπλών έργων με διαφορετικές ιδιότητες (Σκηνοθέτης, Σεναριογράφος, Πρωταγωνιστής)",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ N:M",
                    badge_class="badge-rel-nm",
                    tooltip="Συσχέτιση N:M (ΣΥΜΜΕΤΟΧΗ): Πίνακας διασύνδεσης Έργου και Συντελεστή.",
                ),
                TextSegment(text=". Για κάθε συμμετοχή ενός ηθοποιού σε ένα έργο καταγράφεται το "),
                TextSegment(
                    text="όνομα του ρόλου/χαρακτήρα που υποδύεται",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ ΣΧΕΣΗΣ",
                    badge_class="badge-attr-composite",
                    tooltip="Γνώρισμα Συσχέτισης: Χαρακτήρας σεναρίου.",
                ),
                TextSegment(text=" και η "),
                TextSegment(
                    text="συμφωνηθείσα αμοιβή",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ ΣΧΕΣΗΣ",
                    badge_class="badge-attr-composite",
                    tooltip="Γνώρισμα Συσχέτισης: Αμοιβή συμμετοχής.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-purple-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="4. <strong>Συνδρομητές (Subscribers):</strong> Για κάθε συνδρομητή καταγράφονται: το "),
                TextSegment(
                    text="μοναδικό email",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Μοναδικό email λογαριασμού.",
                ),
                TextSegment(text=", το "),
                TextSegment(
                    text="username",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Υποψήφιο Κλειδί (Candidate Key): Μοναδικό όνομα χρήστη.",
                ),
                TextSegment(text=", ο "),
                TextSegment(text="κρυπτογραφημένος κωδικός πρόσβασης (Password Hash)", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(text="ημερομηνία εγγραφής", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(text="χώρα χρέωσης", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και ο "),
                TextSegment(text="τύπος συνδρομητικού πακέτου ('Basic', 'Standard HD', 'Premium 4K')", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=". Ένας συνδρομητής διαθέτει έναν ή περισσότερους "),
                TextSegment(
                    text="έγκυρους τρόπους πληρωμής (πιστωτική κάρτα, PayPal)",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΠΛΕΙΟΤΙΜΟ",
                    badge_class="badge-attr-multi",
                    tooltip="Πλειότιμο Γνώρισμα: Αποθηκεύεται στον πίνακα ΤΡΟΠΟΣ_ΠΛΗΡΩΜΗΣ.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-emerald-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="5. <strong>Προφίλ Χρηστών (User Profiles):</strong> Κάθε συνδρομητής μπορεί να δημιουργήσει "),
                TextSegment(
                    text="πολλαπλά προφίλ εντός του λογαριασμού του ('Γονείς', 'Παιδικό', 'Προσωπικό')",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ 1:N",
                    badge_class="badge-rel-1n",
                    tooltip="Συσχέτιση 1:N (ΔΗΜΙΟΥΡΓΕΙ_ΠΡΟΦΙΛ): Ταυτοποιούσα σχέση συνδρομητή και προφίλ.",
                ),
                TextSegment(text=". Κάθε προφίλ προσδιορίζεται από το "),
                TextSegment(
                    text="όνομα προφίλ (Profile Name) εντός του συγκεκριμένου συνδρομητή",
                    is_highlight=True,
                    category="key",
                    tag_label="PARTIAL KEY",
                    badge_class="badge-key-partial",
                    tooltip="Μερικό Κλειδί (Partial Key): Ταυτοποιεί το προφίλ μόνο σε συνδυασμό με το email του συνδρομητή.",
                ),
                TextSegment(text=", το "),
                TextSegment(text="επιλεγμένο avatar", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", τη "),
                TextSegment(text="γλώσσα διεπαφής", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", το αν πρόκειται για "),
                TextSegment(text="παιδικό προφίλ (Kids Profile - Boolean)", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και το "),
                TextSegment(text="τετραψήφιο PIN γονικού ελέγχου", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text="."),
            ],
            accent_border_color="border-rose-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="6. <strong>Ιστορικό Θεάσεων & Αξιολογήσεις (Watch History & Reviews):</strong> Κάθε προφίλ παρακολουθεί διάφορα έργα/επεισόδια. Για κάθε θέαση καταγράφονται η "),
                TextSegment(
                    text="ακριβής ημερομηνία και ώρα έναρξης",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ ΣΧΕΣΗΣ",
                    badge_class="badge-attr-composite",
                    tooltip="Γνώρισμα Συσχέτισης: Χρονοσφραγίδα έναρξης προβολής.",
                ),
                TextSegment(text=", η "),
                TextSegment(
                    text="χρονική πρόοδος αναπαραγωγής (σε δευτερόλεπτα)",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ ΣΧΕΣΗΣ",
                    badge_class="badge-attr-composite",
                    tooltip="Γνώρισμα Συσχέτισης: Θέση αναπαραγωγής (resume point).",
                ),
                TextSegment(text=", το "),
                TextSegment(
                    text="αν ολοκληρώθηκε η προβολή (Completed - Boolean)",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ ΣΧΕΣΗΣ",
                    badge_class="badge-attr-composite",
                    tooltip="Γνώρισμα Συσχέτισης: Ένδειξη ολοκλήρωσης θέασης.",
                ),
                TextSegment(text=" και η προαιρετική "),
                TextSegment(
                    text="αξιολόγηση που έδωσε ο χρήστης (βαθμολογία 1 έως 5 αστέρια και ημερομηνία βαθμολόγησης)",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ ΣΧΕΣΗΣ",
                    badge_class="badge-attr-composite",
                    tooltip="Γνώρισμα Συσχέτισης: Αστέρια βαθμολογίας και ημερομηνία αξιολόγησης.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-cyan-500",
        ),
    ]

    # 2. Detailed Entities List
    entities = [
        Entity(
            name="ΕΡΓΟ (Audiovisual Title / Media Item)",
            entity_type="Ισχυρή Οντότητα (Υπερκλάση)",
            is_weak=False,
            owner_entity=None,
            justification="Κεντρική οντότητα περιεχομένου με διεθνή κωδικό ISAN. Αποτελεί υπερκλάση γενίκευσης για Ταινίες και Τηλεοπτικές Σειρές.",
            attributes=[
                Attribute("isan", "Απλό / Μονότιμο", is_pk=True, notes="Διεθνής αριθμός οπτικοακουστικού έργου (PK)"),
                Attribute("prototypos_titlos", "Απλό / Μονότιμο", notes="Πρωτότυπος τίτλος έργου"),
                Attribute("etos_kykloforias", "Απλό / Μονότιμο", notes="Έτος πρώτης κυκλοφορίας"),
                Attribute("ilikia_rating", "Απλό / Μονότιμο", notes="Καταλληλότητα ('G', 'PG', 'PG-13', '18+')"),
                Attribute("kyria_katigoria", "Απλό / Μονότιμο", notes="Είδος/Genre ('Sci-Fi', 'Drama', 'Action')"),
                Attribute("synopsi", "Απλό / Μονότιμο", notes="Περιληπτική περιγραφή υπόθεσης"),
                Attribute("glossa_hxou", "Πλειότιμο", notes="Διαθέσιμες γλώσσες ήχου (Πίνακας GLOSSA_HXOU)"),
                Attribute("glossa_ypotitlon", "Πλειότιμο", notes="Διαθέσιμες γλώσσες υποτίτλων (Πίνακας GLOSSA_YPOTITLON)"),
            ],
        ),
        Entity(
            name="ΤΑΙΝΙΑ (Movie)",
            entity_type="Ισχυρή Οντότητα (Υποκλάση)",
            is_weak=False,
            owner_entity=None,
            justification="Εξειδίκευση της οντότητας ΕΡΓΟ για αυτοτελείς κινηματογραφικές παραγωγές.",
            attributes=[
                Attribute("isan", "Απλό / Μονότιμο", is_pk=True, is_fk=True, notes="ISAN ταινίας (PK & FK στο ΕΡΓΟ)"),
                Attribute("diarkeia_lepta", "Απλό / Μονότιμο", notes="Συνολική διάρκεια σε λεπτά"),
            ],
        ),
        Entity(
            name="ΤΗΛΕΟΠΤΙΚΗ_ΣΕΙΡΑ (TV Series)",
            entity_type="Ισχυρή Οντότητα (Υποκλάση)",
            is_weak=False,
            owner_entity=None,
            justification="Εξειδίκευση της οντότητας ΕΡΓΟ για παραγωγές πολλαπλών επεισοδίων και κύκλων.",
            attributes=[
                Attribute("isan", "Απλό / Μονότιμο", is_pk=True, is_fk=True, notes="ISAN σειράς (PK & FK στο ΕΡΓΟ)"),
                Attribute("synolo_sezon", "Απλό / Μονότιμο", notes="Συνολικός αριθμός παραχθέντων κύκλων"),
            ],
        ),
        Entity(
            name="ΕΠΕΙΣΟΔΙΟ (Episode)",
            entity_type="Ασθενής Οντότητα",
            is_weak=True,
            owner_entity="ΤΗΛΕΟΠΤΙΚΗ_ΣΕΙΡΑ",
            justification="Ασθενής οντότητα. Προσδιορίζεται από το ISAN της σειράς και το σύνθετο μερικό κλειδί (season_number, episode_number).",
            attributes=[
                Attribute("season_number", "Απλό / Μονότιμο", is_partial=True, notes="Αριθμός κύκλου/σεζόν"),
                Attribute("episode_number", "Απλό / Μονότιμο", is_partial=True, notes="Αριθμός επεισοδίου εντός σεζόν"),
                Attribute("titlos_epeisodiou", "Απλό / Μονότιμο", notes="Τίτλος του συγκεκριμένου επεισοδίου"),
                Attribute("diarkeia_lepta", "Απλό / Μονότιμο", notes="Διάρκεια επεισοδίου σε λεπτά"),
                Attribute("hmer_protis_provolis", "Απλό / Μονότιμο", notes="Ημερομηνία πρώτης μετάδοσης"),
            ],
        ),
        Entity(
            name="ΣΥΝΤΕΛΕΣΤΗΣ (Cast & Crew)",
            entity_type="Ισχυρή Οντότητα",
            is_weak=False,
            owner_entity=None,
            justification="Αυτοτελής οντότητα καλλιτέχνη / δημιουργού με μοναδικό κωδικό μητρώου.",
            attributes=[
                Attribute("am_syntelesti", "Απλό / Μονότιμο", is_pk=True, notes="Αριθμός Μητρώου Συντελεστή (PK)"),
                Attribute("onomateponymo", "Απλό / Μονότιμο", notes="Ονοματεπώνυμο συντελεστή"),
                Attribute("kallitexniko_psevdonymo", "Απλό / Μονότιμο", notes="Καλλιτεχνικό ψευδώνυμο / Stage Name"),
                Attribute("hmer_gennisis", "Απλό / Μονότιμο", notes="Ημερομηνία γέννησης"),
                Attribute("ethnikotita", "Απλό / Μονότιμο", notes="Χώρα καταγωγής"),
                Attribute("viografia", "Απλό / Μονότιμο", notes="Βιογραφικό σημείωμα"),
            ],
        ),
        Entity(
            name="ΣΥΝΔΡΟΜΗΤΗΣ (Subscriber)",
            entity_type="Ισχυρή Οντότητα",
            is_weak=False,
            owner_entity=None,
            justification="Φυσικό πρόσωπο κατόχου συνδρομητικού λογαριασμού με μοναδικό email.",
            attributes=[
                Attribute("email", "Απλό / Μονότιμο", is_pk=True, notes="Μοναδική διεύθυνση ηλεκτρονικού ταχυδρομείου (PK)"),
                Attribute("username", "Απλό / Μονότιμο", is_candidate=True, notes="Μοναδικό ψευδώνυμο χρήστη (Candidate Key)"),
                Attribute("password_hash", "Απλό / Μονότιμο", notes="Κρυπτογραφημένος κωδικός πρόσβασης"),
                Attribute("hmer_eggrafis", "Απλό / Μονότιμο", notes="Ημερομηνία δημιουργίας συνδρομής"),
                Attribute("xora_xreosis", "Απλό / Μονότιμο", notes="Χώρα τιμολόγησης"),
                Attribute("syndromitiko_paketo", "Απλό / Μονότιμο", notes="Πακέτο συνδρομής ('Basic', 'Standard HD', 'Premium 4K')"),
                Attribute("tropoi_pliromis", "Πλειότιμο", notes="Πολλαπλές μέθοδοι πληρωμής (Πίνακας TROPOS_PLIROMIS)"),
            ],
        ),
        Entity(
            name="ΠΡΟΦΙΛ_ΧΡΗΣΤΗ (User Profile)",
            entity_type="Ασθενής Οντότητα",
            is_weak=True,
            owner_entity="ΣΥΝΔΡΟΜΗΤΗΣ",
            justification="Ασθενής οντότητα. Κάθε προφίλ υπάρχει μόνο εντός του συνδρομητή και προσδιορίζεται από το όνομα προφίλ.",
            attributes=[
                Attribute("profile_name", "Απλό / Μονότιμο", is_partial=True, notes="Μερικό Κλειδί: Όνομα προφίλ εντός του λογαριασμού"),
                Attribute("avatar", "Απλό / Μονότιμο", notes="Εικονίδιο / Avatar προφίλ"),
                Attribute("glossa_diepafis", "Απλό / Μονότιμο", notes="Προτιμώμενη γλώσσα εμφάνισης"),
                Attribute("is_kids", "Απλό / Μονότιμο", notes="Παιδικό προφίλ (Boolean)"),
                Attribute("parental_pin", "Απλό / Μονότιμο", notes="Τετραψήφιος κωδικός ασφαλείας"),
            ],
        ),
    ]

    # 3. Relationship Attributes
    relationship_attributes = [
        RelationshipAttribute(
            name="idiotita, onoma_rolou, symfonitheisa_amoivi",
            relationship_name="ΣΥΜΜΕΤΟΧΗ_ΣΥΝΤΕΛΕΣΤΗ (ΕΡΓΟ - ΣΥΝΤΕΛΕΣΤΗΣ)",
            justification="Ιδιότητα συμμετοχής (π.χ. 'Σκηνοθέτης', 'Ηθοποιός'), όνομα χαρακτήρα και αμοιβή στον πίνακα σύνδεσης.",
        ),
        RelationshipAttribute(
            name="hmerominia_ora_enarksis, xroniki_proodos_sec, is_completed, rating_stars, hmer_axiologisis",
            relationship_name="ΙΣΤΟΡΙΚΟ_ΘΕΑΣΗΣ (ΠΡΟΦΙΛ_ΧΡΗΣΤΗ - ΕΡΓΟ/ΕΠΕΙΣΟΔΙΟ)",
            justification="Χρονοσφραγίδα αναπαραγωγής, σημείο παύσης (resume point), ένδειξη ολοκλήρωσης, αστέρια βαθμολογίας και ημερομηνία κριτικής.",
        ),
    ]

    # 4. Keys Analysis Table
    keys_analysis = [
        KeyAnalysisRow(
            entity_name="ΕΡΓΟ",
            key_count="1 Υποψήφιο",
            key_types="Υποψήφιο: {isan}",
            final_pk_selection="isan",
            justification="Παγκόσμιος μοναδικός κωδικός ISAN για οπτικοακουστικά έργα.",
        ),
        KeyAnalysisRow(
            entity_name="ΤΑΙΝΙΑ",
            key_count="1 Υποψήφιο (Κληρονομούμενο)",
            key_types="Υποψήφιο: {isan}",
            final_pk_selection="isan",
            justification="Πρωτεύον κλειδί και ταυτόχρονα Foreign Key προς τον υπερπίνακα ΕΡΓΟ.",
        ),
        KeyAnalysisRow(
            entity_name="ΤΗΛΕΟΠΤΙΚΗ_ΣΕΙΡΑ",
            key_count="1 Υποψήφιο (Κληρονομούμενο)",
            key_types="Υποψήφιο: {isan}",
            final_pk_selection="isan",
            justification="Πρωτεύον κλειδί και Foreign Key προς τον υπερπίνακα ΕΡΓΟ.",
        ),
        KeyAnalysisRow(
            entity_name="ΕΠΕΙΣΟΔΙΟ",
            key_count="Ασθενής (2 Μερικά)",
            key_types="Μερικά Κλειδιά: {season_number, episode_number}",
            final_pk_selection="(isan, season_number, episode_number)",
            justification="Σύνθετο πρωτεύον κλειδί: ISAN της σειράς + Season + Episode Number.",
            is_weak=True,
        ),
        KeyAnalysisRow(
            entity_name="ΣΥΝΤΕΛΕΣΤΗΣ",
            key_count="1 Υποψήφιο",
            key_types="Υποψήφιο: {am_syntelesti}",
            final_pk_selection="am_syntelesti",
            justification="Μοναδικός αριθμός μητρώου συντελεστή.",
        ),
        KeyAnalysisRow(
            entity_name="ΣΥΝΔΡΟΜΗΤΗΣ",
            key_count="2 Υποψήφια",
            key_types="Υποψήφια: {email}, {username}",
            final_pk_selection="email",
            justification="Το email αποτελεί το βασικό αναγνωριστικό αυθεντικοποίησης και επικοινωνίας.",
        ),
        KeyAnalysisRow(
            entity_name="ΠΡΟΦΙΛ_ΧΡΗΣΤΗ",
            key_count="Ασθενής (1 Μερικό)",
            key_types="Μερικό Κλειδί: {profile_name}",
            final_pk_selection="(email, profile_name)",
            justification="Σύνθετο πρωτεύον κλειδί: Email συνδρομητή + όνομα προφίλ.",
            is_weak=True,
        ),
    ]

    # 5. Relationships List
    relationships = [
        Relationship(
            letter_id="α",
            name="ΓΕΝΙΚΕΥΣΗ / ΕΞΕΙΔΙΚΕΥΣΗ (ISA Hierarchy)",
            connected_entities="ΕΡΓΟ -> ΤΑΙΝΙΑ / ΤΗΛΕΟΠΤΙΚΗ_ΣΕΙΡΑ",
            cardinality="1:1 (Disjoint/Total)",
            participation="Ολική (Κάθε έργο είναι είτε Ταινία είτε Σειρά)",
            relationship_type="Ιεραρχία Κληρονομικότητας",
            attributes=[],
            justification="Κατηγοριοποίηση σε αυτοτελή ταινία ή τηλεοπτική σειρά με κληρονομικότητα γνωρισμάτων.",
        ),
        Relationship(
            letter_id="β",
            name="ΠΕΡΙΕΧΕΙ_ΕΠΕΙΣΟΔΙΑ (Contains Episodes)",
            connected_entities="ΤΗΛΕΟΠΤΙΚΗ_ΣΕΙΡΑ <-> ΕΠΕΙΣΟΔΙΟ",
            cardinality="1:N",
            participation="Ολική για Επεισόδιο (1,1), Ολική για Σειρά (1,N)",
            relationship_type="Ταυτοποιούσα Σχέση (Identifying)",
            attributes=[],
            justification="Ταυτοποιούσα σχέση της ασθενούς οντότητας ΕΠΕΙΣΟΔΙΟ από την ΤΗΛΕΟΠΤΙΚΗ_ΣΕΙΡΑ.",
        ),
        Relationship(
            letter_id="γ",
            name="ΣΥΜΜΕΤΕΧΕΙ_ΣΕ_ΕΡΓΟ (Cast Participation)",
            connected_entities="ΕΡΓΟ <-> ΣΥΝΤΕΛΕΣΤΗΣ",
            cardinality="N:M",
            participation="Ολική για Έργο (1,N), Μερική για Συντελεστή (0,N)",
            relationship_type="Κανονική Σχέση (Junction)",
            attributes=["idiotita", "onoma_rolou", "symfonitheisa_amoivi"],
            justification="Πολλοί συντελεστές συμμετέχουν σε ένα έργο και ένας συντελεστής συμμετέχει σε πολλά έργα.",
        ),
        Relationship(
            letter_id="δ",
            name="ΔΗΜΙΟΥΡΓΕΙ_ΠΡΟΦΙΛ (Creates Profiles)",
            connected_entities="ΣΥΝΔΡΟΜΗΤΗΣ <-> ΠΡΟΦΙΛ_ΧΡΗΣΤΗ",
            cardinality="1:N",
            participation="Ολική για Προφίλ (1,1), Ολική για Συνδρομητή (1,N)",
            relationship_type="Ταυτοποιούσα Σχέση (Identifying)",
            attributes=[],
            justification="Ταυτοποιούσα σχέση της ασθενούς οντότητας ΠΡΟΦΙΛ_ΧΡΗΣΤΗ από τον ΣΥΝΔΡΟΜΗΤΗ.",
        ),
        Relationship(
            letter_id="ε",
            name="ΙΣΤΟΡΙΚΟ_ΘΕΑΣΗΣ_ΚΑΙ_ΑΞΙΟΛΟΓΗΣΗ (Viewing & Rating)",
            connected_entities="ΠΡΟΦΙΛ_ΧΡΗΣΤΗ <-> ΕΡΓΟ",
            cardinality="N:M",
            participation="Μερική για Προφίλ (0,N), Μερική για Έργο (0,N)",
            relationship_type="Κανονική Σχέση (Junction)",
            attributes=["hmerominia_ora_enarksis", "xroniki_proodos_sec", "is_completed", "rating_stars", "hmer_axiologisis"],
            justification="Ένα προφίλ παρακολουθεί και βαθμολογεί πολλαπλά έργα/επεισόδια και ένα έργο παρακολουθείται από πολλά προφίλ.",
        ),
    ]

    # 6. Design Assumptions
    assumptions = [
        "Η εξειδίκευση ΕΡΓΟ σε ΤΑΙΝΙΑ και ΤΗΛΕΟΠΤΙΚΗ_ΣΕΙΡΑ υλοποιείται με την τεχνική Class Table Inheritance (διακριτοί πίνακες με κοινό PK/FK isan).",
        "Οι γλώσσες ήχου και υπότιτλων αποθηκεύονται σε ξεχωριστούς σχεσιακούς πίνακες 1:N για πλήρη κανονικοποίηση 1NF.",
        "Οι τρόποι πληρωμής συνδρομητή εξάγονται σε ανεξάρτητο πίνακα TROPOS_PLIROMIS.",
        "Το ιστορικό θεάσεων υποστηρίζει τόσο ταινίες (season_number = NULL, episode_number = NULL) όσο και επεισόδια σειρών.",
        "Στον πίνακα SYMMETOXH_SYNTELESTH το γνώρισμα idiotita συμμετέχει στο σύνθετο Primary Key ώστε ένας συντελεστής να μπορεί να έχει πολλαπλούς ρόλους (π.χ. σκηνοθέτης & ηθοποιός) στο ίδιο έργο.",
    ]

    # 7. ER Diagram Tables
    er_tables = [
        ERTable(
            id="t-title",
            label="ERGO",
            x=50,
            y=50,
            attrs=[
                ERTableAttr("isan", pk=True),
                ERTableAttr("prototypos_titlos"),
                ERTableAttr("etos_kykloforias"),
                ERTableAttr("ilikia_rating"),
                ERTableAttr("kyria_katigoria"),
                ERTableAttr("synopsi"),
            ],
        ),
        ERTable(
            id="t-series",
            label="TILEOPTIKI_SEIRA",
            x=450,
            y=50,
            attrs=[
                ERTableAttr("isan", pk=True, fk=True),
                ERTableAttr("synolo_sezon"),
            ],
        ),
        ERTable(
            id="t-episode",
            label="EPEISODIO",
            x=850,
            y=50,
            attrs=[
                ERTableAttr("isan", pk=True, fk=True),
                ERTableAttr("season_number", pk=True),
                ERTableAttr("episode_number", pk=True),
                ERTableAttr("titlos_epeisodiou"),
                ERTableAttr("diarkeia_lepta"),
                ERTableAttr("hmer_protis_provolis"),
            ],
        ),
        ERTable(
            id="t-movie",
            label="TAINIA",
            x=50,
            y=370,
            attrs=[
                ERTableAttr("isan", pk=True, fk=True),
                ERTableAttr("diarkeia_lepta"),
            ],
        ),
        ERTable(
            id="t-participation",
            label="SYMMETOXH_SYNTELESTH",
            x=450,
            y=370,
            attrs=[
                ERTableAttr("isan", pk=True, fk=True),
                ERTableAttr("am_syntelesti", pk=True, fk=True),
                ERTableAttr("idiotita", pk=True),
                ERTableAttr("onoma_rolou"),
                ERTableAttr("symfonitheisa_amoivi"),
            ],
        ),
        ERTable(
            id="t-creator",
            label="SYNTELESTIS",
            x=850,
            y=370,
            attrs=[
                ERTableAttr("am_syntelesti", pk=True),
                ERTableAttr("onomateponymo"),
                ERTableAttr("kallitexniko_psevdonymo"),
                ERTableAttr("hmer_gennisis"),
                ERTableAttr("ethnikotita"),
                ERTableAttr("viografia"),
            ],
        ),
        ERTable(
            id="t-subscriber",
            label="SYNDROMITIS",
            x=50,
            y=640,
            attrs=[
                ERTableAttr("email", pk=True),
                ERTableAttr("username"),
                ERTableAttr("password_hash"),
                ERTableAttr("hmer_eggrafis"),
                ERTableAttr("xora_xreosis"),
                ERTableAttr("syndromitiko_paketo"),
            ],
        ),
        ERTable(
            id="t-profile",
            label="PROFIL_XRHSTH",
            x=450,
            y=640,
            attrs=[
                ERTableAttr("email", pk=True, fk=True),
                ERTableAttr("profile_name", pk=True),
                ERTableAttr("avatar"),
                ERTableAttr("glossa_diepafis"),
                ERTableAttr("is_kids"),
                ERTableAttr("parental_pin"),
            ],
        ),
        ERTable(
            id="t-history",
            label="ISTORIKO_THEASIS",
            x=850,
            y=640,
            attrs=[
                ERTableAttr("email", pk=True, fk=True),
                ERTableAttr("profile_name", pk=True, fk=True),
                ERTableAttr("isan", pk=True, fk=True),
                ERTableAttr("hmerominia_ora_enarksis", pk=True),
                ERTableAttr("season_number", fk=True),
                ERTableAttr("episode_number", fk=True),
                ERTableAttr("xroniki_proodos_sec"),
                ERTableAttr("is_completed"),
                ERTableAttr("rating_stars"),
                ERTableAttr("hmer_axiologisis"),
            ],
        ),
        ERTable(
            id="t-audio-lang",
            label="GLOSSA_HXOU",
            x=50,
            y=260,
            attrs=[
                ERTableAttr("isan", pk=True, fk=True),
                ERTableAttr("glossa_hxou", pk=True),
            ],
        ),
        ERTable(
            id="t-subtitle-lang",
            label="GLOSSA_YPOTITLON",
            x=450,
            y=240,
            attrs=[
                ERTableAttr("isan", pk=True, fk=True),
                ERTableAttr("glossa_ypotitlon", pk=True),
            ],
        ),
        ERTable(
            id="t-payment-method",
            label="TROPOS_PLIROMIS",
            x=50,
            y=880,
            attrs=[
                ERTableAttr("email", pk=True, fk=True),
                ERTableAttr("typos_pliromis", pk=True),
                ERTableAttr("stoixeia_pliromis", pk=True),
            ],
        ),
    ]

    # 8. ER Diagram Edges
    er_edges = [
        # Media to Series (ISA)
        EREdge("M 310 80 L 450 80", "start-one-mandatory", "end-one-mandatory", "ISA (ΣΕΙΡΑ)", 380, 70),
        # Media to Movie (ISA)
        EREdge("M 180 236 L 180 370", "start-one-mandatory", "end-one-mandatory", "ISA (ΤΑΙΝΙΑ)", 195, 310),
        # Series to Episodes (1:N identifying)
        EREdge("M 710 80 L 850 80", "start-one-mandatory", "end-many-mandatory", "ΠΕΡΙΕΧΕΙ (1:N)", 780, 70),
        # Media to Audio Languages (1:N multivalued)
        EREdge("M 180 236 L 180 260", "start-one-mandatory", "end-many-mandatory", "ΓΛΩΣΣΑ_ΗΧΟΥ (1:N)", 205, 248),
        # Media to Subtitles (1:N multivalued)
        EREdge("M 310 160 L 450 240", "start-one-mandatory", "end-many-mandatory", "ΥΠΟΤΙΤΛΟΙ (1:N)", 380, 195),
        # Media to Participation (1:N)
        EREdge("M 310 180 L 450 400", "start-one-mandatory", "end-many-mandatory", "ΣΥΜΜΕΤΟΧΗ (1:N)", 380, 290),
        # Creator to Participation (1:N)
        EREdge("M 850 410 L 710 410", "start-one-optional", "end-many-mandatory", "ΣΥΜΜΕΤΕΧΕΙ (1:N)", 780, 400),
        # Subscriber to Profile (1:N identifying)
        EREdge("M 310 680 L 450 680", "start-one-mandatory", "end-many-mandatory", "ΔΗΜΙΟΥΡΓΕΙ (1:N)", 380, 670),
        # Subscriber to Payment methods (1:N multivalued)
        EREdge("M 180 828 L 180 880", "start-one-mandatory", "end-many-mandatory", "ΠΛΗΡΩΜΗ (1:N)", 205, 854),
        # Profile to History (1:N)
        EREdge("M 710 680 L 850 680", "start-one-optional", "end-many-mandatory", "ΠΑΡΑΚΟΛΟΥΘΕΙ (1:N)", 780, 670),
        # Media to History (1:N)
        EREdge("M 310 120 L 850 660", "start-one-optional", "end-many-mandatory", "ΠΡΟΒΟΛΗ (1:N)", 580, 390),
    ]

    # 9. Relational Conversion Justifications
    relational_justifications = [
        RelationalJustification(
            title="1. Μετατροπή Ιεραρχίας Γενίκευσης/Εξειδίκευσης (ΕΡΓΟ -> ΤΑΙΝΙΑ, ΤΗΛΕΟΠΤΙΚΗ_ΣΕΙΡΑ)",
            color_class="border-blue-500",
            description="Χρήση Class Table Inheritance: Δημιουργείται ο βασικός πίνακας ERGO (κοινά γνωρίσματα) και οι εξειδικευμένοι πίνακες TAINIA και TILEOPTIKI_SEIRA με Primary Key και ταυτόχρονα Foreign Key το isan προς το ERGO.",
        ),
        RelationalJustification(
            title="2. Μετατροπή Ασθενών Οντοτήτων (ΕΠΕΙΣΟΔΙΟ, ΠΡΟΦΙΛ_ΧΡΗΣΤΗ)",
            color_class="border-red-500",
            description="Ο πίνακας EPEISODIO έχει σύνθετο PK (isan, season_number, episode_number). Ο πίνακας PROFIL_XRHSTH έχει σύνθετο PK (email, profile_name) με Foreign Key προς τον ΣΥΝΔΡΟΜΗΤΗ και ON DELETE CASCADE.",
        ),
        RelationalJustification(
            title="3. Μετατροπή Συσχετίσεων N:M (ΣΥΜΜΕΤΟΧΗ_ΣΥΝΤΕΛΕΣΤΗ, ΙΣΤΟΡΙΚΟ_ΘΕΑΣΗΣ)",
            color_class="border-amber-500",
            description="Δημιουργούνται οι πίνακες SYMMETOXH_SYNTELESTH (σύνθετο PK: isan, am_syntelesti, idiotita) και ISTORIKO_THEASIS (σύνθετο PK: email, profile_name, isan, hmerominia_ora_enarksis).",
        ),
        RelationalJustification(
            title="4. Μετατροπή Πλειότιμων Γνωρισμάτων (ΓΛΩΣΣΕΣ_ΗΧΟΥ, ΓΛΩΣΣΕΣ_ΥΠΟΤΙΤΛΩΝ, ΤΡΟΠΟΙ_ΠΛΗΡΩΜΗΣ)",
            color_class="border-purple-500",
            description="Τα πλειότιμα γνωρίσματα αναλύονται στους σχεσιακούς πίνακες GLOSSA_HXOU (isan, glossa_hxou), GLOSSA_YPOTITLON (isan, glossa_ypotitlon) και TROPOS_PLIROMIS (email, typos_pliromis, stoixeia_pliromis).",
        ),
    ]

    # 10. Complete Production SQL DDL
    sql_ddl = """-- ==========================================================
-- PostgreSQL / MySQL Relational Schema for Streaming Platform
-- Case Study: Exam Paper 6 (Πλατφόρμα Συνεχούς Ροής Βίντεο)
-- ==========================================================

-- 1. Superclass Entity: ERGO (Media Item)
CREATE TABLE ERGO (
    isan VARCHAR(30) PRIMARY KEY,
    prototypos_titlos VARCHAR(150) NOT NULL,
    etos_kykloforias INT NOT NULL CHECK (etos_kykloforias >= 1895),
    ilikia_rating VARCHAR(10) NOT NULL CHECK (ilikia_rating IN ('G', 'PG', 'PG-13', '16+', '18+')),
    kyria_katigoria VARCHAR(50) NOT NULL,
    synopsi TEXT NOT NULL
);

-- 2. Multi-valued Attribute: GLOSSA_HXOU
CREATE TABLE GLOSSA_HXOU (
    isan VARCHAR(30) NOT NULL,
    glossa_hxou VARCHAR(50) NOT NULL,
    PRIMARY KEY (isan, glossa_hxou),
    FOREIGN KEY (isan) REFERENCES ERGO(isan) ON DELETE CASCADE
);

-- 3. Multi-valued Attribute: GLOSSA_YPOTITLON
CREATE TABLE GLOSSA_YPOTITLON (
    isan VARCHAR(30) NOT NULL,
    glossa_ypotitlon VARCHAR(50) NOT NULL,
    PRIMARY KEY (isan, glossa_ypotitlon),
    FOREIGN KEY (isan) REFERENCES ERGO(isan) ON DELETE CASCADE
);

-- 4. Subclass Entity: TAINIA
CREATE TABLE TAINIA (
    isan VARCHAR(30) PRIMARY KEY,
    diarkeia_lepta INT NOT NULL CHECK (diarkeia_lepta > 0),
    FOREIGN KEY (isan) REFERENCES ERGO(isan) ON DELETE CASCADE
);

-- 5. Subclass Entity: TILEOPTIKI_SEIRA
CREATE TABLE TILEOPTIKI_SEIRA (
    isan VARCHAR(30) PRIMARY KEY,
    synolo_sezon INT NOT NULL DEFAULT 1 CHECK (synolo_sezon > 0),
    FOREIGN KEY (isan) REFERENCES ERGO(isan) ON DELETE CASCADE
);

-- 6. Weak Entity: EPEISODIO
CREATE TABLE EPEISODIO (
    isan VARCHAR(30) NOT NULL,
    season_number INT NOT NULL CHECK (season_number > 0),
    episode_number INT NOT NULL CHECK (episode_number > 0),
    titlos_epeisodiou VARCHAR(150) NOT NULL,
    diarkeia_lepta INT NOT NULL CHECK (diarkeia_lepta > 0),
    hmer_protis_provolis DATE NOT NULL,
    PRIMARY KEY (isan, season_number, episode_number),
    FOREIGN KEY (isan) REFERENCES TILEOPTIKI_SEIRA(isan) ON DELETE CASCADE
);

-- 7. Entity: SYNTELESTIS (Cast & Crew)
CREATE TABLE SYNTELESTIS (
    am_syntelesti VARCHAR(15) PRIMARY KEY,
    onomateponymo VARCHAR(100) NOT NULL,
    kallitexniko_psevdonymo VARCHAR(100),
    hmer_gennisis DATE NOT NULL,
    ethnikotita VARCHAR(50) NOT NULL,
    viografia TEXT
);

-- 8. Junction Table: SYMMETOXH_SYNTELESTH (N:M)
CREATE TABLE SYMMETOXH_SYNTELESTH (
    isan VARCHAR(30) NOT NULL,
    am_syntelesti VARCHAR(15) NOT NULL,
    idiotita VARCHAR(50) NOT NULL CHECK (idiotita IN ('Σκηνοθέτης', 'Σεναριογράφος', 'Πρωταγωνιστής', 'Ηθοποιός Β Ρόλου', 'Παραγωγός')),
    onoma_rolou VARCHAR(100),
    symfonitheisa_amoivi DECIMAL(12, 2) CHECK (symfonitheisa_amoivi >= 0),
    PRIMARY KEY (isan, am_syntelesti, idiotita),
    FOREIGN KEY (isan) REFERENCES ERGO(isan) ON DELETE CASCADE,
    FOREIGN KEY (am_syntelesti) REFERENCES SYNTELESTIS(am_syntelesti) ON DELETE CASCADE
);

-- 9. Entity: SYNDROMITIS (Subscriber)
CREATE TABLE SYNDROMITIS (
    email VARCHAR(100) PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    hmer_eggrafis DATE NOT NULL,
    xora_xreosis VARCHAR(50) NOT NULL,
    syndromitiko_paketo VARCHAR(30) NOT NULL CHECK (syndromitiko_paketo IN ('Basic', 'Standard HD', 'Premium 4K'))
);

-- 10. Multi-valued Attribute: TROPOS_PLIROMIS
CREATE TABLE TROPOS_PLIROMIS (
    email VARCHAR(100) NOT NULL,
    typos_pliromis VARCHAR(30) NOT NULL CHECK (typos_pliromis IN ('Credit Card', 'Debit Card', 'PayPal', 'Direct Debit')),
    stoixeia_pliromis VARCHAR(100) NOT NULL,
    PRIMARY KEY (email, typos_pliromis, stoixeia_pliromis),
    FOREIGN KEY (email) REFERENCES SYNDROMITIS(email) ON DELETE CASCADE
);

-- 11. Weak Entity: PROFIL_XRHSTH (User Profile)
CREATE TABLE PROFIL_XRHSTH (
    email VARCHAR(100) NOT NULL,
    profile_name VARCHAR(50) NOT NULL,
    avatar VARCHAR(100) DEFAULT 'default_avatar.png',
    glossa_diepafis VARCHAR(20) DEFAULT 'el',
    is_kids BOOLEAN NOT NULL DEFAULT FALSE,
    parental_pin VARCHAR(4),
    PRIMARY KEY (email, profile_name),
    FOREIGN KEY (email) REFERENCES SYNDROMITIS(email) ON DELETE CASCADE
);

-- 12. Junction Table: ISTORIKO_THEASIS (N:M Viewing & Ratings)
CREATE TABLE ISTORIKO_THEASIS (
    email VARCHAR(100) NOT NULL,
    profile_name VARCHAR(50) NOT NULL,
    isan VARCHAR(30) NOT NULL,
    hmerominia_ora_enarksis TIMESTAMP NOT NULL,
    season_number INT,
    episode_number INT,
    xroniki_proodos_sec INT NOT NULL DEFAULT 0 CHECK (xroniki_proodos_sec >= 0),
    is_completed BOOLEAN NOT NULL DEFAULT FALSE,
    rating_stars INT CHECK (rating_stars BETWEEN 1 AND 5),
    hmer_axiologisis DATE,
    PRIMARY KEY (email, profile_name, isan, hmerominia_ora_enarksis),
    FOREIGN KEY (email, profile_name) REFERENCES PROFIL_XRHSTH(email, profile_name) ON DELETE CASCADE,
    FOREIGN KEY (isan) REFERENCES ERGO(isan) ON DELETE CASCADE,
    FOREIGN KEY (isan, season_number, episode_number) REFERENCES EPEISODIO(isan, season_number, episode_number) ON DELETE CASCADE
);"""

    return Scenario(
        id="streaming_platform",
        title="Σύστημα Πλατφόρμας Συνεχούς Ροής Βίντεο (Streaming)",
        subtitle="Μοντελοποίηση Έργων (Ταινιών/Σειρών), Επεισοδίων, Συντελεστών, Συνδρομητών, Προφίλ & Θεάσεων",
        course_tag="Βάσεις Δεδομένων (Πρόοδος 2025-2026 - Θέμα 6)",
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
