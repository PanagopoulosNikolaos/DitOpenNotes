"""Interactive SVG state transition diagram and logic circuit viewer component with pan, zoom, and detail toggle."""

from nicegui import ui
from models.scenario import Scenario


def renderVisualDiagram(scenario: Scenario) -> None:
    """Renders the interactive SVG diagram for FSM state transitions or digital circuits.

    Args:
        scenario (Scenario): The active scenario containing diagram specifications.

    Returns:
        None
    """
    custom_svg_content = scenario.diagram_svg_custom if scenario.diagram_svg_custom else generateDefaultFsmSvg()

    with ui.column().classes("w-full glass-panel gap-4 p-6 border border-[var(--border)]").props('id="visual-diagram-section"'):
        # Header with whitelist controls
        with ui.row().classes("w-full justify-between items-center flex-wrap gap-4 border-b border-[var(--border)] pb-4"):
            with ui.column().classes("gap-1"):
                with ui.row().classes("items-center gap-2"):
                    ui.html('<i class="fa-solid fa-diagram-project text-[var(--accent)] text-xl no-print"></i>')
                    ui.html('<h2 class="text-xl font-bold text-[var(--text-1)] m-0">Διαδραστικό Διάγραμμα Καταστάσεων FSM / Μετρητή (SVG)</h2>')
                ui.label(
                    "Διάγραμμα μεταβάσεων καταστάσεων, ακμών διεγέρσεων και βρόχων αυτοδιόρθωσης. Υποστηρίζει Drag Pan, Scroll Zoom και εμφάνιση λεπτομερειών."
                ).classes("text-xs text-[var(--text-2)] no-print")

            # Whitelist Controls: Pan/Zoom/Reset/Toggle buttons
            with ui.row().classes("items-center gap-2 flex-wrap text-xs no-print"):
                ui.html(
                    """
                    <button onclick="zoomDeDiagram(1.2)" class="filter-chip-btn" title="Μεγέθυνση">
                        <i class="fa-solid fa-magnifying-glass-plus"></i> Μεγέθυνση
                    </button>
                    <button onclick="zoomDeDiagram(0.8)" class="filter-chip-btn" title="Σμίκρυνση">
                        <i class="fa-solid fa-magnifying-glass-minus"></i> Σμίκρυνση
                    </button>
                    <button onclick="resetDeDiagramZoom()" class="filter-chip-btn" title="Επαναφορά Κλίμακας">
                        <i class="fa-solid fa-arrows-to-dot"></i> Επαναφορά
                    </button>
                    <button onclick="toggleDeDiagramDetails()" id="toggle-de-details-btn" class="filter-chip-btn active" title="Εμφάνιση/Απόκρυψη Λεπτομερειών">
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
                    <span class="flex items-center gap-1.5"><span class="w-3 h-3 rounded-full bg-[var(--accent)]"></span> Έγκυρες Καταστάσεις</span>
                    <span class="flex items-center gap-1.5"><span class="w-3 h-3 rounded-full bg-emerald-500"></span> Επιτυχής Ανίχνευση / Έξοδος 1</span>
                    <span class="flex items-center gap-1.5"><span class="w-3 h-3 rounded-full bg-red-500"></span> Don't Care / Unused States</span>
                    <span class="h-3 w-px bg-[var(--border)]"></span>
                    <span class="font-mono text-xs text-[var(--accent)] font-bold">Synchronous Clock Driven</span>
                </div>
                <div class="absolute bottom-3 right-3 z-10 bg-[var(--header-bg)] backdrop-blur-sm text-[var(--text-3)] px-3 py-1.5 rounded-lg text-xs flex items-center gap-2 border border-[var(--border)] no-print shadow-sm">
                    <i class="fa-solid fa-hand-pointer text-[var(--accent)]"></i> Drag για κύλιση • Scroll για Zoom
                </div>
                """
            )

            ui.html(
                f"""
                <div id="de-diagram-viewport" class="w-full h-[450px] overflow-hidden cursor-grab flex items-center justify-center"
                     onmousedown="startDeDrag(event)" onwheel="handleDeWheel(event)">
                    <div id="de-diagram-layer" style="transform-origin: center center; transition: transform 0.05s ease-out;">
                        {custom_svg_content}
                    </div>
                </div>
                """,
                tag="div",
            )


def generateDefaultFsmSvg() -> str:
    """Generates the standard fallback state diagram SVG.

    Returns:
        str: Fallback SVG markup.
    """
    return """
    <svg width="800" height="300" viewBox="0 0 800 300" xmlns="http://www.w3.org/2000/svg">
        <circle cx="200" cy="150" r="40" fill="var(--svg-fill)" stroke="var(--accent)" stroke-width="3" />
        <circle cx="600" cy="150" r="40" fill="var(--svg-fill)" stroke="var(--accent)" stroke-width="3" />
        <text x="200" y="155" text-anchor="middle" font-family="Outfit, sans-serif" font-size="16" fill="var(--text-1)">S0</text>
        <text x="600" y="155" text-anchor="middle" font-family="Outfit, sans-serif" font-size="16" fill="var(--text-1)">S1</text>
    </svg>
    """

