"""Solution code implementation and rationale card component for Discrete Mathematics."""

from nicegui import ui
from models.scenario import Scenario
from config import renderMathHtml


def renderSolutionCode(scenario: Scenario) -> None:
    """Renders design rationale cards and executable Python verification code.

    Args:
        scenario (Scenario): Active scenario containing justifications and solution code.

    Returns:
        None
    """
    with ui.column().classes("w-full glass-panel p-6 gap-6 border border-[var(--border)]").props('id="solution-code-section"'):
        # Section Header
        with ui.row().classes("w-full items-center gap-3 pb-2 border-b border-[var(--border)]"):
            ui.html('<i class="fa-solid fa-code text-[var(--accent)] text-xl"></i>')
            with ui.column().classes("gap-0"):
                ui.html('<h3 class="text-base md:text-lg font-bold text-[var(--text-1)] m-0">Υπολογιστική Επαλήθευση & Μαθηματικές Αιτιολογήσεις</h3>')
                ui.label("Κώδικας Python για αλγοριθμική επαλήθευση αποτελεσμάτων και κάρτες θεωρητικής τεκμηρίωσης.").classes("text-xs text-[var(--text-3)]")

        # Design Justification Cards
        if scenario.justifications:
            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full"):
                for just in scenario.justifications:
                    with ui.column().classes("p-4 rounded-xl bg-[var(--surface-2)] border border-[var(--border)] gap-2"):
                        with ui.row().classes("w-full items-center justify-between"):
                            ui.label(just.title).classes("text-sm font-bold text-[var(--text-1)]")
                            ui.html(f'<span class="text-[0.65rem] px-2 py-0.5 rounded-full font-bold bg-[var(--surface)] text-[var(--accent)] border border-[var(--border-accent)]">{just.category}</span>')
                        ui.html(f'<div class="text-xs text-[var(--text-2)] leading-relaxed latex-target">{renderMathHtml(just.description)}</div>')
                        with ui.row().classes("items-start gap-1.5 pt-1.5 border-t border-[var(--border)] text-xs text-[var(--text-3)]"):
                            ui.html('<i class="fa-solid fa-circle-check text-[var(--green-ok)] text-[0.7rem] mt-0.5"></i>')
                            ui.html(f'<div class="text-[0.75rem] italic latex-target">{renderMathHtml(just.rationale)}</div>')

        # Code Block with Copy Code Button
        if scenario.solution_code:
            with ui.column().classes("w-full gap-2 mt-2"):
                with ui.row().classes("w-full justify-between items-center"):
                    with ui.row().classes("items-center gap-2 text-xs font-bold text-[var(--text-2)]"):
                        ui.html('<i class="fa-brands fa-python text-yellow-500"></i>')
                        ui.label("Python Verification Script (SymPy / NetworkX / Itertools)")

                    ui.button(
                        "Αντιγραφή Κώδικα",
                        icon="fa-solid fa-copy",
                        on_click=lambda: ui.run_javascript(
                            f"navigator.clipboard.writeText({repr(scenario.solution_code)});"
                        ),
                    ).props("flat dense").classes("text-xs text-[var(--text-2)] hover:text-[var(--accent)]")

                ui.code(scenario.solution_code, language="python").classes("w-full rounded-xl text-xs font-mono shadow-inner border border-[var(--border)]")
