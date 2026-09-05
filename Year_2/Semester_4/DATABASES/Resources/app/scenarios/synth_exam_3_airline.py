"""Airline Management and Flight Operations case study scenario module.

Contains the complete parsed and modeled ER analysis for the International Airline
Company (Airports, Flight Schedules, Flight Instances, Aircraft, Flight Crew, Passengers, Bookings),
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


def createAirlineManagementScenario() -> Scenario:
    """Constructs and returns the Airline Management database scenario.

    Returns:
        Scenario: Fully populated scenario instance.
    """
    # 1. Text Paragraphs with Interactive Segments
    paragraphs = [
        Paragraph(
            segments=[
                TextSegment(text="Μια διεθνής αεροπορική εταιρεία σχεδιάζει μια νέα σχεσιακή βάση δεδομένων για τη διαχείριση του πτητικού έργου της, των "),
                TextSegment(
                    text="αεροδρομίων",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Strong Entity): Διεθνής αερολιμένας με μοναδικό κωδικό IATA.",
                ),
                TextSegment(text=", των "),
                TextSegment(
                    text="προγραμματισμένων δρομολογίων",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Strong Entity): Τακτικό δρομολόγιο με μοναδικό αριθμό πτήσης.",
                ),
                TextSegment(text=", των "),
                TextSegment(
                    text="πραγματικών πτήσεων (στιγμιότυπα)",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΑΣΘΕΝΗΣ ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-weak",
                    tooltip="Ασθενής Οντότητα (Weak Entity): Εκτέλεση δρομολογίου σε συγκεκριμένη ημερομηνία.",
                ),
                TextSegment(text=", των "),
                TextSegment(
                    text="αεροσκαφών",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Strong Entity): Σκάφος στόλου με σειριακό αριθμό κατασκευής MSN.",
                ),
                TextSegment(text=", των "),
                TextSegment(
                    text="πληρωμάτων",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Strong Entity): Προσωπικό πτήσεων με αριθμό μητρώου ΑΜΕ.",
                ),
                TextSegment(text=", των "),
                TextSegment(
                    text="επιβατών",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Ισχυρή Οντότητα (Strong Entity): Φυσικό πρόσωπο ταξιδιώτη με αριθμό διαβατηρίου.",
                ),
                TextSegment(text=" και των "),
                TextSegment(
                    text="κρατήσεων εισιτηρίων",
                    is_highlight=True,
                    category="entity",
                    tag_label="ΣΥΣΧΕΤΙΣΤΙΚΗ ΟΝΤΟΤΗΤΑ",
                    badge_class="badge-entity-strong",
                    tooltip="Συσχετιστική Οντότητα (Associative Entity): Ηλεκτρονική κράτηση εισιτηρίου με μοναδικό κωδικό PNR.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color=None,
        ),
        Paragraph(
            segments=[
                TextSegment(text="1. <strong>Αεροδρόμια (Airports):</strong> Κάθε αεροδρόμιο χαρακτηρίζεται από έναν "),
                TextSegment(
                    text="μοναδικό τριγράμματο κωδικό IATA (π.χ. ATH, LHR)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Διεθνής τριγράμματος κωδικός IATA.",
                ),
                TextSegment(text=", την "),
                TextSegment(
                    text="επίσημη ονομασία του",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Υποψήφιο Κλειδί (Candidate Key): Μοναδική ονομασία αερολιμένα.",
                ),
                TextSegment(text=", την "),
                TextSegment(text="πόλη", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και τη "),
                TextSegment(text="χώρα", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" στην οποία βρίσκεται. Κάθε αεροδρόμιο διαθέτει έναν ή περισσότερους "),
                TextSegment(
                    text="διαδρόμους προσγείωσης/απογείωσης (Runways)",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΠΛΕΙΟΤΙΜΟ",
                    badge_class="badge-attr-multi",
                    tooltip="Πλειότιμο Γνώρισμα (Multi-valued): Εξάγεται στον πίνακα ΔΙΑΔΡΟΜΟΣ_ΑΕΡΟΔΡΟΜΙΟΥ.",
                ),
                TextSegment(text=", για τους οποίους καταγράφονται τα διακριτικά μήκη και οι ονομασίες τους."),
            ],
            accent_border_color="border-blue-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="2. <strong>Προγραμματισμένα Δρομολόγια Πτήσεων (Flight Schedules):</strong> Κάθε τακτικό δρομολόγιο έχει έναν "),
                TextSegment(
                    text="μοναδικό αριθμό πτήσης (Flight Number, π.χ. OA315)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Μοναδικός αριθμός πτήσης δρομολογίου.",
                ),
                TextSegment(text=", την "),
                TextSegment(text="προγραμματισμένη ώρα αναχώρησης", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", την "),
                TextSegment(text="προγραμματισμένη ώρα άφιξης", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", την "),
                TextSegment(text="εκτιμώμενη διάρκεια πτήσης", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και την "),
                TextSegment(text="απόσταση σε ναυτικά μίλια", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=". Κάθε προγραμματισμένη πτήση συνδέει ακριβώς δύο αεροδρόμια: ένα "),
                TextSegment(
                    text="αεροδρόμιο αναχώρησης (Departure Airport)",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ 1:N",
                    badge_class="badge-rel",
                    tooltip="Σχέση 1:N (Αεροδρόμιο -> Πτήση): Σημείο αναχώρησης.",
                ),
                TextSegment(text=" και ένα "),
                TextSegment(
                    text="αεροδρόμιο άφιξης (Arrival Airport)",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ 1:N",
                    badge_class="badge-rel",
                    tooltip="Σχέση 1:N (Αεροδρόμιο -> Πτήση): Σημείο προορισμού.",
                ),
                TextSegment(text=". Ένα αεροδρόμιο μπορεί να αποτελεί σημείο αναχώρησης για πολλές πτήσεις και σημείο άφιξης για πολλές άλλες."),
            ],
            accent_border_color="border-emerald-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="3. <strong>Στιγμιότυπα Πτήσεων (Flight Instances / Actual Flights):</strong> Ένα προγραμματισμένο δρομολόγιο "),
                TextSegment(
                    text="εκτελείται",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΤΑΥΤΟΠΟΙΟΥΣΑ 1:N",
                    badge_class="badge-rel",
                    tooltip="Ταυτοποιούσα Σχέση 1:N (Προγραμματισμένη Πτήση -> Στιγμιότυπο Πτήσης): Ολική συμμετοχή στιγμιοτύπου.",
                ),
                TextSegment(text=" σε συγκεκριμένες ημερομηνίες. Κάθε συγκεκριμένη πτήση προσδιορίζεται από τον αριθμό πτήσης και την "),
                TextSegment(
                    text="ημερομηνία πτήσης (Flight Date)",
                    is_highlight=True,
                    category="key",
                    tag_label="PARTIAL KEY",
                    badge_class="badge-key-partial",
                    tooltip="Μερικό Κλειδί (Partial Key / Discriminator): Προσδιορίζει το στιγμιότυπο σε συνδυασμό με τον αριθμό πτήσης.",
                ),
                TextSegment(text=". Για κάθε πραγματική πτήση καταγράφεται η "),
                TextSegment(text="πραγματική ώρα αναχώρησης", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(text="πραγματική ώρα άφιξης", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", η "),
                TextSegment(text="κατάσταση πτήσης (π.χ. 'On Time', 'Delayed', 'Cancelled', 'Landed')", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και ο "),
                TextSegment(text="αριθμός διαθέσιμων θέσεων", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text="."),
            ],
            accent_border_color="border-amber-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="4. <strong>Αεροσκάφη (Aircraft):</strong> Ο στόλος της εταιρείας αποτελείται από αεροσκάφη. Κάθε αεροσκάφος έχει έναν "),
                TextSegment(
                    text="μοναδικό σειριακό αριθμό κατασκευής (MSN)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Manufacturer Serial Number.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="αριθμό νηολογίου (Tail Number)",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Υποψήφιο Κλειδί (Candidate Key): Μοναδικό αναγνωριστικό νηολογίου ουράς.",
                ),
                TextSegment(text=", το "),
                TextSegment(text="μοντέλο (π.χ. 'Airbus A320neo', 'Boeing 787-9')", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", το "),
                TextSegment(text="έτος κατασκευής", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και τη "),
                TextSegment(text="μέγιστη χωρητικότητα επιβατών", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=". Κάθε συγκεκριμένη πτήση (στιγμιότυπο) "),
                TextSegment(
                    text="εκτελείται από ένα και μόνο αεροσκάφος",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ 1:N",
                    badge_class="badge-rel",
                    tooltip="Σχέση 1:N (Αεροσκάφος -> Στιγμιότυπο Πτήσης): Ολική συμμετοχή πτήσης, 1 σκάφος ανά πτήση.",
                ),
                TextSegment(text="."),
            ],
            accent_border_color="border-purple-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="5. <strong>Πλήρωμα & Πιλότοι (Flight Crew):</strong> Για κάθε μέλος πληρώματος καταγράφονται: ο "),
                TextSegment(
                    text="Αριθμός Μητρώου Εργαζομένου (ΑΜΕ)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Μοναδικός αριθμός υπαλληλικού μητρώου αεροπορικής εταιρείας.",
                ),
                TextSegment(text=", "),
                TextSegment(
                    text="ΑΔΤ",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Υποψήφιο Κλειδί (Candidate Key): Κρατικό αναγνωριστικό αστυνομικής ταυτότητας.",
                ),
                TextSegment(text=", "),
                TextSegment(text="ονοματεπώνυμο", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="τηλέφωνο", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="διεύθυνση", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="ημερομηνία πρόσληψης", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και ο "),
                TextSegment(text="ρόλος (Κυβερνήτης, Συγκυβερνήτης, Προϊστάμενος Καμπίνας, Συνοδός)", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=". Για κάθε συγκεκριμένη πτήση ορίζεται μια ομάδα πληρώματος. Για κάθε "),
                TextSegment(
                    text="ανάθεση",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ N:M",
                    badge_class="badge-rel",
                    tooltip="Συσχετιστική Οντότητα / N:M (Πλήρωμα <-> Στιγμιότυπο Πτήσης).",
                ),
                TextSegment(text=" καταγράφεται ο "),
                TextSegment(
                    text="ρόλος του μέλους στη συγκεκριμένη πτήση",
                    is_highlight=True,
                    category="attr",
                    tag_label="ΓΝΩΡΙΣΜΑ ΣΧΕΣΗΣ",
                    badge_class="badge-attr-simple",
                    tooltip="Γνώρισμα Σχέσης: Ρόλος ανάθεσης στη συγκεκριμένη πτήση.",
                ),
                TextSegment(text=". Επιπλέον, κάθε κυβερνήτης μπορεί να "),
                TextSegment(
                    text="επιβλέπει εκπαιδευτικά",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΑΝΑΔΡΟΜΙΚΗ 1:N",
                    badge_class="badge-rel",
                    tooltip="Αναδρομική Σχέση 1:N (Κυβερνήτης-Εκπαιδευτής -> Συγκυβερνήτης-Εκπαιδευόμενος).",
                ),
                TextSegment(text=" άλλους νέους συγκυβερνήτες στα πλαίσια του ετήσιου προγράμματος εκπαίδευσης."),
            ],
            accent_border_color="border-cyan-500",
        ),
        Paragraph(
            segments=[
                TextSegment(text="6. <strong>Επιβάτες & Κρατήσεις Εισιτηρίων (Passengers & Bookings):</strong> Για κάθε επιβάτη καταγράφονται: ο "),
                TextSegment(
                    text="μοναδικός αριθμός διαβατηρίου",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Μοναδικός αριθμός διεθνούς διαβατηρίου επιβάτη.",
                ),
                TextSegment(text=", "),
                TextSegment(text="ονοματεπώνυμο", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="εθνικότητα", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(
                    text="email",
                    is_highlight=True,
                    category="key",
                    tag_label="CANDIDATE KEY",
                    badge_class="badge-key-candidate",
                    tooltip="Υποψήφιο Κλειδί (Candidate Key): Μοναδική διεύθυνση ηλεκτρονικού ταχυδρομείου.",
                ),
                TextSegment(text=" και "),
                TextSegment(text="τηλέφωνο", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=". Ένας επιβάτης μπορεί να εκδώσει "),
                TextSegment(
                    text="ηλεκτρονικά εισιτήρια (κρατήσεις)",
                    is_highlight=True,
                    category="rel",
                    tag_label="ΣΧΕΣΗ N:M",
                    badge_class="badge-rel",
                    tooltip="Οντότητα Κράτησης / N:M (Επιβάτης <-> Στιγμιότυπο Πτήσης).",
                ),
                TextSegment(text=" για συγκεκριμένες πτήσεις. Κάθε κράτηση εισιτηρίου έχει έναν "),
                TextSegment(
                    text="μοναδικό εξαψήφιο αλφαριθμητικό κωδικό κράτησης (PNR)",
                    is_highlight=True,
                    category="key",
                    tag_label="PK",
                    badge_class="badge-key-pk",
                    tooltip="Πρωτεύον Κλειδί (Primary Key): Passenger Name Record 6 αλφαριθμητικών χαρακτήρων.",
                ),
                TextSegment(text=", "),
                TextSegment(text="αριθμό θέσης (Seat Number)", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="κλάση (Economy, Business)", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=", "),
                TextSegment(text="τιμή εισιτηρίου", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text=" και "),
                TextSegment(text="επιτρεπόμενο βάρος αποσκευών", is_highlight=True, category="attr", tag_label="ΓΝΩΡΙΣΜΑ", badge_class="badge-attr-simple"),
                TextSegment(text="."),
            ],
            accent_border_color="border-rose-500",
        ),
    ]

    # 2. Entities & Attributes
    entities = [
        Entity(
            name="ΑΕΡΟΔΡΟΜΙΟ",
            entity_type="Ισχυρή Οντότητα (Strong Entity)",
            is_weak=False,
            justification="Διεθνής αερολιμένας με μοναδικό κωδικό αναγνώρισης IATA.",
            attributes=[
                Attribute(name="Κωδικός_IATA", attr_type="Απλό, Μονότιμο, Primary Key", is_pk=True),
                Attribute(name="Επίσημη_Ονομασία", attr_type="Απλό, Μονότιμο, Candidate Key", is_candidate=True),
                Attribute(name="Πόλη", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Χώρα", attr_type="Απλό, Μονότιμο"),
                Attribute(
                    name="Διάδρομοι_Προσγείωσης",
                    attr_type="Σύνθετο Πλειότιμο (Composite Multi-valued)",
                    components=["Όνομα_Διαδρόμου", "Μήκος_Μέτρα"],
                    notes="Εξάγεται στον πίνακα ΔΙΑΔΡΟΜΟΣ_ΑΕΡΟΔΡΟΜΙΟΥ",
                ),
            ],
        ),
        Entity(
            name="ΠΡΟΓΡΑΜΜΑΤΙΣΜΕΝΗ_ΠΤΗΣΗ",
            entity_type="Ισχυρή Οντότητα (Strong Entity)",
            is_weak=False,
            justification="Τακτικό προγραμματισμένο δρομολόγιο με μοναδικό αναγνωριστικό τον Αριθμό_Πτήσης.",
            attributes=[
                Attribute(name="Αριθμός_Πτήσης", attr_type="Απλό, Μονότιμο, Primary Key", is_pk=True),
                Attribute(name="Προγραμματισμένη_Ώρα_Αναχώρησης", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Προγραμματισμένη_Ώρα_Άφιξης", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Εκτιμώμενη_Διάρκεια_Λεπτά", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Απόσταση_Ναυτικά_Μίλια", attr_type="Απλό, Μονότιμο"),
            ],
        ),
        Entity(
            name="ΣΤΙΓΜΙΟΤΥΠΟ_ΠΤΗΣΗΣ",
            entity_type="Ασθενής Οντότητα (Weak Entity)",
            is_weak=True,
            owner_entity="ΠΡΟΓΡΑΜΜΑΤΙΣΜΕΝΗ_ΠΤΗΣΗ",
            justification="Πραγματική εκτέλεση πτήσης σε συγκεκριμένη ημερομηνία. Προσδιορίζεται συνδυαστικά με τον Αριθμό_Πτήσης.",
            attributes=[
                Attribute(name="Ημερομηνία_Πτήσης", attr_type="Απλό, Μερικό Κλειδί (Partial Key)", is_partial=True),
                Attribute(name="Πραγματική_Ώρα_Αναχώρησης", attr_type="Απλό, Μονότιμο (Nullable)"),
                Attribute(name="Πραγματική_Ώρα_Άφιξης", attr_type="Απλό, Μονότιμο (Nullable)"),
                Attribute(name="Κατάσταση_Πτήσης", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Διαθέσιμες_Θέσεις", attr_type="Απλό, Μονότιμο"),
            ],
        ),
        Entity(
            name="ΑΕΡΟΣΚΑΦΟΣ",
            entity_type="Ισχυρή Οντότητα (Strong Entity)",
            is_weak=False,
            justification="Φυσικό αεροσκάφος στόλου με μοναδικό εργοστασιακό αριθμό MSN και Tail Number.",
            attributes=[
                Attribute(name="Σειριακός_Αριθμός_MSN", attr_type="Απλό, Μονότιμο, Primary Key", is_pk=True),
                Attribute(name="Αριθμός_Νηολογίου_Tail_No", attr_type="Απλό, Μονότιμο, Candidate Key", is_candidate=True),
                Attribute(name="Μοντέλο", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Έτος_Κατασκευής", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Χωρητικότητα_Επιβατών", attr_type="Απλό, Μονότιμο"),
            ],
        ),
        Entity(
            name="ΠΛΗΡΩΜΑ",
            entity_type="Ισχυρή Οντότητα (Strong Entity)",
            is_weak=False,
            justification="Εργαζόμενος πτητικού ή θαλαμικού προσωπικού με μοναδικό Αριθμό Μητρώου Εργαζομένου (ΑΜΕ).",
            attributes=[
                Attribute(name="Αριθμός_Μητρώου_ΑΜΕ", attr_type="Απλό, Μονότιμο, Primary Key", is_pk=True),
                Attribute(name="Αριθμός_Ταυτότητας_ΑΔΤ", attr_type="Απλό, Μονότιμο, Candidate Key", is_candidate=True),
                Attribute(name="Ονοματεπώνυμο", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Τηλέφωνο", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Διεύθυνση", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Ημερ_Πρόσληψης", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Κύριος_Ρόλος", attr_type="Απλό, Μονότιμο"),
            ],
        ),
        Entity(
            name="ΕΠΙΒΑΤΗΣ",
            entity_type="Ισχυρή Οντότητα (Strong Entity)",
            is_weak=False,
            justification="Φυσικό πρόσωπο ταξιδιώτη με μοναδικό Αριθμό Διαβατηρίου.",
            attributes=[
                Attribute(name="Αριθμός_Διαβατηρίου", attr_type="Απλό, Μονότιμο, Primary Key", is_pk=True),
                Attribute(name="Ονοματεπώνυμο", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Εθνικότητα", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Email", attr_type="Απλό, Μονότιμο, Candidate Key", is_candidate=True),
                Attribute(name="Τηλέφωνο", attr_type="Απλό, Μονότιμο"),
            ],
        ),
        Entity(
            name="ΚΡΑΤΗΣΗ_ΕΙΣΙΤΗΡΙΟΥ",
            entity_type="Συσχετιστική Οντότητα (Associative Entity)",
            is_weak=False,
            justification="Έκδοση εισιτηρίου επιβάτη για συγκεκριμένο στιγμιότυπο πτήσης με μοναδικό κωδικό PNR.",
            attributes=[
                Attribute(name="Κωδικός_PNR", attr_type="Απλό, Μονότιμο, Primary Key", is_pk=True),
                Attribute(name="Αριθμός_Θέσης", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Κλάση_Θέσης", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Τιμή_Εισιτηρίου", attr_type="Απλό, Μονότιμο"),
                Attribute(name="Επιτρεπόμενο_Βάρος_Αποσκευών", attr_type="Απλό, Μονότιμο"),
            ],
        ),
    ]

    # 3. Relationship Attributes
    relationship_attributes = [
        RelationshipAttribute(
            name="Ρόλος_Στην_Πτήση",
            relationship_name="ΑΝΑΘΕΣΗ_ΠΛΗΡΩΜΑΤΟΣ (N:M)",
            justification="Περιγράφει τα καθήκοντα του μέλους πληρώματος στη συγκεκριμένη πτήση (π.χ. Κυβερνήτης, Συγκυβερνήτης).",
        ),
    ]

    # 4. Keys Analysis Table
    keys_analysis = [
        KeyAnalysisRow(
            entity_name="ΑΕΡΟΔΡΟΜΙΟ",
            key_count="2",
            key_types="Υποψήφια: {Κωδικός_IATA}, {Επίσημη_Ονομασία}",
            final_pk_selection="Κωδικός_IATA",
            justification="Διεθνής πρότυπος 3ψήφιος αλφαριθμητικός κωδικός.",
        ),
        KeyAnalysisRow(
            entity_name="ΠΡΟΓΡΑΜΜΑΤΙΣΜΕΝΗ_ΠΤΗΣΗ",
            key_count="1",
            key_types="Υποψήφιο: {Αριθμός_Πτήσης}",
            final_pk_selection="Αριθμός_Πτήσης",
            justification="Μοναδικός κωδικός δρομολογίου (π.χ. OA315).",
        ),
        KeyAnalysisRow(
            entity_name="ΣΤΙΓΜΙΟΤΥΠΟ_ΠΤΗΣΗΣ",
            key_count="0 (Ασθενής)",
            key_types="Μερικό Κλειδί: {Ημερομηνία_Πτήσης}",
            final_pk_selection="Σύνθετο PK: {Προγραμματισμένη_Πτήση.Αριθμός_Πτήσης, Ημερομηνία_Πτήσης}",
            justification="Ασθενής οντότητα εξαρτώμενη από το προγραμματισμένο δρομολόγιο.",
            is_weak=True,
        ),
        KeyAnalysisRow(
            entity_name="ΑΕΡΟΣΚΑΦΟΣ",
            key_count="2",
            key_types="Υποψήφια: {Σειριακός_Αριθμός_MSN}, {Αριθμός_Νηολογίου_Tail_No}",
            final_pk_selection="Σειριακός_Αριθμός_MSN",
            justification="Μοναδικός σειριακός αριθμός κατασκευαστή.",
        ),
        KeyAnalysisRow(
            entity_name="ΠΛΗΡΩΜΑ",
            key_count="2",
            key_types="Υποψήφια: {ΑΜΕ}, {ΑΔΤ}",
            final_pk_selection="ΑΜΕ",
            justification="Εσωτερικός αριθμός υπαλληλικού μητρώου αεροπορικής εταιρείας.",
        ),
        KeyAnalysisRow(
            entity_name="ΕΠΙΒΑΤΗΣ",
            key_count="2",
            key_types="Υποψήφια: {Αριθμός_Διαβατηρίου}, {Email}",
            final_pk_selection="Αριθμός_Διαβατηρίου",
            justification="Επίσημο διεθνές ταξιδιωτικό έγγραφο.",
        ),
        KeyAnalysisRow(
            entity_name="ΚΡΑΤΗΣΗ_ΕΙΣΙΤΗΡΙΟΥ",
            key_count="1",
            key_types="Υποψήφιο: {Κωδικός_PNR}",
            final_pk_selection="Κωδικός_PNR",
            justification="Μοναδικός 6ψήφιος κωδικός ηλεκτρονικής κράτησης (Passenger Name Record).",
        ),
    ]

    # 5. Relationships
    relationships = [
        Relationship(
            letter_id="α",
            name="ΑΕΡΟΔΡΟΜΙΟ_ΑΝΑΧΩΡΗΣΗΣ",
            connected_entities="Αεροδρόμιο <-> Προγραμματισμένη Πτήση",
            cardinality="1:N",
            participation="Ολική για Πτήση, Μερική για Αεροδρόμιο",
            relationship_type="Κανονική Σχέση",
            attributes=[],
            justification="Κάθε προγραμματισμένη πτήση αναχωρεί από 1 αεροδρόμιο προέλευσης.",
        ),
        Relationship(
            letter_id="β",
            name="ΑΕΡΟΔΡΟΜΙΟ_ΑΦΙΞΗΣ",
            connected_entities="Αεροδρόμιο <-> Προγραμματισμένη Πτήση",
            cardinality="1:N",
            participation="Ολική για Πτήση, Μερική για Αεροδρόμιο",
            relationship_type="Κανονική Σχέση",
            attributes=[],
            justification="Κάθε προγραμματισμένη πτήση καταλήγει σε 1 αεροδρόμιο προορισμού.",
        ),
        Relationship(
            letter_id="γ",
            name="ΕΚΤΕΛΕΣΗ_ΔΡΟΜΟΛΟΓΙΟΥ",
            connected_entities="Προγραμματισμένη Πτήση <-> Στιγμιότυπο Πτήσης",
            cardinality="1:N",
            participation="Ολική για Στιγμιότυπο, Μερική για Προγραμματισμένη",
            relationship_type="Ταυτοποιούσα Σχέση (Identifying)",
            attributes=[],
            justification="Συνδέει την ασθενή οντότητα Στιγμιότυπο Πτήσης με το προγραμματισμένο δρομολόγιο.",
        ),
        Relationship(
            letter_id="δ",
            name="ΕΚΤΕΛΕΙΤΑΙ_ΜΕ_ΣΚΑΦΟΣ",
            connected_entities="Αεροσκάφος <-> Στιγμιότυπο Πτήσης",
            cardinality="1:N",
            participation="Ολική για Στιγμιότυπο, Μερική για Αεροσκάφος",
            relationship_type="Κανονική Σχέση",
            attributes=[],
            justification="Κάθε συγκεκριμένη πτήση πραγματοποιείται από 1 φυσικό αεροσκάφος.",
        ),
        Relationship(
            letter_id="ε",
            name="ΕΚΠΑΙΔΕΥΕΙ_ΠΙΛΟΤΟΥΣ",
            connected_entities="Πλήρωμα (Κυβερνήτης) <-> Πλήρωμα (Συγκυβερνήτης)",
            cardinality="1:N",
            participation="Μερική και για τις δύο πλευρές",
            relationship_type="Αναδρομική Σχέση (Recursive)",
            attributes=[],
            justification="Ένας έμπειρος κυβερνήτης εκπαιδεύει νέους συγκυβερνήτες.",
        ),
        Relationship(
            letter_id="στ",
            name="ΑΝΑΘΕΣΗ_ΠΛΗΡΩΜΑΤΟΣ",
            connected_entities="Πλήρωμα <-> Στιγμιότυπο Πτήσης",
            cardinality="N:M",
            participation="Μερική και για τις δύο πλευρές",
            relationship_type="Συσχετιστική Οντότητα (Junction)",
            attributes=["Ρόλος_Στην_Πτήση"],
            justification="Σε κάθε πτήση ανατίθενται πολλά μέλη πληρώματος και κάθε μέλος εκτελεί πολλές πτήσεις.",
        ),
        Relationship(
            letter_id="ζ",
            name="ΚΡΑΤΗΣΗ_ΕΙΣΙΤΗΡΙΟΥ",
            connected_entities="Επιβάτης <-> Στιγμιότυπο Πτήσης",
            cardinality="N:M",
            participation="Μερική και για τις δύο πλευρές",
            relationship_type="Συσχετιστική Οντότητα / Booking",
            attributes=["Κωδικός_PNR", "Αριθμός_Θέσης", "Κλάση_Θέσης", "Τιμή_Εισιτηρίου", "Επιτρεπόμενο_Βάρος_Αποσκευών"],
            justification="Ένας επιβάτης κλείνει εισιτήρια για πολλές πτήσεις και μια πτήση μεταφέρει πολλούς επιβάτες.",
        ),
    ]

    # 6. Assumptions
    assumptions = [
        "Πλειότιμα Γνωρίσματα: Οι διάδρομοι προσγείωσης/απογείωσης αεροδρομίων υλοποιούνται στον πίνακα ΔΙΑΔΡΟΜΟΣ_ΑΕΡΟΔΡΟΜΙΟΥ με σύνθετο πρωτεύον κλειδί {iata_code, onoma_diadromou}.",
        "Στιγμιότυπο Πτήσης: Υλοποιείται ως ασθενής οντότητα με σύνθετο PK {Αριθμός_Πτήσης, Ημερομηνία_Πτήσης} και εξάρτηση ταυτοποίησης από το δρομολόγιο.",
        "Κράτηση Εισιτηρίου: Διαθέτει μοναδικό κωδικό PNR ως πρωτεύον κλειδί, με Foreign Keys προς τον Επιβάτη και το συγκεκριμένο Στιγμιότυπο Πτήσης.",
        "Ανάθεση Πληρώματος: Συνδέει μέλη πληρώματος με συγκεκριμένα στιγμιότυπα πτήσεων (N:M), καταγράφοντας τον ειδικό ρόλο ανάθεσης στη συγκεκριμένη πτήση.",
        "Εκπαίδευση Πιλότων: Υλοποιείται ως αναδρομική συσχέτιση 1:N (Self-Referencing) στον πίνακα ΠΛΗΡΩΜΑ μέσω του προαιρετικού γνωρίσματος mentor_ame.",
        "Αεροδρόμια Αναχώρησης & Άφιξης: Κάθε προγραμματισμένη πτήση συνδέει υποχρεωτικά δύο διακριτά αεροδρόμια (departure_iata != arrival_iata).",
    ]

    # 7. ER Table Nodes for SVG Crow's Foot Diagram
    er_tables = [
        ERTable(
            id="aerodromio",
            label="ΑΕΡΟΔΡΟΜΙΟ",
            x=50,
            y=80,
            attrs=[
                ERTableAttr(name="Κωδικός_IATA", pk=True),
                ERTableAttr(name="Επίσημη_Ονομασία"),
                ERTableAttr(name="Πόλη"),
                ERTableAttr(name="Χώρα"),
            ],
        ),
        ERTable(
            id="diadromos",
            label="ΔΙΑΔΡΟΜΟΣ_ΑΕΡΟΔΡΟΜΙΟΥ",
            x=50,
            y=300,
            attrs=[
                ERTableAttr(name="Κωδικός_IATA", pk=True, fk=True),
                ERTableAttr(name="Όνομα_Διαδρόμου", pk=True),
                ERTableAttr(name="Μήκος_Μέτρα"),
            ],
        ),
        ERTable(
            id="programmatismeni",
            label="ΠΡΟΓΡΑΜΜΑΤΙΣΜΕΝΗ_ΠΤΗΣΗ",
            x=450,
            y=50,
            attrs=[
                ERTableAttr(name="Αριθμός_Πτήσης", pk=True),
                ERTableAttr(name="Αεροδρόμιο_Αναχώρησης", fk=True),
                ERTableAttr(name="Αεροδρόμιο_Άφιξης", fk=True),
                ERTableAttr(name="Ώρα_Αναχώρησης"),
                ERTableAttr(name="Ώρα_Άφιξης"),
                ERTableAttr(name="Διάρκεια_Λεπτά"),
                ERTableAttr(name="Απόσταση_NM"),
            ],
        ),
        ERTable(
            id="stigmiotypo",
            label="ΣΤΙΓΜΙΟΤΥΠΟ_ΠΤΗΣΗΣ",
            x=450,
            y=380,
            attrs=[
                ERTableAttr(name="Αριθμός_Πτήσης", pk=True, fk=True),
                ERTableAttr(name="Ημερομηνία_Πτήσης", pk=True),
                ERTableAttr(name="Σειριακός_Αριθμός_MSN", fk=True),
                ERTableAttr(name="Πραγμ_Ώρα_Αναχώρησης"),
                ERTableAttr(name="Πραγμ_Ώρα_Άφιξης"),
                ERTableAttr(name="Κατάσταση_Πτήσης"),
                ERTableAttr(name="Διαθέσιμες_Θέσεις"),
            ],
        ),
        ERTable(
            id="aeroskafos",
            label="ΑΕΡΟΣΚΑΦΟΣ",
            x=50,
            y=480,
            attrs=[
                ERTableAttr(name="Σειριακός_Αριθμός_MSN", pk=True),
                ERTableAttr(name="Αριθμός_Νηολογίου"),
                ERTableAttr(name="Μοντέλο"),
                ERTableAttr(name="Έτος_Κατασκευής"),
                ERTableAttr(name="Χωρητικότητα"),
            ],
        ),
        ERTable(
            id="pliroma",
            label="ΠΛΗΡΩΜΑ",
            x=850,
            y=50,
            attrs=[
                ERTableAttr(name="Αριθμός_Μητρώου_ΑΜΕ", pk=True),
                ERTableAttr(name="ΑΔΤ"),
                ERTableAttr(name="Ονοματεπώνυμο"),
                ERTableAttr(name="Τηλέφωνο"),
                ERTableAttr(name="Διεύθυνση"),
                ERTableAttr(name="Ημερ_Πρόσληψης"),
                ERTableAttr(name="Κύριος_Ρόλος"),
                ERTableAttr(name="Μέντορας_ΑΜΕ", fk=True),
            ],
        ),
        ERTable(
            id="anathesi",
            label="ΑΝΑΘΕΣΗ_ΠΛΗΡΩΜΑΤΟΣ",
            x=850,
            y=380,
            attrs=[
                ERTableAttr(name="Αριθμός_Πτήσης", pk=True, fk=True),
                ERTableAttr(name="Ημερομηνία_Πτήσης", pk=True, fk=True),
                ERTableAttr(name="Αριθμός_Μητρώου_ΑΜΕ", pk=True, fk=True),
                ERTableAttr(name="Ρόλος_Στην_Πτήση"),
            ],
        ),
        ERTable(
            id="epivatis",
            label="ΕΠΙΒΑΤΗΣ",
            x=50,
            y=700,
            attrs=[
                ERTableAttr(name="Αριθμός_Διαβατηρίου", pk=True),
                ERTableAttr(name="Ονοματεπώνυμο"),
                ERTableAttr(name="Εθνικότητα"),
                ERTableAttr(name="Email"),
                ERTableAttr(name="Τηλέφωνο"),
            ],
        ),
        ERTable(
            id="kratisi",
            label="ΚΡΑΤΗΣΗ_ΕΙΣΙΤΗΡΙΟΥ",
            x=450,
            y=700,
            attrs=[
                ERTableAttr(name="Κωδικός_PNR", pk=True),
                ERTableAttr(name="Αριθμός_Πτήσης", fk=True),
                ERTableAttr(name="Ημερομηνία_Πτήσης", fk=True),
                ERTableAttr(name="Αριθμός_Διαβατηρίου", fk=True),
                ERTableAttr(name="Αριθμός_Θέσης"),
                ERTableAttr(name="Κλάση_Θέσης"),
                ERTableAttr(name="Τιμή_Ευρώ"),
                ERTableAttr(name="Βάρος_Αποσκευών_KG"),
            ],
        ),
    ]

    # 8. ER Diagram Edges
    er_edges = [
        EREdge(
            path="M 310,100 L 450,80",
            marker_start="start-one-mandatory",
            marker_end="end-many-mandatory",
            label="Αναχώρηση (1:N)",
            lx=380,
            ly=75,
        ),
        EREdge(
            path="M 310,140 L 450,120",
            marker_start="start-one-mandatory",
            marker_end="end-many-mandatory",
            label="Άφιξη (1:N)",
            lx=380,
            ly=135,
        ),
        EREdge(
            path="M 180,240 L 180,300",
            marker_start="start-one-mandatory",
            marker_end="end-many-mandatory",
            label="Διάδρομοι (1:N)",
            lx=180,
            ly=270,
        ),
        EREdge(
            path="M 580,294 L 580,380",
            marker_start="start-one-mandatory",
            marker_end="end-many-mandatory",
            label="Εκτέλεση (1:N)",
            lx=580,
            ly=337,
        ),
        EREdge(
            path="M 310,540 L 450,480",
            marker_start="start-one-mandatory",
            marker_end="end-many-mandatory",
            label="Σκάφος (1:N)",
            lx=380,
            ly=510,
        ),
        EREdge(
            path="M 980,322 L 980,380",
            marker_start="start-one-mandatory",
            marker_end="end-many-mandatory",
            label="Ανάθεση (1:N)",
            lx=980,
            ly=351,
        ),
        EREdge(
            path="M 710,480 L 850,480",
            marker_start="start-one-mandatory",
            marker_end="end-many-mandatory",
            label="Πτήση-Πλήρωμα (1:N)",
            lx=780,
            ly=465,
        ),
        EREdge(
            path="M 310,750 L 450,750",
            marker_start="start-one-mandatory",
            marker_end="end-many-mandatory",
            label="Κράτηση Επιβάτη (1:N)",
            lx=380,
            ly=735,
        ),
        EREdge(
            path="M 580,624 L 580,700",
            marker_start="start-one-mandatory",
            marker_end="end-many-mandatory",
            label="Κράτηση Πτήσης (1:N)",
            lx=580,
            ly=662,
        ),
        # Pilot Mentor recursive relationship (1:N)
        EREdge(
            path="M 1110,100 C 1180,40 1180,200 1110,160",
            marker_start="start-one-optional",
            marker_end="end-many-optional",
            label="Μέντορας (1:N)",
            lx=1185,
            ly=120,
        ),
    ]

    # 9. Relational Justifications
    relational_justifications = [
        RelationalJustification(
            title="1. Διπλή Συσχέτιση Αεροδρομίου - Πτήσης:",
            color_class="text-blue-400",
            description="Η ΠΡΟΓΡΑΜΜΑΤΙΣΜΕΝΗ_ΠΤΗΣΗ περιλαμβάνει δύο ξεχωριστά Foreign Keys προς τον πίνακα ΑΕΡΟΔΡΟΜΙΟ (departure_iata και arrival_iata) για τον προσδιορισμό αεροδρομίου αναχώρησης και προορισμού.",
        ),
        RelationalJustification(
            title="2. Ασθενής Οντότητα Στιγμιοτύπων Πτήσεων:",
            color_class="text-purple-400",
            description="Το ΣΤΙΓΜΙΟΤΥΠΟ_ΠΤΗΣΗΣ έχει σύνθετο PK {flight_number, flight_date} και εξαρτάται υπαρκτικά και ταυτοποιητικά από το προγραμματισμένο δρομολόγιο (ON DELETE CASCADE).",
        ),
        RelationalJustification(
            title="3. Συσχετιστική Οντότητα Κρατήσεων:",
            color_class="text-emerald-400",
            description="Ο πίνακας ΚΡΑΤΗΣΗ_ΕΙΣΙΤΗΡΙΟΥ έχει αυτόνομο PK το PNR και Foreign Keys προς τον Επιβάτη (passport_number) και το Στιγμιότυπο Πτήσης (flight_number, flight_date).",
        ),
        RelationalJustification(
            title="4. Πλειότιμα Γνωρίσματα (1NF):",
            color_class="text-amber-400",
            description="Οι διάδρομοι προσγείωσης διασπώνται στον πίνακα ΔΙΑΔΡΟΜΟΣ_ΑΕΡΟΔΡΟΜΙΟΥ με σύνθετο PK {iata_code, onoma_diadromou} και FK προς το αεροδρόμιο.",
        ),
        RelationalJustification(
            title="5. Αναδρομική Σχέση Εκπαίδευσης Πιλότων (1:N):",
            color_class="text-cyan-400",
            description="Στον πίνακα ΠΛΗΡΩΜΑ εισάγεται το προαιρετικό Foreign Key mentor_ame που αναφέρεται στο πρωτεύον κλειδί ame του ίδιου πίνακα (Self-Referencing FK).",
        ),
        RelationalJustification(
            title="6. Συσχετιστικός Πίνακας Ανάθεσης Πληρωμάτων (N:M):",
            color_class="text-rose-400",
            description="Η σχέση N:M υλοποιείται στον πίνακα ANATHESI_PLIROMATOS με σύνθετο PK {flight_number, flight_date, ame} και το περιγραφικό γνώρισμα rolos_ptisis.",
        ),
    ]

    # 10. SQL DDL Script
    sql_ddl = """-- SQL DDL Schema: Airline Operations & Bookings Database
