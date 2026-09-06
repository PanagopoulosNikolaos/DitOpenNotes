"""Main NiceGUI Application for Digital Electronics Exam Preparation & Theory.

ARCHETYPE B RATIONALE:
Course classified as Archetype B (Multi-Part Exam / Problem Set).
Examinations comprise distinct computational and synthesis problems covering
2's complement arithmetic, Karnaugh map minimization, universal logic synthesis,
synchronous FSM sequence detectors, counters, and VHDL hardware descriptions.
The canvas presents the complete original exam text verbatim with three-part contract
hover tooltips, followed sequentially by open, fully worked solution sheets with
step-by-step KaTeX derivations and logic diagrams.
"""

from nicegui import Client, ui
import config
from models.registry import scenario_registry
import scenarios  # Auto-registers all past and synthetic exams
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


class DigitalElectronicsApp:
    """Main application controller managing UI state and reactive rendering."""

    def __init__(self) -> None:
        """Initializes the Digital Electronics application with default scenario."""
        default_scenario = scenario_registry.getDefaultScenario()
        self.current_scenario_id = default_scenario.id if default_scenario else "practice_exam_01_core"

    def selectScenario(self, scenario_id: str, content_container: ui.column) -> None:
        """Switches active scenario or opens Theory Guide, re-rendering content.

        Args:
            scenario_id (str): The ID of the scenario or 'theory' to display.
            content_container (ui.column): Container holding dynamic page content.

        Returns:
            None
        """
        self.current_scenario_id = scenario_id
        content_container.clear()
        with content_container:
            self.renderScenarioContent()

        # Trigger KaTeX LaTeX rendering and sync canvas highlights after DOM update
        ui.run_javascript(
            "setTimeout(() => {"
            " if (typeof renderAllLatex === 'function') renderAllLatex();"
            " if (typeof updateCanvasHighlights === 'function') updateCanvasHighlights();"
            "}, 80);"
        )

    def renderScenarioContent(self) -> None:
        """Renders the active scenario sequential sections or the master theory handbook."""
        if self.current_scenario_id == "theory":
            renderTheoryPage()
            return

        scenario = scenario_registry.getScenario(self.current_scenario_id)
        if not scenario:
            ui.label("Το επιλεγμένο θέμα εξέτασης δεν βρέθηκε.").classes("text-red-500 p-4")
            return

        with ui.column().classes("w-full max-w-6xl mx-auto px-4 py-8 space-y-10 latex-target"):
            # SECTION 1: Methodology Quick Guide Cards
            renderMethodologyCards()

            # SECTION 2: Interactive Text Highlighter Canvas (Complete Verbatim Exam)
            renderInteractiveCanvas(scenario)

            # SECTION 3: Open Detailed Question Analysis & Solutions (No Accordions)
            renderAnalysisSection(scenario)

            # SECTION 4: Comparative Methodology Table
            renderMethodologyTable()

            # SECTION 5: Interactive SVG FSM / Circuit Diagram
            renderVisualDiagram(scenario)

            # SECTION 6: Python Verification Code & Hardware Rationale Cards
            renderSolutionCode(scenario)


def buildApp() -> None:
    """Configures global styles, scripts, and root route layout."""
    # Inject KaTeX LaTeX CDN, canvas scripts, theme switcher, and design tokens
    ui.add_head_html(f"<style>{config.CUSTOM_CSS}</style>", shared=True)
    ui.add_head_html(config.KATEX_AND_SCRIPTS_HEAD, shared=True)

    de_app = DigitalElectronicsApp()

    @ui.page("/")
    async def mainPage(client: Client) -> None:
        """Root page handler rendering sticky header and dynamic content."""
        # Initialize default Orange Light theme
        ui.dark_mode(value=False)

        current_scenario = scenario_registry.getScenario(de_app.current_scenario_id)
        content_container = ui.column().classes("w-full gap-0 p-0 items-center min-h-screen")

        header_refs: dict = {}

        def handleScenarioSwitch(new_id: str) -> None:
            """Handles scenario selection change event."""
            de_app.selectScenario(new_id, content_container)
            if new_id == "theory":
                header_refs["subtitle_label"].set_text("Πλήρης Θεωρία, Συνδυαστικά/Ακολουθιακά Κυκλώματα, FSM & VHDL")
                header_refs["course_label"].set_text("Θεωρία / Οδηγός")
            else:
                sc = scenario_registry.getScenario(new_id)
                if sc:
                    header_refs["subtitle_label"].set_text(sc.subtitle)
                    header_refs["course_label"].set_text(sc.course_tag)

        # Header with single dropdown scenario selector and theme toggle
        header_refs_dict = renderHeader(
            current_scenario,
            de_app.current_scenario_id,
            handleScenarioSwitch,
        )
        header_refs.update(header_refs_dict)

        # Main dynamic content container
        with content_container:
            de_app.renderScenarioContent()

        await client.connected()
        ui.run_javascript("if (typeof renderAllLatex === 'function') renderAllLatex();")


buildApp()

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(
        title="Ψηφιακά Ηλεκτρονικά — Master Study & Exam Guide",
        port=8080,
        reload=False,
        dark=False,
    )

