"""Maritime Shipping and Fleet Management case study scenario module.

Contains the complete parsed and modeled ER analysis for the International Maritime
Shipping Company (Vessels, Ports, Voyages, Seafarers, Embarkation Contracts, Statutory Inspections),
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


def createMaritimeShippingScenario() -> Scenario:
    """Constructs and returns the Maritime Fleet Management database scenario.

    Returns:
        Scenario: Fully populated scenario instance.
    """
    # 1. Text Paragraphs with Interactive Segments
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Μια διεθνής ναυτιλιακή εταιρεία διαχείρισης εμπορικών πλοίων (ποντοπόρα πλοία ξηρού φορτίου και δεξαμενόπλοια) αποφάσισε να αντικαταστήσει τα διάσπαρτα συστήματα αρχείων που χρησιμοποιούσε με ένα κεντρικό Σύστημα Διαχείρισης Βάσεων Δεδομένων (ΣΔΒΔ), προκειμένου να διαχειρίζεται αποδοτικά τον "),
                TextSegment(
                    text="στόλο (πλοία)",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Strong Entity): Ποντοπόρο σκάφος με μοναδικό αριθμό IMO και Call Sign.",
                ),
                TextSegment(text=", τα "),
                TextSegment(
                    text="λιμάνια προσέγγισης",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Strong Entity): Λιμένας με μοναδικό κωδικό UN/LOCODE.",
                ),
                TextSegment(text=", τα "),
                TextSegment(
                    text="δρομολόγια/ταξίδια",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Strong Entity): Εμπορικό ταξίδι με μοναδικό Voyage Code.",
                ),
                TextSegment(text=", τις "),
                TextSegment(
                    text="ναυτολογήσεις πληρωμάτων",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΣΥΣΧΕΤΙΣΤΙΚΗ",
                    badge_class="badge-entity-strong",
                    tooltip="Συσχετιστική Οντότητα (Associative Entity): Σύμβαση ναυτολόγησης ναυτικού σε πλοίο.",
                ),
                TextSegment(text=" και τις "),
                TextSegment(
                    text="τακτικές επιθεωρήσεις ασφαλείας",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΑΣΘΕΝΗΣ ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-weak",
                    tooltip="Ασθενής Οντότητα (Weak Entity): Έλεγχος πλοϊμότητας εξαρτώμενος υπαρκτικά από το πλοίο.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color=None,
        ),
        Paragraph(
            segments=[
                TextSegment(text="1. <strong>Πλοία Στόλου (Vessels):</strong> Για κάθε πλοίο καταγράφεται ο "),
                TextSegment(
                    text="μοναδικός διεθνής επταψήφιος αριθμός IMO (International Maritime Organization number)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Μοναδικός παγκόσμιος αριθμός αναγνώρισης πλοίου IMO.",
                ),
                TextSegment(text=", το "),
                TextSegment(text="όνομα του πλοίου", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", το "),
                TextSegment(
                    text="διακριτικό σήμα κλήσης (Call Sign - επίσης μοναδικό)",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Υποψήφιο Κλειδί (Candidate Key): Μοναδικό διεθνές ραδιοτηλεφωνικό σήμα κλήσης.",
                ),
                TextSegment(text=", το "),
                TextSegment(text="έτος ναυπήγησης", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(text="σημαία (χώρα νηολογίου)", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(text="ολική χωρητικότητα σε τόνους (Deadweight Tonnage - DWT)", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και ο "),
                TextSegment(text="τύπος του πλοίου (π.χ. 'Bulk Carrier', 'Crude Oil Tanker')", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=". Κάθε πλοίο "),
                TextSegment(
                    text="έχει υποχρεωτικά έναν και μοναδικό Πλοίαρχο (Master/Captain)",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ 1:1",
                    badge_class="badge-rel",
                    tooltip="Σχέση 1:1 (Πλοίο - Ναυτικός/Πλοίαρχος): Ολική συμμετοχή πλοίου, μερική συμμετοχή ναυτικού.",
                ),
                TextSegment(text=" που έχει τη γενική διοίκηση του σκάφους."),
            ],
            accent_border_color="border-blue-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="2. <strong>Λιμάνια (Ports):</strong> Κάθε λιμάνι ταυτοποιείται μοναδικά από τον "),
                TextSegment(
                    text="πενταψήφιο κωδικό UN/LOCODE (π.χ. GRPIR για Πειραιά, NLRTM για Ρότερνταμ)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Διεθνής κωδικοποίηση λιμένων των Ηνωμένων Εθνών.",
                ),
                TextSegment(text=", την "),
                TextSegment(
                    text="επίσημη ονομασία του",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Υποψήφιο Κλειδί (Candidate Key): Μοναδική γεωγραφική ονομασία λιμένα.",
                ),
                TextSegment(text=", τη "),
                TextSegment(text="χώρα", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και το "),
                TextSegment(text="μέγιστο επιτρεπόμενο βύθισμα (draft)", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=". Ένα λιμάνι διαθέτει "),
                TextSegment(
                    text="πολλαπλούς τερματικούς σταθμούς/προβλήτες (Terminals)",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΠΛΕΙΟΤΙΜΟ",
                    badge_class="badge-attr-multi",
                    tooltip="Πλειότιμο Γνώρισμα (Multi-valued): Εξάγεται σε ξεχωριστό πίνακα ΤΕΡΜΑΤΙΚΟΣ_ΣΤΑΘΜΟΣ.",
                ),
                TextSegment(text=" που καταγράφονται ως λίστα διαθέσιμων εγκαταστάσεων."),
            ],
            accent_border_color="border-emerald-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="3. <strong>Ταξίδια / Εμπορικά Δρομολόγια (Voyages):</strong> Κάθε πλοίο εκτελεί προγραμματισμένα εμπορικά ταξίδια. Για κάθε ταξίδι τηρείται ένας "),
                TextSegment(
                    text="μοναδικός κωδικός ταξιδιού (Voyage Code)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Μοναδικός κωδικός εμπορικού δρομολογίου.",
                ),
                TextSegment(text=", το "),
                TextSegment(
                    text="πλοίο που το εκτελεί",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ 1:N",
                    badge_class="badge-rel",
                    tooltip="Σχέση 1:N (Πλοίο -> Ταξίδι): Κάθε ταξίδι ανήκει σε 1 πλοίο, το πλοίο εκτελεί πολλά ταξίδια.",
                ),
                TextSegment(text=", το "),
                TextSegment(
                    text="λιμάνι αναχώρησης (Port of Origin)",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ 1:N",
                    badge_class="badge-rel",
                    tooltip="Σχέση 1:N (Λιμάνι -> Ταξίδι): Λιμένας απόπλου.",
                ),
                TextSegment(text=", το "),
                TextSegment(
                    text="λιμάνι τελικού προορισμού (Port of Destination)",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ 1:N",
                    badge_class="badge-rel",
                    tooltip="Σχέση 1:N (Λιμάνι -> Ταξίδι): Λιμένας τελικού κατάπλου.",
                ),
                TextSegment(text=", η "),
                TextSegment(text="προγραμματισμένη ημερομηνία απόπλου (ETD)", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(text="προγραμματισμένη ημερομηνία κατάπλου (ETA)", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(text="πραγματική ημερομηνία άφιξης", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", το "),
                TextSegment(text="είδος του μεταφερόμενου φορτίου", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και το "),
                TextSegment(text="συνολικό βάρος του φορτίου σε μετρικούς τόνους", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text="."),
            ],
            accent_border_color="border-amber-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="4. <strong>Ναυτικοί & Πλήρωμα (Seafarers / Crew):</strong> Για κάθε ναυτικό καταγράφονται: ο "),
                TextSegment(
                    text="μοναδικός αριθμός ναυτικού φυλλαδίου (Discharge Book Number)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Μοναδικός αριθμός ναυτικού επαγγελματικού μητρώου.",
                ),
                TextSegment(text=", ο "),
                TextSegment(
                    text="Αριθμός Διαβατηρίου",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Υποψήφιο Κλειδί (Candidate Key): Μοναδικό διεθνές ταξιδιωτικό έγγραφο.",
                ),
                TextSegment(text=", το "),
                TextSegment(text="όνομα", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", το "),
                TextSegment(text="επώνυμο", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(text="ημερομηνία γέννησης", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(text="εθνικότητα", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(
                    text="διεύθυνση μόνιμης κατοικίας (οδός, αριθμός, πόλη, χώρα)",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΣΥΝΘΕΤΟ",
                    badge_class="badge-attr-composite",
                    tooltip="Σύνθετο Γνώρισμα (Composite): Διασπάται σε Οδός, Αριθμός, Πόλη και Χώρα.",
                ),
                TextSegment(text=" και η "),
                TextSegment(text="κύρια ναυτική ειδικότητα (π.χ. Πλοίαρχος, Α' Μηχανικός, Ναύτης)", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=". Κάθε ναυτικός κατέχει "),
                TextSegment(
                    text="μία ή περισσότερες διεθνείς πιστοποιήσεις ικανότητας STCW (π.χ. 'Medical First Aid', 'BRM')",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΠΛΕΙΟΤΙΜΟ",
                    badge_class="badge-attr-multi",
                    tooltip="Πλειότιμο Γνώρισμα (Multi-valued): Εξάγεται σε ξεχωριστό πίνακα ΠΙΣΤΟΠΟΙΗΣΗ_STCW.",
                ),
                TextSegment(text=", οι οποίες καταγράφονται αναλυτικά."),
            ],
            accent_border_color="border-purple-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="5. <strong>Συμβάσεις Ναυτολόγησης (Crew Contracts / Embarkations):</strong> Οι ναυτικοί "),
                TextSegment(
                    text="ναυτολογούνται σε πλοία μέσω επίσημων συμβάσεων ορισμένου χρόνου",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ N:M",
                    badge_class="badge-rel",
                    tooltip="Συσχετιστική Οντότητα / N:M (Ναυτικός <-> Πλοίο): Πολλοί ναυτικοί υπηρετούν σε πολλά πλοία διαδοχικά.",
                ),
                TextSegment(text=". Για κάθε ναυτολόγηση καταγράφεται το πλοίο, ο ναυτικός, η "),
                TextSegment(
                    text="ημερομηνία επιβίβασης/ναυτολόγησης (Sign-on Date)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK COMPONENT",
                    badge_class="badge-key-pk",
                    tooltip="Στοιχείο Πρωτεύοντος Κλειδιού: Επιτρέπει πολλαπλές διαδοχικές ναυτολογήσεις του ίδιου ναυτικού στο ίδιο πλοίο.",
                ),
                TextSegment(text=", η "),
                TextSegment(text="ημερομηνία απόλυσης/αποβίβασης (Sign-off Date)", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", ο "),
                TextSegment(text="βαθμός/θέση καθήκοντος στο συγκεκριμένο ταξίδι", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και οι "),
                TextSegment(text="μηνιαίες καθαρές αποδοχές σε δολάρια ΗΠΑ", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=". Επιπλέον, για λόγους εκπαίδευσης, κάθε δόκιμος ή νεότερος αξιωματικός έχει έναν ορισμένο ανώτερο αξιωματικό ως "),
                TextSegment(
                    text="μέντορα/εκπαιδευτή εν πλω",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΑΝΑΔΡΟΜΙΚΗ 1:N",
                    badge_class="badge-rel",
                    tooltip="Αναδρομική Σχέση 1:N (Ναυτικός-Μέντορας -> Ναυτικός-Εκπαιδευόμενος).",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-cyan-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="6. <strong>Επιθεωρήσεις Ασφαλείας & Πιστοποιητικά (Inspections & Statutory Certificates):</strong> Κάθε πλοίο υποβάλλεται περιοδικά σε επιθεωρήσεις από νηογνώμονες και αρχές ελέγχου λιμένων. Για κάθε επιθεώρηση καταγράφεται ένας "),
                TextSegment(
                    text="αύξων αριθμός επιθεώρησης για το συγκεκριμένο πλοίο",
                    is_highlight=True,
                    category="key",
                    tag_label="PARTIAL KEY",
                    badge_class="badge-key-partial",
                    tooltip="Μερικό Κλειδί (Partial Key / Discriminator): Αριθμεί διαδοχικά τις επιθεωρήσεις του εκάστοτε πλοίου (1, 2, 3...).",
                ),
                TextSegment(text=", η "),
                TextSegment(text="ημερομηνία επιθεώρησης", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", ο "),
                TextSegment(text="οργανισμός επιθεώρησης (π.χ. Lloyd's Register, DNV)", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", το "),
                TextSegment(text="αποτέλεσμα (Επιτυχής, Εκκρεμότητες/Παρατηρήσεις, Απόρριψη)", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και η "),
                TextSegment(text="ημερομηνία λήξης της εκδοθείσας άδειας πλοϊμότητας", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=". Μια επιθεώρηση "),
                TextSegment(
                    text="δεν μπορεί να υπάρξει αυτόνομα χωρίς το αντίστοιχο πλοίο",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΤΑΥΤΟΠΟΙΟΥΣΑ 1:N",
                    badge_class="badge-rel",
                    tooltip="Ταυτοποιούσα Σχέση 1:N (Πλοίο -> Επιθεώρηση): Πλήρης υπαρκτική εξάρτηση της ασθενούς οντότητας.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-rose-500",
        ),
    ]

    # 2. Entities & Attributes
    entities = [
        Entity(
            name="ΠΛΟΙΟ",
            entity_type="Ισχυρή Οντότητα (Strong Entity)",
            is_weak=False,
            justification="Αυτοτελές εμπορικό σκάφος στόλου με μοναδικό διεθνή αριθμό IMO και Call Sign.",
            attributes=[
                Attribute(name="Αριθμός_IMO", attr_type="Απλό, Μονότιμο, Primary Key", is_pk=True),
                Attribute(name="Call_Sign", attr_type="Απλό, Μονότιμο, Candidate Key", is_candidate=True),
                Attribute(name="Όνομα_Πλοίου", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Έτος_Ναυπήγησης", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Σημαία_Νηολογίου", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Χωρητικότητα_DWT", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Τύπος_Πλοίου", attr_type="Απλό, Μονότιμο"),
            ],
        ),
        Entity(
            name="ΛΙΜΑΝΙ",
            entity_type="Ισχυρή Οντότητα (Strong Entity)",
            is_weak=False,
            justification="Διεθνής λιμένας προσέγγισης με μοναδικό κωδικό UN/LOCODE.",
            attributes=[
                Attribute(name="Κωδικός_UN_LOCODE", attr_type="Απλό, Μονότιμο, Primary Key", is_pk=True),
                Attribute(name="Επίσημη_Ονομασία", attr_type="Απλό, Μονότιμο, Candidate Key", is_candidate=True),
                Attribute(name="Χώρα", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Μέγιστο_Βύθισμα", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Τερματικοί_Σταθμοί", attr_type="Πλειότιμο (Multi-valued)", notes="Εξάγεται στον πίνακα ΤΕΡΜΑΤΙΚΟΣ_ΣΤΑΘΜΟΣ"),
            ],
        ),
        Entity(
            name="ΤΑΞΙΔΙ",
            entity_type="Ισχυρή Οντότητα (Strong Entity)",
            is_weak=False,
            justification="Προγραμματισμένο εμπορικό δρομολόγιο με μοναδικό κωδικό Voyage Code.",
            attributes=[
                Attribute(name="Κωδικός_Ταξιδιού", attr_type="Απλό, Μονότιμο, Primary Key", is_pk=True),
                Attribute(name="Προγραμματισμένη_Απόπλους_ETD", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Προγραμματισμένος_Κατάπλους_ETA", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Πραγματική_Άφιξη", attr_type="Απλό, Μονότιμο (Nullable)"),
                Attribute(name="Είδος_Φορτίου", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Βάρος_Φορτίου_Τόνοι", attr_type="Απλό, Μονότιμο"),
            ],
        ),
        Entity(
            name="ΝΑΥΤΙΚΟΣ",
            entity_type="Ισχυρή Οντότητα (Strong Entity)",
            is_weak=False,
            justification="Φυσικό πρόσωπο επαγγελματία ναυτικού με μοναδικό Αριθμό Ναυτικού Φυλλαδίου.",
            attributes=[
                Attribute(name="Αριθμός_Ναυτικού_Φυλλαδίου", attr_type="Απλό, Μονότιμο, Primary Key", is_pk=True),
                Attribute(name="Αριθμός_Διαβατηρίου", attr_type="Απλό, Μονότιμο, Candidate Key", is_candidate=True),
                Attribute(name="Όνομα", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Επώνυμο", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Ημερ_Γέννησης", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Εθνικότητα", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Κύρια_Ειδικότητα", attr_type="Απλό, Μονότιμο"),
                Attribute(
                    name="Διεύθυνση_Κατοικίας",
                    attr_type="Σύνθετο (Composite)",
                    components=["Οδός", "Αριθμός", "Πόλη", "Χώρα"],
                ),
                Attribute(name="Πιστοποιήσεις_STCW", attr_type="Πλειότιμο (Multi-valued)", notes="Εξάγεται στον πίνακα ΠΙΣΤΟΠΟΙΗΣΗ_STCW"),
            ],
        ),
        Entity(
            name="ΣΥΜΒΑΣΗ_ΝΑΥΤΟΛΟΓΗΣΗΣ",
            entity_type="Συσχετιστική Οντότητα (Associative Entity)",
            is_weak=False,
            justification="Σύμβαση εργασίας ναυτικού σε συγκεκριμένο πλοίο με ημερομηνία επιβίβασης και αποδοχές.",
            attributes=[
                Attribute(name="Ημερομηνία_Επιβίβασης", attr_type="Απλό, Στοιχείο PK", is_pk=True),
                Attribute(name="Ημερομηνία_Απόλυσης", attr_type="Απλό, Μονότιμο (Nullable)"),
                Attribute(name="Βαθμός_Θέση_Καθήκοντος", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Μηνιαίες_Αποδοχές_USD", attr_type="Απλό, Μονότιμο"),
            ],
        ),
        Entity(
            name="ΕΠΙΘΕΩΡΗΣΗ_ΑΣΦΑΛΕΙΑΣ",
            entity_type="Ασθενής Οντότητα (Weak Entity)",
            is_weak=True,
            owner_entity="ΠΛΟΙΟ",
            justification="Έλεγχος ασφαλείας πλοϊμότητας. Εξαρτάται υπαρκτικά από το Πλοίο και αριθμείται με αύξοντα αριθμό.",
            attributes=[
                Attribute(name="Αύξων_Αριθμός_Επιθεώρησης", attr_type="Απλό, Μερικό Κλειδί (Partial Key)", is_partial=True),
                Attribute(name="Ημερομηνία_Επιθεώρησης", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Οργανισμός_Επιθεώρησης", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Αποτέλεσμα", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Ημερομηνία_Λήξης_Πιστοποιητικού", attr_type="Απλό, Μονότιμο"),
            ],
        ),
    ]

    # 3. Relationship Attributes
    relationship_attributes = [
        RelationshipAttribute(
            name="Βαθμός_Θέση_Καθήκοντος",
            relationship_name="ΝΑΥΤΟΛΟΓΗΣΗ (N:M)",
            justification="Περιγράφει τον ρόλο του ναυτικού στη συγκεκριμένη σύμβαση ναυτολόγησης.",
        ),
        RelationshipAttribute(
            name="Μηνιαίες_Αποδοχές_USD",
            relationship_name="ΝΑΥΤΟΛΟΓΗΣΗ (N:M)",
            justification="Συμφωνηθείσες καθαρές αποδοχές για τη διάρκεια της σύμβασης.",
        ),
    ]

    # 4. Keys Analysis Table
    keys_analysis = [
        KeyAnalysisRow(
            entity_name="Πλοίο",
            key_count="2",
            key_types="Υποψήφια: {Αριθμός_IMO}, {Call_Sign}",
            final_pk_selection="Αριθμός_IMO",
            justification="Μοναδικός παγκόσμιος 7ψήφιος κωδικός που παραμένει αμετάβλητος καθ' όλη τη διάρκεια ζωής του πλοίου.",
        ),
        KeyAnalysisRow(
            entity_name="Λιμάνι",
            key_count="2",
            key_types="Υποψήφια: {Κωδικός_UN_LOCODE}, {Επίσημη_Ονομασία}",
            final_pk_selection="Κωδικός_UN_LOCODE",
            justification="Διεθνής πρότυπος κωδικός 5 χαρακτήρων.",
        ),
        KeyAnalysisRow(
            entity_name="Ταξίδι",
            key_count="1",
            key_types="Υποψήφιο: {Κωδικός_Ταξιδιού}",
            final_pk_selection="Κωδικός_Ταξιδιού",
            justification="Μοναδικός επιχειρησιακός κωδικός δρομολογίου.",
        ),
        KeyAnalysisRow(
            entity_name="Ναυτικός",
            key_count="2",
            key_types="Υποψήφια: {Αριθμός_Ναυτικού_Φυλλαδίου}, {Αριθμός_Διαβατηρίου}",
            final_pk_selection="Αριθμός_Ναυτικού_Φυλλαδίου",
            justification="Επίσημο ναυτικό έγγραφο ταυτοποίησης μέλους πληρώματος.",
        ),
        KeyAnalysisRow(
            entity_name="Σύμβαση Ναυτολόγησης",
            key_count="1 (Σύνθετο)",
            key_types="Σύνθετο: {Αριθμός_Ναυτικού_Φυλλαδίου, Αριθμός_IMO, Ημερομηνία_Επιβίβασης}",
            final_pk_selection="{Αριθμός_Ναυτικού_Φυλλαδίου, Αριθμός_IMO, Ημερομηνία_Επιβίβασης}",
            justification="Επιτρέπει στον ίδιο ναυτικό να ναυτολογηθεί επανειλημμένα στο ίδιο πλοίο σε διαφορετικές ημερομηνίες.",
        ),
        KeyAnalysisRow(
            entity_name="Επιθεώρηση Ασφαλείας",
            key_count="0 (Ασθενής)",
            key_types="Μερικό Κλειδί: {Αύξων_Αριθμός_Επιθεώρησης}",
            final_pk_selection="Σύνθετο PK: {Πλοίο.Αριθμός_IMO, Αύξων_Αριθμός_Επιθεώρησης}",
            justification="Ασθενής οντότητα με υπαρκτική εξάρτηση από το Πλοίο.",
            is_weak=True,
        ),
    ]

    # 5. Relationships
    relationships = [
        Relationship(
            letter_id="α",
            name="ΔΙΟΙΚΕΙ_ΠΛΟΙΑΡΧΟΣ",
            connected_entities="Πλοίο <-> Ναυτικός (Πλοίαρχος)",
            cardinality="1:1",
            participation="Ολική για Πλοίο, Μερική για Ναυτικό",
            relationship_type="Κανονική Σχέση",
            attributes=[],
            justification="Κάθε πλοίο έχει υποχρεωτικά 1 πλοίαρχο που το διοικεί, κάθε ναυτικός είναι πλοίαρχος σε 1 πλοίο το πολύ.",
        ),
        Relationship(
            letter_id="β",
            name="ΕΚΤΕΛΕΙ_ΤΑΞΙΔΙ",
            connected_entities="Πλοίο <-> Ταξίδι",
            cardinality="1:N",
            participation="Ολική για Ταξίδι, Μερική για Πλοίο",
            relationship_type="Κανονική Σχέση",
            attributes=[],
            justification="Κάθε ταξίδι ανήκει και εκτελείται από 1 πλοίο, το πλοίο πραγματοποιεί πολλά ταξίδια.",
        ),
        Relationship(
            letter_id="γ",
            name="ΑΝΑΧΩΡΗΣΗ_ΑΠΟ",
            connected_entities="Λιμάνι (Αναχώρησης) <-> Ταξίδι",
            cardinality="1:N",
            participation="Ολική για Ταξίδι, Μερική για Λιμάνι",
            relationship_type="Κανονική Σχέση",
            attributes=[],
            justification="Κάθε ταξίδι ξεκινά από 1 συγκεκριμένο λιμάνι προέλευσης.",
        ),
        Relationship(
            letter_id="δ",
            name="ΠΡΟΟΡΙΣΜΟΣ_ΠΡΟΣ",
            connected_entities="Λιμάνι (Προορισμού) <-> Ταξίδι",
            cardinality="1:N",
            participation="Ολική για Ταξίδι, Μερική για Λιμάνι",
            relationship_type="Κανονική Σχέση",
            attributes=[],
            justification="Κάθε ταξίδι καταλήγει σε 1 συγκεκριμένο λιμάνι προορισμού.",
        ),
        Relationship(
            letter_id="ε",
            name="ΝΑΥΤΟΛΟΓΗΣΗ",
            connected_entities="Ναυτικός <-> Πλοίο",
            cardinality="N:M",
            participation="Μερική και για τις δύο πλευρές",
            relationship_type="Συσχετιστική Οντότητα (Junction Table)",
            attributes=["Ημερομηνία_Επιβίβασης", "Ημερομηνία_Απόλυσης", "Βαθμός_Θέση_Καθήκοντος", "Μηνιαίες_Αποδοχές_USD"],
            justification="Πολλοί ναυτικοί ναυτολογούνται σε πολλά πλοία κατά τη διάρκεια της σταδιοδρομίας τους.",
        ),
        Relationship(
            letter_id="στ",
            name="ΕΚΠΑΙΔΕΥΕΙ_ΜΕΝΤΟΡΑΣ",
            connected_entities="Ναυτικός (Μέντορας) <-> Ναυτικός (Εκπαιδευόμενος)",
            cardinality="1:N",
            participation="Μερική για Μέντορα, Μερική για Εκπαιδευόμενο",
            relationship_type="Αναδρομική Σχέση (Recursive)",
            attributes=[],
            justification="Ένας ανώτερος αξιωματικός καθοδηγεί δόκιμους ή νεότερους αξιωματικούς εν πλω.",
        ),
        Relationship(
            letter_id="ζ",
            name="ΥΠΟΒΑΛΛΕΤΑΙ_ΣΕ_ΕΠΙΘΕΩΡΗΣΗ",
            connected_entities="Πλοίο <-> Επιθεώρηση Ασφαλείας",
            cardinality="1:N",
            participation="Ολική για Επιθεώρηση, Μερική για Πλοίο",
            relationship_type="Ταυτοποιούσα Σχέση (Identifying)",
            attributes=[],
            justification="Συνδέει την ασθενή οντότητα Επιθεώρηση Ασφαλείας με το προσδιορίζον Πλοίο.",
        ),
    ]

    # 6. Assumptions
    assumptions = [
        "Διεύθυνση Κατοικίας: Αναλύεται σε Οδός, Αριθμός, Πόλη, Χώρα για την εξασφάλιση της 1ης Κανονικής Μορφής (1NF).",
        "Πλειότιμα Γνωρίσματα: Οι τερματικοί σταθμοί λιμένων και οι πιστοποιήσεις STCW ναυτικών υλοποιούνται ως ξεχωριστοί πίνακες.",
        "Σύμβαση Ναυτολόγησης: Το πρωτεύον κλειδί περιλαμβάνει και την Ημερομηνία Επιβίβασης, επιτρέποντας επαναλαμβανόμενες συμβάσεις του ίδιου ναυτικού στο ίδιο σκάφος.",
        "Επιθεώρηση Ασφαλείας: Ως ασθενής οντότητα, έχει σύνθετο PK {Αριθμός_IMO, Αύξων_Αριθμός_Επιθεώρησης} με κανόνα διαγραφής CASCADE.",
    ]

    # 7. ER Table Nodes for SVG Crow's Foot Diagram
    er_tables = [
        ERTable(
            id="ploio",
            label="ΠΛΟΙΟ",
            x=50,
            y=80,
            attrs=[
                ERTableAttr(name="Αριθμός_IMO", pk=True),
                ERTableAttr(name="Call_Sign"),
                ERTableAttr(name="Όνομα_Πλοίου"),
                ERTableAttr(name="Έτος_Ναυπήγησης"),
                ERTableAttr(name="Σημαία"),
                ERTableAttr(name="Χωρητικότητα_DWT"),
                ERTableAttr(name="Τύπος_Πλοίου"),
                ERTableAttr(name="Πλοίαρχος_Φυλλάδιο", fk=True),
            ],
        ),
        ERTable(
            id="limani",
            label="ΛΙΜΑΝΙ",
            x=50,
            y=450,
            attrs=[
                ERTableAttr(name="Κωδικός_UN_LOCODE", pk=True),
                ERTableAttr(name="Επίσημη_Ονομασία"),
                ERTableAttr(name="Χώρα"),
                ERTableAttr(name="Μέγιστο_Βύθισμα"),
            ],
        ),
        ERTable(
            id="terminal",
            label="ΤΕΡΜΑΤΙΚΟΣ_ΣΤΑΘΜΟΣ",
            x=50,
            y=680,
            attrs=[
                ERTableAttr(name="Κωδικός_UN_LOCODE", pk=True, fk=True),
                ERTableAttr(name="Όνομα_Terminal", pk=True),
            ],
        ),
        ERTable(
            id="taxidi",
            label="ΤΑΞΙΔΙ",
            x=450,
            y=80,
            attrs=[
                ERTableAttr(name="Κωδικός_Ταξιδιού", pk=True),
                ERTableAttr(name="Αριθμός_IMO", fk=True),
                ERTableAttr(name="Λιμάνι_Αναχώρησης", fk=True),
                ERTableAttr(name="Λιμάνι_Προορισμού", fk=True),
                ERTableAttr(name="ETD_Απόπλους"),
                ERTableAttr(name="ETA_Κατάπλους"),
                ERTableAttr(name="Πραγματική_Άφιξη"),
                ERTableAttr(name="Είδος_Φορτίου"),
                ERTableAttr(name="Βάρος_Τόνοι"),
            ],
        ),
        ERTable(
            id="naytikos",
            label="ΝΑΥΤΙΚΟΣ",
            x=850,
            y=50,
            attrs=[
                ERTableAttr(name="Αριθμός_Φυλλαδίου", pk=True),
                ERTableAttr(name="Αριθμός_Διαβατηρίου"),
                ERTableAttr(name="Όνομα"),
                ERTableAttr(name="Επώνυμο"),
                ERTableAttr(name="Ημερ_Γέννησης"),
                ERTableAttr(name="Εθνικότητα"),
                ERTableAttr(name="Κύρια_Ειδικότητα"),
                ERTableAttr(name="Οδός_Κατοικίας"),
                ERTableAttr(name="Αριθμός_Κατοικίας"),
                ERTableAttr(name="Πόλη_Κατοικίας"),
                ERTableAttr(name="Χώρα_Κατοικίας"),
                ERTableAttr(name="Μέντορας_Φυλλάδιο", fk=True),
            ],
        ),
        ERTable(
            id="pistopoiisi_stcw",
            label="ΠΙΣΤΟΠΟΙΗΣΗ_STCW",
            x=850,
            y=480,
            attrs=[
                ERTableAttr(name="Αριθμός_Φυλλαδίου", pk=True, fk=True),
                ERTableAttr(name="Όνομα_Πιστοποίησης", pk=True),
            ],
        ),
        ERTable(
            id="symvasi",
            label="ΣΥΜΒΑΣΗ_ΝΑΥΤΟΛΟΓΗΣΗΣ",
            x=450,
            y=450,
            attrs=[
                ERTableAttr(name="Αριθμός_Φυλλαδίου", pk=True, fk=True),
                ERTableAttr(name="Αριθμός_IMO", pk=True, fk=True),
                ERTableAttr(name="Ημερ_Επιβίβασης", pk=True),
                ERTableAttr(name="Ημερ_Απόλυσης"),
                ERTableAttr(name="Θέση_Καθήκοντος"),
                ERTableAttr(name="Μηνιαίος_Μισθός_USD"),
            ],
        ),
        ERTable(
            id="epitheorisi",
            label="ΕΠΙΘΕΩΡΗΣΗ_ΑΣΦΑΛΕΙΑΣ",
            x=450,
            y=680,
            attrs=[
                ERTableAttr(name="Αριθμός_IMO", pk=True, fk=True),
                ERTableAttr(name="Αύξων_Αριθμός", pk=True),
                ERTableAttr(name="Ημερ_Επιθεώρησης"),
                ERTableAttr(name="Οργανισμός"),
                ERTableAttr(name="Αποτέλεσμα"),
                ERTableAttr(name="Ημερ_Λήξης_Άδειας"),
            ],
        ),
    ]

    # 8. ER Diagram Edges
    er_edges = [
        EREdge(
            path="M 310,120 L 450,120",
            marker_start="start-one-optional",
            marker_end="end-many-mandatory",
            label="Εκτελεί (1:N)",
            lx=380,
            ly=110,
        ),
        EREdge(
            path="M 310,480 L 450,220",
            marker_start="start-one-optional",
            marker_end="end-many-mandatory",
            label="Αναχώρηση (1:N)",
            lx=360,
            ly=340,
        ),
        EREdge(
            path="M 310,540 L 450,260",
            marker_start="start-one-optional",
            marker_end="end-many-mandatory",
            label="Προορισμός (1:N)",
            lx=400,
            ly=400,
        ),
        EREdge(
            path="M 180,600 L 180,680",
            marker_start="start-one-mandatory",
            marker_end="end-many-mandatory",
            label="Terminals (1:N)",
            lx=180,
            ly=640,
        ),
        EREdge(
            path="M 980,440 L 980,480",
            marker_start="start-one-optional",
            marker_end="end-many-mandatory",
            label="STCW (1:N)",
            lx=980,
            ly=460,
        ),
        EREdge(
            path="M 310,240 L 310,500 L 450,500",
            marker_start="start-one-optional",
            marker_end="end-many-mandatory",
            label="Ναυτολόγηση Πλοίου (1:N)",
            lx=360,
            ly=500,
        ),
        EREdge(
            path="M 850,250 L 710,480",
            marker_start="start-one-optional",
            marker_end="end-many-mandatory",
            label="Ναυτολόγηση Ναυτικού (1:N)",
            lx=770,
            ly=370,
        ),
        EREdge(
            path="M 180,320 L 180,720 L 450,720",
            marker_start="start-one-optional",
            marker_end="end-many-mandatory",
            label="Επιθεώρηση (1:N)",
            lx=300,
            ly=720,
        ),
        EREdge(
            path="M 310,80 L 850,80",
            marker_start="start-one-mandatory",
            marker_end="end-one-optional",
            label="Πλοίαρχος (1:1)",
            lx=580,
            ly=70,
        ),
        # Sailor Mentor recursive relationship (1:N)
        EREdge(
            path="M 1110,100 C 1170,40 1170,180 1110,140",
            marker_start="start-one-optional",
            marker_end="end-many-optional",
            label="Μέντορας (1:N)",
            lx=1180,
            ly=110,
        ),
    ]

    # 9. Relational Justifications
    relational_justifications = [
        RelationalJustification(
            title="1. Σχέση 1:1 Πλοιάρχου:",
            color_class="text-blue-400",
            description="Το Πλοίο έχει ολική συμμετοχή στη σχέση διοίκησης. Το Foreign Key Πλοίαρχος_Φυλλάδιο τοποθετείται στον πίνακα ΠΛΟΙΟ.",
        ),
        RelationalJustification(
            title="2. Συσχετιστική Οντότητα ΣΥΜΒΑΣΗ_ΝΑΥΤΟΛΟΓΗΣΗΣ:",
            color_class="text-emerald-400",
            description="Η σχέση N:M υλοποιείται με σύνθετο PK {Αριθμός_Φυλλαδίου, Αριθμός_IMO, Ημερομηνία_Επιβίβασης} που επιτρέπει πολλαπλές ναυτολογήσεις του ίδιου ναυτικού.",
        ),
        RelationalJustification(
            title="3. Πλειότιμα Γνωρίσματα (1NF):",
            color_class="text-amber-400",
            description="Οι τερματικοί σταθμοί λιμένων και οι πιστοποιήσεις STCW ναυτικών διασπώνται στους ανεξάρτητους πίνακες ΤΕΡΜΑΤΙΚΟΣ_ΣΤΑΘΜΟΣ και ΠΙΣΤΟΠΟΙΗΣΗ_STCW.",
        ),
        RelationalJustification(
            title="4. Ασθενής Οντότητα Επιθεωρήσεων:",
            color_class="text-purple-400",
            description="Η ΕΠΙΘΕΩΡΗΣΗ_ΑΣΦΑΛΕΙΑΣ έχει σύνθετο PK {Αριθμός_IMO, Αύξων_Αριθμός} και κανόνα διαγραφής ON DELETE CASCADE.",
        ),
    ]

    # 10. SQL DDL Script
    sql_ddl = """-- SQL DDL Schema: Maritime Fleet Management Database
