"""Header navigation component supporting Study and Exams main modules."""

from typing import Callable, Optional
from nicegui import ui
from models.scenario import NetworkScenario
from models.registry import scenario_registry


# Visual style classes for active and idle mode toggle buttons
_BTN_ACTIVE_CLASSES = "!bg-[rgba(224,107,58,0.25)] !text-[#fed7aa] !border-[rgba(224,107,58,0.8)] shadow-sm"
_BTN_IDLE_CLASSES   = "!bg-transparent !text-[#b5b0a4] hover:!text-[#f4f1ea] !border-transparent"


def renderHeader(
    current_mode: str,  # 'study' or 'exams'
    current_sub_id: str,
    on_mode_change: Callable[[str], None],
    on_sub_change: Callable[[str], None],
    current_scenario: Optional[NetworkScenario] = None,
) -> dict:
    """Renders the top application header with primary Study/Exams switcher and sub-module selector.

    Args:
        current_mode (str): The active primary mode ('study' or 'exams').
        current_sub_id (str): The active sub-module ID within the current mode.
        on_mode_change (Callable[[str], None]): Callback when switching main mode.
        on_sub_change (Callable[[str], None]): Callback when switching sub-module.
        current_scenario (Optional[NetworkScenario]): Active scenario object if in exam mode.

    Returns:
        dict: Dynamic header element references including mode toggle buttons.
    """
    is_study = (current_mode == "study")
    initial_subtitle = (
        "Complete Theory, Course Notes & Interactive Calculators"
        if is_study
        else (current_scenario.subtitle if current_scenario else "Exam Scenarios with Detailed Step-by-Step Solutions")
    )
    initial_badge = "Module: Study" if is_study else (current_scenario.course_tag if current_scenario else "Module: Exams")

    with ui.header().classes(
        "w-full bg-[#141413]/95 backdrop-blur-md border-b border-[rgba(224,107,58,0.25)] "
        "px-4 md:px-8 py-3.5 flex flex-col md:flex-row justify-between items-center gap-4 z-50 sticky top-0 shadow-lg"
    ):
        # Left Title Area
        with ui.row().classes("items-center gap-3.5"):
            ui.html('<i class="fa-solid fa-network-wired text-[#e06b3a] text-2xl"></i>')
            with ui.column().classes("gap-0"):
                ui.html('<h1 class="gradient-title text-lg md:text-xl font-extrabold m-0 tracking-wide">Computer Networks: Interactive Learning & Exams</h1>')
                subtitle_label = ui.label(initial_subtitle).classes("text-xs text-[#b5b0a4] font-medium")

        # Center / Right Navigation Controls
        with ui.row().classes("items-center gap-3 flex-wrap justify-end"):
            # Main Module Toggle Buttons (Study vs Exams)
            with ui.row().classes("p-1 rounded-xl bg-[#201f1d] border border-[rgba(255,255,255,0.08)] gap-1.5 items-center"):
                study_btn = ui.button(
                    "Study (Notes)",
                    icon="menu_book",
                    on_click=lambda: on_mode_change("study"),
                ).props("flat dense no-caps").classes(
                    f"text-xs font-bold px-3 py-1.5 rounded-lg border transition-all cursor-pointer "
                    f"{_BTN_ACTIVE_CLASSES if is_study else _BTN_IDLE_CLASSES}"
                )

                exam_btn = ui.button(
                    "Exams (Papers & Solutions)",
                    icon="school",
                    on_click=lambda: on_mode_change("exams"),
                ).props("flat dense no-caps").classes(
                    f"text-xs font-bold px-3 py-1.5 rounded-lg border transition-all cursor-pointer "
                    f"{_BTN_ACTIVE_CLASSES if not is_study else _BTN_IDLE_CLASSES}"
                )

            # Sub-module Selector Dropdown
            sub_options = scenario_registry.getStudyOptions() if is_study else scenario_registry.getExamOptions()
            
            def handleSelectChange(e) -> None:
                """Safely handles dropdown selection avoiding null event triggers."""
                if e.value:
                    on_sub_change(e.value)

            sub_select = ui.select(
                options=sub_options,
                value=current_sub_id,
                on_change=handleSelectChange,
            ).props(
                "outlined dense dark options-dense options-dark behavior=menu"
            ).classes(
                "w-64 md:w-80 bg-[#201f1d] text-[#f4f1ea] text-xs rounded-lg border border-[rgba(224,107,58,0.4)]"
            )

            # Mode/Course Badge
            with ui.row().classes(
                "items-center gap-2 px-3 py-1.5 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.08)] text-xs text-[#f4f1ea] hidden lg:flex"
            ):
                ui.html('<i class="fa-solid fa-tag text-[#f59e0b]"></i>')
                badge_label = ui.label(initial_badge).classes("font-medium")

            # Print Page Action Button
            print_btn = ui.button(
                "Print / PDF",
                icon="print",
                on_click=lambda: ui.run_javascript("window.print();"),
            ).props("outline dense no-caps").classes(
                "text-xs text-[#fdba74] border-[rgba(224,107,58,0.5)] hover:bg-[#e06b3a]/20 font-bold px-3 py-1.5 rounded-lg cursor-pointer"
            )

    return {
        "subtitle_label": subtitle_label,
        "badge_label": badge_label,
        "sub_select": sub_select,
        "study_btn": study_btn,
        "exam_btn": exam_btn,
    }
