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
                        "Complete Theoretical Guide & ER Design Methodology"
                        "</h1>"
                    )
                    ui.label(
                        "Comprehensive handbook for requirements analysis, entity/relationship identification, "
                        "Crow's Foot notation, and relational schema transformation rules."
                    ).classes("text-sm text-[#b5b0a4] mt-1")

            with ui.row().classes("gap-3 flex-wrap text-xs"):
                with ui.row().classes(
                    "items-center gap-1.5 px-3 py-1.5 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.08)] text-[#f4f1ea]"
                ):
                    ui.html('<i class="fa-solid fa-layer-group text-blue-400"></i>')
                    ui.label("4 Core Analysis Steps")

                with ui.row().classes(
                    "items-center gap-1.5 px-3 py-1.5 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.08)] text-[#f4f1ea]"
                ):
                    ui.html('<i class="fa-solid fa-table text-emerald-400"></i>')
                    ui.label("Recognition Matrix")

                with ui.row().classes(
                    "items-center gap-1.5 px-3 py-1.5 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.08)] text-[#f4f1ea]"
                ):
                    ui.html('<i class="fa-solid fa-code-branch text-[#e06b3a]"></i>')
                    ui.label("Crow's Foot Notation")

                with ui.row().classes(
                    "items-center gap-1.5 px-3 py-1.5 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.08)] text-[#f4f1ea]"
                ):
                    ui.html('<i class="fa-solid fa-database text-amber-400"></i>')
                    ui.label("7 Relational Mapping Rules")

        # SECTION 1: Step-by-Step Methodology Cards
        with ui.column().classes("w-full gap-4"):
            renderMethodologyCards()

            # Deep-dive analysis tips for each step
            with ui.column().classes("w-full glass-panel p-6 rounded-2xl gap-4"):
                with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                    ui.html('<i class="fa-solid fa-lightbulb text-[#f59e0b] text-lg"></i>')
                    ui.html('<h3 class="text-lg font-bold text-[#f4f1ea] m-0">Practical Guidelines & Traps During Analysis</h3>')

                with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full text-xs leading-relaxed"):
                    # Card 1: Entities vs Attributes
                    with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-2"):
                        with ui.row().classes("items-center gap-2"):
                            ui.html('<i class="fa-solid fa-scale-balanced text-blue-400"></i>')
                            ui.label("Entity or Attribute?").classes("font-bold text-blue-300")
                        ui.label(
                            "Rule: If a concept has its own attributes (e.g., a Department has a name, phone, address), "
                            "it is an ENTITY. If it is a simple atomic value without independent properties (e.g., age, status), it is an ATTRIBUTE."
                        ).classes("text-[#b5b0a4]")

                    # Card 2: Relationship Direction
                    with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-2"):
                        with ui.row().classes("items-center gap-2"):
                            ui.html('<i class="fa-solid fa-arrows-left-right text-rose-400"></i>')
                            ui.label("Bidirectional Cardinality Investigation").classes("font-bold text-rose-300")
                        ui.label(
                            "Rule: To determine the cardinality ratio, ALWAYS ask two questions:\n"
                            "1) For 1 instance of A, how many instances of B can be associated? (min, max)\n"
                            "2) For 1 instance of B, how many instances of A can be associated? (min, max)"
                        ).classes("text-[#b5b0a4]")

                    # Card 3: Relationship Attributes
                    with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-2"):
                        with ui.row().classes("items-center gap-2"):
                            ui.html('<i class="fa-solid fa-link text-emerald-400"></i>')
                            ui.label("Relationship Attributes").classes("font-bold text-emerald-300")
                        ui.label(
                            "Rule: When information arises ONLY from the combination of two entities "
                            "(e.g., a Student's grade in a Course, or an Employee's hours on a Project), "
                            "the attribute belongs to the RELATIONSHIP and not to an individual entity."
                        ).classes("text-[#b5b0a4]")

                    # Card 4: Weak Entities & Partial Keys
                    with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-2"):
                        with ui.row().classes("items-center gap-2"):
                            ui.html('<i class="fa-solid fa-fingerprint text-amber-400"></i>')
                            ui.label("Weak Entities & Partial Keys").classes("font-bold text-amber-300")
                        ui.label(
                            "Rule: An entity is weak (Weak Entity) when it lacks its own independent unique identifier "
                            "and is existence-dependent on a strong owner entity (Owner). Its primary key is formed by combining "
                            "the Owner's PK with its own Partial Key (Discriminator)."
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
                    "Crow's Foot Notation (Endpoints & Relationships Guide)"
                    "</h2>"
                )
                ui.label(
                    "Analysis of all relationship endpoint symbols, interpretation of Modality / Cardinality, "
                    "and a comprehensive catalog of combinations (0:1, 1:1, 1:N, 0:M, 1:M, N:M)."
                ).classes("text-xs text-[#b5b0a4] mt-1")

        # Anatomy of Crow's Foot Endpoint
        with ui.column().classes("w-full p-5 rounded-xl bg-[#171615] border border-[rgba(224,107,58,0.25)] gap-3"):
            with ui.row().classes("items-center gap-2"):
                ui.html('<i class="fa-solid fa-circle-info text-[#e06b3a]"></i>')
                ui.html('<h3 class="text-base font-bold text-[#f4f1ea] m-0">Anatomy of a Crow\'s Foot Endpoint (Dual Symbol)</h3>')
            ui.label(
                "In Crow's Foot notation, each connection endpoint consists of two distinct symbols read from inside out:"
            ).classes("text-xs text-[#b5b0a4]")

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full mt-2"):
                with ui.column().classes("p-4 rounded-lg bg-[#201f1d] border-l-4 border-amber-500 gap-1"):
                    ui.label("1. Inner Symbol = Modality (Minimum Participation)").classes(
                        "font-bold text-amber-300 text-xs"
                    )
                    ui.label(
                        "• Circle (O): Minimum = 0 (Optional Participation)\n"
                        "• Vertical Bar (|): Minimum = 1 (Mandatory Participation)"
                    ).classes("text-xs text-[#b5b0a4] leading-relaxed")

                with ui.column().classes("p-4 rounded-lg bg-[#201f1d] border-l-4 border-[#e06b3a] gap-1"):
                    ui.label("2. Outer Symbol = Cardinality (Maximum Ratio)").classes(
                        "font-bold text-[#fdba74] text-xs"
                    )
                    ui.label(
                        "• Vertical Bar (|): Maximum = 1 (One instance)\n"
                        "• Crow's Foot Fork (<): Maximum = N or M (Many instances)"
                    ).classes("text-xs text-[#b5b0a4] leading-relaxed")

        # Official Crow's Foot Connection Reference (7 Variants from Standard / Official Notation)
        with ui.column().classes("w-full gap-4"):
            with ui.row().classes("items-center gap-2"):
                ui.html('<i class="fa-solid fa-diagram-project text-[#e06b3a]"></i>')
                ui.html('<h3 class="text-lg font-bold text-[#f4f1ea] m-0">Official Crow\'s Foot Connections & Endpoints Guide (7 Variants)</h3>')
            ui.label(
                "The following overview presents both generic simplified connections "
                "and detailed Information Engineering (IE) notations with full Modality and Cardinality representations:"
            ).classes("text-xs text-[#b5b0a4]")

            with ui.grid().classes("grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4 w-full"):
                _renderOfficialSymbolCard(
                    title="One to One",
                    display_name="Generic One-to-One",
                    svg_markup="""
                    <svg viewBox="0 0 160 50" class="w-full h-12">
                        <line x1="15" y1="25" x2="145" y2="25" stroke="#e06b3a" stroke-width="2.5" />
                    </svg>
                    """,
                    desc="Continuous solid line for 1:1 without explicit modality markers (Generic One-to-One).",
                    color_class="border-blue-500",
                )
                _renderOfficialSymbolCard(
                    title="One to Many (Mandatory)",
                    display_name="Simple One-to-Many (Mandatory)",
                    svg_markup="""
                    <svg viewBox="0 0 160 50" class="w-full h-12">
                        <line x1="15" y1="25" x2="145" y2="25" stroke="#e06b3a" stroke-width="2.5" />
                        <line x1="35" y1="12" x2="35" y2="38" stroke="#e06b3a" stroke-width="2.5" />
                        <line x1="120" y1="25" x2="145" y2="12" stroke="#e06b3a" stroke-width="2.5" />
                        <line x1="120" y1="25" x2="145" y2="38" stroke="#e06b3a" stroke-width="2.5" />
                    </svg>
                    """,
                    desc="Simplified 1:N connection with single tick mark on One and fork on Many (Simple 1:N).",
                    color_class="border-emerald-500",
                )
                _renderOfficialSymbolCard(
                    title="Many",
                    display_name="Generic Many (Crow's Foot)",
                    svg_markup="""
                    <svg viewBox="0 0 160 50" class="w-full h-12">
                        <line x1="15" y1="25" x2="145" y2="25" stroke="#e06b3a" stroke-width="2.5" />
                        <line x1="15" y1="12" x2="40" y2="25" stroke="#e06b3a" stroke-width="2.5" />
                        <line x1="15" y1="38" x2="40" y2="25" stroke="#e06b3a" stroke-width="2.5" />
                    </svg>
                    """,
                    desc="Simple Many endpoint without distinction between optional and mandatory participation.",
                    color_class="border-amber-500",
                )
                _renderOfficialSymbolCard(
                    title="One and Only One (Mandatory)",
                    display_name="Exactly One (1..1 Mandatory)",
                    svg_markup="""
                    <svg viewBox="0 0 160 50" class="w-full h-12">
                        <line x1="15" y1="25" x2="145" y2="25" stroke="#e06b3a" stroke-width="2.5" />
                        <line x1="28" y1="12" x2="28" y2="38" stroke="#e06b3a" stroke-width="2.5" />
                        <line x1="42" y1="12" x2="42" y2="38" stroke="#e06b3a" stroke-width="2.5" />
                    </svg>
                    """,
                    desc="Two vertical bars (||): Mandatory participation in exactly 1 instance (Modality: 1, Cardinality: 1).",
                    color_class="border-emerald-500",
                )
                _renderOfficialSymbolCard(
                    title="One or More (Mandatory)",
                    display_name="One or More (1..N Mandatory)",
                    svg_markup="""
                    <svg viewBox="0 0 160 50" class="w-full h-12">
                        <line x1="15" y1="25" x2="145" y2="25" stroke="#e06b3a" stroke-width="2.5" />
                        <line x1="15" y1="12" x2="38" y2="25" stroke="#e06b3a" stroke-width="2.5" />
                        <line x1="15" y1="38" x2="38" y2="25" stroke="#e06b3a" stroke-width="2.5" />
                        <line x1="48" y1="12" x2="48" y2="38" stroke="#e06b3a" stroke-width="2.5" />
                    </svg>
                    """,
                    desc="Fork with vertical bar (>|): Mandatory participation in at least 1 instance (Modality: 1, Cardinality: N).",
                    color_class="border-[#e06b3a]",
                )
                _renderOfficialSymbolCard(
                    title="Zero or one (Optional)",
                    display_name="Zero or One (0..1 Optional)",
                    svg_markup="""
                    <svg viewBox="0 0 160 50" class="w-full h-12">
                        <line x1="15" y1="25" x2="145" y2="25" stroke="#e06b3a" stroke-width="2.5" />
                        <circle cx="28" cy="25" r="6" fill="var(--svg-canvas-bg, #ffffff)" stroke="#e06b3a" stroke-width="2.5" class="svg-marker-circle" />
                        <line x1="46" y1="12" x2="46" y2="38" stroke="#e06b3a" stroke-width="2.5" />
                    </svg>
                    """,
                    desc="Circle with vertical bar (O|): Optional participation in at most 1 instance (Modality: 0, Cardinality: 1).",
                    color_class="border-slate-500",
                )
                _renderOfficialSymbolCard(
                    title="Zero or Many (Optional)",
                    display_name="Zero or Many (0..N Optional)",
                    svg_markup="""
                    <svg viewBox="0 0 160 50" class="w-full h-12">
                        <line x1="15" y1="25" x2="145" y2="25" stroke="#e06b3a" stroke-width="2.5" />
                        <line x1="15" y1="12" x2="38" y2="25" stroke="#e06b3a" stroke-width="2.5" />
                        <line x1="15" y1="38" x2="38" y2="25" stroke="#e06b3a" stroke-width="2.5" />
                        <circle cx="50" cy="25" r="6" fill="var(--svg-canvas-bg, #ffffff)" stroke="#e06b3a" stroke-width="2.5" class="svg-marker-circle" />
                    </svg>
                    """,
                    desc="Fork with circle (>O): Optional participation in 0 to many instances (Modality: 0, Cardinality: N).",
                    color_class="border-blue-500",
                )

        # 4 Fundamental Endpoints Cards with SVGs
        with ui.column().classes("w-full gap-4"):
            ui.html('<h3 class="text-lg font-bold text-[#f4f1ea] m-0">The 4 Fundamental Crow\'s Foot Endpoints</h3>')

            with ui.grid().classes("grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 w-full"):
                # Endpoint 1: Zero or One (0..1)
                _renderEndpointCard(
                    title="0..1 (Zero or One)",
                    display_name="Zero or One (Optional 1)",
                    modality="0 (Optional)",
                    cardinality="1 (Single)",
                    svg_markup="""
                    <svg viewBox="0 0 160 70" class="w-full h-16">
                        <!-- Line -->
                        <line x1="10" y1="35" x2="130" y2="35" stroke="#e06b3a" stroke-width="2.5" />
                        <!-- Circle (Modality 0) -->
                        <circle cx="100" cy="35" r="7" fill="var(--svg-canvas-bg, #ffffff)" stroke="#e06b3a" stroke-width="2.5" class="svg-marker-circle" />
                        <!-- Perpendicular Bar (Cardinality 1) -->
                        <line x1="120" y1="20" x2="120" y2="50" stroke="#e06b3a" stroke-width="2.5" />
                        <!-- Target Entity Edge -->
                        <line x1="130" y1="10" x2="130" y2="60" stroke="#b5b0a4" stroke-width="3" />
                    </svg>
                    """,
                    example="An employee can manage at most 1 department or none.",
                    color_class="border-slate-500",
                )

                # Endpoint 2: Exactly One (1..1)
                _renderEndpointCard(
                    title="1..1 (Exactly One)",
                    display_name="Exactly One (Mandatory 1)",
                    modality="1 (Mandatory)",
                    cardinality="1 (Single)",
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
                    example="Each department belongs mandatorily to exactly 1 faculty or company.",
                    color_class="border-emerald-500",
                )

                # Endpoint 3: Zero or Many (0..N / 0..M)
                _renderEndpointCard(
                    title="0..N / 0..M (Zero or Many)",
                    display_name="Zero or Many (Optional Many)",
                    modality="0 (Optional)",
                    cardinality="N (Many)",
                    svg_markup="""
                    <svg viewBox="0 0 160 70" class="w-full h-16">
                        <!-- Line -->
                        <line x1="10" y1="35" x2="130" y2="35" stroke="#e06b3a" stroke-width="2.5" />
                        <!-- Circle (Modality 0) -->
                        <circle cx="85" cy="35" r="7" fill="var(--svg-canvas-bg, #ffffff)" stroke="#e06b3a" stroke-width="2.5" class="svg-marker-circle" />
                        <!-- Crow's Foot Fork (Cardinality N) -->
                        <line x1="105" y1="35" x2="130" y2="18" stroke="#e06b3a" stroke-width="2.5" />
                        <line x1="105" y1="35" x2="130" y2="52" stroke="#e06b3a" stroke-width="2.5" />
                        <!-- Target Entity Edge -->
                        <line x1="130" y1="10" x2="130" y2="60" stroke="#b5b0a4" stroke-width="3" />
                    </svg>
                    """,
                    example="An author may have written 0 to many books.",
                    color_class="border-blue-500",
                )

                # Endpoint 4: One or Many (1..N / 1..M)
                _renderEndpointCard(
                    title="1..N / 1..M (One or Many)",
                    display_name="One or Many (Mandatory Many)",
                    modality="1 (Mandatory)",
                    cardinality="N (Many)",
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
                    example="Each order must mandatorily include at least 1 order line item.",
                    color_class="border-[#e06b3a]",
                )

        # Full Connection Types (1:1, 1:N, N:M) with Interactive SVG Relationship Rows
        with ui.column().classes("w-full gap-4 mt-4"):
            ui.html(
                '<h3 class="text-lg font-bold text-[#f4f1ea] m-0">'
                "Complete Connection Combination Matrix (1:1, 1:N, N:M)"
                "</h3>"
            )

            # 1:1 Relationships Group
            _renderRelationshipCategoryHeader("1:1 — One-to-One Relationships", "fa-arrows-left-right", "text-blue-400")
            with ui.column().classes("w-full space-y-3"):
                _renderConnectionRow(
                    label="1..1 ─── 0..1",
                    subtitle="Mandatory 1 to Optional 1",
                    left_entity="DEPARTMENT",
                    right_entity="EMPLOYEE",
                    rel_name="managed_by",
                    left_type="one-mandatory",
                    right_type="one-optional",
                    explanation="Each Department has mandatorily 1 Manager (1..1), but an Employee can manage 0 or 1 department (0..1).",
                    mapping_rule="The Foreign Key is placed in the DEPARTMENT table (the side with total participation) with NOT NULL and UNIQUE constraints.",
                )
                _renderConnectionRow(
                    label="1..1 ─── 1..1",
                    subtitle="Mandatory 1 to Mandatory 1",
                    left_entity="COUNTRY",
                    right_entity="CAPITAL",
                    rel_name="has_capital",
                    left_type="one-mandatory",
                    right_type="one-mandatory",
                    explanation="Each Country has mandatorily 1 Capital and each Capital belongs to exactly 1 Country.",
                    mapping_rule="Typically merged into 1 combined table or kept as 2 tables sharing a common Primary Key / FK with NOT NULL + UNIQUE.",
                )
                _renderConnectionRow(
                    label="0..1 ─── 0..1",
                    subtitle="Optional 1 to Optional 1",
                    left_entity="EMPLOYEE",
                    right_entity="PARKING_SPACE",
                    rel_name="assigned_space",
                    left_type="one-optional",
                    right_type="one-optional",
                    explanation="An employee may have 0 or 1 parking space, and a parking space may belong to 0 or 1 employee.",
                    mapping_rule="The Foreign Key is placed in either table with a UNIQUE constraint and allowing NULL values.",
                )

            # 1:N Relationships Group
            _renderRelationshipCategoryHeader("1:N — One-to-Many Relationships", "fa-sitemap", "text-emerald-400")
            with ui.column().classes("w-full space-y-3"):
                _renderConnectionRow(
                    label="1..1 ─── 0..N",
                    subtitle="Mandatory 1 to Optional Many (Classic 1:N)",
                    left_entity="DEPARTMENT",
                    right_entity="EMPLOYEE",
                    rel_name="employs",
                    left_type="one-mandatory",
                    right_type="many-optional",
                    explanation="A Department employs 0 to N Employees. Each Employee belongs mandatorily to exactly 1 Department.",
                    mapping_rule="The Primary Key of Department is placed as a Foreign Key in the EMPLOYEE table (the N side) and is NOT NULL.",
                )
                _renderConnectionRow(
                    label="0..1 ─── 0..N",
                    subtitle="Optional 1 to Optional Many",
                    left_entity="PROJECT",
                    right_entity="EMPLOYEE",
                    rel_name="assigned_to",
                    left_type="one-optional",
                    right_type="many-optional",
                    explanation="A Project may have 0 to many employees. An Employee may have 0 or at most 1 primary assigned project.",
                    mapping_rule="The Foreign Key is placed in the N-side table (EMPLOYEE) and is NULLABLE.",
                )
                _renderConnectionRow(
                    label="1..1 ─── 1..N",
                    subtitle="Mandatory 1 to Mandatory Many",
                    left_entity="ORDER",
                    right_entity="ORDER_ITEM",
                    rel_name="contains",
                    left_type="one-mandatory",
                    right_type="many-mandatory",
                    explanation="Each Order must contain at least 1 order item. Each order line item belongs to exactly 1 Order.",
                    mapping_rule="Foreign Key in the ORDER_ITEM table with NOT NULL and ON DELETE CASCADE constraints.",
                )

            # N:M Relationships Group
            _renderRelationshipCategoryHeader("N:M — Many-to-Many Relationships", "fa-network-wired", "text-amber-400")
            with ui.column().classes("w-full space-y-3"):
                _renderConnectionRow(
                    label="0..N ─── 0..N",
                    subtitle="Optional Many to Optional Many",
                    left_entity="STUDENT",
                    right_entity="COURSE",
                    rel_name="enrolled_in",
                    left_type="many-optional",
                    right_type="many-optional",
                    explanation="A Student enrolls in 0..N Courses. A Course is attended by 0..N Students.",
                    mapping_rule="A NEW junction table is created with composite Primary Key = (student_id, course_id).",
                )
                _renderConnectionRow(
                    label="1..N ─── 0..N",
                    subtitle="Mandatory Many to Optional Many",
                    left_entity="AUTHOR",
                    right_entity="BOOK",
                    rel_name="writes",
                    left_type="many-mandatory",
                    right_type="many-optional",
                    explanation="A Book must mandatorily have at least 1 Author (1..N). An Author may have written 0..N Books.",
                    mapping_rule="Junction table (author_id, book_id) with Foreign Keys referencing both participating tables.",
                )
                _renderConnectionRow(
                    label="1..N ─── 1..N",
                    subtitle="Mandatory Many to Mandatory Many",
                    left_entity="DOCTOR",
                    right_entity="PATIENT",
                    rel_name="treats",
                    left_type="many-mandatory",
                    right_type="many-mandatory",
                    explanation="Each Doctor treats at least 1 Patient, and each Patient is treated by at least 1 Doctor.",
                    mapping_rule="Junction table with business logic checks / triggers to guarantee minimum cardinality.",
                )

        # Special Architectural Relationship Patterns
        with ui.column().classes("w-full gap-4 mt-6"):
            ui.html('<h3 class="text-lg font-bold text-[#f4f1ea] m-0">Special Relationship Patterns & Advanced Architectures</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-3 gap-4 w-full"):
                # Pattern 1: Weak Entity / Identifying Relationship
                with ui.column().classes("p-5 rounded-xl bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-2"):
                    with ui.row().classes("items-center gap-2"):
                        ui.html('<i class="fa-solid fa-clone text-amber-400"></i>')
                        ui.label("Weak Entity & Identifying Relationship").classes("font-bold text-amber-300 text-sm")
                    ui.label(
                        "Identifying Relationship: The weak entity borrows the PK of its Owner entity. "
                        "Its composite PK is: (Owner_PK, Partial_Key)."
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
                        ui.label("Recursive (Unary) Relationships").classes("font-bold text-blue-300 text-sm")
                    ui.label(
                        "An entity relates to itself in different roles (e.g., Employee - Supervisor, Course - Prerequisite). "
                        "A self-referencing FK is added to the table schema."
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
                        ui.label("Ternary Relationships").classes("font-bold text-emerald-300 text-sm")
                    ui.label(
                        "Simultaneous association of 3 entities (e.g., Supplier, Project, Part). "
                        "ALWAYS transformed into a separate relational table with 3 Foreign Keys forming a composite key."
                    ).classes("text-xs text-[#b5b0a4] leading-relaxed")
                    ui.html(
                        """
                        <div class="p-2 rounded bg-[#141413] font-mono text-[11px] text-emerald-300">
                            PK: (supplier_id, project_id, part_id)
                        </div>
                        """
                    )


def _renderOfficialSymbolCard(
    title: str,
    display_name: str,
    svg_markup: str,
    desc: str,
    color_class: str,
) -> None:
    """Renders a card for the official reference connection types."""
    with ui.column().classes(
        f"p-4 rounded-xl bg-[#201f1d] border-t-4 {color_class} border border-[rgba(255,255,255,0.06)] gap-2 justify-between"
    ):
        with ui.column().classes("gap-1"):
            ui.label(title).classes("font-bold text-[#f4f1ea] text-sm")
            ui.label(display_name).classes("text-xs text-[#e06b3a] font-semibold")
        ui.html(svg_markup)
        ui.label(desc).classes("text-[11px] text-[#b5b0a4] leading-relaxed border-t border-[rgba(255,255,255,0.06)] pt-2")


def _renderEndpointCard(
    title: str,
    display_name: str,
    modality: str,
    cardinality: str,
    svg_markup: str,
    example: str,
    color_class: str,
) -> None:
    """Renders a single endpoint explanation card with embedded SVG visualization."""
    with ui.column().classes(f"p-4 rounded-xl bg-[#201f1d] border-t-4 {color_class} border border-[rgba(255,255,255,0.06)] gap-2"):
        ui.label(title).classes("font-bold text-[#f4f1ea] text-sm")
        ui.label(display_name).classes("text-xs text-[#e06b3a] font-semibold")

        ui.html(svg_markup)

        with ui.column().classes("gap-1 text-[11px] text-[#b5b0a4] border-t border-[rgba(255,255,255,0.06)] pt-2"):
            with ui.row().classes("justify-between w-full"):
                ui.label("Modality (Min):").classes("text-[#78756d]")
                ui.label(modality).classes("font-medium text-[#f4f1ea]")
            with ui.row().classes("justify-between w-full"):
                ui.label("Cardinality (Max):").classes("text-[#78756d]")
                ui.label(cardinality).classes("font-medium text-[#f4f1ea]")

        with ui.column().classes("bg-[#141413] p-2 rounded text-[11px] text-[#78756d] italic mt-1"):
            ui.label(f"Example: {example}")


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
            ui.label(f"Relationship: {rel_name}").classes("text-[11px] text-[#78756d] font-mono")

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
                ui.label("Relationship Interpretation:").classes("text-[#78756d] font-semibold text-[11px]")
                ui.label(explanation).classes("text-[#b5b0a4] leading-relaxed")

            with ui.column().classes("gap-1 bg-[#171615] p-2.5 rounded-lg border border-[rgba(255,255,255,0.04)]"):
                ui.label("Relational / SQL Conversion Rule:").classes("text-[#f59e0b] font-semibold text-[11px]")
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
        <circle cx="45" cy="20" r="5" fill="var(--svg-canvas-bg, #ffffff)" stroke="#e06b3a" stroke-width="2" class="svg-marker-circle" />
        """
    elif left_type == "many-optional":
        left_elements = """
        <line x1="15" y1="10" x2="35" y2="20" stroke="#e06b3a" stroke-width="2" />
        <line x1="15" y1="30" x2="35" y2="20" stroke="#e06b3a" stroke-width="2" />
        <circle cx="48" cy="20" r="5" fill="var(--svg-canvas-bg, #ffffff)" stroke="#e06b3a" stroke-width="2" class="svg-marker-circle" />
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
        <circle cx="175" cy="20" r="5" fill="var(--svg-canvas-bg, #ffffff)" stroke="#e06b3a" stroke-width="2" class="svg-marker-circle" />
        <line x1="190" y1="12" x2="190" y2="28" stroke="#e06b3a" stroke-width="2" />
        """
    elif right_type == "many-optional":
        right_elements = """
        <circle cx="172" cy="20" r="5" fill="var(--svg-canvas-bg, #ffffff)" stroke="#e06b3a" stroke-width="2" class="svg-marker-circle" />
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
                    "The 7 Golden Rules for ER-to-Relational Mapping (SQL DDL)"
                    "</h2>"
                )
                ui.label(
                    "The rigorous methodology for deriving tables, Primary Keys, Foreign Keys, and integrity constraints."
                ).classes("text-xs text-[#b5b0a4] mt-1")

        with ui.grid().classes("grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 w-full"):
            # Rule 1
            _renderRuleCard(
                number="1",
                title="Strong Entities",
                icon="fa-cube",
                color="border-blue-500",
                description="Each strong entity becomes a separate table. Simple attributes become columns, and the designated identifier is defined as the PRIMARY KEY.",
            )

            # Rule 2
            _renderRuleCard(
                number="2",
                title="Weak Entities",
                icon="fa-clone",
                color="border-amber-500",
                description="Becomes a table containing all its simple attributes plus the Primary Key of the owner entity (Owner FK). The PRIMARY KEY is COMPOSITE: (Owner_PK, Partial_Key).",
            )

            # Rule 3
            _renderRuleCard(
                number="3",
                title="1:1 Relationships",
                icon="fa-arrows-left-right",
                color="border-emerald-500",
                description="The PK of one table is imported as a Foreign Key into the other. Prefer the table with total (mandatory) participation. The Foreign Key is defined as UNIQUE and NOT NULL.",
            )

            # Rule 4
            _renderRuleCard(
                number="4",
                title="1:N Relationships",
                icon="fa-sitemap",
                color="border-[#e06b3a]",
                description="The Primary Key of the '1' side is imported as a Foreign Key into the table on the 'N' side. If participation on the N side is total, the FK is defined as NOT NULL.",
            )

            # Rule 5
            _renderRuleCard(
                number="5",
                title="N:M Relationships",
                icon="fa-network-wired",
                color="border-rose-500",
                description="A NEW independent junction table is created. It includes as Foreign Keys the PKs of both participating entities plus any relationship attributes. PRIMARY KEY = (FK1, FK2).",
            )

            # Rule 6
            _renderRuleCard(
                number="6",
                title="Multivalued Attributes",
                icon="fa-tags",
                color="border-purple-500",
                description="Each multivalued attribute (e.g., multiple phone numbers, facility locations) becomes a new table with: Entity_PK + Attribute_Value column. PRIMARY KEY = (Entity_PK, Attribute_Value).",
            )

            # Rule 7
            _renderRuleCard(
                number="7",
                title="Composite Attributes",
                icon="fa-layer-group",
                color="border-teal-500",
                description="Decomposed into their atomic simple sub-attributes (e.g., Address -> street, number, postal_code, city). The composite attribute itself is not retained as a separate column.",
            )


def _renderRuleCard(number: str, title: str, icon: str, color: str, description: str) -> None:
    """Renders a single rule card in the 7 golden rules grid."""
    with ui.column().classes(f"p-5 rounded-xl bg-[#201f1d] border-l-4 {color} border border-[rgba(255,255,255,0.06)] gap-2"):
        with ui.row().classes("items-center justify-between w-full"):
            with ui.row().classes("items-center gap-2"):
                ui.html(f'<i class="fa-solid {icon} text-sm text-[#e06b3a]"></i>')
                ui.label(title).classes("font-bold text-[#f4f1ea] text-xs")
            ui.label(f"Rule {number}").classes("text-[10px] font-mono text-[#78756d] bg-[#141413] px-2 py-0.5 rounded")
        ui.label(description).classes("text-xs text-[#b5b0a4] leading-relaxed")


def _renderNotationComparisonSection() -> None:
    """Renders a comparative table between Crow's Foot, Chen, and Min-Max notations."""
    with ui.column().classes("w-full glass-panel p-6 md:p-8 rounded-2xl gap-4"):
        with ui.row().classes("items-center gap-3 border-b border-[rgba(255,255,255,0.08)] pb-4"):
            ui.html('<i class="fa-solid fa-code-compare text-blue-400 text-2xl"></i>')
            with ui.column().classes("gap-0"):
                ui.html(
                    '<h2 class="text-xl md:text-2xl font-bold text-[#f4f1ea] m-0">'
                    "Notation Comparison Matrix (Crow's Foot vs Chen vs Min-Max)"
                    "</h2>"
                )
                ui.label(
                    "Reference mapping for recognizing exam problems across diverse ER modeling notations."
                ).classes("text-xs text-[#b5b0a4] mt-1")

        comparison_table = """
        <div class="overflow-x-auto w-full">
            <table class="dark-table">
                <thead>
                    <tr>
                        <th style="width: 25%;">Concept / Type</th>
                        <th style="width: 25%;">Crow's Foot (Martin)</th>
                        <th style="width: 25%;">Classical ER (Peter Chen)</th>
                        <th style="width: 25%;">Min-Max Notation</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="font-bold text-[#f4f1ea]">Entity</td>
                        <td>Rectangle box with attribute list</td>
                        <td>Simple Rectangle</td>
                        <td>Rectangle</td>
                    </tr>
                    <tr>
                        <td class="font-bold text-[#f4f1ea]">Weak Entity</td>
                        <td>Rounded rectangle or PK note</td>
                        <td>Double Rectangle</td>
                        <td>Double Rectangle</td>
                    </tr>
                    <tr>
                        <td class="font-bold text-[#f4f1ea]">Relationship</td>
                        <td>Straight line with endpoint symbols</td>
                        <td>Diamond between entities</td>
                        <td>Diamond with (min, max) labels</td>
                    </tr>
                    <tr>
                        <td class="font-bold text-[#f4f1ea]">Primary Key (PK)</td>
                        <td>[PK] tag or underlined in table</td>
                        <td>Underlined text inside Ellipse</td>
                        <td>Underlined attribute</td>
                    </tr>
                    <tr>
                        <td class="font-bold text-[#f4f1ea]">Partial Key (Discriminator)</td>
                        <td>[Partial Key] tag</td>
                        <td>Dashed underline inside Ellipse</td>
                        <td>Dashed underline</td>
                    </tr>
                    <tr>
                        <td class="font-bold text-[#f4f1ea]">Optional One (0..1)</td>
                        <td>Circle and Vertical Bar (O |)</td>
                        <td>Single line (1) and partial participation</td>
                        <td>(0, 1) on participating entity side</td>
                    </tr>
                    <tr>
                        <td class="font-bold text-[#f4f1ea]">Mandatory One (1..1)</td>
                        <td>Two Vertical Bars (| |)</td>
                        <td>Double line (1) or total participation</td>
                        <td>(1, 1) on participating entity side</td>
                    </tr>
                    <tr>
                        <td class="font-bold text-[#f4f1ea]">Optional Many (0..N)</td>
                        <td>Circle and Fork (O &lt;)</td>
                        <td>Single line with N / M tag</td>
                        <td>(0, N) on participating entity side</td>
                    </tr>
                    <tr>
                        <td class="font-bold text-[#f4f1ea]">Mandatory Many (1..N)</td>
                        <td>Vertical Bar and Fork (| &lt;)</td>
                        <td>Double line with N / M tag</td>
                        <td>(1, N) on participating entity side</td>
                    </tr>
                </tbody>
            </table>
        </div>
        """
        ui.html(comparison_table)
