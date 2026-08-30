"""Main NiceGUI Application for Computer Networks Interactive Learning & Exams.

Provides an interactive learning environment for Computer Networks theory,
problem-solving methodologies, nodal delay calculations, routing algorithms,
interactive SVG network topologies, and past/synthetic exam papers.
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
    renderNetworkDiagram,
    renderCalculators,
    renderTheoryPage,
)


class NetworkingApp:
    """Main application controller managing UI state and reactive view rendering."""

    def __init__(self) -> None:
        """Initializes the Networking application with default scenario."""
        default_scenario = scenario_registry.getDefaultScenario()
        self.current_topic_id = default_scenario.id if default_scenario else "exam_past_2023_2024"

    def selectTopic(self, topic_id: str, content_container: ui.column) -> None:
        """Switches the active scenario or theory page and re-renders the content area.

        Args:
            topic_id (str): The ID of the scenario or theory topic to switch to.
            content_container (ui.column): The container element holding dynamic content.

        Returns:
            None
        """
        self.current_topic_id = topic_id
        content_container.clear()
        with content_container:
            self.renderContent()
        ui.run_javascript(
            "setTimeout(() => { if (typeof updateCanvasHighlights === 'function') updateCanvasHighlights(); }, 50);"
        )

    def renderContent(self) -> None:
        """Renders the active scenario content sections or the compiled theory page."""
        if self.current_topic_id.startswith("theory_") or self.current_topic_id.startswith("topic_"):
            renderTheoryPage(self.current_topic_id)
            return

        scenario = scenario_registry.getScenario(self.current_topic_id)
        if not scenario:
            ui.label("Το επιλεγμένο θέμα / σενάριο δεν βρέθηκε.").classes("text-red-400 p-4")
            return

        with ui.column().classes("w-full max-w-6xl mx-auto px-4 py-8 space-y-10"):
            # SECTION 1: Methodology Quick Formula Cards
            renderMethodologyCards()

            # SECTION 2: Interactive Text Highlighter Canvas
            renderInteractiveCanvas(scenario)

            # SECTION 3: Detailed Question Analysis & Justifications
            renderAnalysisSection(scenario)

            # SECTION 4: Comparative Methodology Tables
            renderMethodologyTable()

            # SECTION 5: Interactive SVG Network Topology
            if scenario.nodes:
                renderNetworkDiagram(scenario)

            # SECTION 6: Embedded Interactive Calculators
            renderCalculators()


def buildApp() -> None:
    """Builds the main NiceGUI web page layout and routes."""
    # Inject design tokens and custom styles
    ui.add_head_html(f"<style>{config.CUSTOM_CSS}</style>", shared=True)

    net_app = NetworkingApp()

    @ui.page("/")
    def mainPage() -> None:
        """Root page handler rendering header and reactive content."""
        current_scenario = scenario_registry.getScenario(net_app.current_topic_id)
        content_container = ui.column().classes("w-full gap-0 p-0 items-center")

        def handleTopicSwitch(new_id: str) -> None:
            """Handles topic / scenario selection event."""
            net_app.selectTopic(new_id, content_container)
            if new_id.startswith("theory_") or new_id.startswith("topic_"):
                header_refs["subtitle_label"].set_text("Πλήρης Θεωρία, Μεθοδολογία & Διαδραστικά Εργαλεία")
                header_refs["course_label"].set_text("Θεωρία / Οδηγός")
            else:
                new_scenario = scenario_registry.getScenario(new_id)
                if new_scenario:
                    header_refs["subtitle_label"].set_text(new_scenario.subtitle)
                    header_refs["course_label"].set_text(new_scenario.course_tag)

        # Top Header
        header_refs = renderHeader(current_scenario, net_app.current_topic_id, handleTopicSwitch)

        # Main Dynamic Content Area
        with content_container:
            net_app.renderContent()


buildApp()

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(
        title="Δίκτυα Υπολογιστών: Διαδραστικός Οδηγός & Εξετάσεις",
        port=8081,
        reload=False,
        dark=True,
    )
