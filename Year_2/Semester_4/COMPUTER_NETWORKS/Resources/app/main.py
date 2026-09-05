"""Main NiceGUI Application for Computer Networks Interactive Learning & Exams.

Organized into two primary main modules:
1. Study Module: Comprehensive theory notes (Topics 1-7), exam cheat sheet, and interactive calculators.
2. Exams Module: Past exams (2023-2024, 2026 Team, Archive) and synthetic realistic exams with step-by-step solutions.

Includes full LaTeX math rendering support via KaTeX.
"""

from nicegui import ui, app
import config
from models.registry import scenario_registry
import scenarios  # Initializes and registers all scenarios
from components.header import _BTN_ACTIVE_CLASSES, _BTN_IDLE_CLASSES
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
        """Initializes the Networking application with default mode and submodules."""
        self.current_mode = "exams"  # 'study' or 'exams'
        self.current_study_sub_id = "theory_full_prep"
        self.current_exam_sub_id = "exam_past_2023_2024"

    def setMode(self, new_mode: str, content_container: ui.column, header_refs: dict) -> None:
        """Switches the primary application mode ('study' or 'exams').

        Args:
            new_mode (str): The mode to switch to ('study' or 'exams').
            content_container (ui.column): The container element holding dynamic content.
            header_refs (dict): References to header UI elements.

        Returns:
            None
        """
        if new_mode not in ("study", "exams") or new_mode == self.current_mode:
            return

        self.current_mode = new_mode
        sub_options = scenario_registry.getStudyOptions() if new_mode == "study" else scenario_registry.getExamOptions()
        current_sub = self.current_study_sub_id if new_mode == "study" else self.current_exam_sub_id

        # Update select options and active value
        header_refs["sub_select"].set_options(sub_options)
        header_refs["sub_select"].set_value(current_sub)

        # Update mode toggle button styling cleanly without destroying Quasar root classes
        is_study = (new_mode == "study")
        if is_study:
            header_refs["study_btn"].classes(remove=_BTN_IDLE_CLASSES, add=_BTN_ACTIVE_CLASSES)
            header_refs["exam_btn"].classes(remove=_BTN_ACTIVE_CLASSES, add=_BTN_IDLE_CLASSES)
        else:
            header_refs["study_btn"].classes(remove=_BTN_ACTIVE_CLASSES, add=_BTN_IDLE_CLASSES)
            header_refs["exam_btn"].classes(remove=_BTN_IDLE_CLASSES, add=_BTN_ACTIVE_CLASSES)

        self.updateHeaderLabels(header_refs)
        self.renderCurrentView(content_container, header_refs)

    def setSubModule(self, new_sub_id: str, content_container: ui.column, header_refs: dict) -> None:
        """Switches the active sub-module within the current mode.

        Args:
            new_sub_id (str): The sub-module ID to switch to.
            content_container (ui.column): The container element holding dynamic content.
            header_refs (dict): References to header UI elements.

        Returns:
            None
        """
        if not new_sub_id:
            return

        if self.current_mode == "study":
            self.current_study_sub_id = new_sub_id
        else:
            self.current_exam_sub_id = new_sub_id

        self.updateHeaderLabels(header_refs)
        self.renderCurrentView(content_container, header_refs)

    def updateHeaderLabels(self, header_refs: dict) -> None:
        """Updates header subtitle and badge according to current mode and sub-module."""
        if self.current_mode == "study":
            options = scenario_registry.getStudyOptions()
            title = options.get(self.current_study_sub_id, "Study Module")
            header_refs["subtitle_label"].set_text(f"Study Module: {title}")
            header_refs["badge_label"].set_text("Ενότητα: Study")
        else:
            scenario = scenario_registry.getScenario(self.current_exam_sub_id)
            if scenario:
                header_refs["subtitle_label"].set_text(scenario.subtitle)
                header_refs["badge_label"].set_text(f"Exams: {scenario.course_tag}")

    def renderCurrentView(self, content_container: ui.column, header_refs: dict) -> None:
        """Renders the active Study notes sub-module or Exam scenario into the container."""
        content_container.clear()
        with content_container:
            if self.current_mode == "study":
                def onStudySubChange(sub_id: str) -> None:
                    """Syncs internal tab clicks back to app state and header dropdown."""
                    if sub_id:
                        self.current_study_sub_id = sub_id
                        header_refs["sub_select"].set_value(sub_id)
                        self.updateHeaderLabels(header_refs)

                renderTheoryPage(
                    self.current_study_sub_id,
                    on_sub_change=onStudySubChange,
                )
            else:
                scenario = scenario_registry.getScenario(self.current_exam_sub_id)
                if not scenario:
                    ui.label("Το επιλεγμένο θέμα εξέτασης δεν βρέθηκε.").classes("text-red-400 p-4")
                    return

                with ui.column().classes("w-full max-w-6xl mx-auto px-4 py-6 space-y-8 latex-target"):
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

        # Re-trigger LaTeX rendering and highlight sync after DOM update
        ui.run_javascript(
            "setTimeout(() => {"
            " if (typeof renderAllLatex === 'function') renderAllLatex();"
            " if (typeof updateCanvasHighlights === 'function') updateCanvasHighlights();"
            "}, 80);"
        )


def buildApp() -> None:
    """Builds the main NiceGUI web page layout, LaTeX headers, and routes."""
    # Inject KaTeX LaTeX CDN, canvas JS, and custom styles — all once at startup
    ui.add_head_html(config.KATEX_HEAD_HTML, shared=True)
    ui.add_head_html(f"<style>{config.CUSTOM_CSS}</style>", shared=True)

    net_app = NetworkingApp()

    @ui.page("/")
    def mainPage() -> None:
        """Root page handler rendering header and reactive container."""
        content_container = ui.column().classes("w-full gap-0 p-0 items-center min-h-screen")
        current_scenario = scenario_registry.getScenario(net_app.current_exam_sub_id)

        header_refs: dict = {}

        def handleModeSwitch(mode: str) -> None:
            """Handles mode switch event (study vs exams)."""
            net_app.setMode(mode, content_container, header_refs)

        def handleSubSwitch(sub_id: str) -> None:
            """Handles sub-module switch event triggered by the header dropdown."""
            net_app.setSubModule(sub_id, content_container, header_refs)

        # Header with dual mode selector and sub-module dropdown
        header_refs_dict = renderHeader(
            net_app.current_mode,
            net_app.current_exam_sub_id if net_app.current_mode == "exams" else net_app.current_study_sub_id,
            handleModeSwitch,
            handleSubSwitch,
            current_scenario,
        )
        header_refs.update(header_refs_dict)

        # Initial Render
        net_app.renderCurrentView(content_container, header_refs)


buildApp()

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(
        title="Δίκτυα Υπολογιστών: Interactive Learning & Exams",
        port=8081,
        reload=False,
        dark=True,
    )
