"""Solution code verification and hardware design rationale component."""

from nicegui import ui
from models.scenario import Scenario
from config import renderMathHtml


def renderSolutionCode(scenario: Scenario) -> None:
    """Renders digital hardware design justifications and computational verification code.

    Args:
        scenario (Scenario): The active scenario containing justifications and code.

    Returns:
        None
    """
    with ui.column().classes("w-full glass-panel gap-6 p-6 border border-[var(--border)]").props('id="solution-code-section"'):
        # Header
        with ui.row().classes("w-full justify-between items-center flex-wrap gap-4 border-b border-[var(--border)] pb-4"):
            with ui.row().classes("items-center gap-3"):
                ui.html('<i class="fa-brands fa-python text-[var(--accent)] text-2xl"></i>')
                with ui.column().classes("gap-0"):
                    ui.html('<h2 class="text-xl md:text-2xl font-bold text-[var(--text-1)] m-0">Υπολογιστικός Κώδικας Επαλήθευσης & Αιτιολογήσεις</h2>')
                    ui.label("Συμβολικός έλεγχος πινάκων αληθείας, αλγορίθμων K-Map και προσομοίωσης FSM σε Python.").classes("text-xs text-[var(--text-2)]")

            # Whitelist Control: Copy Code Button
            with ui.button("Αντιγραφή Κώδικα", icon="content_copy").props("outline dense").classes(
                "text-xs text-[var(--accent)] border-[var(--border-accent)] hover:bg-[var(--surface-hover)] font-bold shadow-sm"
            ).on("click", lambda: ui.run_javascript(
                f"navigator.clipboard.writeText({repr(scenario.solution_code)}).then(() => {{"
                "  const el = document.getElementById('copy-feedback-msg');"
                "  if (el) { el.style.display = 'inline'; setTimeout(() => el.style.display = 'none', 2000); }"
                "}});"
            )):
                pass
            ui.html('<span id="copy-feedback-msg" class="text-xs text-[var(--green-ok)] font-bold hidden"><i class="fa-solid fa-check mr-1"></i>Αντιγράφηκε!</span>')

        # Hardware & Methodological Justification Cards
        if scenario.justifications:
            with ui.column().classes("w-full gap-3"):
                with ui.row().classes("items-center gap-2 text-xs font-bold text-[var(--text-2)]"):
                    ui.html('<i class="fa-solid fa-shield-halved text-[var(--blue-action)]"></i>')
                    ui.label("Θεμελιώσεις & Αρχιτεκτονικές Αρχές Σχεδίασης")

                with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full"):
                    for just in scenario.justifications:
                        with ui.column().classes(
                            "p-4 rounded-xl bg-[var(--card-bg-subtle)] border-l-4 border-[var(--accent)] border border-[var(--border)] gap-1.5 shadow-sm"
                        ):
                            with ui.row().classes("items-center justify-between w-full"):
                                ui.label(just.title).classes("font-bold text-sm text-[var(--text-1)]")
                                ui.html(f'<span class="text-[0.68rem] px-2 py-0.5 rounded-full bg-[var(--surface-2)] text-[var(--accent)] border border-[var(--border-accent)] font-semibold">{just.category}</span>')
                            ui.html(f'<div class="text-xs text-[var(--text-2)] leading-relaxed latex-target">{renderMathHtml(just.description)}</div>')
                            ui.html(f'<div class="text-xs text-[var(--text-3)] leading-relaxed italic latex-target">{renderMathHtml(f"**Αιτιολόγηση:** {just.rationale}")}</div>')

        # Python Code Display
        if scenario.solution_code:
            with ui.column().classes("w-full code-wrapper overflow-hidden"):
                with ui.row().classes("w-full px-4 py-2 bg-[var(--surface-2)] border-b border-[var(--border)] justify-between items-center text-xs text-[var(--text-3)]"):
                    ui.html('<span><i class="fa-brands fa-python text-[var(--accent)] mr-2"></i>digital_logic_verifier.py</span>')
                    ui.label("Python 3 Logic Verification")
                ui.code(scenario.solution_code, language="python").classes("w-full text-xs font-mono p-4")