-- 1. Entity: LIMANI
CREATE TABLE LIMANI (
    un_locode VARCHAR(5) PRIMARY KEY,
    onoma_limaniou VARCHAR(100) NOT NULL UNIQUE,
    chora VARCHAR(50) NOT NULL,
    max_draft DECIMAL(5, 2) NOT NULL
);

-- 2. Multivalued Attribute: TERMATIKOS_STATHMOS
CREATE TABLE TERMATIKOS_STATHMOS (
    un_locode VARCHAR(5) NOT NULL,
    onoma_terminal VARCHAR(100) NOT NULL,
    PRIMARY KEY (un_locode, onoma_terminal),
    FOREIGN KEY (un_locode) REFERENCES LIMANI(un_locode) ON DELETE CASCADE
);

-- 3. Entity: NAYTIKOS
CREATE TABLE NAYTIKOS (
    arithmos_filadiou VARCHAR(20) PRIMARY KEY,
    arithmos_diavatiriou VARCHAR(20) NOT NULL UNIQUE,
    onoma VARCHAR(50) NOT NULL,
    eponymo VARCHAR(50) NOT NULL,
    hmer_gennisis DATE NOT NULL,
    ethnikotita VARCHAR(50) NOT NULL,
    eidikotita VARCHAR(50) NOT NULL,
    odos VARCHAR(100) NOT NULL,
    arithmos VARCHAR(10) NOT NULL,
    poli VARCHAR(50) NOT NULL,
    chora VARCHAR(50) NOT NULL,
    mentor_filadio VARCHAR(20),
    FOREIGN KEY (mentor_filadio) REFERENCES NAYTIKOS(arithmos_filadiou)
);

