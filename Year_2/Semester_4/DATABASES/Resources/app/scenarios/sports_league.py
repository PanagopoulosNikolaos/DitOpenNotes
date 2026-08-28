"""Sports League Management case study scenario module.

Contains the complete parsed and modeled ER analysis for the National Sports League Federation
(Teams, Athletes, Coaches, Player Contracts, Matches, Match Events & Injury Records),
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


def createSportsLeagueScenario() -> Scenario:
    """Constructs and returns the Sports League database scenario.

    Returns:
        Scenario: Fully populated scenario instance.
    """
    # 1. Text Paragraphs with Interactive Segments
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Μια εθνική αθλητική ομοσπονδία επαγγελματικού πρωταθλήματος σχεδιάζει το νέο πληροφοριακό σύστημα βάσεων δεδομένων για τη διαχείριση των "),
                TextSegment(
                    text="ομάδων",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Strong Entity): Αθλητικός σύλλογος/ομάδα με μοναδικό Team ID.",
                ),
                TextSegment(text=", των "),
                TextSegment(
                    text="αθλητών",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Strong Entity): Επαγγελματίας παίκτης με μοναδικό Αριθμό Δελτίου Αθλητή.",
                ),
                TextSegment(text=", των "),
                TextSegment(
                    text="προπονητών",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Strong Entity): Προπονητής με μοναδικό αριθμό διπλώματος προπονητικής (Coach ID).",
                ),
                TextSegment(text=", των "),
                TextSegment(
                    text="αγώνων πρωταθλήματος",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Strong Entity): Προγραμματισμένος αγώνας με μοναδικό Match ID μεταξύ δύο ομάδων.",
                ),
                TextSegment(text=", των "),
                TextSegment(
                    text="στατιστικών συμβάντων αγώνα",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΑΣΘΕΝΗΣ ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-weak",
                    tooltip="Ασθενής Οντότητα (Weak Entity): Κρίσιμο συμβάν εντός αγώνα (γκολ, κάρτα, αλλαγή) που προσδιορίζεται από τον αγώνα.",
                ),
                TextSegment(text=" και των "),
                TextSegment(
                    text="περιστατικών τραυματισμού",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΑΣΘΕΝΗΣ ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-weak",
                    tooltip="Ασθενής Οντότητα (Weak Entity): Ιατρικό ιστορικό τραυματισμών αθλητή.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color=None,
        ),
        Paragraph(
            segments=[
                TextSegment(text="1. <strong>Ομάδες (Teams):</strong> Κάθε ομάδα χαρακτηρίζεται από έναν "),
                TextSegment(
                    text="μοναδικό κωδικό ομάδας (Team ID)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Μοναδικός κωδικός ομάδας.",
                ),
                TextSegment(text=", την "),
                TextSegment(
                    text="επίσημη ονομασία της (π.χ. 'Αθλητικός Όμιλος Αθηνών')",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Υποψήφιο Κλειδί (Candidate Key): Μοναδική επίσημη επωνυμία συλλόγου.",
                ),
                TextSegment(text=", την "),
                TextSegment(text="πόλη έδρας", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", το "),
                TextSegment(text="έτος ίδρυσης", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", το "),
                TextSegment(text="ιδιόκτητο ή μισθωμένο γήπεδο/στάδιο", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και τη "),
                TextSegment(text="χωρητικότητα θεατών", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=". Κάθε ομάδα έχει τα επίσημα "),
                TextSegment(
                    text="χρώματά της (π.χ. 'Κυανό', 'Λευκό') που καταγράφονται ως λίστα χρωμάτων",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΠΛΕΙΟΤΙΜΟ",
                    badge_class="badge-attr-multi",
                    tooltip="Πλειότιμο Γνώρισμα: Εξάγεται στον σχεσιακό πίνακα XROMATA_OMADAS.",
                ),
                TextSegment(text=". Κάθε ομάδα έχει υποχρεωτικά έναν και μόνο "),
                TextSegment(
                    text="Επικεφαλής Προπονητή (Head Coach)",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ 1:1",
                    badge_class="badge-rel-11",
                    tooltip="Συσχέτιση 1:1 (ΕΠΙΚΕΦΑΛΗΣ_ΠΡΟΠΟΝΗΤΗΣ): Ολική συμμετοχή για Ομάδα, μερική για Προπονητή.",
                ),
                TextSegment(text=", για τον οποίο καταγράφεται η "),
                TextSegment(
                    text="ημερομηνία έναρξης της θητείας του",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ ΣΧΕΣΗΣ",
                    badge_class="badge-attr-composite",
                    tooltip="Γνώρισμα Συσχέτισης: Αποθηκεύεται στον σχεσιακό πίνακα OMADA.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-blue-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="2. <strong>Προπονητές (Coaches):</strong> Για κάθε προπονητή καταγράφονται: ο "),
                TextSegment(
                    text="μοναδικός αριθμός διπλώματος προπονητικής (Coach ID)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Μοναδικός αριθμός διπλώματος προπονητικής.",
                ),
                TextSegment(text=", ο "),
                TextSegment(
                    text="ΑΦΜ",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Υποψήφιο Κλειδί (Candidate Key): Αριθμός Φορολογικού Μητρώου προπονητή.",
                ),
                TextSegment(text=", το "),
                TextSegment(text="ονοματεπώνυμο", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(text="ημερομηνία γέννησης", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(text="εθνικότητα", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(text="κατηγορία διπλώματος (π.χ. 'UEFA Pro', 'FIBA Coach 1')", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και το "),
                TextSegment(text="τηλέφωνο επικοινωνίας", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=". Ένας προπονητής μπορεί να "),
                TextSegment(
                    text="εργάζεται ως επικεφαλής προπονητής σε μία μόνο ομάδα κάθε φορά",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΠΕΡΙΟΡΙΣΜΟΣ 1:1",
                    badge_class="badge-rel-11",
                    tooltip="Περιορισμός Μοναδικότητας: Head Coach σε το πολύ 1 ομάδα ταυτόχρονα.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-amber-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="3. <strong>Αθλητές & Επαγγελματικά Συμβόλαια (Athletes & Contracts):</strong> Για κάθε αθλητή καταγράφονται: ο "),
                TextSegment(
                    text="μοναδικός Αριθμός Δελτίου Αθλητή",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Μοναδικός αριθμός δελτίου ομοσπονδίας.",
                ),
                TextSegment(text=", ο "),
                TextSegment(
                    text="Αριθμός Ταυτότητας (ΑΔΤ)",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Υποψήφιο Κλειδί (Candidate Key): Αριθμός Δελτίου Ταυτότητας.",
                ),
                TextSegment(text=", το "),
                TextSegment(text="όνομα", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", το "),
                TextSegment(text="επώνυμο", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(text="ημερομηνία γέννησης", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", το "),
                TextSegment(text="ύψος (σε εκατοστά)", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", το "),
                TextSegment(text="βάρος (σε κιλά)", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(text="εθνικότητα", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και η "),
                TextSegment(text="κύρια αγωνιστική θέση (π.χ. 'Τερματοφύλακας', 'Κεντρικός Αμυντικός', 'Επιθετικός')", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=". Κάθε αθλητής δεσμεύεται με "),
                TextSegment(
                    text="επίσημο επαγγελματικό συμβόλαιο με μία συγκεκριμένη ομάδα",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ 1:N",
                    badge_class="badge-rel-1n",
                    tooltip="Συσχέτιση 1:N (ΣΥΜΒΟΛΑΙΟ): Κάθε παίκτης ανήκει σε 1 ομάδα. Η ομάδα διαθέτει πολλούς παίκτες.",
                ),
                TextSegment(text=". Για κάθε συμβόλαιο καταγράφονται ο "),
                TextSegment(text="αριθμός φανέλας του παίκτη (Jersey Number)", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ ΣΧΕΣΗΣ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(text="ημερομηνία έναρξης", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ ΣΧΕΣΗΣ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(text="ημερομηνία λήξης", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ ΣΧΕΣΗΣ", badge_class="badge-attr-simple"),
                TextSegment(text=" και οι "),
                TextSegment(text="ετήσιες αποδοχές", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ ΣΧΕΣΗΣ", badge_class="badge-attr-simple"),
                TextSegment(text="."),
            ],
            accent_border_color="border-purple-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="4. <strong>Αγώνες Πρωταθλήματος (League Matches):</strong> Στα πλαίσια του πρωταθλήματος διεξάγονται προγραμματισμένοι αγώνες. Κάθε αγώνας έχει έναν "),
                TextSegment(
                    text="μοναδικό κωδικό αγώνα (Match ID)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Μοναδικός κωδικός αγώνα πρωταθλήματος.",
                ),
                TextSegment(text=", την "),
                TextSegment(text="αγωνιστική ημέρα (Round Number)", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", την "),
                TextSegment(text="ημερομηνία και ώρα έναρξης", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", το "),
                TextSegment(text="γήπεδο διεξαγωγής", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και το "),
                TextSegment(text="ονοματεπώνυμο του διαιτητή", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=". Κάθε αγώνας διεξάγεται μεταξύ δύο συγκεκριμένων ομάδων: της "),
                TextSegment(
                    text="Γηπεδούχου Ομάδας (Home Team)",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ 1:N (ΡΟΛΟΣ 1)",
                    badge_class="badge-rel-1n",
                    tooltip="Ρόλος 1 Συσχέτισης με ΟΜΑΔΑ: Γηπεδούχος ομάδα (home_team_id).",
                ),
                TextSegment(text=" και της "),
                TextSegment(
                    text="Φιλοξενούμενης Ομάδας (Away Team)",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ 1:N (ΡΟΛΟΣ 2)",
                    badge_class="badge-rel-1n",
                    tooltip="Ρόλος 2 Συσχέτισης με ΟΜΑΔΑ: Φιλοξενούμενη ομάδα (away_team_id).",
                ),
                TextSegment(text=". Μετά τη λήξη του αγώνα καταγράφεται το "),
                TextSegment(
                    text="τελικό σκορ (επιτευχθέντα τέρματα γηπεδούχου και φιλοξενούμενης ομάδας)",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑΤΑ",
                    badge_class="badge-attr-simple",
                    tooltip="Τελικό Σκορ: score_home, score_away (NULL πριν τη διεξαγωγή του αγώνα).",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-emerald-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="5. <strong>Συμβάντα Αγώνα (Match Events):</strong> Κατά τη διάρκεια κάθε αγώνα καταγράφονται λεπτομερώς όλα τα κρίσιμα συμβάντα. Κάθε συμβάν προσδιορίζεται από έναν "),
                TextSegment(
                    text="αύξοντα αριθμό συμβάντος εντός του συγκεκριμένου αγώνα",
                    is_highlight=True,
                    category="key",
                    tag_label="ΜΕΡΙΚΟ ΚΛΕΙΔΙ",
                    badge_class="badge-key-partial",
                    tooltip="Μερικό Κλειδί (Partial Key): Αύξων αριθμός συμβάντος (event_seq_no) εντός του συγκεκριμένου match_id.",
                ),
                TextSegment(text=", το "),
                TextSegment(text="αγωνιστικό λεπτό (Minute, π.χ. 45', 89')", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", τον "),
                TextSegment(text="τύπο συμβάντος ('Γκολ', 'Κίτρινη Κάρτα', 'Κόκκινη Κάρτα', 'Αλλαγή', 'Πέναλτι')", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και τον "),
                TextSegment(
                    text="εμπλεκόμενο αθλητή που προκάλεσε το συμβάν",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ 1:N",
                    badge_class="badge-rel-1n",
                    tooltip="Συσχέτιση 1:N (ΠΡΟΚΑΛΕΣΕ_ΣΥΜΒΑΝ): Foreign Key athlete_id προς τον πίνακα ΑΘΛΗΤΗΣ.",
                ),
                TextSegment(text=". Ένα συμβάν "),
                TextSegment(
                    text="δεν μπορεί να υπάρξει αυτόνομα χωρίς τον αντίστοιχο αγώνα (Ασθενής Οντότητα)",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΑΣΘΕΝΗΣ ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-weak",
                    tooltip="Ασθενής Οντότητα: Σύνθετο PK (match_id, event_seq_no) με ON DELETE CASCADE.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-red-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="6. <strong>Ιατρικός Φάκελος & Τραυματισμοί (Injury Records):</strong> Για κάθε αθλητή τηρείται ιατρικός φάκελος καταγραφής τραυματισμών. Για κάθε περιστατικό καταγράφονται ένας "),
                TextSegment(
                    text="αύξων αριθμός περιστατικού για τον συγκεκριμένο αθλητή",
                    is_highlight=True,
                    category="key",
                    tag_label="ΜΕΡΙΚΟ ΚΛΕΙΔΙ",
                    badge_class="badge-key-partial",
                    tooltip="Μερικό Κλειδί (Partial Key): Αύξων αριθμός περιστατικού (incident_no) εντός του συγκεκριμένου αθλητή.",
                ),
                TextSegment(text=", η "),
                TextSegment(text="ημερομηνία τραυματισμού", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", το "),
                TextSegment(text="είδος του τραυματισμού", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(text="προβλεπόμενη διάρκεια αποθεραπείας (σε εβδομάδες)", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και η "),
                TextSegment(text="τελική ημερομηνία ιατρικής επανόδου στους αγωνιστικούς χώρους", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text="."),
            ],
            accent_border_color="border-cyan-500",
        ),
    ]

    # 2. Complete Entity List with Detailed Attributes
    entities = [
        Entity(
            name="ΟΜΑΔΑ",
            entity_type="Ισχυρή Οντότητα",
            is_weak=False,
            owner_entity=None,
            justification="Αυτοτελής αθλητικός σύλλογος/ομάδα με μοναδικό Team ID.",
            attributes=[
                Attribute("team_id", "Απλό / Μονότιμο", is_pk=True, notes="Μοναδικός κωδικός ομάδας."),
                Attribute("onomasia", "Απλό / Μονότιμο", is_candidate=True, notes="Μοναδική επίσημη ονομασία ομάδας."),
                Attribute("poli_edras", "Απλό / Μονότιμο", notes="Πόλη φυσικής έδρας του συλλόγου."),
                Attribute("etos_idrysis", "Απλό / Μονότιμο", notes="Έτος ίδρυσης συλλόγου."),
                Attribute("gipedo_stadio", "Απλό / Μονότιμο", notes="Ονομασία έδρας/σταδίου."),
                Attribute("xoritikotita", "Απλό / Μονότιμο", notes="Χωρητικότητα θεατών σταδίου."),
                Attribute("xromata", "Πλειότιμο", notes="Επίσημα χρώματα συλλόγου (εξάγεται στον πίνακα XROMATA_OMADAS)."),
            ],
        ),
        Entity(
            name="ΠΡΟΠΟΝΗΤΗΣ",
            entity_type="Ισχυρή Οντότητα",
            is_weak=False,
            owner_entity=None,
            justification="Φυσικό πρόσωπο επαγγελματία προπονητή με μοναδικό αριθμό διπλώματος.",
            attributes=[
                Attribute("coach_id", "Απλό / Μονότιμο", is_pk=True, notes="Μοναδικός αριθμός διπλώματος προπονητικής."),
                Attribute("afm", "Απλό / Μονότιμο", is_candidate=True, notes="Αριθμός Φορολογικού Μητρώου."),
                Attribute("onomateponymo", "Απλό / Μονότιμο", notes="Πλήρες ονοματεπώνυμο προπονητή."),
                Attribute("hmer_gennisis", "Απλό / Μονότιμο", notes="Ημερομηνία γέννησης."),
                Attribute("ethnikotita", "Απλό / Μονότιμο", notes="Χώρα καταγωγής/υπηκοότητα."),
                Attribute("katigoria_diplomatos", "Απλό / Μονότιμο", notes="Βαθμίδα διπλώματος (π.χ. 'UEFA Pro', 'FIBA 1')."),
                Attribute("tilefono", "Απλό / Μονότιμο", notes="Τηλέφωνο επικοινωνίας."),
            ],
        ),
        Entity(
            name="ΑΘΛΗΤΗΣ",
            entity_type="Ισχυρή Οντότητα",
            is_weak=False,
            owner_entity=None,
            justification="Επαγγελματίας παίκτης με μοναδικό δελτίο αθλητή της ομοσπονδίας.",
            attributes=[
                Attribute("athlete_id", "Απλό / Μονότιμο", is_pk=True, notes="Μοναδικός αριθμός δελτίου αθλητή."),
                Attribute("adt", "Απλό / Μονότιμο", is_candidate=True, notes="Αριθμός Δελτίου Ταυτότητας."),
                Attribute("onoma", "Απλό / Μονότιμο", notes="Όνομα αθλητή."),
                Attribute("eponymo", "Απλό / Μονότιμο", notes="Επώνυμο αθλητή."),
                Attribute("hmer_gennisis", "Απλό / Μονότιμο", notes="Ημερομηνία γέννησης."),
                Attribute("ypsos_cm", "Απλό / Μονότιμο", notes="Ύψος σε εκατοστά."),
                Attribute("varos_kg", "Απλό / Μονότιμο", notes="Σωματικό βάρος σε κιλά."),
                Attribute("ethnikotita", "Απλό / Μονότιμο", notes="Υπηκοότητα αθλητή."),
                Attribute("thesi", "Απλό / Μονότιμο", notes="Κύρια αγωνιστική θέση."),
            ],
        ),
        Entity(
            name="ΑΓΩΝΑΣ",
            entity_type="Ισχυρή Οντότητα",
            is_weak=False,
            owner_entity=None,
            justification="Επίσημος αγώνας πρωταθλήματος μεταξύ γηπεδούχου και φιλοξενούμενης ομάδας.",
            attributes=[
                Attribute("match_id", "Απλό / Μονότιμο", is_pk=True, notes="Μοναδικός κωδικός αγώνα."),
                Attribute("round_number", "Απλό / Μονότιμο", notes="Αγωνιστική ημέρα πρωταθλήματος."),
                Attribute("hmer_ora_enarxis", "Απλό / Μονότιμο", notes="Προγραμματισμένη ημερομηνία και ώρα έναρξης."),
                Attribute("gipedo", "Απλό / Μονότιμο", notes="Στάδιο/γήπεδο διεξαγωγής του αγώνα."),
                Attribute("diaititis", "Απλό / Μονότιμο", notes="Ονοματεπώνυμο πρώτου διαιτητή."),
                Attribute("score_home", "Απλό / Μονότιμο", notes="Τέρματα/πόντοι γηπεδούχου ομάδας."),
                Attribute("score_away", "Απλό / Μονότιμο", notes="Τέρματα/πόντοι φιλοξενούμενης ομάδας."),
            ],
        ),
        Entity(
            name="ΣΥΜΒΑΝ_ΑΓΩΝΑ",
            entity_type="Ασθενής Οντότητα",
            is_weak=True,
            owner_entity="ΑΓΩΝΑΣ",
            justification="Στατιστικό περιστατικό κατά τη ροή του αγώνα που υφίσταται μόνο εντός του συγκεκριμένου αγώνα.",
            attributes=[
                Attribute("event_seq_no", "Απλό / Μονότιμο", is_partial=True, notes="Μερικό κλειδί (αύξων αριθμός συμβάντος εντός του αγώνα)."),
                Attribute("minute", "Απλό / Μονότιμο", notes="Αγωνιστικό λεπτό του συμβάντος (π.χ. 45)."),
                Attribute("event_type", "Απλό / Μονότιμο", notes="'Γκολ', 'Κίτρινη Κάρτα', 'Κόκκινη Κάρτα', 'Αλλαγή', 'Πέναλτι'."),
            ],
        ),
        Entity(
            name="ΠΕΡΙΣΤΑΤΙΚΟ_ΤΡΑΥΜΑΤΙΣΜΟΥ",
            entity_type="Ασθενής Οντότητα",
            is_weak=True,
            owner_entity="ΑΘΛΗΤΗΣ",
            justification="Ιατρικό ιστορικό τραυματισμού που προσδιορίζεται από τον αντίστοιχο αθλητή.",
            attributes=[
                Attribute("incident_no", "Απλό / Μονότιμο", is_partial=True, notes="Μερικό κλειδί (αύξων αριθμός περιστατικού ανά αθλητή)."),
                Attribute("hmer_travmatismou", "Απλό / Μονότιμο", notes="Ημερομηνία εκδήλωσης του τραυματισμού."),
                Attribute("eidos_travmatismou", "Απλό / Μονότιμο", notes="Ιατρική διάγνωση (π.χ. 'Θλάση', 'Ρήξη Χιαστού')."),
                Attribute("diarkeia_apotherapeias_weeks", "Απλό / Μονότιμο", notes="Προβλεπόμενος χρόνος ανάρρωσης σε εβδομάδες."),
                Attribute("hmer_epanodou", "Απλό / Μονότιμο", notes="Πραγματική ημερομηνία επανόδου στις προπονήσεις."),
            ],
        ),
    ]

    # 3. Relationship Attributes
    relationship_attributes = [
        RelationshipAttribute(
            name="hmer_enarxis_thiteias",
            relationship_name="ΕΠΙΚΕΦΑΛΗΣ_ΠΡΟΠΟΝΗΤΗΣ (ΟΜΑΔΑ - ΠΡΟΠΟΝΗΤΗΣ)",
            justification="Ημερομηνία ανάληψης της τεχνικής ηγεσίας της ομάδας.",
        ),
        RelationshipAttribute(
            name="jersey_number",
            relationship_name="ΣΥΜΒΟΛΑΙΟ_ΑΘΛΗΤΗ (ΟΜΑΔΑ - ΑΘΛΗΤΗΣ)",
            justification="Αριθμός φανέλας του αθλητή στην ομάδα.",
        ),
        RelationshipAttribute(
            name="hmer_enarxis_symvolaiou",
            relationship_name="ΣΥΜΒΟΛΑΙΟ_ΑΘΛΗΤΗ (ΟΜΑΔΑ - ΑΘΛΗΤΗΣ)",
            justification="Ημερομηνία έναρξης ισχύος του επαγγελματικού συμβολαίου.",
        ),
        RelationshipAttribute(
            name="hmer_lixis_symvolaiou",
            relationship_name="ΣΥΜΒΟΛΑΙΟ_ΑΘΛΗΤΗ (ΟΜΑΔΑ - ΑΘΛΗΤΗΣ)",
            justification="Ημερομηνία λήξης του επαγγελματικού συμβολαίου.",
        ),
        RelationshipAttribute(
            name="etisies_apodoxes",
            relationship_name="ΣΥΜΒΟΛΑΙΟ_ΑΘΛΗΤΗ (ΟΜΑΔΑ - ΑΘΛΗΤΗΣ)",
            justification="Συμφωνηθείσες ετήσιες οικονομικές αποδοχές του αθλητή.",
        ),
    ]

    # 4. Keys Analysis Table
    keys_analysis = [
        KeyAnalysisRow(
            entity_name="ΟΜΑΔΑ",
            key_count="2 Υποψήφια",
            key_types="Υποψήφια: {team_id}, {onomasia}",
            final_pk_selection="team_id",
            justification="Συμπαγές αλφαριθμητικό κλειδί κατάλληλο για ξένα κλειδιά.",
        ),
        KeyAnalysisRow(
            entity_name="ΠΡΟΠΟΝΗΤΗΣ",
            key_count="2 Υποψήφια",
            key_types="Υποψήφια: {coach_id}, {afm}",
            final_pk_selection="coach_id",
            justification="Επίσημος αριθμός διπλώματος ομοσπονδίας.",
        ),
        KeyAnalysisRow(
            entity_name="ΑΘΛΗΤΗΣ",
            key_count="2 Υποψήφια",
            key_types="Υποψήφια: {athlete_id}, {adt}",
            final_pk_selection="athlete_id",
            justification="Μοναδικός αριθμός δελτίου αθλητή.",
        ),
        KeyAnalysisRow(
            entity_name="ΑΓΩΝΑΣ",
            key_count="1 Υποψήφιο",
            key_types="Υποψήφιο: {match_id}",
            final_pk_selection="match_id",
            justification="Μοναδικός κωδικός αγώνα πρωταθλήματος.",
        ),
        KeyAnalysisRow(
            entity_name="ΣΥΜΒΑΝ_ΑΓΩΝΑ",
            key_count="Ασθενής (1 Μερικό)",
            key_types="Μερικό: {event_seq_no}",
            final_pk_selection="(match_id, event_seq_no)",
            justification="Σύνθετο πρωτεύον κλειδί: match_id + event_seq_no.",
            is_weak=True,
        ),
        KeyAnalysisRow(
            entity_name="ΠΕΡΙΣΤΑΤΙΚΟ_ΤΡΑΥΜΑΤΙΣΜΟΥ",
            key_count="Ασθενής (1 Μερικό)",
            key_types="Μερικό: {incident_no}",
            final_pk_selection="(athlete_id, incident_no)",
            justification="Σύνθετο πρωτεύον κλειδί: athlete_id + incident_no.",
            is_weak=True,
        ),
    ]

    # 5. Relationships List
    relationships = [
        Relationship(
            letter_id="α",
            name="ΕΠΙΚΕΦΑΛΗΣ_ΠΡΟΠΟΝΗΤΗΣ (Head Coach)",
            connected_entities="ΟΜΑΔΑ <-> ΠΡΟΠΟΝΗΤΗΣ",
            cardinality="1:1",
            participation="Ολική για Ομάδα (1,1), Μερική για Προπονητή (0,1)",
            relationship_type="Κανονική Σχέση",
            attributes=["hmer_enarxis_thiteias"],
            justification="Κάθε ομάδα έχει υποχρεωτικά έναν επικεφαλής προπονητή. Ένας προπονητής εργάζεται σε μία ομάδα κάθε φορά.",
        ),
        Relationship(
            letter_id="β",
            name="ΣΥΜΒΟΛΑΙΟ_ΑΘΛΗΤΗ (Player Contract)",
            connected_entities="ΟΜΑΔΑ <-> ΑΘΛΗΤΗΣ",
            cardinality="1:N",
            participation="Ολική για Αθλητή (1,1), Ολική για Ομάδα (1,N)",
            relationship_type="Κανονική Σχέση",
            attributes=["jersey_number", "hmer_enarxis", "hmer_lixis", "etisie_apodoxes"],
            justification="Κάθε παίκτης δεσμεύεται με συμβόλαιο σε 1 ομάδα. Κάθε ομάδα διαθέτει ρόστερ πολλών παικτών.",
        ),
        Relationship(
            letter_id="γ",
            name="ΓΗΠΕΔΟΥΧΟΣ_ΟΜΑΔΑ (Hosts Match)",
            connected_entities="ΟΜΑΔΑ <-> ΑΓΩΝΑΣ",
            cardinality="1:N",
            participation="Ολική για Αγώνα (1,1), Μερική για Ομάδα (0,N)",
            relationship_type="Κανονική Σχέση",
            attributes=[],
            justification="Σε κάθε αγώνα υπάρχει μία γηπεδούχος ομάδα (home_team_id).",
        ),
        Relationship(
            letter_id="δ",
            name="ΦΙΛΟΞΕΝΟΥΜΕΝΗ_ΟΜΑΔΑ (Away Team In Match)",
            connected_entities="ΟΜΑΔΑ <-> ΑΓΩΝΑΣ",
            cardinality="1:N",
            participation="Ολική για Αγώνα (1,1), Μερική για Ομάδα (0,N)",
            relationship_type="Κανονική Σχέση",
            attributes=[],
            justification="Σε κάθε αγώνα υπάρχει μία φιλοξενούμενη ομάδα (away_team_id).",
        ),
        Relationship(
            letter_id="ε",
            name="ΠΕΡΙΛΑΜΒΑΝΕΙ_ΣΥΜΒΑΝ (Match Events)",
            connected_entities="ΑΓΩΝΑΣ <-> ΣΥΜΒΑΝ_ΑΓΩΝΑ",
            cardinality="1:N",
            participation="Ολική για Συμβάν (1,1), Μερική για Αγώνα (0,N)",
            relationship_type="Ταυτοποιούσα Σχέση (Identifying)",
            attributes=[],
            justification="Ταυτοποιούσα σχέση της ασθενούς οντότητας ΣΥΜΒΑΝ_ΑΓΩΝΑ από τον ΑΓΩΝΑ.",
        ),
        Relationship(
            letter_id="στ",
            name="ΠΡΟΚΑΛΕΣΕ_ΣΥΜΒΑΝ (Caused Event)",
            connected_entities="ΑΘΛΗΤΗΣ <-> ΣΥΜΒΑΝ_ΑΓΩΝΑ",
            cardinality="1:N",
            participation="Ολική για Συμβάν (1,1), Μερική για Αθλητή (0,N)",
            relationship_type="Κανονική Σχέση",
            attributes=[],
            justification="Κάθε στατιστικό συμβάν συνδέεται με τον αθλητή που το πραγματοποίησε.",
        ),
        Relationship(
            letter_id="ζ",
            name="ΚΑΤΑΓΡΑΦΗ_ΤΡΑΥΜΑΤΙΣΜΟΥ (Suffered Injury)",
            connected_entities="ΑΘΛΗΤΗΣ <-> ΠΕΡΙΣΤΑΤΙΚΟ_ΤΡΑΥΜΑΤΙΣΜΟΥ",
            cardinality="1:N",
            participation="Ολική για Περιστατικό (1,1), Μερική για Αθλητή (0,N)",
            relationship_type="Ταυτοποιούσα Σχέση (Identifying)",
            attributes=[],
            justification="Ταυτοποιούσα σχέση της ασθενούς οντότητας ΠΕΡΙΣΤΑΤΙΚΟ_ΤΡΑΥΜΑΤΙΣΜΟΥ από τον ΑΘΛΗΤΗ.",
        ),
    ]

    # 6. Design Assumptions
    assumptions = [
        "Ο Επικεφαλής Προπονητής συνδέεται στον πίνακα OMADA μέσω foreign key head_coach_id με UNIQUE constraint (1:1).",
        "Τα επαγγελματικά συμβόλαια ενσωματώνονται στον πίνακα ATHLITIS (1:N με την Ομάδα) καθώς κάθε αθλητής ανήκει σε μία μόνο ομάδα τη δεδομένη χρονική στιγμή.",
        "Τα συμβάντα αγώνα αποτελούν ασθενή οντότητα με σύνθετο κλειδί (match_id, event_seq_no) και συνδέονται μέσω FK με τον αθλητή.",
        "Οι τραυματισμοί αποτελούν ασθενή οντότητα με σύνθετο κλειδί (athlete_id, incident_no).",
    ]

    # 7. ER Diagram Tables
    er_tables = [
        ERTable(
            id="t-team",
            label="OMADA",
            x=60,
            y=50,
            attrs=[
                ERTableAttr("team_id", pk=True),
                ERTableAttr("onomasia"),
                ERTableAttr("poli_edras"),
                ERTableAttr("etos_idrysis"),
                ERTableAttr("gipedo_stadio"),
                ERTableAttr("xoritikotita"),
                ERTableAttr("head_coach_id", fk=True),
                ERTableAttr("hmer_enarxis_thiteias"),
            ],
        ),
        ERTable(
            id="t-coach",
            label="PROPONITIS",
            x=460,
            y=50,
            attrs=[
                ERTableAttr("coach_id", pk=True),
                ERTableAttr("afm"),
                ERTableAttr("onomateponymo"),
                ERTableAttr("hmer_gennisis"),
                ERTableAttr("ethnikotita"),
                ERTableAttr("katigoria_diplomatos"),
                ERTableAttr("tilefono"),
            ],
        ),
        ERTable(
            id="t-color",
            label="XROMA_OMADAS",
            x=860,
            y=50,
            attrs=[
                ERTableAttr("team_id", pk=True, fk=True),
                ERTableAttr("xroma", pk=True),
            ],
        ),
        ERTable(
            id="t-athlete",
            label="ATHLITIS",
            x=60,
            y=360,
            attrs=[
                ERTableAttr("athlete_id", pk=True),
                ERTableAttr("adt"),
                ERTableAttr("onoma"),
                ERTableAttr("eponymo"),
                ERTableAttr("hmer_gennisis"),
                ERTableAttr("ypsos_cm"),
                ERTableAttr("varos_kg"),
                ERTableAttr("ethnikotita"),
                ERTableAttr("thesi"),
                ERTableAttr("team_id", fk=True),
                ERTableAttr("jersey_number"),
                ERTableAttr("hmer_enarxis_symvolaiou"),
                ERTableAttr("hmer_lixis_symvolaiou"),
                ERTableAttr("etisie_apodoxes"),
            ],
        ),
        ERTable(
            id="t-injury",
            label="PERISTATIKO_TRAVMATISMOU",
            x=460,
            y=360,
            attrs=[
                ERTableAttr("athlete_id", pk=True, fk=True),
                ERTableAttr("incident_no", pk=True),
                ERTableAttr("hmer_travmatismou"),
                ERTableAttr("eidos_travmatismou"),
                ERTableAttr("diarkeia_apotherapeias_weeks"),
                ERTableAttr("hmer_epanodou"),
            ],
        ),
        ERTable(
            id="t-event",
            label="SYMVAN_AGONAS",
            x=860,
            y=360,
            attrs=[
                ERTableAttr("match_id", pk=True, fk=True),
                ERTableAttr("event_seq_no", pk=True),
                ERTableAttr("minute"),
                ERTableAttr("event_type"),
                ERTableAttr("athlete_id", fk=True),
            ],
        ),
        ERTable(
            id="t-match",
            label="AGONAS",
            x=460,
            y=630,
            attrs=[
                ERTableAttr("match_id", pk=True),
                ERTableAttr("round_number"),
                ERTableAttr("hmer_ora_enarxis"),
                ERTableAttr("gipedo"),
                ERTableAttr("diaititis"),
                ERTableAttr("home_team_id", fk=True),
                ERTableAttr("away_team_id", fk=True),
                ERTableAttr("score_home"),
                ERTableAttr("score_away"),
            ],
        ),
    ]

    # 8. ER Diagram Edges
    er_edges = [
        # Team to Head Coach (1:1)
        EREdge("M 320 80 L 460 80", "start-one-optional", "end-one-mandatory", "ΕΠΙΚΕΦΑΛΗΣ (1:1)", 390, 70),
        # Team to Colors (1:N)
        EREdge("M 320 120 L 860 120", "start-one-mandatory", "end-many-mandatory", "ΕΧΕΙ_ΧΡΩΜΑΤΑ (1:N)", 590, 110),
        # Team to Athletes (1:N)
        EREdge("M 190 294 L 190 360", "start-one-mandatory", "end-many-mandatory", "ΣΥΜΒΟΛΑΙΟ (1:N)", 205, 330),
        # Athlete to Injuries (1:N identifying)
        EREdge("M 320 400 L 460 400", "start-one-mandatory", "end-many-optional", "ΤΡΑΥΜΑΤΙΣΜΟΙ (1:N)", 390, 390),
        # Athlete to Events (1:N routed under injury table)
        EREdge("M 320 580 L 860 580 L 860 548", "start-one-mandatory", "end-many-optional", "ΠΡΟΚΑΛΕΣΕ (1:N)", 590, 570),
        # Team to Match (Home, 1:N routed around athlete table)
        EREdge("M 320 200 L 400 200 L 400 660 L 460 660", "start-one-mandatory", "end-many-optional", "ΓΗΠΕΔΟΥΧΟΣ (1:N)", 390, 430),
        # Team to Match (Away, 1:N routed around athlete table)
        EREdge("M 320 230 L 420 230 L 420 700 L 460 700", "start-one-mandatory", "end-many-optional", "ΦΙΛΟΞΕΝΟΥΜΕΝΗ (1:N)", 410, 470),
        # Match to Events (1:N identifying)
        EREdge("M 720 650 L 860 480", "start-one-mandatory", "end-many-optional", "ΠΕΡΙΛΑΜΒΑΝΕΙ (1:N)", 780, 570),
    ]

    # 9. Relational Conversion Justifications
    relational_justifications = [
        RelationalJustification(
            title="1. Μετατροπή Συσχέτισης 1:1 (ΕΠΙΚΕΦΑΛΗΣ_ΠΡΟΠΟΝΗΤΗΣ)",
            color_class="border-blue-500",
            description="Η ολική συμμετοχή της Ομάδας επιβάλλει την τοποθέτηση του head_coach_id στον πίνακα OMADA με UNIQUE constraint, διασφαλίζοντας ότι ένας προπονητής διευθύνει το πολύ μία ομάδα.",
        ),
        RelationalJustification(
            title="2. Μετατροπή Πλειότιμου Γνωρίσματος (ΧΡΩΜΑΤΑ_ΟΜΑΔΑΣ)",
            color_class="border-purple-500",
            description="Το πλειότιμο γνώρισμα των χρωμάτων εξάγεται στον σχεσιακό πίνακα XROMA_OMADAS με σύνθετο Primary Key (team_id, xroma) και foreign key προς την ομάδα.",
        ),
        RelationalJustification(
            title="3. Μετατροπή Ασθενών Οντοτήτων (ΣΥΜΒΑΝ_ΑΓΩΝΑ, ΠΕΡΙΣΤΑΤΙΚΟ_ΤΡΑΥΜΑΤΙΣΜΟΥ)",
            color_class="border-red-500",
            description="Ο πίνακας SYMVAN_AGONAS έχει σύνθετο PK (match_id, event_seq_no) και ON DELETE CASCADE. Ο πίνακας PERISTATIKO_TRAVMATISMOU έχει σύνθετο PK (athlete_id, incident_no).",
        ),
        RelationalJustification(
            title="4. Διπλή Συσχέτιση 1:N με Ρόλους (ΓΗΠΕΔΟΥΧΟΣ & ΦΙΛΟΞΕΝΟΥΜΕΝΗ ΟΜΑΔΑ)",
            color_class="border-amber-500",
            description="Στον πίνακα AGONAS συμπεριλαμβάνονται δύο διακριτά Foreign Keys προς τον πίνακα OMADA (home_team_id, away_team_id) με CHECK constraint ώστε home_team_id <> away_team_id.",
        ),
    ]

    # 10. Complete Production SQL DDL
    sql_ddl = """-- ==========================================================
