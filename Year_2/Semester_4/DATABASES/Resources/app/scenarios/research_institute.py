"""Research Institute case study scenario module.

Contains the complete parsed and corrected ER analysis for the Research Institute
problem (Course 404), including all entities, full attribute breakdowns,
relationship cardinalities, keys analysis, and Crow's Foot ER diagram layout.
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


def createResearchInstituteScenario() -> Scenario:
    """Constructs and returns the Research Institute database scenario.

    Returns:
        Scenario: Fully populated scenario instance with corrected data.
    """
    # 1. Text Paragraphs with Interactive Segments
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Ένα ερευνητικό ίδρυμα διατηρεί πληροφορίες σχετικά με τους "),
                TextSegment(
                    text="ερευνητές",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Strong Entity): Φυσικό πρόσωπο με αυτόνομη υπόσταση και ΑΔΤ.",
                ),
                TextSegment(text=", τις "),
                TextSegment(
                    text="ερευνητικές μονάδες",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Strong Entity): Αυτοτελές διοικητικό τμήμα με μοναδικό κωδικό.",
                ),
                TextSegment(text=" και τα "),
                TextSegment(
                    text="ερευνητικά έργα",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Strong Entity): Αυτοτελής δραστηριότητα με μοναδικό αριθμό.",
                ),
                TextSegment(text=" που υλοποιεί."),
            ],
            accent_border_color=None,
        ),
        Paragraph(
            segments=[
                TextSegment(text="Κάθε <strong>ερευνητική μονάδα</strong> έχει έναν "),
                TextSegment(
                    text="μοναδικό κωδικό",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Μοναδικός τεχνητός αναγνωριστικός κωδικός.",
                ),
                TextSegment(text=", ένα "),
                TextSegment(
                    text="μοναδικό όνομα",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Υποψήφιο Κλειδί (Candidate Key): Εναλλακτικό μοναδικό αλφαριθμητικό πεδίο.",
                ),
                TextSegment(text=" και έναν συγκεκριμένο ερευνητή που είναι "),
                TextSegment(
                    text="επιστημονικά υπεύθυνος",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ 1:1",
                    badge_class="badge-rel",
                    tooltip="Σχέση 1:1 μεταξύ Ερευνητή & Μονάδας (Ολική συμμετοχή μονάδας, μερική ερευνητή).",
                ),
                TextSegment(text=" για αυτήν. Για κάθε υπεύθυνο καταγράφεται η "),
                TextSegment(
                    text="ημερομηνία ανάληψης καθηκόντων",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ ΣΧΕΣΗΣ",
                    badge_class="badge-attr-simple",
                    tooltip="Γνώρισμα Σχέσης: Περιγράφει πότε ανέλαβε καθήκοντα ο υπεύθυνος στη συγκεκριμένη μονάδα.",
                ),
                TextSegment(text=". Οι ερευνητικές μονάδες διαθέτουν "),
                TextSegment(
                    text="εγκαταστάσεις σε διάφορες γεωγραφικές περιοχές",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΠΛΕΙΟΤΙΜΟ",
                    badge_class="badge-attr-multi",
                    tooltip="Πλειότιμο Γνώρισμα (Multi-valued): Μία μονάδα μπορεί να έχει πολλαπλές εγκαταστάσεις.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-blue-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Κάθε ερευνητική μονάδα "),
                TextSegment(
                    text="υλοποιεί",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ 1:N",
                    badge_class="badge-rel",
                    tooltip="Σχέση 1:N μεταξύ Μονάδας & Έργων (Μία μονάδα υλοποιεί πολλά έργα, κάθε έργο ανήκει σε 1 μονάδα).",
                ),
                TextSegment(text=" πολλά ερευνητικά έργα. Κάθε έργο έχει έναν "),
                TextSegment(
                    text="μοναδικό αριθμό",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Μοναδικό αναγνωριστικό αριθμητικό πεδίο έργου.",
                ),
                TextSegment(text=", μια "),
                TextSegment(
                    text="μοναδική ονομασία",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Υποψήφιο Κλειδί (Candidate Key): Εναλλακτικό μοναδικό όνομα έργου.",
                ),
                TextSegment(text=" και πραγματοποιείται σε "),
                TextSegment(
                    text="συγκεκριμένο χώρο",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ",
                    badge_class="badge-attr-simple",
                    tooltip="Απλό Μονότιμο Γνώρισμα: Περιγράφει τον χώρο υλοποίησης του έργου.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-amber-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Για κάθε ερευνητή καταγράφονται τα εξής στοιχεία: "),
                TextSegment(text="όνομα", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="επώνυμο", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(
                    text="αριθμός ταυτότητας (ΑΔΤ)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Μοναδικό φυσικό/κρατικό αναγνωριστικό ερευνητή.",
                ),
                TextSegment(text=", "),
                TextSegment(text="επιστημονικό πεδίο", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(
                    text="διεύθυνση κατοικίας",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΣΥΝΘΕΤΟ",
                    badge_class="badge-attr-composite",
                    tooltip="Σύνθετο Γνώρισμα (Composite): Διασπάται σε Οδός, Αριθμός, ΤΚ, Πόλη.",
                ),
                TextSegment(text=", "),
                TextSegment(text="μηνιαίες αποδοχές", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="φύλο", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και "),
                TextSegment(text="ημερομηνία γέννησης", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=". Κάθε ερευνητής "),
                TextSegment(
                    text="ανήκει",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ 1:N",
                    badge_class="badge-rel",
                    tooltip="Σχέση 1:N (Μονάδα -> Ερευνητής): Κάθε ερευνητής ανήκει σε 1 μονάδα, η μονάδα απασχολεί πολλούς.",
                ),
                TextSegment(text=" σε μία συγκεκριμένη ερευνητική μονάδα, αλλά μπορεί να "),
                TextSegment(
                    text="συμμετέχει",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ N:M",
                    badge_class="badge-rel",
                    tooltip="Σχέση N:M μεταξύ Ερευνητή & Έργου: Πολλοί ερευνητές εργάζονται σε πολλά έργα.",
                ),
                TextSegment(text=" στην υλοποίηση πολλών ερευνητικών έργων. Για κάθε συμμετοχή καταγράφεται ο "),
                TextSegment(
                    text="αριθμός ωρών απασχόλησης ανά εβδομάδα",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ ΣΧΕΣΗΣ",
                    badge_class="badge-attr-simple",
                    tooltip="Γνώρισμα Σχέσης: Εξαρτάται ταυτόχρονα από τον συγκεκριμένο ερευνητή και το έργο.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-emerald-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Για κάθε ερευνητή καταγράφονται επίσης τα "),
                TextSegment(
                    text="εξαρτώμενα μέλη",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΑΣΘΕΝΗΣ ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-weak",
                    tooltip="Ασθενής Οντότητα (Weak Entity): Εξαρτάται υπαρκτικά από τον Ερευνητή και δεν έχει αυτόνομο PK.",
                ),
                TextSegment(text=" της οικογένειάς του. Τα στοιχεία που διατηρούνται είναι: "),
                TextSegment(
                    text="όνομα",
                    is_highlight=True,
                    category="key",
                    tag_label="PARTIAL KEY",
                    badge_class="badge-key-partial",
                    tooltip="Μερικό Κλειδί (Partial Key / Discriminator): Διακρίνει τα μέλη της ίδιας οικογένειας.",
                ),
                TextSegment(text=", "),
                TextSegment(text="φύλο", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="ημερομηνία γέννησης", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και "),
                TextSegment(text="συγγενική σχέση", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text="."),
            ],
            accent_border_color="border-purple-500",
        ),
    ]

    # 2. Entity Definitions with Justifications & Full Attributes Breakdown
    entities = [
        Entity(
            name="ΕΡΕΥΝΗΤΙΚΗ ΜΟΝΑΔΑ",
            entity_type="Ισχυρή Οντότητα (Strong Entity)",
            is_weak=False,
            justification=(
                "Περιγράφει αυτοτελές διοικητικό/οργανωτικό τμήμα του ιδρύματος. "
                "Είναι ισχυρή διότι διαθέτει δικό της μοναδικό αναγνωριστικό (Κωδικός_Μονάδας) "
                "και δεν εξαρτάται υπαρκτικά από άλλη οντότητα."
            ),
            attributes=[
                Attribute(name="Κωδικός_Μονάδας", attr_type="Απλό, Μονότιμο, Γνώρισμα-Κλειδί (Primary Key)", is_pk=True),
                Attribute(name="Όνομα_Μονάδας", attr_type="Απλό, Μονότιμο, Υποψήφιο Κλειδί (Candidate Key)", is_candidate=True),
                Attribute(
                    name="Εγκαταστάσεις / Γεωγραφικές Περιοχές",
                    attr_type="Πλειότιμο Γνώρισμα (Multi-valued)",
                    notes="Το κείμενο αναφέρει «σε διάφορες γεωγραφικές περιοχές», άρα μία μονάδα έχει πολλαπλές εγκαταστάσεις.",
                ),
            ],
        ),
        Entity(
            name="ΕΡΕΥΝΗΤΙΚΟ ΕΡΓΟ",
            entity_type="Ισχυρή Οντότητα (Strong Entity)",
            is_weak=False,
            justification=(
                "Αυτοτελής οντότητα που περιγράφει ένα ερευνητικό project με δικό της μοναδικό "
                "αναγνωριστικό (Αριθμός_Έργου) και αυτόνομη υπόσταση."
            ),
            attributes=[
                Attribute(name="Αριθμός_Έργου", attr_type="Απλό, Μονότιμο, Γνώρισμα-Κλειδί (Primary Key)", is_pk=True),
                Attribute(name="Ονομασία_Έργου", attr_type="Απλό, Μονότιμο, Υποψήφιο Κλειδί (Candidate Key)", is_candidate=True),
                Attribute(name="Χώρος_Πραγματοποίησης", attr_type="Απλό, Μονότιμο Γνώρισμα", notes="Προσδιορίζει την τοποθεσία/εργαστήριο διεξαγωγής."),
            ],
        ),
        Entity(
            name="ΕΡΕΥΝΗΤΗΣ",
            entity_type="Ισχυρή Οντότητα (Strong Entity)",
            is_weak=False,
            justification=(
                "Φυσικό πρόσωπο που εργάζεται στο ίδρυμα με αυτοτελή υπόσταση και παγκόσμια "
                "μοναδικό κρατικό αναγνωριστικό (ΑΔΤ)."
            ),
            attributes=[
                Attribute(name="ΑΔΤ", attr_type="Απλό, Μονότιμο, Γνώρισμα-Κλειδί (Primary Key)", is_pk=True),
                Attribute(name="Όνομα", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Επώνυμο", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Επιστημονικό Πεδίο", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Μηνιαίες Αποδοχές", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Φύλο", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Ημερομηνία Γέννησης", attr_type="Απλό, Μονότιμο"),
                Attribute(
                    name="Διεύθυνση Κατοικίας",
                    attr_type="Σύνθετο Γνώρισμα (Composite)",
                    components=["Οδός", "Αριθμός", "ΤΚ", "Πόλη"],
                    notes="Αναλύεται στα επιμέρους ατομικά γνωρίσματα κατά τη σχεδίαση.",
                ),
            ],
        ),
        Entity(
            name="ΕΞΑΡΤΩΜΕΝΟ ΜΕΛΟΣ",
            entity_type="Ασθενής Οντότητα (Weak Entity)",
            is_weak=True,
            owner_entity="ΕΡΕΥΝΗΤΗΣ",
            justification=(
                "Ασθενής οντότητα καθώς δεν διαθέτει δικό της πλήρες μοναδικό κλειδί "
                "(το όνομα μόνο του δεν εξασφαλίζει μοναδικότητα πανελλαδικά) και εξαρτάται υπαρκτικά "
                "από τον Ερευνητή (αν διαγραφεί ο ερευνητής, διαγράφονται και τα εξαρτώμενα μέλη)."
            ),
            attributes=[
                Attribute(name="Όνομα_Μέλους", attr_type="Απλό, Μονότιμο, Μερικό Κλειδί / Διακριτικό (Partial Key)", is_partial=True),
                Attribute(name="Φύλο", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Ημερομηνία Γέννησης", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Συγγενική Σχέση", attr_type="Απλό, Μονότιμο"),
            ],
        ),
    ]

    # 3. Relationship Attributes
    relationship_attributes = [
        RelationshipAttribute(
            name="Ημερομηνία_Ανάληψης_Καθηκόντων",
            relationship_name="ΥΠΕΥΘΥΝΟΣ (1:1)",
            justification="Περιγράφει τη χρονική στιγμή που ο συγκεκριμένος ερευνητής ανέλαβε ως υπεύθυνος στη συγκεκριμένη μονάδα.",
        ),
        RelationshipAttribute(
            name="Ώρες_Απασχόλησης_Ανά_Εβδομάδα",
            relationship_name="ΣΥΜΜΕΤΕΧΕΙ (N:M)",
            justification="Εξαρτάται ταυτόχρονα από το ζεύγος (Ερευνητής, Έργο), καθώς ο ίδιος ερευνητής αφιερώνει διαφορετικές ώρες σε κάθε έργο.",
        ),
    ]

    # 4. Keys Analysis Table
    keys_analysis = [
        KeyAnalysisRow(
            entity_name="ΕΡΕΥΝΗΤΙΚΗ ΜΟΝΑΔΑ",
            key_count="2",
            key_types="Υποψήφια: {Κωδικός_Μονάδας}, {Όνομα_Μονάδας}",
            final_pk_selection="Κωδικός_Μονάδας",
            justification="Προτιμάται ο σύντομος, σταθερός αριθμητικός/αλφαριθμητικός τεχνητός κωδικός έναντι του ευμετάβλητου ονόματος.",
            is_weak=False,
        ),
        KeyAnalysisRow(
            entity_name="ΕΡΕΥΝΗΤΙΚΟ ΕΡΓΟ",
            key_count="2",
            key_types="Υποψήφια: {Αριθμός_Έργου}, {Ονομασία_Έργου}",
            final_pk_selection="Αριθμός_Έργου",
            justification="Σύντομο, μοναδικό αναγνωριστικό που δεν μεταβάλλεται κατά τη διάρκεια ζωής του έργου.",
            is_weak=False,
        ),
        KeyAnalysisRow(
            entity_name="ΕΡΕΥΝΗΤΗΣ",
            key_count="1",
            key_types="Υποψήφιο: {ΑΔΤ}",
            final_pk_selection="ΑΔΤ",
            justification="Επίσημο κρατικό μοναδικό αναγνωριστικό φυσικού προσώπου.",
            is_weak=False,
        ),
        KeyAnalysisRow(
            entity_name="ΕΞΑΡΤΩΜΕΝΟ ΜΕΛΟΣ",
            key_count="0 (Ασθενής Οντότητα / Μερικό Κλειδί)",
            key_types="Μερικό Κλειδί: {Όνομα_Μέλους}",
            final_pk_selection="{ΑΔΤ_Ερευνητή, Όνομα_Μέλους}",
            justification="Σύνθετο Πρωτεύον Κλειδί στη σχεσιακή υλοποίηση (συνδυασμός PK ιδιοκτήτη + Partial Key).",
            is_weak=True,
        ),
    ]

    # 5. Relationships & Cardinalities
    relationships = [
        Relationship(
            letter_id="α",
            name="ΥΠΕΥΘΥΝΟΣ",
            connected_entities="Ερευνητής <-> Ερευνητική Μονάδα",
            cardinality="1:1",
            participation="Ολική για Μονάδα, Μερική για Ερευνητή",
            relationship_type="Κανονική Σχέση",
            attributes=["Ημερομηνία_Ανάληψης_Καθηκόντων"],
            justification=(
                "• Μονάδα -> Ερευνητής (1): «έναν συγκεκριμένο ερευνητή που είναι επιστημονικά υπεύθυνος». "
                "• Ερευνητής -> Μονάδα (1): Παραδοχή ότι ένας ερευνητής διευθύνει το πολύ μία μονάδα."
            ),
        ),
        Relationship(
            letter_id="β",
            name="ΥΛΟΠΟΙΕΙ",
            connected_entities="Ερευνητική Μονάδα <-> Ερευνητικό Έργο",
            cardinality="1:N",
            participation="Ολική για το Έργο",
            relationship_type="Κανονική Σχέση",
            attributes=[],
            justification=(
                "• Μονάδα -> Έργο (N): «Κάθε ερευνητική μονάδα υλοποιεί πολλά ερευνητικά έργα». "
                "• Έργο -> Μονάδα (1): Κάθε έργο υπάγεται σε 1 υπεύθυνη μονάδα υλοποίησης."
            ),
        ),
        Relationship(
            letter_id="γ",
            name="ΑΝΗΚΕΙ / ΑΠΑΣΧΟΛΕΙ",
            connected_entities="Ερευνητής <-> Ερευνητική Μονάδα",
            cardinality="1:N",
            participation="Ολική για τον Ερευνητή",
            relationship_type="Κανονική Σχέση",
            attributes=[],
            justification=(
                "• Ερευνητής -> Μονάδα (1): «Κάθε ερευνητής ανήκει σε μία συγκεκριμένη ερευνητική μονάδα». "
                "• Μονάδα -> Ερευνητής (N): Μία μονάδα απασχολεί πολλούς ερευνητές."
            ),
        ),
        Relationship(
            letter_id="δ",
            name="ΣΥΜΜΕΤΕΧΕΙ",
            connected_entities="Ερευνητής <-> Ερευνητικό Έργο",
            cardinality="N:M",
            participation="Μερική και για τις δύο πλευρές",
            relationship_type="Κανονική Σχέση (Junction)",
            attributes=["Ώρες_Απασχόλησης_Ανά_Εβδομάδα"],
            justification=(
                "• Ερευνητής -> Έργο (M): «μπορεί να συμμετέχει στην υλοποίηση πολλών ερευνητικών έργων». "
                "• Έργο -> Ερευνητής (N): Ένα έργο υλοποιείται από ομάδα πολλών ερευνητών."
            ),
        ),
        Relationship(
            letter_id="ε",
            name="ΔΙΑΤΗΡΕΙ / ΕΧΕΙ",
            connected_entities="Ερευνητής <-> Εξαρτώμενο Μέλος",
            cardinality="1:N",
            participation="Ολική για το Εξαρτώμενο Μέλος",
            relationship_type="Ταυτοποιούσα Σχέση (Identifying Relationship)",
            attributes=[],
            justification=(
                "Ένας ερευνητής μπορεί να έχει 0, 1 ή N εξαρτώμενα μέλη. "
                "Κάθε μέλος ανήκει υποχρεωτικά σε 1 συγκεκριμένο ερευνητή-κηδεμόνα."
            ),
        ),
    ]

    # 6. Design Assumptions
    assumptions = [
        "Διεύθυνση Κατοικίας: Υποθέτουμε ότι αναλύεται σε επιμέρους γνωρίσματα (Οδός, Αριθμός, ΤΚ, Πόλη) κατά τη σχεδίαση, άρα θεωρείται σύνθετο γνώρισμα.",
        "Επιστημονικό Πεδίο: Υποθέτουμε ότι κάθε ερευνητής δηλώνει ένα κύριο επιστημονικό πεδίο (μονότιμο).",
        "Επιστημονικά Υπεύθυνος: Υποθέτουμε ότι ένας ερευνητής δεν μπορεί να είναι υπεύθυνος σε περισσότερες από μία μονάδες ταυτόχρονα (λόγος 1:1).",
        "Εγκαταστάσεις Μονάδας: Εξάγονται σε ξεχωριστό πίνακα (ΕΓΚΑΤΑΣΤΑΣΗ_ΜΟΝΑΔΑΣ) για εξασφάλιση 1ης Κανονικής Μορφής (1NF).",
    ]

    # 7. ER Diagram Tables
    er_tables = [
        ERTable(
            id="unit",
            label="ΕΡΕΥΝΗΤΙΚΗ_ΜΟΝΑΔΑ",
            x=50,
            y=150,
            attrs=[
                ERTableAttr(name="Κωδικός_Μονάδας", pk=True),
                ERTableAttr(name="Όνομα_Μονάδας"),
                ERTableAttr(name="Υπεύθυνος_ΑΔΤ", fk=True),
                ERTableAttr(name="Ημερ_Ανάληψης_Υπευθ"),
            ],
        ),
        ERTable(
            id="facility",
            label="ΕΓΚΑΤΑΣΤΑΣΗ_ΜΟΝΑΔΑΣ",
            x=50,
            y=450,
            attrs=[
                ERTableAttr(name="Κωδικός_Μονάδας", pk=True, fk=True),
                ERTableAttr(name="Τοποθεσία_Εγκατάστασης", pk=True),
            ],
        ),
        ERTable(
            id="researcher",
            label="ΕΡΕΥΝΗΤΗΣ",
            x=430,
            y=50,
            attrs=[
                ERTableAttr(name="ΑΔΤ", pk=True),
                ERTableAttr(name="Όνομα"),
                ERTableAttr(name="Επώνυμο"),
                ERTableAttr(name="Επιστημονικό_Πεδίο"),
                ERTableAttr(name="Μηνιαίες_Αποδοχές"),
                ERTableAttr(name="Φύλο"),
                ERTableAttr(name="Ημερ_Γέννησης"),
                ERTableAttr(name="Οδός_Κατοικίας"),
                ERTableAttr(name="Αριθμός_Κατοικίας"),
                ERTableAttr(name="ΤΚ_Κατοικίας"),
                ERTableAttr(name="Πόλη_Κατοικίας"),
                ERTableAttr(name="Κωδ_Μονάδας_Ανήκει", fk=True),
            ],
        ),
        ERTable(
            id="dependent",
            label="ΕΞΑΡΤΩΜΕΝΟ_ΜΕΛΟΣ",
            x=430,
            y=530,
            attrs=[
                ERTableAttr(name="Ερευνητής_ΑΔΤ", pk=True, fk=True),
                ERTableAttr(name="Όνομα_Μέλους", pk=True),
                ERTableAttr(name="Φύλο"),
                ERTableAttr(name="Ημερ_Γέννησης"),
                ERTableAttr(name="Συγγενική_Σχέση"),
            ],
        ),
        ERTable(
            id="project",
            label="ΕΡΕΥΝΗΤΙΚΟ_ΕΡΓΟ",
            x=810,
            y=150,
            attrs=[
                ERTableAttr(name="Αριθμός_Έργου", pk=True),
                ERTableAttr(name="Ονομασία_Έργου"),
                ERTableAttr(name="Χώρος_Πραγματοποίησης"),
                ERTableAttr(name="Κωδ_Μονάδας_Υλοπ", fk=True),
            ],
        ),
        ERTable(
            id="participation",
            label="ΣΥΜΜΕΤΟΧΗ_ΕΡΓΟΥ",
            x=810,
            y=420,
            attrs=[
                ERTableAttr(name="Ερευνητής_ΑΔΤ", pk=True, fk=True),
                ERTableAttr(name="Αριθμός_Έργου", pk=True, fk=True),
                ERTableAttr(name="Ώρες_Απασχόλησης"),
            ],
        ),
    ]

    # 8. ER Diagram Edges
    er_edges = [
        EREdge(
            path="M 180,150 L 180,25 L 940,25 L 940,150",
            marker_start="start-one-mandatory",
            marker_end="end-many-mandatory",
            label="Υλοποιεί (1:N)",
            lx=560,
            ly=25,
        ),
        EREdge(
            path="M 310,200 L 430,200",
            marker_start="start-one-mandatory",
            marker_end="end-one-optional",
            label="Υπεύθυνος (1:1)",
            lx=370,
            ly=190,
        ),
        EREdge(
            path="M 310,270 L 430,270",
            marker_start="start-one-mandatory",
            marker_end="end-many-mandatory",
            label="Ανήκει (1:N)",
            lx=370,
            ly=260,
        ),
        EREdge(
            path="M 180,280 L 180,450",
            marker_start="start-one-mandatory",
            marker_end="end-many-mandatory",
            label="Εγκαταστάσεις (1:N)",
            lx=180,
            ly=365,
        ),
        EREdge(
            path="M 560,506 L 560,530",
            marker_start="start-one-optional",
            marker_end="end-many-mandatory",
            label="Διατηρεί (1:N)",
            lx=560,
            ly=518,
        ),
        EREdge(
            path="M 690,430 L 750,430 L 750,440 L 810,440",
            marker_start="start-one-optional",
            marker_end="end-many-mandatory",
            label="Συμμετέχει (1:N)",
            lx=750,
            ly=415,
        ),
        EREdge(
            path="M 940,280 L 940,420",
            marker_start="start-one-optional",
            marker_end="end-many-mandatory",
            label="Αφορά (1:N)",
            lx=940,
            ly=350,
        ),
    ]

    # 9. Relational Justifications
    relational_justifications = [
        RelationalJustification(
            title="1. Επιλογή Συμβολισμού Crow's Foot:",
            color_class="text-blue-400",
            description=(
                "Απεικονίζει άμεσα τη σχεσιακή δομή (πίνακες). Οι οντότητες εμφανίζονται με τα γνωρίσματά τους "
                "ως στήλες και σαφή διαχωρισμό των Primary Keys (PK) και Foreign Keys (FK)."
            ),
        ),
        RelationalJustification(
            title="2. Επίλυση Σχέσεων N:M (Junction Tables):",
            color_class="text-purple-400",
            description=(
                "Η σχέση ΣΥΜΜΕΤΕΧΕΙ μεταξύ Ερευνητή και Έργου διασπάστηκε στον ενδιάμεσο πίνακα "
                "ΣΥΜΜΕΤΟΧΗ_ΕΡΓΟΥ με σύνθετο Πρωτεύον Κλειδί που αποτελείται από τα δύο Ξένα Κλειδιά, "
                "φιλοξενώντας και το γνώρισμα Ώρες_Απασχόλησης."
            ),
        ),
        RelationalJustification(
            title="3. Πλειότιμα Γνωρίσματα (Multivalued):",
            color_class="text-emerald-400",
            description=(
                "Το πλειότιμο γνώρισμα Εγκαταστάσεις εξήχθη σε ξεχωριστό πίνακα ΕΓΚΑΤΑΣΤΑΣΗ_ΜΟΝΑΔΑΣ, "
                "εξασφαλίζοντας την 1η Κανονική Μορφή (1NF). Συνδέεται με την Ερευνητική Μονάδα με σχέση 1:N."
            ),
        ),
        RelationalJustification(
            title="4. Τοποθέτηση Ξένων Κλειδιών (FKs):",
            color_class="text-rose-400",
            description=(
                "Στις σχέσεις 1:N (όπως Ανήκει και Διατηρεί), το FK τοποθετήθηκε στην πλευρά του 'N'. "
                "Στη σχέση 1:1 (Υπεύθυνος), το FK τοποθετήθηκε στη Μονάδα, μαζί με την Ημερομηνία_Ανάληψης."
            ),
        ),
    ]

    # 10. SQL DDL Schema
    sql_ddl = """-- ==========================================================
