"""Main NiceGUI Application for Electromagnetics Exam Preparation & Theory.

ARCHETYPE B RATIONALE:
Course classified as Archetype B (Multi-Part Exam / Problem Set).
Examinations comprise distinct multiple-choice theory prompts and multi-part
computational exercises on Maxwell equations, Gauss divergence, sinusoidal plane
waves, and Poynting vectors. The canvas presents the complete original exam text
verbatim with three-part contract hover tooltips, followed sequentially by open,
fully worked solution sheets with step-by-step KaTeX derivations.
"""

from nicegui import ui
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


class ElectromagneticsApp:
    """Main application controller managing UI state and reactive rendering."""

    def __init__(self) -> None:
        """Initializes the Electromagnetics application with default scenario."""
        default_scenario = scenario_registry.getDefaultScenario()
        self.current_scenario_id = default_scenario.id if default_scenario else "past_exam_2024_09_team_b"

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

            # SECTION 5: Interactive SVG Field & Wave Diagram
            renderVisualDiagram(scenario)

            # SECTION 6: Python SymPy Verification Code & Rationale Cards
            renderSolutionCode(scenario)


def buildApp() -> None:
    """Configures global styles, scripts, and root route layout."""
    # Inject KaTeX LaTeX CDN, canvas scripts, theme switcher, and design tokens
    ui.add_head_html(f"<style>{config.CUSTOM_CSS}</style>", shared=True)
    ui.add_head_html(config.KATEX_AND_SCRIPTS_HEAD, shared=True)

    em_app = ElectromagneticsApp()

    @ui.page("/")
    def mainPage() -> None:
        """Root page handler rendering sticky header and dynamic content."""
        # Initialize default Orange Light theme
        ui.dark_mode(value=False)

        current_scenario = scenario_registry.getScenario(em_app.current_scenario_id)
        content_container = ui.column().classes("w-full gap-0 p-0 items-center min-h-screen")

        header_refs: dict = {}

        def handleScenarioSwitch(new_id: str) -> None:
            """Handles scenario selection change event."""
            em_app.selectScenario(new_id, content_container)
            if new_id == "theory":
                header_refs["subtitle_label"].set_text("Πλήρης Θεωρία, Εξισώσεις Maxwell & Κυματική Διάδοση")
                header_refs["course_label"].set_text("Θεωρία / Οδηγός")
            else:
                sc = scenario_registry.getScenario(new_id)
                if sc:
                    header_refs["subtitle_label"].set_text(sc.subtitle)
                    header_refs["course_label"].set_text(sc.course_tag)

        # Header with single dropdown scenario selector and theme toggle
        header_refs_dict = renderHeader(
            current_scenario,
            em_app.current_scenario_id,
            handleScenarioSwitch,
        )
        header_refs.update(header_refs_dict)

        # Main dynamic content container
        with content_container:
            em_app.renderScenarioContent()


buildApp()

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(
        title="Αρχές Ηλεκτρομαγνητισμού & Τηλεπικοινωνιών — Study Guide",
        port=8080,
        reload=False,
        dark=False,
    )