-- PostgreSQL / MySQL Relational Schema for Sports League Federation
-- Case Study: Exam Paper 8 (Εθνικό Πρωτάθλημα & Ομοσπονδία)
-- ==========================================================

-- 1. Entity: PROPONITIS (Coaches)
CREATE TABLE PROPONITIS (
    coach_id VARCHAR(15) PRIMARY KEY,
    afm VARCHAR(10) NOT NULL UNIQUE,
    onomateponymo VARCHAR(100) NOT NULL,
    hmer_gennisis DATE NOT NULL,
    ethnikotita VARCHAR(50) NOT NULL,
    katigoria_diplomatos VARCHAR(50) NOT NULL,
    tilefono VARCHAR(20) NOT NULL
);

-- 2. Entity: OMADA (Teams)
CREATE TABLE OMADA (
    team_id VARCHAR(10) PRIMARY KEY,
    onomasia VARCHAR(100) NOT NULL UNIQUE,
    poli_edras VARCHAR(60) NOT NULL,
    etos_idrysis INT NOT NULL CHECK (etos_idrysis >= 1850),
    gipedo_stadio VARCHAR(100) NOT NULL,
    xoritikotita INT NOT NULL CHECK (xoritikotita > 0),
    head_coach_id VARCHAR(15) NOT NULL UNIQUE,
    hmer_enarxis_thiteias DATE NOT NULL,
    FOREIGN KEY (head_coach_id) REFERENCES PROPONITIS(coach_id) ON DELETE RESTRICT
);

