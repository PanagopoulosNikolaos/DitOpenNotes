"""Banking Management and Transactions case study scenario module.

Contains the complete parsed and modeled ER analysis for the Core Banking System
(Branches, Employees, Customers, Bank Accounts, Account Transactions, Loans),
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


def createBankingManagementScenario() -> Scenario:
    """Constructs and returns the Banking Management database scenario.

    Returns:
        Scenario: Fully populated scenario instance.
    """
    # 1. Text Paragraphs with Interactive Segments
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Ένας τραπεζικός όμιλος σχεδιάζει το νέο κεντρικό πληροφοριακό σύστημα διαχείρισης "),
                TextSegment(
                    text="καταστημάτων",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Strong Entity): Αυτοτελές τραπεζικό κατάστημα με μοναδικό Branch Code.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="πελατών",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Strong Entity): Φυσικό πρόσωπο πελάτη με μοναδικό ΑΦΜ.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="τραπεζικών λογαριασμών",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Strong Entity): Τραπεζικός λογαριασμός με διεθνή κωδικό IBAN.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="δανείων",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Strong Entity): Δανειακή σύμβαση με μοναδικό αριθμό δανείου.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="συναλλαγών / κινήσεων",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΑΣΘΕΝΗΣ ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-weak",
                    tooltip="Ασθενής Οντότητα (Weak Entity): Κίνηση λογαριασμού που εξαρτάται υπαρκτικά από τον λογαριασμό.",
                ),
                TextSegment(text=" και "),
                TextSegment(
                    text="τραπεζικού προσωπικού",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Strong Entity): Εργαζόμενος τράπεζας με μοναδικό ΑΜΥ.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color=None,
        ),
        Paragraph(
            segments=[
                TextSegment(text="1. <strong>Τραπεζικά Καταστήματα (Branches):</strong> Κάθε κατάστημα διαθέτει έναν "),
                TextSegment(
                    text="μοναδικό αριθμό καταστήματος (Branch Code)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Μοναδικός κωδικός καταστήματος.",
                ),
                TextSegment(text=", μια "),
                TextSegment(
                    text="μοναδική ονομασία καταστήματος (π.χ. 'Κεντρικό Συντάγματος')",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Υποψήφιο Κλειδί (Candidate Key): Μοναδική επωνυμία καταστήματος.",
                ),
                TextSegment(text=", την "),
                TextSegment(text="πόλη όπου εδρεύει", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", και τον "),
                TextSegment(text="ετήσιο προϋπολογισμό του", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=". Κάθε κατάστημα "),
                TextSegment(
                    text="διευθύνεται υποχρεωτικά από έναν συγκεκριμένο υπάλληλο (Διευθυντής Καταστήματος)",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ 1:1",
                    badge_class="badge-rel-11",
                    tooltip="Συσχέτιση 1:1 (ΔΙΕΥΘΥΝΕΙ): Υποχρεωτική (ολική) συμμετοχή για Κατάστημα, μερική για Υπάλληλο.",
                ),
                TextSegment(text=". Για κάθε διευθυντή καταγράφεται η "),
                TextSegment(
                    text="ημερομηνία ανάληψης της διεύθυνσης",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ ΣΧΕΣΗΣ",
                    badge_class="badge-attr-composite",
                    tooltip="Γνώρισμα Συσχέτισης: Ενσωματώνεται στον πίνακα ΚΑΤΑΣΤΗΜΑ ως Foreign Key attribute.",
                ),
                TextSegment(text=". Ένας υπάλληλος μπορεί να διευθύνει το πολύ ένα κατάστημα."),
            ],
            accent_border_color="border-blue-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="2. <strong>Τραπεζικό Προσωπικό & Ιεραρχία:</strong> Για κάθε υπάλληλο καταγράφονται: ο "),
                TextSegment(
                    text="Αριθμός Μητρώου Υπαλλήλου (ΑΜΥ)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Μοναδικός αριθμός μητρώου προσωπικού.",
                ),
                TextSegment(text=", ο "),
                TextSegment(
                    text="Αριθμός Φορολογικού Μητρώου (ΑΦΜ)",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Υποψήφιο Κλειδί (Candidate Key): Μοναδικό ΑΦΜ υπαλλήλου.",
                ),
                TextSegment(text=", το "),
                TextSegment(text="όνομα", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", το "),
                TextSegment(text="επώνυμο", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", ο "),
                TextSegment(text="μηνιαίος μισθός", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(text="ημερομηνία πρόσληψης", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και η "),
                TextSegment(
                    text="διεύθυνση κατοικίας (οδός, αριθμός, πόλη)",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΣΥΝΘΕΤΟ",
                    badge_class="badge-attr-composite",
                    tooltip="Σύνθετο Γνώρισμα: Αναλύεται σε απλά πεδία odos, arithmos, poli.",
                ),
                TextSegment(text=". Κάθε υπάλληλος "),
                TextSegment(
                    text="ανήκει υποχρεωτικά σε ένα συγκεκριμένο κατάστημα, όπου και εργάζεται",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ 1:N",
                    badge_class="badge-rel-1n",
                    tooltip="Συσχέτιση 1:N (ΕΡΓΑΖΕΤΑΙ_ΣΕ): Ένα κατάστημα απασχολεί πολλούς υπαλλήλους.",
                ),
                TextSegment(text=". Στο πλαίσιο της διοικητικής ιεραρχίας, "),
                TextSegment(
                    text="κάθε υπάλληλος (εκτός του Γενικού Διευθυντή) εποπτεύεται άμεσα από έναν άλλο ανώτερο υπάλληλο (προϊστάμενο)",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΑΝΑΔΡΟΜΙΚΗ 1:N",
                    badge_class="badge-rel-1n",
                    tooltip="Αναδρομική Συσχέτιση 1:N (ΕΠΟΠΤΕΥΕΙ): Σύνδεση της οντότητας ΥΠΑΛΛΗΛΟΣ με τον εαυτό της.",
                ),
                TextSegment(text=", ενώ ένας προϊστάμενος μπορεί να εποπτεύει πολλούς υπαλλήλους."),
            ],
            accent_border_color="border-amber-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="3. <strong>Πελάτες Τράπεζας (Customers):</strong> Για κάθε πελάτη (φυσικό πρόσωπο) καταγράφονται: ο "),
                TextSegment(
                    text="μοναδικός ΑΦΜ",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Μοναδικός Αριθμός Φορολογικού Μητρώου πελάτη.",
                ),
                TextSegment(text=", ο "),
                TextSegment(
                    text="Αριθμός Δελτίου Ταυτότητας (ΑΔΤ)",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Υποψήφιο Κλειδί (Candidate Key): Μοναδικός αριθμός δελτίου ταυτότητας.",
                ),
                TextSegment(text=", το "),
                TextSegment(text="όνομα", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", το "),
                TextSegment(text="επώνυμο", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(text="ημερομηνία γέννησης", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(
                    text="διεύθυνση κατοικίας (σύνθετο γνώρισμα: οδός, αριθμός, ΤΚ, πόλη)",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΣΥΝΘΕΤΟ",
                    badge_class="badge-attr-composite",
                    tooltip="Σύνθετο Γνώρισμα: Αναλύεται σε απλά γνωρίσματα odos, arithmos, tk, poli.",
                ),
                TextSegment(text=" και η "),
                TextSegment(text="πιστοληπτική βαθμολογία (Credit Score)", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=". Ένας πελάτης μπορεί να δηλώσει ένα ή περισσότερα "),
                TextSegment(
                    text="τηλέφωνα επικοινωνίας (σταθερό, κινητό, εργασίας)",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΠΛΕΙΟΤΙΜΟ",
                    badge_class="badge-attr-multi",
                    tooltip="Πλειότιμο Γνώρισμα: Απαιτεί ξεχωριστό πίνακα ΤΗΛΕΦΩΝΟ_ΠΕΛΑΤΗ στο σχεσιακό μοντέλο.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-purple-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="4. <strong>Τραπεζικοί Λογαριασμοί & Συνδικαιούχοι:</strong> Κάθε λογαριασμός ταυτοποιείται από τον "),
                TextSegment(
                    text="διεθνή αριθμό IBAN (μοναδικός)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Μοναδικός κωδικός IBAN λογαριασμού.",
                ),
                TextSegment(text=", το "),
                TextSegment(text="τρέχον υπόλοιπο (Balance)", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", τον "),
                TextSegment(text="τύπο λογαριασμού (π.χ. 'Ταμιευτήριο', 'Τρεχούμενος', 'Μισθοδοσίας')", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και την "),
                TextSegment(text="ημερομηνία ανοίγματος", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=". Κάθε λογαριασμός "),
                TextSegment(
                    text="ανοίγεται σε ένα συγκεκριμένο κατάστημα",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ 1:N",
                    badge_class="badge-rel-1n",
                    tooltip="Συσχέτιση 1:N (ΑΝΟΙΓΕΤΑΙ_ΣΕ): Ένα κατάστημα εξυπηρετεί πολλούς λογαριασμούς.",
                ),
                TextSegment(text=". Ένας λογαριασμός μπορεί να έχει "),
                TextSegment(
                    text="περισσότερους από έναν συνδικαιούχους πελάτες (κοινός λογαριασμός), και ένας πελάτης μπορεί να κατέχει πολλούς λογαριασμούς",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ N:M",
                    badge_class="badge-rel-nm",
                    tooltip="Συσχέτιση N:M (ΚΑΤΕΧΕΙ_ΛΟΓΑΡΙΑΣΜΟ): Υλοποιείται με πίνακα διασύνδεσης ΣΥΝΔΙΚΑΙΟΥΧΟΣ_ΛΟΓΑΡΙΑΣΜΟΥ.",
                ),
                TextSegment(text=". Για κάθε συσχέτιση πελάτη-λογαριασμού καταγράφεται η "),
                TextSegment(
                    text="ιδιότητα δικαιούχου (π.χ. 'Κύριος Δικαιούχος', 'Συνδικαιούχος')",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ ΣΧΕΣΗΣ",
                    badge_class="badge-attr-composite",
                    tooltip="Γνώρισμα Συσχέτισης N:M: Αποθηκεύεται στον πίνακα ΣΥΝΔΙΚΑΙΟΥΧΟΣ_ΛΟΓΑΡΙΑΣΜΟΥ.",
                ),
                TextSegment(text=" και η "),
                TextSegment(
                    text="ημερομηνία προσθήκης του στον λογαριασμό",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ ΣΧΕΣΗΣ",
                    badge_class="badge-attr-composite",
                    tooltip="Γνώρισμα Συσχέτισης N:M: Αποθηκεύεται στον πίνακα ΣΥΝΔΙΚΑΙΟΥΧΟΣ_ΛΟΓΑΡΙΑΣΜΟΥ.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-emerald-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="5. <strong>Κινήσεις Λογαριασμών & Συναλλαγές (Transactions):</strong> Κάθε φορά που εκτελείται μια συναλλαγή σε έναν λογαριασμό, καταγράφεται μια νέα κίνηση. Κάθε κίνηση χαρακτηρίζεται από έναν "),
                TextSegment(
                    text="αύξοντα αριθμό κίνησης εντός του συγκεκριμένου λογαριασμού",
                    is_highlight=True,
                    category="key",
                    tag_label="PARTIAL KEY",
                    badge_class="badge-key-partial",
                    tooltip="Μερικό Κλειδί (Partial Key / Discriminator): Ταυτοποιεί την κίνηση μόνο σε συνδυασμό με το IBAN.",
                ),
                TextSegment(text=", την "),
                TextSegment(text="ακριβή ημερομηνία και ώρα της συναλλαγής", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", το "),
                TextSegment(text="ποσό", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", τον "),
                TextSegment(text="τύπο συναλλαγής ('Κατάθεση', 'Ανάληψη', 'Πληρωμή', 'Έμβασμα')", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και το "),
                TextSegment(text="κανάλι εξυπηρέτησης (π.χ. 'ATM', 'Web Banking', 'Κατάστημα')", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=". "),
                TextSegment(
                    text="Μια κίνηση δεν μπορεί να υπάρξει αυτόνομα χωρίς τον αντίστοιχο τραπεζικό λογαριασμό",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΑΣΘΕΝΗΣ ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-weak",
                    tooltip="Υπαρκτική Εξάρτηση (Weak Entity): Προσδιορίζουσα οντότητα είναι ο ΤΡΑΠΕΖΙΚΟΣ_ΛΟΓΑΡΙΑΣΜΟΣ.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-rose-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="6. <strong>Τραπεζικά Δάνεια (Loans):</strong> Κάθε δάνειο έχει έναν "),
                TextSegment(
                    text="μοναδικό αριθμό δανείου (Loan Number)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Μοναδικός κωδικός δανείου.",
                ),
                TextSegment(text=", το "),
                TextSegment(text="αρχικό εγκεκριμένο ποσό", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", το "),
                TextSegment(text="τρέχον ανεξόφλητο ποσό", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", το "),
                TextSegment(text="επιτόκιο", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και τη "),
                TextSegment(text="διάρκεια σε μήνες", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=". Κάθε δάνειο "),
                TextSegment(
                    text="χορηγείται από ένα συγκεκριμένο τραπεζικό κατάστημα",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ 1:N",
                    badge_class="badge-rel-1n",
                    tooltip="Συσχέτιση 1:N (ΧΟΡΗΓΕΙΤΑΙ_ΑΠΟ): Κάθε δάνειο εκδίδεται από ένα κατάστημα.",
                ),
                TextSegment(text=" και "),
                TextSegment(
                    text="συνδέεται με έναν ή περισσότερους δανειολήπτες πελάτες",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ N:M",
                    badge_class="badge-rel-nm",
                    tooltip="Συσχέτιση N:M (ΔΑΝΕΙΟΛΗΠΤΗΣ): Ένα δάνειο μπορεί να έχει συν-δανειολήπτες και ένας πελάτης πολλαπλά δάνεια.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-cyan-500",
        ),
    ]

    # 2. Detailed Entities List
    entities = [
        Entity(
            name="ΚΑΤΑΣΤΗΜΑ (Branch)",
            entity_type="Ισχυρή Οντότητα",
            is_weak=False,
            owner_entity=None,
            justification="Αυτοτελής διοικητική μονάδα του τραπεζικού ομίλου με αυτόνομη υπόσταση και μοναδικό κωδικό Branch Code.",
            attributes=[
                Attribute("branch_code", "Απλό / Μονότιμο", is_pk=True, notes="Μοναδικός κωδικός καταστήματος (PK)"),
                Attribute("branch_name", "Απλό / Μονότιμο", is_candidate=True, notes="Μοναδική επωνυμία καταστήματος (Candidate Key)"),
                Attribute("city", "Απλό / Μονότιμο", notes="Πόλη έδρας καταστήματος"),
                Attribute("annual_budget", "Απλό / Μονότιμο", notes="Ετήσιος λειτουργικός προϋπολογισμός"),
            ],
        ),
        Entity(
            name="ΥΠΑΛΛΗΛΟΣ (Staff / Employee)",
            entity_type="Ισχυρή Οντότητα",
            is_weak=False,
            owner_entity=None,
            justification="Φυσικό πρόσωπο εργαζομένου με αυτόνομη οντότητα και μοναδικά αναγνωριστικά ΑΜΥ και ΑΦΜ.",
            attributes=[
                Attribute("amy", "Απλό / Μονότιμο", is_pk=True, notes="Αριθμός Μητρώου Υπαλλήλου (PK)"),
                Attribute("afm", "Απλό / Μονότιμο", is_candidate=True, notes="Αριθμός Φορολογικού Μητρώου (Candidate Key)"),
                Attribute("onoma", "Απλό / Μονότιμο", notes="Όνομα υπαλλήλου"),
                Attribute("eponymo", "Απλό / Μονότιμο", notes="Επώνυμο υπαλλήλου"),
                Attribute("misthos", "Απλό / Μονότιμο", notes="Μηνιαίος μικτός μισθός"),
                Attribute("hmer_proslipsis", "Απλό / Μονότιμο", notes="Ημερομηνία πρόσληψης"),
                Attribute("diefthynsi", "Σύνθετο", components=["odos", "arithmos", "poli"], notes="Διεύθυνση κατοικίας (οδός, αριθμός, πόλη)"),
            ],
        ),
        Entity(
            name="ΠΕΛΑΤΗΣ (Customer)",
            entity_type="Ισχυρή Οντότητα",
            is_weak=False,
            owner_entity=None,
            justification="Φυσικό πρόσωπο συναλλασσόμενο με την τράπεζα, με μοναδικό ΑΦΜ και δελτίο ταυτότητας.",
            attributes=[
                Attribute("afm", "Απλό / Μονότιμο", is_pk=True, notes="Αριθμός Φορολογικού Μητρώου (PK)"),
                Attribute("adt", "Απλό / Μονότιμο", is_candidate=True, notes="Αριθμός Δελτίου Ταυτότητας (Candidate Key)"),
                Attribute("onoma", "Απλό / Μονότιμο", notes="Όνομα πελάτη"),
                Attribute("eponymo", "Απλό / Μονότιμο", notes="Επώνυμο πελάτη"),
                Attribute("hmer_gennisis", "Απλό / Μονότιμο", notes="Ημερομηνία γέννησης"),
                Attribute("diefthynsi", "Σύνθετο", components=["odos", "arithmos", "tk", "poli"], notes="Διεύθυνση κατοικίας (οδός, αριθμός, ΤΚ, πόλη)"),
                Attribute("credit_score", "Απλό / Μονότιμο", notes="Πιστοληπτική βαθμολογία αξιολόγησης"),
                Attribute("tilefona", "Πλειότιμο", notes="Πολλαπλά τηλέφωνα επικοινωνίας (Πίνακας ΤΗΛΕΦΩΝΟ_ΠΕΛΑΤΗ)"),
            ],
        ),
        Entity(
            name="ΤΡΑΠΕΖΙΚΟΣ_ΛΟΓΑΡΙΑΣΜΟΣ (Bank Account)",
            entity_type="Ισχυρή Οντότητα",
            is_weak=False,
            owner_entity=None,
            justification="Αυτοτελής οικονομική οντότητα με παγκοσμίως μοναδικό αριθμό IBAN.",
            attributes=[
                Attribute("iban", "Απλό / Μονότιμο", is_pk=True, notes="Διεθνής αριθμός τραπεζικού λογαριασμού (PK)"),
                Attribute("balance", "Απλό / Μονότιμο", notes="Τρέχον λογιστικό υπόλοιπο"),
                Attribute("typos_logariasmou", "Απλό / Μονότιμο", notes="Είδος ('Ταμιευτήριο', 'Τρεχούμενος', 'Μισθοδοσίας')"),
                Attribute("hmer_anoigmatos", "Απλό / Μονότιμο", notes="Ημερομηνία δημιουργίας λογαριασμού"),
            ],
        ),
        Entity(
            name="ΚΙΝΗΣΗ_ΛΟΓΑΡΙΑΣΜΟΥ (Account Transaction)",
            entity_type="Ασθενής Οντότητα",
            is_weak=True,
            owner_entity="ΤΡΑΠΕΖΙΚΟΣ_ΛΟΓΑΡΙΑΣΜΟΣ",
            justification="Ασθενής οντότητα υπαρκτικά και ταυτοποιητικά εξαρτημένη από τον λογαριασμό. Δεν υφίσταται κίνηση χωρίς IBAN.",
            attributes=[
                Attribute("arithmos_kinisis", "Απλό / Μονότιμο", is_partial=True, notes="Μερικό Κλειδί (Discriminator) εντός του λογαριασμού"),
                Attribute("hmerominia_ora", "Απλό / Μονότιμο", notes="Ακριβής χρονοσφραγίδα εκτέλεσης συναλλαγής"),
                Attribute("poso", "Απλό / Μονότιμο", notes="Ποσό συναλλαγής"),
                Attribute("typos_synallagis", "Απλό / Μονότιμο", notes="Είδος ('Κατάθεση', 'Ανάληψη', 'Πληρωμή', 'Έμβασμα')"),
                Attribute("kanali_exypiretisis", "Απλό / Μονότιμο", notes="Κανάλι ('ATM', 'Web Banking', 'Κατάστημα')"),
            ],
        ),
        Entity(
            name="ΔΑΝΕΙΟ (Loan)",
            entity_type="Ισχυρή Οντότητα",
            is_weak=False,
            owner_entity=None,
            justification="Αυτοτελής δανειακή σύμβαση με μοναδικό αριθμό Loan Number.",
            attributes=[
                Attribute("loan_number", "Απλό / Μονότιμο", is_pk=True, notes="Μοναδικός αριθμός σύμβασης δανείου (PK)"),
                Attribute("arxiko_poso", "Απλό / Μονότιμο", notes="Αρχικό εγκεκριμένο κεφάλαιο"),
                Attribute("anexoflito_poso", "Απλό / Μονότιμο", notes="Τρέχον οφειλόμενο ανεξόφλητο ποσό"),
                Attribute("epitokio", "Απλό / Μονότιμο", notes="Ετήσιο επιτόκιο δανεισμού (%)"),
                Attribute("diarkeia_mines", "Απλό / Μονότιμο", notes="Συνολική διάρκεια αποπληρωμής σε μήνες"),
            ],
        ),
    ]

    # 3. Relationship Attributes
    relationship_attributes = [
        RelationshipAttribute(
            name="hmer_analipsis",
            relationship_name="ΔΙΕΥΘΥΝΕΙ (ΚΑΤΑΣΤΗΜΑ - ΥΠΑΛΛΗΛΟΣ)",
            justification="Ημερομηνία κατά την οποία ο υπάλληλος ανέλαβε καθήκοντα διευθυντή στο κατάστημα (ενσωματώνεται στον πίνακα ΚΑΤΑΣΤΗΜΑ).",
        ),
        RelationshipAttribute(
            name="idiotita_dikaiouxou",
            relationship_name="ΚΑΤΕΧΕΙ_ΛΟΓΑΡΙΑΣΜΟ (ΠΕΛΑΤΗΣ - ΤΡΑΠΕΖΙΚΟΣ_ΛΟΓΑΡΙΑΣΜΟΣ)",
            justification="Χαρακτηρισμός του πελάτη ως 'Κύριος Δικαιούχος' ή 'Συνδικαιούχος' για τον συγκεκριμένο κοινό λογαριασμό.",
        ),
        RelationshipAttribute(
            name="hmer_prosthiki",
            relationship_name="ΚΑΤΕΧΕΙ_ΛΟΓΑΡΙΑΣΜΟ (ΠΕΛΑΤΗΣ - ΤΡΑΠΕΖΙΚΟΣ_ΛΟΓΑΡΙΑΣΜΟΣ)",
            justification="Ημερομηνία κατά την οποία ο συνδικαιούχος προστέθηκε στον τραπεζικό λογαριασμό.",
        ),
    ]

    # 4. Keys Analysis Table
    keys_analysis = [
        KeyAnalysisRow(
            entity_name="ΚΑΤΑΣΤΗΜΑ",
            key_count="2 Υποψήφια",
            key_types="Υποψήφια: {branch_code}, {branch_name}",
            final_pk_selection="branch_code",
            justification="Μικρό, σταθερό, αριθμητικό αναγνωριστικό βέλτιστο για Primary Key και Foreign Key δεικτοδότηση.",
        ),
        KeyAnalysisRow(
            entity_name="ΥΠΑΛΛΗΛΟΣ",
            key_count="2 Υποψήφια",
            key_types="Υποψήφια: {amy}, {afm}",
            final_pk_selection="amy",
            justification="Ο εσωτερικός αριθμός μητρώου (ΑΜΥ) είναι συμπαγής και δεν αλλάζει, ενώ το ΑΦΜ προστατεύεται ως Unique Candidate Key.",
        ),
        KeyAnalysisRow(
            entity_name="ΠΕΛΑΤΗΣ",
            key_count="2 Υποψήφια",
            key_types="Υποψήφια: {afm}, {adt}",
            final_pk_selection="afm",
            justification="Το ΑΦΜ αποτελεί το επίσημο, αναλλοίωτο φορολογικό αναγνωριστικό σε όλα τα τραπεζικά ιδρύματα (το ΑΔΤ μπορεί να αντικατασταθεί).",
        ),
        KeyAnalysisRow(
            entity_name="ΤΡΑΠΕΖΙΚΟΣ_ΛΟΓΑΡΙΑΣΜΟΣ",
            key_count="1 Υποψήφιο",
            key_types="Υποψήφιο: {iban}",
            final_pk_selection="iban",
            justification="Ο παγκόσμιος κωδικός IBAN ταυτοποιεί μονοσήμαντα κάθε λογαριασμό διεθνώς.",
        ),
        KeyAnalysisRow(
            entity_name="ΚΙΝΗΣΗ_ΛΟΓΑΡΙΑΣΜΟΥ",
            key_count="Ασθενής (1 Μερικό)",
            key_types="Μερικό Κλειδί: {arithmos_kinisis}",
            final_pk_selection="(iban, arithmos_kinisis)",
            justification="Σύνθετο πρωτεύον κλειδί αποτελούμενο από το Foreign Key της προσδιορίζουσας οντότητας και τον αύξοντα αριθμό κίνησης.",
            is_weak=True,
        ),
        KeyAnalysisRow(
            entity_name="ΔΑΝΕΙΟ",
            key_count="1 Υποψήφιο",
            key_types="Υποψήφιο: {loan_number}",
            final_pk_selection="loan_number",
            justification="Μοναδικός αριθμός σύμβασης δανείου που εκδίδει το σύστημα πιστοδοτήσεων.",
        ),
    ]

    # 5. Relationships List
    relationships = [
        Relationship(
            letter_id="α",
            name="ΔΙΕΥΘΥΝΕΙ (Manages)",
            connected_entities="ΚΑΤΑΣΤΗΜΑ <-> ΥΠΑΛΛΗΛΟΣ",
            cardinality="1:1",
            participation="Ολική για Κατάστημα (1,1), Μερική για Υπάλληλο (0,1)",
            relationship_type="Κανονική Σχέση",
            attributes=["hmer_analipsis"],
            justification="Κάθε κατάστημα διευθύνεται υποχρεωτικά από έναν διευθυντή. Ένας υπάλληλος μπορεί να διευθύνει το πολύ ένα κατάστημα ή κανένα.",
        ),
        Relationship(
            letter_id="β",
            name="ΕΡΓΑΖΕΤΑΙ_ΣΕ (Works In)",
            connected_entities="ΚΑΤΑΣΤΗΜΑ <-> ΥΠΑΛΛΗΛΟΣ",
            cardinality="1:N",
            participation="Ολική για Υπάλληλο (1,1), Ολική για Κατάστημα (1,N)",
            relationship_type="Κανονική Σχέση",
            attributes=[],
            justification="Κάθε υπάλληλος ανήκει υποχρεωτικά σε ένα κατάστημα. Ένα κατάστημα απασχολεί υποχρεωτικά υπαλλήλους.",
        ),
        Relationship(
            letter_id="γ",
            name="ΕΠΟΠΤΕΥΕΙ (Supervises - Αναδρομική)",
            connected_entities="ΥΠΑΛΛΗΛΟΣ <-> ΥΠΑΛΛΗΛΟΣ",
            cardinality="1:N",
            participation="Μερική για Προϊστάμενο (0,N), Μερική για Υφιστάμενο (0,1)",
            relationship_type="Αναδρομική Σχέση (Unary)",
            attributes=[],
            justification="Ένας προϊστάμενος εποπτεύει πολλούς υπαλλήλους. Κάθε υπάλληλος εποπτεύεται από έναν προϊστάμενο (εκτός του Γενικού Διευθυντή που έχει 0).",
        ),
        Relationship(
            letter_id="δ",
            name="ΑΝΟΙΓΕΤΑΙ_ΣΕ (Account Opening)",
            connected_entities="ΚΑΤΑΣΤΗΜΑ <-> ΤΡΑΠΕΖΙΚΟΣ_ΛΟΓΑΡΙΑΣΜΟΣ",
            cardinality="1:N",
            participation="Ολική για Λογαριασμό (1,1), Μερική για Κατάστημα (0,N)",
            relationship_type="Κανονική Σχέση",
            attributes=[],
            justification="Κάθε λογαριασμός ανοίγεται σε ένα συγκεκριμένο κατάστημα εξυπηρέτησης. Ένα κατάστημα διατηρεί πολλούς λογαριασμούς.",
        ),
        Relationship(
            letter_id="ε",
            name="ΚΑΤΕΧΕΙ_ΛΟΓΑΡΙΑΣΜΟ (Account Ownership)",
            connected_entities="ΠΕΛΑΤΗΣ <-> ΤΡΑΠΕΖΙΚΟΣ_ΛΟΓΑΡΙΑΣΜΟΣ",
            cardinality="N:M",
            participation="Ολική για Λογαριασμό (1,N), Μερική για Πελάτη (0,N)",
            relationship_type="Κανονική Σχέση (Junction)",
            attributes=["idiotita_dikaiouxou", "hmer_prosthiki"],
            justification="Ένας λογαριασμός μπορεί να έχει πολλαπλούς συνδικαιούχους και ένας πελάτης πολλαπλούς λογαριασμούς.",
        ),
        Relationship(
            letter_id="στ",
            name="ΕΚΤΕΛΕΙΤΑΙ_ΣΕ (Contains Movement)",
            connected_entities="ΤΡΑΠΕΖΙΚΟΣ_ΛΟΓΑΡΙΑΣΜΟΣ <-> ΚΙΝΗΣΗ_ΛΟΓΑΡΙΑΣΜΟΥ",
            cardinality="1:N",
            participation="Ολική για Κίνηση (1,1), Μερική για Λογαριασμό (0,N)",
            relationship_type="Ταυτοποιούσα Σχέση (Identifying)",
            attributes=[],
            justification="Ταυτοποιούσα σχέση της ασθενούς οντότητας ΚΙΝΗΣΗ_ΛΟΓΑΡΙΑΣΜΟΥ από τον προσδιορίζοντα ΤΡΑΠΕΖΙΚΟ_ΛΟΓΑΡΙΑΣΜΟ.",
        ),
        Relationship(
            letter_id="ζ",
            name="ΧΟΡΗΓΕΙΤΑΙ_ΑΠΟ (Loan Granting)",
            connected_entities="ΚΑΤΑΣΤΗΜΑ <-> ΔΑΝΕΙΟ",
            cardinality="1:N",
            participation="Ολική για Δάνειο (1,1), Μερική για Κατάστημα (0,N)",
            relationship_type="Κανονική Σχέση",
            attributes=[],
            justification="Κάθε δάνειο χορηγείται από ένα συγκεκριμένο κατάστημα της τράπεζας.",
        ),
        Relationship(
            letter_id="η",
            name="ΣΥΝΔΕΕΤΑΙ_ΜΕ_ΔΑΝΕΙΟΛΗΠΤΗ (Loan Borrowers)",
            connected_entities="ΠΕΛΑΤΗΣ <-> ΔΑΝΕΙΟ",
            cardinality="N:M",
            participation="Ολική για Δάνειο (1,N), Μερική για Πελάτη (0,N)",
            relationship_type="Κανονική Σχέση (Junction)",
            attributes=[],
            justification="Ένα δάνειο μπορεί να έχει κύριο δανειολήπτη και εγγυητές/συνοφειλέτες, και ένας πελάτης μπορεί να λάβει πολλαπλά δάνεια.",
        ),
    ]

    # 6. Design Assumptions
    assumptions = [
        "Ο Γενικός Διευθυντής δεν έχει προϊστάμενο (supervisor_amy IS NULL) στην αναδρομική ιεραρχία.",
        "Κάθε τραπεζικός λογαριασμός έχει τουλάχιστον έναν κύριο δικαιούχο (idiotita_dikaiouxou = 'Κύριος Δικαιούχος').",
        "Τα τηλέφωνα πελάτη εξάγονται σε ανεξάρτητο σχεσιακό πίνακα ΤΗΛΕΦΩΝΟ_ΠΕΛΑΤΗ με σύνθετο πρωτεύον κλειδί (afm, tilefono).",
        "Οι κινήσεις λογαριασμού αριθμούνται σειριακά (1, 2, 3, ...) ανά λογαριασμό (arithmos_kinisis).",
        "Η συσχέτιση 1:1 διεύθυνσης καταστήματος υλοποιείται με Foreign Key manager_amy στον πίνακα ΚΑΤΑΣΤΗΜΑ με UNIQUE constraint.",
    ]

    # 7. ER Diagram Tables (Coordinates & Attributes for Crow's Foot Diagram)
    er_tables = [
        ERTable(
            id="t-branch",
            label="KATASTHMA",
            x=50,
            y=50,
            attrs=[
                ERTableAttr("branch_code", pk=True),
                ERTableAttr("branch_name"),
                ERTableAttr("city"),
                ERTableAttr("annual_budget"),
                ERTableAttr("manager_amy", fk=True),
                ERTableAttr("appointment_date"),
            ],
        ),
        ERTable(
            id="t-employee",
            label="YPALLILOS",
            x=450,
            y=50,
            attrs=[
                ERTableAttr("amy", pk=True),
                ERTableAttr("afm"),
                ERTableAttr("onoma"),
                ERTableAttr("eponymo"),
                ERTableAttr("misthos"),
                ERTableAttr("hmer_proslipsis"),
                ERTableAttr("diefthynsi_odos"),
                ERTableAttr("diefthynsi_arithmos"),
                ERTableAttr("diefthynsi_poli"),
                ERTableAttr("branch_code", fk=True),
                ERTableAttr("supervisor_amy", fk=True),
            ],
        ),
        ERTable(
            id="t-customer",
            label="PELATIS",
            x=850,
            y=50,
            attrs=[
                ERTableAttr("afm", pk=True),
                ERTableAttr("adt"),
                ERTableAttr("onoma"),
                ERTableAttr("eponymo"),
                ERTableAttr("hmer_gennisis"),
                ERTableAttr("odos"),
                ERTableAttr("arithmos"),
                ERTableAttr("tk"),
                ERTableAttr("poli"),
                ERTableAttr("credit_score"),
            ],
        ),
        ERTable(
            id="t-cust-phone",
            label="TILEFONO_PELATI",
            x=850,
            y=430,
            attrs=[
                ERTableAttr("afm", pk=True, fk=True),
                ERTableAttr("tilefono", pk=True),
                ERTableAttr("typos_tilefonou"),
            ],
        ),
        ERTable(
            id="t-account",
            label="LOGARIASMOS",
            x=50,
            y=390,
            attrs=[
                ERTableAttr("iban", pk=True),
                ERTableAttr("balance"),
                ERTableAttr("typos_logariasmou"),
                ERTableAttr("hmer_anoigmatos"),
                ERTableAttr("branch_code", fk=True),
            ],
        ),
        ERTable(
            id="t-transaction",
            label="KINISI_LOGARIASMOU",
            x=50,
            y=640,
            attrs=[
                ERTableAttr("iban", pk=True, fk=True),
                ERTableAttr("arithmos_kinisis", pk=True),
                ERTableAttr("hmerominia_ora"),
                ERTableAttr("poso"),
                ERTableAttr("typos_synallagis"),
                ERTableAttr("kanali_exypiretisis"),
            ],
        ),
        ERTable(
            id="t-account-holder",
            label="SYNDIKAIUXOS_LOGARIASMOU",
            x=450,
            y=430,
            attrs=[
                ERTableAttr("iban", pk=True, fk=True),
                ERTableAttr("afm", pk=True, fk=True),
                ERTableAttr("idiotita_dikaiouxou"),
                ERTableAttr("hmer_prosthiki"),
            ],
        ),
        ERTable(
            id="t-loan",
            label="DANEIO",
            x=450,
            y=640,
            attrs=[
                ERTableAttr("loan_number", pk=True),
                ERTableAttr("arxiko_poso"),
                ERTableAttr("anexoflito_poso"),
                ERTableAttr("epitokio"),
                ERTableAttr("diarkeia_mines"),
                ERTableAttr("branch_code", fk=True),
            ],
        ),
        ERTable(
            id="t-borrower",
            label="DANEIOLIPTIS",
            x=850,
            y=640,
            attrs=[
                ERTableAttr("loan_number", pk=True, fk=True),
                ERTableAttr("afm", pk=True, fk=True),
            ],
        ),
    ]

    # 8. ER Diagram Edges
    er_edges = [
        # Branch directs Employee (1:1)
        EREdge("M 310 80 L 450 80", "start-one-mandatory", "end-one-optional", "ΔΙΕΥΘΥΝΕΙ (1:1)", 380, 70),
        # Branch employs Employees (1:N)
        EREdge("M 310 120 L 450 120", "start-one-mandatory", "end-many-mandatory", "ΕΡΓΑΖΕΤΑΙ_ΣΕ (1:N)", 380, 135),
        # Employee recursive supervisor (1:N)
        EREdge("M 650 90 C 720 30, 720 170, 650 150", "start-one-optional", "end-many-optional", "ΕΠΟΠΤΕΥΕΙ (1:N)", 730, 100),
        # Branch opens Accounts (1:N)
        EREdge("M 150 210 L 150 390", "start-one-optional", "end-many-mandatory", "ΑΝΟΙΓΕΤΑΙ_ΣΕ (1:N)", 165, 300),
        # Account contains Movements (1:N identifying)
        EREdge("M 150 530 L 150 640", "start-one-optional", "end-many-mandatory", "ΕΚΤΕΛΕΙΤΑΙ_ΣΕ (1:N)", 165, 585),
        # Account to Co-holders (1:N)
        EREdge("M 250 430 L 450 430", "start-one-mandatory", "end-many-mandatory", "ΣΥΝΔΙΚΑΙΟΥΧΟΣ (1:N)", 350, 420),
        # Customer to Co-holders (1:N)
        EREdge("M 850 160 L 650 430", "start-one-optional", "end-many-mandatory", "ΚΑΤΕΧΕΙ (1:N)", 750, 300),
        # Customer to Phone numbers (1:N)
        EREdge("M 950 310 L 950 430", "start-one-optional", "end-many-mandatory", "ΕΧΕΙ_ΤΗΛΕΦΩΝΟ (1:N)", 965, 370),
        # Branch issues Loans (1:N)
        EREdge("M 200 210 L 450 670", "start-one-optional", "end-many-mandatory", "ΧΟΡΗΓΕΙΤΑΙ_ΑΠΟ (1:N)", 310, 480),
        # Loan to Borrowers (1:N)
        EREdge("M 650 680 L 850 680", "start-one-mandatory", "end-many-mandatory", "ΔΑΝΕΙΟΛΗΠΤΗΣ (1:N)", 750, 670),
        # Customer to Borrowers (1:N)
        EREdge("M 950 310 L 950 640", "start-one-optional", "end-many-mandatory", "ΛΑΜΒΑΝΕΙ_ΔΑΝΕΙΟ (1:N)", 965, 520),
    ]

    # 9. Relational Conversion Justifications
    relational_justifications = [
        RelationalJustification(
            title="1. Μετατροπή Ισχυρών Οντοτήτων (ΚΑΤΑΣΤΗΜΑ, ΥΠΑΛΛΗΛΟΣ, ΠΕΛΑΤΗΣ, ΛΟΓΑΡΙΑΣΜΟΣ, ΔΑΝΕΙΟ)",
            color_class="border-blue-500",
            description="Κάθε ισχυρή οντότητα μετατρέπεται σε ανεξάρτητο πίνακα με πρωτεύον κλειδί το αντίστοιχο κύριο υποψήφιο κλειδί (branch_code, amy, afm, iban, loan_number). Τα σύνθετα γνωρίσματα διευθύνσεων αναλύονται σε ατομικές στήλες.",
        ),
        RelationalJustification(
            title="2. Μετατροπή Ασθενούς Οντότητας (ΚΙΝΗΣΗ_ΛΟΓΑΡΙΑΣΜΟΥ)",
            color_class="border-red-500",
            description="Ο πίνακας ΚΙΝΗΣΗ_ΛΟΓΑΡΙΑΣΜΟΥ λαμβάνει ως Foreign Key το πρωτεύον κλειδί iban της προσδιορίζουσας οντότητας ΛΟΓΑΡΙΑΣΜΟΣ. Το πρωτεύον κλειδί είναι σύνθετο: PRIMARY KEY (iban, arithmos_kinisis) με ON DELETE CASCADE.",
        ),
        RelationalJustification(
            title="3. Μετατροπή Συσχετίσεων 1:1 και 1:N (ΔΙΕΥΘΥΝΕΙ, ΕΡΓΑΖΕΤΑΙ_ΣΕ, ΕΠΟΠΤΕΥΕΙ, ΑΝΟΙΓΕΤΑΙ_ΣΕ, ΧΟΡΗΓΕΙΤΑΙ_ΑΠΟ)",
            color_class="border-emerald-500",
            description="Στη σχέση 1:1 ΔΙΕΥΘΥΝΕΙ το Foreign Key manager_amy και το γνώρισμα appointment_date τοποθετούνται στον πίνακα ΚΑΤΑΣΤΗΜΑ με UNIQUE constraint. Στις σχέσεις 1:N το PK της πλευράς 1 εισάγεται ως FK στην πλευρά N.",
        ),
        RelationalJustification(
            title="4. Μετατροπή Συσχετίσεων N:M (ΚΑΤΕΧΕΙ_ΛΟΓΑΡΙΑΣΜΟ, ΣΥΝΔΕΕΤΑΙ_ΜΕ_ΔΑΝΕΙΟΛΗΠΤΗ)",
            color_class="border-amber-500",
            description="Δημιουργούνται οι πίνακες σύνδεσης SYNDIKAIUXOS_LOGARIASMOU (με σύνθετο PK iban + afm και τα γνωρίσματα σχέσης) και DANEIOLIPTIS (με σύνθετο PK loan_number + afm).",
        ),
        RelationalJustification(
            title="5. Μετατροπή Πλειότιμου Γνωρίσματος (ΤΗΛΕΦΩΝΑ_ΠΕΛΑΤΗ)",
            color_class="border-purple-500",
            description="Το πλειότιμο γνώρισμα τηλεφώνου εξάγεται στον πίνακα TILEFONO_PELATI με σύνθετο πρωτεύον κλειδί PRIMARY KEY (afm, tilefono) και FOREIGN KEY (afm) REFERENCES PELATIS(afm) ON DELETE CASCADE.",
        ),
    ]

    # 10. Complete Production SQL DDL
    sql_ddl = """-- ==========================================================
