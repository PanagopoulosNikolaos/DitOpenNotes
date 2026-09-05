"""Interactive problem description canvas component with dynamic category filtering."""

from nicegui import ui
from models.scenario import NetworkScenario


def renderInteractiveCanvas(scenario: NetworkScenario) -> None:
    """Renders the interactive problem description canvas with category filters.

    Args:
        scenario (NetworkScenario): The active scenario containing paragraphs and highlights.

    Returns:
        None
    """
    paragraphs_html_list = []
    for p in scenario.paragraphs:
        border_style = (
            "border-left: 3px solid #e06b3a; padding-left: 14px; margin: 16px 0;"
            if p.accent_border_color
            else "margin: 16px 0;"
        )
        segments_html = []
        for seg in p.segments:
            if not seg.is_highlight:
                segments_html.append(seg.text)
            else:
                tooltip_attr = f'title="{seg.tooltip}"' if seg.tooltip else ""
                tag_html = (
                    f'<span class="tag-pill">{seg.tag_label}</span>'
                    if seg.tag_label
                    else ""
                )
                badge_cls = seg.badge_class if seg.badge_class else f"hl-{seg.category}"
                seg_html = (
                    f'<span class="highlight-badge {badge_cls} highlight-active" '
                    f'data-category="{seg.category}" data-badge-class="{badge_cls}" {tooltip_attr}>'
                    f'<span>{seg.text}</span>{tag_html}</span>'
                )
                segments_html.append(seg_html)
        paragraphs_html_list.append(
            f'<p style="{border_style}" class="leading-relaxed m-0">{"".join(segments_html)}</p>'
        )

    full_canvas_body_html = "".join(paragraphs_html_list)

    with ui.column().classes("w-full glass-panel gap-0 p-0 overflow-hidden border border-[rgba(224,107,58,0.25)]"):
        # Header with filters
        with ui.row().classes(
            "w-full bg-[#121211] p-5 justify-between items-center flex-wrap gap-4 border-b border-[rgba(255,255,255,0.08)]"
        ):
            with ui.column().classes("gap-1"):
                with ui.row().classes("items-center gap-2"):
                    ui.html('<i class="fa-solid fa-highlighter text-[#f59e0b] text-lg"></i>')
                    ui.html('<h2 class="text-lg md:text-xl font-bold text-[#f4f1ea] m-0">Διαδραστικό Canvas Εκφώνησης & Παραμέτρων</h2>')
                ui.label(
                    "Επιλέξτε φίλτρα κατηγορίας για δυναμική επισήμανση παραμέτρων καθυστέρησης, συσκευών, πρωτοκόλλων και αλγορίθμων."
                ).classes("text-xs text-[#78756d]")

            # Interactive Filter Buttons
            with ui.row().classes("items-center gap-2 flex-wrap text-xs"):
                ui.html(
                    """
                    <button onclick="setFilterMode('all')" class="filter-chip active" data-filter="all" title="Εμφάνιση όλων των επισημάνσεων">
                        <i class="fa-solid fa-layer-group"></i> Όλα
                    </button>
                    <button onclick="setFilterMode('none')" class="filter-chip" data-filter="none" title="Καθαρό κείμενο χωρίς επισημάνσεις">
                        <i class="fa-solid fa-file-lines"></i> Καθαρό Κείμενο
                    </button>
                    <button onclick="toggleCategory('delay')" class="filter-chip active" data-category="delay" title="Καθυστερήσεις & Μεγέθη">
                        <i class="fa-solid fa-stopwatch text-orange-400"></i> Καθυστερήσεις
                    </button>
                    <button onclick="toggleCategory('device')" class="filter-chip active" data-category="device" title="Συσκευές & Τοπολογίες">
                        <i class="fa-solid fa-server text-amber-400"></i> Συσκευές
                    </button>
                    <button onclick="toggleCategory('protocol')" class="filter-chip active" data-category="protocol" title="Πρωτόκολλα & Επίπεδα">
                        <i class="fa-solid fa-diagram-project text-blue-400"></i> Πρωτόκολλα
                    </button>
                    <button onclick="toggleCategory('routing')" class="filter-chip active" data-category="routing" title="Δρομολόγηση & Μεταγωγή">
                        <i class="fa-solid fa-route text-emerald-400"></i> Δρομολόγηση
                    </button>
                    <button onclick="toggleCategory('error_check')" class="filter-chip active" data-category="error_check" title="Έλεγχος Σφαλμάτων & CRC">
                        <i class="fa-solid fa-shield-halved text-red-400"></i> Έλεγχος Σφαλμάτων
                    </button>
                    """,
                    tag="div",
                )

        # Canvas Body Container
        with ui.column().classes("w-full p-6 text-sm text-[#f4f1ea] leading-relaxed bg-[#1c1b1a]"):
            ui.html(
                f'<div id="interactive-text-canvas" class="space-y-4">{full_canvas_body_html}</div>',
                tag="div",
            )

    # Canvas filter JS is loaded once globally via config.KATEX_HEAD_HTML (no per-render injection needed).
