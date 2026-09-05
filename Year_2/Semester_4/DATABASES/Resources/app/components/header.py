"""Header navigation component for the ER Analysis application."""

from typing import Callable, Optional
from nicegui import ui
from models.scenario import Scenario
from models.registry import scenario_registry


def renderHeader(
    current_scenario: Optional[Scenario],
    current_scenario_id: str,
    on_scenario_change: Callable[[str], None],
) -> dict:
    """Renders the top application header with title, scenario selector, theme switch, and badges.

    Args:
        current_scenario (Optional[Scenario]): The currently active scenario or None.
        current_scenario_id (str): The ID of the currently active scenario or 'theory'.
        on_scenario_change (Callable[[str], None]): Callback triggered when a new scenario is selected.

    Returns:
        dict: References to dynamic header label elements.
    """
    initial_subtitle = (
        current_scenario.subtitle
        if current_scenario
        else "Complete Theory, Methodology & Crow's Foot Notations"
    )
    initial_course_tag = (
        current_scenario.course_tag
        if current_scenario
        else "Theory / Guide"
    )

    with ui.header().classes(
        "w-full bg-[var(--header-bg)] backdrop-blur-md border-b border-[var(--border-accent)] "
        "px-6 py-4 flex flex-col md:flex-row justify-between items-center gap-4 z-50 sticky top-0 transition-colors"
    ):
        with ui.row().classes("items-center gap-4"):
            ui.html('<i class="fa-solid fa-diagram-project text-[var(--accent)] text-2xl"></i>')
            with ui.column().classes("gap-0"):
                ui.html('<h1 class="gradient-title text-xl md:text-2xl font-black">E-R Model Analysis Guide</h1>')
                subtitle_label = ui.label(initial_subtitle).classes("text-xs text-[var(--text-2)]")

        with ui.row().classes("items-center gap-3 flex-wrap"):
            # Scenario Selector Dropdown
            scenario_options = scenario_registry.getScenarioOptions()
            ui.select(
                options=scenario_options,
                value=current_scenario_id,
                on_change=lambda e: on_scenario_change(e.value),
            ).props(
                'outlined dense options-dense popup-content-class="app-select-popup"'
            ).classes(
                "w-80 md:w-96 bg-[var(--input-bg)] text-[var(--text-1)] text-xs rounded-lg border border-[var(--border-accent)] shadow-sm"
            )

            # Course Badge
            with ui.row().classes(
                "items-center gap-2 px-3 py-1.5 rounded-lg bg-[var(--badge-bg)] border border-[var(--border)] text-xs text-[var(--text-1)] shadow-sm"
            ):
                ui.html('<i class="fa-solid fa-graduation-cap text-[#f59e0b]"></i>')
                course_label = ui.label(initial_course_tag)

            # Switchable Theme Button (Light/Dark Toggle)
            ui.html(
                """
                <button id="theme-toggle-btn" onclick="toggleAppTheme()" class="btn-secondary" title="Toggle Light / Dark Theme">
                    <i class="fa-solid fa-moon text-[#71717a]"></i>
                    <span class="theme-btn-label">Dark</span>
                </button>
                """,
                sanitize=False,
            )

            # Print / PDF Export Menu
            with ui.button("Print / PDF", icon="print").props("outline dense").classes(
                "text-xs text-[var(--accent)] border-[var(--border-accent)] hover:bg-[var(--surface-hover)] font-bold shadow-sm"
            ):
                with ui.menu().classes("bg-[var(--menu-bg)] text-[var(--text-1)] border border-[var(--border-accent)] shadow-xl"):
                    ui.menu_item(
                        "Print All (A4 PDF)",
                        on_click=lambda: ui.run_javascript("printERSection('all');"),
                    ).classes("text-xs hover:bg-[var(--surface-hover)] font-bold text-[var(--accent)]")
                    ui.separator().classes("bg-[var(--border)]")
                    ui.menu_item(
                        "1. Requirements Text Canvas",
                        on_click=lambda: ui.run_javascript("printERSection('canvas');"),
                    ).classes("text-xs hover:bg-[var(--surface-hover)]")
                    ui.menu_item(
                        "2. Attributes & Classification",
                        on_click=lambda: ui.run_javascript("printERSection('attributes');"),
                    ).classes("text-xs hover:bg-[var(--surface-hover)]")
                    ui.menu_item(
                        "3. Key Analysis & PK",
                        on_click=lambda: ui.run_javascript("printERSection('keys');"),
                    ).classes("text-xs hover:bg-[var(--surface-hover)]")
                    ui.menu_item(
                        "4. Relationships & Cardinalities",
                        on_click=lambda: ui.run_javascript("printERSection('relationships');"),
                    ).classes("text-xs hover:bg-[var(--surface-hover)]")
                    ui.menu_item(
                        "5. Crow's Foot Diagram",
                        on_click=lambda: ui.run_javascript("printERSection('er-diagram');"),
                    ).classes("text-xs hover:bg-[var(--surface-hover)]")
                    ui.menu_item(
                        "6. Relational Implementation (SQL DDL)",
                        on_click=lambda: ui.run_javascript("printERSection('sql-ddl');"),
                    ).classes("text-xs hover:bg-[var(--surface-hover)]")

    return {"subtitle_label": subtitle_label, "course_label": course_label}