-- PostgreSQL / MySQL Relational Schema for Banking System
-- Case Study: Exam Paper 4 (Τραπεζικός Όμιλος & Συναλλαγές)
-- ==========================================================

-- 1. Entity: YPALLILOS (Pre-created for foreign keys)
CREATE TABLE YPALLILOS (
    amy VARCHAR(15) PRIMARY KEY,
    afm VARCHAR(9) NOT NULL UNIQUE,
    onoma VARCHAR(50) NOT NULL,
    eponymo VARCHAR(50) NOT NULL,
    misthos DECIMAL(10, 2) NOT NULL CHECK (misthos > 0),
    hmer_proslipsis DATE NOT NULL,
    diefthynsi_odos VARCHAR(50) NOT NULL,
    diefthynsi_arithmos VARCHAR(10) NOT NULL,
    diefthynsi_poli VARCHAR(50) NOT NULL,
    branch_code VARCHAR(10) NOT NULL,
    supervisor_amy VARCHAR(15),
    FOREIGN KEY (supervisor_amy) REFERENCES YPALLILOS(amy) ON DELETE SET NULL
);

-- 2. Entity: KATASTHMA
CREATE TABLE KATASTHMA (
    branch_code VARCHAR(10) PRIMARY KEY,
    branch_name VARCHAR(100) NOT NULL UNIQUE,
    city VARCHAR(50) NOT NULL,
    annual_budget DECIMAL(14, 2) NOT NULL CHECK (annual_budget >= 0),
    manager_amy VARCHAR(15) NOT NULL UNIQUE,
    appointment_date DATE NOT NULL,
    FOREIGN KEY (manager_amy) REFERENCES YPALLILOS(amy)
);

