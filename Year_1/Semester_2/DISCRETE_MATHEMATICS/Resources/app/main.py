"""Discrete Mathematics Educational Application (Course 203) - Main Entry Point.

Implements Archetype B (Multi-Part Exam / Problem Set Study Sheet) in NiceGUI:
- Verbatim original exam papers with 3-part interactive highlights and tooltips
- Open stacked master solution sheets with complete KaTeX step-by-step derivations
- Comprehensive Master Theory Guide for 100/100 score coverage
- Visual graph and automata SVG canvas
- Python computational verification code
- Dual themes (Orange Light default and Soft Dark)
- Zero collapsibles, zero accordions, zero Unicode emojis.
"""

import os
import sys
from typing import Optional

# Ensure app directory is in sys.path for direct invocation from repository root
_app_dir = os.path.dirname(os.path.abspath(__file__))
if _app_dir not in sys.path:
    sys.path.insert(0, _app_dir)

from nicegui import ui, app

from config import CUSTOM_CSS, KATEX_AND_SCRIPTS_HEAD
from models.scenario import Scenario
from models.registry import scenario_registry
import scenarios  # Triggers auto-registration of all 11 scenarios
from components import (
    renderHeader,
    renderMethodologyCards,
    renderInteractiveCanvas,
    renderAnalysisSection,
    renderMethodologyTable,
    renderVisualDiagram,
    renderSolutionCode,
    renderTheoryPage,
)


class DiscreteMathematicsApp:
    """Main application controller managing reactive state, scenario navigation, and UI views."""

    def __init__(self) -> None:
        """Initializes application controller with default scenario."""
        default_scenario = scenario_registry.getDefaultScenario()
        self.active_scenario_id: str = default_scenario.id if default_scenario else "final_exam_2025_june"
        self.content_container: Optional[ui.column] = None
        self.header_refs: dict = {}

    def changeScenario(self, scenario_id: str) -> None:
        """Switches the active view to a new exam scenario or the master theory guide.

        Args:
            scenario_id (str): Unique identifier of target scenario or 'theory'.

        Returns:
            None
        """
        self.active_scenario_id = scenario_id
        self.renderActiveContent()

        # Update header labels if references exist
        if "selector" in self.header_refs:
            self.header_refs["selector"].value = scenario_id

        if scenario_id == "theory":
            if "course_label" in self.header_refs:
                self.header_refs["course_label"].text = "Θεωρία / Οδηγός"
            if "subtitle_label" in self.header_refs:
                self.header_refs["subtitle_label"].text = "Πλήρης Θεωρία & Μεθοδολογία για το 100/100 (Όλη η Ύλη Τζίμα)"
        else:
            scenario = scenario_registry.getScenario(scenario_id)
            if scenario:
                if "course_label" in self.header_refs:
                    self.header_refs["course_label"].text = scenario.course_tag
                if "subtitle_label" in self.header_refs:
                    self.header_refs["subtitle_label"].text = scenario.subtitle

        # Re-trigger KaTeX rendering on new DOM elements
        ui.run_javascript("setTimeout(renderAllLatex, 60);")

    def renderActiveContent(self) -> None:
        """Clears and re-renders the main content container based on active view state.

        Returns:
            None
        """
        if self.content_container is None:
            return

        self.content_container.clear()

        with self.content_container:
            if self.active_scenario_id == "theory":
                renderTheoryPage()
            else:
                scenario = scenario_registry.getScenario(self.active_scenario_id)
                if scenario is None:
                    ui.label("Το επιλεγμένο θέμα δεν βρέθηκε.").classes("text-red-500 font-bold p-8 text-center")
                    return

                # Archetype B Master Layout
                # 1. Sequential Methodology Quick Guidance Cards
                renderMethodologyCards()

                # 2. Verbatim Interactive Exam Canvas (3-part tooltips, filter chips, visual legend)
                renderInteractiveCanvas(scenario)

                # 3. Open Stacked Question Solution Sheet (No accordions, open KaTeX steps)
                renderAnalysisSection(scenario)

                # 4. Textual Trigger Recognition & Trap Prevention Table
                renderMethodologyTable()

                # 5. Interactive SVG Graph / Automata Structure Diagram
                renderVisualDiagram(scenario)

                # 6. Design Justification Cards & Python Verification Script
                renderSolutionCode(scenario)

    def buildUi(self) -> None:
        """Builds page structure, registers headers, styles, and initializes view.

        Returns:
            None
        """
        # Inject CSS styles and KaTeX scripts into HTML head
        ui.add_head_html(f"<style>{CUSTOM_CSS}</style>\n{KATEX_AND_SCRIPTS_HEAD}")

        active_scenario = scenario_registry.getScenario(self.active_scenario_id)

        # Sticky Header with Scenario Selector and Theme Switcher
        self.header_refs = renderHeader(
            scenario=active_scenario,
            selected_scenario_id=self.active_scenario_id,
            on_scenario_change=self.changeScenario,
        )

        # Main Content Reactive Container
        with ui.column().classes("w-full max-w-7xl mx-auto px-4 py-8 space-y-8 min-w-0 max-w-full overflow-x-hidden").props('id="main-app-container"'):
            self.content_container = ui.column().classes("w-full max-w-full min-w-0 space-y-8")
            self.renderActiveContent()


@ui.page("/")
def indexPage() -> None:
    """Root route handler initializing application controller instance.

    Returns:
        None
    """
    app_instance = DiscreteMathematicsApp()
    app_instance.buildUi()


def main() -> None:
    """Application entry point function configuring and launching NiceGUI server."""
    ui.run(
        title="Διακριτά Μαθηματικά — Μεθοδολογικός Οδηγός & Λύσεις Εξετάσεων",
        port=8080,
        reload=False,
        show=False,
    )


if __name__ in {"__main__", "__mp_main__"}:
    main()
