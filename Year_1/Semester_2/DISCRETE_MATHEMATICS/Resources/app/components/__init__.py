"""Components package initialization for Discrete Mathematics app."""

from components.header import renderHeader
from components.methodology_card import renderMethodologyCards
from components.interactive_canvas import renderInteractiveCanvas
from components.analysis_section import renderAnalysisSection, renderQuestionSolution
from components.methodology_table import renderMethodologyTable
from components.visual_diagram import renderVisualDiagram
from components.solution_code import renderSolutionCode
from components.theory_page import renderTheoryPage

__all__ = [
    "renderHeader",
    "renderMethodologyCards",
    "renderInteractiveCanvas",
    "renderAnalysisSection",
    "renderQuestionSolution",
    "renderMethodologyTable",
    "renderVisualDiagram",
    "renderSolutionCode",
    "renderTheoryPage",
]