-- Add circular foreign key for Employee's workplace
ALTER TABLE YPALLILOS
ADD CONSTRAINT fk_emp_branch
FOREIGN KEY (branch_code) REFERENCES KATASTHMA(branch_code);

-- 3. Entity: PELATIS
CREATE TABLE PELATIS (
    afm VARCHAR(9) PRIMARY KEY,
    adt VARCHAR(15) NOT NULL UNIQUE,
    onoma VARCHAR(50) NOT NULL,
    eponymo VARCHAR(50) NOT NULL,
    hmer_gennisis DATE NOT NULL,
    odos VARCHAR(50) NOT NULL,
    arithmos VARCHAR(10) NOT NULL,
    tk VARCHAR(10) NOT NULL,
    poli VARCHAR(50) NOT NULL,
    credit_score INT NOT NULL CHECK (credit_score BETWEEN 300 AND 850)
);

-- 4. Multi-valued Attribute: TILEFONO_PELATI
CREATE TABLE TILEFONO_PELATI (
    afm VARCHAR(9) NOT NULL,
    tilefono VARCHAR(20) NOT NULL,
    typos_tilefonou VARCHAR(20) DEFAULT 'Mobile',
    PRIMARY KEY (afm, tilefono),
    FOREIGN KEY (afm) REFERENCES PELATIS(afm) ON DELETE CASCADE
);

