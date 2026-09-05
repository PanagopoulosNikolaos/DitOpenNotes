"""Relational schema justifications and SQL DDL generator preview component."""

from nicegui import ui
from models.scenario import Scenario


def renderRelationalAndSQL(scenario: Scenario) -> None:
    """Renders relational mapping design justifications and SQL DDL schema.

    Args:
        scenario (Scenario): The active scenario containing justifications and DDL code.

    Returns:
        None
    """
    with ui.column().classes("w-full gap-6"):
        # Relational Justifications (Excluded from Print)
        with ui.column().classes("w-full glass-panel gap-4 no-print"):
            with ui.row().classes("items-center gap-2 border-b border-[var(--border)] pb-3 w-full"):
                ui.html('<i class="fa-solid fa-pen-nib text-[var(--accent)]"></i>')
                ui.html('<h3 class="text-lg font-bold text-[var(--text-1)] m-0">Αιτιολόγηση Σχεδιαστικών Επιλογών (Crow\'s Foot / Relational)</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full"):
                for just in scenario.relational_justifications:
                    with ui.column().classes("p-4 rounded-xl bg-[var(--card-bg-subtle)] border border-[var(--border)] gap-1.5 shadow-sm"):
                        ui.label(just.title).classes(f"font-bold {just.color_class} text-sm")
                        ui.label(just.description).classes("text-xs text-[var(--text-2)] leading-relaxed")

        # SQL DDL Code Preview (Included in Print)
        if scenario.sql_ddl:
            with ui.column().classes("w-full glass-panel gap-4 print-section print-sql-ddl"):
                with ui.row().classes("w-full justify-between items-center flex-wrap gap-2 border-b border-[var(--border)] pb-3"):
                    with ui.row().classes("items-center gap-2"):
                        ui.html('<i class="fa-solid fa-database text-[#f59e0b] no-print"></i>')
                        ui.html('<h3 class="text-lg font-bold text-amber-600 dark:text-[#fde68a] m-0">Σχεσιακή Υλοποίηση: SQL DDL Schema</h3>')

                    ui.button(
                        "Αντιγραφή SQL",
                        icon="content_copy",
                        on_click=lambda: ui.run_javascript(f"navigator.clipboard.writeText({repr(scenario.sql_ddl)});"),
                    ).props("outline dense").classes(
                        "text-xs text-[var(--accent)] border-[var(--border-accent)] hover:bg-[var(--surface-hover)] no-print"
                    )

                with ui.column().classes("w-full rounded-xl overflow-hidden print:overflow-visible bg-[var(--code-bg)] border border-[var(--code-border)] p-4 sql-code-container shadow-inner"):
                    ui.code(scenario.sql_ddl, language="sql").classes("w-full text-xs font-mono text-[var(--code-text)]")