-- 1. Entity: AERODROMIO
CREATE TABLE AERODROMIO (
    iata_code VARCHAR(3) PRIMARY KEY,
    onoma_aerodromiou VARCHAR(100) NOT NULL UNIQUE,
    poli VARCHAR(50) NOT NULL,
    chora VARCHAR(50) NOT NULL
);

-- 2. Multivalued Attribute: DIADROMOS_AERODROMIOU
CREATE TABLE DIADROMOS_AERODROMIOU (
    iata_code VARCHAR(3) NOT NULL,
    onoma_diadromou VARCHAR(20) NOT NULL,
    mikos_metra INT NOT NULL,
    PRIMARY KEY (iata_code, onoma_diadromou),
    FOREIGN KEY (iata_code) REFERENCES AERODROMIO(iata_code) ON DELETE CASCADE
);

-- 3. Entity: PROGRAMMATISMENI_PTISI
CREATE TABLE PROGRAMMATISMENI_PTISI (
    flight_number VARCHAR(10) PRIMARY KEY,
    departure_iata VARCHAR(3) NOT NULL,
    arrival_iata VARCHAR(3) NOT NULL,
    scheduled_dept_time TIME NOT NULL,
    scheduled_arr_time TIME NOT NULL,
    duration_minutes INT NOT NULL,
    distance_nm DECIMAL(8, 2) NOT NULL,
    FOREIGN KEY (departure_iata) REFERENCES AERODROMIO(iata_code),
    FOREIGN KEY (arrival_iata) REFERENCES AERODROMIO(iata_code)
);