-- SQL DDL Schema: Research Institute Database (Chen -> Relational)
-- ==========================================================

-- 1. Table: ΕΡΕΥΝΗΤΙΚΗ_ΜΟΝΑΔΑ
CREATE TABLE EREVNTIKI_MONADA (
    kodikos_monadas INT PRIMARY KEY,
    onoma_monadas VARCHAR(120) NOT NULL UNIQUE,
    ypefthynos_adt VARCHAR(20) NOT NULL UNIQUE,
    hmer_analipsis_ypefth DATE NOT NULL
);

-- 2. Table: ΕΓΚΑΤΑΣΤΑΣΗ_ΜΟΝΑΔΑΣ (Multivalued Attribute Extraction)
CREATE TABLE EGKATASTASI_MONADAS (
    kodikos_monadas INT NOT NULL,
    topothesia_egkatastasis VARCHAR(150) NOT NULL,
    PRIMARY KEY (kodikos_monadas, topothesia_egkatastasis),
    FOREIGN KEY (kodikos_monadas) REFERENCES EREVNTIKI_MONADA(kodikos_monadas) 
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- 3. Table: ΕΡΕΥΝΗΤΗΣ
CREATE TABLE EREVNTIS (
    adt VARCHAR(20) PRIMARY KEY,
    onoma VARCHAR(50) NOT NULL,
    eponymo VARCHAR(50) NOT NULL,
    epistimoniko_pedio VARCHAR(100) NOT NULL,
    miniaies_apodoches DECIMAL(10, 2) NOT NULL,
    fylo CHAR(1) CHECK (fylo IN ('M', 'F', 'O')),
    hmer_gennisis DATE NOT NULL,
    odos_katoikias VARCHAR(80),
    arithmos_katoikias VARCHAR(10),
    tk_katoikias VARCHAR(10),
    poli_katoikias VARCHAR(50),
    kod_monadas_anikei INT NOT NULL,
    FOREIGN KEY (kod_monadas_anikei) REFERENCES EREVNTIKI_MONADA(kodikos_monadas)
        ON UPDATE CASCADE
);

-- Add Circular Foreign Key for Υπεύθυνος 1:1
ALTER TABLE EREVNTIKI_MONADA
    ADD CONSTRAINT fk_monada_ypefthynos
    FOREIGN KEY (ypefthynos_adt) REFERENCES EREVNTIS(adt)
        ON UPDATE CASCADE;

-- 4. Table: ΕΞΑΡΤΩΜΕΝΟ_ΜΕΛΟΣ (Weak Entity)
CREATE TABLE EXARTOMENO_MELOS (
    erevntis_adt VARCHAR(20) NOT NULL,
    onoma_melous VARCHAR(50) NOT NULL,
    fylo CHAR(1) CHECK (fylo IN ('M', 'F', 'O')),
    hmer_gennisis DATE NOT NULL,
    syngeniki_schesi VARCHAR(50) NOT NULL,
    PRIMARY KEY (erevntis_adt, onoma_melous),
    FOREIGN KEY (erevntis_adt) REFERENCES EREVNTIS(adt)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- 5. Table: ΕΡΕΥΝΗΤΙΚΟ_ΕΡΓΟ
CREATE TABLE EREVNTIKO_ERGO (
    arithmos_ergou INT PRIMARY KEY,
    onomasia_ergou VARCHAR(150) NOT NULL UNIQUE,
    choros_pragmatopoiisis VARCHAR(100) NOT NULL,
    kod_monadas_ylop INT NOT NULL,
    FOREIGN KEY (kod_monadas_ylop) REFERENCES EREVNTIKI_MONADA(kodikos_monadas)
        ON UPDATE CASCADE
);

-- 6. Table: ΣΥΜΜΕΤΟΧΗ_ΕΡΓΟΥ (N:M Junction Table)
CREATE TABLE SYMMETOCHI_ERGOU (
    erevntis_adt VARCHAR(20) NOT NULL,
    arithmos_ergou INT NOT NULL,
    ores_apascholisis DECIMAL(5, 2) NOT NULL DEFAULT 0.0,
    PRIMARY KEY (erevntis_adt, arithmos_ergou),
    FOREIGN KEY (erevntis_adt) REFERENCES EREVNTIS(adt)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (arithmos_ergou) REFERENCES EREVNTIKO_ERGO(arithmos_ergou)
        ON DELETE CASCADE ON UPDATE CASCADE
);"""

    return Scenario(
        id="research_institute",
        title="Ερευνητικό Ίδρυμα & Έργα",
        subtitle="Διαδραστικό Canvas Αναγνώρισης Στοιχείων, Μεθοδολογία & Πλήρες Διάγραμμα E-R",
        course_tag="Βάσεις Δεδομένων (Μάθημα 404)",
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
