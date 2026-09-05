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

    with ui.column().classes("w-full glass-panel gap-0 p-0 overflow-hidden border border-[var(--border-accent)] print-section print-canvas no-break-before"):
        # Header with filters (Interactive) and Print Banner
        with ui.row().classes(
            "w-full bg-[var(--canvas-header-bg)] p-5 justify-between items-center flex-wrap gap-4 border-b border-[var(--border)]"
        ):
            with ui.column().classes("gap-1"):
                with ui.row().classes("items-center gap-2"):
                    ui.html('<i class="fa-solid fa-highlighter text-[#f59e0b] text-lg no-print"></i>')
                    ui.html('<h2 class="text-lg md:text-xl font-bold text-[var(--text-1)] m-0">Interactive Requirements Text Canvas</h2>')
                ui.label(
                    f"Scenario: {scenario.title} — {scenario.subtitle}"
                ).classes("text-xs text-[var(--accent)] font-medium hidden print:block")
                ui.label(
                    "Click on filters to toggle highlights or select Plain Text."
                ).classes("text-xs text-[var(--text-3)] no-print")

            # Interactive Filter Buttons (Presets + Category Toggles - hidden in print)
            with ui.row().classes("items-center gap-2 flex-wrap text-xs no-print"):
                # sanitize=False keeps inline onclick handlers; content is static trusted markup.
                ui.html(
                    """
                    <button onclick="setFilterMode('all')" class="filter-chip active" data-filter="all" title="Show all elements">
                        <i class="fa-solid fa-layer-group mr-1"></i> All
                    </button>
                    <button onclick="setFilterMode('none')" class="filter-chip" data-filter="none" title="Hide all highlights (Plain text)">
                        <i class="fa-solid fa-file-lines mr-1"></i> Plain Text
                    </button>
                    <button onclick="toggleCategory('entity')" class="filter-chip active" data-category="entity" title="Toggle Entities">
                        <i class="fa-solid fa-cube mr-1 text-blue-500"></i> Entities
                    </button>
                    <button onclick="toggleCategory('key')" class="filter-chip active" data-category="key" title="Toggle Keys">
                        <i class="fa-solid fa-key mr-1 text-amber-500"></i> Keys
                    </button>
                    <button onclick="toggleCategory('attr')" class="filter-chip active" data-category="attr" title="Toggle Attributes">
                        <i class="fa-solid fa-tag mr-1 text-emerald-500"></i> Attributes
                    </button>
                    <button onclick="toggleCategory('rel')" class="filter-chip active" data-category="rel" title="Toggle Relationships">
                        <i class="fa-solid fa-code-branch mr-1 text-rose-500"></i> Relationships
                    </button>
                    """,
                    sanitize=False,
                )

        # Legend Bar (hidden in print)
        with ui.row().classes(
            "w-full bg-[var(--canvas-legend-bg)] px-4 py-2.5 border-b border-[var(--border)] text-xs flex-wrap gap-4 justify-center no-print"
        ):
            ui.html(
                """
                <span class="inline-flex items-center text-blue-600 dark:text-[#93c5fd] gap-1.5 font-medium"><span class="w-2.5 h-2.5 rounded-full bg-blue-500"></span> Strong Entity</span>
                <span class="inline-flex items-center text-purple-600 dark:text-[#d8b4fe] gap-1.5 font-medium"><span class="w-2.5 h-2.5 rounded-full bg-purple-500"></span> Weak Entity</span>
                <span class="inline-flex items-center text-orange-600 dark:text-[#fdba74] gap-1.5 font-medium"><span class="w-2.5 h-2.5 bg-[#e06b3a] rounded-sm"></span> Primary Key (PK)</span>
                <span class="inline-flex items-center text-emerald-600 dark:text-[#86efac] gap-1.5 font-medium"><span class="w-2.5 h-2.5 bg-emerald-500 rounded-sm"></span> Simple / Composite Attribute</span>
                <span class="inline-flex items-center text-fuchsia-600 dark:text-[#f0abfc] gap-1.5 font-medium"><span class="w-2.5 h-2.5 bg-fuchsia-500 rounded-sm"></span> Multivalued Attribute</span>
                <span class="inline-flex items-center text-rose-600 dark:text-[#fda4af] gap-1.5 font-medium"><span class="w-2.5 h-2.5 bg-rose-500 rounded-sm"></span> Relationship / Cardinality</span>
                """
            )

        # Full Contiguous Text Container
        ui.html(
            f"""
            <div id="canvas-text" class="p-6 md:p-8 space-y-4 bg-[var(--canvas-bg)] text-base md:text-lg leading-relaxed text-[var(--text-1)] w-full">
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

        function downloadStandaloneHTML() {
            const title = document.querySelector('h1')?.innerText || 'E-R Model Analysis Guide';
            const subTitle = document.querySelector('header label')?.innerText || '';
            const printSections = document.querySelectorAll('.print-section');
            let sectionsHTML = '';

            printSections.forEach(sec => {
                const clone = sec.cloneNode(true);
                clone.querySelectorAll('.no-print').forEach(el => el.remove());
                sectionsHTML += `<div class="section-wrapper">${clone.outerHTML}</div>`;
            });

            const fullHTML = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${title}</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * { box-sizing: border-box; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; color-adjust: exact !important; }
        body { background-color: #ffffff; color: #18181b; font-family: system-ui, -apple-system, sans-serif; font-size: 13px; line-height: 1.5; margin: 0; padding: 24px; }
        .header-banner { border-bottom: 2px solid rgba(224, 107, 58, 0.4); padding-bottom: 12px; margin-bottom: 20px; }
        .header-banner h1 { margin: 0; font-size: 22px; color: #c2410c; }
        .glass-panel { background: #ffffff; border: 1px solid #d1d5db; border-radius: 8px; padding: 16px; margin-bottom: 16px; }
        h2, h3 { color: #9a3412; margin-top: 0; }
        .attr-card-container, .rel-card-container { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px; }
        .attr-card { background: #f0fdf4; border: 1px solid #86efac; padding: 10px; border-radius: 6px; color: #065f46; }
        .attr-card-rel { grid-column: span 2; background: #fff1f2; border: 1px solid #fda4af; padding: 10px; border-radius: 6px; color: #9f1239; }
        .rel-card { background: #fff1f2; border: 1px solid #fda4af; padding: 10px; border-radius: 6px; }
        .dark-table { width: 100%; border-collapse: collapse; margin-top: 8px; }
        .dark-table th, .dark-table td { border: 1px solid #d1d5db; padding: 6px 10px; font-size: 12px; text-align: left; }
        .dark-table th { background: #f3f4f6; color: #111827; }
        #er-svg-canvas { width: 100%; height: 500px; background: #ffffff; border: 1px solid #d1d5db; border-radius: 8px; }
        pre, code { font-family: monospace; font-size: 11px; white-space: pre-wrap; word-break: break-word; }
        .sql-code-container { background: #f8fafc; border: 1px solid #d1d5db; padding: 14px; border-radius: 8px; color: #0f172a; }
        @media print {
            @page { size: A4 portrait; margin: 6mm 8mm; }
            body { padding: 0; font-size: 8.5pt; background: #ffffff !important; color: #18181b !important; }
            .attr-card-container, .rel-card-container { gap: 6px; }
            .attr-card, .rel-card { padding: 4px 8px; }
            #er-svg-canvas { height: 520px !important; }
            .dark-table th, .dark-table td { padding: 3px 5px; font-size: 7.5pt; }
            .sql-code-container pre { font-size: 7.5pt; line-height: 1.25; }
        }
    </style>
</head>
<body>
    <div class="header-banner">
        <h1>${title}</h1>
        <p style="color:#52525b; margin: 4px 0 0 0; font-size: 12px;">${subTitle}</p>
    </div>
    ${sectionsHTML}
</body>
</html>`;

            const blob = new Blob([fullHTML], { type: 'text/html;charset=utf-8;' });
            const url = URL.createObjectURL(blob);
            const link = document.createElement('a');
            link.href = url;
            link.download = `ER_Model_Report_${new Date().toISOString().slice(0,10)}.html`;
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
            URL.revokeObjectURL(url);
        }

        document.addEventListener('DOMContentLoaded', () => {
            updateCanvasHighlights();
        });
        setTimeout(updateCanvasHighlights, 100);
    </script>
    """,
    shared=True,
)
