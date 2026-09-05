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
    renderTheoryPage,
)


class ERApp:
    """Main application controller managing UI state and rendering."""

    def __init__(self) -> None:
        """Initializes the ER application with default scenario."""
        default_scenario = scenario_registry.getDefaultScenario()
        self.current_scenario_id = default_scenario.id if default_scenario else "research_institute"

    def selectScenario(self, scenario_id: str, content_container: ui.column) -> None:
        """Switches the active scenario or theory page and re-renders the content area.

        Args:
            scenario_id (str): The ID of the scenario or 'theory' to switch to.
            content_container (ui.column): The container element holding dynamic content.

        Returns:
            None
        """
        self.current_scenario_id = scenario_id
        content_container.clear()
        with content_container:
            self.renderScenarioContent()
        ui.run_javascript(
            "setTimeout(() => { if (typeof updateCanvasHighlights === 'function') updateCanvasHighlights(); if (typeof initERDiagram === 'function') initERDiagram(); }, 50);"
        )

    def renderScenarioContent(self) -> None:
        """Renders the active scenario content sections or the compiled theory page."""
        if self.current_scenario_id == "theory":
            renderTheoryPage()
            return

        scenario = scenario_registry.getScenario(self.current_scenario_id)
        if not scenario:
            ui.label("The selected scenario was not found.").classes("text-red-500 p-4")
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
    # Inject design tokens, custom styles, and theme switcher logic
    ui.add_head_html(f"<style>{config.CUSTOM_CSS}</style>", shared=True)
    ui.add_head_html(config.THEME_HEAD_SCRIPT, shared=True)

    er_app = ERApp()

    @ui.page("/")
    def mainPage() -> None:
        """Root page handler rendering header and reactive content."""
        # Initialize default light theme mode
        ui.dark_mode(value=False)

        current_scenario = scenario_registry.getScenario(er_app.current_scenario_id)
        content_container = ui.column().classes("w-full gap-0 p-0 items-center")

        def handleScenarioSwitch(new_id: str) -> None:
            """Handles scenario selection event."""
            er_app.selectScenario(new_id, content_container)
            if new_id == "theory":
                header_refs["subtitle_label"].set_text("Complete Theory, Methodology & Crow's Foot Notations")
                header_refs["course_label"].set_text("Theory / Guide")
            else:
                new_scenario = scenario_registry.getScenario(new_id)
                if new_scenario:
                    header_refs["subtitle_label"].set_text(new_scenario.subtitle)
                    header_refs["course_label"].set_text(new_scenario.course_tag)

        # Top Header (Direct page child)
        header_refs = renderHeader(current_scenario, er_app.current_scenario_id, handleScenarioSwitch)

        # Main Dynamic Content Area
        with content_container:
            er_app.renderScenarioContent()


buildApp()

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(
        title="ER Analysis Guide & Interactive Canvas",
        port=8080,
        reload=False,
        dark=False,
    )
