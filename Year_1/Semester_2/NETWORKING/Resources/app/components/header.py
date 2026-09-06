"""Header navigation component for the Computer Networks exam application."""

from typing import Callable, Optional
from nicegui import ui
from models.scenario import Scenario
from models.registry import scenario_registry


def renderHeader(
    current_scenario: Optional[Scenario],
    current_scenario_id: str,
    on_scenario_change: Callable[[str], None],
) -> dict:
    """Renders the top header with title, scenario selector, theme toggle, and print menu.

    Args:
        current_scenario (Optional[Scenario]): The currently active scenario or None.
        current_scenario_id (str): The ID of the active scenario or 'theory'.
        on_scenario_change (Callable[[str], None]): Callback on scenario selection.

    Returns:
        dict: References to the dynamic header label elements.
    """
    initial_subtitle = (
        current_scenario.subtitle
        if current_scenario
        else "Πλήρης Θεωρία, Τύποι, Αλγόριθμοι & Παγίδες Εξετάσεων"
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
            ui.html('<i class="fa-solid fa-network-wired text-[var(--accent)] text-2xl"></i>')
            with ui.column().classes("gap-0"):
                ui.html('<h1 class="gradient-title text-xl md:text-2xl font-black">Δίκτυα Υπολογιστών: Λυμένες Εξετάσεις</h1>')
                subtitle_label = ui.label(initial_subtitle).classes("text-xs text-[var(--text-2)]")

        with ui.row().classes("items-center gap-3 flex-wrap"):
            # Scenario selector dropdown (the single top-level switcher)
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

            # Course badge
            with ui.row().classes(
                "items-center gap-2 px-3 py-1.5 rounded-lg bg-[var(--badge-bg)] border border-[var(--border)] text-xs text-[var(--text-1)] shadow-sm"
            ):
                ui.html('<i class="fa-solid fa-graduation-cap text-amber-500"></i>')
                course_label = ui.label(initial_course_tag)

            # Light/Dark theme toggle
            ui.html(
                """
                <button id="theme-toggle-btn" onclick="toggleAppTheme()" class="btn-secondary" title="Εναλλαγή Φωτεινού / Σκοτεινού Θέματος">
                    <i class="fa-solid fa-moon text-slate-500"></i>
                    <span class="theme-btn-label">Σκοτεινό</span>
                </button>
                """,
                sanitize=False,
            )

            # Print / PDF export menu
            with ui.button("Εκτύπωση / PDF", icon="print").props("outline dense").classes(
                "text-xs text-[var(--accent)] border-[var(--border-accent)] hover:bg-[var(--surface-hover)] font-bold shadow-sm"
            ):
                with ui.menu().classes("bg-[var(--menu-bg)] text-[var(--text-1)] border border-[var(--border-accent)] shadow-xl"):
                    ui.menu_item(
                        "Εκτύπωση Όλων (A4 PDF)",
                        on_click=lambda: ui.run_javascript("printExamSection('all');"),
                    ).classes("text-xs hover:bg-[var(--surface-hover)] font-bold text-[var(--accent)]")
                    ui.separator().classes("bg-[var(--border)]")
                    ui.menu_item(
                        "1. Πλήρες Κείμενο Εξέτασης (Canvas)",
                        on_click=lambda: ui.run_javascript("printExamSection('canvas');"),
                    ).classes("text-xs hover:bg-[var(--surface-hover)]")
                    ui.menu_item(
                        "2. Λύσεις ανά Θέμα (Βήμα-Βήμα)",
                        on_click=lambda: ui.run_javascript("printExamSection('solutions');"),
                    ).classes("text-xs hover:bg-[var(--surface-hover)]")
                    ui.menu_item(
                        "3. Πίνακες Ανάλυσης & Αναφοράς",
                        on_click=lambda: ui.run_javascript("printExamSection('tables');"),
                    ).classes("text-xs hover:bg-[var(--surface-hover)]")
                    ui.menu_item(
                        "4. Διάγραμμα Τοπολογίας / Κατανομής",
                        on_click=lambda: ui.run_javascript("printExamSection('diagram');"),
                    ).classes("text-xs hover:bg-[var(--surface-hover)]")
                    ui.menu_item(
                        "5. Κώδικας Επαλήθευσης (Python)",
                        on_click=lambda: ui.run_javascript("printExamSection('code');"),
                    ).classes("text-xs hover:bg-[var(--surface-hover)]")
                    ui.separator().classes("bg-[var(--border)]")
                    ui.menu_item(
                        "Εξαγωγή Αυτόνομου HTML",
                        on_click=lambda: ui.run_javascript("downloadStandaloneHTML();"),
                    ).classes("text-xs hover:bg-[var(--surface-hover)] font-bold text-blue-500")

    return {"subtitle_label": subtitle_label, "course_label": course_label}