-- 5. Entity: LOGARIASMOS
CREATE TABLE LOGARIASMOS (
    iban VARCHAR(34) PRIMARY KEY,
    balance DECIMAL(14, 2) NOT NULL DEFAULT 0.00,
    typos_logariasmou VARCHAR(30) NOT NULL CHECK (typos_logariasmou IN ('Ταμιευτήριο', 'Τρεχούμενος', 'Μισθοδοσίας', 'Προθεσμιακός')),
    hmer_anoigmatos DATE NOT NULL,
    branch_code VARCHAR(10) NOT NULL,
    FOREIGN KEY (branch_code) REFERENCES KATASTHMA(branch_code)
);

-- 6. Weak Entity: KINISI_LOGARIASMOU
CREATE TABLE KINISI_LOGARIASMOU (
    iban VARCHAR(34) NOT NULL,
    arithmos_kinisis INT NOT NULL,
    hmerominia_ora TIMESTAMP NOT NULL,
    poso DECIMAL(12, 2) NOT NULL CHECK (poso > 0),
    typos_synallagis VARCHAR(30) NOT NULL CHECK (typos_synallagis IN ('Κατάθεση', 'Ανάληψη', 'Πληρωμή', 'Έμβασμα')),
    kanali_exypiretisis VARCHAR(30) NOT NULL CHECK (kanali_exypiretisis IN ('ATM', 'Web Banking', 'Κατάστημα', 'Mobile App')),
    PRIMARY KEY (iban, arithmos_kinisis),
    FOREIGN KEY (iban) REFERENCES LOGARIASMOS(iban) ON DELETE CASCADE
);

