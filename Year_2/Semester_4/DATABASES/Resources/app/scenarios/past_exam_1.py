"""Past Exam Paper 1 (Educational Institution) case study scenario module.

Contains the complete parsed and modeled ER analysis for the Educational Institution
(Schools, Facilities, Educational Programs, Professors, Dependents, and Program Assignments),
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


def createPastExam1Scenario() -> Scenario:
    """Constructs and returns the Past Exam 1 database scenario.

    Returns:
        Scenario: Fully populated scenario instance.
    """
    # 1. Text Paragraphs with Interactive Segments
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Ένα εκπαιδευτικό ίδρυμα διατηρεί πληροφορίες σχετικά με τους "),
                TextSegment(
                    text="καθηγητές",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Strong Entity): Φυσικό πρόσωπο διδακτικού προσωπικού με μοναδικό ΑΔΤ.",
                ),
                TextSegment(text=", τις "),
                TextSegment(
                    text="σχολές",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Strong Entity): Αυτοτελής ακαδημαϊκή μονάδα με μοναδικό κωδικό σχολής.",
                ),
                TextSegment(text=" και τα "),
                TextSegment(
                    text="εκπαιδευτικά προγράμματα",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Strong Entity): Αυτοτελές πρόγραμμα σπουδών με μοναδικό αριθμό προγράμματος.",
                ),
                TextSegment(text=" που προσφέρει."),
            ],
            accent_border_color=None,
        ),
        Paragraph(
            segments=[
                TextSegment(text="Κάθε <strong>σχολή</strong> έχει έναν "),
                TextSegment(
                    text="μοναδικό κωδικό",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Μοναδικός τεχνητός αναγνωριστικός κωδικός σχολής.",
                ),
                TextSegment(text=", ένα "),
                TextSegment(
                    text="μοναδικό όνομα",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Υποψήφιο Κλειδί (Candidate Key): Εναλλακτικό μοναδικό όνομα σχολής.",
                ),
                TextSegment(text=" και έναν συγκεκριμένο καθηγητή που τη "),
                TextSegment(
                    text="διευθύνει",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ 1:1",
                    badge_class="badge-rel",
                    tooltip="Σχέση 1:1 μεταξύ Σχολής & Καθηγητή (Ολική συμμετοχή σχολής, μερική καθηγητή).",
                ),
                TextSegment(text=". Καταγράφεται η "),
                TextSegment(
                    text="ημερομηνία ανάληψης καθηκόντων",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ ΣΧΕΣΗΣ",
                    badge_class="badge-attr-simple",
                    tooltip="Γνώρισμα Συσχέτισης: Ημερομηνία έναρξης θητείας διευθυντή στη σχολή.",
                ),
                TextSegment(text=" του διευθυντή. Οι σχολές διαθέτουν "),
                TextSegment(
                    text="εγκαταστάσεις σε διάφορες γεωγραφικές περιοχές",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΠΛΕΙΟΤΙΜΟ",
                    badge_class="badge-attr-multi",
                    tooltip="Πλειότιμο Γνώρισμα (Multi-valued Attribute) / Ασθενής Οντότητα: Πολλαπλές τοποθεσίες ανά σχολή.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-blue-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Κάθε σχολή "),
                TextSegment(
                    text="προσφέρει",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ 1:N",
                    badge_class="badge-rel",
                    tooltip="Σχέση 1:N μεταξύ Σχολής & Εκπαιδευτικών Προγραμμάτων (Μία σχολή προσφέρει πολλά προγράμματα, κάθε πρόγραμμα ανήκει σε 1 σχολή).",
                ),
                TextSegment(text=" πολλά εκπαιδευτικά προγράμματα. Κάθε <strong>πρόγραμμα</strong> έχει έναν "),
                TextSegment(
                    text="μοναδικό αριθμό",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Μοναδικός αριθμητικός κωδικός προγράμματος.",
                ),
                TextSegment(text=", μια "),
                TextSegment(
                    text="μοναδική ονομασία",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Υποψήφιο Κλειδί (Candidate Key): Εναλλακτικό μοναδικό όνομα προγράμματος.",
                ),
                TextSegment(text=" και πραγματοποιείται σε συγκεκριμένο "),
                TextSegment(
                    text="χώρο",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ",
                    badge_class="badge-attr-simple",
                    tooltip="Απλό Μονότιμο Γνώρισμα: Χώρος διεξαγωγής του προγράμματος.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-amber-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Για κάθε <strong>καθηγητή</strong> καταγράφονται τα εξής στοιχεία: "),
                TextSegment(
                    text="όνομα",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ",
                    badge_class="badge-attr-simple",
                    tooltip="Απλό Μονότιμο Γνώρισμα: Όνομα καθηγητή.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="επώνυμο",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ",
                    badge_class="badge-attr-simple",
                    tooltip="Απλό Μονότιμο Γνώρισμα: Επώνυμο καθηγητή.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="αριθμός ταυτότητας (ΑΔΤ)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Μοναδικός Αριθμός Δελτίου Ταυτότητας.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="ειδικότητα",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ",
                    badge_class="badge-attr-simple",
                    tooltip="Απλό Μονότιμο Γνώρισμα: Επιστημονική ειδικότητα καθηγητή.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="διεύθυνση κατοικίας",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΣΥΝΘΕΤΟ",
                    badge_class="badge-attr-composite",
                    tooltip="Σύνθετο Γνώρισμα (Composite Attribute): Διασπάται σε Οδός, Αριθμός, ΤΚ, Πόλη.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="μηνιαίες αποδοχές",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ",
                    badge_class="badge-attr-simple",
                    tooltip="Απλό Μονότιμο Γνώρισμα: Μηνιαίες αποδοχές καθηγητή.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="φύλο",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ",
                    badge_class="badge-attr-simple",
                    tooltip="Απλό Μονότιμο Γνώρισμα: Φύλο καθηγητή.",
                ),
                TextSegment(text=" και "),
                TextSegment(
                    text="ημερομηνία γέννησης",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ",
                    badge_class="badge-attr-simple",
                    tooltip="Απλό Μονότιμο Γνώρισμα: Ημερομηνία γέννησης καθηγητή.",
                ),
                TextSegment(text=". Κάθε καθηγητής "),
                TextSegment(
                    text="ανήκει",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ N:1",
                    badge_class="badge-rel",
                    tooltip="Σχέση N:1 (Καθηγητής -> Σχολή): Κάθε καθηγητής ανήκει υποχρεωτικά σε 1 σχολή.",
                ),
                TextSegment(text=" σε μία συγκεκριμένη σχολή, αλλά μπορεί να "),
                TextSegment(
                    text="συμμετέχει",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ N:M",
                    badge_class="badge-rel",
                    tooltip="Σχέση N:M (Καθηγητής <-> Εκπαιδευτικό Πρόγραμμα): Συμμετοχή σε πολλαπλά προγράμματα (ακόμα και άλλων σχολών).",
                ),
                TextSegment(text=" στην υλοποίηση πολλών εκπαιδευτικών προγραμμάτων, ακόμα και αν αυτά εποπτεύονται από άλλες σχολές. Καταγράφεται ο "),
                TextSegment(
                    text="αριθμός ωρών απασχόλησης ανά εβδομάδα",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ ΣΧΕΣΗΣ",
                    badge_class="badge-attr-simple",
                    tooltip="Γνώρισμα Συσχέτισης N:M: Ώρες εβδομαδιαίας απασχόλησης καθηγητή στο συγκεκριμένο πρόγραμμα.",
                ),
                TextSegment(text=" του καθηγητή σε κάθε πρόγραμμα."),
            ],
            accent_border_color="border-emerald-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Για κάθε καθηγητή καταγράφονται επίσης τα "),
                TextSegment(
                    text="εξαρτώμενα μέλη",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΑΣΘΕΝΗΣ ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-weak",
                    tooltip="Ασθενής Οντότητα (Weak Entity): Εξαρτώμενο μέλος οικογένειας καθηγητή χωρίς αυτόνομο πρωτεύον κλειδί.",
                ),
                TextSegment(text=" της οικογένειάς του. Τα στοιχεία που διατηρούνται είναι: "),
                TextSegment(
                    text="όνομα",
                    is_highlight=True,
                    category="key",
                    tag_label="ΜΕΡΙΚΟ ΚΛΕΙΔΙ",
                    badge_class="badge-key-partial",
                    tooltip="Μερικό Κλειδί (Partial Key / Discriminator): Όνομα εξαρτώμενου μέλους.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="φύλο",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ",
                    badge_class="badge-attr-simple",
                    tooltip="Απλό Μονότιμο Γνώρισμα: Φύλο εξαρτώμενου μέλους.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="ημερομηνία γέννησης",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ",
                    badge_class="badge-attr-simple",
                    tooltip="Απλό Μονότιμο Γνώρισμα: Ημερομηνία γέννησης εξαρτώμενου μέλους.",
                ),
                TextSegment(text=" και η "),
                TextSegment(
                    text="συγγενική τους σχέση",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ",
                    badge_class="badge-attr-simple",
                    tooltip="Απλό Μονότιμο Γνώρισμα: Συγγενική σχέση (π.χ. σύζυγος, τέκνο).",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-purple-500",
        ),
    ]

    # 2. Entities & Attributes (Ερώτημα Α)
    entities = [
        Entity(
            name="ΣΧΟΛΗ",
            entity_type="Ισχυρή Οντότητα (Strong Entity)",
            is_weak=False,
            justification="Αυτοτελής ακαδημαϊκή μονάδα του ιδρύματος με μοναδικό κωδικό σχολής και αυτόνομη υπόσταση.",
            attributes=[
                Attribute(name="Κωδικός_Σχολής", attr_type="Απλό, Μονότιμο", is_pk=True),
                Attribute(name="Όνομα_Σχολής", attr_type="Απλό, Μονότιμο", is_candidate=True),
                Attribute(name="Εγκαταστάσεις_Σχολής", attr_type="Πλειότιμο (Multivalued)", notes="Πολλαπλές γεωγραφικές περιοχές ανά σχολή"),
                Attribute(name="Διευθυντής_ΑΔΤ", attr_type="Ξένο Κλειδί (FK)", is_fk=True, notes="Δείχνει στον Καθηγητή που διευθύνει τη Σχολή (Σχέση 1:1)"),
                Attribute(name="Ημερ_Ανάληψης_Διεύθυνσης", attr_type="Γνώρισμα Συσχέτισης ΔΙΕΥΘΥΝΕΙ", notes="Καταγράφει την έναρξη θητείας διευθυντή"),
            ],
        ),
        Entity(
            name="ΕΓΚΑΤΑΣΤΑΣΗ_ΣΧΟΛΗΣ",
            entity_type="Ασθενής Οντότητα / Πλειότιμο Γνώρισμα",
            is_weak=True,
            owner_entity="ΣΧΟΛΗ",
            justification="Γεωγραφική περιοχή εγκατάστασης της σχολής. Εξαρτάται υπαρκτικά και αναγνωριστικά από τη Σχολή.",
            attributes=[
                Attribute(name="Κωδικός_Σχολής", attr_type="Ξένο Κλειδί (FK)", is_pk=True, is_fk=True),
                Attribute(name="Γεωγραφική_Περιοχή", attr_type="Μερικό Κλειδί (Partial Key)", is_partial=True, is_pk=True),
            ],
        ),
        Entity(
            name="ΕΚΠΑΙΔΕΥΤΙΚΟ_ΠΡΟΓΡΑΜΜΑ",
            entity_type="Ισχυρή Οντότητα (Strong Entity)",
            is_weak=False,
            justification="Αυτοτελές πρόγραμμα σπουδών που προσφέρεται από μία σχολή με μοναδικό αριθμό προγράμματος.",
            attributes=[
                Attribute(name="Αριθμός_Προγράμματος", attr_type="Απλό, Μονότιμο", is_pk=True),
                Attribute(name="Ονομασία_Προγράμματος", attr_type="Απλό, Μονότιμο", is_candidate=True),
                Attribute(name="Χώρος_Διεξαγωγής", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Κωδικός_Σχολής_Εποπτεύει", attr_type="Ξένο Κλειδί (FK)", is_fk=True, notes="Σχολή που προσφέρει/εποπτεύει το πρόγραμμα (Σχέση 1:N)"),
            ],
        ),
        Entity(
            name="ΚΑΘΗΓΗΤΗΣ",
            entity_type="Ισχυρή Οντότητα (Strong Entity)",
            is_weak=False,
            justification="Φυσικό πρόσωπο διδακτικού προσωπικού με μοναδικό Αριθμό Δελτίου Ταυτότητας (ΑΔΤ).",
            attributes=[
                Attribute(name="ΑΔΤ", attr_type="Απλό, Μονότιμο", is_pk=True),
                Attribute(name="Όνομα", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Επώνυμο", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Ειδικότητα", attr_type="Απλό, Μονότιμο"),
                Attribute(
                    name="Διεύθυνση_Κατοικίας",
                    attr_type="Σύνθετο (Composite)",
                    components=["Οδός", "Αριθμός", "ΤΚ", "Πόλη"],
                ),
                Attribute(name="Μηνιαίες_Αποδοχές", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Φύλο", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Ημερ_Γέννησης", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Κωδικός_Σχολής_Ανήκει", attr_type="Ξένο Κλειδί (FK)", is_fk=True, notes="Σχολή στην οποία ανήκει οργανικά ο καθηγητής (Σχέση N:1)"),
            ],
        ),
        Entity(
            name="ΕΞΑΡΤΩΜΕΝΟ_ΜΕΛΟΣ",
            entity_type="Ασθενής Οντότητα (Weak Entity)",
            is_weak=True,
            owner_entity="ΚΑΘΗΓΗΤΗΣ",
            justification="Μέλος οικογένειας καθηγητή. Εξαρτάται υπαρκτικά από τον Καθηγητή (Owner Entity) και διακρίνεται από το όνομά του.",
            attributes=[
                Attribute(name="Καθηγητής_ΑΔΤ", attr_type="Ξένο Κλειδί (FK)", is_pk=True, is_fk=True),
                Attribute(name="Όνομα_Μέλους", attr_type="Μερικό Κλειδί (Partial Key)", is_partial=True, is_pk=True),
                Attribute(name="Φύλο", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Ημερ_Γέννησης", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Συγγενική_Σχέση", attr_type="Απλό, Μονότιμο"),
            ],
        ),
    ]

    # 3. Relationship Attributes (Γνωρίσματα Σχέσεων)
    relationship_attributes = [
        RelationshipAttribute(
            name="Ημερ_Ανάληψης_Διεύθυνσης",
            relationship_name="ΔΙΕΥΘΥΝΕΙ (ΣΧΟΛΗ - ΚΑΘΗΓΗΤΗΣ)",
            justification="Καταγράφει την ημερομηνία έναρξης της θητείας του διευθυντή στη συγκεκριμένη σχολή.",
        ),
        RelationshipAttribute(
            name="Ώρες_Απασχόλησης_Εβδομαδιαίως",
            relationship_name="ΣΥΜΜΕΤΟΧΗ (ΚΑΘΗΓΗΤΗΣ - ΕΚΠΑΙΔΕΥΤΙΚΟ_ΠΡΟΓΡΑΜΜΑ)",
            justification="Καταγράφει τις εβδομαδιαίες ώρες απασχόλησης του συγκεκριμένου καθηγητή στο εκπαιδευτικό πρόγραμμα.",
        ),
    ]

    # 4. Keys Analysis (Ερώτημα Α)
    keys_analysis = [
        KeyAnalysisRow(
            entity_name="ΣΧΟΛΗ",
            key_count="2",
            key_types="Υποψήφια: {Κωδικός_Σχολής}, {Όνομα_Σχολής}",
            final_pk_selection="Κωδικός_Σχολής",
            justification="Σύντομος τεχνητός κωδικός ακαδημαϊκής μονάδας (αμετάβλητος και συμπαγής).",
            is_weak=False,
        ),
        KeyAnalysisRow(
            entity_name="ΕΓΚΑΤΑΣΤΑΣΗ_ΣΧΟΛΗΣ",
            key_count="1 (Σύνθετο)",
            key_types="Σύνθετο PK: {Κωδικός_Σχολής, Γεωγραφική_Περιοχή}",
            final_pk_selection="Κωδικός_Σχολής + Γεωγραφική_Περιοχή",
            justification="Πλειότιμο γνώρισμα / Ασθενής οντότητα υπαρκτικά εξαρτώμενη από τη Σχολή.",
            is_weak=True,
        ),
        KeyAnalysisRow(
            entity_name="ΕΚΠΑΙΔΕΥΤΙΚΟ_ΠΡΟΓΡΑΜΜΑ",
            key_count="2",
            key_types="Υποψήφια: {Αριθμός_Προγράμματος}, {Ονομασία_Προγράμματος}",
            final_pk_selection="Αριθμός_Προγράμματος",
            justification="Μοναδικός αριθμητικός αναγνωριστικός κωδικός προγράμματος.",
            is_weak=False,
        ),
        KeyAnalysisRow(
            entity_name="ΚΑΘΗΓΗΤΗΣ",
            key_count="1",
            key_types="Υποψήφιο / Πρωτεύον: {ΑΔΤ}",
            final_pk_selection="ΑΔΤ",
            justification="Μοναδικός Αριθμός Δελτίου Ταυτότητας (φυσικό αναγνωριστικό).",
            is_weak=False,
        ),
        KeyAnalysisRow(
            entity_name="ΕΞΑΡΤΩΜΕΝΟ_ΜΕΛΟΣ",
            key_count="1 (Σύνθετο)",
            key_types="Σύνθετο PK: {Καθηγητής_ΑΔΤ, Όνομα_Μέλους}",
            final_pk_selection="Καθηγητής_ΑΔΤ + Όνομα_Μέλους",
            justification="Ασθενής οντότητα με μερικό κλειδί (διακριτικό) το όνομα του μέλους και FK του ιδιοκτήτη καθηγητή.",
            is_weak=True,
        ),
    ]

    # 5. Relationships, Cardinalities & Participation (Ερώτημα Α & Β)
    relationships = [
        Relationship(
            letter_id="α",
            name="ΔΙΕΥΘΥΝΕΙ",
            connected_entities="ΣΧΟΛΗ <-> ΚΑΘΗΓΗΤΗΣ",
            cardinality="1:1",
            participation="Ολική για Σχολή (1,1), Μερική για Καθηγητή (0,1)",
            relationship_type="Κανονική Σχέση (Regular Relationship)",
            justification="Κάθε σχολή διευθύνεται υποχρεωτικά από 1 καθηγητή. Ένας καθηγητής μπορεί να διευθύνει το πολύ 1 σχολή.",
            attributes=["Ημερ_Ανάληψης_Διεύθυνσης"],
        ),
        Relationship(
            letter_id="β",
            name="ΔΙΑΘΕΤΕΙ_ΕΓΚΑΤΑΣΤΑΣΕΙΣ",
            connected_entities="ΣΧΟΛΗ <-> ΕΓΚΑΤΑΣΤΑΣΗ_ΣΧΟΛΗΣ",
            cardinality="1:N",
            participation="Ολική και για τα δύο μέρη",
            relationship_type="Ταυτοποιούσα Σχέση (Identifying Relationship)",
            justification="Κάθε σχολή διαθέτει εγκαταστάσεις σε 1 ή περισσότερες γεωγραφικές περιοχές (πλειότιμο γνώρισμα).",
        ),
        Relationship(
            letter_id="γ",
            name="ΠΡΟΣΦΕΡΕΙ",
            connected_entities="ΣΧΟΛΗ <-> ΕΚΠΑΙΔΕΥΤΙΚΟ_ΠΡΟΓΡΑΜΜΑ",
            cardinality="1:N",
            participation="Ολική για Πρόγραμμα (1,1), Μερική για Σχολή (0,N)",
            relationship_type="Κανονική Σχέση (Regular Relationship)",
            justification="Κάθε εκπαιδευτικό πρόγραμμα προσφέρεται/εποπτεύεται από 1 σχολή. Μία σχολή προσφέρει πολλά προγράμματα.",
        ),
        Relationship(
            letter_id="δ",
            name="ΑΝΗΚΕΙ",
            connected_entities="ΚΑΘΗΓΗΤΗΣ <-> ΣΧΟΛΗ",
            cardinality="N:1",
            participation="Ολική για Καθηγητή (1,1), Μερική για Σχολή (0,N)",
            relationship_type="Κανονική Σχέση (Regular Relationship)",
            justification="Κάθε καθηγητής ανήκει οργανικά σε 1 συγκεκριμένη σχολή. Μία σχολή απασχολεί πολλούς καθηγητές.",
        ),
        Relationship(
            letter_id="ε",
            name="ΣΥΜΜΕΤΟΧΗ",
            connected_entities="ΚΑΘΗΓΗΤΗΣ <-> ΕΚΠΑΙΔΕΥΤΙΚΟ_ΠΡΟΓΡΑΜΜΑ",
            cardinality="N:M",
            participation="Μερική και για τα δύο μέρη (0,M - 0,N)",
            relationship_type="Κανονική Σχέση (Regular Relationship)",
            justification="Ένας καθηγητής μπορεί να διδάσκει σε πολλά προγράμματα (ακόμα και άλλων σχολών). Σε ένα πρόγραμμα συμμετέχουν πολλοί καθηγητές.",
            attributes=["Ώρες_Απασχόλησης_Εβδομαδιαίως"],
        ),
        Relationship(
            letter_id="στ",
            name="ΕΧΕΙ_ΕΞΑΡΤΩΜΕΝΟ",
            connected_entities="ΚΑΘΗΓΗΤΗΣ <-> ΕΞΑΡΤΩΜΕΝΟ_ΜΕΛΟΣ",
            cardinality="1:N",
            participation="Ολική για Εξαρτώμενο (1,1), Μερική για Καθηγητή (0,N)",
            relationship_type="Ταυτοποιούσα Σχέση (Identifying Relationship)",
            justification="Κάθε εξαρτώμενο μέλος συνδέεται υπαρκτικά με 1 καθηγητή (ασθενής οντότητα).",
        ),
    ]

    # 6. Crow's Foot ER Diagram Tables (Nodes)
    er_tables = [
        ERTable(
            id="sxoli",
            label="ΣΧΟΛΗ",
            x=60,
            y=60,
            attrs=[
                ERTableAttr(name="Κωδικός_Σχολής", pk=True),
                ERTableAttr(name="Όνομα_Σχολής"),
                ERTableAttr(name="Διευθυντής_ΑΔΤ", fk=True),
                ERTableAttr(name="Ημερ_Ανάληψης_Διεύθυνσης"),
            ],
        ),
        ERTable(
            id="egkatastasi",
            label="ΕΓΚΑΤΑΣΤΑΣΗ_ΣΧΟΛΗΣ",
            x=60,
            y=360,
            attrs=[
                ERTableAttr(name="Κωδικός_Σχολής", pk=True, fk=True),
                ERTableAttr(name="Γεωγραφική_Περιοχή", pk=True),
            ],
        ),
        ERTable(
            id="progmma",
            label="ΕΚΠΑΙΔΕΥΤΙΚΟ_ΠΡΟΓΡΑΜΜΑ",
            x=470,
            y=60,
            attrs=[
                ERTableAttr(name="Αριθμός_Προγράμματος", pk=True),
                ERTableAttr(name="Ονομασία_Προγράμματος"),
                ERTableAttr(name="Χώρος_Διεξαγωγής"),
                ERTableAttr(name="Κωδικός_Σχολής_Εποπτεύει", fk=True),
            ],
        ),
        ERTable(
            id="kathigitis",
            label="ΚΑΘΗΓΗΤΗΣ",
            x=470,
            y=340,
            attrs=[
                ERTableAttr(name="ΑΔΤ", pk=True),
                ERTableAttr(name="Όνομα"),
                ERTableAttr(name="Επώνυμο"),
                ERTableAttr(name="Ειδικότητα"),
                ERTableAttr(name="Διεύθυνση_Κατοικίας"),
                ERTableAttr(name="Μηνιαίες_Αποδοχές"),
                ERTableAttr(name="Φύλο"),
                ERTableAttr(name="Ημερ_Γέννησης"),
                ERTableAttr(name="Κωδικός_Σχολής_Ανήκει", fk=True),
            ],
        ),
        ERTable(
            id="symmetochi",
            label="ΣΥΜΜΕΤΟΧΗ_ΠΡΟΓΡΑΜΜΑΤΟΣ",
            x=880,
            y=60,
            attrs=[
                ERTableAttr(name="Καθηγητής_ΑΔΤ", pk=True, fk=True),
                ERTableAttr(name="Αριθμός_Προγράμματος", pk=True, fk=True),
                ERTableAttr(name="Ώρες_Απασχόλησης_Εβδομαδιαίως"),
            ],
        ),
        ERTable(
            id="exartomeno",
            label="ΕΞΑΡΤΩΜΕΝΟ_ΜΕΛΟΣ",
            x=880,
            y=340,
            attrs=[
                ERTableAttr(name="Καθηγητής_ΑΔΤ", pk=True, fk=True),
                ERTableAttr(name="Όνομα_Μέλους", pk=True),
                ERTableAttr(name="Φύλο"),
                ERTableAttr(name="Ημερ_Γέννησης"),
                ERTableAttr(name="Συγγενική_Σχέση"),
            ],
        ),
    ]

    # 7. Crow's Foot Diagram Edges
    er_edges = [
        EREdge(
            path="M 190,220 L 190,360",
            marker_start="start-one-mandatory",
            marker_end="end-many-optional",
            label="ΔΙΑΘΕΤΕΙ (1:N)",
            lx=200,
            ly=290,
        ),
        EREdge(
            path="M 320,120 L 470,120",
            marker_start="start-one-mandatory",
            marker_end="end-many-optional",
            label="ΠΡΟΣΦΕΡΕΙ (1:N)",
            lx=395,
            ly=105,
        ),
        EREdge(
            path="M 470,390 L 320,180",
            marker_start="start-one-optional",
            marker_end="end-one-mandatory",
            label="ΔΙΕΥΘΥΝΕΙ (1:1)",
            lx=395,
            ly=275,
        ),
        EREdge(
            path="M 470,430 L 320,140",
            marker_start="start-many-optional",
            marker_end="end-one-mandatory",
            label="ΑΝΗΚΕΙ (N:1)",
            lx=380,
            ly=320,
        ),
        EREdge(
            path="M 730,120 L 880,120",
            marker_start="start-one-mandatory",
            marker_end="end-many-optional",
            label="ΠΡΟΓΡΑΜΜΑ (1:N)",
            lx=805,
            ly=105,
        ),
        EREdge(
            path="M 730,390 L 880,140",
            marker_start="start-one-mandatory",
            marker_end="end-many-optional",
            label="ΣΥΜΜΕΤΟΧΗ (1:N)",
            lx=805,
            ly=255,
        ),
        EREdge(
            path="M 730,450 L 880,450",
            marker_start="start-one-mandatory",
            marker_end="end-many-optional",
            label="ΕΧΕΙ_ΕΞΑΡΤΩΜΕΝΟ (1:N)",
            lx=805,
            ly=435,
        ),
    ]

    # 8. Relational Mapping Decisions & Exam Question C Presentation
    relational_justifications = [
        RelationalJustification(
            title="1. ΣΧΟΛΗ & ΔΙΕΥΘΥΝΤΗΣ (Σχέση 1:1)",
            color_class="text-blue-400",
            description="Η ολική συμμετοχή της Σχολής (1,1) επιβάλλει την ενσωμάτωση του Foreign Key Διευθυντής_ΑΔΤ στον πίνακα ΣΧΟΛΗ μαζί με το γνώρισμα Ημερ_Ανάληψης_Διεύθυνσης.",
        ),
        RelationalJustification(
            title="2. ΕΓΚΑΤΑΣΤΑΣΗ_ΣΧΟΛΗΣ (Πλειότιμο Γνώρισμα)",
            color_class="text-amber-400",
            description="Το πλειότιμο γνώρισμα μετασχηματίζεται σε ανεξάρτητο πίνακα με σύνθετο Primary Key {Κωδικός_Σχολής, Γεωγραφική_Περιοχή} και FK προς τη ΣΧΟΛΗ με ON DELETE CASCADE.",
        ),
        RelationalJustification(
            title="3. ΣΥΜΜΕΤΟΧΗ_ΠΡΟΓΡΑΜΜΑΤΟΣ (Σχέση N:M)",
            color_class="text-rose-400",
            description="Η σχέση N:M Καθηγητή-Προγράμματος υλοποιείται ως συνδετικός πίνακας (Junction Table) με σύνθετο PK {Καθηγητής_ΑΔΤ, Αριθμός_Προγράμματος} και το γνώρισμα Ώρες_Απασχόλησης_Εβδομαδιαίως.",
        ),
        RelationalJustification(
            title="4. ΕΞΑΡΤΩΜΕΝΟ_ΜΕΛΟΣ (Ασθενής Οντότητα)",
            color_class="text-purple-400",
            description="Η ασθενής οντότητα λαμβάνει το PK του κατόχου (Καθηγητής_ΑΔΤ) ως FK και συνθέτει το Primary Key {Καθηγητής_ΑΔΤ, Όνομα_Μέλους} με ON DELETE CASCADE.",
        ),
    ]

    # 9. SQL DDL Script
    sql_ddl = """-- SQL DDL Schema: Educational Institution Database (Past Exam 1)
