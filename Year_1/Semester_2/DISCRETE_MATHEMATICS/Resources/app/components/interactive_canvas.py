"""Interactive annotated canvas component for Discrete Mathematics study instrument.

Renders the complete exam paper verbatim with semantic highlight badges, category
filter chips, visual legend bar, and three-part hover tooltips.
"""

from nicegui import ui
from models.scenario import Scenario
from config import renderMathHtml


def renderInteractiveCanvas(scenario: Scenario) -> None:
    """Renders the complete original exam text with interactive hover highlighting.

    Args:
        scenario (Scenario): The active scenario containing full verbatim exam paragraphs.

    Returns:
        None
    """
    with ui.column().classes("w-full glass-panel p-6 gap-5 border border-[var(--border)]").props('id="interactive-canvas-section"'):
        # Header: Title and Duration
        with ui.row().classes("w-full justify-between items-center flex-wrap gap-2 pb-3 border-b border-[var(--border)]"):
            with ui.row().classes("items-center gap-3"):
                ui.html('<i class="fa-solid fa-file-signature text-[var(--accent)] text-xl"></i>')
                with ui.column().classes("gap-0"):
                    ui.html(f'<h2 class="text-lg md:text-xl font-bold text-[var(--text-1)] m-0">{scenario.title}</h2>')
                    ui.label(f"{scenario.subtitle} • Διάρκεια: {scenario.duration_info}").classes("text-xs text-[var(--text-3)]")

            with ui.row().classes("items-center gap-2"):
                ui.html(f'<span class="text-xs px-2.5 py-1 rounded-full font-bold bg-[var(--surface-2)] text-[var(--blue-action)] border border-[var(--border)]"><i class="fa-solid fa-layer-group mr-1.5"></i>{scenario.course_tag}</span>')

        # Filter Chips Bar
        with ui.row().classes("w-full items-center gap-2 flex-wrap py-1"):
            ui.label("Φίλτρο Επισήμανσης:").classes("text-xs font-bold text-[var(--text-3)] mr-1")

            ui.html('<button id="chip-all" class="category-chip-btn active-chip px-2.5 py-1 rounded-md text-xs font-semibold bg-[var(--surface-2)] border border-[var(--border)] hover:border-[var(--accent)] cursor-pointer text-[var(--text-1)]" onclick="setFilterMode(\'all\')"><i class="fa-solid fa-list-ul mr-1"></i>Όλα</button>')
            ui.html('<button id="chip-clean" class="category-chip-btn px-2.5 py-1 rounded-md text-xs font-semibold bg-[var(--surface-2)] border border-[var(--border)] hover:border-[var(--accent)] cursor-pointer text-[var(--text-1)]" onclick="setFilterMode(\'clean\')"><i class="fa-solid fa-eye-slash mr-1"></i>Καθαρό Κείμενο</button>')
            ui.html('<button id="chip-logic" class="category-chip-btn px-2.5 py-1 rounded-md text-xs font-semibold bg-[var(--surface-2)] border border-[var(--border)] hover:border-[var(--amber)] cursor-pointer text-[var(--amber)]" onclick="setFilterMode(\'logic\')"><i class="fa-solid fa-diagram-project mr-1"></i>Λογική</button>')
            ui.html('<button id="chip-set" class="category-chip-btn px-2.5 py-1 rounded-md text-xs font-semibold bg-[var(--surface-2)] border border-[var(--border)] hover:border-[var(--blue-action)] cursor-pointer text-[var(--blue-action)]" onclick="setFilterMode(\'set\')"><i class="fa-solid fa-cubes mr-1"></i>Σύνολα</button>')
            ui.html('<button id="chip-prob" class="category-chip-btn px-2.5 py-1 rounded-md text-xs font-semibold bg-[var(--surface-2)] border border-[var(--border)] hover:border-[var(--green-ok)] cursor-pointer text-[var(--green-ok)]" onclick="setFilterMode(\'prob\')"><i class="fa-solid fa-dice mr-1"></i>Πιθανότητες</button>')
            ui.html('<button id="chip-graph" class="category-chip-btn px-2.5 py-1 rounded-md text-xs font-semibold bg-[var(--surface-2)] border border-[var(--border)] hover:border-[var(--purple)] cursor-pointer text-[var(--purple)]" onclick="setFilterMode(\'graph\')"><i class="fa-solid fa-circle-nodes mr-1"></i>Γραφήματα</button>')
            ui.html('<button id="chip-automata" class="category-chip-btn px-2.5 py-1 rounded-md text-xs font-semibold bg-[var(--surface-2)] border border-[var(--border)] hover:border-[var(--accent)] cursor-pointer text-[var(--accent)]" onclick="setFilterMode(\'automata\')"><i class="fa-solid fa-gears mr-1"></i>Αυτόματα</button>')
            ui.html('<button id="chip-induct" class="category-chip-btn px-2.5 py-1 rounded-md text-xs font-semibold bg-[var(--surface-2)] border border-[var(--border)] hover:border-[#0284c7] cursor-pointer text-[#0284c7]" onclick="setFilterMode(\'induct\')"><i class="fa-solid fa-arrow-trend-up mr-1"></i>Επαγωγή</button>')

        # Visual Legend Bar
        with ui.row().classes("w-full items-center gap-3 p-2.5 rounded-lg bg-[var(--canvas-legend-bg)] border border-[var(--border)] text-xs flex-wrap"):
            ui.label("Υπόμνημα:").classes("font-bold text-[var(--text-3)]")
            ui.html('<span class="highlight-badge badge-logic">Λογική / Τύποι</span>')
            ui.html('<span class="highlight-badge badge-set">Σύνολα / Πράξεις</span>')
            ui.html('<span class="highlight-badge badge-prob">Πιθανότητες / Bayes</span>')
            ui.html('<span class="highlight-badge badge-graph">Κορυφές / Γραφήματα</span>')
            ui.html('<span class="highlight-badge badge-automata">Αυτόματα / Γλώσσες</span>')
            ui.html('<span class="highlight-badge badge-induct">Μαθηματική Επαγωγή</span>')
            ui.html('<span class="highlight-badge badge-param">Δεδομένα / Παράμετροι</span>')

        # Verbatim Exam Text Paragraphs
        with ui.column().classes("w-full p-6 rounded-xl bg-[var(--canvas-bg)] border border-[var(--border)] gap-4 text-sm leading-relaxed text-[var(--text-1)] latex-target"):
            for p in scenario.paragraphs:
                p_border = f"border-l-4 pl-4 border-[{p.accent_border_color}]" if p.accent_border_color else ""
                html_parts = []
                for seg in p.segments:
                    if seg.is_highlight:
                        b_class = seg.badge_class or "badge-param"
                        cat = seg.category or "param"
                        tip = (seg.tooltip or "").replace('"', '&quot;')
                        tag_html = f'<span class="text-[0.65rem] opacity-75 font-mono mr-1">[{seg.tag_label}]</span>' if seg.tag_label else ""
                        html_parts.append(
                            f'<span class="highlight-badge {b_class}" data-category="{cat}" title="{tip}">{tag_html}{seg.text}</span>'
                        )
                    else:
                        html_parts.append(seg.text)

                paragraph_html = "".join(html_parts)
                ui.html(f'<div class="{p_border} mb-2">{renderMathHtml(paragraph_html)}</div>')
