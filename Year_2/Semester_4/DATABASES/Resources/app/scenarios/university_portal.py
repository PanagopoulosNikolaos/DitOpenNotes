"""University Portal case study scenario module.

Demonstrates modularity with a second complete ER analysis scenario for a
University Management Information System (Courses, Students, Professors, Departments).
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


def createUniversityPortalScenario() -> Scenario:
    """Constructs and returns the University Management database scenario.

    Returns:
        Scenario: Fully populated scenario instance.
    """
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Ένα πανεπιστημιακό ίδρυμα σχεδιάζει πληροφοριακό σύστημα για τη διαχείριση των "),
                TextSegment(
                    text="φοιτητών",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα: Φυσικό πρόσωπο με μοναδικό Αριθμό Μητρώου (ΑΜ).",
                ),
                TextSegment(text=", των "),
                TextSegment(
                    text="καθηγητών",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα: Διδακτικό προσωπικό με μοναδικό ΑΦΜ.",
                ),
                TextSegment(text=", των "),
                TextSegment(
                    text="τμημάτων",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα: Ακαδημαϊκή μονάδα με μοναδικό κωδικό τμήματος.",
                ),
                TextSegment(text=" και των "),
                TextSegment(
                    text="μαθημάτων",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα: Διδακτικό αντικείμενο με μοναδικό κωδικό μαθήματος.",
                ),
                TextSegment(text=" που προσφέρονται."),
            ],
            accent_border_color=None,
        ),
        Paragraph(
            segments=[
                TextSegment(text="Κάθε <strong>τμήμα</strong> προσδιορίζεται από έναν "),
                TextSegment(
                    text="μοναδικό κωδικό τμήματος",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί: Κωδικός Τμήματος.",
                ),
                TextSegment(text=", ένα "),
                TextSegment(
                    text="όνομα τμήματος",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Υποψήφιο Κλειδί: Μοναδική ονομασία ακαδημαϊκού τμήματος.",
                ),
                TextSegment(text=" και έχει έναν καθηγητή ως "),
                TextSegment(
                    text="πρόεδρο τμήματος",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ 1:1",
                    badge_class="badge-rel",
                    tooltip="Σχέση 1:1 (Τμήμα - Καθηγητής): Κάθε τμήμα έχει υποχρεωτικά 1 πρόεδρο (ολική), ένας καθηγητής μπορεί να είναι πρόεδρος σε το πολύ 1 τμήμα (μερική).",
                ),
                TextSegment(text=" με καταγραφή της "),
                TextSegment(
                    text="ημερομηνίας έναρξης θητείας",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ ΣΧΕΣΗΣ",
                    badge_class="badge-attr-simple",
                    tooltip="Γνώρισμα Σχέσης: Ημερομηνία ανάληψης προεδρίας.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-blue-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Κάθε καθηγητής έχει "),
                TextSegment(
                    text="ΑΦΜ",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί: ΑΦΜ καθηγητή.",
                ),
                TextSegment(text=", "),
                TextSegment(text="ονοματεπώνυμο", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="βαθμίδα", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και "),
                TextSegment(
                    text="ανήκει",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ 1:N",
                    badge_class="badge-rel",
                    tooltip="Σχέση 1:N (Τμήμα -> Καθηγητής): Κάθε καθηγητής ανήκει σε 1 τμήμα.",
                ),
                TextSegment(text=" σε ένα συγκεκριμένο τμήμα. Επίσης, ο καθηγητής "),
                TextSegment(
                    text="διδάσκει",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ 1:N",
                    badge_class="badge-rel",
                    tooltip="Σχέση 1:N (Καθηγητής -> Μάθημα): Ένας καθηγητής διδάσκει πολλά μαθήματα.",
                ),
                TextSegment(text=" ένα ή περισσότερα μαθήματα."),
            ],
            accent_border_color="border-emerald-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="Κάθε μάθημα έχει "),
                TextSegment(
                    text="κωδικό μαθήματος",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί: Κωδικός Μαθήματος.",
                ),
                TextSegment(text=", "),
                TextSegment(text="τίτλο", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="ECTS", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και "),
                TextSegment(
                    text="προσφέρεται",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ 1:N",
                    badge_class="badge-rel",
                    tooltip="Σχέση 1:N (Τμήμα -> Μάθημα): Κάθε μάθημα προσφέρεται από 1 τμήμα.",
                ),
                TextSegment(text=" από ένα τμήμα. Οι φοιτητές "),
                TextSegment(
                    text="εγγράφονται",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ N:M",
                    badge_class="badge-rel",
                    tooltip="Σχέση N:M μεταξύ Φοιτητή & Μαθήματος (Πολλοί φοιτητές παρακολουθούν πολλά μαθήματα).",
                ),
                TextSegment(text=" σε μαθήματα και καταγράφεται ο "),
                TextSegment(
                    text="τελικός βαθμός",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ ΣΧΕΣΗΣ",
                    badge_class="badge-attr-simple",
                    tooltip="Γνώρισμα Σχέσης: Βαθμός φοιτητή στο μάθημα.",
                ),
                TextSegment(text=" και το "),
                TextSegment(
                    text="ακαδημαϊκό εξάμηνο",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ ΣΧΕΣΗΣ",
                    badge_class="badge-attr-simple",
                    tooltip="Γνώρισμα Σχέσης: Εξάμηνο παρακολούθησης.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-amber-500",
        ),
    ]

    entities = [
        Entity(
            name="ΤΜΗΜΑ",
            entity_type="Ισχυρή Οντότητα (Strong Entity)",
            is_weak=False,
            justification="Αυτοτελής διοικητική και ακαδημαϊκή μονάδα με πρωτεύον κλειδί τον Κωδικό_Τμήματος.",
            attributes=[
                Attribute(name="Κωδικός_Τμήματος", attr_type="Απλό, Μονότιμο, Primary Key", is_pk=True),
                Attribute(name="Όνομα_Τμήματος", attr_type="Απλό, Μονότιμο, Candidate Key", is_candidate=True),
            ],
        ),
        Entity(
            name="ΚΑΘΗΓΗΤΗΣ",
            entity_type="Ισχυρή Οντότητα (Strong Entity)",
            is_weak=False,
            justification="Φυσικό πρόσωπο διδάσκον με μοναδικό αναγνωριστικό το ΑΦΜ.",
            attributes=[
                Attribute(name="ΑΦΜ", attr_type="Απλό, Μονότιμο, Primary Key", is_pk=True),
                Attribute(name="Ονοματεπώνυμο", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Βαθμίδα", attr_type="Απλό, Μονότιμο"),
            ],
        ),
        Entity(
            name="ΜΑΘΗΜΑ",
            entity_type="Ισχυρή Οντότητα (Strong Entity)",
            is_weak=False,
            justification="Αυτοτελές διδακτικό αντικείμενο με μοναδικό Κωδικό_Μαθήματος.",
            attributes=[
                Attribute(name="Κωδικός_Μαθήματος", attr_type="Απλό, Μονότιμο, Primary Key", is_pk=True),
                Attribute(name="Τίτλος", attr_type="Απλό, Μονότιμο"),
                Attribute(name="ECTS", attr_type="Απλό, Μονότιμο"),
            ],
        ),
        Entity(
            name="ΦΟΙΤΗΤΗΣ",
            entity_type="Ισχυρή Οντότητα (Strong Entity)",
            is_weak=False,
            justification="Φυσικό πρόσωπο εκπαιδευόμενο με μοναδικό Αριθμό Μητρώου (ΑΜ).",
            attributes=[
                Attribute(name="Αριθμός_Μητρώου", attr_type="Απλό, Μονότιμο, Primary Key", is_pk=True),
                Attribute(name="Ονοματεπώνυμο", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Έτος_Εισαγωγής", attr_type="Απλό, Μονότιμο"),
            ],
        ),
    ]

    relationship_attributes = [
        RelationshipAttribute(
            name="Ημερομηνία_Έναρξης_Θητείας",
            relationship_name="ΠΡΟΕΔΡΟΣ (1:1)",
            justification="Περιγράφει πότε ανέλαβε ο καθηγητής την προεδρία του τμήματος.",
        ),
        RelationshipAttribute(
            name="Τελικός_Βαθμός",
            relationship_name="ΕΓΓΡΑΦΗ / ΠΑΡΑΚΟΛΟΥΘΗΣΗ (N:M)",
            justification="Εξαρτάται από τον συγκεκριμένο φοιτητή και το συγκεκριμένο μάθημα.",
        ),
        RelationshipAttribute(
            name="Ακαδημαϊκό_Εξάμηνο",
            relationship_name="ΕΓΓΡΑΦΗ / ΠΑΡΑΚΟΛΟΥΘΗΣΗ (N:M)",
            justification="Προσδιορίζει την περίοδο εξέτασης/παρακολούθησης.",
        ),
    ]

    keys_analysis = [
        KeyAnalysisRow(
            entity_name="ΤΜΗΜΑ",
            key_count="2",
            key_types="Υποψήφια: {Κωδικός_Τμήματος}, {Όνομα_Τμήματος}",
            final_pk_selection="Κωδικός_Τμήματος",
            justification="Σύντομος τεχνητός κωδικός.",
        ),
        KeyAnalysisRow(
            entity_name="ΚΑΘΗΓΗΤΗΣ",
            key_count="1",
            key_types="Υποψήφιο: {ΑΦΜ}",
            final_pk_selection="ΑΦΜ",
            justification="Κρατικό μοναδικό αναγνωριστικό φορολογικού μητρώου.",
        ),
        KeyAnalysisRow(
            entity_name="ΜΑΘΗΜΑ",
            key_count="1",
            key_types="Υποψήφιο: {Κωδικός_Μαθήματος}",
            final_pk_selection="Κωδικός_Μαθήματος",
            justification="Σταθερός κωδικός προγράμματος σπουδών.",
        ),
        KeyAnalysisRow(
            entity_name="ΦΟΙΤΗΤΗΣ",
            key_count="1",
            key_types="Υποψήφιο: {Αριθμός_Μητρώου}",
            final_pk_selection="Αριθμός_Μητρώου",
            justification="Μοναδικός αριθμός μητρώου στο πανεπιστήμιο.",
        ),
    ]

    relationships = [
        Relationship(
            letter_id="α",
            name="ΠΡΟΕΔΡΟΣ",
            connected_entities="Τμήμα <-> Καθηγητής",
            cardinality="1:1",
            participation="Ολική για Τμήμα, Μερική για Καθηγητή",
            relationship_type="Κανονική Σχέση",
            attributes=["Ημερομηνία_Έναρξης_Θητείας"],
            justification="Κάθε τμήμα έχει 1 πρόεδρο, κάθε καθηγητής προεδρεύει σε 1 τμήμα το πολύ.",
        ),
        Relationship(
            letter_id="β",
            name="ΑΝΗΚΕΙ",
            connected_entities="Καθηγητής <-> Τμήμα",
            cardinality="1:N",
            participation="Ολική για Καθηγητή, Μερική για Τμήμα",
            relationship_type="Κανονική Σχέση",
            attributes=[],
            justification="Κάθε καθηγητής ανήκει σε 1 τμήμα, το τμήμα απασχολεί πολλούς καθηγητές.",
        ),
        Relationship(
            letter_id="γ",
            name="ΠΡΟΣΦΕΡΕΙ",
            connected_entities="Τμήμα <-> Μάθημα",
            cardinality="1:N",
            participation="Ολική για Μάθημα, Μερική για Τμήμα",
            relationship_type="Κανονική Σχέση",
            attributes=[],
            justification="Κάθε μάθημα ανήκει στο πρόγραμμα σπουδών 1 τμήματος.",
        ),
        Relationship(
            letter_id="δ",
            name="ΔΙΔΑΣΚΕΙ",
            connected_entities="Καθηγητής <-> Μάθημα",
            cardinality="1:N",
            participation="Μερική για Καθηγητή, Ολική για Μάθημα",
            relationship_type="Κανονική Σχέση",
            attributes=[],
            justification="Ένας καθηγητής διδάσκει πολλά μαθήματα, κάθε μάθημα έχει 1 υπεύθυνο καθηγητή.",
        ),
        Relationship(
            letter_id="ε",
            name="ΕΓΓΡΑΦΗ / ΠΑΡΑΚΟΛΟΥΘΗΣΗ",
            connected_entities="Φοιτητής <-> Μάθημα",
            cardinality="N:M",
            participation="Μερική και για τις δύο πλευρές",
            relationship_type="Κανονική Σχέση (Junction)",
            attributes=["Τελικός_Βαθμός", "Ακαδημαϊκό_Εξάμηνο"],
            justification="Πολλοί φοιτητές εγγράφονται σε πολλά μαθήματα.",
        ),
    ]

    assumptions = [
        "Κάθε μάθημα διδάσκεται από έναν κύριο υπεύθυνο καθηγητή (λόγος 1:N).",
        "Ένας φοιτητής μπορεί να εγγραφεί σε πολλαπλά μαθήματα ανά εξάμηνο (λόγος N:M).",
        "Ο πρόεδρος τμήματος είναι υποχρεωτικά μέλος ΔΕΠ του ίδιου τμήματος.",
    ]

    er_tables = [
        ERTable(
            id="dept",
            label="ΤΜΗΜΑ",
            x=50,
            y=150,
            attrs=[
                ERTableAttr(name="Κωδικός_Τμήματος", pk=True),
                ERTableAttr(name="Όνομα_Τμήματος"),
                ERTableAttr(name="Πρόεδρος_ΑΦΜ", fk=True),
                ERTableAttr(name="Ημερ_Έναρξης_Θητείας"),
            ],
        ),
        ERTable(
            id="prof",
            label="ΚΑΘΗΓΗΤΗΣ",
            x=450,
            y=80,
            attrs=[
                ERTableAttr(name="ΑΦΜ", pk=True),
                ERTableAttr(name="Ονοματεπώνυμο"),
                ERTableAttr(name="Βαθμίδα"),
                ERTableAttr(name="Κωδικός_Τμήματος", fk=True),
            ],
        ),
        ERTable(
            id="course",
            label="ΜΑΘΗΜΑ",
            x=850,
            y=150,
            attrs=[
                ERTableAttr(name="Κωδικός_Μαθήματος", pk=True),
                ERTableAttr(name="Τίτλος"),
                ERTableAttr(name="ECTS"),
                ERTableAttr(name="Κωδικός_Τμήματος", fk=True),
                ERTableAttr(name="Διδάσκων_ΑΦΜ", fk=True),
            ],
        ),
        ERTable(
            id="student",
            label="ΦΟΙΤΗΤΗΣ",
            x=450,
            y=450,
            attrs=[
                ERTableAttr(name="Αριθμός_Μητρώου", pk=True),
                ERTableAttr(name="Ονοματεπώνυμο"),
                ERTableAttr(name="Έτος_Εισαγωγής"),
            ],
        ),
        ERTable(
            id="enrollment",
            label="ΕΓΓΡΑΦΗ_ΜΑΘΗΜΑΤΟΣ",
            x=850,
            y=450,
            attrs=[
                ERTableAttr(name="Αριθμός_Μητρώου", pk=True, fk=True),
                ERTableAttr(name="Κωδικός_Μαθήματος", pk=True, fk=True),
                ERTableAttr(name="Τελικός_Βαθμός"),
                ERTableAttr(name="Ακαδημαϊκό_Εξάμηνο"),
            ],
        ),
    ]

    er_edges = [
        EREdge(
            path="M 310,180 L 450,140",
            marker_start="start-one-mandatory",
            marker_end="end-one-optional",
            label="Πρόεδρος (1:1)",
            lx=380,
            ly=150,
        ),
        EREdge(
            path="M 310,220 L 450,220",
            marker_start="start-one-mandatory",
            marker_end="end-many-mandatory",
            label="Ανήκει (1:N)",
            lx=380,
            ly=230,
        ),
        EREdge(
            path="M 180,290 L 180,380 L 980,380 L 980,290",
            marker_start="start-one-mandatory",
            marker_end="end-many-mandatory",
            label="Προσφέρει (1:N)",
            lx=580,
            ly=380,
        ),
        EREdge(
            path="M 710,150 L 850,190",
            marker_start="start-one-mandatory",
            marker_end="end-many-mandatory",
            label="Διδάσκει (1:N)",
            lx=780,
            ly=160,
        ),
        EREdge(
            path="M 710,480 L 850,480",
            marker_start="start-one-optional",
            marker_end="end-many-mandatory",
            label="Εγγράφεται (1:N)",
            lx=780,
            ly=470,
        ),
        EREdge(
            path="M 980,290 L 980,450",
            marker_start="start-one-optional",
            marker_end="end-many-mandatory",
            label="Αφορά (1:N)",
            lx=980,
            ly=370,
        ),
    ]

    relational_justifications = [
        RelationalJustification(
            title="1. Σχέση Εγγραφής N:M:",
            color_class="text-purple-400",
            description="Η σχέση ΕΓΓΡΑΦΗ διασπάστηκε στον συνδετικό πίνακα ΕΓΓΡΑΦΗ_ΜΑΘΗΜΑΤΟΣ με σύνθετο PK.",
        ),
        RelationalJustification(
            title="2. Σχέση 1:1 Προέδρου:",
            color_class="text-blue-400",
            description="Το foreign key Πρόεδρος_ΑΦΜ τοποθετήθηκε στο ΤΜΗΜΑ μαζί με την ημερομηνία έναρξης θητείας.",
        ),
    ]

    sql_ddl = """-- SQL DDL Schema: University Portal Database
