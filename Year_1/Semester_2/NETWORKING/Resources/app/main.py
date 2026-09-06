"""Main NiceGUI application for the Computer Networks exam solutions guide.

# Archetype: B — Multi-Part Exam / Problem Set (Computer Networks)
# Rationale: the course's exams (the discovered practice exam and the course
# exercise sets) consist of distinct multi-part Themata with MCQ sub-questions
# and computational exercises rather than one continuous requirements
# narrative. The canvas therefore carries the complete original exam paper
# verbatim, and each question is solved below it as an open, annotated sheet.

Converts the course's exam papers into a paper-first master solution sheet:
full exam transcription with hover-to-explain highlights, step-by-step worked
solutions with KaTeX derivations, interactive diagrams, verification code,
and a comprehensive master theory guide.
"""

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
    renderVisualDiagram,
    renderSolutionCode,
    renderTheoryPage,
)


class NetworkingApp:
    """Main application controller managing UI state and rendering."""

    def __init__(self) -> None:
        """Initializes the networks application with the default scenario."""
        default_scenario = scenario_registry.getDefaultScenario()
        self.current_scenario_id = default_scenario.id if default_scenario else "theory"

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
        # Re-invoke every global renderer after a content re-render
        ui.run_javascript(
            "setTimeout(() => { "
            "if (typeof syncThemeUI === 'function') syncThemeUI(); "
            "if (typeof updateCanvasHighlights === 'function') updateCanvasHighlights(); "
            "if (typeof initExamDiagram === 'function') initExamDiagram(); "
            "if (typeof renderAllLatex === 'function') renderAllLatex(); "
            "}, 80);"
        )

    def renderScenarioContent(self) -> None:
        """Renders the active scenario content sections or the compiled theory page."""
        if self.current_scenario_id == "theory":
            renderTheoryPage()
            return

        scenario = scenario_registry.getScenario(self.current_scenario_id)
        if not scenario:
            ui.label("Το επιλεγμένο σενάριο δεν βρέθηκε.").classes("text-red-500 p-4")
            return

        with ui.column().classes("w-full max-w-6xl mx-auto px-4 py-8 space-y-10"):
            # SECTION 1: Methodology Quick Guide
            renderMethodologyCards()

            # SECTION 2: Complete Original Exam Paper (Interactive Canvas)
            renderInteractiveCanvas(scenario)

            # SECTION 3: Open Per-Question Solution Sheets (same paper structure)
            renderAnalysisSection(scenario)

            # SECTION 4: General Methodology Table
            renderMethodologyTable()

            # SECTION 5: Interactive SVG Diagram (VLSM map / topology / path)
            renderVisualDiagram(scenario)

            # SECTION 6: Solution Rationale & Verification Code
            renderSolutionCode(scenario)


def buildApp() -> None:
    """Builds the main NiceGUI web page layout and routes."""
    # Inject design tokens, KaTeX, custom styles, and theme switcher logic
    ui.add_head_html(f"<style>{config.CUSTOM_CSS}</style>", shared=True)
    ui.add_head_html(config.KATEX_HEAD, shared=True)
    ui.add_head_html(config.THEME_HEAD_SCRIPT, shared=True)

    net_app = NetworkingApp()

    @ui.page("/")
    def mainPage() -> None:
        """Root page handler rendering header and reactive content."""
        current_scenario = scenario_registry.getScenario(net_app.current_scenario_id)
        content_container = ui.column().classes("w-full gap-0 p-0 items-center")

        def handleScenarioSwitch(new_id: str) -> None:
            """Handles scenario selection event."""
            net_app.selectScenario(new_id, content_container)
            if new_id == "theory":
                header_refs["subtitle_label"].set_text("Πλήρης Θεωρία, Τύποι, Αλγόριθμοι & Παγίδες Εξετάσεων")
                header_refs["course_label"].set_text("Θεωρία / Οδηγός")
            else:
                new_scenario = scenario_registry.getScenario(new_id)
                if new_scenario:
                    header_refs["subtitle_label"].set_text(new_scenario.subtitle)
                    header_refs["course_label"].set_text(new_scenario.course_tag)

        # Top header (direct page child)
        header_refs = renderHeader(current_scenario, net_app.current_scenario_id, handleScenarioSwitch)

        # Main dynamic content area
        with content_container:
            net_app.renderScenarioContent()

        # Synchronize theme and render LaTeX formulas upon client connection
        ui.timer(
            0.15,
            lambda: ui.run_javascript(
                "if (typeof setAppTheme === 'function') setAppTheme(getAppTheme()); "
                "if (typeof updateCanvasHighlights === 'function') updateCanvasHighlights(); "
                "if (typeof initExamDiagram === 'function') initExamDiagram(); "
                "if (typeof renderAllLatex === 'function') renderAllLatex(); "
            ),
            once=True,
        )


buildApp()

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(
        title="Δίκτυα Υπολογιστών: Λυμένες Εξετάσεις & Θεωρία",
        port=8080,
        reload=False,
        dark=False,
    )
