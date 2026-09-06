"""Header navigation component for the Digital Electronics application."""

from typing import Callable, Optional, Dict, Any
from nicegui import ui
from models.scenario import Scenario
from models.registry import scenario_registry


def renderHeader(
    current_scenario: Optional[Scenario],
    current_scenario_id: str,
    on_scenario_change: Callable[[str], None],
) -> Dict[str, Any]:
    """Renders the top application header with title, scenario selector, and theme controls.

    Args:
        current_scenario (Optional[Scenario]): The currently active scenario or None.
        current_scenario_id (str): The ID of the currently active scenario or 'theory'.
        on_scenario_change (Callable[[str], None]): Callback triggered when a new scenario is selected.

    Returns:
        Dict[str, Any]: References to dynamic header label elements.
    """
    initial_subtitle = (
        current_scenario.subtitle
        if current_scenario
        else "Πλήρης Θεωρία, Συνδυαστικά/Ακολουθιακά Κυκλώματα, FSM & VHDL"
    )
    initial_course_tag = (
        current_scenario.course_tag
        if current_scenario
        else "Θεωρία / Οδηγός"
    )

    with ui.header().classes(
        "w-full bg-[var(--header-bg)] backdrop-blur-md border-b border-[var(--border-accent)] "
        "px-6 py-4 flex flex-col md:flex-row justify-between items-center gap-4 z-50 sticky top-0 transition-colors"
    ):
        with ui.row().classes("items-center gap-4"):
            ui.html('<i class="fa-solid fa-microchip text-[var(--accent)] text-2xl"></i>')
            with ui.column().classes("gap-0"):
                ui.html('<h1 class="text-xl md:text-2xl font-black text-[var(--text-1)] m-0">Ψηφιακά Ηλεκτρονικά</h1>')
                subtitle_label = ui.label(initial_subtitle).classes("text-xs text-[var(--text-2)]")

        with ui.row().classes("items-center gap-3 flex-wrap"):
            # Whitelist Control: Single Scenario Selector Dropdown
            scenario_options = scenario_registry.getScenarioOptions()
            ui.select(
                options=scenario_options,
                value=current_scenario_id,
                on_change=lambda e: on_scenario_change(e.value),
            ).props(
                'outlined dense options-dense popup-content-class="app-select-popup"'
            ).classes(
                "w-80 md:w-96 text-xs rounded-lg shadow-sm"
            )

            # Course Badge
            with ui.row().classes(
                "items-center gap-2 px-3 py-1.5 rounded-lg bg-[var(--badge-bg)] border border-[var(--border)] text-xs text-[var(--text-1)] shadow-sm"
            ):
                ui.html('<i class="fa-solid fa-graduation-cap text-[var(--amber)]"></i>')
                course_label = ui.label(initial_course_tag)

            # Whitelist Control: Switchable Theme Button (Light/Dark Toggle)
            ui.html(
                """
                <button id="theme-toggle-btn" onclick="toggleAppTheme()" class="filter-chip-btn" title="Εναλλαγή Φωτεινού / Σκοτεινού Θέματος">
                    <i class="fa-solid fa-moon text-[var(--text-3)]"></i>
                    <span class="theme-btn-label">Θέμα</span>
                </button>
                """,
                sanitize=False,
            )

            # Whitelist Control: Print / PDF Export Menu
            with ui.button("Εκτύπωση / PDF", icon="print").props("outline dense").classes(
                "text-xs text-[var(--accent)] border-[var(--border-accent)] hover:bg-[var(--surface-hover)] font-bold shadow-sm"
            ):
                with ui.menu().classes("bg-[var(--menu-bg)] text-[var(--text-1)] border border-[var(--border-accent)] shadow-xl"):
                    ui.menu_item(
                        "Πλήρης Αναφορά Θέματος (A4 PDF)",
                        on_click=lambda: ui.run_javascript("printSection('all');"),
                    ).classes("text-xs hover:bg-[var(--surface-hover)] font-bold text-[var(--accent)]")
                    ui.separator().classes("bg-[var(--border)]")
                    ui.menu_item(
                        "1. Canvas Θεμάτων Εξέτασης",
                        on_click=lambda: ui.run_javascript("printSection('interactive-text-canvas');"),
                    ).classes("text-xs hover:bg-[var(--surface-hover)]")
                    ui.menu_item(
                        "2. Αναλυτικές Λύσεις & Υπολογισμοί",
                        on_click=lambda: ui.run_javascript("printSection('solution-sheet-section');"),
                    ).classes("text-xs hover:bg-[var(--surface-hover)]")
                    ui.menu_item(
                        "3. Διαδραστικό Διάγραμμα FSM / Κυκλώματος",
                        on_click=lambda: ui.run_javascript("printSection('visual-diagram-section');"),
                    ).classes("text-xs hover:bg-[var(--surface-hover)]")
                    ui.menu_item(
                        "4. Κώδικας VHDL & Επαλήθευση",
                        on_click=lambda: ui.run_javascript("printSection('solution-code-section');"),
                    ).classes("text-xs hover:bg-[var(--surface-hover)]")
                    ui.separator().classes("bg-[var(--border)]")
                    ui.menu_item(
                        "Εξαγωγή Αυτόνομου HTML",
                        on_click=lambda: ui.run_javascript("downloadStandaloneHTML();"),
                    ).classes("text-xs hover:bg-[var(--surface-hover)] font-semibold text-[var(--blue-action)]")

    return {"subtitle_label": subtitle_label, "course_label": course_label}