CREATE TABLE TMIMA (
    kodikos_tmimatos INT PRIMARY KEY,
    onoma_tmimatos VARCHAR(100) NOT NULL UNIQUE,
    proedros_afm VARCHAR(15) NOT NULL UNIQUE,
    hmer_enarxis_thiteias DATE NOT NULL
);

CREATE TABLE KATHIGITIS (
    afm VARCHAR(15) PRIMARY KEY,
    onomateponymo VARCHAR(100) NOT NULL,
    vathmida VARCHAR(50) NOT NULL,
    kodikos_tmimatos INT NOT NULL,
    FOREIGN KEY (kodikos_tmimatos) REFERENCES TMIMA(kodikos_tmimatos)
);

ALTER TABLE TMIMA ADD CONSTRAINT fk_tmima_proedros
    FOREIGN KEY (proedros_afm) REFERENCES KATHIGITIS(afm);

CREATE TABLE MATHIMA (
    kodikos_mathimatos VARCHAR(20) PRIMARY KEY,
    titlos VARCHAR(150) NOT NULL,
    ects INT NOT NULL,
    kodikos_tmimatos INT NOT NULL,
    didaskon_afm VARCHAR(15) NOT NULL,
    FOREIGN KEY (kodikos_tmimatos) REFERENCES TMIMA(kodikos_tmimatos),
    FOREIGN KEY (didaskon_afm) REFERENCES KATHIGITIS(afm)
);

CREATE TABLE FOITITIS (
    arithmos_mitroou VARCHAR(20) PRIMARY KEY,
    onomateponymo VARCHAR(100) NOT NULL,
    etos_eisagogis INT NOT NULL
);

CREATE TABLE EGGRAFI_MATHIMATOS (
    arithmos_mitroou VARCHAR(20) NOT NULL,
    kodikos_mathimatos VARCHAR(20) NOT NULL,
    telikos_vathmos DECIMAL(4, 2),
    akadimaiko_examino VARCHAR(20) NOT NULL,
    PRIMARY KEY (arithmos_mitroou, kodikos_mathimatos),
    FOREIGN KEY (arithmos_mitroou) REFERENCES FOITITIS(arithmos_mitroou) ON DELETE CASCADE,
    FOREIGN KEY (kodikos_mathimatos) REFERENCES MATHIMA(kodikos_mathimatos) ON DELETE CASCADE
);"""

    return Scenario(
        id="university_portal",
        title="Πανεπιστημιακό Σύστημα Διαχείρισης",
        subtitle="Μοντελοποίηση Τμημάτων, Καθηγητών, Μαθημάτων & Εγγραφών Φοιτητών",
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
