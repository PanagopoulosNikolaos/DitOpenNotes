"""Header navigation component supporting Study and Exams main modules."""

from typing import Callable, Optional
from nicegui import ui
from models.scenario import NetworkScenario
from models.registry import scenario_registry


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
        dict: Dynamic header element references.
    """
    is_study = (current_mode == "study")
    initial_subtitle = (
        "Πλήρης Θεωρία, Σημειώσεις Μαθήματος & Διαδραστικοί Υπολογιστές"
        if is_study
        else (current_scenario.subtitle if current_scenario else "Θέματα Εξετάσεων με Αναλυτικές Βήμα-προς-Βήμα Λύσεις")
    )
    initial_badge = "Ενότητα: Study" if is_study else (current_scenario.course_tag if current_scenario else "Ενότητα: Exams")

    with ui.header().classes(
        "w-full bg-[#141413]/90 backdrop-blur-md border-b border-[rgba(224,107,58,0.25)] "
        "px-6 py-4 flex flex-col md:flex-row justify-between items-center gap-4 z-50 sticky top-0"
    ):
        # Left Title Area
        with ui.row().classes("items-center gap-4"):
            ui.html('<i class="fa-solid fa-network-wired text-[#e06b3a] text-2xl"></i>')
            with ui.column().classes("gap-0"):
                ui.html('<h1 class="gradient-title text-xl md:text-2xl font-black m-0">Δίκτυα Υπολογιστών: Interactive Learning & Exams</h1>')
                subtitle_label = ui.label(initial_subtitle).classes("text-xs text-[#b5b0a4]")

        # Center / Right Navigation Controls
        with ui.row().classes("items-center gap-3 flex-wrap"):
            # Main Module Toggle Buttons (Study vs Exams)
            with ui.row().classes("p-1 rounded-xl bg-[#201f1d] border border-[rgba(255,255,255,0.08)] gap-1"):
                study_btn_cls = "bg-[rgba(224,107,58,0.25)] text-[#fed7aa] border border-[#e06b3a]" if is_study else "text-[#b5b0a4] hover:text-[#f4f1ea]"
                exam_btn_cls = "bg-[rgba(224,107,58,0.25)] text-[#fed7aa] border border-[#e06b3a]" if not is_study else "text-[#b5b0a4] hover:text-[#f4f1ea]"

                ui.button(
                    "Study (Σημειώσεις & Θεωρία)",
                    icon="book-open",
                    on_click=lambda: on_mode_change("study"),
                ).props("flat dense").classes(f"text-xs font-bold px-3 py-1.5 rounded-lg transition-all {study_btn_cls}")

                ui.button(
                    "Exams (Θέματα & Λύσεις)",
                    icon="graduation-cap",
                    on_click=lambda: on_mode_change("exams"),
                ).props("flat dense").classes(f"text-xs font-bold px-3 py-1.5 rounded-lg transition-all {exam_btn_cls}")

            # Sub-module Selector Dropdown
            sub_options = scenario_registry.getStudyOptions() if is_study else scenario_registry.getExamOptions()
            sub_select = ui.select(
                options=sub_options,
                value=current_sub_id,
                on_change=lambda e: on_sub_change(e.value),
            ).props(
                "outlined dense dark options-dense options-dark"
            ).classes(
                "w-72 md:w-84 bg-[#201f1d] text-[#f4f1ea] text-xs rounded-lg border border-[rgba(224,107,58,0.4)]"
            )

            # Mode/Course Badge
            with ui.row().classes(
                "items-center gap-2 px-3 py-1.5 rounded-lg bg-[#201f1d] border border-[rgba(255,255,255,0.08)] text-xs text-[#f4f1ea]"
            ):
                ui.html('<i class="fa-solid fa-tag text-[#f59e0b]"></i>')
                badge_label = ui.label(initial_badge)

            # Print Action
            with ui.button("Εκτύπωση / PDF", icon="print").props("outline dense").classes(
                "text-xs text-[#fdba74] border-[rgba(224,107,58,0.5)] hover:bg-[#e06b3a]/20 font-bold"
            ):
                with ui.menu().classes("bg-[#1c1b1a] text-[#f4f1ea] border border-[rgba(224,107,58,0.3)] shadow-xl"):
                    ui.menu_item(
                        "Εκτύπωση Σελίδας (A4 PDF)",
                        on_click=lambda: ui.run_javascript("window.print();"),
                    ).classes("text-xs hover:bg-[#e06b3a]/20 font-bold text-[#fdba74]")

    return {
        "subtitle_label": subtitle_label,
        "badge_label": badge_label,
        "sub_select": sub_select,
    }
