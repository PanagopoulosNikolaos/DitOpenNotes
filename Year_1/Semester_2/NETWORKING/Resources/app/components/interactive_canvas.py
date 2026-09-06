"""Interactive exam paper canvas component with dynamic category filtering.

Renders the complete original exam paper verbatim (every Themata,
sub-question, given parameter, and boundary condition) with hover-to-explain
highlights. No synthetic summary replaces the source text.
"""

from nicegui import ui
from models.scenario import Scenario


def renderInteractiveCanvas(scenario: Scenario) -> None:
    """Renders the interactive exam paper canvas with category filters.

    Args:
        scenario (Scenario): The active scenario containing the full exam paper.

    Returns:
        None
    """
    paragraphs_html_list = []
    for p in scenario.paragraphs:
        if p.is_heading:
            # Themata headings render as banner chips to mirror the paper structure
            segments_html = []
            for seg in p.segments:
                if not seg.is_highlight:
                    segments_html.append(seg.text)
                else:
                    tooltip_attr = f'title="{seg.tooltip}"' if seg.tooltip else ""
                    tag_html = f'<span class="tag-label">{seg.tag_label}</span>' if seg.tag_label else ""
                    badge_cls = seg.badge_class if seg.badge_class else ""
                    segments_html.append(
                        f'<span class="highlight-box {badge_cls} highlight-active" '
                        f'data-category="{seg.category}" data-badge-class="{badge_cls}" {tooltip_attr}>'
                        f'<strong>{seg.text}</strong>{tag_html}</span>'
                    )
            paragraphs_html_list.append(
                f'<p class="leading-relaxed m-0" style="margin: 14px 0 6px 0;">'
                f'<span class="thema-banner">{"".join(segments_html)}</span></p>'
            )
            continue

        border_style = (
            "border-left: 3px solid var(--accent); padding-left: 14px; margin: 16px 0;"
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
                    f'<span class="tag-label">{seg.tag_label}</span>'
                    if seg.tag_label
                    else ""
                )
                badge_cls = seg.badge_class if seg.badge_class else ""
                seg_html = (
                    f'<span class="highlight-box {badge_cls} highlight-active" '
                    f'data-category="{seg.category}" data-badge-class="{badge_cls}" {tooltip_attr}>'
                    f'<strong>{seg.text}</strong>{tag_html}</span>'
                )
                segments_html.append(seg_html)
        paragraphs_html_list.append(
            f'<p style="{border_style}" class="leading-relaxed m-0">{"".join(segments_html)}</p>'
        )

    full_canvas_body_html = "".join(paragraphs_html_list)

    with ui.column().classes("w-full glass-panel gap-0 p-0 overflow-hidden border border-[var(--border-accent)] print-section print-canvas"):
        # Header with filters and print banner
        with ui.row().classes(
            "w-full bg-[var(--canvas-header-bg)] p-5 justify-between items-center flex-wrap gap-4 border-b border-[var(--border)]"
        ):
            with ui.column().classes("gap-1"):
                with ui.row().classes("items-center gap-2"):
                    ui.html('<i class="fa-solid fa-file-lines text-amber-500 text-lg no-print"></i>')
                    ui.html('<h2 class="text-lg md:text-xl font-bold text-[var(--text-1)] m-0">Πλήρες Κείμενο Εξέτασης (Διαδραστικό Canvas)</h2>')
                ui.label(
                    f"Σενάριο: {scenario.title} — {scenario.subtitle}"
                ).classes("text-xs text-[var(--accent)] font-medium hidden print:block")
                ui.label(
                    f"Επίσημα δεδομένα εξέτασης: {scenario.exam_meta.duration} • {scenario.exam_meta.scoring}"
                ).classes("text-xs text-[var(--text-2)] font-medium")
                ui.label(
                    "Περάστε τον δρομέα πάνω στις επισημάνσεις για εξήγηση (Ταξινόμηση / Εντοπισμός / Εφαρμογή). Χρησιμοποιήστε τα φίλτρα για εστίαση."
                ).classes("text-xs text-[var(--text-3)] no-print")

            # Interactive filter buttons (presets + category toggles; hidden in print)
            with ui.row().classes("items-center gap-2 flex-wrap text-xs no-print"):
                # sanitize=False keeps the inline onclick handlers; content is static trusted markup.
                ui.html(
                    """
                    <button onclick="setFilterMode('all')" class="filter-chip active" data-filter="all" title="Εμφάνιση όλων των επισημάνσεων">
                        <i class="fa-solid fa-layer-group mr-1"></i> Όλα
                    </button>
                    <button onclick="setFilterMode('none')" class="filter-chip" data-filter="none" title="Απόκρυψη όλων των επισημάνσεων (Καθαρό κείμενο)">
                        <i class="fa-solid fa-file-lines mr-1"></i> Καθαρό Κείμενο
                    </button>
                    <button onclick="toggleCategory('term')" class="filter-chip active" data-category="term" title="Εναλλαγή εμφάνισης Τεχνικών Όρων">
                        <i class="fa-solid fa-bookmark mr-1 text-blue-500"></i> Τεχνικοί Όροι
                    </button>
                    <button onclick="toggleCategory('given')" class="filter-chip active" data-category="given" title="Εναλλαγή εμφάνισης Δεδομένων Εξέτασης">
                        <i class="fa-solid fa-database mr-1 text-amber-500"></i> Δεδομένα
                    </button>
                    <button onclick="toggleCategory('proto')" class="filter-chip active" data-category="proto" title="Εναλλαγή εμφάνισης Πρωτοκόλλων">
                        <i class="fa-solid fa-diagram-project mr-1 text-emerald-500"></i> Πρωτόκολλα
                    </button>
                    <button onclick="toggleCategory('method')" class="filter-chip active" data-category="method" title="Εναλλαγή εμφάνισης Μεθόδων & Τύπων">
                        <i class="fa-solid fa-square-root-variable mr-1 text-purple-500"></i> Μέθοδοι & Τύποι
                    </button>
                    """,
                    sanitize=False,
                )

        # Legend bar (hidden in print)
        with ui.row().classes(
            "w-full bg-[var(--canvas-legend-bg)] px-4 py-2.5 border-b border-[var(--border)] text-xs flex-wrap gap-4 justify-center no-print"
        ):
            ui.html(
                """
                <span class="inline-flex items-center text-blue-600 dark:text-blue-300 gap-1.5 font-medium"><span class="w-2.5 h-2.5 rounded-full bg-blue-500"></span> Τεχνικός Όρος</span>
                <span class="inline-flex items-center text-amber-600 dark:text-amber-300 gap-1.5 font-medium"><span class="w-2.5 h-2.5 rounded-full bg-amber-500"></span> Δεδομένο Εξέτασης</span>
                <span class="inline-flex items-center text-emerald-600 dark:text-emerald-300 gap-1.5 font-medium"><span class="w-2.5 h-2.5 rounded-full bg-emerald-500"></span> Πρωτόκολλο</span>
                <span class="inline-flex items-center text-purple-600 dark:text-purple-300 gap-1.5 font-medium"><span class="w-2.5 h-2.5 rounded-full bg-purple-500"></span> Μέθοδος / Τύπος</span>
                """
            )

        # Full contiguous exam text container
        ui.html(
            f"""
            <div id="canvas-text" class="p-6 md:p-8 space-y-4 bg-[var(--canvas-bg)] text-base md:text-lg leading-relaxed text-[var(--text-1)] w-full">
                {full_canvas_body_html}
            </div>
            """
        )


