"""Components package initialization."""

from .header import renderHeader
from .methodology_card import renderMethodologyCards
from .interactive_canvas import renderInteractiveCanvas
from .analysis_section import renderAnalysisSection
from .methodology_table import renderMethodologyTable
from .visual_diagram import renderVisualDiagram
from .solution_code import renderSolutionCode
from .theory_page import renderTheoryPage

__all__ = [
    "renderHeader",
    "renderMethodologyCards",
    "renderInteractiveCanvas",
    "renderAnalysisSection",
    "renderMethodologyTable",
    "renderVisualDiagram",
    "renderSolutionCode",
    "renderTheoryPage",
]