-- 7. Junction Table: SYNDIKAIUXOS_LOGARIASMOU (N:M)
CREATE TABLE SYNDIKAIUXOS_LOGARIASMOU (
    iban VARCHAR(34) NOT NULL,
    afm VARCHAR(9) NOT NULL,
    idiotita_dikaiouxou VARCHAR(30) NOT NULL CHECK (idiotita_dikaiouxou IN ('Κύριος Δικαιούχος', 'Συνδικαιούχος')),
    hmer_prosthiki DATE NOT NULL,
    PRIMARY KEY (iban, afm),
    FOREIGN KEY (iban) REFERENCES LOGARIASMOS(iban) ON DELETE CASCADE,
    FOREIGN KEY (afm) REFERENCES PELATIS(afm) ON DELETE CASCADE
);

-- 8. Entity: DANEIO
CREATE TABLE DANEIO (
    loan_number VARCHAR(20) PRIMARY KEY,
    arxiko_poso DECIMAL(14, 2) NOT NULL CHECK (arxiko_poso > 0),
    anexoflito_poso DECIMAL(14, 2) NOT NULL CHECK (anexoflito_poso >= 0),
    epitokio DECIMAL(5, 2) NOT NULL CHECK (epitokio >= 0),
    diarkeia_mines INT NOT NULL CHECK (diarkeia_mines > 0),
    branch_code VARCHAR(10) NOT NULL,
    FOREIGN KEY (branch_code) REFERENCES KATASTHMA(branch_code)
);

-- 9. Junction Table: DANEIOLIPTIS (N:M)
CREATE TABLE DANEIOLIPTIS (
    loan_number VARCHAR(20) NOT NULL,
    afm VARCHAR(9) NOT NULL,
    PRIMARY KEY (loan_number, afm),
    FOREIGN KEY (loan_number) REFERENCES DANEIO(loan_number) ON DELETE CASCADE,
    FOREIGN KEY (afm) REFERENCES PELATIS(afm) ON DELETE CASCADE
);"""

    return Scenario(
        id="banking_management",
        title="Σύστημα Διαχείρισης Τραπεζικού Ομίλου & Συναλλαγών",
        subtitle="Μοντελοποίηση Καταστημάτων, Υπαλλήλων, Πελατών, Τραπεζικών Λογαριασμών, Κινήσεων & Δανείων",
        course_tag="Βάσεις Δεδομένων (Πρόοδος 2025-2026 - Θέμα 4)",
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
