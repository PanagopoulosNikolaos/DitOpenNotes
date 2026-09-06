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
                        "Αυτούσιο κείμενο της εξέτασης με διαδραστική επισήμανση. Πλησιάστε τον δείκτη (hover) για πλήρη ανάλυση 3 σημείων."
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
                        <button onclick="toggleCategory('field')" class="filter-chip-btn active" data-category="field" title="Πεδία & Μετατοπίσεις">
                            <i class="fa-solid fa-compass text-blue-500"></i> Πεδία (E, B, D, H)
                        </button>
                        <button onclick="toggleCategory('param')" class="filter-chip-btn active" data-category="param" title="Σταθερές & Παράμετροι">
                            <i class="fa-solid fa-sliders text-orange-500"></i> Παράμετροι (c, ω, λ, k)
                        </button>
                        <button onclick="toggleCategory('calc')" class="filter-chip-btn active" data-category="calc" title="Τελεστές & Ροή Ενέργειας">
                            <i class="fa-solid fa-calculator text-purple-500"></i> Τελεστές & Poynting
                        </button>
                        <button onclick="toggleCategory('law')" class="filter-chip-btn active" data-category="law" title="Φυσικοί Νόμοι & Αρχές">
                            <i class="fa-solid fa-scale-balanced text-emerald-500"></i> Νόμοι Maxwell
                        </button>
                        <button onclick="toggleCategory('geom')" class="filter-chip-btn active" data-category="geom" title="Γεωμετρία & Συντεταγμένες">
                            <i class="fa-solid fa-shapes text-amber-500"></i> Γεωμετρία (x, y, z)
                        </button>
                        """,
                        tag="div",
                    )

            # Legend bar
            with ui.row().classes(
                "w-full pt-2 border-t border-[var(--border)] items-center gap-4 text-xs text-[var(--text-3)] flex-wrap"
            ):
                ui.html('<span><strong class="text-[var(--text-1)]">Υπόμνημα Χρωμάτων:</strong></span>')
                ui.html('<span class="flex items-center gap-1.5"><span class="w-2.5 h-2.5 rounded-full bg-blue-500"></span> Πεδία</span>')
                ui.html('<span class="flex items-center gap-1.5"><span class="w-2.5 h-2.5 rounded-full bg-orange-500"></span> Παράμετροι</span>')
                ui.html('<span class="flex items-center gap-1.5"><span class="w-2.5 h-2.5 rounded-full bg-purple-500"></span> Τελεστές / S</span>')
                ui.html('<span class="flex items-center gap-1.5"><span class="w-2.5 h-2.5 rounded-full bg-emerald-500"></span> Νόμοι Maxwell</span>')
                ui.html('<span class="flex items-center gap-1.5"><span class="w-2.5 h-2.5 rounded-full bg-amber-500"></span> Γεωμετρία</span>')

        # Canvas Body Container
        with ui.column().classes("w-full p-6 text-sm text-[var(--text-1)] leading-relaxed bg-[var(--canvas-bg)]"):
            ui.html(
                f'<div id="interactive-text-canvas" class="space-y-4 latex-target">{full_canvas_body_html}</div>',
                tag="div",
            )

