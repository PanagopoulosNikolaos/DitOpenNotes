"""Main NiceGUI Application for ER Analysis & Diagramming.

Converts requirement descriptions into structured ER models, provides
an interactive text highlighter, step-by-step methodologies, detailed justifications,
and interactive Crow's Foot ER diagrams.
"""

from typing import Optional
from nicegui import ui, app
import config
from models.registry import scenario_registry
import scenarios  # Initializes and registers all scenarios
from components import (
    renderHeader,
    renderMethodologyCards,
    renderInteractiveCanvas,
    renderAnalysisSection,
    renderMethodologyTable,
    renderERDiagram,
    renderRelationalAndSQL,
)


class ERApp:
    """Main application controller managing UI state and rendering."""

    def __init__(self) -> None:
        """Initializes the ER application with default scenario."""
        default_scenario = scenario_registry.getDefaultScenario()
        self.current_scenario_id = default_scenario.id if default_scenario else "research_institute"

    def selectScenario(self, scenario_id: str, content_container: ui.column) -> None:
        """Switches the active scenario and re-renders the main content area.

        Args:
            scenario_id (str): The ID of the scenario to switch to.
            content_container (ui.column): The container element holding dynamic content.

        Returns:
            None
        """
        self.current_scenario_id = scenario_id
        content_container.clear()
        with content_container:
            self.renderScenarioContent()
        ui.run_javascript("setTimeout(() => { if (typeof updateCanvasHighlights === 'function') updateCanvasHighlights(); if (typeof initERDiagram === 'function') initERDiagram(); }, 50);")

    def renderScenarioContent(self) -> None:
        """Renders the active scenario content sections."""
        scenario = scenario_registry.getScenario(self.current_scenario_id)
        if not scenario:
            ui.label("Το επιλεγμένο σενάριο δεν βρέθηκε.").classes("text-red-400 p-4")
            return

        with ui.column().classes("w-full max-w-6xl mx-auto px-4 py-8 space-y-10"):
            # SECTION 1: Methodology Quick Guide
            renderMethodologyCards()

            # SECTION 2: Interactive Text Highlighter Canvas
            renderInteractiveCanvas(scenario)

            # SECTION 3: Detailed Analysis & Justifications
            renderAnalysisSection(scenario)

            # SECTION 4: General Methodology Table
            renderMethodologyTable()

            # SECTION 5: Interactive E-R Diagram
            renderERDiagram(scenario)

            # SECTION 6: Relational Mapping & SQL DDL
            renderRelationalAndSQL(scenario)


def buildApp() -> None:
    """Builds the main NiceGUI web page layout and routes."""
    # Inject design tokens and custom styles
    ui.add_head_html(f"<style>{config.CUSTOM_CSS}</style>", shared=True)

    er_app = ERApp()

    @ui.page("/")
    def mainPage() -> None:
        """Root page handler rendering header and reactive content."""
        current_scenario = scenario_registry.getScenario(er_app.current_scenario_id)
        content_container = ui.column().classes("w-full gap-0 p-0 items-center")

        def handleScenarioSwitch(new_id: str) -> None:
            """Handles scenario selection event."""
            er_app.selectScenario(new_id, content_container)
            new_scenario = scenario_registry.getScenario(new_id)
            if new_scenario:
                header_refs["subtitle_label"].set_text(new_scenario.subtitle)
                header_refs["course_label"].set_text(new_scenario.course_tag)

        # Top Header (Direct page child)
        header_refs = renderHeader(current_scenario, handleScenarioSwitch)

        # Main Dynamic Content Area
        with content_container:
            er_app.renderScenarioContent()


buildApp()

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(
        title="Οδηγός Ανάλυσης ER & Διαδραστικό Canvas",
        port=8080,
        reload=False,
        dark=True,
    )
