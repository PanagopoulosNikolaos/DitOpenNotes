"""Comprehensive Theory and Methodology Guide component for Database ER Modeling.

Compiles step-by-step text analysis methodologies, general recognition tables,
complete Crow's Foot notation symbolism (0:1, 1:1, 1:N, N:M, 0:M, 1:M, etc.),
weak entity patterns, recursive relations, ternary relationships, and relational mapping rules.
"""

from nicegui import ui
from .methodology_card import renderMethodologyCards
from .methodology_table import renderMethodologyTable


def renderTheoryPage() -> None:
    """Renders the comprehensive ER theory, methodology, and Crow's Foot notation handbook."""
    with ui.column().classes("w-full max-w-6xl mx-auto px-4 py-8 space-y-10 print-section"):
        # Page Hero / Banner
        with ui.column().classes(
            "w-full glass-panel p-6 md:p-8 rounded-2xl border border-[rgba(224,107,58,0.35)] gap-4"
        ):
            with ui.row().classes("items-center gap-3"):
                ui.html('<i class="fa-solid fa-book-open-reader text-[#e06b3a] text-2xl md:text-3xl"></i>')
                with ui.column().classes("gap-0"):
                    ui.html(
                        '<h1 class="text-2xl md:text-3xl font-black gradient-title m-0">'
                        "Πλήρης Θεωρητικός Οδηγός & Μεθοδολογία Σχεδίασης ER"
                        "</h1>"
                    )
                    ui.label(
                        "Ολοκληρωμένο εγχειρίδιο ανάλυσης απαιτήσεων, αναγνώρισης οντοτήτων/σχέσεων, "
                        "συμβολισμών Crow's Foot και κανόνων μετατροπής σε σχεσιακό σχήμα."
                    ).classes("text-sm text-[#b5b0a4] mt-1")

            with ui.row().classes("gap-3 flex-wrap text-xs"):
                with ui.row().classes(
                    "items-center gap-1.5 px-3 py-1.5 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.08)] text-[#f4f1ea]"
                ):
                    ui.html('<i class="fa-solid fa-layer-group text-blue-400"></i>')
                    ui.label("4 Βασικά Στάδια Ανάλυσης")

                with ui.row().classes(
                    "items-center gap-1.5 px-3 py-1.5 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.08)] text-[#f4f1ea]"
                ):
                    ui.html('<i class="fa-solid fa-table text-emerald-400"></i>')
                    ui.label("Πίνακας Αναγνώρισης")

                with ui.row().classes(
                    "items-center gap-1.5 px-3 py-1.5 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.08)] text-[#f4f1ea]"
                ):
                    ui.html('<i class="fa-solid fa-code-branch text-[#e06b3a]"></i>')
                    ui.label("Συμβολισμοί Crow's Foot")

                with ui.row().classes(
                    "items-center gap-1.5 px-3 py-1.5 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.08)] text-[#f4f1ea]"
                ):
                    ui.html('<i class="fa-solid fa-database text-amber-400"></i>')
                    ui.label("7 Κανόνες Μετατροπής σε SQL")

        # SECTION 1: Step-by-Step Methodology Cards
        with ui.column().classes("w-full gap-4"):
            renderMethodologyCards()

            # Deep-dive analysis tips for each step
            with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
                with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                    ui.html('<i class="fa-solid fa-lightbulb text-[#f59e0b] text-lg"></i>')
                    ui.html('<h3 class="text-lg font-bold text-[#f4f1ea] m-0">Πρακτικές Οδηγίες & Παγίδες κατά την Ανάλυση</h3>')

                with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs leading-relaxed"):
                    # Card 1: Entities vs Attributes
                    with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-2"):
                        with ui.row().classes("items-center gap-2"):
                            ui.html('<i class="fa-solid fa-scale-balanced text-blue-400"></i>')
                            ui.label("Οντότητα ή Γνώρισμα;").classes("font-bold text-blue-300")
                        ui.label(
                            "Κανόνας: Εάν μια έννοια έχει δικά της χαρακτηριστικά (π.χ. ένα Τμήμα έχει όνομα, τηλέφωνο, διεύθυνση), "
                            "τότε είναι ΟΝΤΟΤΗΤΑ. Εάν είναι μια απλή τιμή χωρίς επιπλέον ιδιότητες (π.χ. ηλικία, κατάσταση), είναι ΓΝΩΡΙΣΜΑ."
                        ).classes("text-[#b5b0a4]")

                    # Card 2: Relationship Direction
                    with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-2"):
                        with ui.row().classes("items-center gap-2"):
                            ui.html('<i class="fa-solid fa-arrows-left-right text-rose-400"></i>')
                            ui.label("Αμφίδρομη Διερεύνηση Πληθικότητας").classes("font-bold text-rose-300")
                        ui.label(
                            "Κανόνας: Για να βρούμε τον λόγο πληθικότητας θέτουμε ΠΑΝΤΑ δύο ερωτήματα:\n"
                            "1) Για 1 στιγμιότυπο του Α, πόσα Β μπορούν να συνδεθούν; (min, max)\n"
                            "2) Για 1 στιγμιότυπο του Β, πόσα Α μπορούν να συνδεθούν; (min, max)"
                        ).classes("text-[#b5b0a4]")

                    # Card 3: Relationship Attributes
                    with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-2"):
                        with ui.row().classes("items-center gap-2"):
                            ui.html('<i class="fa-solid fa-link text-emerald-400"></i>')
                            ui.label("Γνωρίσματα σε Συσχέτιση (Relationship Attributes)").classes("font-bold text-emerald-300")
                        ui.label(
                            "Κανόνας: Όταν μια πληροφορία προκύπτει ΜΟΝΟ από τον συνδυασμό δύο οντοτήτων "
                            "(π.χ. ο βαθμός ενός Φοιτητή σε ένα Μάθημα, ή οι ώρες απασχόλησης ενός Υπαλλήλου σε ένα Έργο), "
                            "το γνώρισμα τοποθετείται πάνω στη ΣΧΕΣΗ και όχι σε μεμονωμένη οντότητα."
                        ).classes("text-[#b5b0a4]")

                    # Card 4: Weak Entities & Partial Keys
                    with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-2"):
                        with ui.row().classes("items-center gap-2"):
                            ui.html('<i class="fa-solid fa-fingerprint text-amber-400"></i>')
                            ui.label("Ασθενείς Οντότητες & Μερικά Κλειδιά").classes("font-bold text-amber-300")
                        ui.label(
                            "Κανόνας: Μια οντότητα είναι ασθενής (Weak Entity) όταν δεν διαθέτει δικό της μοναδικό αναγνωριστικό "
                            "και εξαρτάται υπαρκτικά από μια ισχυρή οντότητα (Owner). Το κλειδί της σχηματίζεται συνδυάζοντας "
                            "το PK του Owner με το Μερικό Κλειδί (Partial Key / Discriminator) της ίδιας."
                        ).classes("text-[#b5b0a4]")

        # SECTION 2: General Methodology Table
        renderMethodologyTable()

        # SECTION 3: Crow's Foot Notation Complete Symbolism Guide
        _renderCrowsFootSection()

        # SECTION 4: Relational Mapping Rules (7 Golden Rules)
        _renderRelationalMappingRules()

        # SECTION 5: Notation Comparison Table (Crow's Foot vs Chen vs Min-Max vs UML)
        _renderNotationComparisonSection()