-- 3. Multi-valued Attribute: XROMA_OMADAS
CREATE TABLE XROMA_OMADAS (
    team_id VARCHAR(10) NOT NULL,
    xroma VARCHAR(30) NOT NULL,
    PRIMARY KEY (team_id, xroma),
    FOREIGN KEY (team_id) REFERENCES OMADA(team_id) ON DELETE CASCADE
);

-- 4. Entity: ATHLITIS (Athletes & Professional Contracts)
CREATE TABLE ATHLITIS (
    athlete_id VARCHAR(20) PRIMARY KEY,
    adt VARCHAR(10) NOT NULL UNIQUE,
    onoma VARCHAR(50) NOT NULL,
    eponymo VARCHAR(50) NOT NULL,
    hmer_gennisis DATE NOT NULL,
    ypsos_cm INT NOT NULL CHECK (ypsos_cm BETWEEN 120 AND 250),
    varos_kg INT NOT NULL CHECK (varos_kg BETWEEN 40 AND 200),
    ethnikotita VARCHAR(50) NOT NULL,
    thesi VARCHAR(50) NOT NULL,
    team_id VARCHAR(10) NOT NULL,
    jersey_number INT NOT NULL CHECK (jersey_number BETWEEN 1 AND 99),
    hmer_enarxis_symvolaiou DATE NOT NULL,
    hmer_lixis_symvolaiou DATE NOT NULL,
    etisie_apodoxes DECIMAL(12, 2) NOT NULL CHECK (etisie_apodoxes >= 0),
    FOREIGN KEY (team_id) REFERENCES OMADA(team_id) ON DELETE RESTRICT,
    CHECK (hmer_lixis_symvolaiou > hmer_enarxis_symvolaiou)
);