-- 4. Entity: AEROSKAFOS
CREATE TABLE AEROSKAFOS (
    msn VARCHAR(20) PRIMARY KEY,
    tail_number VARCHAR(15) NOT NULL UNIQUE,
    montelo VARCHAR(50) NOT NULL,
    etos_kataskevis INT NOT NULL,
    choritikotita INT NOT NULL
);

-- 5. Weak Entity: STIGMIOTYPO_PTISIS
CREATE TABLE STIGMIOTYPO_PTISIS (
    flight_number VARCHAR(10) NOT NULL,
    flight_date DATE NOT NULL,
    msn VARCHAR(20) NOT NULL,
    actual_dept_time TIMESTAMP,
    actual_arr_time TIMESTAMP,
    katastasi_ptisis VARCHAR(30) NOT NULL CHECK (katastasi_ptisis IN ('On Time', 'Delayed', 'Cancelled', 'Landed', 'Boarding')),
    diathesimes_theseis INT NOT NULL,
    PRIMARY KEY (flight_number, flight_date),
    FOREIGN KEY (flight_number) REFERENCES PROGRAMMATISMENI_PTISI(flight_number) ON DELETE CASCADE,
    FOREIGN KEY (msn) REFERENCES AEROSKAFOS(msn)
);

-- 6. Entity: PLIROMA
CREATE TABLE PLIROMA (
    ame VARCHAR(15) PRIMARY KEY,
    adt VARCHAR(15) NOT NULL UNIQUE,
    onomateponymo VARCHAR(100) NOT NULL,
    tilefono VARCHAR(20) NOT NULL,
    diefthynsi VARCHAR(100) NOT NULL,
    hmer_proslipsis DATE NOT NULL,
    kyrios_rolos VARCHAR(50) NOT NULL,
    mentor_ame VARCHAR(15),
    FOREIGN KEY (mentor_ame) REFERENCES PLIROMA(ame)
);

