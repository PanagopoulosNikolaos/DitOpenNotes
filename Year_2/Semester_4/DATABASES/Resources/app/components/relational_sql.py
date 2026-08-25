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
        # Relational Justifications
        with ui.column().classes("w-full glass-panel gap-4"):
            with ui.row().classes("items-center gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3 w-full"):
                ui.html('<i class="fa-solid fa-pen-nib text-[#e06b3a]"></i>')
                ui.html('<h3 class="text-lg font-bold text-[#f4f1ea] m-0">Αιτιολόγηση Σχεδιαστικών Επιλογών (Crow\'s Foot / Relational)</h3>')

            with ui.grid().classes("grid-cols-1 md:grid-cols-2 gap-4 w-full"):
                for just in scenario.relational_justifications:
                    with ui.column().classes("p-4 rounded-xl bg-[#201f1d] border border-[rgba(255,255,255,0.06)] gap-1.5"):
                        ui.label(just.title).classes(f"font-bold {just.color_class} text-sm")
                        ui.label(just.description).classes("text-xs text-[#b5b0a4] leading-relaxed")

        # SQL DDL Code Preview
        if scenario.sql_ddl:
            with ui.column().classes("w-full glass-panel gap-4"):
                with ui.row().classes("w-full justify-between items-center flex-wrap gap-2 border-b border-[rgba(255,255,255,0.08)] pb-3"):
                    with ui.row().classes("items-center gap-2"):
                        ui.html('<i class="fa-solid fa-database text-[#f59e0b]"></i>')
                        ui.html('<h3 class="text-lg font-bold text-[#fde68a] m-0">Σχεσιακή Υλοποίηση: SQL DDL Schema</h3>')

                    ui.button(
                        "Αντιγραφή SQL",
                        icon="content_copy",
                        on_click=lambda: ui.run_javascript(f"navigator.clipboard.writeText({repr(scenario.sql_ddl)});"),
                    ).props("outline dense").classes(
                        "text-xs text-[#fdba74] border-[rgba(224,107,58,0.4)] hover:bg-[#e06b3a]/20"
                    )

                with ui.column().classes("w-full rounded-xl overflow-hidden bg-[#10100f] border border-[rgba(255,255,255,0.08)] p-4"):
                    ui.code(scenario.sql_ddl, language="sql").classes("w-full text-xs font-mono text-[#f4f1ea]")