-- 5. Weak Entity: PERISTATIKO_TRAVMATISMOU (Injury Records)
CREATE TABLE PERISTATIKO_TRAVMATISMOU (
    athlete_id VARCHAR(20) NOT NULL,
    incident_no INT NOT NULL CHECK (incident_no > 0),
    hmer_travmatismou DATE NOT NULL,
    eidos_travmatismou VARCHAR(100) NOT NULL,
    diarkeia_apotherapeias_weeks INT NOT NULL CHECK (diarkeia_apotherapeias_weeks >= 0),
    hmer_epanodou DATE,
    PRIMARY KEY (athlete_id, incident_no),
    FOREIGN KEY (athlete_id) REFERENCES ATHLITIS(athlete_id) ON DELETE CASCADE
);

-- 6. Entity: AGONAS (League Matches)
CREATE TABLE AGONAS (
    match_id VARCHAR(20) PRIMARY KEY,
    round_number INT NOT NULL CHECK (round_number > 0),
    hmer_ora_enarxis TIMESTAMP NOT NULL,
    gipedo VARCHAR(100) NOT NULL,
    diaititis VARCHAR(100) NOT NULL,
    home_team_id VARCHAR(10) NOT NULL,
    away_team_id VARCHAR(10) NOT NULL,
    score_home INT CHECK (score_home >= 0),
    score_away INT CHECK (score_away >= 0),
    FOREIGN KEY (home_team_id) REFERENCES OMADA(team_id) ON DELETE RESTRICT,
    FOREIGN KEY (away_team_id) REFERENCES OMADA(team_id) ON DELETE RESTRICT,
    CHECK (home_team_id <> away_team_id)
);

