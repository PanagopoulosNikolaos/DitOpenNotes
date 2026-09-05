"""Components package for Computer Networks application."""

from .header import renderHeader
from .methodology_card import renderMethodologyCards
from .interactive_canvas import renderInteractiveCanvas
from .analysis_section import renderAnalysisSection, renderQuestionBlock
from .methodology_table import renderMethodologyTable
from .network_diagram import renderNetworkDiagram, generateSvgTopology
from .interactive_calculators import (
    renderNodalDelayCalculator,
    renderCrcCalculator,
    renderSubnetCalculator,
    renderCalculators,
)
from .theory_page import renderTheoryPage

__all__ = [
    "renderHeader",
    "renderMethodologyCards",
    "renderInteractiveCanvas",
    "renderAnalysisSection",
    "renderQuestionBlock",
    "renderMethodologyTable",
    "renderNetworkDiagram",
    "generateSvgTopology",
    "renderNodalDelayCalculator",
    "renderCrcCalculator",
    "renderSubnetCalculator",
    "renderCalculators",
    "renderTheoryPage",
]
