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
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Ένα εκπαιδευτικό ίδρυμα διατηρεί πληροφορίες σχετικά με τις "),
                TextSegment(
                    text="σχολές",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Strong Entity): Αυτοτελής ακαδημαϊκή σχολή.",
                ),
                TextSegment(text=", τα "),
                TextSegment(
                    text="εκπαιδευτικά προγράμματα",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Strong Entity): Πρόγραμμα σπουδών/επιμόρφωσης.",
                ),
                TextSegment(text=", τους "),
                TextSegment(
                    text="καθηγητές",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Strong Entity): Διδακτικό προσωπικό.",
                ),
                TextSegment(text=" και τα "),
                TextSegment(
                    text="εξαρτώμενα μέλη",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΑΣΘΕΝΗΣ ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-weak",
                    tooltip="Ασθενής Οντότητα (Weak Entity): Μέλη οικογένειας εξαρτώμενα από τον καθηγητή.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color=None,
        ),
        Paragraph(
            segments=[
                TextSegment(text="1. <strong>Σχολές & Εγκαταστάσεις:</strong> Κάθε σχολή έχει έναν "),
                TextSegment(text="μοναδικό κωδικό", is_highlight=True, category="key", tag_label="PK", badge_class="badge-key-pk"),
                TextSegment(text=", ένα "),
                TextSegment(text="μοναδικό όνομα", is_highlight=True, category="key", tag_label="CANDIDATE KEY", badge_class="badge-key-candidate"),
                TextSegment(text=" και έναν συγκεκριμένο "),
                TextSegment(text="καθηγητή που τη διευθύνει (1:1)", is_highlight=True, category="rel", tag_label="ΣΧΕΣΗ 1:1", badge_class="badge-rel"),
                TextSegment(text=" με καταγραφή της "),
                TextSegment(text="ημερομηνίας ανάληψης καθηκόντων", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ ΣΧΕΣΗΣ", badge_class="badge-attr-simple"),
                TextSegment(text=". Οι σχολές διαθέτουν "),
                TextSegment(text="εγκαταστάσεις σε διάφορες γεωγραφικές περιοχές", is_highlight=True, category="entity", tag_label="ΠΛΕΙΟΤΙΜΟ / ΑΣΘΕΝΗΣ", badge_class="badge-entity-weak"),
                TextSegment(text="."),
            ],
            accent_border_color=None,
        ),
        Paragraph(
            segments=[
                TextSegment(text="2. <strong>Εκπαιδευτικά Προγράμματα:</strong> Κάθε σχολή προσφέρει πολλά προγράμματα. Κάθε πρόγραμμα έχει "),
                TextSegment(text="μοναδικό αριθμό", is_highlight=True, category="key", tag_label="PK", badge_class="badge-key-pk"),
                TextSegment(text=", "),
                TextSegment(text="μοναδική ονομασία", is_highlight=True, category="key", tag_label="CANDIDATE KEY", badge_class="badge-key-candidate"),
                TextSegment(text=" και πραγματοποιείται σε συγκεκριμένο "),
                TextSegment(text="χώρο", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text="."),
            ],
            accent_border_color=None,
        ),
        Paragraph(
            segments=[
                TextSegment(text="3. <strong>Καθηγητές & Συμμετοχές:</strong> Καταγράφονται "),
                TextSegment(text="όνομα, επώνυμο, ΑΔΤ (PK), ΑΦΜ (Candidate), ειδικότητα, διεύθυνση, αποδοχές, φύλο, ημερομηνία γέννησης", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑΤΑ", badge_class="badge-attr-simple"),
                TextSegment(text=". Κάθε καθηγητής ανήκει σε 1 σχολή, συμμετέχει σε πολλά προγράμματα με "),
                TextSegment(text="ώρες απασχόλησης ανά εβδομάδα", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ ΣΧΕΣΗΣ", badge_class="badge-attr-simple"),
                TextSegment(text=" και έχει "),
                TextSegment(text="εξαρτώμενα μέλη", is_highlight=True, category="entity", tag_label="ΑΣΘΕΝΗΣ ΟΝΤΟΤΗΤΑ", badge_class="badge-entity-weak"),
                TextSegment(text="."),
            ],
            accent_border_color=None,
        ),
    ]

    entities = [
        Entity(
            name="ΣΧΟΛΗ",
            entity_type="Ισχυρή Οντότητα (Strong Entity)",
            is_weak=False,
            justification="Αυτοτελής ακαδημαϊκή μονάδα του ιδρύματος με μοναδικό κωδικό σχολής.",
            attributes=[
                Attribute(name="Κωδικός_Σχολής", attr_type="Απλό, Μονότιμο", is_pk=True),
                Attribute(name="Όνομα_Σχολής", attr_type="Απλό, Μονότιμο", is_candidate=True),
                Attribute(name="Διευθυντής_ΑΔΤ", attr_type="Ξένο Κλειδί (FK)", notes="Δείχνει στον Καθηγητή που διευθύνει τη Σχολή"),
            ],
        ),
        Entity(
            name="ΕΓΚΑΤΑΣΤΑΣΗ_ΣΧΟΛΗΣ",
            entity_type="Ασθενής / Πλειότιμο Γνώρισμα (Weak Entity)",
            is_weak=True,
            justification="Γεωγραφική περιοχή εγκατάστασης της σχολής. Εξαρτάται υπαρκτικά από τη Σχολή.",
            attributes=[
                Attribute(name="Κωδικός_Σχολής", attr_type="Ξένο Κλειδί (FK)", is_pk=True),
                Attribute(name="Γεωγραφική_Περιοχή", attr_type="Μερικό Κλειδί (Partial Key)", is_partial=True, is_pk=True),
            ],
        ),
        Entity(
            name="ΕΚΠΑΙΔΕΥΤΙΚΟ_ΠΡΟΓΡΑΜΜΑ",
            entity_type="Ισχυρή Οντότητα (Strong Entity)",
            is_weak=False,
            justification="Αυτοτελές πρόγραμμα σπουδών με μοναδικό αριθμό προγράμματος.",
            attributes=[
                Attribute(name="Αριθμός_Προγράμματος", attr_type="Απλό, Μονότιμο", is_pk=True),
                Attribute(name="Ονομασία_Προγράμματος", attr_type="Απλό, Μονότιμο", is_candidate=True),
                Attribute(name="Χώρος_Διεξαγωγής", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Κωδικός_Σχολής_Εποπτεύει", attr_type="Ξένο Κλειδί (FK)"),
            ],
        ),
        Entity(
            name="ΚΑΘΗΓΗΤΗΣ",
            entity_type="Ισχυρή Οντότητα (Strong Entity)",
            is_weak=False,
            justification="Φυσικό πρόσωπο διδακτικού προσωπικού με μοναδικό ΑΔΤ.",
            attributes=[
                Attribute(name="ΑΔΤ", attr_type="Απλό, Μονότιμο", is_pk=True),
                Attribute(name="ΑΦΜ", attr_type="Απλό, Μονότιμο", is_candidate=True),
                Attribute(name="Όνομα", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Επώνυμο", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Ειδικότητα", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Διεύθυνση_Κατοικίας", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Μηνιαίες_Αποδοχές", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Φύλο", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Ημερ_Γέννησης", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Κωδικός_Σχολής_Ανήκει", attr_type="Ξένο Κλειδί (FK)"),
            ],
        ),
        Entity(
            name="ΕΞΑΡΤΩΜΕΝΟ_ΜΕΛΟΣ",
            entity_type="Ασθενής Οντότητα (Weak Entity)",
            is_weak=True,
            justification="Μέλος οικογένειας καθηγητή. Εξαρτάται υπαρκτικά από τον Καθηγητή (Owner Entity).",
            attributes=[
                Attribute(name="Καθηγητής_ΑΔΤ", attr_type="Ξένο Κλειδί (FK)", is_pk=True),
                Attribute(name="Όνομα_Μέλους", attr_type="Μερικό Κλειδί (Partial Key)", is_partial=True, is_pk=True),
                Attribute(name="Φύλο", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Ημερ_Γέννησης", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Συγγενική_Σχέση", attr_type="Απλό, Μονότιμο"),
            ],
        ),
    ]

    relationship_attributes = [
        RelationshipAttribute(
            name="Ημερ_Ανάληψης_Διεύθυνσης",
            relationship_name="ΔΙΕΥΘΥΝΕΙ (ΣΧΟΛΗ - ΚΑΘΗΓΗΤΗΣ)",
            justification="Καταγράφει την ημερομηνία έναρξης της θητείας του διευθυντή στη σχολή.",
        ),
        RelationshipAttribute(
            name="Ώρες_Απασχόλησης_Εβδομαδιαίως",
            relationship_name="ΣΥΜΜΕΤΕΧΕΙ (ΚΑΘΗΓΗΤΗΣ - ΕΚΠΑΙΔΕΥΤΙΚΟ_ΠΡΟΓΡΑΜΜΑ)",
            justification="Καταγράφει τις εβδομαδιαίες ώρες διδασκαλίας του καθηγητή στο συγκεκριμένο πρόγραμμα.",
        ),
    ]

    keys_analysis = [
        KeyAnalysisRow(
            entity_name="ΣΧΟΛΗ",
            key_count=2,
            key_types="Υποψήφια: {Κωδικός_Σχολής}, {Όνομα_Σχολής}",
            final_pk_selection="Κωδικός_Σχολής",
            justification="Σύντομος τεχνητός κωδικός ακαδημαϊκής μονάδας.",
            is_weak=False,
        ),
        KeyAnalysisRow(
            entity_name="ΕΓΚΑΤΑΣΤΑΣΗ_ΣΧΟΛΗΣ",
            key_count=1,
            key_types="Σύνθετο PK: {Κωδικός_Σχολής, Γεωγραφική_Περιοχή}",
            final_pk_selection="Κωδικός_Σχολής + Γεωγραφική_Περιοχή",
            justification="Ασθενής οντότητα/Πλειότιμο γνώρισμα εξαρτώμενο από τη σχολή.",
            is_weak=True,
        ),
        KeyAnalysisRow(
            entity_name="ΕΚΠΑΙΔΕΥΤΙΚΟ_ΠΡΟΓΡΑΜΜΑ",
            key_count=2,
            key_types="Υποψήφια: {Αριθμός_Προγράμματος}, {Ονομασία_Προγράμματος}",
            final_pk_selection="Αριθμός_Προγράμματος",
            justification="Μοναδικός αριθμητικός αναγνωριστικός κωδικός προγράμματος.",
            is_weak=False,
        ),
        KeyAnalysisRow(
            entity_name="ΚΑΘΗΓΗΤΗΣ",
            key_count=2,
            key_types="Υποψήφια: {ΑΔΤ}, {ΑΦΜ}",
            final_pk_selection="ΑΔΤ",
            justification="Μοναδικός Αριθμός Δελτίου Ταυτότητας.",
            is_weak=False,
        ),
        KeyAnalysisRow(
            entity_name="ΕΞΑΡΤΩΜΕΝΟ_ΜΕΛΟΣ",
            key_count=1,
            key_types="Σύνθετο PK: {Καθηγητής_ΑΔΤ, Όνομα_Μέλους}",
            final_pk_selection="Καθηγητής_ΑΔΤ + Όνομα_Μέλους",
            justification="Ασθενής οντότητα με μερικό κλειδί το όνομα του μέλους.",
            is_weak=True,
        ),
    ]

    relationships = [
        Relationship(
            letter_id="α",
            name="ΔΙΕΥΘΥΝΕΙ",
            connected_entities="ΣΧΟΛΗ <-> ΚΑΘΗΓΗΤΗΣ",
            cardinality="1:1",
            participation="Ολική για Σχολή, Μερική για Καθηγητή",
            relationship_type="Κανονική Σχέση (Regular Relationship)",
            justification="Κάθε σχολή διευθύνεται από 1 καθηγητή. Ένας καθηγητής μπορεί να διευθύνει το πολύ 1 σχολή.",
            attributes=["Ημερ_Ανάληψης_Διεύθυνσης"],
        ),
        Relationship(
            letter_id="β",
            name="ΔΙΑΘΕΤΕΙ_ΕΓΚΑΤΑΣΤΑΣΗ",
            connected_entities="ΣΧΟΛΗ <-> ΕΓΚΑΤΑΣΤΑΣΗ_ΣΧΟΛΗΣ",
            cardinality="1:N",
            participation="Ολική και για τα δύο μέρη",
            relationship_type="Ταυτοποιούσα Σχέση (Identifying Relationship)",
            justification="Κάθε σχολή διαθέτει εγκαταστάσεις σε 1 ή περισσότερες γεωγραφικές περιοχές.",
        ),
        Relationship(
            letter_id="γ",
            name="ΠΡΟΣΦΕΡΕΙ",
            connected_entities="ΣΧΟΛΗ <-> ΕΚΠΑΙΔΕΥΤΙΚΟ_ΠΡΟΓΡΑΜΜΑ",
            cardinality="1:N",
            participation="Ολική για Πρόγραμμα, Μερική για Σχολή",
            relationship_type="Κανονική Σχέση (Regular Relationship)",
            justification="Κάθε πρόγραμμα προσφέρεται από 1 σχολή. Μια σχολή προσφέρει 0 ή περισσότερα προγράμματα.",
        ),
        Relationship(
            letter_id="δ",
            name="ΑΝΗΚΕΙ",
            connected_entities="ΚΑΘΗΓΗΤΗΣ <-> ΣΧΟΛΗ",
            cardinality="N:1",
            participation="Ολική για Καθηγητή, Μερική για Σχολή",
            relationship_type="Κανονική Σχέση (Regular Relationship)",
            justification="Κάθε καθηγητής ανήκει οργανικά σε 1 συγκεκριμένη σχολή.",
        ),
        Relationship(
            letter_id="ε",
            name="ΣΥΜΜΕΤΕΧΕΙ",
            connected_entities="ΚΑΘΗΓΗΤΗΣ <-> ΕΚΠΑΙΔΕΥΤΙΚΟ_ΠΡΟΓΡΑΜΜΑ",
            cardinality="N:M",
            participation="Μερική και για τα δύο μέρη",
            relationship_type="Κανονική Σχέση (Regular Relationship)",
            justification="Ένας καθηγητής μπορεί να διδάσκει σε πολλά προγράμματα (ακόμα και άλλων σχολών).",
            attributes=["Ώρες_Απασχόλησης_Εβδομαδιαίως"],
        ),
        Relationship(
            letter_id="στ",
            name="ΕΧΕΙ_ΕΞΑΡΤΩΜΕΝΟ",
            connected_entities="ΚΑΘΗΓΗΤΗΣ <-> ΕΞΑΡΤΩΜΕΝΟ_ΜΕΛΟΣ",
            cardinality="1:N",
            participation="Ολική για Εξαρτώμενο, Μερική για Καθηγητή",
            relationship_type="Ταυτοποιούσα Σχέση (Identifying Relationship)",
            justification="Κάθε εξαρτώμενο μέλος συνδέεται υπαρκτικά με 1 καθηγητή.",
        ),
    ]

    er_tables = [
        ERTable(
            id="sxoli",
            label="ΣΧΟΛΗ",
            x=50,
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
            x=50,
            y=340,
            attrs=[
                ERTableAttr(name="Κωδικός_Σχολής", pk=True, fk=True),
                ERTableAttr(name="Γεωγραφική_Περιοχή", pk=True),
            ],
        ),
        ERTable(
            id="progmma",
            label="ΕΚΠΑΙΔΕΥΤΙΚΟ_ΠΡΟΓΡΑΜΜΑ",
            x=450,
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
            x=450,
            y=340,
            attrs=[
                ERTableAttr(name="ΑΔΤ", pk=True),
                ERTableAttr(name="ΑΦΜ"),
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
            id="exartomeno",
            label="ΕΞΑΡΤΩΜΕΝΟ_ΜΕΛΟΣ",
            x=850,
            y=340,
            attrs=[
                ERTableAttr(name="Καθηγητής_ΑΔΤ", pk=True, fk=True),
                ERTableAttr(name="Όνομα_Μέλους", pk=True),
                ERTableAttr(name="Φύλο"),
                ERTableAttr(name="Ημερ_Γέννησης"),
                ERTableAttr(name="Συγγενική_Σχέση"),
            ],
        ),
        ERTable(
            id="symmetochi",
            label="ΣΥΜΜΕΤΟΧΗ_ΠΡΟΓΡΑΜΜΑΤΟΣ",
            x=850,
            y=60,
            attrs=[
                ERTableAttr(name="Καθηγητής_ΑΔΤ", pk=True, fk=True),
                ERTableAttr(name="Αριθμός_Προγράμματος", pk=True, fk=True),
                ERTableAttr(name="Ώρες_Απασχόλησης_Εβδομαδιαίως"),
            ],
        ),
    ]

    er_edges = [
        EREdge(path="M 310,120 L 450,120", marker_start="end-one", marker_end="start-many", label="ΠΡΟΣΦΕΡΕΙ", lx=380, ly=110),
        EREdge(path="M 180,240 L 180,340", marker_start="end-one", marker_end="start-many", label="ΔΙΑΘΕΤΕΙ", lx=190, ly=290),
        EREdge(path="M 310,180 L 450,420", marker_start="start-one", marker_end="end-one", label="ΔΙΕΥΘΥΝΕΙ", lx=380, ly=300),
        EREdge(path="M 310,140 L 450,400", marker_start="end-one", marker_end="start-many", label="ΑΝΗΚΕΙ", lx=370, ly=260),
        EREdge(path="M 710,120 L 850,120", marker_start="end-one", marker_end="start-many", label="ΠΡΟΓΡΑΜΜΑ", lx=780, ly=110),
        EREdge(path="M 710,420 L 850,160", marker_start="end-one", marker_end="start-many", label="ΣΥΜΜΕΤΟΧΗ", lx=780, ly=290),
        EREdge(path="M 710,480 L 850,480", marker_start="end-one", marker_end="start-many", label="ΕΧΕΙ_ΕΞΑΡΤΩΜΕΝΟ", lx=780, ly=470),
    ]

    relational_justifications = [
        RelationalJustification(
            title="1. ΣΧΟΛΗ & ΔΙΕΥΘΥΝΤΗΣ (Σχέση 1:1)",
            description="Η ολική συμμετοχή της Σχολής επιβάλλει την τοποθέτηση του FK Διευθυντής_ΑΔΤ στον πίνακα ΣΧΟΛΗ μαζί με την ημερομηνία ανάληψης.",
            color_class="text-blue-400",
        ),
        RelationalJustification(
            title="2. ΕΓΚΑΤΑΣΤΑΣΗ_ΣΧΟΛΗΣ (Πλειότιμο / Ασθενής)",
            description="Δημιουργείται ξεχωριστός πίνακας με σύνθετο PK {Κωδικός_Σχολής, Γεωγραφική_Περιοχή} και FK προς τη ΣΧΟΛΗ.",
            color_class="text-amber-400",
        ),
        RelationalJustification(
            title="3. ΣΥΜΜΕΤΟΧΗ_ΠΡΟΓΡΑΜΜΑΤΟΣ (Σχέση N:M)",
            description="Η σχέση N:M μεταξύ Καθηγητή και Προγράμματος μετασχηματίζεται σε πίνακα ζεύξης με σύνθετο PK {Καθηγητής_ΑΔΤ, Αριθμός_Προγράμματος} και το γνώρισμα Ώρες_Απασχόλησης.",
            color_class="text-rose-400",
        ),
        RelationalJustification(
            title="4. ΕΞΑΡΤΩΜΕΝΟ_ΜΕΛΟΣ (Ασθενής Οντότητα)",
            description="Ο πίνακας λαμβάνει το PK του κατόχου Καθηγητής_ΑΔΤ ως FK και το συνδυάζει με το μερικό κλειδί Όνομα_Μέλους.",
            color_class="text-purple-400",
        ),
    ]

    sql_ddl = """-- SQL DDL Schema: Educational Institution Database (Past Exam 1)

CREATE TABLE SXOLI (
    kodikos_scholis VARCHAR(15) PRIMARY KEY,
    onoma_scholis VARCHAR(100) NOT NULL UNIQUE,
    dieuthyntis_adt VARCHAR(15),
    hmer_analipsis_dieuthynsis DATE
);

CREATE TABLE EGKATASTASI_SCHOLIS (
    kodikos_scholis VARCHAR(15),
    geografiki_periochi VARCHAR(100),
    PRIMARY KEY (kodikos_scholis, geografiki_periochi),
    FOREIGN KEY (kodikos_scholis) REFERENCES SXOLI(kodikos_scholis) ON DELETE CASCADE
);

CREATE TABLE EKPAIDEUTIKO_PROGRAMMA (
    arithmos_programmatos INT PRIMARY KEY,
    onomasia_programmatos VARCHAR(150) NOT NULL UNIQUE,
    choros_diezagogis VARCHAR(100),
    kodikos_scholis_epopteuei VARCHAR(15) NOT NULL,
    FOREIGN KEY (kodikos_scholis_epopteuei) REFERENCES SXOLI(kodikos_scholis)
);

CREATE TABLE KATHIGITIS (
    adt VARCHAR(15) PRIMARY KEY,
    afm VARCHAR(15) NOT NULL UNIQUE,
    onoma VARCHAR(50) NOT NULL,
    eponymo VARCHAR(50) NOT NULL,
    eidikotita VARCHAR(80),
    dieuthynsi_katoikias VARCHAR(120),
    miniaies_apodoches DECIMAL(10, 2),
    fylo CHAR(1) CHECK (fylo IN ('M', 'F', 'O')),
    hmer_gennisis DATE,
    kodikos_scholis_anikei VARCHAR(15) NOT NULL,
    FOREIGN KEY (kodikos_scholis_anikei) REFERENCES SXOLI(kodikos_scholis)
);

ALTER TABLE SXOLI ADD CONSTRAINT fk_sxoli_dieuthyntis
FOREIGN KEY (dieuthyntis_adt) REFERENCES KATHIGITIS(adt);

CREATE TABLE SYMMETOCHI_PROGRAMMATOS (
    kathigitis_adt VARCHAR(15),
    arithmos_programmatos INT,
    ores_apasscholisis_evdomadiaios INT NOT NULL DEFAULT 1,
    PRIMARY KEY (kathigitis_adt, arithmos_programmatos),
    FOREIGN KEY (kathigitis_adt) REFERENCES KATHIGITIS(adt) ON DELETE CASCADE,
    FOREIGN KEY (arithmos_programmatos) REFERENCES EKPAIDEUTIKO_PROGRAMMA(arithmos_programmatos) ON DELETE CASCADE
);

CREATE TABLE EXARTOMENO_MELOS (
    kathigitis_adt VARCHAR(15),
    onoma_melous VARCHAR(50),
    fylo CHAR(1) CHECK (fylo IN ('M', 'F', 'O')),
    hmer_gennisis DATE,
    syggeniki_schesi VARCHAR(40),
    PRIMARY KEY (kathigitis_adt, onoma_melous),
    FOREIGN KEY (kathigitis_adt) REFERENCES KATHIGITIS(adt) ON DELETE CASCADE
);
"""

    return Scenario(
        id="past_exam_1",
        title="Θέμα Εξετάσεων 1",
        subtitle="Εκπαιδευτικό Ίδρυμα: Σχολές, Καθηγητές, Εκπαιδευτικά Προγράμματα & Εξαρτώμενα Μέλη",
        course_tag="DATABASES (Θέμα 1)",
        paragraphs=paragraphs,
        entities=entities,
        relationship_attributes=relationship_attributes,
        keys_analysis=keys_analysis,
        relationships=relationships,
        assumptions=[
            "Κάθε καθηγητής ανήκει υποχρεωτικά σε 1 σχολή αλλά μπορεί να διδάσκει σε προγράμματα άλλων σχολών.",
            "Η διεύθυνση σχολής ανατίθεται σε 1 καθηγητή με καταγραφή ημερομηνίας ανάληψης.",
            "Τα εξαρτώμενα μέλη αποτελούν ασθενή οντότητα με μερικό κλειδί το όνομα του μέλους.",
        ],
        er_tables=er_tables,
        er_edges=er_edges,
        relational_justifications=relational_justifications,
        sql_ddl=sql_ddl,
    )