-- Database Design & Implementation (Course 404 / DIT UoI)

-- 1. Entity Table: ΣΧΟΛΗ
CREATE TABLE SXOLI (
    kodikos_scholis VARCHAR(15) PRIMARY KEY,
    onoma_scholis VARCHAR(100) NOT NULL UNIQUE,
    dieuthyntis_adt VARCHAR(15),
    hmer_analipsis_dieuthynsis DATE
);

-- 2. Multivalued Attribute Table: ΕΓΚΑΤΑΣΤΑΣΗ_ΣΧΟΛΗΣ
CREATE TABLE EGKATASTASI_SCHOLIS (
    kodikos_scholis VARCHAR(15) NOT NULL,
    geografiki_periochi VARCHAR(100) NOT NULL,
    PRIMARY KEY (kodikos_scholis, geografiki_periochi),
    FOREIGN KEY (kodikos_scholis) REFERENCES SXOLI(kodikos_scholis)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- 3. Entity Table: ΕΚΠΑΙΔΕΥΤΙΚΟ_ΠΡΟΓΡΑΜΜΑ
CREATE TABLE EKPAIDEUTIKO_PROGRAMMA (
    arithmos_programmatos INT PRIMARY KEY,
    onomasia_programmatos VARCHAR(150) NOT NULL UNIQUE,
    choros_diezagogis VARCHAR(100),
    kodikos_scholis_epopteuei VARCHAR(15) NOT NULL,
    FOREIGN KEY (kodikos_scholis_epopteuei) REFERENCES SXOLI(kodikos_scholis)
        ON UPDATE CASCADE
);

-- 4. Entity Table: ΚΑΘΗΓΗΤΗΣ
CREATE TABLE KATHIGITIS (
    adt VARCHAR(15) PRIMARY KEY,
    onoma VARCHAR(50) NOT NULL,
    eponymo VARCHAR(50) NOT NULL,
    eidikotita VARCHAR(80),
    odos VARCHAR(100),
    arithmos VARCHAR(10),
    tk VARCHAR(10),
    poli VARCHAR(50),
    miniaies_apodoches DECIMAL(10, 2) CHECK (miniaies_apodoches >= 0),
    fylo CHAR(1) CHECK (fylo IN ('M', 'F', 'O')),
    hmer_gennisis DATE,
    kodikos_scholis_anikei VARCHAR(15) NOT NULL,
    FOREIGN KEY (kodikos_scholis_anikei) REFERENCES SXOLI(kodikos_scholis)
        ON UPDATE CASCADE
);

-- Add Circular Foreign Key for Clinic / School Director
ALTER TABLE SXOLI ADD CONSTRAINT fk_sxoli_dieuthyntis
    FOREIGN KEY (dieuthyntis_adt) REFERENCES KATHIGITIS(adt)
    ON DELETE SET NULL ON UPDATE CASCADE;

-- 5. Relationship Junction Table: ΣΥΜΜΕΤΟΧΗ_ΠΡΟΓΡΑΜΜΑΤΟΣ (N:M)
CREATE TABLE SYMMETOCHI_PROGRAMMATOS (
    kathigitis_adt VARCHAR(15) NOT NULL,
    arithmos_programmatos INT NOT NULL,
    ores_apasscholisis_evdomadiaios INT NOT NULL DEFAULT 1 CHECK (ores_apasscholisis_evdomadiaios > 0),
    PRIMARY KEY (kathigitis_adt, arithmos_programmatos),
    FOREIGN KEY (kathigitis_adt) REFERENCES KATHIGITIS(adt)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (arithmos_programmatos) REFERENCES EKPAIDEUTIKO_PROGRAMMA(arithmos_programmatos)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- 6. Weak Entity Table: ΕΞΑΡΤΩΜΕΝΟ_ΜΕΛΟΣ
CREATE TABLE EXARTOMENO_MELOS (
    kathigitis_adt VARCHAR(15) NOT NULL,
    onoma_melous VARCHAR(50) NOT NULL,
    fylo CHAR(1) CHECK (fylo IN ('M', 'F', 'O')),
    hmer_gennisis DATE,
    syggeniki_schesi VARCHAR(40) NOT NULL,
    PRIMARY KEY (kathigitis_adt, onoma_melous),
    FOREIGN KEY (kathigitis_adt) REFERENCES KATHIGITIS(adt)
        ON DELETE CASCADE ON UPDATE CASCADE
);"""

    return Scenario(
        id="past_exam_1",
        title="Παλαιό Θέμα Εξετάσεων 1 (Εκπαιδευτικό Ίδρυμα)",
        subtitle="Εκπαιδευτικό Ίδρυμα: Σχολές, Καθηγητές, Εκπαιδευτικά Προγράμματα, Εγκαταστάσεις & Εξαρτώμενα Μέλη",
        course_tag="Παλαιά Θέματα (Θέμα 1)",
        paragraphs=paragraphs,
        entities=entities,
        relationship_attributes=relationship_attributes,
        keys_analysis=keys_analysis,
        relationships=relationships,
        assumptions=[
            "Κάθε σχολή έχει έναν και μοναδικό καθηγητή ως διευθυντή με καταγεγραμμένη ημερομηνία ανάληψης καθηκόντων (Σχέση 1:1, ολική για σχολή).",
            "Οι εγκαταστάσεις των σχολών βρίσκονται σε διάφορες περιοχές και μοντελοποιούνται ως πλειότιμο γνώρισμα / ασθενής οντότητα της σχολής.",
            "Κάθε εκπαιδευτικό πρόγραμμα εποπτεύεται υποχρεωτικά από 1 σχολή (Σχέση 1:N).",
            "Κάθε καθηγητής ανήκει οργανικά σε 1 σχολή (Σχέση N:1), αλλά μπορεί να διδάσκει σε προγράμματα άλλων σχολών (Σχέση N:M).",
            "Η διεύθυνση κατοικίας του καθηγητή είναι σύνθετο γνώρισμα (Οδός, Αριθμός, ΤΚ, Πόλη).",
            "Τα εξαρτώμενα μέλη αποτελούν ασθενή οντότητα με μερικό κλειδί (διακριτικό) το όνομα του μέλους και ταυτοποιούσα σχέση με τον καθηγητή.",
        ],
        er_tables=er_tables,
        er_edges=er_edges,
        relational_justifications=relational_justifications,
        sql_ddl=sql_ddl,
    )
