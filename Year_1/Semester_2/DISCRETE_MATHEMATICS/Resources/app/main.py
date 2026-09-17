"""Main NiceGUI Application for Course 203: Discrete Mathematics.

Interactive learning dashboard, exam problem walkthroughs with multi-team variations,
algorithmic workbench (graphs, truth tables, Venn diagrams, automata, induction),
and comprehensive syllabus theory handbook.
"""

from nicegui import ui
import config
from models.registry import scenario_registry
import scenarios  # Initializes and registers all course exam scenarios
from components import (
    renderHeader,
    renderDashboardMetrics,
    renderVisualSimulator,
    renderAllProblemCards,
    renderTheoryPage,
)


class DiscreteMathApp:
    """Main application controller managing UI state, route selection, and reactive rendering."""

    def __init__(self) -> None:
        """Initializes the Discrete Mathematics application with the default scenario."""
        default_scenario = scenario_registry.getDefaultScenario()
        self.current_scenario_id = default_scenario.id if default_scenario else "past_exam_june_2025"

    def selectScenario(self, scenario_id: str, content_container: ui.column) -> None:
        """Switches active exam scenario or theory guide and re-renders the dynamic content area.

        Args:
            scenario_id (str): The unique ID of the scenario or 'theory'.
            content_container (ui.column): Container element holding dynamic view components.

        Returns:
            None
        """
        self.current_scenario_id = scenario_id
        content_container.clear()
        with content_container:
            self.renderScenarioContent()

        # Re-trigger KaTeX mathematical rendering on dynamic content update
        ui.run_javascript("setTimeout(() => { if (typeof renderKaTeX === 'function') renderKaTeX(); }, 80);")

    def renderScenarioContent(self) -> None:
        """Renders either the master theory handbook or the selected exam dashboard."""
        if self.current_scenario_id == "theory":
            renderTheoryPage()
            return

        scenario = scenario_registry.getScenario(self.current_scenario_id)
        if not scenario:
            ui.label("Το επιλεγμένο θέμα δεν βρέθηκε.").classes("text-red-500 p-4")
            return

        with ui.column().classes("w-full px-5 py-8 space-y-8 items-stretch max-w-7xl mx-auto"):
            # SECTION 1: Top-Level KPI Dashboard & Formula Quick Reference
            renderDashboardMetrics(scenario)

            # SECTION 2: Interactive Algorithmic Workbench & Simulators
            renderVisualSimulator(scenario)

            # SECTION 3: Structured Problem Walkthrough Cards
            renderAllProblemCards(scenario.exercises)


def buildApp() -> None:
    """Builds the main NiceGUI web layout, registers global scripts, and defines routes."""
    # Inject CSS design tokens, typography, and KaTeX script loader
    ui.add_head_html(f"<style>{config.CUSTOM_CSS}</style>", shared=True)
    ui.add_head_html(config.THEME_HEAD_SCRIPT, shared=True)

    app_controller = DiscreteMathApp()

    @ui.page("/")
    def mainPage() -> None:
        """Root page route handler rendering sticky header and dynamic body."""
        # Synchronize stored theme on page connection without competing with dark_mode.js
        ui.run_javascript("if (typeof setAppTheme === 'function') setAppTheme(getAppTheme());")

        current_scenario = scenario_registry.getScenario(app_controller.current_scenario_id)
        content_container = ui.column().props('id="content-area"').classes("w-full gap-0 p-0 items-stretch")

        is_updating = False

        def handleScenarioSwitch(new_id: str) -> None:
            """Handles dropdown change events for scenarios.

            Args:
                new_id (str): The unique scenario identifier or 'theory'.

            Returns:
                None
            """
            nonlocal is_updating
            if not new_id or is_updating:
                return
            is_updating = True
            try:
                app_controller.selectScenario(new_id, content_container)
                if header_refs.get("scenario_select") and header_refs["scenario_select"].value != new_id:
                    header_refs["scenario_select"].set_value(new_id)
                if new_id == "theory":
                    header_refs["subtitle_label"].set_text("Πλήρης Θεωρία, Μεθοδολογία & Συμβολισμοί (Course 203)")
                    header_refs["course_label"].set_text("Θεωρία / Οδηγός")
                else:
                    new_scenario = scenario_registry.getScenario(new_id)
                    if new_scenario:
                        header_refs["subtitle_label"].set_text(new_scenario.subtitle)
                        header_refs["course_label"].set_text(new_scenario.course_tag)
            finally:
                is_updating = False

        # Sticky Top Header
        header_refs = renderHeader(current_scenario, app_controller.current_scenario_id, handleScenarioSwitch)

        # Main Dynamic Dashboard Container
        with content_container:
            app_controller.renderScenarioContent()


buildApp()

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(
        title="Διακριτά Μαθηματικά (Course 203) - Dashboard & Εργαστήριο",
        port=8080,
        reload=False,
    )