-- 4. Multivalued Attribute: PISTOPOIISI_STCW
CREATE TABLE PISTOPOIISI_STCW (
    arithmos_filadiou VARCHAR(20) NOT NULL,
    onoma_pistopoiisis VARCHAR(100) NOT NULL,
    PRIMARY KEY (arithmos_filadiou, onoma_pistopoiisis),
    FOREIGN KEY (arithmos_filadiou) REFERENCES NAYTIKOS(arithmos_filadiou) ON DELETE CASCADE
);

-- 5. Entity: PLOIO
CREATE TABLE PLOIO (
    imo_number VARCHAR(10) PRIMARY KEY,
    call_sign VARCHAR(15) NOT NULL UNIQUE,
    onoma_ploiou VARCHAR(100) NOT NULL,
    etos_nafpigisis INT NOT NULL,
    simaia VARCHAR(50) NOT NULL,
    dwt DECIMAL(12, 2) NOT NULL,
    typos_ploiou VARCHAR(50) NOT NULL,
    ploiarchos_filadio VARCHAR(20) NOT NULL UNIQUE,
    FOREIGN KEY (ploiarchos_filadio) REFERENCES NAYTIKOS(arithmos_filadiou)
);

-- 6. Entity: TAXIDI
CREATE TABLE TAXIDI (
    voyage_code VARCHAR(30) PRIMARY KEY,
    imo_number VARCHAR(10) NOT NULL,
    origin_port_code VARCHAR(5) NOT NULL,
    dest_port_code VARCHAR(5) NOT NULL,
    etd TIMESTAMP NOT NULL,
    eta TIMESTAMP NOT NULL,
    actual_arrival TIMESTAMP,
    eidos_fortiou VARCHAR(100) NOT NULL,
    varos_tonoi DECIMAL(12, 2) NOT NULL,
    FOREIGN KEY (imo_number) REFERENCES PLOIO(imo_number),
    FOREIGN KEY (origin_port_code) REFERENCES LIMANI(un_locode),
    FOREIGN KEY (dest_port_code) REFERENCES LIMANI(un_locode)
);

