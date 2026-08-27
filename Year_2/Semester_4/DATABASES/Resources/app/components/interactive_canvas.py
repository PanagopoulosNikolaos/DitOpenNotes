"""Interactive requirements canvas component with dynamic category filtering."""

from nicegui import ui
from models.scenario import Scenario


def renderInteractiveCanvas(scenario: Scenario) -> None:
    """Renders the interactive problem description canvas with category filters.

    Args:
        scenario (Scenario): The active scenario containing paragraphs and highlights.

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
                    f'<span class="tag-label bg-[rgba(0,0,0,0.5)]">{seg.tag_label}</span>'
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

    with ui.column().classes("w-full glass-panel gap-0 p-0 overflow-hidden border border-[rgba(224,107,58,0.25)] print-section print-canvas no-break-before"):
        # Header with filters (Interactive) and Print Banner
        with ui.row().classes(
            "w-full bg-[#121211] p-5 justify-between items-center flex-wrap gap-4 border-b border-[rgba(255,255,255,0.08)]"
        ):
            with ui.column().classes("gap-1"):
                with ui.row().classes("items-center gap-2"):
                    ui.html('<i class="fa-solid fa-highlighter text-[#f59e0b] text-lg no-print"></i>')
                    ui.html('<h2 class="text-lg md:text-xl font-bold text-[#f4f1ea] m-0">Διαδραστικό Canvas Κειμένου Απαιτήσεων</h2>')
                ui.label(
                    f"Σενάριο: {scenario.title} — {scenario.subtitle}"
                ).classes("text-xs text-[#fdba74] font-medium hidden print:block")
                ui.label(
                    "Κάντε κλικ στα φίλτρα για να εμφανίσετε/αποκρύψετε επιμέρους στοιχεία ή επιλέξτε Καθαρό Κείμενο."
                ).classes("text-xs text-[#78756d] no-print")

            # Interactive Filter Buttons (Presets + Category Toggles - hidden in print)
            with ui.row().classes("items-center gap-2 flex-wrap text-xs no-print"):
                # sanitize=False keeps inline onclick handlers; content is static trusted markup.
                ui.html(
                    """
                    <button onclick="setFilterMode('all')" class="filter-chip active" data-filter="all" title="Εμφάνιση όλων των στοιχείων">
                        <i class="fa-solid fa-layer-group mr-1"></i> Όλα
                    </button>
                    <button onclick="setFilterMode('none')" class="filter-chip" data-filter="none" title="Απόκρυψη όλων των επισημάνσεων (Καθαρό κείμενο)">
                        <i class="fa-solid fa-file-lines mr-1"></i> Καθαρό Κείμενο
                    </button>
                    <button onclick="toggleCategory('entity')" class="filter-chip active" data-category="entity" title="Εναλλαγή εμφάνισης Οντοτήτων">
                        <i class="fa-solid fa-cube mr-1 text-blue-400"></i> Οντότητες
                    </button>
                    <button onclick="toggleCategory('key')" class="filter-chip active" data-category="key" title="Εναλλαγή εμφάνισης Κλειδιών">
                        <i class="fa-solid fa-key mr-1 text-amber-400"></i> Κλειδιά
                    </button>
                    <button onclick="toggleCategory('attr')" class="filter-chip active" data-category="attr" title="Εναλλαγή εμφάνισης Γνωρισμάτων">
                        <i class="fa-solid fa-tag mr-1 text-emerald-400"></i> Γνωρίσματα
                    </button>
                    <button onclick="toggleCategory('rel')" class="filter-chip active" data-category="rel" title="Εναλλαγή εμφάνισης Σχέσεων">
                        <i class="fa-solid fa-code-branch mr-1 text-rose-400"></i> Σχέσεις
                    </button>
                    """,
                    sanitize=False,
                )

        # Legend Bar (hidden in print)
        with ui.row().classes(
            "w-full bg-[#171615] px-4 py-2.5 border-b border-[rgba(255,255,255,0.06)] text-xs flex-wrap gap-4 justify-center no-print"
        ):
            ui.html(
                """
                <span class="inline-flex items-center text-[#93c5fd] gap-1.5"><span class="w-2.5 h-2.5 rounded-full bg-blue-500"></span> Ισχυρή Οντότητα</span>
                <span class="inline-flex items-center text-[#d8b4fe] gap-1.5"><span class="w-2.5 h-2.5 rounded-full bg-purple-500"></span> Ασθενής Οντότητα</span>
                <span class="inline-flex items-center text-[#fdba74] gap-1.5"><span class="w-2.5 h-2.5 bg-[#e06b3a] rounded-sm"></span> Πρωτεύον Κλειδί (PK)</span>
                <span class="inline-flex items-center text-[#86efac] gap-1.5"><span class="w-2.5 h-2.5 bg-emerald-500 rounded-sm"></span> Απλό/Σύνθετο Γνώρισμα</span>
                <span class="inline-flex items-center text-[#f0abfc] gap-1.5"><span class="w-2.5 h-2.5 bg-fuchsia-500 rounded-sm"></span> Πλειότιμο Γνώρισμα</span>
                <span class="inline-flex items-center text-[#fda4af] gap-1.5"><span class="w-2.5 h-2.5 bg-rose-500 rounded-sm"></span> Σχέση / Πληθικότητα</span>
                """
            )

        # Full Contiguous Text Container
        ui.html(
            f"""
            <div id="canvas-text" class="p-6 md:p-8 space-y-4 bg-[#1a1918] text-base md:text-lg leading-relaxed text-[#f4f1ea] w-full">
                {full_canvas_body_html}
            </div>
            """
        )

# Register global head script for filter state management
ui.add_head_html(
    """
    <script>
        let activeCategories = new Set(['entity', 'key', 'attr', 'rel']);

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
                activeCategories = new Set(['entity', 'key', 'attr', 'rel']);
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

        function printERSection(target) {
            if (!target || target === 'all') {
                document.body.removeAttribute('data-print-target');
            } else {
                document.body.setAttribute('data-print-target', target);
            }

            // Ensure all highlight categories are enabled for clean print output
            const prevCategories = new Set(activeCategories);
            activeCategories = new Set(['entity', 'key', 'attr', 'rel']);
            updateCanvasHighlights();

            // Reset ER Diagram zoom and center before printing
            if (typeof resetERZoom === 'function') {
                resetERZoom();
            }

            setTimeout(() => {
                window.print();
                setTimeout(() => {
                    document.body.removeAttribute('data-print-target');
                    activeCategories = prevCategories;
                    updateCanvasHighlights();
                }, 500);
            }, 150);
        }

        document.addEventListener('DOMContentLoaded', () => {
            updateCanvasHighlights();
        });
        setTimeout(updateCanvasHighlights, 100);
    </script>
    """,
    shared=True,
)
