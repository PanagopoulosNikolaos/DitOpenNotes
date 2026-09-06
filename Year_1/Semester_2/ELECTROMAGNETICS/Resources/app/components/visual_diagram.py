"""Interactive SVG field and wave diagram viewer component with pan, zoom, and detail toggle."""

from nicegui import ui
from models.scenario import Scenario


def renderVisualDiagram(scenario: Scenario) -> None:
    """Renders the interactive SVG vector diagram for electromagnetic fields and waves.

    Args:
        scenario (Scenario): The active scenario containing diagram specifications.

    Returns:
        None
    """
    custom_svg_content = scenario.diagram_svg_custom if scenario.diagram_svg_custom else generateDefaultWaveSvg()

    with ui.column().classes("w-full glass-panel gap-4 p-6 border border-[var(--border)]").props('id="visual-diagram-section"'):
        # Header with whitelist controls
        with ui.row().classes("w-full justify-between items-center flex-wrap gap-4 border-b border-[var(--border)] pb-4"):
            with ui.column().classes("gap-1"):
                with ui.row().classes("items-center gap-2"):
                    ui.html('<i class="fa-solid fa-wave-square text-[var(--accent)] text-xl no-print"></i>')
                    ui.html('<h2 class="text-xl font-bold text-[var(--text-1)] m-0">Διαδραστικό Διάγραμμα Πεδίων & ΗΜ Κύματος (SVG)</h2>')
                ui.label(
                    "Τρισδιάστατη προβολή εγκάρσιου κύματος (E, B, k) και διανύσματος Poynting S. Υποστηρίζει Pan, Zoom και εναλλαγή λεπτομερειών."
                ).classes("text-xs text-[var(--text-2)] no-print")

            # Whitelist Controls: Pan/Zoom/Reset/Toggle buttons
            with ui.row().classes("items-center gap-2 flex-wrap text-xs no-print"):
                ui.html(
                    """
                    <button onclick="zoomEmDiagram(1.2)" class="filter-chip-btn" title="Μεγέθυνση">
                        <i class="fa-solid fa-magnifying-glass-plus"></i> Μεγέθυνση
                    </button>
                    <button onclick="zoomEmDiagram(0.8)" class="filter-chip-btn" title="Σμίκρυνση">
                        <i class="fa-solid fa-magnifying-glass-minus"></i> Σμίκρυνση
                    </button>
                    <button onclick="resetEmDiagramZoom()" class="filter-chip-btn" title="Επαναφορά Κλίμακας">
                        <i class="fa-solid fa-arrows-to-dot"></i> Επαναφορά
                    </button>
                    <button onclick="toggleEmDiagramDetails()" id="toggle-em-details-btn" class="filter-chip-btn active" title="Εμφάνιση/Απόκρυψη Λεπτομερειών">
                        <i class="fa-solid fa-eye"></i> Λεπτομέρειες
                    </button>
                    """,
                    sanitize=False,
                )

        # SVG Container with Drag & Wheel handlers
        with ui.element("div").classes(
            "relative w-full rounded-2xl overflow-hidden border border-[var(--border-accent)] bg-[var(--svg-canvas-bg)] shadow-inner"
        ):
            # Top Legend Overlay
            ui.html(
                """
                <div class="absolute top-3 left-3 z-10 bg-[var(--header-bg)] backdrop-blur-md text-[var(--text-1)] p-2.5 rounded-xl border border-[var(--border)] text-xs flex flex-wrap items-center gap-3 no-print shadow-md">
                    <span class="flex items-center gap-1.5"><span class="w-3 h-3 rounded-full bg-blue-500"></span> Ηλεκτρικό Πεδίο E (y)</span>
                    <span class="flex items-center gap-1.5"><span class="w-3 h-3 rounded-full bg-orange-500"></span> Μαγνητικό Πεδίο B (z)</span>
                    <span class="flex items-center gap-1.5"><span class="w-3 h-3 rounded-full bg-emerald-500"></span> Διάδοση k / Poynting S (x)</span>
                    <span class="h-3 w-px bg-[var(--border)]"></span>
                    <span class="font-mono text-xs text-[var(--accent)] font-bold">E ⟂ B ⟂ k</span>
                </div>
                <div class="absolute bottom-3 right-3 z-10 bg-[var(--header-bg)] backdrop-blur-sm text-[var(--text-3)] px-3 py-1.5 rounded-lg text-xs flex items-center gap-2 border border-[var(--border)] no-print shadow-sm">
                    <i class="fa-solid fa-hand-pointer text-[var(--accent)]"></i> Drag για κύλιση • Scroll για Zoom
                </div>
                """
            )

            ui.html(
                f"""
                <div id="em-diagram-viewport" class="w-full h-[450px] overflow-hidden cursor-grab flex items-center justify-center"
                     onmousedown="startEmDrag(event)" onwheel="handleEmWheel(event)">
                    <div id="em-diagram-layer" style="transform-origin: center center; transition: transform 0.05s ease-out;">
                        {custom_svg_content}
                    </div>
                </div>
                """,
                tag="div",
            )