-- 7. Associative Entity / Junction: ANATHESI_PLIROMATOS
CREATE TABLE ANATHESI_PLIROMATOS (
    flight_number VARCHAR(10) NOT NULL,
    flight_date DATE NOT NULL,
    ame VARCHAR(15) NOT NULL,
    rolos_ptisis VARCHAR(50) NOT NULL,
    PRIMARY KEY (flight_number, flight_date, ame),
    FOREIGN KEY (flight_number, flight_date) REFERENCES STIGMIOTYPO_PTISIS(flight_number, flight_date) ON DELETE CASCADE,
    FOREIGN KEY (ame) REFERENCES PLIROMA(ame) ON DELETE CASCADE
);

-- 8. Entity: EPIVATIS
CREATE TABLE EPIVATIS (
    passport_number VARCHAR(20) PRIMARY KEY,
    onomateponymo VARCHAR(100) NOT NULL,
    ethnikotita VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    tilefono VARCHAR(20) NOT NULL
);

-- 9. Associative Entity / Booking: KRATISI_EISITIRIOU
CREATE TABLE KRATISI_EISITIRIOU (
    pnr VARCHAR(6) PRIMARY KEY,
    flight_number VARCHAR(10) NOT NULL,
    flight_date DATE NOT NULL,
    passport_number VARCHAR(20) NOT NULL,
    seat_number VARCHAR(10) NOT NULL,
    klasi_thesis VARCHAR(20) NOT NULL CHECK (klasi_thesis IN ('Economy', 'Premium Economy', 'Business', 'First')),
    timi_evro DECIMAL(8, 2) NOT NULL,
    varos_aposkevon_kg DECIMAL(5, 2) NOT NULL,
    FOREIGN KEY (flight_number, flight_date) REFERENCES STIGMIOTYPO_PTISIS(flight_number, flight_date) ON DELETE CASCADE,
    FOREIGN KEY (passport_number) REFERENCES EPIVATIS(passport_number) ON DELETE CASCADE
);"""

    return Scenario(
        id="airline_management",
        title="Σύστημα Διαχείρισης Αεροπορικής Εταιρείας & Πτήσεων",
        subtitle="Μοντελοποίηση Αεροδρομίων, Δρομολογίων, Στιγμιοτύπων Πτήσεων, Αεροσκαφών, Πληρωμάτων & Κρατήσεων",
        course_tag="Βάσεις Δεδομένων (Πρόοδος 2025-2026 - Θέμα 3)",
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
