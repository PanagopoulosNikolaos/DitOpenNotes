"""Solution rationale cards and verification code preview component."""

from nicegui import ui
from models.scenario import Scenario


def renderSolutionCode(scenario: Scenario) -> None:
    """Renders the step-by-step solution justification cards and the verification code.

    Args:
        scenario (Scenario): The active scenario containing justifications and code.

    Returns:
        None
    """
    with ui.column().classes("w-full gap-6"):
        # Solution rationale cards (excluded from print)
        if scenario.justifications:
            with ui.column().classes("w-full glass-panel gap-4 no-print"):
                with ui.row().classes("items-center gap-2 border-b border-[var(--border)] pb-3 w-full"):
                    ui.html('<i class="fa-solid fa-pen-nib text-[var(--accent)]"></i>')
                    ui.html('<h3 class="text-lg font-bold text-[var(--text-1)] m-0">Αιτιολόγηση Βημάτων & Σχεδιαστικών Επιλογών της Λύσης</h3>')

                with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full"):
                    for just in scenario.justifications:
                        with ui.column().classes("p-4 rounded-xl bg-[var(--card-bg-subtle)] border border-[var(--border)] gap-1.5 shadow-sm"):
                            ui.label(just.title).classes(f"font-bold {just.color_class} text-sm")
                            ui.label(just.description).classes("text-xs text-[var(--text-2)] leading-relaxed")

        # Verification code preview (included in print)
        if scenario.solution_code:
            with ui.column().classes("w-full glass-panel gap-4 print-section print-code"):
                with ui.row().classes("w-full justify-between items-center flex-wrap gap-2 border-b border-[var(--border)] pb-3"):
                    with ui.row().classes("items-center gap-2"):
                        ui.html('<i class="fa-solid fa-code text-amber-500 no-print"></i>')
                        ui.html('<h3 class="text-lg font-bold text-[var(--text-1)] m-0">Κώδικας Επαλήθευσης της Λύσης (Python)</h3>')

                    ui.button(
                        "Αντιγραφή Κώδικα",
                        icon="content_copy",
                        on_click=lambda: ui.run_javascript(
                            f"navigator.clipboard.writeText({repr(scenario.solution_code)});"
                        ),
                    ).props("outline dense").classes(
                        "text-xs text-[var(--accent)] border-[var(--border-accent)] hover:bg-[var(--surface-hover)] no-print"
                    )

                ui.label(
                    "Το παρακάτω σκριπτ επαληθεύει αυτόματα κάθε αριθμητικό αποτέλεσμα της λύσης "
                    "χρησιμοποιώντας μόνο την τυποθήκη ipaddress/math της Python."
                ).classes("text-xs text-[var(--text-2)] no-print")

                with ui.column().classes("w-full rounded-xl overflow-hidden print:overflow-visible bg-[var(--code-bg)] border border-[var(--code-border)] p-4 code-container shadow-inner"):
                    ui.code(scenario.solution_code, language=scenario.code_language).classes(
                        "w-full text-xs font-mono text-[var(--code-text)]"
                    )
