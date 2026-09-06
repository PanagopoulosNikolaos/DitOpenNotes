"""Header and navigation toolbar component for Discrete Mathematics application."""

from typing import Callable, Dict, Any, Optional
from nicegui import ui
from models.scenario import Scenario
from models.registry import scenario_registry


def renderHeader(
    scenario: Optional[Scenario],
    selected_scenario_id: str,
    on_scenario_change: Callable[[str], None],
) -> Dict[str, Any]:
    """Renders the sticky application header and scenario selector dropdown.

    Args:
        scenario (Optional[Scenario]): Currently active scenario or None if theory.
        selected_scenario_id (str): ID string of currently active scenario or 'theory'.
        on_scenario_change (Callable[[str], None]): Callback triggered when scenario changes.

    Returns:
        Dict[str, Any]: References to reactive label elements for title/subtitle updates.
    """
    header_refs: Dict[str, Any] = {}

    course_tag_text = scenario.course_tag if scenario else "Θεωρία / Οδηγός"
    subtitle_text = scenario.subtitle if scenario else "Πλήρης Θεωρία & Μεθοδολογία για το 100/100"

    with ui.header().classes("w-full bg-[var(--surface)] border-b border-[var(--border)] px-4 py-3 sticky top-0 z-50 shadow-sm backdrop-blur-md items-center justify-between"):
        with ui.row().classes("w-full max-w-7xl mx-auto items-center justify-between flex-wrap gap-4"):
            # Left: Course Title & Active Scenario Subtitle
            with ui.row().classes("items-center gap-3"):
                ui.html('<i class="fa-solid fa-square-root-variable text-[var(--accent)] text-2xl"></i>')
                with ui.column().classes("gap-0"):
                    with ui.row().classes("items-center gap-2"):
                        ui.label("Διακριτά Μαθηματικά").classes("text-lg font-black tracking-tight text-[var(--text-1)]")
                        course_badge = ui.label(course_tag_text).classes(
                            "text-xs px-2 py-0.5 rounded-full font-bold bg-[var(--surface-2)] text-[var(--accent)] border border-[var(--border-accent)]"
                        )
                        header_refs["course_label"] = course_badge
                    subtitle_label = ui.label(subtitle_text).classes("text-xs text-[var(--text-3)] font-medium")
                    header_refs["subtitle_label"] = subtitle_label

            # Right: Controls (Scenario Selector, Theme Toggle, Export)
            with ui.row().classes("items-center gap-3 flex-wrap"):
                # Scenario Dropdown Selector
                scenario_options = scenario_registry.getScenarioOptions()
                selector = ui.select(
                    options=scenario_options,
                    value=selected_scenario_id,
                    on_change=lambda e: on_scenario_change(e.value),
                ).props('dense outlined options-dense popup-content-class="scenario-select-popup"').classes("w-72 text-xs bg-[var(--bg-base)] rounded-lg")
                header_refs["selector"] = selector

                # Light / Dark Theme Switcher Button
                ui.button(
                    icon="fa-solid fa-moon",
                    on_click=lambda: ui.run_javascript("toggleAppTheme();"),
                ).props("flat dense round").classes(
                    "text-[var(--text-2)] hover:text-[var(--accent)] transition-colors"
                ).tooltip("Εναλλαγή Θέματος (Φωτεινό / Σκοτεινό)").props('id="theme-toggle-btn"')

                # Print & PDF Export Menu
                with ui.button(icon="fa-solid fa-print").props("flat dense round").classes(
                    "text-[var(--text-2)] hover:text-[var(--accent)] transition-colors"
                ).tooltip("Επιλογές Εκτύπωσης / Εξαγωγής"):
                    with ui.menu().classes("p-2 bg-[var(--surface)] border border-[var(--border)] rounded-xl shadow-lg"):
                        with ui.column().classes("gap-1 text-xs"):
                            ui.button(
                                "Πλήρης Αναφορά Εξέτασης (A4 PDF)",
                                icon="fa-solid fa-file-pdf",
                                on_click=lambda: ui.run_javascript("window.print();"),
                            ).props("flat dense").classes("justify-start text-[var(--text-1)] hover:text-[var(--accent)] w-full")
                            ui.button(
                                "Λήψη Αυτόνομου HTML Οδηγού",
                                icon="fa-solid fa-download",
                                on_click=lambda: ui.run_javascript("downloadStandaloneHTML();"),
                            ).props("flat dense").classes("justify-start text-[var(--text-1)] hover:text-[var(--accent)] w-full")

    return header_refs
