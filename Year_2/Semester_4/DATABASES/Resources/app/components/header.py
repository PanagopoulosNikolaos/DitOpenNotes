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
    """Renders the top application header with title, scenario selector, and badges.

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
        else "Πλήρης Θεωρία, Μεθοδολογία & Συμβολισμοί Crow's Foot"
    )
    initial_course_tag = (
        current_scenario.course_tag
        if current_scenario
        else "Θεωρία / Οδηγός"
    )

    with ui.header().classes(
        "w-full bg-[#141413]/90 backdrop-blur-md border-b border-[rgba(224,107,58,0.25)] "
        "px-6 py-4 flex flex-col md:flex-row justify-between items-center gap-4 z-50 sticky top-0"
    ):
        with ui.row().classes("items-center gap-4"):
            ui.html('<i class="fa-solid fa-diagram-project text-[#e06b3a] text-2xl"></i>')
            with ui.column().classes("gap-0"):
                ui.html('<h1 class="gradient-title text-xl md:text-2xl font-black">Οδηγός Ανάλυσης Μοντέλου Ε-Ρ</h1>')
                subtitle_label = ui.label(initial_subtitle).classes("text-xs text-[#b5b0a4]")

        with ui.row().classes("items-center gap-3 flex-wrap"):
            # Scenario Selector Dropdown
            scenario_options = scenario_registry.getScenarioOptions()
            ui.select(
                options=scenario_options,
                value=current_scenario_id,
                on_change=lambda e: on_scenario_change(e.value),
            ).props(
                "outlined dense dark options-dense options-dark"
            ).classes(
                "w-80 md:w-96 bg-[#201f1d] text-[#f4f1ea] text-xs rounded-lg border border-[rgba(224,107,58,0.4)]"
            )

            # Course Badge
            with ui.row().classes(
                "items-center gap-2 px-3 py-1.5 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.08)] text-xs text-[#f4f1ea]"
            ):
                ui.html('<i class="fa-solid fa-graduation-cap text-[#f59e0b]"></i>')
                course_label = ui.label(initial_course_tag)

            # Print / PDF Export Menu
            with ui.button("Εκτύπωση / PDF", icon="print").props("outline dense").classes(
                "text-xs text-[#fdba74] border-[rgba(224,107,58,0.5)] hover:bg-[#e06b3a]/20 font-bold"
            ):
                with ui.menu().classes("bg-[#1c1b1a] text-[#f4f1ea] border border-[rgba(224,107,58,0.3)] shadow-xl"):
                    ui.menu_item(
                        "Εκτύπωση Όλων (A4 PDF)",
                        on_click=lambda: ui.run_javascript("printERSection('all');"),
                    ).classes("text-xs hover:bg-[#e06b3a]/20 font-bold text-[#fdba74]")
                    ui.separator().classes("bg-white/10")
                    ui.menu_item(
                        "1. Canvas Κειμένου Απαιτήσεων",
                        on_click=lambda: ui.run_javascript("printERSection('canvas');"),
                    ).classes("text-xs hover:bg-white/5")
                    ui.menu_item(
                        "2. Γνωρίσματα & Είδος",
                        on_click=lambda: ui.run_javascript("printERSection('attributes');"),
                    ).classes("text-xs hover:bg-white/5")
                    ui.menu_item(
                        "3. Ανάλυση Κλειδιών & PK",
                        on_click=lambda: ui.run_javascript("printERSection('keys');"),
                    ).classes("text-xs hover:bg-white/5")
                    ui.menu_item(
                        "4. Σχέσεις & Πληθικότητες",
                        on_click=lambda: ui.run_javascript("printERSection('relationships');"),
                    ).classes("text-xs hover:bg-white/5")
                    ui.menu_item(
                        "5. Διάγραμμα Crow's Foot",
                        on_click=lambda: ui.run_javascript("printERSection('er-diagram');"),
                    ).classes("text-xs hover:bg-white/5")
                    ui.menu_item(
                        "6. Σχεσιακή Υλοποίηση (SQL DDL)",
                        on_click=lambda: ui.run_javascript("printERSection('sql-ddl');"),
                    ).classes("text-xs hover:bg-white/5")

    return {"subtitle_label": subtitle_label, "course_label": course_label}
