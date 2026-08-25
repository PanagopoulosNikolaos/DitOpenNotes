"""Header navigation component for the ER Analysis application."""

from typing import Callable
from nicegui import ui
from models.scenario import Scenario
from models.registry import scenario_registry


def renderHeader(current_scenario: Scenario, on_scenario_change: Callable[[str], None]) -> None:
    """Renders the top application header with title, scenario selector, and badges.

    Args:
        current_scenario (Scenario): The currently active scenario.
        on_scenario_change (Callable[[str], None]): Callback triggered when a new scenario is selected.

    Returns:
        None
    """
    with ui.header().classes(
        "w-full bg-[#141413]/90 backdrop-blur-md border-b border-[rgba(224,107,58,0.25)] "
        "px-6 py-4 flex flex-col md:flex-row justify-between items-center gap-4 z-50 sticky top-0"
    ):
        with ui.row().classes("items-center gap-4"):
            ui.html('<i class="fa-solid fa-diagram-project text-[#e06b3a] text-2xl"></i>')
            with ui.column().classes("gap-0"):
                ui.html('<h1 class="gradient-title text-xl md:text-2xl font-black">Οδηγός Ανάλυσης Μοντέλου Ε-Ρ</h1>')
                ui.label(current_scenario.subtitle).classes("text-xs text-[#b5b0a4]")

        with ui.row().classes("items-center gap-3 flex-wrap"):
            # Scenario Selector Dropdown
            scenario_options = scenario_registry.getScenarioOptions()
            ui.select(
                options=scenario_options,
                value=current_scenario.id,
                on_change=lambda e: on_scenario_change(e.value),
            ).props(
                "outlined dense dark options-dense options-dark"
            ).classes(
                "w-72 bg-[#201f1d] text-[#f4f1ea] text-xs rounded-lg border border-[rgba(224,107,58,0.4)]"
            )

            # Course Badge
            with ui.row().classes(
                "items-center gap-2 px-3 py-1.5 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.08)] text-xs text-[#f4f1ea]"
            ):
                ui.html('<i class="fa-solid fa-graduation-cap text-[#f59e0b]"></i>')
                ui.label(current_scenario.course_tag)
