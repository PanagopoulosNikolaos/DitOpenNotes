"""Interactive exam paper canvas component with dynamic category filtering and tooltips."""

from nicegui import ui
from models.scenario import Scenario


def renderInteractiveCanvas(scenario: Scenario) -> None:
    """Renders the interactive problem description canvas with category filters and legend.

    Args:
        scenario (Scenario): The active scenario containing full verbatim exam text.

    Returns:
        None
    """
    paragraphs_html_list = []
    for p in scenario.paragraphs:
        border_style = (
            "border-left: 3px solid var(--accent); padding-left: 14px; margin: 14px 0;"
            if p.accent_border_color
            else "margin: 12px 0;"
        )
        segments_html = []
        for seg in p.segments:
            if not seg.is_highlight:
                segments_html.append(seg.text)
            else:
                tooltip_attr = f'title="{seg.tooltip}"' if seg.tooltip else ""
                tag_html = (
                    f'<span class="tag-label">{seg.tag_label}</span>'
                    if seg.tag_label
                    else ""
                )
                badge_cls = seg.badge_class if seg.badge_class else f"badge-{seg.category}"
                seg_html = (
                    f'<span class="highlight-badge {badge_cls}" '
                    f'data-category="{seg.category}" {tooltip_attr}>'
                    f'<span>{seg.text}</span>{tag_html}</span>'
                )
                segments_html.append(seg_html)
        paragraphs_html_list.append(
            f'<p style="{border_style}" class="leading-relaxed m-0">{"".join(segments_html)}</p>'
        )

    full_canvas_body_html = "".join(paragraphs_html_list)

    with ui.column().classes("w-full glass-panel gap-0 p-0 overflow-hidden border border-[var(--border-accent)]"):
        # Header with filters
        with ui.column().classes(
            "w-full bg-[var(--canvas-header-bg)] p-5 gap-3 border-b border-[var(--border)]"
        ):
            with ui.row().classes("w-full justify-between items-center flex-wrap gap-4"):
                with ui.column().classes("gap-1"):
                    with ui.row().classes("items-center gap-2"):
                        ui.html('<i class="fa-solid fa-highlighter text-[var(--accent)] text-lg"></i>')
                        ui.html('<h2 class="text-lg md:text-xl font-bold text-[var(--text-1)] m-0">Διαδραστικό Canvas Πλήρους Εκφώνησης Εξέτασης</h2>')
                    ui.label(
                        "Αυτούσιο κείμενο της εξέτασης με διαδραστική επισήμανση. Πλησιάστε τον δείκτη (hover) για ανάλυση 3 σημείων."
                    ).classes("text-xs text-[var(--text-2)]")

                # Whitelist Control: Canvas Category Filter Chips
                with ui.row().classes("items-center gap-2 flex-wrap text-xs"):
                    ui.html(
                        """
                        <button onclick="setFilterMode('all')" class="filter-chip-btn active" data-filter="all" title="Εμφάνιση όλων των επισημάνσεων">
                            <i class="fa-solid fa-layer-group"></i> Όλα
                        </button>
                        <button onclick="setFilterMode('clean')" class="filter-chip-btn" data-filter="clean" title="Καθαρό κείμενο χωρίς επισημάνσεις">
                            <i class="fa-solid fa-file-lines"></i> Καθαρό Κείμενο
                        </button>
                        <button onclick="toggleCategory('binary')" class="filter-chip-btn active" data-category="binary" title="Δυαδική Αριθμητική & Συμπληρώματα">
                            <i class="fa-solid fa-binary text-blue-500"></i> Δυαδικά (C2, Bits)
                        </button>
                        <button onclick="toggleCategory('boolean')" class="filter-chip-btn active" data-category="boolean" title="Άλγεβρα Boole & Χάρτες K-Map">
                            <i class="fa-solid fa-diagram-project text-orange-500"></i> Boole & K-Map
                        </button>
                        <button onclick="toggleCategory('fsm')" class="filter-chip-btn active" data-category="fsm" title="Ακολουθιακά Κυκλώματα, FF & FSM">
                            <i class="fa-solid fa-arrows-spin text-purple-500"></i> FSM & Μετρητές
                        </button>
                        <button onclick="toggleCategory('vhdl')" class="filter-chip-btn active" data-category="vhdl" title="Περιγραφή Υλικού σε VHDL">
                            <i class="fa-solid fa-code text-emerald-500"></i> VHDL & MSI
                        </button>
                        <button onclick="toggleCategory('param')" class="filter-chip-btn active" data-category="param" title="Παράμετροι & Περιορισμοί">
                            <i class="fa-solid fa-sliders text-amber-500"></i> Περιορισμοί
                        </button>
                        """,
                        tag="div",
                    )

            # Legend bar
            with ui.row().classes(
                "w-full pt-2 border-t border-[var(--border)] items-center gap-4 text-xs text-[var(--text-3)] flex-wrap"
            ):
                ui.html('<span><strong class="text-[var(--text-1)]">Υπόμνημα Χρωμάτων:</strong></span>')
                ui.html('<span class="flex items-center gap-1.5"><span class="w-2.5 h-2.5 rounded-full bg-blue-500"></span> Δυαδική Αριθμητική</span>')
                ui.html('<span class="flex items-center gap-1.5"><span class="w-2.5 h-2.5 rounded-full bg-orange-500"></span> Boole & K-Map</span>')
                ui.html('<span class="flex items-center gap-1.5"><span class="w-2.5 h-2.5 rounded-full bg-purple-500"></span> FSM & Flip-Flops</span>')
                ui.html('<span class="flex items-center gap-1.5"><span class="w-2.5 h-2.5 rounded-full bg-emerald-500"></span> VHDL & MSI</span>')
                ui.html('<span class="flex items-center gap-1.5"><span class="w-2.5 h-2.5 rounded-full bg-amber-500"></span> Περιορισμοί</span>')

        # Canvas Body Container
        with ui.column().classes("w-full p-6 text-sm text-[var(--text-1)] leading-relaxed bg-[var(--canvas-bg)]"):
            ui.html(
                f'<div id="interactive-text-canvas" class="space-y-4 latex-target">{full_canvas_body_html}</div>',
                tag="div",
            )