def generateDefaultWaveSvg() -> str:
    """Generates the standard 3D isometric plane EM wave SVG.

    Returns:
        str: Scalable vector graphic markup for orthogonal harmonic wave.
    """
    return """
    <svg width="860" height="420" viewBox="0 0 860 420" xmlns="http://www.w3.org/2000/svg" class="select-none">
        <defs>
            <marker id="arrow-blue" markerWidth="8" markerHeight="8" refX="5" refY="3" orient="auto">
                <path d="M0,0 L0,6 L7,3 z" fill="#3b82f6" />
            </marker>
            <marker id="arrow-orange" markerWidth="8" markerHeight="8" refX="5" refY="3" orient="auto">
                <path d="M0,0 L0,6 L7,3 z" fill="#ea580c" />
            </marker>
            <marker id="arrow-green" markerWidth="10" markerHeight="10" refX="7" refY="3" orient="auto">
                <path d="M0,0 L0,6 L8,3 z" fill="#10b981" />
            </marker>
            <linearGradient id="wave-e-grad" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#3b82f6" stop-opacity="0.35"/>
                <stop offset="100%" stop-color="#3b82f6" stop-opacity="0.0"/>
            </linearGradient>
            <linearGradient id="wave-b-grad" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#f97316" stop-opacity="0.30"/>
                <stop offset="100%" stop-color="#f97316" stop-opacity="0.0"/>
            </linearGradient>
        </defs>

        <!-- Coordinate Axes -->
        <!-- Propagation Axis (z / x) -->
        <line x1="80" y1="210" x2="780" y2="210" stroke="var(--svg-stroke)" stroke-width="2" stroke-dasharray="4 4" />
        <line x1="720" y1="210" x2="800" y2="210" stroke="#10b981" stroke-width="4" marker-end="url(#arrow-green)" />
        <text x="815" y="215" font-family="Outfit, sans-serif" font-weight="bold" font-size="14" fill="#10b981">+k, +S (Διάδοση)</text>

        <!-- Vertical E-axis (y) -->
        <line x1="120" y1="360" x2="120" y2="60" stroke="#3b82f6" stroke-width="2" marker-end="url(#arrow-blue)" />
        <text x="110" y="45" font-family="Outfit, sans-serif" font-weight="bold" font-size="14" fill="#3b82f6">+E (y)</text>

        <!-- Oblique B-axis (x / z) -->
        <line x1="120" y1="210" x2="30" y2="300" stroke="#ea580c" stroke-width="2" marker-end="url(#arrow-orange)" />
        <text x="15" y="320" font-family="Outfit, sans-serif" font-weight="bold" font-size="14" fill="#ea580c">+B (z)</text>

        <!-- Sinusoidal Electric Wave Envelope (Vertical Oscillation) -->
        <!-- Cycle 1 Positive -->
        <path d="M 120 210 Q 180 80 240 210 Q 300 340 360 210 Q 420 80 480 210 Q 540 340 600 210 Q 660 80 720 210"
              fill="none" stroke="#3b82f6" stroke-width="3.5" />

        <!-- Vertical E-Field Vectors along propagation -->
        <!-- Peak 1 Positive (x=180) -->
        <line x1="180" y1="210" x2="180" y2="105" stroke="#3b82f6" stroke-width="2" marker-end="url(#arrow-blue)" />
        <line x1="150" y1="210" x2="150" y2="140" stroke="#3b82f6" stroke-width="1.5" marker-end="url(#arrow-blue)" />
        <line x1="210" y1="210" x2="210" y2="140" stroke="#3b82f6" stroke-width="1.5" marker-end="url(#arrow-blue)" />
        <text x="185" y="95" font-family="JetBrains Mono, monospace" font-size="11" font-weight="bold" fill="#3b82f6" class="em-diagram-detail">E₀</text>

        <!-- Peak 1 Negative (x=300) -->
        <line x1="300" y1="210" x2="300" y2="315" stroke="#3b82f6" stroke-width="2" marker-end="url(#arrow-blue)" />
        <line x1="270" y1="210" x2="270" y2="280" stroke="#3b82f6" stroke-width="1.5" marker-end="url(#arrow-blue)" />
        <line x1="330" y1="210" x2="330" y2="280" stroke="#3b82f6" stroke-width="1.5" marker-end="url(#arrow-blue)" />

        <!-- Peak 2 Positive (x=420) -->
        <line x1="420" y1="210" x2="420" y2="105" stroke="#3b82f6" stroke-width="2" marker-end="url(#arrow-blue)" />
        <!-- Peak 2 Negative (x=540) -->
        <line x1="540" y1="210" x2="540" y2="315" stroke="#3b82f6" stroke-width="2" marker-end="url(#arrow-blue)" />
        <!-- Peak 3 Positive (x=660) -->
        <line x1="660" y1="210" x2="660" y2="105" stroke="#3b82f6" stroke-width="2" marker-end="url(#arrow-blue)" />

        <!-- Sinusoidal Magnetic Wave Envelope (Oblique / Transverse Oscillation) -->
        <!-- Projections with skew along isometric plane -->
        <path d="M 120 210 Q 165 270 240 210 Q 315 150 360 210 Q 405 270 480 210 Q 555 150 600 210 Q 645 270 720 210"
              fill="none" stroke="#ea580c" stroke-width="3" stroke-dasharray="7 3" />

        <!-- Oblique B-Field Vectors -->
        <line x1="180" y1="210" x2="140" y2="255" stroke="#ea580c" stroke-width="2" marker-end="url(#arrow-orange)" />
        <line x1="300" y1="210" x2="340" y2="165" stroke="#ea580c" stroke-width="2" marker-end="url(#arrow-orange)" />
        <line x1="420" y1="210" x2="380" y2="255" stroke="#ea580c" stroke-width="2" marker-end="url(#arrow-orange)" />
        <line x1="540" y1="210" x2="580" y2="165" stroke="#ea580c" stroke-width="2" marker-end="url(#arrow-orange)" />
        <line x1="660" y1="210" x2="620" y2="255" stroke="#ea580c" stroke-width="2" marker-end="url(#arrow-orange)" />
        <text x="120" y="275" font-family="JetBrains Mono, monospace" font-size="11" font-weight="bold" fill="#ea580c" class="em-diagram-detail">B₀</text>

        <!-- Wavelength Dimension Line λ (from x=120 to x=360) -->
        <g class="em-diagram-detail">
            <line x1="120" y1="365" x2="360" y2="365" stroke="var(--text-3)" stroke-width="1.5" />
            <line x1="120" y1="355" x2="120" y2="375" stroke="var(--text-3)" stroke-width="1.5" />
            <line x1="360" y1="355" x2="360" y2="375" stroke="var(--text-3)" stroke-width="1.5" />
            <text x="230" y="385" text-anchor="middle" font-family="Outfit, sans-serif" font-weight="bold" font-size="13" fill="var(--text-1)">Μήκος Κύματος λ = 2π / k</text>
        </g>
    </svg>
    """

