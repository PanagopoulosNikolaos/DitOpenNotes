"""Header navigation component for the Computer Networks application."""

from typing import Callable, Optional
from nicegui import ui
from models.scenario import NetworkScenario
from models.registry import scenario_registry


def renderHeader(
    current_scenario: Optional[NetworkScenario],
    current_scenario_id: str,
    on_scenario_change: Callable[[str], None],
) -> dict:
    """Renders the top application header with title, topic selector, and badges.

    Args:
        current_scenario (Optional[NetworkScenario]): The active scenario or None if theory.
        current_scenario_id (str): The ID of the currently active scenario or theory topic.
        on_scenario_change (Callable[[str], None]): Callback triggered when a new topic is selected.

    Returns:
        dict: References to dynamic header label elements.
    """
    initial_subtitle = (
        current_scenario.subtitle
        if current_scenario
        else "Πλήρης Θεωρία, Μεθοδολογία & Διαδραστικά Εργαλεία Δικτύων"
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
            ui.html('<i class="fa-solid fa-network-wired text-[#e06b3a] text-2xl"></i>')
            with ui.column().classes("gap-0"):
                ui.html('<h1 class="gradient-title text-xl md:text-2xl font-black m-0">Δίκτυα Υπολογιστών: Διαδραστικός Οδηγός & Εξετάσεις</h1>')
                subtitle_label = ui.label(initial_subtitle).classes("text-xs text-[#b5b0a4]")

        with ui.row().classes("items-center gap-3 flex-wrap"):
            # Scenario / Theory Selector Dropdown
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
                        on_click=lambda: ui.run_javascript("window.print();"),
                    ).classes("text-xs hover:bg-[#e06b3a]/20 font-bold text-[#fdba74]")

    return {"subtitle_label": subtitle_label, "course_label": course_label}