def _renderCrowsFootSection() -> None:
    """Renders the comprehensive Crow's Foot symbolism guide with SVGs and connection types."""
    with ui.column().classes("w-full glass-panel p-6 md:p-8 rounded-2xl gap-8"):
        # Section Title
        with ui.row().classes("items-center gap-3 border-b border-[rgba(255,255,255,0.08)] pb-4"):
            ui.html('<i class="fa-solid fa-bezier-curve text-[#e06b3a] text-2xl"></i>')
            with ui.column().classes("gap-0"):
                ui.html(
                    '<h2 class="text-xl md:text-2xl font-bold text-[#f4f1ea] m-0">'
                    "Συμβολισμοί Crow's Foot (Οδηγός Ακροδεκτών & Συσχετίσεων)"
                    "</h2>"
                )
                ui.label(
                    "Ανάλυση όλων των πιθανών συμβόλων στα άκρα των σχέσεων, ερμηνεία Modality / Cardinality "
                    "και πλήρης κατάλογος συνδυασμών (0:1, 1:1, 1:N, 0:M, 1:M, N:M)."
                ).classes("text-xs text-[#b5b0a4] mt-1")

        # Anatomy of Crow's Foot Endpoint
        with ui.column().classes("w-full p-5 rounded-xl bg-[#171615] border border-[rgba(224,107,58,0.25)] gap-3"):
            with ui.row().classes("items-center gap-2"):
                ui.html('<i class="fa-solid fa-circle-info text-[#e06b3a]"></i>')
                ui.html('<h3 class="text-base font-bold text-[#f4f1ea] m-0">Ανατομία ενός Άκρου Crow\'s Foot (Διπλό Σύμβολο)</h3>')
            ui.label(
                "Στο μοντέλο Crow's Foot, κάθε άκρο σύνδεσης περιλαμβάνει δύο διακριτά σύμβολα που διαβάζονται από μέσα προς τα έξω:"
            ).classes("text-xs text-[#b5b0a4]")

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full mt-2"):
                with ui.column().classes("p-4 rounded-lg bg-[#201f1d] border-l-4 border-amber-500 gap-1"):
                    ui.label("1. Εσωτερικό Σύμβολο = Modality (Ελάχιστη Συμμετοχή / Minimum)").classes(
                        "font-bold text-amber-300 text-xs"
                    )
                    ui.label(
                        "• Κύκλος (O): Ελάχιστο = 0 (Προαιρετική Συμμετοχή / Optional)\n"
                        "• Κάθετη Γραμμή (|): Ελάχιστο = 1 (Υποχρεωτική Συμμετοχή / Mandatory)"
                    ).classes("text-xs text-[#b5b0a4] leading-relaxed")

                with ui.column().classes("p-4 rounded-lg bg-[#201f1d] border-l-4 border-[#e06b3a] gap-1"):
                    ui.label("2. Εξωτερικό Σύμβολο = Cardinality (Μέγιστη Πληθικότητα / Maximum)").classes(
                        "font-bold text-[#fdba74] text-xs"
                    )
                    ui.label(
                        "• Κάθετη Γραμμή (|): Μέγιστο = 1 (Ένα στιγμιότυπο / One)\n"
                        "• Διχάλα / Πόδι Κόρακα (<): Μέγιστο = N ή M (Πολλά στιγμιότυπα / Many)"
                    ).classes("text-xs text-[#b5b0a4] leading-relaxed")

        # 4 Fundamental Endpoints Cards with SVGs
        with ui.column().classes("w-full gap-4"):
            ui.html('<h3 class="text-lg font-bold text-[#f4f1ea] m-0">Τα 4 Βασικά Άκρα Crow\'s Foot (Endpoints)</h3>')

            with ui.grid().classes("grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 w-full"):
                # Endpoint 1: Zero or One (0..1)
                _renderEndpointCard(
                    title="0..1 (Zero or One)",
                    greek_name="Μηδέν ή Ένα (Προαιρετικό 1)",
                    modality="0 (Προαιρετικό)",
                    cardinality="1 (Μοναδικό)",
                    svg_markup="""
                    <svg viewBox="0 0 160 70" class="w-full h-16">
                        <!-- Line -->
                        <line x1="10" y1="35" x2="130" y2="35" stroke="#e06b3a" stroke-width="2.5" />
                        <!-- Circle (Modality 0) -->
                        <circle cx="100" cy="35" r="7" fill="#1c1b1a" stroke="#e06b3a" stroke-width="2.5" />
                        <!-- Perpendicular Bar (Cardinality 1) -->
                        <line x1="120" y1="20" x2="120" y2="50" stroke="#e06b3a" stroke-width="2.5" />
                        <!-- Target Entity Edge -->
                        <line x1="130" y1="10" x2="130" y2="60" stroke="#b5b0a4" stroke-width="3" />
                    </svg>
                    """,
                    example="Ένας υπάλληλος μπορεί να διαχειρίζεται το πολύ 1 τμήμα ή κανένα.",
                    color_class="border-slate-500",
                )

                # Endpoint 2: Exactly One (1..1)
                _renderEndpointCard(
                    title="1..1 (Exactly One)",
                    greek_name="Ακριβώς Ένα (Υποχρεωτικό 1)",
                    modality="1 (Υποχρεωτικό)",
                    cardinality="1 (Μοναδικό)",
                    svg_markup="""
                    <svg viewBox="0 0 160 70" class="w-full h-16">
                        <!-- Line -->
                        <line x1="10" y1="35" x2="130" y2="35" stroke="#e06b3a" stroke-width="2.5" />
                        <!-- First Bar (Modality 1) -->
                        <line x1="100" y1="20" x2="100" y2="50" stroke="#e06b3a" stroke-width="2.5" />
                        <!-- Second Bar (Cardinality 1) -->
                        <line x1="120" y1="20" x2="120" y2="50" stroke="#e06b3a" stroke-width="2.5" />
                        <!-- Target Entity Edge -->
                        <line x1="130" y1="10" x2="130" y2="60" stroke="#b5b0a4" stroke-width="3" />
                    </svg>
                    """,
                    example="Κάθε τμήμα ανήκει υποχρεωτικά σε ακριβώς 1 σχολή/εταιρεία.",
                    color_class="border-emerald-500",
                )

                # Endpoint 3: Zero or Many (0..N / 0..M)
                _renderEndpointCard(
                    title="0..N / 0..M (Zero or Many)",
                    greek_name="Μηδέν ή Πολλά (Προαιρετικά Πολλά)",
                    modality="0 (Προαιρετικό)",
                    cardinality="N (Πολλά)",
                    svg_markup="""
                    <svg viewBox="0 0 160 70" class="w-full h-16">
                        <!-- Line -->
                        <line x1="10" y1="35" x2="130" y2="35" stroke="#e06b3a" stroke-width="2.5" />
                        <!-- Circle (Modality 0) -->
                        <circle cx="85" cy="35" r="7" fill="#1c1b1a" stroke="#e06b3a" stroke-width="2.5" />
                        <!-- Crow's Foot Fork (Cardinality N) -->
                        <line x1="105" y1="35" x2="130" y2="18" stroke="#e06b3a" stroke-width="2.5" />
                        <line x1="105" y1="35" x2="130" y2="52" stroke="#e06b3a" stroke-width="2.5" />
                        <!-- Target Entity Edge -->
                        <line x1="130" y1="10" x2="130" y2="60" stroke="#b5b0a4" stroke-width="3" />
                    </svg>
                    """,
                    example="Ένας συγγραφέας μπορεί να έχει γράψει από 0 έως πολλά βιβλία.",
                    color_class="border-blue-500",
                )

                # Endpoint 4: One or Many (1..N / 1..M)
                _renderEndpointCard(
                    title="1..N / 1..M (One or Many)",
                    greek_name="Ένα ή Πολλά (Υποχρεωτικά Πολλά)",
                    modality="1 (Υποχρεωτικό)",
                    cardinality="N (Πολλά)",
                    svg_markup="""
                    <svg viewBox="0 0 160 70" class="w-full h-16">
                        <!-- Line -->
                        <line x1="10" y1="35" x2="130" y2="35" stroke="#e06b3a" stroke-width="2.5" />
                        <!-- Bar (Modality 1) -->
                        <line x1="90" y1="20" x2="90" y2="50" stroke="#e06b3a" stroke-width="2.5" />
                        <!-- Crow's Foot Fork (Cardinality N) -->
                        <line x1="105" y1="35" x2="130" y2="18" stroke="#e06b3a" stroke-width="2.5" />
                        <line x1="105" y1="35" x2="130" y2="52" stroke="#e06b3a" stroke-width="2.5" />
                        <!-- Target Entity Edge -->
                        <line x1="130" y1="10" x2="130" y2="60" stroke="#b5b0a4" stroke-width="3" />
                    </svg>
                    """,
                    example="Κάθε παραγγελία περιλαμβάνει υποχρεωτικά τουλάχιστον 1 είδος.",
                    color_class="border-[#e06b3a]",
                )

        # Full Connection Types (1:1, 1:N, N:M) with Interactive SVG Relationship Rows
        with ui.column().classes("w-full gap-4 mt-4"):
            ui.html(
                '<h3 class="text-lg font-bold text-[#f4f1ea] m-0">'
                "Πλήρης Πίνακας Συνδυασμών Συνδέσεων (1:1, 1:N, N:M)"
                "</h3>"
            )

            # 1:1 Relationships Group
            _renderRelationshipCategoryHeader("1:1 — Σχέσεις Ένα-προς-Ένα (One-to-One)", "fa-arrows-left-right", "text-blue-400")
            with ui.column().classes("w-full space-y-3"):
                _renderConnectionRow(
                    label="1..1 ─── 0..1",
                    subtitle="Υποχρεωτικό 1 προς Προαιρετικό 1",
                    left_entity="ΤΜΗΜΑ",
                    right_entity="ΥΠΑΛΛΗΛΟΣ",
                    rel_name="διευθύνεται_από",
                    left_type="one-mandatory",
                    right_type="one-optional",
                    explanation="Κάθε Τμήμα έχει υποχρεωτικά 1 Διευθυντή (1..1), αλλά ένας Υπάλληλος μπορεί να είναι διευθυντής σε 0 ή 1 τμήμα (0..1).",
                    mapping_rule="Το Foreign Key τοποθετείται στον πίνακα του ΤΜΗΜΑΤΟΣ (στην πλευρά με την ολική συμμετοχή) με NOT NULL και UNIQUE περιορισμό.",
                )
                _renderConnectionRow(
                    label="1..1 ─── 1..1",
                    subtitle="Υποχρεωτικό 1 προς Υποχρεωτικό 1",
                    left_entity="ΧΩΡΑ",
                    right_entity="ΠΡΩΤΕΥΟΥΣΑ",
                    rel_name="έχει_πρωτεύουσα",
                    left_type="one-mandatory",
                    right_type="one-mandatory",
                    explanation="Κάθε Χώρα έχει υποχρεωτικά 1 Πρωτεύουσα και κάθε Πρωτεύουσα ανήκει σε ακριβώς 1 Χώρα.",
                    mapping_rule="Συνήθως συγχωνεύονται σε 1 κοινό πίνακα ή διατηρούνται 2 πίνακες με κοινό Primary Key / FK με NOT NULL + UNIQUE.",
                )
                _renderConnectionRow(
                    label="0..1 ─── 0..1",
                    subtitle="Προαιρετικό 1 προς Προαιρετικό 1",
                    left_entity="ΥΠΑΛΛΗΛΟΣ",
                    right_entity="ΘΕΣΗ_ΣΤΑΘΜΕΥΣΗΣ",
                    rel_name="έχει_χώρο",
                    left_type="one-optional",
                    right_type="one-optional",
                    explanation="Ένας υπάλληλος μπορεί να έχει 0 ή 1 θέση, και μια θέση μπορεί να ανήκει σε 0 ή 1 υπάλληλο.",
                    mapping_rule="Το Foreign Key τοποθετείται σε οποιονδήποτε από τους δύο πίνακες, με UNIQUE περιορισμό και επιτρέποντας NULL τιμές.",
                )

            # 1:N Relationships Group
            _renderRelationshipCategoryHeader("1:N — Σχέσεις Ένα-προς-Πολλά (One-to-Many)", "fa-sitemap", "text-emerald-400")
            with ui.column().classes("w-full space-y-3"):
                _renderConnectionRow(
                    label="1..1 ─── 0..N",
                    subtitle="Υποχρεωτικό 1 προς Προαιρετικά Πολλά (Κλασικό 1:N)",
                    left_entity="ΤΜΗΜΑ",
                    right_entity="ΥΠΑΛΛΗΛΟΣ",
                    rel_name="απασχολεί",
                    left_type="one-mandatory",
                    right_type="many-optional",
                    explanation="Ένα Τμήμα απασχολεί 0 έως N Υπαλλήλους. Κάθε Υπάλληλος ανήκει υποχρεωτικά σε ακριβώς 1 Τμήμα.",
                    mapping_rule="Το Primary Key του Τμήματος μπαίνει ως Foreign Key στον πίνακα ΥΠΑΛΛΗΛΟΣ (στην πλευρά του N) και είναι NOT NULL.",
                )
                _renderConnectionRow(
                    label="0..1 ─── 0..N",
                    subtitle="Προαιρετικό 1 προς Προαιρετικά Πολλά",
                    left_entity="ΕΡΓΟ",
                    right_entity="ΥΠΑΛΛΗΛΟΣ",
                    rel_name="ανατίθεται_σε",
                    left_type="one-optional",
                    right_type="many-optional",
                    explanation="Ένα Έργο μπορεί να μην έχει κανέναν ή πολλούς υπαλλήλους. Ένας Υπάλληλος μπορεί να μην έχει αναλάβει έργο ή να έχει το πολύ 1 κύριο έργο.",
                    mapping_rule="Το Foreign Key πηγαίνει στον πίνακα του N (ΥΠΑΛΛΗΛΟΣ) και είναι NULLABLE (μπορεί να πάρει NULL).",
                )
                _renderConnectionRow(
                    label="1..1 ─── 1..N",
                    subtitle="Υποχρεωτικό 1 προς Υποχρεωτικά Πολλά",
                    left_entity="ΠΑΡΑΓΓΕΛΙΑ",
                    right_entity="ΓΡΑΜΜΗ_ΠΑΡΑΓΓΕΛΙΑΣ",
                    rel_name="περιλαμβάνει",
                    left_type="one-mandatory",
                    right_type="many-mandatory",
                    explanation="Κάθε Παραγγελία πρέπει να περιλαμβάνει τουλάχιστον 1 γραμμή παραγγελίας. Κάθε γραμμή ανήκει σε ακριβώς 1 Παραγγελία.",
                    mapping_rule="Foreign Key στον πίνακα ΓΡΑΜΜΗ_ΠΑΡΑΓΓΕΛΙΑΣ με NOT NULL και ON DELETE CASCADE.",
                )

            # N:M Relationships Group
            _renderRelationshipCategoryHeader("N:M — Σχέσεις Πολλά-προς-Πολλά (Many-to-Many)", "fa-network-wired", "text-amber-400")
            with ui.column().classes("w-full space-y-3"):
                _renderConnectionRow(
                    label="0..N ─── 0..N",
                    subtitle="Προαιρετικά Πολλά προς Προαιρετικά Πολλά",
                    left_entity="ΦΟΙΤΗΤΗΣ",
                    right_entity="ΜΑΘΗΜΑ",
                    rel_name="εγγράφεται_σε",
                    left_type="many-optional",
                    right_type="many-optional",
                    explanation="Ένας Φοιτητής εγγράφεται σε 0..N Μαθήματα. Ένα Μάθημα παρακολουθείται από 0..N Φοιτητές.",
                    mapping_rule="Δημιουργείται ΝΕΟΣ ενδιάμεσος πίνακας σύνδεσης (Junction Table) με σύνθετο Primary Key = (student_id, course_id).",
                )
                _renderConnectionRow(
                    label="1..N ─── 0..N",
                    subtitle="Υποχρεωτικά Πολλά προς Προαιρετικά Πολλά",
                    left_entity="ΣΥΓΓΡΑΦΕΑΣ",
                    right_entity="ΒΙΒΛΙΟ",
                    rel_name="συγγράφει",
                    left_type="many-mandatory",
                    right_type="many-optional",
                    explanation="Ένα Βιβλίο έχει υποχρεωτικά τουλάχιστον 1 Συγγραφέα (1..N). Ένας Συγγραφέας μπορεί να έχει 0..N Βιβλία.",
                    mapping_rule="Ενδιάμεσος πίνακας σύνδεσης (author_id, book_id) με FKs και στους δύο πίνακες.",
                )
                _renderConnectionRow(
                    label="1..N ─── 1..N",
                    subtitle="Υποχρεωτικά Πολλά προς Υποχρεωτικά Πολλά",
                    left_entity="ΙΑΤΡΟΣ",
                    right_entity="ΑΣΘΕΝΗΣ",
                    rel_name="παρακολουθεί",
                    left_type="many-mandatory",
                    right_type="many-mandatory",
                    explanation="Κάθε Ιατρός παρακολουθεί τουλάχιστον 1 Ασθενή και κάθε Ασθενής παρακολουθείται από τουλάχιστον 1 Ιατρό.",
                    mapping_rule="Ενδιάμεσος πίνακας σύνδεσης με ελέγχους επιχειρησιακής λογικής / triggers για τη διασφάλιση ελάχιστης πληθικότητας.",
                )

        # Special Architectural Relationship Patterns
        with ui.column().classes("w-full gap-4 mt-6"):
            ui.html('<h3 class="text-lg font-bold text-[#f4f1ea] m-0">Ειδικές Μορφές Σχέσεων & Προχωρημένα Μοτίβα</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-3 gap-4 w-full"):
                # Pattern 1: Weak Entity / Identifying Relationship
                with ui.column().classes("p-5 rounded-xl bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-2"):
                    with ui.row().classes("items-center gap-2"):
                        ui.html('<i class="fa-solid fa-clone text-amber-400"></i>')
                        ui.label("Ασθενής Οντότητα & Ταυτοποίηση").classes("font-bold text-amber-300 text-sm")
                    ui.label(
                        "Σχέση Ταυτοποίησης (Identifying Relationship): Η ασθενής οντότητα δανείζεται το PK του ιδιοκτήτη (Owner). "
                        "Το σύνθετο PK της είναι: (Owner_PK, Partial_Key)."
                    ).classes("text-xs text-[#b5b0a4] leading-relaxed")
                    ui.html(
                        """
                        <div class="p-2 rounded bg-[#141413] font-mono text-[11px] text-[#e06b3a]">
                            PK: (employee_id, dependent_name)
                        </div>
                        """
                    )

                # Pattern 2: Recursive / Unary Relationships
                with ui.column().classes("p-5 rounded-xl bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-2"):
                    with ui.row().classes("items-center gap-2"):
                        ui.html('<i class="fa-solid fa-arrows-rotate text-blue-400"></i>')
                        ui.label("Αναδρομικές Σχέσεις (Recursive)").classes("font-bold text-blue-300 text-sm")
                    ui.label(
                        "Μια οντότητα συνδέεται με τον εαυτό της σε διαφορετικούς ρόλους (π.χ. Υπάλληλος - Προϊστάμενος, Μάθημα - Προαπαιτούμενο). "
                        "Στον πίνακα προστίθεται αυτοαναφορικό FK (Self-referencing FK)."
                    ).classes("text-xs text-[#b5b0a4] leading-relaxed")
                    ui.html(
                        """
                        <div class="p-2 rounded bg-[#141413] font-mono text-[11px] text-blue-300">
                            supervisor_id REFERENCES employees(id)
                        </div>
                        """
                    )

                # Pattern 3: Ternary Relationships
                with ui.column().classes("p-5 rounded-xl bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-2"):
                    with ui.row().classes("items-center gap-2"):
                        ui.html('<i class="fa-solid fa-cubes text-emerald-400"></i>')
                        ui.label("Τριμελείς Σχέσεις (Ternary)").classes("font-bold text-emerald-300 text-sm")
                    ui.label(
                        "Ταυτόχρονη σύνδεση 3 οντοτήτων (π.χ. Προμηθευτής, Έργο, Ανταλλακτικό). "
                        "Μετατρέπεται ΠΑΝΤΑ σε ξεχωριστό σχεσιακό πίνακα με 3 Foreign Keys και σύνθετο κλειδί."
                    ).classes("text-xs text-[#b5b0a4] leading-relaxed")
                    ui.html(
                        """
                        <div class="p-2 rounded bg-[#141413] font-mono text-[11px] text-emerald-300">
                            PK: (supplier_id, project_id, part_id)
                        </div>
                        """
                    )


def _renderEndpointCard(
    title: str,
    greek_name: str,
    modality: str,
    cardinality: str,
    svg_markup: str,
    example: str,
    color_class: str,
) -> None:
    """Renders a single endpoint explanation card with embedded SVG visualization."""
    with ui.column().classes(f"p-4 rounded-xl bg-[#201f1d] border-t-4 {color_class} border border-[rgba(255,255,255,0.06)] gap-2"):
        ui.label(title).classes("font-bold text-[#f4f1ea] text-sm")
        ui.label(greek_name).classes("text-xs text-[#e06b3a] font-semibold")

        ui.html(svg_markup)

        with ui.column().classes("gap-1 text-[11px] text-[#b5b0a4] border-t border-[rgba(255,255,255,0.06)] pt-2"):
            with ui.row().classes("justify-between w-full"):
                ui.label("Modality (Min):").classes("text-[#78756d]")
                ui.label(modality).classes("font-medium text-[#f4f1ea]")
            with ui.row().classes("justify-between w-full"):
                ui.label("Cardinality (Max):").classes("text-[#78756d]")
                ui.label(cardinality).classes("font-medium text-[#f4f1ea]")

        with ui.column().classes("bg-[#141413] p-2 rounded text-[11px] text-[#78756d] italic mt-1"):
            ui.label(f"Παράδειγμα: {example}")


def _renderRelationshipCategoryHeader(title: str, icon: str, color_class: str) -> None:
    """Renders a subsection header for relationship category groupings."""
    with ui.row().classes("items-center gap-2 mt-4"):
        ui.html(f'<i class="fa-solid {icon} {color_class} text-sm"></i>')
        ui.label(title).classes(f"font-bold {color_class} text-sm tracking-wide")


def _renderConnectionRow(
    label: str,
    subtitle: str,
    left_entity: str,
    right_entity: str,
    rel_name: str,
    left_type: str,
    right_type: str,
    explanation: str,
    mapping_rule: str,
) -> None:
    """Renders an interactive visual connection line between two entity boxes."""
    # Generate SVG markers based on type
    svg_code = _generateConnectionSvg(left_type, right_type)

    with ui.column().classes(
        "w-full p-4 rounded-xl bg-[#201f1d] border border-[rgba(255,255,255,0.06)] hover:border-[rgba(224,107,58,0.4)] transition-colors gap-3"
    ):
        with ui.row().classes("justify-between items-center w-full flex-wrap gap-2"):
            with ui.row().classes("items-center gap-2"):
                ui.label(label).classes("font-mono font-bold text-sm text-[#e06b3a] bg-[#141413] px-2.5 py-1 rounded-md border border-[rgba(224,107,58,0.3)]")
                ui.label(subtitle).classes("text-xs font-semibold text-[#f4f1ea]")
            ui.label(f"Συσχέτιση: {rel_name}").classes("text-[11px] text-[#78756d] font-mono")

        # Visual Diagram Row
        with ui.row().classes("items-center justify-between w-full py-2 px-2 bg-[#121211] rounded-lg border border-[rgba(255,255,255,0.04)]"):
            # Left Entity Box
            ui.html(
                f'<div class="px-3 py-2 rounded-md bg-[#242321] border border-blue-500/40 text-blue-300 font-bold text-xs shadow-sm">'
                f'<i class="fa-solid fa-table text-blue-400 mr-1.5"></i>{left_entity}'
                f'</div>'
            )

            # Center SVG Connection Line
            ui.html(svg_code)

            # Right Entity Box
            ui.html(
                f'<div class="px-3 py-2 rounded-md bg-[#242321] border border-emerald-500/40 text-emerald-300 font-bold text-xs shadow-sm">'
                f'<i class="fa-solid fa-table text-emerald-400 mr-1.5"></i>{right_entity}'
                f'</div>'
            )

        # Explanatory Text and Relational Mapping Tip
        with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-3 w-full text-xs"):
            with ui.column().classes("gap-1"):
                ui.label("Ερμηνεία Σχέσης:").classes("text-[#78756d] font-semibold text-[11px]")
                ui.label(explanation).classes("text-[#b5b0a4] leading-relaxed")

            with ui.column().classes("gap-1 bg-[#171615] p-2.5 rounded-lg border border-[rgba(255,255,255,0.04)]"):
                ui.label("Κανόνας Μετατροπής σε SQL / Πίνακες:").classes("text-[#f59e0b] font-semibold text-[11px]")
                ui.label(mapping_rule).classes("text-[#f4f1ea] leading-relaxed")


def _generateConnectionSvg(left_type: str, right_type: str) -> str:
    """Generates an inline SVG showing two endpoints on a horizontal connection line."""
    # Left marker SVG elements (at x ~ 40..60)
    left_elements = ""
    if left_type == "one-mandatory":
        left_elements = """
        <line x1="30" y1="12" x2="30" y2="28" stroke="#e06b3a" stroke-width="2" />
        <line x1="42" y1="12" x2="42" y2="28" stroke="#e06b3a" stroke-width="2" />
        """
    elif left_type == "one-optional":
        left_elements = """
        <line x1="30" y1="12" x2="30" y2="28" stroke="#e06b3a" stroke-width="2" />
        <circle cx="45" cy="20" r="5" fill="#121211" stroke="#e06b3a" stroke-width="2" />
        """
    elif left_type == "many-optional":
        left_elements = """
        <line x1="15" y1="10" x2="35" y2="20" stroke="#e06b3a" stroke-width="2" />
        <line x1="15" y1="30" x2="35" y2="20" stroke="#e06b3a" stroke-width="2" />
        <circle cx="48" cy="20" r="5" fill="#121211" stroke="#e06b3a" stroke-width="2" />
        """
    elif left_type == "many-mandatory":
        left_elements = """
        <line x1="15" y1="10" x2="35" y2="20" stroke="#e06b3a" stroke-width="2" />
        <line x1="15" y1="30" x2="35" y2="20" stroke="#e06b3a" stroke-width="2" />
        <line x1="48" y1="12" x2="48" y2="28" stroke="#e06b3a" stroke-width="2" />
        """

    # Right marker SVG elements (at x ~ 180..205)
    right_elements = ""
    if right_type == "one-mandatory":
        right_elements = """
        <line x1="178" y1="12" x2="178" y2="28" stroke="#e06b3a" stroke-width="2" />
        <line x1="190" y1="12" x2="190" y2="28" stroke="#e06b3a" stroke-width="2" />
        """
    elif right_type == "one-optional":
        right_elements = """
        <circle cx="175" cy="20" r="5" fill="#121211" stroke="#e06b3a" stroke-width="2" />
        <line x1="190" y1="12" x2="190" y2="28" stroke="#e06b3a" stroke-width="2" />
        """
    elif right_type == "many-optional":
        right_elements = """
        <circle cx="172" cy="20" r="5" fill="#121211" stroke="#e06b3a" stroke-width="2" />
        <line x1="185" y1="20" x2="205" y2="10" stroke="#e06b3a" stroke-width="2" />
        <line x1="185" y1="20" x2="205" y2="30" stroke="#e06b3a" stroke-width="2" />
        """
    elif right_type == "many-mandatory":
        right_elements = """
        <line x1="172" y1="12" x2="172" y2="28" stroke="#e06b3a" stroke-width="2" />
        <line x1="185" y1="20" x2="205" y2="10" stroke="#e06b3a" stroke-width="2" />
        <line x1="185" y1="20" x2="205" y2="30" stroke="#e06b3a" stroke-width="2" />
        """

    return f"""
    <svg viewBox="0 0 220 40" class="w-48 sm:w-64 h-10 flex-shrink-0">
        <!-- Main connection line -->
        <line x1="15" y1="20" x2="205" y2="20" stroke="#e06b3a" stroke-width="2" />
        {left_elements}
        {right_elements}
    </svg>
    """


def _renderRelationalMappingRules() -> None:
    """Renders the 7 golden rules for converting ER models into relational schemas."""
    with ui.column().classes("w-full glass-panel p-6 md:p-8 rounded-2xl gap-6"):
        with ui.row().classes("items-center gap-3 border-b border-[rgba(255,255,255,0.08)] pb-4"):
            ui.html('<i class="fa-solid fa-database text-[#f59e0b] text-2xl"></i>')
            with ui.column().classes("gap-0"):
                ui.html(
                    '<h2 class="text-xl md:text-2xl font-bold text-[#f4f1ea] m-0">'
                    "Οι 7 Χρυσοί Κανόνες Μετατροπής ER σε Σχεσιακούς Πίνακες (SQL DDL)"
                    "</h2>"
                )
                ui.label(
                    "Η ακριβής μεθοδολογία για τη δημιουργία πινάκων, Primary Keys, Foreign Keys και περιορισμών."
                ).classes("text-xs text-[#b5b0a4] mt-1")

        with ui.grid().classes("grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 w-full"):
            # Rule 1
            _renderRuleCard(
                number="1",
                title="Ισχυρές Οντότητες (Strong Entities)",
                icon="fa-cube",
                color="border-blue-500",
                description="Κάθε ισχυρή οντότητα γίνεται ένας ξεχωριστός πίνακας. Τα απλά γνωρίσματα γίνονται στήλες και το επιλεγμένο αναγνωριστικό ορίζεται ως PRIMARY KEY.",
            )

            # Rule 2
            _renderRuleCard(
                number="2",
                title="Ασθενείς Οντότητες (Weak Entities)",
                icon="fa-clone",
                color="border-amber-500",
                description="Γίνεται πίνακας που περιλαμβάνει όλα τα απλά γνωρίσματά της συν το Primary Key της οντότητας-ιδιοκτήτη (Owner FK). Το PRIMARY KEY είναι ΣΥΝΘΕΤΟ: (Owner_PK, Partial_Key).",
            )

            # Rule 3
            _renderRuleCard(
                number="3",
                title="Σχέσεις 1:1 (One-to-One)",
                icon="fa-arrows-left-right",
                color="border-emerald-500",
                description="Το PK του ενός πίνακα εισάγεται ως Foreign Key στον άλλο. Προτιμάται ο πίνακας με την ολική (υποχρεωτική) συμμετοχή. Το Foreign Key ορίζεται υποχρεωτικά ως UNIQUE και NOT NULL.",
            )

            # Rule 4
            _renderRuleCard(
                number="4",
                title="Σχέσεις 1:N (One-to-Many)",
                icon="fa-sitemap",
                color="border-[#e06b3a]",
                description="Το Primary Key της πλευράς του '1' εισάγεται ως Foreign Key στον πίνακα της πλευράς του 'N'. Εάν η συμμετοχή του N είναι ολική, το FK ορίζεται NOT NULL.",
            )

            # Rule 5
            _renderRuleCard(
                number="5",
                title="Σχέσεις N:M (Many-to-Many)",
                icon="fa-network-wired",
                color="border-rose-500",
                description="Δημιουργείται ΝΕΟΣ ανεξάρτητος πίνακας σύνδεσης. Περιλαμβάνει ως Foreign Keys τα PKs και των δύο συνδεόμενων οντοτήτων συν τυχόν γνωρίσματα της σχέσης. PRIMARY KEY = (FK1, FK2).",
            )

            # Rule 6
            _renderRuleCard(
                number="6",
                title="Πλειότιμα Γνωρίσματα (Multi-valued)",
                icon="fa-tags",
                color="border-purple-500",
                description="Κάθε πλειότιμο γνώρισμα (π.χ. πολλαπλά τηλέφωνα, εγκαταστάσεις) γίνεται νέος πίνακας με: το PK της οντότητας + τη στήλη της τιμής. PRIMARY KEY = (Entity_PK, Attribute_Value).",
            )

            # Rule 7
            _renderRuleCard(
                number="7",
                title="Σύνθετα Γνωρίσματα (Composite)",
                icon="fa-layer-group",
                color="border-teal-500",
                description="Διασπώνται στα επιμέρους απλά/ατομικά γνωρίσματά τους (π.χ. Διεύθυνση -> οδός, αριθμός, ΤΚ, πόλη). Το σύνθετο γνώρισμα ως ενιαία έννοια δεν αποτελεί ξεχωριστή στήλη.",
            )


def _renderRuleCard(number: str, title: str, icon: str, color: str, description: str) -> None:
    """Renders a single rule card in the 7 golden rules grid."""
    with ui.column().classes(f"p-5 rounded-xl bg-[#201f1d] border-l-4 {color} border border-[rgba(255,255,255,0.06)] gap-2"):
        with ui.row().classes("items-center justify-between w-full"):
            with ui.row().classes("items-center gap-2"):
                ui.html(f'<i class="fa-solid {icon} text-sm text-[#e06b3a]"></i>')
                ui.label(title).classes("font-bold text-[#f4f1ea] text-xs")
            ui.label(f"Κανόνας {number}").classes("text-[10px] font-mono text-[#78756d] bg-[#141413] px-2 py-0.5 rounded")
        ui.label(description).classes("text-xs text-[#b5b0a4] leading-relaxed")


def _renderNotationComparisonSection() -> None:
    """Renders a comparative table between Crow's Foot, Chen, and Min-Max notations."""
    with ui.column().classes("w-full glass-panel p-6 md:p-8 rounded-2xl gap-4"):
        with ui.row().classes("items-center gap-3 border-b border-[rgba(255,255,255,0.08)] pb-4"):
            ui.html('<i class="fa-solid fa-code-compare text-blue-400 text-2xl"></i>')
            with ui.column().classes("gap-0"):
                ui.html(
                    '<h2 class="text-xl md:text-2xl font-bold text-[#f4f1ea] m-0">'
                    "Συγκριτικός Πίνακας Συμβολισμών (Crow's Foot vs Chen vs Min-Max)"
                    "</h2>"
                )
                ui.label(
                    "Χρήσιμη αντιστοίχιση για την αναγνώριση θεμάτων εξετάσεων σε διαφορετικές παραλλαγές μοντελοποίησης."
                ).classes("text-xs text-[#b5b0a4] mt-1")

        comparison_table = """
        <div class="overflow-x-auto w-full">
            <table class="dark-table">
                <thead>
                    <tr>
                        <th style="width: 25%;">Έννοια / Τύπος</th>
                        <th style="width: 25%;">Crow's Foot (Martin)</th>
                        <th style="width: 25%;">Κλασικό ER (Peter Chen)</th>
                        <th style="width: 25%;">Min-Max Συμβολισμός</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="font-bold text-[#f4f1ea]">Οντότητα</td>
                        <td>Ορθογώνιο πλαίσιο με λίστα γνωρισμάτων</td>
                        <td>Απλό Ορθογώνιο</td>
                        <td>Ορθογώνιο</td>
                    </tr>
                    <tr>
                        <td class="font-bold text-[#f4f1ea]">Ασθενής Οντότητα</td>
                        <td>Πλαίσιο με στρογγυλεμένες γωνίες ή ένδειξη PK</td>
                        <td>Διπλό Ορθογώνιο</td>
                        <td>Διπλό Ορθογώνιο</td>
                    </tr>
                    <tr>
                        <td class="font-bold text-[#f4f1ea]">Συσχέτιση</td>
                        <td>Ευθεία γραμμή με σύμβολα στα άκρα</td>
                        <td>Ρόμβος (Diamond) ανάμεσα στις οντότητες</td>
                        <td>Ρόμβος με ετικέτα (min, max)</td>
                    </tr>
                    <tr>
                        <td class="font-bold text-[#f4f1ea]">Πρωτεύον Κλειδί (PK)</td>
                        <td>Ένδειξη [PK] ή υπογράμμιση στο κουτί</td>
                        <td>Υπογραμμισμένο κείμενο μέσα σε Έλλειψη</td>
                        <td>Υπογραμμισμένο γνώρισμα</td>
                    </tr>
                    <tr>
                        <td class="font-bold text-[#f4f1ea]">Μερικό Κλειδί (Weak PK)</td>
                        <td>Ένδειξη [Part-PK]</td>
                        <td>Διακεκομμένη υπογράμμιση σε Έλλειψη</td>
                        <td>Διακεκομμένη υπογράμμιση</td>
                    </tr>
                    <tr>
                        <td class="font-bold text-[#f4f1ea]">Προαιρετικό Ένα (0..1)</td>
                        <td>Κύκλος και Κάθετη Γραμμή (O |)</td>
                        <td>Απλή γραμμή (1) και μερική συμμετοχή</td>
                        <td>(0, 1) στην πλευρά συμμετοχής</td>
                    </tr>
                    <tr>
                        <td class="font-bold text-[#f4f1ea]">Υποχρεωτικό Ένα (1..1)</td>
                        <td>Δύο Κάθετες Γραμμές (| |)</td>
                        <td>Διπλή γραμμή (1) ή ολική συμμετοχή</td>
                        <td>(1, 1) στην πλευρά συμμετοχής</td>
                    </tr>
                    <tr>
                        <td class="font-bold text-[#f4f1ea]">Προαιρετικά Πολλά (0..N)</td>
                        <td>Κύκλος και Διχάλα (O &lt;)</td>
                        <td>Απλή γραμμή με ένδειξη N / M</td>
                        <td>(0, N) στην πλευρά συμμετοχής</td>
                    </tr>
                    <tr>
                        <td class="font-bold text-[#f4f1ea]">Υποχρεωτικά Πολλά (1..N)</td>
                        <td>Κάθετη Γραμμή και Διχάλα (| &lt;)</td>
                        <td>Διπλή γραμμή με ένδειξη N / M</td>
                        <td>(1, N) στην πλευρά συμμετοχής</td>
                    </tr>
                </tbody>
            </table>
        </div>
        """
        ui.html(comparison_table)