-- 7. Associative Entity / Junction: SYMVASEIS_NAFTOLOGISIS
CREATE TABLE SYMVASEIS_NAFTOLOGISIS (
    arithmos_filadiou VARCHAR(20) NOT NULL,
    imo_number VARCHAR(10) NOT NULL,
    hmer_epivivasis DATE NOT NULL,
    hmer_apolysis DATE,
    thesi_kathikontos VARCHAR(50) NOT NULL,
    misthos_usd DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (arithmos_filadiou, imo_number, hmer_epivivasis),
    FOREIGN KEY (arithmos_filadiou) REFERENCES NAYTIKOS(arithmos_filadiou) ON DELETE CASCADE,
    FOREIGN KEY (imo_number) REFERENCES PLOIO(imo_number) ON DELETE CASCADE
);

-- 8. Weak Entity: EPITHEORISI_ASFALEIAS
CREATE TABLE EPITHEORISI_ASFALEIAS (
    imo_number VARCHAR(10) NOT NULL,
    arithmos_epitheorisis INT NOT NULL,
    hmer_epitheorisis DATE NOT NULL,
    organismos VARCHAR(100) NOT NULL,
    apotelesma VARCHAR(50) NOT NULL CHECK (apotelesma IN ('Επιτυχής', 'Εκκρεμότητες/Παρατηρήσεις', 'Απόρριψη')),
    hmer_lixis_adeias DATE NOT NULL,
    PRIMARY KEY (imo_number, arithmos_epitheorisis),
    FOREIGN KEY (imo_number) REFERENCES PLOIO(imo_number) ON DELETE CASCADE
);"""

    return Scenario(
        id="maritime_shipping",
        title="Σύστημα Διαχείρισης Ναυτιλιακού Στόλου & Πληρωμάτων",
        subtitle="Μοντελοποίηση Πλοίων, Λιμένων, Ταξιδιών, Ναυτικών, Συμβάσεων & Επιθεωρήσεων",
        course_tag="Βάσεις Δεδομένων (Πρόοδος 2025-2026 - Θέμα 2)",
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