-- 7. Weak Entity: SYMVAN_AGONAS (Match Events)
CREATE TABLE SYMVAN_AGONAS (
    match_id VARCHAR(20) NOT NULL,
    event_seq_no INT NOT NULL CHECK (event_seq_no > 0),
    minute INT NOT NULL CHECK (minute BETWEEN 1 AND 130),
    event_type VARCHAR(40) NOT NULL CHECK (
        event_type IN ('Γκολ', 'Κίτρινη Κάρτα', 'Κόκκινη Κάρτα', 'Αλλαγή', 'Πέναλτι', 'Αυτογκόλ')
    ),
    athlete_id VARCHAR(20) NOT NULL,
    PRIMARY KEY (match_id, event_seq_no),
    FOREIGN KEY (match_id) REFERENCES AGONAS(match_id) ON DELETE CASCADE,
    FOREIGN KEY (athlete_id) REFERENCES ATHLITIS(athlete_id) ON DELETE RESTRICT
);

-- Performance Indexes
CREATE INDEX idx_athlete_team ON ATHLITIS(team_id);
CREATE INDEX idx_match_teams ON AGONAS(home_team_id, away_team_id, round_number);
CREATE INDEX idx_events_match ON SYMVAN_AGONAS(match_id, minute);
CREATE INDEX idx_injuries_athlete ON PERISTATIKO_TRAVMATISMOU(athlete_id);
"""

    return Scenario(
        id="sports_league",
        title="Σύστημα Διαχείρισης Εθνικού Πρωταθλήματος & Ομοσπονδίας",
        subtitle="Ομάδες, Αθλητές, Προπονητές, Επαγγελματικά Συμβόλαια, Αγώνες Πρωταθλήματος, Συμβάντα Αγώνα & Ιατρικό Ιστορικό",
        course_tag="Βάσεις Δεδομένων (Πρόοδος 2025-2026 - Θέμα 8)",
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