# Register the global head script for category filter state management.
# Only filtering and clean-text mode handlers live here (Section 2.3 whitelist).
ui.add_head_html(
    """
    <script>
        let activeCategories = new Set(['term', 'given', 'proto', 'method']);

        function updateCanvasHighlights() {
            const boxes = document.querySelectorAll('#canvas-text .highlight-box');
            const allBtn = document.querySelector('.filter-chip[data-filter="all"]');
            const noneBtn = document.querySelector('.filter-chip[data-filter="none"]');
            const categoryBtns = document.querySelectorAll('.filter-chip[data-category]');

            // Update category button active classes
            categoryBtns.forEach(btn => {
                const cat = btn.getAttribute('data-category');
                if (activeCategories.has(cat)) {
                    btn.classList.add('active');
                } else {
                    btn.classList.remove('active');
                }
            });

            // Update preset button active states
            if (allBtn) {
                if (activeCategories.size === 4) {
                    allBtn.classList.add('active');
                } else {
                    allBtn.classList.remove('active');
                }
            }

            if (noneBtn) {
                if (activeCategories.size === 0) {
                    noneBtn.classList.add('active');
                } else {
                    noneBtn.classList.remove('active');
                }
            }

            // Update each highlight box appearance
            boxes.forEach(box => {
                const cat = box.getAttribute('data-category');
                const origClass = box.getAttribute('data-badge-class') || '';
                const tag = box.querySelector('.tag-label');

                if (activeCategories.has(cat)) {
                    box.className = 'highlight-box ' + origClass;
                    if (tag) tag.style.display = 'inline-block';
                } else {
                    box.className = 'highlight-box highlight-plain';
                    if (tag) tag.style.display = 'none';
                }
            });
        }

        function setFilterMode(mode) {
            if (mode === 'all') {
                activeCategories = new Set(['term', 'given', 'proto', 'method']);
            } else if (mode === 'none') {
                activeCategories = new Set();
            }
            updateCanvasHighlights();
        }

        function toggleCategory(cat) {
            if (activeCategories.has(cat)) {
                activeCategories.delete(cat);
            } else {
                activeCategories.add(cat);
            }
            updateCanvasHighlights();
        }

        document.addEventListener('DOMContentLoaded', () => {
            updateCanvasHighlights();
        });
        setTimeout(updateCanvasHighlights, 100);
    </script>
    """,
    shared=True,
)
